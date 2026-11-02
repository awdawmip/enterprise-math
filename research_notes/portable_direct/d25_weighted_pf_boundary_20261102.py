#!/usr/bin/env python3
"""Exact original 216-model weighted Picard--Fuchs boundary certificate.

Source: author-side D25 second-digit LIFT research, 2026-11-02.
Purpose: independently verify a proven universal identity on a finite sample.
This does not test the native H0/B0 divided-power experiment.
Only stdlib modular integers and exact rational arithmetic.
"""
from fractions import Fraction
import json


def primes_up_to(n):
    s = bytearray(b'\x01') * (n + 1)
    s[:2] = b'\x00\x00'
    for q in range(2, int(n**0.5) + 1):
        if s[q]:
            s[q*q::q] = b'\x00' * len(s[q*q::q])
    return [q for q in range(5, n + 1) if s[q]]


def direct_fraction_last(p):
    a = Fraction(1)
    for k in range(1, p):
        a *= Fraction((2*k-1)*(3*k-2)*(3*k-1), 18*k**3)
    m = p**4
    return (a.numerator * pow(a.denominator, -1, m)) % m


def check(p):
    m = p**4
    inv18 = pow(18, -1, m)
    inv9 = pow(9, -1, m)
    a = 1
    g0 = 1
    for k in range(1, p):
        num = (2*k-1)*(3*k-2)*(3*k-1)
        den = 18*k**3
        anext = a * num * pow(den, -1, m) % m
        gnext = (6*k+1) * anext % m
        lhs = k**3*(6*k-5)*gnext % m
        rhs = (6*k+1)*num*inv18*g0 % m
        if lhs != rhs:
            raise AssertionError(('weighted_operator_internal', p, k, lhs, rhs))
        a, g0 = anext, gnext
    assert a % (p**3) == 0
    assert (a * inv9) % m == (-p**3*inv9) % m, p
    assert a == (-p**3) % m, (p, a)
    # theta^3 F-x(theta+1/2)(theta+1/3)(theta+2/3)F,
    # the only coefficient is at x^p after truncation to k=p-1.
    q = (2*p-1)*(3*p-2)*(3*p-1)*inv18 % m
    unweighted_boundary = -q*a % m
    assert unweighted_boundary == (-p**3*inv9) % m, p
    # Weighted original-series operator:
    # M=theta^3(6theta-5)-x(6theta+7)(theta+1/2)(theta+1/3)(theta+2/3)
    weighted_boundary = -(6*p+1)*q*g0 % m
    expect_boundary = 5*p**3*inv9 % m
    assert weighted_boundary == expect_boundary, (p, weighted_boundary, expect_boundary)
    weighted_half = weighted_boundary * pow(2, -p, m) % m
    expect_half = 5*p**3*inv18 % m
    assert weighted_half == expect_half, (p, weighted_half, expect_half)
    return {'p':p, 'last_coefficient_a_mod_p4':a,
            'weighted_boundary_coefficient_mod_p4':weighted_boundary,
            'weighted_operator_at_half_mod_p4':weighted_half,
            'normalized_boundary_digit':(weighted_boundary // p**3) % p,
            'normalized_at_half_digit':(weighted_half // p**3) % p}


def main():
    tests = primes_up_to(3000)
    samples = [5, 7, 11, 13, 19, 37, 43, 109, 373, 1171]
    detailed = {p: check(p) for p in tests}
    for p in samples:
        assert p in detailed
    exact_frac = [5, 7, 13, 19, 37]
    for p in exact_frac:
        assert direct_fraction_last(p) == detailed[p]['last_coefficient_a_mod_p4'], p
    out = {
      'schema':'D25_WEIGHTED_PF_BOUNDARY_FINITE_CHECK_V1',
      'model':'original W216; g_k=(6k+1)*(1/2)_k*(1/3)_k*(2/3)_k/(k!)^3',
      'proof_target_scope':'all primes p>3 (proof is symbolic in companion note)',
      'finite_checks_primes_to':3000,
      'finite_checks_count':len(tests),
      'internal_coefficients_verified_per_prime':'k=1,...,p-1 exact mod p^4',
      'internal_coefficients_total':sum(p-1 for p in tests),
      'exact_fraction_independent_primes':exact_frac,
      'passed':True,
      'sample_results':[detailed[p] for p in samples],
      'finite_tests_are_not_universal_proof':True,
      'native_H0B0_experiment':'NOT_EXECUTED',
      'source_class':'AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED'
    }
    print(json.dumps(out,indent=2,ensure_ascii=False))

if __name__ == '__main__':
    main()
