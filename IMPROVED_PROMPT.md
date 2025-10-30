# Prompt — Colorful Study Notes Converter (OPTIMIZED VERSION)
## With Minified Auto-Renderer Code

**Prompt Start (copy everything below):**

You are an expert HTML/CSS document designer and note formatter.
Your task is to convert raw text notes into a visually stunning, colorful, and professional HTML study notebook.

## 🧩 A — Document Layout & Typography
- Complete HTML file with embedded `<style>` (no external CSS)
- Professional printed study notebook layout (A4 optimized)
- Body Font: Georgia, "Times New Roman", serif
- Headings Font: Arial, Helvetica, sans-serif
- Base font size: 12pt
- Margins: ~25mm all sides
- Line-height: 1.6
- Background: #fafafa

## 🎯 B — Topic Headings
Topic headings (`# Topic Name`) render as:
- Bold large blue font (#0055cc)
- Font size: 22pt
- Bottom border (3px solid blue)
- Subtle text shadow
- Proper spacing

## 🔴 C — Important Text Highlighting
Auto-highlight keywords in bright red (#d40000), bold, 1.08em:
- "important", "yaad", "dhayan", "remember", "must", "note", "Do not", "jaruri"
- "Kyun zaroori", "Best practice", "Always", "Never", "Avoid"
- "fail", "crash", "loss", "problem", "critical", "essential", "vital"
- Add light red background (rgba(212,0,0,0.05))

## 💻 D — Code Blocks
Code blocks with:
- Background: #f7f7f7
- Border: 1px solid #ddd, border-radius: 8px
- Line numbers (CSS counters)
- Syntax highlighting (keywords blue, strings green, comments gray)
- **NO horizontal scrolling** - use `white-space: pre-wrap` and `word-wrap: break-word`

## 🎨 E — Color Palette
```css
:root{--heading-blue:#0055cc;--important-red:#d40000;--code-bg:#f7f7f7;--keyword-color:#0074d9;--string-color:#2ecc40;--comment-color:#aaaaaa;--function-color:#b10dc9;--import-color:#ff851b}
```

## 🚀 M — AUTO-RENDERER SYSTEM (MINIFIED & OPTIMIZED)

**Setup Instructions:**
1. Save code below as `NotesRenderer.html`
2. Create `notes.html` with your raw notes (markdown format)
3. Open folder with Live Server (VS Code)
4. Print to PDF: Ctrl+P

**Complete Minified HTML Code:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Study Notes — Beautiful Guide</title>
<style>
:root{--heading-blue:#0055cc;--important-red:#d40000;--code-bg:#f7f7f7;--keyword-color:#0074d9;--string-color:#2ecc40;--comment-color:#aaaaaa;--function-color:#b10dc9;--import-color:#ff851b}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Georgia,"Times New Roman",serif;font-size:12pt;line-height:1.6;background:#fafafa;color:#1a1a1a;padding:25mm;max-width:210mm;margin:0 auto}
h1,h2,h3,h4,h5,h6{font-family:Arial,Helvetica,sans-serif}
.topic-heading{font-size:22pt;color:var(--heading-blue);font-weight:bold;border-bottom:3px solid var(--heading-blue);padding:15px 0 10px 0;margin:2.5em 0 .8em 0;text-shadow:1px 1px 2px rgba(0,85,204,.1)}
.separator{color:#bbb;font-family:"Courier New",monospace;margin:2.5em 0 .8em 0;font-size:10pt;letter-spacing:.5px}
h4{font-size:15pt;color:#2c5aa0;border-left:4px solid #2c5aa0;padding-left:10px;margin:1.5em 0 .8em 0}
p{margin:.6em 0;text-align:justify}
.important{color:var(--important-red);font-weight:bold;font-size:1.08em;background:rgba(212,0,0,.05);padding:2px 6px;border-radius:3px}
.code-block{background:var(--code-bg);border:1px solid #ddd;border-radius:8px;padding:15px;margin:1em 0;box-shadow:0 2px 4px rgba(0,0,0,.08);font-family:"Courier New",monospace;font-size:10pt;position:relative;counter-reset:line}
.code-block pre{margin:0;white-space:pre-wrap;word-wrap:break-word;overflow-x:visible}
.code-line{display:block;padding-left:3.5em;position:relative}
.code-line:before{counter-increment:line;content:counter(line);position:absolute;left:0;width:2.5em;text-align:right;color:#999;font-size:9pt;padding-right:1em;border-right:1px solid #ddd}
code{font-family:"Courier New",monospace;color:#c7254e;background:rgba(199,37,78,.08);padding:2px 6px;border-radius:3px;font-size:.95em}
.keyword{color:var(--keyword-color);font-weight:bold}
.string{color:var(--string-color)}
.comment{color:var(--comment-color);font-style:italic}
.function{color:var(--function-color);font-weight:bold}
.import{color:var(--import-color)}
.tag{color:#e67e22;font-weight:bold}
.attr{color:#b10dc9}
.number{color:#d63384}
.boolean{color:#0074d9;font-weight:bold}
ul,ol{margin:.6em 0 .6em 2em;line-height:1.5}
li{margin:.6em 0}
strong{font-weight:bold;color:#1a1a1a}
hr{border:none;border-top:1px solid #ddd;margin:2em 0}
@media print{body{background:white;padding:15mm}.code-block{page-break-inside:avoid;overflow:visible}.topic-heading{page-break-after:avoid}}
.separator-line{color:#bbb;font-family:"Courier New",monospace;margin:2.5em 0 .8em 0}
</style>
</head>
<body>
<header style="font-family:Arial,Helvetica,sans-serif;color:#666;font-size:10pt;margin-bottom:8px">📚 Study Notes — Auto-Rendered Beautiful UI</header>
<main id="render-target"><p style="color:#666;font-size:11pt">⏳ Loading formatted notes…</p></main>
<script>
(async function(){const target=document.getElementById("render-target");async function loadRaw(){try{const resp=await fetch("notes.html");if(!resp.ok)throw new Error("fetch failed");return await resp.text()}catch(e){return null}}
const raw=await loadRaw();if(!raw){target.innerHTML='<p style="color:#a00"><strong>❌ Error:</strong> Could not load notes.html file.</p><p style="color:#666">Make sure:</p><ul style="color:#666"><li>File named <code>notes.html</code> exists in same folder</li><li>Open with Live Server (VS Code)</li><li>Both files are in same directory</li></ul>';return}
function esc(s){return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}
const importantWords=["important","yaad rakhna","yaad","dhayan","dhyaan","remember","must","note","Do not","jaruri","Kyun zaroori","Agar na kiya","Agar","Best practice","Always","Never","Avoid","fail","crash","loss","problem","yaad rakhna chaiye","critical","essential","vital","key","crucial","CRITICAL","IMPORTANT"];
function markImportant(s){if(!s||typeof s!=="string")return s;const sentences=s.split(/(?<=[\.\?\!\n])/);for(let j=0;j<sentences.length;j++){const sent=sentences[j];const lowered=sent.toLowerCase();for(const cue of importantWords){if(!cue)continue;const cueLc=cue.toLowerCase();if(lowered.indexOf(cueLc)!==-1){sentences[j]='<span class="important">'+sent+"</span>";break}}
if(!/^<span class=\"important\">/.test(sentences[j])){let out=sentences[j];const phrases=importantWords.slice().sort((a,b)=>b.length-a.length);for(const ph of phrases){if(!ph)continue;const phEsc=ph.replace(/[-/\\^$*+?.()|[\]{}]/g,"\\$&");const re=new RegExp(phEsc,"gi");out=out.replace(re,function(m){return'<span class="important">'+m+"</span>"})}
sentences[j]=out}}
return sentences.join("")}
function highlightCode(code){const kw=['import','from','def','class','if','elif','else','for','while','return','try','except','with','as','pass','break','continue','cd','ls','mkdir','pip','python','java','django','manage','len','print','range','append','insert','remove','pop','sort','clear','split','join','strip','replace','upper','lower','get','keys','values','items','update','add'];const kwSet=new Set(kw.map(k=>k.toLowerCase()));let out='';let i=0;while(i<code.length){if(code[i]==='#'){let j=i;while(j<code.length&&code[j]!=='\n')j++;out+='<span class="comment">'+esc(code.substring(i,j))+'</span>';i=j;continue;}if(code[i]==='"'||code[i]==="'"){const q=code[i];let j=i+1;while(j<code.length&&code[j]!==q){if(code[j]==='\\')j++;j++;}if(j<code.length)j++;out+='<span class="string">'+esc(code.substring(i,j))+'</span>';i=j;continue;}if(/[a-zA-Z_]/.test(code[i])){let j=i;while(j<code.length&&/[a-zA-Z0-9_]/.test(code[j]))j++;const word=code.substring(i,j);const nextChar=j<code.length?code[j]:'';if(kwSet.has(word.toLowerCase())){out+='<span class="keyword">'+esc(word)+'</span>';}else if(nextChar==='('){out+='<span class="function">'+esc(word)+'</span>';}else if(/^(True|False|None|true|false|null)$/.test(word)){out+='<span class="boolean">'+esc(word)+'</span>';}else{out+=esc(word);}i=j;continue;}if(/\d/.test(code[i])){let j=i;while(j<code.length&&/[\d.]/.test(code[j]))j++;out+='<span class="number">'+esc(code.substring(i,j))+'</span>';i=j;continue;}out+=esc(code[i]);i++;}return out}
const lines=raw.replace(/\r/g,"").split("\n");const frag=document.createDocumentFragment();let i=0,inCode=false,codeLang="",codeBuf=[];function flushCode(){if(!inCode)return;const div=document.createElement("div");div.className="code-block";const pre=document.createElement("pre");const inner=highlightCode(codeBuf.join("\n")).split("\n").map((l)=>'<span class="code-line">'+l+"</span>").join("\n");pre.innerHTML=inner;div.appendChild(pre);frag.appendChild(div);inCode=false;codeBuf=[];codeLang=""}
while(i<lines.length){const L=lines[i];const mCode=L.match(/^```\s*(\w+)?/);if(mCode){if(!inCode){inCode=true;codeLang=mCode||"";codeBuf=[]}else{flushCode()}
i++;continue}
if(inCode){codeBuf.push(L);i++;continue}
if(/^=+\s*$/.test(L)||/^-+\s*$/.test(L)){const d=document.createElement("div");d.className="separator-line";d.textContent=L.trim();frag.appendChild(d);i++;continue}
if(/^#\s+/.test(L)){const h=document.createElement("h1");h.className="topic-heading";h.innerHTML=markImportant(esc(L.replace(/^#\s+/,"")));frag.appendChild(h);i++;continue}
if(/^##\s+/.test(L)){const h2=document.createElement("h2");h2.innerHTML=markImportant(esc(L.replace(/^##\s+/,"")));frag.appendChild(h2);i++;continue}
if(/^###\s+/.test(L)){const h3=document.createElement("h3");h3.innerHTML=markImportant(esc(L.replace(/^###\s+/,"")));frag.appendChild(h3);i++;continue}
if(/^\*\*\*\s*$/.test(L)){frag.appendChild(document.createElement("hr"));i++;continue}
if(/^\s*[-*]\s+/.test(L)){const ul=document.createElement("ul");while(i<lines.length&&/^\s*[-*]\s+/.test(lines[i])){const li=document.createElement("li");li.innerHTML=markImportant(esc(lines[i].replace(/^\s*[-*]\s+/,"")));ul.appendChild(li);i++}
frag.appendChild(ul);continue}
if(/^\s*\d+\.\s+/.test(L)){const ol=document.createElement("ol");while(i<lines.length&&/^\s*\d+\.\s+/.test(lines[i])){const li=document.createElement("li");li.innerHTML=markImportant(esc(lines[i].replace(/^\s*\d+\.\s+/,"")));ol.appendChild(li);i++}
frag.appendChild(ol);continue}
if(/^\s*$/.test(L)){i++;continue}
if(/`[^`]+`/.test(L)&&(/^(Step|Command|Task|Usage|Example|Output):/i.test(L)||L.match(/`[a-z_]+\s+[^`]*`/)||L.match(/`[^`]{20,}`/))){let parts=L.split(/(`[^`]+`)/);for(let part of parts){if(/^`[^`]+`$/.test(part)){const code=part.slice(1,-1);const div=document.createElement("div");div.className="code-block";const pre=document.createElement("pre");pre.innerHTML='<span class="code-line">'+highlightCode(code)+"</span>";div.appendChild(pre);frag.appendChild(div)}else if(part.trim()){const p=document.createElement("p");p.innerHTML=markImportant(esc(part).replace(/\*\*(.*?)\*\*/g,"<strong>$1</strong>"));frag.appendChild(p)}}i++;continue}
let phtml=esc(L);phtml=phtml.replace(/\*\*(.*?)\*\*/g,"<strong>$1</strong>");phtml=phtml.replace(/`([^`]+)`/g,"<code>$1</code>");phtml=markImportant(phtml);const p=document.createElement("p");p.innerHTML=phtml;frag.appendChild(p);i++}
flushCode();target.innerHTML="";target.appendChild(frag)})();
</script>
</body>
</html>
```

## 🎯 WORKFLOW
1. Save HTML code as `NotesRenderer.html`
2. Create `notes.html` with markdown notes:
```
# Topic Name
This is important concept.
## Subtitle
- List item 1
\`\`\`python
print("Hello")
\`\`\`
```
3. Open with Live Server
4. Print to PDF (Ctrl+P)

## ✅ Features
- Minified for performance
- Character-by-character parser (faster than regex)
- Sentence-level important highlighting
- Auto line numbers in code blocks
- PDF-ready (no horizontal scrolling)
- Live reload support
