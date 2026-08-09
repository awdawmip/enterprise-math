"""Exact shell-total geodesic formulas and periodic Barlow growth invariants.

The finite formula uses only the prefix imbalance at each target layer.  For a
periodic stacking, the imbalance differs from its linear drift by a bounded
periodic term, which yields an exact exponential-growth constant depending only
on the absolute drift density.

The asymptotic constant is recorded without requiring floating-point state.  If
period length is L and period drift is D, the growth constant lambda is the
positive real root greater than two of

    (lambda - 2)^(2L) = 2^(L + |D|).
"""

from __future__ import annotations

from math import comb

from .p022_barlow_precision import barlow_prefix_normal_form
from .p022_barlow_stacking import StackingPattern, stacking_prefix_imbalance


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_pattern(pattern: StackingPattern) -> None:
    if not isinstance(pattern, tuple) or not pattern:
        raise ValueError("stacking pattern must be a nonempty tuple")
    if any(sign not in (-1, 1) for sign in pattern):
        raise ValueError("stacking signs must be -1 or +1")


def barlow_layer_shell_total_geodesic_paths(
    radius: int, target_layer: int, pattern: StackingPattern
) -> int:
    """Exact shortest-path total on one target layer of one graph shell.

    Let ``q=|k|``, ``d=|delta_k|`` and ``c=(q-d)/2``.  The vertical polynomial
    has normal form ``(A+3)^c B_sign^d``.

    If ``q=radius``, no in-layer step is possible in a shortest path; all
    ``3^q`` monotone vertical words end on the radius shell.

    If ``q<radius``, put ``t=radius-q>0``.  The outer triangular boundary of a
    non-negative Laurent polynomial ``P A^t`` can be counted by its six exposed
    faces minus their six corner overlaps.  ``A`` has face mass 2 and corner
    mass 1.  ``A+3`` has the same exposed masses.  ``B_+`` and ``B_-`` each
    have three face masses 1 and three face masses 2, while every corner mass
    is 1.  Product faces multiply, hence

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
    """Return the reduced conceptual pair ``(|D|, L)`` without real division."""
    _require_pattern(pattern)
    return abs(period_drift(pattern)), len(pattern)


def growth_constant_integer_equation(pattern: StackingPattern) -> tuple[int, int]:
    """Return exponents encoding the exact algebraic growth constant.

    The output ``(power, rhs)`` means that the exponential growth constant
    lambda is the positive real root greater than two of

        (lambda - 2)^power = rhs.

    For period length L and drift D,

        power = 2L,
        rhs = 2^(L+|D|).

    This keeps the canonical stored descriptor entirely integral.
    """
    drift, period = period_absolute_drift_data(pattern)
    return 2 * period, 2 ** (period + drift)


def drift_deviation_bound(pattern: StackingPattern) -> int:
    """Exact finite bound C with ||delta_k|-mu|k|| <= C in cross-multiplied form.

    To avoid rational arithmetic, return the maximum value of

        | L*|delta_r| - |D|*r |

    across one upward period prefix ``0<=r<L`` and one downward period phase.
    For arbitrary k, periodic decomposition shows the same bound controls the
    numerator after subtracting the linear drift ``|D|*|k|/L``.

    The bound is mainly an executable certificate used by the asymptotic proof.
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
