---
title: Cross-Vault Organization Findings
date: 2026-08-27
type: organization-audit
status: approved and applied 2026-08-27
related: ["[[Home]]", "[[../Handoff/05 — Vault Cleanup Audit]]"]
---

# Cross-Vault Organization Findings

This is the evidence layer that drove the approved 2026-08-27 organization.
Counts shown below describe the original baseline; the sibling atlas notes now
describe the final organized state. Counts exclude `.git/` internals and do not
traverse symlinks.

> [!success] Applied decisions
> General courses moved to `learning/Courses/` after Chiron and Pytheas gained
> configurable course roots. Pytheas now uses
> `Architecture/Roadmaps/Operations/Generated/Incubator`. Finance's loose ideas
> moved to `finance/Incubator/`. `minecraft-event` remains under `life`, and
> `agonizing-sentience` was not restructured.

## What the atlas proves

| Vault | Folders | Files | Main structural fact |
|---|---:|---:|---|
| `agonizing-sentience` | 8 | 16 | Small and coherent; standing rule excludes it from restructuring |
| `finance` | 24 | 106 | Three substantial systems plus four loose root-level idea notes |
| `learning` | 159 | 1,061 | Largest vault; most depth is legitimate school units and contextual images |
| `life` | 61 | 271 | Two very different domains share one vault: private life and Minecraft project operations |
| `pytheas` | 34 | 349 | Project truth is mixed with generated output, migration records, courses, and operational logs |

The current system has **five** Obsidian vaults, not six or seven. Earlier
counts treated former standalone vaults such as `ai-improvement`, `card-flip`,
and `minecraft-event` as vaults even after they became subtrees.

## Findings by category

### 1. Duplication is not the main problem

No byte-identical, non-empty content files were found outside `.obsidian/` and
the generated atlas. Repeated names such as `Home.md`, `Unit 1 Notes.md`, and
ISO-dated daily files are contextual conventions, not duplicates.

The paired SAT `Practice 11/` and `Practice 11/question-only/` screenshots have
matching names but are not byte-identical. They must not be deduplicated merely
from their names.

### 2. Attachments need provenance, not a global attachments folder

The scan found 343 attachments in `learning` and 198 in `pytheas`. A simple
filename-reference check could not find references for 296 and 143
respectively. Most are concentrated in APUSH progress-check screenshots and SAT
Practice 11 captures. This is a review queue, not proof that the files are
orphans: some may be source material intentionally grouped by folder or used by
scripts.

Recommendation: keep attachments beside the subject or project they support.
Do not create one cross-vault `Attachments/` dump. Add a source README or index
to capture sets that are deliberately retained without inline Markdown embeds.

### 3. Empty directories are minor

The meaningful empty content directory is
`learning/ai-improvement/Conversations/Claude Export/Raw/`. Other empty paths
are plugin history/configuration directories. Empty school subject structures
were not detected, and no broad empty-folder cleanup is needed.

### 4. Pytheas has the largest hierarchy mismatch

The vault root currently mixes:

- canonical project maps and roadmaps;
- generated daily briefings;
- immutable prompt logs and conversation archives;
- migration handoffs and session wraps;
- surveys;
- SAT and basketball course content;
- a complete cross-vault atlas;
- historical Jarvis documents.

These are not equal classes of information. The root should expose current
project truth; generated output and operational records should sit beneath the
systems that produced them.

### 5. Course ownership is unresolved

`pytheas/Courses/` contains SAT learning material and Basketball Rules, while
`learning/` is the declared coursework/reference vault. This is the clearest
cross-vault placement inconsistency. However, Chiron's current Classroom routes
read the Pytheas Courses path, so moving courses requires a code/configuration
change first. A file move alone would break the product.

### 6. Finance needs an incubator rule, not more top-level domains

`finance/` has coherent `card-flip/`, `trading/`, and `Work/` systems. Its four
loose root notes—`anonymous-home-income.md`, `content-lanes.md`,
`product-idea-private-journal-app.md`, and the Home page—show the exact issue in
the stated requirements: small ideas appear beside substantial operating
systems. The three idea notes need either a named active project or one
incubator, not three new permanent folders.

### 7. Life contains a deliberate but awkward merger

`life/personal-private/` is a durable life domain. `life/minecraft-event/` is a
large engineering/creative project with generated upstream reference material.
Their coexistence is not internally inconsistent—the 2026-08-12 restructure
chose it—but it conflicts with the newer domain model that places substantial
projects under Projects and Engineering. Moving Minecraft again would be a
major decision with link, mirror-script, and git-history consequences.

## Proposed organization principles

1. Keep the five-vault boundary unless a concrete workflow proves it wrong.
2. Keep each vault root limited to durable domains and its `Home.md`.
3. Group generated material under the system that generates it.
4. Keep historical records, but mark their status and separate them from live
   instructions.
5. Use one incubator per vault for incomplete ideas; do not make a folder for
   every small thought.
6. Keep attachments contextual to their subject or project.
7. Change generators, routes, and links before moving their target folders.
8. Preserve `agonizing-sentience` exactly as an independent exception.

## Approved target shape

```text
pytheas/
├── Home.md
├── Architecture/
│   ├── Pytheas and Chiron Project Map.md
│   └── current technical specifications
├── Roadmaps/
│   ├── Chiron Roadmap — Mobile Owned Workspace.md
│   ├── Development Roadmap.md
│   └── Historical/
├── Research/
├── Operations/
│   ├── Handoff/
│   ├── Prompts/
│   ├── Conversations/
│   ├── Session Wraps/
│   ├── Surveys/
│   └── Vault Atlas/
├── Generated/
│   └── Briefings/
└── Incubator/
```

App-managed courses now live in `learning/Courses/`, including the registered
Pytheas benchmark fixture. Chiron reads
`CHIRON_COURSES_ROOT`, and Pytheas reads `PYTHEAS_COURSES_ROOT`; both default to
the Learning vault.

## Decisions made

1. General learning courses and the registered Pytheas benchmark fixture moved
   to `learning/Courses/` so the course registry has one canonical root.
2. `minecraft-event` remains under `life`; another subtree move has higher cost
   than the present conceptual mismatch.
3. Pytheas uses the `Architecture/Roadmaps/Operations/Generated/Incubator`
   grouping.
4. The three loose Finance idea notes moved to `finance/Incubator/`.

## Safe first structural actions after decisions

1. Fix live-document factual inconsistencies.
2. Update Chiron and the briefing generator to configurable content paths.
3. Move one collection at a time with link checks after every move.
4. Remove only confirmed empty or redundant artifacts.
5. Regenerate the complete atlas and compare the final state to this baseline.
