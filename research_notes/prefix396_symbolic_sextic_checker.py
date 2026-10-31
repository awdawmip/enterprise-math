#!/usr/bin/env python3
"""Independent SymPy polynomial-identity cross-check of the universal sextic reduction."""
import sympy as S
z,r,k,s4,s5=S.symbols('z r k s4 s5', real=True)
R=1+z*z
U=r*(1-z*z);V=2*r*z
l4=56*U+24*V+72*R
m4=-24*U+56*V-40*R
n4=78*U-8*V+(32*k+29*r**2+53-2*s4)*R
l5=980*U+492*V+980*R
m5=-492*U+980*V-492*R
n5=1418*U+(424*k+709*r**2+709-64*s5)*R
D=S.Poly(l4*m5-m4*l5,z)
C=S.Poly(m4*n5-m5*n4,z)
T=S.Poly(l5*n4-l4*n5,z)
H=C*C+T*T-k*D*D
G,rem=S.div(H,S.Poly(R,z))
assert rem.is_zero
assert G.degree()<=6
D2=(3776-4032*r*r)*R-256*r*(1-z*z)+47104*r*z
assert S.Poly(D.as_expr()-R*D2,z).is_zero
assert S.rem(C.as_expr(),R,z)==-3872*r*r*z-13984*r*r
assert S.rem(T.as_expr(),R,z)==-13984*r*r*z+3872*r*r
print('PASS_PREFIX396_INDEPENDENT_SYMPY_UNIVERSAL_SEXTIC_DEGREE_AND_DETERMINANT')
