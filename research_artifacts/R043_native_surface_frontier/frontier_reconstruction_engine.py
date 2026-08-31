#!/usr/bin/env python3
"""R043 exact native-frontier reconstruction helpers.

This module is intentionally independent of the R039/R041 executables while consuming
their frozen FCC/HCP contact relations and semantics.  The theorem-critical path uses
only integer/combinatorial arithmetic.  Coordinates are opaque implementation carriers;
no Euclidean radius, norm, curvature, or floating point geometry is used.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
from itertools import permutations, product
from typing import Callable, Iterable

Point = tuple[int, int, int]
Cluster = tuple[Point, ...]
Neighbors = Callable[[Point], tuple[Point, ...]]

# ---------- frozen FCC contact graph ----------
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
FCC_OPS = tuple((perm, signs) for perm in permutations(range(3)) for signs in product((-1, 1), repeat=3))


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


# ---------- frozen HCP contact graph ----------
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


# ---------- exact native surface primitives ----------
def frontier(cluster: Iterable[Point], neighbors: Neighbors) -> set[Point]:
    C = set(cluster)
    out: set[Point] = set()
    for p in C:
        out.update(neighbors(p))
    return out - C


def attachment_count(cluster: Iterable[Point], x: Point, neighbors: Neighbors) -> int:
    C = set(cluster)
    return sum(q in C for q in neighbors(x))


def surface(cluster: Iterable[Point], neighbors: Neighbors) -> int:
    C = set(cluster)
    e = sum(sum(q in C for q in neighbors(p)) for p in C) // 2
    return 12 * len(C) - 2 * e


def enumerate_animals(world: str, max_n: int) -> dict[int, set[Cluster]]:
    neighbors, canonical = WORLD[world]
    levels: dict[int, set[Cluster]] = {1: {canonical(((0, 0, 0),))}}
    for n in range(1, max_n):
        nxt: set[Cluster] = set()
        for C in levels[n]:
            Cs = set(C)
            for x in frontier(Cs, neighbors):
                nxt.add(canonical(tuple(sorted(Cs | {x}))))
        levels[n + 1] = nxt
    return levels


# ---------- G0 weighted current-frontier graph ----------
def g0_data(cluster: Iterable[Point], neighbors: Neighbors):
    C = set(cluster)
    F = frontier(C, neighbors)
    weights = {x: attachment_count(C, x, neighbors) for x in F}
    adj = {x: {y for y in neighbors(x) if y in F} for x in F}
    return F, weights, adj


def color_refinement(weights, adj, rounds: int = 12):
    """Canonical isomorphism-invariant refinement; never used as an exact equality test."""
    colors = {v: weights[v] for v in weights}
    for _ in range(rounds):
        sig = {v: (colors[v], tuple(sorted(colors[u] for u in adj[v]))) for v in colors}
        palette = {s: i for i, s in enumerate(sorted(set(sig.values()), key=repr))}
        colors = {v: palette[sig[v]] for v in sig}
    return colors


def g0_safe_invariant(weights, adj):
    """Necessary invariant for weighted-graph isomorphism; collisions require exact checking."""
    colors = color_refinement(weights, adj)
    edge_colors = Counter()
    for u in adj:
        for v in adj[u]:
            if u < v:
                edge_colors[tuple(sorted((colors[u], colors[v])))] += 1
    return (
        len(weights),
        sum(len(v) for v in adj.values()) // 2,
        tuple(sorted(Counter(weights.values()).items())),
        tuple(sorted(Counter((weights[v], len(adj[v])) for v in weights).items())),
        tuple(sorted(Counter(colors.values()).items())),
        tuple(sorted(edge_colors.items())),
    )


def weighted_graph_isomorphic(w1, a1, w2, a2, root1=None, root2=None) -> bool:
    """Dependency-free exact weighted simple-graph isomorphism with optional distinguished roots."""
    if len(w1) != len(w2):
        return False
    if sum(map(len, a1.values())) != sum(map(len, a2.values())):
        return False

    V1, V2 = list(w1), list(w2)
    if (root1 is None) != (root2 is None):
        return False

    # Joint color refinement ensures color IDs are directly comparable across the two graphs.
    c1 = {u: (w1[u], len(a1[u]), 1 if u == root1 else 0) for u in V1}
    c2 = {v: (w2[v], len(a2[v]), 1 if v == root2 else 0) for v in V2}
    for _ in range(max(1, len(V1))):
        s1 = {u: (c1[u], tuple(sorted((c1[z] for z in a1[u]), key=repr))) for u in V1}
        s2 = {v: (c2[v], tuple(sorted((c2[z] for z in a2[v]), key=repr))) for v in V2}
        palette = {s: i for i, s in enumerate(sorted(set(s1.values()) | set(s2.values()), key=repr))}
        n1 = {u: palette[s1[u]] for u in V1}
        n2 = {v: palette[s2[v]] for v in V2}
        if Counter(n1.values()) != Counter(n2.values()):
            return False
        old_partition_1 = {u: c1[u] for u in V1}
        old_partition_2 = {v: c2[v] for v in V2}
        c1, c2 = n1, n2
        # Once the number of color classes no longer grows in either graph, refinement is stable.
        if len(set(c1.values())) == len(set(old_partition_1.values())) and len(set(c2.values())) == len(set(old_partition_2.values())):
            break

    classes2 = defaultdict(list)
    for v in V2:
        classes2[c2[v]].append(v)
    mapping = {}
    used = set()

    def consistent(u, v):
        for um, vm in mapping.items():
            if (um in a1[u]) != (vm in a2[v]):
                return False
        return True

    def search():
        if len(mapping) == len(V1):
            return True
        best_u = None
        best_candidates = None
        for u in V1:
            if u in mapping:
                continue
            cand = [v for v in classes2[c1[u]] if v not in used and consistent(u, v)]
            if not cand:
                return False
            if best_candidates is None or len(cand) < len(best_candidates):
                best_u, best_candidates = u, cand
                if len(cand) == 1:
                    break
        assert best_u is not None and best_candidates is not None
        for v in best_candidates:
            mapping[best_u] = v
            used.add(v)
            if search():
                return True
            used.remove(v)
            del mapping[best_u]
        return False

    return search()


# ---------- exact Boolean operational oracle ----------
@lru_cache(maxsize=None)
def operational_signature(world: str, cluster: Cluster, h: int):
    neighbors, canonical = WORLD[world]
    S = surface(cluster, neighbors)
    if h == 0:
        return (S,)
    C = set(cluster)
    children = set()
    for x in frontier(C, neighbors):
        k = attachment_count(C, x, neighbors)
        D = canonical(tuple(sorted(C | {x})))
        children.add((k, operational_signature(world, D, h - 1)))
    return (S, tuple(sorted(children, key=repr)))


# ---------- R043 coexposure residual below full M3 ----------
def coexposure_carrier(cluster: Iterable[Point], neighbors: Neighbors):
    """One-successor carrier: G0 + L1 incidence + only coexposed L1-L1 edges.

    I[z] = N(z) intersect F.  An L1-L1 edge z--q is retained iff I[z] and I[q]
    intersect, i.e. iff some single current action can expose both endpoints together.
    """
    C = set(cluster)
    F, weights, adj0 = g0_data(C, neighbors)
    L1: set[Point] = set()
    for x in F:
        L1.update(neighbors(x))
    L1 -= C
    L1 -= F
    incidence = {z: frozenset(y for y in neighbors(z) if y in F) for z in L1}
    coedges = set()
    all_l1_edges = set()
    for z in L1:
        for q in neighbors(z):
            if q in L1 and z < q:
                all_l1_edges.add((z, q))
                if incidence[z] & incidence[q]:
                    coedges.add((z, q))
    return F, weights, adj0, L1, incidence, coedges, all_l1_edges


def successor_g0_from_coexposure(carrier, action: Point):
    F, weights, adj0, L1, incidence, coedges, _all_l1_edges = carrier
    if action not in F:
        raise ValueError("action must be a current frontier vertex")
    W = {z for z in L1 if action in incidence[z]}
    old = set(F) - {action}
    V = old | W
    new_weights = {
        y: weights[y] + (1 if y in adj0[action] else 0)
        for y in old
    }
    new_weights.update({z: 1 for z in W})
    new_adj = {v: set() for v in V}

    for u in old:
        new_adj[u].update(adj0[u] & old)
    for z in W:
        for y in incidence[z] - {action}:
            if y in old:
                new_adj[z].add(y)
                new_adj[y].add(z)
    for z, q in coedges:
        if z in W and q in W:
            new_adj[z].add(q)
            new_adj[q].add(z)
    return V, new_weights, new_adj


def coexposure_stats(cluster: Iterable[Point], neighbors: Neighbors):
    F, _w, a0, L1, incidence, coedges, all_l1_edges = coexposure_carrier(cluster, neighbors)
    return {
        "L0_vertices": len(F),
        "L1_vertices": len(L1),
        "E00": sum(map(len, a0.values())) // 2,
        "E01": sum(map(len, incidence.values())),
        "E11_full": len(all_l1_edges),
        "E11_coexposed": len(coedges),
        "E11_pruned": len(all_l1_edges - coedges),
    }


# ---------- targeted negative-control helper ----------
def graph_distance(adj, source, target):
    if source == target:
        return 0
    seen = {source}
    layer = {source}
    d = 0
    while layer:
        d += 1
        nxt = set()
        for u in layer:
            nxt.update(adj[u])
        nxt -= seen
        if target in nxt:
            return d
        seen |= nxt
        layer = nxt
    return None
