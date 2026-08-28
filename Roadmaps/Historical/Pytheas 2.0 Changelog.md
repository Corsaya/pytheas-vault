# Pytheas 2.0 — Changelog

Newest first. Code lives at `~/code/pytheas` (GitHub: `TheBiggerMann/pytheas`,
renamed from `jarvis-desk` 2026-07-24). Mirrors `~/code/pytheas/CHANGELOG.md`;
kept here too so it's visible from the vault.

## 2026-07-29 — Retire jarvis vault

- Courses, `pytheas-memory.md`, Deep Research reports, and daily briefings
  all used to write into the now-retired `jarvis/` vault — repointed to
  write into this vault instead, so everything lands in one place.
  Touched `briefing.py`, `courses.py`, `pytheas_mcp.py`, `research.py`,
  `server.py`.
- Added `~/code/pytheas/CHANGELOG.md` summarizing project history to date.

## 2026-07-28 — Opus 5, conversation projects + imports, voice pack, atlas/usage fixes

- **Models:** Opus 5 as the "opus" tier, explicit Opus 4.8 option, bare
  "claude" entry dropped (default tier now settable to any tier); model
  discovery automatically lists new Claude ids and rejects scrape junk
  (e.g. `claude-fable-53`).
- **Conversations:** group by model or project, project assignment,
  project context index, `read_chat`/`list_chats` agent tools; importers
  for Claude Code transcripts and claude.ai exports (private-vault
  sessions are skipped on import).
- **Voice:** every reply is spoken including errors, 5 local Piper
  voices, default + per-family voice picker, ElevenLabs voice IDs
  supported.
- **Atlas:** stable cooling simulation (alpha decay, velocity caps,
  cluster seeding) replacing the runaway-then-freeze loop.
- **Usage:** gauge refetches on render and on window focus.
- **Gallery:** folder is now configurable in Settings.
- **Briefing:** pulls official X handles plus web-enabled synthesis so
  it can't end up Reddit-only.
- **Tests:** 42 passing.

## 2026-07-24 — Pytheas 2.0: voice conversations, Courses (NotebookLM), model catalog, email/calendar

Everything shipped in the two build sessions of 2026-07-24.

## Voice
- **Conversation mode** (like the Claude app's voice beta): `ctrl+space`
  starts a conversation; Pytheas listens hands-free (silence detection,
  ~1.5 s), answers aloud, listens again. **`ctrl+alt+space` ends it.**
- Every conversation is saved as a chat in the new **Voice** category —
  including ⚡ context rows for each link opened, app launched, file
  written, and Pytheas section visited during the session.
- The voice model sees the running conversation (real follow-ups).
- Fixed silent TTS: piper + en_US-lessac voice were installed but the
  desktop launcher's PATH missed `~/.local/bin` — `voice.py` now checks
  install paths explicitly. **Free local TTS works now.**
- New settings: hands-free toggle, speak-chat-replies-aloud toggle.

## Models
- Chat/voice engine picker now has all Claude tiers: default, **Fable,
  Opus, Sonnet, Haiku** (`claude --model <alias>`).
- **API providers** (Odysseus-style): add OpenAI / Gemini / Anthropic API /
  any OpenAI-compatible key in Settings; live model lists fetched from the
  provider. Keys in `~/.config/pytheas/providers.json` (0600, never echoed).
- **Weekly model discovery** (zero tokens): re-fetches provider model
  lists + scrapes Anthropic docs; "new Claude models spotted" surfaces in
  Settings.
- Per-provider local usage counters (requests + ~tokens) since most
  providers have no usage API.

## Usage display
- "Fable $" renamed **Usage credits** (it's the shared credit balance —
  Fable always, any model past plan limits). Shows $left, $limit/mo, and
  renewal date once `fable_credit_renews` is set in
  `~/.config/ccdash/config.json` (ccdash patched to support it).
- Sidebar mini-usage got a **provider dropdown** (Claude ↔ API providers).
- **Theme-follows-provider** toggle (claude/terminal/ocean/cyberpunk).

## Courses (NotebookLM)
- New 🎓 section. Courses live in `learning/Courses/<name>/` (visible in
  Obsidian). Drag-drop files/folders → saved + added as NotebookLM sources.
- One-click generation: podcast, video, study guide, quiz, flashcards,
  mind map, infographic. Background jobs; artifacts download into
  `_artifacts/` and play in-app.
- **Organize** button with dropdown (by topic/type/date/auto): model
  proposes a move plan, nothing moves until approved.

## Email + Calendar
- Email: IMAP setup (app password) — inbox list, read messages.
  **Send added**: drafts can be written/edited by hand *or by the chat &
  voice model* (`email_draft` agent tool — drafts only); sending always
  requires the human confirm click, behind the default-off `email.send`
  permission. SMTP host derived from IMAP host.
- Calendar: ICS feeds ("secret address" from Google Calendar), 14-day
  agenda view. Both behind default-off read permissions.

## Atlas
- Fixed: builder emits edges `{a,b}`, UI expected `source/target` → graph
  had 0 links. Also devicePixelRatio, node size by degree, hover labels.
- Clicking a node opens an **md preview pane** first (Open in Notes /
  Obsidian buttons).

## App shell
- New Chat tab removed (＋ lives inside Chats). "Briefing" → **Briefings**
  with placeholder tabs for planned Channel + Finance briefs.
- AI briefing now also covers **official lab X accounts** and **GitHub /
  Claude-plugin ecosystem** (new sections in the prompt + topic).
- Settings rebuilt: Models / API Providers / Voice / Integrations /
  grouped Permissions / Diagnostics.
- **Open & edit anything** permission: ✎ on any file row opens an in-app
  editor for any text file under home (private wall still absolute).
- Input styling fixed (untyped/password inputs were white-on-grey).

## Tests
- Suite recreated: `tests/test_pytheas.py`, **40 tests**, pure logic
  (privacy wall, router, engines, providers, courses, ICS, drafts,
  settings/permissions, usage parsing). `python3 -m unittest discover tests`

## Security decisions
- Model can draft email, never send; send = human click + permission.
- Private-vault wall unchanged and untoggleable.
- Course deletion never deletes files/notebooks as a side effect.
