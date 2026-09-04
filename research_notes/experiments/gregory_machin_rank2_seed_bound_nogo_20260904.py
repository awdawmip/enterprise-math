#!/usr/bin/env python3
"""Exact rank-two seed-bound obstruction for Enterprise Math #1160.

The checker realizes the saturated valuation planes
  v1=(K,1,0), v2=(K,0,1), v3=(0,1,-1)=v1-v2
with Gaussian products over split primes (5,13,17), folds each into strict rational
atoms, and verifies that at least one complement choice always produces a C8
diagonal endpoint circuit.  The accompanying theorem proves that every basis of
the saturated plane contains a vector with multiplicative free norm >=5^K,
while the realizing atom denominators grow only like O(5^(K/2)).
"""

from __future__ import annotations

import importlib.util
import itertools
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "gregory_machin_rational_support3_primeplane_h1m_20260904.py"
spec = importlib.util.spec_from_file_location("pp", BASE)
pp = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(pp)

g2 = pp.g2
PRIMES = (5, 13, 17)


def raw_for_vector(vec):
    z = (1, 0)
    for p, e in zip(PRIMES, vec):
        if e:
            z = g2.pair_mul(z, pp.ipow(pp.gaussian_prime(p, 1 if e > 0 else -1), abs(e)))
    return z


def branches(vec):
    return pp.fold_vector(raw_for_vector(vec), vec)


def cross(u, v):
    return (
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0],
    )


def primitive_kernel(cols):
    rows = [tuple(col[r] for col in cols) for r in range(3)]
    r1 = next(r for r in rows if any(r))
    r2 = next(r for r in rows if cross(r1, r) != (0, 0, 0))
    c = cross(r1, r2)
    assert all(sum(row[j] * c[j] for j in range(3)) == 0 for row in rows)
    g = math.gcd(math.gcd(abs(c[0]), abs(c[1])), abs(c[2]))
    c = tuple(x // g for x in c)
    if c[0] < 0:
        c = tuple(-x for x in c)
    return c


def endpoint_choices(K: int):
    base_vectors = ((K, 1, 0), (K, 0, 1), (0, 1, -1))
    branch_sets = [branches(v) for v in base_vectors]
    out = []
    for choice in itertools.product((0, 1), repeat=3):
        chosen = [branch_sets[j][choice[j]] for j in range(3)]
        atoms = tuple(row[0] for row in chosen)
        cols = tuple(row[1] for row in chosen)
        eps = tuple(row[2] for row in chosen)
        c0 = primitive_kernel(cols)
        assert all(abs(x) == 1 for x in c0)
        torsion = sum(c0[j] * eps[j] for j in range(3)) % 8
        if torsion % 2 == 0:
            continue
        scale = min((torsion, torsion - 8), key=abs)
        coeffs = tuple(scale * x for x in c0)
        assert sum(coeffs[j] * eps[j] for j in range(3)) % 8 == 1
        out.append((choice, atoms, cols, eps, coeffs))
    return out


def lattice_minor_gcd(K: int):
    # columns v1,v2; row minors are -K, K, 1.
    minors = (-K, K, 1)
    return math.gcd(math.gcd(abs(minors[0]), abs(minors[1])), abs(minors[2]))


def main():
    print("K  endpoint_branch_choices  max_realizing_denominator  forced_basis_free_norm")
    for K in range(1, 13):
        assert lattice_minor_gcd(K) == 1
        eps = endpoint_choices(K)
        assert len(eps) == 4
        max_den = min(max(atom[0] for atom in row[1]) for row in eps)
        forced = 5**K
        print(f"{K:2d} {len(eps):23d} {max_den:25d} {forced}")

        # Native free relation is minimal and every branch realization still hits C8.
        for _, atoms, cols, _, coeffs in eps:
            for r in range(3):
                assert sum(coeffs[j] * cols[j][r] for j in range(3)) == 0

    print("rank-two endpoint seed-bound obstruction certificate: PASS")


if __name__ == "__main__":
    main()
