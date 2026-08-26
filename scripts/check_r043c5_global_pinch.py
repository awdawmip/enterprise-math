#!/usr/bin/env python3
"""Exact local/regression certificate for R043-C5.

This checker does not attempt to certify Alexander duality computationally.
It verifies the finite native incidence hypotheses used by the proof:
- exact FCC/HCP 12-contact models;
- local Delaunay cells through a site are 8 tetrahedra + 6 octahedra;
- every native triangle through the site is a triangular face of exactly two
  local 3-cells;
- the codimension-two binary cut parity is 0-or-2, with the two Omega-side
  endpoints equal or native adjacent;
- C4 tetra/octa coloring classification and minimal/one-shell regressions.
No floating point or generic animal census is used.
"""
from __future__ import annotations

from collections import deque
from itertools import combinations, product

Point = tuple[int, int, int]

FCC_DIRS: tuple[Point, ...] = tuple(sorted(
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


def hcp_phase_swap(p: Point) -> Point:
    i, j, k = p
    return (-i, -j, k + 1)


def tetrahedra_through_origin(neighbors) -> list[tuple[Point, ...]]:
    o = (0, 0, 0)
    out = []
    for tri in combinations(neighbors(o), 3):
        cell = (o,) + tri
        if all(b in neighbors(a) for a, b in combinations(cell, 2)):
            out.append(tuple(sorted(cell)))
    return sorted(set(out))


def octahedra_through_origin(neighbors) -> list[tuple[Point, ...]]:
    o = (0, 0, 0)
    n1 = set(neighbors(o))
    n2: set[Point] = set()
    for x in n1:
        n2.update(neighbors(x))
    out = []
    for q in sorted(n2 - n1 - {o}):
        common = n1 & set(neighbors(q))
        cell = {o, q} | common
        if len(common) == 4 and all(sum(w in cell for w in neighbors(v)) == 4 for v in cell):
            out.append(tuple(sorted(cell)))
    return out


def triangle_cliques_through_origin(neighbors) -> set[tuple[Point, ...]]:
    o = (0, 0, 0)
    return {
        tuple(sorted((o, a, b)))
        for a, b in combinations(neighbors(o), 2)
        if b in neighbors(a)
    }


def triangular_faces(cells, neighbors) -> set[tuple[Point, ...]]:
    faces = set()
    for cell in cells:
        for tri in combinations(cell, 3):
            if all(b in neighbors(a) for a, b in combinations(tri, 2)):
                faces.add(tuple(sorted(tri)))
    return faces


def verify_codim2_triangle_parity() -> None:
    verts = (0, 1, 2)
    edges = list(combinations(verts, 2))
    for bits in product((0, 1), repeat=3):
        cut = [e for e in edges if bits[e[0]] != bits[e[1]]]
        assert len(cut) in (0, 2)
        if len(cut) == 2:
            omega_endpoints = sorted({v for e in cut for v in e if bits[v] == 1})
            assert len(omega_endpoints) in (1, 2)
            if len(omega_endpoints) == 2:
                assert tuple(omega_endpoints) in edges


def components(adj: list[set[int]], nodes: set[int]) -> list[set[int]]:
    nodes = set(nodes)
    out = []
    while nodes:
        root = nodes.pop()
        seen = {root}
        stack = [root]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v in nodes:
                    nodes.remove(v)
                    seen.add(v)
                    stack.append(v)
        out.append(seen)
    return out


def c4_coloring_regression() -> tuple[int, int, int, int]:
    vt = tuple(range(4))
    et = list(combinations(vt, 2))
    tt = list(combinations(vt, 3))

    vo = tuple(range(6))
    opposite = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}
    eo = [(i, j) for i in vo for j in range(i + 1, 6) if opposite[i] != j]
    to = [tri for tri in combinations(vo, 3) if all(tuple(sorted(e)) in eo for e in combinations(tri, 2))]

    def classify(vertices, edges, triangles):
        total = 0
        bad = []
        for bits in product((0, 1), repeat=len(vertices)):
            if len(set(bits)) == 1:
                continue
            total += 1
            cut = [tuple(sorted(e)) for e in edges if bits[e[0]] != bits[e[1]]]
            idx = {e: i for i, e in enumerate(cut)}
            adj = [set() for _ in cut]
            for tri in triangles:
                local = [tuple(sorted(e)) for e in combinations(tri, 2) if tuple(sorted(e)) in idx]
                for e1, e2 in combinations(local, 2):
                    a, b = idx[e1], idx[e2]
                    adj[a].add(b)
                    adj[b].add(a)
            cc = components(adj, set(range(len(cut))))
            if len(cc) != 1:
                bad.append((bits, tuple(sorted(len(c) for c in cc))))
        return total, bad

    ttot, tbad = classify(vt, et, tt)
    otot, obad = classify(vo, eo, to)
    assert ttot == 14 and not tbad
    assert otot == 62 and len(obad) == 6
    assert all(sizes == (4, 4) for _, sizes in obad)
    return ttot, len(tbad), otot, len(obad)


def frontier(c: set[Point], neighbors) -> set[Point]:
    return {q for p in c for q in neighbors(p) if q not in c}


def connected_in(nodes: set[Point], neighbors, s: Point, t: Point) -> bool:
    if s not in nodes or t not in nodes:
        return False
    seen = {s}
    queue = deque([s])
    while queue:
        x = queue.popleft()
        if x == t:
            return True
        for y in neighbors(x):
            if y in nodes and y not in seen:
                seen.add(y)
                queue.append(y)
    return False


def verify_path(path: list[Point], nodes: set[Point], neighbors) -> None:
    assert all(x in nodes for x in path)
    assert all(path[i + 1] in neighbors(path[i]) for i in range(len(path) - 1))


def one_shell_regression(name: str, neighbors, control_path: list[Point]) -> dict[str, object]:
    o = (0, 0, 0)
    octs = octahedra_through_origin(neighbors)
    first = octs[0]
    v = next(x for x in first if x != o and x not in neighbors(o))
    equator = tuple(sorted(set(first) - {o, v}))
    base = set(equator)

    f = frontier(base, neighbors)
    verify_path(control_path, f, neighbors)
    assert control_path[0] == o and control_path[-1] == v
    assert [sum(q in base for q in neighbors(p)) for p in control_path] == [4, 2, 1, 2, 4]

    pool = sorted(f - {o, v})
    assert len(pool) == 24
    total = 0
    disconnects = 0
    for k in range(5):
        for extra in combinations(pool, k):
            total += 1
            c = base | set(extra)
            ff = frontier(c, neighbors)
            if not connected_in(ff, neighbors, o, v):
                disconnects += 1
    assert total == 12951
    assert disconnects == 0
    return {
        "world": name,
        "initial_pool": 24,
        "extensions": total,
        "disconnects": disconnects,
    }


def world_local_certificate(name: str, neighbors) -> dict[str, object]:
    tets = tetrahedra_through_origin(neighbors)
    octs = octahedra_through_origin(neighbors)
    cells = tets + octs
    faces = triangular_faces(cells, neighbors)
    origin_faces = {f for f in faces if (0, 0, 0) in f}
    cliques = triangle_cliques_through_origin(neighbors)
    assert len(tets) == 8
    assert len(octs) == 6
    assert len(cliques) == 24
    assert origin_faces == cliques
    counts = [sum(set(tri) <= set(cell) for cell in cells) for tri in cliques]
    assert counts == [2] * len(counts)
    return {
        "world": name,
        "tetrahedra_through_origin": 8,
        "octahedra_through_origin": 6,
        "native_triangles_through_origin": 24,
        "three_cells_per_triangle_local_count": sorted(set(counts)),
    }


def main() -> int:
    verify_codim2_triangle_parity()

    for p in ((0, 0, 0), (0, 0, 1)):
        assert {hcp_phase_swap(q) for q in hcp_neighbors(p)} == set(hcp_neighbors(hcp_phase_swap(p)))

    fcc_local = world_local_certificate("FCC", fcc_neighbors)
    hcp_local = world_local_certificate("HCP", hcp_neighbors)
    c4 = c4_coloring_regression()
    fcc_pressure = one_shell_regression(
        "FCC",
        fcc_neighbors,
        [(0, 0, 0), (0, -1, -1), (-1, -2, -1), (-2, -1, -1), (-2, 0, 0)],
    )
    hcp_pressure = one_shell_regression(
        "HCP",
        hcp_neighbors,
        [(0, 0, 0), (1, -1, 0), (1, -2, 0), (0, -2, -1), (-1, -1, -1)],
    )

    print("PASS R043-C5 exact local/topological hypotheses and C4 regressions")
    print(fcc_local)
    print(hcp_local)
    print({"c4_coloring": c4})
    print(fcc_pressure)
    print(hcp_pressure)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
