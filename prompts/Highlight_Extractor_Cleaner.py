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
    hl_balance = 0
    last_extracted_index = -1
    
    # Ye separator hum har naye extraction block ke beech daalenge
    separator = '\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n'
    
    for i, line in enumerate(lines):
        # 1. Handle Code Blocks (` ``` `)
        if line.strip().startswith("```"):
            if not inside_code_block:
                # Entering a code block
                inside_code_block = True
                current_code_block = [line]
                has_highlight_in_code = False
                if "[[HL::" in line:
                    has_highlight_in_code = True
            else:
                # Exiting a code block
                current_code_block.append(line)
                if "[[HL::" in line:
                    has_highlight_in_code = True
                    
                # If there was a highlight anywhere in the block, keep the whole block
                if has_highlight_in_code:
                    # Agar humne original file me kuch un-highlighted lines skip ki thi, toh gap+separator de do
                    block_start_index = i - len(current_code_block) + 1
                    if last_extracted_index != -1 and block_start_index > last_extracted_index + 1:
                        extracted_content.append(separator)
                        
                    extracted_content.extend(current_code_block)
                    extracted_content.append('\n') # Space after block
                    last_extracted_index = i
                
                # Reset state
                inside_code_block = False
                current_code_block = []
                has_highlight_in_code = False
            continue
            
        if inside_code_block:
            current_code_block.append(line)
            if "[[HL::" in line:
                has_highlight_in_code = True
            continue

        # 2. Handle Prose, Bullets and Multi-line highlights
        opens = line.count("[[HL::")
        closes = line.count("::HL]]")
        
        # If we are currently inside a multi-line highlight, OR the current line has a highlight tag
        if hl_balance > 0 or opens > 0 or closes > 0:
            # Agar balance 0 tha (yani naya highlight shuru hua hai) aur humne lines skip ki hain original file mein
            if hl_balance == 0 and last_extracted_index != -1 and i > last_extracted_index + 1:
                extracted_content.append(separator) # Naye extract se pehle separator
                
            extracted_content.append(line)
            last_extracted_index = i
            
        hl_balance += (opens - closes)
        
        # Safety net for formatting quirks
        if hl_balance < 0:
            hl_balance = 0

    # 3. Clean up empty lines AND remove the [[HL:: tags
    final_content = []
    prev_empty = False
    for line in extracted_content:
        is_empty = (line.strip() == '')
        if is_empty and prev_empty:
            continue
        
        # Remove the tags completely from the output
        cleaned_line = line.replace("[[HL::", "").replace("::HL]]", "")
        final_content.append(cleaned_line)
        
        prev_empty = is_empty

    # 4. Save to output file
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
