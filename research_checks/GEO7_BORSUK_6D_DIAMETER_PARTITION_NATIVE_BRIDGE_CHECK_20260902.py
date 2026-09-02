#!/usr/bin/env python3
"""Deterministic finite checker for
RS-GEO7-BORSUK-6D-DIAMETER-PARTITION-NATIVE-BRIDGE.

The checker certifies only finite exact statements:
1. for every nonempty simple graph G on six fixed labels, the 0/1/2 distance
   d_G is a genuine metric and has maximum-distance graph exactly G;
2. the strict-smaller-diameter partition number computed by exhaustive set
   partitions equals the chromatic number computed independently by coloring;
3. the declared C5+isolated six-label model has Borsuk number 3;
4. a same-label/same-readout matching model has Borsuk number 2;
5. the existing project graph_distance helper gives the expected connected
   path-metric reduction on C5.

No Euclidean realization claim is made by this checker.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from enterprise_math.geometry import graph_distance  # noqa: E402

N = 6
VERTICES = tuple(range(1, N + 1))
PAIRS = tuple(combinations(VERTICES, 2))
PAIR_INDEX = {pair: i for i, pair in enumerate(PAIRS)}
ALL_EDGE_MASK = (1 << len(PAIRS)) - 1


def normalize_pair(a: int, b: int) -> tuple[int, int]:
    return (a, b) if a < b else (b, a)


def edge_set(mask: int) -> set[tuple[int, int]]:
    return {pair for i, pair in enumerate(PAIRS) if (mask >> i) & 1}


def mask_from_edges(edges: set[tuple[int, int]]) -> int:
    mask = 0
    for a, b in edges:
        pair = normalize_pair(a, b)
        if pair not in PAIR_INDEX:
            raise ValueError(f"invalid edge {pair}")
        mask |= 1 << PAIR_INDEX[pair]
    return mask


def metric_from_mask(mask: int) -> dict[tuple[int, int], int]:
    """0 on the diagonal, 2 on graph edges, 1 on distinct nonedges."""
    edges = edge_set(mask)
    return {
        (a, b): (
            0
            if a == b
            else 2
            if normalize_pair(a, b) in edges
            else 1
        )
        for a in VERTICES
        for b in VERTICES
    }


def validate_metric(distance: dict[tuple[int, int], int]) -> None:
    for a in VERTICES:
        if distance[a, a] != 0:
            raise AssertionError("diagonal failure")
        for b in VERTICES:
            if distance[a, b] != distance[b, a]:
                raise AssertionError("symmetry failure")
            if a != b and distance[a, b] <= 0:
                raise AssertionError("positive separation failure")
            for c in VERTICES:
                if distance[a, b] > distance[a, c] + distance[c, b]:
                    raise AssertionError(("triangle failure", a, b, c))


def diameter_and_graph_mask(
    distance: dict[tuple[int, int], int]
) -> tuple[int, int]:
    diameter = max(distance[a, b] for a in VERTICES for b in VERTICES)
    mask = 0
    for i, (a, b) in enumerate(PAIRS):
        if distance[a, b] == diameter:
            mask |= 1 << i
    return diameter, mask


def restricted_growth_partitions() -> tuple[tuple[tuple[int, ...], ...], ...]:
    """Enumerate the Bell(6)=203 unlabeled set partitions deterministically."""
    assignment = [0] * N
    output: list[tuple[tuple[int, ...], ...]] = []

    def rec(i: int, max_label: int) -> None:
        if i == N:
            k = max(assignment) + 1
            blocks = [[] for _ in range(k)]
            for idx, label in enumerate(assignment):
                blocks[label].append(VERTICES[idx])
            output.append(tuple(tuple(block) for block in blocks))
            return
        for label in range(max_label + 2):
            assignment[i] = label
            rec(i + 1, max(max_label, label))

    assignment[0] = 0
    rec(1, 0)
    return tuple(output)


PARTITIONS = restricted_growth_partitions()


def block_diameter(
    block: tuple[int, ...],
    distance: dict[tuple[int, int], int],
) -> int:
    if len(block) <= 1:
        return 0
    return max(distance[a, b] for a, b in combinations(block, 2))


def borsuk_number_by_partitions(
    distance: dict[tuple[int, int], int]
) -> tuple[int, tuple[tuple[int, ...], ...]]:
    diameter, _ = diameter_and_graph_mask(distance)
    if diameter <= 0:
        raise ValueError("positive diameter required")
    for partition in sorted(PARTITIONS, key=lambda p: (len(p), p)):
        if all(block_diameter(block, distance) < diameter for block in partition):
            return len(partition), partition
    raise AssertionError("singleton partition must always work")


def chromatic_number(mask: int) -> tuple[int, tuple[int, ...]]:
    edges = edge_set(mask)
    adjacency = {v: set() for v in VERTICES}
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    order = tuple(sorted(VERTICES, key=lambda v: (-len(adjacency[v]), v)))

    for k in range(1, N + 1):
        colors = {v: -1 for v in VERTICES}

        def rec(i: int) -> bool:
            if i == N:
                return True
            v = order[i]
            forbidden = {colors[u] for u in adjacency[v] if colors[u] >= 0}
            for color in range(k):
                if color in forbidden:
                    continue
                colors[v] = color
                if rec(i + 1):
                    return True
                colors[v] = -1
            return False

        if rec(0):
            return k, tuple(colors[v] for v in VERTICES)
    raise AssertionError("n colors always suffice")


def graph_distance_metric(
    adjacency: dict[int, set[int]]
) -> dict[tuple[int, int], int]:
    return {
        (a, b): graph_distance(adjacency, a, b)
        for a in VERTICES
        for b in VERTICES
    }


def run() -> dict[str, object]:
    if len(PARTITIONS) != 203:
        raise AssertionError(("Bell(6) regression", len(PARTITIONS)))

    counts: Counter[int] = Counter()
    for mask in range(1, ALL_EDGE_MASK + 1):  # empty graph excluded
        distance = metric_from_mask(mask)
        validate_metric(distance)
        diameter, recovered = diameter_and_graph_mask(distance)
        if diameter != 2 or recovered != mask:
            raise AssertionError(("maximum-distance realization failure", mask))
        borsuk, _ = borsuk_number_by_partitions(distance)
        chromatic, _ = chromatic_number(mask)
        if borsuk != chromatic:
            raise AssertionError(("Borsuk/chromatic mismatch", mask, borsuk, chromatic))
        counts[borsuk] += 1

    c5_edges = {
        (1, 2), (2, 3), (3, 4), (4, 5), (1, 5)
    }
    matching_edges = {(1, 2), (3, 4), (5, 6)}
    k6_edges = set(PAIRS)

    examples: dict[str, object] = {}
    for name, edges, expected in (
        ("C5_PLUS_ISOLATED", c5_edges, 3),
        ("PERFECT_MATCHING", matching_edges, 2),
        ("K6", k6_edges, 6),
    ):
        mask = mask_from_edges(edges)
        distance = metric_from_mask(mask)
        borsuk, partition = borsuk_number_by_partitions(distance)
        chromatic, coloring = chromatic_number(mask)
        if borsuk != expected or chromatic != expected:
            raise AssertionError((name, borsuk, chromatic, expected))
        examples[name] = {
            "edge_mask": mask,
            "edges": [list(edge) for edge in sorted(edges)],
            "borsuk_number": borsuk,
            "chromatic_number": chromatic,
            "strict_partition": [list(block) for block in partition],
            "proper_coloring_by_vertex_1_to_6": list(coloring),
        }

    if examples["C5_PLUS_ISOLATED"]["borsuk_number"] == examples["PERFECT_MATCHING"]["borsuk_number"]:
        raise AssertionError("same-readout countermodel failed to separate Borsuk number")

    c6_adj = {
        1: {2, 6},
        2: {1, 3},
        3: {2, 4},
        4: {3, 5},
        5: {4, 6},
        6: {5, 1},
    }
    path_distance = graph_distance_metric(c6_adj)
    path_diameter, path_max_mask = diameter_and_graph_mask(path_distance)
    path_borsuk, path_partition = borsuk_number_by_partitions(path_distance)
    path_chromatic, _ = chromatic_number(path_max_mask)
    if path_diameter != 3 or path_borsuk != 2 or path_chromatic != 2:
        raise AssertionError(
            ("C6 graph-metric regression", path_diameter, path_borsuk, path_chromatic)
        )

    return {
        "schema": "GEO7_BORSUK_6D_FINITE_CERTIFICATE_V1",
        "labels": list(VERTICES),
        "nonempty_simple_graphs_checked": ALL_EDGE_MASK,
        "set_partitions_enumerated": len(PARTITIONS),
        "partition_search_policy": "restricted-growth partitions ordered by block count; stop at the first strict-diameter partition",
        "empty_graph_excluded_reason": "a positive-diameter finite metric on at least two points must have at least one maximum-distance pair",
        "metric_failures": 0,
        "maximum_distance_graph_failures": 0,
        "borsuk_chromatic_mismatches": 0,
        "borsuk_number_distribution_over_nonempty_graph_metrics": {
            str(k): counts[k] for k in sorted(counts)
        },
        "realized_positive_diameter_borsuk_numbers": sorted(counts),
        "examples": examples,
        "same_six_label_same_readout_countermodel": {
            "readout": {"type": "AXIS_LABEL", "values": list(VERTICES)},
            "model_A": "C5_PLUS_ISOLATED",
            "model_B": "PERFECT_MATCHING",
            "borsuk_numbers": [
                examples["C5_PLUS_ISOLATED"]["borsuk_number"],
                examples["PERFECT_MATCHING"]["borsuk_number"],
            ],
            "conclusion": "six labels/readout do not determine the metric, maximum-distance graph, or Borsuk number",
        },
        "path_metric_reuse_regression": {
            "relation": "C6 undirected cycle",
            "diameter": path_diameter,
            "maximum_distance_edges": [
                list(edge) for edge in sorted(edge_set(path_max_mask))
            ],
            "borsuk_number": path_borsuk,
            "strict_partition": [list(block) for block in path_partition],
            "project_helper": "enterprise_math.geometry.graph_distance",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    certificate = run()
    if args.json:
        print(json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(
            "PASS GEO7 finite Borsuk bridge:",
            f"graphs={certificate['nonempty_simple_graphs_checked']}",
            f"partitions={certificate['set_partitions_enumerated']}",
            f"realized_b={certificate['realized_positive_diameter_borsuk_numbers']}",
            f"mismatches={certificate['borsuk_chromatic_mismatches']}",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
