#!/usr/bin/env python3
"""EC49FTD exact rational 3D native-price theorem reproducer.

python VERIFY.py                        # exact rational geometry and saved values
python VERIFY.py --source-root PATH     # 12 fresh exhaustive original 228-observer Bellman checks
python VERIFY.py --source-root PATH --trees --independent

PATH: extracted EC49FTA evidence directory with source/ and native_code/ from
the 2026-11-19 self-contained EC49FTD / inherited EC49FTA evidence bundle.
This checker does not modify the canonical frozen scientific input.
"""
import argparse, hashlib, json, sys
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
HERE=Path(__file__).resolve().parent
CERT=json.loads((HERE/"EXACT_EVIDENCE.json").read_text())
PIN="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
A=(Q(2,3),Q(3,4));B=(Q(7,16),Q(57,128));Z=Q(49,64)

def D(a,b,z):
    return min(319-18*a-75*b-141*z,326-32*a-68*b-141*z)
def S(a,b,z):
    return min(327-97*a-9*b-141*z,325-92*a-12*b-141*z)
def vertices():
    corners={(a,b) for a in A for b in B}
    d=corners|{((1+b)/2,b) for b in B}
    s=corners|{(Q(2,3),Q(4,9)),(Q(427,640),Q(57,128))}
    return d,s
def check_certificate():
    assert CERT["frozen_source_commit"]==PIN
    assert CERT["box"]=={"a":["2/3","3/4"],"b":["7/16","57/128"],"z":["49/64","1"]}
    d,s=vertices()
    observed={"D":set(),"S":set()}
    for orientation,aa,bb,value in CERT["anchors"]:
        a,b=Q(aa),Q(bb)
        assert a in [x for x,y in (d if orientation=="D" else s) if y==b]
        assert Q(value)==(D(a,b,Z) if orientation=="D" else S(a,b,Z))
        observed[orientation].add((a,b))
    assert observed["D"]==d and observed["S"]==s
    allpoints=d|s
    gaps=[(D(a,b,Z)-S(a,b,Z),a,b) for a,b in allpoints]
    assert len(allpoints)==8
    assert min(gaps)==(Q(5867,384),Q(2,3),Q(57,128))
    assert max(gaps)==(Q(351,16),Q(3,4),Q(7,16))
    a,b=Q(3,4),Q(7,16)
    for z in (Q(3,4),Q(49,64),Q(1)):
        challenger=332-141*a-8*b-105*z
        saturated=327-97*a-9*b-141*z
        assert challenger-saturated==36*(z-Q(49,64))
    assert 332-141*a-8*b-105*Q(3,4)==144
    print("EC49FTD_RATIONAL_GEOMETRY_AND_12_SAVED_ANCHORS_PASS",flush=True)

def native_checks(root,trees,independent):
    root=Path(root).resolve()
    for fname,sha in CERT["source_sha256"].items():
        assert hashlib.sha256((root/"source"/fname).read_bytes()).hexdigest()==sha
    sys.path.insert(0,str(root/"native_code"))
    from EC49FSA_THREE_OBSERVER_SOLVER import solve,V,PIN as original_pin
    assert original_pin==PIN
    assert len(V)==228 and all(len(v)==141 for v in V)
    for ori,aa,bb,value in CERT["anchors"]:
        a,b=Q(aa),Q(bb)
        discount={32:a,34:b,140:Z} if ori=="D" else {32:b,34:a,140:Z}
        info,_=solve(discount,return_tree=False)
        assert Q(info["numerator"],info["denominator"])==Q(value), (ori,aa,bb,info)
        print("EXACT_ALL228_BELLMAN_PASS",ori,aa,bb,value,flush=True)
    if independent:
        from EC49FSA_FSB_INDEPENDENT_CHECK import certify
        for item in CERT["independent_raw94"]:
            a,b,z=map(Q,(item["a"],item["b"],item["z"]))
            ori=item["orientation"]
            discount={32:a,34:b,140:z} if ori=="D" else {32:b,34:a,140:z}
            val=certify(discount)
            assert Q(val["value"])==Q(item["result"])
            print("INDEPENDENT_RAW94_BELLMAN_PASS",ori,a,b,z,flush=True)
    if trees:
        witness_cases=[
            ("D1","D",Q(2,3),Q(7,16)),
            ("D2","D",Q(3,4),Q(7,16)),
            ("SQ","S",Q(3,4),Q(7,16)),
            ("SR","S",Q(2,3),Q(57,128))]
        for name,ori,a,b in witness_cases:
            discount={32:a,34:b,140:Q(1)} if ori=="D" else {32:b,34:a,140:Q(1)}
            info,tree=solve(discount)
            count=Counter()
            for i in range(141):
                node=tree
                used=set()
                while "named_observer" in node:
                    q=node["named_observer"]
                    assert q not in used and 0<=q<228
                    used.add(q); count[q]+=1
                    node=node["children"][str(V[q][i])]
                assert node=={"leaf":i}
            got=[sum(count.values()),count[32],count[34],count[140]]
            assert got==CERT["witness_tuples"][name],(name,got)
            payload=(json.dumps(tree,sort_keys=True,ensure_ascii=False,
                      separators=(",",":"))+"\n").encode()
            assert hashlib.sha256(payload).hexdigest()==CERT["witness_tree_sha256"][name]
            print("ORIGINAL_INDEX_141_PROFILE_TREE_PASS",name,got,flush=True)
        # A fifth actual non-saturated challenger is reproduced at the lower-price face.
        info,tree=solve({32:Q(7,16),34:Q(3,4),140:Q(3,4)})
        assert [info["U"],info["uses"]["32"],info["uses"]["34"],info["uses"]["140"]]==[332,8,141,105]
        assert Q(info["numerator"],info["denominator"])==Q(144)
        print("STRICT_COUNTEREXAMPLE_NATIVE_TREE_PASS",flush=True)
    print("EC49FTD_NATIVE_VERIFICATION_COMPLETE",flush=True)

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--source-root",type=Path)
    ap.add_argument("--trees",action="store_true")
    ap.add_argument("--independent",action="store_true")
    args=ap.parse_args()
    check_certificate()
    if args.source_root:
        native_checks(args.source_root,args.trees,args.independent)
    else:
        assert not args.trees and not args.independent
