#!/usr/bin/env python3
"""EC49FSS: exact native BRC16943 full three-price prism verification.

Use original frozen source fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Put the frozen native code from the EC49FSS evidence archive on PYTHONPATH and
the two frozen raw input files in ../source relative to that native code.
All 228 physically named queries and all 141 distinct named profiles are used.
"""
import json, hashlib, zlib, base64, gc, itertools, sys
from fractions import Fraction as Q
from pathlib import Path
from collections import Counter
from EC49FSA_THREE_OBSERVER_SOLVER import solve, V, PIN
assert PIN == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"

LO=(Q(1,2),Q(27,64),Q(1,2))
HI=(Q(1),Q(29,64),Q(9,16))
NATIVE={
  "A":(319,18,75,141), "E":(316,141,43,30),
  "H":(315,10,141,77), "W":(323,12,89,141)
}
CELLS=[("A","E","direct"),("E","A","direct"),
       ("H","W","swapped"),("W","H","swapped")]

def cost(v, xyz, orientation):
    a,b,z=xyz
    u,n32,n34,n140=v
    if orientation=="direct":
        return u-n32*a-n34*b-n140*z
    return u-n34*a-n32*b-n140*z

def coeffs(v, orientation):
    u,n32,n34,n140=v
    if orientation=="direct":return (Q(u),-Q(n32),-Q(n34),-Q(n140))
    return (Q(u),-Q(n34),-Q(n32),-Q(n140))

def det(t):
    (a,b,c),(d,e,f),(g,h,i)=t
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def vertex_of(rows):
    A=[list(row[1:]) for row in rows]
    d=det(A)
    if d==0:return None
    ys=[-row[0] for row in rows]
    xyz=[]
    for k in range(3):
        M=[r[:] for r in A]
        for j in range(3):M[j][k]=ys[j]
        xyz.append(det(M)/d)
    return tuple(xyz)

def region_vertices(winner,opponent,orient):
    # Constraints all of the form c0+c1*a+c2*b+c3*z >= 0
    C=[]
    for k in range(3):
        low=[Q(0)]*4;low[0]=-LO[k];low[k+1]=Q(1)
        high=[Q(0)]*4;high[0]=HI[k];high[k+1]=Q(-1)
        C.extend((tuple(low),tuple(high)))
    x=coeffs(NATIVE[winner],orient)
    y=coeffs(NATIVE[opponent],orient)
    C.append(tuple(yy-xx for xx,yy in zip(x,y)))
    out=set()
    for ijk in itertools.combinations(range(len(C)),3):
        v=vertex_of([C[i] for i in ijk])
        if v is not None and all(row[0]+sum(row[j+1]*v[j] for j in range(3))>=0 for row in C):
            out.add(v)
    return out

def trace_all_141(tree,expected):
    counts=Counter()
    for i in range(141):
        nd=tree;used=set()
        while "named_observer" in nd:
            q=nd["named_observer"]
            assert 0<=q<228 and q not in used
            counts[q]+=1;used.add(q)
            nd=nd["children"][str(V[q][i])]
        assert nd["leaf"]==i
    got=(sum(counts.values()),counts[32],counts[34],counts[140])
    assert got==expected,(got,expected)

def main():
    regions={}
    for winner,opponent,orient in CELLS:
        regions[winner]=region_vertices(winner,opponent,orient)
    assert [len(regions[k]) for k in ["A","E","H","W"]]==[8,8,10,6]
    records=[]
    for orient,participants in [("direct",("A","E")),("swapped",("H","W"))]:
        vertices=sorted(regions[participants[0]]|regions[participants[1]])
        assert len(vertices)==12
        for a,b,z in vertices:
            discounts={32:a,34:b,140:z} if orient=="direct" else {32:b,34:a,140:z}
            info,tree=solve(discounts)
            exact=Q(info["numerator"],info["denominator"])
            expected=min(cost(NATIVE[n],(a,b,z),orient) for n in participants)
            assert exact==expected,(orient,a,b,z,exact,expected)
            record={"orientation":orient,"a":str(a),"b":str(b),"z":str(z),
                "exact":str(exact),"attains":[n for n in participants
                     if cost(NATIVE[n],(a,b,z),orient)==exact],
                "native_vector":[info["U"],info["uses"]["32"],info["uses"]["34"],info["uses"]["140"]],
                "reached_subsets":info["states"]}
            records.append(record)
            print("EXACT_228_BELLMAN",json.dumps(record,sort_keys=True),flush=True)
            del info,tree
            gc.collect()
    assert len(records)==24
    # Four complete trees are obtained at exact optimal sample points.
    seeds={
      "A":("direct",(Q(1,2),Q(27,64),Q(1,2))),
      "E":("direct",(Q(1),Q(27,64),Q(9,16))),
      "H":("swapped",(Q(1),Q(27,64),Q(9,16))),
      "W":("swapped",(Q(35,64),Q(27,64),Q(9,16)))
    }
    witness={}
    for name,(orient,(a,b,z)) in seeds.items():
        discounts={32:a,34:b,140:z} if orient=="direct" else {32:b,34:a,140:z}
        info,tree=solve(discounts)
        trace_all_141(tree,NATIVE[name])
        raw=json.dumps(tree,separators=(",",":"),sort_keys=True).encode()
        witness[name]={"orientation":orient, "vector":NATIVE[name],
          "anchor":[str(a),str(b),str(z)],
          "plain_sha256":hashlib.sha256(raw).hexdigest(),
          "plain_bytes":len(raw),
          "tree_base64_zlib":base64.b64encode(zlib.compress(raw,9)).decode()}
        print("FULL_141_TREE",name,NATIVE[name],len(raw),flush=True)
        del info,tree
        gc.collect()
    output=Path(__file__).resolve().parent
    (output/"EC49FSS_REGENERATED_FULL_CERT.json").write_text(json.dumps({
      "science_pin":PIN, "vertices":{k:[list(map(str,p)) for p in sorted(v)] for k,v in regions.items()},
      "bellman":records},indent=2)+"\n")
    (output/"EC49FSS_REGENERATED_COMPLETE_TREES.json").write_text(json.dumps(
      {"science_pin":PIN,"witnesses":witness},indent=2)+"\n")
    print("EC49FSS_FULL_24_VERTEX_4_TREE_PASS")

if __name__=="__main__":main()
