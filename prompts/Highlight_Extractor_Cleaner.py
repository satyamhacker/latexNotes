import os
import re
import sys

SEPARATOR = '\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n'

# Regex to detect a complete, well-formed [[HL::...::HL]] pair (non-greedy, single-line)
_HL_PAIR_RE = re.compile(r'\[\[HL::.*?::HL\]\]')
# Broken table separator row: | [[HL::---::HL]] | (Rule 23)
_BROKEN_TABLE_SEP_RE = re.compile(r'\|\s*\[\[HL::(-+|:?-+:?)::HL\]\]\s*\|')


def _safe_path(path: str) -> str:
    """Resolve and return absolute path; raise ValueError if empty."""
    if not path or not path.strip():
        raise ValueError(f"Invalid path: {path!r}")
    return os.path.realpath(os.path.abspath(path.strip()))


def _is_separator_line(line: str) -> bool:
    """Return True if line is a structural separator (Rule 14).
    
    Matches: ━━━ style, === style, standalone --- horizontal rule.
    Does NOT match table separator rows like | --- | --- | (those start with |).
    """
    s = line.strip()
    if not s:
        return False
    # Must not be a table row (table rows start with |)
    if s.startswith('|'):
        return False
    return bool(re.match(r'^(━+|={3,}|-{3,})$', s))


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


def _is_closing_fence(line: str) -> bool:
    """Return True only for a pure closing fence line (``` with no language tag).
    
    Opening fences have a language identifier: ```bash, ```python, ```text.
    Closing fences are exactly ``` (optionally with surrounding whitespace).
    This prevents premature closure on nested opening fences (Issue 3).
    """
    return bool(re.match(r'^\s*```\s*$', line))


def _process_code_block(lines: list, i: int, extracted: list,
                        last_idx_ref: list):
    """Collect a fenced code block; commit if it contains a highlight.
    
    The opening fence line (```lang) is NEVER checked for [[HL:: tags —
    fence lines must never be highlighted (Rule 12).
    Uses _is_closing_fence() to avoid premature closure on nested opening fences.
    """
    fence_line = lines[i]
    current = [fence_line]
    has_hl = False          # intentionally NOT checking the fence line itself
    j = i + 1
    while j < len(lines):
        line = lines[j]
        current.append(line)
        # Only a pure closing fence (```) ends the block — not ```python etc.
        if _is_closing_fence(line):
            if has_hl:
                _commit_block(current, i, j, extracted, last_idx_ref)
            return j + 1
        if "[[HL::" in line:
            has_hl = True
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


def _skip_yaml_frontmatter(lines: list) -> int:
    """If file starts with YAML frontmatter (---), return index after closing ---.
    
    Rule 10: YAML frontmatter is completely off-limits.
    Returns 0 if no frontmatter found.
    """
    if not lines:
        return 0
    if lines[0].strip() != '---':
        return 0
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            return i + 1
    return 0  # Unclosed frontmatter — treat whole file as content


def _heal_broken_table_separators(lines: list) -> tuple:
    """Detect and heal broken table separator rows like | [[HL::---::HL]] |.
    
    Rule 23: table separator rows must NEVER contain [[HL:: tags.
    Returns (healed_lines, count_of_healed_rows).
    """
    healed = []
    count = 0
    for line in lines:
        if _BROKEN_TABLE_SEP_RE.search(line):
            # Strip all [[HL:: / ::HL]] tags from this separator row entirely
            fixed = re.sub(r'\[\[HL::(.*?)::HL\]\]', r'\1', line)
            healed.append(fixed)
            count += 1
        else:
            healed.append(line)
    return healed, count


def _clean_lines(raw: list) -> list:
    """Strip [[HL:: / ::HL]] tags and collapse consecutive blank lines.
    
    Uses regex to remove only COMPLETE well-formed pairs (single-line).
    Multi-line orphan tags (open on one line, close on another) are left as-is
    and will be caught by the post-flight tag balance check.
    Also strips SEPARATOR lines (━━━) from the output (Rule 14).
    """
    result = []
    prev_empty = False
    for line in raw:
        # Strip the separator marker lines from extracted output
        if _is_separator_line(line):
            continue
        # Remove complete [[HL::...::HL]] pairs only (non-greedy, single-line)
        cleaned = re.sub(r'\[\[HL::(.*?)::HL\]\]', r'\1', line)
        is_empty = cleaned.strip() == ''
        if is_empty and prev_empty:
            continue
        result.append(cleaned)
        prev_empty = is_empty
    return result


def _verify_tag_balance(lines: list) -> tuple:
    """Count [[HL:: opens and ::HL]] closes across all lines.
    
    Returns (opens, closes, is_balanced).
    Rule 33: opens must equal closes exactly.
    """
    opens = sum(line.count("[[HL::") for line in lines)
    closes = sum(line.count("::HL]]") for line in lines)
    return opens, closes, opens == closes


def extract_and_clean_highlights(input_file: str, output_file: str) -> None:
    input_path = _safe_path(input_file)
    output_path = _safe_path(output_file)

    print(f"Reading file: {input_path}")
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # ── PRE-FLIGHT: Tag balance check on INPUT (Rule 33 / Post-flight check) ──
    in_opens, in_closes, in_balanced = _verify_tag_balance(lines)
    if not in_balanced:
        print(f"⚠️  WARNING: Input file has UNBALANCED tags!")
        print(f"   [[HL:: opens : {in_opens}")
        print(f"   ::HL]] closes: {in_closes}")
        print(f"   Difference   : {abs(in_opens - in_closes)} orphan tag(s)")
        print(f"   Proceeding with extraction — orphan tags will be preserved as-is.")

    extracted: list = []
    last_idx_ref = [-1]   # mutable reference so helpers can update it

    # ── Skip YAML frontmatter (Rule 10) ──────────────────────────────────────
    start_i = _skip_yaml_frontmatter(lines)
    if start_i > 0:
        print(f"ℹ️  YAML frontmatter detected — skipping lines 0–{start_i - 1} (Rule 10)")

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
    hl_balance = 0          # tracks open [[HL:: tags not yet closed
    i = start_i

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        has_hl = "[[HL::" in line

        # ── Separator lines: skip entirely (Rule 14) ─────────────────────────
        if _is_separator_line(stripped):
            # Flush any open context blocks before skipping
            if in_table:
                _flush_context_block(table_buf, table_start, i - 1,
                                     table_has_hl, extracted, last_idx_ref)
                in_table = False; table_buf = []; table_has_hl = False
            if in_quote:
                _flush_context_block(quote_buf, quote_start, i - 1,
                                     quote_has_hl, extracted, last_idx_ref)
                in_quote = False; quote_buf = []; quote_has_hl = False
            i += 1
            continue

        # ── Code blocks ──────────────────────────────────────────────────────
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
            # Stray closing fence outside a tracked block — skip
            i += 1
            continue

        # ── Tables ───────────────────────────────────────────────────────────
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

        # ── Blockquotes ──────────────────────────────────────────────────────
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

        # ── Prose / bullets (multi-line highlight balance) ───────────────────
        opens = line.count("[[HL::")
        closes = line.count("::HL]]")

        if hl_balance > 0 or opens > 0 or closes > 0:
            # Only inject separator BEFORE a NEW highlight starts (hl_balance==0)
            # Never inject separator mid-highlight (hl_balance>0) — Rule 31
            if hl_balance == 0 and last_idx_ref[0] != -1 and i > last_idx_ref[0] + 1:
                extracted.append(SEPARATOR)
            extracted.append(line)
            last_idx_ref[0] = i

        hl_balance += (opens - closes)
        if hl_balance < 0:
            hl_balance = 0   # guard against malformed closes
        i += 1

    # ── EOF flush of any still-open context blocks ────────────────────────────
    if in_table and table_has_hl:
        _flush_context_block(table_buf, table_start, len(lines) - 1,
                             True, extracted, last_idx_ref)
    if in_quote and quote_has_hl:
        _flush_context_block(quote_buf, quote_start, len(lines) - 1,
                             True, extracted, last_idx_ref)

    # ── EOF: warn if hl_balance is still non-zero (unclosed tag in prose) ────
    if hl_balance != 0:
        print(f"⚠️  WARNING: {hl_balance} unclosed [[HL:: tag(s) detected in prose at EOF!")
        print(f"   The extracted output may contain orphan opening tags.")

    # ── POST-FLIGHT: Heal broken table separator rows (Rule 23) ─────────────
    extracted, healed_count = _heal_broken_table_separators(extracted)
    if healed_count > 0:
        print(f"⚠️  POST-FLIGHT: Healed {healed_count} broken table separator row(s) (Rule 23).")

    # ── POST-FLIGHT: Tag balance check on EXTRACTED lines (Rule 33) ──────────
    ext_opens, ext_closes, ext_balanced = _verify_tag_balance(extracted)
    if not ext_balanced:
        print(f"⚠️  POST-FLIGHT WARNING: Extracted output has UNBALANCED tags!")
        print(f"   [[HL:: opens : {ext_opens}")
        print(f"   ::HL]] closes: {ext_closes}")
    else:
        print(f"✅ Tag balance verified: {ext_opens} [[HL:: / {ext_closes} ::HL]] — balanced.")

    final = _clean_lines(extracted)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(final)

    # ── Coverage summary (Rule 48 spirit) ────────────────────────────────────
    # Use single-line _HL_PAIR_RE (no DOTALL) — correct for line-by-line counting
    hl_count = sum(len(_HL_PAIR_RE.findall(line)) for line in extracted)
    print(f"\n📊 Extraction Summary:")
    print(f"   Total input lines      : {len(lines)}")
    print(f"   Total extracted lines  : {len(final)}")
    print(f"   [[HL::...::HL]] pairs  : {hl_count}")
    print(f"   Tag balance (input)    : {'✅ OK' if in_balanced else '❌ UNBALANCED'}")
    print(f"   Tag balance (extracted): {'✅ OK' if ext_balanced else '❌ UNBALANCED'}")
    print(f"\nSaved to: {output_path}")


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
