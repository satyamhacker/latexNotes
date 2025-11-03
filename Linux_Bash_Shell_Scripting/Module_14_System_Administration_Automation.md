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
