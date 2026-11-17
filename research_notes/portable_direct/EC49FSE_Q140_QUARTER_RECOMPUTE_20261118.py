#!/usr/bin/env python3
"""EC49FSE exact complete-native q32=q34=1/4, q140=z discount.
Run inside the self-contained EC49FSE evidence bundle containing the
frozen EC49FSA_THREE_OBSERVER_SOLVER.py and EC49FSA_FSB_INDEPENDENT_CHECK.py.
This file reconstructs the four segments and independently checks endpoints.
"""
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
import json
from EC49FSA_THREE_OBSERVER_SOLVER import solve,V
from EC49FSA_FSB_INDEPENDENT_CHECK import certify

out=Path("ec49fse_quarter_runs");out.mkdir(exist_ok=True)
quarter=F(1,4)
witness_points=[F(1,14),F(21,94),F(59,226),F(1)]
segments=[(F(0),F(1,6),F(258),16),
          (F(1,6),F(1,4),F(260),28),
          (F(1,4),F(101,384),F(1057,4),45),
          (F(101,384),F(1),F(579,2),141)]
endpoint_values=[(F(0),F(258)),(F(1,6),F(766,3)),
                 (F(1,4),F(253)),(F(101,384),F(32309,128)),
                 (F(1),F(297,2))]
def witness(z):
    info,tree=solve({32:quarter,34:quarter,140:z})
    counts=Counter()
    for i in range(141):
        node=tree;visited=set()
        while "named_observer" in node:
            q=node["named_observer"]
            assert q not in visited
            visited.add(q);counts[q]+=1
            node=node["children"][str(V[q][i])]
        assert node=={"leaf":i}
    U=sum(counts.values())
    A=F(U)-(counts[32]+counts[34])*quarter
    K=counts[140]
    assert F(info["numerator"],info["denominator"])==A-K*z
    path=out/("anchor_%s_%s.json"%(z.numerator,z.denominator))
    path.write_text(json.dumps({"info":info,"tree":tree},
                               sort_keys=True,separators=(",",":"))+"\n")
    return A,K,info,counts
for point,(left,right,A,K) in zip(witness_points,segments):
    a,k,info,counts=witness(point)
    assert a==A and k==K,(point,a,k,A,K)
    print("WITNESS",str(point),str(A),K,info["root"],flush=True)
for z,expected in endpoint_values:
    first,tree=solve({32:quarter,34:quarter,140:z})
    actual=F(first["numerator"],first["denominator"])
    assert actual==expected
    independent=certify({32:quarter,34:quarter,140:z})
    assert F(independent["value"])==expected
    print("BOTH EXACT BELLMan",str(z),str(expected),flush=True)
for left,right,A,K in segments:
    def val(z):return A-K*z
    assert val(left)==dict(endpoint_values)[left]
    assert val(right)==dict(endpoint_values)[right]
print("CERTIFIED four exact real intervals; endpoints, 228 original observations, 141-state path witnesses")
