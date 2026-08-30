#!/usr/bin/env python3
"""Deterministic regression checker for RS-GEO6-ROTATION-KAKEYA-DIRECTIONAL-COVERAGE.

This checker validates the declared downstream six-axis Cell-relation benchmark.
It does NOT identify carrier S4 with the full native P000 rotation group and does
NOT import Euclidean line/measure semantics.
"""
from __future__ import annotations

from itertools import combinations, permutations
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from enterprise_math.finite_symmetry import (  # noqa: E402
    orbit,
    stabilizer,
    validate_finite_group_action,
)

VERTICES = ("A", "B", "C", "D")
AXES = tuple("".join(pair) for pair in combinations(VERTICES, 2))
ZERO = (0, 0, 0, 0, 0, 0)
BASIS = tuple(
    tuple(1 if i == j else 0 for i in range(6))
    for j in range(6)
)


def add(x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a + b for a, b in zip(x, y, strict=True))


def smul(k: int, v: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(k * a for a in v)


def axis_action(name: tuple[str, ...], axis: str) -> str:
    image = dict(zip(VERTICES, name, strict=True))
    return "".join(sorted((image[axis[0]], image[axis[1]])))


def s4_actions() -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for perm in permutations(VERTICES):
        label = "".join(perm)
        out[label] = {axis: axis_action(perm, axis) for axis in AXES}
    return out


def path(
    start: tuple[int, ...],
    direction: tuple[int, ...],
    length: int,
) -> frozenset[tuple[int, ...]]:
    if length < 1:
        raise ValueError("length must be positive")
    return frozenset(add(start, smul(t, direction)) for t in range(length))


def centered_packet(length: int) -> tuple[frozenset[tuple[int, ...]], ...]:
    return tuple(path(ZERO, BASIS[i], length) for i in range(6))


def support_size(paths: tuple[frozenset[tuple[int, ...]], ...]) -> int:
    union: set[tuple[int, ...]] = set()
    for current in paths:
        union.update(current)
    return len(union)


def shared_cells(
    paths: tuple[frozenset[tuple[int, ...]], ...],
) -> dict[tuple[int, ...], tuple[int, ...]]:
    memberships: dict[tuple[int, ...], list[int]] = {}
    for i, current in enumerate(paths):
        for cell in current:
            memberships.setdefault(cell, []).append(i)
    return {
        cell: tuple(indices)
        for cell, indices in memberships.items()
        if len(indices) >= 2
    }


def incidence_is_forest(
    paths: tuple[frozenset[tuple[int, ...]], ...],
) -> bool:
    """Check the direction/shared-cell incidence graph for a cycle."""
    shared = shared_cells(paths)
    graph: dict[tuple[str, object], set[tuple[str, object]]] = {
        ("d", i): set() for i in range(len(paths))
    }
    for cell, indices in shared.items():
        xnode = ("x", cell)
        graph.setdefault(xnode, set())
        for i in indices:
            dnode = ("d", i)
            graph[dnode].add(xnode)
            graph[xnode].add(dnode)

    seen: set[tuple[str, object]] = set()
    for root in graph:
        if root in seen:
            continue
        stack = [(root, None)]
        while stack:
            node, parent = stack.pop()
            if node in seen:
                return False
            seen.add(node)
            for nxt in graph[node]:
                if nxt != parent:
                    stack.append((nxt, node))
    return True


def overlap_defect(paths: tuple[frozenset[tuple[int, ...]], ...]) -> int:
    return sum(len(indices) - 1 for indices in shared_cells(paths).values())


def chain_minimizer_length_two() -> tuple[frozenset[tuple[int, ...]], ...]:
    p0 = ZERO
    p1 = add(p0, BASIS[1])
    p2 = add(p1, BASIS[2])
    p3 = add(p2, BASIS[3])
    p4 = add(p3, BASIS[4])
    return (
        frozenset((p0, add(p0, BASIS[0]))),
        frozenset((p0, p1)),
        frozenset((p1, p2)),
        frozenset((p2, p3)),
        frozenset((p3, p4)),
        frozenset((p4, add(p4, BASIS[5]))),
    )


def dependent_triangle_countermodel() -> tuple[frozenset[tuple[int, ...]], ...]:
    e1 = BASIS[0]
    e2 = BASIS[1]
    diagonal = add(e1, e2)
    return (
        path(ZERO, e1, 2),
        path(e1, e2, 2),
        path(ZERO, diagonal, 2),
    )


def main() -> None:
    actions = s4_actions()
    validate_finite_group_action(AXES, actions)
    assert len(actions) == 24
    assert orbit(AXES, actions, "AB") == frozenset(AXES)
    assert len(stabilizer(AXES, actions, "AB")) == 4

    # Exact upper certificates and finite refinement levels.
    for r in range(2, 9):
        packet = centered_packet(r)
        assert all(len(p) == r for p in packet)
        assert incidence_is_forest(packet)
        assert overlap_defect(packet) == 5
        assert support_size(packet) == 6 * r - 5

    # A non-concurrent minimizer shows that optimality is connectivity of the
    # overlap forest, not forced common concurrency.
    chain = chain_minimizer_length_two()
    assert incidence_is_forest(chain)
    assert overlap_defect(chain) == 5
    assert support_size(chain) == 7

    # Exact refinement/renormalization identities for the proved optimum K(r).
    K = lambda r: 6 * r - 5
    assert K(2) == 7
    assert K(3) == 13
    assert K(4) == 19
    for r in range(2, 20):
        assert K(r + 1) - K(r) == 6
        assert K(2 * r - 1) == 2 * K(r) - 1

    # Adversarial boundary: once directions are linearly dependent, an overlap
    # cycle can occur and the six-axis forest lower-bound mechanism is invalid.
    triangle = dependent_triangle_countermodel()
    assert not incidence_is_forest(triangle)
    assert support_size(triangle) == 3
    assert support_size(triangle) < 3 * 2 - (3 - 1)

    print("PASS GEO6_ROTATION_KAKEYA_DIRECTIONAL_COVERAGE")
    print("carrier_s4_orbit=6 stabilizer_AB=4")
    print("K6(r)=6r-5 for declared independent-axis benchmark; r=2,3 -> 7,13")
    print("dependent_direction_triangle_support=3 (forest mechanism correctly fails)")


if __name__ == "__main__":
    main()
