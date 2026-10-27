#!/usr/bin/env python3
"""R46 affine-rank no-go from actual p-free factorial sources (no native run)."""
from fractions import Fraction
from math import isqrt


def primes(limit=997):
    for p in range(19, limit + 1):
        if p % 6 == 1 and all(p % j for j in range(2, isqrt(p) + 1)):
            yield p


def modq(fr, p):
    assert fr.denominator % p
    return fr.numerator * pow(fr.denominator, -1, p) % p


def pfactorials(p):
    f = [1] * (4 * p)
    for j in range(1, 4 * p):
        f[j] = f[j - 1] * (j // p if j % p == 0 else j) % p
    return f


def pair(p, k, fs):
    assert 1 <= k and 4 * k < p
    n, d = 1 - 64 * k * k, 1 - 36 * k * k
    assert n * d % p
    b = 3 * pow(32, -1, p) % p

    def tau(t):
        return (pow(b, t, p) * fs[t] * fs[4 * t]
                * pow(fs[2 * t] * fs[3 * t] % p, -1, p)) % p

    weights = ((8 * k + 1) * (8 * (p - k) + 1)
               * pow((6 * k + 1) * (6 * (p - k) + 1), -1, p)) % p
    return weights * tau(k) * tau(p - k) % p


def run():
    f = {k: Fraction(3, 16) * Fraction(1 - 64 * k*k, 1 - 36 * k*k)
         for k in range(1, 5)}
    d2 = f[3] - 2*f[2] + f[1]
    d3 = f[4] - 3*f[3] + 3*f[2] - f[1]
    d124 = f[4] - 3*f[2] + 2*f[1]
    assert d2 == Fraction(1191, 461890)
    assert d3 == Fraction(-58644, 26558675)
    assert d124 == Fraction(909, 164450)
    cases = observations = 0
    exception_397 = None
    samples = []
    for p in primes():
        fs = pfactorials(p)
        ks = (1, 2, 4) if p == 19 else ((1, 2, 3) if p == 31 else (1, 2, 3, 4))
        observed = {}
        for k in ks:
            value = pair(p, k, fs)
            assert value == modq(f[k], p), (p, k, value)
            observed[k] = value
            observations += 1
        if p == 19:
            assert (observed[4]-3*observed[2]+2*observed[1]) % p == modq(d124,p) != 0
        elif p == 31:
            assert (observed[3]-2*observed[2]+observed[1]) % p == modq(d2,p) != 0
        else:
            check2 = (observed[3]-2*observed[2]+observed[1]) % p
            check3 = (observed[4]-3*observed[3]+3*observed[2]-observed[1]) % p
            assert check2 == modq(d2,p)
            assert check3 == modq(d3,p)
            assert check2 or check3
            if p == 397:
                assert check2 == 0 and check3 != 0
                exception_397 = (p, check2, check3)
            else:
                assert check2 != 0
        cases += 1
        if p in (19, 31, 37, 181, 397, 733):
            samples.append((p, observed))

    print("R46 PASS:", cases, "primes", observations,
          "original factorial source-pair tests; exception_397", exception_397)
    for item in samples:
        print(" ", item)


if __name__ == "__main__":
    run()
