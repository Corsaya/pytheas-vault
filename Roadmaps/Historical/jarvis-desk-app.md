---
date: 2026-07-16
tags: [jarvis, jarvis-desk, app, roadmap]
---

# Jarvis Desk — the native app (2026-07-16)

The desktop program requested in the 07-16 dump: "a real program on my
computer… the vault is just one tab… Odysseus workshop format… lots of
permissions and integrations I enable… AI should be local… Odysseus+."

Repo: `~/code/jarvis-desk` (private: github.com/TheBiggerMann/jarvis-desk).
Launch: app launcher → **Jarvis Desk** (installed), or `python3 app.py`.

## What shipped

- **Native GTK window** (not a browser): server runs inside the app process,
  embedded WebKit view, mic permission scoped to the app.
- **Sections**: Chat · Vaults · Atlas · Files · Voice · Run · Usage · Settings.
- **Chat engines**: `qwen3:8b` (pulled 07-16, runs on the 4070 — fully
  private) and `gemma:2b` via Ollama, or Claude subprocess (read-only tools;
  web search only if its permission is on). History kept per conversation.
- **Vaults section**: file tree per vault, full markdown rendering incl.
  images, wikilinks navigate across vaults inside the app, private paths
  locked server-side.
- **Permissions**: 11 switches in Settings, enforced on every request
  server-side. Acting capabilities (open programs, web links, shell, cloud
  voice, Claude-web) default OFF. The private-vault wall has no switch.
- **Usage**: ccdash gauges (5h/7d/Fable) in the sidebar, full tab with bars.

## Verified working (07-16)

Ollama chat, Claude chat with history recall, permission flip live-enforced,
private tree flags (Journal/Daily/Work), raw-attachment privacy guard,
usage gauges, voice roundtrip (earlier same-day), AppImage rebuild.

## Relationship to Odysseus

Odysseus itself still pending (needs Docker — manual install steps given to
Donovan 07-16). Jarvis Desk is the lean, auditable version of the same idea;
if Odysseus gets adopted later it becomes the heavyweight sibling, not a
replacement. Decision log lives in capability-scouting Links.

## Morning AI Briefing (added 2026-07-16, "first build")

- **☀ Briefing tab** (first in the sidebar): AI news *since the last
  briefing* — the since-marker lives in
  `~/.local/state/jarvis-desk/briefing.json`, so no repeated news.
- Sources (all verified live via last30days preflight): **Reddit, X (via
  Chromium cookies + bundled bird scraper), Instagram + TikTok (via free
  ScrapeCreators key, 10k calls, GitHub-device-auth'd 07-16), YouTube, HN,
  Polymarket, GitHub, web**. Config in `~/.config/last30days/.env`
  (key never in any repo).
- Pipeline: last30days pull → claude synthesis (sub-600-word brief) →
  saved to `Briefings/YYYY-MM-DD.md` in this vault → rendered + speakable
  (▶ Play) in the app. Fallback: claude+websearch if the engine fails.
- **07:00 daily timer** installed (`systemctl --user status
  jarvis-briefing.timer`) — the brief is waiting when the app opens.
- Note: X-via-cookies scrapes with Donovan's login; small account risk.
  Alternative if ever worried: XQUIK_API_KEY (paid) or drop X.

## Next candidates

- Screen-control tier via a computer-use MCP (Hermes computer-use-linux —
  unvetted) behind a new permission switch.
- Streaming chat + markdown rendering of AI replies.
- Laptop install (same steps as jarvis: clone, install-desktop.sh).
- Windows .exe build (PyInstaller on Windows; swap xdg-open→os.startfile).
