#!/usr/bin/env python3
"""Canonical result-registry shim with publication-generation and parallel-evidence state reduction.

The durable record writer/auditor lives in ``control_plane.research_result_records_impl``.
This shim preserves its API while replacing task-level result-state reduction:
multiple valid results are routed through the two-pass parallel-evidence synthesis
layer instead of timestamp/latest-result semantics. A small explicit quarantine
overlay can retain a structurally invalid immutable result in history while
removing it from operational truth and returning the task to Driver-directed
execution.
"""
from __future__ import annotations

import json
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
QUARANTINE = "research_result_record_quarantines.json"
_ORIGINAL_IMPL_AUDIT = _impl.audit


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


def _quarantine_map(root: Path) -> dict[str, dict[str, Any]]:
    path = root / QUARANTINE
    if not path.exists():
        return {}
    value = json.loads(path.read_text(encoding="utf-8"))
    if value.get("schema") != "ENTERPRISE_MATH_RESEARCH_RESULT_QUARANTINE_V1":
        raise ResultRecordError("unexpected research-result quarantine schema")
    if value.get("status") != "ACTIVE":
        raise ResultRecordError("research-result quarantine registry must be ACTIVE")
    entries = value.get("entries")
    if not isinstance(entries, list):
        raise ResultRecordError("research-result quarantine entries must be a list")
    out: dict[str, dict[str, Any]] = {}
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            raise ResultRecordError(f"quarantine entries[{index}] must be an object")
        rid = entry.get("result_id")
        if not isinstance(rid, str) or not rid:
            raise ResultRecordError(f"quarantine entries[{index}] missing result_id")
        if rid in out:
            raise ResultRecordError(f"duplicate quarantined result_id: {rid}")
        out[rid] = entry
    return out


def _quarantine_state(
    task_id: str,
    root: Path,
    publication_id: str | None,
) -> dict[str, Any] | None:
    qmap = _quarantine_map(root)
    if not qmap:
        return None
    values = [
        item
        for item in iter_results(root)
        if item.get("task_id") == task_id
        and (publication_id is None or item.get("publication_id") == publication_id)
    ]
    quarantined = [item for item in values if item.get("result_id") in qmap]
    if not quarantined:
        return None
    active = [item for item in values if item.get("result_id") not in qmap]
    if len(active) == 1:
        result = active[0]
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
    if len(active) > 1:
        raise ResultRecordError(
            f"{task_id}: multiple active results coexist with quarantined history; explicit parallel migration required"
        )
    quarantined.sort(key=lambda item: (item.get("frozen_at", ""), item.get("result_id", "")))
    result = quarantined[-1]
    entry = qmap[result["result_id"]]
    return {
        "state": "RETURN_TO_EXECUTION",
        "result": result,
        "review": {
            "review_id": entry.get("resolution_id"),
            "disposition": entry.get("driver_disposition"),
            "review_path": entry.get("review_path"),
            "quarantine_resolution": True,
        },
        "terminal": False,
        "quarantined_result": True,
        "quarantine_resolution_id": entry.get("resolution_id"),
    }


def task_result_state(
    task_id: str,
    root: Path = ROOT,
    publication_id: str | None = None,
) -> dict[str, Any] | None:
    """Return one control state without discarding parallel research evidence.

    Single-result tasks retain the generation-aware historical behavior. Explicitly
    quarantined invalid result records remain immutable evidence but are excluded
    from operational truth; their resolution returns the task to execution. Two or
    more valid results for the same selected publication never use timestamp
    precedence and remain non-dispatchable until two-pass synthesis completes.
    """
    resolved_publication = _publication_for_state(task_id, root, publication_id)
    quarantined = _quarantine_state(task_id, root, resolved_publication)
    if quarantined is not None:
        return quarantined

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


def audit(root: Path = ROOT) -> list[str]:
    """Audit ordinary records strictly while preserving explicit quarantined history.

    A quarantine is an append-only control resolution, not a rewrite. Structural
    errors emitted by the durable V1 auditor are suppressed only for the exact
    immutable record path named by a validated quarantine entry. Everything else
    remains strict.
    """
    try:
        qmap = _quarantine_map(root)
    except Exception as exc:
        return [str(exc)]
    raw_errors = _ORIGINAL_IMPL_AUDIT(root)
    if not qmap:
        return raw_errors

    results = {str(item.get("result_id")): item for item in _impl.iter_results(root)}
    quarantine_paths: set[str] = set()
    errors: list[str] = []
    seen_resolution_ids: set[str] = set()
    for rid, entry in qmap.items():
        result = results.get(rid)
        if result is None:
            errors.append(f"{QUARANTINE}: unknown quarantined result {rid}")
            continue
        path = result.get("_record_path")
        if not isinstance(path, str) or not path:
            errors.append(f"{QUARANTINE}: quarantined result {rid} has no record path")
            continue
        quarantine_paths.add(path)
        if entry.get("record_path") != path:
            errors.append(f"{QUARANTINE}: {rid} record_path mismatch")
        for field in ("task_id", "publication_id"):
            if entry.get(field) != result.get(field):
                errors.append(f"{QUARANTINE}: {rid} {field} mismatch")
        resolution_id = entry.get("resolution_id")
        if not isinstance(resolution_id, str) or not resolution_id:
            errors.append(f"{QUARANTINE}: {rid} missing resolution_id")
        elif resolution_id in seen_resolution_ids:
            errors.append(f"{QUARANTINE}: duplicate resolution_id {resolution_id}")
        seen_resolution_ids.add(str(resolution_id))
        if entry.get("resolution") != "QUARANTINE_INVALID_RECORD":
            errors.append(f"{QUARANTINE}: {rid} has unsupported resolution")
        if entry.get("operational") is not False or entry.get("history_preserved") is not True:
            errors.append(f"{QUARANTINE}: {rid} must be nonoperational with history preserved")
        disposition = entry.get("driver_disposition")
        if disposition not in NONTERMINAL_DISPOSITIONS:
            errors.append(f"{QUARANTINE}: {rid} requires nonterminal Driver disposition")
        driver_id = entry.get("driver_id")
        if not research_identity.valid_execution_id(str(driver_id or "")):
            errors.append(f"{QUARANTINE}: {rid} has invalid driver_id")
        reason = entry.get("reason")
        if not isinstance(reason, list) or not reason or any(not isinstance(x, str) or not x.strip() for x in reason):
            errors.append(f"{QUARANTINE}: {rid} reason must be a nonempty string list")
        review_path = entry.get("review_path")
        if not isinstance(review_path, str) or not review_path or not (root / review_path).exists():
            errors.append(f"{QUARANTINE}: {rid} Driver review artifact missing")

    filtered = [
        error
        for error in raw_errors
        if not any(error.startswith(path + ":") for path in quarantine_paths)
    ]
    return filtered + errors


# Freeze/review commands in the durable implementation invoke its module-global
# ``audit``. Patch that reference so future valid successor results can be frozen
# without forcing deletion or mutation of quarantined historical records.
_impl.audit = audit


if __name__ == "__main__":
    try:
        raise SystemExit(_impl.main())
    except ResultRecordError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
