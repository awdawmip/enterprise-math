#!/usr/bin/env python3
"""Exact finite certificate for R043-C4 native interface link separators.

No floating point, metric threshold, or broad animal census is used.  The native
contact relations are copied exactly from the frozen R039 integer/combinatorial
reference.  The checker classifies the Delaunay tetrahedral/octahedral local
interface colorings and verifies the smallest global-repair control for the
unique octahedral opposite-pair separator type.
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


def components(adj: list[set[int]], nodes: set[int]) -> list[set[int]]:
    nodes = set(nodes)
    out: list[set[int]] = []
    while nodes:
        root = next(iter(nodes))
        nodes.remove(root)
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


def tetrahedra_through_origin(neighbors) -> list[tuple[Point, ...]]:
    o = (0, 0, 0)
    out = []
    for tri in combinations(neighbors(o), 3):
        cell = (o,) + tri
        if all(b in neighbors(a) for a, b in combinations(cell, 2)):
            out.append(tuple(sorted(cell)))
    return sorted(set(out))


def octahedra_through_origin(neighbors) -> list[tuple[Point, tuple[Point, ...]]]:
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
            out.append((q, tuple(sorted(common))))
    return out


def local_polyhedra_coloring_certificate() -> dict[str, object]:
    # Tetrahedron K4.
    vt = tuple(range(4))
    et = list(combinations(vt, 2))
    tt = list(combinations(vt, 3))

    # Octahedron: three opposite pairs (0,1), (2,3), (4,5).
    vo = tuple(range(6))
    opposite = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}
    eo = [(i, j) for i in vo for j in range(i + 1, 6) if opposite[i] != j]
    to = [tri for tri in combinations(vo, 3) if all(tuple(sorted(e)) in eo for e in combinations(tri, 2))]
    assert len(eo) == 12 and len(to) == 8

    def classify(vertices, edges, triangles):
        bad = []
        total = 0
        for bits in product((0, 1), repeat=len(vertices)):
            if len(set(bits)) == 1:
                continue
            total += 1
            cut = [tuple(sorted(e)) for e in edges if bits[e[0]] != bits[e[1]]]
            index = {e: i for i, e in enumerate(cut)}
            adj = [set() for _ in cut]
            for tri in triangles:
                local = [tuple(sorted(e)) for e in combinations(tri, 2) if tuple(sorted(e)) in index]
                for e1, e2 in combinations(local, 2):
                    i, j = index[e1], index[e2]
                    adj[i].add(j)
                    adj[j].add(i)
            cc = components(adj, set(range(len(cut))))
            if len(cc) != 1:
                bad.append({
                    "coloring": bits,
                    "ones": tuple(i for i, b in enumerate(bits) if b),
                    "cut_edges": tuple(cut),
                    "component_sizes": tuple(sorted(len(c) for c in cc)),
                })
        return total, bad

    tetra_total, tetra_bad = classify(vt, et, tt)
    oct_total, oct_bad = classify(vo, eo, to)
    assert tetra_total == 14 and tetra_bad == []
    assert oct_total == 62 and len(oct_bad) == 6

    opposite_pairs = ({0, 1}, {2, 3}, {4, 5})
    for row in oct_bad:
        ones = set(row["ones"])
        zeros = set(vo) - ones
        assert ones in opposite_pairs or zeros in opposite_pairs
        assert row["component_sizes"] == (4, 4)

    return {
        "tetra_nontrivial_colorings": tetra_total,
        "tetra_bad_colorings": len(tetra_bad),
        "octa_nontrivial_colorings": oct_total,
        "octa_bad_colorings": len(oct_bad),
        "octa_bad_type": "one color class is exactly one opposite vertex pair (or equivalently the other color class is its four-vertex complement)",
    }


def frontier(c: set[Point], neighbors) -> set[Point]:
    return {q for p in c for q in neighbors(p) if q not in c}


def verify_path(path: list[Point], nodes: set[Point], neighbors) -> None:
    assert all(p in nodes for p in path)
    assert all(path[i + 1] in neighbors(path[i]) for i in range(len(path) - 1))


def world_certificate(name: str, neighbors, control_path: list[Point]) -> dict[str, object]:
    tets = tetrahedra_through_origin(neighbors)
    octs = octahedra_through_origin(neighbors)
    assert len(tets) == 8
    assert len(octs) == 6

    u = (0, 0, 0)
    v, equator = octs[0]
    c = set(equator)
    assert len(c) == 4
    # Equator is a connected four-cycle/K_{2,2} in the octahedral contact graph.
    equator_degrees = sorted(sum(q in c for q in neighbors(p)) for p in c)
    assert equator_degrees == [2, 2, 2, 2]
    assert v not in neighbors(u)
    assert all(q in neighbors(u) and q in neighbors(v) for q in c)

    f = frontier(c, neighbors)
    verify_path(control_path, f, neighbors)
    assert control_path[0] == u and control_path[-1] == v
    occupied_neighbor_counts = [sum(q in c for q in neighbors(p)) for p in control_path]
    assert occupied_neighbor_counts == [4, 2, 1, 2, 4]

    # Thus the exact local opposite-pair separator does not by itself yield a
    # global frontier counterexample: the minimal connected equator-4 occupied
    # realization is repaired outside the octahedron by a four-contact path.
    return {
        "world": name,
        "origin_tetrahedra": len(tets),
        "origin_octahedra": len(octs),
        "opposite_pair": [u, v],
        "occupied_equator": list(equator),
        "equator_induced_degrees": equator_degrees,
        "frontier_repair_path": control_path,
        "frontier_repair_length": len(control_path) - 1,
        "repair_path_occupied_neighbor_counts": occupied_neighbor_counts,
    }


def main() -> int:
    local = local_polyhedra_coloring_certificate()
    fcc = world_certificate(
        "FCC",
        fcc_neighbors,
        [(0, 0, 0), (0, -1, -1), (-1, -2, -1), (-2, -1, -1), (-2, 0, 0)],
    )
    hcp = world_certificate(
        "HCP",
        hcp_neighbors,
        [(0, 0, 0), (1, -1, 0), (1, -2, 0), (0, -2, -1), (-1, -1, -1)],
    )
    print("PASS R043-C4 exact native local certificate")
    print(local)
    print(fcc)
    print(hcp)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
