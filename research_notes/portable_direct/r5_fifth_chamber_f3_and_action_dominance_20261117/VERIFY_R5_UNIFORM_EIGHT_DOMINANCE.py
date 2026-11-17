#!/usr/bin/env python3
"""R5 fifth-chamber full-real-interval eight-action dominance proof.
Usage: python VERIFY_R5_UNIFORM_EIGHT_DOMINANCE.py EXACT_R5_ALL_101_BUDGETS.json
Standard library only; no floating-point arithmetic.
"""
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

PIN = "435e77af0d180eac32bd1f9c4c464bc4010b7551"
SHA = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
L = 25845652773852463277015040000
U = 58182461585441404127941754880
SEVEN = (214, 215, 216, 217, 223, 295, 296)
EIGHT = (214, 215, 216, 217, 223, 294, 295, 296)


def load(path):
    raw = Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SHA
    source = json.loads(raw)["counts_and_cohorts"]
    rows = {int(k): tuple(map(int, value["counts"]))
            for k, value in source.items()}
    assert set(rows) == set(range(214, 315))
    assert all(len(row) == 256 for row in rows.values())
    return rows


def gaps(row):
    return tuple(abs(row[i] - row[j])
                 for i in range(256) for j in range(i+1, 256))


def dominates_at_tau(j_gaps, k_gaps, tau):
    return all(a > tau or b <= tau
               for a, b in zip(j_gaps, k_gaps))


def dominates_for_all_tau(j_gaps, k_gaps):
    # A witness tau in [L,U) exists iff
    # a < b, a < U and b > L for a pair of masks.
    return all(not (a < b and a < U and b > L)
               for a, b in zip(j_gaps, k_gaps))


def check(path):
    rows = load(path)
    difference = {k: gaps(rows[k]) for k in range(214, 315)}
    assign = {}
    for k in range(214, 315):
        choices = [j for j in EIGHT
                   if j <= k
                   and dominates_for_all_tau(difference[j], difference[k])]
        assert choices, ("uncovered", k)
        assign[k] = choices[0]
    assert len(assign) == 101

    # Each high-noise endpoint indispensable j lacks a cheaper
    # normal-support domination replacement among all 101 queries.
    for j in SEVEN:
        assert all(not dominates_at_tau(difference[k], difference[j], U - 1)
                   for k in range(214, j))

    # Query 294 needs an extra eighth action to cover the low endpoint.
    witnesses = []
    for j in SEVEN:
        if j <= 294:
            assert not dominates_at_tau(difference[j], difference[294], L)
            pair = next((p, q)
                        for p in range(256)
                        for q in range(p+1, 256)
                        if abs(rows[j][p]-rows[j][q]) <= L
                        < abs(rows[294][p]-rows[294][q]))
            witnesses.append({"cheaper_j": j, "target_k": 294,
                              "two_masks": pair,
                              "j_gap": str(abs(rows[j][pair[0]]-rows[j][pair[1]])),
                              "k_gap": str(abs(rows[294][pair[0]]-rows[294][pair[1]]))})
    assert len(witnesses) == 5
    freq = dict(sorted(Counter(assign.values()).items()))
    assert sum(freq.values()) == 101
    return {
        "status": "PASS_R5_FIFTH_CHAMBER_UNIFORM_EIGHT_ACTIONS_MINIMAL_DOMINANCE",
        "source_pin": PIN, "input_sha256": SHA,
        "tau_left_inclusive": str(L), "tau_right_exclusive": str(U),
        "state_count": 256, "all_101_budgets_checked": True,
        "unordered_state_pairs": 32640,
        "uniform_dominating_actions": list(EIGHT),
        "minimum_cardinality_single_query_cost_safe_domination": 8,
        "assignment_frequency": freq, "per_budget_assignment": assign,
        "minimality_294_counterexamples": witnesses,
        "claim": "all real tau in this fifth chamber; any finite arbitrary unmarked error budget f",
        "independent_review": "NOT_REVIEWED"
    }


if __name__ == "__main__":
    assert len(sys.argv) in (2, 3)
    result = check(sys.argv[1])
    print(result["status"])
    print(result["assignment_frequency"])
    if len(sys.argv) == 3:
        Path(sys.argv[2]).write_text(json.dumps(result, indent=2)+"\n")
