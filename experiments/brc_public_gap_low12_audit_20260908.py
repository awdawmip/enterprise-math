"""Audit an existing square filter on three already materialized public gaps.

The companion input certificate is pinned by Git blob hash. No new challenge
integer, multiplier, ceiling position, or factor-search path is generated.
Timing replays repeat the same values; they are not new coverage observations.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha1, sha256
from math import gcd, isqrt, prod
from pathlib import Path
from random import Random
from statistics import median
from time import perf_counter_ns
import json
import platform
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--enterprise-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    sys.path.insert(0, str(args.enterprise_root / "src"))
    from enterprise_math import brc_opportunistic_shortcuts as portfolio
    from enterprise_math.brc_square_gap_prefilter import filtered_square_root

    expected_sources = {
        "brc_opportunistic_shortcuts.py": "7e186c6b17b4b04c37af875c939a92907e929e8a19b2c0c818d3e3bc5f8b94e7",
        "brc_square_gap_prefilter.py": "f8e178771a25221eaab16002b9ffacd188dc5f39be4948ec2b40ee3e22c9f716",
    }
    for name, expected in expected_sources.items():
        assert sha256((args.enterprise_root / "src" / "enterprise_math" / name).read_bytes()).hexdigest() == expected

    input_path = Path(__file__).resolve().parent / "brc_public_rsa_fixed_predicates_20260908.json"
    raw = input_path.read_bytes().replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n"
    input_blob = sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()
    assert input_blob == "e56cfc8457e2398b5de3c90182c2b37824580ef3", input_blob
    parent = json.loads(raw)
    assert [r["label"] for r in parent["records"]] == ["RSA-270", "RSA-896", "RSA-2048"]
    moduli = portfolio.LOW12_COMPACT_MODULI
    assert moduli == (4096, 3465, 221, 12673)

    def native_exact_root(value):
        root = isqrt(value)
        return root if root*root == value else None

    def low12_exact_root(value):
        # The catalog predicate remains unchanged and is only necessary.
        # Retain exact square verification at the output boundary.
        if not portfolio.passes_low12_compact_square_filter(value):
            return None
        return native_exact_root(value)

    public = []
    for item in parent["records"]:
        n = int(item["N"])
        state = item["state_annotation"]
        j, r, gap = int(state["J"]), int(state["R"]), int(state["next_square_gap"])
        assert j*j+r == n and 0 < r <= 2*j and gap == 2*j+1-r
        assert sha256(item["N"].encode("ascii")).hexdigest() == item["decimal_sha256"]
        tag = portfolio.brc_shadow_signature(n, j, r)
        # A distinct isolated cold-cache observation for this fixed value.
        # Cache changes are confined to this short-lived local process.
        portfolio._square_residue_bitset.cache_clear()
        started = perf_counter_ns()
        cold_result = low12_exact_root(gap)
        cold_ns = perf_counter_ns() - started
        cold_tables = portfolio._square_residue_bitset.cache_info().currsize
        expected = native_exact_root(gap)
        assert cold_result == filtered_square_root(gap) == expected
        public.append({"label": item["label"], "direction": state["direction"],
            "source_pdf": item["source_pdf"], "decimal_sha256": item["decimal_sha256"],
            "gap": str(gap), "gap_bits": gap.bit_length(), "shadow_tag": tag,
            "cold_observation_ns": cold_ns, "cold_tables_built": cold_tables,
            "expected_root": None if expected is None else str(expected)})

    # Independently check the packed residue sets over each small modulus.
    # The largest period examined is 12,673, not a challenge-factor interval.
    portfolio._square_residue_bitset.cache_clear()
    started = perf_counter_ns()
    payload_bytes = portfolio.low12_compact_raw_table_bytes()
    all_table_setup_ns = perf_counter_ns() - started
    table_checks = []
    for modulus in moduli:
        table = portfolio._square_residue_bitset(modulus)
        encoded = {r for r in range(modulus) if table[r >> 3] & (1 << (r & 7))}
        expected = {x*x % modulus for x in range(modulus)}
        assert encoded == expected
        table_checks.append({"modulus": modulus, "square_classes": len(encoded),
                             "payload_bytes": len(table), "complete_residue_set_equal": True})
    assert all(gcd(a, b) == 1 for i, a in enumerate(moduli) for b in moduli[i+1:])
    acceptance = Fraction(prod(row["square_classes"] for row in table_checks), prod(moduli))
    assert payload_bytes == 2559

    # Trace is diagnostic only. It does not change stage order or the predicate.
    for item in public:
        gap = int(item["gap"])
        stages = []
        for modulus in moduli:
            residue = gap % modulus
            table = portfolio._square_residue_bitset(modulus)
            passed = bool(table[residue >> 3] & (1 << (residue & 7)))
            stages.append({"modulus": modulus, "residue": residue, "passed": passed})
            if not passed:
                break
        item["stages"] = stages
        item["filter_passed"] = all(row["passed"] for row in stages)
        item["low12_verified_root"] = low12_exact_root(gap)
        assert item["low12_verified_root"] is None if item["expected_root"] is None else str(item["low12_verified_root"]) == item["expected_root"]

    # Known squares are positive controls for the filter, not extra RSA hits.
    positive = {0: 0, 1: 1}
    for item in public:
        root = isqrt(int(item["gap"]))
        for offset in (0, 1, 2, 3, 5, 8):
            positive[(root+offset)**2] = root+offset
    for square, expected_root in positive.items():
        assert portfolio.passes_low12_compact_square_filter(square)
        assert low12_exact_root(square) == filtered_square_root(square) == expected_root

    # Different exact backends, identical prepared-gap input and exact output.
    # Each target is timed separately; no D/U pooled speed claim is produced.
    methods = {"native_exact": native_exact_root,
               "existing_4032_exact": filtered_square_root,
               "existing_low12_exact": low12_exact_root}
    rng = Random(6090802)
    repetitions = 512
    for item in public:
        gap = int(item["gap"])
        expected = native_exact_root(gap)
        rounds = []
        for round_id in range(7):
            order = list(methods)
            rng.shuffle(order)
            ns_per_call = {}
            for name in order:
                fn = methods[name]
                started = perf_counter_ns()
                for _ in range(repetitions):
                    result = fn(gap)
                elapsed = perf_counter_ns() - started
                assert result == expected
                ns_per_call[name] = elapsed/repetitions
            rounds.append({"round": round_id+1, "order": order, "ns_per_call": ns_per_call})
        medians = {name: median(row["ns_per_call"][name] for row in rounds) for name in methods}
        item["timing"] = {"rounds": rounds, "repetitions_per_method_per_round": repetitions,
            "median_ns_per_call": medians,
            "low12_vs_native_ratio": medians["native_exact"]/medians["existing_low12_exact"],
            "low12_vs_4032_ratio": medians["existing_4032_exact"]/medians["existing_low12_exact"],
            "low12_faster_rounds_vs_native": sum(row["ns_per_call"]["existing_low12_exact"] < row["ns_per_call"]["native_exact"] for row in rounds),
            "low12_faster_rounds_vs_4032": sum(row["ns_per_call"]["existing_low12_exact"] < row["ns_per_call"]["existing_4032_exact"] for row in rounds)}
        saving = medians["existing_4032_exact"] - medians["existing_low12_exact"]
        item["timing"]["conditional_full_table_amortization_calls_vs_4032"] = None if saving <= 0 else (all_table_setup_ns / saving)

    inventory = []
    for spec in portfolio.SHORTCUT_SPECS:
        status = "PREREQUISITE_OR_EXECUTION_BUDGET_NOT_SUPPLIED"
        if spec.shortcut_id == "low12_compact_gap_filter":
            status = "REUSE_EXECUTED_ON_THREE_PINNED_PREPARED_GAPS"
        elif spec.shortcut_id == "brc_shadow_telemetry":
            status = "REUSE_EXECUTED_AS_METADATA_ONLY"
        inventory.append({"id": spec.shortcut_id, "family": spec.family,
            "catalog_trigger": spec.trigger, "catalog_safety": spec.safety.value,
            "this_audit_status": status})

    output = {
        "status": "EXACT_PREPARED_GAP_FILTER_AUDIT",
        "researcher": "EM-HME-0CE4FD / TASK_RESEARCH",
        "global_snapshot": "fca4ad184d83679f38a66ae99763c32abb829ee5",
        "project_parent": "b4dc28c17176fcd2660be9dd5194b06a2499fdac",
        "input_certificate_blob": input_blob, "source_sha256": expected_sources,
        "source_portfolio_blob": "1214aa09770893fb3de7f85b994d1994ff56bffe",
        "python": sys.version, "platform": platform.platform(),
        "observer_contract": {"input_to_filter": "prepared nonnegative completion gap A only",
            "future_operation": "exact integer square-root predicate; N/J/R are not accessed by timed backends",
            "separate_metadata": "public identifier, D/U state and existing shadow signature",
            "root_preparation": "reuse the pinned earlier certificate; no new N-root computation",
            "new_public_integers": 0, "new_ceiling_positions": 0, "unique_public_gaps": 3,
            "timing_repetitions_are_new_coverage": False},
        "cost_contract": {"warm_scope": "prepared-gap exact predicate only; input preparation, imports, table setup and output logging excluded",
            "cold_scope": "one isolated cache-cold LOW12 exact observation per public gap, including needed lazy tables",
            "full_table_setup": "all four tables, measured separately; not required for every early exit",
            "positive_square_controls": "correctness only; not included in public timing or hit counts",
            "amortization": "conditional replay estimate on the same fixed gap; not a new input distribution or full-pipeline gain",
            "factor_recovery_or_adaptive_routing": "NOT_PERFORMED"},
        "modulus_tables": table_checks, "raw_table_payload_bytes": payload_bytes,
        "full_table_setup_ns": all_table_setup_ns,
        "complete_period_acceptance_fraction": {"numerator": acceptance.numerator, "denominator": acceptance.denominator,
            "percent": float(acceptance)*100, "combined_period": str(prod(moduli)),
            "scope": "exact uniform complete residue period; not the RSA input distribution"},
        "known_square_positive_controls": len(positive), "records": public,
        "catalog_inventory": inventory,
        "catalog_family_counts": dict(Counter(row["family"] for row in inventory)),
        "goal_status": "ACTIVE; retain conditional local gains; complete shortcut library verification is unfinished",
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    destination = args.output_dir / "brc_public_gap_low12_audit_20260908.json"
    destination.write_text(json.dumps(output, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"output": str(destination), "table_counts": table_checks,
        "payload": payload_bytes, "setup_ns": all_table_setup_ns, "acceptance": output["complete_period_acceptance_fraction"],
        "positive_controls": len(positive), "public_results": [{"label": row["label"],
            "direction": row["direction"], "gap_bits": row["gap_bits"], "stages": row["stages"],
            "cold_ns": row["cold_observation_ns"], "cold_tables": row["cold_tables_built"],
            "timing": {key: value for key, value in row["timing"].items() if key != "rounds"}}
            for row in public], "inventory_count": len(inventory)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
