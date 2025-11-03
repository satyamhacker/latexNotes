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
