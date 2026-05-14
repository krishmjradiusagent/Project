---
type: ai-rules
status: active
source_of_truth: true
tags:
  - ai-rules
  - shadcn
  - design-system
  - context-os
  - graph
  - localhost
  - antigravity
  - codex
  - figma-make
---

# AI Project Rules

> [!important]
> Read this file first. Then read [[PROJECT]]. Then read [[GRAPH]] when working on product/UX relationships.

## Root contract
This repository can have any folder name.

Do not depend on the folder name.
Do not reference this project by folder name.
Treat the current repository root as the only project root.

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

Do not create extra root folders unless explicitly approved.

## Local preview contract
Use this script to start local preview:

```bash
python tools/start.py
```

Do not ask the AI how to run localhost.
Do not create a new dev-server script unless explicitly requested.
Do not move app code outside app/.

## Graph contract
The graph is a curated product/design graph.

It tracks:
- Features
- Screens
- Roles
- Flows
- States
- Use cases
- Edge cases
- Components
- Decisions
- Bugs
- Screenshots
- Important files

It must not track:
- Every function
- Every import
- Every div
- Every className
- Low-level implementation noise

Use `GRAPH.md` for human-readable project relationships.
Use `graph/graph.json` for machine-readable graph data.
Use `graph/graph.html` for interactive browser view.

## Design system source
The design system lives in:

`design-system/`

Before creating, modifying, or styling UI:
1. Inspect `design-system/`.
2. Search existing shadcn/ui components there.
3. Reuse those components.
4. Reuse existing tokens and Tailwind config.
5. Reuse existing product patterns from app/.
6. Only add a missing shadcn component after approval.

Never rebuild shadcn primitives manually if they already exist in `design-system/`.

## Read order
1. Read RULES.md.
2. Read PROJECT.md.
3. Read GRAPH.md for UX/product relationships.
4. Inspect design-system/.
5. Inspect app/.
6. Write a brief plan.
7. Implement only the approved scope.
8. Update PROJECT.md changelog.
9. Run graph update when relationships changed.

## Non-negotiable
- Do not start coding before a brief plan.
- Do not create custom components without approval.
- Do not replace existing layout hierarchy.
- Do not modify shared shadcn/ui primitives.
- Do not hardcode colors, spacing, radius, or typography.
- Use shadcn/ui, Radix, Tailwind tokens, Lucide icons only.
- Use Inter.
- Preserve WCAG AA.
- Preserve desktop 1440 first, responsive 390 mobile.

## Design system rules
- Import components from `design-system/` when available.
- If project aliases differ, map imports without moving files.
- Do not duplicate components into app/ unless required by project setup.
- If duplication is needed, document why in PROJECT.md.
- Do not mutate shared design-system components for one screen.
- If screen-specific behavior is needed, create a local wrapper or variant in app/.
- Do not invent visual language.
- Use quiet premium aesthetic: Airbnb, Zillow, Stripe, Robinhood subtlety.

## Tooling rules
- Scripts live only in tools/.
- Scripts protect context.
- Scripts do not design UI.
- Scripts do not rewrite app code.
- Scripts may update PROJECT.md and GRAPH.md only in clearly marked sections.

## UX responsibility
- AI owns UX structure.
- Designer owns visual direction.
- Always create basic wireframe flow first when feature is new.
- Cover roles: Agent, Team Lead, TC, Admin.
- Cover states: empty, loading, error, success, disabled, permission denied.
- Cover dropdown values inside PROJECT.md.
- Update GRAPH.md when relationships change.

## Approval required
Ask approval before:
- Adding custom component
- Changing typography scale
- Changing color system
- Changing layout hierarchy
- Editing shared shadcn primitives
- Installing new dependency
- Creating extra root folders
- Replacing an existing pattern
- Moving design-system files

## Required response before edits
Return this before implementation:

1. Plan
2. Files affected
3. Components reused from design-system/
4. Existing app patterns reused
5. Graph relationships affected
6. Risks
7. What will not be touched
