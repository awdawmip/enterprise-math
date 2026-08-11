"""Exact semantic word normalization through a finite transformation monoid.

For total deterministic operations on a finite state set, every literal action
word induces one total transformation X->X.  The generated transformation monoid
is finite (at most |X|^|X| elements).

Instead of storing one lookup entry for every literal word through a horizon, one
may store:

* each reachable semantic transformation once;
* the monoid Cayley multiplication table;
* one generator->monoid-element map.

A literal word is then normalized to its exact effect ID by multiplying generator
IDs.  Associativity allows a balanced reduction with depth ceil(log2 h) for a
length-h word, followed by one application of the resulting transformation to
the state.

This produces a third point between generator replay and full literal caching:

* generators: tiny storage, h state-update rounds;
* full literal cache: exponential word-key storage, one lookup/apply round;
* semantic monoid: horizon-independent algebra storage, logarithmic parallel
  normalization depth plus one state application.

The monoid route is not universally smaller.  Its Cayley table costs m^2 cells;
for short horizons or large generated monoids, a literal cache can be cheaper.
The project therefore treats semantic normalization as another representation
Pareto, not as free compression.

Transformation semigroups/monoids and parallel associative reduction are
standard prior algebra/CS.  The Enterprise Math value is the explicit Stage131
resource accounting between literal law tables and exact operational normal
forms.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Mapping, Sequence

from .future_word_cache_pareto import (
    Transformation,
    _validated_operations,
    compose_transformations,
    literal_word_count,
    word_transformation,
)


State = Hashable
Action = Hashable


@dataclass(frozen=True)
class TransformationMonoid:
    states: tuple[State, ...]
    action_names: tuple[Action, ...]
    elements: tuple[Transformation, ...]
    identity_id: int
    generator_ids: dict[Action, int]
    multiplication_table: tuple[tuple[int, ...], ...]

    @property
    def size(self) -> int:
        return len(self.elements)


def generated_transformation_monoid(
    states: Sequence[State],
    operations: Mapping[Action, Mapping[State, State]],
) -> TransformationMonoid:
    order, names, family = _validated_operations(states, operations)
    identity = tuple(range(len(order)))
    generators = {
        name: word_transformation(order, family, (name,))
        for name in names
    }

    discovered = {identity, *generators.values()}
    frontier = list(discovered)
    while frontier:
        left = frontier.pop()
        for generator in generators.values():
            product = compose_transformations(left, generator)
            if product not in discovered:
                discovered.add(product)
                frontier.append(product)
                if len(discovered) > len(order) ** len(order):
                    raise AssertionError("transformation monoid exceeded full endomap bound")

    elements = tuple(sorted(discovered))
    ids = {element: index for index, element in enumerate(elements)}
    if identity not in ids:
        raise AssertionError("generated monoid lost identity")

    table_rows = []
    for left in elements:
        row = []
        for right in elements:
            product = compose_transformations(left, right)
            if product not in ids:
                raise AssertionError("generated transformation set is not composition-closed")
            row.append(ids[product])
        table_rows.append(tuple(row))

    return TransformationMonoid(
        states=order,
        action_names=names,
        elements=elements,
        identity_id=ids[identity],
        generator_ids={name: ids[effect] for name, effect in generators.items()},
        multiplication_table=tuple(table_rows),
    )


def multiply_effect_ids(monoid: TransformationMonoid, left_id: int, right_id: int) -> int:
    size = monoid.size
    for name, value in (("left_id", left_id), ("right_id", right_id)):
        if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value < size:
            raise ValueError(f"{name} outside monoid")
    return monoid.multiplication_table[left_id][right_id]


def normalize_word_sequential(
    monoid: TransformationMonoid,
    word: Sequence[Action],
) -> int:
    current = monoid.identity_id
    for action in word:
        if action not in monoid.generator_ids:
            raise ValueError("word contains undeclared action")
        current = multiply_effect_ids(monoid, current, monoid.generator_ids[action])
    return current


def parallel_normalization_depth(word_length: int) -> int:
    if isinstance(word_length, bool) or not isinstance(word_length, int) or word_length < 0:
        raise ValueError("word_length must be nonnegative")
    if word_length <= 1:
        return 0
    return (word_length - 1).bit_length()


def normalize_word_parallel(
    monoid: TransformationMonoid,
    word: Sequence[Action],
) -> tuple[int, int]:
    """Return exact effect ID and balanced multiplication depth."""
    values = tuple(word)
    if not values:
        return monoid.identity_id, 0
    layer = []
    for action in values:
        if action not in monoid.generator_ids:
            raise ValueError("word contains undeclared action")
        layer.append(monoid.generator_ids[action])

    depth = 0
    while len(layer) > 1:
        nxt = []
        index = 0
        while index < len(layer):
            if index + 1 == len(layer):
                nxt.append(layer[index])
                index += 1
            else:
                nxt.append(multiply_effect_ids(monoid, layer[index], layer[index + 1]))
                index += 2
        layer = nxt
        depth += 1

    expected = parallel_normalization_depth(len(values))
    if depth != expected:
        raise AssertionError("balanced normalizer depth disagreed with ceil-log2 law")
    return layer[0], depth


def normalized_word_effect_matches_literal(
    monoid: TransformationMonoid,
    operations: Mapping[Action, Mapping[State, State]],
    word: Sequence[Action],
) -> bool:
    sequential = normalize_word_sequential(monoid, word)
    parallel, _depth = normalize_word_parallel(monoid, word)
    if sequential != parallel:
        raise AssertionError("sequential and parallel normalizers disagree")
    direct = word_transformation(monoid.states, operations, word)
    if monoid.elements[sequential] != direct:
        raise AssertionError("semantic normal form disagreed with literal word effect")
    return True


def apply_effect_id(
    monoid: TransformationMonoid,
    state: State,
    effect_id: int,
) -> State:
    if state not in monoid.states:
        raise ValueError("state outside monoid action domain")
    if isinstance(effect_id, bool) or not isinstance(effect_id, int) or not 0 <= effect_id < monoid.size:
        raise ValueError("effect_id outside monoid")
    source_index = monoid.states.index(state)
    target_index = monoid.elements[effect_id][source_index]
    return monoid.states[target_index]


@dataclass(frozen=True)
class WordRepresentationResourceReport:
    state_count: int
    action_count: int
    monoid_size: int
    horizon: int
    generator_state_table_cells: int
    literal_word_id_entries: int
    semantic_effect_state_cells: int
    literal_cache_total_cells: int
    cayley_table_cells: int
    normal_form_total_cells: int
    generator_state_execution_rounds: int
    literal_cache_execution_rounds: int
    parallel_normal_form_rounds: int
    sequential_normal_form_rounds: int

    @property
    def normal_form_auxiliary_smaller_than_literal_index(self) -> bool:
        return self.cayley_table_cells < self.literal_word_id_entries


def word_representation_resource_report(
    states: Sequence[State],
    operations: Mapping[Action, Mapping[State, State]],
    horizon: int,
) -> WordRepresentationResourceReport:
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 1:
        raise ValueError("horizon must be positive")
    monoid = generated_transformation_monoid(states, operations)
    n = len(monoid.states)
    k = len(monoid.action_names)
    m = monoid.size
    literal_entries = literal_word_count(k, horizon)
    semantic_cells = m * n
    cayley_cells = m * m
    return WordRepresentationResourceReport(
        state_count=n,
        action_count=k,
        monoid_size=m,
        horizon=horizon,
        generator_state_table_cells=k * n,
        literal_word_id_entries=literal_entries,
        semantic_effect_state_cells=semantic_cells,
        literal_cache_total_cells=literal_entries + semantic_cells,
        cayley_table_cells=cayley_cells,
        normal_form_total_cells=cayley_cells + semantic_cells,
        generator_state_execution_rounds=horizon,
        literal_cache_execution_rounds=1,
        parallel_normal_form_rounds=parallel_normalization_depth(horizon) + 1,
        sequential_normal_form_rounds=horizon,
    )
