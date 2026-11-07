#!/usr/bin/env python3
"""Check shared variable/observer domain and exact radical minimax bridge."""
import sympy as s
A,B,c,U,V=s.symbols('A B c U V',real=True)
a,b=s.Rational(961,1000),s.Rational(151,1000)
P1=(a-A+3*(b-B))/4
Q1=(a-A+b-B)/2
P3=(A*c-a)/6+U/12+V/2
Q3=(A*c-a)/6+U/3+V/4
h=B*c/4
sourceP=((A-a+3*(B-b))/4, h-(A-a+3*(B-b))/4-(a-A*c)/6+U/12+V/2,
         (a-A*c)/6-U/12-V/2, -h)
sourceQ=((A-a+B-b)/2, h-(A-a+B-b)/2-(a-A*c)/6+U/3+V/4,
         (a-A*c)/6-U/3-V/4, -h)
newP=(P1,-P1-P3-h,P3,h)
newQ=(Q1,-Q1-Q3-h,Q3,h)
assert all(s.factor(x+y)==0 for x,y in zip(sourceP,newP))
assert all(s.factor(x+y)==0 for x,y in zip(sourceQ,newQ))
# Existing causal reduction's c is exactly the common conditional rate u.
p=1414*c*c+4091*c-1730
r=(s.sqrt(26521161)-4091)/2828
E=s.sqrt(26521161)/15000-s.Rational(413,1250)
assert s.simplify(p.subs(c,r))==0
AA=(1414*r+1033)/(250*(7-2*r))
BB=(961-1414*r)/(500*(7-2*r))
UU=(1+r)*BB
sub={A:AA,B:BB,U:UU,V:BB,c:r}
assert all(s.simplify(z)==0 for z in (newP[0].subs(sub),newP[1].subs(sub),newP[2].subs(sub)+E,
                                      newP[3].subs(sub)-E,newQ[0].subs(sub)+E,newQ[1].subs(sub),
                                      newQ[2].subs(sub),newQ[3].subs(sub)-E))
print('PASS_BRIDGE_OLD_TARGET_MINUS_VS_NEW_CANDIDATE_MINUS')
print('PASS_COMMON_CONDITIONAL_RATE_AND_4_ATOM_MODEL')
print('PASS_EXACT_ATTAINMENT',s.simplify(E))
