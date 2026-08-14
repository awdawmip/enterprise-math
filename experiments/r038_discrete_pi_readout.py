#!/usr/bin/env python3
"""R038 independent exact FCC/HCP readout and replication checks.

Stdlib only. The enumerators do not call R033/R034 code.
All theorem-critical counts and squared radii use integers/Fraction.
"""

from collections import deque
from fractions import Fraction as F
import json

FCC_DIRS = (
    (0,-1,-1),(0,-1,1),(0,1,-1),(0,1,1),
    (-1,0,-1),(-1,0,1),(1,0,-1),(1,0,1),
    (-1,-1,0),(-1,1,0),(1,-1,0),(1,1,0),
)
TRI_DIRS=((1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1))

def fcc_ball(r):
    out=set()
    for x in range(-r,r+1):
        for y in range(-r,r+1):
            for z in range(-r,r+1):
                if (x+y+z)&1:
                    continue
                if abs(x)+abs(y)+abs(z) <= 2*r:
                    out.add((x,y,z))
    return out

def fcc_r2(p):
    x,y,z=p
    return F(x*x+y*y+z*z,2)

def hcp_neighbors(p):
    i,j,k=p
    same=[(i+a,j+b,k) for a,b in TRI_DIRS]
    shifts=((0,0),(1,0),(0,1)) if (k&1) else ((0,0),(-1,0),(0,-1))
    lower=[(i+a,j+b,k-1) for a,b in shifts]
    upper=[(i+a,j+b,k+1) for a,b in shifts]
    return tuple(same+lower+upper)

def hcp_ball(r):
    d={(0,0,0):0}
    q=deque([(0,0,0)])
    while q:
        p=q.popleft()
        if d[p] == r:
            continue
        for t in hcp_neighbors(p):
            if t not in d:
                d[t]=d[p]+1
                q.append(t)
    return set(d)

def hcp_r2(p):
    i,j,k=p
    s=F(1,3) if (k&1) else F(0)
    u=F(i)+s
    v=F(j)+s
    return u*u+u*v+v*v+F(2,3)*k*k

def fcc_A(r): return 1 if r==0 else 10*r*r+2
def fcc_V(r): return F(10*r**3+15*r*r+11*r+3,3)

def hcp_A(r):
    if r==0: return 1
    return F(21*r*r+(4 if r%2==0 else 3),2)

def hcp_V(r):
    return F(14*r**3+21*r*r+14*r+(4 if r%2==0 else 3),4)

def exposed(r): return 12*(3*r*r+3*r+1)

def fcc_M2(r):
    return F(r*(r+1)*(2*r+1)*(7*r*r+7*r+6),10)

def hcp_M2(r):
    # unified period-2 quasipolynomial
    return (
        F(721,480)*r**5 + F(721,192)*r**4 + F(581,144)*r**3
        + F(147,64)*r**2 + F(1619,2880)*r + F(3,128)
        + ((-1)**r)*F(38*r*r+38*r-9,384)
    )

def outside_count(ball, neighbors):
    return sum(1 for p in ball for q in neighbors(p) if q not in ball)

def fcc_neighbors(p):
    x,y,z=p
    return tuple((x+a,y+b,z+c) for a,b,c in FCC_DIRS)

def fs(x):
    x=F(x)
    return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"

def run():
    rows=[]
    for r in range(1,13):
        fb=fcc_ball(r)
        hb=hcp_ball(r)
        assert len(fb)==fcc_V(r)
        assert len(hb)==hcp_V(r)
        assert sum(1 for p in fb if max(max(map(abs,p)),sum(map(abs,p))//2)==r)==fcc_A(r)
        # HCP shell = B_r - B_{r-1}; avoids using a second distance implementation
        assert len(hb)-len(hcp_ball(r-1))==hcp_A(r)
        assert outside_count(fb,fcc_neighbors)==exposed(r)
        assert outside_count(hb,hcp_neighbors)==exposed(r)
        assert sum(fcc_r2(p) for p in fb)==fcc_M2(r)
        assert sum(hcp_r2(p) for p in hb)==hcp_M2(r)
        rows.append({
            "r":r,
            "fcc":{"A":fs(fcc_A(r)),"V":fs(fcc_V(r)),"M2":fs(fcc_M2(r))},
            "hcp":{"A":fs(hcp_A(r)),"V":fs(hcp_V(r)),"M2":fs(hcp_M2(r))},
            "exposed_both":exposed(r),
        })

    # independent larger HCP moment holdout
    for r in range(13,19):
        hb=hcp_ball(r)
        assert len(hb)==hcp_V(r)
        assert sum(hcp_r2(p) for p in hb)==hcp_M2(r)

    # R033 published r=100 holdout values
    assert fcc_A(100)==100002
    assert fcc_V(100)==3383701
    assert hcp_A(100)==105002
    assert hcp_V(100)==3552851
    assert exposed(100)==363612

    samples={}
    for r in (1,2,5,10,100):
        samples[str(r)]={
          "fcc_pi_A_graph":fs(F(fcc_A(r),4*r*r)),
          "fcc_pi_V_graph":fs(F(3,4*r**3)*fcc_V(r)),
          "hcp_pi_A_graph":fs(F(hcp_A(r),4*r*r)),
          "hcp_pi_V_graph":fs(F(3,4*r**3)*hcp_V(r)),
          "pi_A_unit_bond_both":fs(F(exposed(r),4*r*r)),
        }
    return {
      "schema":"R038_MACHINE_CHECK_V1",
      "checked_bfs_radii":"FCC/HCP r=1..12; HCP M2 holdout r=13..18",
      "r033_holdout":"r=100 formula values checked",
      "rows":rows,
      "samples":samples,
    }

if __name__=="__main__":
    print(json.dumps(run(),indent=2,sort_keys=True))
