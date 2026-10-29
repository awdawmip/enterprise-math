#!/usr/bin/env python3
"""Exact certificate checks for BRC N=4 BU observer, external finite model."""
from fractions import Fraction as F
import random
import sympy as S
a,b,c,A,B,U,V=S.symbols("a b c A B U V",real=True)
s=(A-a+B-b)/2; t=(A-a+3*(B-b))/4; H=B*c/4
rQ=a/6-A*c/6-U/3-V/4
rP=a/6-A*c/6-U/12-V/2
DQ=S.Matrix([s,H-s-rQ,rQ,-H])
DP=S.Matrix([t,H-t-rP,rP,-H])
cp=(7-a-21*b)/(4*a+12*b+2); ep=cp*(a+3*b-1)/12
Bp=(a+3*b-1)/3; Up=Bp*(1+cp)
c0=(2*a-7*b)/(2*a+4*b); e0=b*c0/4
G=5*a*a+8*a*b-21*b*b-2*b-5
N0=131*a*a+576*a*b-232*a+549*b*b-1746*b+245
L0=(4*a-14*b-3*a*c-(a+3*b)*c*c)/(2*(23-2*c))
L3=c*(a-(a+3*b)*c)/(2*(7-2*c))
R=c*(a+3*b-1)/12
Q2=H-s-rQ;Q3=H-rQ;Q7=H;P4=rP;P5=t+rP;P6=H-t
p=(c+4)/(23-2*c);q=(3-7*c)/(23-2*c)
r=2*(1+4*c-c*c)/(23-2*c);u=2*(c*c-2*c+7)/(23-2*c)
l1=c/(7-2*c);l2=7*(1-c)/(7-2*c);l3=2*c*(2-c)/(7-2*c);l4=2*c*c/(7-2*c)
identities={
"L0_event":p*Q2+q*(H-s)+r*P4+u*P6+7*p*(V-B)/4-L0,
"L3_event":l1*Q3+l2*Q7+l3*P4+l4*(t+rP)+7*c*(V-B)/(4*(7-2*c))-L3,
"R_capacity":(1-c/3)*Q7+c*P6/3-R-c*(1-A)/12,
"L0_weights":p+q+r+u-1,
"L3_weights":l1+l2+l3+l4-1,
"cap_Q":DQ.subs({A:1,B:Bp,c:cp,U:Up,V:Bp})-S.Matrix([(1-a)/3,ep-(1-a)/3,0,-ep]),
"cap_P":DP.subs({A:1,B:Bp,c:cp,U:Up,V:Bp})-S.Matrix([0,0,ep,-ep]),
"rational_Q":DQ.subs({A:a,B:b,c:c0,U:b*(1+c0),V:b})-S.Matrix([0,e0,0,-e0]),
"rational_P":DP.subs({A:a,B:b,c:c0,U:b*(1+c0),V:b})-S.Matrix([0,0,e0,-e0]),
"zero_Q":DQ.subs({A:a,B:b,c:0,U:2*a/7,V:2*a/7}),
"zero_P":DP.subs({A:a,B:b,c:0,U:2*a/7,V:2*a/7}),
"G_gap":3*ep-(1-a)-3*G/(8*(2*a+6*b+1)),
"L0_margin":L0.subs(c,S.Rational(3,7))-ep-N0/(840*(2*a+6*b+1)),
"L3_margin":L3.subs(c,S.Rational(3,7))-ep-(19*a+183*b-43)*(31*a+93*b-49)/(7224*(2*a+6*b+1)),
"L3_cp":L3.subs(c,cp)-ep,
"R_cp":R.subs(c,cp)-ep,
"cornerN":N0.subs({a:S.Rational(49,50),b:S.Rational(9,70)})-S.Rational(18926,30625),
"cornerG1":G.subs({a:S.Rational(49,50),b:S.Rational(3,50)})-S.Rational(48,625),
"cornerG2":G.subs({a:S.Rational(49,50),b:S.Rational(9,70)})-S.Rational(36,175),
"capVsRational":(ep-e0).subs(a,S.Rational(49,50))-7*(37500*b*b+8300*b-2107)/(4800*(75*b+37)*(100*b+49))}
for name,value in identities.items():
    if isinstance(value,S.MatrixBase):
        values=list(value)
    else:values=[value]
    for v in values:
        assert S.factor(S.cancel(S.together(v)))==0,(name,v)
print("PASS_CERTIFICATE_ALGEBRA",len(identities))

# Independent exact joint-observer check from all sixteen positive leaves.
q2={"AU":F(1,6),"AV":F(1,3),"BU":F(1,4),"BV":F(1,4)}
ratio={"AU":(F(9,10),F(11,10)),"AV":(F(1,4),F(1,4)),
       "BU":(F(1,5),F(9,5)),"BV":(F(2),F(2))}
leaves=[(path, q/4, q/4*ratio[path][i]) for path,q in q2.items() for i in range(2) for j in range(2)]
assert len(leaves)==16
assert sum(z[1] for z in leaves)==sum(z[2] for z in leaves)==1
assert all(q>0 and p>0 for _,q,p in leaves)
def obs(A,B,c,U,V):
    A,B,c,U,V=map(F,[A,B,c,U,V])
    assert 0<=A<=1 and 0<=B<=1 and 0<=c<=1 and 0<=U<=A and 0<=V<=B
    y={"AU":c,"BU":c,"AV":U/A if A else F(0),"BV":V/B if B else F(0)}
    result=[]
    for col in (1,2):
        v=[F(0)]*4
        for path,q,p in leaves:
            mass=(q,p)[col-1];x=A if path[0]=="A" else B;z=y[path]
            v[0]+=mass*(1-x)
            v[1]+=mass*x*(1-z)
            v[3 if path=="BU" else 2]+=mass*x*z
        assert sum(v)==1
        result.append(v)
    return result
def target(a,b):
    # AU's second-stage continuation is 1; all other second-stage rates 0.
    return obs(a,b,F(0),a,F(0))
def tv(x,y):
    return [sum(abs(u-v) for u,v in zip(p,q))/2 for p,q in zip(x,y)]
for a0 in (F(49,50),F(99,100),F(1)):
    for b0 in (F(3,50),F(2,25),F(1,8),F(9,70)):
        c0=(7-a0-21*b0)/(4*a0+12*b0+2)
        B0=(a0+3*b0-1)/3
        e0=c0*(a0+3*b0-1)/12
        assert tv(target(a0,b0),obs(1,B0,c0,B0*(1+c0),B0))==[e0,e0]
for a0,b0 in ((F(49,50),F(7,25)),(F(49,50),F(1,2)),(F(1,2),F(1,6)),(F(1),F(1))):
    assert tv(target(a0,b0),obs(a0,b0,0,2*a0/7,2*a0/7))==[0,0]
a0,b0=F(49,50),F(1,5)
assert tv(target(a0,b0),obs(a0,b0,F(14,69),F(83,345),b0))==[F(7,690),F(7,690)]
print("PASS_EXACT_16_LEAF",len(leaves),"rectangle_points=12","zero_points=4","counterexample=7/690")
