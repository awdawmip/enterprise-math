#!/usr/bin/env python3
"""Exact finite check for D25 original A216 zeroth/first moment ports.

Author-side regression, not a native H0/B0 benchmark or a uniform theorem.
The rational terms have p-integral denominators for p>3.
"""
from math import comb


def primes_below(bound):
    b = bytearray([1]) * bound
    b[:2] = b'\x00\x00'
    for d in range(2, int(bound**0.5) + 1):
        if b[d]:
            b[d * d:bound:d] = b'\x00' * len(b[d * d:bound:d])
    return [i for i in range(bound) if b[i]]


def moments_recurrence(p):
    mod = p ** 3
    c = 1
    s0 = s1 = 0
    for n in range(p):
        s0 = (s0 + c) % mod
        s1 = (s1 + n * c) % mod
        if n + 1 < p:
            # a_{n+1}/a_n=(2n+1)(3n+1)(3n+2)/(36(n+1)^3)
            c = c * (2 * n + 1) * (3 * n + 1) * (3 * n + 2)
            c = c * pow(36 * (n + 1)**3, -1, mod) % mod
    return s0, s1


def moments_raw_binomial(p):
    mod = p ** 3
    s0 = s1 = 0
    inv = pow(216, -1, mod)
    denominator = 1
    for n in range(p):
        c = comb(2*n, n)**2 * comb(3*n, n) * denominator % mod
        s0 = (s0 + c) % mod
        s1 = (s1 + n*c) % mod
        denominator = denominator * inv % mod
    return s0, s1


def legendre_minus_three(p):
    t = pow((-3) % p, (p - 1)//2, p)
    return -1 if t == p - 1 else 1


def main():
    primes = primes_below(5000)
    assert len(primes) == 669  # includes 2,3
    targets = 0
    inert = 0
    exceptions = []
    profiles = {}
    target_p3_failures = []
    for p in primes:
        if p <= 3:
            continue
        s0, s1 = moments_recurrence(p)
        mod = p**3
        chi = legendre_minus_three(p)
        w = (s0 + 6*s1) % mod
        if p % 24 in (13, 17, 19, 23):
            inert += 1
            if (s0 % (p*p) != 0 or (6*s1-chi*p)%(p*p) != 0):
                exceptions.append((p,'moment first lift',s0,s1))
        if p % 24 in (13, 19):
            targets += 1
            if (w-p)%mod:
                target_p3_failures.append((p,w))
            if p in (13,19,373):
                unit = p*pow(6,-1,mod)%mod
                assert s0%(p*p)==0 and (s1-unit)%(p*p)==0
                profiles[p] = {
                    'modulus':mod,'S0':s0,'S1':s1,'p_div_6':unit,
                    'S0_div_p2_mod_p':s0//(p*p),
                    'first_moment_correction_div_p2_mod_p':((s1-unit)%mod)//(p*p),
                    'original_weighted_sum':w,
                }
    for p in (13,19,373):
        got = moments_recurrence(p)
        raw = moments_raw_binomial(p)
        assert got == raw, (p,got,raw)
    assert not exceptions, exceptions
    assert not target_p3_failures, target_p3_failures
    assert targets == 166, targets
    for p in (13,19,373):
        d = profiles[p]
        assert d['S0_div_p2_mod_p'] != 0
        assert d['first_moment_correction_div_p2_mod_p'] != 0
        assert (d['S0_div_p2_mod_p']+6*d['first_moment_correction_div_p2_mod_p'])%p==0
    print('PASS_D25_ORIGINAL_A216_MOMENT_PORTS')
    print('PRIMES_CHECKED',len(primes)-2)
    print('INERT_CLASSES_CHECKED',inert)
    print('FROZEN_TARGET_CLASSES_CHECKED',targets)
    print('INERT_FIRST_MOMENT_P2_EXCEPTIONS',exceptions)
    print('TARGET_WEIGHTED_P3_EXCEPTIONS',target_p3_failures)
    for p in (13,19,373):
        print('EXACT_SOURCE_PROFILE',p,profiles[p])


if __name__ == '__main__':
    main()
