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
