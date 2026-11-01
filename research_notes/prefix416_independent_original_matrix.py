#!/usr/bin/env python3
"""Independent original matrix and partial derivative checks for PREFIX-416."""
import sympy as s
I=s.I
A=s.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
u,v=s.symbols('u v')
initial=A[:3,:]
assert initial.det()!=0
w=initial.inv()*s.Matrix([1,u,v])
readouts=s.simplify(A*w)
a=(5+9*I)/2;b=(3+7*I)/2;d=(22+15*I)/8;e=(5+9*I)/4
assert [s.simplify(readouts[j]-[1,u,v,a+b*u+4*I*v,d*(1+u)+e*v][j]) for j in range(5)]==[0]*5
x,y=s.symbols('x y',real=True)
for sigma in (1,-1):
    ur=s.Rational(-1,2)+sigma*I/2
    us=s.Rational(1,2)
    z4=(a+b*sigma*I+4*I*(x+I*y)).expand()
    z5=(d*(1+sigma*I)+e*(x+I*y)).expand()
    I4=s.expand(s.conjugate(z4)*z4)
    k=s.expand(s.conjugate(z5)*z5)-s.Rational(709,32)
    if sigma==1:
        Ii=37+48*x+8*y+16*(x*x+y*y)
        ki=23*x+s.Rational(61,8)*y+s.Rational(53,8)*(x*x+y*y)
        dr=(-8*x+20*y-7, -s.Rational(61,16)*x+s.Rational(23,2)*y)
    else:
        Ii=45+24*x-48*y+16*(x*x+y*y)
        ki=s.Rational(61,8)*x-23*y+s.Rational(53,8)*(x*x+y*y)
        dr=(-20*x-8*y-3, -s.Rational(23,2)*x-s.Rational(61,16)*y)
    assert s.simplify(I4-Ii)==0 and s.simplify(k-ki)==0
    for du,(r4,rk) in [(ur,dr),(us,(14*x-6*y+s.Rational(39,2),s.Rational(245,32)*x-s.Rational(123,32)*y+s.Rational(709,64)))]:
        I4part=s.expand(s.conjugate(z4)*b*du+z4*s.conjugate(b*du))
        kpart=s.expand(s.conjugate(z5)*d*du+z5*s.conjugate(d*du))
        assert s.simplify(I4part-r4)==0
        assert s.simplify(kpart-rk)==0
print('PASS_PREFIX416_INDEPENDENT_RAW_PORT_INVERSION_AND_ALL_EIGHT_PARTIALS')
