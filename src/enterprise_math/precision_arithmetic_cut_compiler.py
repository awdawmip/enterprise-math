"""Arithmetic specialization of the R004 structural obstruction compiler.

Exact state is binary, the current observable is a weighted integer sum, and
future generators are coordinate bit flips.  Carrier cuts are exactly the
support-minimal non-dissociated weight subsets.
"""

from __future__ import annotations

from itertools import combinations, product
from typing import FrozenSet, Iterable, Sequence, Tuple


def weighted_observation(state: Sequence[int], weights: Sequence[int]) -> int:
    if len(state) != len(weights):
        raise ValueError("state and weights must have the same length")
    if any(bit not in (0, 1) for bit in state):
        raise ValueError("state must be binary")
    return sum(w * bit for w, bit in zip(weights, state))


def retained_signature(
    state: Sequence[int],
    weights: Sequence[int],
    retained: Iterable[int],
) -> Tuple[int, Tuple[int, ...]]:
    if any(w == 0 for w in weights):
        raise ValueError("all weights must be nonzero")
    kept = tuple(sorted(retained))
    return weighted_observation(state, weights), tuple(state[i] for i in kept)


def subset_sum_collision(
    weights: Sequence[int],
    support: Iterable[int],
) -> Tuple[Tuple[int, ...], Tuple[int, ...]] | None:
    idx = tuple(sorted(support))
    seen: dict[int, Tuple[int, ...]] = {}
    for bits in product((0, 1), repeat=len(idx)):
        total = sum(weights[i] * bits[j] for j, i in enumerate(idx))
        previous = seen.get(total)
        if previous is not None and previous != bits:
            return previous, bits
        seen[total] = bits
    return None


def is_dissociated(weights: Sequence[int], support: Iterable[int] | None = None) -> bool:
    if any(w == 0 for w in weights):
        raise ValueError("all weights must be nonzero")
    idx = range(len(weights)) if support is None else support
    return subset_sum_collision(weights, idx) is None


def signed_relation_witness(
    weights: Sequence[int],
    support: Iterable[int],
) -> Tuple[int, ...] | None:
    idx = tuple(sorted(support))
    collision = subset_sum_collision(weights, idx)
    if collision is None:
        return None
    left, right = collision
    eps = [0] * len(weights)
    for j, i in enumerate(idx):
        eps[i] = left[j] - right[j]
    relation = tuple(eps)
    assert any(relation)
    assert all(e in (-1, 0, 1) for e in relation)
    assert sum(e * w for e, w in zip(relation, weights)) == 0
    return relation


def _powerset_indices(n: int):
    for r in range(n + 1):
        for c in combinations(range(n), r):
            yield frozenset(c)


def minimal_nondissociated_supports(weights: Sequence[int]) -> Tuple[FrozenSet[int], ...]:
    if any(w == 0 for w in weights):
        raise ValueError("all weights must be nonzero")
    bad = []
    for support in _powerset_indices(len(weights)):
        if support and not is_dissociated(weights, support):
            bad.append(support)
    mins = [s for s in bad if not any(t < s for t in bad)]
    return tuple(sorted(mins, key=lambda s: (len(s), tuple(sorted(s)))))


def equal_weight_minimal_cuts(dimension: int) -> Tuple[FrozenSet[int], ...]:
    if dimension < 0:
        raise ValueError("dimension must be nonnegative")
    return tuple(frozenset(c) for c in combinations(range(dimension), 2))


def powers_of_two_weights(dimension: int) -> Tuple[int, ...]:
    if dimension < 0:
        raise ValueError("dimension must be nonnegative")
    return tuple(1 << i for i in range(dimension))
