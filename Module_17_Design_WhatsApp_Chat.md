# Module 17: Design WhatsApp/Chat System

## Topic 17.1: Chat System Architecture - WebSockets & Message Storage

---

## 🎯 1. Title / Topic: WhatsApp/Chat System (Real-time Messaging)

---

## 🐣 2. Samjhane ke liye (Simple Analogy):

WhatsApp ek **Walkie-Talkie System** jaisa hai jo instant communication provide karta hai. Jaise walkie-talkie mein aap button press karo aur dusra person turant sun leta hai (real-time), waise hi WhatsApp mein message bhejo aur receiver ko instantly mil jata hai. **Post Office** (Email) mein letter bhejne mein hours lagte hain, but **Walkie-Talkie** (WhatsApp) instant hai. Technical term: **WebSocket** connection jo hamesha open rahta hai (like walkie-talkie channel always on), HTTP request-response se better (like post office - har baar letter bhejne jaana padta hai).

---

## 📖 3. Technical Definition (Interview Answer):

**Chat System** is a real-time messaging platform using WebSocket protocol for bidirectional communication, with message storage in NoSQL databases (Cassandra/HBase), message queues (Kafka) for reliability, and end-to-end encryption (Signal Protocol) for security.

**Key terms:**
- **WebSocket:** Persistent TCP connection for real-time bidirectional communication (vs HTTP request-response)
- **Message Queue:** Kafka/RabbitMQ for reliable message delivery (sender → queue → receiver)
- **Message Storage:** Cassandra/HBase for chat history (billions of messages, time-series data)
- **Presence Service:** Online/Offline status tracking (last seen, typing indicator)
- **End-to-End Encryption:** Signal Protocol (Double Ratchet) - only sender/receiver can read
- **Message Ticks:** Single tick (sent), Double tick (delivered), Blue tick (read)

---

## 🧠 4. Zaroorat Kyun Hai? (Why?):

**Main Problem:** HTTP polling (har 5 sec request bhejo "new message?") inefficient hai - 1000 users × 12 requests/min = 12K requests/min (mostly empty responses). WebSocket se 1000 persistent connections (idle until message), 99% bandwidth saved.

**Business Impact:** WhatsApp: 100B messages/day, 2B users. Without real-time architecture, impossible to scale. Telegram tried HTTP long-polling initially → Switched to WebSocket → 10x efficiency improvement.

**Technical Benefits:**
- **Real-time:** <100ms message delivery (vs 5 sec polling delay)
- **Efficiency:** 1 persistent connection vs 12 requests/min (99% bandwidth saved)
- **Scalability:** 1M concurrent connections per server (C10K problem solved)
- **Reliability:** Message queue ensures delivery even if receiver offline
- **Privacy:** End-to-end encryption (WhatsApp can't read messages)

---

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario):

**Scenario: HTTP Polling (No WebSocket)**
- 1M users online
- Poll every 5 seconds: "Any new message?"
- Requests: 1M × 12/min = 12M requests/min = 200K requests/sec
- 95% empty responses (no new message)
- Server load: 200K req/sec × 50ms = 10,000 CPU-seconds/sec = 10,000 cores needed
- Cost: $100K/month (vs $10K with WebSocket)

**Real Example:** **Facebook Chat (2008)** - Initially used HTTP polling → Server overload at 100K concurrent users → Switched to Comet (long-polling) then WebSocket (2010) → Scaled to 1B users. Without WebSocket, Facebook Messenger wouldn't exist at current scale.

---

## ⚙️ 6. Under the Hood (Technical Working):

**Message Sending Flow:**

1. **User Types:** "Hello" in chat
2. **WebSocket Send:** Client sends message via WebSocket connection
3. **Chat Server:** Receives message, validates
4. **Message ID:** Generate unique ID (timestamp + user_id + random)
5. **Persistence:** Store in Cassandra (sender_id, receiver_id, message, timestamp)
6. **Queue:** Push to Kafka (reliable delivery)
7. **Receiver Online?** Check presence service
   - **Online:** Forward via WebSocket → Instant delivery
   - **Offline:** Store in queue, deliver when online
8. **Acknowledgment:** Send ACK to sender (single tick ✓)
9. **Delivery Confirmation:** Receiver gets message → Send ACK (double tick ✓✓)
10. **Read Receipt:** Receiver opens chat → Send read ACK (blue tick ✓✓)

**WebSocket Connection Management:**

```
CLIENT                          CHAT SERVER
  |                                  |
  | (1) HTTP Upgrade Request         |
  |--------------------------------->|
  |    GET /chat HTTP/1.1            |
  |    Upgrade: websocket            |
  |    Connection: Upgrade           |
  |                                  |
  | (2) HTTP 101 Switching Protocols |
  |<---------------------------------|
  |    Upgrade: websocket            |
  |    Connection: Upgrade           |
  |                                  |
  | (3) WebSocket Connection Open    |
  |==================================| (Persistent TCP)
  |                                  |
  | (4) Send Message: "Hello"        |
  |--------------------------------->|
  |                                  |
  | (5) Receive ACK (✓)              |
  |<---------------------------------|
  |                                  |
  | (6) Receive Message: "Hi"        |
  |<---------------------------------|
  |                                  |
  | (7) Send Read Receipt            |
  |--------------------------------->|
  |                                  |
  |==================================| (Connection stays open)
  |                                  |
  | (8) Heartbeat (every 30 sec)     |
  |<------------------------------->|
  |      (Keep connection alive)     |
```

**ASCII Architecture Diagram:**

```
[USER A - Mobile App]
     |
     | WebSocket Connection
     v
+---------------------------+
|   LOAD BALANCER           |
|   (Sticky Session)        |
+---------------------------+
     |
     v
+---------------------------+
|   CHAT SERVER (Node 1)    |
|   - WebSocket Handler     |
|   - Connection Manager    |
|   - 1M connections        |
+---------------------------+
     |
     | (1) Store Message
     v
+---------------------------+
|   MESSAGE QUEUE (Kafka)   |
|   - Reliable Delivery     |
|   - Partition by user_id  |
+---------------------------+
     |
     | (2) Persist
     v
+---------------------------+
|   CASSANDRA CLUSTER       |
|   - Chat History          |
|   - Partition: user_id    |
|   - Sort: timestamp       |
+---------------------------+
     |
     | (3) Check Receiver Status
     v
+---------------------------+
|   PRESENCE SERVICE        |
|   (Redis)                 |
|   user_b: online, ws_node2|
+---------------------------+
     |
     | (4) Route to Receiver
     v
+---------------------------+
|   CHAT SERVER (Node 2)    |
|   - User B connected here |
+---------------------------+
     |
     | WebSocket Push
     v
[USER B - Mobile App]


DETAILED MESSAGE FLOW:

[User A sends "Hello" to User B]
     |
     v
[Chat Server Node-1]
     |
     +---> (1) Generate Message ID
     |         msg_id = timestamp_userid_random
     |         "1640000000_userA_abc123"
     |
     +---> (2) Store in Cassandra
     |         INSERT INTO messages
     |         (msg_id, sender, receiver, text, timestamp)
     |
     +---> (3) Push to Kafka
     |         Topic: "chat_messages"
     |         Partition: hash(user_b) % partitions
     |
     +---> (4) Check Presence
     |         Redis: GET "presence:user_b"
     |         Result: {status: "online", server: "node-2"}
     |
     +---> (5) Forward to Node-2
     |         Internal RPC call
     |         (or via Kafka consumer on Node-2)
     |
     v
[Chat Server Node-2]
     |
     +---> (6) Push via WebSocket
     |         ws.send({msg_id, sender, text, timestamp})
     |
     v
[User B receives "Hello"]
     |
     +---> (7) Send Delivery ACK
     |         {msg_id, status: "delivered"}
     |
     v
[Chat Server Node-2]
     |
     +---> (8) Update Message Status
     |         Cassandra: UPDATE messages
     |         SET status = "delivered"
     |
     +---> (9) Notify User A
     |         Forward ACK to Node-1 → User A
     |         (Double tick ✓✓ appears)
     |
     v
[User A sees double tick ✓✓]


OFFLINE MESSAGE HANDLING:

[User A sends message to User B (offline)]
     |
     v
[Chat Server]
     |
     +---> (1) Store in Cassandra (persistent)
     |
     +---> (2) Push to Kafka Queue
     |         (message waits in queue)
     |
     +---> (3) Check Presence
     |         Redis: user_b = "offline"
     |
     +---> (4) Store in Offline Queue
     |         Redis: LPUSH "offline:user_b" msg_id
     |
     v
[User B comes online]
     |
     v
[Chat Server]
     |
     +---> (5) Fetch Offline Messages
     |         Redis: LRANGE "offline:user_b" 0 -1
     |         Result: [msg1, msg2, msg3]
     |
     +---> (6) Fetch from Cassandra
     |         SELECT * FROM messages
     |         WHERE msg_id IN (msg1, msg2, msg3)
     |
     +---> (7) Push via WebSocket
     |         Batch send all offline messages
     |
     v
[User B receives all pending messages]
```

---

## 🛠️ 7. Problems Solved:

- **Real-time Communication:** <100ms latency (vs 5 sec HTTP polling) → Instant messaging experience
- **Scalability:** 1M concurrent WebSocket connections per server (C10K problem solved with epoll/kqueue)
- **Reliability:** Message queue (Kafka) ensures delivery even if receiver offline → 99.99% delivery rate
- **Offline Support:** Messages stored in queue, delivered when user comes online → No message loss
- **Presence Tracking:** Online/Offline status, Last Seen, Typing indicator → Better UX
- **Message History:** Cassandra stores billions of messages, fast retrieval by user_id + timestamp
- **Group Chat:** Fanout to multiple receivers (1 message → N users) → Efficient with message queue

---

## 🌍 8. Real-World Example:

**WhatsApp Architecture:** 100B messages/day, 2B users, 65B messages/sec peak. Technology: Erlang for chat servers (lightweight processes, 2M connections per server), FreeBSD OS (optimized for networking), Cassandra for message storage (petabyte scale), XMPP protocol initially (now custom). Features: End-to-end encryption (Signal Protocol), message compression (reduces bandwidth 70%), media storage (S3), voice/video calls (WebRTC). Scale: 50 engineers support 2B users (highest user-to-engineer ratio). Infrastructure: 10K+ servers globally. Without WebSocket architecture, WhatsApp couldn't handle 100B messages/day (would need 1M servers with HTTP polling).

---

## 🔧 9. Tech Stack / Tools:

- **WebSocket Libraries:** Socket.io (Node.js), ws (Node.js), Netty (Java). Use for: Real-time bidirectional communication, automatic reconnection, fallback to long-polling.

- **Cassandra/HBase:** NoSQL for message storage. Use for: Time-series data (messages sorted by timestamp), horizontal scaling (petabyte scale), high write throughput (1M writes/sec).

- **Kafka:** Message queue for reliability. Use for: Guaranteed delivery, message ordering, replay capability (reprocess failed messages).

- **Redis:** Presence service + caching. Use for: Online/Offline status (fast lookup <1ms), recent messages cache (last 100 messages), typing indicators.

---

## 📐 10. Architecture/Formula:

**WebSocket Connection Capacity:**

```
Max_Connections = Available_Memory / Memory_Per_Connection

Where:
Memory_Per_Connection ≈ 4KB (TCP buffer + WebSocket overhead)
Available_Memory = Total RAM - OS - Application

Example:
Server: 64GB RAM
OS + App: 16GB
Available: 48GB = 48,000 MB

Max_Connections = 48,000 MB / 4 KB
                = 48,000 × 1024 KB / 4 KB
                = 12,288,000 connections
                ≈ 12M connections per server

Practical limit: 2M connections (CPU, network bandwidth constraints)
```

**Message Storage Calculation:**

```
Storage = Messages_Per_Day × Avg_Message_Size × Retention_Days

Example (WhatsApp scale):
Messages_Per_Day = 100 billion
Avg_Message_Size = 100 bytes (text only, compressed)
Retention_Days = 30 days

Storage = 100B × 100 bytes × 30
        = 300 TB per month
        
With replication (3x): 900 TB
With media (images/videos): 10 PB per month

Cassandra sharding: 1000 nodes × 10 TB each = 10 PB capacity
```

**Message Delivery Latency:**

```
Total_Latency = Network_RTT + Queue_Time + Processing_Time

Where:
Network_RTT = Round Trip Time (sender → server → receiver)
Queue_Time = Time in Kafka queue (if receiver offline)
Processing_Time = Server processing (validation, storage)

Example (Both users online):
Network_RTT = 50ms (sender → server) + 50ms (server → receiver) = 100ms
Queue_Time = 0ms (receiver online, direct push)
Processing_Time = 5ms (store in Cassandra + forward)

Total_Latency = 100 + 0 + 5 = 105ms

Example (Receiver offline):
Queue_Time = Variable (until receiver comes online)
When online: Batch delivery (100 messages in 1 sec)
```

**Cassandra Schema (Message Storage):**

```sql
CREATE TABLE messages (
    user_id UUID,              -- Partition key (sharding)
    conversation_id UUID,      -- Clustering key
    timestamp TIMESTAMP,       -- Clustering key (sort order)
    message_id UUID,
    sender_id UUID,
    receiver_id UUID,
    message_text TEXT,
    media_url TEXT,
    status TEXT,               -- sent, delivered, read
    PRIMARY KEY ((user_id), conversation_id, timestamp)
) WITH CLUSTERING ORDER BY (conversation_id ASC, timestamp DESC);

-- Query: Get last 50 messages for user in conversation
SELECT * FROM messages
WHERE user_id = ? AND conversation_id = ?
ORDER BY timestamp DESC
LIMIT 50;

-- Efficient: Partition by user_id (data locality)
-- Sort by timestamp (recent messages first)
-- Cassandra optimized for time-series queries
```

---

## 💻 11. Code / Flowchart:

**Flowchart (Message Sending):**

```
START: User A types "Hello"
  |
  v
[Client: Send via WebSocket]
ws.send({to: "user_b", text: "Hello"})
  |
  v
[Chat Server: Receive]
  |
  v
[Generate Message ID]
msg_id = timestamp + user_id + random
  |
  v
[Store in Cassandra]
INSERT INTO messages (...)
  |
  v
[Push to Kafka]
Topic: "chat_messages"
  |
  v
[Check Receiver Status]
Redis: GET "presence:user_b"
  |
  +---> Online? → Forward via WebSocket
  |                |
  |                v
  |           [User B receives]
  |                |
  |                v
  |           [Send Delivery ACK]
  |                |
  |                v
  |           [Update Status: delivered]
  |
  +---> Offline? → Store in offline queue
                   |
                   v
              [Wait for user to come online]
  |
  v
END
```

**Code (Simplified Chat Server - WebSocket):**

```python
import asyncio
import websockets
import json
import redis
from datetime import datetime

class ChatServer:
    def __init__(self):
        self.connections = {}  # user_id -> websocket
        self.redis = redis.Redis(host='localhost', port=6379)
    
    async def handle_connection(self, websocket, path):
        """Handle new WebSocket connection"""
        user_id = None
        
        try:
            # Authentication (simplified)
            auth_msg = await websocket.recv()
            auth_data = json.loads(auth_msg)
            user_id = auth_data['user_id']
            
            # Store connection
            self.connections[user_id] = websocket
            
            # Update presence
            self.redis.setex(f"presence:{user_id}", 300, "online")
            
            print(f"✅ User {user_id} connected")
            
            # Handle messages
            async for message in websocket:
                await self.handle_message(user_id, message)
        
        except websockets.exceptions.ConnectionClosed:
            print(f"❌ User {user_id} disconnected")
        
        finally:
            # Cleanup
            if user_id:
                self.connections.pop(user_id, None)
                self.redis.setex(f"presence:{user_id}", 300, "offline")
    
    async def handle_message(self, sender_id, message):
        """Process incoming message"""
        data = json.loads(message)
        receiver_id = data['to']
        text = data['text']
        
        # Generate message ID
        msg_id = f"{int(datetime.now().timestamp())}_{sender_id}"
        
        # Store in database (simplified - use Cassandra in production)
        self.redis.hset(f"msg:{msg_id}", mapping={
            'sender': sender_id,
            'receiver': receiver_id,
            'text': text,
            'timestamp': datetime.now().isoformat()
        })
        
        # Send ACK to sender (single tick)
        await self.send_ack(sender_id, msg_id, "sent")
        
        # Forward to receiver
        if receiver_id in self.connections:
            # Receiver online - send immediately
            receiver_ws = self.connections[receiver_id]
            await receiver_ws.send(json.dumps({
                'msg_id': msg_id,
                'from': sender_id,
                'text': text,
                'timestamp': datetime.now().isoformat()
            }))
            
            # Send delivery ACK to sender (double tick)
            await self.send_ack(sender_id, msg_id, "delivered")
        else:
            # Receiver offline - store in queue
            self.redis.lpush(f"offline:{receiver_id}", msg_id)
            print(f"📥 Message queued for offline user {receiver_id}")
    
    async def send_ack(self, user_id, msg_id, status):
        """Send acknowledgment to user"""
        if user_id in self.connections:
            ws = self.connections[user_id]
            await ws.send(json.dumps({
                'type': 'ack',
                'msg_id': msg_id,
                'status': status
            }))

# Start server
async def main():
    server = ChatServer()
    async with websockets.serve(server.handle_connection, "localhost", 8765):
        print("🚀 Chat server running on ws://localhost:8765")
        await asyncio.Future()  # Run forever

# Run
asyncio.run(main())
```

---

## 📈 12. Trade-offs:

- **Gain:** Real-time (<100ms), efficient (1 connection vs 12 req/min), scalable (1M connections/server) | **Loss:** Complex (WebSocket management, connection state), stateful servers (sticky sessions needed)

- **Gain:** Reliable delivery (Kafka queue), offline support (messages queued) | **Loss:** Storage cost (Cassandra petabyte scale), eventual consistency (message may arrive out of order)

- **Gain:** Presence tracking (online/offline), typing indicators, read receipts | **Loss:** Privacy concerns (last seen tracking), extra infrastructure (Redis for presence)

- **When to use:** Real-time chat (WhatsApp, Slack), live updates (stock prices, sports scores), collaborative editing (Google Docs) | **When to skip:** Simple notifications (email sufficient), low-frequency updates (<1/min), one-way communication (no bidirectional needed)

---

## 🐞 13. Common Mistakes:

- **Mistake:** Using HTTP polling instead of WebSocket
  - **Why wrong:** 12 requests/min per user → 1M users = 200K req/sec (95% empty responses)
  - **What happens:** Server overload, high bandwidth cost, 5 sec delay (bad UX)
  - **Fix:** WebSocket persistent connection (idle until message, <100ms latency)

- **Mistake:** Storing messages in SQL database (MySQL)
  - **Why wrong:** Relational DB not optimized for time-series data, slow for billions of rows
  - **What happens:** Slow queries (>1 sec to fetch chat history), can't scale horizontally
  - **Fix:** Cassandra/HBase (NoSQL, time-series optimized, petabyte scale)

- **Mistake:** No message queue (direct WebSocket forwarding)
  - **Why wrong:** Receiver offline → Message lost (sender thinks delivered but receiver never gets)
  - **What happens:** Message loss, poor reliability, user complaints
  - **Fix:** Kafka queue (messages persist until delivered, replay possible)

- **Mistake:** Single chat server (no load balancing)
  - **Why wrong:** 1 server = 2M connections max → Can't scale beyond 2M users
  - **What happens:** Server crash at scale, downtime, can't handle growth
  - **Fix:** Multiple chat servers + Load balancer with sticky sessions (user always connects to same server)

---

## ✅ 14. Zaroori Notes for Interview:

**Must Mention Points:**
1. **Start with WebSocket:** "Chat system ka core WebSocket hai - persistent TCP connection jo bidirectional communication allow karta hai. HTTP polling se 99% efficient (1 connection vs 12 req/min)."

2. **Draw architecture:** User A → WebSocket → Chat Server → Kafka Queue → Cassandra (storage) → Chat Server → WebSocket → User B. Mention presence service (Redis) for online/offline status.

3. **Explain message flow:** Send → Generate ID → Store Cassandra → Push Kafka → Check presence → Forward (if online) or Queue (if offline) → ACK (single/double/blue tick).

4. **Common follow-ups:**
   - **"WebSocket vs HTTP polling?"** → WebSocket: 1 persistent connection, <100ms latency, 99% bandwidth saved. Polling: 12 req/min, 5 sec delay, 95% empty responses.
   - **"Message storage kaise?"** → Cassandra (NoSQL, time-series optimized). Partition by user_id, sort by timestamp. Query: Last 50 messages in <10ms.
   - **"Offline messages kaise handle?"** → Kafka queue + Redis offline list. When user online, fetch from queue, batch deliver.
   - **"Group chat kaise?"** → Fanout: 1 message → N receivers. Kafka partition by group_id, workers fanout to all members.
   - **"Encryption kaise?"** → End-to-end (Signal Protocol - Double Ratchet). Server can't read, only sender/receiver have keys.

5. **Mention scale:** "WhatsApp: 100B messages/day, 2B users, 2M connections per server (Erlang). Cassandra petabyte storage."

6. **Pro tip:** "Interview mein WebSocket handshake draw karo (HTTP Upgrade → 101 Switching Protocols). Aur message ticks explain karo (✓ sent, ✓✓ delivered, ✓✓ blue read). Shows attention to detail."

---

## ❓ 15. FAQ & Comparisons (MANDATORY - 5 Questions):

**Q1: WebSocket vs HTTP Long-Polling - Kaunsa better for chat?**
A: **WebSocket:** Persistent connection (always open), bidirectional (server can push), <100ms latency, efficient (no HTTP overhead per message). **Long-Polling:** HTTP request waits (30-60 sec timeout), server responds when message arrives, then reconnect. Less efficient (HTTP headers per message), but works with old browsers. **Best:** WebSocket for modern chat (WhatsApp, Slack). Long-polling as fallback (Socket.io does this automatically). **Scale:** WebSocket handles 1M connections/server, Long-polling only 10K (connection overhead).

**Q2: Cassandra vs MongoDB for message storage - Kaunsa choose karein?**
A: **Cassandra:** Time-series optimized (messages sorted by timestamp), horizontal scaling (petabyte scale), high write throughput (1M writes/sec), eventual consistency. **MongoDB:** Document-based, flexible schema, strong consistency, but limited scale (100TB max practical). **Best:** Cassandra for chat (WhatsApp, Facebook Messenger use it). Reason: Billions of messages, time-series queries (last 50 messages), write-heavy (100B messages/day). MongoDB OK for small chat (<1M messages/day).

**Q3: Message ticks (✓, ✓✓, ✓✓ blue) kaise implement karein?**
A: **Single Tick (✓):** Message sent to server → Server ACK → Update UI. **Double Tick (✓✓):** Message delivered to receiver's device → Receiver ACK → Forward to sender → Update UI. **Blue Tick (✓✓):** Receiver opens chat → Read receipt sent → Forward to sender → Update UI (blue). **Implementation:** Message status in Cassandra (sent/delivered/read), ACK messages via WebSocket, UI updates on ACK. **Privacy:** User can disable read receipts (blue tick) in settings. **WhatsApp:** Uses this exact system.

**Q4: Group chat mein message kaise deliver karein (1 message → 1000 members)?**
A: **Approach 1 (Fanout on Write):** Sender sends 1 message → Server creates 1000 copies → Store in each member's inbox → Deliver individually. **Pros:** Fast read (each user has own copy), **Cons:** Slow write (1000 DB writes), storage waste (1000 copies). **Approach 2 (Fanout on Read):** Store 1 message → Each member reads from shared location. **Pros:** Fast write (1 write), less storage, **Cons:** Slow read (N users query same message). **Best:** Hybrid - Fanout on write for small groups (<100), Fanout on read for large groups (>100). **WhatsApp:** Uses fanout on write (max 256 members).

**Q5: End-to-end encryption kaise implement karein (Signal Protocol)?**
A: **Key Exchange:** Sender aur receiver ke beech public key exchange (Diffie-Hellman). **Encryption:** Sender message ko receiver's public key se encrypt → Server ko encrypted message milta hai (can't read) → Receiver apni private key se decrypt. **Double Ratchet:** Har message ke liye new key generate (forward secrecy - agar ek key leak toh sirf ek message compromise). **Implementation:** Signal Protocol library use karo (WhatsApp, Signal app use karte hain). **Server Role:** Sirf encrypted message forward karta hai, content nahi dekh sakta. **Metadata:** Server ko sender/receiver/timestamp pata hai (encrypted nahi), but message content encrypted.

---



---

## 🎯 Module 17 Complete Summary:

**All Topics Covered:** 1/1 ✅
- ✅ Topic 17.1: WhatsApp/Chat System - WebSocket Architecture, Message Storage (Cassandra), Presence Service, Message Ticks, End-to-End Encryption

**Key Takeaways:**
1. **WebSocket:** Persistent TCP connection for real-time bidirectional communication, 99% more efficient than HTTP polling (1 connection vs 12 req/min)
2. **Message Storage:** Cassandra/HBase for time-series data (partition by user_id, sort by timestamp), petabyte scale, 1M writes/sec
3. **Message Queue:** Kafka for reliable delivery, offline message handling, guaranteed delivery even if receiver offline
4. **Presence Service:** Redis for online/offline status, last seen, typing indicators (<1ms lookup)
5. **Message Ticks:** Single tick (✓ sent), Double tick (✓✓ delivered), Blue tick (✓✓ read) - ACK-based system
6. **Encryption:** Signal Protocol (Double Ratchet) for end-to-end encryption, server can't read messages

**Interview Focus:**
- Draw WebSocket handshake: HTTP Upgrade → 101 Switching Protocols → Persistent connection
- Explain message flow: Send → Store Cassandra → Push Kafka → Check presence → Forward/Queue → ACK
- Discuss offline handling: Kafka queue + Redis offline list, batch delivery when user online
- Mention scale: WhatsApp (100B messages/day, 2B users, 2M connections/server with Erlang)
- Compare WebSocket vs HTTP polling (99% bandwidth saved)

**Production Patterns:**
- **Connection Management:** Sticky sessions (user always connects to same server), heartbeat every 30 sec
- **Message Delivery:** Kafka for reliability, Cassandra for persistence, Redis for caching recent messages
- **Group Chat:** Fanout on write for small groups (<100), fanout on read for large groups (>100)
- **Scalability:** 1M concurrent WebSocket connections per server (C10K problem solved)

**Scale Numbers:**
- WhatsApp: 100B messages/day, 2B users, 65B messages/sec peak
- Connection capacity: 2M per server (Erlang), 12M theoretical (limited by CPU/network)
- Storage: 300TB/month (text only), 10PB with media
- Latency: <100ms message delivery (both users online)

**Progress:** 17/21 Modules Completed 🎉

**Next Module:** Module 18 - Design Instagram/Newsfeed (Feed Generation, Fanout, Timeline)

---
