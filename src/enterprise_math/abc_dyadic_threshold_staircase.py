"""Multi-threshold staircase normal form for monotone dyadic P025 pressure.

For ordered thresholds T_1<...<T_s and a dyadic pressure orbit
rho_0<=...<=rho_h, each threshold row is an upward-closed suffix.  Its first
activation depths

    j_1 <= j_2 <= ... <= j_s

form a weakly increasing staircase in the ordered state set
{0,...,h,infinity}.  The full s x (h+1) Boolean activation matrix is recovered
exactly from this crossing vector.

The compatible matrix state count is the combinations-with-repetition number

    C(h+s+1, s),

instead of 2^(s(h+1)) unconstrained Boolean matrices.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb

from .abc_signed_exponent_transport import dyadic_difference_pressure_tower


@dataclass(frozen=True)
class DyadicThresholdStaircase:
    q: int
    p: int
    base_exponent: int
    horizon_steps: int
    thresholds: tuple[Fraction, ...]
    exponents: tuple[int, ...]
    pressures: tuple[Fraction, ...]
    crossing_depths: tuple[int | None, ...]
    activation_matrix: tuple[tuple[bool, ...], ...]
    compatible_matrix_state_count: int
    unconstrained_boolean_matrix_state_count: int
    monotone_crossings_verified: bool
    reconstruction_verified: bool


def _require_thresholds(thresholds: tuple[Fraction, ...]) -> None:
    if not thresholds:
        raise ValueError("thresholds must be nonempty")
    if any(not isinstance(value, Fraction) or value <= 0 for value in thresholds):
        raise ValueError("thresholds must be positive Fractions")
    if any(right <= left for left, right in zip(thresholds, thresholds[1:])):
        raise ValueError("thresholds must be strictly increasing")


def _depth_key(depth: int | None, horizon_steps: int) -> int:
    return horizon_steps + 1 if depth is None else depth


def threshold_crossing_depths(
    pressures: tuple[Fraction, ...], thresholds: tuple[Fraction, ...]
) -> tuple[int | None, ...]:
    """Return first depths at which each strictly increasing threshold is reached."""
    _require_thresholds(thresholds)
    if not pressures:
        raise ValueError("pressures must be nonempty")
    if any(right < left for left, right in zip(pressures, pressures[1:])):
        raise ValueError("pressures must be nondecreasing")
    return tuple(
        next((depth for depth, pressure in enumerate(pressures) if pressure >= threshold), None)
        for threshold in thresholds
    )


def activation_matrix_from_crossings(
    horizon_steps: int,
    crossing_depths: tuple[int | None, ...],
) -> tuple[tuple[bool, ...], ...]:
    """Reconstruct threshold rows from weakly increasing first-crossing depths."""
    if isinstance(horizon_steps, bool) or not isinstance(horizon_steps, int) or horizon_steps < 0:
        raise ValueError("horizon_steps must be a non-negative integer")
    if not crossing_depths:
        raise ValueError("crossing_depths must be nonempty")
    keys: list[int] = []
    for depth in crossing_depths:
        if depth is None:
            keys.append(horizon_steps + 1)
        elif isinstance(depth, bool) or not isinstance(depth, int) or not 0 <= depth <= horizon_steps:
            raise ValueError("each crossing depth must lie in 0..h or be None")
        else:
            keys.append(depth)
    if any(right < left for left, right in zip(keys, keys[1:])):
        raise ValueError("crossing depths must be weakly increasing")
    return tuple(
        tuple(False if depth is None else column >= depth for column in range(horizon_steps + 1))
        for depth in crossing_depths
    )


def compatible_staircase_state_count(horizon_steps: int, threshold_count: int) -> int:
    """Return number of weakly increasing s-tuples from h+2 depth states."""
    if isinstance(horizon_steps, bool) or not isinstance(horizon_steps, int) or horizon_steps < 0:
        raise ValueError("horizon_steps must be a non-negative integer")
    if isinstance(threshold_count, bool) or not isinstance(threshold_count, int) or threshold_count < 1:
        raise ValueError("threshold_count must be a positive integer")
    # Weakly increasing s-tuples from N=h+2 ordered values: C(N+s-1,s).
    return comb(horizon_steps + threshold_count + 1, threshold_count)


def dyadic_threshold_staircase(
    q: int,
    p: int,
    base_exponent: int,
    horizon_steps: int,
    thresholds: tuple[Fraction, ...],
) -> DyadicThresholdStaircase:
    """Compile the exact multi-threshold activation matrix into one staircase."""
    _require_thresholds(thresholds)
    tower = dyadic_difference_pressure_tower(q, p, base_exponent, horizon_steps)
    crossings = threshold_crossing_depths(tower.pressures, thresholds)
    keys = tuple(_depth_key(depth, horizon_steps) for depth in crossings)
    if any(right < left for left, right in zip(keys, keys[1:])):
        raise AssertionError("higher threshold activated earlier than a lower threshold")

    matrix = activation_matrix_from_crossings(horizon_steps, crossings)
    direct = tuple(
        tuple(pressure >= threshold for pressure in tower.pressures)
        for threshold in thresholds
    )
    if matrix != direct:
        raise AssertionError("crossing staircase failed to reconstruct activation matrix")

    s = len(thresholds)
    return DyadicThresholdStaircase(
        q=q,
        p=p,
        base_exponent=base_exponent,
        horizon_steps=horizon_steps,
        thresholds=thresholds,
        exponents=tower.exponents,
        pressures=tower.pressures,
        crossing_depths=crossings,
        activation_matrix=matrix,
        compatible_matrix_state_count=compatible_staircase_state_count(horizon_steps, s),
        unconstrained_boolean_matrix_state_count=1 << (s * (horizon_steps + 1)),
        monotone_crossings_verified=True,
        reconstruction_verified=True,
    )
