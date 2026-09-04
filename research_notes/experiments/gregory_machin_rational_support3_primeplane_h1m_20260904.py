#!/usr/bin/env python3
"""Exact generalized support-three Gaussian-prime-plane audit for #1160.

Declared box:
- primitive rational atoms [b+ai] with 0<a<b<=1,000,000;
- free valuation support contained in one two-prime plane (p,q);
- split primes p<q<=5000, p=q=1 mod 4;
- minimal rank-two, three-column circuits hitting the C8 diagonal target.

The audit is complete for combined-Pareto improvement inside this box by splitting
resources into two regimes:
(A) total denominator bit cost <=26: enumerate every prime-plane triple in that
    bit region and retain only triples beating the already-proved support-two
    baseline at the same bit budget;
(B) bit cost >=27: any improvement must have generalized Lehmer measure below the
    support-two H=1M leader 1.3481805739852035, so enumerate exactly all triples
    below that cost using branch-and-bound.

No floating arctangent equality is used.  Floating logarithms are only the declared
post-native completion/Pareto coordinate.
"""

from __future__ import annotations

import importlib.util
import itertools
import math
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "gregory_machin_rational_support2_direction_generator_h1m_20260904.py"
spec = importlib.util.spec_from_file_location("g2", BASE)
g2 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(g2)

gm3 = g2.gm3
HEIGHT = 1_000_000
PRIME_CAP = 5000
LOW_MU = 1.3481805739852035

SUPPORT2_FRONT = [
    (4, 5.4178313691767475, ((2, 1), (3, 1)), (1, 1)),
    (5, 3.2791979367443230, ((3, 1), (7, 1)), (2, 1)),
    (7, 2.5339840126747872, ((7, 1), (11, 2)), (3, 2)),
    (10, 1.8872692426749564, ((7, 1), (79, 3)), (5, 2)),
    (11, 1.8511276523168558, ((5, 1), (239, 1)), (4, -1)),
    (14, 1.8318531749144709, ((46, 9), (239, 1)), (3, 4)),
    (16, 1.7226709198993357, ((79, 3), (278, 29)), (7, 5)),
    (22, 1.5514829532007886, ((79, 3), (22049, 1457)), (12, 5)),
    (27, 1.3481805739852035, ((79, 3), (873121, 24478)), (17, 5)),
]


def primes_upto(n: int):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


def ipow(z, n: int):
    out = (1, 0)
    while n:
        if n & 1:
            out = g2.pair_mul(out, z)
        z = g2.pair_mul(z, z)
        n //= 2
    return out


def gaussian_prime(p: int, sign: int):
    x, y = gm3.sum_two_squares_prime(p)
    return (x, y if sign > 0 else -y)


def fold_vector(raw, vec):
    """Fold raw odd-prime Gaussian product into first octant and preserve signature."""
    folded = g2.fold_pair(raw)
    assert folded is not None
    (b, a), scale = folded
    target = (scale * b, scale * a)
    result = None
    for conjugated in (False, True):
        base = (raw[0], -raw[1]) if conjugated else raw
        for r in range(4):
            if g2.unit_mul(base, r) == target:
                free = tuple(-v for v in vec) if conjugated else tuple(vec)
                eps = (2 * r) % 8
                result = ((b, a), free, eps)
                break
        if result is not None:
            break
    assert result is not None
    atom, free, eps = result
    comp = g2.complement(atom)
    return [
        (atom, free, eps),
        (comp, tuple(-v for v in free), (1 - eps) % 8),
    ]


def plane_atoms(p: int, q: int, height: int = HEIGHT):
    """Generate every strict atom in the (p,q) free-valuation plane under height."""
    out = {}
    max_u = int(math.log(2 * height * height, p)) + 1
    max_v = int(math.log(2 * height * height, q)) + 1
    for au in range(max_u + 1):
        for av in range(max_v + 1):
            if au == av == 0:
                continue
            norm = p**au * q**av
            if norm >= 2 * height * height:
                continue
            signs_u = (1, -1) if au else (1,)
            signs_v = (1, -1) if av else (1,)
            for su in signs_u:
                for sv in signs_v:
                    raw = g2.pair_mul(ipow(gaussian_prime(p, su), au), ipow(gaussian_prime(q, sv), av))
                    vec = (su * au if au else 0, sv * av if av else 0)
                    for atom, free, eps in fold_vector(raw, vec):
                        b, a = atom
                        if b <= height and 0 < a < b:
                            out[atom] = (free, eps)
    return out


def atom_mu(atom):
    b, a = atom
    return 1.0 / math.log10(b / a)


def endpoint_coeff(triple):
    """Exact primitive kernel + C8 target for three 2D free vectors."""
    (_, _, v1, e1), (_, _, v2, e2), (_, _, v3, e3) = triple
    c1 = v2[0] * v3[1] - v2[1] * v3[0]
    c2 = v3[0] * v1[1] - v3[1] * v1[0]
    c3 = v1[0] * v2[1] - v1[1] * v2[0]
    if c1 == 0 or c2 == 0 or c3 == 0:
        return None
    g = math.gcd(math.gcd(abs(c1), abs(c2)), abs(c3))
    c = (c1 // g, c2 // g, c3 // g)
    if c[0] < 0:
        c = tuple(-x for x in c)
    torsion = (c[0] * e1 + c[1] * e2 + c[2] * e3) % 8
    if torsion % 2 == 0:
        return None
    scale = min((torsion, torsion - 8), key=abs)
    return tuple(scale * x for x in c)


def support2_baseline(bits: int):
    vals = [mu for b, mu, _, _ in SUPPORT2_FRONT if b <= bits]
    return min(vals) if vals else float("inf")


def tangent_sheet(atoms, coeffs):
    z = (1, 0)
    sheet = crossings = 0
    for (b, a), coefficient in zip(atoms, coeffs):
        sign = 1 if coefficient > 0 else -1
        factor = (b, sign * a)
        for _ in range(abs(coefficient)):
            old = z
            new = g2.pair_mul(z, factor)
            g = math.gcd(abs(new[0]), abs(new[1]))
            new = (new[0] // g, new[1] // g)
            if old[0] and new[0] and (old[0] > 0) != (new[0] > 0):
                sheet += sign
                crossings += 1
            z = new
    return z, sheet, crossings


def small_bit_audit(atoms, p: int, q: int, max_bits: int = 26):
    buckets = defaultdict(list)
    for atom, (vec, eps) in atoms.items():
        bits = atom[0].bit_length()
        if bits <= max_bits - 4:
            buckets[bits].append((atom_mu(atom), atom, vec, eps))
    lengths = sorted(buckets)
    tested = cost_pass = 0
    endpoints = []

    for ii, l1 in enumerate(lengths):
        for jj in range(ii, len(lengths)):
            l2 = lengths[jj]
            for kk in range(jj, len(lengths)):
                l3 = lengths[kk]
                bits = l1 + l2 + l3
                if bits > max_bits:
                    break
                threshold = support2_baseline(bits)
                A, B, C = buckets[l1], buckets[l2], buckets[l3]
                if ii == jj == kk:
                    iterator = itertools.combinations(A, 3)
                elif ii == jj:
                    iterator = ((x, y, z) for x, y in itertools.combinations(A, 2) for z in C)
                elif jj == kk:
                    iterator = ((x, y, z) for x in A for y, z in itertools.combinations(B, 2))
                else:
                    iterator = itertools.product(A, B, C)
                for triple in iterator:
                    tested += 1
                    mu = sum(row[0] for row in triple)
                    if mu >= threshold - 1e-15:
                        continue
                    cost_pass += 1
                    coeffs = endpoint_coeff(triple)
                    if coeffs is None:
                        continue
                    ats = tuple(row[1] for row in triple)
                    endpoints.append((bits, mu, ats, coeffs, (p, q)))
    return tested, cost_pass, endpoints


def low_mu_audit(atoms, p: int, q: int, bound: float = LOW_MU + 1e-12):
    rows = sorted((atom_mu(atom), atom, vec, eps) for atom, (vec, eps) in atoms.items())
    n = len(rows)
    tested = 0
    endpoints = []
    for i in range(n - 2):
        if rows[i][0] + rows[i + 1][0] + rows[i + 2][0] >= bound:
            break
        for j in range(i + 1, n - 1):
            if rows[i][0] + rows[j][0] + rows[j + 1][0] >= bound:
                break
            for k in range(j + 1, n):
                mu = rows[i][0] + rows[j][0] + rows[k][0]
                if mu >= bound:
                    break
                tested += 1
                triple = (rows[i], rows[j], rows[k])
                coeffs = endpoint_coeff(triple)
                if coeffs is None:
                    continue
                ats = tuple(row[1] for row in triple)
                bits = sum(atom[0].bit_length() for atom in ats)
                endpoints.append((bits, mu, ats, coeffs, (p, q)))
    return tested, endpoints


def combined_pareto(rows):
    best_by_bits = {}
    for row in rows:
        bits = row[0]
        if bits not in best_by_bits or row[1] < best_by_bits[bits][1]:
            best_by_bits[bits] = row
    out = []
    best_mu = float("inf")
    for bits in sorted(best_by_bits):
        row = best_by_bits[bits]
        if row[1] < best_mu - 1e-14:
            out.append(row)
            best_mu = row[1]
    return out


def census():
    split_primes = [p for p in primes_upto(PRIME_CAP) if p % 4 == 1]
    small_tested = small_cost_pass = low_tested = 0
    small_endpoints = []
    low_endpoints = []

    for i, p in enumerate(split_primes):
        for q in split_primes[i + 1 :]:
            atoms = plane_atoms(p, q)
            t, cp, eps = small_bit_audit(atoms, p, q)
            small_tested += t
            small_cost_pass += cp
            small_endpoints.extend(eps)
            t2, eps2 = low_mu_audit(atoms, p, q)
            low_tested += t2
            low_endpoints.extend(eps2)

    rows = [(b, mu, atoms, coeffs, "support2") for b, mu, atoms, coeffs in SUPPORT2_FRONT]
    seen = set()
    for row in small_endpoints + low_endpoints:
        key = (tuple(sorted(row[2])), row[3])
        if key in seen:
            continue
        seen.add(key)
        rows.append(row)
    pareto = combined_pareto(rows)

    for row in pareto:
        if row[4] == "support2":
            continue
        endpoint, sheet, crossings = tangent_sheet(row[2], row[3])
        assert endpoint == (1, 1) and sheet == 0 and crossings == 0, row

    return {
        "split_primes": len(split_primes),
        "planes": math.comb(len(split_primes), 2),
        "small_tested": small_tested,
        "small_cost_pass": small_cost_pass,
        "small_endpoints": small_endpoints,
        "low_tested": low_tested,
        "low_endpoints": low_endpoints,
        "pareto": pareto,
    }


def main():
    result = census()
    for key in ("split_primes", "planes", "small_tested", "small_cost_pass", "low_tested"):
        print(f"{key}={result[key]}")
    print(f"small_endpoint_count={len(result['small_endpoints'])}")
    print(f"low_endpoint_count={len(result['low_endpoints'])}")
    print("combined Pareto:")
    for row in result["pareto"]:
        print(f"  bits={row[0]:2d} mu={row[1]:.15f} atoms={row[2]} c={row[3]} source={row[4]}")

    assert result["split_primes"] == 329
    assert result["planes"] == 53956
    assert result["small_tested"] == 15575052
    assert result["small_cost_pass"] == 65
    assert len(result["small_endpoints"]) == 1
    assert result["low_tested"] == 1546
    assert len(result["low_endpoints"]) == 16

    expected_tail = [
        (21, 1.6939423440424217, ((57, 1), (79, 3), (239, 1)), (20, 12, -5)),
        (22, 1.5514829532007886, ((79, 3), (22049, 1457)), (12, 5)),
        (27, 1.3481805739852035, ((79, 3), (873121, 24478)), (17, 5)),
        (35, 1.3474299837853827, ((128467, 369), (239, 1), (524, 7)), (12, 39, 44)),
        (41, 1.2183602165315697, ((8149, 7), (143237, 309), (601, 7)), (32, 22, 61)),
        (49, 1.2096120143032323, ((8149, 7), (143237, 309), (144047, 1554)), (93, 22, 61)),
    ]
    observed = [(r[0], r[1], r[2], r[3]) for r in result["pareto"] if r[0] >= 21]
    assert len(observed) == len(expected_tail)
    for got, want in zip(observed, expected_tail):
        assert got[0] == want[0] and got[2:] == want[2:]
        assert abs(got[1] - want[1]) < 1e-14
    print("H=1M / p,q<=5000 support-three prime-plane Pareto audit: PASS")


if __name__ == "__main__":
    main()
