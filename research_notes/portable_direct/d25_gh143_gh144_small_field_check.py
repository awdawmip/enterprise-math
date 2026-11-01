#!/usr/bin/env python3
"""GH143/GH144: independent exhaustive finite-field fibre, elliptic and marked correlator checks."""
from collections import Counter


def check(p):
    # Choose the smallest nonsquare basis parameter in F_p, all computations exact.
    d=next(t for t in range(2,p) if pow(t,(p-1)//2,p)==p-1)
    K=[(a,b) for a in range(p) for b in range(p)]
    z=(0,0); one=(1,0)
    def add(x,y): return ((x[0]+y[0])%p,(x[1]+y[1])%p)
    def neg(x): return ((-x[0])%p,(-x[1])%p)
    def sub(x,y): return add(x,neg(y))
    def mul(x,y): return ((x[0]*y[0]+d*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    def sq(x):return mul(x,x)
    leg=[0]+[-1]*(p-1)
    for a in range(1,p):leg[a*a%p]=1
    def chi(x):return leg[(x[0]*x[0]-d*x[1]*x[1])%p]
    def scalar(x,n):return ((x[0]*n)%p,(x[1]*n)%p)
    inv4=pow(4,-1,p);c=(inv4,0);c2=(inv4*pow(2,-1,p)%p,0)
    F={t:0 for t in K}
    for x in K:
        t=neg(add(sq(x),x))
        F[t]+=chi(x)
    assert all(F[t]==F[sub(c,t)] for t in K)
    assert Counter(F.values())==Counter({2:(p*p-9)//8,-2:(p*p-1)//8,1:2,0:3*(p*p-1)//4})
    C={};curve={};Ms={}
    # Independently compute first weighted autocorrelation of a translated fibre.
    B=(3%p,1)
    mu={y:F[sub(B,y)] for y in K}
    for h in K:
        cv=sum(F[t]*F[add(t,h)] for t in K)
        assert cv==sum(mu[y]*mu[add(y,h)] for y in K)
        C[h]=cv
        if h==z: assert cv==p*p-3
        elif h==c or h==neg(c): assert cv==-3
        else:
            sm=0
            for u in K:
                poly=sub(sq(sub(h,u)),sq(sq(u)))
                sm+=chi(poly)
            assert cv==sm-1, (p,h,cv,sm-1)
            # Direct cubic curve trace, separate from quartic point count.
            Bh=scalar(sq(h),4)
            sf=sum(chi(mul(x,add(add(sq(x),x),Bh))) for x in K)
            assert cv==sf-2, (p,h,cv,sf-2)
            curve[h]=-sf
            assert abs(curve[h])<=2*p
        # First marked linear moment: sum y mu_B(y)mu_B(y+h).
        lhs=z
        for y in K:
            lhs=add(lhs,scalar(y,mu[y]*mu[add(y,h)]))
        rhs=scalar(sub(B,scalar(add(c,h),pow(2,-1,p))),cv)
        assert lhs==rhs, (p,h,lhs,rhs)
    assert sum(C.values())==0
    assert sum(curve.values())==-(p*p+3), (p,sum(curve.values()))
    zmark=z
    for y in K: zmark=add(zmark,scalar(y,mu[y]*mu[y]))
    assert zmark==scalar(sub(B,c2),p*p-3)
    assert scalar(sub(B,c2),-3)==zmark
    print('PASS_SMALL', 'p',p,'d',d,'q',p*p,'generic',len(curve),'C0',C[z], 'Cquarter',C[c],'trace_sum',sum(curve.values()),'mark',zmark)


if __name__=='__main__':
    for p in (5,7,11,13,19):check(p)
    print('PASS_GH143_GH144_SMALL_FIELD_ALL_EXACT')
