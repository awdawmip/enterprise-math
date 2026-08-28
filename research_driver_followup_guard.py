#!/usr/bin/env python3
"""Canonical guard for Driver-review automatic follow-up.

The follow-up barrier consumes *operational review authority*, not a raw latest
review.  With one immutable review the authority id is that review id.  With two
or more reviews the authority id is the exact-set review synthesis id after both
reference passes complete.  Source reviews remain immutable evidence and never
become timestamp/latest-wins control authority.

`research_driver_followup.py` remains the storage/task-publication primitive.
This guard binds that primitive to the canonical compatibility + exact-set result
view, owns the frozen legacy baseline, and extends required-gate semantics with
`SATISFIED_BY_EXISTING_CONTROL_ASSET` to avoid duplicate continuations.
"""
from __future__ import annotations

import argparse
import importlib
import json
from pathlib import Path
from typing import Any

import research_driver_followup as _impl

ROOT = Path(__file__).resolve().parent
BASELINE_PATH = ROOT / "research_driver_followup_legacy_reviews.json"
BASELINE_SCHEMA = "ENTERPRISE_MATH_DRIVER_REVIEW_FOLLOWUP_LEGACY_BASELINE_V1"
FROZEN_BASE = "00c3c8143ca38410df7ed0de64158a3d33e3c67b"
FROZEN_REVIEW_TREE = "41a57a0c838d944ac61908fcdb200d425ef89b18"
EXISTING_ASSET_DECISION = "SATISFIED_BY_EXISTING_CONTROL_ASSET"
AUTHORITY_KINDS = {"IMMUTABLE_REVIEW", "REVIEW_SYNTHESIS"}

DriverFollowupError = _impl.DriverFollowupError
GATES = _impl.GATES


def _canonical_results():
    # Lazy import is required because tools.research_result_records imports this
    # guard when installing the follow-up layer.
    return importlib.import_module("tools.research_result_records")


def _review_evidence():
    return importlib.import_module("research_review_evidence")


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
        raise DriverFollowupError(
            "Driver follow-up legacy review_ids must be a nonempty unique string list"
        )
    return value


def legacy_review_ids(root: Path = ROOT) -> frozenset[str]:
    return frozenset(_load_baseline(root)["review_ids"])


def _raw_review_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for row in _canonical_results().iter_reviews(root):
        review_id = row.get("review_id")
        if isinstance(review_id, str) and review_id:
            if review_id in out:
                raise DriverFollowupError(f"duplicate immutable review_id: {review_id}")
            out[review_id] = row
    return out


def _source_reviews(result_id: str, review_ids: list[str], root: Path) -> list[dict[str, Any]]:
    raw = _raw_review_map(root)
    rows: list[dict[str, Any]] = []
    for review_id in review_ids:
        row = raw.get(review_id)
        if row is None or row.get("result_id") != result_id:
            raise DriverFollowupError(
                f"review synthesis source review is unavailable for {result_id}: {review_id}"
            )
        rows.append(row)
    return rows


def _synthesis_destination(
    synthesis: dict[str, Any], source_reviews: list[dict[str, Any]]
) -> tuple[str | None, str]:
    explicit = synthesis.get("operational_destination_class")
    explicit_ref = synthesis.get("operational_destination_ref_or_none")
    if isinstance(explicit, str) and explicit:
        return explicit, explicit_ref if isinstance(explicit_ref, str) else ""

    destinations = {
        str(row.get("destination_class"))
        for row in source_reviews
        if isinstance(row.get("destination_class"), str) and row.get("destination_class")
    }
    if len(destinations) != 1:
        return None, ""
    refs = {
        str(row.get("destination_ref_or_none") or "")
        for row in source_reviews
        if row.get("destination_class") in destinations
    }
    return next(iter(destinations)), next(iter(refs)) if len(refs) == 1 else ""


def authority_for_result(result_id: str, root: Path = ROOT) -> dict[str, Any] | None:
    results = _canonical_results().result_map(root)
    result = results.get(result_id)
    if result is None:
        return None
    state = _review_evidence().state(result_id, root)
    phase = state.get("review_state")
    if phase == "SINGLE_REVIEW_FLOW":
        review = state.get("review")
        if not isinstance(review, dict):
            raise DriverFollowupError("single-review authority is missing its review")
        value = dict(review)
        value.update(
            {
                "review_authority_kind": "IMMUTABLE_REVIEW",
                "review_authority_id": review.get("review_id"),
                "source_review_ids": [review.get("review_id")],
            }
        )
        return value
    if phase not in {"REVIEW_SYNTHESIS_TERMINAL", "REVIEW_SYNTHESIS_NONTERMINAL"}:
        return None

    synthesis = state.get("synthesis")
    if not isinstance(synthesis, dict):
        raise DriverFollowupError("review synthesis authority is missing its synthesis record")
    review_ids = [str(item) for item in synthesis.get("review_ids") or []]
    sources = _source_reviews(result_id, review_ids, root)
    destination, destination_ref = _synthesis_destination(synthesis, sources)
    reviewed_at = max(
        (_impl._parse_time(row.get("reviewed_at"), "reviewed_at") for row in sources),
        default=_impl._parse_time("1970-01-01T00:00:00+00:00", "reviewed_at"),
    ).isoformat()
    authority_id = synthesis.get("synthesis_id")
    return {
        "review_id": authority_id,  # compatibility name consumed by the V1 primitive
        "review_authority_kind": "REVIEW_SYNTHESIS",
        "review_authority_id": authority_id,
        "source_review_ids": review_ids,
        "result_id": result_id,
        "task_id": result.get("task_id"),
        "publication_id": result.get("publication_id"),
        "driver_id": synthesis.get("synthesized_by"),
        "reviewed_at": reviewed_at,
        "disposition": synthesis.get("operational_disposition"),
        "destination_class": destination,
        "destination_ref_or_none": destination_ref,
        "terminal": synthesis.get("terminal"),
        "review_synthesis": synthesis,
    }


def authority_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for result_id in _canonical_results().result_map(root):
        authority = authority_for_result(result_id, root)
        if authority is None:
            continue
        authority_id = authority.get("review_authority_id")
        if not isinstance(authority_id, str) or not authority_id:
            raise DriverFollowupError(f"{result_id}: operational review authority has no id")
        if authority_id in out:
            raise DriverFollowupError(f"duplicate operational review authority id: {authority_id}")
        out[authority_id] = authority
    return out


def review_requires_followup(review: dict[str, Any], root: Path = ROOT) -> bool:
    authority_id = review.get("review_authority_id") or review.get("review_id")
    kind = review.get("review_authority_kind", "IMMUTABLE_REVIEW")
    if kind == "REVIEW_SYNTHESIS":
        return True
    if not isinstance(authority_id, str) or not authority_id.strip():
        return True
    return authority_id.strip() not in legacy_review_ids(root)


def _bind_guard(root: Path = ROOT) -> None:
    """Bind the V1 storage primitive to canonical exact-set review authority."""

    def _guarded(review: dict[str, Any]) -> bool:
        return review_requires_followup(review, root)

    def _authority_view(_root: Path = root) -> dict[str, dict[str, Any]]:
        return authority_map(_root)

    def _result_view(_root: Path = root) -> dict[str, dict[str, Any]]:
        return _canonical_results().result_map(_root)

    _impl.review_map = _authority_view
    _impl.result_map = _result_view

    original_gate_map = getattr(_impl, "_guard_original_gate_map", _impl._gate_map)
    original_forced = getattr(_impl, "_guard_original_forced_rules", _impl._forced_gate_rules)
    _impl._guard_original_gate_map = original_gate_map
    _impl._guard_original_forced_rules = original_forced
    _impl.GATE_DECISIONS.add(EXISTING_ASSET_DECISION)

    def _guarded_gate_map(value: Any) -> dict[str, dict[str, Any]]:
        out = original_gate_map(value)
        for gate, row in out.items():
            if row.get("decision") == EXISTING_ASSET_DECISION and not row.get("evidence_refs"):
                raise DriverFollowupError(
                    f"{gate}: {EXISTING_ASSET_DECISION} requires evidence_refs"
                )
        return out

    def _guarded_forced_rules(
        review: dict[str, Any], result: dict[str, Any], gates: dict[str, dict[str, Any]]
    ) -> None:
        if review.get("destination_class") not in _canonical_results().DESTINATION_CLASSES:
            raise DriverFollowupError(
                "operational review authority has no single-valued destination_class"
            )
        if review.get("disposition") == "REQUEST_REPLICATION":
            shadow = dict(review)
            if gates["INDEPENDENT_REPLICATION"]["decision"] == EXISTING_ASSET_DECISION:
                shadow["disposition"] = "RETURN_TO_OWNER"
            original_forced(shadow, result, gates)
            if gates["INDEPENDENT_REPLICATION"]["decision"] not in {
                "REQUIRED",
                EXISTING_ASSET_DECISION,
            }:
                raise DriverFollowupError(
                    "REQUEST_REPLICATION requires a new or already-materialized "
                    "INDEPENDENT_REPLICATION control asset"
                )
            return
        original_forced(review, result, gates)

    _impl.review_requires_followup = _guarded
    _impl._gate_map = _guarded_gate_map
    _impl._forced_gate_rules = _guarded_forced_rules


def baseline_audit(root: Path = ROOT) -> list[str]:
    try:
        baseline = legacy_review_ids(root)
        current = _raw_review_map(root)
    except Exception as exc:
        return [str(exc)]
    missing = sorted(baseline - set(current))
    if missing:
        return [f"legacy review baseline IDs missing from current immutable store: {missing}"]
    return []


def audit(root: Path = ROOT) -> list[str]:
    errors = baseline_audit(root)
    if errors:
        return errors
    _bind_guard(root)
    try:
        for authority_id, authority in authority_map(root).items():
            if authority.get("review_authority_kind") not in AUTHORITY_KINDS:
                errors.append(f"{authority_id}: invalid review authority kind")
            if authority.get("destination_class") not in _canonical_results().DESTINATION_CLASSES:
                errors.append(
                    f"{authority_id}: operational review destination is unresolved; "
                    "review synthesis must single-value destination before follow-up"
                )
    except Exception as exc:
        errors.append(str(exc))
    errors.extend(_impl.audit(root))
    return errors


def state_for_review(review_id: str, root: Path = ROOT) -> dict[str, Any]:
    _bind_guard(root)
    authority = authority_map(root).get(review_id)
    if authority is not None and authority.get("destination_class") not in _canonical_results().DESTINATION_CLASSES:
        return {
            "review_id": review_id,
            "review_authority_kind": authority.get("review_authority_kind"),
            "required": True,
            "ready": False,
            "state": "REVIEW_AUTHORITY_DESTINATION_UNRESOLVED",
            "packet": None,
        }
    value = _impl.state_for_review(review_id, root)
    if authority is not None:
        value["review_authority_kind"] = authority.get("review_authority_kind")
        value["source_review_ids"] = authority.get("source_review_ids")
    return value


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
    authority = authority_map(root).get(review_id)
    if authority is None:
        raise DriverFollowupError(f"unknown operational review authority: {review_id}")
    if authority.get("destination_class") not in _canonical_results().DESTINATION_CLASSES:
        raise DriverFollowupError(
            "review synthesis must single-value destination_class before follow-up materialization"
        )
    return _impl.materialize(
        review_id=review_id,
        spec=spec,
        created_at=created_at,
        root=root,
    )


# The primitive resolves review_map/result_map dynamically. Binding here keeps
# standalone guard use and the canonical result CLI on one authority view.
_bind_guard(ROOT)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Canonical exact-set Driver-review automatic follow-up control"
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("audit")

    state = sub.add_parser("state")
    state.add_argument("--review-authority-id", "--review-id", dest="review_id", required=True)

    mat = sub.add_parser("materialize")
    mat.add_argument("--review-authority-id", "--review-id", dest="review_id", required=True)
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
            for authority in authority_map(ROOT).values()
            if review_requires_followup(authority, ROOT)
        )
        print(
            "PASS: exact-set Driver follow-up barrier valid "
            f"({len(legacy_review_ids(ROOT))} frozen legacy review(s), "
            f"{governed} governed operational authority record(s), "
            f"{len(_impl.iter_packets(ROOT))} packet(s))."
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
