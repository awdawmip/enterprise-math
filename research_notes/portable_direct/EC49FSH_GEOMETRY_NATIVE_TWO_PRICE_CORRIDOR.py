#!/usr/bin/env python3
"""Reconstruct seven exact 2D native BRC cost-envelope polygons with rational clipping.
Usage: python EC49FSH_GEOMETRY_NATIVE_TWO_PRICE_CORRIDOR.py CERTIFICATE.json
No numpy, floating point geometry or affine approximation.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import sys

def clip(poly, a, b, c):
    def h(p): return a*p[0]+b*p[1]+c
    out=[]
    for P,Q in zip(poly,poly[1:]+poly[:1]):
        p,q=h(P),h(Q)
        if p<=0: out.append(P)
        if p<0<q or p>0>q:
            out.append(tuple((q*x-p*y)/(q-p) for x,y in zip(P,Q)))
        elif p>0 and q==0:
            out.append(Q)
    dedup=[]
    for v in out:
        if v not in dedup:dedup.append(v)
    return dedup

def area(poly):
    if len(poly)<3:return F(0)
    return abs(sum(x*y2-x2*y for (x,y),(x2,y2) in zip(poly,poly[1:]+poly[:1])))/2

def native_regions(planes):
    rectangle=[(F(5,16),F(0)),(F(1,3),F(0)),(F(1,3),F(1)),(F(5,16),F(1))]
    output=[]
    for i,p in enumerate(planes):
        polygon=rectangle[:]
        for j,q in enumerate(planes):
            if i==j: continue
            # U_i-Q_i*alpha-K_i*z <= U_j-Q_j*alpha-K_j*z
            polygon=clip(polygon,q["Q"]-p["Q"],q["K"]-p["K"],p["U"]-q["U"])
            if not polygon:break
        if polygon and area(polygon)>0:
            output.append((i,polygon))
    return output

def main():
    cert=json.loads(Path(sys.argv[1]).read_text())
    planes=cert["strategies"]
    regs=native_regions(planes)
    assert len(regs)==7
    total=F(0)
    for (idx,polygon), expected in zip(regs,cert["polygons"]):
        assert idx+1==expected["strategy"]
        actual=set(polygon)
        claimed=set((F(x),F(y)) for x,y in expected["vertices"])
        assert actual==claimed
        a=area(polygon)
        assert a==F(expected["area"]) and a>0
        total+=a
        print("REGION",idx+1,"area",a,"vertices",
              ",".join("("+str(x)+","+str(y)+")" for x,y in polygon))
    assert total==F(1,48)
    all_vertices=set(p for _,poly in regs for p in poly)
    assert len(all_vertices)==14
    assert all(p[0] in [F(5,16),F(1,3)] for p in all_vertices)
    print("ALL_RATIONAL_POLYGONS_RECONSTRUCTED",len(regs),len(all_vertices),
          "area",total)

if __name__=="__main__":
    main()
