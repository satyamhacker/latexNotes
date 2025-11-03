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
