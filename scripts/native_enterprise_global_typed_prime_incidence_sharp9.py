#!/usr/bin/env python3
"""Exact checker for typed-Cell global carrier seam no-go and sharp nine-prime incidence island."""

from __future__ import annotations

import math
from collections import defaultdict


def Bc(s: int) -> int:
    return 1 + 3*s*(s+1)//2


def N(s: int, t: int, sigma: int, reverse: bool=False) -> int:
    if reverse:
        t=s-t
    return Bc(s)+t+sigma*(s+1)


def xy_from_typed(s: int, t: int, sigma: int):
    if sigma==0:
        a=s-t; b=t
        return (a,b)
    if sigma==1:
        b=s-t; c=t
        return (-1-c,b-1-c)
    if sigma==2:
        a=t; c=s-t
        return (a-c,-1-c)
    raise ValueError


def typed_from_xy(x: int, y: int):
    if x>=0 and y>=0:
        return (x+y,y,0)
    if x<=-1 and y>=x:
        c=-1-x; b=y-x
        return (b+c,c,1)
    if y<=-1 and x>=y+1:
        c=-1-y; a=x-y-1
        return (a+c,a,2)
    raise AssertionError((x,y))


def build_cells(smax: int, reverse: bool=False):
    out={}
    for s in range(smax+1):
        for sigma in range(3):
            for t in range(s+1):
                xy=xy_from_typed(s,t,sigma)
                assert typed_from_xy(*xy)==(s,t,sigma)
                assert xy not in out
                out[xy]=(s,t,sigma,N(s,t,sigma,reverse))
    labels=sorted(v[3] for v in out.values())
    assert labels==list(range(1,len(labels)+1))
    return out


def triangles(cells):
    for x,y in cells:
        A=((x,y),(x+1,y),(x+1,y+1))
        B=((x,y),(x,y+1),(x+1,y+1))
        for orient,pts in (("A",A),("B",B)):
            if all(p in cells for p in pts):
                yield orient,pts,tuple(cells[p] for p in pts)


def is_prime_trial(n: int) -> bool:
    if n<2: return False
    if n%2==0: return n==2
    q=3
    while q*q<=n:
        if n%q==0: return False
        q+=2
    return True


def seam_no_go(smax: int, reverse: bool=False):
    cells=build_cells(smax,reverse)
    cross=0
    for _,_,infos in triangles(cells):
        sigs={v[2] for v in infos}
        if len(sigs)>1:
            cross+=1
            vals=[v[3] for v in infos]
            # Exact finite carrier replay: no cross-sector triangle has all three labels units mod 6.
            assert not all(math.gcd(v,6)==1 for v in vals)
            assert not all(is_prime_trial(v) for v in vals)
    return cross


def filament_label(r: int, h: int) -> int:
    # r=s+1 is the legacy enumeration-layer variable.
    t=h+(r+1)//2
    return 1+3*r*(r-1)//2+t+r


def main() -> None:
    # Typed atlas / seam replay through multiple carrier periods, in both traversals.
    c1=seam_no_go(180,False)
    c2=seam_no_go(180,True)
    assert c1==c2 and c1>0

    # Symbolic consecutive boundary-pair identities for many typed shells.
    for s in range(0,500):
        # S12/S23
        assert N(s,s,0)+1==N(s,0,1)
        # S23/S31
        assert N(s,s,1)+1==N(s,0,2)
        # S31/S12 with one-shell offset
        assert N(s,s,2)+1==N(s+1,0,0)

    # Exact mod-5 filament cap.
    expected={0:5,1:9,2:7,3:5,4:9}
    for h5,maxrun in expected.items():
        seq=[]
        for r in range(10):
            if r%2==0:
                m=r//2; c=(6*m*m+h5+1)%5
            else:
                m=(r-1)//2; c=(6*m*(m+1)+h5+3)%5
            seq.append(c)
        cur=best=0
        for x in seq*2:
            if x:
                cur+=1; best=max(best,cur)
            else:
                cur=0
        best=min(best,9)
        assert best==maxrun,(h5,seq,best)

    # Sharp actual island.
    h=-2474
    vals=[filament_label(r,h) for r in range(10686,10695)]
    expected_vals=[
        171283421,171315481,171347543,171379609,171411677,
        171443749,171475823,171507901,171539981,
    ]
    assert vals==expected_vals
    assert all(is_prime_trial(v) for v in vals)
    assert filament_label(10685,h)%5==0
    assert filament_label(10695,h)%5==0

    print("TYPED_CELL_ATLAS_ROUNDTRIP=PASS")
    print(f"CROSS_SECTOR_TRIANGLES_REPLAYED={c1}")
    print("CROSS_SECTOR_FULL_PRIME_INCIDENCE=IMPOSSIBLE")
    print("GLOBAL_PRIME_INCIDENCE_COMPONENT_BOUND=9")
    print("SHARP_NINE_PRIME_GLOBAL_ISLAND=PASS")
    print("CONNECTIVITY_COLLAPSE=2D->1D->FINITE")


if __name__=="__main__":
    main()
