"""Conditional echelon theorem for the Franel zero-alphabet defect quotient.

Let q be an odd prime, m=(q-1)//2, and Z_q the nonzero Franel zero digits.
Use recurrence nonadjacency, so adjacent members of Z_q never occur.

Every left-half zero s<=m has a canonical pivot unless s is a twin-prime
center.  In the twin case the first re-entry row D_(2s-1) has, after lower
columns, exactly

    +z_s - z_(2s-2) + z_(2s-1).

Therefore it is again a pivot provided neither terminal index 2s-2 nor 2s-1
belongs to Z_q.  Once all left-half columns are pivoted, every right-half
non-twin zero has a direct or successor pivot.  The proved right-half
visibility theorem says the remaining right-half twin columns are identically
zero.

Hence the single arithmetic obstruction to the clean echelon classification is

    s in Z_q, s<=m, 2s-1 and 2s+1 prime,
    and (2s-2 in Z_q or 2s-1 in Z_q).

If no such obstruction occurs then the exact free columns are precisely the
right-half twin zero digits.  This module exposes that reduction; it does not
claim the terminal-exclusion premise for every prime.
"""

from __future__ import annotations

from .p022_barlow_franel_lucas_rank import franel_zero_digits
from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_primitive_successor_capture import is_twin_prime_deferral_center
from .p022_barlow_zero_alphabet_quotient import (
    primitive_source_is_in_defect_rowspace,
    right_half_twin_zero_digits,
    zero_alphabet_free_digits,
)


def left_half_twin_terminal_conflicts(
    prime: int,
) -> tuple[tuple[int, tuple[int, ...]], ...]:
    """Return left-half twin zeros whose first terminal pair contains a zero."""
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")
    midpoint = (prime - 1) // 2
    zero_set = set(franel_zero_digits(prime))
    conflicts = []
    for digit in sorted(zero_set):
        if digit > midpoint or digit < 2:
            continue
        if not is_twin_prime_deferral_center(digit):
            continue
        hits = tuple(
            target
            for target in (2 * digit - 2, 2 * digit - 1)
            if target in zero_set
        )
        if hits:
            conflicts.append((digit, hits))
    return tuple(conflicts)


def left_half_twin_terminal_exclusion_holds(prime: int) -> bool:
    """Finite verifier for the sole remaining arithmetic echelon premise."""
    if left_half_twin_terminal_conflicts(prime):
        raise AssertionError("left-half twin Franel zero has a terminal zero hit")
    return True


def conditional_zero_alphabet_echelon_theorem(prime: int) -> bool:
    """Under terminal exclusion, free columns are exactly right-half twins."""
    left_half_twin_terminal_exclusion_holds(prime)
    actual = zero_alphabet_free_digits(prime)
    expected = right_half_twin_zero_digits(prime)
    if actual != expected:
        raise AssertionError("conditional zero-alphabet echelon classification failed")
    # A nonempty zero alphabet always starts on the left half by reflection.
    # Thus the rank-of-apparition coordinate must be a pivot under the premise.
    if actual or expected:
        pass
    try:
        source_pivot = primitive_source_is_in_defect_rowspace(prime)
    except ValueError:
        return True  # empty zero alphabet
    if not source_pivot:
        raise AssertionError("terminal exclusion must annihilate the primitive source column")
    return True
