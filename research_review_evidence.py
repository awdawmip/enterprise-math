#!/usr/bin/env python3
"""Authoritative exact-set reducer for multiple immutable Driver reviews.

Storage/writer compatibility lives in ``control_plane.research_review_evidence_store``.
This module re-exports that append-only surface, but runtime control is reduced here
with fail-closed validation. A timestamp never selects an operational review.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from control_plane import research_review_evidence_store as _store

for _name in dir(_store):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_store, _name)

ROOT = _store.ROOT
REVIEW_SCHEMA = "ENTERPRISE_MATH_RESEARCH_RESULT_REVIEW_V1"
EM_ID_RE = re.compile(r"^EM-[A-Z0-9]+-(?:[0-9]{2}|[A-Z0-9]{4,8})$")


def _review_ids(value: Any, label: str) -> list[str]:
    if not isinstance(value, list) or len(value) < 2:
        raise ReviewEvidenceError(f"{label} must contain at least two review ids")
    out: list[str] = []
    for raw in value:
        out.append(_id(raw, label))
    if len(out) != len(set(out)):
        raise ReviewEvidenceError(f"{label} contains duplicates")
    return out


def _validate_review(row: dict[str, Any], result_id: str) -> None:
    if row.get("record_schema") != REVIEW_SCHEMA:
        raise ReviewEvidenceError("wrong Driver review schema")
    if row.get("result_id") != result_id:
        raise ReviewEvidenceError("Driver review result_id mismatch")
    _id(row.get("review_id"), "review_id")
    driver = row.get("driver_id")
    if not isinstance(driver, str) or not EM_ID_RE.fullmatch(driver.strip().upper()):
        raise ReviewEvidenceError("Driver review driver_id is not a valid EM execution identity")
    disposition = row.get("disposition")
    if disposition not in ALL_DISPOSITIONS:
        raise ReviewEvidenceError("invalid Driver review disposition")
    if row.get("terminal") is not (disposition in TERMINAL_DISPOSITIONS):
        raise ReviewEvidenceError("Driver review terminal flag mismatch")


def _validate_intake(
    intake: dict[str, Any], result_id: str, root: Path
) -> list[str]:
    if intake.get("schema") != INTAKE_SCHEMA:
        raise ReviewEvidenceError("wrong review intake schema")
    if intake.get("result_id") != result_id:
        raise ReviewEvidenceError("review intake result_id mismatch")
    review_ids = _review_ids(intake.get("review_ids"), "review_ids")
    if intake.get("review_set_sha256") != review_set_hash(review_ids):
        raise ReviewEvidenceError("review intake evidence hash mismatch")
    current_known = {
        str(item["review_id"]) for item in _store.reviews_for_result(result_id, root)
    }
    if any(review_id not in current_known for review_id in review_ids):
        raise ReviewEvidenceError("review intake references unknown immutable review")
    if intake.get("latest_review_wins") is not False:
        raise ReviewEvidenceError("review intake may not enable latest-review-wins")
    if intake.get("all_reviews_retained") is not True:
        raise ReviewEvidenceError("review intake must retain every source review")
    if intake.get("working_truth_granted") is not False:
        raise ReviewEvidenceError("review intake cannot grant Working Truth")
    if intake.get("canonical_promotion_granted") is not False:
        raise ReviewEvidenceError("review intake cannot grant canonical promotion")
    _id(intake.get("opened_by"), "opened_by")
    return review_ids


def _validate_pass(row: dict[str, Any], intake: dict[str, Any]) -> int:
    if row.get("schema") != PASS_SCHEMA:
        raise ReviewEvidenceError("wrong review reference-pass schema")
    if row.get("intake_id") != intake.get("intake_id"):
        raise ReviewEvidenceError("review reference pass intake_id mismatch")
    if row.get("result_id") != intake.get("result_id"):
        raise ReviewEvidenceError("review reference pass result_id mismatch")
    number = row.get("pass_number")
    if type(number) is not int or number not in PASS_KINDS:
        raise ReviewEvidenceError("review reference pass number must be 1 or 2")
    if row.get("pass_kind") != PASS_KINDS[number]:
        raise ReviewEvidenceError("review reference pass kind mismatch")
    review_ids = _review_ids(row.get("review_ids"), "review_ids")
    if sorted(review_ids) != sorted(_review_ids(intake.get("review_ids"), "review_ids")):
        raise ReviewEvidenceError("review reference pass does not cover exact intake reviews")
    if row.get("review_set_sha256") != intake.get("review_set_sha256"):
        raise ReviewEvidenceError("review reference pass evidence hash drift")
    reviewer = row.get("reviewer_id")
    if not isinstance(reviewer, str) or not EM_ID_RE.fullmatch(reviewer.strip().upper()):
        raise ReviewEvidenceError("review reference-pass reviewer_id is invalid")
    if row.get("independence_status") not in INDEPENDENCE:
        raise ReviewEvidenceError("invalid review reference-pass independence_status")
    if not isinstance(row.get("finding"), str) or not row["finding"].strip():
        raise ReviewEvidenceError("review reference-pass finding is required")
    if row.get("working_truth_granted") is not False:
        raise ReviewEvidenceError("review reference pass cannot grant Working Truth")
    if row.get("canonical_promotion_granted") is not False:
        raise ReviewEvidenceError("review reference pass cannot grant canonical promotion")
    _id(row.get("pass_id"), "pass_id")
    return number


def _validated_pass_map(intake: dict[str, Any], root: Path) -> dict[int, dict[str, Any]]:
    rows = _store.reference_passes(root).get(str(intake["intake_id"]), [])
    out: dict[int, dict[str, Any]] = {}
    for row in rows:
        number = _validate_pass(row, intake)
        if number in out:
            raise ReviewEvidenceError(f"duplicate review reference pass {number}")
        out[number] = row
    return out


def _validate_synthesis(
    row: dict[str, Any], intake: dict[str, Any], passes: dict[int, dict[str, Any]]
) -> str:
    if row.get("schema") != SYNTH_SCHEMA:
        raise ReviewEvidenceError("wrong review synthesis schema")
    if row.get("intake_id") != intake.get("intake_id"):
        raise ReviewEvidenceError("review synthesis intake_id mismatch")
    if row.get("result_id") != intake.get("result_id"):
        raise ReviewEvidenceError("review synthesis result_id mismatch")
    review_ids = _review_ids(row.get("review_ids"), "review_ids")
    if sorted(review_ids) != sorted(_review_ids(intake.get("review_ids"), "review_ids")):
        raise ReviewEvidenceError("review synthesis does not cover exact intake reviews")
    if row.get("review_set_sha256") != intake.get("review_set_sha256"):
        raise ReviewEvidenceError("review synthesis evidence hash drift")
    if set(passes) != {1, 2}:
        raise ReviewEvidenceError("review synthesis requires both exact-set reference passes")
    disposition = row.get("operational_disposition")
    if disposition not in ALL_DISPOSITIONS:
        raise ReviewEvidenceError("invalid synthesized operational disposition")
    author = row.get("synthesized_by")
    if not isinstance(author, str) or not EM_ID_RE.fullmatch(author.strip().upper()):
        raise ReviewEvidenceError("review synthesis synthesized_by is invalid")
    if not isinstance(row.get("rationale"), str) or not row["rationale"].strip():
        raise ReviewEvidenceError("review synthesis rationale is required")
    if row.get("latest_review_wins") is not False:
        raise ReviewEvidenceError("review synthesis may not enable latest-review-wins")
    if row.get("all_reviews_retained") is not True:
        raise ReviewEvidenceError("review synthesis must retain every source review")
    if row.get("terminal") is not (disposition in TERMINAL_DISPOSITIONS):
        raise ReviewEvidenceError("review synthesis terminal flag mismatch")
    if row.get("working_truth_granted") is not False:
        raise ReviewEvidenceError("review synthesis cannot grant Working Truth")
    if row.get("canonical_promotion_granted") is not False:
        raise ReviewEvidenceError("review synthesis cannot grant canonical promotion")
    _id(row.get("synthesis_id"), "synthesis_id")
    return str(disposition)


def state(result_id: str, root: Path = ROOT) -> dict[str, Any]:
    """Reduce current review evidence without trusting ordering or offline CI."""
    rid = _id(result_id, "result_id")
    reviews = _store.reviews_for_result(rid, root)
    for review in reviews:
        _validate_review(review, rid)
    ids = [str(item["review_id"]) for item in reviews]
    if not reviews:
        return {"result_id": rid, "review_state": "NO_REVIEW", "review_ids": [], "terminal": False}
    if len(reviews) == 1:
        disposition = reviews[0]["disposition"]
        return {
            "result_id": rid,
            "review_state": "SINGLE_REVIEW_FLOW",
            "review_ids": ids,
            "review": reviews[0],
            "operational_disposition": disposition,
            "terminal": disposition in TERMINAL_DISPOSITIONS,
        }

    digest = review_set_hash(ids)
    exact: list[dict[str, Any]] = []
    for intake in _store.intakes(root).values():
        if intake.get("result_id") != rid:
            continue
        intake_ids = _validate_intake(intake, rid, root)
        if sorted(intake_ids) == sorted(ids) and intake.get("review_set_sha256") == digest:
            exact.append(intake)
    base = {
        "result_id": rid,
        "review_ids": ids,
        "review_set_sha256": digest,
        "terminal": False,
    }
    if not exact:
        return {**base, "review_state": "AWAITING_REVIEW_INTAKE", "intake_id": None}
    if len(exact) != 1:
        raise ReviewEvidenceError("multiple exact review intakes for current evidence set")
    intake = exact[0]
    iid = str(intake["intake_id"])
    passes = _validated_pass_map(intake, root)
    if 1 not in passes:
        return {**base, "review_state": "AWAITING_REVIEW_REFERENCE_PASS_1", "intake_id": iid}
    if 2 not in passes:
        return {**base, "review_state": "AWAITING_REVIEW_REFERENCE_PASS_2", "intake_id": iid}

    matches: list[dict[str, Any]] = []
    for synthesis in _store.syntheses(root).values():
        if synthesis.get("intake_id") != iid or synthesis.get("review_set_sha256") != digest:
            continue
        _validate_synthesis(synthesis, intake, passes)
        matches.append(synthesis)
    if not matches:
        return {**base, "review_state": "AWAITING_REVIEW_SYNTHESIS", "intake_id": iid}
    if len(matches) != 1:
        raise ReviewEvidenceError("multiple review syntheses for current exact evidence set")
    synthesis = matches[0]
    disposition = str(synthesis["operational_disposition"])
    terminal = disposition in TERMINAL_DISPOSITIONS
    return {
        **base,
        "review_state": "REVIEW_SYNTHESIS_TERMINAL" if terminal else "REVIEW_SYNTHESIS_NONTERMINAL",
        "intake_id": iid,
        "synthesis": synthesis,
        "operational_disposition": disposition,
        "terminal": terminal,
    }


def audit(root: Path = ROOT) -> list[str]:
    """Audit stored history and every exact-set authority edge."""
    errors = list(_store.audit(root))
    try:
        for rid in _store.result_map(root):
            for review in _store.reviews_for_result(rid, root):
                _validate_review(review, rid)
        intake_map = _store.intakes(root)
        for iid, intake in intake_map.items():
            rid = _id(intake.get("result_id"), "result_id")
            _validate_intake(intake, rid, root)
            _validated_pass_map(intake, root)
        for sid, synthesis in _store.syntheses(root).items():
            iid = _id(synthesis.get("intake_id"), "intake_id")
            intake = intake_map.get(iid)
            if intake is None:
                raise ReviewEvidenceError(f"{sid}: synthesis references unknown intake")
            passes = _validated_pass_map(intake, root)
            _validate_synthesis(synthesis, intake, passes)
    except Exception as exc:
        errors.append(str(exc))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise Math multiple Driver-review exact-set authority")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("audit")
    status = sub.add_parser("state")
    status.add_argument("--result-id", required=True)
    args = parser.parse_args()
    if args.command == "audit":
        errors = audit()
        if errors:
            for error in errors:
                print("ERROR:", error)
            return 1
        print(
            f"PASS: review evidence valid ({len(_store.intakes())} intake(s), "
            f"{sum(len(v) for v in _store.reference_passes().values())} reference pass(es), "
            f"{len(_store.syntheses())} synthesis record(s))."
        )
        return 0
    print(json.dumps(state(args.result_id), ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ReviewEvidenceError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
