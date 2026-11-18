#!/usr/bin/env python3
"""EC49FTH appendix checker: run against extracted self-contained evidence archive."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,sys,subprocess,argparse

ap=argparse.ArgumentParser()
ap.add_argument("--evidence-root",default=".")
ap.add_argument("--full",action="store_true")
ap.add_argument("--independent",action="store_true")
ap.add_argument("--start",type=int,default=0)
ap.add_argument("--stop",type=int,default=5)
args=ap.parse_args()
root=Path(args.evidence_root)
sys.path.insert(0,str(root/"native_code"))
from EC49FSA_THREE_OBSERVER_SOLVER import V,PIN
assert PIN=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
a,b=Q(3,4),Q(7,16)
usages={
"D30":(316,141,43,30),"D40":(324,141,47,40),
"D43":(326,141,47,43),"D45":(334,141,62,45),
"Dmid":(329,36,68,141),"S82":(318,10,141,82),
"S93":(324,8,141,93),"S105":(332,8,141,105)}
for name,expected in usages.items():
    tree=json.loads((root/"trees"/(name+".json")).read_text())
    counts=Counter()
    for state in range(141):
        node=tree; used=set()
        while "named_observer" in node:
            q=node["named_observer"]
            assert 0<=q<228 and q not in used
            used.add(q);counts[q]+=1
            node=node["children"][str(V[q][state])]
        assert node=={"leaf":state}
    got=(sum(counts.values()),counts[32],counts[34],counts[140])
    assert got==expected,(name,got,expected)
    print("NATIVE_PROFILE_TREE_PASS",name,got,flush=True)

def cost(name,z):
    u,n32,n34,n140=usages[name]
    if name.startswith("D"):return Q(u)-n32*a-n34*b-n140*z
    return Q(u)-n32*b-n34*a-n140*z

D=("D40","D43","D45","Dmid")
S=("S93","S105")
anchors=[
("5/8","2763/16","1253/8"),
("2/3","8209/48","611/4"),
("23/32","5401/32","4713/32"),
("569/768","42953/256","111327/768"),
("3/4","333/2","144")]
for z,ed,es in anchors:
    zz=Q(z)
    assert min(cost(n,zz) for n in D)==Q(ed)
    assert min(cost(n,zz) for n in S)==Q(es)
    print("ENVELOPE_VERTEX_PASS",z,ed,es,flush=True)
assert cost("D30",Q(5,8))==cost("D40",Q(5,8))
assert cost("S82",Q(5,8))==cost("S93",Q(5,8))
breaks=[Q(t[0]) for t in anchors]
for j in range(4):
    mid=(breaks[j]+breaks[j+1])/2
    assert D[j]==min(D,key=lambda n:cost(n,mid))
    assert S[0 if mid<Q(2,3) else 1]==min(S,key=lambda n:cost(n,mid))
gaps=[min(cost(n,z) for n in D)-min(cost(n,z) for n in S) for z in breaks]
assert min(gaps)==Q(257,16) and max(gaps)==Q(1461,64)
print("EXACT_BREAKS_AND_SHARP_GAP_PASS",flush=True)

if args.full:
    script=root/"native_code"/"EC49FSA_THREE_OBSERVER_SOLVER.py"
    for z,ed,es in anchors[args.start:args.stop]:
        for o,expected in [("D",ed),("S",es)]:
            aa,bb=(a,b) if o=="D" else (b,a)
            cmd=[sys.executable,str(script),"--a",str(aa),"--b",str(bb),"--z",z]
            cp=subprocess.run(cmd,capture_output=True,text=True,check=True,timeout=120)
            result=json.loads(cp.stdout)
            assert Q(result["numerator"],result["denominator"])==Q(expected)
            print("PRIMARY_BELLMAN_PASS",o,z,expected,flush=True)

if args.independent:
    from EC49FSA_FSB_INDEPENDENT_CHECK import certify
    for z,ed,es in anchors[:2]:
        for o,expected in [("D",ed),("S",es)]:
            aa,bb=(a,b) if o=="D" else (b,a)
            got=certify({32:aa,34:bb,140:Q(z)})
            assert Q(got["value"])==Q(expected)
            print("INDEPENDENT_RAW94_PASS",o,z,expected,flush=True)
print("EC49FTH_LOWER_LINE_VERIFIED",flush=True)
