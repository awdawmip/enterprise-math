"""Minimum-event support uniformity and its classical design-theory shadow.

Given a family of equal-size primitive event supports B on N slots, define the
t-context incidence of a slot subset S as the number of primitive supports that
contain S.  If this count is constant over all t-subsets, the causal event grammar
cannot distinguish any t-slot context at the support-incidence level.

Classical t-design/Steiner terminology is a shadow of this property.  For the
weight-four supports of the [7,3,4] simplex code the incidence is uniform through
t=2 but splits at t=3.  For the extended [8,4,4] Hamming code every triple occurs
in exactly one weight-four support, giving the classical S(3,4,8) pattern.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from .causal_code_lattice import hamming_weight

Support = frozenset[int]


def codeword_supports(codewords, weight: int) -> tuple[Support, ...]:
    if weight <= 0:
        raise ValueError("weight must be positive")
    return tuple(
        frozenset(index for index, bit in enumerate(word) if bit)
        for word in codewords
        if hamming_weight(word) == weight
    )


def incidence_histogram(
    slot_count: int,
    supports: tuple[Support, ...],
    context_size: int,
) -> dict[int, int]:
    if slot_count < 1 or not (1 <= context_size <= slot_count):
        raise ValueError("invalid slot/context size")
    histogram = Counter()
    for context in combinations(range(slot_count), context_size):
        subset = set(context)
        incidence = sum(subset <= support for support in supports)
        histogram[incidence] += 1
    return dict(sorted(histogram.items()))


def context_incidence_is_uniform(
    slot_count: int,
    supports: tuple[Support, ...],
    context_size: int,
) -> bool:
    return len(incidence_histogram(slot_count, supports, context_size)) == 1


def uniform_incidence_value(
    slot_count: int,
    supports: tuple[Support, ...],
    context_size: int,
) -> int:
    histogram = incidence_histogram(slot_count, supports, context_size)
    if len(histogram) != 1:
        raise ValueError("context incidence is not uniform")
    return next(iter(histogram))


def nontrivial_uniformity_depth(
    slot_count: int,
    supports: tuple[Support, ...],
) -> int:
    """Largest t<=block size with uniform incidence before support size is exceeded."""
    if not supports:
        return 0
    block_sizes = {len(support) for support in supports}
    if len(block_sizes) != 1:
        raise ValueError("supports must have equal size")
    block_size = next(iter(block_sizes))
    depth = 0
    for context_size in range(1, block_size + 1):
        if not context_incidence_is_uniform(slot_count, supports, context_size):
            break
        depth = context_size
    return depth
