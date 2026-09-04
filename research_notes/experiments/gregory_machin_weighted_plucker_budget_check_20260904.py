#!/usr/bin/env python3
"""Finite certificates for the weighted Pluecker resource theorem in #1160.

The theorem itself is an exact inequality proved in the companion note.  This
checker does not substitute numerical testing for proof.  It verifies:
- primitive wedge normalization and the exact triangle-inequality majorant;
- the current support-three Pareto examples in planes (5,13) and (5,17);
- the rank-two seed-bound obstruction family K=1..12, where basis free norm is
  quadratic in atom height while primitive weighted Pluecker height stays small.
"""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOGO = HERE / "gregory_machin_rank2_seed_bound_nogo_20260904.py"
spec = importlib.util.spec_from_file_location("nogo", NOGO)
nogo = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(nogo)


def primitive_wedge(v: dict[int, int], w: dict[int, int]):
    ps = sorted(set(v) | set(w))
    raw = {}
    g = 0
    for i, p in enumerate(ps):
        for q in ps[i + 1 :]:
            m = v.get(p, 0) * w.get(q, 0) - v.get(q, 0) * w.get(p, 0)
            if m:
                raw[(p, q)] = m
                g = math.gcd(g, abs(m))
    assert g > 0
    prim = {pq: m // g for pq, m in raw.items()}
    first = next(iter(sorted(prim)))
    if prim[first] < 0:
        prim = {pq: -m for pq, m in prim.items()}
    return raw, prim, g


def X(v: dict[int, int]) -> float:
    return sum(abs(a) * math.log(p) for p, a in v.items())


def weighted_height(m: dict[tuple[int, int], int]) -> float:
    return sum(abs(a) * math.log(p) * math.log(q) for (p, q), a in m.items())


def triangle_majorant(v: dict[int, int], w: dict[int, int]) -> float:
    ps = sorted(set(v) | set(w))
    return sum(
        (
            abs(v.get(p, 0)) * abs(w.get(q, 0))
            + abs(v.get(q, 0)) * abs(w.get(p, 0))
        )
        * math.log(p)
        * math.log(q)
        for i, p in enumerate(ps)
        for q in ps[i + 1 :]
    )


def check_pair(v, w, H: int):
    raw, omega, g = primitive_wedge(v, w)
    P = weighted_height(omega)
    W = weighted_height(raw)
    T = triangle_majorant(v, w)
    xv, xw = X(v), X(w)
    L = math.log(2 * H * H)
    assert P <= W + 1e-12
    assert W <= T + 1e-12
    assert abs(T - (xv * xw - sum(abs(v.get(p, 0) * w.get(p, 0)) * math.log(p) ** 2 for p in set(v) | set(w)))) < 1e-10
    assert xv < L + 1e-12 and xw < L + 1e-12
    assert P < L * L + 1e-12
    return omega, g, P, L * L


def main():
    # Current combined-Pareto support-three examples.
    examples = [
        (
            "B21 plane(5,13)",
            {5: 3, 13: -1},
            {5: -5, 13: 0},
            79,
        ),
        (
            "B49 plane(5,17)",
            {5: 9, 17: -1},
            {5: -2, 17: 7},
            143237,
        ),
    ]
    for name, v, w, H in examples:
        omega, g, P, budget = check_pair(v, w, H)
        print(f"{name}: gcd_raw={g} omega={omega} P={P:.12f} budget={budget:.12f}")

    # Quadratic basis-norm obstruction family.  The plane gets harder in basis
    # norm, but its primitive exterior state has minors (-K,K,1) and remains
    # within the logarithmic-square budget of its actual endpoint realization.
    print("K  H_actual  basis_norm_lower  Plucker_height  budget  ratio")
    for K in range(1, 13):
        endpoints = nogo.endpoint_choices(K)
        assert endpoints
        # Use the smallest maximum denominator among exact C8 endpoint branch choices.
        H = min(max(atom[0] for atom in row[1]) for row in endpoints)
        v = {5: K, 13: 1}
        w = {5: K, 17: 1}
        omega, g, P, budget = check_pair(v, w, H)
        assert g == 1
        assert omega == {(5, 13):  K, (5, 17): -K, (13, 17): -1} or omega == {(5, 13): -K, (5, 17): K, (13, 17): 1}
        # primitive_wedge fixes the first nonzero sign positive.
        assert abs(omega[(5, 13)]) == K
        basis_lower = 5**K
        print(f"{K:2d} {H:9d} {basis_lower:16d} {P:14.8f} {budget:14.8f} {P/budget:.8f}")

    print("weighted Plucker resource certificates: PASS")


if __name__ == "__main__":
    main()
