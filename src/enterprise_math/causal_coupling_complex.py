"""Factorization failures in the currently exposed causal state language.

For a coherent family of subsystem restrictions, the subsets whose *current
exposed signatures* factor independently are downward closed.  Their abstract
simplicial complex is therefore derived from causal factorization rather than
assumed as an interaction hypergraph.  Minimal nonfaces are the smallest
subsystem groups whose joint future cannot be reconstructed from the currently
exposed component signatures.

Important boundary: a minimal nonface of size q is **language-relative coupling
order**, not proof of an absolute q-body composition primitive.  A finer but
still identity-free continuation type may localize an apparent higher-order
constraint into a lower-order recursive law.  The even-parity three-bit example
is the minimal counterexample: all pairs factor in the marginal language, yet a
two-state parity continuation type generates the full triple constraint through
an associative binary XOR law.
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
    """Minimal nonfaces of the current causal-independence complex."""
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
    """Smallest current-language factorization-failure order.

    This is not an absolute primitive arity.  Refining the exposed state to the
    minimal continuation type can reduce the order required for recursive
    generation.
    """
    groups = minimal_coupling_groups(universe, independent_subsets)
    return None if not groups else min(len(group) for group in groups)
