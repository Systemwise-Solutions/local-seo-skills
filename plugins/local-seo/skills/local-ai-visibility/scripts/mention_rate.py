#!/usr/bin/env python3
"""Turn pasted AI assistant answers into mention rates and cited-source counts.

Answers vary from run to run, so one answer proves nothing. Put the same prompts
to each assistant several times (3 is the minimum), paste every answer into one
file, and run this. Each assistant is reported on its own: rates are never
added together across assistants.

Two input formats.

1. Text (easiest to paste). Header lines, then one block per run:

    business: Example Physio | Example Physiotherapy | example-physio.co.uk
    competitor: Avonside Physio | avonsidephysio.example
    competitor: Downs Movement Clinic
    === ChatGPT | best physio in Clifton
    <the answer, pasted as is>
    Sources: https://www.yell.com/..., doctify.com
    === ChatGPT | best physio in Clifton
    <second run>

   After "business:" and "competitor:", the first item is the name; the rest are
   other names it goes by and its website domain. Every "===" line starts a new
   run: assistant, then the prompt. Repeating the same pair is the next run.
   Lines starting "Sources:" or "Source:" list cited sources; URLs anywhere in
   the answer also count as cited.

2. JSON:

    {"business": {"name": "...", "aliases": [], "domain": "..."},
     "competitors": [{"name": "...", "aliases": [], "domain": "..."}],
     "runs": [{"assistant": "ChatGPT", "prompt": "...", "answer": "...",
               "sources": ["https://..."]}]}

Output: Markdown tables and findings. --json prints the numbers instead.

Usage:
  python mention_rate.py runs.txt
  python mention_rate.py runs.json --json
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from urllib.parse import urlsplit

URL_RE = re.compile(r"https?://[^\s)\]>,;\"']+", re.I)
DOMAIN_RE = re.compile(r"\b((?:[a-z0-9-]+\.)+[a-z]{2,})\b", re.I)
MIN_RUNS = 3
NOT_NAMES = {"sources", "source", "summary", "note", "tip", "tips", "why", "pros", "cons", "location", "address",
             "price", "prices", "website", "phone", "reviews", "rating", "best for", "specialties", "services",
             "opening hours", "hours", "contact", "overview", "conclusion", "final thoughts", "top picks"}


def norm(s):
    s = (s or "").lower().replace("&", " and ").replace("\u2019", "'")
    s = re.sub(r"[^\w\s'.-]", " ", s)
    return " ".join(s.split())


def domain_of(s):
    s = s.strip().strip(".,;")
    if "://" in s:
        host = urlsplit(s).netloc
    else:
        m = DOMAIN_RE.search(s)
        host = m.group(1) if m else ""
    host = host.lower().split(":")[0]
    return host[4:] if host.startswith("www.") else host


def entity(item):
    if isinstance(item, str):
        parts = [p.strip() for p in item.split("|") if p.strip()]
        names = [p for p in parts if not DOMAIN_RE.fullmatch(p.lower().removeprefix("www."))]
        doms = [domain_of(p) for p in parts if DOMAIN_RE.fullmatch(p.lower().removeprefix("www."))]
        if not names:
            sys.exit(f"No name found in '{item}'.")
        return {"name": names[0], "aliases": names[1:], "domain": doms[0] if doms else None}
    return {"name": item["name"], "aliases": item.get("aliases", []), "domain": domain_of(item["domain"]) if item.get("domain") else None}


def parse_text(text):
    data = {"business": None, "competitors": [], "runs": []}
    cur = None
    for line in text.splitlines():
        stripped = line.strip()
        low = stripped.lower()
        if cur is None and low.startswith("business:"):
            data["business"] = stripped.split(":", 1)[1]
        elif cur is None and low.startswith("competitor:"):
            data["competitors"].append(stripped.split(":", 1)[1])
        elif stripped.startswith("==="):
            head = stripped.strip("= ").split("|", 1)
            if len(head) < 2:
                sys.exit(f"Run header needs 'assistant | prompt': {stripped}")
            cur = {"assistant": head[0].strip(), "prompt": head[1].strip(), "answer": "", "sources": []}
            data["runs"].append(cur)
        elif cur is not None and re.match(r"(?i)^sources?:", stripped):
            rest = stripped.split(":", 1)[1]
            cur["sources"] += [s for s in re.split(r"[,\s]+", rest) if s]
        elif cur is not None:
            cur["answer"] += line + "\n"
    if not data["business"]:
        sys.exit("Add a 'business: <name> | <other names> | <domain>' line at the top.")
    return data


def mentioned(ent, answer_norm, answer_raw):
    for n in [ent["name"]] + list(ent["aliases"]):
        if re.search(r"(?<!\w)" + re.escape(norm(n)) + r"(?!\w)", answer_norm):
            return True
    return bool(ent["domain"] and ent["domain"] in answer_raw.lower())


def candidate_names(answer):
    """Names an assistant presented as recommendations: bold text and list-item leads."""
    found = set()
    for m in re.finditer(r"\*\*([^*\n]{3,60})\*\*", answer):
        found.add(m.group(1))
    for m in re.finditer(r"(?m)^\s*(?:\d+[.)]|[-*\u2022])\s+([A-Z][^\n:\u2013\u2014(]{2,60}?)\s*(?:[:\u2013\u2014(-]|$)", answer):
        found.add(m.group(1))
    out = set()
    for f in found:
        f = f.strip(" *.:-")
        if f and f.lower() not in NOT_NAMES and len(f.split()) <= 7 and re.search(r"[A-Z]", f):
            out.add(f)
    return out


def analyse(data):
    you = entity(data["business"])
    comps = [entity(c) for c in data.get("competitors", [])]
    known = {norm(n) for e in [you] + comps for n in [e["name"]] + e["aliases"]}
    runs = data["runs"]
    if not runs:
        sys.exit("No runs found.")
    by_asst = defaultdict(list)
    for r in runs:
        ans = r.get("answer", "")
        an = norm(ans)
        srcs = {domain_of(s) for s in r.get("sources", [])} | {domain_of(u) for u in URL_RE.findall(ans)}
        srcs.discard("")
        r["_you"] = mentioned(you, an, ans)
        r["_comps"] = {c["name"]: mentioned(c, an, ans) for c in comps}
        r["_sources"] = srcs
        r["_cands"] = {c for c in candidate_names(ans) if norm(c) not in known and not any(k in norm(c) for k in known)}
        by_asst[r["assistant"]].append(r)

    out = {"business": you["name"], "assistants": {}, "prompts": {}, "competitors": {}, "sources": [], "other_names": [], "warnings": []}
    for a, rs in by_asst.items():
        n = len(rs)
        named = sum(r["_you"] for r in rs)
        own = sum(1 for r in rs if you["domain"] and you["domain"] in r["_sources"])
        out["assistants"][a] = {"runs": n, "named": named, "rate": named / n, "own_site_cited": own if you["domain"] else None}
        for c in comps:
            k = sum(r["_comps"][c["name"]] for r in rs)
            out["competitors"].setdefault(c["name"], {})[a] = {"named": k, "rate": k / n}
        per_prompt = defaultdict(list)
        for r in rs:
            per_prompt[r["prompt"]].append(r)
        for p, prs in per_prompt.items():
            out["prompts"].setdefault(p, {})[a] = {"runs": len(prs), "named": sum(r["_you"] for r in prs)}
            if len(prs) < MIN_RUNS:
                out["warnings"].append(f"{a}, \"{p}\": only {len(prs)} run(s). Run it at least {MIN_RUNS} times before reading anything into it.")

    cited = defaultdict(lambda: {"runs": 0, "assistants": set(), "with_you": 0})
    for r in runs:
        for d in r["_sources"]:
            cited[d]["runs"] += 1
            cited[d]["assistants"].add(r["assistant"])
            cited[d]["with_you"] += r["_you"]
    owners = {e["domain"]: e["name"] for e in [you] + comps if e["domain"]}
    for d, v in sorted(cited.items(), key=lambda kv: (-kv[1]["runs"], kv[0])):
        out["sources"].append({"domain": d, "runs": v["runs"], "assistants": sorted(v["assistants"]),
                               "runs_naming_you": v["with_you"], "owner": owners.get(d)})

    cand = Counter()
    for r in runs:
        cand.update(r["_cands"])
    out["other_names"] = [{"name": k, "runs": v} for k, v in cand.most_common() if v >= 2]
    out["total_runs"] = len(runs)
    return out


def pct(x):
    return f"{round(x * 100)}%"


def findings(o):
    f = []
    for a, s in o["assistants"].items():
        leaders = [(c, v[a]["rate"]) for c, v in o["competitors"].items() if a in v and v[a]["rate"] >= 0.5]
        if s["rate"] < 0.5 and leaders:
            top = max(leaders, key=lambda t: t[1])
            f.append(f"{a}: named in {s['named']} of {s['runs']} runs ({pct(s['rate'])}), while {top[0]} is named in {pct(top[1])}.")
        elif s["named"] == 0:
            f.append(f"{a}: never named in {s['runs']} runs.")
        if s["own_site_cited"] == 0 and s["runs"] >= MIN_RUNS:
            f.append(f"{a}: your own website was never cited.")
    third = [s for s in o["sources"] if not s["owner"] and s["runs"] >= 2]
    never = [s for s in third if s["runs_naming_you"] == 0]
    rarely = [s for s in third if 0 < s["runs_naming_you"] < s["runs"] / 2]
    if never:
        f.append("Cited in 2 or more runs, and none of those runs named you: " + ", ".join(f"{s['domain']} ({s['runs']})" for s in never[:8])
                 + ". Check whether each lists you, and how.")
    if rarely:
        f.append("Cited often, but fewer than half of those runs named you: "
                 + ", ".join(f"{s['domain']} ({s['runs_naming_you']} of {s['runs']})" for s in rarely[:8])
                 + ". Check how each describes you against the competitors it lists.")
    if o["other_names"]:
        f.append("Other names appearing in 2 or more runs (check them, and add real competitors with 'competitor:' lines): "
                 + ", ".join(f"{c['name']} ({c['runs']})" for c in o["other_names"][:8]) + ".")
    return f


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("runs", help="runs.txt or runs.json")
    ap.add_argument("--json", action="store_true", help="print the numbers as JSON")
    a = ap.parse_args()
    with open(a.runs, encoding="utf-8") as fh:
        raw = fh.read()
    data = json.loads(raw) if a.runs.lower().endswith(".json") else parse_text(raw)
    o = analyse(data)

    if a.json:
        json.dump(o, sys.stdout, indent=2, default=list)
        print()
        return

    asst = list(o["assistants"])
    print(f"# AI mentions: {o['business']}\n")
    print(f"{o['total_runs']} runs across {len(asst)} assistant(s). Each assistant is measured on its own; rates are not added together.\n")
    print("## How often you're named\n")
    print("| Assistant | Runs | Named | Mention rate | Own site cited |")
    print("|---|---|---|---|---|")
    for x, s in o["assistants"].items():
        own = "-" if s["own_site_cited"] is None else f"{s['own_site_cited']} of {s['runs']}"
        print(f"| {x} | {s['runs']} | {s['named']} | {pct(s['rate'])} | {own} |")

    print("\n## By prompt (named / runs)\n")
    print("| Prompt | " + " | ".join(asst) + " |")
    print("|---|" + "---|" * len(asst))
    for p, v in o["prompts"].items():
        cells = [f"{v[x]['named']}/{v[x]['runs']}" if x in v else "-" for x in asst]
        print(f"| {p} | " + " | ".join(cells) + " |")

    if o["competitors"]:
        print("\n## Who is named instead (mention rate)\n")
        print("| Business | " + " | ".join(asst) + " |")
        print("|---|" + "---|" * len(asst))
        print(f"| **{o['business']}** | " + " | ".join(pct(o["assistants"][x]["rate"]) for x in asst) + " |")
        for c, v in sorted(o["competitors"].items(), key=lambda kv: -sum(t["rate"] for t in kv[1].values())):
            print(f"| {c} | " + " | ".join(pct(v[x]["rate"]) if x in v else "-" for x in asst) + " |")

    print("\n## Sources cited\n")
    if o["sources"]:
        print("| Source | Runs citing | Assistants | Of those, runs naming you | Whose site |")
        print("|---|---|---|---|---|")
        for s in o["sources"][:25]:
            print(f"| {s['domain']} | {s['runs']} | {', '.join(s['assistants'])} | {s['runs_naming_you']} | {s['owner'] or '-'} |")
        if len(o["sources"]) > 25:
            print(f"\n({len(o['sources']) - 25} more sources cited once or twice; see --json.)")
    else:
        print("No sources recorded. Paste the links each answer shows, on a 'Sources:' line.")

    fs = findings(o)
    print("\n## Findings\n")
    print("\n".join(f"- {x}" for x in fs) if fs else "- No gaps against the listed competitors.")
    if o["warnings"]:
        print("\n## Sample size\n")
        print("\n".join(f"- {w}" for w in o["warnings"]))
    print("\nTreat these as a pattern from this sample, not a fixed position. Re-run the same prompts monthly to see movement.")


if __name__ == "__main__":
    main()
