#!/usr/bin/env python3
"""All-real low-ratio p=1,q=0 two-wedge G/F proof checks.
Requires VERIFY.py and CERTIFICATES.json in the same directory; Fraction only."""
from fractions import Fraction as F
from VERIFY import E0,E1,anchor,source,diag,lin,mixq,check

def full(eta,theta):
    assert F(0)<=eta<=F(1,40) and F(0)<=theta<=1
    lam=40*eta
    upperG=1-lam/4
    lowerF=1-lam/3
    assert lowerF<=upperG
    def identity0(t):
        x=source(F(0),t)
        return x,x,diag(x)
    if theta<=upperG:
        a=identity0(F(0)); b=anchor("G0")
        lo=(lin(lam,a[0],b[0]),lin(lam,a[1],b[1]),mixq(lam,a[2],b[2]))
        a=identity0(F(1)); b=anchor("G34")
        hi=(lin(lam,a[0],b[0]),lin(lam,a[1],b[1]),mixq(lam,a[2],b[2]))
        t=theta/upperG
        x,y,q=(lin(t,lo[0],hi[0]),lin(t,lo[1],hi[1]),mixq(t,lo[2],hi[2]))
        assert y[2]==0 and y[4]==y[6]
    else:
        a=identity0(F(1)); b=anchor("F23")
        lo=(lin(lam,a[0],b[0]),lin(lam,a[1],b[1]),mixq(lam,a[2],b[2]))
        xx=source(eta,F(1)); hi=(xx,xx,diag(xx))
        t=(theta-lowerF)/(1-lowerF)
        x,y,q=(lin(t,lo[0],hi[0]),lin(t,lo[1],hi[1]),mixq(t,lo[2],hi[2]))
        assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
    assert x==source(eta,theta)
    return x,y,q

def scaled_full(eta,theta,g,s,h):
    assert 0<=s<=g<=1 and 0<=h<=1
    x,y,q=full(eta,theta)
    weights=(1-g,g-s,s)
    xx=tuple(sum(weights[k]*z[k] for k in range(3)) for z in zip(E0,E1,x))
    yy=tuple(sum(weights[k]*z[k] for k in range(3)) for z in zip(E0,E1,y))
    qs=(diag(E0),diag(E1),q)
    qq=tuple(tuple(sum(weights[k]*qs[k][i][j] for k in range(3)) for j in range(7)) for i in range(7))
    return lin(h,xx,yy),yy,mixq(h,qq,diag(yy))

def main():
    for name in ("G0","G34","F23"): check(*anchor(name))
    cases=0
    for eta in map(F,("0","1/1000","1/160","1/80","1/40")):
        lam=40*eta
        midG=1-lam/4; midF=1-lam/3
        thetas=sorted(set((F(0),F(1,4),F(1,2),F(3,4),F(7,8),F(9,10),F(19,20),F(1),midF,(midF+midG)/2,midG)))
        for theta in thetas:
            for g,s in ((F(0),F(0)),(F(1,2),F(1,4)),(F(1),F(1))):
                for h in (F(0),F(1,3),F(1)):
                    check(*scaled_full(eta,theta,g,s,h)); cases+=1
    print("ANCHORS_PASS 3")
    print("TWO_WEDGE_EXACT_GRID_PASS",cases)
    print("PASS_R5_P10_LOW_ETA_FULL_THETA_ALL_REAL_G_F_COVERAGE")
if __name__=="__main__": main()
