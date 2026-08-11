"""Arithmetic structure of the literal word-cache Pareto frontier.

For fixed horizon H, literal cache storage grows strictly with cache depth d,
while worst-case block execution rounds are ceil(H/d).  Therefore a cache depth
is nondominated exactly when it is the **smallest** depth achieving one of the
distinct round counts.

Equivalently, the Pareto cache depths are the distinct values

    ceil(H/r),  r=1,...,H.

This set depends only on H, not on action alphabet size k.  The action count
changes the storage coordinate S(k,d), often exponentially, but not where the
runtime step function changes.

Using ceil(H/r)=floor((H-1)/r)+1, the classical divisor-quotient decomposition
implies only O(sqrt(H)) distinct values.  A simple bound used here is

    #frontier <= 2*ceil(sqrt(H)).

Thus the discrete storage/depth Pareto is sparse even when every cache depth is
allowed.
"""

from __future__ import annotations

from math import isqrt

from .future_word_cache_pareto import (
    cache_execution_rounds,
    word_cache_pareto_frontier,
)


def frontier_cache_depths_closed_form(horizon: int) -> tuple[int, ...]:
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 1:
        raise ValueError("horizon must be a positive integer")
    values = {
        (horizon + rounds - 1) // rounds
        for rounds in range(1, horizon + 1)
    }
    return tuple(sorted(values))


def frontier_cache_depths_match_enumeration(action_count: int, horizon: int) -> bool:
    predicted = frontier_cache_depths_closed_form(horizon)
    actual = tuple(point.cache_depth for point in word_cache_pareto_frontier(action_count, horizon))
    if predicted != actual:
        raise AssertionError("closed-form cache frontier disagreed with enumerated Pareto")
    return True


def frontier_point_count_bound(horizon: int) -> int:
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 1:
        raise ValueError("horizon must be a positive integer")
    root = isqrt(horizon)
    ceil_root = root if root * root == horizon else root + 1
    return 2 * ceil_root


def frontier_is_sqrt_sparse(horizon: int) -> bool:
    return len(frontier_cache_depths_closed_form(horizon)) <= frontier_point_count_bound(horizon)


def frontier_round_counts(horizon: int) -> tuple[int, ...]:
    return tuple(
        cache_execution_rounds(horizon, depth)
        for depth in frontier_cache_depths_closed_form(horizon)
    )
