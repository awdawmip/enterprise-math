#!/usr/bin/env python3
"""R706 exact reciprocal signed-X6 Link and rational future quotient check."""
from itertools import combinations,permutations,product
from collections import defaultdict
from fractions import Fraction as F
from math import comb
D=6; zero=(0,)*6
def move(z,i,s):
 t=list(z);t[i]+=s;return tuple(t)
def link(u,v): return (u,v) if u<v else (v,u)
shell=[defaultdict(set) for _ in range(3)]
end=defaultdict(set)
paths=[]
for ax in combinations(range(6),3):
 for signs in product((-1,1),repeat=3):
  ds=dict(zip(ax,signs))
  for order in permutations(ax):
   z=zero; used=[]
   for h,i in enumerate(order):
    zz=move(z,i,ds[i]);L=link(z,zz);shell[h][L].add(len(paths));used.append(L);z=zz
   paths.append((used,z));end[z].add(len(paths)-1)
assert len(paths)==960 and len(end)==160
assert [len(q) for q in shell]==[12,120,480]
assert all(set(shell[i]).isdisjoint(shell[j]) for i in range(3) for j in range(i+1,3))
assert all(len(x)==[80,8,2][h] for h,block in enumerate(shell) for x in block.values())
terminal=defaultdict(list)
for L,sources in shell[2].items():
 endpoint=paths[next(iter(sources))][1]
 assert all(paths[k][1]==endpoint for k in sources)
 terminal[endpoint].append(L)
assert len(terminal)==160 and all(len(v)==3 for v in terminal.values())
assert all(set().union(*(shell[2][L] for L in links))==end[e] for e,links in terminal.items())
def cls(m,r):return (m.bit_count(),tuple((m>>i)&1 for i in range(r)))
P={}
for m in range(8):
 P[m]={m^1:F(1,480),m^2:F(1,480),m^4:F(1,480),m:F(477,480)}
 assert sum(P[m].values())==1
Q={}
for r in range(4):
 fibers=defaultdict(list)
 for m in range(8):fibers[cls(m,r)].append(m)
 assert len(fibers)==2**r*(4-r)
 Q[r]=len(fibers)
 K={}
 for a,aa in fibers.items():
  K[a]={b:sum((P[aa[0]].get(y,0) for y in bb),F()) for b,bb in fibers.items()}
  assert sum(K[a].values())==1
  for m in aa:
   for b,bb in fibers.items():
    assert sum((P[m].get(y,0) for y in bb),F())==K[a][b]
 for m in range(8):
  full={m:F(1)};quot={cls(m,r):F(1)}
  for t in range(10):
   agg=defaultdict(F)
   for s,rate in full.items():agg[cls(s,r)]+=rate
   assert dict(agg)=={key:val for key,val in quot.items() if val}
   new=defaultdict(F)
   for s,rate in full.items():
    for y,p in P[s].items():new[y]+=rate*p
   full=new
   new=defaultdict(F)
   for s,rate in quot.items():
    for y,p in K[s].items():new[y]+=rate*p
   quot=new
assert Q=={0:4,1:6,2:8,3:8}
assert [(Q[r]**160-1).bit_length() for r in range(4)]==[320,414,480,480]
assert cls(1,0)==cls(2,0) and (1^1).bit_count()==0 and (2^1).bit_count()==2
assert cls(1,1)!=cls(2,1)
levels={0:F(1)}
for n in range(13):
 assert sum(levels.values())==1
 assert sum((F(x)*p for x,p in levels.items()),F())==F(240)*(1-F(239,240)**n)
 nxt=defaultdict(F)
 for x,p in levels.items():
  if x:nxt[x-1]+=p*F(x,480)
  if x<480:nxt[x+1]+=p*F(480-x,480)
 levels=nxt
assert F(1,480)+F(1,240)+F(477,480)==1
print("R706_RECIPROCAL_X6_LINK_BRC_DYNAMICS_EXACT_PASS",len(paths),len(end),[len(x) for x in shell],Q)
