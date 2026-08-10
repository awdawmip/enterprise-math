"""Exact collision-spectrum filtration for the countdown precision-genesis model.

The parent countdown model has states ``0,...,N`` and horizon key

    q_h(x) = min(x,h).

For ``0<=h<=N`` its future-equivalence fiber shape is exactly

    (N-h+1, 1, ..., 1),

with ``h`` singleton fibers.  Hence every collision statistic of order ``k>=2``
comes entirely from the one unresolved tail fiber:

    A_k(h) = C(N-h+1, k).

In particular pair ambiguity is

    A_2(h) = C(N-h+1, 2),

and one additional future step removes exactly

    A_2(h)-A_2(h+1) = N-h

indistinguishable state pairs.  These gains telescope:

    sum_{h=0}^{N-1} (N-h) = C(N+1,2),

exactly the entire initial pair ambiguity of the one-class current observation.

So future horizon is an exact precision filtration: each step increases class
count by one but removes a decreasing linear amount of pair ambiguity.  This is
a P023/FQ-006 specialization of the existing P011 collision/irreversibility
spectrum language, not a new mother invariant.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb

from .partial_action_precision_genesis import (
    countdown_predictive_class_count,
)


def _inputs(maximum_state: int, horizon: int) -> tuple[int, int]:
    for name, value in (("maximum_state", maximum_state), ("horizon", horizon)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
    if maximum_state < 1:
        raise ValueError("maximum_state must be at least one")
    if horizon < 0:
        raise ValueError("horizon must be non-negative")
    return maximum_state, min(horizon, maximum_state)


def countdown_future_fiber_shape(
    maximum_state: int,
    horizon: int,
) -> tuple[int, ...]:
    """Sorted fiber-size shape of ``x -> min(x,h)``."""
    maximum_state, capped = _inputs(maximum_state, horizon)
    tail = maximum_state - capped + 1
    return (tail,) + (1,) * capped


def countdown_collision_ambiguity(
    maximum_state: int,
    horizon: int,
    order: int,
) -> int:
    """Number of unordered order-k state subsets inside one future fiber."""
    maximum_state, capped = _inputs(maximum_state, horizon)
    if isinstance(order, bool) or not isinstance(order, int):
        raise TypeError("order must be an integer")
    if order < 2:
        raise ValueError("collision order must be at least two")
    tail = maximum_state - capped + 1
    return comb(tail, order) if tail >= order else 0


def countdown_pair_ambiguity(maximum_state: int, horizon: int) -> int:
    return countdown_collision_ambiguity(maximum_state, horizon, 2)


def countdown_pair_precision_gain(maximum_state: int, horizon: int) -> int:
    """Pair ambiguity removed by extending horizon from h to h+1."""
    maximum_state, capped = _inputs(maximum_state, horizon)
    if capped >= maximum_state:
        return 0
    return countdown_pair_ambiguity(
        maximum_state, capped
    ) - countdown_pair_ambiguity(maximum_state, capped + 1)


def countdown_collision_precision_gain(
    maximum_state: int,
    horizon: int,
    order: int,
) -> int:
    """Order-k ambiguity removed by one extra future step."""
    maximum_state, capped = _inputs(maximum_state, horizon)
    if capped >= maximum_state:
        return 0
    return countdown_collision_ambiguity(
        maximum_state, capped, order
    ) - countdown_collision_ambiguity(
        maximum_state, capped + 1, order
    )


def countdown_total_pair_gain(maximum_state: int) -> int:
    """Telescoped pair ambiguity removed before terminal discreteness."""
    _inputs(maximum_state, 0)
    return sum(
        countdown_pair_precision_gain(maximum_state, horizon)
        for horizon in range(maximum_state)
    )


@dataclass(frozen=True)
class PrecisionFiltrationStage:
    horizon: int
    class_count: int
    fiber_shape: tuple[int, ...]
    pair_ambiguity: int
    next_pair_gain: int


def countdown_precision_filtration(
    maximum_state: int,
) -> tuple[PrecisionFiltrationStage, ...]:
    _inputs(maximum_state, 0)
    return tuple(
        PrecisionFiltrationStage(
            horizon=horizon,
            class_count=countdown_predictive_class_count(
                maximum_state, horizon
            ),
            fiber_shape=countdown_future_fiber_shape(
                maximum_state, horizon
            ),
            pair_ambiguity=countdown_pair_ambiguity(
                maximum_state, horizon
            ),
            next_pair_gain=countdown_pair_precision_gain(
                maximum_state, horizon
            ),
        )
        for horizon in range(maximum_state + 1)
    )
