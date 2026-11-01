#!/usr/bin/env python3
"""AUTHOR-SIDE exact finite-prime diagnostics; does not establish a universal congruence.

Checks original 216 weighted sum, Van Hamme (E.2), and p-adic fourth-digit
obstructions using integer modular arithmetic with unit denominators.
"""
from math import comb, isqrt


def prime_list(n):
    sieve = bytearray(b'\x01') * n
    sieve[:2] = b'\x00\x00'
    for a in range(2, isqrt(n - 1) + 1):
        if sieve[a]:
            sieve[a * a:n:a] = b'\x00' * ((n - 1 - a * a) // a + 1)
    return [p for p in range(5, n) if sieve[p]]


def a216(p, power=3):
    modulus = p ** power
    a = 1
    result = 0
    for n in range(p):
        result = (result + (6 * n + 1) * a) % modulus
        if n < p - 1:
            # a[n+1]/a[n] = (2n+1)(3n+1)(3n+2)/(36(n+1)^3)
            a = (a * (2 * n + 1) * (3 * n + 1) * (3 * n + 2)
                 * pow(36 * (n + 1) ** 3, -1, modulus)) % modulus
    return result


def e2_van_hamme(p, power=3):
    assert p > 3
    modulus = p ** power
    m = (p - 1) // 3 if p % 3 == 1 else (2 * p - 1) // 3
    a, result = 1, 0
    for n in range(m + 1):
        result = (result + (6 * n + 1) * a) % modulus
        if n < m:
            # a[n+1]/a[n] = -(3n+1)^3/(27(n+1)^3)
            a = (-a * (3 * n + 1) ** 3
                 * pow(27 * (n + 1) ** 3, -1, modulus)) % modulus
    return result


def original_integer(p):
    modulus = p ** 3
    inverse_216 = pow(216, -1, modulus)
    scale = 1
    total = 0
    for n in range(p):
        total = (total + (6 * n + 1) * comb(2 * n, n) ** 2 * comb(3 * n, n) * scale) % modulus
        scale = scale * inverse_216 % modulus
    return total


def main():
    pp = prime_list(5000)
    frozen, p1, p2 = 0, 0, 0
    for p in pp:
        val = a216(p)
        expected = p if p % 3 == 1 else (-p) % p ** 3
        assert val == expected, (p, 'signed', val, expected)
        B = e2_van_hamme(p)
        if p % 3 == 1:
            p1 += 1
            assert B == p, (p, 'E2', B)
            assert val == B, (p, 'bridge', val, B)
        else:
            p2 += 1
            assert B == (-2 * p) % p ** 3, (p, 'E2 second class', B)
            assert (2 * val - B) % (p ** 3) == 0, (p, 'bridge second class', val, B)
        if p % 24 in (13, 19):
            frozen += 1
    samples = (5, 7, 11, 13, 19, 31, 37, 43, 67, 73, 373)
    for p in samples:
        assert a216(p) == original_integer(p), (p, 'integer independent')
    print('EXACT_PASS primes 5<=p<5000:', len(pp))
    print('p mod3 1:', p1, 'p mod3 2:', p2, 'frozen p mod24=13,19:', frozen)
    print('Original integer binomial cross-check samples:', samples)
    for p in (7, 13, 19, 37, 43, 73, 373):
        a4 = a216(p, 4)
        exp = p if p % 3 == 1 else (-p) % p ** 4
        correction = ((a4 - exp) // (p ** 3)) % p
        b4 = e2_van_hamme(p, 4)
        comparison4 = b4 if p % 3 == 1 else (b4 * pow(2, -1, p**4)) % (p**4)
        bridge4 = ((a4 - comparison4) // (p ** 3)) % p
        print('p=%d A4=%d signed4_digit=%d E2_4=%s bridge4_digit=%s' % (p,a4,correction,b4,bridge4))

if __name__ == '__main__':
    main()
