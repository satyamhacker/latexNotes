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
