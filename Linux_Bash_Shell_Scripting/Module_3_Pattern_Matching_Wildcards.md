# **Bash Shell Scripting: Zero-to-Automation Notes (Module 3)**

---

## **PART 1: THE ABSOLUTE BASICS (Shuruaat)**

---

# **Module 3: Pattern Matching (Wildcards)**

---

## **Topic 1: Star Wildcard (`*`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Star Wildcard (*)** - Ek ya zyada characters ko match karne ke liye powerful pattern.

### 2. **Ye Kya Hai? (What is it?)**
Star wildcard (`*`) ek special character hai jo kisi bhi number of characters (zero se lekar unlimited tak) ko represent karta hai. Yeh file names aur patterns match karne ke liye use hota hai.

**Analogy:** Socho ki `*` ek blank cheque hai jo kisi bhi value ko accept kar sakta hai - zero rupees se lekar crores tak. Similarly, `*` zero characters se lekar unlimited characters tak match kar sakta hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Bulk operations** - Ek saath bahut saari files par kaam karna
- ✅ **Time saving** - Har file ka naam type karne ki zaroorat nahi
- ✅ **Pattern matching** - Similar files ko quickly identify karna
- ✅ **Automation** - Scripts mein dynamic file selection

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Jab similar extension wali files chahiye (*.txt, *.jpg)
- Jab similar naam wali files chahiye (report*, backup*)
- Jab saari files par operation karna ho
- Scripts mein jab file patterns match karne hon

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Har file ka naam manually type karna padega (time waste)
- Bulk operations nahi kar paoge
- Scripts mein flexibility nahi hogi
- Professional automation impossible hoga

### 6. **Syntax aur Common Options**

```bash
# Saari files
*

# Specific extension
*.txt
*.jpg
*.sh

# Specific prefix
report*
backup*
test*

# Specific suffix
*_backup
*_old
*_2024

# Middle pattern
*report*
*backup*
```

**Important Patterns:**
- `*` - Saari files/folders
- `*.ext` - Specific extension wali files
- `prefix*` - Specific prefix se shuru hone wali files
- `*suffix` - Specific suffix se khatam hone wali files
- `*pattern*` - Beech mein pattern wali files

### 7. **Example 1 (Basic)**

```bash
# Saari .txt files list karo
$ ls *.txt
file1.txt  file2.txt  notes.txt

# Saari files jo 'report' se shuru hoti hain
$ ls report*
report_jan.pdf  report_feb.pdf  report_summary.txt

# Saari files jo '_backup' se khatam hoti hain
$ ls *_backup
config_backup  data_backup  script_backup

# Saari files (current directory)
$ ls *
file1.txt  file2.txt  folder1  folder2
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Cleanup script - purani backup files delete karna

BACKUP_DIR="/home/user/backups"
DAYS_OLD=30

echo "Cleaning up old backup files..."

# 30 din se purani .bak files dhoodho aur delete karo
find "$BACKUP_DIR" -name "*.bak" -type f -mtime +$DAYS_OLD -exec rm -v {} \;

# Summary
REMAINING=$(ls -1 "$BACKUP_DIR"/*.bak 2>/dev/null | wc -l)
echo "Cleanup complete! $REMAINING backup files remaining."

# Saari log files ko archive karo
tar -czf logs_archive_$(date +%Y%m%d).tar.gz *.log
echo "All .log files archived!"
```

**Output:**
```
Cleaning up old backup files...
removed '/home/user/backups/old_backup.bak'
removed '/home/user/backups/data_20231215.bak'
Cleanup complete! 5 backup files remaining.
All .log files archived!
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Quotes mein `*` use karna:** `"*.txt"` literally *.txt match karega, expand nahi hoga
- ❌ **Hidden files bhoolna:** `*` hidden files (jo `.` se shuru hoti hain) match nahi karta
- ❌ **Dangerous commands:** `rm -rf *` current directory ki sab kuch delete kar dega!

### 10. **Best Practices / Pro Tips**
- 💡 **Pehle test karo:** `ls *.txt` se dekho kya match ho raha hai, phir `rm *.txt` karo
- 💡 **Double quotes use karo:** Variables ke saath: `"$DIR"/*.txt`
- 💡 **Hidden files ke liye:** `.*` use karo (but careful - `.` aur `..` bhi match honge)
- 💡 **Combine patterns:** `*.{txt,log,bak}` multiple extensions ek saath

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek web developer hain aur aapko project mein saari image files ko optimize karna hai:

```bash
#!/bin/bash
# Image optimization script

IMG_DIR="./images"
OUTPUT_DIR="./images/optimized"

mkdir -p "$OUTPUT_DIR"

echo "Optimizing images..."

# Saari .jpg files optimize karo
for img in "$IMG_DIR"/*.jpg; do
    filename=$(basename "$img")
    convert "$img" -quality 85 "$OUTPUT_DIR/$filename"
    echo "Optimized: $filename"
done

# Saari .png files optimize karo
for img in "$IMG_DIR"/*.png; do
    filename=$(basename "$img")
    pngquant --quality=65-80 "$img" --output "$OUTPUT_DIR/$filename"
    echo "Optimized: $filename"
done

echo "All images optimized!"
```

Yeh script automatically saari images ko process kar dega.

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `*` kisi bhi number of characters ko match karta hai
- ✅ `*.ext` specific extension wali files
- ✅ `prefix*` specific prefix wali files
- ✅ `*suffix` specific suffix wali files
- ✅ Pehle `ls` se test karo, phir dangerous commands use karo

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `*` aur `.*` mein kya fark hai?**
A: `*` normal files match karta hai. `.*` hidden files (jo `.` se shuru hoti hain) match karta hai.

**Q2: Kya `*` folders ko bhi match karta hai?**
A: Haan! `*` files aur folders dono ko match karta hai. Sirf files chahiye toh `find` command use karo.

**Q3: Agar koi file match nahi hui toh kya hoga?**
A: By default, `*` literally print ho jayega. `shopt -s nullglob` set karne se empty list milegi.

### 14. **Practice ke liye Task**

```bash
# 1. Test files banao
touch file1.txt file2.txt file3.txt
touch report_jan.pdf report_feb.pdf
touch data_backup config_backup

# 2. Saari .txt files list karo
ls *.txt

# 3. 'report' se shuru hone wali files
ls report*

# 4. '_backup' se khatam hone wali files
ls *_backup

# 5. Saari files count karo
ls * | wc -l

# 6. Cleanup
rm *.txt report* *_backup
```

### 15. **Aakhri Choti Summary (5 lines)**
- ⭐ `*` sabse powerful wildcard hai - kisi bhi characters ko match karta hai
- 📁 `*.ext` specific file types ke liye perfect
- 🎯 Bulk operations ke liye essential tool
- ⚠️ Dangerous commands se pehle HAMESHA test karo
- 🔒 Quotes aur proper paths use karo safety ke liye

> **💡 Ye Zaroor Yaad Rakhein:**
> Star wildcard (`*`) bahut powerful hai lekin dangerous bhi! Hamesha pehle `ls` se verify karo kya match ho raha hai, phir hi `rm` ya `mv` jaise commands use karo!

---

## **Topic 2: Question Mark Wildcard (`?`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Question Mark Wildcard (?)** - Exactly ek character ko match karne ke liye precise pattern.

### 2. **Ye Kya Hai? (What is it?)**
Question mark wildcard (`?`) exactly ek single character ko represent karta hai - na zyada, na kam. Yeh `*` se zyada specific hai kyunki yeh sirf ek character match karta hai.

**Analogy:** Socho ki `?` ek blank space hai crossword puzzle mein - exactly ek letter ki jagah hai, na zyada na kam. `*` ek elastic band hai jo kitna bhi stretch ho sakta hai, lekin `?` ek fixed size ka box hai.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Precise matching** - Exact length wali files match karna
- ✅ **Pattern specificity** - `*` se zyada control
- ✅ **Numbered files** - file1, file2, file3 jaise patterns
- ✅ **Fixed format files** - Date formats, codes, IDs

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Jab file names ki length fixed ho
- Jab specific positions par characters vary karte hon
- Numbered sequences match karne ke liye
- Date formats ya codes match karne ke liye

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- `*` use karke unwanted files bhi match ho jayengi
- Precise patterns nahi bana paoge
- Fixed-length file names handle karna mushkil hoga
- Automation mein accuracy kam hogi

### 6. **Syntax aur Common Options**

```bash
# Exactly ek character
file?.txt        # file1.txt, fileA.txt (NOT file10.txt)

# Multiple positions
file??.txt       # file01.txt, fileAB.txt

# Specific pattern
data_????.csv    # data_2024.csv, data_test.csv

# Mixed with other patterns
report_202?_??.pdf   # report_2024_01.pdf
```

**Important Patterns:**
- `?` - Exactly 1 character
- `??` - Exactly 2 characters
- `???` - Exactly 3 characters
- `file?.txt` - file + 1 char + .txt
- `????-??-??` - Date format (YYYY-MM-DD)

### 7. **Example 1 (Basic)**

```bash
# Single digit files
$ ls file?.txt
file1.txt  file2.txt  file3.txt

# Two digit files
$ ls file??.txt
file10.txt  file11.txt  file99.txt

# Date pattern (YYYY-MM-DD)
$ ls log_????-??-??.txt
log_2024-01-15.txt  log_2024-01-16.txt

# Mixed pattern
$ ls report_?.pdf
report_A.pdf  report_B.pdf  report_1.pdf
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Backup files ko date-wise organize karna

BACKUP_DIR="/backups"
ARCHIVE_DIR="/backups/archive"

mkdir -p "$ARCHIVE_DIR"

echo "Organizing backup files..."

# YYYY-MM-DD format wali files dhoodho
for file in "$BACKUP_DIR"/backup_????-??-??.tar.gz; do
    if [ -f "$file" ]; then
        # Date extract karo (YYYY-MM)
        filename=$(basename "$file")
        year_month=$(echo "$filename" | grep -oP '\d{4}-\d{2}')
        
        # Month folder banao
        mkdir -p "$ARCHIVE_DIR/$year_month"
        
        # File move karo
        mv -v "$file" "$ARCHIVE_DIR/$year_month/"
    fi
done

echo "Organization complete!"

# Summary
echo "Files organized by month:"
du -sh "$ARCHIVE_DIR"/*
```

**Output:**
```
Organizing backup files...
'backup_2024-01-15.tar.gz' -> 'archive/2024-01/backup_2024-01-15.tar.gz'
'backup_2024-01-16.tar.gz' -> 'archive/2024-01/backup_2024-01-16.tar.gz'
Organization complete!
Files organized by month:
1.2G    archive/2024-01
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **`?` aur `*` confuse karna:** `file?.txt` sirf file1.txt match karega, file10.txt nahi
- ❌ **Zero characters expect karna:** `?` exactly 1 character chahiye, zero nahi
- ❌ **Path separators:** `?` forward slash (/) match nahi karta

### 10. **Best Practices / Pro Tips**
- 💡 **Counting characters:** Jitne `?` utne characters - `???` = exactly 3
- 💡 **Combine with `*`:** `file?_*.txt` - file + 1 char + underscore + anything + .txt
- 💡 **Date patterns:** `????-??-??` standard date format ke liye
- 💡 **Testing:** `echo file?.txt` se pehle dekho kya match ho raha hai

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek system administrator hain aur daily log files ko process karna hai jo specific format mein hain:

```bash
#!/bin/bash
# Daily log processor

LOG_DIR="/var/log/app"
TODAY=$(date +%Y-%m-%d)

echo "Processing today's logs: $TODAY"

# Aaj ki saari hourly logs (format: app_2024-01-15_HH.log)
for log in "$LOG_DIR"/app_${TODAY}_??.log; do
    if [ -f "$log" ]; then
        echo "Processing: $(basename "$log")"
        
        # Errors count karo
        error_count=$(grep -c "ERROR" "$log")
        echo "  Errors found: $error_count"
        
        # Agar errors hain toh alert
        if [ "$error_count" -gt 0 ]; then
            echo "  ⚠️  Alert: Errors detected!"
            grep "ERROR" "$log" >> /tmp/error_summary.txt
        fi
    fi
done

echo "Log processing complete!"
```

Yeh script automatically aaj ki saari hourly logs ko process karega.

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `?` exactly ek character match karta hai
- ✅ `??` exactly do characters, `???` exactly teen
- ✅ Fixed-length patterns ke liye perfect
- ✅ `*` se zyada precise control
- ✅ Date formats aur codes ke liye ideal

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `?` aur `*` mein main fark kya hai?**
A: `?` exactly 1 character match karta hai. `*` zero se unlimited characters match karta hai.

**Q2: Kya `?` hidden files match karta hai?**
A: Nahi, agar file `.` se shuru hoti hai toh explicitly `.?` use karna padega.

**Q3: Kya main `?` ko escape kar sakta hoon?**
A: Haan, `\?` ya `'?'` use karo agar literal question mark chahiye.

### 14. **Practice ke liye Task**

```bash
# 1. Test files banao
touch file1.txt file2.txt file3.txt
touch file10.txt file11.txt
touch log_2024-01-15.txt log_2024-01-16.txt

# 2. Single digit files
ls file?.txt

# 3. Two digit files
ls file??.txt

# 4. Date pattern files
ls log_????-??-??.txt

# 5. Difference dekho
ls file*.txt    # Saari files
ls file?.txt    # Sirf single digit

# 6. Cleanup
rm file*.txt log*.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- ❓ `?` exactly ek character ke liye placeholder
- 🎯 Fixed-length patterns ke liye perfect tool
- 📅 Date formats aur codes match karne ke liye ideal
- 🔢 Numbered sequences precisely handle karta hai
- ⚖️ `*` se zyada control, kam flexibility

> **💡 Ye Zaroor Yaad Rakhein:**
> Question mark (`?`) precision ka tool hai! Jab exact length pata ho, tab `?` use karo. Jab variable length ho, tab `*` use karo!

---

## **Topic 3: Bracket Wildcards (`[ ]`, `[abc]`, `[!abc]`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Bracket Wildcards** - Specific characters ya character ranges ko match karne ka surgical tool.

### 2. **Ye Kya Hai? (What is it?)**
Bracket wildcards (`[ ]`) aapko exactly specify karne dete hain ki kaunse characters match hone chahiye. Yeh `?` se bhi zyada precise hai kyunki aap exact characters choose kar sakte hain.

**Analogy:** Socho ki aap ek restaurant mein hain. `*` ka matlab "kuch bhi khilao", `?` ka matlab "koi ek dish do", lekin `[abc]` ka matlab "sirf A, B, ya C dish do - aur kuch nahi!"

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Character-level control** - Exact characters specify karna
- ✅ **Range matching** - [0-9], [a-z] jaise ranges
- ✅ **Exclusion** - [!abc] specific characters ko exclude karna
- ✅ **Complex patterns** - Bahut specific file matching

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Jab specific characters wali files chahiye
- Jab ranges match karne hon (numbers, letters)
- Jab kuch characters ko exclude karna ho
- Case-sensitive matching chahiye

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Complex patterns nahi bana paoge
- Unwanted files match ho jayengi
- Precise filtering nahi kar paoge
- Advanced automation limited rahega

### 6. **Syntax aur Common Options**

```bash
# Specific characters
[abc]           # a, b, ya c
[123]           # 1, 2, ya 3

# Ranges
[a-z]           # a se z tak koi bhi lowercase letter
[A-Z]           # A se Z tak koi bhi uppercase letter
[0-9]           # 0 se 9 tak koi bhi digit

# Negation (NOT)
[!abc]          # a, b, c KE ALAWA koi bhi character
[!0-9]          # Digit KE ALAWA koi bhi character

# Combined
[a-zA-Z]        # Koi bhi letter (upper ya lower)
[0-9a-f]        # Hexadecimal digits
```

**Important Patterns:**
- `file[123].txt` - file1.txt, file2.txt, file3.txt
- `file[0-9].txt` - file0.txt se file9.txt tak
- `file[!0-9].txt` - fileA.txt, fileB.txt (digits nahi)
- `[A-Z]*.txt` - Capital letter se shuru hone wali files

### 7. **Example 1 (Basic)**

```bash
# Specific numbers
$ ls file[123].txt
file1.txt  file2.txt  file3.txt

# Range of numbers
$ ls file[0-9].txt
file0.txt  file1.txt  file2.txt  ...  file9.txt

# Lowercase letters
$ ls file[a-c].txt
filea.txt  fileb.txt  filec.txt

# NOT digits
$ ls file[!0-9].txt
filea.txt  fileb.txt  fileX.txt

# Capital letters se shuru
$ ls [A-Z]*.txt
Apple.txt  Banana.txt  Zebra.txt
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# Grade-wise student files organize karna

STUDENT_DIR="/data/students"
GRADE_DIR="/data/grades"

mkdir -p "$GRADE_DIR"/{A,B,C,D,F}

echo "Organizing student files by grade..."

# Grade A students (90-100)
for file in "$STUDENT_DIR"/student_[9][0-9]_*.txt; do
    [ -f "$file" ] && mv -v "$file" "$GRADE_DIR/A/"
done

# Grade B students (80-89)
for file in "$STUDENT_DIR"/student_[8][0-9]_*.txt; do
    [ -f "$file" ] && mv -v "$file" "$GRADE_DIR/B/"
done

# Grade C students (70-79)
for file in "$STUDENT_DIR"/student_[7][0-9]_*.txt; do
    [ -f "$file" ] && mv -v "$file" "$GRADE_DIR/C/"
done

# Grade D students (60-69)
for file in "$STUDENT_DIR"/student_[6][0-9]_*.txt; do
    [ -f "$file" ] && mv -v "$file" "$GRADE_DIR/D/"
done

# Grade F students (below 60)
for file in "$STUDENT_DIR"/student_[0-5][0-9]_*.txt; do
    [ -f "$file" ] && mv -v "$file" "$GRADE_DIR/F/"
done

echo "Organization complete!"

# Summary
for grade in A B C D F; do
    count=$(ls -1 "$GRADE_DIR/$grade" 2>/dev/null | wc -l)
    echo "Grade $grade: $count students"
done
```

**Output:**
```
Organizing student files by grade...
'student_95_john.txt' -> 'grades/A/student_95_john.txt'
'student_87_sarah.txt' -> 'grades/B/student_87_sarah.txt'
Organization complete!
Grade A: 5 students
Grade B: 8 students
Grade C: 12 students
Grade D: 6 students
Grade F: 3 students
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Spaces dena:** `[a, b, c]` galat - `[abc]` sahi
- ❌ **Multiple characters expect karna:** `[abc]` sirf EK character match karta hai
- ❌ **Range order galat:** `[z-a]` kaam nahi karega, `[a-z]` sahi hai

### 10. **Best Practices / Pro Tips**
- 💡 **Ranges combine karo:** `[a-zA-Z0-9]` alphanumeric characters
- 💡 **Negation powerful hai:** `[!0-9]` non-digits ke liye
- 💡 **Case sensitivity:** `[a-z]` aur `[A-Z]` alag hain
- 💡 **Testing:** `echo file[0-9].txt` se pehle test karo

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek data analyst hain aur CSV files ko process karna hai jo specific naming convention follow karti hain:

```bash
#!/bin/bash
# CSV data processor - sirf valid format wali files

DATA_DIR="/data/csv"
PROCESSED_DIR="/data/processed"
ERROR_DIR="/data/errors"

mkdir -p "$PROCESSED_DIR" "$ERROR_DIR"

echo "Processing CSV files..."

# Valid format: data_[A-Z][0-9][0-9][0-9].csv
# Example: data_A001.csv, data_Z999.csv

for file in "$DATA_DIR"/data_[A-Z][0-9][0-9][0-9].csv; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        echo "Processing: $filename"
        
        # Validate CSV structure
        if head -1 "$file" | grep -q "id,name,value"; then
            # Process file
            awk -F',' '{sum+=$3} END {print "Total:", sum}' "$file" > "$PROCESSED_DIR/${filename%.csv}_summary.txt"
            echo "  ✓ Processed successfully"
        else
            echo "  ✗ Invalid CSV structure"
            mv "$file" "$ERROR_DIR/"
        fi
    fi
done

echo "Processing complete!"
echo "Processed: $(ls -1 "$PROCESSED_DIR" | wc -l) files"
echo "Errors: $(ls -1 "$ERROR_DIR" 2>/dev/null | wc -l) files"
```

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `[abc]` specific characters match karta hai
- ✅ `[a-z]` ranges define karta hai
- ✅ `[!abc]` negation - specified characters KE ALAWA
- ✅ `[0-9]` digits, `[a-zA-Z]` letters
- ✅ Sirf EK character match hota hai per bracket

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `[abc]` aur `{a,b,c}` mein kya fark hai?**
A: `[abc]` ek character match karta hai (a YA b YA c). `{a,b,c}` brace expansion hai jo teen alag strings banata hai.

**Q2: Kya main multiple brackets use kar sakta hoon?**
A: Haan! `file[0-9][0-9].txt` do digits match karega: file00.txt se file99.txt tak.

**Q3: `[!abc]` kaise kaam karta hai?**
A: Yeh negation hai - a, b, c KE ALAWA koi bhi ek character match karega.

### 14. **Practice ke liye Task**

```bash
# 1. Test files banao
touch file1.txt file2.txt file3.txt file9.txt
touch filea.txt fileb.txt fileX.txt
touch File1.txt File2.txt

# 2. Specific numbers
ls file[123].txt

# 3. Range of numbers
ls file[0-9].txt

# 4. Letters only
ls file[a-z].txt

# 5. NOT numbers
ls file[!0-9].txt

# 6. Capital letters
ls [A-Z]*.txt

# 7. Cleanup
rm file*.txt File*.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🎯 Brackets character-level precision dete hain
- 📊 Ranges (`[0-9]`, `[a-z]`) bahut powerful hain
- 🚫 Negation (`[!abc]`) exclusion ke liye
- 🔤 Case-sensitive matching possible hai
- 💡 Complex patterns banane ka foundation

> **💡 Ye Zaroor Yaad Rakhein:**
> Bracket wildcards surgical precision dete hain! `[0-9]` digits ke liye, `[a-z]` lowercase letters ke liye, aur `[!...]` exclusion ke liye yaad rakho!

---

## **Topic 4: Character Classes (`[[:alpha:]]`, `[[:digit:]]`, `[[:lower:]]`, `[[:upper:]]`)**

### 1. **Topic ka Naam / Ek Line Mein Summary** 🚀
**Character Classes** - Predefined character sets jo portable aur reliable hain.

### 2. **Ye Kya Hai? (What is it?)**
Character classes POSIX standard ke predefined sets hain jo specific types of characters ko represent karte hain. Yeh `[a-z]` se zyada reliable hain kyunki yeh locale-aware hain aur har system par same kaam karte hain.

**Analogy:** Socho ki `[a-z]` ek handwritten list hai jo galat ho sakti hai, lekin `[[:lower:]]` ek printed, certified list hai jo hamesha sahi hogi - chahe koi bhi language ya system ho.

### 3. **Kyun Zaroori Hai? (Why is it important?)**
- ✅ **Portability** - Har Unix/Linux system par same kaam karte hain
- ✅ **Locale-aware** - Different languages support karte hain
- ✅ **Reliability** - `[a-z]` se zyada bharosemand
- ✅ **Readability** - Code zyada clear aur self-documenting

### 4. **Ise Kab Use Karna Chahiye? (When to use it?)**
- Production scripts mein (portability ke liye)
- International applications mein
- Jab locale-specific characters chahiye
- Professional code likhte waqt

### 5. **Agar Ye Pata Nahi Hoga Toh Kya Hoga? (Risk?)** 😟
- Scripts different systems par fail ho sakti hain
- Locale issues aa sakte hain
- International characters miss ho sakte hain
- Code less portable hoga

### 6. **Syntax aur Common Options**

```bash
# Alphabetic characters
[[:alpha:]]     # Saare letters (a-z, A-Z)

# Digits
[[:digit:]]     # 0-9

# Alphanumeric
[[:alnum:]]     # Letters + digits

# Lowercase
[[:lower:]]     # a-z (locale-aware)

# Uppercase
[[:upper:]]     # A-Z (locale-aware)

# Whitespace
[[:space:]]     # Space, tab, newline

# Punctuation
[[:punct:]]     # Punctuation characters

# Printable
[[:print:]]     # Printable characters

# Hexadecimal
[[:xdigit:]]    # 0-9, a-f, A-F
```

**Common Character Classes:**
- `[[:alpha:]]` - Letters
- `[[:digit:]]` - Numbers
- `[[:alnum:]]` - Letters + Numbers
- `[[:lower:]]` - Lowercase letters
- `[[:upper:]]` - Uppercase letters
- `[[:space:]]` - Whitespace

### 7. **Example 1 (Basic)**

```bash
# Alphabetic characters se shuru hone wali files
$ ls [[:alpha:]]*.txt
apple.txt  Banana.txt  zebra.txt

# Digits se shuru hone wali files
$ ls [[:digit:]]*.txt
1file.txt  2file.txt  9file.txt

# Lowercase se shuru hone wali files
$ ls [[:lower:]]*.txt
apple.txt  banana.txt  zebra.txt

# Uppercase se shuru hone wali files
$ ls [[:upper:]]*.txt
Apple.txt  Banana.txt  Zebra.txt
```

### 8. **Example 2 (Advanced/Script)**

```bash
#!/bin/bash
# File validator - naming convention check karna

UPLOAD_DIR="/uploads"
VALID_DIR="/uploads/valid"
INVALID_DIR="/uploads/invalid"

mkdir -p "$VALID_DIR" "$INVALID_DIR"

echo "Validating uploaded files..."

# Valid format: lowercase letters, digits, underscore, hyphen only
# Example: my_file-123.txt

for file in "$UPLOAD_DIR"/*; do
    [ -f "$file" ] || continue
    
    filename=$(basename "$file")
    name="${filename%.*}"
    
    # Check if name contains only valid characters
    if [[ "$name" =~ ^[[:lower:][:digit:]_-]+$ ]]; then
        echo "✓ Valid: $filename"
        mv "$file" "$VALID_DIR/"
    else
        echo "✗ Invalid: $filename (contains invalid characters)"
        mv "$file" "$INVALID_DIR/"
    fi
done

echo ""
echo "Validation complete!"
echo "Valid files: $(ls -1 "$VALID_DIR" 2>/dev/null | wc -l)"
echo "Invalid files: $(ls -1 "$INVALID_DIR" 2>/dev/null | wc -l)"
```

**Output:**
```
Validating uploaded files...
✓ Valid: my_document-2024.pdf
✓ Valid: report_final.txt
✗ Invalid: My Document.pdf (contains invalid characters)
✗ Invalid: file@123.txt (contains invalid characters)

Validation complete!
Valid files: 2
Invalid files: 2
```

### 9. **Beginners ki Aam Galtiyan (Common Mistakes)**
- ❌ **Double brackets bhoolna:** `[:alpha:]` galat - `[[:alpha:]]` sahi
- ❌ **`[a-z]` aur `[[:lower:]]` same samajhna:** Different locales mein alag ho sakte hain
- ❌ **Quotes mein use karna:** Globbing ke liye quotes nahi chahiye

### 10. **Best Practices / Pro Tips**
- 💡 **Production mein prefer karo:** `[[:lower:]]` > `[a-z]`
- 💡 **Combine karo:** `[[:alnum:]_-]` alphanumeric + underscore + hyphen
- 💡 **Regex mein bhi kaam karte hain:** `grep`, `sed`, `awk` mein use karo
- 💡 **Self-documenting:** Code zyada readable hota hai

### 11. **Asli Duniya ka Scenario (Real-World Scenario)**

Aap ek security analyst hain aur log files mein suspicious usernames dhoondhni hain:

```bash
#!/bin/bash
# Suspicious username detector

LOG_FILE="/var/log/auth.log"
REPORT_FILE="/tmp/suspicious_users.txt"

echo "Analyzing authentication logs..."
echo "Suspicious Usernames Report" > "$REPORT_FILE"
echo "Generated: $(date)" >> "$REPORT_FILE"
echo "================================" >> "$REPORT_FILE"

# Valid usernames: lowercase letters, digits, underscore, hyphen
# Length: 3-16 characters

grep "Failed password" "$LOG_FILE" | \
    grep -oP 'user \K[^ ]+' | \
    sort -u | \
    while read username; do
        # Check if username is valid format
        if ! [[ "$username" =~ ^[[:lower:][:digit:]_-]{3,16}$ ]]; then
            echo "⚠️  Suspicious: $username" | tee -a "$REPORT_FILE"
            
            # Count attempts
            attempts=$(grep -c "user $username" "$LOG_FILE")
            echo "   Attempts: $attempts" | tee -a "$REPORT_FILE"
        fi
    done

echo ""
echo "Report saved to: $REPORT_FILE"
```

Yeh script automatically invalid username patterns detect karega jo attack attempts ho sakte hain.

### 12. **Checklist / Chota Recap (TL;DR)**
- ✅ `[[:alpha:]]` - Saare letters
- ✅ `[[:digit:]]` - Saare digits
- ✅ `[[:lower:]]` - Lowercase (locale-aware)
- ✅ `[[:upper:]]` - Uppercase (locale-aware)
- ✅ Production scripts mein prefer karo

### 13. **Aksar Puche Jaane Wale Sawaal (FAQs)**

**Q1: `[a-z]` aur `[[:lower:]]` mein kya fark hai?**
A: `[[:lower:]]` locale-aware hai aur international characters bhi include karta hai. `[a-z]` sirf ASCII letters.

**Q2: Kya character classes regex mein kaam karte hain?**
A: Haan! `grep`, `sed`, `awk` sabmein use kar sakte hain.

**Q3: Kya main multiple classes combine kar sakta hoon?**
A: Haan! `[[:alpha:][:digit:]_]` letters + digits + underscore.

### 14. **Practice ke liye Task**

```bash
# 1. Test files banao
touch apple.txt Banana.txt 123.txt
touch file_test.txt File-Test.txt
touch "My File.txt"

# 2. Lowercase se shuru
ls [[:lower:]]*.txt

# 3. Uppercase se shuru
ls [[:upper:]]*.txt

# 4. Digit se shuru
ls [[:digit:]]*.txt

# 5. Alphanumeric se shuru
ls [[:alnum:]]*.txt

# 6. Test validation
for f in *.txt; do
    if [[ "$f" =~ ^[[:lower:][:digit:]_-]+\.txt$ ]]; then
        echo "Valid: $f"
    else
        echo "Invalid: $f"
    fi
done

# 7. Cleanup
rm *.txt
```

### 15. **Aakhri Choti Summary (5 lines)**
- 🌍 Character classes portable aur locale-aware hain
- 📚 Predefined sets: alpha, digit, lower, upper, space
- 🔒 Production code mein `[[:lower:]]` > `[a-z]`
- 🎯 Regex aur globbing dono mein kaam karte hain
- 💼 Professional scripting ka standard

> **💡 Ye Zaroor Yaad Rakhein:**
> Character classes professional scripting ka hallmark hain! Production scripts mein hamesha `[[:lower:]]`, `[[:digit:]]` jaise classes use karo - yeh portable, reliable, aur locale-aware hain!

---

# **🎉 Module 3 Complete! 🎉**

Congratulations! Aapne **Module 3: Pattern Matching (Wildcards)** successfully complete kar liya hai!

## **Aapne Kya Seekha:**
✅ Star Wildcard (`*`) - Unlimited characters match karna
✅ Question Mark (`?`) - Exactly ek character match karna
✅ Bracket Wildcards (`[abc]`, `[0-9]`, `[!abc]`) - Specific characters aur ranges
✅ Character Classes (`[[:alpha:]]`, `[[:digit:]]`) - Professional, portable patterns

## **Key Takeaways:**
- `*` - Sabse powerful, sabse flexible (0 to unlimited characters)
- `?` - Precision tool (exactly 1 character)
- `[...]` - Surgical control (specific characters/ranges)
- `[[:...]]` - Professional standard (portable, locale-aware)

## **Real-World Applications:**
- Bulk file operations (`*.txt`, `*.log`)
- Date-based file matching (`????-??-??`)
- Grade/category organization (`[A-F]`, `[0-9]`)
- Validation scripts (naming conventions)

## **Next Steps:**
Ab aap ready hain **Module 4: I/O Redirection & Piping** ke liye!

---

**📝 Practice Reminder:**
Wildcards ko master karne ka ek hi tarika hai - practice! Har din different patterns try karo. Pehle `ls` se test karo, phir actual commands use karo.

**⚠️ Safety Tip:**
Wildcards powerful hain lekin dangerous bhi! Hamesha:
1. Pehle `ls` se verify karo
2. Important files ka backup lo
3. `-i` (interactive) option use karo
4. `pwd` se location confirm karo

---

**🎯 Challenge:**
Ek script banao jo:
1. Saari `.txt` files ko dhoodhe
2. Sirf lowercase letters se shuru hone wali files select kare
3. Unhe date-wise folders mein organize kare
4. Summary report generate kare

Yeh challenge Module 3 ke saare concepts use karega!

---
