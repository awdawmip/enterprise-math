#!/usr/bin/env python3
"""Verify exact FSL native BRC 10-region tree/geometry/vertex certificate.

Usage:
  python EC49FSL_VERIFY_NATIVE_TEN_REGION.py /path/to/extracted/native_evidence
  python EC49FSL_VERIFY_NATIVE_TEN_REGION.py /path/to/extracted/native_evidence --recompute
  python EC49FSL_VERIFY_NATIVE_TEN_REGION.py /path/to/extracted/native_evidence --recompute --independent

Requires the sibling files of this PR, its inherited FSK 9-tree bundle,
and the frozen original source package containing code/ and source/.
The native source solver was already executed at the 21 exact vertices;
--recompute repeats those finite calculations rather than sampling real parameters.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import base64, hashlib, json, sys, zlib

HERE=Path(__file__).resolve().parent
SRC=Path(sys.argv[1]).resolve()
sys.path.insert(0,str(SRC/"code"))
from EC49FSA_THREE_OBSERVER_SOLVER import V,PIN,solve
from EC49FRQ_INDEPENDENT_ALL228 import OBS,subset_keys
from EC49FQI_NATIVE_DATA import keys
assert PIN=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert len(V)==len(OBS)==228 and all(len(a)==141 for a in V)
assert all(tuple(OBS[i])==tuple(V[i if i<144 else 144+keys.index(subset_keys[i-144])]) for i in range(228))

cert=json.loads((HERE/"EC49FSL_TEN_REGION_MACHINE_CERTIFICATE.json").read_text())
assert cert["scientific_pin"]==PIN
pfile=HERE/"EC49FSK_NINE_WITNESS_TREES_ZLIB_BASE64.txt"
data=pfile.read_text().splitlines()
h=[s for s in data if s.startswith("raw_json_sha256:")]
assert len(h)==1
raw=zlib.decompress(base64.b64decode(data[-1].strip()))
assert hashlib.sha256(raw).hexdigest()==h[0].split(":",1)[1].strip()
trees=json.loads(raw)
new=(HERE/"EC49FSL_NEW_NATIVE_WITNESSES_ZLIB_BASE64.txt").read_text().splitlines()
for i,line in enumerate(new):
    if not line.startswith("tree_"):continue
    name,field=line.split(" sha256=",1)
    b=base64.b64decode(new[i+1].strip())
    t=json.loads(zlib.decompress(b))
    actual=hashlib.sha256(json.dumps(t,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    assert actual==field.strip()
    trees[name]=t

def counts(tree):
    use=Counter();maxdepth=0
    for state in range(141):
        node=tree;seen=set();depth=0
        while "named_observer" in node:
            o=node["named_observer"];assert 0<=o<228 and o not in seen
            seen.add(o);use[o]+=1;depth+=1
            node=node["children"][str(V[o][state])]
        assert node=={"leaf":state}
        maxdepth=max(maxdepth,depth)
    return [sum(use.values()),use[32]+use[34],use[140]],maxdepth

def score(p,x):
    return Q(p[0])-p[1]*x[0]-p[2]*x[1]
def area(poly):
    return abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(poly,poly[1:]+poly[:1])))/2 if len(poly)>2 else Q(0)
def clip(poly,A,B,C):
    def f(x):return A*x[0]+B*x[1]+C
    ans=[]
    for u,v in zip(poly,poly[1:]+poly[:1]):
        a,b=f(u),f(v)
        if a<=0:ans.append(u)
        if a<0<b or b<0<a:
            ans.append(tuple((b*x-a*y)/(b-a) for x,y in zip(u,v)))
        elif a>0 and b==0:ans.append(v)
    uniq=[]
    for x in ans:
        if not uniq or x!=uniq[-1]:uniq.append(x)
    if len(uniq)>1 and uniq[0]==uniq[-1]:uniq.pop()
    return uniq

rows=cert["regions"]
P=[tuple(r["triple"]) for r in rows]
assert len(rows)==len(set(P))==10
assert len({(p[1],p[2]) for p in P})==10
box=[(Q(15,32),Q(0)),(Q(1,2),Q(0)),(Q(1,2),Q(1)),(Q(15,32),Q(1))]
found=set();total=Q(0)
for r,p in zip(rows,P):
    name=r["witness"]["filename"]
    t=trees[name]
    assert counts(t)[0]==list(p) and counts(t)[1]<=4
    digest=hashlib.sha256(json.dumps(t,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    assert digest==r["witness"]["sha256"]
    poly=box[:]
    for other in P:
        if p!=other:
            poly=clip(poly,other[1]-p[1],other[2]-p[2],p[0]-other[0])
    expected={tuple(map(Q,v)) for v in r["vertices"]}
    assert set(poly)==expected,(p,poly,expected)
    assert area(poly)==Q(r["area"])>0
    total+=area(poly)
    found|=expected
assert total==Q(1,32)
assert len(found)==21
C={(Q(v["alpha"]),Q(v["z"])):Q(v["exact_bellman"]) for v in cert["vertices"]}
assert len(C)==21 and set(C)==found
for point,value in C.items():
    assert min(score(p,point) for p in P)==value
    if "--recompute" in sys.argv:
        info,_=solve({32:point[0],34:point[0],140:point[1]})
        assert Q(info["numerator"],info["denominator"])==value
    if "--independent" in sys.argv:
        from EC49FSA_FSB_INDEPENDENT_CHECK import certify
        assert Q(certify({32:point[0],34:point[0],140:point[1]})["value"])==value
print("PASS: 10 complete original native trees; 21 exact vertices; 10 disjoint positive-area regions; area 1/32; source pin and 228 named observers.")
if "--recompute" in sys.argv:print("PASS: primary exact Bellman recomputed at 21/21 vertices.")
if "--independent" in sys.argv:print("PASS: independent original-source Bellman recomputed at 21/21 vertices.")
