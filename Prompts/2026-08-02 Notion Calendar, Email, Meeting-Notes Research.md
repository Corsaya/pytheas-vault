---
tags: [pytheas, roadmap, research, notion, calendar, email, transcription, prompt-log]
created: 2026-08-02
status: research complete — decision pending
type: prompt-log
related: ["[[../Ultimate Workspace Roadmap]]", "[[2026-08-02 Notion vs Odysseus vs Pytheas Comparison]]"]
---

# Notion Calendar / email / meeting-transcription research (2026-08-02)

**Prompt:** "Research the way notion calendar works, so that I can have a
universal calendar on every device, or have it link straight to notion
calendar, the email integration and transcribing feature should also be
seen and researched."

**AI:** Claude Sonnet 5 (this session), via WebSearch + a general-purpose
subagent deep-reading 5 sources.

**Context:** Continuing [[../Ultimate Workspace Roadmap]] workstream 7
(Notion-from-Obsidian) and the confirmed build priority #3 (full email send
+ two-way calendar sync) — checking what Notion Calendar itself actually
offers before deciding whether Pytheas should link into it vs. build
independently.

## Findings

**No developer API for Notion Calendar itself.** It exposes a `cron://`
deep-link scheme (open to a specific event) but no data API. The general
Notion API (databases/pages) doesn't cover calendar events. Notion's new
"Developer Platform" (May 2026) adds agent-facing calendar tools (join
calls, send invites, find meeting times) but that's Notion's own AI-agent
surface, not a raw events API third parties can call. **There is no
supported path to bridge Pytheas into Notion Calendar via API** — the only
route would be through Google/Outlook/iCloud calendar APIs directly (which
Notion Calendar itself syncs from) or a Make/n8n relay into a Notion
database, which is a workaround with real maintenance overhead, not a
first-class integration.

**Sync model: cloud-based, automatic, real-time across devices** — macOS,
Windows, iPhone, Android (with widgets). No manual/local-only sync step.

**Two-way sync with Google/Outlook/iCloud: real, but only for events.**
Events created in Notion Calendar push back to the connected provider in
real time. Outlook got full two-way support (view/edit/RSVP/search/
availability/schedule) in a 2026 update. The gap: Notion database
entries/tasks do **not** auto-convert into calendar events on either side —
that still needs manual creation or an external automation bridge.

**AI Meeting Notes (transcription):**
- Routes audio to sub-processors (OpenAI, Anthropic, Fireworks, Baseten
  Labs, X.AI) for transcription/summarization — not one in-house model.
- Desktop app captures system audio + mic (both sides of a virtual
  meeting) and must be running; browser version is mic-only (in-person
  only, and doesn't capture conferencing audio if you're on headphones);
  mobile is mic-only.
- Requires explicit per-meeting consent confirmation from all
  participants.
- Audio isn't stored by sub-processors; local temp copies deleted after
  processing or within 24 hours.
- **Requires Business or Enterprise Notion plan** — not on Free/Plus/
  Personal.

**Notion Mail is shutting down September 22, 2026.** Confirmed by Notion's
own help center, Notion Mail's X account, and multiple outlets. Notion's
stated reasoning: usage shifted to AI agents managing inbox rather than
people opening a client, so they're "going all in on agents running your
inbox" instead of maintaining a standalone mail app. Email data stays
two-way synced with Gmail throughout, so mail history persists in Gmail
after shutdown; drafts/scheduled sends/snippets/labels needed manual export
by September 21. **No Notion Mail integration should be built — dead end.**

## Implications for Pytheas

- **(a) "Universal calendar on every device" via Notion Calendar itself:**
  works today, free, zero special setup — just connect Google/Outlook/
  iCloud in the app. This is arguably the fastest way to get what you
  asked for, with **no Pytheas engineering at all** — but it's Notion's
  calendar, not Pytheas's, so Pytheas wouldn't get visibility/control over
  it without going through the underlying Google/Outlook/iCloud APIs
  anyway.
- **(b) Pytheas building/linking straight into Notion Calendar via API:**
  not supported. If the goal is Pytheas-native calendar sync, the correct
  target is the Google Calendar / Outlook / iCloud CalDAV APIs directly —
  same providers Notion Calendar itself syncs from — not a Notion Calendar
  API that doesn't exist. This matches `Development Roadmap.md`'s existing
  plan to loosen Pytheas's read-only-calendar design (confirmed build
  priority #3) rather than routing through Notion at all.
- **Meeting transcription:** Notion's version requires a paid Business/
  Enterprise plan and its own desktop app running — not something Pytheas
  can piggyback on for free. If Pytheas wants meeting transcription, it's
  a build-your-own feature (e.g. local Whisper or an API call), not a
  Notion integration point.
- **Notion Mail:** drop from consideration entirely — it's gone by
  September 22, 2026.

## Recommendation (not yet decided by Donovan)

Skip trying to integrate *with* Notion Calendar/Mail — there's no API
surface for it and Mail is dying anyway. If "universal calendar everywhere"
is the actual goal, either (1) just use Notion Calendar directly as an
app (zero Pytheas work, but it's not *your* system), or (2) have Pytheas
sync against Google/Outlook/iCloud calendar APIs directly, which is the
same data source Notion Calendar itself reads from — this is already
`Development Roadmap.md` priority #3's direction, just confirming Notion
isn't a shortcut around building it. For transcription, same logic: build
it into Pytheas (local or API-based) rather than depending on a
Business-tier Notion feature.

## Addendum 2026-08-02: Notion API can *read* meeting transcripts, doesn't help build one

Follow-up check: Notion's API version `2026-03-11` replaced the old
`transcription` block type with `meeting_notes`, and can return AI meeting
notes as Markdown — so a developer *with* an existing Notion Business/
Enterprise meeting-notes page can pull the transcript out via API. This is
read-access to Notion's own output, not a transcription service you can
call independently — the recording/transcription step still requires
Notion's desktop app, a paid plan, and per-meeting consent (see above). It
doesn't change the earlier conclusion: Pytheas already has a working local
transcription pipeline (`voice.py` faster-whisper STT, confirmed
functional in code) that's free and self-hosted, which is strictly better
for Pytheas's purposes than depending on Notion's paid, cloud-routed
pipeline. **No action needed here — Pytheas already exceeds what Notion
offers for this specific piece.**

Source: [Notion Developers — Upgrade guide 2026-03-11](https://developers.notion.com/guides/get-started/upgrade-guide-2026-03-11)

## Sources
- [Akiflow — Notion Calendar Integration: What Works and What Doesn't in 2026](https://akiflow.com/blog/notion-calendar-integration-smarter-scheduling)
- [Notion Calendar product page](https://www.notion.com/product/calendar)
- [Notion Help — Calendar connections](https://www.notion.com/help/notion-calendar-connections)
- [Notion Help — AI Meeting Notes](https://www.notion.com/help/ai-meeting-notes)
- [Notion release notes, 2026-05-13 (Developer Platform)](https://www.notion.com/releases/2026-05-13)
- [AlternativeTo — Notion Calendar introduces Outlook integration](https://alternativeto.net/news/2026/6/notion-calendar-introduces-outlook-integration-for-unified-event-management/)
- [Notion Help — Notion Mail inbox is going away](https://www.notion.com/help/notion-mail-inbox-is-going-away-what-to-do-next)
- [The Register — Notion kills its Gmail client after AI agents keep humans from troubling inbox](https://www.theregister.com/ai-and-ml/2026/06/26/notion-kills-its-gmail-client-after-ai-agents-keep-humans-from-troubling-inbox/5263024)
- [TechCrunch — Here is Notion's email client](https://techcrunch.com/2024/10/24/here-is-notions-email-client)
