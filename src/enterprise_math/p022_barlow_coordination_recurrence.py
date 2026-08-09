"""Periodic Barlow coordination sequences as exact quasi-polynomials.

For a period-L stacking, positive and negative prefix imbalances are affine in
the period index on every residue class.  The exact shell formula therefore
makes every residue subsequence a quadratic polynomial.  Consequently shell
counts are annihilated eventually by ``(E^L-1)^3`` and ball counts by
``(E-1)(E^L-1)^3``.

The module stores residue polynomials in integer numerator form:

    4*S_(mL+r) = c0[r] + c1[r]*m + c2*m^2.
"""

from __future__ import annotations

from .p022_barlow_stacking import StackingPattern, stacking_prefix_imbalance

ResidueQuadratic = tuple[int, int, int]  # c0,c1,c2 for 4*S


def _require_pattern(pattern: StackingPattern) -> None:
    if not isinstance(pattern, tuple) or not pattern:
        raise ValueError("stacking pattern must be a nonempty tuple")
    if any(sign not in (-1, 1) for sign in pattern):
        raise ValueError("stacking signs must be -1 or +1")


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def coordination_residue_quadratic(
    pattern: StackingPattern, residue: int
) -> ResidueQuadratic:
    """Return exact numerator coefficients for one shell residue class.

    Write ``n=mL+r`` with ``0<=r<L``. Let

        D = sum(period),
        a_r = delta_r,
        b_r = delta_-r.

    Periodicity gives

        delta_n   = mD + a_r,
        delta_-n  = -mD + b_r.

    Substituting into ``4*S_n=42n^2+8-delta_n^2-delta_-n^2`` gives

        c2 = 42L^2 - 2D^2,
        c1 = 84Lr - 2D(a_r-b_r),
        c0 = 42r^2 + 8 - a_r^2 - b_r^2.

    Radius zero uses the repository convention ``S_0=1`` rather than the
    quasi-polynomial continuation, so the returned r=0 polynomial is intended
    for ``m>=1``.
    """
    _require_pattern(pattern)
    period = len(pattern)
    if isinstance(residue, bool) or not isinstance(residue, int) or not 0 <= residue < period:
        raise ValueError("residue must lie in 0..L-1")
    drift = sum(pattern)
    upward_phase = stacking_prefix_imbalance(pattern, residue)
    downward_phase = stacking_prefix_imbalance(pattern, -residue)
    c2 = 42 * period * period - 2 * drift * drift
    c1 = 84 * period * residue - 2 * drift * (upward_phase - downward_phase)
    c0 = (
        42 * residue * residue
        + 8
        - upward_phase * upward_phase
        - downward_phase * downward_phase
    )
    return c0, c1, c2


def coordination_phase_signature(
    pattern: StackingPattern,
) -> tuple[ResidueQuadratic, ...]:
    """Finite exact state for the complete periodic shell-cardinality sequence.

    The declared period length is encoded by the tuple length.  Together with
    the radius-zero convention, these L quadratic numerators reconstruct every
    future shell cardinality.
    """
    _require_pattern(pattern)
    return tuple(
        coordination_residue_quadratic(pattern, residue)
        for residue in range(len(pattern))
    )


def shell_from_residue_quadratic(
    period: int, radius: int, quadratic: ResidueQuadratic
) -> int:
    """Evaluate one residue quadratic at an exact positive radius."""
    if isinstance(period, bool) or not isinstance(period, int) or period <= 0:
        raise ValueError("period must be positive")
    _require_natural("radius", radius)
    if radius == 0:
        return 1
    residue = radius % period
    quotient = (radius - residue) // period
    c0, c1, c2 = quadratic
    numerator = c0 + c1 * quotient + c2 * quotient * quotient
    if numerator < 0 or numerator % 4:
        raise ValueError("quadratic is incompatible with an integer shell count")
    return numerator // 4


def shell_from_phase_signature(
    radius: int, signature: tuple[ResidueQuadratic, ...]
) -> int:
    """Reconstruct any periodic shell count from its finite phase signature."""
    _require_natural("radius", radius)
    if not isinstance(signature, tuple) or not signature:
        raise ValueError("signature must be a nonempty tuple")
    if radius == 0:
        return 1
    period = len(signature)
    residue = radius % period
    return shell_from_residue_quadratic(period, radius, signature[residue])


def shell_stride_third_difference(sequence: tuple[int, ...], index: int, period: int) -> int:
    """Residual of ``(E^L-1)^3`` at one shell-sequence index."""
    if not isinstance(sequence, tuple):
        raise ValueError("sequence must be a tuple")
    if isinstance(period, bool) or not isinstance(period, int) or period <= 0:
        raise ValueError("period must be positive")
    if isinstance(index, bool) or not isinstance(index, int) or index < 3 * period:
        raise ValueError("index must be at least 3L")
    if index >= len(sequence):
        raise ValueError("sequence does not contain requested index")
    return (
        sequence[index]
        - 3 * sequence[index - period]
        + 3 * sequence[index - 2 * period]
        - sequence[index - 3 * period]
    )


def ball_stride_recurrence_residual(
    sequence: tuple[int, ...], index: int, period: int
) -> int:
    """Residual of ``(E-1)(E^L-1)^3`` for a ball-count sequence."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 3 * period + 1:
        raise ValueError("index must be at least 3L+1")
    current = shell_stride_third_difference(sequence, index, period)
    previous = shell_stride_third_difference(sequence, index - 1, period)
    return current - previous


def shell_generating_denominator(period: int) -> tuple[int, ...]:
    """Ascending coefficients of the universal denominator ``(1-z^L)^3``."""
    if isinstance(period, bool) or not isinstance(period, int) or period <= 0:
        raise ValueError("period must be positive")
    coefficients = [0] * (3 * period + 1)
    coefficients[0] = 1
    coefficients[period] = -3
    coefficients[2 * period] = 3
    coefficients[3 * period] = -1
    return tuple(coefficients)


def ball_generating_denominator(period: int) -> tuple[int, ...]:
    """Ascending coefficients of ``(1-z)(1-z^L)^3``."""
    shell = shell_generating_denominator(period)
    output = [0] * (len(shell) + 1)
    for index, value in enumerate(shell):
        output[index] += value
        output[index + 1] -= value
    return tuple(output)
