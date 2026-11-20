#!/usr/bin/env python3
"""Independent symbolic derivation of the 8-price overlap first-cost GF.
Requires sympy only for this optional crosscheck; VERIFY.py uses stdlib.
"""
import sympy as s
z,u,v=s.symbols("z u v")
D=lambda x,f:s.expand(x*s.diff(f,x))
G=((1-z*v)**-2 +z*u*(1+z*v)/((1-z*u)*(1-z*v)))/(1-z*z*u*v*v)
T=lambda f:(D(u,D(u,f))+3*D(u,f)+2*f)/2
G0=s.cancel(T(G).subs([(u,1),(v,1)]))
H=s.cancel((s.Rational(429,2)*D(v,T(G))+220*D(u,T(G))).subs([(u,1),(v,1)]))
I012=s.cancel(G0/(1-z)**4)
L012=s.cancel(H/(1-z)**4+651*z*I012/(1-z))
F=(1-z)**-3
A=F+D(z,F)+z*F/(1-z)
B=(D(z,D(z,F))+D(z,F))/2+z*(D(z,F)+F)/(1-z)+z*z*F/(1-z)**2
C=D(z,D(z,F))+D(z,F)+z*D(z,F)/(1-z)
L01_02=s.cancel((1731*z*A/(1-z)+429*B+440*C)/(1-z)**5)
L12=z*(2169+1740*z)/(1-z)**10
K=s.factor(2*(1+3*z)/(1-z)**9+(1+z)/(1-z)**9-I012)
L=s.factor(L01_02+L12-L012)
expect_K=(2+13*z+24*z**2+20*z**3+6*z**4)/((1-z)**9*(1+z)**3)
expect_L=3*z*(2172+12528*z+28819*z**2+31570*z**3+17665*z**4+3909*z**5)/((1-z)**10*(1+z)**4)
assert s.cancel(K-expect_K)==0
assert s.cancel(L-expect_L)==0
print("PASS exact rational identities: K_m and first cost-moment Z_m")
print("Z(z) =",L)
