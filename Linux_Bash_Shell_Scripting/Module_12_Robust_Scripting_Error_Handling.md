# **Bash Shell Scripting: Zero-to-Automation Notes (Module 12)**

---

## **PART 3: BUILDING REAL SCRIPTS**

---

# **Module 12: Robust Scripting & Error Handling**

---

## **Topic 1: Exit Status (`$?`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Exit Status** - Har command ka return code jo success ya failure batata hai.

### 2. **Ye Kya Hai? (What is it?)**
Exit status ek number hai (0-255) jo har command execute hone ke baad return hota hai. `$?` special variable hai jo last command ka exit status store karta hai. `0` matlab success, non-zero matlab error.

**Analogy:** Exit status ek report card hai - 0 matlab pass (success), koi bhi aur number matlab fail (error with specific reason).

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Error detection** - Command success/failure check
- ✅ **Flow control** - Conditional execution
- ✅ **Debugging** - Problem identification
- ✅ **Automation** - Reliable scripts

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Command success verify karna
- Error handling logic
- Conditional execution
- Script debugging

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Silent failures
- Unreliable scripts
- Data corruption
- Production issues

### 6. **Syntax aur Common Options**

```bash
# Check exit status
command
echo $?

# Common exit codes
0     # Success
1     # General error
2     # Misuse of shell command
126   # Command cannot execute
127   # Command not found
130   # Terminated by Ctrl+C
```

### 7. **Example 1 (Basic)**

```bash
# Success case
ls /home
echo $?
# Output: 0

# Failure case
ls /nonexistent
echo $?
# Output: 2

# Using in conditions
if ls /home > /dev/null 2>&1; then
    echo "Directory exists"
else
    echo "Directory not found"
fi

# Check and act
grep "pattern" file.txt
if [ $? -eq 0 ]; then
    echo "Pattern found"
else
    echo "Pattern not found"
fi
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Robust script with exit status checking

set -euo pipefail

readonly LOG_FILE="/var/log/backup.log"
readonly BACKUP_DIR="/backups"

log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

check_status() {
    local status=$?
    local command=$1
    
    if [ $status -eq 0 ]; then
        log_message "✓ $command succeeded"
        return 0
    else
        log_message "✗ $command failed with exit code: $status"
        return $status
    fi
}

# Backup function with status checking
backup_database() {
    local db_name=$1
    local backup_file="$BACKUP_DIR/${db_name}_$(date +%Y%m%d).sql.gz"
    
    log_message "Starting backup of $db_name..."
    
    # Attempt backup
    mysqldump "$db_name" | gzip > "$backup_file"
    check_status "Database backup"
    
    # Verify backup file
    if [ -f "$backup_file" ] && [ -s "$backup_file" ]; then
        log_message "✓ Backup file created: $backup_file"
        return 0
    else
        log_message "✗ Backup file verification failed"
        return 1
    fi
}

# Main execution
main() {
    # Check prerequisites
    command -v mysqldump >/dev/null 2>&1
    if [ $? -ne 0 ]; then
        log_message "✗ mysqldump not found"
        exit 127
    fi
    
    # Create backup directory
    mkdir -p "$BACKUP_DIR"
    check_status "Create backup directory" || exit 1
    
    # Perform backups
    for db in db1 db2 db3; do
        backup_database "$db"
        local result=$?
        
        if [ $result -ne 0 ]; then
            log_message "⚠️  Backup failed for $db, continuing..."
        fi
    done
    
    log_message "Backup process completed"
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`$?` overwrite:** Next command se pehle save karo
- ❌ **Ignore karna:** Hamesha check karo critical commands
- ❌ **Wrong comparison:** `[ $? -eq 0 ]` use karo, not `[ $? == 0 ]`

### 10. **Best Practices / Pro Tips**
- 💡 **Immediately check:** `$?` next command se overwrite hota hai
- 💡 **Save if needed:** `status=$?` pehle save karo
- 💡 **Use `set -e`:** Auto-exit on error
- 💡 **Meaningful codes:** Different errors ke liye different codes

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Production deployment script with comprehensive error checking

set -euo pipefail

readonly APP_NAME="myapp"
readonly DEPLOY_DIR="/var/www/$APP_NAME"
readonly BACKUP_DIR="/backups/$APP_NAME"

deploy() {
    echo "Starting deployment..."
    
    # Backup current version
    echo "Creating backup..."
    tar -czf "$BACKUP_DIR/backup_$(date +%Y%m%d_%H%M%S).tar.gz" "$DEPLOY_DIR"
    
    if [ $? -eq 0 ]; then
        echo "✓ Backup created successfully"
    else
        echo "✗ Backup failed, aborting deployment"
        return 1
    fi
    
    # Pull latest code
    echo "Pulling latest code..."
    cd "$DEPLOY_DIR"
    git pull origin main
    local git_status=$?
    
    if [ $git_status -ne 0 ]; then
        echo "✗ Git pull failed with code: $git_status"
        echo "Rolling back..."
        # Restore backup logic here
        return 1
    fi
    
    # Install dependencies
    echo "Installing dependencies..."
    npm install --production
    
    if [ $? -eq 0 ]; then
        echo "✓ Dependencies installed"
    else
        echo "✗ Dependency installation failed"
        return 1
    fi
    
    # Run tests
    echo "Running tests..."
    npm test
    local test_status=$?
    
    if [ $test_status -eq 0 ]; then
        echo "✓ All tests passed"
    else
        echo "✗ Tests failed with code: $test_status"
        return 1
    fi
    
    # Restart service
    echo "Restarting service..."
    systemctl restart "$APP_NAME"
    
    if [ $? -eq 0 ]; then
        echo "✓ Service restarted successfully"
        echo "✓ Deployment completed successfully"
        return 0
    else
        echo "✗ Service restart failed"
        return 1
    fi
}

# Execute deployment
deploy
exit_code=$?

if [ $exit_code -eq 0 ]; then
    echo "🎉 Deployment successful!"
    exit 0
else
    echo "❌ Deployment failed with exit code: $exit_code"
    exit $exit_code
fi
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `$?` last command ka exit status
- ✅ `0` = success, non-zero = error
- ✅ Immediately check karo
- ✅ Save if needed: `status=$?`
- ✅ Critical commands hamesha check

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `$?` kab overwrite hota hai?**
A: Har command ke baad. Immediately check ya save karo.

**Q2: Exit code 127 ka matlab kya hai?**
A: Command not found.

**Q3: Multiple commands ka status kaise check karu?**
A: Har command ke baad save karo: `status1=$?`

### 14. **Practice ke liye Task**

```bash
# 1. Basic check
ls /home
echo "Exit status: $?"

# 2. Save and use
grep "test" file.txt
status=$?
echo "Grep returned: $status"

# 3. Conditional
if ping -c 1 google.com > /dev/null 2>&1; then
    echo "Network OK"
else
    echo "Network failed: $?"
fi

# 4. Script
#!/bin/bash
command1
[ $? -eq 0 ] || exit 1
command2
[ $? -eq 0 ] || exit 2
echo "All commands succeeded"
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔢 `$?` stores last exit status
- ✅ 0 = success, 1-255 = errors
- ⚡ Check immediately (overwrites)
- 💾 Save if needed: `status=$?`
- 🎯 Critical for error handling

> **💡 Ye Zaroor Yaad Rakhein:**
> `$?` har command ke baad overwrite hota hai! Immediately check karo ya save karo. 0 = success, baaki sab errors. Production scripts mein hamesha check karo!

---

## **Topic 2: Script Exit Codes (`exit 0`, `exit 1`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Script Exit Codes** - Apni script ka status return karna.

### 2. **Ye Kya Hai? (What is it?)**
`exit` command script ko terminate karta hai aur ek exit code return karta hai. `exit 0` success indicate karta hai, `exit 1` (ya koi non-zero) error indicate karta hai. Yeh calling script/process ko batata hai ki script successful rahi ya nahi.

**Analogy:** Exit code ek final report hai jo aap apne boss ko dete hain - "Kaam ho gaya (0)" ya "Problem aayi (1-255)".

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Communication** - Calling process ko status batana
- ✅ **Automation** - CI/CD pipelines
- ✅ **Error handling** - Proper failure indication
- ✅ **Debugging** - Problem identification

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Script completion par
- Error conditions mein
- Early termination
- Automation scripts

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Unclear script status
- Automation failures
- Silent errors
- Pipeline issues

### 6. **Syntax aur Common Options**

```bash
# Exit with status
exit 0          # Success
exit 1          # General error
exit 2          # Misuse
exit 127        # Command not found
exit 130        # Terminated by Ctrl+C

# Exit with last command status
exit $?

# Common convention
0     # Success
1     # General error
2     # Misuse of command
64-78 # Custom error codes
```

### 7. **Example 1 (Basic)**

```bash
#!/bin/bash
# Simple script with exit codes

# Check arguments
if [ $# -eq 0 ]; then
    echo "Error: No arguments provided"
    echo "Usage: $0 <filename>"
    exit 1
fi

filename=$1

# Check file exists
if [ ! -f "$filename" ]; then
    echo "Error: File not found: $filename"
    exit 2
fi

# Process file
echo "Processing $filename..."
cat "$filename"

# Success
echo "Done!"
exit 0
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Professional script with meaningful exit codes

set -euo pipefail

# Exit codes
readonly E_SUCCESS=0
readonly E_GENERAL=1
readonly E_MISUSE=2
readonly E_NO_FILE=3
readonly E_NO_PERMISSION=4
readonly E_NETWORK=5
readonly E_TIMEOUT=6

readonly SCRIPT_NAME=$(basename "$0")
readonly LOG_FILE="/var/log/${SCRIPT_NAME}.log"

# Logging function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Error handler
error_exit() {
    local message=$1
    local exit_code=${2:-$E_GENERAL}
    
    log "ERROR: $message"
    exit "$exit_code"
}

# Cleanup on exit
cleanup() {
    local exit_code=$?
    
    log "Script exiting with code: $exit_code"
    
    # Cleanup temporary files
    rm -f /tmp/temp_$$_*
    
    # Send notification on failure
    if [ $exit_code -ne 0 ]; then
        echo "Script failed with code $exit_code" | \
            mail -s "Script Failure: $SCRIPT_NAME" admin@example.com
    fi
}

trap cleanup EXIT

# Validate prerequisites
validate_prerequisites() {
    log "Validating prerequisites..."
    
    # Check required commands
    for cmd in curl jq mysql; do
        if ! command -v "$cmd" >/dev/null 2>&1; then
            error_exit "Required command not found: $cmd" $E_GENERAL
        fi
    done
    
    # Check permissions
    if [ ! -w "$LOG_FILE" ]; then
        error_exit "Cannot write to log file: $LOG_FILE" $E_NO_PERMISSION
    fi
    
    log "✓ Prerequisites validated"
}

# Main function
main() {
    log "Starting $SCRIPT_NAME..."
    
    # Validate
    validate_prerequisites
    
    # Check arguments
    if [ $# -lt 2 ]; then
        echo "Usage: $0 <source> <destination>"
        error_exit "Insufficient arguments" $E_MISUSE
    fi
    
    local source=$1
    local destination=$2
    
    # Check source exists
    if [ ! -f "$source" ]; then
        error_exit "Source file not found: $source" $E_NO_FILE
    fi
    
    # Check network connectivity
    if ! ping -c 1 -W 2 google.com >/dev/null 2>&1; then
        error_exit "Network connectivity issue" $E_NETWORK
    fi
    
    # Process with timeout
    log "Processing $source..."
    
    if timeout 30 cp "$source" "$destination"; then
        log "✓ File copied successfully"
    else
        local status=$?
        if [ $status -eq 124 ]; then
            error_exit "Operation timed out" $E_TIMEOUT
        else
            error_exit "Copy failed" $E_GENERAL
        fi
    fi
    
    log "✓ Script completed successfully"
    exit $E_SUCCESS
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Exit code bhoolna:** Script end par `exit 0` dena
- ❌ **Same code har error ke liye:** Different errors = different codes
- ❌ **Range exceed:** 0-255 ke andar rakho

### 10. **Best Practices / Pro Tips**
- 💡 **Constants use karo:** `E_SUCCESS=0`, `E_ERROR=1`
- 💡 **Meaningful codes:** Different errors ke liye different codes
- 💡 **Document karo:** Script top par exit codes list karo
- 💡 **Cleanup:** `trap` use karo exit par

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# CI/CD deployment script with proper exit codes

set -euo pipefail

# Exit codes
readonly SUCCESS=0
readonly BUILD_FAILED=1
readonly TEST_FAILED=2
readonly DEPLOY_FAILED=3
readonly ROLLBACK_FAILED=4

readonly PROJECT_DIR="/var/www/app"
readonly BUILD_DIR="$PROJECT_DIR/build"

log() {
    echo "[$(date '+%H:%M:%S')] $1"
}

# Build application
build() {
    log "Building application..."
    
    cd "$PROJECT_DIR"
    
    if npm run build; then
        log "✓ Build successful"
        return 0
    else
        log "✗ Build failed"
        return 1
    fi
}

# Run tests
test() {
    log "Running tests..."
    
    if npm test; then
        log "✓ Tests passed"
        return 0
    else
        log "✗ Tests failed"
        return 1
    fi
}

# Deploy
deploy() {
    log "Deploying application..."
    
    if rsync -avz "$BUILD_DIR/" production:/var/www/; then
        log "✓ Deployment successful"
        return 0
    else
        log "✗ Deployment failed"
        return 1
    fi
}

# Rollback
rollback() {
    log "Rolling back..."
    
    if ssh production "cd /var/www && git checkout HEAD~1"; then
        log "✓ Rollback successful"
        return 0
    else
        log "✗ Rollback failed"
        return 1
    fi
}

# Main pipeline
main() {
    log "Starting CI/CD pipeline..."
    
    # Build
    if ! build; then
        log "Pipeline failed at build stage"
        exit $BUILD_FAILED
    fi
    
    # Test
    if ! test; then
        log "Pipeline failed at test stage"
        exit $TEST_FAILED
    fi
    
    # Deploy
    if ! deploy; then
        log "Pipeline failed at deploy stage"
        
        # Attempt rollback
        if ! rollback; then
            log "CRITICAL: Rollback failed!"
            exit $ROLLBACK_FAILED
        fi
        
        exit $DEPLOY_FAILED
    fi
    
    log "✓ Pipeline completed successfully"
    exit $SUCCESS
}

main "$@"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `exit 0` for success
- ✅ `exit 1-255` for errors
- ✅ Different codes for different errors
- ✅ Document exit codes
- ✅ Use constants for clarity

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Exit code range kya hai?**
A: 0-255. 0=success, 1-255=errors.

**Q2: Multiple exit points ho sakte hain?**
A: Haan, lekin cleanup ke liye `trap` use karo.

**Q3: Exit code kaise check karu calling script mein?**
A: `$?` variable use karo.

### 14. **Practice ke liye Task**

```bash
# 1. Simple script
#!/bin/bash
[ $# -eq 0 ] && exit 1
echo "Args: $@"
exit 0

# 2. With constants
#!/bin/bash
readonly SUCCESS=0
readonly ERROR=1

[ -f "$1" ] || exit $ERROR
cat "$1"
exit $SUCCESS

# 3. Test from command line
./script.sh
echo "Exit code: $?"

# 4. Use in pipeline
./script1.sh && ./script2.sh || echo "Failed"
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🚪 `exit` terminates script with code
- ✅ 0 = success, 1-255 = errors
- 📋 Different errors = different codes
- 📝 Document exit codes in script
- 🧹 Use `trap` for cleanup

> **💡 Ye Zaroor Yaad Rakhein:**
> Hamesha meaningful exit codes use karo! 0=success, different errors ke liye different codes (1-255). Constants define karo aur document karo. CI/CD mein bahut important!

---

## **Topic 3: Debugging (`set -x`, `set -e`, `set -u`, `set -o pipefail`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Debugging Options** - Script ko robust aur debuggable banane ke powerful options.

### 2. **Ye Kya Hai? (What is it?)**
Bash ke debugging options script execution ko control karte hain. `set -x` har command print karta hai, `set -e` error par exit karta hai, `set -u` undefined variables ko error banata hai, aur `set -o pipefail` pipeline mein kisi bhi command ki failure ko catch karta hai.

**Analogy:** Yeh options ek safety net hain - jaise construction site par helmet, safety harness. Accidents hone se pehle rok dete hain.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Early error detection** - Problems jaldi pakdo
- ✅ **Debugging** - Execution flow dekho
- ✅ **Reliability** - Silent failures avoid
- ✅ **Production safety** - Robust scripts

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Production scripts
- Critical automation
- Debugging issues
- CI/CD pipelines

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Silent failures
- Undefined variable bugs
- Pipeline failures ignored
- Hard to debug issues

### 6. **Syntax aur Common Options**

```bash
# Individual options
set -e          # Exit on error
set -u          # Error on undefined variable
set -x          # Print commands (debug)
set -o pipefail # Pipeline fails if any command fails

# Combined (strict mode)
set -euo pipefail

# Disable options
set +e          # Disable exit on error
set +x          # Disable debug mode

# In shebang
#!/bin/bash -e
#!/bin/bash -eux
```

### 7. **Example 1 (Basic)**

```bash
#!/bin/bash

# Without set -e
echo "Starting..."
false           # This fails but script continues
echo "Still running"

# With set -e
set -e
echo "Starting with set -e..."
false           # Script exits here
echo "This won't print"

# set -u example
set -u
echo $UNDEFINED_VAR  # Error: unbound variable

# set -x example
set -x
name="John"
echo "Hello $name"
# Output: + name=John
#         + echo 'Hello John'
#         Hello John

# set -o pipefail example
set -o pipefail
false | true    # Without pipefail: succeeds
                # With pipefail: fails
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Production-ready script with all debugging options

# Strict mode
set -euo pipefail

# Optional: Enable debug mode via environment variable
[ "${DEBUG:-false}" = "true" ] && set -x

readonly SCRIPT_NAME=$(basename "$0")
readonly LOG_FILE="/var/log/${SCRIPT_NAME}.log"

# Trap errors
trap 'error_handler $? $LINENO' ERR

error_handler() {
    local exit_code=$1
    local line_number=$2
    
    echo "Error occurred in script at line $line_number with exit code $exit_code" >&2
    echo "Failed command: $(sed -n "${line_number}p" "$0")" >&2
    
    # Cleanup
    cleanup
    
    exit "$exit_code"
}

cleanup() {
    echo "Cleaning up..."
    rm -f /tmp/temp_$$_*
}

trap cleanup EXIT

# Function with error handling
process_file() {
    local file=$1
    
    # set -e ensures this exits on error
    [ -f "$file" ] || return 1
    
    # Pipeline with pipefail
    cat "$file" | grep "pattern" | sort | uniq
    
    # If any command in pipeline fails, function returns error
}

# Temporarily disable exit on error
safe_operation() {
    set +e
    
    # This might fail, but we handle it
    some_command_that_might_fail
    local status=$?
    
    set -e
    
    if [ $status -ne 0 ]; then
        echo "Command failed, but continuing..."
    fi
}

# Main logic
main() {
    echo "Starting $SCRIPT_NAME..."
    
    # These will auto-exit on error due to set -e
    mkdir -p /tmp/workdir
    cd /tmp/workdir
    
    # Undefined variable will cause error due to set -u
    local required_var="${REQUIRED_VAR:-default}"
    
    # Process files
    for file in *.txt; do
        if [ -f "$file" ]; then
            process_file "$file"
        fi
    done
    
    echo "Completed successfully"
}

# Debug mode example
debug_info() {
    if [ "${DEBUG:-false}" = "true" ]; then
        echo "=== Debug Info ==="
        echo "Script: $0"
        echo "Args: $@"
        echo "PWD: $PWD"
        echo "User: $USER"
        set -x  # Enable command tracing
    fi
}

debug_info "$@"
main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`set -e` with pipes:** Pipeline failures ignore ho sakte hain without `pipefail`
- ❌ **Conditional mein `set -e`:** `if command; then` mein `set -e` kaam nahi karta
- ❌ **`set -u` with `${var:-default}`:** Default values use karo

### 10. **Best Practices / Pro Tips**
- 💡 **Strict mode:** `set -euo pipefail` har script mein
- 💡 **Debug flag:** Environment variable se control karo
- 💡 **Trap ERR:** Error handler add karo
- 💡 **Selective disable:** `set +e` temporarily jahan zaroorat ho

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Database backup script with comprehensive error handling

set -euo pipefail

readonly BACKUP_DIR="/backups/mysql"
readonly LOG_FILE="/var/log/mysql_backup.log"
readonly RETENTION_DAYS=7

# Enable debug mode if DEBUG=true
[ "${DEBUG:-false}" = "true" ] && set -x

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Error trap
trap 'log "ERROR: Script failed at line $LINENO with exit code $?"' ERR
trap 'cleanup' EXIT

cleanup() {
    log "Cleanup: Removing temporary files"
    rm -f /tmp/mysql_backup_$$_*
}

# Validate environment
validate() {
    log "Validating environment..."
    
    # set -u will catch undefined variables
    : "${DB_USER:?DB_USER not set}"
    : "${DB_PASS:?DB_PASS not set}"
    
    # set -e will exit if commands fail
    command -v mysqldump >/dev/null
    mkdir -p "$BACKUP_DIR"
    
    log "✓ Validation passed"
}

# Backup database
backup_database() {
    local db=$1
    local backup_file="$BACKUP_DIR/${db}_$(date +%Y%m%d_%H%M%S).sql.gz"
    
    log "Backing up database: $db"
    
    # Pipeline with pipefail - any failure will exit
    mysqldump -u"$DB_USER" -p"$DB_PASS" "$db" | \
        gzip > "$backup_file"
    
    # Verify backup
    if [ -s "$backup_file" ]; then
        log "✓ Backup created: $backup_file ($(du -h "$backup_file" | cut -f1))"
    else
        log "✗ Backup file is empty or missing"
        return 1
    fi
}

# Cleanup old backups
cleanup_old_backups() {
    log "Cleaning up backups older than $RETENTION_DAYS days..."
    
    # Temporarily disable exit on error
    set +e
    
    find "$BACKUP_DIR" -name "*.sql.gz" -mtime +$RETENTION_DAYS -delete
    local status=$?
    
    set -e
    
    if [ $status -eq 0 ]; then
        log "✓ Old backups cleaned"
    else
        log "⚠️  Cleanup had issues (non-critical)"
    fi
}

# Main execution
main() {
    log "=== Starting MySQL Backup ==="
    
    validate
    
    # Get list of databases
    local databases=$(mysql -u"$DB_USER" -p"$DB_PASS" -e "SHOW DATABASES;" | \
        grep -Ev "^(Database|information_schema|performance_schema|mysql|sys)$")
    
    # Backup each database
    for db in $databases; do
        backup_database "$db"
    done
    
    cleanup_old_backups
    
    log "=== Backup completed successfully ==="
}

main "$@"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `set -e` exit on error
- ✅ `set -u` error on undefined vars
- ✅ `set -x` debug/trace mode
- ✅ `set -o pipefail` catch pipeline failures
- ✅ `set -euo pipefail` strict mode

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `set -e` kab kaam nahi karta?**
A: `if`, `while`, `until` conditions mein, aur `||`, `&&` ke saath.

**Q2: `set -x` output kaise control karu?**
A: `set +x` se disable karo, ya `DEBUG` environment variable use karo.

**Q3: Pipeline mein ek command fail ho toh?**
A: `set -o pipefail` use karo, warna last command ka status milega.

### 14. **Practice ke liye Task**

```bash
# 1. Test set -e
#!/bin/bash
set -e
echo "Start"
false
echo "This won't print"

# 2. Test set -u
#!/bin/bash
set -u
echo $UNDEFINED  # Error

# 3. Test set -x
#!/bin/bash
set -x
name="Test"
echo "Hello $name"

# 4. Test pipefail
#!/bin/bash
set -o pipefail
false | true
echo "Exit code: $?"

# 5. Strict mode
#!/bin/bash
set -euo pipefail
echo "Strict mode enabled"
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🛑 `set -e` auto-exit on errors
- 🚫 `set -u` catch undefined variables
- 🔍 `set -x` trace execution
- 🔗 `set -o pipefail` pipeline safety
- 💪 `set -euo pipefail` = strict mode

> **💡 Ye Zaroor Yaad Rakhein:**
> Production scripts mein hamesha `set -euo pipefail` use karo! Yeh tumhari script ko robust banata hai. Debug ke liye `set -x` use karo. Trap ERR for error handling!

---

## **Topic 4: `trap` Command (Cleanup on exit)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**trap Command** - Signals aur events par custom actions execute karna.

### 2. **Ye Kya Hai? (What is it?)**
`trap` command signals (jaise Ctrl+C, script exit) ko catch karta hai aur specified command execute karta hai. Yeh cleanup, logging, ya graceful shutdown ke liye use hota hai. Script exit hone se pehle temporary files delete karna, connections close karna, etc.

**Analogy:** Trap ek emergency exit plan hai - jaise fire alarm bajne par kya karna hai, waise hi script interrupt hone par kya karna hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Cleanup** - Temporary files remove
- ✅ **Graceful shutdown** - Resources release
- ✅ **Error handling** - Exit par actions
- ✅ **Signal handling** - Ctrl+C, kill, etc.

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Temporary files banate waqt
- Database connections
- Lock files
- Critical cleanup operations

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Resource leaks
- Orphaned processes
- Temporary files clutter
- Incomplete operations

### 6. **Syntax aur Common Options**

```bash
# Basic syntax
trap 'commands' SIGNAL

# Common signals
trap 'cleanup' EXIT      # Script exit (normal or error)
trap 'cleanup' INT       # Ctrl+C (SIGINT)
trap 'cleanup' TERM      # kill command (SIGTERM)
trap 'cleanup' ERR       # Error occurred

# Multiple signals
trap 'cleanup' EXIT INT TERM

# Remove trap
trap - SIGNAL

# List traps
trap -p
```

### 7. **Example 1 (Basic)**

```bash
#!/bin/bash

# Simple cleanup
cleanup() {
    echo "Cleaning up..."
    rm -f /tmp/tempfile_$$
}

trap cleanup EXIT

# Create temp file
echo "Creating temp file..."
touch /tmp/tempfile_$$

echo "Doing work..."
sleep 2

echo "Done"
# cleanup automatically called on exit

# Ctrl+C handler
handle_interrupt() {
    echo ""
    echo "Interrupted! Cleaning up..."
    rm -f /tmp/work_*
    exit 130
}

trap handle_interrupt INT

echo "Press Ctrl+C to interrupt..."
while true; do
    echo "Working..."
    sleep 1
done
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Production script with comprehensive trap handling

set -euo pipefail

readonly SCRIPT_NAME=$(basename "$0")
readonly PID=$$
readonly LOCK_FILE="/var/run/${SCRIPT_NAME}.lock"
readonly TEMP_DIR="/tmp/${SCRIPT_NAME}_${PID}"
readonly LOG_FILE="/var/log/${SCRIPT_NAME}.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Comprehensive cleanup function
cleanup() {
    local exit_code=$?
    
    log "Cleanup started (exit code: $exit_code)"
    
    # Remove temporary directory
    if [ -d "$TEMP_DIR" ]; then
        log "Removing temp directory: $TEMP_DIR"
        rm -rf "$TEMP_DIR"
    fi
    
    # Remove lock file
    if [ -f "$LOCK_FILE" ]; then
        log "Removing lock file: $LOCK_FILE"
        rm -f "$LOCK_FILE"
    fi
    
    # Close database connections
    if [ -n "${DB_CONN:-}" ]; then
        log "Closing database connection"
        # mysql -e "KILL $DB_CONN" 2>/dev/null || true
    fi
    
    # Stop background jobs
    local jobs=$(jobs -p)
    if [ -n "$jobs" ]; then
        log "Stopping background jobs"
        kill $jobs 2>/dev/null || true
    fi
    
    log "Cleanup completed"
    
    # Exit with original code
    exit $exit_code
}

# Handle interrupts (Ctrl+C)
handle_interrupt() {
    log "Received interrupt signal (SIGINT)"
    echo ""
    echo "Interrupted by user. Cleaning up..."
    cleanup
    exit 130
}

# Handle termination (kill)
handle_terminate() {
    log "Received termination signal (SIGTERM)"
    echo "Terminating gracefully..."
    cleanup
    exit 143
}

# Handle errors
handle_error() {
    local exit_code=$?
    local line_number=$1
    
    log "ERROR: Script failed at line $line_number with exit code $exit_code"
    log "Failed command: $(sed -n "${line_number}p" "$0")"
    
    cleanup
    exit $exit_code
}

# Set up traps
trap cleanup EXIT
trap handle_interrupt INT
trap handle_terminate TERM
trap 'handle_error $LINENO' ERR

# Create lock file to prevent multiple instances
create_lock() {
    if [ -f "$LOCK_FILE" ]; then
        local lock_pid=$(cat "$LOCK_FILE")
        
        if ps -p "$lock_pid" > /dev/null 2>&1; then
            log "ERROR: Another instance is running (PID: $lock_pid)"
            exit 1
        else
            log "Removing stale lock file"
            rm -f "$LOCK_FILE"
        fi
    fi
    
    echo $$ > "$LOCK_FILE"
    log "Lock file created: $LOCK_FILE"
}

# Initialize
initialize() {
    log "=== Starting $SCRIPT_NAME (PID: $$) ==="
    
    create_lock
    
    # Create temp directory
    mkdir -p "$TEMP_DIR"
    log "Temp directory created: $TEMP_DIR"
}

# Main work function
do_work() {
    log "Starting main work..."
    
    # Simulate long-running task
    for i in {1..10}; do
        log "Processing step $i/10..."
        
        # Create temp files
        echo "data $i" > "$TEMP_DIR/file_$i.txt"
        
        sleep 1
    done
    
    log "Main work completed"
}

# Main execution
main() {
    initialize
    do_work
    
    log "=== Script completed successfully ==="
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Quotes bhoolna:** `trap 'command'` quotes zaroori hain
- ❌ **EXIT trap mein exit:** Infinite loop ho sakta hai
- ❌ **Signal names galat:** `SIGINT` nahi, `INT` use karo

### 10. **Best Practices / Pro Tips**
- 💡 **EXIT trap:** Hamesha use karo cleanup ke liye
- 💡 **Multiple signals:** `trap 'cleanup' EXIT INT TERM`
- 💡 **Exit code preserve:** `exit_code=$?` save karo
- 💡 **Idempotent cleanup:** Multiple calls safe hone chahiye

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Database migration script with proper cleanup

set -euo pipefail

readonly DB_NAME="production_db"
readonly BACKUP_FILE="/tmp/db_backup_$$.sql"
readonly MIGRATION_LOG="/var/log/migration.log"
readonly LOCK_FILE="/var/run/migration.lock"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$MIGRATION_LOG"
}

# Comprehensive cleanup
cleanup() {
    local exit_code=$?
    
    log "Cleanup: Starting (exit code: $exit_code)"
    
    # Remove backup if migration successful
    if [ $exit_code -eq 0 ] && [ -f "$BACKUP_FILE" ]; then
        log "Cleanup: Removing backup file"
        rm -f "$BACKUP_FILE"
    elif [ -f "$BACKUP_FILE" ]; then
        log "Cleanup: Keeping backup file for rollback: $BACKUP_FILE"
    fi
    
    # Remove lock
    if [ -f "$LOCK_FILE" ]; then
        rm -f "$LOCK_FILE"
        log "Cleanup: Lock file removed"
    fi
    
    # Restore database on failure
    if [ $exit_code -ne 0 ] && [ -f "$BACKUP_FILE" ]; then
        log "Cleanup: Migration failed, restoring database..."
        mysql "$DB_NAME" < "$BACKUP_FILE"
        log "Cleanup: Database restored from backup"
    fi
    
    log "Cleanup: Completed"
}

# Handle Ctrl+C
handle_interrupt() {
    log "Migration interrupted by user"
    echo ""
    echo "⚠️  Migration interrupted! Rolling back..."
    exit 130
}

# Set traps
trap cleanup EXIT
trap handle_interrupt INT TERM

# Create lock
if [ -f "$LOCK_FILE" ]; then
    log "ERROR: Migration already running"
    exit 1
fi
echo $$ > "$LOCK_FILE"

# Main migration
main() {
    log "=== Starting Database Migration ==="
    
    # Backup database
    log "Creating backup..."
    mysqldump "$DB_NAME" > "$BACKUP_FILE"
    log "✓ Backup created: $BACKUP_FILE"
    
    # Run migrations
    log "Running migrations..."
    for migration in migrations/*.sql; do
        log "Applying: $migration"
        mysql "$DB_NAME" < "$migration"
    done
    
    log "✓ All migrations applied successfully"
    log "=== Migration Completed ==="
}

main "$@"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `trap 'cleanup' EXIT` always use
- ✅ `trap 'handler' INT` for Ctrl+C
- ✅ `trap 'handler' ERR` for errors
- ✅ Cleanup idempotent hona chahiye
- ✅ Exit code preserve karo

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: EXIT trap kab execute hota hai?**
A: Script exit hone par - normal exit ya error, dono mein.

**Q2: Multiple traps ek saath kaise set karu?**
A: `trap 'cleanup' EXIT INT TERM ERR`

**Q3: Trap disable kaise karu?**
A: `trap - SIGNAL` use karo.

### 14. **Practice ke liye Task**

```bash
# 1. Basic cleanup
#!/bin/bash
cleanup() {
    echo "Cleaning up..."
    rm -f /tmp/test_$$
}
trap cleanup EXIT
touch /tmp/test_$$
echo "File created"

# 2. Ctrl+C handler
#!/bin/bash
trap 'echo "Interrupted!"; exit' INT
while true; do
    echo "Running..."
    sleep 1
done

# 3. Error handler
#!/bin/bash
trap 'echo "Error at line $LINENO"' ERR
set -e
false

# 4. Multiple signals
#!/bin/bash
cleanup() {
    echo "Cleanup called"
}
trap cleanup EXIT INT TERM
sleep 10
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🪤 `trap` catches signals and events
- 🧹 EXIT trap for cleanup
- ⚡ INT trap for Ctrl+C
- 🚨 ERR trap for errors
- 💪 Essential for robust scripts

> **💡 Ye Zaroor Yaad Rakhein:**
> Har production script mein `trap cleanup EXIT` use karo! Temporary files, locks, connections - sab cleanup karo. Ctrl+C handle karo gracefully. Idempotent cleanup likho!

---

## **Topic 5: Error Logging (Redirecting to `stderr` `>&2`, Logging to files)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Error Logging** - Errors ko properly log karna aur stderr par redirect karna.

### 2. **Ye Kya Hai? (What is it?)**
Error logging errors aur important messages ko stderr (file descriptor 2) par redirect karna hai using `>&2`, aur unhe files mein save karna hai future reference ke liye. Yeh normal output (stdout) se alag hota hai, jisse errors easily identify ho sakti hain.

**Analogy:** Error logging ek black box recorder hai - jab plane crash ho, toh pata chale kya hua. Logs se debugging easy ho jati hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Debugging** - Problems identify karna
- ✅ **Audit trail** - Kya hua record
- ✅ **Monitoring** - System health check
- ✅ **Compliance** - Regulatory requirements

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Production scripts
- Error messages
- Audit logging
- System monitoring

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Lost error information
- Hard to debug
- No audit trail
- Compliance issues

### 6. **Syntax aur Common Options**

```bash
# Redirect to stderr
echo "Error message" >&2

# Log to file
echo "Log message" >> /var/log/script.log

# Both stderr and file
echo "Error" | tee -a /var/log/error.log >&2

# Redirect all stderr to file
exec 2>> /var/log/error.log

# Timestamp
echo "[$(date)] Message" >> /var/log/script.log
```

### 7. **Example 1 (Basic)**

```bash
#!/bin/bash

# Simple error to stderr
error() {
    echo "ERROR: $1" >&2
}

# Simple logging
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> /var/log/script.log
}

# Usage
if [ ! -f "config.txt" ]; then
    error "Config file not found"
    log "ERROR: Config file missing"
    exit 1
fi

echo "Processing..."
log "Processing started"

# Separate stdout and stderr
./command > output.txt 2> error.txt

# Both to same file
./command > all.log 2>&1

# stderr to file, stdout to screen
./command 2>> error.log
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Professional logging system

set -euo pipefail

readonly SCRIPT_NAME=$(basename "$0")
readonly LOG_DIR="/var/log/${SCRIPT_NAME}"
readonly LOG_FILE="${LOG_DIR}/app.log"
readonly ERROR_LOG="${LOG_DIR}/error.log"
readonly DEBUG_LOG="${LOG_DIR}/debug.log"

# Log levels
readonly LOG_LEVEL_DEBUG=0
readonly LOG_LEVEL_INFO=1
readonly LOG_LEVEL_WARN=2
readonly LOG_LEVEL_ERROR=3
readonly LOG_LEVEL_FATAL=4

# Current log level (set via environment)
CURRENT_LOG_LEVEL=${LOG_LEVEL:-$LOG_LEVEL_INFO}

# Initialize logging
init_logging() {
    mkdir -p "$LOG_DIR"
    
    # Redirect all stderr to error log
    exec 2>> "$ERROR_LOG"
    
    # Log rotation check
    for log in "$LOG_FILE" "$ERROR_LOG" "$DEBUG_LOG"; do
        if [ -f "$log" ] && [ $(stat -f%z "$log" 2>/dev/null || stat -c%s "$log") -gt 10485760 ]; then
            mv "$log" "${log}.$(date +%Y%m%d_%H%M%S)"
            gzip "${log}.$(date +%Y%m%d_%H%M%S)" &
        fi
    done
}

# Logging functions
log_message() {
    local level=$1
    local message=$2
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    local log_entry="[$timestamp] [$level] [$$] $message"
    
    echo "$log_entry" >> "$LOG_FILE"
}

log_debug() {
    [ $CURRENT_LOG_LEVEL -le $LOG_LEVEL_DEBUG ] || return 0
    log_message "DEBUG" "$1"
    echo "$1" >> "$DEBUG_LOG"
}

log_info() {
    [ $CURRENT_LOG_LEVEL -le $LOG_LEVEL_INFO ] || return 0
    log_message "INFO" "$1"
    echo "[INFO] $1"
}

log_warn() {
    [ $CURRENT_LOG_LEVEL -le $LOG_LEVEL_WARN ] || return 0
    log_message "WARN" "$1"
    echo "[WARN] $1" >&2
}

log_error() {
    [ $CURRENT_LOG_LEVEL -le $LOG_LEVEL_ERROR ] || return 0
    log_message "ERROR" "$1"
    echo "[ERROR] $1" >&2
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$ERROR_LOG"
}

log_fatal() {
    log_message "FATAL" "$1"
    echo "[FATAL] $1" >&2
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] FATAL: $1" >> "$ERROR_LOG"
    exit 1
}

# Structured logging
log_structured() {
    local level=$1
    local message=$2
    shift 2
    
    local json='{'
    json+="\"timestamp\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\","
    json+="\"level\":\"$level\","
    json+="\"message\":\"$message\","
    json+="\"pid\":$$,"
    json+="\"script\":\"$SCRIPT_NAME\""
    
    # Add extra fields
    while [ $# -gt 0 ]; do
        json+=",\"$1\":\"$2\""
        shift 2
    done
    
    json+='}'
    
    echo "$json" >> "${LOG_DIR}/structured.log"
}

# Error handler with logging
error_handler() {
    local exit_code=$?
    local line_number=$1
    
    log_error "Script failed at line $line_number with exit code $exit_code"
    log_error "Failed command: $(sed -n "${line_number}p" "$0")"
    
    # Send alert
    if command -v mail >/dev/null 2>&1; then
        echo "Script $SCRIPT_NAME failed at line $line_number" | \
            mail -s "Script Failure Alert" admin@example.com
    fi
}

trap 'error_handler $LINENO' ERR

# Example usage
main() {
    init_logging
    
    log_info "Script started"
    log_debug "Debug mode enabled"
    
    # Simulate operations
    log_info "Connecting to database..."
    
    if ! ping -c 1 database.example.com >/dev/null 2>&1; then
        log_error "Cannot reach database server"
        log_structured "ERROR" "Database unreachable" \
            "host" "database.example.com" \
            "retry_count" "3"
        exit 1
    fi
    
    log_info "Database connection successful"
    
    # Warning example
    if [ $(df -h / | tail -1 | awk '{print $5}' | sed 's/%//') -gt 80 ]; then
        log_warn "Disk usage above 80%"
    fi
    
    log_info "Script completed successfully"
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`>&2` bhoolna:** Errors stdout par chale jaate hain
- ❌ **Timestamps nahi:** Kab hua pata nahi chalta
- ❌ **Log rotation nahi:** Disk full ho jati hai
- ❌ **Permissions ignore:** Log files write nahi ho pati

### 10. **Best Practices / Pro Tips**
- 💡 **Timestamps hamesha:** `[$(date)] message`
- 💡 **Log levels:** DEBUG, INFO, WARN, ERROR, FATAL
- 💡 **Structured logging:** JSON format for parsing
- 💡 **Log rotation:** Old logs compress/delete karo
- 💡 **Permissions:** Log directory writable ho

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Production API monitoring script with comprehensive logging

set -euo pipefail

readonly SCRIPT_NAME="api_monitor"
readonly LOG_DIR="/var/log/${SCRIPT_NAME}"
readonly LOG_FILE="${LOG_DIR}/monitor.log"
readonly ERROR_LOG="${LOG_DIR}/error.log"
readonly ALERT_LOG="${LOG_DIR}/alerts.log"
readonly METRICS_LOG="${LOG_DIR}/metrics.log"

# Initialize
mkdir -p "$LOG_DIR"

# Logging functions
log() {
    local level=$1
    local message=$2
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    echo "[$timestamp] [$level] $message" | tee -a "$LOG_FILE"
    
    if [ "$level" = "ERROR" ] || [ "$level" = "FATAL" ]; then
        echo "[$timestamp] $message" >> "$ERROR_LOG"
    fi
}

log_metric() {
    local metric=$1
    local value=$2
    local timestamp=$(date +%s)
    
    echo "$timestamp,$metric,$value" >> "$METRICS_LOG"
}

send_alert() {
    local message=$1
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    echo "[$timestamp] ALERT: $message" >> "$ALERT_LOG"
    
    # Send to monitoring system
    curl -X POST https://monitoring.example.com/alerts \
        -H "Content-Type: application/json" \
        -d "{\"message\":\"$message\",\"timestamp\":\"$timestamp\"}" \
        2>> "$ERROR_LOG" || log "ERROR" "Failed to send alert"
}

# Check API endpoint
check_endpoint() {
    local url=$1
    local name=$2
    
    log "INFO" "Checking endpoint: $name ($url)"
    
    local start_time=$(date +%s%3N)
    local http_code=$(curl -s -o /dev/null -w "%{http_code}" \
        --max-time 10 "$url" 2>> "$ERROR_LOG")
    local end_time=$(date +%s%3N)
    local response_time=$((end_time - start_time))
    
    # Log metrics
    log_metric "${name}_response_time" "$response_time"
    log_metric "${name}_http_code" "$http_code"
    
    # Check status
    if [ "$http_code" = "200" ]; then
        log "INFO" "✓ $name: OK (${response_time}ms)"
        
        if [ $response_time -gt 1000 ]; then
            log "WARN" "$name response time high: ${response_time}ms"
        fi
    else
        log "ERROR" "✗ $name: Failed (HTTP $http_code)"
        send_alert "$name endpoint returned HTTP $http_code"
        return 1
    fi
}

# Main monitoring loop
main() {
    log "INFO" "=== API Monitoring Started ==="
    
    local endpoints=(
        "https://api.example.com/health|Health Check"
        "https://api.example.com/users|Users API"
        "https://api.example.com/orders|Orders API"
    )
    
    local failed=0
    
    for endpoint in "${endpoints[@]}"; do
        IFS='|' read -r url name <<< "$endpoint"
        
        if ! check_endpoint "$url" "$name"; then
            ((failed++))
        fi
        
        sleep 1
    done
    
    if [ $failed -gt 0 ]; then
        log "ERROR" "$failed endpoint(s) failed"
        exit 1
    fi
    
    log "INFO" "=== All endpoints healthy ==="
}

# Error handler
trap 'log "ERROR" "Script failed at line $LINENO"' ERR

main "$@"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `>&2` for stderr
- ✅ Timestamps in logs
- ✅ Log levels (INFO, ERROR, etc.)
- ✅ Separate error logs
- ✅ Log rotation

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: stdout aur stderr mein kya fark hai?**
A: stdout (1) normal output, stderr (2) errors. Alag redirect kar sakte hain.

**Q2: Log files kitni badi honi chahiye?**
A: 10-50MB max, phir rotate karo.

**Q3: Structured logging kyun use karu?**
A: JSON format parsing aur analysis easy karta hai.

### 14. **Practice ke liye Task**

```bash
# 1. Basic stderr
echo "Error message" >&2

# 2. Log function
log() {
    echo "[$(date)] $1" >> /tmp/test.log
}
log "Test message"

# 3. Error logging
error() {
    echo "[ERROR] $1" >&2
    echo "[$(date)] ERROR: $1" >> /tmp/error.log
}
error "Something failed"

# 4. Separate streams
./script.sh > output.log 2> error.log

# 5. Both to file
./script.sh > all.log 2>&1
```

### 15. **Aakhri Choti Summary (5 lines)**
- 📝 `>&2` redirects to stderr
- ⏰ Always add timestamps
- 📊 Use log levels (INFO, ERROR)
- 🔄 Implement log rotation
- 🎯 Separate error logs

> **💡 Ye Zaroor Yaad Rakhein:**
> Errors hamesha stderr (`>&2`) par bhejo! Timestamps zaroori hain. Log levels use karo. Production mein log rotation implement karo. Structured logging (JSON) best hai!

---

## **Topic 6: Secure Credential Handling (Env Vars, `read -s`, `gpg`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Secure Credential Handling** - Passwords aur secrets ko safely handle karna.

### 2. **Ye Kya Hai? (What is it?)**
Secure credential handling passwords, API keys, aur sensitive data ko safely store aur use karna hai. Environment variables, `read -s` (silent input), aur `gpg` (encryption) use karke credentials ko protect karte hain. Kabhi bhi credentials ko plain text mein script mein hardcode nahi karte.

**Analogy:** Credentials ek safe ka combination hai - kabhi paper par nahi likhte, hamesha secure jagah par rakhte hain.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Security** - Credentials leak nahi hote
- ✅ **Compliance** - Security standards
- ✅ **Audit** - Who accessed what
- ✅ **Separation** - Code aur secrets alag

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Database passwords
- API keys
- SSH keys
- Any sensitive data

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Credential leaks
- Security breaches
- Data theft
- Compliance violations

### 6. **Syntax aur Common Options**

```bash
# Environment variables
export DB_PASSWORD="secret"
echo $DB_PASSWORD

# Read password silently
read -s -p "Enter password: " password
echo

# GPG encryption
echo "secret" | gpg -e -r user@example.com > secret.gpg
gpg -d secret.gpg

# .env file
source .env
echo $API_KEY

# Secure file permissions
chmod 600 credentials.txt
```

### 7. **Example 1 (Basic)**

```bash
#!/bin/bash

# Method 1: Environment variables
DB_USER="${DB_USER:-}"
DB_PASS="${DB_PASS:-}"

if [ -z "$DB_USER" ] || [ -z "$DB_PASS" ]; then
    echo "Error: DB credentials not set"
    exit 1
fi

# Method 2: Read from user (silent)
read -s -p "Enter database password: " db_password
echo

# Method 3: Read from file (secure permissions)
if [ -f ~/.db_credentials ]; then
    chmod 600 ~/.db_credentials
    source ~/.db_credentials
fi

# Method 4: Use credentials
mysql -u "$DB_USER" -p"$DB_PASS" mydb

# WRONG - Never do this!
# DB_PASS="hardcoded_password"  # ❌ BAD!
# mysql -u root -p"password123"  # ❌ BAD!
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Production-grade credential management

set -euo pipefail

readonly SCRIPT_NAME=$(basename "$0")
readonly CREDENTIALS_DIR="$HOME/.credentials"
readonly ENCRYPTED_FILE="${CREDENTIALS_DIR}/${SCRIPT_NAME}.gpg"
readonly ENV_FILE="${CREDENTIALS_DIR}/${SCRIPT_NAME}.env"

# Secure logging (mask sensitive data)
log() {
    local message=$1
    # Mask any potential passwords in logs
    message=$(echo "$message" | sed -E 's/(password|token|key)=[^ ]*/\1=***MASKED***/gi')
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $message"
}

# Load credentials from environment
load_from_env() {
    log "Loading credentials from environment variables"
    
    DB_HOST="${DB_HOST:-}"
    DB_USER="${DB_USER:-}"
    DB_PASS="${DB_PASS:-}"
    API_KEY="${API_KEY:-}"
    
    if [ -z "$DB_HOST" ] || [ -z "$DB_USER" ] || [ -z "$DB_PASS" ]; then
        return 1
    fi
    
    log "✓ Credentials loaded from environment"
    return 0
}

# Load credentials from encrypted file
load_from_encrypted_file() {
    log "Loading credentials from encrypted file"
    
    if [ ! -f "$ENCRYPTED_FILE" ]; then
        log "Encrypted file not found: $ENCRYPTED_FILE"
        return 1
    fi
    
    # Decrypt and source
    if command -v gpg >/dev/null 2>&1; then
        local decrypted=$(gpg -d "$ENCRYPTED_FILE" 2>/dev/null)
        
        if [ $? -eq 0 ]; then
            eval "$decrypted"
            log "✓ Credentials decrypted successfully"
            return 0
        else
            log "Failed to decrypt credentials"
            return 1
        fi
    else
        log "GPG not available"
        return 1
    fi
}

# Load credentials from .env file (with secure permissions)
load_from_env_file() {
    log "Loading credentials from .env file"
    
    if [ ! -f "$ENV_FILE" ]; then
        log ".env file not found: $ENV_FILE"
        return 1
    fi
    
    # Check permissions
    local perms=$(stat -c %a "$ENV_FILE" 2>/dev/null || stat -f %A "$ENV_FILE")
    if [ "$perms" != "600" ]; then
        log "WARNING: Insecure permissions on $ENV_FILE (should be 600)"
        chmod 600 "$ENV_FILE"
    fi
    
    source "$ENV_FILE"
    log "✓ Credentials loaded from .env file"
    return 0
}

# Prompt user for credentials
prompt_for_credentials() {
    log "Prompting user for credentials"
    
    read -p "Database host: " DB_HOST
    read -p "Database user: " DB_USER
    read -s -p "Database password: " DB_PASS
    echo
    read -s -p "API key: " API_KEY
    echo
    
    # Optionally save encrypted
    read -p "Save credentials encrypted? (y/n): " save_choice
    if [ "$save_choice" = "y" ]; then
        save_credentials_encrypted
    fi
}

# Save credentials encrypted
save_credentials_encrypted() {
    mkdir -p "$CREDENTIALS_DIR"
    chmod 700 "$CREDENTIALS_DIR"
    
    local creds="export DB_HOST='$DB_HOST'\n"
    creds+="export DB_USER='$DB_USER'\n"
    creds+="export DB_PASS='$DB_PASS'\n"
    creds+="export API_KEY='$API_KEY'\n"
    
    echo -e "$creds" | gpg -e -r "$USER" > "$ENCRYPTED_FILE"
    chmod 600 "$ENCRYPTED_FILE"
    
    log "✓ Credentials saved encrypted"
}

# Validate credentials
validate_credentials() {
    log "Validating credentials"
    
    if [ -z "${DB_HOST:-}" ] || [ -z "${DB_USER:-}" ] || [ -z "${DB_PASS:-}" ]; then
        log "ERROR: Missing required credentials"
        return 1
    fi
    
    # Test database connection
    if command -v mysql >/dev/null 2>&1; then
        if mysql -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASS" -e "SELECT 1" >/dev/null 2>&1; then
            log "✓ Database credentials valid"
            return 0
        else
            log "ERROR: Database credentials invalid"
            return 1
        fi
    fi
    
    return 0
}

# Clear credentials from memory
clear_credentials() {
    unset DB_HOST
    unset DB_USER
    unset DB_PASS
    unset API_KEY
    
    log "Credentials cleared from memory"
}

trap clear_credentials EXIT

# Main credential loading logic
load_credentials() {
    log "=== Loading Credentials ==="
    
    # Try multiple methods in order
    if load_from_env; then
        return 0
    elif load_from_encrypted_file; then
        return 0
    elif load_from_env_file; then
        return 0
    else
        log "No credentials found, prompting user"
        prompt_for_credentials
    fi
    
    # Validate
    if ! validate_credentials; then
        log "ERROR: Credential validation failed"
        exit 1
    fi
}

# Use credentials safely
use_credentials() {
    log "Connecting to database..."
    
    # Use credentials without exposing in process list
    mysql --defaults-extra-file=<(
        echo "[client]"
        echo "host=$DB_HOST"
        echo "user=$DB_USER"
        echo "password=$DB_PASS"
    ) -e "SELECT 'Connected successfully'"
    
    log "✓ Database operation completed"
}

# Main execution
main() {
    load_credentials
    use_credentials
    
    log "=== Script completed ==="
}

main "$@"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Hardcoded passwords:** Script mein password likhna
- ❌ **Git mein commit:** Credentials version control mein
- ❌ **Insecure permissions:** 644 instead of 600
- ❌ **Logs mein passwords:** Error messages mein credentials

### 10. **Best Practices / Pro Tips**
- 💡 **Environment variables:** Production mein best
- 💡 **`.gitignore`:** Credential files add karo
- 💡 **Permissions:** 600 for files, 700 for directories
- 💡 **Mask in logs:** Passwords kabhi log mat karo
- 💡 **Vault services:** HashiCorp Vault, AWS Secrets Manager

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Production deployment script with secure credential handling

set -euo pipefail

readonly APP_NAME="myapp"
readonly SECRETS_DIR="/etc/${APP_NAME}/secrets"
readonly LOG_FILE="/var/log/${APP_NAME}/deploy.log"

# Secure logging - mask sensitive data
log() {
    local message=$1
    # Remove any potential secrets from logs
    message=$(echo "$message" | sed -E 's/(password|token|key|secret)=[^ ]*/\1=***REDACTED***/gi')
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $message" | tee -a "$LOG_FILE"
}

# Load secrets from AWS Secrets Manager
load_from_aws_secrets() {
    log "Loading secrets from AWS Secrets Manager"
    
    if ! command -v aws >/dev/null 2>&1; then
        log "AWS CLI not available"
        return 1
    fi
    
    local secret_name="${APP_NAME}/production"
    local secret_json=$(aws secretsmanager get-secret-value \
        --secret-id "$secret_name" \
        --query SecretString \
        --output text 2>/dev/null)
    
    if [ $? -eq 0 ]; then
        # Parse JSON and export variables
        export DB_HOST=$(echo "$secret_json" | jq -r '.db_host')
        export DB_USER=$(echo "$secret_json" | jq -r '.db_user')
        export DB_PASS=$(echo "$secret_json" | jq -r '.db_password')
        export API_KEY=$(echo "$secret_json" | jq -r '.api_key')
        
        log "✓ Secrets loaded from AWS Secrets Manager"
        return 0
    else
        log "Failed to load secrets from AWS"
        return 1
    fi
}

# Load secrets from local encrypted file (fallback)
load_from_local_encrypted() {
    log "Loading secrets from local encrypted file"
    
    local encrypted_file="${SECRETS_DIR}/credentials.gpg"
    
    if [ ! -f "$encrypted_file" ]; then
        log "Encrypted file not found"
        return 1
    fi
    
    # Check permissions
    local perms=$(stat -c %a "$encrypted_file" 2>/dev/null || stat -f %A "$encrypted_file")
    if [ "$perms" != "600" ]; then
        log "ERROR: Insecure permissions on encrypted file"
        return 1
    fi
    
    # Decrypt
    local decrypted=$(gpg --batch --quiet -d "$encrypted_file" 2>/dev/null)
    
    if [ $? -eq 0 ]; then
        eval "$decrypted"
        log "✓ Secrets decrypted from local file"
        return 0
    else
        log "Failed to decrypt local file"
        return 1
    fi
}

# Create database config file with credentials
create_db_config() {
    local config_file="/tmp/.my.cnf.$$"
    
    cat > "$config_file" <<EOF
[client]
host=$DB_HOST
user=$DB_USER
password=$DB_PASS
EOF
    
    chmod 600 "$config_file"
    echo "$config_file"
}

# Clean up credentials
cleanup() {
    log "Cleaning up credentials"
    
    # Remove temp files
    rm -f /tmp/.my.cnf.$$
    
    # Clear environment variables
    unset DB_HOST DB_USER DB_PASS API_KEY
    
    log "✓ Credentials cleared"
}

trap cleanup EXIT

# Main deployment
main() {
    log "=== Starting Deployment ==="
    
    # Load secrets
    if ! load_from_aws_secrets; then
        log "Falling back to local encrypted file"
        if ! load_from_local_encrypted; then
            log "ERROR: Failed to load secrets"
            exit 1
        fi
    fi
    
    # Validate secrets
    if [ -z "${DB_HOST:-}" ] || [ -z "${DB_PASS:-}" ]; then
        log "ERROR: Required secrets missing"
        exit 1
    fi
    
    # Use credentials safely
    local db_config=$(create_db_config)
    
    log "Running database migrations..."
    mysql --defaults-extra-file="$db_config" < migrations/schema.sql
    
    log "Deploying application..."
    # Use API_KEY without exposing it
    curl -H "Authorization: Bearer $API_KEY" \
        https://api.example.com/deploy \
        -d '{"app":"'$APP_NAME'"}' \
        2>&1 | grep -v "Authorization" >> "$LOG_FILE"
    
    log "=== Deployment Completed ==="
}

main "$@"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ Never hardcode credentials
- ✅ Use environment variables
- ✅ `read -s` for user input
- ✅ GPG for encryption
- ✅ Permissions: 600 for files

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Credentials kahan store karu?**
A: Environment variables (production), encrypted files (local), or vault services.

**Q2: `.env` file secure hai?**
A: Haan, agar permissions 600 hain aur `.gitignore` mein hai.

**Q3: Logs mein password aa gaya toh?**
A: Sed/regex se mask karo: `sed 's/password=[^ ]*/password=***/g'`

### 14. **Practice ke liye Task**

```bash
# 1. Environment variable
export DB_PASS="secret123"
echo $DB_PASS

# 2. Silent read
read -s -p "Password: " pass
echo
echo "You entered: $pass"

# 3. Encrypt with GPG
echo "my_secret" | gpg -e -r your@email.com > secret.gpg
gpg -d secret.gpg

# 4. Secure .env file
cat > .env <<EOF
DB_USER=admin
DB_PASS=secret
EOF
chmod 600 .env
source .env

# 5. Mask in logs
echo "password=secret123" | sed 's/password=[^ ]*/password=***/g'
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔐 Never hardcode credentials
- 🌍 Environment variables best
- 🤫 `read -s` for silent input
- 🔒 GPG for encryption
- 📝 Mask credentials in logs

> **💡 Ye Zaroor Yaad Rakhein:**
> Credentials kabhi hardcode mat karo! Environment variables ya encrypted files use karo. Permissions 600 rakho. Logs mein passwords mask karo. Production mein vault services use karo!

---

# **🎉 Module 12 Complete! 🎉**

Congratulations! Aapne **Module 12: Robust Scripting & Error Handling** successfully complete kar liya hai!

## **Aapne Kya Seekha:**
✅ **Exit Status** - `$?` aur error detection
✅ **Script Exit Codes** - `exit 0`, `exit 1`
✅ **Debugging** - `set -x`, `set -e`, `set -u`, `set -o pipefail`
✅ **trap Command** - Cleanup on exit
✅ **Error Logging** - stderr, log files
✅ **Secure Credentials** - Environment vars, GPG

## **Key Concepts:**

```bash
#!/bin/bash
# Robust script template

set -euo pipefail

readonly LOG_FILE="/var/log/script.log"

log() {
    echo "[$(date)] $1" | tee -a "$LOG_FILE"
}

error() {
    echo "[ERROR] $1" >&2
    log "ERROR: $1"
}

cleanup() {
    log "Cleanup started"
    rm -f /tmp/temp_$$_*
}

trap cleanup EXIT
trap 'error "Failed at line $LINENO"' ERR

# Load credentials securely
DB_PASS="${DB_PASS:-}"
[ -z "$DB_PASS" ] && read -s -p "Password: " DB_PASS

# Main logic
main() {
    log "Script started"
    
    # Your code here
    
    log "Script completed"
    exit 0
}

main "$@"
```

## **Best Practices Summary:**
- ✅ `set -euo pipefail` har script mein
- ✅ `trap cleanup EXIT` for cleanup
- ✅ Exit codes meaningful rakho
- ✅ Errors stderr par bhejo (`>&2`)
- ✅ Timestamps in logs
- ✅ Credentials secure rakho
- ✅ `$?` immediately check karo

## **Production Script Checklist:**
- [ ] Shebang: `#!/bin/bash`
- [ ] Strict mode: `set -euo pipefail`
- [ ] Trap for cleanup
- [ ] Error handling
- [ ] Logging (stdout + file)
- [ ] Exit codes
- [ ] Secure credentials
- [ ] Comments & documentation

## **Common Patterns:**

```bash
# Error handling
command || { error "Command failed"; exit 1; }

# Logging
log "INFO" "Message"
error "ERROR" "Problem"

# Cleanup
trap 'rm -f /tmp/temp_*' EXIT

# Credentials
read -s -p "Password: " pass
export DB_PASS="$pass"

# Debug mode
[ "${DEBUG:-false}" = "true" ] && set -x
```

## **Next Steps:**
Aap ab ready hain **Module 13: Powerful Text Processing** ke liye! Aage seekhenge `grep`, `sed`, `awk`, aur advanced text manipulation!

---

**💡 Remember:** Robust scripts production-ready hoti hain! Error handling, logging, aur security ko kabhi ignore mat karo. Yeh practices aapko professional developer banati hain! 🚀

---
