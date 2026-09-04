#!/usr/bin/env python3
"""Exact finite checks for Selberg coefficient two and full residual closure.

The asymptotic estimates are proved in the accompanying research note.
This checker verifies the exact Möbius, harmonic-convolution, residual,
full-cutoff, and pair-energy identities over rational prime-log atoms.
"""

from __future__ import annotations

from fractions import Fraction
from math import isqrt
from typing import Iterable, Sequence

Q = Fraction


def qsum(values: Iterable[Q]) -> Q:
    return sum(values, Q(0))


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            for multiple in range(p * p, n + 1, p):
                sieve[multiple] = False
    return [p for p in range(2, n + 1) if sieve[p]]


LIMIT = 120
PRIME_LIMIT = 1200
PRIMES = primes_upto(PRIME_LIMIT)
PRIME_LOG = {
    p: Q((p % 7) + 1, (p % 5) + 1)
    for p in PRIMES
}


def factor(n: int) -> dict[int, int]:
    if n < 1:
        raise ValueError("positive integer required")
    out: dict[int, int] = {}
    value = n
    p = 2
    while p * p <= value:
        while value % p == 0:
            out[p] = out.get(p, 0) + 1
            value //= p
        p += 1
    if value > 1:
        out[value] = out.get(value, 0) + 1
    return out


def mobius(n: int) -> int:
    factors = factor(n)
    if any(exponent > 1 for exponent in factors.values()):
        return 0
    return -1 if len(factors) % 2 else 1


def formal_log(n: int) -> Q:
    return qsum(
        exponent * PRIME_LOG[prime]
        for prime, exponent in factor(n).items()
    )


def formal_lambda(n: int) -> Q:
    if n <= 1:
        return Q(0)
    factors = factor(n)
    if len(factors) != 1:
        return Q(0)
    return PRIME_LOG[next(iter(factors))]


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def harmonic(n: int) -> Q:
    return qsum(Q(1, m) for m in range(1, n + 1))


def log_harmonic(n: int) -> Q:
    return qsum(formal_log(m) / m for m in range(1, n + 1))


def first_mass(n: int) -> Q:
    return qsum(formal_lambda(m) / m for m in range(1, n + 1))


def psi(n: int) -> Q:
    return qsum(formal_lambda(m) for m in range(1, n + 1))


def remainder(n: int) -> Q:
    return psi(n) - n


def normalized_remainder(n: int) -> Q:
    return remainder(n) / n


def selberg_square(n: int) -> Q:
    return qsum(
        formal_lambda(a) * formal_lambda(b)
        for a in range(1, n + 1)
        for b in range(1, n // a + 1)
    )


def weighted_log_sum(n: int) -> Q:
    return qsum(
        formal_lambda(m) * formal_log(m)
        for m in range(1, n + 1)
    )


def log_factorial(n: int) -> Q:
    return qsum(formal_log(m) for m in range(1, n + 1))


def pair_energy(weights: Sequence[Q], values: Sequence[Q]) -> Q:
    return qsum(
        wi * wj * (xi - xj) ** 2
        for wi, xi in zip(weights, values)
        for wj, xj in zip(weights, values)
    )


def check_pointwise_selberg_identity() -> None:
    for n in range(1, LIMIT + 1):
        lhs = qsum(
            mobius(d) * formal_log(n // d) ** 2
            for d in divisors(n)
        )
        rhs = (
            formal_lambda(n) * formal_log(n)
            + qsum(
                formal_lambda(d) * formal_lambda(n // d)
                for d in divisors(n)
            )
        )
        assert lhs == rhs, (n, lhs, rhs)


def check_summatory_selberg_identity() -> None:
    for n in range(1, LIMIT + 1):
        lhs = weighted_log_sum(n) + selberg_square(n)
        rhs = qsum(
            mobius(d)
            * qsum(
                formal_log(m) ** 2
                for m in range(1, n // d + 1)
            )
            for d in range(1, n + 1)
        )
        assert lhs == rhs, (n, lhs, rhs)


def check_harmonic_mobius_convolution() -> None:
    for n in range(1, LIMIT + 1):
        lhs = qsum(
            Q(mobius(d), d) * harmonic(n // d)
            for d in range(1, n + 1)
        )
        assert lhs == 1, (n, lhs)


def check_log_harmonic_mobius_convolution() -> None:
    for n in range(1, LIMIT + 1):
        lhs = qsum(
            Q(mobius(d), d) * log_harmonic(n // d)
            for d in range(1, n + 1)
        )
        assert lhs == first_mass(n), (n, lhs, first_mass(n))


def check_factorial_return() -> None:
    for n in range(1, LIMIT + 1):
        lhs = qsum(
            formal_lambda(q) * (n // q)
            for q in range(1, n + 1)
        )
        assert lhs == log_factorial(n), (n, lhs, log_factorial(n))


def check_ideal_selberg_residual_decomposition() -> None:
    for n in range(2, LIMIT + 1):
        direct = (
            formal_log(n) * remainder(n)
            + qsum(
                formal_lambda(q) * remainder(n // q)
                for q in range(1, n + 1)
            )
        )
        complement = qsum(
            formal_lambda(q)
            * (formal_log(n) - formal_log(q))
            for q in range(1, n + 1)
        )
        divisor_return = qsum(
            formal_lambda(q) * (n // q)
            for q in range(1, n + 1)
        )
        decomposed = (
            weighted_log_sum(n)
            + selberg_square(n)
            - 2 * n * formal_log(n)
            + complement
            + n * formal_log(n)
            - divisor_return
        )
        assert direct == decomposed, (n, direct, decomposed)


def full_residual(n: int) -> Q:
    return (
        first_mass(n) * normalized_remainder(n)
        + qsum(
            formal_lambda(q)
            / q
            * normalized_remainder(n // q)
            for q in range(1, n + 1)
        )
    )


def ideal_first_mass_residual(n: int) -> Q:
    return (
        first_mass(n) * remainder(n)
        + qsum(
            formal_lambda(q) * remainder(n // q)
            for q in range(1, n + 1)
        )
    )


def floor_deformation(n: int) -> Q:
    total = Q(0)
    for q in range(1, n + 1):
        weight = formal_lambda(q)
        if weight == 0:
            continue
        child = n // q
        dilation = Q(n, q * child)
        total += (
            weight
            * (dilation - 1)
            * remainder(child)
            / n
        )
    return total


def check_full_residual_decomposition() -> None:
    for n in range(2, LIMIT + 1):
        assert full_residual(n) == (
            ideal_first_mass_residual(n) / n
            + floor_deformation(n)
        ), n


def check_full_cutoff_return() -> None:
    for n in range(3, LIMIT + 1):
        for cutoff in range(2, min(n, 12) + 1):
            base = first_mass(cutoff)
            tail_coefficient = first_mass(n) - base
            present = normalized_remainder(n)
            fixed_transport = qsum(
                formal_lambda(q)
                / q
                * normalized_remainder(n // q)
                for q in range(1, cutoff + 1)
            )
            tail_transport = qsum(
                formal_lambda(q)
                / q
                * normalized_remainder(n // q)
                for q in range(cutoff + 1, n + 1)
            )
            lhs = (
                (base + tail_coefficient) * present
                + fixed_transport
            )
            rhs = full_residual(n) - tail_transport
            assert lhs == rhs, (n, cutoff, lhs, rhs)


def check_high_full_tail_monotonicity() -> None:
    for y in range(3, 11):
        outer_tail_mass = first_mass(y * y) - first_mass(y)
        for a in range(2, y + 1):
            if formal_lambda(a) == 0:
                continue
            high = (y**3) // a
            truncated_endpoint = high // y
            truncated_tail = (
                first_mass(truncated_endpoint) - first_mass(y)
            )
            full_tail = first_mass(high) - first_mass(y)
            assert Q(0) <= truncated_tail <= outer_tail_mass
            assert truncated_tail <= full_tail
            assert truncated_tail**2 <= outer_tail_mass * full_tail
            for q in range(y + 1, high + 1):
                if formal_lambda(q) != 0:
                    assert high // q < y * y


def check_low_tail_scale() -> None:
    for y in range(3, 11):
        for b in range(y + 1, y * y + 1):
            if formal_lambda(b) == 0:
                continue
            low = (y**3) // b
            assert low < y * y
            for q in range(y + 1, low + 1):
                if formal_lambda(q) != 0:
                    assert low // q < y


def check_bounded_residual_pair_energy() -> None:
    weights = [Q(1), Q(3, 2), Q(2), Q(5, 4)]
    values = [Q(-2), Q(1, 3), Q(7, 4), Q(5, 2)]
    bound = max(abs(value) for value in values)
    total = qsum(weights)
    assert pair_energy(weights, values) <= 4 * bound**2 * total**2


def main() -> None:
    checks = [
        check_pointwise_selberg_identity,
        check_summatory_selberg_identity,
        check_harmonic_mobius_convolution,
        check_log_harmonic_mobius_convolution,
        check_factorial_return,
        check_ideal_selberg_residual_decomposition,
        check_full_residual_decomposition,
        check_full_cutoff_return,
        check_high_full_tail_monotonicity,
        check_low_tail_scale,
        check_bounded_residual_pair_energy,
    ]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")
    print("PASS all Selberg coefficient-two/full-residual checks")


if __name__ == "__main__":
    main()
