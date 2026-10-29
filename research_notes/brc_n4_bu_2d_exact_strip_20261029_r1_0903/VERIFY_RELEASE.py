#!/usr/bin/env python3
"""Exact algebraic dual checks for BRC N4 BU 2D strip, see PROOF.md.
This release core is intentionally smaller than the independently run full
16-leaf Python Fraction witness/competitor checker in the archived evidence.
A PASS checks these identities, not mathematical admission or the real-domain
inequalities (proved in PROOF.md).
"""
import sympy as S

a,b,c,A,B,U,V=S.symbols("a b c A B U V",real=True)
s=(A-a+B-b)/2
t=(A-a+3*(B-b))/4
H=B*c/4
rQ=a/6-A*c/6-U/3-V/4
rP=a/6-A*c/6-U/12-V/2
Q1=s
Q2=H-s-rQ
Q3=H-rQ
Q7=H
P4=rP
P5=t+rP
P6=H-t

p=(c+4)/(23-2*c)
q=(3-7*c)/(23-2*c)
r=2*(1+4*c-c*c)/(23-2*c)
u=2*(c*c-2*c+7)/(23-2*c)
w1=7*(1-c)/20
w2=(7*c-3)/20
w3=(3*c+1)/10
w4=(7-3*c)/10
l1=c/(7-2*c)
l2=7*(1-c)/(7-2*c)
l3=2*c*(2-c)/(7-2*c)
l4=2*c*c/(7-2*c)
v1=c/(4+c)
v2=2*(2-c)/(4+c)
v3=2*c/(4+c)

L0=(4*a-14*b-3*a*c-(a+3*b)*c*c)/(2*(23-2*c))
L2=(2*a-7*b-(2*a-b)*c)/20
L3=c*(a-(a+3*b)*c)/(2*(7-2*c))
g=b*c/(4+c)
R=c*(a+3*b-1)/12

f=(a+3*b)*c*c+(3*a+8*b)*c+14*b-4*a
c0=(2*a-7*b)/(2*a+4*b)
c1=4*c0/(4-c0)
e0=b*c0/4
cp=(7-a-21*b)/(4*a+12*b+2)
ep=(a+3*b-1)*cp/12
G=5*a*a+8*a*b-21*b*b-2*b-5
beta=(S.sqrt(25+10*b+121*b*b)-4*b)/5
N2=22*a*a+(126*b-74)*a+180*b*b-495*b+70

tests={
"L0_dual":p*Q2+q*(H-s)+r*P4+u*P5+7*p*(V-B)/4-L0,
"L2_dual":w1*Q2+w2*Q3+w3*P4+w4*P5+S.Rational(7,20)*(V-B)-L2,
"L3_dual":l1*Q3+l2*Q7+l3*P4+l4*P5+7*c*(V-B)/(4*(7-2*c))-L3,
"g_dual":v1*Q1+v2*Q7+v3*P6-g,
"R_capacity":(1-c/3)*Q7+c*P6/3-R-c*(1-A)/12,
"L0_weights":p+q+r+u-1,
"L2_weights":w1+w2+w3+w4-1,
"L3_weights":l1+l2+l3+l4-1,
"g_weights":v1+v2+v3-1,
"L0_c0":L0.subs(c,c0)-e0,
"L3_c0":L3.subs(c,c0)-e0,
"g_c1":g.subs(c,c1)-e0,
"f_c1":f.subs(c,c1)-2*(2*a-7*b)*(16*a*a-50*a*b-329*b*b)/(6*a+23*b)**2,
"L3_c1":L3.subs(c,c1)-e0+(2*a-7*b)**2*(16*a*a-50*a*b-329*b*b)/(8*(a+2*b)*(6*a+23*b)*(26*a+217*b)),
"L0_c37":L0.subs(c,S.Rational(3,7))-e0-(2*a-b)*(8*a-61*b)/(280*(a+2*b)),
"L3_c37":L3.subs(c,S.Rational(3,7))-e0-(6*a-31*b)*(8*a-61*b)/(2408*(a+2*b)),
"L3_g_root":L3-g+c*f/(2*(7-2*c)*(4+c)),
"L3_R_capacity_cross":L3.subs(c,cp)-ep,
"f_cp_G":f.subs(c,cp)+3*(5*a+21*b)*G/(4*(2*a+6*b+1)**2),
"high_gap_G":3*ep-(1-a)-3*G/(8*(2*a+6*b+1)),
"beta_polynomial":G.subs(a,beta),
"capacity_root":f.subs(a,1-3*b*c/(4+c))-(c*c+(3+11*b)*c+14*b-4),
"L2_margin":L2.subs(c,S.Rational(3,4))-ep-N2/(240*(2*a+6*b+1)),
"L2_at_a1":N2.subs(a,1)-9*(b-2)*(20*b-1),
"cplus_endpoint":cp.subs({a:1,b:S.Rational(1,20)})-S.Rational(3,4),
"L3_derivative":S.diff(L3,c)-(7*a-14*(a+3*b)*c+2*(a+3*b)*c*c)/(2*(7-2*c)**2),
}
for label,value in tests.items():
    residue=S.factor(S.cancel(S.together(value)))
    if residue!=0:
        raise AssertionError((label,residue))
print("PASS_SYMBOLIC_BRC_N4_BU_2D_STRIP_RELEASE",len(tests),"identities")
