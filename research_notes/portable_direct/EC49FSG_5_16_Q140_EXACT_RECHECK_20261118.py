#!/usr/bin/env python3
"""EC49FSG: native q140 z in [0,1] at joint q32/q34 discount 5/16.
Run in original self-contained BRC evidence directory containing
EC49FSA_THREE_OBSERVER_SOLVER.py, EC49FSA_FSB_INDEPENDENT_CHECK.py
and their preserved native original-profile/raw data files.
"""
from fractions import Fraction as F
from collections import Counter
from EC49FSA_THREE_OBSERVER_SOLVER import solve, V, PIN
from EC49FSA_FSB_INDEPENDENT_CHECK import certify
assert PIN=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
alpha=F(5,16)
rows=[
("0","1/16","993/4",13,297,15,141,34),
("1/16","1/12","1987/8",15,299,21,141,34),
("1/12","1/6","1989/8",18,298,17,141,34),
("1/6","7/32","2005/8",30,300,17,141,34),
("7/32","5/16","4017/16",32,302,22,141,34),
("5/16","479/1456","4107/16",50,302,4,141,34),
("479/1456","1","2293/8",141,301,7,39,140)]
vertices=sorted({F(s) for row in rows for s in row[:2]})
def value_at(z):
    info, _=solve({32:alpha,34:alpha,140:z})
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
        node=tree;used=set()
        while "named_observer" in node:
            q=node["named_observer"]
            assert q not in used
            used.add(q);counts[q]+=1
            node=node["children"][str(V[q][i])]
        assert node=={"leaf":i}
    assert (sum(counts.values()),counts[32],counts[34],counts[140],info["root"])==(U,N32,N34,K,root)
    assert F(U)-alpha*(N32+N34)-K*z==F(info["numerator"],info["denominator"])==A-K*z
    print("CERTIFIED",lo,hi,A,K,info["states"],flush=True)
print("ALL SEVEN REAL PHASES CERTIFIED",len(vertices))
