#!/usr/bin/env python3
"""Exact finite checks for the R0 and R1 observer-fiber theorems.

The all-prime bounds and unbounded refinement theorem are proved in proof.md.
This verifier checks their finite arithmetic inputs, complete CRT counts, two
compact sharp witnesses, and the R1 membership of three previously certified
exact-cost roots. It does not repeat their pairwise-gcd or native certificates.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import permutations, product
import json
from math import gcd, isqrt, lcm, prod
from pathlib import Path
import sys

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

A_STAR = 690786768637635218740714348513373826260012289
M = 1397394912916194098609132326092145093313722687204526281
P = (7, 17, 31, 41, 71, 97, 113, 127, 151, 241, 257, 281, 337,
     641, 673, 1321, 14449, 29191, 65537, 6700417)
H = (0, 1, 3, 6, 9, 10, 15, 16, 21, 30, 31, 33, 36, 45, 48, 49,
     51, 54, 55, 63, 64, 66, 69, 70, 75, 76, 78, 79, 84, 85, 90,
     91, 93, 96, 99, 100)
OLD_ROWS = (
    (7, 3, 1, 37), (17, 8, 3, 3), (31, 5, 4, 89), (41, 20, 5, 5),
    (71, 35, 13, 293), (97, 48, 21, 117), (113, 28, 21, 413),
    (127, 7, 1, 113), (151, 15, 11, 41), (241, 24, 9, 33),
    (257, 16, 7, 87), (281, 70, 23, 233), (337, 21, 17, 773),
    (641, 64, 15, 207), (673, 48, 45, 237), (1321, 60, 17, 257),
    (14449, 84, 53, 53), (29191, 105, 68, 593),
    (65537, 32, 31, 63), (6700417, 64, 47, 111),
)
V = (5, 13, 11, 61, 331)
U = (11, 61, 331)
W = (19, 37, 73, 109)
B = (433, 38737)
K, J, Z = prod(V), prod(W), prod(B)
L = K * J
R0_V_RESIDUES = (3, 1, 0, 0, 0)
R1_W_RESIDUES = (6, 0, 37, 0)
W_ORDER_2 = {19: 18, 37: 36, 73: 9, 109: 36}
FACTORS = {
    14: {3: 1, 43: 1, 127: 1},
    16: {3: 1, 5: 1, 17: 1, 257: 1},
    18: {3: 3, 7: 1, 19: 1, 73: 1},
    20: {3: 1, 5: 2, 11: 1, 31: 1, 41: 1},
    24: {3: 2, 5: 1, 7: 1, 13: 1, 17: 1, 241: 1},
    36: {3: 3, 5: 1, 7: 1, 13: 1, 19: 1, 37: 1, 73: 1, 109: 1},
    48: {3: 2, 5: 1, 7: 1, 13: 1, 17: 1, 97: 1, 241: 1,
         257: 1, 673: 1},
    60: {3: 2, 5: 2, 7: 1, 11: 1, 13: 1, 31: 1, 41: 1,
         61: 1, 151: 1, 331: 1, 1321: 1},
    72: {3: 3, 5: 1, 7: 1, 13: 1, 17: 1, 19: 1, 37: 1,
         73: 1, 109: 1, 241: 1, 433: 1, 38737: 1},
}


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def prime_factors(n: int) -> tuple[int, ...]:
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return tuple(out)


def has_exact_order(base: int, q: int, order: int) -> bool:
    return (pow(base, order, q) == 1 and
            all(pow(base, order // p, q) != 1 for p in prime_factors(order)))


def crt(pairs) -> tuple[int, int]:
    a, modulus = 0, 1
    for residue, q in pairs:
        assert gcd(modulus, q) == 1
        a += modulus * ((residue - a) * pow(modulus, -1, q) % q)
        modulus *= q
    return a, modulus


def phase_roots(q: int, c: int) -> tuple[int, int]:
    r = pow(pow(2, c, q), -1, q)
    values = tuple(sorted((r, q - r)))
    assert len(set(values)) == 2
    return values


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def incidence(values, divisors):
    return {g: [sum(x % g == c for x in values) for c in range(g)]
            for g in divisors}


def category(residue: int, q: int, table: dict) -> int:
    for row in table[q]:
        if residue in row["root_residues"]:
            return row["relative_phase"]
    return -1


def category_counts(primes, phase_count: int):
    """All weighted category states, not random or bounded-prime samples."""
    counts = Counter()
    for state in product(range(-1, phase_count), repeat=len(primes)):
        weight = prod(q - 2 * phase_count if c == -1 else 2
                      for q, c in zip(primes, state))
        counts[len(set(state) - {-1})] += weight
    assert sum(counts.values()) == prod(primes)
    return counts


def essential_coordinates(primes, table, threshold: int):
    records = []
    for q in primes:
        others = [p for p in primes if p != q]
        before = {p: 0 for p in primes}
        for phase, p in enumerate(others[:threshold - 1]):
            before[p] = table[p][phase]["root_residues"][0]
        after = dict(before)
        after[q] = table[q][threshold - 1]["root_residues"][0]
        def present(residues):
            return len({category(residues[p], p, table) for p in primes} - {-1})
        assert present(before) == threshold - 1
        assert present(after) == threshold
        assert all(before[p] == after[p] for p in others)
        b, period = crt((before[p], p) for p in primes)
        a, _ = crt((after[p], p) for p in primes)
        records.append({"prime": q, "false_residue": b, "true_residue": a,
                        "period": period})
    return records


def coverage_witness(a: int, ordered_primes: tuple[int, ...], period: int):
    holes = set(H)
    uncovered = [n for n in range(1, period + 1)
                 if n % 2 == 0 and (n // 2) % 105 in holes]
    counts = [len(uncovered)]
    rows = []
    for q in ordered_primes:
        o = next(i for i in range(1, q) if pow(2, i, q) == 1)
        d = o // gcd(o, 2)
        phases = [u for u in range(d) if a * a * pow(4, u, q) % q == 1]
        assert len(phases) == 1
        uncovered = [n for n in uncovered if a * a * pow(2, n, q) % q != 1]
        counts.append(len(uncovered))
        rows.append({"prime": q, "root_residue": a % q, "order_2": o,
                     "even_u_period": d, "even_u_phase": phases[0]})
    assert 2 * a * a - 1 > max(P + ordered_primes)
    return {"root_decimal": str(a), "root_decimal_digits": len(str(a)),
            "root_decimal_sha256": sha256(str(a).encode()).hexdigest(),
            "exponent_period_of_uncovered_set": period,
            "ordered_added_rows": rows, "uncovered_counts": counts,
            "density_values": [fraction_text(Fraction(x, period)) for x in counts],
            "all_assigned_divisors_proper": True,
            "total_cover_cost_equality_claimed": False}


def locate(explicit: str | None, relative_path: str, fallbacks: tuple[str, ...]) -> Path:
    if explicit:
        path = Path(explicit)
        assert path.is_file(), path
        return path
    here = Path(__file__).resolve().parent
    # The same file is run in scratch and in a published research-note folder.
    # Search the canonical repository-relative dependency at every ancestor.
    for root in (here,) + tuple(here.parents):
        path = root / relative_path
        if path.is_file():
            return path
    for candidate in fallbacks:
        for root in (here,) + tuple(here.parents):
            path = root / candidate
            if path.is_file():
                return path
    raise FileNotFoundError(f"Pass the dependency certificate explicitly: {relative_path}")


def retained_exact_cost_checks(v8_path: Path, v7_path: Path, r1: int):
    v8 = json.loads(v8_path.read_text())
    v7 = json.loads(v7_path.read_text())
    assert int(v7["a_star"]) == A_STAR and int(v7["M"]) == M
    assert v7["old_rows"] == [list(row) for row in OLD_ROWS]
    witnesses = [(row["additional_cost"], row, "v8")
                 for row in v8["new_explicit_witnesses"]
                 if row["additional_cost"] in (6, 7)]
    witnesses.append((8, v7["numeric_cost_8"], "v7"))
    out = []
    for s, row, source in witnesses:
        root = int(row["root_hex"], 16)
        assert root % (6 * M) == A_STAR
        assert root % K == 666303
        assert tuple(root % q for q in V) == R0_V_RESIDUES
        assert tuple(root % q for q in W) == R1_W_RESIDUES
        assert root % L == r1
        root_text = str(root)
        assert len(root_text) == row["root_decimal_digits"]
        digest = sha256(root_text.encode()).hexdigest()
        assert digest == row["root_decimal_sha256"]
        assert {3, 5, 41, 63}.issubset(row["private_indices"])
        assert row["all_pairwise_gcd_one"]
        out.append({"additional_cost": s, "total_cost": row["total_cost"],
                    "root_decimal_digits": len(root_text),
                    "root_decimal_sha256": digest,
                    "root_residue_mod_L": r1,
                    "W_residues": dict(zip(W, R1_W_RESIDUES)),
                    "existing_gcd_count_reused": row.get("checked_pairwise_gcd_count", row.get("gcd_pair_count")),
                    "source": source,
                    "new_check_scope": "Exact root membership in R1; prior exact-cost and native evidence reused."})
    assert [row["additional_cost"] for row in out] == [6, 7, 8]
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--v8-certificate")
    parser.add_argument("--v7-certificate")
    parser.add_argument("--output", default=str(Path(__file__).with_name("fiber_certificate.json")))
    args = parser.parse_args()
    assert prod(P) == M
    assert A_STAR % 3 == 0
    assert (K, J, L, Z) == (14436565, 5593771, 80754838636615, 16773121)

    # Full factor products plus trial primality make these complete factorizations.
    for n, factors in FACTORS.items():
        assert prod(q ** e for q, e in factors.items()) == (1 << n) - 1
        assert all(is_prime(q) for q in factors)
    assert 17 * 241 * 433 * 38737 == (1 << 36) + 1
    old_or_small = set(P) | {3, 5, 13}
    assert set(FACTORS[16]) <= old_or_small
    assert set(FACTORS[24]) <= old_or_small
    assert set(FACTORS[48]) <= old_or_small
    assert set(FACTORS[20]) - old_or_small == {11}
    assert set(FACTORS[60]) - old_or_small == set(U)
    assert set(FACTORS[36]) - old_or_small == set(W)
    assert set(FACTORS[72]) - old_or_small - set(W) == set(B)
    assert set(FACTORS[18]) - old_or_small == {19, 73}
    assert set(FACTORS[14]) - old_or_small == {43}
    for q in W:
        assert has_exact_order(2, q, W_ORDER_2[q])
        assert has_exact_order(pow(2, 12, q), q, 3)
    for q in B:
        assert has_exact_order(2, q, 72)
        assert has_exact_order(pow(2, 36, q), q, 2)

    # Independently reconstruct the full old residue-union period.
    old_period = lcm(*(row[1] for row in OLD_ROWS))
    assert old_period == 6720
    for q, o, c, private_n in OLD_ROWS:
        assert is_prime(q) and has_exact_order(2, q, o)
        zeros = [n for n in range(o) if A_STAR * A_STAR * pow(2, n, q) % q == 1]
        assert zeros == [c]
        assert [p for p, op, cp, _ in OLD_ROWS if private_n % op == cp] == [q]
    holes = set(H)
    for n in range(old_period):
        old_uncovered = not any(n % o == c for _, o, c, _ in OLD_ROWS)
        assert old_uncovered == (n % 2 == 0 and (n // 2) % 105 in holes)

    divisors = (1, 3, 5, 7, 15, 21, 35, 105)
    h_incidence = incidence(H, divisors)
    h_max = [max(h_incidence[g]) for g in divisors]
    assert h_max == [36, 23, 11, 7, 6, 4, 2, 1]
    assert [sum(u % 3 == r for u in H) for r in range(3)] == [23, 13, 0]
    a_set = tuple(v for v in range(35) if (4 + 6 * v) % 105 in holes)
    assert len(a_set) == 13
    a_incidence = incidence(a_set, (1, 5, 7, 35))
    a_max = [max(a_incidence[g]) for g in (1, 5, 7, 35)]
    assert a_max == [13, 5, 3, 1]
    w_set = tuple(w for w in range(35) if (16 + 18 * w) % 105 in holes)
    assert len(w_set) == 13
    assert [max(v) for v in incidence(w_set, (1, 5, 7, 35)).values()] == a_max

    generic_min_periods = (8, 9, 10, 7, 15, 21, 35, 105)
    generic_bounds = [Fraction(k * g, 36 * d)
                      for k, g, d in zip(h_max, divisors, generic_min_periods)]
    assert max(generic_bounds) == Fraction(23, 108)
    all_except_5_13_top5 = 2 * Fraction(23, 108) + Fraction(7, 36) + 2 * Fraction(1, 6)
    assert all_except_5_13_top5 == Fraction(103, 108)
    # Removing d=9 and d=7 leaves these columnwise bounds, all at most 1/6.
    next_min_periods = (8, 12, 10, 14, 15, 21, 35, 105)
    next_bounds = [Fraction(k * g, 36 * d)
                   for k, g, d in zip(h_max, divisors, next_min_periods)]
    assert max(next_bounds) <= Fraction(1, 6)
    a_divisors = (1, 5, 7, 35)
    a_bounds = [Fraction(k * g, 13 * f) for k, g, f in
                zip(a_max, a_divisors, (3, 10, 7, 35))]
    non_w_bounds = [Fraction(k * g, 13 * f) for k, g, f in
                    zip(a_max, a_divisors, (6, 10, 7, 35))]
    binary_bounds = [Fraction(k * g, 13 * h) for k, g, h in
                     zip(a_max, a_divisors, (2, 5, 7, 35))]
    assert max(a_bounds) == Fraction(1, 3)
    assert max(non_w_bounds) == Fraction(3, 13)
    assert max(binary_bounds) == Fraction(1, 2)

    # Strict comparisons needed to exclude all alternate equality dictionaries.
    r0_densities = [Fraction(n, 1260) for n in (216, 108, 39, 26, 13, 0)]
    for t in (2, 3, 4):
        neither = Fraction(6, 35) * (1 - t * Fraction(23, 108))
        exactly_one = Fraction(3, 35) * (1 - (t - 1) * Fraction(23, 108))
        assert neither > r0_densities[t]
        assert exactly_one > r0_densities[t]
    r1_densities = [Fraction(n, 2520) for n in (432, 216, 78, 52, 26, 13, 0)]
    r1_five_other_bounds = {
        "neither_5_nor_13": Fraction(6, 35) * (1 - all_except_5_13_top5),
        "exactly_one_of_5_13": Fraction(3, 35) * (1 - 4 * Fraction(23, 108)),
        "both_basic_no_active_W": Fraction(13, 420) * (1 - 3 * Fraction(3, 13)),
        "both_basic_one_active_W": Fraction(13, 420) * (1 - Fraction(1, 3) - 2 * Fraction(3, 13)),
    }
    assert all(v > r1_densities[5] for v in r1_five_other_bounds.values())

    w_table = {q: [{"relative_phase": r,
                    "u_phase": (4 + 6 * r) % (W_ORDER_2[q] // gcd(W_ORDER_2[q], 2)),
                    "u_period": W_ORDER_2[q] // gcd(W_ORDER_2[q], 2),
                    "root_residues": phase_roots(q, 4 + 6 * r)} for r in range(3)]
               for q in W}
    b_table = {q: [{"relative_phase": r, "u_phase": 16 + 18 * r,
                    "u_period": 36, "root_residues": phase_roots(q, 16 + 18 * r)}
                   for r in range(2)] for q in B}
    for q, table in list(w_table.items()) + list(b_table.items()):
        all_roots = [root for row in table for root in row["root_residues"]]
        assert len(all_roots) == len(set(all_roots))
        for row in table:
            for root in row["root_residues"]:
                assert root * root * pow(4, row["u_phase"], q) % q == 1

    r0_counts_by_phase = category_counts(W, 3)
    r0_predicate_counts = {"E3": sum(v for c, v in r0_counts_by_phase.items() if c >= 1),
                           "E4": sum(v for c, v in r0_counts_by_phase.items() if c >= 2),
                           "delta5": r0_counts_by_phase[3]}
    p6, p4, p2 = (prod(q - shift for q in W) for shift in (6, 4, 2))
    assert list(r0_predicate_counts.values()) == [J - p6, J - 3 * p4 + 2 * p6,
                                                 J - 3 * p2 + 3 * p4 - p6]
    assert list(r0_predicate_counts.values()) == [2812668, 397152, 10848]
    r0_essential = {name: essential_coordinates(W, w_table, threshold)
                    for name, threshold in (("E3", 1), ("E4", 2), ("delta5", 3))}

    # All 24 phase dictionaries and all free fourth-prime coordinates are covered.
    r0_class_set = set()
    raw_count = 0
    for assignment in permutations(W, 3):
        leftover = next(q for q in W if q not in assignment)
        for residues in product(*(w_table[q][r]["root_residues"]
                                  for r, q in enumerate(assignment))):
            for extra in range(leftover):
                residue, period = crt(list(zip(residues, assignment)) + [(extra, leftover)])
                assert period == J
                r0_class_set.add(residue)
                raw_count += 1
    assert len(r0_class_set) == r0_predicate_counts["delta5"]
    r0_base, r0_modulus = crt([(A_STAR, 6 * M), (666303, K)])
    assert tuple(r0_base % q for q in V) == R0_V_RESIDUES
    r0_minimum = min(crt([(r0_base, r0_modulus), (r, J)])[0] for r in r0_class_set)
    r0_witness = coverage_witness(r0_minimum, (5, 13, 37, 19, 73), 1260)
    assert r0_witness["uncovered_counts"] == [216, 108, 39, 26, 13, 0]
    r0_witness["minimum_scope"] = "Every R0 root with delta_P=5; complete 10848 CRT residue classes."
    r0_witness["delta_P"] = 5

    r1_residue, _ = crt([(666303, K)] + list(zip(R1_W_RESIDUES, W)))
    assert r1_residue == 12926327728523
    r1_base, r1_modulus = crt([(A_STAR, 6 * M), (r1_residue, L)])
    assert tuple(r1_base % q for q in W) == R1_W_RESIDUES
    r1_counts_by_phase = category_counts(B, 2)
    r1_predicate_counts = {"E5": Z - r1_counts_by_phase[0], "nested6": r1_counts_by_phase[2]}
    assert r1_predicate_counts == {"E5": 156664, "nested6": 8}
    assert r1_predicate_counts["E5"] == Z - (433 - 4) * (38737 - 4)
    r1_essential = {"E5": essential_coordinates(B, b_table, 1),
                    "nested6": essential_coordinates(B, b_table, 2)}
    r1_nested_classes = set()
    for phases in permutations((0, 1)):
        for residues in product(*(b_table[q][r]["root_residues"] for q, r in zip(B, phases))):
            residue, period = crt(zip(residues, B))
            assert period == Z
            r1_nested_classes.add(residue)
    assert len(r1_nested_classes) == 8
    r1_nested_minimum = min(crt([(r1_base, r1_modulus), (r, Z)])[0]
                            for r in r1_nested_classes)
    r1_witness = coverage_witness(r1_nested_minimum, (5, 13, 19, 73, 433, 38737), 2520)
    assert r1_witness["uncovered_counts"] == [432, 216, 78, 52, 26, 13, 0]
    r1_witness["minimum_scope"] = "R1 roots admitting a nested simultaneous optimum through budget 6; eight CRT classes."
    r1_witness["delta_P"] = 6
    r1_witness["all_delta6_roots_classified"] = False

    v8_path = locate(args.v8_certificate,
        "research_notes/portable_direct/riesel_observers_20261122/fixed_observer/fixed_observer_certificate.json",
        ("v8_native_work/fixed_observer_certificate.json",))
    v7_path = locate(args.v7_certificate,
        "research_notes/portable_direct/riesel_spectrum_20261121/spectrum/small_spectrum_certificate.json",
        ("v7_spectrum_work/small_spectrum_certificate.json",))
    retained = retained_exact_cost_checks(v8_path, v7_path, r1_residue)
    private_indices = [row[3] for row in OLD_ROWS]
    assert 41 - 5 == 36 and 63 - 3 == 60
    assert all(n in private_indices for n in (3, 5, 41, 63))
    assert has_exact_order(2, 37, 36) and has_exact_order(2, 109, 36)

    certificate = {
        "schema": "riesel-r0-r1-fiber-certificate-v1",
        "status": "Author derivation with exact finite arithmetic checks; no independent Review.",
        "scope": {
            "all_prime_results": "Written proof, using exact finite factor and incidence inputs below; no bounded-prime extrapolation.",
            "compact_witnesses": "Ordinary integer arithmetic only; native execution is supplied separately by the parent integration.",
            "retained_large_roots": "Only membership in the enlarged R1 fiber newly checked; existing gcd/exact-cost/native evidence reused.",
            "unbounded_cost": "For every finite s>=6 there are infinitely many R1 roots with delta_P=s and tau=20+s; no single root of infinite cost is asserted.",
        },
        "old_state": {"a_star": str(A_STAR), "M": str(M), "P": P,
                      "full_old_period_checked": old_period, "holes_u_mod105": H},
        "complete_factorizations_of_2_power_minus_1": FACTORS,
        "incidence": {"H_mod105": h_incidence, "A_v_mod35": a_set,
                      "A_incidence": a_incidence, "binary_w_mod35": w_set},
        "bounds": {"H_and_fixed_parity": [fraction_text(v) for v in generic_bounds],
                   "after_removing_d9_d7": [fraction_text(v) for v in next_bounds],
                   "R0_after_basic_pair": [fraction_text(v) for v in a_bounds],
                   "R1_non_W_after_basic_pair": [fraction_text(v) for v in non_w_bounds],
                   "R1_after_both_W": [fraction_text(v) for v in binary_bounds],
                   "no_basic_pair_five_upper_fraction_of_H": fraction_text(all_except_5_13_top5),
                   "R1_five_strict_case_lower_densities": {k: fraction_text(v) for k, v in r1_five_other_bounds.items()}},
        "R0": {"observer_channels": 25, "K": K, "observer_residue": 666303,
               "V_residues": dict(zip(V, R0_V_RESIDUES)),
               "base_root": str(r0_base), "root_progression_modulus": str(r0_modulus),
               "sharp_density_staircase": [fraction_text(v) for v in r0_densities],
               "W_phase_table": w_table, "relative_predicate_period_J": J,
               "category_state_count": 4 ** 4, "weighted_distinct_phase_counts": dict(r0_counts_by_phase),
               "predicate_counts_per_J": r0_predicate_counts,
               "predicate_relative_densities": {k: fraction_text(Fraction(v, J)) for k, v in r0_predicate_counts.items()},
               "least_period_essential_coordinate_witnesses": r0_essential,
               "all_five_prime_phase_dictionaries": 24,
               "raw_CRT_enumeration_count_with_repetitions": raw_count,
               "distinct_delta5_CRT_classes": len(r0_class_set),
               "delta5_residue_list_sha256": sha256(json.dumps(sorted(r0_class_set), separators=(",", ":")).encode()).hexdigest(),
               "compact_minimum_delta5_witness": r0_witness},
        "R1": {"observer_channels": 29, "L": L, "observer_residue": r1_residue,
               "W_residues": dict(zip(W, R1_W_RESIDUES)),
               "base_root": str(r1_base), "root_progression_modulus": str(r1_modulus),
               "sharp_density_staircase": [fraction_text(v) for v in r1_densities],
               "B_phase_table": b_table, "relative_predicate_period_Z": Z,
               "category_state_count": 3 ** 2, "weighted_distinct_phase_counts": dict(r1_counts_by_phase),
               "predicate_counts_per_Z": r1_predicate_counts,
               "predicate_relative_densities": {k: fraction_text(Fraction(v, Z)) for k, v in r1_predicate_counts.items()},
               "least_period_essential_coordinate_witnesses": r1_essential,
               "nested6_CRT_classes": sorted(r1_nested_classes),
               "compact_minimum_nested6_witness": r1_witness,
               "all_roots_delta_lower_bound": 6,
               "retained_exact_cost_examples": retained},
        "dependencies": [
            {"commit": "a2ae4d93398425e67dacbb4c99b7f3a6755e5771",
             "path": "research_notes/portable_direct/riesel_observers_20261122/fixed_observer/fixed_observer_certificate.json",
             "file_sha256": sha256(v8_path.read_bytes()).hexdigest()},
            {"commit": "af9e1a5e49386a28283781876e10742a71991036",
             "path": "research_notes/portable_direct/riesel_spectrum_20261121/spectrum/small_spectrum_certificate.json",
             "file_sha256": sha256(v7_path.read_bytes()).hexdigest()},
        ],
    }
    Path(args.output).write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({"status": "passed", "certificate": str(Path(args.output)),
                      "R0_counts": r0_predicate_counts, "R1_counts": r1_predicate_counts,
                      "R0_minimum_delta5_root": str(r0_minimum),
                      "R1_minimum_nested6_root": str(r1_nested_minimum),
                      "retained_exact_costs": [r["additional_cost"] for r in retained]}, indent=2))


if __name__ == "__main__":
    main()
