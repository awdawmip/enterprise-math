"""Two-rank primitive coverage criterion for global Franel-defect independence.

For each composite-boundary defect D_n, an automatic triangular valuation pivot
may come from either:

1. a primitive Franel prime at rank n, giving +v_p(F_n); or
2. when 2n-3 is prime, a primitive Franel prime at rank n-1, giving
   -v_p(F_(n-1)) by the successor-capture theorem.

Thus the old sufficient condition 'one primitive Franel prime at every
composite-boundary rank n' is stronger than necessary.  It suffices that every
composite defect column has primitive coverage in this two-rank window.

Because a primitive prime has one unique first rank, rows chosen for distinct
columns are automatically distinct.  Each row vanishes on all earlier defect
columns, so the resulting valuation matrix is triangular.  If every chosen
primitive depth has absolute value one, the finite certificate is unimodular
(up to determinant sign).
"""

from __future__ import annotations

from .p022_barlow_low_order_defect_reduction import (
    _is_prime,
    composite_indices,
    franel_defect_valuation,
)
from .p022_barlow_primitive_defect_criterion import (
    is_primitive_franel_divisor,
    primitive_defect_pivot,
)
from .p022_barlow_primitive_successor_capture import primitive_successor_capture_valuation


def _require_segment(segment: int) -> None:
    if isinstance(segment, bool) or not isinstance(segment, int) or segment < 2:
        raise ValueError("segment must be an integer at least two")
    if _is_prime(2 * segment - 1):
        raise ValueError("segment must have composite odd boundary")


def two_rank_candidate_ranks(segment: int) -> tuple[int, ...]:
    """Ranks that can provide an automatic primitive pivot for D_n."""
    _require_segment(segment)
    candidates = [segment]
    predecessor = segment - 1
    if predecessor >= 2 and _is_prime(2 * predecessor - 1):
        candidates.append(predecessor)
    return tuple(candidates)


def two_rank_primitive_pivot(segment: int, source_rank: int, prime: int) -> int:
    """Return the signed triangular pivot supplied by one allowed source rank."""
    _require_segment(segment)
    if source_rank not in two_rank_candidate_ranks(segment):
        raise ValueError("source_rank is not in the automatic two-rank capture window")
    if not is_primitive_franel_divisor(source_rank, prime):
        raise ValueError("prime must be primitive at source_rank")

    if source_rank == segment:
        value = primitive_defect_pivot(segment, prime)
        if value <= 0:
            raise AssertionError("current-rank primitive pivot must be positive")
        return value

    # source_rank=segment-1 and its odd boundary is prime by candidate rule.
    value = primitive_successor_capture_valuation(source_rank, prime)
    if value >= 0:
        raise AssertionError("predecessor primitive pivot must be negative")
    return value


def two_rank_row_is_triangular(
    segment: int,
    source_rank: int,
    prime: int,
    earlier_composite_segments: tuple[int, ...],
) -> bool:
    """Verify zero valuations on all earlier declared defect columns."""
    pivot = two_rank_primitive_pivot(segment, source_rank, prime)
    if pivot == 0:
        raise AssertionError("two-rank primitive pivot must be nonzero")
    for previous in earlier_composite_segments:
        if previous >= segment:
            raise ValueError("earlier composite segments must be strictly earlier")
        if franel_defect_valuation(previous, prime) != 0:
            return False
    return True


def two_rank_certificate_diagonal(
    max_segment: int,
    markers: tuple[tuple[int, int, int], ...],
) -> tuple[int, ...]:
    """Return tail pivot 1 plus signed primitive pivots for every composite D_n.

    Each marker is `(segment, source_rank, prime)`.  Segments must cover exactly
    all composite odd-boundary indices through max_segment in increasing order.
    """
    if isinstance(max_segment, bool) or not isinstance(max_segment, int) or max_segment <= 0:
        raise ValueError("max_segment must be a positive integer")
    expected_segments = composite_indices(max_segment)
    marker_segments = tuple(segment for segment, _, _ in markers)
    if marker_segments != expected_segments:
        raise ValueError("markers must cover composite indices exactly in order")

    diagonal = [1]  # v_2 of the hidden-tail defect
    earlier: list[int] = []
    used_primes: set[int] = set()
    for segment, source_rank, prime in markers:
        if prime in used_primes:
            raise ValueError("one primitive prime row cannot be reused for two columns")
        if not two_rank_row_is_triangular(segment, source_rank, prime, tuple(earlier)):
            raise AssertionError("two-rank primitive row lost triangularity")
        diagonal.append(two_rank_primitive_pivot(segment, source_rank, prime))
        earlier.append(segment)
        used_primes.add(prime)
    return tuple(diagonal)


def two_rank_certificate_is_unimodular(
    max_segment: int,
    markers: tuple[tuple[int, int, int], ...],
) -> bool:
    """Absolute unit diagonal iff the triangular integer determinant is ±1."""
    diagonal = two_rank_certificate_diagonal(max_segment, markers)
    return all(abs(value) == 1 for value in diagonal)
