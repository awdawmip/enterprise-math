#!/usr/bin/env python3
"""Exact verification of 0<=s<=g<=1 extension of the R5 side-flow Blackwell rectangle."""
from fractions import Fraction as F
from itertools import product
from VERIFY import Z,O,U,R,masses,times,legal,seedless,QS,XS,YS,interpolate,check

def diag(m):
    return [[m[i] if i==j else Z for j in range(7)] for i in range(7)]

X0=(Z,Z,Z,Z,Z,Z,Z)
X1=(O,Z,Z,Z,Z,Z,Z)
Q0=diag(masses(X0))
Q1=diag(masses(X1))

def cone(g,s,p,q):
    assert 0<=s<=g<=1 and 0<=p<=1 and 0<=q<=1
    xr,yr,Qr=interpolate(p,q)
    weights=(1-g,g-s,s)
    xs=(X0,X1,xr);ys=(X0,X1,yr);qs=(Q0,Q1,Qr)
    x=tuple(sum(weights[k]*xs[k][j] for k in range(3)) for j in range(7))
    y=tuple(sum(weights[k]*ys[k][j] for k in range(3)) for j in range(7))
    Q=[[sum(weights[k]*qs[k][i][j] for k in range(3)) for j in range(7)] for i in range(7)]
    return x,y,Q

n=0
for g in (Z,F(1,3),F(4,5),O):
    for ratio,p,q in product((Z,F(1,2),O),(Z,F(1,2),O),(Z,F(1,3),O)):
        s=g*ratio
        x,y,Q=cone(g,s,p,q)
        assert x==(g,s,s,U*s*p,F(9,40)*s,U*s*q,Z)
        assert times(x)==(1+g+F(49,40)*s+U*s*p/2+F(3,2)*U*s*q,
                          1+g+F(49,40)*s+U*s*(p+q))
        assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
        check(x,y,Q)
        n+=1
print('PASS_R5_FOUR_PARAMETER_G_S_P_Q_CONE_EXACT',n,'RATIONAL_CASES')
print('ANALYTIC: all real 0<=s<=g<=1, 0<=p,q<=1 and d in [0,1]^7 by three-way affine transport interpolation')
