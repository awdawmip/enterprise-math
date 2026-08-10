"""Independent path-count oracle for exact count-stable weighted quotients.

A count-stable relation partition defines one weighted quotient matrix per action.
This module executes literal words on those quotient matrices and compares the
resulting observed natural path counts with direct raw relation execution.

The oracle is intentionally separate from the rational trace-closure compiler:
it validates the semantic factorization before any row-space compression is
applied.
"""

from __future__ import annotations

from typing import Callable, Hashable, Mapping, Sequence

from .admissible_support import Relation
from .relation_branching_semiring import natural_semiring, raw_semiring_word_trace
from .relation_structure_first_trace_compiler import (
    Matrix,
    exact_count_branching_partition,
    exact_weighted_quotient_matrices,
    observation_labels_for_blocks,
)


State = Hashable
Action = Hashable
Observation = Hashable


def weighted_quotient_word_trace(
    partition,
    quotient_matrices: Mapping[Action, Matrix],
    observation: Callable[[State], Observation],
    source: State,
    word: Sequence[Action],
) -> dict[Observation, int]:
    blocks = tuple(partition)
    block_of = {
        state: index
        for index, block in enumerate(blocks)
        for state in block
    }
    if source not in block_of:
        raise ValueError("source lies outside quotient partition")
    labels = observation_labels_for_blocks(partition, observation)
    dimension = len(blocks)
    vector = [0 for _ in range(dimension)]
    vector[block_of[source]] = 1

    for action in word:
        if action not in quotient_matrices:
            raise ValueError("word contains action outside quotient matrix family")
        matrix = quotient_matrices[action]
        if len(matrix) != dimension or any(len(row) != dimension for row in matrix):
            raise ValueError("quotient matrix dimension mismatch")
        nxt = [0 for _ in range(dimension)]
        for target in range(dimension):
            nxt[target] = sum(
                matrix[target][current] * vector[current]
                for current in range(dimension)
            )
        vector = nxt

    observed: dict[Observation, int] = {}
    for block_index, count in enumerate(vector):
        if count:
            label = labels[block_index]
            observed[label] = observed.get(label, 0) + count
    return observed


def raw_and_weighted_quotient_traces_agree(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    source: State,
    word: Sequence[Action],
) -> bool:
    partition = exact_count_branching_partition(states, relations, observation)
    matrices = exact_weighted_quotient_matrices(states, relations, partition)
    weighted = weighted_quotient_word_trace(
        partition,
        matrices,
        observation,
        source,
        word,
    )
    raw = raw_semiring_word_trace(
        states,
        relations,
        observation,
        source,
        word,
        natural_semiring(),
    )
    normalized_raw = {label: int(count) for label, count in raw.items()}
    if weighted != normalized_raw:
        raise AssertionError("weighted quotient failed exact raw path-count trace factorization")
    return True
