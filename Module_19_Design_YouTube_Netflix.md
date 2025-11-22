# Module 19: Design YouTube/Netflix (Video Streaming)

## Topic 19.1: Video Streaming System – HLS, CDN & Advanced Features

---

## 🎯 1. Title / Topic: YouTube/Netflix Video Streaming Platform

---

## 🐣 2. Samjhane ke liye (Simple Analogy)

Video streaming ek **Water Pipeline System** jaisa hai. Jaise paani ko ek saath poora tank nahi bhejte (heavy), balki pipe se thoda‑thoda flow karte hain (stream), waise hi video ko ek saath poora download nahi karte (2 GB file), balki chhote‑chhote 2‑second chunks mein stream karte hain. **Adaptive Bitrate**: Jaise pipe ka pressure kam ho toh pipe ka diameter chhota kar dete hain (flow maintain), waise hi internet slow ho toh video quality kam (480p → 360p) hoti hai, lekin playback rukta nahi. **CDN**: Jaise har area mein local water tank hota hai (paas se paani milta hai, fast), waise hi har region mein CDN edge server hota hai, jo video ko user ke kareeb cache karta hai, latency < 50 ms.

---

## 📖 3. Technical Definition (Interview Answer)

**Video Streaming System** is a platform that delivers video content via adaptive bitrate protocols (HLS/DASH), stores raw assets in object storage (S3), transcodes to multiple resolutions, and distributes chunks through a CDN.

**Key terms**:
- **HLS (HTTP Live Streaming)** – Apple ka protocol, video ko 2‑10 sec ke chunks mein split karta hai, manifest (.m3u8) se player ko chunks ka location batata hai.
- **Adaptive Bitrate** – Network speed ke hisaab se quality (1080p → 720p → 480p → 360p) automatically switch hoti hai.
- **Transcoding** – Original video ko multiple resolutions/bitrates mein convert karna (FFmpeg).
- **CDN (Content Delivery Network)** – Globally distributed edge servers jo video chunks cache karte hain, latency kam karte hain.
- **Manifest File** – Playlist (.m3u8) jo chunks aur resolution list karti hai.
- **DRM (Digital Rights Management)** – Encryption + token‑based licence jo unauthorized copying rokti hai.
- **Live Streaming (Low‑Latency HLS)** – Real‑time chunking (≈2 sec) without full transcoding, used for events.
- **Analytics** – Playback metrics (start, stall, bitrate) collected for recommendation & billing.

---

## 🧠 4. Zaroorat Kyun Hai? (Why?)

1. **Problem**: 2 GB video ko ek baar download karna users ke liye 10‑minute wait hota hai, aur network speeds bahut vary karte hain.
2. **Business Impact**: YouTube 1 B+ hours watched daily, Netflix $28 B revenue – dono ko instant playback aur low buffering chahiye.
3. **Technical Benefit**: Adaptive bitrate se latency < 2 sec, bandwidth waste < 50 %, aur CDN se global latency ~ 50 ms, jo user retention aur ad revenue ko boost karta hai.

---

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario)

- **No Streaming**: User ko 2 GB download karna padega → 89 min wait → churn.
- **No Adaptive Bitrate**: Slow 3G user 1080p video dekhega → constant buffering → abandonment.
- **No CDN**: Origin server (US) se India tak 500 ms latency → buffering & high bandwidth cost.
- **Real Example**: YouTube launch (2005) bina adaptive streaming – mobile users could’t watch, 300 % growth after HLS added (2010).

---

## ⚙️ 6. Under the Hood (Technical Working)

1. **Upload & Ingestion**
   - Creator uploads raw .mp4 to S3.
   - Event triggers a transcoding job in Kafka/SQS.
2. **Transcoding Workers**
   - FFmpeg creates 1080p, 720p, 480p, 360p streams (CPU/GPU parallel).
   - Each stream is chunked into 2‑sec .ts files.
3. **Manifest Generation**
   - Master .m3u8 lists resolution playlists; each playlist lists chunk URLs.
4. **CDN Push**
   - Edge servers pull/push chunks, set TTL, enable cache‑hit.
5. **Playback Flow**
   - Player fetches master manifest, detects bandwidth (2‑sec test file), selects quality, streams chunks sequentially, switches quality on‑the‑fly.
6. **Live Streaming (Low‑Latency HLS)**
   - Ingest encoder sends 2‑sec segments directly to CDN (no full transcoding).
   - Manifest updates every 2 sec, enabling < 5 sec end‑to‑end latency.
7. **DRM Token Flow**
   - Client requests licence → Auth Service issues signed token → Player includes token in chunk request → CDN validates token before serving encrypted chunk.
8. **Analytics Pipeline**
   - Player sends playback events (start, stall, bitrate) to Kafka → Real‑time dashboards (Prometheus/Grafana) → Recommendation engine.

**ASCII Diagram – End‑to‑End Pipeline**
```
[Creator] --upload--> [S3 (raw)]
      |                     |
      v                     v
[Transcoding Queue] --> [FFmpeg Workers]
      |                     |
      v                     v
[Chunked Resolutions] --> [Manifest Generator]
      |                     |
      v                     v
[CDN Edge] <---push--- [S3 (processed)]
      |
      | (User request)
      v
[Player] --fetch manifest--> [CDN Edge]
      |                     |
      |--download chunks--> |
      |<--quality switch---|
```

---

## 🛠️ 7. Problems Solved
- **Instant Playback** → 2 sec first chunk vs 89 min download.
- **Adaptive Quality** → No buffering on variable networks.
- **Bandwidth Efficiency** → Stream only watched portion, 50 % saving.
- **Global Scale** → CDN edge delivery, < 50 ms latency.
- **Live Events** → Low‑latency HLS for sports, concerts.
- **Content Protection** → DRM token flow prevents piracy.

---

## 🌍 8. Real‑World Example
**Netflix**: 230 M subscribers, 15 % global internet traffic. Uses proprietary adaptive bitrate, Open Connect CDN (1000+ edge nodes), per‑title encoding, and DRM (PlayReady). Result: 99.9 % uptime, < 1 % buffering, $1 B/year CDN spend.

---

## 🔧 9. Tech Stack / Tools
- **FFmpeg** – Open‑source transcoder, CPU/GPU support, used for multi‑resolution encoding.
- **AWS S3** – Object storage for raw & processed videos, 99.99 % durability.
- **CloudFront / Akamai** – CDN edge network, HTTP caching, DDoS protection.
- **HLS.js / Video.js** – Browser player libraries handling manifest parsing & adaptive switching.
- **Kafka** – Event bus for transcoding jobs & analytics.
- **Redis** – Short‑lived token cache for DRM licence validation.

---

## 📐 10. Architecture / Formula
**Transcoding Time**
```
Transcoding_Time = Video_Duration / (CPU_Cores × Encoding_Efficiency)
```
*Example*: 60 min video, 16 cores, 4× efficiency → 60 min / 64 = 0.94 min ≈ 56 sec per resolution.

**Bandwidth Requirement**
```
Bandwidth = Avg_Bitrate × Concurrent_Users
```
*Example*: 2 Mbps avg bitrate, 2 M peak users → 4 Tbps total → ~ 400 CDN edge servers (10 Gbps each) with 3× redundancy.

**ASCII Diagram – Live‑Latency HLS**
```
[Live Encoder] --2s segments--> [CDN Edge]
      |                         |
      v                         v
[Manifest (updated every 2s)]   |
      |                         |
      v                         v
[Player] <--fetch manifest-- [CDN Edge]
      |                         |
      |--download chunks------>|
```

---

## 💻 11. Code / Flowchart (HLS Player with Detailed Comments)
```python
import requests, time

class HLSPlayer:
    def __init__(self, manifest_url):
        # Master playlist ka URL store karo (jisme saari qualities listed hain)
        self.manifest_url = manifest_url
        # Abhi koi quality select nahi ki hai (e.g., '720p' or '1080p')
        self.current_quality = None
        # Video chunks ko store karne ke liye buffer list
        self.buffer = []

    def start_playback(self):
        """Video playback start karne ka main function"""
        # Step 1: Master manifest download karo jo available qualities batayega
        manifest = self._fetch_manifest(self.manifest_url)
        
        # Step 2: User ki internet speed (bandwidth) check karo
        bandwidth = self._detect_bandwidth()
        
        # Step 3: Internet speed ke hisaab se best quality select karo
        self.current_quality = self._select_quality(manifest, bandwidth)
        
        # Step 4: Chunks download karna aur play karna shuru karo
        self._stream_chunks()

    def _fetch_manifest(self, url):
        # URL se manifest file ka content fetch karo
        resp = requests.get(url)
        # Content ko lines mein split karke return karo
        return resp.text.splitlines()

    def _detect_bandwidth(self):
        """Network speed measure karne ka simplified logic"""
        start = time.time()
        # Ek chhota test file download karke speed check karo
        # Real apps mein ye player ke doran continuous hota hai
        requests.get("https://cdn.example.com/test.bin")
        elapsed = time.time() - start
        # Speed = Data / Time (Mbps mein convert kiya)
        return (1 * 8) / elapsed

    def _select_quality(self, manifest, bw):
        """Bandwidth ke basis par quality choose karo"""
        # Available qualities aur unki required bandwidth (Mbps)
        qualities = {'1080p': 5.0, '720p': 2.5, '480p': 1.0, '360p': 0.5}
        
        # High quality se low quality check karo
        for q, req in sorted(qualities.items(), key=lambda x: x[1], reverse=True):
            # Agar user ki speed required speed se 20% zyada hai toh select karo
            if bw >= req * 1.2:
                return q
        # Agar speed bahut kam hai toh lowest quality (360p) return karo
        return '360p'

    def _stream_chunks(self):
        idx = 0
        while True:
            # Current quality ke hisaab se chunk ka URL banao
            chunk_url = f"https://cdn.example.com/{self.current_quality}/chunk_{idx}.ts"
            
            # Chunk download karo (ye 2 second ka video part hai)
            chunk = requests.get(chunk_url).content
            self.buffer.append(chunk)
            
            # Agar buffer mein 3 chunks (6 sec) aa gaye hain toh play karo
            if len(self.buffer) >= 3:
                self._play_chunk(self.buffer.pop(0))
            
            # Agar buffer kam ho raha hai (internet slow), toh quality low karo
            if len(self.buffer) < 2:
                self._switch_quality_down()
            
            # Next chunk ke liye index badhao
            idx += 1

    def _switch_quality_down(self):
        # Quality order define karo
        order = ['1080p', '720p', '480p', '360p']
        # Current quality ka index dhundo
        i = order.index(self.current_quality)
        
        # Agar lowest quality par nahi hain, toh ek step neeche jao
        if i < len(order) - 1:
            self.current_quality = order[i + 1]
            print(f"📉 Internet slow! Switched to {self.current_quality}")

    def _play_chunk(self, data):
        # Chunk play karo (Simulated)
        print(f"▶️ Playing {self.current_quality} chunk...")
        time.sleep(2)  # 2 second ka video play ho raha hai

# Usage example
player = HLSPlayer("https://cdn.example.com/video_123/master.m3u8")
player.start_playback()
```

---

## 📈 12. Trade‑offs
- **Gain:** Instant start, adaptive quality, global scale | **Loss:** 4× storage for multiple resolutions, high transcoding CPU/GPU cost, CDN bandwidth expense.
- **Gain:** HLS universal device support | **Loss:** 2‑10 sec latency (not suitable for real‑time video calls).
- **Gain:** DRM protects premium content | **Loss:** Added licence server complexity & latency for token validation.

---

## 🐞 13. Common Mistakes
- **Sync Transcoding** – User waits for encoding → Poor UX. *Fix*: Queue job, notify when ready.
- **No CDN** – High latency & origin overload → Buffering. *Fix*: Enable edge caching.
- **Fixed Bitrate** – Buffering on slow networks. *Fix*: Implement adaptive bitrate.
- **Large Chunk Size** – > 5 sec chunks cause long download on bad networks. *Fix*: Use 2‑4 sec chunks.
- **Skipping DRM** – Piracy risk for premium content. *Fix*: Add token‑based encryption (AES‑128) and licence server.

---

## ✅ 14. Zaroori Notes for Interview
1. **Start with HLS** – Explain chunking, manifest, adaptive bitrate.
2. **Draw Architecture** – Upload → S3 → Transcoding → Chunking → CDN → Playback.
3. **Mention Live‑Latency HLS** – 2‑sec segment, < 5 sec end‑to‑end for events.
4. **Explain DRM Flow** – Token issuance, encrypted chunks, licence validation.
5. **Talk about Analytics** – Playback events → Kafka → Real‑time dashboards → Recommendation.
6. **Cost Optimisation** – Multi‑CDN, edge caching, S3 Glacier for cold storage.
7. **Security** – Signed URLs, token validation, HTTPS everywhere.
8. **Monitoring** – Prometheus metrics (buffer‑time, stall‑rate), alerts on high error rates.
9. **A/B Testing** – Feature flags to roll out new encoding profiles.
10. **Personalisation** – Use playback data to feed recommendation engine (e.g., collaborative filtering).

---

## ❓ 15. FAQ & Comparisons
**Q1: HLS vs DASH vs RTMP – Kab use karein?**
A: HLS – universal (iOS, Android, Web), 2‑10 sec latency, best for VOD & live streaming. DASH – MPEG standard, more flexible (multiple audio/subtitles), used when DRM & multi‑audio needed. RTMP – TCP‑based, < 1 sec latency, legacy for live ingest; replaced by WebRTC for real‑time calls.

**Q2: Transcoding CPU vs GPU – Kaunsa better?**
A: CPU (FFmpeg) – flexible, supports all codecs, slower (1‑4× real‑time). GPU (NVENC) – 10‑40× faster, limited to H.264/H.265, higher cost. Use GPU for high‑volume popular videos, CPU for long‑tail.

**Q3: CDN caching strategy – Kya cache karein aur kitni der?**
A: Cache video chunks (.ts) and manifest files with TTL 7 days for popular videos, 1 day for long‑tail, 10 sec for live streams. Purge on video update via CloudFront invalidation API.

**Q4: Live streaming latency – How achieve low latency?**
A: Use Low‑Latency HLS (2‑sec segments), push chunks to CDN immediately, client polls manifest every 2 sec. Combine with WebRTC for sub‑second latency if needed.

**Q5: DRM kaise kaam karta hai?**
A: Video encrypted with AES‑128. Player requests licence token from Auth Service → Service signs token with secret key → Token sent in chunk request header → CDN validates token before serving encrypted chunk → Player decrypts using key from licence.

---

## Topic 19.2: Content Processor Workflow Engine (DAG)

---

## 🎯 1. Title / Topic: Content Processor Workflow Engine (DAG)

---

## 🐣 2. Samjhane ke liye (Simple Analogy)

Video processing ek **Cooking Recipe** jaisa hai. Aap pasta tab tak nahi bana sakte jab tak paani boil na ho jaye. Kuch steps parallel ho sakte hain (sabzi kaatna aur paani boil karna), lekin kuch sequential hote hain (boil hone ke baad pasta daalna). **DAG (Directed Acyclic Graph)** bas yahi "Recipe Map" hai – ye computer ko batata hai ki kaunsa kaam pehle karna hai (Validation), kaunsa parallel mein (Audio/Video encoding), aur kaunsa last mein (Packaging). Agar sabzi kaatne mein galti hui, toh sirf wahi step repeat karo, poora khana mat pheko (Retry mechanism).

---

## 📖 3. Technical Definition (Interview Answer)

**Content Processor Workflow Engine** is a distributed orchestration system that manages complex video processing tasks using a **DAG (Directed Acyclic Graph)** model. It breaks down a video upload into small, independent tasks (validation, metadata extraction, chunking, encoding), manages dependencies (Task B starts only after Task A), handles retries, and scales workers dynamically.

**Key terms**:
- **DAG (Directed Acyclic Graph)** – Ek flow chart jisme tasks ki direction hoti hai (A → B) aur koi loop nahi hota.
- **Orchestrator** – Central brain (e.g., Netflix Conductor) jo tasks assign karta hai.
- **Worker** – Microservice jo actual kaam karta hai (e.g., FFmpeg encoder).
- **Idempotency** – Agar task fail ho jaye aur retry karein, toh result same rahe (duplicate data na bane).

---

## 🧠 4. Zaroorat Kyun Hai? (Why?)

1. **Problem**: Ek linear script (`upload -> encode -> publish`) fail ho sakti hai. Agar 90% encoding ke baad fail hua, toh poora process restart karna padega (waste of time & money).
2. **Business Impact**: Netflix par hazaron videos upload hote hain. Efficiency aur reliability critical hai.
3. **Technical Benefit**: Parallel processing (audio aur video alag encode karo), fault tolerance (sirf failed task retry karo), aur scalability (jitne tasks, utne workers).

---

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario)

- **Linear Script Failure**: 1-hour video encode ho raha hai, 59th minute par server crash. Result: Poora 1 hour waste, restart from zero.
- **No Parallelism**: Audio aur Video sequentially process honge → Double time lagega.
- **Complexity**: Error handling code har jagah likhna padega ("If fail, try again"). DAG engine ye automatically handle karta hai.

---

## ⚙️ 6. Under the Hood (Technical Working)

1. **Workflow Definition**: JSON file mein define karte hain: "Task A (Validate) -> Task B (Chunk) & Task C (Audio Extract) -> Task D (Merge)".
2. **Task Scheduling**: Orchestrator (Conductor) dekhta hai kaunsa task ready hai aur Queue (Kafka/SQS) mein daalta hai.
3. **Worker Execution**: Worker queue se task uthata hai, process karta hai, aur status update karta hai (Completed/Failed).
4. **Dependency Management**: Jab Task B aur C complete hote hain, tabhi Task D trigger hota hai.
5. **Error Handling**: Agar Task B fail hua, Orchestrator policy check karta hai (Retry 3 times). Agar phir bhi fail, toh alert bhejta hai.

**ASCII Diagram – DAG Workflow**
```
          [Start: Video Uploaded]
                    |
                    v
             [Task: Validation]
                    |
            +-------+-------+
            |               |
    [Task: Video Chunk] [Task: Audio Extract]
            |               |
    [Task: Encode 1080p] [Task: Encode Audio]
            |               |
            +-------+-------+
                    |
             [Task: Packaging (Merge)]
                    |
                    v
             [Task: CDN Push]
                    |
             [End: Video Live]
```

---

## 🛠️ 7. Problems Solved
- **Fault Tolerance** → Granular retries (sirf failed chunk retry karo).
- **Speed** → Massive parallelism (100 chunks = 100 workers simultaneously).
- **Observability** → Visualise kar sakte hain ki process kahan atka hai.
- **Flexibility** → Naya format add karna hai? Bas DAG mein ek naya node add karo.

---

## 🌍 8. Real‑World Example
**Netflix Conductor**: Netflix ne apna open-source orchestrator banaya. Ye microservices ko coordinate karta hai. Jab aap "Stranger Things" upload karte hain, Conductor hazaron chhote tasks create karta hai (inspection, encoding, subtitles, trailers). Agar ek subtitle file corrupt hai, toh sirf wahi task fail hota hai, poora video nahi.

---

## 🔧 9. Tech Stack / Tools
- **Netflix Conductor** – Java-based orchestrator, handles millions of workflows.
- **AWS Step Functions** – Serverless orchestration service (good for AWS native apps).
- **Apache Airflow** – Data pipelines ke liye popular, but video workflows ke liye bhi use hota hai.
- **Temporal.io** – Code-first workflow engine (modern & developer friendly).

---

## 📐 10. Architecture / Formula
**Parallelism Efficiency**
```
Total_Time = Max(Time_Video_Encode, Time_Audio_Encode) + Time_Overhead
```
*Linear*: Video (10m) + Audio (2m) = 12 mins.
*DAG Parallel*: Max(10m, 2m) = 10 mins. (20% faster just by splitting).

---

## 💻 11. Code / Flowchart (DAG JSON Example)
```json
{
  "name": "video_processing_workflow",
  "tasks": [
    {
      "name": "validation_task",
      "type": "SIMPLE",
      "next": ["fork_join_task"]
    },
    {
      "name": "fork_join_task",
      "type": "FORK_JOIN",
      "forkTasks": [
        [
          {
            "name": "encode_video_1080p",
            "type": "SIMPLE"
          }
        ],
        [
          {
            "name": "encode_audio_aac",
            "type": "SIMPLE"
          }
        ]
      ],
      "next": ["packaging_task"]
    },
    {
      "name": "packaging_task",
      "type": "SIMPLE"
    }
  ]
}
```
*Ye JSON batata hai: Pehle Validate karo, phir Video aur Audio ko parallel mein encode karo (Fork), aur ant mein Package karo (Join).*

---

## 📈 12. Trade‑offs
- **Gain:** Reliability, Scalability, Visibility | **Loss:** Setup complexity (Orchestrator maintain karna padta hai), Latency (queue overhead).
- **Gain:** Reusability (Validation task har workflow mein use karo) | **Loss:** Debugging distributed systems can be hard.

---

## 🐞 13. Common Mistakes
- **Mistake:** Monolithic Script (ek hi file mein sab kuch). *Fix*: Break into micro-tasks managed by DAG.
- **Mistake:** No Idempotency (Retry karne par data duplicate hona). *Fix*: Ensure output file names are unique/deterministic.
- **Mistake:** Infinite Retries. *Fix*: Set max retry limit (e.g., 3) and Dead Letter Queue (DLQ).

---

## ✅ 14. Zaroori Notes for Interview
1. **Mention DAG**: "Main video processing ke liye DAG workflow engine use karunga (jaise Netflix Conductor) taaki parallel processing aur granular retries possible hon."
2. **Explain 'Why'**: "Linear processing scale nahi karta. DAG se hum 4K encoding ko 100 chhote tasks mein tod kar 100 machines par run kar sakte hain."
3. **Draw the Diagram**: Show the Fork-Join pattern (Split -> Process -> Merge).

---

## ❓ 15. FAQ & Comparisons
**Q1: Cron Jobs vs Workflow Engine – Kya fark hai?**
A: Cron time-based hai (har raat 12 baje chalao). Workflow Engine event-based hai (jab video upload ho, tab chalao) aur dependencies manage karta hai (Task B after Task A). Complex systems ke liye Workflow Engine zaroori hai.

**Q2: Choreography vs Orchestration – Video processing ke liye kya best hai?**
A: **Orchestration (Conductor)** best hai. Ek central manager sabko batata hai kya karna hai. Video processing complex hai, isliye central control easy debugging aur monitoring deta hai. Choreography (Events) mein flow track karna mushkil ho sakta hai.

**Q3: Agar Orchestrator down ho jaye toh?**
A: Orchestrator state ko database (Cassandra/Redis) mein persist karta hai. Agar down hua, toh restart hone par wahin se resume karega jahan chhoda tha. High availability ke liye multiple orchestrator instances run karte hain.

**Q4: Long running tasks (e.g., 4K encoding) kaise handle karein?**
A: Async pattern use karein. Worker task start karta hai aur Orchestrator ko bolta hai "Main kaam kar raha hoon". Beech-beech mein heartbeat bhejta hai. Complete hone par callback deta hai.

**Q5: Dynamic DAGs kya hote hain?**
A: Kabhi-kabhi workflow runtime par decide hota hai. Jaise agar video 4K hai toh 5 resolutions encode karo, agar 720p hai toh sirf 2. DAG dynamic generate hota hai input ke basis par.

---

## 🎯 Module 19 Complete Summary
- **Topic 19.1**: Video Streaming System (HLS, CDN, Adaptive Bitrate) – User experience focus.
- **Topic 19.2**: Content Processor Workflow Engine (DAG) – Backend processing focus.
- **Key Takeaways**: HLS for playback, DAG for processing. Netflix Conductor is the industry standard for orchestration.
- **Interview Ready**: You can now explain both how video is played (Frontend/CDN) and how it is processed (Backend/DAG).
