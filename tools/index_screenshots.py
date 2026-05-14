#!/usr/bin/env python3
from pathlib import Path
ROOT=Path.cwd(); PROJECT=ROOT/"PROJECT.md"; S=ROOT/"screenshots"
START="<!-- AUTO:SCREENSHOT_INDEX_START -->"; END="<!-- AUTO:SCREENSHOT_INDEX_END -->"
EXTS={".png",".jpg",".jpeg",".webp",".gif",".svg"}
def repl(t,b):
    if START not in t or END not in t: return t+f"\n\n## Screenshot index\n{START}\n{b}\n{END}\n"
    return t.split(START)[0]+START+"\n"+b+"\n"+END+t.split(END,1)[1]
S.mkdir(exist_ok=True)
files=sorted([p for p in S.rglob("*") if p.suffix.lower() in EXTS])
body="\n".join([f"- `{p.relative_to(ROOT)}`" for p in files]) if files else "No screenshots indexed yet. Add screenshots to screenshots/ and run `python tools/index_screenshots.py`."
PROJECT.write_text(repl(PROJECT.read_text(errors="ignore"), body))
print(f"Indexed {len(files)} screenshot(s)")
