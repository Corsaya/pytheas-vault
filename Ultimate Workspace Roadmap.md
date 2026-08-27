---
tags: [pytheas, roadmap, courses, sat, ai-prompting, coding, notion-parity, social-automation, mega-prompt]
created: 2026-08-02
status: draft — pending clarifying answers
source: "[[Prompts/2026-08-02 Mega Prompt — Ultimate Workspace Vision]]"
related: ["[[Development Roadmap]]", "[[capabilities-roadmap]]", "[[../ai-improvement/needs-wants-interview-kit]]"]
---

# Ultimate Workspace Roadmap

> [!note] 2026-08-02 snapshot — superseded in direction, not in research.
> The current plan for the workspace is
> [[Handoff/02 — AI Workspace Master Plan]] (2026-08-25), which sets the
> end-of-senior-year deadline and phases the build against the real school/crew
> calendar. **This document's research is still the reasoning of record** —
> the CalDAV decision, Notion ruled out structurally, the Odysseus adoption
> call. Body left unedited on purpose.

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

## 2026-08-04 session — SAT pause overridden, new workstreams added

Donovan explicitly overrode the 2026-08-02 "SAT is sole focus until
2026-08-22" pause for this session to work non-SAT roadmap items. SAT
sequencing (workstream priority) is otherwise unchanged — this is a one-off
override, not a reversal of the decision.

### 12. Graphify — evaluated, not adopted for Atlas
Investigated `github.com/Graphify-Labs/graphify` per Donovan's request.
Verdict: **doesn't fit.** Graphify is a Python CLI/agent-skill that builds a
knowledge graph *of a codebase* via tree-sitter AST parsing + Leiden
clustering (functions, imports, schemas) — a different domain from Atlas,
which graphs *Obsidian notes* by wikilink. The one transferable idea isn't
from Graphify itself: it ships an interactive `graph.html` viewer, which is
exactly what Atlas lacks (no pan/zoom — see workstream 1 below). Recommend
pulling in a real JS graph-rendering library (d3-force, Cytoscape.js, or
Sigma.js) for that piece instead of adopting Graphify. Separate, low-priority
idea surfaced by the research: Graphify itself could later generate a
dependency graph of the **Pytheas codebase** (a devtool, not a vault
feature) — not scoped, flagging only. Note: a different, similarly-named
`github.com/safishamsi/graphify` repo also exists — don't conflate the two if
this comes up again.

### 13. Token-saving / memory / performance research (feeds Pytheas + this Claude Code workflow)
Research done 2026-08-04, both angles:
- **For Pytheas's own memory:** Letta (formerly MemGPT, core/archival/recall
  3-tier memory) and Mem0/Cognee/Graphiti evaluated as options if Pytheas
  needs real persistent user-memory beyond flat context + vault retrieval.
  Not started — worth a spike once workstream 2 (environment context
  injection) exists, since they're complementary, not competing, layers.
  Cheap win available now if/when Pytheas calls the Anthropic API directly:
  native Claude prompt caching for stable context blocks (vault index, tool
  catalog).
- **For this Claude Code session:** claude-mem (already in use) still covers
  cross-session memory; nothing found replaces it. Two narrow, complementary
  tools worth a low-risk trial: **Headroom** (reversible tool-output
  compression, claims 60–95% reduction — `github.com/chopratejas/headroom`)
  and **Caveman** (terser agent responses, ~65% output reduction —
  `github.com/JuliusBrussee/caveman`). Neither adopted yet — flagging for
  Donovan to decide whether to try them.

### 14. Voice/text chat save — fixed 2026-08-04
Root cause from the 2026-08-02 live test (workstream 11): `handle_voice_text`
in `server.py` only persisted a turn if a voice session had already been
started via `POST /api/voice_session {action:"start"}`; if that call raced
or was skipped, the turn ran ephemeral and silently vanished. Fix: if no
session is active when a voice/text-command turn arrives, `server.py` now
calls `voice_session_start()` itself before persisting — every turn always
lands in chat history, no separate start call required. Applies to both
`/api/voice` and `/api/text_command`.

### 15. Gemini/NotebookLM course visibility — fixed 2026-08-04
Root cause (workstream 6/priority 5): `courses.py` only tracked notebooks
created through Pytheas's own "＋ New course" flow in its private registry
(`~/.local/state/pytheas/courses.json`), never querying live NotebookLM
state — so a notebook created via the raw CLI, the NotebookLM web UI, or
directly through Gemini Notebook never appeared in the Courses tab. Fix:
`courses.list_notebooklm()` (calls `notebooklm list --json`, diffs against
known notebook IDs) + `courses.import_notebook()` back a new "⇩ Import from
NotebookLM" button in the Courses tab (`static/sections.js`) that lists
out-of-band notebooks and adopts one into the registry (pulls its existing
sources via `notebooklm source list`). New `/api/courses` actions:
`list_notebooklm`, `import`.

### 16. Library tab — organization capabilities (partial, more scoped as workstream 17)
Donovan: Library tab "only contains briefings" (actually briefings + research
reports, but flat/unfiltered) — wants organization capability, "make it
similar to Odysseus'". Odysseus-parity audit (workstream 17 below) mapped the
full gap. Shipped 2026-08-04, scoped v1: `research.library()` now takes
`search`/`kind`/`sort` params (name search, kind filter, recent/oldest/alpha
sort), `GET /api/library` passes them through, and the Library tab UI
(`static/sections.js`) gained search box + kind dropdown + sort dropdown.
**Not done** (Odysseus has, Pytheas still doesn't): folders/collections,
bulk select+archive+delete+export+clone, an "Archive" state, AI-assisted
"Tidy" auto-cleanup, drag-to-reorder, import/create-from-Library, and
Odysseus's 4-way split (Documents/Chats/Research/Archive) vs. Pytheas's flat
2-kind (research/briefing) list. That's a genuinely bigger UI+backend project
— queued as its own pass, not attempted in full today.

### 17. Odysseus full function/settings parity audit — done 2026-08-04, gap list only
Systematic pass through `~/code/odysseus` vs `~/code/pytheas` (workstream 10,
previously flagged, never executed). Full tab-by-tab table and settings/perms
comparison captured in this session's agent output (see
`ai-improvement/` session notes or ask Pytheas/Claude to regenerate — not
duplicated in full here to keep this doc from bloating). Headline findings:
- **Biggest real gaps:** Library (see workstream 16), Email (Odysseus has a
  full email *library* subsystem — inbox + compose + archive — Pytheas has
  basic send/read only), Notes (`notes.js` far larger in Odysseus, richer
  editor/org), Cookbook (Odysseus: scheduling/serving/diagnosis/hwfit —
  Pytheas has no equivalent concept at all).
- **Odysseus-only, no Pytheas surface at all:** Contacts, Skills admin tab,
  Personal-docs tab, Backup tab, Copilot tab, HWFit, Webhooks.
- **Structural difference, not a gap to close by default:** Odysseus is
  multi-user with real auth/admin gating (13-tab settings modal, admin-only
  tools/users/system tabs, per-account privilege review). Pytheas is
  single-user/local-first by current design (`permissions.py` is a flat
  capability-toggle list, no accounts). **Open decision, not yet made:**
  does "full parity" mean adopting Odysseus's admin/multi-user model too, or
  is that explicitly out of scope for a single-user tool? Needs Donovan's
  call before any of these get prioritized/built — this audit is a map, not
  a build order.

### 18. Odysseus deep architecture read (backend + frontend) — done 2026-08-04
Follow-up to workstream 17's shallow tab-parity survey: two agents did a real
full-file read of Odysseus's backend (`app.py`, `core/`, `src/`, `routes/`)
and frontend (`static/index.html`, `app.js`, `chat.js`, `documentLibrary.js`,
`theme.js`, `dragSort.js`, `style.css`) for design patterns worth stealing,
not just a feature checklist. Full reports live in this session's transcript
(ask Claude to regenerate if needed — not pasted in full here). Verdicts,
condensed:

**Adopt (cheap, scale-independent):**
- Centralized `settings.py`-style module owning each JSON registry, with a
  short TTL cache if read on a hot path, heavily-commented defaults
  ("why," not just "what"), and per-key range-clamping on any settings
  write endpoint.
- Routes/handlers never touch a registry file directly — always through a
  small manager function/class, mirroring Odysseus's
  `core/session_manager.py` pattern.
- `_hlSearch`-style search-highlighting (tokenize → longest-first sort →
  wrap in `<mark>`) — directly portable, ~15 lines.
- Document the CSS custom-property "theme contract" (which vars are
  public/stable) at the top of `style.css`, same as Odysseus does.
- SSE (`text/event-stream`) over plain `setInterval` polling for the
  Courses job-status UI, if/when sub-second responsiveness matters —
  Odysseus itself still polls for most non-chat features, so this isn't
  urgent, just an available upgrade.
- Stylistic: fail-closed security defaults + comments that explain *why* a
  corner wasn't cut, not just what the code does.

**Maybe / only if Pytheas grows into it:**
- Split `sections.js` into per-tab ES modules once it outgrows one file.
- Fernet-encrypt specific sensitive fields (API keys) within the existing
  JSON registries, without adopting a full SQL database.
- `dragSort.js` as a template if drag-to-reorder is ever wanted (Courses
  list, sidebar).
- Odysseus's "5 base colors → derive ~20 CSS vars via HSL math" theming
  approach, if Pytheas ever wants more than light/dark — port the
  derivation function only, not the full custom-theme-editor UI around it.
- Read-only-vs-mutating tool classification (fail-closed default) for a
  future Hermes "dry run" mode.

**Explicitly not worth it at Pytheas's scale:**
- SQLite/SQLAlchemy — Odysseus's data is genuinely relational (messages
  belong to sessions belong to owners, versioned documents, scheduled-task
  run history); Pytheas's registries are small and independent, flat JSON
  stays correct.
- Odysseus's full multi-user auth stack (bcrypt/TOTP/per-user privileges/
  admin lockout prevention) — solves a multi-tenant problem Pytheas, as a
  single-user local tool, doesn't have. This is the clearest case of "don't
  chase parity here" from the whole audit.
- Dynamic MCP-manager with runtime connect/OAuth/per-tool-toggle for
  arbitrary third-party servers — Pytheas's tool list is small, fixed, and
  first-party-trusted; none of that machinery is solving a problem Pytheas
  actually has.
- A shared searchable/sortable/bulk-select list component: genuinely worth
  building for Pytheas's Library/Courses-style tabs, but note **Odysseus
  never built one either** — it duplicates this logic per-tab (Documents/
  Chats/Research/Skills/Notes/Gallery each hand-roll their own). Not a gap
  to copy Odysseus's homework on; build it properly since Odysseus's own
  code doesn't have a working example to copy.

## North Star (set 2026-08-04, supersedes piecemeal workstream picking)

Donovan, 2026-08-04, usage-crunch session: **"make Pytheas essentially
Odysseus but with Obsidian brain connectivity, and the capability to record
and learn off of everything done, said, and asked of from this point on."**
This is now the target end-state — future sessions should pull the next
task from *this*, not re-derive priorities from scratch.

Two pillars:

1. **Odysseus feature-parity, minus the parts workstream 18 flagged as wrong
   scale.** Not "port everything" — the 2026-08-04 backend/frontend audits
   (workstreams 17-18) are the actual map: build toward Odysseus's Library,
   Notes, Email, Cookbook-equivalent depth; explicitly skip the multi-user
   auth stack and dynamic third-party MCP-server manager (wrong problem for
   a single-user local tool). Obsidian-native is the one place Pytheas
   should *exceed* Odysseus, not match it — every feature should read/write
   through the vault, not a parallel SQLite store, wherever that's the
   natural fit (Odysseus's own hybrid of SQL-for-relational +
   JSON-for-config is the model to adapt, with "the vault" standing in for
   both where content is markdown-shaped).
2. **Continuous record-and-learn, starting now, not just chat memory.**
   Broader than the existing claude-mem session-memory pattern this Claude
   Code environment already has — Donovan wants *Pytheas itself* to capture
   everything done/said/asked through it (chats, voice, actions taken,
   courses generated, briefings read) and actually learn from it, not just
   log it. Candidate mechanism: workstream 13's memory-framework research
   (Letta's core/archival/recall tiers, or Mem0/Cognee) layered on top of
   workstream 2 (environment-context injection, not yet built) — a session
   log alone isn't "learning," it needs to feed back into what Pytheas
   knows about Donovan the way `identity.md`/environment-context was always
   meant to. Not designed yet — next real build decision, once usage
   resets: pick one memory framework (or a minimal custom version) and spec
   what "recording everything" actually writes to and how it gets *used*
   on a later turn, not just stored.

**Status:** direction set, not built. This session hit its usage ceiling
(97% of 5h) right after setting it — no implementation started against this
north star yet. Next session: start with picking the memory mechanism for
pillar 2 (it's the prerequisite the rest hangs off of, same logic as
workstream 2 in `Development Roadmap.md`), then work down the workstream
18 "adopt" list for pillar 1.

## North Star expansion (2026-08-07) — life-improvement engine, not just an Odysseus clone

Donovan, 2026-08-07, per
[[../Prompts/2026-08-07 Mega Prompt — SAT Tutor Buildout + Life-Improvement North Star Expansion|the mega-prompt logged this session]]:
the two pillars above (Odysseus parity + Obsidian brain, continuous
record-and-learn) still hold, but the *purpose* they serve is bigger than
"a good local Claude/Odysseus clone." Layering on top, not replacing:

**Third pillar — Pytheas as a life-improvement engine.** Concretely, in
Donovan's own words: make him smarter, help him "verse himself better,"
help him identify and fix bad habits, help him make real money this year
(college costs and beyond), act as a quality assistant for navigating his
own computer, and — a standing, explicit top priority — **be a real tutor**,
teaching him things directly rather than just doing tasks for him. First
subject in line for that tutor role: **AI/software literacy** — tokens,
models, how coding actually works, "essentially everything relating to the
AIs and of the software" — ahead of other subject areas, because
understanding the tool he's building is itself one of the goals (echoes the
existing "How Pytheas Was Built" course concept in workstream 6, and the
North Star's own long-term goal of being good enough that Donovan doesn't
need to depend on paying for frontier access).

This reframes workstream 6's Courses feature and the new SAT tutor work
below (workstream 19) as **the first real instances of pillar 3**, not a
side quest — the SAT diagnostic/tutor build is simultaneously "finish SAT
prep" and "prototype what a Pytheas tutor mode looks like" for every other
subject that comes after it (starting with AI/coding, per the stated
priority above).

**Sequencing:** SAT stays the sole active priority until 2026-08-22 per the
hard deadline elsewhere in this doc — this expansion documents *where
things go once that constraint lifts*, it does not override it. Workstream
19 below is written the same way: content work (the 4 confirmed-gap
lessons) is small enough to fit inside SAT prep time since it directly
serves the test; the app-rebuild and general-tutor-mode pieces of
workstream 19 wait for post-SAT, same as workstreams 1-4 and the North
Star's own two pillars.

### 19. SAT diagnostic app upgrade + general AI tutor mode (added 2026-08-07)

Grew out of building and taking the first SAT diagnostic test
(`Courses/SAT/SAT Diagnostic Test (2026-08-07).md` +
`~/code/pytheas/static/sat-test.*`, a from-scratch Bluebook-style timed
runner — modules, timer, mark-for-review, answer eliminator, basic
built-in calculator with per-question usage tracking, review screen).
First real attempt: 28/32 (87.5%). Post-test interview surfaced two
confirmed content gaps (Advanced Math asymptote rules, Standard English
Conventions subject-verb agreement with interrupting phrases), one process
issue (Algebra: rushed, no scratch work — not a knowledge gap), and one
minor flag (PSDA percent-of-a-number hesitation). Full breakdown and error
log logged in the diagnostic doc itself.

Donovan's four follow-up asks, to sequence rather than build all at once:

1. **Content lessons on the confirmed gaps** — asymptotes, the
   inequality-flip-on-negative rule, subject-verb agreement with
   interrupting phrases, and a percentages refresher. Small, standalone,
   no app changes needed. **In scope during active SAT prep** — directly
   serves the 2026-08-22 deadline. **Done 2026-08-07:**
   `Courses/SAT/Diagnostic Gap Lessons (2026-08-07).md` — all four lessons
   plus a 12-question untimed retest. Retest not yet attempted.
2. **Bluebook-parity app rebuild** — pixel/interaction-level match to the
   real digital SAT interface: proper graphing calculator (current one is a
   basic expression evaluator, not Desmos-equivalent), image/diagram
   support in questions (current test is text-only), and a digital
   scratch-paper/annotation tool (real Bluebook has one; directly relevant
   given Q1's miss was traced to "no scratch work"). **Post-SAT** — this is
   app engineering, not prep time.
3. **Interactive tutoring chatbot mode** — step-by-step Socratic walkthrough
   ("what's the next step," "do you know this," presenting an MC check)
   instead of a static test-then-review flow. This is the first concrete
   design for what a general Pytheas tutor mode looks like (pillar 3 above)
   — build it once, generalize beyond SAT math/English to the AI/coding
   tutor priority next. **Post-SAT**, and the one piece worth scoping
   carefully before building since it's a new interaction pattern, not a
   UI reskin.
4. **A second, easier/untimed diagnostic** — different purpose than the
   first one (which was deliberately timed and Bluebook-proportional to be
   realistic). This one is a teaching tool, not an assessment — lower
   pressure, meant to be worked through with help rather than cold. Depends
   on #3 (the tutoring mode) to actually be useful as "easier," not just
   "the same test with a longer clock."

**Status:** roadmap entry only, nothing beyond #1's scope started. Revisit
sequencing after 2026-08-22.

### 20. Vault/repo restructure v2 + naming ("Chiron") + conversation archive (added 2026-08-07)

**Explicitly deferred by Donovan** — "keep this in roadmap and construct one
day." Nothing here is executed. This supersedes/extends the 2026-08-02 vault
reshuffle below with more detail, and answers (fully, as of 2026-08-08) the
open naming question from workstream 19's discussion.

**What Donovan described, as close to verbatim structure as the raw prompt
allows, updated with 2026-08-08 resolutions:**

- **`finance`** — absorbs `Work` and `card-flip` as subfolders/content.
  Matches the existing 2026-08-02 reshuffle plan below.
- **`learning`** — absorbs `ai-improvement` as a subfolder, and also gains
  the new private `Chiron` vault nested inside it (see below).
- **`Chiron`** — new private, personal-notes vault, nested under
  `learning/`. Also names the code repo: `~/code/pytheas` and its GitHub
  remote `TheBiggerMann/pytheas` rename to `chiron` (see resolution #2
  below).
- **`pytheas`** — stays a separate, distinct **public-facing brand vault**
  for changelogs, additions, non-personal logs, "pretty much like the
  Odysseus repo." Not the same thing as `Chiron` — see resolution #1 below.
- **`life`** (final name — Donovan corrected mid-prompt from an initial
  "journal") — the big personal vault: health, history, and project notes
  for `agonizing-sentience` and `minecraft-event`.
- **Privacy tiers:** `finance`, `learning` (incl. nested `Chiron`), and
  `life` are all **private**. `pytheas` was floated as the one public
  vault, but per resolution #4 below it **stays private for now** —
  going public is off the table until Donovan explicitly revisits it.
- Also requested as part of this work: a **tagging taxonomy** to link files
  across the new structure (including links to content that predates the
  reorg) for Atlas to graph, and **organizing each vault's contents into
  folders** as part of doing the move.

**Open contradictions/ambiguities — resolved 2026-08-08 (still deferred for
execution, but no longer blocked on Donovan clarification):**

1. **RESOLVED (2026-08-08): two separate vaults, not one rename.** `Chiron`
   = private, personal-notes vault, nested under `learning/`. `pytheas` =
   a separate, distinct public-facing brand vault for changelogs/
   non-personal logs (Odysseus-style). Two different vaults, two different
   names, two different audiences.
2. **RESOLVED (2026-08-08): yes, the code repo rename happens too.**
   `~/code/pytheas` (and its GitHub remote `TheBiggerMann/pytheas`)
   renames to `chiron`. This cascades into every script, systemd/
   desktop-launcher reference, the vault's `code/` symlink, and every
   existing roadmap doc that names `pytheas` — scope it as its own task
   when the restructure is actually executed.
3. **`agonizing-sentience` can't simply become private inside `life`** — it
   is explicitly a public, collaborative vault with a friend (per this
   vault's CLAUDE.md). Only the existing private scratchpad
   (`personal-private/agonizing-sentience-scratchpad/`) can move into
   `life`; the actual collaborative vault has to stay separately
   public/shared, or this breaks the collaboration.
4. **RESOLVED (2026-08-08): stay private for now.** Both
   `TheBiggerMann/pytheas` and `TheBiggerMann/pytheas-vault` GitHub repos
   stay private. Drop the "pytheas is the only public vault" framing —
   going public is off the table until Donovan explicitly revisits it
   (at which point a secrets/config audit is still a required pre-step).
5. **Redundant with pillar 2 of the North Star** (continuous record-and-
   learn) — the "tags for cross-vault linking + Atlas" ask here is the same
   underlying need as the not-yet-built memory/learning mechanism from the
   2026-08-04 North Star. Should probably be designed together, not twice.

**Claude Code conversation archive** (the "verbatim record, incognito
toggle, wipe safeword" request from earlier this session) — **fully
specified, being built now, separately from the vault restructure above:**
incognito toggle phrases "incognito mode on"/"incognito mode off" (default
off), deletion safeword "wipe this", archive location `ai-improvement/`.
Implementation as Claude Code hooks in `~/.claude/settings.json` (global,
all projects) — in progress this session; see this session's own commit
history / next session's continuation for build status, since hook payload
schema was still being empirically verified (via a temporary debug hook) as
of this entry.

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

**Progress (2026-08-09):** the one safe, mechanical piece got executed —
`ai-improvement` merged into `learning/ai-improvement` via `git subtree
add` (full git history preserved, pushed to the `personal-vault` GitHub
repo). Old standalone `~/Documents/Obsidian/ai-improvement/` renamed (not
deleted) to `ai-improvement.MERGED-into-learning-2026-08-09/` — safe to
actually delete once Donovan confirms nothing's missing. Chiron's vault
mounts (`docker-compose.yml`, `src/constants.py`) and the new
conversation-archive hook (see prompt-logging section above) both updated
to the new path and verified working (30 `ai-improvement` files correctly
indexed under `/app/vaults/learning/ai-improvement`).

**Explicitly NOT done** — deferred as its own reviewed pass, not attempted
this session given the risk (touches `personal-private`, involves real
deletes, and CLAUDE.md itself says do this "vault by vault," not in one
sweep): Journal/Health spinout from `personal-private` into a new `life`
vault, creating the `life` vault itself, `finance` absorbing
`Work`/`card-flip`, the new private `Chiron` notes vault nested in
`learning/`, and the `pytheas` naming/scope resolution from workstream 21
(decided, not moved).

**Refined plan for the remaining moves, per Donovan 2026-08-09 (end of
session, not yet executed — this is the spec for "next session"):**

- **`card-flip/`** → moves into `finance/` (money-related; matches the
  existing "card-flip is essentially ended, archive it" framing from the
  2026-08-02 reshuffle above).
- **`agonizing-sentience/` + `minecraft-event/` + `personal/`
  (`personal-private/`)** → merge into a single new **`life`** folder/vault
  containing health, hobbies, journals, calendar, email — "all life and
  personal stuff." Donovan's own words: **"some read limitations"** — not
  fully specified which parts stay AI-read-restricted (the existing
  Journal/Daily/Work/Private-Reference.md carve-outs from `personal/`
  presumably still apply at minimum, but this needs an explicit
  confirm-or-correct from Donovan before any move, same caution as
  workstream 20's original open questions). Note `agonizing-sentience` is
  a public collaborative vault with a friend (per this doc's earlier
  flag) — folding it into a walled-off `life` vault needs a decision on
  how the collaboration stays intact, don't silently resolve this.
- **Next session:** run a full scan across the vault set and, file by
  file, (1) sort each file into its correct vault per the plan above, (2)
  organize each vault's files into folders, (3) tag files for cross-vault
  Atlas graph connections and general findability. This is the actual
  execution pass for workstream 20 — do it deliberately, not as one
  unreviewed sweep, per the standing sequencing note above. Re-confirm the
  "some read limitations" scope with Donovan before touching anything
  currently under `personal-private`.

### 21. Architecture pivot — fork Odysseus instead of building Pytheas from scratch (decided 2026-08-08)

Per
[[../Prompts/2026-08-08 Mega Prompt — Fork Odysseus Instead of Custom Pytheas Build|this session's mega-prompt]].
Mid-session on the new [[../Courses/SAT/Foundations Knowledge Check]],
Donovan asked to just fill Odysseus with his Obsidian vaults instead of
continuing the custom Pytheas build. Checked Odysseus's actual ingestion
code (`src/personal_docs.py`, `routes/personal_routes.py`) before
answering — verdict: **not a clean drop-in.** Odysseus's document ingestion
(`PersonalDocsManager`, Chroma-backed RAG) is real but (1) hard-confines
files under its own `data/personal_docs/` root — symlinks to vaults
elsewhere are explicitly rejected by `_resolve_allowed_personal_dir`, so
vaults would need to be copied in, not linked, (2) has **no filesystem
watcher** anywhere — reindex is a manual `POST /api/personal/reload` call,
not live, (3) has **no git-awareness** for documents at all, (4) has **no
Obsidian syntax support** — wikilinks/frontmatter/callouts/embeds all get
flattened to plain text chunks. Chat history (SQLite, owner-scoped) and the
task scheduler are real and usable as-is.

**Decision: fork Odysseus, build the missing vault-integration pieces on
top of its actual codebase**, rather than (a) moving vaults into it
unmodified, or (b) continuing to build Pytheas from scratch and
cherry-picking patterns per workstream 18's adopt list. This changes
*mechanism* only — North Star pillar 1 (Odysseus feature-parity, Obsidian
brain as the differentiator) is unchanged, it's now "start from Odysseus's
code" instead of "build toward Odysseus's feature set."

**Scope, not yet broken into tasks:**
- Fork `~/code/odysseus` (need to decide: new repo name — `chiron`? see
  workstream 20's still-open naming question, now more urgent since a real
  fork forces a decision — new remote, or a local-only fork for now).
- Build live vault sync: replace/extend the single-root path confinement
  in `personal_routes.py` to allow the actual vault paths (`learning/`,
  `finance/`, `ai-improvement/`, `pytheas`/`chiron`, `life`, per
  workstream 20's structure once that executes), add a filesystem watcher
  (e.g. `watchfiles`) so edits in Obsidian show up without a manual reload.
- Teach ingestion Obsidian syntax: parse wikilinks/frontmatter/callouts/
  embeds instead of flattening to plain text — needed for RAG quality and
  for any future Atlas-style graph view.
- Git-awareness: at minimum, read from the existing vault git repos
  correctly (no clone-and-diverge); revisit whether Odysseus needs to
  *write* commits or just read live files.
- Nav/IA consolidation Donovan asked for: New Chat, Search Chats, and
  Email stay top-level; everything else (Documents/personal-docs, Notes,
  Cookbook, Contacts, Tasks, the new Courses/SAT tools, briefings — a
  concept Odysseus doesn't have at all yet) nested under one "Tools" area.
- Conversation logging into Obsidian: mirror sessions into the vault
  (excluding incognito-mode and manually-cleared chats), git-ignore the
  storage file(s), build a delete path that removes a conversation from
  both the vault and the (forked) app's own DB.
- Diagnostic/quiz results (Foundations Knowledge Check and future ones)
  feed the same "understand Donovan better" mechanism — this is North Star
  pillar 2 (continuous record-and-learn), not a separate feature to design
  twice.

**Status (updated 2026-08-09):** first working slice built and verified live
in-browser. `~/code/chiron` created (local `git clone` of `~/code/odysseus`,
`upstream` remote → the real Odysseus GitHub repo, no `origin` yet — no
GitHub repo of its own). Running as its own Docker stack alongside the
existing live Odysseus instance, non-conflicting ports (app 7001, chromadb
8101, searxng 8081, ntfy 8092) — Odysseus on 7000 untouched.

Built and confirmed working:
- Multi-vault ingestion: `src/constants.py` `VAULT_ROOTS`,
  `routes/personal_routes.py` path confinement opened to those roots (still
  excludes `personal-private`). 347 documents indexed across all 7 vaults on
  first boot.
- Live sync: `src/vault_watcher.py`, mtime-polling every 15s, auto-reindex
  on change — no manual reload needed.
- **Classroom UI** (Donovan's ask, not originally scoped above): folder
  convention — `Courses/<Subject>/` in the pytheas vault becomes a
  classroom, files become assignments/materials, subfolders become
  sections. `routes/classroom_routes.py` + `static/classroom.html/js`.
  Known files can be flagged (`CUSTOM_APPS` table) to open a real
  interactive app instead of flat markdown — first one wired up: the SAT
  diagnostic test now opens the actual ported Bluebook-style runner
  (`static/classroom-apps/sat-test/`, moved from `~/code/pytheas/static/`).
- Found Odysseus's own admin RAG-management panel (`static/js/admin.js`
  `loadRag()`) is dead code — the JS exists but the HTML element it targets
  (`adm-ragDirList`) was never added to `index.html` and nothing calls
  `loadRag()` on tab-open. Not a Chiron regression — this was already
  broken in upstream Odysseus. The Classroom UI is the actual answer to
  "where do I see my vault content," not that panel.
- Debugging notes for next session: Odysseus's CSP is strict by default
  (`core/middleware.py`) — inline `<script>` blocks and inline
  `onclick=`/`oninput=`/etc. handlers are both blocked without a nonce, and
  `X-Frame-Options: DENY` is global (no iframing anything, even
  same-origin). Ported apps need either a rewrite to `addEventListener`, or
  a path-based CSP carve-out like `is_classroom_app` in `middleware.py`
  (used for the SAT test app — same pattern Odysseus already uses for
  `is_report`). Docker images don't bind-mount source, so every code change
  needs `docker compose up -d --build`, not just `restart` — slow dev loop,
  worth revisiting (dev bind-mount override) if this becomes a real
  friction point.

Still open, not built: wikilink/frontmatter/callout-aware parsing (RAG
still sees flat text), Atlas-style graph view, the Tools-nav consolidation,
conversation logging into Obsidian (git-ignored, incognito-aware, deletable
both sides), and more `CUSTOM_APPS` entries as more interactive tools get
built. Session paused here — Donovan resuming SAT prep (Foundations
Knowledge Check was mid-way through Algebra when this pivot started).
