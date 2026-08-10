"""Deterministic powerset compiler for finite A4 relation-valued future words.

A finite relation ``R`` is multivalued on raw states, but it induces an ordinary
total deterministic map on support sets:

    R_hat(S) = { y : exists x in S, (x,y) in R }.

The empty set is absorbing.  For a declared target observation ``O``, lift it to

    O_hat(S) = { O(x) : x in S }.

Then every literal word of relation generators is represented exactly by normal
function composition of the corresponding ``R_hat`` maps on ``P(X)``.  Starting
from singleton ``{x}``, the final support and observed-support signature are
exactly those of the raw relational word.

This supplies a finite A4->P023 compiler boundary:

    raw correspondence
      -> deterministic powerset support dynamics
      -> declared observed-support future signature
      -> ordinary functional-kernel/future-quotient machinery.

The powerset state is a compiler/analysis object, not a new physical ontology.
It preserves reachable **support only**.  Distinct witness paths that reach the
same target are merged, and branches that die while other branches survive are
not individually remembered.  Therefore a future language that reads path
multiplicity, branch identity, per-branch definedness or other A4 witness data
must use a richer witness/correspondence state instead of this support compiler.

Subset construction, relational image and nondeterministic automata are standard
prior mathematics/computer science.  This module only makes the project routing
between A4 support and P023 deterministic future signatures explicit.
"""

from __future__ import annotations

from collections.abc import Callable, Hashable, Iterable, Mapping, Sequence
from itertools import product

from .admissible_support import Relation, compose_relations


State = Hashable
Observation = Hashable
Action = Hashable


def _state_set(states: Iterable[State]) -> frozenset[State]:
    result = frozenset(states)
    if not result:
        raise ValueError("state set must be nonempty")
    return result


def _validate_relation(states: frozenset[State], relation: Relation) -> None:
    if not isinstance(relation, frozenset):
        raise TypeError("relation must be a frozenset")
    if any(source not in states or target not in states for source, target in relation):
        raise ValueError("relation contains a state outside the declared state set")


def relation_support_image(
    states: Iterable[State],
    relation: Relation,
    support: Iterable[State],
) -> frozenset[State]:
    """Apply one relation to a finite support set as a total deterministic map."""
    state_values = _state_set(states)
    _validate_relation(state_values, relation)
    current = frozenset(support)
    if not current.issubset(state_values):
        raise ValueError("support contains a state outside the declared state set")
    return frozenset(
        target
        for source, target in relation
        if source in current
    )


def observed_support(
    support: Iterable[State],
    observation: Callable[[State], Observation],
) -> frozenset[Observation]:
    """Powerset-lifted target observation ``O_hat``."""
    return frozenset(observation(state) for state in support)


def _relation_family(
    states: frozenset[State],
    relations: Mapping[Action, Relation],
) -> dict[Action, Relation]:
    if not relations:
        raise ValueError("relation family must contain at least one action")
    result = dict(relations)
    for relation in result.values():
        _validate_relation(states, relation)
    return result


def relation_word_support(
    states: Iterable[State],
    relations: Mapping[Action, Relation],
    source: State,
    word: Sequence[Action],
) -> frozenset[State]:
    """Exact final support of one literal relation word from singleton source."""
    state_values = _state_set(states)
    family = _relation_family(state_values, relations)
    if source not in state_values:
        raise ValueError("source is outside the declared state set")
    support = frozenset({source})
    for action in word:
        if action not in family:
            raise ValueError("word contains an undeclared relation action")
        support = relation_support_image(
            state_values,
            family[action],
            support,
        )
    return support


def relation_word_observed_support(
    states: Iterable[State],
    relations: Mapping[Action, Relation],
    source: State,
    word: Sequence[Action],
    observation: Callable[[State], Observation],
) -> frozenset[Observation]:
    return observed_support(
        relation_word_support(states, relations, source, word),
        observation,
    )


def composed_relation_for_word(
    states: Iterable[State],
    relations: Mapping[Action, Relation],
    word: Sequence[Action],
) -> Relation:
    """Return raw finite relational composition for a nonempty literal word."""
    state_values = _state_set(states)
    family = _relation_family(state_values, relations)
    if not word:
        return frozenset((state, state) for state in state_values)
    first = word[0]
    if first not in family:
        raise ValueError("word contains an undeclared relation action")
    result = family[first]
    for action in word[1:]:
        if action not in family:
            raise ValueError("word contains an undeclared relation action")
        result = compose_relations(result, family[action])
    return result


def support_compiler_matches_raw_composition(
    states: Iterable[State],
    relations: Mapping[Action, Relation],
    source: State,
    word: Sequence[Action],
) -> bool:
    """Verify singleton powerset execution equals the target set of raw composition."""
    state_values = _state_set(states)
    support = relation_word_support(
        state_values,
        relations,
        source,
        word,
    )
    composed = composed_relation_for_word(
        state_values,
        relations,
        word,
    )
    direct = frozenset(target for current, target in composed if current == source)
    if support != direct:
        raise AssertionError("powerset compiler disagreed with relational composition")
    return True


def words_through_horizon(
    actions: Sequence[Action],
    horizon: int,
) -> tuple[tuple[Action, ...], ...]:
    """All literal words through a finite horizon, including the empty word."""
    if isinstance(horizon, bool) or not isinstance(horizon, int):
        raise TypeError("horizon must be an integer")
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    action_values = tuple(actions)
    if not action_values:
        if horizon == 0:
            return ((),)
        raise ValueError("positive horizon requires at least one action")
    if len(set(action_values)) != len(action_values):
        raise ValueError("action names must be unique")
    return tuple(
        word
        for length in range(horizon + 1)
        for word in product(action_values, repeat=length)
    )


def relation_family_future_signature(
    states: Iterable[State],
    relations: Mapping[Action, Relation],
    source: State,
    observation: Callable[[State], Observation],
    horizon: int,
) -> tuple[tuple[tuple[Action, ...], frozenset[Observation]], ...]:
    """Exact observed-support signature for every literal word through horizon."""
    state_values = _state_set(states)
    family = _relation_family(state_values, relations)
    words = words_through_horizon(tuple(family), horizon)
    return tuple(
        (
            word,
            relation_word_observed_support(
                state_values,
                family,
                source,
                word,
                observation,
            ),
        )
        for word in words
    )


def relation_family_future_partition(
    states: Iterable[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
) -> frozenset[frozenset[State]]:
    """Coarsest original-state partition for the declared finite relation-word language."""
    state_values = _state_set(states)
    family = _relation_family(state_values, relations)
    groups: dict[
        tuple[tuple[tuple[Action, ...], frozenset[Observation]], ...],
        set[State],
    ] = {}
    for source in state_values:
        signature = relation_family_future_signature(
            state_values,
            family,
            source,
            observation,
            horizon,
        )
        groups.setdefault(signature, set()).add(source)
    return frozenset(frozenset(group) for group in groups.values())


def aggregate_support_forgets_branch_survival(
    states: Iterable[State],
    relation: Relation,
    larger_support: Iterable[State],
    smaller_support: Iterable[State],
) -> bool:
    """Comparator: distinct input supports can have one identical aggregate image.

    This is not an error in the powerset compiler.  It explicitly diagnoses the
    boundary where a future language wanting per-branch survival cannot use
    aggregate reachable support as its complete state.
    """
    state_values = _state_set(states)
    large = frozenset(larger_support)
    small = frozenset(smaller_support)
    if large == small:
        raise ValueError("support comparator requires distinct input supports")
    large_image = relation_support_image(state_values, relation, large)
    small_image = relation_support_image(state_values, relation, small)
    return large_image == small_image
