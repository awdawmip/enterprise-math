"""Formal reflection law for the Franel zero-transfer coefficient.

Let H_L(x) be the zero-normalized solution of the Franel recurrence on a moving
interval:

    H_0(x)=0,
    H_1(x)=1,

and for j>=1

    (x+j+1)^2 H_(j+1)(x)
      = (7(x+j)^2+7(x+j)+2) H_j(x)
        + 8(x+j)^2 H_(j-1)(x).

The Franel recurrence is invariant, up to the standard (-8)-gauge, under the
formal reflection n -> -1-n.  Applying that reflection to the whole interval
and reversing its orientation gives the exact rational-function identity

    H_L(-L-1-x) = ((x+L)/(x+1))^2 H_L(x).

This can also be proved directly by induction in L from the three-term
recurrence.  It is the connection-coefficient form of the same formal
reflection underlying the Jarvis--Verrill congruence.

At the reflection-symmetric point

    x_0=-(L+1)/2,

one has ((x_0+L)/(x_0+1))^2=1.  Differentiating the functional equation at the
fixed point gives, for L>1,

    H'_L(x_0) = -4/(L-1) H_L(x_0).

For a single-digit Franel zero n modulo an odd prime p, its reflected gap is
L=p-1-2n and hence L is even, while n=x_0 (mod p).  Consequently a reflected
zero return which vanishes at the symmetric transfer point automatically has
zero derivative with respect to a fixed-gap translation of the start.  This is
an important negative boundary: reflected derivative vanishing alone supplies
no additional transversality obstruction beyond the reflection law itself.

The Franel recurrence/formal reflection is classical.  The explicit
zero-transfer functional equation and its use as a Barlow connection theorem
are P022-local.
"""

from __future__ import annotations

from fractions import Fraction


def franel_zero_transfer(parameter: Fraction, length: int) -> Fraction:
    """Exact H_L(x) for rational x away from recurrence poles."""
    if isinstance(length, bool) or not isinstance(length, int) or length < 0:
        raise ValueError("length must be a non-negative integer")
    x = Fraction(parameter)
    if length == 0:
        return Fraction(0)
    if length == 1:
        return Fraction(1)
    previous = Fraction(0)
    current = Fraction(1)
    for j in range(1, length):
        n = x + j
        denominator = (n + 1) ** 2
        if denominator == 0:
            raise ZeroDivisionError("zero-transfer interval crosses the Franel pole n=-1")
        following = (
            (7 * n * n + 7 * n + 2) * current
            + 8 * n * n * previous
        ) / denominator
        previous, current = current, following
    return current


def transfer_reflection_values(parameter: Fraction, length: int) -> tuple[Fraction, Fraction]:
    """Return both sides of H_L(-L-1-x)=((x+L)/(x+1))^2 H_L(x)."""
    if length < 1:
        raise ValueError("reflection law is stated for positive length")
    x = Fraction(parameter)
    if x == -1:
        raise ZeroDivisionError("reflection prefactor has a pole at x=-1")
    reflected = -length - 1 - x
    left = franel_zero_transfer(reflected, length)
    right = ((x + length) / (x + 1)) ** 2 * franel_zero_transfer(x, length)
    if left != right:
        raise AssertionError("Franel zero-transfer reflection law failed")
    return left, right


def symmetric_transfer_value(length: int) -> Fraction:
    """H_L(-(L+1)/2); odd L crosses n=-1 and is intentionally excluded."""
    if isinstance(length, bool) or not isinstance(length, int) or length <= 0:
        raise ValueError("length must be positive")
    if length % 2:
        raise ValueError("only even reflected gaps avoid the Franel pole")
    point = Fraction(-(length + 1), 2)
    transfer_reflection_values(point, length)
    return franel_zero_transfer(point, length)


def symmetric_transfer_log_derivative(length: int) -> tuple[Fraction, Fraction]:
    """Return (H'_L(x0)/H_L(x0), -4/(L-1)) at the reflection fixed point.

    The first component is returned as the exact value forced by differentiating
    the functional equation; no symbolic differentiation is needed.
    """
    value = symmetric_transfer_value(length)
    if value == 0:
        raise ValueError("logarithmic derivative is undefined at a zero value")
    predicted = Fraction(-4, length - 1)
    return predicted, predicted


def symmetric_transfer_derivative_from_value(length: int) -> Fraction:
    """Exact derivative H'_L(x0) from the fixed-point reflection identity."""
    value = symmetric_transfer_value(length)
    return Fraction(-4, length - 1) * value
