# Prompt — Premium Dark Mode Notes Viewer

**Prompt Start:**

You are an expert Frontend Developer.
Your task is to create a single-file `notes_viewer.html` that dynamically renders a Markdown file (e.g., `React_Native_Notes.md`) with a **Premium Dark UI**.
The rendering must look identical to a high-end documentation site (like Stripe or Tailwind docs) and support **Print-to-PDF** with the dark theme preserved.

## 🛠️ Required Dependencies
- **Marked.js**: `https://cdn.jsdelivr.net/npm/marked@4.3.0/marked.min.js` (MUST be v4.3.0)
- **Highlight.js**: `https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js`
- **Highlight CSS**: `https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/atom-one-dark-reasonable.min.css`
- **Fonts**: Inter, Fira Code, Outfit.
- **Icons**: FontAwesome 6.4.0.

## 🎨 HTML Structure & CSS (Critical)

You MUST use this specific wrapper structure and print CSS to ensure the dark theme prints correctly.

```html
<body>
    <div id="loader">Loading...</div>
    
    <!-- WRAPPER IS MANDATORY FOR PRINTING BACKGROUNDS -->
    <div class="print-wrapper">
        <div class="layout">
            <nav class="sidebar" id="sidebar">
                <!-- TOC goes here -->
            </nav>
            <main class="main-content" id="content-area">
                <!-- Markdown content goes here -->
            </main>
        </div>
    </div>
</body>
```

**CSS Rules (Incude these exactly):**

```css
:root {
    /* Color Palette - Deep Dark Theme */
    --bg-primary: #0f1115;
    --bg-secondary: #161b22;
    --text-primary: #ffffff; /* Pure white for better readability */
    --text-secondary: #e6edf3; /* Much brighter grey */
    --accent-blue: #58a6ff;
    --accent-gradient: linear-gradient(135deg, #61dafb 0%, #4facfe 100%);
    --border-color: #30363d;
}

body {
    background-color: var(--bg-primary);
    color: var(--text-primary);
    font-family: 'Inter', sans-serif;
}

h1 {
    font-family: 'Outfit', sans-serif;
    background: var(--accent-gradient);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3rem;
    border-bottom: 3px solid var(--border-color);
}

/* Mac-Style Code Blocks */
pre.mac-window {
    background: #0d1115;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    margin: 2rem 0;
    
    /* STRICT WRAPPING FOR PDF */
    white-space: pre-wrap !important;
    word-break: break-word !important; 
    overflow-x: hidden !important;
}

.code-header {
    background: #161b22;
    padding: 8px 15px;
    border-bottom: 1px solid var(--border-color);
    display: flex; justify-content: space-between;
    align-items: center;
}

/* Dots helper (add these classes too) */
.control { width: 12px; height: 12px; border-radius: 50%; display: inline-block; margin-right: 6px; }
.red { background: #ff5f56; } .yellow { background: #ffbd2e; } .green { background: #27c93f; }

code {
    font-family: 'Fira Code', monospace;
    white-space: pre-wrap !important; 
    word-wrap: break-word !important;
}

/* CRITICAL PRINT STYLES - DO NOT MODIFY */
@media print {
    body { margin: 0; padding: 0; }
    
    .print-wrapper {
        background-color: #0f1115 !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
        min-height: 100vh;
        width: 100%;
        position: absolute; top: 0; left: 0;
        margin: 0; padding: 0;
    }

    /* Force specific TEXT elements to be white for contrast */
    p, li, td, th {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        text-shadow: none !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
         -webkit-print-color-adjust: exact !important;
         print-color-adjust: exact !important;
    }

    /* PRESERVE Code Colors - Explicitly force Highlight.js colors for Print */
    .main-content pre, .main-content code, .hljs {
        background-color: #0d1115 !important;
        /* color: #e6edf3 !important; <-- REMOVED */
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
    }
    
    p code, li code {
        color: #ff7b72 !important;
        background-color: rgba(110, 118, 129, 0.3) !important; 
    }
    
    /* Force specific syntax colors (Atom One Dark approximation) */
    .hljs-keyword, .hljs-literal, .hljs-symbol, .hljs-name { color: #ff7b72 !important; }
    .hljs-link { color: #61aeee !important; }
    .hljs-built_in, .hljs-type { color: #e5c07b !important; }
    .hljs-number, .hljs-class { color: #d19a66 !important; }
    .hljs-string, .hljs-meta-string { color: #98c379 !important; }
    .hljs-title, .hljs-params { color: #61aeee !important; }
    .hljs-comment { color: #5c6370 !important; font-style: italic !important; }

    .sidebar, .copy-btn, .window-controls, #loader {
        display: none !important;
    }
    
    .main-content { padding: 2rem !important; margin: 0; max-width: 100%; }
    
    a { text-decoration: none !important; border: none !important; }
}
```

## 🧠 Javascript Logic (Copy this logic)

Use this specific logic to handle the Markdown parsing. It fixes common bugs and handling specific indented headers.

```javascript
document.addEventListener("DOMContentLoaded", () => {
    // ... Fetch MD logic ...
    
    // 1. Pre-process Markdown (Fix indented modules)
    // Converts "  Module 1:" to "## Module 1:"
    let processed = markdown.replace(/^\s*(Module\s+\d+(\.\d+)?:?)/gm, '## $1');
    // Converts "1.1:" to bold
    processed = processed.replace(/^\s*(\d+\.\d+:)/gm, '**$1**');

    // 2. Configure Renderer
    const renderer = new marked.Renderer();
    
    // Safety check: Cast code to string to avoid [object Object] crash
    renderer.code = function(code, language) {
        const safeCode = code ? String(code) : '';
        // Robust highlighting with Auto-detection
        let highlighted = safeCode;
        // If language is provided and valid, use it
        if (language && hljs.getLanguage(language)) {
            try {
                highlighted = hljs.highlight(safeCode, { language: language }).value;
            } catch (e) { highlighted = hljs.highlightAuto(safeCode).value; }
        } else {
            // Otherwise, or if 'plaintext', force auto-detection
            highlighted = hljs.highlightAuto(safeCode).value;
        }
        
        return `
        <pre class="mac-window">
            <div class="code-header">
                <div class="window-controls">...</div>
                <button onclick="copy(...)">Copy</button>
            </div>
            <code class="hljs language-${validLang}">${highlighted}</code>
        </pre>`;
    };
    
    renderer.heading = function(text, level) {
         const safeText = text ? String(text) : '';
         const id = safeText.toLowerCase().replace(/[^\w]+/g, '-');
         return `<h${level} id="${id}">${safeText}</h${level}>`;
    };

    // 3. Render
    contentArea.innerHTML = marked.parse(processed, { renderer: renderer });
});
```
