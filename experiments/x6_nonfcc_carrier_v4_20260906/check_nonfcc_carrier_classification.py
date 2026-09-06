#!/usr/bin/env python3
"""Exact FCC carrier classification and A6 normalization for all 20 X6 charts."""
from itertools import combinations, permutations, product
from collections import Counter

# K4 edge / native-axis labels in fixed order.
NAMES=('AB','AC','AD','BC','BD','CD')
EDGES=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
EINDEX={tuple(sorted(e)):i for i,e in enumerate(EDGES)}

# One standard unoriented FCC nearest-neighbor line-family representative set.
V=((1,1,0),(1,0,1),(0,1,-1),(0,1,1),(1,0,-1),(1,-1,0))

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def det3(cols):
    a,b,c=cols
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
           -a[1]*(b[0]*c[2]-b[2]*c[0])
           +a[2]*(b[0]*c[1]-b[1]*c[0]))
def gram_det(S): return det3(tuple(V[i] for i in S))**2
def rank(S): return 2 if gram_det(S)==0 else 3

def graph_type(S):
    deg=[0]*4
    for i in S:
        a,b=EDGES[i]; deg[a]+=1;deg[b]+=1
    ds=tuple(sorted(deg,reverse=True))
    return {(3,1,1,1):'STAR',(2,2,2,0):'FACE',(2,2,1,1):'PATH'}[ds]

def orient120_count(S):
    n=0
    for ss in product((-1,1),repeat=3):
        W=[tuple(ss[r]*x for x in V[i]) for r,i in enumerate(S)]
        if all(dot(W[a],W[b])==-1 for a,b in combinations(range(3),2)):
            n+=1
    return n

def parity(p): return sum(p[i]>p[j] for i in range(6) for j in range(i+1,6))%2
def actset(p,S): return frozenset(p[i] for i in S)

CHARTS=tuple(combinations(range(6),3))
rows=[]
for S in CHARTS:
    typ=graph_type(S); gd=gram_det(S); rk=rank(S); oc=orient120_count(S)
    pairdots=tuple(dot(V[a],V[b]) for a,b in combinations(S,2))
    rows.append((S,typ,rk,gd,pairdots,oc))

assert Counter(r[1] for r in rows)==Counter({'STAR':4,'FACE':4,'PATH':12})
assert Counter((r[1],r[2],r[3],r[5]) for r in rows)==Counter({
    ('STAR',2,0,2):4,
    ('FACE',3,4,0):4,
    ('PATH',3,4,0):12,
})

# Structural obstructions: PATH has one carrier-orthogonal line pair. FACE has
# three nonzero +/-1 pair dots whose product is +1, while an all-120 target has
# product (-1)^3=-1; sign reorientation cannot change this product.
for S,typ,rk,gd,dots,oc in rows:
    if typ=='PATH': assert 0 in dots
    if typ=='FACE': assert 0 not in dots and dots[0]*dots[1]*dots[2]==1
    if typ=='STAR': assert oc==2

# K4 vertex permutations induce an S4 subgroup of even permutations on 6 edges.
def induced(vp):
    out=[]
    for a,b in EDGES:
        out.append(EINDEX[tuple(sorted((vp[a],vp[b])))])
    return tuple(out)
S4EDGE={induced(vp) for vp in permutations(range(4))}
assert len(S4EDGE)==24 and all(parity(p)==0 for p in S4EDGE)
unseen={frozenset(S) for S in CHARTS}; orbit_types=[]
while unseen:
    S=next(iter(unseen)); orb={actset(p,S) for p in S4EDGE}; unseen-=orb
    kinds={graph_type(tuple(sorted(T))) for T in orb}
    assert len(kinds)==1
    orbit_types.append((next(iter(kinds)),len(orb)))
assert sorted(orbit_types)==[('FACE',4),('PATH',12),('STAR',4)]

# Full A6 is transitive on all 20 charts. Normalize every chart to reference STAR.
S6=tuple(permutations(range(6)))
A6=tuple(p for p in S6 if parity(p)==0)
assert len(A6)==360
REF=frozenset((0,1,2)) # AB,AC,AD star
assert graph_type(tuple(sorted(REF)))=='STAR'
for S in map(frozenset,CHARTS):
    lifts=[p for p in A6 if actset(p,S)==REF]
    assert len(lifts)==18

# If local cyclic orientation is retained, the normalization fiber has 9 lifts.
def cyc(t):
    a,b,c=t; return {(a,b,c),(b,c,a),(c,a,b)}
REF_OR=(0,1,2)
ORIENTED=[]
for S in CHARTS:
    a,b,c=S; ORIENTED.extend(((a,b,c),(a,c,b)))
assert len(ORIENTED)==40
for o in ORIENTED:
    assert sum(tuple(p[i] for i in o) in cyc(REF_OR) for p in A6)==9
    # Fully ordered visible-slot map leaves exactly 3 hidden-complement lifts.
    assert sum(tuple(p[i] for i in o)==REF_OR for p in A6)==3

print('PASS_X6_NONFCC_CARRIER_CLASSIFICATION_V4')
print('chart_types','STAR=4 FACE=4 PATH=12')
print('STAR_carrier_rank',2)
print('FACE_carrier_rank',3)
print('PATH_carrier_rank',3)
print('direct_all_120_FCC_charts',4)
print('S4_carrier_orbits',sorted(orbit_types))
print('A6_chart_orbit_size',20)
print('A6_unoriented_normalization_lifts',18)
print('A6_oriented_normalization_lifts',9)
print('A6_ordered_slot_normalization_lifts',3)
