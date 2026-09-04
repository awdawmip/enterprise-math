#!/usr/bin/env python3
"""Install exact addendum rows into the existing invalid-review isolation layer.

This shim does not reinterpret review dispositions or mutate immutable review bytes.
It extends the existing fail-closed review-audit quarantine with a small exact
addendum discovered during canonical-dispatch recovery, then reuses the original
validator and runtime filter unchanged.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from control_plane import research_result_review_audit_fault_isolation as base

ROOT = Path(__file__).resolve().parents[1]
ADDENDUM_FILE = "control_plane/research_result_review_audit_quarantine_addendum_20260904.json"
QUARANTINE_FILE = base.QUARANTINE_FILE
SCHEMA = base.SCHEMA
STATE = base.STATE
AUTHORITY_FLAGS = base.AUTHORITY_FLAGS
_ORIGINAL_QUARANTINE_ROWS = base.quarantine_rows


class ReviewAuditAddendumError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ReviewAuditAddendumError(f"{path}: JSON root must be object")
    return value


def _addendum_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    path = root / ADDENDUM_FILE
    if not path.exists():
        return {}
    payload = _load(path)
    if payload.get("schema") != SCHEMA or payload.get("status") != "ACTIVE":
        raise ReviewAuditAddendumError(f"{ADDENDUM_FILE}: wrong schema/status")
    rows = payload.get("entries")
    if not isinstance(rows, list):
        raise ReviewAuditAddendumError(f"{ADDENDUM_FILE}: entries must be list")
    out: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ReviewAuditAddendumError(f"{ADDENDUM_FILE}: entry {index} must be object")
        review_id = row.get("review_id")
        if not isinstance(review_id, str) or not review_id or review_id in out:
            raise ReviewAuditAddendumError(
                f"{ADDENDUM_FILE}: invalid/duplicate review_id {review_id!r}"
            )
        for field in (
            "result_id",
            "task_id",
            "review_record_path",
            "review_record_blob_sha1",
            "result_record_path",
            "result_record_blob_sha1",
        ):
            if not isinstance(row.get(field), str) or not row[field]:
                raise ReviewAuditAddendumError(f"{ADDENDUM_FILE}: {review_id} missing {field}")
        allowed = row.get("allowed_review_audit_errors")
        if (
            not isinstance(allowed, list)
            or not allowed
            or any(not isinstance(item, str) or not item for item in allowed)
            or len(set(allowed)) != len(allowed)
        ):
            raise ReviewAuditAddendumError(
                f"{ADDENDUM_FILE}: {review_id} invalid allowed error set"
            )
        if (
            row.get("state") != STATE
            or row.get("operational") is not False
            or row.get("history_preserved") is not True
        ):
            raise ReviewAuditAddendumError(
                f"{ADDENDUM_FILE}: {review_id} wrong state/operational flags"
            )
        reason = row.get("reason")
        if not isinstance(reason, str) or not reason.strip():
            raise ReviewAuditAddendumError(f"{ADDENDUM_FILE}: {review_id} reason required")
        for flag in AUTHORITY_FLAGS:
            if row.get(flag) is not False:
                raise ReviewAuditAddendumError(f"{ADDENDUM_FILE}: {review_id} cannot grant {flag}")
        out[review_id] = dict(row)
    return out


def quarantine_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    primary = _ORIGINAL_QUARANTINE_ROWS(root)
    addendum = _addendum_rows(root)
    overlap = sorted(set(primary) & set(addendum))
    if overlap:
        raise ReviewAuditAddendumError(
            f"review-audit quarantine duplicated across primary/addendum: {overlap}"
        )
    return {**primary, **addendum}


def _patch() -> None:
    if getattr(base, "_review_audit_addendum_installed", False):
        return
    base.quarantine_rows = quarantine_rows
    base._review_audit_addendum_installed = True


def validated_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    _patch()
    return base.validated_rows(root)


def install(root: Path = ROOT) -> None:
    _patch()
    # Exact bytes and the complete current strict error set are revalidated by
    # the original implementation before any operational review filtering.
    base.validated_rows(root)
    base.install(root)


def main() -> int:
    try:
        rows = validated_rows(ROOT)
        install(ROOT)
    except Exception as exc:
        print("ERROR:", exc)
        return 1
    print(
        "PASS: invalid-review audit isolation includes exact legacy-schema addendum "
        f"({len(rows)} total nonoperational invalid review(s))."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
