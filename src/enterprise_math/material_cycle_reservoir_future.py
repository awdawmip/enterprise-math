"""One-step future separation of body-identical cycle histories by contact reservoirs.

``material_cycle_history_precision_bridge`` constructs a balanced four-contact
cycle whose minimum-total response relation at denominator ``s`` is

    j(t) = (s+t, s-t, s+t, s-t),      -s <= t <= s.

All ``2s+1`` responses have the same body after-state, final contact scores,
total impulse and kinetic energy.  This file gives a deliberately minimal finite
material-history pressure test showing that those witnesses can nevertheless be
future-relevant.

Give each contact an independent finite impulse-capacity reservoir with initial
numerator ``2s``.  A delivered impulse subtracts componentwise from the
reservoir.  After history ``j(t)`` the remaining capacity is

    u(t) = 2s*1 - j(t)
         = (s-t, s+t, s-t, s+t)
         = j(-t).

Now externally reload the bodies to the same balanced closing state.  The next
minimum nonclosing response still needs total numerator ``4s``.  But the total
remaining capacity is also exactly ``4s``.  Hence any feasible next response
must saturate every reservoir coordinate and is unique:

    next(t) = u(t) = j(-t).

The map ``t -> next(t)`` is injective.  Therefore every hidden first-cycle
contact history is distinguished by one further identical reload, despite being
invisible to body-level and aggregate first-cycle observables.

This reservoir law is an explicit toy material-memory operation, not a claim
that real damage equals cumulative impulse.  Its role is to prove a state-safety
boundary: a body-only quotient is not future-safe for operation languages that
retain contact-local capacity/history.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_cycle_history_precision_bridge import (
    balanced_four_cycle_minimum_relation,
)


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def balanced_cycle_reservoir_after_history(
    denominator: int,
    history: tuple[int, ...] | list[int],
) -> tuple[int, int, int, int]:
    """Subtract one declared minimum history from the initial ``2s`` reservoirs."""
    _positive("denominator", denominator)
    vector = tuple(history)
    relation = balanced_four_cycle_minimum_relation(denominator)
    if vector not in relation:
        raise ValueError("history must belong to the balanced-cycle minimum relation")
    capacity = 2 * denominator
    remaining = tuple(capacity - value for value in vector)
    if any(value < 0 for value in remaining):
        raise AssertionError("balanced cycle history exceeded declared initial reservoir")
    return remaining  # type: ignore[return-value]


@dataclass(frozen=True)
class BalancedCycleReservoirFutureReport:
    denominator: int
    first_history: tuple[int, int, int, int]
    remaining_capacity: tuple[int, int, int, int]
    next_unique_response: tuple[int, int, int, int]
    next_shift: int
    first_shift: int
    total_remaining_capacity: int
    future_response_is_unique: bool


def balanced_cycle_history_shift(
    denominator: int,
    history: tuple[int, ...] | list[int],
) -> int:
    """Recover t from j(t)=(s+t,s-t,s+t,s-t)."""
    _positive("denominator", denominator)
    vector = tuple(history)
    if vector not in balanced_four_cycle_minimum_relation(denominator):
        raise ValueError("history must belong to the balanced-cycle minimum relation")
    return vector[0] - denominator


def balanced_cycle_reservoir_future_report(
    denominator: int,
    first_history: tuple[int, ...] | list[int],
) -> BalancedCycleReservoirFutureReport:
    """Return the unique second response after the toy contact-reservoir update."""
    _positive("denominator", denominator)
    vector = tuple(first_history)
    if len(vector) != 4:
        raise ValueError("balanced four-cycle history must have four contact entries")
    relation = balanced_four_cycle_minimum_relation(denominator)
    if vector not in relation:
        raise ValueError("first_history must belong to the minimum relation")
    remaining = balanced_cycle_reservoir_after_history(denominator, vector)
    total_remaining = sum(remaining)
    required_total = 4 * denominator
    if total_remaining != required_total:
        raise AssertionError("balanced reservoir law lost exact second-cycle total capacity")
    if remaining not in relation:
        raise AssertionError("remaining reservoir failed the opposite-cycle minimum relation")
    first_shift = balanced_cycle_history_shift(denominator, vector)
    next_shift = balanced_cycle_history_shift(denominator, remaining)
    if next_shift != -first_shift:
        raise AssertionError("balanced reservoir future failed exact shift reversal")

    # Since the minimum required total equals the total available capacity, any
    # feasible second response must saturate every coordinate.  The response is
    # therefore uniquely equal to ``remaining``.
    return BalancedCycleReservoirFutureReport(
        denominator=denominator,
        first_history=vector,  # type: ignore[arg-type]
        remaining_capacity=remaining,
        next_unique_response=remaining,
        next_shift=next_shift,
        first_shift=first_shift,
        total_remaining_capacity=total_remaining,
        future_response_is_unique=True,
    )


def all_balanced_cycle_histories_future_distinguishable(
    denominator: int,
) -> bool:
    """Verify injectivity of first hidden history -> unique next reload response."""
    _positive("denominator", denominator)
    relation = balanced_four_cycle_minimum_relation(denominator)
    futures = {
        balanced_cycle_reservoir_future_report(
            denominator,
            history,
        ).next_unique_response
        for history in relation
    }
    if len(futures) != len(relation):
        raise AssertionError("contact reservoir future failed to distinguish hidden histories")
    return True
