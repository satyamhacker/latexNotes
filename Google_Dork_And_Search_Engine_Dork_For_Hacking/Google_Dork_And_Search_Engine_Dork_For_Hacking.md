# **Google Dork And Search Engine Dorking: Zero-to-Hacker Notes** 🚀

---

# **Module 1: Basic Search Operators (Google Foundation)**

---

## **Topic 1: Introduction to Google Dorking (What & Why for Pentesters)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Google Dorking** - Search engine ko advanced commands se control karke hidden/sensitive information dhoondhna.

### 2. **Ye Kya Hai? (What is it?)**
Google Dorking (ya Google Hacking) ek technique hai jismein aap Google ke advanced search operators ka use karke woh information dhoondhte ho jo normally search results mein nahi aati. 

**Analogy:** Socho Google ek library hai. Normal search mein aap librarian se "security books" maangte ho. Dorking mein aap kehte ho "Mujhe 2020 ke baad ki, sirf PDF format ki, author 'John' ki security books chahiye, aur jinke title mein 'penetration' word ho." Yeh specific aur powerful hai! 🎯

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- **Reconnaissance ka Foundation:** Pentesting ka pehla phase (information gathering) mein yeh sabse powerful tool hai.
- **Hidden Data Exposure:** Companies galti se sensitive files (configs, passwords, databases) public kar deti hain - dorking se yeh mil jaate hain.
- **Time-Saving:** Manual browsing ki jagah, ek dork 10 minutes mein 1000+ vulnerable sites dhoondh sakta hai.
- **Legal OSINT:** Yeh 100% legal hai (jab tak aap sirf search kar rahe ho, access nahi kar rahe).

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- **Pre-Engagement Phase:** Jab client ne target diya ho aur aapko uski public footprint samajhni ho.
- **Bug Bounty Programs:** Jab aap exposed endpoints, admin panels, ya sensitive files dhoondhna chahte ho.
- **Competitive Analysis:** Apne competitors ki technology stack, subdomains, ya leaked data dekhne ke liye.
- **Vulnerability Research:** Specific software/version waale sites dhoondhne ke liye (jismein known vulnerabilities ho).

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- **Incomplete Recon:** Aap target ke 70% attack surface miss kar doge - exposed admin panels, backup files, error pages sab chhoot jaayenge.
- **Time Waste:** Manual browsing mein weeks lag jaayenge jo dorking 1 hour mein kar deti hai.
- **Competitive Disadvantage:** Dusre pentesters/hackers (black hat) yeh techniques use karke pehle vulnerabilities dhoondh lenge.

### 6. **Syntax aur Common Options**
Google Dorking mein koi special software nahi chahiye - seedha Google.com par type karo:

```
operator:value keyword
```

**Common Operators (Module 1 ke liye):**
- `"exact phrase"` - Exact match dhoondhta hai
- `-keyword` - Results se exclude karta hai
- `OR` / `|` - Multiple options mein se koi ek
- `*` - Wildcard (kuch bhi ho sakta hai)
- `..` - Number range

### 7. **Example 1 (Basic)**
**Dork:**
```
"penetration testing" -course
```

**Kya Hoga:**
- Google "penetration testing" phrase ko exactly dhoondhega
- Lekin jis page mein "course" word hai, usko skip karega
- Result: Actual pentesting reports/articles milenge, training courses nahi

**Output:** Real-world pentesting case studies aur whitepapers.

### 8. **Example 2 (Pentester-Focused)**
**Dork:**
```
"index of" "backup" filetype:sql site:edu
```

**Analysis:**
- `"index of"` - Exposed directory listings dhoondhta hai
- `"backup"` - Jismein backup files ho
- `filetype:sql` - Sirf SQL database files
- `site:edu` - Sirf educational institutions ki sites par

**Output:** University websites ke exposed SQL backup files - inmein student data, admin credentials ho sakte hain (ethical testing ke liye gold!).

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- **Spaces ka Galat Use:** `site: example.com` (galat) vs `site:example.com` (sahi) - operator aur value ke beech space nahi hona chahiye.
- **Quotes Bhoolna:** `admin login` (lakhs results) vs `"admin login"` (specific results) - exact match ke liye quotes zaroori hain.
- **Legal Line Cross Karna:** Search karna legal hai, lekin dhoondhne ke baad us site par login try karna ya files download karna (bina permission) crime hai! 🚨

### 10. **Best Practices / Pro Tips**
- **Combine Operators:** Ek dork mein 3-4 operators use karo for laser-focused results: `site:target.com filetype:pdf "confidential"`
- **Use Google's Tools:** Search karne ke baad "Tools" button se time range set karo (e.g., "Past year") - purane results filter ho jaayenge.
- **Document Everything:** Jo bhi dorks kaam kare, unhe note karo - next pentest mein reuse kar sakte ho.

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**
Ek pentester ko "XYZ Bank" ka security audit karna tha. Usne Google par `site:xyzbank.com filetype:xls "password"` dork chalaya. Results mein ek Excel file mili jismein 200+ employee credentials the (jo ek careless admin ne accidentally public folder mein upload kar diya tha). Pentester ne yeh finding report ki, aur bank ne turant file remove karke apni access controls fix kiye. Yeh ek classic example hai ki dorking se kaise critical vulnerabilities milti hain - bina kisi hacking tool ke, sirf Google se! 🎯

### 12. **Checklist / Chota Recap (TL;DR)**
✅ Google Dorking = Advanced search operators se hidden info dhoondhna  
✅ Pentesting ke reconnaissance phase ka core tool  
✅ Legal hai (jab tak sirf search kar rahe ho)  
✅ Operators mein space nahi, exact match ke liye quotes use karo  
✅ Multiple operators combine karke powerful dorks banao  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kya Google Dorking illegal hai?**  
**A:** Nahi! Google par search karna 100% legal hai. Illegal tab hota hai jab aap dhoondhne ke baad unauthorized access karte ho (login, download, modify). Rule yaad rakho: "Look, don't touch." 👀

**Q2: Kya Google mujhe block kar dega agar main bahut saare dorks chalaunga?**  
**A:** Haan, agar aap bahut fast aur automated queries bhejoge toh Google CAPTCHA dikha sakta hai ya temporarily block kar sakta hai. Solution: Queries ke beech 10-15 second ka gap rakho, ya VPN use karo.

**Q3: Dorking se kya sach mein sensitive data milta hai?**  
**A:** Bilkul! Daily basis par exposed passwords, database backups, config files milte hain. Lekin yaad rakho - yeh data report karne ke liye hai (responsible disclosure), exploit karne ke liye nahi.

### 14. **Practice ke liye Task**
**Task:** Google par yeh dork chalao aur results analyze karo:

```
"index of" "parent directory" "password.txt"
```

**Kya Karna Hai:**
1. Dork ko Google mein paste karo
2. Pehle 5 results open karo (kisi bhi site par login mat karna!)
3. Dekho ki kis type ki sites exposed hain (personal blogs, small companies, etc.)
4. Note karo ki yeh exposure kyun dangerous hai

**Expected Learning:** Aapko samajh aayega ki kitni easily sensitive files internet par mil jaati hain, aur yeh pentesters ke liye kyun important hai.

### 15. **Aakhri Choti Summary (5 lines)**
- 🎯 Google Dorking advanced search operators ka use karke hidden information dhoondhne ki technique hai
- 🔍 Pentesting ke reconnaissance phase mein yeh sabse powerful aur legal tool hai
- ⚡ Operators ko combine karke (site:, filetype:, quotes) laser-focused results milte hain
- 🚨 Sirf search karna legal hai - unauthorized access crime hai
- 💪 Practice se aap 10 minute mein woh dhoondh sakte ho jo manual browsing mein weeks lega

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Google Dorking ek magnifying glass hai - yeh cheezon ko bada karke dikhata hai, lekin unhe chhoona aapki zimmedari hai. Ethical hacker hamesha 'Look, Don't Touch' rule follow karta hai!" 🔐

---



## **Topic 2: Exact Match (`"..."`) & Exclude (`-`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Exact Match & Exclude** - Search results ko precise banane ke liye quotes aur minus operators.

### 2. **Ye Kya Hai? (What is it?)**
**Exact Match (`"..."`):** Jab aap kisi phrase ko quotes mein daalte ho, toh Google exactly wahi phrase dhoondhta hai - same order, same words.

**Exclude (`-`):** Minus sign se aap unwanted keywords ko results se bahar kar sakte ho.

**Analogy:** Socho aap pizza order kar rahe ho. Exact match matlab "Mujhe **exactly** mushroom aur olives chahiye" (quotes = strict order). Exclude matlab "Lekin onions **bilkul nahi** chahiye" (minus = remove karo). 🍕

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- **Noise Reduction:** Bina quotes ke Google synonyms aur related words bhi dikhata hai - quotes se sirf relevant results milte hain.
- **Targeted Recon:** Pentesting mein specific error messages, exact config file names, ya particular software versions dhoondhne ke liye.
- **Time Efficiency:** 10,000 results se 100 relevant results tak pahunchne mein yeh operators critical hain.
- **False Positives Kam:** Exclude se training sites, forums, aur irrelevant content filter ho jaata hai.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- **Error Message Hunting:** Jab specific error text dhoondhni ho: `"SQL syntax error" site:target.com`
- **Version-Specific Search:** Particular software version: `"Apache/2.4.29" "Server at"`
- **Filtering Noise:** Jab results mein courses/tutorials aa rahe ho: `penetration testing -course -tutorial -training`
- **Exact File Names:** Specific config files: `"wp-config.php" "DB_PASSWORD"`

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- **Information Overload:** Bina quotes ke lakhs irrelevant results milenge - 90% time waste hoga.
- **Missed Vulnerabilities:** Exact error messages ya config patterns miss ho jaayenge jo vulnerabilities indicate karte hain.
- **Poor Reporting:** Client ko dikhane ke liye precise evidence nahi milega.

### 6. **Syntax aur Common Options**
```
"exact phrase here"          # Exact match
keyword -unwanted            # Exclude single word
keyword -"unwanted phrase"   # Exclude phrase
"exact" -exclude1 -exclude2  # Combine both
```

**Important Rules:**
- Quotes ke andar ka text exactly match hona chahiye
- Minus sign aur keyword ke beech **NO SPACE**
- Multiple excludes ek saath use kar sakte ho

### 7. **Example 1 (Basic)**
**Without Quotes:**
```
admin login page
```
**Results:** Admin tutorials, login form designs, page templates - sab kuch mixed.

**With Quotes:**
```
"admin login page"
```
**Results:** Sirf woh pages jinke title/content mein exactly yeh phrase hai - actual admin panels.

**Difference:** 5 million results → 50,000 focused results! 🎯

### 8. **Example 2 (Pentester-Focused)**
**Dork:**
```
"Index of /" "Parent Directory" "backup.sql" -forum -stackoverflow
```

**Analysis:**
- `"Index of /"` - Exposed directory listings (exact phrase)
- `"Parent Directory"` - Apache directory browsing enabled
- `"backup.sql"` - SQL backup files present
- `-forum -stackoverflow` - Discussion sites ko exclude karo (sirf real exposed sites chahiye)

**Output:** Live websites jinke SQL backups publicly accessible hain, bina noise ke. Yeh direct vulnerability hai! 🔥

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- **Space After Minus:** `admin -login` (sahi) vs `admin - login` (galat) - space dalne se exclude kaam nahi karega.
- **Quotes Mismatch:** `"admin login` (incomplete quotes) - Google confuse ho jaayega.
- **Over-Excluding:** `hacking -tutorial -course -guide -learn -training` - itna exclude karoge toh kuch bacha hi nahi! Balance chahiye.

### 10. **Best Practices / Pro Tips**
- **Combine with Other Operators:** `site:gov "confidential" -pdf` - government sites par confidential content, lekin PDFs nahi.
- **Use for Error Messages:** Exact error text quotes mein dalo: `"Fatal error: Uncaught exception"` - yeh vulnerable sites dhoondhne ka shortcut hai.
- **Exclude Common Noise:** Hamesha `-site:youtube.com -site:github.com` jodo agar tutorials nahi chahiye.

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**
Ek bug bounty hunter "TechCorp" ke exposed credentials dhoondh raha tha. Usne pehle `TechCorp password` search kiya - 2 million results aaye (mostly news articles aur tutorials). Phir usne dork change kiya: `"TechCorp" "password" filetype:txt -site:reddit.com -site:twitter.com`. Results mein ek pastebin link mila jismein 500+ employee credentials the jo ek disgruntled ex-employee ne leak kiye the. Hunter ne responsible disclosure ki, company ne passwords reset kiye, aur use $5000 bounty mila. Yeh exact match aur exclude ki power hai! 💰

### 12. **Checklist / Chota Recap (TL;DR)**
✅ Quotes (`"..."`) = Exact phrase match, noise kam karta hai  
✅ Minus (`-`) = Unwanted keywords exclude karta hai  
✅ Minus aur keyword ke beech space nahi hona chahiye  
✅ Multiple excludes ek saath use kar sakte ho  
✅ Error messages aur config files ke liye quotes essential hain  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kya main multiple phrases ko quotes mein daal sakta hoon?**  
**A:** Haan! `"admin panel" "login required"` - dono phrases separately exact match honge. Lekin agar aap chahte ho ki dono ek saath ho, toh: `"admin panel login required"` (ek hi quote mein).

**Q2: Exclude karne ke baad bhi unwanted results aa rahe hain, kyun?**  
**A:** Check karo ki minus aur keyword ke beech space toh nahi hai. Aur Google kabhi-kabhi synonyms dikhata hai - zyada specific keywords use karo ya quotes add karo.

**Q3: Kitne words tak quotes use kar sakte hain?**  
**A:** Technically koi limit nahi, lekin 5-7 words se zyada ka phrase rarely exact match hota hai. Chhote, specific phrases zyada effective hain.

### 14. **Practice ke liye Task**
**Task:** Yeh dono dorks chalao aur difference note karo:

**Dork 1 (Without Operators):**
```
database backup sql
```

**Dork 2 (With Operators):**
```
"database backup" filetype:sql -tutorial -github
```

**Kya Karna Hai:**
1. Dono dorks Google mein separately search karo
2. Pehle 10 results compare karo
3. Note karo: Dork 2 mein kitne zyada relevant results hain
4. Dekho ki Dork 2 ne kaunse noise (tutorials, code repos) filter kiye

**Expected Learning:** Aapko practical difference samajh aayega ki operators kaise search quality improve karte hain.

### 15. **Aakhri Choti Summary (5 lines)**
- 🎯 Quotes (`"..."`) exact phrase match karte hain - noise 90% kam ho jaata hai
- ❌ Minus (`-`) unwanted keywords/sites ko results se remove karta hai
- ⚡ Dono operators ko combine karke laser-focused pentesting dorks banao
- 🔧 Error messages aur config file names hamesha quotes mein dalo
- 💡 Space management critical hai - minus aur keyword ke beech NO SPACE

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Quotes aur Minus Google dorking ke 'sniper rifle' hain - bina inke aap shotgun se fire kar rahe ho (sab jagah hit, target miss). Precision chahiye toh yeh dono master karo!" 🎯

---

## **Topic 3: AND / OR (`|`) & Grouping (`( )`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Logical Operators** - Multiple conditions ko combine karke complex search queries banao.

### 2. **Ye Kya Hai? (What is it?)**
**AND (Default):** Jab aap multiple keywords likhte ho, Google automatically AND use karta hai - matlab saare keywords present hone chahiye.

**OR (`|`):** Pipe symbol se aap alternatives de sakte ho - koi bhi ek keyword match ho jaaye, result aayega.

**Grouping (`( )`):** Parentheses se aap operators ko group kar sakte ho, jaise maths mein BODMAS.

**Analogy:** Restaurant mein order karte waqt: "Mujhe pizza **AND** coke chahiye" (dono chahiye). "Mujhe pizza **OR** burger chahiye" (koi ek). "Mujhe (pizza OR burger) AND coke chahiye" (grouping - drink fixed, food flexible). 🍔

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- **Multiple Targets:** Ek hi dork mein multiple companies/domains search kar sakte ho.
- **Variation Handling:** Same cheez ke different names (admin/administrator, login/signin) ek saath dhoondho.
- **Complex Logic:** Real-world pentesting mein simple searches kaam nahi karte - complex conditions chahiye.
- **Efficiency:** 5 alag dorks ki jagah 1 powerful dork - time 80% save.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- **Multiple Domains:** Bug bounty program mein multiple subdomains: `site:admin.target.com | site:dev.target.com`
- **Synonym Search:** Different terms for same thing: `(administrator | admin | root) login`
- **File Type Variations:** Multiple formats: `filetype:xls | filetype:xlsx "password"`
- **Version Hunting:** Specific vulnerable versions: `"Apache" ("2.4.29" | "2.4.30" | "2.4.49")`

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- **Repetitive Work:** Har variation ke liye alag dork chalana padega - 10x zyada time.
- **Incomplete Coverage:** Ek term miss kiya toh poora attack surface chhoot jaayega.
- **Poor Automation:** Scripts likhte waqt logical operators nahi aaye toh automation fail.

### 6. **Syntax aur Common Options**
```
keyword1 keyword2              # AND (default, space = AND)
keyword1 | keyword2            # OR (pipe symbol)
(keyword1 | keyword2) keyword3 # Grouping with OR
site:domain1.com | site:domain2.com  # Multiple sites
```

**Important Rules:**
- OR ke liye pipe (`|`) use karo, ya capital `OR` likh sakte ho
- Grouping ke liye parentheses `( )` zaroori hain
- Spaces matter: `admin|login` (galat) vs `admin | login` (sahi)

### 7. **Example 1 (Basic)**
**Without OR:**
```
site:target.com admin
site:target.com administrator
site:target.com root
```
(3 alag searches)

**With OR:**
```
site:target.com (admin | administrator | root)
```
(1 search, same results) ⚡

**Benefit:** Time saved + ek hi result page mein saare variations.

### 8. **Example 2 (Pentester-Focused)**
**Dork:**
```
(site:staging.target.com | site:dev.target.com | site:test.target.com) (filetype:env | filetype:config | filetype:ini) ("DB_PASSWORD" | "DATABASE_PASSWORD" | "MYSQL_PASSWORD")
```

**Analysis:**
- First Group: Teen development environments (staging/dev/test - yeh usually less secure hote hain)
- Second Group: Teen config file types
- Third Group: Teen password variable names

**Output:** Development servers ke exposed config files jismein database passwords hain - yeh pentesting ka goldmine hai! Ek dork mein 27 combinations (3×3×3) cover ho gaye! 🎰

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- **Pipe ke Aas-Paas Spaces Nahi:** `admin|login` sometimes kaam nahi karta - `admin | login` safe hai.
- **Parentheses Bhoolna:** `site:a.com | site:b.com filetype:pdf` - yeh confusing hai. Sahi: `(site:a.com | site:b.com) filetype:pdf`
- **OR Overuse:** 20 terms OR se jodoge toh results bahut broad ho jaayenge - 5-7 tak limit rakho.

### 10. **Best Practices / Pro Tips**
- **Group Related Terms:** `(login | signin | authenticate)` - similar meaning waale terms ek group mein.
- **Test Incrementally:** Pehle simple dork test karo, phir OR/grouping add karo - debugging easy hoga.
- **Document Your Logic:** Complex dorks mein comments add karo (notepad mein): `# Searching 3 dev environments for config files`

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**
Ek pentester ko "MegaCorp" ke saare development aur staging environments scan karne the. Manually 15+ subdomains the (dev1, dev2, staging, test, qa, etc.). Usne ek master dork banaya: `(site:dev*.megacorp.com | site:staging*.megacorp.com | site:test*.megacorp.com | site:qa*.megacorp.com) (intitle:"index of" | intitle:"directory listing") (filetype:sql | filetype:bak | filetype:old)`. Ek hi search mein usne 50+ exposed backup files dhoondh li jo production mein migrate hone se pehle accidentally public ho gayi thi. Client impressed hua aur usne yeh dork apne monitoring system mein add kar liya. Yeh grouping aur OR ki real power hai! 🚀

### 12. **Checklist / Chota Recap (TL;DR)**
✅ AND = Default behavior (space = AND)  
✅ OR (`|`) = Alternatives search karne ke liye  
✅ Grouping `( )` = Complex logic banane ke liye  
✅ Pipe ke aas-paas spaces safe hain  
✅ Multiple variations ek dork mein cover karo  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: AND explicitly likhna zaroori hai?**  
**A:** Nahi! Google default mein AND use karta hai. `admin login` automatically `admin AND login` hai. Lekin clarity ke liye kabhi-kabhi likh sakte ho.

**Q2: Kya main OR aur AND dono ek saath use kar sakta hoon?**  
**A:** Bilkul! `(admin | root) AND login` - yeh valid hai. Parentheses se priority clear ho jaati hai.

**Q3: Nested grouping kaam karti hai?**  
**A:** Haan, lekin complex ho jaata hai: `((admin | root) (login | signin)) site:target.com`. Simple rakhne ki koshish karo.

### 14. **Practice ke liye Task**
**Task:** Yeh dork banao aur test karo:

**Requirement:** Aapko `.edu` (educational) sites par SQL ya database backups dhoondhni hain, jo ya toh "backup" folder mein ho ya "old" folder mein, aur file ka naam ya toh "database" ho ya "db" ho.

**Your Dork (Try karo pehle):**
```
[Yahan apna dork likho]
```

**Solution:**
```
site:edu (inurl:backup | inurl:old) (database | db) (filetype:sql | filetype:bak)
```

**Kya Karna Hai:**
1. Apna dork likho (solution dekhe bina)
2. Test karo aur results dekho
3. Solution se compare karo
4. Note karo ki grouping kaise multiple conditions handle kar rahi hai

### 15. **Aakhri Choti Summary (5 lines)**
- 🔗 AND default hai (space = AND), explicitly likhne ki zaroorat nahi
- 🔀 OR (`|`) se alternatives search karo - ek dork mein multiple variations
- 📦 Grouping `( )` se complex logic banao - priority clear hoti hai
- ⚡ Multiple domains/filetypes/keywords ek saath search karke time bachao
- 🎯 Real pentesting mein complex dorks zaroori hain - simple searches incomplete hain

> **📌 Ye Zaroor Yaad Rakhein:**  
> "OR aur Grouping Google dorking ke 'multiplier' hain - ek dork mein 10 dorks ki power aa jaati hai. Master karo toh reconnaissance 10x fast ho jaayega!" ⚡

---

## **Topic 4: Wildcard (`*`) & Range (`..`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Wildcard & Range** - Unknown words handle karo aur number ranges mein search karo.

### 2. **Ye Kya Hai? (What is it?)**
**Wildcard (`*`):** Asterisk ek "joker card" hai - yeh kisi bhi word (ya words) ki jagah le sakta hai. Jab aapko exact phrase nahi pata lekin pattern pata hai, tab use karo.

**Range (`..`):** Do dots se aap number range define kar sakte ho - prices, years, versions, etc.

**Analogy:** Wildcard ek "blank tile" hai Scrabble game mein - kuch bhi ban sakta hai. Range ek "slider" hai - "Mujhe 2020 se 2023 ke beech ki cheezein chahiye". 🎲

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- **Pattern Matching:** Jab exact phrase nahi pata lekin structure pata hai (e.g., "admin * login" - beech mein kuch bhi ho sakta hai).
- **Version Hunting:** Specific version ranges dhoondhne ke liye: `Apache 2.4.*` ya `2019..2022`
- **Flexible Search:** Variations automatically cover ho jaate hain bina multiple dorks ke.
- **Time-Based Recon:** Particular time period ki information: `"data breach" 2020..2023`

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- **Incomplete Phrases:** Jab phrase ka structure pata ho lekin exact words nahi: `"error * database connection"`
- **Software Versions:** Vulnerable version ranges: `"WordPress 5.0" .. "WordPress 5.4"`
- **Year-Based Search:** Historical data: `site:target.com "confidential" 2018..2020`
- **Price Ranges:** (Kam useful pentesting mein, lekin OSINT mein kaam aata hai): `laptop $500..$1000`

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- **Rigid Searches:** Sirf exact matches milenge, variations miss ho jaayenge.
- **Multiple Dorks:** Har variation ke liye alag dork - time waste.
- **Version Gaps:** Vulnerable versions ki range miss kar doge agar ek-ek karke search karoge.

### 6. **Syntax aur Common Options**
```
"keyword * keyword"        # Wildcard in phrase
keyword1 * keyword2        # Wildcard between words
number1..number2           # Number range
"version 2.0".."version 2.5"  # Version range
year1..year2               # Year range
```

**Important Rules:**
- Wildcard usually quotes ke andar use hota hai
- Range mein spaces nahi hone chahiye: `2020..2023` (sahi) vs `2020 .. 2023` (galat)
- Wildcard ek ya multiple words replace kar sakta hai

### 7. **Example 1 (Basic)**
**Without Wildcard:**
```
"admin panel login"
"admin dashboard login"
"admin area login"
```
(3 alag searches)

**With Wildcard:**
```
"admin * login"
```
**Results:** Admin panel login, admin dashboard login, admin area login, admin console login - saare variations ek saath! 🎯

**Range Example:**
```
"iPhone" $300..$600
```
**Results:** $300 se $600 ke beech ki iPhone listings (e-commerce OSINT ke liye useful).

### 8. **Example 2 (Pentester-Focused)**
**Dork:**
```
site:target.com "powered by WordPress 5.*" inurl:wp-admin
```

**Analysis:**
- `"powered by WordPress 5.*"` - WordPress version 5.0, 5.1, 5.2... 5.9 tak saare versions
- Wildcard ne 10+ versions ek saath cover kar liye
- `inurl:wp-admin` - Admin panel accessible hai

**Output:** Target site ke saare WordPress 5.x installations jo potentially vulnerable ho sakte hain (5.x mein multiple CVEs hain). Ek dork mein poora version family scan! 🔥

**Range Example (Pentester):**
```
site:target.com filetype:pdf "confidential" 2019..2021
```
**Output:** 2019 se 2021 ke beech ke confidential PDFs - yeh time range important hai kyunki purane docs mein outdated info (old passwords, decommissioned systems) hoti hai jo still useful hai.

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- **Range Mein Spaces:** `2020 .. 2023` kaam nahi karega - `2020..2023` sahi hai.
- **Wildcard Overuse:** `"* * * login"` - itne wildcards se results bahut broad ho jaayenge, irrelevant bhi aayenge.
- **Wrong Context:** Wildcard text ke liye hai, numbers ke liye range use karo: `"version *"` (sahi) vs `"version 2020..2023"` (agar versions numbers hain toh yeh better).

### 10. **Best Practices / Pro Tips**
- **Combine with Other Operators:** `site:gov "budget * million" filetype:pdf 2020..2023` - government budget docs specific years ki.
- **Test Without Wildcard First:** Pehle exact phrase try karo, agar results kam hain toh wildcard add karo.
- **Use for Error Messages:** `"error * occurred while"` - different error types ek saath milenge.

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**
Ek security researcher "FinanceApp" ke vulnerable versions dhoondh raha tha. Usne pehle `"FinanceApp 2.0"`, `"FinanceApp 2.1"`, `"FinanceApp 2.2"` alag-alag search kiye - bahut time laga. Phir usne wildcard use kiya: `"powered by FinanceApp 2.*" (inurl:login | inurl:admin)`. Ek hi search mein usne 200+ installations dhoondh li jo version 2.0 se 2.9 tak use kar rahi thi. Usne CVE database check kiya aur pata chala ki 2.0-2.5 mein critical SQL injection vulnerability thi. Usne affected sites ko report kiya aur multiple bounties jeeti. Wildcard ne uska recon time 5 hours se 30 minutes kar diya! ⏱️

### 12. **Checklist / Chota Recap (TL;DR)**
✅ Wildcard (`*`) = Kisi bhi word ki jagah le sakta hai  
✅ Range (`..`) = Number ranges search karne ke liye  
✅ Wildcard quotes ke andar use karo for phrases  
✅ Range mein spaces nahi hone chahiye  
✅ Version families aur time periods cover karne ke liye perfect  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Wildcard kitne words replace kar sakta hai?**  
**A:** Ek se 5 words tak usually. Google automatically decide karta hai. `"admin * login"` mein `*` = "panel", "dashboard", ya "console area" (1-2 words).

**Q2: Kya range alphabets ke saath kaam karta hai?**  
**A:** Nahi, sirf numbers ke saath. `A..Z` kaam nahi karega. Alphabets ke liye OR use karo: `(A | B | C)`.

**Q3: Wildcard aur OR mein kya difference hai?**  
**A:** Wildcard unknown words ke liye hai (`"admin * panel"` - beech mein kuch bhi). OR known alternatives ke liye hai (`admin | administrator` - dono pata hain).

### 14. **Practice ke liye Task**
**Task:** Yeh dono scenarios ke liye dorks banao:

**Scenario 1:** Aapko `.gov` sites par "budget report" dhoondhni hai, lekin "budget" aur "report" ke beech koi bhi word ho sakta hai (jaise "budget annual report", "budget quarterly report"). Sirf PDF files chahiye, 2020-2023 ke beech ki.

**Your Dork:**
```
[Yahan likho]
```

**Scenario 2:** Aapko Apache server version 2.4.0 se 2.4.50 ke beech ke exposed servers dhoondhne hain jo "server status" page show kar rahe hain.

**Your Dork:**
```
[Yahan likho]
```

**Solutions:**
```
Scenario 1: site:gov "budget * report" filetype:pdf 2020..2023
Scenario 2: "Apache/2.4.*" "server status" inurl:server-status
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🃏 Wildcard (`*`) unknown words ki jagah leta hai - flexible pattern matching
- 📊 Range (`..`) numbers/years ke beech search karta hai - time-based recon
- 🎯 Version families ek saath cover karo: `"software 2.*"` = 2.0, 2.1, 2.2...
- ⏰ Historical data dhoondhne ke liye range perfect hai: `2018..2021`
- 🔧 Dono operators combine karke powerful temporal + pattern searches banao

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Wildcard aur Range Google dorking ke 'flex tools' hain - jab exact nahi pata, tab yeh kaam aate hain. Ek `*` ya `..` se hundreds of variations automatically cover ho jaate hain!" 🎲

---

# **🎓 Module 1 Complete! Congratulations!**

Aapne **Basic Search Operators** master kar liye! Ab aap:
- ✅ Exact matches aur exclusions use kar sakte ho
- ✅ Logical operators (AND/OR) se complex queries bana sakte ho  
- ✅ Wildcards aur ranges se flexible searches kar sakte ho
- ✅ Google ko apne hisaab se control kar sakte ho

**Next Step:** Module 2 mein aap **Core Dorking Operators** seekhoge - `site:`, `inurl:`, `intitle:`, `filetype:` - yeh real pentesting ka arsenal hai! 🚀

**Practice Reminder:** Har topic ke practice tasks zaroor complete karo - theory se zyada, hands-on practice important hai!

---
=============================================================

# **Google Dork And Search Engine Dorking: Zero-to-Hacker Notes** 🚀

---

# **Module 2: Core Dorking Operators (Pentester Focus)**

---

## **Topic 1: `site:` (Targeting Specific Websites)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**site: Operator** - Specific domain ya subdomain par laser-focused search karo.

### 2. **Ye Kya Hai? (What is it?)**
`site:` operator Google ko kehta hai ki "Sirf is domain/subdomain ke pages dikhao, baaki sab ignore karo." Yeh pentesting ka sabse important operator hai kyunki aap target ko precisely define kar sakte ho.

**Analogy:** Socho ek mall mein 100 shops hain. Normal search matlab "Poore mall mein shoes dhoondho." `site:` operator matlab "Sirf Nike store mein shoes dhoondho, baaki stores ignore karo." 🎯

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- **Target-Specific Recon:** Pentesting mein aapko specific company/domain ki information chahiye hoti hai - `site:` se sirf wahi milta hai.
- **Subdomain Discovery:** Hidden subdomains (dev, staging, admin) dhoondh sakte ho.
- **Attack Surface Mapping:** Target ki poori web presence ek jagah dekh sakte ho.
- **Competitor Analysis:** Competitors ki sites par kya exposed hai, yeh dekh sakte ho.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- **Client Engagement:** Jab client ne specific domain diya ho: `site:targetcompany.com`
- **Bug Bounty:** Program scope mein jo domains hain, unpar focus karne ke liye.
- **Subdomain Enumeration:** Development/staging environments dhoondhne ke liye: `site:*.target.com`
- **TLD-Specific Search:** Specific country/organization types: `site:gov` ya `site:edu`

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- **Unfocused Results:** Lakhs irrelevant sites ke results aayenge - target ki info dhoondhna needle in haystack ban jaayega.
- **Scope Violation:** Bug bounty mein out-of-scope domains par time waste karoge.
- **Incomplete Mapping:** Target ke subdomains miss ho jaayenge jo vulnerable ho sakte hain.

### 6. **Syntax aur Common Options**

```
site:example.com                    # Exact domain
site:*.example.com                  # All subdomains
site:example.com -www               # Exclude www
site:example.com | site:example.org # Multiple domains
site:gov                            # All .gov sites
```

**Important Rules:**
- Operator aur domain ke beech **NO SPACE**: `site:example.com` ✅ vs `site: example.com` ❌
- Wildcard (`*`) subdomains ke liye use kar sakte ho
- Multiple sites ke liye OR (`|`) use karo

### 7. **Example 1 (Basic)**

**Dork:**
```
site:github.com password
```

**Kya Hoga:**
- Sirf GitHub.com par search hoga
- "password" keyword waale pages milenge
- Result: GitHub repos/issues jismein "password" mention hai

**Output:** Potentially leaked passwords ya password-related discussions GitHub par.

### 8. **Example 2 (Pentester-Focused)**

**Dork:**
```
site:*.target.com inurl:admin -www
```

**Analysis:**
- `site:*.target.com` - Target ke saare subdomains (dev.target.com, staging.target.com, etc.)
- `inurl:admin` - URL mein "admin" word ho
- `-www` - Main website (www.target.com) ko exclude karo

**Output:** Target company ke hidden admin panels jo subdomains par hain - yeh usually less secure hote hain aur pentesters ka favorite target! 🎯

**Real Example:**
```
site:tesla.com filetype:pdf confidential
```
**Output:** Tesla ki website par saare confidential PDFs (agar accidentally public hue ho).

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Space After Colon:** `site: example.com` - yeh kaam nahi karega. `site:example.com` sahi hai.
- **Protocol Include Karna:** `site:https://example.com` - galat! Sirf `site:example.com` likho.
- **Wildcard Galat Jagah:** `site:example.*` - yeh TLDs ke liye kaam nahi karta. `site:*.example.com` subdomains ke liye hai.

### 10. **Best Practices / Pro Tips**

- **Subdomain Wildcard:** `site:*.target.com` se hidden subdomains milte hain jo DNS enumeration tools miss kar dete hain.
- **Combine with Filetypes:** `site:target.com filetype:pdf` - target ki saari PDFs ek saath.
- **Exclude Main Site:** `site:target.com -site:www.target.com` - sirf subdomains, main site nahi.
- **TLD Hunting:** `site:gov "budget 2023"` - saari government sites par ek saath search.

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

Ek bug bounty hunter "MegaCorp" ke program mein participate kar raha tha. Scope mein sirf `megacorp.com` aur uske subdomains the. Usne `site:*.megacorp.com inurl:test` dork chalaya aur `test-api.megacorp.com` subdomain mila jo company ne bhool gaya tha. Yeh subdomain purane API endpoints expose kar raha tha jismein authentication nahi tha. Hunter ne isse access karke sensitive customer data dekha (bina download kiye - ethical!), report kiya, aur $10,000 bounty jeeti. Company ne turant subdomain band kar diya. Yeh `site:` operator ki real power hai - forgotten assets dhoondhna! 💰

### 12. **Checklist / Chota Recap (TL;DR)**

✅ `site:` = Specific domain/subdomain par search  
✅ Operator aur domain ke beech NO SPACE  
✅ Wildcard (`*`) se subdomains discover karo  
✅ Multiple domains ke liye OR (`|`) use karo  
✅ Pentesting mein yeh sabse pehla operator hai  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kya `site:*.example.com` se saare subdomains mil jaayenge?**  
**A:** Nahi, sirf woh jo Google ne index kiye hain. Kuch hidden subdomains (jo robots.txt mein disallow hain ya recently banaye gaye) miss ho sakte hain. Complete enumeration ke liye DNS tools (subfinder, amass) bhi use karo.

**Q2: Kya main multiple TLDs ek saath search kar sakta hoon?**  
**A:** Haan! `site:example.com | site:example.org | site:example.net` - OR operator se multiple domains combine karo.

**Q3: `site:gov` vs `site:.gov` mein kya difference hai?**  
**A:** Dono same hain. Dot optional hai. `site:gov` aur `site:.gov` dono saari .gov sites dikhayenge.

### 14. **Practice ke liye Task**

**Task:** Yeh dorks chalao aur results compare karo:

**Dork 1:**
```
site:*.microsoft.com inurl:login
```

**Dork 2:**
```
site:microsoft.com inurl:login -www
```

**Kya Karna Hai:**
1. Dono dorks separately Google mein search karo
2. Pehle 10 results note karo
3. Dekho ki Dork 1 mein kaunse subdomains aaye (dev, staging, etc.)
4. Dork 2 mein www exclude hone se kya difference aaya

**Expected Learning:** Aapko samajh aayega ki wildcard aur exclusion se kaise targeted subdomain discovery hoti hai.

### 15. **Aakhri Choti Summary (5 lines)**

- 🎯 `site:` operator specific domain/subdomain par laser-focused search karta hai
- 🔍 Pentesting ka foundation - target ko precisely define karne ke liye
- 🌐 Wildcard (`site:*.domain.com`) se hidden subdomains discover karo
- ⚡ Multiple domains OR se combine karo: `site:a.com | site:b.com`
- 🚀 Har pentest/bug bounty mein sabse pehle yeh operator use hota hai

> **📌 Ye Zaroor Yaad Rakhein:**  
> "`site:` operator pentesting ka 'scope definer' hai - yeh batata hai ki aapko kahaan dhoondhna hai. Bina iske aap ocean mein swimming kar rahe ho, iske saath aap pool mein focused practice kar rahe ho!" 🏊

---


## **Topic 2: `inurl:` & `allinurl:` (Finding Patterns in URLs)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**inurl/allinurl Operators** - URL structure mein specific keywords dhoondhkar hidden endpoints discover karo.

### 2. **Ye Kya Hai? (What is it?)**

**`inurl:`** - URL mein specified keyword hona chahiye (ek keyword).

**`allinurl:`** - URL mein saare specified keywords hone chahiye (multiple keywords).

**Analogy:** Socho URL ek address hai. `inurl:admin` matlab "Jis address mein 'admin' word ho, woh ghar dikhao." `allinurl:admin login` matlab "Address mein 'admin' AUR 'login' dono words ho." 🏠

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Admin Panel Discovery:** Hidden admin/login pages dhoondhne ka fastest method.
- **Endpoint Enumeration:** API endpoints, debug pages, test environments identify karo.
- **Directory Traversal:** Sensitive directories (backup, config, temp) dhoondho.
- **Pattern-Based Hunting:** Common vulnerable URL patterns (phpMyAdmin, cPanel, etc.) target karo.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Admin Hunting:** `inurl:admin`, `inurl:login`, `inurl:dashboard`
- **API Discovery:** `inurl:api`, `inurl:/v1/`, `inurl:graphql`
- **Backup Files:** `inurl:backup`, `inurl:old`, `inurl:temp`
- **Development Environments:** `inurl:dev`, `inurl:staging`, `inurl:test`

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Hidden Panels Miss:** Admin panels jo main page se linked nahi hain, woh chhoot jaayenge.
- **Incomplete Attack Surface:** URLs mein chhupe endpoints (APIs, debug pages) discover nahi honge.
- **Manual Guessing:** URL guessing mein hours waste honge jo `inurl:` seconds mein kar deta hai.

### 6. **Syntax aur Common Options**

```
inurl:keyword                      # Single keyword in URL
inurl:admin site:target.com        # Combine with site:
allinurl:admin login               # Multiple keywords (all must be in URL)
inurl:admin | inurl:login          # Either keyword
inurl:admin -inurl:wordpress       # Exclude specific pattern
```

**Important Rules:**
- `inurl:` ek keyword ke liye, `allinurl:` multiple ke liye
- `allinurl:` ke baad saare words URL mein hone chahiye (order matter nahi karta)
- Operator ke baad NO SPACE

### 7. **Example 1 (Basic)**

**Dork:**
```
inurl:admin
```

**Kya Hoga:**
- Google saare pages dhoondhega jinke URL mein "admin" word hai
- Examples: `example.com/admin`, `site.com/admin-panel`, `test.com/administrator`

**Output:** Lakhs admin pages - lekin bahut noise bhi (WordPress tutorials, etc.).

**Better Version:**
```
inurl:admin site:target.com
```
**Output:** Sirf target site ke admin pages - focused results! 🎯

### 8. **Example 2 (Pentester-Focused)**

**Dork:**
```
site:*.target.com (inurl:admin | inurl:login | inurl:dashboard) -inurl:wordpress -inurl:wp-admin
```

**Analysis:**
- `site:*.target.com` - Target ke saare subdomains
- `(inurl:admin | inurl:login | inurl:dashboard)` - Teen common admin URL patterns
- `-inurl:wordpress -inurl:wp-admin` - WordPress sites exclude (bahut common hain, usually well-secured)

**Output:** Target ke custom-built admin panels jo less secure ho sakte hain! 🔥

**API Discovery Example:**
```
site:api.target.com inurl:/v1/ (inurl:users | inurl:admin | inurl:internal)
```
**Output:** API endpoints jo internal/admin functions expose kar rahe hain.

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **allinurl Overuse:** `allinurl:admin panel login dashboard` - itne keywords se koi result nahi milega. 2-3 keywords tak limit rakho.
- **Slash Bhoolna:** `inurl:admin` vs `inurl:/admin/` - dono different hain. Slash se exact directory match hota hai.
- **Content vs URL Confusion:** `inurl:password` (URL mein) vs `"password"` (page content mein) - dono alag hain!

### 10. **Best Practices / Pro Tips**

- **Common Patterns List:** Yeh patterns save karke rakho:
  - `inurl:admin`, `inurl:login`, `inurl:dashboard`
  - `inurl:config`, `inurl:backup`, `inurl:test`
  - `inurl:api`, `inurl:graphql`, `inurl:swagger`
- **Combine with Filetype:** `inurl:admin filetype:php` - PHP admin pages (often vulnerable).
- **Use Wildcards:** `inurl:admin*` - admin, administrator, admin-panel sab cover ho jaayega.

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

Ek pentester "FinTech Startup" ka security assessment kar raha tha. Company ne bola ki unke paas sirf main website hai. Pentester ne `site:*.fintechstartup.com inurl:api` dork chalaya aur `internal-api.fintechstartup.com` subdomain mila jo company ko yaad hi nahi tha! Yeh API documentation expose kar raha tha (`inurl:swagger`) jismein saare endpoints aur parameters the. Pentester ne yeh API test kiya aur pata chala ki authentication bypass vulnerability hai. Company shocked thi - unhe pata hi nahi tha ki yeh API public hai. Pentester ne detailed report di, company ne API secure kiya, aur pentester ko bonus mila. `inurl:` ne forgotten asset discover kar diya! 🚨

### 12. **Checklist / Chota Recap (TL;DR)**

✅ `inurl:` = URL mein specific keyword dhoondhta hai  
✅ `allinurl:` = Multiple keywords (saare URL mein hone chahiye)  
✅ Admin panels, APIs, backup directories discover karne ke liye best  
✅ `site:` ke saath combine karke targeted search  
✅ Common patterns (admin, login, api, config) yaad rakho  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `inurl:admin` aur `allinurl:admin login` mein kya difference hai?**  
**A:** `inurl:admin` sirf "admin" URL mein dhoondhta hai, page content mein "login" ho sakta hai. `allinurl:admin login` dono words URL mein hone chahiye: `example.com/admin-login` ya `site.com/login/admin`.

**Q2: Kya `inurl:` case-sensitive hai?**  
**A:** Nahi, Google case-insensitive hai. `inurl:Admin` aur `inurl:admin` same results denge.

**Q3: `inurl:/admin/` (slashes ke saath) kyun use karein?**  
**A:** Slashes se exact directory match hota hai. `inurl:admin` se `administrator.php` bhi aa sakta hai, lekin `inurl:/admin/` sirf `/admin/` directory dikhayega.

### 14. **Practice ke liye Task**

**Task:** Yeh teen dorks chalao aur results ka difference samjho:

**Dork 1:**
```
inurl:login
```

**Dork 2:**
```
allinurl:admin login
```

**Dork 3:**
```
site:gov inurl:admin -inurl:wordpress
```

**Kya Karna Hai:**
1. Teeno dorks separately search karo
2. Pehle 5 results ke URLs carefully dekho
3. Note karo:
   - Dork 1: Kitne broad results hain
   - Dork 2: URL mein dono words kaise present hain
   - Dork 3: Government sites ke custom admin panels

**Expected Learning:** URL-based filtering ki power samajh aayegi.

### 15. **Aakhri Choti Summary (5 lines)**

- 🔗 `inurl:` URL structure mein keywords dhoondhta hai - hidden endpoints discover karne ke liye
- 🎯 `allinurl:` multiple keywords (saare URL mein chahiye) - zyada specific search
- 🚪 Admin panels, APIs, backup directories dhoondhne ka fastest method
- ⚡ `site:` ke saath combine karke target-specific endpoint enumeration
- 💡 Common patterns yaad rakho: admin, login, api, config, backup, test

> **📌 Ye Zaroor Yaad Rakhein:**  
> "`inurl:` operator URL ka 'X-ray vision' hai - yeh dikhata hai ki website ke andar kaunse hidden doors (endpoints) hain. Har pentester ka favorite tool!" 🚪

---

## **Topic 3: `intitle:` & `allintitle:` (Finding Specific Page Titles)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**intitle/allintitle Operators** - Page titles mein specific keywords dhoondhkar vulnerable pages identify karo.

### 2. **Ye Kya Hai? (What is it?)**

**`intitle:`** - Page ke title tag (`<title>`) mein specified keyword hona chahiye.

**`allintitle:`** - Title mein saare specified keywords hone chahiye.

**Analogy:** Socho title ek book ka cover hai. `intitle:hacking` matlab "Jis book ke cover par 'hacking' likha ho." `allintitle:hacking guide` matlab "Cover par 'hacking' AUR 'guide' dono likhe ho." 📚

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Error Page Discovery:** Error messages jo title mein hain (SQL errors, PHP warnings).
- **Default Pages:** Default installation pages (phpMyAdmin, cPanel) jo title se identify hote hain.
- **Login Pages:** Login pages usually title mein "login" word rakhte hain.
- **Exposed Dashboards:** Monitoring tools, admin dashboards jinke titles descriptive hain.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Error Hunting:** `intitle:"error" | intitle:"warning"` - vulnerable sites jo errors expose kar rahe hain.
- **Default Installations:** `intitle:"phpMyAdmin" | intitle:"cPanel"` - default credentials try karne ke liye.
- **Login Pages:** `intitle:"admin login" | intitle:"dashboard login"`
- **Monitoring Tools:** `intitle:"Grafana" | intitle:"Kibana"` - exposed monitoring dashboards.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Error Pages Miss:** Valuable error messages jo vulnerabilities reveal karte hain, woh chhoot jaayenge.
- **Default Installs Undetected:** Default installations (jo easy targets hain) discover nahi honge.
- **Incomplete Recon:** Page titles mein bahut information hoti hai jo content mein nahi hoti.

### 6. **Syntax aur Common Options**

```
intitle:keyword                    # Single keyword in title
intitle:"exact phrase"             # Exact phrase in title
allintitle:keyword1 keyword2       # Multiple keywords (all in title)
intitle:admin site:target.com      # Combine with site:
intitle:login -intitle:wordpress   # Exclude pattern
```

**Important Rules:**
- Title = HTML `<title>` tag ka content
- `intitle:` ek keyword, `allintitle:` multiple keywords
- Quotes use karke exact phrases dhoondh sakte ho

### 7. **Example 1 (Basic)**

**Dork:**
```
intitle:"index of"
```

**Kya Hoga:**
- Pages jinke title mein "index of" hai
- Yeh usually directory listings hoti hain (Apache/Nginx)

**Output:** Exposed directories jismein files publicly accessible hain.

**Better Version:**
```
intitle:"index of" "parent directory" site:edu
```
**Output:** Educational institutions ki exposed directories - often sensitive research data! 🎓

### 8. **Example 2 (Pentester-Focused)**

**Dork:**
```
intitle:"Dashboard [Jenkins]" -site:github.com
```

**Analysis:**
- Jenkins CI/CD tool ka default dashboard title
- GitHub exclude kiya (wahan tutorials/docs hain)

**Output:** Exposed Jenkins dashboards jo authentication nahi maang rahe - direct code deployment access! 🔥

**Error Page Example:**
```
site:target.com (intitle:"error" | intitle:"warning" | intitle:"exception") (sql | mysql | database)
```
**Output:** Target site ke pages jo database errors expose kar rahe hain - SQL injection ka indicator!

**Monitoring Tool Example:**
```
intitle:"Grafana" -login -signin
```
**Output:** Grafana dashboards jo bina login ke accessible hain - company metrics exposed!

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Title vs Content Confusion:** `intitle:password` (title mein) vs `password` (content mein) - bahut alag results!
- **allintitle Overuse:** `allintitle:admin panel login dashboard control` - itne words title mein nahi honge.
- **Quotes Bhoolna:** `intitle:index of` vs `intitle:"index of"` - quotes se exact phrase match hota hai.

### 10. **Best Practices / Pro Tips**

- **Common Vulnerable Titles:**
  - `intitle:"phpMyAdmin"` - Database management
  - `intitle:"Index of /"` - Directory listings
  - `intitle:"Dashboard [Jenkins]"` - CI/CD tool
  - `intitle:"Grafana"` - Monitoring
  - `intitle:"Login - Jira"` - Project management
- **Error Hunting Combo:** `intitle:error (sql | mysql | database | exception)`
- **Combine with inurl:** `intitle:admin inurl:login` - double confirmation!

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

Ek security researcher GHDB (Google Hacking Database) explore kar raha tha aur usne yeh dork dekha: `intitle:"Dashboard [Jenkins]"`. Usne yeh dork chalaya aur 500+ exposed Jenkins instances mile. Usne randomly 10 check kiye - 7 mein authentication nahi tha! Jenkins se aap directly servers par code deploy kar sakte ho. Researcher ne ek Fortune 500 company ka Jenkins dashboard dekha jo publicly accessible tha. Usne responsible disclosure ki - company ne turant authentication enable kiya aur researcher ko Hall of Fame mein add kiya. Ek simple `intitle:` dork ne critical vulnerability expose kar di! 🏆

### 12. **Checklist / Chota Recap (TL;DR)**

✅ `intitle:` = Page title mein keyword dhoondhta hai  
✅ `allintitle:` = Multiple keywords (saare title mein)  
✅ Error pages, default installations, login pages discover karne ke liye  
✅ Title = HTML `<title>` tag (browser tab mein jo dikhta hai)  
✅ Common patterns yaad rakho: "index of", "phpMyAdmin", "Dashboard"  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Title aur heading (H1, H2) mein kya difference hai?**  
**A:** Title = Browser tab mein jo dikhta hai (`<title>` tag). Heading = Page content mein bade text (`<h1>`, `<h2>`). `intitle:` sirf title tag search karta hai, headings nahi.

**Q2: Kya `intitle:` partial matches deta hai?**  
**A:** Haan! `intitle:admin` se "Administrator Panel", "Admin Dashboard" sab aayenge. Exact match ke liye quotes use karo: `intitle:"admin"`.

**Q3: `intitle:` aur `inurl:` dono ek saath use karein?**  
**A:** Bilkul! `intitle:admin inurl:login site:target.com` - triple confirmation ki yeh admin login page hai. Bahut powerful combination!

### 14. **Practice ke liye Task**

**Task:** Yeh dorks chalao aur analyze karo:

**Dork 1:**
```
intitle:"index of" "backup"
```

**Dork 2:**
```
allintitle:admin login panel
```

**Dork 3:**
```
intitle:phpMyAdmin "Welcome to phpMyAdmin"
```

**Kya Karna Hai:**
1. Teeno dorks search karo
2. Pehle 5 results ke titles carefully padho
3. Note karo:
   - Dork 1: Kaunsi files exposed hain
   - Dork 2: Title mein teeno words kaise present hain
   - Dork 3: Kitne default phpMyAdmin installs hain
4. Samjho ki title-based search kyun powerful hai

**Expected Learning:** Page titles mein kitni valuable information hoti hai.

### 15. **Aakhri Choti Summary (5 lines)**

- 📄 `intitle:` page title (`<title>` tag) mein keywords dhoondhta hai
- 🎯 `allintitle:` multiple keywords (saare title mein chahiye)
- 🚨 Error pages, default installations, exposed dashboards discover karne ke liye best
- ⚡ `inurl:` aur `site:` ke saath combine karke laser-focused results
- 💡 Common patterns: "index of", "phpMyAdmin", "Dashboard", "error", "warning"

> **📌 Ye Zaroor Yaad Rakhein:**  
> "`intitle:` operator page ka 'business card' padhta hai - title mein hi pata chal jaata hai ki page kya hai. Error pages aur default installations dhoondhne ka shortcut!" 📇

---


## **Topic 4: `intext:` & `allintext:` (Searching Page Content)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**intext/allintext Operators** - Page ke body content mein specific keywords dhoondhkar sensitive information discover karo.

### 2. **Ye Kya Hai? (What is it?)**

**`intext:`** - Page ke visible text content mein specified keyword hona chahiye.

**`allintext:`** - Page content mein saare specified keywords hone chahiye.

**Analogy:** Socho page ek newspaper article hai. `intext:password` matlab "Article ke andar kaheen 'password' word ho." `allintext:username password database` matlab "Article mein teeno words ho (kaheen bhi)." 📰

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Credential Hunting:** Pages jismein passwords, API keys, tokens mention hain.
- **Configuration Exposure:** Config details jo page content mein accidentally paste ho gaye.
- **Error Messages:** Detailed error messages jo page body mein hain (title mein nahi).
- **Documentation Leaks:** Internal documentation jo publicly accessible ho gaya.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Password Leaks:** `intext:"password is" | intext:"your password"`
- **API Keys:** `intext:"api_key" | intext:"api key"`
- **Database Credentials:** `intext:"DB_PASSWORD" | intext:"database password"`
- **Email Addresses:** `intext:"@company.com"` - employee emails harvest karne ke liye.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Content-Based Leaks Miss:** Page content mein chhupe credentials/keys discover nahi honge.
- **Incomplete OSINT:** Valuable information jo sirf text mein hai (URL/title mein nahi), woh chhoot jaayegi.
- **Documentation Gaps:** Exposed internal docs jo sensitive info contain karte hain, undetected rahenge.

### 6. **Syntax aur Common Options**

```
intext:keyword                     # Single keyword in content
intext:"exact phrase"              # Exact phrase in content
allintext:keyword1 keyword2        # Multiple keywords (all in content)
intext:password site:target.com    # Combine with site:
intext:password -tutorial          # Exclude unwanted content
```

**Important Rules:**
- Content = Page ka visible text (HTML body)
- `intext:` ek keyword, `allintext:` multiple keywords
- Meta tags, hidden text, comments include nahi hote

### 7. **Example 1 (Basic)**

**Dork:**
```
intext:"password"
```

**Kya Hoga:**
- Lakhs pages jismein "password" word hai
- Tutorials, forums, actual leaks - sab mixed

**Output:** Bahut noise, filtering zaroori hai.

**Better Version:**
```
intext:"password is" -tutorial -forum site:pastebin.com
```
**Output:** Pastebin par leaked passwords (tutorials/forums exclude) - real leaks! 🔥

### 8. **Example 2 (Pentester-Focused)**

**Dork:**
```
site:target.com intext:"DB_PASSWORD" (intext:"mysql" | intext:"postgres") filetype:txt
```

**Analysis:**
- `site:target.com` - Target domain
- `intext:"DB_PASSWORD"` - Database password variable
- `(intext:"mysql" | intext:"postgres")` - Database type mention
- `filetype:txt` - Text files (often config dumps)

**Output:** Target ke exposed config files jismein database credentials hain! 💣

**API Key Example:**
```
intext:"api_key" (intext:"sk_live" | intext:"pk_live") site:github.com
```
**Output:** GitHub par leaked Stripe API keys (sk_live = secret key, pk_live = public key).

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Too Broad Search:** `intext:password` alone - lakhs irrelevant results. Hamesha `site:` ya filetype add karo.
- **allintext Overuse:** `allintext:username password email database server config` - itne words ek page mein rare hain.
- **Quotes Bhoolna:** `intext:api key` vs `intext:"api key"` - quotes se exact phrase match.

### 10. **Best Practices / Pro Tips**

- **Common Leak Patterns:**
  - `intext:"BEGIN RSA PRIVATE KEY"` - SSH private keys
  - `intext:"api_key" | intext:"apikey"`
  - `intext:"password" (intext:"mysql" | intext:"root")`
  - `intext:"AWS_SECRET_ACCESS_KEY"`
- **Combine with Filetype:** `intext:"password" filetype:log` - log files mein credentials.
- **Use Exclusions:** `-tutorial -forum -stackoverflow` - noise kam karo.

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

Ek bug bounty hunter "CloudTech" company ke program mein tha. Usne `site:cloudtech.com intext:"api_key" filetype:txt` dork chalaya. Results mein ek text file mili jo ek developer ne testing ke liye upload ki thi aur bhool gaya tha. File mein production API keys the jo AWS S3 buckets access karte the. Hunter ne keys verify kiye (read-only access try kiya, kuch modify nahi kiya - ethical!), aur turant report kiya. Company ne keys revoke kiye, file delete ki, aur hunter ko $5000 bounty di. Ek simple `intext:` dork ne major data breach rok diya! 🛡️

### 12. **Checklist / Chota Recap (TL;DR)**

✅ `intext:` = Page content (body text) mein keyword dhoondhta hai  
✅ `allintext:` = Multiple keywords (saare content mein)  
✅ Credentials, API keys, config details discover karne ke liye  
✅ Hamesha `site:` ya `filetype:` ke saath combine karo (noise kam karne ke liye)  
✅ Common patterns yaad rakho: "password", "api_key", "DB_PASSWORD"  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `intext:` aur normal search mein kya difference hai?**  
**A:** Normal search title, URL, content sab mein dhoondhta hai. `intext:` sirf page content (body) mein dhoondhta hai - zyada focused results.

**Q2: Kya `intext:` hidden text (CSS se hidden) bhi dhoondhta hai?**  
**A:** Nahi, sirf visible text. Hidden text, comments, meta tags include nahi hote.

**Q3: `intext:` vs `inurl:` vs `intitle:` - kab kaunsa use karein?**  
**A:** 
- `inurl:` - URL structure important hai (admin, api, login)
- `intitle:` - Page type identify karna hai (error, dashboard)
- `intext:` - Actual content mein kuch specific dhoondhna hai (password, keys)

### 14. **Practice ke liye Task**

**Task:** Yeh dorks chalao aur compare karo:

**Dork 1:**
```
password
```

**Dork 2:**
```
intext:"password" site:pastebin.com
```

**Dork 3:**
```
allintext:username password email
```

**Kya Karna Hai:**
1. Teeno dorks search karo
2. Results count aur quality note karo
3. Dekho ki:
   - Dork 1: Kitna noise hai (tutorials, products, etc.)
   - Dork 2: Pastebin par actual leaks
   - Dork 3: Pages jismein teeno fields mention hain
4. Samjho ki targeted search kyun zaroori hai

**Expected Learning:** Content-based search ki precision aur filtering ki importance.

### 15. **Aakhri Choti Summary (5 lines)**

- 📝 `intext:` page ke body content mein keywords dhoondhta hai
- 🎯 `allintext:` multiple keywords (saare content mein chahiye)
- 🔑 Credentials, API keys, config leaks discover karne ke liye critical
- ⚡ Hamesha `site:` ya `filetype:` ke saath use karo - noise control
- 💡 Common patterns: "password", "api_key", "BEGIN RSA PRIVATE KEY", "DB_PASSWORD"

> **📌 Ye Zaroor Yaad Rakhein:**  
> "`intext:` operator page ke 'diary' ko padhta hai - andar kya likha hai woh dekhta hai. Leaked credentials aur sensitive info dhoondhne ka direct method!" 📖

---

## **Topic 5: `filetype:` (Hunting for Sensitive Files)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**filetype: Operator** - Specific file formats (PDF, DOC, SQL, ENV) dhoondhkar sensitive documents discover karo.

### 2. **Ye Kya Hai? (What is it?)**

**`filetype:`** - Google ko kehta hai ki "Sirf is file extension waali files dikhao."

**Analogy:** Socho ek filing cabinet hai jismein different folders hain - PDF folder, Excel folder, Text folder. `filetype:pdf` matlab "Sirf PDF folder kholo, baaki ignore karo." 📁

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Document Leaks:** Confidential PDFs, Word docs jo accidentally public hue.
- **Database Dumps:** SQL, CSV files jismein sensitive data hai.
- **Config Files:** .env, .config, .ini files jismein credentials hain.
- **Log Files:** .log files jismein errors, IPs, user activities recorded hain.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Confidential Docs:** `filetype:pdf "confidential" | "internal use only"`
- **Database Backups:** `filetype:sql "INSERT INTO" | "CREATE TABLE"`
- **Environment Files:** `filetype:env "DB_PASSWORD" | "API_KEY"`
- **Spreadsheets:** `filetype:xlsx "password" | "credentials"`

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **File-Based Leaks Miss:** Sensitive documents jo HTML pages nahi hain, woh discover nahi honge.
- **Backup Files Undetected:** SQL dumps, database backups jo critical data contain karte hain.
- **Config Exposure:** .env, .config files jismein production credentials hain, chhoot jaayenge.

### 6. **Syntax aur Common Options**

```
filetype:pdf                       # All PDF files
filetype:sql site:target.com       # SQL files on target
filetype:env "password"            # .env files with password
filetype:xls | filetype:xlsx       # Excel files (old or new format)
filetype:log -site:github.com      # Log files (exclude GitHub)
```

**Important File Extensions (Pentester Focus):**
- **Documents:** pdf, doc, docx, xls, xlsx, ppt, pptx
- **Databases:** sql, db, sqlite, mdb
- **Configs:** env, config, ini, cfg, conf, yaml, yml
- **Code:** php, asp, aspx, jsp
- **Logs:** log, txt
- **Backups:** bak, old, backup, zip

### 7. **Example 1 (Basic)**

**Dork:**
```
filetype:pdf
```

**Kya Hoga:**
- Google ke index mein saari PDF files

**Output:** Billions of PDFs - completely useless without filtering!

**Better Version:**
```
site:gov filetype:pdf "confidential" 2023
```
**Output:** Government ki 2023 ki confidential PDFs - targeted aur valuable! 🎯

### 8. **Example 2 (Pentester-Focused)**

**Dork:**
```
site:target.com filetype:env (intext:"DB_PASSWORD" | intext:"API_KEY" | intext:"SECRET")
```

**Analysis:**
- `site:target.com` - Target domain
- `filetype:env` - Environment config files (.env)
- `(intext:"DB_PASSWORD" | intext:"API_KEY" | intext:"SECRET")` - Common credential variables

**Output:** Target ke exposed .env files jismein production credentials hain - game over! 💣

**SQL Dump Example:**
```
filetype:sql intext:"INSERT INTO" intext:"users" (intext:"password" | intext:"email")
```
**Output:** Database dumps jismein user tables hain - passwords (hopefully hashed) aur emails.

**Log File Example:**
```
site:target.com filetype:log (intext:"error" | intext:"exception") intext:"password"
```
**Output:** Error logs jismein accidentally passwords log ho gaye hain.

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Extension vs Filetype:** `filetype:.pdf` (galat) vs `filetype:pdf` (sahi) - dot nahi lagana.
- **No Filtering:** `filetype:pdf` alone - billions of results, kuch kaam ka nahi.
- **Wrong Extensions:** `filetype:environment` (galat) vs `filetype:env` (sahi) - actual extension use karo.

### 10. **Best Practices / Pro Tips**

- **High-Value File Types (Priority Order):**
  1. `filetype:env` - Environment configs (highest priority!)
  2. `filetype:sql` - Database dumps
  3. `filetype:log` - Log files
  4. `filetype:bak` - Backup files
  5. `filetype:config` - Config files
- **Combine Multiple Types:** `(filetype:env | filetype:config | filetype:ini) "password"`
- **Add Context Keywords:** `filetype:pdf "confidential" "salary"` - specific sensitive docs.
- **Time Filter:** Google Tools se "Past year" select karo - recent leaks zyada relevant hain.

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

Ek security researcher GHDB explore kar raha tha aur usne yeh dork dekha: `filetype:env DB_PASSWORD`. Usne yeh dork chalaya aur hundreds of exposed .env files mile. Usne randomly ek startup ki .env file dekhi jo publicly accessible thi - ismein AWS credentials, database passwords, API keys sab the! Researcher ne company ko email kiya (responsible disclosure). Company shocked thi - unhe pata hi nahi tha ki yeh file public hai. Unhone turant file remove ki, saare credentials rotate kiye, aur researcher ko thank you email ke saath $500 gift card bheja. Ek `filetype:env` dork ne major breach rok diya! 🏆

**Real GHDB Dork:**
```
filetype:env "DB_PASSWORD" "AWS_ACCESS_KEY_ID"
```
Yeh dork aaj bhi kaam karta hai - try karo (ethical use only)!

### 12. **Checklist / Chota Recap (TL;DR)**

✅ `filetype:` = Specific file extensions dhoondhta hai  
✅ High-value targets: env, sql, log, bak, config  
✅ Hamesha `site:` aur context keywords ke saath use karo  
✅ Extension mein dot (.) nahi lagana  
✅ Multiple filetypes OR se combine kar sakte ho  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kya `filetype:` aur `ext:` same hain?**  
**A:** Haan, dono same kaam karte hain. `filetype:pdf` = `ext:pdf`. Google dono accept karta hai.

**Q2: Kya compressed files (.zip, .rar) ke andar search kar sakta hai?**  
**A:** Nahi, Google sirf file names index karta hai, zip ke andar nahi jaata. Lekin `filetype:zip "backup"` se suspicious zip files mil sakti hain.

**Q3: Sabse dangerous filetype kaunsi hai pentesting mein?**  
**A:** `.env` files - inmein plain text credentials hote hain (database, AWS, APIs). Iske baad `.sql` (database dumps) aur `.log` (error logs with sensitive data).

### 14. **Practice ke liye Task**

**Task:** Yeh dorks chalao aur analyze karo (ETHICAL USE ONLY - sirf dekho, download/access mat karo):

**Dork 1:**
```
filetype:env "DB_PASSWORD"
```

**Dork 2:**
```
site:edu filetype:xls "password"
```

**Dork 3:**
```
filetype:log intext:"error" intext:"sql"
```

**Kya Karna Hai:**
1. Teeno dorks search karo (VPN use karo for privacy)
2. Pehle 5 results dekho (OPEN MAT KARO - sirf titles/snippets dekho)
3. Note karo:
   - Dork 1: Kitni .env files exposed hain
   - Dork 2: Educational institutions ki spreadsheets
   - Dork 3: SQL error logs
4. Samjho ki yeh exposure kyun dangerous hai

**Expected Learning:** File-based leaks kitne common hain aur kitne dangerous.

### 15. **Aakhri Choti Summary (5 lines)**

- 📄 `filetype:` specific file extensions dhoondhta hai - documents, configs, databases
- 🔥 High-priority targets: .env, .sql, .log, .bak, .config files
- 🎯 Hamesha `site:` aur context keywords ke saath combine karo
- ⚡ Multiple filetypes OR se combine: `(filetype:env | filetype:config)`
- 🚨 `.env` files sabse dangerous - plain text credentials contain karte hain

> **📌 Ye Zaroor Yaad Rakhein:**  
> "`filetype:` operator pentesting ka 'treasure map' hai - yeh batata hai ki sensitive files kahaan chhupe hain. .env aur .sql files dhoondhna har pentester ki priority!" 💎

---

# **🎓 Module 2 Complete! Congratulations!**

Aapne **Core Dorking Operators** master kar liye! Ab aap:
- ✅ `site:` se specific domains/subdomains target kar sakte ho
- ✅ `inurl:` se hidden endpoints (admin, api) discover kar sakte ho
- ✅ `intitle:` se error pages aur default installations dhoondh sakte ho
- ✅ `intext:` se page content mein credentials hunt kar sakte ho
- ✅ `filetype:` se sensitive files (.env, .sql, .log) expose kar sakte ho

**Yeh 5 operators pentesting ka core arsenal hain!** 🚀

**Next Step:** Module 3 mein aap **Advanced Google Operators** seekhoge - `cache:`, `related:`, `link:`, `info:` - yeh advanced recon techniques hain!

**Practice Reminder:** Har topic ke practice tasks zaroor complete karo, lekin hamesha ethical boundaries mein raho - "Look, Don't Touch!" 👀

---
=============================================================

# **Google Dork And Search Engine Dorking: Zero-to-Hacker Notes** 🚀

---

# **Module 3: Advanced Google Operators & Recon**

---

## **Topic 1: `cache:` (Viewing Old Site Versions for Removed Info)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**cache: Operator** - Google ke cached (purane) version se deleted/modified content recover karo.

### 2. **Ye Kya Hai? (What is it?)**

**`cache:`** - Google har page ka snapshot (backup) store karta hai. Yeh operator us purane version ko dikhata hai, chahe abhi page change ho gaya ho ya delete ho gaya ho.

**Analogy:** Socho ek website ek whiteboard hai. Owner ne kuch likha, phir mita diya. `cache:` operator ek photo hai jo mitane se pehle li gayi thi - aap woh purani writing dekh sakte ho! 📸

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Deleted Content Recovery:** Company ne sensitive info delete ki, lekin Google cache mein abhi bhi hai.
- **Historical Data:** Purane versions se company ki strategy, changes, mistakes pata chalti hain.
- **Evidence Collection:** Pentesting reports ke liye proof chahiye ki kab kya exposed tha.
- **Bypass Restrictions:** Agar site down hai ya access restricted hai, cache se dekh sakte ho.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Deleted Pages:** Jab aapko pata hai ki koi sensitive page tha jo ab delete ho gaya.
- **Modified Content:** Original content kya thi, yeh dekhne ke liye.
- **Site Down:** Target site temporarily down hai, lekin recon continue karni hai.
- **Comparison:** Current vs old version compare karke changes identify karo.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Lost Evidence:** Deleted sensitive data jo proof ban sakta tha, woh miss ho jaayega.
- **Incomplete Timeline:** Company ne kab kya change kiya, yeh historical data nahi milega.
- **Missed Vulnerabilities:** Purane versions mein jo vulnerabilities the, unka pata nahi chalega.

### 6. **Syntax aur Common Options**

```
cache:example.com                  # Domain ka cached version
cache:example.com/admin            # Specific page ka cache
cache:example.com keyword          # Cache mein keyword highlight hoga
```

**Important Rules:**
- URL ke saath protocol (http/https) nahi lagana
- Space nahi hona chahiye: `cache:example.com` ✅ vs `cache: example.com` ❌
- Google 1-2 weeks purana cache rakhta hai (kabhi-kabhi zyada)

### 7. **Example 1 (Basic)**

**Dork:**
```
cache:example.com
```

**Kya Hoga:**
- Google ka last cached snapshot dikhega
- Page ke top par date dikhega: "This is Google's cache of..."

**Output:** Site ka purana version, jo abhi se different ho sakta hai.

### 8. **Example 2 (Pentester-Focused)**

**Scenario:** Aapne kal `site:target.com filetype:env` dork chalaya tha aur ek exposed .env file mili thi. Aaj company ne file delete kar di. Lekin aapko proof chahiye report ke liye.

**Dork:**
```
cache:target.com/config/.env
```

**Analysis:**
- Google cache mein file ka purana version abhi bhi hai
- Aap screenshot le sakte ho as evidence
- Company ko dikha sakte ho ki file exposed thi

**Output:** Deleted .env file ka cached version - perfect evidence! 📸

**Real Example:**
```
cache:company.com/admin password
```
- Admin page ka cache dikhega
- "password" word highlight hoga
- Agar page ab password-protected hai, cache mein open version mil sakta hai

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Protocol Include Karna:** `cache:https://example.com` - galat! Sirf `cache:example.com` likho.
- **Recent Changes Expect Karna:** Cache 1-2 weeks purana hota hai, kal ki changes nahi dikhegi.
- **Cache Hamesha Available:** Har page cached nahi hota - dynamic pages, login-protected pages ka cache nahi hota.

### 10. **Best Practices / Pro Tips**

- **Screenshot Lo:** Cache temporary hai, jaldi screenshot/save kar lo.
- **Multiple Dates Check:** Wayback Machine (archive.org) se zyada purane versions dekho.
- **Combine with Search:** `cache:site.com keyword` - keyword highlight ho jaayega, dhoondhna easy.
- **Check Robots.txt:** `cache:site.com/robots.txt` - purane disallowed paths dekho.

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

Ek bug bounty hunter "TechCorp" ke program mein tha. Usne `site:techcorp.com inurl:test` dork chalaya aur `test.techcorp.com/api-docs` page mila jismein internal API documentation thi. Hunter ne page bookmark kiya aur next day detailed analysis karne gaya. Lekin page 404 ho gaya - company ne raat ko hi delete kar diya! Hunter ne `cache:test.techcorp.com/api-docs` use kiya aur Google cache mein poora documentation mila. Usne screenshots liye, API endpoints analyze kiye, vulnerabilities dhoondhein, aur detailed report submit ki. Company ne accept kiya (cache screenshots proof the) aur $3000 bounty di. `cache:` operator ne deleted evidence recover kar diya! 💰

### 12. **Checklist / Chota Recap (TL;DR)**

✅ `cache:` = Google ka stored snapshot (1-2 weeks purana)  
✅ Deleted/modified content recover karne ke liye  
✅ Protocol (http/https) nahi lagana  
✅ Evidence collection ke liye screenshots lo  
✅ Wayback Machine se combine karke deeper history  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kitne purana cache milta hai?**  
**A:** Usually 1-2 weeks, kabhi-kabhi 1 month. Zyada purana chahiye toh Wayback Machine (archive.org) use karo - wahan years purana data hai.

**Q2: Kya login-protected pages ka cache milta hai?**  
**A:** Nahi, Google sirf publicly accessible pages cache karta hai. Login ke peeche ki content cache mein nahi hoti.

**Q3: Cache update kab hota hai?**  
**A:** Google apne crawlers se regularly update karta hai - popular sites daily, less popular weekly. Aap force update nahi kar sakte.

### 14. **Practice ke liye Task**

**Task:** Yeh steps follow karo:

**Step 1:** Koi bhi news website ka URL lo (e.g., bbc.com/news/technology)

**Step 2:** Normal search karo aur current page dekho

**Step 3:** Ab `cache:` operator use karo:
```
cache:bbc.com/news/technology
```

**Step 4:** Cache date dekho (top par "This is Google's cache of [date]")

**Kya Karna Hai:**
1. Current page aur cached page compare karo
2. Kya koi difference hai? (headlines, images, content)
3. Cache kitne din purana hai?
4. Samjho ki yeh pentesting mein kyun useful hai

**Expected Learning:** Cache ki power samajh aayegi - deleted content recovery.

### 15. **Aakhri Choti Summary (5 lines)**

- 📸 `cache:` Google ka stored snapshot dikhata hai (1-2 weeks purana)
- 🔄 Deleted/modified content recover karne ke liye critical
- 🚫 Protocol (http/https) nahi lagana, sirf domain/URL
- 📝 Evidence collection ke liye screenshots zaroori
- ⏰ Zyada purana data ke liye Wayback Machine use karo

> **📌 Ye Zaroor Yaad Rakhein:**  
> "`cache:` operator time machine hai - yeh dikhata hai ki website pehle kaisi thi. Companies delete kar deti hain, lekin Google yaad rakhta hai!" ⏰

---

## **Topic 2: `related:` (Finding Similar Sites/Subdomains)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**related: Operator** - Target site ke similar websites/competitors discover karo.

### 2. **Ye Kya Hai? (What is it?)**

**`related:`** - Google ko kehta hai ki "Is site jaisi aur sites dikhao" - similar content, similar purpose, similar industry.

**Analogy:** Socho aapko ek restaurant pasand hai. `related:` operator ek friend hai jo kehta hai "Agar yeh pasand hai toh yeh 5 aur try karo, same type ke hain!" 🍽️

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Competitor Discovery:** Target ke competitors/similar companies dhoondho.
- **Industry Mapping:** Poore industry ke players identify karo.
- **Technology Stack:** Similar sites same technology use karti hain - patterns identify karo.
- **Expanded Scope:** Bug bounty mein agar ek company vulnerable hai, similar companies bhi ho sakti hain.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Competitor Analysis:** Target ke competitors kaun hain, unki sites kya expose kar rahi hain.
- **Industry Research:** Specific industry (fintech, healthcare) ke saare players.
- **Pattern Recognition:** Ek site mein vulnerability mili, similar sites mein bhi check karo.
- **Subdomain Discovery:** Kabhi-kabhi related sites actually subdomains ya sister companies hoti hain.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Narrow Focus:** Sirf ek target par focus, similar vulnerable sites miss ho jaayengi.
- **Incomplete Industry View:** Poore attack surface (industry-wide) ka pata nahi chalega.
- **Missed Patterns:** Similar sites mein common vulnerabilities jo pattern banati hain, woh chhoot jaayengi.

### 6. **Syntax aur Common Options**

```
related:example.com                # Similar sites
related:example.com keyword        # Similar sites with keyword
```

**Important Rules:**
- Sirf domain use karo, specific pages nahi
- Protocol nahi lagana
- Results limited hote hain (5-10 sites usually)

### 7. **Example 1 (Basic)**

**Dork:**
```
related:amazon.com
```

**Kya Hoga:**
- Google similar e-commerce sites dikhayega
- Examples: ebay.com, walmart.com, alibaba.com

**Output:** Amazon jaisi shopping sites.

### 8. **Example 2 (Pentester-Focused)**

**Scenario:** Aapne "StartupX.com" (ek fintech company) mein vulnerability dhoondhni hai. Pehle aap industry samajhna chahte ho.

**Dork:**
```
related:startupx.com
```

**Analysis:**
- Google similar fintech startups dikhayega
- Aap un sabki sites par same dorks try kar sakte ho
- Agar ek mein vulnerability hai, chances hain similar sites mein bhi ho

**Output:** 5-10 similar fintech companies - expanded target list! 🎯

**Real Example:**
```
related:pastebin.com
```
**Output:** Similar paste sites (hastebin, ghostbin, etc.) - yeh sab data leak sources hain, OSINT ke liye gold!

**Subdomain Discovery Trick:**
```
related:main.company.com
```
Kabhi-kabhi Google sister sites ya subdomains suggest karta hai jo DNS enumeration miss kar deta hai.

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Specific Pages Use Karna:** `related:site.com/admin` - kaam nahi karega. Sirf domain: `related:site.com`
- **Too Much Expectation:** Yeh operator limited results deta hai (5-10), comprehensive list nahi.
- **Irrelevant Results:** Kabhi-kabhi Google galat similar sites dikhata hai - manual filtering zaroori.

### 10. **Best Practices / Pro Tips**

- **Industry Mapping:** Ek major player ka `related:` check karo, poora industry map ho jaayega.
- **Combine with Other Dorks:** `related:target.com` se list banao, phir har site par `site:competitor.com filetype:env` chalao.
- **Technology Patterns:** Similar sites similar tech stack use karti hain - ek mein vulnerability mili toh sabko check karo.
- **Alternative: Manual Research:** LinkedIn, Crunchbase se bhi competitors dhoondh sakte ho.

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

Ek security researcher "PaymentGatewayA" mein exposed API documentation dhoondhne ki koshish kar raha tha. Usne `site:paymentgatewaya.com inurl:api-docs` try kiya - kuch nahi mila. Phir usne `related:paymentgatewaya.com` chalaya aur 8 similar payment gateway companies mile. Usne un sabki sites par same dork chalaya: `site:competitor.com inurl:api-docs`. Teen competitors ki sites par exposed API docs mile! Researcher ne pattern samjha - yeh industry mein common mistake thi. Usne sabko report kiya aur multiple bounties jeeti. `related:` operator ne ek target se 8 targets bana diye! 💰

### 12. **Checklist / Chota Recap (TL;DR)**

✅ `related:` = Similar websites/competitors discover karta hai  
✅ Sirf domain use karo, specific pages nahi  
✅ Industry mapping aur competitor analysis ke liye  
✅ Limited results (5-10 sites) milte hain  
✅ Similar sites par same dorks try karo - patterns milenge  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Google "similar" kaise decide karta hai?**  
**A:** Content similarity, industry, user behavior, backlinks - multiple factors. Algorithm exact nahi pata, lekin results usually accurate hote hain.

**Q2: Kya `related:` subdomains dikhata hai?**  
**A:** Usually nahi, lekin kabhi-kabhi sister companies ya closely related domains suggest karta hai jo technically subdomains nahi hain.

**Q3: Results kyun itne kam hain (5-10)?**  
**A:** Google deliberately limited rakhta hai. Comprehensive list ke liye manual research (LinkedIn, industry reports) zaroori hai.

### 14. **Practice ke liye Task**

**Task:** Yeh dorks chalao aur analyze karo:

**Dork 1:**
```
related:github.com
```

**Dork 2:**
```
related:shodan.io
```

**Kya Karna Hai:**
1. Dono dorks search karo
2. Results note karo (5-10 sites milenge)
3. Dekho ki:
   - Dork 1: GitHub jaisi code hosting sites (GitLab, Bitbucket, etc.)
   - Dork 2: Shodan jaisi search engines (Censys, ZoomEye, etc.)
4. Samjho ki yeh sites kyun "related" hain
5. Socho ki pentesting mein yeh list kyun useful hai

**Expected Learning:** Industry players identify karna aur expanded target list banana.

### 15. **Aakhri Choti Summary (5 lines)**

- 🔗 `related:` similar websites/competitors discover karta hai
- 🎯 Industry mapping aur competitor analysis ke liye perfect
- 📊 Limited results (5-10) lekin high-quality suggestions
- ⚡ Similar sites par same vulnerabilities hone ka chance high
- 💡 Ek target se multiple targets banane ka shortcut

> **📌 Ye Zaroor Yaad Rakhein:**  
> "`related:` operator network effect create karta hai - ek target se poora industry map ho jaata hai. Similar sites, similar vulnerabilities!" 🌐

---


## **Topic 3: `link:` (Finding Backlinks to a Target)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**link: Operator** - Kaun sites target ko link kar rahi hain, yeh discover karo (relationship mapping).

### 2. **Ye Kya Hai? (What is it?)**

**`link:`** - Google ko kehta hai ki "Mujhe woh sites dikhao jo is URL ko link kar rahi hain" (backlinks).

**Note:** ⚠️ Google ne officially yeh operator deprecate kar diya hai (2017 ke baad accurate results nahi deta). Lekin concept samajhna zaroori hai kyunki alternative tools (Ahrefs, Moz) yeh kaam karte hain.

**Analogy:** Socho ek person hai. `link:` operator yeh batata hai ki "Kaun-kaun log is person ko jaante hain aur uska reference dete hain." 🔗

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Relationship Mapping:** Target ke partnerships, affiliations, connections discover karo.
- **Subdomain Discovery:** Kabhi-kabhi internal links se hidden subdomains milte hain.
- **Trust Analysis:** Kaun sites target ko trust karti hain (link karti hain).
- **Attack Surface:** Linked sites bhi attack surface ka part ho sakti hain.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Partnership Discovery:** Target ke business partners kaun hain.
- **Subdomain Enumeration:** Internal cross-links se hidden domains.
- **Reputation Research:** Kaun sites target ko mention/link kar rahi hain.
- **Supply Chain Analysis:** Connected organizations identify karo.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Incomplete Network Map:** Target ke connections miss ho jaayenge.
- **Hidden Relationships:** Partner sites jo vulnerable ho sakti hain, undetected rahenge.
- **Limited Attack Surface:** Sirf main target par focus, connected assets miss.

### 6. **Syntax aur Common Options**

```
link:example.com                   # Sites linking to domain
link:example.com/page              # Sites linking to specific page
```

**Important Notes:**
- ⚠️ Google mein yeh operator ab accurate nahi hai
- Alternative tools use karo: Ahrefs, Moz, SEMrush
- Bing mein `link:` abhi bhi kaam karta hai (limited results)

### 7. **Example 1 (Basic)**

**Dork (Bing mein try karo):**
```
link:example.com
```

**Kya Hoga:**
- Sites jo example.com ko link kar rahi hain
- Partners, news articles, directories

**Output:** Backlink list (limited).

### 8. **Example 2 (Pentester-Focused)**

**Scenario:** Aapko "CompanyX" ke partner organizations dhoondhne hain.

**Modern Approach (Google deprecated hai):**

**Step 1:** Ahrefs/Moz jaise tools use karo:
- Ahrefs.com par jao
- "CompanyX.com" enter karo
- "Backlinks" section dekho

**Step 2:** Results analyze karo:
- Kaun sites link kar rahi hain
- Partner sites identify karo
- Un partner sites par bhi recon karo

**Alternative Google Dork:**
```
"CompanyX.com" -site:companyx.com
```
Yeh dork sites dhoondhega jo CompanyX ko mention kar rahi hain (direct link nahi, lekin relationship indicator).

**Output:** Partner sites, news mentions, connected organizations.

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Google Par Bharosa:** `link:` Google mein deprecated hai - results incomplete/inaccurate.
- **Alternative Tools Ignore:** Ahrefs, Moz jaise paid tools ignore karna - yeh backlinks ke liye best hain.
- **Bing Bhoolna:** Bing mein `link:` abhi bhi partially kaam karta hai.

### 10. **Best Practices / Pro Tips**

- **Use Alternative Tools:**
  - **Ahrefs:** Most comprehensive backlink database
  - **Moz Link Explorer:** Good free tier
  - **SEMrush:** Competitor backlink analysis
- **Bing Fallback:** `link:target.com` Bing mein try karo (limited but free).
- **Mention Search:** `"target.com" -site:target.com` - mentions dhoondhne ka alternative.
- **Manual Research:** LinkedIn, Crunchbase se partnerships manually research karo.

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

Ek pentester "HealthTech Startup" ka assessment kar raha tha. Usne Ahrefs mein backlinks check kiye aur dekha ki "MedicalDataProvider.com" startup ko link kar raha hai. Yeh ek third-party data provider tha jo startup ke liye patient data process karta tha. Pentester ne MedicalDataProvider ki site par recon kiya aur exposed API documentation mili. Is API se startup ka data accessible tha! Pentester ne yeh supply chain vulnerability report ki - main target secure tha, lekin third-party weak tha. Company ne turant provider ko secure karaya. Backlink analysis ne hidden attack vector expose kar diya! 🎯

### 12. **Checklist / Chota Recap (TL;DR)**

✅ `link:` = Backlinks discover karta hai (kaun sites target ko link kar rahi hain)  
✅ ⚠️ Google mein deprecated - accurate nahi  
✅ Alternative tools use karo: Ahrefs, Moz, SEMrush  
✅ Bing mein partially kaam karta hai  
✅ Partnership/relationship mapping ke liye useful  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kya `link:` operator ab bilkul kaam nahi karta?**  
**A:** Google mein officially deprecated hai (2017 se). Kabhi-kabhi kuch results dikhata hai lekin incomplete. Bing mein abhi bhi limited results deta hai.

**Q2: Free alternative kya hai Ahrefs ka?**  
**A:** Moz Link Explorer (limited free tier), Ubersuggest (Neil Patel), ya Bing ka `link:` operator.

**Q3: Backlinks pentesting mein kyun important hain?**  
**A:** Backlinks relationships dikhate hain - partners, suppliers, affiliates. Yeh sab attack surface ka part hain (supply chain attacks).

### 14. **Practice ke liye Task**

**Task:** Backlink analysis practice karo:

**Step 1:** Bing par jao aur yeh dork chalao:
```
link:github.com
```

**Step 2:** Google par alternative try karo:
```
"github.com" -site:github.com
```

**Step 3:** (Optional) Moz Link Explorer free trial use karo:
- moz.com/link-explorer par jao
- "github.com" enter karo
- Top backlinks dekho

**Kya Karna Hai:**
1. Teeno methods se results compare karo
2. Dekho ki kaun sites GitHub ko link kar rahi hain
3. Samjho ki yeh information pentesting mein kyun useful hai
4. Note karo ki Google vs Bing vs Moz mein kya difference hai

**Expected Learning:** Backlink analysis ki importance aur modern tools ka use.

### 15. **Aakhri Choti Summary (5 lines)**

- 🔗 `link:` backlinks discover karta hai (relationship mapping)
- ⚠️ Google mein deprecated - Ahrefs/Moz use karo
- 🔍 Bing mein abhi bhi partially kaam karta hai
- 🎯 Partnership/supply chain analysis ke liye critical
- 💡 Alternative: `"target.com" -site:target.com` mentions ke liye

> **📌 Ye Zaroor Yaad Rakhein:**  
> "`link:` operator concept important hai lekin Google mein dead hai. Modern pentesting mein Ahrefs/Moz jaise tools zaroori hain - backlinks = hidden relationships!" 🕸️

---

## **Topic 4: `info:` (Getting Google's Info on a Site)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**info: Operator** - Google ke paas site ke baare mein kya information hai, yeh quick summary dekho.

### 2. **Ye Kya Hai? (What is it?)**

**`info:`** - Google ko kehta hai ki "Is site ke baare mein tumhare paas jo bhi info hai, woh dikhao" - ek quick overview page.

**Analogy:** Socho ek person ka "profile card" hai jismein basic info hai - naam, address, connections. `info:` operator wahi card dikhata hai. 📇

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Quick Overview:** Ek command mein site ki basic info (cache, similar, links).
- **Indexed Status:** Kya site Google mein indexed hai ya nahi.
- **Shortcut to Other Operators:** `info:` page se cache, related, link operators ka shortcut milta hai.
- **Reconnaissance Starting Point:** Recon ka first step - site Google ko kitni visible hai.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Initial Recon:** Naye target ki quick overview chahiye.
- **Indexed Check:** Kya site/page Google mein hai ya nahi.
- **Quick Access:** Cache, related sites ka shortcut chahiye.
- **Visibility Test:** Target ki Google presence check karna.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Slow Start:** Har operator manually type karna padega (cache, related, etc.).
- **Visibility Miss:** Pata nahi chalega ki site Google mein kitni visible hai.
- **No Quick Overview:** Basic info gather karne mein zyada time.

### 6. **Syntax aur Common Options**

```
info:example.com                   # Site info page
info:example.com/page              # Specific page info
```

**Important Rules:**
- Protocol nahi lagana (http/https)
- Space nahi hona chahiye
- Results page par shortcuts milte hain (cache, related, link)

### 7. **Example 1 (Basic)**

**Dork:**
```
info:google.com
```

**Kya Hoga:**
- Google ek info page dikhayega
- Page par links honge: "Cached", "Similar pages", etc.

**Output:** Quick overview aur shortcuts to other operators.

### 8. **Example 2 (Pentester-Focused)**

**Scenario:** Aapko naye target "StartupY.com" ki recon start karni hai.

**Dork:**
```
info:startupy.com
```

**Analysis:**
- Agar results aaye = Site indexed hai (Google ko pata hai)
- Agar "No information available" = Site new hai ya robots.txt se blocked
- Info page par shortcuts:
  - "Cached" click karo → `cache:startupy.com`
  - "Similar" click karo → `related:startupy.com`

**Output:** Quick recon starting point - ek click mein multiple operators access! ⚡

**Subdomain Check:**
```
info:dev.startupy.com
```
Agar results nahi aaye = Subdomain indexed nahi (hidden/new).

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Too Much Expectation:** `info:` sirf basic overview deta hai, detailed info nahi.
- **Direct Use:** `info:` se direct results nahi milte, shortcuts milte hain - unhe click karna padta hai.
- **Protocol Include:** `info:https://site.com` - galat! Sirf `info:site.com`

### 10. **Best Practices / Pro Tips**

- **First Step:** Naye target par pehle `info:` chalao - quick visibility check.
- **Use Shortcuts:** Info page par jo links hain (cache, similar), unhe use karo - typing bachega.
- **Indexed Check:** `info:target.com/admin` - agar results nahi aaye, admin page indexed nahi (good for target, bad for you).
- **Combine with site::** `site:target.com` zyada detailed results deta hai, `info:` sirf quick check ke liye.

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

Ek bug bounty hunter ko 50 subdomains ki list mili (DNS enumeration se). Har subdomain par detailed recon karne se pehle, usne quick check kiya ki kaun indexed hain. Usne ek script banayi jo har subdomain par `info:` operator chalaye. Results:
- 30 subdomains indexed (Google ko pata hain)
- 20 subdomains not indexed (hidden/new)

Hunter ne pehle un 20 hidden subdomains par focus kiya - kyunki jo Google ko nahi pata, woh usually less monitored aur less secure hote hain. Usne un 20 mein se 3 mein critical vulnerabilities dhoondhein aur bounties jeeti. `info:` operator ne priority set karne mein help ki! 🎯

### 12. **Checklist / Chota Recap (TL;DR)**

✅ `info:` = Site ki quick overview/summary  
✅ Indexed status check karne ke liye  
✅ Shortcuts milte hain (cache, related, link)  
✅ Reconnaissance ka starting point  
✅ Protocol nahi lagana, sirf domain  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `info:` aur `site:` mein kya difference hai?**  
**A:** `info:` sirf overview page dikhata hai (shortcuts ke saath). `site:` actual search results dikhata hai (saare indexed pages). Detailed recon ke liye `site:` better hai.

**Q2: Agar `info:` results nahi dikhaye toh?**  
**A:** Matlab site/page indexed nahi hai - ya toh new hai, ya robots.txt se blocked, ya Google ne crawl nahi kiya.

**Q3: Kya `info:` se koi sensitive data mil sakta hai?**  
**A:** Nahi directly, lekin yeh shortcuts deta hai (cache, related) jinse sensitive data mil sakta hai.

### 14. **Practice ke liye Task**

**Task:** `info:` operator test karo:

**Step 1:** Yeh dork chalao:
```
info:github.com
```

**Step 2:** Info page par jo shortcuts hain (Cached, Similar), unhe click karo

**Step 3:** Ab ek hidden subdomain try karo:
```
info:thissubdomaindoesnotexist123.github.com
```

**Kya Karna Hai:**
1. Step 1 mein dekho ki kya shortcuts milte hain
2. Shortcuts click karke dekho ki kahan jaate hain
3. Step 3 mein "No information available" message dekho
4. Samjho ki indexed vs non-indexed mein kya difference hai

**Expected Learning:** `info:` operator ka practical use aur indexed status check.

### 15. **Aakhri Choti Summary (5 lines)**

- 📇 `info:` site ki quick overview/summary dikhata hai
- ✅ Indexed status check karne ka fastest method
- 🔗 Shortcuts milte hain (cache, related, link operators ke liye)
- ⚡ Reconnaissance ka starting point - quick visibility check
- 💡 Non-indexed subdomains usually less monitored (priority targets)

> **📌 Ye Zaroor Yaad Rakhein:**  
> "`info:` operator reconnaissance ka 'dashboard' hai - ek jagah se saari basic info aur shortcuts. Quick check ke liye perfect!" 📊

---

# **🎓 Module 3 Complete! Congratulations!**

Aapne **Advanced Google Operators & Recon** master kar liye! Ab aap:
- ✅ `cache:` se deleted/modified content recover kar sakte ho
- ✅ `related:` se competitors aur similar sites discover kar sakte ho
- ✅ `link:` concept samajhte ho (modern tools: Ahrefs/Moz)
- ✅ `info:` se quick site overview aur indexed status check kar sakte ho

**Yeh operators advanced reconnaissance ke liye critical hain!** 🚀

**Next Step:** Module 4 mein aap **Practical Hacking & Databases** seekhoge:
- Google Hacking Database (GHDB)
- Login pages dorking
- Sensitive files hunting
- Vulnerability reports
- Exposed devices

**Important Note:** Module 3 ke operators (especially `cache:` aur `related:`) ko Module 1 & 2 ke operators ke saath combine karo - bahut powerful dorks ban jaayenge!

**Practice Reminder:** Real targets par practice karte waqt hamesha ethical boundaries yaad rakho - "Look, Don't Touch!" 👀

---
=============================================================

# **Google Dork And Search Engine Dorking: Zero-to-Hacker Notes** 🚀

---

# **Module 4: Practical Hacking & Databases (The Arsenal)**

---

## **Topic 1: Intro to GHDB (What is Exploit-DB's Google Hacking Database?)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**GHDB (Google Hacking Database)** - Ready-made dorks ka official database jo Exploit-DB par hosted hai.

### 2. **Ye Kya Hai? (What is it?)**

**GHDB** ek publicly available database hai jismein 6000+ pre-built Google dorks hain, jo categories mein organized hain. Yeh Exploit-DB (exploit-db.com) par maintained hai aur security researchers worldwide contribute karte hain.

**Analogy:** Socho GHDB ek "recipe book" hai hackers ke liye. Aapko khud se dork banana nahi padta - book mein already tested recipes (dorks) hain jo kaam karti hain! 📚

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Time-Saving:** Khud se dorks banane ki jagah, tested dorks directly use karo.
- **Learning Resource:** Dusre experts ke dorks dekh kar patterns seekho.
- **Comprehensive Coverage:** Har category covered hai - login pages, files, errors, devices, etc.
- **Updated Regularly:** Naye vulnerabilities ke liye naye dorks add hote rehte hain.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Recon Start:** Naye target par kahan se shuru karein, yeh samajhne ke liye.
- **Specific Hunting:** Login pages, config files, ya specific vulnerabilities dhoondhne ke liye.
- **Learning Phase:** Google dorking seekh rahe ho toh GHDB best teacher hai.
- **Quick Wins:** Bug bounty mein fast results chahiye toh GHDB dorks try karo.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Reinventing the Wheel:** Jo dorks already exist karte hain, unhe phir se banane mein time waste.
- **Missed Patterns:** Expert-level dorks jo aapko nahi pata, woh miss ho jaayenge.
- **Slow Recon:** Manual trial-error ki jagah, GHDB se direct effective dorks.

### 6. **Syntax aur Common Options**

**GHDB Access:**
```
Website: https://www.exploit-db.com/google-hacking-database
```

**Categories (Main):**
- **Footholds:** Login pages, admin panels
- **Files Containing Usernames:** Password files, user lists
- **Sensitive Directories:** Backup folders, config directories
- **Web Server Detection:** Server versions, technologies
- **Vulnerable Files:** Known vulnerable scripts
- **Vulnerable Servers:** Specific software versions
- **Error Messages:** SQL errors, PHP warnings
- **Files Containing Juicy Info:** Credentials, API keys
- **Network or Vulnerability Data:** Firewall configs, vulnerability scans

### 7. **Example 1 (Basic)**

**GHDB Par Jao:**
1. exploit-db.com/google-hacking-database
2. Category select karo: "Files Containing Passwords"
3. Ek dork copy karo:

```
filetype:env "DB_PASSWORD"
```

**Kya Hoga:**
- Yeh tested dork hai jo .env files dhoondhta hai
- Thousands of results milenge

**Output:** Exposed environment files with database passwords.

### 8. **Example 2 (Pentester-Focused)**

**Scenario:** Aapko admin panels dhoondhne hain.

**GHDB Steps:**
1. Category: "Footholds"
2. Search: "admin login"
3. Top dork copy karo:

```
intitle:"Admin Login" inurl:admin
```

**Analysis:**
- `intitle:"Admin Login"` - Title mein "Admin Login" hai
- `inurl:admin` - URL mein "admin" hai
- Double confirmation - false positives kam

**Output:** Real admin panels, not tutorials! 🎯

**Another GHDB Gem:**
```
intitle:"index of" "backup.sql"
```
Category: "Sensitive Directories"
Output: Exposed SQL backup files.

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Blindly Copy-Paste:** GHDB dork copy karke directly use karna bina samjhe - kaam nahi karega. `site:target.com` add karo.
- **Outdated Dorks:** Kuch purane dorks ab kaam nahi karte (Google algorithms change hote hain) - test karo pehle.
- **No Customization:** GHDB dork generic hai - apne target ke liye customize karo.

### 10. **Best Practices / Pro Tips**

- **Combine with site::** GHDB dork + `site:target.com` = targeted results.
- **Browse Categories:** Har category explore karo - naye ideas milenge.
- **Submit Your Dorks:** Agar aapne naya effective dork banaya, GHDB mein submit karo (contribution).
- **Check Date:** Dork ka submission date dekho - recent dorks zyada effective hote hain.
- **Use Filters:** GHDB website par search/filter options use karo specific dorks dhoondhne ke liye.

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

Ek beginner pentester apne pehle bug bounty program mein tha. Usne 2 hours khud se dorks banane ki koshish ki - kuch khaas nahi mila. Phir usne GHDB discover kiya. Usne "Files Containing Juicy Info" category mein yeh dork dekha: `filetype:log inurl:"password.log"`. Usne target par yeh dork chalaya: `site:target.com filetype:log inurl:"password.log"`. Ek result mila - ek forgotten log file jismein test credentials the. Usne verify kiya (ethical!), report kiya, aur apni pehli $500 bounty jeeti! GHDB ne 2 hours ka kaam 5 minutes mein kar diya! 💰

### 12. **Checklist / Chota Recap (TL;DR)**

✅ GHDB = 6000+ ready-made dorks ka database (Exploit-DB par)  
✅ Categories mein organized - login, files, errors, servers, etc.  
✅ Time-saving - tested dorks directly use karo  
✅ Hamesha `site:target.com` add karke customize karo  
✅ Learning resource - expert patterns seekho  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kya GHDB free hai?**  
**A:** Haan, 100% free! Exploit-DB open-source hai. Koi registration nahi chahiye, direct browse karo.

**Q2: Kya main apne dorks GHDB mein submit kar sakta hoon?**  
**A:** Haan! Exploit-DB par account banao aur "Submit Google Dork" option use karo. Agar approve hua toh aapka naam bhi dikhega!

**Q3: GHDB dorks kitne purane hain?**  
**A:** Mixed - kuch 2000s ke hain (still work), kuch recent hain. Har dork ke saath submission date hota hai - recent ones prefer karo.

### 14. **Practice ke liye Task**

**Task:** GHDB explore karo aur ek dork test karo:

**Step 1:** exploit-db.com/google-hacking-database par jao

**Step 2:** "Sensitive Directories" category select karo

**Step 3:** Yeh dork dhoondho aur copy karo:
```
intitle:"index of" "parent directory"
```

**Step 4:** Google par test karo (generic):
```
intitle:"index of" "parent directory" site:edu
```

**Kya Karna Hai:**
1. Results dekho (educational sites ki exposed directories)
2. GHDB par 5 aur dorks explore karo (different categories)
3. Note karo ki har category kis type ki information target karti hai
4. Apni favorite 3 dorks save karo future use ke liye

**Expected Learning:** GHDB ki power aur organization samajh aayega.

### 15. **Aakhri Choti Summary (5 lines)**

- 📚 GHDB = 6000+ tested Google dorks ka official database (Exploit-DB)
- 🗂️ Categories mein organized - har type ki hunting covered
- ⚡ Time-saving - khud banane ki jagah ready dorks use karo
- 🎯 Hamesha customize karo (`site:target.com` add karo)
- 🚀 Learning resource - expert patterns aur techniques seekho

> **📌 Ye Zaroor Yaad Rakhein:**  
> "GHDB pentester ka 'cheat sheet' hai - yeh wheel reinvent karne se bachata hai. Har serious pentester GHDB bookmark karta hai!" 🔖

---

## **Topic 2: Dorking for Login Pages (`intitle:login inurl:admin`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Login Page Dorking** - Hidden admin panels aur authentication pages discover karo.

### 2. **Ye Kya Hai? (What is it?)**

Login page dorking ek technique hai jismein aap specific operators use karke websites ke login/admin pages dhoondhte ho jo normally main page se linked nahi hote.

**Analogy:** Socho ek building mein front door hai (main page) aur ek back door hai (admin panel). Normal visitors front door use karte hain, lekin aap back door dhoondh rahe ho! 🚪

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Attack Surface Discovery:** Hidden admin panels jo main site se linked nahi, woh mil jaate hain.
- **Weak Authentication:** Admin panels often weak passwords ya default credentials use karte hain.
- **Direct Access:** Main site bypass karke directly admin area tak pahunch.
- **Forgotten Panels:** Purane, unmaintained admin pages jo vulnerable hote hain.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Initial Recon:** Target ki admin panels dhoondhne ke liye.
- **Credential Testing:** Agar aapke paas leaked credentials hain, unhe test karne ke liye panels chahiye.
- **Brute Force Prep:** (Ethical, with permission) Brute force attack ke liye login endpoints.
- **Default Creds:** Default credentials (admin/admin) test karne ke liye panels.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Hidden Panels Miss:** Main site se linked nahi hone wale admin areas chhoot jaayenge.
- **Easy Wins Lost:** Default credentials waale panels jo quick wins hain, undetected rahenge.
- **Incomplete Attack Surface:** Authentication endpoints ka poora map nahi banega.

### 6. **Syntax aur Common Options**

**Basic Patterns:**
```
intitle:login                      # Title mein "login"
inurl:admin                        # URL mein "admin"
intitle:"admin login"              # Exact phrase
intitle:login inurl:admin          # Dono conditions
```

**Advanced Combinations:**
```
intitle:login inurl:admin site:target.com
(intitle:login | intitle:signin) inurl:admin
intitle:"Admin Panel" -site:github.com
```

### 7. **Example 1 (Basic)**

**Dork:**
```
intitle:login
```

**Kya Hoga:**
- Lakhs pages jinke title mein "login" hai
- Tutorials, forums, actual login pages - sab mixed

**Output:** Too broad, filtering zaroori.

**Better Version:**
```
intitle:login inurl:admin -site:github.com -site:stackoverflow.com
```
**Output:** Actual admin login pages, tutorials excluded! 🎯

### 8. **Example 2 (Pentester-Focused)**

**Dork:**
```
site:target.com (intitle:"admin login" | intitle:"administrator login" | intitle:"admin panel") (inurl:admin | inurl:login | inurl:dashboard)
```

**Analysis:**
- `site:target.com` - Specific target
- Three title variations (admin login, administrator login, admin panel)
- Three URL patterns (admin, login, dashboard)
- Total 9 combinations (3×3) ek dork mein!

**Output:** Target ke saare possible admin panels - comprehensive coverage! 🔥

**WordPress Specific:**
```
site:target.com inurl:wp-admin intitle:login
```
**Output:** WordPress admin panels (often default credentials).

**Custom CMS:**
```
site:target.com (inurl:admin | inurl:administrator) (intitle:login | intitle:signin) -inurl:wordpress
```
**Output:** Custom-built admin panels (usually less secure than WordPress).

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **No Filtering:** `intitle:login` alone - billions of results, useless.
- **Ignoring Variations:** Sirf "login" search karna - "signin", "log in", "authenticate" miss ho jaayenge.
- **Attempting Login:** Panel mil gaya toh login try karna (bina permission) - CRIME! Sirf discover karo, report karo.

### 10. **Best Practices / Pro Tips**

- **Common Login Patterns:**
  - `intitle:login inurl:admin`
  - `intitle:"admin panel" inurl:login`
  - `intitle:dashboard inurl:admin`
  - `intitle:"control panel" inurl:admin`
- **Technology-Specific:**
  - WordPress: `inurl:wp-admin`
  - Joomla: `inurl:administrator`
  - Drupal: `inurl:user/login`
  - phpMyAdmin: `intitle:phpMyAdmin inurl:index.php`
- **Exclude Noise:** Hamesha `-site:github.com -site:youtube.com` add karo.
- **Screenshot Evidence:** Panel mila toh screenshot lo (login mat karo) - report ke liye proof.

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

Ek bug bounty hunter "RetailCorp" ke program mein tha. Main website (retailcorp.com) bilkul secure thi - no exposed panels. Hunter ne yeh dork chalaya: `site:*.retailcorp.com intitle:"admin login" -www`. Results mein `old-admin.retailcorp.com` subdomain mila jo company bhool gayi thi. Yeh purana admin panel tha jo still live tha! Hunter ne panel access kiya (sirf homepage dekha, login nahi kiya), screenshot li, aur report kiya. Company shocked thi - unhe pata hi nahi tha ki yeh subdomain exist karta hai. Unhone turant panel band kiya aur hunter ko $2000 bounty di. Ek simple login dork ne forgotten asset expose kar diya! 💰

### 12. **Checklist / Chota Recap (TL;DR)**

✅ Login dorking = Hidden admin panels discover karna  
✅ `intitle:` aur `inurl:` combine karo for best results  
✅ Variations include karo: login, signin, authenticate, dashboard  
✅ Technology-specific patterns use karo (WordPress, Joomla, etc.)  
✅ Panel mila = Screenshot lo, login MAT karo (ethical!)  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Login panel mil gaya, ab kya karein?**  
**A:** Screenshot lo, URL note karo, aur report karo. Login try mat karo (even with default credentials) - yeh unauthorized access hai.

**Q2: Kya default credentials try karna legal hai?**  
**A:** Nahi, jab tak explicit permission nahi hai. Bug bounty programs mein bhi "no brute force" rule hota hai usually.

**Q3: Sabse common admin URL patterns kya hain?**  
**A:** `/admin`, `/administrator`, `/login`, `/wp-admin`, `/dashboard`, `/cpanel`, `/admin.php`, `/admin/login.php`

### 14. **Practice ke liye Task**

**Task:** Login page hunting practice karo:

**Dork 1:**
```
site:edu intitle:"admin login" inurl:admin
```

**Dork 2:**
```
site:gov (intitle:login | intitle:signin) inurl:admin -inurl:wordpress
```

**Kya Karna Hai:**
1. Dono dorks search karo
2. Pehle 5 results ke URLs analyze karo
3. Note karo:
   - URL patterns (kaunse paths common hain)
   - Title patterns (kaise worded hain)
   - Technology clues (WordPress, custom, etc.)
4. Samjho ki yeh panels kyun security risk hain

**Expected Learning:** Login page patterns aur discovery techniques.

### 15. **Aakhri Choti Summary (5 lines)**

- 🚪 Login dorking hidden admin panels discover karta hai
- 🎯 `intitle:` + `inurl:` combination most effective
- 🔄 Variations include karo: login, signin, dashboard, admin panel
- 🛠️ Technology-specific patterns (WordPress, Joomla) use karo
- 🚨 Panel mila = Report karo, login mat karo (ethical boundary!)

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Login panels dhoondhna legal hai, login karna illegal! Pentester ka kaam 'door dhoondna' hai, 'door kholna' nahi (bina permission ke)!" 🔐

---


## **Topic 3: Dorking for Sensitive Files (`filetype:env "DB_PASSWORD"`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Sensitive File Dorking** - Config files, credentials, aur sensitive documents hunt karo.

### 2. **Ye Kya Hai? (What is it?)**

Sensitive file dorking ek technique hai jismein aap specific file types aur keywords combine karke accidentally exposed sensitive files dhoondhte ho - jaise .env files, database dumps, config files, password lists.

**Analogy:** Socho ek office mein confidential files filing cabinet mein locked honi chahiye, lekin galti se desk par khuli padhi hain. Aap woh dhoondh rahe ho! 📂

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Direct Credentials:** Plain text passwords, API keys, database credentials mil jaate hain.
- **Critical Vulnerabilities:** Ek exposed .env file se poora application compromise ho sakta hai.
- **Quick Wins:** Bug bounty mein yeh high-severity findings hain - instant bounty.
- **Common Mistake:** Developers accidentally sensitive files commit/upload kar dete hain.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Credential Hunting:** Database passwords, API keys dhoondhne ke liye.
- **Config Discovery:** Application configurations jo sensitive info contain karte hain.
- **Backup Files:** SQL dumps, database backups jo exposed hain.
- **Development Leaks:** .env, .git, debug files jo production mein aa gaye.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Critical Leaks Miss:** Plain text credentials jo easily accessible hain, undetected rahenge.
- **Low-Hanging Fruit Lost:** Sabse easy vulnerabilities jo instant impact hain, chhoot jaayengi.
- **Incomplete Recon:** File-based attack surface ka pata nahi chalega.

### 6. **Syntax aur Common Options**

**High-Priority File Types:**
```
filetype:env                       # Environment configs
filetype:sql                       # Database dumps
filetype:log                       # Log files
filetype:bak                       # Backup files
filetype:config                    # Config files
filetype:ini                       # Initialization files
```

**Common Keyword Patterns:**
```
"DB_PASSWORD"                      # Database password
"API_KEY"                          # API keys
"SECRET"                           # Secret keys
"password"                         # Generic password
"BEGIN RSA PRIVATE KEY"            # SSH keys
```

### 7. **Example 1 (Basic)**

**Dork:**
```
filetype:env
```

**Kya Hoga:**
- Lakhs .env files
- Most are from GitHub, tutorials, etc.

**Output:** Too broad, filtering critical.

**Better Version:**
```
filetype:env "DB_PASSWORD" -site:github.com -site:gitlab.com
```
**Output:** Real production .env files (GitHub excluded) - actual leaks! 🔥

### 8. **Example 2 (Pentester-Focused)**

**Dork:**
```
site:target.com (filetype:env | filetype:config | filetype:ini) ("DB_PASSWORD" | "DATABASE_PASSWORD" | "MYSQL_PASSWORD" | "API_KEY" | "SECRET_KEY")
```

**Analysis:**
- `site:target.com` - Specific target
- Three file types (env, config, ini)
- Five credential keywords
- Total 15 combinations (3×5)!

**Output:** Target ke exposed config files with credentials - jackpot! 💣

**SQL Dump Example:**
```
site:target.com filetype:sql (intext:"INSERT INTO" | intext:"CREATE TABLE") (intext:"users" | intext:"admin") intext:"password"
```
**Output:** Database dumps with user tables containing passwords.

**Log File Example:**
```
site:target.com filetype:log (intext:"password" | intext:"pwd") (intext:"error" | intext:"failed")
```
**Output:** Error logs jismein accidentally passwords log ho gaye hain.

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **No Site Filter:** `filetype:env "password"` - billions of GitHub results, useless.
- **Downloading Files:** File mili toh download karna - ILLEGAL! Sirf existence note karo.
- **Single Keyword:** Sirf "password" search karna - "DB_PASSWORD", "DATABASE_PWD" miss ho jaayenge.

### 10. **Best Practices / Pro Tips**

- **Top Priority Dorks:**
  ```
  filetype:env "DB_PASSWORD"
  filetype:env "AWS_SECRET_ACCESS_KEY"
  filetype:sql "INSERT INTO" "password"
  filetype:log "password" "error"
  filetype:bak "database"
  ```
- **Exclude Code Repos:** Hamesha `-site:github.com -site:gitlab.com -site:bitbucket.org`
- **Multiple Keywords:** OR use karke variations cover karo: `("password" | "pwd" | "pass")`
- **Time Filter:** Google Tools se "Past year" - recent leaks zyada relevant.
- **Evidence Collection:** Screenshot lo (file open mat karo) - report ke liye proof.

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

Ek security researcher routine OSINT kar raha tha aur usne yeh dork chalaya: `filetype:env "AWS_SECRET_ACCESS_KEY" -site:github.com`. Results mein ek startup ki .env file mili jo accidentally public S3 bucket mein upload ho gayi thi. File mein AWS credentials, database passwords, Stripe API keys - sab kuch tha! Researcher ne turant startup ko email kiya (responsible disclosure). Startup panicked - unhe pata hi nahi tha ki file public hai. Unhone immediately:
1. File delete ki
2. Saare credentials rotate kiye
3. S3 bucket permissions fix kiye
4. Researcher ko $10,000 bounty + job offer diya!

Ek simple `filetype:env` dork ne major data breach rok diya! 🛡️

### 12. **Checklist / Chota Recap (TL;DR)**

✅ Sensitive files = .env, .sql, .log, .bak, .config  
✅ Keywords = DB_PASSWORD, API_KEY, SECRET, password  
✅ Hamesha `site:target.com` aur exclude GitHub/GitLab  
✅ Multiple variations OR se combine karo  
✅ File mili = Screenshot lo, download MAT karo  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: File mil gayi, kya main open kar sakta hoon verify karne ke liye?**  
**A:** Nahi! File ka existence hi enough evidence hai. Open karna = accessing unauthorized data = crime. Sirf URL aur screenshot report karo.

**Q2: Sabse dangerous file type kaunsi hai?**  
**A:** `.env` files - inmein plain text credentials hote hain (no encryption). Iske baad `.sql` (database dumps) aur `.log` (error logs with passwords).

**Q3: Kya yeh files really production mein hoti hain?**  
**A:** Haan! Developers galti se commit kar dete hain, ya deployment scripts misconfigured hote hain. Daily basis par naye leaks hote hain.

### 14. **Practice ke liye Task**

**Task:** Sensitive file hunting practice (ETHICAL ONLY):

**Dork 1:**
```
site:edu filetype:xls "password"
```

**Dork 2:**
```
site:gov filetype:pdf "confidential" "internal use only"
```

**Dork 3:**
```
filetype:log "error" "database" -site:github.com
```

**Kya Karna Hai:**
1. Teeno dorks search karo
2. Results count note karo (kitni files exposed hain)
3. Pehle 3 results ke titles/snippets dekho (OPEN MAT KARO)
4. Samjho ki:
   - Dork 1: Educational institutions ki password spreadsheets
   - Dork 2: Government confidential documents
   - Dork 3: Error logs with database info
5. Note karo ki yeh exposure kyun critical hai

**Expected Learning:** File-based leaks kitne common aur dangerous hain.

### 15. **Aakhri Choti Summary (5 lines)**

- 📂 Sensitive files = .env, .sql, .log, .bak (credentials contain karte hain)
- 🔑 Keywords = DB_PASSWORD, API_KEY, SECRET, AWS_SECRET_ACCESS_KEY
- 🎯 Hamesha target-specific (`site:`) aur exclude code repos
- 🚨 File existence = Report karo, open/download MAT karo
- 💰 High-severity findings - instant bug bounty impact

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Sensitive file dorking 'treasure hunting' hai - ek .env file se poora application compromise ho sakta hai. Lekin yaad rakho: dhoondho, chhoona mat!" 💎

---

## **Topic 4: Dorking for Vulnerability Reports (`intitle:"Nessus scan report"`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Vulnerability Report Dorking** - Exposed security scan reports aur vulnerability assessments discover karo.

### 2. **Ye Kya Hai? (What is it?)**

Vulnerability report dorking ek technique hai jismein aap accidentally exposed security scan reports dhoondhte ho - jaise Nessus scans, penetration test reports, vulnerability assessments jo publicly accessible ho gaye hain.

**Analogy:** Socho ek doctor ne patient ki medical report likhi (confidential), lekin galti se hospital ke notice board par laga di. Aap woh report dhoondh rahe ho! 🏥

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Ready-Made Vulnerability List:** Report mein already vulnerabilities listed hain - aapko dhoondhne ki zaroorat nahi.
- **Attack Roadmap:** Pentest reports attack vectors aur exploitation steps contain karte hain.
- **Sensitive Info:** Internal IPs, network topology, system details - sab exposed.
- **Irony Alert:** Security reports ko secure nahi rakha gaya - double vulnerability!

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Quick Recon:** Target ke known vulnerabilities instantly discover karne ke liye.
- **Historical Data:** Purane scan reports se pata chalta hai ki kya fix hua, kya nahi.
- **Network Mapping:** Internal network structure samajhne ke liye.
- **Competitive Intelligence:** Competitors ki security posture dekhne ke liye.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Easy Intel Miss:** Ready-made vulnerability lists jo publicly available hain, undetected rahenge.
- **Time Waste:** Khud se vulnerabilities dhoondhne mein time jab already report available hai.
- **Incomplete Picture:** Historical vulnerability data miss ho jaayega.

### 6. **Syntax aur Common Options**

**Common Report Types:**
```
intitle:"Nessus scan report"       # Nessus vulnerability scanner
intitle:"Acunetix report"           # Acunetix web scanner
intitle:"penetration test report"   # Pentest reports
intitle:"vulnerability assessment"  # VA reports
intitle:"security audit"            # Security audits
```

**File Type Combinations:**
```
filetype:pdf "penetration test"
filetype:doc "vulnerability assessment"
filetype:html "Nessus scan report"
```

### 7. **Example 1 (Basic)**

**Dork:**
```
intitle:"Nessus scan report"
```

**Kya Hoga:**
- Exposed Nessus scan reports
- Mix of real reports aur tutorials

**Output:** Broad results, filtering needed.

**Better Version:**
```
intitle:"Nessus scan report" -site:youtube.com -site:slideshare.net filetype:html
```
**Output:** Actual Nessus reports (tutorials excluded)! 🎯

### 8. **Example 2 (Pentester-Focused)**

**Dork:**
```
site:target.com (intitle:"penetration test" | intitle:"security audit" | intitle:"vulnerability assessment") (filetype:pdf | filetype:doc | filetype:docx)
```

**Analysis:**
- `site:target.com` - Specific target
- Three report types
- Three file formats
- Total 9 combinations!

**Output:** Target ke exposed security reports - complete vulnerability list! 💣

**Nessus Specific:**
```
site:target.com intitle:"Nessus scan report" (intext:"critical" | intext:"high") filetype:html
```
**Output:** Critical/high severity vulnerabilities waale Nessus reports.

**Historical Search:**
```
site:target.com "penetration test report" 2020..2023 filetype:pdf
```
**Output:** 2020-2023 ke beech ke pentest reports - historical vulnerability data.

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **No Filtering:** Generic search - tutorials aur training materials aa jaayenge.
- **Opening Reports:** Report mil gayi toh open karke padhna - ILLEGAL! Existence hi enough hai.
- **Ignoring Old Reports:** Purane reports ignore karna - historical data valuable hai.

### 10. **Best Practices / Pro Tips**

- **Top Report Dorks:**
  ```
  intitle:"Nessus scan report" filetype:html
  intitle:"penetration test report" filetype:pdf
  intitle:"Acunetix report" filetype:html
  filetype:pdf "vulnerability assessment" "executive summary"
  intitle:"security audit" (intext:"findings" | intext:"recommendations")
  ```
- **Exclude Training Sites:** `-site:slideshare.net -site:scribd.com -site:academia.edu`
- **Look for Dates:** Reports mein dates hote hain - recent ones zyada relevant.
- **Check Metadata:** PDF metadata mein company name, author details ho sakte hain.
- **Cross-Reference:** Report mein mentioned vulnerabilities ko verify karo (ethical testing).

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

Ek bug bounty hunter "FinanceApp" ke program mein tha. Usne routine dorking karte waqt yeh dork chalaya: `site:financeapp.com intitle:"penetration test" filetype:pdf`. Ek result mila - `reports.financeapp.com/pentest-2022.pdf`. Yeh ek third-party pentesting company ki report thi jo accidentally public S3 bucket mein upload ho gayi thi! Report mein:
- 15 critical vulnerabilities listed thi
- Internal IP addresses
- Database schema details
- Admin panel URLs

Hunter ne immediately report kiya (PDF open nahi kiya, sirf URL). Company shocked thi - yeh report confidential thi! Unhone:
1. Report delete ki
2. S3 permissions fix kiye
3. Report mein mentioned vulnerabilities fix kiye (jo abhi bhi open the)
4. Hunter ko $5000 bounty + bonus diya

Ek dork ne complete vulnerability roadmap expose kar diya! 🗺️

### 12. **Checklist / Chota Recap (TL;DR)**

✅ Vulnerability reports = Nessus, Acunetix, pentest reports  
✅ `intitle:` + `filetype:` combination most effective  
✅ Exclude training/tutorial sites  
✅ Report mili = URL note karo, open MAT karo  
✅ Historical reports bhi valuable - time range use karo  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Report mil gayi, kya main padh sakta hoon vulnerabilities dekhne ke liye?**  
**A:** Nahi! Report ka existence hi finding hai. Open karna = unauthorized access. Sirf URL aur screenshot report karo.

**Q2: Kya yeh reports really sensitive hain?**  
**A:** Bahut! Inmein complete vulnerability list, internal network details, exploitation steps - sab hota hai. Attackers ke liye goldmine.

**Q3: Sabse common exposed report type kaunsi hai?**  
**A:** Nessus HTML reports - kyunki yeh automatically generate hote hain aur admins accidentally web servers par upload kar dete hain.

### 14. **Practice ke liye Task**

**Task:** Vulnerability report hunting:

**Dork 1:**
```
intitle:"Nessus scan report" -site:youtube.com
```

**Dork 2:**
```
filetype:pdf "penetration test report" "executive summary" site:edu
```

**Kya Karna Hai:**
1. Dono dorks search karo
2. Results count note karo
3. Pehle 3 results ke titles dekho (OPEN MAT KARO)
4. Samjho ki:
   - Dork 1: Nessus reports kitne common hain
   - Dork 2: Educational institutions ke pentest reports
5. Note karo ki yeh reports mein kya information hoti hai (titles/snippets se)

**Expected Learning:** Security reports ka exposure kitna common aur dangerous hai.

### 15. **Aakhri Choti Summary (5 lines)**

- 📊 Vulnerability reports = Nessus, Acunetix, pentest reports (ready-made vuln lists)
- 🎯 `intitle:` + `filetype:` se specific reports dhoondho
- 🚨 Report existence = Critical finding (complete attack roadmap exposed)
- 📝 Report mili = Screenshot lo, open MAT karo
- ⏰ Historical reports bhi check karo - unfixed vulns mil sakte hain

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Exposed vulnerability reports 'cheat codes' hain attackers ke liye - poora game plan ready! Irony yeh hai ki security reports hi insecure hain!" 🎮

---


## **Topic 5: Dorking for Exposed Devices (`intitle:"WEB CAM 7" inurl:admin.html`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Exposed Device Dorking** - Internet-connected devices (cameras, routers, printers) jo publicly accessible hain, unhe discover karo.

### 2. **Ye Kya Hai? (What is it?)**

Exposed device dorking ek technique hai jismein aap IoT devices, IP cameras, routers, printers, aur other network devices dhoondhte ho jo internet par directly accessible hain - often bina authentication ke ya default credentials ke saath.

**Analogy:** Socho har ghar mein CCTV camera hai, lekin kuch log password nahi lagaate. Aap woh "unlocked cameras" dhoondh rahe ho jo koi bhi dekh sakta hai! 📹

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Physical Security Risk:** Cameras, access control systems exposed hain toh physical security compromise.
- **Network Entry Point:** Exposed routers/devices se internal network mein entry mil sakti hai.
- **Privacy Violations:** Webcams, baby monitors exposed - serious privacy issues.
- **IoT Vulnerabilities:** IoT devices usually outdated firmware aur weak security.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **IoT Assessment:** Company ke exposed IoT devices discover karne ke liye.
- **Physical Security Audit:** Cameras, access systems ki security check.
- **Network Perimeter:** External-facing devices jo network entry points hain.
- **Forgotten Assets:** Purane devices jo IT team bhool gayi hai.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **IoT Attack Surface Miss:** Network devices jo vulnerable hain, undetected rahenge.
- **Physical Security Gaps:** Exposed cameras/access systems ka pata nahi chalega.
- **Easy Entry Points:** Weak IoT devices se network compromise ho sakta hai.

### 6. **Syntax aur Common Options**

**Common Device Types:**
```
intitle:"webcam"                   # Webcams
intitle:"IP Camera"                # IP cameras
intitle:"Network Camera"           # Network cameras
inurl:view/index.shtml             # Axis cameras
intitle:"WEB CAM 7"                # Specific webcam software
inurl:admin.html                   # Admin interfaces
```

**Router/Network Devices:**
```
intitle:"DD-WRT"                   # DD-WRT routers
intitle:"pfSense"                  # pfSense firewalls
intitle:"MikroTik"                 # MikroTik routers
intitle:"Cisco"                    # Cisco devices
```

### 7. **Example 1 (Basic)**

**Dork:**
```
intitle:"webcam"
```

**Kya Hoga:**
- Thousands of webcam interfaces
- Mix of public cameras (traffic, weather) aur private cameras

**Output:** Too broad, ethical concerns.

**Better Version (Ethical):**
```
intitle:"webcam" intitle:"public" (intext:"traffic" | intext:"weather")
```
**Output:** Intentionally public cameras (traffic monitoring, weather stations) - ethical to view! 🎯

### 8. **Example 2 (Pentester-Focused)**

**Dork (Target-Specific, Ethical Assessment):**
```
site:target.com (intitle:"IP Camera" | intitle:"Network Camera" | inurl:view/index.shtml)
```

**Analysis:**
- `site:target.com` - Specific target (with permission!)
- Three camera interface patterns
- Discovers company's exposed cameras

**Output:** Target company ke exposed IP cameras - security assessment finding! 🔥

**Router Discovery:**
```
site:target.com (intitle:"DD-WRT" | intitle:"router" | intitle:"gateway") inurl:admin
```
**Output:** Exposed router admin interfaces.

**Printer Discovery:**
```
site:target.com (intitle:"printer" | intitle:"HP LaserJet" | intitle:"Canon") inurl:status
```
**Output:** Network printers with web interfaces - often contain print logs, network configs.

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Privacy Violation:** Private cameras access karna (even if no password) - ILLEGAL aur unethical!
- **No Permission:** Target company ke devices access karna bina written permission - CRIME!
- **Shodan Confusion:** Google se devices dhoondhna limited hai - Shodan iske liye better hai (Module 6 mein).

### 10. **Best Practices / Pro Tips**

- **Ethical Device Dorks (Public Only):**
  ```
  intitle:"webcam" intitle:"public" intext:"traffic"
  intitle:"weather station" inurl:camera
  intitle:"ski resort" intitle:"webcam"
  ```
- **Assessment Dorks (With Permission):**
  ```
  site:target.com intitle:"IP Camera"
  site:target.com inurl:printer/status
  site:target.com intitle:"router" inurl:admin
  ```
- **Shodan Alternative:** Google limited hai devices ke liye - Shodan.io use karo (Module 6).
- **Never Access:** Device interface mila = Screenshot lo, access MAT karo (even if no password).
- **Report Responsibly:** Exposed devices company ko immediately report karo.

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

Ek security consultant "ManufacturingCo" ka physical security audit kar raha tha (signed contract ke saath). Usne `site:manufacturingco.com intitle:"IP Camera"` dork chalaya aur 15 exposed IP cameras mile. Yeh factory floor ke cameras the jo bina authentication ke accessible the! Consultant ne:
1. Screenshots liye (cameras access nahi kiye, sirf login pages)
2. Detailed report banai
3. Company ko dikhayi ki koi bhi factory operations dekh sakta hai

Company shocked thi - IT team ko pata hi nahi tha ki cameras internet-facing hain. Unhone immediately:
- Cameras ko internal network par move kiya
- VPN access mandatory kiya
- Consultant ko bonus diya

Yeh finding ne potential industrial espionage rok diya! 🏭

### 12. **Checklist / Chota Recap (TL;DR)**

✅ Exposed devices = Cameras, routers, printers (internet-facing)  
✅ Google limited hai - Shodan better (Module 6)  
✅ Ethical concerns - private devices access karna ILLEGAL  
✅ Target-specific (`site:`) aur permission zaroori  
✅ Device mila = Screenshot, access MAT karo  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Agar camera bina password ke accessible hai, kya main dekh sakta hoon?**  
**A:** Legally gray area, ethically WRONG! Agar intentionally public nahi hai (traffic cam, weather), toh access mat karo. Privacy violation hai.

**Q2: Google vs Shodan - devices ke liye kaunsa better?**  
**A:** Shodan! Google sirf web pages index karta hai. Shodan specifically devices scan karta hai (ports, banners, services). Module 6 mein detail.

**Q3: Kya yeh dorks legal hain?**  
**A:** Search karna legal hai, lekin device access karna (bina permission) illegal. "Look, don't touch" rule hamesha apply hota hai.

### 14. **Practice ke liye Task**

**Task:** Ethical device discovery (PUBLIC ONLY):

**Dork 1 (Ethical - Public Cameras):**
```
intitle:"webcam" intitle:"public" intext:"traffic"
```

**Dork 2 (Ethical - Weather Stations):**
```
intitle:"weather station" (intext:"live" | intext:"current")
```

**Kya Karna Hai:**
1. Dono dorks search karo
2. Results dekho - yeh intentionally public hain (traffic monitoring, weather)
3. Samjho ki difference kya hai:
   - Public cameras (ethical to view)
   - Private cameras (unethical, even if accessible)
4. Note karo ki exposed devices kyun security risk hain

**Expected Learning:** Device exposure risks aur ethical boundaries.

### 15. **Aakhri Choti Summary (5 lines)**

- 📹 Exposed devices = Cameras, routers, printers (internet-facing, often no auth)
- 🎯 Google limited - Shodan better for device hunting (Module 6)
- 🚨 Ethical concerns critical - private devices access karna ILLEGAL
- 🔐 Target-specific search mein permission mandatory
- 💡 Device mila = Report karo, access MAT karo (privacy violation)

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Exposed device dorking powerful hai lekin ethical minefield bhi! Google se limited results, Shodan se comprehensive (Module 6). Hamesha yaad rakho: 'Look, Don't Touch' - especially cameras!" 👁️

---

# **🎓 Module 4 Complete! Congratulations!**

Aapne **Practical Hacking & Databases** master kar liye! Ab aap:
- ✅ GHDB (Google Hacking Database) use kar sakte ho - 6000+ ready dorks
- ✅ Login pages aur admin panels discover kar sakte ho
- ✅ Sensitive files (.env, .sql, .log) hunt kar sakte ho
- ✅ Vulnerability reports dhoondh sakte ho
- ✅ Exposed devices (cameras, routers) identify kar sakte ho

**Yeh module real-world pentesting ka core hai!** 🚀

**Key Takeaways:**
- GHDB time-saver hai - reinvent the wheel mat karo
- Sensitive files (.env) sabse high-priority targets hain
- Hamesha ethical boundaries yaad rakho - "Look, Don't Touch!"
- Evidence collection = Screenshots, URLs (files/devices open mat karo)

**Next Step:** Module 5 mein aap **Beyond Google (Other Search Engines)** seekhoge:
- Bing dorks (unique operators like `ip:`)
- Bing vs Google differences
- Cross-platform dorking strategies

**Practice Reminder:** GHDB explore karo, har category mein 5-10 dorks try karo (ethical targets par). Real-world practice se patterns samajh aayenge! 💪

**Ethical Reminder:** Module 4 mein bahut powerful techniques hain - misuse mat karo. Hamesha permission ke saath kaam karo, aur "responsible disclosure" follow karo! 🛡️

---

=============================================================

# **Google Dork And Search Engine Dorking: Zero-to-Hacker Notes** 🚀

---

# **Module 5: Beyond Google (Other Search Engines)**

---

## **Topic 1: Why Use Bing? (Different Results & Operators)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Bing for OSINT** - Microsoft ka search engine jo Google se alag results aur unique operators deta hai.

### 2. **Ye Kya Hai? (What is it?)**

**Bing** Microsoft ka search engine hai jo Google ka alternative hai. OSINT mein Bing important hai kyunki:
- Different indexing algorithm (alag pages index karta hai)
- Unique operators jo Google mein nahi hain (jaise `ip:`)
- US/EU data mein zyada focus
- Less restrictive (Google jitna strict nahi)

**Analogy:** Socho Google aur Bing dono libraries hain, lekin different books hain. Ek library mein jo book nahi mili, dusri mein mil sakti hai! 📚

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Different Index:** Bing alag pages index karta hai - Google miss karega, Bing pakdega.
- **Unique Operators:** `ip:` operator (reverse IP lookup) sirf Bing mein hai - pentesting ke liye critical.
- **Cross-Verification:** Ek engine par nahi mila, dusre par try karo - comprehensive coverage.
- **Less Blocking:** Google jaldi CAPTCHA dikhata hai, Bing zyada tolerant hai.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Google Results Incomplete:** Jab Google par expected results nahi mile.
- **IP-Based Search:** Reverse IP lookup chahiye (specific IP par hosted sites).
- **US/EU Targets:** American/European companies ke liye Bing better coverage.
- **Avoiding Detection:** Google par bahut searches ki toh CAPTCHA - Bing switch karo.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Incomplete Coverage:** Sirf Google use karoge toh 30-40% data miss ho jaayega.
- **Unique Operators Miss:** `ip:` jaise powerful operators ka fayda nahi utha paoge.
- **Single Point of Failure:** Ek engine block hua toh recon ruk jaayega.

### 6. **Syntax aur Common Options**

**Bing Operators (Google jaisi):**
```
site:example.com                   # Domain-specific
filetype:pdf                       # File types
intitle:admin                      # Title search
inurl:login                        # URL search
```

**Bing Unique Operators:**
```
ip:192.168.1.1                     # Reverse IP lookup (UNIQUE!)
contains:admin                     # Contains links to
feed:keyword                       # RSS feeds
hasfeed:example.com                # Sites with RSS
```

### 7. **Example 1 (Basic)**

**Google vs Bing Comparison:**

**Google Dork:**
```
site:example.com filetype:pdf confidential
```

**Same Bing Dork:**
```
site:example.com filetype:pdf confidential
```

**Kya Hoga:**
- Dono similar results denge
- Lekin Bing mein kuch alag PDFs bhi honge jo Google ne index nahi kiye

**Output:** Cross-verification se comprehensive results! 🎯

### 8. **Example 2 (Pentester-Focused)**

**Bing's Unique Power - `ip:` Operator:**

**Dork:**
```
ip:104.21.45.67
```

**Analysis:**
- Yeh IP address par hosted SAARI sites dikhayega
- Reverse IP lookup - ek IP par multiple sites ho sakti hain
- Shared hosting environments discover karne ke liye perfect

**Output:** Ek IP par hosted saari websites - hidden connections expose! 🔥

**Real Example:**
```
ip:target-company-ip filetype:pdf
```
**Output:** Target company ke IP par hosted saari PDFs - even from different domains/subdomains.

**Another Unique Dork:**
```
contains:admin site:target.com
```
**Output:** Pages jo "admin" links contain karte hain (Google mein yeh operator nahi hai).

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Bing Ignore Karna:** Sirf Google use karna - 40% coverage miss.
- **Same Expectations:** Bing se Google jitne results expect karna - Bing ka index chhota hai.
- **Syntax Confusion:** Google aur Bing ke operators mix karna - test karo pehle.

### 10. **Best Practices / Pro Tips**

- **Cross-Platform Strategy:**
  1. Pehle Google par dork chalao
  2. Phir same dork Bing par
  3. Results compare karo - unique findings note karo
- **Use Bing for IP Searches:** `ip:` operator Bing ka superpower hai - exploit karo.
- **Bing API:** Bing ka API Google se zyada accessible hai - automation ke liye better.
- **DuckDuckGo Bonus:** DuckDuckGo bhi Bing ke results use karta hai - privacy chahiye toh DDG.

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

Ek pentester "TechStartup" ka assessment kar raha tha. Usne Google par `site:techstartup.com filetype:env` chalaya - koi result nahi. Frustrated hokar usne Bing par same dork try kiya - EK result mila! Bing ne ek forgotten subdomain index kiya tha jo Google ne miss kar diya. Us subdomain par .env file exposed thi with database credentials! Pentester ne report kiya, company ne file remove ki, aur pentester ko bonus mila. Bing ne woh dhoondh diya jo Google miss kar gaya! 💰

**IP Operator Example:**
Ek researcher ne `ip:company-server-ip` Bing par chalaya aur pata chala ki same IP par 5 aur domains hosted hain (shared hosting). Un 5 domains mein se ek mein SQL injection vulnerability thi jo main domain ko bhi affect kar sakti thi (same server). Bing ke `ip:` operator ne hidden attack vector expose kar diya!

### 12. **Checklist / Chota Recap (TL;DR)**

✅ Bing = Google ka alternative with different index  
✅ Unique operator: `ip:` (reverse IP lookup)  
✅ Cross-verification strategy - Google + Bing = comprehensive  
✅ US/EU data mein better coverage  
✅ Less blocking/CAPTCHA than Google  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kya Bing Google se better hai?**  
**A:** Nahi, different hai. Google ka index bada hai, lekin Bing alag pages index karta hai. Dono use karo for complete coverage.

**Q2: Kya saare Google operators Bing mein kaam karte hain?**  
**A:** Most operators same hain (site:, filetype:, intitle:), lekin kuch differences hain. Test karke confirm karo.

**Q3: `ip:` operator kitna accurate hai?**  
**A:** Bahut accurate! Lekin sirf Bing-indexed sites dikhayega. Complete reverse IP ke liye tools (ViewDNS, SecurityTrails) bhi use karo.

### 14. **Practice ke liye Task**

**Task:** Google vs Bing comparison:

**Step 1:** Google par yeh dork chalao:
```
site:github.com filetype:env "API_KEY"
```

**Step 2:** Bing par same dork:
```
site:github.com filetype:env "API_KEY"
```

**Step 3:** Bing unique operator try karo (koi bhi public IP):
```
ip:8.8.8.8
```

**Kya Karna Hai:**
1. Google aur Bing ke results compare karo
2. Note karo ki kaunse results unique hain (ek mein hain, dusre mein nahi)
3. `ip:` operator se kya results aaye
4. Samjho ki cross-platform search kyun important hai

**Expected Learning:** Multi-engine strategy ki power.

### 15. **Aakhri Choti Summary (5 lines)**

- 🔍 Bing = Google ka alternative with different index (30-40% unique results)
- 🎯 Unique operator: `ip:` (reverse IP lookup - pentester essential)
- ⚡ Cross-verification strategy - Google + Bing = comprehensive coverage
- 🌐 US/EU targets ke liye better, less blocking than Google
- 💡 Hamesha dono engines use karo - ek miss karega, dusra pakdega

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Bing Google ka 'backup' nahi, 'partner' hai OSINT mein. `ip:` operator Bing ka superpower hai - reverse IP lookup instant! Dono engines = double coverage!" 🔄

---

## **Topic 2: Bing Dork: `ip:` (Reverse IP Lookup - Pentester Essential)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**ip: Operator** - Specific IP address par hosted saari websites discover karo (Bing exclusive).

### 2. **Ye Kya Hai? (What is it?)**

**`ip:`** operator Bing ka unique feature hai jo reverse IP lookup karta hai - matlab ek IP address par hosted SAARI websites/domains dikhata hai. Yeh shared hosting environments, virtual hosts, aur hidden connections discover karne ke liye perfect hai.

**Analogy:** Socho ek apartment building hai (IP address). `ip:` operator building ke saare flats (websites) ki list deta hai - kaun-kaun rehta hai! 🏢

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Shared Hosting Discovery:** Ek IP par multiple sites - ek vulnerable hai toh baaki bhi risk mein.
- **Hidden Connections:** Company ke different brands/subsidiaries jo same IP use karte hain.
- **Attack Surface Expansion:** Ek target se multiple targets discover karo.
- **Virtual Host Enumeration:** Apache/Nginx virtual hosts jo DNS se miss ho jaate hain.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Shared Hosting Check:** Target shared hosting par hai ya dedicated?
- **Subsidiary Discovery:** Company ke hidden domains/brands.
- **Lateral Movement:** Ek site vulnerable hai, same IP ki baaki sites check karo.
- **Network Mapping:** Company ke IP ranges par kya-kya hosted hai.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Hidden Assets Miss:** Same IP par hosted other sites/domains undetected.
- **Incomplete Attack Surface:** Ek IP par 10 sites hain, aap sirf 1 dekh rahe ho.
- **Lateral Opportunities Lost:** Shared hosting vulnerabilities exploit nahi kar paoge.

### 6. **Syntax aur Common Options**

```
ip:192.168.1.1                     # Basic reverse IP
ip:target-ip filetype:pdf          # PDFs on that IP
ip:target-ip inurl:admin           # Admin panels on that IP
ip:target-ip site:*.com            # Only .com domains on that IP
```

**Important Notes:**
- Sirf Bing mein kaam karta hai (Google mein nahi)
- Public IPs ke liye kaam karta hai (private IPs nahi)
- Bing-indexed sites hi dikhayega (complete list ke liye tools chahiye)

### 7. **Example 1 (Basic)**

**Step 1:** Target ka IP nikalo (nslookup/dig):
```
nslookup target.com
```
Output: `104.21.45.67`

**Step 2:** Bing par reverse IP:
```
ip:104.21.45.67
```

**Kya Hoga:**
- Is IP par hosted saari sites dikhegi
- Main target ke alawa other domains bhi

**Output:** Hidden domains/sites jo same IP use kar rahe hain! 🎯

### 8. **Example 2 (Pentester-Focused)**

**Dork:**
```
ip:target-company-ip (inurl:admin | inurl:login | inurl:dashboard)
```

**Analysis:**
- Target company ke IP par hosted saari sites
- Jinke URLs mein admin/login/dashboard hai
- Ek IP par multiple admin panels discover!

**Output:** Same IP ke saare admin interfaces - shared hosting vulnerability! 🔥

**Real Example:**
```
ip:104.21.45.67 filetype:env
```
**Output:** Is IP par hosted sites ki exposed .env files.

**Subsidiary Discovery:**
```
ip:main-company-ip
```
**Output:** Main company ke IP par hosted saare brands/subsidiaries - hidden connections!

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Google Par Try Karna:** `ip:` sirf Bing mein hai - Google par kaam nahi karega.
- **Private IPs:** `ip:192.168.1.1` (private IP) - yeh kaam nahi karega, sirf public IPs.
- **Incomplete Reliance:** Bing sirf indexed sites dikhayega - complete list ke liye ViewDNS/SecurityTrails use karo.

### 10. **Best Practices / Pro Tips**

- **IP Discovery Methods:**
  - `nslookup target.com` (command line)
  - `dig target.com` (Linux)
  - Online tools: whatismyipaddress.com
- **Combine with Other Operators:**
  ```
  ip:target-ip filetype:pdf "confidential"
  ip:target-ip inurl:backup
  ip:target-ip intitle:"index of"
  ```
- **Multiple IPs:** Company ke multiple IPs hain toh sabko check karo.
- **Tools for Complete List:**
  - ViewDNS.info (Reverse IP Lookup)
  - SecurityTrails (IP Explorer)
  - Shodan (IP search)

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

Ek bug bounty hunter "RetailCorp" ke program mein tha. Main website (retailcorp.com) secure thi. Hunter ne IP nikala: `nslookup retailcorp.com` → `203.0.113.50`. Phir Bing par `ip:203.0.113.50` chalaya. Results:
1. retailcorp.com (main site)
2. retailcorp-staging.com (staging environment!)
3. retailcorp-dev.com (development site!)
4. oldretail.com (purani site, forgotten)

Hunter ne staging aur dev sites check kiye - dono mein debug mode enabled tha aur sensitive info expose ho rahi thi! Usne report kiya:
- Company ko pata hi nahi tha ki staging/dev public IPs par hain
- Unhone immediately sites ko internal network par move kiya
- Hunter ko $3000 bounty mili

Ek `ip:` operator ne 1 target se 4 targets bana diye! 💰

### 12. **Checklist / Chota Recap (TL;DR)**

✅ `ip:` = Reverse IP lookup (Bing exclusive)  
✅ Ek IP par hosted saari sites discover karo  
✅ Shared hosting, subsidiaries, hidden domains milte hain  
✅ Sirf public IPs, sirf Bing mein  
✅ Complete list ke liye ViewDNS/SecurityTrails bhi use karo  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kya `ip:` operator complete list deta hai?**  
**A:** Nahi, sirf Bing-indexed sites. Complete list ke liye ViewDNS.info ya SecurityTrails use karo (yeh DNS records check karte hain).

**Q2: Kya main multiple IPs ek saath search kar sakta hoon?**  
**A:** Nahi directly. Har IP ke liye alag search karna padega: `ip:1.1.1.1`, phir `ip:2.2.2.2`

**Q3: Shared hosting mein vulnerability kyun important hai?**  
**A:** Agar ek site vulnerable hai (same IP par), toh attacker us site se dusri sites ko bhi affect kar sakta hai (server-level access mil jaaye toh).

### 14. **Practice ke liye Task**

**Task:** Reverse IP lookup practice:

**Step 1:** Kisi bhi popular site ka IP nikalo:
```
nslookup github.com
```
(Example IP: `140.82.121.4`)

**Step 2:** Bing par reverse IP:
```
ip:140.82.121.4
```

**Step 3:** Results analyze karo:
- Kitni sites same IP use kar rahi hain?
- Kya yeh shared hosting hai ya dedicated?

**Step 4:** (Optional) ViewDNS.info par same IP check karo:
- viewdns.info/reverseip
- IP enter karo
- Bing vs ViewDNS results compare karo

**Kya Karna Hai:**
1. Samjho ki reverse IP lookup kaise kaam karta hai
2. Note karo ki Bing vs tools mein kya difference hai
3. Socho ki pentesting mein yeh kyun useful hai

**Expected Learning:** Reverse IP ki power aur limitations.

### 15. **Aakhri Choti Summary (5 lines)**

- 🔍 `ip:` operator Bing exclusive - reverse IP lookup instant
- 🏢 Ek IP par hosted saari sites discover (shared hosting, subsidiaries)
- 🎯 Attack surface expansion - 1 target se multiple targets
- ⚡ Combine with other operators: `ip:x.x.x.x filetype:pdf`
- 🛠️ Complete list ke liye ViewDNS/SecurityTrails bhi use karo

> **📌 Ye Zaroor Yaad Rakhein:**  
> "`ip:` operator pentester ka 'X-ray vision' hai - ek IP ke andar kya-kya chhupa hai, sab dikhta hai! Shared hosting = shared risk!" 🔬

---

## **Topic 3: Bing Dork: `contains:` (Finding File Links)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**contains: Operator** - Pages jo specific keywords ke links contain karte hain, unhe discover karo.

### 2. **Ye Kya Hai? (What is it?)**

**`contains:`** operator Bing ka feature hai jo pages dhoondhta hai jismein specific keywords ke LINKS hain (not just text). Matlab page content mein nahi, lekin page ke links mein woh keyword hai.

**Analogy:** Socho ek directory hai jismein different shops ke addresses (links) hain. `contains:admin` matlab "Mujhe woh directory dikhao jismein 'admin' shop ka address hai." 🗂️

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Link Discovery:** Pages jo specific resources ko link kar rahe hain.
- **Directory Listings:** Index pages jo files/folders ko link karte hain.
- **Navigation Pages:** Site maps, menus jo admin/sensitive pages link karte hain.
- **Different from inurl:** `inurl:` URL mein keyword dhoondhta hai, `contains:` links mein.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Link-Based Discovery:** Jab aapko pages chahiye jo specific resources link karte hain.
- **Directory Hunting:** Index pages jo files list karte hain.
- **Navigation Analysis:** Site structure samajhne ke liye.
- **Alternative to inurl:** Jab `inurl:` kaam nahi kar raha.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Link-Based Intel Miss:** Pages jo sensitive resources link karte hain, undetected.
- **Directory Listings:** Index pages jo file links contain karte hain, chhoot jaayenge.
- **Limited Toolkit:** Ek aur useful operator ka fayda nahi utha paoge.

### 6. **Syntax aur Common Options**

```
contains:admin                     # Pages with links containing "admin"
contains:backup site:target.com    # Target site pages linking to "backup"
contains:pdf                       # Pages with PDF links
contains:download                  # Pages with download links
```

**Important Notes:**
- Bing-specific operator (Google mein nahi)
- Links mein keyword dhoondhta hai, page content mein nahi
- Directory listings discover karne ke liye useful

### 7. **Example 1 (Basic)**

**Dork:**
```
contains:admin
```

**Kya Hoga:**
- Pages jismein "admin" word ke links hain
- Example: `<a href="/admin">Admin Panel</a>`

**Output:** Pages jo admin resources link kar rahe hain.

**Better Version:**
```
contains:admin site:target.com -inurl:wordpress
```
**Output:** Target site ke pages jo admin links contain karte hain (WordPress excluded).

### 8. **Example 2 (Pentester-Focused)**

**Dork:**
```
site:target.com contains:backup (contains:sql | contains:database)
```

**Analysis:**
- Target site ke pages
- Jo "backup" links contain karte hain
- Aur "sql" ya "database" links bhi

**Output:** Directory listings ya pages jo backup files link kar rahe hain! 🔥

**File Discovery:**
```
site:target.com contains:download contains:pdf
```
**Output:** Pages jismein PDF download links hain - document repository discover!

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **inurl vs contains Confusion:** `inurl:admin` (URL mein) vs `contains:admin` (links mein) - dono alag hain.
- **Content Expectation:** `contains:password` se pages nahi milenge jismein "password" text hai - sirf links.
- **Limited Use:** Yeh operator kam use hota hai - `inurl:` zyada effective usually.

### 10. **Best Practices / Pro Tips**

- **Use Cases:**
  - Directory listings: `contains:backup`
  - Download pages: `contains:download`
  - Navigation pages: `contains:admin`
- **Combine with site::** Hamesha target-specific banao.
- **Alternative to filetype:** `contains:pdf` se pages milenge jo PDFs link karte hain.
- **Limited Utility:** Honestly, `inurl:` aur `intitle:` zyada useful hain - `contains:` niche use case hai.

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

Ek pentester "DocumentCorp" ka assessment kar raha tha. Usne `site:documentcorp.com contains:confidential` dork chalaya. Ek internal directory listing page mila jismein confidential documents ke links the. Page khud publicly accessible tha (no auth), lekin documents password-protected the. Pentester ne:
1. Directory listing ka screenshot liya
2. Document names note kiye (sensitive info reveal kar rahe the)
3. Report kiya ki directory listing exposed hai

Company ne directory listing disable ki aur pentester ko bounty di. `contains:` operator ne hidden directory expose kar diya! 💰

### 12. **Checklist / Chota Recap (TL;DR)**

✅ `contains:` = Pages jo specific keywords ke links contain karte hain  
✅ Bing-specific (Google mein nahi)  
✅ Links mein keyword, content mein nahi  
✅ Directory listings, download pages discover karne ke liye  
✅ Limited use - `inurl:` usually better  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `contains:` aur `inurl:` mein kya difference hai?**  
**A:** `inurl:admin` = URL mein "admin" (`example.com/admin`). `contains:admin` = Page ke links mein "admin" (`<a href="/admin">`). Dono alag concepts hain.

**Q2: Kya `contains:` bahut useful hai?**  
**A:** Honestly, limited use hai. `inurl:`, `intitle:`, `filetype:` zyada powerful hain. Lekin specific cases mein (directory listings) useful ho sakta hai.

**Q3: Kya Google mein alternative hai?**  
**A:** Nahi direct alternative. Google mein `inurl:` aur `intitle:` use karo similar results ke liye.

### 14. **Practice ke liye Task**

**Task:** `contains:` operator test karo:

**Dork 1:**
```
contains:download site:github.com
```

**Dork 2:**
```
contains:admin site:edu
```

**Kya Karna Hai:**
1. Dono dorks Bing par chalao
2. Results dekho - kya pages link-based discovery kar rahe hain
3. Compare karo: `inurl:download` vs `contains:download`
4. Samjho ki `contains:` ka specific use case kya hai

**Expected Learning:** Link-based discovery aur `contains:` ki limitations.

### 15. **Aakhri Choti Summary (5 lines)**

- 🔗 `contains:` pages jo specific keywords ke links contain karte hain
- 🎯 Bing-specific operator (Google mein nahi)
- 📂 Directory listings, download pages discover karne ke liye
- ⚠️ Limited utility - `inurl:` usually better
- 💡 Niche use cases mein helpful (link-based discovery)

> **📌 Ye Zaroor Yaad Rakhein:**  
> "`contains:` operator Bing ka 'bonus feature' hai - useful hai lekin game-changer nahi. `ip:` operator Bing ka asli superpower hai!" 🎁

---

# **🎓 Module 5 Complete! Congratulations!**

Aapne **Beyond Google (Other Search Engines)** master kar liye! Ab aap:
- ✅ Bing ka importance samajhte ho (different index, unique operators)
- ✅ `ip:` operator use kar sakte ho (reverse IP lookup - pentester essential!)
- ✅ `contains:` operator jaante ho (link-based discovery)
- ✅ Cross-platform dorking strategy implement kar sakte ho

**Key Takeaways:**
- Bing = Google ka partner, not replacement (30-40% unique results)
- `ip:` operator = Bing ka superpower (shared hosting, subsidiaries discover)
- Cross-verification = Google + Bing = comprehensive coverage
- `contains:` = Niche use case (limited utility)

**Next Step:** Module 6 mein aap **Shodan (IoT & Device Search Engine)** seekhoge:
- Shodan introduction (hackers ka Google)
- Basic filters (port, country, city, org)
- Advanced filters (product, version, os, hostname)
- Pentester filters (vuln, has_screenshot, tag)

**Yeh sabse exciting module hoga - Shodan real-world devices dhoondhta hai!** 🚀

**Practice Reminder:** Bing par 10-15 dorks try karo (especially `ip:` operator). Google vs Bing results compare karo - difference samajh aayega! 💪

---
=============================================================

# **Google Dork And Search Engine Dorking: Zero-to-Hacker Notes** 🚀

---

# **Module 6: Shodan (The IoT & Device Search Engine)**

---

## **Topic 1: Intro to Shodan (What is it? Banners?)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Shodan** - Internet-connected devices ka search engine (servers, cameras, routers, IoT) - "Hackers ka Google"!

### 2. **Ye Kya Hai? (What is it?)**

**Shodan** ek specialized search engine hai jo web pages nahi, balki **devices** ko index karta hai - servers, routers, webcams, industrial systems, IoT devices. Yeh internet par continuously scan karta hai aur devices ki "banners" collect karta hai.

**Banner kya hai?** Jab aap kisi device/service se connect karte ho, woh apni identity reveal karta hai - software name, version, OS, etc. Yeh information "banner" kehlati hai.

**Analogy:** Google ek librarian hai jo books (web pages) organize karta hai. Shodan ek security guard hai jo building mein saare devices (cameras, locks, sensors) ki list rakhta hai! 🏢

**Example Banner:**
```
HTTP/1.1 200 OK
Server: Apache/2.4.29 (Ubuntu)
X-Powered-By: PHP/7.2.10
```
Yeh banner batata hai: Apache server, version 2.4.29, Ubuntu OS, PHP 7.2.10

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Device Discovery:** Google web pages dhoondhta hai, Shodan devices - cameras, servers, routers, ICS/SCADA.
- **Vulnerability Research:** Specific software versions dhoondhke known vulnerabilities exploit karo.
- **IoT Security:** Exposed IoT devices (cameras, smart home) jo default credentials use karte hain.
- **Network Reconnaissance:** Target company ke saare internet-facing devices ek jagah.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Device Enumeration:** Target ke exposed servers, cameras, routers dhoondhne ke liye.
- **Vulnerability Scanning:** Specific vulnerable versions (Log4j, Heartbleed) dhoondhne ke liye.
- **IoT Assessment:** Company ke forgotten IoT devices discover karne ke liye.
- **Port Scanning Alternative:** Nmap ki jagah passive reconnaissance.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **50% Attack Surface Miss:** Google sirf web pages dikhata hai, devices nahi - poora IoT/device layer miss.
- **Vulnerable Devices Undetected:** Purane software versions waale devices jo easy targets hain.
- **Industrial Systems:** ICS/SCADA systems jo critical infrastructure control karte hain, undetected.

### 6. **Syntax aur Common Options**

**Shodan Access:**
```
Website: https://www.shodan.io
Free Account: 1 result page (10 results)
Paid Account: Unlimited results + API access
```

**Basic Search:**
```
apache                             # "apache" keyword search
port:80                            # Port 80 open devices
country:IN                         # India mein devices
```

**Shodan vs Google:**
| Feature | Google | Shodan |
|---------|--------|--------|
| Indexes | Web pages | Devices/Services |
| Search | Content | Banners/Ports |
| Results | Websites | IP addresses |
| Use Case | Web recon | Device recon |

### 7. **Example 1 (Basic)**

**Step 1:** Shodan.io par jao aur account banao (free)

**Step 2:** Simple search:
```
webcam
```

**Kya Hoga:**
- Thousands of webcams jo internet par exposed hain
- IP addresses, locations, screenshots (kuch mein)

**Output:** Exposed webcams worldwide - privacy nightmare! 📹

**Step 3:** Filter add karo:
```
webcam country:US
```
**Output:** Sirf US mein exposed webcams.

### 8. **Example 2 (Pentester-Focused)**

**Scenario:** Aapko "TechCorp" company ke exposed servers dhoondhne hain.

**Step 1:** Company ka IP range ya organization name nikalo:
```
whois techcorp.com
```
Output: Organization: "TechCorp Inc", IP range: 203.0.113.0/24

**Step 2:** Shodan par search:
```
org:"TechCorp Inc"
```

**Kya Hoga:**
- TechCorp ke saare internet-facing devices
- Servers, routers, cameras - sab kuch
- Har device ki banner info (software, version, OS)

**Output:** Complete device inventory - attack surface map! 🗺️

**Step 3:** Vulnerable versions dhoondho:
```
org:"TechCorp Inc" apache 2.4.29
```
**Output:** TechCorp ke servers jo purana Apache version use kar rahe hain (known vulnerabilities).

**Real Example - Exposed Database:**
```
port:3306 country:IN
```
**Analysis:**
- Port 3306 = MySQL database
- country:IN = India mein
**Output:** India mein exposed MySQL databases (often no authentication)! 💣

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Google Jaise Use Karna:** Shodan mein web pages nahi milenge - sirf devices/IPs.
- **Free Account Limitations:** Free account sirf 1 page results (10 results) - paid account zaroori for serious work.
- **Direct Access Attempt:** Device mila toh login try karna - ILLEGAL! Sirf discovery karo.

### 10. **Best Practices / Pro Tips**

- **Start with Filters:** Generic search (jaise "apache") se millions results - hamesha filters use karo.
- **Use org: Filter:** Company name se search karo: `org:"Company Name"`
- **Combine Filters:** Multiple filters ek saath: `port:22 country:IN os:ubuntu`
- **Check Screenshots:** `has_screenshot:true` - kuch devices ke screenshots Shodan leta hai.
- **API for Automation:** Serious work ke liye Shodan API use karo (scripting).

**Shodan Cheat Sheet (Beginner):**
```
port:80                    # HTTP servers
port:22                    # SSH servers
port:3389                  # RDP (Remote Desktop)
country:IN                 # India
city:"Mumbai"              # Specific city
os:"Windows"               # Windows OS
```

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

Ek security researcher routine Shodan exploration kar raha tha. Usne yeh search kiya:
```
port:27017 country:US
```
(Port 27017 = MongoDB database)

Results mein 50,000+ exposed MongoDB instances mile - BINA AUTHENTICATION KE! Usne randomly 10 check kiye:
- 7 mein sensitive data tha (customer records, financial data)
- Ek Fortune 500 company ka database bhi tha

Researcher ne responsible disclosure ki:
1. Affected companies ko email kiya (data access nahi kiya, sirf existence report ki)
2. US-CERT ko notify kiya
3. Blog post likha (without naming companies)

Result:
- 1000+ companies ne databases secure kiye
- Researcher ko multiple bounties aur recognition mili
- MongoDB ne default security settings improve kiye

Ek simple Shodan search ne internet-wide vulnerability expose kar diya! 🌐

### 12. **Checklist / Chota Recap (TL;DR)**

✅ Shodan = Device search engine (servers, cameras, routers, IoT)  
✅ Banners = Device identity info (software, version, OS)  
✅ Google = Web pages, Shodan = Devices (complementary tools)  
✅ Free account limited (10 results), paid for serious work  
✅ Hamesha filters use karo - generic search useless  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kya Shodan use karna legal hai?**  
**A:** Haan, search karna 100% legal hai (public data hai). Illegal tab hota hai jab aap devices access karte ho (login, exploit).

**Q2: Shodan kaise data collect karta hai?**  
**A:** Shodan continuously internet scan karta hai (port scanning), devices se connect hota hai, banners collect karta hai. Yeh passive hai - kuch modify nahi karta.

**Q3: Free vs Paid account mein kya difference hai?**  
**A:** Free = 1 result page (10 results), no API. Paid ($59/month) = unlimited results, API access, filters, historical data.

### 14. **Practice ke liye Task**

**Task:** Shodan exploration (ETHICAL ONLY):

**Step 1:** Shodan.io par free account banao

**Step 2:** Yeh searches try karo:

**Search 1:**
```
port:80 country:IN city:"Mumbai"
```
(Mumbai mein HTTP servers)

**Search 2:**
```
apache country:US
```
(US mein Apache servers)

**Search 3:**
```
has_screenshot:true webcam
```
(Webcams with screenshots - intentionally public ones)

**Kya Karna Hai:**
1. Har search ke results dekho (IP addresses, banners)
2. Ek result click karke detail page dekho (banner info, ports, services)
3. Note karo ki Shodan kya information provide karta hai
4. Samjho ki yeh pentesting mein kyun powerful hai
5. **IMPORTANT:** Kisi bhi IP par access attempt MAT karo!

**Expected Learning:** Shodan ki power aur device discovery.

### 15. **Aakhri Choti Summary (5 lines)**

- 🔍 Shodan = Device search engine (servers, cameras, routers, IoT)
- 📡 Banners = Device identity (software, version, OS, services)
- 🌐 Google + Shodan = Complete recon (web pages + devices)
- 💰 Free account limited, paid ($59/month) for serious pentesting
- 🚨 Search legal, device access ILLEGAL (without permission)

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Shodan 'Internet ka map' hai - har device, har port, har service visible hai. Pentesters ke liye goldmine, lekin ethical boundaries critical hain. 'Look, Don't Touch' rule hamesha!" 🗺️

---

## **Topic 2: Basic Filters (`port:`, `country:`, `city:`, `org:`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Shodan Basic Filters** - Search ko narrow karne ke liye fundamental filters (location, port, organization).

### 2. **Ye Kya Hai? (What is it?)**

Shodan filters search results ko refine karte hain - specific ports, countries, cities, ya organizations tak narrow karo. Bina filters ke Shodan search useless hai (millions of results).

**Analogy:** Socho Shodan ek warehouse hai jismein millions devices hain. Filters ek "sorting system" hain - "Mujhe sirf Mumbai ke, port 22 waale, XYZ company ke devices chahiye." 📦

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Targeted Search:** Generic search se millions results - filters se 10-100 relevant results.
- **Geolocation:** Specific country/city mein devices (compliance, legal scope).
- **Port-Based Discovery:** Specific services (SSH, RDP, databases) dhoondhna.
- **Organization Focus:** Target company ke saare devices ek search mein.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Port Scanning:** Specific service dhoondhni hai (SSH, MySQL, RDP).
- **Geo-Targeting:** Specific country/city ke devices (bug bounty scope).
- **Company Assessment:** Target organization ke saare exposed devices.
- **Compliance Check:** Apni company ke devices public internet par kahan exposed hain.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Information Overload:** Bina filters ke millions useless results.
- **Scope Violation:** Wrong country/organization ke devices - legal issues.
- **Time Waste:** Relevant results dhoondhne mein hours waste.

### 6. **Syntax aur Common Options**

**Basic Filters:**
```
port:22                            # SSH port
port:80                            # HTTP
port:443                           # HTTPS
port:3306                          # MySQL
port:3389                          # RDP (Remote Desktop)
port:27017                         # MongoDB
```

```
country:IN                         # India
country:US                         # United States
country:CN                         # China
```

```
city:"Mumbai"                      # Specific city (quotes zaroori)
city:"New York"                    # Multi-word cities
```

```
org:"Company Name"                 # Organization name
org:"Google"                       # Example
```

**Combining Filters:**
```
port:22 country:IN                 # India mein SSH
port:3306 city:"Mumbai"            # Mumbai mein MySQL
org:"TechCorp" port:80             # TechCorp ke HTTP servers
```

### 7. **Example 1 (Basic)**

**Scenario:** Aapko India mein exposed SSH servers dhoondhne hain.

**Step-by-Step:**

**Step 1:** Shodan.io par jao

**Step 2:** Search box mein type karo:
```
port:22 country:IN
```

**Step 3:** Results analyze karo:
- IP addresses of SSH servers in India
- Banner info (SSH version, OS hints)
- Location details

**Output:** India mein 100,000+ exposed SSH servers! 🇮🇳

**Kya Seekha:**
- `port:22` = SSH service
- `country:IN` = India tak limited
- Combination = targeted results

### 8. **Example 2 (Pentester-Focused)**

**Scenario:** Bug bounty program - "TechCorp Inc" ke saare exposed databases dhoondhne hain.

**Step-by-Step:**

**Step 1:** Organization name confirm karo:
```
whois techcorp.com
```
Output: "TechCorp Inc"

**Step 2:** Shodan search:
```
org:"TechCorp Inc" (port:3306 OR port:27017 OR port:5432)
```

**Analysis:**
- `org:"TechCorp Inc"` = Company ke devices
- `port:3306` = MySQL
- `port:27017` = MongoDB
- `port:5432` = PostgreSQL
- OR = Koi bhi ek port

**Step 3:** Results review:
- 5 MySQL servers mile
- 2 MongoDB instances
- 1 PostgreSQL database

**Step 4:** Evidence collection:
- IP addresses note karo
- Banner info screenshot lo
- Port numbers aur versions document karo

**Step 5:** Report:
```
Finding: 8 exposed database servers
Severity: Critical
Evidence: [Screenshots]
Recommendation: Restrict database access to internal network only
```

**Output:** Complete database exposure report - instant high-severity finding! 💣

**Real Example - City-Specific:**
```
city:"Mumbai" port:3389
```
**Analysis:**
- Mumbai mein RDP (Remote Desktop) servers
- Often weak passwords
**Output:** 500+ RDP servers in Mumbai - brute force targets (ethical testing only!).

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **City Without Quotes:** `city:New York` (galat) vs `city:"New York"` (sahi) - multi-word cities mein quotes zaroori.
- **Wrong Country Codes:** `country:India` (galat) vs `country:IN` (sahi) - 2-letter ISO codes use karo.
- **No Filters:** Generic search - millions useless results.

### 10. **Best Practices / Pro Tips**

- **Common Port Cheat Sheet:**
  ```
  21   - FTP
  22   - SSH
  23   - Telnet
  80   - HTTP
  443  - HTTPS
  3306 - MySQL
  3389 - RDP
  5432 - PostgreSQL
  27017 - MongoDB
  ```

- **Organization Discovery:**
  - `whois target.com` se org name nikalo
  - Shodan mein `org:"Exact Name"` use karo
  - Quotes zaroori hain!

- **Multiple Filters:**
  ```
  org:"Company" port:22 country:US
  ```
  (Company ke US mein SSH servers)

- **OR Operator:**
  ```
  port:3306 OR port:27017
  ```
  (MySQL ya MongoDB - dono)

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

Ek pentester "HealthCare Corp" ka security assessment kar raha tha (signed contract). Usne Shodan par yeh search kiya:

```
org:"HealthCare Corp" port:3389
```

**Results:** 15 RDP servers exposed!

**Step-by-Step Investigation:**

**Step 1:** IP addresses note kiye

**Step 2:** Har IP ki banner info analyze ki:
- Windows Server 2012 (purana, vulnerable)
- RDP version 7.0 (known vulnerabilities)

**Step 3:** Location verify kiya:
```
org:"HealthCare Corp" port:3389 city:"Chicago"
```
- 10 servers Chicago office ke the
- 5 servers unknown location (forgotten servers!)

**Step 4:** Report banai:
```
Finding: 15 exposed RDP servers
- 10 in Chicago office (expected)
- 5 in unknown locations (forgotten assets!)
- All running outdated Windows Server 2012
- Vulnerable to BlueKeep (CVE-2019-0708)

Severity: Critical
Risk: Remote code execution, ransomware entry point

Recommendation:
1. Restrict RDP to VPN only
2. Update Windows Server
3. Investigate 5 unknown servers
```

**Company Response:**
- Shocked ki 5 servers bhool gaye the
- Immediately RDP access restricted
- Servers updated
- Pentester ko bonus diya

**Shodan filters ne forgotten assets expose kar diye!** 🏥

### 12. **Checklist / Chota Recap (TL;DR)**

✅ `port:` = Specific service/port (22=SSH, 3306=MySQL, 3389=RDP)  
✅ `country:` = 2-letter ISO code (IN, US, CN)  
✅ `city:` = City name in quotes ("Mumbai", "New York")  
✅ `org:` = Organization name in quotes ("Company Name")  
✅ Combine filters for targeted results  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kitne filters ek saath use kar sakte hain?**  
**A:** Unlimited! Example: `port:22 country:IN city:"Mumbai" org:"TechCorp"` - sab valid hai.

**Q2: OR operator kaise use karein?**  
**A:** Capital OR: `port:3306 OR port:27017` (MySQL ya MongoDB).

**Q3: Kya partial organization name kaam karega?**  
**A:** Haan, lekin exact better hai. `org:Google` se Google LLC, Google Inc sab aayenge. `org:"Google LLC"` specific hai.

### 14. **Practice ke liye Task**

**Task:** Filter mastery practice:

**Exercise 1 - Port Discovery:**
```
port:3306 country:IN
```
**Kya Karna Hai:**
1. Results count note karo
2. Pehle 5 IPs ki banner info dekho
3. MySQL versions note karo
4. Samjho ki exposed databases kyun dangerous hain

**Exercise 2 - City-Specific:**
```
city:"Delhi" port:80
```
**Kya Karna Hai:**
1. Delhi mein kitne HTTP servers hain
2. Kya types ke servers hain (Apache, Nginx, IIS)
3. Banner info se kya pata chalta hai

**Exercise 3 - Organization (Use a public company):**
```
org:"Microsoft" port:443
```
**Kya Karna Hai:**
1. Microsoft ke kitne HTTPS servers exposed hain
2. Locations dekho (worldwide distribution)
3. Samjho ki large companies ka attack surface kitna bada hai

**Exercise 4 - Combination:**
```
port:22 country:US city:"San Francisco"
```
**Kya Karna Hai:**
1. San Francisco mein SSH servers
2. Compare karo: `city:"San Francisco"` vs `city:"New York"`
3. Samjho ki geo-targeting kyun important hai

**Expected Learning:** Filter combinations aur targeted search.

### 15. **Aakhri Choti Summary (5 lines)**

- 🎯 Basic filters = port, country, city, org (search ko narrow karo)
- 🔢 Port filter most important (specific services target karo)
- 🌍 Geo filters (country, city) for compliance aur scope
- 🏢 org filter for company-specific assessment
- ⚡ Combine filters for laser-focused results

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Shodan bina filters ke ocean hai - filters se swimming pool ban jaata hai. Hamesha 2-3 filters combine karo for actionable results!" 🏊

---


## **Topic 3: Advanced Filters (`product:`, `version:`, `os:`, `hostname:`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Shodan Advanced Filters** - Specific software, versions, OS, aur hostnames target karo (vulnerability hunting).

### 2. **Ye Kya Hai? (What is it?)**

Advanced filters Shodan ki real power hain - specific software products, exact versions, operating systems, aur hostnames se search karo. Yeh vulnerability research aur targeted exploitation ke liye critical hain.

**Analogy:** Basic filters "Mumbai mein restaurants" dhoondhte hain. Advanced filters "Mumbai mein Italian restaurants jo 2019 mein khule aur Chef Mario ke hain" dhoondhte hain - bahut specific! 🍝

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Vulnerability Targeting:** Specific vulnerable versions dhoondhna (Log4j 2.15.0, Apache 2.4.49).
- **Technology Stack:** Target ki exact tech stack (Apache, Nginx, IIS, versions).
- **OS-Based Attacks:** Specific OS vulnerabilities exploit karna (Windows 7, Ubuntu 16.04).
- **Hostname Intelligence:** Subdomain discovery aur naming patterns.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **CVE Hunting:** Specific vulnerability waale systems (CVE-2021-44228 = Log4j).
- **Version-Specific Exploits:** Purane versions jo known vulnerabilities hain.
- **OS Targeting:** Specific OS exploits (EternalBlue for Windows 7).
- **Product Research:** Specific software ka exposure (phpMyAdmin, Jenkins).

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Generic Results:** Sirf port/country se bahut broad results - vulnerable systems miss.
- **Version Blindness:** Kaunse versions vulnerable hain, pata nahi chalega.
- **Inefficient Hunting:** Manual filtering ki jagah, Shodan automatically filter kar sakta hai.

### 6. **Syntax aur Common Options**

**Advanced Filters:**
```
product:"Apache"                   # Apache web server
product:"nginx"                    # Nginx
product:"Microsoft IIS"            # IIS
product:"OpenSSH"                  # SSH server
```

```
version:"2.4.49"                   # Specific version
version:"7.2"                      # Version 7.2
```

```
os:"Windows 7"                     # Windows 7
os:"Ubuntu"                        # Ubuntu Linux
os:"Windows Server 2012"           # Specific Windows Server
```

```
hostname:"admin.example.com"       # Specific hostname
hostname:*.example.com             # Wildcard subdomain
```

**Combining Advanced Filters:**
```
product:"Apache" version:"2.4.49"
os:"Windows 7" port:445
hostname:*.target.com port:22
```

### 7. **Example 1 (Basic)**

**Scenario:** Apache 2.4.49 mein path traversal vulnerability hai (CVE-2021-41773). Vulnerable servers dhoondhne hain.

**Step-by-Step:**

**Step 1:** Shodan search:
```
product:"Apache httpd" version:"2.4.49"
```

**Step 2:** Results analyze:
- 50,000+ servers worldwide
- Har server vulnerable hai (known CVE)

**Step 3:** Geo-filter add karo:
```
product:"Apache httpd" version:"2.4.49" country:IN
```

**Output:** India mein 2,000+ vulnerable Apache servers! 🇮🇳

**Kya Seekha:**
- `product:` se specific software
- `version:` se exact vulnerable version
- Combination = targeted vulnerability hunting

### 8. **Example 2 (Pentester-Focused)**

**Scenario:** Bug bounty - "TechCorp" ke Windows 7 machines dhoondhne hain (EternalBlue vulnerability ke liye).

**Step-by-Step:**

**Step 1:** Shodan search:
```
org:"TechCorp Inc" os:"Windows 7" port:445
```

**Analysis:**
- `org:"TechCorp Inc"` = Target company
- `os:"Windows 7"` = Outdated OS (support ended 2020)
- `port:445` = SMB port (EternalBlue target)

**Step 2:** Results:
- 15 Windows 7 machines found!
- All with SMB port open

**Step 3:** Banner analysis:
```
Click on each result → Check banner details:
- SMBv1 enabled? (Vulnerable to EternalBlue)
- Patch level? (KB4012212 installed?)
```

**Step 4:** Evidence collection:
```
Finding: 15 Windows 7 machines with SMB exposed
Vulnerability: EternalBlue (CVE-2017-0144)
Severity: Critical
Risk: Remote code execution, ransomware (WannaCry-style)

Evidence:
- IP: 203.0.113.10 | OS: Windows 7 SP1 | SMBv1: Enabled
- IP: 203.0.113.11 | OS: Windows 7 SP1 | SMBv1: Enabled
[... 13 more]

Recommendation:
1. Upgrade to Windows 10/11 immediately
2. Disable SMBv1
3. Restrict SMB to internal network only
```

**Output:** Critical vulnerability report - instant high-severity finding! 💣

**Real Example - Product Hunting:**
```
product:"phpMyAdmin" country:US
```
**Analysis:**
- phpMyAdmin = Database management tool
- Often default credentials (root/root)
**Output:** 10,000+ phpMyAdmin instances in US - many with weak auth!

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Product Name Typos:** `product:"apache"` vs `product:"Apache httpd"` - exact name zaroori.
- **Version Without Product:** `version:"2.4.49"` alone - product specify karo: `product:"Apache" version:"2.4.49"`
- **OS Variations:** `os:"Win7"` (galat) vs `os:"Windows 7"` (sahi) - full name use karo.

### 10. **Best Practices / Pro Tips**

- **Common Vulnerable Products:**
  ```
  product:"Apache httpd" version:"2.4.49"    # Path traversal
  product:"OpenSSH" version:"7.4"            # User enumeration
  product:"Microsoft IIS" version:"7.5"      # Multiple CVEs
  product:"nginx" version:"1.10.0"           # Integer overflow
  ```

- **OS Targeting:**
  ```
  os:"Windows 7"                             # EternalBlue
  os:"Windows Server 2003"                   # End of life
  os:"Ubuntu 16.04"                          # Old LTS
  ```

- **Hostname Patterns:**
  ```
  hostname:admin.*                           # Admin subdomains
  hostname:dev.*                             # Development
  hostname:staging.*                         # Staging environments
  hostname:*.target.com                      # All subdomains
  ```

- **Version Ranges:**
  Shodan doesn't support ranges directly, use OR:
  ```
  product:"Apache" (version:"2.4.48" OR version:"2.4.49" OR version:"2.4.50")
  ```

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

**Log4Shell Vulnerability (December 2021)**

Jab Log4j vulnerability (CVE-2021-44228) discover hui, ek security researcher ne immediately Shodan par search kiya:

**Step 1:** Initial search:
```
product:"Apache" "log4j"
```
**Results:** 100,000+ servers!

**Step 2:** Vulnerable version targeting:
```
product:"Apache" ("log4j 2.14.1" OR "log4j 2.15.0")
```
**Results:** 50,000+ vulnerable servers

**Step 3:** Critical infrastructure check:
```
product:"Apache" "log4j 2.14.1" (org:"Government" OR org:"Hospital" OR org:"Bank")
```
**Results:** 500+ critical infrastructure servers vulnerable!

**Step 4:** Responsible disclosure:
- US-CERT ko notify kiya
- Affected organizations ko direct email (data access nahi kiya)
- Public advisory release kiya

**Impact:**
- 10,000+ organizations ne patches apply kiye
- Researcher ko multiple CVE credits aur bounties
- Internet-wide vulnerability mitigation

**Shodan advanced filters ne global crisis response mein help ki!** 🌍

**Another Example - Hostname Discovery:**

Ek pentester "FinanceCorp" assess kar raha tha:

```
hostname:*.financecorp.com
```

**Results:**
- www.financecorp.com (known)
- api.financecorp.com (known)
- admin-old.financecorp.com (UNKNOWN!)
- dev-test.financecorp.com (UNKNOWN!)
- staging-2019.financecorp.com (FORGOTTEN!)

**Investigation:**
```
hostname:admin-old.financecorp.com
```
**Banner:** Apache 2.2.15 (2010 version!), PHP 5.3

**Finding:** Forgotten admin panel with 10-year-old software - multiple known vulnerabilities!

**Hostname filter ne hidden assets expose kar diye!** 🔍

### 12. **Checklist / Chota Recap (TL;DR)**

✅ `product:` = Specific software (Apache, nginx, OpenSSH)  
✅ `version:` = Exact version (vulnerability targeting)  
✅ `os:` = Operating system (Windows 7, Ubuntu)  
✅ `hostname:` = Domain/subdomain discovery  
✅ Combine for laser-focused vulnerability hunting  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Product name kaise pata karein?**  
**A:** Shodan results mein banner dekho - exact product name wahan hota hai. Example: "Apache httpd" not just "Apache".

**Q2: Kya version ranges support hain?**  
**A:** Nahi directly. OR operator use karo: `version:"2.4.48" OR version:"2.4.49"`

**Q3: Hostname wildcard kaise kaam karta hai?**  
**A:** `hostname:*.example.com` se saare subdomains (admin.example.com, api.example.com, etc.). `hostname:admin.*` se saare admin subdomains (admin.site1.com, admin.site2.com).

### 14. **Practice ke liye Task**

**Task:** Advanced filter mastery:

**Exercise 1 - Product Discovery:**
```
product:"nginx" country:IN
```
**Kya Karna Hai:**
1. India mein kitne nginx servers hain
2. Versions note karo (banner info mein)
3. Sabse common version kaunsa hai
4. Purane versions identify karo

**Exercise 2 - OS Targeting:**
```
os:"Windows Server 2012" port:3389
```
**Kya Karna Hai:**
1. Kitne Windows Server 2012 machines RDP expose kar rahe hain
2. Yeh OS outdated kyun hai (support ended)
3. Samjho ki yeh vulnerability kyun hai

**Exercise 3 - Version Hunting:**
```
product:"OpenSSH" version:"7.4"
```
**Kya Karna Hai:**
1. OpenSSH 7.4 kitne servers par hai
2. CVE database check karo: OpenSSH 7.4 vulnerabilities
3. Samjho ki version-specific targeting kyun powerful hai

**Exercise 4 - Hostname Discovery (Use a public company):**
```
hostname:*.microsoft.com
```
**Kya Karna Hai:**
1. Microsoft ke kitne subdomains Shodan mein hain
2. Naming patterns note karo (admin, api, dev, etc.)
3. Samjho ki hostname discovery kyun important hai

**Expected Learning:** Advanced filters se targeted vulnerability hunting.

### 15. **Aakhri Choti Summary (5 lines)**

- 🎯 Advanced filters = product, version, os, hostname (vulnerability hunting)
- 🔍 Product + version = specific vulnerable software target karo
- 💻 OS filter = platform-specific exploits (EternalBlue, etc.)
- 🌐 Hostname = subdomain discovery aur forgotten assets
- ⚡ Combine with basic filters for ultimate precision

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Advanced filters Shodan ko 'sniper rifle' bana dete hain - specific vulnerable versions, exact OS, hidden hostnames. CVE hunting ka shortcut!" 🎯

---

## **Topic 4: Pentester Filters (`vuln:CVE-XXXX`, `has_screenshot:true`, `tag:ics`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Shodan Pentester Filters** - Direct vulnerability search, screenshots, aur critical infrastructure tags.

### 2. **Ye Kya Hai? (What is it?)**

Pentester filters Shodan ke most powerful features hain:
- **`vuln:`** - Direct CVE number se vulnerable systems dhoondho
- **`has_screenshot:true`** - Devices jinke screenshots Shodan ne liye hain (RDP, VNC, webcams)
- **`tag:`** - Special tags (ICS, SCADA, malware, honeypot)

**Analogy:** Basic filters "restaurants" dhoondhte hain. Pentester filters "restaurants jahan food poisoning cases hue hain (vuln), jinki photos hain (screenshot), aur jo health department ke watchlist par hain (tag)" dhoondhte hain! 🍴

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Direct CVE Search:** CVE number se instantly vulnerable systems - no manual banner analysis.
- **Visual Confirmation:** Screenshots se verify karo ki device kya hai (camera, desktop, dashboard).
- **Critical Infrastructure:** ICS/SCADA tags se power plants, factories, water treatment identify karo.
- **Time-Saving:** Manual filtering ki jagah, Shodan pre-analyzed data deta hai.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **CVE Exploitation:** Specific vulnerability exploit karna hai (with permission).
- **Visual Recon:** Device type confirm karna hai (screenshot se).
- **ICS/SCADA Assessment:** Critical infrastructure security audit.
- **Quick Wins:** Bug bounty mein fast high-severity findings.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Manual Analysis:** Har banner manually analyze karna - hours waste.
- **Missed Vulnerabilities:** CVE-tagged systems jo instant targets hain, miss ho jaayenge.
- **No Visual Context:** Bina screenshot ke device type guess karna padega.
- **ICS Blindness:** Critical infrastructure systems undetected.

### 6. **Syntax aur Common Options**

**Vulnerability Filter (PAID FEATURE):**
```
vuln:CVE-2021-44228                # Log4Shell
vuln:CVE-2017-0144                 # EternalBlue
vuln:CVE-2014-0160                 # Heartbleed
```

**Screenshot Filter:**
```
has_screenshot:true                # Devices with screenshots
has_screenshot:true port:3389      # RDP with screenshots
has_screenshot:true webcam         # Webcams with screenshots
```

**Tag Filter:**
```
tag:ics                            # Industrial Control Systems
tag:scada                          # SCADA systems
tag:malware                        # Malware-infected devices
tag:honeypot                       # Honeypots (avoid!)
tag:vpn                            # VPN servers
tag:database                       # Database servers
```

**Combining Pentester Filters:**
```
vuln:CVE-2021-44228 country:IN
has_screenshot:true port:5900 country:US
tag:ics port:502
```

### 7. **Example 1 (Basic)**

**Scenario:** Aapko RDP servers ke screenshots dekhne hain (visual confirmation).

**Step-by-Step:**

**Step 1:** Shodan search:
```
has_screenshot:true port:3389
```

**Step 2:** Results browse karo:
- Har result mein screenshot thumbnail
- Click karke full screenshot dekho
- Desktop wallpapers, login screens visible

**Output:** Visual confirmation - yeh sach mein RDP desktops hain! 🖥️

**Kya Seekha:**
- `has_screenshot:true` = Visual evidence
- Port 3389 = RDP
- Screenshots se device type confirm

### 8. **Example 2 (Pentester-Focused)**

**Scenario 1: CVE Hunting (Log4Shell)**

**Step-by-Step:**

**Step 1:** Shodan search (PAID account required):
```
vuln:CVE-2021-44228
```

**Step 2:** Results:
- 100,000+ vulnerable systems worldwide
- Shodan ne automatically detect kiya (banner analysis se)

**Step 3:** Target-specific:
```
vuln:CVE-2021-44228 org:"TechCorp Inc"
```

**Step 4:** Evidence collection:
```
Finding: 5 servers vulnerable to Log4Shell
CVE: CVE-2021-44228
Severity: Critical (CVSS 10.0)
Risk: Remote code execution, full system compromise

Evidence:
- IP: 203.0.113.10 | Product: Apache 2.4.51 | Log4j: 2.14.1
- IP: 203.0.113.11 | Product: Apache 2.4.50 | Log4j: 2.15.0
[... 3 more]

Recommendation:
1. Upgrade Log4j to 2.17.1+ immediately
2. Apply WAF rules
3. Monitor for exploitation attempts
```

**Output:** Direct CVE-to-vulnerable-systems mapping - instant critical finding! 💣

**Scenario 2: ICS/SCADA Discovery**

**Step-by-Step:**

**Step 1:** Shodan search:
```
tag:ics country:IN
```

**Step 2:** Results:
- 500+ Industrial Control Systems in India
- Power plants, factories, water treatment

**Step 3:** Specific protocol:
```
tag:ics port:502 country:IN
```
(Port 502 = Modbus protocol, common in ICS)

**Step 4:** Banner analysis:
```
Click on results:
- Device type: PLC (Programmable Logic Controller)
- Manufacturer: Siemens, Schneider Electric
- Location: Factory floor, power substation
```

**Step 5:** Ethical consideration:
```
⚠️ CRITICAL: ICS systems control physical processes!
- DO NOT attempt access
- DO NOT send any commands
- Report to CERT-In (India) or ICS-CERT (US)
- These are critical infrastructure - lives at risk!
```

**Output:** Critical infrastructure exposure - report to authorities, NOT exploit! 🏭

**Scenario 3: Screenshot-Based Recon**

**Step-by-Step:**

**Step 1:** Webcam discovery:
```
has_screenshot:true product:"webcam"
```

**Step 2:** Results filter:
- Intentionally public cameras (traffic, weather) - OK to view
- Private cameras (homes, offices) - ILLEGAL to view

**Step 3:** Ethical filtering:
```
has_screenshot:true product:"webcam" (title:"traffic" OR title:"weather" OR title:"public")
```

**Output:** Only intentionally public cameras - ethical viewing! 📹

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Free Account CVE Search:** `vuln:` filter PAID feature hai - free account mein kaam nahi karega.
- **ICS Access Attempt:** ICS systems dekhe aur access try kiya - EXTREMELY DANGEROUS aur ILLEGAL!
- **Private Camera Viewing:** Screenshot hai toh dekh liya - privacy violation, potentially illegal.

### 10. **Best Practices / Pro Tips**

- **Top CVEs for Hunting:**
  ```
  vuln:CVE-2021-44228    # Log4Shell (2021)
  vuln:CVE-2017-0144     # EternalBlue (2017)
  vuln:CVE-2014-0160     # Heartbleed (2014)
  vuln:CVE-2019-0708     # BlueKeep (2019)
  vuln:CVE-2021-34527    # PrintNightmare (2021)
  ```

- **Screenshot Use Cases:**
  ```
  has_screenshot:true port:3389              # RDP desktops
  has_screenshot:true port:5900              # VNC
  has_screenshot:true product:"webcam"       # Cameras
  has_screenshot:true "dashboard"            # Admin dashboards
  ```

- **ICS/SCADA Tags:**
  ```
  tag:ics                                    # All ICS
  tag:scada                                  # SCADA systems
  tag:ics port:502                           # Modbus
  tag:ics port:102                           # Siemens S7
  tag:ics port:44818                         # Ethernet/IP
  ```

- **Ethical ICS Research:**
  - NEVER access ICS systems
  - Report to CERT/ICS-CERT
  - Academic research only with permission
  - Lives depend on these systems!

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

**Scenario 1: Heartbleed Discovery (2014)**

Jab Heartbleed vulnerability (CVE-2014-0160) discover hui, researchers ne Shodan use kiya:

**Step 1:** Immediate search:
```
vuln:CVE-2014-0160
```

**Results:** 500,000+ vulnerable servers worldwide!

**Step 2:** Critical services:
```
vuln:CVE-2014-0160 (org:"Bank" OR org:"Hospital" OR org:"Government")
```

**Results:** 10,000+ critical infrastructure servers!

**Step 3:** Mass notification:
- CERT organizations ko notify kiya
- Affected organizations ko direct contact
- Public advisory release

**Impact:**
- 90% servers ne 1 week mein patch kiya
- Major data breaches prevented
- Shodan ne global response accelerate kiya

**Scenario 2: ICS Exposure (Ongoing Issue)**

Ek security researcher ICS exposure study kar raha tha:

**Step 1:** Global ICS search:
```
tag:ics
```

**Results:** 100,000+ ICS devices exposed!

**Step 2:** Critical infrastructure:
```
tag:ics (port:502 OR port:102 OR port:44818)
```

**Results:**
- Power plants: 5,000+
- Water treatment: 2,000+
- Manufacturing: 50,000+

**Step 3:** Geographic analysis:
```
tag:ics country:US
tag:ics country:IN
tag:ics country:CN
```

**Step 4:** Responsible disclosure:
- ICS-CERT ko comprehensive report
- Affected countries ke CERT teams ko notify
- Academic paper publish (no specific IPs)

**Impact:**
- Governments ne ICS security initiatives launch kiye
- Awareness campaigns
- Regulations tighten hue

**Shodan ne global ICS security crisis expose kiya!** 🌍

### 12. **Checklist / Chota Recap (TL;DR)**

✅ `vuln:CVE-XXXX` = Direct CVE search (PAID feature)  
✅ `has_screenshot:true` = Visual confirmation (RDP, VNC, cameras)  
✅ `tag:ics` = Industrial Control Systems (CRITICAL - report only!)  
✅ Combine with other filters for targeted hunting  
✅ ICS systems = NEVER access, always report to authorities  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kya `vuln:` filter free account mein kaam karta hai?**  
**A:** Nahi, yeh PAID feature hai ($59/month Membership plan). Free account mein manual banner analysis karni padegi.

**Q2: Screenshot dekhna legal hai?**  
**A:** Gray area. Intentionally public cameras (traffic, weather) OK. Private cameras (homes, offices) dekhna privacy violation hai - avoid karo.

**Q3: ICS systems ko access karna kitna dangerous hai?**  
**A:** EXTREMELY! Yeh physical processes control karte hain - power grids, water supply, factories. Access attempt se:
- Equipment damage
- Production loss
- Physical harm to people
- Criminal charges (terrorism laws)
NEVER attempt access!

### 14. **Practice ke liye Task**

**Task:** Pentester filter exploration (ETHICAL ONLY):

**Exercise 1 - Screenshot Discovery:**
```
has_screenshot:true port:3389 country:US
```
**Kya Karna Hai:**
1. Results browse karo (screenshots dekho)
2. Note karo ki kya types ke desktops hain
3. Samjho ki visual confirmation kyun important hai
4. **DO NOT attempt login!**

**Exercise 2 - Tag Exploration:**
```
tag:database country:IN
```
**Kya Karna Hai:**
1. India mein kitne database servers tagged hain
2. Types note karo (MySQL, MongoDB, PostgreSQL)
3. Samjho ki tag system kaise kaam karta hai

**Exercise 3 - ICS Awareness (VIEW ONLY):**
```
tag:ics port:502
```
**Kya Karna Hai:**
1. Results count dekho (kitne ICS exposed hain)
2. Banner info padho (device types)
3. Samjho ki yeh exposure kyun critical hai
4. **CRITICAL: Kisi bhi result par click MAT karo, access MAT karo!**

**Exercise 4 - CVE Research (If you have paid account):**
```
vuln:CVE-2019-0708
```
**Kya Karna Hai:**
1. BlueKeep vulnerable systems count
2. Geographic distribution dekho
3. Samjho ki CVE-based hunting kyun powerful hai

**Expected Learning:** Pentester filters ki power aur ethical boundaries.

### 15. **Aakhri Choti Summary (5 lines)**

- 🎯 `vuln:CVE-XXXX` = Direct vulnerability search (PAID, instant targets)
- 📸 `has_screenshot:true` = Visual confirmation (RDP, VNC, cameras)
- 🏭 `tag:ics` = Critical infrastructure (NEVER access, report only!)
- ⚡ Pentester filters = Advanced hunting, pre-analyzed data
- 🚨 ICS systems = Lives at risk, extreme ethical caution required

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Pentester filters Shodan ki 'nuclear option' hain - bahut powerful, bahut dangerous. `vuln:` instant targets deta hai, `tag:ics` critical infrastructure. With great power comes great responsibility!" ⚠️

---

# **🎓 Module 6 Complete! Congratulations!**

Aapne **Shodan (IoT & Device Search Engine)** master kar liye! Ab aap:
- ✅ Shodan kya hai aur banners kaise kaam karte hain
- ✅ Basic filters (port, country, city, org) use kar sakte ho
- ✅ Advanced filters (product, version, os, hostname) se vulnerability hunting
- ✅ Pentester filters (vuln, has_screenshot, tag) ki power samajhte ho

**Shodan Mastery Checklist:**
- ✅ Device discovery (servers, cameras, routers, IoT)
- ✅ Vulnerability targeting (CVE-based, version-specific)
- ✅ Geographic filtering (country, city)
- ✅ Organization assessment (company-wide device inventory)
- ✅ Critical infrastructure awareness (ICS/SCADA - report only!)

**Key Takeaways:**
- Shodan = Device search engine (Google ka complement, not replacement)
- Filters = Essential (bina filters ke useless results)
- Paid account ($59/month) = Serious pentesting ke liye zaroori
- Ethical boundaries = ICS systems NEVER access, screenshots carefully
- "Look, Don't Touch" = Hamesha yaad rakho!

**Next Steps:**
- Module 7: GitHub & Data Leak Dorking (code leaks, API keys)
- Module 8: Advanced Recon Techniques (Wayback Machine, metadata)
- Module 9: OSINT Ethics & Legal Boundaries (staying safe)

**Practice Reminder:** 
Shodan par 20-30 searches practice karo:
- Basic filters se start karo
- Advanced filters add karo
- Real companies par try karo (ethical scope mein)
- Evidence collection practice karo (screenshots, notes)

**Ethical Reminder:**
Shodan bahut powerful hai - misuse mat karo:
- Search = Legal
- Access = Illegal (without permission)
- ICS systems = NEVER touch
- Report vulnerabilities responsibly

**Shodan Resources:**
- Shodan.io - Main website
- Shodan CLI - Command line tool
- Shodan API - Automation
- Shodan Book - "Complete Guide to Shodan" by John Matherly

Aap ab Shodan expert ho! Next module mein GitHub dorking seekhenge - code leaks aur API keys hunting! 🚀

---
=============================================================

# **Google Dork And Search Engine Dorking: Zero-to-Hacker Notes** 🚀

---

# **Module 7: GitHub & Data Leak Dorking**

---

## **Topic 1: Intro to GitHub Dorking (Why it's Dangerous)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**GitHub Dorking** - Code repositories mein accidentally leaked credentials, API keys, aur secrets dhoondhna.

### 2. **Ye Kya Hai? (What is it?)**

**GitHub Dorking** ek technique hai jismein aap GitHub ke search operators use karke accidentally committed sensitive data dhoondhte ho - passwords, API keys, AWS credentials, private keys, database configs. Developers galti se yeh secrets code mein commit kar dete hain aur public repositories par push kar dete hain.

**Analogy:** Socho GitHub ek public library hai jahan developers apni notebooks (code) rakhte hain. Kuch developers galti se notebook mein apna ATM PIN likh dete hain aur bhool jaate hain - aap woh notebooks dhoondh rahe ho! 📓

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Credential Leaks:** Plain text passwords, API keys jo direct access dete hain.
- **Supply Chain Attacks:** Ek leaked key se poora infrastructure compromise.
- **Common Mistake:** Developers daily basis par secrets commit karte hain (human error).
- **High Impact:** Ek AWS key se millions ka damage ho sakta hai.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Credential Hunting:** Target company ke leaked credentials dhoondhne ke liye.
- **API Key Discovery:** Third-party service keys (AWS, Stripe, SendGrid).
- **Supply Chain Research:** Dependencies mein leaked secrets.
- **Bug Bounty:** High-severity findings (leaked credentials = critical).

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Easy Wins Lost:** GitHub par daily basis par credentials leak hote hain - miss kar doge.
- **Supply Chain Blindness:** Code dependencies mein chhupe secrets undetected.
- **Incomplete Recon:** Google/Shodan se sirf 50% coverage - GitHub essential hai.

### 6. **Syntax aur Common Options**

**GitHub Search Operators:**
```
filename:.env                      # .env files
extension:pem                      # PEM files (certificates, keys)
path:.git/config                   # Git config files
"API_KEY"                          # Exact phrase
user:username                      # Specific user
org:organization                   # Organization repos
```

**GitHub Search URL:**
```
https://github.com/search?q=YOUR_QUERY&type=code
```

**Common Leak Patterns:**
```
"password"
"api_key"
"secret_key"
"private_key"
"BEGIN RSA PRIVATE KEY"
"AWS_ACCESS_KEY_ID"
"DB_PASSWORD"
```

### 7. **Example 1 (Basic)**

**Scenario:** .env files mein leaked credentials dhoondhne hain.

**Step-by-Step:**

**Step 1:** GitHub.com par jao

**Step 2:** Search box mein:
```
filename:.env DB_PASSWORD
```

**Step 3:** Results:
- Thousands of .env files
- Most mein database passwords

**Output:** Exposed database credentials - but mostly from tutorials/demos! 🎯

**Problem:** Too many false positives (test repos, tutorials).

**Better Approach:**
```
filename:.env DB_PASSWORD -tutorial -example -demo
```
**Output:** Real production .env files (filtered)!

### 8. **Example 2 (Pentester-Focused)**

**Scenario:** "TechCorp" company ke leaked AWS credentials dhoondhne hain.

**Step-by-Step:**

**Step 1:** Company ke GitHub organization nikalo:
```
Visit: github.com/techcorp
```

**Step 2:** Organization-specific search:
```
org:techcorp AWS_ACCESS_KEY_ID
```

**Step 3:** Results analyze:
- 5 repositories mein AWS keys
- 3 public repos, 2 recently made public

**Step 4:** Key validation:
```
⚠️ ETHICAL BOUNDARY:
- Keys dekho (screenshot lo)
- Validate MAT karo (AWS console mein login mat karo)
- Immediately report karo
```

**Step 5:** Evidence collection:
```
Finding: 5 AWS access keys exposed in public repos
Severity: Critical
Risk: Full AWS account compromise, data breach, financial loss

Evidence:
- Repo: techcorp/backend-api
  File: config/aws.js
  Line: 12
  Key: AKIA... (partial, for proof)
  Committed: 2023-05-15
  
- Repo: techcorp/mobile-app
  File: .env
  Line: 8
  Key: AKIA...
  Committed: 2023-08-20

[... 3 more]

Recommendation:
1. Revoke all exposed keys immediately
2. Rotate credentials
3. Audit all public repos
4. Implement pre-commit hooks (git-secrets)
5. Train developers on secret management
```

**Output:** Critical vulnerability report with evidence! 💣

**Real Example - SSH Private Keys:**
```
extension:pem "BEGIN RSA PRIVATE KEY"
```

**Analysis:**
- PEM files = Certificates/Private keys
- "BEGIN RSA PRIVATE KEY" = SSH private key marker

**Output:** Exposed SSH private keys - direct server access! 🔑

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Key Validation:** Leaked key mili toh test karne ki koshish - ILLEGAL! Sirf report karo.
- **No Filtering:** Generic search - millions of tutorial/demo repos.
- **Ignoring History:** Sirf current files dekhe, git history ignore kiya - deleted secrets bhi accessible hain!

### 10. **Best Practices / Pro Tips**

- **High-Value Searches:**
  ```
  filename:.env "AWS_SECRET_ACCESS_KEY"
  filename:.env "STRIPE_SECRET_KEY"
  extension:pem private
  filename:id_rsa
  path:.git/config password
  "BEGIN RSA PRIVATE KEY"
  "BEGIN OPENSSH PRIVATE KEY"
  ```

- **Organization Targeting:**
  ```
  org:target-company filename:.env
  org:target-company extension:pem
  org:target-company "password"
  ```

- **Exclude False Positives:**
  ```
  -tutorial -example -demo -test -sample
  ```

- **Recent Commits:**
  GitHub search mein "Recently indexed" sort karo - fresh leaks!

- **Git History Mining:**
  Tools: TruffleHog, GitLeaks, Gitleaks
  Yeh tools git history scan karte hain - deleted secrets bhi milte hain!

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

**Uber Data Breach (2016) - GitHub Leak**

**Background:** Uber ka massive data breach hua jismein 57 million users ka data leak hua.

**How it happened:**

**Step 1:** Attackers ne GitHub par Uber ke repos search kiye:
```
org:uber AWS_ACCESS_KEY_ID
```

**Step 2:** Ek private repo accidentally public ho gayi thi (developer mistake)

**Step 3:** Repo mein AWS credentials the:
```
File: config/production.yml
AWS_ACCESS_KEY_ID: AKIA...
AWS_SECRET_ACCESS_KEY: ...
```

**Step 4:** Attackers ne credentials use kiye:
- AWS S3 bucket access kiya
- 57 million user records download kiye
- Uber ko ransom demand kiya

**Impact:**
- $148 million fine (regulatory)
- CEO resignation
- Reputation damage
- Criminal charges

**Lesson:** Ek GitHub leak ne company ko almost destroy kar diya! 💰

**Another Example - Cryptocurrency Theft:**

Ek researcher routine GitHub dorking kar raha tha:

```
filename:.env "PRIVATE_KEY" ethereum
```

**Results:** 100+ Ethereum private keys exposed!

**Investigation:**
- Keys validate kiye (read-only check - balance dekha, transfer nahi kiya)
- Total value: $2 million+ in various wallets
- Most keys already drained (attackers ne pehle hi exploit kiya)

**Action:**
- Remaining wallet owners ko contact kiya
- Funds safe wallets mein transfer karne help ki
- Blog post likha (awareness)

**Saved:** $500,000 worth of cryptocurrency

**GitHub dorking ne financial theft rok diya!** 💰

### 12. **Checklist / Chota Recap (TL;DR)**

✅ GitHub dorking = Code repos mein leaked credentials dhoondhna  
✅ Common leaks = AWS keys, API keys, passwords, SSH keys  
✅ Organization-specific search for targeted hunting  
✅ Exclude false positives (-tutorial -example)  
✅ NEVER validate keys - report immediately  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kya leaked key ko test karna legal hai?**  
**A:** Nahi! Key dekh sakte ho (screenshot), lekin use nahi kar sakte (even read-only). Unauthorized access hai - report karo immediately.

**Q2: Kya deleted commits mein secrets safe hain?**  
**A:** Nahi! Git history mein sab kuch permanent hai. Tools (TruffleHog) deleted commits scan karte hain. Secret commit hua = assume compromised.

**Q3: Company ko kaise report karein?**  
**A:** 
1. Security email (security@company.com)
2. Bug bounty platform (HackerOne, Bugcrowd)
3. GitHub Security Advisory (private disclosure)
4. NEVER public tweet/blog without permission

### 14. **Practice ke liye Task**

**Task:** GitHub dorking practice (ETHICAL ONLY):

**Exercise 1 - Generic Search:**
```
filename:.env "DB_PASSWORD" -tutorial
```
**Kya Karna Hai:**
1. Results count note karo
2. Pehle 5 repos dekho (real vs tutorial)
3. Samjho ki filtering kyun zaroori hai
4. **DO NOT open any .env files!**

**Exercise 2 - SSH Key Search:**
```
extension:pem "BEGIN RSA PRIVATE KEY"
```
**Kya Karna Hai:**
1. Kitne private keys exposed hain
2. File names dekho (id_rsa, server.pem, etc.)
3. Samjho ki yeh exposure kyun critical hai
4. **DO NOT download or use any keys!**

**Exercise 3 - Organization Search (Use a public company):**
```
org:microsoft filename:.env
```
**Kya Karna Hai:**
1. Microsoft ke public repos mein .env files
2. Most are examples/tutorials (expected)
3. Samjho ki large companies bhi vulnerable ho sakte hain

**Exercise 4 - API Key Patterns:**
```
"STRIPE_SECRET_KEY" -example
```
**Kya Karna Hai:**
1. Stripe API keys kitne exposed hain
2. Real vs test keys identify karo (test keys "sk_test_" se start hote hain)
3. Samjho ki API key leaks ka impact

**Expected Learning:** GitHub leak patterns aur ethical boundaries.

### 15. **Aakhri Choti Summary (5 lines)**

- 🔑 GitHub dorking = Code repos mein leaked credentials (AWS, API keys, passwords)
- 🎯 Organization-specific search for targeted hunting
- 🚨 Common leaks = .env files, PEM files, git configs
- ⚠️ NEVER validate/use leaked keys - immediate report
- 💰 High impact - ek key se millions ka damage (Uber example)

> **📌 Ye Zaroor Yaad Rakhein:**  
> "GitHub duniya ka sabse bada 'accidental leak' source hai - developers daily basis par secrets commit karte hain. Ek leaked AWS key se poora infrastructure compromise. 'Look, Report, Don't Touch'!" 🔐

---

## **Topic 2: Dorking for Keys & Passwords**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**GitHub Key Hunting** - Specific patterns use karke API keys, passwords, aur credentials systematically dhoondhna.

### 2. **Ye Kya Hai? (What is it?)**

GitHub key hunting ek systematic approach hai jismein aap specific file types, keywords, aur patterns combine karke high-value credentials dhoondhte ho. Har service (AWS, Stripe, SendGrid) ke keys ka unique pattern hota hai.

**Analogy:** Socho aap treasure hunt kar rahe ho. Generic search "somewhere gold hai" hai. Key hunting "X marks the spot - dig here" hai - specific patterns follow karo! 🗺️

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Pattern Recognition:** Har service ke keys ka unique format - patterns se false positives kam.
- **Systematic Approach:** Random search ki jagah, methodical hunting.
- **High Success Rate:** Specific patterns = relevant results.
- **Service-Specific:** AWS, Stripe, GitHub, SendGrid - har ek alag pattern.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Service-Specific Hunting:** AWS keys specifically chahiye.
- **Bug Bounty:** Target company ki specific services (Stripe for payment, AWS for infra).
- **Supply Chain:** Dependencies mein third-party keys.
- **Systematic Recon:** Har major service ke keys check karo.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Random Searching:** Generic "password" search - 99% false positives.
- **Service Blindness:** AWS keys dhoondhne hain lekin pattern nahi pata - miss ho jaayenge.
- **Time Waste:** Irrelevant results filter karne mein hours.

### 6. **Syntax aur Common Options**

**AWS Keys Pattern:**
```
Access Key: AKIA[A-Z0-9]{16}
Secret Key: [A-Za-z0-9/+=]{40}

GitHub Search:
"AKIA" filename:.env
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
```

**Stripe Keys Pattern:**
```
Secret Key: sk_live_[A-Za-z0-9]{24}
Publishable: pk_live_[A-Za-z0-9]{24}

GitHub Search:
"sk_live_" -example
STRIPE_SECRET_KEY
```

**GitHub Personal Access Tokens:**
```
Pattern: ghp_[A-Za-z0-9]{36}

GitHub Search:
"ghp_"
GITHUB_TOKEN
```

**SSH Private Keys:**
```
Pattern: -----BEGIN RSA PRIVATE KEY-----

GitHub Search:
"BEGIN RSA PRIVATE KEY"
"BEGIN OPENSSH PRIVATE KEY"
filename:id_rsa
extension:pem private
```

**Database Passwords:**
```
Keywords:
DB_PASSWORD
DATABASE_PASSWORD
MYSQL_PASSWORD
POSTGRES_PASSWORD

GitHub Search:
filename:.env "DB_PASSWORD"
path:config "database" "password"
```

### 7. **Example 1 (Basic)**

**Scenario:** AWS keys systematically dhoondhne hain.

**Step-by-Step:**

**Step 1:** AWS Access Key pattern search:
```
"AKIA" filename:.env
```

**Step 2:** Results filter:
- 10,000+ results
- Most are examples/tutorials

**Step 3:** Add exclusions:
```
"AKIA" filename:.env -example -tutorial -demo -test
```

**Step 4:** Results:
- 500 results (filtered)
- Higher chance of real keys

**Step 5:** Verify pattern:
```
Click on result → Check if format matches:
AKIAIOSFODNN7EXAMPLE (example key)
AKIAJ... (real key pattern)
```

**Output:** Filtered AWS keys - higher quality results! 🎯

### 8. **Example 2 (Pentester-Focused)**

**Scenario:** "FinTech Startup" ke Stripe keys dhoondhne hain (payment processing).

**Step-by-Step:**

**Step 1:** Organization identify:
```
github.com/fintech-startup
```

**Step 2:** Stripe secret key search:
```
org:fintech-startup "sk_live_"
```

**Step 3:** Results:
- 2 repositories mein Stripe keys
- Both in .env files

**Step 4:** Evidence collection:
```
Repo 1: fintech-startup/payment-api
File: .env.production
Line: 15
Key: sk_live_51H... (partial)
Committed: 2023-06-10
Commit message: "Update production config"

Repo 2: fintech-startup/mobile-backend
File: config/stripe.js
Line: 8
Key: sk_live_51J... (partial)
Committed: 2023-09-15
Commit message: "Fix stripe integration"
```

**Step 5:** Impact assessment:
```
Finding: 2 Stripe live secret keys exposed
Severity: Critical

Risk:
- Full payment processing access
- Can create charges, refunds
- Access customer payment data
- Financial fraud potential
- PCI-DSS compliance violation

Financial Impact:
- Unauthorized charges
- Refund fraud
- Customer data breach
- Regulatory fines (PCI-DSS)
```

**Step 6:** Report:
```
Subject: Critical - Stripe Live Keys Exposed in Public Repos

Details:
[Evidence screenshots]
[Repo links]
[Commit hashes]

Immediate Actions Required:
1. Revoke exposed keys (Stripe dashboard)
2. Generate new keys
3. Audit all transactions since exposure date
4. Remove keys from git history (BFG Repo-Cleaner)
5. Implement secret management (AWS Secrets Manager)
```

**Output:** High-severity finding with clear impact! 💣

**Real Example - GitHub Token Leak:**

**Step 1:** Search:
```
"ghp_" -example
```

**Step 2:** Results:
- 1,000+ GitHub personal access tokens

**Step 3:** Token analysis:
```
ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
(36 characters after ghp_)
```

**Step 4:** Scope check:
```
⚠️ ETHICAL: DO NOT use token!
Token scopes can include:
- repo (full repo access)
- admin:org (organization control)
- delete_repo (can delete repos)
```

**Step 5:** Impact:
```
One leaked token = Full GitHub account compromise
- Source code theft
- Malicious commits
- Repository deletion
- Supply chain attacks
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Pattern Ignorance:** "password" search kiya - specific patterns nahi use kiye.
- **Test vs Live Confusion:** Stripe test keys (`sk_test_`) ko report kiya - yeh intentionally public hote hain.
- **Token Usage:** GitHub token mila toh "verify" karne ki koshish - ILLEGAL!

### 10. **Best Practices / Pro Tips**

- **Service-Specific Patterns:**

**AWS:**
```
"AKIA" extension:env
AWS_ACCESS_KEY_ID extension:yml
AWS_SECRET_ACCESS_KEY path:config
```

**Stripe:**
```
"sk_live_" -example -test
STRIPE_SECRET_KEY filename:.env
"pk_live_" (publishable key - less sensitive but still report)
```

**SendGrid:**
```
"SG." extension:env
SENDGRID_API_KEY
```

**Twilio:**
```
"SK" "AC" extension:env
TWILIO_AUTH_TOKEN
```

**Google API:**
```
"AIza" extension:json
GOOGLE_API_KEY
```

**SSH Keys:**
```
"BEGIN RSA PRIVATE KEY" extension:pem
"BEGIN OPENSSH PRIVATE KEY"
filename:id_rsa -pub
```

- **Test vs Live Keys:**
  - Stripe: `sk_test_` = Test (OK), `sk_live_` = Live (REPORT!)
  - AWS: All AKIA keys are real (no test pattern)
  - GitHub: All ghp_ tokens are real

- **Git History Mining:**
  ```bash
  # TruffleHog tool
  trufflehog git https://github.com/target/repo --json
  
  # GitLeaks tool
  gitleaks detect --source /path/to/repo
  ```

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

**Toyota Data Breach (2022) - GitHub Leak**

**Background:** Toyota ke 300,000 customers ka data exposed hua.

**How it happened:**

**Step 1:** Subcontractor developer ne accidentally AWS keys commit kiye:
```
File: config/aws.yml
AWS_ACCESS_KEY_ID: AKIA...
AWS_SECRET_ACCESS_KEY: ...
```

**Step 2:** Repo public thi (5 years se!)

**Step 3:** Attacker ne keys discover kiye:
```
org:subcontractor-name "AKIA"
```

**Step 4:** Keys use karke:
- S3 bucket access kiya
- Customer data download kiya
- 300,000 records leaked

**Impact:**
- Public apology
- Regulatory investigation
- Subcontractor contract terminated
- Security overhaul

**Lesson:** Subcontractor ki ek mistake ne Toyota ko affect kiya - supply chain risk! 🚗

**Another Example - Cryptocurrency Wallet Leak:**

Ek researcher ne yeh search kiya:
```
"BEGIN OPENSSH PRIVATE KEY" filename:wallet
```

**Results:** 50+ cryptocurrency wallet private keys!

**Investigation:**
- Keys se wallet addresses derive kiye (offline, no blockchain access)
- Blockchain explorer se balances check kiye (public data)
- Total: $5 million+ in various wallets
- Most already drained (bots monitor GitHub 24/7)

**Action:**
- Remaining wallet owners ko contact kiya (GitHub profiles se)
- 5 owners respond kiye
- Funds safe wallets mein transfer help ki
- Saved: $200,000

**Lesson:** Bots GitHub ko 24/7 monitor karte hain - leak hote hi exploit! ⚡

### 12. **Checklist / Chota Recap (TL;DR)**

✅ Pattern-based search = High-quality results (AWS: AKIA, Stripe: sk_live_)  
✅ Service-specific hunting = Systematic approach  
✅ Test vs Live keys = Stripe test keys ignore, live keys report  
✅ Git history = Deleted secrets bhi accessible (TruffleHog)  
✅ NEVER use/validate keys = Immediate report  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Test keys ko report karna chahiye?**  
**A:** Nahi. Stripe test keys (`sk_test_`), sandbox credentials intentionally public hote hain. Sirf live/production keys report karo.

**Q2: Kya bots sach mein GitHub monitor karte hain?**  
**A:** Haan! Research shows: AWS key commit hone ke 1 minute mein bots detect kar lete hain. Cryptocurrency keys seconds mein drain ho jaate hain.

**Q3: Git history se secrets kaise remove karein?**  
**A:** Tools:
- BFG Repo-Cleaner (fast)
- git filter-branch (manual)
- GitHub's "Remove sensitive data" guide
Lekin yaad rakho: Once committed = assume compromised. Revoke karo!

### 14. **Practice ke liye Task**

**Task:** Pattern-based hunting practice:

**Exercise 1 - AWS Keys:**
```
"AKIA" filename:.env -example -tutorial
```
**Kya Karna Hai:**
1. Results count note karo
2. Pehle 5 results ke patterns verify karo
3. Real vs example keys identify karo
4. **DO NOT copy or use any keys!**

**Exercise 2 - Stripe Keys:**
```
"sk_live_" -example
```
**Kya Karna Hai:**
1. Live Stripe keys kitne exposed hain
2. Compare karo: `sk_live_` vs `sk_test_` results
3. Samjho ki live keys kyun critical hain

**Exercise 3 - SSH Keys:**
```
"BEGIN RSA PRIVATE KEY" extension:pem
```
**Kya Karna Hai:**
1. Private keys kitne exposed hain
2. File names dekho (id_rsa, server.pem, etc.)
3. Samjho ki SSH key leak ka impact

**Exercise 4 - GitHub Tokens:**
```
"ghp_" -example
```
**Kya Karna Hai:**
1. GitHub tokens kitne exposed hain
2. Token format verify karo (ghp_ + 36 chars)
3. Samjho ki token leak se kya ho sakta hai

**Expected Learning:** Service-specific patterns aur systematic hunting.

### 15. **Aakhri Choti Summary (5 lines)**

- 🔑 Pattern-based search = Service-specific keys (AWS: AKIA, Stripe: sk_live_)
- 🎯 Systematic approach = Har major service ke patterns yaad rakho
- ⚡ Bots monitor GitHub 24/7 = Leak hote hi exploit (minutes mein)
- 🧪 Test vs Live = Test keys ignore, live keys critical
- 🚨 Git history = Deleted secrets bhi accessible (assume compromised)

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Har service ke keys ka unique 'fingerprint' hai - AWS ka AKIA, Stripe ka sk_live_, GitHub ka ghp_. Patterns yaad rakho, systematic hunting karo. Bots tumse fast hain - leak = instant compromise!" ⚡

---


## **Topic 3: Pastebin & Public Leaks (Monitoring for Data Dumps)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Pastebin Dorking** - Public paste sites par leaked credentials, database dumps, aur data breaches monitor karo.

### 2. **Ye Kya Hai? (What is it?)**

**Pastebin** aur similar sites (Ghostbin, Hastebin, Privatebin) text sharing platforms hain jahan log code snippets, logs, ya notes share karte hain. Attackers often stolen data yahan dump karte hain - database dumps, credential lists, API keys. OSINT mein yeh sites monitor karna zaroori hai kyunki yahan real-time data leaks hote hain.

**Analogy:** Socho Pastebin ek public notice board hai jahan koi bhi kuch bhi paste kar sakta hai. Hackers yahan "stolen goods" display karte hain - aap woh notice board monitor kar rahe ho! 📋

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Real-Time Leaks:** Data breaches hone ke turant baad yahan dump hote hain.
- **Credential Lists:** Hacked databases ke username/password lists.
- **Proof of Breach:** Attackers yahan proof post karte hain (ransom demands).
- **Early Warning:** Company ko pata chalne se pehle aap detect kar sakte ho.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Breach Monitoring:** Company ke data leaks monitor karne ke liye.
- **Credential Hunting:** Target company ke leaked credentials.
- **Threat Intelligence:** Ongoing attacks aur breach campaigns track karna.
- **Dark Web Alternative:** Pastebin "poor man's dark web" hai - public leaks.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Missed Breaches:** Company breach ho gayi lekin pata nahi chala (Pastebin par dump tha).
- **Late Response:** Attackers ne data public kiya, aap late discover kiye - damage ho chuka.
- **Incomplete Monitoring:** GitHub + Shodan se sirf 70% - Pastebin essential hai.

### 6. **Syntax aur Common Options**

**Google Dorking for Pastebin:**
```
site:pastebin.com "company-name"
site:pastebin.com "company.com" password
site:pastebin.com "database dump"
site:pastebin.com "SQL dump" "INSERT INTO"
```

**Other Paste Sites:**
```
site:ghostbin.com
site:hastebin.com
site:privatebin.net
site:justpaste.it
site:paste.ee
```

**Common Leak Indicators:**
```
"database dump"
"SQL dump"
"hacked by"
"leaked credentials"
"password list"
"email:pass"
"username:password"
```

**Pastebin Search (Direct):**
```
https://pastebin.com/search?q=YOUR_QUERY
```

### 7. **Example 1 (Basic)**

**Scenario:** "TechCorp" company ke Pastebin leaks dhoondhne hain.

**Step-by-Step:**

**Step 1:** Google dorking:
```
site:pastebin.com "techcorp.com"
```

**Step 2:** Results:
- 50+ pastes mentioning techcorp.com
- Most are code snippets, logs

**Step 3:** Filter for sensitive content:
```
site:pastebin.com "techcorp.com" (password OR credentials OR dump)
```

**Step 4:** Results:
- 5 pastes with potential leaks
- Need manual verification

**Output:** Potential leak candidates for investigation! 🎯

### 8. **Example 2 (Pentester-Focused)**

**Scenario:** Recent database dump dhoondhni hai (any company).

**Step-by-Step:**

**Step 1:** Google search:
```
site:pastebin.com "database dump" "INSERT INTO users"
```

**Step 2:** Results:
- 100+ database dumps
- Various companies

**Step 3:** Recent dumps filter:
```
Google Tools → Past 24 hours
```

**Step 4:** Manual verification:
```
Click on paste → Check content:
- Table structure (CREATE TABLE)
- Data rows (INSERT INTO)
- Sensitive fields (email, password, phone)
```

**Step 5:** Evidence collection:
```
Finding: Database dump on Pastebin
Posted: 2024-01-15 10:30 AM
URL: pastebin.com/XXXXXXXX
Database: users_production
Records: ~50,000 rows

Sample data (anonymized):
email: user@company.com
password: $2y$10$... (bcrypt hash)
phone: +1-555-...
created_at: 2023-12-01

Affected Company: [Identified from email domains]
Severity: Critical
```

**Step 6:** Responsible disclosure:
```
⚠️ ETHICAL ACTIONS:
1. Screenshot paste (evidence)
2. DO NOT download full dump
3. Identify affected company (email domains)
4. Report to company security team
5. Report to Pastebin (DMCA takedown)
6. DO NOT share paste URL publicly
```

**Output:** Critical breach discovery with ethical handling! 💣

**Real Example - Credential List:**

**Step 1:** Search:
```
site:pastebin.com "email:pass" "gmail.com"
```

**Step 2:** Results:
- Credential lists (email:password format)
- Combo lists (for credential stuffing)

**Step 3:** Sample paste:
```
user1@gmail.com:password123
user2@yahoo.com:qwerty456
admin@company.com:Admin@2023
...
```

**Step 4:** Impact:
```
- Credential stuffing attacks
- Account takeovers
- Identity theft
- Corporate account compromise
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Downloading Dumps:** Full database dump download kiya - ILLEGAL! Sirf sample dekho.
- **Public Sharing:** Paste URL social media par share kiya - yeh leak ko amplify karta hai.
- **No Reporting:** Leak dekhi aur ignore kiya - ethical responsibility hai report karna.

### 10. **Best Practices / Pro Tips**

- **Monitoring Dorks:**
  ```
  site:pastebin.com "company-name" (password OR credentials OR api OR key)
  site:pastebin.com "@company.com" (dump OR leak OR hacked)
  site:pastebin.com "company database"
  ```

- **Multiple Paste Sites:**
  ```
  (site:pastebin.com OR site:ghostbin.com OR site:hastebin.com) "target-company"
  ```

- **Time-Based Monitoring:**
  - Google Tools → Past 24 hours
  - Daily monitoring for high-value targets
  - Set up Google Alerts for automated monitoring

- **Automated Tools:**
  - **PasteHunter** - Monitors paste sites, alerts on keywords
  - **Dumpmon** - Real-time paste monitoring
  - **OSINT Framework** - Aggregates paste site searches

- **Ethical Handling:**
  1. Screenshot only (evidence)
  2. DO NOT download full data
  3. Report to affected company
  4. Report to paste site (takedown)
  5. DO NOT publicize until company responds

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

**LinkedIn Data Breach (2021) - Pastebin Discovery**

**Background:** 700 million LinkedIn users ka data scraped aur leaked hua.

**Discovery:**

**Step 1:** Security researcher routine Pastebin monitoring kar raha tha:
```
site:pastebin.com "linkedin" "database"
```

**Step 2:** Ek paste mila:
```
Title: "LinkedIn 700M Users - Sample"
Content: 
- 1 million user records (sample)
- Full name, email, phone, location
- Professional details
```

**Step 3:** Verification:
- Random emails check kiye (public LinkedIn profiles se)
- Data accurate tha
- Full dump dark web par sale ke liye

**Step 4:** Disclosure:
- LinkedIn ko immediately notify kiya
- Paste URL provided
- Full dump details shared

**Impact:**
- LinkedIn ne investigation start ki
- Pastebin paste removed
- Public advisory issued
- Users ko password change advisory

**Lesson:** Pastebin monitoring ne major breach early detect kiya! 🔍

**Another Example - API Key Leak:**

Ek developer accidentally production API keys Pastebin par paste kar gaya (debugging ke liye):

**Step 1:** Automated bot ne detect kiya:
```
site:pastebin.com "API_KEY" "sk_live_"
```

**Step 2:** Paste content:
```
# Debug config
STRIPE_SECRET_KEY=sk_live_51H...
AWS_ACCESS_KEY_ID=AKIA...
DATABASE_URL=postgres://user:pass@...
```

**Step 3:** Timeline:
- Posted: 10:00 AM
- Bot detected: 10:02 AM (2 minutes!)
- Company notified: 10:05 AM
- Keys revoked: 10:15 AM

**Step 4:** Damage control:
- Keys revoked before exploitation
- No unauthorized transactions
- Developer trained on security

**Lesson:** Pastebin leaks instant hote hain - monitoring critical! ⚡

### 12. **Checklist / Chota Recap (TL;DR)**

✅ Pastebin = Public paste sites (real-time leak dumps)  
✅ Monitor karo: company name, domain, "database dump"  
✅ Multiple sites check karo (Pastebin, Ghostbin, Hastebin)  
✅ Automated monitoring tools use karo (PasteHunter)  
✅ Ethical handling: Screenshot, report, DON'T download  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kya Pastebin monitoring legal hai?**  
**A:** Haan, Pastebin public hai. Monitoring legal hai, lekin data download/use illegal (without permission).

**Q2: Kitni baar monitor karna chahiye?**  
**A:** High-value targets: Daily. Medium targets: Weekly. Automated tools 24/7 monitor karte hain.

**Q3: Paste mila toh kya karein?**  
**A:** 
1. Screenshot lo (evidence)
2. Affected company ko report karo
3. Pastebin ko report karo (DMCA)
4. DO NOT download data
5. DO NOT share publicly

### 14. **Practice ke liye Task**

**Task:** Pastebin monitoring practice (ETHICAL ONLY):

**Exercise 1 - Company Monitoring:**
```
site:pastebin.com "microsoft.com"
```
**Kya Karna Hai:**
1. Results count note karo
2. Types of pastes dekho (code, logs, etc.)
3. Samjho ki monitoring kyun important hai
4. **DO NOT open suspicious pastes!**

**Exercise 2 - Database Dump Search:**
```
site:pastebin.com "database dump" "INSERT INTO"
```
**Kya Karna Hai:**
1. Kitne database dumps public hain
2. Paste titles dekho (company names visible?)
3. Samjho ki yeh exposure kyun critical hai
4. **DO NOT download any dumps!**

**Exercise 3 - Credential Lists:**
```
site:pastebin.com "email:pass" -tutorial
```
**Kya Karna Hai:**
1. Credential lists kitne common hain
2. Format dekho (email:password)
3. Samjho ki credential stuffing attacks kaise hote hain
4. **DO NOT use any credentials!**

**Exercise 4 - Multi-Site Search:**
```
(site:pastebin.com OR site:ghostbin.com) "API_KEY"
```
**Kya Karna Hai:**
1. Multiple paste sites compare karo
2. API key leaks kitne hain
3. Samjho ki multi-site monitoring kyun zaroori hai

**Expected Learning:** Paste site monitoring aur ethical data handling.

### 15. **Aakhri Choti Summary (5 lines)**

- 📋 Pastebin = Public paste sites (real-time breach dumps)
- 🔍 Monitor karo: company name, database dumps, credentials
- ⚡ Automated tools (PasteHunter) for 24/7 monitoring
- 🚨 Ethical handling: Screenshot only, report immediately
- ⏰ Time-critical: Leaks minutes mein exploit hote hain

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Pastebin 'poor man's dark web' hai - attackers yahan stolen data dump karte hain. Daily monitoring zaroori hai, lekin ethical boundaries critical hain. 'Monitor, Report, Don't Touch'!" 📡

---

# **🎓 Module 7 Complete! Congratulations!**

Aapne **GitHub & Data Leak Dorking** master kar liye! Ab aap:
- ✅ GitHub dorking kar sakte ho (leaked credentials, API keys)
- ✅ Service-specific patterns jaante ho (AWS: AKIA, Stripe: sk_live_)
- ✅ Pastebin aur paste sites monitor kar sakte ho
- ✅ Ethical boundaries samajhte ho (look, report, don't touch)

**Module 7 Mastery Checklist:**
- ✅ GitHub organization-specific searches
- ✅ Pattern-based key hunting (AWS, Stripe, GitHub tokens)
- ✅ Git history awareness (deleted secrets bhi accessible)
- ✅ Pastebin monitoring (real-time breach detection)
- ✅ Responsible disclosure process

**Key Takeaways:**
- GitHub = Duniya ka sabse bada accidental leak source
- Patterns = Har service ke keys ka unique fingerprint
- Bots = GitHub/Pastebin ko 24/7 monitor karte hain (minutes mein exploit)
- Test vs Live = Stripe test keys OK, live keys critical
- Ethical = NEVER validate/use keys - immediate report

**Real-World Impact:**
- Uber breach: $148M fine (GitHub leak)
- Toyota breach: 300K customers (subcontractor GitHub leak)
- LinkedIn breach: 700M users (Pastebin discovery)
- Cryptocurrency: $5M+ in exposed wallets (GitHub)

**Next Steps:**
- Module 8: Advanced Recon Techniques (Wayback Machine, metadata, Censys)
- Module 9: OSINT Ethics & Legal Boundaries (staying safe, responsible disclosure)

**Practice Reminder:**
GitHub aur Pastebin par daily monitoring practice karo:
- Apni company monitor karo (permission ke saath)
- Public companies par practice karo (ethical scope mein)
- Automated tools setup karo (PasteHunter, Google Alerts)
- Evidence collection practice karo (screenshots, documentation)

**Ethical Reminder - CRITICAL:**
Module 7 sabse sensitive hai - misuse mat karo:
- Keys dekho = Legal
- Keys use karo = ILLEGAL (even read-only)
- Data download karo = ILLEGAL
- Public share karo = Unethical (leak amplify)
- Report karo = Ethical responsibility

**Responsible Disclosure Process:**
1. **Discover:** Leak/key dhoondho
2. **Document:** Screenshot, URL, timestamp
3. **Report:** Company security team ko private email
4. **Wait:** Company ko fix karne ka time do (30-90 days)
5. **Follow-up:** Agar response nahi toh escalate (CERT, bug bounty platform)
6. **Disclose:** Company permission ke baad hi public karo

**Tools Mentioned:**
- **GitHub:** github.com/search
- **TruffleHog:** Git history scanner
- **GitLeaks:** Secret detection tool
- **PasteHunter:** Paste site monitor
- **Dumpmon:** Real-time paste monitoring
- **BFG Repo-Cleaner:** Git history cleanup

**Resources:**
- GitHub Security Advisories: github.com/advisories
- HaveIBeenPwned: haveibeenpwned.com (breach database)
- Pastebin Alerts: pastebin.com/alerts
- OSINT Framework: osintframework.com

Aap ab GitHub aur Pastebin expert ho! Next module mein advanced recon techniques seekhenge - Wayback Machine, metadata analysis, aur alternative search engines! 🚀

**Final Warning:**
GitHub aur Pastebin par daily basis par millions of secrets leak hote hain. Yeh knowledge powerful hai lekin dangerous bhi. Hamesha ethical boundaries yaad rakho:

> **"With great power comes great responsibility. Leaked keys dekho, report karo, use MAT karo. Ek galat decision se jail ho sakti hai!"** ⚖️

---

=============================================================

# **Google Dork And Search Engine Dorking: Zero-to-Hacker Notes** 🚀

---

# **Module 8: Advanced Recon Techniques**

---

## **Topic 1: The Wayback Machine (Time-Travel OSINT)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Wayback Machine** - Websites ke purane versions dekho, deleted content recover karo (archive.org).

### 2. **Ye Kya Hai? (What is it?)**

**Wayback Machine** (archive.org) ek digital archive hai jo 1996 se websites ke snapshots save karta hai. Aap kisi bhi website ka purana version dekh sakte ho - deleted pages, old designs, removed content. Yeh "time machine" hai internet ka!

**Analogy:** Socho har website ki ek photo album hai jismein har saal ki photos hain. Wayback Machine woh album hai - aap 2010 ki photo dekh sakte ho, 2015 ki, 2020 ki! 📸

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Deleted Content Recovery:** Company ne sensitive page delete kiya, lekin archive mein hai.
- **Historical Intelligence:** Company ki evolution, old tech stack, removed features.
- **Evidence Collection:** Proof chahiye ki kab kya exposed tha.
- **Subdomain Discovery:** Old pages mein hidden subdomain links.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Deleted Pages:** Current site par nahi hai lekin pehle tha.
- **Historical Recon:** Company ki past technology, partnerships.
- **Evidence:** Pentest report ke liye proof (kab exposed tha).
- **Subdomain Enumeration:** Old sitemaps, old links.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Lost Evidence:** Deleted sensitive content jo proof ban sakti thi.
- **Incomplete Timeline:** Company ne kab kya change kiya, pata nahi chalega.
- **Missed Intelligence:** Old employee pages, old tech stack - valuable info.

### 6. **Syntax aur Common Options**

**Wayback Machine URL:**
```
https://web.archive.org/web/*/example.com
```

**Specific Date:**
```
https://web.archive.org/web/20200101000000/example.com
(Format: YYYYMMDDHHMMSS)
```

**Google Dorking for Archives:**
```
site:web.archive.org "target.com"
site:web.archive.org "target.com" admin
site:web.archive.org "target.com" login
```

### 7. **Example 1 (Basic)**

**Scenario:** Target website ka 2015 version dekhna hai.

**Step-by-Step:**

**Step 1:** Wayback Machine par jao:
```
https://web.archive.org
```

**Step 2:** URL enter karo:
```
target.com
```

**Step 3:** Calendar view:
- Blue dots = Snapshots available
- Click on year → Month → Date

**Step 4:** 2015 snapshot select karo

**Output:** Website ka 2015 version - old design, old content! 🕰️

### 8. **Example 2 (Pentester-Focused)**

**Scenario:** "TechCorp" ne admin panel delete kiya, lekin archive mein dhoondhna hai.

**Step-by-Step:**

**Step 1:** Current site check:
```
techcorp.com/admin → 404 Not Found
```

**Step 2:** Wayback Machine search:
```
https://web.archive.org/web/*/techcorp.com/admin
```

**Step 3:** Results:
- 2018: Admin panel accessible (snapshot available)
- 2019: Still accessible
- 2020: 404 (deleted)

**Step 4:** 2019 snapshot open karo:
```
https://web.archive.org/web/20190615/techcorp.com/admin
```

**Step 5:** Intelligence gathering:
```
Findings from archived admin page:
- Login form visible (username/password fields)
- Technology: PHP 5.6 (visible in source)
- Framework: Custom CMS
- Error messages: SQL error hints
- Employee names: "Contact admin@techcorp.com"
```

**Step 6:** Evidence collection:
```
Finding: Admin panel existed until 2020
Evidence: Wayback Machine snapshot (2019-06-15)
URL: techcorp.com/admin
Technology: PHP 5.6, Custom CMS
Status: Currently deleted (404)

Intelligence Value:
- Old technology stack identified
- Admin email discovered
- Login mechanism understood
- Potential for similar panels on subdomains
```

**Output:** Historical intelligence + evidence! 🔍

**Real Example - Subdomain Discovery:**

**Step 1:** Old sitemap check:
```
https://web.archive.org/web/*/techcorp.com/sitemap.xml
```

**Step 2:** 2017 sitemap:
```xml
<url>
  <loc>https://admin.techcorp.com</loc>
</url>
<url>
  <loc>https://dev.techcorp.com</loc>
</url>
<url>
  <loc>https://staging-old.techcorp.com</loc>
</url>
```

**Step 3:** Current status check:
- admin.techcorp.com → Still exists!
- dev.techcorp.com → 404
- staging-old.techcorp.com → Still exists! (forgotten)

**Output:** Hidden subdomain discovered via old sitemap! 🎯

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Assuming Complete Archive:** Har page archived nahi hota - robots.txt blocked pages miss.
- **Single Snapshot:** Ek hi snapshot dekha - multiple dates check karo (changes track karne ke liye).
- **Ignoring Source Code:** Page dekha lekin source code nahi - comments, hidden links miss.

### 10. **Best Practices / Pro Tips**

- **Multiple Snapshots:**
  - Har year ka ek snapshot dekho
  - Major changes identify karo
  - Timeline banao

- **Source Code Analysis:**
  - Right-click → View Page Source
  - Comments check karo
  - Hidden links, old APIs

- **Specific Pages:**
  ```
  /admin
  /login
  /api
  /docs
  /sitemap.xml
  /robots.txt
  ```

- **Google Dorking:**
  ```
  site:web.archive.org "target.com" admin
  site:web.archive.org "target.com" api
  site:web.archive.org "target.com" password
  ```

- **Automated Tools:**
  - **waybackurls** - Extract all archived URLs
  - **gau** (Get All URLs) - Aggregate URLs from multiple sources

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

**Capital One Breach (2019) - Wayback Intelligence**

**Background:** Capital One breach investigation mein Wayback Machine use hua.

**Investigation:**

**Step 1:** Attacker profile research:
```
Wayback Machine → Attacker's personal website
```

**Step 2:** Old blog posts:
- 2017: "How I hacked XYZ" (deleted post)
- 2018: AWS security research
- 2019: Post deleted (but archived)

**Step 3:** Archived post analysis:
```
Deleted blog post revealed:
- Attack methodology
- Tools used
- Previous targets
- Motivation
```

**Step 4:** Evidence:
- FBI used archived posts as evidence
- Attacker's own documentation helped prosecution

**Lesson:** Wayback Machine ne attacker ki digital footprint preserve ki! 📚

**Another Example - Bug Bounty:**

Ek researcher "FinTech Startup" assess kar raha tha:

**Step 1:** Wayback Machine:
```
https://web.archive.org/web/*/fintechstartup.com
```

**Step 2:** 2016 snapshot:
```
Old homepage had:
- "API Documentation: api.fintechstartup.com/docs"
- Link now deleted from current site
```

**Step 3:** API docs check:
```
api.fintechstartup.com/docs → Still accessible!
```

**Step 4:** Finding:
```
Old API documentation exposed:
- Internal endpoints
- Authentication methods
- Example requests with test keys
- Rate limiting info

Current Status: Docs removed from main site but endpoint still live!
```

**Step 5:** Report:
```
Finding: Exposed API documentation (forgotten endpoint)
Severity: Medium
Discovery: Wayback Machine historical link

Impact:
- API structure exposed
- Authentication methods revealed
- Potential for API abuse

Recommendation: Remove old API docs endpoint
```

**Bounty:** $1,500

**Wayback Machine ne forgotten endpoint discover kiya! 💰**

### 12. **Checklist / Chota Recap (TL;DR)**

✅ Wayback Machine = Website archive (1996 se snapshots)  
✅ Deleted content recover karo (pages, admin panels)  
✅ Multiple snapshots check karo (timeline banao)  
✅ Source code analyze karo (comments, hidden links)  
✅ Old sitemaps = Subdomain discovery goldmine  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kya har website archived hai?**  
**A:** Nahi. robots.txt se blocked sites, password-protected pages, dynamic content (JavaScript-heavy) miss ho sakte hain.

**Q2: Kitne purane snapshots available hain?**  
**A:** 1996 se! Lekin frequency vary karti hai - popular sites daily, less popular monthly/yearly.

**Q3: Kya archived content legal hai use karna?**  
**A:** Viewing legal hai. Lekin archived credentials/keys use karna illegal hai (even if old).

### 14. **Practice ke liye Task**

**Task:** Wayback Machine exploration:

**Exercise 1 - Historical Analysis:**
```
https://web.archive.org/web/*/github.com
```
**Kya Karna Hai:**
1. GitHub ka 2010 version dekho
2. 2015 version dekho
3. 2020 version dekho
4. Changes note karo (design, features)

**Exercise 2 - Deleted Content:**
```
Pick any company website
Check: /admin, /api, /docs in Wayback Machine
```
**Kya Karna Hai:**
1. Current site par check karo (404?)
2. Wayback Machine mein search karo
3. Agar archived hai toh dekho
4. Intelligence note karo

**Exercise 3 - Subdomain Discovery:**
```
https://web.archive.org/web/*/target.com/sitemap.xml
```
**Kya Karna Hai:**
1. Old sitemap dekho
2. Subdomains list banao
3. Current status check karo
4. Forgotten subdomains identify karo

**Expected Learning:** Historical intelligence gathering.

### 15. **Aakhri Choti Summary (5 lines)**

- 🕰️ Wayback Machine = Internet archive (1996 se snapshots)
- 🔍 Deleted content recover karo (admin panels, old pages)
- 📊 Multiple snapshots = Timeline analysis (kab kya change hua)
- 🗺️ Old sitemaps = Subdomain discovery (forgotten assets)
- 📸 Evidence collection = Proof ki kab kya exposed tha

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Wayback Machine 'time machine' hai - internet par kuch bhi permanently delete nahi hota. Deleted pages, old tech stack, forgotten subdomains - sab archived hai. Historical intelligence ka goldmine!" ⏰

---

## **Topic 2: Human OSINT (LinkedIn, Job Postings for Tech Stack Info)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Human OSINT** - Employees, job postings, aur social media se target ki technology stack aur internal info nikalo.

### 2. **Ye Kya Hai? (What is it?)**

**Human OSINT** ek technique hai jismein aap target company ke employees, job postings, LinkedIn profiles, aur social media se technical information gather karte ho. Developers often apni skills, projects, aur company tech stack publicly share karte hain.

**Analogy:** Socho company ek locked building hai. Human OSINT matlab building ke employees se baat karke andar ki information nikalna - "Aap kaunsi technology use karte ho? Kaunsa database?" 🏢

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Tech Stack Discovery:** Job postings mein exact technologies mentioned hoti hain.
- **Version Information:** LinkedIn profiles: "Worked with Apache 2.4.29"
- **Internal Tools:** Employees apne projects share karte hain (GitHub, blogs).
- **Social Engineering Prep:** Employee names, roles, emails - phishing ke liye (ethical testing).

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Initial Recon:** Target ki tech stack samajhne ke liye.
- **Vulnerability Research:** Specific versions identify karke CVEs dhoondho.
- **Social Engineering:** (Ethical) Employee information for awareness training.
- **Competitive Intelligence:** Competitors ki technology aur hiring trends.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Blind Testing:** Tech stack nahi pata toh random attacks - time waste.
- **Missed Vulnerabilities:** Specific versions nahi pata toh targeted exploits miss.
- **Incomplete Profile:** Company ki internal structure, teams, tools - sab miss.

### 6. **Syntax aur Common Options**

**LinkedIn Dorking:**
```
site:linkedin.com "Company Name" "Software Engineer"
site:linkedin.com "Company Name" "DevOps"
site:linkedin.com "Company Name" "Security Engineer"
```

**Job Posting Sites:**
```
site:linkedin.com/jobs "Company Name"
site:indeed.com "Company Name"
site:glassdoor.com "Company Name"
```

**Google Dorking for Job Postings:**
```
"Company Name" "job" (AWS | Azure | GCP)
"Company Name" "hiring" (Python | Java | Node.js)
"Company Name" "looking for" (MySQL | PostgreSQL | MongoDB)
```

**GitHub Employee Search:**
```
site:github.com "Company Name" "employee"
site:github.com "@company-email.com"
```

### 7. **Example 1 (Basic)**

**Scenario:** "TechCorp" ki technology stack nikalni hai.

**Step-by-Step:**

**Step 1:** LinkedIn job search:
```
site:linkedin.com/jobs "TechCorp"
```

**Step 2:** Job posting analysis:
```
Job Title: Senior Backend Developer at TechCorp

Requirements:
- 5+ years Python experience
- Django framework
- PostgreSQL database
- AWS (EC2, S3, RDS)
- Redis for caching
- Docker & Kubernetes
```

**Step 3:** Tech stack identified:
```
Backend: Python + Django
Database: PostgreSQL
Cloud: AWS (EC2, S3, RDS)
Cache: Redis
Containers: Docker + Kubernetes
```

**Output:** Complete tech stack from job posting! 🎯

### 8. **Example 2 (Pentester-Focused)**

**Scenario:** "FinanceApp" ke specific versions aur internal tools nikalne hain.

**Step-by-Step:**

**Step 1:** LinkedIn employee search:
```
site:linkedin.com "FinanceApp" "DevOps Engineer"
```

**Step 2:** Profile analysis:
```
Employee: John Doe - DevOps Engineer at FinanceApp

Experience:
- Managed AWS infrastructure (EC2, RDS)
- Implemented CI/CD with Jenkins 2.289
- Migrated from MySQL 5.7 to PostgreSQL 12
- Configured Nginx 1.18 as reverse proxy
- Monitoring with Grafana + Prometheus
```

**Step 3:** Version information extracted:
```
Jenkins: 2.289
MySQL: 5.7 (old, migrated)
PostgreSQL: 12
Nginx: 1.18
```

**Step 4:** CVE research:
```
Jenkins 2.289: CVE-2021-21642 (RCE vulnerability!)
Nginx 1.18: Multiple known CVEs
PostgreSQL 12: Check for unpatched versions
```

**Step 5:** Intelligence report:
```
Finding: Technology stack identified via LinkedIn OSINT

Tech Stack:
- Jenkins 2.289 (Vulnerable to CVE-2021-21642)
- Nginx 1.18
- PostgreSQL 12
- AWS infrastructure

Source: Employee LinkedIn profile (public)

Recommendation:
- Update Jenkins to latest version
- Patch Nginx
- Verify PostgreSQL patch level
```

**Output:** Targeted vulnerability research based on OSINT! 💣

**Real Example - GitHub Employee Repos:**

**Step 1:** GitHub search:
```
site:github.com "@financeapp.com"
```

**Step 2:** Employee repos:
```
Employee: jane-dev
Email: jane@financeapp.com

Public Repos:
- financeapp-scripts (Internal automation scripts!)
- aws-config-backup (AWS configuration files!)
```

**Step 3:** Repo analysis:
```
financeapp-scripts/deploy.sh:
#!/bin/bash
# Deploy to production
ssh admin@prod-server-01.financeapp.com
cd /var/www/app
git pull origin main
sudo systemctl restart nginx
```

**Step 4:** Intelligence extracted:
```
- Production server hostname: prod-server-01.financeapp.com
- Deployment method: SSH + Git
- Web server: Nginx
- App location: /var/www/app
- Admin user exists
```

**Output:** Internal infrastructure details from employee GitHub! 🔍

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Direct Contact:** Employee ko directly message kiya (suspicious!) - passive OSINT karo.
- **Ignoring Old Profiles:** Sirf current employees dekhe - ex-employees bhi valuable info share karte hain.
- **No Cross-Verification:** Ek source se info li - multiple sources verify karo.

### 10. **Best Practices / Pro Tips**

- **LinkedIn Intelligence:**
  ```
  - Job postings (tech stack)
  - Employee profiles (versions, tools)
  - Company page (size, locations)
  - Skills section (technologies used)
  ```

- **Job Posting Analysis:**
  ```
  - Required skills = Current tech stack
  - "Nice to have" = Future plans
  - Team size mentions = Company scale
  - Salary range = Budget/maturity
  ```

- **GitHub Mining:**
  ```
  site:github.com "@company-domain.com"
  site:github.com "company-name" employee
  site:github.com "company-name" internal
  ```

- **Social Media:**
  ```
  Twitter: Developers tweet about work
  Medium: Technical blog posts
  Dev.to: Project showcases
  Stack Overflow: Questions reveal tech stack
  ```

- **Automated Tools:**
  - **theHarvester** - Email/employee enumeration
  - **LinkedIn2Username** - Generate username lists
  - **CrossLinked** - LinkedIn employee scraper

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

**Target Breach (2013) - Vendor OSINT**

**Background:** Target breach mein attackers ne HVAC vendor ko compromise kiya.

**OSINT Phase:**

**Step 1:** LinkedIn research:
```
Vendor: "Fazio Mechanical Services"
Employees: HVAC technicians
```

**Step 2:** Job postings:
```
"Looking for HVAC tech with basic IT skills"
"Must know Windows XP, basic networking"
```

**Step 3:** Intelligence:
```
- Small company (weak security)
- Outdated tech (Windows XP)
- Basic IT knowledge
- Access to Target network (HVAC monitoring)
```

**Step 4:** Attack:
- Phishing email to vendor employees
- Compromised vendor credentials
- Lateral movement to Target network
- 40 million credit cards stolen

**Lesson:** Human OSINT ne weak link identify kiya - vendor! 🎯

**Another Example - Bug Bounty:**

Ek researcher "StartupX" assess kar raha tha:

**Step 1:** LinkedIn job posting:
```
Job: DevOps Engineer at StartupX

Requirements:
- Experience with Kubernetes
- Helm charts
- AWS EKS
- "We use GitLab CI/CD"
```

**Step 2:** Intelligence:
```
- Kubernetes deployment
- GitLab for CI/CD
- AWS EKS (managed Kubernetes)
```

**Step 3:** GitHub search:
```
site:github.com "startupx" "gitlab-ci.yml"
```

**Step 4:** Public repo found:
```
Repo: startupx-demo
File: .gitlab-ci.yml

Content:
variables:
  AWS_ACCESS_KEY_ID: AKIA...
  KUBE_CONFIG: base64-encoded-config
```

**Step 5:** Finding:
```
Finding: GitLab CI config with AWS keys in public demo repo
Severity: Critical
Discovery: LinkedIn job posting → GitHub search

Impact:
- AWS credentials exposed
- Kubernetes config exposed
- Full infrastructure access
```

**Bounty:** $5,000

**Human OSINT → GitHub leak discovery! 💰**

### 12. **Checklist / Chota Recap (TL;DR)**

✅ Human OSINT = Employees, job postings, social media  
✅ LinkedIn = Tech stack, versions, employee info  
✅ Job postings = Current technologies, future plans  
✅ GitHub = Employee repos (internal scripts, configs)  
✅ Cross-verify = Multiple sources for accuracy  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kya employees ko directly contact karna legal hai?**  
**A:** Legal hai lekin suspicious hai. Passive OSINT better hai (public profiles dekho, contact mat karo).

**Q2: Ex-employees ki profiles useful hain?**  
**A:** Haan! Ex-employees often zyada openly share karte hain (no company restrictions). Lekin info outdated ho sakti hai.

**Q3: Kya yeh social engineering hai?**  
**A:** Nahi, yeh passive OSINT hai. Social engineering mein aap actively manipulate karte ho (calls, emails). Yahan sirf public info collect kar rahe ho.

### 14. **Practice ke liye Task**

**Task:** Human OSINT practice (ETHICAL ONLY):

**Exercise 1 - LinkedIn Job Analysis:**
```
site:linkedin.com/jobs "Microsoft"
```
**Kya Karna Hai:**
1. 5 job postings dekho
2. Tech stack note karo (languages, databases, cloud)
3. Patterns identify karo (common technologies)

**Exercise 2 - Employee Profile Analysis:**
```
site:linkedin.com "Google" "Site Reliability Engineer"
```
**Kya Karna Hai:**
1. 3-5 profiles dekho
2. Skills section analyze karo
3. Common tools/technologies note karo

**Exercise 3 - GitHub Employee Search:**
```
site:github.com "@microsoft.com"
```
**Kya Karna Hai:**
1. Employee repos dekho
2. Public vs private ratio note karo
3. Samjho ki employees kya share karte hain

**Exercise 4 - Cross-Platform:**
```
Pick a company
Check: LinkedIn + GitHub + Twitter
```
**Kya Karna Hai:**
1. LinkedIn se tech stack
2. GitHub se employee repos
3. Twitter se developer tweets
4. Cross-verify information

**Expected Learning:** Multi-source OSINT aur tech stack discovery.

### 15. **Aakhri Choti Summary (5 lines)**

- 👥 Human OSINT = Employees, job postings, social media (tech stack discovery)
- 💼 LinkedIn = Job postings reveal exact technologies aur versions
- 🔧 GitHub = Employee repos expose internal scripts aur configs
- 🎯 Cross-verification = Multiple sources for accurate intelligence
- ⚠️ Passive only = Public info dekho, employees ko contact mat karo

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Humans weakest link hain - lekin best intelligence source bhi! Job postings, LinkedIn profiles, GitHub repos - sab publicly available goldmine. Passive OSINT karo, social engineering nahi!" 👤

---


## **Topic 3: File Metadata (EXIF Data Analysis)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**File Metadata Analysis** - Documents aur images ke hidden metadata se location, software, aur author information nikalo.

### 2. **Ye Kya Hai? (What is it?)**

**Metadata** file ke andar chhupa hua data hai jo file ke baare mein information deta hai - jaise photo kab li gayi, kahan li gayi (GPS), kaunse camera se, kaunse software se edit hui. PDFs, Word docs, images - sabmein metadata hota hai.

**EXIF (Exchangeable Image File Format)** images ka metadata hai - camera model, GPS coordinates, timestamp, software used.

**Analogy:** Socho ek photo hai. Upar se sirf picture dikhti hai, lekin peeche ek "label" chipka hai jismein likha hai "Canon camera, Mumbai, 15 Jan 2024, 3:45 PM" - yeh metadata hai! 🏷️

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Location Discovery:** GPS coordinates se exact location (offices, data centers).
- **Software Identification:** Kaunsa software use hua (versions, tools).
- **Author Information:** Document creator ka naam, email, organization.
- **Timeline Analysis:** Files kab create/modify hui (incident timeline).

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Physical Location:** Target office/data center location nikalna.
- **Employee Information:** Document authors, emails, usernames.
- **Software Versions:** Outdated software identify karna (vulnerabilities).
- **Forensics:** Incident investigation, timeline reconstruction.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Location Blindness:** GPS data miss - physical security assessment incomplete.
- **Software Gaps:** Metadata mein software versions - vulnerability research miss.
- **Author Intel:** Document creators ke names/emails - social engineering prep miss.

### 6. **Syntax aur Common Options**

**Common Metadata Fields:**

**Images (EXIF):**
```
- Camera Make/Model
- GPS Latitude/Longitude
- Date/Time Original
- Software (editing tools)
- Copyright/Author
```

**Documents (PDF/DOCX):**
```
- Author
- Creator (software)
- Creation Date
- Modification Date
- Company/Organization
- Keywords
```

**Tools:**
```
- ExifTool (command line)
- Online: exifdata.com, metapicz.com
- Windows: Right-click → Properties → Details
- Linux: exiftool filename.jpg
```

### 7. **Example 1 (Basic)**

**Scenario:** Company website se downloaded image ka metadata check karna hai.

**Step-by-Step:**

**Step 1:** Image download:
```
company.com/about/team-photo.jpg
```

**Step 2:** Online tool use:
```
Visit: exifdata.com
Upload: team-photo.jpg
```

**Step 3:** Metadata analysis:
```
Camera: iPhone 12 Pro
GPS: 19.0760° N, 72.8777° E (Mumbai)
Date: 2023-08-15 14:30:00
Software: Adobe Photoshop 2023
```

**Step 4:** Intelligence:
```
- Photo Mumbai mein li gayi (office location?)
- iPhone 12 Pro (employee device)
- Photoshop se edit hui (marketing team)
- Date: August 2023 (recent)
```

**Output:** Location aur software information! 📍

### 8. **Example 2 (Pentester-Focused)**

**Scenario:** Target company ke PDF documents se author aur software information nikalna hai.

**Step-by-Step:**

**Step 1:** PDF download:
```
company.com/reports/annual-report-2023.pdf
```

**Step 2:** ExifTool use (command line):
```bash
exiftool annual-report-2023.pdf
```

**Step 3:** Metadata output:
```
File Name: annual-report-2023.pdf
File Size: 5.2 MB
File Type: PDF
Creator: Microsoft Word 2016
Producer: Adobe PDF Library 15.0
Author: John Doe
Company: TechCorp Inc
Creation Date: 2023:12:01 09:15:30
Modify Date: 2023:12:05 16:45:22
Keywords: financial, annual, confidential
```

**Step 4:** Intelligence extraction:
```
Author: John Doe (employee name)
Company: TechCorp Inc (confirmed)
Software: Microsoft Word 2016 (outdated!)
Adobe PDF: Version 15.0
Keywords: "confidential" (sensitivity indicator)
Timeline: Created Dec 1, Modified Dec 5
```

**Step 5:** Vulnerability research:
```
Microsoft Word 2016: Multiple CVEs
- CVE-2017-11882 (RCE)
- CVE-2018-0802 (RCE)
Adobe PDF Library 15.0: Check for vulnerabilities
```

**Step 6:** OSINT expansion:
```
LinkedIn search: "John Doe" "TechCorp"
Result: John Doe - CFO at TechCorp
Email pattern: john.doe@techcorp.com
```

**Step 7:** Report:
```
Finding: Document metadata exposure

Metadata Leaks:
- Author: John Doe (CFO)
- Email pattern: firstname.lastname@techcorp.com
- Software: MS Word 2016 (vulnerable versions)
- Company: TechCorp Inc
- Keywords: confidential

Intelligence Value:
- Employee identification (social engineering risk)
- Email pattern discovery
- Outdated software (exploitation potential)
- Document classification (confidential)

Recommendation:
- Strip metadata from public documents
- Update Microsoft Office
- Implement metadata removal policy
```

**Output:** Complete intelligence report from metadata! 💣

**Real Example - GPS Leak:**

**Step 1:** Company blog image:
```
techcorp.com/blog/new-office-tour.jpg
```

**Step 2:** EXIF analysis:
```
GPS Latitude: 37.7749° N
GPS Longitude: 122.4194° W
GPS Altitude: 15 meters
Date: 2024-01-10
```

**Step 3:** Google Maps:
```
Coordinates → San Francisco, CA
Exact location: 123 Market Street
Building: Tech Tower, Floor 5
```

**Step 4:** Intelligence:
```
- Office location: 123 Market Street, SF
- Floor: 5th (altitude data)
- Recent: January 2024
- Physical security assessment possible
```

**Output:** Exact office location from image metadata! 🗺️

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Assuming No Metadata:** "Image chhoti hai, metadata nahi hoga" - galat! Har file mein ho sakta hai.
- **Single Tool:** Ek tool use kiya - different tools different data show karte hain.
- **Ignoring Documents:** Sirf images check kiye, PDFs/DOCX ignore - documents mein bhi metadata.

### 10. **Best Practices / Pro Tips**

- **Tools Arsenal:**
  ```
  - ExifTool (comprehensive, command line)
  - FOCA (Windows, document metadata)
  - Metagoofil (automated document harvesting)
  - Online: exifdata.com, metapicz.com
  ```

- **Automated Harvesting:**
  ```bash
  # Metagoofil - Download & analyze documents
  metagoofil -d target.com -t pdf,doc,docx -l 100 -o output/
  
  # ExifTool batch processing
  exiftool -r -csv /path/to/files/ > metadata.csv
  ```

- **GPS Coordinates:**
  ```
  - Google Maps: Paste coordinates
  - GPS Visualizer: Batch plotting
  - Reverse geocoding: Address from coordinates
  ```

- **Document Metadata:**
  ```
  - Author names → LinkedIn search
  - Email patterns → Username enumeration
  - Software versions → CVE research
  - Company names → Verification
  ```

- **Privacy Check:**
  ```
  # Check your own files before sharing!
  exiftool -all= file.jpg  # Remove all metadata
  ```

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

**John McAfee Location Discovery (2012)**

**Background:** John McAfee (antivirus founder) hiding in Belize, wanted by police.

**OSINT Mistake:**

**Step 1:** Vice magazine interview:
- Photographer took photos with McAfee
- Published on Vice website

**Step 2:** EXIF analysis:
```
Photo metadata:
GPS: 15.7667° N, 88.5833° W
Date: 2012-12-03
Location: Guatemala (not Belize!)
```

**Step 3:** Discovery:
- Police used EXIF data
- Located McAfee in Guatemala
- Arrested within hours

**Lesson:** Ek photo ke metadata ne location expose kar diya! 📸

**Another Example - Corporate Espionage:**

Ek competitor "CompanyA" ki documents analyze kar raha tha (publicly available reports):

**Step 1:** PDF metadata:
```
Author: Sarah Johnson
Company: CompanyA
Software: Adobe InDesign CC 2019
Creation: 2023-06-15
Keywords: merger, acquisition, confidential
```

**Step 2:** Intelligence:
```
- Sarah Johnson = Senior Designer (LinkedIn)
- Adobe InDesign = Marketing/design team
- Keywords: "merger, acquisition" (strategic plans!)
- Timeline: June 2023
```

**Step 3:** Further OSINT:
```
LinkedIn: Sarah Johnson posted about "exciting project" in June 2023
Twitter: CompanyA CEO met with CompanyB CEO (June 2023)
News: CompanyA-CompanyB merger announced (August 2023)
```

**Step 4:** Competitive intelligence:
```
Metadata keywords revealed merger plans 2 months before announcement!
```

**Lesson:** Document metadata ne strategic plans leak kar diye! 💼

### 12. **Checklist / Chota Recap (TL;DR)**

✅ Metadata = Hidden file information (GPS, author, software)  
✅ EXIF = Image metadata (camera, location, timestamp)  
✅ Documents = Author, company, software versions  
✅ Tools = ExifTool, FOCA, Metagoofil  
✅ GPS coordinates = Exact physical locations  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kya har file mein metadata hota hai?**  
**A:** Most files mein hota hai, lekin deliberately stripped bhi ho sakta hai. Images, PDFs, Office docs - sabmein common hai.

**Q2: Kya metadata fake ho sakta hai?**  
**A:** Haan, manually edit kiya ja sakta hai. Cross-verify karo (multiple files, other sources).

**Q3: Metadata kaise remove karein?**  
**A:** 
- ExifTool: `exiftool -all= file.jpg`
- Online tools: exifremove.com
- Photoshop: Save for Web (strips metadata)
- Office: File → Info → Remove Personal Information

### 14. **Practice ke liye Task**

**Task:** Metadata analysis practice:

**Exercise 1 - Image EXIF:**
```
Download any image from a company website
Use: exifdata.com
```
**Kya Karna Hai:**
1. Image upload karo
2. EXIF data dekho
3. GPS coordinates check karo (agar hain)
4. Software/camera info note karo

**Exercise 2 - PDF Metadata:**
```
Download a public PDF (company report, whitepaper)
Use: ExifTool or online tool
```
**Kya Karna Hai:**
1. Author name dekho
2. Company name verify karo
3. Software version note karo
4. Creation/modification dates analyze karo

**Exercise 3 - Batch Analysis:**
```
Download 5-10 images from same website
Use: ExifTool batch mode
```
**Kya Karna Hai:**
1. Sabka metadata extract karo
2. Patterns identify karo (same camera? same location?)
3. Timeline banao
4. Intelligence report likho

**Exercise 4 - GPS Mapping:**
```
If GPS coordinates found:
Use: Google Maps
```
**Kya Karna Hai:**
1. Coordinates paste karo
2. Location identify karo
3. Street view dekho (if available)
4. Physical security assessment karo

**Expected Learning:** Metadata extraction aur intelligence analysis.

### 15. **Aakhri Choti Summary (5 lines)**

- 🏷️ Metadata = Hidden file info (GPS, author, software, timestamps)
- 📸 EXIF = Image metadata (camera, location, exact coordinates)
- 📄 Documents = Author names, company, software versions (CVE research)
- 🗺️ GPS coordinates = Exact physical locations (offices, data centers)
- 🔧 Tools = ExifTool (best), FOCA, Metagoofil (automated)

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Metadata 'invisible ink' hai - file ke andar chhupa hua intelligence. Ek photo ke GPS se office location, ek PDF se employee names. Hamesha metadata check karo - goldmine hai!" 🔍

---

## **Topic 4: Censys & ZoomEye (Shodan Alternatives)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Censys & ZoomEye** - Shodan ke alternatives jo different data aur unique features provide karte hain.

### 2. **Ye Kya Hai? (What is it?)**

**Censys** aur **ZoomEye** Shodan jaise device search engines hain jo internet-connected devices scan karte hain. Har engine ka apna scanning methodology aur data set hai - ek mein jo nahi milta, dusre mein mil sakta hai.

**Analogy:** Socho teen detectives hain (Shodan, Censys, ZoomEye) jo same city investigate kar rahe hain. Har ek alag routes leta hai, alag clues dhoondhta hai - sabke findings combine karo for complete picture! 🕵️

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Different Coverage:** Censys alag IPs scan karta hai than Shodan.
- **Certificate Search:** Censys SSL/TLS certificates search karta hai (unique feature).
- **Cross-Verification:** Ek engine par nahi mila, dusre par try karo.
- **Free Tiers:** Censys aur ZoomEye ke free accounts Shodan se zyada generous.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Shodan Limitations:** Free account exhausted ya results incomplete.
- **Certificate Intelligence:** SSL certificates se subdomain/organization discovery.
- **Cross-Platform:** Multiple engines se comprehensive coverage.
- **Academic Research:** Censys university accounts free hain.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Incomplete Coverage:** Sirf Shodan use kiya - 30-40% devices miss.
- **Certificate Blindness:** SSL certificate intelligence miss - subdomain discovery gap.
- **Single Source:** Ek engine ka data - verification nahi, false negatives possible.

### 6. **Syntax aur Common Options**

**Censys (censys.io):**
```
Basic Search:
services.port: 22
services.service_name: HTTP
location.country: India

Certificate Search:
parsed.subject.common_name: *.example.com
parsed.issuer.organization: "Let's Encrypt"
parsed.validity.start: [2023-01-01 TO 2023-12-31]

Advanced:
services.http.response.html_title: "Admin Panel"
autonomous_system.name: "Amazon"
```

**ZoomEye (zoomeye.org):**
```
Basic Search:
port:22
country:"IN"
city:"Mumbai"

Service Search:
app:"Apache"
ver:"2.4.49"
os:"Windows"

Advanced:
ssl:"example.com"
header:"Server: nginx"
title:"Dashboard"
```

### 7. **Example 1 (Basic)**

**Scenario:** India mein SSH servers dhoondhne hain (cross-platform comparison).

**Shodan:**
```
port:22 country:IN
Results: 100,000+
```

**Censys:**
```
services.port: 22 AND location.country: India
Results: 85,000+
```

**ZoomEye:**
```
port:22 country:"IN"
Results: 95,000+
```

**Analysis:**
- Different counts (different scanning times/methods)
- Some IPs unique to each platform
- Combined coverage: 120,000+ unique IPs

**Output:** Cross-platform search for comprehensive coverage! 🎯

### 8. **Example 2 (Pentester-Focused)**

**Scenario:** "TechCorp" ke SSL certificates se subdomains discover karne hain.

**Step-by-Step (Censys):**

**Step 1:** Certificate search:
```
parsed.subject.common_name: *.techcorp.com
```

**Step 2:** Results:
```
Certificate 1:
Common Name: *.techcorp.com
SANs (Subject Alternative Names):
- www.techcorp.com
- api.techcorp.com
- admin.techcorp.com
- staging.techcorp.com
- dev-internal.techcorp.com

Certificate 2:
Common Name: *.prod.techcorp.com
SANs:
- db.prod.techcorp.com
- cache.prod.techcorp.com
```

**Step 3:** Subdomain list:
```
Discovered Subdomains:
1. www.techcorp.com (known)
2. api.techcorp.com (known)
3. admin.techcorp.com (interesting!)
4. staging.techcorp.com (development)
5. dev-internal.techcorp.com (internal!)
6. db.prod.techcorp.com (database!)
7. cache.prod.techcorp.com (cache server)
```

**Step 4:** Verification:
```
nslookup dev-internal.techcorp.com
→ Resolves! (hidden subdomain)

nslookup db.prod.techcorp.com
→ Resolves! (database server exposed)
```

**Step 5:** Further recon:
```
Censys: services.port: 3306 AND parsed.subject.common_name: db.prod.techcorp.com
Result: MySQL port 3306 open!
```

**Step 6:** Report:
```
Finding: Hidden subdomains via SSL certificate enumeration

Discovery Method: Censys certificate search
Subdomains Found: 7 (5 new)

Critical Findings:
- dev-internal.techcorp.com (internal development)
- db.prod.techcorp.com (MySQL exposed, port 3306)
- cache.prod.techcorp.com (Redis/Memcached?)

Severity: High
Risk: Internal systems exposed, database accessible

Recommendation:
- Restrict database to internal network
- Review certificate SANs (remove internal domains)
- Implement proper network segmentation
```

**Output:** Hidden subdomain discovery via certificates! 💣

**Real Example - ZoomEye Unique Feature:**

**Step 1:** ZoomEye search:
```
ssl:"techcorp.com" +port:443
```

**Step 2:** Results with screenshots:
```
ZoomEye provides:
- Banner data (like Shodan)
- SSL certificate info
- HTTP response headers
- Screenshots (some results)
```

**Step 3:** Visual confirmation:
```
Screenshot shows: Admin login page
URL: admin-old.techcorp.com
Status: Forgotten subdomain with old admin panel
```

**Output:** Visual discovery of forgotten assets! 📸

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Single Engine:** Sirf Shodan use kiya - Censys/ZoomEye ignore.
- **Syntax Confusion:** Shodan syntax Censys mein use kiya - different syntax hai!
- **Free Tier Limits:** Free accounts ki limits nahi samjhe - paid features expect kiye.

### 10. **Best Practices / Pro Tips**

- **Censys Strengths:**
  ```
  - Certificate search (best in class)
  - Academic free accounts (unlimited)
  - IPv4 + IPv6 coverage
  - Historical data
  ```

- **ZoomEye Strengths:**
  ```
  - Chinese internet coverage (best)
  - Screenshots (visual confirmation)
  - Free tier generous (10,000 results/month)
  - Web + Device search
  ```

- **Cross-Platform Strategy:**
  ```
  1. Start with Shodan (most popular, good docs)
  2. Censys for certificates (subdomain discovery)
  3. ZoomEye for Chinese targets or visual confirmation
  4. Combine results (unique IPs from each)
  ```

- **Censys Certificate Hunting:**
  ```
  parsed.subject.common_name: *.target.com
  parsed.issuer.organization: "Let's Encrypt"
  parsed.validity.start: [2023-01-01 TO *]
  ```

- **ZoomEye Filters:**
  ```
  app:"Apache" +ver:"2.4.49"
  country:"CN" +port:22
  ssl:"target.com" +port:443
  ```

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

**Equifax Breach (2017) - Certificate Intelligence**

**Background:** Equifax breach investigation mein certificate analysis use hua.

**Post-Breach Analysis:**

**Step 1:** Censys certificate search:
```
parsed.subject.organization: "Equifax"
```

**Step 2:** Results:
```
500+ certificates found
Multiple subdomains exposed:
- admin-portal.equifax.com
- legacy-api.equifax.com
- test-environment.equifax.com
```

**Step 3:** Historical analysis:
```
Censys historical data:
- Vulnerable Apache Struts version detected (March 2017)
- Certificate showed internal subdomain
- Subdomain had unpatched Struts
```

**Step 4:** Timeline reconstruction:
```
- March 2017: Vulnerable Struts version live
- May 2017: Breach occurred
- July 2017: Breach discovered
- September 2017: Public disclosure
```

**Lesson:** Certificate intelligence ne breach timeline reconstruct kiya! 📅

**Another Example - Bug Bounty:**

Ek researcher "StartupX" assess kar raha tha:

**Step 1:** Shodan search:
```
org:"StartupX" port:443
Results: 10 servers
```

**Step 2:** Censys certificate search:
```
parsed.subject.common_name: *.startupx.com
Results: 15 certificates (5 extra!)
```

**Step 3:** New subdomains:
```
From Censys certificates:
- internal-api.startupx.com (not in Shodan!)
- backup-db.startupx.com (not in Shodan!)
- old-admin.startupx.com (not in Shodan!)
```

**Step 4:** Verification:
```
nslookup internal-api.startupx.com → Resolves!
Browser: internal-api.startupx.com → API docs exposed!
```

**Step 5:** Finding:
```
Finding: Hidden API documentation via certificate enumeration
Discovery: Censys (not found in Shodan)
Severity: Medium
Impact: API structure exposed, potential for abuse
```

**Bounty:** $2,000

**Censys ne woh dhoondha jo Shodan miss kar gaya! 💰**

### 12. **Checklist / Chota Recap (TL;DR)**

✅ Censys = Certificate search expert (subdomain discovery)  
✅ ZoomEye = Chinese internet + screenshots  
✅ Cross-platform = Shodan + Censys + ZoomEye = complete coverage  
✅ Different syntax = Har engine ka alag query language  
✅ Free tiers = Censys academic, ZoomEye 10K/month  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kaunsa engine best hai?**  
**A:** Depends on use case:
- Shodan: General device search, best documentation
- Censys: Certificate intelligence, academic research
- ZoomEye: Chinese targets, visual confirmation
Best strategy: Sabko use karo!

**Q2: Kya free accounts enough hain?**  
**A:** Basic recon ke liye haan. Serious pentesting ke liye paid accounts better (unlimited searches, API access, historical data).

**Q3: Certificate search kyun important hai?**  
**A:** SSL certificates mein SANs (Subject Alternative Names) hote hain - yeh hidden subdomains reveal karte hain jo DNS enumeration miss kar deta hai.

### 14. **Practice ke liye Task**

**Task:** Multi-engine comparison:

**Exercise 1 - Same Search, Different Engines:**
```
Shodan: port:22 country:IN
Censys: services.port: 22 AND location.country: India
ZoomEye: port:22 country:"IN"
```
**Kya Karna Hai:**
1. Teeno engines par search karo
2. Results count compare karo
3. Pehle 5 IPs note karo (unique hain?)
4. Samjho ki coverage kyun different hai

**Exercise 2 - Certificate Search (Censys):**
```
parsed.subject.common_name: *.microsoft.com
```
**Kya Karna Hai:**
1. Certificate results dekho
2. SANs (subdomains) list banao
3. Kitne subdomains mile
4. Samjho ki certificate enumeration kyun powerful hai

**Exercise 3 - Visual Search (ZoomEye):**
```
ssl:"target.com" +port:443
```
**Kya Karna Hai:**
1. Results browse karo
2. Screenshots dekho (if available)
3. Visual confirmation ki value samjho

**Exercise 4 - Cross-Platform:**
```
Pick a company
Search on: Shodan + Censys + ZoomEye
```
**Kya Karna Hai:**
1. Same query teeno par
2. Unique results note karo
3. Combined list banao
4. Coverage difference calculate karo

**Expected Learning:** Multi-engine strategy aur comprehensive coverage.

### 15. **Aakhri Choti Summary (5 lines)**

- 🔍 Censys = Certificate search expert (subdomain discovery via SANs)
- 🌏 ZoomEye = Chinese internet + screenshots (visual confirmation)
- 🎯 Cross-platform = Shodan + Censys + ZoomEye = 100% coverage
- 📜 Certificates = Hidden subdomains reveal (DNS enumeration miss karta hai)
- 💰 Free tiers = Censys academic unlimited, ZoomEye 10K/month

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Ek engine se 70% milta hai, teen engines se 100%! Censys certificates ka expert, ZoomEye visual confirmation ka king. Multi-engine strategy = comprehensive recon!" 🎯

---

# **🎓 Module 8 Complete! Congratulations!**

Aapne **Advanced Recon Techniques** master kar liye! Ab aap:
- ✅ Wayback Machine use kar sakte ho (deleted content, historical intelligence)
- ✅ Human OSINT kar sakte ho (LinkedIn, job postings, GitHub)
- ✅ File metadata analyze kar sakte ho (EXIF, GPS, author info)
- ✅ Censys & ZoomEye use kar sakte ho (Shodan alternatives)

**Module 8 Mastery Checklist:**
- ✅ Time-travel OSINT (Wayback Machine)
- ✅ Employee intelligence (LinkedIn, job postings)
- ✅ Metadata extraction (images, documents)
- ✅ Multi-engine device search (Shodan + Censys + ZoomEye)
- ✅ Certificate enumeration (subdomain discovery)

**Key Takeaways:**
- Wayback Machine = Internet ka permanent memory (kuch delete nahi hota)
- Human OSINT = Job postings reveal tech stack (versions, tools)
- Metadata = Hidden intelligence (GPS, authors, software)
- Multi-engine = 100% coverage (ek engine 70%, teen engines 100%)
- Certificates = Subdomain goldmine (SANs reveal hidden domains)

**Real-World Impact:**
- John McAfee: EXIF GPS ne location expose kiya
- Target Breach: Vendor OSINT ne weak link identify kiya
- Equifax: Certificate analysis ne timeline reconstruct kiya

**Advanced Tools:**
- Wayback: waybackurls, gau
- Human OSINT: theHarvester, LinkedIn2Username
- Metadata: ExifTool, FOCA, Metagoofil
- Engines: Shodan, Censys, ZoomEye

**Next Module:**
- Module 9: OSINT Ethics & Legal Boundaries (FINAL MODULE!)

Yeh last module hai - sabse important! Legal boundaries, ethical hacking, responsible disclosure, aur kaise safe raho. 

Ready for final module? 🚀

---
=============================================================

# **Google Dork And Search Engine Dorking: Zero-to-Hacker Notes** 🚀

---

# **Module 9: OSINT Ethics & Legal Boundaries**

---

## **Topic 1: The "Look, Don't Touch" Rule (Viewing vs. Accessing)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Look, Don't Touch** - OSINT mein legal line: Information dekh sakte ho, access/use nahi kar sakte.

### 2. **Ye Kya Hai? (What is it?)**

**"Look, Don't Touch"** rule OSINT ka golden rule hai - aap publicly available information dekh sakte ho (search, browse, screenshot), lekin us information ko **use** nahi kar sakte (login, download, exploit). Yeh legal aur illegal ke beech ki line hai.

**Analogy:** Socho ek ghar ka darwaza khula hai. Aap bahar se andar dekh sakte ho (legal), lekin andar ghus nahi sakte (illegal). Window se dekho, darwaza cross mat karo! 🚪

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Legal Protection:** Yeh line cross ki = cybercrime, jail possible.
- **Ethical Hacking:** Professional pentesters yeh rule follow karte hain.
- **Career Safety:** Ek galti se career khatam, criminal record.
- **Trust:** Clients/companies trust karte hain ethical hackers ko.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Har OSINT Activity:** Har search, har discovery mein yeh rule apply hota hai.
- **Bug Bounty:** Program scope mein bhi "look, don't touch" critical.
- **Pentesting:** Client permission ke bina kuch bhi access mat karo.
- **Research:** Academic/security research mein bhi ethical boundaries.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Criminal Charges:** Unauthorized access = Computer Fraud & Abuse Act (US), IT Act (India).
- **Career End:** Criminal record = no security jobs, no certifications.
- **Civil Lawsuits:** Companies sue kar sakti hain (damages, legal fees).
- **Reputation Loss:** Security community mein blacklist.

### 6. **Syntax aur Common Options**

**LEGAL (Look):**
```
✅ Google/Shodan/GitHub search
✅ Public website browsing
✅ Screenshot lena (evidence)
✅ URL noting (documentation)
✅ Banner reading (Shodan results)
✅ Public social media viewing
✅ Wayback Machine browsing
✅ Certificate enumeration
```

**ILLEGAL (Touch):**
```
❌ Login attempt (even with found credentials)
❌ File download (leaked databases, documents)
❌ API key validation (testing if key works)
❌ Exploit execution (even on vulnerable systems)
❌ Brute force attacks
❌ SQL injection testing (without permission)
❌ Port scanning (without permission)
❌ Social engineering (without permission)
```

### 7. **Example 1 (Basic)**

**Scenario:** Shodan par exposed camera mila.

**LEGAL Actions:**
```
✅ Shodan search: port:554 country:IN
✅ Results dekho (IP, port, banner)
✅ Screenshot lo (evidence)
✅ Location note karo
✅ Report likho
```

**ILLEGAL Actions:**
```
❌ Camera stream open karna (browser mein IP:554)
❌ Default credentials try karna (admin/admin)
❌ Camera settings access karna
❌ Recording download karna
```

**Correct Approach:**
```
1. Shodan par camera dekha (LEGAL)
2. Screenshot li (LEGAL)
3. Company ko report kiya: "Your camera exposed on IP x.x.x.x" (ETHICAL)
4. Camera access NAHI kiya (LEGAL BOUNDARY RESPECTED)
```

**Output:** Ethical discovery + responsible disclosure! ✅

### 8. **Example 2 (Pentester-Focused)**

**Scenario:** GitHub par company ke AWS keys mile.

**LEGAL Actions:**
```
✅ GitHub search: org:company "AKIA"
✅ Repository dekho
✅ File path note karo
✅ Key format verify karo (AKIA pattern)
✅ Screenshot lo (partial key, for proof)
✅ Commit hash note karo
```

**ILLEGAL Actions:**
```
❌ AWS console mein login (key validate karna)
❌ S3 buckets list karna (aws s3 ls)
❌ EC2 instances check karna
❌ "Read-only" access bhi ILLEGAL hai!
❌ Key ko test karna (even offline tools)
```

**Correct Approach:**
```
Step 1: GitHub par key dekha (LEGAL)
Step 2: Screenshot li (partial key) (LEGAL)
Step 3: Report banai:
   "Finding: AWS keys exposed in repo X
    File: config/aws.yml
    Commit: abc123
    Evidence: [Screenshot with partial key]
    
    ⚠️ KEY NOT VALIDATED (ethical boundary)
    
    Recommendation: Revoke keys immediately"
    
Step 4: Company ko private email (ETHICAL)
Step 5: Key validate NAHI kiya (LEGAL BOUNDARY RESPECTED)
```

**Output:** High-severity finding without crossing legal line! 💯

**Real Example - Database Exposure:**

**Scenario:** Shodan par MongoDB exposed (no auth).

**LEGAL:**
```
✅ Shodan search: port:27017 country:IN
✅ Banner dekho (MongoDB version)
✅ Screenshot lo
✅ IP note karo
```

**ILLEGAL:**
```
❌ mongo --host IP:27017 (connection attempt)
❌ show dbs (database list)
❌ db.users.find() (data access)
❌ "Just checking" bhi ILLEGAL!
```

**Why Illegal?**
```
- Unauthorized access to computer system
- Even "read-only" = access = crime
- "No password" ≠ "permission to access"
- Intent doesn't matter, action matters
```

**Correct Report:**
```
Finding: MongoDB exposed without authentication
IP: x.x.x.x:27017
Evidence: Shodan banner showing "MongoDB 4.2"
Status: No authentication required (banner indicates)

⚠️ DATABASE NOT ACCESSED (ethical boundary)

Severity: Critical
Risk: Full database access, data breach potential

Recommendation:
1. Enable authentication immediately
2. Restrict to internal network
3. Audit for unauthorized access
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **"Just Checking":** "Main sirf check kar raha tha ki key kaam karti hai" - YEH BHI ILLEGAL HAI!
- **"No Harm Done":** "Maine kuch modify nahi kiya, sirf dekha" - Access itself illegal hai.
- **"Public Data":** "Data public tha toh access kar liya" - Public ≠ Permission.

### 10. **Best Practices / Pro Tips**

- **Golden Rules:**
  ```
  1. Search = Legal
  2. Access = Illegal (without permission)
  3. When in doubt, DON'T!
  4. Screenshot > Download
  5. Report > Exploit
  ```

- **Evidence Collection (Legal):**
  ```
  ✅ Screenshots (with timestamps)
  ✅ URLs (exact paths)
  ✅ Commit hashes (GitHub)
  ✅ Shodan/Censys result IDs
  ✅ Partial data (for proof, not full dump)
  ```

- **Red Flags (Stop Immediately):**
  ```
  🚨 Login prompt appeared
  🚨 "Unauthorized access" warning
  🚨 Authentication required
  🚨 Terms of Service violation
  🚨 Feeling "this might be illegal"
  ```

- **Safe Reporting:**
  ```
  1. Private disclosure (email, bug bounty platform)
  2. Evidence without sensitive data
  3. Clear severity assessment
  4. Actionable recommendations
  5. No public disclosure (until permission)
  ```

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

**Andrew "weev" Auernheimer Case (2010)**

**Background:** AT&T iPad users ka email leak.

**What Happened:**

**Step 1:** Researcher ne AT&T website par vulnerability discover kiya:
```
URL pattern: att.com/device?id=12345
Change ID → Different user's email visible
```

**Step 2:** Script banaya:
```
for id in range(100000, 200000):
    fetch(f"att.com/device?id={id}")
    save_email()
```

**Step 3:** 114,000 emails collected

**Step 4:** Media ko leak kiya (Gawker)

**Legal Outcome:**
```
- Arrested under Computer Fraud & Abuse Act
- Convicted: 41 months prison
- $73,000 fine
- Appeal: Conviction overturned (venue issue)
- But: Years of legal battle, reputation damaged
```

**Lesson:**
```
❌ Automated scraping (beyond normal browsing)
❌ Data collection (even if publicly accessible)
❌ Public disclosure (without responsible disclosure)

✅ Should have: Report to AT&T privately
✅ Should have: Stop after discovering vulnerability
✅ Should have: Not collect 114K emails
```

**"Look, Don't Touch" violated = Legal nightmare! ⚖️**

**Another Example - Ethical Researcher:**

**Scenario:** Researcher ne company database exposed dekha (Shodan).

**Ethical Approach:**

**Step 1:** Shodan par dekha (LEGAL)
```
port:3306 org:"Company X"
Result: MySQL exposed, no auth
```

**Step 2:** Screenshot li (LEGAL)
```
Evidence: Shodan result showing open MySQL
```

**Step 3:** Report banai (ETHICAL)
```
Subject: Critical - MySQL Database Exposed

Dear Security Team,

I discovered your MySQL database exposed on Shodan:
IP: x.x.x.x:3306
Evidence: [Screenshot attached]

⚠️ I did NOT access the database (ethical boundary)

Severity: Critical
Risk: Full database access, data breach

Recommendation: Restrict to internal network immediately

Best regards,
[Researcher]
```

**Step 4:** Company response:
```
- Database secured within 2 hours
- Thank you email + $5,000 bounty
- Hall of Fame mention
```

**Step 5:** Public disclosure (after 90 days, with permission):
```
Blog post: "How I Found Exposed Database (Ethically)"
- No company name (anonymized)
- Focus on methodology
- Emphasis on ethical boundaries
```

**Outcome:**
```
✅ Legal (no access attempt)
✅ Ethical (responsible disclosure)
✅ Rewarded (bounty + reputation)
✅ Educational (blog post helped community)
```

**"Look, Don't Touch" followed = Win-win! 🏆**

### 12. **Checklist / Chota Recap (TL;DR)**

✅ Look = Legal (search, browse, screenshot)  
✅ Touch = Illegal (login, download, access, exploit)  
✅ "Just checking" = Still illegal (intent doesn't matter)  
✅ Public data ≠ Permission (accessible ≠ authorized)  
✅ When in doubt, DON'T (stop immediately)  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Agar password nahi hai toh access kar sakta hoon?**  
**A:** NAHI! "No password" ≠ "permission". Unauthorized access hai, illegal hai.

**Q2: "Read-only" access bhi illegal hai?**  
**A:** Haan! Access itself illegal hai, modify karna zaroori nahi. Dekh bhi nahi sakte without permission.

**Q3: Agar accidentally access ho gaya toh?**  
**A:** Immediately stop karo, back out karo, report karo. "Accident" defense weak hai lekin better than continuing.

### 14. **Practice ke liye Task**

**Task:** Ethical boundary practice:

**Scenario 1:**
```
Shodan par exposed admin panel mila (no password).
```
**Question:** Kya legal hai?
```
A) Login page screenshot
B) admin/admin try karna
C) "Guest" login try karna
D) Source code dekhna
```
**Answer:** Sirf A (screenshot). B, C = illegal. D = legal (public page source).

**Scenario 2:**
```
GitHub par AWS key mila.
```
**Question:** Kya legal hai?
```
A) Key screenshot (partial)
B) aws s3 ls (test karna)
C) Key ko report karna
D) Key delete karne ki koshish
```
**Answer:** A aur C legal. B aur D illegal.

**Scenario 3:**
```
Pastebin par database dump mila.
```
**Question:** Kya legal hai?
```
A) Paste URL note karna
B) Full dump download karna
C) Sample data screenshot (5 rows)
D) Company ko report karna
```
**Answer:** A, C, D legal. B illegal (full download).

**Expected Learning:** Legal vs illegal actions clearly samajh aayenge.

### 15. **Aakhri Choti Summary (5 lines)**

- 👀 Look = Legal (search, browse, screenshot, document)
- 🚫 Touch = Illegal (login, download, access, exploit, validate)
- ⚖️ "No password" ≠ Permission (accessible ≠ authorized)
- 🛡️ "Just checking" = Still crime (intent doesn't matter, action does)
- 📧 Report = Ethical (responsible disclosure, not exploitation)

> **📌 Ye Zaroor Yaad Rakhein:**  
> "'Look, Don't Touch' rule life-saver hai - yeh line cross ki toh career khatam, jail possible. Shodan par dekho, login mat karo. GitHub par key dekho, validate mat karo. Ethical hacker ban ne ke liye yeh rule sacred hai!" 🔐

---

## **Topic 2: Legal Risks & Staying Ethical**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Legal Risks** - Cybercrime laws, penalties, aur kaise ethical boundaries mein raho.

### 2. **Ye Kya Hai? (What is it?)**

Cybercrime laws har country mein hain jo unauthorized computer access ko crime banate hain. India mein **IT Act 2000**, US mein **Computer Fraud & Abuse Act (CFAA)**, UK mein **Computer Misuse Act**. Yeh laws bahut strict hain aur "ethical intent" defense weak hai.

**Analogy:** Socho traffic laws hain - "Main sirf test kar raha tha" red light cross karne ka excuse nahi hai. Similarly, "Main sirf check kar raha tha" unauthorized access ka excuse nahi! 🚦

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Criminal Penalties:** Jail (1-10 years), fines (lakhs/millions), criminal record.
- **Civil Lawsuits:** Companies damages claim kar sakti hain (crores).
- **Career Impact:** Security certifications revoked, jobs lost, blacklisted.
- **International Laws:** Ek country mein crime, dusri country extradite kar sakti hai.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Har Activity:** Har OSINT/pentesting activity se pehle legal check karo.
- **Client Engagement:** Signed contract zaroori (scope, permissions, liability).
- **Bug Bounty:** Program rules carefully padho (scope, restrictions).
- **Personal Research:** Bhi ethical boundaries follow karo (no excuse).

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Arrest:** Police action, investigation, court cases.
- **Financial Ruin:** Legal fees (lakhs), fines, damages.
- **Career End:** No security jobs, certifications lost, reputation destroyed.
- **Family Impact:** Stress, social stigma, financial burden.

### 6. **Syntax aur Common Options**

**Major Cybercrime Laws:**

**India - IT Act 2000:**
```
Section 43: Unauthorized access - Fine up to ₹1 crore
Section 66: Computer-related offenses - 3 years jail + fine
Section 66B: Receiving stolen data - 3 years jail + fine
Section 66C: Identity theft - 3 years jail + ₹1 lakh fine
Section 66D: Cheating using computer - 3 years jail + ₹1 lakh
Section 66E: Privacy violation - 3 years jail + ₹2 lakh
Section 66F: Cyber terrorism - Life imprisonment
```

**US - Computer Fraud & Abuse Act (CFAA):**
```
18 U.S.C. § 1030:
- Unauthorized access: Up to 10 years prison
- Trafficking passwords: Up to 10 years
- Extortion: Up to 5 years
- Damage to computers: Up to 10 years
- Repeat offenses: Up to 20 years
```

**UK - Computer Misuse Act 1990:**
```
Section 1: Unauthorized access - 2 years prison
Section 2: Unauthorized access with intent - 5 years
Section 3: Unauthorized modification - 10 years
Section 3ZA: Serious damage - Life imprisonment
```

### 7. **Example 1 (Basic)**

**Scenario:** Shodan par exposed camera dekha aur "test" karne ki sochi.

**Legal Analysis:**

**Action:** Camera stream open karna (IP:port browser mein)

**Laws Violated:**
```
India:
- IT Act Section 43: Unauthorized access
- Penalty: ₹1 crore fine

US (if US camera):
- CFAA 18 U.S.C. § 1030(a)(2)
- Penalty: Up to 1 year prison (first offense)

UK (if UK camera):
- Computer Misuse Act Section 1
- Penalty: Up to 2 years prison
```

**Defense (Weak):**
```
❌ "Main sirf dekh raha tha" - Access itself crime
❌ "Kuch modify nahi kiya" - Doesn't matter
❌ "No password tha" - Still unauthorized
❌ "Security research" - Without permission = invalid
```

**Correct Approach:**
```
✅ Shodan par dekho (legal)
✅ Screenshot lo (legal)
✅ Report karo (ethical)
✅ Access MAT karo (legal boundary)
```

### 8. **Example 2 (Pentester-Focused)**

**Scenario:** Bug bounty program mein out-of-scope target test kar liya.

**Program Rules:**
```
Scope:
✅ *.company.com
✅ api.company.com
✅ mobile.company.com

Out of Scope:
❌ partner.company.com
❌ Third-party services
❌ Physical testing
```

**What Happened:**
```
Researcher ne partner.company.com par SQL injection test kiya
(Out of scope tha!)
```

**Legal Consequences:**
```
Bug Bounty Platform:
- Account banned (permanent)
- No payment for any findings
- Blacklisted from all programs

Company Action:
- Legal notice sent
- Demanded researcher identity
- Threatened lawsuit

Potential Criminal:
- Unauthorized access (partner.company.com)
- Computer damage (SQL injection)
- IT Act / CFAA violation
```

**Lesson:**
```
❌ Scope violation = No legal protection
❌ Bug bounty rules = Contract (legally binding)
❌ "Didn't know" = Not valid defense
❌ Out of scope = Same as hacking random site

✅ Always read scope carefully
✅ When in doubt, ask program
✅ Stay within boundaries (no exceptions)
```

**Real Example - Aaron Swartz Case (2011):**

**Background:** MIT student, activist, programmer.

**What Happened:**
```
Step 1: MIT network se JSTOR access kiya (academic papers)
Step 2: Automated script se 4.8 million articles download kiye
Step 3: Free distribution ka plan (information should be free)
```

**Legal Action:**
```
Charges:
- Wire fraud
- Computer fraud
- Unlawfully obtaining information
- Recklessly damaging a protected computer

Potential Penalty:
- 35 years prison
- $1 million fine
```

**Outcome:**
```
- 2 years legal battle
- Severe depression
- 2013: Suicide (age 26)
- Case dismissed (posthumously)
```

**Lesson:**
```
❌ "Good intentions" ≠ Legal defense
❌ "Information should be free" ≠ Legal justification
❌ Automated access = Aggravating factor
❌ Federal prosecution = Severe penalties

Impact:
- Life destroyed over "ethical" act
- Family devastated
- Community shocked
- Laws still unchanged
```

**This is why "Look, Don't Touch" is CRITICAL! 💔**

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **"Ethical Intent":** "Meri niyat achhi thi" - Court mein yeh defense weak hai.
- **"No Damage":** "Maine kuch toda nahi" - Access itself crime hai.
- **"Security Research":** Bina permission ke yeh excuse invalid hai.

### 10. **Best Practices / Pro Tips**

- **Legal Protection:**
  ```
  1. Signed Contract (pentesting)
  2. Bug Bounty Program (written scope)
  3. Written Permission (email, letter)
  4. Liability Insurance (professional pentesters)
  5. Legal Consultation (when in doubt)
  ```

- **Safe Practices:**
  ```
  ✅ Passive OSINT only (no active attacks)
  ✅ Public data only (no unauthorized access)
  ✅ Screenshot evidence (no data download)
  ✅ Responsible disclosure (private reporting)
  ✅ Scope adherence (strict boundaries)
  ```

- **Red Flags (Stop Immediately):**
  ```
  🚨 No written permission
  🚨 Scope unclear
  🚨 Client asking illegal activity
  🚨 "Just this once" requests
  🚨 Feeling uncomfortable
  ```

- **If Accused:**
  ```
  1. DO NOT talk to police without lawyer
  2. DO NOT delete evidence (obstruction charge)
  3. DO NOT discuss on social media
  4. Contact lawyer immediately
  5. Preserve all communications (emails, contracts)
  ```

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

**Marcus Hutchins Case (2017)**

**Background:** Security researcher, stopped WannaCry ransomware (hero).

**What Happened:**
```
2014-2015: Created malware (Kronos banking trojan)
2017: Arrested at DEF CON (Las Vegas)
Charges: Creating and distributing malware
```

**Legal Battle:**
```
- 6 counts of computer fraud
- Potential: 40 years prison
- Bail: $30,000
- Travel restricted (US only)
- 2 years legal battle
```

**Outcome (2019):**
```
- Pleaded guilty (2 counts)
- Sentence: Time served + 1 year supervised release
- No prison time (judge considered WannaCry heroics)
```

**Lesson:**
```
❌ Past mistakes haunt you (even if reformed)
❌ "I was young" = Not valid defense
❌ Hero status ≠ Legal immunity
❌ International travel = Arrest risk

✅ Clean record essential
✅ Past activities can destroy career
✅ Legal consequences years later possible
```

**Another Example - Indian Case:**

**Scenario:** Indian student ne college website hack kiya (grades change karne ke liye).

**What Happened:**
```
- SQL injection se admin access
- Grades modify kiye (apne aur friends ke)
- Caught after 6 months (audit trail)
```

**Legal Action:**
```
FIR Filed:
- IT Act Section 66
- IPC Section 420 (Cheating)
- IPC Section 463 (Forgery)

Consequences:
- Arrested (police custody)
- Expelled from college
- Degree cancelled
- Criminal record
- 2 years jail (suspended sentence)
- ₹50,000 fine
```

**Impact:**
```
- No job (criminal record)
- No higher education (expelled)
- Family shame
- Financial burden
- Life ruined at age 21
```

**Lesson:**
```
❌ "College website" = Still crime
❌ "Just grades" = Still fraud
❌ "Everyone does it" = Not defense
❌ Young age = No immunity

Impact:
- One mistake = Lifetime consequences
- Criminal record = Career destroyed
- Family affected
- No second chances in some cases
```

### 12. **Checklist / Chota Recap (TL;DR)**

✅ Cybercrime laws strict (India: IT Act, US: CFAA, UK: CMA)  
✅ Penalties severe (jail 1-10 years, fines lakhs/millions)  
✅ "Ethical intent" = Weak defense (action matters, not intent)  
✅ Written permission essential (contract, bug bounty, email)  
✅ One mistake = Career destroyed (criminal record permanent)  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Agar accidentally unauthorized access ho gaya toh?**  
**A:** Immediately stop, back out, document everything, report to company/lawyer. "Accident" defense weak hai lekin better than continuing.

**Q2: Bug bounty mein legal protection hai?**  
**A:** Haan, lekin SIRF scope ke andar. Out of scope = no protection, same as random hacking.

**Q3: VPN use karne se safe hoon?**  
**A:** NAHI! VPN anonymity deta hai lekin legal protection nahi. Crime still crime hai, chahe pakde ya nahi.

### 14. **Practice ke liye Task**

**Task:** Legal awareness quiz:

**Question 1:**
```
Shodan par exposed database mila (no password).
Aapne connection attempt kiya (read-only).
Kya yeh legal hai?
```
**Answer:** NAHI! Unauthorized access hai, even read-only. IT Act Section 43 violation.

**Question 2:**
```
Bug bounty program: Scope = *.company.com
Aapne partner.company.com test kiya.
Kya yeh legal hai?
```
**Answer:** NAHI! Out of scope = no legal protection. Contract violation + potential criminal charges.

**Question 3:**
```
GitHub par AWS key mila.
Aapne aws s3 ls chalaya (test karne ke liye).
Kya yeh legal hai?
```
**Answer:** NAHI! Unauthorized access to AWS account. CFAA violation (US), IT Act (India).

**Question 4:**
```
Company website par SQL injection vulnerability mili.
Aapne test kiya (no data modified).
Written permission nahi tha.
Kya yeh legal hai?
```
**Answer:** NAHI! Bina permission ke testing = unauthorized access. "No damage" defense weak.

**Expected Learning:** Legal boundaries crystal clear ho jaayengi.

### 15. **Aakhri Choti Summary (5 lines)**

- ⚖️ Cybercrime laws strict (IT Act, CFAA, CMA) - jail + fines
- 🚫 "Ethical intent" = Weak defense (action matters, not motivation)
- 📝 Written permission essential (contract, scope, email)
- 💔 One mistake = Career destroyed (Aaron Swartz, Marcus Hutchins examples)
- 🛡️ Stay within boundaries (no exceptions, no "just this once")

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Cybercrime laws bahut strict hain - 'ethical intent' court mein kaam nahi aata. Ek unauthorized access se jail, fines, career khatam. Written permission zaroori, scope adherence critical. Aaron Swartz aur Marcus Hutchins ke cases yaad rakho - heroes bhi suffer karte hain!" ⚖️

---


## **Topic 3: Understanding Scope (What is it and Why it Matters)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Scope** - Pentesting/bug bounty mein kya test kar sakte ho aur kya nahi - yeh legal contract hai.

### 2. **Ye Kya Hai? (What is it?)**

**Scope** ek written document hai jo clearly define karta hai:
- **In-Scope:** Kya test kar sakte ho (domains, IPs, applications)
- **Out-of-Scope:** Kya test NAHI kar sakte (third-party, production, specific services)
- **Allowed Methods:** Kaunse attacks allowed hain (SQL injection OK, DoS NOT OK)
- **Restrictions:** Kya nahi karna (social engineering, physical access, etc.)

**Analogy:** Socho scope ek "playground" hai jismein aap khel sakte ho. Boundary ke andar = safe, bahar = danger zone. Fence cross kiya = trouble! 🏟️

### 3. **Kyun Zaroori Hai? (Why is it important?)**

- **Legal Protection:** Scope ke andar = legal, bahar = criminal.
- **Clear Boundaries:** Kya allowed hai, kya nahi - confusion nahi.
- **Client Trust:** Professional pentesters scope respect karte hain.
- **Liability:** Scope violation = no insurance coverage, personal liability.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**

- **Pentesting Contract:** Client engagement se pehle scope finalize karo.
- **Bug Bounty:** Program rules = scope (carefully padho).
- **Personal Testing:** Apni websites/apps par bhi scope define karo.
- **Team Collaboration:** Sabko scope pata hona chahiye.

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟

- **Scope Violation:** Out-of-scope testing = criminal charges.
- **Contract Breach:** Client sue kar sakta hai (damages).
- **No Payment:** Findings invalid agar out-of-scope.
- **Reputation Loss:** Industry mein blacklist.

### 6. **Syntax aur Common Options**

**Typical Scope Document:**

```
PENETRATION TESTING SCOPE

Client: TechCorp Inc
Engagement Period: Jan 1-15, 2024
Tester: [Your Name/Company]

IN-SCOPE ASSETS:
✅ Domains:
   - www.techcorp.com
   - api.techcorp.com
   - mobile.techcorp.com
   - *.staging.techcorp.com

✅ IP Ranges:
   - 203.0.113.0/24
   - 198.51.100.0/24

✅ Applications:
   - Web application (all features)
   - Mobile API
   - Admin portal

OUT-OF-SCOPE ASSETS:
❌ Domains:
   - partner.techcorp.com (third-party)
   - legacy.techcorp.com (decommissioned)
   
❌ Services:
   - Email servers (mail.techcorp.com)
   - DNS servers
   - Third-party integrations (Stripe, AWS)

ALLOWED METHODS:
✅ SQL Injection
✅ XSS (Cross-Site Scripting)
✅ CSRF
✅ Authentication bypass
✅ Authorization flaws
✅ File upload vulnerabilities
✅ API testing

RESTRICTED METHODS:
❌ Denial of Service (DoS/DDoS)
❌ Social Engineering (phishing employees)
❌ Physical access attempts
❌ Brute force (rate: max 10 req/sec)
❌ Data exfiltration (download > 100 records)

SPECIAL CONDITIONS:
⚠️ Testing Hours: 9 AM - 6 PM IST (avoid peak hours)
⚠️ Production Data: Do not modify/delete
⚠️ Notification: Alert security team before testing
⚠️ Reporting: Daily updates, final report within 7 days

EMERGENCY CONTACT:
Security Team: security@techcorp.com
Phone: +91-XXXXXXXXXX (24/7)

SIGNATURES:
Client: _________________ Date: _______
Tester: _________________ Date: _______
```

### 7. **Example 1 (Basic)**

**Scenario:** Bug bounty program scope check.

**Program Rules:**
```
BUG BOUNTY PROGRAM - TechCorp

IN SCOPE:
✅ *.techcorp.com
✅ mobile.techcorp.com
✅ api.techcorp.com

OUT OF SCOPE:
❌ blog.techcorp.com (WordPress - managed by third-party)
❌ careers.techcorp.com (Greenhouse integration)
❌ *.staging.techcorp.com (development environments)

RULES:
✅ Web vulnerabilities (SQLi, XSS, CSRF, etc.)
❌ DoS/DDoS
❌ Social engineering
❌ Spam
❌ Physical attacks
```

**Your Testing:**
```
✅ www.techcorp.com → SQL injection test (IN SCOPE)
✅ api.techcorp.com → Authentication bypass (IN SCOPE)
❌ blog.techcorp.com → WordPress plugin vuln (OUT OF SCOPE!)
❌ staging.techcorp.com → Exposed credentials (OUT OF SCOPE!)
```

**Correct Approach:**
```
1. Test only in-scope assets
2. If interesting finding on out-of-scope:
   - DO NOT test further
   - Note it down
   - Ask program if they want to know
   - Wait for permission
3. Report only in-scope findings
```

### 8. **Example 2 (Pentester-Focused)**

**Scenario:** Client pentesting engagement with scope ambiguity.

**Initial Scope:**
```
Client: FinanceApp Inc
Scope: "Test our web application"
```

**Problem:** Too vague!

**Questions to Ask:**
```
1. Specific domains/URLs?
   - www.financeapp.com only?
   - Subdomains included?
   - Mobile app?

2. IP ranges?
   - Hosting provider?
   - CDN IPs?

3. Allowed methods?
   - SQL injection OK?
   - DoS testing?
   - Social engineering?

4. Restrictions?
   - Testing hours?
   - Rate limiting?
   - Data handling?

5. Third-party services?
   - Payment gateway (Stripe)?
   - Cloud services (AWS)?
   - Analytics (Google Analytics)?
```

**Revised Scope (After Discussion):**
```
IN SCOPE:
✅ www.financeapp.com
✅ api.financeapp.com
✅ IP: 203.0.113.50-60

ALLOWED:
✅ SQL Injection
✅ XSS
✅ Authentication/Authorization testing
✅ API abuse

RESTRICTED:
❌ DoS (any form)
❌ Social engineering
❌ Brute force (max 5 attempts)
❌ Third-party services (Stripe, AWS)

OUT OF SCOPE:
❌ partner.financeapp.com
❌ blog.financeapp.com
❌ Email servers
```

**During Testing - Scope Question:**
```
Situation: api.financeapp.com redirects to api-v2.financeapp.com

Question: Is api-v2.financeapp.com in scope?

❌ WRONG: Assume yes, continue testing
✅ RIGHT: Stop, ask client, wait for confirmation

Email to Client:
"During testing, I discovered api-v2.financeapp.com.
This was not explicitly in scope.
Should I include this in testing?
Awaiting confirmation before proceeding."

Client Response: "Yes, api-v2 is in scope. Proceed."

Now: ✅ Continue testing api-v2
```

**Real Example - Scope Violation Consequences:**

**What Happened:**
```
Pentester: Testing www.company.com (in scope)
Discovery: admin.company.com link found
Action: Tested admin.company.com (NOT explicitly in scope)
Finding: SQL injection on admin.company.com
```

**Client Reaction:**
```
"admin.company.com is managed by third-party vendor.
You tested their system without permission.
This is out of scope!"
```

**Consequences:**
```
❌ Finding rejected (no payment)
❌ Contract breach (legal notice)
❌ Vendor complained (potential lawsuit)
❌ Reputation damaged (no future contracts)
❌ Insurance denied (scope violation)
```

**Lesson:**
```
❌ "Found via in-scope site" ≠ Automatically in scope
❌ Subdomain ≠ Always included
❌ Assumption = Dangerous

✅ When in doubt, ASK
✅ Get written confirmation
✅ Document everything
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**

- **Assumption:** "Subdomain hai toh scope mein hoga" - GALAT! Explicitly mentioned hona chahiye.
- **"Just Checking":** "Ek baar dekh leta hoon" out-of-scope asset par - VIOLATION!
- **Verbal Permission:** "Client ne phone par bola OK hai" - WRITTEN chahiye!

### 10. **Best Practices / Pro Tips**

- **Scope Clarity Checklist:**
  ```
  ✅ Specific domains/IPs listed
  ✅ Wildcard subdomains clarified (*.example.com means what?)
  ✅ Third-party services explicitly mentioned
  ✅ Allowed methods listed
  ✅ Restricted methods listed
  ✅ Testing hours defined
  ✅ Data handling rules
  ✅ Emergency contacts
  ✅ Reporting timeline
  ✅ Signatures (both parties)
  ```

- **During Testing:**
  ```
  ✅ Keep scope document handy
  ✅ When in doubt, STOP and ASK
  ✅ Document all communications
  ✅ Get written confirmation for changes
  ✅ Never assume
  ```

- **Scope Expansion:**
  ```
  If you discover interesting out-of-scope asset:
  
  1. STOP testing immediately
  2. Document discovery (screenshot, URL)
  3. Email client:
     "Discovered [asset] during in-scope testing.
      Currently out of scope.
      Would you like to expand scope to include this?
      Awaiting written confirmation."
  4. Wait for response
  5. If approved: Get updated scope document
  6. Then proceed
  ```

- **Red Flags (Scope Issues):**
  ```
  🚨 Vague scope ("test our website")
  🚨 No written document
  🚨 Verbal-only permissions
  🚨 Client says "test everything"
  🚨 No restrictions mentioned
  🚨 No signatures
  ```

### 11. **Asli Duniya ka Scenario (Real-World Pentest Scenario)**

**Case Study 1: Scope Saved Career**

**Scenario:** Pentester testing e-commerce site.

**Scope:**
```
IN SCOPE:
✅ www.shop.com
✅ api.shop.com

OUT OF SCOPE:
❌ payment.shop.com (Stripe integration)
```

**During Testing:**
```
Step 1: Testing www.shop.com checkout
Step 2: Checkout redirects to payment.shop.com
Step 3: Pentester notices: payment.shop.com has SQL injection!
```

**Decision Point:**
```
Option A: Test SQL injection (it's right there!)
Option B: Stop, ask client

Pentester chose: Option B ✅
```

**Email to Client:**
```
"During checkout testing, I was redirected to payment.shop.com.
I noticed potential SQL injection vulnerability.
However, payment.shop.com is out of scope.

Should I:
A) Include in scope and test?
B) Note finding but not test?
C) Ignore completely?

Awaiting guidance."
```

**Client Response:**
```
"payment.shop.com is Stripe's hosted page, not ours.
Thank you for asking!
Please do NOT test - it's Stripe's infrastructure.
We'll report to Stripe directly."
```

**Outcome:**
```
✅ Scope respected
✅ Client impressed (professionalism)
✅ Avoided legal issue (testing Stripe = big problem!)
✅ Future contracts secured
✅ Reputation enhanced
```

**What if Option A chosen?**
```
❌ Testing Stripe infrastructure = Unauthorized access
❌ Stripe legal team involved
❌ Client sued pentester (contract breach)
❌ Criminal charges possible
❌ Career destroyed
```

**Lesson: Scope adherence saved career! 🛡️**

**Case Study 2: Scope Violation Disaster**

**Scenario:** Bug bounty hunter testing "CompanyX".

**Program Scope:**
```
IN SCOPE:
✅ *.companyx.com

OUT OF SCOPE:
❌ Third-party services
❌ Acquisitions (acquired companies)
```

**What Happened:**
```
Step 1: Testing www.companyx.com
Step 2: Found link to subsidiary.com (acquired company)
Step 3: Assumed: "CompanyX owns it, must be in scope"
Step 4: Tested subsidiary.com
Step 5: Found critical vulnerability
Step 6: Reported to CompanyX
```

**Company Response:**
```
"subsidiary.com is separate legal entity.
Different bug bounty program.
You tested without permission.
This is out of scope violation."
```

**Consequences:**
```
❌ Report rejected (no bounty)
❌ Account banned (HackerOne)
❌ Blacklisted (all programs)
❌ subsidiary.com filed complaint
❌ Legal notice received
```

**Researcher's Defense:**
```
"But CompanyX owns subsidiary.com!"
"Link was on CompanyX website!"
"I thought it was in scope!"
```

**Reality:**
```
❌ Ownership ≠ Scope
❌ Link ≠ Permission
❌ Assumption ≠ Authorization
```

**Outcome:**
```
- Career in bug bounty ended
- Legal fees: $10,000+
- Settlement: $5,000 to subsidiary.com
- Reputation destroyed
- No security jobs (blacklisted)
```

**Lesson: One scope violation = Career destroyed! 💔**

### 12. **Checklist / Chota Recap (TL;DR)**

✅ Scope = Written contract (in-scope, out-of-scope, methods, restrictions)  
✅ Explicit mention zaroori (assumption = dangerous)  
✅ When in doubt, ASK (stop, email, wait for written confirmation)  
✅ Scope violation = No legal protection (criminal charges possible)  
✅ Document everything (emails, confirmations, scope changes)  

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Agar scope mein "*.example.com" hai toh kya sab subdomains included hain?**  
**A:** Usually haan, lekin clarify karo. Kuch companies third-party subdomains exclude karte hain. Written confirmation lo.

**Q2: In-scope site se link mila out-of-scope site ka, kya test kar sakta hoon?**  
**A:** NAHI! Link ≠ Permission. Stop, ask client, wait for confirmation.

**Q3: Verbal permission enough hai scope change ke liye?**  
**A:** NAHI! Hamesha written confirmation (email, updated scope document). Verbal = No legal protection.

### 14. **Practice ke liye Task**

**Task:** Scope analysis practice:

**Scenario 1:**
```
Scope: *.company.com
Discovery: partner.company.com (third-party managed)
Question: Test karna chahiye?
```
**Answer:** NAHI! Third-party = likely out of scope. Ask client first.

**Scenario 2:**
```
Scope: www.company.com
Discovery: api.company.com (via JavaScript)
Question: Test karna chahiye?
```
**Answer:** NAHI! api.company.com explicitly mentioned nahi. Ask client.

**Scenario 3:**
```
Scope: www.company.com, api.company.com
Discovery: www.company.com redirects to new-site.company.com
Question: Test karna chahiye?
```
**Answer:** STOP! Redirect ≠ Scope inclusion. Ask client about new-site.company.com.

**Scenario 4:**
```
Scope: *.company.com
Discovery: blog.company.com (WordPress, third-party hosted)
Question: Test karna chahiye?
```
**Answer:** ASK! Wildcard includes it technically, but third-party hosting = potential issue.

**Expected Learning:** Scope ambiguities identify karna aur safe decisions lena.

### 15. **Aakhri Choti Summary (5 lines)**

- 📋 Scope = Legal contract (in-scope, out-of-scope, methods, restrictions)
- ✍️ Written document essential (verbal = no protection)
- ❓ When in doubt, ASK (stop, email, wait for confirmation)
- 🚫 Scope violation = Criminal charges (no "I thought" defense)
- 📧 Document everything (emails, confirmations, scope changes)

> **📌 Ye Zaroor Yaad Rakhein:**  
> "Scope pentester ka 'safety net' hai - iske andar = legal, bahar = criminal. Assumption mat karo, clarification maango. Ek scope violation se career khatam - Case Study 2 yaad rakho. 'When in doubt, ASK' - yeh mantra hai!" 🛡️

---

# **🎓 Module 9 Complete! FINAL MODULE! 🎉**

Aapne **OSINT Ethics & Legal Boundaries** master kar liye! Ab aap:
- ✅ "Look, Don't Touch" rule samajhte ho (viewing vs accessing)
- ✅ Legal risks jaante ho (IT Act, CFAA, penalties)
- ✅ Scope importance samajhte ho (in-scope vs out-of-scope)
- ✅ Ethical hacker ban sakte ho (professional, legal, safe)

**Module 9 Mastery Checklist:**
- ✅ Legal vs illegal actions clearly defined
- ✅ Cybercrime laws awareness (India, US, UK)
- ✅ Scope adherence (contract, boundaries, clarifications)
- ✅ Responsible disclosure process
- ✅ Career protection strategies

**Key Takeaways:**
- "Look, Don't Touch" = Golden rule (search legal, access illegal)
- Cybercrime laws strict = Jail + fines (no "ethical intent" defense)
- Scope = Legal contract (violation = criminal charges)
- Written permission essential = Verbal nahi, document chahiye
- One mistake = Career destroyed (Aaron Swartz, Marcus Hutchins, Case Studies)

**Real-World Lessons:**
- Aaron Swartz: "Good intentions" ≠ Legal defense (tragic outcome)
- Marcus Hutchins: Past mistakes haunt (even heroes suffer)
- Andrew Auernheimer: Automated scraping = Federal crime
- Case Study 1: Scope adherence saved career
- Case Study 2: Scope violation destroyed career

**Ethical Hacker Checklist:**
```
✅ Always get written permission
✅ Define scope clearly (in-scope, out-of-scope)
✅ Follow "Look, Don't Touch" rule
✅ When in doubt, STOP and ASK
✅ Document everything (emails, confirmations)
✅ Responsible disclosure (private, not public)
✅ Respect boundaries (no exceptions)
✅ Professional conduct (reputation matters)
✅ Legal consultation (when needed)
✅ Continuous learning (laws change)
```

---

# **🎊 COMPLETE COURSE FINISHED! ALL 9 MODULES! 🎊**

**Congratulations!** Aapne **OSINT & Dorking: Zero-to-Hacker** course complete kar liya!

**All Modules Completed:**
1. ✅ Module 1: Basic Search Operators (Google Foundation)
2. ✅ Module 2: Core Dorking Operators (site, inurl, intitle, intext, filetype)
3. ✅ Module 3: Advanced Google Operators (cache, related, link, info)
4. ✅ Module 4: Practical Hacking & Databases (GHDB, login pages, sensitive files)
5. ✅ Module 5: Beyond Google (Bing, ip:, contains:)
6. ✅ Module 6: Shodan (IoT & Device Search Engine)
7. ✅ Module 7: GitHub & Data Leak Dorking (keys, passwords, Pastebin)
8. ✅ Module 8: Advanced Recon Techniques (Wayback, Human OSINT, Metadata, Censys)
9. ✅ Module 9: OSINT Ethics & Legal Boundaries (Look Don't Touch, Laws, Scope)

**Total Topics Covered:** 30+ topics with 15-point format each!

**Skills Acquired:**
- 🔍 Google Dorking (basic to advanced)
- 🌐 Multi-engine search (Google, Bing, Shodan, Censys, ZoomEye)
- 🔑 Credential hunting (GitHub, Pastebin, leaked keys)
- 📡 Device discovery (Shodan, IoT, ICS/SCADA)
- 🕰️ Historical intelligence (Wayback Machine)
- 👥 Human OSINT (LinkedIn, job postings, metadata)
- ⚖️ Ethical hacking (legal boundaries, scope, responsible disclosure)

**Real-World Examples:**
- 💰 Uber breach ($148M fine)
- 🚗 Toyota breach (300K customers)
- 💳 Target breach (40M credit cards)
- 🏦 Capital One breach (100M customers)
- 📱 LinkedIn breach (700M users)
- 💔 Aaron Swartz tragedy
- 🏆 Marcus Hutchins case

**Tools Mastered:**
- Google, Bing, DuckDuckGo
- Shodan, Censys, ZoomEye
- GitHub, Pastebin
- Wayback Machine
- ExifTool, FOCA, Metagoofil
- TruffleHog, GitLeaks
- theHarvester, PasteHunter

**Next Steps:**
1. **Practice Daily:** Har module ke practice tasks complete karo
2. **Build Portfolio:** Ethical findings document karo (anonymized)
3. **Bug Bounty:** HackerOne, Bugcrowd par start karo (small programs)
4. **Certifications:** CEH, OSCP, GPEN consider karo
5. **Community:** Twitter, Discord, Reddit - security community join karo
6. **Continuous Learning:** New tools, techniques, CVEs - updated raho

**Final Advice:**
```
🛡️ Hamesha ethical raho
📝 Written permission zaroori
🚫 "Look, Don't Touch" rule sacred hai
📧 Responsible disclosure follow karo
⚖️ Legal boundaries respect karo
💪 Practice makes perfect
🎯 Start small, grow gradually
🤝 Community se seekho
📚 Never stop learning
❤️ Passion + Ethics = Success
```

**Remember:**
> **"With great power comes great responsibility. Aapke paas ab powerful skills hain - inhe ethical use karo. Ek galat decision se career khatam, lekin ethical use se hero ban sakte ho. Choice tumhari hai!"** 🦸

**Thank You for Learning!** 🙏

Aap ab OSINT & Dorking expert ho! Go forth and hack ethically! 🚀

**Questions? Doubts? Practice Issues?**
Keep learning, keep practicing, stay ethical! 💪

---

**Course Complete! 🎓**
**From Zero to Hacker - Ethically! 🔐**

---
=============================================================