---
title: Chiron Delivery Roadmap
date: 2026-09-01
deadline: 2027-04-30
tags: [chiron, roadmap, senior-year, calendar, workspace]
status: active
---

# Chiron Delivery Roadmap

## Operating rule

Chiron is a senior-year project, not a second full-time job. Each milestone must fit in one sitting and leave a piece that is used immediately. No parallel rewrite, no new general-purpose task system, and no “AI company” architecture until the daily workspace works.

The fork already has SQLite, calendar routes/CalDAV code, tasks, and a generic Classroom UI. The first job is therefore **verification and a thin personal layer**, not rebuilding capabilities that may already exist.

## Definition of done for the workspace

For fourteen consecutive days, Chiron shows the correct schedule, the next deadlines, and three current priorities on computer and phone without manual duplication. It may not read journal prose. Its first useful behavior is surfacing the right next action at the actual open window.

## Decisions due before implementation

These are Donovan decisions; the roadmap does not silently choose them.

1. Day-one calendar provider: Google, Outlook, or iCloud.
2. Core database location: host-side data directory or Chiron container. Current recommendation remains host-side.
3. The one behavior that would make Chiron worth opening daily. Current working candidate: **today’s schedule, deadlines, and next action in one view**.
4. Agent/model default: router, GPT API, Codex CLI, or local Ollama. This does not block the calendar slice, so defer it unless needed.

## Delivery schedule

| Window | Deliverable | Verification / exit rule |
|---|---|---|
| Sep 2026 | Baseline, decisions, and calendar-spike evidence | Current `dev` branch runs; existing calendar routes/data model are mapped; one chosen provider can be tested without writing production data |
| Oct 2026 | Calendar vertical slice | One provider syncs to Chiron; a Today view shows events, deadlines, and three priorities; use it for seven days |
| Nov 2026 | Daily capture and vault bridge | A daily-note task/event can enter structured storage without consuming journal prose; one week of real daily use |
| Dec 2026 | Enforcement v1 | A chosen prep plan is surfaced in a real open window and completion/miss is visible; no generic nagging system |
| Jan 2027 | Courses v1 | Japanese progress and one active school subject are tracked through the DB without replacing their markdown truth |
| Feb 2027 | Finances v1 + personal layer | One truthful card-flip/work-income query; remove unused upstream surface and establish Chiron defaults/identity |
| Mar 2027 | Reliability and interface polish | Restore procedure is tested; phone/desktop Today view is reliable; UI polish only after the data path works |
| Apr 1–30, 2027 | Freeze | Back up, document restore, fix bugs only; no feature work after April 30 |
| May–Jun 2027 | Coast and handoff | Chiron serves APs, crew, graduation, and Japan preparation; only urgent fixes and final documentation |

## September: three-hour discovery sprint

September contains school start, summer-work completion, crew, work, Japanese, and Falco. Its Chiron allocation is intentionally small: **three 45–90 minute blocks**, with no production feature expected.

| Date | Block | Deliverable |
|---|---|---|
| Mon Sep 7 | 90 min | Write the four decisions above, run Chiron on `dev`, record the exact launch/test command, and create a one-page current-system map: calendar routes, database models, and current data directory |
| Mon Sep 21 | 45 min | Read the existing calendar route/sync path end-to-end. Record what already works, the one missing link to the selected provider, and the smallest October vertical slice |
| Sun Sep 27 | 45 min | Make the provider spike: use a disposable/test calendar, confirm read-only import or document the exact authentication blocker. Do not connect school/private production calendars yet |
| Mon Sep 28 | 45 min | Write the October implementation ticket list, each independently shippable in 45–90 minutes; choose the first ticket and its automated/manual acceptance check |

If the provider decision is not made by September 7, the later three blocks become documentation only. Do not write calendar integration against an imaginary provider.

## October ticket order

1. Preserve a clean database/config backup and a one-command test/launch procedure.
2. Make one-provider calendar import visible in the existing calendar UI.
3. Add/read only the minimal fields needed for a Today query: start, end, source, title, URL, and owner.
4. Build the Today view: today’s events, upcoming deadlines, and three manually chosen priorities.
5. Use it for seven days; log every manual duplication or incorrect event before adding another feature.

## Explicitly parked

- custom social-media harvesting;
- custom model training;
- meeting transcription;
- broad agent/sub-agent framework;
- full email-send authority;
- a clean-room Chiron rewrite.

These are not September work and cannot borrow time from the calendar vertical slice.
