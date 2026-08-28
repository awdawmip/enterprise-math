#!/usr/bin/env python3
"""Exact task-result review authority isolation for known unauthorized history.

This layer does not reinterpret a review disposition and does not create a new
Driver review. It preserves exact immutable review bytes while removing only
explicitly pinned records from the operational review view when they fail the
source-backed Driver authority contract. The corresponding result therefore
returns to AWAITING_DRIVER_REVIEW until an ordinary authorized replacement review
is created.

Every quarantine is fail-closed: exact review path/blob, identity fields, and the
exact current Driver-authority error set must match. Any drift or newly appearing
error makes the quarantine audit fail.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
QUARANTINE_FILE = "research_driver_review_authority_quarantines.json"
QUARANTINE_SCHEMA = "ENTERPRISE_MATH_DRIVER_REVIEW_AUTHORITY_QUARANTINE_V1"
QUARANTINE_STATE = "INVALID_DRIVER_AUTHORITY"
_AUTHORITY_FLAGS = (
    "working_truth_granted",
    "foundation_authority_granted",
    "canonical_promotion_granted",
    "successor_triggered",
)


class DriverReviewAuthorityIsolationError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise DriverReviewAuthorityIsolationError(f"{path}: cannot load JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise DriverReviewAuthorityIsolationError(f"{path}: JSON root must be object")
    return value


def _git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return "sha1:" + hashlib.sha1(header + data).hexdigest()


def quarantine_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    path = root / QUARANTINE_FILE
    if not path.exists():
        return {}
    payload = _load(path)
    if payload.get("schema") != QUARANTINE_SCHEMA:
        raise DriverReviewAuthorityIsolationError(f"{QUARANTINE_FILE}: wrong schema")
    if payload.get("status") != "ACTIVE":
        raise DriverReviewAuthorityIsolationError(f"{QUARANTINE_FILE}: status must be ACTIVE")
    rows = payload.get("entries")
    if not isinstance(rows, list):
        raise DriverReviewAuthorityIsolationError(f"{QUARANTINE_FILE}: entries must be list")

    out: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise DriverReviewAuthorityIsolationError(
                f"{QUARANTINE_FILE}: entry {index} must be object"
            )
        review_id = row.get("review_id")
        if not isinstance(review_id, str) or not review_id:
            raise DriverReviewAuthorityIsolationError(
                f"{QUARANTINE_FILE}: entry {index} missing review_id"
            )
        if review_id in out:
            raise DriverReviewAuthorityIsolationError(
                f"{QUARANTINE_FILE}: duplicate review_id {review_id}"
            )
        for field in (
            "result_id",
            "task_id",
            "review_record_path",
            "review_record_blob_sha1",
        ):
            if not isinstance(row.get(field), str) or not row[field]:
                raise DriverReviewAuthorityIsolationError(
                    f"{QUARANTINE_FILE}: {review_id} missing {field}"
                )
        if row.get("state") != QUARANTINE_STATE:
            raise DriverReviewAuthorityIsolationError(
                f"{QUARANTINE_FILE}: {review_id} wrong state"
            )
        if row.get("operational") is not False or row.get("history_preserved") is not True:
            raise DriverReviewAuthorityIsolationError(
                f"{QUARANTINE_FILE}: {review_id} must be nonoperational preserved history"
            )
        allowed = row.get("allowed_authority_errors")
        if (
            not isinstance(allowed, list)
            or not allowed
            or any(not isinstance(item, str) or not item for item in allowed)
            or len(set(allowed)) != len(allowed)
        ):
            raise DriverReviewAuthorityIsolationError(
                f"{QUARANTINE_FILE}: {review_id} allowed_authority_errors invalid"
            )
        reason = row.get("reason")
        if not isinstance(reason, str) or not reason.strip():
            raise DriverReviewAuthorityIsolationError(
                f"{QUARANTINE_FILE}: {review_id} reason is required"
            )
        for flag in _AUTHORITY_FLAGS:
            if row.get(flag) is not False:
                raise DriverReviewAuthorityIsolationError(
                    f"{QUARANTINE_FILE}: {review_id} cannot grant {flag}"
                )
        out[review_id] = row
    return out


def validated_quarantines(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    rows = quarantine_rows(root)
    seen_paths: set[str] = set()
    for review_id, row in rows.items():
        rel = row["review_record_path"]
        if rel in seen_paths:
            raise DriverReviewAuthorityIsolationError(
                f"{QUARANTINE_FILE}: duplicate review_record_path {rel}"
            )
        seen_paths.add(rel)
        path = root / rel
        if not path.exists():
            raise DriverReviewAuthorityIsolationError(
                f"{QUARANTINE_FILE}: {review_id} review record missing"
            )
        actual_blob = _git_blob_sha1(path.read_bytes())
        if actual_blob != row["review_record_blob_sha1"]:
            raise DriverReviewAuthorityIsolationError(
                f"{QUARANTINE_FILE}: {review_id} review record blob drift; "
                f"declared={row['review_record_blob_sha1']} actual={actual_blob}"
            )
        item = _load(path)
        if item.get("review_id") != review_id:
            raise DriverReviewAuthorityIsolationError(
                f"{QUARANTINE_FILE}: {review_id} review_id mismatch"
            )
        if item.get("result_id") != row["result_id"]:
            raise DriverReviewAuthorityIsolationError(
                f"{QUARANTINE_FILE}: {review_id} result_id mismatch"
            )
        if item.get("task_id") != row["task_id"]:
            raise DriverReviewAuthorityIsolationError(
                f"{QUARANTINE_FILE}: {review_id} task_id mismatch"
            )
    return rows


def operational_reviews(
    reviews: list[dict[str, Any]], root: Path = ROOT
) -> list[dict[str, Any]]:
    """Remove only exact validated authority-quarantined review IDs."""
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
        raise DriverReviewAuthorityIsolationError(
            f"{QUARANTINE_FILE}: quarantined review(s) absent from pre-isolation view: {missing}"
        )
    return [item for item in reviews if item.get("review_id") not in quarantine]


def quarantine_authority_errors(
    authority_error_fn: Callable[[dict[str, Any], Path], list[str]],
    *,
    legacy_review_ids: set[str] | None = None,
    root: Path = ROOT,
) -> list[str]:
    """Prove every quarantine matches the exact current authority failure set."""
    errors: list[str] = []
    rows = validated_quarantines(root)
    legacy = legacy_review_ids or set()
    for review_id, row in rows.items():
        if review_id in legacy:
            errors.append(
                f"{QUARANTINE_FILE}: {review_id} cannot also be legacy-authority exempt"
            )
            continue
        path = root / row["review_record_path"]
        item = _load(path)
        item["_review_path"] = row["review_record_path"]
        actual = set(authority_error_fn(item, root))
        expected = {
            f"{row['review_record_path']}: {suffix}"
            for suffix in row["allowed_authority_errors"]
        }
        if actual != expected:
            errors.append(
                f"{QUARANTINE_FILE}: {review_id} authority error-set drift; "
                f"expected={sorted(expected)!r} actual={sorted(actual)!r}"
            )
    return errors


def install(root: Path = ROOT) -> None:
    """Patch the public result/review facade so quarantined reviews are nonoperational."""
    validated_quarantines(root)
    from tools import research_result_records

    if getattr(research_result_records, "_driver_review_authority_isolation_installed", False):
        return
    base_iter_reviews = research_result_records.iter_reviews

    def iter_reviews(local_root: Path = research_result_records.ROOT) -> list[dict[str, Any]]:
        return operational_reviews(base_iter_reviews(local_root), local_root)

    research_result_records.iter_reviews = iter_reviews
    research_result_records._driver_review_authority_isolation_installed = True


def audit(root: Path = ROOT) -> list[str]:
    """Validate exact quarantine and prove quarantined reviews leave operational view."""
    errors: list[str] = []
    try:
        import research_driver_authority as driver_authority
        from tools import research_result_records

        rows = validated_quarantines(root)
        errors.extend(
            quarantine_authority_errors(
                driver_authority.review_authority_errors,
                legacy_review_ids=driver_authority.legacy_review_ids(root),
                root=root,
            )
        )
        install(root)
        operational = research_result_records.iter_reviews(root)
        operational_ids = {
            str(item.get("review_id"))
            for item in operational
            if isinstance(item.get("review_id"), str)
        }
        leaked = sorted(set(rows) & operational_ids)
        if leaked:
            errors.append(
                f"{QUARANTINE_FILE}: quarantined reviews remain operational: {leaked}"
            )
        for review in operational:
            errors.extend(driver_authority.review_authority_errors(review, root))
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
        "PASS: exact unauthorized Driver-review history is quarantined from "
        f"operational authority ({len(quarantine_rows())} review(s))."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
