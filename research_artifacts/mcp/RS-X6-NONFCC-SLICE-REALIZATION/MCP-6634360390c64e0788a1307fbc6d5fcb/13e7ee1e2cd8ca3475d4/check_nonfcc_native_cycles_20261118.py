#!/usr/bin/env python3
"""Exact finite checks for a scoped signed-X6 Cell graph lemma. Python 3 stdlib."""
from itertools import combinations, permutations
from collections import Counter
E = tuple(combinations(range(4), 2))  # historical S4 / K4 atlas labels
D = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
def trace(w):
    p=[0,0,0]; out=[tuple(p)]
    for d in w:
        for j in range(3): p[j]+=D[d][j]
        out.append(tuple(p))
    return out
def simple(w):
    t=trace(w)
    return t[-1]==t[0] and len(set(t[:-1]))==len(w)
assert simple((0,2,4,1,3,5))
w12=(0,0,2,1,1,2,4,3,4,3,5,5)
assert simple(w12) and Counter(w12)==Counter({k:2 for k in range(6)})
assert sum(simple(w) for w in permutations(range(6)))==192
triples=list(combinations(range(6),3))
def kind(t):
    degrees=[0]*4
    for k in t:
        a,b=E[k];degrees[a]+=1;degrees[b]+=1
    return {(3,1,1,1):"STAR",(2,2,2,0):"FACE",(2,2,1,1):"PATH"}[tuple(sorted(degrees,reverse=True))]
assert len(triples)==20 and Counter(map(kind,triples))=={"STAR":4,"FACE":4,"PATH":12}
base=triples[0]
assert {tuple(sorted(p[k] for k in base)) for p in permutations(range(6))}==set(triples)
lookup={e:k for k,e in enumerate(E)}
def permute(t,p):
    return tuple(sorted(lookup[tuple(sorted((p[E[k][0]],p[E[k][1]])))] for k in t))
seen=set();orbits=[]
for t in triples:
    if t in seen: continue
    orbit={permute(t,p) for p in permutations(range(4))}
    orbits.append((kind(t),len(orbit)));seen|=orbit
assert sorted(orbits)==sorted([("STAR",4),("FACE",4),("PATH",12)])
face={lookup[(0,1)],lookup[(0,2)],lookup[(1,2)]}
def obs(z):
    v=[z[k] for k in sorted(face)];return tuple(i-min(v) for i in v)
z=(0,)*6
h=tuple(int(k in face) for k in range(6))
a=next(k for k in range(6) if k not in face)
off=tuple(int(k==a) for k in range(6))
assert z!=h and obs(z)==obs(h)==obs(off)==(0,0,0)
assert any(off[k] for k in range(6) if k not in face)
print("PASS: signed C6/C12 witness; 192/720 finite C6; 20 triples; S6 1 orbit; S4 4/4/12; observer witness")
