#!/usr/bin/env python3
from pathlib import Path
import json, re
ROOT=Path.cwd(); GRAPH_DIR=ROOT/"graph"; GRAPH_MD=ROOT/"GRAPH.md"; PROJECT=ROOT/"PROJECT.md"
GRAPH_DIR.mkdir(exist_ok=True)
nodes={}; edges=set()
def slug(s):
    return re.sub(r"[^a-z0-9]+","-",s.lower()).strip("-") or "node"
def node(label,t):
    i=f"{t}.{slug(label)}"; nodes[i]={"id":i,"label":label,"type":t}; return i
def edge(a,b,t):
    if a and b and a!=b: edges.add((a,b,t))
project=node("Current Project","project")
for label,t,rel in [("PROJECT.md","doc","describes"),("RULES.md","doc","governs"),("GRAPH.md","doc","maps"),("design-system/","design_system","uses"),("app/","app","contains"),("tools/start.py","tool","starts_localhost")]:
    n=node(label,t); edge(project,n,rel) if rel in ["uses","contains","starts_localhost"] else edge(n,project,rel)
if PROJECT.exists():
    text=PROJECT.read_text(errors="ignore")
    for role in re.findall(r"^- ([A-Za-z ]+)$", text, re.M):
        if role in ["Agent","Team Lead","TC","Admin"]: edge(project,node(role,"role"),"has_role")
if GRAPH_MD.exists():
    text=GRAPH_MD.read_text(errors="ignore")
    for m in re.findall(r"^- (Feature|Screen|Role|Component|Decision|Bug|Screenshot):\\s*(.+)$", text, re.M):
        edge(project,node(m[1],m[0].lower()),"relates_to")
data={"nodes":list(nodes.values()),"edges":[{"source":a,"target":b,"type":t} for a,b,t in edges]}
(ROOT/"graph"/"graph.json").write_text(json.dumps(data,indent=2))
html=f"""<!doctype html><html><head><meta charset='utf-8'><title>Project Graph</title><style>body{{font-family:Inter,system-ui;background:#0b0b0f;color:#fafafa;margin:0}}header{{padding:16px;border-bottom:1px solid #27272a}}main{{padding:16px}}.node{{display:inline-block;margin:6px;padding:8px 10px;border:1px solid #3f3f46;border-radius:999px;background:#18181b}}.edge{{color:#a1a1aa;margin:4px 0}}</style></head><body><header><b>Project Graph</b></header><main><h2>Nodes</h2>{''.join([f"<span class='node'>{n['type']}: {n['label']}</span>" for n in data['nodes']])}<h2>Edges</h2>{''.join([f"<div class='edge'>{e['source']} → {e['target']} · {e['type']}</div>" for e in data['edges']])}</main></body></html>"""
(ROOT/"graph"/"graph.html").write_text(html)
print(f"Graph built: {len(nodes)} nodes, {len(edges)} edges")
