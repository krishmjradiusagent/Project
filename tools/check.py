#!/usr/bin/env python3
from pathlib import Path
ROOT=Path.cwd()
REQUIRED=["PROJECT.md","RULES.md","GRAPH.md","screenshots","app","design-system","tools","graph"]
ALLOWED=set(REQUIRED+[".obsidian",".git",".gitignore","README.md","package.json","pnpm-lock.yaml","package-lock.json","yarn.lock","node_modules",".DS_Store"])
errors=[]; warnings=[]
for n in REQUIRED:
    if not (ROOT/n).exists(): errors.append(f"Missing required item: {n}")
for item in ROOT.iterdir():
    if item.name not in ALLOWED: warnings.append(f"Unknown root item: {item.name}")
print("Context Check\n"+"="*40)
print("\nNo blocking errors." if not errors else "\nERRORS")
for e in errors: print(f"- {e}")
print("\nNo warnings." if not warnings else "\nWARNINGS")
for w in warnings: print(f"- {w}")
if errors: raise SystemExit(1)
