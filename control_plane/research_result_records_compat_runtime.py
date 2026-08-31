#!/usr/bin/env python3
"""Canonical result registry with parallel evidence and exact history compatibility.

The durable V1 writer/auditor remains in ``control_plane.research_result_records_impl``.
This facade adds only control-layer views that are impossible to express by rewriting
immutable evidence:

1. exact record-blob-pinned metadata normalization for historical enum spellings;
2. secondary SHA-256 repair only when the primary frozen Git-blob identity still matches;
3. exact quarantine of structurally invalid historical records after a writer-conformant
   same-task/same-publication replacement exists;
4. parallel-result synthesis without timestamp/latest-result authority.

No historical result/review/taskbook bytes are rewritten, deleted, or truth-ranked.
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from control_plane import research_result_records_impl as _impl  # noqa: E402

# Preserve the complete historical public/module surface.
for _name in dir(_impl):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_impl, _name)

if str(_impl.ROOT) not in sys.path:
    sys.path.insert(0, str(_impl.ROOT))
import research_parallel_evidence as _parallel  # noqa: E402

ROOT = _impl.ROOT
COMPATIBILITY_FILE = "research_result_record_compatibility.json"
COMPATIBILITY_SCHEMA = "ENTERPRISE_MATH_RESEARCH_RESULT_COMPATIBILITY_V1"
QUARANTINE_FILE = "research_result_record_quarantines.json"
QUARANTINE_SCHEMA = "ENTERPRISE_MATH_RESEARCH_RESULT_QUARANTINE_V1"

# Pin the raw implementation functions exactly once. Historical CLI entrypoints
# can import this file as both tools.research_result_records and bare
# research_result_records; duplicate imports must never wrap an already-filtered view.
for _sentinel, _value in (
    ("_history_original_iter_results", _impl.iter_results),
    ("_history_original_iter_reviews", _impl.iter_reviews),
    ("_history_original_audit", _impl.audit),
):
    if _sentinel not in _impl.__dict__:
        _impl.__dict__[_sentinel] = _value
_RAW_ITER_RESULTS = _impl.__dict__["_history_original_iter_results"]
_RAW_ITER_REVIEWS = _impl.__dict__["_history_original_iter_reviews"]
_RAW_AUDIT = _impl.__dict__["_history_original_audit"]

_RESULT_ALIAS_TARGETS = {
    "terminal_verdict": _impl.TERMINAL_VERDICTS,
    "method_harvest": _impl.METHOD_HARVEST,
    "independence_status": _impl.INDEPENDENCE_STATUS,
    "source_exposure_status": _impl.SOURCE_EXPOSURE_STATUS,
}
_REVIEW_ALIAS_TARGETS = {
    "disposition": _impl.ALL_DISPOSITIONS,
    "destination_class": _impl.DESTINATION_CLASSES,
}
_AUTHORITY_FLAGS = (
    "working_truth_granted",
    "foundation_authority_granted",
    "canonical_promotion_granted",
    "successor_triggered",
)


def _load_object(path: Path, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ResultRecordError(f"{label}: cannot load JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ResultRecordError(f"{label}: JSON root must be an object")
    return value


def _authority_free(payload: dict[str, Any], label: str) -> None:
    for field in _AUTHORITY_FLAGS:
        if field in payload and payload.get(field) is not False:
            raise ResultRecordError(f"{label}: compatibility cannot grant {field}")


def _compatibility_payload(root: Path = ROOT) -> dict[str, Any]:
    path = root / COMPATIBILITY_FILE
    if not path.exists():
        return {
            "schema": COMPATIBILITY_SCHEMA,
            "status": "ACTIVE",
            "result_normalizations": [],
            "review_normalizations": [],
        }
    value = _load_object(path, COMPATIBILITY_FILE)
    if value.get("schema") != COMPATIBILITY_SCHEMA:
        raise ResultRecordError(f"{COMPATIBILITY_FILE}: wrong schema")
    if value.get("status") != "ACTIVE":
        raise ResultRecordError(f"{COMPATIBILITY_FILE}: status must be ACTIVE")
    _authority_free(value, COMPATIBILITY_FILE)
    for key in ("result_normalizations", "review_normalizations"):
        if not isinstance(value.get(key), list):
            raise ResultRecordError(f"{COMPATIBILITY_FILE}: {key} must be a list")
    return value


def _quarantine_payload(root: Path = ROOT) -> dict[str, Any]:
    path = root / QUARANTINE_FILE
    if not path.exists():
        return {"schema": QUARANTINE_SCHEMA, "status": "ACTIVE", "entries": []}
    value = _load_object(path, QUARANTINE_FILE)
    if value.get("schema") != QUARANTINE_SCHEMA:
        raise ResultRecordError(f"{QUARANTINE_FILE}: wrong schema")
    if value.get("status") != "ACTIVE":
        raise ResultRecordError(f"{QUARANTINE_FILE}: status must be ACTIVE")
    entries = value.get("entries")
    if not isinstance(entries, list):
        raise ResultRecordError(f"{QUARANTINE_FILE}: entries must be a list")
    return value


def _unique_entries(rows: list[Any], id_field: str, label: str) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ResultRecordError(f"{label}: entry {index} must be an object")
        value = row.get(id_field)
        if not isinstance(value, str) or not value:
            raise ResultRecordError(f"{label}: entry {index} missing {id_field}")
        if value in out:
            raise ResultRecordError(f"{label}: duplicate {id_field} {value}")
        out[value] = row
    return out


def _record_blob_guard(
    item: dict[str, Any],
    row: dict[str, Any],
    *,
    path_field: str,
    id_label: str,
    root: Path,
) -> None:
    expected_path = row.get("record_path")
    actual_path = item.get(path_field)
    if not isinstance(expected_path, str) or expected_path != actual_path:
        raise ResultRecordError(f"{COMPATIBILITY_FILE}: {id_label}: record_path mismatch")
    pin = row.get("record_blob_sha1")
    if not isinstance(pin, str) or not pin:
        raise ResultRecordError(f"{COMPATIBILITY_FILE}: {id_label}: missing record_blob_sha1")
    path = root / expected_path
    if not path.exists():
        raise ResultRecordError(f"{COMPATIBILITY_FILE}: {id_label}: record path missing")
    if not _impl._same_git_blob_identity(_impl._blob(path), pin):
        raise ResultRecordError(f"{COMPATIBILITY_FILE}: {id_label}: immutable record blob drift")


def _apply_aliases(
    item: dict[str, Any],
    aliases: Any,
    *,
    allowed: dict[str, set[str]],
    id_label: str,
) -> None:
    if not isinstance(aliases, list):
        raise ResultRecordError(f"{COMPATIBILITY_FILE}: {id_label}: field_aliases must be a list")
    seen: set[str] = set()
    for alias in aliases:
        if not isinstance(alias, dict):
            raise ResultRecordError(f"{COMPATIBILITY_FILE}: {id_label}: invalid field alias")
        field = alias.get("field")
        before = alias.get("from")
        after = alias.get("to")
        if field not in allowed:
            raise ResultRecordError(f"{COMPATIBILITY_FILE}: {id_label}: unsupported alias field {field!r}")
        if field in seen:
            raise ResultRecordError(f"{COMPATIBILITY_FILE}: {id_label}: duplicate alias field {field}")
        if not isinstance(before, str) or not isinstance(after, str) or after not in allowed[field]:
            raise ResultRecordError(f"{COMPATIBILITY_FILE}: {id_label}: invalid alias target for {field}")
        if item.get(field) != before:
            raise ResultRecordError(
                f"{COMPATIBILITY_FILE}: {id_label}: stale alias for {field}; expected raw {before!r}, got {item.get(field)!r}"
            )
        item[field] = after
        seen.add(field)


def _repair_result_return_artifact(
    item: dict[str, Any], rel: Any, *, id_label: str, root: Path
) -> None:
    if rel is None:
        return
    if not isinstance(rel, str) or not rel:
        raise ResultRecordError(
            f"{COMPATIBILITY_FILE}: {id_label}: return_artifact_from_manifest must be a path"
        )
    if item.get("return_path") is not None or item.get("return_blob_sha1") is not None:
        raise ResultRecordError(
            f"{COMPATIBILITY_FILE}: {id_label}: return artifact repair is stale"
        )
    candidate = Path(rel)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise ResultRecordError(
            f"{COMPATIBILITY_FILE}: {id_label}: unsafe return artifact path"
        )
    rows = item.get("output_manifest")
    matches = [
        row
        for row in rows if isinstance(row, dict) and row.get("path") == rel
    ] if isinstance(rows, list) else []
    if len(matches) != 1:
        raise ResultRecordError(
            f"{COMPATIBILITY_FILE}: {id_label}: return artifact is not uniquely pinned by manifest"
        )
    path = root / candidate
    if not path.is_file():
        raise ResultRecordError(
            f"{COMPATIBILITY_FILE}: {id_label}: return artifact missing"
        )
    pin = matches[0].get("git_blob_sha1")
    if not _impl._same_git_blob_identity(_impl._blob(path), pin):
        raise ResultRecordError(
            f"{COMPATIBILITY_FILE}: {id_label}: return artifact Git blob drift"
        )
    item["return_path"] = rel
    item["return_blob_sha1"] = pin


def _repair_result_sha256(item: dict[str, Any], paths: Any, *, id_label: str, root: Path) -> None:
    if not isinstance(paths, list) or any(not isinstance(x, str) or not x for x in paths):
        raise ResultRecordError(
            f"{COMPATIBILITY_FILE}: {id_label}: artifact_sha256_repairs must be a string list"
        )
    if len(paths) != len(set(paths)):
        raise ResultRecordError(f"{COMPATIBILITY_FILE}: {id_label}: duplicate SHA repair path")
    manifest = item.get("output_manifest")
    rows = manifest if isinstance(manifest, list) else []
    for rel in paths:
        matches = [row for row in rows if isinstance(row, dict) and row.get("path") == rel]
        top_match = item.get("return_path") == rel
        if not top_match and len(matches) != 1:
            raise ResultRecordError(
                f"{COMPATIBILITY_FILE}: {id_label}: SHA repair path is not uniquely pinned by result: {rel}"
            )
        path = root / rel
        if not path.exists():
            raise ResultRecordError(f"{COMPATIBILITY_FILE}: {id_label}: repair artifact missing: {rel}")
        actual_blob = _impl._blob(path)
        if top_match:
            pin = item.get("return_blob_sha1")
            if not _impl._same_git_blob_identity(actual_blob, pin):
                raise ResultRecordError(
                    f"{COMPATIBILITY_FILE}: {id_label}: primary Git blob drift forbids SHA repair: {rel}"
                )
            item["return_sha256"] = _impl._sha256(path)
        for row in matches:
            pin = row.get("git_blob_sha1")
            if not _impl._same_git_blob_identity(actual_blob, pin):
                raise ResultRecordError(
                    f"{COMPATIBILITY_FILE}: {id_label}: primary manifest Git blob drift forbids SHA repair: {rel}"
                )
            row["sha256"] = _impl._sha256(path)


def _repair_review_sha256(item: dict[str, Any], paths: Any, *, id_label: str, root: Path) -> None:
    if not isinstance(paths, list) or any(not isinstance(x, str) or not x for x in paths):
        raise ResultRecordError(
            f"{COMPATIBILITY_FILE}: {id_label}: artifact_sha256_repairs must be a string list"
        )
    if len(paths) != len(set(paths)):
        raise ResultRecordError(f"{COMPATIBILITY_FILE}: {id_label}: duplicate SHA repair path")
    for rel in paths:
        if item.get("review_path") != rel:
            raise ResultRecordError(
                f"{COMPATIBILITY_FILE}: {id_label}: review SHA repair must target its exact review_path"
            )
        path = root / rel
        if not path.exists():
            raise ResultRecordError(f"{COMPATIBILITY_FILE}: {id_label}: review artifact missing")
        actual_blob = _impl._blob(path)
        if not _impl._same_git_blob_identity(actual_blob, item.get("review_blob_sha1")):
            raise ResultRecordError(
                f"{COMPATIBILITY_FILE}: {id_label}: primary review Git blob drift forbids SHA repair"
            )
        item["review_sha256"] = _impl._sha256(path)


def _normalize_result_item(item: dict[str, Any], row: dict[str, Any], root: Path) -> dict[str, Any]:
    value = copy.deepcopy(item)
    rid = str(item.get("result_id"))
    _record_blob_guard(value, row, path_field="_record_path", id_label=rid, root=root)
    _apply_aliases(
        value,
        row.get("field_aliases"),
        allowed=_RESULT_ALIAS_TARGETS,
        id_label=rid,
    )
    _repair_result_return_artifact(
        value,
        row.get("return_artifact_from_manifest"),
        id_label=rid,
        root=root,
    )
    _repair_result_sha256(
        value,
        row.get("artifact_sha256_repairs"),
        id_label=rid,
        root=root,
    )
    if not isinstance(row.get("reason"), str) or not row["reason"].strip():
        raise ResultRecordError(f"{COMPATIBILITY_FILE}: {rid}: reason is required")
    return value


def _normalize_review_item(item: dict[str, Any], row: dict[str, Any], root: Path) -> dict[str, Any]:
    value = copy.deepcopy(item)
    review_id_value = str(item.get("review_id"))
    _record_blob_guard(value, row, path_field="_review_path", id_label=review_id_value, root=root)
    _apply_aliases(
        value,
        row.get("field_aliases"),
        allowed=_REVIEW_ALIAS_TARGETS,
        id_label=review_id_value,
    )
    _repair_review_sha256(
        value,
        row.get("artifact_sha256_repairs"),
        id_label=review_id_value,
        root=root,
    )
    if not isinstance(row.get("reason"), str) or not row["reason"].strip():
        raise ResultRecordError(f"{COMPATIBILITY_FILE}: {review_id_value}: reason is required")
    return value


def _quarantine_entries(
    raw_results: dict[str, dict[str, Any]], root: Path = ROOT
) -> dict[str, dict[str, Any]]:
    payload = _quarantine_payload(root)
    rows = _unique_entries(payload["entries"], "result_id", QUARANTINE_FILE)
    for rid, row in rows.items():
        _authority_free(row, f"{QUARANTINE_FILE}: {rid}")
        if row.get("resolution") != "QUARANTINE_INVALID_RECORD":
            raise ResultRecordError(f"{QUARANTINE_FILE}: {rid}: unsupported resolution")
        if row.get("operational") is not False or row.get("history_preserved") is not True:
            raise ResultRecordError(f"{QUARANTINE_FILE}: {rid}: must preserve history and be nonoperational")
        historical = raw_results.get(rid)
        if historical is None:
            raise ResultRecordError(f"{QUARANTINE_FILE}: {rid}: historical result missing")
        record_path = row.get("record_path")
        if historical.get("_record_path") != record_path or not isinstance(record_path, str):
            raise ResultRecordError(f"{QUARANTINE_FILE}: {rid}: record_path mismatch")
        path = root / record_path
        pin = row.get("record_blob_sha1")
        if not isinstance(pin, str) or not _impl._same_git_blob_identity(_impl._blob(path), pin):
            raise ResultRecordError(f"{QUARANTINE_FILE}: {rid}: immutable historical record blob drift")
        corrected_id = row.get("corrected_result_id")
        if not isinstance(corrected_id, str) or corrected_id == rid or corrected_id in rows:
            raise ResultRecordError(f"{QUARANTINE_FILE}: {rid}: invalid corrected_result_id")
        corrected = raw_results.get(corrected_id)
        if corrected is None:
            raise ResultRecordError(f"{QUARANTINE_FILE}: {rid}: corrected result is unavailable")
        for field in ("task_id", "publication_id"):
            expected = row.get(field)
            if expected != historical.get(field) or expected != corrected.get(field):
                raise ResultRecordError(
                    f"{QUARANTINE_FILE}: {rid}: {field} mismatch across historical/replacement"
                )
        reason = row.get("reason")
        if not isinstance(reason, list) or not reason or any(not isinstance(x, str) or not x.strip() for x in reason):
            raise ResultRecordError(f"{QUARANTINE_FILE}: {rid}: reason must be a nonempty string list")
    return rows


def iter_results(root: Path = ROOT) -> list[dict[str, Any]]:
    raw = _RAW_ITER_RESULTS(root)
    raw_map = {
        str(item.get("result_id")): item
        for item in raw
        if isinstance(item.get("result_id"), str) and item.get("result_id")
    }
    quarantine = _quarantine_entries(raw_map, root)
    payload = _compatibility_payload(root)
    normalizations = _unique_entries(
        payload["result_normalizations"], "result_id", f"{COMPATIBILITY_FILE}: result_normalizations"
    )
    missing = set(normalizations) - set(raw_map)
    if missing:
        raise ResultRecordError(
            f"{COMPATIBILITY_FILE}: stale result normalization(s): {sorted(missing)!r}"
        )
    overlap = set(normalizations) & set(quarantine)
    if overlap:
        raise ResultRecordError(
            f"{COMPATIBILITY_FILE}: result cannot be both normalized and quarantined: {sorted(overlap)!r}"
        )
    out: list[dict[str, Any]] = []
    for item in raw:
        rid = item.get("result_id")
        if rid in quarantine:
            continue
        row = normalizations.get(str(rid))
        out.append(_normalize_result_item(item, row, root) if row else item)
    return out


def iter_reviews(root: Path = ROOT) -> list[dict[str, Any]]:
    raw_results = {
        str(item.get("result_id")): item
        for item in _RAW_ITER_RESULTS(root)
        if isinstance(item.get("result_id"), str) and item.get("result_id")
    }
    quarantine = _quarantine_entries(raw_results, root)
    raw = _RAW_ITER_REVIEWS(root)
    raw_map = {
        str(item.get("review_id")): item
        for item in raw
        if isinstance(item.get("review_id"), str) and item.get("review_id")
    }
    payload = _compatibility_payload(root)
    normalizations = _unique_entries(
        payload["review_normalizations"], "review_id", f"{COMPATIBILITY_FILE}: review_normalizations"
    )
    missing = set(normalizations) - set(raw_map)
    if missing:
        raise ResultRecordError(
            f"{COMPATIBILITY_FILE}: stale review normalization(s): {sorted(missing)!r}"
        )
    out: list[dict[str, Any]] = []
    for item in raw:
        if item.get("result_id") in quarantine:
            continue
        review_id_value = item.get("review_id")
        row = normalizations.get(str(review_id_value))
        out.append(_normalize_review_item(item, row, root) if row else item)
    return out


def _parallel_results(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for item in iter_results(root):
        rid = item.get("result_id")
        if isinstance(rid, str) and rid:
            if rid in out:
                raise _parallel.ParallelEvidenceError(f"duplicate result_id: {rid}")
            out[rid] = item
    return out


def _parallel_reviews(root: Path = ROOT) -> dict[str, list[dict[str, Any]]]:
    out: dict[str, list[dict[str, Any]]] = {}
    for item in iter_reviews(root):
        rid = item.get("result_id")
        if isinstance(rid, str) and rid:
            out.setdefault(rid, []).append(item)
    return out


# All implementation-side result/review lookups and parallel evidence reducers
# consume the same compatibility view. The original strict audit is retained and
# therefore still validates every active normalized record against V1 semantics.
_impl.iter_results = iter_results
_impl.iter_reviews = iter_reviews
_parallel.results = _parallel_results
_parallel.result_reviews = _parallel_reviews


def audit(root: Path = ROOT) -> list[str]:
    try:
        # Force registry/quarantine validation even if the repository has no
        # downstream consumer for one of the entries yet.
        iter_results(root)
        iter_reviews(root)
        return _RAW_AUDIT(root)
    except Exception as exc:
        return [str(exc)]


_impl.audit = audit


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
