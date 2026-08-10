"""Source-dependent shortcut presentations for a unary implication chain.

For the chain closure law on vertices 0<1<...<n, an unrestricted exact rule
presentation may choose any subset of transitive edges (i,j), i<j, provided the
same reachability relation is preserved.  Since an adjacent pair i,i+1 has no
intermediate vertex, every exact presentation must contain all n adjacent edges;
all other stored edges are optional shortcuts.

Storage is the number of stored edges.  Reusable inference depth is the directed
diameter over all comparable pairs: the maximum shortest-path length from i to j
for i<j.  Thus a presentation with diameter at most k is exactly a k-transitive-
closure spanner of the directed path/total order in standard graph terminology.

This strictly generalizes the parent translation-invariant jump-length family.
Source-specific shortcuts can beat any jump-type presentation with the same edge
budget because an expensive jump length need not be replicated at every source.

A sharp closed form is available for one extra shortcut a->b.  Its diameter is

    max(b-1, n-a-1, n-(b-a)+1).

The optimal one-shortcut diameter over all a<b with b-a>=2 is

    ceil((2n-1)/3) = floor((2n+1)/3).

An optimal shortcut is obtained by d=floor((2n+1)/3),

    a=n-d-1,
    b=2n-2d.

For n=5 this is edge 1->4: only six total rules, diameter3.  Every
translation-invariant six-rule presentation has diameter at least4.

TC-spanners, shortcuts and graph diameter are standard prior graph theory.  The
project value is the Stage131 interpretation: source-dependent caching expands
the exact presentation frontier beyond global jump-length bases.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Iterable

from .stage131_chain_jump_presentation import (
    ChainPresentationPoint,
    exact_chain_jump_pareto_frontier,
)


Edge = tuple[int, int]


def _positive_int(value: int, *, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def adjacent_chain_edges(chain_length: int) -> frozenset[Edge]:
    n = _positive_int(chain_length, name="chain_length")
    return frozenset((index, index + 1) for index in range(n))


def transitive_chain_edges(chain_length: int) -> frozenset[Edge]:
    n = _positive_int(chain_length, name="chain_length")
    return frozenset(
        (source, target)
        for source in range(n + 1)
        for target in range(source + 1, n + 1)
    )


def optional_chain_shortcuts(chain_length: int) -> tuple[Edge, ...]:
    n = _positive_int(chain_length, name="chain_length")
    return tuple(
        (source, target)
        for source in range(n + 1)
        for target in range(source + 2, n + 1)
    )


def normalize_exact_chain_presentation(
    chain_length: int,
    edges: Iterable[Edge],
) -> frozenset[Edge]:
    n = _positive_int(chain_length, name="chain_length")
    values = frozenset(edges)
    allowed = transitive_chain_edges(n)
    if not values.issubset(allowed):
        raise ValueError("presentation contains an edge outside the chain transitive closure")
    adjacent = adjacent_chain_edges(n)
    if not adjacent.issubset(values):
        raise ValueError("exact chain presentation must contain every adjacent edge")
    return values


def chain_shortest_path_lengths(
    chain_length: int,
    edges: Iterable[Edge],
) -> tuple[tuple[int | None, ...], ...]:
    n = _positive_int(chain_length, name="chain_length")
    presentation = normalize_exact_chain_presentation(n, edges)
    outgoing: dict[int, tuple[int, ...]] = {
        source: tuple(sorted(target for left, target in presentation if left == source))
        for source in range(n + 1)
    }
    rows = []
    for source in range(n + 1):
        distance: list[int | None] = [None] * (n + 1)
        distance[source] = 0
        for current in range(source, n + 1):
            current_distance = distance[current]
            if current_distance is None:
                continue
            for target in outgoing[current]:
                candidate = current_distance + 1
                if distance[target] is None or candidate < distance[target]:
                    distance[target] = candidate
        rows.append(tuple(distance))
    return tuple(rows)


def chain_presentation_diameter(
    chain_length: int,
    edges: Iterable[Edge],
) -> int:
    n = _positive_int(chain_length, name="chain_length")
    distances = chain_shortest_path_lengths(n, edges)
    values = []
    for source in range(n):
        for target in range(source + 1, n + 1):
            distance = distances[source][target]
            if distance is None:
                raise AssertionError("exact chain presentation lost transitive reachability")
            values.append(distance)
    return max(values)


def is_k_tc_spanner_of_chain(
    chain_length: int,
    edges: Iterable[Edge],
    diameter_budget: int,
) -> bool:
    k = _positive_int(diameter_budget, name="diameter_budget")
    presentation = normalize_exact_chain_presentation(chain_length, edges)
    return chain_presentation_diameter(chain_length, presentation) <= k


@dataclass(frozen=True)
class ChainShortcutPresentationPoint:
    chain_length: int
    edges: frozenset[Edge]
    stored_rules: int
    diameter: int

    @property
    def shortcut_count(self) -> int:
        return self.stored_rules - self.chain_length


def chain_shortcut_presentation_point(
    chain_length: int,
    edges: Iterable[Edge],
) -> ChainShortcutPresentationPoint:
    n = _positive_int(chain_length, name="chain_length")
    presentation = normalize_exact_chain_presentation(n, edges)
    return ChainShortcutPresentationPoint(
        chain_length=n,
        edges=presentation,
        stored_rules=len(presentation),
        diameter=chain_presentation_diameter(n, presentation),
    )


def shortcut_point_dominates(
    left: ChainShortcutPresentationPoint,
    right: ChainShortcutPresentationPoint,
) -> bool:
    if left.chain_length != right.chain_length:
        raise ValueError("presentation points must belong to the same chain")
    return (
        left.stored_rules <= right.stored_rules
        and left.diameter <= right.diameter
        and (left.stored_rules < right.stored_rules or left.diameter < right.diameter)
    )


def one_shortcut_diameter_closed(
    chain_length: int,
    source: int,
    target: int,
) -> int:
    n = _positive_int(chain_length, name="chain_length")
    if isinstance(source, bool) or not isinstance(source, int):
        raise TypeError("source must be an integer")
    if isinstance(target, bool) or not isinstance(target, int):
        raise TypeError("target must be an integer")
    if not (0 <= source < target <= n) or target - source < 2:
        raise ValueError("shortcut must skip at least one chain edge")
    length = target - source
    return max(
        target - 1,
        n - source - 1,
        n - length + 1,
    )


def one_shortcut_presentation(
    chain_length: int,
    source: int,
    target: int,
) -> ChainShortcutPresentationPoint:
    n = _positive_int(chain_length, name="chain_length")
    shortcut = (source, target)
    edges = frozenset((*adjacent_chain_edges(n), shortcut))
    point = chain_shortcut_presentation_point(n, edges)
    closed = one_shortcut_diameter_closed(n, source, target)
    if point.diameter != closed:
        raise AssertionError("one-shortcut graph diameter disagreed with closed form")
    return point


def optimal_one_shortcut_diameter(chain_length: int) -> int:
    n = _positive_int(chain_length, name="chain_length")
    if n == 1:
        return 1
    return (2 * n + 1) // 3


def optimal_one_shortcut_presentation(chain_length: int) -> ChainShortcutPresentationPoint:
    n = _positive_int(chain_length, name="chain_length")
    if n == 1:
        return chain_shortcut_presentation_point(n, adjacent_chain_edges(n))
    diameter = optimal_one_shortcut_diameter(n)
    source = n - diameter - 1
    target = 2 * n - 2 * diameter
    point = one_shortcut_presentation(n, source, target)
    if point.diameter != diameter:
        raise AssertionError("constructive optimal one-shortcut edge missed theorem diameter")
    return point


def brute_force_best_one_shortcut(chain_length: int) -> ChainShortcutPresentationPoint:
    n = _positive_int(chain_length, name="chain_length")
    if n == 1:
        return chain_shortcut_presentation_point(n, adjacent_chain_edges(n))
    points = tuple(
        one_shortcut_presentation(n, source, target)
        for source in range(n)
        for target in range(source + 2, n + 1)
    )
    return min(points, key=lambda point: (point.diameter, point.stored_rules, sorted(point.edges)))


def enumerate_chain_tc_spanners(chain_length: int) -> tuple[ChainShortcutPresentationPoint, ...]:
    n = _positive_int(chain_length, name="chain_length")
    if n > 6:
        raise ValueError("exhaustive source-dependent shortcut enumeration is limited to n<=6")
    adjacent = adjacent_chain_edges(n)
    optional = optional_chain_shortcuts(n)
    points = []
    for count in range(len(optional) + 1):
        for chosen in combinations(optional, count):
            points.append(
                chain_shortcut_presentation_point(
                    n,
                    frozenset((*adjacent, *chosen)),
                )
            )
    return tuple(points)


def exact_chain_tc_spanner_pareto_frontier(
    chain_length: int,
) -> tuple[ChainShortcutPresentationPoint, ...]:
    points = enumerate_chain_tc_spanners(chain_length)
    return tuple(
        sorted(
            (
                point
                for point in points
                if not any(
                    shortcut_point_dominates(other, point)
                    for other in points
                    if other != point
                )
            ),
            key=lambda point: (point.stored_rules, point.diameter, sorted(point.edges)),
        )
    )


def translation_invariant_frontier_pairs(
    chain_length: int,
) -> frozenset[tuple[int, int]]:
    frontier: tuple[ChainPresentationPoint, ...] = exact_chain_jump_pareto_frontier(chain_length)
    return frozenset((point.stored_rules, point.full_closure_rounds) for point in frontier)


def unrestricted_frontier_pairs(
    chain_length: int,
) -> frozenset[tuple[int, int]]:
    frontier = exact_chain_tc_spanner_pareto_frontier(chain_length)
    return frozenset((point.stored_rules, point.diameter) for point in frontier)
