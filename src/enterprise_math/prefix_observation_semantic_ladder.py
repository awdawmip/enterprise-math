"""Three exact semantic quotients for the commuting-idempotent prefix language.

The same literal word supports three increasingly rich declared observation
languages.

1. Terminal-set semantics
   Keep only the final set/mask of generators that ever appeared.

2. Discovery-order semantics
   Keep the generators in first-appearance order, but forget how many prefix
   positions each cumulative state persists.

3. Full-prefix-timing semantics
   Keep the run-length phase form from the parent generation.

There are exact surjective homomorphisms

    full timing -> discovery order -> terminal set.

The discovery-order product is formulaic: concatenate the left list with those
right generators not already seen on the left.  This is the familiar free
left-regular-band first-occurrence normal form.  It is finite, with

    1 + sum_{s=1}^k P(k,s)

including identity.

For exact nonempty word length H the three semantic class counts are

    terminal:  sum_{s<=min(k,H)} C(k,s),
    discovery: sum_{s<=min(k,H)} P(k,s),
    timing:    sum_{s<=min(k,H)} P(k,s) C(H-1,s-1).

For H>=k the first two saturate, while full timing continues polynomial growth
in H.  Thus observation timing creates an additional semantic precision axis
strictly above order-of-discovery, which is itself strictly above terminal set
when enough generators are available.

Left regular bands, first-occurrence word reductions and quotient homomorphisms
are standard prior algebra/CS.  The project value is the explicit observation-
language precision ladder and exact projection interfaces.
"""

from __future__ import annotations

from math import comb, factorial
from typing import Sequence

from .prefix_run_length_normal_form import (
    PrefixRun,
    PrefixRunNormalForm,
    compose_prefix_run_forms,
    normalize_prefix_word_to_runs,
)


DiscoveryOrder = tuple[int, ...]


def _generator_count(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("generator_count must be a positive integer")
    return value


def _validate_discovery_order(
    order: Sequence[int],
    generator_count: int,
) -> DiscoveryOrder:
    k = _generator_count(generator_count)
    values = tuple(order)
    if len(set(values)) != len(values):
        raise ValueError("discovery order generators must be distinct")
    for generator in values:
        if isinstance(generator, bool) or not isinstance(generator, int) or not 0 <= generator < k:
            raise ValueError("discovery generator outside declared range")
    return values


def discovery_order_normal_form(
    word: Sequence[int],
    generator_count: int,
) -> DiscoveryOrder:
    k = _generator_count(generator_count)
    seen = set()
    result = []
    for generator in word:
        if isinstance(generator, bool) or not isinstance(generator, int) or not 0 <= generator < k:
            raise ValueError("word contains generator outside declared range")
        if generator not in seen:
            seen.add(generator)
            result.append(generator)
    return tuple(result)


def compose_discovery_orders(
    left: Sequence[int],
    right: Sequence[int],
    generator_count: int,
) -> DiscoveryOrder:
    k = _generator_count(generator_count)
    left_order = _validate_discovery_order(left, k)
    right_order = _validate_discovery_order(right, k)
    seen = set(left_order)
    result = list(left_order)
    for generator in right_order:
        if generator not in seen:
            seen.add(generator)
            result.append(generator)
    return tuple(result)


def discovery_composition_matches_words(
    left_word: Sequence[int],
    right_word: Sequence[int],
    generator_count: int,
) -> bool:
    left = discovery_order_normal_form(left_word, generator_count)
    right = discovery_order_normal_form(right_word, generator_count)
    composed = compose_discovery_orders(left, right, generator_count)
    direct = discovery_order_normal_form(
        (*tuple(left_word), *tuple(right_word)),
        generator_count,
    )
    if composed != direct:
        raise AssertionError("discovery-order product disagreed with word concatenation")
    return True


def discovery_order_to_terminal_mask(
    order: Sequence[int],
    generator_count: int,
) -> int:
    values = _validate_discovery_order(order, generator_count)
    mask = 0
    for generator in values:
        mask |= 1 << generator
    return mask


def timing_form_to_discovery_order(
    form: Sequence[PrefixRun],
    generator_count: int,
) -> DiscoveryOrder:
    # Reuse timing-form validation through the parent composition with identity.
    validated: PrefixRunNormalForm = compose_prefix_run_forms((), form, generator_count)
    return tuple(phase.generator for phase in validated)


def timing_to_discovery_is_homomorphism(
    left: Sequence[PrefixRun],
    right: Sequence[PrefixRun],
    generator_count: int,
) -> bool:
    composed_timing = compose_prefix_run_forms(left, right, generator_count)
    projected_product = compose_discovery_orders(
        timing_form_to_discovery_order(left, generator_count),
        timing_form_to_discovery_order(right, generator_count),
        generator_count,
    )
    if timing_form_to_discovery_order(composed_timing, generator_count) != projected_product:
        raise AssertionError("timing->discovery projection failed homomorphism law")
    return True


def discovery_to_terminal_is_homomorphism(
    left: Sequence[int],
    right: Sequence[int],
    generator_count: int,
) -> bool:
    composed = compose_discovery_orders(left, right, generator_count)
    left_mask = discovery_order_to_terminal_mask(left, generator_count)
    right_mask = discovery_order_to_terminal_mask(right, generator_count)
    if discovery_order_to_terminal_mask(composed, generator_count) != (left_mask | right_mask):
        raise AssertionError("discovery->terminal projection failed OR homomorphism law")
    return True


def prefix_event_masks_from_discovery_order(
    order: Sequence[int],
    generator_count: int,
) -> tuple[int, ...]:
    values = _validate_discovery_order(order, generator_count)
    current = 0
    result = []
    for generator in values:
        current |= 1 << generator
        result.append(current)
    return tuple(result)


def discovery_order_from_event_masks(
    event_masks: Sequence[int],
    generator_count: int,
) -> DiscoveryOrder:
    k = _generator_count(generator_count)
    masks = tuple(event_masks)
    limit = 1 << k
    previous = 0
    result = []
    for mask in masks:
        if isinstance(mask, bool) or not isinstance(mask, int) or not 0 <= mask < limit:
            raise ValueError("event mask outside semantic state space")
        added = mask & ~previous
        if added == 0 or added & (added - 1):
            raise ValueError("each discovery event must add exactly one new generator")
        if previous & ~mask:
            raise ValueError("event masks must be monotone")
        generator = added.bit_length() - 1
        result.append(generator)
        previous = mask
    return _validate_discovery_order(tuple(result), k)


def falling_factorial(total: int, selected: int) -> int:
    if not 0 <= selected <= total:
        raise ValueError("selected must lie in 0..total")
    return factorial(total) // factorial(total - selected)


def terminal_semantic_count_exact_length(generator_count: int, word_length: int) -> int:
    k = _generator_count(generator_count)
    if isinstance(word_length, bool) or not isinstance(word_length, int) or word_length < 0:
        raise ValueError("word_length must be nonnegative")
    if word_length == 0:
        return 1
    return sum(comb(k, s) for s in range(1, min(k, word_length) + 1))


def discovery_semantic_count_exact_length(generator_count: int, word_length: int) -> int:
    k = _generator_count(generator_count)
    if isinstance(word_length, bool) or not isinstance(word_length, int) or word_length < 0:
        raise ValueError("word_length must be nonnegative")
    if word_length == 0:
        return 1
    return sum(
        falling_factorial(k, s)
        for s in range(1, min(k, word_length) + 1)
    )


def timing_semantic_count_exact_length(generator_count: int, word_length: int) -> int:
    k = _generator_count(generator_count)
    if isinstance(word_length, bool) or not isinstance(word_length, int) or word_length < 0:
        raise ValueError("word_length must be nonnegative")
    if word_length == 0:
        return 1
    return sum(
        falling_factorial(k, s) * comb(word_length - 1, s - 1)
        for s in range(1, min(k, word_length) + 1)
    )


def discovery_monoid_size(generator_count: int) -> int:
    k = _generator_count(generator_count)
    return 1 + sum(falling_factorial(k, s) for s in range(1, k + 1))


def discovery_left_regular_band_identities_hold(
    left: Sequence[int],
    right: Sequence[int],
    generator_count: int,
) -> bool:
    x = _validate_discovery_order(left, generator_count)
    y = _validate_discovery_order(right, generator_count)
    xx = compose_discovery_orders(x, x, generator_count)
    xy = compose_discovery_orders(x, y, generator_count)
    xyx = compose_discovery_orders(xy, x, generator_count)
    return xx == x and xyx == xy


def normalize_word_to_all_three_levels(
    word: Sequence[int],
    generator_count: int,
) -> tuple[PrefixRunNormalForm, DiscoveryOrder, int]:
    timing = normalize_prefix_word_to_runs(word, generator_count)
    discovery = timing_form_to_discovery_order(timing, generator_count)
    terminal = discovery_order_to_terminal_mask(discovery, generator_count)
    return timing, discovery, terminal
