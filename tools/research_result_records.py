#!/usr/bin/env python3
"""Canonical result-registry shim with publication-generation and parallel-evidence state reduction.

The durable record writer/auditor lives in ``control_plane.research_result_records_impl``.
This shim preserves its API while replacing only task-level result-state reduction:
multiple results are retained and routed through the two-pass parallel-evidence
synthesis layer instead of timestamp/latest-result semantics.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from control_plane import research_result_records_impl as _impl  # noqa: E402

# Preserve the complete historical public/module surface, including compatibility
# helpers used by tests and downstream control-plane code.
for _name in dir(_impl):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_impl, _name)

if str(_impl.ROOT) not in sys.path:
    sys.path.insert(0, str(_impl.ROOT))
import research_parallel_evidence as _parallel  # noqa: E402

ROOT = _impl.ROOT


def _publication_for_state(task_id: str, root: Path, publication_id: str | None) -> str | None:
    if publication_id is not None:
        return publication_id
    try:
        current = research_task_records.current_records(root).get(task_id)
    except Exception:
        current = None
    if isinstance(current, dict) and isinstance(current.get("publication_id"), str):
        return current["publication_id"]
    return None


def _single_result_state(
    task_id: str,
    root: Path,
    publication_id: str | None,
) -> dict[str, Any] | None:
    """Reduce one publication generation through the public result-registry API.

    Keeping the reduction on this module boundary preserves compatibility with
    callers/tests that intentionally replace ``iter_results`` or ``latest_review``
    while retaining the exact generation-aware semantics of the implementation.
    """
    values = [
        item
        for item in iter_results(root)
        if item.get("task_id") == task_id
        and (publication_id is None or item.get("publication_id") == publication_id)
    ]
    if not values:
        return None
    values.sort(key=lambda item: (item.get("frozen_at", ""), item.get("result_id", "")))
    result = values[-1]
    review = latest_review(result["result_id"], root)
    if review is None:
        return {"state": "AWAITING_DRIVER_REVIEW", "result": result, "review": None, "terminal": False}
    disposition = review.get("disposition")
    return {
        "state": "TERMINAL" if disposition in TERMINAL_DISPOSITIONS else "RETURN_TO_EXECUTION",
        "result": result,
        "review": review,
        "terminal": disposition in TERMINAL_DISPOSITIONS,
    }


def _parallel_synthesis(intake_id: str, evidence_set_sha256: str, root: Path) -> dict[str, Any] | None:
    for item in _parallel.syntheses(root).values():
        if item.get("intake_id") == intake_id and item.get("evidence_set_sha256") == evidence_set_sha256:
            return item
    return None


def task_result_state(
    task_id: str,
    root: Path = ROOT,
    publication_id: str | None = None,
) -> dict[str, Any] | None:
    """Return one control state without discarding parallel research evidence.

    Single-result tasks retain the generation-aware historical behavior. Two or
    more results for the same selected publication never use timestamp precedence;
    they remain non-dispatchable until intake -> reference pass 1 -> reference
    pass 2 -> synthesis completes.
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
