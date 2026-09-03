#!/usr/bin/env python3
"""Exact support-four Gaussian valuation circuit census for #1160.

Search scope:
- 2 <= D <= height (default 12943);
- four distinct denominators;
- the union of their split-prime valuation supports has size exactly 3;
- free valuation columns form a rational circuit (rank 3, every triple independent);
- the primitive circuit can be scaled to the diagonal C8 torsion target.

Endpoint certification is exact integer arithmetic. Floating logarithms are used only
for post-certification Lehmer-measure ranking.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import math
from collections import defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
BASE = HERE / "gregory_machin_gaussian_triple_census_20260903.py"
spec = importlib.util.spec_from_file_location("gm3", BASE)
gm3 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(gm3)


def det3(m):
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def primitive_circuit_coefficients(quad, primes):
    rows = []
    eps = []
    for p in primes:
        rows.append([dict(gm3.signature(D)[1]).get(p, 0) for D in quad])
    eps = [gm3.signature(D)[0] for D in quad]

    # Kernel cofactors of a 3x4 matrix. All four must be nonzero for a circuit.
    cof = []
    for j in range(4):
        minor = [[row[k] for k in range(4) if k != j] for row in rows]
        cof.append(((-1) ** j) * det3(minor))
    if any(c == 0 for c in cof):
        return None

    g = 0
    for c in cof:
        g = math.gcd(g, abs(c))
    c0 = [c // g for c in cof]
    for c in c0:
        if c:
            if c < 0:
                c0 = [-x for x in c0]
            break

    # Exact free-row verification.
    for row in rows:
        assert sum(a * b for a, b in zip(row, c0)) == 0

    torsion = sum(a * b for a, b in zip(eps, c0)) % 8
    if torsion % 2 == 0:
        return None
    scale = min((torsion, torsion - 8), key=abs)
    coeffs = tuple(scale * c for c in c0)
    assert sum(a * b for a, b in zip(eps, coeffs)) % 8 == 1
    return coeffs


def support_groups(core):
    groups = defaultdict(list)
    for D in core:
        s = tuple(p for p, _ in gm3.signature(D)[1])
        if len(s) <= 3:
            groups[s].append(D)
    return groups


def all_three_prime_unions(groups):
    keys1 = [s for s in groups if len(s) == 1]
    keys2 = [s for s in groups if len(s) == 2]
    keys3 = [s for s in groups if len(s) == 3]
    out = set(keys3)

    for a, b in itertools.combinations(keys2, 2):
        u = tuple(sorted(set(a) | set(b)))
        if len(u) == 3:
            out.add(u)
    for a in keys2:
        for b in keys1:
            u = tuple(sorted(set(a) | set(b)))
            if len(u) == 3:
                out.add(u)
    for p in itertools.combinations(sorted(s[0] for s in keys1), 3):
        out.add(p)
    return out


def candidates_inside_prime_triple(groups, primes):
    ds = []
    for r in (1, 2, 3):
        for subset in itertools.combinations(primes, r):
            ds.extend(groups.get(tuple(sorted(subset)), ()))
    return sorted(set(ds))


def census(height: int):
    core, removed, core_prime_count = gm3.leaf_prime_core(height)
    groups = support_groups(core)
    prime_triples = all_three_prime_unions(groups)

    viable_prime_triples = []
    for pset in prime_triples:
        ds = candidates_inside_prime_triple(groups, pset)
        if len(ds) >= 4:
            viable_prime_triples.append((pset, ds))

    seen_quads = set()
    circuits = []
    for pset, ds in viable_prime_triples:
        for quad in itertools.combinations(ds, 4):
            if quad in seen_quads:
                continue
            seen_quads.add(quad)
            actual = tuple(
                sorted(
                    set().union(
                        *(set(p for p, _ in gm3.signature(D)[1]) for D in quad)
                    )
                )
            )
            if len(actual) != 3:
                continue
            coeffs = primitive_circuit_coefficients(quad, actual)
            if coeffs is None:
                continue
            mu = sum(1.0 / math.log10(D) for D in quad)
            circuits.append((mu, sum(abs(c) for c in coeffs), quad, coeffs, actual))

    circuits.sort()
    return {
        "height": height,
        "core_size": len(core),
        "removed": removed,
        "core_prime_count": core_prime_count,
        "three_prime_unions": len(prime_triples),
        "viable_prime_triples": len(viable_prime_triples),
        "checked_quads": len(seen_quads),
        "endpoint_circuits": len(circuits),
        "best": circuits,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--height", type=int, default=12943)
    parser.add_argument("--top", type=int, default=10)
    args = parser.parse_args()

    result = census(args.height)
    for key in (
        "height",
        "core_size",
        "removed",
        "core_prime_count",
        "three_prime_unions",
        "viable_prime_triples",
        "checked_quads",
        "endpoint_circuits",
    ):
        print(f"{key}={result[key]}")
    print("best_by_Lehmer_measure:")
    for mu, l1, quad, coeffs, primes in result["best"][: args.top]:
        print(
            f"  mu={mu:.15f} L1={l1:4d} D={quad} c={coeffs} primes={primes}"
        )

    if args.height == 12943:
        assert result["core_size"] == 4773
        assert result["removed"] == 8169
        assert result["core_prime_count"] == 1009
        assert result["checked_quads"] == 87436
        assert result["endpoint_circuits"] == 2159
        mu, l1, quad, coeffs, primes = result["best"][0]
        assert quad == (57, 239, 682, 12943)
        assert coeffs == (44, 7, -12, 24)
        assert primes == (5, 13, 61)
        assert l1 == 87
        assert abs(mu - 1.5860413585818451) < 1e-14
        print("H=12943 support-four regression certificate: PASS")


if __name__ == "__main__":
    main()
