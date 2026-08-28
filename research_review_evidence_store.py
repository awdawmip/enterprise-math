#!/usr/bin/env python3
"""Retain multiple Driver reviews and single-value only synthesized control.

One review keeps the historical low-burden flow. Two or more immutable reviews
for the same result are evidence multiplicity, not an ordering problem: no
reviewed_at/latest-wins rule may decide task control. The exact current review set
must traverse intake -> semantic reference -> adversarial reference -> synthesis.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Any

from control_plane import research_result_records_impl as _result_contract

ROOT = Path(__file__).resolve().parent
INTAKE_SCHEMA = "ENTERPRISE_MATH_REVIEW_EVIDENCE_INTAKE_V1"
PASS_SCHEMA = "ENTERPRISE_MATH_REVIEW_REFERENCE_PASS_V1"
SYNTH_SCHEMA = "ENTERPRISE_MATH_REVIEW_SYNTHESIS_V1"
PASS_KINDS = {1: "SEMANTIC_EVIDENCE_CROSSCHECK", 2: "ADVERSARIAL_CONTROL_CROSSCHECK"}
TERMINAL_DISPOSITIONS = {"ACCEPTED", "REJECTED", "PARKED", "CLOSED", "SUPERSEDED"}
NONTERMINAL_DISPOSITIONS = {"RETURN_TO_OWNER", "REQUEST_REPLICATION", "REQUEST_REVISION"}
ALL_DISPOSITIONS = TERMINAL_DISPOSITIONS | NONTERMINAL_DISPOSITIONS
INDEPENDENCE = {"CLEAN_INDEPENDENT_CONTEXT", "SHARED_CONTROL_CONTEXT_DISCLOSED", "NOT_INDEPENDENT", "NOT_APPLICABLE"}
# Single-source the destination enum from the canonical result/review contract.
DESTINATION_CLASSES = _result_contract.DESTINATION_CLASSES


class ReviewEvidenceError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ReviewEvidenceError(f"{path}: JSON object required")
    return value


def _exclusive(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    try:
        with path.open("x", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError as exc:
        raise ReviewEvidenceError(f"immutable record already exists: {path}") from exc


def _id(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ReviewEvidenceError(f"{label} is required")
    text = value.strip()
    if any(ch not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._-" for ch in text):
        raise ReviewEvidenceError(f"{label} contains unsupported characters")
    return text


def result_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    directory = root / "research_result_records"
    if not directory.exists():
        return out
    for path in sorted(directory.glob("*/*.json")):
        item = _load(path)
        rid = item.get("result_id")
        if isinstance(rid, str) and rid:
            if rid in out:
                raise ReviewEvidenceError(f"duplicate result_id: {rid}")
            out[rid] = item
    return out


def reviews_for_result(result_id: str, root: Path = ROOT) -> list[dict[str, Any]]:
    directory = root / "research_result_reviews" / _id(result_id, "result_id")
    out: list[dict[str, Any]] = []
    seen: set[str] = set()
    if not directory.exists():
        return out
    for path in sorted(directory.glob("*.json")):
        item = _load(path)
        review_id = _id(item.get("review_id"), "review_id")
        if item.get("result_id") != result_id:
            raise ReviewEvidenceError(f"{path}: result_id mismatch")
        if review_id in seen:
            raise ReviewEvidenceError(f"duplicate review_id: {review_id}")
        seen.add(review_id)
        item["_path"] = path.relative_to(root).as_posix()
        out.append(item)
    return sorted(out, key=lambda item: str(item["review_id"]))


def review_set_hash(review_ids: list[str]) -> str:
    raw = json.dumps(sorted(review_ids), separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def intake_id(result_id: str, evidence_hash: str) -> str:
    raw = f"{result_id}\0{evidence_hash}".encode("utf-8")
    return "RVI-" + hashlib.sha256(raw).hexdigest()[:20].upper()


def pass_id(intake_id_value: str, pass_number: int, reviewer_id: str, finding: str) -> str:
    raw = f"{intake_id_value}\0{pass_number}\0{reviewer_id}\0{finding}".encode("utf-8")
    return "RVP-" + hashlib.sha256(raw).hexdigest()[:20].upper()


def synthesis_id(intake_id_value: str, disposition: str, synthesized_by: str) -> str:
    raw = f"{intake_id_value}\0{disposition}\0{synthesized_by}".encode("utf-8")
    return "RVS-" + hashlib.sha256(raw).hexdigest()[:20].upper()


def intakes(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    directory = root / "research_review_intakes"
    if not directory.exists():
        return out
    for path in sorted(directory.glob("*/*.json")):
        item = _load(path)
        iid = _id(item.get("intake_id"), "intake_id")
        if iid in out:
            raise ReviewEvidenceError(f"duplicate intake_id: {iid}")
        item["_path"] = path.relative_to(root).as_posix()
        out[iid] = item
    return out


def reference_passes(root: Path = ROOT) -> dict[str, list[dict[str, Any]]]:
    out: dict[str, list[dict[str, Any]]] = {}
    directory = root / "research_review_reference_passes"
    if not directory.exists():
        return out
    for path in sorted(directory.glob("*/*.json")):
        item = _load(path)
        iid = _id(item.get("intake_id"), "intake_id")
        item["_path"] = path.relative_to(root).as_posix()
        out.setdefault(iid, []).append(item)
    return out


def syntheses(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    directory = root / "research_review_syntheses"
    if not directory.exists():
        return out
    for path in sorted(directory.glob("*/*.json")):
        item = _load(path)
        sid = _id(item.get("synthesis_id"), "synthesis_id")
        if sid in out:
            raise ReviewEvidenceError(f"duplicate synthesis_id: {sid}")
        item["_path"] = path.relative_to(root).as_posix()
        out[sid] = item
    return out


def _current_intake(result_id: str, review_ids: list[str], root: Path) -> dict[str, Any] | None:
    digest = review_set_hash(review_ids)
    matches = [
        item for item in intakes(root).values()
        if item.get("result_id") == result_id
        and item.get("review_set_sha256") == digest
        and sorted(item.get("review_ids") or []) == sorted(review_ids)
    ]
    if len(matches) > 1:
        raise ReviewEvidenceError("multiple exact review intakes for one evidence set")
    return matches[0] if matches else None


def state(result_id: str, root: Path = ROOT) -> dict[str, Any]:
    rid = _id(result_id, "result_id")
    reviews = reviews_for_result(rid, root)
    review_ids = [str(item["review_id"]) for item in reviews]
    if not reviews:
        return {"result_id": rid, "review_state": "NO_REVIEW", "review_ids": [], "terminal": False}
    if len(reviews) == 1:
        disposition = reviews[0].get("disposition")
        return {
            "result_id": rid,
            "review_state": "SINGLE_REVIEW_FLOW",
            "review_ids": review_ids,
            "review": reviews[0],
            "operational_disposition": disposition,
            "terminal": disposition in TERMINAL_DISPOSITIONS,
        }

    digest = review_set_hash(review_ids)
    intake = _current_intake(rid, review_ids, root)
    base = {
        "result_id": rid,
        "review_ids": review_ids,
        "review_set_sha256": digest,
        "terminal": False,
    }
    if intake is None:
        return {**base, "review_state": "AWAITING_REVIEW_INTAKE", "intake_id": None}
    iid = str(intake["intake_id"])
    rows = reference_passes(root).get(iid, [])
    by_number = {row.get("pass_number"): row for row in rows}
    if 1 not in by_number:
        return {**base, "review_state": "AWAITING_REVIEW_REFERENCE_PASS_1", "intake_id": iid}
    if 2 not in by_number:
        return {**base, "review_state": "AWAITING_REVIEW_REFERENCE_PASS_2", "intake_id": iid}
    matches = [
        item for item in syntheses(root).values()
        if item.get("intake_id") == iid and item.get("review_set_sha256") == digest
    ]
    if not matches:
        return {**base, "review_state": "AWAITING_REVIEW_SYNTHESIS", "intake_id": iid}
    if len(matches) > 1:
        raise ReviewEvidenceError("multiple review syntheses for exact evidence set")
    synthesis = matches[0]
    disposition = synthesis.get("operational_disposition")
    terminal = disposition in TERMINAL_DISPOSITIONS
    return {
        **base,
        "review_state": "REVIEW_SYNTHESIS_TERMINAL" if terminal else "REVIEW_SYNTHESIS_NONTERMINAL",
        "intake_id": iid,
        "synthesis": synthesis,
        "operational_disposition": disposition,
        "terminal": terminal,
    }


def create_intake(result_id: str, opened_by: str, root: Path = ROOT) -> dict[str, Any]:
    rid = _id(result_id, "result_id")
    if rid not in result_map(root):
        raise ReviewEvidenceError("unknown result_id")
    reviews = reviews_for_result(rid, root)
    if len(reviews) < 2:
        raise ReviewEvidenceError("review intake requires at least two immutable reviews")
    review_ids = [str(item["review_id"]) for item in reviews]
    digest = review_set_hash(review_ids)
    iid = intake_id(rid, digest)
    value = {
        "schema": INTAKE_SCHEMA,
        "intake_id": iid,
        "result_id": rid,
        "review_ids": review_ids,
        "review_set_sha256": digest,
        "opened_by": _id(opened_by, "opened_by"),
        "latest_review_wins": False,
        "all_reviews_retained": True,
        "working_truth_granted": False,
        "canonical_promotion_granted": False,
    }
    _exclusive(root / "research_review_intakes" / rid / f"{iid}.json", value)
    return value


def create_reference_pass(
    intake_id_value: str,
    pass_number: int,
    reviewer_id: str,
    finding: str,
    independence_status: str,
    root: Path = ROOT,
) -> dict[str, Any]:
    iid = _id(intake_id_value, "intake_id")
    intake = intakes(root).get(iid)
    if intake is None:
        raise ReviewEvidenceError("unknown intake_id")
    if pass_number not in PASS_KINDS:
        raise ReviewEvidenceError("pass_number must be 1 or 2")
    if independence_status not in INDEPENDENCE:
        raise ReviewEvidenceError("invalid independence_status")
    if not isinstance(finding, str) or not finding.strip():
        raise ReviewEvidenceError("finding is required")
    existing = reference_passes(root).get(iid, [])
    if any(row.get("pass_number") == pass_number for row in existing):
        raise ReviewEvidenceError(f"reference pass {pass_number} already exists")
    if pass_number == 2 and not any(row.get("pass_number") == 1 for row in existing):
        raise ReviewEvidenceError("reference pass 1 must precede pass 2")
    reviewer = _id(reviewer_id, "reviewer_id")
    pid = pass_id(iid, pass_number, reviewer, finding.strip())
    value = {
        "schema": PASS_SCHEMA,
        "pass_id": pid,
        "intake_id": iid,
        "result_id": intake["result_id"],
        "review_ids": list(intake["review_ids"]),
        "review_set_sha256": intake["review_set_sha256"],
        "pass_number": pass_number,
        "pass_kind": PASS_KINDS[pass_number],
        "reviewer_id": reviewer,
        "finding": finding.strip(),
        "independence_status": independence_status,
        "working_truth_granted": False,
        "canonical_promotion_granted": False,
    }
    _exclusive(root / "research_review_reference_passes" / iid / f"{pid}.json", value)
    return value


def create_synthesis(
    intake_id_value: str,
    operational_disposition: str,
    synthesized_by: str,
    rationale: str,
    root: Path = ROOT,
    *,
    operational_destination_class: str | None = None,
    operational_destination_ref_or_none: str = "",
) -> dict[str, Any]:
    iid = _id(intake_id_value, "intake_id")
    intake = intakes(root).get(iid)
    if intake is None:
        raise ReviewEvidenceError("unknown intake_id")
    if operational_disposition not in ALL_DISPOSITIONS:
        raise ReviewEvidenceError("invalid operational_disposition")
    if not isinstance(rationale, str) or not rationale.strip():
        raise ReviewEvidenceError("rationale is required")
    if operational_destination_class is not None:
        if operational_destination_class not in DESTINATION_CLASSES:
            raise ReviewEvidenceError("invalid operational_destination_class")
        if not isinstance(operational_destination_ref_or_none, str):
            raise ReviewEvidenceError("operational_destination_ref_or_none must be a string")
    elif operational_destination_ref_or_none:
        raise ReviewEvidenceError(
            "operational_destination_ref_or_none requires operational_destination_class"
        )
    passes = reference_passes(root).get(iid, [])
    if {row.get("pass_number") for row in passes} != {1, 2}:
        raise ReviewEvidenceError("both reference passes are required before synthesis")
    for row in passes:
        if row.get("review_set_sha256") != intake.get("review_set_sha256"):
            raise ReviewEvidenceError("reference pass evidence set drift")
    author = _id(synthesized_by, "synthesized_by")
    sid = synthesis_id(iid, operational_disposition, author)
    value = {
        "schema": SYNTH_SCHEMA,
        "synthesis_id": sid,
        "intake_id": iid,
        "result_id": intake["result_id"],
        "review_ids": list(intake["review_ids"]),
        "review_set_sha256": intake["review_set_sha256"],
        "operational_disposition": operational_disposition,
        "synthesized_by": author,
        "rationale": rationale.strip(),
        "all_reviews_retained": True,
        "latest_review_wins": False,
        "terminal": operational_disposition in TERMINAL_DISPOSITIONS,
        "working_truth_granted": False,
        "canonical_promotion_granted": False,
    }
    if operational_destination_class is not None:
        value["operational_destination_class"] = operational_destination_class
        value["operational_destination_ref_or_none"] = operational_destination_ref_or_none
    _exclusive(root / "research_review_syntheses" / str(intake["result_id"]) / f"{sid}.json", value)
    return value


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        results = result_map(root)
        intake_map = intakes(root)
        passes = reference_passes(root)
        synth_map = syntheses(root)
    except Exception as exc:
        return [str(exc)]
    for iid, intake in intake_map.items():
        try:
            rid = _id(intake.get("result_id"), "result_id")
            if intake.get("schema") != INTAKE_SCHEMA:
                raise ReviewEvidenceError("wrong intake schema")
            if rid not in results:
                raise ReviewEvidenceError("intake references unknown result")
            review_ids = intake.get("review_ids")
            if not isinstance(review_ids, list) or len(review_ids) < 2 or len(set(review_ids)) != len(review_ids):
                raise ReviewEvidenceError("intake review_ids invalid")
            current_ids = [str(item["review_id"]) for item in reviews_for_result(rid, root)]
            if any(review_id not in current_ids for review_id in review_ids):
                raise ReviewEvidenceError("intake references unknown review")
            if intake.get("review_set_sha256") != review_set_hash(list(review_ids)):
                raise ReviewEvidenceError("intake review_set_sha256 mismatch")
            if intake.get("latest_review_wins") is not False or intake.get("all_reviews_retained") is not True:
                raise ReviewEvidenceError("intake multiplicity semantics invalid")
        except Exception as exc:
            errors.append(f"{iid}: {exc}")
    for iid, rows in passes.items():
        intake = intake_map.get(iid)
        if intake is None:
            errors.append(f"reference passes for unknown intake {iid}")
            continue
        numbers = [row.get("pass_number") for row in rows]
        if len(numbers) != len(set(numbers)):
            errors.append(f"{iid}: duplicate reference pass number")
        for row in rows:
            try:
                number = row.get("pass_number")
                if row.get("schema") != PASS_SCHEMA or number not in PASS_KINDS:
                    raise ReviewEvidenceError("invalid reference pass")
                if row.get("pass_kind") != PASS_KINDS[number]:
                    raise ReviewEvidenceError("reference pass kind mismatch")
                if row.get("review_set_sha256") != intake.get("review_set_sha256"):
                    raise ReviewEvidenceError("reference pass evidence set drift")
            except Exception as exc:
                errors.append(f"{row.get('_path', iid)}: {exc}")
    for sid, synthesis in synth_map.items():
        try:
            if synthesis.get("schema") != SYNTH_SCHEMA:
                raise ReviewEvidenceError("wrong synthesis schema")
            iid = _id(synthesis.get("intake_id"), "intake_id")
            intake = intake_map.get(iid)
            if intake is None:
                raise ReviewEvidenceError("synthesis references unknown intake")
            rows = passes.get(iid, [])
            if {row.get("pass_number") for row in rows} != {1, 2}:
                raise ReviewEvidenceError("synthesis lacks both reference passes")
            if synthesis.get("review_set_sha256") != intake.get("review_set_sha256"):
                raise ReviewEvidenceError("synthesis evidence set drift")
            if synthesis.get("operational_disposition") not in ALL_DISPOSITIONS:
                raise ReviewEvidenceError("invalid synthesis disposition")
            destination = synthesis.get("operational_destination_class")
            destination_ref = synthesis.get("operational_destination_ref_or_none")
            if destination is not None:
                if destination not in DESTINATION_CLASSES:
                    raise ReviewEvidenceError("invalid synthesis operational destination")
                if not isinstance(destination_ref, str):
                    raise ReviewEvidenceError("synthesis operational destination ref must be a string")
            elif destination_ref is not None:
                raise ReviewEvidenceError(
                    "synthesis destination ref cannot exist without operational destination"
                )
            if synthesis.get("latest_review_wins") is not False or synthesis.get("all_reviews_retained") is not True:
                raise ReviewEvidenceError("synthesis multiplicity semantics invalid")
        except Exception as exc:
            errors.append(f"{sid}: {exc}")
    return errors
