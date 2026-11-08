"""Check original 216 grade-2 quotient against its new finite 3F2 source-port formula.

Standard-library exact integers. Author-side verification only, NOT native H0/B0.
Usage: python d25_w216_grade2_3f2_checker_20261108.py [max_prime]
"""
from math import factorial, comb, isqrt
import sys


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def verify(p):
    assert is_prime(p) and p > 3 and p % 6 == 1
    m = (p - 1) // 6
    N = 3 * m + 1

    # Exact finite hypergeometric K recurrence, all denominators p-units.
    k, S = 1, 0
    for r in range(m):
        S = (S + (6 * r + 4) * k) % p
        if r + 1 < m:
            num = (r + 1) * (6 * r + 5) * (6 * r + 7)
            den = 9 * (2 * r + 3) ** 3
            k = k * num * pow(den, -1, p) % p

    C = (N + 1) * pow(pow(factorial(N), 4, p) * pow(216, N, p) % p, -1, p) % p
    hyper = C * S % p

    # Independent original integer/binomial path, no Pochhammer coefficients.
    mod = p ** 3
    inv216 = pow(216, -1, mod)
    n_power = pow(inv216, N, mod)
    direct, source_digits = 0, []
    for n in range(N, 4 * m + 1):
        numerator = (6 * n + 1) * comb(2 * n, n) ** 2 * comb(3 * n, n)
        weighted_term = numerator * n_power % mod
        assert weighted_term % (p * p) == 0
        digit = weighted_term // (p * p)
        direct = (direct + digit) % p
        if p <= 19:
            source_digits.append(digit)
        n_power = n_power * inv216 % mod
    assert direct == hyper, (p, direct, hyper)
    return p, m, N, direct, S, C, source_digits if p <= 19 else None


if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    primes = [p for p in range(7, limit + 1) if p % 6 == 1 and is_prime(p)]
    results = [verify(p) for p in primes]
    print("all_exact_agree", len(results), "frozen_targets",
          sum(p % 24 in (13, 19) for p in primes))
    for p in (7, 13, 19, 37, 211, 373):
        if p <= limit:
            print(verify(p))
