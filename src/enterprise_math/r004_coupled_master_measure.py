"""Coupling-compressed finite rational counterfactual master measures.

The original R004 existence compiler samples every mutually exclusive action
branch independently.  Independence is stronger than the operational marginal
requirement: a literal word or deterministic adaptive policy selects only one
action at each realized node.

At every state/depth this module therefore builds the correct child-master
marginal for each action, then couples those marginals using the exact rational
common-quantile construction.  The resulting joint response-table measure has
the same selected-action marginals and hence the same literal-word/adaptive
policy laws, while often using far fewer deterministic masters.

This is a resource-compression construction, not a new causal assumption.  The
choice of coupling among counterfactual branches is operationally invisible in
the declared single-action-at-a-node language unless extra cross-world
observables are added.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Hashable, Mapping
from fractions import Fraction
from functools import lru_cache

from .r004_causal_identifiability_completion import (
    Action,
    CounterfactualMaster,
    State,
)
from .r004_counterfactual_coupling import common_quantile_coupling


def _state_set(states) -> frozenset[State]:
    result = frozenset(states)
    if not result:
        raise ValueError("state set must be nonempty")
    return result


def _action_order(actions) -> tuple[Action, ...]:
    result = tuple(actions)
    if not result:
        raise ValueError("action family must be nonempty")
    if len(set(result)) != len(result):
        raise ValueError("actions must be unique")
    return tuple(sorted(result, key=repr))


def _validate_rational_kernels(
    states,
    kernels: Mapping[Action, Mapping[State, Mapping[State, Fraction]]],
) -> tuple[
    frozenset[State],
    tuple[Action, ...],
    dict[Action, dict[State, dict[State, Fraction]]],
]:
    state_values = _state_set(states)
    actions = _action_order(kernels)
    normalized: dict[Action, dict[State, dict[State, Fraction]]] = {}
    for action in actions:
        rows: dict[State, dict[State, Fraction]] = {}
        for source in state_values:
            if source not in kernels[action]:
                raise ValueError("kernel is missing a declared source state")
            row: dict[State, Fraction] = {}
            for target, raw_weight in kernels[action][source].items():
                if isinstance(raw_weight, bool) or not isinstance(raw_weight, (int, Fraction)):
                    raise ValueError("kernel weights must be int or Fraction")
                weight = Fraction(raw_weight)
                if target not in state_values:
                    raise ValueError("kernel contains a target outside the declared state set")
                if weight < 0:
                    raise ValueError("kernel weights must be nonnegative")
                if weight:
                    row[target] = weight
            if not row or sum(row.values(), Fraction(0)) != 1:
                raise ValueError("every rational kernel row must have positive support summing to one")
            rows[source] = row
        normalized[action] = rows
    return state_values, actions, normalized


def compile_coupled_rational_master_measure(
    states,
    kernels: Mapping[Action, Mapping[State, Mapping[State, Fraction]]],
    source: State,
    horizon: int,
) -> dict[CounterfactualMaster, Fraction]:
    """Compile a policy-independent master measure with coupled action branches.

    The result is not claimed minimum-support.  It is a constructive compression
    that replaces counterfactual branch independence by an exact coupling while
    preserving every selected-action child marginal recursively.
    """
    state_values, actions, normalized = _validate_rational_kernels(states, kernels)
    if source not in state_values:
        raise ValueError("source is outside the declared state set")
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 0:
        raise ValueError("horizon must be a non-negative integer")

    @lru_cache(maxsize=None)
    def compile_from(state: State, depth: int) -> tuple[tuple[CounterfactualMaster, Fraction], ...]:
        if depth == 0:
            leaf = CounterfactualMaster(state=state, depth=0, branches=())
            return ((leaf, Fraction(1)),)

        child_marginals: dict[Action, dict[CounterfactualMaster, Fraction]] = {}
        for action in actions:
            marginal: defaultdict[CounterfactualMaster, Fraction] = defaultdict(Fraction)
            for target, transition_weight in normalized[action][state].items():
                for child, child_weight in compile_from(target, depth - 1):
                    marginal[child] += transition_weight * child_weight
            child_marginals[action] = dict(marginal)

        response_coupling = common_quantile_coupling(child_marginals)
        result: defaultdict[CounterfactualMaster, Fraction] = defaultdict(Fraction)
        for response_table, weight in response_coupling.items():
            branches = tuple((action, child) for action, child in response_table)
            master = CounterfactualMaster(
                state=state,
                depth=depth,
                branches=branches,
            )
            result[master] += weight

        if sum(result.values(), Fraction(0)) != 1:
            raise AssertionError("coupled master measure must retain unit total mass")
        return tuple(result.items())

    return dict(compile_from(source, horizon))


def master_support_compression_ratio(
    independent_measure: Mapping[Hashable, Fraction],
    coupled_measure: Mapping[Hashable, Fraction],
) -> tuple[int, int]:
    """Return support sizes (coupled, independent) without inventing a scalar ratio."""
    if not independent_measure or not coupled_measure:
        raise ValueError("both master measures must be nonempty")
    return len(coupled_measure), len(independent_measure)
