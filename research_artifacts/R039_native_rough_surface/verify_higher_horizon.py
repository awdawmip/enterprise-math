#!/usr/bin/env python3
"""Exact verifier for the R039 higher-horizon checkpoint.

All theorem-critical computations are integer/combinatorial. Coordinates are only
implementation coordinates for the frozen native contact relations.
"""
from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations, product

Point = tuple[int, int, int]

# ---------- FCC ----------
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

def fcc_apply(p: Point, op) -> Point:
    perm, signs = op
    return tuple(signs[i] * p[perm[i]] for i in range(3))  # type: ignore[return-value]

# ---------- HCP frozen local action ----------
TRI_DIRS = ((1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1))

def hcp_neighbors(p: Point) -> tuple[Point, ...]:
    i, j, k = p
    out = [(i + di, j + dj, k) for di, dj in TRI_DIRS]
    offsets = ((0,0),(-1,0),(0,-1)) if k % 2 == 0 else ((0,0),(1,0),(0,1))
    for dk in (-1, 1):
        for di, dj in offsets:
            out.append((i + di, j + dj, k + dk))
    return tuple(out)

def hcp_r120(p: Point) -> Point:
    i, j, k = p
    e = k & 1
    return (-i - j - e, i, k)

def hcp_apply(p: Point, code) -> Point:
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

HCP_SITE_OPS = tuple(
    (r, s, h, 0)
    for r in range(3)
    for s in (0,1)
    for h in (0,1)
)

# ---------- generic local/group helpers ----------
def cycle_type(p: tuple[int, ...]):
    seen = [False] * len(p)
    out = Counter()
    for i in range(len(p)):
        if seen[i]:
            continue
        j, n = i, 0
        while not seen[j]:
            seen[j] = True
            n += 1
            j = p[j]
        out[n] += 1
    return tuple(sorted(out.items()))

def slot_permutations(neighbors, ops, apply):
    center = (0,0,0)
    slots = tuple(neighbors(center))
    idx = {p:i for i,p in enumerate(slots)}
    result = []
    for op in ops:
        transformed = tuple(apply(q, op) for q in slots)
        assert all(q in idx for q in transformed)
        result.append(tuple(idx[q] for q in transformed))
    return tuple(result)

def orbit_counts(perms):
    seen = set()
    by_degree = Counter()
    for mask in range(1 << 12):
        if mask in seen:
            continue
        orbit = set()
        for p in perms:
            image = 0
            for i in range(12):
                if mask >> i & 1:
                    image |= 1 << p[i]
            orbit.add(image)
        seen.update(orbit)
        by_degree[mask.bit_count()] += 1
    return [by_degree[d] for d in range(13)]

def burnside_counts(perms):
    total = [0] * 13
    cts = Counter(cycle_type(p) for p in perms)
    for ct, multiplicity in cts.items():
        poly = [1]
        for cycle_len, number in ct:
            for _ in range(number):
                nxt = [0] * (len(poly) + cycle_len)
                for i, a in enumerate(poly):
                    nxt[i] += a
                    nxt[i + cycle_len] += a
                poly = nxt
        for i, a in enumerate(poly):
            total[i] += multiplicity * a
    assert all(v % len(perms) == 0 for v in total)
    return [v // len(perms) for v in total], cts

# ---------- surface/frontier ----------
def frontier(C, neighbors=fcc_neighbors):
    C = set(C)
    F = set()
    for p in C:
        F.update(neighbors(p))
    return F - C

def internal_edges(C, neighbors=fcc_neighbors):
    C = set(C)
    return sum(sum(q in C for q in neighbors(p)) for p in C) // 2

def surface(C, neighbors=fcc_neighbors):
    return 12 * len(C) - 2 * internal_edges(C, neighbors)

def histogram(C, neighbors=fcc_neighbors):
    C = set(C)
    return tuple(sorted(Counter(
        sum(q in C for q in neighbors(x))
        for x in frontier(C, neighbors)
    ).items()))

def reduced_profile(C, x, neighbors=fcc_neighbors):
    C = set(C)
    F = frontier(C, neighbors)
    k = sum(q in C for q in neighbors(x))
    A = Counter()
    for y in neighbors(x):
        if y in F and y != x:
            ky = sum(q in C for q in neighbors(y))
            A[ky] += 1
    b_direct = sum(1 for y in neighbors(x) if y not in C and y not in F)
    b_reconstructed = 12 - k - sum(A.values())
    assert b_direct == b_reconstructed
    return (k, tuple(sorted(A.items())))

def reduced_R2(C, neighbors=fcc_neighbors):
    return tuple(sorted(
        (reduced_profile(C, x, neighbors) for x in frontier(C, neighbors)),
        key=repr
    ))

# ---------- fixed-horizon order-free support ----------
def reachable_added_sets(C, h, neighbors=fcc_neighbors):
    C = frozenset(C)
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

def added_contact_count(C, A, neighbors=fcc_neighbors):
    C, A = set(C), set(A)
    cross = sum(1 for a in A for q in neighbors(a) if q in C)
    inner = sum(sum(q in A for q in neighbors(a)) for a in A) // 2
    return cross + inner

def terminal_support(C, h, neighbors=fcc_neighbors):
    S0 = surface(C, neighbors)
    vals, qmax = set(), -1
    for A in reachable_added_sets(C, h, neighbors):
        q = added_contact_count(C, A, neighbors)
        qmax = max(qmax, q)
        vals.add(S0 + 12*h - 2*q)
        assert surface(set(C) | set(A), neighbors) == S0 + 12*h - 2*q
    return tuple(sorted(vals)), qmax

# ---------- exact FCC zonotope volume ----------
def det3(a, b, c):
    return (
        a[0]*(b[1]*c[2]-b[2]*c[1])
        - a[1]*(b[0]*c[2]-b[2]*c[0])
        + a[2]*(b[0]*c[1]-b[1]*c[0])
    )

def zonotope_volume():
    reps = (
        (0,1,-1), (0,1,1),
        (1,-1,0), (1,0,-1), (1,0,1), (1,1,0),
    )
    dets = [abs(det3(*tri)) for tri in combinations(reps, 3)]
    assert Counter(dets) == Counter({2:16, 0:4})
    return 8 * sum(dets)

def main():
    fcc_perms = slot_permutations(fcc_neighbors, FCC_OPS, fcc_apply)
    hcp_perms = slot_permutations(hcp_neighbors, HCP_SITE_OPS, hcp_apply)

    fcc_expected = [1,1,4,9,18,24,30,24,18,9,4,1,1]
    hcp_expected = [1,2,10,25,54,78,96,78,54,25,10,2,1]

    assert orbit_counts(fcc_perms) == fcc_expected
    assert orbit_counts(hcp_perms) == hcp_expected

    fcc_burnside, fcc_ct = burnside_counts(fcc_perms)
    hcp_burnside, hcp_ct = burnside_counts(hcp_perms)
    assert fcc_burnside == fcc_expected
    assert hcp_burnside == hcp_expected

    C = (
        (0,0,0),(0,0,2),(0,1,-1),
        (1,-1,4),(1,0,1),(1,0,3),
    )
    D = (
        (0,0,0),(0,0,2),(0,1,-1),
        (0,1,1),(1,0,3),(1,1,-2),
    )
    assert surface(C) == surface(D) == 62
    assert histogram(C) == histogram(D) == ((1,24),(2,10),(3,6))
    assert reduced_R2(C) == reduced_R2(D)

    support_C, lambda4_C = terminal_support(C, 4)
    support_D, lambda4_D = terminal_support(D, 4)
    assert support_C == (82,84,86,88,90,92,94,96,98,100,102)
    assert support_D == (80,82,84,86,88,90,92,94,96,98,100,102)
    assert (lambda4_C, lambda4_D) == (14, 15)

    A_D = {(1,0,1),(1,1,0),(1,0,-1),(1,1,2)}
    assert added_contact_count(D, A_D) == 15
    assert surface(set(D) | A_D) == 80

    vol_phys = zonotope_volume()
    assert vol_phys == 256
    assert vol_phys // 2 == 128

    print("FCC alphabet:", fcc_expected, "total", sum(fcc_expected))
    print("HCP alphabet:", hcp_expected, "total", sum(hcp_expected))
    print("FCC cycle types:", dict(fcc_ct))
    print("HCP cycle types:", dict(hcp_ct))
    print("CE6 support C:", support_C, "Lambda4", lambda4_C)
    print("CE6 support D:", support_D, "Lambda4", lambda4_D)
    print("FCC zonotope volumes: physical=256 lattice-normalized=128")
    print("ALL_HIGHER_HORIZON_CHECKS_OK")

if __name__ == "__main__":
    main()
