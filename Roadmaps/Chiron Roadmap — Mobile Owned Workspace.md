---
title: Chiron Roadmap — Mobile Owned Workspace
date: 2026-08-26
tags: [chiron, pytheas, roadmap, mega-prompt, mobile, workspace, obsidian]
status: draft — implementation waits for vault/repository/code cleanup
related:
  - "[[../Architecture/Pytheas and Chiron Project Map]]"
  - "[[../Operations/Handoff/02 — AI Workspace Master Plan]]"
  - "[[../Operations/Handoff/07 — Senior Year Priorities and Workspace Requirements]]"
---

# Chiron Roadmap — Mobile Owned Workspace

## Starting constraint

Implementation begins only after Donovan's planned cleanup and reorganization
of the Obsidian vaults, GitHub repositories, and `~/code` directory. Until then,
this document is planning material, not authorization to restructure them.

## Permanent division of responsibility

| Component | Responsibility |
|---|---|
| **Obsidian** | Durable human-readable knowledge: notes, school materials, project documentation, and journal ciphertext |
| **Chiron** | Main workspace interface: dashboard, search, calendar, assignments, documents, connectors, and mobile access |
| **Host-side SQLite** | Structured operational state: tasks, deadlines, accounts, logs, knowledge progress, and fitness data |
| **Pytheas** | Small experimental capability laboratory: voice, local actions, model routing, and prototypes |
| **Codex/models** | Replaceable reasoning layer; never the sole owner of information |

The core architectural decision is that **Chiron becomes the product and
Pytheas becomes its experimental workshop**. They should not remain competing
workspace applications.

## Phase 0 — Establish the truth

- Produce a current feature inventory for Pytheas and Chiron.
- Mark each feature working, partial, stale, or inherited-but-unused.
- Correct documentation claiming Chiron still contains the removed SAT apps.
- Establish how personal Chiron commits remain separate from upstream Odysseus.
- Record minimum test, startup, backup, and restore commands.
- Decide which Pytheas capabilities deserve migration into Chiron.
- Do not migrate a capability merely because it exists.

**Done when:** one authoritative architecture/status document matches the
current code and commit history.

## Phase 1 — Secure data foundation

Build the host-side database before another interface feature. Start with:

- `accounts`
- `connectors`
- `events`
- `tasks`
- `artifacts`
- `courses`
- `knowledge_state`
- `fitness_activities`
- `sync_runs`
- `audit_log`

Requirements:

- The database lives outside Chiron's container.
- Backups are automatic and restoration is tested.
- Every imported object records its source account and external identifier.
- Secrets live in an OS keyring or restricted secret store, never Obsidian or
  ordinary SQLite fields.
- Schema migrations are versioned and tested.

**Done when:** Chiron can be rebuilt without losing its structured state.

## Phase 2 — Mobile-ready daily cockpit

Build the smallest useful daily interface:

- Today's events
- Deadlines
- Three current priorities
- School assignments
- Quick capture
- Recently used project files
- Fitness summary
- Connector health
- An inbox of unprocessed information

Make Chiron a responsive installable PWA suitable for a future GrapheneOS
phone. Initial remote access goes through a private WireGuard/Tailscale-style
network, not an openly exposed home server.

**Done when:** Chiron is genuinely useful from a phone away from home.

## Phase 3 — Accounts and connectors

Treat every identity as a separate connector:

- Personal Google
- School Google
- Future college Google or Microsoft account
- Independent mail/calendar account
- GitHub
- Garmin later

Each connector receives separate tokens, explicit scopes, read-only access
first, sync timestamps, revocation controls, visible errors, and provenance.
Start with calendars and assignments. External writes come later.

**Done when:** Chiron shows information from multiple accounts without merging
their identities or permissions.

## Phase 4 — School workspace

Reproduce the useful workflow of Google Classroom, not Google itself:

- Course and subject dashboards
- Assignments and due dates
- Materials and attachments
- Submission-status tracking
- Teacher announcements
- Links to the authoritative school service

Use LibreOffice Writer, Calc, and Impress locally. Prefer `.odt`, `.ods`, and
`.odp`; generate PDF submission snapshots; use Microsoft formats only when
compatibility requires them. Consider Collabora only if browser editing proves
worth operating.

**Done when:** one subject completes a full assignment cycle through Chiron
before expanding to every class.

## Phase 5 — Obsidian bridge

- Approved Markdown task syntax writes structured tasks to SQLite.
- Calendar events appear in daily notes.
- Project dashboards link to relevant notes.
- Search returns structured records and vault documents.
- Generated notes declare source and generation time.
- Small captures enter an inbox instead of becoming premature permanent notes.

A permanent note should normally have a clear title, a one-sentence purpose,
source/provenance, one meaningful link, and enough content to support a future
action, decision, or retrieval.

**Done when:** Obsidian and Chiron no longer behave like separate systems.

## Phase 6 — Fitness and crew

- Import Garmin FIT/TCX exports.
- Store measurements in SQLite and reflections in Markdown.
- Track rowing, erg tests, exercises, and coach-provided plans.
- Compare scheduled and completed training.
- Produce trends without inventing medical, weight-cut, or coaching decisions.

**Done when:** Donovan owns a useful training history independent of Garmin.

## Phase 7 — Private journal broker

Use an encrypted store with two interfaces:

- Metadata: list, move, duplicate, rename, delete, and back up.
- Content: unavailable to Chiron and AI unless Donovan deliberately unlocks a
  specific entry.

Chiron should not continuously hold the decryption key.

**Done when:** Chiron can manage journal objects without reading their content.

## Phase 8 — Retrieval and controlled agents

- Hybrid lexical and semantic search
- Related-note recommendations
- Project context packages
- Source citations for recalled facts
- Per-project agent permissions
- Draft-before-action workflow
- Audit log for external writes
- Mobile approval queue

Retrieve the minimum relevant material instead of injecting the whole vault.

**Done when:** questions such as “What is blocking Chiron?” and “What is due for
AP Physics?” return sourced, current answers.

## Phase 9 — Expansion

Only after daily use validates the foundation:

- Email triage and drafting
- Calendar writeback
- College-application workspace
- YouTube production pipeline
- Course/SRS engine
- Local voice control
- Advanced automations
- Optional local-model routing

## Immediate build order after cleanup

1. Finish the source and documentation audit.
2. Declare Chiron the workspace and Pytheas the capability lab.
3. Create the host-side database and tested backups.
4. Build the mobile daily cockpit.
5. Connect one calendar account read-only.
6. Connect one school account read-only.
7. Implement one complete school subject.
8. Build the Obsidian task/event bridge.
9. Use it for two weeks before expanding.

## First proof of usefulness

> For fourteen consecutive days, Chiron shows the correct schedule, deadlines,
> and three current priorities on both computer and phone without manual
> duplication.

That proof matters more than copying every Notion, Classroom, Docs, Sheets, or
Slides screen.
