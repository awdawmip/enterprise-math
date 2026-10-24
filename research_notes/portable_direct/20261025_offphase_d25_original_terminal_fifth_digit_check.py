#!/usr/bin/env python3
"""Exact finite falsification only; not the proof, Source run or independent review."""
from fractions import Fraction
from math import factorial, gcd, isqrt


def qualifying_primes(limit=1000):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for k in range(2, isqrt(limit) + 1):
        if sieve[k]:
            sieve[k*k:limit+1:k] = b"\x00" * ((limit-k*k)//k + 1)
    return [p for p in range(13, limit, 6) if sieve[p]]


def residue(x, mod):
    x = Fraction(x)
    assert gcd(x.denominator, mod) == 1
    return (x.numerator * pow(x.denominator, -1, mod)) % mod


def original_factorial_U(p):
    m = (p - 1) // 6
    x = Fraction(1, 108**(p-1) * factorial(2*m) * factorial(4*m)**2)
    for j in range(1, p - 1):
        x *= (p + j)**2
    for j in range(1, 2*m):
        x /= p + j
    return x


def check(p):
    m = (p - 1) // 6
    r = 2*m
    mod = p**5
    inv = lambda z: pow(z, -1, mod)
    half = inv(2)
    third = inv(3)
    fourth = inv(4)
    six = inv(6)
    twentyfour = inv(24)
    # q_p(108) modulo p^4; valid because 108^(p-1) is 1 modulo p.
    q = (pow(108, p-1, mod) - 1) // p
    def harmonic(n, k):
        return sum(pow(j, -k, mod) for j in range(1, n+1)) % mod
    h = [0] + [harmonic(r, k) for k in range(1, 5)]
    g = [0] + [harmonic(r-1, k) for k in range(1, 5)]
    full_h2 = harmonic(p-1, 2)
    assert full_h2 % p == 0
    T = full_h2 // p
    A = (4 - q - 2*h[1] - g[1]) % mod
    W = (4 + half*q*q - h[2] + half*g[2]) % mod
    D = (16*third - 2*T - third*q**3
         - 2*third*h[3] - third*g[3]) % mod
    F4 = (8 + fourth*q**4 - half*h[4] + fourth*g[4]) % mod
    B = (W + half*A*A) % mod
    C = (D + A*W + six*A**3) % mod
    E = (F4 + A*D + half*W*W + half*A*A*W
         + twentyfour*A**4) % mod
    pred = (2*m*(1+p*A+p*p*B+p**3*C+p**4*E)) % mod

    # Independent exact product inherited from the ORIGINAL factorial source.
    orig = 2*m*inv(pow(108, p-1, mod)) % mod
    for k in range(2, r+1):
        orig = orig * pow((1-p*inv(k)) % mod, 2, mod) % mod
    for j in range(1, p-1):
        orig = orig * pow((1+p*inv(j)) % mod, 2, mod) % mod
    for j in range(1, r):
        orig = orig * inv((1+p*inv(j)) % mod) % mod

    exact_coefficient = Fraction((p+1)*(2*p-1)**2*(30*p*p+77*p+40),
        2*(p+2)*(2*p+1)*(4*p-1)*(4*p+5))
    Cpoly = (-2 + Fraction(3,4)*p - Fraction(393,40)*p**2
             - Fraction(10051,400)*p**3 - Fraction(524817,4000)*p**4)
    assert orig == pred, (p, "terminal")
    assert residue(exact_coefficient, mod) == residue(Cpoly, mod), (p, "edge coefficient")
    if p in (13, 19, 31, 37, 43, 61, 67, 73, 79, 97, 103, 109, 127, 211):
        u = original_factorial_U(p)
        assert residue(u, mod) == pred, (p, "unexpanded original factorial")
        assert residue(u * exact_coefficient, mod) == (
            pred*residue(Cpoly, mod)) % mod, (p, "original old edge")
    return pred, residue(exact_coefficient, mod), (
        pred*residue(exact_coefficient, mod)) % mod


def main():
    primes = qualifying_primes()
    assert len(primes) == 79, len(primes)
    for p in primes:
        u, c, edge = check(p)
        if p in (13, 19, 31, 109, 211):
            print(f"p={p}: U={u} C={c} E0/p={edge} (mod p^5)")
    print("PASS: 79/79 p<1000 authentic unit and coefficient mod p^5")
    print("PASS: 14/14 independent unexpanded original factorial and old edge")


if __name__ == '__main__':
    main()
