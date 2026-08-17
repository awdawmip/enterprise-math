"""Finite distributive action compiler for the R007/Stage131 resource axis.

Executable evidence only; the theorem targets are elementary finite-poset statements.

For a finite poset P, let J(P) be its lower-set lattice.  Every mask I in J(P)
acts on states X in J(P) by projection

    q_I(X) = X ∩ I.

Composition is meet/intersection.  The unique primitive meet program for I is
the frontier Min(P \\ I), via masks M_p = P \\ ↑p.  Consequently:

* minimal universal basis storage = |P|;
* exact target depth = |Min(P \\ I)|;
* worst depth = width(P);
* depth spectrum = antichain-size spectrum of P;
* full one-step table storage = |J(P)| - 1.

The helpers below also check sharp bounds on |J(P)| at fixed n=|P| and width w.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from typing import Iterable, Sequence

Pair = tuple[int, int]
Order = frozenset[Pair]
LowerSet = frozenset[int]


def transitive_closure(size: int, relations: Iterable[Pair]) -> Order:
    if size < 0:
        raise ValueError("size must be nonnegative")
    closure = set(relations)
    if any(a < 0 or b < 0 or a >= size or b >= size or a == b for a, b in closure):
        raise ValueError("relations must be strict pairs on 0..size-1")
    changed = True
    while changed:
        changed = False
        current = tuple(closure)
        for a, b in current:
            for c, d in current:
                if b == c and a != d and (a, d) not in closure:
                    closure.add((a, d))
                    changed = True
    if any((b, a) in closure for a, b in closure):
        raise ValueError("relations contain a cycle")
    return frozenset(closure)


def is_lower_set(size: int, order: Order, subset: Iterable[int]) -> bool:
    values = frozenset(subset)
    if any(x < 0 or x >= size for x in values):
        return False
    return all(not (b in values and a not in values) for a, b in order)


def lower_sets(size: int, order: Order) -> tuple[LowerSet, ...]:
    out: list[LowerSet] = []
    for mask in range(1 << size):
        subset = frozenset(i for i in range(size) if mask & (1 << i))
        if is_lower_set(size, order, subset):
            out.append(subset)
    return tuple(out)


def principal_upset(size: int, order: Order, point: int) -> frozenset[int]:
    if not 0 <= point < size:
        raise ValueError("point out of range")
    return frozenset(
        q for q in range(size) if q == point or (point, q) in order
    )


def meet_irreducible_mask(size: int, order: Order, point: int) -> LowerSet:
    """M_p = P \\ ↑p, the primitive fixed-mask action attached to p."""
    return frozenset(set(range(size)) - set(principal_upset(size, order, point)))


def mask_frontier(size: int, order: Order, mask: LowerSet) -> frozenset[int]:
    """Minimal elements of the upset complement P \\ mask."""
    if not is_lower_set(size, order, mask):
        raise ValueError("mask must be a lower set")
    complement = set(range(size)) - set(mask)
    return frozenset(
        p
        for p in complement
        if not any(q in complement and (q, p) in order for q in complement)
    )


def compile_mask(size: int, order: Order, mask: LowerSet) -> tuple[int, ...]:
    """Unique shortest primitive program for q_mask."""
    return tuple(sorted(mask_frontier(size, order, mask)))


def execute_program(size: int, order: Order, program: Sequence[int]) -> LowerSet:
    result = set(range(size))
    for point in program:
        result.intersection_update(meet_irreducible_mask(size, order, point))
    return frozenset(result)


def project(state: LowerSet, mask: LowerSet) -> LowerSet:
    return frozenset(state & mask)


def language_envelope(masks: Sequence[LowerSet]) -> LowerSet:
    """Collective one-step observational envelope: join/union of masks."""
    result: set[int] = set()
    for mask in masks:
        result.update(mask)
    return frozenset(result)


def one_step_signature(state: LowerSet, masks: Sequence[LowerSet]) -> tuple[LowerSet, ...]:
    return tuple(project(state, mask) for mask in masks)


def composite_projection(state: LowerSet, masks: Sequence[LowerSet]) -> LowerSet:
    """Output of a nonempty composition word; composition is intersection."""
    if not masks:
        raise ValueError("word must be nonempty")
    result = set(state)
    for mask in masks:
        result.intersection_update(mask)
    return frozenset(result)


def antichains(size: int, order: Order) -> tuple[frozenset[int], ...]:
    out: list[frozenset[int]] = []
    for r in range(size + 1):
        for subset in combinations(range(size), r):
            if all(
                (a, b) not in order and (b, a) not in order
                for a, b in combinations(subset, 2)
            ):
                out.append(frozenset(subset))
    return tuple(out)


def width(size: int, order: Order) -> int:
    return max((len(a) for a in antichains(size, order)), default=0)


def depth_spectrum(size: int, order: Order) -> dict[int, int]:
    counts = Counter(
        len(mask_frontier(size, order, mask))
        for mask in lower_sets(size, order)
    )
    return dict(sorted(counts.items()))


def antichain_spectrum(size: int, order: Order) -> dict[int, int]:
    counts = Counter(len(a) for a in antichains(size, order))
    return dict(sorted(counts.items()))


def compiler_resources(size: int, order: Order) -> tuple[int, int, int]:
    """(full nonidentity table, unique primitive basis, worst primitive depth)."""
    return len(lower_sets(size, order)) - 1, size, width(size, order)


def ideal_count_extremal_bounds(size: int, poset_width: int) -> tuple[int, int]:
    """Sharp min/max possible |J(P)| for n=size and width=w.

    lower = n-w+2^w, attained by a chain of n-w points below a w-antichain.
    upper = balanced product of w chains, from Dilworth plus product balancing.
    """
    if size == 0:
        if poset_width != 0:
            raise ValueError("empty poset has width 0")
        return 1, 1
    if not 1 <= poset_width <= size:
        raise ValueError("require 1 <= width <= size")
    lower = size - poset_width + 2**poset_width
    q, r = divmod(size, poset_width)
    upper = (q + 2) ** r * (q + 1) ** (poset_width - r)
    return lower, upper


def lower_extremizer(size: int, poset_width: int) -> Order:
    """Ordinal sum: a chain of n-w points below a w-antichain."""
    if not 1 <= poset_width <= size:
        raise ValueError("require 1 <= width <= size")
    stem = size - poset_width
    relations: set[Pair] = set()
    for i in range(stem):
        for j in range(i + 1, stem):
            relations.add((i, j))
    for i in range(stem):
        for j in range(stem, size):
            relations.add((i, j))
    return transitive_closure(size, relations)


def upper_extremizer(size: int, poset_width: int) -> Order:
    """Disjoint union of w chains with lengths as balanced as possible."""
    if not 1 <= poset_width <= size:
        raise ValueError("require 1 <= width <= size")
    q, r = divmod(size, poset_width)
    lengths = [q + 1] * r + [q] * (poset_width - r)
    relations: set[Pair] = set()
    start = 0
    for length in lengths:
        chain = list(range(start, start + length))
        for i, a in enumerate(chain):
            for b in chain[i + 1 :]:
                relations.add((a, b))
        start += length
    return transitive_closure(size, relations)


def disjoint_chain_ideal_count_bounds(
    size: int, poset_width: int
) -> tuple[int, int]:
    """Sharp |J(P)| bounds when P is a disjoint union of exactly w nonempty chains.

    If chain lengths alpha_i are positive and sum to n, then
        |J(P)| = product_i (alpha_i + 1).
    The minimum is maximally skewed and the maximum is balanced.
    """
    if not 1 <= poset_width <= size:
        raise ValueError("require 1 <= width <= size")
    lower = (size - poset_width + 2) * 2 ** (poset_width - 1)
    _general_lower, upper = ideal_count_extremal_bounds(size, poset_width)
    return lower, upper
