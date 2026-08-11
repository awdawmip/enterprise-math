"""Tail-Casoratian representation of the fixed P022 continuant.

The classical Franel recurrence

    (n+1)^2 F_(n+1) = (7n^2+7n+2)F_n + 8n^2 F_(n-1)

becomes the integer Euler--Wallis recurrence after the factorial-square gauge

    P_n = ((n+1)!)^2 F_(n+1),
    P_n = (7n^2+7n+2)P_(n-1) + 8n^4 P_(n-2).

Let Q_-1=0,Q_0=1 satisfy the same integer recurrence.  This is the standard
continued-fraction denominator solution; equivalently

    Q_n = ((n+1)!)^2 B^(3,1)(n+1),

where B^(3,1) is the standard second Franel solution.  Its Casoratian is

    P_(n-1) Q_n - P_n Q_(n-1) = (-8)^n (n!)^4.

These recurrence/second-solution facts are prior art.  The P022 statement is
that the fixed terminal continuant R_r from ``p022_barlow_franel_gap_continuant``
is exactly the tail transfer determinant

    R_r = -[P_(r-1)Q_(2r-3)-Q_(r-1)P_(2r-3)]
            / [2^(r+6)(r!)^4].

Using the standard Casoratian sum for the second solution gives the equivalent
exact tail sum

    R_r = -((2r-2)!)^2 F_r F_(2r-2) / [2^(r+6)(r!)^2]
          * sum_(k=r+1)^(2r-2)
              (-8)^(k-1)/(k^2 F_(k-1) F_k).

Thus the large-terminal obstruction is a genuine finite Franel tail transfer,
not an unrelated auxiliary sequence.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial

from .p022_barlow_franel_gap_continuant import eliminated_gap_transfer
from .p022_barlow_low_order_identifiability import triple_moment_factor


def franel_integer_solution(index: int) -> int:
    """P_n=((n+1)!)^2 F_(n+1), valid for n>=-1."""
    if isinstance(index, bool) or not isinstance(index, int) or index < -1:
        raise ValueError("index must be an integer at least -1")
    return factorial(index + 1) ** 2 * (
        1 if index == -1 else triple_moment_factor(index + 1)
    )


def second_integer_solution(index: int) -> int:
    """Standard Q_-1=0,Q_0=1 Euler--Wallis denominator solution."""
    if isinstance(index, bool) or not isinstance(index, int) or index < -1:
        raise ValueError("index must be an integer at least -1")
    if index == -1:
        return 0
    if index == 0:
        return 1
    previous = 0
    current = 1
    for n in range(1, index + 1):
        previous, current = (
            current,
            (7 * n * n + 7 * n + 2) * current + 8 * n**4 * previous,
        )
    return current


def integer_casoratian(index: int) -> int:
    """Return P_(n-1)Q_n-P_nQ_(n-1)."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be non-negative")
    return (
        franel_integer_solution(index - 1) * second_integer_solution(index)
        - franel_integer_solution(index) * second_integer_solution(index - 1)
    )


def integer_casoratian_closed(index: int) -> int:
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be non-negative")
    return (-8) ** index * factorial(index) ** 4


def fixed_continuant_casoratian(rank: int) -> int:
    """Recover R_r from the two standard integer Franel solutions."""
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 3:
        raise ValueError("rank must be an integer at least three")
    numerator = (
        franel_integer_solution(rank - 1) * second_integer_solution(2 * rank - 3)
        - second_integer_solution(rank - 1) * franel_integer_solution(2 * rank - 3)
    )
    denominator = 2 ** (rank + 6) * factorial(rank) ** 4
    if (-numerator) % denominator:
        raise AssertionError("tail Casoratian must have the fixed-continuant normalization")
    value = (-numerator) // denominator
    if value != eliminated_gap_transfer(rank):
        raise AssertionError("tail Casoratian disagrees with the eliminated gap continuant")
    return value


def second_solution_tail_sum(index: int) -> Fraction:
    """B^(3,1)(n)/F_n partial sum at n=index+1 in integer-solution indexing."""
    if isinstance(index, bool) or not isinstance(index, int) or index < -1:
        raise ValueError("index must be an integer at least -1")
    n = index + 1
    total = Fraction(0, 1)
    for k in range(1, n + 1):
        total += Fraction(
            (-8) ** (k - 1),
            k * k * (1 if k - 1 == 0 else triple_moment_factor(k - 1)) * triple_moment_factor(k),
        )
    return total


def fixed_continuant_tail_sum(rank: int) -> int:
    """Recover R_r from the exact Casoratian tail sum from r+1 to 2r-2."""
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 3:
        raise ValueError("rank must be an integer at least three")
    tail = Fraction(0, 1)
    for k in range(rank + 1, 2 * rank - 1):
        tail += Fraction(
            (-8) ** (k - 1),
            k * k * triple_moment_factor(k - 1) * triple_moment_factor(k),
        )
    value = -Fraction(
        factorial(2 * rank - 2) ** 2
        * triple_moment_factor(rank)
        * triple_moment_factor(2 * rank - 2),
        2 ** (rank + 6) * factorial(rank) ** 2,
    ) * tail
    if value.denominator != 1:
        raise AssertionError("the Franel tail sum must normalize to an integer")
    if value.numerator != eliminated_gap_transfer(rank):
        raise AssertionError("tail sum disagrees with the fixed continuant")
    return value.numerator


def primitive_second_solution_residue(rank: int, prime: int) -> tuple[int, int]:
    """At a first Franel zero, Q_(r-1) has an explicit q-unit residue.

    This is the finite Casoratian consequence used by the terminal route.  The
    function only assumes q|F_r and q does not divide F_(r-1); it does not
    assert primitivity beyond that local condition.
    """
    if isinstance(prime, bool) or not isinstance(prime, int) or prime <= rank:
        raise ValueError("prime must exceed rank")
    current = triple_moment_factor(rank)
    previous = triple_moment_factor(rank - 1)
    if current % prime:
        raise ValueError("prime must divide F_r")
    if previous % prime == 0:
        raise ValueError("F_(r-1) must be a q-unit")
    actual = second_integer_solution(rank - 1) % prime
    expected = (
        factorial(rank - 1) ** 2
        * pow(-8, rank - 1, prime)
        * pow(previous % prime, -1, prime)
    ) % prime
    if actual != expected or actual == 0:
        raise AssertionError("second-solution residue at the first zero changed")
    return actual, expected
