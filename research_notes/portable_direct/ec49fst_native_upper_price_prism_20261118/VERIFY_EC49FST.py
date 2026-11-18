#!/usr/bin/env python3
"""EC49FST exact native BRC16943 upper-prism recomputation.
Place original frozen EC49FSA_THREE_OBSERVER_SOLVER.py and its original
frozen source input directory on PYTHONPATH. No alias compression.
Run: python VERIFY_EC49FST.py
"""
from fractions import Fraction as Q
from pathlib import Path
from collections import Counter
import base64, hashlib, json, zlib
from EC49FSA_THREE_OBSERVER_SOLVER import solve, V, PIN

HERE=Path(__file__).resolve().parent
assert PIN=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert len(V)==228 and all(len(v)==141 for v in V)
cert=json.loads((HERE/"EXACT_CERTIFICATE.json").read_text())
wits=json.loads((HERE/"COMPLETE_JK_TREES.json").read_text())["witnesses"]
assert cert["frozen_science_pin"]==PIN
assert len(cert["primary_bellman_anchors"])==10

D=lambda a,b,z: Q(316)-141*a-43*b-30*z
H=lambda a,b,z: Q(315)-141*a-10*b-77*z
K=lambda a,b,z: Q(318)-141*a-10*b-82*z
J=lambda a,b,z: Q(324)-141*a-58*b-32*z
assert H(Q(2,3),Q(27,64),Q(3,5))==K(Q(2,3),Q(27,64),Q(3,5))

for row in cert["primary_bellman_anchors"]:
    a,b,z=map(Q,(row["a"],row["b"],row["z"]))
    orient=row["orientation"]
    discounts={32:a,34:b,140:z} if orient=="direct" else {32:b,34:a,140:z}
    info,tree=solve(discounts)
    observed=Q(info["numerator"],info["denominator"])
    expected=D(a,b,z) if orient=="direct" else min(H(a,b,z),K(a,b,z))
    assert observed==expected==Q(row["exact"]),(row,observed,expected)
    assert info["states"]==row["reached_subsets"]
    print("EXACT_228",orient,row["b"],row["z"],observed,info["states"],flush=True)

for name,expected in (("J",[324,141,58,32]),("K",[318,10,141,82])):
    w=wits[name]
    raw=zlib.decompress(base64.b64decode(w["packed_tree_base64_zlib"]))
    assert len(raw)==w["plain_bytes"]
    assert hashlib.sha256(raw).hexdigest()==w["plain_sha256"]
    obj=json.loads(raw)
    counts=Counter()
    for i in range(141):
        nd=obj; visited=set()
        while "named_observer" in nd:
            q=int(nd["named_observer"])
            assert 0<=q<228 and q not in visited
            visited.add(q); counts[q]+=1
            nd=nd["children"][str(V[q][i])]
        assert nd["leaf"]==i
    found=[sum(counts.values()),counts[32],counts[34],counts[140]]
    assert found==expected,(name,found,expected)
    print("FULL_141_TREE",name,found,flush=True)

a,b,z=Q(2,3),Q(29,64),Q(39,64)
info,tree=solve({32:a,34:b,140:z})
v=Q(info["numerator"],info["denominator"])
assert v==J(a,b,z)==Q(5895,32)
assert D(a,b,z)-v==Q(1,64)
assert D(a,Q(29,64),Q(77,128))==J(a,Q(29,64),Q(77,128))
assert D(a,Q(29,64),Q(1,2))-H(a,Q(29,64),Q(1,2))==Q(611,64)
assert D(a,Q(27,64),Q(77,128))-K(a,Q(27,64),Q(77,128))==Q(983,64)
print("EC49FST_EXACT_10_ANCHORS_2_NATIVE_TREES_AND_EDGE_PASS")
