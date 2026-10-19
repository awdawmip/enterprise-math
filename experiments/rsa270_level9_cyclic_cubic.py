#!/usr/bin/env python3
"""
Regression verifier for the level-9 cyclic cubic reformulation.

Checks the fixed polynomial f(x)=x^3-3x+1:
- discriminant = 81;
- for primes r != 3, root count is 3 iff r == +/-1 mod 9, else 0;
- synthetic H2 semiprime branches {8,8} vs {2,5} give 9 vs 0 CRT roots.

Researcher-ID: EM-DIRECT-66DE45
No RSA-270 factor is used or produced.
"""
from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def f(x):
    return x * x * x - 3 * x + 1


def roots_mod_prime(p):
    return [x for x in range(p) if f(x) % p == 0]


def check_prime_splitting(bound=1000):
    count = 0
    for p in range(5, bound):
        if not is_prime(p) or p == 3:
            continue
        roots = roots_mod_prime(p)
        expected = 3 if p % 9 in (1, 8) else 0
        assert len(roots) == expected, (p, p % 9, roots)
        count += 1
    return count


def crt_root_count(p, q):
    # Number of roots modulo pq is the product of local counts by CRT.
    return len(roots_mod_prime(p)) * len(roots_mod_prime(q))


def check_h2_branches():
    primes = {2: [], 5: [], 8: []}
    for p in range(5, 300):
        if is_prime(p) and p % 3 == 2:
            primes[p % 9].append(p)

    tested = 0
    for p in primes[8][:8]:
        for q in primes[8][:8]:
            if p == q:
                continue
            assert (p * q) % 9 == 1
            assert crt_root_count(p, q) == 9
            tested += 1

    for p in primes[2][:8]:
        for q in primes[5][:8]:
            assert (p * q) % 9 == 1
            assert crt_root_count(p, q) == 0
            tested += 1

    return tested


def discriminant_monic_cubic(a, b, c):
    # x^3 + a x^2 + b x + c
    return a*a*b*b - 4*b*b*b - 4*a*a*a*c - 27*c*c + 18*a*b*c


if __name__ == "__main__":
    assert discriminant_monic_cubic(0, -3, 1) == 81
    print("discriminant: 81 PASS")
    print("prime splitting cases:", check_prime_splitting(), "PASS")
    print("H2 semiprime branch cases:", check_h2_branches(), "PASS")
    print("ALL PASS")
