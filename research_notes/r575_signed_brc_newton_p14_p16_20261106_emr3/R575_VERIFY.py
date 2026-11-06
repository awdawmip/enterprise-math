#!/usr/bin/env python3
"""R575: signed BRC auxiliary Newton p14,p16 exact certificate.
Frozen source: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f.
Continuation: R574@2860e9a1596027fba449e3ce2522a985e9519bea.
Only stdlib+SymPy, exact rational/integer acceptance conditions.
"""
from fractions import Fraction
from math import comb, factorial
import sympy as S

k, u = S.symbols('k u', integer=True)

def choose(n, t):
    return comb(n, t) if 0 <= t <= n else 0

def catalan(n):
    return comb(2*n, n)//(n+1)

def H_catalan(n, s):
    r = 2*n+1
    if s < 2 or s > r:
        return 0
    return choose(r+s, 2*s)*sum(choose(s-1, 2*q)*4**q*catalan(n-q)
                                    for q in range(min(n, (s-1)//2)+1))

def H_signed_convolution(n, s):
    """Independent integer coefficient extraction from frozen signed BRC."""
    r = 2*n+1
    if s < 2 or s > r:
        return 0
    return choose(r+s, 2*s)*sum(choose(r-s,b)*
         (choose(2*s, r-2*b)-choose(2*s, r-2*b-1))
         for b in range(r-s+1))

def A_poly(j):
    """Fixed-j rational-polynomial H_k(j+2)/H_k(2), Catalan ratio eliminated."""
    b = (S.Rational(24, factorial(2*j+4))
         * S.prod(2*k+a for a in range(4,j+4))
         * S.prod(2*k-1-a for a in range(j)))
    def ratio(q):
        return S.prod((k-v+1)/(2*(2*(k-v)-1)) for v in range(q))
    bracket = sum(comb(j+1,2*q)*4**q*ratio(q)
                  for q in range((j+1)//2+1))
    return S.Poly(S.cancel(b*bracket), k, domain=S.QQ)

A = {}
p = {}
for m in range(1,17):
    A[m] = A_poly(m)
    p[m] = -sum(((-1)**j*A[j]*p[m-j] for j in range(1,m)),
                S.Poly(0,k,domain=S.QQ)) - m*(-1)**m*A[m]
    assert p[m].degree()==2*m, m

def all_shift_coeff_sign(m, start, sign):
    cs = S.Poly(p[m].as_expr().subs(k,u+start), u, domain=S.QQ).all_coeffs()
    assert len(cs)==2*m+1
    assert all(sign*x > 0 for x in cs)
    return len(cs)

n14=all_shift_coeff_sign(14,3,+1)
n16=all_shift_coeff_sign(16,7,-1)
assert p[14].eval(2)>0
assert all(p[16].eval(n)>0 for n in range(2,7))
assert all(p[16].eval(n)<0 for n in range(7,17))

# Independent arithmetic checks, including original signed generating function.
checks=0
for n in range(2,1001):
    h=H_catalan(n,2)
    raw={j:Fraction(H_catalan(n,j+2),h) for j in range(1,17)}
    vals={}
    for m in range(1,17):
        assert raw[m]==Fraction(A[m].eval(n)),(n,m,'A')
        vals[m]=-sum((-1)**j*raw[j]*vals[m-j] for j in range(1,m))-m*(-1)**m*raw[m]
        assert vals[m]==Fraction(p[m].eval(n)),(n,m,'p')
        checks+=2
for n in range(2,21):
    for s in range(2,min(2*n+1,18)+1):
        assert H_catalan(n,s)==H_signed_convolution(n,s),(n,s)

c14=S.factor(abs(p[14].LC())/2)
c16=S.factor(abs(p[16].LC())/2)
print('FROZEN R462@18783e01e3646c72b7aab3b16d3f565e83e6446f')
print('CONTINUATION R574@2860e9a1596027fba449e3ce2522a985e9519bea')
print('MODEL d=2k-1, H_r(s) frozen signed BRC coefficient, Q_k(z)=z^d+sum_j (-1)^j H_k(j+2)/H_k(2) z^(d-j)')
print('P14_DEGREE',p[14].degree(), 'LC',p[14].LC())
print('P14_SHIFT_K3',n14,'ALL_POSITIVE True')
print('P14_K2_POSITIVE',p[14].eval(2)>0)
print('P16_DEGREE',p[16].degree(),'LC',p[16].LC())
print('P16_SHIFT_K7',n16,'ALL_NEGATIVE True')
print('P16_K2_TO_K6_POSITIVE',all(p[16].eval(n)>0 for n in range(2,7)))
print('RHO14_CONSTANT_POWER14',c14)
print('RHO14_CONSTANT',S.N(c14**S.Rational(1,14),16))
print('RHO16_CONSTANT_POWER16',c16)
print('RHO16_CONSTANT',S.N(c16**S.Rational(1,16),16))
print('P14_VALUES',[(n,'+' if p[14].eval(n)>0 else '-') for n in range(2,12)])
print('P16_VALUES',[(n,'+' if p[16].eval(n)>0 else '-') for n in range(2,12)])
print('INDEPENDENT_CATALAN_FRACTION_CROSSCHECK',checks,'checks for k=2..1000')
print('INDEPENDENT_SIGNED_BRC_COEFFICIENT_CROSSCHECK k=2..20, s=2..min(2k+1,18)')
print('R575_NEWTON_P14_P16_EXACT_PASS')
