#!/usr/bin/env python3
"""Author independent symbolic audit of the GH-94 universal identity.
Requires SymPy. No native execution is represented.
"""
import sympy as sp
z=sp.symbols('z')
s0,s1,s2=sp.symbols('s0 s1 s2')
u0,u1,u2,u3=sp.symbols('u0 u1 u2 u3')

def B(y0,y1,y2):
    return ((1-z)*(y0*s2-y1*s1+y2*s0)
         +(z-3)*y0*s1/4
         +(3-5*z)*y1*s0/4
         +(2-7*z)*y0*s0/16)
H=8*u1+5*u0
J=8*u2+5*u1
T=8*s1+s0
K=8*(1-z)*s2+2*(z-3)*s1+(15*z+5)*s0/8
W=64*B(u1,u2,u3)+40*B(u0,u1,u2)
R=(z-1)*J*T+(2*(z+3)*J+(z+15)*u0/8)*s0+H*K
Lplus=(1-z)*u3+(3-9*z)*u2/4+(2-27*z)*u1/16-27*z*u0/64
assert sp.expand(W-R-64*s0*Lplus)==0
print('PASS_GH94_UNIVERSAL_SIGNED_SYZYGY_OVER_QZ_WITH_ARBITRARY_JETS')
