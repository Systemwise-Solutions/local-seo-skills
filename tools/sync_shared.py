#!/usr/bin/env python3
"""Copy the files in shared/ into every skill's references/, so each skill zip is self-contained.

Edit shared/*.md, never the copies. build_zips.py runs this first.
Usage: python tools/sync_shared.py [--check]   (--check exits 1 if any copy is out of date)
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main():
    check = "--check" in sys.argv
    stale = []
    for src in sorted((ROOT / "shared").glob("*.md")):
        for skill in sorted(ROOT.glob("plugins/*/skills/*/SKILL.md")):
            dst = skill.parent / "references" / src.name
            text = src.read_text(encoding="utf-8")
            if not dst.exists() or dst.read_text(encoding="utf-8") != text:
                stale.append(dst.relative_to(ROOT))
                if not check:
                    dst.parent.mkdir(exist_ok=True)
                    dst.write_text(text, encoding="utf-8")
    for s in stale:
        print(("out of date: " if check else "updated: ") + str(s))
    if check and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()
