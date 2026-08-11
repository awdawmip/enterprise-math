"""A two-integral Lagrange invariant for the Franel formal derivative.

Let F_n be the Franel numbers and F'_n Straub's formal derivative of the
Apéry-like recurrence.  Put

    W_n = F_n F'_(n+1) - F_(n+1) F'_n.

Combining the classical Franel recurrence with its differentiated recurrence
gives the exact first-order identity

    (n+1)^3 W_n
      = -8 n^2 (n+1) W_(n-1)
        + F_n ((7n+3)F_n + 16n F_(n-1)).

The apparent division by n+1 in the corresponding integrating-factor form is
actually integral.  Write

    B_n=(7n+3)F_n+16nF_(n-1).

Reducing the Franel recurrence modulo n+1 gives

    2(F_n+4F_(n-1)) = 0  (mod n+1),

while B_n=-4(F_n+4F_(n-1)) (mod n+1).  If n+1 is odd this directly gives
(n+1)|B_n.  If n+1 is even it gives (n+1)/2|B_n, and the missing factor two is
supplied by the elementary fact that F_n is even for every n>=1.  Hence

    T_n := F_n B_n/(n+1)

is always an integer.

Therefore

    Y_n := (n+1)^2 (-8)^(-n) W_n

satisfies

    Y_n-Y_(n-1) = (-8)^(-n) T_n,

so Y_n belongs to Z[1/2]: all odd harmonic denominators in F'_n cancel from
this local Lagrange coordinate.

For a prime p>n with p|F_n, recurrence nonadjacency makes F_(n+1) a p-unit and
therefore

    F'_n=0 (mod p)  iff  W_n=0 (mod p)  iff  Y_n=0 (mod p).

Thus the remaining single-digit multiple-root/transversality problem can be
studied through the 2-integral sequence Y rather than through harmonic sums.
The Franel recurrence and formal derivative are prior art; the Wronskian
reduction, integer increment, and Barlow transversality packaging are P022-local.
"""

from __future__ import annotations

from fractions import Fraction

from .p022_barlow_franel_gessel_lucas_copy import franel_formal_derivative
from .p022_barlow_low_order_identifiability import triple_moment_factor


def franel_is_even(index: int) -> bool:
    """Certify the elementary parity fact F_n is even for every n>=1."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 1:
        raise ValueError("index must be a positive integer")
    value = triple_moment_factor(index)
    if value % 2:
        raise AssertionError("Franel parity theorem failed")
    return True


def derivative_wronskian(index: int) -> Fraction:
    """W_n=F_n F'_(n+1)-F_(n+1)F'_n."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be non-negative")
    current = 1 if index == 0 else triple_moment_factor(index)
    following = triple_moment_factor(index + 1)
    return (
        current * franel_formal_derivative(index + 1)
        - following * franel_formal_derivative(index)
    )


def wronskian_forcing_bracket(index: int) -> int:
    """B_n=(7n+3)F_n+16nF_(n-1), n>=1."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 1:
        raise ValueError("index must be positive")
    current = triple_moment_factor(index)
    previous = 1 if index == 1 else triple_moment_factor(index - 1)
    return (7 * index + 3) * current + 16 * index * previous


def wronskian_integer_increment(index: int) -> int:
    """T_n=F_n B_n/(n+1), certified integral by recurrence/parity."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 1:
        raise ValueError("index must be positive")
    current = triple_moment_factor(index)
    bracket = wronskian_forcing_bracket(index)
    numerator = current * bracket
    if numerator % (index + 1):
        raise AssertionError("Franel Wronskian forcing term must be divisible by n+1")
    return numerator // (index + 1)


def wronskian_recurrence_residual(index: int) -> Fraction:
    """Residual of the exact first-order Wronskian recurrence."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 1:
        raise ValueError("index must be positive")
    current_w = derivative_wronskian(index)
    previous_w = derivative_wronskian(index - 1)
    current_f = triple_moment_factor(index)
    return (
        (index + 1) ** 3 * current_w
        + 8 * index * index * (index + 1) * previous_w
        - current_f * wronskian_forcing_bracket(index)
    )


def two_integral_lagrange_coordinate(index: int) -> Fraction:
    """Y_n=(n+1)^2(-8)^(-n)W_n."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be non-negative")
    return Fraction((index + 1) ** 2, (-8) ** index) * derivative_wronskian(index)


def lagrange_increment_identity(index: int) -> tuple[Fraction, Fraction]:
    """Certify Y_n-Y_(n-1)=(-8)^(-n)T_n for n>=1."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 1:
        raise ValueError("index must be positive")
    left = two_integral_lagrange_coordinate(index) - two_integral_lagrange_coordinate(index - 1)
    right = Fraction(wronskian_integer_increment(index), (-8) ** index)
    if left != right:
        raise AssertionError("two-integral Lagrange increment identity failed")
    return left, right


def lagrange_coordinate_has_power_two_denominator(index: int) -> bool:
    """Certify Y_n belongs to Z[1/2] for one exact index."""
    value = two_integral_lagrange_coordinate(index)
    denominator = value.denominator
    if denominator & (denominator - 1):
        raise AssertionError("Lagrange coordinate denominator must be a power of two")
    return True
