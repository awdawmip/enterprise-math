#!/usr/bin/env python3
"""Necessary exact 2-adic v5 two-atom/profile sieve for T6 (integers only).

Uses prior complete cancellation v2(d)>=6. Does NOT assert global v2=5 elimination.
"""
from itertools import combinations_with_replacement
from collections import defaultdict
from heapq import heappop, heappush

CAP=2331
K=range(1,7)
MOD=tuple(1<<k for k in K)
J5=[j for j in range(1,72,2) if 32*j-1<=CAP]
PROFILES=[(a,b) for a,b in combinations_with_replacement(J5,2) if 32*(a+b)-2<=CAP]
assert len(PROFILES)==342

def signature(profile, k, modulus):
    return sum(pow(j,-k,modulus) for j in profile)%modulus

def low_signature(profile):
    return tuple(signature(profile,k,1<<k) for k in K)

def add(a,b):
    return tuple((u+v)%m for u,v,m in zip(a,b,MOD))

def residual_t(p,q):
    v=[]
    for k in K:
        d=(signature(p,k,1<<(2*k))-signature(q,k,1<<(2*k)))%(1<<(2*k))
        assert d%(1<<k)==0
        v.append(d//(1<<k))
    return tuple(v)

by=defaultdict(list)
for p in PROFILES:
    by[low_signature(p)].append(p)

# The minimum mass for each v4 signature is a shortest-path problem in a
# finite additive group: positive-cost edges are individual atom occurrences.
J4=[j for j in range(1,146,2) if 16*j-1<=CAP]
G4=[tuple(pow(j,-k,1<<k) for k in K) for j in J4]
W4=[16*j-1 for j in J4]
zero=(0,)*6
best={zero:0}
pq=[(0,zero)]
while pq:
    c,s=heappop(pq)
    if c!=best[s]:continue
    for g,w in zip(G4,W4):
        nc=c+w
        if nc>CAP:continue
        t=add(s,g)
        if nc<best.get(t,CAP+1):
            best[t]=nc
            heappush(pq,(nc,t))
assert len(best)==2048 and max(best.values())==813

counts=[0,0,0,0]
final=[]
for grp in by.values():
    for i,p in enumerate(grp):
        for q in grp[i+1:]:
            counts[0]+=1
            t=residual_t(p,q)
            if (t[3]-t[5])%8:continue
            counts[1]+=1
            if t not in best:continue
            counts[2]+=1
            ra=CAP-(32*sum(p)-2)
            rb=CAP-(32*sum(q)-2)
            if any(c<=ra and best.get(add(s,t),CAP+1)<=rb
                   for s,c in best.items()):
                counts[3]+=1
                final.append((p,q))
assert counts==[1038,82,33,26]
assert len(final)==26
print('PASS 342 complete two-v5-atom one-side profiles')
print('PASS first-tier pairs=1038; cross k4/k6=82; v4 group=33')
print('PASS budget-aware v4 necessary sieve leaves exactly 26 pairs')
print('NOT_CLOSED: 26 necessary-condition candidates, not full H-collisions')
