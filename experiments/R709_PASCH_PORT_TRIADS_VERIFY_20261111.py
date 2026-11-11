#!/usr/bin/env python3
"""R709 exact six-axis port-filtered triad-support checker.

Checks a finite combinatorial model, NOT a native V29/V39 or BRC physics engine.
Uses only exact integers and rational Fraction source weights.
"""
from itertools import combinations, permutations
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path

V=tuple(range(6))
E=tuple(combinations(V,3))
U=set(V)
P=((0,1,2),(0,3,4),(1,3,5),(2,4,5))
comp=lambda e:tuple(sorted(U.difference(e)))

def degree(H):
    return tuple(sum(i in e for e in H) for i in V)

def covers(H):
    s=set(H)
    return sum(comp(e) in s for e in H)//2

def pasch(H):
    return len(H)==4 and degree(H)==(2,)*6 and all(
        len(set(a)&set(b))==1 for a,b in combinations(H,2))

def fractional_half(H):
    return all(sum((Fraction(1,2) for e in H if i in e),Fraction(0))==1
               for i in V)

assert len(E)==20
assert all(comp(comp(e))==e for e in E)
assert len({tuple(sorted((a,comp(a)))) for a in E})==10
assert pasch(P) and fractional_half(P) and covers(P)==0

families=0
witnesses=set()
for H in combinations(E,4):
    families+=1
    if pasch(H):
        assert fractional_half(H) and covers(H)==0
        witnesses.add(H)
assert families==4845 and len(witnesses)==30

orbit={tuple(sorted(tuple(sorted(p[i] for i in a)) for a in P))
       for p in permutations(V)}
assert orbit==witnesses and len(orbit)==30

def residual(a,b):
    c=Counter(a)+Counter(b)
    return sum(abs(c[i]-1) for i in V)

c=Counter(residual(a,b) for a in P for b in P)
assert c=={2:12,6:4}
new=comp(P[0])
assert new not in P
Q=P+(new,)
assert covers(Q)==1
complete=[(a,b) for a in Q for b in Q if residual(a,b)==0]
assert len(complete)==2
assert Fraction(len(complete),len(Q)**2)==Fraction(2,25)
assert [b for b in Q if residual(P[0],b)==0]==[new]

result={
 "schema":"EM_R709_PORT_FILTER_PASCH_EXACT_EVIDENCE_V1",
 "task":"RS-X6-TRIADIC-CLOSURE-DYNAMICS",
 "publication":"TP2-8B7E13C5904A2D6F1142",
 "frozen_science":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
 "date":"2026-11-11",
 "model":"candidate six-axis permitted 3-uniform hypergraph, individually labeled equal-q tokens, positive rational provenance branches",
 "six_axis_triples":20,
 "four_edge_families":families,
 "pasch_families":len(witnesses),
 "pasch_permutation_orbit":len(orbit),
 "pasch_edges":[list(a) for a in P],
 "pasch_axis_degrees":list(degree(P)),
 "fractional_weights":["1/2"]*4,
 "pasch_integral_covers":covers(P),
 "pre_repair_residual_counts":{str(k):v for k,v in sorted(c.items())},
 "added_complement":list(new),
 "post_repair_integral_covers":covers(Q),
 "post_repair_uniform_exact_observer_probability":"2/25",
 "verification":"R709_PASCH_PORT_TRIADS_EXACT_PASS",
 "native_status":"native Link/Port + V29/V39 integration not executed"
}
out=Path(__file__).with_name("R709_PASCH_PORT_TRIADS_EVIDENCE_20261111.json")
out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
print(result["verification"],families,len(witnesses),len(orbit),"2/25")
