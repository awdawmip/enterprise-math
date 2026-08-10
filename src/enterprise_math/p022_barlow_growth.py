"""Exact shell-total geodesic formulas and periodic Barlow growth invariants.

The finite formula uses only the prefix imbalance at each target layer. For a
periodic stacking, the imbalance differs from its linear drift by a bounded
periodic term, which yields an exact exponential-growth constant depending only
on the absolute drift density.

Periodic stacking also makes the whole shell-total sequence eventually
C-finite. If period length is L and absolute period drift is |D|, one universal
integer characteristic polynomial is

    (x-1)(x-2)(x-3)
    (x^L-A+)(x^L-A-)
    ((x-2)^L-A+)((x-2)^L-A-),

where A+ = 2^((L+|D|)/2) and A- = 2^((L-|D|)/2).

The polynomial need not be minimal: repeated/cancelled factors depend on the
specific period phase. It is a uniform annihilator for every stacking with the
same period length and absolute drift.
"""

from __future__ import annotations

from math import comb

from .p022_barlow_precision import barlow_prefix_normal_form
from .p022_barlow_stacking import StackingPattern, stacking_prefix_imbalance

Polynomial = tuple[int, ...]  # ascending coefficients: p[power]


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_pattern(pattern: StackingPattern) -> None:
    if not isinstance(pattern, tuple) or not pattern:
        raise ValueError("stacking pattern must be a nonempty tuple")
    if any(sign not in (-1, 1) for sign in pattern):
        raise ValueError("stacking signs must be -1 or +1")


def _poly_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    output = [0] * (len(left) + len(right) - 1)
    for left_power, left_value in enumerate(left):
        for right_power, right_value in enumerate(right):
            output[left_power + right_power] += left_value * right_value
    return tuple(output)


def _x_minus(constant: int) -> Polynomial:
    return (-constant, 1)


def _x_power_minus(power: int, constant: int) -> Polynomial:
    _require_natural("power", power)
    if power == 0:
        raise ValueError("power must be positive")
    coefficients = [-constant] + [0] * (power - 1) + [1]
    return tuple(coefficients)


def _shifted_x_power_minus(power: int, shift: int, constant: int) -> Polynomial:
    """Ascending coefficients of ``(x-shift)^power-constant``."""
    _require_natural("power", power)
    if power == 0:
        raise ValueError("power must be positive")
    coefficients = [comb(power, exponent) * ((-shift) ** (power - exponent)) for exponent in range(power + 1)]
    coefficients[0] -= constant
    return tuple(coefficients)


def barlow_layer_shell_total_geodesic_paths(
    radius: int, target_layer: int, pattern: StackingPattern
) -> int:
    """Exact shortest-path total on one target layer of one graph shell.

    Let ``q=|k|``, ``d=|delta_k|`` and ``c=(q-d)/2``. The vertical polynomial
    has normal form ``(A+3)^c B_sign^d``.

    If ``q=radius``, no in-layer step is possible in a shortest path; all
    ``3^q`` monotone vertical words end on the radius shell.

    If ``q<radius``, put ``t=radius-q>0``. The outer triangular boundary of a
    non-negative Laurent polynomial ``P A^t`` can be counted by its six exposed
    faces minus their six corner overlaps. ``A`` has face mass 2 and corner
    mass 1. ``A+3`` has the same exposed masses. ``B_+`` and ``B_-`` each
    have three face masses 1 and three face masses 2, while every corner mass
    is 1. Product faces multiply, hence

        boundary_mass = 3*2^(c+t)*(1+2^d) - 6.

    Finally ``C(radius,t)=C(radius,q)`` interleaves the t in-layer steps with
    the q monotone vertical steps.
    """
    _require_natural("radius", radius)
    _require_pattern(pattern)
    if isinstance(target_layer, bool) or not isinstance(target_layer, int):
        raise ValueError("target_layer must be an integer")
    vertical = abs(target_layer)
    if vertical > radius:
        return 0
    if radius == 0:
        return 1 if target_layer == 0 else 0
    if vertical == radius:
        return 3 ** vertical

    paired, _, drift_count = barlow_prefix_normal_form(pattern, target_layer)
    in_layer = radius - vertical
    boundary_mass = 3 * (2 ** (paired + in_layer)) * (1 + 2 ** drift_count) - 6
    return comb(radius, in_layer) * boundary_mass


def barlow_shell_total_geodesic_paths_closed(
    radius: int, pattern: StackingPattern
) -> int:
    """Exact whole-shell shortest-path total from prefix imbalances only."""
    _require_natural("radius", radius)
    _require_pattern(pattern)
    if radius == 0:
        return 1
    return sum(
        barlow_layer_shell_total_geodesic_paths(radius, layer, pattern)
        for layer in range(-radius, radius + 1)
    )


def period_drift(pattern: StackingPattern) -> int:
    """Signed interface imbalance accumulated over one upward period."""
    _require_pattern(pattern)
    return sum(pattern)


def period_absolute_drift_data(pattern: StackingPattern) -> tuple[int, int]:
    """Return the exact conceptual pair ``(|D|, L)`` without real division."""
    _require_pattern(pattern)
    return abs(period_drift(pattern)), len(pattern)


def period_exponential_weights(pattern: StackingPattern) -> tuple[int, int]:
    """Return ``(A_minus, A_plus)`` used by the universal recurrence.

    Because a ±1 period has D congruent to L mod 2, both exponents below are
    integers:

        A_plus  = 2^((L+|D|)/2),
        A_minus = 2^((L-|D|)/2).
    """
    drift, period = period_absolute_drift_data(pattern)
    if (period + drift) % 2 or (period - drift) % 2:
        raise AssertionError("period length and ±1 drift must have matching parity")
    smaller = 2 ** ((period - drift) // 2)
    larger = 2 ** ((period + drift) // 2)
    return smaller, larger


def growth_constant_integer_equation(pattern: StackingPattern) -> tuple[int, int]:
    """Return exponents encoding the exact algebraic growth constant.

    The output ``(power, rhs)`` means that the exponential growth constant
    lambda is the positive real root greater than two of

        (lambda - 2)^power = rhs.

    For period length L and drift D,

        power = 2L,
        rhs = 2^(L+|D|).
    """
    drift, period = period_absolute_drift_data(pattern)
    return 2 * period, 2 ** (period + drift)


def universal_growth_characteristic_polynomial(
    pattern: StackingPattern,
) -> Polynomial:
    """Uniform eventual recurrence annihilator for one periodic-drift class.

    Coefficients are returned in ascending powers. The monic polynomial is

      Q(x)=(x-1)(x-2)(x-3)
           (x^L-A+)(x^L-A-)
           ((x-2)^L-A+)((x-2)^L-A-).

    ``A+`` and ``A-`` are integer powers of two from
    :func:`period_exponential_weights`.  The same Q works for every period word
    with the same ``(L,|D|)``. It may have repeated or unnecessary factors.

    The exact shell-total sequence satisfies ``Q(E)T=0`` for every index
    strictly larger than ``deg(Q)=4L+3``.  The one-step warm-up reflects the
    special radius-zero convention ``T(0)=1``.
    """
    _require_pattern(pattern)
    period = len(pattern)
    a_minus, a_plus = period_exponential_weights(pattern)
    polynomial: Polynomial = (1,)
    for factor in (
        _x_minus(1),
        _x_minus(2),
        _x_minus(3),
        _x_power_minus(period, a_plus),
        _x_power_minus(period, a_minus),
        _shifted_x_power_minus(period, 2, a_plus),
        _shifted_x_power_minus(period, 2, a_minus),
    ):
        polynomial = _poly_multiply(polynomial, factor)
    return polynomial


def universal_growth_generating_denominator(
    pattern: StackingPattern,
) -> Polynomial:
    """Reciprocal integer denominator associated with the universal recurrence.

    If Q is monic of degree d, return ``z^d Q(1/z)`` in ascending powers. Thus
    a formal ordinary generating function for the eventually recurrent shell
    sequence has denominator dividing this polynomial after cancellation.
    """
    characteristic = universal_growth_characteristic_polynomial(pattern)
    return tuple(reversed(characteristic))


def recurrence_residual(
    sequence: tuple[int, ...], index: int, characteristic: Polynomial
) -> int:
    """Return ``Q(E) sequence`` at one index for an ascending monic Q.

    For ``Q(x)=q_0+...+q_d x^d``, this evaluates

        q_d a_index + q_(d-1) a_(index-1) + ... + q_0 a_(index-d).
    """
    if not isinstance(sequence, tuple):
        raise ValueError("sequence must be a tuple")
    if not characteristic or characteristic[-1] != 1:
        raise ValueError("characteristic polynomial must be nonempty and monic")
    degree = len(characteristic) - 1
    if isinstance(index, bool) or not isinstance(index, int) or index < degree:
        raise ValueError("index must be at least the characteristic degree")
    if index >= len(sequence):
        raise ValueError("sequence does not contain requested index")
    return sum(
        characteristic[degree - lag] * sequence[index - lag]
        for lag in range(degree + 1)
    )


def drift_deviation_bound(pattern: StackingPattern) -> int:
    """Finite cross-multiplied bound for periodic absolute imbalance error.

    Return a C such that

        |L*|delta_k| - |D|*|k|| <= C

    for every target layer k. Periodic decomposition reduces the check to one
    upward and one downward phase of the finite period.
    """
    _require_pattern(pattern)
    period = len(pattern)
    drift = abs(period_drift(pattern))
    deviations = [0]
    for layer in range(1, period):
        imbalance = abs(stacking_prefix_imbalance(pattern, layer))
        deviations.append(abs(period * imbalance - drift * layer))
        downward = abs(stacking_prefix_imbalance(pattern, -layer))
        deviations.append(abs(period * downward - drift * layer))
    return max(deviations)
