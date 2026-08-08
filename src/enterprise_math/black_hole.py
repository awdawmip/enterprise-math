"""Integer-only discrete horizon helpers for Enterprise Math P019.

This module is an executable specification for the arithmetic statements in the
P019 research note. It does not claim to implement general relativity.
"""

from __future__ import annotations

from math import comb

from .core import integer_nth_root


def _positive(name: str, value: int) -> int:
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value


def _nonnegative(name: str, value: int) -> int:
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")
    return value


def _ceil_div_positive(numerator: int, denominator: int) -> int:
    _nonnegative("numerator", numerator)
    _positive("denominator", denominator)
    return (numerator + denominator - 1) // denominator


def horizon_observation(precision: int, radius: int, horizon: int) -> int:
    """Return q_lambda(n;h) = floor(lambda * |n-h| / n).

    The quotient is represented directly by integer floor division; no hidden
    fractional state is retained.
    """
    _positive("precision", precision)
    _positive("radius", radius)
    _positive("horizon", horizon)
    return precision * abs(radius - horizon) // radius


def project_horizon_observation(
    fine_value: int, coarse_precision: int, fine_precision: int
) -> int:
    """Project a divisible fine precision observation to a coarser one."""
    _nonnegative("fine_value", fine_value)
    _positive("coarse_precision", coarse_precision)
    _positive("fine_precision", fine_precision)
    if fine_precision % coarse_precision != 0:
        raise ValueError("coarse precision must divide fine precision")
    return fine_value // (fine_precision // coarse_precision)


def horizon_zero_interval(precision: int, horizon: int) -> tuple[int, int]:
    """Return the exact positive-radius zero fiber of q_lambda for lambda >= 2."""
    _positive("precision", precision)
    _positive("horizon", horizon)
    if precision < 2:
        raise ValueError("finite zero interval requires precision >= 2")
    lower = precision * horizon // (precision + 1) + 1
    upper = (precision * horizon - 1) // (precision - 1)
    return lower, upper


def horizon_zero_width(precision: int, horizon: int) -> int:
    """Return the cardinality of the exact zero-observation horizon basin."""
    lower, upper = horizon_zero_interval(precision, horizon)
    return upper - lower + 1


def horizon_is_singleton(precision: int, horizon: int) -> bool:
    """Return whether the zero basin has resolved to the unique radius h."""
    _positive("precision", precision)
    _positive("horizon", horizon)
    return precision >= horizon + 1


def clock_state(sigma: int, radius: int, horizon: int) -> int:
    """Return the external integer lapse state at square precision sigma^2."""
    _positive("sigma", sigma)
    _positive("radius", radius)
    _positive("horizon", horizon)
    if sigma < 2:
        raise ValueError("sigma must be at least 2")
    if radius < horizon:
        raise ValueError("clock_state is defined only on or outside the horizon")
    return integer_nth_root(horizon_observation(sigma * sigma, radius, horizon), 2)


def clock_shell_interval(
    sigma: int, horizon: int, clock: int
) -> tuple[int, int | None] | None:
    """Return the exact external radius shell for one integer clock state.

    ``None`` means that the clock level is skipped entirely.
    ``(lower, None)`` denotes the unbounded outer tail at ``clock=sigma-1``.
    """
    _positive("sigma", sigma)
    _positive("horizon", horizon)
    _nonnegative("clock", clock)
    if sigma < 2:
        raise ValueError("sigma must be at least 2")
    if clock >= sigma:
        raise ValueError("external finite-radius clock state must be below sigma")

    scale = sigma * sigma
    lower = _ceil_div_positive(scale * horizon, scale - clock * clock)
    if clock == sigma - 1:
        return lower, None

    upper_denominator = scale - (clock + 1) * (clock + 1)
    upper = _ceil_div_positive(scale * horizon, upper_denominator) - 1
    if lower > upper:
        return None
    return lower, upper


def outgoing_primitive_step(precision: int, radius: int, horizon: int) -> int:
    """Return -1, 0, or +1 for the finite-precision outgoing radial step."""
    _positive("precision", precision)
    _nonnegative("radius", radius)
    _positive("horizon", horizon)
    if radius == 0:
        return 0
    magnitude = horizon_observation(precision, radius, horizon)
    if magnitude == 0:
        return 0
    return 1 if radius > horizon else -1


def outgoing_update(precision: int, radius: int, horizon: int) -> int:
    """Advance one primitive outgoing causal update."""
    return radius + outgoing_primitive_step(precision, radius, horizon)


def l1_shell_count(dimension: int, radius: int) -> int:
    """Count states at exact L1 radius in the standard-axis Z^d lattice."""
    _positive("dimension", dimension)
    _nonnegative("radius", radius)
    if radius == 0:
        return 1
    return sum(
        (2**nonzero)
        * comb(dimension, nonzero)
        * comb(radius - 1, nonzero - 1)
        for nonzero in range(1, min(dimension, radius) + 1)
    )


def l1_ball_count(dimension: int, radius: int) -> int:
    """Count states in the closed L1 ball of integer radius."""
    _positive("dimension", dimension)
    _nonnegative("radius", radius)
    return sum(l1_shell_count(dimension, shell) for shell in range(radius + 1))


def horizon_boundary_state_count(precision: int, horizon: int, dimension: int) -> int:
    """Count all L1 lattice states in the finite zero-observation radial basin."""
    lower, upper = horizon_zero_interval(precision, horizon)
    return sum(l1_shell_count(dimension, radius) for radius in range(lower, upper + 1))


def outgoing_shell_expansion(
    precision: int, radius: int, horizon: int, dimension: int
) -> int:
    """Return the exact change in intrinsic shell cardinality after one update."""
    next_radius = outgoing_update(precision, radius, horizon)
    return l1_shell_count(dimension, next_radius) - l1_shell_count(dimension, radius)


def horizon_zero_collision_count(precision: int, horizon: int, order: int) -> int:
    """Return the zero-fiber contribution C(W,k) to a local collision spectrum."""
    _nonnegative("order", order)
    width = horizon_zero_width(precision, horizon)
    if order > width:
        return 0
    return comb(width, order)
