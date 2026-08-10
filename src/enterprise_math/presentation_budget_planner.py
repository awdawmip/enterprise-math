"""Exact inverse resource planner for literal macro-table presentations.

The parent presentation theorem maps macro depth d to

    stored rules S(k,d) = sum_(i=1)^d k^i
    worst-case execution blocks D(h,d) = ceil(h/d).

This module solves the inverse design problems inside the same literal-macro
representation class.

Depth budget R:
    the least macro depth satisfying ceil(h/d)<=R is

        d_min = ceil(h/R).

    Because storage is strictly increasing with d, this d_min also minimizes
    stored literal macro rules among all presentations meeting the execution
    budget.

Rule budget B:
    choose the largest d<=h with S(k,d)<=B.  Since execution depth decreases
    monotonically with d, this d maximizes precomputation and minimizes the
    worst-case execution blocks under B.

Scalar-storage budgets reduce to a rule budget by dividing by the per-rule
matrix cost b^2 for a b-dimensional transition state.

These are exact inverse laws only inside the literal macro-table class; circuits,
algebraic normal forms and shared DAGs can define different resource frontiers.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil

from .presentation_storage_depth_pareto import (
    PresentationParetoPoint,
    literal_macro_rule_count,
    macro_execution_blocks,
    presentation_pareto_point,
)


def _positive_int(value: int, *, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def minimal_macro_depth_for_execution_budget(
    horizon: int,
    max_execution_blocks: int,
) -> int:
    h = _positive_int(horizon, name="horizon")
    rounds = _positive_int(max_execution_blocks, name="max_execution_blocks")
    # More allowed rounds than literal generator execution needs do not reduce
    # the presentation below generator depth1.
    return max(1, ceil(h / rounds))


def minimal_rule_count_for_execution_budget(
    action_count: int,
    horizon: int,
    max_execution_blocks: int,
) -> int:
    k = _positive_int(action_count, name="action_count")
    d = minimal_macro_depth_for_execution_budget(horizon, max_execution_blocks)
    return literal_macro_rule_count(k, d)


def max_macro_depth_for_rule_budget(
    action_count: int,
    horizon: int,
    rule_budget: int,
) -> int:
    k = _positive_int(action_count, name="action_count")
    h = _positive_int(horizon, name="horizon")
    budget = _positive_int(rule_budget, name="rule_budget")
    if budget < k:
        raise ValueError("rule budget cannot even store the generator presentation")

    # Monotone exact search.  h is also the only useful upper macro depth for a
    # declared horizon, so no floating logarithm or approximation is required.
    low = 1
    high = h
    while low < high:
        middle = (low + high + 1) // 2
        if literal_macro_rule_count(k, middle) <= budget:
            low = middle
        else:
            high = middle - 1
    return low


def minimal_execution_blocks_for_rule_budget(
    action_count: int,
    horizon: int,
    rule_budget: int,
) -> int:
    d = max_macro_depth_for_rule_budget(action_count, horizon, rule_budget)
    return macro_execution_blocks(horizon, d)


def max_macro_depth_for_scalar_budget(
    action_count: int,
    horizon: int,
    state_dimension: int,
    scalar_budget: int,
) -> int:
    b = _positive_int(state_dimension, name="state_dimension")
    budget = _positive_int(scalar_budget, name="scalar_budget")
    per_rule = b * b
    rule_budget = budget // per_rule
    if rule_budget <= 0:
        raise ValueError("scalar budget cannot store one transition matrix")
    return max_macro_depth_for_rule_budget(action_count, horizon, rule_budget)


def minimal_execution_blocks_for_scalar_budget(
    action_count: int,
    horizon: int,
    state_dimension: int,
    scalar_budget: int,
) -> int:
    d = max_macro_depth_for_scalar_budget(
        action_count,
        horizon,
        state_dimension,
        scalar_budget,
    )
    return macro_execution_blocks(horizon, d)


@dataclass(frozen=True)
class ExecutionBudgetPlan:
    action_count: int
    horizon: int
    max_execution_blocks: int
    macro_depth: int
    stored_rules: int
    achieved_execution_blocks: int

    @property
    def slack_blocks(self) -> int:
        return self.max_execution_blocks - self.achieved_execution_blocks


def plan_for_execution_budget(
    action_count: int,
    horizon: int,
    max_execution_blocks: int,
) -> ExecutionBudgetPlan:
    k = _positive_int(action_count, name="action_count")
    h = _positive_int(horizon, name="horizon")
    rounds = _positive_int(max_execution_blocks, name="max_execution_blocks")
    d = minimal_macro_depth_for_execution_budget(h, rounds)
    achieved = macro_execution_blocks(h, d)
    if achieved > rounds:
        raise AssertionError("inverse depth formula failed execution budget")
    if d > 1 and macro_execution_blocks(h, d - 1) <= rounds:
        raise AssertionError("chosen macro depth is not minimal for execution budget")
    return ExecutionBudgetPlan(
        action_count=k,
        horizon=h,
        max_execution_blocks=rounds,
        macro_depth=d,
        stored_rules=literal_macro_rule_count(k, d),
        achieved_execution_blocks=achieved,
    )


@dataclass(frozen=True)
class RuleBudgetPlan:
    action_count: int
    horizon: int
    rule_budget: int
    macro_depth: int
    stored_rules: int
    achieved_execution_blocks: int
    unused_rule_budget: int


def plan_for_rule_budget(
    action_count: int,
    horizon: int,
    rule_budget: int,
) -> RuleBudgetPlan:
    k = _positive_int(action_count, name="action_count")
    h = _positive_int(horizon, name="horizon")
    budget = _positive_int(rule_budget, name="rule_budget")
    d = max_macro_depth_for_rule_budget(k, h, budget)
    stored = literal_macro_rule_count(k, d)
    if stored > budget:
        raise AssertionError("chosen macro depth exceeded rule budget")
    if d < h and literal_macro_rule_count(k, d + 1) <= budget:
        raise AssertionError("chosen macro depth is not maximal under rule budget")
    return RuleBudgetPlan(
        action_count=k,
        horizon=h,
        rule_budget=budget,
        macro_depth=d,
        stored_rules=stored,
        achieved_execution_blocks=macro_execution_blocks(h, d),
        unused_rule_budget=budget - stored,
    )


@dataclass(frozen=True)
class ScalarBudgetPlan:
    action_count: int
    horizon: int
    state_dimension: int
    scalar_budget: int
    macro_depth: int
    stored_rules: int
    stored_transition_scalars: int
    achieved_execution_blocks: int
    unused_scalars: int


def plan_for_scalar_budget(
    action_count: int,
    horizon: int,
    state_dimension: int,
    scalar_budget: int,
) -> ScalarBudgetPlan:
    k = _positive_int(action_count, name="action_count")
    h = _positive_int(horizon, name="horizon")
    b = _positive_int(state_dimension, name="state_dimension")
    budget = _positive_int(scalar_budget, name="scalar_budget")
    d = max_macro_depth_for_scalar_budget(k, h, b, budget)
    point: PresentationParetoPoint = presentation_pareto_point(
        k,
        h,
        d,
        state_dimension=b,
    )
    stored_scalars = point.stored_transition_scalars
    if stored_scalars is None:
        raise AssertionError("state dimension failed scalar storage accounting")
    if stored_scalars > budget:
        raise AssertionError("scalar-budget plan exceeded storage budget")
    return ScalarBudgetPlan(
        action_count=k,
        horizon=h,
        state_dimension=b,
        scalar_budget=budget,
        macro_depth=d,
        stored_rules=point.stored_macro_rules,
        stored_transition_scalars=stored_scalars,
        achieved_execution_blocks=point.worst_case_execution_blocks,
        unused_scalars=budget - stored_scalars,
    )


def state_compression_execution_gain(
    action_count: int,
    horizon: int,
    scalar_budget: int,
    larger_state_dimension: int,
    smaller_state_dimension: int,
) -> tuple[ScalarBudgetPlan, ScalarBudgetPlan]:
    """Compare two exact state representations under one scalar-storage budget."""
    large = _positive_int(larger_state_dimension, name="larger_state_dimension")
    small = _positive_int(smaller_state_dimension, name="smaller_state_dimension")
    if small >= large:
        raise ValueError("smaller_state_dimension must be strictly smaller")
    return (
        plan_for_scalar_budget(action_count, horizon, large, scalar_budget),
        plan_for_scalar_budget(action_count, horizon, small, scalar_budget),
    )
