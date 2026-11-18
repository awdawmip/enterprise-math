#!/usr/bin/env python3
"""R270 exact positive-rational one-port BRC resonance checks."""
from fractions import Fraction as F
import json
def local(x,m):
    x=F(x)
    assert x.denominator%13
    return x.numerator*pow(x.denominator,-1,m)%m
def star(w,r):
    assert 0<=w<1 and 0<=r and w+r<1
    return 1/(1-w-r)
def check():
    a,b,r=F(1,5),F(33,100),F(27,50)
    assert [local(w,13) for w in (a,b)]==[8,8]
    assert [star(w,r) for w in (a,b)]==[F(50,13),F(100,13)]
    assert [local(13*star(w,r),13) for w in (a,b)]==[11,9]
    evidence=[]
    for n in range(1,9):
        P=13**n; M=100*P+1
        w0=F(1,5);w1=w0+F(P,M);c=F(4,5)-F(2*P,M)
        assert local(w0,P)==local(w1,P)
        assert [star(w,c) for w in (w0,w1)]==[F(M,2*P),F(M,P)]
        assert [local(P*star(w,c),13) for w in (w0,w1)]==[7,1]
        assert local(w0,13*P)!=local(w1,13*P)
        evidence.append(dict(N=n,M=M,readouts=[7,1],status="PASS"))
    print(json.dumps(dict(status="PASS",p=13,example=[11,9],
          checked_family=evidence,
          all_N="symbolic theorem, not inferred from eight checks"),indent=2))
if __name__=="__main__":check()
