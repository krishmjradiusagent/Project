---
type: project-context
status: active
source_of_truth: true
tags:
  - radius
  - ux
  - prototype
  - shadcn
  - design-system
  - context-os
  - graph
  - localhost
  - figma-make
  - antigravity
  - codex
---

# Project Context

> [!important]
> This is the source of truth. Folder name does not matter.

## Linked rules
See [[RULES]].

## Linked graph
See [[GRAPH]].

## Project identity
This repository is a generic AI-assisted product design and prototype workspace.

The folder name is not important.
Agents must treat the current repository root as the source of truth.

## Product
Radius real estate platform.

## Folder contract
Allowed root structure:
- PROJECT.md
- RULES.md
- GRAPH.md
- screenshots/
- app/
- design-system/
- tools/
- graph/
- .obsidian/

No other root knowledge folders.

## Local preview
Run:

```bash
python tools/start.py
```

Do not ask AI how to start localhost.
Use this script.

The script:
- enters app/
- installs dependencies if node_modules is missing
- detects package manager
- starts dev server
- opens browser
- falls back to static Python server if no package.json exists

## Design system location
The design system lives in:

`design-system/`

Agents must inspect `design-system/` before editing UI.

## Graph system
The graph system is curated.

Use:
- `GRAPH.md` for human-readable product/design relationships
- `graph/graph.json` for machine-readable nodes/edges
- `graph/graph.html` for interactive browser view

Run:

```bash
python tools/graph_build.py
```

Do not create a full code graph.
Only track meaningful product/design concepts.

## Tooling
Use tools for context protection:

```bash
python tools/start.py
python tools/check.py
python tools/index_screenshots.py
python tools/extract_components.py
python tools/graph_build.py
python tools/prompt.py figma
python tools/prompt.py codex
python tools/prompt.py antigravity
python tools/prompt.py qa
python tools/risk.py
python tools/visual_qa.py
python tools/screen.py "Screen Name"
python tools/update_project.py
```

## Design system import policy
Preferred:
- Reuse existing components directly from `design-system/`.
- Map aliases if needed.
- Keep app-specific composition inside `app/`.

Forbidden:
- Rebuilding existing components.
- Duplicating shadcn components without reason.
- Editing shared primitives for one screen.
- Creating custom components without approval.

## Designer strength
- Strong UI taste.
- Strong micro-interactions.
- Needs AI support for UX structure, flows, edge cases, states, and role logic.

## Core problem
AI tools keep drifting:
- Figma Make modifies UI heavily.
- Codex/Antigravity assume design system.
- shadcn components get rewritten.
- Popups do not copy cleanly back to Figma.
- TSX prototypes shrink or misalign.
- Context is scattered across many files.
- Deployment breaks when app root is nested incorrectly.
- AI ignores existing design-system files unless explicitly told.
- Full code graphs create noise and hide product concepts.
- Repeated localhost setup asks waste tokens.

## Product decisions
- Use shadcn/ui as default component system.
- Use design-system/ before app-specific UI.
- Use local wrappers/variants instead of mutating shared primitives.
- Figma Make is for wireframe/prototype output, not final design-system truth.
- Keep root flat and deployment-friendly.
- Use curated graph, not full code graph.
- Use tools/start.py for local preview.

## Agent modes
### UX_ARCHITECT
Use for flows, states, roles, permissions, edge cases, and screen contracts. Do not code.

### FIGMA_PROMPT
Use for Figma Make prompts. Must create visible popup states and avoid modifying existing screens unless requested.

### CODE_PATCH
Use for scoped implementation in app/. Must reuse design-system/.

### VISUAL_QA
Use for bug finding only. Do not redesign.

### GRAPH_UPDATE
Use for updating GRAPH.md and graph outputs after product/design relationships change.

## AI failure patterns
- Do not shrink frames.
- Do not center full app shell.
- Do not replace shadcn DropdownMenu.
- Do not create native select.
- Do not edit shared Button.
- Do not hide popup states.
- Do not use hover-only critical UI.
- Do not add random gradients.
- Do not create new design language.
- Do not rewrite unrelated screens.
- Do not create full noisy code graphs.
- Do not ask how to run localhost; use tools/start.py.
- Do not claim visual verification without checking.

## Product roles
- Agent
- Team Lead
- TC
- Admin

## UX coverage required
Every feature must define:
- Primary user
- Secondary users
- Entry point
- Main flow
- Empty state
- Error state
- Permission state
- Mobile behavior
- Dropdown values
- Confirmation dialogs
- Success feedback
- Audit/log behavior if relevant

## Current feature
Name:
TBD

Goal:
TBD

Primary user:
TBD

Secondary users:
TBD

Entry point:
TBD

Screenshots:
- screenshots/current.png
- screenshots/reference.png
- screenshots/bug.png

## Screen contract
Name:
Viewport:
Role:
Entry:
Main CTA:
Secondary CTA:
Components:
States:
Do not change:
Mobile behavior:

## Flow
TBD

## Role matrix
| Role | Can view | Can edit | Notes |
|---|---|---|---|
| Agent | TBD | TBD | TBD |
| Team Lead | TBD | TBD | TBD |
| TC | TBD | TBD | TBD |
| Admin | TBD | TBD | TBD |

## Component registry
<!-- AUTO:COMPONENT_REGISTRY_START -->
No components indexed yet. Run `python tools/extract_components.py`.
<!-- AUTO:COMPONENT_REGISTRY_END -->

## Screenshot index
<!-- AUTO:SCREENSHOT_INDEX_START -->
No screenshots indexed yet. Add screenshots to screenshots/ and run `python tools/index_screenshots.py`.
<!-- AUTO:SCREENSHOT_INDEX_END -->

## Dropdown registry
Format:
- Section:
  - Dropdown name:
    - Option 1
    - Option 2
    - Option 3

## State coverage
- Empty:
- Loading:
- Error:
- Success:
- Disabled:
- Permission denied:
- Mobile:

## Protected files
- design-system/components/ui/button.tsx
- design-system/components/ui/dropdown-menu.tsx
- design-system/components/ui/dialog.tsx
- design-system/components/ui/sheet.tsx
- design-system/components/ui/popover.tsx
- design-system/components/ui/select.tsx
- design-system/components/ui/card.tsx
- design-system/components/ui/avatar.tsx

## Known bugs
- Popovers can mount offscreen.
- Figma Make may shrink frames.
- Generated TSX may not match Figma copy behavior.
- AI may modify unrelated components.
- AI may replace shadcn patterns with custom UI.
- AI may ignore design-system unless RULES.md and PROJECT.md are read first.
- AI may over-index code and confuse product concepts.

## Changelog
Format:
- Date:
  - Agent:
  - Change:
  - Files touched:
  - Design-system files touched:
  - Graph updated:
  - Visual verification:
  - Remaining issues:
