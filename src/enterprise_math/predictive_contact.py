"""Predictive Boolean-contact precision for the E001 gap-collapse candidate.

The active E001 engineering candidate observes contact at scale ``d`` by
``gap < d``.  This module does not redefine collision response.  It asks a
narrow P023/E002 question: under a declared separating gap action ``g -> g+a``,
how much of the currently collapsed contact fiber must be retained to predict
Boolean contact for a finite or arbitrary future horizon?

For one positive separating increment, the exact predictive coordinate is the
first contact-exit sample, capped by the declared horizon.  The generic finite
predictive-quotient compiler is used as an independent oracle in tests.
"""

from __future__ import annotations


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _require_positive(name: str, value: int) -> None:
    _require_int(name, value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def _require_nonnegative(name: str, value: int) -> None:
    _require_int(name, value)
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")


def collapse_contact(gap: int, precision: int) -> bool:
    """E001 active coarse-contact candidate ``gap < precision``."""
    _require_nonnegative("gap", gap)
    _require_positive("precision", precision)
    return gap < precision


def contact_exit_time(gap: int, precision: int, separating_step: int) -> int:
    """First positive sample at which a currently-contact gap exits contact."""
    _require_nonnegative("gap", gap)
    _require_positive("precision", precision)
    _require_positive("separating_step", separating_step)
    if not collapse_contact(gap, precision):
        raise ValueError("gap must currently belong to the contact fiber")
    remaining = precision - gap
    return (remaining + separating_step - 1) // separating_step


def contact_horizon_rank(
    gap: int,
    precision: int,
    separating_step: int,
    horizon: int,
) -> int:
    """Coarsest within-contact repair for Boolean contact through one horizon.

    Exit samples later than the declared horizon are merged into the terminal
    bucket ``horizon + 1``.
    """
    _require_nonnegative("horizon", horizon)
    exit_time = contact_exit_time(gap, precision, separating_step)
    return min(exit_time, horizon + 1)


def contact_horizon_class_count(
    precision: int,
    separating_step: int,
    horizon: int,
) -> int:
    """Exact number ``min(h+1, ceil(d/a))`` of predictive contact classes."""
    _require_positive("precision", precision)
    _require_positive("separating_step", separating_step)
    _require_nonnegative("horizon", horizon)
    stable = (precision + separating_step - 1) // separating_step
    return min(horizon + 1, stable)


def stable_contact_class_count(precision: int, separating_step: int) -> int:
    """Arbitrary-future Boolean-contact classes inside the coarse contact fiber."""
    _require_positive("precision", precision)
    _require_positive("separating_step", separating_step)
    return (precision + separating_step - 1) // separating_step


def contact_future_signature(
    gap: int,
    precision: int,
    separating_step: int,
    horizon: int,
) -> tuple[bool, ...]:
    """Direct Boolean contact observations from sample 0 through ``horizon``."""
    _require_nonnegative("gap", gap)
    _require_positive("precision", precision)
    _require_positive("separating_step", separating_step)
    _require_nonnegative("horizon", horizon)
    return tuple(
        collapse_contact(gap + sample * separating_step, precision)
        for sample in range(horizon + 1)
    )


def stable_contact_state_savings(precision: int, separating_step: int) -> int:
    """Fine contact-gap states avoided by the arbitrary-future Boolean quotient."""
    return precision - stable_contact_class_count(precision, separating_step)
