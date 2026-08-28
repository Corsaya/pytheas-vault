---
title: Pytheas and Chiron Project Map
date: 2026-08-25
updated: 2026-08-27
tags: [pytheas, chiron, architecture, project-map]
type: project-map
status: current
---

# Pytheas and Chiron Project Map

This note defines which part of the personal AI system owns what. It is the
canonical naming and responsibility map; detailed implementation plans remain
in the roadmaps and handoff documents.

## System map

| Layer | Canonical component | Responsibility |
|---|---|---|
| Durable knowledge | Obsidian vaults | Notes, journal, courses, research, project documentation, and other human-readable truth; general courses live in `learning/Courses/` |
| Workspace shell | Chiron (`~/code/chiron`) | Primary web interface, multi-vault ingestion, chat, agents, documents, calendar, classroom, and workspace services |
| Native capability lab | Pytheas (`~/code/pytheas`) | Smaller local-first desktop assistant, voice, computer actions, briefings, and focused experiments |
| Structured data | Host-side SQLite database (planned) | Events, tasks, progress, training logs, finance records, and other queryable state |
| External accounts | Per-account Google Workspace connectors (planned) | Read authorized school/personal mail, calendars, Classroom coursework, and Drive metadata through narrowly scoped OAuth grants |
| Historical predecessor | Jarvis (`~/code/jarvis`) | Original design and experiments; not an active competing product |

## Direction of travel

1. **Protect Chiron first.** It contains the most substantial custom workspace
   work and must always have an off-machine private remote.
2. **Build daily-use workspace features in Chiron.** Do not duplicate them in
   Pytheas unless the native desktop boundary is the reason for the feature.
3. **Use Pytheas for focused local capabilities.** Successful experiments can
   later become Chiron services or remain lightweight companions.
4. **Keep authored knowledge in Markdown.** Chiron may index, render, and edit
   it, but the database must not become the only readable copy.
5. **Keep aggregate state out of Markdown.** SQLite should own records that need
   filtering, calculations, reminders, or synchronization.
6. **Treat each external account as a separate trust boundary.** School and
   personal Google accounts receive separate tokens, scopes, sync state, and
   revocation controls. Start read-only and add write permissions capability by
   capability, never as one blanket Google connection.

## Canonical repositories

| Repository | Role | State |
|---|---|---|
| `Corsaya/chiron` | Flagship personal workspace | Active, private |
| `Corsaya/pytheas` | Native assistant and capability lab | Active, private |
| `Corsaya/pytheas-vault` | Project knowledge, roadmaps, operations, and generated briefings | Active, private |
| `Corsaya/jarvis` | Historical predecessor | Preserve until unique work is audited; then archive |

## Decision rule

When a new feature could live in multiple places:

- Put it in **Chiron** when it depends on the unified workspace, database,
  browser UI, or multiple vaults.
- Put it in **Pytheas** when it is a small native/local capability, computer
  action, voice interaction, or isolated experiment.
- Put its durable explanation in **Obsidian**.
- Put its structured records in **SQLite**.

## Related

- [[../Operations/Handoff/02 — AI Workspace Master Plan]]
- [[../Roadmaps/Development Roadmap]]
- [[../Roadmaps/Historical/Pytheas 2.0 Changelog]]
- [[Home]]
