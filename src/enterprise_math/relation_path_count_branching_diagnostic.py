"""One-step natural path count separates undefinedness from branching degree.

For a finite 0/1 relation adjacency matrix A and the constant all-target
observation row ``1^T``, ordinary natural-number multiplication gives

    1^T A = (outdegree(source))_source.

Thus one scalar count per source classifies raw relation structure exactly:

* 0 successors -> UNDEFINED / DOMAIN defect;
* 1 successor  -> locally deterministic;
* >1 successors -> RELATION branching with the exact raw branch count.

Applying the coefficient quotient ``n -> [n>0]`` collapses the last two cases,
retaining totality/definedness but forgetting branching multiplicity.  This is
the local one-step form of the N->Boolean precision quotient.

The diagnostic counts distinct relation targets because a Relation is a set of
ordered pairs; parallel labeled edges would require a richer edge/witness model.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Iterable

from .admissible_support import Relation


State = Hashable
UNDEFINED = "UNDEFINED"
DETERMINISTIC = "DETERMINISTIC"
BRANCHING = "BRANCHING"


def relation_source_outdegrees(
    states: Iterable[State],
    relation: Relation,
) -> tuple[tuple[State, int], ...]:
    order = tuple(states)
    if not order:
        raise ValueError("state set must be nonempty")
    if len(set(order)) != len(order):
        raise ValueError("state order must contain distinct states")
    if not isinstance(relation, frozenset):
        raise TypeError("relation must be a frozenset")
    state_set = set(order)
    if any(source not in state_set or target not in state_set for source, target in relation):
        raise ValueError("relation contains state outside declared set")
    targets = {state: set() for state in order}
    for source, target in relation:
        targets[source].add(target)
    return tuple((state, len(targets[state])) for state in order)


def source_relation_class_from_count(count: int) -> str:
    if isinstance(count, bool) or not isinstance(count, int) or count < 0:
        raise ValueError("successor count must be a nonnegative integer")
    if count == 0:
        return UNDEFINED
    if count == 1:
        return DETERMINISTIC
    return BRANCHING


@dataclass(frozen=True)
class SourceCountDiagnostic:
    source: State
    successor_count: int
    raw_class: str
    boolean_defined: bool


def relation_source_count_diagnostics(
    states: Iterable[State],
    relation: Relation,
) -> tuple[SourceCountDiagnostic, ...]:
    return tuple(
        SourceCountDiagnostic(
            source=state,
            successor_count=count,
            raw_class=source_relation_class_from_count(count),
            boolean_defined=count > 0,
        )
        for state, count in relation_source_outdegrees(states, relation)
    )
