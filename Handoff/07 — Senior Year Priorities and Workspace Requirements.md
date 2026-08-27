---
title: Senior Year Priorities and Workspace Requirements
date: 2026-08-25
updated: 2026-08-25
tags: [handoff, senior-year, priorities, workspace, google, classroom, fitness]
type: requirements
status: current snapshot — dates and ordering still subject to Donovan's decisions
---

# Senior Year Priorities and Workspace Requirements

This is the current input to the workspace design. It records Donovan's stated
priorities and constraints without turning them into a schedule. Donovan owns
ordering decisions when priorities conflict and will supply more exact school
dates later.

## Current priorities

1. **Finish summer work.** Read *The Kite Runner*, *In Cold Blood*, and *Night*
   before the third week of school; complete the AP Calculus and AP Physics
   packets before September 14. Confirm exact reading deadline later.
2. **Track fitness and build consistent habits toward crew goals.** A fitness
   watch is acceptable if it produces useful, exportable data. Log exercise in
   the workspace as that system is developed.
3. **SAT, conditionally.** If the latest score is unsatisfying and improvement
   before October 3 is realistic, take it one final time.
4. **Complete the college essay.** This may move ahead of fitness or SAT when
   application pressure requires it.
5. **Apply to the selected colleges.** The college list and deadlines remain to
   be supplied.
6. **Make the most of senior year.** Continue developing the workspace and
   potentially begin a YouTube channel documenting the Corsaya lifestyle.
7. **Hobbies.** Current named hobbies are Super Smash Bros. Melee and the
   Minecraft modpack TerraFirmaGreg.

## Information architecture rule

Top-level areas must represent durable, substantial domains—not every output
type or generator. A large domain such as School should not sit conceptually
beside a flat folder of low-quality generated briefings as though they have
equal importance.

A note, folder, database view, or automation earns a permanent place only when
it has enough useful data, a repeatable input, or a clear ongoing function.
Small and incomplete experiments stay in an incubator or project area until
they meet that threshold. Low-quality generated output is archived beneath the
system that produced it; it does not become a first-class knowledge domain.

## Proposed durable domains

| Domain | Examples of substantial systems |
|---|---|
| School and college | Subjects, assignments, readings, grade/progress data, college essay, applications |
| Health and performance | Crew training, workouts, recovery, sleep, fitness-device imports |
| Knowledge and learning | Japanese, durable research, courses, reference notes |
| Projects and engineering | Chiron, Pytheas, Minecraft event, future software and physical builds |
| Life and reflection | Daily capture, encrypted journal, private reference, experiences |
| Finance and work | Employment, card-flip, trading, budgets and structured records |
| Creative and public work | Corsaya/YouTube, documentation, portfolio outputs |

Briefings, prompts, imports, session wraps, and generated reports are supporting
collections inside these domains, not peer domains themselves.

## Google-account integration goal

Chiron should act like a personal Notion-style workspace connected to multiple
Google accounts, including a school-managed account, while keeping the data in
Donovan's workspace.

Required design:

- Connect each Google identity separately through OAuth.
- Maintain separate tokens, granted scopes, sync cursors, provenance, and a
  one-click disconnect for every account.
- Start with read-only access for Gmail, Calendar, Classroom, and Drive metadata.
- Import Classroom courses, topics, coursework, materials, due dates, and the
  requesting student's permitted submission state.
- Preserve source account and source URL on every imported record.
- Merge calendars into one view without merging account ownership.
- Deduplicate the same event or attachment when it appears through multiple
  Google services.
- Never assume a school domain permits an API or scope; display denial clearly
  and degrade to supported feeds or manual import.
- Add write access only as named, separately approved capabilities such as
  create calendar event or save draft—not a blanket Google-write switch.

## Document system goal

Use LibreOffice as the owned/local counterpart to Google Workspace:

- Google Docs ↔ LibreOffice Writer (`.odt`, with `.docx` interchange where needed)
- Google Sheets ↔ LibreOffice Calc (`.ods`, with `.xlsx` interchange where needed)
- Google Slides ↔ LibreOffice Impress (`.odp`, with `.pptx` interchange where needed)

Obsidian notes describe and link the work. LibreOffice owns complex documents.
SQLite owns structured status and history. Chiron provides one interface and
launches or previews the appropriate artifact.

## Journal lock requirement

The journal must be unreadable to Chiron and AI agents while still supporting
explicit management operations such as list, move, duplicate, and delete.
Relying only on a written instruction is insufficient.

Proposed boundary:

1. Store journal content encrypted at rest outside Chiron's index roots.
2. Give entries opaque IDs plus a minimal non-content metadata catalog.
3. Expose management through a narrow broker that implements only list, move,
   copy, and delete; it has no read-content operation.
4. Require explicit confirmation for delete.
5. Let Donovan unlock the journal directly for reading/writing in Obsidian,
   without granting the agent access to the decrypted mount.

## Consistent-output rule

Every recurring system needs:

1. A defined input or capture trigger.
2. A template or schema.
3. A reliable storage destination.
4. A review surface that is actually revisited.
5. An archive/retention rule.
6. A measurable definition of a useful output.

If those six pieces are absent, do not automate the output yet.
