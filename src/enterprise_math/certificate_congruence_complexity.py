"""Finite congruence-language complexity extracted from Smith defect factors.

A certificate defect group with invariant factors

    s_1 | s_2 | ... | s_d

has one nontrivial cyclic congruence coordinate for each ``s_i>1``.  The number
of such factors is the minimal number of generators of the finite abelian
defect group, hence a lower/exact count of independent abstract congruence
guards needed to represent the full defect group type.

This is standard finite-abelian-group mathematics.  P025 uses it only to
separate defect *size* from certificate-language *guard count*.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import prod

from .certificate_image_index import LatticeDefectSignature


@dataclass(frozen=True)
class CongruenceComplexity:
    invariant_factors: tuple[int, ...]
    defect_order: int
    defect_exponent: int
    independent_guard_count: int
    cyclic: bool
    prime_guard_profile: tuple[tuple[int, int, tuple[int, ...]], ...]


def _factor_integer(n: int) -> tuple[tuple[int, int], ...]:
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    value = n
    result: list[tuple[int, int]] = []
    prime = 2
    while prime * prime <= value:
        exponent = 0
        while value % prime == 0:
            value //= prime
            exponent += 1
        if exponent:
            result.append((prime, exponent))
        prime += 1
    if value > 1:
        result.append((value, 1))
    return tuple(result)


def congruence_complexity_from_factors(
    invariant_factors: tuple[int, ...],
) -> CongruenceComplexity:
    """Return exact abstract congruence resources from Smith invariant factors."""
    previous = 1
    for factor in invariant_factors:
        if isinstance(factor, bool) or not isinstance(factor, int) or factor <= 0:
            raise ValueError("Smith invariant factors must be positive integers")
        if factor % previous:
            raise ValueError("Smith invariant factors must form a divisibility chain")
        previous = factor

    nontrivial = tuple(factor for factor in invariant_factors if factor > 1)
    order = prod(invariant_factors) if invariant_factors else 1
    exponent = invariant_factors[-1] if invariant_factors else 1
    guard_count = len(nontrivial)

    primes = sorted(
        {
            prime
            for factor in nontrivial
            for prime, _exponent in _factor_integer(factor)
        }
    )
    prime_profile: list[tuple[int, int, tuple[int, ...]]] = []
    for prime in primes:
        valuations: list[int] = []
        for factor in invariant_factors:
            value = factor
            exponent_p = 0
            while value % prime == 0:
                value //= prime
                exponent_p += 1
            valuations.append(exponent_p)
        local_guards = sum(exponent_p > 0 for exponent_p in valuations)
        prime_profile.append((prime, local_guards, tuple(valuations)))

    if prime_profile:
        max_local = max(local_guards for _prime, local_guards, _vals in prime_profile)
        if max_local != guard_count:
            raise AssertionError(
                "invariant-factor form must realize minimal generator count in a prime component"
            )
    elif guard_count != 0:
        raise AssertionError("nontrivial defect lost all prime factors")

    return CongruenceComplexity(
        invariant_factors=invariant_factors,
        defect_order=order,
        defect_exponent=exponent,
        independent_guard_count=guard_count,
        cyclic=guard_count <= 1,
        prime_guard_profile=tuple(prime_profile),
    )


def congruence_complexity(signature: LatticeDefectSignature) -> CongruenceComplexity:
    """Return congruence resources for one computed lattice defect signature."""
    result = congruence_complexity_from_factors(signature.invariant_factors)
    if result.defect_order != signature.saturation_index:
        raise AssertionError("Smith factors failed to reconstruct saturation index")
    return result
