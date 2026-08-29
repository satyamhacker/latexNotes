import os

def extract_and_clean_highlights(input_file, output_file):
    print(f"Reading file: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    extracted_content = []
    
    # State tracking variables for context awareness
    inside_code_block = False
    current_code_block = []
    has_highlight_in_code = False
    
    inside_table = False
    current_table = []
    has_highlight_in_table = False
    
    inside_blockquote = False
    current_blockquote = []
    has_highlight_in_blockquote = False
    
    hl_balance = 0
    last_extracted_index = -1
    
    # Ye separator hum har naye extraction block ke beech daalenge
    separator = '\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n'
    
    def commit_block(block_lines, start_idx, end_idx):
        nonlocal last_extracted_index
        if last_extracted_index != -1 and start_idx > last_extracted_index + 1:
            extracted_content.append(separator)
        extracted_content.extend(block_lines)
        extracted_content.append('\n')
        last_extracted_index = end_idx

    for i, line in enumerate(lines):
        is_table_line = line.strip().startswith('|')
        is_blockquote_line = line.strip().startswith('>')
        is_code_fence = line.strip().startswith("```")
        has_hl = "[[HL::" in line
        
        # 1. Handle Code Blocks (` ``` `)
        if is_code_fence:
            if not inside_code_block:
                inside_code_block = True
                current_code_block = [line]
                has_highlight_in_code = has_hl
            else:
                current_code_block.append(line)
                has_highlight_in_code = has_highlight_in_code or has_hl
                
                if has_highlight_in_code:
                    start_idx = i - len(current_code_block) + 1
                    commit_block(current_code_block, start_idx, i)
                
                inside_code_block = False
                current_code_block = []
                has_highlight_in_code = False
            continue
            
        if inside_code_block:
            current_code_block.append(line)
            has_highlight_in_code = has_highlight_in_code or has_hl
            continue

        # 2. Handle Tables
        if is_table_line:
            if not inside_table:
                inside_table = True
                current_table = [line]
                has_highlight_in_table = has_hl
            else:
                current_table.append(line)
                has_highlight_in_table = has_highlight_in_table or has_hl
            continue
        else:
            if inside_table:
                if has_highlight_in_table:
                    start_idx = i - len(current_table)
                    commit_block(current_table, start_idx, i - 1)
                inside_table = False
                current_table = []
                has_highlight_in_table = False

        # 3. Handle Blockquotes
        if is_blockquote_line:
            if not inside_blockquote:
                inside_blockquote = True
                current_blockquote = [line]
                has_highlight_in_blockquote = has_hl
            else:
                current_blockquote.append(line)
                has_highlight_in_blockquote = has_highlight_in_blockquote or has_hl
            continue
        else:
            if inside_blockquote:
                if has_highlight_in_blockquote:
                    start_idx = i - len(current_blockquote)
                    commit_block(current_blockquote, start_idx, i - 1)
                inside_blockquote = False
                current_blockquote = []
                has_highlight_in_blockquote = False

        # 4. Handle Prose, Bullets and Multi-line highlights
        opens = line.count("[[HL::")
        closes = line.count("::HL]]")
        
        if hl_balance > 0 or opens > 0 or closes > 0:
            if hl_balance == 0 and last_extracted_index != -1 and i > last_extracted_index + 1:
                extracted_content.append(separator)
                
            extracted_content.append(line)
            last_extracted_index = i
            
        hl_balance += (opens - closes)
        if hl_balance < 0:
            hl_balance = 0

    # Catch remaining blocks at EOF
    if inside_table and has_highlight_in_table:
        commit_block(current_table, len(lines) - len(current_table), len(lines) - 1)
    if inside_blockquote and has_highlight_in_blockquote:
        commit_block(current_blockquote, len(lines) - len(current_blockquote), len(lines) - 1)

    # Clean up empty lines AND remove the [[HL:: tags
    final_content = []
    prev_empty = False
    for line in extracted_content:
        is_empty = (line.strip() == '')
        if is_empty and prev_empty:
            continue
        
        cleaned_line = line.replace("[[HL::", "").replace("::HL]]", "")
        final_content.append(cleaned_line)
        
        prev_empty = is_empty

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(final_content)
        
    print(f"Extraction and cleanup successful! Total extracted lines: {len(final_content)}")
    print(f"File saved to: {output_file}")

if __name__ == "__main__":
    # 👇 Yaha par aap apne input aur output files ka path change kar sakte hain 👇
    input_path = r"e:\latexNotes\Code_with_harry_data_analytis_course\Code_with_harry_data_analytis_course_notes.md"
    output_path = r"e:\latexNotes\Code_with_harry_data_analytis_course\Code_with_harry_data_analytis_course_notes_Highlights.md"
    
    if os.path.exists(input_path):
        extract_and_clean_highlights(input_path, output_path)
    else:
        print(f"Error: Input file '{input_path}' nahi mili.")
