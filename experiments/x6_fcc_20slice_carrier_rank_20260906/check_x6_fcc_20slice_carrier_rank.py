#!/usr/bin/env python3
"""Exact census of the 20 selected 3-of-6 axis triples in the current FCC carrier.

Uses the six official unoriented FCC line-family representatives from
P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md and the K4 edge labeling
induced by the four established STAR slices.

Checks:
- 20 triples split under K4/S4 incidence as 4 STAR + 4 TRIANGLE + 12 PATH;
- exactly the 4 STAR triples are rank two / determinant zero;
- all 16 non-STAR triples have determinant +/-2 and are Z-bases of D3;
- the signed-ray 60-degree carrier adjacency is respectively
  C6, C3 disjoint union C3, and P3 disjoint union P3.
"""

from __future__ import annotations

from itertools import combinations, product

V4 = tuple(range(4))
K4_EDGES = tuple(combinations(V4, 2))

FCC = {
    "L1": (1, 1, 0),
    "L2": (1, -1, 0),
    "L3": (1, 0, 1),
    "L4": (1, 0, -1),
    "L5": (0, 1, 1),
    "L6": (0, 1, -1),
}

# K4 vertices are the four established STARs A,B,C,D.  Each K4 edge is the
# unique line family shared by its endpoint STARs.
EDGE_TO_LINE = {
    (0, 1): "L1",  # A cap B
    (0, 2): "L3",  # A cap C
    (0, 3): "L6",  # A cap D
    (1, 2): "L5",  # B cap C
    (1, 3): "L4",  # B cap D
    (2, 3): "L2",  # C cap D
}


def determinant3(vectors):
    (a, b, c), (d, e, f), (g, h, i) = vectors
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def triple_type(edges):
    degree = [0, 0, 0, 0]
    for a, b in edges:
        degree[a] += 1
        degree[b] += 1
    signature = tuple(sorted(degree, reverse=True))
    if signature == (3, 1, 1, 1):
        return "STAR"
    if signature == (2, 2, 2, 0):
        return "TRIANGLE"
    if signature == (2, 2, 1, 1):
        return "PATH"
    raise AssertionError(f"unexpected 3-edge K4 signature: {signature}")


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def signed_rays(vectors):
    return tuple(
        (axis, sign, tuple(sign * x for x in vectors[axis]))
        for axis in range(3)
        for sign in (-1, 1)
    )


def acute_carrier_graph(vectors):
    """60-degree adjacency among norm-squared-two signed FCC rays.

    Every official FCC line representative has squared norm two, so dot=1 is
    exactly cosine 1/2, i.e. classical carrier separation 60 degrees.
    """
    rays = signed_rays(vectors)
    adj = {ray[:2]: set() for ray in rays}
    for left, right in combinations(rays, 2):
        if left[0] == right[0]:
            continue
        if dot(left[2], right[2]) == 1:
            adj[left[:2]].add(right[:2])
            adj[right[:2]].add(left[:2])
    return adj


def component_sizes(adj):
    seen = set()
    sizes = []
    for start in adj:
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        size = 0
        while stack:
            node = stack.pop()
            size += 1
            for nxt in adj[node]:
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        sizes.append(size)
    return tuple(sorted(sizes))


def star_relations(vectors):
    """All +/- coefficient relations s1*v1+s2*v2+s3*v3=0."""
    out = []
    for signs in product((-1, 1), repeat=3):
        total = tuple(
            sum(signs[k] * vectors[k][coordinate] for k in range(3))
            for coordinate in range(3)
        )
        if total == (0, 0, 0):
            out.append(signs)
    return tuple(out)


def main():
    counts = {"STAR": 0, "TRIANGLE": 0, "PATH": 0}
    determinant_counts = {"STAR": [], "TRIANGLE": [], "PATH": []}

    for edges in combinations(K4_EDGES, 3):
        kind = triple_type(edges)
        counts[kind] += 1
        line_names = tuple(EDGE_TO_LINE[e] for e in edges)
        vectors = tuple(FCC[name] for name in line_names)
        det = determinant3(vectors)
        determinant_counts[kind].append(det)

        graph = acute_carrier_graph(vectors)
        components = component_sizes(graph)
        degrees = tuple(sorted(len(graph[node]) for node in graph))

        if kind == "STAR":
            assert det == 0
            relations = star_relations(vectors)
            assert len(relations) == 2
            assert relations[1] == tuple(-x for x in relations[0])
            assert components == (6,)
            assert degrees == (2, 2, 2, 2, 2, 2)
        elif kind == "TRIANGLE":
            assert abs(det) == 2
            assert components == (3, 3)
            assert degrees == (2, 2, 2, 2, 2, 2)
        else:
            assert abs(det) == 2
            assert components == (3, 3)
            assert degrees == (1, 1, 1, 1, 2, 2)

        if kind != "STAR":
            # Every selected FCC vector lies in the parity lattice D3.
            assert all(sum(v) % 2 == 0 for v in vectors)
            # |det|=2 means the generated sublattice has index two in Z^3.
            # Since D3 itself has index two, containment forces equality.
            assert abs(det) == 2

    assert counts == {"STAR": 4, "TRIANGLE": 4, "PATH": 12}
    assert determinant_counts["STAR"] == [0, 0, 0, 0]
    assert all(abs(d) == 2 for d in determinant_counts["TRIANGLE"])
    assert all(abs(d) == 2 for d in determinant_counts["PATH"])

    print("PASS: X6/FCC 20-slice carrier rank census")
    print("4 STAR: rank2 and signed-ray graph C6")
    print("4 TRIANGLE: determinant +/-2, D3 basis, graph C3 disjoint union C3")
    print("12 PATH: determinant +/-2, D3 basis, graph P3 disjoint union P3")
    print("only STAR triples support the existing connected planar C6 carrier mechanism")


if __name__ == "__main__":
    main()
