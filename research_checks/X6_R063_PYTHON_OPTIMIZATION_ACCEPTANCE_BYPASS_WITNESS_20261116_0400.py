#!/usr/bin/env python3
"""Deterministic synthetic replay acceptance gate witness, not a native R063 replay.

Usage: python [-O] ... --runner PATH.  Deliberately corrupts synthetic source
bytes, all original gates (one false), and original r=1..512 tested count (zero).
Returns JSON with whether each invalid object was accepted.
"""
import argparse
import importlib.util
import json
import sys
import tempfile
from pathlib import Path


def load(path):
    spec = importlib.util.spec_from_file_location("r063_attestor", path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def status(fn):
    try:
        fn()
        return {"accepted": True}
    except (AssertionError, FileNotFoundError, KeyError) as e:
        return {"accepted": False, "reason": str(e)[:180]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runner", type=Path, required=True)
    args = ap.parse_args()
    m = load(args.runner.resolve())
    with tempfile.TemporaryDirectory() as root:
        root = Path(root)
        repo = root / "repo"
        (repo / "scripts/r063_stage0_checker_parts").mkdir(parents=True)
        for file in m.SOURCES:
            p = repo / file
            p.write_bytes(b"INTENTIONALLY TAMPERED SOURCE; NOT FROZEN\n")
        source_test = status(lambda: m.check_sources(repo))

        out = root / "output"
        out.mkdir()
        for file in m.REQUIRED_OUTPUTS:
            (out / file).write_text("{}\n")
        discovery = {"input": {"N": 2500}, "generated_component_roots": [[0, 50]]}
        digest = m.canonical_sha256(discovery)
        m.EXPECTED_DISCOVERY_SHA = digest
        discovery["discovery_snapshot_sha256"] = digest
        reg = {
            "r_range": [1, 512], "tested_r_count": 0,
            "combined_checker_mismatch_count": 0,
            "C3_mismatch_count": 0, "C4_mismatch_count": 0,
            "rows_sha256": "SYNTHETIC_DIGEST", "C2_failure_count": 484
        }
        m.EXPECTED_ROWS_SHA = "SYNTHETIC_DIGEST"
        gates = {name: True for name in m.EXPECTED_GATES}
        gates["PATHIFICATION_FORMULA_EXACT"] = False
        summary = {
            "acceptance_gates": gates,
            "N": 2500, "r": 50, "discovery_snapshot_sha256": digest,
            "ordered_nonnegative_component_root_count": 6,
            "one_sector_total_path_cardinality": m.EXPECTED_SECTOR_BRC,
            "general_regression": {
                "r_range": [1, 512], "rows_sha256": "SYNTHETIC_DIGEST",
                "combined_checker_mismatch_count": 0,
            }
        }
        summary["summary_core_sha256"] = m.canonical_sha256(summary)
        entries = {
            "R063_STAGE0_DISCOVERY_PHASE_FROZEN.json": discovery,
            "R063_STAGE0_GENERAL_SQUARE_REGRESSION.json": reg,
            "R063_STAGE0_REPLAY_SUMMARY.json": summary,
            "R063_STAGE0_MISMATCHES.json": {"mismatch_count": 0},
            "R063_STAGE0_COMPONENT_ROOT_FIBER.json": {"root_count": 6, "C3_exact": True, "C4_exact": True},
            "R063_STAGE0_PATH_CARDINALITY_CERTIFICATE.json": {
                "one_sector_total_path_cardinality": m.EXPECTED_SECTOR_BRC,
                "branches": [{"cardinality": m.EXPECTED_SECTOR_BRC}],
            },
            "R063_STAGE0_DERIVATION_PROVENANCE_GRAPH.json": {"node_id_uniqueness": True},
        }
        for name, obj in entries.items():
            (out / name).write_text(json.dumps(obj), encoding="utf-8")
        output_test = status(lambda: m.audit_outputs(out, {}))
    print(json.dumps({
        "schema": "X6_R063_ASSERT_OPTIMIZATION_BYPASS_WITNESS_V1",
        "runner_name": args.runner.name,
        "python_optimize": sys.flags.optimize,
        "invalid_frozen_source": source_test,
        "invalid_zero_case_false_gate_output": output_test,
        "original_r063_benchmark_executed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
