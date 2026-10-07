import os
import sys

SEPARATOR = '\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n'


def _safe_path(path: str) -> str:
    """Resolve and return absolute path; raise ValueError if empty."""
    if not path or not path.strip():
        raise ValueError(f"Invalid path: {path!r}")
    return os.path.realpath(os.path.abspath(path.strip()))


def _commit_block(block_lines: list, start_idx: int, end_idx: int,
                  extracted: list, last_idx_ref: list) -> None:
    """Append a highlighted block (with separator if needed) to extracted."""
    if not block_lines:
        return
    last = last_idx_ref[0]
    if last != -1 and start_idx > last + 1:
        extracted.append(SEPARATOR)
    extracted.extend(block_lines)
    extracted.append('\n')
    last_idx_ref[0] = end_idx


def _process_code_block(lines: list, i: int, extracted: list,
                        last_idx_ref: list):
    """Collect a fenced code block; commit if it contains a highlight."""
    current = [lines[i]]
    has_hl = "[[HL::" in lines[i]
    j = i + 1
    while j < len(lines):
        line = lines[j]
        current.append(line)
        if "[[HL::" in line:
            has_hl = True
        if line.strip().startswith("```"):
            if has_hl:
                _commit_block(current, i, j, extracted, last_idx_ref)
            return j + 1
        j += 1
    # EOF without closing fence — commit if highlighted
    if has_hl:
        _commit_block(current, i, j - 1, extracted, last_idx_ref)
    return j


def _flush_context_block(block: list, start_i: int, end_i: int,
                         has_hl: bool, extracted: list,
                         last_idx_ref: list) -> None:
    """Commit a table or blockquote block if it contained a highlight."""
    if has_hl:
        _commit_block(block, start_i, end_i, extracted, last_idx_ref)


def _clean_lines(raw: list) -> list:
    """Strip [[HL:: / ::HL]] tags and collapse consecutive blank lines."""
    result = []
    prev_empty = False
    for line in raw:
        is_empty = line.strip() == ''
        if is_empty and prev_empty:
            continue
        result.append(line.replace("[[HL::", "").replace("::HL]]", ""))
        prev_empty = is_empty
    return result


def extract_and_clean_highlights(input_file: str, output_file: str) -> None:
    input_path = _safe_path(input_file)
    output_path = _safe_path(output_file)

    print(f"Reading file: {input_path}")
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    extracted: list = []
    last_idx_ref = [-1]   # mutable reference so helpers can update it

    # Context state
    in_code = False
    in_table = False
    table_buf: list = []
    table_start = 0
    table_has_hl = False
    in_quote = False
    quote_buf: list = []
    quote_start = 0
    quote_has_hl = False
    hl_balance = 0
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        has_hl = "[[HL::" in line

        # ── Code blocks ──────────────────────────────────────────────────
        if stripped.startswith("```"):
            # Flush any open table/quote first
            if in_table:
                _flush_context_block(table_buf, table_start, i - 1,
                                     table_has_hl, extracted, last_idx_ref)
                in_table = False; table_buf = []; table_has_hl = False
            if in_quote:
                _flush_context_block(quote_buf, quote_start, i - 1,
                                     quote_has_hl, extracted, last_idx_ref)
                in_quote = False; quote_buf = []; quote_has_hl = False

            if not in_code:
                in_code = True
                i = _process_code_block(lines, i, extracted, last_idx_ref)
                in_code = False
                continue
            # Shouldn't reach here normally
            i += 1
            continue

        # ── Tables ───────────────────────────────────────────────────────
        if stripped.startswith('|'):
            if in_quote:
                _flush_context_block(quote_buf, quote_start, i - 1,
                                     quote_has_hl, extracted, last_idx_ref)
                in_quote = False; quote_buf = []; quote_has_hl = False
            if not in_table:
                in_table = True; table_buf = [line]
                table_start = i; table_has_hl = has_hl
            else:
                table_buf.append(line)
                table_has_hl = table_has_hl or has_hl
            i += 1
            continue
        else:
            if in_table:
                _flush_context_block(table_buf, table_start, i - 1,
                                     table_has_hl, extracted, last_idx_ref)
                in_table = False; table_buf = []; table_has_hl = False

        # ── Blockquotes ──────────────────────────────────────────────────
        if stripped.startswith('>'):
            if not in_quote:
                in_quote = True; quote_buf = [line]
                quote_start = i; quote_has_hl = has_hl
            else:
                quote_buf.append(line)
                quote_has_hl = quote_has_hl or has_hl
            i += 1
            continue
        else:
            if in_quote:
                _flush_context_block(quote_buf, quote_start, i - 1,
                                     quote_has_hl, extracted, last_idx_ref)
                in_quote = False; quote_buf = []; quote_has_hl = False

        # ── Prose / bullets (multi-line highlight balance) ───────────────
        opens = line.count("[[HL::")
        closes = line.count("::HL]]")
        if hl_balance > 0 or opens > 0 or closes > 0:
            if hl_balance == 0 and last_idx_ref[0] != -1 and i > last_idx_ref[0] + 1:
                extracted.append(SEPARATOR)
            extracted.append(line)
            last_idx_ref[0] = i
        hl_balance += (opens - closes)
        if hl_balance < 0:
            hl_balance = 0
        i += 1

    # EOF flush
    if in_table and table_has_hl:
        _flush_context_block(table_buf, table_start, len(lines) - 1,
                             True, extracted, last_idx_ref)
    if in_quote and quote_has_hl:
        _flush_context_block(quote_buf, quote_start, len(lines) - 1,
                             True, extracted, last_idx_ref)

    final = _clean_lines(extracted)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(final)

    print(f"Done! Extracted lines: {len(final)}")
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    # Usage: python Highlight_Extractor_Cleaner.py [input_path] [output_path]
    # Falls back to hardcoded defaults if no args given.
    if len(sys.argv) == 3:
        inp = sys.argv[1]
        out = sys.argv[2]
    else:
        # 👇 Change these defaults as needed
        inp = r"e:\latexNotes\Code_with_harry_data_analytis_course\Code_with_harry_data_analytis_course_notes.md"
        out = r"e:\latexNotes\Code_with_harry_data_analytis_course\Code_with_harry_data_analytis_course_notes_Highlights.md"

    try:
        inp_safe = _safe_path(inp)
        out_safe = _safe_path(out)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    if not os.path.exists(inp_safe):
        print(f"Error: Input file not found — '{inp_safe}'")
        sys.exit(1)

    extract_and_clean_highlights(inp_safe, out_safe)
