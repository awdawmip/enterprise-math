#!/usr/bin/env python3
"""Exact finite evidence for the optimal-budget residue observers.

The all-prime necessity theorem is proved in the companion staircase proof.
This verifier checks the complete finite phase dictionaries, their root
congruences, densities, least-period witnesses, and CRT minimum. It does not
replace that theorem by a prime cutoff. No external packages are required.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import gcd, prod
from pathlib import Path


A_STAR = 690786768637635218740714348513373826260012289
P = [7, 17, 31, 41, 71, 97, 113, 127, 151, 241, 257, 281, 337,
     641, 673, 1321, 14449, 29191, 65537, 6700417]
M = prod(P)
H = [0, 1, 3, 6, 9, 10, 15, 16, 21, 30, 31, 33, 36, 45, 48, 49,
     51, 54, 55, 63, 64, 66, 69, 70, 75, 76, 78, 79, 84, 85,
     90, 91, 93, 96, 99, 100]
U = (11, 61, 331)
QS = (5, 13, *U)
K = prod(QS)
D = {5: 2, 13: 6, 11: 5, 61: 30, 331: 15}
HOLES = [u for u in range(210) if u % 105 in H]
COUNTS = (72, 36, 13, 8, 3, 0)


def factor(n: int) -> dict[int, int]:
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def order(b: int, q: int) -> int:
    x, d = b % q, 1
    while x != 1:
        x = x * b % q
        d += 1
    return d


def crt(residues: list[int] | tuple[int, ...], moduli: list[int] | tuple[int, ...]) -> tuple[int, int]:
    x, modulus = 0, 1
    for residue, q in zip(residues, moduli, strict=True):
        assert gcd(modulus, q) == 1
        x += modulus * ((residue - x) * pow(modulus, -1, q) % q)
        modulus *= q
    return x, modulus


def phase(q: int, epsilon: int, category: int | None = None) -> int:
    if q == 5:
        return 1 - epsilon
    if q == 13:
        return 3 * epsilon
    assert category in {0, 1, 4}
    allowed = [c for c in range(D[q]) if c % 5 == category
               and (q == 11 or c % 3 == 1)
               and (q != 61 or c % 2 == epsilon)]
    assert len(allowed) == 1
    return allowed[0]


def roots(q: int, c: int) -> tuple[int, int]:
    a = pow(pow(2, c, q), -1, q)
    return tuple(sorted((a, -a % q)))


def basic_epsilon(residues: dict[int, int]) -> int | None:
    for epsilon in (0, 1):
        if all(residues[q] in roots(q, phase(q, epsilon)) for q in (5, 13)):
            return epsilon
    return None


def category(q: int, epsilon: int, residue: int) -> int | None:
    for r in (0, 1, 4):
        if residue in roots(q, phase(q, epsilon, r)):
            return r
    return None


def predicate(name: str, residues: dict[int, int]) -> bool:
    if name == "E1":
        return residues[5] != 0
    epsilon = basic_epsilon(residues)
    if epsilon is None:
        return False
    if name == "E2":
        return True
    labels = {category(q, epsilon, residues[q]) for q in U}
    if name == "E3":
        return bool(labels & {0, 1})
    if name == "E4":
        return {0, 1} <= labels
    assert name == "NESTED"
    return {0, 1, 4} <= labels


def missing(rows: list[tuple[int, int]]) -> list[int]:
    return [u for u in HOLES if all(u % D[q] != c for q, c in rows)]


def row_data(q: int, epsilon: int, r: int | None = None) -> dict:
    c = phase(q, epsilon, r)
    return {"q": q, "order_2": order(2, q), "order_4": D[q],
            "phase_u": c, "category": r, "root_residues": list(roots(q, c))}


def verify() -> dict:
    assert K == 14436565
    assert A_STAR % 3 == 0 and 0 < A_STAR < 6 * M
    assert gcd(6 * M, K) == 1 and len(HOLES) == 72
    for q in QS:
        assert factor(q) == {q: 1}
        assert q not in P and order(4, q) == D[q]
        assert 210 % D[q] == 0
        for c in range(D[q]):
            actual = [a for a in range(q) if (a * a * pow(4, c, q) - 1) % q == 0]
            assert actual == list(roots(q, c))

    # Equality theorem reduces every all-prime candidate to these phases.
    phase_table = []
    for epsilon in (0, 1):
        phase_table.append({"epsilon": epsilon,
                            "basic": [row_data(q, epsilon) for q in (5, 13)],
                            "categories": [row_data(q, epsilon, r)
                                           for q in U for r in (0, 1, 4)]})

    four_dictionaries = []
    for epsilon in (0, 1):
        for q0, q1 in permutations(U, 2):
            rows = [(5, phase(5, epsilon)), (13, phase(13, epsilon)),
                    (q0, phase(q0, epsilon, 0)), (q1, phase(q1, epsilon, 1))]
            remain = missing(rows)
            expected = [64, 154, 184] if epsilon == 0 else [49, 79, 169]
            assert remain == expected
            assert Fraction(len(remain), 420) == Fraction(1, 140)
            differences = [2 * (remain[i] - remain[0]) for i in range(1, 3)]
            assert gcd(420, *differences) == 60
            four_dictionaries.append({"epsilon": epsilon, "category_0_prime": q0,
                                      "category_1_prime": q1, "rows": rows,
                                      "missing_u_mod_210": remain,
                                      "missing_n_mod_420": [2*u for u in remain],
                                      "single_completion_order_divisor": 60})
    assert len(four_dictionaries) == 12
    factor_60 = factor(2**60 - 1)
    assert prod(q**e for q, e in factor_60.items()) == 2**60 - 1
    assert set(factor_60) - set(P) - {3, 5, 13} == set(U)

    # Count complete residue products. This is exhaustive over all U residues,
    # not over a selection of plausible phases or small roots.
    exact_counts = {name: 0 for name in ("E1", "E2", "E3", "E4", "NESTED")}
    basic_pairs = [(a5, a13) for a5 in range(5) for a13 in range(13)
                   if basic_epsilon({5: a5, 13: a13}) is not None]
    assert len(basic_pairs) == 8
    exact_counts["E1"] = 4 * K // 5
    exact_counts["E2"] = 8 * prod(U)
    per_epsilon_counts = []
    optimal_four_dictionary_multiplicity = Counter()
    eligible_third_channel_counts = Counter()
    for epsilon in (0, 1):
        mappings = [{a: category(q, epsilon, a) for a in range(q)} for q in U]
        local = Counter()
        for residues in product(*(range(q) for q in U)):
            labels = [mapping[a] for mapping, a in zip(mappings, residues, strict=True)]
            n0, n1, n4 = (labels.count(r) for r in (0, 1, 4))
            local["E3"] += n0 + n1 > 0
            local["E4"] += n0 > 0 and n1 > 0
            local["NESTED"] += n0 > 0 and n1 > 0 and n4 > 0
            eligible_third_channel_counts[n0 + n1] += 4
            if n0 * n1:
                optimal_four_dictionary_multiplicity[n0 * n1] += 4
        assert local == {"E3": 91628, "E4": 3176, "NESTED": 48}
        per_epsilon_counts.append({"epsilon": epsilon, "U_residue_counts": dict(local),
                                   "basic_root_sign_choices": 4})
        for name in ("E3", "E4", "NESTED"):
            exact_counts[name] += 4 * local[name]
    assert exact_counts == {"E1": 11549252, "E2": 1776808, "E3": 733024,
                            "E4": 25408, "NESTED": 384}
    assert optimal_four_dictionary_multiplicity == {1: 25024, 2: 384}
    assert eligible_third_channel_counts == {0: 1043784, 1: 682464, 2: 50048, 3: 512}
    assert 8*(prod(U) - 2*prod(q-2 for q in U) + prod(q-4 for q in U)) == exact_counts["E4"]
    assert 8*(prod(U) - prod(q-4 for q in U)) == exact_counts["E3"]
    assert 8*6*2**3 == exact_counts["NESTED"]

    five_dictionaries = []
    nested_residues = set()
    nested_root_examples = []
    for epsilon in (0, 1):
        for assignments in permutations((0, 1, 4)):
            labels = dict(zip(U, assignments, strict=True))
            phases = {q: phase(q, epsilon, labels.get(q)) for q in QS}
            rows = [(q, phases[q]) for q in QS]
            assert missing(rows) == []
            by_label = {r: q for q, r in labels.items()}
            chains = []
            for first_r, second_r in ((0, 1), (1, 0)):
                chain = [5, 13, by_label[first_r], by_label[second_r], by_label[4]]
                counts = [len(missing([(q, phases[q]) for q in chain[:t]])) for t in range(6)]
                assert tuple(counts) == COUNTS
                chains.append({"prime_order": chain, "hole_counts_mod_210": counts})
            local_examples = []
            for signed_roots in product(*(roots(q, phases[q]) for q in QS)):
                b, modulus = crt(signed_roots, QS)
                assert modulus == K and b not in nested_residues
                nested_residues.add(b)
                residues = dict(zip(QS, signed_roots, strict=True))
                assert all(predicate(name, residues) for name in exact_counts)
                a, a_modulus = crt([A_STAR, b], [6*M, K])
                assert a_modulus == 6*M*K
                assert a % (2*M) == A_STAR and a % 3 == 0
                assert 2*a*a - 1 > max(P + list(QS))
                local_examples.append({"root": str(a), "root_mod_K": b,
                                       "root_residues": list(signed_roots)})
                nested_root_examples.append({"root": a, "epsilon": epsilon,
                                             "U_categories": labels,
                                             "phases": phases, "root_mod_K": b,
                                             "root_residues": list(signed_roots)})
            minimum = min(local_examples, key=lambda x: int(x["root"]))
            five_dictionaries.append({"epsilon": epsilon, "U_categories": labels,
                                      "rows": rows, "ordered_chains": chains,
                                      "sign_choices": len(local_examples),
                                      "least_positive_root_for_dictionary": minimum})
    assert len(five_dictionaries) == 12 and len(nested_residues) == 384
    assert sum(len(x["ordered_chains"]) for x in five_dictionaries) == 24
    least = min(nested_root_examples, key=lambda x: x["root"])
    assert least["root"] == 39741911323337250951212360989279347168190786597922987443929
    assert least["root_mod_K"] == 10046119
    least["root"] = str(least["root"])

    # A witness differs at one prime coordinate only, so that coordinate
    # cannot be discarded by any smaller additive period (see proof).
    essential_primes = {"E1": (5,), "E2": (5, 13),
                        "E3": QS, "E4": QS, "NESTED": QS}
    witnesses = []
    base = {5: 2, 13: 1, 11: 1, 61: 25, 331: 62}
    for name, primes in essential_primes.items():
        for q in primes:
            yes = dict(base)
            if name == "E3" and q in U:
                yes.update({p: 0 for p in U})
                yes[q] = roots(q, phase(q, 0, 0))[0]
            elif name == "E4" and q in U:
                others = [p for p in U if p != q]
                yes.update({p: 0 for p in U})
                yes[q] = roots(q, phase(q, 0, 0))[0]
                yes[others[0]] = roots(others[0], phase(others[0], 0, 1))[0]
            no = dict(yes)
            no[q] = 0
            assert predicate(name, yes) and not predicate(name, no)
            assert [p for p in QS if yes[p] != no[p]] == [q]
            yes_residue, _ = crt([yes[p] for p in QS], QS)
            no_residue, _ = crt([no[p] for p in QS], QS)
            witnesses.append({"predicate": name, "essential_prime": q,
                              "true_residues": yes, "false_residues": no,
                              "true_a_mod_K": yes_residue, "false_a_mod_K": no_residue})

    compact_root = 8681796600341899699165924755002845830837950628236344137765453
    assert predicate("NESTED", {q: compact_root % q for q in QS})

    fixed_observer_residues = {5: 3, 13: 1, 11: 0, 61: 0, 331: 0}
    fixed_observer_residue, fixed_observer_modulus = crt(
        [fixed_observer_residues[q] for q in QS], QS)
    assert (fixed_observer_residue, fixed_observer_modulus) == (666303, K)
    fixed_observer_flags = {name: predicate(name, fixed_observer_residues)
                            for name in exact_counts}
    assert fixed_observer_flags == {"E1": True, "E2": True, "E3": False,
                                    "E4": False, "NESTED": False}

    return {
        "status": "PASS", "scope": "Author arithmetic verification; not independent formal Review",
        "old_root": str(A_STAR), "old_modulus_2M": str(2*M),
        "blocked_branch_modulus_6M": str(6*M), "observer_modulus_K": K,
        "root_progression_period_6MK": str(6*M*K),
        "old_hole_count_mod_210_u": len(HOLES),
        "universal_optimal_densities": [str(Fraction(x, 420)) for x in COUNTS],
        "phase_table": phase_table, "four_dictionaries": four_dictionaries,
        "factorization_2_power_60_minus_1": factor_60,
        "conditional_root_counts_mod_K": exact_counts,
        "conditional_root_densities": {name: str(Fraction(count, K)) for name, count in exact_counts.items()},
        "whole_old_class_densities_of_blocked_branch_subsets": {
            name: str(Fraction(count, 3*K)) for name, count in exact_counts.items()},
        "per_epsilon_U_counts": per_epsilon_counts,
        "optimal_four_dictionary_multiplicity": dict(optimal_four_dictionary_multiplicity),
        "eligible_third_channel_counts_within_E2": dict(eligible_third_channel_counts),
        "five_dictionaries": five_dictionaries,
        "nested_root_residues_mod_K": sorted(nested_residues),
        "least_nested_optimal_positive_root": least,
        "least_periods_in_branch_parameter_j": {name: prod(primes) for name, primes in essential_primes.items()},
        "essential_coordinate_witnesses": witnesses,
        "fixed_observer_residue_for_companion_spectrum": {
            "residues": fixed_observer_residues, "a_mod_K": fixed_observer_residue,
            "predicate_flags": fixed_observer_flags,
            "scope": "Finite CRT and predicate check only; the companion fixed-observer spectrum proof establishes its cost conclusions."
        },
        "limitations": [
            "All-prime necessity is the analytic companion theorem, not inferred from this enumeration.",
            "E_t asserts existence of a supplement attaining the stated universal lower bound, for t=1..4 and 3|a.",
            "NESTED classifies simultaneous optimal chains Q_0 subset ... subset Q_5; it does not classify every delta_P=5 root.",
            "Minimal periods concern these observable predicates, not the full native integer state.",
            "The least displayed root is least within NESTED, not necessarily among all delta_P=5 roots."
        ]
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify()
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
        print(json.dumps({"status": result["status"], "output": str(args.output),
                          "observer_K": K, "counts": result["conditional_root_counts_mod_K"],
                          "least_nested_root": result["least_nested_optimal_positive_root"]["root"]}))
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
