#!/usr/bin/env python3
"""Exact generalized support-two direction-generator census for #1160.

This replaces O(H^2) enumeration of all primitive rational atoms 0<a<b<=H by
an exact Gaussian free-direction generator.

Key theorem used by the checker:
- for primitive z=b+ai with normalized free valuation direction g and multiplier m,
  N(z)=a^2+b^2 is either M(g)^|m| or 2 M(g)^|m|;
- if a two-atom rank-one circuit has unequal |m| values and both denominators are
  <=H, then M(g)<sqrt(2) H;
- equal-|m| pairs are complementary pairs.  The prior Pell theorem gives their
  generalized Lehmer lower bound >5.22499; hence every such pair with denominator
  bit cost >=5 is dominated by the already-known (1/3,1/7) Pareto point.  The only
  bit-4 point is (1/2,1/3).

Therefore the complete (mu, denominator-bit) support-two Pareto frontier is found
by enumerating primitive Gaussian free directions of norm <sqrt(2)H, taking their
powers and complements, plus the one bit-4 complementary point.

Endpoint feasibility remains exact C8 + Gaussian free-valuation arithmetic.
Floating logarithms are used only after exact feasibility for Pareto ranking.
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

DEFAULT_H = 1_000_000


def spf_sieve(n: int) -> list[int]:
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    for p in range(2, math.isqrt(n) + 1):
        if spf[p] == p:
            for q in range(p * p, n + 1, p):
                if spf[q] == q:
                    spf[q] = p
    return spf


def factor_spf(n: int, spf: list[int]) -> dict[int, int]:
    out: dict[int, int] = {}
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out[p] = e
    return out


def small_signature(b: int, a: int, spf: list[int]):
    """Exact signature for seed norm <=sqrt(2)H."""
    z = (b, a)
    coords = {}
    for p, e in factor_spf(b * b + a * a, spf).items():
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
    unit_exp = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}[z]
    return (ramified + 2 * unit_exp) % 8, tuple(sorted(coords.items()))


def normalized_direction(items):
    if not items:
        return None
    g = 0
    for _, v in items:
        g = math.gcd(g, abs(v))
    vals = [(p, v // g) for p, v in items]
    if vals[0][1] < 0:
        vals = [(p, -v) for p, v in vals]
    return tuple(vals), g


def pair_mul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def unit_mul(z, r: int):
    x, y = z
    return ((x, y), (-y, x), (-x, -y), (y, -x))[r % 4]


def fold_pair(z):
    x, y = z
    g = math.gcd(abs(x), abs(y))
    x //= g
    y //= g
    b, a = max(abs(x), abs(y)), min(abs(x), abs(y))
    if a == 0 or a == b:
        return None
    return (b, a), g


def fold_info(raw, seed_eps: int, h: int):
    folded = fold_pair(raw)
    if folded is None:
        return None
    (b, a), scale = folded
    target = (scale * b, scale * a)
    for conjugated in (False, True):
        base = (raw[0], -raw[1]) if conjugated else raw
        for r in range(4):
            if unit_mul(base, r) == target:
                multiplier = -h if conjugated else h
                eps = ((-h * seed_eps if conjugated else h * seed_eps) + 2 * r) % 8
                return (b, a), multiplier, eps
    raise AssertionError((raw, folded))


def complement(v):
    b, a = v
    return (b + a, b - a)


def enumerate_direction_seeds(height: int):
    max_norm = math.floor(math.sqrt(2) * height)
    spf = spf_sieve(max_norm)
    seeds = {}
    xmax = math.isqrt(max_norm)
    for x in range(2, xmax + 1):
        ymax = min(x - 1, math.isqrt(max_norm - x * x))
        for y in range(1, ymax + 1):
            if math.gcd(x, y) != 1:
                continue
            eps, items = small_signature(x, y, spf)
            nd = normalized_direction(items)
            if nd is None or nd[1] != 1:
                continue
            key = nd[0]
            seeds.setdefault(key, (x, y, eps, x * x + y * y))
    return seeds


def generated_atoms(height: int):
    seeds = enumerate_direction_seeds(height)
    groups = defaultdict(list)
    for key, (x, y, seed_eps, M) in seeds.items():
        raw = (1, 0)
        h = 0
        while True:
            h += 1
            raw = pair_mul(raw, (x, y))
            if M**h >= 2 * height * height:
                break
            info = fold_info(raw, seed_eps, h)
            if info is None:
                continue
            (b, a), multiplier, eps = info
            if b <= height:
                groups[key].append((b, a, multiplier, eps))
            cb, ca = complement((b, a))
            if cb <= height:
                groups[key].append((cb, ca, -multiplier, (1 - eps) % 8))
    return seeds, groups


def generalized_mu(atom):
    b, a = atom
    return 1.0 / math.log10(b / a)


def tangent_sheet(v1, v2, coeffs):
    z = (1, 0)
    sheet = crossings = 0
    for (b, a), coefficient in ((v1, coeffs[0]), (v2, coeffs[1])):
        sign = 1 if coefficient > 0 else -1
        factor = (b, sign * a)
        for _ in range(abs(coefficient)):
            old = z
            new = pair_mul(z, factor)
            g = math.gcd(abs(new[0]), abs(new[1]))
            new = (new[0] // g, new[1] // g)
            if old[0] and new[0] and (old[0] > 0) != (new[0] > 0):
                sheet += sign
                crossings += 1
            z = new
    return z, sheet, crossings


def census(height: int = DEFAULT_H):
    seeds, groups = generated_atoms(height)
    generated_count = sum(len(set(rows)) for rows in groups.values())
    checked = 0
    endpoints = []

    for key, raw_rows in groups.items():
        rows = list(set(raw_rows))
        for u, v in itertools.combinations(rows, 2):
            checked += 1
            b1, a1, m1, e1 = u
            b2, a2, m2, e2 = v
            if (b1, a1) == (b2, a2):
                continue
            g = math.gcd(abs(m1), abs(m2))
            c1, c2 = m2 // g, -m1 // g
            torsion = (c1 * e1 + c2 * e2) % 8
            if torsion % 2 == 0:
                continue
            scale = min((torsion, torsion - 8), key=abs)
            coeffs = (scale * c1, scale * c2)
            assert coeffs[0] * m1 + coeffs[1] * m2 == 0
            assert (coeffs[0] * e1 + coeffs[1] * e2) % 8 == 1
            atoms = tuple(sorted(((b1, a1), (b2, a2))))
            if atoms[0] != (b1, a1):
                coeffs = (coeffs[1], coeffs[0])
            mu = sum(generalized_mu(atom) for atom in atoms)
            bits = sum(atom[0].bit_length() for atom in atoms)
            endpoints.append((bits, mu, atoms, coeffs, key))

    # All omitted equal-multiplier complementary pairs have mu > 5.22499 by the
    # Pell theorem.  At bit cost >=5 they are dominated by the generated
    # (1/3,1/7) point.  The only possible bit-4 pair is Euler (1/2,1/3), which is
    # already generated because its direction norm is 5.
    best_by_bits = {}
    for row in endpoints:
        bits = row[0]
        if bits not in best_by_bits or row[1] < best_by_bits[bits][1]:
            best_by_bits[bits] = row

    pareto = []
    best_mu = float("inf")
    for bits in sorted(best_by_bits):
        row = best_by_bits[bits]
        if row[1] < best_mu - 1e-15:
            endpoint, sheet, crossings = tangent_sheet(row[2][0], row[2][1], row[3])
            assert endpoint == (1, 1) and sheet == 0
            pareto.append(row + (crossings,))
            best_mu = row[1]

    return {
        "height": height,
        "direction_seeds": len(seeds),
        "generated_atoms": generated_count,
        "checked_pairs": checked,
        "endpoint_pairs": len(endpoints),
        "pareto": pareto,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--height", type=int, default=DEFAULT_H)
    args = parser.parse_args()
    result = census(args.height)
    for k in ("height", "direction_seeds", "generated_atoms", "checked_pairs", "endpoint_pairs"):
        print(f"{k}={result[k]}")
    print("Pareto(mu, denominator_bits):")
    for row in result["pareto"]:
        print(
            f"  bits={row[0]:2d} mu={row[1]:.15f} atoms={row[2]} "
            f"c={row[3]} free={row[4]} crossings={row[5]}"
        )

    if args.height == 1_000_000:
        assert result["direction_seeds"] == 224883
        assert result["generated_atoms"] == 757785
        assert result["checked_pairs"] == 977206
        assert result["endpoint_pairs"] == 612512
        observed = [(r[0], r[2], r[3]) for r in result["pareto"]]
        expected = [
            (4, ((2, 1), (3, 1)), (1, 1)),
            (5, ((3, 1), (7, 1)), (2, 1)),
            (7, ((7, 1), (11, 2)), (3, 2)),
            (10, ((7, 1), (79, 3)), (5, 2)),
            (11, ((5, 1), (239, 1)), (4, -1)),
            (14, ((46, 9), (239, 1)), (3, 4)),
            (16, ((79, 3), (278, 29)), (7, 5)),
            (22, ((79, 3), (22049, 1457)), (12, 5)),
            (27, ((79, 3), (873121, 24478)), (17, 5)),
        ]
        assert observed == expected
        assert abs(result["pareto"][-1][1] - 1.3481805739852035) < 1e-14
        assert result["pareto"][-1][4] == ((5, 1),)
        print("H=1,000,000 direction-generated support-two Pareto certificate: PASS")


if __name__ == "__main__":
    main()
