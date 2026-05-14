#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
import argparse
ROOT=Path.cwd(); PROJECT=ROOT/'PROJECT.md'
p=argparse.ArgumentParser(); p.add_argument('--agent',default='AI Agent'); p.add_argument('--change',default='TBD'); p.add_argument('--files',default='TBD'); p.add_argument('--ds-files',default='None'); p.add_argument('--graph',default='Not updated'); p.add_argument('--visual',default='Not verified'); p.add_argument('--issues',default='TBD')
a=p.parse_args(); date=datetime.now().strftime('%Y-%m-%d')
entry=f'''\n- {date}:\n  - Agent: {a.agent}\n  - Change: {a.change}\n  - Files touched: {a.files}\n  - Design-system files touched: {a.ds_files}\n  - Graph updated: {a.graph}\n  - Visual verification: {a.visual}\n  - Remaining issues: {a.issues}\n'''
PROJECT.write_text(PROJECT.read_text(errors='ignore').rstrip()+entry)
print('Changelog entry appended')
