#!/usr/bin/env python3
"""Independent symbolic port inversion using only the original raw 5x3 matrix."""
import sympy as s
I=s.I
M=s.Matrix([
    [4,4,0],
    [0,-4,4],
    [-5+3*I,0,-3+I],
    [-2-2*I,4+4*I,2+2*I],
    [-2,0,5+2*I]
])
u,v=s.symbols('u v')
x,y=s.symbols('x y', real=True)
t=x*x+y*y
q=M[:3,:].inv()*s.Matrix([1,u,v]);out=s.simplify(M*q)
assert [s.expand(a) for a in out[:3]]==[s.Integer(1),u,v]
assert s.simplify(out[3]-((5+9*I)+(3+7*I)*u)/2-4*I*v)==0
assert s.simplify(out[4]-(22+15*I)*(1+u)/8-(5+9*I)*v/4)==0
for sign in [1,-1]:
    z4=s.expand(out[3].subs({u:sign*I,v:x+I*y}))
    z5=s.expand(out[4].subs({u:sign*I,v:x+I*y}))
    intensity=lambda z:s.expand_complex(z*s.conjugate(z)).expand()
    p=s.Rational(245+sign*123,16)
    q=s.Rational(-123+sign*245,16)
    a=48 if sign==1 else 24
    b=8 if sign==1 else -48
    j=37 if sign==1 else 45
    assert s.simplify(intensity(z4)-(j+a*x+b*y+16*t))==0
    assert s.simplify(intensity(z5)-s.Rational(709,32)-(p*x+q*y+s.Rational(53,8)*t))==0
assert s.expand((x*x+y*y)-t)==0
print('PASS original 5x3 matrix -> exact P4,P5 phase-fiber coefficients')
print('PASS_PREFIX420_INDEPENDENT_RAW_MATRIX_PROVENANCE')
