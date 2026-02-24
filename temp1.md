I've gone through all your notes and extracted everything, page by page. I've converted the explanations into **Hinglish** (Roman script) as you requested, while keeping the technical terms and code snippets exactly as they are.

---

## Page 1: Unauthorized Access through Response Manipulation

### # Unauthorized Access through manipulating Status Code or Response message or Both

Pentesting ke time server response mein **status code** ya **response message** ko manipulate karna bohot useful hota hai taaki check kiya ja sake ki app different scenarios ko kaise handle karti hai.

**Scenario: Testing on App's response to Authentication failures**

* Maano tum ek login form test kar rahe ho. User correct username aur password submit karta hai aur server **200 OK** status aur **authentication token** ke saath respond karta hai.
* **Note:** Is case mein, hum response ko intercept karenge aur status code change kar denge authentication failure simulate karne ke liye aur dekhenge ki app use kaise handle karti hai.

### Steps to perform Response manipulation with Burp Suite:

1. **Enter correct username & password.**
2. **Capture the response:** Server response capture karo (likely a 200 OK with a token in the response body).
3. **Modify the Response Status Code:** Response ko client (browser) tak forward karne se pehle status code ko **200 OK** se change karke **401 Unauthorized** ya **403 Forbidden** kar do.
* *Tip:* Agar sure nahi ho ki 401/403 response kaisa dikhta hai, toh Google ya Burp Suite mein search karke waise hi modify kar lo.



---

## Page 2: Exploiting Frontend Logic

4. **Forward the modified Response to the client:**
* Sirf status code change karke baaki sab same rehne do. Agar web app ya frontend sirf status code ke base par react kar raha hai aur body ko check nahi kar raha...
* ...toh hackers isse exploit kar sakte hain! Wo server response status code ko **200 OK** mein modify karke kisi ke bhi account mein login kar sakte hain, bhale hi unhone **wrong username/password** dala ho.



### How to Know if frontend is only validating based on Server response status code?

* **Original Server response for Correct username & password:**
```http
HTTP/1.1 200 OK
Content-Type: application/json
{
  "token": "ey....",
  "user": {
    "id": 1234,
    "role": "user"
  }
}

```


*(Referenced as eq -> 1)*

---

## Page 3: Verifying the Vulnerability

* **Now, we will modify the original response to 403 or 401:**
```http
HTTP/1.1 403 Forbidden
Content-Type: application/json
{
  "error": "Authentication Failed"
}

```


* Agar ye modified response milne par frontend error message dikhata hai, toh humein idea mil jayega ki frontend decision ya toh status code, ya error message, ya dono ke base par le raha hai.



### Verification Steps:

1. **Case 1 (Status Code only):** Correct login ke time status code ko **200 OK** se **403 Forbidden** kar do lekin body same (eq -> 1 wali) rakho. Agar frontend "Unauthorized" popup dikhata hai, iska matlab frontend sirf **Status Code** par depend hai.
* *Hacker Exploit:* Wrong credentials dalo aur status code ko 200 OK kar do—hacker login ho jayega!


2. **Case 2 (Response Body only):** Wrong credentials dalo aur sirf response body change karke success wali (eq -> 1) kar do. Agar login ho jata hai, iska matlab decision **Response Body** par hai.
* *Note:* Kabhi kabhi dono (Status code + Body) change karne padte hain agar server dono check karta hai.



---

## Page 4: API Hacking & Burp Suite Tips (Date: 20/09/24)

### # I.C.M Security - API Hacking

**Section 3: Lab Setup & Burp Suite Introduction**

* **Note:** Agar body length aur status code correct aur incorrect login ke liye exact same hai, toh **Grep-match** method zyada reliable hai.
* **Steps for Grep-match:**
1. Intruder -> Options -> Grep-match par click karo.
2. 'Clear' click karke previous cheezein hatao.
3. 'Add' input box mein `1` dalo (ya jo bhi success flag ho).
4. Ye un requests ko highlight/flag kar dega jisme response body mein `1` (Correct) hai.


* Ye isliye karte hain kyunki wrong login par body mein `0` (Zero) aur correct par `1` (One) ho sakta hai, jabki baaki sab same ho.


* **Note for HTTP History:**
* Tum kisi bhi request par right-click karke use **color** de sakte ho taaki wo history mein alag se highlight ho aur tum use easily dhoond sako.



---

## Page 5: Scoping & Headers

* **Note on 'Add to Scope':**
* Jab tum kisi URL ko scope mein add karte ho, toh HTTP history tab mein filter enable kar sakte ho (**"Show only in-scope items"**).
* *Path:* Top right corner of HTTP history -> Filter icon -> Check "Show only in-scope items".


* **Pro Tip:** Poore base domain (e.g., `https://testphp.vulnweb.com`) ko scope mein add karna better hai bajaye sirf ek specific path (`/account`) ke, taaki saari relevant requests dikhein.
* **Note - 'Referer' header:** Ye server ko batata hai ki request kahan se originate hui (source page).
* **Note - 'Host' header:** Ye domain ya IP address hota hai jisse tum communicate kar rahe ho (where the request is sent).

---

## Page 6: Section 4 - Enumerating APIs

### #2) Fuzzing APIs:

Agar tum koi request Burp mein dekhte ho jaise:
`GET /api/v2/resources/books?published=1993`
Toh in jagahon par fuzzing try karo:

* `v2` ki jagah `v1` ya `v3`.
* `books` ki jagah `office` ya `users`.
* `published` ki jagah `unpublished`.
* Intruder use karke simple wordlist se attack karo single parameter ya multiple parameters par.

### #3) Discovery via Source Code:

* Frontend JavaScript files ko read karo taaki hidden URL paths mil sakein.
* Website par right-click -> **Inspect/Debugger**.
* Sari frontend JS files check karo aur route ya "juicy info" dhoondo.
* **Note:** Agar code readable nahi hai (minified hai), toh code copy karke Chrome mein **"JavaScript JS Formatter"** search karo aur wahan se format kar lo.

---

## Page 7: Section 5 & 6 - Authorization & JWT

### Section 5: Attacking Authorization

* **Note:** Agar koi ID mile (e.g., `vehicleId`), toh use manipulate karne ki koshish karo.
* **Note:** **Negative ID** dekar dekho, app break ho sakti hai aur error message mein "juicy info" (sensitive data) de sakti hai.

### Section 6: Attacking Authentication

**#4) JSON Web Tokens (JWT) -> Part 1 Theory**

* JWT base64 encoded data hota hai. Iske teen parts hote hain:
1. **Header**
2. **Payload**
3. **Signature**


* *(Example shown: eyh... . ey... . xxA...)*


* **Note:** `jwt.io` website par jab tum JWT daloge, toh right side mein decoded Header, Payload aur Signature input box dikh jayenge.

---

## Page 8: JWT Attacking (Part 2)

### #5) JSON Web Tokens -> Part 2 Attacking

Hum **hashcat** tool use karenge JWT secret key ko brute-force karne ke liye.

* Agar secret key mil gayi, toh hum payload change karke (e.g., `"user": "sat"` ko `"user": "admin"` mein) use usi key se sign kar sakte hain. Backend ise accept kar lega kyunki signature correct hoga.

**Hashcat Command:**
`hashcat -m 16500 <jwt_token> /path/to/wordlist.txt`

* `-m 16500` specify karta hai ki ye **JWT HMAC-SHA256** mode hai.

**Common Hash modes for JWT:**

* 16500 -> JWT HMAC-SHA256 (HS256)
* 16510 -> JWT HMAC-SHA384 (HS384)
* 16520 -> JWT HMAC-SHA512 (HS512)
* *Tip:* `jwt.io` ke header section mein tum dekh sakte ho ki konsa algorithm use ho raha hai.

---

## Page 9: JWT & Asymmetric Algorithms

* **Note:** Agar JWT asymmetric algorithms (RS256 ya ES256) se signed hai, toh wo is tarah brute-force nahi ho sakta kyunki wo private/public key pairs use karte hain. Ye method sirf **HMAC (HS256, HS384, HS512)** ke liye hai.
* **Note:** Jab hashcat password crack kar leta hai, toh terminal mein password dikhane ke liye aapko command ke end mein `--show` lagana padta hai:
`hashcat -m 16500 <jwt_token> <wordlist> --show`

**Once secret key is found:**

1. `jwt.io` par jao, encoded token paste karo.
2. Payload tab mein user ID change karo (e.g., `"userId": "admin"`).
3. 'Verify Signature' section mein secret key paste karo.
4. Ab ye naya token backend accept kar lega aur tum admin ban jaoge.

---

## Page 10: Section 7 - Injection

### #3) SQL Injection Lab:

1. **Send request to Intruder.**
* E.g., `GET /v1/001.php?id=$1$`


2. **Intruder -> Positions -> Attack type -> Sniper.**
3. **Payload tab -> Payload Options -> Add from list...**
4. List mein se **"Fuzzing SQL Injection"** select karo.
5. **Start Attack.**

* **Note:** Brute-force ke baad status code check karo (401, 501, 200...). Agar kisi payload par status code ya response length change hoti hai, toh iska matlab SQL injection possible hai.
* Ek baar confirm ho jaye, toh manually database se saare username aur password nikalne ki koshish karo.

---

I’ve extracted and converted the rest of your notes into **Hinglish** (Roman script), keeping all the technical commands and code snippets intact.

---

## Page 11: SQL & NoSQL Injection

### # SQL Injection (Continued)

SQL injection ke through data extract karne ke liye `UNION SELECT` ka use hota hai:
`GET /v1/001.php?id=5+UNION+SELECT+username,password,null,null+from+users--`

* Is query mein `+` symbols URL encoded spaces hain.
* `null` ka matlab hai wo fields jinse humein koi value nahi chahiye.

### #5) NoSQL Injection Lab:

**How to know if a web app uses MongoDB as a database?**

1. **Look for MongoDB-specific error messages:** Input fields mein special characters ya invalid data inject karke error trigger karo. Agar app MongoDB use kar rahi hai, toh aapko keywords dikhenge jaise:
* `MongoError`
* `E11000` (duplicate key error)


2. **Check for MongoDB-specific API responses:** Server ke bheje gaye response mein patterns dhoondo, jaise:
* Fields like `_id`, `objectId`, or `bsontype`.
* **Example Response:** `{"id": "507...", "username": "admin", "created_at": "2023/..."}`



---

## Page 12: Tools & NoSQL Injection Types

### # Tools to Detect Tech Stack:

* **Wappalyzer:** Ek browser extension hai jo website ki technologies detect karta hai.
* **BuiltWith:** Ek online tool hai jahan URL enter karke aap website ki poori technology profile dekh sakte ho.

### # NoSQL Injection Methods:

**1) Boolean Based Injection:** Ismein hum aisi condition inject karte hain jo hamesha **true** evaluate ho, taaki authentication bypass ho sake.

* **Example Query:** `db.users.find({"username": username, "password": password})`
* **Attacker's Injection:**
* Username: `"admin"`
* Password: `{"$ne": null}`


* **Final Query:** `db.users.find({"username": "admin", "password": {"$ne": null}})`
* **Result:** Ye query us user ko return karegi jiska username "admin" hai aur password null nahi hai (jo ki true hi hoga), isse authentication bypass ho jata hai.

---

## Page 13: Advanced NoSQL Bypass

### # Bypassing Username and Password:

Dono fields bypass karne ke liye `$or` operator ya existing fields ka use kar sakte ho.

* **Injection:** `username: {"$exists": true}, password: {"$ne": null}`
* **Logic:** Ye query kisi bhi aise user ko return karegi jahan username field exist karti ho aur password null na ho. Isse specific username ki zaroorat nahi padti.

### #2) Query Parameter Manipulation:

Attacker extra parameters add karke query manipulate karta hai, kabhi kabhi query ke andar JavaScript bhi execute karwa deta hai.

* **Example Query:** `db.users.find({"username": username})`
* **Attacker's Injection:** `username: {"$where": "this.username == 'admin'"}`
* **Result:** Ye injected JS code server par execute hota hai aur result "admin" user return karta hai.

---

## Page 14: Command Injection in NoSQL

### #3) Command Injection:

MongoDB operators ka use karke query ka behavior badal dena.

* **Original:** `db.users.find({"username": username})`
* **Injection:** `username: {"$gt": ""}`
* **Modified Query:** `db.users.find({"username": {"$gt": ""}})`
* **Result:** `$gt` (greater than) operator un saare usernames ko check karega jo empty string से bade hain. Isse database ke saare non-empty users expose ho sakte hain.

---

## Page 15: Mass Assignment & Method Brute-forcing

### # Section 8 -> Mass Assignment

* **Note:** Aap Intruder ka use karke **Request Method** ko bhi brute-force kar sakte ho taaki pata chale ki kaunse methods allowed hain.
* **Example:** `GET /workshop/api/shop/products`
* Intruder/Payloads mein `HTTP verbs` select karo (GET, POST, PUT, DELETE, etc.).
* Agar kisi method (jaise POST) ke liye **200 Status Code** milta hai, toh iska matlab wo method allowed hai.
* **Next Step:** Ab wahi request POST method ke saath bhejo. Agar response mein "username required" aata hai, toh samajh jao ki aap naya user create ya modify kar sakte ho.

---

## Page 16: Burp Suite Scoping

### # Burp Suite Target Scope Configuration:

HTTP history tab mein sirf specific domain ka traffic dekhne ke liye scope configure karein:

1. **Set the Target Scope:** Target tab -> Scope -> 'Add' par click karein aur domain dalo (e.g., `https://example.com`).
2. **Configure Interception:** Proxy tab -> Intercept -> Options. "Intercept client requests" aur "Intercept server responses" section mein **"Intercept requests/responses based on the current target scope"** select karo. Isse फालतू traffic intercept nahi hoga.

---

## Page 17: Filtering & Settings

### #3) Filter HTTP History:

* Proxy -> HTTP history tab ke top par filter options par click karo.
* **"Show only in-scope items"** select karo. Ab sirf aapke defined scope ka traffic dikhega aur baaki ignore ho jayega.

### # To see all Request-Response in 'Intercept' tab:

1. Click on 'Settings'.
2. Tick `[✓] Intercept response based on the following rules`.
3. Tick `[✓] OR Request was intercepted`.

* Ye karne ke baad aap har request ka server response dekh paoge.

---

## Page 18: No-Rate Limit & Clickjacking

### # No-Rate Limit Attack on Password Reset:

Agar password reset feature par rate limit nahi hai, toh attacker baar-baar OTP ya reset links request kar sakta hai.

* **Exploit:** Burp Suite ya Python script se spamming karna. Isse user ka email bhar jayega ya DoS (Denial of Service) ho sakta hai.
* **Fix:** 1-2 OTPs per minute ki limit lagao aur Captcha use karo.

### # Clickjacking Attack:

Clickjacking ek aisa attack hai jahan hacker aapko kisi aisi cheez par click karne ke liye trick karta hai jahan aapka iraada nahi tha. Hacker ek legitimate website (jaise bank) ko ek **invisible frame** ke andar apne fake website par chhupa deta hai.

* **Example:** Auto-liking ya sharing a post.
* Hacker ek fake webpage banata hai (e.g., "Click here to watch cute video").
* Is button ke neeche invisible iframe mein Facebook ka "Like" ya "Follow" button hota hai.

---

## Page 19: Clickjacking (cont.) & Session ID

* Jab aap fake button par click karte ho, toh aap anjaane mein Facebook post share ya like kar dete ho kyunki aap pehle se logged-in the.
* **Note:** Is attack mein aapko koi form bharne ki zaroorat nahi padti, attacker bas aapke existing session ka fayda uthata hai.

### # Session ID:

* **Session ID** ek unique identifier hai jo tab generate hota hai jab user login karta hai. Ye server ko track rakhne mein madad karta hai ki user ne kaunse pages visit kiye, taaki baar-baar login na karna pade.
* **How it is used:** Ye ID cookie mein store hoti hai aur har request ke saath server ko bheji jaati hai.
* **Security Risk:** Agar attacker ye Session ID chura leta hai (Hijacking ya Cookie theft), toh wo user ke account ka access pa sakta hai bina password ke.
* **Note:** Sabse badi problem tab hoti hai jab **Session ID change nahi hoti**. Hacker us static session ID ka use karke kabhi bhi login kar sakta hai.

---

Bhai, aapke notes base clear karne ke liye bohot solid hain, khaas karke **JWT** aur **NoSQLi** wala part aapne kaafi detail mein cover kiya hai. Lekin agar hum "Industry Standards" aur "Senior Pentester" ke point of view se dekhen, toh kaafi saare critical topics abhi missing hain jo modern API security testing mein must-have hote hain.

Yahan missing topics ki structured list hai jo aapko apne notes mein add karni chahiye:

### 1. Broken Object Level Authorization (BOLA / IDOR)

Aapne "Attacking Authorization" mein ID manipulation touch kiya hai, lekin BOLA industry ka **#1 API Risk** hai. Ismein aapko ye sub-topics missing lag rahe hain:

* **Massive BOLA:** Multi-tenancy environment mein ek organization ka user dusri organization ka data kaise access karta hai.
* **BOLA in Delete/Update:** Sirf GET requests nahi, balki `DELETE /api/user/123` jaisi requests test karna.
* **UUID/GUID Brute-forcing:** Agar ID predictable nahi hai (like UUID), toh use leak karne ke methods (Search results, Logs, etc.).

### 2. Broken Property Level Authorization (BPLA)

Ye OWASP 2023 ki naye category hai jo aapke notes mein nahi hai:

* **Mass Assignment (Advanced):** Aapne method brute-forcing likha hai, lekin "Hidden Properties" dhoondna (jaise `is_admin: true` ya `role: superuser`) missing hai.
* **Excessive Data Exposure:** Server response mein aisi properties aana jo frontend ko nahi chahiye (jaise user ka mobile number ya internal ID).

### 3. Server-Side Request Forgery (SSRF) in APIs

Modern APIs aksar dusre internal services se communicate karti hain.

* **Exploiting via Webhooks:** API parameters mein apna URL dalkar server se request karwana.
* **Cloud Metadata Exploitation:** API ke zariye AWS/Azure ke internal metadata (169.254.169.254) ka access lena.

### 4. GraphQL Specific Attacks

Aapne REST APIs cover ki hain, lekin modern apps **GraphQL** use karti hain jiske attacks bilkul alag hote hain:

* **Introspection Queries:** Poora database schema (queries/mutations) extract karna.
* **Circular Queries (DoS):** Aisi query bhejna jo server ko infinite loop mein daal de.
* **Direct Object Injection:** GraphQL queries mein nested objects manipulate karna.

### 5. Advanced Recon & Tooling

Professional level par discovery manual nahi hoti:

* **Documentation Analysis:** Swagger (OpenAPI) ya Postman collections se hidden endpoints dhoondna.
* **Active Recon Tools:** **Kiterunner** (context-aware fuzzing) aur **Arjun** (parameter discovery) ka use.
* **Passive Recon:** GitHub dorks ya JS files se hidden API keys aur secrets nikalna.

### 6. OAuth 2.0 & OIDC Vulnerabilities

Sirf JWT kafi nahi hai, login flows bhi test karne hote hain:

* **Redirect URI Manipulation:** Authorization code ko apne server par redirect karwana.
* **State Parameter Missing:** CSRF attacks in OAuth flow.
* **Token Leakage:** Referer headers ke zariye access token churaana.

### 7. Security Misconfigurations (Modern)

* **CORS (Cross-Origin Resource Sharing):** `Access-Control-Allow-Origin: *` ki wajah se sensitive data leak hona.
* **HPP (HTTP Parameter Pollution):** Same name ke do parameters bhejna (e.g., `?id=1&id=2`) taaki security filter bypass ho sake.

---

**Next Step:** Kya aap chahte hain ki main **BOLA (Broken Object Level Authorization)** se shuru karun aur aapko iska ek practical industry-standard roadmap aur lab setup samjhaun?