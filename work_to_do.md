
==================================================================================

## Module 5: Typing React Components (Web & Mobile Shared)


### DEPENDENCY MAP

* **CONCEPT 1 — Component Props Typing & `ReactNode**` → no dependencies (start here)
* **CONCEPT 2 — Standard Typed Functions vs `React.FC**` → needs Concept 1
* **CONCEPT 3 — Polymorphic Components (`as` prop pattern)** → needs Concept 1 + Concept 2
* **CONCEPT 4 — Component as Props (Slot Pattern)** → needs Concept 1

---

### CONCEPT 1 — Component Props Typing & `ReactNode` [Beginner]

📌 Prerequisites: None (start here)

#### ── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What is component prop typing and `ReactNode`? Define it in simple words.
[STRUCTURE] 🟢 What are the mandatory fields and syntax for typing a React component interface? What goes inside each one? Show the minimal working code skeleton for a typed component.
[WHEN] 🟡 When should I use strict interface typing for my component props? Give 3 real-world situations/triggers. When should I NOT use explicit prop typing (if ever)?
[COMPARE] 🟡 How is `type` (Type Alias) different from `interface` for defining React props? Make a clear side-by-side comparison table covering: extensibility, IDE hover behavior, and when to use which.
[PURPOSE] 🟡 If strict TypeScript typing for props didn't exist, what exact problem would I face in a production app? Why was it adopted over plain JavaScript?
[ANTI-PATTERN] 🔴 What is the wrong way to type props (e.g., using `any` or typing `children` as `JSX.Element`)? What common mistake do beginners make when facing TS errors? What is the correct approach instead?
[REAL EXAMPLE] 🟡 Give a real-world scenario (like the Shopify Polaris design system) where strict prop interfaces are used. Show exactly how it fits into the design system's architecture.
[BREAK IT] 🔴 What can go wrong when rendering user-provided strings via props using `dangerouslySetInnerHTML`? What exact XSS vulnerability can occur, and how do you fix it using libraries like DOMPurify? `[🔍 Verify from docs]`

#### ── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**Parameter: `title**`
[PARAM-WHAT] 🟢 What is the `title` parameter in the `CardProps` interface? What does it do? What happens if I don't pass it from the parent component?
[PARAM-VALUES] 🟡 What values can the `title` parameter accept based on its type? What is the default value if any? Show an example of a valid value.
[PARAM-MISTAKE] 🔴 What is the most common mistake with the `title` parameter? What exact error or silent bug will I get if I pass a number instead of a string?
[PARAM-REALCODE] 🟡 Show exactly how the `title` parameter is destructured and used in a real working React code snippet. Why is the string type specifically chosen here?

**Parameter: `isActive**`
[PARAM-WHAT] 🟢 What is the `isActive` parameter? What does the `?` symbol next to it indicate? What happens if I don't pass it?
[PARAM-VALUES] 🟡 What values can `isActive` accept? What is its default fallback value inside the component parameters? Show examples of passing true, false, and nothing.
[PARAM-MISTAKE] 🔴 What is the most common mistake with optional boolean parameters like `isActive`? What exact error or UI bug will I get if I don't provide a default value and try to use it in a template literal?
[PARAM-REALCODE] 🟡 Show exactly how `isActive` is used in a real working code snippet to toggle a CSS class. Why is `false` chosen as the specific default value here?

**Parameter: `children**`
[PARAM-WHAT] 🟢 What is the `children` parameter? What does it represent in React? What happens if I don't pass it when it is marked as required in the interface?
[PARAM-VALUES] 🟡 What values can the `children` parameter accept when typed as `ReactNode`? Show an example of each possible value (string, valid React element, null).
[PARAM-MISTAKE] 🔴 What is the most common mistake when typing the `children` parameter (e.g., using `JSX.Element` instead of `ReactNode`)? What exact error will I get if I try to pass a plain text string to a `JSX.Element`?
[PARAM-REALCODE] 🟡 Show exactly how the `children` parameter is passed between opening and closing tags in a parent component, and how it is rendered in the child component snippet.

---

### CONCEPT 2 — Standard Typed Functions vs `React.FC` [Beginner]

📌 Prerequisites: Concept 1

#### ── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What is `React.FC` (FunctionComponent) and why is it now deprecated/discouraged by the React team? Define it in simple words.
[STRUCTURE] 🟢 What is the mandatory syntax for defining a standard functional component without using `React.FC`? Show the minimal working code skeleton typing the props directly.
[WHEN] 🟡 When should I use standard typed functions? Give 3 real-world situations. When should I NOT use `React.FC`?
[COMPARE] 🟡 How does a Standard Typed Function compare to `React.FC`? Make a clear side-by-side comparison table covering: implicit children behavior, Generics support (`<T>`), readability, and future-proofing.
[PURPOSE] 🟡 If standard functional components hadn't replaced `React.FC`, what exact problem would I face when building dynamic/generic components in modern React 18+ codebases?
[ANTI-PATTERN] 🔴 What is the wrong way to define a component in new projects? What common mistake do beginners make regarding `defaultProps` or generics when using `React.FC`? What is the correct approach instead?
[REAL EXAMPLE] 🟡 Give a real-world scenario (like Meta's React 18 codebase migration) where `React.FC` was mass-removed via codemods. Show exactly how this cleans up the system.
[BREAK IT] 🔴 What could go wrong in React 17 when relying on the implicit `children` of `React.FC`? What exact silent bug occurs on the UI? What is the root cause and fix?

#### ── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**Parameter: `P` (Generic Props in `React.FC<P>`)**
[PARAM-WHAT] 🟢 What is the generic parameter `P` in `React.FC<P>`? What does it represent? What happens if I don't pass it?
[PARAM-VALUES] 🟡 What values/types can `P` accept? What is the default type (`{}`) if omitted? Show an example of passing a custom interface to it.
[PARAM-MISTAKE] 🔴 What is the most common mistake with the `P` parameter when trying to build a Generic component (like `<Table<User>>`)? What exact syntax error will I get?
[PARAM-REALCODE] 🟡 Show exactly how the generic `P` parameter pattern is discarded and replaced by direct prop typing in a real working modern functional component snippet.

**Parameter: implicit `children` (Legacy `React.FC` behavior)**
[PARAM-WHAT] 🟢 What is the implicit `children` property that used to exist inside `React.FC`? What happens if I don't explicitly define it in my interface but use `React.FC` in React 17?
[PARAM-VALUES] 🟡 What values could this implicit `children` accept? Show examples of what the TS compiler allowed to be passed.
[PARAM-MISTAKE] 🔴 What is the most common mistake when migrating away from `React.FC` regarding the `children` parameter? What exact error (`Binding element 'children' implicitly has an 'any' type`) will I get?
[PARAM-REALCODE] 🟡 Show exactly how the `children` parameter must now be explicitly typed and destructured in a real working standard function component.

---

### CONCEPT 3 — Polymorphic Components (`as` prop pattern) [Intermediate]

📌 Prerequisites: Concept 1, Concept 2

#### ── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What is a Polymorphic Component? Define it in simple words.
[STRUCTURE] 🟢 What are the mandatory fields, utility types, and syntax to create a polymorphic component? What goes inside each one? Show the minimal working code skeleton (including `ElementType`).
[WHEN] 🟡 When should I use the Polymorphic Component pattern? Give 3 real-world situations/triggers (e.g., SEO requirements). When should I NOT use it?
[COMPARE] 🟡 How does a Polymorphic Component compare to Hardcoded Wrapper Components (e.g., `<H1Text>`, `<PText>`)? Make a clear side-by-side comparison table covering: maintenance overhead, flexibility, and TypeScript complexity.
[PURPOSE] 🟡 If Polymorphic components didn't exist, what exact problem would I face regarding semantic HTML, SEO, and CSS duplication? Why was this pattern created?
[ANTI-PATTERN] 🔴 What is the wrong way to implement dynamic tags (e.g., using massive switch-cases or failing to capitalize the dynamic tag variable)? What common beginner trap causes invalid HTML tags like `<as>` to render? What is the correct approach instead?
[REAL EXAMPLE] 🟡 Give a real-world scenario (like Material UI/MUI or a shared Web/Mobile Typography component) where polymorphic components are used. Show exactly how it fits into the design system.
[BREAK IT] 🔴 What can go wrong when passing un-sanitized, user-provided string data to the `as` prop? What exact security vulnerability (injection) will occur, and how do you fix it with an allowlist?

#### ── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**Parameter: `variant**`
[PARAM-WHAT] 🟢 What is the `variant` parameter in a design system component? What does it control? What happens if I don't pass it?
[PARAM-VALUES] 🟡 What values can the `variant` parameter accept in the Typography example? What is the default fallback value if any? Show an example of each possible value.
[PARAM-MISTAKE] 🔴 What is the most common mistake with the `variant` parameter? What exact TypeScript error will I get if I pass an undocumented string?
[PARAM-REALCODE] 🟡 Show exactly how the `variant` parameter is mapped to specific CSS classes dynamically in a real working code snippet.

**Parameter: `as` (or `component`)**
[PARAM-WHAT] 🟢 What is the `as` parameter typed as `ElementType`? What does it dictate to the React rendering engine? What happens if I don't pass it?
[PARAM-VALUES] 🟡 What values can the `as` parameter accept? Show an example of passing a standard HTML string tag vs passing a React Router `Link` component.
[PARAM-MISTAKE] 🔴 What is the most common mistake with the `as` parameter when creating the JSX tag (e.g., `<as>{children}</as>`)? What exact DOM error or rendering bug will I get?
[PARAM-REALCODE] 🟡 Show exactly how the `as` parameter is safely aliased with a capital letter (e.g., `const Component = as || variant`) and rendered in a real working code snippet. Why is this capital letter capitalization strictly required by React?

**Parameter: `...restProps` (HTMLAttributes)**
[PARAM-WHAT] 🟢 What is the `...restProps` spread parameter? What does it do by inheriting `HTMLAttributes<HTMLElement>`? What happens to standard HTML props if I don't spread it onto the final element?
[PARAM-VALUES] 🟡 What values/keys does `...restProps` capture? Show examples of HTML attributes it safely absorbs (like `className`, `id`, `onClick`).
[PARAM-MISTAKE] 🔴 What is the most common mistake when using `...restProps` alongside the `as` prop? What exact error (`React does not recognize the 'as' prop on a DOM element`) will I get if I don't destructure `as` out of the props first?
[PARAM-REALCODE] 🟡 Show exactly how `...restProps` is correctly destructured and spread onto the dynamic element in a real working code snippet. `[🔍 Verify from docs how Omit is used to prevent prop clashing here]`.

---

### CONCEPT 4 — Component as Props (Slot Pattern) [Advanced]

📌 Prerequisites: Concept 1

#### ── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What is the "Passing components as props" (Slot Pattern / Render Props) technique? Define it in simple words using the Inversion of Control concept.
[STRUCTURE] 🟢 What are the mandatory types and syntax for accepting components as props in an interface? What goes inside each one? Show the minimal working code skeleton using `ReactNode` and `ComponentType`.
[WHEN] 🟡 When should I use the Slot Pattern? Give 3 real-world situations/triggers (e.g., Page Layouts). When should I NOT use it and stick to the standard `children` prop?
[COMPARE] 🟡 How does Passing Components as Props compare to Passing State/Props Down (Prop Drilling)? Make a clear side-by-side comparison table covering: data flow direction, component coupling, and best use cases.
[PURPOSE] 🟡 If the Slot Pattern didn't exist, what exact problem would I face in large applications regarding reusable wrapper components? How does this solve the "bloated if-else inside Modals" issue?
[ANTI-PATTERN] 🔴 What is the wrong way to pass components as props (e.g., overusing `React.cloneElement` to force props down, or turning simple text into component props)? What is the correct approach instead?
[REAL EXAMPLE] 🟡 Give a real-world scenario (like building Headers in React Navigation for Mobile) where components are passed as props. Show exactly how it fits into the layout engine.
[BREAK IT] 🔴 What can go wrong when mixing up `ReactNode` and `ComponentType` typings? What exact error (`Functions are not valid as a React child` or `Type '() => Element' is not assignable to type 'ReactNode'`) will I see, and how do I fix it?

#### ── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**Parameter: `header` (typed as `ReactNode`)**
[PARAM-WHAT] 🟢 What is the `header` parameter when strictly typed as `ReactNode`? What role does it play in the layout? What happens if I don't pass it?
[PARAM-VALUES] 🟡 What values can the `header` parameter accept? Show an example of an instantiated JSX element being passed to it from the parent.
[PARAM-MISTAKE] 🔴 What is the most common mistake with a `ReactNode` typed slot parameter? What exact runtime error will I get if I pass a function reference `() => <Header />` instead of an instantiated element?
[PARAM-REALCODE] 🟡 Show exactly how the `header` parameter is passed down and rendered directly inside a `div` wrapper in a real working layout snippet.

**Parameter: `SidebarComponent` (typed as `ComponentType`)**
[PARAM-WHAT] 🟢 What is the `SidebarComponent` parameter when typed as `ComponentType`? How does it differ fundamentally from `ReactNode`? What happens if I don't pass it?
[PARAM-VALUES] 🟡 What values can `SidebarComponent` accept? Show an example of passing a component reference (un-instantiated function name) to it.
[PARAM-MISTAKE] 🔴 What is the most common mistake when rendering a `ComponentType` parameter inside the parent layout? What exact silent failure or error will I get if I forget to mount it with JSX brackets (e.g., writing `{SidebarComponent}` instead of `<SidebarComponent />`)?
[PARAM-REALCODE] 🟡 Show exactly how `SidebarComponent` is executed/mounted dynamically inside a real working layout snippet, demonstrating how the parent layout retains control of rendering it.

---

### 📊 STUDY SET SUMMARY

→ **Total concept count:** 4
→ **Total parameter count covered:** 9
→ **Total question count:** 68
→ **Recommended study order:** 1. Component Props Typing & `ReactNode`
2. Standard Typed Functions vs `React.FC`
3. Polymorphic Components (`as` prop pattern)
4. Component as Props (Slot Pattern)

**🏆 Scoring System:**

* 🟢 Beginner = 1 pt
* 🟡 Intermediate = 2 pts
* 🔴 Advanced = 3 pts
* **Mastery Threshold:** 85% of total points
* **Self-check method:** Attempt all → compare with official docs → add 1 pt per verified correct understanding.

==================================================================================
