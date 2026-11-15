#!/usr/bin/env python3
"""External, fail-closed R063 Stage0 replay acceptance guard (stdlib only).

Does NOT execute or modify the frozen R063 benchmark, nor attest that it ran.
Use only after the genuine original program exits successfully in an authorized
checkout. Run: python3 this_file.py --out <isolated-replay-output-directory>
"""
import argparse
import hashlib
import json
from math import comb
from pathlib import Path

EXPECTED_ROW_SHA = "51891fbf9c3a66b1e00dfaa92fa6ae46984e4a6c99325624ec5b88371b66dcae"
EXPECTED_DISCOVERY_SHA = "6dd26e75436fb6740134590fc243b59ab9eb287cadbc46d417d5bbbb74022f0d"
EXPECTED_GATES = frozenset({
    "ALGEBRAIC_DERIVATION_VS_NATIVE_PATH_MULTIPLICITY_CLASSIFIED",
    "C2_UNSCALED_SQUARE_LIFT_CLASSIFIED", "C3_SCALED_SQUARE_LIFT_CLASSIFIED",
    "C4_GAUSSIAN_FACTOR_ROUTE_CLASSIFIED", "COMMITTED_DETERMINISTIC_CHECKER_PASS",
    "DISCOVERED_COMPONENT_ROOTS_MATCH_D2500_EXACTLY",
    "GENERAL_R_SQUARED_REGRESSION_R_LE_512_PASS_OR_MINIMAL_COUNTEREXAMPLE_PRESERVED",
    "HUGE_PATH_FIBER_COMPRESSED_REPRESENTATION_EXACT",
    "INPUT_ONLY_DISCOVERY_NO_BRANCH_HARDCODE",
    "NO_CARRIER_VECTOR_RELATION_PROMOTED_TO_NATIVE_IDENTITY",
    "NO_EXTRA_COMPONENT_ROOTS", "NO_JUMP_COUNT_AS_NATIVE_LENGTH_LEAKAGE",
    "ONE_SECTOR_TOTAL_PATH_CARDINALITY_EXACT", "PATHIFICATION_FORMULA_EXACT",
    "R061_TRACE_IDENTITY_COMPATIBILITY_PASS", "SCALAR_SQRT_2500_EXACT",
    "SECTOR_NORM_ALGEBRA_TYPED",
})
ROOTS = ((0, 50), (14, 48), (30, 40), (40, 30), (48, 14), (50, 0))
FILES = {
    "summary": "R063_STAGE0_REPLAY_SUMMARY.json",
    "regression": "R063_STAGE0_GENERAL_SQUARE_REGRESSION.json",
    "discovery": "R063_STAGE0_DISCOVERY_PHASE_FROZEN.json",
    "mismatches": "R063_STAGE0_MISMATCHES.json",
    "fiber": "R063_STAGE0_COMPONENT_ROOT_FIBER.json",
    "paths": "R063_STAGE0_PATH_CARDINALITY_CERTIFICATE.json",
}


def ensure(test, message):
    if not test:
        raise ValueError(message)


def _unique_pairs(pairs):
    out = {}
    for k, v in pairs:
        ensure(k not in out, f"duplicate JSON key: {k}")
        out[k] = v
    return out


def _read(path):
    ensure(path.is_file(), f"missing replay output: {path}")
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_pairs,
                      parse_constant=lambda v: (_ for _ in ()).throw(ValueError(f"nonfinite number: {v}")))


def _sha(obj):
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def verify(outdir):
    data = {k: _read(outdir / filename) for k, filename in FILES.items()}
    s, r, d, m, f, p = (data[k] for k in FILES)
    ensure(s.get("schema") == "R063_STAGE0_REPLAY_SUMMARY_V1", "wrong summary schema")
    ensure(r.get("schema") == "R063_STAGE0_GENERAL_SQUARE_REGRESSION_V1", "wrong regression schema")
    ensure(s.get("N") == 2500 and s.get("r") == 50, "not original N=2500/r=50 replay")
    gates = s.get("acceptance_gates")
    ensure(type(gates) is dict and frozenset(gates) == EXPECTED_GATES, "incomplete/altered 17-gate set")
    ensure(all(value is True for value in gates.values()), "original checker gate failed")
    ensure(r.get("r_range") == [1, 512] and type(r.get("tested_r_count")) is int
           and r["tested_r_count"] == 512, "regression range/count must be exactly 1..512")
    for name in ("C3_mismatch_count", "C4_mismatch_count", "combined_checker_mismatch_count"):
        ensure(type(r.get(name)) is int and r[name] == 0, f"regression {name} nonzero")
    ensure(r.get("rows_sha256") == EXPECTED_ROW_SHA, "regression rows digest drift")
    ensure(r.get("strong_result") == "C3_AND_C4_EXACT_FOR_ALL_TESTED_SQUARES", "wrong regression classification")
    gr = s.get("general_regression", {})
    ensure(gr.get("r_range") == [1, 512] and gr.get("combined_checker_mismatch_count") == 0
           and gr.get("rows_sha256") == EXPECTED_ROW_SHA, "summary/regression mismatch")
    ensure(d.get("discovery_snapshot_sha256") == EXPECTED_DISCOVERY_SHA
           and s.get("discovery_snapshot_sha256") == EXPECTED_DISCOVERY_SHA,
           "discovery freeze digest mismatch")
    unsigned = dict(d)
    del unsigned["discovery_snapshot_sha256"]
    ensure(_sha(unsigned) == EXPECTED_DISCOVERY_SHA, "actual discovery bytes do not match digest")
    ensure(m.get("schema") == "R063_STAGE0_MISMATCHES_V1" and m.get("mismatch_count") == 0
           and m.get("checker_mismatches") == [] and m.get("smallest_mismatch") is None,
           "original checker mismatches")
    ensure(s.get("C3", {}).get("exact_set_equality") is True
           and s.get("C4", {}).get("exact_set_equality") is True
           and s.get("C2", {}).get("exact_set_equality") is False,
           "C2/C3/C4 typed classification changed")
    ensure(p.get("N") == 2500 and p.get("r") == 50
           and f.get("N") == 2500 and f.get("r") == 50,
           "wrong path/cell population")
    ensure(p.get("ordered_nonnegative_branch_count") == 6 and f.get("root_count") == 6,
           "incomplete positive-sector roots")
    branches = p.get("branches")
    ensure(type(branches) is list and len(branches) == 6, "missing path branches")
    pairs = []
    total = 0
    for branch in branches:
        coord = branch.get("components")
        ensure(type(coord) is list and len(coord) == 2
               and all(type(v) is int and v >= 0 for v in coord), "untyped branch")
        a, b = coord
        ensure(a * a + b * b == 2500, "branch norm incorrect")
        count = branch.get("cardinality")
        ensure(type(count) is int and count == comb(a + b, a), "path BRC count not exact integer")
        ensure(branch.get("word_length_path_letters_only") == a + b, "word length mismatch")
        pairs.append((a, b))
        total += count
    ensure(tuple(pairs) == ROOTS, "ordered six-root set changed")
    ensure(total == 110695538274255714208, "sector total exact integer mismatch")
    ensure(type(s.get("one_sector_total_path_cardinality")) is int
           and s["one_sector_total_path_cardinality"] == total
           and type(p.get("one_sector_total_path_cardinality")) is int
           and p["one_sector_total_path_cardinality"] == total,
           "summary/path totals mismatch")
    ensure(f.get("ordered_nonnegative_component_roots") == [list(x) for x in ROOTS],
           "component fiber roots changed")
    ensure(s.get("final_classification") ==
           "PATH_VALUED_SQUARE_ROOT_FACTORIZATION_OPERATOR_COMPLETE_FOR_SQUARE_NATIVE_NORMS",
           "changed historical classification")
    return {"status": "PASS", "scope": "EXTERNAL_REPLAY_ARTIFACT_GUARD_ONLY",
            "regression_rows": 512, "original_gate_count": len(gates),
            "ordered_sector_roots": len(branches), "sector_brc_exact": str(total)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(verify(args.out), ensure_ascii=False, sort_keys=True))
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(json.dumps({"status": "FAIL", "scope": "EXTERNAL_REPLAY_ARTIFACT_GUARD_ONLY",
                          "reason": str(exc)}, ensure_ascii=False))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
