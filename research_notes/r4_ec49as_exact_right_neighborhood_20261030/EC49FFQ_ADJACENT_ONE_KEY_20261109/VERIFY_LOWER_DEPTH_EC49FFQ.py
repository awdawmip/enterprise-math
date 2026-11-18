#!/usr/bin/env python3
"""Finite independent audit of universal L-2/L-3 signed native prefix-separation lemmas.
Run next to VERIFY_EC49FFQ.py. Finite tests support the model transcription; universal proof is in README.
"""
from collections import defaultdict
import json
import VERIFY_EC49FFQ as m

rows=[]
for h in (5,6,7,8):
 inventory=sorted(set(m.keys(h))&set(m.keys(h+1)))
 total=0
 for key in inventory:
  L=2*(sum(key)-1)
  labels_l2=defaultdict(set)
  labels_l3=defaultdict(set)
  for horizon in (h,h+1):
   for word,sig in m.original_words(horizon,key):
    path=m.native(word)
    assert len(path)==L
    if sig==4: assert path[0]==1
    if sig==1: assert path[0]==2
    labels_l2[path[:L-2]].add((horizon,sig))
    labels_l3[(horizon,path[:L-3])].add(sig)
    total+=1
  assert all(len(s)==1 for s in labels_l2.values()),(h,key,'L-2')
  assert all(len(s)==1 for s in labels_l3.values()),(h,key,'L-3')
 rows.append({'h':h,'keys':len(inventory),'eligible_words':total,'status':'PASS'})
assert [r['eligible_words'] for r in rows]==[2910,17532,99988,544840]
print(json.dumps({'schema':'EC49FFQ_LOWER_DEPTH_FINITE_AUDIT_V1',
 'scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
 'status':'EXACT_FINITE_PASS','rows':rows},indent=2))
