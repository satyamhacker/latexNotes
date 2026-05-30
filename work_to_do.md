## Module 6 and 7:


Ekdum clear! Maafi chahunga agar pichle order mein confusion hui ho. Main exactly tumhare diye hue **STRICT DEPENDENCY MAP** ke order (Concept 1 to 12) mein saare master notes ek sath de raha hu.

Isko direct copy-paste karke apne notes mein save kar lo. Isme sirf wo "To-The-Point" code aur rules hain jo real-world development mein 95% time use hote hain.

---

### 💡 BONUS CONCEPT: What is `children` in React?

`children` sirf **UI (User Interface)** ke liye hota hai, logic ke liye nahi. Tag ke beech mein jo bhi visual cheez aati hai, wo `children` hai.

* **Type:** `ReactNode`
* **Valid:** HTML tags, Strings, Numbers, Arrays, Components, null, booleans.
* **Invalid:** `useState`, functions, raw logic.

```tsx
const Wrapper = ({ children }: { children: ReactNode }) => (
  <div className="box">{children}</div> 
);

```

---

## 📘 MODULE 6: Typing Hooks & Component State

### Concept 1: `useState` Typing

* **Inference (Let TS Guess):** Primitive values (string, number, boolean) ke liye generic lagana redundant hai. Use `useState(false)`.
* **Explicit Generic:** Complex objects, arrays, ya API data ke liye jinki initial value `null` hoti hai.
* **Rule:** Hamesha data absence ke liye `null` use karo, `undefined` nahi.

```tsx
type User = { id: string; name: string };
const [user, setUser] = useState<User | null>(null); 
// Usage: <h1>{user?.name}</h1> (Optional chaining is mandatory)

```

### Concept 2: `useRef` Typing

* **DOM Reference (Laser Pointer):** Tag par lagane ke liye. Generic mein exact HTML Element Type do aur initial value strictly `null` rakho. `.current` read-only hota hai.
```tsx
const inputRef = useRef<HTMLInputElement>(null);
// Usage: inputRef.current?.focus();

```


* **Mutable Value (Background Data):** Data store karne ke liye jisse UI re-render na ho (jaise timer ID). Non-null initial value do.
```tsx
const timerId = useRef<number>(0);
// Usage: timerId.current += 1;

```



### Concept 3: Custom Hooks Typing

* **Tuple Return (1-2 items):** Array return karo aur `as const` lagao. Isse "Type Widening" rukti hai aur TS index positions/length ko lock kar deta hai. Parent apne hisaab se variable rename kar sakta hai.
```tsx
return [isOpen, toggle] as const; 
// Usage: const [isModalOpen, toggleModal] = useToggle();

```


* **Object Return (3+ items):** Object return karo. Keys inherently strict hoti hain, toh `as const` ki zaroorat nahi.
```tsx
return { data, isLoading, error };

```



### Concept 4: `useReducer` Typing

* **Discriminated Unions:** Action types hamesha exact literal strings hone chahiye, generic `string` nahi. NEVER use `payload?: any`.
* **Rule:** Actions ko pipe `|` se connect karo taaki `switch` block mein TS automatically correct payload shape guess (narrow down) kar le.

```tsx
type Action = 
  | { type: 'ADD_ITEM'; payload: { id: string } } 
  | { type: 'CLEAR_CART' }; // Strict: No payload allowed

```

### Concept 5: `useContext` Typing

* **Rule:** `createContext` ko hamesha `undefined` se initialize karo. Fake empty object `({} as Type)` ka use paap hai.
* **The Guard Hook:** Hamesha ek custom hook banao jo check kare ki context `undefined` toh nahi hai. Agar hai, toh error throw kare (meaning Provider wrap nahi kiya gaya).

```tsx
const AuthContext = createContext<AuthType | undefined>(undefined);

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) throw new Error("Must be inside Provider!");
  return context;
};

```

### Concept 6: `forwardRef` Typing

* **Rule:** Functional React components default `ref` prop accept nahi karte. Unhe `forwardRef` se wrap karna padta hai.
* **Syntax Trap:** TypeScript mein generic order ulta hota hai: `<RefType, PropsType>`.

```tsx
type Props = { label: string };

// Note order: HTMLInputElement first, Props second
export const CustomInput = forwardRef<HTMLInputElement, Props>((props, ref) => (
  <input ref={ref} placeholder={props.label} />
));

```

---

## 📙 MODULE 7: Web-Specific Types (React Web & Angular)

### Concept 7: DOM Events Typing

* **Rule:** Inline functions khud type infer kar lete hain. Par agar event handler file mein alag se banaya hai, toh type dena mandatory hai.
* **Forms/Inputs:** `e: React.ChangeEvent<HTMLInputElement>` (To read `e.target.value`)
* **Form Submit:** `e: React.FormEvent<HTMLFormElement>` (To use `e.preventDefault()`)
* **Clicks:** `e: React.MouseEvent<HTMLButtonElement>`
* *Pro-Tip:* Tag ka id/data read karne ke liye `e.currentTarget` use karo, `e.target` se safe hota hai.

### Concept 8: Inline Styles (`React.CSSProperties`)

* **Rule:** JSX ke bahar ya props mein style object banate waqt `React.CSSProperties` type use karo.
* **Syntax:** Hamesha `camelCase` (e.g., `backgroundColor`). Number values (jaise `padding: 10`) par React khud `"px"` laga deta hai.
* **When to use:** Sirf highly dynamic styles ke liye (jaise progress bar width). Static ke liye Tailwind/CSS use karo.

```tsx
const dynamicStyle: React.CSSProperties = { width: `${progress}%`, borderRadius: 8 };

```

### Concept 9: Extending Native HTML Attributes

* **Rule:** Custom UI element (jaise Button) banate waqt native HTML properties ko inherit karo taaki `onClick`, `disabled` baar-baar na likhna pade.
* **Syntax:** `ComponentPropsWithoutRef` aur `&` operator use karo. DOM node par `{...props}` end mein spread karo.

```tsx
type ButtonProps = CustomProps & React.ComponentPropsWithoutRef<'button'>;

export const Button = ({ variant, ...props }: ButtonProps) => (
  <button className={variant} {...props} />
);

```

### Concept 10: Web Accessibility (WAI-ARIA)

* **Rule:** Native tags (`<button>`, `<nav>`) prefer karo. ARIA sirf custom UI (jaise divs ko button banana) ke liye use karo.
* **`aria-expanded`**: Boolean accept karta hai. Screen reader ko batata hai menu khula hai ya band.
* **`aria-hidden={true}`**: Screen reader se content permanently chupane ke liye (Focusable inputs pe kabhi mat lagana).
* **`role`**: UI ka purpose badalne ke liye (e.g., `role="button"`). Keyboard events ke bina role adhoora hai.

### Concept 11: Next.js Specific Types

* **Server vs Client:** Next.js mein sab kuch by default Server Component hai (fast, secure DB access, SEO friendly). Interactive cheezon (`useState`, `onClick`) ke liye file ke top par `"use client"` likho.
* **Leaf Node Pattern:** Page ko Server Component rakho, sirf interactive chote parts ko Client Component bana kar import karo.
* **Route Typing:** Dynamic URLs ke params pakadne ke liye `PageProps` standard interface use karo.

```tsx
type PageProps = {
  params: { slug: string };
  searchParams?: { [key: string]: string | string[] | undefined };
};

```

### Concept 12: Angular Context

* **Inputs/Outputs:** Parent-Child data flow strict hona chahiye. Output hamesha typed object emit kare.
```typescript
@Output() userSaved = new EventEmitter<User>();

```


* **RxJS Observables:** Streams hain jo `.subscribe()` karne par chalti hain. Memory leak rokne ke liye destroy hone par unsubscribe karo ya HTML template mein `| async` pipe use karo.
* **Typed Reactive Forms (Angular 14+):** Form objects strict hote hain. Reset karne par form null na ho uske liye `nonNullable` use karo.
```typescript
name: new FormControl<string>('', { nonNullable: true })

```

==================================================================================
