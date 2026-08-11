"""Contextual finite-code reflection for weighted local laws.

The coarse theorem in ``bounded_local_law_reflection`` uses one global union of
all local aggregate values.  That is sufficient but can overstate the required
coefficient precision: aggregate values living in different semantic signature
coordinates are never compared.

For a fixed initial observation, every later refinement block remains inside one
initial observation class.  Therefore one target-block coefficient has a stable
semantic coordinate

    (action, source_observation, target_observation).

For each such coordinate, collect all subset-sum aggregates that any fine source
in the source observation class can contribute to a target block contained in
the target observation class.  A quotient modulus is contextually reflective
when reduction is injective **inside every one of these codebooks separately**.
Cross-coordinate residue collisions are harmless.

The module also removes a verification circularity from the parent bridge.  A
modular-only weighted law (same edge structure, only residue weights) plus the
known exact admissible contextual codebooks is enough to reconstruct the exact
integer weighted quotient matrix.  No exact primitive edge weight is consulted
by the decoder.

This is the executable form of the reflection principle:

    finite quotient code + semantic coordinate + finite admissible codebook
        -> exact local law
        -> exact unbounded composition in the source algebra.

Context-dependent coding and finite-alphabet decoding are standard prior
mathematics/information theory.  The project value is the exact precision
routing and the removal of unnecessary cross-coordinate injectivity demands.
"""

from __future__ import annotations

from typing import Callable, Hashable, Mapping, Sequence

from .bounded_local_law_reflection import (
    Matrix,
    WeightedFamily,
    _states,
    _weighted_family,
    modulus_is_injective_on_values,
    subset_sum_alphabet,
    weighted_refinement_sequence,
)
from .relation_support_stable_refinement import (
    Partition,
    normalize_partition,
    partition_from_observation,
)


State = Hashable
Action = Hashable
Observation = Hashable
Context = tuple[Action, Observation, Observation]
ModularWeightedFamily = Mapping[Action, Mapping[tuple[State, State], int]]


def contextual_local_aggregate_codebooks(
    states: Sequence[State],
    family: WeightedFamily,
    observation: Callable[[State], Observation],
) -> dict[Context, frozenset[int]]:
    """Admissible block aggregates keyed by semantic signature coordinate."""
    order = _states(states)
    weighted = _weighted_family(order, family)
    labels = {state: observation(state) for state in order}
    for label in labels.values():
        hash(label)

    source_labels = tuple(dict.fromkeys(labels[state] for state in order))
    target_labels = source_labels
    result: dict[Context, set[int]] = {}

    for action, relation in weighted.items():
        for source_label in source_labels:
            sources = tuple(state for state in order if labels[state] == source_label)
            for target_label in target_labels:
                key = (action, source_label, target_label)
                values = {0}
                for source in sources:
                    outgoing = tuple(
                        weight
                        for (left, target), weight in relation.items()
                        if left == source and labels[target] == target_label
                    )
                    values.update(subset_sum_alphabet(outgoing))
                result[key] = values
    return {key: frozenset(values) for key, values in result.items()}


def modulus_is_contextually_reflective(
    codebooks: Mapping[Context, Sequence[int] | frozenset[int]],
    modulus: int,
) -> bool:
    if not codebooks:
        raise ValueError("at least one contextual codebook is required")
    return all(
        modulus_is_injective_on_values(values, modulus)
        for values in codebooks.values()
    )


def minimal_contextual_reflective_modulus(
    codebooks: Mapping[Context, Sequence[int] | frozenset[int]],
) -> int:
    if not codebooks:
        raise ValueError("at least one contextual codebook is required")
    widths = []
    for values in codebooks.values():
        alphabet = tuple(set(values))
        if not alphabet:
            raise ValueError("contextual codebooks must be nonempty")
        widths.append(max(alphabet) - min(alphabet))
    guaranteed = max(2, max(widths, default=0) + 1)
    for modulus in range(2, guaranteed + 1):
        if modulus_is_contextually_reflective(codebooks, modulus):
            return modulus
    raise AssertionError("context-width bound failed to supply a reflective modulus")


def modularize_weighted_family(
    states: Sequence[State],
    family: WeightedFamily,
    modulus: int,
) -> dict[Action, dict[tuple[State, State], int]]:
    order = _states(states)
    weighted = _weighted_family(order, family)
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 1:
        raise ValueError("modulus must exceed one")
    return {
        action: {edge: weight % modulus for edge, weight in relation.items()}
        for action, relation in weighted.items()
    }


def _validate_modular_family(
    states: Sequence[State],
    family: ModularWeightedFamily,
    modulus: int,
) -> dict[Action, dict[tuple[State, State], int]]:
    order = _states(states)
    state_set = set(order)
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 1:
        raise ValueError("modulus must exceed one")
    if not family:
        raise ValueError("modular weighted family must be nonempty")
    result: dict[Action, dict[tuple[State, State], int]] = {}
    for action, relation in family.items():
        mapping = dict(relation)
        for edge, residue in mapping.items():
            if not isinstance(edge, tuple) or len(edge) != 2:
                raise TypeError("modular weighted relation keys must be ordered pairs")
            source, target = edge
            if source not in state_set or target not in state_set:
                raise ValueError("modular edge lies outside declared state set")
            if isinstance(residue, bool) or not isinstance(residue, int):
                raise TypeError("modular primitive weights must be integers")
            if not 0 <= residue < modulus:
                raise ValueError("modular primitive weights must be canonical residues")
        result[action] = mapping
    return result


def modular_target_block_aggregate(
    partition: Sequence[Sequence[State] | frozenset[State]],
    relation: Mapping[tuple[State, State], int],
    source: State,
    target_block_index: int,
    modulus: int,
) -> int:
    current = normalize_partition(partition)
    states = frozenset().union(*current)
    if source not in states:
        raise ValueError("source outside partition")
    if not 0 <= target_block_index < len(current):
        raise ValueError("target_block_index outside partition")
    if modulus <= 1:
        raise ValueError("modulus must exceed one")
    target_block = current[target_block_index]
    return sum(
        residue
        for (left, target), residue in relation.items()
        if left == source and target in target_block
    ) % modulus


def decode_contextual_residue(
    residue: int,
    modulus: int,
    codebook: Sequence[int] | frozenset[int],
) -> int:
    alphabet = tuple(set(codebook))
    if not alphabet:
        raise ValueError("codebook must be nonempty")
    if not modulus_is_injective_on_values(alphabet, modulus):
        raise ValueError("modulus is not injective on this contextual codebook")
    candidates = tuple(value for value in alphabet if value % modulus == residue % modulus)
    if len(candidates) != 1:
        raise ValueError("residue has no unique contextual exact lift")
    return candidates[0]


def reconstruct_exact_quotient_from_modular_only(
    states: Sequence[State],
    partition: Sequence[Sequence[State] | frozenset[State]],
    modular_family: ModularWeightedFamily,
    observation: Callable[[State], Observation],
    modulus: int,
    codebooks: Mapping[Context, Sequence[int] | frozenset[int]],
) -> dict[Action, Matrix]:
    """Decode exact quotient weights without consulting exact primitive weights."""
    order = _states(states)
    current = normalize_partition(partition)
    if frozenset().union(*current) != frozenset(order):
        raise ValueError("partition must cover exactly the declared states")
    modular = _validate_modular_family(order, modular_family, modulus)
    if not modulus_is_contextually_reflective(codebooks, modulus):
        raise ValueError("modulus is not reflective on all contextual codebooks")

    block_labels: list[Observation] = []
    for block in current:
        labels = {observation(state) for state in block}
        if len(labels) != 1:
            raise ValueError("partition must refine the declared observation")
        block_labels.append(next(iter(labels)))

    matrices: dict[Action, Matrix] = {}
    for action, relation in modular.items():
        columns: list[tuple[int, ...]] = []
        for source_block_index, source_block in enumerate(current):
            source_label = block_labels[source_block_index]
            modular_vectors = tuple(
                tuple(
                    modular_target_block_aggregate(
                        current,
                        relation,
                        source,
                        target_block_index,
                        modulus,
                    )
                    for target_block_index in range(len(current))
                )
                for source in source_block
            )
            if len(set(modular_vectors)) != 1:
                raise ValueError(
                    f"partition is not modular-stable for action {action!r} at source block {source_block_index}"
                )
            lifted: list[int] = []
            for target_block_index, residue in enumerate(modular_vectors[0]):
                target_label = block_labels[target_block_index]
                key = (action, source_label, target_label)
                if key not in codebooks:
                    raise ValueError("missing contextual codebook for quotient coordinate")
                lifted.append(
                    decode_contextual_residue(
                        residue,
                        modulus,
                        codebooks[key],
                    )
                )
            columns.append(tuple(lifted))
        matrices[action] = tuple(
            tuple(columns[source][target] for source in range(len(current)))
            for target in range(len(current))
        )
    return matrices


def contextual_reflection_reproduces_exact_sequence(
    states: Sequence[State],
    family: WeightedFamily,
    observation: Callable[[State], Observation],
    modulus: int,
) -> bool:
    order = _states(states)
    weighted = _weighted_family(order, family)
    codebooks = contextual_local_aggregate_codebooks(order, weighted, observation)
    if not modulus_is_contextually_reflective(codebooks, modulus):
        raise ValueError("modulus is not contextually reflective")
    initial = partition_from_observation(order, observation)
    exact = weighted_refinement_sequence(initial, weighted)
    modular = weighted_refinement_sequence(initial, weighted, modulus=modulus)
    if exact != modular:
        raise AssertionError("contextual reflection failed exact refinement sequence")
    return True
