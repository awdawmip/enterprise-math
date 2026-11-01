#!/usr/bin/env python3
"""Symbolic release checks of BRC N4 BU true 2D capacity switch (SymPy required).
This release is shorter than locally executed full sixteen-leaf verifier.
"""
import sympy as S
a,b,c,A,B,U,V=S.symbols('a b c A B U V',real=True)
H=B*c/4
s=(A-a+B-b)/2
t=(A-a+3*(B-b))/4
rq=a/6-A*c/6-U/3-V/4
rp=a/6-A*c/6-U/12-V/2
f=(a+3*b)*c*c+(3*a+8*b)*c+14*b-4*a
G=5*a*a+8*a*b-21*b*b-2*b-5
K=b*c/(4+c)
L0=(4*a-14*b-3*a*c-(a+3*b)*c*c)/(2*(23-2*c))
L3=c*(a-(a+3*b)*c)/(2*(7-2*c))
R=c*(a+3*b-1)/12
cp=(7-a-21*b)/(4*a+12*b+2)
ec=cp*(a+3*b-1)/12
q2=H-s-rq
p4=rp
p5=t+rp
w0=(c+4,3-7*c,2*(1+4*c-c*c),2*(c*c-2*c+7))
w3=(c,7*(1-c),2*c*(2-c),2*c*c)
checks={
 'K_event':(c*s+(4-2*c)*H+2*c*(H-t))/(4+c)-K,
 'L3_minus_K':L3-K+c*f/(2*(7-2*c)*(4+c)),
 'L0_event':(w0[0]*q2+w0[1]*(H-s)+w0[2]*p4+w0[3]*p5)/(23-2*c)+7*(c+4)*(V-B)/(4*(23-2*c))-L0,
 'L3_event':(w3[0]*(H-rq)+w3[1]*H+w3[2]*p4+w3[3]*p5)/(7-2*c)+7*c*(V-B)/(4*(7-2*c))-L3,
 'R_event':(1-c/3)*H+(c/3)*(H-t)-c*(a+3*b-A)/12,
 'L0_weight':sum(w0)/(23-2*c)-1,
 'L3_weight':sum(w3)/(7-2*c)-1,
 'L0_endpoint':L0.subs(c,S.Rational(3,7))-(124*a-713*b)/2170,
 'L3_endpoint':L3.subs(c,S.Rational(3,7))-3*(4*a-9*b)/602,
 'L3_cap':L3.subs(c,cp)-R.subs(c,cp),
 'G_cap':ec-(1-a)/3-G/(8*(2*a+6*b+1)),
 'f_cap':f.subs(c,cp)+3*(5*a+21*b)*G/(4*(2*a+6*b+1)**2),
 'f_3_4':f.subs(c,S.Rational(3,4))+(19*a-347*b)/16,
 'f_one':f.subs(c,1)-25*b,
}
for name,value in checks.items():
 assert S.cancel(value)==0,(name,S.factor(value))
BR=(4*a-1-S.sqrt(121*a*a-8*a-104))/21
for a0 in (S.Rational(979,1000),S.Rational(49,50),S.Rational(981,1000)):
 beta=S.N(BR.subs(a,a0),25)
 assert S.Rational(3,100)<beta<S.Rational(1,20)
 print('beta',a0,beta)
print('PASS_SYMBOLIC_BRC_N4_BU_2D_SWITCH_RELEASE')
