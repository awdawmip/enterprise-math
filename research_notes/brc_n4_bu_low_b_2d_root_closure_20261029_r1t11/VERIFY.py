#!/usr/bin/env python3
"""Exact symbolic and rational checks for the low-b 2D BRC N4 BU root phase.
The continuum theorem follows from the analytic event-dual proof, not sampling.
"""
from fractions import Fraction as F
import sympy as S

a,b,c,A,B,U,V=S.symbols('a b c A B U V', real=True)
s=(A-a+B-b)/2; t=(A-a+3*(B-b))/4; H=B*c/4
rQ=a/6-A*c/6-U/3-V/4; rP=a/6-A*c/6-U/12-V/2
DQ=(s,H-s-rQ,rQ,-H);DP=(t,H-t-rP,rP,-H)
q1=s;q2=H-s-rQ;q3=H-rQ;q7=H;p4=rP;p5=t+rP;p6=H-t
l0=(4*a-14*b-3*a*c-(a+3*b)*c*c)/(2*(23-2*c))
l3=c*(a-(a+3*b)*c)/(2*(7-2*c))
k=b*c/(4+c)
f=(a+3*b)*c*c+(3*a+8*b)*c+14*b-4*a
# Each L_i is a convex mix of signed actual observable events plus a <=0 term.
w0=((c+4)*q2+(3-7*c)*(H-s)+2*(1+4*c-c*c)*p4+2*(c*c-2*c+7)*p5)/(23-2*c)
w3=(c*q3+7*(1-c)*q7+2*c*(2-c)*p4+2*c*c*p5)/(7-2*c)
wk=(c*q1+(4-2*c)*q7+2*c*p6)/(4+c)
assert S.cancel(l0-w0-7*(c+4)*(V-B)/(4*(23-2*c)))==0
assert S.cancel(l3-w3-7*c*(V-B)/(4*(7-2*c)))==0
assert S.cancel(wk-k)==0
assert S.cancel(l3-k+c*f/(2*(7-2*c)*(4+c)))==0
assert S.cancel(f.subs(c,S.Rational(3,7))+(124*a-881*b)/49)==0
assert S.expand(f.subs(c,1)-25*b)==0
# Explicit tight universal rectangle lower bounds: a >=97/100, b<=1/100.
corner={a:S.Rational(97,100),b:S.Rational(1,100),c:S.Rational(3,7)}
assert S.factor(l0.subs(corner))==S.Rational(73,1400)>S.Rational(1,500)
assert S.factor(l3.subs(corner))==S.Rational(1137,60200)>S.Rational(1,500)
assert S.cancel(S.diff(l0,a)-(4-3*c-c*c)/(2*(23-2*c)))==0
assert S.cancel(S.diff(l0,b)+(14+3*c*c)/(2*(23-2*c)))==0
assert S.cancel(S.diff(l3,a)-c*(1-c)/(2*(7-2*c)))==0
assert S.cancel(S.diff(l3,b)+3*c*c/(2*(7-2*c)))==0
assert 4-3*S.Rational(3,7)-S.Rational(3,7)**2>0
# The unique positive root c may be parameterized with b=b(c).
rb=a*(1-c)*(4+c)/(3*c*c+8*c+14)
hb=rb*c/(4+c)
assert S.cancel(f.subs(b,rb))==0
root={b:rb,A:a+3*hb,B:4*rb/(4+c),U:4*rb*(1+c)/(4+c),V:4*rb/(4+c)}
assert all(S.cancel(x.subs(root)-y)==0 for x,y in zip(DQ,(hb,0,0,-hb)))
assert all(S.cancel(x.subs(root)-y)==0 for x,y in zip(DP,(0,0,hb,-hb)))
# Prove L0 is decreasing on [0,3/7], L3 has endpoint minima there and beyond.
assert S.cancel(S.diff(l0,c)- (a*(2*c*c-46*c-61)+b*(6*c*c-138*c-28))/(2*(23-2*c)**2))==0
D=7*a-14*(a+3*b)*c+2*(a+3*b)*c*c
assert S.cancel(S.diff(l3,c)-D/(2*(7-2*c)**2))==0
assert S.cancel(S.diff(D,c)-4*(a+3*b)*(c-S.Rational(7,2)))==0

def fraction(sym):
    return F(int(S.fraction(sym)[0]),int(S.fraction(sym)[1]))
for av,cv in [(S.Rational(97,100),S.Rational(19,20)),
              (S.Rational(99,100),S.Rational(24,25)),
              (S.Rational(98,100),S.Rational(999,1000))]:
    bv=S.factor(rb.subs({a:av,c:cv}))
    ev=S.factor(hb.subs({a:av,c:cv}))
    assert 0<bv<=S.Rational(1,100)
    vals={a:av,b:bv,c:cv,A:S.factor((a+3*hb).subs({a:av,c:cv})),
          B:S.factor((4*rb/(4+c)).subs({a:av,c:cv})),
          U:S.factor((4*rb*(1+c)/(4+c)).subs({a:av,c:cv})),
          V:S.factor((4*rb/(4+c)).subs({a:av,c:cv}))}
    assert all(0<=vals[v]<=1 for v in (A,B,U,V))
    assert vals[U]<=vals[A] and vals[V]<=vals[B]
    Q=[S.factor(u.subs(vals)) for u in DQ]
    P=[S.factor(u.subs(vals)) for u in DP]
    assert Q==[ev,0,0,-ev] and P==[0,0,ev,-ev]
    print('LOW_B_RATIONAL_WITNESS', 'a=',av,'b=',bv,'c*=',cv,'TV_Q=TV_P=',ev)
print('RECTANGLE_ENDPOINT_CERTIFICATES','L0_3_7>=',S.Rational(73,1400),'L3_3_7>=',S.Rational(1137,60200),'root_e<=',S.Rational(1,500))
print('PASS_EXACT_BRC_N4_BU_LOW_B_2D_CLOSURE')
