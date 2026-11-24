#!/usr/bin/env python3
"""Exact R2 budget-seven observer arithmetic, reusing the tail certificate.

No large factorization or primality search is repeated.  All prime inventories
come from the exhaustive analytic tail proof and its saved exact certificate.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from math import comb, gcd, prod
from pathlib import Path


FAMILIES = {
    "B": {"tail_name": "binary", "primes": (577, 487824887233), "phases": (0, 2)},
    "C": {"tail_name": "modulo_five", "primes": (181, 631, 23311, 54001, 18837001, 29247661), "phases": (0, 1, 3)},
    "D": {"tail_name": "ternary", "primes": (87211, 246241, 262657, 279073), "phases": (0, 1, 2)},
}
EXPECTED_T = 35095524795781473254136196580356738045833417602831290421525609131
EXPECTED_N = 916603393453788765429110921373053984059735989421687074488
EXPECTED_MIN = 168515727251568031139784117408423468924151126118048106286760549300706338389494633573


def decimal_ratio(num: int, den: int) -> str:
    with localcontext() as context:
        context.prec = 60
        return str(Decimal(num) / Decimal(den))


def crt(pairs: list[tuple[int, int]]) -> tuple[int, int]:
    root, modulus = 0, 1
    for residue, prime in pairs:
        assert gcd(modulus, prime) == 1
        root += modulus * ((residue - root) * pow(modulus, -1, prime) % prime)
        modulus *= prime
    return root, modulus


def prime_divisors(n: int) -> list[int]:
    result = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            result.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        result.append(n)
    return result


def default_tail_path() -> Path:
    here = Path(__file__).resolve().parent
    candidates = (
        here.parent / "v11_tail_work" / "tail_certificate.json",
        here.parent / "tail" / "tail_certificate.json",
        here / "tail_certificate.json",
    )
    return next((p for p in candidates if p.exists()), candidates[0])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tail-certificate", type=Path, default=default_tail_path())
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("observer_certificate.json"))
    args = parser.parse_args()
    tail_bytes = args.tail_certificate.read_bytes()
    tail = json.loads(tail_bytes)
    assert tail["schema"] == "riesel-r2-all-three-prime-tail-classification-v1"
    assert tail["total_phase_dictionaries"] == 146
    assert tail["total_CRT_progression_starts"] == 1160
    A2 = int(tail["R2"]["base_root"])
    S2 = int(tail["R2"]["progression_modulus"])
    all_primes = tuple(q for fam in FAMILIES.values() for q in fam["primes"])
    assert len(set(all_primes)) == 12
    T = prod(all_primes)
    assert T == EXPECTED_T and gcd(S2, T) == 1

    # Reconstruct every relevant root pair from n=32+36w; compare the saved
    # phase table and exact orders, without repeating large factorization.
    root_pairs: dict[int, dict[int, tuple[int, int]]] = {}
    orders = {}
    for name, fam in FAMILIES.items():
        previous = tail["families"][fam["tail_name"]]
        assert tuple(previous["candidate_primes"]) == fam["primes"]
        assert tuple(previous["w_phases"]) == fam["phases"]
        for q in fam["primes"]:
            assert q in tail["verified_prime_factors"]
            order = int(tail["base2_orders"][str(q)])
            assert pow(2, order, q) == 1
            assert all(pow(2, order // p, q) != 1 for p in prime_divisors(order))
            orders[q] = order
            root_pairs[q] = {}
            for phase in fam["phases"]:
                r = pow(pow(2, 16 + 18 * phase, q), -1, q)
                pair = tuple(sorted((r, (-r) % q)))
                assert len(set(pair)) == 2
                saved_pair = tuple(tail["phase_root_table"][str(q)][str(phase)]["root_residues"])
                assert pair == saved_pair
                assert all((a * a * pow(2, 32 + 36 * phase, q) - 1) % q == 0 for a in pair)
                root_pairs[q][phase] = pair
            assert len(set(r for pair in root_pairs[q].values() for r in pair)) == 2 * len(fam["phases"])

    def family_truth(name: str, residues: dict[int, int]) -> bool:
        fam = FAMILIES[name]
        return all(any(residues[q] % q in root_pairs[q][phase] for q in fam["primes"])
                   for phase in fam["phases"])

    def truth(residues: dict[int, int]) -> bool:
        return any(family_truth(name, residues) for name in FAMILIES)

    products, counts, family_records = {}, {}, {}
    for name, fam in FAMILIES.items():
        phases, qs = fam["phases"], fam["primes"]
        color_count = len(phases)
        total = prod(qs)
        inclusion_exclusion = sum((-1) ** j * comb(color_count, j)
                                  * prod(q - 2 * j for q in qs)
                                  for j in range(color_count + 1))
        # Exact weighted color-mask counting, independent of inclusion-exclusion.
        dp = {0: 1}
        for q in qs:
            nxt = {mask: 0 for mask in range(1 << color_count)}
            for mask, weight in dp.items():
                nxt[mask] += weight * (q - 2 * color_count)
                for color in range(color_count):
                    nxt[mask | (1 << color)] += 2 * weight
            dp = nxt
        assert sum(dp.values()) == total
        assert dp[(1 << color_count) - 1] == inclusion_exclusion
        products[name], counts[name] = total, inclusion_exclusion

        # Recheck all 1,160 short CRT starts from the saved phase/root inputs.
        starts = []
        minimizer = None
        for selected in permutations(qs, color_count):
            assignment = dict(zip(phases, selected))
            options = [root_pairs[q][phase] for phase, q in assignment.items()]
            for roots in product(*options):
                pairs = [(A2, S2)] + [(r, q) for r, q in zip(roots, selected)]
                start, modulus = crt(pairs)
                assert start > 0 and start % S2 == A2
                starts.append(start)
                if minimizer is None or start < int(minimizer["root"]):
                    minimizer = {"root": str(start), "root_digits": len(str(start)),
                                 "progression_modulus": str(modulus),
                                 "phase_to_prime": {str(b): q for b, q in assignment.items()},
                                 "root_residues": {str(q): r for q, r in zip(selected, roots)}}
        previous = tail["families"][fam["tail_name"]]
        assert len(starts) == previous["CRT_progression_starts"]
        assert minimizer == previous["minimum"]
        family_records[name] = {
            "name": fam["tail_name"], "primes": list(qs), "required_w_phases": list(phases),
            "modulus": str(total), "true_classes": str(inclusion_exclusion),
            "false_classes": str(total - inclusion_exclusion),
            "relative_density_in_R2_exact": str(Fraction(inclusion_exclusion, total)),
            "relative_density_in_R2_decimal": decimal_ratio(inclusion_exclusion, total),
            "weighted_color_mask_counts": {str(k): str(v) for k, v in sorted(dp.items())},
            "phase_dictionaries": previous["phase_dictionaries"],
            "CRT_progression_descriptions": len(starts), "minimum": minimizer,
            "sorted_CRT_start_list_sha256": sha256(("\n".join(map(str, sorted(starts))) + "\n").encode()).hexdigest(),
        }
    assert counts == {"B": 8, "C": 2068723011224822069760, "D": 42008160}
    assert products["C"] == 79208819702303143625098260481
    N = T - prod(products[k] - counts[k] for k in FAMILIES)
    assert N == EXPECTED_N

    intersections = {}
    for size in (1, 2, 3):
        for selected in combinations(FAMILIES, size):
            amount = prod(counts[k] if k in selected else products[k] for k in FAMILIES)
            intersections["".join(selected)] = {"count_mod_T": str(amount),
                "relative_density_in_R2_exact": str(Fraction(amount, T)),
                "relative_density_in_R2_decimal": decimal_ratio(amount, T)}
    alternating_union = sum((-1) ** (len(k) + 1) * int(v["count_mod_T"])
                            for k, v in intersections.items())
    assert alternating_union == N
    atoms = {}
    for bits in product((0, 1), repeat=3):
        amount = prod(counts[k] if bit else products[k] - counts[k]
                      for k, bit in zip(FAMILIES, bits))
        atoms["".join(map(str, bits))] = {"count_mod_T": str(amount),
            "relative_density_in_R2_exact": str(Fraction(amount, T)),
            "relative_density_in_R2_decimal": decimal_ratio(amount, T)}
    assert sum(int(v["count_mod_T"]) for v in atoms.values()) == T
    assert T - int(atoms["000"]["count_mod_T"]) == N

    # A concrete essential-coordinate witness for each of the 12 primes.
    witnesses = []
    for name, fam in FAMILIES.items():
        for target in fam["primes"]:
            yes = {q: 0 for q in all_primes}
            others = [q for q in fam["primes"] if q != target]
            supplied = fam["phases"][:-1]
            missing = fam["phases"][-1]
            for phase, q in zip(supplied, others):
                yes[q] = root_pairs[q][phase][0]
            yes[target] = root_pairs[target][missing][0]
            no = dict(yes)
            no[target] = 0
            assert truth(yes) and not truth(no)
            assert all(family_truth(k, yes) == (k == name) for k in FAMILIES)
            yes_T, yes_modulus = crt([(yes[q], q) for q in all_primes])
            no_T, no_modulus = crt([(no[q], q) for q in all_primes])
            assert yes_modulus == no_modulus == T
            assert (yes_T - no_T) % (T // target) == 0
            assert (yes_T - no_T) % target != 0
            yes_R2, yes_M = crt([(A2, S2), (yes_T, T)])
            no_R2, no_M = crt([(A2, S2), (no_T, T)])
            assert yes_M == no_M == S2 * T
            assert yes_R2 % S2 == no_R2 % S2 == A2
            witnesses.append({"prime": target, "family": name,
                "missing_phase": missing,
                "true_residues": {str(q): r for q, r in yes.items()},
                "false_residues": {str(q): r for q, r in no.items()},
                "true_root_mod_T": str(yes_T), "false_root_mod_T": str(no_T),
                "true_positive_R2_root": str(yes_R2), "false_positive_R2_root": str(no_R2)})
    assert len(witnesses) == 12
    assert max(orders.values()) == 180
    minimum = min((v["minimum"] for v in family_records.values()), key=lambda v: int(v["root"]))
    assert int(minimum["root"]) == EXPECTED_MIN
    assert minimum == tail["minimum_conditional_on_fixed_prefix"]

    certificate = {
        "schema": "riesel-r2-complete-budget-seven-observer-v1",
        "status": "AUTHOR_PROOF_AND_EXACT_ARITHMETIC; NOT_INDEPENDENT_REVIEW",
        "researcher": "EM-DIRECT-970E1C", "activity": "RA-D2EC212845B63844081F9A14",
        "scope": "All roots in fixed R2; full delta_P=7 predicate after forced-prefix and exhaustive-tail theorems.",
        "reused_tail_certificate_sha256": sha256(tail_bytes).hexdigest(),
        "R2": tail["R2"], "prefix": [5, 13, 19, 73],
        "predicate": "B OR C OR D; each family contains every listed required phase among its prime coordinates.",
        "phase_root_pairs": {str(q): {str(b): list(v) for b, v in rows.items()} for q, rows in root_pairs.items()},
        "families": family_records, "all_relevant_prime_base2_orders": {str(q): t for q, t in orders.items()},
        "total_modulus": str(T), "true_classes_mod_T": str(N), "false_classes_mod_T": str(T - N),
        "delta7_relative_density_in_R2_exact": str(Fraction(N, T)),
        "delta7_relative_density_in_R2_decimal": decimal_ratio(N, T),
        "reciprocal_relative_density_in_R2_decimal": decimal_ratio(T, N),
        "intersections": intersections, "disjoint_partition_bit_order": ["B", "C", "D"],
        "disjoint_partition": atoms,
        "essential_coordinate_witnesses": witnesses,
        "root_modulus_characterization": "For every integer N>=1, a mod N decides delta_P<=7 on R2 iff T divides N.",
        "complete_residual_trajectory_characterization": "For every integer N>=1, (F_n(a) mod N)_{n>=1} decides delta_P<=7 on R2 iff T divides N.",
        "minimal_additional_root_modulus": str(T),
        "least_period_of_root_predicate_and_R2_progression_parameter": str(T),
        "minimum_additional_distinct_prime_channels": 12,
        "fixed_prime_channels": 31, "total_prime_channels_under_declared_counting_convention": 43,
        "Omega_7_R2": 180, "trajectory_Omega_7_R2": 180,
        "global_minimum_delta7_root_in_R2": minimum,
        "phase_dictionary_count": 146, "CRT_progression_description_count": 1160,
        "native_scope": "Fixed X6, typed integer register, positive singleton BRC weight and multiplicity one; x maps to 2x+1; full integer and joint cofactor data retained. Residue channels are observations, not replacement axes.",
        "nonclaims": ["No claim about Omega_7 on all R1.", "No minimum-channel claim for arbitrary noncongruence encodings.", "No independent project Review or new native execution.", "False predicate means delta_P>7, allowing infinity; it does not decide finite-cover existence."],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "T": str(T), "N": str(N),
        "relative_density_in_R2": decimal_ratio(N, T), "minimum_additional_prime_channels": 12,
        "Omega_7_R2": 180, "minimum_root_digits": minimum["root_digits"],
        "output": str(args.output.resolve())}))


if __name__ == "__main__":
    main()
