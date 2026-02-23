## **Module 13: Advanced BApp Extensions – Deep Dive**

*Burp ki basic functionality kaafi hai, lekin extensions se ye Iron Man ban jata hai. BApp Store se ye must-have extensions install karo.*

### Topic 13.1: AuthAnalyzer / AuthMatrix – IDOR Automation
**Installation:** BApp Store > Search > Install

**AuthAnalyzer Workflow:**
1. **Record Base Request:** Admin user ki request capture karo.
2. **Add Test Users:** Low-privilege user, anonymous user, different roles.
3. **Configure Parameters:** Session tokens, cookies, headers automatically replace honge.
4. **Run Analysis:** Ek saath 100+ users ke saath request replay.
5. **Compare Responses:** Status code, length, content analysis – jo admin jaisa response de, woh IDOR hai.

**AuthMatrix Features:**
- **Role Matrix:** Admin, Manager, User, Guest - sabke saath test.
- **Unauthenticated Checks:** Bina login ke kya access ho raha hai.
- **Forced Browsing Detection:** Hidden endpoints par role-based access.

> **Pro-Tip:** "Manual IDOR testing? 100 users hain toh saal lag jayenge. AuthAnalyzer laga, ek baar config kar aur soja. Jo response admin jaisa dikhega, wahi IDOR hai. Pro tip: 401 vs 200 ka difference dekh, 200 aaya toh bug confirmed."

### Topic 13.2: Turbo Intruder – Race Conditions & High-Speed Attacks
**Installation:** BApp Store > Turbo Intruder

**Python-Based Architecture:**
```python
def queueRequests(target, weapons):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=10,
                           requestsPerConnection=100,
                           pipeline=False)
    for i in range(1000):
        engine.queue(target.req, i)
```

**Race Condition Testing:**
1. **Scenario:** Ek coupon code ko multiple times apply karna.
2. **Turbo Intruder Setup:** 50 concurrent requests ek saath bhejo.
3. **Analyze:** Agar ek se zyada baar apply ho gaya, race condition.

**Use Cases:**
- **Gift Card Redeem:** Ek card multiple baar redeem.
- **Inventory Bypass:** Limited stock mein ek saath multiple orders.
- **Rate Limit Bypass:** WAF ko overwhelm karo.

**Configuration Options:**
- **Concurrent Connections:** 1 se 100+.
- **Requests per Connection:** Keep-alive connections.
- **Pipelining:** HTTP pipelining enable/disable.
- **Failed Request Handling:** Retry policies.

> **Pro-Tip:** "Normal Intruder 1 sec mein 10 requests bhejta hai, Turbo Intruder 1000. Race condition dhundhni hai? Coupon code ek hi baar apply hona chahiye, lekin 50 requests ek saath bhej. Agar 2 baar apply ho gaya, toh race condition mil gayi. Payment logic test karne ka ye sabse tez tarika hai."

### Topic 13.3: Param Miner – Hidden Parameter Discovery
**Installation:** BApp Store > Param Miner

**Core Functionality:**
- **Passive Scan:** Background mein chalta hai, hidden parameters detect karta hai.
- **Active Scan:** Custom wordlist se parameters brute-force karta hai.

**Detection Capabilities:**
- **Cache Poisoning Parameters:** `?cb=123` jaise cache busters.
- **Hidden GET/POST Parameters:** Jo UI mein nahi dikhte.
- **Server Headers:** `X-Forwarded-For`, `X-Original-URL` etc.
- **Framework Specific:** `_method` (HTTP method override), `debug` parameters.

**Parameter Brute-Forcing:**
1. Request select karo > Right Click > Extensions > Param Miner > Guess GET/POST parameters.
2. Wordlist se thousands parameters try honge.
3. Jo naye parameters response change karein, woh vulnerable ho sakte hain.

**Use Cases:**
- **Hidden Admin Functions:** `?admin=true`, `?debug=1`.
- **SQL Injection Points:** Hidden parameters jo server process karta hai.
- **Cache Poisoning:** Unique parameters cache behavior change kar sakte hain.

> **Pro-Tip:** "UI mein 3 parameters dikhte hain, backend mein 10 process hote hain. Param Miner un hidden 7 ko dhoond ke laata hai. Jaise `?test=1` daala aur response mein 'Test Mode Enabled' aaya, iska matlab developer debug mode bhool gaya. CVE yahin se shuru hoti hai."

### Topic 13.4: JWT Editor – JSON Web Token Testing
**Installation:** BApp Store > JWT Editor

**Key Features:**
- **View/Edit JWTs:** Tokens ko decode karo, claims modify karo.
- **Signing Keys Management:** New keys generate karo, existing import karo.
- **Attack Automation:** Built-in attacks with one click.

**Attack Types:**
**A. Algorithm Confusion**
- `alg: HS256` ko `alg: none` mein change karo.
- Server accept karta hai? Authentication bypass.

**B. Key Confusion (RS256 -> HS256)**
- Public key se sign karo as HS256.
- Server public key verify karega? RCE possible.

**C. Brute-Force Weak Secrets**
- Weak signing key? JWT Editor brute-force karega.

**D. Kid (Key ID) Injection**
- `kid` parameter mein path traversal: `../../../../dev/null`
- SQL injection in `kid`: `' UNION SELECT ...`

**Workflow:**
1. Request capture karo with JWT.
2. Send to JWT Editor.
3. Modify claims (e.g., `"admin": true`).
4. Re-sign with appropriate key.
5. Send modified request.

> **Pro-Tip:** "JWT mila? Pehle `alg: none` try kar. Agar server ne maan liya, poora authentication bypass. Phir `kid` parameter dekh, path traversal try kar. Weak signing key hai? Brute-force kar. Modern APIs ki chabi JWT editor ke paas hai."

### Topic 13.5: Other Essential Extensions
| Extension | Purpose | Pro-Tip |
|-----------|---------|---------|
| **Active Scan++** | Additional scan checks | Burp's default scan se zyada vulnerabilities detect karta hai |
| **Backslash Powered Scanner** | Advanced injection points | Encoding bypass ke liye |
| **CSP Auditor** | Content Security Policy analysis | CSP bypass techniques |
| **Freddy** | Deserialization testing | Java/Node/PHP deserialization |
| **GAP** | Wayback machine integration | Archived URLs se endpoints dhoondho |
| **HTTP Request Smuggler** | Request smuggling | Modern HTTP/2 attacks |
| **JS Miner** | JavaScript analysis | Hidden endpoints in JS files |
| **403 Bypasser** | Access control bypass | 403 forbidden ko 200 mein convert |

---

## **Module 14: API & Modern Web Testing**

*Aaj ki apps APIs par chalti hain – REST, GraphQL, WebSockets. Burp ko inke hisaab se taiyar karo.*

### Topic 14.1: JWT (JSON Web Tokens) Deep Dive
**JWT Structure:**
`header.payload.signature` – teeno parts Base64 encoded.

**Critical Vulnerabilities:**
- **None Algorithm Attack:** Header mein `alg` ko `none` karo, signature hata do. Server accept karta hai?
- **Algorithm Confusion (CVE-2016-10555):** RS256 (asymmetric) public key available hai. HS256 (symmetric) mein same public key use karo. Server verify kar lega?
- **Key Injection (CVE-2018-0114):** `jku` (JWK Set URL) header mein apna server URL daalo. Server aapki public key use karega.
- **Weak HMAC Key:** Weak secret (e.g., "secret") ko brute-force karo (`hashcat -m 16500`).
- **Kid Parameter Injection:** Path Traversal, SQL Injection.

> **Pro-Tip:** JWT mila toh pehle step: Base64 decode karo. Header mein `alg: none` try kar. Kaam kiya? Critical bug. Phir `kid` parameter dekh, path traversal try kar.

### Topic 14.2: GraphQL Testing
**GraphQL Basics:**
- Single endpoint (usually `/graphql`).
- POST requests with JSON body.
- Introspection se poora schema pata chal sakta hai.

**Reconnaissance:**
```graphql
query { __schema { types { name fields { name type { name kind } } } } }
```
- Agar introspection enabled hai, toh saare queries, mutations, fields dikh jayenge.

**Common Attacks:**
- **Introspection Enabled – Hidden Fields:** Schema mein `isAdmin`, `resetPassword` jaisi fields dhoondo jo UI mein nahi hain.
- **Batching Attacks (Rate Limit Bypass):** Ek request mein multiple mutations bhej kar rate limit bypass.
- **Deep Recursion Queries (DoS):** Circular queries se server resource exhaust.
- **Field Duplication:** Same field multiple times – server overload.
- **Injection in Arguments:** SQL/NoSQL injection in arguments.

> **Pro-Tip:** GraphQL endpoint mila? Pehle introspection query bhej. Schema mil gaya? Ab hidden fields search kar. Batching attack se rate limit bypass kar aur saara data nikaal.

### Topic 14.3: WebSockets Testing
**WebSocket Basics:** Full-duplex communication, persistent connection (ws://, wss://).

**Burp Configuration:**
- Proxy automatically WebSocket traffic intercept karta hai.
- **WebSockets History tab** mein saare messages dikhte hain.
- **Intercept WebSocket messages:** Proxy > Intercept > WebSocket sub-tab.

**Testing Methodology:**
- **Message Interception & Modification:** Real-time modify karo – XSS, IDOR.
- **Replay Attacks:** WebSocket message copy karo, Repeater ke WebSocket tab mein paste karo, send karo.
- **Connection Manipulation:** Origin header bypass, authentication bypass.
- **Injection Attacks:** SQL injection, command injection in messages.
- **Denial of Service:** Infinite messages, large payloads.

> **Pro-Tip:** WebSocket traffic intercept kar. Chat app test kar raha hai? Message mein XSS payload daal. Admin ko message bhej, jab wo dekhega, tera XSS trigger. IDOR check: `to` parameter change kar ke kisi aur ka message padh le.

### Topic 14.4: Content-Type Confusion & XXE
**Concept:** API accepts JSON but XML bhej kar dekho.

**JSON to XML Conversion:**
```
POST /api HTTP/1.1
Content-Type: application/xml
<user>admin</user>
```

**XXE (XML External Entity) Testing:**
```xml
<?xml version="1.0"?>
<!DOCTYPE root [
<!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<user>&xxe;</user>
```

**Swagger/OpenAPI Discovery:**
- `/swagger.json`, `/swagger/v1`, `/api-docs` – ye endpoints often open hote hain.
- Mil gaya? Saare API endpoints ki list mil gayi, ab systematically test kar.

> **Pro-Tip:** JSON API hai toh XML bhej ke dekh. Accept kiya? XXE try kar. `/etc/passwd` read kar liya? Critical bug.

---

## **Module 15: Mobile Pentesting with Burp**

*Mobile apps ko intercept karna thoda tricky hai, lekin zaroori hai. SSL pinning, invisible proxy – ye sab aana chahiye.*

### Topic 15.1: SSL Pinning Bypass
**Problem:** Mobile apps Burp certificate accept nahi karte (SSL pinning).

**Solutions:**
- **A. Frida:**
  ```bash
  pip install frida-tools
  frida -U -f com.target.app -l frida-multiple-unpinning.js
  frida -U com.target.app -l ios-ssl-bypass.js
  ```
- **B. Objection:**
  ```bash
  pip install objection
  objection -g com.target.app explore
  > android sslpinning disable
  > ios sslpinning disable
  ```
- **C. Xposed Modules:** JustTrustMe, SSLUnpinning.
- **D. Re-patching APK:** APK decompile, network security config modify, recompile, sign.

> **Pro-Tip:** Mobile app mein traffic nahi aa raha? SSL pinning hai. Pehle Frida script try kar. 2 minute mein bypass ho jayega. Yaad rakh: pehle bypass, phir intercept.

### Topic 15.2: Invisible Proxying
**When Needed:** Apps jo system proxy ignore karte hain.

**Windows Setup:**
1. Burp > Proxy > Options > Add > Bind to port `8080`, All interfaces.
2. **Request Handling:** Support invisible proxying (enable).
3. Windows: `netsh winhttp set proxy localhost:8080`

**Linux/Android (iptables):**
```bash
iptables -t nat -A OUTPUT -p tcp --dport 80 -j DNAT --to-destination 127.0.0.1:8080
iptables -t nat -A OUTPUT -p tcp --dport 443 -j DNAT --to-destination 127.0.0.1:8080
```
- Saara traffic Burp par forward ho jayega.

**Transparent Proxy Mode:** Client ko proxy settings nahi batani padti, traffic automatically redirect.

> **Pro-Tip:** App proxy ignore kar raha hai? Invisible proxying mode on kar. Android rooted hai? iptables use kar ke saara traffic Burp par forward kar. Ab app ko pata bhi nahi chalega ki proxy use ho raha hai, lekin tu saara traffic dekh raha hai.

### Topic 15.3: Non-HTTP Traffic Interception
**Problem:** Mobile apps custom protocols use karte hain (XMPP, MQTT, raw TCP).

**Solution:** Burp Proxy Listener with invisible mode + network redirect. Burp raw data capture karega, tum manually analyze karo.
- **XMPP (Chat apps):** Port 5222, messages decode karo.
- **MQTT (IoT):** Port 1883, subscribe/publish messages, topic enumeration.
- **Custom Protocols:** Hex dump analysis, pattern identification, replay attacks.

### Topic 15.4: Burp Mobile Assistant
**Android Setup:**
1. Burp > Extender > BApp Store > Install Burp Mobile Assistant.
2. Android device par assistant app install karo.
3. QR code scan karo for configuration.

**Features:** Automatic proxy configuration, certificate installation helper, traffic recording controls.

**iOS Setup:** Manual proxy config, certificate install via Safari, trust certificate in Settings.

> **Pro-Tip:** Burp Mobile Assistant use kar, life easy ho jayegi. Ek click mein proxy set, certificate install. iOS mein certificate trust karna mat bhool.

---

## **Module 16: WAF/IPS Evasion Techniques**

*WAF tumhe block karta hai? Koi baat nahi, ye techniques seekh lo.*

### Topic 16.1: Advanced Match/Replace Rules
Burp ke Match/Replace se tum har request mein changes kar sakte ho.
- **User-Agent Rotation:** Randomly different User-Agent bhejo.
- **Header Randomization:** `X-Forwarded-For` spoofing, `Accept-Language` variation.

### Topic 16.2: Payload Obfuscation
**Encoding Techniques:**
- Base64, URL encoding (double, UTF-8), HTML entities, Unicode normalization.
- **Case Manipulation:** `<ScRiPt>alert(1)</ScRiPt>`
- **Comments Injection:** `SEL/*foo*/ECT/*bar*/username`

### Topic 16.3: Parameter Pollution
```
?id=1&id=2&id=3
?user=admin&user=guest
```
- Server kaunsa lega? Pehla? Akhri? Dono? Confusion paida karo.

### Topic 16.4: Rate Limiting Bypass
- **Resource Pool:** Delay between requests, random delays.
- **IP Rotation:** Upstream proxy chains, SOCKS proxy (Tor), residential proxies.
- **Session Rotation:** Har kuch requests ke baad new session, cookies clear.

### Topic 16.5: Request Splitting/Smuggling
**CL.TE (Content-Length vs Transfer-Encoding):**
```
POST / HTTP/1.1
Content-Length: 13
Transfer-Encoding: chunked

0

GET /admin HTTP/1.1
```
**TE.CL:** Reverse.

### Topic 16.6: WAF Fingerprinting & Bypass
**Identify WAF:** Response headers (`Server: cloudflare`), block page content.
**Bypass Techniques:**
- Size Limits Bypass (chunked requests).
- Signature Evasion (null bytes `%00`, newlines `%0a`).
- HTTP Verb Tampering (`HEAD /admin`, `POST /admin with GET parameter`).

> **Pro-Tip:** WAF block kar raha hai? Slow down. IP rotate kar. Payload encode kar. WAF confuse ho jayega. Phir bhi block ho raha hai? Request smuggling try kar. WAF ek request dekh raha hai, backend doosri.

---

## **Module 17: Advanced Scanning & Automation**

*Burp Professional ke scanning features ko optimize karo.*

### Topic 17.1: Custom Scan Configurations
- **Scan Speed vs Accuracy:**
    - Fast Scan: Critical issues only (5-10 min).
    - Deep Scan: All checks (1-2 hours).
    - Stealth Scan: Low and slow (1 request/sec).
- **Insertion Points:** Sab parameters, headers, cookies, JSON/XML nodes.

### Topic 17.2: Application Login Configuration
- **Recorded Login Sequences:** Manually login karte waqt Burp record kare, phir scan mein use kare.
- **Credential Management:** Multiple usernames/passwords provide karo.
- **2FA Handling:** OTP entry automation (advanced, but possible with macros).

### Topic 17.3: Resource Pools for Scale
- **Custom Pool Settings:** "WAF Bypass" – max concurrent 2, delay 2000ms, retries 3 with exponential backoff.
- **Pool Assignment:** Intruder → Aggressive pool (50 concurrent). Scanner → Balanced pool (10 concurrent). Manual testing → Single-threaded pool.

### Topic 17.4: Scheduled Scanning
- Burp Professional mein scheduled scans feature hai.
- Night scans schedule karo jab traffic kam ho.
- Email notifications.

> **Pro-Tip:** Scanner chala raha hai aur WAF block kar raha hai? Stealth mode use kar. Raat ko scan scheduled kar. Login sequence record kar ke de, scanner automatically login karega aur andar ke pages bhi scan karega.

---

## **Module 18: Professional Reporting & Remediation Verification**

*Bug dhoondhna aadha kaam hai, report likhna aur fix verify karna baaki aadha.*

### Topic 18.1: Client-Ready Reporting
- **Executive Summary:** Non-technical overview for management – risk, impact, business context.
- **Technical Findings:** Detailed steps, proof of concept (POC), screenshots, request/response.
- **CVSS Scoring:** Correct severity calculation – Base, Temporal, Environmental.
    - CVSS v3 calculator use karo. Impact aur Exploitability metrics samjho.

### Topic 18.2: Remediation Verification
- Client fix apply karega, tumhe re-test karna hoga.
- **Proof of Fix:** Same POC run karo, confirm vulnerability resolved.
- **False Positive Handling:** Scanner ki report mein false positives ho sakte hain. Manually verify karo aur report se hatao.

### Topic 18.3: Generating Reports in Burp
- **Target** tab → right-click on host → **Generate report**.
- Choose report type: HTML, XML.
- Select issues, include request/response, remediation.
- Customize template (if Pro).

> **Pro-Tip:** Report aisi banao ki CTO padh kar budget approve kare aur developer padh kar fix kar sake. Screenshots clear hon, steps reproducible hon.

---

## **Module 19: Custom BCheck Scripts**

*Burp Professional mein custom scan checks likhne ki language hai – BCheck. Isse app-specific logic bugs scanner mein add kar sakte ho.*

### Topic 19.1: What is BCheck?
- BCheck Burp ki scripting language hai jo custom active/passive scan checks banane deti hai.
- `.bcheck` files mein likhi jati hain.

### Topic 19.2: Basic BCheck Structure
```
metadata:
  language: v1-beta
  name: "Custom SQLi Check"
  description: "Detects SQL injection in parameter 'id'"
  author: "Your Name"

given host then
  send request:
    method: GET
    path: "/page?id=1'"
    follow-redirects: false

  if response.status == 200 and response.body contains "SQL syntax" then
    report issue:
      severity: high
      confidence: certain
      detail: "SQL injection detected with single quote."
```

### Topic 19.3: Use Cases
- **App-specific logic:** Tumhe pata hai ki is app mein 'X-Header' se SQLi hota hai, uska custom check banao.
- **Compliance checks:** Check karo ki specific headers present hain ya nahi.
- **False positive reduction:** Custom checks se noise kam karo.

### Topic 19.4: Sharing BCheck Scripts
- Team ke saath share karo.
- Burp BApp Store mein bhi contribute kar sakte ho.

> **Pro-Tip:** Default scanner sabke liye same hai, par tumhara client unique hai. BCheck scripts likhna seekh. Ye tumhe baaki testers se alag banata hai.

---

## **Module 20: Burp REST API & DevSecOps**

*Burp ko command line se chalana, CI/CD mein integrate karna – ye next level automation hai.*

### Topic 20.1: Burp REST API
- Burp Professional mein REST API enable kar sakte ho. Port usually 1337, authentication via API key.

### Topic 20.2: Common API Endpoints
- `/scan` – Start a new scan.
- `/scans` – List scans.
- `/issues` – Get findings.
- `/report` – Generate report.

### Topic 20.3: CI/CD Integration
**Jenkins / GitLab CI / GitHub Actions:**
- Code push hote hi automatically Burp scan trigger karo.
- API call bhejo scan start karne ke liye.
- Scan complete hone par report fetch karo.
- Build fail karo agar critical issues hain.

**Example curl command:**
```bash
curl -X POST "http://localhost:1337/v0.1/scan" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"urls": ["https://staging.example.com"], "scan_configurations": ["ci_cd_scan"]}'
```

### Topic 20.4: Headless Burp (CLI)
- Burp Suite Pro command line se bhi chala sakte ho – headless mode.
- Load project file, start scan, export results.

> **Pro-Tip:** Bhai, sirf GUI pe depend mat reh. Seekh ki Burp REST API se scan kaise trigger karte hain. Jab developer code push kare, toh automatically Burp scan run hona chahiye. Ye hi asli DevSecOps hai.

---

## **Module 21: Cloud Security & Team Collaboration**

### Topic 21.1: Cloud Security Testing with Burp
**Cloud Metadata Service:**
- **AWS:** `http://169.254.169.254/latest/meta-data/`
- **Azure:** `http://169.254.169.254/metadata/instance?api-version=2017-08-01`
- **GCP:** `http://metadata.google.internal/computeMetadata/v1/`

**SSRF Vulnerability mein:** Tum Burp se request bhej kar in endpoints ko hit kar sakte ho. Agar server ne response diya, to IAM credentials, instance data leak ho sakta hai.

**IAM Credential Leakage:**
- AWS metadata se temporary credentials milte hain: `http://169.254.169.254/latest/meta-data/iam/security-credentials/<role-name>`
- Ye credentials use karke tum AWS resources access kar sakte ho.

**Cloud Storage Buckets:**
- **S3 buckets:** `https://<bucket>.s3.amazonaws.com`
- **Azure Blob:** `https://<storage>.blob.core.windows.net/<container>`
- Misconfiguration testing via Burp – try listing buckets, accessing private files.

**Serverless Testing:**
- AWS Lambda, API Gateway – API endpoints test karo. Serverless functions often have misconfigured permissions.

> **Pro-Tip:** Sirf app mat todo, uske peeche ka cloud todo. SSRF mila? Toh seedha AWS Metadata hit karne ki koshish kar. Agar wahan se IAM credentials mil gaye, toh poora cloud compromise. Ye bug bounty mein highest payout deta hai.

### Topic 21.2: Team Collaboration & Project Management
- **Burp Project Files (.burp):** State save/restore karo. Ek engagement ke saare findings, requests, responses ek file mein save ho jate hain.
- **Project Merging:** Do testers ka kaam ek file mein merge karo. Burp mein import functionality hai.
- **Comments & Issue Assignment:** Har issue par comment add kar sakte ho – "Needs verification", "Fixed, waiting for re-test". Team members ko assign kar sakte ho.
- **Scan Comparison:** Purane scan aur naye scan ka comparison – regression testing. Check karo ki jo issues pehle the, wo fix ho gaye ya nahi.

> **Pro-Tip:** Team mein kaam karte ho toh project files ka version control rakhlo. Git mein bhi daal sakte ho. Comments se communication clear rahega.

---

## **Module 22: Extra Tips & Tricks (Pro Level)**

*Ye wo tips hain jo ek **Noob** aur **Pro Pentester** ke beech ka difference dikhati hain.*

- Aap URL copy karke seedha **Repeater** tab mein `Right Click -> Paste URL as Request` kar sakte hain.
- > **Note:** **HACKTOOLS** Firefox extension hacker's ke liye best hai.
    > * Is extension mein aapko saare **Payloads** mil jayenge (e.g., XSS payloads).
    > * Isme aapko har language ke **Reverse Shell** payloads (Python, Bash, Netcat, etc.) milte hain.
    > * Ye hacking ke liye ek unique extension hai jo aapka kaafi time save karti hai.

---

========================================================================================
