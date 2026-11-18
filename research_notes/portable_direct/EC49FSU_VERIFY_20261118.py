#!/usr/bin/env python3
"""EC49FSU exact original-228-observation certificate verifier.

Run from the companion self-contained native evidence bundle with this file,
EC49FSU_UPPER_FAN_CERT_20261118.json, native_code/ and source/ co-located.
No remote access; standard Python 3, integer/Fraction arithmetic only.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import hashlib, json, sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/"native_code"))
from EC49FSA_THREE_OBSERVER_SOLVER import PIN,V,solve
from EC49FSA_FSB_INDEPENDENT_CHECK import certify
assert PIN=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert len(V)==228 and all(len(x)==141 for x in V)
C=json.loads((HERE/"EC49FSU_UPPER_FAN_CERT_20261118.json").read_text())
assert C["frozen_science_pin"]==PIN
for name,filename in (("master_sha256","frozen_original_master.txt"),("profile_csv_sha256","EC49FPG_PROFILE.csv")):
    blob=(HERE/"source"/filename).read_bytes()
    assert hashlib.sha256(blob).hexdigest()==C["original_hashes"][name]

a=F(2,3);b0,b1=F(27,64),F(29,64);z0,z1=F(77,128),F(5,8)
box=[(b0,z0),(b1,z0),(b1,z1),(b0,z1)]
ps={orientation:[tuple(p["uses"]) for p in C["planes"][orientation]] for orientation in ("direct","swapped")}

def cost(t,b,z,orientation):
    u,n32,n34,n140=t
    return (F(u)-a*n32-b*n34-z*n140 if orientation=="direct"
            else F(u)-b*n32-a*n34-z*n140)

def clip(poly,func):
    if not poly:return []
    output=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        x,y=func(p),func(q)
        if x<=0:output.append(p)
        if (x<0<y) or (y<0<x):
            output.append(((p[0]*y-q[0]*x)/(y-x),(p[1]*y-q[1]*x)/(y-x)))
    compact=[]
    for p in output:
        if not compact or p!=compact[-1]:compact.append(p)
    if len(compact)>1 and compact[-1]==compact[0]:compact.pop()
    return compact

def area(poly):
    if len(poly)<3:return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1])))/2

poly={}
for orientation in ps:
    for witness in C["planes"][orientation]:
        t=tuple(witness["uses"])
        shape=box[:]
        for other in ps[orientation]:
            if other!=t:
                shape=clip(shape,lambda x,t=t,other=other,orientation=orientation:
                           cost(t,*x,orientation)-cost(other,*x,orientation))
        assert area(shape)==F(witness["region_area"])>0
        poly[(orientation,t)]=shape
    assert sum(area(poly[(orientation,t)]) for t in ps[orientation])==F(3,4096)
print("RATIONAL_PHASE_AREA_PASS",flush=True)

gap=[]
overlap_count=0;overlap_total=F(0)
for d in ps["direct"]:
    for s in ps["swapped"]:
        shape=poly[("direct",d)][:]
        for other in ps["swapped"]:
            if other!=s:
                shape=clip(shape,lambda x,s=s,other=other:
                           cost(s,*x,"swapped")-cost(other,*x,"swapped"))
        if area(shape)>0:
            overlap_count+=1;overlap_total+=area(shape)
            gap += [(cost(d,*x,"direct")-cost(s,*x,"swapped"),*x) for x in shape]
assert overlap_count==5 and overlap_total==F(3,4096)
assert min(gap)==(F(917,64),b1,z0)
assert max(gap)==(F(1065,64),b0,z1)
print("FIVE_OVERLAPS_AND_SHARP_SWAP_GAP_PASS",flush=True)

if "--native" in sys.argv:
    oracle_trees={}
    for orientation in ps:
        for bstr,zstr,vstr,states in C["anchors"][orientation]:
            b,z=F(bstr),F(zstr)
            assert b0<=b<=b1 and z0<=z<=z1
            expected=min(cost(t,b,z,orientation) for t in ps[orientation])
            assert expected==F(vstr)
            params={32:a,34:b,140:z} if orientation=="direct" else {32:b,34:a,140:z}
            info,tree=solve(params)
            assert F(info["numerator"],info["denominator"])==expected
            assert info["states"]==states
            oracle_trees[(orientation,b,z)]=(info,tree)
            print("NATIVE_BELLMAN_PASS",orientation,b,z,expected,flush=True)
    # Reconstruct all seven immutable original named-profile tree witnesses.
    witness_input={
       "E":("direct",F(27,64),F(77,128)),
       "J":("direct",F(29,64),F(77,128)),
       "L":("direct",F(29,64),F(5,8)),
       "M":("direct",F(17,38),F(5,8)),
       "K":("swapped",F(27,64),F(77,128)),
       "N":("swapped",F(27,64),F(5,8)),
       "O":("swapped",F(29,64),F(5,8))}
    for orientation in ps:
        for witness in C["planes"][orientation]:
            info,tree=oracle_trees[witness_input[witness["id"]]]
            raw=json.dumps(tree,sort_keys=True,separators=(",",":")).encode()
            assert hashlib.sha256(raw).hexdigest()==witness["tree_plain_sha256"]
            assert len(raw)==witness["tree_plain_bytes"]
            assert tuple((info["U"],info["uses"]["32"],info["uses"]["34"],info["uses"]["140"]))==tuple(witness["uses"])
            # Replay every path independently against original observation values.
            counts=Counter()
            for i in range(141):
                node=tree;used=set()
                while "named_observer" in node:
                    q=node["named_observer"]
                    assert q not in used and 0<=q<228
                    used.add(q);counts[q]+=1
                    node=node["children"][str(V[q][i])]
                assert node["leaf"]==i
            assert (sum(counts.values()),counts[32],counts[34],counts[140])==tuple(witness["uses"])
            print("ALL_141_NAMED_PATHS_REPLAY_PASS",witness["id"],flush=True)

if "--independent" in sys.argv:
    for datum in C["independently_reconstructed_94_family"]:
        orientation,b,z=datum["orientation"],F(datum["b"]),F(datum["z"])
        params={32:a,34:b,140:z} if orientation=="direct" else {32:b,34:a,140:z}
        assert F(certify(params)["value"])==F(datum["result"])
        print("INDEPENDENT_RAW_94_FAMILY_PASS",orientation,b,z,flush=True)
print("EC49FSU_EXACT_CERTIFICATE_PASS",flush=True)
