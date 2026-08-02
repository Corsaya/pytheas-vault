---
tags: [pytheas, mega-prompt, roadmap, comparison, notion, odysseus]
created: 2026-08-02
status: research complete — awaiting preference
type: prompt-log
related: ["[[../Ultimate Workspace Roadmap]]", "[[../Development Roadmap]]"]
---

# Notion vs Odysseus vs Pytheas — capability comparison (2026-08-02)

Continuing [[../Ultimate Workspace Roadmap]]. Researched Notion (cloud,
AI-native workspace) and Odysseus (`pewdiepie-archdaemon/odysseus`,
self-hosted AI workspace — the same project already scouted in
`ai-improvement/fable-5-launch-prep.md` §9 and never adopted, still pending
Docker install as of this pass) against Pytheas's actual shipped feature
set per `Pytheas 2.0 Changelog.md`.

## Snapshot

| | Notion (2026) | Odysseus | Pytheas (current) |
|---|---|---|---|
| Hosting | Cloud only | Self-hosted, Docker or native macOS | Self-hosted, native GTK desktop |
| License/cost | Proprietary, paid AI tiers | AGPL-3.0, free | Private repo, free (your Claude sub) |
| Models | GPT-5.2 / Opus 4.5 / Gemini 3 / Auto-select | 270+ via Cookbook, local Ollama or OpenRouter/OpenAI/Anthropic | Claude subprocess (all tiers) + Ollama + any OpenAI-compatible API |
| Second-brain integration | Its own DB/pages only | Its own docs/notes only | **Native to your actual Obsidian vaults** — cross-vault wikilinks, private-wall enforcement |
| Agents | Custom Agents: autonomous, scheduled/event-triggered, work up to 20 min across hundreds of pages | Agent with shell access | Agent-mode via `claude -p` + fixed MCP tool list (Hermes expansion planned, not shipped) |
| Deep Research | Enterprise Search (workspace + connected tools, cited) | Dedicated Deep Research (multi-step, report generation) | Briefing pipeline (last30days + Claude synthesis) — not a general-purpose Deep Research feature |
| Model comparison | Auto-select only | **Compare** — blind side-by-side model testing | None |
| Email | Not native | IMAP/SMTP, full send | IMAP read + **draft-only** send (human-confirm gate, `email.send` permission) |
| Calendar | Native | CalDAV two-way sync | ICS read-only |
| Meeting notes | Background transcription (iOS/Android, screen-locked) | Not mentioned | None |
| Mobile | Full parity with desktop (Jan 2026) | Not primary focus | None (desktop app only) |
| Image gen | Via connected tools | Native, with gallery | Gallery view only (no generation) |
| Voice | Not a core feature | Not mentioned | **Hands-free conversation mode**, 5 local Piper voices + ElevenLabs, per-model voice routing |
| Usage/cost tracking | Plan-based, no live gauge | Not mentioned | **ccdash gauges** (5h/7d/Fable credit) live in sidebar |
| Developer platform | Workers (sandboxed code), Database sync, External Agent API (May 2026) | MCP support | MCP tools today, wider MCP discovery planned |
| 2FA | Account-level (cloud) | **Built in** | Not applicable (local app, no remote auth surface yet) |
| Auth/security model | Cloud account | Docker self-hosted, own auth | Server-side permission switches (11), private-vault wall un-toggleable |
| Adoption/maturity | Mature, enterprise-scale | ~84.5k★, 929 open issues, young (launched May 2026) | Yours, actively developed, 40+ tests |

## What Notion has that Pytheas doesn't
1. **Custom Agents on schedules/triggers** — Pytheas agent-mode is currently invoked per-conversation, not a background job runner. Closest Pytheas analog: the daily briefing timer, but that's one fixed job, not a general scheduler.
2. **Enterprise Search across connected external tools** — Pytheas searches within vaults/chats; no live connectors to outside SaaS.
3. **Meeting Notes (background transcription)** — nothing like this exists in Pytheas.
4. **Full mobile parity** — Pytheas is desktop-only.
5. **External Agent API / Workers sandbox** — lets *other* agents plug into the workspace; Pytheas doesn't expose itself as a host for third-party agents.

## What Odysseus has that Pytheas doesn't
1. **Deep Research as a first-class feature** (multi-step web research → structured report), separate from the briefing pipeline.
2. **Compare** — blind side-by-side model output comparison. Directly useful for your "test multiple models, confirmed/denied edits" testing goal.
3. **Cookbook** — model recommendations matched to your actual hardware, across 270+ models. Pytheas has model discovery but not hardware-aware recommendation.
4. **Full email send + CalDAV two-way calendar sync** (Pytheas is deliberately more conservative here — draft-only send, read-only calendar — which is a safety choice, not an oversight).
5. **Native image generation + gallery**, **2FA**.
6. **Agent shell access** shipped today (Pytheas's equivalent is roadmapped as "Hermes," not yet built).

## What Pytheas has that neither Notion nor Odysseus have
1. **Real cross-vault Obsidian integration** — private-vault wall (`Journal/Daily/Work` un-toggleable), wikilink navigation across 8 vaults, Atlas graph visualization of your actual second brain. This is the moat — neither competitor knows your vault structure at all.
2. **ccdash usage-credit gauges** tied directly to your Claude subscription tiers (5h/7d/Fable), so you see spend in real time instead of guessing.
3. **Per-model/per-engine voice routing** with hands-free conversation mode, entirely local by default (Piper).
4. **Deliberate safety gating on irreversible actions** (draft-only email send, confirm-gated agent actions) — a design stance, not a missing feature.
5. **Courses via NotebookLM** generating podcast/video/study guide/quiz/flashcards/mind map/infographic from vault content — this is the exact mechanism your SAT/coding/AI-prompting course tracks depend on, and neither competitor has a vault-grounded equivalent.

## Notes for the roadmap
- Odysseus was already scouted and never adopted (`fable-5-launch-prep.md` §9: "adopt as GUI/email layer, shared vault memory," pending Docker). This research confirms it's still a live, maturing option — worth an actual hands-on trial now rather than re-scouting later.
- Sources: [pewdiepie-archdaemon/odysseus GitHub](https://github.com/pewdiepie-archdaemon/odysseus), [Notion AI review 2026 — eesel AI](https://www.eesel.ai/blog/notion-ai-review), [Notion developer platform for AI agents — InfoWorld](https://www.infoworld.com/article/4171166/notion-courts-developers-with-platform-for-ai-agents-and-workflow-automation.html), [Odysseus review — XDA Developers](https://www.xda-developers.com/tried-pewdiepie-open-source-ai-workspace-odysseus-weirdly-great/).

## AI usage
Claude Sonnet 5, Claude Code CLI — WebFetch (Odysseus README) + WebSearch
(Notion AI 2026 features, Odysseus reviews) + vault grep for prior scouting
notes. No code changes.

## Result
Comparison built; feeding into the next roadmap step — Donovan picks
priorities from the "what Notion/Odysseus has that Pytheas doesn't" lists
above, then hands-on testing (install guide follows in chat) confirms which
gaps are real pain points vs. nice-to-haves before anything gets built.
