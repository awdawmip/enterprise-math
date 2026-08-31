#!/usr/bin/env python3
"""R039 exact metric-free rough-surface reference.

The theorem-critical path is integer/combinatorial only. Coordinates are implementation
coordinates for native contact relations and symmetry quotienting; no norm, radius,
Euclidean area, or floating-point geometry is used.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from functools import lru_cache
from itertools import permutations, product

Point = tuple[int, int, int]
Cluster = tuple[Point, ...]
Histogram = tuple[tuple[int, int], ...]

# ---------- FCC: parity-even Z^3 with the 12 (±1,±1,0) contact steps ----------
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
assert len(FCC_DIRS) == 12

FCC_OPS = tuple((perm, signs) for perm in permutations(range(3)) for signs in product((-1, 1), repeat=3))
assert len(FCC_OPS) == 48


def fcc_neighbors(p: Point) -> tuple[Point, ...]:
    x, y, z = p
    return tuple((x + dx, y + dy, z + dz) for dx, dy, dz in FCC_DIRS)


def fcc_apply(p: Point, op: tuple[tuple[int, int, int], tuple[int, int, int]]) -> Point:
    perm, signs = op
    a = p
    return tuple(signs[i] * a[perm[i]] for i in range(3))  # type: ignore[return-value]


def _normalize_fcc_translation(points: list[Point]) -> Cluster:
    points.sort()
    a = points[0]
    return tuple(sorted((x - a[0], y - a[1], z - a[2]) for x, y, z in points))


@lru_cache(maxsize=None)
def canonical_fcc(cluster: Cluster) -> Cluster:
    best: Cluster | None = None
    for op in FCC_OPS:
        sig = _normalize_fcc_translation([fcc_apply(p, op) for p in cluster])
        if best is None or sig < best:
            best = sig
    assert best is not None
    return best


# ---------- HCP: exact ABAB combinatorial coordinates ----------
TRI_DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1))


def hcp_neighbors(p: Point) -> tuple[Point, ...]:
    i, j, k = p
    out: list[Point] = [(i + di, j + dj, k) for di, dj in TRI_DIRS]
    offsets = ((0, 0), (-1, 0), (0, -1)) if k % 2 == 0 else ((0, 0), (1, 0), (0, 1))
    for dk in (-1, 1):
        for di, dj in offsets:
            out.append((i + di, j + dj, k + dk))
    return tuple(out)


def hcp_r120(p: Point) -> Point:
    i, j, k = p
    e = k & 1
    return (-i - j - e, i, k)


def hcp_apply(p: Point, code: tuple[int, int, int, int]) -> Point:
    r, swap, href, phase_swap = code
    for _ in range(r):
        p = hcp_r120(p)
    i, j, k = p
    if swap:
        i, j = j, i
    if href:
        k = -k
    if phase_swap:
        i, j, k = -i, -j, k + 1
    return (i, j, k)


# 24 space-group representatives modulo HCP Bravais translations (a,b,2m).
HCP_OPS = tuple((r, s, h, t) for r in range(3) for s in (0, 1) for h in (0, 1) for t in (0, 1))
assert len(HCP_OPS) == 24


def _normalize_hcp_translation(points: list[Point]) -> Cluster:
    mi = min(p[0] for p in points)
    mj = min(p[1] for p in points)
    mk = min(p[2] for p in points)
    tz = mk if mk % 2 == 0 else mk - 1
    return tuple(sorted((x - mi, y - mj, z - tz) for x, y, z in points))


@lru_cache(maxsize=None)
def canonical_hcp(cluster: Cluster) -> Cluster:
    best: Cluster | None = None
    for op in HCP_OPS:
        sig = _normalize_hcp_translation([hcp_apply(p, op) for p in cluster])
        if best is None or sig < best:
            best = sig
    assert best is not None
    return best


WORLD = {
    "fcc": (fcc_neighbors, canonical_fcc),
    "hcp": (hcp_neighbors, canonical_hcp),
}


def frontier(cluster: Cluster | set[Point], neighbors) -> set[Point]:
    C = set(cluster)
    F: set[Point] = set()
    for p in C:
        F.update(neighbors(p))
    return F - C


def internal_edges(cluster: Cluster | set[Point], neighbors) -> int:
    C = set(cluster)
    return sum(sum(q in C for q in neighbors(p)) for p in C) // 2


def boundary_size(cluster: Cluster | set[Point], neighbors) -> int:
    C = set(cluster)
    return 12 * len(C) - 2 * internal_edges(C, neighbors)


def direct_cut_size(cluster: Cluster | set[Point], neighbors) -> int:
    C = set(cluster)
    return sum(sum(q not in C for q in neighbors(p)) for p in C)


def frontier_histogram(cluster: Cluster | set[Point], neighbors) -> Histogram:
    C = set(cluster)
    h = Counter()
    for x in frontier(C, neighbors):
        k = sum(q in C for q in neighbors(x))
        h[k] += 1
    return tuple(sorted(h.items()))


def frontier_weighted_boundary(H: Histogram) -> int:
    return sum(k * count for k, count in H)


def delta_s_for_addition(cluster: Cluster | set[Point], x: Point, neighbors) -> int:
    C = set(cluster)
    assert x not in C and x in frontier(C, neighbors)
    k = sum(q in C for q in neighbors(x))
    return 12 - 2 * k


def set_boundary_after_addition(cluster: Cluster | set[Point], x: Point, neighbors):
    """Return the exact oriented cut after adding x, using only local incidences."""
    C = set(cluster)
    old = {(u, v) for u in C for v in neighbors(u) if v not in C}
    consumed = {(u, x) for u in C if x in neighbors(u)}
    emitted = {(x, y) for y in neighbors(x) if y not in C and y != x}
    predicted = (old - consumed) | emitted
    C1 = C | {x}
    actual = {(u, v) for u in C1 for v in neighbors(u) if v not in C1}
    assert predicted == actual
    return predicted


def second_order_profile(cluster: Cluster | set[Point], x: Point, neighbors):
    """Small residual sufficient to update H exactly after the declared addition x.

    (k_x, A_x, b_x), where A_x(j) counts existing frontier neighbors of x in
    current bin j, and b_x counts neighbors of x that are not yet in C or F(C).
    """
    C = set(cluster)
    F = frontier(C, neighbors)
    assert x in F
    kx = sum(q in C for q in neighbors(x))
    a = Counter()
    for y in neighbors(x):
        if y in F and y != x:
            ky = sum(q in C for q in neighbors(y))
            a[ky] += 1
    b = sum(1 for y in neighbors(x) if y not in C and y not in F)
    return (kx, tuple(sorted(a.items())), b)


def predict_histogram_after_addition(H: Histogram, profile) -> Histogram:
    kx, ah, b = profile
    c = Counter(dict(H))
    c[kx] -= 1
    if c[kx] == 0:
        del c[kx]
    for j, count in ah:
        c[j] -= count
        if c[j] == 0:
            del c[j]
        c[j + 1] += count
    if b:
        c[1] += b
    return tuple(sorted((k, n) for k, n in c.items() if n))


def local_surface_type_fcc(cluster: Cluster | set[Point], center: Point):
    """Canonical occupied-slot mask; exposed mask is its 12-slot complement."""
    C = set(cluster)
    occupied = [q for q in fcc_neighbors(center) if q in C]
    best = None
    for op in FCC_OPS:
        tc = fcc_apply(center, op)
        tq = [fcc_apply(q, op) for q in occupied]
        rel = tuple(sorted((q[0]-tc[0], q[1]-tc[1], q[2]-tc[2]) for q in tq))
        if best is None or rel < best:
            best = rel
    return best


def local_surface_type_hcp(cluster: Cluster | set[Point], center: Point):
    """HCP phase-aware local mask quotiented by the 24 native space-group cosets."""
    C = set(cluster)
    occupied = [q for q in hcp_neighbors(center) if q in C]
    best = None
    for op in HCP_OPS:
        tc = hcp_apply(center, op)
        tq = [hcp_apply(q, op) for q in occupied]
        tz = tc[2] if tc[2] % 2 == 0 else tc[2] - 1
        sig = (
            tc[2] - tz,
            tuple(sorted((q[0]-tc[0], q[1]-tc[1], q[2]-tz) for q in tq)),
        )
        if best is None or repr(sig) < repr(best):
            best = sig
    return best


def surface_type_multiset(world: str, cluster: Cluster | set[Point]):
    C = set(cluster)
    typ = local_surface_type_fcc if world == "fcc" else local_surface_type_hcp
    return tuple(sorted(Counter(repr(typ(C, p)) for p in C).items()))


def one_step_delta_support(cluster: Cluster | set[Point], neighbors) -> tuple[int, ...]:
    return tuple(sorted(12 - 2*k for k, _ in frontier_histogram(cluster, neighbors)))


def two_step_surface_support(cluster: Cluster | set[Point], neighbors) -> tuple[int, ...]:
    """Boolean terminal-S support after exactly two additions, derived via second-order residuals."""
    C = set(cluster)
    S0 = boundary_size(C, neighbors)
    H0 = frontier_histogram(C, neighbors)
    vals = set()
    for x in frontier(C, neighbors):
        kx = sum(q in C for q in neighbors(x))
        S1 = S0 + 12 - 2*kx
        H1 = predict_histogram_after_addition(H0, second_order_profile(C, x, neighbors))
        for k, _count in H1:
            vals.add(S1 + 12 - 2*k)
    return tuple(sorted(vals))


def enumerate_animals(world: str, max_n: int):
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


def greedy_levels(world: str, max_n: int):
    neighbors, canonical = WORLD[world]
    levels: dict[int, set[Cluster]] = {1: {canonical(((0, 0, 0),))}}
    for n in range(1, max_n):
        nxt: set[Cluster] = set()
        for Csig in levels[n]:
            C = set(Csig)
            ks = {x: sum(q in C for q in neighbors(x)) for x in frontier(C, neighbors)}
            best = max(ks.values())
            for x, k in ks.items():
                if k == best:
                    nxt.add(canonical(tuple(sorted(C | {x}))))
        levels[n + 1] = nxt
    return levels


def level_row(level: set[Cluster], neighbors):
    ss = [boundary_size(C, neighbors) for C in level]
    smin = min(ss)
    return {
        "count": len(level),
        "S_min": smin,
        "S_max": max(ss),
        "minimizer_count": sum(s == smin for s in ss),
    }


def validate_symmetries() -> None:
    sample = [(i, j, k) for i in range(-1, 2) for j in range(-1, 2) for k in range(-2, 3)]
    for op in FCC_OPS:
        for p in sample:
            assert {fcc_apply(q, op) for q in fcc_neighbors(p)} == set(fcc_neighbors(fcc_apply(p, op)))
    for op in HCP_OPS:
        for p in sample:
            assert {hcp_apply(q, op) for q in hcp_neighbors(p)} == set(hcp_neighbors(hcp_apply(p, op)))


def validate_levels(world: str, levels) -> None:
    neighbors, _ = WORLD[world]
    for n, level in levels.items():
        for C in level:
            assert len(C) == n
            assert direct_cut_size(C, neighbors) == boundary_size(C, neighbors)
            H = frontier_histogram(C, neighbors)
            assert frontier_weighted_boundary(H) == boundary_size(C, neighbors)
            Cset = set(C)
            for x in frontier(Cset, neighbors):
                s0 = boundary_size(Cset, neighbors)
                ds = delta_s_for_addition(Cset, x, neighbors)
                assert boundary_size(Cset | {x}, neighbors) == s0 + ds
                set_boundary_after_addition(Cset, x, neighbors)
                pred = predict_histogram_after_addition(H, second_order_profile(Cset, x, neighbors))
                assert pred == frontier_histogram(Cset | {x}, neighbors)


EXPECTED = {
    "fcc": {
        1: (1, 12, 12, 1), 2: (1, 22, 22, 1), 3: (4, 30, 32, 1), 4: (20, 36, 42, 1),
        5: (131, 44, 52, 2), 6: (1211, 48, 62, 1), 7: (12734, 54, 72, 1), 8: (144158, 60, 82, 3),
    },
    "hcp": {
        1: (1, 12, 12, 1), 2: (2, 22, 22, 2), 3: (9, 30, 32, 3), 4: (57, 36, 42, 1),
        5: (460, 42, 52, 1), 6: (4641, 48, 62, 1), 7: (50353, 54, 72, 1), 8: (575375, 60, 82, 4),
    },
}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--world", choices=("fcc", "hcp", "both"), default="both")
    ap.add_argument("--max-n", type=int, default=6, help="Python reference is intended for small exact checks; use exhaustive_n8.cpp for N=8.")
    ap.add_argument("--validate", action="store_true")
    args = ap.parse_args()
    validate_symmetries()
    worlds = ("fcc", "hcp") if args.world == "both" else (args.world,)
    payload = {}
    for world in worlds:
        levels = enumerate_animals(world, args.max_n)
        if args.validate:
            validate_levels(world, levels)
        neighbors, _ = WORLD[world]
        rows = {n: level_row(level, neighbors) for n, level in levels.items()}
        for n, row in rows.items():
            if n in EXPECTED[world]:
                assert (row["count"], row["S_min"], row["S_max"], row["minimizer_count"]) == EXPECTED[world][n]
        payload[world] = rows
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
