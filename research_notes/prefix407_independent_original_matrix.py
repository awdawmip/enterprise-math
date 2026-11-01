#!/usr/bin/env python3
"""PREFIX-407 independent SymPy verification using original A rows."""
import sympy as sp
I=sp.I
A=sp.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
B=sp.simplify(A*A[:3,:].inv())
assert B[:3,:]==sp.eye(3)
a,b,c=list(B[3,:]); d,e,f=list(B[4,:])
assert [sp.simplify(z) for z in [a-(sp.Rational(5,2)+sp.Rational(9,2)*I),b-(sp.Rational(3,2)+sp.Rational(7,2)*I),c-4*I,d-(sp.Rational(11,4)+sp.Rational(15,8)*I),e-d,f-(sp.Rational(5,4)+sp.Rational(9,4)*I)]]==[0]*6
x,y,r,s,j=sp.symbols("x y r s j",real=True)
u=x+I*y
abs2=lambda z:sp.expand_complex(z*sp.conjugate(z)).expand()
f4=sp.expand(abs2(a+b*u))
f5=sp.expand(abs2(d*(1+u)))
assert sp.simplify(f4-(sp.Rational(53,2)+sp.Rational(29,2)*(x*x+y*y)+39*x-4*y))==0
assert sp.simplify(f5-sp.Rational(709,64)*((1+x)**2+y*y))==0
X=(s-1-r)/2; Y=(2*j-14+10*r-39*s)/8
D=64*r-16*(s-1-r)**2-(2*j-14+10*r-39*s)**2
assert sp.expand(D-64*(r-X**2-Y**2))==0
for sign,j4 in [(1,37),(-1,45)]:
    originalY=A[:3,:].inv()*sp.Matrix([1,sign*I,0])
    readouts=A*originalY
    assert [sp.simplify(abs2(readouts[k])) for k in range(5)]==[1,1,0,j4,sp.Rational(709,32)]
t=sp.sqrt(2)
assert sp.simplify(D.subs({r:2,s:3,j:sp.Rational(111,2)-4*t}))==0
print("PASS_PREFIX407_INDEPENDENT_ORIGINAL_MATRIX_AND_ELIMINATION")
