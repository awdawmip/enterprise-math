"""Separate lifted momentum direction from the coarse whole-count observable.

For one inward-oriented retained momentum state write

    Pi = D*p + eta,        |eta| < D,

with ``D>0``.  Starting from positive lifted momentum ``Pi0`` and accumulating a
non-negative outward impulse numerator ``I`` gives ``Pi=Pi0-I``.

The physical/lifted direction changes as soon as Pi changes sign:

    I < Pi0  -> lifted inward,
    I = Pi0  -> lifted zero,
    I > Pi0  -> lifted outward.

The whole momentum count is a coarser signed-toward-zero observation.  It stays
zero throughout

    -D < Pi < D,

so it can hide both a small inward lift and a small outward lift.  In particular

    Pi0 < I < Pi0+D

is already lifted-outward while whole momentum is still zero.  Calling this a
physical stall is valid only for a downstream policy that consumes the whole
momentum quotient and discards/hides its retained detail.  A lifted-momentum drift
may respond immediately.

This module turns the earlier normalized ``stall band`` into an explicit
observable-alias band.  It is an E001 specialization of future-observable
precision, not a generic quotient theorem.
"""

from __future__ import annotations

from dataclasses import dataclass

LIFTED_INWARD = "LIFTED_INWARD"
LIFTED_ZERO = "LIFTED_ZERO"
LIFTED_OUTWARD = "LIFTED_OUTWARD"
WHOLE_INWARD = "WHOLE_INWARD"
WHOLE_ZERO = "WHOLE_ZERO"
WHOLE_OUTWARD = "WHOLE_OUTWARD"
HIDDEN_INWARD = "HIDDEN_INWARD"
EXACT_STOP = "EXACT_STOP"
HIDDEN_OUTWARD = "HIDDEN_OUTWARD"
VISIBLE_INWARD = "VISIBLE_INWARD"
VISIBLE_OUTWARD = "VISIBLE_OUTWARD"


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _toward_zero(value: int, divisor: int) -> int:
    return value // divisor if value >= 0 else -((-value) // divisor)


@dataclass(frozen=True)
class MomentumVisibilityReport:
    initial_lifted_inward_momentum: int
    cumulative_outward_impulse: int
    momentum_detail_divisor: int
    lifted_momentum: int
    whole_inward_momentum_count: int
    lifted_direction: str
    whole_direction: str
    visibility_phase: str
    lifted_outward: bool
    whole_outward_visible: bool


def momentum_visibility_report(
    initial_lifted_inward_momentum: int,
    cumulative_outward_impulse: int,
    momentum_detail_divisor: int,
) -> MomentumVisibilityReport:
    """Classify true lifted direction versus whole-count direction after impulse."""
    _positive("initial_lifted_inward_momentum", initial_lifted_inward_momentum)
    _nonnegative("cumulative_outward_impulse", cumulative_outward_impulse)
    _positive("momentum_detail_divisor", momentum_detail_divisor)
    pi = initial_lifted_inward_momentum - cumulative_outward_impulse
    whole = _toward_zero(pi, momentum_detail_divisor)
    lifted_direction = (
        LIFTED_INWARD if pi > 0 else LIFTED_OUTWARD if pi < 0 else LIFTED_ZERO
    )
    whole_direction = (
        WHOLE_INWARD if whole > 0 else WHOLE_OUTWARD if whole < 0 else WHOLE_ZERO
    )
    if whole > 0:
        phase = VISIBLE_INWARD
    elif whole < 0:
        phase = VISIBLE_OUTWARD
    elif pi > 0:
        phase = HIDDEN_INWARD
    elif pi < 0:
        phase = HIDDEN_OUTWARD
    else:
        phase = EXACT_STOP
    return MomentumVisibilityReport(
        initial_lifted_inward_momentum=initial_lifted_inward_momentum,
        cumulative_outward_impulse=cumulative_outward_impulse,
        momentum_detail_divisor=momentum_detail_divisor,
        lifted_momentum=pi,
        whole_inward_momentum_count=whole,
        lifted_direction=lifted_direction,
        whole_direction=whole_direction,
        visibility_phase=phase,
        lifted_outward=pi < 0,
        whole_outward_visible=whole < 0,
    )


@dataclass(frozen=True)
class MomentumVisibilityThresholds:
    initial_lifted_inward_momentum: int
    momentum_detail_divisor: int
    first_whole_zero_impulse: int
    exact_lifted_stop_impulse: int
    first_lifted_outward_impulse: int
    first_whole_outward_impulse: int
    hidden_outward_impulse_count: int


def momentum_visibility_thresholds(
    initial_lifted_inward_momentum: int,
    momentum_detail_divisor: int,
) -> MomentumVisibilityThresholds:
    """Return exact impulse thresholds for whole/lifted directional visibility."""
    _positive("initial_lifted_inward_momentum", initial_lifted_inward_momentum)
    _positive("momentum_detail_divisor", momentum_detail_divisor)
    pi0 = initial_lifted_inward_momentum
    d = momentum_detail_divisor
    first_zero = max(0, pi0 - d + 1)
    stop = pi0
    lifted_out = pi0 + 1
    whole_out = pi0 + d
    # I = pi0+1,...,pi0+d-1 are lifted-outward but whole-zero.
    hidden_count = max(0, d - 1)
    return MomentumVisibilityThresholds(
        initial_lifted_inward_momentum=pi0,
        momentum_detail_divisor=d,
        first_whole_zero_impulse=first_zero,
        exact_lifted_stop_impulse=stop,
        first_lifted_outward_impulse=lifted_out,
        first_whole_outward_impulse=whole_out,
        hidden_outward_impulse_count=hidden_count,
    )
