"""Bounded local-law reflection before unbounded exact composition.

This module generalizes the unweighted count-branching cutoff.  Raw finite
transition laws may carry nonzero integer primitive weights.  For one source,
action and current target block, the exact local coefficient is the sum of the
primitive edge weights whose targets lie in that block.

Across every possible partition, such a coefficient belongs to a finite
**local aggregate alphabet**: for each source/action it is a subset sum of the
finitely many outgoing primitive weights.

If reduction modulo M is injective on that finite alphabet, exact integer and
mod-M weighted refinement steps are identical on every partition.  The full
stable weighted quotient is therefore recoverable from the modular world.  Each
local residue can then be uniquely lifted back to its exact integer aggregate.

Once the local weighted machine has been reflected exactly, future semantics may
be composed in the exact integer algebra.  Derived path weights can be
arbitrarily larger than M.  This is the precise ``reflect before compose``
mechanism: finite quotient precision is required only for the bounded primitive
local law, not for every unbounded derived value.

If instead one composes inside Z/MZ and only observes the final residue, distinct
large exact derived values can collide even though every local coefficient was
perfectly reflected.

Subset sums, weighted equitable partitions, quotient/lumping and modular
reflection on bounded sets are standard prior mathematics/CS.  The project value
is the explicit bounded-local-law -> unbounded-derived-semantics precision
architecture.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Hashable, Mapping, Sequence

from .relation_support_stable_refinement import (
    Partition,
    normalize_partition,
    partition_from_observation,
    partition_refines,
)


State = Hashable
Action = Hashable
Observation = Hashable
WeightedRelation = Mapping[tuple[State, State], int]
WeightedFamily = Mapping[Action, WeightedRelation]
Matrix = tuple[tuple[int, ...], ...]


def _states(values: Sequence[State]) -> tuple[State, ...]:
    result = tuple(values)
    if not result or len(set(result)) != len(result):
        raise ValueError("states must be a nonempty distinct sequence")
    return result


def _partition_states(partition: Partition) -> frozenset[State]:
    current = normalize_partition(partition)
    return frozenset().union(*current)


def _weighted_family(
    states: Sequence[State],
    family: WeightedFamily,
) -> dict[Action, dict[tuple[State, State], int]]:
    order = _states(states)
    state_set = set(order)
    if not family:
        raise ValueError("weighted action family must be nonempty")
    result: dict[Action, dict[tuple[State, State], int]] = {}
    for name, relation in family.items():
        mapping = dict(relation)
        for edge, weight in mapping.items():
            if not isinstance(edge, tuple) or len(edge) != 2:
                raise TypeError("weighted relation keys must be ordered state pairs")
            source, target = edge
            if source not in state_set or target not in state_set:
                raise ValueError("weighted edge contains state outside declared state set")
            if isinstance(weight, bool) or not isinstance(weight, int):
                raise TypeError("primitive edge weights must be integers")
            if weight == 0:
                raise ValueError("zero-weight edges are algebraically absent; omit them")
        result[name] = mapping
    return result


def outgoing_primitive_weights(
    states: Sequence[State],
    family: WeightedFamily,
    action: Action,
    source: State,
) -> tuple[int, ...]:
    order = _states(states)
    weighted = _weighted_family(order, family)
    if action not in weighted:
        raise ValueError("unknown action")
    if source not in order:
        raise ValueError("source outside declared state set")
    relation = weighted[action]
    return tuple(
        weight
        for (left, _target), weight in relation.items()
        if left == source
    )


def subset_sum_alphabet(weights: Sequence[int]) -> frozenset[int]:
    values = tuple(weights)
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("weights must be integers")
    sums = {0}
    for weight in values:
        sums.update(value + weight for value in tuple(sums))
    return frozenset(sums)


def weighted_local_aggregate_alphabet(
    states: Sequence[State],
    family: WeightedFamily,
) -> frozenset[int]:
    """All block aggregates that can occur under any target partition.

    A current target block intersects one source/action outgoing edge set in an
    arbitrary subset, so every local block aggregate is one of these subset sums.
    """
    order = _states(states)
    weighted = _weighted_family(order, family)
    alphabet = {0}
    for name in weighted:
        for source in order:
            alphabet.update(
                subset_sum_alphabet(
                    outgoing_primitive_weights(order, weighted, name, source)
                )
            )
    return frozenset(alphabet)


def bounded_primitive_sumset(
    primitive_weights: Sequence[int],
    max_terms: int,
) -> frozenset[int]:
    """Universal aggregate alphabet for <=max_terms edges drawn with repetition."""
    primitives = tuple(primitive_weights)
    if not primitives:
        raise ValueError("primitive_weights must be nonempty")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value == 0
        for value in primitives
    ):
        raise ValueError("primitive weights must be nonzero integers")
    if isinstance(max_terms, bool) or not isinstance(max_terms, int):
        raise TypeError("max_terms must be an integer")
    if max_terms < 0:
        raise ValueError("max_terms must be nonnegative")
    reachable = {0}
    frontier = {0}
    for _ in range(max_terms):
        frontier = {
            value + primitive
            for value in frontier
            for primitive in primitives
        }
        reachable.update(frontier)
    return frozenset(reachable)


def bounded_primitive_sumset_witnesses(
    primitive_weights: Sequence[int],
    max_terms: int,
) -> dict[int, tuple[int, ...]]:
    """One <=max_terms primitive decomposition for each universal aggregate."""
    primitives = tuple(primitive_weights)
    alphabet = bounded_primitive_sumset(primitives, max_terms)
    witness: dict[int, tuple[int, ...]] = {0: ()}
    frontier: dict[int, tuple[int, ...]] = {0: ()}
    for _ in range(max_terms):
        nxt: dict[int, tuple[int, ...]] = {}
        for value, terms in frontier.items():
            for primitive in primitives:
                total = value + primitive
                candidate = (*terms, primitive)
                if total not in witness:
                    witness[total] = candidate
                if total not in nxt:
                    nxt[total] = candidate
        frontier = nxt
    if set(witness) != set(alphabet):
        raise AssertionError("sumset witness compiler missed a reachable aggregate")
    return witness


def modulus_is_injective_on_values(values: Sequence[int] | frozenset[int], modulus: int) -> bool:
    alphabet = tuple(values)
    if not alphabet:
        raise ValueError("value alphabet must be nonempty")
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 1:
        raise ValueError("modulus must exceed one")
    residues = tuple(value % modulus for value in alphabet)
    return len(set(residues)) == len(set(alphabet))


def guaranteed_reflective_modulus_from_width(values: Sequence[int] | frozenset[int]) -> int:
    alphabet = tuple(set(values))
    if not alphabet:
        raise ValueError("value alphabet must be nonempty")
    width = max(alphabet) - min(alphabet)
    return max(2, width + 1)


def minimal_reflective_modulus(values: Sequence[int] | frozenset[int]) -> int:
    alphabet = tuple(set(values))
    if not alphabet:
        raise ValueError("value alphabet must be nonempty")
    upper = guaranteed_reflective_modulus_from_width(alphabet)
    for modulus in range(2, upper + 1):
        if modulus_is_injective_on_values(alphabet, modulus):
            return modulus
    raise AssertionError("width+1 failed to reflect a finite integer alphabet")


def exact_target_block_aggregate(
    partition: Sequence[Sequence[State] | frozenset[State]],
    relation: WeightedRelation,
    source: State,
    target_block_index: int,
) -> int:
    current = normalize_partition(partition)
    states = _partition_states(current)
    if source not in states:
        raise ValueError("source outside partition")
    if not 0 <= target_block_index < len(current):
        raise ValueError("target_block_index outside partition")
    target_block = current[target_block_index]
    total = 0
    for (left, target), weight in relation.items():
        if left == source and target in target_block:
            total += weight
    return total


def weighted_refinement_step(
    partition: Sequence[Sequence[State] | frozenset[State]],
    family: WeightedFamily,
    *,
    modulus: int | None = None,
) -> Partition:
    current = normalize_partition(partition)
    states = tuple(sorted(_partition_states(current), key=repr))
    weighted = _weighted_family(states, family)
    if modulus is not None:
        if isinstance(modulus, bool) or not isinstance(modulus, int):
            raise TypeError("modulus must be an integer")
        if modulus <= 1:
            raise ValueError("modulus must exceed one")
    names = tuple(sorted(weighted, key=repr))
    refined: list[set[State]] = []
    for block in current:
        groups: dict[tuple[object, ...], set[State]] = {}
        for state in block:
            signature = []
            for name in names:
                vector = tuple(
                    exact_target_block_aggregate(current, weighted[name], state, index)
                    for index in range(len(current))
                )
                if modulus is not None:
                    vector = tuple(value % modulus for value in vector)
                signature.append((name, vector))
            groups.setdefault(tuple(signature), set()).add(state)
        refined.extend(groups.values())
    result = normalize_partition(refined)
    if not partition_refines(result, current):
        raise AssertionError("weighted refinement failed to refine current partition")
    return result


def weighted_refinement_sequence(
    initial_partition: Sequence[Sequence[State] | frozenset[State]],
    family: WeightedFamily,
    *,
    modulus: int | None = None,
) -> tuple[Partition, ...]:
    current = normalize_partition(initial_partition)
    states = tuple(sorted(_partition_states(current), key=repr))
    _weighted_family(states, family)
    steps = [current]
    while True:
        nxt = weighted_refinement_step(current, family, modulus=modulus)
        if nxt == current:
            return tuple(steps)
        if len(nxt) <= len(current):
            raise AssertionError("strict weighted refinement failed block-count growth")
        steps.append(nxt)
        current = nxt
        if len(steps) - 1 > len(states) - len(steps[0]):
            raise AssertionError("weighted refinement exceeded finite block-growth bound")


def reflective_modulus_reproduces_exact_weighted_sequence(
    states: Sequence[State],
    family: WeightedFamily,
    observation: Callable[[State], Observation],
    modulus: int,
) -> bool:
    order = _states(states)
    weighted = _weighted_family(order, family)
    alphabet = weighted_local_aggregate_alphabet(order, weighted)
    if not modulus_is_injective_on_values(alphabet, modulus):
        raise ValueError("modulus is not injective on the local aggregate alphabet")
    initial = partition_from_observation(order, observation)
    exact = weighted_refinement_sequence(initial, weighted)
    modular = weighted_refinement_sequence(initial, weighted, modulus=modulus)
    if exact != modular:
        raise AssertionError("local-alphabet-reflective modulus changed weighted refinement sequence")
    return True


def decode_residue_from_local_alphabet(
    residue: int,
    modulus: int,
    alphabet: Sequence[int] | frozenset[int],
) -> int:
    values = tuple(set(alphabet))
    if not modulus_is_injective_on_values(values, modulus):
        raise ValueError("local alphabet is not injective modulo modulus")
    candidates = tuple(value for value in values if value % modulus == residue % modulus)
    if len(candidates) != 1:
        raise ValueError("residue has no unique local-alphabet lift")
    return candidates[0]


def exact_weighted_quotient_matrices(
    partition: Sequence[Sequence[State] | frozenset[State]],
    family: WeightedFamily,
) -> dict[Action, Matrix]:
    current = normalize_partition(partition)
    states = tuple(sorted(_partition_states(current), key=repr))
    weighted = _weighted_family(states, family)
    matrices: dict[Action, Matrix] = {}
    for name, relation in weighted.items():
        columns = []
        for source_block_index, source_block in enumerate(current):
            representatives = tuple(source_block)
            vectors = tuple(
                tuple(
                    exact_target_block_aggregate(
                        current,
                        relation,
                        source,
                        target_block_index,
                    )
                    for target_block_index in range(len(current))
                )
                for source in representatives
            )
            if len(set(vectors)) != 1:
                raise ValueError(
                    f"partition is not exact-weight-stable for action {name!r} at source block {source_block_index}"
                )
            columns.append(vectors[0])
        matrices[name] = tuple(
            tuple(columns[source][target] for source in range(len(current)))
            for target in range(len(current))
        )
    return matrices


def reconstruct_exact_quotient_from_modular_local_law(
    partition: Sequence[Sequence[State] | frozenset[State]],
    family: WeightedFamily,
    modulus: int,
) -> dict[Action, Matrix]:
    """Recover exact integer quotient weights from a reflective local modulus."""
    current = normalize_partition(partition)
    states = tuple(sorted(_partition_states(current), key=repr))
    weighted = _weighted_family(states, family)
    alphabet = weighted_local_aggregate_alphabet(states, weighted)
    if not modulus_is_injective_on_values(alphabet, modulus):
        raise ValueError("modulus is not reflective on local aggregate alphabet")

    matrices: dict[Action, Matrix] = {}
    for name, relation in weighted.items():
        columns = []
        for source_block_index, source_block in enumerate(current):
            modular_vectors = tuple(
                tuple(
                    exact_target_block_aggregate(
                        current,
                        relation,
                        source,
                        target_block_index,
                    )
                    % modulus
                    for target_block_index in range(len(current))
                )
                for source in source_block
            )
            if len(set(modular_vectors)) != 1:
                raise ValueError(
                    f"partition is not modular-weight-stable for action {name!r} at source block {source_block_index}"
                )
            lifted = tuple(
                decode_residue_from_local_alphabet(residue, modulus, alphabet)
                for residue in modular_vectors[0]
            )
            columns.append(lifted)
        matrices[name] = tuple(
            tuple(columns[source][target] for source in range(len(current)))
            for target in range(len(current))
        )
    return matrices


def weighted_word_state_values(
    states: Sequence[State],
    family: WeightedFamily,
    source: State,
    word: Sequence[Action],
    *,
    modulus: int | None = None,
) -> dict[State, int]:
    order = _states(states)
    weighted = _weighted_family(order, family)
    if source not in order:
        raise ValueError("source outside state set")
    current = {state: int(state == source) for state in order}
    for action in word:
        if action not in weighted:
            raise ValueError("word contains unknown action")
        relation = weighted[action]
        nxt = {state: 0 for state in order}
        for (left, target), edge_weight in relation.items():
            nxt[target] += current[left] * edge_weight
        if modulus is not None:
            nxt = {state: value % modulus for state, value in nxt.items()}
        current = nxt
    return current


def weighted_word_observation_trace(
    states: Sequence[State],
    family: WeightedFamily,
    observation: Callable[[State], Observation],
    source: State,
    word: Sequence[Action],
    *,
    modulus: int | None = None,
) -> dict[Observation, int]:
    values = weighted_word_state_values(states, family, source, word, modulus=modulus)
    result: dict[Observation, int] = {}
    for state, value in values.items():
        label = observation(state)
        result[label] = result.get(label, 0) + value
        if modulus is not None:
            result[label] %= modulus
    return result


def matrix_word_apply(
    matrices: Mapping[Action, Matrix],
    source_index: int,
    word: Sequence[Action],
) -> tuple[int, ...]:
    if not matrices:
        raise ValueError("matrix family must be nonempty")
    size = len(next(iter(matrices.values())))
    if not 0 <= source_index < size:
        raise ValueError("source_index outside quotient state set")
    current = tuple(int(index == source_index) for index in range(size))
    for action in word:
        if action not in matrices:
            raise ValueError("word contains unknown action")
        matrix = matrices[action]
        if len(matrix) != size or any(len(row) != size for row in matrix):
            raise ValueError("quotient action matrix dimension mismatch")
        current = tuple(
            sum(matrix[target][source] * current[source] for source in range(size))
            for target in range(size)
        )
    return current


def quotient_word_trace_matches_raw(
    states: Sequence[State],
    family: WeightedFamily,
    observation: Callable[[State], Observation],
    stable_partition: Sequence[Sequence[State] | frozenset[State]],
    source: State,
    word: Sequence[Action],
) -> bool:
    order = _states(states)
    partition = normalize_partition(stable_partition)
    if source not in _partition_states(partition):
        raise ValueError("source outside stable partition")
    matrices = exact_weighted_quotient_matrices(partition, family)
    source_block = next(index for index, block in enumerate(partition) if source in block)
    quotient_values = matrix_word_apply(matrices, source_block, word)

    quotient_trace: dict[Observation, int] = {}
    for index, block in enumerate(partition):
        labels = {observation(state) for state in block}
        if len(labels) != 1:
            raise ValueError("stable partition must refine observation for trace comparison")
        label = next(iter(labels))
        quotient_trace[label] = quotient_trace.get(label, 0) + quotient_values[index]

    raw = weighted_word_observation_trace(order, family, observation, source, word)
    all_labels = set(raw) | set(quotient_trace)
    if any(raw.get(label, 0) != quotient_trace.get(label, 0) for label in all_labels):
        raise AssertionError("exact weighted quotient failed raw word trace factorization")
    return True


@dataclass(frozen=True)
class BoundedLocalLawReflectionReport:
    local_aggregate_alphabet: frozenset[int]
    alphabet_minimum: int
    alphabet_maximum: int
    guaranteed_width_modulus: int
    minimal_reflective_modulus: int
    tested_modulus: int
    exact_partition: Partition
    modular_partition: Partition
    complete_sequences_equal: bool
    exact_quotient_matrices: dict[Action, Matrix]
    reconstructed_quotient_matrices: dict[Action, Matrix]


def bounded_local_law_reflection_report(
    states: Sequence[State],
    family: WeightedFamily,
    observation: Callable[[State], Observation],
    modulus: int | None = None,
) -> BoundedLocalLawReflectionReport:
    order = _states(states)
    weighted = _weighted_family(order, family)
    alphabet = weighted_local_aggregate_alphabet(order, weighted)
    minimum = min(alphabet)
    maximum = max(alphabet)
    guaranteed = guaranteed_reflective_modulus_from_width(alphabet)
    minimal = minimal_reflective_modulus(alphabet)
    tested = minimal if modulus is None else modulus
    if not modulus_is_injective_on_values(alphabet, tested):
        raise ValueError("tested modulus does not reflect local aggregate alphabet")
    initial = partition_from_observation(order, observation)
    exact_steps = weighted_refinement_sequence(initial, weighted)
    modular_steps = weighted_refinement_sequence(initial, weighted, modulus=tested)
    if exact_steps != modular_steps:
        raise AssertionError("reflective local modulus changed weighted state refinement")
    final = exact_steps[-1]
    exact_matrices = exact_weighted_quotient_matrices(final, weighted)
    reconstructed = reconstruct_exact_quotient_from_modular_local_law(
        final, weighted, tested
    )
    if exact_matrices != reconstructed:
        raise AssertionError("modular local-law reconstruction changed exact weighted machine")
    return BoundedLocalLawReflectionReport(
        local_aggregate_alphabet=alphabet,
        alphabet_minimum=minimum,
        alphabet_maximum=maximum,
        guaranteed_width_modulus=guaranteed,
        minimal_reflective_modulus=minimal,
        tested_modulus=tested,
        exact_partition=final,
        modular_partition=modular_steps[-1],
        complete_sequences_equal=exact_steps == modular_steps,
        exact_quotient_matrices=exact_matrices,
        reconstructed_quotient_matrices=reconstructed,
    )


def primitive_collision_modulus(
    primitive_weights: Sequence[int],
    max_terms: int,
    modulus: int,
) -> tuple[int, int, tuple[int, ...], tuple[int, ...]] | None:
    witness = bounded_primitive_sumset_witnesses(primitive_weights, max_terms)
    by_residue: dict[int, int] = {}
    for value in sorted(witness):
        residue = value % modulus
        if residue in by_residue and by_residue[residue] != value:
            other = by_residue[residue]
            return other, value, witness[other], witness[value]
        by_residue[residue] = value
    return None


def primitive_collision_fixture(
    primitive_weights: Sequence[int],
    max_terms: int,
    modulus: int,
) -> tuple[
    tuple[str, ...],
    dict[str, dict[tuple[str, str], int]],
    Callable[[str], str],
    tuple[int, int],
]:
    """Build a one-step world witnessing failure when the local code collides."""
    collision = primitive_collision_modulus(primitive_weights, max_terms, modulus)
    if collision is None:
        raise ValueError("modulus is injective on the bounded primitive sumset")
    left_value, right_value, left_terms, right_terms = collision
    target_count = max(len(left_terms), len(right_terms), 1)
    left_targets = tuple(f"l{index}" for index in range(target_count))
    right_targets = tuple(f"r{index}" for index in range(target_count))
    states = ("x", "y", *left_targets, *right_targets)
    edges: dict[tuple[str, str], int] = {}
    for index, weight in enumerate(left_terms):
        edges[("x", left_targets[index])] = weight
    for index, weight in enumerate(right_terms):
        edges[("y", right_targets[index])] = weight

    def observation(_state: str) -> str:
        return "visible"

    return states, {"a": edges}, observation, (left_value, right_value)


def primitive_weighted_chain_collision_fixture() -> tuple[
    tuple[str, ...],
    dict[str, dict[tuple[str, str], int]],
    Callable[[str], str],
]:
    """Local mod3 reflection is exact, but two-step derived values 4 and1 collide."""
    states = ("p", "q", "r", "s", "z")
    family = {
        "a": {
            ("p", "r"): 2,
            ("q", "s"): 1,
        },
        "b": {
            ("r", "z"): 2,
            ("s", "z"): 1,
        },
    }

    def observation(state: str) -> str:
        return "terminal" if state == "z" else "nonterminal"

    return states, family, observation
