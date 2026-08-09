"""Primitive-Franel-divisor criterion for global defect independence.

For composite-boundary indices n, the pure defect is

    D_n = F_n / prod_(j<n) F_j^alpha_(n,j).

If q_n is a primitive prime divisor of F_n relative to the earlier Franel
terms -- q_n|F_n and q_n does not divide any F_j for j<n -- then

    v_(q_n)(D_m)=0  for m<n,
    v_(q_n)(D_n)=v_(q_n)(F_n)>0.

Thus one primitive Franel divisor per composite-boundary index gives a
triangular valuation certificate for multiplicative independence of all pure
defects.  If every chosen primitive valuation is one, the finite certificate
is unimodular.  This is a sufficient condition, not a claimed primitive-divisor
theorem for Franel numbers.
"""

from __future__ import annotations

from .p022_barlow_low_order_defect_reduction import (
    composite_indices,
    franel_defect_valuation,
)
from .p022_barlow_low_order_identifiability import (
    p_adic_valuation,
    triple_moment_factor,
)


def _require_prime_candidate(prime: int) -> None:
    if isinstance(prime, bool) or not isinstance(prime, int) or prime <= 1:
        raise ValueError("prime must exceed one")


def is_primitive_franel_divisor(segment: int, prime: int) -> bool:
    """Exact finite test: prime first divides the Franel sequence at segment."""
    if isinstance(segment, bool) or not isinstance(segment, int) or segment <= 0:
        raise ValueError("segment must be a positive integer")
    _require_prime_candidate(prime)
    if p_adic_valuation(triple_moment_factor(segment), prime) <= 0:
        return False
    return all(
        p_adic_valuation(triple_moment_factor(previous), prime) == 0
        for previous in range(1, segment)
    )


def primitive_defect_pivot(segment: int, prime: int) -> int:
    """Exact diagonal valuation contributed by a primitive Franel divisor."""
    if not is_primitive_franel_divisor(segment, prime):
        raise ValueError("prime is not primitive at the declared Franel segment")
    if segment not in composite_indices(segment):
        raise ValueError("primitive defect pivot is needed only at composite boundary")
    expected = p_adic_valuation(triple_moment_factor(segment), prime)
    actual = franel_defect_valuation(segment, prime)
    if actual != expected:
        raise AssertionError("primitive prime must survive unchanged in D_n")
    return actual


def primitive_row_is_triangular(
    segment: int, prime: int, earlier_composite_segments: tuple[int, ...]
) -> bool:
    """Verify zero valuations on all declared earlier defect columns."""
    pivot = primitive_defect_pivot(segment, prime)
    if pivot <= 0:
        raise AssertionError("primitive pivot must be positive")
    for previous in earlier_composite_segments:
        if previous >= segment:
            raise ValueError("earlier_composite_segments must be strictly earlier")
        if franel_defect_valuation(previous, prime) != 0:
            return False
    return True


def primitive_certificate_diagonal(
    max_segment: int,
    markers: tuple[tuple[int, int], ...],
) -> tuple[int, ...]:
    """Return tail pivot 1 followed by primitive-defect diagonal valuations.

    ``markers`` must list exactly one `(segment,prime)` for every composite
    boundary index through ``max_segment``, in increasing segment order.
    The resulting valuation matrix has first column tail defect 2 read by v_2,
    then one primitive row per D_n.  It is triangular with this diagonal.
    """
    if isinstance(max_segment, bool) or not isinstance(max_segment, int) or max_segment <= 0:
        raise ValueError("max_segment must be a positive integer")
    expected_segments = composite_indices(max_segment)
    marker_segments = tuple(segment for segment, _ in markers)
    if marker_segments != expected_segments:
        raise ValueError("markers must cover composite indices exactly in order")

    diagonal = [1]  # v_2 of the tail defect 2
    earlier: list[int] = []
    for segment, prime in markers:
        if not primitive_row_is_triangular(segment, prime, tuple(earlier)):
            raise AssertionError("primitive valuation row lost triangularity")
        diagonal.append(primitive_defect_pivot(segment, prime))
        earlier.append(segment)
    return tuple(diagonal)


def primitive_certificate_is_unimodular(
    max_segment: int,
    markers: tuple[tuple[int, int], ...],
) -> bool:
    """All primitive valuations are simple iff the triangular determinant is one."""
    diagonal = primitive_certificate_diagonal(max_segment, markers)
    return all(value == 1 for value in diagonal)
