"""Finite audit helpers for simultaneous fixed-prime P017 split patterns.

The asymptotic independence theorem is analytic/equidistribution mathematics.
This module only supplies exact finite pattern evaluation and counts for bounded
regression, using the already exact fixed-prime split predicate.
"""

from __future__ import annotations

from collections.abc import Iterable

from .p017_fixed_prime_split_density import actual_fixed_prime_split


def split_pattern(k: int, primes: Iterable[int]) -> tuple[bool, ...]:
    family = tuple(primes)
    if not family:
        raise ValueError("prime family must be nonempty")
    if len(family) != len(set(family)):
        raise ValueError("prime family must contain distinct primes")
    if k < max(family):
        raise ValueError("k must be at least the largest fixed prime")
    return tuple(actual_fixed_prime_split(k, prime) for prime in family)


def split_pattern_count(
    primes: Iterable[int], pattern: Iterable[bool], max_k: int
) -> int:
    family = tuple(primes)
    target = tuple(pattern)
    if len(family) != len(target) or not family:
        raise ValueError("prime family and pattern must be nonempty with equal length")
    if max_k < max(family):
        return 0
    return sum(
        split_pattern(k, family) == target
        for k in range(max(family), max_k + 1)
    )


def simultaneous_split_count(primes: Iterable[int], max_k: int) -> int:
    family = tuple(primes)
    return split_pattern_count(family, (True,) * len(family), max_k)
