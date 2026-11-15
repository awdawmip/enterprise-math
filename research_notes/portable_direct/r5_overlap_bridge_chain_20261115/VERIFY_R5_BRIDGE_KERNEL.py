#!/usr/bin/env python3
"""R5 local bridge spectrum and guard-separated tensors; exact integer test."""
from itertools import product
from pathlib import Path
import json
import sys

OLD=[(0,1,2,5),(0,1,3,5),(0,2,3,5),(0,2,4,5),(0,2,4,6)]
NEW_A=[((1,2,3,5),1),((1,2,4,5),1),((1,2,4,6),1),((1,3,4,5),0),((1,3,4,6),0)]
NEW_AB=NEW_A+[((1,2,3,6),1)]
Y=(1,2,4,11,13,14)
GROUPS={5:(1,4,13),10:(2,11,14)}
CHOICES=((),(5,),(10,),(5,10))

def hd(u,v): return (u^v).bit_count()
def cd(C,O): return len(set(C)-set(O))
def rho(target,source):
    C,t,v=target
    j,s,u=source
    return cd(C,OLD[j])+int(t!=s)+hd(v,u)
def targets(ys,ab=False):
    return [(C,t,y) for y in ys for C,t in (NEW_AB if ab else NEW_A)]
def covers(library,ys,ab=False):
    return all(any(rho(t,r)<=2 for r in library) for t in targets(ys,ab))
def guards(k):
    return [sum(1<<(4+3*i+j) for j in range(3)) for i in range(k)]
def witness(gs,hs):
    out=[]
    for g,H in zip(gs,hs):
        out.extend((1,0,g|y) for y in Y)
        for h,G in GROUPS.items():
            if h in H:
                out.extend([(0,1,g|h),(4,1,g|h)])
            else:
                out.extend((0,1,g|y) for y in G)
    return out
def local_tests():
    rows=((1,1,1,2,3),(1,2,2,1,2),(2,3,3,2,1),(2,1,2,2,3),(3,2,3,3,2),(2,2,2,3,2))
    assert tuple(tuple(cd(C,O) for O in OLD) for C,t in NEW_AB)==rows
    assert min(hd(x,y) for i,x in enumerate(Y) for y in Y[i+1:])==2
    assert set(Y)==set(GROUPS[5])|set(GROUPS[10])
    for h,G in GROUPS.items():
        assert {y for y in Y if hd(h,y)==1}==set(G)
    for y in Y:
        E=((1,3,4,6),0,y)
        permissible=[(j,s,u) for j,s,u in product(range(5),(0,1),Y+(5,10)) if rho(E,(j,s,u))<=2]
        assert set(permissible)=={(1,0,y),(4,0,y)}
        crit=[((1,2,4,5),1,y),((1,2,4,6),1,y),((1,3,4,5),0,y)]
        for base in permissible:
            assert sum(rho(t,base)>2 for t in crit)>=2
        h=5 if y in GROUPS[5] else 10
        for j,s in product(range(5),(0,1)):
            assert sum(rho(t,(j,s,h))<=2 for t in crit)<=1
    out=[]
    for H in CHOICES:
        ws=witness([0],[H])
        assert len(ws)==12-len(H) and len(set(ws))==len(ws)
        assert {u for j,s,u in ws}<=set(Y)|set(H)
        assert covers(ws,Y)
        out.append({"helpers":list(H),"kappa_a":12-len(H),"kappa_ab":12,"witness":ws})
    return out
def tensor_tests():
    out=[]
    for k in range(1,5):
        gs=guards(k)
        ys=[g|y for g in gs for y in Y]
        assert len(set(ys))==6*k
        if k>1:
            assert min(hd(gs[i]|y,gs[j]|z) for i in range(k)
                       for j in range(i+1,k) for y in Y for z in Y)>=6
        vals=[]
        for hs in product(CHOICES,repeat=k):
            ws=witness(gs,hs)
            want=12*k-sum(map(len,hs))
            assert len(ws)==want and len(set(ws))==want
            assert all(any(u==(g|v) for g,H in zip(gs,hs)
                           for v in (*Y,*H)) for j,s,u in ws)
            assert covers(ws,ys)
            vals.append(want)
        assert len(vals)==4**k
        out.append({"k":k,"suffix_dimension":4+3*k,"cases":len(vals),
                    "kappa_a_min":min(vals),"kappa_a_max":max(vals),
                    "kappa_ab":12*k})
    return out
def main():
    data={"model":"R5 auxiliary indexed-center radius-two source-aware repair",
          "scientific_pin":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
          "local_cases":local_tests(),
          "tensors":tensor_tests(),
          "universal_scope":"Proved analytically for all integer k>=1 and all helper subsets",
          "verification_scope":"All four local cases and all 340 guarded tensor cases, exact integers"}
    if len(sys.argv)>1:
        Path(sys.argv[1]).write_text(json.dumps(data,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print("PASS_R5_BRIDGE_SPECTRUM_TENSOR_AND_PROVENANCE")
    for row in data["tensors"]: print(row)
if __name__=="__main__":main()
