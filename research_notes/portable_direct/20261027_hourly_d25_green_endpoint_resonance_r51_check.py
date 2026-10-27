#!/usr/bin/env python3
"""Exact author checks for D25/LIFT R51 two-endpoint Green pole classification.

No Sage/NumPy/SymPy needed. All arithmetic is integer or rational.
The finite coverage is supporting evidence; the written proof is general.
"""

from fractions import Fraction
from math import factorial


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def vp_integer(n, p):
    if not n:
        return float("inf")
    n = abs(n)
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def vp(q, p):
    q = Fraction(q)
    return vp_integer(q.numerator, p) - vp_integer(q.denominator, p)


def norm_mod(q, p, strip):
    """q / p**strip modulo p, provided its p-valuation is >= strip."""
    q = Fraction(q)
    assert vp(q, p) >= strip, (p, strip, q)
    num_p = vp_integer(q.numerator, p)
    den_p = vp_integer(q.denominator, p)
    numerator_unit = q.numerator // (p ** num_p)
    denominator_unit = q.denominator // (p ** den_p)
    return (p ** (num_p - den_p - strip) * numerator_unit * pow(denominator_unit, -1, p)) % p


def w(k):
    return Fraction((6*k + 1)*factorial(2*k)*factorial(3*k), factorial(k)**5 * 216**k)


def s(k):
    return Fraction((8*k + 1)*factorial(4*k), factorial(k)**4 * 2304**k)


def a(k):
    return Fraction((6*k+7)*(2*k+1)*(3*k+1)*(3*k+2), 36*(6*k+1)*(k+1)**3)


def b(k):
    return Fraction((8*k+9)*(2*k+1)*(4*k+1)*(4*k+3), 288*(8*k+1)*(k+1)**3)


def P(k):
    return 2688*k**4 + 6160*k**3 + 4456*k**2 + 1166*k + 85


def check_one(p):
    assert p >= 13 and p % 6 == 1 and is_prime(p)
    N = (3*p - 1)//4 + 1
    assert 2 <= N and N+1 < p
    w0, s0 = w(N), s(N)
    w1, s1 = w(N+1), s(N+1)
    a0, b0 = Fraction(7, 18), Fraction(3, 32)
    assert w1 == a(N)*w0 and s1 == b(N)*s0
    assert (a(N)-b(N)) == Fraction((2*N+1)*P(N), 288*(N+1)**3*(6*N+1)*(8*N+1))
    assert tuple(vp(q, p) for q in (w0, s0, w1, s1)) == (3, 3, 3, 3)
    det = w0*s1-s0*w1
    assert det == w0*s0*(b(N)-a(N)) and det != 0
    C_N = (-a0*s1+b0*w1)/det
    C_N1 = (a0*s0-b0*w0)/det
    assert C_N*w0 + C_N1*w1 == -a0
    assert C_N*s0 + C_N1*s1 == -b0
    assert C_N*(w0-s0) + C_N1*(w1-s1) == -(a0-b0)
    assert vp(det, p) == 6 + vp(a(N)-b(N), p)
    expected = {139: -4, 199: -4, 277: -4}.get(p, -3)
    got = min(vp(C_N, p), vp(C_N1, p))
    assert got == expected, (p, N, got, expected)
    if p in (139,199,277):
        assert vp(a(N)-b(N), p) == 1
        assert vp(C_N, p) == vp(C_N1, p) == -4
    else:
        assert vp(a(N)-b(N), p) == 0
        assert vp(C_N, p) >= -3 and vp(C_N1, p) >= -3
    return N, vp(C_N, p), vp(C_N1, p), vp(a(N)-b(N), p)


def main():
    assert Fraction(P(Fraction(1, 4))) == Fraction(3047, 4)
    assert Fraction(P(Fraction(3, 4))) == Fraction(27661, 4)
    assert 3047 == 11 * 277 and 27661 == 139 * 199
    results = {}
    for p in range(13, 501):
        if p % 6 == 1 and is_prime(p):
            results[p] = check_one(p)
    for p, expect in {
        139: (105,108,66,105,3),
        199: (150,106,138,68,162),
        277: (208,78,251,224,224),
    }.items():
        n = results[p][0]
        assert n == expect[0]
        assert (P(n)//p) % p == expect[1]
        W, S = w(n), s(n)
        assert norm_mod(W,p,3) == expect[2]
        assert norm_mod(S,p,3) == expect[3]
        assert norm_mod(Fraction(3,32)*W - Fraction(7,18)*S,p,3) == expect[4]
    print('R51 PASS: target primes 13<=p<=500:', len(results))
    print('R51 resonances:', [(p, results[p]) for p in [139,199,277]])
    print('R51 ordinary samples:', [(p, results[p]) for p in [13,19,37,181,373,397]])


if __name__ == '__main__':
    main()
