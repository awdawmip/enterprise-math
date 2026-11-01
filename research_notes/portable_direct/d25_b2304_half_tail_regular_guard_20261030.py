#!/usr/bin/env python3
"""Exact B2304 half-tail/regular-kernel guard.

Scientific scope: derived corollary of Guo--Zudilin (Adv. Math. 346, 2019).
This is scalar p-local arithmetic, NOT the native H0/B0 benchmark.
Only Python's standard library is used. No theorem status or Source authority implied.
"""
from math import comb, factorial


def primes_below(limit):
    sieve = bytearray(b"\x01") * limit
    if limit:
        sieve[0] = 0
    if limit > 1:
        sieve[1] = 0
    for p in range(2, int((limit - 1) ** 0.5) + 1):
        if sieve[p]:
            for j in range(p * p, limit, p):
                sieve[j] = 0
    return [p for p in range(limit) if sieve[p]]


def b_regular_kernel(p):
    """Return H and its source splits, reducing only after labeled accumulation."""
    assert p > 3 and p % 2
    n0 = (p + 1) // 2
    n2 = (2 * p - 1) // 3
    n3 = (3 * p - 1) // 4
    last = n3 - n0
    assert last >= 0 and n0 <= n2 < n3 + 1
    h_first = h_second = 0
    r = 1
    for s in range(last + 1):
        n = n0 + s
        if n <= n2:
            h_first = (h_first + (8 * s + 5) * r) % p
        else:
            h_second = (h_second + (8 * s + 5) * r) % p
        if s < last:
            den = (18 * pow(2 * s + 3, 3, p)) % p
            assert den != 0
            r = r * ((4 * s + 3) * (s + 1) * (4 * s + 5)) * pow(den, -1, p) % p
    # The numerator causes natural termination at the first index after the tail.
    assert (4 * last + 3) * (4 * last + 5) % p == 0
    return (h_first + h_second) % p, h_first, h_second


def b_original_term(n, p):
    q = p ** 3
    raw = comb(2 * n, n) ** 2 * comb(4 * n, 2 * n)
    return (8 * n + 1) * raw * pow(pow(2304, n, q), -1, q) % q


def b_factorial_term(n, p):
    q = p ** 3
    # Independent factorial-form integer numerator (4n)! / n!^4.
    raw = factorial(4 * n) // factorial(n) ** 4
    return (8 * n + 1) * raw * pow(pow(2304, n, q), -1, q) % q


def test_original(p):
    q = p ** 3
    n0 = (p + 1) // 2
    n2 = (2 * p - 1) // 3
    n3 = (3 * p - 1) // 4
    full = half = first = second = tail_after = 0
    for n in range(p):
        term = b_original_term(n, p)
        if n in (0, n0 - 1, n0, n2, n3, p - 1):
            assert term == b_factorial_term(n, p)
        full = (full + term) % q
        if n < n0:
            half = (half + term) % q
        elif n <= n2:
            first = (first + term) % q
        elif n <= n3:
            second = (second + term) % q
        else:
            tail_after = (tail_after + term) % q
            assert term == 0
    character = 1 if p % 3 == 1 else -1
    assert half == full == p * character % q
    assert (first + second) % q == 0 and tail_after == 0
    assert first % (p * p) == second % (p * p) == 0
    h, h1, h2 = b_regular_kernel(p)
    inv36 = pow(36, -1, p)
    assert first // (p * p) == h1 * inv36 % p
    assert second // (p * p) == h2 * inv36 % p
    assert h == 0
    k = p % 8  # 1, 3, 5, 7 for odd p
    root = (k * p - 1) // 8
    assert (8 * root + 1) % p == 0
    return dict(p=p, n0=n0, n2=n2, n3=n3,
                B_first_over_p2=first // (p * p),
                B_second_over_p2=second // (p * p),
                regular_H1=h1, regular_H2=h2, B_half=half,
                B_full=full, weighted_zero_index=root)


def main():
    primes = [p for p in primes_below(5000) if p >= 5]
    for p in primes:
        h, _, _ = b_regular_kernel(p)
        assert h == 0, ("REGULAR_KERNEL_FAIL", p, h)
    print("REGULAR_KERNEL_EXACT_PRIMES", len(primes))
    targets = [p for p in primes if p % 24 in (13, 19)]
    print("FROZEN_TARGET_PRIMES", len(targets))
    for p in (5, 7, 13, 19, 61, 67, 373):
        print("SOURCE_CERT", test_original(p))
    print("PASS_B2304_GZ_TWO_TRUNCATION_TAIL_AND_REGULAR_KERNEL")


if __name__ == "__main__":
    main()
