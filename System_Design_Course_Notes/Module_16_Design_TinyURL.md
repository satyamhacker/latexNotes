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

**What is Zookeeper? (Beginner Explanation)**

Zookeeper ek **Traffic Controller** hai distributed systems ke liye. Jaise airport mein Air Traffic Controller planes ko runway assign karta hai (Runway 1 to Flight A, Runway 2 to Flight B), waise Zookeeper different servers ko ID ranges assign karta hai (taaki collision na ho).

**Core Functions:**
1. **Coordination:** Multiple servers ko organize kare (who does what)
2. **Configuration:** Settings centrally store (all servers read from one place)
3. **Leadership Election:** Decide kaun leader hai (if master crashes, elect new)
4. **Distributed Locking:** Ensure only one server edits data at a time

**For TinyURL:** Zookeeper assigns non-overlapping ID ranges to each KGS server (no duplicate IDs possible).

```
ZOOKEEPER COORDINATION (Detailed):

+---------------------------+
|       Zookeeper           |
|    (Range Manager)        |
|                           |
| Stored Data:              |
| /ranges/allocated         |
|   - 1 to 1M: Server-1     |
|   - 1M to 2M: Server-2    |
|   - 2M to 3M: Server-3    |
| /ranges/next_available    |
|   - 3M (next free range)  |
+---------------------------+
        |       |       |
     (1)|    (2)|    (3)| Assign non-overlapping ranges
        v       v       v
+----------+----------+----------+
| KGS      | KGS      | KGS      |
| Server-1 | Server-2 | Server-3 |
|          |          |          |
| Range:   | Range:   | Range:   |
| 1-1M     | 1M-2M    | 2M-3M    |
|          |          |          |
| Queue:   | Queue:   | Queue:   |
| [b,c,d,  | [eMJc,   | [q5Kp,   |
|  ...900K | ...800K  | ...1M    |
|  keys]   | keys]    | keys]    |
|          |          |          |
| Current: | Current: | Current: |
| 500K     | 1.5M     | 2.2M     |
+----------+----------+----------+
     |          |          |
     v          v          v
+----------------------------------+
|     API Servers (Consumers)      |
|  Request key from any KGS server |
+----------------------------------+
```

**Step-by-Step Flow (Server Startup):**

```
STEP 1: KGS Server-1 Starts
        |
        v
[Connect to Zookeeper]
Request: "Give me an ID range"
        |
        v
[Zookeeper Checks]
/ranges/next_available = 1 (start from 1)
        |
        v
[Zookeeper Assigns]
Range: 1 to 1,000,000
Update: /ranges/allocated → "1-1M: Server-1"
Update: /ranges/next_available → 1,000,001
        |
        v
[KGS Server-1 Receives]
Range: 1 to 1M
        |
        v
[Pre-Generate Keys]
for id in range(1, 1000001):
    key = base62_encode(id)  # "b", "c", "d", ...
    memory_queue.push(key)   # Store in memory
        |
        v
[Ready to Serve]
Queue has 1M pre-generated keys
Serving time: O(1) (just pop from queue)


STEP 2: API Server Requests Key
        |
        v
[API → KGS Server-1]
Request: "Give me a unique key"
        |
        v
[KGS Pops from Queue]
key = memory_queue.pop()  # "b" (first key)
current_position = 1
        |
        v
[Return to API]
Response: {"key": "b"}
        |
        v
[API Creates Short URL]
Short URL: tiny.url/b


STEP 3: Range Exhaustion Check
        |
        v
[KGS Monitors Usage]
Used: 800,000 / 1,000,000 (80%)
        |
        v
[Trigger: Request New Range]
When 80% consumed (safety buffer)
        |
        v
[Request to Zookeeper]
"I'm running low, give me next range"
        |
        v
[Zookeeper Assigns]
New Range: 3M to 4M (next available)
Update allocated ranges
        |
        v
[KGS Pre-Generates]
Pre-generate 1M more keys
Add to queue (parallel to serving current range)
        |
        v
[Seamless Continuation]
No downtime, old range exhausts → new range ready
```

**Crash Recovery (What if KGS Server Dies?):**

```
Scenario: KGS Server-1 crashes at position 500K (used 500K, unused 500K)

Problem: Unused IDs (500K to 1M) are LOST (in memory, not persisted)

Solution 1: WASTAGE (Simple)
- Zookeeper doesn't reassign lost range
- 500K IDs wasted (acceptable - 62^7 = 3.5T total capacity)
- New KGS server gets fresh range (3M-4M)

Solution 2: RECOVERY (Complex)
- Periodic checkpoints to disk (every 100K IDs)
- On restart, read checkpoint (500K), resume from there
- Minimal wastage (only since last checkpoint)

Production (Bitly): Use Solution 1 (wastage acceptable, simplicity wins)

Math: 1M IDs wasted per crash
      62^7 total capacity = 3.5 trillion
      Can afford 3.5 million crashes (unrealistic)
```

**Why Zookeeper vs Database?**

| Feature | Zookeeper | Database (PostgreSQL) |
|---------|-----------|----------------------|
| **Latency** | <10ms | 50-100ms |
| **Consistency** | Strong (consensus) | Depends on isolation level |
| **Coordination** | Built-in (leader election) | Complex to implement |
| **Failure Detection** | Automatic (heartbeat) | Manual (health checks) |
| **Atomic Operations** | Yes (CAS - Compare-And-Swap) | Yes (Transactions) |
| **Use Case** | Distributed coordination | Data persistence |

**For KGS:** Zookeeper better (coordination is primary need, data is just ranges)

**Benefits:**
- **No Collisions:** Ranges non-overlapping (Server-1: 1-1M, Server-2: 1M-2M, never overlap)
- **Fast:** Pre-generated (no computation on request)
- **Scalable:** Add more KGS servers (Zookeeper assigns new ranges)
- **Fault Tolerant:** One KGS down, others continue (Zookeeper tracks all)

**Interview Tip:**

Interviewer: "KGS server crash ho gaya, kya hoga?"

Answer: "KGS crash → Unused IDs lost (in-memory queue). But:
1. No data corruption (other KGS servers unaffected)
2. New KGS starts → Gets fresh range from Zookeeper
3. Wasted IDs acceptable (62^7 = 3.5T capacity)
4. Zookeeper ensures no overlap (new range always unique)
5. High availability: Multiple KGS servers running (load balanced)"

---

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
import hashlib  # MD5 hash for URL deduplication (check if URL already shortened)
import redis  # Redis for caching (fast lookup, TTL support)
from typing import Optional  # Optional type hint (return value can be None)

class TinyURL:
    def __init__(self):
        # Redis connection for caching (in-memory, <1ms latency vs 50ms DB)
        self.redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
        
        # Base62 character set: [a-z, A-Z, 0-9] = 62 total characters
        # Order: a=0, b=1, ..., z=25, A=26, ..., Z=51, 0=52, ..., 9=61
        # Why 62? Compact (7 chars = 62^7 = 3.5T URLs), URL-safe (no special chars)
        self.base62_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        
        # Counter for auto-increment IDs (start from 1M for demo readability)
        # Production: KGS (Key Generation Service) provides IDs from distributed ranges
        # Thread safety: In production, use atomic Redis INCR or database AUTO_INCREMENT
        self.counter = 1000000
    
    def base62_encode(self, num: int) -> str:
        """
        Convert decimal number to Base62 string (like decimal to binary conversion)
        Example: 125 → "cb" (c=2, b=1 in base62)
        Logic: Repeatedly divide by 62, collect remainders bottom-up
        """
        # Edge case: 0 maps to first character 'a'
        if num == 0:
            return self.base62_chars[0]  # Return 'a'
        
        result = ""  # Build result string character by character
        
        # Keep dividing by 62 until number becomes 0
        while num > 0:
            # Modulo 62 gives digit in base62 (0-61 maps to a-9)
            remainder = num % 62  # e.g., 125 % 62 = 1
            
            # Prepend character (read bottom-up like decimal to binary)
            # Example: 125 → [1, 2] remainders → 'b' + 'c' = "cb" (reversed)
            result = self.base62_chars[remainder] + result  
            
            # Integer division (floor division) to get quotient for next iteration
            num = num // 62  # e.g., 125 // 62 = 2, then 2 // 62 = 0 (stop)
        
        return result  # Return base62 string (e.g., "cb" for ID=125)
    
    def shorten(self, long_url: str) -> str:
        """
        Shorten a long URL to short code
        Flow: Check cache → Generate ID → Base62 encode → Store → Return
        """
        # STEP 1: Deduplication check (agar same URL pehle shortened hai toh wapas use karo)
        # MD5 hash: 128-bit hash of URL (deterministic - same URL = same hash)
        # Why MD5? Fast (not for security here), consistent hash for deduplication
        url_hash = hashlib.md5(long_url.encode()).hexdigest()  # e.g., "5d41402abc4b2a76b9719d911017c592"
        
        # Redis key pattern: "url_hash:{hash_value}" → short_code
        # Check if this URL was already shortened before
        cached = self.redis.get(f"url_hash:{url_hash}")
        
        if cached:
            # URL already shortened, return existing short URL (avoid duplicate entries)
            # No need to decode since decode_responses=True in Redis connection
            return f"https://tiny.url/{cached}"
        
        # STEP 2: Generate unique short code
        # Increment counter (in production: KGS provides pre-generated IDs)
        # Thread safety concern: Multiple servers → race condition
        # Solution: Redis INCR (atomic) or database AUTO_INCREMENT
        self.counter += 1  # e.g., 1000000 → 1000001
        
        # Convert numeric ID to Base62 string (compact representation)
        short_code = self.base62_encode(self.counter)  # e.g., 1000001 → "eMJd"
        
        # STEP 3: Store bidirectional mapping in Redis
        # Mapping 1: short_code → long_url (for redirect flow)
        # TTL = 86400 seconds (24 hours) - auto-expire temporary links
        # Production: Store in database (PostgreSQL) + cache in Redis
        self.redis.setex(f"short:{short_code}", 86400, long_url)
        
        # Mapping 2: url_hash → short_code (for deduplication check)
        # Prevents same URL from getting multiple short codes
        self.redis.setex(f"url_hash:{url_hash}", 86400, short_code)
        
        # Return complete short URL
        return f"https://tiny.url/{short_code}"  # e.g., "https://tiny.url/eMJd"
    
    def redirect(self, short_code: str) -> Optional[str]:
        """
        Get original URL from short code (redirect flow)
        Flow: Cache lookup → Return original URL → Log analytics
        Returns None if short_code not found (404 case)
        """
        # STEP 1: Cache lookup (Redis key pattern: "short:{code}")
        # 99% cache hit rate for popular URLs (no DB query needed)
        long_url = self.redis.get(f"short:{short_code}")
        
        if long_url:
            # Cache HIT: Original URL found
            # Log click asynchronously (don't block redirect)
            # Production: Publish to Kafka, separate analytics service processes
            self._log_click(short_code)
            
            # Return original URL (no need to decode with decode_responses=True)
            return long_url  # e.g., "https://example.com/very/long/url"
        
        # Cache MISS: URL not found (expired OR invalid short_code)
        # Production: Query database as fallback, update cache if found
        return None  # Return None → API returns 404 Not Found
    
    def _log_click(self, short_code: str):
        """
        Log click event for analytics (async in production)
        Tracks: click count, timestamp, IP, geography, referrer
        """
        # Redis INCR: Atomic increment (thread-safe counter)
        # Key pattern: "clicks:{short_code}" → total click count
        # Production: Also log to Cassandra (time-series DB) for detailed analytics
        self.redis.incr(f"clicks:{short_code}")
        
        # Production additional logging (not shown here):
        # - Timestamp: datetime.now()
        # - IP address: request.remote_addr
        # - User agent: request.headers.get('User-Agent')
        # - Referrer: request.headers.get('Referer')
        # - Geography: IP geolocation lookup
        # Store in Cassandra partition by (short_code, date) for fast queries

# ============ USAGE EXAMPLES ============

service = TinyURL()

# Example 1: Shorten a long URL (e.g., Amazon product link)
long_url = "https://example.com/very/long/url/with/many/parameters?utm_source=twitter&utm_campaign=sale"
short_url = service.shorten(long_url)
print(f"✅ Short URL created: {short_url}")  
# Output: ✅ Short URL created: https://tiny.url/eMJd
# Space saved: 90 chars → 25 chars (72% reduction)

# Example 2: Shorten same URL again (deduplication test)
short_url_2 = service.shorten(long_url)  # Same URL as above
print(f"🔄 Duplicate check: {short_url_2}")  
# Output: 🔄 Duplicate check: https://tiny.url/eMJd (same short code)
# No new entry created, cache hit on url_hash

# Example 3: Redirect user (when they click short URL)
clicked_code = "eMJd"  # Extract from URL path
original_url = service.redirect(clicked_code)
if original_url:
    print(f"📍 Redirecting to: {original_url}")
    # HTTP 302 redirect to original_url
    # Analytics logged (click count incremented)
else:
    print(f"❌ Short URL not found (404)")
    # Invalid or expired short code

# Example 4: Check analytics
click_count = service.redis.get(f"clicks:eMJd")
print(f"📊 Total clicks: {click_count}")  
# Output: 📊 Total clicks: 1 (from example 3)
```

---

### **MD5 Collision Handling (Why Production Avoids It):**

**Problem Statement:**  
Agar hum MD5 hash ke first 7 characters use karte hain as short code, toh collision possible hai (2 different URLs → same short code).

**Birthday Paradox (Math Behind Collisions):**

```
MD5 hash = 128 bits = 2^128 possible hashes
First 7 chars (base62) = 62^7 = 3.5 trillion possibilities

Birthday Paradox: Collision probability
P(collision) ≈ n^2 / (2 × possible_values)

For n = 1 million URLs, 62^7 possibilities:
P(collision) = (10^6)^2 / (2 × 3.5 × 10^12)
             = 10^12 / (7 × 10^12)
             = 14.3% (HIGH RISK!)

For n = 10K URLs:
P(collision) = (10^4)^2 / (7 × 10^12)
             = 10^8 / (7 × 10^12)
             = 0.0014% (LOW RISK)

Collision happens at √n (square root):
√(3.5 × 10^12) ≈ 1.87 million URLs
```

**ASCII Diagram (Collision Scenario):**

```
URL 1: https://example.com/page1
    ↓ MD5 hash
"a1b2c3d4e5f6g7h8..."
    ↓ Take first 7 chars
Short code: "a1b2c3d"

URL 2: https://different.com/page2
    ↓ MD5 hash  
"a1b2c3d9x8y7z6w5..."  (different hash)
    ↓ Take first 7 chars
Short code: "a1b2c3d"  ❌ COLLISION!

Result: Two URLs → Same short code → Wrong redirect
User clicks tiny.url/a1b2c3d → Which URL to return?
```

**Detection \u0026 Regeneration Strategy:**

```python
def generate_short_code_with_collision_handling(long_url: str, attempt: int = 0) -> str:
    """
    Generate short code with MD5, handle collisions by regeneration
    attempt: Retry counter (0, 1, 2, ...)
    """
    # Generate MD5 hash with salt (attempt number) to vary hash
    # Adding attempt ensures different hash on each retry
    salted_url = f"{long_url}:{attempt}"  # e.g., "http://example.com:0", "http://example.com:1"
    hash_value = hashlib.md5(salted_url.encode()).hexdigest()
    
    # Take first (7 + attempt) characters (longer code on collision)
    # First attempt: 7 chars, Second: 8 chars, Third: 9 chars, etc.
    code_length = 7 + attempt
    short_code = hash_value[:code_length]
    
    # Check if short_code already exists in database
    if database.exists(short_code):
        # COLLISION DETECTED!
        # Retry with next attempt (longer hash)
        if attempt < 5:  # Max 5 retries (avoid infinite loop)
            return generate_short_code_with_collision_handling(long_url, attempt + 1)
        else:
            # After 5 retries, fallback to guaranteed unique method
            # Use auto-increment ID + Base62 (collision-free)
            unique_id = database.get_next_id()
            return base62_encode(unique_id)
    
    # No collision, return short code
    return short_code

# Example flow:
# Attempt 0: "a1b2c3d" (7 chars) → Collision → Retry
# Attempt 1: "a1b2c3d4" (8 chars) → Collision → Retry
# Attempt 2: "a1b2c3d4e" (9 chars) → Available → Use this
```

**Why Production Avoids MD5 for Primary Keys:**

1. **Collision Risk:** At 1.87M URLs, collision probability becomes significant (birthday paradox)
2. **No Guarantee:** Hash functions don't guarantee uniqueness (pigeonhole principle - infinite URLs → finite hash space)
3. **Detection Overhead:** Checking collision on every insert = extra DB query (latency)
4. **Regeneration Cost:** Retry logic complex, multiple DB queries per collision
5. **Unpredictable Length:** Collision → longer code → inconsistent UX (7 vs 9 chars)

**Production Best Practice:**

```
✅ RECOMMENDED: Auto-increment ID + Base62 encoding
   - Guaranteed unique (ID unique by definition)
   - Fast (no collision check needed)
   - Predictable length (7 chars consistent)
   - Sequential (can be security issue, but solvable with KGS random ranges)

✅ RECOMMENDED: Key Generation Service (KGS)
   - Pre-generated unique keys
   - Distributed ranges (Server1: 1-1M, Server2: 1M-2M)
   - No collision (ranges non-overlapping)
   - Fast (no computation, just pop from queue)

❌ AVOID: MD5/SHA hash first N characters
   - Collision possible (birthday paradox)
   - Detection overhead (DB query per insert)
   - Unpredictable (regeneration logic complex)
```

**Real-World Example:**

**Bitly's Evolution:**
- **2008-2010 (Early days):** MD5 hash with collision detection → Slow, complex
- **2010-2015:** Switched to auto-increment ID + Base62 → Fast, simple, no collisions
- **2015-Present:** KGS with Zookeeper → Distributed, scalable, 100K req/sec

**Lesson:** Start simple (Auto-increment + Base62), scale to KGS when needed. Avoid hash-based approaches for production URL shorteners.

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

---

### **HTTP 301 vs 302: Detailed Comparison for URL Shorteners**

**Understanding Redirect Types:**

HTTP redirects tell the browser "this URL has moved, go here instead." But there are 2 types with very different behaviors:

| Feature | HTTP 301 (Permanent) | HTTP 302 (Temporary) |
|---------|---------------------|---------------------|
| **Meaning** | URL moved forever (never coming back) | URL moved temporarily (might change later) |
| **Browser Caching** | ✅ YES - Browser remembers redirect | ❌ NO - Browser asks server every time |
| **Server Hit** | First time only (then cached) | Every click (no cache) |
| **Analytics** | ❌ BREAKS - Subsequent clicks invisible | ✅ WORKS - Every click logged |
| **Update Destination** | ❌ IMPOSSIBLE - Cached in browser | ✅ POSSIBLE - Server controls |
| **Performance** | Faster (no server request after first) | Slower (server round-trip every time) |
| **SEO Impact** | Passes link juice to new URL | Doesn't pass link juice |
| **Use Case** | Domain migration, permanent moves | Short URLs, A/B testing, tracking |
| **HTTP Header** | `Status: 301 Moved Permanently` | `Status: 302 Found` |

**Flow Comparison (ASCII Diagram):**

```
HTTP 301 (Permanent):

First Click:
[User] → [tiny.url/abc] → [Server: 301 → example.com] → [Browser: Cache this]
                                                            ↓
                                                    [Browser Cache]
                                                    tiny.url/abc → example.com

Second Click (NO SERVER HIT):
[User] → [tiny.url/abc] → [Browser Cache: Go directly to example.com] → [example.com]
                           ^
                           |
                      Server NOT contacted
                      Analytics NOT logged ❌


HTTP 302 (Temporary):

First Click:
[User] → [tiny.url/abc] → [Server: 302 → example.com] → [Browser: Don't cache]
                                 |
                                 v
                          [Log Analytics ✅]

Second Click (SERVER HIT EVERY TIME):
[User] → [tiny.url/abc] → [Server: 302 → example.com] → [Browser loads example.com]
                                 |
                                 v
                          [Log Analytics ✅]
```

**Real-World Scenario:**

**Scenario 1: Marketing Campaign (302 Required)**
```
Marketing team: "Share this link: tiny.url/sale2024"
Week 1: Points to: example.com/winter-sale
Week 2: UPDATE to: example.com/summer-sale (destination changed)

With 301: ❌ Users who clicked Week 1 still see winter-sale (cached)
With 302: ✅ All users see current destination (summer-sale)
```

**Scenario 2: Click Analytics (302 Required)**
```
Marketer needs: "How many people clicked the link?"

With 301: ❌ First click logged, repeat clicks invisible (browser cache)
              10 actual clicks → Analytics show only 1 click
With 302: ✅ Every click logged (server hit every time)
              10 actual clicks → Analytics show 10 clicks
```

**Scenario 3: Permanent Website Move (301 Appropriate)**
```
Company changed domain: oldsite.com → newsite.com
Redirect all old links permanently

With 301: ✅ SEO preserved (Google shows newsite.com)
              Performance good (browser caches)
With 302: ❌ SEO not transferred (Google confused)
              Performance poor (server hit every time)
```

**Best Practice for TinyURL:**

```python
def redirect_url(short_code: str, track_analytics: bool = True):
    """
    Redirect user to original URL
    track_analytics: If True, use 302 (analytics), else 301 (performance)
    """
    long_url = get_url_from_database(short_code)
    
    if track_analytics:
        # HTTP 302: Temporary redirect (analytics tracked)
        # Browser won't cache, every click hits server
        return redirect(long_url, code=302)
    else:
        # HTTP 301: Permanent redirect (performance)
        # Browser caches, no analytics on repeat clicks
        # Use only for permanent redirects (domain changes)
        return redirect(long_url, code=301)

# Default: Always use 302 for URL shorteners (analytics critical)
redirect_url("abc123", track_analytics=True)  # 302
```

**Modern Approach (HTTP 307/308):**

```
HTTP 307: Temporary Redirect (like 302 but preserves HTTP method)
HTTP 308: Permanent Redirect (like 301 but preserves HTTP method)

For POST requests:
302/301 might change POST → GET (browser behavior)
307/308 guarantee method preservation

URL shorteners: Use 302/307 (both work, 302 more common)
```

**Performance Impact:**

```
301 (First click): 100ms (server round-trip)
301 (Repeat clicks): 0ms (browser cache - instant)

302 (Every click): 100ms (server round-trip)

At 1000 users, 10 clicks each:
301: 1000 server requests (first click only)
302: 10,000 server requests (every click)

But: 302 gets analytics for all 10,000 clicks
301 gets analytics for only 1,000 clicks (90% data loss!)
```

**Interview Tip:**

Interviewer: "301 ya 302 use karoge TinyURL mein?"

Answer: "302 (Temporary) because:
1. Analytics critical hai - har click log karna zaroori
2. Destination update kar sakte hain (marketing campaigns)
3. A/B testing possible (change destination without users noticing)
4. Performance impact minimal (100ms acceptable)
5. 301 se analytics break ho jaati hai (browser caching)

Lekin agar permanent redirect hai (domain change) toh 301 use karo (SEO benefits)."

---

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
