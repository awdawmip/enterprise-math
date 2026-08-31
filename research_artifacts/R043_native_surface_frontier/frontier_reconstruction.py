#!/usr/bin/env python3
"""R043 exact native-surface frontier reconstruction verifier.

The theorem-critical path is integer/combinatorial. Coordinates are implementation
carriers for the frozen FCC/HCP contact relations only; no norm, radius, Euclidean
area, curvature, or floating point geometry is used.

This module is intentionally independent of the R039/R041 executables. It consumes
their frozen definitions/results semantically and supplies an independent G0 checker,
B_h oracle, residual engine, and stationary slot-cut update verifier.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
from itertools import permutations, product
from typing import Callable, Iterable

import networkx as nx

Point = tuple[int, int, int]
Cluster = tuple[Point, ...]
Neighbors = Callable[[Point], tuple[Point, ...]]

# ---------------------------------------------------------------------------
# Frozen FCC / HCP native contact worlds
# ---------------------------------------------------------------------------

FCC_DIRS: tuple[Point, ...] = tuple(sorted(
    tuple(v)
    for zero in range(3)
    for a in (-1, 1)
    for b in (-1, 1)
    for v in [tuple(
        0 if i == zero else (a if i == [j for j in range(3) if j != zero][0] else b)
        for i in range(3)
    )]
))
FCC_OPS = tuple(
    (perm, signs)
    for perm in permutations(range(3))
    for signs in product((-1, 1), repeat=3)
)


def fcc_neighbors(p: Point) -> tuple[Point, ...]:
    x, y, z = p
    return tuple((x + dx, y + dy, z + dz) for dx, dy, dz in FCC_DIRS)


def _fcc_apply(p: Point, op) -> Point:
    perm, signs = op
    return tuple(signs[i] * p[perm[i]] for i in range(3))  # type: ignore[return-value]


def _normalize_fcc(points: Iterable[Point]) -> Cluster:
    pts = sorted(points)
    a = pts[0]
    return tuple(sorted((x - a[0], y - a[1], z - a[2]) for x, y, z in pts))


@lru_cache(maxsize=None)
def canonical_fcc(cluster: Cluster) -> Cluster:
    return min(_normalize_fcc(_fcc_apply(p, op) for p in cluster) for op in FCC_OPS)


TRI_DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1))


def hcp_neighbors(p: Point) -> tuple[Point, ...]:
    i, j, k = p
    out: list[Point] = [(i + di, j + dj, k) for di, dj in TRI_DIRS]
    offsets = ((0, 0), (-1, 0), (0, -1)) if k % 2 == 0 else ((0, 0), (1, 0), (0, 1))
    for dk in (-1, 1):
        for di, dj in offsets:
            out.append((i + di, j + dj, k + dk))
    return tuple(out)


def _hcp_r120(p: Point) -> Point:
    i, j, k = p
    return (-i - j - (k & 1), i, k)


def _hcp_apply(p: Point, code) -> Point:
    r, swap, href, phase_swap = code
    for _ in range(r):
        p = _hcp_r120(p)
    i, j, k = p
    if swap:
        i, j = j, i
    if href:
        k = -k
    if phase_swap:
        i, j, k = -i, -j, k + 1
    return (i, j, k)


HCP_OPS = tuple((r, s, h, t) for r in range(3) for s in (0, 1) for h in (0, 1) for t in (0, 1))


def _normalize_hcp(points: Iterable[Point]) -> Cluster:
    pts = list(points)
    mi = min(p[0] for p in pts)
    mj = min(p[1] for p in pts)
    mk = min(p[2] for p in pts)
    tz = mk if mk % 2 == 0 else mk - 1
    return tuple(sorted((x - mi, y - mj, z - tz) for x, y, z in pts))


@lru_cache(maxsize=None)
def canonical_hcp(cluster: Cluster) -> Cluster:
    return min(_normalize_hcp(_hcp_apply(p, op) for p in cluster) for op in HCP_OPS)


WORLD = {
    "fcc": (fcc_neighbors, canonical_fcc),
    "hcp": (hcp_neighbors, canonical_hcp),
}

# ---------------------------------------------------------------------------
# Native surface primitives and exact branch oracle
# ---------------------------------------------------------------------------


def frontier(cluster: Iterable[Point], neighbors: Neighbors) -> set[Point]:
    C = set(cluster)
    out: set[Point] = set()
    for p in C:
        out.update(neighbors(p))
    return out - C


def attachment_count(cluster: Iterable[Point], x: Point, neighbors: Neighbors) -> int:
    C = set(cluster)
    return sum(q in C for q in neighbors(x))


def internal_edges(cluster: Iterable[Point], neighbors: Neighbors) -> int:
    C = set(cluster)
    return sum(sum(q in C for q in neighbors(p)) for p in C) // 2


def surface(cluster: Iterable[Point], neighbors: Neighbors) -> int:
    C = set(cluster)
    return 12 * len(C) - 2 * internal_edges(C, neighbors)


def enumerate_animals(world: str, max_n: int) -> dict[int, set[Cluster]]:
    neighbors, canonical = WORLD[world]
    levels: dict[int, set[Cluster]] = {1: {canonical(((0, 0, 0),))}}
    for n in range(1, max_n):
        nxt: set[Cluster] = set()
        for Csig in levels[n]:
            C = set(Csig)
            for x in frontier(C, neighbors):
                nxt.add(canonical(tuple(sorted(C | {x}))))
        levels[n + 1] = nxt
    return levels


class SignatureEngine:
    """Canonical exact branch-aware Boolean B_h oracle."""

    def __init__(self, world: str):
        self.neighbors, self.canonical = WORLD[world]
        self._cache: dict[tuple[Cluster, int], tuple] = {}

    def operational(self, C: Cluster, h: int):
        key = (C, h)
        if key in self._cache:
            return self._cache[key]
        S = surface(C, self.neighbors)
        if h == 0:
            ans = (S,)
        else:
            children = set()
            Cset = set(C)
            for x in frontier(Cset, self.neighbors):
                k = attachment_count(Cset, x, self.neighbors)
                D = self.canonical(tuple(sorted(Cset | {x})))
                children.add((k, self.operational(D, h - 1)))
            ans = (S, tuple(sorted(children, key=repr)))
        self._cache[key] = ans
        return ans

# ---------------------------------------------------------------------------
# G0 weighted abstract frontier graph
# ---------------------------------------------------------------------------


def g0_graph(C: Iterable[Point], neighbors: Neighbors) -> nx.Graph:
    C = tuple(C)
    F = sorted(frontier(C, neighbors))
    Fs = set(F)
    G = nx.Graph()
    for x in F:
        G.add_node(x, w=attachment_count(C, x, neighbors))
    for x in F:
        for y in neighbors(x):
            if y in Fs and x < y:
                G.add_edge(x, y)
    return G


def g0_wl_key(C: Iterable[Point], neighbors: Neighbors):
    C = tuple(C)
    G = g0_graph(C, neighbors)
    return (
        surface(C, neighbors),
        len(G),
        G.number_of_edges(),
        nx.weisfeiler_lehman_graph_hash(G, node_attr="w", iterations=5, digest_size=16),
    )


def g0_equal(C: Iterable[Point], D: Iterable[Point], neighbors: Neighbors) -> bool:
    if g0_wl_key(C, neighbors) != g0_wl_key(D, neighbors):
        return False
    return nx.is_isomorphic(
        g0_graph(C, neighbors),
        g0_graph(D, neighbors),
        node_match=lambda a, b: a["w"] == b["w"],
    )


def rooted_g0_candidate_buckets(C: Iterable[Point], neighbors: Neighbors):
    """Necessary buckets for abstract G0 automorphism orbits."""
    G = g0_graph(C, neighbors)
    sub = nx.weisfeiler_lehman_subgraph_hashes(
        G,
        node_attr="w",
        iterations=6,
        digest_size=12,
        include_initial_labels=True,
    )
    buckets: dict[tuple, list[Point]] = defaultdict(list)
    for x in G:
        buckets[(G.nodes[x]["w"], tuple(sub[x]))].append(x)
    return G, [xs for xs in buckets.values() if len(xs) > 1]


def rooted_isomorphic(G: nx.Graph, x: Point, y: Point) -> bool:
    A = G.copy()
    B = G.copy()
    nx.set_node_attributes(A, False, "root")
    nx.set_node_attributes(B, False, "root")
    A.nodes[x]["root"] = True
    B.nodes[y]["root"] = True
    return nx.is_isomorphic(
        A,
        B,
        node_match=lambda a, b: a["w"] == b["w"] and a["root"] == b["root"],
    )

# ---------------------------------------------------------------------------
# L1 residuals
# ---------------------------------------------------------------------------


def exterior_L1(C: Iterable[Point], neighbors: Neighbors) -> tuple[set[Point], set[Point]]:
    C = set(C)
    F = frontier(C, neighbors)
    seen = C | F
    L1: set[Point] = set()
    for x in F:
        L1.update(neighbors(x))
    L1 -= seen
    return F, L1


def pair_overlap(C: Iterable[Point], neighbors: Neighbors):
    F, L1 = exterior_L1(C, neighbors)
    O: Counter[tuple[Point, Point]] = Counter()
    for z in L1:
        xs = sorted(x for x in neighbors(z) if x in F)
        for i in range(len(xs)):
            for j in range(i + 1, len(xs)):
                O[(xs[i], xs[j])] += 1
    return dict(O)


def shared_future_multihypergraph(C: Iterable[Point], neighbors: Neighbors):
    F, L1 = exterior_L1(C, neighbors)
    return tuple(sorted((z, tuple(sorted(x for x in neighbors(z) if x in F))) for z in L1))

# ---------------------------------------------------------------------------
# R043 stationary native slot-cut carrier K_partial
# ---------------------------------------------------------------------------


def _delta(a: Point, b: Point) -> Point:
    return (b[0] - a[0], b[1] - a[1], b[2] - a[2])


def slot_cut_carrier(C: Iterable[Point], neighbors: Neighbors):
    """K_partial in one coherent implementation coordinate frame.

    State = current frontier plus, for each frontier cell, the native contact-slot
    offsets that point to occupied neighbors. No L1/deeper exterior or deep interior
    state is retained.
    """
    C = set(C)
    F = frontier(C, neighbors)
    inward = {
        x: frozenset(_delta(x, q) for q in neighbors(x) if q in C)
        for x in F
    }
    return frozenset(F), inward


def slot_cut_update(carrier, x: Point, neighbors: Neighbors):
    F0, inward0 = carrier
    F = set(F0)
    if x not in F:
        raise ValueError("action must be a current frontier cell")

    newly_exposed: set[Point] = set()
    for z in neighbors(x):
        if z in F:
            continue
        if _delta(x, z) in inward0[x]:
            continue
        newly_exposed.add(z)

    F1 = (F - {x}) | newly_exposed
    inward1: dict[Point, frozenset[Point]] = {}

    for y in F - {x}:
        slots = set(inward0[y])
        if x in neighbors(y):
            slots.add(_delta(y, x))
        inward1[y] = frozenset(slots)

    for z in newly_exposed:
        inward1[z] = frozenset({_delta(z, x)})

    return frozenset(F1), inward1


def slot_cut_equal(A, B) -> bool:
    FA, IA = A
    FB, IB = B
    return FA == FB and all(IA[x] == IB[x] for x in FA)


def g0_from_slot_cut(carrier, neighbors: Neighbors):
    F0, inward = carrier
    F = set(F0)
    weights = tuple(sorted((x, len(inward[x])) for x in F))
    edges = []
    for x in F:
        for y in neighbors(x):
            if y in F and x < y:
                edges.append((x, y))
    return sum(len(inward[x]) for x in F), weights, tuple(sorted(edges))


def derived_L1_from_slot_cut(carrier, neighbors: Neighbors) -> set[Point]:
    F0, inward = carrier
    F = set(F0)
    L1: set[Point] = set()
    for x in F:
        for z in neighbors(x):
            if z in F:
                continue
            if _delta(x, z) in inward[x]:
                continue
            L1.add(z)
    return L1

# ---------------------------------------------------------------------------
# Bounded audit helpers
# ---------------------------------------------------------------------------


def collision_atlas(world: str, max_n: int):
    neighbors, _ = WORLD[world]
    levels = enumerate_animals(world, max_n)
    seen: dict[tuple, tuple[int, Cluster]] = {}
    collisions = []
    rows = {}
    for n, level in levels.items():
        for C in level:
            key = g0_wl_key(C, neighbors)
            if key in seen:
                n0, D = seen[key]
                if g0_equal(C, D, neighbors):
                    collisions.append((n0, D, n, C))
            else:
                seen[key] = (n, C)
        rows[n] = {"states": len(level)}
    return rows, collisions, len(seen)


def rooted_update_audit(world: str, max_parent_n: int):
    neighbors, canonical = WORLD[world]
    levels = enumerate_animals(world, max_parent_n)
    splits = []
    for n, level in levels.items():
        for C in level:
            G, buckets = rooted_g0_candidate_buckets(C, neighbors)
            for bucket in buckets:
                by_child: dict[tuple, list[Point]] = defaultdict(list)
                Cset = set(C)
                for x in bucket:
                    D = tuple(sorted(Cset | {x}))
                    by_child[g0_wl_key(D, neighbors)].append(x)
                if len(by_child) <= 1:
                    continue
                groups = list(by_child.values())
                for i in range(len(groups)):
                    for j in range(i + 1, len(groups)):
                        for x in groups[i]:
                            for y in groups[j]:
                                if rooted_isomorphic(G, x, y):
                                    Dx = canonical(tuple(sorted(Cset | {x})))
                                    Dy = canonical(tuple(sorted(Cset | {y})))
                                    splits.append((n, C, x, y, Dx, Dy))
    return splits


def slot_cut_audit(world: str, max_n: int):
    neighbors, _ = WORLD[world]
    levels = enumerate_animals(world, max_n)
    actions = 0
    mismatches = []
    for n, level in levels.items():
        for C in level:
            carrier = slot_cut_carrier(C, neighbors)
            for x in carrier[0]:
                actions += 1
                got = slot_cut_update(carrier, x, neighbors)
                want = slot_cut_carrier(set(C) | {x}, neighbors)
                if not slot_cut_equal(got, want):
                    mismatches.append((n, C, x))
                    return {"actions": actions, "mismatches": mismatches}
    return {"actions": actions, "mismatches": mismatches}


if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("collision", "rooted", "slot"))
    parser.add_argument("world", choices=("fcc", "hcp"))
    parser.add_argument("--n", type=int, default=6)
    args = parser.parse_args()

    if args.mode == "collision":
        rows, collisions, distinct = collision_atlas(args.world, args.n)
        print(json.dumps({
            "levels": rows,
            "collisions": collisions,
            "distinct_g0_keys": distinct,
        }, default=repr, indent=2))
    elif args.mode == "rooted":
        print(repr(rooted_update_audit(args.world, args.n)))
    else:
        print(json.dumps(slot_cut_audit(args.world, args.n), default=repr, indent=2))
