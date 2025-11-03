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
