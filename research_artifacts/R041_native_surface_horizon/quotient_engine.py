#!/usr/bin/env python3
"""R041 exact finite-horizon native-surface quotient engine.

Independent of the R039 executable.  The theorem-critical path uses only integer /
combinatorial operations.  Coordinates are implementation carriers for the frozen
FCC/HCP contact graphs; no radius, norm, Euclidean area, curvature, or floating point
is used.
"""
from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import permutations, product
from typing import Callable, Iterable

Point = tuple[int, int, int]
Cluster = tuple[Point, ...]
Neighbors = Callable[[Point], tuple[Point, ...]]

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


def frontier(cluster: Iterable[Point], neighbors: Neighbors) -> set[Point]:
    C = set(cluster)
    out: set[Point] = set()
    for p in C:
        out.update(neighbors(p))
    return out - C


def internal_edges(cluster: Iterable[Point], neighbors: Neighbors) -> int:
    C = set(cluster)
    return sum(sum(q in C for q in neighbors(p)) for p in C) // 2


def surface(cluster: Iterable[Point], neighbors: Neighbors) -> int:
    C = set(cluster)
    return 12 * len(C) - 2 * internal_edges(C, neighbors)


def attachment_count(cluster: Iterable[Point], x: Point, neighbors: Neighbors) -> int:
    C = set(cluster)
    return sum(q in C for q in neighbors(x))


def histogram(cluster: Iterable[Point], neighbors: Neighbors):
    C = set(cluster)
    return tuple(sorted(Counter(attachment_count(C, x, neighbors) for x in frontier(C, neighbors)).items()))


def reduced_profile(cluster: Iterable[Point], x: Point, neighbors: Neighbors):
    C = set(cluster)
    F = frontier(C, neighbors)
    k = attachment_count(C, x, neighbors)
    A = Counter()
    for y in neighbors(x):
        if y in F and y != x:
            A[attachment_count(C, y, neighbors)] += 1
    return (k, tuple(sorted(A.items())))


def reduced_r2(cluster: Iterable[Point], neighbors: Neighbors):
    C = set(cluster)
    return tuple(sorted((reduced_profile(C, x, neighbors) for x in frontier(C, neighbors)), key=repr))


def reachable_added_sets(cluster: Iterable[Point], h: int, neighbors: Neighbors):
    C = frozenset(cluster)
    states = {frozenset()}
    for _ in range(h):
        nxt = set()
        for A in states:
            current = C | A
            for x in frontier(current, neighbors):
                if x not in C:
                    nxt.add(A | {x})
        states = nxt
    return states


def added_contact_score(cluster: Iterable[Point], added: Iterable[Point], neighbors: Neighbors) -> int:
    C, A = set(cluster), set(added)
    cross = sum(1 for a in A for q in neighbors(a) if q in C)
    inner = sum(sum(q in A for q in neighbors(a)) for a in A) // 2
    return cross + inner


def terminal_support(cluster: Iterable[Point], h: int, neighbors: Neighbors) -> tuple[int, ...]:
    C = tuple(cluster)
    S0 = surface(C, neighbors)
    return tuple(sorted({
        S0 + 12 * h - 2 * added_contact_score(C, A, neighbors)
        for A in reachable_added_sets(C, h, neighbors)
    }))


def contact_score_spectrum(cluster: Iterable[Point], h: int, neighbors: Neighbors) -> tuple[int, ...]:
    C = tuple(cluster)
    return tuple(sorted({added_contact_score(C, A, neighbors) for A in reachable_added_sets(C, h, neighbors)}))


def exterior_layers(cluster: Iterable[Point], h: int, neighbors: Neighbors) -> tuple[frozenset[Point], ...]:
    if h <= 0:
        return ()
    C = set(cluster)
    layers: list[set[Point]] = []
    seen = set(C)
    layer = frontier(C, neighbors)
    for _ in range(h):
        layers.append(set(layer))
        seen.update(layer)
        nxt: set[Point] = set()
        for p in layer:
            nxt.update(neighbors(p))
        layer = nxt - seen
    return tuple(frozenset(x) for x in layers)


def cone_stats(cluster: Iterable[Point], h: int, neighbors: Neighbors) -> dict:
    layers = exterior_layers(cluster, h, neighbors)
    layer_of = {v: r for r, layer in enumerate(layers) for v in layer}
    V = set(layer_of)
    edges: set[tuple[Point, Point]] = set()
    by_layer = Counter()
    for u in V:
        for v in neighbors(u):
            if v in V and u < v:
                edges.add((u, v))
                by_layer[tuple(sorted((layer_of[u], layer_of[v])))] += 1
    last = h - 1
    retained = {e for e in edges if not (layer_of[e[0]] == last and layer_of[e[1]] == last)}
    return {
        "layer_sizes": [len(x) for x in layers],
        "vertices": len(V),
        "j_edges": len(edges),
        "k_edges": len(retained),
        "pruned_last_layer_edges": len(edges) - len(retained),
        "edge_layer_counts": {f"{a}-{b}": n for (a, b), n in sorted(by_layer.items())},
    }


def activation_pruned_carrier(cluster: Iterable[Point], h: int, neighbors: Neighbors):
    C = tuple(cluster)
    layers = exterior_layers(C, h, neighbors)
    layer_of = {v: r for r, layer in enumerate(layers) for v in layer}
    V = tuple(sorted(layer_of))
    last = h - 1
    weights = tuple((v, attachment_count(C, v, neighbors) if layer_of[v] == 0 else 0) for v in V)
    edges = []
    for u in V:
        for v in neighbors(u):
            if v in layer_of and u < v:
                if layer_of[u] == last and layer_of[v] == last:
                    continue
                edges.append((u, v))
    return (surface(C, neighbors), weights, tuple(sorted(edges)))


def carrier_trajectory_support(cluster: Iterable[Point], h: int, neighbors: Neighbors):
    _S0, weights_items, edges = activation_pruned_carrier(cluster, h, neighbors)
    weights = dict(weights_items)
    adj: dict[Point, set[Point]] = {v: set() for v in weights}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    states: set[tuple[frozenset[Point], tuple[int, ...]]] = {(frozenset(), ())}
    for _ in range(h):
        nxt = set()
        for chosen, ks in states:
            for x in weights:
                if x in chosen:
                    continue
                k = weights[x] + sum(y in chosen for y in adj[x])
                if k > 0:
                    nxt.add((chosen | {x}, ks + (k,)))
        states = nxt
    return tuple(sorted({ks for _, ks in states}))


def direct_trajectory_support(cluster: Iterable[Point], h: int, neighbors: Neighbors):
    C0 = frozenset(cluster)
    states: set[tuple[frozenset[Point], tuple[int, ...]]] = {(C0, ())}
    for _ in range(h):
        nxt = set()
        for current, ks in states:
            for x in frontier(current, neighbors):
                k = attachment_count(current, x, neighbors)
                nxt.add((current | {x}, ks + (k,)))
        states = nxt
    return tuple(sorted({ks for _, ks in states}))


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
    def __init__(self, world: str):
        self.world = world
        self.neighbors, self.canonical = WORLD[world]
        self._succ_cache: dict[Cluster, tuple[tuple[int, Cluster], ...]] = {}
        self._terminal_cache: dict[tuple[Cluster, int], tuple[int, ...]] = {}
        self._oper_cache: dict[tuple[Cluster, int], tuple] = {}

    def successors(self, C: Cluster):
        if C not in self._succ_cache:
            Cset = set(C)
            self._succ_cache[C] = tuple(
                (attachment_count(Cset, x, self.neighbors), self.canonical(tuple(sorted(Cset | {x}))))
                for x in frontier(Cset, self.neighbors)
            )
        return self._succ_cache[C]

    def terminal(self, C: Cluster, h: int):
        key = (C, h)
        if key not in self._terminal_cache:
            if h == 0:
                ans = (surface(C, self.neighbors),)
            else:
                vals = set()
                for _k, D in self.successors(C):
                    vals.update(self.terminal(D, h - 1))
                ans = tuple(sorted(vals))
            self._terminal_cache[key] = ans
        return self._terminal_cache[key]

    def cumulative_terminal(self, C: Cluster, h: int):
        return tuple(self.terminal(C, t) for t in range(h + 1))

    def operational(self, C: Cluster, h: int):
        key = (C, h)
        if key not in self._oper_cache:
            s = surface(C, self.neighbors)
            if h == 0:
                ans = (s,)
            else:
                children = {(k, self.operational(D, h - 1)) for k, D in self.successors(C)}
                ans = (s, tuple(sorted(children, key=repr)))
            self._oper_cache[key] = ans
        return self._oper_cache[key]


def quotient_class_counts(world: str, max_n: int, max_h: int) -> dict[int, dict[str, int]]:
    neighbors, _ = WORLD[world]
    eng = SignatureEngine(world)
    levels = enumerate_animals(world, max_n)
    out = {}
    for n, level in levels.items():
        row = {
            "states": len(level),
            "S": len({surface(C, neighbors) for C in level}),
            "H": len({histogram(C, neighbors) for C in level}),
            "R2bar": len({reduced_r2(C, neighbors) for C in level}),
        }
        for h in range(1, max_h + 1):
            row[f"T{h}"] = len({eng.terminal(C, h) for C in level})
            row[f"B{h}"] = len({eng.operational(C, h) for C in level})
            row[f"cumT{h}"] = len({eng.cumulative_terminal(C, h) for C in level})
        out[n] = row
    return out
