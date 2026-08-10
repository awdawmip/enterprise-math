"""Exact integer reconstruction of finite-TTL queue-age state from total traces.

For a D-bucket whole-contact queue under pure aging/no arrivals/no consumption,
let

    T_k = total queue after k aging steps.

Then for ``0<=k<D-1``

    T_k - T_(k+1) = q_(D-1-k),

and

    T_(D-1) = q_0.

Hence the complete age histogram is recovered from the D totals
``T_0,...,T_(D-1)`` using subtraction only:

    q_0     = T_(D-1),
    q_1     = T_(D-2)-T_(D-1),
    ...,
    q_(D-1) = T_0-T_1.

More generally, a horizon-h trace recovers exactly the P023 predictive key from
the sibling module:

    (T_h, T_(h-1)-T_h, ..., T_0-T_1),

for ``h<=D-1``.  The first coordinate is the still-aggregated younger pool and
the differences are the individually exposed oldest buckets.

Thus the TTL observability transform is integer-exact and denominator-free.  It
contrasts with graph critical-group decompositions, where topology can force a
nontrivial rational denominator.  Both are future-visible hidden-state effects,
but they have different integer-lattice structures.
"""

from __future__ import annotations

from typing import Sequence

from .material_contact_queue_age_precision import (
    ContactWholeQueueAgeState,
    age_total_future_key,
    pure_aging_total_trace,
)


Vector = tuple[int, ...]


def _integer_trace(values: Sequence[int]) -> Vector:
    trace = tuple(values)
    if not trace:
        raise ValueError("total trace must be nonempty")
    for value in trace:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("total trace entries must be integers")
        if value < 0:
            raise ValueError("total trace entries must be nonnegative")
    if any(right > left for left, right in zip(trace, trace[1:], strict=False)):
        raise ValueError("pure TTL total trace must be nonincreasing")
    return trace


def age_future_key_from_total_trace(
    total_trace: Sequence[int],
) -> Vector:
    """Invert a pure-aging total trace to the exact finite-horizon age key."""
    trace = _integer_trace(total_trace)
    return (
        trace[-1],
        *(
            trace[index] - trace[index + 1]
            for index in range(len(trace) - 2, -1, -1)
        ),
    )


def age_histogram_from_full_total_trace(
    total_trace: Sequence[int],
    retention_depth: int,
) -> ContactWholeQueueAgeState:
    """Recover the full D-bucket age histogram from horizon D-1 total observations."""
    if isinstance(retention_depth, bool) or not isinstance(retention_depth, int):
        raise TypeError("retention_depth must be an integer")
    if retention_depth <= 0:
        raise ValueError("retention_depth must be positive")
    trace = _integer_trace(total_trace)
    if len(trace) != retention_depth:
        raise ValueError(
            "full reconstruction requires exactly retention_depth total observations"
        )
    state = ContactWholeQueueAgeState(
        age_future_key_from_total_trace(trace)
    )
    if state.retention_depth != retention_depth:
        raise AssertionError("reconstructed age histogram has wrong depth")
    if pure_aging_total_trace(state, retention_depth - 1) != trace:
        raise AssertionError("reconstructed histogram failed forward total trace")
    return state


def verify_age_trace_key_inversion(
    state: ContactWholeQueueAgeState,
    horizon: int,
) -> bool:
    """Check trace inversion equals the sibling closed predictive key."""
    if not isinstance(state, ContactWholeQueueAgeState):
        raise TypeError("state must be ContactWholeQueueAgeState")
    if isinstance(horizon, bool) or not isinstance(horizon, int):
        raise TypeError("horizon must be an integer")
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    effective = min(horizon, state.retention_depth - 1)
    trace = pure_aging_total_trace(state, effective)
    inverted = age_future_key_from_total_trace(trace)
    expected = age_total_future_key(state, effective)
    if inverted != expected:
        raise AssertionError("TTL total-trace inversion disagreed with age future key")
    return True
