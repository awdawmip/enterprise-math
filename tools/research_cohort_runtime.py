#!/usr/bin/env python3
"""Task-level completeness reducer for opt-in parallel execution cohorts.

A cohort is execution-complete only after every declared lane has produced at
least one immutable result. Until then, a result from one lane must not close the
whole task or suppress sibling-lane execution. Once all lanes have evidence, the
exact current cohort result set must traverse parallel intake -> reference pass 1
-> reference pass 2 -> synthesis before the cohort can be terminal.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

try:
    from tools import research_result_records
except ModuleNotFoundError:
    import research_result_records  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import research_execution_cohorts  # noqa: E402
import research_parallel_evidence as parallel  # noqa: E402


class CohortRuntimeError(ValueError):
    pass


def active_cohorts(task_id: str, root: Path = ROOT) -> list[dict[str, Any]]:
    values = [
        item
        for item in research_execution_cohorts.cohort_map(root).values()
        if item.get("task_id") == task_id and item.get("record_state") == "ACTIVE"
    ]
    return sorted(values, key=lambda item: str(item.get("cohort_id")))


def _cohort(task_id: str, cohort_id: str, root: Path) -> dict[str, Any]:
    cohort = research_execution_cohorts.cohort_map(root).get(cohort_id)
    if cohort is None or cohort.get("task_id") != task_id:
        raise CohortRuntimeError("unknown execution cohort for task")
    return cohort


def _lane_map(cohort: dict[str, Any]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for row in cohort.get("lanes", []):
        if not isinstance(row, dict) or not isinstance(row.get("lane_id"), str):
            raise CohortRuntimeError("cohort contains malformed lane")
        lane_id = row["lane_id"]
        if lane_id in out:
            raise CohortRuntimeError(f"duplicate lane_id: {lane_id}")
        out[lane_id] = row
    if len(out) < 2:
        raise CohortRuntimeError("parallel cohort requires at least two lanes")
    return out


def cohort_results(
    task_id: str, cohort_id: str, root: Path = ROOT
) -> list[dict[str, Any]]:
    return sorted(
        [
            item
            for item in research_result_records.iter_results(root)
            if item.get("task_id") == task_id
            and item.get("execution_cohort_id") == cohort_id
        ],
        key=lambda item: str(item.get("result_id")),
    )


def lane_results(
    task_id: str, cohort_id: str, lane_id: str, root: Path = ROOT
) -> list[dict[str, Any]]:
    return [
        item
        for item in cohort_results(task_id, cohort_id, root)
        if item.get("execution_lane_id") == lane_id
    ]


def _parallel_phase(
    task_id: str,
    publication_ids: list[str],
    result_ids: list[str],
    root: Path,
) -> dict[str, Any]:
    evidence_hash = parallel.evidence_hash(publication_ids, result_ids)
    intake = next(
        (
            item
            for item in parallel.intakes(root).values()
            if item.get("task_id") == task_id
            and item.get("evidence_set_sha256") == evidence_hash
            and sorted(item.get("result_ids") or []) == sorted(result_ids)
        ),
        None,
    )
    if intake is None:
        return {
            "state": "AWAITING_PARALLEL_INTAKE",
            "terminal": False,
            "evidence_set_sha256": evidence_hash,
            "intake_id": None,
            "synthesis": None,
        }
    rows = parallel.reference_passes(root).get(intake["intake_id"], [])
    by_number = {row.get("pass_number"): row for row in rows}
    if 1 not in by_number:
        phase = "AWAITING_REFERENCE_PASS_1"
        synthesis = None
    elif 2 not in by_number:
        phase = "AWAITING_REFERENCE_PASS_2"
        synthesis = None
    else:
        synthesis = next(
            (
                item
                for item in parallel.syntheses(root).values()
                if item.get("intake_id") == intake["intake_id"]
                and item.get("evidence_set_sha256") == evidence_hash
            ),
            None,
        )
        if synthesis is None:
            phase = "AWAITING_SYNTHESIS"
        elif synthesis.get("task_terminal") is True:
            phase = "PARALLEL_SYNTHESIS_TERMINAL"
        else:
            phase = "PARALLEL_SYNTHESIS_NONTERMINAL"
    return {
        "state": phase,
        "terminal": phase == "PARALLEL_SYNTHESIS_TERMINAL",
        "evidence_set_sha256": evidence_hash,
        "intake_id": intake["intake_id"],
        "synthesis": synthesis,
    }


def cohort_state(
    task_id: str, cohort_id: str, root: Path = ROOT
) -> dict[str, Any]:
    cohort = _cohort(task_id, cohort_id, root)
    lanes = _lane_map(cohort)
    results = cohort_results(task_id, cohort_id, root)
    result_ids: list[str] = []
    publication_ids: list[str] = []
    completed: set[str] = set()
    for result in results:
        lane_id = result.get("execution_lane_id")
        lane = lanes.get(str(lane_id))
        if lane is None:
            raise CohortRuntimeError(
                f"cohort result {result.get('result_id')} references unknown lane {lane_id}"
            )
        if result.get("publication_id") != lane.get("publication_id"):
            raise CohortRuntimeError(
                f"cohort result {result.get('result_id')} publication differs from lane pin"
            )
        rid = result.get("result_id")
        if not isinstance(rid, str) or not rid:
            raise CohortRuntimeError("cohort result missing result_id")
        result_ids.append(rid)
        publication_ids.append(str(result.get("publication_id")))
        completed.add(str(lane_id))
    missing = sorted(set(lanes) - completed)
    base = {
        "task_id": task_id,
        "execution_cohort_id": cohort_id,
        "cohort_record_state": cohort.get("record_state"),
        "lane_ids": sorted(lanes),
        "completed_lane_ids": sorted(completed),
        "missing_lane_ids": missing,
        "result_ids": sorted(result_ids),
        "publication_ids": sorted(set(publication_ids)),
    }
    if missing:
        return {
            **base,
            "state": "COHORT_EXECUTION_ACTIVE",
            "terminal": False,
            "ready_for_parallel_intake": False,
            "next_control_action": "DISPATCH_OR_COMPLETE_MISSING_LANES",
        }
    if len(result_ids) < len(lanes):
        raise CohortRuntimeError("cohort lane completeness invariant is inconsistent")
    phase = _parallel_phase(
        task_id,
        sorted(set(publication_ids)),
        sorted(result_ids),
        root,
    )
    synthesis = phase.get("synthesis")
    terminal = phase["state"] == "PARALLEL_SYNTHESIS_TERMINAL"
    return {
        **base,
        **phase,
        "ready_for_parallel_intake": True,
        "terminal": terminal,
        "terminal_control_disposition": (
            synthesis.get("terminal_control_disposition")
            if isinstance(synthesis, dict)
            else None
        ),
        "next_control_action": {
            "AWAITING_PARALLEL_INTAKE": "CREATE_EXACT_COHORT_PARALLEL_INTAKE",
            "AWAITING_REFERENCE_PASS_1": "REFERENCE_PASS_1",
            "AWAITING_REFERENCE_PASS_2": "REFERENCE_PASS_2",
            "AWAITING_SYNTHESIS": "SYNTHESIZE_EXACT_COHORT_EVIDENCE",
            "PARALLEL_SYNTHESIS_NONTERMINAL": "FOLLOW_SYNTHESIS_NONTERMINAL_DISPOSITION",
            "PARALLEL_SYNTHESIS_TERMINAL": "COHORT_CAN_CLOSE_AFTER_TERMINAL_CONTROL_DISPOSITION",
        }.get(phase["state"], "FAIL_CLOSED"),
    }


def task_active_cohort_state(task_id: str, root: Path = ROOT) -> dict[str, Any] | None:
    cohorts = active_cohorts(task_id, root)
    if not cohorts:
        return None
    states = [cohort_state(task_id, str(item["cohort_id"]), root) for item in cohorts]
    return {
        "task_id": task_id,
        "state": "ACTIVE_PARALLEL_COHORTS",
        "terminal": False,
        "active_cohort_ids": [str(item["cohort_id"]) for item in cohorts],
        "cohorts": states,
        "next_control_action": "RESOLVE_ACTIVE_COHORT_LANES_AND_SYNTHESIS",
    }


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        cohorts = research_execution_cohorts.cohort_map(root)
    except Exception as exc:
        return [str(exc)]
    for cohort_id, cohort in cohorts.items():
        task_id = cohort.get("task_id")
        if not isinstance(task_id, str) or not task_id:
            continue
        try:
            state = cohort_state(task_id, cohort_id, root)
            if state.get("terminal") is True:
                synthesis = state.get("synthesis")
                disposition = (
                    synthesis.get("terminal_control_disposition")
                    if isinstance(synthesis, dict)
                    else None
                )
                if disposition not in research_result_records.TERMINAL_DISPOSITIONS:
                    errors.append(
                        f"{cohort_id}: terminal cohort synthesis lacks terminal control disposition"
                    )
        except Exception as exc:
            errors.append(f"{cohort_id}: {exc}")
    return errors
