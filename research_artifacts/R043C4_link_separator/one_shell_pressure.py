#!/usr/bin/env python3
"""Targeted one-shell pressure for the unique R043-C4 octahedral separator.

This is not a generic animal census.  For each frozen close-packed world it fixes
one exact octahedral opposite-pair separator, occupies its connected equator-4,
and tests every extension obtained by occupying at most four of the 24 initial
outer-frontier sites.  Every such extension remains connected because each added
site was already adjacent to the equator-4 base.
"""
from __future__ import annotations

from itertools import combinations

Point = tuple[int, int, int]
FCC_DIRS = tuple(sorted(
    [(a, b, 0) for a in (-1, 1) for b in (-1, 1)]
    + [(a, 0, b) for a in (-1, 1) for b in (-1, 1)]
    + [(0, a, b) for a in (-1, 1) for b in (-1, 1)]
))
TRI_DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1))


def fcc_neighbors(p: Point) -> tuple[Point, ...]:
    x, y, z = p
    return tuple((x + a, y + b, z + c) for a, b, c in FCC_DIRS)


def hcp_neighbors(p: Point) -> tuple[Point, ...]:
    i, j, k = p
    out = [(i + di, j + dj, k) for di, dj in TRI_DIRS]
    offsets = ((0, 0), (-1, 0), (0, -1)) if k % 2 == 0 else ((0, 0), (1, 0), (0, 1))
    for dk in (-1, 1):
        for di, dj in offsets:
            out.append((i + di, j + dj, k + dk))
    return tuple(out)


def octahedra_through_origin(neighbors):
    o = (0, 0, 0)
    n1 = set(neighbors(o))
    n2 = set()
    for x in n1:
        n2.update(neighbors(x))
    out = []
    for q in sorted(n2 - n1 - {o}):
        common = n1 & set(neighbors(q))
        cell = {o, q} | common
        if len(common) == 4 and all(sum(w in cell for w in neighbors(v)) == 4 for v in cell):
            out.append((q, tuple(sorted(common))))
    return out


def frontier(c: set[Point], neighbors) -> set[Point]:
    return {q for p in c for q in neighbors(p) if q not in c}


def connected_in(nodes: set[Point], neighbors, s: Point, t: Point) -> bool:
    if s not in nodes or t not in nodes:
        return False
    seen = {s}
    queue = [s]
    for x in queue:
        if x == t:
            return True
        for y in neighbors(x):
            if y in nodes and y not in seen:
                seen.add(y)
                queue.append(y)
    return t in seen


def run_world(name: str, neighbors) -> dict[str, int | str]:
    u = (0, 0, 0)
    v, equator = octahedra_through_origin(neighbors)[0]
    base = set(equator)
    pool = sorted(frontier(base, neighbors) - {u, v})
    assert len(pool) == 24
    total = 0
    disconnects = 0
    by_added = {}
    for k in range(5):
        count = 0
        for extra in combinations(pool, k):
            count += 1
            total += 1
            c = base | set(extra)
            f = frontier(c, neighbors)
            if not connected_in(f, neighbors, u, v):
                disconnects += 1
        by_added[k] = count
    assert by_added == {0: 1, 1: 24, 2: 276, 3: 2024, 4: 10626}
    assert total == 12951
    assert disconnects == 0
    return {
        "world": name,
        "initial_outer_frontier_pool": len(pool),
        "extensions_tested": total,
        "frontier_disconnects": disconnects,
        "max_added_sites": 4,
    }


def main() -> int:
    print(run_world("FCC", fcc_neighbors))
    print(run_world("HCP", hcp_neighbors))
    print("PASS R043-C4 targeted one-shell pressure")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
