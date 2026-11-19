# Verify and record

A connection counts only when a read call returns this business's data. Configured is not connected.

## The cheap read per server

| Server | Call | Pass when | Watch for |
|---|---|---|---|
| SearchOps | `list_locations` (with `query` set to the business name) | The business is listed. For Maps goals, `list_scans` for that location shows at least one scan, or the user knows scans haven't been set up yet. | Empty list: wrong SearchOps account, or the location isn't added yet. |
| SearchOps, Google data | `list_search_console_sites`, `list_analytics_properties` | The site or property for this business is there with `active: true` and linked to the location. | An error from `list_analytics_properties` means Analytics isn't connected in SearchOps. |
| Local Falcon | A list or account read tool from its tool list | The business's location or saved reports appear. | Never a scan: scans spend credits. |
| BrightLocal | A list-locations or account read tool | The business's location appears. | Needs Grow plan and Labs access; an access error usually means that. |
| DataForSEO | One small request, after a yes | A result with data and a cost line. | Every data call is billed. Say how many requests before running. |
| Google Analytics MCP | `get_account_summaries` | The property for this website is listed. Then one `run_report` for the last 7 days shows sessions above zero. | Zero sessions: wrong property, or GA4 isn't on the site. |
| Search Console MCP | Its list-sites tool | The site is listed and returns rows for the last 28 days. | A URL-prefix property for `http://` or without `www` can be empty while the real data sits in another property. |

Then one more check for the goal: for Maps goals, a recent grid exists or can be run; for calls, profile performance returns calls; for AI visibility, SearchOps has tracked prompts for the location or the user will run them by hand.

If a call fails: say what failed, try the fix in the vendor's troubleshooting once, and if it still fails record it as "configured, not working" with the error in a few words.

## Recording it

Update the brief's **Data available** section. Layout is up to you, but keep a "Tier" line first, because other skills read it to decide how they measure. It must say:

- **Tier**: free, or the connected servers by name, or a DataForSEO key for scripts.
- **Verified, with the date**: each tool, what it covers for this business, and which location, site or property it returned.
- **Configured, not working**: each tool and the error in a few words, or none.
- **By hand or free**: what the user will screenshot, export or check on their phone, and how often.
- **Not available**: what no connection covers, and how the skills will handle it.
- **Environment**: Claude app (and plan), Claude Code, Cursor or other, because the next skill's steps depend on it.

Add one line per connection made, removed or failed to `local-seo-log.md` (mechanics in loop.md), with when to re-check anything left half-done.

Never record keys, tokens, account emails or URLs containing keys in the brief or log, because both files get shared and committed.
