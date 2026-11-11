#!/usr/bin/env python3
"""EC49FJD exact signed native X6 BRC prefix-union/key-cover solver."""
from EC49FGW_RADIUS5_SCREEN import *
from collections import defaultdict,Counter
from itertools import combinations
from pathlib import Path
import time,json
B=11
cat=list(all_words());assert len(cat)==178850
bykey=defaultdict(lambda:defaultdict(list));cover=defaultdict(set)
for label,w in cat:
 k=raw_key(w);bykey[k][label].append(w);cover[k].add(label)
assert len(cover)==94
def key_cover(labels,fixed,slots,forbid=None):
 missing=[lab for lab in labels if not any(lab in cover[k] for k in fixed)]
 if not missing:return True
 goal=(1<<len(missing))-1
 choices={sum(1<<i for i,lab in enumerate(missing) if lab in labs) for k,labs in cover.items() if k not in fixed and k!=forbid}
 choices.discard(0);reach={0}
 for _ in range(slots):
  reach|={m|c for m in tuple(reach) for c in choices}
  if goal in reach:return True
 return False
def antichain(masks):
 out=[]
 for m in sorted(set(masks),key=lambda x:(x.bit_count(),x)):
  if not any((s&m)==s for s in out):out.append(m)
 return out
def solve_high(F,selected,allowed_keys):
 opts={}
 for lab in selected:
  choices=set()
  for k in allowed_keys:
   for w in bykey[k].get(lab,[]):
    pp=pref(w);i=0
    while i<len(pp) and pp[i] in F:i+=1
    new=tuple(pp[i:])
    if len(new)<=B:choices.add(new)
  opts[lab]=choices
 if not all(opts.values()):return {'status':'EXCLUDED_MISSING_LABEL','options':{str(k):len(v) for k,v in opts.items()}}
 universe={pp for sets in opts.values() for new in sets for pp in new}
 ix={p:i for i,p in enumerate(sorted(universe))}
 masks={lab:antichain(sum(1<<ix[p] for p in new) for new in opts[lab]) for lab in selected}
 order=sorted(selected,key=lambda x:(len(masks[x]),x));states=[0];rounds=[]
 for lab in order:
  nxt=[]
  for s in states:
   for m in masks[lab]:
    v=s|m
    if v.bit_count()<=B:nxt.append(v)
  states=antichain(nxt)
  rounds.append({'label':list(lab),'states':len(states)})
  if not states:return {'status':'EXCLUDED_HIGH','rounds':rounds,'option_counts':{str(k):len(v) for k,v in masks.items()},'lower_bound_at_least':B+1}
 return {'status':'SURVIVES_HIGH','rounds':rounds,'option_counts':{str(k):len(v) for k,v in masks.items()},'min_cost_within_budget':min(s.bit_count() for s in states)}
