#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path.cwd(); PROJECT=ROOT/'PROJECT.md'; GRAPH=ROOT/'GRAPH.md'
name=' '.join(sys.argv[1:]).strip() or 'New Screen'
block=f'''\n\n## Screen contract: {name}\nPurpose:\nPrimary role:\nSecondary roles:\nViewport:\nEntry point:\nMain CTA:\nSecondary CTA:\nComponents from design-system/:\nExisting app patterns reused:\nStates:\nMobile behavior:\nGraph relationships:\nDo not change:\nOpen questions:\n'''
PROJECT.write_text(PROJECT.read_text(errors='ignore').rstrip()+block)
GRAPH.write_text(GRAPH.read_text(errors='ignore').rstrip()+f'\n\n- Screen: {name}\n')
print(f'Added screen contract and graph node: {name}')
