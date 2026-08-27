#!/usr/bin/env python3
"""Canonical result-registry shim with parallel-evidence and Driver follow-up gates.

The durable result/review writer/auditor lives in
``control_plane.research_result_records_impl``. This shim preserves its public
API while replacing task-level result-state reduction:

* multiple results are retained and routed through two-pass parallel evidence;
* post-cutover Driver reviews cannot terminalize runtime state until the
  automatic follow-up taskset (or canonical parent-closure exception) exists.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from control_plane import research_result_records_impl as _impl  # noqa: E402

for _name in dir(_impl):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_impl, _name)

if str(_impl.ROOT) not in sys.path:
    sys.path.insert(0, str(_impl.ROOT))
import research_parallel_evidence as _parallel  # noqa: E402
import research_driver_followup_guard as _driver_followup  # noqa: E402

ROOT = _impl.ROOT


def _publication_for_state(
    task_id: str, root: Path, publication_id: str | None
) -> str | None:
    if publication_id is not None:
        return publication_id
    try:
        current = research_task_records.current_records(root).get(task_id)
    except Exception:
        current = None
    if isinstance(current, dict) and isinstance(current.get("publication_id"), str):
        return current["publication_id"]
    return None


def _review_followup_gate(
    result: dict[str, Any],
    review: dict[str, Any],
    root: Path,
) -> dict[str, Any] | None:
    """Return a nonterminal state while a governed review lacks its next taskset."""
    review_id = review.get("review_id")
    if not isinstance(review_id, str) or not review_id:
        return {
            "state": "AWAITING_DRIVER_REVIEW",
            "result": result,
            "review": review,
            "terminal": False,
            "driver_followup_state": "REVIEW_ID_UNAVAILABLE",
            "driver_followup": None,
        }
    followup = _driver_followup.state_for_review(review_id, root)
    if followup.get("required") is True and followup.get("ready") is not True:
        return {
            "state": "AWAITING_DRIVER_REVIEW",
            "result": result,
            "review": review,
            "terminal": False,
            "driver_followup_state": followup.get("state"),
            "driver_followup_error": followup.get("error"),
            "driver_followup": followup.get("packet"),
        }
    return None


def _single_result_state(
    task_id: str,
    root: Path,
    publication_id: str | None,
) -> dict[str, Any] | None:
    values = [
        item
        for item in iter_results(root)
        if item.get("task_id") == task_id
        and (publication_id is None or item.get("publication_id") == publication_id)
    ]
    if not values:
        return None
    values.sort(
        key=lambda item: (item.get("frozen_at", ""), item.get("result_id", ""))
    )
    result = values[-1]
    review = latest_review(result["result_id"], root)
    if review is None:
        return {
            "state": "AWAITING_DRIVER_REVIEW",
            "result": result,
            "review": None,
            "terminal": False,
        }

    pending = _review_followup_gate(result, review, root)
    if pending is not None:
        return pending

    followup = _driver_followup.state_for_review(review["review_id"], root)
    disposition = review.get("disposition")
    return {
        "state": (
            "TERMINAL"
            if disposition in TERMINAL_DISPOSITIONS
            else "RETURN_TO_EXECUTION"
        ),
        "result": result,
        "review": review,
        "terminal": disposition in TERMINAL_DISPOSITIONS,
        "driver_followup_state": followup.get("state"),
        "driver_followup": followup.get("packet"),
    }


def _parallel_synthesis(
    intake_id: str, evidence_set_sha256: str, root: Path
) -> dict[str, Any] | None:
    for item in _parallel.syntheses(root).values():
        if (
            item.get("intake_id") == intake_id
            and item.get("evidence_set_sha256") == evidence_set_sha256
        ):
            return item
    return None


def _parallel_followup_pending(
    result_ids: list[str], root: Path
) -> list[dict[str, Any]]:
    """Return governed reviewed results whose review->taskset barrier is incomplete."""
    by_result = {item.get("result_id"): item for item in iter_results(root)}
    pending: list[dict[str, Any]] = []
    for result_id_value in result_ids:
        result = by_result.get(result_id_value)
        if not isinstance(result, dict):
            continue
        review = latest_review(result_id_value, root)
        if review is None:
            continue
        review_id = review.get("review_id")
        if not isinstance(review_id, str) or not review_id:
            pending.append(
                {
                    "result_id": result_id_value,
                    "review_id": None,
                    "state": "REVIEW_ID_UNAVAILABLE",
                }
            )
            continue
        followup = _driver_followup.state_for_review(review_id, root)
        if followup.get("required") is True and followup.get("ready") is not True:
            pending.append(
                {
                    "result_id": result_id_value,
                    "review_id": review_id,
                    "state": followup.get("state"),
                    "error": followup.get("error"),
                }
            )
    return pending


def task_result_state(
    task_id: str,
    root: Path = ROOT,
    publication_id: str | None = None,
) -> dict[str, Any] | None:
    """Return one control state without discarding parallel research evidence.

    Single-result tasks retain generation-aware behavior except that governed
    Driver reviews remain nonterminal until their automatic follow-up taskset (or
    canonical parent-closure exception) is materialized. Parallel terminal
    synthesis inherits the same barrier for each governed reviewed result.
    """
    resolved_publication = _publication_for_state(task_id, root, publication_id)
    parallel = _parallel.state(task_id, resolved_publication, root)
    phase = parallel.get("parallel_state")
    if phase == "SINGLE_RESULT_FLOW":
        return _single_result_state(task_id, root, resolved_publication)

    result_ids = list(parallel.get("result_ids") or [])
    intake_id = parallel.get("intake_id")
    evidence_hash = parallel.get("evidence_set_sha256")
    synthetic_result = {
        "result_id": intake_id or f"PARALLEL-{task_id}",
        "task_id": task_id,
        "publication_id": resolved_publication,
        "parallel_result_ids": result_ids,
        "_record_path": None,
    }

    if phase in {
        "AWAITING_PARALLEL_INTAKE",
        "AWAITING_REFERENCE_PASS_1",
        "AWAITING_REFERENCE_PASS_2",
        "AWAITING_SYNTHESIS",
    }:
        return {
            "state": "AWAITING_DRIVER_REVIEW",
            "result": synthetic_result,
            "review": None,
            "terminal": False,
            "parallel_state": phase,
            "parallel_result_ids": result_ids,
            "parallel_intake_id": intake_id,
            "evidence_set_sha256": evidence_hash,
        }

    synthesis = (
        _parallel_synthesis(str(intake_id), str(evidence_hash), root)
        if intake_id and evidence_hash
        else None
    )
    if synthesis is None:
        return {
            "state": "AWAITING_DRIVER_REVIEW",
            "result": synthetic_result,
            "review": None,
            "terminal": False,
            "parallel_state": "AWAITING_SYNTHESIS",
            "parallel_result_ids": result_ids,
            "parallel_intake_id": intake_id,
            "evidence_set_sha256": evidence_hash,
        }

    synth_result = {
        **synthetic_result,
        "result_id": synthesis.get("synthesis_id"),
        "_record_path": synthesis.get("_path"),
    }
    if phase == "PARALLEL_SYNTHESIS_NONTERMINAL":
        return {
            "state": "RETURN_TO_EXECUTION",
            "result": synth_result,
            "review": {
                "review_id": synthesis.get("synthesis_id"),
                "disposition": synthesis.get("disposition"),
            },
            "terminal": False,
            "parallel_state": phase,
            "parallel_result_ids": result_ids,
            "parallel_intake_id": intake_id,
            "evidence_set_sha256": evidence_hash,
        }

    if phase == "PARALLEL_SYNTHESIS_TERMINAL":
        disposition = synthesis.get("terminal_control_disposition")
        if disposition not in TERMINAL_DISPOSITIONS:
            return {
                "state": "AWAITING_DRIVER_REVIEW",
                "result": synth_result,
                "review": None,
                "terminal": False,
                "parallel_state": "TERMINAL_SYNTHESIS_MISSING_CONTROL_DISPOSITION",
                "parallel_result_ids": result_ids,
                "parallel_intake_id": intake_id,
                "evidence_set_sha256": evidence_hash,
            }

        followup_pending = _parallel_followup_pending(result_ids, root)
        if followup_pending:
            return {
                "state": "AWAITING_DRIVER_REVIEW",
                "result": synth_result,
                "review": {
                    "review_id": synthesis.get("synthesis_id"),
                    "disposition": disposition,
                },
                "terminal": False,
                "parallel_state": "TERMINAL_SYNTHESIS_AWAITING_DRIVER_FOLLOWUP",
                "parallel_result_ids": result_ids,
                "parallel_intake_id": intake_id,
                "evidence_set_sha256": evidence_hash,
                "driver_followup_pending": followup_pending,
            }

        return {
            "state": "TERMINAL",
            "result": synth_result,
            "review": {
                "review_id": synthesis.get("synthesis_id"),
                "disposition": disposition,
            },
            "terminal": True,
            "parallel_state": phase,
            "parallel_result_ids": result_ids,
            "parallel_intake_id": intake_id,
            "evidence_set_sha256": evidence_hash,
        }

    raise ResultRecordError(f"unknown parallel result state: {phase}")


if __name__ == "__main__":
    try:
        raise SystemExit(_impl.main())
    except ResultRecordError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
