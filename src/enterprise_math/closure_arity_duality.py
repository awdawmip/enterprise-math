"""Exact separation of query-generator arity and relation-law premise arity.

For a finite exact-state family Omega on labels P:

* g(Omega) is the maximum, over closure classes C, of the smallest cardinality
  of a seed S with cl(S)=C.  It measures conjunction-query representation.
* h_circ(Omega) is the maximum premise size among rooted minimal implications.
  It measures direct irreducible relation-law arity.

The two quantities are incomparable.  This module computes both by exhaustive
finite closure enumeration for pressure-test fixtures.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Hashable, Iterable

from .closure_implication_circuits import closure_of, maximum_circuit_arity

Label = Hashable
State = frozenset[Label]


@dataclass(frozen=True)
class ClosureArityReport:
    query_generator_horizon: int
    direct_circuit_horizon: int
    closed_class_count: int
    minimum_generator_sizes: tuple[tuple[State, int], ...]


def _powerset(labels: tuple[Label, ...]):
    for size in range(len(labels) + 1):
        for subset in combinations(labels, size):
            yield frozenset(subset)


def minimum_closure_generator_sizes(
    labels: Iterable[Label], states: Iterable[State]
) -> dict[State, int]:
    """Return min seed cardinality for every closure class realized by Omega."""
    labels = tuple(labels)
    states = tuple(states)
    minima: dict[State, int] = {}
    for seed in _powerset(labels):
        closed = closure_of(labels, states, seed)
        size = len(seed)
        prior = minima.get(closed)
        if prior is None or size < prior:
            minima[closed] = size
    return minima


def closure_generator_horizon(labels: Iterable[Label], states: Iterable[State]) -> int:
    minima = minimum_closure_generator_sizes(labels, states)
    return max(minima.values(), default=0)


def closure_arity_report(labels: Iterable[Label], states: Iterable[State]) -> ClosureArityReport:
    labels = tuple(labels)
    states = tuple(states)
    minima = minimum_closure_generator_sizes(labels, states)
    ordered = tuple(sorted(minima.items(), key=lambda item: (item[1], tuple(sorted(map(repr, item[0]))))))
    return ClosureArityReport(
        query_generator_horizon=max(minima.values(), default=0),
        direct_circuit_horizon=maximum_circuit_arity(labels, states),
        closed_class_count=len(minima),
        minimum_generator_sizes=ordered,
    )


def boolean_identity_states(labels: Iterable[Label]) -> tuple[State, ...]:
    """All subsets of P; the induced closure is the identity closure."""
    labels = tuple(labels)
    return tuple(_powerset(labels))
