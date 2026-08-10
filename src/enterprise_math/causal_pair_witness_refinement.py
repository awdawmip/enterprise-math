"""Pair relation refinement by explicit intermediate primitive witnesses.

For a primitive-direction graph, an ordered pair (u,v) begins with only a small
causal relation label: equality, antipode, primitive adjacency, adjacency to the
antipode, or other.  One refinement round asks how the pair can factor through
*every* intermediate primitive witness z, retaining the multiplicity of typed
compositions

    (type(u,z), type(z,v)).

Pairs are equivalent only when these complete witness-composition profiles agree.
Iterating to stability gives a finite pair-context quotient.  This is closely
related to coherent configurations / 2-dimensional Weisfeiler-Leman refinement;
those are prior-art computational languages.  The project interpretation is the
P021-style future-safe refinement of a pair relation under all one-witness
insertions.
"""

from __future__ import annotations

from collections import Counter
from typing import Hashable

from .causal_primitive_link_profile import Adjacency, Vector

Pair = tuple[Vector, Vector]
PairColors = dict[Pair, int]


def negate(vector: Vector) -> Vector:
    return tuple(-value for value in vector)


def initial_pair_label(adjacency: Adjacency, left: Vector, right: Vector) -> str:
    if left == right:
        return "same"
    if left == negate(right):
        return "antipode"
    if right in adjacency[left]:
        return "+adj"
    anti = negate(right)
    if anti in adjacency[left]:
        return "-adj"
    return "other"


def _canonicalize(signatures: dict[Pair, Hashable]) -> PairColors:
    ids: dict[Hashable, int] = {}
    result: PairColors = {}
    for pair, signature in signatures.items():
        if signature not in ids:
            ids[signature] = len(ids)
        result[pair] = ids[signature]
    return result


def initial_pair_colors(adjacency: Adjacency) -> PairColors:
    signatures = {
        (left, right): initial_pair_label(adjacency, left, right)
        for left in adjacency
        for right in adjacency
    }
    return _canonicalize(signatures)


def pair_refine_once(adjacency: Adjacency, colors: PairColors) -> PairColors:
    vertices = tuple(adjacency)
    expected = {(left, right) for left in vertices for right in vertices}
    if set(colors) != expected:
        raise ValueError("colors must cover every ordered primitive pair")

    signatures = {}
    for left in vertices:
        for right in vertices:
            witness_profile = Counter(
                (colors[(left, middle)], colors[(middle, right)])
                for middle in vertices
            )
            signatures[(left, right)] = (
                colors[(left, right)],
                tuple(sorted(witness_profile.items())),
            )
    return _canonicalize(signatures)


def same_pair_partition(left: PairColors, right: PairColors) -> bool:
    if set(left) != set(right):
        return False
    pairs = tuple(left)
    return all(
        (left[a] == left[b]) == (right[a] == right[b])
        for a in pairs
        for b in pairs
    )


def pair_refinement_sequence(
    adjacency: Adjacency,
    maximum_rounds: int,
) -> tuple[PairColors, ...]:
    if (
        isinstance(maximum_rounds, bool)
        or not isinstance(maximum_rounds, int)
        or maximum_rounds < 0
    ):
        raise ValueError("maximum_rounds must be a non-negative integer")
    current = initial_pair_colors(adjacency)
    result = [current]
    for _ in range(maximum_rounds):
        refined = pair_refine_once(adjacency, current)
        result.append(refined)
        if same_pair_partition(current, refined):
            break
        current = refined
    return tuple(result)


def pair_color_count(colors: PairColors) -> int:
    return len(set(colors.values()))


def observation_factors_through_pair_colors(
    colors: PairColors,
    observation,
) -> bool:
    value_by_color = {}
    for pair, color in colors.items():
        value = observation(*pair)
        if color in value_by_color and value_by_color[color] != value:
            return False
        value_by_color[color] = value
    return True


def minimum_pair_refinement_round_for_observation(
    adjacency: Adjacency,
    observation,
    maximum_rounds: int,
) -> int | None:
    sequence = pair_refinement_sequence(adjacency, maximum_rounds)
    for round_index, colors in enumerate(sequence):
        if observation_factors_through_pair_colors(colors, observation):
            return round_index
    return None
