#!/usr/bin/env python3
"""Independent doubled-left-endpoint and tuple-counter f=0..3 oracle for 11 R5 14-label pair classes."""
from pathlib import Path
import csv, json, hashlib, functools
ROOT=Path(__file__).parent
src=(ROOT/'EXACT_R5_ALL_101_BUDGETS.json').read_bytes()
assert hashlib.sha256(src).hexdigest()=='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
d=json.loads(src);tau=int(json.loads((ROOT/'stages_18.json').read_text())['U'])-1
counts={k:tuple(map(int,d['counts_and_cohorts'][str(k)]['counts'])) for k in range(214,315)}
W=(0,16,32,48,1,64,17,80,18,24,34,82)
with (ROOT/'R5_FOURTEEN_PAIR_F0_ALL29646.csv').open() as f: pairs=list(csv.DictReader(f))
reps={}
for r in pairs: reps.setdefault(int(r['signature_class']),(int(r['u']),int(r['v'])))
assert len(pairs)==29646 and len(reps)==1906
BELL={}
for f in (1,2,3):
 with (ROOT/f'R5_FOURTEEN_PAIR_F{f}_CLASSES1906.csv').open() as fn:
  BELL[f]={int(r['class']):int(r[f'f{f}']) for r in csv.DictReader(fn)}
 assert len(BELL[f])==1906
selected=[0,1,7,49,113,270,502,709,1000,1500,1905]
for cls in selected:
 u,v=reps[cls]; h=W+(u,v); unique={}
 for k in counts:
  center=tuple(counts[k][i] for i in h)
  masks={sum(1<<j for j,b in enumerate(center) if abs(2*b-(2*a-tau))<=tau) for a in center}
  maximal=tuple(sorted(m for m in masks if not any(m!=n and (m&n)==m for n in masks)))
  if maximal!=(16383,):unique.setdefault(maximal,k)
 acts=tuple((c,m) for m,c in unique.items())
 for f in range(4):
  @functools.lru_cache(None)
  def value(state):
   live=sum(1<<i for i,e in enumerate(state) if e<=f)
   if live.bit_count()<=1:return 0
   options=[]
   for cost,ms in acts:
    if any((m&live)==live for m in ms):continue
    worst=max(value(tuple(min(f+1,e+(not (m>>i&1))) for i,e in enumerate(state))) for m in ms)
    options.append(cost+worst)
   assert options
   return min(options)
  expected=735 if f==0 else BELL[f][cls]
  actual=value((0,)*14)
  assert actual==expected,(cls,f,actual,expected)
 print('CROSSCHECK',cls,u,v,'f0..3 match')
print('PASS_R5_FOURTEEN_INDEPENDENT_F0_F3',len(selected),'classes')
