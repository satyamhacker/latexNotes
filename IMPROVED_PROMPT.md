Prompt — Colorful Study Notes Converter (IMPROVED VERSION)
With Complete Auto-Renderer Code
Prompt Start (copy everything below):

You are an expert HTML/CSS document designer and note formatter.
Your task is to convert the following raw text notes into a visually stunning, colorful, and professional HTML study notebook following these rules carefully.

🧩 A — Document Layout & Typography
Output must be a complete HTML file (with <style> included — no external CSS or fonts).

Layout should look like a professional printed study notebook, easy to read and print (A4 optimized).

Use:

Body Font: Georgia, "Times New Roman", serif

Headings Font: Arial, Helvetica, sans-serif

Base font size: 12pt

Margins: ~25mm all sides

Comfortable vertical spacing between paragraphs (1.6 line-height)

Each section should have visible breathing space — not cramped.

Background: Light off-white (#fafafa) for better contrast

🎯 B — Topic Headings
Each topic starts with a separator like:

# text

### **Topic Name**

Render the separator visibly using a soft gray horizontal style (color: #bbb, monospace font).

Topic Name should appear in:

Bold large blue font (--heading-blue: #0055cc)

Font size: 22pt

Bottom border (3px solid blue) for emphasis

Subtle text shadow for depth

Padding above and below

Remove literal "###" when rendering.

🔴 C — Important Text Highlighting (CRITICAL)
Automatically identify and highlight important keywords and phrases in bright red (#d40000), bold, and slightly larger (1.08em).

Add a light red background (rgba(212, 0, 0, 0.05)) with padding and border-radius for emphasis.

Keywords to ALWAYS highlight:

"important", "yaad", "dhayan", "remember", "must", "note", "Do not", "jaruri"

"Kyun zaroori", "Best practice", "Always", "Never", "Avoid"

Any phrase indicating consequences: "fail", "crash", "loss", "problem"

Key technical terms that are critical to remember

Also highlight:

Phrases starting with "Kyun zaroori:", "Agar na kiya:", "Best practice:"

Consequences and warnings

Critical steps or requirements (e.g., "Python 3.3+ chahiye")

Wrap such text in <span class="important">...</span>.

This makes key points pop visually for quick revision.

💻 D — Code Blocks & Commands (CRITICAL FOR PDF)
Code sections (inside triple backticks ``` or inline backticks) should appear inside a rounded, bordered, syntax-highlighted box.

IMPORTANT: NO HORIZONTAL SCROLLING - Code must wrap to fit the page width for PDF conversion.

Use:

css
background: #f7f7f7;
border: 1px solid #ddd;
border-radius: 8px;
padding: 15px;
box-shadow: 0 2px 4px rgba(0,0,0,0.08);
font-family: "Courier New", monospace;
overflow-x: visible; /_ NO scrolling _/
white-space: pre-wrap; /_ Wrap long lines _/
word-wrap: break-word; /_ Break long words _/
Add line numbers on the left using CSS counters (gray color #999, 9pt font).

Syntax colors (wrap keywords/strings/functions with appropriate span classes):

Keywords (commands like python, pip, source) → blue (#0074D9)

Strings (arguments, file names) → green (#2ECC40)

Comments → gray italic (#AAAAAA)

Functions (venv, install, activate) → purple (#B10DC9)

Imports → orange (#FF851B)

Inline code (single backtick) should be rendered as <code> with:

Dark red color (#c7254e)

Light red background (rgba(199, 37, 78, 0.08))

Monospace font

Padding and border-radius

PDF Compatibility:

All code must be visible without scrolling

Long lines should wrap automatically

Comments should not get hidden

Use white-space: pre-wrap and word-wrap: break-word in CSS

🎨 E — Color Palette
Use these CSS variables:

css
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
🎨 F — Additional Styling
Subheadings (h4):

Font size: 15pt

Color: #2c5aa0 (darker blue)

Left border: 4px solid #2c5aa0

Padding-left: 10px

Lists (ul, ol):

Proper margins and spacing

Line-height: 1.5

Margin between items: 0.6em

Strong text:

Bold weight

Slightly darker color (#1a1a1a)

🧾 G — Page Header & Footer (Optional for Print)
Header (left): Document title (e.g., "API Testing Notes")

Footer (right): Page number

Use @page and @media print for print support

Ensure code boxes don't break across pages

CRITICAL for PDF: In @media print, ensure:

overflow: visible for code blocks

white-space: pre-wrap for text wrapping

word-wrap: break-word for long lines

No horizontal scrolling

🧱 H — Formatting Details
Keep separator lines like =================================================================== exactly as they are, but style them neatly:

Light gray color (#bbb)

Monospace font

Proper spacing (2.5em top, 0.8em bottom)

After all content, end with one more separator line for closure.

Ensure good spacing between topics.

All text should be justified for professional look.

⚙️ I — Input Placeholder
Your input text notes will appear inside this placeholder:

text
[INSERT YOUR NOTES HERE]
Replace that section with the user's notes and render the full HTML beautifully formatted.

📄 J — Expected Output Structure
Output should be a single complete HTML file like this:

xml

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
✅ K — Final Requirements (CRITICAL)
Do NOT remove or rewrite any words from the notes — only add HTML markup and CSS styling.

Keep Hinglish, punctuation, and spacing exactly the same.

Actively identify and highlight important concepts in red (don't wait for explicit keywords only).

Apply syntax highlighting to ALL code blocks by wrapping commands, functions, and strings with appropriate span classes.

Make it colorful, clean, and easy to study quickly.

CRITICAL: NO SCROLLABLE CODE BLOCKS - All code must wrap for PDF conversion.

The final output should have:

✅ Blue headings with underlines

✅ Red highlighted important keywords throughout

✅ Colorful syntax-highlighted code blocks with line numbers

✅ Professional spacing and layout

✅ Print-ready formatting with NO horizontal scrolling

✅ All code visible without scrolling (wrapped text)

📋 L — Quality Checklist
Before delivering, ensure:

All headings are blue with bottom borders

Important keywords are wrapped in red spans

Code blocks have syntax highlighting (not plain text)

Line numbers appear in code blocks

Separator lines are styled properly

No words from original notes are removed

Layout is clean and professional

NO horizontal scrolling in code blocks

Code wraps properly for PDF conversion

All comments in code are visible (not hidden)

CSS includes white-space: pre-wrap and word-wrap: break-word

🚀 M — AUTO-RENDERER SYSTEM (COMPLETE CODE)
Use this complete HTML code to auto-render your notes with Live Server!

Save this as NotesRenderer.html and place it in the same folder as your notes file.

Setup Instructions:
Save this code as NotesRenderer.html

Create a notes.html file with your raw notes (plain text markdown format)

Open folder with Live Server (VS Code extension)

Both files automatically sync and render beautifully

Print to PDF: Ctrl+P

Complete HTML Code:
xml

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>Study Notes Renderer — Beautiful & Colorful</title>
    <style>
      :root {
        --heading-blue: #0055cc;
        --important-red: #d40000;
        --code-bg: #f7f7f7;
        --keyword-color: #0074d9;
        --string-color: #2ecc40;
        --comment-color: #aaaaaa;
        --function-color: #b10dc9;
        --import-color: #ff851b;
      }
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      body {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 12pt;
        line-height: 1.6;
        background: #fafafa;
        color: #1a1a1a;
        padding: 25mm;
        max-width: 210mm;
        margin: 0 auto;
      }
      h1,
      h2,
      h3,
      h4,
      h5,
      h6 {
        font-family: Arial, Helvetica, sans-serif;
      }
      .topic-heading {
        font-size: 22pt;
        color: var(--heading-blue);
        font-weight: bold;
        border-bottom: 3px solid var(--heading-blue);
        padding: 15px 0 10px 0;
        margin: 2.5em 0 0.8em 0;
        text-shadow: 1px 1px 2px rgba(0, 85, 204, 0.1);
      }
      .separator {
        color: #bbb;
        font-family: "Courier New", monospace;
        margin: 2.5em 0 0.8em 0;
        font-size: 10pt;
        letter-spacing: 0.5px;
      }
      h4 {
        font-size: 15pt;
        color: #2c5aa0;
        border-left: 4px solid #2c5aa0;
        padding-left: 10px;
        margin: 1.5em 0 0.8em 0;
      }
      p {
        margin: 0.6em 0;
        text-align: justify;
      }
      .important {
        color: var(--important-red);
        font-weight: bold;
        font-size: 1.08em;
        background: rgba(212, 0, 0, 0.05);
        padding: 2px 6px;
        border-radius: 3px;
      }
      .code-block {
        background: var(--code-bg);
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 15px;
        margin: 1em 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
        font-family: "Courier New", monospace;
        font-size: 10pt;
        position: relative;
        counter-reset: line;
      }
      .code-block pre {
        margin: 0;
        white-space: pre-wrap;
        word-wrap: break-word;
        overflow-x: visible;
      }
      .code-line {
        display: block;
        padding-left: 3.5em;
        position: relative;
      }
      .code-line:before {
        counter-increment: line;
        content: counter(line);
        position: absolute;
        left: 0;
        width: 2.5em;
        text-align: right;
        color: #999;
        font-size: 9pt;
        padding-right: 1em;
        border-right: 1px solid #ddd;
      }
      code {
        font-family: "Courier New", monospace;
        color: #c7254e;
        background: rgba(199, 37, 78, 0.08);
        padding: 2px 6px;
        border-radius: 3px;
        font-size: 0.95em;
      }
      .keyword {
        color: var(--keyword-color);
        font-weight: bold;
      }
      .string {
        color: var(--string-color);
      }
      .comment {
        color: var(--comment-color);
        font-style: italic;
      }
      .function {
        color: var(--function-color);
        font-weight: bold;
      }
      .import {
        color: var(--import-color);
      }
      .tag {
        color: #e67e22;
        font-weight: bold;
      }
      .attr {
        color: #b10dc9;
      }
      .number {
        color: #d63384;
      }
      .boolean {
        color: #0074d9;
        font-weight: bold;
      }
      ul,
      ol {
        margin: 0.6em 0 0.6em 2em;
        line-height: 1.5;
      }
      li {
        margin: 0.6em 0;
      }
      strong {
        font-weight: bold;
        color: #1a1a1a;
      }
      hr {
        border: none;
        border-top: 1px solid #ddd;
        margin: 2em 0;
      }
      @media print {
        body {
          background: white;
          padding: 15mm;
        }
        .code-block {
          page-break-inside: avoid;
          overflow: visible;
        }
        .topic-heading {
          page-break-after: avoid;
        }
      }
      .separator-line {
        color: #bbb;
        font-family: "Courier New", monospace;
        margin: 2.5em 0 0.8em 0;
      }
    </style>
  </head>
  <body>
    <header
      style="
        font-family: Arial, Helvetica, sans-serif;
        color: #666;
        font-size: 10pt;
        margin-bottom: 8px;
      "
    >
      📚 Study Notes — Auto-Rendered with Beautiful UI
    </header>
    <main id="render-target">
      <p style="color: #666; font-size: 11pt">
        ⏳ Loading formatted notes…
      </p>
    </main>
    <script>
      (async function () {
        const target = document.getElementById("render-target");
        async function loadRaw() {
          try {
            const resp = await fetch("notes.html");
            if (!resp.ok) throw new Error("fetch failed");
            const txt = await resp.text();
            return txt;
          } catch (e) {
            return null;
          }
        }

        const raw = await loadRaw();
        if (!raw) {
          target.innerHTML =
            '<p style="color:#a00"><strong>❌ Error:</strong> Could not load notes.html file.</p><p style="color:#666">Make sure:</p><ul style="color:#666"><li>File named <code>notes.html</code> exists in same folder</li><li>Open with Live Server (VS Code)</li><li>Both files are in same directory</li></ul>';
          return;
        }

        function esc(s) {
          return s
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;");
        }

        const importantWords = [
          "important",
          "yaad rakhna",
          "yaad",
          "dhayan",
          "dhyaan",
          "remember",
          "must",
          "note",
          "Do not",
          "jaruri",
          "Kyun zaroori",
          "Agar na kiya",
          "Agar",
          "Best practice",
          "Always",
          "Never",
          "Avoid",
          "fail",
          "crash",
          "loss",
          "problem",
          "yaad rakhna chaiye",
          "critical",
          "essential",
          "vital",
          "key",
          "crucial"
        ];

        function markImportant(s) {
          if (!s || typeof s !== "string") return s;
          const sentences = s.split(/(?<=[\.\?\!\n])/);
          for (let j = 0; j < sentences.length; j++) {
            const sent = sentences[j];
            const lowered = sent.toLowerCase();
            for (const cue of importantWords) {
              if (!cue) continue;
              const cueLc = cue.toLowerCase();
              if (lowered.indexOf(cueLc) !== -1) {
                sentences[j] =
                  '<span class="important">' + esc(sent) + "</span>";
                break;
              }
            }
            if (!/^<span class=\"important\">/.test(sentences[j])) {
              let out = esc(sentences[j]);
              const phrases = importantWords
                .slice()
                .sort((a, b) => b.length - a.length);
              for (const ph of phrases) {
                if (!ph) continue;
                const phEsc = ph.replace(/[-/\\^$*+?.()|[\]{}]/g, "\\$&");
                const re = new RegExp(phEsc, "gi");
                out = out.replace(re, function (m) {
                  return '<span class="important">' + m + "</span>";
                });
              }
              sentences[j] = out;
            }
          }
          return sentences.join("");
        }

        function highlightCode(code) {
          let s = esc(code);
          s = s.replace(/(\/\/.*?$)/gm, '<span class="comment">$1</span>');
          s = s.replace(/(^|\n)(\s*#.*?$)/gm, function (m, p1, p2) {
            return p1 + '<span class="comment">' + p2 + "</span>";
          });
          s = s.replace(/("[^"]*"|'[^']*')/g, '<span class="string">$1</span>');
          s = s.replace(
            /(&lt;\/?[A-Za-z0-9\-:\.]+)([^&]*?)(&gt;)/g,
            function (m, p1, p2, p3) {
              let attrs = p2.replace(
                /([a-zA-Z_:][-a-zA-Z0-9_:.]*)=("[^"]*"|'[^']*')/g,
                '<span class="attr">$1</span>=<span class="string">$2</span>'
              );
              return (
                '<span class="tag">' +
                p1 +
                "</span>" +
                attrs +
                '<span class="tag">' +
                p3 +
                "</span>"
              );
            }
          );
          s = s.replace(
            /\b(\d+(?:\.\d+)?)\b/g,
            '<span class="number">$1</span>'
          );
          s = s.replace(
            /\b(true|false|null)\b/gi,
            '<span class="boolean">$1</span>'
          );
          const kw = [
            "abstract",
            "assert",
            "boolean",
            "break",
            "byte",
            "case",
            "catch",
            "char",
            "class",
            "const",
            "continue",
            "default",
            "do",
            "double",
            "else",
            "enum",
            "extends",
            "final",
            "finally",
            "float",
            "for",
            "goto",
            "if",
            "implements",
            "import",
            "instanceof",
            "int",
            "interface",
            "long",
            "native",
            "new",
            "package",
            "private",
            "protected",
            "public",
            "return",
            "short",
            "static",
            "strictfp",
            "super",
            "switch",
            "synchronized",
            "this",
            "throw",
            "throws",
            "transient",
            "try",
            "void",
            "volatile",
            "while",
            "cd",
            "ls",
            "mkdir",
            "npm",
            "pip",
            "python",
            "java",
          ];
          s = s.replace(
            new RegExp("\\b(" + kw.join("|") + ")\\b", "gi"),
            '<span class="keyword">$1</span>'
          );
          s = s.replace(
            /(import\s+[\w\.\*]+)/g,
            '<span class="import">$1</span>'
          );
          s = s.replace(
            /([A-Za-z_][A-Za-z0-9_]*)\s*\(/g,
            '<span class="function">$1</span>('
          );
          return s;
        }

        const lines = raw.replace(/\r/g, "").split("\n");
        const frag = document.createDocumentFragment();
        let i = 0,
          inCode = false,
          codeLang = "",
          codeBuf = [];
        function flushCode() {
          if (!inCode) return;
          const div = document.createElement("div");
          div.className = "code-block";
          const pre = document.createElement("pre");
          const inner = highlightCode(codeBuf.join("\n"))
            .split("\n")
            .map((l) => '<span class="code-line">' + l + "</span>")
            .join("\n");
          pre.innerHTML = inner;
          div.appendChild(pre);
          frag.appendChild(div);
          inCode = false;
          codeBuf = [];
          codeLang = "";
        }

        while (i < lines.length) {
          const L = lines[i];
          const mCode = L.match(/^```\s*(\w+)?/);
          if (mCode) {
            if (!inCode) {
              inCode = true;
              codeLang = mCode || "";
              codeBuf = [];
            } else {
              flushCode();
            }
            i++;
            continue;
          }
          if (inCode) {
            codeBuf.push(L);
            i++;
            continue;
          }

          if (/^=+\s*$/.test(L) || /^-+\s*$/.test(L)) {
            const d = document.createElement("div");
            d.className = "separator-line";
            d.textContent = L.trim();
            frag.appendChild(d);
            i++;
            continue;
          }
          if (/^#\s+/.test(L)) {
            const h = document.createElement("h1");
            h.className = "topic-heading";
            h.innerHTML = markImportant(esc(L.replace(/^#\s+/, "")));
            frag.appendChild(h);
            i++;
            continue;
          }
          if (/^##\s+/.test(L)) {
            const h2 = document.createElement("h2");
            h2.innerHTML = markImportant(esc(L.replace(/^##\s+/, "")));
            frag.appendChild(h2);
            i++;
            continue;
          }
          if (/^###\s+/.test(L)) {
            const h3 = document.createElement("h3");
            h3.innerHTML = markImportant(esc(L.replace(/^###\s+/, "")));
            frag.appendChild(h3);
            i++;
            continue;
          }
          if (/^\*\*\*\s*$/.test(L)) {
            frag.appendChild(document.createElement("hr"));
            i++;
            continue;
          }
          if (/^\s*[-*]\s+/.test(L)) {
            const ul = document.createElement("ul");
            while (i < lines.length && /^\s*[-*]\s+/.test(lines[i])) {
              const li = document.createElement("li");
              li.innerHTML = markImportant(
                esc(lines[i].replace(/^\s*[-*]\s+/, ""))
              );
              ul.appendChild(li);
              i++;
            }
            frag.appendChild(ul);
            continue;
          }
          if (/^\s*\d+\.\s+/.test(L)) {
            const ol = document.createElement("ol");
            while (i < lines.length && /^\s*\d+\.\s+/.test(lines[i])) {
              const li = document.createElement("li");
              li.innerHTML = markImportant(
                esc(lines[i].replace(/^\s*\d+\.\s+/, ""))
              );
              ol.appendChild(li);
              i++;
            }
            frag.appendChild(ol);
            continue;
          }
          if (/^\s*$/.test(L)) {
            i++;
            continue;
          }
          let phtml = esc(L);
          phtml = phtml.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
          phtml = phtml.replace(/`([^`]+)`/g, "<code>$1</code>");
          phtml = markImportant(phtml);
          const p = document.createElement("p");
          p.innerHTML = phtml;
          frag.appendChild(p);
          i++;
        }
        flushCode();
        target.innerHTML = "";
        target.appendChild(frag);
      })();
    </script>

  </body>
</html>
🎯 WORKFLOW WITH LIVE SERVER
Step 1: Save the HTML code above as NotesRenderer.html

Step 2: Create a file named notes.html in same folder with your notes

Step 3: Format your notes with markdown:

text

# Topic Name

This is important concept that must be remembered.

## Subtitle

- List item 1
- List item 2

\`\`\`java
// Your code here
public void example() {
System.out.println("Hello");
}
\`\`\`
Step 4: Open folder with Live Server (right-click → Open with Live Server)

Step 5: Refresh automatically when notes change

Step 6: Print to PDF (Ctrl+P)
