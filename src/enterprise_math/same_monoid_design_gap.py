"""Same execution monoid, different minimum precision-preserving generator design.

For universe size m>=2 compare two Set-Cover action catalogues with m+1 named
generators.

Catalogue A:
    every singleton {i}, plus one duplicate singleton {0}.

Catalogue B:
    every singleton {i}, plus the full universe.

Both catalogues generate exactly the same semantic effect monoid: every subset
of the universe is reachable as a union of singleton masks, so the monoid is the
full Boolean semilattice 2^[m] under OR.  Both have the same number of named
generators and the same formulaic execution law.

Yet minimum full-precision preserving subset sizes differ maximally:

    A needs all m singleton directions;
    B needs only the full-universe generator.

Thus even the complete generated operation monoid plus action-count metadata does
not determine minimum capability-basis size.  Generator presentation relative
to the semantic target remains an independent design resource.
"""

from __future__ import annotations

from dataclasses import dataclass

from .set_cover_formulaic_execution import (
    distinct_word_effect_masks,
    minimum_cover_size_exact,
)


def duplicate_singleton_catalogue(universe_size: int) -> tuple[frozenset[int], ...]:
    if isinstance(universe_size, bool) or not isinstance(universe_size, int) or universe_size < 2:
        raise ValueError("universe_size must be an integer at least two")
    singletons = tuple(frozenset({element}) for element in range(universe_size))
    return (*singletons, frozenset({0}))


def full_action_catalogue(universe_size: int) -> tuple[frozenset[int], ...]:
    if isinstance(universe_size, bool) or not isinstance(universe_size, int) or universe_size < 2:
        raise ValueError("universe_size must be an integer at least two")
    singletons = tuple(frozenset({element}) for element in range(universe_size))
    return (*singletons, frozenset(range(universe_size)))


@dataclass(frozen=True)
class SameMonoidDesignGapReport:
    universe_size: int
    action_count: int
    semantic_effect_count: int
    duplicate_catalogue_minimum: int
    full_action_catalogue_minimum: int
    minimum_basis_gap: int


def same_monoid_design_gap_report(universe_size: int) -> SameMonoidDesignGapReport:
    left = duplicate_singleton_catalogue(universe_size)
    right = full_action_catalogue(universe_size)
    left_effects = distinct_word_effect_masks(universe_size, left)
    right_effects = distinct_word_effect_masks(universe_size, right)
    if left_effects != right_effects:
        raise AssertionError("catalogues failed same generated effect-monoid witness")
    expected_effects = 1 << universe_size
    if len(left_effects) != expected_effects:
        raise AssertionError("singleton generators failed full powerset monoid")
    left_min = minimum_cover_size_exact(universe_size, left)
    right_min = minimum_cover_size_exact(universe_size, right)
    if left_min != universe_size:
        raise AssertionError("duplicate-singleton catalogue had unexpected minimum cover")
    if right_min != 1:
        raise AssertionError("full-action catalogue had unexpected minimum cover")
    return SameMonoidDesignGapReport(
        universe_size=universe_size,
        action_count=universe_size + 1,
        semantic_effect_count=expected_effects,
        duplicate_catalogue_minimum=left_min,
        full_action_catalogue_minimum=right_min,
        minimum_basis_gap=left_min - right_min,
    )
