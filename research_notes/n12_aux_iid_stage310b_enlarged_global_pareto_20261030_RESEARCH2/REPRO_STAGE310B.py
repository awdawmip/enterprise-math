#!/usr/bin/env python3
"""Stage310-B: exact-rational checks; continuum theorem is in PROOF_STAGE310B.md."""
from fractions import Fraction as Q
from itertools import product
from math import comb

r=Q(9,400); E=r/52
p0,p1=Q(1,4),Q(3,4)
P0,T0=Q(11,256),Q(77,1024)
weights={(0,0,0):(63,1),(0,0,1):(21,3),
         (0,1,0):(21,3),(0,1,1):(7,9),
         (1,0,0):(9,7),(1,0,1):(3,21),
         (1,1,0):(3,21),(1,1,1):(1,63)}
def B(k,z): return z**k*(1-z)**(3-k)
def q(u): return Q(9,128)*u+Q(3,32)*u*u-u**3/8
def g(u): return Q(117,4096)*u-Q(123,1024)*u*u+Q(23,256)*u**3
def table(u):
    t={h:(p0 if a>b else p1) for h,(a,b) in weights.items()}
    t[(1,0,0)]=p0+u
    return t
def score(t):
    P=T=Q(0)
    for w,y in product(range(2),repeat=2):
        for bits in product(range(2),repeat=3):
            k=sum(bits)
            original=sum((a*B(k,p0)+b*B(k,p1) for (j,ww,yy),(a,b) in weights.items() if (w,y)==(ww,yy)),Q(0))/256
            compact=sum(((a+b)*B(k,t[j,ww,yy]) for (j,ww,yy),(a,b) in weights.items() if (w,y)==(ww,yy)),Q(0))/256
            P+=abs(original-compact)/2
    for h,(a,b) in weights.items():
        for bits in product(range(2),repeat=3):
            k=sum(bits)
            T+=(a*abs(B(k,p0)-B(k,t[h]))+b*abs(B(k,p1)-B(k,t[h])))/512
    return P,T
def main():
    assert len(weights)==8 and sum(a+b for a,b in weights.values())==256
    assert all(a>0 and b>0 for a,b in weights.values())
    assert E==Q(9,20800)>Q(1,10000) and q(r)>E and 52*E==r
    L=[3*(Q(3,4)+r)**2,
       (Q(3,4)+r)*(Q(1,4)+3*r),
       (Q(1,4)+r)*(Q(5,4)-3*r),
       3*(Q(1,4)+r)**2]
    assert Q(1,4)+r<Q(1,3)
    margins=[Q(13,1024),Q(3,1024),Q(3,1024),Q(13,1024)]
    for k in range(4):
        v=Q(5,16)*r*L[k]
        assert v<margins[k]
        print("SIGN_MARGIN",k,"max_perturbation",v,"original_residual",margins[k])
    assert Q(3,16)-Q(3,4)*r>0
    assert -Q(123,512)+Q(69,128)*r<0
    assert Q(117,4096)-Q(123,512)*r+Q(69,256)*r*r>0
    assert 189*(p1-r)>390*(p0+r)
    assert Q(13,32)*q(r)-g(r)==Q(9,512)*r*r*(9-8*r)>0
    assert score(table(Q(0)))==(P0,T0)
    for u in (Q(1,200),Q(3,500)):
        eps=q(u); expected=(P0-eps,T0+g(u))
        assert Q(1,10000)<eps<E and u<r
        assert score(table(u))==expected
        print("NEW_WITNESS u",u,"epsilon",eps,"P",expected[0],"T",expected[1])
    print("INTERVAL_OLD_MAX",Q(1,10000))
    print("INTERVAL_NEW_MAX",E)
    print("INTERVAL_EXPANSION_FACTOR",E/Q(1,10000))
    print("STAGE310B_EXACT_RATIONAL_EXTENSION_PASS")
if __name__=="__main__": main()
