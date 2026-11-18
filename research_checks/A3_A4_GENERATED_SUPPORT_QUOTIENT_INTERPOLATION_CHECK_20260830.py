#!/usr/bin/env python3
"""Exact bounded regression for RS-A3-A4-GENERATED-SUPPORT.

This checker verifies three query-typed boundaries without importing unpublished
branch code:

1. A3 weighted relation support factors pairwise through the exact normalized
   rational coordinate c_i / m_i.
2. A rank-one hidden scalar band is decided state-locally by its least absolute
   residue, but the 2x2 universal fine-support cancellation query has hidden
   rank two with Smith factors (1,2) and cannot be recovered from one coarse
   relation scalar.
3. Any connected undirected simple-graph shortest-step metric (the canonical
   intrinsic graph-metric contract used by Enterprise geometry) is exactly
   split-complete: R_r ; R_s = R_(r+s).
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from itertools import combinations
from math import gcd


def check_a3_normalization() -> int:
    checks = 0
    for m1 in range(1, 6):
        for m2 in range(1, 6):
            for c1 in range(-10, 11):
                for c2 in range(-10, 11):
                    z = m2 * c1 - m1 * c2
                    rho1 = Fraction(c1, m1)
                    rho2 = Fraction(c2, m2)
                    assert (z == 0) == (rho1 == rho2)
                    checks += 1
                    for radius in range(6):
                        assert (abs(z) <= radius * m1 * m2) == (
                            abs(rho1 - rho2) <= radius
                        )
                        checks += 1
    return checks


def least_absolute_residue(value: int, modulus: int) -> int:
    residue = value % modulus
    return min(residue, modulus - residue)


def check_rank_one_band_residue() -> int:
    checks = 0
    for step in range(1, 13):
        for base in range(-30, 31):
            nearest = least_absolute_residue(base, step)
            brute = min(abs(base + step * t) for t in range(-50, 51))
            assert nearest == brute
            checks += 1
            for radius in range(11):
                assert (nearest <= radius) == any(
                    abs(base + step * t) <= radius for t in range(-50, 51)
                )
                checks += 1
    return checks


def cross_relations_unit(state: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    c0, c1, c2, c3 = state
    return (c0 - c2, c0 - c3, c1 - c2, c1 - c3)


def coarse_relation_unit(state: tuple[int, int, int, int]) -> int:
    # A={0,1}, B={2,3}, both coarse capacities equal two.
    left_total = state[0] + state[1]
    right_total = state[2] + state[3]
    return 2 * left_total - 2 * right_total


def check_cancellation_module() -> int:
    checks = 0

    # W(a,-a,b,-b) = a*(1,1,-1,-1) + b*(-1,1,-1,1).
    generators = ((1, 1, -1, -1), (-1, 1, -1, 1))

    delta1 = 0
    for row in generators:
        for value in row:
            delta1 = gcd(delta1, abs(value))
    assert delta1 == 1
    checks += 1

    delta2 = 0
    for left, right in combinations(range(4), 2):
        det = (
            generators[0][left] * generators[1][right]
            - generators[0][right] * generators[1][left]
        )
        delta2 = gcd(delta2, abs(det))
    assert delta2 == 2
    checks += 1

    smith = (delta1, delta2 // delta1)
    assert smith == (1, 2)
    checks += 1

    # Same coarse state, opposite universal radius-zero fine-support truth.
    supported = (5, 5, 5, 5)
    cancelled = (0, 10, 0, 10)
    assert (sum(supported[:2]), sum(supported[2:])) == (10, 10)
    checks += 1
    assert (sum(cancelled[:2]), sum(cancelled[2:])) == (10, 10)
    checks += 1
    assert coarse_relation_unit(supported) == coarse_relation_unit(cancelled) == 0
    checks += 1
    assert all(value == 0 for value in cross_relations_unit(supported))
    checks += 1
    assert not all(value == 0 for value in cross_relations_unit(cancelled))
    checks += 1

    # Rank is two because the two generators are not rational multiples.
    assert generators[0][0] * generators[1][1] - generators[0][1] * generators[1][0] == 2
    checks += 1
    # Therefore coker has free rank 4-2=2 plus one Z/2 torsion factor.
    assert 4 - 2 == 2 and smith[1] == 2
    checks += 1
    return checks


def graph_distances(vertex_count: int, edge_mask: int) -> list[list[int]] | None:
    adjacency = [[] for _ in range(vertex_count)]
    bit = 0
    for left in range(vertex_count):
        for right in range(left + 1, vertex_count):
            if (edge_mask >> bit) & 1:
                adjacency[left].append(right)
                adjacency[right].append(left)
            bit += 1

    out: list[list[int]] = []
    for start in range(vertex_count):
        distance = [-1] * vertex_count
        distance[start] = 0
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            for neighbor in adjacency[vertex]:
                if distance[neighbor] < 0:
                    distance[neighbor] = distance[vertex] + 1
                    queue.append(neighbor)
        if any(value < 0 for value in distance):
            return None
        out.append(distance)
    return out


def split_complete_queries(distance: list[list[int]]) -> int:
    vertex_count = len(distance)
    diameter = max(max(row) for row in distance)
    checks = 0
    for start in range(vertex_count):
        for goal in range(vertex_count):
            endpoint = distance[start][goal]
            for left_radius in range(diameter + 1):
                for right_radius in range(diameter + 1):
                    total_supported = endpoint <= left_radius + right_radius
                    has_intermediate = any(
                        distance[start][middle] <= left_radius
                        and distance[middle][goal] <= right_radius
                        for middle in range(vertex_count)
                    )
                    assert total_supported == has_intermediate
                    checks += 1
    return checks


def distance_from_edges(
    vertex_count: int, edges: set[tuple[int, int]]
) -> list[list[int]]:
    normalized = {tuple(sorted(edge)) for edge in edges}
    mask = 0
    bit = 0
    for left in range(vertex_count):
        for right in range(left + 1, vertex_count):
            if (left, right) in normalized:
                mask |= 1 << bit
            bit += 1
    distance = graph_distances(vertex_count, mask)
    assert distance is not None
    return distance


def check_intrinsic_graph_metrics() -> tuple[int, int, dict[int, int], dict[str, int]]:
    checks = 0
    connected_graphs = 0
    by_order: dict[int, int] = {}
    for vertex_count in range(2, 6):
        edge_count = vertex_count * (vertex_count - 1) // 2
        local_count = 0
        for edge_mask in range(1 << edge_count):
            distance = graph_distances(vertex_count, edge_mask)
            if distance is None:
                continue
            local_count += 1
            connected_graphs += 1
            checks += split_complete_queries(distance)
        by_order[vertex_count] = local_count

    representatives = {
        "path6": distance_from_edges(6, {(i, i + 1) for i in range(5)}),
        "cycle6": distance_from_edges(
            6, {tuple(sorted((i, (i + 1) % 6))) for i in range(6)}
        ),
        "grid3x3": distance_from_edges(
            9,
            {
                tuple(sorted((3 * i + j, 3 * (i + 1) + j)))
                for i in range(2)
                for j in range(3)
            }
            | {
                tuple(sorted((3 * i + j, 3 * i + j + 1)))
                for i in range(3)
                for j in range(2)
            },
        ),
    }
    representative_checks: dict[str, int] = {}
    for name, distance in representatives.items():
        count = split_complete_queries(distance)
        representative_checks[name] = count
        checks += count
    return checks, connected_graphs, by_order, representative_checks


def main() -> None:
    a3_checks = check_a3_normalization()
    band_checks = check_rank_one_band_residue()
    cancellation_checks = check_cancellation_module()
    graph_checks, graph_count, by_order, representatives = check_intrinsic_graph_metrics()
    total = a3_checks + band_checks + cancellation_checks + graph_checks
    print(
        "PASS "
        f"checks={total} "
        f"a3={a3_checks} "
        f"rank1_band={band_checks} "
        f"cancellation={cancellation_checks} "
        f"graph={graph_checks} "
        f"connected_graphs={graph_count} "
        f"by_order={by_order} "
        f"representatives={representatives}"
    )


if __name__ == "__main__":
    main()
