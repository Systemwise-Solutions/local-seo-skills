# Orient: what connecting needs, and where to find it

This skill needs less than the audit. Find each piece yourself first; ask the user only for what you can't find, in one message, and say why you need it.

| Connecting needs | Look here first | Why it matters |
|---|---|---|
| The goal | The user's request, `local-seo-brief.md`, `local-seo-log.md` (a re-check that's due, a finding that needs data) | Decides which data matters. Without it you'd recommend tools by habit. |
| The business, as tools will show it | The brief, the website, the Maps listing | You verify each connection against it: a tool that returns the wrong location or property is not connected. |
| One location or many, and who it's for | The brief, location pages, the conversation | Past a handful of locations, by-hand checks stop scaling. Agencies need accounts and Google access set up so the client keeps ownership. |
| How customers become revenue | The site (call links, booking widgets, forms, checkout), the brief | Decides what tracking is worth connecting: profile calls, GA4 key events, bookings, orders. |
| How far customers or the business travel | The brief, the profile, site copy | Sizes the geo-grid, which sets the cost of a grid source. |
| Where Claude is running | The session itself: config files and a shell mean Claude Code; their absence usually means the Claude app. Ask if unclear. | The steps differ completely, and the Claude web app can't run local servers. |
| Claude plan, if they use the app | Ask, only if it changes the answer | Plan limits decide how many custom connectors they can add and whether an admin must do it (environments.md). |
| What's already connected or configured | Your tool list; in Claude Code `scripts/check_env.py` and `claude mcp list`; the repo's `.mcp.json` and `.env.example` | The cheapest connection is the one that already exists. Configured is not connected until a read call proves it. |
| What they already pay for | The brief, configured servers, the user | Use it before recommending anything new. |
| Google access | The brief; the site's source (a GA4 or Tag Manager tag shows GA4 is installed, a verification meta tag suggests Search Console); the user | Owner or manager on the profile, verified Search Console, GA4 on the site. Getting access back from an old agency or web designer can come before any connection. |
| What's been tried | `local-seo-log.md`, the user | So you don't reconnect something they removed on purpose, or repeat a setup that failed. |

The money searches are optional here; the audit will find them. Note any the user mentions.

## Writing the brief

If a brief exists, confirm it in one line and update only what changed. If there isn't one, write `local-seo-brief.md` with plain labels (other skills read it): the business, website, profile name, the shape from the lens, locations, money searches if known, goal, and the data section from verify.md. Mark anything this skill didn't need as "to confirm" so the next skill fills it. Keep it short and factual.
