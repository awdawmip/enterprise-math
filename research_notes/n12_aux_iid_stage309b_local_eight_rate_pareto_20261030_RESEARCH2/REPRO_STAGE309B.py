#!/usr/bin/env python3
"""Stage309-B: exact rational check of a sharp local Pareto interval.
The mathematical continuum proof is in PROOF_STAGE309B.md; this checks the
source model, signs and inequalities with Fraction (not a sampling proof).
"""
from fractions import Fraction as Q
from itertools import product
from math import comb
P0,T0=Q(11,256),Q(77,1024)
p0,p1=Q(1,4),Q(3,4)
weights={(0,0,0):(63,1),(0,0,1):(21,3),(0,1,0):(21,3),
         (0,1,1):(7,9),(1,0,0):(9,7),(1,0,1):(3,21),
         (1,1,0):(3,21),(1,1,1):(1,63)}

def bk(k,t):return t**k*(1-t)**(3-k)
def A(t):return 1-3*t*t+2*t**3
def q(u):return Q(9,128)*u+Q(3,32)*u*u-Q(1,8)*u**3
def g(u):return Q(117,4096)*u-Q(123,1024)*u*u+Q(23,256)*u**3
def H(u):
    z=p0+u
    return (63*((Q(3,4))**3-(Q(3,4)-u)**3)+(A(z)-A(p0)))/256

def score(table):
    P=T=Q(0)
    for w,y in product(range(2),repeat=2):
        for k in range(4):
            original=sum((a*bk(k,p0)+b*bk(k,p1) for (j,ww,yy),(a,b) in weights.items() if (ww,yy)==(w,y)),Q(0))/256
            compact=sum(((a+b)*bk(k,table[(j,w,y)]) for (j,ww,yy),(a,b) in weights.items() if (ww,yy)==(w,y)),Q(0))/256
            P+=Q(comb(3,k),2)*abs(original-compact)
    for h,(a,b) in weights.items():
        t=table[h]
        for k in range(4):
            T+=Q(comb(3,k),512)*(a*abs(bk(k,p0)-bk(k,t))+b*abs(bk(k,p1)-bk(k,t)))
    return P,T

def table(u):
    out={h:(p0 if a>b else p1) for h,(a,b) in weights.items()}
    out[(1,0,0)]=p0+u
    return out

def main():
    assert sum(a+b for a,b in weights.values())==256 and len(weights)==8
    assert all(a>0 and b>0 and a!=b for a,b in weights.values())
    assert score(table(Q(0)))==(P0,T0)
    assert q(Q(1,100))>Q(1,10000)
    for i in range(11):
        u=Q(i,1000)
        P,T=score(table(u))
        assert (P,T)==(P0-q(u),T0+g(u))
        assert Q(13,32)*q(u)-g(u)==Q(9,512)*u*u*(9-8*u)
        assert H(u) >= 4*q(u)
        if u: assert H(u)>4*q(u)
    margin=[Q(13,1024),Q(3,1024),Q(3,1024),Q(13,1024)]
    lips=[Q(2),Q(1,3),Q(1,3),Q(1,3)]
    for k in range(4): assert Q(5,16)*Q(1,100)*lips[k]<margin[k]
    assert min(abs(a-b) for a,b in weights.values())==2
    eps=Q(1,10000)
    assert Q(52)*eps<Q(1,100)
    for u in (Q(0),Q(1,100)):
        z=p0+u
        gp=(Q(3,4)-u)*(27*(Q(3,4)-u)-42*z)/256
        qp=6*z*(1-z)/16
        majp=(189*(Q(3,4)-u)**2-6*z*(1-z))/256
        qmajp=4*qp
        assert gp>0 and qp>0 and gp/qp<=Q(13,32)
        assert majp>qmajp
        assert Q(-123,512)+Q(69,128)*u<0
        assert Q(3,16)-Q(3,4)*u>0
    for u in (Q(1,1000),Q(1,900),Q(1,2000)):
        epsilon=q(u)
        assert 0<epsilon<Q(1,10000)
        P,T=score(table(u))
        assert P==P0-epsilon and T==T0+g(u)
        print('WITNESS u',u,'epsilon',epsilon,'P',P,'T',T)
    print('LOCAL_PARETO_DELTA',Q(1,10000))
    print('LOCAL_PARETO_PARAMETRIC_P', '11/256 - q(u)')
    print('LOCAL_PARETO_PARAMETRIC_T', '77/1024 + g(u)')
    print('CHECKED_RATIONAL_SIGN_AND_COST_COMPARISON_PASS')
    print('STAGE309B_LOCAL_EIGHT_RATE_PARETO_EXACT_PASS')
if __name__=='__main__':main()
