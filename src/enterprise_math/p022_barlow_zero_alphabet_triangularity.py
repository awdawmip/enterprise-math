"""Conditional triangular classification of a Franel zero-alphabet quotient.

Fix an odd prime q and its single-digit Franel zero alphabet Z_q.  The only
columns which can fail the obvious local triangular pivot are twin-prime
center zeros.  Right-half twin zeros are already proved to be identically zero
columns.

For a left-half twin zero s, the guaranteed terminal defect D_(2s-1) has, at
zero coordinates >=s, only

    +e_s + e_(2s-1) - e_(2s-2).

Thus if neither terminal endpoint 2s-2 nor 2s-1 is itself a q-zero, this row
reduces to e_s plus zero coordinates strictly below s.

Consequently, if every left-half twin zero avoids its two terminal endpoints,
then the whole zero-alphabet matrix is triangular after ordering zero digits by
index.  Every column except the proved right-half twin zero axes is a pivot,
and the free columns are exactly those right-half twin axes.

This theorem is conditional on the terminal-collision exclusion.  The
remaining universal arithmetic frontier is therefore the existence or
impossibility of a left-half twin zero s with q dividing F_(2s-2) or F_(2s-1).
For an actual primitive source, the F_(2s-1) branch strengthens the terminal
defect; only F_(2s-2) can cancel its positive primitive depth.
"""

from __future__ import annotations

from .p022_barlow_franel_lucas_rank import franel_zero_digits
from .p022_barlow_low_order_defect_reduction import (
    _is_prime,
    composite_A_relation_exponents,
)
from .p022_barlow_right_half_defect_visibility import (
    right_half_zero_column_iff_twin,
)
from .p022_barlow_twin_defect_difference import twin_blackout_high_support


def _require_odd_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")


def _is_twin_center(index: int) -> bool:
    return _is_prime(2 * index - 1) and _is_prime(2 * index + 1)


def right_half_twin_zero_digits(prime: int) -> tuple[int, ...]:
    """Actual q-zero digits whose D_<q columns are identically zero."""
    _require_odd_prime(prime)
    midpoint = (prime - 1) // 2
    return tuple(
        digit
        for digit in franel_zero_digits(prime)
        if digit > midpoint and right_half_zero_column_iff_twin(prime, digit)
    )


def left_half_twin_zero_digits(prime: int) -> tuple[int, ...]:
    """Twin-center Franel zero digits strictly left of the midpoint."""
    _require_odd_prime(prime)
    midpoint = (prime - 1) // 2
    return tuple(
        digit
        for digit in franel_zero_digits(prime)
        if 2 < digit < midpoint and _is_twin_center(digit)
    )


def left_twin_terminal_collisions(prime: int) -> tuple[tuple[int, int], ...]:
    """Return (s,t) with left twin zero s and terminal endpoint t also zero."""
    _require_odd_prime(prime)
    zeros = set(franel_zero_digits(prime))
    output = []
    for source in left_half_twin_zero_digits(prime):
        for endpoint in (2 * source - 2, 2 * source - 1):
            if endpoint < prime and endpoint in zeros:
                output.append((source, endpoint))
    return tuple(output)


def non_twin_local_triangular_row(
    prime: int,
    zero_index: int,
) -> tuple[int, tuple[tuple[int, int], ...]]:
    """Return a local pivot row whose other zero support lies below s."""
    _require_odd_prime(prime)
    zeros = set(franel_zero_digits(prime))
    if zero_index not in zeros:
        raise ValueError("zero_index must be a Franel zero digit")
    if _is_twin_center(zero_index):
        raise ValueError("twin-center zeros use the terminal row")

    if not _is_prime(2 * zero_index - 1):
        segment = zero_index
        pivot = 1
    else:
        if _is_prime(2 * zero_index + 1):
            raise AssertionError("non-twin zero must have a local defect row")
        segment = zero_index + 1
        if segment in zeros:
            raise AssertionError("adjacent Franel zero digits are impossible")
        pivot = -1

    row: dict[int, int] = {}
    if segment in zeros:
        row[segment] = row.get(segment, 0) + 1
    for index, exponent in composite_A_relation_exponents(segment):
        if index in zeros:
            row[index] = row.get(index, 0) - exponent
            if row[index] == 0:
                del row[index]
    if row.get(zero_index) != pivot:
        raise AssertionError("local zero pivot coefficient changed")
    if any(index >= zero_index for index in row if index != zero_index):
        raise AssertionError(
            "all nonpivot zero support must lie below the pivot"
        )
    return segment, tuple(sorted(row.items()))


def left_twin_terminal_triangular_row(
    prime: int,
    zero_index: int,
) -> tuple[int, tuple[tuple[int, int], ...]]:
    """Return the terminal twin row when both terminal endpoints are q-units."""
    _require_odd_prime(prime)
    zeros = set(franel_zero_digits(prime))
    midpoint = (prime - 1) // 2
    if zero_index not in zeros or not 2 < zero_index < midpoint:
        raise ValueError("zero_index must be a strict left-half zero")
    if not _is_twin_center(zero_index):
        raise ValueError("zero_index must be a twin-prime center")
    if 2 * zero_index - 2 in zeros or 2 * zero_index - 1 in zeros:
        raise ValueError("terminal collision prevents the triangular twin row")

    segment = 2 * zero_index - 1
    twin_blackout_high_support(zero_index, segment)
    row: dict[int, int] = {}
    if segment in zeros:
        row[segment] = row.get(segment, 0) + 1
    for index, exponent in composite_A_relation_exponents(segment):
        if index in zeros:
            row[index] = row.get(index, 0) - exponent
            if row[index] == 0:
                del row[index]
    if row.get(zero_index) != 1:
        raise AssertionError(
            "terminal twin row must carry the source with coefficient +1"
        )
    if any(index >= zero_index for index in row if index != zero_index):
        raise AssertionError(
            "endpoint exclusion must leave only lower zero support"
        )
    return segment, tuple(sorted(row.items()))


def triangular_pivot_rows_if_no_terminal_collision(
    prime: int,
) -> tuple[tuple[int, int], ...]:
    """Return (zero digit,pivot row) for every nonfree zero column."""
    _require_odd_prime(prime)
    if left_twin_terminal_collisions(prime):
        raise ValueError("left-twin terminal collision remains unresolved")
    midpoint = (prime - 1) // 2
    free = set(right_half_twin_zero_digits(prime))
    pivots = []
    used_rows: set[int] = set()
    for digit in franel_zero_digits(prime):
        if digit in free:
            continue
        if digit < midpoint and _is_twin_center(digit):
            segment, _ = left_twin_terminal_triangular_row(prime, digit)
        else:
            segment, _ = non_twin_local_triangular_row(prime, digit)
        if segment in used_rows:
            raise AssertionError(
                "triangular pivot construction reused a defect row"
            )
        used_rows.add(segment)
        pivots.append((digit, segment))
    return tuple(pivots)


def triangular_free_columns_are_right_half_twins(prime: int) -> bool:
    """Conditional theorem: no terminal collisions implies the exact free set."""
    pivots = triangular_pivot_rows_if_no_terminal_collision(prime)
    zeros = franel_zero_digits(prime)
    pivot_digits = {digit for digit, _ in pivots}
    predicted_free = tuple(
        digit for digit in zeros if digit not in pivot_digits
    )
    actual_free = right_half_twin_zero_digits(prime)
    if predicted_free != actual_free:
        raise AssertionError(
            "conditional triangular free-column classification failed"
        )
    return True
