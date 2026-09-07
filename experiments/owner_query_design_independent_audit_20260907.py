#!/usr/bin/env python3
"""Bounded independent query-design audit; does not run the author's test suite."""
from __future__ import annotations

import argparse
from copy import deepcopy
from fractions import Fraction as F
import hashlib
from itertools import combinations
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "experiments/owner_query_design_20260907/query_design.py"
NOTE = ROOT / "research_notes/OWNER_OBSERVATION_QUERY_DESIGN_20260907.md"
sys.path.insert(0, str(SOURCE.parent))
import query_design as qd


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def binding(s, queries, chart):
    # Independent reproduction of the public canonical input contract.
    value = {"support_bound": s,
             "queries": [list(q) for q in sorted(tuple(sorted(q)) for q in queries)],
             "chart": {"anchor": list(chart.anchor), "permutation": list(chart.permutation),
                       "signs": list(chart.signs)}}
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(encoded.encode("ascii")).hexdigest()


def record(label, coordinate, weight):
    return {"label": label, "coordinate": list(coordinate),
            "weight": f"{weight.numerator}/{weight.denominator}"}


def run():
    alternate = tuple(tuple(a - 1 for a in q) for q in
                      ((1, 2, 3), (4, 5, 6), (1, 2, 6), (1, 3, 5), (2, 4, 6), (3, 4, 5)))
    covered = {p for q in alternate for p in combinations(q, 2)}
    missing = sorted(set(combinations(range(6), 2)) - covered)
    assert missing == [(0, 3), (1, 4), (2, 5)]
    assert all(sum(a in q for q in alternate) == 3 for a in range(6))
    failed_plan = qd.classify_query_set(2, alternate)
    assert failed_plan["status"] == "COUNTEREXAMPLE"
    assert failed_plan["missing_required_subsets"] == [list(p) for p in missing]
    alt_verification = qd.verify_counterexample(2, alternate, failed_plan["counterexample"])
    assert alt_verification["valid"] and alt_verification["target_support"] == 2

    formal = ((0, 1, 2), (0, 1, 3), (0, 4, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5))
    assert {p for q in formal for p in combinations(q, 2)} == set(combinations(range(6), 2))
    assert all(sum(a in q for q in formal) == 3 for a in range(6))
    guaranteed = qd.classify_query_set(3, formal)
    assert guaranteed["status"] == "GUARANTEED" and guaranteed["global_minimum_table_count"] == 6
    assert guaranteed["input_sha256"] == binding(3, formal, qd.DEFAULT_CHART)
    for witness in guaranteed["coverage_witness"]:
        assert tuple(witness["read_query"]) in formal
        assert set(witness["required_axes"]).issubset(witness["read_query"])

    # Target support one, competitor support nine: no hidden s-bound on nu.
    chart = qd.SignedAxisChart((7, -4, 9, 0, 3, -8), (4, 2, 5, 0, 3, 1), (-1, 1, -1, 1, -1, 1))
    queries = ((0, 1, 2),)
    coordinate = (3, -5, 7, -11, 13, -17)
    assert chart.to_chart(chart.to_world(coordinate)) == coordinate
    target = [record("target", chart.to_world((0,) * 6), F(1))]
    competitor = []
    for j in range(1, 10):
        x = (0, 0, 0, j, 0, 0)
        competitor.append(record(f"competitor:{j}", chart.to_world(x), F(1, 9)))
    base = {"schema": "owner_x6_query_counterexample_v1", "input_sha256": binding(1, queries, chart),
            "varying_axes": [3], "target": target, "competitor": competitor}
    baseline = qd.verify_counterexample(1, queries, base, chart=chart)
    assert baseline["valid"] and baseline["target_support"] == 1 and baseline["competitor_support"] == 9
    # The actual histograms differ (one 1 versus nine 1/9), but raw mass is equal.
    assert all(not c["fiber_histograms_equal"] for c in baseline["comparisons"])

    rejected = {}

    def reject(name, witness, *, support=1, qs=queries, frame=chart):
        verdict = qd.verify_counterexample(support, qs, witness, chart=frame)
        assert verdict["valid"] is False, (name, verdict)
        rejected[name] = verdict["reason"]

    reject("changed_support_contract", base, support=2)
    reject("changed_chart_contract", base, frame=qd.DEFAULT_CHART)
    reject("changed_query_contract", base, qs=((0, 1, 3),))
    bad = deepcopy(base)
    bad["input_sha256"] = "0" * 64
    reject("wrong_contract_digest", bad)
    bad = deepcopy(base)
    bad["target"][0]["weight"] = "2/1"
    reject("false_mass_equality", bad)
    bad = deepcopy(base)
    bad["varying_axes"] = [0, 3]
    reject("false_varying_axes", bad)
    bad = deepcopy(base)
    bad["target"][0]["weight"] = "2/2"
    reject("noncanonical_rational", bad)
    bad = deepcopy(base)
    bad["target"][0]["weight"] = "0/1"
    reject("zero_branch_weight", bad)
    bad = deepcopy(base)
    bad["competitor"] = deepcopy(bad["target"])
    bad["competitor"][0]["label"] = "different-label-same-spatial-mass"
    bad["varying_axes"] = []
    reject("same_spatial_mass_different_label", bad)
    bad = deepcopy(base)
    bad["raw_tables_equal"] = True
    reject("untrusted_extra_equality_flag", bad)
    bad = deepcopy(base)
    newly_observed = ((0, 1, 3),)
    bad["input_sha256"] = binding(1, newly_observed, chart)
    reject("correctly_rebound_but_raw_tables_differ", bad, qs=newly_observed)

    # Digest binds the contract, not immutable witness bytes. Legitimately new
    # witnesses under the same contract must still be accepted on their merits.
    scaled = deepcopy(base)
    for item in scaled["target"] + scaled["competitor"]:
        weight = 2 * F(item["weight"])
        item["weight"] = f"{weight.numerator}/{weight.denominator}"
    assert scaled["input_sha256"] == base["input_sha256"]
    assert qd.verify_counterexample(1, queries, scaled, chart=chart)["valid"]
    split = deepcopy(base)
    split["target"] = [record("split:a", chart.to_world((0,) * 6), F(1, 3)),
                       record("split:b", chart.to_world((0,) * 6), F(2, 3))]
    split_result = qd.verify_counterexample(1, queries, split, chart=chart)
    assert split_result["valid"] and split_result["target_support"] == 1

    # can3 and depth are individually lossy; only their JOINT address is bijective.
    pairs = [((0, 0, 1), 1), ((1, 1, 1), 1)]
    swapped = [((1, 1, 2), 1), ((0, 0, 0), 1)]

    def branches(items, prefix):
        return [qd.Branch(f"{prefix}:{i}", tuple(address) + (0, 0, 0), F(weight))
                for i, (address, weight) in enumerate(items)]

    left, right = branches(pairs, "left"), branches(swapped, "right")
    q = (0, 1, 2)
    raw_left, raw_right = qd.observe(left, [q])[q], qd.observe(right, [q])[q]
    joint_left = qd.observe(left, [q], encoding="can3_depth")[q]
    joint_right = qd.observe(right, [q], encoding="can3_depth")[q]
    assert raw_left != raw_right and joint_left != joint_right

    def separate(joint, index):
        out = {}
        for address, mass in joint.items():
            key = address[index]
            out[key] = out.get(key, F(0)) + mass
        return out

    assert separate(joint_left, 0) == separate(joint_right, 0)
    assert separate(joint_left, 1) == separate(joint_right, 1)
    for raw, joint in ((raw_left, joint_left), (raw_right, joint_right)):
        reconstructed = {tuple(value + depth for value in can): mass
                         for (can, depth), mass in joint.items()}
        assert reconstructed == raw

    return {
        "schema": "owner_query_design_independent_audit_v1", "status": "PASS",
        "provenance": {"source_sha256": sha(SOURCE), "note_sha256": sha(NOTE),
                       "audit_script_sha256": sha(Path(__file__)),
                       "global_knowledge_canonical": "4fa7d7d0c19a5e80a681b33c8ee2ab643ce97563"},
        "alternate_six_tables": {"covered_pair_count": len(covered),
                                 "missing_pairs_one_based": [[a + 1 for a in p] for p in missing],
                                 "all_axis_degrees_three": True,
                                 "actual_brc_witness_verification": alt_verification},
        "formal_six_tables_cover_all_pairs": True,
        "independent_contract_digest_matches": True,
        "unrestricted_competitor_verification": baseline,
        "invalid_witness_mutations_rejected": rejected,
        "legitimate_common_scaling_accepted": True,
        "coalesced_support_one_despite_two_target_branches": True,
        "separate_can3_and_depth_lose_pairing": True,
        "joint_can3_depth_exactly_reconstructs_raw": True,
        "scope": "Focused independent probes plus separately written analytic audit; author 11-test suite not rerun",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    encoded = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8", newline="\n")
        print(json.dumps({"status": result["status"], "output_sha256": sha(args.output),
                          "invalid_mutations_rejected": len(result["invalid_witness_mutations_rejected"])}))
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
