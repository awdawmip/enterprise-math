#!/usr/bin/env python3
"""Independent doubled-endpoint verification for selected R5 pair augmentations.
Usage after running the C++ census:
 python3 VERIFY_PAIR_ENDPOINT.py
Requires the frozen EXACT_R5_ALL_101_BUDGETS.json, stages_18.json,
pair_signature_members.tsv, and pair_budget_results.tsv in this directory.
"""
import json, random, functools, hashlib
from pathlib import Path
root=Path(__file__).parent
raw=(root/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
assert hashlib.sha256(raw).hexdigest()=="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
data=json.loads(raw)
tau=int(json.loads((root/"stages_18.json").read_text())["U"])-1
centers=[tuple(map(int,data["counts_and_cohorts"][str(k)]["counts"])) for k in range(214,315)]
H=(0,16,32,48,1,64)
byid={}
for line in (root/"pair_budget_results.tsv").read_text().splitlines():
 if line.startswith("#"):continue
 row=list(map(int,line.split()))
 byid[row[0]]=row
pairs={}
for line in (root/"pair_signature_members.tsv").read_text().splitlines():
 if line.startswith("#"):continue
 u,v,ident=map(int,line.split())
 pairs[(u,v)]=byid[ident]
assert len(pairs)==31125

def families(labels):
 classes={}
 for k,cs in enumerate(centers,214):
  v=[cs[i] for i in labels]
  # 2*y is a doubled left endpoint; this is independent of center windows
  endpoints=[2*t-tau for t in v]
  masks={sum(1<<j for j,z in enumerate(v) if abs(2*z-x)<=tau)
         for x in endpoints}
  fam=tuple(sorted(s for s in masks
       if all(s==t or (s&t)!=s for t in masks)))
  classes.setdefault(fam,k)
 return tuple(sorted((k,fam) for fam,k in classes.items() if fam!=(255,)))

def solve(acts,f):
 @functools.lru_cache(None)
 def visit(e):
  live=sum(1<<i for i,x in enumerate(e) if x<=f)
  if live.bit_count()<=1:return 0
  opts=[]
  for k,ss in acts:
   if any((s&live)==live for s in ss):continue
   nxt=[]
   for s in ss:
    ee=tuple(min(f+1,x+(1 if not(s&(1<<i)) else 0))
             for i,x in enumerate(e))
    nxt.append(visit(ee))
   opts.append(k+max(nxt))
  assert opts
  return min(opts)
 return visit((0,)*8)

rare=[pair for pair,v in pairs.items() if v[5]>1678]
assert len(rare)==36
rng=random.Random(20261119)
chosen=set(rare+rng.sample(list(pairs),400))
for pair in chosen:
 acts=families(H+pair)
 assert solve(acts,0)==pairs[pair][4],(pair,"f0")
for pair in rare:
 acts=families(H+pair)
 assert solve(acts,1)==pairs[pair][5],(pair,"f1")
 assert solve(acts,2)==pairs[pair][6],(pair,"f2")
print("PASS_ENDPOINT_PAIR_CENSUS",len(chosen),"f0; rare f1/f2",len(rare))
