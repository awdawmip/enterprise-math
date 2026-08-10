"""Workload-weighted selection on the support-promotion Pareto frontier.

Given positive costs alpha (per executable action), beta (per retained state
coordinate), and gamma (per remaining promotion-horizon unit), assign

    C_t = alpha*|A_t| + beta*|R_t| + gamma*(h-t).

No weights are canonical.  Once a workload declares them, the optimal promotion
depth is simply the minimum-cost frontier point.  Adjacent promotion t->t+1
lowers cost iff

    gamma > alpha*Delta|A| + beta*Delta|R|.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .closure_support_promotion_frontier import support_promotion_frontier


@dataclass(frozen=True)
class WeightedPromotionChoice:
    arity: int
    actions: frozenset[str]
    alpha: Fraction
    beta: Fraction
    gamma: Fraction
    costs: tuple[Fraction, ...]
    optimal_depths: tuple[int, ...]
    minimum_cost: Fraction
    adjacent_switch_thresholds: tuple[Fraction, ...]


def _positive_fraction(value: int | Fraction, name: str) -> Fraction:
    result = value if isinstance(value, Fraction) else Fraction(value)
    if result <= 0:
        raise ValueError(f"{name} must be positive")
    return result


def weighted_promotion_choice(
    arity: int,
    actions: frozenset[str],
    *,
    alpha: int | Fraction,
    beta: int | Fraction,
    gamma: int | Fraction,
) -> WeightedPromotionChoice:
    a = _positive_fraction(alpha, "alpha")
    b = _positive_fraction(beta, "beta")
    g = _positive_fraction(gamma, "gamma")
    frontier = support_promotion_frontier(arity, actions)
    costs = tuple(
        a * point.executable_action_count
        + b * point.static_state_support_count
        + g * point.remaining_horizon
        for point in frontier.points
    )
    minimum = min(costs)
    optimal = tuple(index for index, cost in enumerate(costs) if cost == minimum)
    thresholds = []
    for left, right in zip(frontier.points, frontier.points[1:]):
        delta_actions = right.executable_action_count - left.executable_action_count
        delta_state = right.static_state_support_count - left.static_state_support_count
        thresholds.append(a * delta_actions + b * delta_state)
    return WeightedPromotionChoice(
        arity=arity,
        actions=actions,
        alpha=a,
        beta=b,
        gamma=g,
        costs=costs,
        optimal_depths=optimal,
        minimum_cost=minimum,
        adjacent_switch_thresholds=tuple(thresholds),
    )
