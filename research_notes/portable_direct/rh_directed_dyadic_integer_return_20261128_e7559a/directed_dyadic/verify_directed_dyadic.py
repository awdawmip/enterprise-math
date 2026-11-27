#!/usr/bin/env python3
"""Exact finite author checks for directed dyadic Green transfer.

The all-length theorem is proved in DIRECTED_DYADIC_GREEN_TRANSFER.md.
No old certificate, prime sieve, source exponential or road point is run here.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


def pav(a):
    """Projection onto the nonincreasing cone; return maximal constant pools."""
    pools = []
    for i, x in enumerate(a):
        pools.append([i, i + 1, F(x)])
        while len(pools) >= 2:
            l, r = pools[-2:]
            if l[2] / (l[1] - l[0]) > r[2] / (r[1] - r[0]):
                break
            pools[-2:] = [[l[0], r[1], l[2] + r[2]]]
    fitted = []
    for lo, hi, total in pools:
        fitted.extend([total / (hi - lo)] * (hi - lo))
    distance = sum((x - y) ** 2 for x, y in zip(a, fitted))
    return fitted, pools, distance


def powers(h):
    d = 1
    while d < h:
        yield d
        d *= 2


def qplus(a):
    return sum(max(a[i + d] - a[i], F(0)) ** 2
               for d in powers(len(a)) for i in range(len(a) - d))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def check_pav(a, fitted, pools):
    assert all(fitted[i] >= fitted[i + 1] for i in range(len(a) - 1))
    for lo, hi, total in pools:
        mean = total / (hi - lo)
        running = F(0)
        for x in a[lo:hi]:
            running += x - mean
            assert running <= 0
        assert running == 0


def merge_parity_projection(a):
    even, _, _ = pav(a[::2])
    odd, _, _ = pav(a[1::2])
    p = [even[i // 2] if i % 2 == 0 else odd[i // 2]
         for i in range(len(a))]
    assert all(p[i] >= p[i + 2] for i in range(len(a) - 2))
    rises = [i for i in range(len(a) - 1) if p[i] < p[i + 1]]
    assert all(rises[j + 1] > rises[j] + 1 for j in range(len(rises) - 1))
    c = p.copy()
    for i in rises:
        c[i] = c[i + 1] = (p[i] + p[i + 1]) / 2
    assert all(c[i] >= c[i + 1] for i in range(len(c) - 1))
    d = [x - y for x, y in zip(p, c)]
    assert dot(c, d) == 0
    assert dot(d, d) <= dot(p, p)
    return p, c, d


def check_directed_vectors():
    count = pool_count = 0
    max_ratio = F(0)
    for h in range(1, 9):
        for raw in product((-2, 0, 3), repeat=h):
            a = list(map(F, raw))
            fit, pools, distance = pav(a)
            check_pav(a, fit, pools)
            adj = sum(max(a[i + 1] - a[i], F(0)) ** 2 for i in range(h - 1))
            recursive = pav(a[::2])[2] + pav(a[1::2])[2] + adj / 2
            assert distance <= recursive
            q = qplus(a)
            assert 2 * distance <= q
            if q:
                max_ratio = max(max_ratio, distance / q)
            for lo, hi, total in pools:
                mean = total / (hi - lo)
                z = [x - mean for x in a[lo:hi]]
                p, c, d = merge_parity_projection(z)
                assert dot(z, p) == dot(p, p)
                assert dot(z, c) <= 0
                assert dot(p, p) <= dot(z, d)
                za = sum(max(z[i + 1] - z[i], F(0)) ** 2
                         for i in range(len(z) - 1))
                assert 2 * dot(p, p) <= za
                pool_count += 1
            count += 1
    for h in range(2, 34):
        a = list(map(F, [0, 1] + list(range(-2, -h, -1))))
        assert len(a) == h
        assert pav(a)[2] == F(1, 2)
        assert qplus(a) == 1
    return {
        "alphabet": [-2, 0, 3], "lengths": [1, 8],
        "vectors": count, "complete_pools_checked": pool_count,
        "max_distance_over_directed_energy": str(max_ratio),
        "sharpness_family_lengths": [2, 33], "sharpness_cases": 32,
    }


def abel(v, L):
    return [v[i] / (L + i)
            + sum(v[j] / ((L + j) * (L + j + 1)) for j in range(i))
            for i in range(len(v))]


def green_values(b, L):
    h = len(b) + 1
    R = L + h
    return [sum(F(min(i, j) * (h - max(i, j)), h) * b[j - 1] / (L + j)
                for j in range(1, h)) for i in range(h + 1)]


def interpolate(values, grid):
    out = [F(0)] * len(values)
    for l, r in zip(grid, grid[1:]):
        for n in range(l, r + 1):
            out[n] = (F(r - n, r - l) * values[l]
                      + F(n - l, r - l) * values[r])
    return out


def positive_energy(values, L):
    return sum(max(v, F(0)) ** 2 / (L + i) ** 2 for i, v in enumerate(values))


def source_case(h, kind):
    if kind == 0:
        return [F(1)] * (h - 1)
    if kind == 1:
        return [F(-1)] * (h - 1)
    if kind == 2:
        return [F((7 * j + h) % 11 - 5, 1 + j % 3) for j in range(1, h)]
    return [F(1 if j <= h // 2 else -2, 1 + j % 2) for j in range(1, h)]


def check_weighted_green():
    sources = meshes = 0
    summaries = []
    for h in range(2, 18):
        L = 2 * h + 3
        R = L + h
        for kind in range(4):
            b = source_case(h, kind)
            A, B = [F(0)], [F(0)]
            for j, x in enumerate(b, 1):
                A.append(A[-1] + x)
                B.append(B[-1] + x / (L + j))
            assert abel(A, L) == B
            mA, _, dA = pav(A)
            _, _, dB = pav(B)
            tm = abel(mA, L)
            assert all(tm[i] >= tm[i + 1] for i in range(h - 1))
            for i in range(1, h):
                assert tm[i] - tm[i - 1] == (mA[i] - mA[i - 1]) / (L + i)
            normT = F(R, L * L * (L + 1))
            assert dB <= normT * dA
            q = qplus(A)
            assert 2 * dA <= q
            U = green_values(b, L)
            grids = {tuple(range(h + 1)), (0, h // 2, h), tuple(sorted({0, 1, h - 1, h}))}
            best_energy = F(0)
            C = F(h * h, 8 * L * L)
            for grid in sorted(grids):
                V = interpolate(U, grid)
                E = positive_energy(V, L)
                assert E <= C * dB <= C * normT * dA <= C * normT * q / 2
                if kind == 1:
                    assert E == dA == dB == q == 0
                best_energy = max(best_energy, E)
                meshes += 1
            summaries.append({"L": L, "h": h, "source_kind": kind,
                              "D_A": str(dA), "Q_directed": str(q),
                              "max_checked_positive_energy": str(best_energy)})
            sources += 1
    return {"source_cases": sources, "mesh_cases": meshes,
            "lengths": [2, 17], "cases": summaries}


def check_disjoint_cover():
    X, Y = 32, 64
    cells = [(32, 37), (37, 48), (48, 64)]
    H = max(r - l for l, r in cells)
    outputs = []
    for kind in range(4):
        b = {n: F(((7 * n + 3 * kind) % 13) - 6, 1 + n % 3)
             for n in range(X + 1, Y)}
        if kind == 0:
            b = {n: F(1) for n in b}
        if kind == 1:
            b = {n: F(-1) for n in b}
        lhs = F(0)
        for L, R in cells:
            h = R - L
            U = green_values([b[n] for n in range(L + 1, R)], L)
            grid = tuple(sorted({0, 1, h // 3, h - 1, h}))
            lhs += positive_energy(interpolate(U, grid), L)
        J = {}
        for d in powers(H):
            J[d] = sum(max(sum(b[n] for n in range(u + 1, u + d + 1)), F(0)) ** 2
                       for u in range(X, Y - d))
        rhs = F(H * H, 8 * X ** 4) * sum(J.values())
        assert lhs <= rhs
        K = max((q / (X * d) for d, q in J.items()), default=F(0))
        coarse_squared = K * F(H ** 3, 4 * X ** 3)
        assert rhs <= coarse_squared
        outputs.append({"source_kind": kind, "positive_energy": str(lhs),
                        "directed_cover_upper": str(rhs),
                        "K_plus": str(K), "coarse_root_bound_squared": str(coarse_squared)})
    return {"X": X, "Y": Y, "cells": cells, "H": H, "cases": outputs}


def main():
    result = {"schema": "DIRECTED_DYADIC_GREEN_AUTHOR_CHECK_V1",
              "date_hong_kong": "2026-11-28",
              "arithmetic": "Python standard-library Fraction; exact rational",
              "claim_scope": "finite implementation checks; all-parameter theorem is analytic",
              "vectors": check_directed_vectors(),
              "weighted_green": check_weighted_green(),
              "disjoint_cover": check_disjoint_cover(),
              "new_prime_sieve": False,
              "new_direct_source_exponentials": 0,
              "old_certificates_rerun": False}
    path = Path(__file__).with_name("directed_dyadic_certificate.json")
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print("PASS:", result["vectors"]["vectors"], "vectors;",
          result["vectors"]["complete_pools_checked"], "complete pools;",
          result["weighted_green"]["source_cases"], "weighted sources;",
          result["weighted_green"]["mesh_cases"], "meshes; 4 disjoint covers.")


if __name__ == "__main__":
    main()
