#!/usr/bin/env python3
"""Independent maximal-clique graph vs direct scalar-window support verification."""
from pathlib import Path
import hashlib, itertools, json, random
P=Path(__file__).resolve().parent
orig=(P/'EXACT_R5_ALL_101_BUDGETS.json').read_bytes()
assert hashlib.sha256(orig).hexdigest()=='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
C={k:list(map(int,v['counts'])) for k,v in ((int(k),v) for k,v in json.loads(orig)['counts_and_cohorts'].items())}
T=list(map(int,json.loads((P/'stages_18.json').read_text())['stage_taus']))
H={18,24,82,34,17,144,208};cand=[x for x in range(256) if x not in H]
allpairs=list(itertools.combinations(cand,2))
rng=random.Random(20261119)
sample=[(0,1),(0,49)]+rng.sample([p for p in allpairs if p not in ((0,1),(0,49))],70)
def maximal(masks):
 m=set(masks)
 return tuple(sorted(z for z in m if not any(z!=w and (z&w)==z for w in m)))
def window_family(c,tau):
 return maximal(sum(1<<i for i,z in enumerate(c) if a<=z<=a+tau) for a in c)
def clique_family(c,tau):
 n=len(c)
 adj=[sum(1<<j for j in range(n) if i!=j and abs(c[i]-c[j])<=tau) for i in range(n)]
 out=[]
 def bk(r,p,x):
  if not p and not x:
   out.append(r);return
  u=((p|x)&-(p|x)).bit_length()-1
  cand=p & ~adj[u]
  while cand:
   bit=cand&-cand;v=bit.bit_length()-1
   bk(r|bit,p&adj[v],x&adj[v]);p^=bit;x|=bit;cand^=bit
 bk(0,(1<<n)-1,0)
 return tuple(sorted(out))
checks=0
for x,y in sample:
 slots=(18,24,82,34,17,x,144,208,y)
 for k in range(214,315):
  c=[C[k][h] for h in slots]
  for tau in T:
   assert clique_family(c,tau)==window_family(c,tau),(x,y,k,tau)
   checks+=1
k=294;t=T[0];a=(0,1);b=(0,49)
for kk in range(214,315):
 for tt in T:
  for h in H:
   for slot in (0,1):
    assert (abs(C[kk][a[slot]]-C[kk][h])<=tt)==(abs(C[kk][b[slot]]-C[kk][h])<=tt)
ca=[C[k][h] for h in (18,24,82,34,17,a[0],144,208,a[1])]
cb=[C[k][h] for h in (18,24,82,34,17,b[0],144,208,b[1])]
assert window_family(ca,t)==(511,)
assert window_family(cb,t)==(255,479)
assert abs(C[k][a[0]]-C[k][a[1]])==0
assert abs(C[k][b[0]]-C[k][b[1]])==45392032647559604256815185920
print('PASS_PAIRWISE_CLIQUE_INDEPENDENT',len(sample),checks,'WITNESS',a,b,'k',k,'stage',0)
