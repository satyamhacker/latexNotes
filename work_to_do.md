# Section 26: Unions




# 🧠 QUICK REVISION CHEAT SHEET: C Unions & Embedded Memory

### 1. The `union` Keyword (Basic Rule)

* **Concept:** Union ek parking space hai jahan saare variables **ek hi memory address** share karte hain.
* **Size Rule:** Total size saare variables ko add karke nahi, balki **Sabse Bade (Biggest) Member** ke size ke barabar hota hai.
* **Kab Use Karein:** Jab 2 ya usse zyada chizon ki zaroorat ho, par *ek time pe sirf kisi ek ki* (e.g., ya toh short address aayega ya long, dono nahi). Isse RAM bachti hai.

```c
union NetworkAddr {
    uint16_t shortAddr; // 2 bytes
    uint32_t longAddr;  // 4 bytes -> Union ka total size = 4 bytes!
};

```

### 2. Mutually Exclusive Access (Ek Miyan Me Ek Talwar)

* **Concept:** Kyunki address same hai, tum ek waqt par sirf ek hi variable use kar sakte ho.
* **Golden Rule:** Jis variable mein last time *Write* kiya hai, sirf usi variable se *Read* karna hai. Galti se dusra read kiya toh Garbage value aayegi.

### 3. Data Overwriting & Endianness (Hardware Trap)

* **Overwriting:** Naya data dalte hi purana permanently delete (overwrite) ho jata hai.
* **Endianness:**
* **Little-Endian (PC/Intel):** Data ko pichhe se (Least Significant Byte pehle) store karta hai.
* **Big-Endian (Network/Internet):** Data ko aage se store karta hai.


* **The Bug:** Agar tum Little-Endian PC par 4-byte `longAddr` me `0xEEEECCCC` daloge, aur 2-byte `shortAddr` read karoge, toh output `0xCCCC` (pichla hissa) aayega.

### 4. The "Cheat Code": Nested Structs in Union

* **Concept:** Union roopi bade dabbe ke andar ek `struct` ki "Divider Tray" laga dena.
* **Why:** Embedded me 32-bit sensor data ek sath aata hai. Hum bina bitwise math (`>>`, `&`) ke direct specific tukde nikal sakte hain.
* **How:** Ek solid 32-bit variable dalo, aur theek uske niche ek anonymous struct dalo memory overlap karne ke liye.

```c
union Packet {
    uint32_t full_data;     // Yahan hardware ne poora data 1 shot me daala
    struct {
        uint16_t part1;     // Pehle 2 bytes
        uint16_t part2;     // Aakhiri 2 bytes
    } parts;                // CPU auto-filter karke data yahan dikha dega
};

```

### 5. Bit-Fields (Memory in 0s and 1s)

* **Concept:** Struct data ko "Bytes" me todta hai, par **Bit-fields** data ko direct "Bits" (0s and 1s) me todte hain.
* **Syntax Rule:** Colon `:` laga kar bits define karte hain. Sabka total outer union ke size ko cross nahi karna chahiye.

```c
union SmartPacket {
    uint32_t full_data; 
    struct {
        uint32_t crc     : 2;  // Sirf 2 Bits lega
        uint32_t status  : 1;  // Sirf 1 Bit (0 ya 1)
        uint32_t payload : 29; // Bacha hua 29 Bits
    } bits;
}; // Usage: packet.bits.crc 

```

### 6. The Safety Lock: `ntohl()` Macro

* **The Problem:** Internet hamesha **Big-Endian** me data bhejta hai, par PC **Little-Endian** hota hai. Direct data union me dala toh saare bits ulte extract honge.
* **The Fix:** Hamesha `ntohl()` (Network To Host Long) use karo. Yeh data ko PC ke hisaab se seedha kar deta hai.

```c
// NEVER DO THIS:
// packet.full_data = raw_network_data; 

// ALWAYS DO THIS:
packet.full_data = ntohl(raw_network_data); 
// Ab aaram se bit-fields read karo!



==================================================================================
