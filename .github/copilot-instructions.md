# Copilot Instructions For This Portfolio

This repository is a Jekyll portfolio site.

Prefer scoped content updates over broad layout changes.

Use the local `portfolioSite` MCP server when the request is about changing site content.

Treat these files as the primary editable content surfaces:

- `index.md` for homepage copy and highlight sections.
- `about.md` for biography and interests.
- `projects.md` for the projects landing page.
- `blog/index.md` for the blog landing page.
- `_projects/*.md` for individual project case studies.
- `_posts/*.md` for dated blog posts.

Do not edit `_layouts/`, `assets/css/`, or `assets/js/` unless the request is explicitly about design or behavior changes.

For content work, follow this workflow:

1. Use `get_site_content_map` or `list_content_files` to identify the right target.
2. Use `get_content_file` before overwriting an existing file.
3. Use `write_content_file` only for allowed content files.
4. Use `build_site` after content changes when available.

Preserve frontmatter conventions:

- Pages use `layout: default`.
- Project entries use `layout: project` and should include `title` and `description`.
- Blog posts use `layout: post` and should include `title` and `date`.

Keep copy warm, concise, and product-minded. Avoid generic filler text.
