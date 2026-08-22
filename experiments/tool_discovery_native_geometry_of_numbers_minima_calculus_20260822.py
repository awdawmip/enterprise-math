#!/usr/bin/env python3
"""Deterministic finite checks for the native finite-fiber minima calculus.

No external dependencies. This checker validates the finite quotient/fiber
identities, the S_12 modular-sector example, and the PathSqrt_E square-norm
example used by the accompanying research note.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from math import comb, isqrt


def occupied(labels, subset):
    return {labels[i] for i in subset}


def defect(labels, subset):
    return len(subset) - len(occupied(labels, subset))


def witness_forest(labels, subset):
    buckets = {}
    for i in subset:
        buckets.setdefault(labels[i], []).append(i)
    edges = []
    for bucket in buckets.values():
        if bucket:
            root = bucket[0]
            edges.extend((root, v) for v in bucket[1:])
    return edges


def check_generic():
    cases = 0
    for n in range(1, 9):
        for modulus in range(1, min(n, 4) + 1):
            labels = [i % modulus for i in range(n)]
            for mask in range(1 << n):
                subset = [i for i in range(n) if mask & (1 << i)]
                kappa = len(occupied(labels, subset))
                delta = defect(labels, subset)
                edges = witness_forest(labels, subset)
                assert delta == len(subset) - kappa
                assert (delta == 0) == (len(subset) == kappa)
                assert len(edges) == delta
                assert all(u != v and labels[u] == labels[v] for u, v in edges)
                cases += 1

            for mask in range(1 << n):
                A = [i for i in range(n) if mask & (1 << i)]
                dA = defect(labels, A)
                for x in range(n):
                    if x not in A:
                        B = A + [x]
                        assert defect(labels, B) in (dA, dA + 1)

    for n in range(1, 8):
        labels = [i % 3 for i in range(n)]
        universe = range(n)
        for assignment in itertools.product((0, 1, 2), repeat=n):
            A = [i for i in universe if assignment[i] == 1]
            B = [i for i in universe if assignment[i] == 2]
            lhs = defect(labels, A + B)
            rhs = (
                defect(labels, A)
                + defect(labels, B)
                + len(occupied(labels, A) & occupied(labels, B))
            )
            assert lhs == rhs

    return {"generic_subset_cases": cases}


def sector_ball(R):
    return [
        (a, b, 0)
        for a in range(R + 1)
        for b in range(isqrt(R * R - a * a) + 1)
    ]


def residue(point, m):
    a, b, c = point
    assert c == 0
    return (a % m, b % m)


def first_collision(points, m):
    seen = {}
    for p in points:
        q = residue(p, m)
        if q in seen:
            return seen[q], p, q
        seen[q] = p
    return None


def check_spatial():
    rows = []
    for m in range(2, 21):
        capacity = m * m

        extremal = [(a, b, 0) for a in range(m) for b in range(m)]
        assert len(extremal) == capacity
        assert len({residue(p, m) for p in extremal}) == capacity
        assert first_collision(extremal, m) is None

        enlarged = [(a, b, 0) for a in range(m + 1) for b in range(m + 1)]
        assert len(enlarged) > capacity
        assert first_collision(enlarged, m) is not None

        R = 0
        while len(sector_ball(R)) <= capacity:
            R += 1
        pts = sector_ball(R)
        prev_count = len(sector_ball(R - 1)) if R else 0
        col = first_collision(pts, m)
        assert col is not None
        assert prev_count <= capacity < len(pts)
        rows.append(
            {
                "m": m,
                "capacity": capacity,
                "first_ball_R_guaranteed_by_capacity": R,
                "previous_ball_count": prev_count,
                "ball_count": len(pts),
                "sample_collision": [list(col[0]), list(col[1]), list(col[2])],
            }
        )
    return {"spatial_modular_sector": rows}


def groots_square(r):
    target = r * r
    out = []
    for a in range(r + 1):
        b2 = target - a * a
        b = isqrt(b2)
        if b * b == b2:
            out.append((a, b))
    return out


def path_fiber_size(root):
    a, b = root
    return comb(a + b, a)


def check_roots():
    for r in range(1, 129):
        roots = groots_square(r)
        assert roots
        assert all(a * a + b * b == r * r for a, b in roots)
        total = sum(path_fiber_size(x) for x in roots)
        capacity = len(roots)
        assert total >= capacity
        delta = total - capacity
        assert delta == sum(path_fiber_size(x) - 1 for x in roots)

    r = 50
    roots = groots_square(r)
    expected_roots = [(0, 50), (14, 48), (30, 40), (40, 30), (48, 14), (50, 0)]
    assert roots == expected_roots
    sizes = [path_fiber_size(x) for x in roots]
    expected_sizes = [
        1,
        29078984349975,
        55347740058143507128,
        55347740058143507128,
        29078984349975,
        1,
    ]
    assert sizes == expected_sizes
    total = sum(sizes)
    assert total == 110695538274255714208
    assert total - len(roots) == 110695538274255714202
    return {
        "root_regression_r_max": 128,
        "N2500": {
            "roots": [list(x) for x in roots],
            "fiber_sizes": sizes,
            "trace_capacity": len(roots),
            "total_paths": total,
            "collision_defect": total - len(roots),
        },
    }


def main():
    result = {}
    result.update(check_generic())
    result.update(check_spatial())
    result.update(check_roots())
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps({"sha256": digest, "result": result}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
