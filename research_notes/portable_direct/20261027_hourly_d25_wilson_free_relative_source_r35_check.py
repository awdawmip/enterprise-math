#!/usr/bin/env python3
"""Exact original-source relative transfer; AUTHOR-only, not native CM experiment."""
from fractions import Fraction
from math import factorial, gcd


def primes_19_24(limit=2000):
    for p in range(19, limit, 24):
        if all(p % d for d in range(2, int(p**0.5) + 1)):
            yield p


def modulo(q, n):
    assert isinstance(q, Fraction)
    assert gcd(q.denominator, n) == 1
    return (q.numerator * pow(q.denominator, -1, n)) % n


def verify(p):
    assert p % 24 == 19
    k, r, R = (3*p - 1)//8, (p - 3)//8, (p - 1)//2
    w = Fraction((6*k+1)*factorial(2*k)*factorial(3*k), factorial(k)**5*216**k)
    s = Fraction((8*k+1)*factorial(4*k), factorial(k)**4*2304**k)
    gamma = s / (p*w)
    G = Fraction(12*3**k*factorial(k)*factorial(R), 32**k*factorial(2*k)*factorial(r))
    exact = G / (1+9*p)
    for j in range(r+1, R+1):
        exact *= 1 + Fraction(p, j)
    assert exact == gamma, (p, "EXACT")
    h1 = sum((Fraction(1, j) for j in range(r+1, R+1)), Fraction(0))
    h2 = sum((Fraction(1, j*j) for j in range(r+1, R+1)), Fraction(0))
    approximate = G*(1+p*(h1-9)+p*p*((h1*h1-h2)/2-9*h1+81))
    assert modulo(gamma, p**3) == modulo(approximate, p**3), (p, "JET")
    assert modulo(gamma, p) != 0, (p, "UNIT")
    return p, modulo(gamma, p**3)


if __name__ == "__main__":
    rows = [verify(p) for p in primes_19_24()]
    print("PASS", len(rows), "prime inputs: exact rational T1, p^3 jet T2, unit assertions")
    for row in rows:
        if row[0] in (19,43,67,139,163,211):
            print(*row)
