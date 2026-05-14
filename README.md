# AI Context OS + Graph + Localhost

Minimal AI project template for design-system-safe product design and prototype work.

## Start local preview

```bash
python tools/start.py
```

## Structure

```txt
PROJECT.md
RULES.md
GRAPH.md
screenshots/
design-system/
app/
tools/
graph/
.obsidian/
```

## First-time setup

1. Open this folder as an Obsidian vault.
2. Put your shadcn/design-system repo inside `design-system/`.
3. Put implementation/prototype code inside `app/`.
4. Add screenshots into `screenshots/`.
5. Run:

```bash
python tools/check.py
python tools/extract_components.py
python tools/index_screenshots.py
python tools/graph_build.py
```

## Open graph

Open:

```txt
graph/graph.html
```
