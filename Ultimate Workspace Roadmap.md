---
tags: [pytheas, roadmap, courses, sat, ai-prompting, coding, notion-parity, social-automation, mega-prompt]
created: 2026-08-02
status: draft — pending clarifying answers
source: "[[Prompts/2026-08-02 Mega Prompt — Ultimate Workspace Vision]]"
related: ["[[Development Roadmap]]", "[[capabilities-roadmap]]", "[[../ai-improvement/needs-wants-interview-kit]]"]
---

# Ultimate Workspace Roadmap

Structured breakdown of the [[Prompts/2026-08-02 Mega Prompt — Ultimate Workspace Vision|2026-08-02 mega prompt]],
mapped against what's already planned in [[Development Roadmap]] (workstreams
1–4: Atlas, environment-context injection, vault-pyramid agents, Hermes).
This doc only adds what's *new* — it doesn't restate the existing plan.

## Deadline note
SAT: **21 days out as of 2026-08-01** (so ~19 days as of this writing).
Recommendation: build the SAT course track now, in parallel with Pytheas
capability testing, rather than sequencing it after — see "Sequencing"
below.

## Decisions confirmed 2026-08-02

- **SAT sequencing:** strict, as originally stated — no SAT course work
  starts until Pytheas capability testing is to Donovan's standard. Risk
  accepted: this can compress the ~19 remaining days.
- **Hermes autonomy split:** read-only actions (open notes/links, view
  windows, screenshots, read files) run without confirmation; anything
  mutating state (shell commands, file write/delete, opening arbitrary
  apps, sending messages/emails) stays confirm-gated. Matches
  `Development Roadmap.md` workstream 4's existing design — no change
  needed there, just confirms the split.
- **Social-media harvesting:** custom build, not `last30days` — across
  IG/X/TikTok, using Donovan's own account logins (not anonymous/public
  pulls) to reach more content. **Not started, and not buildable from this
  vault session** — this is a real coding project (credential handling +
  platform automation, likely Playwright+stealth similar to the existing
  `card-flip/drop-monitor/target_alert.py` pattern) that belongs in
  `~/code/pytheas` or a dedicated scraper module, with its own security
  pass: credentials must never live in a vault markdown file — OS
  keyring/env-file pattern only, same as existing card-flip venv secrets.
  IG and TikTok both have aggressive anti-automation detection; logging in
  as Donovan risks account action (rate-limit/lockout) — worth designing
  conservative pacing from the start, not just functionality.
- **Credential storage:** local `.env` file, gitignored, same pattern as
  the existing card-flip venv secrets — never committed, never written into
  any vault markdown.

## Priorities confirmed 2026-08-02 (post-comparison research)

Source: [[Prompts/2026-08-02 Notion vs Odysseus vs Pytheas Comparison]].
Odysseus installed hands-on (`~/code/odysseus`, `docker compose up -d
--build`, `http://localhost:7000`) for direct testing rather than
spec-reading only. Live and connected to local Ollama (`qwen3:8b`,
`gemma:2b` — same models Pytheas uses) as of 2026-08-02.

**Setup notes for next time (Docker + host Ollama on this machine):**
- Admin login is auto-seeded on first boot — temp password is printed in
  `docker logs odysseus-odysseus-1` (search "Temporary password"), not
  shown in the UI. Change it immediately after first login.
- Host Ollama was bound to `127.0.0.1` only — Docker containers couldn't
  reach it. Fixed via a systemd drop-in
  (`/etc/systemd/system/ollama.service.d/override.conf`, `OLLAMA_HOST=0.0.0.0:11434`)
  + `systemctl daemon-reload && systemctl restart ollama`.
- ufw (active, default-deny incoming) needed an explicit allow rule
  scoped to the **Compose network's actual subnet**, not the default
  Docker bridge — Compose creates its own network per-project
  (`odysseus_default`, `172.18.0.0/16` here), not `docker0`'s
  `172.17.0.0/16`. Check with `docker network inspect <project>_default`
  before writing the ufw rule. Rule used: `ufw allow from 172.18.0.0/16 to
  any port 11434 proto tcp` — scoped to the container network only, not
  LAN/internet-wide.

Confirmed build priorities, in the order they'll be
tackled once SAT prep is done (strict sequencing still holds):

1. **Deep Research + Compare** (from Odysseus) — a dedicated multi-step
   research/report feature distinct from the briefing pipeline, plus a
   blind side-by-side model-comparison tool. Directly serves the
   multi-model testing goal from the original mega-prompt.
2. **Scheduled/autonomous Custom Agents** (from Notion) — background jobs
   on a schedule or trigger, not just per-conversation agent-mode. Natural
   fit: auto-refresh courses, auto-check SAT progress, not just the
   existing fixed daily-briefing timer.
3. **Full email send + two-way calendar sync** (from Odysseus) — **note:**
   this deliberately loosens Pytheas's current draft-only-send /
   read-only-calendar safety design. Confirmed as an intentional choice,
   not an oversight to fix. Build it as a new, explicitly-named permission
   (not a silent change to `email.send`'s current meaning), so the safer
   draft-only mode stays available/default.
4. **Courses generation — test, don't assume it works.** Before building
   anything new here, run an actual end-to-end test: drag SAT-prep and
   coding-history material into a course, generate podcast/study
   guide/quiz, confirm output quality. This gates the SAT/coding/AI-prompting
   course tracks from the original mega-prompt.
5. **API integration for models, Gemini first.** Pytheas already has an
   "add OpenAI/Gemini/Anthropic API key" provider slot
   (`Pytheas 2.0 Changelog.md`, 2026-07-24). Priority: verify Gemini works
   end-to-end, since **NotebookLM (Google) is the actual engine behind the
   Courses feature** — Gemini-family API access and NotebookLM API access
   are two different Google surfaces (a plain Gemini API key does not
   grant NotebookLM access); confirm which one Pytheas's `courses.py`
   actually calls today before assuming the two are the same credential.
   Relevant: the `notebooklm` skill (full programmatic NotebookLM API —
   notebooks, sources, all artifact types) is available in this Claude Code
   session and should be cross-checked against however `courses.py`
   currently talks to NotebookLM.

## New workstreams this prompt adds

### 5. Prompt-logging convention (this file + the Prompts/ folder are the pilot)
- Every future prompt gets saved as a file in the vault it relates to, in a
  `Prompts/` subfolder, tagged automatically, with **AI usage** (model/tool)
  and **result** recorded in the same file — established by this session's
  two new files.
- Roadmap to extend to other vaults: `learning/Prompts/`,
  `ai-improvement/Prompts/`, `finance/Prompts/`, `card-flip/Prompts/` —
  **not** `personal-private/` (writes stay hook-blocked there except the
  Health allowlist).
- Open question: should this be manual (Claude writes the file each time,
  as done here) or built into Pytheas itself (auto-log every chat turn to
  the relevant vault)? The latter is a Hermes/environment-context feature,
  not a vault-side one — belongs in `Development Roadmap.md` workstream 4
  once Hermes exists.

### 6. Courses — three self-teaching tracks
Location: `pytheas/Courses/` (existing folder, currently has Basketball
Rules as its only content — first real use of the Courses feature).

1. **"How Pytheas Was Built"** — a course version of the actual build
   history: this vault's session-wraps, the `Development Roadmap.md`
   workstreams, and the `~/code/pytheas` git log/CHANGELOG, restructured as
   a learn-to-code-by-example course rather than raw changelog entries.
   Goal per Donovan's closing note: teach him to build similar things
   *without* AI generating it for him.
2. **SAT** — diagnostic first (where the 1310 is weak), then a 21-day (now
   ~19-day) study plan. This doesn't need Hermes or multi-model — usable
   today with whatever course-generation Pytheas already has.
3. **AI Prompting & Behavior** — start from
   [[../ai-improvement/needs-wants-interview-kit|needs-wants-interview-kit]]
   as the intake interview, use `ai-improvement/` as the knowledge bank.
   Goal: Pytheas builds an actual model of what Donovan does/doesn't know
   (a "knowledge map"), not just a course playlist — this is the piece that
   makes Pytheas able to *help him reach goals* rather than just answer
   questions.

**Open question:** does course content get generated fresh each session, or
does Pytheas need a persistent "what Donovan already knows" store that
courses update? The mega-prompt implies the latter (Pytheas should "know
exactly what I do and don't know") — that's a new data model, not covered
in `Development Roadmap.md` today. Worth a workstream-2.5 addendum: an
`identity.md`-style knowledge-state file per topic, injected the same way
environment context is.

### 7. Notion-from-Obsidian — universal lifetime workspace
Calendar/email integration is already noted as planned in
`capabilities-roadmap.md` ("Planned for Odysseus... Docker install first").
This prompt raises the bar from "integrated" to "Notion-replacement" —
single pane over vaults + email + calendar + AI + (implicitly) tasks/docs.
This is a large, open-ended UI/IA project, not a single workstream — needs
its own design pass once workstreams 1–4 land, not before.

### 8. Social media guide harvesting (IG/X/TikTok)
Goal as stated: collect AI-generated "how to use AI" guides from Instagram,
X, and TikTok, both to learn from and to feed Daily Briefings. `last30days`
already pulls from X/TikTok/Reddit/etc. as research sources — check whether
it already covers this before building anything new. **Flagged, not
started:** scraping Instagram/TikTok specifically has real ToS/access
constraints (both are much more locked-down than X for automated pulls) —
needs a scoping conversation before any automation is built, not just an
engineering task.

### 9. Update/usage schedule
Explicit ask: "make an update schedule so usage doesn't burn instantly."
Once the technical workstreams have an implementer, pair this with a
cadence (e.g. daily briefing already exists; propose weekly Pytheas
dev-sprint cadence + per-session token budget, mirroring the `ccdash`
tracking already in place per `Jarvis Progress Guide.md`). Not yet
scheduled — needs your input on cadence preference.

## Sequencing recommendation (supersedes strict "test Pytheas fully first")

Given the 21-day SAT clock, propose interleaving instead of strict
sequencing:

1. **Now, parallel:** SAT diagnostic + course track (doesn't need Hermes).
   Atlas fix (small, isolated, per `Development Roadmap.md` workstream 1).
2. **This week:** environment-context injection (workstream 2) — this is
   the prerequisite for Pytheas actually knowing the vault/codebase/tools,
   which the "coding" and "AI prompting" courses both depend on to be
   accurate rather than generic.
3. **After SAT (post ~2026-08-21):** vault-pyramid agents, Hermes full tool
   parity, multi-model integration, social-media harvesting, Notion-parity
   UI — the heavier, higher-risk builds.

Flagging for your explicit confirmation rather than assuming — see
questions asked in-session.

## Cross-vault reorg roadmap (per "roadmap to do this with all other
vaults")
Once the `Prompts/` + tagging pattern is validated here, apply the same
structure (subcategory folders, `Prompts/` logging, tag linking) to:
`learning/`, `ai-improvement/`, `finance/`, `card-flip/`,
`agonizing-sentience/`, `minecraft-event/` — each vault's existing
`Home.md` stays the entry point; this only adds structure underneath.
`personal-private/` excluded (AI writes blocked there except Health).
Not started — sequencing this after Atlas + SAT track, per above.

## Vault reshuffle (decided 2026-08-02, not yet executed)

Donovan's target end-state for the whole vault set — **planning only,
nothing moved yet** (this is file moves/deletes across multiple vaults,
needs its own careful pass, not a side effect of a chat message):

- **`learning/`** becomes the Courses home — school work *and* other
  learning/side-projects live here, integrated with the Courses feature
  (see workstream 6 above).
- **`finance/`** — all money-related record-keeping. Also absorbs
  whatever's salvageable from `personal/Work` (per "work stuff can be
  moved to finance").
- **`card-flip/`** — status change: the card-flipping operation is
  "essentially ended." Vault stays as historical record, not an active-ops
  vault going forward — revisit whether it still needs its own top-level
  slot or folds into `finance/` as an archive.
- **`personal/` (`personal-private/`) — mostly dissolved.** Donovan's
  read: it "highkey doesn't need to exist" except `Journal/`. Plan:
  - `Journal/` → **spun out into its own standalone vault** (soon, per
    Donovan — not tonight). Keeps the strict AI-walled-off treatment,
    just as its own vault instead of a folder inside `personal/`.
  - `Health/` → **made independent** (own vault or clearly separated
    section) — currently the one write-allowlisted exception buried
    inside a vault that's otherwise going away; give it a real home.
  - Everything else currently in `personal/` → moved into `learning/`
    (general life/learning content) unless it's `Work/`-flagged, which
    goes to `finance/` instead.
  - Net effect: **no more general-purpose `personal/` vault.** What's left
    (Journal, Health) either becomes its own vault or gets promoted out;
    everything else lives under the AI/Pytheas-managed vault set
    (`learning`, `finance`, `ai-improvement`, `pytheas`, etc.).
- **Sequencing:** this is a structural vault migration (moves + deletes,
  some across the private-wall boundary) — do this deliberately, vault by
  vault, with Donovan reviewing each move, not in one sweep. Comes after
  the Atlas fix + SAT track per the existing sequencing above; CLAUDE.md's
  "Vault layout" section (still describing the current, soon-obsolete
  structure) gets rewritten as the last step once the moves are done, not
  before.
