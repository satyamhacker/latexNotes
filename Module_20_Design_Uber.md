# Module 20: Design Uber (Ride-Hailing System)

## Topic 20.1: Location Services & Spatial Indexing (S2/QuadTree)

---

## 🎯 1. Title / Topic: Uber Location Service (Geospatial Indexing)

---

## 🐣 2. Samjhane ke liye (Simple Analogy)

Imagine karo ek **Library** jisme millions of books hain. Agar aapko "Harry Potter" dhundhni hai aur books random padi hain, toh aapko ek-ek book check karni padegi (Linear Search - bahut slow). Isliye library **Sections** (Fiction, Sci-Fi) aur **Racks** (A1, A2) mein divide hoti hai.
Uber ke liye, puri duniya ek library hai aur drivers books hain. Hum duniya ko chhote **Grids** (Racks) mein divide karte hain. Jab rider Delhi mein request karta hai, toh hum sirf "Delhi Grid" check karte hain, New York nahi. **Google S2** ek special tareeka hai jo duniya ko ek **Hilbert Curve** (ek continuous line) mein convert karta hai, taaki computers nearby drivers ko fast dhund sakein.

---

## 📖 3. Technical Definition (Interview Answer)

**Uber Location Service** uses **Spatial Indexing** to efficiently store and query millions of real-time driver locations. It utilizes **Google S2 Geometry** (based on Hilbert Curves) or **QuadTrees** to map 2D geographical coordinates (Latitude/Longitude) into 1D integers (Cell IDs), enabling sub-millisecond **K-Nearest Neighbor (KNN)** searches.

**Key terms**:
- **Spatial Indexing**: 2D map ko searchable grids mein todna.
- **QuadTree**: Ek box ko 4 chhote boxes mein recursively divide karna.
- **Geohash**: Location ko string mein encode karna (e.g., "ttcgx2").
- **Google S2**: Earth ko mathematical cells mein divide karna using Hilbert Curve (Uber uses this).
- **Hilbert Curve**: Ek continuous line jo 2D space ko fill karti hai without crossing itself (preserves locality).

---

## 🧠 4. Zaroorat Kyun Hai? (Why?)

1. **Problem**: 1 Million drivers online hain. Rider ke paas wale 5 drivers dhundne ke liye agar sabka distance calculate karein (Linear Search), toh 10 seconds lagenge. User wait nahi karega.
2. **Business Impact**: Uber ka core business "Fast Pickup" hai. Agar matching slow hui, toh business fail.
3. **Technical Benefit**: Spatial Indexing se search time **O(N)** se ghatkar **O(log N)** ya **O(1)** ho jata hai (< 10ms latency).

---

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario)

- **Linear Search Disaster**:
    - Rider request: "Find drivers near me".
    - Server: "Ruko, main India ke saare 500,000 drivers ka distance calculate karta hoon."
    - Result: CPU 100%, Request Timeout, App Crash.
- **Battery Drain**: Agar driver har second location bhejega aur server inefficiently process karega, toh phone battery jaldi khatam hogi.

---

## ⚙️ 6. Under the Hood (Technical Working)

**How S2 Geometry Works (The Magic):**
1. **Sphere to Cube**: Earth (sphere) ko ek Cube mein project karte hain.
2. **Cube to Cells**: Har cube face ko chhote cells mein divide karte hain (Hierarchy levels 0-30).
3. **Hilbert Curve**: In cells ko ek specific order mein number dete hain (Cell ID).
    - *Magic*: Jo cells map par paas hain, unke Cell IDs bhi numerically paas hote hain.
4. **Storage**: Driver ki location (Lat/Long) → Cell ID (Int64). Database mein sirf Cell ID store hota hai.
5. **Query**: "Find drivers in Cell X". Database query: `SELECT * FROM drivers WHERE cell_id BETWEEN min AND max`.

**ASCII Diagram – QuadTree vs Hilbert Curve**

```
QuadTree (Recursive Box):      Hilbert Curve (S2 - Snake Line):

+-------+-------+             +---+   +---+
|       |       |             | 1 |---| 2 |
|   A   |   B   |             +---+   +---+
|       |       |               |       |
+-------+-------+             +---+   +---+
|       |       |             | 4 |---| 3 |
|   C   |   D   |             +---+   +---+
|       |       |
+-------+-------+
(Divide space into 4)         (One line connects all cells)
```

---

## 🛠️ 7. Problems Solved
- **Ultra-Fast Search**: Nearby drivers dhundna ab bas ek range query hai.
- **Scalability**: Grid size adjust kar sakte hain (City mein chhota grid, Village mein bada).
- **Precision**: S2 cm-level precision de sakta hai.

---

## 🌍 8. Real‑World Example
**Uber**: Uses **Google S2** (Level 12 cells, approx 3km² area) for dispatching. Drivers aur Riders ko same S2 cell mein map karte hain.
**Yelp/Tinder**: Use **Geohash** to find nearby restaurants/dates. Geohash simple hai but S2 zyada accurate hai boundaries par.

---

## 🔧 9. Tech Stack / Tools
- **Google S2 Library**: C++/Go/Java/Python library for spatial geometry.
- **Redis (Geo)**: In-memory storage jo Geohash support karta hai (`GEOADD`, `GEORADIUS`).
- **PostgreSQL (PostGIS)**: Persistent storage for maps and shapes.

---

## 📐 10. Architecture / Formula
**Search Radius Logic**
```
1. Rider Location -> Convert to S2 Cell ID (Level 12).
2. Find Neighbors -> Get Cell IDs of 8 surrounding cells.
3. Query DB -> SELECT drivers WHERE cell_id IN (Center + Neighbors).
```

**ASCII Diagram – Location Update Flow**
```
[Driver App] --(GPS: Lat/Long)--> [Load Balancer]
                                        |
                                        v
                                [Location Service]
                                (Converts to S2 Cell ID)
                                        |
                                        v
                                [Redis Cluster]
                                (Key: CellID, Val: DriverID)
```

---

## 💻 11. Code / Flowchart (S2 Concept)
*Note: This is conceptual Python code using a hypothetical S2 library.*

```python
# S2 Geometry Concept - Finding Nearby Drivers

class LocationService:
    def __init__(self):
        # Redis simulation: Key = CellID, Value = List of DriverIDs
        self.driver_index = {} 

    def update_driver_location(self, driver_id, lat, lng):
        """Driver ki location update hoti hai har 4 sec"""
        # 1. Lat/Long ko S2 Cell ID mein convert karo (Level 12 ~ 3km area)
        cell_id = self._get_s2_cell_id(lat, lng)
        
        # 2. Purani location remove karo (Real system mein ye complex hota hai)
        self._remove_driver(driver_id)
        
        # 3. Nayi location par add karo
        if cell_id not in self.driver_index:
            self.driver_index[cell_id] = []
        self.driver_index[cell_id].append(driver_id)
        print(f"📍 Driver {driver_id} moved to Cell {cell_id}")

    def find_nearby_drivers(self, rider_lat, rider_lng):
        """Rider ke paas wale drivers dhundo"""
        # 1. Rider ka Cell ID nikalo
        center_cell = self._get_s2_cell_id(rider_lat, rider_lng)
        
        # 2. Sirf current cell nahi, aas-paas ke 8 cells bhi check karo (Neighbors)
        # Kyunki rider cell ki boundary par ho sakta hai
        cells_to_check = [center_cell] + self._get_neighbors(center_cell)
        
        nearby_drivers = []
        for cell in cells_to_check:
            if cell in self.driver_index:
                nearby_drivers.extend(self.driver_index[cell])
                
        return nearby_drivers

    def _get_s2_cell_id(self, lat, lng):
        # Mock function: Real S2 library math use karti hai
        return f"cell_{int(lat)+int(lng)}" 

    def _get_neighbors(self, cell_id):
        # Mock: Return dummy neighbor cells
        return [f"{cell_id}_n1", f"{cell_id}_n2"]

    def _remove_driver(self, driver_id):
        # Helper to cleanup old location
        pass

# Usage
service = LocationService()
service.update_driver_location("Driver_A", 28.5, 77.2)
matches = service.find_nearby_drivers(28.5, 77.2)
print(f"✅ Found Drivers: {matches}")
```

---

## 📈 12. Trade‑offs
- **Gain:** S2 is mathematical (CPU fast) vs QuadTree (Memory heavy).
- **Loss:** S2 implementation complex hai, debugging mushkil ho sakti hai (Cell IDs are just numbers).
- **Gain:** Redis Geo is easy to start | **Loss:** Redis memory expensive hai at Uber scale.

---

## 🐞 13. Common Mistakes
- **Mistake:** Searching only the current cell.
    - **Why Wrong:** Agar rider cell ke edge par hai, toh driver dusre cell mein paas ho sakta hai.
    - **Fix:** Always search Current Cell + 8 Neighbors.
- **Mistake:** Storing history in Redis.
    - **Why Wrong:** Redis RAM bhara jayega.
    - **Fix:** Only store *current* location in Redis. History goes to Cassandra/S3.

---

## ✅ 14. Zaroori Notes for Interview
1. **Mention S2**: "Main Google S2 use karunga kyunki ye Earth ke curvature ko Geohash se better handle karta hai."
2. **Hilbert Curve**: "S2 Hilbert Curve use karta hai jo 2D locality ko 1D mein preserve karta hai."
3. **Update Frequency**: "Drivers har 4 second mein location bhejte hain, hum Redis mein TTL (Time To Live) use karte hain taaki stale drivers expire ho jayein."

---

## ❓ 15. FAQ & Comparisons
**Q1: Geohash vs S2 - Kya fark hai?**
A: Geohash string-based hai ("abc"), S2 number-based hai (Int64). S2 math operations (finding neighbors) mein fast hai aur Earth ke poles par better kaam karta hai. Uber switched from Geohash to S2.

**Q2: QuadTree kyu nahi?**
A: QuadTree ko update karna mushkil hai (tree re-balancing). S2 mein cell ID fix hota hai, bas map update karna hai. High-write systems (like Uber) ke liye S2 better hai.

**Q3: Location updates push ya pull?**
A: **Push**. Driver app server ko location *push* karta hai (WebSocket/HTTP). Server rider ko *push* karta hai. Pull karna (polling) server ko crash kar dega.

**Q4: Privacy ka kya?**
A: Driver ki exact location database mein store hoti hai, lekin rider ko thoda "fuzz" karke dikhate hain jab tak trip start na ho, taaki stalking na ho sake.

**Q5: Agar Redis fail ho jaye?**
A: Redis cluster mode mein hota hai (Sharding). Agar ek node fail ho, toh replica take over karta hai. Location data transient hai (kuch seconds mein naya aa jayega), so strict durability critical nahi hai.

---

## Topic 20.2: Trip Management & Matching Engine

---

## 🎯 1. Title / Topic: Uber Matching Engine & State Machine

---

## 🐣 2. Samjhane ke liye (Simple Analogy)

Matching Engine ek **Auction House** jaisa hai. Rider "Bid" karta hai (Request), aur system best "Seller" (Driver) dhundta hai.
State Machine ek **Board Game** ke rules jaisi hai. Aap seedha "Start" se "Finish" par jump nahi kar sakte. Aapko steps follow karne padenge: Start -> Dice Roll -> Move -> Finish. Waise hi Trip: Request -> Match -> Pickup -> Drop -> End. Aap bina Pickup kiye Drop nahi kar sakte.

---

## 📖 3. Technical Definition (Interview Answer)

**Matching Engine** is a heuristic-based system that pairs riders with drivers by calculating a weighted score of **ETA (Estimated Time of Arrival)**, **Distance**, and **Driver Rating**.
**Trip State Machine** is a Finite State Machine (FSM) that enforces valid transitions for a trip lifecycle (e.g., `REQUESTED` → `MATCHED` → `IN_PROGRESS` → `COMPLETED`), ensuring data consistency and preventing logical errors.

**Key terms**:
- **FSM (Finite State Machine)**: Mathematical model of computation with fixed states.
- **Shadowing**: Driver ko request bhejna but reject hone par turant dusre ko bhejna.
- **Batched Matching**: Request aate hi match karne ki jagah, 2-second window mein requests collect karke best global match dhundna.

---

## 🧠 4. Zaroorat Kyun Hai? (Why?)

1. **Problem (Matching)**: Sirf closest driver best nahi hota. Wo traffic mein fasa ho sakta hai.
2. **Problem (State)**: Kya hoga agar driver "Trip End" daba de jab trip start hi nahi hui? System confuse ho jayega aur paise kat jayenge.
3. **Business Impact**: Wrong matching = Long wait time = Cancelled rides. Invalid state = Billing disputes.

---

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario)

- **Bad Matching**: Driver 1km door hai but traffic jam mein hai (15 min ETA). Driver 2km door hai but highway par hai (5 min ETA). Simple distance logic Driver 1 ko chunega (Wrong choice).
- **State Chaos**: Driver galti se "Drop off" daba deta hai pickup se pehle. Bina State Machine ke, ride end ho jayegi aur rider sadak par khada reh jayega.

---

## ⚙️ 6. Under the Hood (Technical Working)

**Matching Logic (The Score):**
Hum har candidate driver ke liye ek score calculate karte hain:
`Score = (w1 * ETA) + (w2 * Distance) + (w3 * Rating)`
Jiska score best hoga, usko request jayegi.

**Trip State Machine Flow:**
1. **REQUESTED**: Rider ne button dabaya.
2. **SEARCHING**: System drivers dhund raha hai.
3. **OFFERED**: Driver ko notification gayi.
4. **MATCHED**: Driver ne accept kiya.
5. **ARRIVED**: Driver pickup point par hai.
6. **IN_PROGRESS**: Rider baith gaya, trip start.
7. **COMPLETED**: Destination pahunch gaye.
8. **CANCELLED**: Kisi ne cancel kiya (valid from Searching/Matched).

**ASCII Diagram – Trip State Machine**
```
   [REQUESTED] --(System finds driver)--> [OFFERED]
                                            |
        +-----------------------------------+
        | (Driver Accepts)
        v
   [MATCHED] --(Driver reaches)--> [ARRIVED]
        |                             |
        | (User Cancels)              | (Trip Starts)
        v                             v
   [CANCELLED]                  [IN_PROGRESS]
                                      |
                                      | (Destination Reached)
                                      v
                                 [COMPLETED]
```

---

## 🛠️ 7. Problems Solved
- **Global Optimization**: Batched matching se system ensure karta hai ki overall wait time kam ho, na ki sirf ek user ka.
- **Consistency**: State machine ensure karti hai ki billing tabhi trigger ho jab state `COMPLETED` ho.

---

## 🌍 8. Real‑World Example
**Uber**: Uses a service called **Ringpop** (consistent hash ring) to manage stateful objects like Trips. Matching logic considers traffic prediction (Uber Movement).
**Grab**: Uses similar logic but optimizes heavily for "Cash Payments" and "Traffic Jams" specific to SE Asia.

---

## 🔧 9. Tech Stack / Tools
- **Uber Ringpop**: Node.js library for application-layer sharding (handling trip states in memory).
- **Kafka**: State transitions events (e.g., `TripStarted`) Kafka topic mein jate hain for billing & analytics.
- **DynamoDB/Cassandra**: Trip history store karne ke liye (High write throughput).

---

## 📐 10. Architecture / Formula
**Matching Score Formula**
```
Score = (0.6 * Normalised_ETA) + (0.3 * Normalised_Distance) + (0.1 * Driver_Rating)
*Lower score is better (cost function).*
```

**ASCII Diagram – Matching Flow**
```
[Rider] --Request--> [Matching Service]
                          |
              (1) Query Location Service (Get 10 nearby drivers)
                          |
              (2) Calculate ETA (Google Maps API)
                          |
              (3) Rank Drivers (Score Formula)
                          |
              (4) Send Offer to Driver #1
                          |
              +-----------+-----------+
              |                       |
        (Accepts)                 (Rejects/Timeout)
              |                       |
        [Trip Created]          [Offer to Driver #2]
```

---

## 💻 11. Code / Flowchart (State Machine & Matching)

```python
# Uber Matching & State Machine Logic

class TripStateMachine:
    def __init__(self, trip_id):
        self.trip_id = trip_id
        self.state = "REQUESTED"
        # Valid transitions map
        self.valid_transitions = {
            "REQUESTED": ["SEARCHING", "CANCELLED"],
            "SEARCHING": ["OFFERED", "CANCELLED"],
            "OFFERED": ["MATCHED", "SEARCHING"], # Searching if rejected
            "MATCHED": ["ARRIVED", "CANCELLED"],
            "ARRIVED": ["IN_PROGRESS", "CANCELLED"],
            "IN_PROGRESS": ["COMPLETED"],
            "COMPLETED": [],
            "CANCELLED": []
        }

    def transition(self, new_state):
        """State change logic with validation"""
        if new_state in self.valid_transitions[self.state]:
            print(f"✅ Trip {self.trip_id}: {self.state} -> {new_state}")
            self.state = new_state
            self._trigger_side_effects(new_state)
            return True
        else:
            print(f"❌ Invalid Transition: {self.state} -> {new_state}")
            return False

    def _trigger_side_effects(self, state):
        # State change hone par kya karna hai
        if state == "MATCHED":
            print("   -> Notify Rider: Driver Found")
        elif state == "COMPLETED":
            print("   -> Trigger Payment Service")

class MatchingService:
    def calculate_score(self, driver, rider_loc):
        # Simplified scoring logic
        # ETA aur Distance real world mein Maps API se aayega
        eta_mins = self._mock_eta(driver['loc'], rider_loc)
        dist_km = self._mock_dist(driver['loc'], rider_loc)
        
        # Formula: 70% weight to ETA, 30% to Distance
        # Real world mein rating, vehicle type bhi hota hai
        score = (0.7 * eta_mins) + (0.3 * dist_km)
        return score

    def _mock_eta(self, p1, p2): return 5 # Mock 5 mins
    def _mock_dist(self, p1, p2): return 2 # Mock 2 km

# Usage
trip = TripStateMachine("TRIP_123")
trip.transition("SEARCHING") # ✅ OK
trip.transition("COMPLETED") # ❌ Invalid (Can't jump steps)
trip.transition("OFFERED")   # ✅ OK
trip.transition("MATCHED")   # ✅ OK
```

---

## 📈 12. Trade‑offs
- **Gain:** State Machine bugs kam karta hai | **Loss:** Flexibility kam hoti hai (Manual override mushkil).
- **Gain:** Batched Matching efficiency badhata hai | **Loss:** Rider ko 2-3 second extra wait karna padta hai matching ke liye.

---

## 🐞 13. Common Mistakes
- **Mistake:** Client-side State Management.
    - **Why Wrong:** Users app hack karke fake "Trip Complete" bhej sakte hain.
    - **Fix:** State always Server par manage honi chahiye.
- **Mistake:** Locking the driver immediately.
    - **Why Wrong:** Agar driver reject kare, toh lock release karne mein time lagta hai.
    - **Fix:** Optimistic locking ya short TTL offers use karein.

---

## ✅ 14. Zaroori Notes for Interview
1. **State Machine**: "Trip ka lifecycle manage karne ke liye main Finite State Machine use karunga taaki invalid transitions (jaise Start se pehle End) na hon."
2. **Batched Matching**: "Instant match ki jagah, hum 2-second window mein requests collect karke 'Bipartite Matching' kar sakte hain for global optimization."
3. **Concurrency**: "Agar do riders same driver ko book karein, toh Database Transaction (Row Lock) ya Redis Atomic operations use karenge race condition rokne ke liye."

---

## ❓ 15. FAQ & Comparisons
**Q1: Driver ko request kaise bhejte hain?**
A: WebSocket ya Push Notification (FCM/APNS). WebSocket fast hai (real-time), Push backup hai agar app background mein hai.

**Q2: Agar Driver accept na kare?**
A: Offer ka timeout hota hai (e.g., 15 seconds). Agar timeout ho jaye ya reject ho, toh state wapas "SEARCHING" mein jati hai aur next best driver ko offer jata hai.

**Q3: Surge Pricing kab calculate hota hai?**
A: Matching se pehle. Jab rider app kholta hai, tabhi demand/supply check karke price fix (lock) kar diya jata hai kuch minutes ke liye.

**Q4: Pool/Share rides kaise kaam karti hain?**
A: Ye complex hai. Isme "Knapsack Problem" jaisa logic lagta hai. System ko dekhna padta hai ki detour kitna bada hai aur kya wo acceptable limit mein hai.

**Q5: Payment kab hoti hai?**
A: State machine jab `COMPLETED` state mein aati hai, tab Payment Service ko event jata hai. Auth pehle hi le li jati hai (Pre-auth).

---

## 🎯 Module 20 Complete Summary
- **Topic 20.1**: Location Services (S2 Geometry, Hilbert Curve, Redis Geo) – Finding drivers efficiently.
- **Topic 20.2**: Matching & State Machine (FSM, Scoring, WebSocket) – Managing the ride lifecycle.
- **Key Takeaways**: S2 > Geohash for Uber. State Machines prevent billing errors.
- **Interview Ready**: Focus on "Why S2?" and "How State Machine ensures consistency".
