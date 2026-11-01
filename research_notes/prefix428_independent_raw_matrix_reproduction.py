#!/usr/bin/env python3
"""Independent reconstruction directly from z4,z5 (SymPy)."""
import sympy as S
a,b,x,y,t=S.symbols('a b x y t',real=True)
D,M,delta,rho,h=S.symbols('D M delta rho h',positive=True)
u=a+S.I*b; v=x+S.I*y
H=(5+9*S.I)/2+(3+7*S.I)*u/2
z4=H+4*S.I*v
z5=(22+15*S.I)*(1+u)/8+(5+9*S.I)*v/4
F=S.expand(z4*S.conjugate(z4))
k=S.expand(z5*S.conjugate(z5)-S.Rational(709,32))
A=S.re(H.expand());B=S.im(H.expand())
P=(245*(1+a)+123*b)/16
Q=(-123*(1+a)+245*b)/16
J=S.expand(H*S.conjugate(H))
assert S.simplify(F-J-16*(x*x+y*y)-8*B*x+8*A*y)==0
assert S.simplify(k-S.Rational(709,64)*((1+a)**2+b*b-2)-P*x-Q*y-S.Rational(53,8)*(x*x+y*y))==0
assert S.simplify(J-(7-5*(a*a+b*b)+S.Rational(39,2)*((1+a)**2+b*b)-4*b))==0
e,w=S.symbols('e w',real=True)
AA=(5-3*e+7*w)/2;BB=(9-7*e-3*w)/2
PP=(245*(1-e)-123*w)/16
QQ=(-123*(1-e)-245*w)/16
T=1226-705*e+61*w;g=4+59*e+368*w
mod=w*w-(1+e-e*e)
assert S.rem(S.expand(PP*BB-QQ*AA-T/8),mod,w)==0
assert S.rem(S.expand(-PP*AA-QQ*BB-g/16),mod,w)==0
co=(1-t*t)/(1+t*t); si=2*t/(1+t*t)
assert S.simplify(rho*((-M/rho)*(co-1)+(D/rho)*si)-(2*D*t+2*M*t*t)/(1+t*t))==0
assert S.simplify(8*rho*h*(1-co)-16*rho*h*t*t/(1+t*t))==0
z=S.symbols('z',real=True)
poly=(delta-M*z)**2-D**2*(2*z-z*z)
zexact=delta**2/(D**2+M*delta+D*S.sqrt(D**2+2*M*delta-delta**2))
assert S.simplify(poly.subs(z,zexact))==0
gap=8*rho*h*delta**2/(D**2+M*delta+D*S.sqrt(D**2+2*M*delta-delta**2))
series=S.series(gap,delta,0,5).removeO().expand()
assert S.simplify(series.coeff(delta,2)-4*rho*h/D**2)==0
assert S.simplify(series.coeff(delta,3)+4*rho*h*M/D**4)==0
assert S.simplify(series.coeff(delta,4)-rho*h*(D**2+5*M**2)/D**6)==0
print('PREFIX428_INDEPENDENT_RAW_MATRIX_SYMBOLIC_PASS')
