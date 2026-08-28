# Pytheas — custom voices & why the briefing was Reddit-only

## Adding custom TTS voices

Pytheas speaks through **piper** (free, local, offline) with optional
**ElevenLabs** (paid, best quality). Installed voices live in
`~/.local/share/jarvis-desk/voices/`.

**Installed now:** `en_US-amy-medium` (warm female), `en_US-ryan-medium`
(male), `en_US-joe-medium` (male, deeper), `en_GB-alba-medium` (Scottish
female), `en_US-lessac-medium` (neutral, original default).

### Add another piper voice
1. Browse samples: <https://rhasspy.github.io/piper-samples/>
2. Download the pair (`.onnx` **and** `.onnx.json`) from
   <https://huggingface.co/rhasspy/piper-voices>
3. Drop both in `~/.local/share/jarvis-desk/voices/`
4. It appears in Settings → Voice on next launch. No restart of anything
   else needed.

Quality tiers: `x_low` → `low` → `medium` → `high`. Medium is the sweet
spot (~63 MB, instant on this GPU). "High" voices are ~110 MB and only
marginally better.

### Use an ElevenLabs voice
1. Put the key in `~/.config/pytheas/elevenlabs.key`
2. Settings → Voice → any voice dropdown → **ElevenLabs / custom…**
3. Paste `eleven:<voice_id>` (voice ids come from your ElevenLabs
   library page). Cloned voices work the same way.

### Voice per model
Settings → Voice has a default plus per-family overrides:
**Claude models**, **Local models**, **API providers**. So Claude can
answer in one voice and a local model in another. Under the hood it's a
`voice_map` in settings keyed by engine prefix — `claude:opus` can be
given its own voice by hand-editing `~/.config/pytheas/settings.json`
if you want per-tier voices later.

## Why the briefing was Reddit-only

Diagnosed 2026-07-28 with `last30days.py --diagnose`:

- `"bird_authenticated": false` — the X/Twitter collector needs the
  **bird CLI** logged in. Not installed → **every X query returned
  nothing**.
- No web-search backend key (Brave / Exa / Serper) in
  `~/.config/last30days/.env` — only `SCRAPECREATORS_API_KEY`, which
  covers TikTok/Instagram/YouTube.
- Net effect: Reddit (+ HN) were the only sources actually returning
  data, so the brief looked Reddit-only even though 9 sources were
  "available".

### Fix applied in Pytheas
`briefing.py` now:
1. Passes official handles: `--x-handle AnthropicAI --x-related
   OpenAI,GoogleDeepMind,GoogleAI,xai,MistralAI,AIatMeta,ClaudeAI,…`
2. **Runs the synthesis pass with WebSearch/WebFetch enabled**, and the
   prompt explicitly tells it to check anthropic.com/news,
   openai.com/blog, deepmind.google, official X accounts, reputable
   outlets (Verge/Ars/TechCrunch/Axios), and GitHub trending + new
   Claude Code plugins/MCP servers before writing — so a Reddit-only
   research pull can no longer produce a Reddit-only briefing.
3. Marks anything unverified "(unconfirmed)" instead of promoting a
   Reddit rumor to fact.

### Optional, to get real X data back
Authenticate the bird CLI (`bird auth`) — then the `--x-handle` flags
start returning actual posts instead of relying on the web-search pass.
A Brave or Exa API key in `~/.config/last30days/.env` would likewise
restore the web collector.
