#!/usr/bin/env python3
"""Independent original five-Port matrix and coefficient checks using SymPy.
The original A_1:3 inverse is recomputed, not loaded from prior PREFIX notes.
"""
import sympy as sp
I=sp.I
A=sp.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
B=sp.simplify(A*A[:3,:].inv())
assert B[:3,:]==sp.eye(3)
a,b,c=[sp.expand_complex(B[3,i]).simplify() for i in range(3)]
d,e,f=[sp.expand_complex(B[4,i]).simplify() for i in range(3)]
assert (a,b,c)==(sp.Rational(5,2)+sp.Rational(9,2)*I,sp.Rational(3,2)+sp.Rational(7,2)*I,4*I)
assert (d,e,f)==(sp.Rational(11,4)+sp.Rational(15,8)*I,sp.Rational(11,4)+sp.Rational(15,8)*I,sp.Rational(5,4)+sp.Rational(9,4)*I)
assert sp.simplify(a*sp.conjugate(b))==sp.Rational(39,2)-2*I
assert sp.simplify(d*sp.conjugate(d))==sp.Rational(709,64)
x,y,r,s,j4=sp.symbols('x y r s j4',real=True)
u=x+I*y
f4=sp.expand_complex((a+b*u)*sp.conjugate(a+b*u)).expand().simplify()
f5=sp.expand_complex(d*(1+u)*sp.conjugate(d*(1+u))).expand().simplify()
assert sp.expand(f4-(sp.Rational(53,2)+sp.Rational(29,2)*(x*x+y*y)+39*x-4*y))==0
assert sp.expand(f5-sp.Rational(709,64)*((1+x)**2+y*y))==0
X=(s-1-r)/2
Y=(2*j4-14+10*r-39*s)/8
Delta=sp.factor(r-X**2-Y**2)
assert sp.expand(64*Delta-(64*r-16*(s-1-r)**2-(2*j4-14+10*r-39*s)**2))==0
# Two original coherent sources have identical first observables and different port4.
for sign,j in [(1,37),(-1,45)]:
    Yorig=sp.simplify(A[:3,:].inv()*sp.Matrix([1,sign*I,0]))
    physical=A*Yorig
    obs=[sp.simplify(physical[k]*sp.conjugate(physical[k])) for k in range(5)]
    assert obs==[1,1,0,j,sp.Rational(709,32)]  # original five Port intensities
    assert sp.simplify((1+sign*I)*(1-sign*I))==2
# Exact irrational phase source validates the algebraic (not only rational) domain.
t=sp.sqrt(2)
irr=(sp.Integer(2),sp.Integer(3),sp.Rational(111,2)-4*t)
assert sp.simplify(Delta.subs(dict(zip((r,s,j4),irr))))==0
assert sp.simplify(f4.subs({x:0,y:t})-irr[2])==0
print('row4:',a,b,c)
print('row5:',d,e,f)
print('polynomial_rank_defect:',sp.factor(64*Delta))
print('PASS_PREFIX407_INDEPENDENT_ORIGINAL_MATRIX_AND_ELIMINATION')
