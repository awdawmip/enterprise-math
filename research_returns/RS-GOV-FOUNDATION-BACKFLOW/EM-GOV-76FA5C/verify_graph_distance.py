"""Finite independent recheck of the existing FQ-20260809-005 graph APIs.

Run with --source pointing to the frozen repository geometry.py. The Git blob
pin is checked before execution. This is finite test evidence, not a general
proof, Driver review, or Foundation admission.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

SOURCE_COMMIT = "3359e465daf353c0bda3a748fa9e98dd3c8e4e0b"
SOURCE_PATH = "src/enterprise_math/geometry.py"
EXPECTED_BLOB = "a1a8dc4d1ca53fde2ca00d9b944c1b8aa346a152"


def oracle(adjacency: dict[int, set[int]]) -> list[list[int | None]]:
    """Independent integer Floyd-Warshall; None denotes unreachable."""
    n = len(adjacency)
    d = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
        for j in adjacency[i]:
            if i != j:
                d[i][j] = 1
    for k, i, j in itertools.product(range(n), repeat=3):
        if d[i][k] is not None and d[k][j] is not None:
            v = d[i][k] + d[k][j]
            if d[i][j] is None or v < d[i][j]:
                d[i][j] = v
    return d


def verify(source: Path) -> dict:
    data = source.read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    if blob != EXPECTED_BLOB:
        raise ValueError(f"source pin mismatch: {blob}")
    spec = importlib.util.spec_from_file_location("verified_geometry", source)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load the pinned source module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    counts = dict(directed_graphs=0, undirected_graphs=0, directed_queries=0,
                  undirected_queries=0, negative_boundary_checks=0)
    for directed in (True, False):
        name = "directed" if directed else "undirected"
        function = module.directed_graph_distance if directed else module.graph_distance
        for n in range(1, 5):
            edges = [(i, j) for i in range(n) for j in range(n)
                     if (i != j if directed else i < j)]
            for mask in range(1 << len(edges)):
                adjacency = {i: set() for i in range(n)}
                for bit, (i, j) in enumerate(edges):
                    if mask & (1 << bit):
                        adjacency[i].add(j)
                        if not directed:
                            adjacency[j].add(i)
                expected = oracle(adjacency)
                counts[name + "_graphs"] += 1
                for i, j in itertools.product(range(n), repeat=2):
                    counts[name + "_queries"] += 1
                    try:
                        actual = function(adjacency, i, j)
                    except ValueError:
                        assert expected[i][j] is None, (name, n, mask, i, j)
                    else:
                        assert type(actual) is int and actual == expected[i][j], (
                            name, n, mask, i, j, actual, expected[i][j])
    negative = [
        (module.graph_distance, {0: {1}, 1: set()}, 0, 1, "symmetric"),
        (module.graph_distance, {0: {1}, 1: set()}, 0, 0, "symmetric"),
        (module.graph_distance, {0: {0}}, 0, 0, "loop-free"),
        (module.graph_distance, {0: {1}}, 0, 0, "closed"),
        (module.directed_graph_distance, {0: {1}}, 0, 0, "closed"),
        (module.graph_distance, {0: set()}, 1, 1, "present"),
        (module.directed_graph_distance, {0: set()}, 1, 1, "present"),
        (module.graph_distance, {0: set(), 1: {2}, 2: set()}, 0, 0, "symmetric"),
        (module.graph_distance, {0: set(), 1: {1}}, 0, 0, "loop-free"),
        (module.directed_graph_distance, {0: set(), 1: {2}}, 0, 0, "closed"),
    ]
    for function, adjacency, i, j, message in negative:
        try:
            function(adjacency, i, j)
        except ValueError as exc:
            assert message in str(exc), str(exc)
        else:
            raise AssertionError("invalid input was accepted")
        counts["negative_boundary_checks"] += 1
    assert module.directed_graph_distance({0: {0}}, 0, 0) == 0
    assert counts == dict(directed_graphs=4165, undirected_graphs=75,
                          directed_queries=66129, undirected_queries=1105,
                          negative_boundary_checks=10)
    return {
        "status": "PASS", "task_id": "RS-GOV-FOUNDATION-BACKFLOW",
        "question_id": "FQ-20260809-005", "source_commit": SOURCE_COMMIT,
        "source_path": SOURCE_PATH, "source_git_blob": blob,
        "source_sha256": hashlib.sha256(data).hexdigest(),
        "method": "existing BFS API against independent integer Floyd-Warshall",
        "domain": "all labelled loop-free directed and undirected graphs on 1..4 vertices",
        **counts, "directed_self_loop_zero_query": "PASS",
        "full_repository_regression": "NOT_RUN",
        "package_export_execution": "NOT_RUN",
        "general_theorem_proved": False, "driver_review": "NOT_GRANTED",
        "foundation_canonicalization": "NOT_GRANTED",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = json.dumps(verify(args.source), indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(result, encoding="utf-8")
    print(result, end="")


if __name__ == "__main__":
    main()
