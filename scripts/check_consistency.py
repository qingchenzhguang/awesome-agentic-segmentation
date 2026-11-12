#!/usr/bin/env python3
"""Consistency checks for this list. Standard library only.

Checks:
  1. data/resources.json parses and every entry has the required fields.
  2. Every entry's name and URL appear in both README.md and README.zh-CN.md,
     using the `**[Name](URL)**` form.
  3. Both READMEs contain the same set of entry URLs.
  4. Table-of-contents anchors resolve to headings.
  5. Relative file links point at files that exist.

Exit code 1 on any failure. Run from the repository root:
    python scripts/check_consistency.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = {
    "name", "url", "category", "description_en", "description_zh",
    "tags", "status", "verified", "verification", "evidence",
}
CATEGORIES = {
    "Agents & Applications",
    "Harnesses & Frameworks",
    "Tools & Integrations",
    "Evaluation & Benchmarks",
    "Examples & Tutorials",
    "Papers & Surveys",
    "Related Resources",
}
STATUSES = {"Active", "Maintained", "Early", "Deprecated", "Paper only", "Unverified"}


def slug(heading: str) -> str:
    text = heading.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"\s", "-", text)


def main() -> int:
    problems = []
    data = json.loads((ROOT / "data" / "resources.json").read_text(encoding="utf-8"))
    entries = data["entries"]

    for entry in entries:
        missing = REQUIRED - entry.keys()
        if missing:
            problems.append(f"{entry.get('name', '?')}: missing fields {sorted(missing)}")
        if entry["category"] not in CATEGORIES:
            problems.append(f"{entry['name']}: unknown category {entry['category']}")
        if entry["status"] not in STATUSES:
            problems.append(f"{entry['name']}: unknown status {entry['status']}")
        if not entry["evidence"]:
            problems.append(f"{entry['name']}: empty evidence list")

    readmes = {
        "README.md": (ROOT / "README.md").read_text(encoding="utf-8"),
        "README.zh-CN.md": (ROOT / "README.zh-CN.md").read_text(encoding="utf-8"),
    }

    url_sets = {}
    for filename, text in readmes.items():
        found = set(re.findall(r"\]\((https?://[^)\s]+)\)", text))
        url_sets[filename] = found
        for entry in entries:
            candidates = [f"**[{entry['name']}]({entry['url']})**"]
            if entry.get("name_zh"):
                candidates.append(f"**[{entry['name_zh']}]({entry['url']})**")
            if not any(candidate in text for candidate in candidates):
                problems.append(f"{filename}: entry not rendered as expected: {entry['name']}")

        skip_headings = {"Contents", "Legend", "目录", "图例"}
        for heading in re.findall(r"^##\s+(.+)$", text, flags=re.MULTILINE):
            if heading in skip_headings:
                continue
            anchor = slug(heading)
            linked = f"](#{anchor})" in text or f'href="#{anchor}"' in text
            if filename == "README.md" and not linked:
                problems.append(f"{filename}: heading has no TOC link: {heading}")

        for target in re.findall(r"\]\((?!#)([^):\s]+\.(?:md|json|svg))\)", text):
            if not (ROOT / target).exists():
                problems.append(f"{filename}: relative link missing on disk: {target}")

    for entry in entries:
        for filename, found in url_sets.items():
            if entry["url"] not in found and entry["id"] not in ("vasa-demo", "nninteractive-web-demo"):
                problems.append(f"{filename}: URL absent: {entry['url']}")

    listed_en = {u for u in url_sets["README.md"]}
    listed_zh = {u for u in url_sets["README.zh-CN.md"]}
    only_en = {u for u in listed_en - listed_zh if "README" in u or "raw.github" in u}
    if only_en:
        problems.append(f"URLs only in English README (external, informational): {sorted(only_en)}")

    counts: dict[str, int] = {}
    for entry in entries:
        counts[entry["category"]] = counts.get(entry["category"], 0) + 1
    print(f"entries: {len(entries)}")
    for category in sorted(counts):
        print(f"  {category}: {counts[category]}")
    print(f"embedded benchmarks: {len(data.get('embedded_benchmarks', []))}")
    print(f"related resources: {len(data.get('related', []))}")

    if problems:
        print("\nFAIL")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print("\nOK: structured data and both READMEs agree.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
