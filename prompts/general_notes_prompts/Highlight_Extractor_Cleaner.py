#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Highlight_Extractor_Cleaner.py — Production-Grade Highlight Extraction & Hierarchy Engine
Extracts highlighted concepts ([[HL::...::HL]]) from massive Markdown course notes,
preserving headings, code blocks, tables, and structural hierarchy with 100% integrity.
"""

import os
import re
import sys
import argparse

# ── Force UTF-8 on Windows Consoles (Prevents UnicodeEncodeError on emojis/arrows) ──
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

_HL_PAIR_RE = re.compile(r'\[\[HL::.*?::HL\]\]')


def _safe_path(path: str) -> str:
    """Resolve and return absolute path; raise ValueError if empty."""
    if not path or not path.strip():
        raise ValueError(f"Invalid path: {path!r}")
    return os.path.realpath(os.path.abspath(path.strip()))


def _is_table_separator_row(line: str) -> bool:
    """Return True if line is a Markdown table separator row like |---|---|."""
    stripped_tags = line.replace("[[HL::", "").replace("::HL]]", "").strip()
    if not stripped_tags.startswith('|') or '-' not in stripped_tags:
        return False
    return bool(re.match(r'^\|[\s|:-]+\|?\s*$', stripped_tags))


def _normalize_table_row(line: str) -> str:
    """Normalize a table row so highlight tags are strictly inside cells (Rule 13/44)."""
    m = re.match(r'^(\s*)\[\[HL::\s*(\|.*?\|)\s*::HL\]\]\s*$', line)
    if not m:
        return line
    indent = m.group(1)
    row_inner = m.group(2)
    parts = row_inner.split('|')
    if len(parts) < 4:
        return line
    new_parts = [parts[0]]
    for cell in parts[1:-1]:
        clean = cell.strip()
        if not clean:
            new_parts.append(cell)
        elif clean.startswith('[[HL::') and clean.endswith('::HL]]'):
            new_parts.append(f' {clean} ')
        else:
            new_parts.append(f' [[HL::{clean}::HL]] ')
    new_parts.append(parts[-1])
    return indent + '|'.join(new_parts)


def _is_fence(line: str) -> tuple:
    """Check if line is a code fence. Returns (is_fence, is_closing, fence_chars, lang)."""
    m = re.match(r'^(\s*)(`{3,}|~{3,})(\w*.*)?$', line)
    if not m:
        return False, False, '', ''
    indent, fence, rest = m.groups()
    lang = (rest or '').strip()
    is_closing = len(lang) == 0
    return True, is_closing, fence, lang


def _verify_tag_balance(lines: list) -> tuple:
    """Count [[HL:: opens and ::HL]] closes. Returns (opens, closes, is_balanced)."""
    opens = sum(line.count("[[HL::") for line in lines)
    closes = sum(line.count("::HL]]") for line in lines)
    return opens, closes, opens == closes


def _skip_yaml_frontmatter(lines: list) -> int:
    """Skip YAML frontmatter if present (Rule 10)."""
    if not lines or lines[0].strip() != '---':
        return 0
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            return i + 1
    return 0


DEFAULT_SEPARATOR = '\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n'


def extract_highlights(input_file: str, output_file: str = None,
                       keep_highlights: bool = True,
                       include_headings: bool = True,
                       clean_output_file: str = None,
                       separator: str = DEFAULT_SEPARATOR,
                       no_separator: bool = False) -> None:
    """
    Extracts highlighted blocks and preserves structural context.
    - keep_highlights: If True, preserves [[HL::...::HL]] markers for the HTML viewer.
    - include_headings: If True, retains parent Module & Topic headers for context.
    - clean_output_file: Optional second output file with all highlight tags stripped.
    - separator: Separator string inserted between disjoint highlight blocks (Rule 14/31).
    - no_separator: If True, disables separator insertion.
    """
    input_path = _safe_path(input_file)
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if not output_file:
        base, ext = os.path.splitext(input_path)
        output_file = f"{base}_Highlights{ext}"
    output_path = _safe_path(output_file)

    print(f"📖 Reading Source Notes: {input_path}")
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Pre-flight tag check
    in_opens, in_closes, in_balanced = _verify_tag_balance(lines)
    status_icon = "✅ Balanced" if in_balanced else f"⚠️ UNBALANCED (Diff: {abs(in_opens - in_closes)})"
    print(f"📊 Pre-Flight Parity Audit: {in_opens} [[HL:: opens / {in_closes} ::HL]] closes [{status_icon}]")

    start_i = _skip_yaml_frontmatter(lines)
    if start_i > 0:
        print(f"ℹ️  YAML frontmatter skipped (lines 0–{start_i - 1})")

    # Hierarchy tracking
    current_h1 = None
    current_h2 = None
    current_h3 = None
    current_h4 = None

    emitted_h1 = None
    emitted_h2 = None
    emitted_h3 = None
    emitted_h4 = None

    extracted = []
    in_code = False
    code_fence = ''
    code_buf = []
    code_has_hl = False

    hl_balance = 0
    last_idx = -1
    heading_just_emitted = False
    sep_str = separator if (separator and not no_separator) else ""

    def emit_headings():
        nonlocal emitted_h1, emitted_h2, emitted_h3, emitted_h4, heading_just_emitted
        needed = False
        if current_h1 and current_h1 != emitted_h1:
            needed = True
        elif current_h2 and current_h2 != emitted_h2:
            needed = True
        elif current_h3 and current_h3 != emitted_h3:
            needed = True
        elif current_h4 and current_h4 != emitted_h4:
            needed = True

        if needed:
            if current_h1 and current_h1 != emitted_h1:
                extracted.append(f"\n# {current_h1}\n\n")
                emitted_h1 = current_h1
                emitted_h2 = None
                emitted_h3 = None
                emitted_h4 = None
            if current_h2 and current_h2 != emitted_h2:
                extracted.append(f"\n## {current_h2}\n\n")
                emitted_h2 = current_h2
                emitted_h3 = None
                emitted_h4 = None
            if current_h3 and current_h3 != emitted_h3:
                extracted.append(f"\n### {current_h3}\n\n")
                emitted_h3 = current_h3
                emitted_h4 = None
            if current_h4 and current_h4 != emitted_h4:
                extracted.append(f"\n#### {current_h4}\n\n")
                emitted_h4 = current_h4
            heading_just_emitted = True

    i = start_i
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Track headings for context
        clean_heading = re.sub(r'\[\[HL::(.*?)\]\]', r'\1', stripped).replace('[[HL::', '').replace('::HL]]', '')
        if clean_heading.startswith('# '):
            current_h1 = clean_heading[2:].strip()
            current_h2 = None
            current_h3 = None
            current_h4 = None
            i += 1
            continue
        elif clean_heading.startswith('## '):
            current_h2 = clean_heading[3:].strip()
            current_h3 = None
            current_h4 = None
            i += 1
            continue
        elif clean_heading.startswith('### '):
            current_h3 = clean_heading[4:].strip()
            current_h4 = None
            i += 1
            continue
        elif clean_heading.startswith('#### '):
            current_h4 = clean_heading[5:].strip()
            i += 1
            continue

        # ── Code Blocks (Rule 12/40) ─────────────────────────────────────────
        is_fn, is_cl, fn_str, lang = _is_fence(line)
        if is_fn and not in_code:
            in_code = True
            code_fence = fn_str
            code_buf = [line]
            code_has_hl = False
            j = i + 1
            while j < len(lines):
                c_line = lines[j]
                c_fn, c_cl, c_str, _ = _is_fence(c_line)
                code_buf.append(c_line)
                if "[[HL::" in c_line:
                    code_has_hl = True
                if c_fn and c_cl and c_str == code_fence:
                    break
                j += 1
            
            if code_has_hl:
                emit_headings()
                if sep_str and last_idx != -1 and i > last_idx + 1 and not heading_just_emitted:
                    extracted.append(sep_str)
                extracted.extend(code_buf)
                extracted.append('\n')
                last_idx = j
                heading_just_emitted = False
            
            in_code = False
            code_buf = []
            i = j + 1
            continue

        # ── Tables (Rule 13/23/44) ───────────────────────────────────────────
        is_tbl = stripped.startswith('|') or re.match(r'^(\s*)\[\[HL::\s*\|', line)
        if is_tbl:
            table_buf = []
            table_has_hl = False
            j = i
            while j < len(lines):
                t_line = lines[j]
                t_str = t_line.strip()
                if not (t_str.startswith('|') or re.match(r'^(\s*)\[\[HL::\s*\|', t_line)):
                    break
                norm_line = _normalize_table_row(t_line)
                table_buf.append(norm_line)
                if "[[HL::" in norm_line:
                    table_has_hl = True
                j += 1
            
            if table_has_hl:
                emit_headings()
                if sep_str and last_idx != -1 and i > last_idx + 1 and not heading_just_emitted:
                    extracted.append(sep_str)
                extracted.extend(table_buf)
                extracted.append('\n')
                last_idx = j - 1
                heading_just_emitted = False
            
            table_buf = []
            i = j
            continue

        # ── Prose, Blockquotes, Lists ────────────────────────────────────────
        has_hl = "[[HL::" in line or "::HL]]" in line or hl_balance > 0
        opens = line.count("[[HL::")
        closes = line.count("::HL]]")

        if has_hl:
            emit_headings()
            # If start of a new highlight and gap exists
            if sep_str and hl_balance == 0 and last_idx != -1 and i > last_idx + 1 and not heading_just_emitted:
                extracted.append(sep_str)
            extracted.append(line)
            last_idx = i
            heading_just_emitted = False

        hl_balance += (opens - closes)
        if hl_balance < 0:
            hl_balance = 0
        i += 1

    # Format extracted lines
    final_lines = []
    prev_empty = False
    for chunk in extracted:
        for l in chunk.splitlines(keepends=True):
            if not keep_highlights:
                l = re.sub(r'\[\[HL::(.*?)::HL\]\]', r'\1', l).replace("[[HL::", "").replace("::HL]]", "")
            is_empty = l.strip() == ''
            if is_empty and prev_empty:
                continue
            final_lines.append(l)
            prev_empty = is_empty

    # Post-flight integrity checks
    out_opens, out_closes, out_balanced = _verify_tag_balance(final_lines)
    print(f"\n📊 Post-Flight Parity Audit: {out_opens} [[HL:: opens / {out_closes} ::HL]] closes {'(Balanced ✅)' if out_balanced else '(Unbalanced ⚠️)'}")

    # Check for broken table rows (at least 2 columns with pipes)
    broken_tbls = [l for l in final_lines if re.match(r'^\s*\[\[HL::\s*\|.*?\|.*?\|', l)]
    if broken_tbls:
        print(f"⚠️  WARNING: Found {len(broken_tbls)} broken table rows in output!")
    else:
        print("✅ Table Integrity: 0 broken table rows.")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(final_lines)
    print(f"🚀 SUCCESS: Highlighted Summary written to: {output_path}")

    # Optionally write clean version
    if clean_output_file:
        clean_path = _safe_path(clean_output_file)
        clean_lines = []
        for l in final_lines:
            cl = re.sub(r'\[\[HL::(.*?)::HL\]\]', r'\1', l).replace("[[HL::", "").replace("::HL]]", "")
            clean_lines.append(cl)
        with open(clean_path, 'w', encoding='utf-8') as f:
            f.writelines(clean_lines)
        print(f"🧹 Clean Version (Tags Stripped) written to: {clean_path}")

    print(f"\n📊 Summary Stats:")
    print(f"   Input Lines    : {len(lines):,}")
    print(f"   Extracted Lines: {len(final_lines):,}")
    print(f"   Saved Output   : {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Production-Grade Highlight Extractor & Cleaner for Large Markdown Course Notes."
    )
    parser.add_argument("input_file", nargs="?", default=None,
                        help="Path to source Markdown notes with [[HL::...::HL]] tags.")
    parser.add_argument("-o", "--output", default=None,
                        help="Path to save extracted highlights. Defaults to <input>_Highlights.md.")
    parser.add_argument("--clean-output", default=None,
                        help="Optional second output file path to save a clean version without highlight tags.")
    parser.add_argument("--strip-tags", action="store_true",
                        help="Strip [[HL:: and ::HL]] tags in the main output file.")
    parser.add_argument("--separator", default=DEFAULT_SEPARATOR,
                        help="Separator string between non-contiguous highlights (default: ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━).")
    parser.add_argument("--no-separator", action="store_true",
                        help="Do not insert separators between non-contiguous highlights.")
    parser.add_argument("--no-headings", action="store_true",
                        help="Omit parent Module and Topic headings from the output.")

    args = parser.parse_args()

    # Default to NestJS Course Notes if no file given
    if not args.input_file:
        default_notes = r"e:\latexNotes\NestJs_Course_Notes\NestJs_Course_Notes.md"
        if os.path.exists(default_notes):
            args.input_file = default_notes
        else:
            parser.print_help()
            sys.exit(1)

    extract_highlights(
        input_file=args.input_file,
        output_file=args.output,
        keep_highlights=not args.strip_tags,
        include_headings=not args.no_headings,
        clean_output_file=args.clean_output,
        separator=args.separator,
        no_separator=args.no_separator
    )


if __name__ == "__main__":
    main()