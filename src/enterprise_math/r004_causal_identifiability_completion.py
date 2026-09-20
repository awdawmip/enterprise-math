"""Finite counterfactual-completion compiler for R004 / FQ-20260810-007.

This owner-local research module pressure-tests whether finite causal/accessibility
or intervention syntax can, by itself, distinguish online branching from a finite
latent pre-sampled completion.

Two exact finite constructions are provided.

1. Possibilistic relation families.
   For a finite action-indexed relation family and finite horizon, compile every
   complete deterministic counterfactual master tree.  Each master chooses one
   successor subtree for every declared action at every contingent node.  The
   union of master outcomes for every literal action word exactly equals the raw
   relational support for that word, including disabled words.

2. Total rational stochastic kernels.
   Construct one policy-independent rational probability measure over finite
   deterministic counterfactual masters by pre-sampling, independently at each
   latent node, one weighted child master for every counterfactual action.  The
   same measure reproduces the exact state law of every literal action word and
   the exact history law of every deterministic adaptive policy through the
   compiled horizon.

The construction is deliberately a *no-go pressure test*, not a proposed
physical hidden-variable law.  It shows that unrestricted finite latent state
extension is enough to absorb finite branching/randomization syntax into an
ex-ante deterministic master.  Therefore operational falsifiability of such
pre-sampling requires an additional admissibility restriction on latent
extensions (for example an independently justified capacity or factorization
constraint).

This module does not re-own A1/A2/A4 mother theory, FQ-004, or FQ-006.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable, Hashable, Iterable, Mapping, Sequence
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import product


State = Hashable
Action = Hashable
Relation = frozenset[tuple[State, State]]
Policy = Callable[[tuple[State, ...]], Action]


@dataclass(frozen=True)
class CounterfactualMaster:
    """One deterministic finite contingent-response tree."""

    state: State
    depth: int
    branches: tuple[tuple[Action, CounterfactualMaster | None], ...]


def _state_set(states: Iterable[State]) -> frozenset[State]:
    result = frozenset(states)
    if not result:
        raise ValueError("state set must be nonempty")
    return result


def _action_order(actions: Iterable[Action]) -> tuple[Action, ...]:
    result = tuple(actions)
    if not result:
        raise ValueError("action family must be nonempty")
    if len(set(result)) != len(result):
        raise ValueError("actions must be unique")
    return tuple(sorted(result, key=repr))


def _validate_relations(
    states: frozenset[State],
    relations: Mapping[Action, Relation],
) -> tuple[Action, ...]:
    actions = _action_order(relations)
    for relation in relations.values():
        if not isinstance(relation, frozenset):
            raise TypeError("relations must be frozensets")
        if any(source not in states or target not in states for source, target in relation):
            raise ValueError("relation contains a state outside the declared state set")
    return actions


def _relation_successors(
    relation: Relation,
    source: State,
) -> tuple[State, ...]:
    return tuple(sorted((target for state, target in relation if state == source), key=repr))


def compile_support_masters(
    states: Iterable[State],
    relations: Mapping[Action, Relation],
    source: State,
    horizon: int,
) -> tuple[CounterfactualMaster, ...]:
    """Compile all deterministic counterfactual masters through ``horizon``.

    A disabled action is stored as ``None``.  If an action is enabled, a master
    chooses one successor and one complete child master for that successor.  The
    Cartesian product over actions is the unrestricted counterfactual table at
    the current latent node.
    """
    state_values = _state_set(states)
    actions = _validate_relations(state_values, relations)
    if source not in state_values:
        raise ValueError("source is outside the declared state set")
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")

    @lru_cache(maxsize=None)
    def compile_from(state: State, depth: int) -> tuple[CounterfactualMaster, ...]:
        if depth == 0:
            return (CounterfactualMaster(state=state, depth=0, branches=()),)

        choices_by_action: list[tuple[CounterfactualMaster | None, ...]] = []
        for action in actions:
            successors = _relation_successors(relations[action], state)
            if not successors:
                choices_by_action.append((None,))
                continue
            child_choices: list[CounterfactualMaster] = []
            for target in successors:
                child_choices.extend(compile_from(target, depth - 1))
            choices_by_action.append(tuple(child_choices))

        masters: list[CounterfactualMaster] = []
        for chosen_children in product(*choices_by_action):
            masters.append(
                CounterfactualMaster(
                    state=state,
                    depth=depth,
                    branches=tuple(zip(actions, chosen_children, strict=True)),
                )
            )
        return tuple(masters)

    return compile_from(source, horizon)


def master_child(master: CounterfactualMaster, action: Action) -> CounterfactualMaster | None:
    """Read one declared action branch from a deterministic master."""
    for declared_action, child in master.branches:
        if declared_action == action:
            return child
    raise ValueError("action is not declared at this master node")


def master_word_target(
    master: CounterfactualMaster,
    word: Sequence[Action],
) -> State | None:
    """Run one literal action word through one master; ``None`` means disabled."""
    node = master
    for action in word:
        child = master_child(node, action)
        if child is None:
            return None
        node = child
    return node.state


def raw_relation_word_support(
    states: Iterable[State],
    relations: Mapping[Action, Relation],
    source: State,
    word: Sequence[Action],
) -> frozenset[State]:
    """Direct A4-style reachable support of a literal relation word."""
    state_values = _state_set(states)
    _validate_relations(state_values, relations)
    if source not in state_values:
        raise ValueError("source is outside the declared state set")

    support = frozenset({source})
    for action in word:
        if action not in relations:
            raise ValueError("word contains an undeclared action")
        support = frozenset(
            target
            for current, target in relations[action]
            if current in support
        )
    return support


def masters_word_support(
    masters: Iterable[CounterfactualMaster],
    word: Sequence[Action],
) -> frozenset[State]:
    """Union the visible target states produced by a family of masters."""
    result: set[State] = set()
    for master in masters:
        target = master_word_target(master, word)
        if target is not None:
            result.add(target)
    return frozenset(result)


def support_completion_holds(
    states: Iterable[State],
    relations: Mapping[Action, Relation],
    source: State,
    horizon: int,
) -> bool:
    """Check exact support agreement for every word up to ``horizon``."""
    state_values = _state_set(states)
    actions = _validate_relations(state_values, relations)
    masters = compile_support_masters(state_values, relations, source, horizon)
    for depth in range(horizon + 1):
        for word in product(actions, repeat=depth):
            if masters_word_support(masters, word) != raw_relation_word_support(
                state_values,
                relations,
                source,
                word,
            ):
                return False
    return True


def _validate_rational_kernels(
    states: Iterable[State],
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
            row = {
                target: Fraction(weight)
                for target, weight in kernels[action][source].items()
            }
            if any(target not in state_values for target in row):
                raise ValueError("kernel contains a target outside the declared state set")
            if any(weight < 0 for weight in row.values()):
                raise ValueError("kernel weights must be nonnegative")
            positive_row = {target: weight for target, weight in row.items() if weight}
            if not positive_row:
                raise ValueError("every rational kernel row must have positive support")
            if sum(positive_row.values(), Fraction(0)) != 1:
                raise ValueError("every rational kernel row must sum exactly to one")
            rows[source] = positive_row
        normalized[action] = rows

    return state_values, actions, normalized


def compile_rational_master_measure(
    states: Iterable[State],
    kernels: Mapping[Action, Mapping[State, Mapping[State, Fraction]]],
    source: State,
    horizon: int,
) -> dict[CounterfactualMaster, Fraction]:
    """Compile one policy-independent rational measure over deterministic masters.

    This routine intentionally accepts *total* rational kernels.  Partial-action
    legality is a separate FQ-006 channel; the possibilistic relation compiler
    above already permits disabled relation actions.
    """
    state_values, actions, normalized = _validate_rational_kernels(states, kernels)
    if source not in state_values:
        raise ValueError("source is outside the declared state set")
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")

    @lru_cache(maxsize=None)
    def compile_from(state: State, depth: int) -> tuple[tuple[CounterfactualMaster, Fraction], ...]:
        if depth == 0:
            master = CounterfactualMaster(state=state, depth=0, branches=())
            return ((master, Fraction(1)),)

        distributions_by_action: list[tuple[tuple[CounterfactualMaster, Fraction], ...]] = []
        for action in actions:
            child_distribution: defaultdict[CounterfactualMaster, Fraction] = defaultdict(Fraction)
            for target, transition_weight in normalized[action][state].items():
                for child, child_weight in compile_from(target, depth - 1):
                    child_distribution[child] += transition_weight * child_weight
            distributions_by_action.append(tuple(child_distribution.items()))

        result: defaultdict[CounterfactualMaster, Fraction] = defaultdict(Fraction)
        for chosen in product(*distributions_by_action):
            children = tuple(child for child, _ in chosen)
            weight = Fraction(1)
            for _, child_weight in chosen:
                weight *= child_weight
            master = CounterfactualMaster(
                state=state,
                depth=depth,
                branches=tuple(zip(actions, children, strict=True)),
            )
            result[master] += weight
        return tuple(result.items())

    return dict(compile_from(source, horizon))


def rational_word_law(
    states: Iterable[State],
    kernels: Mapping[Action, Mapping[State, Mapping[State, Fraction]]],
    source: State,
    word: Sequence[Action],
) -> dict[State, Fraction]:
    """Direct exact rational state law after one literal action word."""
    state_values, _, normalized = _validate_rational_kernels(states, kernels)
    if source not in state_values:
        raise ValueError("source is outside the declared state set")

    law: dict[State, Fraction] = {source: Fraction(1)}
    for action in word:
        if action not in normalized:
            raise ValueError("word contains an undeclared action")
        next_law: defaultdict[State, Fraction] = defaultdict(Fraction)
        for current, current_weight in law.items():
            for target, transition_weight in normalized[action][current].items():
                next_law[target] += current_weight * transition_weight
        law = dict(next_law)
    return law


def master_measure_word_law(
    master_measure: Mapping[CounterfactualMaster, Fraction],
    word: Sequence[Action],
) -> dict[State, Fraction]:
    """Push a pre-sampled master measure through one literal action word."""
    result: defaultdict[State, Fraction] = defaultdict(Fraction)
    for master, weight in master_measure.items():
        target = master_word_target(master, word)
        if target is None:
            raise ValueError("total-kernel master unexpectedly contains a disabled branch")
        result[target] += weight
    return dict(result)


def direct_policy_history_law(
    states: Iterable[State],
    kernels: Mapping[Action, Mapping[State, Mapping[State, Fraction]]],
    source: State,
    horizon: int,
    policy: Policy,
) -> dict[tuple[State, ...], Fraction]:
    """Exact history law when a deterministic policy chooses actions online."""
    state_values, _, normalized = _validate_rational_kernels(states, kernels)
    if source not in state_values:
        raise ValueError("source is outside the declared state set")
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")

    law: dict[tuple[State, ...], Fraction] = {(source,): Fraction(1)}
    for _ in range(horizon):
        next_law: defaultdict[tuple[State, ...], Fraction] = defaultdict(Fraction)
        for history, history_weight in law.items():
            action = policy(history)
            if action not in normalized:
                raise ValueError("policy returned an undeclared action")
            for target, transition_weight in normalized[action][history[-1]].items():
                next_law[history + (target,)] += history_weight * transition_weight
        law = dict(next_law)
    return law


def master_measure_policy_history_law(
    master_measure: Mapping[CounterfactualMaster, Fraction],
    horizon: int,
    policy: Policy,
) -> dict[tuple[State, ...], Fraction]:
    """History law induced by the same ex-ante master measure under a policy."""
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")

    result: defaultdict[tuple[State, ...], Fraction] = defaultdict(Fraction)
    for master, master_weight in master_measure.items():
        node = master
        history = (master.state,)
        for _ in range(horizon):
            action = policy(history)
            child = master_child(node, action)
            if child is None:
                raise ValueError("total-kernel master unexpectedly contains a disabled branch")
            node = child
            history = history + (node.state,)
        result[history] += master_weight
    return dict(result)
