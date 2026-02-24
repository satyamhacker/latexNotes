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


