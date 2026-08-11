"""Formulaic execution for the arbitrary monotone capability compiler.

The parent universality theorem realizes every finite nonempty upward-closed
preserving family P on k actions through a Set-Cover construction built from the
inclusion-maximal false subsets F_i.

For each action a define a t-bit mask over those maximal false subsets:

    mask(a)_i = 1  iff  a notin F_i.

This is exactly the Set-Cover incidence used by the compiled 0/1 action matrix.
Consequently every literal word effect is determined by bitwise OR of its action
masks.  The full precision-preservation predicate can be an arbitrary monotone
set system, while the execution algebra of the same compiled actions remains a
commuting-idempotent semilattice with formulaic OR composition.

Thus generic design-selection geometry and operation-execution algebra
complexity are orthogonal: an easy exact executor does not imply matroid,
submodular, unique-basis, or polynomial minimum-design structure.

Monotone Boolean functions, Set Cover encodings and semilattice actions are
standard prior mathematics/CS.  This module only makes the cross-owner resource
separation executable.
"""

from __future__ import annotations

from itertools import product
from typing import Sequence

from .integer_action_capability_monotone_universality import (
    MonotoneCapabilityCompilation,
    compile_monotone_capability_family,
)
from .set_cover_formulaic_execution import (
    activation_matrix_from_mask,
    matrix_product,
)


def monotone_compilation_action_masks(
    compilation: MonotoneCapabilityCompilation,
) -> tuple[int, ...]:
    if compilation.trivial_all_preserving:
        return tuple(0 for _ in range(compilation.action_count))
    false_sets = compilation.maximal_false_subsets
    return tuple(
        sum(
            (1 << false_index)
            for false_index, false_subset in enumerate(false_sets)
            if action not in false_subset
        )
        for action in range(compilation.action_count)
    )


def monotone_word_union_mask(
    compilation: MonotoneCapabilityCompilation,
    word: Sequence[int],
) -> int:
    masks = monotone_compilation_action_masks(compilation)
    result = 0
    for action in word:
        if isinstance(action, bool) or not isinstance(action, int):
            raise TypeError("action index must be an integer")
        if not 0 <= action < compilation.action_count:
            raise ValueError("action index outside compiled family")
        result |= masks[action]
    return result


def monotone_literal_word_matrix(
    compilation: MonotoneCapabilityCompilation,
    word: Sequence[int],
):
    if compilation.trivial_all_preserving:
        return ((1,),)
    dimension = len(compilation.action_matrices[0])
    identity = tuple(
        tuple(int(row == column) for column in range(dimension))
        for row in range(dimension)
    )
    result = identity
    for action in word:
        if isinstance(action, bool) or not isinstance(action, int):
            raise TypeError("action index must be an integer")
        if not 0 <= action < compilation.action_count:
            raise ValueError("action index outside compiled family")
        result = matrix_product(result, compilation.action_matrices[action])
    return result


def monotone_formulaic_word_matrix(
    compilation: MonotoneCapabilityCompilation,
    word: Sequence[int],
):
    if compilation.trivial_all_preserving:
        return ((1,),)
    universe_size = len(compilation.maximal_false_subsets)
    mask = monotone_word_union_mask(compilation, word)
    return activation_matrix_from_mask(universe_size, mask)


def monotone_formulaic_execution_matches_literal(
    compilation: MonotoneCapabilityCompilation,
    word: Sequence[int],
) -> bool:
    formulaic = monotone_formulaic_word_matrix(compilation, word)
    literal = monotone_literal_word_matrix(compilation, word)
    if formulaic != literal:
        raise AssertionError("monotone-universality OR normal form disagreed with literal matrices")
    return True


def preserving_subset_mask_covers_all_false_witnesses(
    compilation: MonotoneCapabilityCompilation,
    selected_actions: Sequence[int],
) -> bool:
    if compilation.trivial_all_preserving:
        return True
    union = monotone_word_union_mask(compilation, selected_actions)
    full = (1 << len(compilation.maximal_false_subsets)) - 1
    return union == full


def preserving_subset_matches_formulaic_cover(
    compilation: MonotoneCapabilityCompilation,
    selected_actions: Sequence[int],
) -> bool:
    subset = frozenset(selected_actions)
    if any(
        isinstance(action, bool)
        or not isinstance(action, int)
        or not 0 <= action < compilation.action_count
        for action in subset
    ):
        raise ValueError("selected action outside compiled family")
    expected = subset in compilation.preserving_family
    actual = preserving_subset_mask_covers_all_false_witnesses(
        compilation,
        tuple(sorted(subset)),
    )
    if actual != expected:
        raise AssertionError("formulaic full-mask criterion disagreed with monotone preserving family")
    return expected


def compile_and_verify_formulaic_monotone_family(
    action_count: int,
    preserving_subsets,
    max_word_length: int,
) -> MonotoneCapabilityCompilation:
    if isinstance(max_word_length, bool) or not isinstance(max_word_length, int) or max_word_length < 0:
        raise ValueError("max_word_length must be nonnegative")
    compilation = compile_monotone_capability_family(action_count, preserving_subsets)
    actions = tuple(range(action_count))
    for length in range(max_word_length + 1):
        for word in product(actions, repeat=length):
            monotone_formulaic_execution_matches_literal(compilation, word)
    return compilation
