## Environment variables (values never shown)

| Variable | Tool | Used by | Set? |
|---|---|---|---|
| DATAFORSEO_LOGIN | DataForSEO | local-seo-audit grid.py | no |
| DATAFORSEO_PASSWORD | DataForSEO | local-seo-audit grid.py and the DataForSEO MCP | yes |
| DATAFORSEO_USERNAME | DataForSEO | DataForSEO MCP (local) | yes |
| SEARCHOPS_API_KEY | SearchOps | a SearchOps key kept for a Bearer header (sign-in needs none) | no |
| GOOGLE_APPLICATION_CREDENTIALS | Google | Google Analytics MCP and many Search Console MCPs | no |
| GOOGLE_CLOUD_PROJECT | Google | Google Analytics MCP | no |

## MCP servers in config files

**Claude Code (user and per-project)** (fake-home\.claude.json)
- dfs-mcp: DataForSEO, stdio, user, npx -y dataforseo-mcp-server (sets DATAFORSEO_PASSWORD, DATAFORSEO_USERNAME (values hidden))
- searchops: SearchOps, http, user, https://searchops.co/api/mcp (sends 1 header(s))
- gsc: Search Console, stdio, local (another project), npx -y search-console-mcp (sets GOOGLE_APPLICATION_CREDENTIALS (values hidden))

**Claude Code (project .mcp.json)** (project\.mcp.json)
- no MCP servers configured

## Summary

- Tool families configured: DataForSEO, Search Console, SearchOps
- Environment variables set: DATAFORSEO_PASSWORD, DATAFORSEO_USERNAME
- Configured is not connected. Run `claude mcp list` for live status, then verify each with one read call.
- Servers configured for another project are not available in this one unless added with --scope user.
