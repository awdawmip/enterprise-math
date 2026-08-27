#!/usr/bin/env python3
"""Fail-closed operational reducer for multiple Driver-review evidence.

``research_review_evidence`` owns immutable storage and whole-repository audit.
This module is the runtime-facing reducer: it validates only the exact evidence
objects that could affect one result, so malformed unrelated history does not
block every task while malformed current intake/pass/synthesis can never gain
operational authority before CI runs.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import research_review_evidence as store

ROOT = Path(__file__).resolve().parent


class ReviewControlError(ValueError):
    pass


# Keep the multiplicity probe on the same canonical immutable review store.
reviews_for_result = store.reviews_for_result


def _string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ReviewControlError(f"{label} is required")
    return value.strip()


def _review_ids(result_id: str, root: Path) -> tuple[list[dict[str, Any]], list[str]]:
    reviews = store.reviews_for_result(result_id, root)
    ids: list[str] = []
    for review in reviews:
        review_id = _string(review.get("review_id"), "review_id")
        if review.get("result_id") != result_id:
            raise ReviewControlError("review result_id mismatch")
        disposition = review.get("disposition")
        if disposition not in store.ALL_DISPOSITIONS:
            raise ReviewControlError(f"review {review_id} has invalid disposition")
        ids.append(review_id)
    if len(ids) != len(set(ids)):
        raise ReviewControlError("duplicate review_id in current review set")
    return reviews, ids


def _validate_intake(
    intake: dict[str, Any], result_id: str, review_ids: list[str], digest: str
) -> str:
    if intake.get("schema") != store.INTAKE_SCHEMA:
        raise ReviewControlError("current review intake has wrong schema")
    iid = _string(intake.get("intake_id"), "intake_id")
    if intake.get("result_id") != result_id:
        raise ReviewControlError("current review intake result_id mismatch")
    if sorted(intake.get("review_ids") or []) != sorted(review_ids):
        raise ReviewControlError("current review intake does not pin exact review set")
    if intake.get("review_set_sha256") != digest:
        raise ReviewControlError("current review intake hash mismatch")
    if intake.get("latest_review_wins") is not False:
        raise ReviewControlError("current review intake enables latest-review-wins")
    if intake.get("all_reviews_retained") is not True:
        raise ReviewControlError("current review intake does not retain all reviews")
    if intake.get("working_truth_granted") is not False:
        raise ReviewControlError("review intake cannot grant Working Truth")
    if intake.get("canonical_promotion_granted") is not False:
        raise ReviewControlError("review intake cannot grant canonical promotion")
    _string(intake.get("opened_by"), "opened_by")
    return iid


def _current_intake(
    result_id: str, review_ids: list[str], digest: str, root: Path
) -> dict[str, Any] | None:
    matches = [
        item
        for item in store.intakes(root).values()
        if item.get("result_id") == result_id
        and item.get("review_set_sha256") == digest
        and sorted(item.get("review_ids") or []) == sorted(review_ids)
    ]
    if len(matches) > 1:
        raise ReviewControlError("multiple exact review intakes for current evidence set")
    if not matches:
        return None
    _validate_intake(matches[0], result_id, review_ids, digest)
    return matches[0]


def _validated_passes(
    intake_id: str,
    result_id: str,
    review_ids: list[str],
    digest: str,
    root: Path,
) -> dict[int, dict[str, Any]]:
    rows = store.reference_passes(root).get(intake_id, [])
    by_number: dict[int, dict[str, Any]] = {}
    for row in rows:
        if row.get("schema") != store.PASS_SCHEMA:
            raise ReviewControlError("current review reference pass has wrong schema")
        number = row.get("pass_number")
        if type(number) is not int or number not in store.PASS_KINDS:
            raise ReviewControlError("current review reference pass number invalid")
        if number in by_number:
            raise ReviewControlError(f"duplicate current review reference pass {number}")
        if row.get("pass_kind") != store.PASS_KINDS[number]:
            raise ReviewControlError("current review reference pass kind mismatch")
        if row.get("intake_id") != intake_id or row.get("result_id") != result_id:
            raise ReviewControlError("current review reference pass authority mismatch")
        if sorted(row.get("review_ids") or []) != sorted(review_ids):
            raise ReviewControlError("current review reference pass review set mismatch")
        if row.get("review_set_sha256") != digest:
            raise ReviewControlError("current review reference pass hash mismatch")
        if row.get("independence_status") not in store.INDEPENDENCE:
            raise ReviewControlError("current review reference pass independence invalid")
        _string(row.get("reviewer_id"), "reviewer_id")
        _string(row.get("finding"), "finding")
        if row.get("working_truth_granted") is not False:
            raise ReviewControlError("reference pass cannot grant Working Truth")
        if row.get("canonical_promotion_granted") is not False:
            raise ReviewControlError("reference pass cannot grant canonical promotion")
        by_number[number] = row
    if 2 in by_number and 1 not in by_number:
        raise ReviewControlError("reference pass 2 exists without pass 1")
    return by_number


def _current_synthesis(
    intake_id: str,
    result_id: str,
    review_ids: list[str],
    digest: str,
    root: Path,
) -> dict[str, Any] | None:
    matches = [
        item
        for item in store.syntheses(root).values()
        if item.get("intake_id") == intake_id
        and item.get("review_set_sha256") == digest
    ]
    if len(matches) > 1:
        raise ReviewControlError("multiple review syntheses for current evidence set")
    if not matches:
        return None
    synthesis = matches[0]
    if synthesis.get("schema") != store.SYNTH_SCHEMA:
        raise ReviewControlError("current review synthesis has wrong schema")
    if synthesis.get("result_id") != result_id:
        raise ReviewControlError("current review synthesis result_id mismatch")
    if sorted(synthesis.get("review_ids") or []) != sorted(review_ids):
        raise ReviewControlError("current review synthesis review set mismatch")
    disposition = synthesis.get("operational_disposition")
    if disposition not in store.ALL_DISPOSITIONS:
        raise ReviewControlError("current review synthesis disposition invalid")
    if synthesis.get("terminal") is not (disposition in store.TERMINAL_DISPOSITIONS):
        raise ReviewControlError("current review synthesis terminal bit mismatch")
    if synthesis.get("latest_review_wins") is not False:
        raise ReviewControlError("current review synthesis enables latest-review-wins")
    if synthesis.get("all_reviews_retained") is not True:
        raise ReviewControlError("current review synthesis does not retain all reviews")
    if synthesis.get("working_truth_granted") is not False:
        raise ReviewControlError("review synthesis cannot grant Working Truth")
    if synthesis.get("canonical_promotion_granted") is not False:
        raise ReviewControlError("review synthesis cannot grant canonical promotion")
    _string(synthesis.get("synthesized_by"), "synthesized_by")
    _string(synthesis.get("rationale"), "rationale")
    return synthesis


def state(result_id: str, root: Path = ROOT) -> dict[str, Any]:
    """Derive runtime control for exactly one result's immutable review set."""
    rid = _string(result_id, "result_id")
    reviews, review_ids = _review_ids(rid, root)
    if not reviews:
        return {"result_id": rid, "review_state": "NO_REVIEW", "review_ids": [], "terminal": False}
    if len(reviews) == 1:
        disposition = reviews[0]["disposition"]
        return {
            "result_id": rid,
            "review_state": "SINGLE_REVIEW_FLOW",
            "review_ids": review_ids,
            "review": reviews[0],
            "operational_disposition": disposition,
            "terminal": disposition in store.TERMINAL_DISPOSITIONS,
        }

    digest = store.review_set_hash(review_ids)
    base = {
        "result_id": rid,
        "review_ids": review_ids,
        "review_set_sha256": digest,
        "terminal": False,
    }
    intake = _current_intake(rid, review_ids, digest, root)
    if intake is None:
        return {**base, "review_state": "AWAITING_REVIEW_INTAKE", "intake_id": None}
    iid = str(intake["intake_id"])
    passes = _validated_passes(iid, rid, review_ids, digest, root)
    if 1 not in passes:
        return {**base, "review_state": "AWAITING_REVIEW_REFERENCE_PASS_1", "intake_id": iid}
    if 2 not in passes:
        return {**base, "review_state": "AWAITING_REVIEW_REFERENCE_PASS_2", "intake_id": iid}
    synthesis = _current_synthesis(iid, rid, review_ids, digest, root)
    if synthesis is None:
        return {**base, "review_state": "AWAITING_REVIEW_SYNTHESIS", "intake_id": iid}
    disposition = synthesis["operational_disposition"]
    terminal = disposition in store.TERMINAL_DISPOSITIONS
    return {
        **base,
        "review_state": "REVIEW_SYNTHESIS_TERMINAL" if terminal else "REVIEW_SYNTHESIS_NONTERMINAL",
        "intake_id": iid,
        "synthesis": synthesis,
        "operational_disposition": disposition,
        "terminal": terminal,
    }
