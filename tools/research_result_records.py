#!/usr/bin/env python3
"""Canonical result registry with parallel-evidence and quarantine reduction.

The durable V1 writer/auditor lives in ``control_plane.research_result_records_impl``.
This shim preserves that writer while adding two control-only compatibility layers:
parallel-result synthesis and an explicit quarantine registry for immutable historical
records that cannot satisfy the current V1 schema. Quarantine never rewrites bytes;
it only removes named records/reviews from operational truth after validating that a
replacement result exists.
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

# Preserve the historical public/module surface, including compatibility helpers
# used by tests and downstream control-plane code.
for _name in dir(_impl):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_impl, _name)

if str(_impl.ROOT) not in sys.path:
    sys.path.insert(0, str(_impl.ROOT))
import research_parallel_evidence as _parallel  # noqa: E402

ROOT = _impl.ROOT
QUARANTINE_FILE = "research_result_record_quarantines.json"
QUARANTINE_SCHEMA = "ENTERPRISE_MATH_RESEARCH_RESULT_QUARANTINE_V1"
_RAW_ITER_RESULTS = _impl.iter_results
_RAW_ITER_REVIEWS = _impl.iter_reviews
_RAW_AUDIT = _impl.audit


def _quarantine_entries(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    path = root / QUARANTINE_FILE
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema") != QUARANTINE_SCHEMA:
        raise ResultRecordError(f"{QUARANTINE_FILE}: wrong schema")
    if payload.get("status") != "ACTIVE":
        raise ResultRecordError(f"{QUARANTINE_FILE}: status must be ACTIVE")
    rows = payload.get("entries")
    if not isinstance(rows, list):
        raise ResultRecordError(f"{QUARANTINE_FILE}: entries must be a list")
    out: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ResultRecordError(f"{QUARANTINE_FILE}: entry {index} must be an object")
        rid = row.get("result_id")
        if not isinstance(rid, str) or not rid:
            raise ResultRecordError(f"{QUARANTINE_FILE}: entry {index} missing result_id")
        if rid in out:
            raise ResultRecordError(f"{QUARANTINE_FILE}: duplicate result_id {rid}")
        if row.get("resolution") != "QUARANTINE_INVALID_RECORD":
            raise ResultRecordError(f"{QUARANTINE_FILE}: {rid} unsupported resolution")
        if row.get("operational") is not False or row.get("history_preserved") is not True:
            raise ResultRecordError(f"{QUARANTINE_FILE}: {rid} must preserve history and be nonoperational")
        corrected = row.get("corrected_result_id")
        if not isinstance(corrected, str) or not corrected:
            raise ResultRecordError(f"{QUARANTINE_FILE}: {rid} missing corrected_result_id")
        reason = row.get("reason")
        if not isinstance(reason, list) or not reason or any(not isinstance(x, str) or not x.strip() for x in reason):
            raise ResultRecordError(f"{QUARANTINE_FILE}: {rid} reason must be a nonempty string list")
        out[rid] = row
    return out


def iter_results(root: Path = ROOT) -> list[dict[str, Any]]:
    quarantined = set(_quarantine_entries(root))
    return [item for item in _RAW_ITER_RESULTS(root) if item.get("result_id") not in quarantined]


def iter_reviews(root: Path = ROOT) -> list[dict[str, Any]]:
    quarantined = set(_quarantine_entries(root))
    return [item for item in _RAW_ITER_REVIEWS(root) if item.get("result_id") not in quarantined]


def _parallel_results(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    return {
        str(item["result_id"]): item
        for item in iter_results(root)
        if isinstance(item.get("result_id"), str) and item.get("result_id")
    }


def _parallel_reviews(root: Path = ROOT) -> dict[str, list[dict[str, Any]]]:
    out: dict[str, list[dict[str, Any]]] = {}
    for item in iter_reviews(root):
        rid = item.get("result_id")
        if isinstance(rid, str) and rid:
            out.setdefault(rid, []).append(item)
    return out


# Every durable result/review lookup and the parallel reducer sees only active
# records. Historical quarantined bytes remain available through raw repository
# paths and are validated separately below.
_impl.iter_results = iter_results
_impl.iter_reviews = iter_reviews
_parallel.results = _parallel_results
_parallel.result_reviews = _parallel_reviews


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
    """Return one control state without discarding valid parallel evidence."""
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

    synth_result = {**synthetic_result, "result_id": synthesis.get("synthesis_id"), "_record_path": synthesis.get("_path")}
    if phase == "PARALLEL_SYNTHESIS_NONTERMINAL":
        return {
            "state": "RETURN_TO_EXECUTION",
            "result": synth_result,
            "review": {"review_id": synthesis.get("synthesis_id"), "disposition": synthesis.get("disposition")},
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
            "review": {"review_id": synthesis.get("synthesis_id"), "disposition": disposition},
            "terminal": True,
            "parallel_state": phase,
            "parallel_result_ids": result_ids,
            "parallel_intake_id": intake_id,
            "evidence_set_sha256": evidence_hash,
        }
    raise ResultRecordError(f"unknown parallel result state: {phase}")


def audit(root: Path = ROOT) -> list[str]:
    """Strictly audit active V1 records and validate every quarantine mapping."""
    try:
        quarantine = _quarantine_entries(root)
    except Exception as exc:
        return [str(exc)]

    raw_results = {
        str(item.get("result_id")): item
        for item in _RAW_ITER_RESULTS(root)
        if isinstance(item.get("result_id"), str)
    }
    active_results = {
        str(item.get("result_id")): item
        for item in iter_results(root)
        if isinstance(item.get("result_id"), str)
    }
    errors: list[str] = []
    for rid, row in quarantine.items():
        historical = raw_results.get(rid)
        corrected = active_results.get(str(row.get("corrected_result_id")))
        if historical is None:
            errors.append(f"{QUARANTINE_FILE}: unknown historical result {rid}")
            continue
        if corrected is None:
            errors.append(f"{QUARANTINE_FILE}: {rid} corrected result is unavailable")
            continue
        for field in ("task_id", "publication_id"):
            expected = row.get(field)
            if expected != historical.get(field) or expected != corrected.get(field):
                errors.append(f"{QUARANTINE_FILE}: {rid} {field} mismatch across quarantine/replacement")
        record_path = row.get("record_path")
        if record_path != historical.get("_record_path"):
            errors.append(f"{QUARANTINE_FILE}: {rid} historical record_path mismatch")

    # _RAW_AUDIT resolves its module-global iterators at call time, which above
    # are patched to active-only views. Therefore all nonquarantined V1 records
    # remain subject to the original strict durable auditor.
    return _RAW_AUDIT(root) + errors


_impl.audit = audit


if __name__ == "__main__":
    try:
        raise SystemExit(_impl.main())
    except ResultRecordError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
