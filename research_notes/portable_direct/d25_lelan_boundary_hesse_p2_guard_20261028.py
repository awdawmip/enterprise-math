#!/usr/bin/env python3
"""Exact author-side checker for Le Lan cutoff boundary K_(p-1) mod p^2.
Not a native H0/B0 benchmark or Source Result.
"""
from math import comb, isqrt


def is_prime(n):
    if n < 2:
        return False
    for k in range(2, isqrt(n) + 1):
        if n % k == 0:
            return False
    return True


def coefficients(p, power):
    modulus = p ** power
    # Denominators k, 4k, and 36k^3 are p-units for 1 <= k < p.
    t = [1]
    b = [1]
    for k in range(1, p):
        t.append(t[-1] * (2*k-1) * (3*k-2) * (3*k-1)
                 * pow(36 * k*k*k, -1, modulus) % modulus)
        b.append(b[-1] * (2*k-1) * pow(4*k, -1, modulus) % modulus)
    return t, b


def boundary(p, power=2):
    mod = p ** power
    t, b = coefficients(p, power)
    N = p-1
    return (3 * pow(2, -1, mod) *
            sum((2*(N-k)+1) * t[k] * b[N-k] for k in range(p))) % mod


def original_binomial_boundary(p, power=2):
    mod = p ** power
    t = [comb(2*k,k)**2 * comb(3*k,k) * pow(216, -k, mod) % mod
         for k in range(p)]
    b = [comb(2*j,j) * pow(8, -j, mod) % mod for j in range(p)]
    return (3 * pow(2, -1, mod) *
            sum((2*(p-1-k)+1)*t[k]*b[p-1-k] for k in range(p))) % mod


def hesse_unit(p):
    assert p % 6 == 1
    mod = p
    m = (p-1)//6
    a = 1
    value = 1
    # (1/3)_k (2/3)_k / (k!)^2, k <= 2m.
    for k in range(1, 2*m+1):
        a = a*(3*k-2)*(3*k-1)*pow(9*k*k, -1, mod)%mod
        value = (value + a)%mod
    return value


def check_prime(p):
    assert is_prime(p) and p % 6 == 1
    k = boundary(p)
    assert k % p == 0, (p, "not p divisible", k)
    assert k == (3*p*pow(2,-1,p*p)) % (p*p), (p, "bad p2 boundary", k)
    assert hesse_unit(p) == 1, (p, "nonunit Hesse sum")
    if p <= 373:
        assert k == original_binomial_boundary(p), (p, "independent binomial mismatch")
    return k // p


def check_373_p3():
    p = 373
    q = p**3
    t, b = coefficients(p, 3)
    B = []
    v = 0
    for bj in b:
        v = (v+bj)%q
        B.append(v)
    w = sum((6*k+1)*t[k] for k in range(p))%q
    h = pow(2,-1,q)*sum((6*k+1)*t[k]*B[p-1-k] for k in range(p))%q
    k = boundary(p,3)
    s = (h-k)%q
    assert (w,s,h,k)==(373, 8487242, 29983232, 21495990)
    assert k%(p*p)==70124==p*188
    assert h%(p*p)==70497==p*189
    assert s%(p*p)==p
    return (w,s,h,k)


if __name__ == '__main__':
    primes = [p for p in range(7, 2000) if is_prime(p) and p%6 == 1]
    for p in primes:
        check_prime(p)
    print('checked_plus_class_primes', len(primes))
    print('p373_exact_mod_p3', check_373_p3())
    # The theorem assumes p=6m+1. Check non-extension at p=11.
    other = boundary(11)
    assert other % (11*11) != (3*11*pow(2,-1,11*11))%(11*11)
    print('non_target_p11_boundary', other)
    print('PASS_D25_LELAN_BOUNDARY_HESSE_ALL_1_MOD_6_P2')
