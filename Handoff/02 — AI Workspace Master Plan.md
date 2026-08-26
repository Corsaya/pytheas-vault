---
title: AI Workspace Master Plan — Senior Year
date: 2026-08-25
tags: [handoff, roadmap, chiron, odysseus, workspace, senior-year]
deadline: 2027-06 (end of senior year)
status: plan — not started, supersedes nothing
related: ["[[01 — DONOVAN Master Context]]", "[[../Ultimate Workspace Roadmap]]", "[[../Development Roadmap]]"]
---

# AI Workspace Master Plan — finish by end of senior year

**The goal, in his words:** his own AI workspace and database by the end of
senior year — schedule, calendar, courses, notes, journaling, finances, all
contained in his own program. *"Odysseus is great, I just have to make it my own."*

**The deadline is real and it is ~10 months: September 2026 → June 2027.**

---

## 0. The constraint nobody has written down yet

Senior year is the single worst year to attempt a large build, and the plan has
to be honest about that or it will fail the same way the Japanese roadmap did.
The actual calendar:

| Window | What's happening | Build capacity |
|---|---|---|
| **Sept–Oct 2026** | School starts, college applications, fall crew | **Low-medium** |
| **Nov–Dec 2026** | Application deadlines (EA/ED/RD), winter training | **Low**, then winter break spike |
| **Jan–Feb 2027** | Decisions arrive, winter training, semester 2 | **Medium — the real build window** |
| **Mar–Apr 2027** | Spring crew season ramps, AP prep begins | **Low** |
| **May 2027** | AP exams, **SRAA Nationals May 28–29** | **Zero. Assume zero.** |
| **June 2027** | Graduation | Polish only |

**Design consequences, and these are the whole plan:**

1. **Everything must be shippable in one sitting.** No feature that needs three
   consecutive free evenings. He does not have three consecutive free evenings
   between October and June.
2. **The workspace must be useful before it is finished.** If it only pays off at
   100%, it dies at 40%. Every phase below ends with something he actually uses
   daily, or it doesn't ship.
3. **The build must survive May 2027 untouched.** By April 30 it must be
   *done-enough to coast* — no half-migrated data, no "I'll finish this after
   Nationals."
4. **It has to enforce, not just store.** Per Master Context §6, his one real
   failure came from self-directed prep with nothing enforcing it. A workspace
   that is a pretty database is a workspace that loses to procrastination. The
   enforcement layer is not a nice-to-have; it is the reason to build it.

---

## 1. What "make it my own" actually means

Chiron is already a fork of Odysseus (`~/code/chiron`, Docker, port 7001, seven
vaults ingested, custom SAT classroom app). "Making it his own" is four distinct
things that get confused with each other:

| Meaning | Verdict |
|---|---|
| **Own the data model** — one database he controls, not Odysseus's schema by accident | ✅ **Do this. This is the core of the project.** |
| **Own the code** — diverge far enough that it's his program, not a patched fork | ✅ **Do this incrementally**, via a personal layer, not a rewrite |
| **Own the interface** — it looks and works like his tool | ✅ Do this, cheaply, last |
| **Own the model** — run his own LLM | ❌ **Not this year.** That's the separate 4-step ladder in Master Context §9. Attempting it during senior year kills the workspace. |

**The single highest-priority action, before any feature work:**

> ⚠ **Chiron has no personal git remote.** `git remote -v` shows only `upstream`
> pointing at the original Odysseus repo. Four-plus commits of his own work —
> including the entire Bluebook-parity SAT app — exist **only on the local `dev`
> branch on one machine.** One disk failure erases the most sophisticated thing
> he has built. **Create a private GitHub remote and push, today.** Nothing else
> on this list matters if that work evaporates.

---

## 2. The architecture: one database, many faces

The mistake to avoid is building six features that each own their own storage.
The thing that makes it *a workspace* rather than six apps is a single core.

```
                  ┌─────────────────────────────┐
                  │   Obsidian vaults (markdown) │   ← human-editable truth
                  │   6 vaults, per-vault git    │      for notes/journal/courses
                  └──────────────┬───────────────┘
                                 │  two-way sync
                  ┌──────────────▼───────────────┐
                  │      CORE DB (SQLite)        │   ← machine truth for
                  │  entities · events · tasks   │      structured/queryable data
                  │  finances · progress · logs  │
                  └──────────────┬───────────────┘
             ┌───────────────────┼───────────────────┐
             │                   │                   │
     ┌───────▼──────┐   ┌────────▼───────┐   ┌───────▼────────┐
     │ Chiron web   │   │ CalDAV sync    │   │ Agent layer    │
     │ UI (:7001)   │   │ Google/iCloud  │   │ Codex + local  │
     └──────────────┘   └────────────────┘   └────────────────┘
```

**The division of labor, and it is the key design decision:**

- **Markdown owns anything he'd want to read, write, or think in** — notes,
  journal, course content, project docs. It stays in Obsidian, in git, portable,
  and readable in fifty years without his program existing. This is
  non-negotiable and it is also his stated preference: *everything linked to
  Obsidian.*
- **SQLite owns anything he'd want to query, aggregate, or get reminded about** —
  calendar events, tasks, deadlines, training logs, flip P&L, study hours,
  spaced-repetition scheduling. Markdown is a terrible database; stop trying.
- **The sync layer is the actual product.** Events surface *inside* daily notes.
  Training logs written in markdown land in the DB. That bidirectional bridge is
  the thing Odysseus can't do and Notion structurally can't do — and it is
  exactly the gap already identified in the Ultimate Workspace Roadmap.

**Why not Notion (settled, don't relitigate):** Notion Calendar has no developer
API, Notion Mail shut down 2026-09-22, and the data model is closed. Ruled out
structurally, not on preference.

**Calendar protocol (settled):** CalDAV via the `caldav` Python library —
two-way syncs Google, Outlook, and iCloud through one protocol. Odysseus's own
`caldav_sync.py` is the pattern to copy; it was read directly and confirmed.
Open decision he still owes: **which of Google / Outlook / iCloud is day one.**

---

## 3. The phases

Each phase is sized to fit its window and ends in something used daily.

### Phase 0 — Don't lose the work (this week, ~1 hour)
- Private GitHub remote for `~/code/chiron`; push `dev`. **Blocking everything.**
- Same audit for `~/code/pytheas`, `~/code/jarvis`, and the six vault repos —
  confirm each has a live remote and a clean tree.
- Write `AGENTS.md` at the vault root so Codex loads the rules automatically
  (delivered with this handoff — see `04 — Claude Code to Codex Migration`).
- **Done when:** every repo has an off-machine copy.

### Phase 1 — The core DB and the calendar (Sept–Oct 2026)
The calendar goes first because it's the piece with a hard external dependency,
the piece he'll feel every single day, and the piece that makes the workspace
worth opening in the morning.

- Define the core schema. Start deliberately small — `events`, `tasks`,
  `entities`, `logs`. Resist modelling everything on day one.
- CalDAV two-way sync against **one** provider. Pick it and commit.
- **The vault-native piece Odysseus cannot do:** today's events render into the
  daily note in `life/personal-private/Daily/`, and a task written in a daily
  note lands in the DB.
- **Done when:** he checks his own program instead of his phone calendar for a
  full week.

### Phase 2 — Journaling and daily capture (Oct–Nov 2026)
Cheap to build, and it's the data source everything downstream learns from.

- Daily note template pipeline: journal, training log, study hours, one-line
  "what I did by hand that this should have done" (the standing
  needs-discovery question from the interview kit).
- Structured fields extracted to the DB; prose stays in markdown, untouched.
- **The AI never writes journal prose.** Standing anti-goal. It prompts,
  extracts, and summarizes back — it does not author.
- **Done when:** a week of daily notes exists without him thinking about it.

### Phase 3 — The enforcement layer (Nov–Dec 2026) ⭐ the differentiator
This is the phase that justifies the entire project. Per Master Context §1.4
and §6: conditioned immediacy beats backlogs, and self-directed prep with no
enforcement is his single proven failure mode.

- **Surface at the moment of opportunity, not into a backlog.** The system knows
  his schedule (Phase 1) and his patterns (Phase 2), so it interrupts with *this
  specific 20-minute thing, now*, rather than showing a to-do list.
- Deadline pressure made visible: college app dates, AP dates, Nationals,
  JLPT registration, flip drop dates — all on one countdown surface.
- Spaced repetition scheduling backed by the DB (feeds Phase 4 courses).
- **Prep-schedule enforcement**: when he sets himself a prep schedule, the system
  holds him to it and reports the gap honestly. Encourage outward, audit inward.
- **Done when:** it has successfully made him do something he'd have skipped.

### Phase 4 — Courses (Dec 2026 – Feb 2027)
Full spec in `03 — Course Build Plan`. Built on the DB's progress and SRS tables,
not as isolated markdown.
- **Done when:** Japanese Stage 0 is actually finished — katakana done, hiragana
  no longer rusty. That's the honest test, not "the course exists."

### Phase 5 — Finances (Jan–Feb 2027)
- card-flip P&L that tells the truth (per §5 of Master Context, he has not
  profited on singles — the system must never flatter the numbers).
- Ventnor Social hours and tip-out tracking.
- Exact figures stay in `life/personal-private/Private-Reference.md`; the
  AI-accessible vaults keep the structure, not the amounts. **Preserve this
  split** — it's his existing convention and it's a good one.
- **Done when:** he can answer "did card-flip make money this month" in one query.

### Phase 6 — Make it look like his (Feb–Mar 2027)
Deliberately last. Interface work is infinitely expandable and never blocking.
- Strip Odysseus branding; his own name, layout, defaults.
- Atlas fix (full viewport, ResizeObserver, pan/zoom) — already specced in the
  Development Roadmap, still unbuilt, small.
- Kill the features he doesn't use. A fork that deletes is a fork that's his.

### Phase 7 — Freeze (April 30, 2027)
- **Feature freeze.** Bugs only.
- Full backup, documented restore, a written handoff to himself.
- May 2027: AP exams and Nationals. The workspace serves him; he does not serve it.

---

## 4. What to cut, and say so out loud

A senior-year build survives on what it refuses. These are already in the vault
as ideas and should be explicitly parked:

- ❌ **Custom social-media harvesting across IG/X/TikTok using his own logins.**
  Real credential-handling and anti-automation work, genuine account-ban risk,
  and it serves no Phase 1–5 goal. Park it.
- ❌ **Training his own model.** Steps 3–4 of the ladder. Post-graduation.
- ❌ **Meeting transcription.** Nice, unnecessary, not a bottleneck.
- ❌ **Agent/company tree with named sub-agents.** Fun architecture, zero daily value
  until the DB exists. Revisit in Phase 6 if there's slack.
- ⚠️ **Email send.** Read + draft is Phase 5-optional. Full send authority is a
  safety loosening he already flagged as intentional — if built, build it as a
  *new named permission*, never as a silent change to the existing draft-only path.

---

## 5. The five decisions he still owes

Batched, per the standing ask-don't-assume rule:

1. **Which calendar provider is day one** — Google, Outlook, or iCloud?
2. **Chiron fork or clean build?** Recommendation: **stay on the fork**, add a
   personal layer, diverge gradually. A clean build is ~3 months he does not have.
3. **Does the DB live in Chiron's container or beside it?** Recommendation:
   **beside it**, on the host, so the workspace survives him rebuilding or
   abandoning Chiron. The database should outlive the fork.
4. **Which model backs the agent layer** now that the Claude subscription ends —
   GPT-5.6 via API, Codex CLI, local Ollama as the free tier, or a router across
   all three? (The router already exists in Pytheas and is the cheapest answer.)
5. **What's the one thing that, if the workspace did it perfectly, would make
   the other five features optional?** Build that first. His answer, not a guess.
