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
