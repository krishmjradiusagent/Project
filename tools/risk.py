#!/usr/bin/env python3
import subprocess
HIGH=['design-system/components/ui/button','design-system/components/ui/dropdown-menu','tailwind.config','app/layout','package.json']
try:
    out=subprocess.check_output(['git','status','--short'],text=True)
    changed=[l[3:] for l in out.splitlines() if l.strip()]
except Exception:
    changed=[]
print('Change Risk\n'+'='*40)
if not changed: print('No git changes detected or git not initialized.')
for f in changed:
    if any(p in f.replace('\\','/') for p in HIGH): print(f'HIGH RISK: {f}')
