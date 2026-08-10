"""Dimension-nonselection boundary for the R004 divisor-grid candidate.

The current scale/divisor machinery can realize an isotropic exponent-grid
candidate of every finite positive rank.  Therefore P005 divisibility + unique
factorization + the equal-exponent divisor-grid construction do not select
physical dimension three.

This is a negative structural result, not a claim that every rank is physically
realized.  A future physical theory needs an additional rule that selects one
support rank.
"""
from __future__ import annotations

from enterprise_math.precision_isotropic_genesis import isotropic_genesis_signature
from enterprise_math.precision_prime_axes import prime_axis_rank, prime_factorization


def _positive(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def first_primes(count: int) -> tuple[int, ...]:
    _positive(count, "count")
    primes: list[int] = []
    candidate = 2
    while len(primes) < count:
        if all(candidate % prime for prime in primes if prime * prime <= candidate):
            primes.append(candidate)
        candidate = 3 if candidate == 2 else candidate + 2
    return tuple(primes)


def squarefree_support_for_rank(rank: int) -> int:
    """Construct one squarefree support with exactly ``rank`` prime axes."""
    primes = first_primes(rank)
    support = 1
    for prime in primes:
        support *= prime
    if any(exponent != 1 for _, exponent in prime_factorization(support)):
        raise AssertionError("constructed support must be squarefree")
    if prime_axis_rank(support) != rank:
        raise AssertionError("constructed support must have requested rank")
    return support


def isotropic_candidate_exists(rank: int, level: int) -> bool:
    _positive(rank, "rank")
    if isinstance(level, bool) or not isinstance(level, int) or level < 0:
        raise ValueError("level must be a non-negative integer")
    support = squarefree_support_for_rank(rank)
    signature = isotropic_genesis_signature(support, level)
    expected_dimension = 0 if level == 0 else rank
    expected_shape = () if level == 0 else (level + 1,) * rank
    return (
        signature.dimension == expected_dimension
        and signature.shape == expected_shape
    )


def current_structure_selects_three(max_rank_checked: int = 8) -> bool:
    """Finite executable witness that the construction is not rank-selective.

    The mathematical theorem is constructive for every positive finite rank:
    ``squarefree_support_for_rank(rank)`` supplies a support.  This bounded
    helper simply regression-checks several ranks and returns False whenever a
    non-three rank is also admitted, as it must be.
    """
    _positive(max_rank_checked, "max_rank_checked")
    admitted = {
        rank
        for rank in range(1, max_rank_checked + 1)
        if isotropic_candidate_exists(rank, 1)
    }
    return admitted == {3}
