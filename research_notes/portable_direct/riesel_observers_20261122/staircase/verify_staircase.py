#!/usr/bin/env python3
"""Finite arithmetic evidence for the all-prime staircase and equality theorem.

The universal quantifiers are proved in proof.md. This program checks the
complete incidence/factorization inputs and, after the proof has reduced
equality to a finite dictionary, exhausts that dictionary's phases. It does
not use a prime-size or multiplicative-order search cutoff.
"""

from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import gcd, prod
from pathlib import Path

A_STAR = 690786768637635218740714348513373826260012289
P = [7, 17, 31, 41, 71, 97, 113, 127, 151, 241, 257, 281, 337,
     641, 673, 1321, 14449, 29191, 65537, 6700417]
M = prod(P)
H = [0, 1, 3, 6, 9, 10, 15, 16, 21, 30, 31, 33, 36, 45, 48, 49,
     51, 54, 55, 63, 64, 66, 69, 70, 75, 76, 78, 79, 84, 85,
     90, 91, 93, 96, 99, 100]
H_SET = set(H)
G = [1, 3, 5, 7, 15, 21, 35, 105]
U = [11, 61, 331]
ORD4 = {5: 2, 13: 6, 11: 5, 61: 30, 331: 15}
ROOT = 8681796600341899699165924755002845830837950628236344137765453
ROOT_MODULUS = 121041494945903853943122890515382691774327737794816871699188590
NESTED_ROWS = [(5, 1), (13, 0), (11, 0), (61, 16), (331, 4)]


def factor(n: int) -> dict[int, int]:
    """Complete trial division of the explicitly bounded proof inputs."""
    out = {}
    q = 2
    while q * q <= n:
        while n % q == 0:
            out[q] = out.get(q, 0) + 1
            n //= q
        q = 3 if q == 2 else q + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def order(base: int, q: int) -> int:
    assert gcd(base, q) == 1
    value, d = base % q, 1
    while value != 1:
        value = value * base % q
        d += 1
    return d


def crt(residues, moduli):
    x, modulus = 0, 1
    for residue, q in zip(residues, moduli, strict=True):
        assert gcd(modulus, q) == 1
        x += modulus * ((residue - x) * pow(modulus, -1, q) % q)
        modulus *= q
    return x, modulus


def missing_u(rows):
    return [u for u in range(210) if u % 105 in H_SET
            and all(u % ORD4[q] != c for q, c in rows)]


def category_phase(q: int, epsilon: int, category: int) -> int:
    candidates = [c for c in range(ORD4[q]) if c % 5 == category
                  and (q == 11 or c % 3 == 1)
                  and (q != 61 or c % 2 == epsilon)]
    assert len(candidates) == 1
    return candidates[0]


def canonical_rows(rows):
    return tuple(sorted(rows))


def verify():
    assert len(H_SET) == 36 and M == 1397394912916194098609132326092145093313722687204526281
    assert sorted(g for g in range(1, 106) if 105 % g == 0) == G
    maxima = [max(Counter(h % g for h in H).values()) for g in G]
    assert maxima == [36, 23, 11, 7, 6, 4, 2, 1]
    sub = {r: [h for h in H if h % 3 == r] for r in range(3)}
    assert [len(sub[r]) for r in range(3)] == [23, 13, 0]
    mod5_counts = {r: [sum(h % 5 == c for h in sub[r]) for c in range(5)]
                   for r in [0, 1]}
    assert mod5_counts == {0: [6, 6, 0, 6, 5], 1: [5, 5, 0, 0, 3]}

    fact_small = {j: factor(4**j - 1) for j in range(1, 7)}
    assert set().union(*(set(f) for f in fact_small.values())) == {3, 5, 7, 11, 13, 17, 31}
    facts = {m: factor(2**m - 1) for m in [20, 24, 60]}
    for m, f in facts.items():
        assert prod(q**e for q, e in f.items()) == 2**m - 1
        assert all(factor(q) == {q: 1} for q in f)
    assert facts[20] == {3: 1, 5: 2, 11: 1, 31: 1, 41: 1}
    assert facts[24] == {3: 2, 5: 1, 7: 1, 13: 1, 17: 1, 241: 1}
    assert facts[60] == {3: 2, 5: 2, 7: 1, 11: 1, 13: 1, 31: 1,
                         41: 1, 61: 1, 151: 1, 331: 1, 1321: 1}
    excluded = set(P) | {3, 5, 13}
    parity_equality_primes = [q for q in facts[20] if q not in excluded and order(16, q) == 5]
    fiber_equality_primes = [q for q in facts[60] if q not in excluded and order(2**12, q) == 5]
    assert parity_equality_primes == [11]
    assert fiber_equality_primes == U

    # At fixed gcd, formula K_g/(K*(period/g)) strictly decreases with period.
    # These scans check the claimed minimum admissible period in each of the
    # finitely many gcd columns, not an upper cutoff on arbitrary periods.
    minimum_all = [8, 9, 10, 7, 15, 21, 35, 105]
    minimum_parity = [4, 9, 5, 7, 15, 21, 35, 105]
    minimum_parity_without_11 = [4, 9, 10, 7, 15, 21, 35, 105]
    tables = {}
    for name, minima, allowed in [
        ("all", minimum_all, lambda d: d >= 7),
        ("parity", minimum_parity, lambda d: d not in {1, 2, 3, 6}),
        ("parity_without_11", minimum_parity_without_11, lambda d: d not in {1, 2, 3, 5, 6}),
    ]:
        values = []
        for g, k, d in zip(G, maxima, minima, strict=True):
            assert allowed(d) and gcd(d, 105) == g
            assert not any(allowed(x) and gcd(x, 105) == g for x in range(1, d))
            values.append(Fraction(k, 36 * (d // g)))
        tables[name] = values
    assert max(tables["all"]) == Fraction(23, 108)
    assert max(tables["parity"]) == Fraction(11, 36)
    assert max(tables["parity_without_11"]) == Fraction(1, 4)

    fiber_tables = {}
    for r in [0, 1]:
        k = len(sub[r])
        mx5 = max(mod5_counts[r])
        mx7 = max(Counter(h % 7 for h in sub[r]).values())
        values = [Fraction(1, 3), Fraction(mx5, k), Fraction(mx7, k), Fraction(1, k)]
        fiber_tables[r] = values
        for epsilon in [0, 1]:
            u0 = next(u for u in range(6) if u % 2 == epsilon and u % 3 == r)
            image = [v for v in range(35) if (u0 + 6*v) % 105 in H_SET]
            assert len(image) == k
            assert max(Counter(v % 5 for v in image).values()) == mx5
            assert max(Counter(v % 7 for v in image).values()) == mx7
    assert max(fiber_tables[0]) == Fraction(1, 3)
    assert max(fiber_tables[1]) == Fraction(5, 13)

    target_relative = {0: Fraction(1), 1: Fraction(1, 2),
                       2: Fraction(13, 72), 3: Fraction(8, 72),
                       4: Fraction(3, 72), 5: Fraction(0)}
    cases = {}
    for t in [2, 3, 4]:
        cases[t] = {
            "neither_5_nor_13": 1 - Fraction(11, 36) - (t - 1)*Fraction(23, 108),
            "exactly_one": Fraction(1, 2) * (1 - (t - 1)*Fraction(11, 36)),
            "same_parity": Fraction(1, 2) * (1 - (t - 2)*Fraction(11, 36)),
            "opposite_parity_13_mod3_0": Fraction(13, 72) * (1 - (t - 2)*Fraction(5, 13)),
            "opposite_parity_13_mod3_1": Fraction(23, 72) * (1 - (t - 2)*Fraction(1, 3)),
            "opposite_parity_13_mod3_2": Fraction(1, 2) * (1 - (t - 2)*Fraction(11, 36)),
        }
        assert min(cases[t].values()) == target_relative[t]
    strict_one_t4 = Fraction(1, 2) * (1 - Fraction(11, 36) - 2*Fraction(1, 4))
    assert strict_one_t4 == Fraction(7, 72) > target_relative[4]
    single_coverage = {5: Fraction(1, 2), 13: Fraction(23, 72),
                       11: Fraction(11, 36), "other": Fraction(23, 108)}
    assert max(single_coverage.values()) == Fraction(1, 2)
    assert [q for q, v in single_coverage.items() if v == Fraction(1, 2)] == [5]

    # The analytic rigidity argument first proves these are the only possible
    # equality prime sets. Exhaust all phases in that resulting finite set.
    equality_rows = {}
    phase_scan_counts = {}
    for t in [2, 3, 4]:
        found, expected, scanned = set(), set(), 0
        for selected in combinations(U, t - 2):
            qs = [5, 13, *selected]
            for phases in product(*(range(ORD4[q]) for q in qs)):
                rows = list(zip(qs, phases, strict=True))
                missing = missing_u(rows)
                assert Fraction(len(missing), 72) >= target_relative[t]
                if Fraction(len(missing), 72) == target_relative[t]:
                    found.add(canonical_rows(rows))
                scanned += 1
        for epsilon in [0, 1]:
            base = [(5, 1-epsilon), (13, 3*epsilon)]
            if t == 2:
                expected.add(canonical_rows(base))
            elif t == 3:
                for q, category in product(U, [0, 1]):
                    expected.add(canonical_rows(base + [(q, category_phase(q, epsilon, category))]))
            else:
                for q0, q1 in product(U, U):
                    if q0 != q1:
                        expected.add(canonical_rows(base + [(q0, category_phase(q0, epsilon, 0)),
                                                           (q1, category_phase(q1, epsilon, 1))]))
        assert found == expected
        assert len(found) == {2: 2, 3: 12, 4: 12}[t]
        equality_rows[t] = []
        for rows in sorted(found):
            epsilon = dict(rows)[13] % 2
            missing = missing_u(rows)
            # Every listed phase is realizable by independent root congruences.
            roots = []
            for q, c in rows:
                x = pow(pow(2, c, q), -1, q)
                roots.append({"q": q, "order_4": ORD4[q], "phase_u": c,
                              "root_residues": sorted({x, (-x) % q})})
                actual = [a for a in range(q) if (a*a*pow(4, c, q)-1) % q == 0]
                assert actual == roots[-1]["root_residues"]
            if t == 4:
                assert missing == {0: [64, 154, 184], 1: [49, 79, 169]}[epsilon]
            equality_rows[t].append({"epsilon": epsilon, "rows": roots,
                                     "missing_u_mod210": missing,
                                     "missing_n_mod420": [2*u for u in missing]})
        phase_scan_counts[t] = scanned

    for q, d in ORD4.items():
        assert factor(q) == {q: 1}
        assert order(4, q) == d and order(2, q) == 2*d
        assert 210 % d == 0
    assert ROOT % (2*M) == A_STAR and ROOT % 3 == 0
    residues = [A_STAR, 0] + [pow(pow(2, c, q), -1, q) for q, c in NESTED_ROWS]
    moduli = [2*M, 3] + [q for q, c in NESTED_ROWS]
    assert crt(residues, moduli) == (ROOT, ROOT_MODULUS)
    assert all(ROOT % q == residue for q, residue in zip(moduli, residues, strict=True))
    nested = []
    for t in range(6):
        missing = missing_u(NESTED_ROWS[:t])
        density = Fraction(len(missing), 420)
        assert len(missing) == [72, 36, 13, 8, 3, 0][t]
        assert density == Fraction(6, 35) * target_relative[t]
        # Direct modular readout, independently of the phase comparisons.
        for u in range(210):
            modular_missing = u % 105 in H_SET and all(
                (ROOT*ROOT*pow(4, u, q)-1) % q for q, c in NESTED_ROWS[:t])
            assert modular_missing == (u in missing)
        nested.append({"budget": t, "rows": [{"q": q, "phase_u": c} for q, c in NESTED_ROWS[:t]],
                       "missing_u_mod210": missing, "missing_count_mod420": len(missing),
                       "density": str(density)})

    return {
        "schema": "enterprise-math.riesel-density-staircase.v1",
        "status": "Author proof and exact arithmetic verification; not independent project Review.",
        "researcher_id": "EM-DIRECT-970E1C",
        "activity_id": "RA-D2EC212845B63844081F9A14",
        "scope": "For every positive a congruent to a_star modulo 2M with 3 dividing a, every supplement of at most t new primes leaves density at least D_t. Equality conditions for t=1,2,3,4 are necessary and sufficient.",
        "a_star": str(A_STAR), "M": str(M), "P": P, "H": H,
        "density_staircase": [str(Fraction(n, 420)) for n in [72, 36, 13, 8, 3, 0]],
        "incidence": {"gcds": G, "maxima": maxima, "H_mod3_sizes": [23, 13, 0],
                      "H_r_mod5_counts": mod5_counts},
        "complete_factorizations": {"four_powers": fact_small, "two_powers": facts},
        "all_order_bounds": {"minimum_period_all": minimum_all,
                             "minimum_period_parity": minimum_parity,
                             "minimum_period_parity_without_11": minimum_parity_without_11,
                             "tables": {k: list(map(str, v)) for k, v in tables.items()},
                             "fiber_tables": {r: list(map(str, v)) for r, v in fiber_tables.items()},
                             "single_coverage_bounds": {str(k): str(v) for k, v in single_coverage.items()},
                             "case_gaps_relative_to_H": {t: {k: str(v) for k, v in row.items()} for t, row in cases.items()},
                             "strict_exactly_one_t4_gap": str(strict_one_t4)},
        "rigidity": {"parity_11_over_36_equality_primes": parity_equality_primes,
                     "fiber_5_over_13_equality_primes": fiber_equality_primes,
                     "fiber_maximal_mod5_categories": [0, 1],
                     "minimum_fiber_order_for_equality": 5},
        "equality_phase_dictionary_counts": {1: 2, 2: 2, 3: 12, 4: 12},
        "exhaustive_phase_scan_counts_after_analytic_reduction": phase_scan_counts,
        "equality_phase_dictionaries": equality_rows,
        "simultaneous_sharp_root": {"a": str(ROOT), "progression_modulus": str(ROOT_MODULUS),
                                    "properness_first_term": str(2*ROOT*ROOT - 1),
                                    "nested_prefixes": nested},
        "dependencies": {
            "repository": "awdawmip/enterprise-math",
            "old_certificate_commit": "e61a43115cf9dcbd0b3d8a746a5ac8086b8ca8fe",
            "old_certificate_path": "research_notes/portable_direct/riesel_mixed_20261119/certificate.json",
            "round7_commit": "af9e1a5e49386a28283781876e10742a71991036",
            "round7_gap_proof": "research_notes/portable_direct/riesel_spectrum_20261121/gap/proof.md",
            "round7_native_certificate": "research_notes/portable_direct/riesel_spectrum_20261121/gap/small_gap_certificate.json",
            "native_source_commit": "b1efc6c805661ed7b476e6e730107da6043176ee",
            "native_semantics": "Unchanged positive singleton BRC x -> 2x+1, even packet x -> 4x+3, weight and multiplicity 1. Reuses round7 full native run; this certificate makes no new native-execution claim."
        },
        "limits": ["The universal bound is sharp across roots; an arbitrary fixed root need not attain it.",
                   "No classification of all five-prime completions is claimed.",
                   "Density-optimal partial dictionaries do not determine the exact total cover cost."]
    }


if __name__ == "__main__":
    result = verify()
    target = Path(__file__).with_name("staircase_certificate.json")
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "certificate": str(target),
                      "density_staircase": result["density_staircase"],
                      "equality_phase_dictionary_counts": result["equality_phase_dictionary_counts"],
                      "exhaustive_phase_scan_counts": result["exhaustive_phase_scan_counts_after_analytic_reduction"]}))
