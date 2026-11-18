#!/usr/bin/env python3
"""R270A: coupled-port exact rational BRC/adjugate checks."""
from fractions import Fraction as F
import json
def residue(x,m):
    assert x.denominator%13
    return x.numerator*pow(x.denominator,-1,m)%m
def port(w,r):
    x=F(1,10); a=w+r; det=1-a-x*x
    assert x>0 and 0<=a<1 and det>0
    return ((1/det,x/det),(x/det,(1-a)/det)),det
def check():
    s0,d0=port(F(1,5),F(53,100))
    s1,d1=port(F(33,100),F(53,100))
    assert (d0,d1)==(F(13,50),F(13,100))
    assert (s0[0][0],s1[0][0],s0[0][1],s1[0][1])==(F(50,13),F(100,13),F(5,13),F(10,13))
    rows=[]
    for n in range(1,9):
        P=13**n; M=100*P+1
        w0=F(1,5);w1=w0+F(P,M);r=F(79,100)-F(2*P,M)
        S0,D0=port(w0,r);S1,D1=port(w1,r)
        assert residue(w0,P)==residue(w1,P)
        assert (D0,D1)==(F(2*P,M),F(P,M))
        assert [residue(P*S[0][0],13) for S in (S0,S1)]==[7,1]
        assert [residue(P*S[0][1],13) for S in (S0,S1)]==[2,4]
        rows.append({'N':n,'M':M,'diagonal':[7,1],'off_diagonal':[2,4]})
    print(json.dumps({'status':'PASS','p':13,'two_port_coupling':'1/10',
       'checks':rows,'all_N':'symbolic theorem, finite tests are supporting checks'},indent=2))
if __name__=='__main__':check()
