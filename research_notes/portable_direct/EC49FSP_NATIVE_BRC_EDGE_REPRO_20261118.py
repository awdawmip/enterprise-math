#!/usr/bin/env python3
"""Exact EC49FSP price-swap corner checker.

Without --native-root: check every rational phase equation, all published
certificate endpoints and named-tree cost counts. This does NOT independently
establish global Bellman optimality.
With --native-root DIR: additionally replay every complete native tree and
recompute every envelope vertex with the frozen 228-observer exact solver.
Use --independent to check all native endpoints with the separate raw-family
decoder (both source implementations are in the self-contained evidence archive).
"""
import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "EC49FSP_NATIVE_BRC_PRICE_SWAP_CORNER_MACHINE_CERT_20261118.json"
p = argparse.ArgumentParser()
p.add_argument("--native-root", type=Path)
p.add_argument("--independent", action="store_true")
args = p.parse_args()
c = json.loads(CERT.read_text())
assert c["frozen_science_pin"] == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"

def cost(v, a, b, z):
    U,n32,n34,n140 = map(F,v)
    return U-a*n32-b*n34-z*n140

def phase_value(orientation,z):
    record = c["orientations"][orientation]
    a,b=F(record["a"]),F(record["b"])
    lines = c["phases"][orientation]
    found=[]
    for row in lines:
        lo,hi=map(F,row["interval"])
        if lo <= z <= hi:
            intercept,slope = F(row["intercept"]),F(row["z_slope"])
            observed = cost(row["witness"],a,b,z)
            assert intercept+slope*z == observed
            found.append(observed)
    assert len(found) >= 1 and len(set(found))==1,(orientation,z,found)
    return found[0]

for orientation in ("direct","swapped"):
    phases=c["phases"][orientation]
    assert F(phases[0]["interval"][0])==0
    assert F(phases[-1]["interval"][1])==F(1,4)
    for left,right in zip(phases,phases[1:]):
        x=F(left["interval"][1])
        assert x==F(right["interval"][0])
        assert phase_value(orientation,x)==cost(right["witness"],
              F(c["orientations"][orientation]["a"]),
              F(c["orientations"][orientation]["b"]),x)
for row in c["bellman_all228_vertices"]:
    z=F(row["z"])
    assert phase_value("direct",z)==F(row["direct"])
    assert phase_value("swapped",z)==F(row["swapped"])
    assert phase_value("direct",z)-phase_value("swapped",z)==F(row["difference"])
assert phase_value("direct",F(1,4))-phase_value("swapped",F(1,4))==F(193,64)
print("RATIONAL_CERT_PASS",len(c["bellman_all228_vertices"]),"vertices")

if args.native_root:
    root=args.native_root.resolve()
    sys.path.insert(0,str(root/"code"))
    from EC49FSA_THREE_OBSERVER_SOLVER import solve,V,PIN
    assert PIN==c["frozen_science_pin"]
    for orientation, rows in c["phases"].items():
        for row in rows:
            tuple_str="_".join(str(u) for u in row["witness"])
            path=root/"EC49FSP_EDGE"/orientation/("tree_"+tuple_str+".json")
            text=path.read_text().strip()
            assert hashlib.sha256(text.encode()).hexdigest()==row["tree_sha256"]
            tree=json.loads(text)
            counts=[0]*228
            for s in range(141):
                node=tree; seen=set()
                while "named_observer" in node:
                    q=node["named_observer"]
                    assert 0<=q<228 and q not in seen
                    seen.add(q); counts[q]+=1
                    node=node["children"][str(V[q][s])]
                assert node=={"leaf":s}
            assert (sum(counts),counts[32],counts[34],counts[140])==tuple(row["witness"])
    print("ALL_NATIVE_TREE_REPLAYS_PASS",6,"witness classes; 141 profiles each")
    for orientation in ("direct","swapped"):
        a=F(c["orientations"][orientation]["a"])
        b=F(c["orientations"][orientation]["b"])
        zs=sorted({F(x) for row in c["phases"][orientation] for x in row["interval"]})
        for z in zs:
            info,_=solve({32:a,34:b,140:z})
            actual=F(info["numerator"],info["denominator"])
            assert actual==phase_value(orientation,z), (orientation,z,actual)
            print("PRIMARY_ALL228_PASS",orientation,str(z),str(actual))
    if args.independent:
        from EC49FSA_FSB_INDEPENDENT_CHECK import certify
        for row in c["independent_decoder_checks"]:
            orient=row["orientation"]
            a=F(c["orientations"][orient]["a"])
            b=F(c["orientations"][orient]["b"])
            z=F(row["z"])
            got=certify({32:a,34:b,140:z})
            assert F(got["value"])==F(row["value"])
            print("INDEPENDENT_RAW228_PASS",orient,str(z),got["value"])
print("CERTIFICATE_CHECK_COMPLETE")
