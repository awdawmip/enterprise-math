"""Non-interactive runner for the immutable valley-band benchmark matrix."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import platform
import statistics
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable

from core import RunMetrics, run_collector, static_multiplier_score
from qs_context import run_python_spqs_context


ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = Path(__file__).with_name("frozen_config.json")
CORPUS_PATH = ROOT / "research_output" / "VALLEY_BAND_BENCHMARK_CORPUS_20260823.csv"
RUN_PATH = ROOT / "research_output" / "VALLEY_BAND_BENCHMARK_RUNS_20260823.csv"
EVIDENCE_PATH = ROOT / "research_output" / "evidence" / "VALLEY_BAND_FACTORING_REPRODUCIBLE_BENCHMARK_20260823.jsonl"
CALIBRATION_PATH = ROOT / "research_output" / "VALLEY_BAND_ADAPTIVE_CALIBRATION_20260823.json"


@dataclass(frozen=True)
class PublicInstance:
    corpus_id: str
    purpose: str
    split: str
    bits: int
    n: int


@dataclass(frozen=True)
class PlannedRun:
    corpus_id: str
    repeat: int
    algorithm: str
    threshold: int | None
    multiplier_policy: str
    multiplier: int
    large_prime_mode: str
    policy_variant: str = "frozen"
    priority: int = 50


STAGE_NAMES = (
    "state_update",
    "root_setup",
    "sieve",
    "trial_division",
    "recombination",
    "linear_algebra",
    "gcd_extraction",
)


RUN_FIELDS = [
    "run_id", "planned_order", "corpus_id", "purpose", "split", "bits", "n_sha256",
    "repeat", "algorithm", "band_threshold", "policy_variant", "multiplier_policy",
    "multiplier", "large_prime_mode", "factor_base_bound", "max_orbit_steps",
    "timeout_seconds", "status", "completed", "not_run_reason", "factor_found",
    "factor_validation_pass", "factor_found_value", "orbit_steps", "bands_considered",
    "bands_opened", "bands_skipped_resource", "total_band_width", "point_candidates",
    "band_candidates", "full_relations", "partial_relations", "dlp_edges",
    "completed_cycles", "rank", "dependencies", "dependencies_tested", "wall_seconds",
    "peak_memory_bytes",
] + [f"stage_{name}_seconds" for name in STAGE_NAMES] + [
    "rank_trajectory_digest", "relation_stream_digest", "mathematical_relation_digest",
    "error", "known_factor_used_in_decision",
]


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("ascii")).hexdigest()


def load_inputs() -> tuple[dict, dict[str, PublicInstance], dict[str, tuple[int, int]]]:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    public: dict[str, PublicInstance] = {}
    validation_only: dict[str, tuple[int, int]] = {}
    with CORPUS_PATH.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            corpus_id = row["corpus_id"]
            public[corpus_id] = PublicInstance(
                corpus_id, row["purpose"], row["split"], int(row["bits"]), int(row["N"])
            )
            # This mapping is not passed to planning, multiplier selection, collection,
            # dependency selection, or stopping.  It is read only after each run returns.
            validation_only[corpus_id] = (
                int(row["factor_p_validation_only"]), int(row["factor_q_validation_only"])
            )
    return config, public, validation_only


def build_plan(config: dict, public: dict[str, PublicInstance]) -> list[PlannedRun]:
    matrix = config["frozen_matrix"]
    plan: list[PlannedRun] = []
    # Three complete repeats of both independently equivalent point paths come first.
    for corpus_id in matrix["completed_sub128_core_instances"]:
        for repeat in range(config["timing_repetitions_sub128"]):
            for algorithm in ("cfrac_point", "closed_point"):
                plan.append(PlannedRun(corpus_id, repeat, algorithm, None, "M1", 1, "none", priority=10))
    # All pre-frozen band thresholds receive at least one scheduled diagnostic.
    for threshold in config["band_thresholds"]:
        plan.append(PlannedRun("R96-00", 0, "closed_band", threshold, "M1", 1, "slp", priority=20))
    plan.append(PlannedRun("R96-06", 0, "closed_band", None, "M1", 1, "slp",
                           "adaptive_holdout", 21))
    # Same smoothness base, with no-LP / SLP / DLP ablation.
    for mode in matrix["large_prime_modes"]:
        plan.append(PlannedRun("R96-00", 1, "closed_band", 256, "M1", 1, mode, "lp_ablation", 25))
    # Exact-size checkpoint diagnostics cover point, closed point, and full band.
    for corpus_id in matrix["checkpoint_instances"]:
        plan.extend(
            [
                PlannedRun(corpus_id, 0, "cfrac_point", None, "M1", 1, "none", "checkpoint", 16),
                PlannedRun(corpus_id, 0, "closed_point", None, "M1", 1, "none", "checkpoint", 31),
                PlannedRun(corpus_id, 0, "closed_band", 256, "M1", 1, "slp", "checkpoint", 32),
            ]
        )
    # Pinned same-language QS context; explicitly context-only in the reports.
    for corpus_id in matrix["context_qs_instances"]:
        plan.append(PlannedRun(corpus_id, 0, "python_spqs_context", None, "M1", 1, "none", "context_only", 35))
    # Remaining full core matrix rows are scheduled and remain visible even if budget stops execution.
    existing = {(r.corpus_id, r.repeat, r.algorithm, r.threshold, r.large_prime_mode) for r in plan}
    for corpus_id in matrix["completed_sub128_core_instances"]:
        for repeat in range(config["timing_repetitions_sub128"]):
            for variant in matrix["core_variants"]:
                key = (corpus_id, repeat, variant["algorithm"], variant["threshold"], variant["large_prime_mode"])
                if key not in existing:
                    plan.append(
                        PlannedRun(
                            corpus_id, repeat, variant["algorithm"], variant["threshold"],
                            variant["multiplier_policy"], 1, variant["large_prime_mode"], "full_core", 50,
                        )
                    )
                    existing.add(key)
    return sorted(plan, key=lambda r: (r.priority, r.corpus_id, r.repeat, r.algorithm, r.threshold or -1, r.large_prime_mode))


def choose_multiplier(config: dict, public: dict[str, PublicInstance]) -> tuple[int, dict]:
    """Training-only static score plus point-pilot rank selection."""
    training_ids = [cid for cid in config["splits"]["training_ids"] if public[cid].bits == 96][:3]
    candidates = config["multiplier_candidates"]
    average_static = {
        m: statistics.fmean(static_multiplier_score(public[cid].n, m, config["multiplier_static_prime_limit"])
                            for cid in training_ids)
        for m in candidates
    }
    top = sorted(candidates, key=lambda m: (-average_static[m], m))[: config["multiplier_static_top_k"]]
    pilot: dict[int, dict[str, float | int]] = {}
    for multiplier in top:
        rank = relations = candidates_seen = 0
        wall = 0.0
        for corpus_id in training_ids:
            instance = public[corpus_id]
            metrics = run_collector(
                instance.n, multiplier, int(config["factor_base_bounds"][str(instance.bits)]),
                "cfrac_point", "none", config["multiplier_pilot_steps"], 6.0,
            )
            rank += metrics.rank
            relations += metrics.full_relations
            candidates_seen += metrics.point_candidates
            wall += metrics.wall_seconds
        pilot[multiplier] = {
            "rank": rank, "full_relations": relations, "candidates": candidates_seen,
            "wall_seconds": wall, "average_static_score": average_static[multiplier],
        }
    selected = max(
        top,
        key=lambda m: (
            pilot[m]["rank"], pilot[m]["full_relations"],
            -float(pilot[m]["wall_seconds"]), average_static[m], -m,
        ),
    )
    audit = {
        "schema": "valley-multiplier-training-v1", "training_ids": training_ids,
        "candidate_static_scores": average_static, "static_top_k": top, "pilots": pilot,
        "selected_multiplier": selected,
        "decision_inputs": "N, frozen candidates, static characters, and training pilot metrics only; no known factors",
    }
    return selected, audit


def adaptive_callback(calibration: RunMetrics | None, config: dict) -> tuple[Callable[[int, int, int, int], bool], dict]:
    policy = config["adaptive_policy"]
    full = calibration.full_relations if calibration else 0
    candidates = (calibration.band_candidates + calibration.point_candidates) if calibration else 0
    posterior = (full + policy["laplace_relation_numerator"]) / (
        candidates + policy["laplace_width_denominator"]
    )
    def should_open(a: int, _A: int, factor_base_size: int, width: int) -> bool:
        setup = 2 * factor_base_size * policy["setup_equivalent_candidates_per_root"]
        return (
            a >= policy["minimum_a"]
            and width * posterior >= policy["open_when_expected_full_relations_ge"] + setup
        )
    audit = {
        "schema": "valley-adaptive-calibration-v1", "training_split_only": True,
        "calibration_run": "R96-00/closed_band/threshold=256/repeat=0",
        "full_relations": full, "observed_candidates": candidates,
        "laplace_posterior_relation_per_candidate": posterior,
        "formula": "open iff a>=32 and width*p >= 0.75 + 2*factor_base_size*0.125",
    }
    return should_open, audit


def blank_row(run: PlannedRun, order: int, instance: PublicInstance, config: dict) -> dict[str, object]:
    limits = config["run_limits"][str(instance.bits)]
    run_id = f"{instance.corpus_id}|r{run.repeat}|{run.algorithm}|t{run.threshold}|{run.multiplier_policy}|m{run.multiplier}|{run.large_prime_mode}|{run.policy_variant}"
    row: dict[str, object] = {field: "" for field in RUN_FIELDS}
    row.update({
        "run_id": run_id, "planned_order": order, "corpus_id": instance.corpus_id,
        "purpose": instance.purpose, "split": instance.split, "bits": instance.bits,
        "n_sha256": sha256_text(str(instance.n)), "repeat": run.repeat,
        "algorithm": run.algorithm, "band_threshold": "" if run.threshold is None else run.threshold,
        "policy_variant": run.policy_variant, "multiplier_policy": run.multiplier_policy,
        "multiplier": run.multiplier, "large_prime_mode": run.large_prime_mode,
        "factor_base_bound": config["factor_base_bounds"][str(instance.bits)],
        "max_orbit_steps": limits["max_orbit_steps"], "timeout_seconds": limits["timeout_seconds"],
        "known_factor_used_in_decision": "false",
    })
    return row


def materialize_metrics(row: dict[str, object], metrics: RunMetrics, validation: tuple[int, int]) -> None:
    factor = metrics.factor
    valid = factor is None or factor in validation
    row.update({
        "status": metrics.status, "completed": "true", "not_run_reason": "",
        "factor_found": str(factor is not None).lower(), "factor_validation_pass": str(valid).lower(),
        "factor_found_value": "" if factor is None else factor, "orbit_steps": metrics.orbit_steps,
        "bands_considered": metrics.bands_considered, "bands_opened": metrics.bands_opened,
        "bands_skipped_resource": metrics.bands_skipped_resource,
        "total_band_width": metrics.total_band_width, "point_candidates": metrics.point_candidates,
        "band_candidates": metrics.band_candidates, "full_relations": metrics.full_relations,
        "partial_relations": metrics.partial_relations, "dlp_edges": metrics.dlp_edges,
        "completed_cycles": metrics.completed_cycles, "rank": metrics.rank,
        "dependencies": metrics.dependencies, "dependencies_tested": metrics.dependencies_tested,
        "wall_seconds": f"{metrics.wall_seconds:.9f}", "peak_memory_bytes": metrics.peak_memory_bytes,
        "rank_trajectory_digest": metrics.rank_trajectory_digest,
        "relation_stream_digest": metrics.relation_stream_digest,
        "mathematical_relation_digest": metrics.mathematical_relation_digest, "error": metrics.error,
    })
    for name in STAGE_NAMES:
        row[f"stage_{name}_seconds"] = f"{metrics.stages.get(name, 0.0):.9f}"


def append_evidence(handle, event: dict) -> None:
    handle.write(json.dumps(event, sort_keys=True, separators=(",", ":")) + "\n")
    handle.flush()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--matrix", choices=("frozen",), required=True)
    parser.add_argument("--budget-seconds", type=float, default=300.0,
                        help="bounded local checkpoint budget; all omitted planned rows remain explicit")
    args = parser.parse_args()
    config, public, validation_only = load_inputs()
    plan = build_plan(config, public)
    # Training-only multiplier decision happens before any holdout execution.
    multiplier, multiplier_audit = choose_multiplier(config, public)
    plan.insert(18, PlannedRun("R96-06", 0, "closed_point", None, "TRAINED_HOLDOUT", multiplier,
                               "none", "multiplier_holdout", 15))
    started = time.perf_counter()
    rows: list[dict[str, object]] = []
    calibration_metrics: RunMetrics | None = None
    adaptive_audit: dict | None = None
    EVIDENCE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with EVIDENCE_PATH.open("w", encoding="utf-8", newline="\n") as evidence:
        append_evidence(evidence, {
            "event": "matrix_start", "schema": "valley-benchmark-evidence-v1",
            "budget_seconds": args.budget_seconds, "planned_runs": len(plan),
            "config_sha256": hashlib.sha256(CONFIG_PATH.read_bytes()).hexdigest(),
            "corpus_sha256": hashlib.sha256(CORPUS_PATH.read_bytes()).hexdigest(),
            "python": platform.python_version(), "known_factor_firewall": config["known_factor_firewall"],
            "multiplier_training": multiplier_audit,
        })
        for order, run in enumerate(plan):
            instance = public[run.corpus_id]
            row = blank_row(run, order, instance, config)
            remaining = args.budget_seconds - (time.perf_counter() - started)
            if remaining <= 0:
                row.update({"status": "NOT_RUN_BUDGET", "completed": "false",
                            "not_run_reason": "global local-checkpoint execution budget exhausted"})
                rows.append(row)
                append_evidence(evidence, {"event": "run_not_started", "run_id": row["run_id"],
                                           "reason": row["not_run_reason"]})
                continue
            limits = config["run_limits"][str(instance.bits)]
            timeout = min(float(limits["timeout_seconds"]), max(0.001, remaining))
            append_evidence(evidence, {"event": "run_start", "run_id": row["run_id"],
                                       "remaining_budget_seconds": remaining})
            if run.policy_variant == "adaptive_holdout":
                callback, adaptive_audit = adaptive_callback(calibration_metrics, config)
                metrics = run_collector(
                    instance.n, run.multiplier, int(row["factor_base_bound"]), run.algorithm,
                    run.large_prime_mode, int(row["max_orbit_steps"]), timeout,
                    adaptive_open=callback,
                )
            elif run.algorithm == "python_spqs_context":
                metrics = run_python_spqs_context(instance.n, int(row["factor_base_bound"]),
                                                  int(row["max_orbit_steps"]), timeout)
            else:
                metrics = run_collector(
                    instance.n, run.multiplier, int(row["factor_base_bound"]), run.algorithm,
                    run.large_prime_mode, int(row["max_orbit_steps"]), timeout,
                    band_threshold=run.threshold,
                )
            materialize_metrics(row, metrics, validation_only[run.corpus_id])
            rows.append(row)
            append_evidence(evidence, {"event": "run_end", "run_id": row["run_id"],
                                       "status": metrics.status, "rank": metrics.rank,
                                       "full_relations": metrics.full_relations,
                                       "wall_seconds": metrics.wall_seconds,
                                       "factor_validation_pass": row["factor_validation_pass"]})
            if (run.corpus_id, run.repeat, run.algorithm, run.threshold, run.large_prime_mode) == (
                "R96-00", 0, "closed_band", 256, "slp"
            ):
                calibration_metrics = metrics
        if adaptive_audit is None:
            _, adaptive_audit = adaptive_callback(calibration_metrics, config)
        append_evidence(evidence, {"event": "adaptive_policy_frozen", **adaptive_audit})
        append_evidence(evidence, {"event": "matrix_end", "elapsed_seconds": time.perf_counter() - started,
                                   "completed_runs": sum(r["completed"] == "true" for r in rows),
                                   "not_run_runs": sum(r["completed"] != "true" for r in rows)})
    with RUN_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=RUN_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    CALIBRATION_PATH.write_text(json.dumps({
        "adaptive": adaptive_audit, "multiplier": multiplier_audit,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "runs": len(rows), "completed": sum(r["completed"] == "true" for r in rows),
        "not_run": sum(r["completed"] != "true" for r in rows),
        "elapsed_seconds": time.perf_counter() - started, "runs_csv": str(RUN_PATH),
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
