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
