#!/usr/bin/env python3
"""Symbolic capacity identities and exact rational TV bound witnesses (external N4 BRC)."""
import json
from fractions import Fraction as F
import sympy as S

a,b,ca,cb,aa,bb,c,x,y=S.symbols('a b ca cb aa bb c x y', nonzero=True)
s=(aa-a+bb-b)/2
t=(aa-a+3*(bb-b))/4
zq=(a+b)/2-a*ca/6-b*cb/4-((aa+bb)/2-aa*c/6-bb*c/4-x-y)
zp=(a+3*b)/4-a*ca/6-b*cb/4-((aa+3*bb)/4-aa*c/6-bb*c/4-x/4-2*y)
ha=(a*ca-aa*c)/6
hb=(b*cb-bb*c)/4
r=b/a; R=a/b
GA=(3*b*(cb-ca)-7*a)/21
GB=(2*a*(ca-cb)-7*b)/28
EA=GA+(4+6*r)*ha/7+(1+c*(3*r+1))*s/7+(2-6*c*(r+1))*t/21+8*zq/7-4*zp/7
EB=GB+(3+2*R)*hb/7+(S.Rational(3,28)-c*(R+3)/14)*s+(S.Rational(1,14)+c*(R+1)/7)*t+4*zp/7-zq/7
assert S.cancel(x-aa/3-EA)==0
assert S.cancel(y-bb/4-EB)==0

def certify(a,b,ca,cb):
    r=b/a; R=a/b
    qA=max((4+6*r)/7,F(8,7)); pA=max(F(2,3),(6*r+4)/21)
    qB=(3+2*R)/7+max(F(1,7),(2*R+3)/28)
    pB=max(F(4,7),(2*R+3)/14)
    gA=max(F(0),(3*b*(cb-ca)-7*a)/21)
    gB=max(F(0),(2*a*(ca-cb)-7*b)/28)
    upper=(a/6)*(b/4)*abs(ca-cb)/(a/6+b/4)
    lowA=gA/(qA+pA);lowB=gB/(qB+pB)
    assert lowA<=upper and lowB<=upper
    return dict(parameters=[str(v) for v in (a,b,ca,cb)], AU_lower=str(lowA),BU_lower=str(lowB),S23_upper=str(upper))

samples=[certify(F(1,20),F(1),F(0),F(1)),certify(F(1),F(1,20),F(1),F(0))]
assert samples[0]['AU_lower']=='53/9920' and samples[0]['S23_upper']=='1/124'
assert samples[1]['BU_lower']=='33/6020' and samples[1]['S23_upper']=='1/86'
print(json.dumps({'status':'PASS_SYMBOLIC_BINARY_CAPACITY_IDENTITIES',
                  'scope':'two polynomial identities over rational functions; all real 0<a,b<=1 by algebraic proof and range-TV dual argument in PROOF.md',
                  'examples':samples,'admission':'UNREVIEWED_NOT_ADMITTED'},indent=2))
