#!/usr/bin/env python3
"""Exact rational EC49FTE certificate and optional full native solver verification.

Default: python VERIFY.py
Fresh original-input Bellman + two independently decoded samples:
    python VERIFY.py --source-root /path/to/extracted/EC49FTE_SHARP_MIDDLE_SATURATION_BRIDGE_20261119 --full --independent --trees
The source-root directory must contain native_code/, source/, and trees/.
"""
import argparse, hashlib, json, sys
from pathlib import Path
from fractions import Fraction as Q

HERE = Path(__file__).resolve().parent
CERT = json.loads((HERE / "EXACT_CERT.json").read_text())
Z = Q("1709/2080")
AL = (Q("3/4"), Q("4/5"))
BL = (Q("7/16"), Q("57/128"))
PIN = "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"

def D(a, b, z):
    return min(329 - 36*a - 68*b - 141*z, 333 - 40*a - 70*b - 141*z)

def S(a, b, z):
    return 333 - 105*a - 9*b - 141*z

def geometry():
    assert CERT["frozen_source_commit"] == PIN
    dv = {(a,b) for a in AL for b in BL} | {(1-b/2,b) for b in BL}
    sv = {(a,b) for a in AL for b in BL}
    found = {"D":set(), "S":set()}
    for row in CERT["anchors"]:
        ori, a, b, z = row["orientation"],Q(row["a"]),Q(row["b"]),Q(row["z"])
        assert z == Z and (a,b) in (dv if ori == "D" else sv)
        assert Q(row["optimum"]) == (D(a,b,z) if ori == "D" else S(a,b,z))
        found[ori].add((a,b))
    assert len(CERT["anchors"]) == 10 and found == {"D":dv,"S":sv}
    gaps = [D(a,b,Z)-S(a,b,Z) for a,b in dv | sv]
    assert min(gaps) == Q("2749/128") and max(gaps) == Q("405/16")
    a,b=Q("4/5"),Q("7/16")
    for z in (Q("13/16"),Z,Q(1)):
        challenger = 340-141*a-8*b-115*z
        assert challenger-S(a,b,z) == 26*(z-Z)
    print("EC49FTE_EXACT_GEOMETRY_AND_10_SAVED_ANCHORS_PASS",flush=True)

def native(root,full,independent,trees):
    root=Path(root).resolve()
    for name,sha in CERT["frozen_raw_sha256"].items():
        assert hashlib.sha256((root/"source"/name).read_bytes()).hexdigest()==sha
    sys.path.insert(0,str(root/"native_code"))
    from EC49FSA_THREE_OBSERVER_SOLVER import V,PIN as source_pin,solve
    assert source_pin == PIN and len(V)==228 and all(len(v)==141 for v in V)
    if full:
        for r in CERT["anchors"]:
            ori,a,b,z=r["orientation"],Q(r["a"]),Q(r["b"]),Q(r["z"])
            discounts={32:a,34:b,140:z} if ori=="D" else {32:b,34:a,140:z}
            info,_=solve(discounts,return_tree=False)
            assert Q(info["numerator"],info["denominator"]) == Q(r["optimum"])
            print("EXACT_ALL228_BELLMAN_PASS",ori,a,b,r["optimum"],flush=True)
    if independent:
        from EC49FSA_FSB_INDEPENDENT_CHECK import certify
        for r in CERT["independent_raw94"]:
            ori,a,b,z=r["orientation"],Q(r["a"]),Q(r["b"]),Q(r["z"])
            discounts={32:a,34:b,140:z} if ori=="D" else {32:b,34:a,140:z}
            x=certify(discounts)
            assert Q(x["value"])==Q(r["optimum"])
            print("INDEPENDENT_RAW94_PASS",ori,a,b,r["optimum"],flush=True)
    if trees:
        from collections import Counter
        for r in CERT["witness_trees"]:
            name=r["name"]
            p=root/"trees"/(name+".json")
            data=p.read_bytes()
            assert hashlib.sha256(data).hexdigest()==r["sha256"]
            t=json.loads(data);cnt=Counter()
            for i in range(141):
                node=t;used=set()
                while "named_observer" in node:
                    q=node["named_observer"]
                    assert 0 <= q < 228 and q not in used
                    used.add(q);cnt[q]+=1
                    node=node["children"][str(V[q][i])]
                assert node=={"leaf":i}
            assert [sum(cnt.values()),cnt[32],cnt[34],cnt[140]]==r["counts"]
            print("ORIGINAL_141_PROFILE_TREE_PASS",name,r["counts"],flush=True)
    print("EC49FTE_ORIGINAL_SOURCE_VERIFIED",flush=True)

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--source-root",type=Path)
    ap.add_argument("--full",action="store_true")
    ap.add_argument("--independent",action="store_true")
    ap.add_argument("--trees",action="store_true")
    args=ap.parse_args()
    geometry()
    if args.source_root:
        native(args.source_root,args.full,args.independent,args.trees)
    else:
        assert not (args.full or args.independent or args.trees), "--source-root required for native checks"
