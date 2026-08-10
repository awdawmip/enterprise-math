"""Closed structural laws for the literal-macro budget frontier.

Because stored rule count S(k,d) is strictly increasing in d for every k>=1,
Pareto dominance among macro depths is controlled entirely by execution depth
``ceil(h/d)``.  Therefore the set of nondominated macro depths depends only on
the declared horizon:

    D_h = { ceil(h/r) : r=1,...,h }.

The action count k changes the storage coordinate attached to each depth, but not
which depths are Pareto-efficient.

For dense transition matrices of state dimension b, the minimum scalar storage
needed to meet an execution budget R is exactly

    b^2 * S(k, ceil(h/R)).

Hence changing exact state representation from dimension b to r multiplies the
transition-macro storage needed for the same literal-macro latency target by the
exact factor r^2/b^2.

These are representation-class laws, not hardware or circuit lower bounds.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import ceil, isqrt

from .presentation_budget_planner import (
    minimal_macro_depth_for_execution_budget,
    minimal_rule_count_for_execution_budget,
)
from .presentation_storage_depth_pareto import (
    PresentationParetoPoint,
    literal_macro_pareto_frontier,
    literal_macro_rule_count,
    macro_execution_blocks,
)


def _positive_int(value: int, *, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def horizon_pareto_macro_depths(horizon: int) -> tuple[int, ...]:
    h = _positive_int(horizon, name="horizon")
    return tuple(
        sorted(
            {ceil(h / rounds) for rounds in range(1, h + 1)}
        )
    )


def pareto_depths_match_scanned_frontier(action_count: int, horizon: int) -> bool:
    k = _positive_int(action_count, name="action_count")
    h = _positive_int(horizon, name="horizon")
    predicted = horizon_pareto_macro_depths(h)
    scanned = tuple(
        sorted(point.macro_depth for point in literal_macro_pareto_frontier(k, h))
    )
    if predicted != scanned:
        raise AssertionError("horizon-only Pareto depth theorem disagreed with scanned frontier")
    return True


def pareto_frontier_size_sqrt_bound(horizon: int) -> int:
    """Simple O(sqrt(h)) upper bound for the number of distinct Pareto depths.

    Since ``ceil(h/r)=floor((h-1)/r)+1``, the usual divisor-quotient argument
    gives at most ``2*floor(sqrt(h-1))+1`` distinct values (including the value1
    from r=h).  The bound is intentionally simple, not always tight.
    """
    h = _positive_int(horizon, name="horizon")
    if h == 1:
        return 1
    return 2 * isqrt(h - 1) + 1


def minimal_scalar_storage_for_execution_budget(
    action_count: int,
    horizon: int,
    max_execution_blocks: int,
    state_dimension: int,
) -> int:
    k = _positive_int(action_count, name="action_count")
    h = _positive_int(horizon, name="horizon")
    rounds = _positive_int(max_execution_blocks, name="max_execution_blocks")
    b = _positive_int(state_dimension, name="state_dimension")
    rules = minimal_rule_count_for_execution_budget(k, h, rounds)
    return b * b * rules


def same_latency_storage_ratio(
    larger_state_dimension: int,
    smaller_state_dimension: int,
) -> Fraction:
    large = _positive_int(larger_state_dimension, name="larger_state_dimension")
    small = _positive_int(smaller_state_dimension, name="smaller_state_dimension")
    if small >= large:
        raise ValueError("smaller_state_dimension must be strictly smaller")
    return Fraction(small * small, large * large)


@dataclass(frozen=True)
class LatencyTargetStorageComparison:
    action_count: int
    horizon: int
    max_execution_blocks: int
    macro_depth: int
    stored_rules: int
    larger_state_dimension: int
    smaller_state_dimension: int
    larger_scalar_storage: int
    smaller_scalar_storage: int
    exact_storage_ratio: Fraction

    @property
    def scalar_storage_saved(self) -> int:
        return self.larger_scalar_storage - self.smaller_scalar_storage


def compare_state_dimensions_at_same_latency(
    action_count: int,
    horizon: int,
    max_execution_blocks: int,
    larger_state_dimension: int,
    smaller_state_dimension: int,
) -> LatencyTargetStorageComparison:
    k = _positive_int(action_count, name="action_count")
    h = _positive_int(horizon, name="horizon")
    rounds = _positive_int(max_execution_blocks, name="max_execution_blocks")
    large = _positive_int(larger_state_dimension, name="larger_state_dimension")
    small = _positive_int(smaller_state_dimension, name="smaller_state_dimension")
    if small >= large:
        raise ValueError("smaller_state_dimension must be strictly smaller")

    depth = minimal_macro_depth_for_execution_budget(h, rounds)
    rules = literal_macro_rule_count(k, depth)
    large_storage = large * large * rules
    small_storage = small * small * rules
    ratio = Fraction(small_storage, large_storage)
    expected = same_latency_storage_ratio(large, small)
    if ratio != expected:
        raise AssertionError("state-dimension storage scaling lost square law")
    if macro_execution_blocks(h, depth) > rounds:
        raise AssertionError("latency-target comparison missed execution budget")
    return LatencyTargetStorageComparison(
        action_count=k,
        horizon=h,
        max_execution_blocks=rounds,
        macro_depth=depth,
        stored_rules=rules,
        larger_state_dimension=large,
        smaller_state_dimension=small,
        larger_scalar_storage=large_storage,
        smaller_scalar_storage=small_storage,
        exact_storage_ratio=ratio,
    )


def frontier_points_from_horizon_formula(
    action_count: int,
    horizon: int,
    *,
    state_dimension: int | None = None,
) -> tuple[PresentationParetoPoint, ...]:
    k = _positive_int(action_count, name="action_count")
    h = _positive_int(horizon, name="horizon")
    if state_dimension is not None:
        _positive_int(state_dimension, name="state_dimension")
    return tuple(
        PresentationParetoPoint(
            action_count=k,
            horizon=h,
            macro_depth=depth,
            stored_macro_rules=literal_macro_rule_count(k, depth),
            worst_case_execution_blocks=macro_execution_blocks(h, depth),
            state_dimension=state_dimension,
        )
        for depth in horizon_pareto_macro_depths(h)
    )
