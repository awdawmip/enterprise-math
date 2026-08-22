#!/usr/bin/env python3
"""
R065 Phase A deterministic validator.

Information boundary:
- theorem decisions are derived only from the primitive substrate encoded here:
  3 component types, sector-supported nonnegative multiplicities, token typing,
  S3 relabeling, and admissible componentwise composition.
- no target formula is encoded.

The script uses exact integer / finite relational operations only.
"""

from itertools import permutations, product, combinations
from math import comb
import json
from collections import defaultdict

PERMS = list(permutations(range(3)))
MAX_M = 6


def support(n):
    return tuple(i for i, x in enumerate(n) if x != 0)


def admissible(n):
    return len(support(n)) <= 2


def permute(n, p):
    # p sends old component i to new component p[i]
    out = [0, 0, 0]
    for i, x in enumerate(n):
        out[p[i]] = x
    return tuple(out)


def orbit_signature(n):
    """Complete unlabeled multiplicity invariant under S3."""
    return tuple(sorted(n))


def partition_signature(n):
    """Unordered positive type-class cardinalities."""
    return tuple(sorted(x for x in n if x))


def total_tokens(n):
    return sum(n)


def support_cardinality(n):
    return sum(1 for x in n if x)


def largest_block(n):
    return max(n)


def cross_type_unordered_pairs(n):
    return sum(n[i] * n[j] for i in range(3) for j in range(i + 1, 3))


def same_type_unordered_pairs(n):
    return sum(comb(x, 2) for x in n)


SCALARS = {
    "TOTAL_TOKENS": total_tokens,
    "SUPPORT_CARDINALITY": support_cardinality,
    "LARGEST_TYPE_BLOCK": largest_block,
    "CROSS_TYPE_UNORDERED_PAIRS": cross_type_unordered_pairs,
    "SAME_TYPE_UNORDERED_PAIRS": same_type_unordered_pairs,
}


def state_key(n):
    return (total_tokens(n), orbit_signature(n), n)


STATES = [n for n in product(range(MAX_M + 1), repeat=3) if admissible(n)]


def verify_s3():
    mismatches = []
    for n in STATES:
        base = {
            "orbit": orbit_signature(n),
            "partition": partition_signature(n),
            **{k: f(n) for k, f in SCALARS.items()},
        }
        for p in PERMS:
            m = permute(n, p)
            cur = {
                "orbit": orbit_signature(m),
                "partition": partition_signature(m),
                **{k: f(m) for k, f in SCALARS.items()},
            }
            if cur != base:
                mismatches.append({"state": n, "perm": p, "base": base, "got": cur})
    return mismatches


def verify_token_renaming_by_canonical_reduction():
    by_orbit = defaultdict(list)
    for n in STATES:
        by_orbit[orbit_signature(n)].append(n)
    mismatches = []
    for sig, orbit in by_orbit.items():
        for name, f in SCALARS.items():
            vals = {f(n) for n in orbit}
            if len(vals) != 1:
                mismatches.append({"orbit": sig, "candidate": name, "values": sorted(vals)})
        ps = {partition_signature(n) for n in orbit}
        if len(ps) != 1:
            mismatches.append({"orbit": sig, "candidate": "PARTITION_SIGNATURE", "values": list(ps)})
    return mismatches


def verify_orbit_completeness():
    mismatches = []
    for a in STATES:
        for b in STATES:
            sig_equal = orbit_signature(a) == orbit_signature(b)
            isomorphic = any(permute(a, p) == b for p in PERMS)
            if sig_equal != isomorphic:
                mismatches.append({"a": a, "b": b, "sig_equal": sig_equal, "isomorphic": isomorphic})
    return mismatches


def verify_composition():
    mismatches = []
    tested = 0
    for a in STATES:
        for b in STATES:
            s = tuple(a[i] + b[i] for i in range(3))
            if not admissible(s):
                continue
            tested += 1
            if total_tokens(s) != total_tokens(a) + total_tokens(b):
                mismatches.append({"law": "TOTAL_TOKENS_ADDITIVE", "a": a, "b": b, "sum": s})
    return tested, mismatches


def smallest_counterexample(predicate):
    candidates = []
    for a in STATES:
        for b in STATES:
            s = tuple(a[i] + b[i] for i in range(3))
            if admissible(s):
                candidates.append((total_tokens(a)+total_tokens(b), orbit_signature(a), orbit_signature(b), a, b, s))
    candidates.sort()
    for _, _, _, a, b, s in candidates:
        if not predicate(a, b, s):
            return {"left": a, "right": b, "sum": s}
    return None


def find_additivity_counterexamples():
    out = {}
    for name, f in SCALARS.items():
        if name == "TOTAL_TOKENS":
            continue
        out[name] = smallest_counterexample(lambda a, b, s, f=f: f(s) == f(a) + f(b))
    return out


def orbit_composition_not_well_defined_witness():
    a1, b1 = (1, 0, 0), (1, 0, 0)
    a2, b2 = (1, 0, 0), (0, 1, 0)
    s1 = tuple(a1[i] + b1[i] for i in range(3))
    s2 = tuple(a2[i] + b2[i] for i in range(3))
    assert admissible(s1) and admissible(s2)
    assert orbit_signature(a1) == orbit_signature(a2)
    assert orbit_signature(b1) == orbit_signature(b2)
    assert orbit_signature(s1) != orbit_signature(s2)
    return {
        "input_orbit_left": orbit_signature(a1),
        "input_orbit_right": orbit_signature(b1),
        "aligned_sum_orbit": orbit_signature(s1),
        "distinct_type_sum_orbit": orbit_signature(s2),
        "aligned_case": {"left": a1, "right": b1, "sum": s1},
        "distinct_type_case": {"left": a2, "right": b2, "sum": s2},
    }


def compare_scalar_families():
    comparisons = {}
    names = list(SCALARS)
    ordered = sorted(STATES, key=state_key)
    for x, y in combinations(names, 2):
        witness = None
        for n in ordered:
            vx, vy = SCALARS[x](n), SCALARS[y](n)
            if vx != vy:
                witness = {"state": n, x: vx, y: vy}
                break
        comparisons[f"{x}__VS__{y}"] = witness
    return comparisons


def verify_normalized_monotone_witnesses():
    mismatches = []
    witnesses = {"TOTAL_TOKENS": total_tokens, "LARGEST_TYPE_BLOCK": largest_block}
    zero = (0, 0, 0)
    units = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    for name, f in witnesses.items():
        if f(zero) != 0:
            mismatches.append({"law": "zero_normalization", "candidate": name})
        for u in units:
            if f(u) != 1:
                mismatches.append({"law": "unit_normalization", "candidate": name, "unit": u})
        for a in STATES:
            for b in STATES:
                if all(a[i] <= b[i] for i in range(3)) and f(a) > f(b):
                    mismatches.append({"law": "componentwise_monotone", "candidate": name, "a": a, "b": b})
    return mismatches


def verify_conditional_additive_classification():
    mismatches = []
    for c in range(7):
        f = lambda n, c=c: c * total_tokens(n)
        for n in STATES:
            for p in PERMS:
                if f(permute(n, p)) != f(n):
                    mismatches.append({"law": "conditional_s3", "c": c, "state": n, "perm": p})
        for a in STATES:
            for b in STATES:
                s = tuple(a[i] + b[i] for i in range(3))
                if admissible(s) and f(s) != f(a) + f(b):
                    mismatches.append({"law": "conditional_additive", "c": c, "a": a, "b": b})
    return mismatches


def main():
    s3_mismatch = verify_s3()
    token_mismatch = verify_token_renaming_by_canonical_reduction()
    orbit_mismatch = verify_orbit_completeness()
    composition_tested, composition_mismatch = verify_composition()
    conditional_mismatch = verify_conditional_additive_classification()
    normalized_monotone_mismatch = verify_normalized_monotone_witnesses()
    additivity_ce = find_additivity_counterexamples()
    scalar_comparisons = compare_scalar_families()
    orbit_comp_witness = orbit_composition_not_well_defined_witness()

    all_mismatches = s3_mismatch + token_mismatch + orbit_mismatch + composition_mismatch + conditional_mismatch + normalized_monotone_mismatch

    report = {
        "schema": "R065_PHASEA_VALIDATOR_REPORT_V1",
        "domain": {
            "component_multiplicity_range": [0, MAX_M],
            "sector_supported_state_count": len(STATES),
            "s3_permutation_count": len(PERMS),
            "state_permutation_checks": len(STATES) * len(PERMS),
            "admissible_composition_pairs_tested": composition_tested,
        },
        "retained_candidates": ["ORBIT_SIGNATURE", "TYPE_PARTITION", *SCALARS.keys()],
        "theorem_checks": {
            "s3_invariance": "PASS" if not s3_mismatch else "FAIL",
            "token_renaming_via_canonical_isomorphism_reduction": "PASS" if not token_mismatch else "FAIL",
            "orbit_signature_complete_for_s3_isomorphism": "PASS" if not orbit_mismatch else "FAIL",
            "total_tokens_additive_on_all_admissible_compositions": "PASS" if not composition_mismatch else "FAIL",
            "conditional_additive_family_c_times_total_tokens": "PASS" if not conditional_mismatch else "FAIL",
            "total_and_largest_block_zero_unit_normalized_monotone": "PASS" if not normalized_monotone_mismatch else "FAIL",
            "orbit_quotient_composition_not_single_valued_without_relative_alignment": "PASS",
        },
        "smallest_additivity_counterexamples": additivity_ce,
        "orbit_composition_alignment_counterexample": orbit_comp_witness,
        "smallest_scalar_family_distinguishers": scalar_comparisons,
        "unclassified_mismatches": all_mismatches,
        "unclassified_mismatch_count": len(all_mismatches),
        "verdict": "PASS_ZERO_UNCLASSIFIED_MISMATCHES" if not all_mismatches else "FAIL_RESIDUALS_PRESENT",
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
