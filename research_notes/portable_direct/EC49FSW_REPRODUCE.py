#!/usr/bin/env python3
"""EC49FSW reproducibility: run from unpacked full evidence archive (native_code/ and source/ present).
Unrestricted exact Fraction Bellman, all 228 physically named observations, 141 profiles."""
from fractions import Fraction as Q
from native_code.EC49FSA_THREE_OBSERVER_SOLVER import solve
from native_code.EC49FSA_FSB_INDEPENDENT_CHECK import certify
from native_code.EC49FQI_NATIVE_DATA import V,PIN
from collections import Counter
import json
assert PIN == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab" and len(V)==228
A=Q(2,3)
B=(Q(7,16),Q(4,9),Q(57,128))
Z=(Q(1531,2304),Q(1))
def desired(o,b,z):
    direct=307-75*b-141*z
    swapped=min(Q(787,3)-9*b-141*z,Q(791,3)-12*b-141*z)
    return direct if o=="D" else swapped
def discounts(o,b,z):
    return {32:A,34:b,140:z} if o=="D" else {32:b,34:A,140:z}
# Full-tree replay at all 141 named states, exact physical q indexes.
for name,vec in [("D_7_16",(319,18,75,141)),
                 ("S_7_16",(327,9,97,141)),
                 ("S_57_128",(325,12,92,141))]:
    tree=json.load(open("trees/"+name+".json"))
    used=Counter()
    for i in range(141):
        node=tree;seen=set()
        while "named_observer" in node:
            q=node["named_observer"]
            assert 0<=q<228 and q not in seen
            seen.add(q);used[q]+=1
            node=node["children"][str(V[q][i])]
        assert node == {"leaf":i}
    assert (sum(used.values()),used[32],used[34],used[140]) == vec
    print("TREE_CHECKED",name,vec,flush=True)
# Twelve Bellman vertices. No partition collapsing; 228 candidate physical queries.
for o in ("D","S"):
    for b in B:
        for z in Z:
            i,_=solve(discounts(o,b,z))
            actual=Q(i["numerator"],i["denominator"])
            assert actual==desired(o,b,z),(o,b,z,actual,desired(o,b,z))
            print("EXACT_BELLMAN",o,b,z,actual,"states",i["states"],flush=True)
# Run independently in a fresh process if checking every point; the distinct
# original-94-family decoder can consume substantial memory if repeated after the
# native all-vertex sweep. Three original independent checks were performed separately
# and preserved in INDEPENDENT_3.log (no self-certification implied).
print("PRIMARY_12_AND_ALL_COMPLETE_TREE_REPLAYS_PASSED")
