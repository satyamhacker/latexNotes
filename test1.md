## 🧩 Module 0: API Hacking Mindset & Methodology

Is module mein hum API hacking ki **soch** aur **approach** seekhenge. Yeh foundation hai, agar ye clear nahi hoga, baaki sab bekaar hai.

---

### 0.1 🎯 Title: API vs Web App – Dono mein farak hai bhai!

#### 🐣 Samjhane ke liye (Analogy)
Socho tum ek **Dukaan (Web App)** mein gaye. Wahan ek salesman (UI) hai jo tumse baat karta hai, product dikhata hai, bill banata hai. Lekin agar tum **godown (API)** mein seedha ghus gaye, to salesman ko bypass kar ke stock check kar sakte ho, price change kar sakte ho, ya direct samaan nikal sakte ho. API exactly yahi hai – **bina UI ke backend se baat karne ka tareeka**.

#### 📖 Technical Definition
- **Web Application:** User Interface (HTML, CSS, JS) ke through interact karta hai. Requests browser se aati hain, responses render hote hain. 
- **API (Application Programming Interface):** Machine-to-machine communication. Direct backend se baat hoti hai, generally JSON/XML format mein. Koi UI nahi, sirf endpoints hote hain jo specific functions perform karte hain.

#### 🧠 Zaroorat Kyun Hai?
API testing mein humein UI ke jhanjhat se nahi ulajhna, seedha backend logic ko todna hai. Isliye API aur web app ka difference samjhe bina, API hacking mumkin nahi.

#### 🔍 Visual - Screen Par Kya Dikhega
- **Web App:** Browser mein URL type karo, ek page khulta hai, forms hain, buttons hain.
- **API:** Koi UI nahi. Tum tool (Burp, Postman) mein direct endpoint hit karoge aur raw JSON response dekhega.

#### ⚙️ Under the Hood
Web app request mein usually headers hote hain jaise `User-Agent`, `Cookie`, `Referer`, aur response mein HTML content. API request mein content-type `application/json` hota hai, authentication token `Authorization` header mein jaata hai, response structured data (JSON/XML) hota hai.

#### 💻 Hands-On Step-by-Step
1. **Burp Suite kholo** aur target site browse karo (web app mode).
2. **HTTP history** mein jakar kisi bhi request ko dekho.
3. Agar request ka response **HTML** hai, to wo web app hai. Agar response **JSON** array ya object hai, wo API endpoint hai.
4. Ab wahi request **Repeater** mein bhejo, aur `Accept` header ko `application/json` mein badal kar dekho – kabhi kabhi web app bhi JSON de deta hai, matlab woh API bhi expose kar raha hai.

#### ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Successful Exploit:** Tumne kisi web app form ke background mein API call identify kar li, aur direct API mein vulnerability find kar li.
- **Failure:** Tum web app ki UI vulnerabilities (XSS, etc.) mein phase rahe, aur API endpoints miss kar diye.

#### ⚖️ Comparison (X vs Y)

| Feature | Web Application | API |
|---------|----------------|-----|
| Interface | Browser UI | Direct HTTP calls |
| Data Format | HTML | JSON, XML |
| Authentication | Session cookies | Tokens (JWT, OAuth) |
| State | Usually stateful (sessions) | Usually stateless |
| Attacker Focus | Input validation, XSS, CSRF | Business logic, BOLA, Mass Assignment |

#### 🚫 Common Mistakes
- Beginners API ko bhi web app ki tarah treat karte hain, aur UI mein hi atke rehte hain.
- Har endpoint ko web app ke through hit karna, direct request modify karna bhoolna.

#### 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Par web app mein bhi toh API calls hoti hain?"** – Haan, lekin woh browser ke through hoti hain, tum unhe intercept kar ke direct API hit kar sakte ho. UI ke andar API chhupi hoti hai.

#### 🌍 Real-World Use Case
Ek bug bounty program mein target tha "example.com". Logo ne web app mein XSS dhundha, lekin ek hunter ne `example.com/api/v1/users` endpoint discover kiya jo bina auth ke saare users ka data leak kar raha tha. **API vs Web app** samajhne se fayda hua.

#### 🎨 Visual Diagram (ASCII Art)
```
Web App (Browser):
[User] -> [Browser] -> [Server]
         (UI ke saath)

API (Direct):
[Attacker] -> [Tool] -> [Server]
         (Bina UI ke, raw data)
```

#### 🛠️ Best Practices (Pro Tips)
- Har web app mein background API calls dhundho – Chrome DevTools ka Network tab kholo, XHR/Fetch requests dekho.
- Burp ke Target site map mein jakar, saare endpoints ko scope mein lao, aur unhe API ya web app classify karo.

#### ❓ FAQ
1. **Q: Web app ka bhi API testing karna hai kya?**  
   A: Haan, web app ke andar jo API calls ho rahi hain, woh bhi test karo.
2. **Q: Sirf JSON hi API hota hai?**  
   A: Nahi, XML, GraphQL, ya koi bhi structured data API ho sakta hai.
3. **Q: Agar API endpoint mil jaye, lekin kuch data na mile?**  
   A: Auth missing ho sakti hai, ya method galat ho sakta hai (GET vs POST).

#### 📝 Ek Line Mein Yaad Rakhne Ko
**API web app ka "backdoor" hai, jahan UI nahi, sirf logic hota hai.**

---

### 0.2 🎯 Title: Attack Surface Samjho – Har endpoint ek darwaza hai

#### 🐣 Samjhane ke liye (Analogy)
Socho ek building hai jiske kitne darwaze hain. Har darwaza (endpoint) alag room mein jaata hai. Kisi darwaze par lock hai (auth), kisi par nahi. Kuch darwaze andar ka raasta dikhate hain (GET), kuch naya saman daalne ke liye hain (POST), kuch purana saman nikalne ke liye (DELETE). Attack surface in sab darwazon ka collection hai jinme se tum andar ghus sakte ho.

#### 📖 Technical Definition
Attack surface ek API ke saare **endpoints**, unke **HTTP methods**, **parameters**, **headers**, aur **data formats** ka set hota hai jo attacker ke liye accessible hai. Ismein woh endpoints bhi shamil hain jo publicly documented nahi hain (shadow APIs).

#### 🧠 Zaroorat Kyun Hai?
Har endpoint ek potential vulnerability hai. Jaise building ke saare darwaze check kiye bina security claim nahi kar sakte, waise API ke saare endpoints test kiye bina uski security pakki nahi hoti.

#### 🔍 Visual - Screen Par Kya Dikhega
Burp Suite mein jab tum site map dekhte ho, to saare URLs list hote hain – `/api/users`, `/api/posts`, `/admin/api/health`, etc. Inhi ko attack surface kehte hain.

#### ⚙️ Under the Hood
API framework (jaise Express, Django REST) mein routes define hote hain. Har route ek function se mapped hota hai. Attack surface discovery ka matlab in routes ki mapping nikalna, chahe wo documented ho ya nahi.

#### 💻 Hands-On Step-by-Step
1. **Kiterunner (kr) tool use karo:**  
   `kr scan http://target.com/api -w api_words.txt`  
   Ye tool common API endpoints ki wordlist se fuzzing karega aur jo bhi exist karta hai wo batayega.
2. **Swagger UI dhundho:**  
   `/swagger`, `/api/docs`, `/v2/api-docs` jaise paths try karo. Agar mil gaya to automatically saare endpoints ka pata chal jayega.
3. **Burp Passive Scan:**  
   Burp ko passive scan mode mein rakho, jab tum web app browse kar rahe ho, wo background mein API endpoints collect karta rahega.
4. **Wayback Machine / Gau:**  
   `gau target.com` se purane archived URLs nikaalo, jinme hidden endpoints ho sakte hain.

#### ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success:** Tumhe koi aisa endpoint mil gaya jo documentation mein nahi tha (shadow API) aur uspar vulnerability hai.
- **Failure:** Sirf documented endpoints tak simit rahe, shadow APIs miss kar diye.

#### ⚖️ Comparison (X vs Y)
| Concept | Documented API | Shadow API |
|---------|----------------|------------|
| Access | Publicly available | Hidden, no docs |
| Security | Usually tested | Often forgotten, more vulnerable |
| Discovery | Easy (Google, docs) | Hard (fuzzing, recon) |

#### 🚫 Common Mistakes
- Sirf Swagger milne par khush ho jana, aur baaki endpoints miss karna.
- Fuzzing nahi karna, sirf manual enumeration karna.

#### 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Bahut saare endpoints mil gaye, sab test kaise karun?"** – Prioritize karo: sensitive data wale endpoints (users, admin) pehle test karo, aur easily guessable endpoints (test, dev) bhi check karo.

#### 🌍 Real-World Use Case
Paytm ke bug bounty mein ek researcher ne `/v1/payments/internal` endpoint fuzz kiya, jo internal use ke liye tha aur bina auth ke access tha. Isse woh kisi bhi user ka balance change kar sakta tha. Shadow API discovery ne bounty dilwaya.

#### 🎨 Visual Diagram (ASCII Art)
```
Target API
  ├── /api/public (documented)
  ├── /api/private (auth required)
  ├── /internal/health (shadow)
  ├── /swagger (documentation)
  └── /backup/api (shadow)
```

#### 🛠️ Best Practices (Pro Tips)
- Wordlist use karo jo specifically API endpoints ke liye bani ho (assetnote, kiterunner ki).
- Directory brute-force ke saath saath, parameter fuzzing bhi karo: `/api/users?uid=1`, `/api/users/1` dono try karo.

#### ❓ FAQ
1. **Q: Attack surface discovery ke liye kaunsa tool best hai?**  
   A: Kiterunner fast hai, Burp Intruder bhi use kar sakte ho, aur Gau passive recon ke liye.
2. **Q: Shadow API kya hota hai?**  
   A: Jo API publicly document nahi hui, lekin accessible hai – jaane-anjaane mein developer ne chhod di.
3. **Q: Agar endpoint mil gaya lekin 403 aata hai?**  
   A: Authentication bypass try karo, ya method change karo (GET to POST), ya headers manipulate karo.

#### 📝 Ek Line Mein Yaad Rakhne Ko
**Har endpoint ek darwaza hai, chahe lock ho ya na ho, check toh karna hi padega.**

---

### 0.3 🎯 Title: Rule #1 – Kabhi bhi server ke response par bharosa mat karo

#### 🐣 Samjhane ke liye (Analogy)
Maano tumne kisi se udhaar manga aur usne kaha "Mere paas paisa nahi hai". Tumne maan liya. Lekin uski jeb mein 500 rupaye the. Tumne bharosa kar liya, galat kiya. Waise hi, server "Error" dikha raha hai, lekin ho sakta hai andar operation ho gaya ho. Kabhi bhi sirf response dekh kar mat maano ki kaam hua ya nahi.

#### 📖 Technical Definition
Rule #1: **Never trust the server's response blindly.** Sirf HTTP status code ya response message ko final proof mat samjho. Hamesha real-world impact check karo. Jaise 200 OK aaya, to automatic success nahi; 403 Forbidden aaya, to automatic failure nahi. Ho sakta hai server ne 403 dikhaya, lekin database mein changes ho gaye.

#### 🧠 Zaroorat Kyun Hai?
API testing mein hum server ko confuse kar rahe hote hain. Kabhi kabhi server error message dekar bhi request process kar deta hai (race conditions, logic flaws). Agar hum response par bharosa kar lenge, to vulnerability miss ho jayegi.

#### 🔍 Visual - Screen Par Kya Dikhega
Burp Repeater mein request bheji, response aaya "403 Forbidden". Par agar tum database check karoge (agar access ho), ya kisi aur user se confirm karoge, to pata chalega ki record delete ho gaya. Response ne jhooth bola.

#### ⚙️ Under the Hood
Server-side validation mein kabhi kabhi "fail-open" condition hoti hai. Jaise, authorization fail hone par bhi database operation commit ho jata hai, lekin server 403 return kar deta hai. Ya error handling theek nahi hai, to operation to ho jata hai lekin response galat aata hai.

#### 💻 Hands-On Step-by-Step
1. Kisi bhi endpoint par request bhejo jisme tum authorization bypass kar rahe ho (e.g., IDOR attempt).
2. Response check karo – 403 aaya.
3. Ab tum kisi aur tarah se verify karo ki operation hua ya nahi. Jaise kisi aur user se pucho ki uski profile delete hui ya nahi, ya kisi aur endpoint se data check karo.
4. Agar operation ho gaya, to vulnerability hai, chahe response kuch bhi ho.

#### ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Successful Exploit:** Response 403 aaya, lekin data delete ho gaya – vulnerability found.
- **Failure:** Tumne 403 dekh kar assume kar liya ki "kuch nahi hua" aur aage badh gaye – vulnerability miss.

#### ⚖️ Comparison (X vs Y)
| Situation | Response | Actual Impact | Conclusion |
|-----------|----------|---------------|------------|
| Normal | 200 OK | Data changed | Expected |
| Vulnerable | 403 Forbidden | Data changed | Vulnerability |
| Vulnerable | 200 OK | Data unchanged? | Maybe false positive? |
| Secure | 403 Forbidden | Data unchanged | Secure |

#### 🚫 Common Mistakes
- Beginners 200 OK dekh kar happy ho jate hain, aur 403 dekh kar ignore kar dete hain.
- Response body mein "error" ya "success" flags par bharosa karna.

#### 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Par agar response 403 aaya to kaise pata chale ki operation hua?"** – Indirect methods use karo: jaise user activity logs, duplicate requests se trigger, ya kisi aur API se verify.

#### 🌍 Real-World Use Case
Ek pentest mein, tester ne password change API mein CSRF token bypass kiya. Request bheji, response 403 aaya. Lekin user ke password actually change ho gaye. Server ne 403 dekar attacker ko confuse kiya, lekin impact tha.

#### 🛠️ Best Practices (Pro Tips)
- Response ke saath-saath, second-order effects check karo. Jaise profile update API 200 de rahi hai, lekin profile view API mein changes nazar aa rahe hain? Toh kaam hua.
- Race conditions mein to ye rule aur bhi important hai.

#### ❓ FAQ
1. **Q: Har response ko kaise verify karun?**  
   A: Jitna ho sake, out-of-band ya parallel checks karo. Jaise email trigger ho raha hai? Database entry ban rahi hai?
2. **Q: Agar verify karne ka koi tarika na ho?**  
   A: Toh bhi response ko grain of salt ke saath lo. Multiple requests bhej kar pattern dekho.

#### 📝 Ek Line Mein Yaad Rakhne Ko
**Server jhooth bol sakta hai, uski baaton mein mat aao – asliyat check karo.**

---

### 0.4 🎯 Title: Rule #2 – API Testing = Logic Testing

#### 🐣 Samjhane ke liye (Analogy)
Ek ghar mein chor ghusna chahta hai. Web app testing hai ki darwaza kitna majboot hai, lock kaise todna hai. API testing hai ki ghar ka layout kaisa hai, kaunsa darwaza kitchen mein jaata hai, kaunsa bedroom mein, aur kitchen ke darwaze se bedroom mein kaise pahunch sakte ho. **Logic testing** matlab flows ko todna, ordering mein gadbadi karna, parameters ki mapping galat karna.

#### 📖 Technical Definition
API testing asal mein **business logic testing** hai. Iska matlab hai ki API ke intended functionality ko examine karo, aur dekho ki usko kahan tod sakte ho – jaise kisi ko do baar refund kar dena, kisi aur ka order cancel kar dena, discount ek se zyada baar apply kar dena.

#### 🧠 Zaroorat Kyun Hai?
Technical vulnerabilities (SQLi, XSS) toh automated tools bhi dhundh lete hain. Lekin business logic flaws sirf humans dhundh sakte hain. Inhi flaws se sabse bada impact hota hai (financial loss, data breach).

#### 🔍 Visual - Screen Par Kya Dikhega
Burp mein ek request sequence capture karo:  
1. User login -> Add to cart -> Apply coupon -> Checkout -> Payment -> Order confirmation.  
Ab tum dekho ki kya tum coupon apply karne ke baad cart mein items add kar sakte ho, jisse coupon un items par bhi apply ho jaye (logic flaw).

#### ⚙️ Under the Hood
Har API call ek state change karta hai. Backend mein ek process flow hota hai. Logic flaw tab aata hai jab ye flow expected order mein nahi hota, ya steps skip ho sakte hain, ya conditions properly check nahi hoti.

#### 💻 Hands-On Step-by-Step
1. **Functional flow samjho:** Pehle application ko normally use karo, har step ka request note karo.
2. **Sequence break karo:** Kisi step ko skip kar ke agla step try karo. Jaise payment ke bina order confirm kar do.
3. **Parameters manipulate karo:** Kisi step mein jo parameter auto-calculated hai (jaise total price), usko modify kar ke bhejo.
4. **Race condition try karo:** Ek hi resource par do parallel requests bhejo, jaise ek hi coupon do baar apply kar do.

#### ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success:** Tumne kisi step ko bypass kar ke directly confirmation generate kar li, ya ek se zyada baar discount le liya.
- **Failure:** Tumne har step properly follow kiya, koi flaw nahi mila.

#### ⚖️ Comparison (X vs Y)
| Flaw Type | Example | Impact |
|-----------|---------|--------|
| Technical | SQLi in id parameter | Data leak |
| Logic | Order after payment bypass | Free product |

#### 🚫 Common Mistakes
- Sirf OWASP Top 10 technical flaws par focus karna, business logic ko ignore karna.
- Application ko normal user ki tarah use karna, na ki hacker ki tarah.

#### 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Business logic samajhna mushkil hai, kaise pata chale ki kya todna hai?"** – Developers ki tarah socho. Agar tum developer hote to kaise implement karte? Us implementation mein loopholes dhundho.

#### 🌍 Real-World Use Case
Uber mein ek flaw tha: Ride complete hone ke baad fare calculate hota tha. Tester ne ride cancel kar di, lekin fare calculate ho gaya, aur usse refund mil gaya. Phir usne same ride ko complete kiya, aur doosra fare calculate hua. Logic flaw tha ki cancellation ke baad fare state reset nahi hua.

#### 🛠️ Best Practices (Pro Tips)
- **Mind map banao:** Har feature ke steps ka diagram banao, aur har step par "what if" socho.
- **Turbo Intruder use karo** race conditions ke liye.
- **Multi-step workflows** ko ek saath test karo, alag-alag nahi.

#### ❓ FAQ
1. **Q: Logic testing ke liye koi tool hai?**  
   A: Tool nahi, dimaag chahiye. Burp bas requests capture karta hai, logic tumhe sochna hai.
2. **Q: Kaise pata chale ki koi logic flaw hai?**  
   A: Jab tum socho ki "aisa nahi hona chahiye" aur woh ho jaye.
3. **Q: Sabse common logic flaw?**  
   A: Race conditions aur parameter manipulation.

#### 📝 Ek Line Mein Yaad Rakhne Ko
**API todna hai toh uska logic samjho, technical flaws toh side mein hain.**

---

## 🔥 Module 0 Summary: API Hacking Mindset in 4 Points
1. **API vs Web App:** UI ke piche chhupi API dhundho.
2. **Attack Surface:** Har endpoint, har method scan karo.
3. **Rule #1:** Server ke response ko kabhi trust mat karo.
4. **Rule #2:** Technical se zyada logic flaws par dhyan do.

Yeh mindset lekar aage badho, ab Modules 1 se 8 mein asli maza ayega. Agla module chahiye toh batao! 🚀

========================================================================================

## 🔍 Module 1: Reconnaissance & Advanced Discovery
*Target ki "Jaikaashi" karna. Jitna jaayega jaanoge, utna deep jaayega exploit.*

**Welcome Mentor ji!** Ab hum shuru karte hain API hacking ka pehla aur sabse important phase – **Reconnaissance**. Is module ko padhne ke baad, aap kisi bhi target ki "naak, nose, brain" sab pata kar sakoge bina trigger kiye ya directly map karke.

---

### Topic 1.1: Passive Recon (Bina Touch Kiye)
*Jaise chor ghar mein ghusne se pehle bahar se hi windows count karta hai, kaunsi light on hai, kaunsi off – waise hi hum bina kisi request bheje target ke baare mein jaankari ikattha karte hain.*

#### 🐣 Samjhane ke liye (Analogy)
Maano tum kisi ladki ko impress karna chahte ho. Pehle tum uske Facebook, Instagram, LinkedIn dekhte ho bina usse message kiye. Dekhte ho ki uski photo kahan ki hai, kya pasand hai, kahan job karti hai. Ye sab **Passive Recon** hai. Tumne usse touch nahi kiya, lekin uske baare mein bahut kuch jaan liya.

#### 📖 Technical Definition
Passive Reconnaissance ka matlab hai target ke saath **direct interaction kiye bina** (bina kisi HTTP request bheje) maximum information collect karna. Ismein hum OSINT (Open Source Intelligence) tools aur techniques use karte hain.

#### 🧠 Zaroorat Kyun Hai?
- **Stealth:** Target ko pata nahi chalega ki hum test kar rahe hain. Isliye bug bounty mein passive recon pehle karte hain, taaki WAF block na kare.
- **Surface Mapping:** JS files, third-party services, tech stack se hume endpoints ka andaaza ho jata hai ki kahan active recon karna hai.

#### 🔍 Visual - Screen Par Kya Dikhega
- **Wappalyzer:** Browser extension install karo. Kisi bhi website par jao, extension icon click karo – ek popup aayega jisme likha hoga: "Framework: React", "Web Server: Nginx", "Database: MongoDB". (Reference: **Page 12**)
- **BuiltWith:** `builtwith.com` par target domain daalo – ek detailed report milega, jismein hosting provider, analytics tools, CDN sab kuch.
- **Browser DevTools:** Right-click -> Inspect -> Sources tab. Yahan saari JS files list hongi. Koi file kholo, usmein `/api`, `api-key` search karo.

#### ⚙️ Under the Hood
- **Wappalyzer/BuiltWith:** Ye tools target ke HTTP response headers (jaise `Server`, `X-Powered-By`) aur HTML content mein specific patterns dhundhte hain. Jaise agar `wp-content` dikha to WordPress samajhte hain.
- **JS Mining:** Jab browser JS file download karta hai, toh us file ke andar strings hote hain. Developers kabhi kabhi endpoints ya keys comments mein daal dete hain. Minified code (without spaces) ko beautify karne se readable ho jata hai.

#### 💻 Hands-On Step-by-Step
**Step 1: Tech Stack Detection (Wappalyzer)**
1. Chrome ya Firefox mein **Wappalyzer** extension add karo.
2. Target site kholo, jaise `https://target.com`.
3. Extension icon click karo – list dekho:
   - **JavaScript Frameworks:** React, Vue, Angular (matlab Single Page Application, API calls zyada hongi).
   - **Web Servers:** Nginx, Apache.
   - **Databases:** MySQL, MongoDB (MongoDB hai toh NoSQLi try karna).
4. **BuiltWith** par bhi domain daal kar confirm karo.

**Step 2: Source Code Analysis (JS Mining) – (Reference: Page 6)**
1. Target site par right-click -> **Inspect** ya `Ctrl+Shift+I`.
2. **Sources (Debugger)** tab par jao.
3. Left sidebar mein saari `.js` files dikhengi. Har file par click karo.
4. Agar code minified hai (ek line mein sab kuch), toh us code ko copy karo aur **"JavaScript JS Formatter"** (jaune `beautifier.io`) mein paste karo.
5. Ab beautified code mein `Ctrl+F` karke dhoondo:
   - `/api` – kya koi endpoint dikh raha hai?
   - `swagger` – `/swagger-ui.html` mil sakta hai?
   - `graphql` – introspection endpoint ka clue?
   - `key`, `secret`, `token` – hardcoded credentials?
6. **Pro Tip:** Manual search ke alawa, **LinkFinder** tool use karo:
   - Install: `pip install linkfinder`
   - Command: `python linkfinder.py -i https://target.com -o cli`
   - Ye automatically saari JS files se endpoints nikal dega.

#### ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success:** Aapko koi aisa endpoint mila jo documentation mein nahi tha, jaise `/internal/api/v3/users`. Ya koi hardcoded API key mili.
- **Failure:** Sirf homepage dekha, JS files ignore kar di, koi valuable info nahi mili.

#### ⚖️ Comparison (X vs Y)
| Technique | Wappalyzer | JS Mining |
|-----------|------------|-----------|
| Input | URL | JS files |
| Output | Tech stack (server, framework) | Hidden endpoints, keys |
| Difficulty | Easy | Moderate |
| Automation | Extension | Tools (LinkFinder) |

#### 🚫 Common Mistakes
- Sirf Wappalyzer par bharosa karke active recon shuru kar dena, JS files na dekhna.
- Minified code ko bypass karna, "yeh toh padhte nahi" kehkar.
- Hardcoded keys ko ignore karna, "demo key hoga" samajhna.

#### 🤔 Agar Dimag Ghoom Rahe Hai?
- **"JS files mein endpoints mil gaye, lekin wo sahi hain kaise pata chalega?"** – Kuch endpoints relative hote hain (`/api/user`), kuch absolute (`https://api.target.com`). Unhe Burp ya browser console mein hit kar ke dekho. 401 aaya toh auth chahiye, 200 aaya toh open hai.
- **"BuiltWith aur Wappalyzer alag kyun dikha rahe?"** – BuiltWith deep DNS records aur third-party services bhi scan karta hai, Wappalyzer sirf frontend response se kaam karta hai.

#### 🌍 Real-World Use Case
Ek bug bounty hunter ne `target.com` ki JS files mein `window.API_KEY = "AIzaSy..."` dekha. Ye Google API key tha. Usne woh key use karke Google Cloud services access kar li, aur sensitive data leak kar diya. **JS Mining** ne bounty dilwaya.

#### 🛠️ Best Practices (Pro Tips)
- **Burp Suite Passive Scanner** on rakho – jab tum web app browse kar rahe ho, wo background mein JS files scan karega aur endpoints collect karega.
- **JS files ke saath saath, source maps (.map)** bhi dekho. Kabhi kabhi original source code mil jata hai.
- **Wayback Machine** (archive.org) par target dhundho – purani JS files mein zyada secrets hote hain.

#### ❓ FAQ
1. **Q: Wappalyzer se pata chala ki site React par bani hai. Isse kya fayda?**  
   A: React SPAs mein API calls frontend se hoti hain, isliye JS files mein endpoints milne ke chances zyada hain.
2. **Q: JS files mein API key mili, lekin wo invalid hai?**  
   A: Kabhi kabhi wo staging environment ki key hoti hai. Phir bhi usse production mein try karo, kuch na kuch milta hai.
3. **Q: BuiltWith ke liye paise dene padte hain?**  
   A: Free version kaafi hai basic recon ke liye.

#### 📝 Ek Line Mein Yaad Rakhne Ko
**Passive recon mein target ko touch mat karo, uski JS files aur tech stack se sab pata karo.**

---

### Topic 1.2: Active Recon (Mapping the Territory)
*Ab hum darwaza khatkhatayenge, lekin dheere se, taaki pata chal jaye ki andar kaun hai.*

#### 🐣 Samjhane ke liye (Analogy)
Passive recon ke baad, tum ladki ke baare mein thoda jaante ho. Ab tum uski friend list dekhte ho, uske photos par likes count karte ho, lekin abhi tak message nahi kiya. **Active recon** hai usse ek "Hi" bhejna aur dekna ki wo reply karti hai ya nahi, kaise karti hai. Yahan hum target server ko directly request bhejte hain.

#### 📖 Technical Definition
Active Recon mein hum target API endpoints par **legitimate ya malformed requests bhej kar** unke response analyze karte hain. Isse hume pata chalta hai ki kaunse endpoints exist karte hain, kaunse parameters accepted hain, aur authentication kaise kaam karta hai.

#### 🧠 Zaroorat Kyun Hai?
- **Discovery:** Passive recon mein jo endpoints nahi mile, wo active fuzzing se mil jayenge.
- **Validation:** Jo endpoints mile, wo actually exist karte hain ya nahi, ye confirm hota hai.
- **Behavior Analysis:** API ka behavior kaise change hota hai different inputs se, ye pata chalta hai.

#### 🔍 Visual - Screen Par Kya Dikhega
- **Kiterunner Terminal:** `kr scan http://target.com/api -w api_words.txt` chalane par terminal mein responses flood honge. `[200] /api/users`, `[403] /api/admin`, `[404] /api/xyz`.
- **Burp Param Miner:** Extension install karo, kisi endpoint par right-click -> "Guess params". Neche ek tab khulega jisme "Discovered params" dikhenge.

#### ⚙️ Under the Hood
- **Directory Fuzzing:** Tool wordlist ki har entry ko base URL ke saath jod kar request bhejta hai. Response status code dekhta hai. 200/403/500 matlab endpoint exist karta hai, 404 matlab nahi.
- **Kiterunner (kr):** Ye normal fuzzer se alag hai. Ye API routes ko samajhta hai. Jaise `/api/users/:id` format mein ye `:id` ko wildcard maan kar fuzzing karta hai aur common IDs (1,2,3, admin, etc.) try karta hai.
- **Param Miner:** Ye hidden parameters dhundhta hai. Jaise kisi endpoint par `id` parameter accept ho raha hai, toh ye `admin`, `debug`, `test` jaise common hidden params try karega.

#### 💻 Hands-On Step-by-Step
**Step 1: Directory/File Fuzzing (Basic) with ffuf**
1. `ffuf` install karo (ya `gobuster`).
2. Command:  
   `ffuf -u https://target.com/api/FUZZ -w /path/to/api-wordlist.txt -ac`
   - `-ac` auto-calibrate karta hai, 404 responses filter karne ke liye.
3. Wordlist mein `users`, `admin`, `v1`, `swagger`, `graphql`, `health` jaise words hote hain.
4. Output dekho: `[Status: 200] /api/users` matlab mil gaya.

**Step 2: API-Specific Fuzzing (Advanced) with Kiterunner (Reference: Page 6)**
1. Kiterunner download karo (`github.com/assetnote/kiterunner`).
2. Command:  
   `kr scan https://target.com/api -w /path/to/assetnote-api-words`
3. Ye tool pehle routes fuzzing karega, phir common IDs aur parameters try karega.
4. Example output:  
   `[200] GET /api/users/1` – user 1 exist karta hai.  
   `[403] GET /api/admin` – admin endpoint exist karta hai par auth chahiye.

**Step 3: Hidden Parameter Discovery with Arjun**
1. Arjun install karo: `pip install arjun`
2. Command:  
   `arjun -u https://target.com/api/users -m GET`
3. Arjun common parameter wordlist lekar har parameter try karega aur response mein difference dekhega.
4. Output: `{"id": "1", "admin": "true"}` – matlab `admin` hidden parameter accept ho raha hai.

**Step 4: Documentation Mining (Sone ki chidiya)**
1. Burp Suite mein target site browse karo.
2. In URLs manually ya intruder se try karo:
   - `/swagger-ui.html`
   - `/swagger.json`
   - `/v2/api-docs`
   - `/openapi.json`
   - `/redoc`
   - `/graphql?introspection`
3. Agar `200 OK` mila aur JSON/HTML docs dikhe, toh poora API ka map mil gaya.

**Step 5: Improper Assets Management – Shadow APIs**
1. Assume karo ki current version `/v2/` hai. Lekin `/v1.1/`, `/v3-beta/`, `/internal/` bhi ho sakte hain.
2. Fuzzing mein `v1`, `v2`, `v3`, `internal`, `test`, `dev`, `staging` jaise words add karo.
3. Agar `/v1/` par 200 aaya, toh shadow API mil gaya.

**Step 6: Environment Leakage**
1. Kisi request mein `Host` header change karo:  
   Original: `Host: api.target.com`  
   Modified: `Host: dev-api.target.com`
2. Dekho kya response aata hai. Agar data mila, toh environment leakage hai.
3. Ya parameters mein `env=prod` ko `env=dev` karo.

#### ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success:** Koi aisa endpoint mila jo documentation mein nahi tha, aur wo sensitive data leak kar raha hai.
- **Failure:** Sirf documented endpoints mile, koi hidden ya shadow API nahi mila.

#### ⚖️ Comparison (X vs Y)
| Tool | Use Case | Advantage |
|------|----------|-----------|
| ffuf | Directory/File fuzzing | Fast, flexible |
| Kiterunner | API route fuzzing | Context-aware, API-specific |
| Arjun | Parameter discovery | Finds hidden params |
| Param Miner | Burp extension | Integrates with Burp |

#### 🚫 Common Mistakes
- Sirf `200 OK` ko success samajhna, `403` ko ignore karna. `403` matlab endpoint exist karta hai, lekin auth hai – baad mein bypass try karo.
- Fuzzing mein default wordlists use karna (jaise directory-list-2.3-medium) – ye API ke liye ineffective hain. API-specific wordlists use karo (assetnote, kiterunner ki).
- Swagger milne par happy ho jana aur aage fuzzing nahi karna.

#### 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Fuzzing se bahut saare 403 mile, unka kya karun?"** – Un endpoints ko note karo. Baad mein authentication bypass techniques lagao (JWT manipulation, header injection).
- **"Shadow API mila, lekin data nahi mil raha?"** – Method change karo (GET to POST), headers add karo, ya authentication tokens try karo.

#### 🌍 Real-World Use Case
Ek researcher ne `api.instagram.com` par Kiterunner chalaya. Use `/api/v1/feed/internal` mila, jo shadow API tha. Usne request bheji toh saare users ki private posts leak ho rahi thi. **API-specific fuzzing** ne $10,000 ka bounty dilwaya.

#### 🛠️ Best Practices (Pro Tips)
- **Rate limiting** ka dhyan rakho. Fuzzing mein `-t` (threads) kam rakho (5-10) taaki block na ho.
- **Wordlists:** Assetnote ki API wordlist best hai. Github se download karo.
- **Burp Intruder** mein `sniper` attack use karo clusterbomb se pehle, taahi basic fuzzing karo.

#### ❓ FAQ
1. **Q: Kiterunner aur ffuf mein kya difference hai?**  
   A: ffuf general purpose fuzzer hai, Kiterunner specifically API routes ke liye design hua hai aur common ID fuzzing bhi karta hai.
2. **Q: Shadow API ka pata chal gaya, lekin authentication bypass kaise karun?**  
   A: Module 2 (Auth) mein padhenge.
3. **Q: Swagger UI mil gaya, lekin wo blank hai?**  
   A: Kabhi kabhi Swagger JSON alag endpoint par hota hai (`/swagger.json`). Use dhundho.

#### 📝 Ek Line Mein Yaad Rakhne Ko
**Active recon mein tools se fuzzing karo, hidden endpoints aur parameters dhundho, aur Swagger mila toh lottery lag gaya.**

---

### Topic 1.3: Version Control & Leak Search
*Developer ki galtiyan – kabhi kabhi code ke saath keys bhi commit ho jati hain.*

#### 🐣 Samjhane ke liye (Analogy)
Tumhari girlfriend ne tumhe apni diary padhne di. Usme usne likha tha ki "Mera password meri birthday hai". Diwali par usne woh page phaad kar phenk diya, lekin nishaan reh gaya. Waise hi, developers kabhi kabhi code ke saath sensitive info commit kar dete hain, aur baad mein delete bhi kar dete hain, lekin Git history mein reh jata hai.

#### 📖 Technical Definition
Version control systems (Git) par kabhi kabhi accidentally API keys, tokens, credentials commit ho jate hain. Public repositories (GitHub, GitLab) mein ye dhundhna possible hai. Mobile apps decompile karne par bhi hardcoded keys milti hain.

#### 🧠 Zaroorat Kyun Hai?
- **Direct Access:** API key mil gayi toh authentication bypass kar sakte ho.
- **Internal Docs:** Kabhi kabhi internal endpoints aur architecture details mil jate hain.

#### 🔍 Visual - Screen Par Kya Dikhega
- **GitHub Search:** `"target.com" API key` search karo. Result mein kisi file mein `API_KEY=12345` dikhega.
- **Mobile Decompilation:** `jadx-gui` mein APK kholi, `strings.xml` mein `api_endpoint` dikha.

#### ⚙️ Under the Hood
- **GitHub Dorking:** GitHub ka search engine specific keywords dhundh sakta hai. Jaise `org:target "api_key"` se target organization ke andar search hota hai.
- **APK Decompilation:** APK ek compressed file hai. Jadx use kar ke usse Java source code mein convert kiya ja sakta hai. Strings.xml mein app ke saari strings hoti hain, jahan API keys store ho sakti hain.

#### 💻 Hands-On Step-by-Step
**Step 1: GitHub Dorks**
1. GitHub.com par jao.
2. Ye queries try karo:
   - `"target.com" api_key`
   - `"target.com" secret`
   - `"target.com" token`
   - `"target.com" password`
   - `filename:.env "target.com"` (environment files)
   - `extension:pem "target.com"` (private keys)
3. Results mein agar koi file mili jisme key hai, to copy karo.

**Step 2: GitLeaks Tool**
1. Gitleaks install karo: `brew install gitleaks` (Mac) ya binary download.
2. Command:  
   `gitleaks detect --source /path/to/repo --report output.json`
3. Ye tool automatically sensitive info scan karega.

**Step 3: Mobile App Decompilation**
1. APK download karo (apkpure, apkmirror se).
2. `jadx-gui` install karo, APK kholo.
3. Resources -> `strings.xml` open karo.
4. `Ctrl+F` karo `api`, `key`, `secret`.
5. Source code mein bhi dekho, kabhi kabhi endpoints hardcoded hote hain.

#### ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success:** Valid API key mil gayi, jisse API access mila.
- **Failure:** Koi key nahi mili, ya jo mili wo expired/invalid thi.

#### 🚫 Common Mistakes
- Sirf GitHub search karna, GitLab, Bitbucket ignore karna.
- Mobile app decompile karke strings.xml dekhna, source code na dekhna.
- Mili key ko immediately use karna bina validate kiye.

#### 🤔 Agar Dimag Ghoom Rahe Hai?
- **"API key mil gayi, lekin wo revoke ho sakti hai?"** – Haan, lekin jab tak revoke na ho, tab tak access hai. Turant use karo.
- **"GitHub par target ka official repo nahi mil raha?"** – Forked repos mein bhi original keys ho sakti hain.

#### 🌍 Real-World Use Case
Uber ki ek private GitHub repository mein ek employee ne AWS keys commit kar di. Kisi hacker ne dorking se wo keys dhundh li aur Uber ke AWS servers par access kar liya. Data breach hua.

#### 🛠️ Best Practices (Pro Tips)
- GitHub search ke saath **filters** use karo: `language:javascript` ya `path:config` taaki relevant files milein.
- Mobile apps ke alawa, **iOS IPA files** bhi decompile karo (similar process).
- **Shodan** par bhi API keys search karo – kabhi kabhi logs mein keys expose hoti hain.

#### ❓ FAQ
1. **Q: GitHub dorking legal hai?**  
   A: Public repos search karna legal hai. Lekin mili keys ka unauthorized use illegal ho sakta hai. Bug bounty mein report karo, use nahi.
2. **Q: APK decompile karne ke liye kaunsa tool best hai?**  
   A: Jadx (GUI) best hai, ya apktool + dex2jar.
3. **Q: Mili key ko test kaise karun?**  
   A: Us key ke saath API request bhejo. Agar 200 aaya toh valid hai.

#### 📝 Ek Line Mein Yaad Rakhne Ko
**Developer ki galti teri bounty hai – GitHub aur mobile apps mein secrets dhundho.**

---

## 🔥 Module 1 Summary: Recon & Discovery Checklist
1. **Passive:** Wappalyzer, BuiltWith se tech stack. JS files mein endpoints/keys.
2. **Active:** Kiterunner/ffuf se fuzzing, Arjun se hidden params, Swagger docs.
3. **Shadow APIs:** Version fuzzing, Host header change.
4. **Leaks:** GitHub dorks, APK decompilation.

Agla module chahiye toh batao – **Module 2: Authentication Bypass Techniques**? 🚀

========================================================================================

## 🔐 Module 2: Authentication & Session Management Deep-Dive
*Andar ka raasta (gateway) kitna strong hai?*

**Swagat hai Mentor ji!** Module 2 mein hum API ke **gateway** ko todna seekhenge – yani **Authentication**. Agar aap API ko ek private building maano, to authentication us building ka **security guard** hai. Agar hum guard ko bypass kar lete hain, ya uski uniform pehen lete hain, to andar ghusna aasaan ho jata hai. Is module mein hum response manipulation, JWT attacks, OAuth flaws, rate limiting bypass, aur bhi bahut kuch cover karenge. Chaliye shuru karte hain!

---

### Topic 2.1: 🎯 Title: Response Manipulation (Login Bypass)
*Server jhooth bole to frontend maan jaaye?*

#### 🐣 Samjhane ke liye (Analogy)
Socho tum school mein ho aur tumhe Principal se milna hai. Guard ne kaha "Principal sahab nahi milenge". Tumne Principal ka phone milaya, unhone kaha "Aajao beta". Ab tum guard ko jhooth bolte ho ki "Principal ne bulaya hai" aur guard maan jaata hai bina verify kiye. Yahan **guard = frontend (browser)**, **Principal ka phone = server response**.

#### 📖 Technical Definition
Response Manipulation tab hota hai jab frontend application server ke HTTP response par **blindly trust** karti hai, bina response body ko properly parse kiye. Agar frontend sirf **status code** (200 OK, 403 Forbidden) check karta hai na ki actual response body mein success flag, to attacker server se aaya 403 Forbidden ko intercept karke 200 OK mein badal kar frontend ko fool kar sakta hai.

#### 🧠 Zaroorat Kyun Hai?
Ye vulnerability **authentication bypass** ka ek simple lekin powerful tarika hai. Isse aap bina valid credentials ke kisi bhi user ke account mein login kar sakte ho, agar frontend silly hai.

#### 🔍 Visual - Screen Par Kya Dikhega
Burp Suite mein:
1. Request intercept karo login ki.
2. Server se response aata hai:  
   **Failed login:** `HTTP/1.1 403 Forbidden` with body `{"error":"Invalid credentials"}`  
   **Successful login:** `HTTP/1.1 200 OK` with body `{"token":"xyz","success":true}`
3. Tum response ko modify karoge: Failed login ka status code 200 OK kar doge, ya body mein success flag true kar doge.

#### ⚙️ Under the Hood
Frontend developers kabhi kabhi lazy programming karte hain. Jaise:
```javascript
fetch('/api/login', { /* credentials */ })
  .then(response => {
    if (response.status === 200) {
      // Login successful, redirect
      window.location = '/dashboard';
    } else {
      showError('Invalid credentials');
    }
  })
```
Is code mein sirf **status code** check ho raha hai. Response body nahi dekhi ja rahi. Isliye agar hum 403 ko 200 mein badal denge, to frontend samjhega ki login successful ho gaya.

#### 💻 Hands-On Step-by-Step (Reference: Page 1-4)
**Phase 1: Observation – Kya frontend sirf status code dekhta hai?**
1. Burp Suite open karo aur intercept ON karo.
2. Target website par correct credentials (e.g., `admin:admin`) daal kar login karo.
3. Burp mein request aayegi, usse forward karo.
4. Response aayega – maan lo `200 OK` with token.
5. Ab is response ko forward karne se pehle, status line change karo:
   - Original: `HTTP/1.1 200 OK`
   - Modified: `HTTP/1.1 403 Forbidden`
   - Response body mein token waisa hi rahne do.
6. Forward karo aur browser dekho.
7. **Observation:** Agar browser "Login Successful" dikhata hai (ya dashboard par le jata hai) 403 ke baad bhi, to frontend **sirf status code nahi** dekh raha, wo response body bhi dekh raha hai (success flag).  
   Agar browser "Unauthorized" error dikhata hai, to frontend **sirf status code** dekh raha hai.

**Phase 2: Exploit – Login Bypass**
1. Ab wrong credentials daalo (e.g., `admin:wrongpass`).
2. Burp mein response aayega `403 Forbidden` with body `{"error":"Invalid"}`.
3. Status line modify karo: `HTTP/1.1 200 OK`.
4. Agar body mein success flag hai (`"success":false`), to use bhi `"success":true` kar do.
5. Forward karo.
6. **Success:** Agar browser dashboard dikhata hai, to vulnerability confirmed! Tum bina correct password ke login kar gaye.

#### ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Successful Exploit:** Wrong credentials dene par bhi 200 OK modify karne se dashboard khul gaya.
- **Failure:** Wrong credentials par 200 OK modify karne se bhi error aaya – matlab frontend response body bhi check kar raha hai.

#### ⚖️ Comparison (X vs Y)
| Scenario | Response Status | Response Body | Frontend Behavior |
|----------|----------------|---------------|-------------------|
| Normal | 200 OK | `{"success":true}` | Login success |
| Vulnerable | 403 Forbidden (modified to 200) | `{"success":false}` (unchanged) | Login success (sirf status dekha) |
| Secure | 403 Forbidden (modified to 200) | `{"success":false}` | Login failed (body check kiya) |

#### 🚫 Common Mistakes
- Sirf status code badalna, body mein success flag nahi badalna, jabki frontend dono check kar raha ho.
- Response manipulation ke baad verify nahi karna ki actually login hua ya nahi.

#### 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Response body mein success flag bhi badal diya, lekin login nahi hua?"** – Ho sakta hai frontend token bhi validate kar raha ho. Agar token invalid hai, to login nahi hoga. Isliye correct credentials ka token copy karke use karo.
- **"Ye vulnerability kitni common hai?"** – Purani websites mein common thi, abhi bhi kuch mobile apps mein mil jati hai.

#### 🌍 Real-World Use Case
Ek banking app mein, researchers ne dekha ki OTP verification sirf status code check kar raha tha. Unhone wrong OTP daala, response intercept kiya, 403 ko 200 mein badala, aur OTP bypass kar diya. **Critical vulnerability** thi.

#### 🎨 Visual Diagram (ASCII Art)
```
[User] -> [Frontend] -> [API] (wrong pass)
                         [API] -> 403 Forbidden
[Attacker intercepts] -> changes 403 to 200
[Frontend receives 200] -> "Login successful! Redirecting..."
[Attacker logged in]
```

#### 🛠️ Best Practices (Pro Tips)
- **Verification (Grep-Match Method):** (Reference: Page 4)  
  Agar correct aur wrong credentials ka response body same hai, to Intruder mein "Grep-Match" use karo:
  1. Burp Intruder mein request bhejo.
  2. Positions tab mein parameter ko variable mark karo (e.g., password).
  3. Payloads tab mein passwords list daalo.
  4. Options tab mein **Grep-Match** add karo: `"success":true` ya `"status":1` (jo bhi success flag ho).
  5. Attack start karo. Jo bhi response mein ye flag match karega, wo highlight hoga – matlab valid password mil gaya.
- Response manipulation ke baad, browser ke network tab mein dekho ki actual request response kya aaya.

#### ❓ FAQ
1. **Q: Response manipulation se session token bhi mil sakta hai?**  
   A: Haan, agar correct credentials ka token copy kar ke wrong credentials ke response mein daal do, to direct session mil jayega.
2. **Q: Frontend body check kar raha hai to kya karun?**  
   A: Body mein bhi manipulation karo – `"success":false` ko `"success":true` karo.
3. **Q: Ye vulnerability OWASP mein hai?**  
   A: OWASP API Top 10 mein specific nahi hai, lekin broken authentication ka part hai.

#### 📝 Ek Line Mein Yaad Rakhne Ko
**Agar frontend sirf status code dekhta hai, to 403 ko 200 bana ke andar ghus jao.**

---

### Topic 2.2: 🎯 Title: No-Rate Limit Attacks
*OTP se user ki inbox blast kar do*

#### 🐣 Samjhane ke liye (Analogy)
Tum kisi dukaan par gaye aur wahan ek button hai "Free Gift". Tumne use 100 baar dabaya. Dukaan wale ne rok kyun nahi? Agar wo rokta, to tum ek baar hi dabate. Yahan **Rate Limit** wo rokne ka mechanism hai. Agar nahi hai, to tum 1000 baar OTP bhej kar user ki inbox bhar sakte ho, ya OTP brute-force kar sakte ho.

#### 📖 Technical Definition
Rate limiting ek mechanism hai jo ek specific time frame mein ek user ya IP se hone wali requests ki frequency limit karta hai. Agar API par rate limiting nahi hai, to attacker **brute-force attacks** (OTP/password guessing) ya **DoS (Denial of Service)** kar sakta hai.

#### 🧠 Zaroorat Kyun Hai?
- **OTP Brute-Force:** Agar OTP sirf 4-digit hai aur koi limit nahi, to 9999 attempts mein se koi na koi sahi ho jayega.
- **Account Takeover:** Isse accounts hack ho sakte hain.
- **Inbox Bombing:** User ko hundreds of OTP messages bhej kar irritate kar sakte ho.

#### 🔍 Visual - Screen Par Kya Dikhega
Burp Intruder mein:
1. OTP verification request capture karo.
2. OTP field ko variable mark karo (e.g., `otp=§1234§`).
3. Payloads mein numbers daalo (0000 to 9999).
4. Attack start karo. Har request 200 OK aayega, koi limit nahi.

#### ⚙️ Under the Hood
Server usually:
- IP address ya user ID ke saath ek counter store karta hai.
- Har attempt par counter increment.
- Agar counter > threshold, to block karo.

Agar ye logic missing hai, to unlimited attempts possible.

#### 💻 Hands-On Step-by-Step (Reference: Page 18)
**Exploit 1: OTP Brute-Force**
1. Login ya password reset flow mein OTP daalne wala step dhundho.
2. Burp mein request capture karo, jaise:
   `POST /api/verify-otp`  
   `{"phone":"1234567890","otp":"1234"}`
3. Send to Intruder.
4. OTP parameter ko `§` mein mark karo.
5. Payloads tab mein **Numbers** select karo, from 0000 to 9999, step 1.
6. Attack start karo. Response length dekho – jiska response length algha ho, wo successful OTP ho sakta hai.
7. Ya **Grep-Match** use karo `"success":true`.

**Exploit 2: Inbox Bombing (DoS)**
1. OTP send request capture karo, jaise:
   `POST /api/send-otp`  
   `{"email":"victim@example.com"}`
2. Is request ko **Intruder** mein bhejo, ya simple Python script likho.
3. 1000 requests bhejo.
4. Victim ke inbox mein 1000 OTP messages aa jayenge.
5. **Impact:** User ka phone spam se bhar jayega, aur wo temporary block bhi ho sakta hai.

#### ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success:** 1000 requests sab 200 OK aaye, OTP brute-force successful.
- **Failure:** 5-6 requests ke baad 429 Too Many Requests aaya – rate limiting hai.

#### ⚖️ Comparison (X vs Y)
| Attack Type | Method | Impact |
|-------------|--------|--------|
| OTP Brute-Force | Har possible OTP try karna | Account takeover |
| Inbox Bombing | Har second OTP bhejna | User annoyance, SMS costs |
| Password Brute-Force | Common passwords try karna | Account takeover |

#### 🚫 Common Mistakes
- Sirf login attempts check karna, password reset OTP ko ignore karna.
- IP-based rate limiting ko bypass karne ke liye VPN/proxy use nahi karna.

#### 🤔 Agar Dimag Ghoom Rahe Hai?
- **"OTP 6-digit hai to 10 lakh attempts lagenge. Itna time kaise milega?"** – Isliye rate limit ka issue tab critical hota hai jab OTP 4-digit ho (9999 attempts), ya 6-digit ho lekin koi lockout na ho. Phir bhi automated tool se raat bhar chhod do, mil jayega.
- **"Server ne IP block kar diya to?"** – Rotating proxies use karo, ya different headers (`X-Forwarded-For`) se bypass try karo.

#### 🌍 Real-World Use Case
WhatsApp par ek flaw tha ki OTP verification unlimited attempts ki ja sakti thi. Attackers ne iska fayda utha kar accounts hack kiye. Baad mein rate limiting implement ki gayi.

#### 🛠️ Best Practices (Pro Tips)
- **Turbo Intruder** use karo for high-speed attacks.
- Python script mein **proxies** rotate karo:
  ```python
  proxies = {'http': 'http://proxy1.com', 'https': 'https://proxy1.com'}
  requests.post(url, json=data, proxies=proxies)
  ```
- Agar response time mein difference ho, to usse bhi brute-force mein help milti hai.

#### ❓ FAQ
1. **Q: Rate limiting bypass ke aur tarike?**  
   A: IP rotation, headers manipulation (`X-Forwarded-For`), ya multiple accounts use karna.
2. **Q: Kaunsa OTP vulnerable hota hai?**  
   A: Sirf numeric OTP (4-6 digit) brute-force ho sakta hai. Alphanumeric mushkil hai.
3. **Q: Bug bounty mein iska kya severity hai?**  
   A: OTP brute-force se account takeover possible hai to **Critical** ya **High**.

#### 📝 Ek Line Mein Yaad Rakhne Ko
**Jahan limit nahi, wahan brute-force se account tod do.**

---

### Topic 2.3: 🎯 Title: Clickjacking (Session Riding)
*User ko dhokha de kar button daba do*

#### 🐣 Samjhane ke liye (Analogy)
Tum market mein khade ho. Ek banda aaya aur bola "Ye button daba do, free ice cream milega". Tumne daba diya. Pata chala ki wo button tumhare bank ka "Transfer Money" button tha aur tumne apne saare paise transfer kar diye. Yahan **browser = tum**, **hacker ka page = wo banda**, **transparent iframe = chhupa button**.

#### 📖 Technical Definition
Clickjacking (UI redressing) mein attacker ek transparent iframe mein target website ko load karta hai, aur uske upar ek attractive button ya link rakhta hai. User jab attractive button par click karta hai, actually wo target website ke button par click kar deta hai, kyunki wo already logged-in hai. Isse **session riding** bhi kehte hain.

#### 🧠 Zaroorat Kyun Hai?
Isse attacker user ki permission ke bina sensitive actions kara sakta hai – jaise account delete karna, password change karna, money transfer karna.

#### 🔍 Visual - Screen Par Kya Dikhega
Burp Suite mein:
1. Kisi bhi response par right-click karo.
2. **"Check for Clickjacking"** option select karo.
3. Burp ek HTML page generate karega jo target ko iframe mein load karega.
4. Agar page iframe mein load ho jata hai, to vulnerable hai.

#### ⚙️ Under the Hood
Clickjacking se bachne ke liye websites **X-Frame-Options** header use karti hain:
- `X-Frame-Options: DENY` – koi bhi iframe mein load nahi ho sakta.
- `X-Frame-Options: SAMEORIGIN` – sirf same domain ke iframe mein load ho sakta hai.

Agar ye header missing hai, to koi bhi website iframe mein target load kar sakti hai.

#### 💻 Hands-On Step-by-Step (Reference: Page 18-19)
**Phase 1: Testing for Clickjacking**
1. Burp Suite mein kisi bhi sensitive page ki request dhundho (e.g., `GET /delete-account`).
2. Response select karo, right-click -> **"Check for Clickjacking"**.
3. Burp ek HTML file generate karega. Use browser mein open karo.
4. **Observation:** Agar target page iframe mein dikh raha hai, to vulnerable hai.

**Phase 2: Creating a Proof-of-Concept**
1. Ye HTML code likho:
```html
<html>
<head>
  <title>Clickjacking PoC</title>
  <style>
    iframe {
      width: 500px;
      height: 500px;
      position: absolute;
      top: 0;
      left: 0;
      opacity: 0.5; /* Initially transparent rakh sakte ho */
      z-index: 2;
    }
    button {
      position: absolute;
      top: 200px;
      left: 200px;
      z-index: 1;
      font-size: 50px;
    }
  </style>
</head>
<body>
  <button>Click for Free Ice Cream!</button>
  <iframe src="https://target.com/delete-account"></iframe>
</body>
</html>
```
2. Is file ko server par host karo ya locally open karo.
3. User ko ye page bhejo.
4. Jab user button click karega, actually wo iframe ke andar "Delete Account" button par click karega.

#### ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success:** Target page iframe mein load ho raha hai, aur user ko dhokha de kar action karaya ja sakta hai.
- **Failure:** Page iframe mein load nahi hota (blank aata hai) – `X-Frame-Options` present hai.

#### ⚖️ Comparison (X vs Y)
| Header | Behavior | Security |
|--------|----------|----------|
| No header | Kisi bhi site ke iframe mein load ho sakta hai | ❌ Vulnerable |
| `X-Frame-Options: DENY` | Kisi bhi iframe mein load nahi hoga | ✅ Secure |
| `X-Frame-Options: SAMEORIGIN` | Same domain ke iframe mein load hoga | ⚠️ Partial secure |

#### 🚫 Common Mistakes
- Sirf login page check karna, sensitive action pages (delete, transfer) miss karna.
- Ye assume karna ki agar page iframe mein load ho raha hai to exploit possible hai. Actually, user ko click dila pana bhi important hai.

#### 🤔 Agar Dimag Ghoom Rahe Hai?
- **"User ko click kaise dilayenge?"** – Attractive offers, games, ya urgent messages ka sahara lo. Social engineering se.
- **"Opacity 0 kar di to user dekhega nahi iframe, to click kaise karega?"** – Opacity 0 karne se iframe invisible ho jayega, lekin user attractive button par click karega jo uske upar hai. Lekin us attractive button ke click event ko iframe tak forward karna padega – isliye opacity 0.5 rakho taaki debug ho sake, final exploit mein opacity 0 kar do.

#### 🌍 Real-World Use Case
Facebook pe clickjacking attack hua tha jisme users ko "Like" button par click karaya gaya bina unki jaankari ke. Isse pages ki likes artificially badh gayi.

#### 🛠️ Best Practices (Pro Tips)
- **Double-check:** Agar `X-Frame-Options` missing hai, to bhi kuch modern browsers `frame-ancestors` CSP header use karte hain. Use bhi check karo:
  `Content-Security-Policy: frame-ancestors 'none';`
- Bug bounty mein report karte waqt, PoC mein iframe ko visible rakh sakte ho taaki triage team samajh sake.

#### ❓ FAQ
1. **Q: Clickjacking se session hijack ho sakta hai?**  
   A: Nahi, session hijack nahi hota, but user ke session ka fayda utha kar actions karaye ja sakte hain.
2. **Q: Iska OWASP Top 10 mein kya number hai?**  
   A: OWASP API Top 10 mein specifically nahi hai, but ye client-side attack hai.
3. **Q: Mobile apps mein clickjacking possible hai?**  
   A: Mobile apps mein WebViews mein ho sakta hai, agar settings sahi nahi hain.

#### 📝 Ek Line Mein Yaad Rakhne Ko
**Agar iframe mein load ho raha hai, to user ko dhokha de kar kuch bhi karwa lo.**

---

### Topic 2.4: 🎯 Title: JWT Attacks – The JSON Web Token Manipulation
*Apna khud ka token bana lo*

#### 🐣 Samjhane ke liye (Analogy)
Socho tumhe concert mein jaana hai. Ticket counter par tumhe ek paper ticket milta hai jisme likha hai "VIP Access". Tum ticket lekar andar ghus jaate ho. Ab agar tum ticket ke paper par "VIP" ko erase kar ke "Backstage" likh do, aur guard wahi ticket check kare bina signature verify kiye, to tum backstage mein ghus jaoge. Yahan **ticket = JWT**, **signature = server ka secret**.

#### 📖 Technical Definition
JWT (JSON Web Token) ek stateless authentication mechanism hai. Ye teen parts mein banta hai: `header.payload.signature`. Header aur payload base64 encoded hote hain, aur signature server ke secret se sign hota hai. Agar server signature properly verify nahi karta, to attacker payload modify kar ke apna role change kar sakta hai.

#### 🧠 Zaroorat Kyun Hai?
JWT attacks se aap **privilege escalation** kar sakte ho – normal user se admin ban sakte ho, ya kisi aur user ban sakte ho. Ye API hacking mein sabse common aur critical vulnerabilities hain.

#### 🔍 Visual - Screen Par Kya Dikhega
JWT kuch aisa dikhta hai:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4iLCJyb2xlIjoidXNlciJ9.4x1jU8JkL9KxJkL9KxJkL9K
```
Dots se separated teen parts.

#### ⚙️ Under the Hood
JWT verification mein teen steps:
1. Header se algorithm pata karo (`alg`).
2. Signature verify karo using secret.
3. Payload mein se user info lo.

Agar koi step galat hai, to attack possible hai.

#### 💻 Hands-On Step-by-Step
**Attack 1: None Algorithm Attack**
1. Token capture karo.
2. Header mein `"alg":"HS256"` ko `"alg":"none"` karo.
3. Signature part hata do (empty rakho).
4. Payload modify karo (e.g., `"role":"admin"`).
5. New token banao: `eyJhbGciOiJub25lIn0.eyJyb2xlIjoiYWRtaW4ifQ.`
6. Request mein token replace karo.
7. **Success:** Agar server `alg:none` accept karta hai to admin access mil jayega.

**Attack 2: Algorithm Confusion (RS256 to HS256)**
1. Agar server RS256 use kar raha hai (asymmetric), to public key mil sakti hai (e.g., from `/jwks.json`).
2. Public key ko HS256 (symmetric) ke liye secret ki tarah use karo.
3. New token banao with HS256 and public key as secret.
4. Server verify karega to public key se hi hoga, aur accept kar lega.
5. Tool: `jwt_tool` use karo:
   `python jwt_tool.py <token> -X a -pk public.key`

**Attack 3: kid (Key ID) Injection**
1. Token header mein `"kid":"key1"` hota hai.
2. Agar server `kid` ko path ki tarah use karta hai, to try karo:
   - `"kid":"../../../../dev/null"` – ye null key use karega.
   - `"kid":"file:///etc/passwd"` – LFI try karo.
3. Command injection bhi try karo: `"kid":"| whoami"`

**Attack 4: jku (JWK Set URL) Injection**
1. Header mein `"jku":"https://server.com/jwks.json"` hota hai.
2. Apna khud ka JWKS server banao with your public key.
3. Header mein `"jku":"https://attacker.com/jwks.json"` set karo.
4. Apne private key se sign karo.
5. Server aapke JWKS se public key leke verify karega, aur accept kar lega.

#### ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success:** Token modify kar ke admin access mil gaya, ya kisi aur user ka data mila.
- **Failure:** Server "Invalid signature" error deta hai.

#### ⚖️ Comparison (X vs Y)
| Attack | Method | Difficulty |
|--------|--------|------------|
| None Algorithm | `alg:none` | Easy |
| Algorithm Confusion | RS256 to HS256 | Medium |
| kid Injection | Path traversal | Medium |
| jku Injection | External JWKS | Hard |

#### 🚫 Common Mistakes
- Sirf HS256 tokens par focus karna, RS256 ignore karna.
- `kid` injection mein path traversal ke alawa SQLi bhi ho sakti hai, ignore karna.

#### 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Public key kaise milegi?"** – Often `/jwks.json`, `/.well-known/jwks.json`, ya response headers mein.
- **"None algorithm kaise try karun?"** – Header base64 decode karo, modify karo, fir base64 encode karo aur signature part khali rakho.

#### 🌍 Real-World Use Case
Paytm ki API mein JWT vulnerability thi jisme `kid` parameter SQL injection vulnerable tha. Attacker `kid` mein SQLi daal kar secret nikal sakta tha.

#### 🛠️ Best Practices (Pro Tips)
- **jwt_tool** install karo: `git clone https://github.com/ticarpi/jwt_tool`
- **Burp Extension:** "JSON Web Tokens" extension use karo.
- Manual tampering ke liye `jwt.io` website use kar sakte ho.

#### ❓ FAQ
1. **Q: JWT secret kaise pata karein?**  
   A: Weak secret hai to crack karo `hashcat` se. Common wordlist use karo.
2. **Q: JWKS kya hai?**  
   A: JSON Web Key Set – server ke public keys ka set.
3. **Q: Kya JWT hamesha vulnerable hota hai?**  
   A: Nahi, proper implementation secure hai.

#### 📝 Ek Line Mein Yaad Rakhne Ko
**JWT ka header aur payload kholo, algorithm badlo, signature hatao, aur admin ban jao.**

---

### Topic 2.5: 🎯 Title: OAuth 2.0 Misconfigurations
*Dusre ke account se login karo*

#### 🐣 Samjhane ke liye (Analogy)
Tum kisi hotel mein gaye. Wahan bola "Google se login karo". Tum Google login karte ho, aur hotel ko apna Google ID ka pata chalta hai. Ab agar hotel wala Google se pooche "Iska email kya hai?" bina tumhari permission ke, to tumhari privacy leak ho jayegi. Yahan **Google = OAuth provider**, **hotel = client app**.

#### 📖 Technical Definition
OAuth 2.0 ek authorization framework hai jisme user kisi third-party app ko apne resources ka limited access de sakta hai bina apni credentials share kiye. Misconfigurations mein attacker authorization code hijack kar sakta hai, ya redirect_uri manipulate kar sakta hai.

#### 🧠 Zaroorat Kyun Hai?
OAuth flaws se aap kisi bhi user ke account mein login kar sakte ho bina unka password jaane, agar client app ne OAuth theek implement nahi kiya.

#### 🔍 Visual - Screen Par Kya Dikhega
OAuth flow:
1. User clicks "Login with Google"
2. Redirect to `accounts.google.com/o/oauth2/auth?client_id=123&redirect_uri=https://client.com/callback&response_type=code`
3. User grants permission
4. Google redirects to `client.com/callback?code=AUTH_CODE`
5. Client server exchanges code for token.

#### ⚙️ Under the Hood
Main components:
- **Client ID:** App ki public identity
- **Client Secret:** App ka private key (server-side)
- **Redirect URI:** Jahan code bhejna hai
- **Authorization Code:** Temporary code jo token ke liye exchange hota hai
- **Access Token:** Actual resource access ke liye

#### 💻 Hands-On Step-by-Step
**Attack 1: Redirect URI Manipulation**
1. OAuth login flow start karo.
2. Burp mein authorize request capture karo.
3. `redirect_uri` parameter ko modify karo apne domain par:
   `redirect_uri=https://attacker.com/callback`
4. Agar server allowed redirect URIs ko properly validate nahi karta, to authorization code attacker ke server par aa jayega.
5. Attacker ye code use kar ke token le sakta hai.

**Attack 2: CSRF on OAuth**
1. Jab user OAuth login karta hai, ek `state` parameter hota hai jo CSRF token ka kaam karta hai.
2. Agar `state` missing hai ya predictable hai, to attacker apna OAuth code kisi aur user ke account se link kar sakta hai.

**Attack 3: Code Leakage via Referer**
1. Jab Google redirect karta hai client callback par, URL mein `code` hota hai.
2. Agar client page mein koi external resource (image, script) load ho raha hai, to `Referer` header mein `code` leak ho sakta hai.

#### ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success:** Authorization code apne server par mil gaya, use token exchange kiya, aur user ka account access kar liya.
- **Failure:** Server invalid redirect_uri error dega, ya code validate nahi hoga.

#### ⚖️ Comparison (X vs Y)
| Attack | Target | Impact |
|--------|--------|--------|
| Redirect URI Manipulation | Authorization code hijack | Account takeover |
| CSRF | State parameter missing | Account linking |
| Code Leakage | Referer header | Token theft |

#### 🚫 Common Mistakes
- Sirf client_id check karna, redirect_uri ko ignore karna.
- `state` parameter implement na karna.
- Code ko URL mein expose karna (should be POST).

#### 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Redirect URI validate kaise hota hai?"** – Client registration ke time allowed URIs list di jati hai. Server check karta hai ki redirect_uri us list mein hai ya nahi. Agar partial match check ho raha hai, to `https://client.com/callback.attacker.com` bhi accept ho sakta hai.

#### 🌍 Real-World Use Case
Facebook OAuth mein ek flaw tha ki `redirect_uri` properly validate nahi hota tha. Attacker code hijack kar ke kisi bhi user ka account le sakta tha.

#### 🛠️ Best Practices (Pro Tips)
- OAuth testing ke liye **OAuth 2.0 Pentesting Guide** padho.
- Burp Extension: **OAuth Scan** use karo.
- Manual testing mein har redirect_uri variation try karo.

#### ❓ FAQ
1. **Q: OAuth aur JWT mein kya difference?**  
   A: OAuth authorization framework hai, JWT token format hai. OAuth JWT use kar sakta hai.
2. **Q: Authorization code kaise hijack karun?**  
   A: Redirect URI apne server par point karo, aur code capture karo.
3. **Q: CSRF se kaise bachein?**  
   A: `state` parameter use karo jo unpredictable ho.

#### 📝 Line Mein Yaad Rakhne Ko
**OAuth ka redirect_URI kholo, code apne paas bhej lo, aur account le lo.**

---

### Topic 2.6: 🎯 Title: Password Reset Logic Flaws
*Password reset tod do*

#### 🐣 Samjhane ke liye (Analogy)
Maano tum apna password bhool gaye. Website par "Forgot Password" click karte ho. Wo tumhe email bhejti hai link. Ab agar wo link ka format simple ho, jaise `reset?token=123`, to tum 123,124,125 try kar sakte ho aur kisi aur ka reset kar sakte ho.

#### 📖 Technical Definition
Password reset functionality mein flaws hote hain jaise predictable tokens, token reuse, ya parameter manipulation se kisi aur ka password change kar dena.

#### 🧠 Zaroorat Kyun Hai?
Isse aap kisi bhi user ka password change kar sakte ho, account takeover kar sakte ho.

#### 🔍 Visual - Screen Par Kya Dikhega
Reset link kuch aisa:  
`https://target.com/reset?token=abc123&user=john`

#### 💻 Hands-On Step-by-Step
**Attack 1: Predictable Tokens**
1. Apne email par reset request karo.
2. Token note karo: `token=123456`
3. Dusra reset request karo, token aaya `123457`.
4. Incrementing hai to brute-force possible hai.
5. Victim ka email daalo aur tokens brute-force karo.

**Attack 2: Host Header Injection**
1. Reset request intercept karo.
2. `Host` header change karo `attacker.com`.
3. Server reset link bana sakta hai `http://attacker.com/reset?token=xyz`
4. User link click karega to token attacker ke server par aa jayega.

**Attack 3: Parameter Pollution**
1. Reset request: `POST /reset` with `{"email":"victim@mail.com"}`
2. Try `{"email":"victim@mail.com","email":"attacker@mail.com"}`
3. Kya server victim ko link bhejta hai ya attacker ko?

#### ✅ Kaamyabi ki Nishani
- **Success:** Victim ka password change kar diya.
- **Failure:** Apna hi password change ho raha hai.

#### 📝 Ek Line Mein Yaad Rakhne Ko
**Reset token weak hai to kisi ka bhi account le lo.**

---

### Topic 2.7: 🎯 Title: Multi-Factor Authentication (MFA) Bypass
*Do tala tod do*

#### 🐣 Samjhane ke liye (Analogy)
Ghar par do tala lagaye hain. Ek guard ke paas, ek gate par. Agar tum guard ko bypass kar ke gate tak pahunch gaye, to ek tala todna hai. Waise hi, MFA ke baad bhi agar session handling weak hai to bypass possible hai.

#### 📖 Technical Definition
MFA bypass tab hota hai jab:
- MFA sirf specific steps par apply ho (e.g., login par, but API calls par nahi)
- MFA code predictable ho
- MFA ko disable kar sakte ho

#### 💻 Hands-On Step-by-Step
**Attack 1: MFA Not Required on APIs**
1. Login with MFA, capture session token.
2. Ab sensitive API call karo (e.g., change password) with same token.
3. Agar server MFA nahi maang raha, to bypass ho gaya.

**Attack 2: MFA Disable via Parameter**
1. Request mein `"mfa_enabled":true` ho sakta hai.
2. Use `false` karo.

#### 📝 Ek Line Mein Yaad Rakhne Ko
**MFA sirf login par hai, baaki APIs par nahi, to MFA ka kya fayda?**

---


### Topic 2.4: 🎯 Title: Session Security – Fixation, Rotation, Concurrency
*Session ID se khelo, account le lo*

#### 🐣 Samjhane ke liye (Analogy)
Socho tum ek party mein jaate ho. Guard tumhe ek slip deta hai jisme number likha hai `123`. Tum andar jao, party karo. Jab wapas aao, guard slip check karta hai aur andar jaane deta hai. Ab agar guard slip ka number change nahi karta, toh koi aur tumhari slip copy kar ke aake bol sakta hai "Mera number bhi `123` hai" aur andar ghus jayega. Yahan **slip = session ID**, **guard = server**.

#### 📖 Technical Definition
Session security ka matlab hai ki server har user ko ek unique session ID deta hai, aur us ID se user ki identity maintain karta hai. Agar ye session ID **predictable**, **static**, ya **poorly managed** ho, toh attacker usse hijack kar ke user ka account le sakta hai.

#### 🧠 Zaroorat Kyun Hai?
Session fixation, session hijacking, concurrent session issues – ye sab flaws se aap bina password ke kisi bhi user ke account mein ghus sakte ho.

#### 🔍 Visual - Screen Par Kya Dikhega
Burp Suite mein:
- Login se pehle: `Cookie: PHPSESSID=abc123`
- Login ke baad: `Cookie: PHPSESSID=abc123` (same) – **Vulnerable!**
- Login ke baad: `Cookie: PHPSESSID=xyz789` (changed) – **Secure**.

#### ⚙️ Under the Hood
- **Session Fixation:** Attacker pehle user ko ek session ID de deta hai (jaise email mein link bhej kar). User login karta hai to server usi session ID ko authenticated mark kar deta hai. Ab attacker ke paas bhi wahi session ID hai, to wo user banke ghoom sakta hai.
- **Refresh Token Rotation:** OAuth 2.0 mein refresh token long-lived hota hai, access token short-lived. Jab access token expire ho, to refresh token se naya access token lete hain. Agar refresh token rotate nahi hota (purana wahi rehta hai), to attacker chura kar hamesha access le sakta hai.
- **Concurrent Sessions:** Kitne devices par ek user login ho sakta hai? Isse brute-force attacks mein madad milti hai.

#### 💻 Hands-On Step-by-Step (Reference: Page 19)
**Attack 1: Session Fixation**
1. Target site par bina login kiye request bhejo (e.g., homepage).
2. Response mein cookie note karo: `Set-Cookie: PHPSESSID=abc123`
3. Ab ek phishing email bhejo user ko jisme ye link ho: `https://target.com/login?PHPSESSID=abc123`
4. User login karta hai to server isi session ID ko authenticate kar dega.
5. Ab tum wahi session ID use karo: `Cookie: PHPSESSID=abc123`
6. Request bhejo – tum user banke logged-in ho!

**Attack 2: Check Session ID Static Hai Kya?** (Reference: Page 19)
1. Burp mein login se pehle kisi bhi request ka cookie capture karo.
2. Login request karo aur successful login ke baad ki cookie dekho.
3. Compare karo:
   - Same hai → **Session Fixation Vulnerability**
   - Different hai → Secure

**Attack 3: Refresh Token Rotation Test**
1. Login karo, refresh token capture karo (usually in response body).
2. Jab access token expire ho, refresh token use kar ke naya access token lo.
3. Response mein naya refresh token aaya ya purana?
   - Naya aaya → Rotation implement hai (secure)
   - Purana wahi aaya → Rotation nahi hai (vulnerable)
4. Ab purana refresh token dobara use karo. Agar accept ho jata hai, to **refresh token replay** possible hai.

**Attack 4: Concurrent Sessions Test**
1. Ek browser (Chrome) se login karo.
2. Doosra browser (Firefox) se same credentials se login karo.
3. Chrome se logout karo.
4. Firefox check karo – logout hua ya nahi?
   - Dono sessions active hain → Concurrent sessions allowed.
   - Kitne max? Try 10 browsers se login. Limit check karo.

#### ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success:** Session ID same mili, refresh token rotate nahi ho raha, unlimited concurrent sessions.
- **Failure:** Session ID change ho gayi, refresh token rotate ho raha, concurrent sessions limited.

#### ⚖️ Comparison (X vs Y)
| Feature | Secure Implementation | Vulnerable Implementation |
|---------|----------------------|--------------------------|
| Session ID | Login ke baad change | Login ke baad same |
| Refresh Token | Har use par rotate | Static, reuse possible |
| Concurrent Sessions | Limited (1-5) | Unlimited |

#### 🚫 Common Mistakes
- Sirf login form test karna, session fixation ke liye pre-login cookies ignore karna.
- Refresh token ko bhi access token ki tarah treat karna – dono alag hote hain.
- Concurrent sessions test karte waqt rate limit bhoolna.

#### 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Session fixation ke liye user ko link kaise bhejein?"** – Bug bounty mein aap PoC bana kar dikha sakte ho ki agar user ye link click kare to kya hoga. Direct user ko bhejna illegal hai.
- **"Refresh token rotation test mein kaise pata chale ki naya token aaya?"** – Response body dekho, usually `refresh_token` field mein naya token aata hai.

#### 🌍 Real-World Use Case
Facebook pe ek time pe session fixation tha. Attacker ne user ko ek link bheja jisme session ID set thi. User login kiya to attacker us session ID se account access kar sakta tha.

#### 🎨 Visual Diagram (Session Fixation)
```
[Attacker] -> Generates session ID (SID=123)
[Attacker] -> Sends link to user: https://target.com/?SID=123
[User] -> Clicks link, logs in
[Server] -> Associates SID=123 with user's account
[Attacker] -> Uses SID=123 -> Logged in as user!
```

#### 🛠️ Best Practices (Pro Tips)
- **Burp Extension:** "Session Fixation Scanner" use karo.
- Refresh token rotation test ke liye **AutoRepeater** extension use karo to automatically replay old tokens.
- Concurrent sessions test ke liye different browsers ya incognito windows use karo.

#### ❓ FAQ
1. **Q: Session fixation ka OWASP Top 10 mein kya number hai?**  
   A: OWASP API Top 10 mein specifically nahi, lekin "Broken Authentication" ka part hai.
2. **Q: Refresh token reuse se kya ho sakta hai?**  
   A: Attacker ek baar token chura kar hamesha naye access tokens le sakta hai, kabhi logout nahi hona.
3. **Q: Concurrent sessions ka kitna limit safe hai?**  
   A: Usually 3-5 sessions allowed hote hain, isse zyada suspicious hai.

#### 📝 Ek Line Mein Yaad Rakhne Ko
**Session ID login pe change ho, refresh token rotate ho, aur concurrent sessions limited ho.**

---

### Topic 2.5: 🎯 Title: JWT (JSON Web Tokens) Deep-Dive
*Token ka khel, admin ban ne ka spell*

#### 🐣 Samjhane ke liye (Analogy)
JWT ek **magic pass** ki tarah hai jo tumhe har jagah entry deta hai. Iss pass par likha hota hai "User: Normal", aur neeche ek **chhapa (signature)** hota hai jo sirf king ke paas hai. Agar tum pass par "User: Admin" likh kar signature nahi bana sakte, to guard pakad lega. Lekin agar guard signature check karna bhool jaye, ya tum koi aisa trick use karo ki signature valid lagne lage, to tum admin ban sakte ho.

#### 📖 Technical Definition
JWT (JSON Web Token) ek stateless authentication mechanism hai. Ye teen parts mein banta hai: `header.payload.signature`. Sab kuch base64 encoded hota hai. Server token ko verify karta hai signature se, aur agar valid hai to payload par bharosa karta hai.

#### 🧠 Zaroorat Kyun Hai?
JWT attacks se aap:
- **Privilege Escalation** kar sakte ho (user to admin)
- **Account Takeover** kar sakte ho (kisi aur ka token bana lo)
- **Information Disclosure** kar sakte ho (payload mein sensitive data ho to)

#### 🔍 Visual - Screen Par Kya Dikhega
JWT kuch aisa dikhta hai:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4iLCJyb2xlIjoidXNlciJ9.4x1jU8JkL9KxJkL9KxJkL9K
```
- **Part 1 (Header):** `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9` → Decode: `{"alg":"HS256","typ":"JWT"}`
- **Part 2 (Payload):** `eyJ1c2VyIjoiYWRtaW4iLCJyb2xlIjoidXNlciJ9` → Decode: `{"user":"admin","role":"user"}`
- **Part 3 (Signature):** `4x1jU8JkL9KxJkL9KxJkL9K` → HMAC-SHA256(secret, header.payload)

#### ⚙️ Under the Hood
JWT verification:
1. Header aur payload ka base64 decode karo.
2. Header se `alg` parameter dekho.
3. Agar `alg: HS256`, to secret se signature verify karo.
4. Agar `alg: RS256`, to public key se signature verify karo.
5. Agar `alg: none`, to signature check mat karo (vulnerable!).

#### 💻 Hands-On Step-by-Step

##### Sub-Topic 2.5.1: JWT Structure & Decoding (Reference: Page 7)

**Step-by-Step:**
1. Kisi bhi request se JWT token copy karo (usually `Authorization: Bearer <token>` header mein).
2. `jwt.io` website kholo.
3. Token paste karo – decoded header aur payload dikh jayega.
4. Header mein dekho `alg` kya hai (HS256, RS256, none).
5. Payload mein dekho kaunsa data hai (`user`, `role`, `exp`, `jti`, etc.).
6. **Note:** Signature verify karne ke liye secret/pubic key chahiye, jo humein nahi pata.

##### Sub-Topic 2.5.2: Hashcat – Brute-force HS256 Secret (Reference: Page 8-9)

**Scenario:** Server HS256 use kar raha hai, aur secret key weak hai (e.g., `secret`, `password`, `123456`). Hum token ka signature crack kar ke secret nikal sakte hain.

**Step-by-Step:**
1. Token capture karo, e.g.:
   ```
   eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4iLCJyb2xlIjoidXNlciJ9.4x1jU8JkL9KxJkL9KxJkL9K
   ```
2. Is token ko ek file mein save karo: `token.txt`
3. Hashcat command:
   ```bash
   hashcat -m 16500 token.txt /path/to/wordlist.txt --show
   ```
   - `-m 16500` = JWT HS256 (HS384 ke liye `16510`, HS512 ke liye `16520`)
   - Wordlist mein common secrets daalo (e.g., `rockyou.txt`)
4. Agar secret crack ho gaya, to output kuch aisa hoga:
   ```
   eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4iLCJyb2xlIjoidXNlciJ9.4x1jU8JkL9KxJkL9KxJkL9K:secret123
   ```
   Means secret = `secret123`
5. Ab is secret se apna khud ka token bana sakte ho.

##### Sub-Topic 2.5.3: None Algorithm Attack

**Scenario:** Purani JWT libraries mein `alg: none` ko support karti thi, jisme signature verify nahi hota tha.

**Step-by-Step:**
1. Original token ka header base64 decode karo:
   ```
   echo "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" | base64 -d
   {"alg":"HS256","typ":"JWT"}
   ```
2. Modify karo `alg` ko `none`:
   ```
   {"alg":"none","typ":"JWT"}
   ```
3. Base64 encode karo (URL-safe):
   ```
   echo -n '{"alg":"none","typ":"JWT"}' | base64 | tr '/+' '_-' | tr -d '='
   eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0
   ```
4. Payload modify karo, e.g., `{"user":"admin","role":"admin"}`
   ```
   echo -n '{"user":"admin","role":"admin"}' | base64 | tr '/+' '_-' | tr -d '='
   eyJ1c2VyIjoiYWRtaW4iLCJyb2xlIjoiYWRtaW4ifQ
   ```
5. Signature part hata do (empty rakho). Token ban gaya:
   ```
   eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyIjoiYWRtaW4iLCJyb2xlIjoiYWRtaW4ifQ.
   ```
6. Request mein token replace karo. Agar server `alg:none` accept karta hai to admin access mil jayega.

##### Sub-Topic 2.5.4: Algorithm Confusion (RS256 -> HS256)

**Scenario:** Server RS256 (asymmetric) use kar raha hai, aur public key publicly available hai (e.g., `/jwks.json`). Hum public key ko HS256 symmetric key ki tarah use karte hain.

**Step-by-Step:**
1. Public key dhundho:
   - Try `/.well-known/jwks.json`
   - Try `/jwks.json`
   - Try `/.well-known/openid-configuration` (jo jwks_uri batayega)
2. Public key save karo `public.key` file mein.
3. JWT token capture karo.
4. `jwt_tool` use karo:
   ```bash
   python jwt_tool.py <token> -X a -pk public.key
   ```
   - `-X a` = Algorithm confusion attack
5. Ye tool naya token banayega with `alg: HS256` aur public key se sign karega.
6. Request mein naya token bhejo. Agar server public key se verify karta hai (jo ab secret ban gaya), to accept ho jayega.

**Manual Method:**
1. Header change karo: `{"alg":"HS256","typ":"JWT"}`
2. Payload modify karo.
3. Public key ko secret maan kar HMAC-SHA256 sign karo.
   - Python mein:
     ```python
     import jwt
     with open('public.key', 'r') as f:
         public_key = f.read()
     token = jwt.encode({'user':'admin'}, public_key, algorithm='HS256')
     print(token)
     ```

##### Sub-Topic 2.5.5: `kid` (Key ID) Injection

**Scenario:** Header mein `kid` parameter hota hai jo server ko batata hai ki kaunsi key use karni hai verify karne ke liye. Agar server is `kid` ko bina validate kiye file system ya database se read karta hai, to hum path traversal ya SQLi kar sakte hain.

**Step-by-Step:**
1. Original token ka header dekho:
   ```json
   {
     "alg": "HS256",
     "typ": "JWT",
     "kid": "key1"
   }
   ```
2. `kid` ko modify karo:
   - **Path Traversal:** `"kid": "../../../../dev/null"` (null key use karega)
   - **Path Traversal:** `"kid": "../../../../etc/passwd"` (LFI try)
   - **Command Injection:** `"kid": "| whoami"`
   - **SQLi:** `"kid": "key' UNION SELECT 'secret'"`
3. Agar server `kid` ko file path samajh kar read karta hai, to:
   - `../../../../dev/null` ka matlab empty string, to signature verification fail ho sakta hai ya empty key use ho sakti hai.
   - Agar `/etc/passwd` read ho jata hai, to uske content se key bana sakte ho.
4. Naya token banao with modified `kid` aur sign karo (agar secret pata ho to).
5. Bhej kar dekho.

##### Sub-Topic 2.5.6: `jku` / `x5u` Header Injection

**Scenario:** `jku` (JWK Set URL) header mein server JWKS file ka URL deta hai jahan se public key leni hai. Agar server bina validate kiye is URL se key uthata hai, to hum apna khud ka JWKS server bana sakte hain.

**Step-by-Step:**
1. Apna khud ka JWKS server banao (ya online tool use karo).
2. Apne private-public key pair banao.
3. JWKS endpoint par apni public key serve karo.
4. Original token ka header modify karo:
   ```json
   {
     "alg": "RS256",
     "typ": "JWT",
     "jku": "https://attacker.com/jwks.json"
   }
   ```
5. Payload modify karo, aur apne private key se sign karo.
6. Token bhejo. Server `jku` se public key uthayega aur verify karega – jo ki valid hoga!

##### Sub-Topic 2.5.7: JTI (JWT ID) Replay Attack

**Scenario:** `jti` claim unique ID hota hai token ka. Agar server check nahi karta ki ye ID already use ho chuki hai, to same token baar-baar use kar sakte ho.

**Step-by-Step:**
1. Koi sensitive action ka token capture karo (e.g., password change).
2. Use token repeat karo multiple times.
3. Agar har baar action successful ho, to replay vulnerability hai.

##### Sub-Topic 2.5.8: Timing Attacks

**Scenario:** Valid aur invalid signature verify karne mein server different time le raha hai. Isse brute-force fast ho sakta hai.

**Step-by-Step:**
1. Burp Suite ya Python script se time measure karo.
2. Multiple requests bhejo with slightly different signatures.
3. Agar response time mein consistent difference ho, to timing attack possible hai.

#### ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success:** Token modify kar ke admin access mil gaya, ya kisi aur user ka data mila.
- **Failure:** Server "Invalid signature" error deta hai, ya 401 Unauthorized.

#### ⚖️ Comparison (X vs Y)
| Attack | Difficulty | Impact | Fix |
|--------|------------|--------|-----|
| None Algorithm | Easy | Critical | Disable `alg:none` |
| Algorithm Confusion | Medium | Critical | Validate algorithm, use separate keys |
| `kid` Injection | Medium | High | Validate `kid` input |
| `jku` Injection | Hard | Critical | Whitelist JWKS URLs |
| JTI Replay | Easy | Medium | Store used JTIs |
| Hashcat | Easy | Critical | Use strong secrets |

#### 🚫 Common Mistakes
- Sirf HS256 tokens par focus karna, RS256 ignore karna.
- `kid` injection mein path traversal ke alawa SQLi bhi ho sakti hai, ignore karna.
- JTI replay ke liye `exp` (expiry) check karna, lekin `jti` check na karna.

#### 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Public key kaise milegi?"** – Often `/jwks.json`, `/.well-known/jwks.json`, ya response headers mein. Kuch APIs metadata endpoint bhi dete hain.
- **"None algorithm kaise try karun?"** – Header base64 decode karo, modify karo, fir base64 encode karo aur signature part khali rakho. Ya tool use karo.
- **"`kid` injection mein SQLi kaise kaam karega?"** – Agar server `kid` ko database query mein use karta hai jaise `SELECT key FROM keys WHERE kid='key1'`, to SQLi daal kar secret nikal sakte ho.

#### 🌍 Real-World Use Case
- **Paytm:** `kid` parameter SQL injection vulnerable tha. Attacker `kid` mein SQLi daal kar secret nikal sakta tha.
- **Microsoft:** Algorithm confusion vulnerability thi jisme public key se HS256 sign kar sakte the.
- **Apple:** `jku` injection se attacker apna JWKS server laga kar token bana sakta tha.

#### 🎨 Visual Diagram (JWT Structure)
```
JWT Token:
[Header] . [Payload] . [Signature]
    |           |            |
    v           v            v
{"alg":"HS256"} {"user":"admin"} HMAC-SHA256(secret, header.payload)
```

#### 🛠️ Best Practices (Pro Tips)
- **jwt_tool** install karo: `git clone https://github.com/ticarpi/jwt_tool`
- **Burp Extension:** "JSON Web Tokens" extension use karo jo automatically decode karega aur attacks suggest karega.
- Manual tampering ke liye `jwt.io` website use kar sakte ho, lekin signature verify nahi hoga.
- Hashcat ke liye `-m 16500` yaad rakho.
- Algorithm confusion ke liye public key mile to turant try karo.

#### ❓ FAQ
1. **Q: JWT secret kaise pata karein?**  
   A: Weak secret hai to crack karo `hashcat` se. Common wordlist use karo (`rockyou.txt`). Agar secret strong hai to nahi milega.
2. **Q: JWKS kya hai?**  
   A: JSON Web Key Set – server ke public keys ka set. Multiple keys ho sakti hain, `kid` se identify hoti hain.
3. **Q: Kya JWT hamesha vulnerable hota hai?**  
   A: Nahi, proper implementation secure hai. Lekin implementation flaws common hain.
4. **Q: JWT mein signature verify kaise hota hai?**  
   A: Server header ke `alg` ke according signature verify karta hai. HS256 mein secret se, RS256 mein public key se.
5. **Q: JWT replay se kaise bachein?**  
   A: `jti` claim use karo aur expire kar do, ya short expiry (`exp`) rakho.

#### 📝 Ek Line Mein Yaad Rakhne Ko
**JWT ka header aur payload kholo, algorithm badlo, signature hatao, `kid` mein traversal daalo, aur admin ban jao.**

---

### Topic 2.6: 🎯 Title: OAuth 2.0 / OIDC Flows
*Dusre ke account se login karo*

*(Is topic ko hum pehle hi cover kar chuke hain as Topic 2.5 in previous response. Yahan sirf missing points add kar rahe hain.)*

#### Additional Points from Raw Notes:

**Redirect URI Manipulation (Detailed):**
1. OAuth flow start karo "Login with Google".
2. Authorize request capture karo:
   ```
   GET /authorize?client_id=123&redirect_uri=https://client.com/callback&response_type=code
   ```
3. `redirect_uri` modify karo:
   - Try `https://attacker.com/callback`
   - Try `https://client.com/callback.attacker.com` (if suffix check)
   - Try `https://client.com/callback@attacker.com`
   - Try `https://client.com/callback/../attacker.com`
4. Agar server allowed redirect URIs ko properly validate nahi karta, to authorization code attacker ke server par aa jayega.
5. Attacker ye code use kar ke token le sakta hai.

**State Parameter Missing (CSRF):**
1. OAuth request mein `state` parameter dekho.
2. Agar missing hai ya predictable hai (e.g., `state=123`), to CSRF possible hai.
3. Attacker apni site par ek form bana sakta hai jo user ke browser se OAuth flow start kare.
4. User jab us form par click kare, to uske account ko attacker ke account se link kar de.

**Token Leakage via Referer:**
1. Jab Google redirect karta hai client callback par, URL mein `#access_token=` ya `?code=` hota hai.
2. Client callback page mein agar koi external resource load ho raha hai (image, script, font), to `Referer` header mein ye URL leak ho sakta hai.
3. Attacker apni site par aisi resource rakhe jo log collect kare.

#### 📝 Ek Line Mein Yaad Rakhne Ko
**OAuth ka redirect_URI kholo, state parameter check karo, aur referer se token leak dhundho.**

---

## 🔥 Module 2 Complete Summary: Authentication Attacks Checklist

| Topic | What to Check | Impact |
|-------|---------------|--------|
| Response Manipulation | 403 to 200, body flags | Login bypass |
| No-Rate Limit | OTP brute-force, inbox bombing | Account takeover |
| Clickjacking | X-Frame-Options missing | Session riding |
| Session Fixation | Login pe session ID change? | Account hijack |
| Refresh Token Rotation | Old token reuse? | Persistent access |
| Concurrent Sessions | Unlimited sessions? | Easy brute-force |
| JWT None Algorithm | `alg:none` accept? | Admin access |
| JWT Algorithm Confusion | RS256 to HS256 | Token forgery |
| JWT `kid` Injection | Path traversal, SQLi | Secret leak |
| JWT `jku` Injection | External JWKS | Token forgery |
| JWT JTI Replay | Same token reuse | Action replay |
| OAuth Redirect URI | Manipulation possible? | Code hijack |
| OAuth State Missing | CSRF | Account linking |
| OAuth Token Leakage | Referer header | Token theft |

========================================================================================

## 🔑 Module 3: Authorization (BOLA, BPLA, BFLA)
*Andar aane ke baad, kya kya kar sakte ho?*

---

### Topic 3.1: BOLA / IDOR (Broken Object Level Authorization)

---

#### 1. 🎯 Title
**Broken Object Level Authorization (BOLA) / IDOR**

#### 2. 🐣 Samjhane ke liye (Analogy)
Maan lo ek school mein har student ke paas ek **locker** hai jisme wo apni books aur copy rakhta hai. Locker par ek **number** likha hai (e.g., locker 123). Jab kisi student ko apna locker kholna hota hai, wo guard ko apna **ID card** (authentication token) aur locker number batata hai. Guard sirf ye check karta hai ki **ID card valid hai ya nahi** (authentication), lekin ye nahi check karta ki **ye locker is student ka hai ya nahi** (authorization). Ab ek student, Aman (locker 123), apne dost ke locker 456 ko kholne ki koshish karta hai. Guard dekhta hai ID card valid hai, to locker khol deta hai – bina ye dekhe ki Aman ka locker 456 se koi lena-dena nahi. Yahi BOLA vulnerability hai.

#### 3. 📖 Technical Definition
BOLA (ya IDOR) tab hota hai jab API kisi **object** (jaise user, file, order, etc.) ko access karne ke liye client se ek **identifier** (ID, number, UUID) leta hai, par server **authorization check** karna bhool jata hai. Matlab, server sirf authentication check karta hai – “kya aap valid user ho?” – lekin ye verify nahi karta ki **current authenticated user ko is specific object ko access karne ka permission hai ya nahi**. Iski vajah se ek user doosre user ke data ko dekh, badal, ya delete kar sakta hai.

#### 4. 🧠 Zaroorat Kyun Hai?
Ye vulnerability OWASP API Security Top 10 mein **#1** position par hai, kyunki iska **impact bahut high** hota hai – attackers seedha doosron ka private data chura sakte hain (PII, financial details, medical records), ya unke resources ko modify/delete kar sakte hain. Bug bounty programs mein sabse zyada reports BOLA/IDOR ki hoti hain aur inka bounty bhi highest hota hai.

#### 5. 🔍 Visual - Screen Par Kya Dikhega
Burp Suite ya kisi bhi proxy tool mein jab aap kisi API request ko intercept karte ho, toh kuch aisa dikhega:

**Request:**
```
GET /api/v1/users/123 HTTP/1.1
Host: target.com
Authorization: Bearer <attacker_token>
```
Yahan `123` object ID hai. Isko badalkar `456` karte ho:
```
GET /api/v1/users/456 HTTP/1.1
...
```
Agar response mein user 456 ka data aata hai (jaise name, email, etc.), to ye **success** hai – BOLA mil gaya. Agar error aata hai (403, 401, 404) to failure.

#### 6. ⚙️ Under the Hood
Server ka backend code kuch is tarah ho sakta hai (dummy example):
```python
@app.route('/api/users/<user_id>')
def get_user(user_id):
    # Sirf authentication check
    if not is_authenticated(request.headers['Authorization']):
        return {"error": "Unauthorized"}, 401

    # Database se user fetch karo
    user = db.query("SELECT * FROM users WHERE id = ?", user_id)
    return user, 200
```
Yahan `is_authenticated` to check ho raha hai, lekin ye nahi dekha gaya ki currently logged-in user ka ID `user_id` ke barabar hai ya nahi. Isliye koi bhi authenticated user kisi bhi user ka data le sakta hai.

#### 7. 💻 Hands-On Step-by-Step
1. **Login** karo ek normal user account se (e.g., user A).
2. **Intercept** karo koi bhi request jisme object ID ho – jaise profile view, order details, file download. Common patterns:
   - `GET /api/profile?id=123`
   - `GET /api/orders/ORD-456`
   - `DELETE /api/posts/789`
3. Request ko **Burp Repeater** mein bhejo (right click → Send to Repeater).
4. ID ko modify karo:
   - Numeric IDs: `123` → `124`, `125`, `0`, `-1` (negative IDs se error messages mein DB info leak ho sakta hai).
   - UUIDs: Agar IDs `user-abc123` jaisi predictable nahi hain, to unhe kisi aur jagah se leak karne ki koshish karo (JS files, referrer header, other API responses). Fuzzing ke liye Burp Intruder mein payload set karo.
   - Strings: Agar IDs `ORD-2025-001` jaisi hain, to pattern guess karo.
5. Request forward karo aur response dekho. Agar doosre user ka data mil raha hai, to BOLA hai.
6. **Bulk BOLA**: Agar API multiple IDs ek saath accept karti ho (jaise POST request mein JSON array), to try karo:
   ```json
   POST /api/users/batch
   {
     "ids": [123,124,125]
   }
   ```
   Agar saare users ka data dump mil gaya, to wo massive BOLA hai.
7. **Chained BOLA**: Pehle kisi IDOR se doosre user ki ID leak karo (e.g., kisi public profile se), fir us ID se private data access karo.
8. **Non-CRUD operations**: Sirf GET/POST nahi, balki `DELETE /api/user/123`, `PUT /api/user/123/password` jaise endpoints par bhi try karo.
9. **API versioning**: Agar `/v2/user/me` secure hai, to `/v1/user/123` try karo (version downgrade attack).
10. **Password Reset**: Reset link mein `user_id` ya `email` parameter change karke kisi aur ka password reset karne ki koshish karo.

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)
| **Situation** | **Response** |
|---------------|--------------|
| **Success** (BOLA present) | `200 OK` ke saath JSON mein victim ka data. Jaise: `{"id":456,"name":"Victim","email":"victim@example.com"}` |
| **Failure** (BOLA not present / patched) | `403 Forbidden` / `401 Unauthorized` / `404 Not Found` (agar ID exist nahi karti) ya phir `200 OK` but same user ka data aaye (current user ka hi data aaye, kyunki server ne enforce kiya ki current user hi access kar sakta hai) |

#### 9. ⚖️ Comparison (IDOR vs BOLA)
| **IDOR (Insecure Direct Object Reference)** | **BOLA (Broken Object Level Authorization)** |
|----------------------------------------------|-----------------------------------------------|
| Old term, mostly used in web apps. | Modern term, OWASP API Security Top 10 mein use hota hai. |
| Focuses on direct reference to object (like file path, DB key). | Focuses on missing authorization check at object level. |
| Basically same vulnerability. | Basically same vulnerability. |

#### 10. 🚫 Common Mistakes
- Sirf numeric IDs try karna, UUIDs ko ignore karna (par UUIDs bhi leak ho sakte hain).
- Sirf GET requests par focus karna; DELETE, PUT, POST ko bhool jana.
- Positive IDs par atakna; negative IDs na try karna (negative IDs se SQL injection ya error leaks mil sakte hain).
- Error messages ignore karna – jaise "User not found for ID 456" se confirm ho jata hai ki 456 exist karta hai, jisse brute force mein madad milti hai.
- Automated tools par depend rehna; manual fuzzing nahi karna.

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Mere API mein UUID use ho raha hai, to safe hoon na?"**
  Nahi, UUID sirf guess karna mushkil banata hai, lekin agar authorization check missing hai to vulnerability abhi bhi maujood hai. Agar UUIDs kisi aur jagah leak ho rahe hain (JS files, other API responses, referrer header), to attacker unhe collect kar sakta hai aur access kar sakta hai.
- **"Mere paas /me endpoint hai, to sab safe hai?"**
  `/me` usually current user ki details deta hai, lekin doosre endpoints ho sakte hain jaise `/user?id=` jahan check missing ho. Isliye sab endpoints test karo.
- **"Agar IDOR mil gaya to kya wo humesha critical hota hai?"**
  Impact par depend karta hai. Agar kisi user ka public data mil raha hai (jo anyway public hai), to severity low ho sakti hai. Lekin agar private data (email, phone, address) ya sensitive actions (delete, update) ho rahe hain, to critical hai.

#### 12. 🌍 Real-World Use Case
Ek bug bounty hunter ne Facebook mein GraphQL API ke through IDOR paya. Usne ek request mein `user_id` parameter change kiya aur doosre user ki private photos dekh li. Facebook ne usko $10,000+ ka bounty diya. Is tarah ke BOLA bugs aaj bhi regularly report hote hain.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
[Attacker] --> GET /api/user/456 (with attacker's session token)
   |
   v
[Server] --> Token verify? OK (attacker is user 123)
   |
   v
[Database] --> SELECT * FROM users WHERE id = 456;  (No check: user 123 can access 456?)
   |
   v
[Server] --> Returns data of user 456
   |
   v
[Attacker] gets Victim's private data
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Burp Intruder** ka use karo: payload positions set karo aur numbers, common patterns, UUID lists daalo.
- **Param Miner** extension se hidden parameters dhoondo.
- **Always test with two different accounts**: Ek low-privilege user se doosre user ke resources access karne ki koshish karo.
- **Check HTTP methods** – `GET`, `POST`, `PUT`, `DELETE` sab try karo.
- **API versioning** – `/v1`, `/v2`, `/v3` sab check karo.
- **Error messages analyse karo** – kahi ID exist karti hai ya nahi, iska clue milta hai.
- **Automated scanners** ki blind trust mat karo; manual testing essential hai.

#### 15. ❓ FAQ (Interview Q&A)
1. **Q:** BOLA aur IDOR mein kya antar hai?
   **A:** Dono same vulnerability hai. IDOR purana term hai, BOLA modern OWASP API Top 10 ka term hai jo authorization check missing par focus karta hai.
2. **Q:** Agar UUID use kar rahe hain, to kya BOLA possible hai?
   **A:** Haan, possible hai. UUID sirf enumeration mushkil banata hai, lekin agar authorization check missing hai to vulnerable hai. Agar UUID leak ho jaye (jaise kisi response mein), to attacker access kar sakta hai.
3. **Q:** BOLA sirf GET requests mein hota hai?
   **A:** Nahi, kisi bhi method (POST, PUT, DELETE) mein ho sakta hai. Jaise `DELETE /api/post/123` se kisi aur ka post delete karna.
4. **Q:** Bulk BOLA kya hai?
   **A:** Jab API ek saath multiple objects ki IDs accept karti hai (jaise array) aur server bina authorization check ke saare ka data return kar deta hai.
5. **Q:** BOLA ko kaise prevent karein?
   **A:** Har object access request mein check karo ki current user ke paas us object par access ka permission hai ya nahi. Jaise `if current_user.id == requested_user_id` ya role-based permissions.

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"BOLA matlab server ne sirf token check kiya, par ye nahi dekha ki token wala banda is ID ka malik hai ya nahi."**

---

### Topic 3.2: BPLA / Mass Assignment (Broken Property Level Authorization)

---

#### 1. 🎯 Title
**Broken Property Level Authorization (BPLA) / Mass Assignment**

#### 2. 🐣 Samjhane ke liye (Analogy)
Maano tum ek online form bhar rahe ho koi naya account banane ke liye. Form mein sirf **naam** aur **email** ke fields hain. Tum form bhar kar submit kar dete ho. Par peeche server pe jo code hai, wo tumhare bheje gaye saare data ko seedha database mein daal deta hai bina check kiye ki tumhe konsi fields bharne ki permission thi. Ab tum socho, form mein to sirf do fields the, lekin agar tum ek extra field bhej do, jaise `"isAdmin": true`, to server maan lega ki tum admin ban gaya. Isi tarah, **Mass Assignment** vulnerability mein attacker extra properties bhej kar un fields ko modify kar sakta hai jinhe modify karne ka uske paas authority nahi hai.

#### 3. 📖 Technical Definition
BPLA (ya Mass Assignment) tab hota hai jab API server client se aaye hue data ko **directly** internal objects (jaise database models) mein bind kar leta hai, bina **allowlist** ke ki kaunse properties ko update karne ki anumati hai. Iski vajah se attacker hidden ya sensitive fields (jaise `isAdmin`, `balance`, `role`) ko request mein bhej kar unki value badal sakta hai.

#### 4. 🧠 Zaroorat Kyun Hai?
Ye vulnerability bahut common hai, khaas kar un frameworks mein jo auto-binding karte hain (jaise Spring, Rails, Django REST Framework). Iska impact high ho sakta hai – attacker khud ko admin bana sakta hai, apna balance badha sakta hai, kisi aur ka password change kar sakta hai, etc.

#### 5. 🔍 Visual - Screen Par Kya Dikhega
Aap ek normal request dekhte hain:
```
POST /api/user/update
{
  "name": "Aman",
  "email": "aman@example.com"
}
```
Aap isme extra properties add karte hain:
```
{
  "name": "Aman",
  "email": "aman@example.com",
  "isAdmin": true,
  "balance": 99999,
  "role": "superuser"
}
```
Agar response mein kuch nahi badla, ya fir updated user ka data aaye jisme `isAdmin: true` dikhe, to mass assignment vulnerable hai.

#### 6. ⚙️ Under the Hood
Framework ka code kuch is tarah ho sakta hai:
```python
class User(models.Model):
    name = models.CharField()
    email = models.EmailField()
    is_admin = models.BooleanField(default=False)

@app.route('/api/user/update', methods=['POST'])
def update_user():
    user = get_current_user(request)
    data = request.json
    # Directly update user object with request data - MASS ASSIGNMENT VULNERABLE!
    for key, value in data.items():
        setattr(user, key, value)
    user.save()
    return user
```
Yahan saari incoming properties ko blindly user object par set kar diya gaya. Agar attacker `is_admin: true` bhej de, to wo admin ban jayega.

#### 7. 💻 Hands-On Step-by-Step
1. Kisi bhi request ko intercept karo jisme data bheja ja raha ho (POST, PUT, PATCH).
2. Request body mein **extra properties** add karo jo sensitive ho sakti hain. Common fields:
   - `isAdmin`, `admin`, `role`, `user_type`, `permissions`
   - `balance`, `credit`, `wallet`
   - `verified`, `email_verified`, `phone_verified`
   - `password`, `pass`, `pwd` (agar password change ho sakta hai to)
   - `status`, `active`
   - `group`, `team`
   - `owner_id`, `user_id` (agar kisi aur ka data claim kar sakte ho)
3. **Nested JSON** bhi try karo:
   ```json
   {
     "user": {
       "name": "Aman",
       "settings": {
         "isAdmin": true
       }
     }
   }
   ```
4. **HTTP Verb Tampering**: Check karo ki kaunse methods allowed hain. Jaise agar `POST` par update hota hai, to `PUT`, `PATCH` bhi try karo.
5. Response dekho – agar 200 OK aata hai, aur server ne extra properties accept kar li, to vulnerable hai. Agar error aata hai jaise "Unknown field", to probably safe hai (par pura confirm nahi).
6. **Excessive Data Exposure** bhi check karo: response mein koi sensitive field aa raha hai jo UI mein nahi dikh raha? Jaise server bhej raha hai `"mobile": "9876543210"` lekin UI mein sirf last 4 digits dikha raha hai. Iska matlab data leak ho raha hai aur mass assignment ke liye bhi field exist karti hai.

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success**: Request accepted (200 OK) aur property update ho gayi. Agar `isAdmin` true kiya to ab admin access milna chahiye.
- **Failure**: 400 Bad Request – "Unknown field", "Invalid parameter", "isAdmin not allowed". Ya phir server ignore kar de aur property update na ho (jaise response mein `isAdmin` false hi rahe).

#### 9. ⚖️ Comparison (Mass Assignment vs Excessive Data Exposure)
| **Mass Assignment** | **Excessive Data Exposure** |
|----------------------|-----------------------------|
| Attacker *sends* extra properties to modify them. | Server *returns* extra properties in response, jo client ko nahi dikhni chahiye. |
| Active attack – attacker changes data. | Passive leak – server unintentionally exposes data. |
| Fix: whitelist allowed fields. | Fix: filter response fields. |

#### 10. 🚫 Common Mistakes
- Sirf JSON mein top-level properties try karna, nested JSON ignore karna.
- Sirf boolean fields (`isAdmin`) try karna, numeric fields (`balance`) na try karna.
- Sirf `POST` par try karna, `PUT/PATCH` bhool jana.
- Excessive data exposure ko mass assignment ka sign na samajhna – agar response mein sensitive field aa raha hai, to wo mass assignment ke liye bhi candidate ho sakta hai.

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Mere framework mein mass assignment protection hai, to safe hoon?"**
  Kya wo protection by default enabled hai? Kya aapne `protected_attributes` ya `attr_accessible` sahi set kiye hain? Manual testing karo – koi na koi field ho sakti hai jo unprotected reh gayi.
- **"Response mein extra fields aa rahe hain, to mass assignment bhi ho sakta hai?"**
  Hamesha nahi, lekin possibility hai. Response mein fields ka matlab hai ki wo model mein exist karte hain, to agar request mein bhejo to server accept kar sakta hai. Isliye try karna chahiye.

#### 12. 🌍 Real-World Use Case
Github par ek bug aaya tha jahan users apne profile mein `plan` field bhej kar apne account ko free se paid me upgrade kar sakte the. `plan` field normally UI mein nahi tha, lekin API request mein bhejne par server ne maan liya. Isse kisi ko bhi free me private repos mil gaye.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
[Attacker] --> POST /api/user/update { "name":"Aman", "isAdmin":true }
   |
   v
[Server] --> Gets data, loops over all keys
   |
   v
[Database] --> UPDATE users SET name='Aman', isAdmin=true WHERE id=123;
   |
   v
[Attacker] now has isAdmin=true
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Burp Intruder** se common field names ki wordlist fuzz karo (`mass-assignment-wordlist`).
- **Param Miner** extension bhi useful hai.
- Pehle server ke response mein dekho ki kaunse fields aa rahe hain (excessive data exposure). Un fields ko request mein bhej kar dekho.
- JSON mein nesting ko explore karo – kai baar `user[isAdmin]` ya `settings.isAdmin` kaam karta hai.
- **Different HTTP methods** – kai baar `PATCH` vulnerable hota hai jab `POST` secure ho.
- **Automated tools** ki madad lo, par manual fuzzing bhi karo.

#### 15. ❓ FAQ (Interview Q&A)
1. **Q:** Mass Assignment se kaise bacha ja sakta hai?
   **A:** Whitelist approach use karo – explicitly define konse fields update karne ki anumati hai. Blacklist mat karo, kyunki naye fields add hote rahenge.
2. **Q:** Kya mass assignment sirf JSON mein hota hai?
   **A:** Nahi, XML, form-data, kisi bhi format mein ho sakta hai agar server data ko directly bind kar raha ho.
3. **Q:** `isAdmin` field try kiya to 400 aaya, lekin `role` try kiya to 200 aaya – ye kaise possible hai?
   **A:** Server ne `isAdmin` ko protected kar rakha hai, lekin `role` ko whitelist mein include kar liya. Isliye alag-alag fields alag response de sakte hain.
4. **Q:** Excessive data exposure ka mass assignment se kya relation hai?
   **A:** Agar server response mein sensitive fields bhej raha hai, to wo fields model mein exist karte hain. Unhe request mein bhej kar mass assignment try karna chahiye.
5. **Q:** Kya mass assignment GET requests mein ho sakta hai?
   **A:** GET mein body nahi hoti, to mass assignment generally POST/PUT/PATCH mein hota hai. Lekin agar server query parameters ko bhi bind kar raha ho, to ho sakta hai (rare).

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"Mass Assignment matlab server ne client ki bheji hui saari cheezein bina check kiye maan li, chahe wo fields sensitive kyun na hon."**

---

### Topic 3.3: BFLA (Broken Function Level Authorization)

---

#### 1. 🎯 Title
**Broken Function Level Authorization (BFLA)**

#### 2. 🐣 Samjhane ke liye (Analogy)
Ek office mein do tarah ke employees hain: **normal employees** aur **admins**. Admins ke paas special powers hain – wo kisi bhi employee ki file delete kar sakte hain, naye employees add kar sakte hain, etc. Office ka door normal employees ke liye sirf office area mein khulta hai, lekin admin ke room ka door alag hai. Ab agar kisi normal employee ko admin room ka door mil jaye (ya pata chal jaye ki wo bhi khul sakta hai), to wo andar ghus kar admin jaisa kaam kar sakta hai. BFLA yahi hai – ek low-privilege user un functions (endpoints) ko access kar leta hai jo sirf high-privilege users (jaise admin) ke liye hone chahiye.

#### 3. 📖 Technical Definition
BFLA tab hota hai jab API ke kuch endpoints (functions) sirf specific roles (jaise admin, manager) ke liye intended hote hain, par server ye verify nahi karta ki current user ke paas us function ko call karne ka permission hai ya nahi. Iski vajah se ek normal user admin-level actions perform kar sakta hai – jaise users ko delete karna, system settings change karna, etc.

#### 4. 🧠 Zaroorat Kyun Hai?
Ye vulnerability bhi OWASP API Top 10 mein #5 par aati hai (Broken Function Level Authorization). Iska impact critical ho sakta hai kyunki attacker poora system control kar sakta hai.

#### 5. 🔍 Visual - Screen Par Kya Dikhega
Maan lo aap normal user se login hain. Aap koshish karte hain:
```
GET /api/admin/users
```
Response:
```
401 Unauthorized
```
Ab aap method tamper karte hain:
```
POST /api/admin/users
```
Agar response 200 OK aata hai aur users ki list milti hai, to BFLA hai.

#### 6. ⚙️ Under the Hood
Server ka code kuch aisa ho sakta hai:
```python
@app.route('/api/admin/users')
def get_all_users():
    # Sirf authentication check, role check missing
    if not is_authenticated(request.headers['Authorization']):
        return 401
    users = db.query("SELECT * FROM users")
    return users
```
Yahan sirf authenticate check kiya, role nahi dekha ki user admin hai ya nahi. Isliye koi bhi authenticated user is endpoint ko call kar sakta hai.

Ya phir:
```python
@app.route('/api/admin/users', methods=['GET'])
def get_all_users():
    # GET ke liye role check hai
    check_admin()
    ...

@app.route('/api/admin/users', methods=['POST'])
def create_user():
    # POST ke liye role check karna bhool gaye
    # Sirf authenticate check
    ...
```
Is case mein method tampering se BFLA possible hai.

#### 7. 💻 Hands-On Step-by-Step
1. Sabse pehle, **API documentation** ya reconnaissance se admin endpoints ki list banao. Common patterns:
   - `/admin`, `/api/admin`, `/v1/admin`
   - `/internal`, `/private`, `/management`
   - `/users/delete`, `/users/create` jaisi actions jo sensitive hon.
2. Ek low-privilege user se login karo (jo admin na ho).
3. In endpoints par request bhejo different HTTP methods ke saath:
   - `GET /api/admin/users`
   - `POST /api/admin/users` (kuch data ke saath)
   - `PUT /api/admin/users/123`
   - `DELETE /api/admin/users/123`
   - `PATCH /api/admin/users/123`
   - `OPTIONS /api/admin/users` (dekhne ke liye kaunse methods allowed hain)
4. Har method ke response dekho. Agar 200 OK aata hai, to BFLA mil gaya.
5. Agar 403/401 aata hai, toh koshish karo ki kya koi parameter change kar sakte ho? Jaise:
   - `GET /api/admin/getUser?id=123` – yahan `admin` path mein nahi hai, par function admin level ka ho sakta hai.
   - `POST /api/user/delete` – bina admin prefix ke, par delete ka action admin level ka ho sakta hai.
6. **Method tampering** ke alawa, **parameter tampering** bhi karo – jaise `role=admin` bhej kar dekh lo ki kya server role-based access allow karta hai.
7. **Forced browsing** – directly admin URLs hit karo jo hidden hon.

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success**: 200 OK ke saath admin-level response (e.g., all users list) ya successful action (e.g., user deleted).
- **Failure**: 401 Unauthorized, 403 Forbidden, 404 Not Found (agar endpoint hi exist na karta ho).

#### 9. ⚖️ Comparison (BOLA vs BFLA)
| **BOLA** | **BFLA** |
|----------|----------|
| Object level – ek specific resource (user, file) ko unauthorized access. | Function level – ek entire functionality (admin panel) ko unauthorized access. |
| "Mere ko doosre ka data de do." | "Mujhe admin wala button dabane do." |
| Impact: data leak/modification of specific object. | Impact: full system compromise, privilege escalation. |

#### 10. 🚫 Common Mistakes
- Sirf GET methods par focus karna, POST/PUT/DELETE ko ignore karna.
- Sirf obvious admin paths (`/admin`) try karna, non-standard paths miss karna.
- Authentication ke baare mein sochna par authorization bhool jana.
- Role-based access sirf UI mein implement karna, API par nahi.

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Mere API mein role-based access hai, to sab safe hai?"**
  Kya tumne har endpoint par role check kiya hai? Kya koi endpoint aisa hai jo sirf isLiye safe hai kyunki uska naam admin jaisa nahi lagta, par wo admin-level kaam karta hai? Jaise `/api/users/deleteAll` – ye bhi BFLA ka candidate hai.
- **"Admin endpoints hidden hain, to attacker ko kaise pata chalega?"**
  Attacker API documentation padh sakta hai, ya JS files mein URLs search kar sakta hai, ya common patterns fuzz kar sakta hai. Hidden ka matlab secure nahi.

#### 12. 🌍 Real-World Use Case
Tesla ke bug bounty program mein ek researcher ne BFLA paya. Usne dekha ki `/api/vehicle/config` endpoint normal user se bhi accessible tha, jo ki vehicle ki advanced configuration change kar sakta tha (jo sirf service center ko karna chahiye). Isse wo kisi bhi Tesla car ki settings change kar sakta tha. Tesla ne turant fix kiya aur researcher ko bounty diya.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
[Attacker (normal user)] --> POST /api/admin/deleteUser?id=456
   |
   v
[Server] --> Check token? Valid (user 123). Role check? Missing.
   |
   v
[Database] --> DELETE FROM users WHERE id=456;
   |
   v
[Attacker] --> User 456 deleted successfully.
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Directory brute forcing** karo common admin paths ke liye (use tools like dirsearch, ffuf, Burp Intruder).
- **HTTP methods** ka pura set test karo – har endpoint ke liye `GET, POST, PUT, DELETE, PATCH, OPTIONS` try karo.
- **Parameter pollution** – agar `/api/admin/users` blocked hai, to try `/api/admin/users?` ya `/api//admin/users` (path normalization).
- **Role headers** – kabhi kabhi server `X-Role: admin` header check karta hai. Use bhi modify karo.
- **Check for IDOR in functions** – jaise `POST /api/user/delete` bina role check ke, lekin body mein `user_id` daal kar kisi aur ko delete karna – wo BOLA + BFLA mix ho sakta hai.

#### 15. ❓ FAQ (Interview Q&A)
1. **Q:** BFLA aur BOLA mein kya antar hai?
   **A:** BOLA object-level authorization hai – ek specific resource par unauthorized access. BFLA function-level authorization hai – ek poori functionality par unauthorized access, jo aksar role-based hoti hai.
2. **Q:** BFLA ko kaise prevent karein?
   **A:** Har endpoint par role-based access control (RBAC) implement karo. Sirf UI hide karna kaafi nahi, har API request mein check karo ki user ke paas required role hai ya nahi.
3. **Q:** Method tampering se BFLA kaise hota hai?
   **A:** Agar admin endpoint sirf GET ke liye protected ho, par POST ke liye role check bhool gaye hain, to attacker POST request bhej kar admin action perform kar sakta hai.
4. **Q:** Kya BFLA sirf admin endpoints tak limited hai?
   **A:** Nahi, koi bhi function jo higher privilege require karta hai, BFLA ka candidate hai. Jaise manager level functions, support team functions, etc.
5. **Q:** BFLA testing ke liye kaunse tools use kar sakte hain?
   **A:** Burp Suite (Intruder, Repeater), OWASP ZAP, ffuf for directory brute force, Postman for manual testing.

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"BFLA matlab low-privilege user ne high-privilege wala button daba diya, kyunki server ne role check karna bhool gaya."**

---

========================================================================================

