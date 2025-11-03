# **Bash Shell Scripting: Zero-to-Automation Notes (Module 9)**

---

## **PART 3: BUILDING REAL SCRIPTS**

---

# **Module 9: Script Parameters & Expansion**

---

## **Topic 1: Positional Parameters (`$1`, `$2`, ... `${10}`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Positional Parameters** - Script ko command-line arguments pass karna.

### 2. **Ye Kya Hai? (What is it?)**
Positional parameters woh values hain jo script ko run karte waqt pass ki jaati hain. `$1` pehla argument, `$2` doosra, etc. `$0` script ka naam hota hai.

**Analogy:** Socho ki script ek function hai aur positional parameters uske arguments hain - jaise function ko values pass karte hain, waise hi script ko.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Flexibility** - Dynamic input
- ✅ **Reusability** - Same script, different inputs
- ✅ **Automation** - Command-line tools
- ✅ **Professional scripts** - Industry standard

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Script ko flexible banana ho
- User input chahiye
- Command-line tools banate waqt
- Automation scripts mein

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Hardcoded values (inflexible)
- Script reusable nahi hogi
- Professional tools nahi bana paoge
- Automation limited

### 6. **Syntax aur Common Options**

```bash
# Positional parameters
$0    # Script name
$1    # First argument
$2    # Second argument
${10} # 10th argument (braces needed for 10+)

# Special parameters
$#    # Number of arguments
$@    # All arguments (as separate)
$*    # All arguments (as single string)
$?    # Exit status of last command
$$    # Current process ID
$!    # PID of last background job
```

### 7. **Example 1 (Basic)**

```bash
#!/bin/bash
# greeting.sh

echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "Total arguments: $#"
echo "All arguments: $@"

# Usage: ./greeting.sh Alice Bob
# Output:
# Script name: ./greeting.sh
# First argument: Alice
# Second argument: Bob
# Total arguments: 2
# All arguments: Alice Bob
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# backup.sh - Flexible backup script

SOURCE=$1
DEST=$2
DATE=$(date +%Y%m%d_%H%M%S)

# Validate arguments
if [ $# -lt 2 ]; then
    echo "Usage: $0 <source> <destination>"
    echo "Example: $0 /home/user /backups"
    exit 1
fi

# Validate source
if [ ! -d "$SOURCE" ]; then
    echo "Error: Source directory not found: $SOURCE"
    exit 1
fi

# Create destination
mkdir -p "$DEST"

# Backup
BACKUP_FILE="$DEST/backup_${DATE}.tar.gz"
echo "Backing up $SOURCE to $BACKUP_FILE"

if tar -czf "$BACKUP_FILE" "$SOURCE" 2>/dev/null; then
    SIZE=$(du -h "$BACKUP_FILE" | cut -f1)
    echo "✓ Backup successful: $SIZE"
else
    echo "✗ Backup failed"
    exit 1
fi

# Optional: compression level
if [ -n "$3" ]; then
    echo "Compression level: $3"
fi
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Quotes bhoolna:** `$1` ki jagah `"$1"` safe
- ❌ **Validation nahi:** Arguments check karo
- ❌ **10+ arguments:** `$10` galat, `${10}` sahi

### 10. **Best Practices / Pro Tips**
- 💡 **Hamesha validate:** `$#` se count check karo
- 💡 **Quotes use karo:** `"$1"` safe hai
- 💡 **Usage function:** Help message banao
- 💡 **Meaningful names:** Variables mein store karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# deploy.sh - Deployment script

APP_NAME=$1
ENVIRONMENT=$2
VERSION=${3:-latest}

usage() {
    cat << EOF
Usage: $0 <app-name> <environment> [version]

Arguments:
  app-name      Application name
  environment   dev|staging|prod
  version       Version to deploy (default: latest)

Examples:
  $0 myapp dev
  $0 myapp prod v2.1.0
EOF
    exit 1
}

# Validate
[ $# -lt 2 ] && usage

case $ENVIRONMENT in
    dev|staging|prod)
        echo "Deploying $APP_NAME to $ENVIRONMENT (version: $VERSION)"
        ;;
    *)
        echo "Error: Invalid environment: $ENVIRONMENT"
        usage
        ;;
esac

# Deploy logic here
echo "✓ Deployment complete"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `$1, $2, $3` - Arguments
- ✅ `$0` - Script name
- ✅ `$#` - Argument count
- ✅ `$@` - All arguments
- ✅ Validate hamesha

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `$@` aur `$*` mein kya fark hai?**
A: `"$@"` har argument alag, `"$*"` sab ek string mein.

**Q2: 10+ arguments kaise access karu?**
A: Braces use karo: `${10}`, `${11}`, etc.

**Q3: Default value kaise set karu?**
A: `${1:-default}` syntax use karo.

### 14. **Practice ke liye Task**

```bash
#!/bin/bash
# test_args.sh

echo "Script: $0"
echo "Args: $#"
echo "First: $1"
echo "Second: $2"
echo "All: $@"

# Run: ./test_args.sh hello world
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📥 `$1, $2` command-line arguments
- 🔢 `$#` argument count
- 📋 `$@` all arguments
- ✅ Hamesha validate karo
- 💬 Quotes use karo: `"$1"`

> **💡 Ye Zaroor Yaad Rakhein:**
> Positional parameters scripts ko flexible banate hain! Hamesha validate karo (`$#`), quotes use karo (`"$1"`), aur usage function banao!

---

## **Topic 2: Professional Argument Parsing (`getopts`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**getopts** - Professional command-line options parsing.

### 2. **Ye Kya Hai? (What is it?)**
`getopts` ek built-in command hai jo Unix-style options (`-a`, `-b value`) parse karta hai. Yeh professional scripts ka standard hai.

**Analogy:** Socho ki getopts ek receptionist hai jo forms check karta hai - kaunse fields filled hain, kaunse required hain, kaunse optional.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Professional** - Industry standard
- ✅ **Flexible** - Options in any order
- ✅ **Error handling** - Invalid options detect
- ✅ **User-friendly** - `-h` for help

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Professional scripts
- Multiple options chahiye
- Optional parameters
- Command-line tools

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Manual parsing (error-prone)
- Inflexible scripts
- Poor user experience
- Non-standard tools

### 6. **Syntax aur Common Options**

```bash
while getopts "abc:d:" opt; do
    case $opt in
        a) # Flag without value ;;
        b) # Flag without value ;;
        c) # Option with value: $OPTARG ;;
        d) # Option with value: $OPTARG ;;
        \?) # Invalid option ;;
    esac
done

shift $((OPTIND-1))  # Remove processed options
```

**Format:**
- `a` - Flag (no value)
- `a:` - Option (requires value)
- `:abc:` - Leading `:` for silent errors

### 7. **Example 1 (Basic)**

```bash
#!/bin/bash

while getopts "hvf:" opt; do
    case $opt in
        h)
            echo "Usage: $0 [-h] [-v] [-f file]"
            exit 0
            ;;
        v)
            VERBOSE=true
            ;;
        f)
            FILE=$OPTARG
            ;;
        \?)
            echo "Invalid option: -$OPTARG"
            exit 1
            ;;
    esac
done

echo "Verbose: ${VERBOSE:-false}"
echo "File: ${FILE:-none}"
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# backup.sh - Professional backup script

usage() {
    cat << EOF
Usage: $0 [OPTIONS]

Options:
  -s SOURCE     Source directory (required)
  -d DEST       Destination directory (required)
  -c LEVEL      Compression level (1-9, default: 6)
  -e            Encrypt backup
  -v            Verbose output
  -h            Show this help

Examples:
  $0 -s /home -d /backups
  $0 -s /data -d /backups -c 9 -e -v
EOF
    exit 1
}

# Defaults
COMPRESSION=6
ENCRYPT=false
VERBOSE=false

# Parse options
while getopts "s:d:c:evh" opt; do
    case $opt in
        s) SOURCE=$OPTARG ;;
        d) DEST=$OPTARG ;;
        c) COMPRESSION=$OPTARG ;;
        e) ENCRYPT=true ;;
        v) VERBOSE=true ;;
        h) usage ;;
        \?)
            echo "Error: Invalid option -$OPTARG"
            usage
            ;;
        :)
            echo "Error: Option -$OPTARG requires argument"
            usage
            ;;
    esac
done

# Validate required
if [ -z "$SOURCE" ] || [ -z "$DEST" ]; then
    echo "Error: Source and destination required"
    usage
fi

# Validate compression
if [ "$COMPRESSION" -lt 1 ] || [ "$COMPRESSION" -gt 9 ]; then
    echo "Error: Compression must be 1-9"
    exit 1
fi

# Execute
[ "$VERBOSE" = true ] && echo "Source: $SOURCE"
[ "$VERBOSE" = true ] && echo "Dest: $DEST"
[ "$VERBOSE" = true ] && echo "Compression: $COMPRESSION"

BACKUP_FILE="$DEST/backup_$(date +%Y%m%d_%H%M%S).tar.gz"

if tar -czf "$BACKUP_FILE" "$SOURCE"; then
    [ "$VERBOSE" = true ] && echo "✓ Backup created"
    
    if [ "$ENCRYPT" = true ]; then
        [ "$VERBOSE" = true ] && echo "Encrypting..."
        gpg -c "$BACKUP_FILE"
        rm "$BACKUP_FILE"
        [ "$VERBOSE" = true ] && echo "✓ Encrypted"
    fi
    
    echo "✓ Complete: $BACKUP_FILE"
else
    echo "✗ Backup failed"
    exit 1
fi
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`:` bhoolna:** `a:` value ke liye zaroori
- ❌ **`$OPTARG` nahi use karna:** Value access karne ke liye
- ❌ **`shift` bhoolna:** Remaining args ke liye

### 10. **Best Practices / Pro Tips**
- 💡 **Usage function:** `-h` hamesha implement karo
- 💡 **Validation:** Required options check karo
- 💡 **Silent mode:** Leading `:` use karo
- 💡 **shift:** `shift $((OPTIND-1))` remaining args ke liye

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# deploy.sh - Production deployment

usage() {
    cat << EOF
Usage: $0 -e ENV -a APP [OPTIONS]

Required:
  -e ENV        Environment (dev|staging|prod)
  -a APP        Application name

Optional:
  -v VERSION    Version (default: latest)
  -r            Rollback mode
  -f            Force deployment
  -n            Dry run
  -h            Help

Examples:
  $0 -e prod -a myapp
  $0 -e staging -a myapp -v v2.1.0 -n
EOF
    exit 1
}

# Defaults
VERSION="latest"
ROLLBACK=false
FORCE=false
DRY_RUN=false

while getopts "e:a:v:rfnh" opt; do
    case $opt in
        e) ENVIRONMENT=$OPTARG ;;
        a) APP_NAME=$OPTARG ;;
        v) VERSION=$OPTARG ;;
        r) ROLLBACK=true ;;
        f) FORCE=true ;;
        n) DRY_RUN=true ;;
        h) usage ;;
        \?) usage ;;
    esac
done

# Validate
[ -z "$ENVIRONMENT" ] && { echo "Error: Environment required"; usage; }
[ -z "$APP_NAME" ] && { echo "Error: App name required"; usage; }

# Production safety
if [ "$ENVIRONMENT" = "prod" ] && [ "$FORCE" = false ]; then
    read -p "Deploy to PRODUCTION? (yes/no): " confirm
    [ "$confirm" != "yes" ] && exit 0
fi

# Deploy
echo "Deploying $APP_NAME to $ENVIRONMENT (version: $VERSION)"
[ "$DRY_RUN" = true ] && echo "[DRY RUN]" && exit 0

# Actual deployment logic
echo "✓ Deployment complete"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `getopts "abc:" opt` - Parse options
- ✅ `a:` requires value
- ✅ `$OPTARG` - Option value
- ✅ `shift $((OPTIND-1))` - Remaining args
- ✅ Usage function zaroori

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Long options (`--help`) kaise handle karu?**
A: `getopts` sirf short options. Long ke liye manual parsing ya `getopt` (external).

**Q2: Required options kaise enforce karu?**
A: Parse ke baad check karo: `[ -z "$VAR" ] && usage`

**Q3: Multiple values ek option mein?**
A: Array use karo ya comma-separated parse karo.

### 14. **Practice ke liye Task**

```bash
#!/bin/bash
# test_getopts.sh

while getopts "hvf:o:" opt; do
    case $opt in
        h) echo "Help" ;;
        v) VERBOSE=true ;;
        f) FILE=$OPTARG ;;
        o) OUTPUT=$OPTARG ;;
        \?) exit 1 ;;
    esac
done

echo "Verbose: ${VERBOSE:-false}"
echo "File: ${FILE:-none}"
echo "Output: ${OUTPUT:-none}"

# Run: ./test_getopts.sh -v -f input.txt -o output.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🎯 Professional option parsing
- 📝 `a:` value chahiye, `a` flag
- 💼 `$OPTARG` value access
- ✅ Usage function mandatory
- 🔧 Industry standard tool

> **💡 Ye Zaroor Yaad Rakhein:**
> getopts professional scripts ka standard hai! Usage function banao, required options validate karo, aur `-h` help hamesha implement karo!

---

## **Topic 3: Brace Expansion (`file{1,2,3}.txt`, `echo {a,b,c}-{1,2,3}`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Brace Expansion** - Multiple strings automatically generate karna.

### 2. **Ye Kya Hai? (What is it?)**
Brace expansion ek shorthand hai jo multiple strings generate karta hai. `{a,b,c}` expand hokar `a b c` ban jaata hai. Yeh file creation, loops, aur batch operations ke liye powerful hai.

**Analogy:** Socho ki brace expansion ek copy machine hai jo ek template se multiple copies banata hai - har copy mein thoda variation.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Efficiency** - Multiple items quickly
- ✅ **Batch operations** - Files, directories
- ✅ **Ranges** - Numbers, letters
- ✅ **Combinations** - Cartesian product

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Multiple files banana ho
- Ranges generate karni hon
- Batch operations
- Directory structures

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Manual repetition
- Verbose commands
- Time waste
- Error-prone

### 6. **Syntax aur Common Options**

```bash
# List expansion
{a,b,c}           # a b c

# Range expansion
{1..10}           # 1 2 3 ... 10
{a..z}            # a b c ... z

# Step
{1..10..2}        # 1 3 5 7 9

# Combinations
{a,b}{1,2}        # a1 a2 b1 b2

# Nested
{a,b{1,2}}        # a b1 b2
```

### 7. **Example 1 (Basic)**

```bash
# Create multiple files
touch file{1,2,3}.txt
# Creates: file1.txt file2.txt file3.txt

# Create range
touch file{1..5}.txt
# Creates: file1.txt file2.txt ... file5.txt

# Combinations
echo {a,b,c}-{1,2,3}
# Output: a-1 a-2 a-3 b-1 b-2 b-3 c-1 c-2 c-3

# Directory structure
mkdir -p project/{src,test,docs}
# Creates: project/src project/test project/docs

# Backup
cp config.conf{,.backup}
# Same as: cp config.conf config.conf.backup
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Project structure creator

create_project() {
    local name=$1
    
    echo "Creating project: $name"
    
    # Main structure
    mkdir -p "$name"/{src,test,docs,config}
    
    # Source subdirectories
    mkdir -p "$name"/src/{controllers,models,views,utils}
    
    # Test subdirectories
    mkdir -p "$name"/test/{unit,integration,e2e}
    
    # Config files
    touch "$name"/config/{dev,staging,prod}.conf
    
    # Documentation
    touch "$name"/docs/{README,API,INSTALL}.md
    
    # Source files
    touch "$name"/src/controllers/{user,auth,admin}.js
    touch "$name"/src/models/{user,post,comment}.js
    
    echo "✓ Project structure created"
    tree "$name"
}

# Batch file operations
batch_rename() {
    # Rename file1.txt to file001.txt, etc.
    for i in {1..100}; do
        old="file${i}.txt"
        new="file$(printf "%03d" $i).txt"
        [ -f "$old" ] && mv "$old" "$new"
    done
}

# Generate test data
generate_test_files() {
    # Create test files with different extensions
    for ext in {txt,log,csv,json}; do
        for i in {1..5}; do
            echo "Test data" > "test_${i}.${ext}"
        done
    done
}

# Backup multiple configs
backup_configs() {
    local date=$(date +%Y%m%d)
    
    for config in {database,server,app}.conf; do
        if [ -f "$config" ]; then
            cp "$config" "${config}.${date}.backup"
            echo "✓ Backed up: $config"
        fi
    done
}

create_project "myapp"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Spaces dena:** `{a, b, c}` galat, `{a,b,c}` sahi
- ❌ **Variables use karna:** `{$a..$b}` kaam nahi karega
- ❌ **Quotes:** `"{1..5}"` expand nahi hoga

### 10. **Best Practices / Pro Tips**
- 💡 **No spaces:** Commas ke paas spaces nahi
- 💡 **Ranges:** `{1..100}` efficient hai
- 💡 **Combinations:** Multiple braces powerful
- 💡 **Backup trick:** `file{,.bak}` quick backup

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Multi-environment deployment

deploy_configs() {
    local app=$1
    
    # Create environment configs
    for env in {dev,staging,prod}; do
        cat > "${app}_${env}.conf" << EOF
[${env}]
app_name=${app}
environment=${env}
debug=$( [ "$env" = "prod" ] && echo "false" || echo "true" )
EOF
        echo "✓ Created: ${app}_${env}.conf"
    done
}

# Setup monitoring for multiple servers
setup_monitoring() {
    for server in web{1..5} db{1..2} cache{1..3}; do
        echo "Setting up monitoring for: $server"
        
        # Create monitoring config
        cat > "/etc/monitoring/${server}.conf" << EOF
[server]
name=${server}
check_interval=60
alerts=true
EOF
    done
}

# Batch image processing
process_images() {
    # Process images in multiple formats and sizes
    for img in photo{1..10}.jpg; do
        [ -f "$img" ] || continue
        
        for size in {thumb,medium,large}; do
            case $size in
                thumb)  convert "$img" -resize 150x150 "${img%.jpg}_${size}.jpg" ;;
                medium) convert "$img" -resize 800x600 "${img%.jpg}_${size}.jpg" ;;
                large)  convert "$img" -resize 1920x1080 "${img%.jpg}_${size}.jpg" ;;
            esac
        done
    done
}

deploy_configs "myapp"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `{a,b,c}` list expansion
- ✅ `{1..10}` range expansion
- ✅ `{1..10..2}` step expansion
- ✅ `{a,b}{1,2}` combinations
- ✅ No spaces, no quotes

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Variables use kar sakte hain?**
A: Nahi directly. `eval` use karo ya `seq` command.

**Q2: Kya nested braces kaam karte hain?**
A: Haan! `{a,b{1,2}}` → `a b1 b2`

**Q3: Leading zeros kaise add karu?**
A: `{01..10}` automatically add karega.

### 14. **Practice ke liye Task**

```bash
# 1. Create files
touch file{1..5}.txt

# 2. Create directories
mkdir -p dir{A,B,C}

# 3. Combinations
echo {red,green,blue}-{light,dark}

# 4. Range with step
echo {0..100..10}

# 5. Backup
cp important.conf{,.backup}

# 6. Project structure
mkdir -p project/{src,test}/{js,css,html}

# 7. Cleanup
rm file{1..5}.txt
rm -r dir{A,B,C} project
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔢 `{1..10}` ranges generate
- 📝 `{a,b,c}` lists expand
- 🔄 `{a,b}{1,2}` combinations
- 📁 Directory structures quickly
- ⚡ Efficient aur powerful

> **💡 Ye Zaroor Yaad Rakhein:**
> Brace expansion time-saver hai! No spaces, ranges powerful hain, combinations se multiple items quickly generate karo. `file{,.bak}` backup trick yaad rakho!

---

# **🎉 Module 9 Complete! 🎉**

Congratulations! Aapne **Module 9: Script Parameters & Expansion** successfully complete kar liya hai!

## **Aapne Kya Seekha:**
✅ **Positional Parameters** - `$1, $2, $#, $@`
✅ **getopts** - Professional option parsing
✅ **Brace Expansion** - `{1..10}`, `{a,b,c}`

## **Key Patterns:**

```bash
# Positional parameters
SOURCE=$1
DEST=$2
[ $# -lt 2 ] && echo "Usage: $0 <source> <dest>" && exit 1

# getopts
while getopts "hvf:o:" opt; do
    case $opt in
        h) usage ;;
        v) VERBOSE=true ;;
        f) FILE=$OPTARG ;;
        o) OUTPUT=$OPTARG ;;
    esac
done

# Brace expansion
touch file{1..10}.txt
mkdir -p project/{src,test,docs}
cp config{,.backup}
```

## **Real-World Applications:**
- Command-line tools
- Deployment scripts
- Batch operations
- Project scaffolding
- Configuration management

## **Best Practices:**
- Always validate arguments
- Implement usage/help function
- Use getopts for options
- Quote variables: `"$1"`
- Brace expansion for efficiency

## **Next Steps:**
Ab aap ready hain **Module 10: Functions & Arrays** ke liye!

---
