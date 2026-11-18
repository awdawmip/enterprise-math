#!/usr/bin/env python3
"""EC49FSZ native-BRC16943 exact 3D-prism certificate checker.

Usage:
  python EC49FSZ_PRISM_RECHECK.py
  python EC49FSZ_PRISM_RECHECK.py --source-root /path/to/EC49FSZ_EVIDENCE --native --independent
The second form checks the original 228 named observers, all 20 Bellman vertices,
three actual full 141-profile decision trees, and two independent raw-family anchors.
"""
import argparse, hashlib, json, sys
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument("--cert", default=str(HERE / "EC49FSZ_NATIVE_3D_CERT.json"))
ap.add_argument("--source-root", default=str(HERE))
ap.add_argument("--native", action="store_true")
ap.add_argument("--independent", action="store_true")
args = ap.parse_args()
cert = json.loads(Path(args.cert).read_text())
source = Path(args.source_root)
assert cert["scientific_source_commit"] == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert cert["model"]["physical_observers"] == 228
assert cert["model"]["named_profiles"] == 141
a_lo, a_hi = map(Q, cert["region"]["a"])
b_lo, b_hi = map(Q, cert["region"]["b"])
z_lo, z_hi = map(Q, cert["region"]["z"])
assert (a_lo,a_hi,b_lo,b_hi,z_lo,z_hi) == (Q(1,2),Q(133,246),Q(7,16),Q(57,128),Q(1,2),Q(21,32))
def val(plane, p):
    a,b,z=p
    return Q(plane[0])-Q(plane[1])*a-Q(plane[2])*b-Q(plane[3])*z
def star(a,b):
    return (Q(4)+26*a-b)/32
def target(kind, p):
    return val(cert["direct_plane"],p) if kind=="D" else min(val(t,p) for t in cert["swapped_planes"])
V_D = set(product((a_lo,a_hi),(b_lo,b_hi),(z_lo,z_hi)))
V_S = V_D | {(a,b,star(a,b)) for a,b in product((a_lo,a_hi),(b_lo,b_hi))}
assert len(V_D)==8 and len(V_S)==12
assert all(z_lo<star(a,b)<z_hi for a,b in product((a_lo,a_hi),(b_lo,b_hi)))
for kind, target_vertices in (("D",V_D),("S",V_S)):
    data=cert["oracle_anchors"][kind]
    pts={tuple(map(Q, row[:3])) for row in data}
    assert pts==target_vertices and len(pts)==len(data)
    for row in data:
        p=tuple(map(Q,row[:3]))
        assert Q(row[3])==target(kind,p), (kind,p,row[3])
gaps=[target("D",p)-target("S",p) for p in V_S]
assert min(gaps)==Q(441,128) and max(gaps)==Q(161,16)
assert target("D",(a_hi,b_lo,z_lo))-val(["313","141","43","24"],(a_hi,b_lo,z_lo))==0
new_a=a_hi+Q(1,1024)
assert target("D",(new_a,b_lo,z_lo))-val(["313","141","43","24"],(new_a,b_lo,z_lo))==Q(123,1024)
print("PASS rational 3D vertices 8+12, exact plane values, moving interface, sharp gap and a-boundary")

if args.native or args.independent:
    for filename,expected in (("source/frozen_original_master.txt",cert["source_sha256"]["master"]),
                              ("source/EC49FPG_PROFILE.csv",cert["source_sha256"]["named_profiles"])):
        assert hashlib.sha256((source/filename).read_bytes()).hexdigest()==expected
    sys.path.insert(0,str(source))
    from native_code.EC49FQI_NATIVE_DATA import V,PIN
    assert PIN==cert["scientific_source_commit"] and len(V)==228
    for label,path,expected in (
      ("D", "trees/D.json",(319,18,75,141)),
      ("C", "trees/C.json",(323,12,89,141)),
      ("P", "trees/EC49FSAB_TREE_S_315_10_141_77.json",(315,10,141,77))):
        data=json.loads((source/path).read_text())
        tree=data.get("tree",data)
        counts=Counter()
        for i in range(141):
            node=tree
            seen=set()
            while "named_observer" in node:
                q=node["named_observer"]
                assert q not in seen and 0<=q<228
                seen.add(q); counts[q]+=1
                node=node["children"][str(V[q][i])]
            assert node=={"leaf":i}
        assert (sum(counts.values()),counts[32],counts[34],counts[140])==expected
        print("PASS native full tree",label,expected)

if args.native:
    from native_code.EC49FSA_THREE_OBSERVER_SOLVER import solve
    for kind in ("D","S"):
        for row in cert["oracle_anchors"][kind]:
            a,b,z=map(Q,row[:3])
            discount={32:a,34:b,140:z} if kind=="D" else {32:b,34:a,140:z}
            info,_=solve(discount,return_tree=False)
            got=Q(info["numerator"],info["denominator"])
            assert got==Q(row[3]),(kind,a,b,z,got,row[3])
            print("PASS exact native Bellman",kind,a,b,z,got,flush=True)

if args.independent:
    from native_code.EC49FSA_FSB_INDEPENDENT_CHECK import certify
    for row in cert["independent_raw_94_family"]:
        a,b,z=map(Q,(row["a"],row["b"],row["z"]))
        result=certify({32:b,34:a,140:z})
        assert Q(result["value"])==Q(row["value"])
        print("PASS independent raw-family oracle",a,b,z,row["value"],flush=True)
print("EC49FSZ_CERTIFICATE_PASS")
