#!/usr/bin/env python3
"""S23/AV global count-uniform decoder: exact finite checks of full TV identity.

The analytic n>=20000 theta theorem is in PROOF.md. These are exact scoped
finite checks, not a computer substitution for the Stirling/Hoeffding proof.
"""
from fractions import Fraction
from math import comb
from itertools import product

HALF = Fraction(1, 2)
LEGAL = ((Fraction(1, 2), Fraction(1, 2)),
         (Fraction(1, 2), Fraction(7, 8)),
         (Fraction(7, 8), Fraction(1, 2)),
         (Fraction(7, 8), Fraction(7, 8)),
         (Fraction(3, 5), Fraction(5, 7)))


def bin_pmf(n, k, p):
    return Fraction(comb(n, k)) * p**k * (1-p)**(n-k)


def count_overlap(n, z, p):
    """Exact overlap of target ternary law and decoded law."""
    result = Fraction(0)
    for m in range(n+1):
        mw = bin_pmf(n, m, 1-z)
        overlap = sum((min(bin_pmf(m,k,p), Fraction(1,m+1))
                      for k in range(m+1)), Fraction(0))
        result += mw*overlap
    return result


def ordered_overlap(n, a, z):
    """Independent brute-force enumeration over all 3^n ordered target words."""
    b = 1-a-z
    overlap = Fraction(0)
    for x in product((1,3,4),repeat=n):
        r = x.count(3)
        m = n-r
        k = x.count(1)
        actual = a**k*z**r*b**(m-k)
        decoded = z**r*(1-z)**m / ((m+1)*comb(m,k))
        overlap += min(actual, decoded)
    return overlap

assert Fraction(3249,22400) < Fraction(1,4)
assert 16 >= 2**4  # 1/2 * m^(-3/4) >= 1/m for every m>=16
for a,c in LEGAL:
    assert HALF <= a <= Fraction(7,8) and HALF <= c <= Fraction(7,8)
    z = (1-a)*c
    p = a/(1-z)
    assert Fraction(1,16) <= z <= Fraction(7,16)
    assert Fraction(2,3) <= p <= Fraction(56,57)
    assert a+z+(1-a-z) == 1
    assert (1-z)*p == a
    for n in (2,3,4,5):
        target_mass = decoded_mass = Fraction(0)
        for x in product((1,3,4),repeat=n):
            r, m, k = x.count(3), n-x.count(3), x.count(1)
            target_mass += a**k*z**r*(1-a-z)**(m-k)
            decoded_mass += z**r*(1-z)**m / ((m+1)*comb(m,k))
        assert target_mass == decoded_mass == 1
        o = count_overlap(n,z,p)
        assert o == ordered_overlap(n,a,z), (a,c,n)
        assert 0 < o <= 1
    for n in (12,24,48):
        o = count_overlap(n,z,p)
        assert o > 0 and o < 1
        print(f'corner_a={a} c={c} n={n} overlap={float(o):.12f} tv={float(1-o):.12f}')

# Fixed z=1/4 compare direct predecessor fiber points with same exact decoder.
for a in (Fraction(1,2), Fraction(3,5), Fraction(5,7)):
    z = Fraction(1,4)
    c = z/(1-a)
    assert HALF <= c <= Fraction(7,8)
    p = a/(1-z)
    assert count_overlap(5,z,p) == ordered_overlap(5,a,z)
print('PASS_S23_AV_FULL_LAWFUL_UNIFORM_COUNT_LOG_FACTOR_EXACT_CHECK_20261107')
