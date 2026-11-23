#!/usr/bin/env python3
"""Exact T6 necessary-condition audit for three exact-v2(d)=5 atoms per side.

Independent mass cap <=2331, high layer-mass >=2011 on EACH side.
Assumes already-proved exact-v2(d)>=6 cancellation; checks lower v2 tiers
without assuming standalone rational equality for any valuation layer.
All integer modular arithmetic; finite exhaustive recursion.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations_with_replacement
from heapq import heappop, heappush

CAP=2331
LOWER_LAYER_MASS=2011
K=range(1,7)
M1=tuple(1<<k for k in K)
M2=tuple(1<<(2*k) for k in K)
M3=tuple(1<<(3*k) for k in K)
ZERO=(0,)*6

def signature(js, moduli):
    return tuple(sum(pow(j,-k,m) for j in js)%m for k,m in zip(K,moduli))

def add(a,b, moduli=M1):
    return tuple((x+y)%m for x,y,m in zip(a,b,moduli))

profiles=[p for p in combinations_with_replacement(range(1,72,2),3)
          if 32*sum(p)-3 <= CAP]
assert len(profiles)==1461
eligible=[p for p in profiles if 32*sum(p)-3 >= LOWER_LAYER_MASS]

# First 2-adic tier: D5,k == 0 modulo 2^k.
by=defaultdict(list)
for p in eligible:
    by[signature(p,M1)].append(p)

# Second tier: D5/2^k is the required V_B-V_A signature, not its negative.
# Each nonnegative v2=4 profile has a path with exact atom mass 16*j-1.
weights=[(16*j-1,signature((j,),M1)) for j in range(1,146,2)
         if 16*j-1<=CAP]
best={ZERO:0}
pq=[(0,ZERO)]
while pq:
    mass,s=heappop(pq)
    if mass!=best[s]:continue
    for w,g in weights:
        nc=mass+w
        if nc>CAP:continue
        ns=add(s,g)
        if nc<best.get(ns,CAP+1):
            best[ns]=nc
            heappush(pq,(nc,ns))
assert len(best)==2048

# All signed v2=3 inverse-moment signatures belong to this generated group.
G3={ZERO}
Q=deque([ZERO])
generators=[signature((j,),M1) for j in range(1,64,2)]
while Q:
    s=Q.popleft()
    for g in generators:
        t=add(s,g)
        if t not in G3:
            G3.add(t)
            Q.append(t)
assert len(G3)==2048

@lru_cache(None)
def v4_options(max_cost):
    opts={}
    ws=[(16*j-1,signature((j,),M2))
        for j in range(1,(max_cost+1)//16+1,2)]
    def recurse(i, mass, s):
        if i==len(ws):
            old=opts.get(s)
            if old is None or mass<old:
                opts[s]=mass
            return
        w,g=ws[i]
        while mass<=max_cost:
            recurse(i+1,mass,s)
            mass+=w
            s=add(s,g,M2)
    recurse(0,0,ZERO)
    return opts

cnt=Counter()
examples=[]
for grp in by.values():
    for i,a in enumerate(grp):
        for b in grp[i+1:]:
            cnt["first_tier"]+=1
            ra=CAP-(32*sum(a)-3)
            rb=CAP-(32*sum(b)-3)
            va,vb=signature(a,M2),signature(b,M2)
            shift=tuple(((x-y)//(1<<k))%(1<<k)
                        for x,y,k in zip(va,vb,K))
            if (shift[3]-shift[5])%8:
                continue
            cnt["cross_tier"]+=1
            if shift not in best:
                continue
            cnt["group"]+=1
            if not any(mass<=ra and best.get(add(s,shift),CAP+1)<=rb
                       for s,mass in best.items()):
                continue
            cnt["budget_feasible"]+=1
            aa=signature(a,M3)
            bb=signature(b,M3)
            fixed_delta=tuple((x-y)%m for x,y,m in zip(aa,bb,M3))
            for sa in v4_options(ra):
                for sb in v4_options(rb):
                    rem=tuple((d+(1<<k)*((x-y)%m2))%m3
                              for d,x,y,k,m2,m3 in zip(fixed_delta,sa,sb,K,M2,M3))
                    if any(z%(1<<(2*k)) for z,k in zip(rem,K)):
                        continue
                    cnt["third_tier_tested"]+=1
                    needed=tuple((-(z>>(2*k)))%(1<<k)
                                 for z,k in zip(rem,K))
                    if needed in G3:
                        cnt["third_tier_possible"]+=1
                        examples.append((a,b,needed))

expected={"first_tier":4469,"cross_tier":474,"group":197,
          "budget_feasible":104,"third_tier_tested":4377,
          "third_tier_possible":0}
assert dict(cnt)=={k:v for k,v in expected.items() if v!=0},(cnt,examples[:2])
assert len(eligible)==511
print("all profiles =",len(profiles),"; high mass =",len(eligible))
print("G4 and G3 cardinalities =",len(best),len(G3))
print("stage counts:",dict(cnt))
print("PASS: high-mass three-atom exact-v2=5 profiles are rigid")
