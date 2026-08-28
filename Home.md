---
tags: [project, pytheas, chiron, ai, home]
type: vault-index
updated: 2026-08-27
repos: ["~/code/pytheas", "~/code/chiron", "~/code/jarvis (design-only)"]
---

# Pytheas — Vault Home

Notes for **Pytheas**, Donovan's personal AI assistant, and **Chiron**, the
Odysseus fork that became its workspace shell. Source code lives outside the
vault; this vault holds their architecture, roadmaps, research, generated
output, and operating history. General course content now lives in the Learning
vault.

**[[Architecture/Pytheas and Chiron Project Map]]** is the canonical responsibility map for
the two codebases and their relationship to Obsidian and the planned database.

> [!important] Start here if you're new to this vault
> **[[Operations/Handoff/00 — START HERE|Handoff/]]** — written 2026-08-25 at the Claude
> Code → Codex migration. Identity/context doc, the senior-year workspace plan,
> the course plan, the migration checklist, and a vault cleanup audit.

## Where the code actually lives

| Repo | What it is | State |
|---|---|---|
| `~/code/pytheas` | The Pytheas desktop app (Python). `server.py`, `voice.py`, `courses.py`, `research.py`, `models.py`, `actions.py`, `briefing.py`, `chats.py`, `emailcal.py`, `permissions.py` | **Live and implemented** |
| `~/code/chiron` | Personal fork of Odysseus. Docker, port 7001, ingests the five current vaults. Generic course/classroom interface remains; the SAT test and drill apps were removed 2026-08-26 | **Live and backed up** at private `Corsaya/chiron`; local `dev` tracks `origin/dev` |
| `~/code/jarvis` | The original terminal CLI. Fully architected, never implemented | **Design-only.** Historical |

## Vault structure

- **`Architecture/`** — the canonical project map and capability specifications.
- **`Roadmaps/`** — current build plans. Superseded Jarvis and workspace plans
  live under `Roadmaps/Historical/`.
- **`Operations/`** — handoffs, immutable prompt logs, conversation archives,
  surveys, session wraps, scripts, and the cross-vault atlas.
- **`Generated/Briefings/`** — ISO-dated AI-news output written by
  `~/code/pytheas/briefing.py`.
- **`Incubator/`** — incomplete artifacts that have not earned a permanent
  project location.
- **`learning/Courses/`** — canonical app-managed course content, including SAT,
  Basketball Rules, and the registered Pytheas benchmark. Chiron and Pytheas
  read this configurable location.

## The roadmaps, newest first

- **[[Operations/Handoff/02 — AI Workspace Master Plan]]** (2026-08-25) — **current.** The
  senior-year goal: own workspace + database by June 2027.
- **[[Roadmaps/Historical/Ultimate Workspace Roadmap]]** (2026-08-02) — snapshot. Superseded in
  direction by the above, but its research (CalDAV decision, Notion ruled out)
  is still the reasoning of record.
- **[[Roadmaps/Development Roadmap]]** (2026-07-29) — the four technical workstreams
  (Atlas, environment-context injection, vault-pyramid agents, Hermes). Still
  the live technical plan.
- **[[Roadmaps/perfect-assistant-goals-2026-07-15]]** — the four capability goals and the
  "graduating from Claude" ladder.
- **[[Roadmaps/Historical/capabilities-roadmap]]** · **[[Roadmaps/Historical/jarvis-desk-app]]** · **[[Roadmaps/Historical/Pytheas 2.0 Changelog]]**

## Historical

- **[[Roadmaps/Historical/Summary]]** — a 2026-05-30 snapshot of the *Jarvis design phase*. Kept as
  an artifact; it does not describe the current system.

## Symlinks

- `code/` → `~/code` — the source repos
- `learning-vault/` → `~/Documents/Obsidian/learning`

> [!note] Access
> Full read/write across all five vaults by default since 2026-08-12. The old
> `personal-private` wall is retired. The one override is a doc Donovan marks
> **"locked"**. See `~/Documents/Obsidian/AGENTS.md`.
