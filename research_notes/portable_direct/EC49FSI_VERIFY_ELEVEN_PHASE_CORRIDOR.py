#!/usr/bin/env python3
"""EC49FSI portable exact native-tree/geometry certificate checker.

Requires Python 3.10+ (stdlib). Geometry and tree checks are offline.
For actual exhaustive Bellman confirmation, pass the earlier frozen solver
source directory with --solver-dir, and optionally --independent-dir.
The frozen source module directory containing EC49FQI_NATIVE_DATA.py is
required to validate observer responses, rather than trusting leaf labels.
"""
import argparse
import base64
from collections import Counter
from fractions import Fraction as F
import hashlib
import importlib
import json
from pathlib import Path
import sys
import zlib

def area(poly):
    return abs(sum(x[0]*y[1]-y[0]*x[1] for x,y in zip(poly,poly[1:]+poly[:1])))/2 if len(poly)>2 else F(0)

def price(line, a, z):
    return line["U"]-F(line["Q"])*a-F(line["K"])*z

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--certificate",default="EC49FSI_TWO_PRICE_BRIDGE_MACHINE_CERTIFICATE.json")
    p.add_argument("--trees",default="EC49FSI_ELEVEN_NATIVE_TREES_JSON_ZLIB_BASE64.txt")
    p.add_argument("--native-data-dir",required=True,help="Directory containing frozen EC49FQI_NATIVE_DATA.py")
    p.add_argument("--solver-dir",help="Directory containing EC49FSA_THREE_OBSERVER_SOLVER.py; optional full global Bellman checks")
    p.add_argument("--independent-dir",help="Directory containing EC49FSA_FSB_INDEPENDENT_CHECK.py")
    args=p.parse_args()
    doc=json.loads(Path(args.certificate).read_text())
    assert doc["science_pin"]=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
    sys.path.insert(0,args.native_data_dir)
    from EC49FQI_NATIVE_DATA import V,PIN
    assert PIN==doc["science_pin"] and len(V)==228 and len(V[0])==141
    bundle=json.loads(zlib.decompress(base64.b64decode(Path(args.trees).read_text().strip())).decode())
    rows=doc["regions"]
    assert len(rows)==11 and len(bundle)==11
    for r in rows:
        U,Q,K=r["U"],r["Q"],r["K"]
        tree=bundle[f"{U},{Q},{K}"]
        b=json.dumps(tree,sort_keys=True,separators=(",",":")).encode()
        assert hashlib.sha256(b).hexdigest()==r["tree_sha256"]
        count=Counter()
        for i in range(141):
            n=tree
            used=set()
            while "named_observer" in n:
                q=n["named_observer"]
                assert q not in used and 0<=q<228
                used.add(q)
                count[q]+=1
                n=n["children"][str(V[q][i])]
            assert n=={"leaf":i}
        assert (sum(count.values()),count[32]+count[34],count[140])==(U,Q,K)
        poly=[tuple(F(v) for v in point) for point in r["polygon"]]
        assert area(poly)==F(r["area"]) and area(poly)>0
        for a,z in poly:
            assert F(1,3)<=a<=F(3,8) and 0<=z<=1
            assert price(r,a,z)==min(price(q,a,z) for q in rows)
    assert sum(F(r["area"]) for r in rows)==F(1,24)
    for point in doc["vertex_bellman"]:
        a,z=F(point["alpha"]),F(point["z"])
        assert F(point["value"])==min(price(r,a,z) for r in rows)
    assert len(doc["vertex_bellman"])==19
    print("EXACT GEOMETRY + 11 NATIVE TREES + 141 NAMED PROFILES: PASS")
    if args.solver_dir:
        sys.path.insert(0,args.solver_dir)
        from EC49FSA_THREE_OBSERVER_SOLVER import solve
        for point in doc["vertex_bellman"]:
            a,z=F(point["alpha"]),F(point["z"])
            info,_=solve({32:a,34:a,140:z})
            assert F(info["numerator"],info["denominator"])==F(point["value"])
            print("PRIMARY BELLMAN MATCH",a,z,point["value"],flush=True)
    if args.independent_dir:
        sys.path.insert(0,args.independent_dir)
        from EC49FSA_FSB_INDEPENDENT_CHECK import certify
        for pt in doc["independent_new_interior_vertices"]:
            a,z=F(pt["alpha"]),F(pt["z"])
            v=certify({32:a,34:a,140:z})
            assert F(v["value"])==F(pt["value"])
            print("INDEPENDENT BELLMAN MATCH",a,z,pt["value"],flush=True)
    print("CERTIFICATE VERIFIED; independent human mathematical review still pending")

if __name__=="__main__":
    main()
