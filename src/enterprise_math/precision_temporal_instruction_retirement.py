"""Temporal primitive-instruction retirement over a sequence of cut clutters."""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations
from typing import Dict, Hashable, Iterable, Mapping, Sequence, Tuple

Generator = Hashable
Cut = frozenset[Generator]
Clutter = Tuple[Cut, ...]


def _subsets(generators: Sequence[Generator]):
    gens = tuple(generators)
    for r in range(len(gens) + 1):
        for items in combinations(gens, r):
            yield frozenset(items)


def hits(retained: frozenset[Generator], clutter: Sequence[Iterable[Generator]]) -> bool:
    return all(retained.intersection(cut) for cut in clutter)


def minimal_transversals(generators: Sequence[Generator], clutter: Sequence[Iterable[Generator]]) -> Tuple[frozenset[Generator], ...]:
    feasible = [S for S in _subsets(generators) if hits(S, clutter)]
    return tuple(S for S in feasible if not any(T < S for T in feasible))


def minimum_transversals(generators: Sequence[Generator], clutter: Sequence[Iterable[Generator]]) -> Tuple[frozenset[Generator], ...]:
    mins = minimal_transversals(generators, clutter)
    if not mins:
        return (frozenset(),)
    k = min(len(S) for S in mins)
    return tuple(S for S in mins if len(S) == k)


def cut_clutter_weakens(early: Sequence[Iterable[Generator]], late: Sequence[Iterable[Generator]]) -> bool:
    """Every late minimal cut contains some early minimal cut."""
    early_sets = tuple(frozenset(C) for C in early)
    return all(any(E.issubset(frozenset(L)) for E in early_sets) for L in late)


def optimal_nested_schedule(
    generators: Sequence[Generator],
    clutters: Sequence[Sequence[Iterable[Generator]]],
    weights: Sequence[Mapping[Generator, int]] | None = None,
):
    """Minimum holding-cost schedule under no-reacquisition S_(i+1) subseteq S_i."""
    gens = tuple(generators)
    if weights is None:
        weights = tuple({g: 1 for g in gens} for _ in clutters)
    if len(weights) != len(clutters):
        raise ValueError("weights must match number of stages")
    feasible = [tuple(S for S in _subsets(gens) if hits(S, C)) for C in clutters]

    @lru_cache(None)
    def solve(i: int, retained_tuple: Tuple[Generator, ...]):
        S = frozenset(retained_tuple)
        stage_cost = sum(int(weights[i][g]) for g in S)
        if i == len(clutters) - 1:
            return stage_cost, (S,)
        candidates = []
        for T in feasible[i + 1]:
            if T.issubset(S):
                future_cost, suffix = solve(i + 1, tuple(sorted(T, key=repr)))
                candidates.append((stage_cost + future_cost, (S,) + suffix))
        if not candidates:
            return 10**18, tuple()
        return min(candidates, key=lambda item: (item[0], tuple(map(len, item[1]))))

    starts = [solve(0, tuple(sorted(S, key=repr))) for S in feasible[0]]
    return min(starts, key=lambda item: (item[0], tuple(map(len, item[1]))))
