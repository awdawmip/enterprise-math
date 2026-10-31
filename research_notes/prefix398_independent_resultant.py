#!/usr/bin/env python3
"""Independent nominal coherent-observer resultant audit. Exact SymPy arithmetic."""
import sympy as s
z,q=s.symbols('z q')
P5=(247273497*z**5-45399147334*z**4+719077831171*z**3
    +1525709995366*z**2-179308209566*z-8362430980)
F=s.expand((3*z+2)*P5)
C=(441+z*z)-100*q*(1+z*z)
R=s.Poly(s.resultant(F,C,z),q,domain=s.QQ).primitive()[1]
assert R.degree()==6
assert s.rem(R.as_expr(),1300*q-3973,q)==0
_,fac=s.factor_list(R.as_expr())
assert sorted((s.degree(f,q),m) for f,m in fac)==[(1,1),(5,1)]
assert s.gcd(R,R.diff()).degree()==0
z0=s.Rational(-2,3)
assert F.subs(z,z0)==0
assert (s.Rational(441)+z0*z0)/(100*(1+z0*z0))==s.Rational(3973,1300)
assert R.eval(s.Rational(44101,10100))!=0
print('PASS_PREFIX398_INDEPENDENT_RESULTANT_IRREDUCIBILITY_AND_RATIONAL_SOURCE')
