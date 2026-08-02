---
date: 2026-08-02
tags: [pytheas, session-wrap, mega-prompt, roadmap, odysseus, notion, sat, comparison, deep-research, compare, prompt-logging]
---

# Pytheas Session Wrap — 2026-08-02

Kicked off by Donovan's mega-prompt: turn Pytheas into a full Claude-Code-parity,
multi-model, Odysseus-like workspace, teach him coding/SAT/AI-prompting
through Courses, log every prompt in-vault, and eventually stop needing AI
to build things himself. SAT is 21 days out (19 remaining as of today).
Full raw prompt saved verbatim in
[[../Prompts/2026-08-02 Mega Prompt — Ultimate Workspace Vision]].

## Decisions confirmed today
- **Prompt-logging convention** established and written into
  `~/Documents/Obsidian/CLAUDE.md`: every substantive prompt → a file in
  the relevant vault's `Prompts/` folder, tagged, with AI usage + result
  included. This session-wrap is the second layer of that (per-session
  summary, mirroring the existing `jarvis-session-wrap-*` convention).
- **SAT sequencing: strict.** No SAT course-building starts until Pytheas
  capability testing is to Donovan's standard — accepted risk against the
  21-day clock.
- **Hermes autonomy split:** read-only actions auto-approved, anything
  mutating state (shell, file write/delete, opening apps, send) stays
  confirm-gated — matches `Development Roadmap.md` workstream 4 as already
  designed, no change needed.
- **Social-media harvesting (IG/X/TikTok):** custom build using Donovan's
  own logins, not `last30days`. Not started — real coding project for
  `~/code/pytheas` or a scraper module, credentials via local `.env`
  (gitignored), flagged for its own security pass (anti-automation
  detection risk, account-lockout risk).
- **Five build priorities confirmed** after the Notion/Odysseus comparison
  (full detail in [[../Ultimate Workspace Roadmap]]): Deep Research +
  Compare, scheduled/autonomous agents, full email send + 2-way calendar
  (intentional loosening of current draft-only/read-only safety default),
  Courses end-to-end test, and Gemini/NotebookLM credential verification
  (NotebookLM is the actual Courses engine — a Gemini API key alone may
  not grant NotebookLM access, needs checking against `courses.py`).

## Research done
[[../Prompts/2026-08-02 Notion vs Odysseus vs Pytheas Comparison]] — full
capability comparison table. Findings: Notion has scheduled Custom Agents,
Enterprise Search, Meeting Notes, mobile parity, External Agent API that
Pytheas lacks; Odysseus has Deep Research, Compare, hardware-aware
Cookbook, full email/calendar, image gen, 2FA that Pytheas lacks; Pytheas
has real cross-vault Obsidian integration, ccdash usage gauges, per-model
voice routing, and safety-gated actions that neither competitor has.

## Odysseus — installed and hands-on tested
Cloned `pewdiepie-archdaemon/odysseus` to `~/code/odysseus`, brought up via
`docker compose up -d --build` (chromadb, ntfy, searxng, odysseus-app
containers). **This is a third-party upstream repo — not ours to push to,
and not part of tonight's "push everything."**

**Setup troubleshooting (logged in detail in
[[../Ultimate Workspace Roadmap]]):**
- Admin temp password is only in `docker logs`, not shown in-UI.
- Host Ollama was `127.0.0.1`-only; rebound to `0.0.0.0:11434` via a
  systemd drop-in so the Docker container could reach it.
- ufw (active, default-deny incoming) needed a rule scoped to the
  **Compose-created network's actual subnet** (`172.18.0.0/16`, not the
  default `docker0` bridge `172.17.0.0/16` — Compose makes its own network
  per project). Rule scoped to that subnet only, not LAN/internet-wide.
- Tried the built-in `LOCALHOST_BYPASS` dev flag to let Playwright in
  without a password — doesn't work through Docker's port-publishing
  (source IP isn't real loopback from the container's perspective).
  Reverted; logged in with real credentials instead.

**Hands-on feature tests (via Playwright browser automation):**
- **Chat** — works cleanly; `qwen3:8b` answered correctly with a visible
  reasoning/thinking trace.
- **Compare** (blind A/B) — works well; real result: `gemma:2b` failed a
  calculus-explanation prompt outright ("not defined in context, see a
  textbook") while `qwen3:8b` gave a correct, well-reasoned answer. Also
  caught a bug: local Ollama models show a fake per-1k-token dollar cost
  in the UI (`$0.51/1k`) — should be $0 for local inference.
- **Deep Research** — ran a real SAT-strategy query end to end: 382s, 3
  rounds, 25 URLs, 18 kept sources, produced a genuinely well-structured,
  cited report (saved in full at
  [[../Prompts/2026-08-02 Odysseus Deep Research Test — SAT Prep]]).
  Found a real defect worth designing around: the 8B model's query
  decomposition grabbed stray words from the prompt ("most," "top") and
  searched them literally, pulling in 3 junk sources (a dictionary
  definition, Topgolf, a Wikipedia domain-name article). Synthesis
  correctly ignored the junk, but it's wasted research rounds — implies
  Pytheas's own Deep Research build should test with a larger model before
  trusting an 8B default for the decomposition step specifically.

**GPU note:** sustained inference load during Compare/Deep Research hit
99% utilization, ~180W/200W, 74-76°C — normal, safe operating range for
the RTX 4070 (throttle point is ~83-87°C), not a damage risk. Confirmed
with Donovan mid-session after a "chill on my GPU" check-in; throttled
back to lightweight `curl`-based status polling instead of repeated
headless-browser reloads once he flagged it.

## Not started (explicitly deferred to next session)
Scheduled/autonomous agents, full email send + 2-way calendar build,
Courses end-to-end test, Gemini/NotebookLM credential check, cross-vault
`Prompts/` rollout to other vaults, per-model Ultimate Reference doc. All
still on [[../Ultimate Workspace Roadmap]] — nothing lost.

## Files touched this session
- `~/Documents/Obsidian/CLAUDE.md` — added prompt-logging convention.
- `pytheas/Prompts/2026-08-02 Mega Prompt — Ultimate Workspace Vision.md` (new)
- `pytheas/Prompts/2026-08-02 Notion vs Odysseus vs Pytheas Comparison.md` (new)
- `pytheas/Prompts/2026-08-02 Odysseus Deep Research Test — SAT Prep.md` (new)
- `pytheas/Ultimate Workspace Roadmap.md` (new, then updated twice with
  confirmed decisions and setup notes)
- `pytheas/session-wraps/pytheas-session-wrap-2026-08-02.md` (this file)
- `~/code/odysseus/` — new clone, running locally (not pushed, upstream repo)
- Host system: `/etc/systemd/system/ollama.service.d/override.conf` (new),
  ufw rule added for `172.18.0.0/16:11434/tcp`

## Goal check-in
Donovan's stated end goal: move his day-to-day AI usage from Claude Code
to Pytheas itself, with SAT improvement as the first real proving ground.
Tonight's session was capability research + hands-on troubleshooting
(comparison + Odysseus trial), not Pytheas code changes — next session
picks up the five confirmed build priorities against `~/code/pytheas`.
