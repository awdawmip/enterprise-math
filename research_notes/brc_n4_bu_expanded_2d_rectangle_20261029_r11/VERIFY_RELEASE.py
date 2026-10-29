#!/usr/bin/env python3
"""Concise exact algebra checks for the published BRC N=4 rectangle proof."""
import sympy as S
a,b,c,A,B,U,V=S.symbols("a b c A B U V")
s=(A-a+B-b)/2;t=(A-a+3*(B-b))/4;H=B*c/4
rq=a/6-A*c/6-U/3-V/4;rp=a/6-A*c/6-U/12-V/2
Q=[s,H-s-rq,rq,-H];P=[t,H-t-rp,rp,-H]
Q2=Q[1];Hs=H-s;P4=P[2];P5=P[0]+P[2]
Q3=Q[0]+Q[1];Q7=sum(Q[:3]);P6=P[1]+P[2]
L0=(4*a-14*b-3*a*c-(a+3*b)*c**2)/(2*(23-2*c))
L3=c*(a-(a+3*b)*c)/(2*(7-2*c))
K=b*c/(4+c);R=c*(a+3*b-1)/12
W0=((c+4)*Q2+(3-7*c)*Hs+2*(1+4*c-c*c)*P4+2*(c*c-2*c+7)*P5)/(23-2*c)
W3=(c*Q3+7*(1-c)*Q7+2*c*(2-c)*P4+2*c*c*P5)/(7-2*c)
assert S.cancel(L0-W0-7*(c+4)*(V-B)/(4*(23-2*c)))==0
assert S.cancel(L3-W3-7*c*(V-B)/(4*(7-2*c)))==0
assert S.cancel((1-c/3)*Q7+c*P6/3-c*(a+3*b-A)/12)==0
assert S.cancel((c*Q[0]+(4-2*c)*Q7+2*c*P6)/(4+c)-K)==0
f=(a+3*b)*c*c+(3*a+8*b)*c+14*b-4*a
G=5*a*a+8*a*b-21*b*b-2*b-5
cc=(7-a-21*b)/(4*a+12*b+2);ep=cc*(a+3*b-1)/12
N0=131*a*a+576*a*b-232*a+549*b*b-1746*b+245
assert S.cancel(L3-K+c*f/(2*(7-2*c)*(4+c)))==0
assert S.cancel(L3.subs(c,cc)-ep)==0
assert S.cancel(ep-(1-a)/3-G/(8*(2*a+6*b+1)))==0
assert S.cancel(L0.subs(c,S.Rational(3,7))-ep-N0/(840*(2*a+6*b+1)))==0
assert S.cancel(L3.subs(c,S.Rational(3,7))-ep-(19*a+183*b-43)*(31*a+93*b-49)/(7224*(2*a+6*b+1)))==0
aa=S.Rational(97,100); bb=S.Rational(1,8)
assert N0.subs({a:aa,b:bb})==S.Rational(135441,40000)
assert cc.subs({a:S.Rational(99,100),b:bb})==S.Rational(677,1492)
assert G.subs({a:S.Rational(99,100),b:S.Rational(1,100)})==-S.Rational(53,1250)
assert G.subs({a:aa,b:S.Rational(7,100)})==S.Rational(3,625)
assert S.cancel(f.subs(c,S.Rational(3,7))+(124*a-881*b)/49)==0
print("PASS_SYMBOLIC_BU_N4_EXPANDED_2D_RECTANGLE_RELEASE")
