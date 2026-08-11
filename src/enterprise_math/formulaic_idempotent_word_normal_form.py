"""Formulaic exact word normal form for commuting idempotent generators.

Use k-bit mask states.  Generator i acts by

    x -> x OR (1<<i).

The generators commute and are idempotent.  Every literal word therefore has the
exact normal form

    nu(w) = bitwise OR of the generators appearing in w,

and the induced transformation is

    x -> x OR nu(w).

The generated transformation monoid has 2^k elements, one for every mask.  A
generic table representation would use 4^k Cayley cells and 4^k effect-action
cells because the state set also has 2^k elements.  Yet the exact algebra is
represented formulaically by k-bit masks and one OR law.

Balanced OR reduction normalizes a length-h word in ceil(log2 h) depth, matching
the generic full-Cayley parallel depth without storing the Cayley table.

This is a sharp witness that semantic monoid cardinality and operational
representation complexity are independent resources.  Large exact operation
sets can have compact compositional laws.

Semilattices, commuting idempotents and bitmask representations are standard
prior algebra/CS.  The Enterprise Math value is the explicit Stage131 formulaic-
versus-tabulated normal-form resource boundary.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb
from typing import Sequence

from .future_word_cache_pareto import literal_word_count
from .semantic_word_normalizer import (
    generated_transformation_monoid,
    parallel_normalization_depth,
    word_transformation,
)


def _generator_count(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("generator_count must be a positive integer")
    return value


def commuting_idempotent_mask_fixture(
    generator_count: int,
) -> tuple[tuple[int, ...], dict[int, dict[int, int]]]:
    k = _generator_count(generator_count)
    states = tuple(range(1 << k))
    operations = {
        generator: {
            state: state | (1 << generator)
            for state in states
        }
        for generator in range(k)
    }
    return states, operations


def word_mask_normal_form(
    word: Sequence[int],
    generator_count: int,
) -> int:
    k = _generator_count(generator_count)
    mask = 0
    for generator in word:
        if isinstance(generator, bool) or not isinstance(generator, int) or not 0 <= generator < k:
            raise ValueError("word contains generator outside declared range")
        mask |= 1 << generator
    return mask


def multiply_mask_normal_forms(left: int, right: int, generator_count: int) -> int:
    k = _generator_count(generator_count)
    limit = 1 << k
    for name, value in (("left", left), ("right", right)):
        if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value < limit:
            raise ValueError(f"{name} normal form outside mask range")
    return left | right


def apply_mask_effect(state: int, effect_mask: int, generator_count: int) -> int:
    k = _generator_count(generator_count)
    limit = 1 << k
    for name, value in (("state", state), ("effect_mask", effect_mask)):
        if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value < limit:
            raise ValueError(f"{name} outside mask state space")
    return state | effect_mask


def mask_normal_form_matches_literal(
    word: Sequence[int],
    generator_count: int,
) -> bool:
    states, operations = commuting_idempotent_mask_fixture(generator_count)
    normal = word_mask_normal_form(word, generator_count)
    direct = word_transformation(states, operations, word)
    expected = tuple(apply_mask_effect(state, normal, generator_count) for state in states)
    if direct != expected:
        raise AssertionError("formulaic mask normal form disagreed with literal word transformation")
    return True


def reachable_nonidentity_effect_count(
    generator_count: int,
    horizon: int,
) -> int:
    k = _generator_count(generator_count)
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 0:
        raise ValueError("horizon must be a nonnegative integer")
    maximum_support = min(k, horizon)
    return sum(comb(k, size) for size in range(1, maximum_support + 1))


def reachable_effect_count_including_identity(
    generator_count: int,
    horizon: int,
) -> int:
    return 1 + reachable_nonidentity_effect_count(generator_count, horizon)


def parallel_formulaic_normalization(
    word: Sequence[int],
    generator_count: int,
) -> tuple[int, int]:
    k = _generator_count(generator_count)
    masks = []
    for generator in word:
        if isinstance(generator, bool) or not isinstance(generator, int) or not 0 <= generator < k:
            raise ValueError("word contains generator outside declared range")
        masks.append(1 << generator)
    if not masks:
        return 0, 0
    depth = 0
    layer = masks
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
    expected_depth = parallel_normalization_depth(len(word))
    if depth != expected_depth:
        raise AssertionError("formulaic OR reduction depth disagreed with ceil-log2 law")
    exact = word_mask_normal_form(word, k)
    if layer[0] != exact:
        raise AssertionError("parallel formulaic reduction disagreed with exact mask normal form")
    return exact, depth


@dataclass(frozen=True)
class FormulaicNormalFormResourceReport:
    generator_count: int
    state_count: int
    monoid_size: int
    horizon: int
    generic_cayley_cells: int
    generic_effect_action_cells: int
    literal_word_entries: int
    formulaic_normal_form_bits: int
    formulaic_generator_metadata_entries: int
    formulaic_parallel_normalization_depth: int
    formulaic_state_apply_depth: int

    @property
    def formulaic_total_depth(self) -> int:
        return self.formulaic_parallel_normalization_depth + self.formulaic_state_apply_depth


def formulaic_normal_form_resource_report(
    generator_count: int,
    horizon: int,
    *,
    verify_monoid: bool = True,
) -> FormulaicNormalFormResourceReport:
    k = _generator_count(generator_count)
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 1:
        raise ValueError("horizon must be positive")
    n = 1 << k
    m = 1 << k
    if verify_monoid:
        states, operations = commuting_idempotent_mask_fixture(k)
        monoid = generated_transformation_monoid(states, operations)
        if monoid.size != m:
            raise AssertionError("commuting-idempotent fixture failed 2^k monoid theorem")
    return FormulaicNormalFormResourceReport(
        generator_count=k,
        state_count=n,
        monoid_size=m,
        horizon=horizon,
        generic_cayley_cells=m * m,
        generic_effect_action_cells=m * n,
        literal_word_entries=literal_word_count(k, horizon),
        formulaic_normal_form_bits=k,
        formulaic_generator_metadata_entries=k,
        formulaic_parallel_normalization_depth=parallel_normalization_depth(horizon),
        formulaic_state_apply_depth=1,
    )
