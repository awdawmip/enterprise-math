"""Pair relation refinement by explicit intermediate primitive witnesses.

For a primitive-direction graph, an ordered pair (u,v) begins with only a small
causal relation label: equality, antipode, primitive adjacency, adjacency to the
antipode, or other.  One refinement round asks how the pair can factor through
*every* intermediate primitive witness z, retaining the multiplicity of typed
compositions

    (type(u,z), type(z,v)).

Pairs are equivalent only when these complete witness-composition profiles agree.
Iterating to stability gives the coarsest pair quotient closed under this witness
language.  At stability, for every three stable types a,b,c, the number

    p[a,b|c] = #{z : type(x,z)=a and type(z,y)=b}

is independent of the representative pair (x,y) of type c.  Thus the stable
causal pair types carry an exact finite integer witness-composition algebra.

This is closely related to coherent configurations / 2-dimensional
Weisfeiler-Leman refinement; those are prior-art computational languages.  The
project interpretation is the P021-style future-safe closure of a pair relation
under all one-witness insertions.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import Hashable

from .causal_primitive_link_profile import Adjacency, Vector

Pair = tuple[Vector, Vector]
PairColors = dict[Pair, int]
IntersectionNumbers = dict[tuple[int, int, int], int]


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


def _validate_colors(adjacency: Adjacency, colors: PairColors) -> None:
    vertices = tuple(adjacency)
    expected = {(left, right) for left in vertices for right in vertices}
    if set(colors) != expected:
        raise ValueError("colors must cover every ordered primitive pair")


def pair_refine_once(adjacency: Adjacency, colors: PairColors) -> PairColors:
    _validate_colors(adjacency, colors)
    vertices = tuple(adjacency)
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


def stable_pair_colors(
    adjacency: Adjacency,
    maximum_rounds: int | None = None,
) -> PairColors:
    """Return the stable witness-composition pair quotient.

    Finite termination is guaranteed because each strict round refines a finite
    set of |V|^2 ordered pairs.  `maximum_rounds` is an optional audit guard.
    """
    current = initial_pair_colors(adjacency)
    rounds = 0
    while True:
        refined = pair_refine_once(adjacency, current)
        if same_pair_partition(current, refined):
            return current
        current = refined
        rounds += 1
        if maximum_rounds is not None and rounds >= maximum_rounds:
            raise RuntimeError("pair refinement did not stabilize within maximum_rounds")


def pair_color_count(colors: PairColors) -> int:
    return len(set(colors.values()))


def stable_intersection_numbers(
    adjacency: Adjacency,
    colors: PairColors | None = None,
) -> IntersectionNumbers:
    """Exact witness-composition constants of a stable pair quotient.

    Raises if the supplied colors are not stable or if one color has inconsistent
    witness counts across representatives.
    """
    stable = stable_pair_colors(adjacency) if colors is None else colors
    _validate_colors(adjacency, stable)
    refined = pair_refine_once(adjacency, stable)
    if not same_pair_partition(stable, refined):
        raise ValueError("intersection numbers require a stable pair partition")

    vertices = tuple(adjacency)
    by_color: dict[int, list[Pair]] = defaultdict(list)
    for pair, color in stable.items():
        by_color[color].append(pair)

    constants: IntersectionNumbers = {}
    for color_c, pairs in by_color.items():
        reference_profile = None
        for left, right in pairs:
            profile = Counter(
                (stable[(left, middle)], stable[(middle, right)])
                for middle in vertices
            )
            if reference_profile is None:
                reference_profile = profile
            elif profile != reference_profile:
                raise AssertionError("stable color has representative-dependent witness profile")
        assert reference_profile is not None
        for (color_a, color_b), multiplicity in reference_profile.items():
            constants[(color_a, color_b, color_c)] = multiplicity
    return constants


def stable_pair_algebra_is_well_defined(adjacency: Adjacency) -> bool:
    colors = stable_pair_colors(adjacency)
    try:
        stable_intersection_numbers(adjacency, colors)
    except (ValueError, AssertionError):
        return False
    return True


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
