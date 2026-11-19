#!/usr/bin/env python3
"""Report which SEO data connections are already set up on this machine.

Checks two things, and never prints a secret:
  1. Known environment variables: set or not set. Values are never printed.
  2. MCP servers configured for Claude Code, Claude Desktop and Cursor: the
     server name, transport, host or command, and which known tool family it
     looks like. Headers, env values and URL query strings are never printed.

It reads local files only. No network.

Usage:
  python check_env.py                      # this machine, current folder as the project
  python check_env.py --project PATH       # a different project folder
  python check_env.py --home PATH          # a different home folder (for testing)
  python check_env.py --json               # machine-readable output
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

# Variables that tools in this pack, or their documented setups, read.
ENV_VARS = [
    ("DATAFORSEO_LOGIN", "DataForSEO", "local-seo-audit grid.py"),
    ("DATAFORSEO_PASSWORD", "DataForSEO", "local-seo-audit grid.py and the DataForSEO MCP"),
    ("DATAFORSEO_USERNAME", "DataForSEO", "DataForSEO MCP (local)"),
    ("SEARCHOPS_API_KEY", "SearchOps", "a SearchOps key kept for a Bearer header (sign-in needs none)"),
    ("GOOGLE_APPLICATION_CREDENTIALS", "Google", "Google Analytics MCP and many Search Console MCPs"),
    ("GOOGLE_CLOUD_PROJECT", "Google", "Google Analytics MCP"),
]

# Substrings in a server's name, URL or command that identify a tool family.
FAMILIES = [
    ("searchops", "SearchOps"),
    ("dataforseo", "DataForSEO"),
    ("dfs-mcp", "DataForSEO"),
    ("analytics-mcp", "Google Analytics"),
    ("google-analytics", "Google Analytics"),
    ("search-console", "Search Console"),
    ("searchconsole", "Search Console"),
    ("gsc", "Search Console"),
    ("mybusiness", "Business Profile"),
    ("business-profile", "Business Profile"),
]


def config_files(home, project):
    appdata = os.environ.get("APPDATA")
    files = [
        ("Claude Code (user and per-project)", home / ".claude.json"),
        ("Claude Code (project .mcp.json)", project / ".mcp.json"),
        ("Cursor (global)", home / ".cursor" / "mcp.json"),
        ("Cursor (project)", project / ".cursor" / "mcp.json"),
        ("Claude Desktop (macOS)", home / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"),
        ("Claude Desktop (Linux)", home / ".config" / "Claude" / "claude_desktop_config.json"),
    ]
    if appdata:
        files.append(("Claude Desktop (Windows)", Path(appdata) / "Claude" / "claude_desktop_config.json"))
    files.append(("Claude Desktop (Windows)", home / "AppData" / "Roaming" / "Claude" / "claude_desktop_config.json"))
    seen, out = set(), []
    for label, p in files:
        key = str(p.resolve()) if p.exists() else str(p)
        if key not in seen:
            seen.add(key)
            out.append((label, p))
    return out


def family(*parts):
    text = " ".join(p for p in parts if p).lower()
    for needle, fam in FAMILIES:
        if needle in text:
            return fam
    return "other"


SECRET_WORDS = ("auth", "bearer", "token", "key", "secret", "password", "passwd", "credential")
SAFE_ARG = re.compile(r"^[-@\w][\w./@:+-]*$")


def safe_args(args, limit=4):
    """Keep package names, plain flags and key-free URLs; drop anything that could be a secret."""
    out, skip_next = [], False
    for a in args:
        if skip_next:
            skip_next = False
            continue
        low = a.lower()
        if low in ("--header", "-h", "--env", "-e", "--api-key", "--token"):
            skip_next = True
            out.append(a + " (value hidden)")
            continue
        if low.startswith("http"):
            parts = urlsplit(a)
            out.append(f"{parts.scheme}://{parts.netloc}{parts.path}" + (" (query hidden)" if parts.query else ""))
        elif "=" in a or any(w in low for w in SECRET_WORDS) or not SAFE_ARG.match(a) or len(a) > 60:
            out.append("(argument hidden)")
        else:
            out.append(a)
        if len(out) >= limit:
            break
    return out


def describe(name, cfg):
    """Return a safe description of one server entry: nothing secret."""
    url = cfg.get("url") or cfg.get("serverUrl")
    notes = []
    if url:
        parts = urlsplit(url)
        where = f"{parts.scheme}://{parts.netloc}{parts.path}"
        transport = cfg.get("type", "http")
        if parts.query:
            notes.append("URL carries a query string (often a key); prefer sign-in or a header")
        fam = family(name, parts.netloc, parts.path)
    else:
        cmd = cfg.get("command", "")
        args = [a for a in cfg.get("args", []) if isinstance(a, str)]
        shown = safe_args(args)
        where = " ".join([cmd] + shown).strip()
        if any("(query hidden)" in x for x in shown):
            notes.append("a URL argument carries a query string (often a key); prefer sign-in or a header")
        transport = cfg.get("type", "stdio")
        fam = family(name, cmd, " ".join(args))
    if cfg.get("headers"):
        notes.append(f"sends {len(cfg['headers'])} header(s)")
    if cfg.get("env"):
        notes.append("sets " + ", ".join(sorted(cfg["env"].keys())) + " (values hidden)")
    return {"name": name, "family": fam, "transport": transport, "where": where, "notes": notes}


def read_servers(label, path, project):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except (json.JSONDecodeError, UnicodeDecodeError, OSError) as e:
        return [{"name": "(unreadable)", "family": "-", "transport": "-", "where": str(path), "notes": [f"could not read: {type(e).__name__}"]}]
    found = []
    for name, cfg in (data.get("mcpServers") or {}).items():
        d = describe(name, cfg if isinstance(cfg, dict) else {})
        d["scope"] = "user" if path.name == ".claude.json" else "file"
        found.append(d)
    # ~/.claude.json keeps local-scope servers per project path.
    projects = data.get("projects") or {}
    target = str(project.resolve()).replace("\\", "/").lower()
    for ppath, pcfg in projects.items():
        if not isinstance(pcfg, dict):
            continue
        servers = pcfg.get("mcpServers") or {}
        if not servers:
            continue
        here = ppath.replace("\\", "/").lower() == target
        for name, cfg in servers.items():
            d = describe(name, cfg if isinstance(cfg, dict) else {})
            d["scope"] = "local (this project)" if here else "local (another project)"
            found.append(d)
    return found


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--home", type=Path, default=None)
    ap.add_argument("--project", type=Path, default=Path.cwd())
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.home is None:
        try:
            a.home = Path.home()
        except RuntimeError:
            sys.exit("Could not work out the home folder. Pass --home PATH.")

    env = [{"var": v, "tool": t, "used_by": u, "set": bool(os.environ.get(v))} for v, t, u in ENV_VARS]
    configs = []
    for label, path in config_files(a.home, a.project):
        servers = read_servers(label, path, a.project)
        if servers is not None:
            configs.append({"file": label, "path": str(path), "servers": servers})

    if a.json:
        json.dump({"env": env, "configs": configs}, sys.stdout, indent=2)
        print()
        return

    print("## Environment variables (values never shown)\n")
    print("| Variable | Tool | Used by | Set? |")
    print("|---|---|---|---|")
    for e in env:
        print(f"| {e['var']} | {e['tool']} | {e['used_by']} | {'yes' if e['set'] else 'no'} |")

    print("\n## MCP servers in config files\n")
    if not configs:
        print("No Claude Code, Claude Desktop or Cursor MCP config files found.")
    families = set()
    for c in configs:
        print(f"**{c['file']}** ({c['path']})")
        if not c["servers"]:
            print("- no MCP servers configured")
        for s in c["servers"]:
            families.add(s["family"])
            extra = f" ({'; '.join(s['notes'])})" if s["notes"] else ""
            scope = f", {s['scope']}" if s.get("scope") else ""
            print(f"- {s['name']}: {s['family']}, {s['transport']}{scope}, {s['where']}{extra}")
        print()

    known = sorted(f for f in families if f not in ("other", "-"))
    print("## Summary\n")
    print(f"- Tool families configured: {', '.join(known) if known else 'none recognised'}")
    print(f"- Environment variables set: {', '.join(e['var'] for e in env if e['set']) or 'none'}")
    print("- Configured is not connected. Run `claude mcp list` for live status, then verify each with one read call.")
    print("- Servers configured for another project are not available in this one unless added with --scope user.")


if __name__ == "__main__":
    main()
