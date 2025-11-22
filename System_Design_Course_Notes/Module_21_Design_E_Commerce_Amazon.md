# Module 21: Design E-Commerce Store (Amazon)

## Topic 21.1: Inventory & Order Management (Consistency)

---

## 🎯 1. Title / Topic: E-Commerce Inventory & Order System

---

## 🐣 2. Samjhane ke liye (Simple Analogy)

E-Commerce system ek **Grand Wedding Buffet** jaisa hai.
1.  **Inventory (Buffet Items)**: Limited Gulab Jamuns (Stock). Agar 2 log aakhri Gulab Jamun par ek saath haath maarein (Concurrency), toh jhagda hoga. Hamein ek waiter chahiye jo bole "Sir, ye reserved hai" (Locking).
2.  **Order Process (Saga)**: Ye ek **Relay Race** hai. Pehla runner (Inventory) baton pass karta hai dusre ko (Payment), phir teesre ko (Shipping). Agar Payment wala gir jaye (Fail), toh Inventory wale ko wapas peeche aana padega (Rollback/Compensation) taaki baton wapas jagah par rakhi jaye.

---

## 📖 3. Technical Definition (Interview Answer)

**E-Commerce Order System** is a distributed architecture that manages high-concurrency inventory updates using **Optimistic Locking** and processes complex orders using the **Saga Pattern** (Distributed Transactions). It ensures **Data Consistency** across microservices (Inventory, Payment, Order) without using a global lock (2PC), favoring availability and scalability.

**Key terms**:
- **Optimistic Locking**: Database record par version number lagana. Update tabhi hoga jab version match kare (Check-then-Act).
- **Saga Pattern**: Long-running transaction ko chhote steps mein todna. Agar step fail ho, toh "Compensating Transaction" (Undo) chalana.
- **Idempotency**: Ensure karna ki agar user galti se do baar button dabaye, toh order ek hi baar place ho.
- **Race Condition**: Jab 2 threads same data ko simultaneously modify karne ki koshish karein.

---

## 🧠 4. Zaroorat Kyun Hai? (Why?)

1.  **Problem (Overselling)**: Flash sale mein 1 iPhone bacha hai, aur 1000 log "Buy" click karte hain. Bina locking ke, system 1000 orders le lega par phone 1 hi hai.
2.  **Problem (Distributed Failure)**: Inventory deduct ho gayi, lekin Payment fail ho gaya. Agar rollback nahi kiya, toh item "Sold" dikhayega par paise nahi aaye (Dead Stock).
3.  **Business Impact**: Amazon ke liye overselling = Customer Trust Loss + Refunds. Dead stock = Revenue Loss.

---

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario)

-   **No Optimistic Locking**:
    -   User A aur User B same time par last item dekhte hain.
    -   Dono checkout karte hain. DB update karta hai `Stock = Stock - 1`.
    -   Stock -1 ho jata hai.
    -   **Result**: Ek customer ko order cancel ka email bhejna padega (Bad UX).
-   **No Saga Pattern**:
    -   Inventory service ne stock kam kar diya.
    -   Payment gateway down hai.
    -   Order create nahi hua.
    -   **Result**: System mein item gayab hai, par kisi ne kharida nahi.

---

## ⚙️ 6. Under the Hood (Technical Working)

**Optimistic Locking Flow:**
1.  **Read**: User product data padhta hai (`Stock: 5, Version: 1`).
2.  **Validate**: User "Buy" click karta hai.
3.  **Update**: Query chalti hai: `UPDATE products SET stock=4, version=2 WHERE id=1 AND version=1`.
4.  **Check**: Agar 1 row update hui → Success. Agar 0 row update hui (kyunki version badal gaya kisi aur ne kharid liya) → Fail & Retry.

**Saga Pattern (Order Flow):**
1.  **Order Service**: "New Order" event publish karta hai.
2.  **Inventory Service**: Stock reserve karta hai. Success event bhejta hai.
3.  **Payment Service**: Payment process karta hai.
    -   *Scenario A (Success)*: "Payment Done" event bhejta hai → Order Confirmed.
    -   *Scenario B (Fail)*: "Payment Failed" event bhejta hai → Inventory Service "Compensate" logic chalata hai (Stock wapas add karta hai).

**ASCII Diagram – Saga Choreography**

```
      [Order Service]
             |
    (1) Create Order (PENDING)
             |
             v
      [Kafka: OrderCreated]
             |
             +-----------------------+
             |                       |
             v                       v
    [Inventory Service]       [Payment Service]
    (2) Reserve Stock         (3) Deduct Money
             |                       |
             v                       v
    [Kafka: StockReserved]    [Kafka: PaymentFailed]
             |                       |
             +-----------+-----------+
                         |
                         v
                [Inventory Service]
                (4) COMPENSATE: Release Stock
```

---

## 🛠️ 7. Problems Solved
-   **Data Integrity**: Optimistic locking ensure karta hai ki stock kabhi negative na ho.
-   **Fault Tolerance**: Saga pattern ensure karta hai ki system consistent state mein rahe, chahe beech mein failure ho.
-   **Performance**: Database level locking (Pessimistic) ki jagah Application level locking (Optimistic) fast hoti hai.

---

## 🌍 8. Real‑World Example
**Amazon**: Prime Day par millions of transactions hote hain. Wo **DynamoDB** use karte hain with Conditional Writes (Optimistic Locking) inventory manage karne ke liye.
**Uber**: Ride booking mein bhi Saga use hota hai (Driver Lock -> Payment Auth -> Trip Start).

---

## 🔧 9. Tech Stack / Tools
-   **PostgreSQL/MySQL**: ACID properties ke liye (Order & Inventory tables).
-   **Kafka/RabbitMQ**: Saga events pass karne ke liye.
-   **Redis**: Cart session store karne ke liye (Fast access).
-   **Stripe/Razorpay**: Payment processing ke liye.

---

## 📐 10. Architecture / Formula
**Optimistic Locking SQL**
```sql
UPDATE inventory 
SET quantity = quantity - 1, version = version + 1 
WHERE product_id = 123 AND version = current_version;
```

**ASCII Diagram – Order Architecture**
```
[User] --HTTPS--> [API Gateway]
                        |
                        v
                 [Order Service] --(gRPC)--> [Inventory Service] (DB: Postgres)
                        |
                        +--(Async)--> [Payment Service] (Stripe)
                        |
                        +--(Async)--> [Notification Service] (SES)
```

---

## 💻 11. Code / Flowchart (Order Service)

```python
# E-Commerce Order Placement with Optimistic Locking

import psycopg2

class OrderSystem:
    def __init__(self, db_conn):
        self.conn = db_conn

    def place_order(self, user_id, product_id, qty):
        cur = self.conn.cursor()
        
        try:
            # Step 1: Current Stock aur Version read karo
            cur.execute("SELECT stock, version FROM products WHERE id = %s", (product_id,))
            row = cur.fetchone()
            
            if not row: return "Product Not Found"
            stock, version = row
            
            # Step 2: Check availability
            if stock < qty:
                return "Out of Stock"
            
            # Step 3: Optimistic Locking Update
            # Hum sirf tab update karenge agar version wahi hai jo humne read kiya tha
            cur.execute("""
                UPDATE products 
                SET stock = stock - %s, version = version + 1 
                WHERE id = %s AND version = %s
            """, (qty, product_id, version))
            
            # Step 4: Check agar update hua ya nahi
            if cur.rowcount == 0:
                # Rowcount 0 matlab kisi aur ne beech mein version change kar diya
                self.conn.rollback()
                return "Concurrent Update Fail - Please Retry"
            
            # Step 5: Order Create karo
            cur.execute("INSERT INTO orders (user_id, product_id) VALUES (%s, %s)", (user_id, product_id))
            
            self.conn.commit()
            return "Order Placed Successfully"

        except Exception as e:
            self.conn.rollback()
            return f"Error: {str(e)}"

# Usage Concept
# db = connect_db()
# system = OrderSystem(db)
# print(system.place_order(101, 500, 1))
```

---

## 📈 12. Trade‑offs
-   **Gain:** High Concurrency (No DB locks holding up traffic).
-   **Loss:** Retry Logic implement karna padta hai (Complexity).
-   **Gain:** Saga gives scalability | **Loss:** Eventual Consistency (User ko "Processing" dikhta hai, "Confirmed" thodi der baad).

---

## 🐞 13. Common Mistakes
-   **Mistake:** Using `SELECT ... FOR UPDATE` (Pessimistic Lock) everywhere.
    -   **Why Wrong:** Ye database ko slow kar dega high traffic mein.
    -   **Fix:** Use Optimistic Locking for inventory.
-   **Mistake:** No Idempotency key in Payment.
    -   **Why Wrong:** Network glitch par user double charge ho sakta hai.
    -   **Fix:** Pass unique `order_id` to payment gateway.

---

## ✅ 14. Zaroori Notes for Interview
1.  **Concurrency**: "Main Optimistic Locking use karunga inventory ke liye kyunki read-heavy system hai aur conflicts kam hote hain normal days mein."
2.  **Saga**: "Distributed transactions ke liye Saga pattern best hai. Main Choreography approach use karunga Kafka ke saath."
3.  **Idempotency**: "Payment service mein Idempotency Key zaroori hai taaki double deduction na ho."

---

## ❓ 15. FAQ & Comparisons
**Q1: Optimistic vs Pessimistic Locking - Kab kya use karein?**
A: **Optimistic**: Jab conflicts kam hon (e.g., Normal shopping). Fast hai. **Pessimistic**: Jab conflicts bahut zyada hon (e.g., Ticket booking last 5 mins). Data integrity guarantee karta hai par slow hai.

**Q2: Saga Orchestration vs Choreography?**
A: **Choreography**: Services ek dusre se event ke through baat karti hain (Decoupled). Small systems ke liye accha hai. **Orchestration**: Ek central "Conductor" service hoti hai jo sabko batati hai kya karna hai. Complex workflows (Amazon) ke liye better hai.

**Q3: Agar Payment fail ho jaye toh?**
A: Saga ka "Compensating Transaction" trigger hoga. Inventory service ko event milega "PaymentFailed", aur wo stock wapas increment kar dega.

**Q4: Cart data kahan store karein?**
A: **Redis** mein. Kyunki cart temporary data hai aur fast access chahiye. Agar user login kare, toh DB mein persist kar sakte hain.

**Q5: Flash Sales ko kaise handle karein?**
A: Flash sales ke liye alag queue aur simplified flow use karte hain. Kabhi-kabhi inventory ko Redis (Lua Script) mein move kar dete hain super-fast atomic decrement ke liye.

---

## Topic 21.2: Product Search & Discovery (Elasticsearch)

---

## 🎯 1. Title / Topic: Search Engine & Recommendations

---

## 🐣 2. Samjhane ke liye (Simple Analogy)

**Elasticsearch** ek **Book Index** jaisa hai.
Agar aapko book mein "Harry Potter" dhundhna hai, toh aap poori book page-by-page nahi padhte (SQL Full Scan). Aap peeche **Index** dekhte hain: "Harry Potter -> Page 10, 45, 99". Elasticsearch yahi karta hai – wo har shabd ka ek index banata hai (**Inverted Index**).
**Faceted Search**: Jaise Amazon par filters hote hain (Brand: Nike, Price: < 2000). Ye waise hi hai jaise Excel mein filter lagana – data ko kaat-chaat kar chhota karna.

---

## 📖 3. Technical Definition (Interview Answer)

**Product Search** is powered by **Elasticsearch** (or Solr), a distributed search engine built on Lucene. It uses an **Inverted Index** data structure to perform full-text searches in milliseconds. It supports **Faceted Search** (aggregations) for filtering and **Fuzzy Matching** for typo tolerance.
**Recommendations** use **Collaborative Filtering** (User-Item Matrix) to suggest products based on user behavior.

**Key terms**:
- **Inverted Index**: Mapping of Content -> Document ID (e.g., "Shoe" -> Product 1, 5, 9).
- **Tokenization**: Sentence ko words mein todna ("Blue Nike Shoe" -> ["blue", "nike", "shoe"]).
- **Sharding**: Index ko multiple parts mein todna taaki parallel search ho sake.
- **Collaborative Filtering**: "Users who bought X also bought Y".

---

## 🧠 4. Zaroorat Kyun Hai? (Why?)

1.  **Problem**: SQL database `LIKE %query%` search ke liye bahut slow hai (Full Table Scan). Millions of products mein seconds lagenge.
2.  **Feature Need**: Users ko "Typo tolerance" (Niike -> Nike) aur "Filters" (Red color, Size 10) chahiye. SQL mein ye complex hai.
3.  **Business Impact**: Fast aur accurate search = High Conversion Rate.

---

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario)

-   **Slow Search**: User "Shoes" type karega aur 5 second wait karega. Wo site chhod dega.
-   **No Typos**: User ne "Iphone" ki jagah "Iphonee" likha, aur SQL ne bola "No results found". Sale lost.

---

## ⚙️ 6. Under the Hood (Technical Working)

**How Inverted Index Works:**
Imagine 3 Products:
1.  "Blue Nike Shoe" (ID: 1)
2.  "Red Nike Shoe" (ID: 2)
3.  "Blue Adidas Shirt" (ID: 3)

**Index Table:**
| Term | Product IDs |
| :--- | :--- |
| Blue | [1, 3] |
| Nike | [1, 2] |
| Shoe | [1, 2] |
| Red | [2] |

**Query**: "Blue Shoe"
1.  "Blue" -> [1, 3]
2.  "Shoe" -> [1, 2]
3.  **Intersection**: [1] (Product 1 match both).

**Search Workflow:**
1.  User query bhejta hai.
2.  Search Service query ko **Tokenize** karti hai.
3.  Elasticsearch shards par parallel query run karta hai.
4.  Results ko **Rank** kiya jata hai (TF-IDF / BM25 score).
5.  Top results return hote hain.

**ASCII Diagram – Inverted Index**
```
[Documents]             [Inverted Index]
Doc 1: "Apple Phone"    "Apple" -> [1, 2]
Doc 2: "Apple Watch"    "Phone" -> [1]
Doc 3: "Smart Watch"    "Watch" -> [2, 3]
                        "Smart" -> [3]

Query: "Apple" -> Returns Doc 1, 2
```

---

## 🛠️ 7. Problems Solved
-   **Speed**: O(1) lookup time for words.
-   **Relevance**: Results ko score ke hisaab se sort karta hai (Best match first).
-   **Scalability**: Sharding se petabytes of data search ho sakta hai.

---

## 🌍 8. Real‑World Example
**Amazon Search**: Jab aap "Laptop" type karte hain, toh wo Elasticsearch hit karta hai. Sidebar mein jo filters aate hain (Dell, HP, 8GB RAM), wo **Aggregations** hain.
**Netflix**: Movie search bhi isi technology par chalta hai.

---

## 🔧 9. Tech Stack / Tools
-   **Elasticsearch / OpenSearch**: Industry standard for search.
-   **Logstash / Kafka**: Database se data ko Elasticsearch mein sync karne ke liye (CDC - Change Data Capture).
-   **Kibana**: Search analytics visualize karne ke liye.

---

## 📐 10. Architecture / Formula
**Relevance Score (BM25)**
Elasticsearch uses BM25 algorithm. Simple words mein:
`Score = (Term Frequency in Doc) / (Total Documents with Term)`
Agar "Rare" word match hota hai, toh score zyada milta hai.

**ASCII Diagram – Sync Architecture**
```
[Product DB (SQL)] --(CDC/Debezium)--> [Kafka]
                                          |
                                          v
                                   [Search Indexer]
                                          |
                                          v
                                   [Elasticsearch]
```

---

## 💻 11. Code / Flowchart (Elasticsearch Query)

```json
// Elasticsearch Query DSL Example
// Query: "Nike Shoes" with Filter: Price <= 5000

GET /products/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "name": "nike shoes" } }  // Full text search (Typo tolerant)
      ],
      "filter": [
        { "range": { "price": { "lte": 5000 } } } // Hard filter (Fast)
      ]
    }
  },
  "aggs": {
    "brands": { "terms": { "field": "brand" } } // Facets for sidebar
  }
}
```

---

## 📈 12. Trade‑offs
-   **Gain**: Super fast search & rich features.
-   **Loss**: **Eventual Consistency**. Database update hone ke baad Index update hone mein 1-2 second lagte hain.
-   **Loss**: Complexity. Do system maintain karne padte hain (SQL + ES) aur sync rakhna padta hai.

---

## 🐞 13. Common Mistakes
-   **Mistake**: Using Elasticsearch as primary database.
    -   **Why Wrong**: ES data loss kar sakta hai (Split brain scenarios). Transactions support nahi karta.
    -   **Fix**: Use SQL as Source of Truth, ES only for search.
-   **Mistake**: Not handling "Stop Words" (is, the, a).
    -   **Why Wrong**: Index size badh jata hai aur search slow hoti hai.
    -   **Fix**: Configure analyzer to remove stop words.

---

## ✅ 14. Zaroori Notes for Interview
1.  **Inverted Index**: "Elasticsearch ka core Inverted Index hai, jo book index ki tarah kaam karta hai for O(1) lookups."
2.  **Sync**: "Main CDC (Change Data Capture) pattern use karunga SQL se Elasticsearch data sync karne ke liye taaki latency kam ho."
3.  **Fuzzy Search**: "Typo tolerance ke liye Fuzzy Query use hoti hai (Levenshtein Distance)."

---

## ❓ 15. FAQ & Comparisons
**Q1: SQL vs Elasticsearch - Search ke liye kya use karein?**
A: Simple exact match (e.g., Username) ke liye SQL theek hai. Complex text search, filters, aur ranking ke liye Elasticsearch mandatory hai.

**Q2: Data Sync kaise karein (DB to ES)?**
A: **Dual Write**: Application dono jagah write kare (Risk: Inconsistency). **CDC (Best)**: DB logs read karke async update karein (Reliable).

**Q3: Faceted Search kya hai?**
A: Sidebar mein jo filters dikhte hain with counts (e.g., Nike (50), Adidas (30)). Ye Elasticsearch ki **Aggregations** feature se aata hai.

**Q4: Collaborative Filtering kya hai?**
A: Ye recommendation algorithm hai. "Jo user A ko pasand hai, wo user B ko bhi pasand aayega agar unki history same hai." Matrix Factorization use hota hai.

**Q5: Autocomplete kaise kaam karta hai?**
A: Elasticsearch mein **Edge N-gram** tokenizer use hota hai. "Apple" ko `["A", "Ap", "App", "Appl", "Apple"]` mein todte hain taaki user ke type karte hi match mil jaye.

---

## 🎯 Module 21 Complete Summary
-   **Topic 21.1**: Inventory & Orders – Optimistic Locking for consistency, Saga Pattern for distributed transactions.
-   **Topic 21.2**: Search & Discovery – Elasticsearch (Inverted Index) for speed, Faceted Search for UX.
-   **Key Takeaways**: E-Commerce is about balancing Consistency (Inventory) with Availability (Search).
-   **Interview Ready**: Focus on "How to prevent overselling" and "How Search works internally".

---

# 🏆 CONGRATULATIONS! You've completed the ENTIRE System Design Course!

All 21 modules covering:
-   Fundamentals, Scaling, Databases, Caching, Distributed Systems
-   Messaging, Observability, Deployment, IoT, Gaming, Mobile
-   Rate Limiter, Search, Notifications, TinyURL, WhatsApp, Instagram
-   YouTube, Uber, E-Commerce

**Total Topics:** 50+ comprehensive topics with 15-point structure in Hinglish.
**Ready for:** Google, Amazon, Microsoft, Meta interviews! 🚀
