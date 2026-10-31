#!/usr/bin/env python3
"""Exact finite evidence for a fourth-order affine 216/2304 bridge.

Every assertion is about explicitly enumerated primes only. No p^4 theorem for
all primes is claimed. Native 373 H0/B0 and Frobenius are NOT executed here.
Run: python d25_affine_p4_bridge_cert_20261031.py [prime_limit]
"""
from hashlib import sha256
from math import comb, isqrt
import sys


def primes_up_to(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for k in range(2, isqrt(limit) + 1):
        if sieve[k]:
            sieve[k * k::k] = b'\x00' * ((limit - k * k) // k + 1)
    return [p for p in range(5, limit + 1) if sieve[p]]


def term_sums(p, exponent=4):
    mod = p**exponent
    # Only indices 1..p-1 are inverted, all units modulo p**exponent.
    inv = [0] * p
    inv[1] = 1
    for k in range(2, p):
        inv[k] = (-(mod // k) * inv[mod % k]) % mod
    ia = pow(36, -1, mod)
    ib = pow(288, -1, mod)
    a = b = 1
    A = B = 1
    for k in range(1, p):
        j = k - 1
        inv_k_3 = (inv[k]**3) % mod
        a = a * (2*j+1) * (3*j+1) * (3*j+2) * ia * inv_k_3 % mod
        b = b * (4*j+1) * (2*j+1) * (4*j+3) * ib * inv_k_3 % mod
        A = (A + (6*k+1)*a) % mod
        B = (B + (8*k+1)*b) % mod
    return A, B


def original_binomial_sums(p, exponent):
    m = p**exponent
    pow_a = pow_b = 1
    inv_a = pow(216, -1, m)
    inv_b = pow(2304, -1, m)
    A = B = 0
    for k in range(p):
        A = (A + (6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow_a) % m
        B = (B + (8*k+1)*comb(4*k,2*k)*comb(2*k,k)**2*pow_b) % m
        pow_a = pow_a*inv_a % m
        pow_b = pow_b*inv_b % m
    return A,B


def main(limit=15000):
    ps = primes_up_to(limit)
    sh = sha256()
    target_count = 0
    p4_affine_failures = []
    rows = {}
    for p in ps:
        m = p**4
        A, B = term_sums(p, 4)
        chi = 1 if p % 3 == 1 else -1
        # Proved published B congruence; finite recheck of the comparison input.
        assert B % p**3 == (p*chi) % p**3, (p, 'B theorem regression')
        # Existing third-order bridge from prior author's finite experiments.
        assert A % p**3 == B % p**3, (p, 'p3 bridge regression')
        residual = (A - 2*B + p*chi) % m
        if residual:
            p4_affine_failures.append((p, residual))
        target_count += (p % 24 in (13,19))
        ua = ((A-p*chi) % m)//p**3
        ub = ((B-p*chi) % m)//p**3
        gap = ((A-B) % m)//p**3
        sh.update(f'{p},{A},{B},{ua},{ub},{gap};'.encode('ascii'))
        if p in (5,7,11,13,19,31,37,67,373,997,14983):
            rows[p] = dict(A4=A, B4=B, A_defect=ua,
                           B_defect=ub, bridge_defect=gap,
                           affine4=residual)
    # Test the original binomial definitions independently, including 373.
    for p in (5,7,13,19,31,37,67,373):
        assert term_sums(p, 4) == original_binomial_sums(p, 4), (p, 'direct original mismatch')
    # A target-class counterexample to the stronger A==B mod p^4.
    assert rows[13]['bridge_defect'] == 11
    assert rows[19]['bridge_defect'] == 6
    assert rows[373]['bridge_defect'] == 114
    print('EXACT_PRIME_DOMAIN: 5 <= p <=', limit)
    print('PRIMES_CHECKED:',len(ps),'FROZEN_TARGET_PRIMES:',target_count)
    print('AFFINE_P4_CANDIDATE_FAILURES:',len(p4_affine_failures),p4_affine_failures[:10])
    print('WITNESS_STREAM_SHA256:',sh.hexdigest())
    for p,r in sorted(rows.items()):
        print('WITNESS',p,r)
    print('DIRECT_BINOMIAL_CROSSCHECKS: 5,7,13,19,31,37,67,373 PASS')
    for p in (13,19,373):
        A5,B5 = term_sums(p, 5)
        assert (A5,B5) == original_binomial_sums(p, 5), (p, 'p5 independent direct mismatch')
        chi=1 if p%3==1 else -1
        q5=((A5 - 2*B5 + p*chi) % (p**5)) // p**4
        assert q5 != 0
        print('P5_AFFINE_NON_LIFT',p, 'p4_quotient_mod_p',q5)
    assert not p4_affine_failures
    print('FINITE_EXACT_PASS: affine p^4 holds on enumerated primes; NO UNIVERSAL PROOF / NATIVE_NOT_EXECUTED')

if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv)>1 else 15000)
