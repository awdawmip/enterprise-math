#!/usr/bin/env python3
"""Exact H=1000 support-two rational-atom census for Enterprise Math #1160.

Universe: all primitive 0<a<b<=H. Endpoint feasibility is exact Gaussian free
valuation + C8 torsion arithmetic. Floating logarithms are used only for the
post-certification generalized Lehmer coordinate. The final reported Pareto set
also carries a finite tangent-sheet certificate.
"""

from __future__ import annotations

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

HEIGHT = 1000


def general_signature(b: int, a: int):
    assert 0 < a < b and math.gcd(a, b) == 1
    z = (b, a)
    coords = {}
    for p, e in gm3.factorint(b * b + a * a).items():
        if p == 2:
            continue
        assert p % 4 == 1, (b, a, p)
        pi = gm3.sum_two_squares_prime(p)
        pib = (pi[0], -pi[1])
        vp = vb = 0
        while True:
            q = gm3.gaussian_div_exact(z, pi)
            if q is None:
                break
            z = q
            vp += 1
        while True:
            q = gm3.gaussian_div_exact(z, pib)
            if q is None:
                break
            z = q
            vb += 1
        assert vp + vb == e
        if vp != vb:
            coords[p] = vp - vb

    ramified = 0
    while True:
        q = gm3.gaussian_div_exact(z, (1, 1))
        if q is None:
            break
        z = q
        ramified += 1

    unit_exp = {
        (1, 0): 0,
        (0, 1): 1,
        (-1, 0): 2,
        (0, -1): 3,
    }.get(z)
    assert unit_exp is not None, (b, a, z)
    eps = (ramified + 2 * unit_exp) % 8
    return eps, tuple(sorted(coords.items()))


def normalized_free_direction(items):
    if not items:
        return None
    g = 0
    for _, value in items:
        g = math.gcd(g, abs(value))
    key = [(p, value // g) for p, value in items]
    if key[0][1] < 0:
        key = [(p, -value) for p, value in key]
    key = tuple(key)
    first_p, first_v = key[0]
    scalar = dict(items)[first_p] // first_v
    return key, scalar


def generalized_mu(v1, v2):
    return sum(1.0 / math.log10(b / a) for b, a in (v1, v2))


def pair_mul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def tangent_sheet(v1, v2, coeffs):
    z = (1, 0)
    sheet = 0
    crossings = 0
    for (b, a), coefficient in ((v1, coeffs[0]), (v2, coeffs[1])):
        sign = 1 if coefficient > 0 else -1
        factor = (b, sign * a)
        for _ in range(abs(coefficient)):
            old = z
            new = pair_mul(z, factor)
            g = math.gcd(abs(new[0]), abs(new[1]))
            new = (new[0] // g, new[1] // g)
            if old[0] != 0 and new[0] != 0 and (old[0] > 0) != (new[0] > 0):
                sheet += sign
                crossings += 1
            z = new
    return z, sheet, crossings


def census(height: int = HEIGHT):
    groups = defaultdict(list)
    atom_count = 0

    for b in range(2, height + 1):
        for a in range(1, b):
            if math.gcd(a, b) != 1:
                continue
            atom_count += 1
            eps, items = general_signature(b, a)
            norm = normalized_free_direction(items)
            # A strict positive rational slope cannot be a useful torsion-only atom.
            if norm is None:
                continue
            key, scalar = norm
            groups[key].append((b, a, eps, scalar))

    checked_pairs = 0
    endpoints = []
    for key, atoms in groups.items():
        if len(atoms) < 2:
            continue
        for u, v in itertools.combinations(atoms, 2):
            checked_pairs += 1
            b1, a1, e1, t1 = u
            b2, a2, e2, t2 = v
            g = math.gcd(abs(t1), abs(t2))
            c1, c2 = t2 // g, -t1 // g
            torsion = (c1 * e1 + c2 * e2) % 8
            if torsion % 2 == 0:
                continue
            scale = min((torsion, torsion - 8), key=abs)
            coeffs = (scale * c1, scale * c2)
            assert (coeffs[0] * e1 + coeffs[1] * e2) % 8 == 1
            assert coeffs[0] * t1 + coeffs[1] * t2 == 0

            v1, v2 = (b1, a1), (b2, a2)
            mu = generalized_mu(v1, v2)
            bits = b1.bit_length() + b2.bit_length()
            endpoints.append((mu, bits, v1, v2, coeffs, key))

    endpoints.sort()

    # Pareto-minimize generalized Lehmer measure and denominator-coordinate bits.
    pareto = []
    best_mu = float("inf")
    for row in sorted(endpoints, key=lambda r: (r[1], r[0])):
        if row[0] < best_mu - 1e-15:
            endpoint, sheet, crossings = tangent_sheet(row[2], row[3], row[4])
            if endpoint == (1, 1) and sheet == 0:
                pareto.append(row + (crossings,))
                best_mu = row[0]

    return {
        "height": height,
        "atom_count": atom_count,
        "direction_groups": len(groups),
        "checked_pairs": checked_pairs,
        "endpoint_pairs": len(endpoints),
        "best": endpoints,
        "pareto": pareto,
    }


def main():
    result = census()
    for key in ("height", "atom_count", "direction_groups", "checked_pairs", "endpoint_pairs"):
        print(f"{key}={result[key]}")

    print("best endpoint circuits:")
    for row in result["best"][:10]:
        print(f"  mu={row[0]:.15f} bits={row[1]} atoms={row[2:4]} c={row[4]} free={row[5]}")

    print("Pareto(mu, denominator_bits):")
    for row in result["pareto"]:
        print(f"  bits={row[1]:2d} mu={row[0]:.15f} atoms={row[2:4]} c={row[4]} crossings={row[6]}")

    if result["height"] == 1000:
        assert result["atom_count"] == 304191
        assert result["direction_groups"] == 202662
        assert result["checked_pairs"] == 102186
        assert result["endpoint_pairs"] == 101706

        best = result["best"][0]
        assert best[2] == (79, 3)
        assert best[3] == (278, 29)
        assert best[4] == (7, 5)
        assert best[5] == ((5, 1),)
        assert abs(best[0] - 1.7226709198993357) < 1e-14
        assert tangent_sheet(best[2], best[3], best[4]) == ((1, 1), 0, 0)

        expected_pareto = [
            (4, (2, 1), (3, 1), (1, 1)),
            (5, (3, 1), (7, 1), (2, 1)),
            (7, (7, 1), (11, 2), (3, 2)),
            (10, (7, 1), (79, 3), (5, 2)),
            (11, (5, 1), (239, 1), (4, -1)),
            (14, (46, 9), (239, 1), (4, 3)),
            (16, (79, 3), (278, 29), (7, 5)),
        ]
        observed = [(row[1], row[2], row[3], row[4]) for row in result["pareto"]]
        assert observed == expected_pareto
        assert all(row[6] == 0 for row in result["pareto"])
        print("H=1000 rational support-two Pareto regression certificate: PASS")


if __name__ == "__main__":
    main()
