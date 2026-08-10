"""Workload-weighted exact shortcut presentations for a unary implication chain.

Worst-case directed diameter is only one possible execution contract.  If a
Stage131 system sees a nonuniform distribution of premise/target queries, an
exact presentation can instead minimize weighted or expected shortest-path
length while preserving the same semantic closure law.

For query weights mu(i,j)>=0 on comparable pairs i<j, define total execution cost

    C_E(mu) = sum_(i<j) mu(i,j) * dist_E(i,j)

and expected depth by dividing by total query mass.

Starting from adjacent chain edges, add one shortcut a->b.  A query i->j can use
that shortcut iff i<=a and b<=j.  When it can, the shortcut saves exactly

    b-a-1

hops, independent of i,j.  Therefore the exact weighted benefit is

    Gain_mu(a,b)
      = (b-a-1) * sum_(i<=a, j>=b) mu(i,j).

So the optimal one-shortcut workload presentation is obtained by maximizing a
simple shortcut-length x query-rectangle-mass score.

For uniform all-pairs workload, put

    x=a+1, y=b-a-1, z=n-b+1.

Then x,y,z are positive and sum to n+1, while the total gain is exactly xyz.
Hence the optimal uniform one-shortcut locations are the integer triples as
balanced as possible around (n+1)/3.

This objective can differ radically from worst-case diameter.  If all workload
mass lies on one pair i->j, the optimal shortcut is exactly i->j and makes that
query one round, even though global diameter may remain large.

Shortest-path workload optimization and graph shortcuts are standard prior
mathematics/CS.  The project value is the Stage131 future-language point: cached
transitive rules should be optimized against the declared execution/query
contract, not against one universal notion of rule redundancy.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from typing import Mapping

from .stage131_chain_tc_spanner import (
    ChainShortcutPresentationPoint,
    Edge,
    adjacent_chain_edges,
    chain_shortest_path_lengths,
    chain_shortcut_presentation_point,
    optional_chain_shortcuts,
)


Query = tuple[int, int]
QueryWeights = Mapping[Query, int | Fraction]


def _positive_int(value: int, *, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def normalize_query_weights(chain_length: int, weights: QueryWeights) -> dict[Query, Fraction]:
    n = _positive_int(chain_length, name="chain_length")
    result: dict[Query, Fraction] = {}
    total = Fraction(0)
    for query, raw_weight in weights.items():
        if not isinstance(query, tuple) or len(query) != 2:
            raise TypeError("query keys must be (source,target) pairs")
        source, target = query
        if (
            isinstance(source, bool)
            or not isinstance(source, int)
            or isinstance(target, bool)
            or not isinstance(target, int)
        ):
            raise TypeError("query endpoints must be integers")
        if not (0 <= source < target <= n):
            raise ValueError("query must be a comparable chain pair i<j")
        weight = Fraction(raw_weight)
        if weight < 0:
            raise ValueError("query weights must be nonnegative")
        if weight == 0:
            continue
        result[(source, target)] = result.get((source, target), Fraction(0)) + weight
        total += weight
    if total <= 0:
        raise ValueError("query workload must have positive total mass")
    return result


def uniform_all_pairs_workload(chain_length: int) -> dict[Query, Fraction]:
    n = _positive_int(chain_length, name="chain_length")
    return {
        (source, target): Fraction(1)
        for source in range(n)
        for target in range(source + 1, n + 1)
    }


def single_query_workload(
    chain_length: int,
    source: int,
    target: int,
) -> dict[Query, Fraction]:
    n = _positive_int(chain_length, name="chain_length")
    if not (0 <= source < target <= n):
        raise ValueError("single query must satisfy 0<=source<target<=chain_length")
    return {(source, target): Fraction(1)}


def query_total_mass(chain_length: int, weights: QueryWeights) -> Fraction:
    normalized = normalize_query_weights(chain_length, weights)
    return sum(normalized.values(), Fraction(0))


def adjacent_workload_total_cost(chain_length: int, weights: QueryWeights) -> Fraction:
    normalized = normalize_query_weights(chain_length, weights)
    return sum(
        weight * (target - source)
        for (source, target), weight in normalized.items()
    )


def workload_total_cost(
    chain_length: int,
    edges: set[Edge] | frozenset[Edge],
    weights: QueryWeights,
) -> Fraction:
    n = _positive_int(chain_length, name="chain_length")
    normalized = normalize_query_weights(n, weights)
    distances = chain_shortest_path_lengths(n, edges)
    total = Fraction(0)
    for (source, target), weight in normalized.items():
        distance = distances[source][target]
        if distance is None:
            raise ValueError("presentation does not preserve required chain reachability")
        total += weight * distance
    return total


def workload_expected_depth(
    chain_length: int,
    edges: set[Edge] | frozenset[Edge],
    weights: QueryWeights,
) -> Fraction:
    normalized = normalize_query_weights(chain_length, weights)
    total_mass = sum(normalized.values(), Fraction(0))
    total_cost = workload_total_cost(chain_length, edges, normalized)
    return total_cost / total_mass


def one_shortcut_rectangle_mass(
    chain_length: int,
    weights: QueryWeights,
    source: int,
    target: int,
) -> Fraction:
    n = _positive_int(chain_length, name="chain_length")
    normalized = normalize_query_weights(n, weights)
    if not (0 <= source < target <= n) or target - source < 2:
        raise ValueError("shortcut must skip at least one chain edge")
    return sum(
        weight
        for (query_source, query_target), weight in normalized.items()
        if query_source <= source and target <= query_target
    )


def one_shortcut_weighted_gain(
    chain_length: int,
    weights: QueryWeights,
    source: int,
    target: int,
) -> Fraction:
    mass = one_shortcut_rectangle_mass(
        chain_length,
        weights,
        source,
        target,
    )
    return Fraction(target - source - 1) * mass


def one_shortcut_total_cost_closed(
    chain_length: int,
    weights: QueryWeights,
    source: int,
    target: int,
) -> Fraction:
    baseline = adjacent_workload_total_cost(chain_length, weights)
    return baseline - one_shortcut_weighted_gain(
        chain_length,
        weights,
        source,
        target,
    )


@dataclass(frozen=True)
class WorkloadShortcutPoint:
    chain_length: int
    edges: frozenset[Edge]
    stored_rules: int
    worst_case_diameter: int
    total_query_mass: Fraction
    total_weighted_depth: Fraction
    expected_depth: Fraction

    @property
    def shortcut_count(self) -> int:
        return self.stored_rules - self.chain_length


def workload_shortcut_point(
    chain_length: int,
    edges: set[Edge] | frozenset[Edge],
    weights: QueryWeights,
) -> WorkloadShortcutPoint:
    n = _positive_int(chain_length, name="chain_length")
    normalized = normalize_query_weights(n, weights)
    graph_point: ChainShortcutPresentationPoint = chain_shortcut_presentation_point(n, edges)
    mass = sum(normalized.values(), Fraction(0))
    total = workload_total_cost(n, graph_point.edges, normalized)
    return WorkloadShortcutPoint(
        chain_length=n,
        edges=graph_point.edges,
        stored_rules=graph_point.stored_rules,
        worst_case_diameter=graph_point.diameter,
        total_query_mass=mass,
        total_weighted_depth=total,
        expected_depth=total / mass,
    )


def optimal_one_shortcut_for_workload(
    chain_length: int,
    weights: QueryWeights,
) -> WorkloadShortcutPoint:
    n = _positive_int(chain_length, name="chain_length")
    normalized = normalize_query_weights(n, weights)
    baseline = adjacent_chain_edges(n)
    candidates = []
    for source, target in optional_chain_shortcuts(n):
        gain = one_shortcut_weighted_gain(n, normalized, source, target)
        point = workload_shortcut_point(
            n,
            frozenset((*baseline, (source, target))),
            normalized,
        )
        closed_cost = one_shortcut_total_cost_closed(
            n,
            normalized,
            source,
            target,
        )
        if point.total_weighted_depth != closed_cost:
            raise AssertionError("one-shortcut workload cost disagreed with rectangle-gain theorem")
        candidates.append((gain, point))
    if not candidates:
        return workload_shortcut_point(n, baseline, normalized)
    # Maximize gain / minimize expected depth.  Ties prefer smaller diameter,
    # then lexicographically earlier shortcut placement for deterministic output.
    return min(
        (point for _gain, point in candidates),
        key=lambda point: (
            point.total_weighted_depth,
            point.worst_case_diameter,
            sorted(point.edges),
        ),
    )


def uniform_one_shortcut_gain_closed(
    chain_length: int,
    source: int,
    target: int,
) -> int:
    n = _positive_int(chain_length, name="chain_length")
    if not (0 <= source < target <= n) or target - source < 2:
        raise ValueError("shortcut must skip at least one edge")
    x = source + 1
    y = target - source - 1
    z = n - target + 1
    return x * y * z


def balanced_three_partitions(total: int) -> tuple[tuple[int, int, int], ...]:
    s = _positive_int(total, name="total")
    best_product = -1
    best = []
    for x in range(1, s - 1):
        for y in range(1, s - x):
            z = s - x - y
            if z <= 0:
                continue
            product_value = x * y * z
            if product_value > best_product:
                best_product = product_value
                best = [(x, y, z)]
            elif product_value == best_product:
                best.append((x, y, z))
    return tuple(best)


def optimal_uniform_one_shortcuts(chain_length: int) -> tuple[Edge, ...]:
    n = _positive_int(chain_length, name="chain_length")
    if n == 1:
        return ()
    triples = balanced_three_partitions(n + 1)
    edges = {
        (x - 1, x + y)
        for x, y, _z in triples
        if y >= 1
    }
    return tuple(sorted(edges))


def uniform_adjacent_expected_depth(chain_length: int) -> Fraction:
    n = _positive_int(chain_length, name="chain_length")
    return Fraction(n + 2, 3)


def optimal_uniform_one_shortcut_expected_depth(chain_length: int) -> Fraction:
    n = _positive_int(chain_length, name="chain_length")
    workload = uniform_all_pairs_workload(n)
    point = optimal_one_shortcut_for_workload(n, workload)
    return point.expected_depth


def best_shortcut_set_under_rule_budget(
    chain_length: int,
    weights: QueryWeights,
    stored_rule_budget: int,
) -> WorkloadShortcutPoint:
    n = _positive_int(chain_length, name="chain_length")
    if isinstance(stored_rule_budget, bool) or not isinstance(stored_rule_budget, int):
        raise TypeError("stored_rule_budget must be an integer")
    if stored_rule_budget < n:
        raise ValueError("budget cannot omit forced adjacent chain edges")
    optional_budget = stored_rule_budget - n
    optional = optional_chain_shortcuts(n)
    if n > 7:
        raise ValueError("exact workload shortcut-set enumeration is limited to n<=7")
    if optional_budget > len(optional):
        optional_budget = len(optional)
    adjacent = adjacent_chain_edges(n)
    best = workload_shortcut_point(n, adjacent, weights)
    for count in range(1, optional_budget + 1):
        for chosen in combinations(optional, count):
            point = workload_shortcut_point(
                n,
                frozenset((*adjacent, *chosen)),
                weights,
            )
            if (
                point.total_weighted_depth,
                point.worst_case_diameter,
                point.stored_rules,
                sorted(point.edges),
            ) < (
                best.total_weighted_depth,
                best.worst_case_diameter,
                best.stored_rules,
                sorted(best.edges),
            ):
                best = point
    return best


def workload_budget_curve(
    chain_length: int,
    weights: QueryWeights,
) -> tuple[WorkloadShortcutPoint, ...]:
    n = _positive_int(chain_length, name="chain_length")
    if n > 7:
        raise ValueError("exact workload budget curve is limited to n<=7")
    maximum = len(transitive_edges := frozenset(
        (source, target)
        for source in range(n + 1)
        for target in range(source + 1, n + 1)
    ))
    points = []
    last_key = None
    for budget in range(n, maximum + 1):
        point = best_shortcut_set_under_rule_budget(n, weights, budget)
        key = (point.total_weighted_depth, point.stored_rules)
        if key != last_key:
            points.append(point)
            last_key = key
    return tuple(points)
