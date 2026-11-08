#!/usr/bin/env python3
"""Independent integer audit of the exact operator/observer involution."""
import json
from collections import Counter, defaultdict
from itertools import product
from pathlib import Path
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
     'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
ORDER='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
QUOTA={2:4,3:2,4:2,5:4,6:2,7:4,8:4,9:2}
CLAUSES=(18,20,33,40)
TABLE=str.maketrans('cdfg','dcgf')
STATE=(0,1,3,2,5,4,7,6,8)
PI={0:0,1:4,4:1,2:8,8:2,16:32,32:16}
def inv(w): return w.translate(TABLE)
def kmap(k):
    x,y,z=k
    return (y+2*z,x-2*z,z)
def native(w): return tuple(t for a in w for t in OPS[a])
def key(w):
    c=Counter(t for t in native(w) if t>0)
    return (c[1],c[2],c[3])
def signature(w):
    q=0
    for a in w: q=T[q][ORDER.index(a)]
    return SIG[q]
def native_cost(words):
    return len({native(w)[:i] for w in words for i in range(1,len(native(w))+1)})
def operator_cost(words):
    d=defaultdict(set)
    for w in words:
        for i,a in enumerate(w):d[w[:i]].add(a)
    return sum(len(OPS[a]) for children in d.values() for a in children)-sum({'c','f'}<=s for s in d.values())-sum({'d','g'}<=s for s in d.values())
def verify(groups,A,B,C):
    words=[w for group in groups.values() for w in group]
    assert len(words)==24 and len(set(words))==24
    assert {int(h):len(v) for h,v in groups.items()}==QUOTA
    kk=set()
    for h,group in groups.items():
        h=int(h);mask=0
        for w in group:
            assert len(w)==h
            steps=native(w)
            assert tuple(steps.count(i)-steps.count(-i) for i in range(1,7))==(2,0,0,0,0,0)
            k=key(w);kk.add(k)
            if h>=4:assert k==(A if h==4 else B if h in (5,6) else C)
            assert len(steps)==2*sum(k)-2
            mask|=signature(w)
        assert all(mask&cl for cl in CLAUSES)
    assert len(kk)<=5
    return native_cost(words),operator_cost(words)
for q,a in product(range(9),ORDER):
    assert STATE[T[q][ORDER.index(a)]]==T[STATE[q]][ORDER.index(inv(a))]
    assert SIG[STATE[q]]==PI[SIG[q]]
for a in ORDER:
    assert key(inv(a))==kmap(key(a))
    assert sum(OPS[a])==sum(OPS[inv(a)])
A=[(3,2,1),(4,1,1)]
B=[(3,4,1),(4,3,1),(5,2,1),(5,2,2),(6,1,1),(6,1,2)]
C=[(4,6,1),(5,5,1),(6,4,1),(6,4,2),(7,3,1),(7,3,2),(8,2,1),(8,2,2),(8,2,3)]
assert all(set(map(kmap,v))==set(v) for v in (A,B,C))
triples=set(product(A,B,C))
orbits={tuple(sorted([t,tuple(map(kmap,t))])) for t in triples}
assert len(triples)==108 and len(orbits)==54 and all(len(v)==2 for v in orbits)
witnesses=json.loads(Path(__file__).with_name('EC49FEF_WITNESS.json').read_text())
assert len(witnesses)==2
for row in witnesses:
    a,b,c=map(tuple,[row['A'],row['B'],row['C']])
    val,weighted=verify(row['words'],a,b,c)
    assert val==weighted==row['cost']==118
    mirror={h:[inv(w) for w in v] for h,v in row['words'].items()}
    mircost,mirweighted=verify(mirror,kmap(a),kmap(b),kmap(c))
    assert mircost==mirweighted==val
    assert row['mip_status']==0 and row['mip_gap']==0
    assert row['late_primal']==row['late_dual_bound']==83
print(json.dumps({'DFA_equalities':54,'late_orbits':54,'complete_systems_checked':4,'paths_per_system':24,'native_cost_per_system':118},sort_keys=True))
