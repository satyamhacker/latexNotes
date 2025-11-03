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
