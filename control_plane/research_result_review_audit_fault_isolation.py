#!/usr/bin/env python3
"""Exact audit/runtime isolation for immutable invalid Driver-review records.

A quarantined review remains immutable history but is never operational review
authority.  Every row pins exact review/result bytes and the complete strict V1
review-audit error set recomputed from those bytes.  No disposition is repaired,
interpreted, or promoted by this layer.
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

from control_plane import research_result_records_impl as impl  # noqa: E402

QUARANTINE_FILE = "research_result_review_audit_quarantines.json"
SCHEMA = "ENTERPRISE_MATH_RESULT_REVIEW_AUDIT_QUARANTINE_V1"
STATE = "INVALID_IMMUTABLE_REVIEW_RECORD"
AUTHORITY_FLAGS = (
    "working_truth_granted",
    "foundation_authority_granted",
    "canonical_promotion_granted",
    "successor_triggered",
)


class ReviewAuditIsolationError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ReviewAuditIsolationError(f"{path}: JSON root must be object")
    return value


def _blob(path: Path) -> str:
    data = path.read_bytes()
    return "sha1:" + hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def _sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _same_blob(left: Any, right: Any) -> bool:
    return impl._same_git_blob_identity(left, right)


def _raw_reviews(root: Path) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    directory = root / "research_result_reviews"
    for path in sorted(directory.glob("*/*.json")) if directory.exists() else []:
        value = _load(path)
        value["_review_path"] = path.relative_to(root).as_posix()
        out.append(value)
    return out


def _raw_results(root: Path) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    directory = root / "research_result_records"
    for path in sorted(directory.glob("*/*.json")) if directory.exists() else []:
        value = _load(path)
        value["_record_path"] = path.relative_to(root).as_posix()
        out.append(value)
    return out


def _review_errors(review: dict[str, Any], result: dict[str, Any], root: Path) -> list[str]:
    errors: list[str] = []
    if review.get("record_schema") != impl.REVIEW_SCHEMA:
        errors.append("wrong review schema")
    for field in ("task_id", "publication_id", "execution_record_id"):
        if review.get(field) != result.get(field):
            errors.append(f"result-linked field mismatch: {field}")
    result_has_lane = result.get("execution_cohort_id") is not None or result.get("execution_lane_id") is not None
    review_has_lane = review.get("execution_cohort_id") is not None or review.get("execution_lane_id") is not None
    if result_has_lane != review_has_lane:
        errors.append("lane identity presence differs from result record")
    if result_has_lane:
        for field in impl.LANE_FIELDS:
            if review.get(field) != result.get(field):
                errors.append(f"result-linked lane field mismatch: {field}")
    result_record_path = review.get("result_record_path")
    if not isinstance(result_record_path, str) or not (root / result_record_path).exists():
        errors.append("result record pin missing")
    elif _sha256(root / result_record_path) != review.get("result_record_sha256"):
        errors.append("result record digest drift")
    review_path = review.get("review_path")
    if not isinstance(review_path, str) or not (root / review_path).exists():
        errors.append("review artifact missing")
    else:
        if (
            not _same_blob(_blob(root / review_path), review.get("review_blob_sha1"))
            or _sha256(root / review_path) != review.get("review_sha256")
        ):
            errors.append("review artifact digest drift")
    if review.get("disposition") not in impl.ALL_DISPOSITIONS:
        errors.append("invalid disposition")
    if review.get("destination_class") not in impl.DESTINATION_CLASSES:
        errors.append("invalid destination_class")
    if review.get("terminal") is not (review.get("disposition") in impl.TERMINAL_DISPOSITIONS):
        errors.append("terminal flag mismatch")
    return sorted(set(errors))


def quarantine_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    path = root / QUARANTINE_FILE
    if not path.exists():
        return {}
    payload = _load(path)
    if payload.get("schema") != SCHEMA or payload.get("status") != "ACTIVE":
        raise ReviewAuditIsolationError(f"{QUARANTINE_FILE}: wrong schema/status")
    rows = payload.get("entries")
    if not isinstance(rows, list):
        raise ReviewAuditIsolationError(f"{QUARANTINE_FILE}: entries must be list")
    out: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ReviewAuditIsolationError(f"{QUARANTINE_FILE}: entry {index} must be object")
        review_id = row.get("review_id")
        if not isinstance(review_id, str) or not review_id or review_id in out:
            raise ReviewAuditIsolationError(f"{QUARANTINE_FILE}: invalid/duplicate review_id {review_id!r}")
        for field in (
            "result_id", "task_id", "review_record_path", "review_record_blob_sha1",
            "result_record_path", "result_record_blob_sha1",
        ):
            if not isinstance(row.get(field), str) or not row[field]:
                raise ReviewAuditIsolationError(f"{QUARANTINE_FILE}: {review_id} missing {field}")
        allowed = row.get("allowed_review_audit_errors")
        if not isinstance(allowed, list) or not allowed or any(not isinstance(x, str) or not x for x in allowed) or len(set(allowed)) != len(allowed):
            raise ReviewAuditIsolationError(f"{QUARANTINE_FILE}: {review_id} invalid allowed error set")
        if row.get("state") != STATE or row.get("operational") is not False or row.get("history_preserved") is not True:
            raise ReviewAuditIsolationError(f"{QUARANTINE_FILE}: {review_id} wrong state/operational flags")
        for flag in AUTHORITY_FLAGS:
            if row.get(flag) is not False:
                raise ReviewAuditIsolationError(f"{QUARANTINE_FILE}: {review_id} cannot grant {flag}")
        out[review_id] = row
    return out


def validated_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    rows = quarantine_rows(root)
    raw_reviews = {str(x.get("review_id")): x for x in _raw_reviews(root) if isinstance(x.get("review_id"), str)}
    raw_results = {str(x.get("result_id")): x for x in _raw_results(root) if isinstance(x.get("result_id"), str)}
    for review_id, row in rows.items():
        review = raw_reviews.get(review_id)
        result = raw_results.get(row["result_id"])
        if review is None or result is None:
            raise ReviewAuditIsolationError(f"{QUARANTINE_FILE}: {review_id} pinned review/result missing")
        if review.get("result_id") != row["result_id"] or review.get("task_id") != row["task_id"] or result.get("task_id") != row["task_id"]:
            raise ReviewAuditIsolationError(f"{QUARANTINE_FILE}: {review_id} identity mismatch")
        if review.get("_review_path") != row["review_record_path"] or result.get("_record_path") != row["result_record_path"]:
            raise ReviewAuditIsolationError(f"{QUARANTINE_FILE}: {review_id} path mismatch")
        if _blob(root / row["review_record_path"]) != row["review_record_blob_sha1"]:
            raise ReviewAuditIsolationError(f"{QUARANTINE_FILE}: {review_id} review record blob drift")
        if _blob(root / row["result_record_path"]) != row["result_record_blob_sha1"]:
            raise ReviewAuditIsolationError(f"{QUARANTINE_FILE}: {review_id} result record blob drift")
        actual = _review_errors(review, result, root)
        expected = sorted(row["allowed_review_audit_errors"])
        if actual != expected:
            raise ReviewAuditIsolationError(
                f"{QUARANTINE_FILE}: {review_id} exact audit error set drift; expected={expected!r}; actual={actual!r}"
            )
    return rows


def operational_reviews(reviews: list[dict[str, Any]], root: Path = ROOT) -> list[dict[str, Any]]:
    rows = validated_rows(root)
    return [item for item in reviews if item.get("review_id") not in rows]


def install(root: Path = ROOT) -> None:
    validated_rows(root)
    from control_plane import research_result_records_compat_runtime as compat
    from tools import research_result_records as public

    if getattr(compat, "_review_audit_isolation_installed", False):
        return
    base_iter_reviews = compat.iter_reviews

    def iter_reviews(local_root: Path = compat.ROOT) -> list[dict[str, Any]]:
        return operational_reviews(base_iter_reviews(local_root), local_root)

    compat.iter_reviews = iter_reviews
    impl.iter_reviews = iter_reviews
    public.iter_reviews = iter_reviews
    compat._review_audit_isolation_installed = True
    impl._review_audit_isolation_installed = True
    public._review_audit_isolation_installed = True


def main() -> int:
    try:
        rows = validated_rows(ROOT)
    except Exception as exc:
        print("ERROR:", exc)
        return 1
    print(
        "PASS: exact invalid immutable Driver reviews are nonoperational preserved history "
        f"({len(rows)} review(s)); no review disposition or authority inferred."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
