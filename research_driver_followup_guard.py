#!/usr/bin/env python3
"""Canonical guard for Driver-review automatic follow-up.

`research_driver_followup.py` contains the storage/materialization primitive.  This
guard owns the cutover authority.  Legacy compatibility is an exact immutable
review-ID baseline pinned to the pre-policy repository tree; `reviewed_at` is
never allowed to self-declare legacy status.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import research_driver_followup as _impl

ROOT = Path(__file__).resolve().parent
BASELINE_PATH = ROOT / "research_driver_followup_legacy_reviews.json"
BASELINE_SCHEMA = "ENTERPRISE_MATH_DRIVER_REVIEW_FOLLOWUP_LEGACY_BASELINE_V1"
FROZEN_BASE = "00c3c8143ca38410df7ed0de64158a3d33e3c67b"
FROZEN_REVIEW_TREE = "41a57a0c838d944ac61908fcdb200d425ef89b18"

DriverFollowupError = _impl.DriverFollowupError
GATES = _impl.GATES


def _load_baseline(root: Path = ROOT) -> dict[str, Any]:
    path = root / BASELINE_PATH.name
    if not path.exists():
        raise DriverFollowupError(f"Driver follow-up legacy baseline is missing: {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise DriverFollowupError("Driver follow-up legacy baseline root must be an object")
    if value.get("schema") != BASELINE_SCHEMA:
        raise DriverFollowupError("Driver follow-up legacy baseline schema mismatch")
    if value.get("frozen_base") != FROZEN_BASE:
        raise DriverFollowupError("Driver follow-up legacy baseline frozen_base drift")
    if value.get("frozen_review_tree") != FROZEN_REVIEW_TREE:
        raise DriverFollowupError("Driver follow-up legacy baseline review-tree drift")
    ids = value.get("review_ids")
    if (
        not isinstance(ids, list)
        or not ids
        or any(not isinstance(item, str) or not item.strip() for item in ids)
        or len(ids) != len(set(ids))
    ):
        raise DriverFollowupError("Driver follow-up legacy review_ids must be a nonempty unique string list")
    return value


def legacy_review_ids(root: Path = ROOT) -> frozenset[str]:
    return frozenset(_load_baseline(root)["review_ids"])


def review_requires_followup(review: dict[str, Any], root: Path = ROOT) -> bool:
    review_id = review.get("review_id")
    if not isinstance(review_id, str) or not review_id.strip():
        # Missing identity can never gain a compatibility exemption.
        return True
    return review_id.strip() not in legacy_review_ids(root)


def _bind_guard(root: Path = ROOT) -> None:
    """Replace the implementation primitive's time-based classifier in-process."""

    def _guarded(review: dict[str, Any]) -> bool:
        return review_requires_followup(review, root)

    _impl.review_requires_followup = _guarded


def baseline_audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        baseline = legacy_review_ids(root)
    except Exception as exc:
        return [str(exc)]
    try:
        current = _impl.review_map(root)
    except Exception as exc:
        return [f"cannot enumerate current Driver reviews: {exc}"]
    missing = sorted(baseline - set(current))
    if missing:
        errors.append(f"legacy review baseline IDs missing from current immutable store: {missing}")
    return errors


def audit(root: Path = ROOT) -> list[str]:
    errors = baseline_audit(root)
    if errors:
        return errors
    _bind_guard(root)
    return _impl.audit(root)


def state_for_review(review_id: str, root: Path = ROOT) -> dict[str, Any]:
    _bind_guard(root)
    return _impl.state_for_review(review_id, root)


def materialize(
    *,
    review_id: str,
    spec: dict[str, Any],
    created_at: str | None = None,
    root: Path = ROOT,
) -> dict[str, Any]:
    errors = baseline_audit(root)
    if errors:
        raise DriverFollowupError("; ".join(errors))
    _bind_guard(root)
    return _impl.materialize(
        review_id=review_id,
        spec=spec,
        created_at=created_at,
        root=root,
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Canonical guarded Driver-review automatic follow-up taskset control"
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("audit")

    state = sub.add_parser("state")
    state.add_argument("--review-id", required=True)

    mat = sub.add_parser("materialize")
    mat.add_argument("--review-id", required=True)
    mat.add_argument("--spec", required=True)
    mat.add_argument("--created-at")

    args = parser.parse_args()
    if args.command == "audit":
        errors = audit(ROOT)
        if errors:
            for error in errors:
                print("ERROR:", error)
            return 1
        governed = sum(
            1
            for review in _impl.review_map(ROOT).values()
            if review_requires_followup(review, ROOT)
        )
        print(
            "PASS: guarded Driver follow-up barrier valid "
            f"({len(legacy_review_ids(ROOT))} frozen legacy review(s), "
            f"{governed} governed review(s), {len(_impl.iter_packets(ROOT))} packet(s))."
        )
        return 0

    if args.command == "state":
        print(json.dumps(state_for_review(args.review_id, ROOT), ensure_ascii=False, indent=2, sort_keys=True))
        return 0

    spec_path = Path(args.spec)
    if not spec_path.is_absolute():
        spec_path = ROOT / spec_path
    if not spec_path.exists():
        raise DriverFollowupError(f"follow-up spec not found: {spec_path}")
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    if not isinstance(spec, dict):
        raise DriverFollowupError("follow-up spec root must be an object")
    result = materialize(
        review_id=args.review_id,
        spec=spec,
        created_at=args.created_at,
        root=ROOT,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except DriverFollowupError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
