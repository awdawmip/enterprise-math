#!/usr/bin/env python3
"""Independent four-label subset DP for five selected C++ R7 B15 certificates."""
import json,collections,sys,time,os
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(Path(os.environ.get('EC49FKB_INPUT_DIR',ROOT.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))))
import EC49FGW_RADIUS5_SCREEN as g
assert g.PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
cert=[line.split('\t') for line in (ROOT/'EC49FKD_FOUR_RESULTS.tsv').read_text().splitlines()]
bykey=collections.defaultdict(list)
for label,word in g.all_words():bykey[(label,g.raw_key(word))].append(frozenset(g.pref(word)))
case_index={tuple(r[:2]):r for r in (line.split('\t') for line in (ROOT/'EC49FKD_FOUR_CASES.tsv').read_text().splitlines()) if tuple(r[:2]) in {(x[0],x[1]) for x in cert}}
picked=[]
for profile in ('A','B'):
 for size in ('10','54','65'):
  selected=next((r for r in cert if r[0]==profile and r[2]==size),None)
  if selected:picked.append(selected)
def pareto(seq):
 out=[]
 for n in sorted(set(seq),key=lambda x:(x.bit_count(),x)):
  if not any((m&n)==m for m in out):out.append(n)
 return out
report=[]
for prof,gid,context,labs,exact,nodes in picked:
 data=case_index[(prof,gid)]
 F={bytes.fromhex(x) for x in data[5].split(';')};keys=[tuple(int(x) for x in v.split(',')) for v in data[4].split(';')]
 assert len(F)==78 and len(keys)==7
 labels=[tuple(int(x) for x in v.split(',')) for v in labs.split(';')]
 choices=[]
 for lab in labels:
  c=[v-F for key in keys for v in bykey[(lab,key)] if len(v-F)<=15]
  assert c
  choices.append(c)
 universe=set().union(*(set(x) for sub in choices for x in sub)); index={p:i for i,p in enumerate(sorted(universe))}
 masks=[]
 for ch in choices:
  m=[]
  for s in ch:
   bits=0
   for p in s:bits|=1<<index[p]
   m.append(bits)
  masks.append(pareto(m))
 states=[0];sizes=[]
 for opts in masks:
  nxt={m|v for m in states for v in opts if (m|v).bit_count()<=15}
  states=pareto(nxt)
  sizes.append(len(states))
  if not states:break
 assert not states,(prof,gid)
 report.append({'profile':prof,'group_index':int(gid),'context_count':int(context),'labels':labels,'state_counts':sizes,'verdict':'no 15-prefix four-label completion'})
 print('EC49FKD_PY_PASS',prof,gid,context,sizes,flush=True)
assert len(report)==5
(ROOT/'EC49FKD_PY_CROSSCHECK.json').write_text(json.dumps({'frozen_pin':g.PIN,'checked':report},indent=2)+'\n')
print('EC49FKD_PY_5_DISTINCT_CLASSES_PASS',flush=True)
