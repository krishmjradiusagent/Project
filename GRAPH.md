---
type: project-graph
status: active
source_of_truth: true
tags:
  - graph
  - ux
  - product
  - design-spec
---

# Project Graph

> [!important]
> Curated product/design graph only. Do not turn this into a full code graph.

## Graph rules
Track:
- Feature
- Screen
- Role
- Flow
- State
- Use case
- Edge case
- Component
- Decision
- Bug
- Screenshot
- Important file

Do not track:
- Every import
- Every function
- Every className
- Every div
- Every utility call
- Low-level code noise

## Nodes
<!-- AUTO:GRAPH_NODES_START -->
- Project: Current Project
- Design System: design-system/
- App: app/
- Rules: RULES.md
- Context: PROJECT.md
<!-- AUTO:GRAPH_NODES_END -->

## Edges
<!-- AUTO:GRAPH_EDGES_START -->
- Current Project uses design-system/
- Current Project contains app/
- RULES.md governs Current Project
- PROJECT.md describes Current Project
<!-- AUTO:GRAPH_EDGES_END -->

## Product map
Use this area for manually curated relationships.

Example:
- Feature: Client Profile
  - contains Screen: Right Panel
  - uses Component: DropdownMenu
  - supports Role: Agent
  - has Edge Case: Multiple BRBC agreements
  - references Screenshot: screenshots/reference-fub-message-panel.png

## Open graph questions
- Which features are active?
- Which screens are approved?
- Which components are reused?
- Which roles need permissions?
- Which edge cases are unresolved?
