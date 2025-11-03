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
