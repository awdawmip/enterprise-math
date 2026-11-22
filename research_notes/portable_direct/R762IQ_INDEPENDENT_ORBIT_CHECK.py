#!/usr/bin/env python3
"""Independent exact 2-missing-support parity obstructions and S6 orbits."""
from itertools import combinations, permutations
from collections import Counter, defaultdict
P=list(combinations(range(6),2))
S=list(combinations(range(6),3))
I={a:i for i,a in enumerate(P)}
TRI=[[I[tuple(a)] for a in combinations(s,2)] for s in S]
FORCED=[sum(1<<i for i,t in enumerate(TRI) if sum((m>>v)&1 for v in t)>=2)
        for m in range(1<<15)]
def analyze(z,m):
    parent=list(range(15))
    def root(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]
            a=parent[a]
        return a
    def join(a,b):
        ra,rb=root(a),root(b)
        if ra!=rb: parent[ra]=rb
    boundary=0
    for i,t in enumerate(TRI):
        if z>>i&1: continue
        live=[v for v in t if not (m>>v&1)]
        if len(live)==3:
            join(live[0],live[1]); join(live[1],live[2])
        elif len(live)==2:
            boundary^=(1<<live[0])^(1<<live[1])
        else:
            raise AssertionError('local incidence violated')
    charge=0
    for v in range(15):
        if boundary>>v&1: charge^=1<<root(v)
    cc=defaultdict(list)
    for v in range(15):
        if not (m>>v&1): cc[root(v)].append(v)
    return [tuple(C) for r,C in cc.items() if charge>>r&1], tuple(cc.values())
fails=[]
by_pair=Counter()
for a,b in combinations(range(20),2):
    z=(1<<a)|(1<<b)
    for m,f in enumerate(FORCED):
        if f&~z: continue
        odd,cc=analyze(z,m)
        if odd:
            fails.append((a,b,m))
            overlap=len(set(S[a])&set(S[b]))
            by_pair[(overlap,m.bit_count())]+=1
            assert len(cc)==2 and sorted(map(len,cc))==[1,14-m.bit_count()]
            assert sorted(map(len,odd))==[1,14-m.bit_count()]
assert len(fails)==720 and by_pair=={(1,3):360,(1,4):360}
keyset=set(fails)
sym=[]
for perm in permutations(range(6)):
    pi={i:I[tuple(sorted((perm[u],perm[v])))] for i,(u,v) in enumerate(P)}
    si={i:S.index(tuple(sorted(perm[v] for v in s))) for i,s in enumerate(S)}
    sym.append((pi,si))
orbits=[]
while keyset:
    a,b,m=min(keyset)
    orbit=set()
    for pi,si in sym:
        m2=sum(1<<pi[i] for i in range(15) if m>>i&1)
        a2,b2=sorted((si[a],si[b]))
        orbit.add((a2,b2,m2))
    assert orbit <= keyset
    keyset-=orbit
    orbits.append((len(orbit),m.bit_count(),S[a],S[b],
                  tuple(P[i] for i in range(15) if m>>i&1)))
assert sorted(x[0] for x in orbits)==[360,360]
assert sorted(x[1] for x in orbits)==[3,4]
print('PASS R762IQ_INDEPENDENT_TWO_ZERO_SCAN; failures=720')
print('by overlap and inactive size:',dict(by_pair))
print('S6 orbits:',orbits)
