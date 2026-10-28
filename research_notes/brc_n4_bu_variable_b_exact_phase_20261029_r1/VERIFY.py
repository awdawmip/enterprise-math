#!/usr/bin/env python3
"""Exact symbolic and rational release checker. Universal proof: PROOF.md."""
from fractions import Fraction as F
import sympy as S
import json
a,b,z,A,B,c,U,V=S.symbols("a b z A B c U V")
s=(A-a+B-b)/2
t=(A-a+3*(B-b))/4
H=B*c/4
rQ=a*z/6-A*c/6-U/3-V/4
rP=a*z/6-A*c/6-U/S.Integer(12)-V/2
alpha=(c+4)/(23-2*c)
beta=(3-7*c)/(23-2*c)
gamma=2*(1+4*c-c*c)/(23-2*c)
eta=2*(c*c-2*c+7)/(23-2*c)
w1=7*(1-c)/20; w2=(7*c-3)/20
w3=(3*c+1)/10; w4=(7-3*c)/10
D=2*a*z-7*b; h=2*a+4*b
assert S.factor(alpha+beta+gamma+eta-1)==0
assert S.factor(w1+w2+w3+w4-1)==0
assert S.factor(alpha*(H-s-rQ)+beta*(H-s)+gamma*rP+eta*(t+rP)+7*alpha*(V-B)/4-(alpha*(D-h*c)+b*c)/4)==0
assert S.factor(w1*(H-s-rQ)+w2*(H-rQ)+w3*rP+w4*(t+rP)+S.Rational(7,20)*(V-B)-(D-(2*a-b)*c)/20)==0
def check(aa,bb,zz,AA,BB,cc,UU,VV):
    ss=(AA-aa+BB-bb)/2
    tt=(AA-aa+3*(BB-bb))/4
    HH=BB*cc/4
    rq=aa*zz/6-AA*cc/6-UU/3-VV/4
    rp=aa*zz/6-AA*cc/6-UU/12-VV/2
    Q=(ss,HH-ss-rq,rq,-HH)
    P=(tt,HH-tt-rp,rp,-HH)
    return max(sum(abs(x) for x in Q)/2,sum(abs(x) for x in P)/2)
n=0
for bb in (F(1,200),F(1,50),F(1,20),F(1,10),F(1,5),F(2,7),F(1,3),F(1,2),F(3,4),F(1)):
 for zz in (F(0),F(1,10),F(7,40),F(1,4),F(1,2),F(3,4),F(1)):
    if 2*zz<=7*bb:cc=F(0);UU=VV=2*zz/7
    else:cc=(2*zz-7*bb)/(2+4*bb);VV=bb;UU=bb*(1+cc)
    assert 0<=cc<=1 and 0<=UU<=1 and 0<=VV<=bb
    expected=bb*max(F(0),2*zz-7*bb)/(8*(1+2*bb))
    assert check(F(1),bb,zz,F(1),bb,cc,UU,VV)==expected
    n+=1
A0,B0,c0,U0,V0=F(41,80),F(1,48),F(4,5),F(23,700),F(17,1050)
assert check(F(1,2),F(1,40),F(1),A0,B0,c0,U0,V0)==F(1,240)<F(3,640)
print(json.dumps(dict(status="PASS_EXACT_BU_BIT_VARIABLE_B_RELEASE",symbolic_dual_residuals=[0,0],rational_witnesses=n,counterexample_tv="1/240"),ensure_ascii=False))
