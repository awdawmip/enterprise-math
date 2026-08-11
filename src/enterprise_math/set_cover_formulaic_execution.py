"""Formulaic execution algebra for the Set-Cover action-capability compiler.

The parent precision-selection generation compiles a Set Cover instance into
pairwise commuting idempotent 0/1 action matrices.  Minimum precision-preserving
action selection is exactly Minimum Set Cover.

The very same compiled family has an extremely simple **execution** algebra.
For a universe element j, action a maps source coordinate e_j to future coordinate
f_j iff candidate set S_a contains j; once f_j is reached it remains fixed.
Therefore composing any action word depends only on the union of the candidate
sets occurring in the word.

Represent that union by an m-bit mask U(w).  Then

    U(empty)=0,
    U(uv)=U(u) OR U(v),

and the exact matrix effect of w is the canonical activation matrix associated
with U(w).  Repetition and order are irrelevant.

Hence word execution/normalization is formulaic and admits balanced OR depth
ceil(log2 h), while selecting a minimum generator subset preserving the full
future precision remains exactly Set Cover.

This gives one family in which **execution algebra complexity** and **design-
selection complexity** are provably orthogonal.  Set Cover, commuting
idempotents and semilattice normal forms are standard prior mathematics/CS.  The
project value is the explicit precision-resource separation.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Iterable, Sequence

from .integer_action_capability_set_cover import (
    Matrix,
    selected_sets_cover_universe,
    set_cover_action_matrices,
    verify_set_cover_capability_equivalence,
)


def _universe_size(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("universe_size must be a positive integer")
    return value


def _sets(
    universe_size: int,
    sets: Sequence[Iterable[int]],
) -> tuple[frozenset[int], ...]:
    size = _universe_size(universe_size)
    result = tuple(frozenset(values) for values in sets)
    if not result:
        raise ValueError("at least one candidate set/action is required")
    for subset in result:
        if any(
            isinstance(element, bool)
            or not isinstance(element, int)
            or not 0 <= element < size
            for element in subset
        ):
            raise ValueError("candidate set element outside universe")
    return result


def set_mask(subset: Iterable[int], universe_size: int) -> int:
    size = _universe_size(universe_size)
    mask = 0
    for element in subset:
        if isinstance(element, bool) or not isinstance(element, int) or not 0 <= element < size:
            raise ValueError("set element outside universe")
        mask |= 1 << element
    return mask


def action_masks(
    universe_size: int,
    sets: Sequence[Iterable[int]],
) -> tuple[int, ...]:
    cover_sets = _sets(universe_size, sets)
    return tuple(set_mask(subset, universe_size) for subset in cover_sets)


def word_union_mask(
    universe_size: int,
    sets: Sequence[Iterable[int]],
    word: Sequence[int],
) -> int:
    masks = action_masks(universe_size, sets)
    result = 0
    for action_index in word:
        if isinstance(action_index, bool) or not isinstance(action_index, int):
            raise TypeError("action index must be an integer")
        if not 0 <= action_index < len(masks):
            raise ValueError("action index outside family")
        result |= masks[action_index]
    return result


def multiply_union_masks(left: int, right: int, universe_size: int) -> int:
    size = _universe_size(universe_size)
    limit = 1 << size
    for name, value in (("left", left), ("right", right)):
        if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value < limit:
            raise ValueError(f"{name} mask outside universe")
    return left | right


def activation_matrix_from_mask(universe_size: int, mask: int) -> Matrix:
    size = _universe_size(universe_size)
    if isinstance(mask, bool) or not isinstance(mask, int) or not 0 <= mask < (1 << size):
        raise ValueError("mask outside universe")
    dimension = 2 * size
    rows = [[0] * dimension for _ in range(dimension)]
    for element in range(size):
        source = element
        target = size + element
        if mask & (1 << element):
            rows[source][target] = 1
        else:
            rows[source][source] = 1
        rows[target][target] = 1
    return tuple(tuple(row) for row in rows)


def matrix_product(left: Matrix, right: Matrix) -> Matrix:
    if not left or len(left) != len(right):
        raise ValueError("matrices must share one positive square dimension")
    dimension = len(left)
    if any(len(row) != dimension for row in left + right):
        raise ValueError("matrices must be square")
    return tuple(
        tuple(
            sum(left[row][inner] * right[inner][column] for inner in range(dimension))
            for column in range(dimension)
        )
        for row in range(dimension)
    )


def literal_word_matrix(
    universe_size: int,
    sets: Sequence[Iterable[int]],
    word: Sequence[int],
) -> Matrix:
    size = _universe_size(universe_size)
    actions = set_cover_action_matrices(size, sets)
    identity = activation_matrix_from_mask(size, 0)
    result = identity
    for action_index in word:
        if isinstance(action_index, bool) or not isinstance(action_index, int):
            raise TypeError("action index must be an integer")
        if not 0 <= action_index < len(actions):
            raise ValueError("action index outside family")
        result = matrix_product(result, actions[action_index])
    return result


def formulaic_word_matrix_matches_literal(
    universe_size: int,
    sets: Sequence[Iterable[int]],
    word: Sequence[int],
) -> bool:
    mask = word_union_mask(universe_size, sets, word)
    formulaic = activation_matrix_from_mask(universe_size, mask)
    literal = literal_word_matrix(universe_size, sets, word)
    if formulaic != literal:
        raise AssertionError("union-mask normal form disagreed with compiled action word")
    return True


def parallel_union_normalization_depth(word_length: int) -> int:
    if isinstance(word_length, bool) or not isinstance(word_length, int) or word_length < 0:
        raise ValueError("word_length must be nonnegative")
    if word_length <= 1:
        return 0
    return (word_length - 1).bit_length()


def parallel_word_union_mask(
    universe_size: int,
    sets: Sequence[Iterable[int]],
    word: Sequence[int],
) -> tuple[int, int]:
    masks = action_masks(universe_size, sets)
    layer = []
    for action_index in word:
        if isinstance(action_index, bool) or not isinstance(action_index, int):
            raise TypeError("action index must be an integer")
        if not 0 <= action_index < len(masks):
            raise ValueError("action index outside family")
        layer.append(masks[action_index])
    if not layer:
        return 0, 0
    depth = 0
    while len(layer) > 1:
        nxt = []
        index = 0
        while index < len(layer):
            if index + 1 == len(layer):
                nxt.append(layer[index])
                index += 1
            else:
                nxt.append(layer[index] | layer[index + 1])
                index += 2
        layer = nxt
        depth += 1
    expected = parallel_union_normalization_depth(len(word))
    if depth != expected:
        raise AssertionError("balanced union depth disagreed with ceil-log2 law")
    exact = word_union_mask(universe_size, sets, word)
    if layer[0] != exact:
        raise AssertionError("parallel union normalizer disagreed with exact union mask")
    return exact, depth


def distinct_word_effect_masks(
    universe_size: int,
    sets: Sequence[Iterable[int]],
) -> frozenset[int]:
    """All semantic operation effects from arbitrary words, via subset unions."""
    cover_sets = _sets(universe_size, sets)
    masks = action_masks(universe_size, cover_sets)
    effects = {0}
    for size in range(1, len(masks) + 1):
        for selected in combinations(range(len(masks)), size):
            union = 0
            for index in selected:
                union |= masks[index]
            effects.add(union)
    return frozenset(effects)


def minimum_cover_size_exact(
    universe_size: int,
    sets: Sequence[Iterable[int]],
) -> int | None:
    size = _universe_size(universe_size)
    cover_sets = _sets(size, sets)
    for selected_size in range(1, len(cover_sets) + 1):
        for selected in combinations(range(len(cover_sets)), selected_size):
            if selected_sets_cover_universe(size, cover_sets, selected):
                return selected_size
    return None


@dataclass(frozen=True)
class DesignExecutionSeparationReport:
    universe_size: int
    action_count: int
    semantic_effect_count: int
    full_union_mask: int
    full_family_preserves_precision: bool
    minimum_preserving_action_count: int | None
    word_normal_form_bits: int
    word_normalization_depth_at_horizon: int
    word_normalization_bit_work_at_horizon: int


def design_execution_separation_report(
    universe_size: int,
    sets: Sequence[Iterable[int]],
    horizon: int,
) -> DesignExecutionSeparationReport:
    size = _universe_size(universe_size)
    cover_sets = _sets(size, sets)
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 1:
        raise ValueError("horizon must be positive")
    full_indices = tuple(range(len(cover_sets)))
    full_cover = selected_sets_cover_universe(size, cover_sets, full_indices)
    if full_cover:
        verify_set_cover_capability_equivalence(size, cover_sets, full_indices)
    effects = distinct_word_effect_masks(size, cover_sets)
    full_mask = 0
    for mask in action_masks(size, cover_sets):
        full_mask |= mask
    return DesignExecutionSeparationReport(
        universe_size=size,
        action_count=len(cover_sets),
        semantic_effect_count=len(effects),
        full_union_mask=full_mask,
        full_family_preserves_precision=full_cover,
        minimum_preserving_action_count=(
            minimum_cover_size_exact(size, cover_sets) if full_cover else None
        ),
        word_normal_form_bits=size,
        word_normalization_depth_at_horizon=parallel_union_normalization_depth(horizon),
        word_normalization_bit_work_at_horizon=size * max(0, horizon - 1),
    )
