#!/usr/bin/env python3
"""EC49FSP exact 2D native BRC discount-wedge reproduction.

Default: exact rational validation of complete published polygon certificate.
--native-root DIR: additionally compute unrestricted native all-228-observer
Bellman for all six vertices, using frozen original BRC inputs in DIR/code.
--independent: separately rebuild raw-family named observations and recompute
the six new top-edge point values, using the alternate original decoder.

Mathematical status: complete tree+Bellman vertex proof for the declared
two-parameter rectangle, not a physical-time/heartbeat model.
"""
import argparse
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"EC49FSP_TWO_PARAMETER_SWAP_WEDGE_MACHINE_CERT_20261118.json"
c=json.loads(CERT.read_text())
assert c["science"]["source_pin"]=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
a=Q(31,64); b0=Q(27,64); b1=Q(29,64); zmax=Q(1,8)
def cost(t,b,z):
    U,n32,n34,n140=t
    return Q(U)-a*Q(n32)-b*Q(n34)-z*Q(n140)
T=c["complete_trees"]
def predicted(b,z):
    d=cost(T[0]["tuple"],b,z)
    # For orientation swapped, observation q32 receives b,
    # q34 receives a. cost U-b*N32-a*N34-z*N140.
    s=min(Q(t["tuple"][0])-b*t["tuple"][1]-a*t["tuple"][2]-z*t["tuple"][3]
          for t in T[1:])
    return d,s
for v in c["exact_full228_bellman_polygon_vertices"]:
    b,z=Q(v["b"]),Q(v["z"])
    assert predicted(b,z)==(Q(v["direct"]),Q(v["swapped"]))
    direct,swapped=predicted(b,z)
    expected = 6*z if 7*z<=9*b-3 else 3-9*b+13*z
    assert direct-swapped==expected
assert Q(9*b0-3,7)==Q(51,448)
assert Q(3+7*zmax,9)==Q(31,72)
print("EXACT_RATIONAL_WEDGE_PASS 6 vertices, 2 polygonal regions")

p=argparse.ArgumentParser()
p.add_argument("--native-root",type=Path)
p.add_argument("--independent",action="store_true")
args=p.parse_args()
if args.independent and not args.native_root:
    p.error("--independent requires --native-root")
if args.native_root:
    sys.path.insert(0,str(args.native_root.resolve()/"code"))
    from EC49FSA_THREE_OBSERVER_SOLVER import solve, PIN
    assert PIN==c["science"]["source_pin"]
    for v in c["exact_full228_bellman_polygon_vertices"]:
        b,z=Q(v["b"]),Q(v["z"])
        for orient in ("direct","swapped"):
            discounts={32:a,34:b,140:z} if orient=="direct" else {32:b,34:a,140:z}
            out,_=solve(discounts,return_tree=False)
            value=Q(out["numerator"],out["denominator"])
            assert value==Q(v[orient]),(v,orient,value)
            print("ALL228_BELLMAN_PASS",orient,str(b),str(z),str(value))
    if args.independent:
        from EC49FSA_FSB_INDEPENDENT_CHECK import certify
        for v in c["independent_94_family_decoder"]:
            b,z=Q(v["b"]),Q(v["z"])
            discounts={32:a,34:b,140:z} if v["orientation"]=="direct" else {32:b,34:a,140:z}
            x=certify(discounts)
            assert Q(x["value"])==Q(v["value"])
            print("INDEPENDENT_RAW_FAMILY_PASS",v["orientation"],str(b),str(z))
print("EC49FSP_WEDGE_CERTIFICATE_DONE")
