# **Bash Shell Scripting: Zero-to-Automation Notes (Module 8)**

---

## **PART 2: THE CORE OF SCRIPTING**

---

# **Module 8: Loops & Control**

---

## **Topic 1: `for` Loop (List-based: `for i in {1..5}`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**for Loop (List-based)** - List ke har item par iterate karna.

### 2. **Ye Kya Hai? (What is it?)**
List-based `for` loop ek list ke har element par ek-ek karke kaam karta hai. List files, numbers, strings, ya kuch bhi ho sakti hai.

**Analogy:** Socho ki aapke paas ek playlist hai. For loop har song ko ek-ek karke play karta hai - pehla song, phir doosra, phir teesra.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Iteration** - Multiple items process karna
- ✅ **Automation** - Repetitive tasks
- ✅ **File processing** - Batch operations
- ✅ **Data processing** - Arrays, lists handle karna

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Multiple files process karni hon
- List of items par kaam karna ho
- Range of numbers iterate karni ho
- Array elements process karne hon

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Manual repetition (time waste)
- Code duplication
- Batch operations impossible
- Automation limited

### 6. **Syntax aur Common Options**

```bash
# Basic list
for item in item1 item2 item3; do
    commands
done

# Range (brace expansion)
for i in {1..10}; do
    commands
done

# Files
for file in *.txt; do
    commands
done

# Command output
for user in $(cat users.txt); do
    commands
done

# Array
for item in "${array[@]}"; do
    commands
done
```

### 7. **Example 1 (Basic)**

```bash
# Simple list
for name in Alice Bob Charlie; do
    echo "Hello, $name"
done

# Number range
for i in {1..5}; do
    echo "Number: $i"
done

# Files
for file in *.txt; do
    echo "Processing: $file"
done

# Step range
for i in {0..10..2}; do
    echo "Even: $i"
done
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Batch file processor

process_images() {
    local source_dir=$1
    local dest_dir=$2
    
    mkdir -p "$dest_dir"
    
    for img in "$source_dir"/*.{jpg,png,gif}; do
        [[ -f $img ]] || continue
        
        filename=$(basename "$img")
        name="${filename%.*}"
        ext="${filename##*.}"
        
        echo "Processing: $filename"
        
        # Resize
        convert "$img" -resize 800x600 "$dest_dir/${name}_resized.$ext"
        
        # Thumbnail
        convert "$img" -resize 150x150 "$dest_dir/${name}_thumb.$ext"
        
        echo "  ✓ Created resized and thumbnail"
    done
}

# Backup multiple directories
backup_dirs() {
    local backup_root="/backups/$(date +%Y%m%d)"
    
    for dir in /home /etc /var/www; do
        [[ -d $dir ]] || continue
        
        echo "Backing up: $dir"
        
        dir_name=$(basename "$dir")
        tar -czf "$backup_root/${dir_name}.tar.gz" "$dir" 2>/dev/null
        
        if [[ $? -eq 0 ]]; then
            echo "  ✓ Backup successful"
        else
            echo "  ✗ Backup failed"
        fi
    done
}

# User creation from list
create_users() {
    local user_list=$1
    
    while IFS=: read -r username fullname email; do
        echo "Creating user: $username"
        
        if id "$username" &>/dev/null; then
            echo "  ⚠️  User already exists"
            continue
        fi
        
        useradd -m -c "$fullname" "$username"
        echo "  ✓ User created"
        
        # Send welcome email
        echo "Welcome $fullname" | mail -s "Account Created" "$email"
    done < "$user_list"
}

# Process log files
analyze_logs() {
    for log in /var/log/app/*.log; do
        [[ -f $log ]] || continue
        
        filename=$(basename "$log")
        echo "Analyzing: $filename"
        
        errors=$(grep -c "ERROR" "$log")
        warnings=$(grep -c "WARN" "$log")
        
        echo "  Errors: $errors"
        echo "  Warnings: $warnings"
        
        if [[ $errors -gt 0 ]]; then
            echo "  ⚠️  Errors found, check log"
        fi
    done
}

process_images "/data/images" "/data/processed"
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Quotes bhoolna:** `for file in *.txt` spaces wale names break karenge
- ❌ **Globbing fail:** Agar koi file nahi toh loop literal string par chalega
- ❌ **IFS issues:** Word splitting problems

### 10. **Best Practices / Pro Tips**
- 💡 **Quotes use karo:** `"$item"` safe hai
- 💡 **Check existence:** `[[ -f $file ]]` pehle check karo
- 💡 **Arrays prefer:** `"${array[@]}"` safer than command substitution
- 💡 **Nullglob:** `shopt -s nullglob` agar files nahi hon

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Server deployment script

SERVERS=("web1.example.com" "web2.example.com" "web3.example.com")
APP_DIR="/var/www/app"
DEPLOY_USER="deploy"

echo "=== Deploying to ${#SERVERS[@]} servers ==="

for server in "${SERVERS[@]}"; do
    echo ""
    echo "Deploying to: $server"
    
    # Check connectivity
    if ! ping -c 1 "$server" &>/dev/null; then
        echo "  ✗ Server unreachable"
        continue
    fi
    
    # Deploy
    echo "  Uploading files..."
    if scp -r ./dist/* "$DEPLOY_USER@$server:$APP_DIR/"; then
        echo "  ✓ Files uploaded"
    else
        echo "  ✗ Upload failed"
        continue
    fi
    
    # Restart service
    echo "  Restarting service..."
    if ssh "$DEPLOY_USER@$server" "systemctl restart app"; then
        echo "  ✓ Service restarted"
    else
        echo "  ✗ Restart failed"
    fi
    
    echo "  ✓ Deployment complete"
done

echo ""
echo "=== Deployment finished ==="
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `for item in list; do ... done`
- ✅ `{1..10}` range ke liye
- ✅ `*.txt` files ke liye
- ✅ `"${array[@]}"` arrays ke liye
- ✅ Quotes aur checks zaroori

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: Agar koi file match nahi hui toh?**
A: Loop literal string par chalega. `shopt -s nullglob` use karo ya check karo.

**Q2: Spaces wale filenames kaise handle karu?**
A: Quotes use karo: `for file in *.txt; do echo "$file"; done`

**Q3: Command output par loop kaise?**
A: `for item in $(command); do` lekin arrays prefer karo.

### 14. **Practice ke liye Task**

```bash
# 1. Simple list
for fruit in apple banana cherry; do
    echo "Fruit: $fruit"
done

# 2. Number range
for i in {1..10}; do
    echo "Count: $i"
done

# 3. Files
for file in *.txt; do
    [[ -f $file ]] && echo "File: $file"
done

# 4. Step range
for i in {0..20..5}; do
    echo "Multiple of 5: $i"
done

# 5. Array
colors=("red" "green" "blue")
for color in "${colors[@]}"; do
    echo "Color: $color"
done
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔁 List ke har item par iterate
- 📊 `{1..10}` ranges ke liye
- 📁 `*.txt` file patterns ke liye
- 🎯 Arrays safest option
- 💬 Quotes hamesha use karo

> **💡 Ye Zaroor Yaad Rakhein:**
> For loops automation ka backbone hain! Hamesha quotes use karo, file existence check karo, aur arrays prefer karo command substitution se!

---

## **Topic 2: `for` Loop (C-style: `for (( i=1; i<=10; i++ ))`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**for Loop (C-style)** - Traditional programming jaisa loop with counter.

### 2. **Ye Kya Hai? (What is it?)**
C-style for loop traditional programming languages (C, Java) jaisa syntax use karta hai - initialization, condition, increment. Yeh numeric iterations ke liye perfect hai.

**Analogy:** Socho ki C-style loop ek stopwatch hai jo start se end tak count karta hai, har second par kuch kaam karta hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Numeric iteration** - Counter-based loops
- ✅ **Precise control** - Start, end, step control
- ✅ **Familiar syntax** - C/Java programmers ke liye
- ✅ **Complex conditions** - Multiple variables

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Numeric counters chahiye
- Complex loop conditions
- Multiple variables track karne hon
- Traditional loop syntax prefer karo

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- List-based loops verbose honge
- Counter management manual
- Complex iterations mushkil
- Code less readable

### 6. **Syntax aur Common Options**

```bash
# Basic C-style
for (( i=1; i<=10; i++ )); do
    commands
done

# Custom step
for (( i=0; i<=100; i+=10 )); do
    commands
done

# Decrement
for (( i=10; i>=1; i-- )); do
    commands
done

# Multiple variables
for (( i=0, j=10; i<j; i++, j-- )); do
    commands
done
```

### 7. **Example 1 (Basic)**

```bash
# Count 1 to 10
for (( i=1; i<=10; i++ )); do
    echo "Number: $i"
done

# Even numbers
for (( i=0; i<=20; i+=2 )); do
    echo "Even: $i"
done

# Countdown
for (( i=10; i>=1; i-- )); do
    echo "Countdown: $i"
    sleep 1
done
echo "Blast off!"

# Multiplication table
for (( i=1; i<=10; i++ )); do
    result=$((5 * i))
    echo "5 x $i = $result"
done
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Performance testing script

run_load_test() {
    local url=$1
    local requests=$2
    local concurrent=$3
    
    echo "=== Load Test ==="
    echo "URL: $url"
    echo "Requests: $requests"
    echo "Concurrent: $concurrent"
    
    local success=0
    local failed=0
    
    for (( i=1; i<=requests; i++ )); do
        if (( i % concurrent == 0 )); then
            wait  # Wait for background jobs
        fi
        
        # Send request in background
        {
            if curl -s -o /dev/null -w "%{http_code}" "$url" | grep -q "200"; then
                ((success++))
            else
                ((failed++))
            fi
        } &
        
        # Progress
        if (( i % 10 == 0 )); then
            printf "\rProgress: %d/%d" $i $requests
        fi
    done
    
    wait  # Wait for remaining jobs
    
    echo ""
    echo "Results:"
    echo "  Success: $success"
    echo "  Failed: $failed"
    echo "  Success rate: $(( success * 100 / requests ))%"
}

# Batch file renaming
rename_files() {
    local pattern=$1
    local prefix=$2
    
    local count=1
    
    for file in $pattern; do
        [[ -f $file ]] || continue
        
        ext="${file##*.}"
        new_name="${prefix}_$(printf "%03d" $count).$ext"
        
        mv "$file" "$new_name"
        echo "Renamed: $file → $new_name"
        
        ((count++))
    done
}

# Progress bar
show_progress() {
    local duration=$1
    local steps=50
    
    for (( i=0; i<=steps; i++ )); do
        percent=$(( i * 100 / steps ))
        bar=$(printf "%${i}s" | tr ' ' '█')
        spaces=$(printf "%$((steps - i))s")
        
        printf "\r[%s%s] %d%%" "$bar" "$spaces" "$percent"
        
        sleep $(echo "$duration / $steps" | bc -l)
    done
    
    echo ""
}

# Matrix multiplication
matrix_multiply() {
    local size=$1
    
    echo "Multiplying ${size}x${size} matrices..."
    
    for (( i=0; i<size; i++ )); do
        for (( j=0; j<size; j++ )); do
            sum=0
            for (( k=0; k<size; k++ )); do
                ((sum += i * j * k))
            done
            result[i*size+j]=$sum
        done
    done
    
    echo "Multiplication complete"
}

run_load_test "http://localhost:8080" 100 10
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Spaces galat:** `for((i=1;i<=10;i++))` galat, spaces chahiye
- ❌ **`$` use karna:** `for (( $i=1; ... ))` galat, `for (( i=1; ... ))` sahi
- ❌ **Infinite loops:** Condition check karo

### 10. **Best Practices / Pro Tips**
- 💡 **Spaces use karo:** Readability ke liye
- 💡 **No `$` inside:** Variables directly use karo
- 💡 **Infinite loop check:** Condition validate karo
- 💡 **Performance:** Numeric operations fast hain

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Database backup rotation

DB_NAME="production"
BACKUP_DIR="/backups/database"
KEEP_DAYS=7

echo "=== Database Backup Rotation ==="

# Create new backup
echo "Creating backup..."
backup_file="$BACKUP_DIR/${DB_NAME}_$(date +%Y%m%d_%H%M%S).sql"
mysqldump "$DB_NAME" > "$backup_file"
gzip "$backup_file"

echo "✓ Backup created: ${backup_file}.gz"

# Count and cleanup old backups
backup_count=$(ls -1 "$BACKUP_DIR"/${DB_NAME}_*.sql.gz 2>/dev/null | wc -l)

echo "Total backups: $backup_count"

if (( backup_count > KEEP_DAYS )); then
    to_delete=$(( backup_count - KEEP_DAYS ))
    echo "Deleting $to_delete old backups..."
    
    deleted=0
    for backup in $(ls -t "$BACKUP_DIR"/${DB_NAME}_*.sql.gz | tail -n "$to_delete"); do
        echo "  Deleting: $(basename $backup)"
        rm "$backup"
        ((deleted++))
    done
    
    echo "✓ Deleted $deleted backups"
fi

# Verify backups
echo ""
echo "Current backups:"
for (( i=1; i<=KEEP_DAYS; i++ )); do
    backup=$(ls -t "$BACKUP_DIR"/${DB_NAME}_*.sql.gz 2>/dev/null | sed -n "${i}p")
    if [[ -n $backup ]]; then
        size=$(du -h "$backup" | cut -f1)
        date=$(stat -c %y "$backup" | cut -d' ' -f1)
        echo "  $i. $(basename $backup) - $size - $date"
    fi
done
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `for (( init; condition; increment ))`
- ✅ C/Java jaisa syntax
- ✅ Numeric iterations perfect
- ✅ No `$` inside `(())`
- ✅ Spaces zaroori

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: List-based aur C-style mein kab kaunsa use karu?**
A: Lists/files ke liye list-based, numeric counters ke liye C-style.

**Q2: Kya multiple variables use kar sakte hain?**
A: Haan! `for (( i=0, j=10; i<j; i++, j-- ))`

**Q3: Infinite loop kaise banau?**
A: `for (( ; ; )); do ... done` ya `while true; do ... done`

### 14. **Practice ke liye Task**

```bash
# 1. Basic counter
for (( i=1; i<=5; i++ )); do
    echo "Count: $i"
done

# 2. Custom step
for (( i=0; i<=100; i+=10 )); do
    echo "Value: $i"
done

# 3. Countdown
for (( i=10; i>=1; i-- )); do
    echo "$i..."
    sleep 1
done

# 4. Multiplication table
for (( i=1; i<=10; i++ )); do
    echo "7 x $i = $((7 * i))"
done

# 5. Multiple variables
for (( i=0, j=10; i<=j; i++, j-- )); do
    echo "i=$i, j=$j"
done
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔢 C-style syntax: `for (( i=1; i<=10; i++ ))`
- 🎯 Numeric iterations ke liye perfect
- 🚫 No `$` inside `(())`
- ⚙️ Init, condition, increment control
- 📊 Complex counters handle kar sakta hai

> **💡 Ye Zaroor Yaad Rakhein:**
> C-style loops numeric iterations ke liye best hain! No `$` inside, spaces use karo, aur condition validate karo infinite loops se bachne ke liye!

---

## **Topic 3: `while` Loop (`while [ ... ]`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**while Loop** - Jab tak condition true hai tab tak repeat karo.

### 2. **Ye Kya Hai? (What is it?)**
`while` loop tab tak chalta rahta hai jab tak condition true hai. Jaise hi condition false hui, loop band ho jaata hai. Yeh unknown iterations ke liye perfect hai.

**Analogy:** Socho ki while loop ek guard hai jo gate par khada hai. Jab tak pass valid hai (condition true), andar jaane deta hai. Pass invalid hua (condition false), gate band.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Unknown iterations** - Jab pata nahi kitni baar
- ✅ **Condition-based** - Dynamic stopping
- ✅ **File reading** - Line-by-line processing
- ✅ **User input** - Until valid input

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- File line-by-line read karni ho
- User input validate karna ho
- Condition-based loops
- Monitoring scripts

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- For loops verbose honge
- File reading mushkil
- Infinite loops ka risk
- Dynamic conditions handle nahi kar paoge

### 6. **Syntax aur Common Options**

```bash
# Basic while
while [ condition ]; do
    commands
done

# Read file
while IFS= read -r line; do
    commands
done < file.txt

# Infinite loop
while true; do
    commands
done

# Until (opposite of while)
until [ condition ]; do
    commands
done
```

### 7. **Example 1 (Basic)**

```bash
# Counter
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done

# User input
while true; do
    read -p "Enter password: " pass
    if [[ $pass == "secret" ]]; then
        echo "Access granted"
        break
    else
        echo "Wrong password, try again"
    fi
done

# File reading
while IFS= read -r line; do
    echo "Line: $line"
done < data.txt

# Until loop
count=1
until [ $count -gt 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Service monitor

monitor_service() {
    local service=$1
    local check_interval=5
    local max_failures=3
    local failures=0
    
    echo "Monitoring: $service"
    
    while true; do
        if systemctl is-active --quiet "$service"; then
            echo "[$(date '+%H:%M:%S')] ✓ $service is running"
            failures=0
        else
            ((failures++))
            echo "[$(date '+%H:%M:%S')] ✗ $service is down (failure $failures/$max_failures)"
            
            if [ $failures -ge $max_failures ]; then
                echo "Max failures reached. Attempting restart..."
                
                if systemctl restart "$service"; then
                    echo "✓ Service restarted successfully"
                    failures=0
                else
                    echo "✗ Restart failed. Sending alert..."
                    echo "$service failed on $(hostname)" | mail -s "Service Alert" admin@example.com
                fi
            fi
        fi
        
        sleep $check_interval
    done
}

# Log file processor
process_logs() {
    local log_file=$1
    local error_count=0
    local warning_count=0
    
    while IFS= read -r line; do
        # Skip empty lines
        [[ -z $line ]] && continue
        
        # Count errors
        if [[ $line == *ERROR* ]]; then
            ((error_count++))
            echo "ERROR: $line"
        fi
        
        # Count warnings
        if [[ $line == *WARN* ]]; then
            ((warning_count++))
        fi
        
    done < "$log_file"
    
    echo ""
    echo "Summary:"
    echo "  Errors: $error_count"
    echo "  Warnings: $warning_count"
}

# Interactive menu
show_menu() {
    while true; do
        clear
        echo "=== System Menu ==="
        echo "1. Check disk space"
        echo "2. Check memory"
        echo "3. List processes"
        echo "4. Exit"
        echo "==================="
        
        read -p "Enter choice [1-4]: " choice
        
        case $choice in
            1)
                df -h
                read -p "Press Enter to continue..."
                ;;
            2)
                free -h
                read -p "Press Enter to continue..."
                ;;
            3)
                ps aux | head -20
                read -p "Press Enter to continue..."
                ;;
            4)
                echo "Goodbye!"
                break
                ;;
            *)
                echo "Invalid choice"
                sleep 2
                ;;
        esac
    done
}

# Wait for file
wait_for_file() {
    local file=$1
    local timeout=${2:-60}
    local elapsed=0
    
    echo "Waiting for file: $file"
    
    while [ ! -f "$file" ]; do
        if [ $elapsed -ge $timeout ]; then
            echo "✗ Timeout waiting for file"
            return 1
        fi
        
        echo "  Waiting... ($elapsed/$timeout seconds)"
        sleep 5
        ((elapsed += 5))
    done
    
    echo "✓ File found: $file"
    return 0
}

show_menu
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Infinite loops:** Condition kabhi false nahi hoti
- ❌ **File reading galat:** `while read line` ki jagah `while IFS= read -r line`
- ❌ **Counter update bhoolna:** Loop kabhi end nahi hoga

### 10. **Best Practices / Pro Tips**
- 💡 **`IFS= read -r`:** File reading ke liye proper syntax
- 💡 **Break condition:** Hamesha exit strategy rakho
- 💡 **Sleep use karo:** Monitoring loops mein
- 💡 **Timeout implement:** Infinite wait avoid karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Database connection retry

connect_database() {
    local host=$1
    local max_retries=5
    local retry_delay=3
    local attempt=1
    
    echo "Connecting to database: $host"
    
    while [ $attempt -le $max_retries ]; do
        echo "Attempt $attempt/$max_retries..."
        
        if mysql -h "$host" -u root -p"$DB_PASS" -e "SELECT 1" &>/dev/null; then
            echo "✓ Connected successfully"
            return 0
        else
            echo "✗ Connection failed"
            
            if [ $attempt -lt $max_retries ]; then
                echo "Retrying in $retry_delay seconds..."
                sleep $retry_delay
            fi
        fi
        
        ((attempt++))
    done
    
    echo "✗ Failed to connect after $max_retries attempts"
    return 1
}

# CSV file processor
process_csv() {
    local csv_file=$1
    local line_num=0
    local processed=0
    local errors=0
    
    while IFS=',' read -r id name email status; do
        ((line_num++))
        
        # Skip header
        [ $line_num -eq 1 ] && continue
        
        # Validate data
        if [[ -z $id || -z $email ]]; then
            echo "Line $line_num: Missing required fields"
            ((errors++))
            continue
        fi
        
        # Process record
        echo "Processing: $name ($email)"
        
        # Insert into database
        if mysql -e "INSERT INTO users VALUES ('$id', '$name', '$email', '$status')"; then
            ((processed++))
        else
            ((errors++))
        fi
        
    done < "$csv_file"
    
    echo ""
    echo "Processing complete:"
    echo "  Total lines: $line_num"
    echo "  Processed: $processed"
    echo "  Errors: $errors"
}

connect_database "localhost"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `while [ condition ]; do ... done`
- ✅ Condition-based iteration
- ✅ `while IFS= read -r line` file reading
- ✅ `while true` infinite loop
- ✅ Break condition zaroori

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `while` aur `until` mein kya fark hai?**
A: `while` jab tak true, `until` jab tak false. Opposite logic.

**Q2: File reading mein `IFS=` kyun?**
A: Leading/trailing whitespace preserve karne ke liye.

**Q3: Infinite loop se kaise nikalu?**
A: `break` statement ya Ctrl+C.

### 14. **Practice ke liye Task**

```bash
# 1. Basic counter
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done

# 2. User input
while true; do
    read -p "Enter 'quit' to exit: " input
    [[ $input == "quit" ]] && break
    echo "You entered: $input"
done

# 3. File reading
while IFS= read -r line; do
    echo "Line: $line"
done < /etc/passwd

# 4. Until loop
num=1
until [ $num -gt 5 ]; do
    echo "Number: $num"
    ((num++))
done

# 5. Monitoring
while true; do
    clear
    date
    uptime
    sleep 5
done
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🔁 Condition true tak repeat
- 📄 File reading: `while IFS= read -r line`
- ♾️ `while true` infinite loop
- 🚪 `break` se exit karo
- ⏱️ Monitoring ke liye perfect

> **💡 Ye Zaroor Yaad Rakhein:**
> While loops condition-based iterations ke liye perfect hain! File reading mein `IFS= read -r` use karo, infinite loops mein break condition rakho!

---

## **Topic 4: `break` Statement**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**break Statement** - Loop se turant bahar nikalna.

### 2. **Ye Kya Hai? (What is it?)**
`break` statement loop ko immediately terminate kar deta hai - chahe condition true ho ya false. Yeh early exit ke liye use hota hai jab koi specific condition mil jaye.

**Analogy:** Socho ki aap ek maze mein hain. Break ek emergency exit hai jo aapko directly bahar le jaata hai, bina poora maze complete kiye.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Early exit** - Unnecessary iterations avoid
- ✅ **Efficiency** - Time save karna
- ✅ **Search operations** - Found hone par stop
- ✅ **Error handling** - Critical error par exit

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Search operations mein
- Validation fail hone par
- User input "quit" kare
- Error conditions

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Unnecessary iterations
- Performance waste
- Complex exit logic
- Code verbose

### 6. **Syntax aur Common Options**

```bash
# Basic break
while condition; do
    if [ some_condition ]; then
        break
    fi
done

# Break from nested loops
for i in {1..10}; do
    for j in {1..10}; do
        if [ condition ]; then
            break 2  # Break 2 levels
        fi
    done
done

# Break with status
break  # Exit innermost loop
```

### 7. **Example 1 (Basic)**

```bash
# Search in array
names=("Alice" "Bob" "Charlie" "David")
search="Charlie"

for name in "${names[@]}"; do
    if [[ $name == $search ]]; then
        echo "Found: $name"
        break
    fi
done

# User input
while true; do
    read -p "Enter command (quit to exit): " cmd
    
    if [[ $cmd == "quit" ]]; then
        echo "Exiting..."
        break
    fi
    
    echo "You entered: $cmd"
done

# File search
while IFS= read -r line; do
    if [[ $line == *ERROR* ]]; then
        echo "Error found: $line"
        break
    fi
done < logfile.txt
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Advanced break usage

# Find first available port
find_free_port() {
    local start_port=8000
    local end_port=9000
    
    echo "Searching for free port..."
    
    for (( port=start_port; port<=end_port; port++ )); do
        if ! nc -z localhost $port 2>/dev/null; then
            echo "✓ Found free port: $port"
            return $port
        fi
        
        # Stop after checking 100 ports
        if (( port - start_port >= 100 )); then
            echo "⚠️  Checked 100 ports, stopping search"
            break
        fi
    done
    
    echo "✗ No free port found"
    return 1
}

# Process files until error
process_batch() {
    local files=("$@")
    local processed=0
    
    for file in "${files[@]}"; do
        echo "Processing: $file"
        
        if [[ ! -f $file ]]; then
            echo "✗ File not found: $file"
            echo "Stopping batch processing"
            break
        fi
        
        if ! process_file "$file"; then
            echo "✗ Processing failed: $file"
            echo "Stopping batch processing"
            break
        fi
        
        ((processed++))
    done
    
    echo "Processed $processed files"
}

# Nested loop with break
find_in_matrix() {
    local target=$1
    local found=false
    
    for (( i=0; i<10; i++ )); do
        for (( j=0; j<10; j++ )); do
            value=$((i * 10 + j))
            
            if [ $value -eq $target ]; then
                echo "Found $target at position [$i,$j]"
                found=true
                break 2  # Break both loops
            fi
        done
    done
    
    if [ "$found" = false ]; then
        echo "Value $target not found"
    fi
}

# Retry with break
retry_operation() {
    local max_attempts=5
    local attempt=1
    
    while [ $attempt -le $max_attempts ]; do
        echo "Attempt $attempt/$max_attempts"
        
        if perform_operation; then
            echo "✓ Operation successful"
            break
        fi
        
        if [ $attempt -eq $max_attempts ]; then
            echo "✗ All attempts failed"
            return 1
        fi
        
        echo "Retrying..."
        sleep 2
        ((attempt++))
    done
    
    return 0
}

find_in_matrix 42
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`break` outside loop:** Error dega
- ❌ **Nested loops:** `break` sirf innermost se nikalta hai
- ❌ **Overuse:** Har jagah break mat use karo

### 10. **Best Practices / Pro Tips**
- 💡 **Early exit:** Jaldi mil gaya toh break karo
- 💡 **`break N`:** N levels break karne ke liye
- 💡 **Clear conditions:** Break condition clear rakho
- 💡 **Cleanup:** Break se pehle cleanup karo if needed

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Server health check with break

check_servers() {
    local servers=("web1" "web2" "web3" "db1" "db2")
    local critical_failure=false
    
    for server in "${servers[@]}"; do
        echo "Checking: $server"
        
        if ! ping -c 1 "$server" &>/dev/null; then
            echo "✗ $server is unreachable"
            
            # Check if critical server
            if [[ $server == db* ]]; then
                echo "⚠️  CRITICAL: Database server down!"
                critical_failure=true
                break  # Stop checking, alert immediately
            fi
        else
            echo "✓ $server is up"
        fi
    done
    
    if [ "$critical_failure" = true ]; then
        echo "Sending critical alert..."
        echo "Database server down!" | mail -s "CRITICAL ALERT" admin@example.com
        return 1
    fi
    
    return 0
}

# Configuration validator
validate_config() {
    local config_file=$1
    local errors=0
    
    while IFS='=' read -r key value; do
        [[ -z $key || $key == \#* ]] && continue
        
        # Check required fields
        case "$key" in
            "DB_HOST"|"DB_NAME"|"DB_USER")
                if [[ -z $value ]]; then
                    echo "✗ Missing required field: $key"
                    ((errors++))
                    
                    if [ $errors -ge 3 ]; then
                        echo "Too many errors, stopping validation"
                        break
                    fi
                fi
                ;;
        esac
    done < "$config_file"
    
    return $errors
}

check_servers
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `break` loop se exit karta hai
- ✅ Early exit ke liye useful
- ✅ `break N` nested loops ke liye
- ✅ Search operations mein efficient
- ✅ Error handling mein helpful

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `break` aur `exit` mein kya fark hai?**
A: `break` loop se nikalta hai, `exit` poori script terminate karta hai.

**Q2: Nested loops se kaise nikalu?**
A: `break 2` (2 levels), `break 3` (3 levels), etc.

**Q3: `break` ke baad code execute hota hai?**
A: Loop ke baad ka code execute hota hai, loop ke andar ka nahi.

### 14. **Practice ke liye Task**

```bash
# 1. Simple break
for i in {1..10}; do
    echo $i
    [[ $i -eq 5 ]] && break
done

# 2. Search with break
for name in Alice Bob Charlie; do
    if [[ $name == "Bob" ]]; then
        echo "Found: $name"
        break
    fi
done

# 3. User input
while true; do
    read -p "Enter (q to quit): " input
    [[ $input == "q" ]] && break
    echo "You entered: $input"
done

# 4. Nested loops
for i in {1..5}; do
    for j in {1..5}; do
        echo "[$i,$j]"
        [[ $i -eq 3 && $j -eq 3 ]] && break 2
    done
done
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🚪 Loop se immediately exit
- 🎯 Early exit ke liye efficient
- 🔢 `break N` nested loops ke liye
- 🔍 Search operations perfect
- ⚠️ Cleanup before break if needed

> **💡 Ye Zaroor Yaad Rakhein:**
> Break statement efficiency ka tool hai! Jaldi mil gaya toh break karo, unnecessary iterations avoid karo. Nested loops ke liye `break N` use karo!

---

## **Topic 5: `case` Statement (Menu-driven logic)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**case Statement** - Multiple conditions ko elegantly handle karna.

### 2. **Ye Kya Hai? (What is it?)**
`case` statement ek variable ko multiple values ke against match karta hai - jaise switch statement programming languages mein. Yeh multiple if-elif chains ka clean alternative hai.

**Analogy:** Socho ki case statement ek sorting machine hai jo items ko unke type ke hisaab se alag-alag bins mein dalta hai - ek glance mein pata chal jaata hai kahan jaana hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Readability** - Clean aur organized code
- ✅ **Menu systems** - Interactive scripts
- ✅ **Pattern matching** - Wildcards support
- ✅ **Efficiency** - Multiple if-elif se better

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Menu-driven scripts
- File type detection
- Command-line argument parsing
- Multiple fixed options

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Long if-elif chains (messy)
- Code duplication
- Poor readability
- Maintenance mushkil

### 6. **Syntax aur Common Options**

```bash
case $variable in
    pattern1)
        commands
        ;;
    pattern2)
        commands
        ;;
    pattern3|pattern4)
        commands
        ;;
    *)
        default commands
        ;;
esac
```

**Pattern Matching:**
- `*` : Any string
- `?` : Any single character
- `[...]` : Character class
- `|` : OR (multiple patterns)

### 7. **Example 1 (Basic)**

```bash
# Simple menu
read -p "Enter choice (a/b/c): " choice

case $choice in
    a)
        echo "You chose A"
        ;;
    b)
        echo "You chose B"
        ;;
    c)
        echo "You chose C"
        ;;
    *)
        echo "Invalid choice"
        ;;
esac

# File type detection
file="document.txt"

case $file in
    *.txt)
        echo "Text file"
        ;;
    *.jpg|*.png|*.gif)
        echo "Image file"
        ;;
    *.sh)
        echo "Shell script"
        ;;
    *)
        echo "Unknown type"
        ;;
esac

# Yes/No prompt
read -p "Continue? (y/n): " answer

case $answer in
    y|Y|yes|Yes|YES)
        echo "Continuing..."
        ;;
    n|N|no|No|NO)
        echo "Stopping..."
        exit 0
        ;;
    *)
        echo "Invalid input"
        ;;
esac
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# System management menu

show_menu() {
    clear
    cat << 'EOF'
╔════════════════════════════════╗
║   SYSTEM MANAGEMENT MENU       ║
╚════════════════════════════════╝

1. System Information
2. Disk Usage
3. Memory Usage
4. Network Status
5. Process Management
6. Service Control
7. Backup Operations
8. Exit

EOF
}

system_info() {
    echo "=== System Information ==="
    echo "Hostname: $(hostname)"
    echo "Kernel: $(uname -r)"
    echo "Uptime: $(uptime -p)"
    echo "Users: $(who | wc -l)"
}

disk_usage() {
    echo "=== Disk Usage ==="
    df -h | grep -v "tmpfs"
}

memory_usage() {
    echo "=== Memory Usage ==="
    free -h
}

network_status() {
    echo "=== Network Status ==="
    ip addr show | grep "inet "
    echo ""
    echo "Active connections:"
    ss -tuln | head -10
}

process_menu() {
    echo "Process Management:"
    echo "1. Top processes"
    echo "2. Kill process"
    echo "3. Back"
    
    read -p "Choice: " pchoice
    
    case $pchoice in
        1)
            ps aux --sort=-%mem | head -20
            ;;
        2)
            read -p "Enter PID: " pid
            if kill -0 "$pid" 2>/dev/null; then
                kill "$pid" && echo "Process killed"
            else
                echo "Invalid PID"
            fi
            ;;
        3)
            return
            ;;
    esac
}

service_control() {
    echo "Service Control:"
    echo "1. List services"
    echo "2. Start service"
    echo "3. Stop service"
    echo "4. Restart service"
    
    read -p "Choice: " schoice
    
    case $schoice in
        1)
            systemctl list-units --type=service --state=running
            ;;
        2|3|4)
            read -p "Service name: " service
            
            case $schoice in
                2) systemctl start "$service" ;;
                3) systemctl stop "$service" ;;
                4) systemctl restart "$service" ;;
            esac
            
            systemctl status "$service"
            ;;
    esac
}

backup_operations() {
    echo "Backup Operations:"
    echo "1. Create backup"
    echo "2. List backups"
    echo "3. Restore backup"
    
    read -p "Choice: " bchoice
    
    case $bchoice in
        1)
            backup_file="/backups/backup_$(date +%Y%m%d_%H%M%S).tar.gz"
            tar -czf "$backup_file" /home
            echo "Backup created: $backup_file"
            ;;
        2)
            ls -lh /backups/*.tar.gz 2>/dev/null || echo "No backups found"
            ;;
        3)
            echo "Available backups:"
            ls /backups/*.tar.gz 2>/dev/null
            read -p "Enter backup file: " backup
            tar -xzf "$backup" -C /
            ;;
    esac
}

# Main loop
while true; do
    show_menu
    read -p "Enter choice [1-8]: " choice
    
    case $choice in
        1)
            system_info
            ;;
        2)
            disk_usage
            ;;
        3)
            memory_usage
            ;;
        4)
            network_status
            ;;
        5)
            process_menu
            ;;
        6)
            service_control
            ;;
        7)
            backup_operations
            ;;
        8)
            echo "Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter 1-8."
            ;;
    esac
    
    echo ""
    read -p "Press Enter to continue..."
done
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`;;` bhoolna:** Har case ko `;;` se close karo
- ❌ **`esac` bhoolna:** `case` ko `esac` se close karo
- ❌ **Default case nahi:** `*)` hamesha add karo

### 10. **Best Practices / Pro Tips**
- 💡 **Default case:** `*)` hamesha include karo
- 💡 **Multiple patterns:** `|` se combine karo
- 💡 **Wildcards:** Pattern matching powerful hai
- 💡 **Indentation:** Readable code ke liye

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

```bash
#!/bin/bash
# Deployment script with environment selection

ENVIRONMENT=$1

case $ENVIRONMENT in
    dev|development)
        echo "Deploying to DEVELOPMENT"
        SERVER="dev.example.com"
        DB_NAME="myapp_dev"
        DEBUG=true
        ;;
        
    staging|stage)
        echo "Deploying to STAGING"
        SERVER="staging.example.com"
        DB_NAME="myapp_staging"
        DEBUG=true
        ;;
        
    prod|production)
        echo "Deploying to PRODUCTION"
        SERVER="prod.example.com"
        DB_NAME="myapp_prod"
        DEBUG=false
        
        # Extra confirmation for production
        read -p "Are you sure? (yes/no): " confirm
        case $confirm in
            yes)
                echo "Proceeding with production deployment..."
                ;;
            *)
                echo "Deployment cancelled"
                exit 0
                ;;
        esac
        ;;
        
    *)
        echo "Usage: $0 {dev|staging|prod}"
        echo ""
        echo "Environments:"
        echo "  dev        - Development environment"
        echo "  staging    - Staging environment"
        echo "  prod       - Production environment"
        exit 1
        ;;
esac

echo "Server: $SERVER"
echo "Database: $DB_NAME"
echo "Debug: $DEBUG"

# Deployment logic here
echo "Deploying application..."
scp -r ./dist/* "deploy@$SERVER:/var/www/app/"
ssh "deploy@$SERVER" "systemctl restart app"

echo "✓ Deployment complete"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `case $var in ... esac`
- ✅ Pattern matching support
- ✅ `|` multiple patterns ke liye
- ✅ `*)` default case
- ✅ `;;` har case ke end mein

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `case` aur `if-elif` mein kab kaunsa use karu?**
A: Fixed options ke liye `case`, complex conditions ke liye `if-elif`.

**Q2: Kya regex use kar sakte hain?**
A: Nahi, sirf shell wildcards (`*`, `?`, `[...]`).

**Q3: Multiple commands ek case mein?**
A: Haan, `;;` se pehle jitne chahiye.

### 14. **Practice ke liye Task**

```bash
# 1. Simple menu
read -p "Choice (1/2/3): " choice
case $choice in
    1) echo "Option 1" ;;
    2) echo "Option 2" ;;
    3) echo "Option 3" ;;
    *) echo "Invalid" ;;
esac

# 2. File type
file="test.txt"
case $file in
    *.txt) echo "Text" ;;
    *.jpg|*.png) echo "Image" ;;
    *) echo "Unknown" ;;
esac

# 3. Yes/No
read -p "Continue? (y/n): " ans
case $ans in
    y|Y) echo "Yes" ;;
    n|N) echo "No" ;;
    *) echo "Invalid" ;;
esac

# 4. Command handler
cmd=$1
case $cmd in
    start) echo "Starting..." ;;
    stop) echo "Stopping..." ;;
    restart) echo "Restarting..." ;;
    *) echo "Usage: $0 {start|stop|restart}" ;;
esac
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🎯 Multiple options elegantly handle
- 🔀 Pattern matching support
- 📋 Menu systems ke liye perfect
- ✨ Cleaner than if-elif chains
- 🎨 Readable aur maintainable

> **💡 Ye Zaroor Yaad Rakhein:**
> Case statements menu-driven scripts ka backbone hain! Pattern matching powerful hai, default case (`*`) hamesha add karo, aur `;;` mat bhoolna!

---

# **🎉 Module 8 Complete! 🎉**

Congratulations! Aapne **Module 8: Loops & Control** successfully complete kar liya hai!

## **Aapne Kya Seekha:**
✅ **for Loop (List-based)** - `for i in list`
✅ **for Loop (C-style)** - `for (( i=1; i<=10; i++ ))`
✅ **while Loop** - `while [ condition ]`
✅ **break Statement** - Loop se exit
✅ **case Statement** - Menu-driven logic

## **Key Patterns:**

```bash
# List-based for
for item in "${array[@]}"; do
    echo "$item"
done

# C-style for
for (( i=1; i<=10; i++ )); do
    echo $i
done

# While loop
while [ condition ]; do
    commands
done

# File reading
while IFS= read -r line; do
    echo "$line"
done < file.txt

# Break
for i in {1..100}; do
    [[ $i -eq 50 ]] && break
done

# Case statement
case $var in
    pattern1) commands ;;
    pattern2) commands ;;
    *) default ;;
esac
```

## **Real-World Applications:**
- **Batch processing:** Multiple files
- **Monitoring:** Service health checks
- **Menus:** Interactive scripts
- **Automation:** Repetitive tasks
- **Data processing:** CSV, logs

## **Best Practices:**
- Use appropriate loop type
- Always quote variables
- Check file existence
- Implement break conditions
- Use case for menus

## **Next Steps:**
Ab aap ready hain **Module 9: Script Parameters & Expansion** ke liye - PART 3 shuru hoga!

---

**📝 Practice Reminder:**
Loops scripting ka powerhouse hain! Daily practice karo:
- Different loop types try karo
- File processing scripts banao
- Interactive menus implement karo
- Break conditions properly use karo

**🎯 Challenge:**
Ek complete system management menu banao jo:
1. Multiple options de (case statement)
2. Files process kare (for loop)
3. Services monitor kare (while loop)
4. Error par exit kare (break)
5. User-friendly ho

Yeh challenge Module 8 ke saare concepts use karega!

---
