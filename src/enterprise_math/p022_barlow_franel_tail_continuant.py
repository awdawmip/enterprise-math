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

The same integer recurrence is the Euler--Wallis recurrence of the Franel
continued fraction.  If p_n/q_n denotes its convergents, with

    p_n = (n+1)!^2 F_(n+1),

then the general continuant determinant specializes to

    p_(2r-3) q_(r-1) - p_(r-1) q_(2r-3)
        = 2^(r+6) (r!)^4 R_r.

If an odd prime q>4r-3 divides F_r, the source denominator has the explicit
unit residue

    q_(r-1) = (r-1)!^2 (-8)^(r-1) / F_(r-1)        (mod q).

Consequently the terminal Franel value itself is the following unit multiple
of R_r:

    F_(2r-2) = (-1)^(r-1) 2^(9-2r) r^4
               ((r-1)!/(2r-2)!)^2 F_(r-1) R_r     (mod q).

Thus R_r is not merely a zero detector: it is a normalized residue coordinate
for the terminal return.  The published continued-fraction identification is
prior art; the exact tail specialization and P022 escape interpretation are the
use recorded here.
"""

from __future__ import annotations

from math import factorial

from .p022_barlow_franel_gap_continuant import eliminated_gap_transfer
from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import triple_moment_factor


def _require_rank(rank: int) -> None:
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 4:
        raise ValueError("rank must be an integer at least four")


def franel_integer_recurrence_a(index: int) -> int:
    """Diagonal coefficient 7n^2+7n+2 of the integer Franel recurrence."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be a non-negative integer")
    return 7 * index * index + 7 * index + 2


def franel_integer_recurrence_b(index: int) -> int:
    """Backward coefficient 8n^4 of the integer Franel recurrence."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be a non-negative integer")
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
    """Certify the factorial cancellation behind the 4^(r-3) factor."""
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


def euler_wallis_convergent(index: int) -> tuple[int, int]:
    """Return (p_n,q_n) for the Franel generalized continued fraction."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be a non-negative integer")

    p_minus_one = 1
    q_minus_one = 0
    p_current = franel_integer_recurrence_a(0)
    q_current = 1
    if index == 0:
        return p_current, q_current

    p_previous = p_minus_one
    q_previous = q_minus_one
    for n in range(1, index + 1):
        a_n = franel_integer_recurrence_a(n)
        b_n = franel_integer_recurrence_b(n)
        p_previous, p_current = (
            p_current,
            a_n * p_current + b_n * p_previous,
        )
        q_previous, q_current = (
            q_current,
            a_n * q_current + b_n * q_previous,
        )
    return p_current, q_current


def euler_wallis_franel_numerator_identity(index: int) -> bool:
    """Certify p_n=(n+1)!^2 F_(n+1) from the same integer recurrence."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be a non-negative integer")
    p_n, _ = euler_wallis_convergent(index)
    expected = factorial(index + 1) ** 2 * triple_moment_factor(index + 1)
    if p_n != expected:
        raise AssertionError("Euler-Wallis numerator is not the scaled Franel term")
    return True


def fixed_gap_euler_wallis_determinant(rank: int) -> tuple[int, int]:
    """Certify the exact cross-determinant formula for R_r."""
    _require_rank(rank)
    p_left, q_left = euler_wallis_convergent(rank - 1)
    p_right, q_right = euler_wallis_convergent(2 * rank - 3)
    determinant = p_right * q_left - p_left * q_right
    predicted = (
        2 ** (rank + 6)
        * factorial(rank) ** 4
        * eliminated_gap_transfer(rank)
    )
    if determinant != predicted:
        raise AssertionError("Euler-Wallis cross determinant disagrees with R_r")
    return determinant, predicted


def source_denominator_residue(rank: int, prime: int) -> int:
    """q_(r-1) modulo a large prime divisor of F_r, in explicit unit form."""
    _require_rank(rank)
    if not _is_prime(prime) or prime <= 4 * rank - 3:
        raise ValueError("prime must exceed the large-terminal threshold")
    source = triple_moment_factor(rank)
    previous = triple_moment_factor(rank - 1)
    if source % prime:
        raise ValueError("prime must divide F_r")
    if previous % prime == 0:
        raise AssertionError("adjacent Franel zeros are impossible in this range")

    _, q_left = euler_wallis_convergent(rank - 1)
    predicted = (
        factorial(rank - 1) ** 2
        * pow(-8, rank - 1, prime)
        * pow(previous % prime, -1, prime)
    ) % prime
    if q_left % prime != predicted:
        raise AssertionError("source Euler-Wallis denominator residue changed")
    if predicted == 0:
        raise AssertionError("source denominator residue must be a unit")
    return predicted


def terminal_franel_residue_from_gap(rank: int, prime: int) -> tuple[int, int]:
    """Return equal residues of F_(2r-2) and its explicit unit multiple of R_r."""
    _require_rank(rank)
    if not _is_prime(prime) or prime <= 4 * rank - 3:
        raise ValueError("prime must exceed the large-terminal threshold")
    if triple_moment_factor(rank) % prime:
        raise ValueError("prime must divide F_r")
    source_denominator_residue(rank, prime)
    fixed_gap_euler_wallis_determinant(rank)

    terminal = triple_moment_factor(2 * rank - 2) % prime
    numerator_factorial = factorial(rank - 1) % prime
    denominator_factorial = factorial(2 * rank - 2) % prime
    unit = (-1 if (rank - 1) % 2 else 1) % prime
    unit = unit * pow(2, 9 - 2 * rank, prime) % prime
    unit = unit * pow(rank, 4, prime) % prime
    unit = unit * numerator_factorial**2 % prime
    unit = unit * pow(denominator_factorial**2 % prime, -1, prime) % prime
    unit = unit * (triple_moment_factor(rank - 1) % prime) % prime
    predicted = unit * (eliminated_gap_transfer(rank) % prime) % prime
    if unit == 0:
        raise AssertionError("terminal normalization must be a unit")
    if terminal != predicted:
        raise AssertionError("terminal Franel residue and normalized R_r disagree")
    return terminal, predicted


def primitive_large_gap_is_projective_return(rank: int, prime: int) -> bool:
    """For q>4r-3 and q|F_r, certify R_r=0 iff the later numerator is zero."""
    terminal, predicted = terminal_franel_residue_from_gap(rank, prime)
    if terminal != predicted:
        raise AssertionError("terminal residue normalization failed")
    fixed_zero = eliminated_gap_transfer(rank) % prime == 0
    later_zero = terminal == 0
    if fixed_zero != later_zero:
        raise AssertionError("R_r must detect the projective return to [0:1]")
    return fixed_zero
