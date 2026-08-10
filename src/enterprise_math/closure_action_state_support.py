"""Static state support versus autonomous action-support closure.

Assume the asynchronous helper phase has fixed raw antecedents already present.
For a declared helper action family Q, if *only actions in Q may fire*, then
legality of every Q-action depends only on the current status of the action and
its direct helper predecessors.  Hidden predecessors outside Q are static state
inputs; they need not themselves become declared executable actions.

Thus the Q-only word future factors through

    R_Q = Q union direct_helper_predecessors(Q).

This can be much smaller than the predecessor-closed autonomous action support
down(Q), which is needed when the dependency actions themselves are included in
the executable subsystem.
"""

from __future__ import annotations

from dataclasses import dataclass

from .balanced_binary_synergy import balanced_binary_synergy
from .closure_action_support_cost import (
    action_dependency_support,
    largest_single_action_support,
)
from .closure_async_progress_poset import helper_ideals, helper_predecessors
from .closure_async_query_ladder import enabled_helpers


@dataclass(frozen=True)
class ActionStateSupportReport:
    arity: int
    actions: frozenset[str]
    state_support: frozenset[str]
    autonomous_action_support: frozenset[str]
    q_word_one_step_factorization_verified: bool
    direct_predecessor_necessity_verified: bool


@dataclass(frozen=True)
class SingleActionSupportComparison:
    arity: int
    action: str
    raw_action_count: int
    static_state_support_count: int
    autonomous_action_support_count: int


def q_only_state_support(arity: int, actions: frozenset[str]) -> frozenset[str]:
    compiler = balanced_binary_synergy(arity)
    helpers = frozenset(compiler.helpers)
    if not actions.issubset(helpers):
        raise ValueError("action set contains a non-helper label")
    predecessors = helper_predecessors(arity)
    support = set(actions)
    for action in actions:
        support.update(predecessors[action])
    return frozenset(support)


def projected_q_enabled(
    arity: int,
    projected_state: frozenset[str],
    actions: frozenset[str],
    action: str,
) -> bool:
    if action not in actions:
        raise ValueError("action is not in declared Q family")
    support = q_only_state_support(arity, actions)
    if not projected_state.issubset(support):
        raise ValueError("projected state contains a label outside Q-only support")
    predecessors = helper_predecessors(arity)
    return action not in projected_state and predecessors[action].issubset(projected_state)


def _direct_predecessor_is_necessary(
    arity: int,
    actions: frozenset[str],
    action: str,
    predecessor: str,
) -> bool:
    """Find same reduced projection with different legality after dropping predecessor."""
    support = q_only_state_support(arity, actions)
    if predecessor not in support or predecessor in actions:
        # Declared actions themselves are retained by definition; this helper is
        # for hidden direct predecessor necessity.
        return True
    reduced = frozenset(support.difference({predecessor}))
    ideals = tuple(helper_ideals(arity))
    by_projection: dict[frozenset[str], list[frozenset[str]]] = {}
    for ideal in ideals:
        by_projection.setdefault(frozenset(ideal.intersection(reduced)), []).append(ideal)
    for bucket in by_projection.values():
        values = {action in enabled_helpers(arity, ideal) for ideal in bucket}
        if len(values) > 1:
            return True
    return False


def action_state_support_report(arity: int, actions: frozenset[str]) -> ActionStateSupportReport:
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 4:
        raise ValueError("arity must be an integer >= 4")
    support = q_only_state_support(arity, actions)
    autonomous = action_dependency_support(arity, actions)
    ideals = tuple(helper_ideals(arity))
    one_step = True
    for ideal in ideals:
        projected = frozenset(ideal.intersection(support))
        for action in actions:
            global_enabled = action in enabled_helpers(arity, ideal)
            local_enabled = projected_q_enabled(arity, projected, actions, action)
            if global_enabled != local_enabled:
                one_step = False
                break
        if not one_step:
            break

    predecessors = helper_predecessors(arity)
    necessary = all(
        _direct_predecessor_is_necessary(arity, actions, action, predecessor)
        for action in actions
        for predecessor in predecessors[action]
        if predecessor not in actions
    )

    return ActionStateSupportReport(
        arity=arity,
        actions=actions,
        state_support=support,
        autonomous_action_support=autonomous,
        q_word_one_step_factorization_verified=one_step,
        direct_predecessor_necessity_verified=necessary,
    )


def largest_single_action_support_comparison(arity: int) -> SingleActionSupportComparison:
    autonomous_report = largest_single_action_support(arity)
    action = next(iter(autonomous_report.support_generators))
    actions = frozenset({action})
    state_support = q_only_state_support(arity, actions)
    return SingleActionSupportComparison(
        arity=arity,
        action=action,
        raw_action_count=1,
        static_state_support_count=len(state_support),
        autonomous_action_support_count=autonomous_report.dependency_support_count,
    )
