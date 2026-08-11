"""Finite zero-alphabet observability for one Franel prime.

Fix an odd prime q and let Z_q be the nonzero Franel digits j<q with
q|F_j.  Restrict every composite-defect valuation row

    v_q(D_n)=z_n-sum_j alpha_(n,j) z_j

to the coordinates in Z_q.  This gives a finite integer matrix M_q.  If a
q-adic row is invisible on every composite defect n<q, its positive depth
vector z|Z_q lies in ker(M_q).

There is one transparent geometric source of linear kernel: if s is a zero
digit above the midpoint and both 2s-1 and 2s+1 are prime, then the standard
basis vector at s is invisible through n<q.  The two relevant new A-generators
lie above q and, before the horizon q, their valuation columns differ only at
s.  We call these upper-half twin modes.

For every other zero digit the canonical candidate row is chosen without
search:

* D_s when 2s-1 is composite;
* D_(s+1) when 2s-1 is prime and 2s+1 is composite;
* D_(2s-1) for a lower-half twin center.

`canonical_unit_peeling_certificate` repeatedly uses only those rows and
requires a unit singleton pivot after already-certified coordinates are
removed.  Success is an exact finite theorem for that prime: all non-free
coordinates are killed, the kernel dimension equals the number of upper-half
twin modes, and in particular the first Franel zero digit is observable unless
it is the exceptional small q=5,r=2 geometry.

This module deliberately separates the exact per-prime certificate from the
open uniform theorem that the peeling succeeds for every odd prime.  The
Franel p-Lucas/reflection facts are prior art; the zero-alphabet defect
restriction and canonical peeling interpretation are P022-local.
"""

from __future__ import annotations

from .p022_barlow_franel_lucas_rank import franel_zero_digits
from .p022_barlow_low_order_defect_reduction import (
    _is_prime,
    composite_A_relation_exponents,
)
from .p022_barlow_primitive_successor_capture import is_twin_prime_deferral_center

IntegerRow = tuple[int, ...]
LabeledRow = tuple[int, IntegerRow]
Pivot = tuple[int, int, int]  # zero digit, defect segment, coefficient


def _require_odd_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")


def zero_alphabet(prime: int) -> tuple[int, ...]:
    _require_odd_prime(prime)
    return franel_zero_digits(prime)


def zero_restricted_defect_rows(prime: int) -> tuple[tuple[int, ...], tuple[LabeledRow, ...]]:
    """Return (Z_q, labeled rows of M_q) for composite defects 2<=n<q."""
    zeros = zero_alphabet(prime)
    index = {digit: column for column, digit in enumerate(zeros)}
    rows: list[LabeledRow] = []
    for segment in range(2, prime):
        if _is_prime(2 * segment - 1):
            continue
        row = [0] * len(zeros)
        if segment in index:
            row[index[segment]] += 1
        for digit, exponent in composite_A_relation_exponents(segment):
            column = index.get(digit)
            if column is not None:
                row[column] -= exponent
        if any(row):
            rows.append((segment, tuple(row)))
    return zeros, tuple(rows)


def upper_half_twin_zero_digits(prime: int) -> tuple[int, ...]:
    """Zero digits whose singleton coordinate is invisible before the q horizon."""
    zeros = zero_alphabet(prime)
    midpoint = (prime - 1) // 2
    return tuple(
        digit
        for digit in zeros
        if digit > midpoint and is_twin_prime_deferral_center(digit)
    )


def upper_twin_columns_are_zero(prime: int) -> bool:
    """Certify every declared upper-half twin column of M_q is identically zero."""
    zeros, rows = zero_restricted_defect_rows(prime)
    column = {digit: index for index, digit in enumerate(zeros)}
    for digit in upper_half_twin_zero_digits(prime):
        j = column[digit]
        if any(row[j] != 0 for _, row in rows):
            raise AssertionError("upper-half twin mode must be invisible before q")
    return True


def canonical_capture_segment(prime: int, digit: int) -> int | None:
    """The direct/successor/re-entry row assigned to one zero digit.

    `None` is reserved for an upper-half twin mode or the tiny q=5,r=2
    exception, where the first twin re-entry lies on a prime boundary.
    """
    _require_odd_prime(prime)
    if digit not in zero_alphabet(prime):
        raise ValueError("digit must belong to the Franel zero alphabet")
    if not _is_prime(2 * digit - 1):
        return digit
    if not _is_prime(2 * digit + 1):
        return digit + 1
    reentry = 2 * digit - 1
    if reentry >= prime or _is_prime(2 * reentry - 1):
        return None
    return reentry


def canonical_unit_peeling_certificate(prime: int) -> tuple[tuple[int, ...], tuple[Pivot, ...]]:
    """Peel all non-free zero coordinates by their canonical unit rows.

    Returns `(free_upper_twins, pivots)`.  Failure means the current uniform
    proof frontier has found a genuine unresolved finite coupling for this
    prime; the function never silently falls back to arbitrary Gaussian
    elimination.
    """
    zeros, labeled_rows = zero_restricted_defect_rows(prime)
    upper_twin_columns_are_zero(prime)
    free = set(upper_half_twin_zero_digits(prime))
    remaining = set(zeros) - free
    column = {digit: index for index, digit in enumerate(zeros)}
    row_by_segment = {segment: row for segment, row in labeled_rows}
    pivots: list[Pivot] = []

    while remaining:
        found: Pivot | None = None
        for digit in sorted(remaining):
            segment = canonical_capture_segment(prime, digit)
            if segment is None:
                continue
            row = row_by_segment.get(segment)
            if row is None:
                continue
            live = [
                other
                for other in remaining
                if row[column[other]] != 0
            ]
            if live != [digit]:
                continue
            coefficient = row[column[digit]]
            if coefficient not in (-1, 1):
                raise AssertionError("canonical peeling pivot must be a unit")
            found = (digit, segment, coefficient)
            break
        if found is None:
            raise AssertionError(
                "canonical zero-alphabet peeling stalled; uniform theorem frontier reached"
            )
        pivots.append(found)
        remaining.remove(found[0])

    return tuple(sorted(free)), tuple(pivots)


def certified_zero_kernel_dimension(prime: int) -> int:
    """Exact kernel dimension after a successful canonical unit peeling."""
    free, pivots = canonical_unit_peeling_certificate(prime)
    zeros = zero_alphabet(prime)
    if len(free) + len(pivots) != len(zeros):
        raise AssertionError("free modes plus unit pivots must partition Z_q")
    return len(free)


def primitive_source_is_observable(prime: int) -> bool:
    """Certify the first zero digit is killed by the finite defect system."""
    zeros = zero_alphabet(prime)
    if not zeros:
        raise ValueError("prime has no Franel zero digit")
    source = zeros[0]
    free, pivots = canonical_unit_peeling_certificate(prime)
    if source in free:
        raise AssertionError("the first zero digit cannot be an upper-half free mode")
    return any(digit == source for digit, _, _ in pivots)
