---
layout: post
title: "Using GitHub Copilot CLI to Maintain This Portfolio"
date: 2026-03-08 09:00:00 +0000
author: "Thairux"
permalink: /github-copilot-cli-portfolio-workflow/
---

If I want GitHub Copilot to help maintain this portfolio from the command line, the safest workflow is not "let it change everything automatically." The better approach is to let it inspect the repo, help build a plan, suggest commands, and then make targeted changes that I still review.

## 1. Install GitHub Copilot CLI

Current GitHub documentation points to the standalone Copilot CLI installation flow rather than the older GitHub CLI extension setup.

### Install with npm

```bash
npm install -g @github/copilot
```

### Install with Homebrew

```bash
brew install copilot-cli
```

### Install with WinGet

```powershell
winget install GitHub.Copilot
```

## 2. Log in on first launch

Start Copilot from your terminal:

```bash
copilot
```

If you are not already authenticated, use:

```text
/login
```

and complete the sign-in flow.

## 3. Use it interactively first

The best first step is to open an interactive session and give it context about the site:

```bash
copilot
```

Then ask something like:

```text
Review this Jekyll portfolio and tell me which files control the homepage, footer, blog index, and project pages.
```

This is a good way to make sure Copilot understands the structure before asking it to update anything.

## 4. Switch to plan mode before edits

Copilot CLI supports plan mode. In interactive mode, press:

```text
Shift+Tab
```

That lets you collaborate on an implementation plan before changes are made.

For this portfolio, a good plan-mode prompt would be:

```text
Plan the changes needed to add a new project, write a related blog post, update the homepage highlights, and keep all links working.
```

## 5. Good prompts for this site

Here are the kinds of prompts that fit this repository well:

### Add a project

```text
Add a new project to this portfolio, create a case-study page in the projects collection, and update the projects page if needed.
```

### Add a blog post

```text
Write a new blog post for this portfolio based on my notes and make sure it appears correctly in the blog index.
```

### Refresh the homepage

```text
Improve the homepage highlights so the latest post, selected projects, and contact section feel more relevant to a developer portfolio.
```

### Audit links

```text
Check this site for broken links, duplicate routes, and inconsistent trailing slash behavior.
```

## 6. Use single-prompt mode for focused tasks

For one-off tasks, Copilot CLI also supports prompt-based execution:

```bash
copilot --prompt "Summarize this portfolio repository and suggest the next three content improvements."
```

For focused automation, you can also allow specific tools when your environment supports that:

```bash
copilot --prompt "Review this repo and suggest homepage copy improvements." --allow-tool 'shell(git)'
```

The exact tool permissions depend on the environment you run Copilot in, so it is better to start narrow and explicit.

## 7. Keep the workflow safe

The safest pattern for a personal site looks like this:

1. Ask Copilot to inspect the repo
2. Use plan mode before file edits
3. Make one logical change at a time
4. Review the diff
5. Run the site locally or inspect the generated output
6. Commit only after the route and content checks look correct

For a portfolio repo, this matters because content updates can easily create broken links, duplicate pages, or route conflicts if changes are made too broadly.

## 8. What to ask Copilot to check after edits

After a content or design change, I would usually ask it to confirm:

- homepage links still resolve
- blog index points to real posts
- project cards match project detail pages
- footer and contact links still use the latest social URLs
- favicon and shared assets still load under the GitHub Pages base path

## 9. Where Copilot CLI helps most here

For this portfolio, Copilot CLI is most useful for:

- writing first drafts for blog posts
- turning notes into cleaner project summaries
- tracing which files control a section of the site
- generating a plan before touching layouts or CSS
- auditing routes, links, and content consistency

It is less useful when used as an unchecked "edit everything" tool. The best results come from scoped prompts, reviewable diffs, and a workflow that treats Copilot as a collaborator rather than an autopilot.
