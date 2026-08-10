"""Right-half visibility in the canonical central-binomial defect basis.

Fix an odd prime q and m=(q-1)//2.  For m<s<q, the prime generator attached
to the central-binomial coordinate A_s is p=2s-1>q-2.  In a composite defect
D_n with n<q, this high coordinate cannot be introduced by the recursive
integer basis of n, and it cannot be introduced by the integer basis of
2n-1: a composite integer below 2q-1 has no prime factor strictly above q.
Thus A_s can occur only in the adjacent term A_(n-1), namely at n=s+1.
The defect numerator itself contributes z_s only at n=s.

Consequently the complete D_n (n<q) column of a right-half coordinate s has
at most two entries:

    +1 at D_s       when 2s-1 is composite,
    -1 at D_(s+1)   when 2s+1 is composite.

It is an identically zero column iff both 2s-1 and 2s+1 are prime, i.e. iff s
is a twin-prime center.  This explains the right-half singleton kernel axes
seen in the finite Franel zero-alphabet matrices without appealing to Franel
arithmetic.

A related localization holds for every composite m+2<=n<q: all relation
indices above the midpoint are exhausted by the adjacent index n-1.  Hence
on the high half the defect is the path difference z_n-z_(n-1); every other
term lies at an index <=m.
"""

from __future__ import annotations

from .p022_barlow_low_order_defect_reduction import (
    _is_prime,
    composite_A_relation_exponents,
)


def _require_odd_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")


def _require_right_half_index(prime: int, index: int) -> int:
    _require_odd_prime(prime)
    if isinstance(index, bool) or not isinstance(index, int):
        raise ValueError("index must be an integer")
    midpoint = (prime - 1) // 2
    if not midpoint < index < prime:
        raise ValueError("index must lie strictly in the right half below q")
    return midpoint


def right_half_relation_occurrences(prime: int, index: int) -> tuple[tuple[int, int], ...]:
    """Rows n<q whose canonical A-relation contains A_index.

    The only possible relation occurrence is the adjacent row n=index+1.
    """
    _require_right_half_index(prime, index)
    occurrences = []
    for segment in range(2, prime):
        if _is_prime(2 * segment - 1):
            continue
        exponent = dict(composite_A_relation_exponents(segment)).get(index, 0)
        if exponent:
            occurrences.append((segment, exponent))
    expected = ()
    successor = index + 1
    if successor < prime and not _is_prime(2 * successor - 1):
        expected = ((successor, 1),)
    result = tuple(occurrences)
    if result != expected:
        raise AssertionError("right-half relation support escaped the adjacent row")
    return result


def right_half_defect_column(prime: int, index: int) -> tuple[tuple[int, int], ...]:
    """Full generic depth-column coefficients across all D_n with n<q."""
    _require_right_half_index(prime, index)
    column = []
    for segment in range(2, prime):
        if _is_prime(2 * segment - 1):
            continue
        coefficient = 1 if segment == index else 0
        coefficient -= dict(composite_A_relation_exponents(segment)).get(index, 0)
        if coefficient:
            column.append((segment, coefficient))

    expected = []
    if not _is_prime(2 * index - 1):
        expected.append((index, 1))
    if index + 1 < prime and not _is_prime(2 * index + 1):
        expected.append((index + 1, -1))
    result = tuple(column)
    if result != tuple(expected):
        raise AssertionError("right-half defect column escaped direct/adjacent support")
    return result


def right_half_zero_column_iff_twin(prime: int, index: int) -> bool:
    """Certify: the D_<q column is zero iff 2s-1 and 2s+1 are prime."""
    _require_right_half_index(prime, index)
    column_is_zero = not right_half_defect_column(prime, index)
    twin = _is_prime(2 * index - 1) and _is_prime(2 * index + 1)
    if column_is_zero != twin:
        raise AssertionError("right-half zero-column/twin classification failed")
    return column_is_zero


def above_midpoint_relation_support(
    prime: int, segment: int
) -> tuple[tuple[int, int], ...]:
    """High support of a composite row m+2<=n<q is exactly (n-1,+1)."""
    _require_odd_prime(prime)
    midpoint = (prime - 1) // 2
    if (
        isinstance(segment, bool)
        or not isinstance(segment, int)
        or not midpoint + 2 <= segment < prime
    ):
        raise ValueError("segment must satisfy m+2<=n<q")
    if _is_prime(2 * segment - 1):
        raise ValueError("segment must have composite odd boundary")
    high = tuple(
        (index, exponent)
        for index, exponent in composite_A_relation_exponents(segment)
        if index > midpoint
    )
    expected = ((segment - 1, 1),)
    if high != expected:
        raise AssertionError("above-midpoint relation support escaped the path edge")
    return high
