#!/usr/bin/env python3
"""EC49FTB exact rational 3D fan checker.

Pure rational geometry:
  python EC49FTB_CHECK.py

With frozen native 228-observer input and solver from the EC49FTA evidence bundle:
  python EC49FTB_CHECK.py --source-root /path/to/EC49FTA --replay --full --independent

The primary certificate's 20 values were computed at creation; --full
recalculates the exact all-observer Bellman value instead of trusting that record.
"""
import argparse
import hashlib
import json
import sys
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
A=(Q(31,32),Q(1))
B=(Q(7,16),Q(57,128))
Z=(Q(15,16),Q(1))
D0=(Q(348),-Q(141),-Q(44),-Q(72))
D1=(Q(367),-Q(91),-Q(44),-Q(141))
S0=(Q(340),-Q(141),-Q(8),-Q(115))
S1=(Q(343),-Q(118),-Q(8),-Q(141))
SD=tuple(i-j for i,j in zip(D1,D0))
SS=tuple(i-j for i,j in zip(S1,S0))
FACES=[(-v,Q(1),Q(0),Q(0)) for v in A]
FACES += [(-v,Q(0),Q(1),Q(0)) for v in B]
FACES += [(-v,Q(0),Q(0),Q(1)) for v in Z]

def det(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))

def intersection(rows):
    m=[v[1:] for v in rows]
    d=det(m)
    if not d:
        return None
    rhs=[-v[0] for v in rows]
    return tuple(det([[rhs[i] if j==k else m[i][j]
                       for j in range(3)] for i in range(3)])/d
                 for k in range(3))

def vertices(switches):
    found=set()
    for triple in combinations(FACES+list(switches),3):
        x=intersection(triple)
        if x is not None and all(lo <= t <= hi
                for t,(lo,hi) in zip(x,(A,B,Z))):
            found.add(x)
    return sorted(found)

def plane(p,x):
    return p[0]+sum(i*j for i,j in zip(p[1:],x))

def cost(orientation,x):
    pair=(D0,D1) if orientation=="D" else (S0,S1)
    return min(plane(p,x) for p in pair)

def as_point(r):
    return tuple(Q(v) for v in r["point"])

def verify_geometry(cert):
    assert cert["frozen_source_commit"]=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
    assert SD==(Q(19),Q(50),Q(0),-Q(69))
    assert SS==(Q(3),Q(23),Q(0),-Q(26))
    for orientation, switch in (("D",SD),("S",SS)):
        expected=set(vertices([switch]))
        rows=cert[orientation]
        assert len(expected)==len(rows)==10
        assert set(as_point(r) for r in rows)==expected
        for r in rows:
            assert Q(r["exact_bellman"])==cost(orientation,as_point(r))
        print("SAVED_RATIONAL_ANCHORS_MATCH_PLANES",orientation,len(rows))
    joint=vertices([SD,SS])
    assert len(joint)==12
    vals=[(cost("D",x)-cost("S",x),x) for x in joint]
    assert min(vals)==(Q(1033,32),(Q(31,32),Q(57,128),Q(15,16)))
    assert max(vals)==(Q(141,4),(Q(1),Q(7,16),Q(1)))
    print("JOINT_GEOMETRY_SHARP_GAP_EXACT",len(joint),min(vals),max(vals))
    return True

def native(orientation,x):
    a,b,z=x
    return ({32:a,34:b,140:z} if orientation=="D"
            else {32:b,34:a,140:z})

def verify_native(cert,source,full=False,replay=False,independent=False):
    assert source is not None
    m=source/"source"/"frozen_original_master.txt"
    p=source/"source"/"EC49FPG_PROFILE.csv"
    for f,h in ((m,"cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"),
                (p,"a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f")):
        assert hashlib.sha256(f.read_bytes()).hexdigest()==h
    sys.path.insert(0,str(source/"native_code"))
    from EC49FQI_NATIVE_DATA import V,PIN
    from EC49FSA_THREE_OBSERVER_SOLVER import solve
    assert PIN==cert["frozen_source_commit"]
    assert len(V)==228 and all(len(row)==141 for row in V)
    if replay:
        cases=(("D0","D",(Q(1),Q(7,16),Q(15,16))),
               ("D1","D",(Q(31,32),Q(7,16),Q(1))),
               ("S0","S",(Q(1),Q(7,16),Q(15,16))),
               ("S1","S",(Q(31,32),Q(7,16),Q(1))))
        for name,ori,x in cases:
            info,tree=solve(native(ori,x))
            counts=Counter()
            for i in range(141):
                node=tree
                seen=set()
                while "named_observer" in node:
                    q=node["named_observer"]
                    assert 0<=q<228 and q not in seen
                    seen.add(q)
                    counts[q]+=1
                    node=node["children"][str(V[q][i])]
                assert node=={"leaf":i}
            got=[sum(counts.values()),counts[32],counts[34],counts[140]]
            assert got==cert["witness_uses"][name],(name,got)
            assert Q(info["numerator"],info["denominator"])==cost(ori,x)
            print("NATIVE_WITNESS_141_PATHS_PASS",name,got,flush=True)
    if full:
        for ori in ("D","S"):
            for i,row in enumerate(cert[ori],1):
                x=as_point(row)
                info,_=solve(native(ori,x),return_tree=False)
                assert Q(info["numerator"],info["denominator"])==Q(row["exact_bellman"])
                print("FRESH_ALL228_BELLMAN_PASS",ori,i,flush=True)
    if independent:
        from EC49FSA_FSB_INDEPENDENT_CHECK import certify
        for r in cert["independent_raw94_anchors"]:
            ori=r["orientation"]
            x=as_point(r)
            assert Q(certify(native(ori,x))["value"])==Q(r["result"])
            print("RAW94_INDEPENDENT_RECALCULATION_PASS",ori,flush=True)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--source-root",type=Path)
    parser.add_argument("--replay",action="store_true")
    parser.add_argument("--full",action="store_true")
    parser.add_argument("--independent",action="store_true")
    args=parser.parse_args()
    data=json.loads((HERE/"EC49FTB_EXACT_20_BELLMAN_ANCHORS_20261119.json").read_text())
    verify_geometry(data)
    if args.replay or args.full or args.independent:
        verify_native(data,args.source_root,full=args.full,
                      replay=args.replay,independent=args.independent)
    print("EC49FTB_CHECK_COMPLETE")
