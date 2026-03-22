# Thairux Portfolio

![Status](https://img.shields.io/badge/status-active-7a5c45)
![Jekyll](https://img.shields.io/badge/jekyll-4.3-8b5d45)
![GitHub Pages](https://img.shields.io/badge/deploy-github%20pages-a06b4f)

A Jekyll-based personal portfolio for showcasing projects, writing, and product-minded engineering work.

## Quick Start

```bash
bundle install
bundle exec jekyll serve
bundle exec jekyll build
```

## Project Status

- Live portfolio structure is in place.
- Projects and blog collections are active.
- GitHub Copilot CLI content workflow is now supported through a local MCP server.

## Documentation

- `docs/architecture.md`
- `docs/workflows.md`
- `docs/conventions.md`
- `docs/integrations.md`
- `docs/error-handling-and-logging.md`
- `docs/copilot-mcp-plan.md`

## Repository Structure

```text
.
├── _posts/      # Blog posts
├── _projects/   # Project case studies
├── _layouts/    # Shared layouts
├── assets/      # CSS, JS, and images
├── blog/        # Blog landing page
├── docs/        # Project and integration docs
└── mcp/         # Copilot MCP server and setup scripts
```

## GitHub Copilot CLI Integration

Install the local MCP server entry:

```bash
python mcp/install_copilot_mcp.py
```

Then start Copilot CLI from the repository root and ask it to use the `portfolioSite` MCP server for content changes.

## Contributors

- Thairux

## Roadmap

- Add richer content automation for homepage highlight updates.
- Add local build prerequisites to streamline first-time setup.
- Add CI-based Jekyll verification for portfolio content changes.
