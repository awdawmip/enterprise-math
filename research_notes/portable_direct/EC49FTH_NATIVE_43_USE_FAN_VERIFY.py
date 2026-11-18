#!/usr/bin/env python3
"""EC49FTH exact BRC16943 3-price fan verification.

Run this file beside EC49FTH_NATIVE_43_USE_FAN_CERT.json and optionally provide
--bundle-root pointing to the self-contained EC49FTH evidence folder.

  python EC49FTH_VERIFY.py
  python EC49FTH_VERIFY.py --bundle-root /path/to/EC49FTH... --full --independent

The geometry requires only stdlib. --full uses the preserved frozen 228-query
original-index Bellman solver; --independent uses the raw94 reconstruction.
"""
import argparse
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from collections import Counter

D = {"Dmid":(329,-36,-68,-141),"D45":(334,-141,-62,-45),
     "D43":(326,-141,-47,-43)}
S = {"S105":(332,-141,-8,-105)}

def dot(v,p):
    return F(v[0]) + sum(F(v[i+1])*p[i] for i in range(3))

def sub(v,w):
    return tuple(F(x)-F(y) for x,y in zip(v,w))

def det(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))

def vertices(constraints):
    points=set()
    for triple in combinations(constraints,3):
        matrix=[row[1:] for row in triple]
        denom=det(matrix)
        if not denom: continue
        rhs=[-row[0] for row in triple]
        p=tuple(det([[rhs[i] if j==k else matrix[i][j]
                      for j in range(3)] for i in range(3)])/denom
                for k in range(3))
        if all(dot(row,p)>=0 for row in constraints):
            points.add(p)
    return sorted(points)

def anchors(cert):
    dom=cert["domain"]
    (a0,a1),(b0,b1),(z0,z1)=[
        tuple(map(F,dom[x])) for x in ("a","b","z")]
    box=[(-a0,1,0,0),(a1,-1,0,0),
         (-b0,0,1,0),(b1,0,-1,0),
         (-z0,0,0,1),(z1,0,0,-1)]
    dpts=set()
    gaps=[]
    for name,vec in D.items():
        cell=vertices(box+[sub(other,vec)
                           for key,other in D.items() if key!=name])
        assert len(cell)==cert["D_cell_vertex_counts"][name]
        for p in cell:
            assert dot(vec,p)==min(dot(v,p) for v in D.values())
            dpts.add(p)
            gaps.append(dot(vec,p)-dot(S["S105"],p))
    assert len(dpts)==16
    assert min(gaps)==F(cert["gap"]["min"]["value"])
    assert max(gaps)==F(cert["gap"]["max"]["value"])
    samples=(
        [("D",p,min(dot(v,p) for v in D.values())) for p in sorted(dpts)]
        +[("S",p,dot(S["S105"],p)) for p in vertices(box)]
    )
    assert len(samples)==24
    published=[
        (r["orientation"],(F(r["a"]),F(r["b"]),F(r["z"])),F(r["value"]))
        for r in cert["bellman_anchors"]
    ]
    assert samples==published
    print("GEOMETRY_AND_PUBLISHED_24_ANCHORS_PASS",flush=True)
    return samples

def native_trees(root):
    sys.path.insert(0,str(root/"native_code"))
    from EC49FSA_THREE_OBSERVER_SOLVER import V,PIN
    assert PIN=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
    assert len(V)==228 and all(len(v)==141 for v in V)
    wanted={"Dmid":(329,36,68,141),"D45":(334,141,62,45),
            "D43":(326,141,47,43),"S105":(332,8,141,105)}
    for name,vec in wanted.items():
        tree=json.loads((root/"trees"/(name+".json")).read_text())
        use=Counter()
        for i in range(141):
            seen=set()
            node=tree
            while "named_observer" in node:
                q=node["named_observer"]
                assert q not in seen and 0<=q<228
                seen.add(q)
                use[q]+=1
                node=node["children"][str(V[q][i])]
            assert node=={"leaf":i},(name,i)
        got=(sum(use.values()),use[32],use[34],use[140])
        assert got==vec,(name,got,vec)
        print("ORIGINAL_141_PROFILE_TREE_PASS",name,flush=True)

def full_native(root,samples,workers):
    script=root/"native_code"/"EC49FSA_THREE_OBSERVER_SOLVER.py"
    def single(indexed):
        i,(orient,(a,b,z),expected)=indexed
        x,y=(a,b) if orient=="D" else (b,a)
        args=[sys.executable,str(script),"--a",str(x),"--b",str(y),"--z",str(z)]
        result=subprocess.run(args,check=True,text=True,
                              capture_output=True,timeout=100)
        obj=json.loads(result.stdout)
        got=F(obj["numerator"],obj["denominator"])
        assert got==expected,(i,got,expected)
        return i,orient,expected
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for i,orient,expected in ex.map(single,enumerate(samples)):
            print("EXACT_UNRESTRICTED_ALL228_BELLMAN_PASS",i,orient,expected,flush=True)

def independent(root):
    sys.path.insert(0,str(root/"native_code"))
    from EC49FSA_FSB_INDEPENDENT_CHECK import certify
    cases=[
      ("D",F(3,4),F(7,16),F(11,16),F(1361,8)),
      ("S",F(49,64),F(57,128),F(11,16),F(9491,64))]
    for orient,a,b,z,expected in cases:
        prices={32:a,34:b,140:z} if orient=="D" else {32:b,34:a,140:z}
        assert F(certify(prices)["value"])==expected
        print("INDEPENDENT_RAW94_PASS",orient,str(expected),flush=True)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--cert",default=str(Path(__file__).with_name(
         "EC49FTH_NATIVE_43_USE_FAN_CERT.json")))
    parser.add_argument("--bundle-root",default=None)
    parser.add_argument("--full",action="store_true")
    parser.add_argument("--independent",action="store_true")
    parser.add_argument("--workers",type=int,default=4)
    args=parser.parse_args()
    cert=json.loads(Path(args.cert).read_text())
    samples=anchors(cert)
    if args.full or args.independent:
        if not args.bundle_root:
            parser.error("--bundle-root required for native data/tree replay")
        root=Path(args.bundle_root)
        native_trees(root)
        if args.full:
            full_native(root,samples,args.workers)
        if args.independent:
            independent(root)
    print("EC49FTH_CERT_VERIFICATION_COMPLETE",flush=True)

if __name__=="__main__":
    main()
