# Module 16: Design TinyURL (URL Shortener)

## Topic 16.1: TinyURL System - Base62 Encoding & Key Generation

---

## 🎯 1. Title / Topic: TinyURL (URL Shortener System)

---

## 🐣 2. Samjhane ke liye (Simple Analogy):

TinyURL ek **Parking Valet Service** jaisa hai. Jaise aap apni **lambi car** (long URL: https://amazon.com/product/electronics/laptop/dell-inspiron-15-3000-series?color=black&storage=512gb) valet ko dete ho, wo aapko ek **chhota token** (short URL: bit.ly/abc123) deta hai. Jab wapas chahiye, token dikhao aur car mil jaati hai. Similarly, long URL ko short code mein convert karte hain (abc123), jab user short URL par click kare toh original URL mil jaye. Result: Twitter mein 280 characters limit, long URL nahi fit hota, short URL perfect.

---

## 📖 3. Technical Definition (Interview Answer):

**TinyURL** is a URL shortening service that converts long URLs into short, unique identifiers using Base62 encoding or Key Generation Service, stores the mapping in a database, and redirects users from short URL to original URL via HTTP 301/302 redirect.

**Key terms:**
- **Base62 Encoding:** Convert number to string using [a-z, A-Z, 0-9] (62 characters) - compact representation
- **Short Code:** 6-7 character unique identifier (e.g., "abc123") - 62^7 = 3.5 trillion combinations
- **Key Generation Service (KGS):** Pre-generate unique keys, avoid collisions
- **HTTP 301:** Permanent redirect (cached by browser) vs 302 (temporary, not cached)
- **Hash Collision:** Two URLs generate same short code (problem to solve)

---

## 🧠 4. Zaroorat Kyun Hai? (Why?):

**Main Problem:** Long URLs (100-200 characters) Twitter/SMS mein fit nahi hote (280 char limit). Share karna mushkil, ugly dikhte hain, tracking nahi kar sakte.

**Business Impact:** Bitly: 600M+ links shortened/month, $50M+ revenue from analytics. Twitter: Without URL shorteners, character limit would be useless (URLs consume 50% of tweet).

**Technical Benefits:**
- **Space Saving:** 200 char URL → 15 char short URL (93% reduction)
- **Analytics:** Click tracking, geographic data, referrer info (marketing insights)
- **Branding:** Custom domains (bit.ly/brand-name) - professional look
- **Expiry:** Temporary links (expire after 7 days) - security
- **QR Codes:** Short URLs → Small QR codes (easy to scan)

---

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario):

**Scenario: No URL Shortener**
- Marketing campaign: Share product link on Twitter
- Original URL: https://example.com/products/electronics/laptops/dell-inspiron-15-3000-series-intel-core-i5-8gb-ram-512gb-ssd?color=black&warranty=2years&discount=SAVE20
- Length: 180 characters
- Tweet limit: 280 characters
- Remaining: 100 characters for message (insufficient)
- Result: Can't add compelling text, low engagement, campaign fails

**Real Example:** **Twitter (Pre-2010)** - No built-in URL shortener → Users manually used bit.ly → Inconsistent experience → Twitter built t.co (2010) → All links auto-shortened → 30% increase in link clicks → Better analytics for advertisers.

---

## ⚙️ 6. Under the Hood (Technical Working):

**URL Shortening Flow:**

1. **User Input:** Long URL submit (https://example.com/very/long/url)
2. **Validation:** Check if URL valid (regex), not malicious (blacklist check)
3. **Check Existing:** Hash URL, check if already shortened (avoid duplicates)
4. **Generate Short Code:**
   - **Approach 1 (Base62):** Auto-increment ID (1, 2, 3...) → Base62 encode → "b", "c", "d"
   - **Approach 2 (KGS):** Pre-generated unique keys from Key Generation Service
5. **Store Mapping:** Database insert (short_code → long_url)
6. **Return:** Short URL (https://tiny.url/abc123)

**Redirect Flow:**

1. **User Clicks:** Short URL (https://tiny.url/abc123)
2. **Lookup:** Database query (short_code = "abc123")
3. **Fetch:** Original URL (https://example.com/very/long/url)
4. **Analytics:** Log click (timestamp, IP, referrer, user-agent)
5. **Redirect:** HTTP 301/302 to original URL
6. **Browser:** Loads original URL

**ASCII Architecture Diagram:**

```
SHORTENING FLOW:

[User]
  |
  | POST /shorten
  | Body: {"url": "https://example.com/very/long/url"}
  v
+------------------------+
| API Gateway            |
| (Rate Limit: 10/min)   |
+------------------------+
  |
  v
+------------------------+
| URL Shortener Service  |
+------------------------+
  |
  | (1) Validate URL
  v
+------------------------+
| Validation             |
| - Regex check          |
| - Blacklist check      |
+------------------------+
  |
  | (2) Check if exists
  v
+------------------------+
| Cache (Redis)          |
| hash(url) → short_code |
+------------------------+
  |
  +---> Cache HIT? → Return existing short_code
  |
  +---> Cache MISS? → Continue
  |
  v
+------------------------+
| Key Generation Service |
| (Pre-generated keys)   |
+------------------------+
  |
  | Get unique key: "abc123"
  v
+------------------------+
| Database (Write)       |
| INSERT INTO urls       |
| (short_code, long_url) |
+------------------------+
  |
  v
+------------------------+
| Cache Update           |
| Store mapping          |
+------------------------+
  |
  v
[Return: https://tiny.url/abc123]


REDIRECT FLOW:

[User clicks: https://tiny.url/abc123]
  |
  v
+------------------------+
| Load Balancer          |
+------------------------+
  |
  v
+------------------------+
| Redirect Service       |
+------------------------+
  |
  | (1) Extract short_code: "abc123"
  v
+------------------------+
| Cache (Redis)          |
| short_code → long_url  |
+------------------------+
  |
  +---> Cache HIT? → Return long_url
  |
  +---> Cache MISS? → Query DB
  |
  v
+------------------------+
| Database (Read)        |
| SELECT long_url        |
| WHERE short_code=...   |
+------------------------+
  |
  v
+------------------------+
| Analytics Service      |
| (Async - Kafka)        |
| Log: click, IP, time   |
+------------------------+
  |
  v
+------------------------+
| HTTP 301 Redirect      |
| Location: original_url |
+------------------------+
  |
  v
[Browser loads: https://example.com/very/long/url]
```

**Base62 Encoding Process:**

```
AUTO-INCREMENT ID → BASE62 ENCODE → SHORT CODE

Base62 Characters: [a-z, A-Z, 0-9] = 62 chars
Mapping: 0→a, 1→b, ..., 25→z, 26→A, ..., 51→Z, 52→0, ..., 61→9

Example 1:
ID = 125
125 ÷ 62 = 2 remainder 1
2 ÷ 62 = 0 remainder 2
Read bottom-up: 2, 1 → "cb" (c=2, b=1)

Example 2:
ID = 1000000
1000000 ÷ 62 = 16129 remainder 2
16129 ÷ 62 = 260 remainder 9
260 ÷ 62 = 4 remainder 12
4 ÷ 62 = 0 remainder 4
Read bottom-up: 4, 12, 9, 2 → "eMJc"

Length Calculation:
62^6 = 56 billion URLs (6 chars)
62^7 = 3.5 trillion URLs (7 chars)
```

---

## 🛠️ 7. Problems Solved:

- **Character Limit:** Long URLs fit in Twitter (280 chars), SMS (160 chars) → 93% space saved
- **Tracking:** Click analytics (who, when, where clicked) → Marketing insights (conversion tracking)
- **Branding:** Custom short domains (go.company.com/promo) → Professional, trustworthy
- **Security:** Expiring links (share sensitive doc for 24 hours) → Auto-delete after expiry
- **Readability:** Ugly URLs hidden (amazon.com/dp/B08N5WRWNW → amzn.to/3xYz) → Clean, shareable
- **QR Codes:** Short URLs → Smaller QR codes → Easier to scan

---

## 🌍 8. Real-World Example:

**Bitly:** 600M links shortened/month, 10B+ clicks/month. Scale: 100K requests/sec during peak. Implementation: Base62 encoding with auto-increment IDs, PostgreSQL for storage (sharded by short_code), Redis for caching (99% cache hit rate). Features: Custom domains (bit.ly/brand), link expiry, A/B testing (multiple URLs for same campaign), geographic analytics. Revenue: $50M+/year from premium analytics. Technology: Python backend, Cassandra for analytics (time-series data), Kafka for click stream. Without URL shortening, social media marketing would be 50% less effective (long URLs have 30% lower click rates).

---

## 🔧 9. Tech Stack / Tools:

- **PostgreSQL/MySQL:** Relational DB for URL mappings. Use for: ACID properties, simple schema (short_code, long_url, created_at). Index on short_code for fast lookup.

- **Redis:** Cache for hot URLs. Use for: 99% cache hit rate (popular links cached), <1ms latency. TTL for expiring links.

- **Cassandra:** Analytics storage. Use for: Time-series click data (billions of rows), write-heavy (10K clicks/sec), distributed.

- **Zookeeper:** Key Generation Service coordination. Use for: Distribute ID ranges to servers (Server1: 1-1M, Server2: 1M-2M), avoid collisions.

---

## 📐 10. Architecture/Formula:

**Short Code Length Calculation:**

```
Total_URLs = Base^Length

Where:
Base = 62 ([a-z, A-Z, 0-9])
Length = Number of characters in short code

Examples:
Length 6: 62^6 = 56,800,235,584 (56 billion URLs)
Length 7: 62^7 = 3,521,614,606,208 (3.5 trillion URLs)

For 1 billion URLs:
62^x = 1,000,000,000
x = log(1B) / log(62) = 9 / 1.79 = 5.02
Minimum length = 6 characters

Safety margin: Use 7 characters (3.5T capacity)
```

**Base62 Encoding Algorithm:**

```
function base62_encode(num):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    result = ""
    
    while num > 0:
        remainder = num % 62
        result = chars[remainder] + result
        num = num // 62
    
    return result if result else "a"

Example:
base62_encode(125) = "cb"
base62_encode(1000000) = "eMJc"
```

**Key Generation Service (Range-based):**

```
ZOOKEEPER COORDINATION:

+------------------+
| Zookeeper        |
| (Range Manager)  |
+------------------+
  |
  | Assign ranges
  v
+------------------+------------------+------------------+
| KGS Server-1     | KGS Server-2     | KGS Server-3     |
| Range: 1-1M      | Range: 1M-2M     | Range: 2M-3M     |
| Current: 500K    | Current: 1.5M    | Current: 2.2M    |
+------------------+------------------+------------------+

Flow:
1. KGS Server-1 starts → Request range from Zookeeper
2. Zookeeper assigns: 1 to 1,000,000
3. KGS Server-1 pre-generates keys: base62(1), base62(2), ..., base62(1M)
4. Store in memory queue (fast access)
5. API Server requests key → KGS returns "b" (ID=1)
6. When 80% consumed (800K used) → Request new range from Zookeeper
7. Zookeeper assigns: 3M to 4M (next available)

Benefits:
- No collisions (each server has unique range)
- Fast (pre-generated, no computation)
- Scalable (add more KGS servers)
```

**Database Schema:**

```sql
CREATE TABLE urls (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    short_code VARCHAR(10) UNIQUE NOT NULL,
    long_url TEXT NOT NULL,
    user_id BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NULL,
    click_count INT DEFAULT 0,
    INDEX idx_short_code (short_code),
    INDEX idx_user_id (user_id)
);

CREATE TABLE clicks (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    short_code VARCHAR(10) NOT NULL,
    clicked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45),
    user_agent TEXT,
    referrer TEXT,
    country VARCHAR(2),
    INDEX idx_short_code_time (short_code, clicked_at)
);

Sharding Strategy:
Shard by short_code (hash-based)
Shard_ID = hash(short_code) % num_shards

Example:
short_code = "abc123"
hash("abc123") = 987654
num_shards = 10
Shard_ID = 987654 % 10 = 4 → Store in Shard-4
```

---

## 💻 11. Code / Flowchart:

**Flowchart (URL Shortening):**

```
START: User submits long URL
  |
  v
[Validate URL]
Regex: ^https?://.*
  |
  +---> Invalid? → Return 400 error
  |
  +---> Valid? → Continue
  |
  v
[Check if already shortened]
hash = MD5(long_url)
Redis: GET "url_hash:{hash}"
  |
  +---> Exists? → Return existing short_code
  |
  +---> Not exists? → Continue
  |
  v
[Get unique key from KGS]
Request: GET /kgs/get_key
Response: {key: "abc123"}
  |
  v
[Store in Database]
INSERT INTO urls (short_code, long_url)
VALUES ("abc123", "https://...")
  |
  v
[Cache mapping]
Redis: SET "short:abc123" "https://..." EX 86400
Redis: SET "url_hash:{hash}" "abc123" EX 86400
  |
  v
[Return short URL]
Response: {"short_url": "https://tiny.url/abc123"}
  |
  v
END
```

**Code (Simplified TinyURL Service):**

```python
import hashlib
import redis
from typing import Optional

class TinyURL:
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379)
        self.base62_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.counter = 1000000  # Start from 1M (for demo)
    
    def base62_encode(self, num: int) -> str:
        """Convert number to base62 string"""
        if num == 0:
            return self.base62_chars[0]
        
        result = ""
        while num > 0:
            remainder = num % 62
            result = self.base62_chars[remainder] + result
            num = num // 62
        
        return result
    
    def shorten(self, long_url: str) -> str:
        """Shorten a long URL"""
        # Check if already shortened
        url_hash = hashlib.md5(long_url.encode()).hexdigest()
        cached = self.redis.get(f"url_hash:{url_hash}")
        
        if cached:
            return f"https://tiny.url/{cached.decode()}"
        
        # Generate short code
        self.counter += 1
        short_code = self.base62_encode(self.counter)
        
        # Store mapping (in production: database)
        self.redis.setex(f"short:{short_code}", 86400, long_url)  # 24h TTL
        self.redis.setex(f"url_hash:{url_hash}", 86400, short_code)
        
        return f"https://tiny.url/{short_code}"
    
    def redirect(self, short_code: str) -> Optional[str]:
        """Get original URL from short code"""
        # Check cache
        long_url = self.redis.get(f"short:{short_code}")
        
        if long_url:
            # Log analytics (async in production)
            self._log_click(short_code)
            return long_url.decode()
        
        return None  # Not found
    
    def _log_click(self, short_code: str):
        """Log click for analytics"""
        self.redis.incr(f"clicks:{short_code}")

# Usage
service = TinyURL()

# Shorten URL
long_url = "https://example.com/very/long/url/with/many/parameters"
short_url = service.shorten(long_url)
print(f"Short URL: {short_url}")  # https://tiny.url/eMJd

# Redirect
original = service.redirect("eMJd")
print(f"Original URL: {original}")  # https://example.com/...
```

---

## 📈 12. Trade-offs:

- **Gain:** Space saving (93% reduction), analytics tracking, branding | **Loss:** Extra redirect hop (50-100ms latency), dependency on service (service down = links broken)

- **Gain:** Base62 simple, sequential IDs predictable | **Loss:** Predictable = security risk (abc123 → try abc124, abc125 - enumerate all URLs), no randomness

- **Gain:** KGS pre-generated keys (fast, no collision) | **Loss:** Extra service to maintain, range exhaustion handling, Zookeeper dependency

- **When to use:** Social media sharing, SMS campaigns, QR codes, analytics needed | **When to skip:** Internal links (no need to shorten), SEO-critical pages (direct URLs better for search engines)

---

## 🐞 13. Common Mistakes:

- **Mistake:** Using MD5 hash first 7 chars as short code
  - **Why wrong:** Collision possible (2 URLs → same 7 chars), birthday paradox (56B combinations but collision at ~250K URLs)
  - **What happens:** User clicks short URL, gets wrong destination (security issue)
  - **Fix:** Use auto-increment ID + Base62 or KGS (guaranteed unique)

- **Mistake:** No caching (every redirect queries database)
  - **Why wrong:** Database overload (10K redirects/sec = 10K DB queries), slow (50ms DB vs 1ms Redis)
  - **What happens:** High latency, database crash during traffic spike
  - **Fix:** Redis cache with 99% hit rate (popular URLs cached)

- **Mistake:** HTTP 301 (permanent redirect) for all URLs
  - **Why wrong:** Browser caches 301 → Analytics not tracked (subsequent clicks don't hit server)
  - **What happens:** Click count inaccurate, can't update destination URL
  - **Fix:** Use 302 (temporary) for analytics, 301 only for permanent URLs

- **Mistake:** No expiry for temporary links
  - **Why wrong:** Sensitive links (password reset) active forever → Security risk
  - **What happens:** Old link leaked → Unauthorized access
  - **Fix:** Expiry timestamp in DB, cron job deletes expired (or TTL in Redis)

---

## ✅ 14. Zaroori Notes for Interview:

**Must Mention Points:**
1. **Start with requirements:** "TinyURL ko 2 main operations hain - Shorten (long → short) aur Redirect (short → long). Scale: 100M URLs, 10K requests/sec. Latency: <100ms."

2. **Explain Base62:** "Auto-increment ID (1, 2, 3...) ko Base62 encode karte hain. 62 characters [a-z, A-Z, 0-9]. 7 chars = 62^7 = 3.5 trillion URLs. Formula: ID ÷ 62 repeatedly, remainders se string banao."

3. **Draw architecture:** User → API → KGS (get key) → Database (store mapping) → Redis (cache) → Return short URL. Redirect: User → Redis (cache lookup) → Database (if miss) → HTTP 302 → Original URL.

4. **Common follow-ups:**
   - **"Collision kaise handle karoge?"** → KGS use karo (pre-generated unique keys, no collision) ya Auto-increment ID (guaranteed unique). MD5 hash avoid karo (collision possible).
   - **"Scale kaise karoge (1B URLs)?"** → Database sharding (hash-based on short_code), Redis cluster for cache, multiple KGS servers with Zookeeper coordination.
   - **"Analytics kaise track karoge?"** → Async logging (Kafka), separate Cassandra DB for clicks (time-series), don't block redirect flow.
   - **"Custom short URLs kaise (bit.ly/my-brand)?"** → Check if custom code available (not taken), reserve it, store mapping. Collision check needed.

5. **Mention 301 vs 302:** "301 = Permanent (browser cache, no analytics). 302 = Temporary (hit server every time, analytics tracked). Use 302 for tracking."

6. **Pro tip:** "Interview mein Base62 encoding ka example do (125 → 'cb'). Interviewer ko dikhao ki math samajhte ho. Aur KGS mention karo (shows distributed system knowledge)."

---

## ❓ 15. FAQ & Comparisons (MANDATORY - 5 Questions):

**Q1: Base62 encoding vs MD5 hash - Kaunsa better for short code generation?**
A: **Base62 (Auto-increment ID):** Guaranteed unique (ID unique hai), short (7 chars for 3.5T URLs), sequential (predictable - security concern). **MD5 Hash:** Random (not predictable), but collision possible (birthday paradox - 2^64 hashes but collision at 2^32 ≈ 4B). **Best:** Base62 with auto-increment for uniqueness, add random salt if security needed. **Production:** Bitly uses Base62, Google (goo.gl) used Base62. MD5 avoid karo for primary key.

**Q2: Key Generation Service (KGS) vs On-demand generation - Trade-off?**
A: **KGS:** Pre-generated keys (fast - no computation), no collision (ranges assigned), scalable (multiple KGS servers). But extra service (complexity), range management (Zookeeper needed). **On-demand:** Simple (no extra service), generate when needed (Base62 encode ID). But slower (computation per request), potential collision if distributed (need distributed counter). **Best:** KGS for high scale (>10K req/sec), On-demand for small scale (<1K req/sec). **Bitly:** Uses KGS for 100K req/sec.

**Q3: Database sharding strategy for TinyURL - Hash vs Range based?**
A: **Hash-based:** `shard_id = hash(short_code) % num_shards`. Even distribution, but resharding hard (add shard → rehash all). **Range-based:** Shard1: a-m, Shard2: n-z. Easy to add shards, but uneven (some letters more common). **Best:** Hash-based for TinyURL (short_codes random distribution). **Implementation:** Consistent hashing for easy scaling (add shard → only 1/n keys move). **Bitly:** Uses hash-based sharding with 100+ shards.

**Q4: Cache strategy - Cache short→long or long→short or both?**
A: **Cache short→long:** Redirect flow (most frequent - 99% traffic), Redis: `short:abc123 → https://...`. **Cache long→short:** Avoid duplicate shortening (same URL submitted multiple times), Redis: `url_hash:md5 → abc123`. **Best:** Cache both (different use cases). **TTL:** short→long = 24 hours (popular links), long→short = 1 hour (less critical). **Memory:** 1M URLs × 200 bytes = 200MB (affordable). **Bitly:** Caches both with 99% hit rate.

**Q5: Custom short URLs (vanity URLs) kaise implement karein?**
A: **Approach:** User requests custom code (bit.ly/my-brand). **Validation:** Check if available (not taken), length 4-20 chars, alphanumeric only. **Storage:** Same table, mark as custom (flag). **Collision:** If taken, suggest alternatives (my-brand-2, my-brand-2024). **Reservation:** Premium users can reserve (paid feature). **Implementation:** Separate namespace (custom codes don't conflict with auto-generated). **Example:** Bitly charges $29/month for custom domains. **Security:** Blacklist offensive words, prevent squatting (expire unused after 90 days).

---

## 🎯 Module 16 Complete Summary:

**All Topics Covered:** 1/1 ✅
- ✅ Topic 16.1: TinyURL System - Base62 Encoding, Key Generation Service, Sharding, Caching, Analytics

**Key Takeaways:**
1. **Base62 Encoding:** Auto-increment ID → Base62 string (62^7 = 3.5T URLs), guaranteed unique
2. **Key Generation Service:** Pre-generated keys with Zookeeper coordination, no collisions, scalable
3. **Caching:** Redis for 99% hit rate (short→long for redirects, long→short for deduplication)
4. **Sharding:** Hash-based on short_code for even distribution across database shards
5. **Analytics:** Async logging via Kafka, Cassandra for time-series click data

**Interview Focus:**
- Draw architecture: User → API → KGS → Database → Redis → Return short URL
- Explain Base62 encoding with example (125 → "cb")
- Discuss collision handling (KGS vs MD5 hash)
- Mention 301 vs 302 redirects (caching vs analytics)
- Real-world: Bitly (600M links/month, 100K req/sec)

**Production Patterns:**
- **Deduplication:** Hash long URL, check cache before generating new short code
- **Expiry:** TTL for temporary links (password reset expires in 24 hours)
- **Custom URLs:** Vanity URLs for branding (bit.ly/brand-name)
- **Rate Limiting:** 10 shortenings/min per user (prevent abuse)

**Scale Numbers:**
- 7 characters = 3.5 trillion URLs (62^7)
- 99% cache hit rate with Redis
- <100ms redirect latency
- 100K requests/sec capacity

**Progress:** 16/21 Modules Completed 🎉

**Next Module:** Module 17 - Design WhatsApp/Chat System (WebSockets, Message Storage, Encryption)

---
