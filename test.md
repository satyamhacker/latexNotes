### 📄 Page 1: Introduction & Step 1 (Requirements)

**Header:**
* **Date:** 12/11/2025
* **Topic:** # Udemy -> System Design Masterclass

**# Section -> 1 -> Introduction:**
* **Video 1, 2:** "Not of use" (Ye videos kaam ke nahi hain, skip kiye gaye hain).
* **Video 3:** Yahan se "Framework for System Design Interviews" shuru hota hai.

**Step -> 1 -> Deciding Requirements (Requirements decide karna):**
Is step mein hum requirements ko do hisson (parts) mein divide karte hain:

1.  **Functional Requirements:**
    * Iska matlab hai: **What should the system do?** (System ko kya kaam karna chahiye? Features kya honge?)
2.  **Non-Functional Requirements:**
    * Iska matlab hai: **How well your system perform?** (Aapka system kaisa perform karega?)
    * Example parameters: Speed, Scalability... Etc.
    * Isme **Latency** bhi include hoti hai (System kitni jaldi respond karta hai).

---

### 📄 Page 2: Step 2 (Capacity Estimation)

**Step -> 2 -> Capacity Estimation:**
Is step mein hum numbers calculate karte hain:
* **Sawaal:** How many servers (Kitne servers), how many databases (kitne databases), how many caches... etc. ki zarurat padegi?

**Ye estimation in cheezon par depend karta hai:**
1.  **DAU/MAU:** Daily Active Users / Monthly Active Users (Rozana aur mahine mein kitne users active hain).
2.  **Throughput:** System kitna load le sakta hai.
3.  **Storage / Memory:** Data store karne ki jagah.
4.  **Network / Bandwidth:** Internet speed aur data transfer capacity.

**Detailed Definitions (Jo notes mein likhi hain):**
* **Throughput:** How many requests our system processes each second. (Hamara system har second kitni requests process kar sakta hai).
* **Storage & Memory:** Amount of Storage and memory required. (Total kitni storage aur RAM ki requirement hogi).
* **Network & Bandwidth:** How much data move in and out of Server System. (Server system se kitna data aa raha hai aur ja raha hai).

*(Footer pe likha hai: P.T.O - Please Turn Over)*

---

### 📄 Page 3: Steps 3, 4, & 5 (Design & Deep Dive)

**Step -> 3 -> API Design:**
API design karte waqt humein 3 cheezon par focus karna hai:
1.  **Endpoint:** (URL path kya hoga).
2.  **Body:** (Request ke andar kya data jayega).
3.  **Response:** (Server wapas kya bhejega).

**Step -> 4 -> High Level Design (HLD):**
* **Instruction:** Draw the box diagram and all. (System ka ek upar-upar se box diagram banao).
* **Diagram flow:** Client <-> API Gateway <-> (Aage connect hoga services se).

**Step -> 5 -> Deep Dive:**
Ab system ke specific parts ko detail mein discuss karna hai:
* **Database Selection:** Konsa DB use karein? (Example: SQL vs NoSQL).
* **Database Modeling:** Data kaise structure hoga.
* **Caches:** Speed badhane ke liye caching use karna.
* **Other components:** Example -> CDN (Content Delivery Network) images/videos ke liye.

**Bottom Note:**
> "This five (5) Step make system design framework for every system."
> (Ye paanch steps har system ke liye ek standard design framework banate hain).
> **Examples:** Facebook, Youtube... etc.

---





=============================================================


### 📄 Page 10: Client-Server & Database Basics

**Header:**
* **Section -> 10 to 17:** Ye appendix section hai "The Ultimate System Design" ka. (Note: Pehle ye basic clarity honi chahiye).

**Video -> 171 -> Client & Server:**
* **Client:** Client wo device hai jo information request karta hai (Jaise aapka mobile ya laptop).
* **Server:** Server ek computer hai jo fast hota hai. Ye client ki request sunta hai (listens) aur wapas jawab deta hai (responds).
* **Diagram:** User (Client) -> Request Bhejta hai -> Server -> Response (Webpage) wapas bhejta hai.

**Video -> 172 -> Database:**
* **Purpose:** Data store karne ke liye humein Database chahiye.
* **Storage Types:**
    1.  **Normal Data:** Database mein store hota hai.
    2.  **Static/Heavy Data:** (Jaise images, videos) Inke liye "Object Storage" use hota hai kyunki ye size mein bade hote hain.

---

### 📄 Page 11: Dynamic Content & Scaling Types

**Database (Continued):**
* Similarly, humare paas Database hota hai **Dynamic Content** store karne ke liye.
* **Dynamic Content:** Wo content jo change ho sakta hai (Jaise user profile, PG room availability).

**Video -> 173 -> Vertical vs Horizontal Scaling:**
* **Problem:** Jab server par load badh jata hai (zyada users aa jate hain), toh use handle kaise karein?
* **Solution 1: Vertical Scaling:**
    * Iska matlab hai server ki power badhana (CPU aur RAM badhana).
    * **Limitation:** Iski ek limit hoti hai. Aap ek hi computer ko infinite power nahi de sakte.

---

### 📄 Page 12: Horizontal Scaling & Load Balancing

**Solution 2: Horizontal Scaling:**
* Iska matlab hai **Number of Servers** badhana (ek powerful server ki jagah kayi saare servers lagana).

**Video -> 174 -> Load Balancing:**
* Horizontal scaling mein request ko balance karne ke liye hum **Load Balancer** use karte hain.
* **Process:**
    1.  Request pehle **Load Balancer** ke paas jati hai.
    2.  Load Balancer us load ko **equally distribute** kar deta hai multiple servers ke beech mein.

**Video -> 175 -> Database Sharding:**
* **Problem:** Jab users bahut zyada badh jate hain (millions mein), toh do problems aati hain:
    1.  Server overwhelm ho jata hai (Load Balancer se solve ho gaya).
    2.  **Database** overwhelm ho jata hai (Iska solution Sharding hai).

---

### 📄 Page 13: Sharding & Replication

**What is Database Sharding?**
* Iska matlab hai apne single database ko todkar **Several Smaller Databases** mein split karna.

**Video -> 176 -> Database Replication:**
* Sirf Sharding kaafi nahi hai. Humein **Replication** bhi chahiye.
* **Replication:** Iska matlab hai database ki **Copies** banana.
* **Why?** Agar ek database fail ho jaye, toh humare paas kam se kam ek copy (replica) honi chahiye taaki system chalta rahe.
* Is process ko **Database Replication** kehte hain.
* **Benefit:** Ye **Crash Recovery** mein help karta hai.

---

### 📄 Page 14: Crash Recovery & Caching

**Crash Recovery (Cont.):**
* Example: Agar shared database crash ho jaye, toh hum use turant uske replica se replace kar sakte hain. Isse ensure hota hai ki "No Data is ever Lost".

**Video -> 177 -> Cache:**
* **Example:** Agar koi user website ko din mein 100 baar visit karta hai. Iska matlab hum database se same data baar-baar maang rahe hain.
* Is cheez ko optimize karne ke liye hum **Cache** use karte hain.
* **Definition:** Cache ek "Quick Access Memory" ki tarah hai jo wo information store karta hai jo log baar-baar poochte hain (frequently asked).
* **Performance:** Cache se data fetch karna Database se data fetch karne ke comparison mein **Much Faster** hota hai.

---

### 📄 Page 15: Object Storage & CDN Introduction

**Video -> 178 -> Content Delivery Network (CDN):**
* **Problem:** Object Storage (jo Page 10 pe dekha tha) static assets hold karta hai (Images, Videos, HTML files).
* Ye assets bahut heavy hote hain. Agar user server se door hai, toh inhe load hone mein time lagta hai.
* **Solution:** Is problem ko solve karne ke liye hum **CDN** use karte hain.
* **CDN:** Ye static assets ko cache karta hai aur duniya bhar mein alag-alag locations par rakhta hai taaki access fast ho.

---

### 📄 Page 16: CDN Details & Microservices Intro

**CDN (Continued):**
* CDN aapke website ke **Static Content** ki copies store karta hai.
* **Static Content:** Example -> Images, Videos, Static files (Wo cheezein jo jaldi change nahi hoti).
* **Process:** Data user ke closest server se serve hota hai, na ki main server se.

**Video -> 179 -> Monolith vs Microservices:**
* **Monolith:**
    * Isme saare tasks ek **Single Service** handle karti hai.
    * Pura code ek hi jagah hota hai.
* **Microservices:**
    * **Definition:** "What is Service?" -> Service servers ka ek set hai jo kisi **Specific Task** ko handle karne mein specialize karta hai.

---

### 📄 Page 17 (Continuation of Microservices logic):

* **Understanding the difference:**
    * **Monolithic:** Sab kuch ek sath mix hai.
    * **Microservices:** Har feature (jaise Login, Payment, Orders) ki apni alag service hai.

*(Note: Notes mein ye part thoda mix hai, par core concept yahi hai ki Microservices mein har task dedicated service ke paas hota hai).*

---

### 📄 Page 18 & 19: Message Queues (Important for logic)

**Video -> 180 -> Message Queue:**
* **Scenario:** Imagine karo bohot saare users order place kar rahe hain.
* Sequence aisa hai: First **Order Processing** -> Then **Payment Processing**.
* **Problem:** Agar payment service slow hai, toh order service atak jayegi.
* **Solution:** Introduce **Message Queue** between Order and Payment services.

**Process (Decoupling):**
1.  Order service order receive karti hai.
2.  Wo order ko **Message Queue** mein bhej deti hai.
3.  Aur phir wo us order ke baare mein bhool jati hai (wait nahi karti).
4.  Payment Processing service queue se order uthati hai aur process karti hai.
* **Benefit:** Isse ye dono services **Decoupled** (independent) ho jati hain. New orders turant process ho jate hain bina payment ka wait kiye. Ye system ko **More Efficient** banata hai.

---

### 📄 Page 20: API Gateway

**Video -> 181 -> API Gateway:**
* **Problem:** Kuch users book order kar rahe hain, kuch offers request kar rahe hain. Alag-alag requests hain.
* **Solution:** Managing different requests using **API Gateway**.
* **Function:** API Gateway ek **Single Entry Point** ki tarah act karta hai.
* Ye saari incoming requests ko sahi jagah direct karta hai (Route karta hai).
* Example: Agar order ki request aayi -> To Order Service. Agar payment ki aayi -> To Payment Service.
* **Frameworks:** Node Express, Django, Springboot wagara use karke hum backend banate hain jo ye handle karta hai.

---

### 🚀 Quick Summary for Your "PG Management System":

Based on these notes, aapka system aisa dikhega:

1.  **Client:** Tenant/Owner ka Mobile App.
2.  **API Gateway:** Saari requests pehle yahan aayengi.
3.  **Microservices:**
    * *Room Service:* Rooms dikhane ke liye.
    * *Booking Service:* Bed book karne ke liye.
    * *Payment Service:* Rent lene ke liye.
4.  **Message Queue:** Jab koi "Book Now" dabaye, toh request Queue mein jaye taaki Payment fail hone par bhi booking process hang na ho.
5.  **Database:** SQL Database (User info ke liye).
6.  **CDN/Object Storage:** PG ke photos aur videos store karne ke liye (taaki app fast chale).

=============================================================

### 📄 Page 21: Scalability

**Header:**
* **Section -> 11 -> Appendix -> Design Goals Buzzwords:**
* **Video -> 182 -> Introduction:** (Not of use - Kaam ka nahi hai).

**Video -> 183 -> Scalability:**
* **Definition:** Scalability system ki wo ability hai jisse wo badhte hue workload (more work) ko smoothly handle kar sake jaise-jaise demand grow hoti hai.

**Example (Dukaan wala example):**
* Ek shop hai jisme **One Checkout Counter** hai.
* Ab shop ki popularity badh gayi (More customers).
* Line lambi hone ki wajah se customers frustrate ho gaye (Wait time increases).
* **Solution:** Shop ne **Multiple Checkout Counters** laga diye.
* **Result:** Customers ab khush hain kyunki "Less Waiting Time" hai.
* Iska matlab shop ne **Scaled Up** kiya.

**Technical Link:**
* Similarly, humare technical system (software) ko bhi scale up karne ki zarurat padti hai jab zyada users join karte hain.

---

### 📄 Page 22: Availability & Consistency

**Video -> 184 -> Availability:**
* **Definition:** Availability ka matlab hai ki aapka system kitne time tak **Up** (chalu) ya **Operational** rehta hai.
* (Jitna zyada time system chalega bina down huye, utni achi availability).

**Video -> 185 -> Consistency:**
* **Definition:** Consistency ka matlab hai ki har koi **Same Time** par **Same Information** dekhe.
* **Types of Consistency:**
    1.  **Strong Consistency:**
        * Iska matlab hai "Consistent Everyone Immediately".
        * Bina kisi delay ke, sabko same data visible hona chahiye immediately.

---

### 📄 Page 23: Eventual Consistency & Fault Tolerance

**(Continuation of Consistency from Page 22):**
* 2. **Eventual Consistency:**
    * Data thode time ke baad consistent ho jayega (**Over time**), lekin zaruri nahi ki wo **Instantly** (turant) consistent ho.

**Video -> 186 -> Fault Tolerance / No SPOF:**
* **Goal:** Ye ensure karna ki humare system mein koi **Single Point of Failure (SPOF)** na ho.

**Example (Bridge wala):**
* Ek bridge hai jisme sirf **One Pillar** hai.
* Agar wo pillar gir gaya (goes down), toh **Whole Bridge Collapses** (pura bridge gir jayega).
* Yahan wo pillar **Single Point of Failure** hai.

**Technical Diagram Explanation:**
* Diagram mein dikhaya gaya hai: `Client <-> Server <-> Database`.
* **Sawaal:** What if server goes down? (Agar server kharab ho jaye toh?)
* Yahan Server **Single Point of Failure** hai. Agar ye down hua, toh "Nothing will work" (kuch nahi chalega) aur sab kuch down ho jayega.
* **Conclusion:** So, we don't want any single point of failure in our system. (Hum nahi chahte ki humare system mein koi bhi aisi ek cheez ho jiske kharab hone se sab kuch ruk jaye).

---

### 💡 Applying this to your "Smart PG System" (OYO for PGs):

1.  **Scalability:** Jab aapke app par 10 PGs se 1000 PGs ho jayenge, tab aapka backend "Scale" hona chahiye (Page 21 ke hisaab se multiple servers add karke).
2.  **Strong Consistency (Zaruri hai):** **Bed Booking** ke time par.
    * *Example:* Agar Bed A ko User 1 book kar le, toh turant User 2 ko wo "Booked" dikhna chahiye. Yahan delay nahi chalega, warna double booking ho jayegi.
3.  **Fault Tolerance:** Aap multiple servers use karenge (Load balancer ke saath) taaki agar ek server crash bhi ho jaye, toh Tenants app khol sakein aur rent pay kar sakein.



=============================================================

### 📄 Page 24: Networking Basics (IP & DNS)

**Header:**
* **Section -> 12 -> Appendix -> Networking Buzzwords:**
* **Problem Statement:** (Previous page se continue) "So, how to solve this issue... by adding more servers." (Zayada servers add karke hum load handle karte hain).

**Video -> 187 -> IP Address:**
* **Concept:** Har computer ka internet par ek address hota hai, jise **IP Address** kehte hain.
* **Types:** IPv4, IPv6.
* **Definition:** "Each computer is known by its IP address on Internet." (Internet par har computer apni IP se pehchana jata hai).

**Video -> 188 -> DNS (Domain Name Service):**
* **Question:** How does yours find the right server when you type `xyz.com`? (Jab aap koi website type karte hain toh computer ko kaise pata chalta hai ki kis server par jana hai?)
* **Answer:** DNS.
* **Function:** It maps site name to its IP. (Ye website ke naam ko uske IP address se jodta hai).

---

### 📄 Page 25: Protocols Introduction

**Video -> 189:** "Not of use" (Kaam ka nahi hai).

**Video -> 190 -> Protocols -> Introduction:**
* **Analogy:** "Just human use grammatical rule to communicate similarly computers also need certain rule."
    * (Jaise insaan baat karne ke liye grammar ke rules use karte hain, waise hi computers ko bhi baat karne ke liye rules chahiye hote hain).
* **Definition:** In rules ko **Protocols** kehte hain.
* **Usage:** Hum task ke hisaab se alag-alag protocols use karte hain.
    * **Example 1:** Web ke liye -> **HTTP** Protocol use karte hain.
    * **Example 2:** File transfer ke liye -> **FTP** Protocol use karte hain.

**Video -> 191, 192, 193 -> Some Commonly Used Protocols:**
* TCP
* UDP
* HTTP

---

### 📄 Page 26: WebSockets & Proxies (Start)

**Video -> 194 -> Protocols WebSocket:**
* **Comparison:**
    * **HTTP:** Isme communication **One Directional** hota hai. (Client request karta hai, Server bhejta hai).
    * **WebSocket:** Isme communication **Bidirectional** hota hai.
* **Meaning:** "This means BOTH Client and Server can send data to each other at any time." (Client aur Server kabhi bhi ek dusre ko data bhej sakte hain).
* **Example:** Live chat apps.
* **Function:** WebSocket push serves to send message to client. (Server bina pooche client ko message push kar sakta hai).


**Video -> 195 -> Forward Proxy & Reverse Proxy:**
* **Analogy:** "Forward Proxy -> Goes near personal assistant." (Forward proxy aapke personal assistant jaisa hai).

---

### 📄 Page 27: Deep Dive into Proxies

**Analogy Continued (Personal Assistant):**
* **Forward Proxy:**
    * **Example:** "If you want vegetable you say to your personal assistant." (Agar aapko sabzi chahiye, aap apne assistant ko bolte ho).
    * **Note:** "This is Forward Proxy."
    * **Internet Context:** "In the same way in Internet: Users want something from Internet. It say to Forward Proxy." (Users internet se kuch maangte hain toh wo pehle Forward Proxy ke paas jata hai).

* **Reverse Proxy:**
    * **Analogy:** "A personal assistant for your **family**." (Ye aapki family/server ka assistant hai).
    * **Example:** "Outside world want to connect to your family. So, it will go to your assistant first and then it will send the appropriate calls." (Bahar wale pehle assistant se milenge, fir wo decide karega ki family mein kis se milana hai).

**Important Question Raised in Notes:**
* "But why it is done users can also directly ask from server then why forward proxy what problem it solves."
* (Notes mein ye sawaal likha hai: Aakhir hum aisa karte kyun hain? Users direct server se kyun nahi maang lete? Forward proxy kya problem solve karta hai?)


---

### 💡 Quick Application for your "Smart PG System":

1.  **DNS:** Aapka domain `smartpg.com` (example) purchase karna padega jo aapke server IP se map hoga.
2.  **WebSocket (Bahut Important):**
    * Jab Tenant ticket raise kare "Water issue", toh Owner ke app par **turant notification** aana chahiye.
    * Iske liye **WebSocket** use hoga (Real-time communication), kyunki normal HTTP mein owner ko baar-baar refresh karna padega check karne ke liye.
3.  **Reverse Proxy (Nginx):**
    * Aapke backend servers (Microservices) ke aage hum ek **Reverse Proxy** lagayenge.
    * **Fayda:** Ye security badhayega. Hackers direct aapke main database wale server tak nahi pahunch payenge, wo pehle Proxy se takrayenge.


=============================================================


### 📄 Page 28: Reverse Proxy (Diagram) & API Introduction

**Header:**
* **Section -> 13 -> Communication Buzzwords:**

**Reverse Proxy (Diagram Explanation):**
* Diagram mein dikhaya gaya hai ki **Reverse Proxy in Internet** kaise kaam karta hai.
* **Flow:**
    1.  Multiple Users request bhejte hain.
    2.  Request pehle **Reverse Proxy Server** ke paas jati hai.
    3.  Reverse Proxy us request ko sahi jagah bhejta hai:
        * Ya toh **Authentication Server** ke paas (Login check karne ke liye).
        * Ya toh **Content Server** ke paas (Data lene ke liye).

**Video -> 196 -> Introduction (APIs):**
* **Analogy:** "As we people communicate... similarly computers also communicate."
    * (Jaise insaan aapas mein baat karte hain signs ya shabdon ka use karke, waise hi computers bhi aapas mein baat karte hain).
* **Mechanism:** Computers baat karne ke liye **APIs** ka use karte hain.
* **Types:** Is course mein hum 3 tarah ke communication styles dekhenge:
    1.  **REST**
    2.  **GraphQL**
    3.  **gRPC**

---

### 📄 Page 29: GraphQL vs REST

**Video -> 197 -> GraphQL:**
* **Comparison:**
    * **REST:** Unlike REST framework, Jahan humare paas **Predefined Options** hote hain (Jo server dega wahi lena padega).
    * **REST Limitation:** "In REST you have to place separate request for each order." (Agar alag-alag data chahiye, toh alag-alag requests bhejni padti hain).
* **GraphQL Benefit:**
    * "In GraphQL you can customize." (Aap customize kar sakte ho).
    * "Ask for what you need in a **Single Query**." (Jo chahiye bas wahi maango, ek hi baar mein).

**Example (Blog Scenario):**
* Imagine karo aapko ek **Blog** chahiye, saath mein uske **Related Posts** chahiye, aur un posts ke **Authors** ki info chahiye (aur last 15 days ke comments bhi).
* **REST mein:** Aapko 3-4 alag requests bhejni padengi.
* **GraphQL mein:** "If you are asking for multiple pieces of info in one go." (Aap ek request mein ye sab maang sakte ho).

**When to use:**
* Jab aapko relationships (data ke beech ka rishta) handle karna ho.
* **Note:** "Graph Databases specializes in storing the relationship between data."

---

### 📄 Page 30: REST Verbs & gRPC Intro

**REST API Methods (Left Side):**
* Notes mein REST ke standard actions likhe hain:
    * **HTTP GET:** Data lene ke liye.
    * **HTTP POST:** Naya data create karne ke liye.
    * **PATCH:** Data update karne ke liye.
    * **DELETE:** Data delete karne ke liye.

**Video -> 198 -> gRPC:**
* **The Big Question:** Notes mein ek sawal uthaya gaya hai—
    * "Explain what it is, when to use it, why to use it."
    * "If we have REST API and GraphQL already then why to use this (gRPC)?"
    * (Agar humare paas already REST aur GraphQL hain jo acha kaam kar rahe hain, toh humein gRPC ki zarurat kyun hai?)

* **Focus:** "What real world problem is solved by gRPC."
* (Iska jawab aage ke lectures mein hoga, lekin mainly ye **Performance** aur **Internal Microservices Communication** ke liye hota hai).

---

### 🚀 Application for your "Smart PG System":

In teeno (REST, GraphQL, gRPC) ka use aapke project mein kaise hoga, simple language mein:

1.  **REST (Sabse Common):**
    * Aapke zyadatar features ke liye use hoga.
    * *Example:* `POST /api/login` (Login karne ke liye), `GET /api/rooms` (Rooms ki list lene ke liye). Ye simple aur standard hai.

2.  **GraphQL (Complex Data ke liye):**
    * Owner ke **Dashboard** ke liye best hai.
    * *Scenario:* Owner ek hi screen par dekhna chahta hai: "Total Rent Collected" + "Empty Rooms List" + "Pending Complaints".
    * REST mein iske liye 3 API calls lagengi. GraphQL mein 1 call mein sara data aa jayega. Mobile app fast chalega.

3.  **gRPC (Speed ke liye):**
    * Ye servers ki aapsi baat cheet ke liye hai.
    * *Scenario:* Jab "Booking Service" ko "Payment Service" se baat karni ho, toh wo gRPC use karenge kyunki ye **Lightning Fast** hota hai. User ko wait nahi karna padega.


=============================================================



### 📄 Page 31: Introduction to Data Storage

**Header:**
* **Section -> 14 -> Database & Storage Buzzwords:**

**Video -> 201 -> Introduction:**
* Is section mein hum samjhenge:
    1.  Relational / SQL Database.
    2.  Non-Relational / NoSQL Database.
    3.  Object Storage.
    4.  Database Sharding (Todna).
    5.  Database Replication (Copy banana).
    6.  Caching.
    7.  CDN.
* **Goal:** "We will understand... how to choose between SQL & NoSQL database." (Hum samjhenge ki kab SQL use karna hai aur kab NoSQL).

---

### 📄 Page 32: SQL (Relational) Databases

**Video -> 202 -> Relational Database / SQL Database:**
* **Definition:** Ye data ko **Table-like format** mein store karta hai.
* **Structure:** Isme **Rows and Columns** hoti hain.
* **Requirement:** "Means the data that fit into **Predefined Fields**." (Data ka format pehle se fix hona chahiye).
* **Examples:** MySQL, PostgreSQL.
* **Key Question:** Difference between the two, and when to use what? (Ye hum aage compare karenge).

---

### 📄 Page 33: NoSQL (Non-Relational) Databases

**Video -> 203 -> Non-Relational Database:**
* **Problem:** "What happen when our data doesn't fit in predefined categories or data is **Unstructured**?" (Jab data ka koi fix format na ho toh kya karein?)
* **Example (Social Media Post):**
    * Kuch posts mein sirf text hota hai, kuch mein photos, kuch mein location.
    * Agar hum ise Table (SQL) mein daalenge, toh "Few rows will be empty."
    * "Means that is a **Wastage of Storage**." (Kyunki khali dabbo ke liye bhi jagah reserve ho jati hai).

* **Solution:** NoSQL Database.
* **Method:** Example -> Saving it in **JSON format** (JSON Document).
* **Examples:** MongoDB, DynamoDB.
* **Benefit:** "Perfect for handling **Unstructured** and varying data." (Ye data storage aur management ko customize kar deta hai).

---

### 📄 Page 34: SQL vs NoSQL (Comparison Part 1)

**Video -> 204 -> SQL vs NoSQL:**
* **Decision Framework:** "How do we choose between this two?" (Hum decide kaise karein?)

**1. Speed:**
* "When you need **Fast Data Access**, NoSQL database is preferred." (Speed ke maamle mein NoSQL behtar hai).

**2. Scale (Scaling):**
* **SQL:** Mostly Vertical Scaling (Powerful server chahiye).
* **NoSQL:** "When the Scale is too large -> NoSQL is preferred." (Kyunki ye Horizontal Scaling/Sharding support karta hai).

**3. Structure:**
* **SQL:** Fixed Structure (Rigid).
* **NoSQL:** Flexible Structure -> "But if your data fit into a fixed structure -> SQL Database."

---

### 📄 Page 35: SQL vs NoSQL (Comparison Part 2)

**4. Complexity of Queries:**
* **SQL:** "Complex Queries -> SQL Databases." (Agar aapko data join karna hai, complex calculations karni hain, toh SQL best hai).
* **NoSQL:** "If the query is simple -> NoSQL databases." (Simple data fetch karne ke liye).

**5. Data Changes:**
* "If your data changes frequently -> NoSQL database."
* **Example:** "Rapidly evolving applications."
    * (Agar aap startup bana rahe hain aur har hafte naye features/fields add kar rahe hain jaise 'Likes', 'Reactions', 'Share count', toh NoSQL behtar hai kyunki usme schema badalna aasan hai).

---

### 📄 Page 36: Object Storage

**Video -> 205 -> Object Storage:**
* **Definition:** "Object storage is perfect for handling **Large amounts of data**."
* **Concept:** Data = Object.
* **Use Case:** "For object storage we store data as object."
* **Real World Use:** Storing frequently used data like **Images, Videos** specifically.
* **Example:** AWS S3 bucket.

---

### 📄 Page 37: Cache Limitations

**Video -> 207 -> Cache (Review):**
* Note: "Already done in above topic." (Humne pehle padh liya hai).
* **Important Note on Side:**
    * "Cache has **Limited Capacity** compared to database." (Cache database jitna bada nahi ho sakta, wo mehenga hota hai RAM ki wajah se).
    * **Concepts:**
        * **Cache Hit:** Data cache mein mil gaya.
        * **Cache Miss:** Data cache mein nahi mila (Database ke paas jana padega).
* **Warning:** "What is that limitation?" -> Size and Cost.

---

### 💡 Blueprint for your "Smart PG System" (Hybrid Approach):

Aapko **Smart PG System** (OYO type model) ke liye **Hybrid Database** structure use karna chahiye. Ye raha breakdown:

1.  **SQL (PostgreSQL/MySQL):**
    * **Kahan use karein:** User Accounts (Tenant/Owner details), Booking Records, Payment Transactions.
    * *Why:* Kyunki ye data structured hai aur payment mein galti nahi honi chahiye (Strict consistency chahiye).

2.  **NoSQL (MongoDB):**
    * **Kahan use karein:** Tenant Complaints/Tickets, Chat System, Reviews/Ratings.
    * *Why:* Kyunki complaint ka data fix nahi hota (kabhi photo hogi, kabhi lamba text), aur ye data rapidly change ho sakta hai.

3.  **Object Storage (AWS S3):**
    * **Kahan use karein:** Rooms ki Photos, KYC Documents (Aadhar Card images), Lease Agreements (PDF).
    * *Why:* Database mein images store karna system ko slow kar dega. Images S3 mein rakho aur unka Link database mein rakho.

4.  **Cache (Redis):**
    * **Kahan use karein:** Available Rooms ki list dikhane ke liye.
    * *Why:* Log baar-baar search karenge "PG in [Location]". Ye data database se baar-baar maangne ki bajaye Cache mein rakho taaki loading super fast ho.



=============================================================



### 📄 Page 38: Introduction & Cache Aside Strategy

**Header:**
* **Section -> 15 -> Appendix -> Caching Deep Dive:**

**Video -> 208 -> Read Caching Strategies:**
* **Definition:** "Caching is a technique that is used to **Speed Up** the data retrieval."
* (Caching ek technique hai jo data lane ki speed badhane ke liye use hoti hai).
* **Method:** Hum frequently accessed data (jo baar-baar chahiye) ko ek **Fast Access Cache** mein store karte hain taaki slow database ke paas na jana pade.

**Strategy 1: Cache Aside Strategy:**
* **Process:**
    1.  Server sabse pehle **Cache** mein check karta hai.
    2.  Agar data mil gaya -> Return kar do.
    3.  Agar nahi mila -> To **Database** mein jao.
    4.  Wahan se data lo, phir **Cache ko Update karo**, aur finally user ko return karo.
* (Isme server khud zimmedari leta hai data lane aur cache update karne ki).

---

### 📄 Page 39: Read Through Strategy

**Strategy 2: Read Through Strategy:**
* **Concept:** "Cache itself will first check if the data is available."
* (Isme Cache khud responsible hota hai).
* **Process:**
    1.  Server Cache se data mangta hai.
    2.  Cache check karta hai apne paas.
    3.  Agar nahi mila, toh **Cache khud Database se fetch karta hai**.
    4.  Future requests ke liye save karta hai aur return karta hai.
* (Yahan server ko database se baat karne ki zarurat nahi padti, wo sirf cache ko janta hai).

**Crucial Question:**
* "Which is better between the two and which to use when?"
* (Cache Aside vs Read Through: Konsa behtar hai aur kab use karein? Iska jawab pros/cons mein milega).

---

### 📄 Page 40: Write Strategies & Cache Pros

**Video -> 209 -> Write Caching Strategies:**
* Ab tak humne padha data *padhte* (Read) waqt kya karna hai. Ab dekhenge data *likhte* (Write/Save) waqt kya karna hai.
* **Types:**
    1.  **Write Around** (Lazy Caching).
    2.  **Write Through** Strategy.
    3.  **Write Behind** Strategy.

**Video -> 210 -> Read Cache (Pros and Cons):**
* **Focus:** Cache Aside Strategy ke fayde (Pros).
    1.  **Fault Tolerance:** "Increase fault tolerance."
        * (Agar Cache fail bhi ho jaye, toh system nahi rukega, server seedha database se data le aayega).
    2.  **Flexible Schema:** "Flexible Data Models."
        * (Aap alag-alag tarah ka data aasani se cache kar sakte ho).

---

### 📄 Page 41: Read Through Cons & Cache Invalidation

**Read Through Strategy (Pros & Cons):**
* **Cons (Nuksan):**
    * **System Failure:** "Cache failure -> System failure."
    * (Kyunki Server sirf Cache par dependent hai, agar Cache crash hua toh pura system down ho jayega. Ye **Less Reliable** hai).

**Video -> 211 -> Write Cache Strategy (Details):**
* **Instructions:** Explain all above properly step by step with pros & cons.
* Explain Write Through, Write Around, Write Behind.

**Buzzword -> Cache Invalidation:**
* Notes mein ek bahut important term likha hai: **Cache Invalidation**.
* **Meaning:** Jab database mein data change ho jaye (e.g., Rent badh gaya), toh purana data Cache se hatana padta hai taaki user ko galat purana price na dikhe.

---

### 🚀 Applying Caching to your "Smart PG System":

In strategies ka use aapke project mein kaise hoga:

1.  **Read Strategy (Use "Cache Aside"):**
    * **Scenario:** "PG Rooms List" dikhane ke liye.
    * **Why:** Agar Redis (Cache) down bhi ho jaye, toh bhi Tenants app chala payenge (Direct Database se slow load hoga, par chalega). **Fault Tolerance** zaruri hai.

2.  **Write Strategy (Use "Write Around"):**
    * **Scenario:** Chat Messages ya Logs save karne ke liye.
    * **Why:** Har chat message ko turant Cache mein daalne ki zarurat nahi hai. Pehle DB mein save karo, jab user wapas chat open karega, tab cache mein layenge (Lazy Loading).

3.  **Cache Invalidation (Bahut Zaruri):**
    * **Scenario:** Jab Owner kisi room ka status "Available" se "Occupied" kare.
    * **Action:** Us waqt turant Cache se wo room delete karna padega, warna dusra user usse book kar lega (Double Booking Issue).


**Iske saath aapke System Design ke "Core Concepts" aur "Buzzwords" complete ho gaye hain!**


=============================================================



### 📄 Page 42: Cloud Computing & Logging Introduction

**Header:**
* **Section -> 16 -> Appendix -> Extra Buzzwords:**

**Video -> 212 -> Cloud Computing:**
* **Sawaal:** What is Cloud Computing all about? (Aakhir ye hai kya?)
* **Definition:** "Instead of buying and maintaining the server yourself you rent them from famous company."
* (Khud ka server khareedne aur uski dekh-rekh karne ki bajaye, aap Amazon (AWS) ya Google (GCP) jaisi badi companies se server **Rent (Kiraye)** par lete hain).
* **Benefit:** Aapko hardware ki tension nahi leni padti, bas code par focus karna hota hai.

**Video -> 213 -> Logging & Monitoring:**
* **Concept 1: Logging:**
    * **Analogy:** "Logging is like computer writing in a **Diary**."
    * (Logging bilkul waise hi hai jaise computer apni diary likh raha ho).
    * **Function:** "Server also logs all of its **Key Activities**." (Server apne har important kaam ka record rakhta hai).

---

### 📄 Page 43: Logging Details & Monitoring

**Logging (Continued):**
* **Diary mein kya likha hota hai?**
    1.  **What Request:** Kaunsi request execute ho rahi hai (e.g., Login request).
    2.  **How it is executing:** Process sahi se hua ya nahi.
    3.  **Responsibility back to client:** Client ko kya jawab diya.
    4.  **Any Error:** Kya koi error aayi?
* **Best Analogy:** "You can think of logs as **Footprints** left behind if something goes wrong."
    * (Logs wo pairon ke nishan hain jo tab kaam aate hain jab koi musibat aati hai, taaki hum trace kar sakein ki galti kahan hui).

**Concept 2: Monitoring:**
* **Analogy:** "Monitoring is just like having **Security Camera** that is watching our servers daily."
    * (Monitoring ek CCTV camera ki tarah hai jo 24/7 server par nazar rakhta hai).
* **Function:**
    * "If something goes wrong, **Alerts** are triggered."
    * (Agar kuch gadbad hoti hai, jaise server crash hona ya slow hona, toh ye turant alarm baja deta hai).

**Instruction in Notes:**
* "Explain between difference this above two, when to use what." (In dono mein fark kya hai aur kab kya use karein?)

---

### 💡 Difference & Usage (Explained for Smart PG System):

In notes ke basis par, Logging aur Monitoring mein fark samajhna zaruri hai:

| Feature | **Logging (Diary)** 📝 | **Monitoring (CCTV)** 📹 |
| :--- | :--- | :--- |
| **Kya hai?** | Past ka record (Jo ho chuka hai). | Present ki health (Jo abhi chal raha hai). |
| **Example** | "Tenant A ne 2:00 PM par payment kiya par fail ho gaya." | "Payment Server par abhi load 90% hai, crash hone wala hai!" |
| **Analogy** | **Post-mortem:** Marne ke baad check karna ki kyun mara. | **Pulse Rate:** Check karna ki insaan zinda hai ya nahi. |
| **Action** | Jab koi bug aaye, tab hum **Logs** padhte hain. | Jab server down ho, tab **Monitoring** humein SMS/Email bhejta hai. |

### 🚀 Quick Application for your Project:

1.  **Cloud:** Aap apna PG System **AWS (Amazon Web Services)** par host karenge (Step 1).
2.  **Logging:**
    * Agar kisi Tenant ka rent pay nahi hua, toh aap **Logs** check karenge ki *Payment Gateway ne kya error diya tha*.
3.  **Monitoring:**
    * Aap alerts set karenge. Agar raat ke 2 baje server band ho gaya, toh Monitoring system Owner ko **SMS bhej dega** taaki wo turant thik kar sake.



=============================================================

Ye rahe aapke **System Design Masterclass (Section 17 -> Common FAQs & Buzzwords)** ke notes. Maine inhein logical flow mein **Hinglish** mein convert kiya hai.


---

### 📄 Page 44: Database Indexing (Concept)

**Header:**
* **Section -> 17 -> Common FAQs:**

**Video -> 216 -> Database Indexing:**
* **Sawaal:** What is database indexing? Why use it? When to use it?
* **Analogy (Book Example):**
    * "What is database indexing -> Very similar to **Index page in a book**."
    * (Ye bilkul kitab ke shuru mein diye gaye Index page jaisa hai).
    * **Benefit:** "It help you jump directly to the page you need."
    * (Agar index na ho, toh aapko puri kitab chhan-ni padegi. Index ho, toh aap seedha us page par pahunch jate ho).
* **Technical Application:** Database mein bhi hum yahi concept use karte hain data jaldi dhundne ke liye.

**Questions raised in notes:**
* Does the DB automatically add indexes? (Kya DB khud add karta hai?)
* How do we create indexes? (Hum kaise banate hain?)

---

### 📄 Page 45: Creating Indexes & Benefits

**How Indexing Works:**
* "DB Indexing help in locating **Specific Rows** instead of scanning every record."
* (Bina index ke database ko har row check karni padti hai, ise "Full Table Scan" kehte hain. Index ke saath wo seedha sahi row par jata hai).

**Structure:**
* Indexes **Pointers** ki tarah store hote hain. Ye "Sorted Searches" ko optimize karte hain.

**Creating an Index (Syntax):**
* **Query Patterns:** `CREATE INDEX index_name ON Users(Username)`
* (Agar aap users ko "Username" se search karte hain, toh us column par index bana dijiye).

**Automatic vs Manual:**
* **Primary Key:** "Most DB automatically create an index on **Primary Key** column." (ID column par index khud ban jata hai).
* **Manual Indexing:** "We have the option to add indexes manually based on query patterns." (Jin columns par aap `WHERE` clause lagate hain, wahan manual index banta hai).


---

### 📄 Page 46: Capacity Estimation & Indexing Downsides

**Video -> 217 -> Why should you do Capacity Estimation?:**
* **Reason 1: Determine Resources:** "To determine numbers of servers and databases."
* **Reason 2: Cost Management:**
    * **Example:** Agar aapka server 1 million requests/hour handle kar sakta hai, aur ab requirement 10 million requests/hour ki hai.
    * "Now you need 10 million requests/hour." -> Aapko pehle se pata hona chahiye taaki aap budget plan kar sako.

**Downside of Indexing (Nuksan):**
* Indexing free nahi hai, iske kuch nuksan bhi hain:
    1.  **Storage Overhead:** Index alag se jagah leta hai storage mein.
    2.  **Write Performance:** "Write performance" slow ho jati hai.
    * **Kyun?** Jab bhi aap naya data insert karte ho, database ko Table update karne ke saath-saath Index bhi update karna padta hai.

---

### 📄 Page 47: Read/Write Heavy & Apache Kafka

**System Type Determination:**
* Capacity estimation humein ye batata hai ki humara system kaisa hai:
    * **Read Heavy System:** (Log data padhte zyada hain, likhte kam hain). Example: Instagram/Twitter Feed. -> Iske liye **PostgreSQL with Indexing** best hai.
    * **Write Heavy System:** (Data bahut tezi se likha ja raha hai). Example: IoT Sensors, Logs. -> Iske liye **Cassandra/HBase** best hai.

**Video -> 218 -> Apache Kafka (Event Streaming):**
* **Topic:** Event Streaming Platform.
* **Questions:** What is Kafka? When to use it? Is it Open Source?
* **Definition:** Kafka ek tool hai jo **Real-time Data Feeds** (Events) ko handle karta hai.
* (Example: Uber mein jab driver location update karta hai, wo Kafka ke through real-time mein user tak pahunchta hai).


---

### 📄 Page 48: GraphQL vs REST (Problem Solving)

**Video -> 219 -> Beginner Guide to GraphQL:**
* **Questions:** What real problem does it solve? What was the problem with REST?

**The Problem with REST:**
1.  **Multiple Round Trips:** Ek page ka data lane ke liye baar-baar server ke paas jana padta hai.
2.  **Over Fetching:** Zarurat se zyada data aa jana (Mobile data waste hota hai).
3.  **Under Fetching:** Zarurat se kam data aana (phir se request bhejni padti hai).

**GraphQL Solution:**
* "GraphQL solve the problem of Over fetching and under fetching."
* Ye clients ko power deta hai ki wo server se **Exactly** wahi maange jo unhein chahiye.

---

### 📄 Page 49: GraphQL Processing & Consistent Hashing

**GraphQL Processing Steps:**
* Parsing -> Validation -> Execution -> Response Formatting.
* (Notes mein likha hai ki iska example Express JS ke saath samjhana hai).

**Video -> 220 -> Consistent Hashing:**
* **Topic:** Consistent Hashing.
* **Questions:** What it is? Why it is used?
* **Usage:** Ye Distributed Systems (Database Sharding) mein use hota hai taaki jab hum naya server add karein ya purana remove karein, toh pura data hilaana na pade. (Load Balancing ko efficient banata hai).

---

### 🚀 Application for your "Smart PG System":

In concepts ko apne Project mein kaise apply karein:

1.  **Indexing (Bahut Important):**
    * Apne Database mein `City`, `Area`, aur `Price` columns par **Index** zaroor lagana.
    * **Kyun?** Kyunki Users search karenge: *"Show PGs in Delhi under 5000"*. Index ke bina ye search bahut slow hogi jab users badh jayenge.

2.  **Capacity Estimation:**
    * Calculate kariye: Agar 100 PG hain aur har PG mein 10 photos hain. Total 1000 photos.
    * Agar 1 photo 2MB ki hai = 2GB Storage chahiye (S3 Bucket estimate).

3.  **Kafka:**
    * Abhi ke liye **Skip** kar sakte hain (Startups ke liye complex hai).
    * Future mein jab millions users honge tab Real-time Notifications ke liye use hoga.

4.  **GraphQL:**
    * **Tenant App** ke liye REST thik hai.
    * **Admin/Owner Dashboard** ke liye GraphQL use karein, kyunki wahan ek screen par bahut sara mixed data dikhana hota hai (Revenue + Complaints + Occupancy).



=============================================================


Ye rahe aapke **System Design Masterclass (Section 2 -> Design Instagram Newsfeed)** ke detailed notes. Maine inhein logical sequence mein arrange kiya hai taaki aap samajh sakein ki ek real-world system (jaise Instagram ya aapka PG System) scratch se kaise design hota hai.


### 📄 Page 4: Functional Requirements

**Header:**
* **Section -> 2 -> Design Instagram Newsfeed:** (Hum Instagram ka example le rahe hain).

**Video -> 4 -> Deciding Requirements (Functional):**
* **Goal:** Humein sabse pehle ye decide karna hai ki system **karega kya** (Functional Requirements).
* **Core Features:**
    1.  **Newsfeed:** User ko posts dikhni chahiye.
    2.  **Follow/Unfollow:** Users ek dusre ko follow kar sakein.
    3.  **Create Post:** User naya content daal sake.
        * Content types: Text, Image, Video.
    4.  **Like & Comment:** Engagement ke liye features.

---

### 📄 Page 5: Non-Functional Requirements

**Video -> 5 -> Non-Functional Requirements:**
* **Goal:** Humein ye decide karna hai ki system **kaise perform karega**.
* **Note:** "It talks about... Availability, Scalability, Consistency, Latency, Extensibility & Usability."
* **Translation:**
    * System hamesha chalu rehna chahiye (Availability).
    * Load badhne par crash nahi hona chahiye (Scalability).
    * Jaldi load hona chahiye (Low Latency).

---

### 📄 Page 6: Capacity Estimation Basics

**Video -> 6 -> Capacity Estimation:**
* **Definition:** "Calculate how much hardware/resources we need."
* **Key Metrics (Napne ke tarike):**
    1.  **DAU / MAU:** Daily Active Users / Monthly Active Users.
        * (Rozana kitne log app kholte hain).
    2.  **Throughput:** Amount of data handled in one second.
    3.  **Storage:** Data store karne ki jagah.
    4.  **Memory (RAM):** Fast access ke liye.
    5.  **Network:** Bandwidth speed.

---

### 📄 Page 7: Why Capacity Estimation?

**Video -> 7 -> Capacity Estimation (Why?):**
* **Sawaal:** Why should you do Capacity Estimation? (Hum ye ganit kyun lagayein?)
* **Reasons:**
    1.  **Determine Hardware:** "To determine numbers of servers and databases." (Kitne computer khareedne padenge).
    2.  **Cost Management:** "Decide type and specification of all hardware."
        * (Agar pehle se pata ho ki load kam hoga, toh sasta server lenge. Paise bachenge).
    3.  **Real Life Problem:** "Explain by real life example... If our system is read heavy or write heavy."

---

### 📄 Page 8: DB Selection (Read vs Write Heavy)

**Video -> 8 -> Capacity Estimation (DB Strategy):**
* **Concept:** System do tarah ke hote hain:
    1.  **Read Heavy:** Log data padhte zyada hain, likhte kam hain. (Example: Instagram, PG App - log room dekhte zyada hain, book kam karte hain).
    2.  **Write Heavy:** Data likha zyada ja raha hai. (Example: IoT Sensors logs).

* **Decision Tree (Diagram):**
    * **Read Heavy:** Use **PostgreSQL** (SQL Database) -> saath mein **Indexing** use karo speed ke liye.
    * **Write Heavy:** Use **Cassandra** or **HBase** (NoSQL/Wide-column store).

---

### 📄 Page 9: Calculating Throughput

**Video -> 9 -> Capacity Estimation (Throughput):**
* **Definition:** "Throughput -> Amount of data handled by a system in one second."
* **Types:**
    * **Write Throughput:** Kitne log post create kar rahe hain.
    * **Read Throughput:** Kitne log feed scroll kar rahe hain.

* **Example Calculation (Instagram):**
    * **Scenario:** Creating a Post.
    * "So, if Total API requests daily = 100 Million."
    * Formula: `100,000,000 / 86400 (seconds in a day)`
    * **Result:** Approx **1150 requests per second**.
    * (Iska matlab humara server aisa hona chahiye jo har second 1150 posts save kar sake).

---

### 📄 Page 10: Advanced Throughput Calculation

**Video -> 10 -> Calculate Throughput (Continued):**
* **Scenario:** "Calculate write requests for following." (Follow karne ki requests calculate karo).
* **Assumption:** "Each user follows 1 new user per week."
* **Math:**
    * Total Requests in one day = `(500 Million Users / 7 days)`.
    * Is number ko seconds mein convert karke throughput nikalenge.
* **Note:** "Similarly correct throughput for Like and Comment." (Aise hi Likes aur Comments ka bhi load calculate karo).

---

### 📄 Page 11: Storage Estimation

**Video -> 11 -> Capacity Estimation -> Storage:**
* **Process:** "First question: What are we trying to store?"
    * **Answer:** Example -> **Posts**.
* **Factors:** Storage calculate karne ke liye do cheezein chahiye:
    1.  **Number of posts** for a day.
    2.  **Size** (Average size of one post).

---

### 📄 Page 12: Detailed Storage Math

**Video -> 12 -> Query Solutions (Calculate Storage):**
* **Example Breakdown:**
    * Maan lijiye 3 tarah ki posts hain:
        1.  **Video Posts:** 20MB size (20% users ye karte hain).
        2.  **Image Posts:** 0.5MB size (60% users ye karte hain).
        3.  **Text Posts:** 100KB size (20% users ye karte hain).

* **Calculation (Text example):**
    * "Based on above assumptions and 1 million posts..."
    * Storage = `0.2 (20%) * 1 Million * 100 KB`.
    * Isse total storage nikal aayegi.
    * **Instruction:** "We can calculate the storage." (Is tarah humein pata chalega ki hard disk kitni badi chahiye).

---

### 📄 Page 13: Memory (Cache) & Network

**Video -> 13 -> Capacity Estimation (Memory/Cache):**
* **Rule of Thumb:** "By memory we mean **Cache Memory**."
* **Formula:** "Amount of Cache required everyday = Example -> **1% of daily Total Storage**."
* (Jitna data hard disk mein save ho raha hai, uska 1% RAM (Cache) mein rakho fast speed ke liye).

**Video -> 14 -> Capacity Estimation (Network/Bandwidth):**
* **Definition:** "It tells us how much data flows Into and Out of our system per second."
* **Terms:**
    * **Ingress:** Data coming INTO our system (Uploads).
    * **Egress:** Data going OUT of our system (Downloads/Viewing).
* **Why:** Taaki hum internet connection ki speed (Bandwidth) sahi khareed sakein.

---

### 📄 Page 14: API Design Introduction

**Video -> 15 -> API Design:**
* **Task:** "Create a Text Post."
* **REST API Structure:**
    * **Endpoint:** `/v1/posts` (URL kya hoga).
    * **HTTP Method:** `POST` (Kyunki hum naya data bana rahe hain).
    * **HTTP Body:** (Data jo server ko bhejna hai - Text content).

* **Important Question in Red:**
    * "Why to version the API (v1)?" (API ke aage v1 kyun lagaya?)
    * **Reason:** "What real life problem it solves."
    * (Answer: Agar future mein app update karna pade, toh purane users ka app band na ho. Wo v1 use karte rahenge, naye users v2 use karenge).


---

### 🚀 Blueprint for your "Smart PG System":

Ye ganit (Math) aapke project ke liye kaise kaam aayega:

1.  **Read Heavy System:**
    * Aapka **Smart PG System** definitely **Read Heavy** hai.
    * Tenants din mein 10 baar app khol kar check karenge (Menu, Events, Bills), lekin Rent mahine mein 1 baar pay karenge (Write).
    * **Decision:** Isliye **PostgreSQL** best database hai aapke liye.

2.  **Storage Estimation (Smart PG):**
    * *Assumption:* 100 PGs. Har PG ke pass 5 Rooms. Har Room ki 3 Photos.
    * Total Photos = 100 * 5 * 3 = 1500 Photos.
    * Average Size = 2 MB per photo.
    * **Total Storage Needed:** 3000 MB (3GB).
    * **Result:** Aap shuruwat mein AWS S3 ki free tier use kar sakte hain, dedicated server ki zarurat nahi hai.

3.  **API Design:**
    * Jab aap "Ticket Raise" feature banayenge:
    * `POST /v1/tickets`
    * Body: `{ "type": "Plumbing", "desc": "Tap leaking", "room_id": "101" }`

Ye rahe aapke **System Design Masterclass (Section -> Deep Dive Insights)** ke notes. Maine inhein logical sequence mein **Hinglish** mein convert kiya hai.

Ye section aapke **Smart PG System** ke "Technical Implementation" ke liye sabse critical hai, khaaskar jab aap Images aur Videos handle karenge.

---

### 📄 Page 50: SQL vs NoSQL (The Final Decision Checklist)

**Header:**
* **Video -> 27 -> Deep Dive Insights Database Selections:**

**Factors Table (Kaun jeetega?):**
Yahan hum compare kar rahe hain ki kis situation mein **SQL** use karein aur kis mein **NoSQL**.

1.  **Fast Data Access:**
    * **Winner:** **NoSQL** (✅)
    * **SQL:** (❌)
    * *Reason:* NoSQL mein data Key-Value pair mein hota hai, toh dhundna bahut fast hota hai.

2.  **Scale is too Large:**
    * **Winner:** **NoSQL** (✅)
    * **SQL:** (❌)
    * *Reason:* Jab data petabytes mein ho (Big Data), toh NoSQL ko horizontally scale karna aasan hai (Servers add karte jao).

3.  **Data is in Fixed Structure:**
    * **Winner:** **SQL** (✅)
    * **NoSQL:** (❌)
    * *Reason:* Agar aapko pata hai ki har user ka Name, Email, aur Phone Number hi hoga (Fixed Columns), toh SQL best hai.

4.  **Complex Queries:**
    * **Winner:** **SQL** (✅)
    * **NoSQL:** (❌)
    * *Reason:* Agar aapko data JOIN karna hai (e.g., "Wo users dikhao jinhone pichle mahine rent nahi diya aur Delhi mein rehte hain"), toh SQL powerful hai.

5.  **Data Changes Frequently (Schema):**
    * **Winner:** **NoSQL** (✅)
    * **SQL:** (❌)
    * *Reason:* Agar aaj aapko `Height` store karni hai, kal `Weight`, aur parson `Color`, toh NoSQL bina error diye naye fields accept kar lega.

**Note:** "Explain all these with real life example..." (Niche dekhein application).

---

### 📄 Page 51: Data Modeling, Pre-signed URLs & Media Processing

**Header:**
* **Video -> 28 -> Deep Dive Insights Data Modeling:**

* **What it is:** Data Modeling ka matlab hai Database ka naksha (Map) banana. Kaunsi table kis se judi hai.
* **Why we need to know:**
    * Agar Data Model kharab hoga, toh query slow ho jayegi.
    * *Real Life Example:* Ek library mein agar kitabein random padi hon (Bad Modeling), toh dhundne mein ghanto lagenge. Agar Genre wise rakhi hon (Good Modeling), toh seconds lagenge.

**Header:**
* **Video -> 29 -> Deep Dive Insights Pre-signed URLs:** (Most Important for your PG App)

* **The Problem:**
    * Normal tareeke mein: User Image upload karta hai -> App Server ke paas -> Phir Server use S3 (Storage) mein dalta hai.
    * Isse App Server par load badh jata hai.
* **The Solution (Pre-signed URL):**
    * User App Server se ek "Permission Token" (Pre-signed URL) mangta hai.
    * Server wo URL deta hai.
    * User **Directly** image S3 bucket mein upload karta hai (Server ko bypass karke).
* **Real Life Analogy:**
    * Ye ek **Gate Pass** jaisa hai. Security guard (Server) aapko andar nahi le jata, wo bas pass deta hai, aap khud chale jate ho.

**Header:**
* **Video -> 30 -> Deep Dive Insights Media Processing:**

* **Scenario:**
    * Agar humare server par high-quality images/videos hain.
    * Lekin user ka internet slow hai ya device chota hai.
* **Concept:**
    * "Serve user different format of images based on user's internet and device."
* **How it works:**
    * Hum original image ko process karke alag-alag versions banate hain (Small, Medium, Large).
    * Agar User 4G/5G par hai -> **High Quality** dikhao.
    * Agar User 2G/3G par hai -> **Low Quality** (Compressed) dikhao taaki app fast chale.

---

### 🚀 Application for your "Smart PG System":

In "Deep Dive" concepts ko apne project mein kaise lagayein:

1.  **Database Selection (Hybrid Strategy):**
    * **SQL (PostgreSQL):** Use karein **Bookings, Payments, aur User Profiles** ke liye. (Kyunki yahan structure fixed hai aur galti ki gunjaish nahi hai).
    * **NoSQL (MongoDB):** Use karein **User Reviews aur Chat** ke liye. (Kyunki reviews lambe-chote ho sakte hain aur chat ka data fast access hona chahiye).

2.  **Data Modeling:**
    * Aapko Tables design karni hongi:
    * `Owner Table` <-> `PG Table` <-> `Room Table` <-> `Tenant Table`.
    * (Ek Owner ke multiple PGs, Ek PG mein multiple Rooms).

3.  **Pre-signed URLs (Action Item):**
    * Jab Owner "Room Photos" upload karega, toh aapka server busy nahi hona chahiye.
    * Owner ke phone se seedha AWS S3 par photo jayegi **Pre-signed URL** use karke. Isse aapka server fast rahega.

4.  **Media Processing:**
    * Owner 10MB ki photo upload karega (DSLR quality).
    * Lekin Tenant jab list scroll karega, toh usse 10MB ki photo load karne mein data waste nahi karna hai.
    * Aap **Cloudinary** ya **AWS Lambda** use karke photo ko automatically chota (thumbnail) bana denge display ke liye.


=============================================================



### **Page 1: Functional & Non-Functional Requirements**
*(Source: IMG_20251120_005929_1.jpg)*

**#Section 3 -> Design YouTube/Netflix**

**Video 31 -> Functional Requirements**
Yahan hum system ke functional requirements define kar rahe hain. Isme mainly **Two types of users** hote hain:

1.  **Viewers (Dekhne wale):**
    * **Streaming:** Device Compatibility honi chahiye. (Matlab user mobile, laptops, computers, etc., kisi par bhi stream kar sake).
    * **Search:** User kisi bhi video ko search kar sake.
2.  **Content Creators (Video dalne wale):**
    * **Upload Video:** Creator video upload kar sake.
    * **Notification:** Upload successful hone par unhe notification milna chahiye.

**Video 32 -> Non-functional Requirements**
Yeh quality aur performance se related requirements hain:

1.  **For Viewers:**
    * **Low Latency:** Video bina rukawat ke chalni chahiye (No buffering, no lagging). "More time wait" nahi hona chahiye.
2.  **For Content Creators:**
    * **Scalability:** System ko heavy traffic ya number of users handle karna aana chahiye.
    * **User Experience:** Video high quality mein honi chahiye (4k, 1080p etc.).

---

### **Page 2: Availability & Capacity Estimation (Part 1)**
*(Source: IMG_20251120_005931_1.jpg)*

1.  **Availability:** System hamesha available hona chahiye (Should be available 99.99% of time).
2.  **For Content Creators:**
    * Scalability
    * Security (Content secure rahe)
    * Storage Reliability (Data loss nahi hona chahiye)

**Video 33 (Marked as 32 in notes) -> Capacity Estimation (DAU/MAU)**
* Capacity estimate karne ke liye humein **DAU** (Daily Active Users) aur **MAU** (Monthly Active Users) ka pata hona chahiye.
* Hum kuch **Assumptions** lenge ki daily aur monthly kitne users active rahenge.

**Video 34 -> Throughput Estimation**
* **Write Throughput:** Kitna data write (upload) ho raha hai.
* **Read Throughput:** Kitna data read (view) ho raha hai.
* **Method:** Assumptions lo ki "How many read and write requests will be regularly" (kitni requests regular basis pe aayengi), us hisaab se calculate karo.

---

### **Page 3: Capacity Estimation (Storage & Memory)**
*(Source: IMG_20251120_005938_1.jpg)*

**Video 35 -> Capacity Estimation (Storage)**
* **Assumptions:**
    * Average video upload size = **600 MB**.
    * Total upload requests = **0.4 million** (4 lakh).
* **Calculation:** Isse humein pata chalega ki ek single day mein kitna data upload hoga. (So, you will get how much data will be uploaded in a single day).

**Video 36 -> Capacity Estimation (Memory/Cache)**
* **Cache Memory Size:** Humein decide karna hai ki cache ka size kya hoga.
* **Logic:** "Cache memory size per day".
* **Explanation:** Assumptions ka use karke explain karo ki cache memory estimation kaise calculate karte hain.

**Video 37 -> Capacity Estimation (Network Bandwidth)**
* Isme hum network ki bandwidth requirement estimate karenge.

---

### **Page 4: Bandwidth Concepts & API Design (Upload)**
*(Source: IMG_20251120_005941.jpg)*

**Network Bandwidth vs. Throughput:**
* **Network Bandwidth:** Yeh batata hai ki hamare system se **"How much data is flows in and out per second"** (kitna data har second aa raha hai ya ja raha hai).
* **Throughput:** Yeh batata hai ki **"How many requests flowed in and out of system per second"** (kitni requests har second process ho rahi hain).
* *Note:* In dono terms mein confuse nahi hona hai. Explain the steps to calculate network bandwidth.

**Video 38 -> API Design: Upload Content**
* **Problem:** Jo video client upload karega, wo 10 minutes se lekar 2 hours tak ki ho sakti hai. Agar video bahut badi hai, toh usey **one request** mein upload karna feasible nahi hai.
* **Solution:** Hum multiple requests use karenge taaki video data ko **small chunks** (chote tukdon) mein bheja ja sake.
* **Tech Stack:** Node.js aur Express.js mein yeh kaam **Form-data** ya **Multipart** ka use karke kiya jata hai. (How it is done in Node JS Express JS -> explain with code like form-data or multipart).

---

### **Page 5: Streaming Logic & Manifest File**
*(Source: IMG_20251120_005947.jpg)*

**Video 39 -> Stream Content**
* **Challenge:** Since video ka size bahut bada (too long) hota hai, "Complete video in one request" fetch karna hard hai.
* **Solution:** Isliye humein **multiple requests** karni padti hain for **multiple chunks of videos**.
* **Implementation:** Yeh Node.js aur Express.js mein kaise hota hai, woh samjhna zaroori hai.

**The YouTube Flow (Manifest File):**
* Jab client ko koi video dekhni hoti hai (watch a video), YouTube sabse pehle ek **Manifest File** bhejta hai.
* **Manifest File kya hai?** Yeh ek file hoti hai jisme video ke saare **chunks ki locations** hoti hain.
* **Client Logic:** Client iss manifest file ke base par server se video ke **different chunks** get karta hai, rather than fetching a "complete heavy video" at once.
* *Note:* "This is the initial request from client." (Yeh client ki taraf se pehli request hoti hai).

---

### **Page 6: HLS Protocol & HLD (Upload)**
*(Source: IMG_20251120_005949_1.jpg)*

**Note: HLS Protocol**
* **Question:** YouTube **HLS Protocol** use karta hai. Why not other protocols like FTP, HTTP, etc.?
* **HLS (HTTP Live Streaming):** Yeh ek **Adaptive Streaming** protocol hai.
* **Benefit:** Yeh video ki **quality adjust** kar sakta hai based on user's internet speed. (Agar net slow hai to quality low, fast hai to high).
* **Learning:** Yeh protocols kaise likhe jate hain, yeh samjhna chahiye.

**Video 40/60 -> High Level Design (HLD) of Upload Content**
* **Flow Explanation:** Client video upload karta hai -> Server respond karta hai ek **Session URL** ke saath.
* Explain everything: Client upload video, server respond with session URL.

---

### **Page 7: Upload Workflow & Message Queue**
*(Source: IMG_20251120_005955_1.jpg)*

**Video 41 -> HLD Upload Content (Continued)**
1.  **Session URL:** Client ko jab session URL mil jata hai.
2.  **PUT Request:** Ab client us session URL ke saath **API Gateway** par PUT request marta hai.
3.  **Service Routing:** API Gateway isey **Content Upload Service** ke paas bhejta hai.
4.  **Storage:** Service video ko **Object Storage** (jaise AWS S3) mein store karti hai.
5.  **Async Processing:** Video upload hone ke baad, Content Upload Service ek **Event** add karti hai **Message Queue** mein.

**Message Queue Kya Hai?**
* It is a queue where **tasks/events are added by one service** and then those events/tasks are **picked by another service**.
* Is process ko **Asynchronous Messaging** kehte hain.
* *Summary:* Content upload service adds an event to message queue.

---

### **Page 8: Processing & Content Workflow**
*(Source: IMG_20251120_005958_1.jpg)*

* **Video ID:** Us event mein **Video ID** hoti hai, kyunki Video ID hi video ko recognize karti hai.
* **YouTube's Complete Flow:**
    1.  Complete video ko **multiple chunks** mein break kiya jata hai.
    2.  Har chunk ko **different resolutions** aur **formats** mein convert kiya jata hai.
    3.  Finally, ise **CDN** (Content Delivery Network) par upload kiya jata hai.

**Video 42 -> High Level Design: Content Processor Workflow Engine**
* Is section mein hum **Content Processor Workflow Engine** ko samjhenge.
* **Questions to answer:**
    * What it is? (Yeh kya hai)
    * Why it is used? (Kyun use hota hai)
    * When to use it? (Kab use karein)
    * How to use it and all? (Kaise use karein)
    * If not use then? (Agar use na karein toh kya hoga)

---

### **Page 9: Chunking & Workflow Nodes**
*(Source: IMG_20251120_010004_1.jpg)*

**Content Processor Workflow Engine Diagram:**
(Notes mein ek diagram hai: 1 -> 2 -> 3, showing services interaction)

1.  **Content Chunker Service:**
    * Yeh service Message Queue se **event retrieve** karti hai.
2.  **Processing Step:**
    * Event mein se **Video ID** use karke Object Storage se video leti hai.
    * Video ko **smaller chunks** mein break karti hai.
    * In chunks ko wapis **Object Storage** mein upload karti hai.
3.  **Next Event Creation:**
    * Har uploaded chunk ke liye, yeh service ek naya **Event (with Chunk ID)** create karti hai aur usey **Message Queue** mein add karti hai.

**Why Add to Message Queue again?**
* Kyunki jo next service hai (**Format Converter Service**), usey pata hona chahiye ki "something to work on" (kaam karne ke liye kuch data ready hai).

---

### **Page 10: Format Conversion & Database Selection**
*(Source: IMG_20251120_010007_1.jpg)*

4.  **Format Converter Service:**
    * Yeh service individual chunks ko **different formats** mein convert karti hai.
    * *Example:* **.mov** format laptops ke liye, **.mp4** format mobile ke liye.
    * Har step ko explain karo.
5.  **Quality Converter Service:**
    * (Iska detail next page ya section mein hoga, bas naam mention hai).

**Video 43 -> High Level Design: Stream Content**
* **HLS Protocol:** Streaming content ke liye **HLS Protocol** use hota hai kyunki yeh **Adaptive** hai (network ke hisaab se adjust hota hai).

**Video 44 -> Deep Dive Insights: Database Selections**
* **Video DB (Metadata):**
    * Is database mein millions of requests aayengi video stream karne ke liye.
    * **Requirements:**
        * **High Scale** handle karna chahiye.
        * **Fast Access** hona chahiye.
        * **Simple Query Pattern** hota hai.
 
Yeh raha tumhare notes ke last page ka extraction aur Hinglish conversion. Maine page number sequence maintain kiya hai pichle response ke hisaab se.

-----

### **Page 11: Data Modeling & HLS Encoding**

*(Source: IMG\_20251120\_010017\_1.jpg)*

**Video 45 -\> Deep Dive Insights (Data Modeling)**

  * **Schema Definition:** Is section mein hum **Video DB Database** ke liye Data Modeling ka **Schema** define karte hain.
  * **Example Schema:**
    ```json
    Eg {
       videoId: "...",
       format: "...",
       ...
    }
    ```
  * **Note on Indexing:**
      * **VideoDB** mein **Indexing** add karna bahut zaroori hai.
      * **Reason:** Kyunki hamare system mein **"Common Query"** yahi hogi ki hum video ka metadata fetch karein (grab karein) using **VideoID**.
      * **Conclusion:** Isliye, **VideoID** hi hamara **Index** banega taaki search fast ho sake.

**Video 46 -\> Deep Dive Insights - HLS Encoding**

  * **HLS Encoding:** Is topic mein humein yeh samajhna hai:
      * **What it is:** HLS Encoding kya hai?
      * **Why we need to do this:** Humein iski zaroorat kyun padti hai?
      * **What problem it solves:** Yeh kaunsi problems ko solve karta hai? (Jaise network speed ke hisaab se video quality adjust karna).

-----

### **Next Step:**




=============================================================



### **Page 12: Introduction to TinyURL**
*(Source: IMG_20251120_010020_1.jpg)*

**#Section 4 -> Design TinyURL**

**Video 47 -> Introduction -> What is TinyURL?**
* **Definition:** TinyURL service kya hai aur yeh real life mein kaunsi problem solve karti hai?
* **Also known as:** Ise **URL Shortener Service** bhi kehte hain.
* **Function:** It shortens the long URLs. (Yeh lambe URLs ko chhota karti hai).
* **Logic:**
    * Agar aap ek **long URL** provide karte hain.
    * Toh TinyURL service us long URL ko leti hai (takes this long URL) aur badle mein **Short URL** provide karti hai.

**Video 48 -> Why do we need a TinyURL Service?**
* **Why it is useful (Yeh zaroori kyun hai):**
    1.  **Very easy to share:** Chhote link share karna aasaan hota hai.
    2.  **Character Limit:** Kuch platforms par character limit hoti hai (jaise Twitter/X par pehle thi), wahan short URL help karta hai.
    3.  **Clean and Professional:** Jab hum links share karte hain toh woh clean aur professional lagne chahiye, na ki messy.

---

### **Page 13: Functional & Non-Functional Requirements**
*(Source: IMG_20251120_010025_1.jpg)*

**Video 49 -> Deciding Requirements (Functional Requirements)**
* **Goal:** "What our service is able to do." (Hamari service kya kar payegi).
* **Features:** Humein describe karna hai ki users ko kya chahiye.
    1.  **To Generate a short URL:** User long URL dega, system short URL dega.
    2.  **To Get the long URL back:** Jab user short URL par click kare, toh system use wapis original long URL par bhej de.

**Video 50 -> Deciding Requirements (Non-functional Requirements)**
* **Availability:** Service hamesha available honi chahiye (Should be available 99.99% of time).
* **Low Latency:** "No one wanted to wait." (Koi intezaar nahi karna chahta).
    * Agar TinyURL service slow hai, toh website open hone mein delay hoga (Delay in opening website).

---

### **Page 14: Capacity Estimation (Users & Why it's important)**
*(Source: IMG_20251120_010028.jpg)*

* **Scalability:** Service ko ready hona chahiye heavy load handle karne ke liye (Service should be ready to handle).
* **Used to Create Short URL:** Load creation ke time par bhi handle hona chahiye.

**Video 51 -> Capacity Estimation (DAU/MAU)**
* **Estimated Number of Users:**
    1.  **DAU (Daily Active Users):** Hum assume kar rahe hain **300 Million users**.
    2.  **MAU (Monthly Active Users):** Number of unique users who use our service over one month. **Eg -> 1 Billion people**.
* **Important Question:** "Why Capacity Estimation of DAU/MAU is very important?"
    * Isko explain karte waqt **Real World Example** dena zaroori hai.

---

### **Page 15: Throughput Estimation (Write Operations)**
*(Source: IMG_20251120_010035_1.jpg)*

**Video 52 -> Capacity Estimation (Throughput)**
* **User Base Estimation:**
    * Hum calculate kar rahe hain throughput (requests per second/day).
    * "Read & Write requests our system will handle daily."
* **Primary Way - Assumption:**
    * Maan lete hain ki **10% of DAU** will create short URL.
    * **Calculation:** 10% of 300 Million users = **30 Million users**.
    * So, **30 Million daily requests** for short URL creation.
* **New Assumption:**
    * "Let's assume one user creates 5 short URLs/day."
    * **Calculation:** 30 Million users * 5 short URLs = **150 Million short URLs per day**.
* **Conclusion:** So, this is the total number of **Write Requests** or Write Operations that we need to handle each day.

---

### **Page 16: Throughput (Read) & Storage Estimation**
*(Source: IMG_20251120_010041.jpg)*

**Read Throughput (Primary Operation):**
* **Action:** Client reads the long URL (jab koi short link par click karta hai).
* **Assumption:** **20 read requests per 1 write request**. (Matlab 1 link banta hai toh 20 baar open hota hai).
* **Calculation:**
    * 300 Million DAU * (Assuming logic here implies total reads derived from writes).
    * Wait, notes mein likha hai: "Assume 20 long urls requests per day" (context shayad read vs write ratio ka hai).
    * **Calculation:** 300 Million * 20 = **6 Billion Read Requests per day**.
    * "Read requests that our system need to handle each day."

**Video 53 -> Capacity Estimation - Storage**
* **Storage Estimation:** Size of mapping of each URL.
* **Example Schema Size:**
    * 100 bytes (Long URL) + 30 bytes (Hash/Short ID) + 70 bytes (Metadata) = **Approx 200 Bytes per entry**.
    * "Average size of entry in a database."
* **Total Storage Calculation:**
    * "And we already calculated 150 Million create short URL/day."
    * **Total Storage/Day** = 150 Million * 200 Bytes = **30 GB**.
    * **Total Storage for 10 Years** = 30 GB * 365 * 10.

---

### **Page 17: Egress & API Design**
*(Source: IMG_20251120_010050_1.jpg)*

**EGRESS (Data Outflow):**
* **Definition:** Data flow out of our system.
* **When it happens:** Jab user long URL maangta hai (short URL par click karke) -> "User reads from our system."
* **Calculation:**
    * **6 Billion Read Requests/day**.
    * 1 Request returns **200 Bytes** of data.
    * Total Egress = 6 Billion * 200 Bytes = **1200 GB**.

**Video 56 -> API Design - Generate a Short URL**
* Hum API design karenge short URL generate karne ke liye.

**Video 57 -> API URL -> Get Long URL Back**
* Hum API design karenge wapis long URL fetch karne ke liye.
* "Explain all these how to do and all." (Is process ko detail mein samjhana hai).

---

### **Page 18: High Level Design (HLD) - Flow**
*(Source: IMG_20251120_010055_1.jpg)*

**Video 58 -> High Level Design - Generate Short URL**
* "Explain all the steps how it will be done."
* **Diagram Flow:**
    1.  **Client** request bhejta hai.
    2.  **API Gateway** request receive karta hai.
    3.  Gateway request ko **Generate Short URL Service** ke paas bhejta hai.
    4.  Service database (**DB**) mein URL mapping store karti hai aur Cache update karti hai.
* **Business Logic:** Isme main business logic hota hai.

**Video 59 -> High Level Design - Problem Collision**
* **Example:**
    * `tiny.url/abc` -> points to `www.google.com`
    * `tiny.url/abc` -> points to `www.facebook.com`
    * **Issue:** Two short URLs point to same long URL? (Notes mein thoda correction lag raha hai, actually collision tab hota hai jab **same short code** 'abc' do alag-alag websites ke liye generate ho jaye).
    * "Point to same long URL" (Likha hai, but context collision ka hai unique keys ke liye).

---

### **Page 19: Design Approaches (Random vs MD5)**
*(Source: IMG_20251120_010059_1.jpg)*

**Video 60 -> High Level Design Approach 1**
* **Approach 1: Random String Generation.**
* **Problem:** "Collision happen when same short url is generated for two or more different long url." (Jab do alag long URLs ke liye same short string generate ho jaye).

**Video 61 -> High Level Design Approach 2**
* **Approach 2: Use MD5 Algorithm.**
* **Properties of MD5:**
    * MD5 creates **unique outputs**.
    * MD5 doesn't rely on the server but on the **Input**. (Server ka state matter nahi karta, input same hai to output same hoga).
* **Guarantee:**
    * "So, if we input two different long URLs, MD5 will guarantee that each will have unique output."
    * "No 2 long URLs will ever get the same result."

---

### **Page 20: Handling MD5 Length & Collisions**
*(Source: IMG_20251120_010106.jpg)*

* **MD5 Output Issue:** MD5 generates unique string but output is a **long string**.
* **Length:** It is more than 20 characters.
* **Question:** "Can we shorten the MD5 output?"
    * **Answer:** Yes -> **Take the first 7 characters** from the MD5 output.
* **New Problem (Collision):**
    * "Collision happen -> If we take first 7 characters."
    * Kyunki MD5 unique hai puri string ke liye, but **MD5 don't guarantee first 7 characters will be unique**.

**Video 62 -> High Level Design**
* **Solution Flow:**
    * Approach 3: **Check DB for Collision.**
    * **Step 1:** Check DB for Collision.
    * **Meaning:** "After short URL is generated, check in database if there is..." (Agar database mein wo 7 character wali ID pehle se exist karti hai, toh collision hai, aur humein regenerate karna padega).

---

### **Summary of Next Steps:**
Tumhara **TinyURL System Design** ka section shuru ho gaya hai. Isme humne cover kiya:
1.  Functional/Non-functional requirements.
2.  Capacity Estimation (Storage 30GB/day, Read 6 Billion/day).
3.  Approaches: Random String (Bad) vs MD5 (Good but needs handling).

Yeh raha tumhare TinyURL Design ke remaining notes ka complete extraction aur Hinglish conversion step-by-step. Sequence wahin se continue kar raha hoon jahan pichla khatam hua tha.

---

### **Page 21: Handling Collisions & Approach 4 (Counters)**
*(Source: IMG_20251120_010108_1.jpg)*

* **Problem with Approach 3 (Check DB):**
    * Agar collision hota hai, toh "Again create the short URL" (phir se naya generate karo).
    * **Drawback:** "This approach makes system slow and also increases the low latency problem." (Yeh system ko slow kar deta hai aur latency badha deta hai).

**Video 63 -> High Level Design: Approach 4 (Counters)**
* **Solution:** "Let's keep Counters."
* **Goal:** Humein collision avoid karna hai **without needing to regenerate strings**.
* **Concept:** "A simple approach -> Numbering System."
* **Example:**
    * `www.google.com` -> Generated -> `tiny.url/1`
    * `www.facebook.com` -> Generated -> `tiny.url/2`
    * `www.instagram.com` -> Generated -> `tiny.url/3`
* **Logic:**
    * Hum har "Long URL input" ko ek **Unique Number** assign karenge.
    * Isse **Collision can be eliminated** (collision khatam ho jayega).
    * "Every URL is bound to get a distinct number in the sequence." (Har URL ko sequence mein ek alag number milega).

---

### **Page 22: Distributed Systems & Zookeeper**
*(Source: IMG_20251120_010114.jpg)*

* **Distributed System Problem:**
    * "But if you start this algorithm on two different servers..." (Agar aap yehi counting algorithm do alag servers par chalaoge).
    * **Issue:** "Again same problem will happen." (Server 1 ne bhi '1' generate kiya, Server 2 ne bhi '1' generate kiya -> Overlap/Collision).
    * Explain this -> Explain how synchronization fails here.

* **Solution: Coordination:**
    * "So, all the servers need to coordinate with each other."
    * Isse ensure hoga ki woh **same number generate na karein** aur koi **overlap** na ho.

**Video 64 -> High Level Design: Approach 4 (Zookeeper)**
* **Tool:** "This problem is solved by **Zookeeper**."
* **Zookeeper Service Logic:**
    * Imagine **Server 1** aur **Server 2** hain.
    * Zookeeper ek **Range** assign karta hai:
        * Server 1 ko range di: `[1, 1000]`
        * Server 2 ko range di: `[1001, 2000]`
    * **Benefit:** "Zookeeper solves the problem of coordination between distributed systems."

---

### **Page 23: Zookeeper Recap & Base 62 Introduction**
*(Source: IMG_20251120_010117.jpg)*

* **Zookeeper Assurance:**
    * Zookeeper ensure karega ki "Servers can coordinate to assign unique numbers preventing collisions."
    * Different ranges dene se overlap hone ka chance khatam ho jata hai.

**Video 65 -> High Level Design: Approach 4 (Base 62 Encoding)**
* **Problem with Simple Numbers:**
    * Agar hum simple numbering system use karein (jaise `tiny.url/1`, `tiny.url/10`, `tiny.url/987654`), toh...
    * **Issue:** "As we keep going, length of our short url will keep on increasing." (Jaise users badhenge, URL lamba hota jayega).
    * Example: `tiny.url/999999999` -> Yeh "short" nahi raha.

---

### **Page 24: Understanding Base 62 Encoding**
*(Source: IMG_20251120_010121_1.jpg)*

* **Solution:** "So, this is where **Base 62 Encoding** comes."
* **Base 10 (Normal Math):**
    * Isme digits `0-9` hote hain. Total 10 symbols.
* **Base 62 (Our Solution):**
    * Hum "Number of characters" ko expand karte hain.
    * **Composition:**
        * Numbers (0-9) = 10
        * Uppercase Letters (A-Z) = 26
        * Lowercase Letters (a-z) = 26
    * **Total Possibilities:** $10 + 26 + 26 = 62$.
    * Isliye isey **Base 62** kehte hain.

* **Advantage:**
    * Base 10 ke comparison mein, Base 62 se hum **much shorter URLs** create kar sakte hain jo same number ko represent karte hain.
* **Example:**
    * Base 10 mein value: **9876549**
    * Base 62 mein wahi value ban jati hai: **fRLB** (Only 4 chars!).

---

### **Page 25: Mathematical Proof (Base 10 vs Base 62)**
*(Source: IMG_20251120_010124_1.jpg)*

* **Base 10 Calculation:**
    * Number `9876549` ko kaise likhte hain:
    * $$(9 \times 10^6) + (8 \times 10^5) + \dots + (9 \times 10^0)$$
* **Base 62 Calculation:**
    * Wahi number `9876549` Base 62 mein `fRLB` hai:
    * $$(f \times 62^3) + (R \times 62^2) + \dots + (B \times 62^0)$$
* **Observation:**
    * Base 62 mein humein "Very many more possibilities and combinations for that single character" milti hain.

* **Scale:**
    * Agar hum sirf **7 Characters** use karein Base 62 mein:
    * $$62^7 = 3.5 \text{ Trillion unique URLs}$$
* **Conclusion:**
    * "Every character can be of 62 possibilities instead of the 10 possibilities we saw in Base 10."
    * Hum **kam characters mein zyada information pack** kar rahe hain. (Pack more information into fewer characters).
    * Isse hum Billions aur Trillions unique short URLs bana sakte hain.

---

### **Page 26: Generating Design Pattern (Read Flow)**
*(Source: IMG_20251120_010130_1.jpg)*

**Video 66 -> High Level Design (Approach 4 Pattern)**
* Explain everything step by step.

**Video 67 -> High Level Design: Get Long URL (Read Flow)**
* **Scenario:** Jab user browser mein short URL type karta hai.
    1.  **Request:** Browser sends a **GET Request** to the **API Gateway** on the `/{shortUrl}` endpoint.
    2.  **Forwarding:** API Gateway request receive karta hai aur usey **Forward** karta hai **GetLongURL Service** ko (via Load Balancer).
    3.  **Checking:** "GetLongURL Service checks the **Cache** (URL Mappings) for the Short URL."

---

### **Page 27: Cache Miss & Database Selection**
*(Source: IMG_20251120_010133_1.jpg)*

* **Cache Logic:**
    * Agar Cache mein data nahi mila, toh service **Database** check karegi.
    * "Ultimately it would also update itself" (Cache DB se data lekar khud ko update karega taaki agli baar request Cache se hi serve ho jaye).

**Video 68 -> Deep Dive Insights: Database Selections**
* **Criteria:** Database select karte waqt humein kya dhyan rakhna hai?
    * Speed
    * Scale
    * Query Pattern
    * Structure Flexibility
* **Decision:**
    * Iss project ke liye **Speed is Priority**. Humein Long URL ko "Quickly Convert" karna hai.
    * **Speed:** NoSQL is better.
    * **Scale:** NoSQL can handle large amounts of data easily.
    * **Query Pattern:** NoSQL suits our simple Key-Value lookup.
    * **Conclusion:** Isliye hum **NoSQL** use karenge.

---

### **Page 28: Data Modeling & Redirection**
*(Source: IMG_20251120_010143.jpg)*

**Video 69 -> Deep Dive Insights: Data Modeling**
* **Structure:** Hamara database **Key-Value format** mein hoga.
    * **Key:** Short URL
    * **Value:** Long URL
* **Optimization:** Cheezon ko speed up karne ke liye, hum **Indexing** use karenge on `'Short URL'` column.

**Video 70 -> Deep Dive Insights: Redirection (301 vs 302)**
* **Process:**
    * Browser short URL ko big (long) URL mein convert karta hai.
    * Server jab response bhejta hai, toh usme **HTTP Status Code 301** hota hai.
* **Meaning of 301:**
    * "This 301 Status Code tells the browser to **Redirect** to the Long URL."

---

### **Page 29: Completing the Flow**
*(Source: IMG_20251120_010145_1.jpg)*

* **Final Step:**
    * "So the Browser gets the Long URL from the response along with the Status Code."
    * **Action:** Browser is status ko samajhta hai ki yeh redirection hai.
    * Isliye woh "Actually open the long web page," completing the whole process.

---
**Summary of Concepts Covered:**
1.  **Collision Handling:** Counter method is better than checking DB repeatedly.
2.  **Zookeeper:** Multiple servers ke beech counters sync karne ke liye (Ranges assign karna).
3.  **Base 62 Encoding:** Numbers ko chhota karne ka math method ($62^7$ combinations).
4.  **Database:** NoSQL use karenge speed aur scale ke liye.
5.  **Status Code:** 301 Redirect use hoga.

=============================================================

Yeh raha tumhare **Section 5: Design Rate Limiter** ke notes ka complete extraction aur Hinglish conversion step-by-step. Sequence bilkul logical flow mein set kiya gaya hai.

---

### **Page 30: Introduction to Rate Limiter**
*(Source: IMG_20251120_010152.jpg)*

**#Section 5 -> Design Rate Limiter**

**Video 71 -> Introduction -> Analogy**
* Sabse pehle hum ek **Analogy** (example) se samjhenge.
* *Note:* Jaise club ke bahar bouncer khada hota hai jo limit karta hai ki kitne log andar jayenge, waise hi Rate Limiter kaam karta hai.

**Video 72 -> Introduction -> What is Rate Limiter?**
* **Definition:** Rate Limiter kya hai, yeh kyun use hota hai?
* **Real Life Problem:** Yeh kaunsi real life problem solve karta hai?
* **When we need:** Humein Rate Limiter ki zaroorat kab padti hai?

**Video 73 -> Why do we need Rate Limiter?**
* **Reason 1: Prevent Overloading:**
    * Yeh server ko **Too many requests** se bachata hai.
    * **Overloading:** Yeh system ko overwhelm kar sakta hai, jisse system ya toh **Crash** ho jayega ya phir **Poorly Perform** karega.

---

### **Page 31: Benefits & Requirements**
*(Source: IMG_20251120_010156_1.jpg)*

* **Role:** Rate limiter requests ke number ko **Cap** (limit) karta hai taaki sab kuch stable rahe.
* **Reason 2: Ensure Fair Usage:**
    * "One user sending too many requests can block other users from their service."
    * Ek user agar spam karega toh baaki innocent users block nahi hone chahiye. Rate limiter sabko barabar mauka deta hai.
* **Reason 3: Control Costs:**
    * "More requests mean more processing power." (Zyada requests matlab zyada server bill).
    * **Restrict Excessive Usage:** Faaltu traffic ko rok kar hum **Processing Costs** ko control mein rakhte hain.

**Video 74 -> Deciding Requirements (Functional Requirements)**
* **Features:**
    1.  **Restrict based on:**
        * IP Address
        * User ID
        * Device ID
        * Session ID
    2.  **Notification:** Agar user limit exceed kar deta hai, toh "User must notify them" (System user ko bataye ki limit khatam ho gayi hai).

---

### **Page 32: Non-Functional Requirements & Capacity**
*(Source: IMG_20251120_010202_1.jpg)*

**Video 75 -> Deciding Requirements (Non-Functional)**
1.  **High Availability:** System hamesha chalna chahiye.
2.  **Low Latency:** "Because Rate Limiter is implemented as a part (sub-system) of a big system." (Kyunki yeh har request ke raaste mein aata hai, isliye iska fast hona bahut zaroori hai).
3.  **Cost Effectiveness:** Rate limiter khud mehnga nahi padna chahiye.

**Video 76 to 79 -> Capacity Estimation**
* **Video 76:** Capacity Estimation DAU/MAU.
* **Video 77:** Throughput Estimation.
* **Video 78:** Storage & Memory Estimation.
* **Video 79:** Network Bandwidth Estimation.
* *Note:* In sab videos mein wahi calculations hongi jo humne pichle sections mein ki thi (Assumptions lo aur multiply karo), bas example badal jayenge taaki "Pure Clarity" mile.

---

### **Page 33: Placement of Rate Limiter (Option 1)**
*(Source: IMG_20251120_010204_1.jpg)*

**Video 80 -> High Level - Placement of Rate Limiter**
* **Topic:** Humein Rate Limiter kahan lagana chahiye?

**Option 1: Placing the Rate Limiter BEFORE the API Servers**
* **Mechanism:** Effectively controls the traffic **before it is reaching the API servers**. (Server tak baat pahunchne se pehle hi rok lo).
* **Pros (Fayde):**
    * **Security:** We are blocking malicious traffic early, improving security.
    * **Reduced Load:** API Server handle less traffic as the Rate Limiter blocks many requests. (Server par load kam padta hai).
* **Cons (Nuksaan):**
    * **Increased Latency:** Add an extra processing step, which might slow things down.
    * **Single Point of Failure:** Agar yeh Rate Limiter fail ho gaya, toh "Everything is stopped" (poora system access band ho jayega).

---

### **Page 34: Placement of Rate Limiter (Option 2)**
*(Source: IMG_20251120_010209_1.jpg)*

**Option 2: Placing the Rate Limiter IN the API Servers or WITH the API Servers**
* **Mechanism:** Code level par implementation.
* **Pros:**
    * **Granular Control:** Allows custom rate limiting for each server or service. (Har service ka apna rule ho sakta hai).
    * **No Central Point of Failure:** Improve fault tolerance as there is no central failure point.
* **Cons:**
    * **Increased Server Load:** Servers have to handle the rate limiting logic, adding extra work. (Server ko business logic ke saath filtering bhi karni padegi).

**Conclusion:** "Now, which approach is better depend on system." (System ki zaroorat ke hisaab se decide karo).

---

### **Page 35: High Level Design Flow**
*(Source: IMG_20251120_010212.jpg)*

**Video 81 -> High Level Design - Basic Flow**
1.  **Client Request:** Process tab shuru hota hai jab Client request bhejta hai.
2.  **Rate Limiter Check:** Server tak pahunchne se pehle, request ko Rate Limiter check karta hai.
    * *Condition:* "The limit is 100 requests in a minute."
    * **Allowed:** Agar request allowed hai, toh woh API Server tak pahunchti hai for processing.
    * **Blocked (Exceeded):**
        * "Note -> If the client exceeds their rate limit -> It send the HTTP Status Code of **429**."
        * **HTTP 429:** This means **"Too Many Requests"**.

---

### **Page 36: Storing Request Counters**
*(Source: IMG_20251120_010217.jpg)*

**Video 82 -> High Level Design: Storing Requests**
* **Logic:** Jab client request bhejta hai, woh pehle Rate Limiter tak pahunchta hai.
* **Decision:** Rate Limiter decide karta hai **Allow** or **Block**.
* **How?** Based on "Number of requests made by that client in a specific time frame."
    * Iske liye humein ek **Request Counter** chahiye.
* **Problem:**
    * "If request is above then Request Counter then request is dropped and vice-versa."
    * **Storage Issue:** "Where are we actually storing this Request Counter?"
    * **Database?** "Database are **too slow** for this type of frequency check." (Har request par DB query karna slow hoga).

---

### **Page 37: Cache & Rules Database**
*(Source: IMG_20251120_010219_1.jpg)*

* **Solution: Cache (Redis):**
    * "What about storing in Cache?"
    * Cache fast aur efficient hota hai for storing small pieces of data like **Request Counters**.
    * Yeh millions of requests ko bina kisi delay ke handle kar sakta hai.

**Video 83 -> High Level Design: Storing Rate Limiter Rules**
* Counters ke alawa humein **Rules** bhi store karne padte hain.
* "The limit is stored in something we call as the **Rules DB**."
* **Example Rules:**
    * `Create Post API` -> Limit: 100 posts/day.
    * `Comments Post API` -> Limit: 500 comments/day.
* **Process:**
    * Hum saare threshold values (Rules) ko store karte hain for different types of requests.

---

### **Page 38: Updating Rules & Algorithms Overview**
*(Source: IMG_20251120_010225.jpg)*

* **Rule Service:**
    * "We also have Rule Service."
    * Yeh service **Rules DB** se rules leti hai aur unhein **Rules Cache** mein update karti hai periodically.
    * **Why Cache?** "Access these rules faster from a Cache versus a Database." (Taaki rules check karne mein time na lage).

**Video 84 -> Deep Dive Insights: Rate Limiting Algorithms**
* **Core Logic:** Rate limiting ke peeche ka logic 5 algorithms se implement ho sakta hai.
* **List of Algorithms:**
    1.  **Token Bucket** (Bahut popular hai).
    2.  **Leaky Bucket** (Smooth traffic ke liye).
    3.  **Fixed Window Counter**.
    4.  **Sliding Window Log**.
    5.  **Sliding Window Counter**.

---

### **Page 39: Token Bucket & Leaky Bucket Details**
*(Source: IMG_20251120_010233_1.jpg)*

**Video 85 -> Deep Dive Insights - Token Bucket Algorithm**
* **Bucket Capacity:** Suppose capacity = 3 (Matlab hum 3 coins/tokens store kar sakte hain).
* **Bucket Refiller:** Yeh refiller bucket ko refill karta hai "at a particular rate."
* **Consumption:** "Each request will consume one coin." (Har request ek token le jayegi).
* *Note:* Explain this algorithm, how it is used solving real life problem.

**Video 86 -> Deep Dive Insights - Leaky Bucket Algorithm**
* **Analogy:**
    * **Incoming Water Tap:** Represents all the **Incoming requests** to our system.
    * **Outgoing Water (via hole):** Represents all the **Processed requests**.
    * **Overflowing Water:** Represents all the requests that are **Dropped** (Rate Limited).
* *Note:* Isme requests ek constant speed par process hoti hain, jaise bucket se paani tapakta hai.

---
**Summary of Section 5:**
Is section mein humne **Rate Limiter** ka poora design dekha:
1.  **Placement:** Gateway (Middleware) vs Server code.
2.  **Storage:** Counters **Cache (Redis)** mein rahenge speed ke liye, aur Rules **DB** mein.
3.  **Flow:** Client -> Rate Limiter (Check Cache) -> API Server.
4.  **Algorithms:** Token Bucket aur Leaky Bucket main hain.

Yeh raha tumhare **Rate Limiter Algorithms** ke remaining notes ka complete extraction aur Hinglish conversion step-by-step. Sequence wahin se continue ho raha hai (Page 40 se).

---

### **Page 40: Fixed Window Counter Algorithm**
*(Source: IMG_20251120_010240_1.jpg)*

**Video 87 -> Deep Dive Insights: Fixed Window Counter Algorithm**
* **Concept:**
    * "Time is divided into fixed window." (Time ko fixed tukdon mein baata jata hai).
    * **Window Size:** Humne choose kiya hai ki window ki length **60 seconds** hogi.
* **Structure:**
    * **Window 1:** 0 se 60 seconds tak.
    * **Window 2:** 60 se 120 seconds tak.
* **Logic:**
    * "Every window has a certain limit that we set." (Har window ki apni ek limit hoti hai).
    * Yeh limit batati hai ki "Maximum request allowed in that window."
* **Rate Limiting:**
    * Agar limit cross hoti hai, toh "All the extra requests would be rate limited" (baaki requests drop ho jayengi).
    * **Reset:** "At the beginning of every window our counter is reset." (Jaise hi nayi window shuru hoti hai, counter zero ho jata hai).

---

### **Page 41: Fixed Window Example**
*(Source: IMG_20251120_010247_1.jpg)*

* **Example Scenario:**
    * **Window Size:** 60 seconds.
    * **Limit:** "We allow 5 requests every minute at the maximum."
* **Execution:**
    * **First Window:** Maan lo 3 requests aayi. Since **3 < 5**, yeh allow hongi.
    * **Reset Point:** "At t=60 second, before the start our second window, the counter is reset."
    * **Next Step:** Hum wapis zero se counting start karte hain (We start counting from zero again).
* **Note:**
    * Explain all these. How it solves real world problem. (Isse hum traffic spikes ko simple tareeke se control karte hain).

---

### **Page 42: Sliding Window Log (The Improvement)**
*(Source: IMG_20251120_010255.jpg)*

**Video 88 -> Deep Dive Insights: Sliding Window Log Algorithm**
* **Why this algorithm?**
    * "Sliding window is an improvement over the Fixed Window Counter algorithm."
* **Problem with Fixed Window (Edge Case):**
    * Fixed Window mein agar limit 60s ki hai, toh user system ko cheat kar sakta hai.
    * **Trick:** User apni requests "near the edge of the window" bhej sakta hai (End of window 1 and Start of window 2).
    * Isse woh double requests bhej payega kam waqt mein.
* **Solution (Sliding Window):**
    * "It keeps a sliding window instead of a fixed window."
    * **Logic:** Yeh hamesha **current time se peeche dekhta hai** (Look back from the current time to the window size).
    * Is hisaab se decide hota hai ki request ko allow karna hai ya rate limit karna hai.

---

### **Page 43: How Sliding Window Log Works**
*(Source: IMG_20251120_010300_1.jpg)*

1.  **Sliding Window Capacity:**
    * Iska matlab hai "Maximum number of timestamps that the window can hold."
2.  **Sliding Window Lookback:**
    * "How many second to look back." (Kitna peeche dekhna hai).
3.  **Step-by-Step Process:**
    * **Step A:** Whenever a request comes in, we first **look back 60 seconds**.
    * **Step B:** "Remove any requests that are outside this window." (Jo requests 60 second se purani hain, unhein hata do).
    * **Step C:** "Count the total number of requests within this window."
4.  **Decision:**
    * **If (Sum < Limit):** "If the sum is within the limit, it means that our window still has the capacity to hold request." -> **Allow**.
    * **If (Sum > Limit):** "But if this exceeds the limit, or our window is already at its fullest capacity" -> **Reject**.
    * *Note:* Explain this how it is useful. (Yeh 'Edge Case' problem ko solve karta hai kyunki window user ke saath-saath move karti hai).

---

### **Page 44: Sliding Window Counter & Race Conditions**
*(Source: IMG_20251120_010305_1.jpg)*

**Video 89 -> Deep Dive Insights: Sliding Window Counter Algorithm**
* **Hybrid Approach:**
    * "It is the average of -> **Fixed Window Counter + Sliding Window Log** algorithms."
    * (Yeh dono algorithms ke best parts ko combine karta hai taaki accuracy bhi mile aur memory bhi kam use ho).
    * Explain this also: when to use what and all.

**Video 90 -> Deep Dive Insights: Handling Race Conditions**
* **Problem:** Jab multiple requests ek saath aati hain (Concurrency).
* **Topic:** "Handling Race Conditions."
* Explain this also. (Race conditions tab hoti hain jab do process ek sath counter read/write karte hain, aur counting galat ho jati hai. Iske liye locking ya Lua scripts use hote hain Redis mein).

---

**Summary of Concepts Covered:**
1.  **Fixed Window:** Simple hai, par "Edges" par double traffic allow kar deta hai.
2.  **Sliding Window Log:** Accurate hai (Lookback mechanism), par memory heavy ho sakta hai (saare timestamps store karne padte hain).
3.  **Sliding Window Counter:** Best of both worlds (Hybrid).
4.  **Race Conditions:** Multi-threaded environment mein counters ko protect karna zaroori hai.


=============================================================

Based on the images you provided, these are handwritten notes for the **System Design of a Chat Application (like WhatsApp)**. The notes follow a sequence of video lectures (marked as Video 91, 92, etc.).

### **Page 1: Requirements & Capacity (From IMG_20251120_010308_1.jpg)**

**Topics Covered:** Video 91, 92, 93 (Functional & Non-Functional Requirements)

* **Section 6 -> Design WhatsApp -> Deciding Requirements**
    * **Video 91: Functional Requirements**
        Is section mein hum decide kar rahe hain ki app kya kya karega:
        1.  **One on one messaging:** Do logon ke beech direct chat.
        2.  **Message Status:** Pata chalna chahiye message gaya ya nahi (Sent, Delivered, Read).
        3.  **Last seen and online status:** User kab online tha ye dikhna chahiye.
        4.  **Group chat:** Ya fir "Chat for group" feature hona chahiye.

    * **Video 92: Deciding Requirements (Non-functional)**
        System kaisa perform karna chahiye:
        1.  **High Availability:** System hamesha chalna chahiye, down nahi hona chahiye.
        2.  **Low Latency:** Message turant deliver hona chahiye, delay nahi hona chahiye.
        3.  **Scalability:** Agar users badh gaye to system handle kar sake.
        4.  **Security:** Chats secure honi chahiye.

    * **Video 93: Capacity DAU/MAU**
        Isme hum **Daily Active Users (DAU)** aur **Monthly Active Users (MAU)** ka estimation lagayenge taaki system ki capacity plan kar sakein.

---

### **Page 2: Capacity Estimation - Throughput (From IMG_20251120_010316.jpg)**

**Topics Covered:** Video 94 (Throughput & Message States)

* **Video 94: Capacity Estimation - Throughput**
    * Humein **Read and Write QPS (Queries Per Second)** calculate karna hai ki system pe kitna load padega.
    * **Writes process:** Data add karna -> Data update karna.
    * **Message Flow (Explain all these):**
        1.  **Sender sends a message:** Sender ne message bheja.
        2.  **State of the message changes:** Message ka status badalta rehta hai.
            * Flow: **Sent -> Delivered -> Read**.
        3.  **Receiver reads:** Jab receiver message padhta hai to state update hoti hai.
        4.  **Note:** Har baar jab state change hoti hai (Sent se Delivered, Delivered se Read), server ko update update karna padta hai, jo system par write load badhata hai.

---

### **Page 3: Storage & Bandwidth Estimation (From IMG_20251120_010319_1.jpg)**

**Topics Covered:** Video 95, 96, 97 (Storage, Memory, Network)

* **Video 95: Capacity Estimation - Storage**
    * Humein store karne ke liye space estimate karna hai.
    * **Text Messages:** Maan lete hain ek message **100 Bytes** ka hai.
    * **Media (Images, Videos, Docs):** Average size **250 Kilo Bytes (KB)** maan lete hain.
    * **Assumption:** Maan lo ki har 100 messages mein se **1 (one)** message media file hoti hai (Wait 1:1 message is media message).

* **Video 96: Capacity Estimation - Memory**
    * **Cache Memory:** Isko bhi estimate karna hai. Cache wo fast memory hai jo frequently accessed data ko store karti hai taaki database par load kam ho.

* **Video 97: Capacity Estimation (Network Bandwidth)**
    * Ye estimate karna hai ki kitna data internet cable/network ke through second travel karega (upload/download speed required for server).

---

### **Page 4: API Design - Fundamentals (From IMG_20251120_010325_1.jpg)**

**Topics Covered:** Video 98 (HTTP vs WebSocket)

* **Video 98: API Design - 1:1 Messaging**
    * **Issue with HTTP:** Normal HTTP mein sirf **Client (app)** server ko data bhej sakta hai (request). Server khud se client ko data nahi bhej sakta jab tak client na mange.
    * **Requirement:** Messaging app ke liye humein **Two-way communication** chahiye. Server ko bhi client ko message bhejna padta hai jab koi naya message aaye.
    * **Solution - WebSocket:** Isliye hum **WebSocket** use karte hain jo **Bidirectional communication** (dono taraf se baat) allow karta hai.
    * **Process:**
        1.  WebSocket asal mein HTTP connection ka hi **upgraded version** hai.
        2.  Pehle client server ko ek **HTTP request** bhejta hai ki "Please connection ko HTTP se WebSocket protocol par upgrade kar do."
        3.  Ek baar connection upgrade ho gaya, fir data dono taraf transfer ho sakta hai smoothly.

---

### **Page 5: API Design - Status & Groups (From IMG_20251120_010328_1.jpg)**

**Topics Covered:** Video 99, 100, 101 (Detailed API Design)

* **Video 99: API Design - Message Status**
    * Message teen steps mein move karta hai:
        1.  **Sent from client:** Sender ke phone se chala gaya.
        2.  **Received by user:** Receiver ke phone par pahunch gaya (Delivered).
        3.  **Seen by user / Read by user:** Receiver ne chat khol kar padh liya.

* **Video 100: API Design - Online Status**
    * Online status aur **Last Seen** kaise kaam karta hai.
    * *Note:* Isme example ke saath samjhna hai ki API request body mein kya data pass hota hai (jaise `userId`, `timestamp`, `status: "online"`).

* **Video 101: API Design - Group Messages**
    * **Difference:** 1:1 mein single recipient hota hai, lekin Group message mein **multiple recipients** (bahut saare log) hote hain.
    * Iska API design alag hoga kyunki server ko ek message copy karke group ke saare members ko bhejna padega.

---

### **Page 6: High Level Design - Connections (From IMG_20251120_010334_1.jpg)**

**Topics Covered:** Video 102, 103, 104 (WebSocket & Offline Handling)

* **Video 102: High Level Design - WebSocket Connection**
    * Ye explain karna hai ki WebSocket connection exactly establish kaise hota hai (Handshake process). Ye beginners ke liye clear hona chahiye taaki koi confusion na ho.

* **Video 103: High Level Design - 1:1 Messaging**
    * Do logon ke beech message server ke through kaise flow karta hai.

* **Video 104: High Level Design - 1:1 Messaging (Offline Client)**
    * Agar receiver offline hai (internet band hai) to kya hoga?
    * **Solution:** Server us message ko **Database** mein store kar lega taaki message lost na ho. Jab user online aayega, DB se message deliver ho jayega.

---

### **Page 7: High Level Design - Media & Status (From IMG_20251120_010336_1.jpg)**

**Topics Covered:** Video 105, 106, 107, 108 (Media & Online Logic)

* **Video 105 & 106: HLD - Image, Video, Document (Media)**
    * Badi files (media) directly websocket se nahi bhejte.
    * **Process:**
        1.  Media ko **CDN (Content Delivery Network)** ya Object Store (S3) par upload karte hain.
        2.  Wahan se ek **URL** milta hai.
        3.  Sirf wo URL doosre user ko message text ke roop mein bheja jata hai.

* **Video 107: HLD - Message Status**
    * Kaise server track karta hai ki message deliver hua ya read hua.

* **Video 108: HLD - Online Status Design**
    * **Logic:** Kaise pata chalega user online hai?
    * Diagram dikhata hai: **Actively using the app** + **Internet is ON**.
    * Agar connection bana hua hai (Heartbeat signal), to user Online hai. Connection toota, to Offline.

---

### **Page 8: Deep Dive - DB & Security (From IMG_20251120_010342.jpg)**

**Topics Covered:** Video 109, 110, 111, 112 (Group Msg, Database, E2EE)

* **Video 109: High Level Design - Group Messages**
    * **Ticks Logic:**
        * One Tick -> Sent (Server tak pahunch gaya).
        * Double Tick (Grey) -> Delivered (User ke phone tak pahunch gaya).
        * Blue Tick -> Received/Read (User ne dekh liya).

* **Video 110: Deep Dive Insights - Database Selection**
    * **SQL vs NoSQL:** Hum kya choose karein?
    * **Decision:** WhatsApp Messages aur Group Messages ke DB ke liye **NoSQL** best hai.
    * **Reason:** "Because of faster access." Messaging mein bohot high write aur read rate hota hai, jo NoSQL (jaise Cassandra or HBase) achi tarah handle karta hai.

* **Video 111: Deep Dive - Data Modelling**
    * **Indexing:** Humein **ReceiverId** par indexing karni chahiye.
    * **Why?** Kyunki jab user app kholta hai, to humein wo saare messages query karne hote hain jo *uske liye* (ReceiverId = User) aaye hain.
    * **Table Structure:** `messageId`, `senderId`, `receiverId`, `messageType`, `message`, `assetUrl`, `state`, `time`.

* **Video 112: Deep Dive - End to End Encryption (E2EE)**
    * Ye samjhna zaroori hai ki **End to End Encryption** exactly kya hoti hai. (Matlab message sirf sender aur receiver padh sakte hain, beech mein server ya hackers nahi padh sakte).
    
    
=============================================================

Based on the images you provided, these notes cover the **System Design of a Search System (like Twitter/X)**. They range from Video 113 to Video 118.



### **Page 1: Introduction to Search System (From IMG_20251120_010351_1.jpg)**

**Topics Covered:** Video 113 (Functional Requirements)

* **Section 7 -> Design Search System**
    * **Video 113: Deciding Requirements (Functional)**
        * **Search System:** Ye system users ko relevant information efficiently find karne mein help karta hai.
        * **Example:** Hum **Twitter (X.com)** ka example le rahe hain is course mein.
    * **Functional Requirements:**
        1.  **Users can search by keywords:** Users specific words type karke search kar sakein.
        2.  **Hashtags:** Topics dhoondhne ke liye hashtags use kar sakein.
        3.  **Usernames:** Specific person ya account ko dhoondh sakein.
        * **Goal:** User specific topic ya person ko dhoondhne ki koshish kar raha hai, to system ko accurate result dena chahiye.

---

### **Page 2: Non-Functional Requirements (From IMG_20251120_010405_1.jpg)**

**Topics Covered:** Video 114 (Attributes of the System)

* **Video 114: Deciding Requirements (Non-Functional)**
    * Ye wo qualities hain jo determine karti hain ki system kaise perform karta hai (How it performs vs What it does).
    * **Key Attributes:**
        1.  **Availability (Sabse Important):**
            * Search system ke liye **High Availability** critical hai (99.99%).
            * System hamesha available hona chahiye. Users hamesha search kar paayein.
            * Peak loads (jab bahut log use kar rahe hon) ya minor outages mein bhi system down nahi hona chahiye.
        2.  **Scalability:** System grow kar sake.
        3.  **Reliability:** Bharosemand hona chahiye.
        4.  **Speed:** Results fast aane chahiye.

---

### **Page 3: Capacity Estimation - High Level (From IMG_20251120_010412_1.jpg)**

**Topics Covered:** Video 115 (DAU/MAU & Latency)

* **Video 115: Capacity Estimation (DAU/MAU)**
    * **Why?** Users expect instant results.
    * **Low Latency:** Chahe kitne bhi log platform use kar rahe hon (millions of users searching simultaneously), search function sabke liye fast aur available hona chahiye.
    * **Metrics:**
        * **DAU:** Daily Active Users.
        * **MAU:** Monthly Active Users.
    * Ye calculations humein future ke liye plan karne mein help karti hain.

---

### **Page 4: Throughput Definition (From IMG_20251120_010415_1.jpg)**

**Topics Covered:** Video 116 (Throughput basics)

* **Video 116: Throughput**
    * Throughput measure karta hai ki system overtime kitna data process kar sakta hai.
    * **System Capacity:** System bina performance giraye (degradation) kitne user requests handle kar sakta hai.
    * Ise hum do parts mein divide karte hain:
        1.  **The Read Throughput:**
            * Iska matlab hai kitna data system se read kiya ja raha hai.
            * Examples: Fetching parts, loading user profiles, searching for information.
        2.  **The Write Throughput:**
            * Iska matlab hai kitna data system mein likha (insert) ja raha hai.

---

### **Page 5: Throughput Calculation (From IMG_20251120_010426_1.jpg)**

**Topics Covered:** Video 116 (Calculation Example)

* **Example of Write:** Creating posts, Saving settings, Uploading content.
* **Balance:** Ek balanced system ke liye Read aur Write dono types important hain. But search system mein Read load zyada hota hai.
* **Calculation (Case of Search for Twitter):**
    * **Assumption:** Maan lo **DAU (Daily Active Users) = 100 Million** (Note mein math 100M ke hisaab se hai, text mein 500M likha hai par calculation dekho).
    * **Usage:** Har user din mein **5 searches** karta hai.
    * **Total Searches:** $100 \text{ Million} \times 5 = 500 \text{ Million searches/day}$.
    * **Searches per Second:**
        * $500 \text{ Million} / (24 \text{ hours} \times 60 \text{ mins} \times 60 \text{ secs})$.
        * Result $\approx$ **5,787 searches/second**.
    * Iska matlab system ko itna load har second handle karna padega.

---

### **Page 6: Storage Estimation (From IMG_20251120_010430_1.jpg)**

**Topics Covered:** Video 117 (Storage)

* **Video 117: Capacity Estimation - Storage**
    * Humein data store karne ke liye space calculate karna hai.
    * **Assumptions:**
        * **DAU:** 100 Million users.
        * **Tweets:** Average 1 tweet per day per user.
        * **Tweet Size:** Average tweet size **200 Bytes** (200 characters).
    * **Total Storage per Day:**
        * $100 \text{ Million users} \times 1 \text{ tweet} \times 200 \text{ Bytes}$.
        * $20,000 \text{ Million Bytes}$ = **20 GB/day**.
    * Iska matlab humein rozana **20 GB** naya data store karna padega.

---

### **Page 7: Long Term Storage & Cache Intro (From IMG_20251120_010436_1.jpg)**

**Topics Covered:** Video 118 (Long term storage & Cache Concept)

* **Total Storage for 10 Years:**
    * $20 \text{ GB/day} \times 365 \text{ days} \times 10 \text{ years} = 73,000 \text{ GB}$.
    * Total = **73 TB (Terabytes)** data 10 saal mein.
* **Video 118: Capacity Estimation (Memory/Cache)**
    * **Concept:** "Why Cache is your secret weapon."
    * **Analogy:** Database se data access karna aisa hai jaise coffee shop mein lambi line mein khade hona.
    * **Cache:** Cache use karna aisa hai jaise aapka favorite drink counter par pehle se ready hai (waiting time khatam).

---

### **Page 8: Cache Calculation (From IMG_20251120_010440.jpg)**

**Topics Covered:** Video 118 (Cache Math)

* **Benefits of Cache:**
    1.  Speeding up search results.
    2.  Reducing stress on the database.
    3.  Delivers a smooth experience to users.
* **How much memory? (Calculation):**
    * Total storage of tweets/day = **20 GB**.
    * **Rule:** Hum mante hain ki **20%** (ya notes mein **5%** likha hai specific context ke liye) data "most frequently accessed" hota hai.
    * **Calculation:** $20 \text{ GB} \text{ ka } 5\% = 1 \text{ GB}$.
    * **Conclusion:** "Means keep things fast and responsive, we will need **1 GB of Cache memory per day** to store tweets/hashtags."
    * Ye data baar-baar access hota hai, isliye isse fast memory (RAM) mein rakhte hain.

---

### **Page 9 & 10: Why Quality Matters (Fuzzy Search) (From IMG_20251120_010401_1.jpg & IMG_20251120_010355_1.jpg)**

**Topics Covered:** Fuzzy Search & User Experience

* **Why all of these matter?**
    * Ek efficient search system sirf "exact match" dhundhna nahi hai.
    * System ko **Relevant**, **Timely**, aur **Intuitive** hona chahiye.
* **Fuzzy Search:**
    * **"Errors are forgiven":** Agar user spelling mistake kare, to bhi system ko samajhna chahiye.
    * **Example:**
        * User ne type kiya: "Quantom Compnting" (Wrong spelling).
        * System ne samjha: "Quantum Computing" (Correct result dikhaya).
    * User aksar jaldi mein typing errors karte hain ("typo"), lekin wo expect karte hain ki system sahi result dega.
    * **Significance:** Ye "Forgiving nature" search system ko user-friendly banata hai aur user experience ko improve karta hai.
    
    
Based on the additional images you provided, these notes continue the **System Design of a Search System (Twitter/X)**, covering **Videos 119 to 124**. The focus moves from estimation to API design, detailed data flow, Fuzzy search, and Ranking.

Here is the complete step-by-step extraction and conversion into **Hinglish**.

---

### **Page 1: Network Bandwidth - Incoming Data (From IMG_20251120_010446_1.jpg)**

**Topics Covered:** Video 119 (Network Bandwidth - Ingress)

* **Video 119: Capacity Estimation (Network Bandwidth)**
    * Humein ye calculate karna hai ki data ka flow (incoming aur outgoing) kaisa hoga.
    * **Incoming Data (Data flow in):**
        * **How much data flows in:** Kitna naya content create ho raha hai?
        * **Data Generated & Saved:** Humne pichle steps mein calculate kiya tha **20 GB/day**.
        * **Calculation:**
            * $20 \text{ GB} / \text{day}$
            * $20 \text{ GB} / (24 \times 60 \times 60 \text{ seconds})$.
            * Result $\approx$ **231 KB/s** (Notes mein *231 MB* likha hai, par calculation logic yehi hai).
        * **Conclusion:** Ye amount of fresh data system mein har second aa raha hai jo parse aur save karna hai.

* **Outgoing Data (Data flow out):**
    * **How much data flows out:**
        * Total searches: **500 Million searches/day**.
        * **Each search returns:** Approx **10 tweets**.
        * **Tweet size:** Approx **200 Bytes**.

---

### **Page 2: Network Bandwidth - Outgoing Data (From IMG_20251120_010449.jpg)**

**Topics Covered:** Video 119 (Network Bandwidth - Egress)

* **Calculation for Outgoing Data:**
    * $500 \text{ Million requests} \times 10 \text{ tweets} \times 200 \text{ Bytes}$.
    * Total = **100 GB/day** to **1 TB/day** range (Notes mein 1TB mention hai).
    * **Per Second Load:**
        * $1 \text{ TB} / (24 \times 60 \times 60)$.
        * Result $\approx$ **11.5 GB/second** (Notes ki calculation ke hisaab se heavy load hai).
    * **Conclusion:** "Tweet data being read and sent back to users through the search results."
    * Network bandwidth **4,231 MB per second** flowing into the system (Note: Values vary in rough estimation).

* **Why this matters?**
    * System ko massive data flows handle karne ke liye **proper bandwidth** ready rakhni padegi.
    * Agar bandwidth kam hui, to user ko "slow down" ya "lag" experience hoga jab wo search karega.

---

### **Page 3: API Design (From IMG_20251120_010454_1.jpg)**

**Topics Covered:** Video 120 (API Structure)

* **Video 120: API Design Search**
    * **Goal:** User ke search karne par server kya action perform karega.
    * Humein tweets ki list retrieve karni hai. Iske liye **GET method** use karenge (HTTP GET).
    * **API Endpoint:** `/v1/search`

* **Parameter Handling:**
    * Agar user space daalta hai (Example: "Space is here"), to URL mein space allowed nahi hota.
    * **URL Encoding:** Space replace ho jata hai `%20` se.
    * Example: `Space%20is%20here`.
    * Server is query ko decode karta hai aur process karta hai.

* **Response:**
    * Server response JSON format mein bhejta hai user ko wapas.

---

### **Page 4: High Level Design - Indexing Strategy (From IMG_20251120_010458_1.jpg)**

**Topics Covered:** Video 121 (Bad Design) & Video 122 (Good Design - Indexing)

* **Video 121: High Level Design - Search (Suboptimal)**
    * Ye samjhna zaroori hai ki humein kya **NAHI** karna hai.
    * **Bad Approach:** Agar hum simple SQL query use karein jo poore database ko scan kare (Scanning the entire database for keywords).
    * **Problem:** Ye waise hi hai jaise poore OS ya hard drive par bina index ke file dhundhna.
    * **Drawbacks:**
        1.  **Painfully Slow:** Bohot time lagega.
        2.  **Inefficient:** Resources waste honge.

* **Video 122: High Level Design - Search Indexing**
    * **Solution:** Hum kuch aur use karenge jise **Indexing** kehte hain.
    * **Concept:** Ye ek "Magic List" jaisa hai (Inverted Index).
    * Is list mein **Keywords** pehle se map hote hain un tweets ke saath jisme wo keyword aaya hai.
    * **Benefit:** Instantly humein wo tweets mil jate hain bina poora database scan kiye.
    * "This magic list exists and its called the **Index DB**."

---

### **Page 5: Fuzzy Search Introduction (From IMG_20251120_010511_1.jpg)**

**Topics Covered:** Video 123 (Fuzzy Search Concept)

* **Video 123: High Level Design (How to support Fuzzy Search)**
    * **Scenario:** "Why Indexing Rocks."
    * Humara system itna smart hona chahiye ki agar user **spelling mistake** bhi kare, to bhi sahi result mile.
    * **Example:**
        * User types: "Something wrong" (typo).
        * System gets: The right result.
    * Is "Big Giant Websites" feature ko hum **Fuzzy Search** kehte hain.
    * "That's the magic of fuzzy search."

---

### **Page 6: Complete User Journey - Step 1 & 2 (From IMG_20251120_010514.jpg)**

**Topics Covered:** Video 123 (Flow Steps 1-2)

* **Step 1: The Search Request**
    * **Scenario:** John (User) accidentally types a typo. He searches for "quantum cmputing" (unclear or ambiguous).
    * **Flow:**
        1.  John ki request **Load Balancer** ke through **API Gateway** par aati hai.
        2.  API Gateway request ko **validate** karta hai (ki sab kuch sahi format mein hai ya nahi).
    * If validated, request aage "Search Service" ko bheji jati hai.

* **Step 2: Search Service**
    * API gateway request ko **Search Service** ko forward karta hai.
    * Search Service ka kaam hai load ko distribute karna aur ensure karna ki request process ho.

---

### **Page 7: Complete User Journey - Step 3 (From IMG_20251120_010519.jpg)**

**Topics Covered:** Video 123 (Flow Step 3 - Correction)

* **Step 3: Query Correction (The Magic)**
    * Search Service dekhta hai ki "quantum cmputing" naam ka keyword exist nahi karta.
    * Wo **Query Correction Service** ko call karta hai.
    * **Process:**
        * Query Correction Service input leti hai ("cmputing").
        * Wo guess karti hai "Most likely correct word".
        * Output deti hai: **"Quantum Computing"**.
    * **Fun Fact:** Ye correction scenes ke peeche hoti hai. Algorithms (like Levenshtein distance) design kiye jate hain common typos aur spelling mistakes ko pakadne ke liye. 
    * **Step 4 (Part 1):**
        * Ab Search Service ko sahi keyword mil gaya hai.
        * Wo **Index Database** mein "Quantum" keyword search karta hai.

---

### **Page 8: Complete User Journey - Step 4 & 5 (From IMG_20251120_010506.jpg)**

**Topics Covered:** Video 123 (Flow Step 4-5)

* **Step 4 (Part 2): Retrieve IDs**
    * Index Database turant wo saare **Tweet IDs** return karta hai jinmein "Quantum" keyword hai.
    * *Example IDs:* 1002, 1003, 1005.
    * **Fetching Actual Content:**
        * Search Service ab in IDs (1002, 1003...) ke saath **Main Database** ke paas jata hai.
        * Wahan se actual tweet ka content (text, image url, user info) retrieve karta hai.

* **Step 5: Response**
    * Search Service ye tweets **John** (User) ko wapas bhej deta hai.
    * John ko lagta hai system ne typo samajh liya, par peeche ye poora process hua.

---

### **Page 9: Recap of the Flow (From IMG_20251120_010503_1.jpg)**

**Topics Covered:** Recap of the Search Process

* **Example Recap:**
    * **Scenario:** John searches for "Quantum Computing" on Twitter.
    * **Instant Process:**
        1.  **API Gateway:** Checks and validates request.
        2.  **Search Service:** Moves forward.
        3.  **Index DB:** Instead of checking every single tweet (which is impossible fast), it checks the Index.
        4.  **Result:** Instantly gives all the tweet IDs that contain "Quantum Computing".
        5.  **Explanation:** Because in search, lots of keywords and all can be searched, so making an **Index of every search keyword is possible**.
    * Is tarah se hum "Hogwarts" style magic create karte hain jahan user ko wait nahi karna padta.

---

### **Page 10: High Level Design - Ranking (From IMG_20251120_010521_1.jpg)**

**Topics Covered:** Video 124 (Ranking Service)

* **Video 124: High Level Design (Ranking)**
    * **Problem:** Index Database ne bohot saare tweets return kar diye jinmein keyword tha. Par user ko sabse upar kya dikhana hai?
    * **Solution:** **Ranking Service**.
    * Index database quickly returns the tweets containing both keywords.
    * **Ranking Logic:**
        * Ye "Sorting Hat of Hogwarts" ki tarah hai.
        * Ye service ensure karti hai ki **Relevant** aur **Important** tweets sabse upar dikhein.
    * **Process:**
        1.  Search Service results ko Ranking Service ko bhejta hai.
        2.  Ranking Service unhe sort karti hai (based on likes, recency, relevance).
        3.  Sorted list user ko milti hai.
    * **Explanation:** Explain how to do this for any Ecommerce website having 100 users. (Ye concept e-commerce product search mein bhi same apply hota hai).
    
    
Based on the new images you provided, these notes cover the **Deep Dive into Search System**, specifically focusing on **Query Correction, Data Modeling (Indexing), and Elastic Search** (Videos 125 to 129).

Here is the complete extraction and conversion into **Hinglish**.

---

### **Page 1: Query Correction & Data Modeling Intro (From IMG_20251120_010528_1.jpg)**

**Topics Covered:** Video 125 (Query Correction Logic), Video 126 (DB Selection), Video 127 (Data Modeling Intro)

* **Video 125: Deep Dive Insights - Query Correction**
    * **Fun Fact:** Query Correction algorithms bilkul humare **Spell Checkers** ki tarah hote hain.
    * **How it works:** Ye algorithms specific common typos (types) aur mistakes ko pehchanne ke liye **train** kiye jate hain taaki wo unhe **Real Time** mein fix kar sakein.
    * *Example:* Agar user "Ipone" likhe, to system real-time mein samajh jaye ki wo "Iphone" dhoondh raha hai.

* **Video 126: High Level Design Search (Final Design)**
    * Is video mein hum **Database Selection** par final decision le rahe hain.
    * Humein decide karna hai ki kaunsa database search ke liye best rahega (SQL vs NoSQL vs Specialized Search DB).

* **Video 127: Data Modeling**
    * **Goal:** "To make the search fast." (Search ko tez banana).
    * **Strategy:** Hum important fields ki **Indexing** karenge.
    * **Example:** Sabse common search hoti hai **Tweet ID** ke basis par, isliye humein Tweet ID ko index karna padega.

---

### **Page 2: Detailed Data Modeling (From IMG_20251120_010536.jpg)**

**Topics Covered:** Video 127 (Tweet DB vs Index DB)

* **Tweet Database (Storage):**
    * Ye wo jagah hai jahan saare tweets actually store hote hain.
    * **Schema Fields:**
        * `TweetID`: Unique ID.
        * `Text`: Tweet ka content.
        * `UserID`: Kisne tweet kiya.
        * `CreatedAt`: Kab tweet kiya.
    * **Optimization:** "Most common query is to find the tweet by tweet id."
    * Is query ko fast karne ke liye hum `TweetID` field par **Index** banate hain.
    * **Analogy:** Ye index ek **Shortcut** ki tarah kaam karta hai taaki Tweet ID se tweet turant mil jaye.

* **Index Database (Search Optimization):**
    * Ye alag database hai jo searching ke liye use hota hai.
    * **Definition:** "The Index DB is a place where we store the **map of keywords, hashtags**."
    * **Structure:**
        * `Keyword` -> `TweetIDs`
        * *Example:* `{"Coding": [101, 105, 199]}`
    * Iska matlab agar koi "Coding" search karega, to system ko turant pata chal jayega ki ye keyword Tweet ID 101, 105 aur 199 mein hai.
    * *Note:* "Explain all these step by step properly." (Lecture mein is flow ko detail mein samjhaya gaya hai).


---

### **Page 3: Implementation & Elastic Search (From IMG_20251120_010541_1.jpg)**

**Topics Covered:** Video 128 (Code Implementation), Video 129 (Elastic Search)

* **Video 128: Deep Dive Query Correction Service**
    * **Practical Coding:** "How to write Query Correction Service in **Express JS**."
    * Is video mein hum code likh kar samjhenge ki backend mein ye logic kaise implement hota hai.
    * **Application:** Explain karna hai ki kaise ek **Small Ecommerce Web App** mein is feature ko use kiya ja sakta hai (e.g., Product search correction).

* **Video 129: Deep Dive Insights - Elastic Search**
    * **What is Elastic Search?**
        * Ye "Elastic charge super charge of search engine" hai. (Basically, ye search engines ke liye ek booster hai).
        * Ye specially design kiya gaya hai **Massive amount of Data** ko handle karne ke liye.
        * Ye **Real Time Search Results** deliver karta hai.
    * **Implementation:**
        * "Explain this - how to code or use any package in **Node JS**."
        * Developers Node.js mein Elastic Search ka package use karke ise easily integrate kar sakte hain.
        
=============================================================

Based on the images you provided, these notes cover **Section 8: Design Airbnb (Booking System)**. The topics range from **Video 130 to 149**, covering Requirements, Capacity Estimation, API Design, Data Modeling, and specifically handling **Concurrent Bookings (Locking Mechanisms)**.



### **Page 1: Introduction to Airbnb Design (From IMG_20251120_010548.jpg)**

**Topics Covered:** Video 130, 131, 132 (Requirements & Capacity Intro)

* **Section 8 -> Design Airbnb**
    * Airbnb ek complex system hai jo sirf booking nahi karta, balki typos handle karta hai aur search results ko relevance ke basis par sort karta hai.
    * **Video 130: Deciding Requirements (Functional)**
        * Humein ye define karna hai ki Airbnb exactly hai kya aur ye real world ki kaunsi problem solve karta hai.
        * Iske core features kya honge? (Search, Booking, Listings).
    * **Video 131: Deciding Requirements (Non-functional)**
        * System ki performance, scalability aur consistency requirements kya hongi.
    * **Video 132: Capacity Estimation (DAU/MAU)**
        * Daily Active Users aur Monthly Active Users ka estimation lagana hai taaki scale plan kar sakein.

---

### **Page 2: Capacity Estimation - Storage Calculation (From IMG_20251120_010554_1.jpg)**

**Topics Covered:** Video 133, 134 (Throughput & Storage)

* **Video 133: Capacity Estimation - Throughput**
    * **Write per Second:** System mein kitna naya data aa raha hai.
    * **Read per Second:** Kitne log data read kar rahe hain (Searching/Viewing).
* **Video 134: Capacity Estimation - Storage**
    * Humein **Each Property Data** ka size calculate karna hai.
    * **Calculation Breakdown:**
        1.  **Description:** Text details $\approx 10 \text{ KB}$.
        2.  **Metadata:** Location, price, rules $\approx 4 \text{ KB}$.
        3.  **Images:** High quality photos $\approx 450 \text{ KB}$.
    * **Total per Property:** $10 + 4 + 450 \approx 500 \text{ KB}$ (approx).
    * Iske basis par hum **Each Booking Data** ka load calculate karenge.

---

### **Page 3: Memory & Network Estimation (From IMG_20251120_010557_1.jpg)**

**Topics Covered:** Video 135, 136, 137 (Cache, Network, API Intro)

* **Video 135: Capacity Estimation - Memory (Cache)**
    * **Assumption:** Hum daily data ka **5%** cache memory mein store karenge (frequently accessed listings).
    * Jaise-jaise system ka size increase hoga, memory size requirement bhi increase hogi.
* **Video 136: Capacity Estimation - Network Bandwidth**
    * **Ingress:** Incoming traffic/data upload speed.
    * **Egress:** Outgoing traffic/data download speed (Images load hona, search results aana).
* **Video 137: API Design - Add Property**
    * **User:** Property Owner.
    * **Action:** Owner Airbnb servers par apni property add kar raha hai.
    * **Method:** HTTP POST (add property details).
    * **Endpoint:** `/api/v1/properties` (Example).

---

### **Page 4: API Design - Detailed Endpoints (From IMG_20251120_010604.jpg)**

**Topics Covered:** Video 138, 139, 140, 141 (Core APIs)

* **Video 138: API Design - View Bookings**
    * **User:** Property Owner.
    * **Goal:** Apni properties ki bookings dekhna.
    * **Method:** HTTP GET `/bookings`.
* **Video 139: API Design - Search Properties**
    * **User:** Guest.
    * **Goal:** Search box mein query type karke properties dhoondhna.
    * **Method:** HTTP GET `/search?q=location`.
* **Video 140: API Design - View Property**
    * **User:** Guest (Property details dekhna).
* **Video 141: API Design - Book Property**
    * **User:** Guest (Final booking karna).
    * "Explain all this" - In sabke request/response structure ko samjhna hai.

---

### **Page 5: High Level Design - Elastic Search (From IMG_20251120_010606_1.jpg)**

**Topics Covered:** Video 143 (Search Tech), Skipped Videos (142, 144-147)

* **Video 142:** Not of use (skipped).
* **Video 143: High Level Design - Search Properties**
    * Searching ke liye hum **Elastic Search** use karte hain.
    * **Question:** "How to use this in General Ecommerce web app which is hosted on VPS?"
    * **Scenario:** Agar aapke paas koi **Ecommerce website** hai ya **Open Source Classic Search** chahiye, to Elastic search best option hai complex queries handle karne ke liye.
* **Video 144 - 147:** Not of use (skipped as per notes).

---

### **Page 6: Data Modeling (From IMG_20251120_010614.jpg)**

**Topics Covered:** Video 148 (Database Schema)

* **Video 148: Deep Dive Insights - Data Modeling**
    * Humein database tables design karne hain.
    * **Properties DB:**
        * Fields: `Name`, `Desc`, `Image`, `OwnerID`, `AvailabilityStartDate`, `Price`.
    * **Booking DB:**
        * Tables: `Bookings`, `Properties`, `Guests`.
    * Isme relationships define karni hain (One owner has multiple properties, One property has multiple bookings).

---

### **Page 7: Handling Concurrent Bookings - The Problem (From IMG_20251120_010618_1.jpg)**

**Topics Covered:** Video 149 (Concurrency Issue & Pessimistic Locking)

* **Video 149: Handling Concurrent Bookings**
    * **Problem:** "Both people booked the property at the same time."
    * Agar do log ek hi time par same property book karne ki koshish karein to kya hoga? Ise **Concurrent Booking** problem kehte hain.
    * **Solution 1: Pessimistic Locking (Mechanism Locking)**
        * Is approach mein hum database ko **Lock** kar dete hain jab koi ek user booking kar raha hota hai.
        * **Process:** If I block the other requests by putting the lock on the database...
        * Ye assume karta hai ki conflict hoga hi hoga (Pessimistic view).
        * 
---

### **Page 8: Optimistic Locking Strategy (From IMG_20251120_010626.jpg)**

**Topics Covered:** Video 149 (Optimistic Locking Concept)

* **Issues with Pessimistic:**
    * Agar ek request ne DB lock kar diya, to baaki saare requests ko **Wait** karna padega.
    * Isse **Delay** badh jata hai aur system slow ho jata hai.
* **Solution 2: Optimistic Locking (Better Approach)**
    * **Mindset:** Hum problem ko "Optimistic Mindset" se approach karte hain.
    * **Idea:** "Allow all the request to go through without blocking."
    * Hum pehle se kisi ko nahi rokenge. Confirmation se bilkul pehle ek **Quick Check** karenge.
* **Example:**
    * Hum **Bob** aur **Smith** dono ki requests ko allow kar dete hain.
    * Bob ki request pehle process ho gayi aur booking create ho gayi.
    * Ab Smith ki request process ho rahi hai...

---

### **Page 9: Conflict Resolution (From IMG_20251120_010634.jpg)**

**Topics Covered:** Video 149 (Handling the Conflict)

* **Finalizing Smith's Request:**
    * Smith ki booking create karne se just pehle, hum Database mein check karte hain.
    * Humein pata chalta hai ki **Bob** ne already wo dates book kar li hain.
    * **Action:** Just before confirming and committing Smith's transaction, we would **REJECT Smith's Request**.
    * Isse duplicate bookings avoid ho jati hain.
* **Benefit:**
    * Iska faayda ye hai ki system ka **throughput choke nahi hota** (rukti nahi hai processing).
    * Hum parallel mein sab kuch process kar sakte hain aur sirf end mein "Double Check" karte hain.
    * Waiting time khatam ho jata hai.

---

### **Page 10: Conclusion on Locking (From IMG_20251120_010639_1.jpg)**

**Topics Covered:** Video 149 (Summary)

* **Why Optimistic is best for Airbnb?**
    * Ye system "Fail fast" karta hai lekin blockage create nahi karta.
    * It finds it doesn't commit that transaction (agar conflict mila).
    * **Result:** "Higher Throughput and Better Performance."
    * Khaaskar **High Traffic Situations** mein (jaise Airbnb or Ticket booking), ye approach best hai.
* **Definition:** Ise **Optimistic** isliye kehte hain kyunki ye assume karta hai ki "Most of the things will go smoothly without Conflicts" (Zyadatar transactions bina ladayi ke ho jayenge).
* So, Optimistic locking helps handle more requests in less time while ensuring **Data Integrity**.


Based on the image provided, this is the final page of your notes covering **Video 150**, which explains a specific optimization technique used in systems like Airbnb or Instagram for handling file uploads efficiently.

Here is the step-by-step extraction and conversion into **Hinglish**.

---

### **Page 1: Deep Dive - Pre-signed URLs (From IMG_20251120_010643.jpg)**

**Topics Covered:** Video 150 (Pre-signed URLs & Direct Uploads)

* **Video 150: Deep Dive Insights (Pre-signed URLs)**
    * **Question:** "What it is, where it is used and all."
    * Ye concept samjhna bohot zaroori hai jab hum images ya videos handle karte hain.

* **What are Pre-signed URLs?**
    * **Definition:** "Pre-signed URLs are special URLs that allow users to upload **directly to the object storage**."
    * Matlab, bajaye iske ki file pehle server par jaye aur fir server use database mein daale, user seedha storage (jaise AWS S3) par upload karta hai.
    * **How it works:**
        1.  Client server se permission mangta hai.
        2.  "Once the client receives the pre-signed URLs it has some **temporary permissions** to upload their content."
        3.  Client ke paas ek limited time ke liye permission aa jati hai file upload karne ki.

* **Constraint:**
    * "The pre-signed URL has a **time limit** to upload."
    * Ye URL hamesha ke liye valid nahi hota, kuch der baad expire ho jata hai.

* **Why do we need Pre-signed URLs?**
    * **Reason 1: Faster Upload**
        * "When client uploads directly to the object storage it **doesn't bother the server**."
        * Server free rehta hai kyunki heavy lifting (file uploading) directly storage handle kar raha hai.
        * "It is the system which is different from the servers." (Object storage server se alag hota hai).
        * **Result:** "This makes whole upload system fast." (Isse poora system fast ho jata hai).
    * **Reason 2: Security**
        * "The second reason is **Secure and temporary access**."
        * Kyunki URL expire ho jata hai, to koi uska misuse nahi kar sakta baad mein.




=============================================================


Based on the images provided, these notes cover **Section 9: Design Notification System**. They range from **Video 151 to 170**, covering everything from requirements and capacity estimation to High-Level Design (HLD), Decoupling using Queues, and Data Modeling.



### **Page 1: Introduction to Notification System (From IMG_20251120_010648_1.jpg)**

**Topics Covered:** Video 151, 152 (Intro & Need)

* **Section 9 -> Design Notification System**
* **Video 151: Introduction**
    * **What is a Notification System?**
        * Humein samajhna hai ki ye system kya hai aur kahan use hota hai.
        * "What it is, where it is used and all." (Jaise Amazon order update, WhatsApp message alert).

* **Video 152: Introduction - Why do we need it?**
    * Humein notification system ki zaroorat kyun hai?
    * **Key Reasons:**
        1.  **Timely Alert:** User ko turant inform karne ke liye (Example: OTP, Transaction alert).
        2.  **Engagement:** User ko app par wapas laane ke liye.
        3.  **User Experience:** User ko important updates dene ke liye.

---

### **Page 2: Requirements - Functional (From IMG_20251120_010651_1.jpg)**

**Topics Covered:** Video 153 (Types & Features)

* **Video 153: Deciding Requirements (Functional)**
    * **Core Requirements:**
        1.  **Send Notifications:** System notification bhej sake.
        2.  **Users:**
            * **Sender:** Kaun notification bhej raha hai (System ya Admin).
            * **Receiver:** Kisko mil raha hai (End User).
    * **Notification Types:** System ko 3 types handle karne chahiye:
        * **SMS**
        * **Email**
        * **App Notifications** (Push Notifications)
    * **Advanced Features:**
        * **Rate Limiting:** Spam rokne ke liye.
        * **Prioritization:** Important messages pehle jayein (OTP > Promotional).
        * **Validation:** Data sahi hai ya nahi.
        * **User Preferences:** User ne kya opt kiya hai (Email chahiye ya nahi).

---

### **Page 3: Non-Functional & Capacity Intro (From IMG_20251120_010657_1.jpg)**

**Topics Covered:** Video 154, 155, 156 (Quality Attributes & Throughput)

* **Video 154: Deciding Requirements (Non-Functional)**
    * System ki qualities kya honi chahiye:
        1.  **High Availability:** Notification service hamesha up honi chahiye.
        2.  **Low Latency:** Notification turant pahunchna chahiye.
        3.  **Scalability:** Millions of users ko handle kar sake.
        4.  **Reliability:** Message lost nahi hona chahiye.
        5.  **Flexibility:** Naye channels (like WhatsApp) easily add ho sakein.

* **Video 155: Capacity Estimation (DAU/MAU)**
    * Hum **Daily Active Users** aur **Monthly Active Users** ka data use karke system ka scale decide karenge.

* **Video 156: Capacity Estimation - Throughput**
    * Humein calculate karna hai ki Notification Service par **Write** (Sending request) aur **Read** (Status check) ka load kitna hoga.

---

### **Page 4: Capacity Estimation - Storage (From IMG_20251120_010700_1.jpg)**

**Topics Covered:** Video 157 (Storage Math)

* **Video 157: Capacity Estimation - Storage**
    * Humein Notification Server ke liye storage calculate karni hai.
    * **Data Types:**
        1.  **User Info Data:** User ki details.
        2.  **User Preferences Data:** User ne kya settings ki hain.
        3.  **Notification Data:** Actual message content.
    * **Assumption:**
        * Email: 30%
        * Push: 40%
        * SMS: 30%
        * Average size per notification $\approx$ **1 KB (Kilo Bytes)**.
    * **Calculation:** Total users $\times$ Notifications per day $\times$ Size (5 KB approx load per user activity).
    * Is tarah hum total storage requirement nikaal sakte hain.

---

### **Page 5: Memory, Network & API Design (From IMG_20251120_010707_1.jpg)**

**Topics Covered:** Video 158, 159, 160 (Cache & API)

* **Video 158: Capacity Estimation (Memory)**
    * **Cache Memory:** Frequently accessed data (jaise User Preferences) ko fast access ke liye cache mein rakhenge.

* **Video 159: Capacity Estimation (Network Bandwidth)**
    * Kitna data network par flow karega (Incoming requests vs Outgoing notifications).

* **Video 160: API Design - Send Notification**
    * **Goal:** Notification bhejne ke liye API structure.
    * **Method:** HTTP POST (Recommended).
    * **Endpoint:** `/v1/send/notification` (Example).
    * **HTTP Body:**
        * `userId`: Kisko bhejna hai.
        * `from`: Kisne bheja.
        * `message`: Content kya hai.
        * `type`: Email/SMS/Push.
        * `priority`: High/Low.
        * `time`: Scheduling time.

---

### **Page 6: Basic High Level Design (From IMG_20251120_010711_1.jpg)**

**Topics Covered:** Video 161 (The Flow - iOS/Android)

* **Video 161: Basic High Level Design**
    * **Service:** Hamari service directly user ke phone par message nahi bhejti. Wo intermediate services (Third-party providers) se connect karti hai.
    * **For Apple (iOS):**
        * Hum **APNS** (Apple Push Notification Service) se connect karte hain.
        * Flow: Our Service -> APNS -> User's iPhone.
    * **For Android:**
        * Hum **FCM** (Firebase Cloud Messaging) se connect karte hain.
        * Flow: Our Service -> FCM -> User's Android Phone.
    * **Delivery Confirmation:** Ye services humein wapas batati hain ki message deliver hua ya nahi.


---

### **Page 7: Problems with Basic Design (From IMG_20251120_010717_1.jpg)**

**Topics Covered:** Video 162 (Challenges)

* **Video 162: High Level Design (Problems)**
    * Basic design mein kuch issues hain:
        1.  **Prioritization and Validation:** Har message ko validate karna zaroori hai.
        2.  **Rate Limiting to avoid Spam:** Agar system hack ho gaya ya glitch aaya, to user ko thousands of messages nahi jaane chahiye (Spamming prevent karna).
        3.  **Filter based on Preferences:** Agar user ne kaha hai "No Email", to email nahi jaana chahiye.
    * "Explain all these." (In sabko handle karna padega).

---

### **Page 8: Improving Design - Validation & Preferences (From IMG_20251120_010721_1.jpg)**

**Topics Covered:** Video 163, 164, 165 (Solutions)

* **Video 163: HLD - Validation & Prioritization**
    * OTPs ko high priority deni hai aur Marketing ko low.
* **Video 164: HLD - Rate Limiting**
    * Ek user ko limited notifications hi bhejein (e.g., Max 5 per minute).
* **Video 165 (marked as 164): Adjusting to User Preferences**
    * **Importance:** "User preferences play a crucial role."
    * Ye ensure karta hai ki user ko wahi mile jo usne maanga hai.
    * **Example:** "If user opts for Email notification, user will get **only Email** notification."
    * Hum unnecessary SMS bhej kar paise waste nahi karenge.

---

### **Page 9: Advanced HLD - Decoupling (From IMG_20251120_010727_1.jpg)**

**Topics Covered:** Video 166, 167, 168 (Parallel Processing & Queues)

* **Video 166: Handling Different Notification Types**
    * Different protocols (SMTP for email, SMPP for SMS) aur requirements hoti hain.
    * **Problem:** Lack of Parallel processing in basic design. Sab kuch line mein laga rehta hai.

* **Video 167 & 168: Reorganizing & Decoupling**
    * **What is Decoupling?** Components ko alag karna taaki ek ke fail hone par doosra na ruke.
    * **Solution:** **Message Queue** use karna (RabbitMQ, Kafka).
    * **Process:**
        1.  Main Service notification ko **Queue** mein daal deti hai.
        2.  Workers (Notification servers) queue se pick karke process karte hain.
    * Isse system fast aur reliable banta hai.


---

### **Page 10: Deep Dive - Database & Modeling (From IMG_20251120_010735_1.jpg)**

**Topics Covered:** Video 169, 170 (DB Choice & Schema)

* **Video 169: Deep Dive - Database Selection**
    * Hum **SQL** aur **NoSQL** dono use kar sakte hain based on data type.
    * **User Info:** Structured data (SQL like MySQL/PostgreSQL).
    * **User Preferences/Logs:** Large volume, flexible data (NoSQL like MongoDB/Cassandra).

* **Video 170: Deep Dive - Data Modeling**
    * **User Info DB:**
        * `userId`, `name`, `email`, `phoneNumber`, `isActive`, `createdAt`, `updatedAt`.
    * **User Preference DB:**
        * `userId`, `preferenceType` (e.g., email_marketing: false, sms_alert: true).
    * **Application:**
        * Explain karna hai ki ye setup **Microservice architecture** mein kaise fit hota hai vs Monolithic e-commerce app mein.
        * Large scale (millions of users) ke liye NoSQL preferences store karna better hai efficiency ke liye.
        
        
=============================================================

🛠 1. Advanced Distributed System Concepts (The "Hard" Stuff)
Aapke notes mein "Concept" hai, par "Implementation Detail" miss ho sakti hai.

Distributed Transactions (Saga Pattern & 2PC):

Kyun Zaruri Hai: Airbnb design mein aapne "Booking" dekhi. Par agar Payment fail ho jaye toh Booking cancel kaise hogi across microservices?

Topic: Two-Phase Commit (2PC) (Old way) vs Saga Pattern (New way - Choreography/Orchestration).

Consensus Algorithms (Paxos & Raft):

Kyun Zaruri Hai: TinyURL mein aapne Zookeeper use kiya. Par Zookeeper khud kaise decide karta hai ki leader kaun hai?

Topic: Leader Election kaise hoti hai distributed system mein.

Consistent Hashing (Deep Dive):

Kyun Zaruri Hai: Notes mein mention hai, lekin Virtual Nodes ka concept aur Data Rebalancing kaise hoti hai jab server add/remove hota hai, ye detail interview mein puchi jati hai.

📍 2. Specialized Data Structures (Jo specific designs mein chahiye)
Aapke notes mein SQL/NoSQL/ElasticSearch hai. Par kuch specialized structures missing hain:

Geo-Spatial Indexing (QuadTree / Geohash):

Kahan use hoga: Uber / Ola / Google Maps / Tinder.

Scenario: "Show all PGs near me within 5km." SQL mein WHERE distance < 5 karna bahut slow hota hai. Iske liye QuadTree use hota hai.

Bloom Filters:

Kahan use hoga: Database & Cache.

Scenario: Server ko DB check karne se pehle ye pata karna hai ki kya data exist karta hai ya nahi (taaki DB par load na pade). Ye "No" bahut fast bolta hai.

Count-Min Sketch / HyperLogLog:

Kahan use hoga: YouTube View Count.

Scenario: Jab billions of views ho, toh exact count rakhna mushkil hai. Ye approximate counting algorithms hain.

🛡 3. Resiliency & Failure Patterns (System tootne par kya karein?)
Aapne "Fault Tolerance" padha, par specific patterns missing hain:

Circuit Breaker Pattern:

Scenario: Agar Payment Service down hai, toh Order Service ko baar-baar request bhej kar wait nahi karna chahiye. Circuit "Open" kar dena chahiye taaki system fail fast kare.

Bulkhead Pattern:

Scenario: Agar "Image Upload" service slow hai, toh uski wajah se "Login" service slow nahi honi chahiye. Dono ko alag-alag pools mein rakhna.

Retry & Exponential Backoff:

Scenario: Jab network fail ho, toh turant retry mat karo. Pehle 1 sec wait karo, fir 2 sec, fir 4 sec. (Jitter ke saath).

🔐 4. Security (Briefly touched, needs detail)
OAuth 2.0 / OIDC / JWT:

System Design mein aksar puchte hain: "User authentication flow kaise kaam karega across microservices?"

HTTPS/TLS Handshake:

Data encrypt kaise hota hai wire par.

🏗 5. Missing Popular Design Problems (Jo aksar puche jate hain)
Aapne major wale cover kiye hain, par ye 3 bahut common hain jo missing hain:

Design Uber/Ola (Ride Sharing):

Isme Geo-Spatial Indexing aur Driver Matching Logic kaafi important hai.

Design Google Docs (Collaborative Editing):

Isme WebSockets ke saath OT (Operational Transformation) ya CRDTs concept aata hai (ki do log ek sath type karein toh conflict kaise resolve ho).

Design Web Crawler (Google Search Bot):

Internet se billions pages kaise crawl karein, links kaise parse karein, aur duplicate content kaise avoid karein.


=============================================================



### 📊 1. Analytics & Data Warehousing (OLTP vs OLAP)
Aapke notes mein abhi tak **Operational Databases (OLTP)** par focus hai (jaise User login, Booking save karna). Lekin companies puchti hain: *"Business Intelligence kaise nikaloge?"*

* **Concept:** Transactional DB (PostgreSQL) ko Analysis ke liye use nahi karte (kyunki wo slow ho jayega).
* **ETL Pipelines:** Data ko Main DB se nikaal kar Data Warehouse mein daalna.
* **OLAP Databases:** Snowflake, Amazon Redshift, ya BigQuery.
* **Apply to Smart PG:** "Owner ko dashboard dikhana hai ki pichle 1 saal mein kitna revenue aaya aur kaunsa maheena sabse slow tha." Iske liye **Batch Processing** aur **Data Warehousing** chahiye.

---

### 🕵️ 2. Observability & Distributed Tracing
Jab system mein 50 Microservices honge, aur koi User bole "Mera payment fail ho gaya", toh aapko kaise pata chalega galti kahan hui? Logs padhna kaafi nahi hai.

* **Distributed Tracing:** Har Request ko ek `Unique-ID` dena jo saare microservices mein pass ho. (Tools: **Jaeger**, **Zipkin**).
* **Metrics & Monitoring:** CPU high hai ya Memory leak ho rahi hai? (Tools: **Prometheus**, **Grafana**).
* **Apply to Smart PG:** Agar Tenant bole "App slow chal raha hai", toh aap Tracing se dekhoge ki kya **API Gateway** slow hai ya **Database** query time le rahi hai.

---

### 🚀 3. Deployment Strategies (Zero Downtime)
System Design sirf code likhna nahi hai, code ko **Live** karna bhi hai bina site band kiye. Interviewer puchega: *"Naya feature release karte waqt site down hogi kya?"*

* **Blue-Green Deployment:** Do server groups rakho (Blue = Old, Green = New). Traffic switch kar do.
* **Canary Deployment:** Naya update pehle sirf 1% users ko dikhao. Agar sab sahi raha, toh baaki 99% ko.
* **Apply to Smart PG:** Jab aap "Chat Feature" launch karein, toh pehle sirf Delhi ke users (Canary) ko dikhayein test karne ke liye.

---

### ☁️ 4. Modern Architectures (Serverless & Edge)
Aajkal sab kuch servers par nahi hota.

* **Serverless (AWS Lambda):**
    * *Kahan use karein:* Image resizing (Smart PG photos), PDF generation (Rent Agreement). Server 24/7 run karne ki zarurat nahi, jab kaam ho tabhi chalega.
* **Edge Computing / Edge Caching:**
    * Processing ko user ke paas le aana (CDN ke logic jaisa, par computation ke liye).

---

### 🔒 5. Advanced Security (Specific Attacks)
Basic Auth (JWT) aapne likh liya hoga. Par ye 3 cheezein pata honi chahiye:

* **DDoS Mitigation:** Agar koi hacker fake traffic bhej kar server down karna chahe toh? (Solution: WAF - Web App Firewall).
* **SQL Injection & XSS:** Input sanitization kaise karein.
* **Salting & Hashing Passwords:** Passwords ko plain text mein save nahi karte. (Bcrypt use karte hain).

---

### ✅ Final Checklist for Your Notes
Agar aapne ye niche diye gaye topics bhi likh liye, toh **kuch bhi missing nahi hai**.

1.  **OLTP vs OLAP** (Data Warehouse concept).
2.  **Distributed Tracing** (Request ID concept).
3.  **Blue-Green / Canary Deployment** (Release strategy).
4.  **Serverless Functions** (AWS Lambda use cases).
5.  **DDoS & WAF** (Security layer).



=============================================================

1. Idempotency (Bahut Zaroori for Payments)
System Design mein sabse badi galti hoti hai jab user "Pay Now" par 2 baar click kar de aur paise 2 baar kat jayein.

Concept: Idempotency ka matlab hai: "Ek request ko chahe 1 baar process karo ya 100 baar, result same hi hona chahiye."

Implementation:

Client har request ke saath ek unique idempotency_key (UUID) bhejta hai.

Server check karta hai: "Kya maine ye Key pehle process ki hai?"

Agar haan, toh wahi purana result return karo, dobara process mat karo.

Smart PG Use Case: Rent payment ke liye bahut critical hai.

📍 2. Service Discovery (Microservices ka GPS)
Aapne likha hai "Microservices". Lekin Service A ko kaise pata chalega ki Service B ka IP Address kya hai? (Kyunki cloud mein IP change hote rehte hain).

Problem: Hardcoded IP addresses use nahi kar sakte.

Solution: Service Discovery (Client-side vs Server-side).

Use tools like Consul, Etcd, or Netflix Eureka.

Process: Jab Service B start hoti hai, wo apna IP "Service Registry" (Phonebook) mein likhwati hai. Service A wahan se number dhoondhti hai.

📦 3. Data Serialization (JSON vs Protobuf)
Ab tak aapne API design mein JSON use kiya hai. Lekin jab millions of requests aati hain, JSON slow ho jata hai (kyunki ye text-based hai aur size bada hota hai).

Protocol Buffers (Protobuf) / Avro:

Ye data ko Binary Format (0s aur 1s) mein convert karte hain.

Ye JSON se chhota aur fast hota hai.

gRPC (jo aapne pehle note kiya tha) isi ko use karta hai internally.

Smart PG Use Case: Microservices aapas mein baat karne ke liye Protobuf use karein, aur Frontend se baat karne ke liye JSON.

💾 4. Event Sourcing & CQRS (Advanced Data Pattern)
Ye thoda complex hai par bahut powerful hai.

CQRS (Command Query Responsibility Segregation):

Database ko 2 hisson mein tod do:

Write Database: Sirf data likhne ke liye.

Read Database: Sirf data padhne ke liye.

Event Sourcing:

Bajaye "Current State" store karne ke (e.g., Balance = 500), hum Saare Events store karte hain (e.g., +100, -50, +200).

Balance calculate karne ke liye saare events ko replay kiya jata hai.

Why? Audit logs ke liye best hai. (Bank transactions aise hi kaam karte hain).

🔥 5. Disaster Recovery (DR) Strategies (Agar Data Center Jal Jaye toh?)
High Availability (HA) ka matlab hai server crash hone par backup chalana. Disaster Recovery (DR) ka matlab hai agar poora AWS Region (Mumbai) down ho jaye toh kya hoga?

RPO (Recovery Point Objective): Kitna data loss hum bardasht kar sakte hain? (e.g., Last 5 mins).

RTO (Recovery Time Objective): System ko wapas online aane mein kitna time lagna chahiye? (e.g., 1 hour).

Strategies:

Active-Active: Do alag regions mein system chalu hai (Mumbai & Singapore).

Active-Passive: Mumbai mein chalu hai, Singapore mein backup ready hai par off hai.

🕷 6. Webhooks (Push vs Pull)
Aapne Polling aur WebSockets dekha. Webhooks third-party systems ke liye bahut zaruri hain.

Concept: Jab humein baar-baar server se puchna na pade "Kaam hua kya?", balki server khud humare URL par data bhej de.

Smart PG Use Case: Jab Payment Gateway (Razorpay) par payment success ho jaye, toh Razorpay aapke server ke ek URL par Webhook bhejega confirm karne ke liye.


=============================================================

Haan, ab tak aapne jo notes banaye hain wo **"Backend/Server-Side System Design"** ke liye **100% complete** hain. Aap Google/Amazon ka backend design kar sakte hain.

Lekin aapne **Android Apps, Windows Software, aur Games** ka zikr kiya. Inke liye **"Client-Side System Design"** ke concepts bilkul alag hote hain jo abhi tak aapke notes mein **Missing** hain.

Agar aapko ek complete Architect banna hai jo Server ke saath-saath **App aur Game** bhi design kare, toh ye rahi **Final List of Missing Topics** (Client & Game Architecture):

---

### 📱 1. Mobile & Client System Design (Android/iOS)
Server par data safe hai, par agar user ke phone mein internet chala jaye toh?

* **Offline-First Architecture:**
    * *Concept:* App bina internet ke chalna chahiye. Data pehle Local Database (SQLite/Room) mein save hota hai, phir background mein Server par sync hota hai.
    * *Smart PG Use Case:* Tenant basement mein hai (No Network), usne "Complaint" add ki. App usse save kar le aur jaise hi net aaye, upload kar de.
* **Synchronization & Conflict Resolution:**
    * *Problem:* User A ne offline hokar "Profile Photo" change ki. User B ne online hokar "Profile Photo" change ki. Jab A online aayega toh kaunsi photo rahegi?
    * *Strategy:* Last-Write-Wins ya Manual Merge.
* **Deep Linking:**
    * *Concept:* Ek URL (`smartpg://room/101`) par click karne se seedha App ka specific page khulna.
* **Push Notification Handling (Client Side):**
    * Server se message aa gaya, par App usse kaise dikhayega? (Foreground vs Background handling).



---

### 💻 2. Desktop & Software Architecture (Windows/Linux/macOS)
Desktop apps mobile se alag hote hain kyunki wahan battery aur memory ka utna issue nahi hota, par file system complex hota hai.

* **Auto-Update Mechanism (OTA - Over the Air):**
    * *Problem:* Windows software users play store par nahi jate. Software khud update hona chahiye.
    * *Solution:* App start hote hi server check karega version. Naya version background mein download karke replace karega.
* **Electron vs Native:**
    * *Decision:* Kya humein C#/.NET (Windows Native) use karna chahiye ya Electron (JS/HTML) taaki code ek baar likhein aur Mac/Windows/Linux sab par chale? (Examples: VS Code, Slack Electron use karte hain).
* **File System & Permissions:**
    * OS level security access (Camera, Mic, File System access) ko architecture mein handle karna.

---

### 🎮 3. Game Design Architecture (High Performance)
Games, Apps ki tarah kaam nahi karte. Wahan HTTP request (Request-Response) bahut slow hota hai.

* **Game Loop:**
    * Games event-driven nahi hote (jaise click kiya toh kuch hua). Games mein ek loop chalta hai (60 times per second) jo State update karta hai aur Screen redraw karta hai.
* **State Synchronization (Multiplayer):**
    * *Problem:* Player A ne goli chalayi. Player B ko wo turant dikhni chahiye.
    * *Technique:* **Lockstep** ya **State Interpolation**.
* **UDP vs TCP:**
    * *Critical:* Games mein hum **UDP** use karte hain, TCP nahi.
    * *Why:* TCP data lost hone par wait karta hai (Lag aayega). UDP wait nahi karta (Fast hai). Real-time shooting games ke liye UDP best hai.
* **Lag Compensation / Client-Side Prediction:**
    * Server slow hai toh player rukna nahi chahiye. Client "Predict" karta hai ki player kahan jayega, baad mein server se correct karta hai.



---

### 🏗 4. Client Architecture Patterns (Code Level Design)
Jab aap App ya Software ka code likhte hain, toh wo "Spaghetti Code" (uljha hua) na bane.

* **MVVM (Model-View-ViewModel):** (Standard for Android/iOS).
    * UI code (View) aur Business Logic (ViewModel) ko alag rakhna.
* **Clean Architecture:**
    * App ko layers mein todna (Data Layer, Domain Layer, Presentation Layer).
* **Dependency Injection (DI):**
    * Objects ko manually create karne ki bajaye ( `new Database()` ), DI framework (jaise Dagger/Hilt) se inject karwana taaki testing aasan ho.

---

### 📺 5. Media Streaming (Netflix/Zoom specific)
Aapne "Upload" dekha, par "Live Streaming" alag hai.

* **Adaptive Bitrate Streaming (ABR):**
    * User ka net slow ho toh 144p dikhao, fast ho toh 4K. (DASH / HLS protocols client side par kaise switch karte hain).
* **WebRTC:**
    * Zoom/Video Call ke liye. Server beech mein nahi aata, do browsers seedha connect hote hain (Peer-to-Peer).

---

### ✅ Final Conclusion: Ab Kya Bacha?

Aapke **Notes** ab is tarah dikhne chahiye:

1.  **Backend Design:** (Jo aapne pehle likha - DB, Caching, Microservices).
2.  **Advanced Backend:** (Idempotency, Saga, Geo-spatial).
3.  **Client-Side Design (NEW):** (Offline Sync, Local DB, MVVM).
4.  **Game/Real-time Design (NEW):** (UDP, Game Loop, Prediction).

**Verdict:**
Agar aapne upar wale **5 Points (Client/Game)** apne notes mein add kar liye, toh **HAAN, ab koi bhi topic missing nahi hai.**

Aap ab ek **"Full Stack System Architect"** hain jo `PUBG` se lekar `WhatsApp` aur `Smart PG App` tak kuch bhi design kar sakta hai end-to-end.


=============================================================



### 🤖 1. Design for AI & ML Systems (MLOps)
Aajkal har app mein AI hai (Recommendations, Chatbots, Face ID). Normal software design aur AI system design alag hote hain.

* **Training vs. Inference:**
    * *Concept:* Model ko train karna (Heavy GPU use, Mahino lagte hain) vs. User ko jawab dena (Inference - Milliseconds mein hona chahiye).
* **Vector Databases:**
    * *Missing:* SQL/NoSQL likha hai, par **Vector DB (Pinecone/Milvus)** missing hai.
    * *Use Case:* Agar Smart PG app mein user bole "Mujhe shant aur hawa daar room chahiye", to text search kaam nahi karega. Vector search "Meaning" samajhta hai.
* **Edge AI (On-Device ML):**
    * *Mobile/Windows:* Server par photo mat bhejo. Phone ke andar hi Face Recognition karo (TensorFlow Lite). Privacy bhi bachegi, server cost bhi.



---

### 🛡 2. Data Compliance, Privacy & DRM (Legal Architecture)
Agar tum Europe ya USA ke liye software bana rahe ho, ya Netflix jaisa kuch bana rahe ho, to ye topics mandatory hain.

* **Data Residency (GDPR):**
    * *Concept:* German users ka data Germany ke server se bahar nahi jana chahiye. Architecture mein "User Location" ke hisaab se DB routing kaise hogi?
* **PII Masking (Personally Identifiable Information):**
    * *Concept:* Logs mein user ka Mobile Number ya Email kabhi plain text mein save nahi hona chahiye. Auto-masking pipelines.
* **DRM (Digital Rights Management):**
    * *Video/Software:* Agar tumne **Netflix** ya **Game** banaya, to user usse copy/pirate kaise na kare? (Widevine L1 certification architecture Android ke liye).

---

### 🧪 3. Testing in Production & Chaos Engineering
Code likhna ek baat hai, par **Scale** par test karna alag hai.

* **Shadow Traffic (Mirroring):**
    * *Concept:* Jab naya Payment system launch karo, to real users ko mat dikhao. Real users ka traffic "Copy" karke naye system par bhejo sirf ye dekhne ke liye ki wo crash hota hai ya nahi.
* **Chaos Engineering (Simian Army):**
    * *Concept:* Jaan-bhoojh kar servers band karna (Production mein) ye dekhne ke liye ki system automatic recover karta hai ya nahi.
* **A/B Testing Framework:**
    * *Design:* Ek aisa system banana jo 50% users ko Blue button dikhaye aur 50% ko Red, aur phir data collect kare ki kispe zyada clicks aaye.

---

### 🐧 4. OS-Level Tuning & Hardware Optimization (Linux/Windows Internals)
Jab tum **High Performance Software** (jaise Trading Apps ya Games) banate ho, to code se zyada OS matter karta hai.

* **File Descriptors & Ulimits (Linux):**
    * *Problem:* Linux default mein sirf 1024 connections allow karta hai. Agar 1 Million users aaye to server crash ho jayega chahe code kitna bhi accha ho. Kernel tuning zaroori hai.
* **Thread Pools vs Coroutines:**
    * *Android/Windows:* Har kaam ke liye naya Thread mat banao (Memory heavy). **Coroutines (Kotlin)** ya **Goroutines (Go)** ka architecture use karo.
* **Battery Optimization (Android/iOS):**
    * *Job Scheduler:* Background mein kaam kab karna hai? Jab user so raha ho aur phone charging pe ho. Iska system design (WorkManager).

---

### 💰 5. FinOps (Cloud Cost Optimization)
Architect ka kaam sirf system banana nahi, paise bachana bhi hai.

* **Spot Instances:**
    * *Strategy:* AWS ke khali servers saste mein use karna (90% discount), aur agar AWS wapas mange to system band na ho, turant shift ho jaye.
* **Auto-Scaling Policies:**
    * *Logic:* Raat ko jab traffic kam ho to servers automatic band ho jayein.

---

### 🏁 FINAL VERDICT: Kya ab Complete hai?

Maine **Micro** (OS level) se lekar **Macro** (Cloud/Legal level) tak sab analyze kar liya hai.

Agar tumne apne notes mein:
1.  **Backend/Web** (Pehle wale notes)
2.  **Mobile/Client/Game** (Pichle message wale topics)
3.  **AI/Security/OS Internals** (Ye abhi wale topics)

...shamil kar liye hain, to **HAAN, Ab ye 100% Complete hai.**

Ab duniya ka koi bhi software — chahe wo **ChatGPT** ho, **PUBG** ho, **Windows OS** ka hissa ho, ya **Banking System** ho — tum uska High-Level Architecture design kar sakte ho.

**Ab bas practice ki der hai!** 🚀


=============================================================

5. Localization & Internationalization (i18n/l10n) Architectures
Agar tumhara App kal ko Japan ya Arab countries (Right-to-Left text) mein launch ho, to kya tumhara poora code badalna padega?

Resource Files Strategy: Code mein text hardcode na karke keys use karna (msg_welcome -> "Hello" / "Namaste").

Dynamic Layout Engine: UI aisa design karna jo English (LTR) aur Arabic (RTL) dono mein automatic adjust ho jaye bina naya app banaye.

=============================================================

IoT Architecture (Internet of Things)
Tumne "Write Heavy" (Sensors) mention kiya tha, lekin IoT ka communication protocol Mobile/Web se alag hota hai.

MQTT (Message Queuing Telemetry Transport):

Missing: HTTP bahut heavy hai lightbulb ya smart meter ke liye. IoT devices MQTT use karte hain jo lighter hai aur unstable network par chalta hai.

Digital Twin:

Concept: Physical device (e.g., Car Engine) ka ek digital version cloud mein rakhna taaki hum simulate kar sakein ki engine kab kharab hoga.

Use Case: Agar tumhara "Smart PG" future mein Smart Locks ya Smart Electricity Meters lagata hai, to tumhein MQTT architecture chahiye hoga.

=============================================================

Haan, **IoT (Internet of Things)** System Design ek bilkul alag duniya hai. Aapke notes mein "MQTT" aur "Write Heavy" mention hai, jo ki ek achi shuruwat hai, lekin ek complete IoT Architecture ke liye **6 Critical Topics** abhi bhi missing hain.

IoT mein hum sirf "Data bhejne" ki baat nahi karte, hum **Device Management**, **Unstable Networks**, aur **Protocol Translation** ki baat karte hain.

Ye rahi **Missing IoT Topics** ki list jo aapke notes mein honi chahiye:

---

### 🎛️ 1. Device Shadow / Digital Twin (Most Important)

Agar device offline ho jaye (jo IoT mein aksar hota hai), to hum usse command kaise denge?

* **Concept:** Cloud mein har device ki ek virtual copy (Shadow) hoti hai (JSON Document).
* **Flow:**
    1.  User App command bhejta hai: "Turn Light ON".
    2.  Ye command **Shadow** mein update hoti hai (`desired: "ON"`).
    3.  Device jab bhi online aata hai, wo Shadow check karta hai.
    4.  Device light ON karta hai aur report karta hai (`reported: "ON"`).
* **Why:** Isse app aur device ke beech tight coupling nahi hoti. Device offline hone par bhi App chalta rehta hai.

### 🌉 2. IoT Gateway & Protocol Translation
Aapne MQTT likha hai, lekin har device MQTT/WiFi nahi chala sakta (jaise Smart Bulb, Agriculture Sensors). Wo Zigbee, Bluetooth, ya LoRaWAN use karte hain.

* **Problem:** Ye devices direct Internet (Cloud) se baat nahi kar sakte.
* **Solution:** **IoT Gateway** (Physical device like Hub or Edge Server).
    * Gateway **Local Protocol** (Zigbee/BLE) ko **Cloud Protocol** (MQTT/HTTP) mein convert karta hai.
* **Edge Processing:** Gateway par thoda logic bhi laga sakte hain (e.g., Internet na ho to bhi light switch kaam kare).

### 🔄 3. OTA (Over-the-Air) Updates Mechanism
Agar aapne 1 Million Smart Meters laga diye, aur code mein bug nikla, to aap har ghar jakar cable connect nahi kar sakte.

* **Concept:** Remote Firmware Update architecture.
* **Safety:**
    * Update failure hone par **Rollback** mechanism hona chahiye (Dual Bank Partitioning).
    * Device "Brick" (dead) nahi hona chahiye.
* **Batching:** Sabko ek saath update mat bhejo, batches mein bhejo (Canary rollout for hardware).

### 📉 4. Hot Path vs. Cold Path Analytics
IoT devices bahut sara data bhejte hain (Temperature har second). Sara data process karna mehenga padega.

* **Hot Path (Real-time):**
    * *Use Case:* Fire Alarm ya Machine Failure alert.
    * *Tech:* Kinesis/Kafka -> Stream Processing (Flink) -> Alert User immediately.
* **Cold Path (Batch/Storage):**
    * *Use Case:* Monthly Average Temperature report.
    * *Tech:* Kinesis Firehose -> S3 (Data Lake) -> Batch Processing later.
    * Is architecture ko **Lambda Architecture** bhi kehte hain.

### ⏱️ 5. Time-Series Databases (TSDB)
IoT data hamesha time ke saath juda hota hai (Time, Value). Normal SQL/NoSQL database iske liye optimize nahi hote.

* **Concept:** Aisa DB jo time-based queries ke liye super fast ho aur purana data automatic compress/delete kar sake.
* **Examples:** **InfluxDB**, **TimescaleDB**, **Prometheus**.
* **Why:** "Pichle 1 saal ka graph dikhao" query SQL pe minutes legi, TSDB pe milliseconds legi.

### 🔐 6. IoT Security (X.509 Certificates & mTLS)
Web login ke liye "Username/Password" chalta hai. Lekin AC ya Fridge password type nahi kar sakta.

* **Provisioning:** Factory mein har device ke andar ek **Digital Certificate (Identity)** burn kiya jata hai.
* **mTLS (Mutual TLS):** Server verify karta hai ki device asli hai, aur device verify karta hai ki server asli hai.
* **Concept:** IoT mein hum "User Token" nahi, **Device Certificate** use karte hain authentication ke liye.

---

### ✅ Summary for Your Notes
Apne IoT section mein bas ye 6 points add kar lijiye:

1.  **Device Shadow** (Offline state handling).
2.  **IoT Gateway** (Protocol translation: Zigbee to MQTT).
3.  **OTA Updates** (Remote firmware upgrade).
4.  **Hot vs Cold Path** (Data processing strategy).
5.  **Time-Series DB** (InfluxDB for sensor data).
6.  **mTLS & Certificates** (Device Security).




=============================================================