#!/usr/bin/env python3
from pathlib import Path
import re
ROOT=Path.cwd(); APP=ROOT/'app'
patterns={'native select found':r'<select\\b','hardcoded color':r'#[0-9a-fA-F]{3,8}|rgb\\(','full-width button':r'<Button[^>]*className=.*\\bw-full\\b'}
print('Visual QA Heuristic Scan\n'+'='*40)
for p in APP.rglob('*'):
    if p.is_file() and p.suffix in {'.tsx','.ts','.jsx','.js','.html','.css'}:
        t=p.read_text(errors='ignore')
        for label,pat in patterns.items():
            if re.search(pat,t,re.S): print(f'- {label}: `{p.relative_to(ROOT)}`')
print('Note: heuristic only.')
