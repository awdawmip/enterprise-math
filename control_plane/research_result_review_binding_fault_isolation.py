#!/usr/bin/env python3
"""Exact isolation for immutable reviews that pin a stale result digest.

This layer is intentionally independent of Driver-identity/authority quarantine.
It preserves exact review/result bytes, proves the one registered binding defect,
and removes only the exact review from the operational review view.  It does not
reinterpret review disposition, create a replacement review, or assess theorem or
Foundation semantics.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
QUARANTINE_FILE = "research_result_review_binding_quarantines.json"
QUARANTINE_SCHEMA = "ENTERPRISE_MATH_RESULT_REVIEW_BINDING_QUARANTINE_V1"
QUARANTINE_STATE = "STALE_RESULT_BINDING"
_AUTHORITY_FLAGS = (
    "working_truth_granted",
    "foundation_authority_granted",
    "canonical_promotion_granted",
    "successor_triggered",
)


class ResultReviewBindingIsolationError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ResultReviewBindingIsolationError(f"{path}: cannot load JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ResultReviewBindingIsolationError(f"{path}: JSON root must be object")
    return value


def _git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return "sha1:" + hashlib.sha1(header + data).hexdigest()


def _sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def quarantine_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    path = root / QUARANTINE_FILE
    if not path.exists():
        return {}
    payload = _load(path)
    if payload.get("schema") != QUARANTINE_SCHEMA:
        raise ResultReviewBindingIsolationError(f"{QUARANTINE_FILE}: wrong schema")
    if payload.get("status") != "ACTIVE":
        raise ResultReviewBindingIsolationError(f"{QUARANTINE_FILE}: status must be ACTIVE")
    rows = payload.get("entries")
    if not isinstance(rows, list):
        raise ResultReviewBindingIsolationError(f"{QUARANTINE_FILE}: entries must be list")
    out: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ResultReviewBindingIsolationError(
                f"{QUARANTINE_FILE}: entry {index} must be object"
            )
        review_id = row.get("review_id")
        if not isinstance(review_id, str) or not review_id or review_id in out:
            raise ResultReviewBindingIsolationError(
                f"{QUARANTINE_FILE}: invalid/duplicate review_id {review_id!r}"
            )
        for field in (
            "result_id",
            "task_id",
            "review_record_path",
            "review_record_blob_sha1",
            "result_record_path",
            "result_record_blob_sha1",
            "stale_declared_result_record_sha256",
        ):
            if not isinstance(row.get(field), str) or not row[field]:
                raise ResultReviewBindingIsolationError(
                    f"{QUARANTINE_FILE}: {review_id} missing {field}"
                )
        if row.get("state") != QUARANTINE_STATE:
            raise ResultReviewBindingIsolationError(
                f"{QUARANTINE_FILE}: {review_id} wrong state"
            )
        if row.get("operational") is not False or row.get("history_preserved") is not True:
            raise ResultReviewBindingIsolationError(
                f"{QUARANTINE_FILE}: {review_id} must be nonoperational preserved history"
            )
        allowed = row.get("allowed_binding_errors")
        if allowed != ["result record digest drift"]:
            raise ResultReviewBindingIsolationError(
                f"{QUARANTINE_FILE}: {review_id} binding error set must be exact"
            )
        reason = row.get("reason")
        if not isinstance(reason, str) or not reason.strip():
            raise ResultReviewBindingIsolationError(
                f"{QUARANTINE_FILE}: {review_id} reason required"
            )
        for flag in _AUTHORITY_FLAGS:
            if row.get(flag) is not False:
                raise ResultReviewBindingIsolationError(
                    f"{QUARANTINE_FILE}: {review_id} cannot grant {flag}"
                )
        out[review_id] = row
    return out


def validated_quarantines(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    rows = quarantine_rows(root)
    for review_id, row in rows.items():
        review_path = root / row["review_record_path"]
        result_path = root / row["result_record_path"]
        if not review_path.exists() or not result_path.exists():
            raise ResultReviewBindingIsolationError(
                f"{QUARANTINE_FILE}: {review_id} pinned review/result record missing"
            )
        if _git_blob_sha1(review_path.read_bytes()) != row["review_record_blob_sha1"]:
            raise ResultReviewBindingIsolationError(
                f"{QUARANTINE_FILE}: {review_id} review record blob drift"
            )
        if _git_blob_sha1(result_path.read_bytes()) != row["result_record_blob_sha1"]:
            raise ResultReviewBindingIsolationError(
                f"{QUARANTINE_FILE}: {review_id} result record blob drift"
            )
        review = _load(review_path)
        result = _load(result_path)
        if review.get("review_id") != review_id:
            raise ResultReviewBindingIsolationError(
                f"{QUARANTINE_FILE}: {review_id} review_id mismatch"
            )
        if review.get("result_id") != row["result_id"] or result.get("result_id") != row["result_id"]:
            raise ResultReviewBindingIsolationError(
                f"{QUARANTINE_FILE}: {review_id} result identity mismatch"
            )
        if review.get("task_id") != row["task_id"] or result.get("task_id") != row["task_id"]:
            raise ResultReviewBindingIsolationError(
                f"{QUARANTINE_FILE}: {review_id} task identity mismatch"
            )
        if review.get("result_record_path") != row["result_record_path"]:
            raise ResultReviewBindingIsolationError(
                f"{QUARANTINE_FILE}: {review_id} result_record_path mismatch"
            )
        if review.get("result_record_sha256") != row["stale_declared_result_record_sha256"]:
            raise ResultReviewBindingIsolationError(
                f"{QUARANTINE_FILE}: {review_id} stale declared digest drifted"
            )
        actual_result_sha256 = _sha256(result_path)
        if actual_result_sha256 == row["stale_declared_result_record_sha256"]:
            raise ResultReviewBindingIsolationError(
                f"{QUARANTINE_FILE}: {review_id} quarantine is stale because result binding now matches"
            )
        for field in ("publication_id", "execution_record_id"):
            if review.get(field) != result.get(field):
                raise ResultReviewBindingIsolationError(
                    f"{QUARANTINE_FILE}: {review_id} unexpected result-linked mismatch: {field}"
                )
        review_has_lane = review.get("execution_cohort_id") is not None or review.get("execution_lane_id") is not None
        result_has_lane = result.get("execution_cohort_id") is not None or result.get("execution_lane_id") is not None
        if review_has_lane != result_has_lane:
            raise ResultReviewBindingIsolationError(
                f"{QUARANTINE_FILE}: {review_id} unexpected lane-identity mismatch"
            )
        if result_has_lane:
            for field in ("execution_cohort_id", "execution_lane_id"):
                if review.get(field) != result.get(field):
                    raise ResultReviewBindingIsolationError(
                        f"{QUARANTINE_FILE}: {review_id} unexpected lane mismatch: {field}"
                    )
        artifact = review.get("review_path")
        if not isinstance(artifact, str) or not (root / artifact).exists():
            raise ResultReviewBindingIsolationError(
                f"{QUARANTINE_FILE}: {review_id} review artifact missing"
            )
        artifact_path = root / artifact
        if _git_blob_sha1(artifact_path.read_bytes()) != review.get("review_blob_sha1"):
            raise ResultReviewBindingIsolationError(
                f"{QUARANTINE_FILE}: {review_id} unexpected review artifact blob drift"
            )
        if _sha256(artifact_path) != review.get("review_sha256"):
            raise ResultReviewBindingIsolationError(
                f"{QUARANTINE_FILE}: {review_id} unexpected review artifact SHA-256 drift"
            )
    return rows


def operational_reviews(reviews: list[dict[str, Any]], root: Path = ROOT) -> list[dict[str, Any]]:
    quarantine = validated_quarantines(root)
    if not quarantine:
        return reviews
    available = {
        str(item.get("review_id"))
        for item in reviews
        if isinstance(item.get("review_id"), str)
    }
    missing = sorted(set(quarantine) - available)
    if missing:
        raise ResultReviewBindingIsolationError(
            f"{QUARANTINE_FILE}: quarantined review(s) absent from pre-isolation view: {missing}"
        )
    return [item for item in reviews if item.get("review_id") not in quarantine]


def install(root: Path = ROOT) -> None:
    """Remove exact stale-binding reviews from all canonical operational review views."""
    validated_quarantines(root)
    from control_plane import research_result_records_compat_runtime as compat
    from control_plane import research_result_records_impl as impl
    from tools import research_result_records as public

    if getattr(compat, "_review_binding_isolation_installed", False):
        return
    base_iter_reviews = compat.iter_reviews

    def iter_reviews(local_root: Path = compat.ROOT) -> list[dict[str, Any]]:
        return operational_reviews(base_iter_reviews(local_root), local_root)

    compat.iter_reviews = iter_reviews
    impl.iter_reviews = iter_reviews
    public.iter_reviews = iter_reviews
    compat._review_binding_isolation_installed = True
    impl._review_binding_isolation_installed = True
    public._review_binding_isolation_installed = True


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        rows = validated_quarantines(root)
        install(root)
        from tools import research_result_records

        operational = research_result_records.iter_reviews(root)
        operational_ids = {
            str(item.get("review_id"))
            for item in operational
            if isinstance(item.get("review_id"), str)
        }
        leaked = sorted(set(rows) & operational_ids)
        if leaked:
            errors.append(
                f"{QUARANTINE_FILE}: stale-binding reviews remain operational: {leaked}"
            )
        errors.extend(research_result_records.audit(root))
    except Exception as exc:
        errors.append(str(exc))
    return errors


def main() -> int:
    errors = audit()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(
        "PASS: exact stale result-review bindings are preserved as history and removed "
        f"from operational review authority ({len(quarantine_rows())} review(s))."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
