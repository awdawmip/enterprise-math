#!/usr/bin/env python3
"""Exact sixth reciprocal moment p-adic sieve for T6, two v2(d)=5 atoms on each side."""
from collections import defaultdict
from functools import lru_cache
from heapq import heappop, heappush
from itertools import combinations_with_replacement

CAP=2331
KS=range(1,7)
MOD=tuple(1<<k for k in KS)
profiles=[(a,b) for a,b in combinations_with_replacement(range(1,72,2),2)
          if 32*(a+b)-2<=CAP]
assert len(profiles)==342

def sig(js,k,m): return sum(pow(j,-k,m) for j in js)%m
def add(a,b): return tuple((x+y)%m for x,y,m in zip(a,b,MOD))
def low(js): return tuple(sig(js,k,1<<k) for k in KS)
def residue(a,b):
    ans=[]
    for k in KS:
        d=(sig(a,k,1<<(2*k))-sig(b,k,1<<(2*k)))%(1<<(2*k))
        assert d%(1<<k)==0
        ans.append(d//(1<<k))
    return tuple(ans)

g4=[(tuple(pow(j,-k,1<<k) for k in KS),16*j-1)
    for j in range(1,146,2)]
zero=(0,)*6
best={zero:0};heap=[(0,zero)]
while heap:
    cost,s=heappop(heap)
    if cost!=best[s]:continue
    for g,w in g4:
        c=cost+w
        if c>CAP:continue
        t=add(s,g)
        if c<best.get(t,CAP+1):
            best[t]=c
            heappush(heap,(c,t))
assert len(best)==2048 and max(best.values())==813

by=defaultdict(list)
for p in profiles:by[low(p)].append(p)
counts=[0]*4
remaining=[]
for grp in by.values():
    for i,a in enumerate(grp):
        for b in grp[i+1:]:
            counts[0]+=1
            t=residue(a,b)
            if (t[3]-t[5])%8:continue
            counts[1]+=1
            if t not in best:continue
            counts[2]+=1
            ra=CAP-(32*sum(a)-2)
            rb=CAP-(32*sum(b)-2)
            if any(c<=ra and best.get(add(s,t),CAP+1)<=rb
                   for s,c in best.items()):
                counts[3]+=1
                remaining.append((a,b,ra,rb))
assert counts==[1038,82,33,26]

def prime_factors(n):
    out=set()
    d=2
    while d*d<=n:
        while n%d==0:
            out.add(d);n//=d
        d+=1
    if n>1:out.add(n)
    return out

@lru_cache(maxsize=None)
def sixth_residue_set(p,budget):
    modulus=p**6
    steps=[(p*u-1,pow(u,-6,modulus))
           for u in range(1,(budget+1)//p+1)]
    out=set()
    def rec(i,mass,signature):
        if i==len(steps):
            out.add(signature)
            return
        w,g=steps[i]
        for _ in range((budget-mass)//w+1):
            rec(i+1,mass,signature)
            mass+=w
            signature=(signature+g)%modulus
    rec(0,0,0)
    return out

def high_sixth(profile,p):
    return sum(pow(32*(j//p),-6,p**6)
               for j in profile if j%p==0)%(p**6)

excluded=[]
survivors=[]
for i,(a,b,ra,rb) in enumerate(remaining,1):
    witnesses=[]
    for p in sorted(set().union(*(prime_factors(j) for j in a+b))):
        if p<17 or p*p<=max(ra,rb)+1:continue
        m=p**6
        ha=high_sixth(a,p);hb=high_sixth(b,p)
        if ha==hb:continue
        sa={(ha+s)%m for s in sixth_residue_set(p,ra)}
        sb={(hb+s)%m for s in sixth_residue_set(p,rb)}
        if sa.isdisjoint(sb):
            witnesses.append((p,len(sa),len(sb)))
    if witnesses:
        excluded.append(i)
        print('EXCLUDED',i,a,b,'witnesses',witnesses)
    else:
        survivors.append(i)
        print('OPEN',i,a,b,'budgets',ra,rb)
assert excluded==[2,4,5,6,8,10,12,14,15,16,17,18,19,20,21,22,24,25,26]
assert survivors==[1,3,7,9,11,13,23]
print('PASS: 26 necessary-condition pairs; 19 excluded; 7 remain')
