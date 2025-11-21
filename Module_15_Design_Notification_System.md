# Module 15: Design Notification System

## Topic 15.1: Notification System Architecture & Channels

---

## 🎯 1. Title / Topic: Notification System (Multi-Channel Alert System)

---

## 🐣 2. Samjhane ke liye (Simple Analogy):

Notification System ek **Post Office** jaisa hai jo different types ke messages deliver karta hai. Jaise post office mein **Speed Post** (urgent - OTP), **Regular Mail** (normal - newsletters), **Courier** (important - payment alerts) hote hain, waise hi notification system mein **SMS** (urgent), **Email** (detailed), **Push** (instant) channels hain. Post office decide karta hai kis message ko kaunse channel se bhejein based on priority aur user preference. Result: Right message, right channel, right time par user tak pahunchta hai.

---

## 📖 3. Technical Definition (Interview Answer):

**Notification System** is a distributed service that sends messages to users through multiple channels (Push, SMS, Email, In-App) with priority-based routing, rate limiting, retry logic, and vendor abstraction for high reliability and scalability.

**Key terms:**
- **Multi-Channel:** Push notifications, SMS, Email, In-App, WhatsApp (different delivery methods)
- **Priority Queue:** High priority (OTP) vs Low priority (marketing) - urgent messages first
- **Vendor Abstraction:** Twilio, SendGrid, FCM ko decouple (switch vendors easily)
- **Rate Limiting:** User ko 10 notifications/hour se zyada nahi (spam prevent)
- **Retry Logic:** Failed notification ko 3 times retry with exponential backoff
- **Template Engine:** Dynamic content injection ("Hi {name}, your order {id} is shipped")

---

## 🧠 4. Zaroorat Kyun Hai? (Why?):

**Main Problem:** Bina proper notification system ke, har service apna notification logic implement karega (code duplication). Payment service SMS bhejegi, Order service email bhejegi - no consistency, no rate limiting, no retry logic.

**Business Impact:** Critical notifications miss ho jayenge (OTP not delivered = user can't login = revenue loss). Spam notifications bhejne se users unsubscribe (engagement loss).

**Technical Benefits:**
- **Centralized:** Ek system saare notifications handle (consistency)
- **Reliability:** Retry logic + fallback channels (SMS fail → Email try)
- **Scalability:** 1M notifications/sec handle (queue-based architecture)
- **Cost Optimization:** Vendor switching easy (Twilio expensive → switch to cheaper)
- **User Preference:** User choose kar sakta hai (email only, no SMS)

---

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario):

**Scenario: No Centralized Notification System**
- Payment Service: Directly calls Twilio API for SMS (hardcoded)
- Order Service: Directly calls SendGrid for Email (hardcoded)
- Problems:
  1. No rate limiting → User gets 100 SMS in 1 hour (spam)
  2. No retry → SMS fails, user never knows payment succeeded
  3. Vendor lock-in → Twilio price increase, can't switch (code in 50 services)
  4. No analytics → Don't know delivery rate (80% emails going to spam?)

**Real Example:** **Uber (2015)** - No proper notification system → Drivers got 50+ push notifications during surge pricing → Notification fatigue → Drivers disabled notifications → Missed ride requests → Revenue loss. After implementing priority-based notification system (2016) → Critical notifications only → Driver engagement increased 40%.

---

## ⚙️ 6. Under the Hood (Technical Working):

**Notification Flow (Step-by-Step):**

1. **Event Trigger:** User places order → Order Service publishes event to Kafka
2. **Notification Service:** Consumes event from Kafka
3. **Template Selection:** "Order Confirmed" template select
4. **Content Generation:** Template + User data → "Hi John, Order #12345 confirmed"
5. **Channel Selection:** User preference check (Email + Push enabled, SMS disabled)
6. **Priority Assignment:** Order confirmation = Medium priority
7. **Queue Routing:** Medium priority queue mein push
8. **Worker Processing:** Worker picks from queue
9. **Vendor Selection:** Email → SendGrid, Push → FCM
10. **Rate Limit Check:** User ne last 1 hour mein 5 notifications received (under limit)
11. **Send:** Vendor API call
12. **Retry on Failure:** Failed → Retry after 1 min, 2 min, 4 min (exponential backoff)
13. **Status Update:** Delivered/Failed status database mein store
14. **Analytics:** Delivery rate, open rate track

**ASCII Architecture Diagram:**

```
[TRIGGER SOURCES]
Payment Service, Order Service, Auth Service, etc.
     |
     | Events (Kafka/RabbitMQ)
     v
+---------------------------+
|  NOTIFICATION SERVICE     |
|  (Core Orchestrator)      |
+---------------------------+
     |
     | (1) Fetch User Preferences
     v
+---------------------------+
|  USER PREFERENCE DB       |
|  user123: {               |
|    email: true,           |
|    sms: false,            |
|    push: true             |
|  }                        |
+---------------------------+
     |
     | (2) Select Template
     v
+---------------------------+
|  TEMPLATE ENGINE          |
|  "Hi {name}, Order {id}"  |
+---------------------------+
     |
     | (3) Route by Priority
     v
+---------------------------+
|  PRIORITY QUEUES          |
|  +---------------------+  |
|  | HIGH (OTP, Alerts)  |  |
|  +---------------------+  |
|  | MEDIUM (Orders)     |  |
|  +---------------------+  |
|  | LOW (Marketing)     |  |
|  +---------------------+  |
+---------------------------+
     |
     | (4) Workers Process
     v
+---------------------------+
|  NOTIFICATION WORKERS     |
|  (Parallel Processing)    |
|  Worker-1, Worker-2, ...  |
+---------------------------+
     |
     | (5) Rate Limit Check
     v
+---------------------------+
|  RATE LIMITER (Redis)     |
|  user123: 5 notifs/hour   |
+---------------------------+
     |
     | (6) Vendor Abstraction
     v
+---------------------------+
|  VENDOR ADAPTERS          |
|  +---------------------+  |
|  | SMS: Twilio/SNS     |  |
|  | Email: SendGrid/SES |  |
|  | Push: FCM/APNS      |  |
|  +---------------------+  |
+---------------------------+
     |
     | (7) External APIs
     v
+---------------------------+
|  EXTERNAL VENDORS         |
|  Twilio, SendGrid, FCM    |
+---------------------------+
     |
     | (8) Delivery Status
     v
+---------------------------+
|  STATUS TRACKING DB       |
|  notif_id: delivered      |
|  timestamp: 2024-01-15    |
+---------------------------+
     |
     | (9) Analytics
     v
+---------------------------+
|  ANALYTICS DASHBOARD      |
|  Delivery Rate: 98%       |
|  Open Rate: 25%           |
+---------------------------+


DETAILED FLOW (Order Confirmation):

[Order Service]
     |
     | Kafka Event: {user_id: 123, order_id: 456, type: "order_confirmed"}
     v
[Notification Service Consumer]
     |
     v
[Check User Preferences]
user123 → email: true, push: true, sms: false
     |
     v
[Template Engine]
Template: "Hi {name}, your order {order_id} is confirmed!"
Data: {name: "John", order_id: "456"}
Result: "Hi John, your order 456 is confirmed!"
     |
     v
[Priority Assignment]
Order confirmation → MEDIUM priority
     |
     v
[Queue: MEDIUM]
Push notification to queue
     |
     v
[Worker Picks]
Worker-5 available → Process
     |
     v
[Rate Limit Check]
Redis: user123:notif_count = 3 (last hour)
3 < 10 → Allow
     |
     v
[Send Email via SendGrid]
API Call: POST /v3/mail/send
     |
     +---> Success? → Mark delivered
     |
     +---> Failed? → Retry queue (1 min delay)
     |
     v
[Send Push via FCM]
API Call: POST /fcm/send
     |
     v
[Update Status]
DB: notif_id=789, status=delivered, channel=email+push
     |
     v
[Analytics Update]
Increment: email_sent_count, push_sent_count
```

---

## 🛠️ 7. Problems Solved:

- **Reliability:** Retry logic + fallback channels → 99.9% delivery rate (vs 80% without retry)
- **Scalability:** Queue-based architecture → 1M notifications/sec (horizontal scaling)
- **Vendor Independence:** Adapter pattern → Switch Twilio to SNS in 1 day (no code change in services)
- **Spam Prevention:** Rate limiting → User gets max 10 notifs/hour (engagement maintained)
- **Cost Optimization:** Intelligent routing (SMS expensive → Use push if possible) → 40% cost reduction
- **User Control:** Preference management → Users opt-out of marketing (compliance - GDPR)
- **Analytics:** Delivery tracking → Identify issues (90% emails in spam → Fix sender reputation)

---

## 🌍 8. Real-World Example:

**Amazon Notification System:** 500M+ notifications/day across Email, SMS, Push, In-App. Architecture: Event-driven (Kinesis streams), priority queues (SQS), vendor abstraction (SNS for SMS, SES for Email, custom for Push). Features: Smart routing (if push fails within 5 min, send SMS), rate limiting (max 5 marketing emails/week), personalization (ML-based send time optimization). Scale: 100K notifications/sec during Prime Day. Cost: $10M/year saved by switching from Twilio to SNS. Delivery rate: 99.5% for critical (OTP), 95% for marketing. Without this system, Amazon's customer engagement would drop significantly.

---

## 🔧 9. Tech Stack / Tools:

- **Kafka/RabbitMQ:** Message queue for event streaming. Use for: Decoupling services, buffering spikes (1M events/sec), guaranteed delivery. Kafka better for high throughput.

- **Redis:** Rate limiting + caching. Use for: User notification count (10/hour limit), template caching, fast lookup (<1ms). Atomic INCR for rate limiting.

- **Twilio/AWS SNS:** SMS vendor. Use for: OTP, critical alerts. Twilio: Rich API, expensive ($0.0075/SMS). SNS: Cheap ($0.00645/SMS), AWS integration.

- **SendGrid/AWS SES:** Email vendor. Use for: Transactional emails, newsletters. SendGrid: Easy setup, analytics. SES: Cheap ($0.10/1000 emails), requires sender verification.

- **FCM/APNS:** Push notifications. Use for: Mobile apps. FCM: Android + iOS support, free. APNS: iOS only, Apple ecosystem.

---

## 📐 10. Architecture/Formula:

**Priority Queue Selection Formula:**

```
Priority_Score = Urgency × 10 + User_Engagement × 5 + Business_Value × 3

Where:
Urgency: 1-10 (10 = OTP, 1 = Newsletter)
User_Engagement: 0-10 (based on past open rate)
Business_Value: 0-10 (revenue impact)

Example 1 (OTP):
Urgency = 10, Engagement = 5, Value = 8
Score = 10×10 + 5×5 + 8×3 = 100 + 25 + 24 = 149 → HIGH queue

Example 2 (Marketing):
Urgency = 2, Engagement = 3, Value = 2
Score = 2×10 + 3×5 + 2×3 = 20 + 15 + 6 = 41 → LOW queue

Thresholds:
Score > 100 → HIGH queue (process immediately)
Score 50-100 → MEDIUM queue (process within 1 min)
Score < 50 → LOW queue (process within 1 hour)
```

**Rate Limiting Formula (Sliding Window):**

```
Allowed = Current_Count < Limit

Where:
Current_Count = Notifications sent in last 1 hour
Limit = User tier based (Free: 10/hour, Premium: 100/hour)

Redis Implementation:
Key: "notif:user123:count"
Value: 7 (current count)
TTL: 3600 seconds (1 hour)

On new notification:
count = INCR "notif:user123:count"
if count == 1:
    EXPIRE "notif:user123:count" 3600
if count > limit:
    REJECT
else:
    ALLOW
```

**Retry Backoff Formula:**

```
Retry_Delay = Base_Delay × (2 ^ Attempt_Number)

Where:
Base_Delay = 1 minute
Max_Attempts = 3

Attempt 1: 1 × 2^0 = 1 min
Attempt 2: 1 × 2^1 = 2 min
Attempt 3: 1 × 2^2 = 4 min

Total time: 1 + 2 + 4 = 7 minutes
After 3 failures → Move to Dead Letter Queue (manual review)
```

**Channel Selection Decision Tree:**

```
START: Notification to send
     |
     v
[Check User Preference]
     |
     +---> Email enabled? → Add to email_channels
     +---> SMS enabled? → Add to sms_channels
     +---> Push enabled? → Add to push_channels
     |
     v
[Check Priority]
     |
     +---> HIGH (OTP)? → Send ALL enabled channels (redundancy)
     |
     +---> MEDIUM (Order)? → Send Email + Push (cost-effective)
     |
     +---> LOW (Marketing)? → Send Email only (cheapest)
     |
     v
[Check Cost]
SMS: $0.0075, Email: $0.0001, Push: Free
     |
     v
[Final Selection]
Example: MEDIUM priority, all enabled
→ Email + Push (skip SMS to save cost)
```

---

## 💻 11. Code / Flowchart:

**Flowchart (Notification Processing):**

```
START: Event arrives (Order Confirmed)
     |
     v
[Parse Event]
user_id=123, order_id=456, type="order_confirmed"
     |
     v
[Fetch User Preferences]
DB query: SELECT * FROM user_prefs WHERE user_id=123
Result: {email: true, sms: false, push: true}
     |
     v
[Select Template]
Template DB: "order_confirmed" → "Hi {name}, order {id} confirmed"
     |
     v
[Render Content]
Data: {name: "John", id: "456"}
Output: "Hi John, order 456 confirmed"
     |
     v
[Assign Priority]
Order confirmed → MEDIUM (score=75)
     |
     v
[Rate Limit Check]
Redis: INCR "notif:user123:count"
Result: 6 (under limit of 10)
     |
     v
[Push to Queue]
MEDIUM queue: {user_id, content, channels: [email, push]}
     |
     v
[Worker Picks]
Worker-3 available
     |
     v
[Send Email]
SendGrid API call
     |
     +---> Success? → Mark delivered
     |
     +---> Failed? → Retry queue (1 min delay)
     |
     v
[Send Push]
FCM API call
     |
     v
[Update Status]
DB: INSERT INTO notif_log (id, user_id, status, channels)
     |
     v
   END
```

**Code (Simplified Notification Service):**

```python
from enum import Enum
import redis
import time

class Priority(Enum):
    HIGH = 3    # OTP, Critical alerts
    MEDIUM = 2  # Orders, Updates
    LOW = 1     # Marketing, Newsletters

class NotificationService:
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379)
        self.rate_limit = 10  # per hour
    
    def send_notification(self, user_id: str, message: str, 
                         channels: list, priority: Priority):
        """Main notification sending logic"""
        
        # 1. Rate limit check
        if not self._check_rate_limit(user_id):
            print(f"❌ Rate limit exceeded for user {user_id}")
            return False
        
        # 2. Push to priority queue
        queue_name = f"queue:{priority.name}"
        notification = {
            'user_id': user_id,
            'message': message,
            'channels': channels,
            'timestamp': time.time()
        }
        
        # 3. Send via each channel
        results = {}
        for channel in channels:
            success = self._send_via_channel(channel, user_id, message)
            results[channel] = success
            
            # Retry logic for failures
            if not success:
                self._schedule_retry(notification, channel)
        
        # 4. Update analytics
        self._update_analytics(user_id, channels, results)
        
        return all(results.values())
    
    def _check_rate_limit(self, user_id: str) -> bool:
        """Check if user is under rate limit"""
        key = f"notif:{user_id}:count"
        count = self.redis.incr(key)
        
        if count == 1:
            self.redis.expire(key, 3600)  # 1 hour TTL
        
        return count <= self.rate_limit
    
    def _send_via_channel(self, channel: str, user_id: str, 
                         message: str) -> bool:
        """Send via specific channel (mock)"""
        # In production: Call Twilio/SendGrid/FCM API
        print(f"📤 Sending via {channel} to {user_id}: {message}")
        return True  # Mock success
    
    def _schedule_retry(self, notification: dict, channel: str):
        """Schedule retry with exponential backoff"""
        retry_queue = "queue:retry"
        notification['retry_channel'] = channel
        notification['retry_count'] = notification.get('retry_count', 0) + 1
        
        if notification['retry_count'] <= 3:
            delay = 60 * (2 ** notification['retry_count'])  # 1, 2, 4 min
            print(f"🔄 Retry scheduled in {delay}s for {channel}")
            # Push to retry queue with delay
    
    def _update_analytics(self, user_id: str, channels: list, 
                         results: dict):
        """Track delivery metrics"""
        for channel, success in results.items():
            metric = f"analytics:{channel}:{'success' if success else 'failed'}"
            self.redis.incr(metric)

# Usage
service = NotificationService()

# Send order confirmation
service.send_notification(
    user_id="user123",
    message="Your order #456 is confirmed!",
    channels=["email", "push"],
    priority=Priority.MEDIUM
)

# Send OTP (high priority)
service.send_notification(
    user_id="user123",
    message="Your OTP is 123456",
    channels=["sms", "email", "push"],  # All channels for redundancy
    priority=Priority.HIGH
)
```

---

## 📈 12. Trade-offs:

- **Gain:** Centralized system (consistency), vendor abstraction (easy switching), retry logic (reliability) | **Loss:** Single point of failure (notification service down = no notifications), added latency (queue processing 1-5 sec)

- **Gain:** Rate limiting (spam prevention), priority queues (critical first) | **Loss:** Complexity (multiple queues to manage), potential delays for low priority (marketing emails sent after 1 hour)

- **Gain:** Multi-channel support (reach users anywhere), fallback channels (SMS fails → Email) | **Loss:** Cost (SMS expensive - $0.0075 each), vendor management (multiple APIs to integrate)

- **When to use:** Any app with notifications (e-commerce, social media, banking), high volume (>1000 notifs/day), multiple channels needed | **When to skip:** Very simple apps (<100 users), single channel only (email only), low volume (<10 notifs/day - direct API call sufficient)

---

## 🐞 13. Common Mistakes:

- **Mistake:** Synchronous notification sending (blocking)
  - **Why wrong:** Order API waits for email to send (5 sec) → Slow response to user
  - **What happens:** Poor UX, API timeout, user thinks order failed
  - **Fix:** Async processing (publish to queue, return immediately)

- **Mistake:** No rate limiting
  - **Why wrong:** Bug in code → Infinite loop → User gets 10,000 SMS in 1 hour
  - **What happens:** User angry, unsubscribes, potential legal issues (spam), huge bill ($75 for 10K SMS)
  - **Fix:** Redis-based rate limiting (10 notifs/hour per user)

- **Mistake:** Hardcoding vendor APIs in business logic
  - **Why wrong:** Twilio price increase → Need to change code in 50 services
  - **What happens:** Weeks of work, risky deployment, vendor lock-in
  - **Fix:** Adapter pattern (vendor abstraction layer), switch vendor in config

- **Mistake:** No retry logic
  - **Why wrong:** Network glitch → SMS fails → User never gets OTP → Can't login
  - **What happens:** Support tickets, frustrated users, revenue loss
  - **Fix:** Exponential backoff retry (3 attempts: 1 min, 2 min, 4 min)

---

## ✅ 14. Zaroori Notes for Interview:

**Must Mention Points:**
1. **Start with architecture:** "Notification system mein 3 main components hain - Event Source (Kafka), Priority Queues (HIGH/MEDIUM/LOW), Workers (parallel processing). Vendor abstraction layer se Twilio/SendGrid/FCM decouple."

2. **Draw flow:** Event → Notification Service → User Preferences → Template Engine → Priority Queue → Worker → Rate Limit Check → Vendor API → Status Update.

3. **Explain priority:** "OTP = HIGH (immediate), Order = MEDIUM (1 min), Marketing = LOW (1 hour). Formula: Priority_Score = Urgency×10 + Engagement×5 + Value×3."

4. **Common follow-ups:**
   - **"Rate limiting kaise implement karoge?"** → Redis INCR command with TTL. Key: "notif:user123:count", limit: 10/hour. Atomic operation (race condition nahi).
   - **"Retry logic kaise?"** → Exponential backoff: 1 min, 2 min, 4 min. After 3 failures → Dead Letter Queue (manual review).
   - **"Vendor switch kaise karoge?"** → Adapter pattern. Interface: send(user, message), implementations: TwilioAdapter, SNSAdapter. Config change se switch.
   - **"Multi-channel kaise decide?"** → User preference + Priority + Cost. HIGH priority = all channels (redundancy), MEDIUM = Email+Push (cost-effective), LOW = Email only.

5. **Mention scale:** "Amazon: 500M notifs/day, 100K/sec during peak. Queue-based architecture scales horizontally (add more workers)."

6. **Pro tip:** "Interview mein mention karo - Async processing (non-blocking), Rate limiting (spam prevent), Vendor abstraction (flexibility), Retry logic (reliability). Yeh 4 points critical hain."

---

## ❓ 15. FAQ & Comparisons (MANDATORY - 5 Questions):

**Q1: Push vs SMS vs Email - Kab kaunsa channel use karein?**
A: **Push:** Instant, free, high engagement (70% open rate), but requires app install. Use for: Real-time updates (ride arrived, message received). **SMS:** Reliable (99% delivery), works without app, but expensive ($0.0075/SMS). Use for: OTP, critical alerts. **Email:** Cheap ($0.0001), detailed content, but low open rate (20%). Use for: Receipts, newsletters, detailed updates. **Decision:** HIGH priority (OTP) = SMS+Push (redundancy), MEDIUM (orders) = Email+Push (cost-effective), LOW (marketing) = Email only.

**Q2: Kafka vs RabbitMQ for notification queue - Kaunsa better?**
A: **Kafka:** High throughput (1M msgs/sec), durable (disk-based), replay possible, but complex setup. Use for: Event streaming, high volume (>10K notifs/sec), need replay (reprocess failed). **RabbitMQ:** Easy setup, flexible routing, lower throughput (50K msgs/sec), memory-based. Use for: Simple queuing, priority queues (built-in), moderate volume (<10K/sec). **Most systems:** Start with RabbitMQ (simpler), migrate to Kafka if scale needed. **Amazon/Uber:** Use Kafka (massive scale).

**Q3: Template engine kaise implement karein (dynamic content)?**
A: **Approach:** Template store in DB with placeholders. **Example:** "Hi {name}, your order {order_id} is {status}". **Rendering:** Replace placeholders with actual data. **Implementation:** (1) Simple: String replace (fast but limited), (2) Advanced: Jinja2/Handlebars (conditionals, loops). **Storage:** Redis cache for hot templates (1 sec load), DB for all templates. **Versioning:** Template_v1, Template_v2 (A/B testing). **Localization:** Templates per language (en, hi, es).

**Q4: Dead Letter Queue (DLQ) kya hai aur kab use karein?**
A: **DLQ:** Queue for messages that failed after all retries (3 attempts). **Purpose:** Manual review, debugging, prevent infinite retry loops. **Flow:** Notification fails 3 times → Move to DLQ → Alert ops team → Manual investigation (vendor down? invalid phone number?). **Processing:** Daily job checks DLQ, categorizes failures (vendor issue vs bad data), retries vendor issues, discards bad data. **Monitoring:** DLQ size > 1000 → Alert (something wrong). **Example:** Twilio down for 1 hour → 10K SMS in DLQ → Twilio back → Retry all from DLQ.

**Q5: Notification deduplication kaise karein (same notif 2 baar na jaye)?**
A: **Problem:** Network retry → Same event processed twice → User gets duplicate OTP. **Solution:** Idempotency key. **Implementation:** Generate unique key per notification (hash of user_id + event_type + timestamp). **Redis check:** Before processing, check if key exists. If yes, skip (already processed). If no, process and store key (TTL 24 hours). **Example:** Event: {user_id: 123, type: "otp", timestamp: 1234567890} → Key: hash("123:otp:1234567890") = "abc123" → Redis: SET "dedup:abc123" 1 EX 86400 → If key exists, skip. **Edge case:** Same OTP request after 1 hour (legitimate) → Different timestamp → Different key → Allowed.

---



---

## 🎯 Module 15 Complete Summary:

**All Topics Covered:** 1/1 ✅
- ✅ Topic 15.1: Notification System Architecture - Multi-channel delivery (Push, SMS, Email), Priority Queues, Vendor Abstraction, Rate Limiting, Retry Logic

**Key Takeaways:**
1. **Multi-Channel:** Push (instant, free), SMS (reliable, expensive), Email (cheap, detailed) - choose based on priority and cost
2. **Priority Queues:** HIGH (OTP - immediate), MEDIUM (Orders - 1 min), LOW (Marketing - 1 hour) based on urgency score
3. **Vendor Abstraction:** Adapter pattern for easy switching (Twilio → SNS), no vendor lock-in
4. **Rate Limiting:** Redis-based (10 notifs/hour per user), prevent spam, atomic INCR operation
5. **Retry Logic:** Exponential backoff (1, 2, 4 min), max 3 attempts, then Dead Letter Queue

**Interview Focus:**
- Draw architecture: Event Source → Kafka → Notification Service → Priority Queues → Workers → Vendor APIs
- Explain priority formula: Score = Urgency×10 + Engagement×5 + Value×3
- Mention rate limiting: Redis INCR with TTL (atomic operation)
- Discuss retry: Exponential backoff with DLQ for failed messages
- Real-world: Amazon (500M notifs/day), Uber (priority-based system increased engagement 40%)

**Production Patterns:**
- **Async Processing:** Non-blocking (publish to queue, return immediately)
- **Idempotency:** Deduplication key (prevent duplicate notifications)
- **Fallback Channels:** SMS fails → Try Email (reliability)
- **Template Engine:** Dynamic content with placeholders ({name}, {order_id})
- **Analytics:** Track delivery rate, open rate, identify issues

**Cost Optimization:**
- SMS: $0.0075 (expensive) - use only for critical
- Email: $0.0001 (cheap) - use for detailed content
- Push: Free - use whenever possible
- Smart routing: MEDIUM priority → Email+Push (skip SMS)

**Progress:** 15/21 Modules Completed 🎉

**Next Module:** Module 16 - Design TinyURL (URL Shortener with Base62 encoding, Key Generation Service)

---
