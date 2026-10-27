#!/usr/bin/env python3
"""Exact original S-side Clausen port / high-tail checker, p = 19 mod 24."""
from math import isqrt, factorial
from fractions import Fraction


def plist(bound=1000):
    return [p for p in range(19, bound) if p % 24 == 19 and
            all(p % q for q in range(2, isqrt(p) + 1))]


def coeff_units(p):
    val = [0] * p
    unit = [1] * p
    for k in range(p - 1):
        x = (8 * k + 1) * (8 * k + 3)
        e = 0
        while x % p == 0:
            e += 1
            x //= p
        val[k + 1] = val[k] + e
        unit[k + 1] = unit[k] * x * pow(576 * (k + 1) ** 2, -1, p) % p
    return val, unit


def fact_unit(p):
    nmax = 4 * (p - 1)
    unit = [1] * (nmax + 1)
    val = [0] * (nmax + 1)
    for n in range(1, nmax + 1):
        a = n
        e = 0
        while a % p == 0:
            a //= p
            e += 1
        unit[n] = unit[n - 1] * a % p
        val[n] = val[n - 1] + e
    return unit, val


def run(p):
    a, b = (p - 3) // 8, (3 * p - 1) // 8
    h, H = (p - 1) // 2, (3 * p - 1) // 4
    assert a + b == h and 2 * b == H
    val, unit = coeff_units(p)
    assert all(val[k] == (0 if k <= a else 1 if k <= b else 2)
               for k in range(p))
    fu, fv = fact_unit(p)
    Gmm = Glh = upper = 0
    for n in range(h + 1, p):
        mm = sum(unit[i] * unit[n - i]
                 for i in range(a + 1, b + 1)
                 if a < n - i <= b) % p
        lh = sum(unit[j] * unit[n - j]
                 for j in range(a + 1) if b < n - j < p) % p
        coeff = (8 * n + 1) * (mm + 2 * lh) % p
        vn = fv[4 * n] - 4 * fv[n]
        original = ((8 * n + 1) * fu[4 * n] *
                    pow(fu[n] ** 4 * pow(2304, n, p), -1, p)) % p
        if n <= H:
            assert vn == 2 and coeff == original, (p, n, coeff, original)
            Gmm = (Gmm + (8 * n + 1) * mm) % p
            Glh = (Glh + 2 * (8 * n + 1) * lh) % p
        else:
            assert vn == 3 and mm == 0 and lh == 0 and coeff == 0
            assert unit[n] == (-sum(unit[j] * unit[n - j]
                                    for j in range(1, a + 1))) % p
            upper += 1
    # Finite author test of an *externally proved* S full/half congruence.
    assert (Gmm + Glh) % p == 0, (p, Gmm, Glh)
    assert upper == p - 1 - H
    return (a, b, h, H, Gmm, Glh, upper)


def check_unit_square_gap(p):
    """13 mod 24: unit Gauss square has p^2 coefficient-gap above half."""
    assert p % 24 == 13
    a, b = (5 * p - 1) // 8, (7 * p - 3) // 8
    h = (p - 1) // 2
    assert h < a < b < p
    mod = p * p
    unit = [1] * (a + 1)
    for k in range(a):
        num = (8 * k + 1) * (8 * k + 3)
        assert num % p != 0
        unit[k + 1] = unit[k] * num * pow(576 * (k + 1)**2, -1, mod) % mod
    for n in range(h + 1, a + 1):
        coeff = sum(unit[j] * unit[n - j] for j in range(n + 1)) % mod
        assert coeff == 0, (p, n, coeff)
    return (a, b, h, a-h)


def check_exact_clausen():
    """Independent small-degree rational calculation from unchanged S factorials."""
    t = [Fraction(1)]
    for k in range(11):
        t.append(t[-1] * Fraction((8*k + 1)*(8*k + 3),
                                  576*(k + 1)**2))
    for n in range(12):
        convolution = sum((t[j]*t[n-j] for j in range(n+1)), Fraction(0))
        original = Fraction(factorial(4*n),factorial(n)**4*2304**n)
        assert convolution == original, (n, convolution, original)
    return 12


def main():
    print('PASS_EXACT_RATIONAL_CLAUSEN', 'degrees', check_exact_clausen())
    primes = plist()
    records = {p:run(p) for p in primes}
    print('PASS', 'primes', len(primes),
          'source_ranks', sum(r[3] - r[2] for r in records.values()),
          'upper_gap', sum(r[6] for r in records.values()))
    ps13 = [p for p in range(13, 1000) if p % 24 == 13 and
            all(p % q for q in range(2, isqrt(p) + 1))]
    unit_gaps = {p:check_unit_square_gap(p) for p in ps13}
    print('PASS_13_CLASS', 'primes', len(ps13),
          'unit-square-p2-gap-ranks', sum(r[3] for r in unit_gaps.values()))
    for p in (13, 37, 61, 181, 229, 277, 373):
        if p in unit_gaps:
            print('p=',p,'a,b,h,unit-gap=',*unit_gaps[p])
    for p in (19, 43, 67, 139, 211, 283, 307, 379):
        if p in records:
            print('p=', p, 'a,b,h,H,Gmm,Glh,gap=', *records[p])


if __name__ == '__main__':
    main()
