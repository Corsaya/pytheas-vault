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
3. **Full email send + two-way calendar sync** (from Odysseus) — **status:
   🚧 under construction, paused.** Decided 2026-08-02: SAT is the sole
   main focus through 2026-08-22 (see Deadline note above); this
   workstream's design is settled (CalDAV, per the Odysseus research
   below) but no build work starts until SAT prep is handled. **note:**
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

**Research done 2026-08-02:** see
[[Prompts/2026-08-02 Notion Calendar, Email, Meeting-Notes Research|Notion
Calendar, Email, Meeting-Notes Research]]. Bottom line: **Notion Calendar
has no developer API** (only a `cron://` deep link) and **Notion Mail shuts
down 2026-09-22** — so there's no supported way to link Pytheas *into*
Notion Calendar/Mail, and no reason to try. Two real options instead:
(1) just use Notion Calendar directly as a standalone app for "universal
calendar everywhere" (zero Pytheas engineering, but not Pytheas-native),
or (2) have Pytheas sync against Google/Outlook/iCloud calendar APIs
directly — the same underlying data Notion Calendar itself reads from —
which is already the direction of confirmed build priority #3 above (full
email send + two-way calendar sync). Recommendation: skip Notion as an
integration target entirely, treat priority #3 as the real path. Meeting
transcription is a similar case — Notion's version needs a paid
Business/Enterprise plan and its own desktop app running, so it's not a
piggyback opportunity; if Pytheas wants transcription it should be a
built-in feature (local Whisper or an API), not a Notion dependency. Needs
Donovan's decision before either path is built.

**Decision leaning, 2026-08-02:** confirmed — see
[[Prompts/2026-08-02 Odysseus Calendar Architecture and Notion-vs-Build Decision|Odysseus
Calendar Architecture and Notion-vs-Build Decision]]. Donovan wants
everything linked to Obsidian, including email and calendar, which rules
Notion out structurally (closed data model, no calendar API, Mail dying
2026-09-22). Odysseus's calendar implementation was read directly
(`~/code/odysseus/src/caldav_sync.py` etc.) and confirmed as the pattern to
copy: **CalDAV** (via the `caldav` library) two-way syncs against Google,
Outlook, and iCloud in one protocol — verified Google still runs a CalDAV
server as of 2026, not deprecated. Plan: build Pytheas calendar sync on
CalDAV + local SQLite (Odysseus's shape), then add the vault-native piece
Odysseus can't do — surfacing events inside Obsidian markdown (daily
notes, Atlas, Courses deadlines). This becomes the concrete protocol
choice for confirmed build priority #3 above. Not yet decided: build now
vs. after SAT, and which of Google/Outlook/iCloud to support day one.

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

## Sequencing recommendation — SUPERSEDED 2026-08-02

The interleaving proposal below is superseded: Donovan confirmed **SAT is
the main focus now**, full stop, hard deadline **2026-08-22 8:00 AM** (SAT
test date; today is 2026-08-02, so 20 days). Email/calendar work (priority
3) and any workstream not directly serving the SAT curriculum are paused
(🚧 under construction, not active) until the SAT window closes. The two
concrete, active-today tasks are:

1. **Connect a Gemini API key in Pytheas Settings**, so SAT-course chat/
   organize traffic can route to Gemini instead of Claude and not burn the
   5h/7d Claude usage window during the SAT crunch. (Backend/UI for this
   already exists and works — `models.py`, `server.py:1274-1283`,
   `static/sections.js:1517-1539` — no `providers.json` key has been added
   yet on this machine. Donovan needs to paste his own Gemini key into the
   Settings UI himself, not into chat, per credential-handling norms.)
2. **Run the actual NotebookLM course-generation test for the full 3-week
   SAT curriculum** (Aug 2 → Aug 22 8AM) — this is confirmed build
   priority #4 above, now scoped concretely to SAT with a hard deadline
   instead of a generic "test it" note. `courses.py` drives this via the
   `notebooklm` CLI (already installed + authenticated locally, not a
   Gemini-API call — see `courses.py:1-14,30,143-146`), so the Gemini key
   from step 1 doesn't feed course generation itself, only the optional
   "Organize" chat feature (`courses.py:328-361`) and any direct SAT Q&A
   chat in Pytheas.

Original (now superseded) interleaving text, kept for record:

1. **Now, parallel:** SAT diagnostic + course track (doesn't need Hermes).
   Atlas fix (small, isolated, per `Development Roadmap.md` workstream 1).
2. **This week:** environment-context injection (workstream 2) — this is
   the prerequisite for Pytheas actually knowing the vault/codebase/tools,
   which the "coding" and "AI prompting" courses both depend on to be
   accurate rather than generic.
3. **After SAT (post ~2026-08-21):** vault-pyramid agents, Hermes full tool
   parity, multi-model integration, social-media harvesting, Notion-parity
   UI — the heavier, higher-risk builds.

### 10. Odysseus settings/feature parity audit
New 2026-08-02: Donovan wants all *other* Odysseus settings/features
correctly integrated into Pytheas, not just calendar (workstream 7) and
Deep Research/Compare/scheduled-agents (priorities 1-2 above). Not started
— needs a systematic pass through `~/code/odysseus`'s settings surface
(`config/`, its admin console per `docs/setup.md`, `routes/`) compared
against Pytheas's actual `Settings` UI (`static/sections.js`) and
`permissions.py`, the same way the calendar piece was audited (read
Odysseus source directly, not just docs — docs there are sparse per the
calendar research). Output should be a gap list (Odysseus has X, Pytheas
doesn't) prioritized by what's actually useful to Donovan, not a blanket
"port everything." Queued after SAT, same as workstream 7.

### 11. Voice conversation — comprehend + execute commands, any model
Checked 2026-08-02: **this mostly already works.** `server.py`'s
`_handle_voice` → `handle_voice_text` routes a transcribed voice message
through the exact same `chats.run_engine` pipeline as typed chat
(`server.py:840-892`, `chats.py:209-233`), including the Hermes/MCP tool-
execution path (`chats.py:166-206`, `pytheas_mcp.py`) when `ai.agent` is
permitted. So talking to Pytheas and having it act on a command (open a
note, run a permitted tool) already functions today, **provided** the
voice engine (`voice_model` setting) is a `claude*` engine and `ai.agent`
is on.

**Two real gaps, not a from-scratch build:**
1. **No per-turn control in the voice UI.** The typed-chat Ask/Agent
   toggle and engine picker (`static/sections.js:155-164`) have no
   equivalent in the voice UI (`static/app.js:275-472`) — agent mode is
   implicitly on/off based only on whether `voice_model` happens to start
   with `"claude"`, not a conscious per-utterance choice the way typed
   chat has. Fix: surface the same mode-pill/engine picker in voice mode.
2. **"Any model" is unconfirmed for agent execution.** The agent/tool path
   is proven for `claude*` engines; whether Ollama or Gemini engines can
   also drive tool-executing turns through `chats.run_engine` wasn't
   checked in this pass — worth confirming before promising true
   any-model voice command execution (ties into workstream 4's Hermes
   "widen tool surface" plan in `Development Roadmap.md`).

Queued after SAT; the plumbing gap is small (UI toggle) so this is
lower-effort than workstreams 7/10 once picked up.

**Live-tested 2026-08-02:** ran a 4-sentence voice benchmark (2 general
knowledge Q&A, 1 math word problem, 1 "open khanacademy.org" command).
Comprehension and spoken responses were all correct — the pipeline really
does route voice → Claude Sonnet 5 → correct answer today. One real bug
found: STT (faster-whisper `"base"` model, per `voice.py`) misheard
"khanacademy.org" as "conacademy.org" and **opened the wrong URL without
any confirmation** — logged in `ai-improvement/Gotchas.md` (2026-08-02).
Two fix candidates for whenever this workstream gets picked up: bump the
Whisper model size (`"base"` → `"small"`/`"medium"`) for better proper-
noun/brand-name accuracy, and/or add a lightweight confirm step before a
voice-triggered link/app open executes (a mis-hear currently acts
silently — worth reconsidering given the "read-only actions run without
confirmation" design, since *opening* is read-only but the destination
being wrong isn't harmless, e.g. a typo'd domain could be squatted).

**Second bug found in the same live test:** the voice conversation didn't
appear in chat history afterward. Root cause (traced in `server.py`): the
save path is real and normally works — `handle_voice_text` writes each
turn to the same `chats.json` typed chat uses — but it's entirely gated on
a `chat_id` set by a prior `POST /api/voice_session {action:"start"}` call.
If a voice turn ever reaches `/api/voice` without that session-start call
having succeeded first, it silently falls back to a throwaway in-memory
history list and never persists — no error surfaced anywhere. This is a
real bug, not expected behavior (unlike the Courses-tab item below). Not
yet root-caused *why* session-start didn't stick in this specific test
(frontend race, a slow/failed `/api/voice_session` request, permissions).
Fix should probably include making the failure loud (log/toast when a
voice turn is running ephemeral instead of saved) in addition to whatever
the underlying timing bug turns out to be. Logged in
`ai-improvement/Gotchas.md` (2026-08-02).

**Third finding, same test session (Courses tab, not voice):** a notebook/
quiz created directly via the raw `notebooklm` CLI (bypassing Pytheas's
own UI) never appears in Pytheas's Courses tab. Confirmed **not a bug** —
`courses.py` maintains its own private registry
(`~/.local/state/pytheas/courses.json`) and only tracks notebooks/
artifacts created through Pytheas's own "＋ New course" flow; it never
queries live NotebookLM state (no `notebooklm list` call anywhere), and
there's no "import existing notebook" action. Practical takeaway: generate
the real SAT curriculum through Pytheas's own Courses UI, not the raw CLI.
Possible small future addition: an "import from NotebookLM" button so
out-of-band notebooks can be adopted into the registry — not scoped or
prioritized yet.

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
