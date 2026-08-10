"""Path-count precision and its Boolean support quotient for finite relations.

For one literal action word in a finite relation family, propagate a natural-
number count of witness paths.  With no parallel relation edges, the count at a
target is the number of distinct intermediate-state sequences realizing the word.

The coefficient map

    phi : N -> B,    phi(n) = 1[n>0]

is a semiring homomorphism.  Therefore the Boolean observed-support signature of
one relation word is exactly the positivity image of its natural-number observed
path-count signature.

Consequences:

* exact path-count future equality always refines Boolean reachable-support
  equality;
* the converse can fail when two sources reach the same observed class with
  different witness multiplicities;
* reducing counts modulo M gives another coarser future signature, so exact count
  equality also refines every declared modular-count equality.

This module intentionally counts paths only.  It still forgets literal path
identity once several paths contribute to one integer count.

Adjacency-matrix/path counting and the N->Boolean support map are standard prior
mathematics/automata theory.  The project value is the explicit coefficient-
precision bridge for A4/P023.
"""

from __future__ import annotations

from collections.abc import Callable, Hashable, Mapping, Sequence
from itertools import product

from .admissible_support import Relation
from .relation_future_powerset import relation_word_observed_support


State = Hashable
Observation = Hashable
Action = Hashable


def _states(values: Sequence[State]) -> tuple[State, ...]:
    result = tuple(values)
    if not result:
        raise ValueError("state order must be nonempty")
    if len(set(result)) != len(result):
        raise ValueError("state order must contain distinct states")
    return result


def _family(
    states: tuple[State, ...],
    relations: Mapping[Action, Relation],
) -> dict[Action, Relation]:
    if not relations:
        raise ValueError("relation family must be nonempty")
    state_set = set(states)
    result = dict(relations)
    for relation in result.values():
        if not isinstance(relation, frozenset):
            raise TypeError("relations must be frozensets")
        if any(source not in state_set or target not in state_set for source, target in relation):
            raise ValueError("relation contains state outside declared order")
    return result


def words_through_horizon(
    actions: Sequence[Action],
    horizon: int,
) -> tuple[tuple[Action, ...], ...]:
    if isinstance(horizon, bool) or not isinstance(horizon, int):
        raise TypeError("horizon must be an integer")
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    action_values = tuple(actions)
    if not action_values:
        if horizon == 0:
            return ((),)
        raise ValueError("positive horizon requires actions")
    return tuple(
        word
        for length in range(horizon + 1)
        for word in product(action_values, repeat=length)
    )


def relation_word_path_counts(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    source: State,
    word: Sequence[Action],
) -> tuple[int, ...]:
    """Natural-number path counts at each named target state."""
    order = _states(states)
    family = _family(order, relations)
    if source not in order:
        raise ValueError("source is outside declared state order")
    index = {state: position for position, state in enumerate(order)}
    counts = [0] * len(order)
    counts[index[source]] = 1
    for action in word:
        if action not in family:
            raise ValueError("word contains undeclared action")
        after = [0] * len(order)
        for current, target in family[action]:
            after[index[target]] += counts[index[current]]
        counts = after
    return tuple(counts)


def observed_path_counts(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    source: State,
    word: Sequence[Action],
    observation: Callable[[State], Observation],
) -> tuple[tuple[Observation, int], ...]:
    order = _states(states)
    counts = relation_word_path_counts(order, relations, source, word)
    labels: list[Observation] = []
    for state in order:
        label = observation(state)
        if label not in labels:
            labels.append(label)
    return tuple(
        (
            label,
            sum(
                count
                for state, count in zip(order, counts, strict=True)
                if observation(state) == label
            ),
        )
        for label in labels
    )


def positive_count_observed_support(
    observed_counts: Sequence[tuple[Observation, int]],
) -> frozenset[Observation]:
    result = []
    for label, count in observed_counts:
        if isinstance(count, bool) or not isinstance(count, int) or count < 0:
            raise ValueError("path counts must be nonnegative integers")
        if count > 0:
            result.append(label)
    return frozenset(result)


def path_count_support_homomorphism_matches(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    source: State,
    word: Sequence[Action],
    observation: Callable[[State], Observation],
) -> bool:
    counts = observed_path_counts(
        states,
        relations,
        source,
        word,
        observation,
    )
    positive = positive_count_observed_support(counts)
    boolean = relation_word_observed_support(
        states,
        relations,
        source,
        word,
        observation,
    )
    if positive != boolean:
        raise AssertionError("N->Boolean path-support homomorphism failed")
    return True


def path_count_future_signature(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    source: State,
    observation: Callable[[State], Observation],
    horizon: int,
    *,
    modulus: int | None = None,
) -> tuple[tuple[tuple[Action, ...], tuple[tuple[Observation, int], ...]], ...]:
    order = _states(states)
    family = _family(order, relations)
    if modulus is not None:
        if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 0:
            raise ValueError("modulus must be a positive integer")
    signature = []
    for word in words_through_horizon(tuple(family), horizon):
        counts = observed_path_counts(
            order,
            family,
            source,
            word,
            observation,
        )
        if modulus is not None:
            counts = tuple((label, count % modulus) for label, count in counts)
        signature.append((word, counts))
    return tuple(signature)


def path_count_future_partition(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
    *,
    modulus: int | None = None,
) -> frozenset[frozenset[State]]:
    order = _states(states)
    groups: dict[object, set[State]] = {}
    for source in order:
        signature = path_count_future_signature(
            order,
            relations,
            source,
            observation,
            horizon,
            modulus=modulus,
        )
        groups.setdefault(signature, set()).add(source)
    return frozenset(frozenset(group) for group in groups.values())


def partition_refines(
    finer: frozenset[frozenset[State]],
    coarser: frozenset[frozenset[State]],
) -> bool:
    return all(any(block.issubset(parent) for parent in coarser) for block in finer)


def count_partition_refines_support_partition(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
) -> bool:
    from .relation_future_powerset import relation_family_future_partition

    counts = path_count_future_partition(
        states,
        relations,
        observation,
        horizon,
    )
    support = relation_family_future_partition(
        states,
        relations,
        observation,
        horizon,
    )
    if not partition_refines(counts, support):
        raise AssertionError("path-count precision failed to refine support precision")
    return True


def exact_count_partition_refines_modular_partition(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
    modulus: int,
) -> bool:
    exact = path_count_future_partition(
        states,
        relations,
        observation,
        horizon,
    )
    modular = path_count_future_partition(
        states,
        relations,
        observation,
        horizon,
        modulus=modulus,
    )
    if not partition_refines(exact, modular):
        raise AssertionError("exact path-count precision failed to refine modular count precision")
    return True
