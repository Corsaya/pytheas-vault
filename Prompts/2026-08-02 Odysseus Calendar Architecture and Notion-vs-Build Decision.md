---
tags: [pytheas, roadmap, research, odysseus, caldav, calendar, notion, prompt-log, decision]
created: 2026-08-02
status: research complete — leaning decision, awaiting confirmation
type: prompt-log
related: ["[[../Ultimate Workspace Roadmap]]", "[[2026-08-02 Notion Calendar, Email, Meeting-Notes Research]]", "[[2026-08-02 Notion vs Odysseus vs Pytheas Comparison]]"]
---

# Odysseus calendar architecture + "is Notion best?" decision (2026-08-02)

**Prompt:** "Have Pytheas sync against Google/Outlook/iCloud calendar APIs
directly, how does Odysseus' calendar work, is notion the best option
overall? I like everything linked to my obsidian, including email and
calendar."

**AI:** Claude Sonnet 5 (this session) — read Odysseus source directly
(`~/code/odysseus`, already installed per
[[2026-08-02 Notion vs Odysseus vs Pytheas Comparison]]) via an Explore
subagent, plus one web check on Google's CalDAV API status.

## How Odysseus's calendar actually works

- **Protocol: CalDAV** (`src/caldav_sync.py`), via the pure-Python `caldav`
  library — works against Google Calendar, Nextcloud, Radicale, Apple
  iCloud, Fastmail. Not the Google Calendar API, not MS Graph, not plain
  ICS import.
- **Two-way.** Pull: remote → local SQLite, upsert by VEVENT UID, delete
  local rows no longer seen remotely. Push: local edits build a VEVENT and
  PUT/DELETE it back via CalDAV (`src/caldav_writeback.py`, wired into
  `routes/calendar_routes.py`). Local DB is the source of truth; a failed
  remote push is logged, not fatal.
- **Auth: CalDAV username + app-password, not OAuth** — stored per-account,
  Fernet-encrypted at rest (`src/secret_storage.py`, key at
  `data/.app_key`, mode 0600, gitignored). SSRF-hardened against
  localhost/private IPs by default.
- **Local data model**, not live-API-on-every-read: `CalendarCal`,
  `CalendarEvent`, `CalendarDeletedEvent` tables in `core/database.py`. UI
  and agent always read local SQLite; CalDAV sync just refreshes it.
- **No separate calendar MCP server** — it's a native agent tool
  (`manage_calendar`, `src/tools/calendar.py`) doing CRUD on local SQLite
  and triggering write-back, registered like any other tool.

## Is Google/Outlook/iCloud CalDAV actually usable?

Checked because I'd have assumed Google locked this down — it hasn't.
Google still runs a CalDAV server for Calendar (Google's own dev docs,
[developers.google.com/workspace/calendar/caldav/v2/guide](https://developers.google.com/workspace/calendar/caldav/v2/guide)),
with a May 2026 quota update but no deprecation. It's the same mechanism
Apple Calendar and Thunderbird use to sync Google Calendar today. Outlook.com
and iCloud both run their own CalDAV servers natively. **So one protocol
(CalDAV) genuinely covers Google + Outlook + iCloud + Nextcloud/Radicale —
Odysseus's choice is well-founded, not a workaround.**

## Is Notion the best option overall?

**No — given your stated preference ("everything linked to my Obsidian,
including email and calendar"), Notion is close to the worst fit, not the
best:**

- Notion Calendar has no developer API (previous research note) — it can
  only ever be *another app you also use*, never something wired into your
  Obsidian vault. Nothing in it can surface inside a note, a daily log, or
  Atlas.
- Notion Mail is shutting down September 22, 2026 — a dead end regardless
  of preference.
- Notion's calendar/email are fundamentally **their** data model (pages/
  databases + their own calendar UI), not yours — the opposite of the
  Obsidian-native, vault-first design Pytheas already has for everything
  else (courses, briefings, research all write back into markdown you own).

**Odysseus's CalDAV approach is the right shape to copy, not Notion's.**
CalDAV gives Pytheas the same thing Odysseus has — two-way sync against
Google/Outlook/iCloud, a local data store Pytheas fully controls — and
because Pytheas is already Obsidian-native, events can additionally be
surfaced *inside vault markdown* (e.g. a daily note calendar block, an
Atlas node, a Courses deadline pull) in a way Notion structurally cannot
do for you, and Odysseus doesn't attempt (it stays inside its own SQLite/
UI, not a linked knowledge vault).

Email: same logic — IMAP/SMTP directly (which Pytheas already has for
read + draft-only send) is the Obsidian-compatible answer; Notion Mail was
never viable and is now moot.

## Recommendation

Do **not** integrate with or route through Notion for calendar or email.
Build calendar sync into Pytheas using the same CalDAV architecture
Odysseus already proves out:
1. `caldav` library, per-account creds (app passwords), Fernet-encrypted
   at rest — same pattern, don't reinvent.
2. Local SQLite (or reuse whatever Pytheas's existing storage is) as
   source of truth, two-way push/pull, so Pytheas isn't hitting the
   provider API on every read.
3. Because Pytheas is vault-native, add the piece Odysseus doesn't have:
   surface calendar data *into* Obsidian markdown (daily notes, Atlas,
   Courses deadlines) — this is the actual differentiator over both Notion
   and Odysseus.
4. This directly extends `Development Roadmap.md`'s existing plan to move
   Pytheas's calendar from read-only ICS to full two-way sync (confirmed
   build priority #3 in [[../Ultimate Workspace Roadmap]]) — CalDAV is the
   concrete protocol choice for that workstream, now decided rather than
   open.

**Not yet decided:** whether to build this now or after SAT (per the
existing strict-sequencing rule), and whether iCloud/Google/Outlook all
need day-one support or just whichever Donovan actually uses day to day.

## Sources
- Odysseus source: `~/code/odysseus/src/caldav_sync.py`,
  `src/caldav_writeback.py`, `src/secret_storage.py`,
  `routes/calendar_routes.py`, `core/database.py`, `src/tools/calendar.py`
- [Google CalDAV API Developer's Guide](https://developers.google.com/workspace/calendar/caldav/v2/guide)
- [Google Calendar API release notes](https://developers.google.com/workspace/calendar/release-notes)
