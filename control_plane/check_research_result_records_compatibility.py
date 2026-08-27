#!/usr/bin/env python3
"""Fail-closed result/review audit with exact immutable destination aliases."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools import research_result_records, research_task_records  # noqa: E402

WAIVER_FILE = "research_result_review_compatibility_waivers.json"
WAIVER_SCHEMA = "ENTERPRISE_MATH_RESULT_REVIEW_COMPATIBILITY_WAIVERS_V1"
WAIVER_SCOPE = "DESTINATION_CLASS_ALIAS_ONLY"


class ResultCompatibilityAuditError(ValueError):
    pass


def _load_registry(root: Path) -> list[dict[str, Any]]:
    path = root / WAIVER_FILE
    if not path.exists():
        return []
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or value.get("schema") != WAIVER_SCHEMA:
        raise ResultCompatibilityAuditError(f"{WAIVER_FILE}: wrong schema")
    if value.get("status") != "ACTIVE":
        raise ResultCompatibilityAuditError(f"{WAIVER_FILE}: status must be ACTIVE")
    rows = value.get("waivers")
    if not isinstance(rows, list):
        raise ResultCompatibilityAuditError(f"{WAIVER_FILE}: waivers must be a list")
    seen_ids: set[str] = set()
    seen_reviews: set[str] = set()
    out: list[dict[str, Any]] = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ResultCompatibilityAuditError(f"{WAIVER_FILE}: waiver {index} must be an object")
        wid = row.get("waiver_id")
        review_id = row.get("review_id")
        if not isinstance(wid, str) or not wid:
            raise ResultCompatibilityAuditError(f"{WAIVER_FILE}: waiver {index} missing waiver_id")
        if wid in seen_ids:
            raise ResultCompatibilityAuditError(f"{WAIVER_FILE}: duplicate waiver_id {wid}")
        if not isinstance(review_id, str) or not review_id:
            raise ResultCompatibilityAuditError(f"{WAIVER_FILE}: {wid} missing review_id")
        if review_id in seen_reviews:
            raise ResultCompatibilityAuditError(f"{WAIVER_FILE}: duplicate review waiver {review_id}")
        if row.get("scope") != WAIVER_SCOPE:
            raise ResultCompatibilityAuditError(f"{WAIVER_FILE}: {wid} has unsupported scope")
        if row.get("stored_destination_class") == row.get("compatibility_destination_class"):
            raise ResultCompatibilityAuditError(f"{WAIVER_FILE}: {wid} alias must change the stored class")
        if row.get("compatibility_destination_class") not in research_result_records.DESTINATION_CLASSES:
            raise ResultCompatibilityAuditError(f"{WAIVER_FILE}: {wid} compatibility class is not canonical")
        if row.get("compatibility_destination_class") != "NONE":
            raise ResultCompatibilityAuditError(
                f"{WAIVER_FILE}: {wid} only NONE aliases are supported by this V1 compatibility scope"
            )
        if row.get("required_destination_ref_or_none") is not None:
            raise ResultCompatibilityAuditError(f"{WAIVER_FILE}: {wid} NONE alias requires null destination ref")
        for flag in (
            "working_truth_granted",
            "foundation_authority_granted",
            "canonical_promotion_granted",
            "successor_triggered",
        ):
            if row.get(flag) is not False:
                raise ResultCompatibilityAuditError(f"{WAIVER_FILE}: {wid} cannot grant {flag}")
        seen_ids.add(wid)
        seen_reviews.add(review_id)
        out.append(row)
    return out


def _waiver_suppressions(root: Path) -> tuple[set[str], list[str]]:
    suppressions: set[str] = set()
    errors: list[str] = []
    try:
        waivers = _load_registry(root)
        reviews = research_result_records.iter_reviews(root)
    except Exception as exc:
        return set(), [str(exc)]
    by_id = {
        str(item.get("review_id")): item
        for item in reviews
        if isinstance(item.get("review_id"), str)
    }
    raw_errors = research_result_records.audit(root)
    for row in waivers:
        wid = str(row["waiver_id"])
        review_id = str(row["review_id"])
        review = by_id.get(review_id)
        if review is None:
            errors.append(f"{WAIVER_FILE}: {wid}: unknown review_id {review_id}")
            continue
        path_value = row.get("review_record_path")
        if review.get("_review_path") != path_value:
            errors.append(f"{WAIVER_FILE}: {wid}: review_record_path does not match immutable review")
            continue
        for field in ("result_id", "task_id", "publication_id"):
            if review.get(field) != row.get(field):
                errors.append(f"{WAIVER_FILE}: {wid}: {field} does not match immutable review")
                break
        else:
            if review.get("destination_class") != row.get("stored_destination_class"):
                errors.append(f"{WAIVER_FILE}: {wid}: stored destination class drift")
                continue
            if review.get("destination_ref_or_none") is not row.get("required_destination_ref_or_none"):
                errors.append(f"{WAIVER_FILE}: {wid}: destination ref does not match NONE alias semantics")
                continue
            if not isinstance(path_value, str):
                errors.append(f"{WAIVER_FILE}: {wid}: invalid review_record_path")
                continue
            path = root / path_value
            if not path.exists():
                errors.append(f"{WAIVER_FILE}: {wid}: review record path missing")
                continue
            actual_blob = research_task_records.git_blob_sha1_bytes(path.read_bytes())
            if actual_blob != row.get("review_record_blob_sha1"):
                errors.append(f"{WAIVER_FILE}: {wid}: pinned review-record blob drift")
                continue
            expected = f"{path_value}: invalid destination_class"
            same_prefix = [item for item in raw_errors if item.startswith(f"{path_value}:")]
            if same_prefix != [expected]:
                errors.append(
                    f"{WAIVER_FILE}: {wid}: waiver scope does not exactly equal current review errors; "
                    f"expected={[expected]!r} actual={same_prefix!r}"
                )
                continue
            suppressions.add(expected)
    return suppressions, errors


def audit(root: Path = ROOT) -> list[str]:
    raw_errors = research_result_records.audit(root)
    suppressions, waiver_errors = _waiver_suppressions(root)
    raw_set = set(raw_errors)
    errors = list(waiver_errors)
    errors.extend(
        f"{WAIVER_FILE}: stale or unused suppression: {item}"
        for item in sorted(suppressions - raw_set)
    )
    errors.extend(item for item in raw_errors if item not in suppressions)
    return errors


def main() -> int:
    errors = audit(ROOT)
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    suppressions, _ = _waiver_suppressions(ROOT)
    print(
        "PASS: immutable result/review audit valid with "
        f"{len(suppressions)} exact destination-alias suppression(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
