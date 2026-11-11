#!/usr/bin/env python3
"""R711 exact certificate; standard library, integers and Fraction only."""
from itertools import combinations, permutations
from fractions import Fraction
from collections import Counter
import json

V=tuple(range(6))
E=tuple(combinations(V,2))
EI={e:i for i,e in enumerate(E)}
T=tuple(combinations(V,3))
TE=tuple(sum(1<<EI[e] for e in combinations(t,2)) for t in T)
COMP=tuple(T.index(tuple(v for v in V if v not in t)) for t in T)

def triangles(g):
    return sum(1<<i for i,need in enumerate(TE) if g&need==need)

def has_factor(tmask):
    return any((tmask>>i&1) and (tmask>>COMP[i]&1) for i in range(20))

TM=[triangles(g) for g in range(1<<15)]
FACTOR=[has_factor(t) for t in TM]
NO_FACTOR=sum(not f for f in FACTOR)
MAXIMAL=[g for g in range(1<<15) if not FACTOR[g]
         and all(FACTOR[g | (1<<i)] for i in range(15) if not g>>i&1)]
PERM_BITS=[]
for p in permutations(V):
    PERM_BITS.append(tuple(1<<EI[tuple(sorted((p[a],p[b])))] for a,b in E))

def canonical(g):
    return min(sum(new[i] for i in range(15) if g>>i&1) for new in PERM_BITS)

CLASSES={}
for m in MAXIMAL:
    CLASSES.setdefault(canonical(m),[]).append(m)

def license(g):
    return [T[i] for i in range(20) if TM[g]>>i&1]

def witness(ts):
    used=set(x for t in ts for x in t)
    for v in V:
        if v not in used:return ("UNUSED_VERTEX",[v])
    for v in V:
        if all(v in t for t in ts):return ("COMMON_VERTEX",[v])
    for s in combinations(V,3):
        if all(len(set(s)&set(t))>=2 for t in ts):
            return ("DOUBLE_HIT_TRIPLE",list(s))
    return None

assert len(TM)==32768 and NO_FACTOR==28662
assert len(MAXIMAL)==182 and len(CLASSES)==4
assert sorted(len(a) for a in CLASSES.values())==[20,30,60,72]
assert all(FACTOR[g] or any(g&m==g for m in MAXIMAL) for g in range(1<<15))
rows=[]
for m,orbit in sorted(CLASSES.items()):
    ts=license(m)
    proof=witness(ts)
    assert proof
    rows.append(dict(canonical_mask=m,orbit_size=len(orbit),
                     edge_count=m.bit_count(),triangle_count=len(ts),
                     edges=[list(e) for i,e in enumerate(E) if m>>i&1],
                     triangles=[list(t) for t in ts],
                     obstruction_type=proof[0],obstruction_vertices=proof[1]))
assert [(r["canonical_mask"],r["orbit_size"]) for r in rows]==[(4095,20),(5887,30),(6142,60),(7071,72)]

# Connected nine-tagged-quanta graph: K4, K5 and one cross bridge.
E9=set(combinations(range(4),2))|set(combinations(range(4,9),2))|{(3,4)}
T9=tuple(t for t in combinations(range(9),3) if all(e in E9 for e in combinations(t,2)))
WEIGHTS={t:(Fraction(1,3) if t[0]<4 else Fraction(1,6)) for t in T9}
assert len(E9)==17 and len(T9)==14
assert all(sum(w for t,w in WEIGHTS.items() if v in t)==1 for v in range(9))
assert sum(WEIGHTS.values())==3
assert not any(set(a).isdisjoint(b) and set(a).isdisjoint(c) and set(b).isdisjoint(c)
               for a,b,c in combinations(T9,3))

report=dict(schema="EM_R711_EXACT_GRAPH_TRIANGLE_CERTIFICATE_V1",
            graph_count=32768,without_integral_factor=NO_FACTOR,
            with_integral_factor=sum(FACTOR),maximal_obstructions=182,
            isomorphism_classes=4,orbit_certificates=rows,
            nine_quantum_counterexample=dict(vertex_count=9,edge_count=17,
              triangle_count=14,weight_total="3",saturation_verified=True,
              integral_factor=False,
              weights=[dict(triangle=list(t),weight=str(w)) for t,w in WEIGHTS.items()]),
            finite_validation="PASS",
            limitations="No native X6 Link/Port or V29/V39 legality verified")
print("R711_SIX_VERTEX_CLIQUE_TRIANGLE_GAP_EXACT_PASS",32768,NO_FACTOR,len(MAXIMAL),len(CLASSES),len(T9))
