#!/usr/bin/env python3
"""Exact reverse-history corner: all-real two-tail rectangle lift."""
from fractions import Fraction as F

r0=F(1,10);r6=F(19,10)
# Frozen x=(g,a,b,u,v,w,z)=(1,1,1,0,9/40,0,0): R<0
x=(F(1),F(1),F(1),F(0),F(9,40),F(0),F(0))
# A separate seedless flow with identical stopping times.
y=(F(1),F(19,20),F(19,20),F(0),F(11,40),F(0),F(11,130))

def LR_tail(x):
    g,a,b,u,v,w,z=x
    m0=F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+F(1,100)*w
    m6=F(1,100)*u+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w
    return m0,m6

def T(x):
    g,a,b,u,v,w,z=x
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)

assert 9*x[2]*x[6]-4*x[1]*(x[4]-x[6])==-F(9,10)
assert 9*y[2]*y[6]-4*y[1]*(y[4]-y[6])==0
assert T(x)==T(y)==(F(129,40),F(129,40))
assert LR_tail(x)==(F(67,720),F(67,720))
assert LR_tail(y)==(F(121,1200),F(121,1200))
q=F(67,720)/F(121,1200)
assert q==F(335,363) and 0<q<1
# For ALL real s,t in [0,1], choose d_x0=s,d_x6=t;
# select d_y0=q*s,d_y6=q*t. Then both error coordinates coincide.
for s in (F(0),F(1,7),F(1,2),F(1)):
    for t in (F(0),F(2,5),F(3,4),F(1)):
        m0,m6=LR_tail(x);n0,n6=LR_tail(y)
        assert m0*s+m6*t==n0*(q*s)+n6*(q*t)
        assert r0*m0*s+r6*m6*t==r0*n0*(q*s)+r6*n6*(q*t)
        assert 0<=q*s<=1 and 0<=q*t<=1
print('REVERSE_CORNER_RESIDUAL',-F(9,10),'TIMES',T(x))
print('FULL_TAIL_MASSES',LR_tail(x),'SEEDLESS_TAIL_MASSES',LR_tail(y),'DECLARATION_SCALE',q)
print('PASS_REVERSE_CORNER_ALL_REAL_TWO_TAIL_RECTANGLE_EXPLICIT_LIFT')
