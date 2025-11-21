# Module 1: Fundamentals & Capacity Planning

## Topic 1.1: System Design Basics

## 🎯 1. Title / Topic: System Design Basics

## 🐣 2. Samjhane ke liye (Simple Analogy):
System Design ek Restaurant chalane jaisa hai. Socho tumhara ek restaurant hai:
- **Frontend** = Menu card (jo customer dekhta hai, colorful, attractive)
- **API** = Waiter (customer aur kitchen ke beech communication karta hai)
- **Backend** = Kitchen (actual cooking hoti hai, logic execute hota hai)
- **Database** = Fridge/Storage (ingredients store hote hain, data save hota hai)

Jaise restaurant mein zyada customers aaye toh tum waiters badhate ho, kitchen expand karte ho, waise hi system design mein traffic badhne par servers aur resources scale karte hain.

## 📖 3. Technical Definition (Interview Answer):
System Design is the process of defining the architecture, components, modules, interfaces, and data flow of a system to satisfy specified requirements while ensuring scalability, reliability, and maintainability.

**Key terms:**
- **Scalability (स्केलेबिलिटी):** System ki capacity badhane ki ability jab load/traffic badhe. Example: 100 users se 1 million users handle karna.
- **Reliability (रिलायबिलिटी):** System kitna dependable hai, failures ke bawajood kaam karta rahe. Example: 99.9% uptime (year mein sirf 8 hours downtime).
- **Maintainability (मेंटेनेबिलिटी):** Code ko update/fix karna kitna easy hai. Clean code, proper documentation.
- **Fault Tolerance (फॉल्ट टॉलरेंस):** Ek component fail ho jaye toh bhi system chalta rahe. Example: Ek server crash ho toh dusra le le.

## 🧠 4. Zaroorat Kyun Hai? (Why?):
**Main Problem:** Jab application chhoti hoti hai (100 users) toh ek simple server kaam kar jata hai. Par jab millions of users aate hain, toh ek server crash ho jayega. System Design sikhata hai ki kaise large-scale applications build karein jo fast, reliable aur scalable ho.

**Business Impact:** Agar system slow ya down ho jaye toh customers chale jayenge competitors ke paas. Amazon ka study: 100ms delay = 1% revenue loss.

**Technical Benefit:** Proper system design se aap bottlenecks identify kar sakte ho, failures handle kar sakte ho, aur cost optimize kar sakte ho (unnecessary resources nahi lagane padte).

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario):
Agar System Design nahi kiya toh:
- **Technical Error:** Single server par saara load → CPU 100%, Memory full → Server crash → 503 Service Unavailable error
- **User Impact:** Website slow/down → Users frustrated → Bounce rate badh jayega → Negative reviews
- **Business Impact:** Revenue loss (e-commerce mein har minute downtime = lakhs ka loss), Brand reputation damage
- **Real Example:** Knight Capital (2012) - Poor system design + deployment error → $440 million loss in 45 minutes. System ne galat trades execute kar diye kyunki proper testing aur fault tolerance nahi tha.

## ⚙️ 6. Under the Hood (Technical Working):

**System Design Process (Step-by-step):**
1. **Requirements Gathering:** Functional (kya karna hai) aur Non-Functional (kaise perform karna hai) requirements define karo
2. **Capacity Estimation:** Calculate karo kitne users, kitna storage, kitna bandwidth chahiye
3. **High-Level Design:** Major components identify karo (Frontend, Backend, Database, Cache, Load Balancer)
4. **Database Design:** Schema design, SQL vs NoSQL decide karo
5. **API Design:** Endpoints define karo (REST/GraphQL)
6. **Scaling Strategy:** Vertical vs Horizontal scaling decide karo
7. **Bottleneck Identification:** Kahan problem aa sakti hai (database queries slow, network latency)
8. **Trade-offs:** CAP theorem apply karo, consistency vs availability choose karo

**ASCII Diagram - Basic System Architecture:**
```
                    [Users/Clients]
                          |
                          | (1) HTTP/HTTPS Request
                          v
                 +------------------+
                 |   Load Balancer  |
                 |   (Nginx/AWS)    |
                 +------------------+
                    /      |      \
         (2) Route /       |       \ Route
                  /        |        \
                 v         v         v
            +--------+ +--------+ +--------+
            |Backend | |Backend | |Backend |
            |Server 1| |Server 2| |Server 3|
            +--------+ +--------+ +--------+
                 \        |        /
          (3) Query \     |       / Query
                     \    |      /
                      v   v     v
                   +-------------+
                   |  Database   |
                   | (PostgreSQL)|
                   +-------------+
                          |
                   (4) Store/Retrieve Data
```

**Flow Explanation:**
(1) User browser/app se request bhejta hai
(2) Load Balancer request ko available server par distribute karta hai
(3) Backend server business logic execute karta hai aur database se data fetch/store karta hai
(4) Response wapas user tak reverse path se jaata hai

## 🛠️ 7. Problems Solved:
- **Single Point of Failure:** Multiple servers use karke agar ek fail ho toh dusra handle kare
- **Performance Bottleneck:** Load balancing se traffic distribute hota hai, koi ek server overload nahi hota
- **Data Loss:** Database replication se data multiple places par store hota hai, backup available
- **Slow Response:** Caching layer add karke frequently accessed data fast serve hota hai

## 🌍 8. Real-World Example:
**WhatsApp:** 2 billion+ users, 100 billion+ messages daily. Architecture: Erlang-based backend servers (fault-tolerant), FreeBSD OS, Mnesia database for metadata, Load balancers for traffic distribution. Key Design: Horizontal scaling (servers add karte rahe jaise users badhte gaye), Minimal features (sirf messaging focus, no bloat), Efficient protocol (custom binary protocol, not HTTP). Result: 50 engineers ne 2 billion users handle kiye, $19 billion mein Facebook ko becha.

## 🔧 9. Tech Stack / Tools:
- **Frontend:** React/Angular/Vue (UI banane ke liye), Mobile: Flutter/React Native
- **Backend:** Node.js (JavaScript, fast I/O), Java Spring Boot (enterprise apps), Python Django/Flask (rapid development), Go (high performance, concurrency)
- **Database:** PostgreSQL (relational, ACID), MongoDB (NoSQL, flexible schema), Redis (in-memory cache)
- **Load Balancer:** Nginx (lightweight, reverse proxy), HAProxy (TCP/HTTP), AWS ELB (managed service)
- **Monitoring:** Prometheus (metrics), Grafana (visualization), ELK Stack (logs)

## 📐 10. Architecture/Formula:

**Restaurant Analogy Detailed Mapping:**
```
[Customer] -----> [Menu Card] -----> [Waiter] -----> [Kitchen] -----> [Fridge]
    |                  |                 |               |                |
    v                  v                 v               v                v
  [User]          [Frontend]          [API]         [Backend]        [Database]
                  (React/HTML)     (REST/GraphQL)   (Node.js/Java)   (PostgreSQL)

Customer Order Flow:
1. Customer menu dekhta hai (Frontend load hota hai)
2. Order deta hai waiter ko (API call: POST /order)
3. Waiter kitchen ko bolta hai (Backend receives request)
4. Kitchen ingredients fridge se nikalta hai (Database query)
5. Food ready hota hai (Backend processes data)
6. Waiter customer ko serve karta hai (API response)
```

**Key Metrics Formula:**
- **Availability:** (Total Time - Downtime) / Total Time × 100
  - Example: 99.9% = 8.76 hours downtime per year allowed
- **Throughput:** Requests processed per second (RPS)
- **Latency:** Time taken for one request (milliseconds)

## 💻 11. Code / Flowchart:

**System Design Interview Flowchart:**
```
Start Interview
     |
     v
[Clarify Requirements]
     |
     ├─> Functional: What features? (Upload video, Send message)
     └─> Non-Functional: Scale? Latency? Consistency?
     |
     v
[Capacity Estimation]
     |
     ├─> Users: DAU (Daily Active Users)
     ├─> Storage: Data size per user × users
     └─> Bandwidth: Upload/Download speed needed
     |
     v
[High-Level Design]
     |
     ├─> Draw boxes: Client, LB, Servers, DB, Cache
     └─> Show data flow with arrows
     |
     v
[Deep Dive Components]
     |
     ├─> Database: SQL vs NoSQL? Sharding?
     ├─> Cache: Redis? What to cache?
     └─> APIs: REST endpoints design
     |
     v
[Identify Bottlenecks]
     |
     └─> Database slow? Add read replicas
         Network latency? Add CDN
     |
     v
[Discuss Trade-offs]
     |
     └─> CAP theorem: Consistency vs Availability
     |
     v
End Interview
```

## 📈 12. Trade-offs:
- **Scalability vs Simplicity:** Distributed system complex hota hai (multiple servers, databases) but scale karta hai. Simple monolith easy hai maintain karna but limited scale. **When to use:** Start simple, scale jab zaroorat ho (premature optimization mat karo).
- **Consistency vs Availability (CAP Theorem):** Banking app mein consistency zaroori (balance galat nahi dikha sakte), Social media mein availability zaroori (thoda outdated feed dikha sakte ho). **Trade-off:** Dono saath mein nahi mil sakte network partition ke time.
- **Cost vs Performance:** High-end servers expensive but fast. Budget servers cheap but limited. **Balance:** Auto-scaling use karo, peak time par servers badhao, off-peak par reduce karo.

## 🐞 13. Common Mistakes:
- **Mistake 1:** Premature optimization - Shuru se hi complex distributed system banana. **Why wrong:** Unnecessary complexity, maintenance hard. **Fix:** Start with monolith, scale when needed (>10K users).
- **Mistake 2:** Ignoring Non-Functional Requirements - Sirf features par focus, performance/security ignore. **Why wrong:** Production mein system crash hoga. **Fix:** Interview mein explicitly poocho: "Kitna latency acceptable hai? Kitne users expected hain?"
- **Mistake 3:** Single Point of Failure - Ek hi database, ek hi server. **Why wrong:** Wo fail hua toh pura system down. **Fix:** Redundancy add karo (multiple servers, database replicas).
- **Mistake 4:** Not considering Data Consistency - Distributed system mein data sync nahi kiya. **Why wrong:** User ko different data dikhega different servers se. **Fix:** Replication strategy define karo (Master-Slave, eventual consistency).

## ✅ 14. Zaroori Notes for Interview:
1. **Always start with Requirements:** Interviewer ko clarifying questions poocho - "Kitne users expected hain? Read-heavy ya write-heavy system? Latency requirements kya hain?" Ye dikhata hai ki tum assumptions nahi kar rahe.

2. **Draw Diagrams:** Whiteboard par boxes aur arrows draw karo. Visual representation se interviewer ko samajh aata hai tumhara thought process. Components label karo clearly.

3. **Mention 4 Key Qualities:** Har system design mein in chaar cheezein discuss karo - Scalability (kaise scale karoge), Reliability (failures kaise handle karoge), Maintainability (code clean hai?), Fault Tolerance (redundancy hai?).

4. **Numbers Matter:** Vague mat bolo "bahut users hain". Specific bolo: "1 million DAU, 10 million requests/day, 100 GB storage needed". Capacity estimation dikhata hai tumhe production experience hai.

5. **Trade-offs Discuss Karo:** Koi bhi decision lo toh uske pros-cons bolo. "Main SQL use kar raha hoon kyunki ACID properties chahiye, but agar future mein horizontal scaling chahiye toh NoSQL consider karenge."

6. **Common Follow-ups:** 
   - "How will you handle 10x traffic?" → Horizontal scaling, caching, CDN
   - "What if database becomes bottleneck?" → Read replicas, sharding, caching layer
   - "How to ensure data consistency?" → Transactions, distributed locks, eventual consistency

7. **Real-world Examples:** Apne design ko real companies se relate karo: "Netflix bhi similar approach use karta hai for video streaming" - ye credibility badhata hai.

## ❓ 15. FAQ & Comparisons:

**Q1: Monolithic vs Microservices - Kab kya use karein?**
A: Monolithic (ek hi codebase, ek deployment) use karo jab team chhoti ho (<10 developers) aur product simple ho. Microservices (independent services) use karo jab team badi ho, different teams different features par kaam karein, aur independent scaling chahiye. Trade-off: Microservices complex but scalable.

**Q2: SQL vs NoSQL - Main difference kya hai?**
A: SQL (PostgreSQL, MySQL) structured data ke liye, fixed schema, ACID properties (banking, inventory). NoSQL (MongoDB, Cassandra) unstructured/flexible data ke liye, horizontal scaling easy, eventual consistency (social media, logs). Decision factor: Data structure fixed hai ya dynamic? Consistency critical hai ya availability?

**Q3: Vertical Scaling vs Horizontal Scaling - Kaise decide karein?**
A: Vertical (ek server mein CPU/RAM badhao) quick fix hai but hardware limit hai aur expensive. Horizontal (zyada servers add karo) unlimited scaling but complexity badhti hai (load balancing, data consistency). Start vertical, move to horizontal jab limit hit ho.

**Q4: What if Load Balancer fail ho jaye?**
A: Load Balancer khud single point of failure ban sakta hai. Solution: Multiple load balancers use karo with failover mechanism (Active-Passive setup). DNS level par multiple IPs configure karo. Cloud providers (AWS ELB) automatically redundancy provide karte hain.

**Q5: CAP Theorem practically kaise apply hota hai?**
A: CAP = Consistency, Availability, Partition Tolerance. Network partition (servers ka communication break) hone par sirf 2 choose kar sakte ho. Banking: CP (Consistency + Partition Tolerance) - transaction fail kar do but galat balance mat dikhao. Social Media: AP (Availability + Partition Tolerance) - thoda purana feed dikha do but app down mat karo. Real-world mein "eventual consistency" use karte hain - temporarily inconsistent but eventually sync ho jata hai.

---


## Topic 1.2: Requirements Gathering (The Interview Starter)

## 🎯 1. Title / Topic: Requirements Gathering

## 🐣 2. Samjhane ke liye (Simple Analogy):
Requirements Gathering ek ghar banane se pehle blueprint banana jaisa hai. Architect pehle puchta hai: "Kitne rooms chahiye? Budget kya hai? Kitne log rahenge? Earthquake-proof chahiye?" Waise hi system design interview mein pehle clarify karo: "Kitne users hain? Kya features chahiye? Kitna fast hona chahiye?" Bina requirements ke seedha coding karna = bina blueprint ke ghar banana = disaster!

## 📖 3. Technical Definition (Interview Answer):
Requirements Gathering is the process of identifying and documenting what the system should do (Functional Requirements) and how it should perform (Non-Functional Requirements) before designing the architecture.

**Key terms:**
- **Functional Requirements (FR):** System ki features aur capabilities - "KYA karna hai". Example: User can upload video, User can search products, User can send messages.
- **Non-Functional Requirements (NFR):** System ki quality attributes - "KAISE perform karna hai". Example: Latency < 200ms, 99.99% availability, Handle 1M concurrent users.
- **Constraints:** Limitations jo follow karne hain. Example: Budget $10K/month, Use only AWS, Must comply with GDPR.

## 🧠 4. Zaroorat Kyun Hai? (Why?):
**Main Problem:** Agar requirements clear nahi hain toh tum galat system design kar doge. Example: Tumne SQL database use kiya but system write-heavy tha, toh performance issue aayega. Ya tumne consistency optimize kiya but availability chahiye thi.

**Business Impact:** Wrong requirements = Wrong product = Waste of time and money. Agar product user ki zaroorat fulfill nahi karta toh launch ke baad redesign karna padega (costly).

**Technical Benefit:** Clear requirements se tum sahi technology stack choose kar sakte ho, bottlenecks pehle se identify kar sakte ho, aur interviewer ko dikhata hai ki tum assumptions nahi karte, clarify karte ho (senior engineer quality).

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario):
Agar Requirements nahi gather kiye toh:
- **Technical Error:** Wrong architecture choice - Example: Synchronous processing use kiya jahan asynchronous chahiye tha → System slow, requests timeout
- **User Impact:** Features miss ho jayenge ya performance poor hoga → Users frustrated → App uninstall
- **Business Impact:** Rework karna padega (time + money waste), Delayed launch, Competitors aage nikal jayenge
- **Real Example:** Healthcare.gov (2013) - Requirements properly gather nahi kiye, load estimation galat tha. Launch day par 250K users expected the but system 50K par hi crash ho gaya. Result: 2 weeks downtime, $500M+ spent on fixes, Government embarrassment.

## ⚙️ 6. Under the Hood (Technical Working):

**Requirements Gathering Process (Interview mein):**

1. **Clarify Functional Requirements (5 minutes):**
   - Core features identify karo: "User kya kar sakta hai?"
   - Example (WhatsApp): Send text, Send media, Group chat, Voice/Video call, Status updates
   - Prioritize karo: MVP (Minimum Viable Product) mein kya chahiye vs Nice-to-have

2. **Define Non-Functional Requirements (5 minutes):**
   - **Scale:** Kitne users? DAU (Daily Active Users), Peak traffic?
   - **Performance:** Latency kitna acceptable? Throughput (RPS)?
   - **Availability:** Downtime kitna acceptable? 99.9% (8 hours/year) ya 99.99% (52 min/year)?
   - **Consistency:** Strong consistency chahiye (banking) ya eventual consistency ok hai (social media)?

3. **Identify Constraints:**
   - Budget, Technology stack, Team size, Timeline, Compliance (GDPR, HIPAA)

4. **Understand Latency Numbers (Critical for Performance Requirements):**
   - Ye numbers har programmer ko pata honi chahiye kyunki isse samajh aata hai ki cache/network optimization kitna important hai

**ASCII Diagram - Requirements Categories:**
```
                    REQUIREMENTS
                         |
         +---------------+---------------+
         |                               |
    FUNCTIONAL (FR)              NON-FUNCTIONAL (NFR)
         |                               |
    "What to do"                   "How to perform"
         |                               |
    +----+----+                    +-----+-----+
    |    |    |                    |     |     |
  User Post Search            Scalability Performance
  Login Share Filter          Reliability  Security
                              Availability Consistency
```

**Latency Numbers Every Programmer Should Know:**
```
Operation                           Time (Approx)       Analogy
---------------------------------------------------------------------------
L1 Cache access                     0.5 ns              Ek second = 1 second
L2 Cache access                     7 ns                Ek second = 14 seconds  
RAM access                          100 ns              Ek second = 3 minutes
SSD random read                     150,000 ns          Ek second = 4 days
Network call (same datacenter)      500,000 ns          Ek second = 11 days
SSD sequential read (1 MB)          1,000,000 ns        Ek second = 23 days
Disk seek                           10,000,000 ns       Ek second = 8 months
Network round trip (US to Europe)   150,000,000 ns      Ek second = 5 years

Key Takeaway: 
- RAM access SSD se 1500x FAST hai → Caching (Redis/Memcached) zaroori hai
- Network call RAM se 5000x SLOW hai → Database queries minimize karo
- Disk seek bahut slow → Sequential reads prefer karo (SSDs better)
```

**CAP Theorem Triangle:**
```
                    Consistency (C)
                         /\
                        /  \
                       /    \
                      /  CP  \
                     /  (SQL) \
                    /          \
                   /     CA     \
                  /   (Single)   \
                 /                \
                +------------------+
    Availability (A)      AP      Partition Tolerance (P)
                      (NoSQL)
                      
Network Partition ke time sirf 2 choose kar sakte ho:
- CP: Banking (Consistency + Partition) - Galat balance mat dikhao, service down kar do
- AP: Social Media (Availability + Partition) - Thoda purana feed dikha do but app chalta rahe
- CA: Single server (No partition) - Real distributed system mein possible nahi
```

**CAP Theorem Detailed Examples:**

**Scenario 1 - Banking App (CP System):**
```
[User A] ----Check Balance----> [Bank Server Mumbai]
                                         |
                                 Network Partition! ❌
                                 (Cable cut, connection lost)
                                         X
[User B] ----Withdraw Money---> [Bank Server Delhi]

Problem: Dono servers sync nahi kar sakte (Partition)

CP Choice (Consistency Priority):
- User B ki request REJECT kar do
- Show error: "Service temporarily unavailable, try later"
- Reason: Agar allow karte toh User A aur B dono same account se withdraw kar lete
  (Balance = ₹10,000, dono ₹8,000 withdraw → ₹16,000 total → Bank loss!)
- Availability sacrifice ki but Consistency maintain kiya

Real Example: ICICI Bank, HDFC Bank - Transaction fail but data correct
```

**Scenario 2 - Social Media App (AP System):**
```
[User posts photo] ----> [Server US]
                              |
                      Network Partition! ❌  
                              X
[User's friend views] <---- [Server India]

Problem: India server ko naya photo nahi dikhega (sync nahi hua)

AP Choice (Availability Priority):
- Friend ko purana feed dikha do (without new photo)
- App DOWN mat karo, user experience maintain karo
- Eventually (5-10 min baad) jab network theek hoga, sync ho jayega
- Reason: Thodi der purana feed dikha diya toh koi business loss nahi
  but agar app down ho jaye toh users frustrated (competitors pe chale jayenge)

Real Example: Instagram, Facebook, Twitter - Eventual consistency acceptable
```

## 🛠️ 7. Problems Solved:
- **Ambiguity Removal:** Clear requirements se confusion nahi hota, sab ko pata hai kya banana hai
- **Right Technology Choice:** Read-heavy system hai toh caching focus, Write-heavy hai toh queue-based processing
- **Scope Creep Prevention:** Documented requirements se baad mein "ye bhi add karo" nahi hota
- **Estimation Accuracy:** Proper requirements se capacity estimation sahi hota hai (servers, storage, bandwidth)

## 🌍 8. Real-World Example:
**Instagram (Initial Launch - 2010):** Founders ne clear requirements define kiye: FR = Photo upload, Filters, Feed, Follow/Unfollow. NFR = Fast upload (<5 sec), High availability (99.9%), Mobile-first. Constraints = Small team (2 engineers), Limited budget. Result: Simple architecture (Django + PostgreSQL + S3 + Redis), Focus on core features only. 1 million users in 2 months, $1 billion acquisition by Facebook in 2 years. Key: Clear requirements se focused product bana.

## 🔧 9. Tech Stack / Tools:
**Requirements Documentation Tools:**
- **Confluence/Notion:** Requirements document banane ke liye, team collaboration
- **Draw.io/Lucidchart:** Architecture diagrams banane ke liye based on requirements
- **JIRA:** Requirements ko tasks mein break karna, tracking

**Interview mein:**
- **Whiteboard:** Requirements list banao left side par, refer karte raho design karte time
- **Clarifying Questions Template:** "Can you clarify the scale?", "What's the priority: consistency or availability?", "Any specific technology constraints?"

## 📐 10. Architecture/Formula:

**Throughput vs Latency (Key NFR Metrics):**
```
THROUGHPUT                          LATENCY
    |                                  |
"Kitna load handle kar sakte"    "Ek request kitni der mein"
    |                                  |
Measured in: RPS                  Measured in: milliseconds
(Requests Per Second)             (ms)
    |                                  |
Example: 10,000 RPS               Example: 50ms response time
    |                                  |
Analogy: Pipe ka diameter         Analogy: Paani ki speed
(Kitna paani flow ho sakta)       (Kitni der mein aayega)

Trade-off: High throughput often increases latency
Solution: Load balancing + Caching + Async processing
```

**Availability Formula:**
```
Availability % = (Total Time - Downtime) / Total Time × 100

Examples:
99%     (Two Nines)   = 3.65 days downtime/year    ❌ Not acceptable
99.9%   (Three Nines) = 8.76 hours downtime/year   ⚠️ Minimum for production
99.99%  (Four Nines)  = 52.56 minutes downtime/year ✅ Good
99.999% (Five Nines)  = 5.26 minutes downtime/year  ✅ Excellent (costly)

Interview mein: Always ask "What availability is expected?"
```

**Read-Heavy vs Write-Heavy Classification:**
```
READ-HEAVY SYSTEM                WRITE-HEAVY SYSTEM
(Read:Write = 100:1)             (Write:Read = 10:1)
        |                                |
Examples:                        Examples:
- YouTube (videos watch)         - Twitter (tweets post)
- Wikipedia (articles read)      - IoT sensors (data log)
- E-commerce (browse)            - Analytics (events track)
        |                                |
Optimization:                    Optimization:
- Caching (Redis)                - Message Queues (Kafka)
- Read Replicas (DB)             - Write-optimized DB (Cassandra)
- CDN (static content)           - Async processing
```

## 💻 11. Code / Flowchart:

**Interview Requirements Gathering Flowchart:**
```
Interviewer: "Design WhatsApp"
     |
     v
[ASK CLARIFYING QUESTIONS]
     |
     ├─> Functional Requirements
     |   ├─> "One-to-one chat only or group chat bhi?"
     |   ├─> "Media sharing (images/videos) supported?"
     |   ├─> "Voice/Video calls needed?"
     |   └─> "Read receipts (blue ticks) chahiye?"
     |
     ├─> Non-Functional Requirements
     |   ├─> "Kitne users expected? (1M, 100M, 1B?)"
     |   ├─> "Message delivery latency? (Real-time <1sec?)"
     |   ├─> "Availability target? (99.9% or 99.99%?)"
     |   └─> "Strong consistency ya eventual consistency?"
     |
     └─> Constraints
         ├─> "Any specific tech stack? (AWS, GCP?)"
         ├─> "Budget constraints?"
         └─> "Compliance requirements? (GDPR, encryption?)"
     |
     v
[DOCUMENT REQUIREMENTS]
Write on whiteboard:
FR: 1-to-1 chat, Group chat, Media sharing
NFR: 1B users, <1sec latency, 99.99% availability
Constraints: End-to-end encryption mandatory
     |
     v
[START HIGH-LEVEL DESIGN]
Based on requirements choose:
- WebSockets (real-time needed)
- Cassandra (write-heavy, billions of messages)
- S3 (media storage)
- Redis (online status cache)
```

## 📈 12. Trade-offs:
- **Detailed Requirements vs Time:** Interview mein 5-7 minutes requirements par spend karo, zyada time liya toh design ka time nahi milega. **Balance:** Core requirements quickly clarify karo, edge cases baad mein discuss karo.
- **Consistency vs Availability (CAP):** Banking app mein consistency non-negotiable (galat balance nahi dikha sakte), Social media mein availability priority (thoda delay ok hai). **Decision:** Business requirement se decide hota hai, technical preference se nahi.
- **Feature Completeness vs MVP:** Sab features include karne ki koshish mat karo, core features identify karo jo MVP mein chahiye. **Example:** WhatsApp initially sirf text messaging thi, baad mein media/calls add kiye.

## 🐞 13. Common Mistakes:
- **Mistake 1:** Bina poocho assume kar lena - "I'll assume 1 million users". **Why wrong:** Interviewer ko lagega tum clarify nahi karte. **Fix:** Always ask: "Can you help me understand the expected scale?"
- **Mistake 2:** Sirf Functional Requirements par focus - Features list bana diya but performance/scale discuss nahi kiya. **Why wrong:** NFRs se architecture decide hota hai. **Fix:** Explicitly poocho: "What are the non-functional requirements like latency, availability?"
- **Mistake 3:** Unrealistic Requirements - "I'll design for 1 billion users with 1ms latency". **Why wrong:** Over-engineering, impractical. **Fix:** Realistic numbers use karo based on problem statement.
- **Mistake 4:** Requirements document nahi karna - Verbally discuss kiya but whiteboard par nahi likha. **Why wrong:** Design karte time bhool jayenge. **Fix:** Whiteboard ke ek corner mein requirements list banao, refer karte raho.

## ✅ 14. Zaroori Notes for Interview:
1. **First 5 Minutes Critical:** Interview start hote hi clarifying questions poocho. Ye dikhata hai tum experienced ho. Template: "Before I start designing, let me clarify a few things..."

2. **FR vs NFR Dono Cover Karo:** Sirf "What features" mat poocho, "How many users, what latency" bhi poocho. Balanced approach dikhata hai.

3. **Write Down Requirements:** Whiteboard ke top-left corner mein list banao:
   ```
   FR: Feature1, Feature2, Feature3
   NFR: 10M users, <100ms latency, 99.9% uptime
   Constraints: AWS only, $5K/month budget
   ```
   Design karte time isko refer karo.

4. **CAP Theorem Mention Karo:** Jab consistency/availability discuss ho, CAP theorem ka naam lo. "Given the requirements, I'm choosing AP (Availability + Partition Tolerance) because social media app hai."

5. **Numbers Specific Rakho:** Vague mat bolo "many users". Specific bolo: "10 million DAU, 100 million requests/day". Agar nahi pata toh assume karo aur bolo: "I'm assuming 10M users, please correct me if different."

6. **Common Follow-ups:**
   - "Why did you choose consistency over availability?" → Business requirement explain karo
   - "How will you handle 10x traffic?" → Scaling strategy based on NFRs
   - "What if latency requirement is 10ms instead of 100ms?" → Architecture changes discuss karo (more caching, edge servers)

7. **Read-Heavy vs Write-Heavy Identify Karo:** Ye explicitly poocho: "Is this a read-heavy or write-heavy system?" Isse architecture decisions easy ho jayenge (read-heavy = caching focus, write-heavy = queue-based).

## ❓ 15. FAQ & Comparisons:

**Q1: Functional vs Non-Functional Requirements - Interview mein dono kaise balance karein?**
A: Pehle FR quickly list karo (2-3 min), phir NFR detail mein discuss karo (3-4 min). NFR zyada important hai kyunki wahi se architecture decide hota hai. FR sirf features batata hai, NFR batata hai kaise build karna hai.

**Q2: CAP Theorem - CP vs AP kab choose karein?**
A: CP (Consistency + Partition Tolerance) choose karo jab data correctness critical ho: Banking (balance), Inventory (stock count), Booking (seat availability). AP (Availability + Partition Tolerance) choose karo jab service uptime critical ho: Social media (feed), Analytics (logs), Monitoring (metrics). Real-world: Most systems "eventual consistency" use karte hain (AP with delayed consistency).

**Q3: Latency vs Throughput - Dono improve kaise karein?**
A: Latency reduce karne ke liye: Caching (Redis), CDN (static content), Database indexing, Async processing. Throughput badhane ke liye: Horizontal scaling (more servers), Load balancing, Connection pooling, Batch processing. Trade-off: Sometimes high throughput increases latency (queuing delay).

**Q4: What if interviewer says "You decide the requirements"?**
A: Realistic assumptions lo aur justify karo. Example: "I'm assuming this is a consumer app like Instagram, so I'll target 10M DAU, read-heavy (100:1 read:write ratio), 99.9% availability, eventual consistency acceptable. Does this sound reasonable?" Interviewer ko option do correct karne ka.

**Q5: Strong Consistency vs Eventual Consistency - Kaise decide karein?**
A: Strong Consistency (data immediately consistent across all nodes) use karo jab: Financial transactions, Inventory management, Booking systems. Eventual Consistency (data eventually consistent, temporary lag ok) use karo jab: Social media feeds, Analytics dashboards, Caching layers. Decision factor: Business impact of stale data. Agar stale data se problem ho (double booking) toh strong consistency, nahi toh eventual consistency (cost-effective aur scalable).

**Q6: PostgreSQL vs MongoDB - Interview mein kab kya choose karein?**
A: PostgreSQL (SQL) choose karo jab: Complex queries/JOINs chahiye (reports, analytics), Strong ACID needed (banking, e-commerce orders), Data structure fixed hai (schema stable). MongoDB (NoSQL) choose karo jab: Flexible schema chahiye (rapid development, evolving requirements), Document-based data (user profiles, product catalogs), Horizontal scaling important (millions of users). Decision point: "Data structure kitna stable hai?" - Stable = SQL, Evolving = NoSQL.

**Q7: DNS Load Balancing vs Nginx Load Balancing - Main difference kya hai?**
A: DNS Load Balancing (Layer 3/4): Domain name multiple IPs ko resolve karta hai (client-side decision). Fast but sticky sessions issue (browser cache DNS). Example: example.com → [IP1, IP2, IP3] (round-robin). Nginx Load Balancing (Layer 7): Application level routing (URL/cookie based). Smart decisions (health checks, sticky sessions). Example: /api → Backend, /static → CDN. Use DNS for simple geographic distribution, Nginx for complex routing logic.

**Q8: Active Health Check vs Passive Health Check kaise kaam karta hai?**
A: Active Health Check (Proactive): Load balancer periodically ping karta hai servers ko (HTTP GET /health every 10 sec). Server respond nahi kiya toh mark as unhealthy → traffic stop. Example: Nginx sends GET request, agar 3 consecutive failures toh server removed. Passive Health Check (Reactive): Load balancer actual traffic monitor karta hai. Agar client requests fail ho rahi hain (5xx errors) toh server ko unhealthy mark karo. Active = Faster detection (10 sec), Passive = No extra load (production traffic se detect). Best practice: Dono use karo (Active + Passive).

---

## 📊 BONUS SECTION: Database Concepts Deep Dive (For Module 1 Context)

> **Note:** Ye topics Module 3 mein detail mein covered honge, but Module 1 mein requirements aur capacity planning ke liye basic understanding zaroori hai.

### 🔐 ACID vs BASE Properties

**ACID (SQL Databases ke liye):**
```
A = Atomicity (अटोमिसिटी):
    - Transaction ya toh COMPLETELY execute hoga ya COMPLETELY fail
    - No half-done transactions
    - Example: Bank transfer mein agar Account A se debit hua but Account B mein credit fail
      toh ROLLBACK hoga, Account A mein bhi amount wapis aayega
    - All or Nothing principle

C = Consistency (कंसिस्टेंसी):
    - Data hamesha valid state mein rahega
    - Database constraints violate nahi honge
    - Example: Agar age column mein constraint hai "age > 0" toh negative age allow nahi hoga
    - Rules are always enforced

I = Isolation (आइसोलेशन):
    - Multiple transactions simultaneously chale toh ek dusre ko affect nahi karenge
    - Example: User A aur User B simultaneously same product ki last item buy kar rahe
      hain, sirf ek succeed karega (locking mechanism)
    - Concurrent transactions don't interfere

D = Durability (ड्यूरेबिलिटी):
    - Ek baar transaction commit ho gaya toh data permanent hai
    - Power failure/crash ke baad bhi data safe rahega
    - Write-Ahead Logging (WAL) use karke disk par write hota hai
    - Data survives crashes
```

**BASE (NoSQL Databases ke liye):**
```
BA = Basically Available (बेसिकली अवेलेबल):
     - System hamesha available rahega (99.9%+ uptime)
     - Partial failures ke bawajood kaam karta rahega
     - Example: Ek Cassandra node down ho toh baki nodes se data milega

S = Soft State (सॉफ्ट स्टेट):
    - System ki state time ke saath change ho sakti hai (without input)
    - Data replicas ke beech synchronization background mein hota hai
    - Example: Cache data expire ho jata hai, stale data temporarily exist kar sakta hai

E = Eventual Consistency (इवेंचुअल कंसिस्टेंसी):
    - Eventually (kuch time baad) sab replicas consistent ho jayenge
    - Immediately consistent nahi, but given time (seconds/minutes) sync ho jayega
    - Example: Instagram par photo post ki, kuch friends ko turant dikha, kuch ko 30 sec
      baad dikha (replication lag)
```

**When to Use What:**
```
ACID (SQL)                          BASE (NoSQL)
    |                                    |
Banking Apps                      Social Media Apps
E-commerce Orders                 Analytics/Logging  
Inventory Management              Content Management
Booking Systems                   Real-time Feeds
    |                                    |
Correctness > Availability        Availability > Correctness
```

---

### 🗄️ Database Comparison Table: PostgreSQL vs MongoDB vs Cassandra

```
+----------------------+--------------------+--------------------+----------------------+
| Feature              | PostgreSQL (SQL)   | MongoDB (NoSQL)    | Cassandra (NoSQL)    |
+----------------------+--------------------+--------------------+----------------------+
| Data Model           | Relational (Tables)| Document (JSON)    | Wide Column (Tables) |
|                      | Fixed Schema       | Flexible Schema    | Schema Optional      |
+----------------------+--------------------+--------------------+----------------------+
| Query Language       | SQL                | MongoDB Query Lang | CQL (SQL-like)       |
|                      | (SELECT, JOIN)     | (find, aggregate)  | (No JOINs)           |
+----------------------+--------------------+--------------------+----------------------+
| Consistency          | Strong (ACID)      | Eventual (tunable) | Eventual (tunable)   |
|                      | ACID guaranteed    | Can configure level| Tunable consistency  |
+----------------------+--------------------+--------------------+----------------------+
| Scalability          | Vertical (Scale-Up)| Horizontal         | Horizontal           |
|                      | Read Replicas      | Sharding built-in  | Auto-sharding        |
+----------------------+--------------------+--------------------+----------------------+
| Indexing             | B-Tree (auto on PK)| B-Tree, Text       | Primary Key only     |
|                      | Secondary indexes  | Secondary indexes  | (Secondary slow)     |
+----------------------+--------------------+--------------------+----------------------+
| Best For             | Complex Queries    | Flexible Data      | Write-Heavy          |
|                      | JOINs, Aggregations| Rapid Development  | Time-series          |
|                      | Transactions       | Content Management | Logs, Events         |
+----------------------+--------------------+--------------------+----------------------+
| Use Cases            | Banking, ERP       | E-commerce Catalog | IoT Sensor Data      |
|                      | CRM, Inventory     | Content CMS        | User Activity Logs   |
|                      | Financial Systems  | User Profiles      | Messaging History    |
+----------------------+--------------------+--------------------+----------------------+
| Read Performance     | Fast (with indexes)| Fast (document-    | Fast (partition key) |
|                      | JOINs can be slow  | based queries)     | (No JOINs = faster)  |
+----------------------+--------------------+--------------------+----------------------+
| Write Performance    | Moderate           | Fast               | Very Fast            |
|                      | (ACID overhead)    | (async replication)| (Optimized for write)|
+----------------------+--------------------+--------------------+----------------------+
| Auto Primary Key     | ✅ YES             | ✅ YES (_id auto)  | ❌ NO (manual define)|
| Index                | (B-Tree index auto)| (ObjectId indexed) | (Partition key only) |
+----------------------+--------------------+--------------------+----------------------+
```

**Auto-Creation of Indexes on Primary Key:**
- **PostgreSQL/MySQL:** Jab tum `PRIMARY KEY` define karte ho, automatically B-Tree index create ho jata hai. Ye index `WHERE id = 5` jaisi queries ko O(log n) mein fast banata hai instead of O(n) full table scan.
- **MongoDB:** `_id` field automatically indexed hota hai (default Primary Key).
- **Cassandra:** Primary Key par index nahi banta, direct partition-based lookup hota hai (even faster but JOINs nahi ho sakte).

---

### ❌ SQL Unstructured Data Wastage Example

**Problem:** SQL tables fixed schema expect karte hain. Agar different rows mein different fields hain toh space waste hota hai.

**Example - Social Media Posts Table:**
```
+----+---------+---------+----------+----------+----------+--------+
| ID | UserID  | Type    | Text     | ImageURL | VideoURL | PollID |
+----+---------+---------+----------+----------+----------+--------+
| 1  | user123 | text    | "Hello!" | NULL     | NULL     | NULL   |  ← 3 columns wasted
| 2  | user456 | image   | NULL     | "img.jpg"| NULL     | NULL   |  ← 3 columns wasted  
| 3  | user789 | video   | NULL     | NULL     | "vid.mp4"| NULL   |  ← 3 columns wasted
| 4  | user999 | poll    | "Vote?"  | NULL     | NULL     | 101    |  ← 2 columns wasted
+----+---------+---------+----------+----------+----------+--------+

Problem:
- Har row mein 2-3 columns NULL hain (space waste)
- Storage inefficient: NULLs bhi space lete hain (metadata)
- Agar nayi post type add karni hai (e.g., Audio) toh ALTER TABLE (slow, downtime)

Solution (NoSQL - MongoDB):
{_id: 1, userId: "user123", type: "text", text: "Hello!"}  ← Only needed fields
{_id: 2, userId: "user456", type: "image", imageURL: "img.jpg"}  
{_id: 3, userId: "user789", type: "video", videoURL: "vid.mp4"}  
{_id: 4, userId: "user999", type: "poll", text: "Vote?", pollId: 101}

Benefit: No NULLs, flexible schema, storage efficient
```

---

### 🔄 Replication Strategies: Master-Slave vs Master-Master

**1. Master-Slave Replication (Already in notes, expanding):**
```
        WRITE                          READ (Load distributed)
          ↓                              ↑
      [Master DB] ─────replicate────→ [Slave 1]
          |                              ↑
          +─────────replicate────→ [Slave 2]
                                         ↑
Advantages:                        [Slave 3]
✅ Read scaling (multiple slaves)
✅ Backup (slaves have copy)
✅ Simple consistency (single write point)

Disadvantages:
❌ Master = Single Point of Failure (write downtime)
❌ Replication lag (slaves thoda delay se update hote hain, 100ms-1sec)
❌ Write scaling nahi (sirf ek master)
```

**2. Master-Master Replication (NEW - For High Write Availability):**
```
    WRITE ↓                    WRITE ↓
      [Master 1] ←──sync──→ [Master 2]
          ↓                      ↓
      Replicate             Replicate
          ↓                      ↓
      [Slave 1-1]           [Slave 2-1]
      [Slave 1-2]           [Slave 2-2]

Advantages:
✅ High Write Availability (dono masters writes le sakte hain)
✅ Geographic distribution (US master + Europe master, low latency)
✅ No single point of failure (ek master down toh dusra handle kare)

Disadvantages:
❌ Conflict resolution complex (same row ko dono masters mein update)
   Example: User ka name Master1 mein "Amit", Master2 mein "Sumit" update
   → Conflict! Last-Write-Wins ya Version Vector use karo
❌ Consistency issues (eventual consistency, immediate nahi)
❌ Complex setup and maintenance

When to Use:
- Multi-region applications (AWS US-East + EU-West)
- High write availability critical (e-commerce flash sales)
- Can tolerate eventual consistency
```

---

### 💥 Crash Recovery with Replica Replacement

**Scenario: Master Database Crash Ho Gaya!**

```
BEFORE CRASH:                         AFTER CRASH (Master fails):
                                      
[Master] ─→ [Slave1]                  [Master] ❌ DEAD
    ↓        [Slave2]                     ↓
  Clients    [Slave3]                  Clients ← No writes! 😱

STEP-BY-STEP RECOVERY PROCESS:

Step 1: DETECT FAILURE (10-30 seconds)
  - Health check fails (heartbeat missing)
  - Monitoring alerts (Prometheus/CloudWatch)
  - Example: 3 consecutive heartbeat failures = Master dead

Step 2: PROMOTE SLAVE TO MASTER (30-60 seconds - FAILOVER)
  - Automated (Orchestration tool: Kubernetes, AWS RDS)
  - Manual (DBA intervention in legacy systems)
  ┌──────────────────────────────────────┐
  │ [Slave1] ← PROMOTED ✅ (ab yeh Master)│  
  │    ↓                                 │
  │  [Slave2] ← Still slave              │
  │  [Slave3] ← Still slave              │
  └──────────────────────────────────────┘
  - DNS/Load Balancer update (client traffic Slave1 pe redirect)
  - Slave1 configuration change: READ_ONLY = OFF (ab writes accept karega)

Step 3: VERIFY DATA CONSISTENCY (Critical!)
  - Check replication lag resolved (Slave1 latest data)
  - Commit any pending transactions from Write-Ahead Log (WAL)

Step 4: SPAWN NEW REPLICA (Replace dead Master - 5-10 minutes)
  - New EC2/VM instance launch
  - Copy data from current Master (Slave1) → New Slave
  - Configure replication
  ┌──────────────────────────────────────┐
  │ [Slave1/New Master]                  │  
  │    ↓         ↓           ↓           │
  │ [Slave2] [Slave3] [New Slave4] ✅    │
  └──────────────────────────────────────┘

Step 5: MONITOR (Ongoing)
  - Verify replication working
  - Check no data loss (compare row counts, checksums)

TOTAL DOWNTIME: 30 seconds - 2 minutes (for automated failover)
                5-10 minutes (for manual failover)

REAL-WORLD EXAMPLE:
- AWS RDS Multi-AZ: Automated failover in 60-120 seconds
- Google Cloud SQL: Automated failover in ~30 seconds
- Self-managed: Manual failover can take 5-30 minutes (depends on team)
```

---


## Topic 1.3: Capacity Estimation (The Math)

## 🎯 1. Title / Topic: Capacity Estimation

## 🐣 2. Samjhane ke liye (Simple Analogy):
Capacity Estimation ek wedding plan karne jaisa hai. Tumhe pehle calculate karna padta hai: Kitne guests aayenge (users)? Kitna khana chahiye (storage)? Kitne waiters chahiye (servers)? Kitni chairs (bandwidth)? Agar 500 guests ke liye 100 chairs book kiye toh problem! Waise hi system design mein pehle calculate karo kitne resources chahiye - servers, storage, bandwidth. Bina calculation ke resources book karna = paise waste ya system crash.

## 📖 3. Technical Definition (Interview Answer):
Capacity Estimation is the process of calculating the infrastructure resources (servers, storage, bandwidth, memory) required to handle the expected load based on user traffic, data volume, and performance requirements.

**Key terms:**
- **DAU (Daily Active Users):** Ek din mein kitne unique users app use karte hain. Example: Instagram ka 500M DAU.
- **RPS (Requests Per Second):** Ek second mein kitne requests aate hain. Formula: (DAU × Requests per user) / 86400 seconds.
- **Storage:** Kitna data store karna hai (GB/TB/PB). Formula: Data per user × Total users × Time period.
- **Bandwidth:** Network speed chahiye upload/download ke liye (Mbps/Gbps). Ingress = Upload, Egress = Download.
- **80-20 Rule (Pareto Principle):** 20% data ko 80% baar access kiya jata hai. Cache mein ye 20% hot data rakho.

## 🧠 4. Zaroorat Kyun Hai? (Why?):
**Main Problem:** Bina capacity estimation ke tum blindly resources provision karoge. Agar kam resources liye toh system crash (users frustrated), agar zyada liye toh paise waste (unnecessary servers running).

**Business Impact:** Proper estimation se cost optimize hota hai. AWS/GCP pay-per-use hai, agar 10 servers ki zaroorat hai aur 50 book kar liye toh monthly bill 5x ho jayega. Ya agar 2 servers liye aur 10 chahiye the toh downtime = revenue loss.

**Technical Benefit:** Capacity estimation se tum bottlenecks pehle identify kar sakte ho (database storage full ho jayega 6 months mein, plan karo), scaling strategy bana sakte ho, aur interviewer ko dikhata hai tumhe production experience hai (numbers se baat karte ho, vague nahi).

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario):
Agar Capacity Estimation nahi kiya toh:
- **Technical Error:** Under-provisioning → Server CPU 100%, Memory full → Requests timeout → 503 Service Unavailable. Ya Over-provisioning → 90% servers idle → Paise waste.
- **User Impact:** Slow response times (>5 sec) → Users frustrated → App uninstall → Negative reviews.
- **Business Impact:** Downtime = Revenue loss (Amazon: 1 sec delay = $1.6B loss/year). Ya unnecessary infrastructure cost → Burn rate high → Funding issues.
- **Real Example:** Pokemon Go (2016 launch) - Capacity estimation galat tha, expected 5M users but 50M+ aaye. Servers crash ho gaye, 2 weeks tak instability. Niantic ko emergency mein Google Cloud se 10x servers lene pade (costly). Proper estimation hota toh gradual scaling plan ready hota.

## ⚙️ 6. Under the Hood (Technical Working):

**Capacity Estimation Process (Step-by-step):**

**1. Traffic Estimation (Users & Requests):**
```
Step 1: Define DAU (Daily Active Users)
Step 2: Calculate requests per user per day
Step 3: Calculate total requests per day = DAU × Requests per user
Step 4: Calculate RPS (Requests Per Second) = Total requests / 86400 seconds
Step 5: Calculate Peak RPS = Average RPS × 2 (or 3 for spikes)
```

**2. Storage Estimation:**
```
Step 1: Calculate data per user (text, images, videos)
Step 2: Calculate daily storage = DAU × Data per user
Step 3: Calculate storage for X years = Daily storage × 365 × X years
Step 4: Add replication factor (3x for redundancy)
Step 5: Add growth buffer (20-30% extra)
```

**3. Bandwidth Estimation:**
```
Step 1: Calculate Ingress (Upload) = Write requests × Data size
Step 2: Calculate Egress (Download) = Read requests × Data size
Step 3: Convert to Mbps or Gbps
Step 4: Peak bandwidth = Average × 3 (for traffic spikes)
```

**4. Memory Estimation (Cache):**
```
Step 1: Identify hot data (80-20 rule: 20% data = 80% requests)
Step 2: Calculate cache size = 20% of total storage
Step 3: Add metadata overhead (10-15%)
```

**ASCII Diagram - Capacity Estimation Flow:**
```
                    [REQUIREMENTS]
                          |
                    10M DAU, 5 years
                          |
                          v
            +-------------+-------------+
            |             |             |
        TRAFFIC       STORAGE       BANDWIDTH
            |             |             |
            v             v             v
    +--------------+ +--------------+ +--------------+
    | RPS Calc     | | Data/User    | | Ingress      |
    | Peak RPS     | | Daily Total  | | Egress       |
    | Servers      | | 5 Year Total | | Peak Traffic |
    +--------------+ +--------------+ +--------------+
            |             |             |
            +-------------+-------------+
                          |
                          v
                  [INFRASTRUCTURE]
                          |
            +-------------+-------------+
            |             |             |
        Servers       Database        CDN
        (EC2)         (RDS/S3)      (CloudFront)
```

## 🛠️ 7. Problems Solved:
- **Cost Optimization:** Exact resources calculate karke unnecessary expenses avoid karo. Auto-scaling policies set karo based on estimates.
- **Performance Planning:** Bottlenecks pehle identify karo (database storage 80% full in 3 months → plan migration).
- **Scaling Strategy:** Growth projections se pata chalta hai kab horizontal scaling chahiye, kab database sharding.
- **Interview Confidence:** Numbers se baat karne se interviewer impressed hota hai, shows you think like a senior engineer.

## 🌍 8. Real-World Example:
**Twitter (2020 estimates):** 330M MAU (Monthly Active Users), ~150M DAU. Average user: 10 tweets read, 1 tweet post per day. Calculation: 150M × 10 = 1.5B read requests/day = 17,361 RPS (average), Peak RPS = 50K+ (during events like Super Bowl). Storage: 500M tweets/day × 280 chars × 2 bytes = 280 GB/day text. Images: 200M images/day × 200 KB = 40 TB/day. Total: ~40 TB/day → 14.6 PB/year. Infrastructure: 1000+ servers, Multi-region deployment, Cassandra for tweets, Manhattan (custom DB) for timelines. Result: Handles 500M+ tweets/day, 99.9% uptime.

## 🔧 9. Tech Stack / Tools:
**Calculation Tools:**
- **Excel/Google Sheets:** Capacity estimation spreadsheet banao, formulas use karo
- **AWS Calculator:** https://calculator.aws - Infrastructure cost estimate karne ke liye
- **Back-of-envelope calculations:** Interview mein quick math (calculator allowed nahi hota)

**Monitoring Tools (Production mein actual capacity track karne ke liye):**
- **Prometheus + Grafana:** Real-time metrics (CPU, Memory, RPS)
- **CloudWatch (AWS):** Infrastructure monitoring, alerts set karo jab threshold cross ho
- **New Relic / Datadog:** Application performance monitoring (APM)

## 📐 10. Architecture/Formula:

**Key Formulas (Interview mein yaad rakho):**

**1. RPS (Requests Per Second):**
```
RPS = (DAU × Requests_per_user) / 86400

Example:
DAU = 10 million
Requests per user = 20 (10 reads, 10 writes)
RPS = (10M × 20) / 86400 = 200M / 86400 = 2,315 RPS (average)
Peak RPS = 2,315 × 3 = 6,945 RPS (traffic spikes ke liye)

Servers needed = Peak RPS / RPS_per_server
If 1 server handles 500 RPS → 6,945 / 500 = 14 servers
Add 20% buffer → 14 × 1.2 = 17 servers
```

**2. Storage Estimation:**
```
Storage = Data_per_item × Items_per_day × Days × Replication_factor

Example (Instagram-like app):
- 10M photos uploaded/day
- Average photo size = 2 MB
- Store for 5 years
- Replication factor = 3 (redundancy)

Daily storage = 10M × 2 MB = 20 TB/day
5 year storage = 20 TB × 365 × 5 = 36,500 TB = 36.5 PB
With replication = 36.5 PB × 3 = 109.5 PB
```

**3. Bandwidth Estimation:**
```
Bandwidth = (Data_transferred_per_second) / 8

Example:
- 2,315 RPS (from above)
- Average response size = 100 KB
- Data per second = 2,315 × 100 KB = 231.5 MB/sec
- Bandwidth = 231.5 MB/sec × 8 = 1,852 Mbps ≈ 1.85 Gbps

Ingress (Upload) = Write requests × Data size
Egress (Download) = Read requests × Data size
(Usually Egress >> Ingress for read-heavy systems)
```

**4. Memory (Cache) Estimation:**
```
Cache Size = Total_storage × 0.20 (80-20 rule)

Example:
- Total storage = 100 TB
- Hot data (20%) = 100 TB × 0.20 = 20 TB
- Cache this in Redis/Memcached
- Distributed cache: 20 TB / 100 GB per node = 200 cache nodes
```

**Read-Heavy vs Write-Heavy Impact:**
```
READ-HEAVY (100:1 ratio)          WRITE-HEAVY (1:10 ratio)
        |                                  |
Example: YouTube                   Example: IoT Sensors
        |                                  |
Optimization:                      Optimization:
- Cache aggressively               - Message queues (Kafka)
- CDN for static content           - Write-optimized DB (Cassandra)
- Read replicas (DB)               - Batch writes
        |                                  |
Bandwidth: Egress >> Ingress       Bandwidth: Ingress >> Egress
```

## 💻 11. Code / Flowchart:

**Capacity Estimation Calculation (Python-style pseudocode with DETAILED comments):**
```python
# ============================================================================
# TRAFFIC ESTIMATION (Kitne servers chahiye calculate karne ke liye)
# ============================================================================
DAU = 10_000_000  # Daily Active Users = Ek din mein kitne unique log app use karte hain
                  # Example: Instagram ka ~500M DAU, Twitter ka ~200M DAU

requests_per_user = 20  # Har user average kitne API calls karta hai ek din mein
                        # Example: Feed refresh=5, Profile view=3, Post=2, etc. = ~20 total

total_requests_per_day = DAU * requests_per_user  # Total daily API calls
                                                   # 10M × 20 = 200 million requests per day

average_RPS = total_requests_per_day / 86400  # RPS = Requests Per Second (ek second mein kitne)
                                              # 86400 = seconds in a day (24×60×60)
                                              # 200M / 86400 = 2,315 RPS (average load)

peak_RPS = average_RPS * 3  # Peak traffic planning (traffic uniform nahi hota)
                            # Multiplier 2-3x leta hain spike handle karne ke liye
                            # Example: E-commerce par 9PM sale time, social media par evening
                            # 2,315 × 3 = 6,945 RPS (peak time capacity)

# ============================================================================
# STORAGE ESTIMATION (Kitna database/S3 space chahiye)
# ============================================================================
data_per_user_per_day = 5 * 1024 * 1024  # Har user daily kitna data generate karta hai
                                         # 5 MB in bytes (1 MB = 1024 KB = 1024×1024 bytes)
                                         # Breakdown: 2 photos (2MB each) + text/metadata (1MB)

daily_storage = DAU * data_per_user_per_day  # Ek din mein total storage needed
                                              # 10M users × 5 MB = 50 TB per day
                                              # 1 TB = 1024 GB = 1024×1024 MB

storage_5_years = daily_storage * 365 * 5  # 5 saal ka data store karna hai (requirement)
                                           # 50 TB × 365 days × 5 years = 91,250 TB = 91.25 PB
                                           # PB = Petabyte = 1024 TB

with_replication = storage_5_years * 3  # Production mein data ki 3 copies rakhte hain
                                        # 1 Primary + 2 Replicas (fault tolerance ke liye)
                                        # Agar 1 server crash ho toh data loss nahi hoga
                                        # 91.25 PB × 3 = 273.75 PB (actual storage cost)

# ============================================================================
# BANDWIDTH ESTIMATION (Network speed kitni chahiye)
# ============================================================================
average_response_size = 100 * 1024  # Ek API response mein kitna data transfer hota hai
                                    # 100 KB in bytes (feed mein 10 posts, har post 10KB)

data_per_second = average_RPS * average_response_size  # Per second kitna data transfer
                                                       # 2,315 requests × 100 KB = 231.5 MB/sec
                                                       # Ye EGRESS hai (download/outgoing)

bandwidth_required = data_per_second * 8 / (1024**2)  # Mbps/Gbps mein convert karo
                                                      # 8 multiply kyunki 1 Byte = 8 bits
                                                      # Network speed bits mein measure hota hai
                                                      # 231.5 MB/sec × 8 = 1,852 Mbps ≈ 1.85 Gbps

# ============================================================================
# MEMORY (CACHE) ESTIMATION (Redis/Memcached mein kitna RAM chahiye)
# ============================================================================
cache_size = storage_5_years * 0.20  # 80-20 Rule (Pareto Principle)
                                     # 20% data ko 80% baar access kiya jata hai (hot data)
                                     # Example: Trending videos, Popular posts, Recent feeds
                                     # 91.25 PB × 0.20 = 18.25 PB cache mein rakho
                                     # Distributed Redis cluster: 18.25 PB / 64GB per node
                                     # = ~300,000 cache nodes (realistic nahi, optimize karo)
```

**Interview Flowchart:**
```
Start Capacity Estimation
     |
     v
[Ask Scale Questions]
     |
     ├─> "Kitne users expected?" → DAU
     ├─> "Read-heavy ya write-heavy?" → Ratio
     └─> "Kitne time ka data store?" → Years
     |
     v
[Calculate Traffic]
     |
     ├─> RPS = (DAU × Requests) / 86400
     ├─> Peak RPS = RPS × 3
     └─> Servers = Peak RPS / 500 (per server capacity)
     |
     v
[Calculate Storage]
     |
     ├─> Daily = DAU × Data per user
     ├─> Total = Daily × 365 × Years
     └─> With replication = Total × 3
     |
     v
[Calculate Bandwidth]
     |
     ├─> Ingress = Write RPS × Data size
     ├─> Egress = Read RPS × Data size
     └─> Peak = Average × 3
     |
     v
[Calculate Cache]
     |
     └─> Cache = Total storage × 0.20
     |
     v
[Present Numbers to Interviewer]
"We need ~20 servers, 100 TB storage, 2 Gbps bandwidth"
```

## 📈 12. Trade-offs:
- **Accuracy vs Speed:** Interview mein perfect calculation ki zaroorat nahi, ballpark estimate chahiye. **Balance:** Round numbers use karo (10M instead of 9.7M), quick mental math karo. Interviewer accuracy se zyada approach dekhta hai.
- **Over-provisioning vs Under-provisioning:** Over-provisioning (zyada resources) = Safe but costly. Under-provisioning (kam resources) = Cheap but risky (downtime). **Solution:** Start with estimates + 20% buffer, use auto-scaling to handle spikes.
- **Current vs Future:** Current load ke liye design karo ya 5 years future ke liye? **Balance:** Design for 2x current load, plan for 10x (architecture should support scaling, but don't build for 10x day 1).

## 🐞 13. Common Mistakes:
- **Mistake 1:** Vague numbers - "Bahut users hain, bahut storage chahiye". **Why wrong:** Shows lack of analytical thinking. **Fix:** Always give specific numbers: "10M DAU, 100 TB storage, 2 Gbps bandwidth". Agar exact nahi pata toh assume karo aur bolo: "Assuming 10M users..."
- **Mistake 2:** Peak load ignore karna - Average RPS calculate kiya but peak nahi. **Why wrong:** Traffic spikes ke time system crash hoga (Black Friday, viral event). **Fix:** Peak RPS = Average × 2 or 3, design for peak.
- **Mistake 3:** Replication factor bhoolna - Storage calculate kiya but redundancy nahi. **Why wrong:** Production mein data 3 copies mein store hota hai (backup). **Fix:** Final storage = Calculated × 3.
- **Mistake 4:** 80-20 rule ignore karna - Saara data cache karne ki koshish. **Why wrong:** Cache expensive hai (RAM), sab kuch cache nahi kar sakte. **Fix:** Sirf 20% hot data cache karo jo 80% requests serve karta hai.

## ✅ 14. Zaroori Notes for Interview:
1. **Always Start with Scale:** Pehla question: "Kitne users expected hain?" Isse saare calculations depend karte hain. Agar interviewer nahi bolta toh assume karo: "I'm assuming 10M DAU, please correct if different."

2. **Use Round Numbers:** Interview mein 9,876,543 mat bolo, 10M bolo. Mental math easy ho jata hai aur interviewer ko bhi samajh aata hai. Precision se zyada approach matter karta hai.

3. **Show Your Work:** Calculation steps whiteboard par likho, don't just give final answer. Example:
   ```
   DAU = 10M
   Requests/user = 20
   Total = 10M × 20 = 200M requests/day
   RPS = 200M / 86400 ≈ 2,300 RPS
   ```

4. **Mention 80-20 Rule:** Cache estimation mein explicitly bolo: "Using the 80-20 rule, I'll cache 20% of data which serves 80% of requests." Ye shows you know production best practices.

5. **Read-Heavy vs Write-Heavy:** Ye explicitly identify karo aur bolo: "This is a read-heavy system (100:1 ratio), so I'll focus on caching and read replicas." Architecture decisions isse depend karte hain.

6. **Common Follow-ups:**
   - "What if traffic increases 10x?" → Horizontal scaling, auto-scaling policies, CDN
   - "How did you calculate storage?" → Walk through formula step-by-step
   - "Why 3x replication?" → Explain redundancy (1 primary + 2 backups for fault tolerance)

7. **Time Management:** Capacity estimation par 5-7 minutes spend karo, zyada time liya toh design ka time nahi milega. Quick calculations karo, move on.

## ❓ 15. FAQ & Comparisons:

**Q1: DAU vs MAU - Interview mein kaunsa use karein?**
A: DAU (Daily Active Users) use karo capacity estimation ke liye kyunki daily load calculate karna hai. MAU (Monthly Active Users) product metrics ke liye hota hai. Conversion: MAU ≈ DAU × 3 to 5 (rough estimate). Example: 100M MAU ≈ 20-30M DAU.

**Q2: Average RPS vs Peak RPS - Kiske liye design karein?**
A: Always design for Peak RPS, not average. Peak = Average × 2 to 3 (traffic spikes ke liye). Example: E-commerce site par Black Friday sale ke time 10x traffic aa sakta hai. Solution: Auto-scaling policies set karo jo peak handle kar sake, off-peak time par scale down ho jaye (cost save).

**Q3: Storage estimation mein replication factor kyun zaroori hai?**
A: Production mein data hamesha multiple copies mein store hota hai (redundancy for fault tolerance). Standard: 3 copies (1 primary + 2 replicas). Agar 1 server crash ho toh data loss nahi hoga. Interview mein agar replication mention nahi kiya toh follow-up aayega: "What about data redundancy?" Always multiply storage by 3x.

**Q4: 80-20 rule practically kaise apply hota hai?**
A: 80-20 rule (Pareto Principle): 20% data ko 80% baar access kiya jata hai. Example: YouTube par trending videos (20%) ko 80% views milte hain. Cache strategy: Ye 20% hot data Redis/Memcached mein rakho, baaki 80% cold data database mein. Benefit: Cache hit rate high (80%), cost low (sirf 20% data cache).

**Q5: Bandwidth estimation mein Ingress vs Egress kya hai?**
A: Ingress = Incoming traffic (Upload) - Users jo data bhejte hain (photos upload, messages send). Egress = Outgoing traffic (Download) - Users jo data receive karte hain (feed load, videos watch). Read-heavy systems mein Egress >> Ingress (YouTube: videos download zyada, upload kam). Write-heavy systems mein Ingress >> Egress (IoT sensors: data upload zyada). CDN mainly Egress reduce karta hai (static content edge servers se serve).

---

**🎉 Module 1 Complete! 🎉**

Aapne successfully Module 1: Fundamentals & Capacity Planning complete kar liya hai! 

**Covered Topics:**
✅ 1.1 System Design Basics (Scalability, Reliability, Maintainability, Fault Tolerance)
✅ 1.2 Requirements Gathering (FR, NFR, CAP Theorem, Throughput vs Latency)
✅ 1.3 Capacity Estimation (Traffic, Storage, Bandwidth, Memory calculations)

**Next Steps:**
Kya aap Module 2: Scaling Architectures ke liye ready hain? 

Module 2 mein hum cover karenge:
- 2.1 Vertical Scaling (Scale Up)
- 2.2 Horizontal Scaling (Scale Out)  
- 2.3 Load Balancing (Algorithms, Layer 4 vs 7, Health Checks)

**Should I proceed with Module 2?** 🚀
