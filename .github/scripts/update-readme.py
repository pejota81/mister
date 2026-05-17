#!/usr/bin/env python3
"""Update README files with latest changelog information.

Run from the repo root:
    python .github/scripts/update-readme.py

What it changes in each README:
  - The "Latest Release" section heading (version, title, date)
  - The "Full Release Notes" link at the bottom of that section
  - All rows in the "Release History" table

Existing translated content (section body text, translated table highlights)
is preserved; only new-version rows use the English changelog title.
"""

import os
import re
import sys
from glob import glob
from datetime import datetime

MONTHS = {
    "en": [
        "", "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December",
    ],
    "pt": [
        "", "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro",
    ],
    "es": [
        "", "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
    ],
}


def format_date(iso_date, lang):
    """Convert YYYY-MM-DD to a localized date string."""
    d = datetime.strptime(iso_date, "%Y-%m-%d")
    m = MONTHS[lang][d.month]
    if lang == "en":
        return f"{m} {d.day}, {d.year}"
    return f"{d.day} de {m} de {d.year}"


def parse_changelog(path):
    """Return (version, iso_date, english_title) from a changelog file."""
    version = os.path.basename(path)[:-3]  # e.g. "v0.03"
    with open(path, encoding="utf-8") as f:
        text = f.read()
    date_m = re.search(r"> Released: (\d{4}-\d{2}-\d{2})", text)
    date = date_m.group(1) if date_m else "2026-05-01"
    # Title line: "# Mister v0.03 — Mobile UX, ..."
    # Changelog files use an em-dash (U+2014) between version and title.
    title_m = re.search(r"^# (?:Mister|PJfoot) \S+ [\u2014-] (.+)$", text, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else version
    return version, date, title


def get_changelogs():
    """Return all v*.md changelogs sorted by version descending."""
    entries = [parse_changelog(p) for p in glob("changelog/v*.md")]
    entries.sort(key=lambda x: x[0], reverse=True)
    return entries


def parse_table_rows(content):
    """Extract existing table rows as {version: highlights_str}."""
    rows = {}
    for m in re.finditer(
        r"^\| \*\*(v[\d.]+)\*\* \| [^|]+ \| ([^|]+?) \|$",
        content,
        re.MULTILINE,
    ):
        rows[m.group(1)] = m.group(2).strip()
    return rows


def update_readme(path, changelogs, lang):
    with open(path, encoding="utf-8") as f:
        content = f.read()

    latest_ver, latest_date, latest_title = changelogs[0]
    new_date = format_date(latest_date, lang)

    # 1. Update the "Latest Release" heading line.
    #    Pattern: ### **v0.03** – Some Title *(May 2, 2026)*
    # README headings use an en-dash (U+2013): ### **v0.03** – Title *(date)*
    # The replacement also writes an en-dash for consistency.
    def repl_heading(m):
        cur_ver = m.group(1)
        cur_title = m.group(2)
        # Keep existing (translated) title when the version hasn't changed.
        title = cur_title if cur_ver == latest_ver else latest_title
        return f"### **{latest_ver}** \u2013 {title} *({new_date})*"

    content = re.sub(
        r"^### \*\*(v[\d.]+)\*\* \u2013 (.+?) \*\([^)]*\)\*$",
        repl_heading,
        content,
        flags=re.MULTILINE,
    )

    # 2. Update the "Full Release Notes" link (any translated link text).
    #    Pattern: [📖 Any text](changelog/v0.03.md)
    content = re.sub(
        r"(\[📖[^\]]*\])\(changelog/v[\d.]+\.md\)",
        rf"\1(changelog/{latest_ver}.md)",
        content,
    )

    # 3. Rebuild the Release History table rows.
    existing = parse_table_rows(content)
    new_rows = []
    for ver, date, title in changelogs:
        highlights = existing.get(ver, title)  # keep translated highlights if present
        new_rows.append(f"| **{ver}** | {format_date(date, lang)} | {highlights} |")
    new_body = "\n".join(new_rows) + "\n"

    content = re.sub(
        r"(\| \*\*v[\d.]+\*\*[^\n]+\n)+",
        new_body,
        content,
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Updated {path}")


def main():
    changelogs = get_changelogs()
    if not changelogs:
        print("No changelog files found in changelog/v*.md — nothing to do.")
        sys.exit(0)
    print(f"Found {len(changelogs)} changelog(s). Latest: {changelogs[0][0]}")
    update_readme("README.md", changelogs, "en")
    update_readme("README.pt-BR.md", changelogs, "pt")
    update_readme("README.es.md", changelogs, "es")
    print("Done.")


if __name__ == "__main__":
    main()
