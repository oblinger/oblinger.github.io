---
description: "Dan's personal website, oblinger.github.io: the live site, its per-project pages, and how it deploys"
---

| -[[WEB]]-              | : Website — Dan's personal website, oblinger.github.io: the live site, its per-project pages, and how it deploys<br>→ [WEB](ha://p/WEB)  (kmr/SYS/Bespoke/Website)                                                                                         |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Website                | [🌐 Home](https://oblinger.github.io/)  ·  [Projects index](https://oblinger.github.io/gitproj/)  ·  [Repo](https://github.com/oblinger/oblinger.github.io)  ·  [Elsewhere](https://oblinger.github.io/elsewhere/)  ·  Src `~/ob/grove/oblinger.github.io/` |
| WEB links              | ~~[Web Public](ha://Web/Web%20Public)~~ ([Drive](https://drive.google.com/drive/folders/1asHv4t89nzMF0nCyz0uL6sneQ4mR2d5z))                                                                                                                                |
|                        |                                                                                                                                                                                                                                                            |
| Hook Anchor            | Src `~/ob/proj/Hook Anchor/`  →  [live page](https://oblinger.github.io/gitproj/HookAnchor/)  ·  ~~[[Hook Anchor]]~~                                                                                                                                       |
| Dan's Skills           | Src `~/.claude/skills/`  →  [live page](https://oblinger.github.io/gitproj/dans-anchor-system/)  ·  [[DAS Skills\|dans-anchor-system]]                                                                                                                     |
| Alien Biology          | Src `~/ob/proj/abio/`  →  [live page](https://oblinger.github.io/gitproj/AlienBiology)  ·  [[ABIO]]                                                                                                                                                        |
| Deliberative Coherence | Src `oblinger.github.io/gitproj/DeliberativeCoherence/*.qmd` (Quarto, in-repo)  →  [live page](https://oblinger.github.io/gitproj/DeliberativeCoherence)  ·  [[DCP]]                                                                                       |
| ASI Outcomes           | Src `oblinger.github.io/ASIO/` (in-repo)  →  [live page](https://oblinger.github.io/ASIO/ASI_Outcomes/)  ·  [[ASIO]]                                                                                                                                       |
| [[MYWEB]]              | dev / local-Jekyll / hosting notes                                                                                                                                                                                                                         |
| ...                    | [[Web Hooks\|Hooks]],  [[WSITE]],                                                                                                                                                                                                                          |

# WEB
Dispatch surface for the personal website published at https://oblinger.github.io/ — the live site, its per-project pages, and the deploy setup.

| Card |  |
| --- | --- |
| **Engine** | Jekyll + jekyll-theme-cayman · GitHub Pages auto-deploys on `git push` |
| **Deploy** | **Full topology + copy mechanisms at [[WIRE Website Deploy]].** Summary: HookAnchor / AlienBio: `just docs-deploy` in the project repo · Skills: `git push` from `~/.claude/skills/` · Quarto DCP: `just publish-dcl` · KM homepage: `km_github.py` in [[KM]] |


# BRIEF

The anchor page for the personal Jekyll website published at https://oblinger.github.io/ — a pointer + dispatch surface, not the site source. Slug **WEB**.

- **This is an anchor page**, not the website source — wiki-links + `hook://` URIs + external URLs only; not published. The Jekyll site source lives at `/Users/oblinger/ob/grove/oblinger.github.io/`, reached here via the `oblinger.github.io` symlink.
- **The `Website` row is the live site** — Home is the top page; Projects index lists everything published under `gitproj/`. The project rows below it each pair the **live page** with its **vault anchor** (the project's home in the knowledge repo).
- **Key projects are the published `gitproj/<project>/` pages** — Hook Anchor, Dan's Skills (dans-anchor-system), Alien Biology, Deliberative Coherence, ASI Outcomes. Each project repo populates its own `gitproj/<name>/` subdir; add a row here when a new project goes live.
- **Deploy discipline**: GitHub Pages auto-builds on `git push` from the `oblinger.github.io/` repo. Per-project doc sites deploy via `just docs-deploy` in that project's repo. No `/publish` skill flow — the deploy IS the push.
- **Code + per-project setup** live in `Bespoke/Website/CLAUDE.md` (Jekyll layouts `blank` vs `cayman`, the `gitproj/<project>/` populate mechanism) — read it before editing site code.
- **Web Public = Drive `Oblio/GShare`** (hook in [[Web Hooks]], local path via Google Drive for desktop). The folder is owner-only by design; each file is shared on its own as anyone-with-link/viewer, not searchable — see the `gshare` skill. Added 2026-09-25 at Dan's ask.
- **Don't pile per-project detail into this file** — it is the entry point. Dev/local-hosting notes live in [[MYWEB]]; each project's detail lives in its own anchor.
