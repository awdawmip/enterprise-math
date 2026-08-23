"""Fail-closed cross-artifact validator for the frozen local checkpoint."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

from corpus import canonical_digest, generate_rows


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "research_output"
EXPECTED_CORPUS_DIGEST = "8897e83bff43616e52705a4640449f638505a35f46452ac00efada67885d7fd1"
EXPECTED_CONFIG_HASH = "6970dce467be91d889413c026ff13bdfb79901c40a4a7d18ef75caea5c6edf24"
EXPECTED_RUN_HASH = "3988fb9fc13beab74037c2baaeec8e24f077cd742b3c3f4f1d71fe46c70c34eb"
EXPECTED_VERIFICATION_HASH = "8ae201d659ff6f25882dc24c13fe0d761e0f209bb595604f419d4cd7eaef9f4b"
EXPECTED_VERIFICATION_DIGEST = "b6e20e176b721388ab004be26798bd38dec1d8a169bf7162a2a170bde01efc10"
LABEL = "INCONCLUSIVE_AFTER_VALIDATED_PARTIAL_MATRIX"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    required = [
        OUTPUT / "VALLEY_BAND_FACTORING_REPRODUCIBLE_BENCHMARK_ABLATION_20260823.md",
        OUTPUT / "reducer_results" / "VALLEY_BAND_FACTORING_REPRODUCIBLE_BENCHMARK_ABLATION_REDUCER_20260823.md",
        ROOT / "experiments" / "valley_band_benchmark",
        OUTPUT / "VALLEY_BAND_BENCHMARK_CORPUS_20260823.csv",
        OUTPUT / "VALLEY_BAND_BENCHMARK_RUNS_20260823.csv",
        OUTPUT / "VALLEY_BAND_BENCHMARK_AGGREGATES_20260823.csv",
        OUTPUT / "VALLEY_BAND_OPENING_COST_MODEL_20260823.md",
        OUTPUT / "VALLEY_BAND_BENCHMARK_ENVIRONMENT_20260823.json",
        OUTPUT / "evidence" / "VALLEY_BAND_FACTORING_REPRODUCIBLE_BENCHMARK_20260823.jsonl",
    ]
    assert all(path.exists() for path in required)
    config_path = ROOT / "experiments" / "valley_band_benchmark" / "frozen_config.json"
    assert sha(config_path) == EXPECTED_CONFIG_HASH
    assert canonical_digest(generate_rows()) == EXPECTED_CORPUS_DIGEST

    runs_path = OUTPUT / "VALLEY_BAND_BENCHMARK_RUNS_20260823.csv"
    assert sha(runs_path) == EXPECTED_RUN_HASH
    with runs_path.open(encoding="utf-8", newline="") as handle:
        runs = list(csv.DictReader(handle))
    assert len(runs) == 80 and len({row["run_id"] for row in runs}) == 80
    statuses = Counter(row["status"] for row in runs)
    assert statuses == Counter({"MAX_STEPS": 22, "TIMEOUT": 9, "NOT_RUN_BUDGET": 49})
    completed = [row for row in runs if row["completed"] == "true"]
    assert len(completed) == 31
    assert all(row["factor_validation_pass"] == "true" for row in completed)
    assert all(row["known_factor_used_in_decision"] == "false" for row in runs)
    assert all(row["factor_found"] == "false" for row in completed)

    for corpus_id in ("R96-00", "R96-01", "R96-02"):
        for repeat in range(3):
            selected = [row for row in completed if row["corpus_id"] == corpus_id
                        and row["repeat"] == str(repeat) and row["policy_variant"] == "frozen"
                        and row["algorithm"] in ("cfrac_point", "closed_point")]
            assert len(selected) == 2
            assert selected[0]["mathematical_relation_digest"] == selected[1]["mathematical_relation_digest"]
            assert selected[0]["rank_trajectory_digest"] == selected[1]["rank_trajectory_digest"]
    threshold_rows = [row for row in completed if row["algorithm"] == "closed_band"
                      and row["policy_variant"] == "frozen"]
    assert {int(row["band_threshold"]) for row in threshold_rows} == {32, 64, 128, 256, 512}
    assert all(row["status"] == "TIMEOUT" for row in threshold_rows)
    for corpus_id in ("F104", "F112", "F128"):
        assert any(row["corpus_id"] == corpus_id and row["algorithm"] == "cfrac_point"
                   and row["completed"] == "true" for row in runs)
    assert any(row["policy_variant"] == "multiplier_holdout" and row["multiplier"] == "13"
               and row["completed"] == "true" for row in runs)
    assert any(row["policy_variant"] == "adaptive_holdout" and row["completed"] == "true"
               for row in runs)
    qs = [row for row in runs if row["algorithm"] == "python_spqs_context"]
    assert len(qs) == 4 and all(row["status"] == "NOT_RUN_BUDGET" for row in qs)

    aggregates_path = OUTPUT / "VALLEY_BAND_BENCHMARK_AGGREGATES_20260823.csv"
    with aggregates_path.open(encoding="utf-8", newline="") as handle:
        aggregates = list(csv.DictReader(handle))
    assert len(aggregates) == 30
    assert all(row["source_runs_sha256"] == EXPECTED_RUN_HASH for row in aggregates)

    evidence_path = OUTPUT / "evidence" / "VALLEY_BAND_FACTORING_REPRODUCIBLE_BENCHMARK_20260823.jsonl"
    events = [json.loads(line) for line in evidence_path.read_text(encoding="utf-8").splitlines()]
    assert len(events) == 114
    assert events[0]["event"] == "matrix_start" and events[-1]["event"] == "matrix_end"
    assert events[-1]["completed_runs"] == 31 and events[-1]["not_run_runs"] == 49

    verification_path = OUTPUT / "VALLEY_BAND_VERIFICATION_SUMMARY_20260823.json"
    assert sha(verification_path) == EXPECTED_VERIFICATION_HASH
    verification = json.loads(verification_path.read_text(encoding="utf-8"))
    assert verification["digest"] == EXPECTED_VERIFICATION_DIGEST
    assert verification["result"]["paired_equivalence"]["paired_steps"] == 100000
    assert verification["result"]["band_roots"]["roots"] == 10783
    assert verification["result"]["negative_controls"]["invalid_band_root_rejected"] is True
    assert verification["result"]["negative_controls"]["recurrence_sign_invariant_failure"] is True
    smoke = verification["result"]["relation_rank_smoke"]
    assert all(smoke[key]["status"] == "MAX_STEPS"
               for key in ("cfrac_point", "closed_point", "closed_band_256_slp"))
    assert smoke["cfrac_point"]["rank"] > 0 and smoke["closed_point"]["rank"] > 0
    assert smoke["closed_band_256_slp"]["orbit_steps"] == 1000
    nondeterministic_fields = {"wall_seconds", "peak_memory_bytes", "stages"}
    assert all(not (nondeterministic_fields & set(metrics)) for key, metrics in smoke.items()
               if key != "point_stream_exact_agreement")

    report = required[0].read_text(encoding="utf-8")
    assert LABEL in report
    assert report.rstrip().endswith("Global-Knowledge-Sync: main@506eb72 / GLOBAL_KNOWLEDGE_V1")
    environment = json.loads(required[7].read_text(encoding="utf-8"))
    assert environment["node_reuse_disclosure"]["prior_lane_math_code_or_output_reused"] is False
    assert environment["matrix_execution"]["factor_rows"] == 0

    result = {
        "schema": "valley-band-local-freeze-validation-v1",
        "classification": LABEL,
        "required_artifacts": 9,
        "runs": len(runs),
        "status_counts": dict(sorted(statuses.items())),
        "paired_point_digest_checks": 9,
        "paired_steps": 100000,
        "band_root_checks": 10783,
        "factor_rows": 0,
        "hashes": {str(path.relative_to(ROOT)).replace("\\", "/"): sha(path)
                   for path in required if path.is_file()},
    }
    output_path = OUTPUT / "VALLEY_BAND_LOCAL_FREEZE_VALIDATION_20260823.json"
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(output_path), **{k: result[k] for k in (
        "classification", "required_artifacts", "runs", "status_counts", "factor_rows")}}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
