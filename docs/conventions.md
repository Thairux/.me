# Conventions

## Content Structure

- Use `layout: default` for main pages.
- Use `layout: project` for files in `_projects/`.
- Use `layout: post` for files in `_posts/`.
- Keep filenames stable and URL-friendly.

## Page Ownership

- `index.md`: homepage messaging and highlights.
- `about.md`: profile narrative and interests.
- `projects.md`: project landing page.
- `blog/index.md`: blog landing page.
- `_projects/*.md`: project case studies.
- `_posts/*.md`: dated blog posts.

## Writing Style

- Keep copy warm, direct, and specific.
- Prefer product-minded language over generic portfolio filler.
- Use short paragraphs and clear headings.
- Preserve existing tone unless the request says to reframe it.

## Frontmatter Rules

### Pages

```yaml
layout: default
title: Home
```

### Projects

```yaml
layout: project
title: "Project Name"
description: "Short summary"
```

### Posts

```yaml
layout: post
title: "Post Title"
date: 2026-03-08 09:00:00 +0000
```

## MCP Editing Rules

- Use `get_content_file` before overwriting an existing content file.
- Use `write_content_file` only for approved content targets.
- Do not use the MCP server for layout, CSS, JavaScript, or non-content repository files.

## Related Files

- `.github/copilot-instructions.md`
- `docs/integrations.md`
- `mcp/portfolio_site_mcp_server.py`
