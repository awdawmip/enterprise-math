#!/usr/bin/env python3
"""Exact runtime compatibility for Driver-review authority pins.

Two distinct historical cases are handled without rewriting immutable reviews:

1. A review may pin the *raw* authority_record_id of an authority record whose
   ID is already byte-pinned and normalized by research_driver_authority_compatibility.json.
   That raw pin remains valid iff it is exactly the active authority record's
   validated ``_raw_authority_record_id`` and the source comment pin also matches.
2. Current-schema reviews that contain no source-backed authority pin are not
   repaired. Exact review bytes are added to the existing INVALID_DRIVER_AUTHORITY
   quarantine so they remain history and lose operational review/follow-up authority.

No review disposition, Driver authority event, Working Truth, Foundation,
canonical-promotion, or successor authority is created by this adapter.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
ADDENDUM_FILE = "control_plane/driver_review_authority_quarantine_addendum_20260904.json"


class DriverReviewAuthorityCompatRuntimeError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise DriverReviewAuthorityCompatRuntimeError(f"{path}: JSON root must be object")
    return value


def _patch_authority_checker() -> None:
    import research_driver_authority as authority

    if getattr(authority, "_raw_authority_review_pin_compat_installed", False):
        return
    base = authority.review_authority_errors

    def review_authority_errors(review: dict[str, Any], root: Path = authority.ROOT) -> list[str]:
        errors = base(review, root)
        if len(errors) != 1 or not errors[0].endswith(
            ": driver_authority_record_id does not pin active authority"
        ):
            return errors
        driver_id = review.get("driver_id")
        reviewed_at = review.get("reviewed_at")
        if not isinstance(driver_id, str) or not isinstance(reviewed_at, str):
            return errors
        try:
            active = authority.require_active_driver(driver_id, reviewed_at, root)
        except Exception:
            return errors
        if not isinstance(active, dict):
            return errors
        raw_id = active.get("_raw_authority_record_id")
        if not isinstance(raw_id, str) or not raw_id:
            return errors
        if review.get("driver_authority_record_id") != raw_id:
            return errors
        # Raw-ID compatibility never relaxes the independent source-comment pin.
        if review.get("driver_authority_source_comment_id") != active.get("source_comment_id"):
            return errors
        return []

    authority.review_authority_errors = review_authority_errors
    authority._raw_authority_review_pin_compat_installed = True


def _patch_quarantine_registry() -> None:
    from control_plane import research_driver_review_authority_fault_isolation as isolation

    if getattr(isolation, "_authority_quarantine_addendum_installed", False):
        return
    base = isolation.quarantine_rows

    def quarantine_rows(root: Path = isolation.ROOT) -> dict[str, dict[str, Any]]:
        primary = base(root)
        path = root / ADDENDUM_FILE
        if not path.exists():
            return primary
        payload = _load(path)
        if payload.get("schema") != isolation.QUARANTINE_SCHEMA:
            raise DriverReviewAuthorityCompatRuntimeError(f"{ADDENDUM_FILE}: wrong schema")
        if payload.get("status") != "ACTIVE":
            raise DriverReviewAuthorityCompatRuntimeError(f"{ADDENDUM_FILE}: status must be ACTIVE")
        rows = payload.get("entries")
        if not isinstance(rows, list):
            raise DriverReviewAuthorityCompatRuntimeError(f"{ADDENDUM_FILE}: entries must be list")
        addendum: dict[str, dict[str, Any]] = {}
        for index, row in enumerate(rows):
            if not isinstance(row, dict):
                raise DriverReviewAuthorityCompatRuntimeError(
                    f"{ADDENDUM_FILE}: entry {index} must be object"
                )
            review_id = row.get("review_id")
            if not isinstance(review_id, str) or not review_id or review_id in addendum:
                raise DriverReviewAuthorityCompatRuntimeError(
                    f"{ADDENDUM_FILE}: invalid/duplicate review_id {review_id!r}"
                )
            addendum[review_id] = dict(row)
        overlap = sorted(set(primary) & set(addendum))
        if overlap:
            raise DriverReviewAuthorityCompatRuntimeError(
                f"Driver-review authority quarantine duplicated across primary/addendum: {overlap}"
            )
        return {**primary, **addendum}

    isolation.quarantine_rows = quarantine_rows
    isolation._authority_quarantine_addendum_installed = True


def install(root: Path = ROOT) -> None:
    _patch_authority_checker()
    _patch_quarantine_registry()
    from control_plane import research_driver_review_authority_fault_isolation as isolation

    # Reuse the original exact blob/error-set validation after both patches.
    rows = isolation.validated_quarantines(root)
    import research_driver_authority as authority

    errors = isolation.quarantine_authority_errors(
        authority.review_authority_errors,
        legacy_review_ids=authority.legacy_review_ids(root),
        root=root,
    )
    if errors:
        raise DriverReviewAuthorityCompatRuntimeError("; ".join(errors))
    if not rows:
        raise DriverReviewAuthorityCompatRuntimeError(
            "Driver-review authority quarantine unexpectedly empty after compatibility install"
        )


def audit(root: Path = ROOT) -> list[str]:
    try:
        install(root)
        import research_driver_authority as authority
        from control_plane import research_driver_review_authority_fault_isolation as isolation

        isolation.install(root)
        errors = isolation.audit(root)
        errors.extend(authority.audit(root))
        return errors
    except Exception as exc:
        return [str(exc)]


def main() -> int:
    errors = audit(ROOT)
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(
        "PASS: raw authority-record aliases remain valid review pins; reviews with "
        "no authority pin remain exact nonoperational history."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
