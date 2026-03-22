# Error Handling And Logging

## MCP Server Error Model

The local MCP server returns structured JSON-RPC errors when:

- a method is unknown
- a tool name is unknown
- a requested path is outside the approved content scope
- required frontmatter fields are missing
- unsupported frontmatter types are provided

## Common Failure Cases

### Invalid Content Path

Only these targets are writable through the MCP server:

```text
index.md
about.md
projects.md
blog/index.md
_projects/*.md
_posts/YYYY-MM-DD-slug.md
```

### Missing Build Dependencies

If `bundle exec jekyll build` fails because Bundler is unavailable, install Ruby, Bundler, and the project gems first.

### Invalid Post Filename

Post filenames must begin with `YYYY-MM-DD-` and end with `.md`.

## Logging Approach

- The server keeps stdout reserved for MCP protocol messages.
- Errors are surfaced through JSON-RPC responses instead of plain console output.
- The local Copilot CLI logs remain available under `~/.copilot/logs/` for session troubleshooting.

## Related Files

- `mcp/portfolio_site_mcp_server.py`
- `docs/integrations.md`
- `docs/workflows.md`
