# Module 13: Design Rate Limiter

## Topic 13.1: Rate Limiter - Algorithms & Architecture

---

## 🎯 1. Title / Topic: Rate Limiter (API Request Control System)

---

## 🐣 2. Samjhane ke liye (Simple Analogy):

Rate Limiter ek **Security Guard** hai jo mall ke entrance par khada hai. Jaise guard kehta hai "Ek family sirf 5 baar andar ja sakti hai 1 ghante mein, isse zyada nahi", waise hi Rate Limiter kehta hai "Ek user sirf 100 requests bhej sakta hai 1 minute mein". Agar koi baar-baar try kare (spam/attack), toh guard rok deta hai. Result: Mall mein bheed control, genuine customers ko space milta hai. Similarly, server overload nahi hota, genuine users ko fast service milti hai.

---

## 📖 3. Technical Definition (Interview Answer):

**Definition:** A Rate Limiter is a system component that controls the rate of traffic sent or received by a network/API by limiting the number of requests a user/IP can make within a specified time window.

**Key terms:**
- **Controls rate:** Requests ki speed/frequency ko limit karna (e.g., 100 req/min)
- **Time window:** Fixed duration jisme limit apply hoti hai (1 sec, 1 min, 1 hour)
- **Throttling:** Excess requests ko reject/delay karna
- **HTTP 429:** "Too Many Requests" response code jo client ko milta hai jab limit exceed ho
- **Client identification:** User ko identify karna (User ID, IP Address, API Key se)

---

## 🧠 4. Zaroorat Kyun Hai? (Why?):

**Main Problem:** Bina Rate Limiter ke, koi bhi user unlimited requests bhej sakta hai. Ek malicious user 1 million requests/sec bhej de toh server crash ho jayega (DDoS attack). Ya phir ek buggy client infinite loop mein requests bhejta rahe.

**Business Impact:** Server crash = Downtime = Revenue loss. AWS/GCP billing bhi badh jayega kyunki unnecessary compute resources use ho rahe hain.

**Technical Benefits:**
- **DoS/DDoS Protection:** Malicious traffic block hoti hai
- **Cost Control:** Cloud resources ka wastage nahi hota (bandwidth, compute)
- **Fair Usage:** Saare users ko equal access milta hai, koi ek user saare resources nahi le sakta
- **API Monetization:** Free tier (100 req/day), Paid tier (10K req/day) - business model enable hota hai

---

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario):

**Technical Breakdown:**
- Ek attacker 1 million requests/sec bhejta hai → Server CPU 100%, Memory full → Database connections exhaust (max 1000 connections) → Server crash (503 Service Unavailable)
- Legitimate users ko timeout errors milti hain
- Database bhi overload ho jata hai (slow queries, deadlocks)

**User Impact:** Genuine customers website/app use nahi kar paate, frustrated hokar competitor ke paas chale jaate hain.

**Business Impact:** Revenue loss, brand reputation damage, AWS bill skyrocket (bandwidth + compute charges).

**Real Example:** **GitHub (2018)** - DDoS attack without proper rate limiting → 1.35 Tbps traffic → Services down for 10 minutes → Millions of developers affected. After implementing advanced rate limiting, similar attacks automatically blocked.

---

## ⚙️ 6. Under the Hood (Technical Working):

**Rate Limiter Flow (Step-by-Step):**

1. **Request Arrival:** Client request aata hai API Gateway/Load Balancer par
2. **Client Identification:** User ko identify karo (User ID, IP Address, API Key)
3. **Counter Check:** Redis/Memory se current count fetch karo for this user in current time window
4. **Limit Comparison:** 
   - If count < limit → Allow request, increment counter
   - If count >= limit → Reject request, return HTTP 429
5. **Counter Update:** Redis mein counter update karo with TTL (Time To Live)
6. **Response:** Allowed request ko backend server par forward karo, rejected request ko error response bhejo

**Key Components:**
- **Rules Database:** Limit rules store (e.g., "/api/login" → 5 req/min, "/api/search" → 100 req/min)
- **Redis Cache:** Fast counter storage (in-memory, microsecond latency)
- **Rate Limiting Middleware:** Application layer component jo har request ko intercept karta hai

**ASCII Diagram:**

```
[Client/User]
     |
     | (1) HTTP Request (User ID: user123)
     v
+------------------------+
|   API Gateway/LB       |
|  (Rate Limiter Layer)  |
+------------------------+
     |
     | (2) Check: user123 count in Redis
     v
+------------------------+
|    Redis Cache         |
| Key: user123:api_call  |
| Value: 95 (count)      |
| TTL: 60 sec            |
+------------------------+
     |
     | (3) Count < 100? YES
     v
+------------------------+
| Increment: 95 → 96     |
| Allow Request          |
+------------------------+
     |
     | (4) Forward to Backend
     v
+------------------------+
|   Backend Server       |
|   (Process Request)    |
+------------------------+
     |
     | (5) Response
     v
[Client receives 200 OK]


--- REJECTION FLOW ---

[Attacker]
     |
     | Request #101 (within 1 min)
     v
[Rate Limiter]
     |
     | Check: count = 100 (limit reached)
     v
[REJECT]
     |
     | HTTP 429 Too Many Requests
     | Header: Retry-After: 45 seconds
     v
[Attacker blocked]
```

---

## 🛠️ 7. Problems Solved:

- **DDoS/DoS Attacks:** Malicious traffic automatically block → Server safe rahta hai, legitimate users unaffected
- **Cost Explosion:** Unlimited API calls prevent → Cloud billing control mein rahta hai (bandwidth + compute savings)
- **Resource Starvation:** Ek user saare resources nahi le sakta → Fair distribution, all users get service
- **Brute Force Attacks:** Login API par 1000 password tries block → Security improve (e.g., 5 failed attempts → 15 min cooldown)
- **API Monetization:** Free vs Paid tiers enforce → Business model enable (Stripe: Free=100 req/day, Pro=10K req/day)

---

## 🌍 8. Real-World Example:

**Twitter API:** 300 requests per 15-minute window for standard users, 900 requests for premium. Algorithm: Sliding Window Counter. Scale: 500M+ tweets/day, billions of API calls. Benefit: Prevents spam bots from scraping all tweets, protects infrastructure, enables paid API tiers ($100/month for higher limits). When limit exceeded, response includes `X-Rate-Limit-Remaining: 0` header and `Retry-After` timestamp. This saved Twitter millions in infrastructure costs while maintaining 99.9% uptime for legitimate developers.

---

## 🔧 9. Tech Stack / Tools:

- **Redis:** In-memory cache for counters. Use for: High-speed read/write (microsecond latency), TTL support for automatic expiry, atomic operations (INCR command). Perfect for distributed systems.

- **Nginx (ngx_http_limit_req_module):** Built-in rate limiting at web server level. Use for: Simple IP-based limiting, low latency (no external dependency), good for small-scale apps.

- **Kong/AWS API Gateway:** Managed API Gateway with rate limiting. Use for: Enterprise systems, multiple rate limit policies (per user, per IP, per API key), analytics dashboard, no code needed.

---

## 📐 10. Architecture/Formula:

**Architecture Diagram (Distributed Rate Limiter):**

```
                    [Multiple Clients]
                    /       |        \
                   /        |         \
                  v         v          v
            +--------+  +--------+  +--------+
            | LB-1   |  | LB-2   |  | LB-3   |
            | (Rate  |  | (Rate  |  | (Rate  |
            | Limit) |  | Limit) |  | Limit) |
            +--------+  +--------+  +--------+
                  \        |         /
                   \       |        /
                    v      v       v
              +----------------------+
              |   Redis Cluster      |
              |  (Centralized Store) |
              |                      |
              | user123:api → 45     |
              | user456:api → 89     |
              | TTL: 60 sec          |
              +----------------------+
                        |
                        | (If allowed)
                        v
              +----------------------+
              |   Backend Servers    |
              |   (App Logic)        |
              +----------------------+

Key: All Load Balancers share same Redis → Consistent counting
```

**Formula (Token Bucket Algorithm):**

```
Tokens_Available = min(Max_Tokens, Current_Tokens + (Time_Elapsed × Refill_Rate))

Example:
- Max_Tokens = 100 (bucket capacity)
- Refill_Rate = 10 tokens/second
- Current_Tokens = 20
- Time_Elapsed = 5 seconds

Calculation:
New_Tokens = 20 + (5 × 10) = 20 + 50 = 70
Tokens_Available = min(100, 70) = 70

Request arrives → Needs 1 token → 70 - 1 = 69 tokens remaining
```

---

## 💻 11. Code / Flowchart:

**Flowchart (Token Bucket Algorithm):**

```
START: Request arrives
     |
     v
[Get current timestamp]
     |
     v
[Calculate tokens to add]
tokens = (now - last_refill) × refill_rate
     |
     v
[Update bucket]
current_tokens = min(max_tokens, current_tokens + tokens)
     |
     v
[Check availability]
     |
     +---> current_tokens >= 1?
     |              |
     |              v
     |            YES: Allow
     |              |
     |              v
     |         [Deduct 1 token]
     |         current_tokens -= 1
     |              |
     |              v
     |         [Forward request]
     |              |
     v              v
    NO: Reject    SUCCESS
     |
     v
[Return HTTP 429]
[Header: Retry-After]
     |
     v
   END
```

**Code (Redis + Lua for Atomicity - Only for understanding):**

```python
import redis
import time

# Redis connection
r = redis.Redis(host='localhost', port=6379)

def rate_limit(user_id, limit=100, window=60):
    key = f"rate_limit:{user_id}"
    current_time = int(time.time())
    
    # Lua script for atomic operation (prevent race condition)
    lua_script = """
    local count = redis.call('INCR', KEYS[1])  -- Counter increment (atomic)
    if count == 1 then
        redis.call('EXPIRE', KEYS[1], ARGV[1])  -- Set TTL on first request
    end
    return count  -- Return current count
    """
    
    count = r.eval(lua_script, 1, key, window)  # Execute atomically
    
    if count > limit:
        return False, f"Rate limit exceeded. Retry after {window} seconds"
    return True, f"Request allowed. {limit - count} remaining"

# Usage
allowed, message = rate_limit("user123", limit=5, window=60)
print(message)  # "Request allowed. 4 remaining"
```

---

## 📈 12. Trade-offs:

- **Gain:** DDoS protection, cost control, fair usage | **Loss:** Added latency (1-2ms for Redis lookup), complexity in distributed systems, false positives (legitimate users blocked during traffic spikes)

- **Gain:** Prevents server crash, enables API monetization | **Loss:** Extra infrastructure cost (Redis cluster), single point of failure (if Redis down, all requests blocked or allowed - need fallback strategy)

- **When to use:** Public APIs, high-traffic systems (>1000 RPS), any system exposed to internet | **When to skip:** Internal microservices (trusted environment), very low traffic (<10 users)

- **Algorithm Trade-off:** Token Bucket (smooth traffic, burst allowed) vs Fixed Window (simple but boundary issue - 2x requests at window edge)

---

## 🐞 13. Common Mistakes:

- **Mistake:** Using application memory instead of Redis for counters in distributed systems
  - **Why wrong:** Har server ka apna counter hoga, total limit enforce nahi hoga
  - **What happens:** User 100 requests Server-1 ko, 100 Server-2 ko = 200 total (limit bypass)
  - **Fix:** Centralized Redis cluster use karo, all servers share same counter

- **Mistake:** Not using Lua scripts in Redis, separate GET-INCR-SET operations
  - **Why wrong:** Race condition - 2 requests simultaneously aaye toh dono pass ho jayenge
  - **What happens:** Limit exceed ho sakti hai (101 requests instead of 100)
  - **Fix:** Lua script use karo for atomic operations (Redis single-threaded hai, Lua script atomically execute hota hai)

- **Mistake:** Fixed Window algorithm use karna without understanding boundary issue
  - **Why wrong:** Window ke end aur start par double requests possible (12:00:59 → 100 req, 12:01:00 → 100 req = 200 in 2 seconds)
  - **What happens:** Burst traffic se server overload
  - **Fix:** Sliding Window Counter ya Token Bucket use karo

- **Mistake:** Not returning proper HTTP headers (Retry-After, X-RateLimit-Remaining)
  - **Why wrong:** Client ko pata nahi kab retry kare, blind retries se aur load badhta hai
  - **Fix:** Always return `Retry-After: 60` and `X-RateLimit-Remaining: 0` headers

---

## ✅ 14. Zaroori Notes for Interview:

**Must Mention Points:**
1. **Start with algorithm choice:** "Main 4 algorithms hain - Token Bucket (best for smooth traffic), Leaky Bucket (constant output rate), Fixed Window (simple but flawed), Sliding Window (accurate but complex). I'll use Token Bucket kyunki burst traffic handle kar sakta hai."

2. **Draw architecture:** Client → API Gateway (Rate Limiter) → Redis (Counter Store) → Backend. Mention Redis kyun (in-memory, fast, TTL support, atomic operations).

3. **Distributed challenge:** "Multiple servers hain toh centralized Redis zaroori hai, warna har server apna counter rakhega aur total limit enforce nahi hoga."

4. **Common follow-ups:**
   - **"Fixed Window vs Sliding Window?"** → Fixed: Simple but boundary issue (2x requests at edge). Sliding: Accurate but memory-heavy (har request ka timestamp store).
   - **"Redis down ho gaye toh?"** → Fallback: (a) Fail-open (allow all - risky), (b) Fail-closed (block all - bad UX), (c) Local cache with eventual consistency.
   - **"Rate limit kaise decide karoge?"** → Analyze: (1) Server capacity (max RPS), (2) User behavior (avg requests/min), (3) Business needs (free vs paid tiers).

5. **Mention HTTP 429:** "Rejected requests ko 429 status code with Retry-After header bhejenge, client ko pata chalega kab retry kare."

6. **Scalability:** "Redis Cluster use karenge for horizontal scaling, consistent hashing se keys distribute hongi multiple nodes par."

7. **Pro tip:** "Different endpoints ke liye different limits - Login API (5 req/min - brute force prevent), Search API (100 req/min - normal usage), Upload API (10 req/hour - resource-heavy)."

---

## ❓ 15. FAQ & Comparisons (MANDATORY - 5 Questions):

**Q1: Token Bucket vs Leaky Bucket - Kab kaunsa use karein?**
A: **Token Bucket** use karo jab burst traffic allow karni ho (e.g., user ne 10 sec wait kiya toh 10 requests ek saath bhej sakta hai - tokens accumulate hote hain). **Leaky Bucket** use karo jab constant output rate chahiye (e.g., video streaming - fixed bandwidth, no bursts). Token Bucket zyada flexible hai, most APIs mein yahi use hota hai.

**Q2: Fixed Window vs Sliding Window - Main difference?**
A: **Fixed Window:** Time ko fixed chunks mein divide (12:00-12:01, 12:01-12:02). Problem: Boundary par 2x requests (12:00:59 → 100, 12:01:00 → 100 = 200 in 2 sec). Simple but flawed. **Sliding Window:** Har request ke time se pichle 60 sec ka count check (accurate). Memory-heavy (har request timestamp store). Sliding Window accurate hai but complex, Fixed Window simple hai but boundary issue hai.

**Q3: Rate Limiter Redis ke saath kaise integrate hota hai?**
A: Rate Limiter middleware har request ko intercept karta hai → Redis se counter fetch (`GET user123:api`) → Limit check → Agar allowed toh counter increment (`INCR user123:api`) with TTL (`EXPIRE 60`) → Request forward. Redis ka INCR command atomic hai (race condition nahi hota). Lua scripts use karte hain for multi-step atomic operations (GET-CHECK-INCR ek saath).

**Q4: Agar Redis crash ho jaye toh kya hoga?**
A: **3 strategies:** (1) **Fail-Open** - Sab requests allow (risky, DDoS possible), (2) **Fail-Closed** - Sab requests block (bad UX, legitimate users affected), (3) **Local Cache Fallback** - Har server apna in-memory counter use kare temporarily (not perfect but better than nothing). Best: Redis Cluster with replication (Master-Slave) - agar Master down toh Slave promote ho jata hai (high availability).

**Q5: Different users ke liye different limits kaise set karein (Free vs Paid)?**
A: **User Tier Mapping:** Database mein user tier store (`user123 → tier: premium`). Rate Limiter request aane par user tier fetch kare → Tier ke basis par limit apply (`free → 100/day, premium → 10K/day`). Redis key mein tier include (`rate_limit:user123:free:api`). Ya phir API Key based (`api_key_abc123 → 10K/day`). Kong/AWS API Gateway mein ye built-in feature hai (policy-based rate limiting).

---

## 🎯 Module 13 Summary:

**Topics Covered:** 1/4
- ✅ Topic 13.1: Rate Limiter Basics - Algorithms & Architecture

**Next Topics:**
- Topic 13.2: Rate Limiting Algorithms Deep Dive (Token Bucket, Leaky Bucket, Fixed Window, Sliding Window)
- Topic 13.3: Distributed Rate Limiter with Redis + Lua Scripts
- Topic 13.4: Advanced Rate Limiting (Multi-tier, Geo-based, Adaptive Rate Limiting)

**Progress:** 13/21 Modules Completed

---


---

## Topic 13.2: Rate Limiting Algorithms Deep Dive

---

## 🎯 1. Title / Topic: Rate Limiting Algorithms (Token Bucket, Leaky Bucket, Fixed Window, Sliding Window)

---

## 🐣 2. Samjhane ke liye (Simple Analogy):

Imagine 4 different **ticket counters** at a railway station:
1. **Token Bucket:** Counter mein tokens hain (100), har minute 10 tokens add hote hain. Passenger aaya toh 1 token le gaya. Agar tokens khatam toh wait karo.
2. **Leaky Bucket:** Queue hai fixed speed se process hoti hai (10 passengers/min), chahe 100 ek saath aaye. Overflow ho gaya toh reject.
3. **Fixed Window:** 9:00-9:01 mein 100 tickets, 9:01-9:02 mein phir 100 tickets (reset). Problem: 9:00:59 mein 100 aur 9:01:00 mein 100 = 200 in 2 seconds.
4. **Sliding Window:** Har passenger ke time se pichle 60 seconds mein kitne aaye, wo count (accurate but complex).

---

## 📖 3. Technical Definition (Interview Answer):

**Rate Limiting Algorithms** are mathematical approaches to control request flow by tracking and limiting the number of operations within time constraints.

**Key Algorithms:**
- **Token Bucket:** Tokens refill at constant rate, requests consume tokens, allows burst traffic
- **Leaky Bucket:** Requests queued, processed at fixed rate, smooths traffic spikes
- **Fixed Window Counter:** Time divided into fixed intervals, counter resets at boundary
- **Sliding Window Log:** Tracks timestamp of each request, accurate but memory-intensive
- **Sliding Window Counter:** Hybrid approach, weighted count from previous + current window

---

## 🧠 4. Zaroorat Kyun Hai? (Why?):

**Main Problem:** Ek hi algorithm sab scenarios mein fit nahi hota. Kuch systems ko burst traffic allow karni hoti hai (Token Bucket), kuch ko constant output rate chahiye (Leaky Bucket), kuch ko simplicity chahiye (Fixed Window).

**Business Impact:** Wrong algorithm choose kiya toh ya toh legitimate users block ho jayenge (bad UX) ya phir attackers limit bypass kar lenge (security risk).

**Technical Benefits:**
- **Flexibility:** Different use cases ke liye different algorithms (API calls vs Video streaming vs Login attempts)
- **Optimization:** Memory vs Accuracy trade-off (Fixed Window: low memory, Sliding Log: high accuracy)
- **Burst Handling:** Token Bucket allows short bursts (user waited 10 sec, now 10 requests ek saath)

---

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario):

**Scenario 1 - Wrong Algorithm (Fixed Window for critical API):**
- Banking API uses Fixed Window (100 req/min)
- Attacker exploits boundary: 11:59:59 → 100 requests, 12:00:00 → 100 requests = 200 in 2 seconds
- Database overload → Transactions fail → Money transfer errors → Customer complaints

**Scenario 2 - No Burst Support (Leaky Bucket for user API):**
- User opens app after 1 hour (should have accumulated tokens)
- Leaky Bucket doesn't allow burst → User's 10 requests queued → Slow loading → Bad UX → App uninstall

**Real Example:** **Cloudflare** initially used Fixed Window, faced boundary exploitation. Switched to Sliding Window Counter → 40% reduction in false positives (legitimate users blocked).

---

## ⚙️ 6. Under the Hood (Technical Working):

### **Algorithm 1: Token Bucket**

**Working:**
1. Bucket mein tokens hain (capacity = 100)
2. Tokens refill at constant rate (10 tokens/sec)
3. Request aata hai → 1 token consume
4. Tokens available → Allow, else Reject
5. Tokens accumulate (max = capacity), burst allow

**Data Structure:** `{tokens: 45, last_refill: 1234567890, capacity: 100, refill_rate: 10}`

```
Time: 0s  → Tokens: 100 (full bucket)
Time: 5s  → 50 requests → Tokens: 50
Time: 10s → Refill: 50 + (5×10) = 100 (capped at capacity)
Time: 11s → 20 requests → Tokens: 80
Time: 12s → Burst: 80 requests ek saath → Tokens: 0 (allowed!)
```

### **Algorithm 2: Leaky Bucket**

**Working:**
1. Requests queue mein jaate hain (FIFO)
2. Fixed rate se process (10 req/sec)
3. Queue full → Reject new requests
4. Output rate constant (smooth traffic)

**Data Structure:** `{queue: [req1, req2, ...], capacity: 100, leak_rate: 10}`

```
Time: 0s  → 100 requests arrive → Queue: 100
Time: 1s  → Process 10 → Queue: 90
Time: 2s  → 50 new requests → Queue: 140 → Reject 40 (overflow)
Time: 10s → Queue: 0 (all processed at 10/sec)
```

### **Algorithm 3: Fixed Window Counter**

**Working:**
1. Time ko fixed windows mein divide (12:00-12:01)
2. Counter increment per request
3. Window end → Counter reset to 0
4. Simple but boundary issue

**Data Structure:** `{count: 45, window_start: 1234567890}`

```
Window: 12:00:00 - 12:00:59
12:00:30 → 50 requests → Count: 50
12:00:59 → 50 requests → Count: 100 (limit reached)
12:01:00 → Counter reset → Count: 0
12:01:00 → 100 requests → Count: 100 (allowed!)

Problem: 200 requests in 2 seconds (12:00:59 to 12:01:00)
```

### **Algorithm 4: Sliding Window Log**

**Working:**
1. Har request ka timestamp store
2. New request → Remove timestamps older than window
3. Count remaining timestamps
4. Accurate but memory-heavy

**Data Structure:** `{timestamps: [1234567890, 1234567891, ...]}`

```
Limit: 100 req/min
Current time: 12:01:00

Timestamps: [12:00:05, 12:00:10, ..., 12:00:55] (95 entries)
New request at 12:01:00 → Remove entries < 12:00:00 → Count: 95
95 < 100 → Allow (Count: 96)

Memory: 100 timestamps × 8 bytes = 800 bytes per user
```

### **Algorithm 5: Sliding Window Counter (Hybrid)**

**Working:**
1. Current window + Previous window ka weighted average
2. Formula: `Count = Prev_Count × Overlap% + Curr_Count`
3. Accurate + Memory efficient

**Data Structure:** `{prev_count: 80, curr_count: 30, window_start: 1234567890}`

```
Window: 60 seconds, Limit: 100
Previous window (12:00-12:01): 80 requests
Current window (12:01-12:02): 30 requests
Current time: 12:01:30 (30 sec into current window)

Overlap = 30/60 = 50% of previous window
Estimated count = 80 × 0.5 + 30 = 40 + 30 = 70
70 < 100 → Allow
```

**ASCII Comparison Diagram:**

```
TOKEN BUCKET (Burst Allowed):
Tokens: [●●●●●●●●●●] (10 tokens)
Request burst: ●●●●●●●● (8 consumed)
Remaining: [●●] (2 left)
Refill: +2 tokens/sec → [●●●●] after 1 sec


LEAKY BUCKET (Constant Output):
Queue: [R R R R R R R R R R] (10 requests)
         ↓ ↓ ↓ (leak rate: 3/sec)
Output: [R R R] → [R R R] → [R R R] (smooth)


FIXED WINDOW (Boundary Issue):
Window 1 (0-60s):  [████████████████████] 100 req at 59s
Window 2 (60-120s):[████████████████████] 100 req at 60s
                    ↑ Problem: 200 req in 2 seconds


SLIDING WINDOW (Accurate):
Timeline: |----60s----|----60s----|
          [████░░░░░░░░][░░░░████]
          Old requests  New requests
          (fade out)    (counted)
```

---

## 🛠️ 7. Problems Solved:

- **Burst Traffic:** Token Bucket allows accumulated tokens → User waited 10 sec, now 10 requests ek saath (good UX)
- **Smooth Output:** Leaky Bucket ensures constant processing rate → Video streaming bandwidth consistent (no jitter)
- **Boundary Exploitation:** Sliding Window prevents 2x requests at window edge → Accurate limiting (security)
- **Memory Efficiency:** Fixed Window uses O(1) memory vs Sliding Log O(n) → Scalable for millions of users
- **Accuracy vs Cost:** Sliding Window Counter balances both → 99% accurate with 10x less memory than Sliding Log

---

## 🌍 8. Real-World Example:

**Stripe API (Payment Gateway):** Uses **Token Bucket** algorithm. Free tier: 100 requests/sec with burst up to 1000 (10 sec accumulation). Scale: 1M+ API calls/sec globally. Implementation: Redis with Lua scripts for atomic token deduction. Benefit: Developers can make burst requests during peak loads (e.g., Black Friday sales spike) without hitting limits immediately. Headers returned: `X-RateLimit-Limit: 100`, `X-RateLimit-Remaining: 45`, `X-RateLimit-Reset: 1638360000`. This flexibility improved developer satisfaction by 60% while preventing abuse.

---

## 🔧 9. Tech Stack / Tools:

- **Redis + Lua:** Custom implementation of any algorithm. Use for: Full control, atomic operations, distributed systems. Token Bucket implementation: Store `{tokens, last_refill}`, Lua script calculates refill + deduction atomically.

- **Nginx (limit_req):** Built-in Leaky Bucket. Use for: Simple rate limiting at web server level, low latency, no external dependency. Config: `limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;`

- **Kong (Rate Limiting Plugin):** Supports multiple algorithms (Token Bucket, Fixed Window, Sliding Window). Use for: API Gateway, policy-based limits, analytics. Config via YAML/API.

---

## 📐 10. Architecture/Formula:

### **Token Bucket Formula:**

```
Tokens_To_Add = (Current_Time - Last_Refill_Time) × Refill_Rate
New_Token_Count = min(Capacity, Current_Tokens + Tokens_To_Add)

If New_Token_Count >= Request_Cost:
    Allow request
    New_Token_Count -= Request_Cost
Else:
    Reject request

Example:
Capacity = 100, Refill_Rate = 10/sec, Current_Tokens = 30
Last_Refill = 12:00:00, Current_Time = 12:00:05

Tokens_To_Add = (5 seconds) × 10 = 50
New_Token_Count = min(100, 30 + 50) = min(100, 80) = 80

Request arrives (cost = 1):
80 >= 1 → Allow
New_Token_Count = 80 - 1 = 79
```

### **Sliding Window Counter Formula:**

```
Overlap_Percentage = (Window_Size - Time_Since_Window_Start) / Window_Size
Estimated_Count = (Previous_Window_Count × Overlap_Percentage) + Current_Window_Count

If Estimated_Count < Limit:
    Allow request
Else:
    Reject request

Example:
Window_Size = 60 sec, Limit = 100
Previous_Window_Count = 80, Current_Window_Count = 30
Time_Since_Window_Start = 20 sec

Overlap_Percentage = (60 - 20) / 60 = 40/60 = 0.667
Estimated_Count = (80 × 0.667) + 30 = 53.36 + 30 = 83.36 ≈ 83

83 < 100 → Allow
```

### **Algorithm Comparison Diagram:**

```
ALGORITHM COMPARISON TABLE:

+------------------+----------+----------+---------+---------+
| Algorithm        | Memory   | Accuracy | Burst   | Output  |
+------------------+----------+----------+---------+---------+
| Token Bucket     | O(1)     | Good     | YES     | Variable|
| Leaky Bucket     | O(n)     | Good     | NO      | Constant|
| Fixed Window     | O(1)     | Poor     | NO      | Variable|
| Sliding Log      | O(n)     | Perfect  | NO      | Variable|
| Sliding Counter  | O(1)     | Excellent| NO      | Variable|
+------------------+----------+----------+---------+---------+

n = number of requests in window


DECISION TREE:

Need burst traffic?
    YES → Token Bucket
    NO  → Need constant output?
            YES → Leaky Bucket
            NO  → Need perfect accuracy?
                    YES → Sliding Window Log (if memory OK)
                    NO  → Sliding Window Counter (best balance)
```

---

## 💻 11. Code / Flowchart:

**Flowchart (Algorithm Selection):**

```
START: Request arrives
     |
     v
[Identify user/IP]
     |
     v
[Check algorithm type]
     |
     +------------------+------------------+
     |                  |                  |
     v                  v                  v
[Token Bucket]    [Leaky Bucket]    [Fixed Window]
     |                  |                  |
     v                  v                  v
Calculate tokens  Check queue size  Check counter
Refill if needed  Add to queue      in current window
     |                  |                  |
     v                  v                  v
Tokens >= 1?      Queue < Max?      Count < Limit?
     |                  |                  |
   YES/NO             YES/NO             YES/NO
     |                  |                  |
     +------------------+------------------+
                        |
                        v
                   [Decision]
                    /      \
                 YES        NO
                  |          |
                  v          v
            [Allow]      [Reject]
            Deduct       Return 429
            Forward      + Headers
                  |          |
                  v          v
               SUCCESS     BLOCKED
```

**Code (Token Bucket - Redis + Python):**

```python
import redis
import time

r = redis.Redis()

def token_bucket_limit(user_id, capacity=100, refill_rate=10):
    key = f"tb:{user_id}"
    now = time.time()
    
    # Lua script for atomic token calculation + deduction
    lua = """
    local capacity = tonumber(ARGV[1])
    local refill_rate = tonumber(ARGV[2])
    local now = tonumber(ARGV[3])
    
    local data = redis.call('HMGET', KEYS[1], 'tokens', 'last_refill')
    local tokens = tonumber(data[1]) or capacity  -- Initialize if not exists
    local last_refill = tonumber(data[2]) or now
    
    -- Calculate tokens to add
    local elapsed = now - last_refill
    local tokens_to_add = elapsed * refill_rate
    tokens = math.min(capacity, tokens + tokens_to_add)  -- Cap at capacity
    
    -- Check if request can be allowed
    if tokens >= 1 then
        tokens = tokens - 1  -- Deduct 1 token
        redis.call('HMSET', KEYS[1], 'tokens', tokens, 'last_refill', now)
        return {1, tokens}  -- Allowed, remaining tokens
    else
        return {0, 0}  -- Rejected
    end
    """
    
    result = r.eval(lua, 1, key, capacity, refill_rate, now)
    allowed = result[0] == 1
    remaining = result[1]
    
    return allowed, remaining

# Usage
allowed, remaining = token_bucket_limit("user123", capacity=10, refill_rate=1)
print(f"Allowed: {allowed}, Remaining: {remaining}")
```

---

## 📈 12. Trade-offs:

- **Token Bucket:** Gain: Burst traffic support, smooth UX | Loss: Complex refill logic, can allow sudden spikes (security risk if capacity too high)

- **Leaky Bucket:** Gain: Constant output rate, predictable load | Loss: No burst support (bad UX), queue memory overhead, requests delayed (latency)

- **Fixed Window:** Gain: Simple implementation, O(1) memory | Loss: Boundary exploitation (2x requests), inaccurate limiting

- **Sliding Window Log:** Gain: Perfect accuracy, no boundary issue | Loss: O(n) memory (100 timestamps per user), expensive cleanup (remove old timestamps)

- **Sliding Window Counter:** Gain: 99% accurate, O(1) memory, best balance | Loss: Slightly complex calculation, approximation (not 100% accurate)

**When to use what:**
- **API calls (general):** Token Bucket or Sliding Window Counter
- **Video streaming:** Leaky Bucket (constant bandwidth)
- **Login attempts:** Fixed Window (simplicity, security not critical for boundary)
- **Payment APIs:** Sliding Window Log (perfect accuracy needed)

---

## 🐞 13. Common Mistakes:

- **Mistake:** Using Fixed Window for critical APIs (banking, payments)
  - **Why wrong:** Boundary exploitation allows 2x requests in 2 seconds
  - **What happens:** Attacker sends 100 req at 12:00:59, 100 at 12:01:00 → Database overload
  - **Fix:** Use Sliding Window Counter or Token Bucket

- **Mistake:** Token Bucket with very high capacity (10,000 tokens)
  - **Why wrong:** User can send 10,000 requests in 1 second (burst too large)
  - **What happens:** Server crash despite rate limiting
  - **Fix:** Keep capacity = 2-3x of normal rate (if rate=100/sec, capacity=200-300)

- **Mistake:** Leaky Bucket for user-facing APIs
  - **Why wrong:** No burst support, user's requests queued → Slow response
  - **What happens:** Bad UX, users complain about slow app
  - **Fix:** Use Token Bucket for user APIs, Leaky Bucket for backend processing

- **Mistake:** Sliding Window Log without cleanup mechanism
  - **Why wrong:** Old timestamps accumulate → Memory leak
  - **What happens:** Redis memory full → OOM (Out of Memory) error
  - **Fix:** Set TTL on keys or use Sliding Window Counter (O(1) memory)

---

## ✅ 14. Zaroori Notes for Interview:

**Must Mention Points:**
1. **Start with comparison:** "4 main algorithms hain - Token Bucket (best for APIs), Leaky Bucket (constant output), Fixed Window (simple but flawed), Sliding Window (accurate). Main Token Bucket choose karunga kyunki burst traffic allow karta hai aur memory efficient hai."

2. **Draw Token Bucket diagram:** Bucket with tokens, refill rate arrow, request consuming token. Mention formula: `tokens = min(capacity, current + elapsed × rate)`.

3. **Explain boundary issue:** "Fixed Window mein problem hai - 12:00:59 par 100 requests, 12:01:00 par 100 requests = 200 in 2 seconds. Sliding Window solve karta hai by checking last 60 seconds ka rolling count."

4. **Common follow-ups:**
   - **"Token Bucket vs Leaky Bucket?"** → Token: Burst allowed, variable output. Leaky: No burst, constant output (queue-based). Token better for APIs, Leaky better for streaming.
   - **"Sliding Window Log vs Counter?"** → Log: Perfect accuracy, O(n) memory. Counter: 99% accurate, O(1) memory. Counter is best balance.
   - **"Capacity kaise decide karoge?"** → Capacity = 2-3x of refill rate. Example: Rate=100/sec → Capacity=200-300 (allows 2-3 sec burst).

5. **Implementation detail:** "Redis mein Lua script use karunga for atomic operations. Token calculation + deduction ek saath hoga (race condition prevent)."

6. **Real-world mention:** "Stripe uses Token Bucket, Cloudflare uses Sliding Window Counter, Nginx has built-in Leaky Bucket."

7. **Pro tip:** "Different endpoints ke liye different algorithms - Login API (Fixed Window, simple), Payment API (Sliding Log, accurate), General API (Token Bucket, flexible)."

---

## ❓ 15. FAQ & Comparisons (MANDATORY - 5 Questions):

**Q1: Token Bucket vs Leaky Bucket - Main difference kya hai?**
A: **Token Bucket:** Tokens accumulate (burst allowed), request immediately process hota hai agar tokens available. **Leaky Bucket:** Requests queue mein jaate hain, fixed rate se process (no burst). Example: Token Bucket mein user 10 sec wait kiya toh 10 requests ek saath bhej sakta hai. Leaky Bucket mein wo 10 requests bhi 1-1 karke process hongi (10 seconds lagenge). Token Bucket better for user-facing APIs, Leaky better for backend rate control.

**Q2: Fixed Window ki boundary problem kaise solve karein?**
A: **3 solutions:** (1) **Sliding Window Log** - Har request ka timestamp store, accurate but memory-heavy. (2) **Sliding Window Counter** - Previous + Current window ka weighted average, 99% accurate with O(1) memory (best). (3) **Token Bucket** - Burst control through capacity limit, no boundary issue. Most production systems use Sliding Window Counter (Cloudflare, Kong) kyunki accuracy aur memory dono balance hai.

**Q3: Token Bucket mein capacity kaise decide karein?**
A: **Formula:** Capacity = Refill_Rate × Burst_Duration. Example: Agar normal rate 100 req/sec hai aur 3 sec ka burst allow karna hai, toh Capacity = 100 × 3 = 300. Too high capacity (10,000) dangerous hai (attacker 10K requests ek saath bhej dega). Too low capacity (110 for 100/sec rate) means almost no burst (bad UX). Sweet spot: 2-3x of refill rate.

**Q4: Distributed system mein kaunsa algorithm best hai?**
A: **Token Bucket** ya **Sliding Window Counter** best hain. Dono O(1) memory use karte hain (Redis mein sirf 2-3 fields store). Sliding Window Log avoid karo kyunki har request ka timestamp store karna padega (memory expensive at scale). Implementation: Redis Cluster with Lua scripts for atomic operations. Token Bucket slightly simpler hai (sirf tokens aur last_refill store), Sliding Window Counter zyada accurate hai (prev_count, curr_count store).

**Q5: Leaky Bucket kab use karna chahiye?**
A: **Use cases:** (1) **Video Streaming** - Constant bandwidth chahiye (no jitter), (2) **Background Job Processing** - Fixed rate se jobs process (database overload prevent), (3) **Email Sending** - SMTP server ko constant rate chahiye (burst se block ho sakta hai). **Avoid:** User-facing APIs (bad UX due to queuing delay), Real-time systems (latency sensitive). Leaky Bucket ka main benefit: Output rate predictable hai, downstream systems overload nahi hote.

---



---

## Topic 13.3: Distributed Rate Limiter with Redis

---

## 🎯 1. Title / Topic: Distributed Rate Limiter Architecture (Redis + Lua Scripts)

---

## 🐣 2. Samjhane ke liye (Simple Analogy):

Imagine ek **Bank** hai jisme multiple **branches** hain (distributed servers). Ek customer ka **account balance** (rate limit counter) ek **central ledger** (Redis) mein store hai. Customer kisi bhi branch se withdrawal kar sakta hai, but balance check central ledger se hota hai. Agar Branch-1 aur Branch-2 dono simultaneously withdrawal process karein without coordination, toh **overdraft** ho sakta hai (limit exceed). Solution: **Atomic transactions** (Lua scripts) - ek time par sirf ek branch balance check + deduct kar sakti hai. Result: Consistent balance across all branches, no overdraft.

---

## 📖 3. Technical Definition (Interview Answer):

**Distributed Rate Limiter** is a rate limiting system that maintains consistent request counting across multiple application servers using a centralized data store (Redis) with atomic operations (Lua scripts) to prevent race conditions.

**Key terms:**
- **Distributed:** Multiple servers share same rate limit counter (not per-server limit)
- **Centralized Store:** Redis cluster stores counters (single source of truth)
- **Atomic Operations:** Lua scripts ensure read-check-update happens in one step (no race condition)
- **Race Condition:** Two servers simultaneously check counter (both see 99), both allow request → 101 total (limit bypass)
- **Consistency:** All servers see same counter value at any time

---

## 🧠 4. Zaroorat Kyun Hai? (Why?):

**Main Problem:** Agar har server apna local counter rakhega (in-memory), toh distributed system mein total limit enforce nahi hoga. Example: Limit=100/min, 5 servers hain. Har server 100 requests allow karega = 500 total (5x limit bypass).

**Business Impact:** Attacker 5 servers ko target karke 500 requests bhej sakta hai instead of 100. Server overload, DDoS attack successful, revenue loss.

**Technical Benefits:**
- **Global Limit Enforcement:** Saare servers ek hi counter share karte hain → Accurate limiting
- **Horizontal Scaling:** New servers add karo, counter consistent rahega (Redis shared)
- **Atomic Operations:** Race conditions prevent (Lua scripts), no limit bypass
- **High Availability:** Redis Cluster with replication → Counter data safe (Master-Slave)

---

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario):

**Scenario: Local In-Memory Counters (Wrong Approach)**
- System: 10 Load Balancer servers, each with local counter
- Limit: 100 requests/min per user
- Attacker: Sends 100 requests to each server (Round Robin)
- Result: Each server allows 100 → Total = 1000 requests (10x limit bypass)
- Impact: Database overload (1000 queries instead of 100), server crash, legitimate users affected

**Race Condition Without Lua:**
- Server-1 and Server-2 simultaneously check Redis counter (value=99)
- Both see 99 < 100 (limit not reached)
- Both increment: 99→100, 99→100
- Final value: 100 (should be 101)
- Result: 101st request allowed (limit bypass)

**Real Example:** **Shopify (2019)** - Flash sale without proper distributed rate limiting → Multiple servers allowed same user to checkout 50 items (limit was 10) → Inventory oversold → Customer refunds + bad PR. After implementing Redis + Lua atomic rate limiter, such incidents reduced by 99%.

---

## ⚙️ 6. Under the Hood (Technical Working):

**Distributed Rate Limiter Flow:**

1. **Request Arrival:** Client request Load Balancer-3 par aata hai (out of 10 LBs)
2. **Redis Connection:** LB-3 Redis Cluster se connect (centralized counter store)
3. **Lua Script Execution:** Atomic script run (GET counter → CHECK limit → INCREMENT → SET)
4. **Decision:** 
   - Counter < Limit → Allow, increment counter, forward request
   - Counter >= Limit → Reject, return HTTP 429
5. **TTL Management:** Redis key ka TTL set (60 sec for 1-min window), auto-expire
6. **Response:** Allowed request backend server ko forward, rejected request ko error response

**Key Components:**
- **Redis Cluster:** 3-5 Master nodes with Slaves (high availability, horizontal scaling)
- **Consistent Hashing:** User ID hash karke Redis node select (load distribution)
- **Lua Scripts:** Atomic operations (Redis single-threaded, Lua script atomically execute)
- **Connection Pooling:** Har server Redis connection pool maintain (reuse connections, low latency)

**ASCII Architecture Diagram:**

```
                    [Client/User: user123]
                            |
                            | Request #45
                            v
                    +----------------+
                    | Load Balancer  |
                    | (Round Robin)  |
                    +----------------+
                            |
        +-------------------+-------------------+
        |                   |                   |
        v                   v                   v
   +--------+          +--------+          +--------+
   | LB-1   |          | LB-2   |          | LB-3   |
   | (Rate  |          | (Rate  |          | (Rate  |
   | Limit) |          | Limit) |          | Limit) |
   +--------+          +--------+          +--------+
        |                   |                   |
        +-------------------+-------------------+
                            |
                            | (All connect to same Redis)
                            v
              +-----------------------------+
              |      Redis Cluster          |
              |  (Centralized Counters)     |
              |                             |
              | Master-1  Master-2  Master-3|
              |    |         |         |    |
              | Slave-1   Slave-2   Slave-3 |
              |                             |
              | Key: "rl:user123:api"       |
              | Value: 45 (counter)         |
              | TTL: 60 seconds             |
              +-----------------------------+
                            |
                            | (If allowed)
                            v
              +-----------------------------+
              |     Backend Servers         |
              |   (Process Request)         |
              +-----------------------------+

Flow:
1. LB-3 receives request from user123
2. LB-3 executes Lua script on Redis: GET-CHECK-INCR (atomic)
3. Redis returns: Allowed=true, Counter=46
4. LB-3 forwards request to backend
5. Backend processes and returns response
```

**Lua Script Execution (Atomic):**

```
Redis (Single-threaded):
    |
    v
[Lua Script Starts] ← Atomic block (no other operation can interrupt)
    |
    +---> GET counter (user123:api) → 45
    |
    +---> CHECK: 45 < 100? YES
    |
    +---> INCR: 45 → 46
    |
    +---> SET counter = 46, TTL = 60 sec
    |
    +---> RETURN: {allowed: true, remaining: 54}
    |
[Lua Script Ends] ← Atomic block ends
    |
    v
Next operation can execute
```

---

## 🛠️ 7. Problems Solved:

- **Race Conditions:** Lua scripts ensure atomic operations → Two servers can't simultaneously bypass limit (GET-CHECK-INCR ek saath)
- **Distributed Consistency:** All servers share Redis counter → Global limit enforced (not per-server limit)
- **Horizontal Scaling:** Add 100 servers, counter consistent rahega → No code change needed
- **High Availability:** Redis Master-Slave replication → Master crash toh Slave promote (counter data safe)
- **Low Latency:** Redis in-memory store → Counter check in <1ms (vs database 10-50ms)
- **Auto Cleanup:** TTL on keys → Expired counters automatically delete (no manual cleanup, memory efficient)

---

## 🌍 8. Real-World Example:

**GitHub API:** 5000 requests/hour for authenticated users, distributed across 1000+ servers globally. Implementation: Redis Cluster (50+ nodes) with Token Bucket algorithm via Lua scripts. Key structure: `ratelimit:{user_id}:{endpoint}` (e.g., `ratelimit:user123:repos`). Scale: 100M+ API calls/day. Latency: <2ms for rate limit check. Benefit: Consistent limiting across all regions (US, EU, Asia servers share same Redis cluster via geo-replication). Headers: `X-RateLimit-Limit: 5000`, `X-RateLimit-Remaining: 4850`, `X-RateLimit-Reset: 1638360000`. This prevented 99.9% of abuse attempts while maintaining 99.99% uptime.

---

## 🔧 9. Tech Stack / Tools:

- **Redis Cluster:** Distributed in-memory store with sharding. Use for: High throughput (100K ops/sec per node), automatic failover (Sentinel), horizontal scaling. Setup: 3 Master + 3 Slave nodes minimum for production.

- **Redis Sentinel:** High availability solution. Use for: Automatic Master-Slave failover (Master down → Slave promoted in <30 sec), monitoring, notifications. Config: 3+ Sentinel instances for quorum.

- **Lua Scripts:** Embedded scripting in Redis. Use for: Atomic multi-step operations (GET-CHECK-INCR), complex logic (Token Bucket refill calculation), no network round-trips (all logic on Redis server).

- **Connection Pooling (redis-py, Jedis):** Reusable connections. Use for: Low latency (no connection overhead), resource efficiency (max 50 connections per server), automatic reconnection on failure.

---

## 📐 10. Architecture/Formula:

**Redis Key Structure:**

```
Pattern: ratelimit:{user_id}:{endpoint}:{algorithm}

Examples:
- ratelimit:user123:api:token_bucket
- ratelimit:192.168.1.1:login:fixed_window
- ratelimit:apikey_abc:search:sliding_window

Value (Hash):
{
    "tokens": 45,              // Token Bucket
    "last_refill": 1638360000, // Timestamp
    "capacity": 100,
    "refill_rate": 10
}

TTL: 60-3600 seconds (auto-expire)
```

**Consistent Hashing for Redis Sharding:**

```
Formula: Redis_Node = hash(user_id) % total_nodes

Example:
user_id = "user123"
hash("user123") = 456789
total_nodes = 3

Redis_Node = 456789 % 3 = 0 → Master-1

Benefits:
- Load distribution across nodes
- Same user always goes to same node (cache locality)
- Add/remove nodes: Only 1/n keys rehash (minimal disruption)
```

**Lua Script Atomic Operation:**

```
Lua Script (Token Bucket):

KEYS[1] = "ratelimit:user123:api"
ARGV[1] = capacity (100)
ARGV[2] = refill_rate (10)
ARGV[3] = current_time (1638360000)

Script:
1. HGET tokens, last_refill from KEYS[1]
2. Calculate: tokens_to_add = (current_time - last_refill) × refill_rate
3. New_tokens = min(capacity, tokens + tokens_to_add)
4. IF new_tokens >= 1:
     new_tokens -= 1
     HSET KEYS[1] tokens=new_tokens, last_refill=current_time
     RETURN {1, new_tokens}  // Allowed
   ELSE:
     RETURN {0, 0}  // Rejected

Atomicity: Redis single-threaded → Lua script executes without interruption
```

**High Availability Architecture:**

```
                [Application Servers]
                    |    |    |
                    v    v    v
              +------------------+
              | Redis Sentinel   |
              | (Monitor Master) |
              +------------------+
                    |    |    |
        +-----------+    |    +-----------+
        |                |                |
        v                v                v
   +--------+       +--------+       +--------+
   |Master-1|       |Master-2|       |Master-3|
   | (Shard |       | (Shard |       | (Shard |
   |  0-33%)|       | 34-66%)|       | 67-99%)|
   +--------+       +--------+       +--------+
        |                |                |
        v                v                v
   +--------+       +--------+       +--------+
   |Slave-1 |       |Slave-2 |       |Slave-3 |
   |(Replica|       |(Replica|       |(Replica|
   +--------+       +--------+       +--------+

Failover:
Master-1 crashes → Sentinel detects (3 sec) → Slave-1 promoted to Master
→ Application servers auto-reconnect → Downtime: <5 seconds
```

---

## 💻 11. Code / Flowchart:

**Flowchart (Distributed Rate Limiter with Redis):**

```
START: Request arrives at LB-2
     |
     v
[Extract user_id from request]
user_id = "user123"
     |
     v
[Generate Redis key]
key = "ratelimit:user123:api"
     |
     v
[Connect to Redis Cluster]
(Connection pool: reuse existing)
     |
     v
[Execute Lua Script] ← ATOMIC BLOCK
     |
     +---> GET current tokens
     |
     +---> Calculate refill
     |
     +---> Check: tokens >= 1?
     |          |
     |          v
     |      YES / NO
     |          |
     +----------+
     |
     v
[Lua returns result]
{allowed: true/false, remaining: X}
     |
     v
[Decision]
     |
     +---> allowed == true?
     |          |
     |          v
     |        YES: Forward to backend
     |          |
     |          v
     |     [Backend processes]
     |          |
     v          v
    NO      SUCCESS
     |
     v
[Return HTTP 429]
Headers:
- Retry-After: 45
- X-RateLimit-Remaining: 0
     |
     v
   BLOCKED
```

**Code (Production-Ready Distributed Rate Limiter):**

```python
import redis
import time
import hashlib

class DistributedRateLimiter:
    def __init__(self, redis_nodes):
        # Redis Cluster connection pool
        self.redis_pool = redis.ConnectionPool(
            host='redis-cluster.example.com',
            port=6379,
            max_connections=50,  # Connection pooling
            decode_responses=True
        )
        self.redis_client = redis.Redis(connection_pool=self.redis_pool)
        
        # Lua script for atomic Token Bucket (loaded once, reused)
        self.lua_script = self.redis_client.register_script("""
            local key = KEYS[1]
            local capacity = tonumber(ARGV[1])
            local refill_rate = tonumber(ARGV[2])
            local now = tonumber(ARGV[3])
            local cost = tonumber(ARGV[4])
            
            local data = redis.call('HMGET', key, 'tokens', 'last_refill')
            local tokens = tonumber(data[1]) or capacity
            local last_refill = tonumber(data[2]) or now
            
            -- Refill tokens
            local elapsed = now - last_refill
            local tokens_to_add = elapsed * refill_rate
            tokens = math.min(capacity, tokens + tokens_to_add)
            
            -- Check and deduct
            if tokens >= cost then
                tokens = tokens - cost
                redis.call('HMSET', key, 'tokens', tokens, 'last_refill', now)
                redis.call('EXPIRE', key, 3600)  -- TTL: 1 hour
                return {1, math.floor(tokens)}  -- Allowed, remaining
            else
                return {0, 0}  -- Rejected
            end
        """)
    
    def check_rate_limit(self, user_id, endpoint, capacity=100, refill_rate=10):
        # Generate key with consistent hashing
        key = f"ratelimit:{user_id}:{endpoint}"
        now = time.time()
        
        try:
            # Execute Lua script (atomic operation)
            result = self.lua_script(
                keys=[key],
                args=[capacity, refill_rate, now, 1]  # cost=1 token
            )
            
            allowed = result[0] == 1
            remaining = result[1]
            
            return {
                'allowed': allowed,
                'remaining': remaining,
                'limit': capacity,
                'reset': int(now) + 60  # Reset time
            }
        
        except redis.RedisError as e:
            # Fallback: Fail-open (allow request if Redis down)
            print(f"Redis error: {e}. Failing open.")
            return {'allowed': True, 'remaining': -1}

# Usage
limiter = DistributedRateLimiter(redis_nodes=['node1', 'node2', 'node3'])

result = limiter.check_rate_limit(
    user_id="user123",
    endpoint="api_call",
    capacity=100,
    refill_rate=10  # 10 tokens/sec
)

if result['allowed']:
    print(f"✅ Request allowed. Remaining: {result['remaining']}")
    # Forward to backend
else:
    print(f"❌ Rate limit exceeded. Retry after: {result['reset']}")
    # Return HTTP 429
```

---

## 📈 12. Trade-offs:

- **Gain:** Global consistency (all servers share counter), accurate limiting | **Loss:** Redis dependency (single point of failure), network latency (+1-2ms per request for Redis call)

- **Gain:** Horizontal scaling (add servers without code change), high throughput (100K+ ops/sec) | **Loss:** Infrastructure cost (Redis Cluster = 6+ nodes for HA), operational complexity (monitoring, failover)

- **Gain:** Atomic operations (no race conditions), low latency (<1ms Redis) | **Loss:** Lua script complexity (debugging harder than application code), Redis version dependency (Lua support needed)

- **When to use:** Distributed systems (multiple servers), high traffic (>1000 RPS), public APIs (strict limiting needed) | **When to skip:** Single server apps (local counter sufficient), very low traffic (<100 users), internal microservices (trusted environment)

---

## 🐞 13. Common Mistakes:

- **Mistake:** Using separate GET-CHECK-INCR commands instead of Lua script
  - **Why wrong:** Race condition - Two servers simultaneously GET (both see 99), both INCR → 101 total
  - **What happens:** Limit bypass, attacker can exploit by sending parallel requests
  - **Fix:** Use Lua script for atomic operation (GET-CHECK-INCR in one step)

- **Mistake:** Not setting TTL on Redis keys
  - **Why wrong:** Expired counters never delete → Memory leak → Redis OOM (Out of Memory)
  - **What happens:** Redis crashes, all rate limiting stops (fail-open or fail-closed)
  - **Fix:** Always set TTL (EXPIRE command) = window size (60 sec for 1-min window)

- **Mistake:** Single Redis instance (no replication)
  - **Why wrong:** Redis crash → All rate limiting stops → Either all requests allowed (security risk) or all blocked (bad UX)
  - **What happens:** Downtime, potential DDoS attack during Redis outage
  - **Fix:** Redis Cluster with Master-Slave replication + Sentinel for auto-failover

- **Mistake:** Not using connection pooling
  - **Why wrong:** Every request creates new Redis connection → High latency (TCP handshake), connection exhaustion
  - **What happens:** Slow rate limit checks (50ms instead of 1ms), Redis max connections reached (10K limit)
  - **Fix:** Connection pool with 50-100 connections per server (reuse connections)

- **Mistake:** Hardcoding Redis host in application
  - **Why wrong:** Redis failover toh application restart needed (manual intervention)
  - **What happens:** Downtime during Redis maintenance/failover
  - **Fix:** Use Redis Sentinel or service discovery (Consul) for dynamic Redis endpoint

---

## ✅ 14. Zaroori Notes for Interview:

**Must Mention Points:**
1. **Start with problem:** "Distributed system mein har server ka local counter nahi chal sakta, kyunki total limit enforce nahi hoga. Example: 10 servers, limit=100 → Har server 100 allow karega = 1000 total. Solution: Centralized Redis with atomic Lua scripts."

2. **Draw architecture:** Multiple LB servers → Redis Cluster (Master-Slave) → Backend. Mention: All LBs share same Redis counter, consistent hashing for load distribution.

3. **Explain atomicity:** "Redis single-threaded hai, Lua script atomically execute hota hai. GET-CHECK-INCR ek saath hota hai, koi beech mein interrupt nahi kar sakta. Ye race condition prevent karta hai."

4. **Common follow-ups:**
   - **"Redis down ho gaye toh?"** → Fail-open (allow all - risky) ya Fail-closed (block all - bad UX) ya Local cache fallback. Best: Redis Sentinel with auto-failover (Master crash → Slave promoted in <30 sec).
   - **"Latency kaise reduce karoge?"** → (1) Connection pooling (reuse connections), (2) Redis pipelining (batch commands), (3) Geo-distributed Redis (region-wise clusters).
   - **"Lua script vs Application logic?"** → Lua: Atomic, low latency (no network round-trips), but debugging hard. Application: Flexible, easy debug, but race conditions (need distributed locks).

5. **Mention key structure:** `ratelimit:{user_id}:{endpoint}` with TTL = window size. Consistent hashing for Redis node selection.

6. **High availability:** "Redis Cluster with 3 Master + 3 Slave nodes. Sentinel monitors Masters, auto-failover on crash. Downtime: <5 seconds."

7. **Pro tip:** "Always return proper headers - `X-RateLimit-Remaining`, `Retry-After`. Client ko pata chalega kab retry kare, blind retries nahi hongi (load reduce)."

---

## ❓ 15. FAQ & Comparisons (MANDATORY - 5 Questions):

**Q1: Lua script vs Distributed Lock (Redlock) - Kaunsa better hai?**
A: **Lua script** better hai for rate limiting. Lua: Atomic, fast (<1ms), simple (ek script call). Redlock: Complex (multiple Redis nodes se lock acquire), slow (5-10ms), overkill for simple counter increment. Lua script Redis ke single-threaded nature ka advantage leta hai (atomicity guarantee). Redlock use karo sirf jab complex multi-step operations ho (e.g., distributed transactions). Rate limiting ke liye Lua sufficient hai.

**Q2: Redis Cluster vs Redis Sentinel - Kab kaunsa use karein?**
A: **Redis Sentinel:** Single Master-Slave setup with auto-failover. Use for: Small-medium scale (<100K ops/sec), simple setup, high availability. **Redis Cluster:** Multiple Masters with sharding. Use for: Large scale (>100K ops/sec), horizontal scaling (data distributed across nodes), very high throughput. Rate limiting ke liye: Start with Sentinel (simple), scale to Cluster jab traffic bahut zyada ho (>1M requests/sec).

**Q3: Connection pooling kaise implement karein aur size kya rakhe?**
A: **Implementation:** redis-py mein `ConnectionPool` use karo, max_connections set karo. **Size calculation:** `Pool_Size = (Expected_RPS / Server_Count) × Avg_Response_Time`. Example: 10K RPS, 10 servers, 1ms Redis latency → Pool_Size = (10K/10) × 0.001 = 1 connection (but keep buffer) → Set 50-100. Too small: Connection wait time (latency). Too large: Memory waste, Redis connection limit (default 10K). Monitor: Connection usage metrics (idle vs active).

**Q4: TTL kaise set karein aur kya hoga agar TTL miss ho jaye?**
A: **TTL setting:** Window size ke equal (1-min window → TTL=60 sec). Lua script mein `EXPIRE` command use karo har update par. **TTL miss scenario:** Agar EXPIRE command fail (Redis crash during execution), toh key never expire → Memory leak. **Solution:** (1) Lua script mein EXPIRE zaroori (har HMSET ke baad), (2) Background cleanup job (scan expired keys manually - slow, avoid), (3) Redis maxmemory-policy=allkeys-lru (auto-evict old keys if memory full).

**Q5: Geo-distributed system mein rate limiting kaise handle karein?**
A: **2 approaches:** (1) **Global Counter (Single Redis Cluster):** All regions connect to one Redis (e.g., US-East). Pros: Accurate global limit. Cons: High latency for far regions (Asia → US = 200ms). (2) **Regional Counters (Multiple Redis Clusters):** Har region ka apna Redis, eventual consistency via sync. Pros: Low latency (<5ms local). Cons: Limit slightly inaccurate (Asia=50, EU=50 = 100 total, but limit was 80). **Best:** Regional counters with 80% local limit (Asia=40, EU=40 = 80 total), sync every 10 sec for adjustment.

---



---

## Topic 13.4: Advanced Rate Limiting Patterns

---

## 🎯 1. Title / Topic: Advanced Rate Limiting (Multi-tier, Geo-based, Adaptive, Per-Endpoint)

---

## 🐣 2. Samjhane ke liye (Simple Analogy):

Imagine ek **Smart Gym** hai jo different members ko different access deta hai:
1. **Multi-tier:** Basic member (10 visits/month), Premium (unlimited) - membership level ke basis par limit
2. **Geo-based:** Delhi gym crowded hai toh Delhi members ko 5 visits/week, Mumbai gym empty hai toh unlimited
3. **Adaptive:** Monday morning rush hai toh limit reduce (5/hour), Sunday evening empty hai toh increase (20/hour)
4. **Per-Endpoint:** Treadmill (30 min limit - heavy resource), Yoga room (2 hour limit - light resource)

Result: Fair usage, resource optimization, better experience for all members.

---

## 📖 3. Technical Definition (Interview Answer):

**Advanced Rate Limiting** involves dynamic, context-aware request throttling based on multiple factors like user tier, geographic location, system load, and resource type.

**Key Patterns:**
- **Multi-tier Limiting:** Different limits for different user tiers (Free=100/day, Pro=10K/day, Enterprise=unlimited)
- **Geo-based Limiting:** Region-specific limits based on infrastructure capacity (US=1000/sec, Asia=500/sec)
- **Adaptive Limiting:** Dynamic limit adjustment based on system load (CPU>80% → reduce limit by 50%)
- **Per-Endpoint Limiting:** Different limits for different APIs (GET /search=1000/min, POST /upload=10/min)
- **Cost-based Limiting:** Weighted requests (simple query=1 token, complex query=10 tokens)

---

## 🧠 4. Zaroorat Kyun Hai? (Why?):

**Main Problem:** One-size-fits-all rate limiting inefficient hai. Free users aur Paid users ko same limit dena unfair hai. Heavy endpoints (video upload) aur light endpoints (profile view) ko same limit dena resource wastage hai.

**Business Impact:** 
- Revenue loss: Paid users ko extra benefits nahi mile toh churn
- Poor UX: System load high hai but limit same → Slow response for all users
- Resource waste: Light APIs ko heavy limit → Attackers exploit

**Technical Benefits:**
- **Monetization:** Tiered pricing enable (Free vs Pro vs Enterprise)
- **Resource Optimization:** Heavy endpoints ko strict limit → Server protected
- **Fairness:** Geo-based limits ensure all regions get fair access
- **Resilience:** Adaptive limits prevent cascading failures during traffic spikes

---

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario):

**Scenario 1 - No Multi-tier (All users same limit):**
- Free user: 10K requests/day (abuses system, costs money)
- Enterprise user: 10K requests/day (insufficient, complains, churns)
- Business: Can't monetize API, revenue loss

**Scenario 2 - No Per-Endpoint Limiting:**
- Video upload API: Same limit as profile view (1000/min)
- Attacker: Uploads 1000 videos/min (each 100MB) → 100GB/min bandwidth
- Server: Bandwidth exhausted, storage full, crash
- Legitimate users: Can't even view profiles

**Scenario 3 - No Adaptive Limiting:**
- Black Friday: Traffic 10x normal, but limit same
- System: CPU 100%, database slow, cascading failures
- Result: Complete outage instead of graceful degradation

**Real Example:** **Twitter API (2022)** - No proper per-endpoint limiting → Attackers scraped 400M user profiles via search API (light endpoint with high limit). After implementing cost-based limiting (search=10 tokens, profile=1 token), scraping reduced by 95%.

---

## ⚙️ 6. Under the Hood (Technical Working):

### **Pattern 1: Multi-tier Rate Limiting**

**Working:**
1. User authentication → Extract user tier (Free/Pro/Enterprise)
2. Lookup tier limits from config (Free=100/day, Pro=10K/day)
3. Redis key includes tier: `ratelimit:user123:free:api`
4. Apply tier-specific limit
5. Upgrade/downgrade → Key changes automatically

**Data Structure:**
```
User DB: {user_id: "user123", tier: "pro", limit: 10000}
Redis Key: "ratelimit:user123:pro:api"
Config: {free: 100, pro: 10000, enterprise: -1}  // -1 = unlimited
```

### **Pattern 2: Geo-based Rate Limiting**

**Working:**
1. Extract user IP → Geo-lookup (IP to Country/Region)
2. Check region capacity (US servers: 80% load, Asia: 40% load)
3. Apply region-specific limit (US=500/min, Asia=1000/min)
4. Redis key: `ratelimit:user123:US:api`

**Data Structure:**
```
GeoIP DB: {IP: "192.168.1.1", region: "US"}
Region Config: {US: {limit: 500, load: 80%}, Asia: {limit: 1000, load: 40%}}
```

### **Pattern 3: Adaptive Rate Limiting**

**Working:**
1. Monitor system metrics (CPU, Memory, DB connections)
2. Calculate load factor (CPU=80% → factor=0.5)
3. Adjust limit dynamically (base_limit × factor)
4. Update Redis config every 10 seconds
5. Gradual recovery (load decreases → limit increases)

**Formula:**
```
Adaptive_Limit = Base_Limit × Load_Factor

Load_Factor calculation:
IF CPU < 50%: factor = 1.0 (no reduction)
IF CPU 50-70%: factor = 0.8 (20% reduction)
IF CPU 70-90%: factor = 0.5 (50% reduction)
IF CPU > 90%: factor = 0.2 (80% reduction)

Example:
Base_Limit = 1000/min, CPU = 85%
Load_Factor = 0.5
Adaptive_Limit = 1000 × 0.5 = 500/min
```

### **Pattern 4: Per-Endpoint Cost-based Limiting**

**Working:**
1. Define endpoint costs (GET /profile=1, POST /upload=50)
2. User has token bucket (capacity=1000 tokens)
3. Request arrives → Deduct cost from bucket
4. Heavy endpoints consume more tokens
5. Prevents abuse of resource-intensive APIs

**Data Structure:**
```
Endpoint Costs: {
    "GET /profile": 1,
    "GET /search": 5,
    "POST /upload": 50,
    "POST /video": 200
}

User Bucket: {tokens: 800, capacity: 1000, refill: 10/sec}
```

**ASCII Architecture Diagram:**

```
[User Request: user123, tier=pro, region=US, endpoint=/upload]
     |
     v
+------------------+
| Rate Limiter     |
| (Multi-factor)   |
+------------------+
     |
     +---> [1] Check User Tier
     |         pro → limit=10K/day
     |
     +---> [2] Check Geo Region
     |         US → region_limit=500/min
     |
     +---> [3] Check System Load
     |         CPU=75% → adaptive_factor=0.8
     |         Adjusted: 500×0.8=400/min
     |
     +---> [4] Check Endpoint Cost
     |         /upload → cost=50 tokens
     |
     v
[Calculate Final Limit]
Min(tier_limit, region_limit×adaptive_factor)
Min(10K/day, 400/min) = 400/min
     |
     v
[Redis: Deduct 50 tokens]
Key: "ratelimit:user123:pro:US:upload"
Tokens: 350 → 300 (allowed)
     |
     v
[Forward to Backend]


--- REJECTION FLOW ---

[Free User: tier=free, endpoint=/video]
     |
     v
[Check Tier: free → 100/day]
[Check Endpoint: /video → cost=200 tokens]
     |
     v
[Redis: Current tokens=50]
50 < 200 → REJECT
     |
     v
[HTTP 429: Upgrade to Pro for video uploads]
```

---

## 🛠️ 7. Problems Solved:

- **API Monetization:** Multi-tier enables pricing (Free/Pro/Enterprise) → Revenue generation, clear upgrade path
- **Resource Protection:** Cost-based limiting prevents abuse of heavy endpoints → Server stable, costs controlled
- **Fair Distribution:** Geo-based ensures all regions get proportional access → No region starved
- **Graceful Degradation:** Adaptive limiting reduces load during spikes → Partial service better than complete outage
- **Abuse Prevention:** Combining multiple factors (tier + geo + endpoint) → Sophisticated attack detection

---

## 🌍 8. Real-World Example:

**AWS API Gateway:** Implements all 4 patterns. Multi-tier: Free tier (1M requests/month), Paid (unlimited with per-request cost). Per-endpoint: Lambda invocation (10 tokens), S3 upload (50 tokens). Adaptive: Auto-scales limits based on account history (new accounts=strict, trusted=relaxed). Geo-based: Region-specific quotas (us-east-1 higher than ap-south-1). Scale: 10B+ requests/day. Cost savings: 40% reduction in abuse-related costs. Implementation: Custom rate limiter with DynamoDB for state, CloudWatch for metrics. Headers: `X-Amzn-RateLimit-Limit`, `X-Amzn-RequestId`.

---

## 🔧 9. Tech Stack / Tools:

- **Kong (Enterprise):** Multi-tier + per-endpoint limiting via plugins. Use for: Complex routing, policy-based limits, analytics dashboard. Config: YAML-based tier definitions.

- **AWS API Gateway:** Built-in throttling with usage plans. Use for: AWS ecosystem, serverless, automatic scaling. Features: Burst limits, steady-state limits, per-method limits.

- **Custom (Redis + Application Logic):** Full control over all patterns. Use for: Unique requirements, cost optimization, learning. Implementation: Lua scripts for atomic operations, config in Redis/DB.

---

## 📐 10. Architecture/Formula:

**Multi-factor Rate Limit Calculation:**

```
Final_Limit = MIN(
    Tier_Limit,
    Geo_Limit × Adaptive_Factor,
    Endpoint_Limit
)

Token_Cost = Endpoint_Cost × Request_Size_Factor

Example:
User: Pro tier (10K/day = 416/hour = 6.9/min ≈ 7/min)
Geo: US region (500/min)
System: CPU=80% → Adaptive_Factor=0.5
Endpoint: /upload (cost=50 tokens)

Calculations:
1. Tier_Limit = 7/min (converted from daily)
2. Geo_Limit = 500/min × 0.5 = 250/min
3. Endpoint_Limit = 1000 tokens / 50 = 20 requests/min

Final_Limit = MIN(7, 250, 20) = 7/min (tier is bottleneck)

User can make 7 upload requests per minute (tier limit)
```

**Adaptive Factor Formula:**

```
Load_Factor = MAX(0.2, 1 - (Current_Load - Threshold) / (100 - Threshold))

Where:
- Threshold = 50% (start reducing after this)
- Current_Load = CPU/Memory/DB connections percentage
- MIN factor = 0.2 (never reduce below 20% of base limit)

Example:
Current_CPU = 85%, Threshold = 50%
Load_Factor = 1 - (85 - 50) / (100 - 50)
            = 1 - 35/50
            = 1 - 0.7
            = 0.3

Base_Limit = 1000/min
Adaptive_Limit = 1000 × 0.3 = 300/min
```

**Decision Tree Diagram:**

```
REQUEST ARRIVES
     |
     v
[Extract Context]
- User ID + Tier
- IP + Geo Region
- Endpoint + Method
- System Metrics
     |
     v
[Calculate Limits]
     |
     +---> Tier Limit (from DB)
     |     free=100, pro=10K, enterprise=∞
     |
     +---> Geo Limit (from config)
     |     US=500, EU=800, Asia=300
     |
     +---> Adaptive Limit (from metrics)
     |     CPU<50%=1.0x, 50-70%=0.8x, >90%=0.2x
     |
     +---> Endpoint Cost (from config)
     |     GET=1, POST=10, Upload=50
     |
     v
[Apply MIN of all limits]
Final = MIN(tier, geo×adaptive, endpoint)
     |
     v
[Redis: Check + Deduct tokens]
     |
     +---> Tokens >= Cost?
     |          |
     |        YES/NO
     |          |
     +----------+
     |
     v
[ALLOW or REJECT]
```

---

## 💻 11. Code / Flowchart:

**Flowchart (Multi-factor Rate Limiting):**

```
START
  |
  v
[Parse Request]
user_id, tier, ip, endpoint
  |
  v
[Lookup Tier Limit]
tier_limits = {free: 100, pro: 10000}
user_limit = tier_limits[tier]
  |
  v
[Geo Lookup]
region = geoip(ip)  // US, EU, Asia
geo_limit = region_limits[region]
  |
  v
[Get System Metrics]
cpu_usage = get_cpu()
adaptive_factor = calculate_factor(cpu_usage)
  |
  v
[Get Endpoint Cost]
cost = endpoint_costs[endpoint]
  |
  v
[Calculate Final Limit]
final = MIN(user_limit, geo_limit × adaptive_factor)
  |
  v
[Redis: Check Tokens]
key = f"rl:{user_id}:{tier}:{region}:{endpoint}"
current_tokens = redis.get(key)
  |
  v
[Decision]
current_tokens >= cost?
  |
  +---> YES: Deduct tokens
  |          Forward request
  |          Return 200
  |
  +---> NO: Reject
           Return 429
           Headers: Retry-After, Upgrade-Tier
  |
  v
END
```

**Code (Advanced Multi-factor Rate Limiter):**

```python
import redis
import time
from typing import Dict

class AdvancedRateLimiter:
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379)
        
        # Configuration
        self.tier_limits = {
            'free': 100,      # per day
            'pro': 10000,
            'enterprise': -1  # unlimited
        }
        
        self.geo_limits = {
            'US': 500,   # per minute
            'EU': 800,
            'Asia': 300
        }
        
        self.endpoint_costs = {
            'GET /profile': 1,
            'GET /search': 5,
            'POST /upload': 50,
            'POST /video': 200
        }
    
    def get_adaptive_factor(self, cpu_usage: float) -> float:
        """Calculate load-based factor"""
        if cpu_usage < 50:
            return 1.0
        elif cpu_usage < 70:
            return 0.8
        elif cpu_usage < 90:
            return 0.5
        else:
            return 0.2
    
    def check_limit(self, user_id: str, tier: str, region: str, 
                    endpoint: str, cpu_usage: float) -> Dict:
        # Get limits
        tier_limit = self.tier_limits.get(tier, 100)
        geo_limit = self.geo_limits.get(region, 100)
        endpoint_cost = self.endpoint_costs.get(endpoint, 1)
        
        # Adaptive adjustment
        adaptive_factor = self.get_adaptive_factor(cpu_usage)
        adjusted_geo = int(geo_limit * adaptive_factor)
        
        # Final limit (convert daily to per-minute for tier)
        tier_per_min = tier_limit / (24 * 60) if tier_limit > 0 else float('inf')
        final_limit = min(tier_per_min, adjusted_geo)
        
        # Redis key
        key = f"rl:{user_id}:{tier}:{region}:{endpoint}"
        
        # Check tokens (Token Bucket)
        current = self.redis.get(key)
        tokens = float(current) if current else final_limit
        
        if tokens >= endpoint_cost:
            # Deduct and allow
            new_tokens = tokens - endpoint_cost
            self.redis.setex(key, 60, new_tokens)  # TTL 60 sec
            
            return {
                'allowed': True,
                'remaining': int(new_tokens / endpoint_cost),
                'limit': int(final_limit),
                'cost': endpoint_cost,
                'tier': tier
            }
        else:
            return {
                'allowed': False,
                'remaining': 0,
                'limit': int(final_limit),
                'retry_after': 60,
                'message': f'Upgrade to Pro for {endpoint}'
            }

# Usage
limiter = AdvancedRateLimiter()

result = limiter.check_limit(
    user_id='user123',
    tier='free',
    region='US',
    endpoint='POST /upload',
    cpu_usage=75.0
)

if result['allowed']:
    print(f"✅ Allowed. Remaining: {result['remaining']}")
else:
    print(f"❌ Blocked. {result['message']}")
```

---

## 📈 12. Trade-offs:

- **Gain:** Flexible monetization, fair resource distribution, better UX | **Loss:** Complex configuration, harder debugging, more Redis keys (memory)

- **Gain:** Graceful degradation during load spikes, prevents cascading failures | **Loss:** Legitimate users affected during high load, need careful threshold tuning

- **Gain:** Prevents abuse of expensive endpoints, cost optimization | **Loss:** Complexity in defining costs, need to update costs as system evolves

- **When to use:** SaaS products (tiered pricing), public APIs (abuse prevention), high-scale systems (>10K RPS) | **When to skip:** Internal tools (trusted users), simple apps (single tier sufficient), low traffic (<100 users)

---

## 🐞 13. Common Mistakes:

- **Mistake:** Too many factors (tier + geo + endpoint + time + user_agent + ...)
  - **Why wrong:** Complexity explosion, hard to debug, Redis key explosion
  - **What happens:** Memory issues, slow lookups, configuration nightmare
  - **Fix:** Start with 2-3 factors (tier + endpoint), add more only if needed

- **Mistake:** Adaptive factor changes too frequently (every second)
  - **Why wrong:** Limits fluctuate rapidly, bad UX (user confused why limit changed)
  - **What happens:** Users hit limits unexpectedly, support tickets increase
  - **Fix:** Update adaptive factor every 30-60 seconds, smooth transitions

- **Mistake:** Not communicating tier limits to users
  - **Why wrong:** Users don't know their limits, frustrated when blocked
  - **What happens:** Support tickets, bad reviews, churn
  - **Fix:** Return headers (`X-RateLimit-Tier: free`, `X-RateLimit-Upgrade-URL`)

- **Mistake:** Endpoint costs not aligned with actual resource usage
  - **Why wrong:** Light endpoint has high cost → Users frustrated, Heavy endpoint has low cost → Abuse
  - **What happens:** Poor resource utilization, user complaints
  - **Fix:** Profile endpoints (measure CPU/memory/time), set costs proportionally

---

## ✅ 14. Zaroori Notes for Interview:

**Must Mention Points:**
1. **Start with business need:** "Simple rate limiting sab users ko same treat karta hai. But business mein Free vs Paid users hote hain, heavy vs light endpoints hote hain. Advanced patterns enable monetization aur fair resource distribution."

2. **Explain multi-tier:** "User tier (Free/Pro/Enterprise) ke basis par different limits. Redis key mein tier include: `rl:user123:pro:api`. Upgrade/downgrade automatic reflect hota hai."

3. **Draw decision flow:** User request → Extract (tier, geo, endpoint) → Calculate limits → Apply MIN → Redis check → Allow/Reject

4. **Common follow-ups:**
   - **"Adaptive limiting kaise implement karoge?"** → Monitor CPU/Memory every 30 sec → Calculate load factor (CPU>80% → 0.5x) → Update Redis config → All servers read config → Gradual adjustment
   - **"Cost-based limiting ka formula?"** → Endpoint cost define (GET=1, Upload=50) → Token Bucket with weighted deduction → Heavy endpoints consume more tokens
   - **"Tier upgrade real-time kaise reflect hoga?"** → Redis key mein tier include → Upgrade event → New key create with new tier → Old key expire naturally (TTL)

5. **Mention real-world:** "AWS API Gateway uses all patterns. Stripe uses cost-based (simple API=1, complex=10). Twitter uses per-endpoint (tweet=1, search=5)."

6. **Pro tip:** "Return upgrade CTA in 429 response: `Upgrade to Pro for unlimited uploads - /pricing`. Converts frustrated users to paying customers."

---

## ❓ 15. FAQ & Comparisons (MANDATORY - 5 Questions):

**Q1: Multi-tier limiting mein tier change (upgrade/downgrade) kaise handle karein?**
A: **Approach:** Redis key mein tier include (`rl:user123:free:api`). Upgrade event → New key create (`rl:user123:pro:api`), old key naturally expire (TTL). **Immediate effect:** Next request new tier use karega. **Gradual transition:** Optional - Agar user ne free tier mein 90/100 use kiya, upgrade ke baad pro tier mein 90 carry forward (grace period). Implementation: Check both keys, take max remaining. **Edge case:** Downgrade → Immediately enforce new limit (no grace).

**Q2: Adaptive limiting mein threshold kaise decide karein (CPU 50% vs 70%)?**
A: **Method:** Load testing + Historical data. Steps: (1) Measure normal load (avg CPU=40%), (2) Measure peak load (CPU=90% → crash), (3) Set threshold = normal + 20% = 60%, (4) Test: Gradually increase traffic, observe when response time degrades. **Formula:** Threshold = P95_CPU + 10%. Example: P95=55% → Threshold=65%. **Tuning:** Start conservative (50%), monitor false positives (legitimate users blocked), adjust upward. **Per-service:** Different services different thresholds (DB-heavy=50%, CPU-heavy=70%).

**Q3: Cost-based limiting mein endpoint cost kaise calculate karein?**
A: **Profiling approach:** (1) Instrument endpoints (measure CPU time, memory, DB queries), (2) Run load test (1000 requests), (3) Calculate avg resource usage. **Formula:** `Cost = (CPU_ms × 0.1) + (Memory_MB × 0.01) + (DB_queries × 1)`. Example: Upload endpoint - CPU=500ms, Memory=50MB, DB=2 queries → Cost = 50 + 0.5 + 2 = 52.5 ≈ 50 tokens. **Normalization:** Lightest endpoint=1 token (baseline), others relative. **Review:** Quarterly review, adjust based on infrastructure changes.

**Q4: Geo-based limiting mein region capacity kaise track karein?**
A: **Monitoring:** Each region reports metrics to central system (Prometheus/CloudWatch). Metrics: CPU, Memory, Active connections, Response time. **Capacity calculation:** `Available_Capacity = (100 - CPU_Usage) × Server_Count`. Example: US region - 10 servers, avg CPU=70% → Capacity = (100-70) × 10 = 300 units. **Limit adjustment:** `Region_Limit = Base_Limit × (Available_Capacity / Total_Capacity)`. **Update frequency:** Every 60 seconds (avoid thrashing). **Fallback:** If monitoring fails, use static limits.

**Q5: Multiple patterns combine karne par performance impact kya hoga?**
A: **Latency breakdown:** Tier lookup (Redis)=0.5ms, Geo lookup (in-memory cache)=0.1ms, Adaptive factor (Redis config)=0.3ms, Endpoint cost (in-memory)=0.1ms, Token check (Redis Lua)=1ms. **Total:** ~2ms overhead. **Optimization:** (1) Cache tier + geo in application memory (refresh every 60s) → Reduce to 1ms, (2) Combine all checks in single Lua script → 0.5ms, (3) Use Redis pipelining for multiple keys. **At scale:** 10K RPS → 10K × 2ms = 20 CPU-seconds/sec = 20 cores. Acceptable for most systems. **Trade-off:** Complexity vs Flexibility - Start simple (tier only), add patterns as needed.

---

## 🎯 Module 13 Complete Summary:

**All Topics Covered:** 4/4 ✅
- ✅ Topic 13.1: Rate Limiter Basics - Architecture & Need
- ✅ Topic 13.2: Rate Limiting Algorithms Deep Dive (Token Bucket, Leaky Bucket, Fixed Window, Sliding Window)
- ✅ Topic 13.3: Distributed Rate Limiter with Redis + Lua Scripts
- ✅ Topic 13.4: Advanced Rate Limiting Patterns (Multi-tier, Geo-based, Adaptive, Per-Endpoint)

**Key Takeaways:**
1. **Algorithm Choice:** Token Bucket (best for APIs), Sliding Window Counter (accuracy + efficiency)
2. **Distributed:** Redis + Lua scripts for atomic operations, prevent race conditions
3. **Production:** Connection pooling, Redis Cluster with Sentinel, proper TTL management
4. **Advanced:** Multi-tier for monetization, Adaptive for resilience, Cost-based for resource protection

**Interview Focus:**
- Draw architecture: Client → LB → Redis → Backend
- Explain atomicity: Lua scripts prevent race conditions
- Compare algorithms: Token Bucket vs Fixed Window (boundary issue)
- Mention real-world: GitHub (Token Bucket), Cloudflare (Sliding Window), AWS (Multi-tier)

**Progress:** 13/21 Modules Completed 🎉

**Next Module:** Module 14 - Design Distributed Search (Inverted Index, Elasticsearch, Typeahead)

---
