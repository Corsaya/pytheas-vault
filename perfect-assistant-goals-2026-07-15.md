---
date: 2026-07-15
tags: [jarvis, roadmap, goals]
---

# Perfect Assistant — Goals & Route (2026-07-15)

From Donovan's 07-15 thought dump. Companion to [[Jarvis Progress Guide]];
this is the *what's next and why*, that one is the *what exists*.

## The four capability goals, with honest status

### 1. Search repos + social media for self-improvement ✅ built
- `jarvis` briefing (DEC-024): daily AI-news fetch covers Anthropic news,
  X/Twitter builder sentiment, and short-form creator trends.
- `~/code/repo-scout`: `search` (gh-backed, scored) + `adopt` (shallow clone
  into `~/code/_sandbox/` + security checklist).
- `~/code/jarvis/SELF-IMPROVEMENT.md`: discover → evaluate → adopt → record.
- Remaining: actually *run* the loop weekly. It's built, not yet habitual.

### 2. Act like the other Jarvis-esque projects
Scouted field lives in the capability-scouting Links note. What they have
that we don't yet: **voice**, **GUI**, **computer actions** (open apps, file
ops on request). Computer actions = the "ease of access of my computer" goal;
route it through the propose-then-approve protocol (vierisid/jarvis's
"authority limits" pattern was flagged for exactly this — re-read it first).
**Update (same day):** first cut shipped as `~/code/jarvis-desk` — localhost
panel with the live atlas, file browser/opener, read-only claude Ask, and
confirmed-only Run. GUI ✅ and computer actions ✅ (open/run tier); screen
control stays with Hermes's computer-use-linux as an unvetted candidate.

### 3. Respond as an AI voice
DEC-005 deferred voice to v2; push-to-talk ranked first. Local-first stack,
both already queued as candidates:
- **TTS:** rhasspy/piper — small, fast on CPU, sounds decent.
- **STT:** SYSTRAN/faster-whisper — Python-native, fits the codebase.
Plan: safe-adopt piper first (TTS alone gives "responds as an AI voice"),
inject it as an output transport so tests stay runnable without audio.
Dependency rule applies: both need written justification + approval
(PyYAML-only rule), so this is a propose-first session, not a drive-by.

### 4. Downloadable on the laptop
Nothing blocks this today:
1. `git clone` the repo (or push to a private GitHub remote first — cleaner).
2. `pip install -e .` — PyYAML is the only dependency.
3. Install Claude Code, run `claude setup-token` on the laptop.
4. Copy `~/.config/jarvis/` config; state files live per-machine in
   `~/.local/state/jarvis/` (briefing markers are *supposed* to be
   per-machine — don't sync those).
5. Optional: Syncthing (unvetted, in Links) to share the Obsidian vault so
   both machines see the same memory.

## Odysseus as the AI workspace

Decision already on record (Links.md, scouted 2026-07-01, re-affirmed by
this dump): **adopt as a second front-end sharing the vault as memory** —
GUI chat/agents, email, calendar, deep research, local models via
Ollama/llama.cpp, AGPL-3.0, Docker Compose deploy. Don't rebuild it; don't
make it critical infra (~1,400 open issues — daily driver only). Jarvis
stays the lean, tested, terminal core with propose-then-approve; Odysseus
becomes the workspace shell around it. First step when ready: safe-adopt
protocol on the repo, then Docker deploy on the PC before the laptop.

## Graduating from Claude (own model)

Long-run goal, staged honestly:
1. **Use** local models as the free/fast tier (Ollama; Odysseus's Cookbook
   picks models per hardware). Ceiling is far below Fable 5 — tier, not
   replacement (already noted in Links).
2. **Understand** them — the ML block in the learning vault's
   [[Learning Plan]] (neural-nets-from-scratch track) is the prerequisite.
3. **Fine-tune** a small open model on our own data (session wraps, vault,
   DECISIONS style) — first genuinely "own" model.
4. **Train from scratch** only if 1–3 prove it's worth it.

## The mutual-improvement loop

Jarvis improves Donovan (lessons, plans, schedules, goal memory) while
Donovan improves Jarvis (surveys, `/remember`, `jarvis improve`, gotchas).
The money side funds it: see [[product-idea-private-journal-app]] and
[[anonymous-home-income]] in the finance vault. The journal app is
deliberately the first product because it *is* Jarvis's memory/goal engine
pointed at other people — building it compounds.
