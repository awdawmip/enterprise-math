#!/usr/bin/env python3
"""EC49FTH: exact-rational polygon geometry, full named-tree replay and optional Bellman reruns.
Extract the separately supplied EC49FTH source archive and run from its root.
"""
import sys, json, argparse, subprocess
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from itertools import combinations
from collections import Counter

ap=argparse.ArgumentParser()
ap.add_argument("--evidence-root", default=".")
ap.add_argument("--full", action="store_true")
ap.add_argument("--start", type=int, default=0)
ap.add_argument("--stop", type=int, default=12)
ap.add_argument("--independent", action="store_true")
args=ap.parse_args()
root=Path(args.evidence_root)
cert=json.loads((root/"EC49FTH_CERT.json").read_text())
assert cert["pin"]=="awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
a=Q(cert["domain"]["a"])
names=("D43","D45","Dmid")
def line(name):
    u,n32,n34,n140=cert["usage_vectors"][name]
    if name in names:return (Q(u)-n32*a,-Q(n34),-Q(n140))
    return (Q(u)-n34*a,-Q(n32),-Q(n140))
def cost(name,b,z):
    v=line(name)
    return v[0]+v[1]*b+v[2]*z
def crossing(x,y):
    (p,q,r),(P,Q_,R)=x,y
    d=q*R-Q_*r
    return ((-p*R+P*r)/d,(-q*P+Q_*p)/d) if d else None
def vertices(name):
    (b0,b1),(z0,z1)=[list(map(Q,cert["domain"][k])) for k in ("b","z")]
    inequalities=[(-b0,1,0),(b1,-1,0),(-z0,0,1),(z1,0,-1)]
    for other in names:
        if other!=name:
            inequalities.append(tuple(x-y for x,y in zip(line(other),line(name))))
    ret=set()
    for x,y in combinations(inequalities,2):
        p=crossing(x,y)
        if p is not None and all(c[0]+c[1]*p[0]+c[2]*p[1]>=0 for c in inequalities):
            ret.add(p)
    return sorted(ret)

all_vertices=set()
for name in names:
    vv=vertices(name)
    assert [[str(b),str(z)] for b,z in vv]==cert["D_cell_vertices"][name]
    all_vertices.update(vv)
assert len(all_vertices)==8
D_anchors=[r for r in cert["primary_anchors"] if r["o"]=="D"]
S_anchors=[r for r in cert["primary_anchors"] if r["o"]=="S"]
assert len(D_anchors)==8 and len(S_anchors)==4
assert {(Q(r["b"]),Q(r["z"])) for r in D_anchors}==all_vertices
for r in cert["primary_anchors"]:
    b,z=Q(r["b"]),Q(r["z"])
    choices=names if r["o"]=="D" else ("S105",)
    assert min(cost(name,b,z) for name in choices)==Q(r["expected"])
gaps=[(cost(name,b,z)-cost("S105",b,z),b,z)
      for name in names for b,z in vertices(name)]
for key,fn in (("gap_min",min),("gap_max",max)):
    v=fn(x[0] for x in gaps)
    assert v==Q(cert[key]["value"])
    b,z=map(Q,cert[key]["witness"])
    assert min(cost(n,b,z) for n in names)-cost("S105",b,z)==v
print("GEOMETRY_PASS 3_CELLS 8_D_VERTICES 4_S_CORNERS SHARP_GAPS",flush=True)

for filename,expected in cert["source_sha256"].items():
    assert sha256((root/"source"/filename).read_bytes()).hexdigest()==expected
sys.path.insert(0,str(root/"native_code"))
from EC49FSA_THREE_OBSERVER_SOLVER import V,PIN
assert PIN==cert["pin"].split("@")[1] and len(V)==228 and all(len(row)==141 for row in V)
for name,usage in cert["usage_vectors"].items():
    p=root/"trees"/(name+".json")
    assert sha256(p.read_bytes()).hexdigest()==cert["tree_sha256"][name]
    tree=json.loads(p.read_text()); observed=Counter()
    for state in range(141):
        node=tree;seen=set()
        while "named_observer" in node:
            q=node["named_observer"]
            assert q in range(228) and q not in seen
            seen.add(q);observed[q]+=1
            node=node["children"][str(V[q][state])]
        assert node=={"leaf":state}
    actual=[sum(observed.values()),observed[32],observed[34],observed[140]]
    assert actual==usage,(name,actual,usage)
    print("NATIVE_TREE_PASS",name,actual,flush=True)

if args.full:
    assert 0<=args.start<=args.stop<=12
    script=root/"native_code"/"EC49FSA_THREE_OBSERVER_SOLVER.py"
    for r in cert["primary_anchors"][args.start:args.stop]:
        ra,rb,rz=r["a"],r["b"],r["z"]
        cmd=[sys.executable,str(script),"--a",ra if r["o"]=="D" else rb,
             "--b",rb if r["o"]=="D" else ra,"--z",rz]
        cp=subprocess.run(cmd,capture_output=True,text=True,check=True,timeout=120)
        got=json.loads(cp.stdout)
        assert Q(got["numerator"],got["denominator"])==Q(r["expected"])
        print("ALL228_EXACT_BELLMAN_PASS",r["o"],b,z,r["expected"],flush=True)

if args.independent:
    from EC49FSA_FSB_INDEPENDENT_CHECK import certify
    for r in cert["independent_new_points"]:
        b,z=Q(r["b"]),Q(r["z"])
        discounts={32:a,34:b,140:z} if r["o"]=="D" else {32:b,34:a,140:z}
        got=certify(discounts)
        expected=min(cost(n,b,z) for n in (names if r["o"]=="D" else ("S105",)))
        assert Q(got["value"])==expected
        print("INDEPENDENT_RAW94_PASS",r["o"],b,z,str(expected),flush=True)
print("EC49FTH_VERIFICATION_COMPLETE",flush=True)
