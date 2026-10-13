"""Only new post-open correctness/ledger checks for the frozen inverse generator.

No old checker/census, factor corpus, rank correlation, or 32--96bit benchmark is
run here. Forward k enumeration is an independent exact reference interface.
"""
from __future__ import annotations

import hashlib
import json
from math import isqrt
from pathlib import Path

from normalized_4kn_square_index_bucket_generator import (
    Candidate, PaidLedger, ascending_hart_stream, bucket_stream,
    build_qr_tables, consume_for_factor, ceil_cuberoot,
)

BASE = Path(__file__).resolve().parent
CASES = (
    (1, 1, 1), (1, 9, 4), (2, 11, 4), (3, 17, 4),
    (9, 12, 4), (15, 24, 4), (15, 25, 7), (21, 22, 4),
    (29, 73, 4), (77, 73, 4), (101, 73, 4),
    (100160063, 73, 4),
)


def reference_sqrt(n: int) -> int:
    z = isqrt(n)
    return z if z * z == n else z + 1


def reference(N: int, K: int, B: int) -> list[Candidate]:
    rows = []
    for k in range(1, K + 1):
        x = reference_sqrt(4 * N * k)
        e = x * x - 4 * N * k
        assert 0 <= e < 2 * x - 1
        rows.append(Candidate(k, x, e, B * e // (2 * x - 1)))
    return sorted(rows, key=lambda c: (c.bucket, c.k))


def verify_case(N: int, K: int, B: int) -> dict:
    expected = reference(N, K, B)
    meter = PaidLedger()
    actual = list(bucket_stream(N, K, B, meter))
    assert actual == expected
    assert len({c.k for c in actual}) == K == len(actual)
    a0, amax = reference_sqrt(4 * N), reference_sqrt(4 * N * K)
    A = amax - a0 + 1
    counts = meter.counts
    for key, value in {
        "integer_sqrt": 2,
        "bucket_pass": B,
        "square_index_row": B * A,
        "row_floor_divisions": 4 * B * A,
        "row_products": 3 * B * A,
        "square_index_transport": B * (A - 1),
        "candidate_emission": K,
    }.items():
        assert counts.get(key, 0) == value, (key, counts.get(key, 0), value)

    baseline_meter = PaidLedger()
    baseline = list(ascending_hart_stream(N, K, B, baseline_meter))
    assert [(c.k, c.x, c.residual) for c in baseline] == [
        (c.k, c.x, c.residual) for c in sorted(expected, key=lambda c: c.k)]
    assert baseline_meter.counts["integer_sqrt"] == K
    assert baseline_meter.counts["multiplier_point"] == K

    prefixes = []
    for index in sorted({0, len(expected) // 2, len(expected) - 1}):
        pm = PaidLedger()
        stream = bucket_stream(N, K, B, pm)
        found = None
        for _ in range(index + 1):
            found = next(stream)
        assert found == expected[index]
        assert found is not None
        exact_rows = found.bucket * A + found.x - a0 + 1
        assert pm.counts["square_index_row"] == exact_rows
        assert pm.counts["candidate_emission"] == index + 1
        stream.close()
        prefixes.append({"output_index": index, "k": found.k, "bucket": found.bucket,
                         "x": found.x, "exact_partial_rows": exact_rows})
    return {"N": N, "K": K, "B": B, "full_a_rows_per_pass": A,
            "all_candidate_and_order_equal": True, "full_ledger": counts,
            "forward_baseline_integer_sqrt_calls": K, "prefix_checks": prefixes}


def main() -> None:
    initial_freeze = (BASE / "NORMALIZED_4KN_BUCKET_GENERATOR_FREEZE_V1.json").read_bytes()
    initial_freeze_sha = hashlib.sha256(initial_freeze).hexdigest()
    results = [verify_case(*case) for case in CASES]

    # Exact original-family rounding witness: never 2*ceil_sqrt(kN).
    true_x = reference_sqrt(120)
    changed_x = 2 * reference_sqrt(30)
    assert (true_x, true_x * true_x - 120) == (11, 1)
    assert (changed_x, changed_x * changed_x - 120) == (12, 24)

    # Multiple k share one a when the safe K<=N regime is left.
    shell = [c for c in reference(15, 24, 4) if c.x == 38]
    assert [(c.k, c.residual) for c in sorted(shell, key=lambda c: c.k)] == [(23, 64), (24, 4)]
    assert 38 * 38 // 60 == 24  # single-floor rule misses k=23

    # A zero square with gcd N is a failed candidate, including the plus sign.
    common = PaidLedger()
    mods = (64, 3, 5, 7)
    tables = build_qr_tables(mods, common)
    failure_meter = PaidLedger()
    failed, failed_row = consume_for_factor(
        15, iter([Candidate(15, 30, 0, 0)]), mods, tables, failure_meter)
    assert failed is None and failed_row is None
    assert failure_meter.counts["trivial_gcd_failure"] == 2
    assert failure_meter.counts["gcd"] == 2

    # Tiny new consumer interface check; not a corpus/benchmark comparison.
    scan_meter, hart_meter = PaidLedger(), PaidLedger()
    ds, cs = consume_for_factor(15, bucket_stream(15, 3, 4, scan_meter),
                               mods, tables, scan_meter)
    dh, ch = consume_for_factor(15, ascending_hart_stream(15, 3, 4, hart_meter),
                               mods, tables, hart_meter)
    assert ds == 5 and cs is not None and cs.k == 2
    assert dh == 3 and ch is not None and ch.k == 1
    assert scan_meter.counts["square_index_row"] == 4
    assert hart_meter.counts["multiplier_point"] == 1

    cube_checks = []
    for n in (1, 2, 3, 7, 8, 9, 27, 28, 1000000001):
        cm = PaidLedger()
        k = ceil_cuberoot(n, cm)
        assert (k - 1) ** 3 < n <= k ** 3
        cube_checks.append({"N": n, "K": k, "public_budget_ledger": cm.counts})

    assert hashlib.sha256((BASE / "NORMALIZED_4KN_BUCKET_GENERATOR_FREEZE_V1.json").read_bytes()).hexdigest() == initial_freeze_sha
    report = {
        "schema": "HART_NEW_INVERSE_NORMALIZED_BUCKET_CORRECTNESS_LEDGER_CHECK_V1",
        "status": "PASS_NEW_EXACT_INTERFACE_AND_LEDGER_CHECKS",
        "scientist_id": "EM-SEMIPRIME-1F8B9B",
        "actual_run_id": "RUN-02bc03dfff15c15ce7daf2f3",
        "post_open_request_id": "hart-streaming-own-cost-audit-20261013-005",
        "precheck_freeze_sha256": initial_freeze_sha,
        "case_count": len(CASES), "cases": results,
        "normalization_witness": {"N": 15, "k": 2, "true_x": 11, "true_e": 1,
                                  "changed_x": 12, "changed_e": 24},
        "multi_k_shell_witness": {"N": 15, "K": 24, "a": 38, "rows": [[23, 64], [24, 4]]},
        "gcd_N_failure_preserved": True, "failure_ledger": failure_meter.counts,
        "tiny_consumer_interface": {
            "N": 15, "K": 3, "B": 4,
            "bucket_first_proper_factor": ds, "bucket_hit_k": cs.k,
            "ascending_first_proper_factor": dh, "ascending_hit_k": ch.k,
            "scan_ledger": scan_meter.counts, "ascending_ledger": hart_meter.counts,
            "finite_walltime_or_general_performance_claim": False},
        "common_qr_preparation_ledger": common.counts,
        "public_cube_budget_checks": cube_checks,
        "old_checkers_or_census_executed": False,
        "static_feature_or_rank_correlations_computed": False,
        "seven_bit_strata_ratio_holdout_classification_done": False,
        "reference_materialization": "Offline checker only; not free deployment cache.",
        "new_code_files_only": [
            "normalized_4kn_square_index_bucket_generator.py",
            "CHECK_FROZEN_NORMALIZED_4KN_GENERATOR_NEW_MICRO_CASES.py"],
        "proof_scope": "This literal row-scanning implementation only; no universal selector or factoring lower bound.",
    }
    path = BASE / "NEW_NORMALIZED_4KN_GENERATOR_EXACT_CHECK_REPORT.json"
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "case_count": len(CASES),
                      "new_N_above_old_census": 100160063, "new_K": 73,
                      "report": str(path),
                      "report_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    main()

