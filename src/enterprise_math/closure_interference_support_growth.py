"""Iterated support growth when hidden prerequisite state becomes executable.

For declared action family Q, Supplement 155 says Q-only words need state support
Q union Pred(Q).  If those newly exposed predecessor coordinates are themselves
promoted to executable actions, their own hidden predecessors become relevant.
Iterating

    Q_(t+1) = Q_t union Pred(Q_t)

reaches the predecessor/downward closure down(Q), exactly the autonomous action
support from Supplements 153-154.

Thus dependency closure can be viewed as precision generated step-by-step by an
expanding future operation envelope.
"""

from __future__ import annotations

from dataclasses import dataclass

from .balanced_binary_synergy import balanced_binary_synergy
from .closure_action_support_cost import action_dependency_support
from .closure_async_progress_poset import helper_ideals, helper_predecessors
from .closure_async_query_ladder import enabled_helpers


@dataclass(frozen=True)
class InterferenceSupportGrowth:
    arity: int
    initial_actions: frozenset[str]
    layers: tuple[frozenset[str], ...]
    layer_sizes: tuple[int, ...]
    fixed_point: frozenset[str]
    equals_dependency_closure: bool
    first_promotion_legality_collision: bool


def one_predecessor_expansion(arity: int, actions: frozenset[str]) -> frozenset[str]:
    compiler = balanced_binary_synergy(arity)
    helpers = frozenset(compiler.helpers)
    if not actions.issubset(helpers):
        raise ValueError("action set contains a non-helper label")
    predecessors = helper_predecessors(arity)
    expanded = set(actions)
    for action in actions:
        expanded.update(predecessors[action])
    return frozenset(expanded)


def support_growth_layers(arity: int, actions: frozenset[str]) -> tuple[frozenset[str], ...]:
    layers = [actions]
    while True:
        nxt = one_predecessor_expansion(arity, layers[-1])
        if nxt == layers[-1]:
            return tuple(layers)
        layers.append(nxt)


def _promotion_legality_collision(
    arity: int,
    current_actions: frozenset[str],
    promoted_actions: frozenset[str],
) -> bool:
    """Can same current-support projection give different legality for new actions?"""
    newly_promoted = promoted_actions.difference(current_actions)
    if not newly_promoted:
        return False
    # State support for the current action family is promoted_actions itself.
    support = promoted_actions
    ideals = tuple(helper_ideals(arity))
    by_projection: dict[frozenset[str], list[frozenset[str]]] = {}
    for ideal in ideals:
        by_projection.setdefault(frozenset(ideal.intersection(support)), []).append(ideal)
    for bucket in by_projection.values():
        observed = {
            frozenset(enabled_helpers(arity, ideal).intersection(newly_promoted))
            for ideal in bucket
        }
        if len(observed) > 1:
            return True
    return False


def interference_support_growth(arity: int, actions: frozenset[str]) -> InterferenceSupportGrowth:
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 4:
        raise ValueError("arity must be an integer >= 4")
    layers = support_growth_layers(arity, actions)
    dependency = action_dependency_support(arity, actions)
    if layers[-1] != dependency:
        raise AssertionError("iterated direct-predecessor expansion must reach downward closure")
    first_collision = False
    if len(layers) >= 3:
        # Q1 is enough state for Q0-only actions. If Q1 is then promoted to an
        # executable family, hidden predecessors outside Q1 can affect its new
        # action legality; Q2 is the repair.
        first_collision = _promotion_legality_collision(arity, layers[0], layers[1])
    return InterferenceSupportGrowth(
        arity=arity,
        initial_actions=actions,
        layers=layers,
        layer_sizes=tuple(len(layer) for layer in layers),
        fixed_point=layers[-1],
        equals_dependency_closure=layers[-1] == dependency,
        first_promotion_legality_collision=first_collision,
    )
