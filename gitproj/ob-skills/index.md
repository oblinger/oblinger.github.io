---
layout: cayman
title: Dan's Skills
description: Reusable skill modules for Claude Code
permalink: /gitproj/ob-skills/
---

# Dan's Skills

A collection of reusable skill modules for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Each skill defines workflows, conventions, and domain knowledge that Claude Code agents can invoke during interactive sessions.

Skills extend what an AI coding agent can do — from structured development workflows and markdown formatting to product research, Google Workspace integration, and multi-agent role management.

**[View on GitHub](https://github.com/oblinger/ob-skills)**

## Skills

| Skill | Description |
|-------|-------------|
| **CAB** | Common Anchor Blueprint — create, validate, and manage structured folder systems |
| **Dev** | Development workflow — planning, execution, setup, forge, and publish |
| **Edit** | Visual editing — Excalidraw diagrams, mockups, and visual content |
| **Google** | Google Workspace — Sheets and Slides via CLI |
| **MD** | Markdown formatting — heading spacing, file trees, TOCs, dispatch tables |
| **Product** | Product research and purchasing — hunt, compare, buy |
| **Research** | Investigation and synthesis — entity dossiers and topic surveys |
| **Role** | Agent role definitions — persistent identity across sessions |

## How Skills Work

Each skill lives in its own folder with a `SKILL.md` entry point. When a user types `/skill-name action` (e.g., `/dev plan`, `/research dig`), Claude Code reads the corresponding action file and executes the workflow defined there.

Skills are **declarative** (written in markdown, not code), **composable** (they reference each other), and **stateless** (no runtime dependencies).

## License

MIT License. See [LICENSE](https://github.com/oblinger/ob-skills/blob/main/LICENSE) for details.
