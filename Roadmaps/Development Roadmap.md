---
tags: [pytheas, roadmap]
created: 2026-07-29
status: active
---

# Pytheas Development Roadmap — 2026-07-29

Four workstreams, in the order they unblock each other: **Atlas fix** (fast,
isolated, no dependencies) → **environment context injection** (makes every
model that comes after it competent) → **vault pyramid agents** (needs the
context layer) → **Hermes** (needs both — it's the thing that acts on what
the pyramid knows, described in the voice the environment layer teaches).

Repo: `~/code/pytheas` (Odysseus fork at `~/code/chiron`). Vaults:
`~/Documents/Obsidian/{pytheas, learning, finance, life,
agonizing-sentience}` — see `~/Documents/Obsidian/AGENTS.md` (or `CLAUDE.md`)
for the access rules every agent below must respect.

> [!warning] Header corrected 2026-08-25
> This block previously listed the pre-restructure vault roots (`personal`,
> `ai-improvement`, `card-flip`, `minecraft-event` as top-level) and stated
> that `personal/Journal`, `personal/Daily`, `personal/Work`, and
> `personal/Private-Reference.md` were "never AI-readable, never AI-writable,
> no exceptions." **Both are retired** — the vaults were restructured
> 2026-08-12 and the standing private wall was dropped the same day. Access is
> now open by default across all vaults; the single override is a doc Donovan
> marks **"locked"**. The four workstreams below are unaffected and still live.
> Current direction: `Operations/Handoff/02 — AI Workspace Master Plan.md`.

---

## 1. Atlas — full-screen, interactive, non-bunching graph

**Current state** (`static/sections.js:861-1020`, `static/style.css:396-409`):
canvas-based force-directed graph, vaults seeded as radial clusters,
d3-style cooling simulation. Three concrete bugs:

- `#atlas-wrap { height: calc(100vh - 170px) }` — hardcoded height budget,
  not actually the full viewport, and brittle if the header/sidebar chrome
  changes height.
- Canvas size is read once at `render()` (`canvas.offsetWidth/Height`) with
  no `ResizeObserver`/window-resize listener — resizing the window or
  toggling the preview pane leaves the simulation drawing at the stale size,
  which reads as nodes "bunching" into a corner.
- No pan or zoom. The charge force (`d2 < 6000` cutoff) is the only thing
  keeping nodes apart; once note count grows past ~150-200 the canvas is
  simply too small for the force to spread them out, and there's no way to
  scroll in and look at a dense cluster.

**Target state:** Atlas takes the full section viewport (not `100vh -
170px`), stays correctly sized across window resizes and preview-pane
toggles, and supports scroll-to-zoom + click-drag-to-pan so dense clusters
are inspectable instead of an unreadable smear.

**Plan:**
1. CSS: `#atlas-wrap { height: 100%; }` inside a section container that's
   already `height: 100vh` minus real chrome via flexbox (`flex: 1;
   min-height: 0`), not a magic-number subtraction.
2. `ResizeObserver` on `#atlas-wrap` → recompute `canvas.width/height` and
   re-run `redraw()` (not the full sim restart — just redraw at new scale).
3. Add a view transform: `{scale, offsetX, offsetY}` applied in `redraw()`
   before drawing nodes/links. Wheel event → zoom around cursor position;
   mousedown+drag (when not hitting a node) → pan. `nearest()` needs to
   invert the transform when hit-testing.
4. Bump the charge-force cutoff / add a minimum-separation pass so dense
   note clusters settle further apart by default, less reliant on manual
   zoom to be legible.

**Effort:** small — one focused session, no backend changes, no new
dependencies (still stdlib canvas, no d3/pixi).

**2026-08-04 addendum:** evaluated `github.com/Graphify-Labs/graphify` as a
possible base for this rebuild (Donovan's request). Doesn't fit — it's a
Python codebase-analysis tool (tree-sitter + Leiden clustering over source
code), not a note-graph renderer. If pan/zoom ends up wanting more than the
hand-rolled canvas transform in the plan above, a real JS graph library
(d3-force, Cytoscape.js, or Sigma.js) is the right escape hatch, not
Graphify. See `Ultimate Workspace Roadmap.md` workstream 12 for the full
writeup.

---

## 2. Environment context injection (not fine-tuning)

**Why this comes before the pyramid and Hermes:** every local Ollama model
and every Claude tier currently answers Pytheas questions from general
knowledge only — `chats.py`'s `ASK_GUARD` is a privacy rule, not a
description of what Pytheas *is*. A vault-pyramid agent or a Hermes with
full tool access is only as good as its understanding of the environment
it's operating in (what vaults exist, what's private, what tools exist,
what "confirm before running" means here). Fine-tuning was considered and
rejected for now — it's expensive to keep current as Pytheas changes weekly,
and context injection gets ~95% of the benefit for near-zero cost.

**Plan:**
1. **`environment.py`** (new module) generates a single `ENVIRONMENT.md`-style
   context block from live state, not hand-maintained prose:
   - Vault list + AI-scope rules, sourced from `~/Documents/Obsidian/CLAUDE.md`
     (parse the "AI scope per area" section rather than duplicating it —
     one source of truth, no drift).
   - Tool catalog: read `pytheas_mcp.py`'s `TOOLS` list and `permissions.py`'s
     `PERMISSIONS` dict directly (they're already structured data) to
     produce "here's what you can do, and whether it's currently on."
   - API surface: the `/api/*` routes Pytheas exposes (courses, research,
     briefing, email, calendar) so a model asked "can Pytheas do X" answers
     from what's actually wired up, not a guess.
   - A version/hash stamp so stale context is detectable.
2. Inject this block into **every** engine path in `chats.py` /
   `models.py` — Claude subprocess, Ollama, and API providers alike — the
   same way `ASK_GUARD` is injected today. One system-prompt prelude
   function, called from all three send paths.
3. Regenerate on Pytheas startup and whenever `permissions.json` or
   `CLAUDE.md` changes (cheap: a file mtime check, not a watcher daemon).
4. **API-driven, not hardcoded:** the whole point of generating this from
   `PERMISSIONS`/`TOOLS`/`CLAUDE.md` instead of writing it by hand is that
   turning a permission on/off or adding an MCP tool updates every model's
   understanding automatically on next send — no prompt file to remember to
   edit.

**Effort:** medium — mostly plumbing (one new module, one injection point
reused three times), the design risk is keeping the generated block short
enough not to eat context on every single turn (target: under ~800 tokens).

---

## 3. Vault pyramid — Pytheas apex + one agent per vault

**Shape:** Pytheas is the top-level orchestrator. Each AI-accessible vault
(`learning`, `ai-improvement`, `finance`, `pytheas`, `agonizing-sentience`,
`card-flip`, `minecraft-event`, and the AI-readable slice of `personal`) gets
a scoped sub-agent that only reads/writes inside its own vault and reports
up. This mirrors the private-vault-guard pattern that already hard-blocks
`personal/Journal` etc. at the hook level — the pyramid formalizes the same
idea for every vault, not just the walled-off one.

**Plan:**
1. **Registry, not hardcoded per-vault code.** A `vaults.json` (or generated
   from `CLAUDE.md`, same parser as workstream 2) listing each vault's path,
   AI-read/write scope, and any sub-exclusions (Journal, Daily, Work,
   Private-Reference.md for `personal`).
2. **Per-vault agent = a scoped system prompt + a filesystem jail**, not a
   separate process per vault. Reuse the existing `claude -p` subprocess
   path in `chats.py`, but the "vault agent" is a call variant that (a)
   injects only that vault's slice of the environment context from
   workstream 2, (b) is passed a working-directory / allowed-path
   restriction so a bug can't leak into a sibling vault, (c) inherits the
   same permission-gated action tools as everything else — no new
   capability class.
3. **Pytheas (apex) role:** routes a request to the right vault agent(s)
   based on which vault(s) the question touches (can be multi-vault — e.g.
   "what's due in AP Chem and did I log it in card-flip" spans `learning`
   and `card-flip`), and synthesizes their answers. This is the same
   fan-out/synthesize shape as the existing `last30days` research pipeline
   in `research.py`, reused rather than reinvented.
4. **Private-vault wall is unchanged and non-negotiable:** the `personal`
   vault agent inherits the exact same read exclusions
   (`Journal/Daily/Work/Private-Reference.md`) as today's guard, and there
   is still no vault agent for anything the hook currently blocks writes to
   beyond the existing `Health` allowlist exception.

**Effort:** medium-large — the mechanism (scoped subprocess call + registry)
is straightforward; most of the work is testing that scope leaks don't
happen (a vault agent asked something out of its lane should say so, not
guess from training data or peek at a sibling vault).

**Open question to confirm before building:** should vault agents be
addressable directly in chat (e.g. `@learning what's due this week`), or
only reachable through Pytheas's routing? Recommend routing-only for v1 —
direct addressing is a UI feature that can layer on later without changing
the underlying mechanism.

---

## 4. Hermes — Claude-Code-parity agent inside Pytheas chats

**Current state:** agent-mode already exists — `ai.agent` permission +
`pytheas_mcp.py` gives a `claude -p --mcp-config` subprocess hands (open
app, open note, window control, screenshots, file open) via HTTP calls back
to the Pytheas server, each gated by its own `permissions.py` switch and
logged. This is 80% of Hermes already; it's currently scoped to one-off
Ask/Agent calls, not a named, consistent identity across chats and voice
conversations.

**Target (per your answer: full parity including MCP tool access):**
Hermes is Pytheas's acting persona — available in any chat or voice
conversation (not just a special "Agent" tab), with the same breadth of
action Claude Code has: read/write files, run shell commands (behind
confirm, per `shell.run`'s existing default-off + confirm-click pattern),
open apps/links/notes, control windows, see the screen, and reach any MCP
server Pytheas is connected to — not just the fixed `TOOLS` list in
`pytheas_mcp.py` today.

**Plan:**
1. **Name and surface it.** Give the existing agent-mode engine a stable
   identity ("Hermes") shown in the chat UI when `ai.agent` is on, so it's
   clear to you when a conversation can act vs. when it's a plain Ask. Every
   engine picker entry that currently says "Claude (agent mode)" becomes
   "Hermes."
2. **Make it a chat-native engine, not a separate mode.** Currently agent
   mode is invoked differently from a normal chat send; unify so any chat
   or voice conversation can be *assigned* the Hermes engine the same way
   it's assigned `claude:sonnet` or `ollama:llama3` today (`chats.py`'s
   engine-string convention — add `hermes` as a first-class engine value).
3. **Widen the tool surface to real MCP, not a fixed list.** Today
   `pytheas_mcp.py` hardcodes ~6 tools. Full parity means Hermes can attach
   to any MCP server configured for the session (same discovery Claude Code
   itself uses) in addition to the native Pytheas action tools — so Hermes
   in a Pytheas chat has the same reach as Claude Code in a terminal,
   scoped by the same `permissions.py` switches either way.
4. **Every new tool call still round-trips through the Pytheas server**
   (the existing design: the MCP bridge process holds no capabilities of
   its own, every action is an HTTP POST enforced and logged server-side).
   This is the right shape to keep — extending the tool surface doesn't
   mean loosening where enforcement happens.
5. **Environment-aware by construction:** Hermes gets the workstream-2
   context block on every turn, so it knows the vault-pyramid layout, which
   permissions are live, and what it's allowed to touch before it tries.
6. **Confirm-gated destructive actions stay confirm-gated.** `shell.run`
   and any file-write/delete action keep the existing confirm-click pattern
   — "full parity with Claude Code" means capability, not silently skipping
   the safety rail Claude Code itself doesn't have a UI for in a chat
   context.

**Effort:** medium-large — mostly widening `pytheas_mcp.py` from a fixed
tool list to real MCP client/discovery, plus the chat-engine unification.
The permission/logging backbone already exists and doesn't need
re-architecting.

**Sequencing note:** build workstream 2 (environment context) before
Hermes gets its expanded tool surface — an agent with shell access and no
grounding in what it's allowed to touch is a worse idea than the same agent
with grounding.

---

## Housekeeping surfaced during this pass

- `~/Documents/Obsidian/CLAUDE.md` still refers to a `jarvis/` vault; that
  vault is retired (superseded by `pytheas/`, migrated 2026-07-29 — Courses,
  memory, Research, and Briefings all now live under `pytheas/`). The vault
  doc's "Vault layout" section needs an update pass to replace `jarvis/`
  references with `pytheas/`; flagging rather than editing since that file
  documents AI-scope rules and changes there should be deliberate, not a
  side effect of this roadmap.
- The old `jarvis/` vault folder itself (`~/Documents/Obsidian/jarvis/`)
  still exists on disk with two stale duplicate notes; nothing writes to it
  anymore as of this pass. Delete whenever you're ready — not done
  automatically.
