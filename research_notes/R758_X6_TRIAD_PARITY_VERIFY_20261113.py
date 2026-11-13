#!/usr/bin/env python3
"""Exact R758 X6 primitive-path and three-port-cycle verifier. stdlib only."""
from itertools import product, combinations, permutations
from collections import Counter, defaultdict
D=tuple((i,s) for i in range(6) for s in (-1,1))
Z=(0,)*6
def end(word):
    x=[0]*6
    for i,s in word:x[i]+=s
    return tuple(x)
def B(ports):
    p,q,r=ports
    return frozenset(((p,q),(q,r),(r,p)))
def re(p,g):return (g[p[0]],p[1])
v=Counter()
for w in product(D,repeat=3):
    z=end(w)
    assert z!=Z
    v[sum(abs(x) for x in z)]+=1
assert v==Counter({1:396,3:1332})
closed=0
for axes in combinations(range(6),3):
    d=tuple((i,s) for i in axes for s in (-1,1))
    for w in permutations(d):
        assert end(w)==Z
        closed+=1
assert closed==14400
P={Z:1}; returns={0:1}
for n in range(1,7):
    Q=defaultdict(int)
    for z,c in P.items():
        for i,s in D:
            zz=list(z);zz[i]+=s
            Q[tuple(zz)]+=c
    P=Q;returns[n]=P.get(Z,0)
assert returns=={0:1,1:0,2:12,3:0,4:396,5:0,6:19920}
cycles=set()
for axes in combinations(range(6),3):
    for signs in product((-1,1),repeat=3):
        p,q,r=tuple(zip(axes,signs))
        cycles.add(B((p,q,r)))
        cycles.add(B((p,r,q)))
assert len(cycles)==320
for edges in cycles:
    u=Counter()
    for p,q in edges:u[p]+=1;u[q]-=1
    assert all(x==0 for x in u.values())
num=0
for g in permutations(range(6)):
    for edges in cycles:
        assert frozenset((re(p,g),re(q,g)) for p,q in edges) in cycles
        num+=1
assert num==230400
for axes in combinations(range(6),3):
    for signs in product((-1,1),repeat=3):
        z=end(tuple(zip(axes,signs)))
        assert sum(x*x for x in z)==3 and z!=Z
print({"three_step_L1_counts":dict(sorted(v.items())),
       "closed_walks_by_length":returns,
       "six_step_three_axis_closed_words":closed,
       "oriented_signed_port_cycles":len(cycles),
       "S6_covariance_checks":num,
       "status":"R758_X6_TYPED_PARITY_AND_PORT_CYCLE_EXACT_PASS"})
