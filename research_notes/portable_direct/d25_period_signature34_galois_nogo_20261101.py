#!/usr/bin/env python3
"""D25 author-side exact interval and Galois obstruction certificates.

No mathematical claims about the native H0/B0/Frobenius benchmark.
"""
from fractions import Fraction as Q
from math import isqrt


def hyper_interval(a, b, z, terms):
    """Positive 2F1(a,b;1;z) interval using geometric ratio upper bound z."""
    term = Q(1)
    partial = Q(0)
    for k in range(terms):
        partial += term
        term *= (a + k) * (b + k) * z / (k + 1) ** 2
    return partial, partial + term / (1 - z)


def real_interval_certificate():
    n = 460
    scale = 10 ** 140
    sqrt_floor = isqrt(2 * scale * scale)
    s_low, s_high = Q(sqrt_floor, scale), Q(sqrt_floor + 1, scale)
    al, ah = hyper_interval(Q(1, 6), Q(1, 3), Q(1, 2), n)
    bl, bh = hyper_interval(Q(1, 8), Q(3, 8), Q(1, 9), n)
    lower = 4 * al**2 - 3 * s_high * bh**2
    upper = 4 * ah**2 - 3 * s_low * bl**2
    tol = Q(1, 10**115)
    assert -tol < lower < upper < tol
    assert upper - lower < tol
    print('ANALYTIC_INTERVAL_PASS', 'terms=', n, '|4*Fa² - 3*sqrt(2)*Fb²| < 10^-115')
    print('INTERVAL_WIDTH_LESS_THAN', '1e-115', upper - lower < tol)
    return al, ah, bl, bh


def primes(limit):
    table = bytearray([1]) * (limit + 1)
    table[:2] = b'\x00\x00'
    for q in range(2, isqrt(limit)+1):
        if table[q]:
            table[q*q::q] = b'\x00' * ((limit-q*q)//q+1)
    return [p for p in range(19, limit+1) if table[p] and p % 24 == 19]


def gauss_factors(p):
    """Original rational α and β Gauss series in Z/p³Z, 0<=k<p."""
    modulus = p ** 3
    aa = bb = 1
    A = B = 0
    for k in range(p):
        A = (A+aa) % modulus
        B = (B+bb) % modulus
        if k+1 < p:
            aa = aa * (6*k+1)*(3*k+1)*pow(36*(k+1)**2, -1, modulus) % modulus
            bb = bb * (8*k+1)*(8*k+3)*pow(576*(k+1)**2, -1, modulus) % modulus
    return A, B


def finite_field_obstruction():
    """Non-squareness gives all-class proof; finite checks confirm hypotheses."""
    samples = []
    for p in primes(2500):
        # For p=19 mod 24, 2 is a quadratic nonresidue, and 3,4 are units.
        assert pow(2, (p-1)//2, p) == p-1
        A, B = gauss_factors(p)
        assert A % p == B % p == 0
        a, b = (A // p) % p, (B // p) % p
        # The numerical regression checks both normalized factors are units.
        # The mathematical no-go itself only requires v_p(B)<=1.
        assert a != 0 and b != 0, p
        # If A² = (3 sqrt2 / 4) B² mod p³, then taking p² quotients
        # forces sqrt2 to equal a square in Fp: (4/3)*(a/b)^2.
        forced_root2 = (4 * pow(3, -1, p) * a * a * pow(b*b, -1, p)) % p
        assert (forced_root2 * forced_root2 - 2) % p != 0
        if p in (19, 43, 67, 139, 211, 523):
            samples.append((p, a, b, forced_root2))
    A13, B13 = gauss_factors(13)
    assert A13 % 13 == 0 and (A13 // 13) % 13 == 11
    assert B13 % (13**2) == 0
    # The same proposed congruence already fails at 13 by valuations:
    # A13²/13² = 11² != 0, whereas B13²/13² = 0 (mod 13).
    assert pow((A13 // 13) % 13, 2, 13) == 4
    print('FINITE_P19_OBSTRUCTION_PASS', len(primes(2500)), 'primes p<=2500')
    print('FIXED_P13_VALUATION_WITNESS_PASS', 'A13/p=11 mod13', 'B13=0 mod13²')
    print('SAMPLE_p_Malpha/p_Mbeta/p_forced_sqrt2:', samples)
    return samples


if __name__ == '__main__':
    real_interval_certificate()
    finite_field_obstruction()
