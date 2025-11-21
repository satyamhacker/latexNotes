# Module 20: Design Uber (Ride-Hailing System)

## Topic 20.1: Uber System - Location Services & Matching

---

## 🎯 1. Title / Topic: Uber/Grab (Ride-Hailing Platform)

---

## 🐣 2. Samjhane ke liye (Simple Analogy):

Uber ek **Smart Traffic Control System** jaisa hai jo riders aur drivers ko match karta hai. Jaise traffic police ek **Grid Map** use karta hai city ko chhote areas mein divide karne ke liye (Sector 1, Sector 2), waise hi Uber **Geohash/QuadTree** use karta hai location ko divide karne ke liye. Jab rider request karta hai, system nearby drivers dhundta hai (same grid mein), closest driver ko assign karta hai. **ETA Calculation:** Jaise Google Maps batata hai "15 min mein pahunchoge" (traffic + distance), waise hi Uber ETA calculate karta hai. **Dynamic Pricing:** Jaise festival mein hotel rates badh jaate hain (demand high), waise hi Uber mein surge pricing (demand > supply).

---

## 📖 3. Technical Definition (Interview Answer):

**Uber System** is a real-time ride-hailing platform that uses geospatial indexing (QuadTree/Geohash) for location-based matching, WebSocket for real-time updates, routing algorithms (Dijkstra/A*) for ETA calculation, and dynamic pricing based on supply-demand ratio.

**Key terms:**
- **Geohash:** Location ko string mein encode (lat/long → "u4pruydqqvj") - nearby locations have similar prefixes
- **QuadTree:** 2D space ko recursively 4 parts mein divide - efficient nearby search
- **Matching Algorithm:** Rider ko nearest available driver assign (distance + ETA + rating)
- **ETA (Estimated Time of Arrival):** Route distance + traffic + driver speed → Time calculation
- **Surge Pricing:** Demand > Supply → Price multiply by surge factor (1.5x, 2x, 3x)
- **Trip State Machine:** Requested → Matched → Started → Completed (state transitions)

---

## 🧠 4. Zaroorat Kyun Hai? (Why?):

**Main Problem:** 1M drivers online, rider request karta hai, kaunsa driver assign karein? Linear search (1M drivers check) = 1 second (too slow). Geospatial indexing se nearby drivers in <10ms.

**Business Impact:** Uber: 131M users, 23M trips/day, $31B revenue (2022). Without efficient matching, wait time 10x increase → Users switch to competitors.

**Technical Benefits:**
- **Fast Matching:** <10ms to find nearby drivers (vs 1 sec linear search)
- **Real-time Updates:** Driver location updates every 4 sec (WebSocket)
- **Accurate ETA:** Traffic-aware routing → 90% accuracy (within 2 min)
- **Dynamic Pricing:** Surge pricing balances supply-demand → 30% more drivers during peak

---

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario):

**Scenario: No Geospatial Indexing (Linear Search)**
- Rider requests ride in Delhi
- System: Check all 100K online drivers in India
- Query: SELECT * FROM drivers WHERE status='available' (100K rows)
- Calculate distance for each: 100K × haversine formula = 10 seconds
- Result: 10 sec wait → Rider frustrated → Cancels

**Scenario: No Real-time Location Updates**
- Driver location updated every 5 minutes (instead of 4 sec)
- Rider sees driver 2 km away (stale data)
- Reality: Driver already 5 km away (moved in 5 min)
- Result: Wrong ETA, rider waits 20 min instead of 5 min

**Real Example:** **Ola (2015)** - Initially used simple radius search (all drivers within 5 km) → Slow during peak (10K drivers in 5 km radius) → Switched to QuadTree (2016) → Matching time reduced from 5 sec to 50ms → 40% improvement in rider satisfaction.

---

## ⚙️ 6. Under the Hood (Technical Working):

**Ride Request Flow:**

1. **Rider Opens App:** Location detected (GPS: 28.6139°N, 77.2090°E - Delhi)
2. **Request Ride:** Tap "Request Uber" button
3. **Geohash Encoding:** Convert location to geohash ("ttcgx2" - 6 char = ~1 km precision)
4. **Find Nearby Drivers:** Query drivers with same geohash prefix
5. **Calculate Distance:** Haversine formula for top 10 drivers
6. **Rank Drivers:** Sort by (distance × 0.7 + ETA × 0.3)
7. **Send Request:** Push notification to top 3 drivers (parallel)
8. **Driver Accepts:** First to accept gets the ride
9. **Match Confirmed:** Rider sees driver details (name, car, ETA)
10. **Real-time Tracking:** Driver location updates every 4 sec (WebSocket)

**Driver Location Update Flow:**

1. **Driver App:** GPS location every 4 seconds
2. **Send to Server:** WebSocket connection (persistent)
3. **Update Database:** Redis (fast write) + PostgreSQL (persistent)
4. **Geohash Update:** Recalculate geohash if moved to new cell
5. **Broadcast:** Send location to matched rider (if any)

**ETA Calculation:**

1. **Route Calculation:** Dijkstra/A* algorithm on road network graph
2. **Distance:** Sum of edge weights (road segments)
3. **Traffic Factor:** Real-time traffic data (Google Maps API / internal)
4. **Speed Estimation:** Historical data (avg speed on this route at this time)
5. **ETA Formula:** Distance / (Speed × Traffic_Factor)

**ASCII Architecture Diagram:**

```
RIDE REQUEST FLOW:

[Rider App]
Location: 28.6139°N, 77.2090°E
     |
     | (1) Request ride
     v
+---------------------------+
|   API GATEWAY             |
|   (Load Balancer)         |
+---------------------------+
     |
     v
+---------------------------+
|   MATCHING SERVICE        |
+---------------------------+
     |
     | (2) Convert to Geohash
     | "ttcgx2" (6 chars)
     v
+---------------------------+
|   LOCATION SERVICE        |
|   (QuadTree / Geohash)    |
+---------------------------+
     |
     | (3) Find nearby drivers
     | Query: geohash LIKE 'ttcgx%'
     v
+---------------------------+
|   REDIS (Driver Cache)    |
|   - Online drivers        |
|   - Location (geohash)    |
|   - Status (available)    |
+---------------------------+
     |
     | (4) Get top 10 drivers
     | [driver1, driver2, ...]
     v
+---------------------------+
|   RANKING SERVICE         |
|   - Calculate distance    |
|   - Calculate ETA         |
|   - Sort by score         |
+---------------------------+
     |
     | (5) Top 3 drivers
     v
+---------------------------+
|   NOTIFICATION SERVICE    |
|   (Push to drivers)       |
+---------------------------+
     |
     | (6) Driver accepts
     v
+---------------------------+
|   TRIP SERVICE            |
|   - Create trip record    |
|   - State: MATCHED        |
+---------------------------+
     |
     v
[Rider sees driver details]


GEOSPATIAL INDEXING (QuadTree):

WORLD MAP (Divided into Quadrants):
+-----------------------------------+
|                |                  |
|   NW (Q1)      |    NE (Q2)       |
|                |                  |
|----------------|------------------|
|                |                  |
|   SW (Q3)      |    SE (Q4)       |
|                |                  |
+-----------------------------------+

Recursively divide until cell has <100 drivers:

Delhi Area (Zoomed):
+----------------+----------------+
|  Q1 (50 drv)   |  Q2 (30 drv)   |
|                |                |
|----------------|----------------|
|  Q3 (80 drv)   |  Q4 (120 drv)  | ← Too many, divide again
+----------------+----------------+

Q4 subdivided:
+--------+--------+
| Q4.1   | Q4.2   |
| 40 drv | 30 drv |
|--------|--------|
| Q4.3   | Q4.4   |
| 25 drv | 25 drv |
+--------+--------+

Rider in Q4.3 → Search Q4.3 first (25 drivers)
If no match → Expand to Q4 (120 drivers)
If still no match → Expand to adjacent quadrants


GEOHASH EXAMPLE:

Location: 28.6139°N, 77.2090°E (Delhi)
Geohash: "ttcgx2" (6 characters)

Precision:
- 1 char: ±2500 km
- 2 char: ±630 km
- 3 char: ±78 km
- 4 char: ±20 km
- 5 char: ±2.4 km
- 6 char: ±0.61 km (610 meters)

Nearby locations have similar prefixes:
- "ttcgx2" (Connaught Place)
- "ttcgx3" (Nearby area)
- "ttcgx8" (Adjacent area)

Query: SELECT * FROM drivers WHERE geohash LIKE 'ttcgx%'
Returns: All drivers within ~2.4 km (5-char prefix)
```

---

## 🛠️ 7. Problems Solved:

- **Fast Matching:** <10ms to find nearby drivers (vs 1 sec linear search) → Better UX
- **Real-time Tracking:** Driver location updates every 4 sec → Accurate ETA, rider confidence
- **Scalability:** 1M concurrent drivers, 100K requests/sec → Geospatial indexing handles scale
- **Accurate ETA:** Traffic-aware routing → 90% accuracy (within 2 min) → Rider trust
- **Dynamic Pricing:** Surge pricing balances supply-demand → 30% more drivers during peak
- **State Management:** Trip state machine prevents errors (can't complete before starting)

---

## 🌍 8. Real-World Example:

**Uber Architecture:** 131M users, 23M trips/day, 5M drivers. Technology: Geohash for location indexing (6-char precision), Redis for driver cache (1M online drivers), PostgreSQL for trip records, Kafka for event streaming, WebSocket for real-time updates. Matching: <50ms to find nearby drivers, considers distance (70%) + ETA (30%). ETA: Google Maps API + internal traffic data, 90% accuracy. Surge: ML model predicts demand, adjusts pricing (1.2x to 5x). Scale: 100K requests/sec during peak, 99.99% uptime. Cost: $1B/year on infrastructure. Without geospatial indexing, Uber couldn't handle 23M trips/day (matching would take 10x longer).

---

## 🔧 9. Tech Stack / Tools:

- **Redis:** Driver location cache. Use for: Fast writes (location updates every 4 sec), geospatial queries (GEORADIUS command), 1M drivers in memory.

- **PostgreSQL/MySQL:** Trip records, user data. Use for: ACID transactions (payment, trip completion), complex queries (analytics), persistent storage.

- **Kafka:** Event streaming. Use for: Trip events (requested, matched, started, completed), analytics pipeline, audit logs.

- **Google Maps API / Mapbox:** Routing and ETA. Use for: Road network data, traffic information, distance calculation, turn-by-turn navigation.

---

## 📐 10. Architecture/Formula:

**Haversine Distance Formula:**

```
Distance = 2 × R × arcsin(√(sin²(Δlat/2) + cos(lat1) × cos(lat2) × sin²(Δlong/2)))

Where:
R = Earth radius = 6371 km
Δlat = lat2 - lat1 (in radians)
Δlong = long2 - long1 (in radians)

Example:
Rider: 28.6139°N, 77.2090°E (Delhi)
Driver: 28.6200°N, 77.2150°E

Δlat = (28.6200 - 28.6139) × π/180 = 0.00106 radians
Δlong = (77.2150 - 77.2090) × π/180 = 0.00105 radians

Distance = 2 × 6371 × arcsin(√(sin²(0.00053) + cos(28.6139°) × cos(28.6200°) × sin²(0.000525)))
         ≈ 0.75 km (750 meters)
```

**ETA Calculation:**

```
ETA = Distance / (Average_Speed × Traffic_Factor)

Where:
Average_Speed = Historical data (e.g., 30 km/h in city)
Traffic_Factor = Current traffic (0.5 = heavy, 1.0 = normal, 1.5 = light)

Example:
Distance = 5 km
Average_Speed = 30 km/h
Traffic_Factor = 0.7 (moderate traffic)

ETA = 5 / (30 × 0.7) = 5 / 21 = 0.238 hours = 14.3 minutes

Add buffer (10%): 14.3 × 1.1 = 15.7 minutes ≈ 16 minutes
```

**Surge Pricing Formula:**

```
Surge_Multiplier = 1 + (Demand - Supply) / Supply × Sensitivity

Where:
Demand = Active ride requests
Supply = Available drivers
Sensitivity = 0.5 (tunable parameter)

Example:
Demand = 1000 requests
Supply = 500 drivers
Sensitivity = 0.5

Surge_Multiplier = 1 + (1000 - 500) / 500 × 0.5
                 = 1 + 500/500 × 0.5
                 = 1 + 0.5
                 = 1.5x

Base_Fare = $10
Surge_Fare = $10 × 1.5 = $15

Caps: Min = 1.0x (no surge), Max = 5.0x (extreme surge)
```

**Matching Score Formula:**

```
Match_Score = (Distance_Score × 0.7) + (ETA_Score × 0.3)

Where:
Distance_Score = 1 - (Distance / Max_Distance)
ETA_Score = 1 - (ETA / Max_ETA)

Example:
Driver1: Distance = 0.5 km, ETA = 2 min
Driver2: Distance = 1.0 km, ETA = 3 min
Max_Distance = 5 km, Max_ETA = 10 min

Driver1_Score = (1 - 0.5/5) × 0.7 + (1 - 2/10) × 0.3
              = 0.9 × 0.7 + 0.8 × 0.3
              = 0.63 + 0.24 = 0.87

Driver2_Score = (1 - 1.0/5) × 0.7 + (1 - 3/10) × 0.3
              = 0.8 × 0.7 + 0.7 × 0.3
              = 0.56 + 0.21 = 0.77

Driver1 wins (higher score)
```

---

## 💻 11. Code / Flowchart:

**Flowchart (Ride Matching):**

```
START: Rider requests ride
  |
  v
[Get rider location]
lat = 28.6139, long = 77.2090
  |
  v
[Convert to Geohash]
geohash = encode(lat, long, precision=6)
Result: "ttcgx2"
  |
  v
[Query nearby drivers]
Redis: GEORADIUS key lat long 5 km
  |
  v
[Get top 10 drivers]
drivers = [d1, d2, d3, ..., d10]
  |
  v
[Calculate distance for each]
for driver in drivers:
    distance = haversine(rider, driver)
  |
  v
[Calculate ETA for each]
for driver in drivers:
    eta = distance / (speed × traffic)
  |
  v
[Calculate match score]
for driver in drivers:
    score = distance×0.7 + eta×0.3
  |
  v
[Sort by score (descending)]
sorted_drivers = sort(drivers, key=score)
  |
  v
[Send to top 3 drivers]
for driver in sorted_drivers[:3]:
    send_notification(driver)
  |
  v
[Wait for acceptance (30 sec timeout)]
  |
  +---> Driver accepts? → Match confirmed
  |
  +---> Timeout? → Try next driver
  |
  v
END
```

**Code (Simplified Matching Service):**

```python
import math
import redis
from typing import List, Tuple

class UberMatchingService:
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379)
    
    def haversine_distance(self, lat1: float, lon1: float, 
                          lat2: float, lon2: float) -> float:
        """Calculate distance between two points (km)"""
        R = 6371  # Earth radius in km
        
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        
        a = (math.sin(dlat/2)**2 + 
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * 
             math.sin(dlon/2)**2)
        
        c = 2 * math.asin(math.sqrt(a))
        return R * c
    
    def calculate_eta(self, distance: float, traffic_factor: float = 0.7) -> float:
        """Calculate ETA in minutes"""
        avg_speed = 30  # km/h in city
        eta_hours = distance / (avg_speed * traffic_factor)
        return eta_hours * 60  # Convert to minutes
    
    def find_nearby_drivers(self, rider_lat: float, rider_lon: float, 
                           radius_km: float = 5) -> List[dict]:
        """Find drivers within radius using Redis GEORADIUS"""
        # Redis geospatial query
        drivers = self.redis.georadius(
            'drivers:location',
            rider_lon, rider_lat,
            radius_km, unit='km',
            withdist=True,
            withcoord=True
        )
        
        return [
            {
                'id': driver[0].decode(),
                'distance': driver[1],
                'lat': driver[2][1],
                'lon': driver[2][0]
            }
            for driver in drivers
        ]
    
    def match_rider_to_driver(self, rider_lat: float, rider_lon: float):
        """Main matching logic"""
        # Find nearby drivers
        drivers = self.find_nearby_drivers(rider_lat, rider_lon)
        
        if not drivers:
            return None  # No drivers available
        
        # Calculate scores
        for driver in drivers:
            distance = driver['distance']
            eta = self.calculate_eta(distance)
            
            # Match score (distance 70%, ETA 30%)
            distance_score = 1 - (distance / 5)  # Normalize by max 5 km
            eta_score = 1 - (eta / 10)  # Normalize by max 10 min
            
            driver['score'] = (distance_score * 0.7) + (eta_score * 0.3)
            driver['eta'] = eta
        
        # Sort by score (highest first)
        drivers.sort(key=lambda d: d['score'], reverse=True)
        
        # Return top driver
        best_driver = drivers[0]
        return {
            'driver_id': best_driver['id'],
            'distance': round(best_driver['distance'], 2),
            'eta': round(best_driver['eta'], 1),
            'score': round(best_driver['score'], 2)
        }

# Usage
service = UberMatchingService()

# Rider requests ride
rider_location = (28.6139, 77.2090)  # Delhi
match = service.match_rider_to_driver(*rider_location)

if match:
    print(f"✅ Matched with driver {match['driver_id']}")
    print(f"📍 Distance: {match['distance']} km")
    print(f"⏱️ ETA: {match['eta']} minutes")
else:
    print("❌ No drivers available")
```

---

## 📈 12. Trade-offs:

- **Gain:** Fast matching (<10ms), accurate ETA (90%), real-time tracking | **Loss:** Complex geospatial indexing, high infrastructure cost ($1B/year), battery drain (GPS every 4 sec)

- **Gain:** Geohash simple to implement, prefix-based search efficient | **Loss:** Edge cases (geohash boundaries - nearby locations different prefixes), less accurate than QuadTree

- **Gain:** Surge pricing balances supply-demand, incentivizes drivers | **Loss:** User backlash (expensive during peak), regulatory issues (some cities ban surge)

- **When to use:** Ride-hailing (Uber, Lyft), food delivery (DoorDash, Zomato), location-based services (Tinder, Airbnb) | **When to skip:** Static locations (no real-time updates needed), small scale (<1000 drivers), no matching needed

---

## 🐞 13. Common Mistakes:

- **Mistake:** Linear search through all drivers (no geospatial indexing)
  - **Why wrong:** 100K drivers × distance calculation = 10 seconds
  - **What happens:** Slow matching, rider waits, cancels ride
  - **Fix:** Geohash/QuadTree indexing (search only nearby drivers in <10ms)

- **Mistake:** Stale driver locations (update every 5 minutes)
  - **Why wrong:** Driver moved 5 km in 5 min, rider sees wrong location
  - **What happens:** Inaccurate ETA, rider frustration
  - **Fix:** Real-time updates every 4 seconds (WebSocket)

- **Mistake:** Matching only by distance (ignoring ETA)
  - **Why wrong:** Closest driver stuck in traffic (20 min ETA), farther driver on highway (5 min ETA)
  - **What happens:** Suboptimal matching, longer wait times
  - **Fix:** Combined score (distance 70% + ETA 30%)

- **Mistake:** No surge pricing (fixed pricing always)
  - **Why wrong:** Peak demand (1000 requests, 100 drivers) → 900 riders wait forever
  - **What happens:** Poor supply-demand balance, riders can't get rides
  - **Fix:** Dynamic surge pricing (incentivizes more drivers to come online)

---

## ✅ 14. Zaroori Notes for Interview:

**Must Mention Points:**
1. **Start with geospatial indexing:** "Uber ka core Geohash/QuadTree hai. Location ko encode karke nearby drivers efficiently dhundte hain. Geohash: lat/long → string ('ttcgx2'), prefix match se nearby search (<10ms vs 1 sec linear)."

2. **Draw architecture:** Rider request → Geohash encoding → Redis query (nearby drivers) → Calculate distance (Haversine) → Calculate ETA (traffic-aware) → Rank drivers → Send to top 3 → First accepts.

3. **Explain matching algorithm:** "Score = Distance×0.7 + ETA×0.3. Distance important but ETA bhi (traffic consider). Top driver ko assign."

4. **Common follow-ups:**
   - **"Geohash vs QuadTree?"** → Geohash: Simple, string-based, prefix search. QuadTree: More accurate, handles boundaries better, complex. Uber uses Geohash (simpler at scale).
   - **"Real-time location kaise track?"** → WebSocket connection, GPS update every 4 sec, Redis write (fast), broadcast to rider (if matched).
   - **"ETA kaise calculate?"** → Distance (Haversine) / (Avg speed × Traffic factor). Traffic from Google Maps API or internal data. 90% accuracy.
   - **"Surge pricing kaise decide?"** → Demand/Supply ratio. Formula: 1 + (Demand-Supply)/Supply × 0.5. Example: 1000 requests, 500 drivers → 1.5x surge.

5. **Mention scale:** "Uber: 23M trips/day, 5M drivers, 100K requests/sec peak, <50ms matching time."

6. **Pro tip:** "Interview mein Haversine formula mention karo (distance calculation). Aur Geohash precision levels (6 char = 610m). Shows technical depth."

---

## ❓ 15. FAQ & Comparisons (MANDATORY - 5 Questions):

**Q1: Geohash vs QuadTree - Kaunsa better for Uber?**
A: **Geohash:** String-based encoding (lat/long → "ttcgx2"), prefix search (SQL LIKE 'ttcgx%'), simple implementation. **Pros:** Easy to store (string column), database-friendly, scales well. **Cons:** Boundary issues (nearby locations different prefixes). **QuadTree:** Tree structure, recursively divide space into 4 quadrants. **Pros:** No boundary issues, more accurate. **Cons:** Complex implementation, in-memory structure (not DB-friendly). **Best:** Geohash for production (Uber, Lyft use it) - simpler at scale. QuadTree for in-memory caching (hot areas).

**Q2: Driver location update frequency - 4 sec vs 10 sec vs 1 min?**
A: **4 seconds (Uber):** Accurate real-time tracking, smooth rider experience, high battery drain (GPS active), high server load (1M drivers × 15 updates/min = 15M writes/min). **10 seconds:** Balanced (less battery, acceptable accuracy). **1 minute:** Stale data (driver moved 1 km), poor ETA accuracy. **Trade-off:** Accuracy vs Battery vs Server load. **Best:** 4 sec during active trip (rider watching), 30 sec when idle (driver waiting for request). **Battery optimization:** Use cell tower triangulation (less accurate but 10x less battery) when not in trip.

**Q3: Matching algorithm - Distance only vs Distance+ETA vs ML-based?**
A: **Distance only:** Simple, fast, but suboptimal (closest driver in traffic = long wait). **Distance + ETA:** Balanced (70% distance, 30% ETA), considers traffic, 90% rider satisfaction. **ML-based:** Predicts best match using 100+ features (driver rating, acceptance rate, historical performance), 95% satisfaction but complex. **Uber evolution:** Started with distance-only (2010) → Distance+ETA (2014) → ML-based (2018). **Best:** Distance+ETA for most cases (simple, effective), ML for optimization (marginal 5% improvement).

**Q4: Surge pricing - Kaise implement karein without user backlash?**
A: **Transparent communication:** Show surge multiplier upfront (1.5x, 2x), explain reason ("High demand in your area"). **Caps:** Max 5x surge (prevent extreme prices). **Alternatives:** Offer scheduled rides (no surge, wait 15 min). **Notifications:** "Surge ending soon" (incentivize waiting). **Gradual increase:** 1.2x → 1.5x → 2x (not sudden 3x). **Uber approach:** Heat map showing surge areas (users can walk to lower surge zone). **Regulation:** Some cities ban surge (NYC caps at 2x) - need compliance.

**Q5: Trip state machine - Kaise design karein?**
A: **States:** REQUESTED → MATCHED → ACCEPTED → STARTED → COMPLETED → PAID. **Transitions:** Only valid transitions allowed (can't COMPLETE before START). **Implementation:** Database column (trip_state), state transition table (valid moves), event-driven (Kafka events for each transition). **Idempotency:** Duplicate events ignored (START event twice → process once). **Rollback:** MATCHED → CANCELLED (driver/rider cancels), STARTED → CANCELLED (emergency). **Analytics:** Track state durations (REQUESTED→MATCHED avg 30 sec - KPI). **Uber:** Uses state machine with 15+ states (including DRIVER_ARRIVED, RIDER_PICKUP, etc.).

---

## 🎯 Module 20 Complete Summary:

**All Topics Covered:** 1/1 ✅
- ✅ Topic 20.1: Uber System - Geospatial Indexing (Geohash/QuadTree), Real-time Location Tracking, Matching Algorithm, ETA Calculation, Surge Pricing

**Key Takeaways:**
1. **Geospatial Indexing:** Geohash encodes lat/long to string ("ttcgx2"), prefix search finds nearby drivers in <10ms (vs 1 sec linear)
2. **Real-time Tracking:** WebSocket connection, GPS updates every 4 sec, Redis for fast writes, broadcast to rider
3. **Matching Algorithm:** Score = Distance×0.7 + ETA×0.3, considers traffic, top driver assigned
4. **ETA Calculation:** Haversine distance / (Avg speed × Traffic factor), 90% accuracy within 2 min
5. **Surge Pricing:** Formula: 1 + (Demand-Supply)/Supply × 0.5, balances supply-demand, caps at 5x

**Interview Focus:**
- Draw architecture: Rider → Geohash → Redis query → Distance calc → ETA calc → Rank → Match
- Explain Haversine formula for distance calculation
- Discuss Geohash precision levels (6 char = 610m)
- Mention real-time updates (WebSocket, 4 sec frequency)
- Real-world: Uber (23M trips/day, 5M drivers, <50ms matching)

**Progress:** 20/21 Modules Completed 🎉

**Next Module:** Module 21 - Design E-Commerce (Amazon) - Final Module!

---
