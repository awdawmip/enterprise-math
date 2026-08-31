#!/usr/bin/env python3
"""Exact audit-only containment for malformed results on superseded publications.

This layer never removes a result from the result API and never repairs immutable
result bytes.  It may suppress strict audit errors only when the exact result
record is byte-pinned and its publication is directly superseded by a strictly
newer same-task publication generation.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

QUARANTINE_FILE = "research_result_record_audit_quarantines.json"
SCHEMA = "ENTERPRISE_MATH_RESULT_RECORD_AUDIT_QUARANTINE_V1"
STATE = "NONOPERATIONAL_PUBLICATION_GENERATION_RESULT_AUDIT_DEFECT"


class ResultAuditIsolationError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ResultAuditIsolationError(f"{path}: JSON root must be object")
    return value


def _blob(path: Path) -> str:
    data = path.read_bytes()
    return "sha1:" + hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def quarantine_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    path = root / QUARANTINE_FILE
    if not path.exists():
        return {}
    payload = _load(path)
    if payload.get("schema") != SCHEMA or payload.get("status") != "ACTIVE":
        raise ResultAuditIsolationError(f"{QUARANTINE_FILE}: wrong schema/status")
    rows = payload.get("entries")
    if not isinstance(rows, list):
        raise ResultAuditIsolationError(f"{QUARANTINE_FILE}: entries must be list")
    out: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ResultAuditIsolationError(f"{QUARANTINE_FILE}: entry {index} must be object")
        rid = row.get("result_id")
        if not isinstance(rid, str) or not rid or rid in out:
            raise ResultAuditIsolationError(f"{QUARANTINE_FILE}: invalid/duplicate result_id {rid!r}")
        for field in (
            "task_id", "publication_id", "superseding_publication_id", "record_path", "record_blob_sha1"
        ):
            if not isinstance(row.get(field), str) or not row[field]:
                raise ResultAuditIsolationError(f"{QUARANTINE_FILE}: {rid} missing {field}")
        errors = row.get("allowed_result_audit_errors")
        if not isinstance(errors, list) or not errors or any(not isinstance(x, str) or not x for x in errors) or len(set(errors)) != len(errors):
            raise ResultAuditIsolationError(f"{QUARANTINE_FILE}: {rid} invalid exact error set")
        if row.get("state") != STATE or row.get("audit_only") is not True or row.get("history_preserved") is not True:
            raise ResultAuditIsolationError(f"{QUARANTINE_FILE}: {rid} wrong state/audit flags")
        for flag in ("working_truth_granted", "foundation_authority_granted", "canonical_promotion_granted", "successor_triggered"):
            if row.get(flag) is not False:
                raise ResultAuditIsolationError(f"{QUARANTINE_FILE}: {rid} cannot grant {flag}")
        out[rid] = row
    return out


def validated_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    from control_plane import research_result_records_impl as result_impl
    from control_plane import research_task_records_impl as task_impl

    rows = quarantine_rows(root)
    raw_results = {
        str(item.get("result_id")): item
        for item in result_impl.__dict__.get("_history_original_iter_results", result_impl.iter_results)(root)
        if isinstance(item.get("result_id"), str)
    }
    publications = task_impl.iter_records(root)
    by_pub = {
        str(item.get("publication_id")): item
        for item in publications
        if isinstance(item.get("publication_id"), str)
    }
    for rid, row in rows.items():
        result = raw_results.get(rid)
        if result is None:
            raise ResultAuditIsolationError(f"{QUARANTINE_FILE}: {rid} result missing")
        if result.get("task_id") != row["task_id"] or result.get("publication_id") != row["publication_id"]:
            raise ResultAuditIsolationError(f"{QUARANTINE_FILE}: {rid} result identity mismatch")
        if result.get("_record_path") != row["record_path"]:
            raise ResultAuditIsolationError(f"{QUARANTINE_FILE}: {rid} result path mismatch")
        record_path = root / row["record_path"]
        if not record_path.is_file() or _blob(record_path) != row["record_blob_sha1"]:
            raise ResultAuditIsolationError(f"{QUARANTINE_FILE}: {rid} result record blob drift")
        old = by_pub.get(row["publication_id"])
        new = by_pub.get(row["superseding_publication_id"])
        if old is None or new is None:
            raise ResultAuditIsolationError(f"{QUARANTINE_FILE}: {rid} publication lineage object missing")
        if old.get("task_id") != row["task_id"] or new.get("task_id") != row["task_id"]:
            raise ResultAuditIsolationError(f"{QUARANTINE_FILE}: {rid} publication lineage task mismatch")
        if new.get("supersedes_publication_id") != row["publication_id"]:
            raise ResultAuditIsolationError(f"{QUARANTINE_FILE}: {rid} successor is not direct")
        old_gen = old.get("publication_generation")
        new_gen = new.get("publication_generation")
        if not isinstance(old_gen, int) or not isinstance(new_gen, int) or new_gen <= old_gen:
            raise ResultAuditIsolationError(f"{QUARANTINE_FILE}: {rid} successor generation is not newer")
    return rows


def suppression_strings(root: Path = ROOT) -> set[str]:
    return {
        f"{row['record_path']}: {suffix}"
        for row in validated_rows(root).values()
        for suffix in row["allowed_result_audit_errors"]
    }


def audit_against(errors: list[str], root: Path = ROOT) -> list[str]:
    suppressions = suppression_strings(root)
    raw = set(errors)
    stale = sorted(suppressions - raw)
    out = [f"{QUARANTINE_FILE}: stale or unused suppression: {item}" for item in stale]
    out.extend(item for item in errors if item not in suppressions)
    return out


def main() -> int:
    try:
        rows = validated_rows(ROOT)
    except Exception as exc:
        print("ERROR:", exc)
        return 1
    print(
        "PASS: exact superseded-publication result audit defects pinned "
        f"({len(rows)} result(s)); result runtime/history remains unchanged."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
