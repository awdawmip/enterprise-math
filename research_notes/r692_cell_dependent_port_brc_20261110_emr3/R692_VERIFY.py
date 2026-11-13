#!/usr/bin/env python3
"""R692 exact E* cell-gated signed-square BRC kernel test. Python standard library."""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations,product
E=(0,2,4); O=(1,3,5)
T={(0,0):(0,1,2),(1,0):(0,1,3),(2,0):(0,1,4),
   (0,1):(0,2,3),(1,1):(1,2,3),(2,1):(0,1,3)}
Z=(0,)*6
def phase(z):return (sum(z[i] for i in E)%3,sum(z[i] for i in O)%2)
def plus(z,i,s):
    v=list(z);v[i]+=s;return tuple(v)
def transport(frame,u,v):
    old=next(iter(set(u)-set(v)));new=next(iter(set(v)-set(u)))
    return tuple(new if x==old else x for x in frame)
def square(z,i,j,s,t):
    start=z;f=T[phase(z)];g=[]
    for ax,d in ((i,s),(j,t),(i,-s),(j,-t)):
        g.append((z,ax,d));n=plus(z,ax,d)
        f=transport(f,T[phase(z)],T[phase(n)]);z=n
    assert z==start
    return tuple(T[phase(z)].index(x) for x in f),tuple(g)
def sources(z,axes=range(6)):
    return {(i,j,s,t):square(z,i,j,s,t) for i,j in combinations(axes,2)
            for s,t in product((-1,1),repeat=2)}
def kernel(S,denied=frozenset()):
    kept={q:p for q,(p,G) in S.items() if all(g not in denied for g in G)}
    counts=Counter(kept.values());N=len(kept)
    return counts,N,{p:Fraction(n,N) for p,n in counts.items()} if N else {}
ID=(0,1,2);TAU=(0,2,1);C=(1,2,0);C2=(2,0,1)
for a,b in product(range(3),range(2)):
    z=(a,b,0,0,0,0);S=sources(z)
    assert len(S)==60
    expected=[{ID:24,TAU:18,C:6,C2:12},
              {ID:42,C:12,C2:6},{ID:42,TAU:18}][a]
    assert dict(kernel(S)[0])==expected,(a,b)
S=sources(Z)
uses=Counter(g for _,G in S.values() for g in G)
assert len(uses)==140 and sum(uses.values())==240
assert len({g[0] for g in uses})==73
assert Counter(uses.values())=={1:120,2:4,4:4,6:4,8:4,10:4}
assert max(sum(abs(x) for x in g[0]) for g in uses)==2
for gate,n in uses.items():
    _,remain,_=kernel(S,{gate});assert remain==60-n
a=plus(Z,0,1);corner=plus(a,1,1)
g2=(a,1,1);g3=(corner,0,-1)
assert uses[g2]==uses[g3]==1
assert [q for q,(_,G) in S.items() if g3 in G]==[(0,1,1,1)]
for g in (g2,g3):
    cnt,n,_=kernel(S,{g})
    assert n==59 and cnt=={ID:24,TAU:18,C:6,C2:11}
S2=sources(Z,(0,1))
assert kernel(S2)[0]=={TAU:2,C2:2}
gplus=(plus(a,1,1),0,-1);gminus=(plus(a,1,-1),0,-1)
cnt,n,mass=kernel(S2,{gplus,gminus})
assert (n,cnt,mass)==(2,{TAU:2},{TAU:Fraction(1)})
coverage=defaultdict(set)
for q,(p,G) in S2.items():
    if p==C2:
        for g in G:
            if g[0]!=Z:coverage[g].add(q)
assert max(map(len,coverage.values()))==1
print('R692_DYNAMIC_PORT_GATE_BRC_EXACT_PASS')
