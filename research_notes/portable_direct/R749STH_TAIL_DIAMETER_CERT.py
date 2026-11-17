#!/usr/bin/env python3
"""R749STH exact rational certificate: six-phase tail diameter and injective tail.
Python 3 + SymPy. Regenerates all counts C_n/T_n; no floats in checks.
"""
import json
from math import factorial
from pathlib import Path
import sympy as s

N, J = s.symbols('N J')
W = (1, 1, 2, 3, 6)

def convolution(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            result[i+j] += ai * bj
    return result

def block_numerator(weights):
    product = [1]
    for w in weights:
        assert 6 % w == 0
        product = convolution(product, [int(k % w == 0) for k in range(7-w)])
    return product

def falling_binomial(x, k):
    return s.prod((x-i) for i in range(k)) / factorial(k)

QC = block_numerator((*W, 1))
QT = convolution([0, 1], block_numerator((1, 1, 1, 1, 2, 3, 6)))
assert len(QC) == 23 and len(QT) == 29

def quasipolys(r):
    c = s.Poly(sum((a*falling_binomial((N-1-i)/6+5,5)
                    for i, a in enumerate(QC) if (r-1-i)%6 == 0), s.Integer(0)), N)
    t = s.Poly(sum((a*falling_binomial((N-1-i)/6+6,6)
                    for i, a in enumerate(QT) if (r-1-i)%6 == 0), s.Integer(0)), N)
    return c, t

L = 115
part = [0]*(L+1)
part[0] = 1
for w in W:
    for k in range(w, L+1):
        part[k] += part[k-w]
C, T = [0]*(L+1), [0]*(L+1)
for k in range(1,L+1):
    C[k] = C[k-1] + part[k-1]
    T[k] = T[k-1] + C[k-1]

certificate = {
    'unit':'R749STH',
    'status':'AUTHOR_EXACT_NOT_REVIEWED',
    'frozen_science':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
    'model':'five labeled weights (1,1,2,3,6); e,d in [-2,2] fixed per state',
    'claim':'all n>=73: exact full error-state diameter decreases at six-step increments; n*diameter -> 2880; exact same-cutoff infinite tails injective',
    'quasipolynomial':'QC(z)/(1-z^6)^6, QT(z)/(1-z^6)^7 for [z^(n-1)], valid n>=29',
    'phase_certificates':{},
}

common_c = [s.Rational(1,4320), s.Rational(1,144), s.Rational(95,1296)]
common_t = [s.Rational(1,25920), s.Rational(11,8640), s.Rational(155,10368)]
for r in range(6):
    cp, tp = quasipolys(r)
    assert cp.degree() == 5 and tp.degree() == 6
    assert cp.all_coeffs()[:3] == common_c
    assert tp.all_coeffs()[:3] == common_t
    for k in range(73, L+1):
        if k%6 == r:
            assert cp.eval(k) == C[k] and tp.eval(k) == T[k]
    start = next(k for k in range(73,79) if k%6 == r)
    c, t = cp.as_expr(), tp.as_expr()
    A = s.expand(N**3*(c+t))
    B = s.expand(c**2-4)
    diff = s.Poly(s.expand((A*B.subs(N,N+6)-A.subs(N,N+6)*B)
                           .subs(N,start+6*J)), J)
    coeff = list(reversed(diff.all_coeffs()))
    assert diff.degree() == 18 and len(coeff) == 19
    assert all(v>0 for v in coeff), (r, coeff)
    certificate['phase_certificates'][str(r)] = {
        'start_n': start,
        'polynomial_degree': diff.degree(),
        'strict_positive_coefficients': len(coeff),
        'coefficient_list_ascending':[str(v) for v in coeff],
        'first_coefficient':str(coeff[0]),
        'leading_coefficient':str(coeff[-1]),
    }

a,b,c=common_c
u,v,w=common_t
assert s.cancel(u/a**2) == 720
assert s.cancel(v/a**2-2*b*u/a**3) == -19440
assert s.cancel(w/a**2-2*b*v/a**3+(3*b**2/a**2-2*c/a)*u/a**2) == 341400
assert 1/a == 4320 and -b/a**2 == -129600
assert 4*720 == 2880
assert 4*(4320-19440) == -60480
assert 4*(341400-129600) == 847200
for k in (73,77,79,83,100):
    assert C[k]>2 and T[k]>2
    exact = s.Rational(4*k**3*(C[k]+T[k]), C[k]**2-4)
    certificate.setdefault('sample_exact_diameters',{})[str(k)] = str(exact)

certificate['verified_coefficients'] = 114
certificate['asymptotic_coefficients'] = {
 'general_delta_d_1_over_n':'720',
 'general_delta_e_1_over_n2':'4320',
 'general_delta_d_1_over_n2':'-19440',
 'general_delta_e_1_over_n3':'-129600',
 'general_delta_d_1_over_n3':'341400',
 'diameter_1_over_n':'2880',
 'diameter_1_over_n2':'-60480',
 'diameter_1_over_n3':'847200'
}
out=Path(__file__).with_name('R749STH_TAIL_DIAMETER_RESULTS.json')
out.write_text(json.dumps(certificate,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf-8')
print('PASS R749STH: 114/114 strict positive coefficients, six phases; infinite six-step diameter monotonicity; Laurent invariants')
print('output:',out,'bytes=',out.stat().st_size)
