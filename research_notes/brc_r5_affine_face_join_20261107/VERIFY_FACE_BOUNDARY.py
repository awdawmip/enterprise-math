#!/usr/bin/env python3
"""Exact Fraction verification of the R5 stopping-time extremal identity."""
from fractions import Fraction as F
Z=F(0)
# Coefficients ordered as (constant,g,a,b,u,v,w,z).
L=[Z,Z,-F(1,8),F(1,8),-F(1,2),Z,F(1,2),Z]  # T_P - T_Q.
R=[F(23,80),Z,-F(23,80)+F(13,80),F(19,160)+F(1,160),-F(1,2),Z,F(1,2),Z]
assert R==[F(23,80)]+L[1:]
g,a,b,u,v,w,z=F(1),F(1),Z,F(13,40),Z,Z,Z
assert 0<=a<=g<=1 and 0<=b<=g
assert 0<=u<=F(13,40)*a+b/80
assert 0<=w<=F(3,40)*a+F(21,80)*b
assert 0<=z<=a/10 and 0<=v-z<=F(9,40)*b
assert 9*b*z==4*a*(v-z)
tp=1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w
tq=1+g+(a+b)/2+u+v+w
assert (tp,tq)==(F(203,80),F(113,40))
assert tq-tp==F(23,80)
assert tp+F(1,10)==F(211,80)
print('PASS_R5_EXTREMAL_STOP_TIME_IDENTITY',str(tq-tp))
print('PASS_R5_FACE_F_OBSTRUCTION',str(tp),str(tp+F(1,10)))
