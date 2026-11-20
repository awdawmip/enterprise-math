#!/usr/bin/env python3
"""Independent validation of selected R5 14-label exact Bellman states.
Different endpoint construction and Python tuple-state recursion; no C++ solver import.
"""
import csv,functools,hashlib,json,random
from pathlib import Path
R=Path(__file__).parent
raw=(R/'EXACT_R5_ALL_101_BUDGETS.json').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
j=json.loads(raw)
tau=int(json.loads((R/'stages_18.json').read_text())['U'])-1
centers={k:tuple(map(int,j['counts_and_cohorts'][str(k)]['counts'])) for k in range(214,315)}
W=(0,16,32,48,1,64,17,80,18,24,34,82)
classes={int(r['id']):r for r in csv.DictReader((R/'classes_1906.tsv').open(),delimiter='\t')}
rawrows=list(csv.DictReader((R/'FULL_D14_F0_F3.csv').open()))
assert len(rawrows)==1906*4
lookup={(int(r['class']),int(r['f'])):int(r['exact_cost']) for r in rawrows}
assert all(r['status']=='EXACT' for r in rawrows)
rng=random.Random(20261120)
ids={0,5,8,29,368,847,1090,1265,1600,1905}
for action in (7,8,9):
 candidates=[i for i,r in classes.items() if int(r['actions'])==action]
 ids.update(rng.sample(candidates,min(4,len(candidates))))
def actions_for(cid):
 r=classes[cid];labels=W+(int(r['u']),int(r['v']))
 byfam={}
 for cost in range(214,315):
  c=centers[cost]
  x=[c[u] for u in labels]
  supports=set()
  for y in x:
   q=2*y-tau
   supports.add(sum((1<<k) for k,t in enumerate(x) if abs(2*t-q)<=tau))
  maximal=tuple(sorted(m for m in supports if not any(m!=t and m&t==m for t in supports)))
  if maximal==(16383,):continue
  if maximal not in byfam:byfam[maximal]=cost
 return tuple((cost,masks) for masks,cost in sorted(byfam.items(),key=lambda x:x[1]))
def solver(actions,f):
 @functools.lru_cache(None)
 def V(e):
  live=sum(1<<i for i,x in enumerate(e) if x<=f)
  if live.bit_count()<=1:return 0
  ans=10**12
  for cost,masks in actions:
   if any((m&live)==live for m in masks):continue
   worst=0
   for m in masks:
    nxt=tuple(min(f+1,z+(not (m>>i&1))) for i,z in enumerate(e))
    worst=max(worst,V(nxt))
    if cost+worst>=ans:break
   ans=min(ans,cost+worst)
  assert ans<10**12
  return ans
 return V((0,)*14),V.cache_info().currsize
verified=[]
for cid in sorted(ids):
 acts=actions_for(cid)
 assert len(acts)==int(classes[cid]['actions']),(cid,len(acts),classes[cid]['actions'])
 for f in (0,1,2) if cid not in (0,5,847,1090,1905) else (0,1,2,3):
  val,n=solver(acts,f)
  assert val==lookup[cid,f]==735+950*f,(cid,f,val,lookup[cid,f])
  verified.append((cid,f,val,n))
print('PASS independent doubled-endpoint tuple DP:',len(ids),'distinct classes,',len(verified),'exact crosschecks')
for x in verified:print(*x)
