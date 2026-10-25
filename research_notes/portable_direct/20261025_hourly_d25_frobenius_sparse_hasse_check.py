#!/usr/bin/env python3
"""Exact finite-field coefficient test of the D25 all-Hasse-jets cutoff theorem.
Pure standard library, no native CM experiment or formal acceptance.
"""
from math import factorial

PRIMES = (7, 13, 19, 31, 37, 43, 73, 103, 373)

def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] = (out[i + j] + x * y) % p
    return out

def check(p):
    left1 = [1]
    left2 = [1]
    for j in range(p - 1):
        left1 = mul(left1, [j % p, -1 % p], p)       # (-x)_(p-1)
        left2 = mul(left2, [j % p, -2 % p], p)       # (-2x)_(p-1)
    a = mul([(p - 1) % p, -1 % p], [(p - 1) % p, -2 % p], p)
    inv = pow(factorial(p - 1) ** 2, -1, p)
    boundary = mul(mul(mul(left1, left2, p), a, p), [(-inv) % p], p)

    predicted = [0] * (2 * p + 1)
    predicted[2] = -2 % p
    predicted[p + 1] = 4 % p
    predicted[2 * p] = -2 % p
    assert boundary == predicted, (p, "global polynomial cutoff")

    # Source's highest parameter coefficient yields the last Hasse consistency port.
    numer = mul(left1, left2, p)
    assert (numer[-1] * inv) % p == 1, (p, "top parameter jet")
    assert [(i, c) for i, c in enumerate(boundary) if c] == [
        (2, -2 % p), (p + 1, 4 % p), (2 * p, -2 % p)
    ], (p, "three Hasse ports")
    assert p % 6 == 1
    return (p, boundary[2], boundary[p + 1], boundary[2 * p])

if __name__ == "__main__":
    for p in PRIMES:
        print("PASS", *check(p))
    print(f"PASS all {len(PRIMES)} exact polynomial identities")
