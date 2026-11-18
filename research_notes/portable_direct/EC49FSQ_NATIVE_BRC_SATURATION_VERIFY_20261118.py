#!/usr/bin/env python3
"""EC49FSQ exact saturated-observer BRC cone verifier.

Default: exact Fraction evaluation of published complete-tree planes and all
12 observed high-discount anchor values.
--native-root PATH: additionally recompute unrestricted all-228-observer Bellman
on the 12 new anchors using the frozen original dataset/solver in PATH/code.
--independent: with --native-root, recheck the two identified anchors using the
second original 94-family reconstruction.
The continuum proof is the saturation lemma in the paired theorem, not the
finite anchor test.
"""
import argparse
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "EC49FSQ_NATIVE_BRC_SATURATION_MACHINE_CERT_20261118.json"
c = json.loads(CERT.read_text(encoding="utf-8"))
assert c["science"]["freeze_commit"] == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert (c["science"]["configurations"], c["science"]["named_profiles"],
        c["science"]["named_observers"]) == (310, 141, 228)

def tree_cost(t, a, b, z, orient):
    U, n32, n34, n140 = t
    if orient == "swapped":
        a, b = b, a
    return Q(U) - a * n32 - b * n34 - z * n140

def phase_cost(key, a, b, z, orient):
    section = c["regions"][key]
    tuples = section["swapped_tuples" if orient == "swapped" else "direct_tuples"]
    return min(tree_cost(t, a, b, z, orient) for t in tuples)

def check_region(k, a, b, z):
    R = c["regions"][k]
    assert Q(R["a"][0]) <= a <= Q(R["a"][1])
    if isinstance(R["b"], list):
        assert Q(R["b"][0]) <= b <= Q(R["b"][1])
    else:
        assert Q(R["b"]) == b
    assert Q(R["z"][0]) <= z <= Q(R["z"][1])
    for orient in ("direct", "swapped"):
        tuples = R["swapped_tuples" if orient == "swapped" else "direct_tuples"]
        # The discounted observation in this orientation has 141 path uses.
        assert all(t[2 if orient == "swapped" else 1] == 141 for t in tuples)
    return phase_cost(k,a,b,z,"direct"),phase_cost(k,a,b,z,"swapped")

# Structural and exact cost checks at all newly observed high-a anchors.
for point in c["primary_native_bellman_new_points"]:
    a,b,z = [Q(point[x]) for x in ("a","b","z")]
    key = "R3" if b == Q(7,16) else "R2" if z > Q(1,8) else "R1"
    d,s = check_region(key,a,b,z)
    pred = d if point["orientation"] == "direct" else s
    assert pred == Q(point["value"]), (point,pred)
    if key == "R1":
        gap = 6*z if 7*z <= 9*b-3 else 3-9*b+13*z
        assert d-s == gap

# Validate the exact polyhedral boundary in R1.
assert Q(9*Q(27,64)-3,7) == Q(51,448)
assert Q(3+7*Q(1,8),9) == Q(31,72)
assert phase_cost("R1",Q(1),Q(27,64),Q(51,448),"swapped") == \
       Q(306)-141-Q(27,64)*41-Q(51,448)*10

# The saturated ray itself is algebraic: every candidate plane in a region
# has -141*a. Evaluate a non-anchor rational pair as a cheap regression.
for k,b,z,a0 in [("R1",Q(28,64),Q(1,12),Q(31,64)),
                  ("R2",Q(27,64),Q(7,32),Q(31,64)),
                  ("R3",Q(7,16),Q(2,7),Q(1,2))]:
    for orient in ("direct","swapped"):
        v0 = phase_cost(k,a0,b,z,orient)
        v1 = phase_cost(k,Q(73,80),b,z,orient)
        assert v0-v1 == 141*(Q(73,80)-a0)
print("EC49FSQ_EXACT_SATURATION_PASS 3 regions, 12 high-a anchors, full rational phase regression")

p = argparse.ArgumentParser()
p.add_argument("--native-root", type=Path, default=None)
p.add_argument("--independent", action="store_true")
args = p.parse_args()
if args.independent and args.native_root is None:
    p.error("--independent requires --native-root")
if args.native_root is not None:
    sys.path.insert(0,str(args.native_root.resolve()/"code"))
    from EC49FSA_THREE_OBSERVER_SOLVER import solve, PIN
    assert PIN == c["science"]["freeze_commit"]
    for point in c["primary_native_bellman_new_points"]:
        a,b,z = [Q(point[x]) for x in ("a","b","z")]
        if point["orientation"] == "direct":
            disc = {32:a,34:b,140:z}
        else:
            disc = {32:b,34:a,140:z}
        out,_ = solve(disc,return_tree=False)
        v = Q(out["numerator"],out["denominator"])
        assert v == Q(point["value"]), (point,v)
        print("ALL228_BELLMAN_PASS",point["orientation"],str(b),str(z),str(v))
    if args.independent:
        from EC49FSA_FSB_INDEPENDENT_CHECK import certify
        rows = [row for row in c["primary_native_bellman_new_points"] if row["independent_raw94"]]
        assert len(rows)==2
        for row in rows:
            a,b,z = [Q(row[x]) for x in ("a","b","z")]
            disc = {32:b,34:a,140:z} if row["orientation"]=="swapped" else {32:a,34:b,140:z}
            out = certify(disc)
            assert Q(out["value"]) == Q(row["independent_raw94"]["value"])
            print("INDEPENDENT_94_FAMILY_PASS",row["orientation"],str(b),str(z),out["value"])
print("EC49FSQ_VERIFICATION_COMPLETE")
