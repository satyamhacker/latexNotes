# Module 19: Design YouTube/Netflix (Video Streaming)

## Topic 19.1: Video Streaming System - HLS & CDN

---

## 🎯 1. Title / Topic: YouTube/Netflix (Video Streaming Platform)

---

## 🐣 2. Samjhane ke liye (Simple Analogy):

Video streaming ek **Water Pipeline System** jaisa hai. Jaise paani ko ek saath poora tank nahi bhejte (heavy), balki continuous pipe se thoda-thoda flow karte hain (stream), waise hi video ko ek saath poora download nahi karte (2GB file), balki chhote-chhote chunks mein stream karte hain (2 sec ka chunk). **Adaptive Bitrate:** Jaise paani ka pressure kam ho toh pipe ka diameter chhota kar dete hain (flow maintain), waise hi internet slow ho toh video quality reduce (480p → 360p) but playback continue. **CDN:** Jaise har area mein local water tank hota hai (paas se paani milta hai, fast), waise hi har region mein CDN server (video paas se milta hai, low latency).

---

## 📖 3. Technical Definition (Interview Answer):

**Video Streaming System** is a platform that delivers video content via adaptive bitrate streaming (HLS/DASH), stores videos in object storage (S3), transcodes to multiple resolutions (1080p, 720p, 480p), distributes via CDN for low latency, and tracks playback analytics.

**Key terms:**
- **HLS (HTTP Live Streaming):** Video ko chhote chunks (2-10 sec) mein divide, HTTP se stream (Apple protocol)
- **Adaptive Bitrate:** Network speed ke basis par quality change (1080p → 720p → 480p automatically)
- **Transcoding:** Original video ko multiple formats/resolutions mein convert (1080p, 720p, 480p, 360p)
- **CDN (Content Delivery Network):** Video ko geographically distributed servers par cache (low latency)
- **Manifest File:** Playlist jo batata hai kaunse chunks kahan hain (.m3u8 file)

---

## 🧠 4. Zaroorat Kyun Hai? (Why?):

**Main Problem:** 2GB video ko ek saath download karna slow hai (10 min wait on 3 Mbps), aur user different network speeds par hain (4G vs WiFi). Streaming se immediate playback (2 sec wait), adaptive quality (network ke according).

**Business Impact:** YouTube: 1B+ hours watched daily, $28B revenue (2021). Netflix: 230M subscribers, 15% internet traffic globally. Without streaming, video platforms impossible (users won't wait 10 min for download).

**Technical Benefits:**
- **Instant Playback:** 2 sec wait vs 10 min download (user retention)
- **Adaptive Quality:** Auto-adjust to network (no buffering, smooth playback)
- **Bandwidth Optimization:** Stream only what user watches (50% videos abandoned after 1 min)
- **Global Scale:** CDN delivers from nearest server (50ms latency vs 500ms)

---

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario):

**Scenario: No Streaming (Full Download)**
- User clicks video (2GB, 1080p)
- Download: 2GB / 3 Mbps = 5333 seconds = 89 minutes
- User: Waits 89 min → Frustrated → Closes tab
- Business: 0 views, 0 revenue

**Scenario: No Adaptive Bitrate**
- User on slow 3G (1 Mbps)
- Video: 1080p (5 Mbps required)
- Result: Constant buffering every 2 seconds
- User: Frustrated → Closes video

**Real Example:** **YouTube (2005 launch)** - Initially no adaptive streaming → Users on slow connections couldn't watch → Added adaptive bitrate (2010) → Mobile views increased 300%. **Netflix (2007)** - Started with progressive download → Switched to adaptive streaming (2011) → Buffering reduced 90%, subscriber growth accelerated.

---

## ⚙️ 6. Under the Hood (Technical Working):

**Video Upload & Processing Flow:**

1. **User Uploads:** Creator uploads 4K video (5GB, .mp4)
2. **Storage:** Upload to S3 (object storage)
3. **Transcoding Job:** Queue job in processing pipeline
4. **Transcoding:** Convert to multiple resolutions
   - 1080p (5 Mbps bitrate)
   - 720p (2.5 Mbps)
   - 480p (1 Mbps)
   - 360p (0.5 Mbps)
5. **Chunking:** Split each resolution into 2-sec chunks
   - 1080p: chunk_0.ts, chunk_1.ts, chunk_2.ts, ...
   - 720p: chunk_0.ts, chunk_1.ts, ...
6. **Manifest Generation:** Create .m3u8 playlist file
7. **CDN Upload:** Push chunks to CDN (edge servers globally)
8. **Database Update:** Mark video as "ready"

**Video Playback Flow:**

1. **User Clicks:** Play button on video
2. **Fetch Manifest:** Download .m3u8 file (playlist)
3. **Parse Manifest:** Get list of chunks and resolutions
4. **Bandwidth Detection:** Measure network speed (initial 2 sec)
5. **Quality Selection:** Choose appropriate resolution (720p for 3 Mbps)
6. **Chunk Download:** Download chunk_0.ts (2 sec video)
7. **Playback Start:** Play chunk_0 while downloading chunk_1
8. **Adaptive Switch:** Network slow → Switch to 480p
9. **Continue:** Download chunks sequentially, play continuously

**ASCII Architecture Diagram:**

```
UPLOAD FLOW:

[Creator uploads video.mp4 (5GB)]
     |
     v
+---------------------------+
|   UPLOAD SERVICE          |
|   - Validate format       |
|   - Generate video_id     |
+---------------------------+
     |
     v
+---------------------------+
|   S3 STORAGE              |
|   (Object Storage)        |
|   /videos/original/       |
|   video_123.mp4           |
+---------------------------+
     |
     v
+---------------------------+
|   TRANSCODING QUEUE       |
|   (Kafka/SQS)             |
|   Job: {video_id, format} |
+---------------------------+
     |
     v
+---------------------------+
|   TRANSCODING WORKERS     |
|   (FFmpeg on EC2/Lambda)  |
|   - 1080p encoding        |
|   - 720p encoding         |
|   - 480p encoding         |
|   - 360p encoding         |
+---------------------------+
     |
     v
+---------------------------+
|   CHUNKING SERVICE        |
|   - Split into 2-sec      |
|   - Generate .m3u8        |
+---------------------------+
     |
     v
+---------------------------+
|   S3 STORAGE              |
|   /videos/processed/      |
|   video_123/1080p/        |
|     chunk_0.ts            |
|     chunk_1.ts            |
|   video_123/720p/         |
|     chunk_0.ts            |
+---------------------------+
     |
     v
+---------------------------+
|   CDN DISTRIBUTION        |
|   (CloudFront/Akamai)     |
|   - Push to edge servers  |
|   - Global cache          |
+---------------------------+


PLAYBACK FLOW:

[User clicks play]
     |
     v
+---------------------------+
|   VIDEO PLAYER            |
|   (Browser/App)           |
+---------------------------+
     |
     | (1) Request manifest
     v
+---------------------------+
|   CDN EDGE SERVER         |
|   (Nearest to user)       |
+---------------------------+
     |
     | (2) Return manifest.m3u8
     v
[Player parses manifest]
     |
     | Available: 1080p, 720p, 480p, 360p
     v
[Detect bandwidth: 3 Mbps]
     |
     | Select: 720p (2.5 Mbps)
     v
+---------------------------+
|   CDN EDGE SERVER         |
+---------------------------+
     |
     | (3) Download chunk_0.ts (2 sec)
     v
[Player: Start playback]
     |
     | While playing chunk_0, download chunk_1
     v
[Continuous streaming]
     |
     | Network drops to 1 Mbps
     v
[Switch to 480p automatically]
     |
     v
[Smooth playback continues]


HLS MANIFEST FILE (.m3u8):

#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:BANDWIDTH=5000000,RESOLUTION=1920x1080
1080p/playlist.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=2500000,RESOLUTION=1280x720
720p/playlist.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=1000000,RESOLUTION=854x480
480p/playlist.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=500000,RESOLUTION=640x360
360p/playlist.m3u8

(Player chooses based on bandwidth)


CHUNK PLAYLIST (720p/playlist.m3u8):

#EXTM3U
#EXT-X-TARGETDURATION:2
#EXTINF:2.0,
chunk_0.ts
#EXTINF:2.0,
chunk_1.ts
#EXTINF:2.0,
chunk_2.ts
...
#EXT-X-ENDLIST
```

---

## 🛠️ 7. Problems Solved:

- **Instant Playback:** 2 sec wait (first chunk) vs 89 min full download → 99% faster start
- **Adaptive Quality:** Auto-switch based on network → No buffering, smooth experience
- **Bandwidth Efficiency:** Stream only watched portion → 50% bandwidth saved (many videos abandoned)
- **Global Scale:** CDN delivers from nearest server → 50ms latency (vs 500ms from origin)
- **Multiple Devices:** Same video works on mobile (360p), laptop (1080p), TV (4K) → Transcoding enables
- **Cost Optimization:** CDN caching reduces origin server load → 90% requests served from cache

---

## 🌍 8. Real-World Example:

**Netflix Streaming:** 230M subscribers, 15% of global internet traffic. Technology: Adaptive bitrate (proprietary algorithm), 1000+ CDN servers (Open Connect), AWS for transcoding (100K+ EC2 instances), S3 for storage (petabytes). Encoding: Per-title optimization (different bitrates for different content types - action vs dialogue). Scale: 1B hours watched/week, 10 Gbps per CDN server. Cost: $1B/year on CDN infrastructure. Result: 99.9% uptime, <1% buffering rate, avg 3 Mbps streaming (vs 5 Mbps industry avg - better compression). Without adaptive streaming and CDN, Netflix couldn't serve 230M users globally.

---

## 🔧 9. Tech Stack / Tools:

- **FFmpeg:** Video transcoding. Use for: Convert formats, change resolution, extract audio, generate thumbnails. Open-source, industry standard.

- **AWS S3:** Object storage for videos. Use for: Unlimited storage (petabytes), 99.99% durability, lifecycle policies (move old videos to Glacier).

- **CloudFront/Akamai:** CDN for distribution. Use for: Global edge servers (200+ locations), low latency (<50ms), DDoS protection.

- **HLS.js / Video.js:** Video player libraries. Use for: Browser playback, adaptive bitrate logic, analytics tracking.

---

## 📐 10. Architecture/Formula:

**Transcoding Time Calculation:**

```
Transcoding_Time = Video_Duration / Transcoding_Speed

Where:
Transcoding_Speed = CPU_Cores × Encoding_Efficiency

Example:
Video: 60 min (3600 sec)
CPU: 16 cores
Encoding_Efficiency: 4x (real-time)

Transcoding_Speed = 16 × 4 = 64x real-time
Transcoding_Time = 3600 / 64 = 56 seconds

For 4 resolutions: 56 × 4 = 224 seconds ≈ 4 minutes
(Parallel encoding: Still 56 seconds with 4 workers)
```

**Bandwidth Requirement:**

```
Bandwidth = Bitrate × Concurrent_Users

Example (YouTube scale):
Concurrent_Users = 2 million (peak)
Avg_Bitrate = 2 Mbps (720p)

Bandwidth = 2 Mbps × 2M = 4 Tbps (4000 Gbps)

CDN servers: 4000 Gbps / 10 Gbps per server = 400 servers minimum
With redundancy (3x): 1200 servers globally
```

**Storage Calculation:**

```
Storage = Videos × Avg_Size × Resolutions × Retention

Example (YouTube scale):
Videos_Uploaded_Per_Day = 500 hours = 30,000 minutes
Avg_Size_Per_Minute = 100 MB (1080p)
Resolutions = 4 (1080p, 720p, 480p, 360p)
Retention = Forever (never delete)

Daily_Storage = 30,000 × 100 MB × 4 = 12 TB/day
Yearly_Storage = 12 TB × 365 = 4.38 PB/year

After 10 years: 43.8 PB
With compression (50%): 21.9 PB
```

**Adaptive Bitrate Selection:**

```
Quality_Selection = 
    if bandwidth > 5 Mbps: 1080p
    elif bandwidth > 2.5 Mbps: 720p
    elif bandwidth > 1 Mbps: 480p
    else: 360p

Buffer_Threshold = 10 seconds (switch if buffer < 10 sec)

Example:
Current: 720p (2.5 Mbps)
Bandwidth drops to 1.5 Mbps
Buffer: 8 seconds (< 10 sec threshold)
Action: Switch to 480p (1 Mbps)
Result: Buffer increases, smooth playback
```

---

## 💻 11. Code / Flowchart:

**Flowchart (Video Upload & Processing):**

```
START: User uploads video
  |
  v
[Upload to S3]
/videos/original/video_123.mp4
  |
  v
[Create transcoding jobs]
Jobs: [1080p, 720p, 480p, 360p]
  |
  v
[Queue in Kafka/SQS]
  |
  v
[Workers pick jobs (parallel)]
  |
  +---> Worker-1: 1080p
  +---> Worker-2: 720p
  +---> Worker-3: 480p
  +---> Worker-4: 360p
  |
  v
[FFmpeg transcoding]
ffmpeg -i input.mp4 -vf scale=1280:720 -b:v 2.5M output_720p.mp4
  |
  v
[Chunk into 2-sec segments]
ffmpeg -i output_720p.mp4 -c copy -f hls -hls_time 2 playlist.m3u8
  |
  v
[Upload chunks to S3]
/videos/processed/video_123/720p/chunk_0.ts
  |
  v
[Generate master manifest]
master.m3u8 (links to all resolutions)
  |
  v
[Push to CDN]
Distribute to edge servers globally
  |
  v
[Update database]
video_status = "ready"
  |
  v
END
```

**Code (Simplified HLS Player Logic):**

```python
import requests
import time

class HLSPlayer:
    def __init__(self, manifest_url):
        self.manifest_url = manifest_url
        self.current_quality = None
        self.buffer = []
    
    def start_playback(self):
        """Start video playback"""
        # Fetch master manifest
        manifest = self._fetch_manifest(self.manifest_url)
        
        # Detect bandwidth
        bandwidth = self._detect_bandwidth()
        
        # Select quality
        self.current_quality = self._select_quality(manifest, bandwidth)
        
        # Start streaming
        self._stream_chunks()
    
    def _detect_bandwidth(self):
        """Measure network speed (simplified)"""
        start = time.time()
        response = requests.get("https://cdn.example.com/test.bin")  # 1MB test file
        elapsed = time.time() - start
        
        bandwidth = (1 * 8) / elapsed  # Mbps
        return bandwidth
    
    def _select_quality(self, manifest, bandwidth):
        """Choose appropriate quality based on bandwidth"""
        qualities = {
            '1080p': 5.0,   # Mbps
            '720p': 2.5,
            '480p': 1.0,
            '360p': 0.5
        }
        
        for quality, required_bw in sorted(qualities.items(), 
                                          key=lambda x: x[1], 
                                          reverse=True):
            if bandwidth >= required_bw * 1.2:  # 20% buffer
                return quality
        
        return '360p'  # Fallback
    
    def _stream_chunks(self):
        """Download and play chunks"""
        chunk_index = 0
        
        while True:
            # Download next chunk
            chunk_url = f"https://cdn.example.com/{self.current_quality}/chunk_{chunk_index}.ts"
            chunk_data = requests.get(chunk_url).content
            
            # Add to buffer
            self.buffer.append(chunk_data)
            
            # Play if buffer sufficient
            if len(self.buffer) >= 3:  # 6 seconds buffered
                self._play_chunk(self.buffer.pop(0))
            
            # Check if quality switch needed
            if len(self.buffer) < 2:  # Buffer low
                self._switch_quality_down()
            
            chunk_index += 1
    
    def _switch_quality_down(self):
        """Switch to lower quality"""
        quality_order = ['1080p', '720p', '480p', '360p']
        current_index = quality_order.index(self.current_quality)
        
        if current_index < len(quality_order) - 1:
            self.current_quality = quality_order[current_index + 1]
            print(f"📉 Switched to {self.current_quality}")
    
    def _play_chunk(self, chunk_data):
        """Play video chunk (simplified)"""
        print(f"▶️ Playing chunk ({self.current_quality})")
        time.sleep(2)  # Simulate 2-sec playback

# Usage
player = HLSPlayer("https://cdn.example.com/video_123/master.m3u8")
player.start_playback()
```

---

## 📈 12. Trade-offs:

- **Gain:** Instant playback (2 sec), adaptive quality (no buffering), global scale (CDN) | **Loss:** Storage cost (4x for 4 resolutions), transcoding cost (CPU-intensive), CDN cost ($0.08/GB)

- **Gain:** HLS works on all devices (iOS, Android, Web) | **Loss:** 2-10 sec latency (not real-time like WebRTC), chunk overhead (HTTP requests per 2 sec)

- **Gain:** CDN caching reduces origin load 90% | **Loss:** Cache invalidation complexity (update video → purge CDN cache), CDN cost ($1B/year for Netflix)

- **When to use:** Video platforms (YouTube, Netflix), live streaming (Twitch), video courses (Udemy) | **When to skip:** Real-time video calls (use WebRTC), small videos (<1 min - progressive download OK), internal videos (no global scale needed)

---

## 🐞 13. Common Mistakes:

- **Mistake:** Transcoding synchronously (user waits for processing)
  - **Why wrong:** 60 min video → 4 min transcoding → User waits 4 min
  - **What happens:** Poor UX, user abandons upload
  - **Fix:** Async transcoding (queue job, notify when ready)

- **Mistake:** No CDN (serving from origin server)
  - **Why wrong:** User in India, server in US → 500ms latency, buffering
  - **What happens:** Poor playback experience, high bandwidth cost
  - **Fix:** CDN with edge servers globally (50ms latency)

- **Mistake:** Fixed bitrate (no adaptive streaming)
  - **Why wrong:** User on 3G (1 Mbps) gets 1080p (5 Mbps) → Constant buffering
  - **What happens:** Frustrated user, video abandonment
  - **Fix:** HLS adaptive bitrate (auto-switch to 480p)

- **Mistake:** Large chunk size (10 sec)
  - **Why wrong:** 10 sec chunk on slow network → 20 sec download → Buffering
  - **What happens:** Poor startup time, frequent buffering
  - **Fix:** 2-4 sec chunks (balance between overhead and responsiveness)

---

## ✅ 14. Zaroori Notes for Interview:

**Must Mention Points:**
1. **Start with HLS:** "Video streaming ka standard HLS (HTTP Live Streaming) hai. Video ko 2-sec chunks mein divide, multiple resolutions mein transcode (1080p, 720p, 480p), manifest file (.m3u8) se player ko batate hain kaunse chunks kahan hain."

2. **Draw architecture:** User uploads → S3 storage → Transcoding workers (FFmpeg) → Chunking → CDN distribution → User playback (adaptive bitrate).

3. **Explain adaptive bitrate:** "Player network speed detect karta hai (bandwidth test), appropriate quality select (3 Mbps → 720p), agar network slow ho toh automatically lower quality switch (480p). Buffer maintain rehta hai, no buffering."

4. **Common follow-ups:**
   - **"HLS vs DASH?"** → HLS: Apple protocol, .m3u8 manifest, widely supported. DASH: MPEG standard, .mpd manifest, more flexible but complex. HLS simpler, industry standard.
   - **"Transcoding kaise optimize?"** → Per-title encoding (action movies high bitrate, dialogue low bitrate), parallel workers (4 resolutions simultaneously), GPU acceleration (10x faster than CPU).
   - **"CDN kaise kaam karta hai?"** → Edge servers globally (200+ locations), cache popular videos, serve from nearest server (low latency), origin server se fetch only on cache miss.
   - **"Live streaming kaise?"** → Same HLS but real-time chunking (2 sec delay), no full transcoding (single pass encoding), CDN push instead of pull.

5. **Mention scale:** "Netflix: 230M users, 15% global internet traffic, 1000+ CDN servers, <1% buffering rate."

6. **Pro tip:** "Interview mein manifest file (.m3u8) ka example dikhao. Aur mention karo - Async transcoding (non-blocking), CDN caching (90% requests), Adaptive bitrate (smooth playback). Yeh 3 points critical hain."

---

## ❓ 15. FAQ & Comparisons (MANDATORY - 5 Questions):

**Q1: HLS vs DASH vs RTMP - Kaunsa protocol kab use karein?**
A: **HLS (HTTP Live Streaming):** Apple protocol, HTTP-based, .m3u8 manifest, 2-10 sec latency. **Pros:** Universal support (iOS, Android, Web), CDN-friendly (HTTP caching). **Use:** VOD (YouTube, Netflix), live streaming (Twitch). **DASH (Dynamic Adaptive Streaming):** MPEG standard, .mpd manifest, similar to HLS but more flexible. **Use:** When need advanced features (DRM, multi-audio). **RTMP (Real-Time Messaging Protocol):** TCP-based, <1 sec latency, Flash-era. **Deprecated:** Flash dead, use WebRTC for real-time. **Best:** HLS for 99% use cases (industry standard).

**Q2: Transcoding mein CPU vs GPU - Kaunsa better?**
A: **CPU (FFmpeg):** Software encoding, flexible (all codecs supported), slower (1x-4x real-time). **Cost:** $0.10/hour (EC2 c5.xlarge). **GPU (NVIDIA NVENC):** Hardware encoding, 10x faster (40x real-time), limited codecs (H.264, H.265). **Cost:** $0.50/hour (EC2 g4dn.xlarge). **Trade-off:** GPU 10x faster but 5x expensive. **Best:** GPU for high volume (YouTube scale - 500 hours/day), CPU for low volume (<100 videos/day). **Hybrid:** GPU for popular videos (fast processing), CPU for long-tail (cost-effective).

**Q3: CDN caching strategy - Kya cache karein aur kitne time ke liye?**
A: **What to cache:** Video chunks (.ts files), manifest files (.m3u8), thumbnails. **Don't cache:** User-specific data (watch history, recommendations). **TTL (Time To Live):** Popular videos = 7 days (high cache hit rate), Long-tail videos = 1 day (balance storage cost), Live streams = 10 seconds (real-time). **Cache invalidation:** Video updated → Purge CDN cache (CloudFront invalidation API). **Cache hit rate:** Target 90%+ (Netflix achieves 95%). **Storage:** 1 PB per CDN server (10K videos × 100 GB each).

**Q4: Video storage mein S3 vs Glacier - Kab kaunsa use karein?**
A: **S3 Standard:** Hot storage, instant access, $0.023/GB/month. **Use:** Recent videos (<1 year), popular content (high views). **S3 Glacier:** Cold storage, 3-5 hour retrieval, $0.004/GB/month (5x cheaper). **Use:** Old videos (>1 year), low views (<100/month). **Lifecycle policy:** Auto-move to Glacier after 1 year (S3 lifecycle rules). **Example:** YouTube - 500 hours uploaded/day, 80% videos get <100 views → Move to Glacier after 1 year → 60% storage cost saved. **Retrieval:** Rare access OK (3-5 hour wait acceptable for old videos).

**Q5: Adaptive bitrate algorithm - Quality switch kab karein?**
A: **Metrics:** (1) **Bandwidth:** Measure download speed (last 10 chunks avg), (2) **Buffer:** Current buffer size (seconds), (3) **CPU:** Device capability (mobile vs desktop). **Switch UP:** Bandwidth > 1.5x current bitrate AND buffer > 20 sec (safe to upgrade). **Switch DOWN:** Buffer < 10 sec OR bandwidth < 0.8x current bitrate (prevent buffering). **Hysteresis:** Don't switch too frequently (min 10 sec between switches - avoid flickering). **Example:** Current 720p (2.5 Mbps), bandwidth drops to 1.8 Mbps, buffer = 8 sec → Switch to 480p (1 Mbps). **Netflix algorithm:** Proprietary, considers 100+ factors (device, time of day, content type).

---

## 🎯 Module 19 Complete Summary:

**All Topics Covered:** 1/1 ✅
- ✅ Topic 19.1: YouTube/Netflix Video Streaming - HLS Protocol, Adaptive Bitrate, Transcoding (FFmpeg), CDN Distribution, Storage (S3)

**Key Takeaways:**
1. **HLS Protocol:** Video split into 2-sec chunks, multiple resolutions (1080p, 720p, 480p, 360p), manifest file (.m3u8) guides player
2. **Adaptive Bitrate:** Auto-switch quality based on network speed (3 Mbps → 720p, 1 Mbps → 480p), no buffering
3. **Transcoding:** FFmpeg converts to multiple formats, parallel workers (4 resolutions simultaneously), 4 min for 60 min video
4. **CDN:** Edge servers globally (200+ locations), 90% cache hit rate, 50ms latency (vs 500ms origin)
5. **Storage:** S3 for recent videos, Glacier for old (5x cheaper), lifecycle policies auto-move after 1 year

**Interview Focus:**
- Draw architecture: Upload → S3 → Transcoding → Chunking → CDN → Playback
- Explain HLS manifest file (.m3u8) with example
- Discuss adaptive bitrate algorithm (bandwidth detection, quality selection)
- Mention async transcoding (non-blocking upload)
- Real-world: Netflix (230M users, 15% internet traffic, <1% buffering)

**Progress:** 19/21 Modules Completed 🎉

**Next Module:** Module 20 - Design Uber (Location Services, Matching, ETA)

---
