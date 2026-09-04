#!/usr/bin/env python3
"""Exact finite checks for the prime-winding carry/Chebyshev frontier.

All checks are integer divisibility or integer inequalities.  No logarithm,
floating approximation, numerical PNT input, or target value of tau is used.
"""

from __future__ import annotations

from math import comb, gcd


def factorint(n: int) -> dict[int, int]:
    assert n >= 1
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def is_prime(n: int) -> bool:
    return n >= 2 and factorint(n) == {n: 1}


def primes_upto(limit: int) -> list[int]:
    return [n for n in range(2, limit + 1) if is_prime(n)]


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def lcm_upto(limit: int) -> int:
    value = 1
    for n in range(1, limit + 1):
        value = lcm(value, n)
    return value


def vp_int(n: int, p: int) -> int:
    assert n >= 1 and is_prime(p)
    exponent = 0
    while n % p == 0:
        n //= p
        exponent += 1
    return exponent


def carry_count_double(n: int, p: int) -> int:
    assert n >= 0 and is_prime(p)
    carries = 0
    carry = 0
    while n > 0 or carry:
        digit = n % p
        n //= p
        carry = 1 if 2 * digit + carry >= p else 0
        carries += carry
    return carries


def central_carry_product(n: int) -> int:
    value = 1
    for p in primes_upto(2 * n):
        q = p
        while q <= 2 * n:
            epsilon = (2 * n) // q - 2 * (n // q)
            assert epsilon in (0, 1), (n, q, epsilon)
            value *= p**epsilon
            q *= p
    return value


def next_power_of_two_at_least(n: int) -> int:
    power = 1
    while power < n:
        power *= 2
    return power


def check_carry_product_and_valuations(limit: int = 500) -> None:
    for n in range(1, limit + 1):
        central = comb(2 * n, n)
        assert central_carry_product(n) == central, n
        for p in primes_upto(2 * n):
            projected = 0
            q = p
            while q <= 2 * n:
                projected += (2 * n) // q - 2 * (n // q)
                q *= p
            assert projected == vp_int(central, p), (n, p)
            assert projected == carry_count_double(n, p), (n, p)


def check_divisibility_sandwich(limit: int = 1000) -> None:
    for n in range(1, limit + 1):
        L_n = lcm_upto(n)
        L_2n = lcm_upto(2 * n)
        central = comb(2 * n, n)
        annulus = L_2n // L_n

        assert L_2n % L_n == 0
        assert central % annulus == 0, (n, annulus, central)
        assert L_2n % central == 0, (n, central, L_2n)

        # Exact finite central-shell size bounds.
        assert central <= 4**n
        assert (2 * n + 1) * central >= 4**n


def check_dyadic_upper_bound(max_exponent: int = 15) -> None:
    for m in range(0, max_exponent + 1):
        cutoff = 2**m
        # L_{2^m} <= product_{j=1}^m 4^(2^(j-1)) = 4^(2^m-1).
        assert lcm_upto(cutoff) <= 4 ** (cutoff - 1), m

        if m > 0:
            previous = 2 ** (m - 1)
            annulus = lcm_upto(cutoff) // lcm_upto(previous)
            assert comb(cutoff, previous) % annulus == 0
            assert comb(cutoff, previous) <= 4**previous


def check_all_cutoff_linear_envelopes(limit: int = 4000) -> None:
    for M in range(2, limit + 1):
        L_M = lcm_upto(M)

        # Exponentiated form of
        # psi(M) >= (M-1) log 2 - log(M+1).
        assert (M + 1) * L_M >= 2 ** (M - 1), M

        power = next_power_of_two_at_least(M)
        assert power < 2 * M
        assert L_M <= lcm_upto(power)
        assert lcm_upto(power) <= 4 ** (power - 1)

        # Exponentiated weakened all-M upper bound psi(M) < 4 M log 2.
        assert L_M < 2 ** (4 * M), M


def main() -> None:
    check_carry_product_and_valuations()
    check_divisibility_sandwich()
    check_dyadic_upper_bound()
    check_all_cutoff_linear_envelopes()
    print("prime-winding carry/Chebyshev exact checks: PASS")


if __name__ == "__main__":
    main()
