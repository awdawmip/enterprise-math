#!/usr/bin/env python3
"""Exact-integer author-side checks for D25 original-216 and dual kernel.

A finite test is not a proof of the all-prime character-pattern conjecture.
No H0/B0 native Frobenius computation is performed here.
"""
from math import comb, factorial, isqrt

PRIME_LIMIT = 6000


def primes_below(bound):
    for n in range(5, bound):
        if all(n % d for d in range(2, isqrt(n) + 1)):
            yield n


def original_modular_terms(p, exponent=3):
    modulus = p ** exponent
    t = 1
    for n in range(p):
        yield n, t
        if n < p - 1:
            numerator = (2 * n + 1) * (3 * n + 1) * (3 * n + 2)
            denominator = 36 * (n + 1) ** 3
            t = t * numerator * pow(denominator, -1, modulus) % modulus


def original_weighted_sum(p):
    modulus = p ** 3
    return sum((6 * n + 1) * t for n, t in original_modular_terms(p)) % modulus


def original_independent_binomial(p):
    modulus = p ** 3
    inv216 = pow(216, -1, modulus)
    a = 1
    value = 0
    for n in range(p):
        value = (value + (6 * n + 1) * comb(2 * n, n) ** 2 * comb(3 * n, n) * a) % modulus
        a = a * inv216 % modulus
    return value


def dual_s_recurrence(p):
    """mod-p dual hypergeometric finite moment, r=0,...,m-1."""
    m = (p - 1) // 6
    h = 1
    s = 0
    for r in range(m):
        s = (s + (66 * r * r - 25 * r + 3) * h) % p
        if r < m - 1:
            den = 3 * (6 * r + 7) * (3 * r + 4) * (r + 1)
            assert den % p
            h = h * 4 * (3 * r - 1) ** 3 * pow(den, -1, p) % p
    return 9 * pow(32, -1, p) * s % p


def dual_s_binomial(p):
    """Fixed-row binomial dualization, uses only p-unit denominators."""
    m = (p - 1) // 6
    s = 0
    for r in range(m):
        den = comb(m - 1, r) * comb(2 * m - 1, r)
        assert den % p
        s += ((66 * r * r - 25 * r + 3) * pow(-2, r, p)
              * pow(comb(4 * m + 1, r), 3, p) * pow(den, -1, p))
    return 9 * pow(32, -1, p) * s % p


def single_seed(p):
    m = (p - 1) // 6
    return (-2 * factorial(4 * m + 2)
            * pow(factorial(2 * m + 1), -5, p)
            * pow(216, -(2 * m + 1), p)) % p


def high_tail_original(p):
    m = (p - 1) // 6
    modulus = p ** 3
    acc = 0
    for n, t in original_modular_terms(p):
        if 3 * m + 1 <= n <= 4 * m:
            acc += (66*n*n + 113*n + 49) * t * pow(9*(n+1)**3, -1, modulus)
    return acc % modulus


def main():
    primes = list(primes_below(PRIME_LIMIT))
    conjecture_tests = 0
    kernel_tests = 0
    high_tests = 0
    split_targets = 0
    for p in primes:
        observed = original_weighted_sum(p)
        sign = 1 if p % 3 == 1 else -1
        expected = sign * p % (p ** 3)
        assert observed == expected, ("character-conjecture-counterexample", p, observed, expected)
        conjecture_tests += 1
        if p % 24 in (13, 19):
            split_targets += 1
        if p % 6 == 1:
            sr = dual_s_recurrence(p)
            sb = dual_s_binomial(p)
            assert sr == sb, ("binomial-dualization-failed", p, sr, sb)
            kernel_tests += 1
            if p < 400:
                u0 = single_seed(p)
                assert u0 % p
                high = high_tail_original(p)
                predicted = p ** 2 * sr * pow(u0, -1, p) % (p**3)
                assert high == predicted, ("native-index-scalar-tail-mismatch", p, high, predicted)
                high_tests += 1
    for p in (5, 7, 13, 19, 37, 43, 211, 373):
        assert original_weighted_sum(p) == original_independent_binomial(p)
    p = 373
    m = (p-1)//6
    seed = single_seed(p)
    moment = dual_s_binomial(p)
    high = high_tail_original(p)
    assert (seed,moment,high) == (320,230,8208611)
    print("PASS_D25_FIXED_ROW_BINOMIAL_DUALIZATION", kernel_tests, "p=1(mod6) primes")
    print("PASS_D25_ORIGINAL_HIGH_TAIL_BRIDGE", high_tests, "p=1(mod6) primes <400")
    print("OBSERVED_UNPROVED_ALL_PRIME_CHARACTER_PATTERN", conjecture_tests,
          "primes <", PRIME_LIMIT, "; frozen target residue-class count", split_targets)
    print("P373_CERTIFICATE", {"m":m,"u0":seed,"S_m":moment,"high_tail_mod_p3":high,
                               "W_mod_p3":original_weighted_sum(p)})


if __name__ == "__main__":
    main()
