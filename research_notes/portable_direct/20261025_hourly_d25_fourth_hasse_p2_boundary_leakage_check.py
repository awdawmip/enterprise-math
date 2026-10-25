#!/usr/bin/env python3
"""Exact integer/rational author checks for D25 fourth Hasse cutoff forcing."""
from fractions import Fraction
from math import factorial, isqrt

def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))

def harmonic_mod(k, exponent, modulus):
    return sum(pow(pow(j, -1, modulus), exponent, modulus)
               for j in range(1, k + 1)) % modulus

def cutoff_coefficients(p, modulus):
    """Return [t^2,t^3,t^4] of (-m-t)_p(-2m-2t)_p/((p-1)!)^2."""
    m = (p - 1) // 6
    v0, v1, v2 = 1, 0, 0
    for shift, slope in ((m, 1), (2 * m, 2)):
        for j in range(p):
            h = j - shift
            if h == 0:
                continue
            v0, v1, v2 = (v0 * h) % modulus, (v1 * h - slope * v0) % modulus, (v2 * h - slope * v1) % modulus
    fac = 1
    for j in range(1, p):
        fac = fac * j % modulus
    scale = 2 * pow(fac, -2, modulus) % modulus
    return tuple(scale * x % modulus for x in (v0, v1, v2))

def rational_check(p):
    m = (p - 1) // 6
    facsq = factorial(p - 1) ** 2
    product = 1
    linear = Fraction(0)
    quadratic = Fraction(0)
    raw = [1, 0, 0]
    for shift, slope in ((m, 1), (2 * m, 2)):
        for j in range(p):
            h = j - shift
            if h == 0:
                continue
            product *= h
            linear += Fraction(slope, h)
            quadratic += Fraction(slope * slope, h * h)
            a, b, c = raw
            raw = [a * h, b * h - slope * a, c * h - slope * b]
    direct = Fraction(2 * raw[2], facsq)
    derived = Fraction(product, facsq) * (linear * linear - quadratic)
    assert direct == derived, (p, direct, derived)

def run():
    ps = [p for p in range(7, 501) if p % 6 == 1 and prime(p)]
    ps += [1327, 19963]
    for p in ps:
        assert prime(p) and p % 6 == 1
        m, mod = (p - 1) // 6, p * p
        e2, e3, e4 = cutoff_coefficients(p, mod)
        hm2 = harmonic_mod(m, 2, p)
        h2m2 = harmonic_mod(2 * m, 2, p)
        hm3 = harmonic_mod(m, 3, p)
        h2m3 = harmonic_mod(2 * m, 3, p)
        hall2 = harmonic_mod(p - 1, 2, mod)
        third_expected = -2 * p * (hm2 + 2 * h2m2) % mod
        fourth_expected = (-5 * hall2 + 2 * p * (hm3 + 4 * h2m3)) % mod
        assert e2 % p == 2 and e3 == third_expected and e4 == fourth_expected, (p, e2, e3, e4, third_expected, fourth_expected)
        assert hall2 % p == 0 and e4 % p == 0
        actual_at_half = (-e4 * pow(2, -p, mod)) % mod
        simplified_at_half = (-e4 * pow(2, -1, mod)) % mod
        assert actual_at_half == simplified_at_half
        if p in (7, 13, 19):
            rational_check(p)
        if p in (7, 13, 19, 31, 37, 73, 373, 1327, 19963):
            print(f"p={p}, e2={e2}, e3={e3}, e4={e4}, "
                  f"forcing_4={-e4 % mod}, at_half={actual_at_half}")
    print(f"PASS: {len(ps)} primes, all direct modular product / harmonic / observer checks; 3 exact Fraction checks")

if __name__ == "__main__":
    run()
