"""Rank-two binary boundary for hyperoctahedral signed-channel repair.

For an equal positive chamber cluster p=(a,...,a), a microscopic sign choice
selects which labelled channels move inward to a-1 and which move outward to
a+1.  After quotienting labels, the transition retaining exactly k inward
channels has lift multiplicity C(d,k).

Consequences:
- d=2 is the only genuinely multi-channel rank for which every local repair
  multiplicity remains a power of two;
- every d>=3 has an explicit non-binary equal-cluster transition;
- prime valuations give an exact additive coordinate of total path-lift fiber
  size, while forgetting the ordered local-radix mechanism.
"""

from __future__ import annotations

from math import comb

from .p022_barlow_higher_channel_repair import (
    ChamberPath,
    is_power_of_two,
    path_lift_count,
    path_lift_factors,
    transition_multiplicity,
)

PrimeSignature = tuple[tuple[int, int], ...]


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def equal_cluster_target(
    dimension: int, magnitude: int, inward_count: int
) -> tuple[int, ...]:
    """Target with ``inward_count`` copies of a-1 and the rest a+1."""
    _require_positive("dimension", dimension)
    _require_positive("magnitude", magnitude)
    if (
        isinstance(inward_count, bool)
        or not isinstance(inward_count, int)
        or inward_count < 0
        or inward_count > dimension
    ):
        raise ValueError("inward_count must lie in 0..dimension")
    return (magnitude - 1,) * inward_count + (magnitude + 1,) * (
        dimension - inward_count
    )


def equal_cluster_transition_multiplicity(
    dimension: int, magnitude: int, inward_count: int
) -> int:
    """Exact C(d,k) lift multiplicity of one positive equal-cluster split."""
    target = equal_cluster_target(dimension, magnitude, inward_count)
    previous = (magnitude,) * dimension
    direct = transition_multiplicity(previous, target)
    expected = comb(dimension, inward_count)
    if direct != expected:
        raise AssertionError("equal-cluster transition must have binomial multiplicity")
    return expected


def nonbinary_equal_cluster_witness(dimension: int) -> tuple[int, int, int]:
    """Return ``(dimension,k,C(d,k))`` with a non-power-of-two coefficient.

    For d=3 use k=1, giving 3.  For d>=4 use k=2.  Then

        C(d,2)=d(d-1)/2.

    Since d and d-1 are coprime and exactly one is odd, if this were a power of
    two the odd member would have to equal one, impossible for d>=4.
    """
    if isinstance(dimension, bool) or not isinstance(dimension, int) or dimension < 3:
        raise ValueError("dimension must be at least three")
    inward_count = 1 if dimension == 3 else 2
    multiplicity = comb(dimension, inward_count)
    if is_power_of_two(multiplicity):
        raise AssertionError("chosen binomial witness must be non-binary")
    return dimension, inward_count, multiplicity


def all_equal_cluster_radices_binary_through_dimension_two(
    dimension: int,
) -> bool:
    """Whether all positive equal-cluster binomial radices are powers of two."""
    _require_positive("dimension", dimension)
    return all(is_power_of_two(comb(dimension, k)) for k in range(dimension + 1))


def prime_signature(value: int) -> PrimeSignature:
    """Exact prime-valuation coordinate of a positive integer."""
    _require_positive("value", value)
    remaining = value
    prime = 2
    output = []
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent:
            output.append((prime, exponent))
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        output.append((remaining, 1))
    return tuple(output)


def path_prime_repair_signature(path: ChamberPath) -> PrimeSignature:
    """Additive prime-valuation signature of the total path-lift fiber."""
    totals: dict[int, int] = {}
    for factor in path_lift_factors(path):
        for prime, exponent in prime_signature(factor):
            totals[prime] = totals.get(prime, 0) + exponent
    signature = tuple(sorted(totals.items()))
    if signature != prime_signature(path_lift_count(path)):
        raise AssertionError("prime valuations must add across local radices")
    return signature


def has_odd_prime_repair(path: ChamberPath) -> bool:
    """Whether exact total lift multiplicity contains an odd-prime factor."""
    return any(prime != 2 for prime, _ in path_prime_repair_signature(path))
