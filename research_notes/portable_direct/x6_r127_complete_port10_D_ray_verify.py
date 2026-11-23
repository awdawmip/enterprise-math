#!/usr/bin/env python3
"""R127 exact Fraction replay: six-pair conditional BRC, Port 10, D>=900."""
from fractions import Fraction as Q
import json

PAIRS=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
def port(a):
    return max(sum(max(0,x) for x in a),sum(max(0,-x) for x in a))
def heights(a):
    x,y,z=a
    return (0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
ROWS=[]
for x in range(-10,11):
    for y in range(-10,11):
        for z in range(-10,11):
            a=(x,y,z)
            if a>(-x,-y,-z) and port(a)<=10:
                H=heights(a)
                ROWS.append((a,tuple(abs(H[i]-H[j]) for i,j in PAIRS)))
assert len(ROWS)==1935

BASE={(1,0,0),(4,-1,0),(5,-4,1),(5,-1,0),(6,-4,1),(9,-5,1)}
V=(4,-1,0); B=(6,-4,1)
def expected(D):
    if D<=912:
        N=BASE
    elif D<=976:
        N=BASE|{(9,-2,0)}
    elif D<Q(6096,5):
        N=BASE|{(9,-2,0),(1,-3,1)}
    elif D<1536:
        N=BASE|{(9,-2,0)}
    elif D<11202:
        N={V,B}
    else:
        N={B}
    if D<=1008:
        eta=Q(1,96)
    elif D<=5771:
        eta=Q(11,D+48)
    elif D<=6923:
        eta=Q(12,D+577)
    elif D<=7452:
        eta=Q(1,625)
    else:
        eta=Q(12,D+48)
    return eta,N

SAMPLES=[
    Q(900),Q(912),Q(913),Q(976),Q(977),Q(1008),Q(1009),
    Q(6096,5)-Q(1,5),Q(6096,5),Q(6096,5)+Q(1,5),
    Q(1300),Q(1535),Q(1536),Q(1537),
    Q(5770),Q(5771),Q(5772),
    Q(6922),Q(6923),Q(6924),
    Q(7451),Q(7452),Q(7453),
    Q(11201),Q(11202),Q(11203),Q(50000)
]
out=[]
for D in SAMPLES:
    den=(Q(625),Q(288),D+48,Q(817),D+577,D+240)
    scores=[(max(Q(g,d) for g,d in zip(G,den)),a) for a,G in ROWS]
    eta=min(s for s,a in scores)
    near={a for s,a in scores if 2*s<3*eta}
    ex_eta,ex_near=expected(D)
    assert eta==ex_eta,(D,"eta",eta,ex_eta)
    assert near==ex_near,(D,"near",near^ex_near)
    out.append({"D":str(D),"eta":str(eta),"near_count":len(near),"minimizers":[list(a) for s,a in scores if s==eta]})
print(json.dumps({"status":"PASS","population":len(ROWS),"samples":len(SAMPLES),"comparisons":len(ROWS)*len(SAMPLES),"snapshots":out},ensure_ascii=False,indent=2))
