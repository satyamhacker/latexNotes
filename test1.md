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
