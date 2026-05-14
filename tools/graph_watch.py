#!/usr/bin/env python3
from pathlib import Path
import time, subprocess, sys
ROOT=Path.cwd(); WATCH=[ROOT/'PROJECT.md',ROOT/'GRAPH.md',ROOT/'screenshots',ROOT/'app',ROOT/'design-system']
def snap():
    d={}
    for p in WATCH:
        if p.exists():
            for f in ([p] if p.is_file() else p.rglob('*')):
                if f.is_file(): d[str(f)]=f.stat().st_mtime
    return d
last=snap(); print('Watching graph inputs. Ctrl+C to stop.')
while True:
    time.sleep(2); now=snap()
    if now!=last:
        subprocess.call([sys.executable,'tools/graph_build.py'],cwd=ROOT); last=now
