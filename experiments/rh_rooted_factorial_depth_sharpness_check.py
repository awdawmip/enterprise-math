#!/usr/bin/env python3
"""Finite regression for the rooted factorial-depth sharpness law.

For the increasing-prime Volterra operator K and the constant source 1,

    (K^r 1)(N,1)
      = sum_{q_1<...<q_r, product<=N}
          floor(N/product)/N.

The accompanying note proves that, for
r = alpha log N / log log N with fixed 0<alpha<1,

    (K^r 1)(N,1) = N^(-alpha+o(1)).

This checker verifies the exact finite path formula, the factorial upper
bound, and the polylogarithmic prime-shell lower bound. It is a finite
algebraic/diagnostic regression, not an asymptotic proof and not evidence
for the Riemann hypothesis.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial, log


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for prime in range(2, int(limit**0.5) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [value for value in range(2, limit + 1) if sieve[value]]


def rooted_path_mass(limit: int, depth: int, primes: list[int]) -> Fraction:
    """Exact sum of floor(N/product)/N over increasing prime paths."""
    total = Fraction(0)

    def visit(start: int, remaining: int, product_value: int) -> None:
        nonlocal total
        if remaining == 0:
            total += Fraction(limit // product_value, limit)
            return

        for index in range(start, len(primes)):
            prime = primes[index]
            next_product = product_value * prime
            if next_product > limit:
                break
            visit(index + 1, remaining - 1, next_product)

    visit(0, depth, 1)
    return total


def factorial_upper_bound(depth: int, primes: list[int]) -> Fraction:
    harmonic_mass = sum((Fraction(1, prime) for prime in primes), Fraction(0))
    return harmonic_mass**depth / factorial(depth)


def shell_lower_bound(
    limit: int, depth: int, primes: list[int]
) -> tuple[Fraction, int, int]:
    """Use primes in (Z/2,Z], Z=floor(N^(1/r)), as admissible paths."""
    shell_top = int(limit ** (1.0 / depth))
    while (shell_top + 1) ** depth <= limit:
        shell_top += 1
    while shell_top**depth > limit:
        shell_top -= 1

    shell_primes = [
        prime
        for prime in primes
        if 2 * prime > shell_top and prime <= shell_top
    ]
    count = len(shell_primes)
    lower = (
        Fraction(comb(count, depth), limit)
        if count >= depth
        else Fraction(0)
    )
    return lower, shell_top, count


def verify_exact_bounds() -> None:
    for limit in (100, 500, 2_000, 10_000):
        primes = primes_up_to(limit)
        for depth in (1, 2, 3):
            exact = rooted_path_mass(limit, depth, primes)
            upper = factorial_upper_bound(depth, primes)
            lower, shell_top, shell_count = shell_lower_bound(
                limit, depth, primes
            )
            assert lower <= exact <= upper
            if shell_count >= depth:
                assert shell_top**depth <= limit


def finite_critical_table() -> None:
    alpha = 0.5
    print(
        "N          r   Z=N^(1/r)  shell primes  "
        "lower bound       exact mass        factorial upper"
    )
    for limit in (10_000, 100_000, 1_000_000):
        depth = max(1, round(alpha * log(limit) / log(log(limit))))
        primes = primes_up_to(limit)
        exact = rooted_path_mass(limit, depth, primes)
        upper = factorial_upper_bound(depth, primes)
        lower, shell_top, shell_count = shell_lower_bound(
            limit, depth, primes
        )
        assert lower <= exact <= upper
        print(
            f"{limit:<10d} {depth:<3d} {shell_top:<12d} "
            f"{shell_count:<13d} {float(lower):<17.10g} "
            f"{float(exact):<17.10g} {float(upper):.10g}"
        )


def main() -> None:
    verify_exact_bounds()
    finite_critical_table()
    print("rooted factorial-depth sharpness regression passed")


if __name__ == "__main__":
    main()
