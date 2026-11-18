#!/usr/bin/env python3
"""Verify the R5 weighted probe extension against exact prior frozen inputs.
Requires VERIFY_ADAPTIVE_EXACT.py and its three original data files in this folder.
"""
from pathlib import Path
from collections import defaultdict, Counter
from fractions import Fraction
import runpy

P = Path(__file__).resolve().parent
base = runpy.run_path(str(P/'VERIFY_ADAPTIVE_EXACT.py'))
components, support = base['comp'], base['support']
C, S = base['C'], base['S']
triple = Counter()
for anchor,vs in sorted(components.items()):
    groups = defaultdict(list)
    for a in sorted(vs):
        groups[(support(a,214,4),support(a,214,8))].append(a)
    if len(groups) != 3:
        continue
    reps = [g[0] for g in groups.values()]
    for k in C:
        for j in range(len(S)):
            buckets = defaultdict(list)
            for i, a in enumerate(reps):
                buckets[support(a,k,j)].append(i)
            actual = tuple(sorted(tuple(v) for v in buckets.values()))
            expected = (((0,), (1,2)) if k==214 and 4<=j<=7 else
                        ((0,1), (2,)) if k==214 and 8<=j<=15 else
                        ((0,1,2),))
            assert actual == expected, (anchor,k,j,actual,expected)
    sizes = tuple(map(len,groups.values()))
    assert sizes in ((1,1,1),(2,2,2))
    triple[sizes]+=1
assert triple == {(1,1,1):16,(2,2,2):24}, triple

def expected(p):
    p=tuple(map(Fraction,p))
    assert len(p)==3 and all(v>=0 for v in p) and sum(p)==1
    return 2-max(p[0],p[2])

assert expected([Fraction(1,3)]*3)==Fraction(5,3)
assert expected([Fraction(1,6),Fraction(2,3),Fraction(1,6)])==Fraction(11,6)
assert expected([Fraction(2,3),Fraction(1,6),Fraction(1,6)])==Fraction(4,3)
N=30876
endpoints=N*101*2
full=N*101*18
fixed=256+192*2
adaptive=256+192*expected([Fraction(1,3)]*3)
assert (endpoints,full,fixed,adaptive)==(6236952,56132568,640,576)
print('PASS_R5_WEIGHTED_EXTENSION',sum(triple.values()),len(C)*len(S)*sum(triple.values()),
      expected([Fraction(1,3)]*3),expected([Fraction(1,6),Fraction(2,3),Fraction(1,6)]),
      endpoints, full, endpoints+int(adaptive),Fraction(fixed-int(adaptive),endpoints+fixed))
