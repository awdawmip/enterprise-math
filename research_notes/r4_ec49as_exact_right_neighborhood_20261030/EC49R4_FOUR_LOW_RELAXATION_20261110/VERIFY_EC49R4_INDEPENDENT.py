#!/usr/bin/env python3
"""Independent Cartesian-product candidate enumeration and literal signed-X6 audit."""
import json
from collections import Counter
from itertools import product
from pathlib import Path
from ec49fgd_mixed_seed_dp import OPS,T,SIG,expand,pref,key,signature
report=Path(__file__).with_name('EXACT_REPORT_EC49R4.json')
d=json.loads(report.read_text(encoding='utf-8'))
chosen={'2:16':'fe','2:32':'ge','3:16':'feg','3:32':'gef'}|d['witness']
expected={2:(16,32),3:(16,32),4:(1,2,4,8),6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8)}
for h,labels in expected.items():
 assert {int(k.split(':')[1]) for k in chosen if k.startswith(f'{h}:')}==set(labels)
for hs,w in chosen.items():
 h,s=map(int,hs.split(':'))
 assert len(w)==h and signature(w)==s
 steps=expand(w)
 assert tuple(steps.count(j)-steps.count(-j) for j in range(1,7))==(2,0,0,0,0,0)
 if h>=4:assert min(key(w))>0
assert len(set().union(*(pref(w) for w in chosen.values())))==64
counts={}
for h in (4,6,7,8):
 n=0
 for tup in product(OPS,repeat=h):
  c=Counter(tup)
  if c['e']!=c['a']+1 or c['e']<1:continue
  if min((h+1-c['g'],h+1-2*c['e']-c['f'],c['e']))<=0:continue
  q=0
  for op in tup:
   q=T[q][OPS.index(op)]
   if q==8:break
  if SIG[q] in (1,2,4,8):n+=1
 counts[h]=n
assert counts=={4:176,6:4932,7:25060,8:125680},counts
print(json.dumps({'independent_audit':'PASS','full_words':len(chosen),'four_window_words':16,'signed_native_prefix_cost':64,'pool_counts':counts},sort_keys=True))
