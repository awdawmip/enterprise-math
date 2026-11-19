#!/usr/bin/env python3
"""Task-level completeness reducer for opt-in parallel execution cohorts.

A cohort is execution-complete only after every declared lane has produced at
least one immutable result. Until then, a result from one lane must not close the
whole task or suppress sibling-lane execution. Once all lanes have evidence, the
exact current cohort result set requires an explicit synthesis. Reference methods
and count follow the actual proposition/task, while terminality still requires
the existing Result review and follow-up authority for every lane result.

Cohort records remain immutable historical control objects even after terminal
synthesis. Runtime terminality is therefore *derived*: when every ACTIVE cohort
record for a task has terminal exact-set synthesis, the task-level cohort overlay
becomes TERMINAL_PARALLEL_COHORTS and returns control to the parent. Opening a
new explicit replication/audit cohort later makes the derived state active again
without rewriting any prior cohort or result.
"""
from __future__ import annotations

import argparse
import json
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
    evidence_state = parallel.intake_state(intake, root)
    phase = evidence_state["parallel_state"]
    synthesis = evidence_state["synthesis"]
    authority_state: dict[str, Any] = {}
    if phase == "PARALLEL_SYNTHESIS_TERMINAL":
        if synthesis.get("terminal_control_disposition") not in research_result_records.TERMINAL_DISPOSITIONS:
            phase = "TERMINAL_SYNTHESIS_MISSING_CONTROL_DISPOSITION"
        else:
            evidence, authorities, pending, followup_pending = research_result_records._parallel_review_authority(result_ids, root)
            authority_state = {
                "result_review_authority": evidence,
                "result_operational_review_authority": authorities,
            }
            if pending:
                phase = "AWAITING_RESULT_REVIEW_AUTHORITY"
                authority_state["pending_result_review_ids"] = pending
            elif followup_pending:
                phase = "AWAITING_RESULT_REVIEW_FOLLOWUP"
                authority_state["pending_result_followup_ids"] = followup_pending
            elif any(authority.get("driver_followup_state") == research_result_records._followup_impl.RESULT_CONTINUATION_STATE
                     for authority in authorities.values()):
                phase = research_result_records._followup_impl.RESULT_CONTINUATION_STATE
    return {
        "state": phase,
        "terminal": phase == "PARALLEL_SYNTHESIS_TERMINAL",
        "evidence_set_sha256": evidence_hash,
        "intake_id": intake["intake_id"],
        "synthesis": synthesis,
        "reference_pass_ids": evidence_state["reference_pass_ids"],
        "reference_pass_count": evidence_state["reference_pass_count"],
        "reference_review_status": evidence_state["reference_review_status"],
        "stale_synthesis_ids": evidence_state["stale_synthesis_ids"],
        **authority_state,
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
            "AWAITING_SYNTHESIS": "SYNTHESIZE_EXACT_COHORT_EVIDENCE",
            "PARALLEL_SYNTHESIS_NONTERMINAL": "FOLLOW_SYNTHESIS_NONTERMINAL_DISPOSITION",
            "PARALLEL_SYNTHESIS_TERMINAL": "COHORT_CAN_CLOSE_AFTER_TERMINAL_CONTROL_DISPOSITION",
            "AWAITING_RESULT_REVIEW_AUTHORITY": "RESOLVE_RESULT_REVIEW_AUTHORITY",
            "AWAITING_RESULT_REVIEW_FOLLOWUP": "COMPLETE_RESULT_REVIEW_FOLLOWUP",
            "TERMINAL_SYNTHESIS_MISSING_CONTROL_DISPOSITION": "RESOLVE_TERMINAL_CONTROL_DISPOSITION",
            research_result_records._followup_impl.RESULT_CONTINUATION_STATE: "CONTINUE_INCOMPLETE_RESULT",
        }.get(phase["state"], "FAIL_CLOSED"),
    }


def task_active_cohort_state(task_id: str, root: Path = ROOT) -> dict[str, Any] | None:
    cohorts = active_cohorts(task_id, root)
    if not cohorts:
        return None
    states = [cohort_state(task_id, str(item["cohort_id"]), root) for item in cohorts]
    cohort_ids = [str(item["cohort_id"]) for item in cohorts]
    terminal_ids = [
        str(state["execution_cohort_id"])
        for state in states
        if state.get("terminal") is True
    ]
    if states and len(terminal_ids) == len(states):
        return {
            "task_id": task_id,
            "state": "TERMINAL_PARALLEL_COHORTS",
            "terminal": True,
            "active_cohort_ids": cohort_ids,
            "terminal_cohort_ids": terminal_ids,
            "cohorts": states,
            "terminal_control_dispositions": [
                state.get("terminal_control_disposition") for state in states
            ],
            "next_control_action": "REEVALUATE_PARENT",
        }
    return {
        "task_id": task_id,
        "state": "ACTIVE_PARALLEL_COHORTS",
        "terminal": False,
        "active_cohort_ids": cohort_ids,
        "terminal_cohort_ids": terminal_ids,
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


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Enterprise Math execution-cohort completeness/runtime audit"
    )
    sub = parser.add_subparsers(dest="command", required=True)
    audit_parser = sub.add_parser("audit")
    audit_parser.set_defaults(command="audit")
    status = sub.add_parser("status")
    status.add_argument("--task-id", required=True)
    status.add_argument("--cohort-id", required=True)
    args = parser.parse_args()
    if args.command == "audit":
        errors = audit()
        if errors:
            for error in errors:
                print("ERROR:", error)
            return 1
        print(
            f"PASS: cohort runtime completeness valid "
            f"({len(research_execution_cohorts.cohort_map(ROOT))} cohort record(s))."
        )
        return 0
    value = cohort_state(args.task_id, args.cohort_id)
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except CohortRuntimeError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
