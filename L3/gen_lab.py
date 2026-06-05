#!/usr/bin/python3
"""
    Program name: gen_lab.py
    Purpose: Generate a lab submission template file based on a given week's raw markdown document.
    Author: Cameron Lamoureux with Claude Sonnet 4.6
    Date: 24 May 2026

Usage:
    python3 gen_lab.py <markdown_file_or_url> <username>

Examples:
    python3 gen_lab.py l03-ndp.md donn1234
    python3 gen_lab.py https://raw.githubusercontent.com/.../l04-ospf.md donn1234

Output:
    l<NN>-<username>.txt
"""

import re
import sys
import urllib.request
from datetime import date
from pathlib import Path


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_source(src: str) -> str:
    # Return raw text from a local file path or a URL.
    if src.startswith("http://") or src.startswith("https://"):
        with urllib.request.urlopen(src) as r:
            return r.read().decode("utf-8")
    return Path(src).read_text(encoding="utf-8")


def extract_lab_number(text: str, src: str) -> str:
    """
    Try to pull the two-digit lab number from the markdown heading,
    e.g.  # Lab 03 — ...   →  '03'
    Fall back to the filename if the heading isn't found.
    """
    m = re.search(r"#\s+Lab\s+(\d+)", text)
    if m:
        return m.group(1).zfill(2)
    # Fallback: grab digits from filename/URL stem
    stem = Path(src.split("?")[0]).stem        # e.g. 'l03-ndp'
    m2 = re.search(r"(\d+)", stem)
    return m2.group(1).zfill(2) if m2 else "XX"


def extract_lab_title(text: str) -> str:
    # Pull the full title from the first H1 heading.
    m = re.search(r"^#\s+(.+)", text, re.MULTILINE)
    raw = m.group(1).strip() if m else "<TITLE>"
    # Remove leading "Lab NN — " so the header template doesn't double it
    raw = re.sub(r"^Lab\s+\d+\s*[—–-]\s*", "", raw)
    return raw


def extract_checkpoints(text: str) -> list[dict]:
    """
    Find every C<N> collection block.  Returns a list of dicts:
        {
          "tag":     "C01",
          "heading": "EDGE IPv6 Addressing and RA Source",
          "comment": "!-- EDGE has IPv6 routing enabled ...",
        }

    Detection strategy
    ------------------
    The markdown pattern is (from l03-ndp.md):

        #### C0N — Collection of Information
        ...
        ```text
        === C0N – <heading> ===
        ```
        ...
        ```text
        !-- <comment text>
        ```
    """
    checkpoints = []

    # Split into sections at each "#### C\d" heading
    sections = re.split(r"(?=####\s+C\d+\s*[—–-])", text)

    for section in sections:
        # Only process actual collection sections
        if not re.match(r"####\s+C\d+\s*[—–-]\s*Collection", section):
            continue

        # --- tag (e.g. C01) ---
        tag_m = re.match(r"####\s+(C\d+)", section)
        tag = tag_m.group(1) if tag_m else "C??"

        # --- section heading from the ``` text block with === ===
        head_m = re.search(r"```\s*text\s*\n===\s*" + re.escape(tag)
                           + r"\s*[–—-]\s*(.+?)\s*===", section, re.IGNORECASE)
        heading = head_m.group(1).strip() if head_m else f"<heading for {tag}>"

        # --- comment line starting with !--
        comment_m = re.search(r"```\s*text\s*\n(!--[^\n]+)", section)
        comment = comment_m.group(1).strip() if comment_m else "!-- <add your reflection here>"

        checkpoints.append({"tag": tag, "heading": heading, "comment": comment})

    return checkpoints


# ---------------------------------------------------------------------------
# Output builder
# ---------------------------------------------------------------------------

HEADER_TEMPLATE = """\
! ============================================================
! Lab {lab_num} — {title}
! Student  : {username}
! Date     : {today}
! ============================================================
"""

SECTION_TEMPLATE = """\
=== {tag} – {heading} ===

{comment}

"""

FOOTER_TEMPLATE = """\
! ============================================================
! END OF EVIDENCE — l{lab_num}-{username}.txt
! ============================================================
"""


def build_output(lab_num: str, title: str, username: str,
                 checkpoints: list[dict]) -> str:
    today = date.today().isoformat()
    parts = [HEADER_TEMPLATE.format(
        lab_num=lab_num, title=title, username=username, today=today
    )]
    for cp in checkpoints:
        parts.append(SECTION_TEMPLATE.format(**cp))
    parts.append(FOOTER_TEMPLATE.format(lab_num=lab_num, username=username))
    return "".join(parts)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    src, username = sys.argv[1], sys.argv[2]

    print(f"Loading: {src}")
    text = load_source(src)

    lab_num     = extract_lab_number(text, src)
    title       = extract_lab_title(text)
    checkpoints = extract_checkpoints(text)

    if not checkpoints:
        print("WARNING: No collection checkpoints found. Check the markdown format.")

    output      = build_output(lab_num, title, username, checkpoints)
    out_name    = f"l{lab_num}-{username}.txt"
    out_path    = Path(r"[ENTER YOUR FILEPATH HERE]") / out_name

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(output, encoding="utf-8")

    print(f"Generated: {out_path}")
    print(f"Sections : {[cp['tag'] for cp in checkpoints]}")


if __name__ == "__main__":
    main()