"""PREFIX-786: exact two-source affine mixed-sign margin certificate.

External scalar BRC-Gamma observer theorem only. No native X6 transfer,
original 189-layer recurrence re-execution, or BRC-Shor arithmetic.
All comparisons use Python fractions.Fraction.
"""
from fractions import Fraction as Q
from random import Random
import json


def observe(A1, A2, B1, B2, q, s, t):
    v1 = A1 - q * B1 + s
    v2 = A2 - q * B2 + s + t
    return (v1, v2, -v1, -v2)


def certificate(A1, A2, B1, B2, sigma, eta):
    assert A1 > 0 and 0 < B1 < B2 and sigma >= 0 and eta >= 0
    D = A2 * B1 - A1 * B2
    assert D > 0
    T = (B2 - B1) * sigma + B1 * eta
    r = max(Q(0), (D - T) / (B1 + B2))
    if T < D:
        s, t = sigma, -eta
        q = (A1 + s + r) / B1
        assert q > 0
        assert observe(A1, A2, B1, B2, q, s, t) == (-r, r, r, -r)
    else:
        theta = D / T
        s, t = theta * sigma, -theta * eta
        q = (A1 + s) / B1
        assert q > 0
        assert observe(A1, A2, B1, B2, q, s, t) == (0, 0, 0, 0)
    assert abs(s) <= sigma and abs(t) <= eta
    return {'D': D, 'T': T, 'radius': r,
            'q_witness': q, 's_witness': s, 't_witness': t}


def frac(x):
    return str(x.numerator) + '/' + str(x.denominator)


rng = Random(20261115786)
tests, point_probes, zero_cases, strict_cases = 0, 0, 0, 0
for k in range(8192):
    B1 = Q(rng.randint(1, 15), rng.randint(1, 9))
    B2 = B1 + Q(rng.randint(1, 15), rng.randint(1, 9))
    A1 = Q(rng.randint(1, 15), rng.randint(1, 9))
    D = Q(rng.randint(1, 15), rng.randint(1, 9))
    A2 = (D + A1 * B2) / B1
    sigma = Q(rng.randint(0, 25), rng.randint(1, 12))
    eta = Q(rng.randint(0, 25), rng.randint(1, 12))
    c = certificate(A1, A2, B1, B2, sigma, eta)
    strict_cases += int(c['radius'] > 0)
    zero_cases += int(c['radius'] == 0)
    for _ in range(8):
        q = Q(rng.randint(1, 35), rng.randint(1, 14))
        s = Q(rng.randint(-100, 100), 100) * sigma
        t = Q(rng.randint(-100, 100), 100) * eta
        v = observe(A1, A2, B1, B2, q, s, t)
        margin = max(abs(v[0]), abs(v[1]))
        assert v[0] == -v[2] and v[1] == -v[3]
        assert margin >= c['radius']
        if c['radius'] > 0:
            assert max(v) >= c['radius'] and min(v) <= -c['radius']
        point_probes += 1
    tests += 1

# Extends the illustrative PREFIX-785 family (A1=0 case).
family = []
for eta in (Q(0), Q(1, 2), Q(1), Q(3, 2), Q(2), Q(3)):
    predicted = max(Q(0), (2-eta)/3)
    if eta <= 2:
        q, s, t = (5-eta)/3, Q(1), -eta
    else:
        q, s, t = Q(1), Q(1), Q(-2)
    v = observe(Q(0), Q(3), Q(1), Q(2), q, s, t)
    assert max(abs(v[0]), abs(v[1])) == predicted
    family.append({'eta': frac(eta), 'sharp_margin': frac(predicted),
                   'q': frac(q), 's': frac(s), 't': frac(t),
                   'four_signs': [frac(x) for x in v]})

out = {
    'schema': 'PREFIX786_R6_TWO_SOURCE_AFFINE_MARGIN_V1',
    'status': 'ALL_CHECKS_PASS PREFIX786 TWO_SOURCE_SHARP_MARGIN',
    'date': '2026-11-15',
    'scientific_pin': 'f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'domain': 'A1>0, 0<B1<B2, D=A2*B1-A1*B2>0, sigma,eta>=0, q>0',
    'observer': '(v1,v2,-v1,-v2), v1=A1-qB1+s, v2=A2-qB2+s+t, |s|<=sigma, |t|<=eta',
    'sharp_uniform_infimum': 'max(0,(D-(B2-B1)*sigma-B1*eta)/(B1+B2))',
    'strict_two_sign_iff': '(B2-B1)*sigma+B1*eta<D',
    'dual_witness': 'lambda=(-B2/(B1+B2), B1/(B1+B2)); lambda dot B=0',
    'constructive_minimizer': 'T<D: s=sigma,t=-eta,r=(D-T)/(B1+B2),q=(A1+sigma+r)/B1. T>=D: theta=D/T,s=theta*sigma,t=-theta*eta,q=(A1+s)/B1, r=0.',
    'regression': {'rational_parameter_cases': tests,
                   'pointwise_rational_probes': point_probes,
                   'strict_cases': strict_cases,
                   'zero_cases': zero_cases,
                   'method': 'Python fractions.Fraction; seeded samples and explicit algebraic witnesses'},
    'prefix785_extended_family': family,
    'scope': 'External scalar reflected four-cell observation with correlated sources; not a native BRC/X6 physical realization or independent review.'
}
with open('PREFIX786_R6_TWO_SOURCE_AFFINE_MARGIN_RESULTS.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'status':out['status'], 'regression':out['regression'],
                  'family':family}, ensure_ascii=False))
