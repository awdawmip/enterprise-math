#!/usr/bin/env python3
"""Exact p-adic inverse-moment certificate for the original signed W216.
Nine target-class primes; raw independent binomial coefficient path for p<=373.
No native H0/B0 execution or independent mathematical review is inferred.
"""
from math import comb, isqrt


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def check(p, raw=False):
    assert is_prime(p) and p > 5 and p % 24 in (13, 19)
    m3, mod = p ** 3, p ** 4
    u = 1
    W = 0
    reduced = 0
    u_last = None
    for k in range(p):
        if raw:
            independent = (comb(2*k, k)**2 * comb(3*k, k)
                           * pow(216, -k, mod)) % mod
            assert u == independent, (p, k, u, independent)
        W = (W + (6*k + 1)*u) % mod
        if k <= p - 2:
            numerator = -(k - 1)*(6*k + 5)
            denominator = 3*(k + 1)**2
            assert denominator % p != 0
            reduced = (reduced + u*numerator*pow(denominator, -1, mod)) % mod
        else:
            u_last = u
        if k < p - 1:
            numerator = (2*k + 1)*(3*k + 1)*(3*k + 2)
            denominator = 36*(k + 1)**3
            assert denominator % p != 0
            u = u*numerator*pow(denominator, -1, mod) % mod
    correction = ((7 - 6*p)*u_last) % mod
    assert (reduced + correction - W) % mod == 0
    assert u_last % m3 == 0
    assert W % m3 == reduced % m3
    assert (correction + 7*m3) % mod == 0
    residue = (W - p) % m3
    fourth = ((W - p)//m3) % p if residue == 0 else None
    return dict(p=p, class24=p % 24, W_mod_p3=W % m3, W_mod_p4=W,
                inverse_moments_mod_p4=reduced,
                inverse_moments_mod_p3=reduced % m3,
                correction_mod_p4=correction,
                terminal_quotient_mod_p=(u_last//m3) % p,
                LIFT_remainder_p3=residue, W_fourth_digit=fourth,
                inverse_fourth_digit=((reduced-p)//m3) % p if residue == 0 else None,
                passed=True)


if __name__ == '__main__':
    for p in (13, 19, 37, 43, 61, 67, 373, 10069, 10099):
        print(check(p, raw=p <= 373))
