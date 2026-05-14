#!/usr/bin/env python3
import sys
MODES={
"figma":"MODE: FIGMA_PROMPT\n\nRead RULES.md.\nRead PROJECT.md.\nRead GRAPH.md.\nUse design-system/.\nDo not code.\nCreate one copy-ready Figma Make prompt.\n",
"codex":"MODE: CODE_PATCH\n\nRead RULES.md, PROJECT.md, GRAPH.md.\nInspect design-system/ and app/.\nImplement only requested scope.\nUse tools/start.py for localhost.\n",
"antigravity":"MODE: CODE_PATCH / VISUAL_FIX\n\nRead RULES.md, PROJECT.md, GRAPH.md.\nPatch existing UI only.\nReuse design-system/.\nUse tools/start.py for localhost.\n",
"qa":"MODE: VISUAL_QA\n\nRead RULES.md, PROJECT.md, GRAPH.md.\nDo not redesign.\nFind layout, component, graph, and visual bugs.\n",
"graph":"MODE: GRAPH_UPDATE\n\nRead RULES.md, PROJECT.md, GRAPH.md.\nUpdate curated relationships only.\nRun python tools/graph_build.py.\n"
}
m=sys.argv[1].lower() if len(sys.argv)>1 else "figma"
if m not in MODES: raise SystemExit(f"Unknown mode. Use: {', '.join(MODES)}")
print(MODES[m])
