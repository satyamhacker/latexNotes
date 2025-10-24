import re

def format_notes_to_html(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    html_content = []
    html_content.append('<!DOCTYPE html>')
    html_content.append('<html lang="en">')
    html_content.append('<head>')
    html_content.append('<meta charset="UTF-8">')
    html_content.append('<link rel="stylesheet" href="styles.css">')
    html_content.append('<title>Android Development with Java - Study Notes</title>')
    html_content.append('</head>')
    html_content.append('<body>')
    
    lines = content.split('\n')
    in_code_block = False
    code_lang = ''
    code_lines = []
    
    for line in lines:
        line = line.rstrip()
        
        # Code blocks
        if line.startswith('```'):
            if not in_code_block:
                in_code_block = True
                code_lang = line[3:].strip()
                code_lines = []
            else:
                in_code_block = False
                html_content.append('<div class="code-block"><pre>')
                for code_line in code_lines:
                    formatted = highlight_code(code_line, code_lang)
                    html_content.append(f'<span class="code-line">{formatted}</span>')
                html_content.append('</pre></div>')
            continue
        
        if in_code_block:
            code_lines.append(line)
            continue
        
        # Separators
        if line.startswith('==='):
            html_content.append(f'<div class="separator">{line}</div>')
            continue
        
        # Topic headings (# Title)
        if line.startswith('# ') and not line.startswith('## '):
            title = line[2:].strip()
            html_content.append(f'<h1 class="topic-heading">{title}</h1>')
            continue
        
        # Subheadings (## Title)
        if line.startswith('## '):
            title = line[3:].strip()
            html_content.append(f'<h4>{title}</h4>')
            continue
        
        # Horizontal rules
        if line == '***' or line == '---':
            html_content.append('<hr>')
            continue
        
        # Lists
        if line.startswith('- '):
            if not html_content or not html_content[-1].startswith('<ul>'):
                html_content.append('<ul>')
            item = line[2:].strip()
            item = highlight_important(item)
            item = highlight_inline_code(item)
            html_content.append(f'<li>{item}</li>')
            continue
        elif html_content and html_content[-1].startswith('<li>'):
            if not line.startswith('- '):
                html_content.append('</ul>')
        
        # Empty lines
        if not line.strip():
            continue
        
        # Regular paragraphs
        line = highlight_important(line)
        line = highlight_inline_code(line)
        html_content.append(f'<p>{line}</p>')
    
    html_content.append('</body>')
    html_content.append('</html>')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_content))

def highlight_important(text):
    keywords = [
        'important', 'yaad', 'dhayan', 'remember', 'must', 'note', 'Do not', 'jaruri',
        'Kyun zaroori', 'Best practice', 'Always', 'Never', 'Avoid', 'zaroori',
        'fail', 'crash', 'loss', 'problem', 'error', 'mandatory', 'required'
    ]
    
    for keyword in keywords:
        pattern = re.compile(f'({re.escape(keyword)})', re.IGNORECASE)
        text = pattern.sub(r'<span class="important">\1</span>', text)
    
    return text

def highlight_inline_code(text):
    return re.sub(r'`([^`]+)`', r'<code>\1</code>', text)

def highlight_code(line, lang):
    if not line.strip():
        return ''
    
    # Comments
    if line.strip().startswith('#') or line.strip().startswith('//'):
        return f'<span class="comment">{line}</span>'
    
    # Keywords
    keywords = ['public', 'private', 'protected', 'class', 'void', 'int', 'String', 'return', 
                'if', 'else', 'for', 'while', 'new', 'static', 'final', 'extends', 'implements',
                'cd', 'mkdir', 'chmod', 'sudo']
    
    for kw in keywords:
        line = re.sub(rf'\b({kw})\b', r'<span class="keyword">\1</span>', line)
    
    # Strings
    line = re.sub(r'"([^"]*)"', r'<span class="string">"\1"</span>', line)
    line = re.sub(r"'([^']*)'", r"<span class='string'>'\1'</span>", line)
    
    return line

if __name__ == '__main__':
    format_notes_to_html('AndroidDevelopmentJava.html', 'AndroidDevelopmentJava_final.html')
    print('Formatting complete!')
