#!/usr/bin/env python3
"""Generate `docs/index.md` listing all markdown files in `docs/`.

Usage: python scripts/generate_docs_index.py
"""
from pathlib import Path
import re


def title_from_stem(stem: str) -> str:
    # Remove leading numeric prefixes like "1. "
    return re.sub(r"^\s*\d+\.\s*", "", stem).strip()


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    docs_dir = repo_root / "docs"
    if not docs_dir.exists():
        print(f"Docs directory not found: {docs_dir}")
        return

    md_files = sorted(docs_dir.glob("*.md"), key=lambda p: p.name)
    index_path = docs_dir / "index.md"

    lines = ["# Docs Index\n", "Auto-generated list of docs in this folder.\n\n"]
    for md in md_files:
        stem = md.stem
        title = title_from_stem(stem)
        # Use the filename (relative link) so the index.md lives inside docs/
        lines.append(f"- [{title}]({md.name})\n")

    index_path.write_text("".join(lines), encoding="utf-8")
    print(f"Wrote {index_path}")


if __name__ == "__main__":
    main()
