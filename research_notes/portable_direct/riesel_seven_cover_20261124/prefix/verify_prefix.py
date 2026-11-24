#!/usr/bin/env python3
"""Exact arithmetic support for the conditional seven-prime prefix theorem."""

from fractions import Fraction as F
from itertools import product
from math import gcd, isqrt, prod
from pathlib import Path
import json


P = {7, 17, 31, 41, 71, 97, 113, 127, 151, 241, 257, 281,
     337, 641, 673, 1321, 14449, 29191, 65537, 6700417}
H = {0, 1, 3, 6, 9, 10, 15, 16, 21, 30, 31, 33, 36, 45,
     48, 49, 51, 54, 55, 63, 64, 66, 69, 70, 75, 76, 78,
     79, 84, 85, 90, 91, 93, 96, 99, 100}
A = {1, 2, 10, 11, 12, 16, 17, 22, 25, 26, 30, 31, 32}
INACTIVE = {3, 11, 61, 331, 37, 109, 433}
EXCLUDED = P | {3, 5, 13}
FACTORS = {
    24: {3: 2, 5: 1, 7: 1, 13: 1, 17: 1, 241: 1},
    36: {3: 3, 5: 1, 7: 1, 13: 1, 19: 1, 37: 1, 73: 1, 109: 1},
    48: {3: 2, 5: 1, 7: 1, 13: 1, 17: 1, 97: 1, 241: 1, 257: 1, 673: 1},
    60: {3: 2, 5: 2, 7: 1, 11: 1, 13: 1, 31: 1, 41: 1, 61: 1,
         151: 1, 331: 1, 1321: 1},
    72: {3: 3, 5: 1, 7: 1, 13: 1, 17: 1, 19: 1, 37: 1, 73: 1,
         109: 1, 241: 1, 433: 1, 38737: 1},
    84: {3: 2, 5: 1, 7: 2, 13: 1, 29: 1, 43: 1, 113: 1,
         127: 1, 337: 1, 1429: 1, 5419: 1, 14449: 1},
    120: {3: 2, 5: 2, 7: 1, 11: 1, 13: 1, 17: 1, 31: 1, 41: 1,
          61: 1, 151: 1, 241: 1, 331: 1, 1321: 1, 61681: 1,
          4562284561: 1},
}


def prime_trial(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def exact_order_from_bound(base, q, bound):
    assert pow(base, bound, q) == 1
    return next(d for d in range(1, bound + 1)
                if bound % d == 0 and pow(base, d, q) == 1)


def zero_v_phases(q, residue, period):
    return [v for v in range(period)
            if (residue * residue * pow(2, 8 + 12 * v, q) - 1) % q == 0]


def main():
    primes = sorted(set().union(*(set(f) for f in FACTORS.values())))
    assert all(prime_trial(q) for q in primes)
    ord2 = {}
    for power, factors in FACTORS.items():
        assert prod(q ** multiplicity for q, multiplicity in factors.items()) == 2 ** power - 1
        for q in factors:
            order = exact_order_from_bound(2, q, power)
            assert q not in ord2 or ord2[q] == order
            ord2[q] = order

    f_order = {q: order // gcd(order, 12) for q, order in ord2.items()}
    power_for_f = {1: 24, 2: 24, 3: 36, 4: 48, 5: 60, 6: 72, 7: 84, 10: 120}
    expected = {1: [], 2: [], 3: [19, 37, 73, 109], 4: [],
                5: [11, 61, 331], 6: [433, 38737],
                7: [29, 43, 1429, 5419], 10: [61681, 4562284561]}
    inventories = {}
    for period, power in power_for_f.items():
        candidates = sorted(q for q in FACTORS[power]
                            if q not in EXCLUDED and f_order[q] == period)
        assert candidates == expected[period]
        inventories[period] = {
            "eligible": candidates,
            "not_fixed_inactive": [q for q in candidates if q not in INACTIVE],
            "base2_orders": {q: ord2[q] for q in candidates},
        }

    assert len(H) == 36 and len(A) == 13
    residual_u = {u for u in range(210) if u % 105 in H and u % 2 != 1 and u % 6 != 0}
    assert residual_u == {4 + 6 * v for v in A}
    counts = {g: [sum(r % g == c for r in A) for c in range(g)] for g in (1, 5, 7, 35)}
    assert [max(counts[g]) for g in (1, 5, 7, 35)] == [13, 5, 3, 1]
    assert counts[7] == [0, 2, 3, 3, 3, 2, 0]

    fixed = {19: (6, 3, [0]), 73: (37, 3, [1]),
             433: (0, 6, []), 38737: (38733, 6, [5])}
    fixed_phases = {}
    for q, (residue, period, phases) in fixed.items():
        assert f_order[q] == period
        observed = zero_v_phases(q, residue, period)
        assert observed == phases
        fixed_phases[q] = {"root_residue": residue, "f": period, "v_zero_phases": observed}

    # Exact inequalities used in the all-prime written reduction.
    nonw = [F(1, 6), F(5, 26), F(3, 13), F(1, 13)]
    one_w_div3 = [F(1, 6), F(5, 39), F(1, 13), F(1, 39)]
    assert max(nonw) == F(3, 13)
    assert F(2, 3) * max(nonw) == F(2, 13) < F(1, 6)
    assert one_w_div3[0] == F(1, 6) and all(x < F(1, 6) for x in one_w_div3[1:])
    assert F(1, 3) + 4 * F(1, 6) == 1
    assert 5 * F(5, 26) < 1
    assert F(3, 13) + 4 * F(5, 26) == 1
    m2_threshold = 1 - 2 * F(3, 13) - 2 * F(5, 26)
    assert m2_threshold == F(2, 13)
    assert F(3, 26) < m2_threshold and F(1, 13) < m2_threshold
    assert 2 * F(3, 13) + 2 * F(5, 26) == F(11, 13)
    m3_threshold = 1 - 3 * F(3, 13) - F(5, 26)
    assert m3_threshold == F(3, 26) > F(1, 13)

    # m=2: every abstract choice of the four unfixed phases fails even after
    # adding the prescribed v=5 (mod 6) channel. This is a full period check.
    m2_count = 0
    m2_min_missed = 210
    for c7a, c7b, c10a, c10b in product(range(7), range(7), range(10), range(10)):
        missed = [v for v in range(210)
                  if v % 35 in A
                  and v % 7 not in (c7a, c7b)
                  and v % 10 not in (c10a, c10b)
                  and v % 6 != 5]
        assert missed
        m2_min_missed = min(m2_min_missed, len(missed))
        m2_count += 1

    # m=3: whole remaining mod-7 classes always obstruct g=5,7,35
    # compatibility for either of the required e=2 channels.
    m3_count = 0
    m3_min_size = 35
    for phases in product(range(7), repeat=3):
        residual = {r for r in A if r % 7 not in phases}
        assert len(residual) >= 4
        assert len({r % 7 for r in residual}) >= 2
        assert len({r % 5 for r in residual}) >= 2
        for g in (5, 7, 35):
            assert len({r % g for r in residual}) >= 2
        m3_min_size = min(m3_min_size, len(residual))
        m3_count += 1

    # m=4: any uncovered nonempty class supplies the exact gcd obstruction.
    m4_count = 0
    m4_min_size = 35
    for phases in product(range(7), repeat=4):
        residual = {r for r in A if r % 7 not in phases}
        groups = [[r for r in residual if r % 7 == c] for c in range(7)]
        group = next(group for group in groups if group)
        assert len(group) >= 2
        assert gcd(35, group[1] - group[0]) == 7
        m4_min_size = min(m4_min_size, len(residual))
        m4_count += 1

    certificate = {
        "status": "PASS: exact arithmetic support; universal completeness rests on proof.md",
        "theorem": "For a in R2, every complete supplement Q outside P with |Q|<=7 and {5,13} subset Q also contains {19,73}.",
        "scope": {"researcher": "EM-DIRECT-970E1C", "activity": "RA-D2EC212845B63844081F9A14",
                  "independent_review": False, "new_native_execution": False,
                  "scientific_source_v10": "f57dd6fd49d5b3f0a12abb3703c76edd6dbd37b5",
                  "scientific_source_v9": "b1de1acbdc97b5e51d486127abd1fadd24babd99"},
        "A": sorted(A), "A_incidence_counts": counts,
        "fixed_root_phases": fixed_phases,
        "complete_factorizations": FACTORS,
        "deterministic_primality_method": "trial division through integer square root",
        "effective_period_inventories": inventories,
        "rational_thresholds": {"nonW_gcd_column_bounds": [str(x) for x in nonw],
                                "outside_one_W_divisible_by_3_bounds": [str(x) for x in one_w_div3],
                                "m2_each_other_minimum": str(m2_threshold),
                                "m3_each_other_minimum": str(m3_threshold)},
        "finite_geometry_checks": {
            "m2_phase_assignments": m2_count, "m2_common_period": 210,
            "m2_minimum_missed_positions": m2_min_missed,
            "m3_phase_assignments": m3_count, "m3_minimum_residual_size": m3_min_size,
            "m4_phase_assignments": m4_count, "m4_minimum_residual_size": m4_min_size,
        },
    }
    output = Path(__file__).with_name("prefix_certificate.json")
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({"result": "PASS", "inventory_f6_active": inventories[6]["not_fixed_inactive"],
                      "inventory_f7": inventories[7]["eligible"],
                      "inventory_f10": inventories[10]["eligible"],
                      "geometry": certificate["finite_geometry_checks"],
                      "certificate": str(output)}, indent=2))


if __name__ == "__main__":
    main()
