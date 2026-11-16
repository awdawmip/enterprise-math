#!/usr/bin/env python3
"""R422: exact independent checks of the signed BRC auxiliary Turan bound."""
from fractions import Fraction
from math import comb

def rho(q, d):
    d = abs(d)
    if d > q:
        return Fraction(0)
    z = Fraction(1)
    for j in range(d):
        z *= Fraction(q - j, q + j + 1)
    return z

def a(q, n):
    assert 0 <= n <= q
    return sum((comb(n, k) * (rho(q, n - 2*k) - rho(q, n - 2*k - 1))
                for k in range(n + 1)), Fraction(0))

def signed_delta(r, q):
    n = r-q
    result = 0
    for k in range(n + 1):
        d = r - 2*k
        v = comb(2*q, d) if 0 <= d <= 2*q else 0
        d -= 1
        w = comb(2*q, d) if 0 <= d <= 2*q else 0
        result += comb(n, k) * (v - w)
    return result

def normalized_turan(s, m):
    lam = Fraction(m * s*s * (2*s+m+1), (m+1)*(s+1)**2 * (2*s+m))
    aa = a(s, m)
    a_minus = a(s-1, m+1)
    a_plus = a(s+1, m-1)
    return aa*aa - lam*a_minus*a_plus

def bound(s, m):
    return Fraction(4**m, 2*(m+1)*s*s)

def check():
    direct = 0
    for m in range(1, 9):
        for s in range(m+2, m+11):
            r = s+m
            for h in (-1, 0, 1):
                q = s+h
                assert a(q, m-h) * comb(2*q, q) == signed_delta(r, q)
                direct += 1
            W = comb(2*s+m, 2*s)*comb(2*s, s)
            H = lambda q: comb(r+q, 2*q) * signed_delta(r, q)
            assert normalized_turan(s,m)*W*W == H(s)**2 - H(s-1)*H(s+1)
    threshold = 0
    worst_gap = None
    for m in range(1, 33):
        s = 72*(m+2)**4
        actual = normalized_turan(s,m)
        lower = bound(s,m)
        assert actual >= lower > 0, (m, s, actual, lower)
        for h in (-1, 0, 1):
            q, n = s+h, m-h
            b = Fraction(s, 2**n)*a(q, n)
            eps = Fraction(1,8*(m+2))
            assert abs(b-1) <= eps, (m,h)
        threshold += 1
        ratio = actual / lower
        if worst_gap is None or ratio < worst_gap:
            worst_gap = ratio
    print(f'R422_EXACT_PASS direct_signed_delta_checks={direct} '
          f'direct_turan_checks={8*9} threshold_checks={threshold} '
          f'worst_actual_over_bound={worst_gap.numerator}/{worst_gap.denominator}')

if __name__ == '__main__':
    check()
