#!/usr/bin/env python3
"""EC49FSF: 3/8 joint q32/q34 discount, native q140 z in [0,1].
Recompute in the EC49FSE complete original-science evidence directory.
Requires its frozen original master/profile CSV, EC49FSA_THREE_OBSERVER_SOLVER.py,
and EC49FSA_FSB_INDEPENDENT_CHECK.py (each preserves all 228 named observers).
"""
from fractions import Fraction as F
from collections import Counter
from EC49FSA_THREE_OBSERVER_SOLVER import solve, V, PIN
from EC49FSA_FSB_INDEPENDENT_CHECK import certify
assert PIN=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
alpha=F(3,8)
rows=[
("0","3/56","1901/8",8,304,36,141,34),
("3/56","1/16","238",15,301,27,141,34),
("1/16","1/6","1905/8",17,303,32,141,34),
("1/6","5/14","1925/8",32,304,28,141,34),
("5/14","3/8","1965/8",46,309,28,141,34),
("3/8","2/5","2019/8",64,309,10,141,34),
("2/5","77/192","2035/8",69,311,10,141,34),
("77/192","1","1133/4",141,305,7,51,140)]
vertices=sorted({F(s) for row in rows for s in row[:2]})
def value_at(z):
    info, tree=solve({32:alpha,34:alpha,140:z})
    v=F(info["numerator"],info["denominator"])
    other=certify({32:alpha,34:alpha,140:z})
    assert F(other["value"])==v,(z,v,other)
    return v
bellman={z:value_at(z) for z in vertices}
for lo,hi,A,K,U,N32,N34,root in rows:
    lo,hi,A=F(lo),F(hi),F(A)
    assert bellman[lo]==A-K*lo and bellman[hi]==A-K*hi
    z=(lo+hi)/2
    info,tree=solve({32:alpha,34:alpha,140:z})
    counts=Counter()
    for i in range(141):
        node=tree; used=set()
        while "named_observer" in node:
            q=node["named_observer"]
            assert q not in used
            used.add(q);counts[q]+=1
            node=node["children"][str(V[q][i])]
        assert node=={"leaf":i}
    assert (sum(counts.values()), counts[32], counts[34],counts[140],info["root"])==(U,N32,N34,K,root)
    assert F(U)-alpha*(N32+N34)-K*z==F(info["numerator"],info["denominator"])==A-K*z
    print("CERTIFIED_ROW",lo,hi,A,K,info["states"],flush=True)
print("ALL 8 REAL PHASES CERTIFIED BY EXACT ENDPOINTS AND WITNESSES",len(vertices))
