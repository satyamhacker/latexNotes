# Prompt — Premium Dark Mode Notes Viewer

**Prompt Start:**

You are an expert Frontend Developer.

**CRITICAL INSTRUCTION FOR AI:** 
1. When generating the JavaScript code, **DO NOT escape backticks (\`) or dollar signs ($)** in your template literals.
2. Include the full `fetch` block provided in the logic below, handling `response.status !== 0` so local `file:///` viewing works without a server.

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

**CSS Rules (Include these exactly):**

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

/* Module Sections - Big Bold Blue */
.module-section {
    font-family: 'Outfit', sans-serif;
    font-size: 2.5rem;
    font-weight: 800;
    color: #4facfe;
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    border-left: 6px solid #4facfe;
    padding-left: 1rem;
    margin-top: 4rem;
    margin-bottom: 2rem;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Topic Sections - Distinct Vibrant Gradient */
.topic-section {
    font-family: 'Outfit', sans-serif;
    font-size: 1.7rem;
    font-weight: 700;
    background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); /* Orange-ish gradient */
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    border-left: 4px solid #fda085;
    padding-left: 1rem;
    margin-top: 2.5rem;
    margin-bottom: 1.2rem;
    padding-top: 0.2rem;
    padding-bottom: 0.2rem;
    background-color: rgba(253, 160, 133, 0.05); /* very subtle background for depth */
    border-radius: 0 8px 8px 0;
    display: inline-block; /* Makes background fit the text width + padding */
    width: 100%;
    box-sizing: border-box;
}

/* Ensure normal H3 looks standard */
h3:not(.topic-section) {
    color: var(--text-primary);
    font-size: 1.4rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 0.4rem;
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

/* Inline Code Styling */
p code, li code, td code {
    background-color: rgba(88, 166, 255, 0.15);
    color: #79c0ff;
    padding: 0.2em 0.4em;
    border-radius: 6px;
    font-size: 0.9em;
    font-family: 'Fira Code', monospace;
    border: 1px solid rgba(88, 166, 255, 0.2);
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

/* Sidebar */
.sidebar {
    width: 260px;
    min-height: 100vh;
    background: var(--bg-secondary);
    border-right: 1px solid var(--border-color);
    padding: 2rem 1rem;
    position: sticky;
    top: 0;
    overflow-y: auto;
    flex-shrink: 0;
}

.sidebar a {
    display: block;
    color: var(--text-secondary);
    text-decoration: none;
    padding: 0.4rem 0.75rem;
    border-radius: 6px;
    font-size: 0.875rem;
    transition: background 0.2s, color 0.2s;
}

.sidebar a:hover {
    background: rgba(88, 166, 255, 0.12);
    color: var(--accent-blue);
}

.layout {
    display: flex;
    min-height: 100vh;
}

.main-content {
    flex: 1;
    padding: 3rem 4rem;
    max-width: 900px;
    margin: 0 auto;
    line-height: 1.7;
    font-size: 1.05rem;
}

/* Content Links */
.main-content a {
    color: #58a6ff;
    text-decoration: none;
    border-bottom: 1px dashed rgba(88, 166, 255, 0.5);
    transition: all 0.2s;
}
.main-content a:hover {
    color: #79c0ff;
    border-bottom: 1px solid #79c0ff;
}

/* Images */
img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    margin: 1.5rem 0;
    border: 1px solid var(--border-color);
}

/* Task Lists / Checkboxes */
input[type="checkbox"] {
    accent-color: #58a6ff;
    width: 1.2rem;
    height: 1.2rem;
    margin-right: 0.5rem;
    cursor: pointer;
    position: relative;
    top: 2px;
}

/* Blockquote */
blockquote {
    border-left: 4px solid var(--accent-blue);
    background: rgba(88, 166, 255, 0.06);
    margin: 1.5rem 0;
    padding: 1rem 1.5rem;
    border-radius: 0 8px 8px 0;
    color: var(--text-secondary);
    font-style: italic;
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

    /* PDF Page Breaking Rules */
    .module-section {
        page-break-before: always; /* Each new section starts on a fresh page */
        margin-top: 0 !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
        page-break-after: avoid; /* Prevent header at the bottom of a page */
    }
    
    pre, blockquote, table, img {
        page-break-inside: avoid; /* Prevent code blocks and tables from splitting across pages */
    }
}
```

## 🧠 Javascript Logic (Copy this logic)

Use this specific logic to handle the Markdown parsing. It fixes common bugs and handling specific indented headers.

```javascript
document.addEventListener("DOMContentLoaded", () => {
    // Fetch MD logic (with local file support)
    fetch("YOUR_MARKDOWN_FILE.md")
        .then(response => {
            // Support local file:/// protocols where status is 0
            if (!response.ok && response.status !== 0) {
                throw new Error("Failed to load markdown file");
            }
            return response.text();
        })
        .then(markdown => {
    
    // 1. Pre-process Markdown (Universal Module & Topic Catcher)
    // Catch explicit headers like "# Section 1...", "### ⚛️ Module 1..."
    let processed = markdown.replace(/^#+\s*(?:.*?\s)?(Module\s+\d+|Section\s+\d+)(.*)/gim, '## MODULE_MARKER $1$2');
    
    // Catch implicitly indented modules like "  Module 1: ..."
    processed = processed.replace(/^\s*(Module\s+\d+.*)/gim, '## MODULE_MARKER $1');
    
    // Convert remaining h3 and h4 headers into properly styled Topics
    processed = processed.replace(/^#{3,4}\s+(?!MODULE_MARKER)(.*)/gm, '### TOPIC_MARKER $1');
    
    // Converts "1.1:" to bold for better readability
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
            <code class="hljs language-${language || 'plaintext'}">${highlighted}</code>
        </pre>`;
    };
    
    renderer.heading = function(text, level) {
         const safeText = text ? String(text) : '';
         let id = safeText.toLowerCase().replace(/[^\w]+/g, '-');
         let classStr = '';
         let cleanText = safeText;
         
         if (safeText.includes('MODULE_MARKER ')) {
             cleanText = safeText.replace(/MODULE_MARKER /g, '');
             id = cleanText.toLowerCase().replace(/[^\w]+/g, '-');
             classStr = ' class="module-section"';
             level = 2; // enforce level 2
         }
         else if (safeText.includes('TOPIC_MARKER ')) {
             cleanText = safeText.replace(/TOPIC_MARKER /g, '');
             id = cleanText.toLowerCase().replace(/[^\w]+/g, '-');
             classStr = ' class="topic-section"';
             level = 3; // enforce level 3
         }
         
         return `<h${level}${classStr} id="${id}">${cleanText}</h${level}>`;
    };

    // GitHub-Style Alerts (Callouts)
    renderer.blockquote = function(quote) {
        const text = quote ? String(quote) : '';
        let color = '#58a6ff'; // Default Blue (Note)
        let bg = 'rgba(88, 166, 255, 0.08)';
        let title = 'Note';
        let icon = 'fa-info-circle';
        
        let isAlert = false;
        
        if (text.includes('[!WARNING]')) { color = '#d29922'; bg = 'rgba(210, 153, 34, 0.1)'; title = 'Warning'; icon = 'fa-triangle-exclamation'; isAlert = true; }
        else if (text.includes('[!IMPORTANT]')) { color = '#8957e5'; bg = 'rgba(137, 87, 229, 0.1)'; title = 'Important'; icon = 'fa-circle-exclamation'; isAlert = true; }
        else if (text.includes('[!TIP]') || text.includes('[!SUCCESS]')) { color = '#238636'; bg = 'rgba(35, 134, 54, 0.1)'; title = 'Tip'; icon = 'fa-lightbulb'; isAlert = true; }
        else if (text.includes('[!CAUTION]') || text.includes('[!DANGER]')) { color = '#da3633'; bg = 'rgba(218, 54, 51, 0.1)'; title = 'Caution'; icon = 'fa-skull-crossbones'; isAlert = true; }
        else if (text.includes('[!NOTE]')) { isAlert = true; }
        
        if (isAlert) {
            // Strip out the tag whether it's wrapped in a <p> or standalone
            const cleanText = text.replace(/(<p>)?\s*\[!(NOTE|WARNING|IMPORTANT|TIP|SUCCESS|CAUTION|DANGER)\]\s*(<\/p>|<br>)?/i, '<p>');
            return `<div style="border-left: 4px solid ${color}; background: ${bg}; padding: 1rem 1.5rem; margin: 1.5rem 0; border-radius: 0 8px 8px 0; page-break-inside: avoid;">
                <div style="color: ${color}; font-weight: bold; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem; font-family: 'Outfit', sans-serif;">
                    <i class="fa-solid ${icon}"></i> ${title}
                </div>
                <div style="color: var(--text-secondary); margin: 0;">${cleanText}</div>
            </div>`;
        }
        
        // Default blockquote behavior
        return `<blockquote>${text}</blockquote>`;
    };

    // 3. Render
    contentArea.innerHTML = marked.parse(processed, { renderer: renderer });
        })
        .catch(err => {
            console.error(err);
            document.getElementById("loader").innerHTML = '<i class="fas fa-exclamation-triangle"></i> Error loading notes (Is CORS blocking local files?)';
        });
});
```
