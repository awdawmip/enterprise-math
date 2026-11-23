#!/usr/bin/env python3
"""Exact T6 v2=5 three-atom rigidity audit for layer mass >=1949 on BOTH sides.

Uses published universal cancellation of v2(d)>=6 and of 81|d differences.
The full six original rational moments are the source of all necessary
mixed 2-adic and 3-adic congruences. Integer-only exhaustive enumeration.
"""
from collections import Counter,defaultdict,deque
from functools import lru_cache
from itertools import combinations_with_replacement
from heapq import heappop,heappush

CAP=2331
LOWER_LAYER_MASS=1949
K=range(1,7)
M1=tuple(1<<k for k in K)
M2=tuple(1<<(2*k) for k in K)
M3=tuple(1<<(3*k) for k in K)
ZERO=(0,)*6

def signature(js,moduli):
    return tuple(sum(pow(j,-k,m) for j in js)%m for k,m in zip(K,moduli))

def add(a,b,moduli=M1):
    return tuple((x+y)%m for x,y,m in zip(a,b,moduli))

profiles=[p for p in combinations_with_replacement(range(1,72,2),3)
          if 32*sum(p)-3<=CAP]
assert len(profiles)==1461
eligible=[p for p in profiles if 32*sum(p)-3>=LOWER_LAYER_MASS]
assert len(eligible)==596

by=defaultdict(list)
for p in eligible:
    by[signature(p,M1)].append(p)

# Complete v2=4 group with exact minimum positive-atom mass per signature.
weights=[(16*j-1,signature((j,),M1)) for j in range(1,146,2)
         if 16*j-1<=CAP]
best={ZERO:0}
pq=[(0,ZERO)]
while pq:
    c,s=heappop(pq)
    if c!=best[s]:continue
    for w,g in weights:
        nc=c+w
        if nc>CAP:continue
        ns=add(s,g)
        if nc<best.get(ns,CAP+1):
            best[ns]=nc
            heappush(pq,(nc,ns))
assert len(best)==2048

# Complete signed v2=3 group: all possible odd unit classes modulo 64.
G3={ZERO}
Q=deque([ZERO])
Gens=[signature((j,),M1) for j in range(1,64,2)]
while Q:
    s=Q.popleft()
    for g in Gens:
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
    def rec(i,c,s):
        if i==len(ws):
            if c<opts.get(s,10**9):opts[s]=c
            return
        w,g=ws[i]
        while c<=max_cost:
            rec(i+1,c,s)
            c+=w
            s=add(s,g,M2)
    rec(0,0,ZERO)
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
            # Full S_k implies V_B-V_A=D5/2^k mod2^k.
            t=tuple(((x-y)//(1<<k))%(1<<k) for x,y,k in zip(va,vb,K))
            if (t[3]-t[5])%8:
                continue
            cnt["cross_tier"]+=1
            if t not in best:
                continue
            cnt["group"]+=1
            if not any(c<=ra and best.get(add(s,t),CAP+1)<=rb
                       for s,c in best.items()):
                continue
            cnt["budget_feasible"]+=1

            fixed_delta=tuple((x-y)%m for x,y,m in
                zip(signature(a,M3),signature(b,M3),M3))
            v4a=v4_options(ra)
            v4b=v4_options(rb)
            buckets=defaultdict(list)
            for sb in v4b:
                buckets[tuple(x%m for x,m in zip(sb,M1))].append(sb)
            d2=tuple((x-y)%m for x,y,m in zip(va,vb,M2))
            correction=tuple((x//(1<<k))%(1<<k) for x,k in zip(d2,K))
            for sa in v4a:
                req=tuple((x+tk)%m for x,tk,m in zip(sa,correction,M1))
                for sb in buckets.get(req,()):
                    E=tuple((d+(1<<k)*((x-y)%m2))%m3
                            for d,x,y,k,m2,m3 in
                            zip(fixed_delta,sa,sb,K,M2,M3))
                    assert all(z%(1<<(2*k))==0 for z,k in zip(E,K))
                    cnt["third_tier_tested"]+=1
                    needed=tuple((-(z>>(2*k)))%(1<<k)
                                 for z,k in zip(E,K))
                    if needed in G3:
                        cnt["third_tier_possible"]+=1
                        examples.append((a,b,needed))

expected={"first_tier":5095,"cross_tier":539,"group":220,
          "budget_feasible":127,"third_tier_tested":14251,
          "third_tier_possible":7}
assert dict(cnt)==expected,(cnt,expected)
possible_pairs=sorted({(a,b) for a,b,_ in examples})
assert possible_pairs==[((3,3,55),(7,27,27))],possible_pairs

# Use earlier 81|d cancellation. All fixed p3-cube atoms in this pair
# occur on B as 2 copies of d=32*27=27*32; neither fixed A atom is v3=3.
# Both side residual budgets equal 382 after their 3 v2=5 atoms.
P3=tuple(3**k for k in K)
ws3=[(27*u-1,signature((u,),P3)) for u in range(1,15) if u%3]
def p3_options(B):
    options={}
    def rec(i,c,s):
        if i==len(ws3):
            if c<options.get(s,10**9):options[s]=c
            return
        w,g=ws3[i]
        while c<=B:
            rec(i+1,c,s)
            c+=w
            s=add(s,g,P3)
    rec(0,0,ZERO)
    return options
assert sum(possible_pairs[0][0])==sum(possible_pairs[0][1])==61
O=p3_options(382)
assert len(O)==246
shift=signature((32,32),P3)
hits=[s for s in O if tuple((x-y)%m for x,y,m in
                           zip(s,shift,P3)) in O]
assert not hits
print("profile counts: full",len(profiles),"high-mass",len(eligible))
print("2-adic stage counts",dict(cnt))
print("last 2-adic potential",possible_pairs)
print("3-adic cube signature options",len(O),"shift",shift,"intersections",len(hits))
print("PASS: exact-v2(d)=5 three-atom rigidity for both layer masses>=1949")
