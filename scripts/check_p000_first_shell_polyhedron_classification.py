#!/usr/bin/env python3
"""Exact certificate for RS-P000-FIRST-SHELL-POLYHEDRON-CLASSIFICATION.

Coordinates p=(X,Y,Z) are integer certificate coordinates.  The Euclidean
close-packing realization is
    Phi(p) = (X/2, Y/(2*sqrt(3)), Z*sqrt(6)/3).
Hence 12*||Phi(p)-Phi(q)||^2 =
    3*dX^2 + dY^2 + 8*dZ^2,
so all finite hull decisions and face metric checks below are exact integers.

For the centered Voronoi cell, put u=Phi^T x.  The 12 nearest-neighbor
bisectors become rational halfspaces p.u <= 1/2.  Euclidean squared distance
in u-coordinates is
    4*du_X^2 + 12*du_Y^2 + (3/2)*du_Z^2,
so the dual-cell geometry is checked exactly with Fraction.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from itertools import combinations
import json

RING = [
    (2, 0, 0), (1, 3, 0), (-1, 3, 0),
    (-2, 0, 0), (-1, -3, 0), (1, -3, 0),
]
UP = [(1, 1, 1), (-1, 1, 1), (0, -2, 1)]
DOWN_H = [(1, 1, -1), (-1, 1, -1), (0, -2, -1)]
DOWN_C = [(0, 2, -1), (-1, -1, -1), (1, -1, -1)]

MODELS = {
    "FCC_C": RING + UP + DOWN_C,
    "HCP_H": RING + UP + DOWN_H,
}


def sub(a, b):
    return tuple(a[i] - b[i] for i in range(3))


def dot(a, b):
    return sum(a[i] * b[i] for i in range(3))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def shell_qdist(a, b):
    """12 times Euclidean squared distance after Phi."""
    dx, dy, dz = sub(a, b)
    return 3 * dx * dx + dy * dy + 8 * dz * dz


def supporting_facets(points):
    """Enumerate maximal supporting coplanar vertex sets, exactly."""
    out = set()
    for i, j, k in combinations(range(len(points)), 3):
        n = cross(sub(points[j], points[i]), sub(points[k], points[i]))
        if n == (0, 0, 0):
            continue
        d = dot(n, points[i])
        vals = [dot(n, p) - d for p in points]
        if all(v >= 0 for v in vals) or all(v <= 0 for v in vals):
            face = frozenset(t for t, v in enumerate(vals) if v == 0)
            if len(face) >= 3:
                out.add(face)
    return sorted(out, key=lambda s: (len(s), tuple(sorted(s))))


def shell_edges(points, facets):
    """All hull edges: in these exact regular faces they are contact pairs."""
    edges = set()
    for face in facets:
        for i, j in combinations(sorted(face), 2):
            if shell_qdist(points[i], points[j]) == 12:
                edges.add((i, j))
    return sorted(edges)


def face_metric_type(points, face):
    ds = sorted(shell_qdist(points[i], points[j]) for i, j in combinations(sorted(face), 2))
    if len(face) == 3:
        assert ds == [12, 12, 12]
        return "equilateral_triangle"
    if len(face) == 4:
        assert ds == [12, 12, 12, 12, 24, 24]
        return "square"
    raise AssertionError(f"unexpected hull face size: {len(face)}")


def solve3(A, b):
    M = [[F(A[i][j]) for j in range(3)] + [F(b[i])] for i in range(3)]
    for col in range(3):
        pivot = next((r for r in range(col, 3) if M[r][col] != 0), None)
        if pivot is None:
            raise ValueError("singular")
        M[col], M[pivot] = M[pivot], M[col]
        q = M[col][col]
        M[col] = [v / q for v in M[col]]
        for r in range(3):
            if r == col:
                continue
            q = M[r][col]
            if q:
                M[r] = [M[r][c] - q * M[col][c] for c in range(4)]
    return tuple(M[i][3] for i in range(3))


def voronoi_vertices(points, facets):
    """Vertices of {u: p.u <= 1/2 for all p}; one per shell facet."""
    vertices = []
    for face in facets:
        inds = sorted(face)
        u = None
        for tri in combinations(inds, 3):
            try:
                candidate = solve3([points[i] for i in tri], [F(1, 2)] * 3)
            except ValueError:
                continue
            if all(sum(F(points[i][j]) * candidate[j] for j in range(3)) == F(1, 2) for i in inds):
                u = candidate
                break
        assert u is not None
        assert all(sum(F(p[j]) * u[j] for j in range(3)) <= F(1, 2) for p in points)
        vertices.append(u)
    return vertices


def dual_edges(facets, primal_edges):
    out = set()
    for edge in primal_edges:
        incident = [k for k, face in enumerate(facets) if set(edge) <= face]
        assert len(incident) == 2
        out.add(tuple(sorted(incident)))
    return sorted(out)


def dual_qdist(a, b):
    """Euclidean squared distance in physical x-space, in rational u-coordinates."""
    dx, dy, dz = sub(a, b)
    return 4 * dx * dx + 12 * dy * dy + F(3, 2) * dz * dz


def cycle_order(vertices, edges):
    adj = {v: [] for v in vertices}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    assert all(len(adj[v]) == 2 for v in vertices)
    start = min(vertices)
    prev = None
    cur = start
    order = []
    while True:
        order.append(cur)
        a, b = adj[cur]
        nxt = a if a != prev else b
        prev, cur = cur, nxt
        if cur == start:
            break
        assert len(order) <= len(vertices)
    assert len(order) == len(vertices)
    return order


def is_parallel(a, b):
    return cross(a, b) == (0, 0, 0)


def fracstr(q):
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def analyze(name, points):
    assert len(points) == 12
    assert all(shell_qdist((0, 0, 0), p) == 12 for p in points)

    facets = supporting_facets(points)
    edges = shell_edges(points, facets)
    face_kinds = [face_metric_type(points, f) for f in facets]
    face_count = Counter(face_kinds)

    edge_face_types = Counter()
    for e in edges:
        incident = [f for f in facets if set(e) <= f]
        assert len(incident) == 2
        sig = tuple(sorted(("T" if len(f) == 3 else "S") for f in incident))
        edge_face_types["-".join(sig)] += 1

    assert len(points) - len(edges) + len(facets) == 2
    assert sum(len(f) for f in facets) == 2 * len(edges)

    central = all(tuple(-x for x in p) in set(points) for p in points)

    dv = voronoi_vertices(points, facets)
    de = dual_edges(facets, edges)
    assert len(dv) - len(de) + len(points) == 2
    assert 4 * len(points) == 2 * len(de)

    dual_face_kinds = Counter()
    dual_face_details = []
    for p_idx in range(len(points)):
        vids = [k for k, face in enumerate(facets) if p_idx in face]
        fedges = [e for e in de if e[0] in vids and e[1] in vids]
        assert len(vids) == 4 and len(fedges) == 4
        order = cycle_order(vids, fedges)
        cyc = [dv[k] for k in order]
        side2 = [dual_qdist(cyc[i], cyc[(i + 1) % 4]) for i in range(4)]
        diag2 = [dual_qdist(cyc[0], cyc[2]), dual_qdist(cyc[1], cyc[3])]
        vec = [sub(cyc[(i + 1) % 4], cyc[i]) for i in range(4)]
        parallel_pairs = [is_parallel(vec[0], vec[2]), is_parallel(vec[1], vec[3])]
        sside = sorted(side2)
        sdiag = sorted(diag2)
        if sside == [F(3, 8)] * 4 and parallel_pairs == [True, True]:
            kind = "rhombus"
            assert sdiag == [F(1, 2), F(1, 1)]
        else:
            assert sside == [F(1, 6), F(3, 8), F(3, 8), F(2, 3)]
            assert parallel_pairs.count(True) == 1
            assert sdiag == [F(17, 24), F(17, 24)]
            kind = "isosceles_trapezoid"
        dual_face_kinds[kind] += 1
        dual_face_details.append({
            "shell_vertex": p_idx,
            "kind": kind,
            "side_squared": [fracstr(x) for x in sorted(side2)],
            "diagonal_squared": [fracstr(x) for x in sorted(diag2)],
            "opposite_edge_parallel_pair_count": parallel_pairs.count(True),
        })

    expected = {
        "FCC_C": {
            "edge_face": {"S-T": 24},
            "central": True,
            "dual": {"rhombus": 12},
        },
        "HCP_H": {
            "edge_face": {"S-S": 3, "S-T": 18, "T-T": 3},
            "central": False,
            "dual": {"rhombus": 6, "isosceles_trapezoid": 6},
        },
    }[name]
    assert dict(edge_face_types) == expected["edge_face"]
    assert central == expected["central"]
    assert dict(dual_face_kinds) == expected["dual"]
    assert face_count == Counter({"equilateral_triangle": 8, "square": 6})

    return {
        "model": name,
        "shell": {
            "V": len(points),
            "E": len(edges),
            "F": len(facets),
            "face_types": dict(face_count),
            "face_edge_incidence": sum(len(f) for f in facets),
            "edge_face_type_counts": dict(edge_face_types),
            "centrally_symmetric": central,
            "facets_by_vertex_index": [sorted(f) for f in facets],
        },
        "voronoi": {
            "V": len(dv),
            "E": len(de),
            "F": len(points),
            "face_types": dict(dual_face_kinds),
            "face_edge_incidence": 4 * len(points),
            "vertices_u": [[fracstr(x) for x in u] for u in dv],
            "face_details": dual_face_details,
        },
    }


def barlow_local_types():
    symbols = "ABC"
    rows = []
    counts = Counter()
    for mid in symbols:
        for left in symbols:
            for right in symbols:
                if left == mid or right == mid:
                    continue
                env = "HCP_H" if left == right else "FCC_C"
                rows.append((left + mid + right, env))
                counts[env] += 1
    assert counts == Counter({"HCP_H": 6, "FCC_C": 6})
    return rows


def main():
    results = {name: analyze(name, points) for name, points in MODELS.items()}
    rows = barlow_local_types()
    out = {
        "schema": "P000_FIRST_SHELL_POLYHEDRON_EXACT_CERTIFICATE_V1",
        "coordinate_map": "Phi(X,Y,Z)=(X/2, Y/(2*sqrt(3)), Z*sqrt(6)/3)",
        "models": results,
        "barlow_local_layer_triples": [{"triple": t, "type": k} for t, k in rows],
        "conclusions": {
            "barlow_shell_universal": "V=12,E=24,F=14 with 8 triangles + 6 squares",
            "barlow_shell_exact_types": ["FCC_C:cuboctahedron", "HCP_H:triangular_orthobicupola"],
            "barlow_voronoi_universal": "V=14,E=24,F=12, all quadrilateral faces",
            "barlow_voronoi_exact_types": [
                "FCC_C:rhombic_dodecahedron",
                "HCP_H:trapezo_rhombic_dodecahedron",
            ],
            "twelve_to_six_antipodal_pairing": {
                "FCC_C": "exists as six Euclidean antipodal pairs, but is carrier-only unless bridged to native axes",
                "HCP_H": "does not exist: the 12-point kissing shell is not centrally symmetric",
            },
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
