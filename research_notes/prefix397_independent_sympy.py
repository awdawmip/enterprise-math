#!/usr/bin/env python3
"""Independent SymPy audit of universal sextic and centered-polynomial implementation."""
from fractions import Fraction as F
import sympy as S
from prefix397_exact_checker import endpoint_poly,ROOT_BINS,R0,K0,S40,S50
z,r,k,s4,s5=S.symbols('z r k s4 s5')
R=1+z*z;U=r*(1-z*z);V=2*r*z
l4=56*U+24*V+72*R;m4=-24*U+56*V-40*R
n4=78*U-8*V+(32*k+29*r*r+53-2*s4)*R
l5=980*U+492*V+980*R;m5=-492*U+980*V-492*R
n5=1418*U+(424*k+709*r*r+709-64*s5)*R
D=S.expand(l4*m5-m4*l5);C=S.expand(m4*n5-m5*n4);T=S.expand(l5*n4-l4*n5)
H=S.expand(C*C+T*T-k*D*D)
G,rem=S.div(S.Poly(H,z),S.Poly(R,z))
assert rem.is_zero and G.degree()<=6
D2=(3776-4032*r*r)*R-256*r*(1-z*z)+47104*r*z
assert S.expand(D-R*D2)==0
shifts=((F(1,7000),-F(1,10000),F(1,8000),-F(1,12000)),
        (-F(1,24000),F(1,9000),-F(1,4000),F(1,18000)),(F(0),F(0),F(0),F(0)))
count=0
for lo,hi in ROOT_BINS:
    for zi in (lo,hi):
        op=endpoint_poly(zi)
        for shift in shifts:
            vals=[R0+shift[0],K0+shift[1],S40+shift[2],S50+shift[3]]
            values={z:S.Rational(zi.numerator,zi.denominator)}
            values.update({p:S.Rational(v.numerator,v.denominator) for p,v in zip((r,k,s4,s5),vals)})
            direct=H.subs(values)
            ours=sum(v*__import__('math').prod(shift[j]**key[j] for j in range(4)) for key,v in op.t.items())
            assert direct==S.Rational(ours.numerator,ours.denominator)
            count+=1
for zi in (ROOT_BINS[0][0],ROOT_BINS[-1][-1]):
    a,b,c,d=S.symbols('a b c d')
    vals={z:S.Rational(zi.numerator,zi.denominator),
          r:S.Rational(R0.numerator,R0.denominator)+a,
          k:S.Rational(K0.numerator,K0.denominator)+b,
          s4:S.Rational(S40.numerator,S40.denominator)+c,
          s5:S.Rational(S50.numerator,S50.denominator)+d}
    poly=S.Poly(H.subs(vals).expand(),a,b,c,d)
    independent={key:F(coeff.numerator,coeff.denominator) for key,coeff in poly.terms() if coeff}
    assert independent==endpoint_poly(zi).t
print('PASS_PREFIX397_INDEPENDENT_SYMPY_SEXTIC_AND_CENTERED_POLYNOMIAL',count)
