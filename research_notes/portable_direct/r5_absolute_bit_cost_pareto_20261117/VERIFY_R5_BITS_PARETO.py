#!/usr/bin/env python3
"""Exact, auditable postprocessing of pinned R5 cohort coefficients.

Usage: python VERIFY_R5_BITS_PARETO.py compact_stdout.json EXACT_R5_ALL_101_BUDGETS.json
No nonstdlib packages or network calls. Integer arithmetic only.
"""
import hashlib
import itertools
import json
import pathlib
import sys

EXPECTED_COHORT_SHA256 = "a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d"
EXPECTED_COUNT_SHA256 = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
FROZEN_INPUT = "435e77af0d180eac32bd1f9c4c464bc4010b7551"


def load(path, expected_hash):
    payload = pathlib.Path(path).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == expected_hash, path
    return json.loads(payload)


def run(cohorts, counted):
    assert cohorts["scientific_input"] == FROZEN_INPUT
    assert FROZEN_INPUT in counted["scope"]
    assert counted["status"] == "PASS_R5_ALL_101_BUDGETS_256_MASKS_EXACT"
    assert cohorts["status"] == "PASS_R5_101_BUDGET_INTERACTION_HIERARCHY"
    peak_bits = {}
    reconstructed_values = 0
    for k in range(214, 315):
        coefficients = {int(mask): int(v) for mask, v in cohorts["all_budget_coefficients"][str(k)].items()}
        exact = [sum(v for mask, v in coefficients.items() if mask & b == mask) for b in range(256)]
        target = [int(v) for v in counted["counts_and_cohorts"][str(k)]["counts"]]
        assert exact == target, (k, "cohort mismatch")
        assert min(exact) > 0, k
        peak_bits[k] = max(n.bit_length() for n in exact)
        reconstructed_values += len(exact)
    assert reconstructed_values == 25856

    family3 = [(217, m, l) for m in range(224, 291) for l in range(298, 312)]
    family4 = [(217, e, m, l) for e in (218, 219) for m in range(224, 291) for l in range(298, 312)]
    assert len(family3) == 938 and len(family4) == 1876

    def outcomes(family):
        rows = [dict(budgets=q, cost=sum(q), max_count_bits=max(peak_bits[k] for k in q),
                     total_count_bits=sum(peak_bits[k] for k in q)) for q in family]
        # Strict two-objective domination; count ties as separate schedules.
        nd = [r for r in rows if not any(
            s["cost"] <= r["cost"] and s["max_count_bits"] <= r["max_count_bits"]
            and (s["cost"] < r["cost"] or s["max_count_bits"] < r["max_count_bits"])
            for s in rows)]
        nd.sort(key=lambda r: (r["cost"], r["max_count_bits"], r["budgets"]))
        best_peak = min(r["max_count_bits"] for r in rows)
        best_total = min(r["total_count_bits"] for r in rows)
        return {
            "candidate_count": len(rows),
            "pareto_schedules": nd,
            "best_peak_bits": best_peak,
            "best_peak_witness_count": sum(r["max_count_bits"] == best_peak for r in rows),
            "minimum_cost_at_best_peak_bits": min(r["cost"] for r in rows if r["max_count_bits"] == best_peak),
            "minimum_total_count_bits": best_total,
            "minimum_total_count_bits_witness_count": sum(r["total_count_bits"] == best_total for r in rows),
            "minimum_cost": min(r["cost"] for r in rows),
        }

    R3, R4 = outcomes(family3), outcomes(family4)
    e3 = [(739, 133, (217, 224, 298)), (804, 128, (217, 289, 298)), (805, 116, (217, 290, 298))]
    e4 = [(957, 133, (217, 218, 224, 298)), (1022, 128, (217, 218, 289, 298)), (1023, 116, (217, 218, 290, 298))]
    for observed, expected in [(R3, e3), (R4, e4)]:
        assert [(x["cost"], x["max_count_bits"], x["budgets"]) for x in observed["pareto_schedules"]] == expected
        assert observed["best_peak_bits"] == 116
    assert R3["minimum_total_count_bits"] == 335 and R4["minimum_total_count_bits"] == 443
    assert R3["minimum_total_count_bits_witness_count"] == 1
    assert R4["minimum_total_count_bits_witness_count"] == 2
    assert R3["best_peak_witness_count"] == 4 and R4["best_peak_witness_count"] == 8

    return {
        "status": "PASS_R5_SHARP_ABSOLUTE_MARGIN_BIT_COST_PARETO",
        "scientific_scope": "derived indexed-event radius-two integer count observer only, frozen input " + FROZEN_INPUT,
        "relation_to_prior": "conditional on the exact exhaustive classification of all D3/D4-margin-optimal fixed schedules at commit 9a87e52e",
        "full_count_checks": reconstructed_values,
        "middle_window_peak_bits": {str(k): peak_bits[k] for k in range(224, 291)},
        "late_window_peak_bits": {str(k): peak_bits[k] for k in range(298, 312)},
        "early_window_peak_bits": {str(k): peak_bits[k] for k in (217, 218, 219)},
        "optimal_three_calls": R3,
        "optimal_four_calls": R4,
        "interpretation": "bit_length(N) for positive exact integer N; peak bits per scalar count, not compressed-code lower bound or measured runtime",
    }


def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: python VERIFY_R5_BITS_PARETO.py compact_stdout.json EXACT_R5_ALL_101_BUDGETS.json")
    report = run(load(sys.argv[1], EXPECTED_COHORT_SHA256), load(sys.argv[2], EXPECTED_COUNT_SHA256))
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
