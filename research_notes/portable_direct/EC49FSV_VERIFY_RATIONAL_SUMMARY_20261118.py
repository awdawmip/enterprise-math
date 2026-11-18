#!/usr/bin/env python3
"""Offline exact-rational summary audit for EC49FSV; use complete bundle VERIFY.py for native source replay."""
from pathlib import Path
from fractions import Fraction as Q
import json,sys

p=Path(__file__).with_name("EC49FSV_Q140_SATURATION_CERT_20261118.json")
C=json.loads(p.read_text())
assert C["source_pin"]=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
A,B=Q(2,3),Q(7,16)
lo,hi=Q(5,8),Q(1)
dstar,sstar=Q(259,404),Q(1531,2304)
assert lo<dstar<sstar<hi

def cost(t,orientation,z):
    U,N32,N34,N140=t
    return Q(U)-(A*N32+B*N34 if orientation=="direct" else B*N32+A*N34)-z*N140

for orient in ("direct","swapped"):
    trees=[tuple(x["vector"]) for x in C[orient]["planes"]]
    assert len(trees)==3
    vertices=[Q(z) for z,_ in C[orient]["oracle_vertices"]]
    assert vertices==sorted(vertices) and vertices[0]==lo and vertices[-1]==hi
    for z,expected in C[orient]["oracle_vertices"]:
        assert min(cost(t,orient,Q(z)) for t in trees)==Q(expected)

D1,D2=(324,141,47,40),(319,18,75,141)
S1,S2=(324,8,141,93),(327,9,97,141)
def D(z):return min(cost(t,"direct",z) for t in (D1,D2))
def S(z):return min(cost(t,"swapped",z) for t in (S1,S2))
assert cost(D1,"direct",dstar)==cost(D2,"direct",dstar)
assert cost(S1,"swapped",sstar)==cost(S2,"swapped",sstar)
assert [D(z)-S(z) for z in (lo,dstar,sstar,hi)]==[Q(257,16),Q(27335,1616),Q(379,24),Q(379,24)]
assert D2[-1]==141 and S2[-1]==141
print("PASS exact rational continuous-envelope bookkeeping; raw Bellman and full-tree witnesses: execute archive VERIFY.py --oracle --independent")
