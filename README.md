# Local SEO skills for Claude

Consultant [Mani Bharij](https://localseoconsultant.net)'s local SEO methods, as open-source skills you run in Claude.

Rank across your area in Google Maps, get more calls, recover lost rankings, fix your Business Profile, build pages that rank, get reviews arriving every week and get recommended by AI assistants. For your own business, a brand's locations, or your agency's clients.

Every skill works with no paid tools, and gets sharper when you connect a data source (SearchOps, Local Falcon, BrightLocal, DataForSEO, Search Console, Analytics). Every skill reads the same `local-seo-brief.md`, so you answer the questions once.

**Not sure where to start?** Pick your goal at [localseoconsultant.net](https://localseoconsultant.net/#start) and get the skills to install, the tools worth connecting and a prompt to paste.

## The skills

| Skill | What it does |
|---|---|
| `local-seo-audit` | Finds the few things stopping you ranking and getting calls, in the order to fix them, with a 90-day plan. |
| `local-seo-connect` | Works out which data tools would help, then walks you through connecting them to Claude. |
| `gbp-optimisation` | Compares your Business Profile with the businesses beating you and writes the changes, in a safe order. |
| `local-pages` | Decides which service and town pages deserve to exist, then writes them. New sites and exact-match domains included. |
| `review-engine` | SMS, email and QR request flow with the wording, reply templates, and review pace against competitors. |
| `calls-and-leads` | Finds where enquiries leak, from the profile to the phone, and sets up tracking to prove the fix. |
| `local-ranking-recovery` | Pins down what dropped and when, lines it up against what changed, and gets it back. Suspensions included. |
| `local-ai-visibility` | Measures whether ChatGPT, Gemini and Google's AI recommend you across many runs, and closes the source gaps. |

Website and technical SEO (crawling, indexing, migrations, new builds) is covered by the companion pack [SEO for AI Agents](https://github.com/manibharij/seo-for-ai-agents). The local skills hand over to it when a job needs it.

## Install

### Claude app (web or desktop): no terminal needed

1. Download the zip for each skill you want from [localseoconsultant.net/skills](https://localseoconsultant.net/skills/), or from `dist/` after running the build below.
2. In Claude, turn on code execution: Settings > Capabilities.
3. Go to Customize > Skills, click +, then Upload a skill, and choose a zip. Repeat for each skill.
4. Start a new chat and say: "Run a local SEO audit for my business."

### Claude Code

```
/plugin marketplace add Systemwise-Solutions/local-seo-skills
/plugin install local-seo@mani-bharij
```

That installs every skill. Ask for what you need, or call one directly, for example `/local-seo:local-seo-audit`.

To use a skill on its own, copy its folder from `plugins/local-seo/skills/` into `~/.claude/skills/`.

### Cursor, Codex, Gemini CLI and other agents

Copy `plugins/local-seo/skills/` into your project and add a line to `AGENTS.md` (or your agent's rules file): "For local SEO tasks, follow the skills in that folder."

## How the audit works

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

## Audit scripts

Every skill's scripts are Python 3, standard library only, and run with `--help`. The audit's:

- `grid.py`: summarise a geo-grid (strong radius, coverage, who takes over where you drop out) or run one with DataForSEO.
- `review_velocity.py`: reviews per month, recency and bursts against competitors.
- `nap_check.py`: name, address and phone across listings.
- `prioritise.py`: findings into a ranked fix list and 90-day plan.

Every skill has a fictional worked example in [`examples/`](examples) and test prompts in [`evals/`](evals). Contributing a skill? Read [CONVENTIONS.md](CONVENTIONS.md).

## Build the zips

```
python tools/build_zips.py
```

Writes one upload-ready zip per skill to `dist/` and checks the frontmatter will be accepted by the Claude app.

## Licence

MIT. Use it, change it, run it for clients.

Built by Mani Bharij, local SEO and AI search consultant, London. If you'd rather have the audit done with you, with full geo-grid scans, a recorded walkthrough and 90 days of follow-up: [localseoconsultant.net](https://localseoconsultant.net/consulting/local-seo-audit/).
