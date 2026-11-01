#!/usr/bin/env python3
"""Independent exact modular check of a sourced E.2 second-harmonic corollary.

External theorem (not reproved here): for primes p == 1 mod 6,
B_p = sum_{n=0}^{(p-1)//3} (-1)^n(6n+1)(1/3)_n^3/(n!)^3 == p (mod p^3).
This checker compares a separate original recurrence against an exact finite
binomial expansion. It does not execute the D25 native H0/B0 experiment.
"""

from math import comb


def primes(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for i in range(2, int(limit**.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = b'\x00' * ((limit - i * i) // i + 1)
    return [p for p in range(7, limit + 1) if sieve[p] and p % 6 == 1]


def one(p):
    assert p > 3 and p % 6 == 1
    m = (p - 1) // 3
    mod = p**3
    # Direct E.2 branch, independent of harmonic formulas.
    b = 1
    original = 0
    for n in range(m + 1):
        original = (original + (6 * n + 1) * b) % mod
        if n < m:
            b = b * (-(3 * n + 1)**3) * pow(27 * (n + 1)**3, -1, mod) % mod

    h1 = h2 = 0
    franel = 0
    binomial_expansion = 0
    d1 = d2 = 0
    for n in range(m + 1):
        w = 6 * n + 1
        v = comb(m, n)**3 % mod
        # Delta_m(n) = H_m - H_{m-n}; after n -> n+1, add 1/(m-n).
        if n > 0:
            r = m - n + 1
            d1 = (d1 + pow(r, -1, p**2)) % (p**2)
            d2 = (d2 + pow(r, -2, p)) % p
        franel = (franel + v) % (p**2)
        h1 = (h1 + w * v * d1) % (p**2)
        k2 = (pow(2, -1, p) * (d1 % p)**2 - pow(6, -1, p) * d2) % p
        h2 = (h2 + w * (v % p) * k2) % p
        binomial_expansion = (binomial_expansion + w * v * (1 - p * d1 + p * p * k2)) % mod

    # Second-order signed reflection port: the weighted sum only sees the
    # antisymmetric part under n -> m-n, because w_n + w_{m-n} = 2p.
    harm = [0] * (m + 1)
    harm2 = [0] * (m + 1)
    for n in range(1, m + 1):
        harm[n] = (harm[n-1] + pow(n, -1, p)) % p
        harm2[n] = (harm2[n-1] + pow(n, -2, p)) % p
    signed_second = 0
    for n in range(m + 1):
        wv = (6 * n + 1) * (comb(m, n)**3 % p)
        hn, hr = harm[n], harm[m-n]
        term = (pow(4, -1, p) * (hn-hr)*(2*harm[m]-hn-hr)
                - pow(12, -1, p) * (harm2[n]-harm2[m-n]))
        signed_second = (signed_second + wv * term) % p
    assert signed_second == h2, (p, h2, signed_second)
    assert (p * franel - p * h1 + p * p * h2) % mod == binomial_expansion
    assert original == binomial_expansion, (p, original, binomial_expansion)
    # The following uses the cited, previously proved E.2 theorem, not a claimed new proof.
    assert original == p, (p, original)
    harmonic_defect = (h1 - franel + 1 - p * h2) % (p * p)
    assert harmonic_defect == 0, (p, harmonic_defect)
    first_defect = (h1 - franel + 1) % p
    assert first_defect == 0
    return dict(p=p, m=m, B=original, franel_mod_p=franel % p,
                harmonic1_mod_p2=h1, harmonic2_mod_p=h2,
                harmonic1_first_digit=h1 % p, signed_second_reflection=signed_second,
                lift_correction=(h1-franel+1)//p % p
                if (h1-franel+1) % p == 0 else None)


def run(limit=5000):
    ps = primes(limit)
    rows = [one(p) for p in ps]
    target = [v for v in rows if v['p'] % 24 in (13,19)]
    print('PROVED_EXTERNALLY: Van Hamme E.2 theorem, exact B == p mod p^3')
    print('EXECUTED_PRIMES_1_MOD_6', len(rows))
    print('FROZEN_D25_CLASS_PRIMES', len(target))
    for row in rows:
        if row['p'] in (7,13,19,31,37,157,373,1327):
            print('ANCHOR', row)
    print('PASS_SOURCED_E2_SECOND_HARMONIC_MOMENT_AND_RAW_RECURRENCE')

if __name__ == '__main__':
    run()
