"""Bonferroni lower certificates for p-rough interval occupancy.

The exact p-rough count is a finite inclusion-exclusion sum over primes below p.
Odd inclusion-exclusion truncations give lower bounds for the complement of the
union of divisibility events.  A positive odd truncation therefore certifies
that the interval contains a p-rough integer without evaluating the full Mobius
sum.
"""

from __future__ import annotations

from itertools import combinations
from math import prod

from .legendre import primes_up_to
from .rough_interval_mobius import rough_interval_mobius_count


def intersection_sums(lower: int, upper: int, prime: int) -> tuple[int, ...]:
    """Return S_j, sums of j-fold small-prime divisibility intersections."""

    if lower < 1 or upper < lower:
        raise ValueError("require positive interval with lower <= upper")
    small_primes = tuple(primes_up_to(prime - 1))
    sums = []
    for depth in range(1, len(small_primes) + 1):
        total = 0
        for subset in combinations(small_primes, depth):
            divisor = prod(subset)
            total += upper // divisor - (lower - 1) // divisor
        sums.append(total)
    return tuple(sums)


def rough_bonferroni_lower_bound(
    lower: int, upper: int, prime: int, depth: int
) -> int:
    """Odd-depth Bonferroni lower bound for the p-rough interval count.

    ``depth=0`` is accepted only when no prime lies below ``prime`` (the p=2
    case), where every positive integer is p-rough and the count is exact.
    """

    if lower < 1 or upper < lower:
        raise ValueError("require positive interval with lower <= upper")
    small_primes = tuple(primes_up_to(prime - 1))
    if not small_primes:
        if depth != 0:
            raise ValueError("p=2 exact certificate uses depth 0")
        return upper - lower + 1
    if depth < 1 or depth > len(small_primes) or depth % 2 == 0:
        raise ValueError("depth must be an odd positive integer within the small-prime family")

    sums = intersection_sums(lower, upper, prime)
    value = upper - lower + 1
    for order in range(1, depth + 1):
        value += (-1) ** order * sums[order - 1]
    exact = rough_interval_mobius_count(lower, upper, prime)
    if value > exact:
        raise AssertionError("Bonferroni lower bound exceeded exact rough count")
    return value


def minimum_positive_bonferroni_depth(
    lower: int, upper: int, prime: int
) -> int | None:
    """Smallest odd truncation proving occupancy, or None if no odd truncation does.

    ``None`` does not imply that the interval is rough-empty.  Full exact
    inclusion-exclusion may still be positive after an even final correction.
    """

    small_primes = tuple(primes_up_to(prime - 1))
    if not small_primes:
        return 0
    for depth in range(1, len(small_primes) + 1, 2):
        if rough_bonferroni_lower_bound(lower, upper, prime, depth) > 0:
            return depth
    return None
