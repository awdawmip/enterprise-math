#!/usr/bin/env python3
"""EC49FEB exact finite 2/3-key rank+quota census (standard library).
Frozen native science input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
from collections import defaultdict, Counter
from functools import reduce
from itertools import combinations
import json
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
S=(0,0,4,1,16,32,8,2,0)
Q={4:2,5:4,6:2,7:4,8:4,9:2}
H=tuple(Q)
def rank9(m): return all(m&v for v in (18,20,33,40))
def support(h,group):
    c=Counter()
    for k in group: c.update(P[h].get(k,{}))
    return c
def quota(h,group):
    c=support(h,group)
    if sum(c.values())<Q[h]: return False
    return any(len(v)<=Q[h] and all(c[x]>0 for x in v)
               for v in ((16,32),(16,1,8),(32,2,4),(1,2,4,8)))
state={(0,0,0,0,0,0,0):1};P={}
for h in range(1,10):
    nxt=defaultdict(int)
    for s,n in state.items():
        for i in range(6):
            t=tuple(s[j]+(j==i) for j in range(6))+(T[s[6]][i],)
            nxt[t]+=n
    state=nxt
    if h not in Q:continue
    prof=defaultdict(lambda:defaultdict(int))
    for (a,c,d,e,f,g,q),n in state.items():
        if e==a+1 and S[q]:prof[(2*e+c+d+f,c+d+g,e)][S[q]]+=n
    P[h]={k:dict(v) for k,v in prof.items()}
K=sorted(set().union(*(P[h] for h in H)))
assert len(K)==155
M={h:{k:sum(P[h].get(k,{})) for k in K} for h in H}
def allrank(t):
    return all(rank9(reduce(int.__or__,(M[h][k] for k in t),0)) for h in H)
def allquota(t):return all(quota(h,t) for h in H)
pairs={p for p in combinations(K,2) if allrank(p)}
assert len(pairs)==124
assert not any(allquota(p) for p in pairs)
rank3=withpair=nopair=0;valid=[];valid_withpair=[]
for t in combinations(K,3):
    if not allrank(t): continue
    rank3+=1
    haspair=any(p in pairs for p in combinations(t,2))
    withpair+=haspair; nopair+=not haspair
    if allquota(t):
        valid.append(t)
        if haspair: valid_withpair.append(t)
assert (rank3,withpair,nopair,len(valid),len(valid_withpair))==(23728,16994,6734,108,44)
A=((3,2,1),(4,1,1))
B=((3,4,1),(4,3,1),(5,2,1),(5,2,2),(6,1,1),(6,1,2))
C=((4,6,1),(5,5,1),(6,4,1),(6,4,2),(7,3,1),
   (7,3,2),(8,2,1),(8,2,2),(8,2,3))
assert set(valid)=={tuple(sorted((a,b,c))) for a in A for b in B for c in C}
assert all(quota(4,(a,)) for a in A)
assert all(quota(h,(b,)) for b in B for h in (5,6))
assert all(quota(h,(c,)) for c in C for h in (7,8,9))
assert all(not P[h].get(a) for a in A for h in (5,6,7,8,9))
assert all(not P[h].get(b) for b in B for h in (7,8,9))
assert all(not any(x in (16,32) for x in P[4].get(b,{})) for b in B)
assert all(not P[4].get(c) for c in C)
assert all(not P[5].get(c) for c in C if c!=(6,4,1))
assert all(not any(x in (16,32) for x in P[6].get(c,{})) for c in C)
h9=[k for k in K if quota(9,(k,))]
assert len(h9)==16
assert all(not any(x in (16,32) for x in P[6].get(k,{})) for k in h9)
assert all(not P[6].get(a) for a in A)
assert set(P[5][(6,4,1)])=={1,2,4,8}
assert all({1,2,4,8}<=set(P[5][b]) for b in B)
print(json.dumps({'pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
  'later_keys':len(K),'rank_pairs':len(pairs),'rank_quota_pairs':0,
  'rank_triples':rank3,'rank_triples_with_rank_pair':withpair,
  'rank_triples_without_rank_pair':nopair,'rank_quota_triples':len(valid),
  'new_triples_with_rank_pair':len(valid_withpair),
  'rectangular_family_sizes':[len(A),len(B),len(C)],
  'literal_schedule_rigid_triples':96,'H5_optional_mixing_triples':12,
  'H9_quota_key_count':len(h9),'all_feasible_triples':valid},
  ensure_ascii=False,separators=(',',':')))
