#!/usr/bin/env python3
"""EC49FSK exact native BRC certificate verifier (Python stdlib).

From the self-contained evidence archive, point --native-dir to code/ which
contains EC49FQI_NATIVE_DATA.py and its frozen source/ sibling directory.
Optionally use --primary/--independent to rerun exact Bellman computation.
"""
import argparse,base64,hashlib,json,sys,zlib
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

def area(poly):
    return abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(poly,poly[1:]+poly[:1])))/2 if len(poly)>2 else F(0)

def clip(poly,A,B,C):
    def h(x):return A*x[0]+B*x[1]+C
    out=[]
    for x,y in zip(poly,poly[1:]+poly[:1]):
        a,b=h(x),h(y)
        if a<=0:out.append(x)
        if (a<0<b) or (b<0<a):out.append(tuple((b*u-a*v)/(b-a) for u,v in zip(x,y)))
        elif a>0 and b==0:out.append(y)
    unique=[]
    for x in out:
        if not unique or unique[-1]!=x:unique.append(x)
    if len(unique)>1 and unique[0]==unique[-1]:unique.pop()
    return unique

def value(r,a,z):
    return F(r["U"])-F(r["Q"])*a-F(r["K"])*z

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--native-dir",required=True)
    ap.add_argument("--certificate",default="EC49FSK_NATIVE_BRC_11_REGION_MACHINE_CERTIFICATE.json")
    ap.add_argument("--trees",default="EC49FSK_ELEVEN_NATIVE_TREES_JSON_ZLIB_BASE64.txt")
    ap.add_argument("--primary",action="store_true")
    ap.add_argument("--independent",action="store_true")
    a=ap.parse_args()
    c=json.loads(Path(a.certificate).read_text())
    assert c["science_pin"]=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
    sys.path.insert(0,a.native_dir)
    from EC49FQI_NATIVE_DATA import V,PIN
    assert PIN==c["science_pin"] and len(V)==228 and all(len(row)==141 for row in V)
    trees=json.loads(zlib.decompress(base64.b64decode(Path(a.trees).read_text().strip())))
    regions=c["regions"]
    assert len(regions)==len(trees)==11
    low,high=F(7,16),F(1,2)
    bounds=[(low,F(0)),(high,F(0)),(high,F(1)),(low,F(1))]
    all_vertices=set();sum_area=F(0)
    for r in regions:
        key=f'{r["U"]}_{r["Q"]}_{r["K"]}'
        tree=trees[key]
        digest=hashlib.sha256(json.dumps(tree,sort_keys=True,separators=(",",":")).encode()).hexdigest()
        assert digest==r["tree_sha256"],key
        counts=Counter();depth=0
        for state in range(141):
            node=tree;seen=set();d=0
            while "named_observer" in node:
                q=node["named_observer"]
                assert 0<=q<228 and q not in seen
                seen.add(q);counts[q]+=1;d+=1
                node=node["children"][str(V[q][state])]
            assert node=={"leaf":state}
            depth=max(depth,d)
        assert (sum(counts.values()),counts[32]+counts[34],counts[140])==(r["U"],r["Q"],r["K"])
        assert tree["named_observer"]==r["root"] and depth==r["max_depth"]
        poly=bounds[:]
        for s in regions:
            if s is r:continue
            poly=clip(poly,F(s["Q"]-r["Q"]),F(s["K"]-r["K"]),F(r["U"]-s["U"]))
            if not poly:break
        exact_area=area(poly)
        assert exact_area==F(r["area"]) and exact_area>0,(key,exact_area)
        sum_area+=exact_area;all_vertices.update(poly)
        for alpha,z in poly:
            assert value(r,alpha,z)==min(value(t,alpha,z) for t in regions)
    assert sum_area==F(1,16)==F(c["exact_region_area_sum"])
    expected={(F(p["alpha"]),F(p["z"])):F(p["value"]) for p in c["vertices"]}
    assert len(expected)==len(all_vertices)==22 and set(expected)==all_vertices
    for (alpha,z),optimal in expected.items():
        assert optimal==min(value(t,alpha,z) for t in regions)
    print("PASS: 11 full native 141-profile trees, 22 exact rational vertices, area 1/16")
    if a.primary:
        from EC49FSA_THREE_OBSERVER_SOLVER import solve
        for i,((alpha,z),optimal) in enumerate(sorted(expected.items())):
            out,_=solve({32:alpha,34:alpha,140:z})
            assert F(out["numerator"],out["denominator"])==optimal
            print("PRIMARY",i+1,"/22",alpha,z,optimal,flush=True)
    if a.independent:
        from EC49FSA_FSB_INDEPENDENT_CHECK import certify
        checked=0
        for (alpha,z),optimal in sorted(expected.items()):
            if alpha==low:continue
            assert F(certify({32:alpha,34:alpha,140:z})["value"])==optimal
            checked+=1
            print("INDEPENDENT",checked,"/13",alpha,z,optimal,flush=True)
        assert checked==13
    print("PASS: exact model certificate; independent peer review remains open")

if __name__=="__main__":
    main()
