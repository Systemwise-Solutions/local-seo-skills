#!/usr/bin/env python3
"""Build one upload-ready zip per skill into dist/, for the Claude app (Customize > Skills > Upload).

Each zip's root is the skill folder, named to match the skill's `name`, as the app requires.
Also checks the frontmatter uses only keys the app and API accept.

Usage: python tools/build_zips.py
"""
import pathlib
import re
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
ALLOWED = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}


def check(skill_md: pathlib.Path) -> str:
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        sys.exit(f"{skill_md}: frontmatter must start on line 1")
    keys = {l.split(":", 1)[0] for l in m.group(1).splitlines() if l and not l.startswith((" ", "\t"))}
    bad = keys - ALLOWED
    if bad:
        sys.exit(f"{skill_md}: keys the Claude app rejects: {', '.join(sorted(bad))}")
    name = re.search(r"^name:\s*(\S+)", m.group(1), re.M).group(1)
    desc = re.search(r"^description:\s*(.+)$", m.group(1), re.M).group(1)
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name) or "claude" in name or "anthropic" in name:
        sys.exit(f"{skill_md}: invalid name '{name}'")
    if len(desc) > 1024:
        sys.exit(f"{skill_md}: description is {len(desc)} chars (max 1024)")
    if name != skill_md.parent.name:
        sys.exit(f"{skill_md}: folder name must match name '{name}'")
    if "—" in text:
        sys.exit(f"{skill_md}: contains an em dash")
    return name


def main():
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    for skill_md in sorted(ROOT.glob("plugins/*/skills/*/SKILL.md")):
        name = check(skill_md)
        folder = skill_md.parent
        out = dist / f"{name}.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(folder.rglob("*")):
                if f.is_file() and "__pycache__" not in f.parts:
                    z.write(f, pathlib.Path(name) / f.relative_to(folder))
        print(f"{out.relative_to(ROOT)}  ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
