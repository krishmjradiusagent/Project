#!/usr/bin/env python3
from pathlib import Path
import re
ROOT=Path.cwd(); PROJECT=ROOT/"PROJECT.md"; DS=ROOT/"design-system"
START="<!-- AUTO:COMPONENT_REGISTRY_START -->"; END="<!-- AUTO:COMPONENT_REGISTRY_END -->"
COMMON={"button","card","dialog","dropdown-menu","sheet","popover","select","avatar","badge","separator","tabs","table","input","textarea","command","calendar","tooltip","accordion","alert-dialog","switch","checkbox","radio-group","toast","sonner","drawer","label"}
def titleize(n): return "".join(p.capitalize() for p in re.split(r"[-_]",n))
def repl(t,b):
    if START not in t or END not in t: return t+f"\n\n## Component registry\n{START}\n{b}\n{END}\n"
    return t.split(START)[0]+START+"\n"+b+"\n"+END+t.split(END,1)[1]
found=[]
for p in DS.rglob("*"):
    if p.is_file() and p.suffix in {".tsx",".ts",".jsx",".js"} and (p.stem in COMMON or "components" in str(p)):
        found.append((titleize(p.stem),p.relative_to(ROOT)))
lines=[f"- {n}\n  - Source: `{r}`\n  - Used in: TBD\n  - Notes: Reuse before creating custom UI." for n,r in sorted(found)]
body="\n".join(lines) if lines else "No components indexed yet. Add shadcn/design-system files to design-system/ and run `python tools/extract_components.py`."
PROJECT.write_text(repl(PROJECT.read_text(errors="ignore"),body))
print(f"Indexed {len(lines)} component source(s)")
