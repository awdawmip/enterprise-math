"""Irreducible coupling groups from causal signature factorization failures.

For a coherent family of subsystem restrictions, the subsets whose signatures
factor independently are downward closed.  Their abstract simplicial complex is
therefore derived from causal factorization rather than assumed as an interaction
hypergraph.  Minimal nonfaces are the smallest subsystem groups whose joint
future cannot be reconstructed from independent component futures.
"""

from __future__ import annotations

from itertools import combinations
from typing import Hashable


Subsystem = Hashable
Subset = frozenset[Subsystem]


def all_nonempty_subsets(universe: tuple[Subsystem, ...]) -> tuple[Subset, ...]:
    if not isinstance(universe, tuple) or not universe:
        raise ValueError("universe must be a non-empty tuple")
    if len(set(universe)) != len(universe):
        raise ValueError("universe elements must be unique")
    return tuple(
        frozenset(group)
        for size in range(1, len(universe) + 1)
        for group in combinations(universe, size)
    )


def is_downward_closed(
    universe: tuple[Subsystem, ...],
    independent_subsets: frozenset[Subset],
) -> bool:
    """Whether every nonempty subset of an independent set is independent."""
    allowed = set(independent_subsets)
    for subset in allowed:
        if not subset:
            continue
        if not subset <= set(universe):
            return False
        elements = tuple(subset)
        for size in range(1, len(elements)):
            for child in combinations(elements, size):
                if frozenset(child) not in allowed:
                    return False
    return True


def minimal_coupling_groups(
    universe: tuple[Subsystem, ...],
    independent_subsets: frozenset[Subset],
) -> tuple[Subset, ...]:
    """Minimal nonfaces of the causal independence complex."""
    if not is_downward_closed(universe, independent_subsets):
        raise ValueError("independent_subsets must be downward closed")
    independent = set(independent_subsets)
    result: list[Subset] = []
    for subset in all_nonempty_subsets(universe):
        if subset in independent:
            continue
        elements = tuple(subset)
        proper_nonempty = (
            frozenset(child)
            for size in range(1, len(elements))
            for child in combinations(elements, size)
        )
        if all(child in independent for child in proper_nonempty):
            result.append(subset)
    return tuple(sorted(result, key=lambda item: (len(item), tuple(sorted(map(str, item))))))


def coupling_order(
    universe: tuple[Subsystem, ...],
    independent_subsets: frozenset[Subset],
) -> int | None:
    """Smallest irreducible factorization-failure order, or None if fully independent."""
    groups = minimal_coupling_groups(universe, independent_subsets)
    return None if not groups else min(len(group) for group in groups)
