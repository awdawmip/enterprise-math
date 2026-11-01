#!/usr/bin/env python3
"""Exact symbolic checks of the new low-b observable dual and matching policy."""
import sympy as S
a,b,c,A,B,U,V=S.symbols('a b c A B U V',real=True)
s=(A-a+B-b)/2;t=(A-a+3*(B-b))/4;H=B*c/4
rQ=a/6-A*c/6-U/3-V/4;rP=a/6-A*c/6-U/12-V/2
DQ=S.Matrix((s,H-s-rQ,rQ,-H));DP=S.Matrix((t,H-t-rP,rP,-H))
f=(a+3*b)*c*c+(3*a+8*b)*c+14*b-4*a
K=b*c/(4+c);L3=c*(a-(a+3*b)*c)/(2*(7-2*c))
L0=(4*a-14*b-3*a*c-(a+3*b)*c*c)/(2*(23-2*c))
Q1=s;Q2=H-s-rQ;Q3=H-rQ;Q7=H;P4=rP;P5=t+rP;P6=H-t
p=(c+4)/(23-2*c);w=(3-7*c)/(23-2*c)
r=2*(1+4*c-c*c)/(23-2*c);v=2*(c*c-2*c+7)/(23-2*c)
l1=c/(7-2*c);l2=7*(1-c)/(7-2*c)
l3=2*c*(2-c)/(7-2*c);l4=2*c*c/(7-2*c)
assert S.cancel(c/(4+c)*Q1+(4-2*c)/(4+c)*Q7+2*c/(4+c)*P6-K)==0
assert S.cancel(L3-K+c*f/(2*(7-2*c)*(4+c)))==0
assert S.cancel(p*Q2+w*(H-s)+r*P4+v*P5+7*p*(V-B)/4-L0)==0
assert S.cancel(l1*Q3+l2*Q7+l3*P4+l4*P5+7*c*(V-B)/(4*(7-2*c))-L3)==0
W=4*b/(4+c);X=b*c/(4+c)
sub={A:a+3*X,B:W,U:W*(1+c),V:W}
for vec,target in ((DQ,S.Matrix((X,0,0,-X))),(DP,S.Matrix((0,0,X,-X)))):
    for z in vec.subs(sub,simultaneous=True)-target:
        num=S.cancel(z).as_numer_denom()[0]
        assert S.rem(S.Poly(num,c),S.Poly(f,c),domain=S.QQ.frac_field(a,b)).is_zero
A0=S.Rational(49,50);cap=(146-S.sqrt(10921))/1050;C=(139+S.sqrt(10921))/300
assert S.simplify(f.subs({a:A0,b:cap,c:C}))==0
assert S.simplify(cap*C/(4+C)-S.Rational(1,150))==0
cp=(7-A0-21*b)/(4*A0+12*b+2);ep=cp*(A0+3*b-1)/12
assert S.simplify(cp.subs(b,cap)-C)==0
assert S.simplify(L3.subs({a:A0,c:cp})-ep)==0
assert S.Rational(127,3500)>S.Rational(1,75)
assert S.Rational(507,30100)>S.Rational(1,75)
assert bool(S.simplify(cap>S.Rational(1,30)))
print('PASS_EXACT_BRC_N4_BU_FULL_B_AXIS_RELEASE')
