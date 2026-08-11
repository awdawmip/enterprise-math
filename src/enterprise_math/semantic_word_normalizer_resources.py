"""Internal storage/depth Pareto for finite semantic word normalizers.

Once literal words have been quotiented to a finite transformation monoid of size
m, normalization itself still admits multiple exact representations.

1. Sequential right-generator automaton
   Store m*k transitions ``effect_id --generator--> effect_id``.  Normalize a
   length-h word sequentially in h generator-update rounds.

2. Full Cayley table
   Store m^2 arbitrary effect products.  Associativity permits balanced parallel
   normalization in ceil(log2 h) multiplication rounds.

3. Full literal word index through horizon H
   Store S(k,H) word->effect IDs.  One whole-word lookup returns the effect.

All three can share one semantic effect action table of m*n state cells, so their
auxiliary normalization-storage comparison is exactly

    m*k  vs  m^2  vs  S(k,H).

The first horizon where a Cayley table uses fewer auxiliary cells than the full
literal index is the least H with

    S(k,H) > m^2.

This phase transition is finite for every k>=1,m>=1 and is horizon-independent
on the semantic side.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Mapping, Sequence

from .future_word_cache_pareto import literal_word_count
from .semantic_word_normalizer import (
    TransformationMonoid,
    generated_transformation_monoid,
    parallel_normalization_depth,
)


State = Hashable
Action = Hashable


def right_generator_transition_table(
    monoid: TransformationMonoid,
) -> tuple[tuple[int, ...], ...]:
    names = monoid.action_names
    return tuple(
        tuple(
            monoid.multiplication_table[effect_id][monoid.generator_ids[action]]
            for action in names
        )
        for effect_id in range(monoid.size)
    )


def sequential_effect_automaton_storage_cells(monoid_size: int, action_count: int) -> int:
    for name, value in (("monoid_size", monoid_size), ("action_count", action_count)):
        if isinstance(value, bool) or not isinstance(value, int) or value < 1:
            raise ValueError(f"{name} must be a positive integer")
    return monoid_size * action_count


def cayley_storage_cells(monoid_size: int) -> int:
    if isinstance(monoid_size, bool) or not isinstance(monoid_size, int) or monoid_size < 1:
        raise ValueError("monoid_size must be a positive integer")
    return monoid_size * monoid_size


def first_horizon_cayley_smaller_than_literal_index(
    action_count: int,
    monoid_size: int,
) -> int:
    for name, value in (("action_count", action_count), ("monoid_size", monoid_size)):
        if isinstance(value, bool) or not isinstance(value, int) or value < 1:
            raise ValueError(f"{name} must be a positive integer")
    cayley = cayley_storage_cells(monoid_size)
    horizon = 1
    while literal_word_count(action_count, horizon) <= cayley:
        horizon += 1
    return horizon


@dataclass(frozen=True)
class SemanticNormalizerResourcePoint:
    name: str
    auxiliary_storage_cells: int
    normalization_depth: int
    state_apply_depth: int

    @property
    def total_depth(self) -> int:
        return self.normalization_depth + self.state_apply_depth


@dataclass(frozen=True)
class SemanticNormalizerResourceReport:
    state_count: int
    action_count: int
    monoid_size: int
    horizon: int
    shared_effect_action_cells: int
    sequential_automaton: SemanticNormalizerResourcePoint
    cayley_parallel: SemanticNormalizerResourcePoint
    literal_index: SemanticNormalizerResourcePoint
    first_cayley_break_even_horizon: int


def semantic_normalizer_resource_report(
    states: Sequence[State],
    operations: Mapping[Action, Mapping[State, State]],
    horizon: int,
) -> SemanticNormalizerResourceReport:
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 1:
        raise ValueError("horizon must be positive")
    monoid = generated_transformation_monoid(states, operations)
    n = len(monoid.states)
    k = len(monoid.action_names)
    m = monoid.size
    shared = m * n
    return SemanticNormalizerResourceReport(
        state_count=n,
        action_count=k,
        monoid_size=m,
        horizon=horizon,
        shared_effect_action_cells=shared,
        sequential_automaton=SemanticNormalizerResourcePoint(
            name="right-generator-automaton",
            auxiliary_storage_cells=sequential_effect_automaton_storage_cells(m, k),
            normalization_depth=horizon,
            state_apply_depth=1,
        ),
        cayley_parallel=SemanticNormalizerResourcePoint(
            name="full-cayley-parallel",
            auxiliary_storage_cells=cayley_storage_cells(m),
            normalization_depth=parallel_normalization_depth(horizon),
            state_apply_depth=1,
        ),
        literal_index=SemanticNormalizerResourcePoint(
            name="full-literal-index",
            auxiliary_storage_cells=literal_word_count(k, horizon),
            normalization_depth=0,
            state_apply_depth=1,
        ),
        first_cayley_break_even_horizon=first_horizon_cayley_smaller_than_literal_index(k, m),
    )
