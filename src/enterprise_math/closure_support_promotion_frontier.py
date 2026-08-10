"""Pareto frontier between executable action support and static state support.

Given predecessor-expansion layers Q^0,...,Q^h=down(Q), choose a promotion depth
t: actions Q^t are executable.  If t<h, Q^(t+1) is the exact one-layer static
state support used by the Stage155 Q-only compiler; at t=h the action family is
already predecessor-closed and state/action support coincide.

The structural cost vector is

    (|actions|, |state support|, remaining promotion horizon).

Along strict growth layers the first two coordinates do not improve as t grows,
while the remaining horizon strictly improves, so every stage is nondominated
without an external workload/cost weighting.
"""

from __future__ import annotations

from dataclasses import dataclass

from .closure_interference_support_growth import support_growth_layers


@dataclass(frozen=True)
class SupportPromotionPoint:
    promotion_depth: int
    executable_action_count: int
    static_state_support_count: int
    remaining_horizon: int
    actions: frozenset[str]
    state_support: frozenset[str]


@dataclass(frozen=True)
class SupportPromotionFrontier:
    arity: int
    initial_actions: frozenset[str]
    horizon: int
    points: tuple[SupportPromotionPoint, ...]
    all_points_nondominated: bool


def support_promotion_frontier(arity: int, actions: frozenset[str]) -> SupportPromotionFrontier:
    layers = support_growth_layers(arity, actions)
    horizon = len(layers) - 1
    points = []
    for t, action_layer in enumerate(layers):
        state_layer = layers[min(t + 1, horizon)]
        points.append(
            SupportPromotionPoint(
                promotion_depth=t,
                executable_action_count=len(action_layer),
                static_state_support_count=len(state_layer),
                remaining_horizon=horizon - t,
                actions=action_layer,
                state_support=state_layer,
            )
        )

    def dominates(left: SupportPromotionPoint, right: SupportPromotionPoint) -> bool:
        a = (
            left.executable_action_count,
            left.static_state_support_count,
            left.remaining_horizon,
        )
        b = (
            right.executable_action_count,
            right.static_state_support_count,
            right.remaining_horizon,
        )
        return all(x <= y for x, y in zip(a, b)) and any(x < y for x, y in zip(a, b))

    nondominated = all(
        not any(dominates(other, point) for other in points if other != point)
        for point in points
    )
    return SupportPromotionFrontier(
        arity=arity,
        initial_actions=actions,
        horizon=horizon,
        points=tuple(points),
        all_points_nondominated=nondominated,
    )
