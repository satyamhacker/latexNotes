# Prompt — Colorful Study Notes Converter (IMPROVED VERSION)

**Prompt Start (copy everything below):**

---

You are an expert HTML/CSS document designer and note formatter.
Your task is to **convert the following raw text notes** into a **visually stunning, colorful, and professional HTML study notebook** following these rules carefully.

---

## 🧩 A — Document Layout & Typography

* Output must be a **complete HTML file** (with `<style>` included — no external CSS or fonts).
* Layout should look like a **professional printed study notebook**, easy to read and print (A4 optimized).
* Use:
  * **Body Font:** Georgia, "Times New Roman", serif
  * **Headings Font:** Arial, Helvetica, sans-serif
* Base font size: **12pt**
* Margins: ~25mm all sides
* Comfortable vertical spacing between paragraphs (1.6 line-height)
* Each section should have visible breathing space — not cramped.
* Background: Light off-white (#fafafa) for better contrast

---

## 🎯 B — Topic Headings

* Each topic starts with a separator like:
  ```
  ===================================================================
  ### **Topic Name**
  ```
* Render the separator visibly using a **soft gray horizontal style** (color: #bbb, monospace font).
* Topic Name should appear in:
  * **Bold large blue font** (`--heading-blue: #0055cc`)
  * Font size: 22pt
  * **Bottom border** (3px solid blue) for emphasis
  * Subtle text shadow for depth
  * Padding above and below
* Remove literal "###" when rendering.

---

## 🔴 C — Important Text Highlighting (CRITICAL)

* **Automatically identify and highlight** important keywords and phrases in **bright red (#d40000)**, **bold**, and slightly larger (1.08em).
* Add a **light red background** (rgba(212, 0, 0, 0.05)) with padding and border-radius for emphasis.
* Keywords to ALWAYS highlight:
  * "important", "yaad", "dhayan", "remember", "must", "note", "Do not", "jaruri"
  * "Kyun zaroori", "Best practice", "Always", "Never", "Avoid"
  * Any phrase indicating consequences: "fail", "crash", "loss", "problem"
  * Key technical terms that are critical to remember
* **Also highlight:**
  * Phrases starting with "Kyun zaroori:", "Agar na kiya:", "Best practice:"
  * Consequences and warnings
  * Critical steps or requirements (e.g., "Python 3.3+ chahiye")
* Wrap such text in `<span class="important">...</span>`.
* This makes key points pop visually for **quick revision**.

---

## 💻 D — Code Blocks & Commands (CRITICAL FOR PDF)

* Code sections (inside triple backticks ``` or inline backticks) should appear inside a **rounded, bordered, syntax-highlighted box**.
* **IMPORTANT: NO HORIZONTAL SCROLLING** - Code must wrap to fit the page width for PDF conversion.
* Use:
  ```css
  background: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.08);
  font-family: "Courier New", monospace;
  overflow-x: visible;  /* NO scrolling */
  white-space: pre-wrap;  /* Wrap long lines */
  word-wrap: break-word;  /* Break long words */
  ```
* **Add line numbers** on the left using CSS counters (gray color #999, 9pt font).
* **Syntax colors** (wrap keywords/strings/functions with appropriate span classes):
  * **Keywords** (commands like python, pip, source) → blue (`#0074D9`)
  * **Strings** (arguments, file names) → green (`#2ECC40`)
  * **Comments** → gray italic (`#AAAAAA`)
  * **Functions** (venv, install, activate) → purple (`#B10DC9`)
  * **Imports** → orange (`#FF851B`)
* **Inline code** (single backtick) should be rendered as `<code>` with:
  * Dark red color (#c7254e)
  * Light red background (rgba(199, 37, 78, 0.08))
  * Monospace font
  * Padding and border-radius
* **PDF Compatibility:**
  * All code must be visible without scrolling
  * Long lines should wrap automatically
  * Comments should not get hidden
  * Use `white-space: pre-wrap` and `word-wrap: break-word` in CSS

---

## 🎨 E — Color Palette

Use these CSS variables:

```css
:root {
  --heading-blue: #0055cc;
  --important-red: #d40000;
  --code-bg: #f7f7f7;
  --keyword-color: #0074D9;
  --string-color: #2ECC40;
  --comment-color: #AAAAAA;
  --function-color: #B10DC9;
  --import-color: #FF851B;
}
```

---

## 🎨 F — Additional Styling

* **Subheadings (h4):**
  * Font size: 15pt
  * Color: #2c5aa0 (darker blue)
  * Left border: 4px solid #2c5aa0
  * Padding-left: 10px
* **Lists (ul, ol):**
  * Proper margins and spacing
  * Line-height: 1.5
  * Margin between items: 0.6em
* **Strong text:**
  * Bold weight
  * Slightly darker color (#1a1a1a)

---

## 🧾 G — Page Header & Footer (Optional for Print)

* Header (left): Document title (e.g., "API Testing Notes")
* Footer (right): Page number
* Use `@page` and `@media print` for print support
* Ensure code boxes don't break across pages
* **CRITICAL for PDF:** In `@media print`, ensure:
  * `overflow: visible` for code blocks
  * `white-space: pre-wrap` for text wrapping
  * `word-wrap: break-word` for long lines
  * No horizontal scrolling

---

## 🧱 H — Formatting Details

* Keep separator lines like `===================================================================` exactly as they are, but style them neatly:
  * Light gray color (#bbb)
  * Monospace font
  * Proper spacing (2.5em top, 0.8em bottom)
* After all content, end with one more separator line for closure.
* Ensure good spacing between topics.
* All text should be justified for professional look.

---

## ⚙️ I — Input Placeholder

Your input text notes will appear inside this placeholder:

```
[INSERT YOUR NOTES HERE]
```

Replace that section with the user's notes and render the full HTML beautifully formatted.

---

## 📄 J — Expected Output Structure

Output should be a **single complete HTML file** like this:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Study Notes</title>
<style>
/* All CSS styles from rules above go here */
</style>
</head>
<body>
<!-- Beautifully formatted notes go here -->
</body>
</html>
```

---

## ✅ K — Final Requirements (CRITICAL)

1. Do **NOT remove or rewrite** any words from the notes — only add HTML markup and CSS styling.
2. Keep **Hinglish**, punctuation, and spacing exactly the same.
3. **Actively identify and highlight** important concepts in red (don't wait for explicit keywords only).
4. **Apply syntax highlighting** to ALL code blocks by wrapping commands, functions, and strings with appropriate span classes.
5. Make it **colorful**, **clean**, and **easy to study quickly**.
6. **CRITICAL: NO SCROLLABLE CODE BLOCKS** - All code must wrap for PDF conversion.
7. The final output should have:
   - ✅ Blue headings with underlines
   - ✅ Red highlighted important keywords throughout
   - ✅ Colorful syntax-highlighted code blocks with line numbers
   - ✅ Professional spacing and layout
   - ✅ Print-ready formatting with NO horizontal scrolling
   - ✅ All code visible without scrolling (wrapped text)

---

## 📋 L — Quality Checklist

Before delivering, ensure:
- [ ] All headings are blue with bottom borders
- [ ] Important keywords are wrapped in red spans
- [ ] Code blocks have syntax highlighting (not plain text)
- [ ] Line numbers appear in code blocks
- [ ] Separator lines are styled properly
- [ ] No words from original notes are removed
- [ ] Layout is clean and professional
- [ ] **NO horizontal scrolling in code blocks**
- [ ] Code wraps properly for PDF conversion
- [ ] All comments in code are visible (not hidden)
- [ ] CSS includes `white-space: pre-wrap` and `word-wrap: break-word`

---

Now, take my text notes below and convert them to a **visually stunning HTML document** following all these rules:

```
[INSERT YOUR NOTES HERE]
```

---

**Prompt End**
