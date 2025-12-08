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

h2 {
    color: var(--text-primary);
    font-size: 2rem;
    margin-top: 2.5rem;
    margin-bottom: 1rem;
    border-bottom: 2px solid var(--border-color);
    padding-bottom: 0.5rem;
}

/* Topic & Module Sections - Big Bold Blue */
h2.topic-section, h2.module-section {
    font-family: 'Outfit', sans-serif;
    font-size: 2.5rem;
    font-weight: 800;
    color: #4facfe;
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    border-left: 5px solid #4facfe;
    padding-left: 1rem;
    margin-top: 3rem;
    margin-bottom: 1.5rem;
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

table {
    width: 100%;
    border-collapse: collapse;
    margin: 2rem 0;
    background: var(--bg-secondary);
    border-radius: 8px;
    overflow: hidden;
}

th, td {
    padding: 1rem;
    text-align: left;
    border: 1px solid var(--border-color);
}

th {
    background: #1c2128;
    color: var(--accent-blue);
    font-weight: 600;
}

tr:hover {
    background: rgba(88, 166, 255, 0.1);
}

/* CRITICAL PRINT STYLES - DO NOT MODIFY */
@media print {
    * {
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
        color-adjust: exact !important;
    }

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

    /* Force white text for readability */
    .main-content, p, li, h1, h2, h3, h4, h5, h6, td, th {
        color: #ffffff !important;
    }

    /* Keep code blocks distinct */
    pre {
        border: 1px solid #444;
        page-break-inside: avoid;
    }

    .sidebar, .copy-btn, .window-controls, #loader {
        display: none !important;
    }

    .layout {
        display: block;
    }
    
    .main-content { padding: 2rem !important; margin: 0 auto; max-width: 100%; }
    
    a { text-decoration: none !important; border-bottom: none !important; }
}
```

## 🧠 Javascript Logic (Copy this logic)

Use this specific logic to handle the Markdown parsing. It fixes common bugs and handling specific indented headers.

```javascript
document.addEventListener("DOMContentLoaded", () => {
    // ... Fetch MD logic ...
    
    // 1. Pre-process Markdown (Fix indented modules)
    // Converts "  Module 1:" to "## MODULE_MARKER Module 1:"
    let processed = markdown.replace(/^\s*(Module\s+\d+(\.\d+)?:?)/gm, '## MODULE_MARKER $1');
    // Converts "Topic X.X:" to special heading
    processed = processed.replace(/^##\s+(Topic\s+\d+\.\d+:.*)/gm, '## TOPIC_MARKER $1');
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
         
         // Check if this is a Module section
         if (safeText.startsWith('MODULE_MARKER ')) {
             const cleanText = safeText.replace('MODULE_MARKER ', '');
             const cleanId = cleanText.toLowerCase().replace(/[^\w]+/g, '-');
             return `<h${level} class="module-section" id="${cleanId}">${cleanText}</h${level}>`;
         }
         
         // Check if this is a Topic section
         if (safeText.startsWith('TOPIC_MARKER ')) {
             const cleanText = safeText.replace('TOPIC_MARKER ', '');
             const cleanId = cleanText.toLowerCase().replace(/[^\w]+/g, '-');
             return `<h${level} class="topic-section" id="${cleanId}">${cleanText}</h${level}>`;
         }
         
         return `<h${level} id="${id}">${safeText}</h${level}>`;
    };

    // 3. Render
    contentArea.innerHTML = marked.parse(processed, { renderer: renderer });
});
```
