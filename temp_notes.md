# Section 1: Not of use


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 2: Introduction & Fundamentals


### 🏁 Section 2: Introduction & Fundamentals

Yeh section bootcamp ki foundation set karta hai — bug bounty mindset, ethical boundaries, aur AI-assisted recon se automated reporting tak ki end-to-end strategy.

---

### 🎯 1. Bug Bounty Mindset & Best Practices

Is topic mein hum seekhenge ki ek successful bug bounty hunter ka mindset kaisa hona chahiye, AI aur LLMs ka sahi use kya hai, aur kyun SSRF ya Broken Access Control jaise bugs ko apni methodology se exclude nahi karna chahiye.

*(Note: Yeh topic Surface Level & Conceptual hai, isliye Context-Aware Flexibility rule ke according sirf Top 7 critical points diye gaye hain.)*

#### 📖 3. Technical Definition

* **Precise English:** A holistic pentesting methodology requires out-of-the-box thinking, where automation handles repetitive discovery and reconnaissance phases, while human cognition focuses on uncovering zero-days and complex logic flaws.
* **Hinglish Simplification:** Bug bounty sirf tools chalana nahi hai, balki creative thinking lagake un hidden areas ko test karna hai jinhe baaki log chhod dete hain.

#### 🧠 4. Why This Matters (Pentester/Red Teamer ke liye Zaroorat Kyun Hai?)

* **Problem:** Log aksar apne favorite bug types tak limited reh jaate hain. Agar koi sirf XSS dhundh raha hai, toh woh saamne pada SSRF miss kar dega.
* **Solution:** Ek solid **pentesting methodology** (security testing ka step-by-step framework) honi chahiye jisme har category cover ho. AI aur shell scripting se boring task automate karo taaki dimag actual hacking pe focus kare.
* **What breaks if we don't know this?** Tum hamesha duplicates ya low-hanging fruits pe atak jaoge aur real **zero days** (aisi vulnerabilities jo abhi tak vendor ko bhi nahi pata) miss kar doge.
* **✅ Kab use karo (Use in engagement when):** Jab **reconnaissance phase** (target ke baare mein information gather karne ka initial step) mein **hidden attack surface**, **hidden assets**, aur **hidden content** dhundhna ho, toh **shell scripting** (terminal commands ko ek file mein automate karna) aur **low code** scripts use karo.
* **❌ Kab mat karo / Alternative prefer karo:** **LLM** (Large Language Model, jaise ChatGPT) ya **AI bot** ko direct exploit likhne ya zero-day dhundhne ke liye use mat karo — woh sirf syntax aur logic refine karne mein assist kar sakte hain.

> **💡 7. Concept Visualization (Theory Topic ke liye):**
> Yeh purely conceptual topic hai — Hands-On section ki jagah Concept Visualization de raha hoon.
> **Mindset Shift Flow:**
> 1. **Initial Approach:** Sirf favorite bugs dhundhna → **Better Approach:** Har category ko test karna ("Don't discriminate with programs or bug categories while reporting").
> 2. **Automation Shift:** Manual discovery → **Better Approach:** Shell scripting use karke hidden assets aur content discovery ko fast karna.
> 3. **AI Utilization:** "AI mere liye bug dhundhega" → **Better Approach:** "Main AI bot ko repetitive tasks aur code analysis ke liye use karunga, par **out of the box** thinking meri hogi."
> 
> 

#### 🔒 8. Attack Surface & Defense (Dual Perspective)

* **🔴 Attacker Perspective:** Red teaming aur bug bounty mein sabse badi jeet **hidden attack surface** dhundhne mein hoti hai. Attackers **SSRF** (Server-Side Request Forgery — server ko trick karke internal network mein request bhejna) aur **broken access control** (unauthorized access mil jana, jaise admin panel bina login ke) jaisi vulnerabilities pe focus karte hain jo automated scanners miss kar dete hain.
* **🔵 Defender Perspective:** Defenders ko apni asset inventory update rakhni padti hai, warna shadow IT aur hidden content attackers ke liye open entry point ban jaate hain.

#### ⚠️ 10. Pentest Anti-Patterns & Common Mistakes (Beginner Traps)

* **❌ Mistake:** Sochna ki "SSRF toh mujhe kabhi nahi milegi" aur usse test hi nahi karna.
* **🤦 Why:** Beginners ko lagta hai ki complex bugs sirf pros ko milte hain.
* **✅ The 'Pro' Way:** Apni testing methodology mein har bug category ko include karo, chahe target kaisa bhi ho. Bug bounty tips yahi kehti hain ki discrimination mat karo.
* **⚡ Consequences:** Tum critical findings miss kar doge aur target ka actual impact demonstrate nahi kar paoge.

#### 🔑 18. Keywords Coverage Verification

```text
🔑 Keywords Coverage Check — Bug Bounty Mindset & Best Practices
✅ Covered   : bug bounty tips, out of the box, LLM, AI bot, zero days, red teaming, pentesting methodology, shell scripting, low code, broken access control, SSRF, methodology, hidden attack surface, hidden assets, hidden content, discovery, reconnaissance phase
⚠️ Mentioned but needs more depth : (none)
❌ MISSED    : (none)

```

> ✅ Verified: 100% keyword coverage achieved for this topic.

---

### 🎯 1. Ethics, Rules of Engagement & Community

Is topic mein hum ethical hacking ke limits, triagers ke saath professional communication, aur critical data (like PII/KYC) handle karne ke rules seekhenge. Yeh Moderate depth ka conceptual topic hai, isliye full 18-point structure with visual flow diya gaya hai.

#### 🐣 2. Simple Analogy (Hinglish)

Socho tum ek bank ke security guard ho jiska kaam vault ka lock test karna hai. Agar tumhe lock khula mil jaye, toh tumhara kaam hai bank manager ko batana. Agar tum vault ke andar jaake cash ginnne lago ya documents ki photo lene lago — toh tum guard nahi, chor kehlaoge. Same bug bounty mein hota hai, vulnerability milne par limit cross nahi karni hoti.

#### 📖 3. Technical Definition

* **Precise English:** Adhering to the Rules of Engagement (RoE) ensures security testing remains within legal boundaries, prioritizing proof of concept over data exfiltration, especially regarding sensitive PII or KYC data.
* **Hinglish Simplification:** Hacking karte waqt company ki di gayi rules aur limits ko strictly follow karna, aur critical data ko access kiye bina apna impact prove karna.

#### 🧠 4. Why This Matters

* **Problem:** Agar tum **SQL injection** (SQLi — database queries ko manipulate karke unauthorized data nikalna) exploit karte waqt user ka real data dump kar loge, toh legal trouble mein fas sakte ho.
* **Solution:** Apni limits jano. **Scope** (jo targets test karne ke liye allowed hain) aur **exclusion** (jo explicitly test karne se mana kiya gaya hai) ki **policies** ko properly padho.
* **What breaks?** Target organization trust loose kar degi, tumhe ban kar diya jayega, aur legal action ho sakta hai.
* **✅ Kab use karo:** Jab bhi **database** ka access mile ya koi **critical information** samne aaye, turant pause karo aur permission lo.
* **❌ Kab mat karo:** Kabhi bhi production server pe destructive commands (jaise `DROP TABLE` ya mass delete) run mat karo.

#### 🔍 5. Visual / Terminal Mein Kya Dikhega

*(N/A — is concept mein koi direct terminal state nahi hota, yeh strictly behavior aur reporting process par based hai.)*

#### ⚙️ 6. Under the Hood (Deep Dive — Attack/Defense Flow)

1. **(1) Discovery:** Attacker ko SQL injection vulnerability milti hai.
2. **(2) Exploitation:** Attacker database se connect hota hai.
3. **(3) The Limit:** Attacker ko users ke **PII** (Personally Identifiable Information — jaise naam, email, phone) aur **KYC information** (Know Your Customer — jaise Aadhar/Passport details) ke tables dikhte hain.
4. **(4) Ethical Action:** Yahan data dump (download) karne ke bajaye, attacker sirf version details (`SELECT @@version`) ya basic columns ka structure nikalta hai as proof.

> **💡 7. Concept Visualization (Theory Topic ke liye):**
> Yeh purely conceptual topic hai — Hands-On section ki jagah Concept Visualization de raha hoon.
> **Ethical Reporting Flow:**
> 1. Exploit the vulnerability safely.
> 2. Document the exact steps (without accessing PII/KYC).
> 3. Record **video POC** (Proof of Concept — screen recording jo dikhaye attack kaise hua) ya **screenshots** lo.
> 4. Draft a clear **bug report**.
> 5. Submit to **triagers** (bug bounty platforms ke security engineers jo report verify karte hain).
> 
> 

#### 🔒 8. Attack Surface & Defense

* **🔴 Attacker Perspective:** Penetration tester ka goal sirf **impact** (attack se business ko kya nuksan ho sakta hai) dikhana hota hai. Poora data churana zaroori nahi hai.
* **🔵 Defender Perspective:** Defenders scope set karte hain taaki production data safe rahe. Agar tester out of scope jata hai, toh incident response team usse real attack samajh ke block kar deti hai.

#### 🌍 9. Real-World Penetration Testing Use-Case

Bug bounty platforms (HackerOne, Bugcrowd) par sabse zyada reports reject hone ka reason incomplete ya disrespectful communication hota hai. Agar tumhe koi bug milta hai, toh **community contributions** (dusre hackers ke liye writeups ya tools open-source karna) aur professional **bug report** likhna **cybersecurity domain** mein tumhari reputation banata hai. Triagers din mein 100+ reports padhte hain, clear video POC unka time bachata hai aur tumhe jaldi bounty milti hai.

#### ⚠️ 10. Pentest Anti-Patterns & Common Mistakes (Beginner Traps)

* **❌ Mistake:** PII/KYC data dump karke screenshot bhejna taaki "critical severity" proof ho sake.
* **🤦 Why:** Beginners ko lagta hai jitna sensitive data dikhayenge, utne zyada paise milenge.
* **✅ The 'Pro' Way:** "Knowing limits in bug hunting" — database ke schema/structure ka screenshot lo, aur report mein explicitly mention karo ki "Maine KYC table access nahi kiya to respect the rules of engagement."
* **⚡ Consequences:** Organization data breach declare kar degi aur bounty dene ki jagah tum par legal action le legi.

#### 🤔 11. Agar Dimag Ghoom Raha Hai? (Confusion Clarifier)

* **Confusion 1 — "Kya out-of-scope asset pe bug mile toh report kar sakte hain?"**
* **Galat soch:** Bug toh bug hai, reward milna hi chahiye.
* **Actually:** Agar target clearly "exclusion" policy mein hai, toh test karna illegal hai.
* **Prove karo:** Program ki policy page pe "Out of Scope" section verify karo, wahan clearly likha hota hai ki in domains pe testing strictly prohibited hai.


* **Confusion 2 — "Kya triagers mere bugs jaan-बूझ ke reject karte hain?"**
* **Galat soch:** Triagers bounty nahi dena chahte.
* **Actually:** Triagers humans hain aur unse galti ho sakti hai.
* **Prove karo:** Agar report clear nahi hogi toh reject hogi. Same bug ki video POC bana ke bhejo, chances of acceptance badh jayenge.



#### 🛠️ 12. Troubleshooting Flowchart (Tool/Exploit Issues)

* **`[Report marked as N/A or Informative by Triager]`**
* **Root Cause:** Report mein actual business impact properly elaborated nahi hai.
* **Fix:** Report ko update karo aur clear business logic samjhao ki company ko isse kya financial ya reputational loss hoga.



#### ⚖️ 13. Comparison (Tool vs Tool / Technique vs Technique)

| Feature | Professional Hunter | Amateur Hunter |
| --- | --- | --- |
| **Data Handling** | Stops at proof, never dumps KYC/PII | Tries to download entire database |
| **Communication** | Respectful to triagers, clear bug report | Argues with triagers, vague steps |
| **Community** | **Open sourced** tools, shares writeups | Keeps everything secret |

#### 🔄 14. Kill Chain & Attack Phase Flow

* ⚔️ **Attack Phase:** Reporting / Post-Exploitation
* 📍 **Kill Chain Position:** Execution of exploitation -> Post-Exploitation -> Reporting
* 🔗 **This connects to:** Reconnaissance (finding the bug) and Payment/Bounty (after successful triage).
* 🔄 **Flow:** Exploit -> Realize sensitive access (SQLi database) -> Pause -> Record Video POC -> Write clear bug report -> Communicate with triagers.

#### 🎨 15. Visual Diagram (ASCII Art — Attack Flow / Network Topology)

```text
[Vulnerable Server] 
       │ (SQL Injection)
       ▼
[Database Access] ───(❌ DON'T)──▶ [Dump KYC/PII Data] (Banned!)
       │
       └───(✅ DO)──▶ [Run `SELECT user()`] 
                         │
                         ▼
                  [Take Screenshot / Video POC]
                         │
                         ▼
                  [Submit Bug Report to Triager]

```

#### ❓ 16. Interview & Certification Exam Q&A

* **Q:** You found an RCE on an in-scope server. You notice a folder named "Customer_Credit_Cards". What is your next step?
* **A:** Immediately stop. Do not open or copy the folder. Take a screenshot showing the directory listing (like `ls -la`) to prove access, write the report, and notify the organization about the critical exposure. Reading PII/Financial data violates the rules of engagement.
* **Q:** How do you ensure your bug report gets triaged effectively?
* **A:** By providing clear steps to reproduce, an accurate assessment of the business impact, and attaching a high-quality video POC so the triager can replicate the issue without guesswork.

#### 📝 17. One-Line Memory Hook

"Access mile toh shor machao, par database se data kabhi mat churao!" (Impact dikhana hai, PII/KYC data dump nahi karna).

#### 🔑 18. Keywords Coverage Verification

```text
🔑 Keywords Coverage Check — Ethics, Rules of Engagement & Community
✅ Covered   : triagers, bug report, impact, community contributions, open sourced, cybersecurity domain, critical information, KYC information, PII, SQL injection, database, screenshots, video POC, scope, exclusion, policies
⚠️ Mentioned but needs more depth : (none)
❌ MISSED    : (none)

```

> ✅ Verified: 100% keyword coverage achieved for this topic.

---

### 🎯 3. Bootcamp Strategy - Recon to Reporting

Is topic mein hum overall bootcamp approach samjhenge: AI ki power use karke target ka deep recon kaise karein, aur end mein ek solid automated report kaise generate karein jo time bachaye aur impact maximize kare.

*(Note: Yeh topic Surface Level & Conceptual hai, isliye Context-Aware Flexibility rule ke according sirf Top 7 critical points diye gaye hain.)*

#### 📖 3. Technical Definition

* **Precise English:** The strategic approach involves leveraging AI to enhance attack surface management, scale asset and content discovery, and streamline the reporting process for maximum efficiency.
* **Hinglish Simplification:** Bootcamp ka aim hai manual kaam ko AI se fast karna — chahe woh target ke hidden subdomains dhundhna ho, ya end mein bug report likhna ho.

#### 🧠 4. Why This Matters

* **Problem:** Normal **recon** (target ki information jama karna) aur **manual reporting** mein **bug bounty researchers** apna 70% time waste kar dete hain.
* **Solution:** **AI** ka use karo **reconnaissance** ko scale karne ke liye aur **automated reports** generate karne ke liye.
* **What breaks?** Bina automation aur structured approach ke, tum unhi targets pe ghoomte rahoge jahan baaki log already test kar chuke hain.
* **✅ Kab use karo:** Jab target ki **attack surface management** (target ke saare public assets aur unke risks track karna) karni ho, taaki **untouched targets** aur **commonly overlooked areas** mil sakein.
* **❌ Kab mat karo:** AI pe completely rely mat karo for logic-based vulnerabilities; wahan manual testing hi kaam aati hai.

> **💡 7. Concept Visualization (Theory Topic ke liye):**
> Yeh purely conceptual topic hai — Hands-On section ki jagah Concept Visualization de raha hoon.
> **Bootcamp Workflow Pipeline:**
> 1. **Asset Discovery:** AI + Tools se domains/subdomains dhundhna.
> 2. **Content Discovery:** Hidden directories, APIs, aur **hidden assets** map karna.
> 3. **Vulnerability Hunting:** Focus on **commonly overlooked areas** jahan dusre **pentesters** nahi jaate.
> 4. **Reporting:** AI ka use karke **steps to reproduce**, **screenshots**, aur **video POCs** ko ek professional **automated report** mein convert karna.
> 
> 

#### 🔒 8. Attack Surface & Defense (Dual Perspective)

* **🔴 Attacker Perspective:** Attacker ka goal hamesha **untouched targets** dhundhna hota hai. Agar koi sub-domain 5 saal purana hai aur kisi ne dhundha nahi, toh wahan bug milne ke chances 10x hote hain. **Asset discovery** (naye servers dhundhna) aur **content discovery** (hidden files/folders dhundhna) iske primary tools hain.
* **🔵 Defender Perspective:** Defenders ko apni puri digital footprint monitor karni hoti hai. Agar attacker ko hidden asset mil gaya jo defender ko nahi pata tha (shadow IT), toh system compromise ho jayega.

#### ⚠️ 10. Pentest Anti-Patterns & Common Mistakes (Beginner Traps)

* **❌ Mistake:** Main domain (jaise `www.target.com`) pe seedha scanner chala dena aur hidden assets ko ignore karna.
* **🤦 Why:** Beginners ko lagta hai ki samne jo website dikh rahi hai bas wahi hack karni hai.
* **✅ The 'Pro' Way:** Proper **reconnaissance** karo. Un commonly overlooked areas ko test karo jahan developers se galti hone ke chances zyada hote hain (jaise old API versions, staging servers).
* **⚡ Consequences:** Agar tum deep asset discovery nahi karoge, toh hamesha unhi bugs ke liye compete karoge jo hazaaron researchers already dhundh rahe hain — output hamesha "Duplicate" aayega.

#### 🔑 18. Keywords Coverage Verification

```text
🔑 Keywords Coverage Check — Bootcamp Strategy - Recon to Reporting
✅ Covered   : recon, reporting, reconnaissance, attack surface management, asset discovery, content discovery, hidden assets, AI, untouched targets, commonly overlooked areas, pentesters, bug bounty researchers, impact, steps to reproduce, screenshots, video POCs, automated reports, manual reporting
⚠️ Mentioned but needs more depth : (none)
❌ MISSED    : (none)

```

> ✅ Verified: 100% keyword coverage achieved for this topic.

---

### ✅ Section Completion Checklist: Introduction & Fundamentals

* [x] Topic 1: Bug Bounty Mindset & Best Practices
* [x] Topic 2: Ethics, Rules of Engagement & Community
* [x] Topic 3: Bootcamp Strategy - Recon to Reporting
Total Topics: 3 | Total Keywords: 51 | CVEs: 0 | Missed: 0

> ✅ **Notes Guru confirms:** Poora Section complete ho gaya. All rules, keywords, and format strictly followed!

---

🛑 **PART 1 FINISHED.** Agle section ka skeleton paste karo and type **'CONTINUE'** to proceed! 🚀


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 3: Bug Bounty Techniques




━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━




━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━