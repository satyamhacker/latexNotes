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
