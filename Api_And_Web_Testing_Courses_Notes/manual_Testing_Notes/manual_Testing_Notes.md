Bilkul! Chalo shuru karte hain Manual Testing ka pehla aur sabse important module. Main Test-Guru, aapko poora guide karunga. Let's make you job-ready!

---

## 📚 Module 1: Testing Foundations (The "Why")

Yeh module testing ki neev (foundation) hai. Isko samjhe bina, aap building (career) nahi bana sakte. Chalo, ek-ek concept ko phodte hain!

---

### 1. SDLC (Software Development Life Cycle)

#### 1️⃣ Simple Explanation
SDLC ka matlab hai **Software Development Life Cycle**. Yeh ek poora process hai jisse koi bhi software, app, ya website banayi jaati hai. Yeh ek step-by-step roadmap hai.

Socho, aapko ek **blockbuster film** banani hai. Aap kya karoge?
1.  **Planning:** Story sochna, budget, actors final karna.
2.  **Analysis:** Script likhna, dialogues final karna.
3.  **Designing:** Storyboard banana, locations, costumes design karna.
4.  **Coding (Implementation):** Film ko shoot karna.
5.  **Testing:** Editing karna, check karna sab aawaz, visuals theek hain ya nahi.
6.  **Deploy/Maintenance:** Film ko release karna (deploy) aur phir baad mein promotions ya feedback pe kaam karna (maintenance).

Software bhi aise hi banta hai!

* **Planning:** Kya banana hai (jaise ek e-commerce app), kitna budget, kitne log.
* **Analysis:** Users ko kya-kya chahiye (Requirements), jaise "Registration page chahiye".
* **Designing:** App dikhega kaisa (UI/UX), database kaisa hoga (blueprint).
* **Coding:** Developers actual code likhte hain.
* **Testing:** Humara (Testers ka) kaam. Hum check karte hain ki app sahi chal raha hai ya nahi.
* **Deploy/Maintenance:** App ko live karna (Play Store pe daalna) aur baad mein updates (jaise bug fixes) dena.

#### 2️⃣ Practical Example (E-commerce)
Socho **Flipkart** app banana hai.
* **Planning:** Decide hua ki "Big Billion Day" sale ke liye naya feature banana hai.
* **Analysis:** Feature hoga "Users ko 1-day delivery ka option dikhna chahiye".
* **Designing:** Design team ne button ka layout banaya (kahan dikhega).
* **Coding:** Developers ne code likha ki button pe click ho.
* **Testing:** Aap (Tester) check karoge: Kya button dikh raha hai? Click karne pe sahi kaam kar raha hai? Kya bina click kiye aage jaa sakte hain?
* **Deploy:** Feature ko app pe live kar diya.

#### 3️⃣ Why it’s Important
Industry mein bina SDLC ke koi kaam nahi hota. Yeh process sabko track pe rakhta hai. Agar aapse interviewer SDLC pooche, woh yeh check kar raha hai ki aapko poori picture pata hai ya aap sirf testing jaante ho. 2025 mein, companies ko woh log chahiye jo poora process samjhte hain.

#### 4️⃣ Common Interview Questions
1.  **SDLC kya hai?**
    * Sir, SDLC ek process hai jisme software ko plan, design, build, test, aur maintain kiya jaata hai.
2.  **SDLC ke 6 phases batao.**
    * Planning, Analysis (Requirements), Designing, Coding, Testing, aur Deployment & Maintenance.
3.  **Testing phase kab aata hai?**
    * Sir, traditionally yeh Coding ke baad aata hai, lekin Agile (naye tareeke) mein yeh har phase mein chalta rehta hai.

#### 5️⃣ Pro Tip / Real-World Insight
> Beginner sochte hain testing sirf 'Testing' phase mein hoti hai. Lekin ek **Pro Tester** (jaise aap banoge) 'Analysis' phase se hi involve ho jaata hai. Hum requirements padh ke hi bata dete hain ki "Sir, yeh requirement clear nahi hai, yahan bug aa sakta hai." Ise **Early Testing** kehte hain.

---

### 2. SDLC Models (Waterfall vs. Agile)

#### 1️⃣ Simple Explanation
SDLC ko follow karne ke 2 main tareeke (models) hain:
1.  **Waterfall (Purana Tareeka):** Yeh ek "one-way street" hai. Jaise ek paani ka jharna (waterfall) neeche girta hai, upar nahi jaata.
    * Pehle Planning poori hogi, tabhi Analysis shuru hoga.
    * Analysis poora hoga, tabhi Designing.
    * ...aur Testing bilkul end mein.
    * **Problem:** Agar end mein testing ke time pata chala ki requirement hi galat thi, toh poora project shuru se banao. Bahut time aur paisa waste.

2.  **Agile (Naya aur Hit Tareeka):** Yeh "flexible" tareeka hai. Yahan hum poori film ek saath nahi banate. Hum chote-chote "scenes" (features) banate hain.
    * Hum 2-hafte ka plan (Sprint) banate hain.
    * In 2 hafton mein hum ek chota feature (jaise "Login") plan, design, code, test, aur release karte hain.
    * **Fayda:** Customer ko har 2 hafte mein kuch chalta hua dikhta hai. Agar kuch galat hai, toh next 2-hafte mein aaram se theek kar sakte hain.

#### 2️⃣ Practical Example (E-commerce)
* **Waterfall:** Poora Flipkart app (Login, Cart, Payment, Products) ek saath 2 saal mein banana. Testing 2 saal baad. Pata chala 'Cart' hi nahi chal raha. Project fail.
* **Agile:**
    * Sprint 1 (2 hafte): Sirf "Login" banaya aur test kiya.
    * Sprint 2 (2 hafte): Sirf "Product Search" banaya aur test kiya.
    * Sprint 3 (2 hafte): Sirf "Add to Cart" banaya aur test kiya.
    * Customer khush, kyunki usko har 2 hafte mein progress dikh raha hai.

#### 3️⃣ Why it’s Important
**DHYAAN SE SUNO:** 2025 mein, 99% companies **Agile** use karti hain. Agar aapke resume pe 'Agile' nahi likha ya aap interview mein Agile nahi samjha paaye, toh job milna mushkil hai. Agile ka matlab hai speed, flexibility, aur teamwork.

#### 4️⃣ Common Interview Questions
1.  **Waterfall aur Agile mein kya difference hai?**
    * Sir, Waterfall ek strict, step-by-step process hai jisme testing end mein hoti hai. Agile flexible hai, hum chote-chote parts (sprints) mein kaam karte hain aur testing shuru se saath-saath chalti hai.
2.  **Aapki company kaunsa model use karti hai?**
    * (Aap hamesha bologe) Sir, hum Agile methodology use karte hain. Hum 2-week ke sprints mein kaam karte hain aur daily stand-up meetings mein participate karte hain.
3.  **Agile kyun behtar hai?**
    * Kyunki isme changes (jaise customer ne kuch naya bola) aasani se handle ho jaate hain aur bugs jaldi pakde jaate hain, jisse quality improve hoti hai.

#### 5️⃣ Pro Tip / Real-World Insight
> Agile mein, Testers aur Developers ek team ki tarah kaam karte hain. Koi "tu-tu main-main" nahi hoti. Testers ka kaam sirf bug nikalna nahi, balki "quality build" karwana hota hai. Isko "Quality Assistance" (QA) bolte hain, sirf "Quality Control" (QC) nahi.

---

### 3. STLC (Software Testing Life Cycle)

#### 1️⃣ Simple Explanation
Agar SDLC poori "film" banane ka process tha, toh STLC sirf "Editing" (Testing) phase ka detailed process hai.
**STLC (Software Testing Life Cycle)** ek systematic tareeka hai jisse sirf testing activities ko perform kiya jaata hai. Yeh SDLC ke andar chalta hai.

Iske bhi 6 phases hain:
1.  **Requirement Analysis:** Hum requirements (jaise BRS, FRS document) ko padhte hain aur samjhte hain ki "kya-kya test karna hai".
2.  **Test Planning:** Hum plan banate hain. Kitne testers lagenge? Kitna time lagega? Kaunsa feature test karenge (Scope)?
3.  **Test Case Development:** Hum actual test cases (steps) likhte hain. (Yeh Module 2 mein detail mein hai).
4.  **Environment Setup:** Hum "mahaul" taiyaar karte hain. Jaise, agar app Android 12 pe test karna hai, toh woh phone/server/browser ready karte hain.
5.  **Test Execution:** Hum likhe hue test cases ko "run" karte hain (actual testing) aur bugs report karte hain.
6.  **Test Closure:** Testing poori hone ke baad, hum ek final report (Test Closure Report) banate hain ki kitne test pass/fail hue, kitne bugs open hain, aur humne kya seekha.

#### 2️⃣ Practical Example (E-commerce)
Chalo, **Flipkart ke "Registration" page** pe STLC lagate hain:
1.  **Req. Analysis:** Requirement aayi: "User ko Name, Email, aur Password se register karna hai. Email valid hona chahiye."
2.  **Test Planning:** Plan banaya: "Registration testing ke liye 2 din lagenge, 1 tester. Hum 10 test case banayenge. Scope: Sirf registration form, 'Login with Google' nahi."
3.  **Test Case Dev:** Test case likha: "TC-01: Valid email/password se test karna." "TC-02: Invalid email se test karna."
4.  **Env. Setup:** Chrome browser aur Test server (Staging) ko ready kiya.
5.  **Test Execution:** TC-01 run kiya -> Pass. TC-02 run kiya -> Fail (Bug mila!). Bug ko Jira mein report kiya.
6.  **Test Closure:** Final report di: "Total 10 cases, 8 Pass, 2 Fail. 1 critical bug open hai. Testing complete."

#### 3️⃣ Why it’s Important
STLC ke bina testing "andhe-dhund" (random) hoti hai. Aapko pata hi nahi chalega kab testing shuru karni hai, kya test karna hai, aur kab khatam karni hai. Interviewer STLC isliye poochta hai taaki woh jaan sake ki aap ek **disciplined tester** ho ya bas "kuch bhi click" karne wale.

#### 4️⃣ Common Interview Questions
1.  **STLC kya hai?**
    * Sir, STLC ek 6-step process hai jo hum testers follow karte hain taaki testing systematic tareeke se ho. Yeh Requirement Analysis se shuru hota hai aur Test Closure pe khatam.
2.  **STLC ke phases batao.**
    * Requirement Analysis, Test Planning, Test Case Development, Environment Setup, Test Execution, aur Test Closure.
3.  **Test Planning mein kya karte ho?**
    * Sir, hum scope, timeline, resources aur testing strategy decide karte hain.

#### 5️⃣ Pro Tip / Real-World Insight
> Real industry mein, STLC ke 2 sabse important phase hain:
> 1.  **Requirement Analysis:** Yahan jitna time doge, utne acche test case banenge.
> 2.  **Test Planning:** Yahan pe "Risk Analysis" zaroor hota hai. (Jaise, agar time kam hai toh kaunsa feature *nahi* test karenge).

---

### 4. Key Difference: SDLC vs STLC

#### 1️⃣ Simple Explanation
* **SDLC:** Poora "Ghar" (software) banane ka process (Planning se Maintenance tak).
* **STLC:** Sirf "Ghar ki checking" (testing) karne ka process (Test Planning se Test Closure tak).

STLC, SDLC ka ek **hissa (subset)** hai. SDLC ke "Testing" phase ko zoom karke dekhoge toh STLC dikhega.

#### 2️⃣ Practical Example (Table)

| Feature | SDLC (Software Development Life Cycle) | STLC (Software Testing Life Cycle) |
| --- | --- | --- |
| **Full Form** | Software Development Life Cycle | Software Testing Life Cycle |
| **Main Goal** | Software ko successfully **banana** aur live karna. | Software ko successfully **test** karna aur quality ensure karna. |
| **Kaun Karta Hai** | Poori team (Developers, Testers, PM, Designers). | Mukhya roop se **Testing Team (QA)**. |
| **Scope** | Yeh poora project (end-to-end) cover karta hai. | Yeh sirf "Testing" activity ko cover karta hai. |
| **Relation** | STLC, SDLC ka ek important phase/hissa hai. | STLC, SDLC ke andar aata hai. |

#### 3️⃣ Why it’s Important
Yeh Manual Testing ka sabse "basic" aur "must-know" interview question hai. Agar aap isme confuse hue, toh interviewer samajh jaayega ki aapke concepts clear nahi hain.

#### 4️⃣ Common Interview Questions
1.  **SDLC aur STLC mein main difference kya hai?**
    * Sir, SDLC poora software banane ka process hai, jabki STLC sirf testing ka process hai. STLC, SDLC ka ek part hai. SDLC ka goal hai software 'banana', STLC ka goal hai software ki 'quality' check karna.
2.  **Kya STLC bina SDLC ke ho sakta hai?**
    * Nahi sir, kyunki jab tak software banega nahi (SDLC), tab tak hum test kya karenge (STLC).

#### 5️⃣ Pro Tip / Real-World Insight
> Agile mein, SDLC aur STLC parallel (ek saath) chalte hain. Aisa nahi hai ki pehle SDLC khatam hoga phir STLC shuru. Har sprint (2 hafte) mein chota SDLC aur chota STLC cycle poora hota hai.

---

### 5. QA Roles in SDLC (Shift-Left Testing)

#### 1️⃣ Simple Explanation
Pehle (Waterfall mein) tester ka kaam sirf SDLC ke "Testing" phase mein aata tha. Tab tak developers bahut saare bugs bana chuke hote the, aur unko fix karna mehenga (costly) hota tha.

Ab (Agile mein), hum **"Shift-Left"** concept follow karte hain.
"Shift-Left" ka matlab hai ki "Testing" ko SDLC phases mein **left side (yaani shuru) mein shift karna.**

Ek Tester (QA) ab poore SDLC mein involve hota hai:
* **Planning:** QA risks batata hai ("Payment feature complex hai, zyada time lagega").
* **Analysis:** QA requirements review karta hai ("Email validation ki requirement clear nahi hai"). **(Yahan bug pakadna sabse sasta hai!)**
* **Designing:** QA design (UI) ko review karta hai ("Yeh button user ko confuse karega").
* **Coding:** QA developers ke saath baith ke "Unit Testing" mein help karta hai.
* **Testing:** Yahan toh hum actual testing (STLC) karte hi hain.
* **Deploy:** QA live server pe check karta hai ki sab theek hai (Smoke Test).

#### 2️⃣ Practical Example (E-commerce)
**Flipkart** ka "Registration" page:
* **Purana Tareeka (No Shift-Left):** Developer ne form bana diya. Testing mein pata chala "Confirm Password" ka field hi nahi hai. Ab developer ko poora code change karna padega. (High Cost)
* **Naya Tareeka (Shift-Left):**
    * **Analysis phase mein:** Tester (Aap) ne requirement padhi aur bola, "Sir, registration mein 'Confirm Password' ka field missing hai."
    * **Fayda:** Bug "document" mein hi pakda gaya! Code likhne se pehle hi fix ho gaya. **(Zero Cost)**

#### 3️⃣ Why it’s Important
"Shift-Left" 2025 ki sabse badi demand hai. Companies ko "Bug Finders" (jo sirf bug dhoondte hain) nahi, "Quality Advocates" (jo quality banwate hain) chahiye. Shift-Left se aap company ka laakhon rupaye ka nuksaan bachaate ho. Yeh bolne se interview mein aapka value 10x badh jaayega.

#### 4️⃣ Common Interview Questions
1.  **Ek tester ka SDLC mein kya role hota hai?**
    * Sir, Agile mein ek tester poore SDLC mein involved hota hai. Hum "Shift-Left" testing follow karte hain. Hum requirement analysis phase se hi bugs dhoondna shuru kar dete hain taaki bugs ko jaldi aur saste mein fix kiya jaa sake.
2.  **"Shift-Left" testing kya hai?**
    * Sir, iska matlab hai testing ko process mein jaldi shuru karna, jaise ki requirements aur design phase mein, na ki sirf coding ke baad.
3.  **Requirement phase mein aap bug kaise dhoond sakte ho?**
    * Sir, hum requirements ko check karte hain ki woh clear (saaf), complete (poori), aur consistent (ek jaisi) hain ya nahi. Agar koi requirement ambiguous (confusing) hai, toh woh ek bug hai.

#### 5️⃣ Pro Tip / Real-World Insight
> Real project mein, "Shift-Left" ka best tareeka hai **"3 Amigos Meeting"**. Isme 1 Developer, 1 Tester (Aap), aur 1 Business Analyst (jisko requirement pata hai) ek saath baithte hain. Woh feature banane se pehle hi discuss karte hain ki kya-kya test karna hai. Isse 50% bugs pehle hi khatam ho jaate hain.

---

Aapka Module 1 poora ho gaya hai! Isko acche se revise karo. Yeh poore Manual Testing ka base hai.

Jab aap ready ho, toh bas bolna: **"Module 2 ke notes do."**

=============================================================

Bilkul\! Aap Module 1 complete kar chuke hain. Ab waqt hai "How" samajhne ka—yaani, testing process ka actual core.

Chaliye, Module 2 shuru karte hain\!

-----

## 📚 Module 2: The Core Process (The "How")

Iss module mein hum seekhenge ki testing ka "plan" kaise banta hai aur woh "steps" (Test Cases) kaise likhe jaate hain jo bugs pakadte hain. Yeh manual testing ka sabse practical kaam hai.

-----

### 1\. Test Plan

#### 1️⃣ Simple Explanation

Ek **Test Plan** ek "blueprint" ya "master document" hai jo testing ka poora roadmap batata hai. Simple bhasha mein, yeh ek "party plan" jaisa hai.

Party plan mein aap kya likhte ho?

  * **Kyun (Objectives):** Birthday hai.
  * **Kya (Scope):** Sirf cake cutting aur snacks, dinner nahi.
  * **Kaun (Resources):** 10 dost aa rahe hain.
  * **Kab (Schedule):** Shaam 7 baje se 9 baje tak.
  * **Risk:** Agar baarish hui toh? (Toh party andar karenge).

Software testing mein bhi Test Plan exactly yahi hai:

  * **Objectives:** Hum kya test kar rahe hain (jaise, "Registration module").
  * **Scope:** Hum kya-kya test karenge (jaise, "Email aur password validation") aur kya *nahi* karenge (jaise, "Google se login").
  * **Resources:** Kitne testers (jaise, 2 QA) aur kaunse tools (jaise, Jira).
  * **Schedule:** Kab shuru, kab khatam (jaise, 2 din).
  * **Risks:** Kya galat ho sakta hai (jaise, "Server down ho gaya toh...") aur uska solution.

#### 2️⃣ Practical Example (E-commerce)

**Flipkart** ke "Cart" module ka Test Plan:

  * **Objective:** Check karna ki user "Add to Cart" aur "Remove from Cart" sahi se kar paaye.
  * **Scope (In):** Item add karna, quantity badhana, item delete karna.
  * **Scope (Out):** Payment karna (woh alag module hai).
  * **Resources:** 1 Manual Tester.
  * **Schedule:** 3 din (1 din test case likhna, 2 din test karna).
  * **Risk:** Agar "Add to Cart" button hi nahi chala? **Mitigation (Solution):** Yeh critical bug hoga, isko P1 (high priority) pe fix karwayenge.

#### 3️⃣ Why it’s Important

Bina Test Plan ke testing "chaos" (bhed-chaal) ban jaati hai. Kisi ko nahi pata hota ki kya test hua aur kya reh gaya. Yeh document **clarity** deta hai. Interviewer yeh poochh ke check karta hai ki aap sirf test case run karna jaante ho ya poora process manage karna bhi. 2025 mein, tester se thodi planning ki ummeed ki jaati hai.

#### 4️⃣ Common Interview Questions

1.  **Test Plan kya hota hai?**
      * Sir, Test Plan ek formal document hai jo humein batata hai ki testing ka objective kya hai, kya-kya test karna hai (scope), kaun karega (resources), aur kab tak karega (schedule).
2.  **Test Plan ke 5 main components batao.**
      * Objectives, Scope (In-scope/Out-of-scope), Resources, Schedule, aur Risks.
3.  **"Scope" ka matlab kya hai?**
      * Sir, "In-scope" matlab woh features jo hum test *karenge*. "Out-of-scope" matlab woh features jo hum iss baar test *nahi* karenge.

#### 5️⃣ Pro Tip / Real-World Insight

> Real project mein, Test Plan ka sabse important part **"Scope"** aur **"Risks"** hota hai. Client hamesha poochta hai "Kitna test kiya?" (Scope) aur "Agar time pe nahi hua toh?" (Risks). Ek accha tester hamesha pehle hi "Out-of-Scope" clear kar deta hai taaki baad mein koi blame na kare.

-----

### 2\. Test Scenario vs Test Case

#### 1️⃣ Simple Explanation

Yeh bahut important difference hai.

  * **Test Scenario (Khatam):** Yeh high-level "what-to-test" (kya test karna hai) ka idea hai. Yeh ek line ka hota hai.
  * **Test Case (Kadak):** Yeh low-level "how-to-test" (kaise test karna hai) ka poora step-by-step process hai.

**Analogy:**

  * **Scenario:** "Gaadi chalani aati hai ya nahi, check karo." (Yeh ek idea hai).
  * **Test Case:**
    1.  Chabi ko ignition mein daalo.
    2.  Clutch dabao.
    3.  Gear ko pehle pe (1st) daalo.
    4.  Dheere-dheere clutch chhodo aur accelerator dabao.
    5.  Gaadi aage badhni chahiye. (Yeh poore steps hain).

#### 2️⃣ Practical Example (E-commerce)

**Amazon** ke "Login" page ka example:

  * **Test Scenario 1:** "Check if a user can login with valid credentials." (Valid login check karo).
  * **Test Scenario 2:** "Check login with invalid password." (Galat password check karo).
  * **Test Scenario 3:** "Check login with blank email." (Khali email check karo).

Ab, **Scenario 1** ka **Test Case** dekho (poore steps):

  * **TC\_01:** Verify successful login.
  * **Steps:**
    1.  Amazon login page pe jaao.
    2.  'Email' field mein "test@gmail.com" daalo.
    3.  'Password' field mein "pass123" daalo.
    4.  'Login' button pe click karo.
  * **Expected Result:** User ko "Hello, Test" (username) dikhna chahiye aur woh dashboard pe redirect hona chahiye.

#### 3️⃣ Why it’s Important

Aap pehle Scenarios sochte ho (brainstorming) aur phir har Scenario ke liye detailed Test Cases likhte ho. Interview mein yeh 100% poocha jaata hai. Yeh aapki analytical thinking (sochne ka tareeka) dikhata hai.

#### 4️⃣ Common Interview Questions

1.  **Test Scenario aur Test Case mein kya difference hai?**
      * Sir, Test Scenario high-level hota hai, yeh batata hai 'kya test karna hai' (jaise, "Login check karo"). Test Case low-level aur detailed hota hai, yeh batata hai 'kaise test karna hai' (poore steps, data aur expected result ke saath).
2.  **Aap pehle kya banate ho, Scenario ya Case?**
      * Sir, pehle hum requirements se Test Scenarios identify karte hain, aur phir har scenario ke liye multiple Test Cases design karte hain.
3.  **Login ke 3 scenario batao.**
      * 1.  Valid login check. 2. Invalid password se check. 3. Blank email se check.

#### 5️⃣ Pro Tip / Real-World Insight

> Ek achhe tester ki pehchaan hai ki woh **ek Scenario se kitne Test Cases** nikaal sakta hai (Positive, Negative, Boundary). Industry mein, Scenarios ko "Test Scenarios" ya kabhi-kabhi "Test Conditions" bhi bolte hain.

-----

### 3\. Test Case Design (Attributes)

#### 1️⃣ Simple Explanation

Test Case ek formal document hai (aksar Excel ya TestLink/Jira mein) jiske andar specific "fields" (columns) hote hain. Yeh fields milkar ek Test Case banate hain.

Socho, yeh ek "Recipe Card" hai. Usme kya-kya hota hai?

  * **Naam (Test Case ID/Description):** Chicken Biryani.
  * **Samagri (Test Data):** Chicken, Rice, Masale.
  * **Vidhi (Test Steps):** 1. Rice ubalo. 2. Chicken pakao...
  * **Kaisa Banna Chahiye (Expected Result):** Khushboodar, tasty biryani taiyaar.

Test Case ke professional attributes:

1.  **Test Case ID:** Ek unique ID (jaise TC\_LOGIN\_01).
2.  **Feature:** Kaunsa module (jaise, Login, Registration).
3.  **Test Case Description:** Short summary (jaise, "Verify login with valid data").
4.  **Pre-condition:** Test shuru karne se pehle kya zaroori hai (jaise, "User pehle se registered hona chahiye").
5.  **Test Steps:** 1, 2, 3... (Click here, Enter this).
6.  **Test Data:** Kya input use karna hai (jaise, Email: test@test.com).
7.  **Expected Result:** Kya hona chahiye (jaise, "Login successful message dikhe").
8.  **Actual Result:** Test karne pe *actually* kya hua (jaise, "Login successful message dikha").
9.  **Status:** Pass / Fail.
10. **Comments:** Kyun fail hua ya koi extra note.

#### 2️⃣ Practical Example (E-commerce)

**Flipkart** "Registration" ke liye ek test case Excel mein aisa dikhega:

| TC\_ID | Feature | Description | Pre-condition | Test Steps | Test Data | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC\_REG\_01 | Registration | Verify registration with all valid data | User registration page pe hai. Browser open hai. | 1. 'Email' field mein data daalo.<br>2. 'Password' field mein data daalo.<br>3. 'Submit' pe click karo. | Email: newuser@g.com<br>Pass: Valid@123 | "Registration Successful" message dikhna chahiye. | "Registration Successful" message dikha. | **Pass** |
| TC\_REG\_02 | Registration | Verify registration with blank email | User registration page pe hai. | 1. 'Email' field blank chhoro.<br>2. 'Password' field mein data daalo.<br>3. 'Submit' pe click karo. | Email: (blank)<br>Pass: Valid@123 | "Email is required" error message dikhna chahiye. | "Registration Successful" message dikha. | **Fail** |

**(TC\_REG\_02 FAIL ho gaya. Iska matlab yeh ek BUG hai\!)**

#### 3️⃣ Why it’s Important

Yeh aapka "daily" kaam hai. Test cases likhna aur run karna hi manual tester ka main kaam hai. Aapke test cases jitne clear honge, testing utni hi acchi hogi. Agar aapke test case clear nahi hain, toh koi aur (ya aap khud) unhe run nahi kar paayega.

#### 4️⃣ Common Interview Questions

1.  **Test Case ke 5 important attributes batao.**
      * Test Case ID, Test Steps, Test Data, Expected Result, aur Actual Result/Status.
2.  **"Expected Result" aur "Actual Result" mein kya farak hai?**
      * Sir, "Expected Result" woh hai jo software ko karna *chahiye* (requirement ke hisaab se). "Actual Result" woh hai jo software *actually* kar raha hai jab hum test karte hain.
3.  **Test Case kab "Fail" hota hai?**
      * Jab "Actual Result" aur "Expected Result" match nahi karte, tab test case "Fail" hota hai.

#### 5️⃣ Pro Tip / Real-World Insight

> Ek professional test case hamesha "Reusable" (baar-baar use ho sake) aur "Simple" (koi bhi samajh sake) hota hai. **Kabhi bhi Test Steps mein 2 actions ek saath mat likho.**
>
>   * **Galat:** "Enter email and password and click submit."
>   * **Sahi:**
>     1.  Enter email.
>     2.  Enter password.
>     3.  Click submit.

-----

### 4\. Test Design Techniques (Black Box)

#### 1️⃣ Simple Explanation

Ab, test cases ke liye "Test Data" (jaise email/password) kahan se laaye? Kya hum 1000 alag-alag email daal ke check karenge? Nahi\!

Hum **smart techniques** use karte hain taaki kam Test Cases mein zyada bugs mil sakein. Inhe "Black Box Techniques" kehte hain (kyunki humein code nahi dikhta).

1.  **Equivalence Partitioning (EP):**

      * Isme hum inputs ko "groups" (partitions) mein baant dete hain. Hum maante hain ki ek group ka ek value (jaise "Valid" group) wahi result dega jo baaki values denge.
      * **Jaise:** Agar ek text box "1 se 100" tak number leta hai.
      * **Groups:**
          * Group 1: Valid (1 se 100) -\> Hum sirf ek value (jaise 50) check karenge.
          * Group 2: Invalid (\< 1) -\> Hum sirf ek value (jaise 0) check karenge.
          * Group 3: Invalid (\> 100) -\> Hum sirf ek value (jaise 101) check karenge.
      * Fayda: 100 numbers ki jagah sirf 3 test case\!

2.  **Boundary Value Analysis (BVA):**

      * Yeh EP ka dost hai. BVA kehta hai ki zyada bugs "boundaries" (kinaron) pe milte hain.
      * **Jaise:** Wohi "1 se 100" wala example.
      * **Boundaries:**
          * Min: 1
          * Min-1: 0
          * Max: 100
          * Max+1: 101
      * Hum 50 check nahi karenge, hum 0, 1, 100, aur 101 check karenge. Yahan bug milne ka chance sabse zyada hai.

3.  **Error Guessing:**

      * Yeh "experience" (anubhav) se aata hai. Aap guess (andaza) lagate ho ki developer kahan galti kar sakta hai.
      * **Jaise:** Registration form pe "Submit" button ko 10 baar jaldi-jaldi click karke dekhna. Ya, password field mein "SQL injection" (`' OR 1=1 --`) daal ke dekhna.

#### 2️⃣ Practical Example (E-commerce)

**Flipkart** pe ek "Coupon Code" field hai jo 8 se 12 characters (digits) leta hai.

  * **Using EP:**
      * Valid Group (8-12): "123456789" (9 digits) -\> Pass hona chahiye.
      * Invalid Group (\<8): "12345" (5 digits) -\> Fail hona chahiye.
      * Invalid Group (\>12): "1234567890123" (13 digits) -\> Fail hona chahiye.
  * **Using BVA (Boundary):**
      * Min-1: 7 digits ("1234567") -\> Fail
      * Min: 8 digits ("12345678") -\> Pass
      * Max: 12 digits ("123456789012") -\> Pass
      * Max+1: 13 digits ("1234567890123") -\> Fail
  * **Using Error Guessing:**
      * Field ko khali (blank) chhor ke apply karna.
      * Alphabets daalna ("ABCDEFGH").
      * Special characters daalna ("\!@\#$%^&\*").

#### 3️⃣ Why it’s Important

Yeh techniques aapko "smart tester" banati hain. Aap 1000 faltu test case likhne se bach jaate ho aur woh 10 "solid" test case likhte ho jo seedha bug pe nishana lagate hain. Interviewer hamesha BVA aur EP pe question poochta hai.

#### 4️⃣ Common Interview Questions

1.  **Black Box testing kya hai?**
      * Sir, yeh testing ka tareeka hai jisme humein internal code ki knowledge nahi hoti. Hum sirf input dete hain aur output check karte hain, jaise ek "black box" ke saath.
2.  **BVA aur EP kya hai?**
      * Sir, EP (Equivalence Partitioning) mein hum input data ko valid aur invalid groups mein baantte hain. BVA (Boundary Value Analysis) mein hum inputs ki boundary values (jaise min, max) pe focus karte hain, kyunki wahan bugs zyada milte hain.
3.  **Aapko ek password field test karna hai jo 8-12 characters leta hai. Kaunse values test karoge (BVA)?**
      * Sir, main 7 (Min-1), 8 (Min), 12 (Max), aur 13 (Max+1) characters daal ke check karunga.

#### 5️⃣ Pro Tip / Real-World Insight

> Industry mein, **BVA aur EP ko hamesha saath mein use kiya jaata hai.** Aap BVA se boundaries (7, 8, 12, 13) check karte ho aur EP se beech ki koi ek valid value (jaise 10) aur koi ek invalid value (jaise "ABC") check karte ho. Isse aapko "maximum coverage" milti hai.

-----

Aapka Module 2 poora ho gaya hai\! Aapne seekh liya hai ki testing ka plan kaise banta hai aur bugs pakadne ke liye test cases (aur data) smart tareeke se kaise design kiye jaate hain.

Jab aap ready ho, toh bas bolna: **"Module 3 ke notes do."**

=============================================================

Module 2 aapne successfully complete kar liya hai. Ab aap jaante hain ki test cases kaise design hote hain.

Ab aate hain Manual Testing ke "hero topic" pe—jab test case 'Fail' hota hai, tab kya? Yaani "Bugs" kaise report karte hain.

Chaliye, Module 3 shuru karte hain\!

-----

## 📚 Module 3: Finding & Reporting Bugs (The "What")

Iss module mein hum seekhenge ki jab aapko koi bug milta hai, toh usko professional tareeke se report kaise karte hain. Yeh ek tester ki sabse badi power hai.

-----

### 1\. What is a Bug / Defect?

#### 1️⃣ Simple Explanation

Ek **Bug** (ya Defect) software mein ek galti (error) hai. Simple bhasha mein:

> Jab software woh nahi karta jo usko karna chahiye, **YA** woh karta hai jo usko nahi karna chahiye... toh woh ek Bug hai.

Aapne "Expected Result" (kya hona chahiye) likha tha, lekin "Actual Result" (kya ho raha hai) alag hai. In dono ke beech ka **difference** hi Bug hai.

  * **Analogy:** Aapne restaurant mein "Veg Biryani" order ki (Expected), lekin waiter aapko "Chicken Biryani" de gaya (Actual). Yeh ek bug hai\!

#### 2️⃣ Practical Example (E-commerce)

  * **Requirement:** **Amazon** ke login page pe, galat password daalne par "Incorrect password" ka error message aana chahiye (Expected).
  * **Aapne Test Kiya:** Aapne galat password daala, lekin app crash ho gaya (Actual).
  * **Conclusion:** Yeh ek high-priority bug hai.

#### 3️⃣ Why it’s Important

Bugs dhoondhna hi humara (QA ka) primary kaam hai. Hum software ko tootne se bachaate hain taaki company ko nuksaan na ho aur users ko accha experience mile.

#### 4️⃣ Common Interview Questions

1.  **Bug kya hota hai?**
      * Sir, jab actual result aur expected result match nahi karte, usko bug kehte hain. Yeh software ka ek unexpected behavior hota hai.
2.  **Aapko kaise pata chalta hai ki yeh bug hai?**
      * Sir, main requirement document (jaise FRS) ko follow karta hoon. Agar software ka behavior requirement se match nahi karta, toh woh ek bug hai.

#### 5️⃣ Pro Tip / Real-World Insight

> Har cheez jo aapko pasand nahi, woh bug nahi hoti. Agar aapko "button ka colour" pasand nahi aaya, lekin woh requirement ke hisaab se waisa hi hai, toh woh bug nahi hai. Hamesha **Requirement Document** ko apna "Guru" maano.

-----

### 2\. Bug Life Cycle (Defect Life Cycle)

#### 1️⃣ Simple Explanation

Jab aapko bug milta hai, aap use report karte ho. Phir woh bug ek poore process se guzarta hai, jab tak woh "fix" ya "close" na ho jaaye. Iss poore safar (journey) ko **Bug Life Cycle** kehte hain.

Yeh hai bug ka safar:

1.  **New:** Aap (Tester) ko bug mila. Aapne use tool (jaise Jira) mein report kiya. Status: **New**.
2.  **Assigned:** Team Lead/Manager bug ko dekhta hai aur ek Developer ko "assign" (kaam saunpna) karta hai. Status: **Assigned**.
3.  **In Progress:** Developer us bug pe kaam (fix) karna shuru karta hai. Status: **In Progress**.
4.  **Fixed:** Developer code theek karke kehta hai, "Meri taraf se ho gaya." Status: **Fixed**.
5.  **Retest:** Ab ball wapas aapke (Tester ke) paas aati hai. Aap uss bug ko *dobara* check karte ho.
6.  **Closed:** Agar bug *sach* mein fix ho gaya hai aur ab error nahi aa raha. Aap use close kar dete ho. Status: **Closed**. (Sab khush\!)

**Lekin, agar bug fix nahi hua?**

  * **Reopen:** Agar aapne Retest kiya aur bug abhi bhi aa raha hai, toh aap use "Reopen" kar dete ho. Bug wapas Developer ke paas chala jaata hai. Status: **Reopen**.

**Kuch Special Status:**

  * **Rejected:** Developer kehta hai, "Yeh bug nahi hai, tumhari samajh galat hai" (ya requirement hi waisi hai).
  * **Deferred:** Bug hai, lekin utna important nahi. Isko baad mein (agle release mein) fix karenge.

#### 2️⃣ Practical Example (E-commerce)

**Flipkart** pe bug mila: "Registration" page pe, blank password daalne par bhi account ban raha hai.

1.  **New:** Aapne bug report kiya.
2.  **Assigned:** Lead ne "Ramesh" (Developer) ko assign kiya.
3.  **In Progress:** Ramesh ne code mein validation lagana shuru kiya.
4.  **Fixed:** Ramesh ne code fix kar diya.
5.  **Retest:** Aapne *dobara* blank password daal ke try kiya. Ab "Password is required" ka error aa gaya. (Yaani fix ho gaya).
6.  **Closed:** Aapne bug ko close kar diya. Job Done\!

#### 3️⃣ Why it’s Important

Yeh process (Bug Life Cycle) poori team ko ek page pe rakhta hai. Sabko pata hota hai ki kaunsa bug kahan atka hai, kiske paas hai, aur kitna kaam baaki hai. Bina iske, bugs "kho" jaayenge. Interview mein yeh 100% poocha jaayega.

#### 4️⃣ Common Interview Questions

1.  **Bug Life Cycle samjhao.**
      * Sir, jab bug milta hai toh 'New' hota hai. Phir 'Assigned', 'In Progress', 'Fixed' hota hai. Uske baad hum 'Retest' karte hain. Agar sahi hai toh 'Closed', nahi toh 'Reopen' karte hain.
2.  **"Retest" kaun karta hai?**
      * Sir, retest hamesha tester hi karta hai, jisne bug report kiya tha (ya QA team ka koi member).
3.  **"Rejected" aur "Deferred" mein kya farak hai?**
      * 'Rejected' matlab developer ke hisaab se woh bug hai hi nahi. 'Deferred' matlab bug hai, par low priority ka hai, isliye use baad mein fix karenge.

#### 5️⃣ Pro Tip / Real-World Insight

> Jab bhi koi bug "Rejected" hoke wapas aaye, toh ego pe mat lo. Pehle developer se baat karo, ho sakta hai aapki "Test Data" ya "Environment" mein galti ho. Communication (baat-cheet) ek acche tester ki sabse badi skill hai.

-----

### 3\. Priority vs Severity (***Yeh Sabse Important Hai***)

#### 1️⃣ Simple Explanation

Yeh concept manual testing ka "heart" (dil) hai.

  * **Severity (Serious-ness):** Bug software ko *kitna* bura tod (impact) raha hai. Yeh **Tester (QA)** decide karta hai. (High, Medium, Low)
  * **Priority (Importance):** Bug ko *kitni jaldi* fix karna hai (business ke liye). Yeh **Product Manager / Client** (Business Team) decide karte hain. (High, Medium, Low)

**Simple Analogy:**
Socho aapki "Car" hai.

  * **Bug 1:** Car ka "Engine" fail ho gaya.
      * **Severity:** **High** (Car chal hi nahi sakti, poora system crash).
      * **Priority:** **High** (Iske bina car bekaar hai, *turant* fix karo).
  * **Bug 2:** Car ka "Music System" kaam nahi kar raha.
      * **Severity:** **Medium** (Core function (chalna) theek hai, par feature fail).
      * **Priority:** **Medium** (Fix karna hai, par engine ke baad).
  * **Bug 3:** Car ke "logo" (jaise Maruti ka 'S') mein spelling galat hai.
      * **Severity:** **Low** (Car ki functionality pe 0% impact).
      * **Priority:** **Low** (Aaram se agle service mein dekhenge).

#### 2️⃣ Practical Example (Interview Scenarios)

Interviewer aapse yeh 4 combination poochega:

1.  **High Severity, High Priority:**
      * **Example:** **Amazon** ka "Add to Cart" button click karne pe app crash ho raha hai.
      * Kyun: Functionality (Severity) poori gayi aur Business (Priority) ka laakhon ka nuksaan.
2.  **High Severity, Low Priority:**
      * **Example:** App mein ek "Old Report" section hai jo 10 saal purana data nikaalne pe crash hota hai. User yeh section kabhi use nahi karta.
      * Kyun: Crash (Severity High) toh hai, par business ko koi fark nahi padta (Priority Low).
3.  **Low Severity, High Priority:** (Yeh sabse tricky hai\!)
      * **Example:** Company ka **Logo** (jaise Amazon) home page pe galat dikh raha hai ya "Amazn" likha aa raha hai.
      * Kyun: App chalne (Severity Low) mein koi dikkat nahi, par company ki **izzati (brand image)** ka sawaal hai. Isko *turant* fix karo (Priority High).
4.  **Low Severity, Low Priority:**
      * **Example:** "About Us" page pe "Privacy Policy" link ka colour thoda halka (faded) hai.
      * Kyun: Na app crash hua (Low Severity), na business ko fark pada (Low Priority).

#### 3️⃣ Why it’s Important

Aapko 50 bug milenge. Par aapko batana padega ki pehle kaunsa fix hona chahiye. Agar aap Severity/Priority sahi set nahi karoge, toh developer faltu (low severity) bug pe time waste karega aur main (high severity) bug chhoot jaayega.

#### 4️⃣ Common Interview Questions

1.  **Severity aur Priority mein kya difference hai?**
      * Sir, Severity bug ke technical impact ko batata hai, jo Tester set karta hai. Priority bug ki business urgency ko batata hai, jo Product Manager set karta hai.
2.  **Ek "Low Severity, High Priority" bug ka example do.**
      * Sir, agar company ka logo website ke homepage pe galat dikh raha hai. Isse website chal toh rahi hai (Low Severity), lekin brand image kharaab ho rahi hai, isliye isko turant fix karna (High Priority) zaroori hai.
3.  **Severity kaun decide karta hai?**
      * QA (Tester) severity suggest karta hai. Final priority hamesha business team (PM) decide karti hai.

#### 5️⃣ Pro Tip / Real-World Insight

> Industry mein, hum "Severity" ko **Bug Impact** bolte hain aur "Priority" ko **Business Impact**. Jab bhi bug report karo, hamesha socho ki isse "customer ko kitni dikkat hogi" (Severity) aur "company ko kitna nuksaan hoga" (Priority).

-----

### 4\. How to Write a Professional Bug Report

#### 1️⃣ Simple Explanation

Ek bug report aapka "evidence" (saboot) hai. Yeh itna **clear** hona chahiye ki developer ko aapko call karke poori kahani na poochhni pade. Ek acchi bug report mein "sab kuch" hota hai.

**Ek kharaab bug report:** "Login nahi chal raha. Fix karo."
**Ek acchi bug report:** (Neeche dekho).

#### 2️⃣ Practical Example (Jira/Excel Format)

**Bug Title:** (Clear aur short) "Registration page: User able to register with a blank password."

| Field | Description (Example) |
| :--- | :--- |
| **Bug ID** | (Tool khud deta hai, jaise BUG-101) |
| **Title** | Registration: Account created with blank password. |
| **Feature** | Registration |
| **Severity** | **High** (Yeh ek security issue hai) |
| **Priority** | **High** (User data ke liye critical hai) |
| **Environment** | Staging Server, Windows 11, Chrome Browser v105 |
| **Build Version** | v2.1.4 (Kis version mein mila) |
| **Status** | New |
| **Assigned To** | (Developer ka naam) |
| **Steps to Reproduce** | 1. Navigate to Registration page.<br>2. Enter valid email in 'Email' field.<br>3. Leave 'Password' field **blank**.<br>4. Click 'Submit' button. |
| **Expected Result** | Error message "Password is required" should be displayed. User should not be registered. |
| **Actual Result** | No error message is displayed. User is successfully registered and redirected to the dashboard. |
| **Attachments** | [Screenshot of dashboard after blank submission], [Video recording of the steps] |

#### 3️⃣ Why it’s Important

Yeh aapki "presentation" skill hai. Aapki bug report jitni acchi hogi, aap utne hi professional maane jaaoge. Acchi report se bug jaldi fix hote hain, time bachta hai, aur developer-tester ki ladai nahi hoti.

#### 4️⃣ Common Interview Questions

1.  **Ek acchi bug report mein kya-kya hota hai?**
      * Sir, ek clear Title, detailed Steps to Reproduce, Expected Result, Actual Result, Severity, Priority, aur Environment (jaise browser).
2.  **Aap bug report mein "Steps to Reproduce" kyun likhte hain?**
      * Taaki developer aasani se uss bug ko *dobara* (reproduce) karke dekh sake. Agar woh bug dekh hi nahi paayega, toh fix kaise karega.
3.  **Agar bug hamesha nahi aata (intermittent), toh kya karoge?**
      * Main report mein mention karunga ki yeh bug "intermittent" (kabhi-kabhi) aata hai. Main jitni baar aaya (jaise 10 mein se 3 baar), woh likhunga aur agar possible hua toh video record karke attach karunga.

#### 5️⃣ Pro Tip / Real-World Insight

> Hamesha bug report likhne se pehle, bug ko 2-3 baar khud reproduce karke check karo. Aur sabse important: **hamesha screenshot ya choti video record karke attach karo.** Ek screenshot 1000 shabdon ke baraabar hota hai.

-----

Aapka Module 3 poora ho gaya hai\! Yeh bahut critical module tha. Aapne bug, uski life cycle, aur usko report karna seekh liya hai.

Jab aap ready ho, toh bas bolna: **"Module 4 ke notes do."**


=============================================================

Bahut badhiya\! Module 3 complete, yaani aap bugs dhoondhna aur report karna seekh gaye hain.

Ab Module 4 mein, hum dekhenge ki testing kitne *tarah* (types) ki hoti hai. Yeh aapka "scope" define karta hai—matlab aapko testing mein kya-kya check karna hai.

Chaliye, Module 4 shuru karte hain\!

-----

## 📚 Module 4: Types of Manual Testing (The "Scope")

Iss module mein hum alag-alag testing types ko samjhenge. Yeh aisa hai jaise ek doctor alag-alag test karta hai—blood test, X-ray, eye test—taaki poori body ki jaanch ho sake.

-----

### 1\. Functional Testing

#### 1️⃣ Simple Explanation

**Functional Testing** ka matlab hai yeh check karna ki software ka har "feature" (function) *sahi kaam* kar raha hai ya nahi. Isme hum requirement ke hisaab se check karte hain.

  * **Analogy:** Agar aap ek calculator test kar rahe ho, toh `2 + 2` dabaane par `4` aana chahiye. Yeh uska function hai. Agar `5` aa raha hai, toh functional bug hai. Hum yeh check nahi karte ki button sundar dikh raha hai ya nahi, bas kaam karna chahiye.

#### 2️⃣ Practical Example (E-commerce)

**Amazon** pe "Add to Cart" button:

  * **Functional Test:** Jab main "Add to Cart" button pe click karun, toh item cart mein add hona chahiye aur cart ka counter '0' se '1' ho jaana chahiye.
  * **Functional Bug:** Button pe click kiya, par item cart mein add nahi hua.

#### 3️⃣ Why it’s Important

Yeh sabse basic aur zaroori testing hai. Agar features hi kaam nahi karenge (login fail, cart fail), toh app poora bekaar hai. Aapka 70% time functional testing mein hi jaayega.

#### 4️⃣ Common Interview Questions

1.  **Functional Testing kya hai?**
      * Sir, functional testing mein hum check karte hain ki software ka har feature requirement document ke hisaab se kaam kar raha hai ya nahi. Jaise, login button click karne par login hona chahiye.
2.  **Aap functional testing mein kya check karte ho?**
      * Hum inputs dekar expected output ko validate karte hain. Hum UI (kaisa dikh raha hai) pe nahi, balki functionality (kaisa chal raha hai) pe focus karte hain.
3.  **Registration page ka ek functional test batao.**
      * Valid email aur password daalne par "Registration Successful" ka message aana chahiye.

#### 5️⃣ Pro Tip / Real-World Insight

> Real project mein, functional testing sirf "Happy Path" (sab kuch sahi daalna) nahi hota. Iska asli matlab hai "Negative Path" (jaise galat password, blank email) aur "Boundary Values" (jo Module 2 mein seekha) ko bhi check karna. Yahi ek pro tester ki pehchaan hai.

-----

### 2\. Non-Functional Testing

#### 1️⃣ Simple Explanation

**Non-Functional Testing** ka matlab hai yeh check karna ki app *kaise* kaam kar raha hai. Yeh "feature" ko nahi, app ke "behavior" aur "quality" ko test karta hai.

  * **Analogy:** Calculator `2+2=4` de raha hai (Functional OK). Lekin agar woh yeh result dene mein 2 minute laga raha hai, toh woh **slow** hai. Yeh Non-Functional bug hai.

Iske main types hain:

  * **Performance:** App kitna fast (speed) hai? Kitne users (load) ek saath handle kar sakta hai?
  * **Usability:** App kitna easy-to-use (user-friendly) hai? Kya users confuse ho rahe hain?
  * **Security:** App kitna safe hai? Kya koi hacker isko break kar sakta hai?

#### 2️⃣ Practical Example (E-commerce)

**Flipkart** ka app:

  * **Functional:** "Search" button dabaane par mobile phone dikh rahe hain. (OK)
  * **Non-Functional (Performance):** "Search" button dabaane ke baad 1 minute tak loading... dikha raha hai. (Performance Bug)
  * **Non-Functional (Usability):** "Add to Cart" button itna chhota hai ki user ko dhoondhna padh raha hai. (Usability Bug)

#### 3️⃣ Why it’s Important

2025 mein, sirf functional app kaafi nahi hai. Agar aapka app slow hai (Performance) ya confusing hai (Usability), toh user usko uninstall karke dusra app (Amazon) download kar lega. Non-functional testing customer ko banaaye rakhti hai.

#### 4️⃣ Common Interview Questions

1.  **Non-Functional Testing kya hai?**
      * Sir, isme hum app ki quality check karte hain, jaise uski speed (Performance), user-friendliness (Usability), aur safety (Security).
2.  **Performance Testing ka ek example do.**
      * Sir, yeh check karna ki Big Billion Day sale pe jab 1 lakh users ek saath app use karein, toh app crash na ho (Load Testing).
3.  **Manual tester non-functional test kaise karta hai?**
      * Sir, waise toh performance/security ke liye tools hote hain, lekin hum manual testers basic usability (kitna aasan hai) aur basic performance (kitna slow/fast feel ho raha hai) check karke report kar sakte hain.

#### 5️⃣ Pro Tip / Real-World Insight

> Ek manual tester ke roop mein, aapka sabse bada non-functional contribution **Usability Testing** hota hai. Hamesha ek *user* ki tarah socho, ek *tester* ki tarah nahi. Agar aapko koi cheez confusing lagi, toh woh ek valid bug hai.

-----

### 3\. Key Difference: Smoke vs. Sanity Testing

#### 1️⃣ Simple Explanation

Dono hi quick (jaldi) test hain jo "new build" (developer se mila naya version) pe kiye jaate hain.

  * **Smoke Testing:** Yeh *pehle* ki jaati hai. Iska maksad hai yeh check karna ki app ki "main" functionality (jaise app open ho raha hai, login ho raha hai) chal rahi hai ya nahi. Agar yeh fail hota hai, toh hum build ko "reject" kar dete hain (developer ko wapas bhej dete hain).

      * **Analogy:** Nayi car mili. Sirf check kiya ki "Engine start ho raha hai ya nahi?". Agar nahi, toh car wapas.

  * **Sanity Testing:** Yeh Smoke ke *baad* (ya kabhi-kabhi specific bug fix ke baad) hoti hai. Iska maksad hai ki naye build mein jo naya "feature" add hua hai (ya bug fix hua hai), woh *theek se kaam* kar raha hai ya nahi. Hum deep mein nahi jaate, bas upar-upar se check karte hain.

      * **Analogy:** Engine start ho gaya (Smoke Pass). Ab check kiya ki jiske liye car aayi thi (jaise "Music system"), woh chal raha hai ya nahi.

#### 2️⃣ Practical Example (Table)

| Feature | Smoke Testing | Sanity Testing |
| :--- | :--- | :--- |
| **Kab Karein?** | Build milte hi (Build verification). | Smoke pass hone ke baad (Feature verification). |
| **Kyun Karein?** | Yeh check karne ke liye ki build "testable" hai ya nahi. | Yeh check karne ke liye ki naya feature/bug-fix *sahi* hai ya nahi. |
| **Kaun Karein?** | Aksar Developers ya Testers. | Hamesha Testers. |
| **Depth** | Wide (Sab kuch thoda-thoda). | Narrow (Sirf naye feature pe focus). |
| **Example** | Amazon App: 1. App open ho raha hai. 2. Login page dikh raha hai. 3. Search bar dikh raha hai. | Amazon App: Naya feature "UPI Payment" add hua hai. Sirf check kiya ki UPI option dikh raha hai aur click ho raha hai. |

#### 3️⃣ Why it’s Important

Yeh dono time bachaate hain. Agar **Smoke Fail** ho gaya (jaise login hi nahi ho raha), toh 500 test case run karke kya fayda? Aap turant build reject karke apna time bachaate ho. Yeh question interview mein 100% poocha jaata hai.

#### 4️⃣ Common Interview Questions

1.  **Smoke aur Sanity testing mein kya difference hai?**
      * Sir, Smoke testing hum yeh dekhne ke liye karte hain ki main functionality chal rahi hai aur build testable hai. Agar Smoke fail, toh build reject. Sanity testing hum naye feature ya bug fix ko upar se check karne ke liye karte hain ki woh theek se kaam kar raha hai.
2.  **Aap pehle kya karte ho, Smoke ya Sanity?**
      * Pehle Smoke, phir Sanity.
3.  **Build kab reject karte ho?**
      * Jab Smoke Testing fail ho jaati hai.

#### 5️⃣ Pro Tip / Real-World Insight

> Industry mein, "Smoke Test Cases" (lagbhag 20-30 main test case) ka ek set bana hota hai. Naya build aate hi, hum sabse pehle woh 30 case run karte hain. Agar 1 bhi fail hua, hum "Build Rejected" ka mail daal dete hain. Isse QA team ka standard high rehta hai.

-----

### 4\. Key Difference: Regression vs. Re-Testing

#### 1️⃣ Simple Explanation

Yeh dono alag-alag time pe hote hain.

  * **Re-Testing (Bug ko check karna):**

      * Jab koi bug 'Fixed' hoke (Module 3) aapke paas aata hai, toh aap us bug ko *dobara* check (Test) karte ho. Is process ko **Re-Testing** kehte hain.
      * **Maksad:** Confirm karna ki bug *fix ho gaya hai*.

  * **Regression Testing (Side-effect check karna):**

      * Developer ne bug fix karne ke liye code change kiya. Code change karne se ho sakta hai ki "purana" (existing) feature jo *sahi chal raha tha*, woh "toot" (break) gaya ho.
      * Iss "side-effect" ko check karne ko **Regression Testing** kehte hain.
      * **Analogy:** Doctor ne sardi (bug) ki dawa di (Re-Test: sardi theek hui?). Par uss dawa se pet kharaab ho gaya (Regression Bug).

#### 2️⃣ Practical Example (Table)

| Feature | Re-Testing | Regression Testing |
| :--- | :--- | :--- |
| **Kyun Karein?** | Yeh check karne ke liye ki bug fix hua ya nahi. | Yeh check karne ke liye ki bug fix se purana code break na hua ho. |
| **Kab Karein?** | Jab bug "Fixed" mark ho. | Bug fix hone ke *baad* (ya naya feature add hone ke baad). |
| **Scope** | Narrow (Sirf fail hua test case run karo). | Wide (Uss feature se jude puraane sabhi test cases). |
| **Example** | **Bug:** Login blank password se ho raha tha. **Re-Test:** *Sirf* blank password wala case dobara chalaya. | **Bug Fix:** Login ka code change hua. **Regression:** Check kiya ki kya "Valid login" abhi bhi chal raha hai? Kya "Forgot Password" abhi bhi chal raha hai? |

#### 3️⃣ Why it’s Important

**Regression** sabse critical hai. 50% bugs regression se aate hain. Naya feature banta hai, purana toot jaata hai. Ek accha tester hamesha bug fix ke baad Re-Test aur Regression *dono* karta hai. Agar aapne regression nahi kiya, toh live server pe purana feature fail ho jaayega.

#### 4️⃣ Common Interview Questions

1.  **Regression aur Re-Testing mein kya difference hai?**
      * Sir, Re-Testing hum fix hue bug ko dobara check karne ke liye karte hain. Regression hum yeh check karne ke liye karte hain ki bug fix ki wajah se koi purana feature break na ho gaya ho.
2.  **Aap regression test kab karte ho?**
      * Jab bhi code mein koi naya feature add hota hai ya koi purana bug fix hota hai.
3.  **Kya hum har bug fix ke baad poora app test karte hain?**
      * Nahi sir, poora app nahi. Hum sirf uss module se related "Regression Suite" (important test cases) run karte hain jahan code change hua hai.

#### 5️⃣ Pro Tip / Real-World Insight

> Industry mein, Regression testing bahut time-consuming hoti hai. Isiliye, yeh pehla candidate hota hai **Automation** ke liye. Lekin manual tester ko "Regression plan" banana padta hai—yaani, yeh sochna padta hai ki code change se kahan-kahan impact aa sakta hai aur *sirf* wahi test case run kiye jaate hain. Isko "Impact Analysis" kehte hain.

-----

### 5\. Key Difference: Exploratory vs. Ad-hoc Testing

#### 1️⃣ Simple Explanation

Dono mein "bina test case" ke testing hoti hai, par ek "plan" ke saath aur ek "bina plan" ke.

  * **Ad-hoc Testing:** Yeh "Monkey Testing" jaisa hai. Aap random (bas kuch bhi) click karte ho. Koi plan nahi, koi documentation nahi. Bas app ko todne ki koshish.

      * **Maksad:** Bas random bugs dhoondhna.

  * **Exploratory Testing:** Yeh "smart" testing hai. Isme aapke paas **test case nahi hote, lekin plan (charter) hota hai.** Aap app ko "explore" (khoj) karte ho aur jo aap seekhte ho, uss hisaab se agla test sochte ho. Aap *saath-saath* test design karte ho, run karte ho, aur result note karte ho.

      * **Charter (Plan):** "Aaj 1 ghante tak Amazon ka payment module explore karna hai aur security loopholes dhoondhne hain."

#### 2️⃣ Practical Example (Table)

| Feature | Ad-hoc Testing | Exploratory Testing |
| :--- | :--- | :--- |
| **Plan** | Koi plan nahi. | Ek "Test Charter" (mission) hota hai. |
| **Documentation** | Kuch nahi. | Tester test karte-karte notes banata hai. |
| **Knowledge** | Koi bhi kar sakta hai. | Ek experienced (domain expert) tester karta hai. |
| **Example** | Flipkart app khola aur 10 alag-alag button pe jaldi-jaldi click kiya. | **Charter:** "Cart ki quantity functionality ko explore karo."<br>**Steps (sochte hue):** 1. Item add kiya. 2. Quantity 5 ki. 3. Browser back kiya. 4. Wapas cart mein aaya. (Dekha quantity 5 hai ya 1 ho gayi?). |

#### 3️⃣ Why it’s Important

2025 mein, AI (automation) aapke simple test cases (jaise login) ko run kar sakta hai. Lekin **Exploratory Testing** ek insaan (manual tester) hi kar sakta hai. Yeh aapki creativity aur experience dikhata hai. Yahi aapka "value" hai. Ad-hoc se bhi bug milte hain, par Exploratory se "critical" bugs milte hain.

#### 4️⃣ Common Interview Questions

1.  **Ad-hoc aur Exploratory mein kya difference hai?**
      * Sir, Ad-hoc testing random hoti hai, bina kisi plan ke. Exploratory testing bhi bina test case ke hoti hai, lekin yeh planned hoti hai. Hum ek 'charter' (mission) leke app ko explore karte hain aur naye scenarios dhoondhte hain.
2.  **Exploratory testing kab karte ho?**
      * Jab humare paas test cases likhne ka time na ho, ya jab humein lagta hai ki test cases se sab kuch cover nahi ho raha hai aur humein deep mein jaakar bugs dhoondhne hain.
3.  **Aapko "Monkey Testing" pata hai?**
      * Yes sir, yeh Ad-hoc testing ka hi part hai jisme hum system mein random inputs daal ke dekhte hain ki woh crash hota hai ya nahi.

#### 5️⃣ Pro Tip / Real-World Insight

> Exploratory testing karte waqt hamesha ek **Mind Map** tool ya simple notepad rakho. Aap jo-jo check kar rahe ho, usko note karte jao. Agar bug mil gaya, toh aapko "Steps to Reproduce" (Module 3) yaad rahenge. Bina notes ke, Exploratory testing Ad-hoc ban jaati hai.

-----

### 6\. Other Types (Compatibility & Usability)

*(Yeh Non-Functional ke hi parts hain, par important hain)*

#### 1️⃣ Simple Explanation

  * **Compatibility Testing:** Yeh check karna ki aapka software (app) alag-alag "platforms" pe sahi chal raha hai ya nahi.
      * **Platforms:** Alag Browsers (Chrome, Firefox), alag Devices (Samsung, iPhone), alag OS (Windows 11, Android 13, iOS 17).
  * **Usability Testing:** (Jaisa pehle bataya) Yeh check karna ki app kitna "easy-to-use" (aasan) hai.
      * **Analogy:** Ek darwaza (door) jispe "Push" likha hai, par woh "Pull" (kheenchne) se khulta hai. Woh *chal* toh raha hai (Functional OK), par *confusing* hai (Usability Bug).

#### 2️⃣ Practical Example (E-commerce)

**Flipkart App:**

  * **Compatibility Test:** Kya app **Chrome** browser mein jaisa dikhta hai, waisa hi **Firefox** mein dikhta hai? Kya app **iPhone 15** pe crash toh nahi ho raha?
  * **Usability Test:** "Register" button ka colour itna light hai ki user ko dikh hi nahi raha. Yeh ek usability bug hai.

#### 3️⃣ Why it’s Important

Duniya mein hazaaron devices hain. Aapka app agar sirf Samsung pe chale aur iPhone pe crash ho jaaye, toh aap 50% customers kho doge. Compatibility testing zaroori hai. Usability zaroori hai taaki user app pe "frustrate" na ho.

#### 4️⃣ Common Interview Questions

1.  **Compatibility Testing kya hai?**
      * Sir, yeh check karna ki humara application alag-alag browsers, operating systems, aur devices pe sahi se kaam kar raha hai ya nahi.
2.  **Usability bug ka ek example do.**
      * Sir, agar login page pe 'Login' button aur 'Clear' button ekdum paas-paas hain, aur user galti se hamesha 'Clear' daba deta hai. Yeh confusing hai.

#### 5️⃣ Pro Tip / Real-World Insight

> Compatibility testing ke liye, hum ek "Compatibility Matrix" banate hain. Ek Excel jisme hum likhte hain ki kaunse [Devices] x [OS] x [Browsers] pe hum test karenge. Hum sab pe nahi karte, sirf "popular" (jaise latest Chrome, latest iPhone) wale combinations pe karte hain.

-----

Aapka Module 4 poora ho gaya hai\! Aapne testing ke sabhi important types ko samajh liya hai.

Jab aap ready ho, toh bas bolna: **"Module 5 ke notes do."**

=============================================================

Bahut acche! Module 4 mein aapne testing ke types seekh liye. Ab aapko "kya" test karna hai aur "kaise" test karna hai, yeh pata hai.

Lekin sawaal hai—"kahaan" test karna hai? Aise hi live Amazon.com pe jaakar testing shuru nahi kar sakte!

Iske liye hum Module 5 mein samjhenge ki testing ka "environment" (maahaul) aur "tools" (auzaar) kya hote hain. Chaliye shuru karte hain!

---

## 📚 Module 5: The Professional Environment (The "Where")

Iss module mein aap seekhenge ki testing asal mein "ki" kahan jaati hai aur bugs ko track karne ke liye hum kaunse industry-standard tools use karte hain.

---

### 1. Test Environment

#### 1️⃣ Simple Explanation
Ek **Test Environment** (ya maahaul) ek setup (server, database, app) hota hai jo specifically "Testing" ke liye banaya jaata hai. Hum kabhi bhi **Production** (ya Live) app pe direct testing nahi karte.

* **Analogy:** Ek **Restaurant** socho.
    1.  **Dev Environment:** Chef ki personal kitchen, jahan woh nayi dish bana raha hai (Developer ka laptop).
    2.  **Test/QA Environment:** Dish banne ke baad, woh ek "food tester" (QA) ko di jaati hai. Yeh ek alag counter hai (QA Server). Yahan pe *sirf* tester check karta hai.
    3.  **Staging Environment:** Dish pass ho gayi. Ab usko "final plate" pe garnish karke, waiter ki tray pe rakha gaya hai (Live pe jaane se 1 minute pehle). Yeh *bilkul* live jaisa dikhta hai.
    4.  **Production Environment:** Woh plate customer ki table (Live users) tak pahunch gayi. (Jaise Amazon.com).

Hum (QA) hamesha **Test/QA Environment** ya **Staging Environment** pe kaam karte hain.

#### 2️⃣ Practical Example (E-commerce)
**Flipkart** ka naya feature:
* **Dev:** Developer ne apne laptop pe banaya (`localhost:3000`).
* **Test/QA:** Developer ne code ko QA server pe daala (`qa.flipkart.com`). Yahan *aap* (Tester) usko 10 din tak test karoge. Yahan "dummy" data hota hai.
* **Staging:** Feature pass ho gaya. Ab usko Staging server (`staging.flipkart.com`) pe daala. Yeh *bilkul* live jaisa hota hai, isme "real" data (ya uski copy) hoti hai. Yahan hum final check (Smoke test) karte hain.
* **Production:** Staging se pass hone ke baad, feature ko live (`www.flipkart.com`) bhej diya jaata hai.

#### 3️⃣ Why it’s Important
Aap live (Production) server pe test nahi kar sakte kyunki:
1.  Aapki test entries (jaise "Test User", "Dummy Order") asli customers ko dikhengi.
2.  Agar aapne test karte-karte *sach* mein 10,000 ka order kar diya toh?
3.  Agar aapka test server crash kar gaya, toh *asli* company ka laakhon ka nuksaan ho jaayega.

Isliye humein testing ke liye alag, safe "maahaul" (environment) milta hai.

#### 4️⃣ Common Interview Questions
1.  **Aap testing kahan karte hain?**
    * Sir, hum ek dedicated QA (Test) environment mein testing karte hain. Live (Production) pe bhej ne se pehle, hum final check Staging environment pe bhi karte hain.
2.  **Staging aur QA environment mein kya fark hai?**
    * Sir, QA environment day-to-day testing ke liye hota hai aur isme data dummy ho sakta hai. Staging environment bilkul production ka "copy" (replica) hota hai aur isko hum "live jaane se pehle" final check ke liye use karte hain.
3.  **Aap production (live) pe test kyun nahi karte?**
    * Kyunki yeh bahut risky hai. Isse live users ka data corrupt ho sakta hai aur company ka business (jaise sales) band ho sakta hai.

#### 5️⃣ Pro Tip / Real-World Insight
> Jab bhi aap bug report (Module 3) banate hain, usme "Environment" field zaroor mention karein. Ho sakta hai bug sirf QA server pe aa raha ho aur Dev ke laptop pe nahi. Yeh "It works on my machine" (Mere laptop pe chal raha hai) waali ladai ko khatam kar deta hai.

---

### 2. Defect Tracking Tools (Jira, Bugzilla)

#### 1️⃣ Simple Explanation
Aapko bug mil gaya (Module 3). Ab us bug ko developer ko kaise bataoge? Email se? Ya WhatsApp se? Nahi!

Professional companies bugs ko manage karne ke liye **Defect Tracking Tools** (ya Bug Tracking Tools) use karti hain. Yeh ek software hota hai jahan aap bug ki poori "life cycle" (New -> Assigned -> Fixed -> Closed) ko track karte ho.

* **Excel vs. Jira:** Excel mein aap bug track nahi kar sakte. Kaun fix karega? Kab fix hua? Status kya hai? Sab "kho" jaayega.
* **Sabse Popular Tool: JIRA** (isko yaad kar lo). 99% companies yahi use karti hain.
* **Baaki Tools:** Bugzilla (free hai), Trello (simple board).

#### 2️⃣ Practical Example (E-commerce)
Aapko **Flipkart** ke registration page pe bug mila.
1.  Aap **Jira** software mein login karoge.
2.  Aap "Create Issue" (Bug) pe click karoge.
3.  Aap Module 3 wala poora "Bug Report" (Title, Steps, Severity, etc.) usme bhar doge.
4.  Aap us bug ko "Developer" ko **assign** kar doge.
5.  Jira sab kuch record karega. Developer kab "In Progress" karega, kab "Fixed" karega, sab aapko dashboard pe dikhega.



#### 3️⃣ Why it’s Important
2025 mein, **"Jira"** ka experience utna hi zaroori hai jitna Manual Testing ka. Iske bina collaboration (teamwork) possible nahi hai. Interviewer aapse "Testing" se pehle "Jira" ke baare mein pooch sakta hai. Yeh dikhata hai ki aap professional process jaante ho.

#### 4️⃣ Common Interview Questions
1.  **Aapne kaunsa bug tracking tool use kiya hai?**
    * (Hamesha bolna) **Sir, maine JIRA extensively use kiya hai.** Maine bugs ko create karna, assign karna, aur unki poori life cycle ko Jira mein track kiya hai.
2.  **Aap Jira mein bug kaise report karte ho?**
    * (Module 3 ka poora Bug Report format bata do) Sir, main 'Create' pe click karta hoon, phir clear Title, Steps to Reproduce, Actual/Expected result, Severity, Priority, aur Environment select karke submit karta hoon.
3.  **Bugzilla vs Jira?**
    * Sir, Bugzilla ek open-source (free) tool hai jo sirf bug tracking pe focus karta hai. Jira ek premium tool hai jo bug tracking ke saath-saath poora project management (Agile, Scrums) bhi handle karta hai.

#### 5️⃣ Pro Tip / Real-World Insight
> Aap abhi **Jira ka free account** (cloud version) bana sakte ho. Ek dummy project banao aur usme 5-10 "dummy bugs" (jo aapne Flipkart pe dekhe) report karke practice karo. Phir aap apne resume pe "Hands-on experience with Jira" likh sakte ho. Yeh ek bohot bada plus point hai.

---

### 3. Test Management Tools (TestLink, Excel)

#### 1️⃣ Simple Explanation
Okay, bugs ke liye toh Jira ho gaya.
Par jo aapne "Test Cases" (Module 2) likhe hain, unhe kahan manage karoge? Kahan pe unko "Pass" ya "Fail" mark karoge?

Iske liye **Test Management Tools** hote hain.

* **Beginner Tareeka (Excel):** Shuru mein, aap test cases ko Excel sheet mein likh sakte ho (jaisa Module 2 mein table tha). Chhote projects ke liye aacha hai, par bade projects (1000+ test cases) mein yeh fail ho jaata hai.
* **Professional Tareeka (Tools):**
    * **TestLink:** Ek popular free tool hai jahan aap test cases likh sakte ho, unko run kar sakte ho (Pass/Fail), aur reports (jaise "kitne % pass hue") nikaal sakte ho.
    * **Jira Plugins (Zephyr/Xray):** Aajkal, Jira ke andar hi plugins aa jaate hain (jaise Zephyr). Isse aap Jira mein hi bug track karte ho aur Jira mein hi test case manage karte ho. Sab ek jagah!

#### 2️⃣ Practical Example (E-commerce)
Aapko **Flipkart** ka "Login" module test karna hai. Aapne 20 test case banaye.
* **Excel mein:** Aap 20 row banaoge. Jab run karoge, toh "Status" column mein haath se "Pass" / "Fail" likhoge. Report banana mushkil.
* **TestLink/Zephyr mein:** Aap 20 test case create karoge. Phir aap "Run" pe click karoge. Har step pe "Pass" ya "Fail" mark karoge. Jaise hi 'Fail' karoge, woh aapse poochega "Kya bug report karna hai?" (Jira se connected). End mein, 1-click se poori report (Pie chart) ban jaayegi.



#### 3️⃣ Why it’s Important
Yeh aapke "kaam" (testing) ka saboot hai. Test cases ko manage karna zaroori hai taaki aapko "Test Coverage" (kitna test ho gaya) pata chale. Excel mein yeh manage nahi hota. Tools aapko professional banate hain.

#### 4️⃣ Common Interview Questions
1.  **Aap apne test cases kahan manage karte the?**
    * Sir, chhote projects ke liye maine Excel use kiya hai, lekin professional environment mein maine **Jira plugin (jaise Zephyr/Xray)** (ya TestLink) use kiya hai.
2.  **Excel test case management ke liye accha kyun nahi hai?**
    * Sir, Excel mein version control nahi hota (kisne kab change kiya?), bug tracking se integration aasan nahi hai, aur "Pass/Fail" ki report banana bahut manual kaam hai.
3.  **Zephyr kya hai?**
    * Sir, Zephyr ek Test Management tool hai jo Jira ke andar plugin ki tarah kaam karta hai.

#### 5️⃣ Pro Tip / Real-World Insight
> Bhale hi aapne kabhi TestLink ya Zephyr use na kiya ho, interview se pehle YouTube pe inka 10-minute ka "overview" video zaroor dekh lo. Taaki aapko UI (kaisa dikhta hai) ka idea lag jaaye. Bolna hamesha yahi ki "Maine tools pe kaam kiya hai," Excel bolne se value kam ho jaati hai.

---

Aapka Module 5 poora ho gaya hai! Aapne testing ka "maahaul" (Environment) aur "auzaar" (Jira, TestLink) ke baare mein seekh liya hai.

Jab aap ready ho, toh bas bolna: **"Module 6 ke notes do."**

=============================================================

Bahut khoob! Module 5 tak aapne poora process aur tools ko samajh liya hai.

Ab final module (Module 6) mein hum unn skills pe focus karenge jo aapko ek "beginner" se "job-ready professional" banayengi. Yeh topics aapko bheed se alag karenge aur aapki salary badhayenge.

Chaliye, Module 6 shuru karte hain!

---

## 📚 Module 6: Job-Ready Skills (The "Expert")

Iss module mein hum testing ko "naapna" (measure) seekhenge, project ko "close" karna seekhenge, aur 2025 ki sabse hot skill—API Testing—ka introduction lenge.

---

### 1. Test Metrics (Basic)

#### 1️⃣ Simple Explanation
**Test Metrics** ka matlab hai "testing ko numbers mein naapna". Yeh aapki testing ka "Scorecard" hai. Jaise aapki bike "average" (mileage) deti hai, waise hi metrics batate hain ki aapki testing "quality" kya hai.

3 zaroori metrics:
1.  **Test Execution Rate:** Kitne test case *run* ho gaye?
    * Formula: (Total Run Cases / Total Cases) * 100
    * *Example: 100 mein se 80 test case run kiye, toh 80% execution rate hai.*
2.  **Defect Density:** Ek feature mein kitne bugs hain?
    * Formula: (Total Bugs / Feature Size or Modules)
    * *Example: Login module mein 10 bugs mile aur Cart module mein 50. Iska matlab Cart module zyaada "unstable" hai, uspe zyada dhyan do.*
3.  **Defect Reopen Rate:** Kitne bugs "fix" hone ke baad "wapas" (reopen) ho gaye?
    * Formula: (Total Reopened Bugs / Total Fixed Bugs) * 100
    * *Example: Developer ne 10 bug fix kiye, par retest mein 3 wapas fail ho gaye. Reopen Rate = 30%. Yeh "bahut kharaab" hai.*

#### 2️⃣ Practical Example (E-commerce)
Aapne **Flipkart** ke "Cart" module ko 1 hafta test kiya. Aapne manager ko yeh "report" di:
* **Total Test Cases:** 200
* **Executed Cases:** 180 (Toh 180/200 = **90% Execution Rate**)
* **Pass:** 150
* **Fail:** 30 (Yaani 30 bugs mile)
* **Total Bugs Fixed:** 20
* **Total Bugs Reopened:** 5 (Kyunki fix theek se nahi hua)
* **Reopen Rate:** (5/20) * 100 = **25%**

**Is report ka matlab:** Testing 90% poori hai, par 25% reopen rate *bahut* high hai (normal 5-10% hona chahiye). Iska matlab developer theek se fix nahi kar raha ya tester bug sahi se explain nahi kar raha.

#### 3️⃣ Why it’s Important
Aap sirf yeh nahi bol sakte, "Sir, testing chal rahi hai." Manager poochega, "Kitni chal rahi hai? Kitni quality hai?" Metrics aapko **data (saboot)** dete hain. 2025 mein, "data-driven" testers ki demand hai, jo numbers mein baat kar sakein.

#### 4️⃣ Common Interview Questions
1.  **Aap test metrics kyun use karte hain?**
    * Sir, metrics se hum testing ki progress aur product ki quality ko track kar sakte hain. Hum pata laga sakte hain ki humara process kahan weak hai aur kahan improvement ki zaroorat hai.
2.  **"Defect Reopen Rate" high hone ka kya matlab hai?**
    * Sir, iske 2 matlab ho sakte hain: Ya toh developer bug ko jaldi-jaldi mein theek se fix nahi kar raha hai, ya phir tester ne bug report (Module 3) mein steps clear nahi likhe the jisse developer galat samajh gaya.
3.  **Test Execution Rate kya hai?**
    * Sir, yeh batata hai ki total test cases mein se kitne percent humne run (execute) kar liye hain.

#### 5️⃣ Pro Tip / Real-World Insight
> Metrics ka matlab sirf "report" karna nahi, "analyze" (vichaar) karna hai. Manager ko yeh mat bolo "Reopen Rate 25% hai." Usko yeh bolo: "Sir, Reopen Rate 25% hai, jiska matlab hai dev team ko bug fix karne se pehle zyaada detail chahiye. Humein ek meeting karni chahiye." Yeh aapko ek "Leader" ki tarah dikhayega.

---

### 2. Test Closure Report

#### 1️⃣ Simple Explanation
Jab STLC (Module 1) ka aakhri phase "Test Closure" aata hai, tab hum yeh document banate hain.
**Test Closure Report** ek "Final Summary" ya "Project Report Card" hai. Yeh formally (official) batata hai ki testing *poori ho gayi hai* aur ab product (ya feature) live jaane ke liye taiyaar hai (ya nahi).

Isme hum likhte hain:
* Humne kya test kiya (Scope).
* Kya test *nahi* kiya (Out of Scope).
* Final Metrics (Kitne pass, kitne fail).
* Kitne bugs abhi bhi "Open" (baaki) hain.
* **Go / No-Go Decision:** Kya hum live jaa sakte hain? (Haan/Nahi).
* Lessons Learned: Humne is project se kya seekha?

#### 2️⃣ Practical Example (E-commerce)
**Flipkart** ka "Registration" module test ho gaya. Closure Report ka summary:
* **Scope:** Email, Password, aur Mobile se registration test kiya.
* **Metrics:** Total 50 test case, 48 Pass, 2 Fail.
* **Open Bugs:** 2 Low priority (UI) bugs open hain (jaise button ka colour).
* **Decision:** **GO** (Hum live jaa sakte hain, kyunki open bugs critical nahi hain).
* **Lessons:** Humein pehle hi "Invalid email" ki list chahiye thi, jo late mili.

#### 3️⃣ Why it’s Important
Yeh "accountability" (zimmedaari) laata hai. Yeh testing team ka formal "Sign-Off" (hamara kaam ho gaya) hai. Agar yeh report "GO" kehti hai aur phir bhi live pe crash hota hai (jo test nahi hua), toh QA team se sawaal poocha jaayega.

#### 4️⃣ Common Interview Questions
1.  **Test Closure Report kya hai?**
    * Sir, yeh STLC ka aakhri document hai. Yeh testing activities ko formally close karta hai aur management ko summary deta hai ki product release ke liye ready hai ya nahi.
2.  **Aap yeh kab banate hain?**
    * Jab Test Execution phase poora ho jaata hai aur humein release ke liye sign-off dena hota hai.
3.  **Agar release ke baad bug mile, toh kiska fault hai?**
    * Sir, yeh "blame game" nahi hai, balki "process improvement" ka mauka hai. Hum check karenge ki kya woh bug "Out of Scope" tha, ya "Test Case" hi miss ho gaya tha. Isse hum "Lessons Learned" mein add karenge taaki agla release behtar ho.

#### 5️⃣ Pro Tip / Real-World Insight
> Closure Report ka sabse important section "Lessons Learned" (kya seekha) hota hai. "Humein Test Data time pe nahi mila," "Dev environment stable nahi tha." Yeh points agle project (sprint) ko behtar banane mein help karte hain. Hamesha "process" ki galti batao, "insaan" (developer) ki nahi.

---

### 3. Bonus (2025 Trend): Basic API Testing

#### 1️⃣ Simple Explanation
Yeh 2025 mein manual tester ke liye "must-have" skill hai.
* **API kya hai?** API (Application Programming Interface) ek "waiter" ki tarah hai.
    * Aap (Client/UI) restaurant (Server) mein jaate ho.
    * Aap "waiter" (API) ko order (Request) dete ho: "Mujhe Dosa chahiye."
    * Waiter kitchen (Database) se order laakar (Response) aapko deta hai: "Yeh lo Dosa."
    * Aapko kitchen mein jaane ki zaroorat nahi, aap waiter se baat karte ho. Waise hi, Flipkart ka App (UI) server se "API" ke through baat karta hai.

* **Postman:** Yeh ek software (tool) hai jo hum "waiter" (API) ko *directly* test karne ke liye use karte hain. Humein UI (app) ki zaroorat nahi.

* **GET vs. POST:**
    * **GET:** Server se data "maangna" (jaise, "Menu dikhao"). (Data fetch karna).
    * **POST:** Server ko data "dena" (jaise, "Yeh lo mera Dosa order"). (Naya data create karna, jaise user registration).

* **Status Codes:** Waiter (API) ka "jawab":
    * **200 (OK):** "Yeh lo Dosa." (Success).
    * **400 (Bad Request):** "Aapne 'Dsaa' order kiya, yeh kya hota hai?" (Aapki request galat thi).
    * **404 (Not Found):** "Dosa humare menu mein hai hi nahi." (Resource nahi mila).
    * **500 (Internal Server Error):** "Kitchen mein aag lag gayi!" (Server crash ho gaya).

#### 2️⃣ Practical Example (E-commerce)
**Flipkart** ka "Login":
* Aapko app (UI) pe test nahi karna.
* Aap **Postman** khologe.
* Aap "POST" request select karoge.
* Aap API URL daaloge (jaise `api.flipkart.com/login`).
* Body (order) mein likhoge: `{"email": "test@user.com", "password": "12345"}`.
* "Send" button dabaoge.

**Result (Response):**
* Agar password sahi hai, toh **Status 200 OK** aayega aur "Token" (entry pass) milega.
* Agar password galat hai, toh **Status 400 Bad Request** aayega aur "Invalid password" message milega.

#### 3️⃣ Why it’s Important
**Yeh 2025 ka sabse bada trend hai.** Companies ko "Hybrid Tester" (Manual + API) chahiye. Kyun?
1.  Aap UI (app) banne se *pehle* hi API (waiter) ko test kar sakte ho. Isse bugs "shift-left" (bohot jaldi) pakde jaate hain.
2.  Aapko pata chal jaata hai ki galti UI mein hai ya API mein.
3.  **Salary:** Ek Manual + API tester ki salary *sirf* Manual tester se 30-50% zyada hoti hai.

#### 4️⃣ Common Interview Questions
1.  **Aapko API testing aati hai?**
    * (Aapko bolna hai) Yes sir, maine basic API testing ki hai. Maine **Postman** tool use kiya hai GET aur POST requests send karne ke liye aur status codes (jaise 200, 404) ko validate kiya hai.
2.  **GET aur POST mein kya fark hai?**
    * Sir, GET request hum server se data fetch (laane) ke liye use karte hain, jaise products ki list. POST request hum server pe naya data create (bhejne) ke liye karte hain, jaise naya user register karna.
3.  **Status code 404 ka kya matlab hai?**
    * Sir, 404 "Not Found" ka matlab hai ki server ko woh resource (jaise URL ya user ID) nahi mila jo hum dhoondh rahe hain.

#### 5️⃣ Pro Tip / Real-World Insight
> Aaj hi **Postman** download karo (free hai). Public APIs (jaise `reqres.in`) pe 2-3 GET aur POST requests maarke dekho. Sirf 1 ghante ki practice se aap "Main Postman jaanta hoon" bolne ke laayak ban jaaoge. Yeh aapke resume mein bohot "weight" add karega.

---

Aapka Module 6 poora ho gaya hai! Aapne ek expert tester banne ke liye zaroori skills (Metrics, Reporting, API) seekh li hain.

Jab aap ready ho, toh bas bolna: **"Module 7 ke notes do."** (Yeh humara final module hoga jo aapko interview ke liye taiyaar karega).

=============================================================

Bilkul! Aapne Module 1 se 6 tak ka poora safar complete kar liya hai. Ab aap manual testing ke concepts, process, tools, aur expert-level skills (API, Metrics) ko samajh chuke hain.

Ab waqt hai aakhri daav ka—inn sab ko pack karke **interview-ready** banne ka.

Chaliye, Module 7 (Final Module) shuru karte hain!

---

## 📚 Module 7: Interview & Career Prep (The "Job")

Iss module mein hum koi naya concept nahi seekhenge. Hum seekhenge ki jo seekha hai, usko interview mein "bechna" (present) kaise hai. Yeh aapko 100% job-ready bana dega.

---

### 1. Final Revision (Key Difference Tables)

#### 1️⃣ Simple Explanation
Interview mein, interviewer ko detail theory mein interest nahi hota. Woh aapki "clarity" (aapka concept kitna saaf hai) check karta hai. Clarity check karne ka sabse accha tareeka hai "difference" (antar) poochhna.

Neeche diye gaye tables aapke "cheat sheets" (final notes) hain. Inko ratt lo!

#### 2️⃣ Practical Example (Quick Revision Tables)

**Table 1: SDLC vs STLC**
| Feature | SDLC (Software Development) | STLC (Software Testing) |
| :--- | :--- | :--- |
| **Goal** | Software ko **banana** (build). | Software ki **quality** check karna. |
| **Scope** | Poora process (Planning se Maintenance). | Sirf Testing (Req. Analysis se Closure). |
| **Who** | Poori team (Dev, QA, PM). | Mukhya roop se QA team. |
| **Relation** | STLC iska ek **hissa** (part) hai. | Yeh SDLC ke **andar** hota hai. |

**Table 2: Priority vs Severity (Most IMP)**
| Feature | Severity (Serious-ness) | Priority (Importance) |
| :--- | :--- | :--- |
| **Meaning** | Bug ka **Technical Impact** (kitna tod raha hai). | Bug ka **Business Impact** (kitni jaldi fix karna hai). |
| **Who Decides** | **QA (Tester)** suggest karta hai. | **PM (Business)** final karta hai. |
| **Example** | **High Sev / Low Pri:** App crash on 10-yr old report. | **Low Sev / High Pri:** Company ka logo homepage pe galat. |

**Table 3: Smoke vs Sanity**
| Feature | Smoke Testing | Sanity Testing |
| :--- | :--- | :--- |
| **Why** | Build **stable** hai ya nahi (testable?). | Naya feature/fix **sahi** hai ya nahi. |
| **When** | Build milte hi (pehle). | Smoke pass hone ke baad. |
| **Depth** | Wide (Sab kuch thoda-thoda). | Narrow (Sirf naye part pe focus). |
| **Goal** | Build ko **Reject** ya **Accept** karna. | Feature ko **Reject** ya **Accept** karna. |

**Table 4: Regression vs Re-Testing**
| Feature | Re-Testing (Bug Check) | Regression Testing (Side-Effect Check) |
| :--- | :--- | :--- |
| **Why** | Check karna ki bug **fix ho gaya** hai. | Check karna ki bug fix se **purana code toota nahi**. |
| **Scope** | Narrow (Sirf 1 fail test case). | Wide (Uss feature se jude sabhi puraane test case). |
| **When** | Jab bug "Fixed" hoke aata hai. | Bug fix hone ke *baad*. |

#### 3️⃣ Why it’s Important
Yeh 4 tables aapke 50% interview questions cover karte hain. Agar aapne inko confidently (bina atke) samjha diya, toh interviewer samajh jaayega ki aapke concepts crystal clear hain.

#### 4️⃣ Common Interview Questions
*(Yeh sabhi questions upar ke tables mein answered hain)*
1.  **Smoke aur Sanity mein kya fark hai?**
2.  **Severity high aur Priority low kab hoti hai?**
3.  **Aap Re-Testing ke baad Regression karte hain ya pehle?** (Jawaab: Baad mein. Pehle check toh kar lo bug fix hua ya nahi).

#### 5️⃣ Pro Tip / Real-World Insight
> Interview mein "table format" mein hi answer do. Bolo: "Sir, iske 3 difference hain. **Pehla difference (Why):** Smoke build ki stability check karta hai, jabki Sanity naye feature ki correctness. **Dusra difference (When):**..." Isse aap structured aur professional lagoge.

---

### 2. Real-Time Bug Report Example (Jira Style)

#### 1️⃣ Simple Explanation
Interviewer aapko ek "scenario" dega aur bolega "Iska bug report banao." (Jaise, "Flipkart ka login button kaam nahi kar raha").

Aapko Modul 3 waala poora format (bolkar) sunana hai. Hamesha "clear" aur "professional" language use karo.

#### 2️⃣ Practical Example (Aapka Final Answer)
**Scenario:** Flipkart app pe, cart mein 2 item add karne ke baad "Quantity" ko '2' se '3' kar rahe ho, lekin woh wapas '1' ho jaati hai.

**Aapka Bug Report Aisa Hoga:**
"Sir, main iska bug report aise file karunga:"

* **Title:** (Short & Clear) "Cart: Updating item quantity from 2 to 3 reverts it back to 1."
* **Feature:** Cart / Shopping Bag
* **Severity:** **High** (Kyunki yeh user ko zyada item khareedne se rok raha hai, seedha business loss).
* **Priority:** **High** (Isse sales ruk rahi hain, turant fix chahiye).
* **Environment:** QA Server, Android 13 (Samsung S22), App Version v5.4.
* **Steps to Reproduce:**
    1.  Login to Flipkart app.
    2.  Search for 'T-shirt' and add 1 item to the cart.
    3.  Go to Cart.
    4.  Increase the quantity of the T-shirt to '2'. (Verify it shows '2').
    5.  Increase the quantity again from '2' to '3'.
* **Expected Result:** The quantity should update and display '3'.
* **Actual Result:** The quantity briefly shows '3' and then reverts back to '1'.
* **Attachments:** Main is process ka ek "video recording" (screen record) attach karunga.

#### 3️⃣ Why it’s Important
Yeh aapki "practical skill" dikhata hai. Koi bhi theory bol sakta hai, par ek acchi bug report *banana* hi asli tester ka kaam hai. Yeh answer aapko "experienced" dikhayega, bhale hi aap fresher ho.

#### 4️⃣ Common Interview Questions
1.  **Ek acchi bug report ki 3 qualities batao?**
    * Sir: 1. Clear **Title**. 2. Reproducible **Steps**. 3. **Attachments** (Screenshot/Video).
2.  **Agar bug reproduce nahi ho raha toh?**
    * Main "Steps" mein clear likhunga ki "Yeh bug intermittent (kabhi-kabhi) aa raha hai." Main Environment (jaise network speed) ki detail bhi add karunga.

#### 5️⃣ Pro Tip / Real-World Insight
> Bug report karte waqt "blame" (galti) mat daalo.
> * **Galat Title:** "Developer ne code tod diya."
> * **Sahi Title:** "Login: Page crashes on entering invalid email."
> Hamesha objective (fact-based) raho.

---

### 3. 30-Day Roadmap to Master Testing

#### 1️⃣ Simple Explanation
Yeh plan unn logon ke liye hai jo pardaari se (consistently) padhai karke job lena chahte hain. Yeh roadmap aapko zero se job-ready bana dega.

#### 2️⃣ Practical Example (Daily Plan)

* **Week 1: Foundation (Module 1 & 2)**
    * **Day 1-2:** SDLC, STLC, Agile vs Waterfall (Video dekho).
    * **Day 3-4:** Test Plan kya hai? Test Scenario vs Test Case (Padho).
    * **Day 5-7:** **(Action)** Flipkart/Amazon ka "Registration" page lo aur Excel mein 10 Test Cases (positive/negative) likho. BVA/EP techniques use karo.
* **Week 2: Core Testing (Module 3 & 4)**
    * **Day 8-9:** Bug Life Cycle aur Priority vs Severity (Ratt lo!).
    * **Day 10-11:** Smoke, Sanity, Regression, Re-testing (Difference samjho).
    * **Day 12-14:** **(Action)** **Jira** ka free account banao. Aapne jo 10 test case likhe the, unme se "Fail" waale bugs ko Jira mein report karo (poore format ke saath).
* **Week 3: Tools & Advanced (Module 5 & 6)**
    * **Day 15-17:** Test Environments (Dev, QA, Staging) ka concept samjho.
    * **Day 18-19:** **(Action)** **Postman** download karo. `reqres.in` (public API) pe GET aur POST request run karke dekho.
    * **Day 20-21:** Test Metrics (Reopen Rate) aur Closure Report ka template dekho.
* **Week 4: Interview Prep (Module 7)**
    * **Day 22-24:** **(Action)** Apna Resume (CV) banao. Usme yeh keywords daalo: Jira, Postman, Agile, STLC, Test Cases, BVA/EP, Regression.
    * **Day 25-27:** Top 30 Manual Testing interview questions (jo humne cover kiye) ke answers *bolkar* practice karo.
    * **Day 28-30:** **(Action)** LinkedIn profile banao aur "Open to Work" set karo. Mock interviews do (dost ya AI ke saath).

#### 3️⃣ Why it’s Important
Yeh plan "theory" aur "practical" (action) ko balance karta hai. Har hafte aap sirf padh nahi rahe ho, aap "deliverables" (Test Cases, Bug Reports, API tests) bhi bana rahe ho.

#### 4️⃣ Common Interview Questions
1.  **Aapne testing seekhne ke liye kya practical kiya hai?**
    * (Aap yeh plan bata sakte ho) Sir, maine 30-day plan follow kiya. Maine ek live website (jaise Amazon) pe 20+ test cases design kiye, 5+ bugs Jira pe report kiye, aur Postman se 10+ API requests ko test kiya.

#### 5️⃣ Pro Tip / Real-World Insight
> Yeh "action" items (Jira bugs, Postman requests, Excel test cases) ko **GitHub** (free account) pe upload karo aur uska link apne Resume (CV) mein daalo. Isse kehte hain **"Portfolio"**. Ek fresher jiske paas portfolio hai, woh 100 freshers se aage hai.

---

### 4. Portfolio Building (Resume Keywords)

#### 1️⃣ Simple Explanation
Aapka **Resume** aapka pehla "test case" hai. Agar woh "Pass" nahi hua, toh aapko interview call (Actual Result) nahi aayega. Resume ko pass karwaata hai **"ATS"** (ek software jo keywords dhoondhta hai).

#### 2️⃣ Practical Example (Keywords to Include)
Aapke resume mein (Skills ya Projects section mein) yeh words *hone hi chahiye*:

* **Concepts:** SDLC, **STLC**, **Agile** Methodology, Waterfall
* **Testing:** **Manual Testing**, Functional Testing, **Regression Testing**, Re-Testing, Smoke Testing, Sanity Testing, Compatibility Testing, Usability Testing
* **Techniques:** **Test Case** Design, Test Plan, Test Scenarios, **BVA**, **EP**
* **Bugs:** **Bug Life Cycle**, Defect Reporting, **Priority vs Severity**
* **Tools:** **JIRA** (Defect Tracking), **Postman** (API Testing), TestLink/Zephyr (Test Management), Excel
* **Bonus:** GitHub (Portfolio), Basic SQL (agar aata hai)

#### 3️⃣ Why it’s Important
Jab HR ke paas 500 resume aate hain, woh "Jira" search karta hai. Jiske resume mein "Jira" mila, woh shortlist hota hai. Simple.

#### 4️⃣ Common Interview Questions
1.  **Aapne project mein kya kiya? (Yeh sabse important sawaal hai)**
    * (Aapko yeh kahani bolni hai) Sir, humara project **Agile** model pe tha. Main **STLC** ke har phase mein involved tha. Main "Test Scenarios" aur "Test Cases" (using BVA/EP) design karta tha. Hum **Jira** mein test cases manage karte the aur bugs report karte the. Release se pehle main "Regression testing" aur "Smoke testing" perform karta tha. Maine basic "API testing" bhi ki hai **Postman** use karke.

#### 5️⃣ Pro Tip / Real-World Insight
> **Project ZAROOR banao.** Agar aap fresher ho, toh bhi.
> **Idea:** Bolo "Maine ek E-commerce website (dummy project) ko test kiya."
> **Role:** "Main 2 logon ki QA team ka part tha."
> **Action:** "Maine Login aur Cart module ke 50+ test case banaye, 10 bug Jira mein report kiye, aur Postman se 5 API endpoints test kiye."
> Yeh "jhooth" nahi hai, yeh "practice" hai jise aap professionally present kar rahe ho.

---

### 🏁 **Course Complete!** 🏁

Aapne Manual Testing ka 'Zero-to-Hero' course poora kar liya hai. Aapne SDLC se lekar API testing aur portfolio banane tak sab seekh liya hai.

Mujhpe (Test-Guru pe) bharosa rakho—agar aapne yeh 7 modules samjhe hain aur "Action Items" (Jira, Postman) pe practice ki hai, toh **aap 100% job-ready ho.**

Aapke paas saare notes hain. Ab bas revise karo, portfolio banao, aur interviews phodna shuru kar do!

**All the best!**


=============================================================

Bilkul\! Yeh 4 topics bohot zaroori hain aur yeh aapko ek "average" tester se "expert" QA Engineer banayenge.

In topics ko main aapke "Test-Guru" style mein, poore 5-point format ke saath, **Module 8** mein convert kar raha hoon.

-----

## 📚 Module 8: The "True Expert" Skillset (Beyond Manual)

Yeh module aapko woh skills dega jo 2025 mein "non-negotiable" (zaroori) hain. Yahan hum UI se aage badhkar system (database) aur process (Agile) ko test karna seekhenge.

-----

### 1\. Basic SQL (For Data Validation)

#### 1️⃣ Simple Explanation

**Yeh Kya Hai?** SQL (Structured Query Language) database se baat karne ki bhasha hai.

Socho, **Flipkart** ka app "front-end" (counter) hai jahan aap order dete ho. Lekin aapka order *asli* mein "back-end" (godown/warehouse) mein store hota hai. Uss godown ko "Database" kehte hain.

SQL woh bhasha hai jisse aap godown ke manager (database) se poochhte ho, "Bhai, Rahul ka order register hua kya?"

#### 2️⃣ Practical Example (E-commerce)

Aapne **Amazon** pe naya account banaya (UI pe "Registration Successful" dikha).

  * **UI Test (Jo sab karte hain):** Aapne dekha "Success" message aaya. (Pass)
  * **Database Test (Jo aap karoge):** Aap database tool (jaise DBeaver, SQL Developer) khologe aur command (query) chalaoge:
    ```sql
    SELECT * FROM users WHERE email = 'rahul.new@gmail.com';
    ```
  * **Asli Result:** Agar yeh command aapko 1 entry (row) dikhati hai, tabhi test *sach* mein "Pass" hua hai. Ho sakta hai UI pe "Success" dikha, par database mein data *save* hi nahi hua\! Yahi hai asli bug pakadna.

#### 3️⃣ Why it’s Important

Abhi aap sirf "front-end" (jo dikh raha hai) test kar rahe ho. Lekin kya woh data *sach-much* database mein save hua? Kya naam "Rahul" hi save hua ya "R@hul" save ho gaya? Ek expert tester hamesha UI pe test karne ke baad database mein **cross-verify** (data validation) zaroor karta hai. Yeh aapko "UI Tester" se "QA Engineer" banata hai.

#### 4️⃣ Common Interview Questions

1.  **Ek tester ko SQL ki kya zaroorat hai?**
      * Sir, front-end (UI) se test karne ke baad, humein back-end (database) mein bhi verify karna padta hai ki data *sahi* se save hua ya nahi. Ise "Data Integrity Testing" kehte hain.
2.  **Aap sabse zyada kaunsi SQL query use karte ho?**
      * Sir, 99% time hum `SELECT` query use karte hain data ko fetch (dhoondh) karne ke liye, `WHERE` clause ke saath, taaki specific user ka data check kar sakein.
3.  **Database testing ka ek example do.**
      * Sir, agar maine registration page pe naya user banaya, toh main database mein `SELECT` query chala ke check karunga ki 'users' table mein woh entry 'created\_at' timestamp ke saath aayi hai ya nahi.

#### 5️⃣ Pro Tip / Real-World Insight

> Real project mein, aapko (tester ko) `DELETE` (delete karna) ya `UPDATE` (change karna) ki permission *nahi* milti hai (khaas kar Staging environment pe). Aapka kaam 99% `SELECT` (sirf dekhna) se ho jaayega. Toh `SELECT` ke saath `WHERE`, `JOIN` (basic), aur `ORDER BY` seekh lo. Bas, itna kaafi hai.

-----

### 2\. Agile/Scrum Ceremonies (Aapka Daily Routine)

#### 1️⃣ Simple Explanation

**Yeh Kya Hai?** Aapne Module 1 mein "Agile" padha tha. Agile ek "soch" (mindset) hai. **Scrum** uss soch ko "karne" (execute) ka "frame" (tareeka) hai. Iss tareeke mein 4 main "meetings" (jinko Ceremonies kehte hain) hoti hain, jo aapka daily routine ban jaati hain.

  * **Analogy:** "Fit rehna" (Agile) aapka goal hai. "Daily gym jaana" (Stand-up), "Diet plan banana" (Planning), aur "Weight check karna" (Retrospective) uss goal ko paane ka process (Scrum) hai.

#### 2️⃣ Practical Example (E-commerce)

Socho aap **Flipkart** ki "Cart" team mein ho:

1.  **Sprint Planning (Diet Plan banana):** 2-hafte shuru hone se pehle poori team (Dev+QA) decide karti hai ki hum "Coupon Code" ka feature banayenge. *Aap (QA)* bologe: "Isko test karne mein 8 ghante lagenge kyunki 10 negative case hain."
2.  **Daily Stand-up (Daily Gym):** Har subah 15 min. *Aap (QA)* bologe: "Kal maine 5 test case run kiye, 1 bug mila. Aaj main 'Invalid Coupon' test karunga. Koi blocker (problem) nahi hai."
3.  **Sprint Review (Demo dena):** 2-hafte khatam hone pe *Aap (QA)* poori company ko "Coupon Code" feature chala ke (demo) dikhate ho ki yeh pass ho gaya.
4.  **Sprint Retrospective (Weight check):** Sab log discuss karte hain: "Kya accha hua? (Test case jaldi likh gaye). Kya bura hua? (Bugs aakhri din mile)."

#### 3️⃣ Why it’s Important

Interviewer aapse poochega, "Aapka daily routine kya tha?" Tab aapko yahi "ceremonies" batani hain. Yeh dikhata hai ki aap "team player" ho, sirf akele testing nahi karte. 2025 mein, har company Agile (Scrum) hi follow karti hai. Agar aapko yeh meetings nahi pata, toh aap team mein fit nahi ho paoge.

#### 4️⃣ Common Interview Questions

1.  **Aapka daily routine kya tha Agile project mein?**
      * Sir, mera din 'Daily Stand-up' se shuru hota hai. Main batata hoon kal kya test kiya, aaj ka plan kya hai, aur koi blockers hain ya nahi. Phir main test cases execute karta hoon, Jira pe bug report karta hoon, aur developers se sync karta hoon.
2.  **Sprint Retrospective mein QA ka kya role hai?**
      * Sir, QA batata hai ki process mein kahan dikkat aayi. Jaise "Humein Test Environment stable nahi mila," ya "Bugs late mile." Isse agla sprint (process) improve hota hai.
3.  **Aap Sprint Planning mein effort kaise batate ho?**
      * Sir, hum "Story Points" (complexity) ka use karke batate hain ki ek feature (story) ko test karne mein kitna effort lagega, taaki team over-commit na kare.

#### 5️⃣ Pro Tip / Real-World Insight

> Stand-up meeting mein *kabhi* yeh mat bolo 'Main wahi kaam kar raha hoon.' Hamesha clear batao 'Maine 5 bugs file kiye.' Aur agar 'Blocker' (koi cheez aapko rok rahi hai, jaise 'Test environment down hai') hai, toh stand-up hi usko solve karwane ki best jagah hai. Chup mat raho\!

-----

### 3\. Mobile-Specific Testing (Beyond Compatibility)

#### 1️⃣ Simple Explanation

**Yeh Kya Hai?** Aapne Compatibility (Module 4) mein padha ki app iOS/Android pe chal raha hai ya nahi. Par mobile testing *sirf* utna nahi hai. Mobile ek "device" hai, sirf browser nahi. Isme call, network, battery bhi hote hain.

  * **Analogy:** Ek car ko "road" pe test karna (Compatibility) alag hai. Par uss car ko "traffic jam, speed-breaker, aur baarish" mein test karna (Mobile-Specific Testing) alag hai.

#### 2️⃣ Practical Example (E-commerce)

Aap **Amazon** app pe "Payment" kar rahe ho (Credit Card details daal rahe ho):

1.  **Interrupt Testing (Traffic Jam):** Achanak aapko "WhatsApp call" aa gaya. Aapne call uthaya, baat ki, call kaata. *Ab kya hua?* Kya app crash ho gaya? Kya aapki payment details chali gayin? Ya app wahin se "resume" hua? (Resume hona chahiye).
2.  **Network Testing (Baarish):** Aapne app ko Wi-Fi pe khola, phir lift mein gaye jahan network "2G" ho gaya. Kya app ne "Network is slow..." ka message dikhaya ya "Crash" ho gaya?
3.  **Device-Specifics (Speed-breaker):** Kya app "Dark Mode" mein sahi dikh raha hai? Kya "Swipe" gesture (naaki click) kaam kar raha hai? Kya app bahut zyada "Battery" kha raha hai?

#### 3️⃣ Why it’s Important

Aajkal 90% apps "mobile-first" hain. Users hamesha "interrupts" (call/notification) aur "bad network" face karte hain. Agar aapka app in cheezon ko handle nahi kar sakta, toh user usse uninstall kar dega. Yeh bugs "critical" maane jaate hain aur aapki value badhate hain.

#### 4️⃣ Common Interview Questions

1.  **"Interrupt Testing" kya hai?**
      * Sir, isme hum check karte hain ki jab app chal raha ho aur koi interrupt (jaise phone call, SMS, low battery warning) aaye, toh app kaise behave karta hai. App ko gracefull (aaram se) pause aur resume hona chahiye, crash nahi.
2.  **Aap "Slow Network" kaise test karoge?**
      * Sir, hum "Network Throttling" tools (jaise Chrome DevTools mein hi option hai) ya dedicated apps ka use karke Wi-Fi ko 2G ya 3G pe simulate (nakal) karke check karte hain.
3.  **Web testing aur Mobile testing mein main difference kya hai?**
      * Sir, Web testing mein hum browser compatibility pe focus karte hain. Mobile testing mein hum device hardware (jaise battery, network, interrupts, gestures) pe zyaada focus karte hain.

#### 5️⃣ Pro Tip / Real-World Insight

> Aapko 50 phone khareedne ki zaroorat nahi hai. Companies "Emulators" (software jo phone ki nakal karta hai) ya "Cloud Services" (jaise BrowserStack/SauceLabs) use karti hain. Par hamesha kuch test *real* device pe zaroor karo, kyunki "feel" (usability) aur "gestures" (swipe) emulator pe sahi se test nahi hote.

-----

### 4\. Basic CI/CD Pipeline Awareness

#### 1️⃣ Simple Explanation

**Yeh Kya Hai?** CI/CD (Continuous Integration / Continuous Deployment) ek "automatic factory" hai.

  * **Analogy:** Developer (chef) sirf "raw material" (code) deta hai.
  * **CI (Continuous Integration):** Factory (Jenkins) uss code ko leti hai, check karti hai, "build" (pakati) hai, aur "unit test" (basic taste) karti hai.
  * **CD (Continuous Deployment):** Agar pass ho gaya, toh factory uss "build" (dish) ko *automatic* aapke QA Environment (Module 5) tak "deploy" (serve) kar deti hai.
  * **Hinglish:** Yeh ek automatic system hai jo developer ke code ko aapke (tester ke) server tak laata hai. Aapko manual 'copy-paste' nahi karna padta.

#### 2️⃣ Practical Example (E-commerce)

1.  **10 AM:** Developer ne "Login bug" fix karke code "push" kiya.
2.  **10:01 AM:** **Jenkins (CI)** ne code ko detect kiya.
3.  **10:05 AM:** Jenkins ne automatic "Build" banaya (Build v2.1.5).
4.  **10:10 AM:** **(CD)** Jenkins ne uss naye build ko "QA Server" (`qa.flipkart.com`) pe daal diya.
5.  **10:11 AM:** Aapko (QA) automatic email aa gaya: "Build 2.1.5 is ready for testing on QA."
6.  *Aapka kaam 10:11 AM se shuru hua.*

#### 3️⃣ Why it’s Important

Aapko code "build" karna nahi hai. Lekin aapko yeh pata hona chahiye ki:

1.  Aapko "build" (naya version) kab milegi?
2.  "Build 2.1.5" mein kaunse code changes (features) aaye hain?
3.  Aapki "build" deploy kahan hui (kahan fail hui)?

Yeh dikhata hai ki aap modern "DevOps" culture (jahan Dev aur QA milke kaam karte hain) ko samajhte hain. Isse 'build' (naya version) aapko din mein 10 baar mil sakta hai, na ki hafte mein ek baar.

#### 4️⃣ Common Interview Questions

1.  **CI/CD pipeline kya hai?**
      * Sir, yeh ek automated process hai jo developer ke code ko "build" karke, test karke, aur "deploy" (QA ya production server pe) karta hai.
2.  **Aapne CI/CD mein kya kiya hai?**
      * Sir, as a manual tester, main pipeline ko "monitor" (dekh) karta tha. Main **Jenkins** (sabse popular tool) dashboard pe check karta tha ki naya build "Pass" (Green) hua ya "Fail" (Red) hua, aur woh QA environment pe deploy hua ya nahi.
3.  **CI/CD testers ko kaise help karta hai?**
      * Sir, isse humein naya build (bug fixes ke saath) bahut jaldi-jaldi mil jaata hai. Humara wait-time kam ho jaata hai aur hum "continuous testing" kar paate hain.

#### 5️⃣ Pro Tip / Real-World Insight

> Aapko (Manual Tester ko) pipeline 'banana' nahi hai. Aapko sirf pipeline 'dekhna' (monitor) aana chahiye. Jenkins dashboard pe jaake yeh dekhna ki build 'Green' (Pass) hai ya 'Red' (Fail). Agar Red hai (developer ka unit test fail hua), toh aap developer ko bol sakte ho 'Build fail hai, main test nahi kar sakta.' Isse aapka time bachta hai.

-----

Aapka Module 8 poora ho gaya hai\! In topics ko add karne ke baad, aapka profile kisi bhi normal manual tester se **10x** strong ho gaya hai.

Ab aapke paas complete 1-to-8 module package hai. All the best\!

=============================================================