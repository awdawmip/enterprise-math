#!/usr/bin/env python3
"""Exact author check of the universal D25 terminal Jacobi second-jet forcing.
Standard library only. This finite check is NOT a proof of the universal theorem.
"""
from fractions import Fraction
from math import factorial, isqrt


def primes_upto(limit):
    for n in range(2, limit + 1):
        if all(n % d for d in range(2, isqrt(n) + 1)):
            yield n


def jets(p):
    """Return coefficients of F0, F1 and F2/2 at x=m for degrees 0..p-1."""
    m = (p - 1) // 6
    a, v, w = [Fraction(1)], [Fraction(0)], [Fraction(0)]
    for n in range(p - 1):
        q0 = Fraction((n - m) * (n - 2 * m), (n + 1) ** 2)
        q1 = Fraction(4 * m - 3 * n, (n + 1) ** 2)
        q2 = Fraction(2, (n + 1) ** 2)
        a.append(a[-1] * q0)
        v.append(v[-1] * q0 + a[-2] * q1)
        w.append(w[-1] * q0 + v[-2] * q1 + a[-2] * q2)
    return a, v, w


def residue(q, p):
    assert q.denominator % p, "Not a p-integral rational input"
    return q.numerator * pow(q.denominator, -1, p) % p


def check(p):
    assert p >= 7 and p % 6 == 1
    m, n_max = (p - 1) // 6, p - 1
    a, v, w = jets(p)
    end = Fraction(
        2 * (-1) ** m * factorial(m) * factorial(2 * m)
        * factorial(5 * m - 1) * factorial(4 * m - 1),
        factorial(n_max) ** 2,
    )
    assert w[-1] == end
    assert residue(end, p) == residue(Fraction(18, 5), p)
    forced = -40 * m * m * end
    assert residue(forced, p) == (-4) % p
    assert residue(forced / (2 ** p), p) == (-2) % p

    # Polynomial coefficients of L_m F2 + 2z(3theta-4m)F1 - 4zF0.
    # F2=2w. Degree p is essential: it is the terminal forcing, not zero.
    for k in range(p + 1):
        lhs = k * k * 2 * w[k] if k < p else Fraction(0)
        if k:
            lhs -= (k - 1 - m) * (k - 1 - 2 * m) * (2 * w[k - 1])
            lhs += 2 * (3 * (k - 1) - 4 * m) * v[k - 1]
            lhs -= 4 * a[k - 1]
        assert lhs == (forced if k == p else 0), (p, k, lhs)
    return residue(end, p), residue(forced, p)


if __name__ == "__main__":
    tested = [p for p in primes_upto(373) if p % 6 == 1]
    for p in tested:
        check(p)
    for p in (7, 13, 19, 373):
        print(f"p={p}: (w_(p-1), endpoint)={check(p)}")
    print(f"PASS {len(tested)} primes, full rational degree-by-degree checks")
