"""Reverse dependency distance geometry of operation-support growth.

The predecessor expansion Q_(t+1)=Q_t union Pred(Q_t) is exactly breadth-first
growth in the reverse helper-dependency graph.  Q_t consists of helpers at
reverse dependency distance at most t from the declared actions Q.  The first
fixed-point time is the maximum such distance over down(Q).
"""

from __future__ import annotations

from dataclasses import dataclass

from .balanced_binary_synergy import balanced_binary_synergy
from .closure_interference_support_growth import support_growth_layers
from .closure_async_progress_poset import helper_predecessors


@dataclass(frozen=True)
class SupportHorizonGeometry:
    arity: int
    actions: frozenset[str]
    distance_by_helper: tuple[tuple[str, int], ...]
    horizon: int
    layer_sizes: tuple[int, ...]
    ball_identity_verified: bool


def reverse_dependency_distances(arity: int, actions: frozenset[str]) -> dict[str, int]:
    compiler = balanced_binary_synergy(arity)
    helpers = frozenset(compiler.helpers)
    if not actions or not actions.issubset(helpers):
        raise ValueError("actions must be a nonempty helper subset")
    predecessors = helper_predecessors(arity)
    distance = {action: 0 for action in actions}
    frontier = set(actions)
    level = 0
    while frontier:
        nxt = set()
        for node in frontier:
            for pred in predecessors[node]:
                if pred not in distance:
                    distance[pred] = level + 1
                    nxt.add(pred)
        frontier = nxt
        level += 1
    return distance


def support_horizon_geometry(arity: int, actions: frozenset[str]) -> SupportHorizonGeometry:
    distance = reverse_dependency_distances(arity, actions)
    layers = support_growth_layers(arity, actions)
    horizon = max(distance.values(), default=0)
    verified = len(layers) == horizon + 1
    if verified:
        for t, layer in enumerate(layers):
            ball = frozenset(node for node, dist in distance.items() if dist <= t)
            if ball != layer:
                verified = False
                break
    if not verified:
        raise AssertionError("predecessor expansion must equal reverse dependency balls")
    return SupportHorizonGeometry(
        arity=arity,
        actions=actions,
        distance_by_helper=tuple(sorted(distance.items())),
        horizon=horizon,
        layer_sizes=tuple(len(layer) for layer in layers),
        ball_identity_verified=verified,
    )
