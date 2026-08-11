"""Uniform versus target-specific storage for bounded-support semantic shortcuts.

In the Boolean OR effect algebra, the canonical depth-d shortcut catalogue stores
all nonzero masks of Hamming weight at most d.

This catalogue is **minimum**, not merely sufficient, for the uniform requirement:

every effect T with 1<=|T|<=d must be executable from identity in one primitive
shortcut application.

One-round execution from0 returns exactly the chosen primitive mask, so every
such T must itself be present.  Therefore minimum uniform catalogue size is

    sum_{i=1}^d C(k,i).

If the declared task only needs one target mask T, the required storage can be
far smaller.  Partition T's support into chunks of size at most d and store only
those chunk masks.  This uses ceil(|T|/d) target-specific primitives and reaches T
in the same number of rounds, but it does not preserve the uniform future-effect
language.

This is the shortcut analogue of fixed-target versus all-target precision:
resource minimality is relative to the declared target language.
"""

from __future__ import annotations

from .semantic_shortcut_generator_pareto import (
    decompose_target_into_shortcuts,
    semantic_shortcut_generator_count,
)


def minimum_uniform_one_round_catalogue_size(generator_count: int, shortcut_depth: int) -> int:
    return semantic_shortcut_generator_count(generator_count, shortcut_depth)


def target_specific_shortcut_catalogue(
    target_mask: int,
    generator_count: int,
    shortcut_depth: int,
) -> tuple[int, ...]:
    return decompose_target_into_shortcuts(target_mask, generator_count, shortcut_depth)


def target_specific_catalogue_size(
    target_mask: int,
    generator_count: int,
    shortcut_depth: int,
) -> int:
    return len(target_specific_shortcut_catalogue(target_mask, generator_count, shortcut_depth))


def uniform_catalogue_is_strictly_larger_for_full_target(
    generator_count: int,
    shortcut_depth: int,
) -> bool:
    full = (1 << generator_count) - 1
    uniform = minimum_uniform_one_round_catalogue_size(generator_count, shortcut_depth)
    target = target_specific_catalogue_size(full, generator_count, shortcut_depth)
    return uniform > target
