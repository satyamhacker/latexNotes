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
# Import asyncio for asynchronous I/O (non-blocking operations)
# Async = Multiple tasks run concurrently without waiting (like cooking multiple dishes)
import asyncio

# Import websockets library for WebSocket protocol implementation
# WebSocket = Persistent TCP connection for real-time bidirectional communication
import websockets

# Import json for parsing message data (convert string ↔ Python dict)
import json

# Import redis for presence tracking and message storage (fast in-memory database)
# Redis used for: online/offline status, offline message queue, recent messages cache
import redis

# Import datetime for timestamp generation (message ordering, uniqueness)
from datetime import datetime

class ChatServer:
    def __init__(self):
        """
        Initialize Chat Server
        Sets up connection tracking and Redis client for presence/storage
        """
        # Dictionary to track active WebSocket connections
        # Structure: {user_id: websocket_object}
        # Example: {"user123": <WebSocket object>, "user456": <WebSocket object>}
        # Why dictionary? O(1) lookup to find user's WebSocket connection for message delivery
        self.connections = {}
        
        # Redis client for presence tracking and message storage
        # Production uses: Redis Cluster for high availability (multiple nodes)
        # Here: localhost for simplicity (single Redis instance)
        self.redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
    
    async def handle_connection(self, websocket, path):
        """
        Handle new WebSocket connection (called for each client connection)
        Flow: Authenticate → Store connection → Update presence → Listen for messages
        
        async = Function runs asynchronously (doesn't block, other connections can process)
        websocket = WebSocket object for this specific client connection
        path = URL path from WebSocket request (e.g., "/chat")
        """
        # Variable to track user_id (None initially, set after authentication)
        # Important for cleanup in finally block (if connection fails during auth)
        user_id = None
        
        try:
            # ========== STEP 1: AUTHENTICATION ==========
            # Wait for first message from client (authentication data)
            # await = Pause here until message arrives (non-blocking, other connections continue)
            # recv() = Receive message from WebSocket (blocking call made async)
            auth_msg = await websocket.recv()
            
            # Parse JSON authentication message
            # Expected format: {"user_id": "user123", "token": "auth_token_xyz"}
            # Production: Verify JWT token here, check expiry, validate signature
            auth_data = json.loads(auth_msg)
            
            # Extract user_id from authentication data
            # Production validation: Check if user exists in database, token valid, not banned
            user_id = auth_data['user_id']
            
            # ========== STEP 2: STORE CONNECTION ==========
            # Store WebSocket connection in dictionary for fast lookup
            # When message arrives for this user, we can instantly find their WebSocket
            # Why store? To push messages to user (server → client communication)
            self.connections[user_id] = websocket
            
            # ========== STEP 3: UPDATE PRESENCE (ONLINE STATUS) ==========
            # Mark user as online in Redis (fast lookup for presence queries)
            # SETEX = SET with EXpiry (key, ttl_seconds, value)
            # TTL = 300 seconds (5 minutes) - auto-expire if connection drops
            # Why TTL? If server crashes, presence auto-clears after 5 min (stale data prevented)
            self.redis.setex(f"presence:{user_id}", 300, "online")
            
            # Log successful connection (for debugging/monitoring)
            print(f"✅ User {user_id} connected")
            
            # ========== STEP 4: LISTEN FOR MESSAGES (MAIN LOOP) ==========
            # async for = Asynchronously iterate over incoming WebSocket messages
            # Loop continues until WebSocket connection closes
            # Each iteration processes one message from client
            async for message in websocket:
                # Handle incoming message (send to receiver, store, ACK, etc.)
                # await = Process this message asynchronously (don't block other connections)
                await self.handle_message(user_id, message)
        
        except websockets.exceptions.ConnectionClosed:
            # Connection closed by client (user closed app, network issue, etc.)
            # This is normal behavior, not an error
            print(f"❌ User {user_id} disconnected")
        
        finally:
            # ========== CLEANUP (ALWAYS RUNS) ==========
            # Cleanup code runs whether connection succeeds or fails
            # Important: Remove connection and update presence
            
            if user_id:
                # Remove WebSocket from connections dictionary
                # pop(key, default) = Remove key, return default if not exists (no error)
                self.connections.pop(user_id, None)
                
                # Mark user as offline in Redis
                # Still use SETEX (not permanent) in case user reconnects quickly
                # TTL = 300 seconds, then auto-delete (cleanup stale offline status)
                self.redis.setex(f"presence:{user_id}", 300, "offline")
    
    async def handle_message(self, sender_id, message):
        """
        Process incoming message from sender
        Flow: Parse → Generate ID → Store → Queue → Check receiver status → Forward/Queue
        
        sender_id: User who sent the message (e.g., "user123")
        message: JSON string from WebSocket (e.g., '{"to": "user456", "text": "Hello"}')
        """
        # ========== STEP 1: PARSE MESSAGE ==========
        # Convert JSON string to Python dictionary
        # Example: '{"to": "user456", "text": "Hello"}' → {"to": "user456", "text": "Hello"}
        # Production: Add try-except for invalid JSON, validate required fields
        data = json.loads(message)
        
        # Extract receiver_id (who should receive this message)
        # Production: Validate receiver exists in database, not blocked, etc.
        receiver_id = data['to']
        
        # Extract message text
        # Production: Validate text length (max 4096 chars), check for spam, profanity filter
        text = data['text']
        
        # ========== STEP 2: GENERATE UNIQUE MESSAGE ID ==========
        # Format: {timestamp}_{sender_id}
        # timestamp = Current Unix timestamp (seconds since 1970)
        # Example: "1640000000_user123"
        # Why unique? Timestamp (precise to second) + sender_id = collision unlikely
        # Production: Add random UUID for guaranteed uniqueness across distributed servers
        msg_id = f"{int(datetime.now().timestamp())}_{sender_id}"
        
        # ========== STEP 3: STORE MESSAGE IN DATABASE ==========
        # Redis HSET = Hash SET (store multiple fields in one key)
        # Key: "msg:{msg_id}" (e.g., "msg:1640000000_user123")
        # mapping = Dictionary of field-value pairs
        # Production: Use Cassandra for persistence (Redis is cache, data lost on restart)
        self.redis.hset(f"msg:{msg_id}", mapping={
            'sender': sender_id,       # Who sent the message
            'receiver': receiver_id,   # Who should receive it
            'text': text,              # Message content
            'timestamp': datetime.now().isoformat()  # ISO format: "2024-01-15T10:30:00"
        })
        
        # ========== STEP 4: SEND ACK TO SENDER (SINGLE TICK ✓) ==========
        # Acknowledge that server received the message
        # This shows single tick (✓) in WhatsApp UI
        # await = Asynchronously send ACK (non-blocking)
        await self.send_ack(sender_id, msg_id, "sent")
        
        # ========== STEP 5: CHECK RECEIVER STATUS & FORWARD ==========
        # Check if receiver is currently connected to this server
        # Why check? If online, deliver immediately via WebSocket (real-time)
        if receiver_id in self.connections:
            # ===== RECEIVER ONLINE (INSTANT DELIVERY) =====
            # Get receiver's WebSocket connection from dictionary
            receiver_ws = self.connections[receiver_id]
            
            # Send message to receiver via WebSocket
            # json.dumps() = Convert Python dict to JSON string
            # await = Asynchronously send (don't block other messages)
            await receiver_ws.send(json.dumps({
                'msg_id': msg_id,                      # Unique message identifier
                'from': sender_id,                     # Who sent it
                'text': text,                          # Message content
                'timestamp': datetime.now().isoformat()  # When received (for ordering)
            }))
            
            # Send delivery ACK to sender (DOUBLE TICK ✓✓)
            # Confirms message was delivered to receiver's device
            # This changes tick from ✓ to ✓✓ in sender's UI
            await self.send_ack(sender_id, msg_id, "delivered")
        else:
            # ===== RECEIVER OFFLINE (QUEUE FOR LATER) =====
            # Receiver not connected to this server (offline or on different server)
            
            # Store message ID in offline queue (Redis list)
            # LPUSH = List PUSH (add to left/front of list)
            # Key: "offline:{receiver_id}" (e.g., "offline:user456")
            # Value: message_id (e.g., "1640000000_user123")
            # When user comes online, fetch all messages from this list
            self.redis.lpush(f"offline:{receiver_id}", msg_id)
            
            # Log for debugging/monitoring
            print(f"📥 Message queued for offline user {receiver_id}")
    
    async def send_ack(self, user_id, msg_id, status):
        """
        Send acknowledgment (ACK) to user
        ACK types: "sent" (✓), "delivered" (✓✓), "read" (blue ✓✓)
        
        user_id: Who to send ACK to (e.g., "user123")
        msg_id: Which message this ACK is for (e.g., "1640000000_user123")
        status: ACK type ("sent", "delivered", "read")
        """
        # Check if user is currently connected to this server
        # If not connected, ACK is lost (acceptable, UI will request status on reconnect)
        if user_id in self.connections:
            # Get user's WebSocket connection
            ws = self.connections[user_id]
            
            # Send ACK message via WebSocket
            # Format: {"type": "ack", "msg_id": "...", "status": "sent"}
            # Client UI uses this to update tick display (✓ → ✓✓ → blue ✓✓)
            await ws.send(json.dumps({
                'type': 'ack',      # Message type (client knows to update UI, not show as chat message)
                'msg_id': msg_id,   # Which message ID to update
                'status': status    # New status (sent/delivered/read)
            }))

# ============ SERVER STARTUP ============

async def main():
    """
    Start Chat Server
    Creates WebSocket server listening on localhost:8765
    """
    # Create ChatServer instance
    server = ChatServer()
    
    # Start WebSocket server
    # websockets.serve() = Create WebSocket server
    # Arguments:
    #   - server.handle_connection = Function to call for each new connection
    #   - "localhost" = Listen on localhost only (production: "0.0.0.0" for all interfaces)
    #   - 8765 = Port number (production: use 443 for WSS - WebSocket Secure)
    async with websockets.serve(server.handle_connection, "localhost", 8765):
        # Log server status
        print("🚀 Chat server running on ws://localhost:8765")
        
        # Run forever (keep server alive)
        # asyncio.Future() = Never completes (blocks indefinitely)
        # Server processes connections concurrently while waiting here
        await asyncio.Future()

# ============ RUN SERVER ============

# asyncio.run() = Start async event loop and run main()
# Event loop manages all async operations (connections, messages, ACKs)
# This is the entry point - server starts here
asyncio.run(main())


# ============ USAGE EXAMPLES FOR TESTING ============

"""
CLIENT SIDE (JavaScript example for testing):

// Connect to server
const ws = new WebSocket('ws://localhost:8765');

// Authenticate on connection open
ws.onopen = () => {
    ws.send(JSON.stringify({user_id: 'user123', token: 'auth_token'}));
};

// Send message
ws.send(JSON.stringify({to: 'user456', text: 'Hello!'}));

// Receive messages
ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    if (data.type === 'ack') {
        console.log(`ACK: Message ${data.msg_id} is ${data.status}`);
        // Update UI: Show tick (✓, ✓✓, or blue ✓✓)
    } else {
        console.log(`New message from ${data.from}: ${data.text}`);
        // Display in chat UI
    }
};


TESTING SCENARIO:

1. Start server: python chat_server.py
2. Open 2 browser tabs (User A and User B)
3. User A sends "Hello" to User B
4. User B receives "Hello" instantly (if online)
5. User A sees tick change: ✓ (sent) → ✓✓ (delivered)
6. User B opens chat → User A sees blue ✓✓ (read)

OFFLINE SCENARIO:

1. User B offline (not connected)
2. User A sends "Hello" to User B
3. Message stored in Redis: "offline:user_b" → [msg_id]
4. User A sees ✓ (sent) but NOT ✓✓ (not delivered yet)
5. User B comes online
6. Server fetches offline messages, delivers to User B
7. User A sees ✓✓ (delivered)
"""
```

---

### **Signal Protocol: End-to-End Encryption (Message Security)**

**What is End-to-End Encryption?**

End-to-end encryption (E2EE) means only the sender and receiver can read the message. The server (WhatsApp, Signal) cannot decrypt it. It's like putting your message in a locked box - only the receiver has the key.

**Why Signal Protocol:** Used by WhatsApp (2B+ users), Signal App, Facebook Messenger

**Key Concept - Forward Secrecy:** Even if today's key is stolen, yesterday's messages remain safe (keys deleted after use).

**Quick ASCII Diagram:**

```
[ALICE sends "Hello" to BOB]
   ↓
[Encrypt with unique Message Key MK_1]
   ↓
[Server sees] → Only encrypted gibberish "%$#@!^&*" (can't read "Hello")
   ↓
[BOB receives and decrypts with MK_1]
   ↓
[BOB reads "Hello"]

After use: MK_1 DELETED (forward secrecy)
Next message uses MK_2 (different key)
```

**For detailed Double Ratchet Algorithm, X3DH key exchange, and implementation:** See FAQ Q5.

---

### **Message Ticks State Machine (✓ → ✓✓ → Blue ✓✓)**

**3 States:**

| Tick | Meaning | When it appears |
|------|---------|----------------|
| ✓ | Sent | Server received message |
| ✓✓ | Delivered | Receiver's device got it |
| Blue ✓✓ | Read | Receiver opened chat |

**State Flow:**

```
[Send] → [Server ACK] → ✓ Sent → [Device ACK] → ✓✓ Delivered → [Open Chat] → Blue ✓✓ Read
```

**Database Updates:**

```sql
-- Message stored with status tracking
status: 'sent' → sent_at: 2024-01-15 10:00:00
status: 'delivered' → delivered_at: 2024-01-15 10:00:01
status: 'read' → read_at: 2024-01-15 10:05:00
```

**Network Failure:** If ACK lost, app requests status on reconnect.

**Privacy:** Users can disable read receipts (blue tick won't show to sender).

---

### **Group Chat Architecture (1 Message → N Users)**

**Challenge:** User A sends message in group with 100 members → How to deliver to all 100 efficiently?

**Two Approaches:**

**1. Fanout-on-Write (WhatsApp's Choice for groups ≤ 256):**

```
User A sends "Hello" to Group (100 members)
   ↓
[Chat Server receives]
   ↓
[Fanout Logic]
- Create 100 delivery tasks
- For each member:
  → Check online status (Redis)
  → If online: Push via WebSocket
  → If offline: Add to offline queue
   ↓
[Kafka Queue]
Partition by group_id for ordering
Topic: "group_messages"
100 messages in queue (1 per member)
   ↓
[Workers process in parallel]
50 members online → Instant delivery
50 members offline → Queued
   ↓
[Delivery Tracking]
Database: Track delivery status per member
Sender sees: "✓✓ Delivered to 50/100"
```

**ASCII Diagram:**

```
[User A sends to Group-123]
  (100 members: B, C, D, ... Z)
         ↓
   [Chat Server]
         |
         | (Fanout: 1 → 100)
         ↓
 +--------+--------+--------+
 |        |        |        |
 v        v        v        v
[User B] [User C] [User D] ... [User Z]
 Online   Offline  Online       Online
  ↓        ↓        ↓            ↓
 ✓✓     (Queue)    ✓✓           ✓✓
```

**Delivery Status Tracking:**

```sql
CREATE TABLE group_message_delivery (
    msg_id UUID,
    group_id UUID,
    member_id UUID,
    status VARCHAR(20),  -- 'sent', 'delivered', 'read'
    delivered_at TIMESTAMP,
    
    PRIMARY KEY (msg_id, member_id)
);

-- Query: How many members received message?
SELECT COUNT(*) as delivered_count
FROM group_message_delivery
WHERE msg_id = '123' AND status = 'delivered';

-- Result: "Delivered to 87/100 members"
```

**2. Fanout-on-Read (For large groups > 256 - Telegram uses this):**

```
User A sends "Hello" to Group
   ↓
[Save 1 copy in shared location]
Key: "group:123:messages"
Value: [{msg_1}, {msg_2}, ...]
   ↓
[Each member fetches when they open chat]
- User B opens group → Fetches last 50 messages
- User C opens group → Fetches last 50 messages
- User D never opens → Never fetches (saves bandwidth)
```

**Comparison:**

| Feature | Fanout-on-Write | Fanout-on-Read |
|---------|----------------|----------------|
| **Write Cost** | High (N DB writes) | Low (1 DB write) |
| **Read Cost** | Low (user has own copy) | High (query shared location) |
| **Storage** | High (N copies) | Low (1 copy) |
| **Delivery Confirmation** | Easy (track per user) | Hard (don't know who read) |
| **Best for** | Small groups (<100) | Large broadcast (>1000) |

**WhatsApp Limits:**

- Max group size: 256 members (fanout manageable)
- Why 256? Balance between UX (personal groups) and scalability
- Larger groups → Telegram (unlimited, uses fanout-on-read)

**Member Management:**

```python
async def send_group_message(self, sender_id, group_id, text):
    """
    Send message to group (fanout to all members)
    """
    # Fetch group members from database
    members = self.db.query(
        "SELECT user_id FROM group_members WHERE group_id = ?",
        group_id
    )
    
    # Generate message ID
    msg_id = generate_unique_id()
    
    # Store message once (shared copy)
    self.db.insert("group_messages", {
        'msg_id': msg_id,
        'group_id': group_id,
        'sender_id': sender_id,
        'text': text,
        'timestamp': datetime.now()
    })
    
    # Fanout to all members
    for member in members:
        if member.user_id != sender_id:  # Don't send to self
            # Check if member online
            if member.user_id in self.connections:
                # Online: Deliver immediately
                await self.send_to_user(member.user_id, {
                    'msg_id': msg_id,
                    'group_id': group_id,
                    'from': sender_id,
                    'text': text
                })
                
                # Track delivery
                self.db.insert("group_message_delivery", {
                    'msg_id': msg_id,
                    'member_id': member.user_id,
                    'status': 'delivered'
                })
            else:
                # Offline: Queue for later
                self.redis.lpush(f"offline:{member.user_id}", msg_id)
```

**Kafka Partitioning for Groups:**

```
Topic: "group_messages"
Partitions: 100 (for parallelism)

Partitioning Strategy:
partition_id = hash(group_id) % 100

Why?
- All messages from Group-123 go to same partition
- Ensures message ordering within group
- Different groups processed in parallel (different partitions)

Example:
Group-123: Partition 23 (all messages ordered)
Group-456: Partition 56 (different partition, parallel processing)
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

**Q5: End-to-end encryption (Signal Protocol) kaise kaam karta hai - Complete flow?**  
A: **Step 1 - Key Exchange (X3DH):** Alice wants to message Bob. Bob's app has already published his Identity Key (permanent) + 100 Prekeys (one-time use) to WhatsApp server. Alice fetches Bob's Identity Key + one Prekey. Alice performs 4 Diffie-Hellman (DH) key exchanges using her keys × Bob's keys. All 4 outputs combined → Shared Secret (256-bit). Alice derives 3 keys: Root Key (for future), Chain Key (for messages), Message Key (for this message). **Step 2 - Encryption:** Alice encrypts "Hello" with Message Key using AES-256-GCM (encryption + authentication). Creates MAC using HMAC-SHA256 (prevents tampering). **Step 3 - Send:** Alice sends {encrypted_message, her_keys, MAC} to server. Server forwards to Bob (can't read content, only encrypted blob). **Step 4 - Bob Decrypts:** Bob uses Alice's keys to perform same 4 DH exchanges → derives same Shared Secret → derives same Message Key → decrypts message. **Step 5 - Forward Secrecy (Double Ratchet):** After use, Message Key DELETED from both devices. Next message uses new key derived from Chain Key. Chain Key also updates (ratchets forward). If attacker steals current key, past messages still safe (keys already deleted). **WhatsApp:** Uses Signal Protocol since 2016. 2B+ users, all messages encrypted. Server sees: sender, receiver, timestamp, encrypted blob. Cannot read: message content ("Hello"), media, voice notes. **Metadata NOT encrypted:** Who talked to whom, when, how often. **Trade-off:** Can't search messages on server, can't restore from cloud backup (keys on device only).

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
