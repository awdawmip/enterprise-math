#!/usr/bin/env python3
"""Independent SymPy reconstruction from original normalized five-Port matrix.
Algebraic checks only; continuous-domain signs are certified by the companion
Fraction checker and analytic proof, not by these symbolic identities alone.
"""
import sympy as S
I=S.I
a,b,x,y=S.symbols('a b x y',real=True)
u=a+I*b; v=x+I*y
z4=(5+9*I)/2+(3+7*I)*u/2+4*I*v
z5=(22+15*I)*(1+u)/8+(5+9*I)*v/4
r=a*a+b*b; s=(1+a)**2+b*b
F=S.expand_complex(z4*S.conjugate(z4)).expand()
k=S.expand_complex(z5*S.conjugate(z5)-S.Rational(709,32)).expand()
J=7-5*r+S.Rational(39,2)*s-4*b
PFx=36+28*a+12*b
PFy=-20-12*a+28*b
K0=S.Rational(709,64)*(s-2)
PKx=(245*(1+a)+123*b)/16
PKy=(-123*(1+a)+245*b)/16
assert S.simplify(F-J-PFx*x-PFy*y-16*(x*x+y*y))==0
assert S.simplify(k-K0-PKx*x-PKy*y-S.Rational(53,8)*(x*x+y*y))==0
assert S.simplify((PFx*x+PFy*y)-(8*S.im(z4.subs({x:0,y:0}))*x-8*S.re(z4.subs({x:0,y:0}))*y))==0

# Exact source-parametrized normal/tangent observer coefficients.
e,w=S.symbols('e w',real=True)
a0=-e;b0=-w
h_re=S.expand(S.re(z4.subs({x:0,y:0,a:a0,b:b0})))
h_im=S.expand(S.im(z4.subs({x:0,y:0,a:a0,b:b0})))
Jexp=41-S.Rational(49,2)*e+4*w
P0=PKx.subs({a:a0,b:b0});Q0=PKy.subs({a:a0,b:b0})
T=1226-705*e+61*w
g=4+59*e+368*w

# Reduce all expressions modulo the genuine algebraic relation w^2=1+e-e^2.
def reduce_w(expr):
    p=S.Poly(S.together(expr).expand(),w)
    relation=S.Poly(w*w-(1+e-e*e),w)
    return S.factor(p.rem(relation).as_expr())
assert reduce_w(h_re*h_re+h_im*h_im-Jexp)==0
assert reduce_w(-P0*h_im+Q0*h_re+T/8)==0
assert reduce_w(-P0*h_re-Q0*h_im-g/16)==0

# Exact Cayley-circle laws, with a symbolic unit normal and the two
# independently recovered fifth-observer normal/tangent values.
t,D,M,h,rho=S.symbols('t D M h rho',real=True,positive=True)
c=(1-t*t)/(1+t*t)
z=2*t/(1+t*t)
Fdelta=S.factor(8*h*rho*(1-c))
kdelta=S.factor(-M*(c-1)+D*z)
assert S.simplify(Fdelta-16*rho*h*t*t/(1+t*t))==0
assert S.simplify(kdelta-(2*D*t+2*M*t*t)/(1+t*t))==0
lam=16*h*rho*t/(D*(1-t*t)+2*M*t)
assert S.factor(lam*(D*c+M*z)-8*h*rho*z)==0
assert S.factor(lam*D*c-(8*h*rho-lam*M)*z)==0

print('PASS_PREFIX429_INDEPENDENT_RAW_FIVE_PORT_AND_DUAL_STATIONARITY')
print('IDENTITIES_CHECKED',10)
print('ORIGINAL_MODEL: z4 and z5 exact complex-affine observers; full F,k identities')
print('SOURCE_NORMAL_TANGENT: J, M, D algebraic laws modulo w^2=1+e-e^2')
print('RATIONAL_CIRCLE: fifth-port increment, fourth-port increment and dual multiplier')
