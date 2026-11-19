# Local SEO skills for Claude

A free local SEO audit, the way consultant [Mani Bharij](https://localseoconsultant.net) runs it, built into Claude.

Tell Claude about your business. It asks a few questions, checks where you rank across your area, your Google Business Profile, your website, reviews, listings and AI answers, then gives you the few fixes that matter in the order to make them, with a 90-day plan.

It works with no paid tools. It gets sharper if you connect a local SEO data source (a geo-grid MCP server, or your own DataForSEO key).

## What's in it

| Skill | What it does |
|---|---|
| `local-seo-audit` | Tailored intake, six-area audit, Visibility Ladder diagnosis, ranked fix list and 90-day plan. Works for one location, multi-location brands, and agencies auditing a client (white-label). |

More skills are on the way: service and location pages, review engine, AI search visibility.

## Install

### Claude app (web or desktop): no terminal needed

1. Download [`local-seo-audit.zip`](https://localseoconsultant.net/skills/local-seo-audit.zip).
2. In Claude, turn on code execution: Settings > Capabilities.
3. Go to Customize > Skills, click +, then Upload a skill, and choose the zip.
4. Start a new chat and say: "Run a local SEO audit for my business."

### Claude Code

```
/plugin marketplace add Systemwise-Solutions/local-seo-skills
/plugin install local-seo@mani-bharij
```

Then ask for a local SEO audit, or run `/local-seo:local-seo-audit`.

To use the skill on its own, copy `plugins/local-seo/skills/local-seo-audit` into `~/.claude/skills/`.

## How it works

1. **Intake.** Who the audit is for, how many locations, the sector, what's going wrong, and the searches that make money. Claude writes a short brief (`local-seo-brief.md`) and reuses it next time.
2. **Data check.** It tells you what it can measure with what you have, and what it will ask you to check on your phone.
3. **Six areas.** Where you rank, Business Profile, website, reviews, consistency across the web, AI answers.
4. **Diagnosis.** The Visibility Ladder: eligible, understood, ranked, chosen, named. The plan starts at the lowest broken rung.
5. **Prioritise.** A script ranks the fixes and splits them across three months.
6. **Report.** Three things to do first, the findings by month, what not to waste time on, and how to measure progress.

## Data, from free to paid

| You have | What the audit can do |
|---|---|
| Nothing but Claude | Checks your site, profile, listings and competitors through web search. Rankings come from a 5-point check you do on your phone. |
| A local SEO MCP server connected (for example SearchOps, Local Falcon, BrightLocal) | Uses its geo-grid scans, reviews, citations and AI visibility data instead of asking you. |
| Your own DataForSEO key (Claude Code) | `scripts/grid.py scan` runs a real geo-grid. It shows the number of requests and waits for a yes before spending anything. |

## Scripts

Python 3, standard library only. Each runs with `--help`.

- `grid.py`: summarise a geo-grid (strong radius, coverage, who takes over where you drop out) or run one with DataForSEO.
- `review_velocity.py`: reviews per month, recency and bursts against competitors.
- `nap_check.py`: name, address and phone across listings.
- `prioritise.py`: findings into a ranked fix list and 90-day plan.

Try them on the fictional clinic in [`examples/clinic`](examples/clinic).

## Build the zips

```
python tools/build_zips.py
```

Writes one upload-ready zip per skill to `dist/` and checks the frontmatter will be accepted by the Claude app.

## Licence

MIT. Use it, change it, run it for clients.

Built by Mani Bharij, local SEO and AI search consultant, London. If you'd rather have the audit done with you, with full geo-grid scans, a recorded walkthrough and 90 days of follow-up: [localseoconsultant.net](https://localseoconsultant.net/consulting/local-seo-audit/).
