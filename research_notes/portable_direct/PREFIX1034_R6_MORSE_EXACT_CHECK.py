#!/usr/bin/env python3
"""Exact Morse data and symbolic cusp coefficients for frozen X6 six-phase spectral observer.
The script computes exact symbolic Hessian, Morse indices and cusp constants. It does
not implement a native Heartbeat/BRC time evolution; the five-angle quotient
is the already established auxiliary Haar/Laurent observer.
"""
from itertools import product
from collections import Counter
from sympy import Matrix, Rational, sqrt, pi, simplify

records=Counter()
for eps in product([-1,1],repeat=5):
    s=1+sum(eps)
    if s==0:
        continue # degenerate Y=0 critical set; out of this local theorem
    H=2*(Matrix(eps)*Matrix([eps])-s*Matrix.diag(*eps))
    # All s != 0 are nondegenerate. SymPy exactly certifies eigenvalue signs.
    eigs=H.eigenvals()
    negatives=0
    for eigenvalue,multiplicity in eigs.items():
        assert eigenvalue.is_real
        assert eigenvalue.is_negative in (True, False)
        negatives+= multiplicity if eigenvalue.is_negative else 0
    assert abs(H.det())==32*s**4
    records[(s*s, negatives, abs(H.det()))]+=1

expected={(4,3,512):15,(16,4,8192):6,(36,5,41472):1}
assert dict(records)==expected,(records,expected)

c4=simplify(Rational(15,1)/(3*sqrt(2)*pi**3*sqrt(512)))
c16=simplify(Rational(6,1)/(3*sqrt(2)*pi**3*sqrt(8192)))
assert simplify(c4-Rational(5,32)/pi**3)==0
assert simplify(c16-Rational(1,64)/pi**3)==0
H4=4**2*(36-4)**2;H16=16**2*(36-16)**2
A4=simplify(Rational(6,5)*H4*c4)
A16=simplify(Rational(6,5)*H16*c16)
assert simplify(A4-3072/pi**3)==0
assert simplify(A16-1920/pi**3)==0
print('Nonzero stationary strata (Y,negative Hessian index,abs det):')
for key in sorted(records):print(key,'count',records[key])
print('rho_cusp_coeff: v=4, negative left',c4,';v=16 positive right',c16)
print('g_cusp_coeff: v=4 positive left',A4,';v=16 positive right',A16)
print('PASS exact Hessian counts, determinants, signatures, and coefficients')
