#!/usr/bin/env python3
"""EC49FTC exact rational base polygon and native q140 saturation validator.
python EC49FTC_CHECK_VERTICAL_SATURATION_20261119.py
python EC49FTC_CHECK_VERTICAL_SATURATION_20261119.py --source-root /path/to/EC49FTA --full --independent
"""
from fractions import Fraction as Q
from pathlib import Path
from collections import Counter
import argparse, hashlib, json, sys

PIN="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
HERE=Path(__file__).resolve().parent
A=Q(133,246); B0=Q(7,16); B1=Q(57,128)
def top(b): return (Q(14)+b)/26
def zS(a,b): return (4+26*a-b)/32
def zD(a,b): return (3+123*a-32*b)/111
def D(a,b,z): return 319-18*a-75*b-141*z
def S(a,b,z): return 323-89*a-12*b-141*z
def GAP(a,b): return -4+71*a-63*b

def check_geometry():
    vertices=[(A,B0),(A,B1),(top(B0),B0),(top(B1),B1)]
    for a,b in vertices:
        assert A<=a<=top(b)
        assert Q(1,2)<zS(a,b)<=Q(9,16)
        assert zD(a,b)<zS(a,b)
        assert D(a,b,zS(a,b))-S(a,b,zS(a,b))==GAP(a,b)
    lo=min((GAP(a,b),a,b) for a,b in vertices)
    hi=max((GAP(a,b),a,b) for a,b in vertices)
    assert lo==(Q(99683,15744),A,B1),lo
    assert hi==(Q(3271,416),top(B0),B0),hi
    print("EXACT_BASE_POLYGON_PASS",lo,hi)

def read_anchors():
    data=json.loads((HERE/"EC49FTC_ZERO_PRICE_BELLMAN_20261119.json").read_text())
    assert data["frozen_source_pin"]==PIN and len(data["anchors"])==4
    for row in data["anchors"]:
        a,b,z=map(Q,[row["a"],row["b"],row["z"]])
        assert z==1 and A<=a<=top(b) and B0<=b<=B1
        val=D(a,b,z) if row["orientation"]=="D" else S(a,b,z)
        assert Q(row["value"])==val
        assert row["uses"]["q140"]==141
        assert Q(row["raw_integer"],row["denominator"])==val
    print("SAVED_BELLMAN_TOP_ANCHORS_PASS",len(data["anchors"]))
    return data["anchors"]

def check_native(root,rows,full=False,independent=False):
    root=Path(root).resolve()
    hashes={
        "source/frozen_original_master.txt":"cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e",
        "source/EC49FPG_PROFILE.csv":"a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f"
    }
    for name,digest in hashes.items():
        assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest
    sys.path.insert(0,str(root))
    from native_code.EC49FQI_NATIVE_DATA import PIN as sourcepin,V
    assert sourcepin==PIN and len(V)==228 and all(len(obs)==141 for obs in V)
    for filename,expected in [
        ("D1_319_18_75_141.json",(319,18,75,141)),
        ("S_C_323_89_12_141.json",(323,12,89,141))
    ]:
        data=json.loads((root/"trees"/filename).read_text())
        tree=data.get("tree",data);counts=Counter()
        for i in range(141):
            node=tree;seen=set()
            while "named_observer" in node:
                q=node["named_observer"]
                assert 0<=q<228 and q not in seen
                seen.add(q);counts[q]+=1
                node=node["children"][str(V[q][i])]
            assert node=={"leaf":i}
        got=(sum(counts.values()),counts[32],counts[34],counts[140])
        assert got==expected,(filename,got)
        print("NATIVE_TREE_REPLAY_PASS",filename,got)
    if full:
        from native_code.EC49FSA_THREE_OBSERVER_SOLVER import solve
        for row in rows:
            a,b,z=map(Q,[row["a"],row["b"],row["z"]])
            disc={32:a,34:b,140:z} if row["orientation"]=="D" else {32:b,34:a,140:z}
            info,_=solve(disc,return_tree=False)
            assert Q(info["numerator"],info["denominator"])==Q(row["value"])
            print("FRESH_UNRESTRICTED_NATIVE_BELLMAN_PASS",row["orientation"],a,b,z)
    if independent:
        from native_code.EC49FSA_FSB_INDEPENDENT_CHECK import certify
        for row in rows[:2]:
            a,b,z=map(Q,[row["a"],row["b"],row["z"]])
            disc={32:a,34:b,140:z} if row["orientation"]=="D" else {32:b,34:a,140:z}
            assert Q(certify(disc)["value"])==Q(row["value"])
            print("INDEPENDENT_RAW94_NATIVE_BELLMAN_PASS",row["orientation"])

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--source-root",type=Path)
    parser.add_argument("--full",action="store_true")
    parser.add_argument("--independent",action="store_true")
    args=parser.parse_args()
    check_geometry(); rows=read_anchors()
    if args.source_root:
        check_native(args.source_root,rows,args.full,args.independent)
    else:
        assert not args.full and not args.independent
    print("EC49FTC_CHECK_COMPLETE")
