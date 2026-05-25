# 📝 SECTION 29: ARRAYS — MASTER NOTES

## 🎯 1. Introduction & Memory Structure

* **Technical Definition:** Array ek linear data structure hai jo hamesha **same data type** (homogeneous data) ke multiple items ko **contiguous memory locations** (lagataar addresses) mein store karta hai.
* **Base Pointer Rule:** Array ka jo variable naam hota hai, woh memory mein hamesha **very first data item (0th index)** ke address ko point karta hai. Ise **Base Address** kehte hain.
* *Proof:* `printf("%p", array_name);` aur `printf("%p", &array_name[0]);` ka output exactly same aata hai.


* **Cache Friendliness:** Contiguous memory hone ki wajah se CPU jab ek element read karta hai, toh aage ke elements ko bhi ek saath cache memory mein utha lata hai. Isiliye array processing fast aur highly scalable hoti hai.

> **NOTE:** C arrays ka size hamesha **fixed** hota hai. Ek baar declare hone ke baad iska size runtime par dynamically badhaya nahi ja sakta.

### 🧠 Yaad Rakhne Wali Baatein:

* Array size define karne ke liye hamesha **Square Brackets `[]**` use hote hain, parentheses `()` nahi.
* Pointers ya base address print karne ke liye `printf` mein format specifier **`%p`** ka use hota hai.
* **Size Formula:** Total element count nikalne ka standard trick:

$$Total\ Elements = \frac{sizeof(array\_name)}{sizeof(array\_name[0])}$$



---

## 🎯 2. Array Initialization & VLA (Variable Length Arrays)

* **Garbage Value Risk:** C mein agar array ko bina initialize kiye direct create kiya jaye (`int arr[5];`), toh memory mein bacha hua purana kachra data (garbage value) usme reh jata hai, jo security vulnerabilities aur bugs ka bada reason banta hai.
* **Partial Initialization Rule:** Agar aap array ko initialize karte waqt size se kam values dete hain, toh C compiler bache hue saare slots ko **automatically zero (0)** se fill kar deta hai.
* *Shorthand:* `uint8_t buffer[256] = {0};` likhne se pura array zero se saaf ho jata hai.


* **Implicit Sizing:** Agar declaration ke waqt brackets `[]` khali chhod dein aur aage curly braces `{}` mein values de dein, toh compiler khud elements gin kar array ka size fix kar deta hai. (e.g., `int arr[] = {1, 2, 3};` $\rightarrow$ size automatically 3 lock ho jayega).
* **Variable Length Array (VLA):** Jab array ka size compile-time constant na hokar, runtime par kisi variable se tay ho, toh use VLA kehte hain (introduced in **C99 standard**).
* *Example:* `int len = 10; uint8_t vlaData[len];`



> **NOTE:** Embedded aur safety-critical systems (jaise car ECU) mein VLAs ko **strictly avoid** kiya jata hai. Agar runtime par variable ki value bohot badi ho jaye, toh direct **Stack Overflow** ho jata hai aur pura system crash ho jata hai.

### 🧠 Yaad Rakhne Wali Baatein:

* `int arr[];` bina values ke likhna completely illegal hai. Compiler `array size missing` error dega.
* Agar purana compiler use ho raha ho, toh VLA support ke liye GCC mein **`--std=c99`** compiler flag lagana padta hai, nahi toh `ISO C90 forbids variable length array` ki pedantic warning aayegi.

---

## 🎯 3. Array Read/Write & Indexing Logic

* **Syntactic Sugar (Shortcut):** Array index (`arr[i]`) asal mein sirf ek shorthand method hai, jo internally compiler dwara **Pointer Manipulation** mein convert ho jata hai.
* `arr[1] = 0x9;` $\rightarrow$ internally becomes $\rightarrow$ `*(arr + 1) = 0x9;`


* **Zero-Based Indexing Reason:** Index ka matlab counting nahi, balki **offset** (base address se doori) hota hai. Pehla element base address par hi hota hai, isiliye uska distance/offset `0` hota hai.
* **Dereferencing:** Address par jaakar uske andar ki actual value ko access karne (read/write) ki process ko dereferencing kehte hain (using `*` or `[]`).

> **NOTE:** C language mein `3[arr]` likhna completely legal hai aur bina error ke compile hoga, kyunki addition commutative hota hai: `*(arr + 3)` is equal to `*(3 + arr)`. Par code readability ke liye yeh ek bad anti-pattern hai.

### 🧠 Yaad Rakhne Wali Baatein:

* **The `<=` Loop Trap:** Agar array size 10 hai, toh last valid index 9 hoga (0 se 9). Loop condition hamesha `i < 10` (strictly less than) honi chahiye. Agar `i <= 10` chalaya, toh **Buffer Overflow** ho jayega.
* **Segmentation Fault:** Agar program kisi aise out-of-bounds index ko access karne ki koshish karega jo OS ke allocated area se bahar hai, toh runtime par `Segmentation fault (core dumped)` error aayega.
* Hexadecimal values ko output mein print karne ke liye **`%x`** format specifier lagta hai.

---

## 🎯 4. Passing Arrays to Functions

* **Pass by Reference Only:** C mein arrays kabhi bhi value se (copy hokar) function mein nahi jaate. Performance optimize rakhne ke liye hamesha array ka **Base Address (Reference)** pass hota hai.
* **Pointer Decay:** Jab array kisi function mein pass hota hai, toh woh simple pointer mein badal jata hai. Is wajah se function ke andar `sizeof` operator kaam nahi karta (woh array size ke bajaye sirf pointer ka size, e.g., 8 bytes dega).
* **Explicit Size Parameter:** Pointer decay ki wajah se function ko kabhi nahi pata chalta ki array kitna bada hai. Isiliye caller function se hamesha array ka size (`nItems`) ek alag parameter ke roop mein pass karna mandatory hai.
* **Prototype Notation:** Function prototype mein `void func(int arr[])` aur `void func(int *arr)` dono compiler ke liye 100% same hain. Both accept pointers.

> **NOTE:** Agar receiving function read-only hai (jaise logging ya display), toh receiving parameter mein **`const`** qualifier lagana mandatory industry standard hai (e.g., `const uint8_t *pArray`). Yeh galti se hone wale data corruption ko compiler level par hi block kar deta hai.

### 🧠 Yaad Rakhne Wali Baatein:

* Function ke andar kabhi bhi `sizeof(pArray) / sizeof(pArray[0])` se length calculate na karein.
* **Offset Passing:** Agar array ke kisi beech ke element se processing shuru karwani ho, toh call karte waqt ampersand `&` se address pass karein: `func(&someData[2], 3);` (or `someData + 2`).
* `const uint8_t *ptr` ka matlab hai data constant hai (edit nahi hoga). `uint8_t * const ptr` ka matlab hai pointer ka address constant hai (address change nahi hoga).

---

## 🎯 5. Array Swap Exercise Implementation

* **Bucket Strategy (Temp Variable):** Do array elements ko aapas mein bina data loss ke swap karne ke liye 3-step logic mandatory hai:
1. `temp = array1[i];` (Backup data)
2. `array1[i] = array2[i];` (Override slot 1)
3. `array2[i] = temp;` (Fill slot 2 from backup)


* **Uneven Length Guard:** Agar do alag-alag size ke arrays ko swap karna hai, toh loop ko hamesha dono lengths mein se jo **minimum (lowest) size** hai, wahan tak hi chalana chahiye. Iske liye **Ternary/Conditional Operator (`? :`)** best practice hai.
* `uint32_t length = (nItem1 < nItem2) ? nItem1 : nItem2;`



> **NOTE:** Massive datasets (millions of rows) mein element-by-element swap karna CPU par heavy hota hai. Production mein senior developers actual values ke bajaye sirf un arrays ke **Base Pointers ka address** aaspaas mein swap kar dete hain (**Pointer Swapping**), jo $O(1)$ time mein instantly ho jata hai.

### 🧠 Yaad Rakhne Wali Baatein:

* **Scanf Pointer Requirement:** `scanf` ek input buffer function hai. Isme variable ka original data update karne ke liye hamesha pointer pass karna padta hai, isiliye loop mein **`&array[i]`** (ampersand address-of operator) lagana compulsory hai.
* **Width Specifier Benefit:** `printf` karte waqt `%4d` ya `%3d` lagane se output console par numbers ke beech perfect equal space (column alignment gap) ban jata hai, jo grid formatting ke liye best hai.
* 64-bit systems par agar architecture size match check warning aaye format specifier mein, toh `%d` ki jagah **`%ld`** (Long Integer) ka use karein.

==================================================================================
