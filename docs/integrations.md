# Integrations

## GitHub Copilot CLI + Portfolio MCP

This repository includes a local MCP server so GitHub Copilot CLI can work with portfolio content through a safer, content-scoped interface.

## Server Files

- `mcp/portfolio_site_mcp_server.py`: local MCP server implementation.
- `mcp/install_copilot_mcp.py`: installer that merges the server into `~/.copilot/mcp-config.json`.
- `mcp/copilot-mcp-config.example.json`: example standalone config snippet.

## Supported MCP Tools

- `get_site_content_map`: returns editable content targets and frontmatter conventions.
- `list_content_files`: lists editable pages, posts, and project files.
- `get_content_file`: reads an allowed content file with parsed frontmatter.
- `write_content_file`: writes a page, post, or project file inside the allowed content scope.
- `build_site`: runs `bundle exec jekyll build`.

## Allowed Content Targets

```text
index.md
about.md
projects.md
blog/index.md
_projects/*.md
_posts/YYYY-MM-DD-slug.md
```

## Install Steps

```bash
python mcp/install_copilot_mcp.py
```

After installation, restart Copilot CLI and start working from the repository root:

```bash
copilot
```

## Example Prompt

```text
Use the portfolioSite MCP server to add a new project case study for my latest app, update the homepage highlights to mention it, and then run the site build.
```

## Configuration Example

```json
{
  "mcpServers": {
    "portfolioSite": {
      "type": "local",
      "command": "python",
      "args": [
        "F:/path/to/thairux.github.io_portfolio/mcp/portfolio_site_mcp_server.py",
        "--repo",
        "F:/path/to/thairux.github.io_portfolio"
      ]
    }
  }
}
```

## Notes

- The installer preserves unrelated user MCP entries.
- The server intentionally blocks arbitrary file edits outside content targets.
- Build verification depends on Ruby, Bundler, and the project gems being installed locally.

## Related Files

- `docs/architecture.md`
- `docs/workflows.md`
- `docs/conventions.md`
- `.github/copilot-instructions.md`
