#!/usr/bin/env python3
"""Author-side exact finite integer certificate for original signed W216.
This does not execute the native H0/B0 benchmark and is not an all-prime proof."""
from math import comb, isqrt

def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i:n + 1:i] = b'\x00' * (((n - i * i) // i) + 1)
    return [i for i in range(5, n + 1) if sieve[i]]

def W_recur(p):
    m = p ** 3
    a, s = 1, 1
    for k in range(p - 1):
        a = a * (2*k + 1) * (3*k + 1) * (3*k + 2) * pow(36 * (k+1)**3, -1, m) % m
        s = (s + (6*k + 7) * a) % m
    return s

def W_binom(p):
    m = p ** 3
    inv216 = pow(216, -1, m)
    power216, s = 1, 0
    for k in range(p):
        a = comb(2*k, k)**2 * comb(3*k, k) * power216 % m
        s = (s + (6*k + 1) * a) % m
        power216 = power216 * inv216 % m
    return s

def W_strata(p):
    m = p ** 3
    a = 1
    s = [0, 0, 0, 0]
    for k in range(p):
        v = (2 * k) // p + (3 * k) // p
        s[v] = (s[v] + (6*k + 1)*a) % m
        if k + 1 < p:
            a = a * (2*k + 1) * (3*k + 1) * (3*k + 2) * pow(36*(k+1)**3, -1, m) % m
    return s

def main():
    bound = 10000
    primes = primes_upto(bound)
    residue_counts = {r:0 for r in (1, 5, 7, 11, 13, 17, 19, 23)}
    failures, target_count = [], 0
    for p in primes:
        w = W_recur(p)
        character = 1 if p % 3 == 1 else -1
        residue_counts[p % 24] += 1
        if p % 24 in (13, 19):
            target_count += 1
        if (w - character*p) % p**3:
            failures.append((p, w, character*p % p**3))
    cross_primes = [7,13,17,19,23,37,43,109,139,157,373]
    crosschecks = []
    for p in cross_primes:
        x, y = W_recur(p), W_binom(p)
        assert x == y, (p, x, y)
        crosschecks.append((p, x))
    strata = W_strata(373)
    assert len(primes) == 1227 and target_count == 312 and not failures
    assert strata == [28094360, 38687933, 37008314, 0]
    assert sum(strata) % 373**3 == 373
    print("range 5..10000 total primes", len(primes))
    print("residue counts", residue_counts)
    print("original LIFT target primes", target_count)
    print("signed relation failures", len(failures), failures[:5])
    print("independent binomial checks", crosschecks)
    print("p373 original valuation strata", strata)
    print("p373 low-strata second digit", ((sum(strata[:2]) % 373**3) - 373) // 373**2)
    print("p373 v2 second digit", strata[2] // 373**2)
if __name__ == "__main__":
    main()
