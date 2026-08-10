"""Identify the fixed large-terminal obstruction with a Franel tail continuant.

Put

    U_n = (n!)^2 F_n.

The Franel recurrence becomes the integer recurrence

    U_(n+1) = (7 n^2 + 7 n + 2) U_n + 8 n^4 U_(n-1).

For r>=4 let T^(r) be the normalized tail solution of the same recurrence,

    T_r = 0,  T_(r+1) = 1.

The fixed companion-gap integer R_r introduced by the large-terminal reduction
is exactly

    R_r = (-1)^(r+1) 4^(r-3) T_(2r-2).

Thus, away from the prime 2, R_r has exactly the same prime divisors as a
standard tail continuant of the integer-normalized Franel recurrence.  This
places the remaining primitive-gcd question inside the same continuant system
as the Ramanujan-machine Franel continued fraction rather than in a new
auxiliary sequence.
"""

from __future__ import annotations

from .p022_barlow_franel_gap_continuant import eliminated_gap_transfer


def _require_rank(rank: int) -> None:
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 4:
        raise ValueError("rank must be an integer at least four")


def franel_integer_recurrence_a(index: int) -> int:
    """Diagonal coefficient 7n^2+7n+2 of the integer Franel recurrence."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 1:
        raise ValueError("index must be a positive integer")
    return 7 * index * index + 7 * index + 2


def franel_integer_recurrence_b(index: int) -> int:
    """Backward coefficient 8n^4 of the integer Franel recurrence."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 1:
        raise ValueError("index must be a positive integer")
    return 8 * index**4


def franel_tail_continuant(rank: int) -> int:
    """Return T_(2r-2) for T_r=0,T_(r+1)=1."""
    _require_rank(rank)
    previous = 0
    current = 1
    for index in range(rank + 1, 2 * rank - 2):
        previous, current = (
            current,
            franel_integer_recurrence_a(index) * current
            + franel_integer_recurrence_b(index) * previous,
        )
    return current


def formal_reflection_scale(rank: int) -> int:
    """4^(r-2)(2r-3)!!/(r(r+1)), the square-root connection scale."""
    _require_rank(rank)
    odd_double_factorial = 1
    for value in range(1, 2 * rank - 2, 2):
        odd_double_factorial *= value
    numerator = 4 ** (rank - 2) * odd_double_factorial
    denominator = rank * (rank + 1)
    if numerator % denominator:
        raise AssertionError("formal reflection scale must be integral")
    return numerator // denominator


def fixed_gap_equals_tail_continuant(rank: int) -> tuple[int, int]:
    """Return the two equal forms of R_r and certify the exact identity."""
    _require_rank(rank)
    fixed = eliminated_gap_transfer(rank)
    tail = franel_tail_continuant(rank)
    predicted = (-1) ** (rank + 1) * 4 ** (rank - 3) * tail
    if fixed != predicted:
        raise AssertionError("fixed gap and Franel tail continuant disagree")
    return fixed, predicted


def reflection_scale_ratio_identity(rank: int) -> bool:
    """Certify the factorial cancellation behind the 4^(r-3) factor.

    If K_r is the coefficient of y_(r+1) in y_(2r-2) for the normalized
    Franel recurrence with y_r=0,y_(r+1)=1, then

        K_r = ((r+1)!/(2r-2)!)^2 T_(2r-2).

    The formal midpoint scale S_r satisfies

        S_r^2 ((r+1)!/(2r-2)!)^2 = 4^(r-3).
    """
    _require_rank(rank)
    scale = formal_reflection_scale(rank)
    left_numerator = scale * scale
    for value in range(2, rank + 2):
        left_numerator *= value * value
    left_denominator = 1
    for value in range(2, 2 * rank - 1):
        left_denominator *= value * value
    expected = 4 ** (rank - 3)
    if left_numerator != expected * left_denominator:
        raise AssertionError("reflection/factorial scales failed to cancel")
    return True
