# Module 21: Design E-Commerce Store (Amazon)

## Topic 21.1: E-Commerce System - Inventory & Order Management

---

## 🎯 1. Title / Topic: Amazon/E-Commerce (Online Shopping Platform)

---

## 🐣 2. Samjhane ke liye (Simple Analogy):

E-Commerce ek **Digital Mall** jaisa hai jisme multiple challenges hain. **Inventory Management:** Jaise physical store mein stock register hota hai (10 items available), waise hi database mein inventory count. **Concurrent Booking Problem:** Jaise 2 customers ek hi last item ko simultaneously kharidna chahte hain (race condition), system ko handle karna padta hai. **Distributed Transaction:** Order place karna ek **Multi-step Process** hai - (1) Inventory check, (2) Payment deduct, (3) Order create. Agar payment fail ho toh inventory wapas add karna padega (rollback). **Search:** Jaise mall mein directory board hota hai (product dhundne ke liye), waise hi Elasticsearch (fast product search with filters).

---

## 📖 3. Technical Definition (Interview Answer):

**E-Commerce System** is a distributed platform that manages product catalog (Elasticsearch), handles inventory with concurrency control (optimistic locking), processes orders via distributed transactions (Saga pattern), manages payments (Stripe/Razorpay), and provides recommendations (collaborative filtering).

**Key terms:**
- **Inventory Management:** Stock tracking with concurrent booking prevention (pessimistic/optimistic locking)
- **Distributed Transaction:** Multi-service operation (Inventory → Payment → Order) with consistency (Saga pattern)
- **Optimistic Locking:** Version-based concurrency control (check version before update, retry if changed)
- **Product Search:** Elasticsearch with faceted search (filters: price, brand, rating)
- **Recommendation Engine:** Collaborative filtering (users who bought X also bought Y)
- **Cart Management:** Session-based (Redis) or persistent (database)

---

## 🧠 4. Zaroorat Kyun Hai? (Why?):

**Main Problem:** 2 users simultaneously buy last item → Both see "In Stock" → Both checkout → Inventory becomes -1 (oversold). Need concurrency control. Also, order placement involves multiple services (Inventory, Payment, Shipping) - if payment fails, inventory should rollback.

**Business Impact:** Amazon: $514B revenue (2022), 12M products, 300M customers. Without proper inventory management, overselling causes customer complaints, refunds, reputation damage.

**Technical Benefits:**
- **Concurrency Control:** Prevents overselling (optimistic locking with version check)
- **Consistency:** Distributed transactions ensure all-or-nothing (Saga pattern)
- **Fast Search:** Elasticsearch returns results in <50ms with filters
- **Scalability:** Microservices architecture handles 1M orders/day
- **Personalization:** Recommendations increase sales 35% (Amazon data)

---

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario):

**Scenario: No Concurrency Control**
- Product: iPhone (1 item left)
- User A: Checks stock → 1 available → Adds to cart
- User B: Checks stock → 1 available → Adds to cart (simultaneously)
- User A: Checkout → Inventory: 1 - 1 = 0
- User B: Checkout → Inventory: 0 - 1 = -1 (oversold!)
- Result: 2 orders, 1 item → 1 customer disappointed, refund, bad review

**Scenario: No Distributed Transaction**
- User orders iPhone ($1000)
- Step 1: Inventory deducted (1 → 0) ✓
- Step 2: Payment fails (insufficient balance) ✗
- Step 3: Order not created
- Problem: Inventory deducted but no order → Item stuck, can't be sold to others

**Real Example:** **Flipkart Big Billion Day (2014)** - No proper concurrency control → 10K products oversold → Massive customer complaints → Had to cancel orders and give compensation → Lost $10M + reputation damage. After implementing optimistic locking (2015) → Overselling reduced 99%.

---

## ⚙️ 6. Under the Hood (Technical Working):

**Order Placement Flow (Distributed Transaction):**

1. **User Adds to Cart:** Product added (session-based, Redis)
2. **Checkout:** User clicks "Place Order"
3. **Inventory Check:** Check if product available (with version lock)
4. **Reserve Inventory:** Optimistic lock (version check + update)
5. **Payment Processing:** Call payment gateway (Stripe/Razorpay)
6. **Payment Success?**
   - **Yes:** Create order, confirm inventory deduction
   - **No:** Rollback inventory (release reservation)
7. **Order Created:** Generate order ID, send confirmation email
8. **Shipping:** Create shipping label, notify warehouse

**Optimistic Locking (Concurrency Control):**

```
Product Table:
+----+-------+-------+---------+
| id | name  | stock | version |
+----+-------+-------+---------+
| 1  | iPhone| 1     | 5       |
+----+-------+-------+---------+

User A Transaction:
1. Read: SELECT stock, version FROM products WHERE id=1
   Result: stock=1, version=5
2. Check: stock >= 1? Yes
3. Update: UPDATE products 
           SET stock=0, version=6 
           WHERE id=1 AND version=5
   Result: 1 row updated (success)

User B Transaction (simultaneous):
1. Read: SELECT stock, version FROM products WHERE id=1
   Result: stock=1, version=5 (same as User A)
2. Check: stock >= 1? Yes
3. Update: UPDATE products 
           SET stock=0, version=6 
           WHERE id=1 AND version=5
   Result: 0 rows updated (version changed to 6 by User A)
4. Retry: Read again → stock=0 → Show "Out of Stock"
```

**ASCII Architecture Diagram:**

```
ORDER PLACEMENT FLOW:

[User: Place Order]
     |
     v
+---------------------------+
|   ORDER SERVICE           |
|   (Orchestrator)          |
+---------------------------+
     |
     | (1) Check Inventory
     v
+---------------------------+
|   INVENTORY SERVICE       |
|   - Check stock           |
|   - Optimistic lock       |
|   - Reserve item          |
+---------------------------+
     |
     | Stock available? YES
     v
+---------------------------+
|   PAYMENT SERVICE         |
|   - Call Stripe API       |
|   - Deduct amount         |
+---------------------------+
     |
     +---> Payment Success? → Continue
     |
     +---> Payment Failed? → Rollback Inventory
     |
     v
+---------------------------+
|   ORDER SERVICE           |
|   - Create order record   |
|   - Generate order_id     |
+---------------------------+
     |
     v
+---------------------------+
|   NOTIFICATION SERVICE    |
|   - Send email            |
|   - Send SMS              |
+---------------------------+
     |
     v
+---------------------------+
|   SHIPPING SERVICE        |
|   - Create shipment       |
|   - Notify warehouse      |
+---------------------------+


SAGA PATTERN (Distributed Transaction):

HAPPY PATH (All Success):
[Order Service] → Reserve Inventory → SUCCESS
                → Process Payment → SUCCESS
                → Create Order → SUCCESS
                → Ship Order → SUCCESS

FAILURE PATH (Payment Fails):
[Order Service] → Reserve Inventory → SUCCESS
                → Process Payment → FAILED
                → Compensate: Release Inventory
                → Return Error to User


PRODUCT SEARCH ARCHITECTURE:

[User: Search "laptop"]
     |
     v
+---------------------------+
|   SEARCH SERVICE          |
+---------------------------+
     |
     | Query: "laptop"
     | Filters: price<50000, brand=Dell
     v
+---------------------------+
|   ELASTICSEARCH           |
|   - Inverted Index        |
|   - Faceted Search        |
|   - Ranking (relevance)   |
+---------------------------+
     |
     | Results: 1000 products
     v
+---------------------------+
|   RANKING SERVICE         |
|   - Popularity score      |
|   - User preferences      |
|   - Personalization       |
+---------------------------+
     |
     | Top 20 products
     v
+---------------------------+
|   CACHE (Redis)           |
|   - Popular searches      |
|   - Product details       |
+---------------------------+
     |
     v
[User sees results]


INVENTORY MANAGEMENT (Optimistic Locking):

DATABASE:
products table:
+----+--------+-------+---------+
| id | name   | stock | version |
+----+--------+-------+---------+
| 1  | iPhone | 5     | 10      |
+----+--------+-------+---------+

CONCURRENT TRANSACTIONS:

Time  | User A                        | User B
------|-------------------------------|-------------------------------
T1    | BEGIN TRANSACTION             | BEGIN TRANSACTION
T2    | SELECT stock, version         | SELECT stock, version
      | WHERE id=1                    | WHERE id=1
      | Result: stock=5, version=10   | Result: stock=5, version=10
T3    | UPDATE products               |
      | SET stock=4, version=11       |
      | WHERE id=1 AND version=10     |
      | (1 row updated - SUCCESS)     |
T4    | COMMIT                        |
T5    |                               | UPDATE products
      |                               | SET stock=4, version=11
      |                               | WHERE id=1 AND version=10
      |                               | (0 rows updated - FAILED)
T6    |                               | ROLLBACK
      |                               | Retry: Read again
      |                               | stock=4, version=11
      |                               | Update with new version
      |                               | (SUCCESS)

Result: No overselling, both transactions succeed sequentially
```

---

## 🛠️ 7. Problems Solved:

- **Concurrency Control:** Optimistic locking prevents overselling → 99% reduction in inventory errors
- **Distributed Transactions:** Saga pattern ensures consistency → Payment fails → Inventory rollback
- **Fast Search:** Elasticsearch with filters → <50ms search (vs 5 sec SQL LIKE query)
- **Scalability:** Microservices architecture → 1M orders/day (horizontal scaling)
- **Personalization:** Recommendation engine → 35% increase in sales (Amazon data)
- **Cart Persistence:** Redis session + DB backup → Cart survives browser close

---

## 🌍 8. Real-World Example:

**Amazon E-Commerce:** $514B revenue (2022), 12M products, 300M customers, 1.6M orders/day. Technology: Microservices (100+ services), Elasticsearch for search (50ms latency), DynamoDB for cart (NoSQL, fast writes), Saga pattern for orders (distributed transactions), Collaborative filtering for recommendations (35% sales from recommendations). Inventory: Optimistic locking with version control, 99.9% accuracy. Payment: Stripe integration, 3D Secure for fraud prevention. Scale: 10K orders/sec during Prime Day, 99.99% uptime. Without proper concurrency control and distributed transactions, Amazon couldn't handle Black Friday sales (10x normal traffic).

---

## 🔧 9. Tech Stack / Tools:

- **Elasticsearch:** Product search with faceted filters. Use for: Fast full-text search (<50ms), filters (price, brand, rating), autocomplete, typo tolerance.

- **Redis:** Cart management, session storage. Use for: Fast reads/writes (<1ms), session persistence, cache popular products.

- **PostgreSQL/MySQL:** Order records, user data. Use for: ACID transactions (payment + order), complex queries (order history), referential integrity.

- **Kafka:** Event streaming for order events. Use for: Saga pattern (distributed transactions), analytics pipeline, audit logs.

---

## 📐 10. Architecture/Formula:

**Optimistic Locking Query:**

```sql
-- Step 1: Read current state
SELECT stock, version FROM products WHERE id = 1;
-- Result: stock=5, version=10

-- Step 2: Update with version check
UPDATE products 
SET stock = stock - 1, version = version + 1
WHERE id = 1 AND version = 10;

-- If affected_rows = 1: Success (version matched)
-- If affected_rows = 0: Conflict (version changed by another transaction)
--   → Retry from Step 1

-- Step 3: Commit
COMMIT;
```

**Saga Pattern (Compensating Transactions):**

```
Order Saga:
1. Reserve Inventory (Compensate: Release Inventory)
2. Process Payment (Compensate: Refund Payment)
3. Create Order (Compensate: Cancel Order)
4. Ship Order (Compensate: Cancel Shipment)

Example (Payment Fails):
1. Reserve Inventory → SUCCESS
2. Process Payment → FAILED
3. Compensate: Release Inventory
4. Return error to user

Implementation:
- Event-driven (Kafka)
- Each service publishes events
- Saga orchestrator coordinates
- Timeout handling (if service doesn't respond in 30 sec)
```

**Recommendation Score Formula:**

```
Recommendation_Score = 
    (Collaborative_Filtering × 0.5) + 
    (Content_Based × 0.3) + 
    (Popularity × 0.2)

Where:
Collaborative_Filtering = Similarity(User, Other_Users) × Rating
Content_Based = Similarity(Product, User_Preferences)
Popularity = (Sales_Count / Total_Sales) × 10

Example:
User bought "iPhone 13"
Recommend "iPhone Case":

Collaborative: 80% users who bought iPhone also bought case → 0.8
Content: iPhone accessories category match → 0.9
Popularity: 10K sales out of 100K total → 0.1

Score = (0.8 × 0.5) + (0.9 × 0.3) + (0.1 × 0.2)
      = 0.4 + 0.27 + 0.02
      = 0.69

Higher score → Higher rank in recommendations
```

**Inventory Reservation Timeout:**

```
Reserve_Timeout = 10 minutes (cart expiry)

Flow:
1. User adds to cart → Reserve inventory (soft lock)
2. Timer starts (10 min)
3. User completes checkout → Confirm reservation (hard lock)
4. Timer expires → Release reservation (back to available)

Database:
inventory_reservations table:
+----+------------+---------+---------------------+
| id | product_id | user_id | expires_at          |
+----+------------+---------+---------------------+
| 1  | 123        | 456     | 2024-01-15 10:10:00 |
+----+------------+---------+---------------------+

Cron job: Every 1 min, delete expired reservations
DELETE FROM inventory_reservations WHERE expires_at < NOW();
```

---

## 💻 11. Code / Flowchart:

**Flowchart (Order Placement with Saga):**

```
START: User clicks "Place Order"
  |
  v
[Validate Cart]
Items in cart? YES
  |
  v
[Reserve Inventory]
For each item:
  - Check stock
  - Optimistic lock (version check)
  - Reserve quantity
  |
  +---> All reserved? → Continue
  |
  +---> Any failed? → Show "Out of Stock"
  |
  v
[Process Payment]
Call Stripe API
  |
  +---> Success? → Continue
  |
  +---> Failed? → Compensate
  |                |
  |                v
  |           [Release Inventory]
  |           [Return Error]
  |
  v
[Create Order]
Generate order_id
Insert into orders table
  |
  v
[Send Notifications]
Email + SMS confirmation
  |
  v
[Create Shipment]
Notify warehouse
  |
  v
[Return Success]
Show order confirmation page
  |
  v
END
```

**Code (Simplified Order Service with Optimistic Locking):**

```python
import psycopg2
from typing import Optional

class OrderService:
    def __init__(self):
        self.db = psycopg2.connect("dbname=ecommerce user=postgres")
    
    def place_order(self, user_id: int, product_id: int, quantity: int) -> Optional[str]:
        """Place order with optimistic locking"""
        cursor = self.db.cursor()
        max_retries = 3
        
        for attempt in range(max_retries):
            try:
                # Start transaction
                cursor.execute("BEGIN")
                
                # Step 1: Reserve inventory (optimistic lock)
                if not self._reserve_inventory(cursor, product_id, quantity):
                    cursor.execute("ROLLBACK")
                    return None  # Out of stock
                
                # Step 2: Process payment
                payment_success = self._process_payment(user_id, product_id, quantity)
                
                if not payment_success:
                    # Compensate: Release inventory
                    cursor.execute("ROLLBACK")
                    return None  # Payment failed
                
                # Step 3: Create order
                order_id = self._create_order(cursor, user_id, product_id, quantity)
                
                # Commit transaction
                cursor.execute("COMMIT")
                
                # Step 4: Async tasks (notifications, shipping)
                self._send_notifications(order_id)
                
                return order_id
            
            except psycopg2.IntegrityError:
                # Version conflict - retry
                cursor.execute("ROLLBACK")
                if attempt == max_retries - 1:
                    return None  # Max retries exceeded
                continue
        
        return None
    
    def _reserve_inventory(self, cursor, product_id: int, quantity: int) -> bool:
        """Reserve inventory with optimistic locking"""
        # Read current state
        cursor.execute(
            "SELECT stock, version FROM products WHERE id = %s",
            (product_id,)
        )
        result = cursor.fetchone()
        
        if not result:
            return False
        
        stock, version = result
        
        # Check availability
        if stock < quantity:
            return False
        
        # Update with version check (optimistic lock)
        cursor.execute(
            """
            UPDATE products 
            SET stock = stock - %s, version = version + 1
            WHERE id = %s AND version = %s
            """,
            (quantity, product_id, version)
        )
        
        # Check if update succeeded
        return cursor.rowcount == 1
    
    def _process_payment(self, user_id: int, product_id: int, quantity: int) -> bool:
        """Process payment via payment gateway"""
        # In production: Call Stripe/Razorpay API
        # Here: Mock success
        return True
    
    def _create_order(self, cursor, user_id: int, product_id: int, quantity: int) -> str:
        """Create order record"""
        cursor.execute(
            """
            INSERT INTO orders (user_id, product_id, quantity, status)
            VALUES (%s, %s, %s, 'CONFIRMED')
            RETURNING order_id
            """,
            (user_id, product_id, quantity)
        )
        
        order_id = cursor.fetchone()[0]
        return str(order_id)
    
    def _send_notifications(self, order_id: str):
        """Send order confirmation (async)"""
        # In production: Queue to Kafka/RabbitMQ
        print(f"📧 Order confirmation sent for {order_id}")

# Usage
service = OrderService()

# User places order
order_id = service.place_order(user_id=123, product_id=456, quantity=1)

if order_id:
    print(f"✅ Order placed successfully: {order_id}")
else:
    print("❌ Order failed (out of stock or payment failed)")
```

---

## 📈 12. Trade-offs:

- **Gain:** Optimistic locking prevents overselling, high concurrency support | **Loss:** Retry logic needed (version conflicts), potential user frustration (retry 3 times then fail)

- **Gain:** Saga pattern ensures consistency across services | **Loss:** Complex implementation (compensating transactions), eventual consistency (not immediate)

- **Gain:** Elasticsearch fast search (<50ms) with filters | **Loss:** Extra infrastructure cost, eventual consistency (product updates take 1-2 sec to reflect in search)

- **When to use:** E-commerce (Amazon, Flipkart), booking systems (hotels, flights), inventory management | **When to skip:** Simple CRUD apps (no concurrency issues), single-service apps (no distributed transactions), low traffic (<100 orders/day)

---

## 🐞 13. Common Mistakes:

- **Mistake:** No concurrency control (simple stock check without locking)
  - **Why wrong:** Race condition → 2 users buy last item → Overselling
  - **What happens:** Customer complaints, refunds, reputation damage
  - **Fix:** Optimistic locking with version check (retry on conflict)

- **Mistake:** No distributed transaction handling (inventory deducted but payment fails)
  - **Why wrong:** Inconsistent state → Item stuck (can't be sold)
  - **What happens:** Inventory inaccuracy, lost sales
  - **Fix:** Saga pattern with compensating transactions (rollback on failure)

- **Mistake:** Cart stored only in session (lost on browser close)
  - **Why wrong:** User adds items, closes browser, cart empty → Frustrated
  - **What happens:** Lost sales, poor UX
  - **Fix:** Hybrid approach (Redis session + DB backup for logged-in users)

- **Mistake:** Synchronous order processing (user waits for all steps)
  - **Why wrong:** Inventory → Payment → Order → Shipping → Email = 5 sec wait
  - **What happens:** Poor UX, timeout errors
  - **Fix:** Async processing (Kafka queue for notifications/shipping)

---

## ✅ 14. Zaroori Notes for Interview:

**Must Mention Points:**
1. **Start with concurrency problem:** "E-commerce ka main challenge concurrent booking hai. 2 users last item simultaneously kharidna chahte hain. Solution: Optimistic locking with version check. UPDATE products SET stock=stock-1, version=version+1 WHERE id=1 AND version=5. Agar version match nahi toh retry."

2. **Draw Saga pattern:** Order Service → Reserve Inventory (success) → Process Payment (fail) → Compensate: Release Inventory. Event-driven with Kafka.

3. **Explain optimistic vs pessimistic locking:** Optimistic: Version check, retry on conflict, high concurrency. Pessimistic: Row lock (SELECT FOR UPDATE), blocks others, low concurrency. Optimistic better for e-commerce (high traffic).

4. **Common follow-ups:**
   - **"Inventory reservation timeout?"** → 10 min cart expiry. Soft lock when added to cart, hard lock on checkout. Cron job releases expired reservations.
   - **"Payment failure handling?"** → Saga pattern compensating transaction. Rollback inventory, return error to user, log for analytics.
   - **"Search optimization?"** → Elasticsearch with inverted index, faceted search (filters), autocomplete, typo tolerance. Cache popular searches in Redis.
   - **"Recommendation algorithm?"** → Collaborative filtering (users who bought X also bought Y) + Content-based (similar products) + Popularity. Weighted score.

5. **Mention scale:** "Amazon: 1.6M orders/day, 10K orders/sec during Prime Day, 99.99% uptime, optimistic locking prevents 99% overselling."

6. **Pro tip:** "Interview mein optimistic locking ka SQL query likhke dikhao (UPDATE with version check). Aur Saga pattern ka diagram draw karo (compensating transactions). Shows practical knowledge."

---

## ❓ 15. FAQ & Comparisons (MANDATORY - 5 Questions):

**Q1: Optimistic Locking vs Pessimistic Locking - Kaunsa better for e-commerce?**
A: **Optimistic Locking:** Version-based, no row lock, high concurrency, retry on conflict. **Pros:** Scales well (1000s concurrent users), no blocking. **Cons:** Retry logic needed (3-5% conflicts). **Pessimistic Locking:** Row lock (SELECT FOR UPDATE), blocks other transactions. **Pros:** No conflicts, guaranteed success. **Cons:** Low concurrency (blocks others), deadlock risk. **Best:** Optimistic for e-commerce (Amazon, Flipkart use it) - high traffic needs high concurrency. Pessimistic for banking (low traffic, critical consistency).

**Q2: Saga Pattern vs 2-Phase Commit (2PC) - Distributed transactions mein kaunsa use karein?**
A: **Saga Pattern:** Event-driven, compensating transactions, eventual consistency. **Pros:** Scalable (no global lock), fault-tolerant (services can fail independently). **Cons:** Complex (compensating logic), eventual consistency (not immediate). **2PC:** Coordinator-based, prepare-commit phases, strong consistency. **Pros:** ACID guarantees, immediate consistency. **Cons:** Blocking (coordinator failure = all blocked), not scalable. **Best:** Saga for microservices (e-commerce, booking) - scalability important. 2PC for monoliths (legacy systems) - strong consistency needed.

**Q3: Cart storage - Session (Redis) vs Database - Kaunsa approach better?**
A: **Session (Redis):** In-memory, fast (<1ms), expires on browser close. **Pros:** Fast, no DB load. **Cons:** Lost on browser close (bad UX for logged-in users). **Database:** Persistent, survives browser close. **Pros:** Cart preserved, better UX. **Cons:** Slower (10ms), DB load. **Best:** Hybrid - Redis for guest users (fast, temporary), DB for logged-in users (persistent). **Amazon approach:** Redis primary + DB backup (async sync every 5 min). **Cart expiry:** 30 days for logged-in, 1 day for guest.

**Q4: Product search - SQL LIKE vs Elasticsearch - Performance difference?**
A: **SQL LIKE:** `SELECT * FROM products WHERE name LIKE '%laptop%'`. **Pros:** Simple, no extra infrastructure. **Cons:** Slow (5 sec for 1M products), no ranking, no typo tolerance, no filters. **Elasticsearch:** Inverted index, full-text search. **Pros:** Fast (<50ms), ranking (relevance), typo tolerance, faceted search (filters). **Cons:** Extra infrastructure ($1K/month), eventual consistency (1-2 sec lag). **Performance:** SQL LIKE = 5 sec, Elasticsearch = 50ms (100x faster). **Best:** Elasticsearch for e-commerce (Amazon, Flipkart use it) - fast search critical for UX.

**Q5: Recommendation engine - Collaborative filtering vs Content-based - Kaunsa better?**
A: **Collaborative Filtering:** "Users who bought X also bought Y". Based on user behavior. **Pros:** Discovers unexpected patterns (iPhone → iPhone case), no product metadata needed. **Cons:** Cold start problem (new users/products), sparsity (not enough data). **Content-Based:** "Similar products based on attributes" (category, brand, price). **Pros:** No cold start, works for new products. **Cons:** Limited discovery (only similar items), needs product metadata. **Best:** Hybrid (Amazon uses this) - Collaborative 50% + Content 30% + Popularity 20%. **Cold start solution:** Use content-based for new users, switch to collaborative after 10+ purchases.

---

## 🎯 Module 21 Complete Summary:

**All Topics Covered:** 1/1 ✅
- ✅ Topic 21.1: E-Commerce System - Inventory Management (Optimistic Locking), Distributed Transactions (Saga Pattern), Product Search (Elasticsearch), Recommendations, Cart Management

**Key Takeaways:**
1. **Optimistic Locking:** Version-based concurrency control, prevents overselling, retry on conflict, 99% accuracy
2. **Saga Pattern:** Distributed transactions with compensating transactions, event-driven (Kafka), eventual consistency
3. **Product Search:** Elasticsearch with inverted index, <50ms search, faceted filters, typo tolerance
4. **Recommendations:** Collaborative filtering (50%) + Content-based (30%) + Popularity (20%), 35% sales increase
5. **Cart Management:** Hybrid (Redis for speed + DB for persistence), 10 min reservation timeout

**Interview Focus:**
- Draw Saga pattern: Reserve Inventory → Payment → Create Order (with compensating transactions)
- Explain optimistic locking SQL query (UPDATE with version check)
- Discuss concurrency problem (2 users, 1 item, race condition)
- Mention Elasticsearch for fast search (<50ms vs 5 sec SQL)
- Real-world: Amazon (1.6M orders/day, 10K orders/sec Prime Day)

**Progress:** 21/21 Modules Completed 🎉🎉🎉

**🏆 CONGRATULATIONS! You've completed the ENTIRE System Design Course!**

All 21 modules covering:
- Fundamentals, Scaling, Databases, Caching, Distributed Systems
- Messaging, Observability, Deployment, IoT, Gaming, Mobile
- Rate Limiter, Search, Notifications, TinyURL, WhatsApp, Instagram
- YouTube, Uber, E-Commerce

**Total Topics:** 50+ comprehensive topics with 15-point structure in Hinglish
**Ready for:** Google, Amazon, Microsoft, Meta interviews! 🚀

---
