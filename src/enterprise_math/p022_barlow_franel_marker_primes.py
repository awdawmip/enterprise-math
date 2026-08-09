"""Private Franel marker primes and coefficient-reading defect valuations.

Suppose a prime q divides exactly one Franel term F_j among F_1,...,F_N, with
valuation e>0.  If j is a prime-boundary index (2j-1 prime), then j itself has
no composite defect column.  For every composite defect

    D_n = F_n / prod_(k<n) F_k^alpha_(n,k),

the q-valuation is therefore exactly

    v_q(D_n) = -e * alpha_(n,j).

So a private Franel prime at a prime-boundary segment reads one coordinate of
the central-binomial elimination relation directly.

At N=150 the two primes used to saturate the 40-dimensional core have exactly
this form:
- 176459 is a simple private divisor of F_12, and 2*12-1=23 is prime;
- 73589 is a simple private divisor of F_66, and 2*66-1=131 is prime.
"""

from __future__ import annotations

from .p022_barlow_low_order_defect_reduction import (
    composite_A_relation_exponents,
    composite_indices,
    franel_defect_valuation,
    primes_through,
)
from .p022_barlow_low_order_identifiability import (
    p_adic_valuation,
    triple_moment_factor,
)

MARKER_12 = 176_459
MARKER_66 = 73_589
HORIZON_150 = 150


def _require_prime(prime: int) -> None:
    if isinstance(prime, bool) or not isinstance(prime, int) or prime <= 1:
        raise ValueError("prime must exceed one")
    if prime not in primes_through(prime):
        raise ValueError("value must be prime")


def franel_occurrence_indices(prime: int, horizon: int) -> tuple[int, ...]:
    """Indices 1..horizon whose Franel number is divisible by ``prime``."""
    _require_prime(prime)
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon <= 0:
        raise ValueError("horizon must be a positive integer")
    return tuple(
        index
        for index in range(1, horizon + 1)
        if p_adic_valuation(triple_moment_factor(index), prime) > 0
    )


def private_franel_marker(prime: int, horizon: int) -> tuple[int, int]:
    """Return unique marked index and valuation within the finite horizon."""
    occurrences = franel_occurrence_indices(prime, horizon)
    if len(occurrences) != 1:
        raise ValueError("prime is not a private Franel marker on this horizon")
    index = occurrences[0]
    valuation = p_adic_valuation(triple_moment_factor(index), prime)
    return index, valuation


def marker_reads_relation_coefficient(
    prime: int, marker_index: int, segment: int, *, horizon: int
) -> tuple[int, int]:
    """Compare v_q(D_n) with ``-e*alpha_(n,j)`` for a private prime marker."""
    index, valuation = private_franel_marker(prime, horizon)
    if index != marker_index:
        raise ValueError("marker_index does not match the private Franel occurrence")
    if 2 * marker_index - 1 not in primes_through(2 * marker_index - 1):
        raise ValueError("marker index must be a prime-boundary segment")
    if segment not in composite_indices(horizon):
        raise ValueError("segment must be a composite-boundary defect index")

    alpha = dict(composite_A_relation_exponents(segment)).get(marker_index, 0)
    expected = -valuation * alpha
    actual = franel_defect_valuation(segment, prime)
    return actual, expected


def verify_saturation_markers_150() -> bool:
    if private_franel_marker(MARKER_12, HORIZON_150) != (12, 1):
        raise AssertionError("176459 must remain a simple private marker of F_12")
    if private_franel_marker(MARKER_66, HORIZON_150) != (66, 1):
        raise AssertionError("73589 must remain a simple private marker of F_66")

    for segment in composite_indices(HORIZON_150):
        if marker_reads_relation_coefficient(
            MARKER_12, 12, segment, horizon=HORIZON_150
        )[0] != marker_reads_relation_coefficient(
            MARKER_12, 12, segment, horizon=HORIZON_150
        )[1]:
            raise AssertionError("F_12 marker row must equal relation coefficient row")
        if marker_reads_relation_coefficient(
            MARKER_66, 66, segment, horizon=HORIZON_150
        )[0] != marker_reads_relation_coefficient(
            MARKER_66, 66, segment, horizon=HORIZON_150
        )[1]:
            raise AssertionError("F_66 marker row must equal relation coefficient row")
    return True
