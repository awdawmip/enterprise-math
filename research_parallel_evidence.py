#!/usr/bin/env python3
"""Parallel publication/result evidence registry and exact-set synthesis reducer.

This is a control-plane checker/reducer. It deliberately preserves every
publication/result/review artifact and only single-values operational control at
an explicit synthesis boundary.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
INTAKE_ROOT = ROOT / "research_parallel_intakes"
PASS_ROOT = ROOT / "research_parallel_reference_passes"
SYNTH_ROOT = ROOT / "research_parallel_syntheses"

INTAKE_SCHEMA = "ENTERPRISE_MATH_PARALLEL_EVIDENCE_INTAKE_V1"
PASS_SCHEMA = "ENTERPRISE_MATH_PARALLEL_REFERENCE_PASS_V1"
SYNTH_SCHEMA = "ENTERPRISE_MATH_PARALLEL_SYNTHESIS_V1"

INTAKE_MODES = {
    "PARALLEL_PUBLICATIONS",
    "PARALLEL_RESULTS",
    "MIXED_PARALLEL_EVIDENCE",
}
PASS_KINDS = {
    1: "SEMANTIC_EVIDENCE_CROSSCHECK",
    2: "ADVERSARIAL_CONTROL_CROSSCHECK",
}
# Historical labels remain readable; a number identifies a reference record,
# not a mandated method, sequence, independence claim, or sufficiency threshold.
INDEPENDENCE = {
    "CLEAN_INDEPENDENT_CONTEXT",
    "SHARED_CONTROL_CONTEXT_DISCLOSED",
    "NOT_INDEPENDENT",
    "NOT_APPLICABLE",
}
SYNTHESIS_DISPOSITIONS = {
    "KEEP_PARALLEL",
    "MERGE_TO_NEW_GENERATION",
    "SPLIT_TO_TYPED_TASKS",
    "RESELECT_OPERATIONAL_WITHOUT_REJECTING_OTHERS",
    "CLASSIFY_CONTRADICTION_AND_KEEP_ALL",
    "RETURN_FOR_MORE_RESEARCH",
}
ID_RE = re.compile(r"^[A-Za-z0-9._-]+$")
EM_ID_RE = re.compile(r"^EM-[A-Z0-9]+-(?:[0-9]{2}|[A-Z0-9]{4,8})$")


class ParallelEvidenceError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ParallelEvidenceError(f"{path}: JSON root must be an object")
    return value


def _iter(root: Path, pattern: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    if not root.exists():
        return out
    for path in sorted(root.glob(pattern)):
        value = _load(path)
        value["_path"] = path.relative_to(ROOT).as_posix()
        out.append(value)
    return out


def publications(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    directory = root / "research_task_records"
    if not directory.exists():
        return out
    for path in sorted(directory.glob("*/*.json")):
        item = json.loads(path.read_text(encoding="utf-8"))
        pid = item.get("publication_id")
        if isinstance(pid, str) and pid:
            if pid in out:
                raise ParallelEvidenceError(f"duplicate publication_id: {pid}")
            out[pid] = item
    return out


def results(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    directory = root / "research_result_records"
    if not directory.exists():
        return out
    for path in sorted(directory.glob("*/*.json")):
        item = json.loads(path.read_text(encoding="utf-8"))
        rid = item.get("result_id")
        if isinstance(rid, str) and rid:
            if rid in out:
                raise ParallelEvidenceError(f"duplicate result_id: {rid}")
            out[rid] = item
    return out


def result_reviews(root: Path = ROOT) -> dict[str, list[dict[str, Any]]]:
    out: dict[str, list[dict[str, Any]]] = {}
    directory = root / "research_result_reviews"
    if not directory.exists():
        return out
    for path in sorted(directory.glob("*/*.json")):
        item = json.loads(path.read_text(encoding="utf-8"))
        rid = item.get("result_id")
        if isinstance(rid, str) and rid:
            out.setdefault(rid, []).append(item)
    return out


def intakes(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    directory = root / "research_parallel_intakes"
    if not directory.exists():
        return out
    for path in sorted(directory.glob("*/*.json")):
        item = json.loads(path.read_text(encoding="utf-8"))
        iid = item.get("intake_id")
        if isinstance(iid, str) and iid:
            if iid in out:
                raise ParallelEvidenceError(f"duplicate intake_id: {iid}")
            item["_path"] = path.relative_to(root).as_posix()
            out[iid] = item
    return out


def reference_passes(root: Path = ROOT) -> dict[str, list[dict[str, Any]]]:
    out: dict[str, list[dict[str, Any]]] = {}
    directory = root / "research_parallel_reference_passes"
    if not directory.exists():
        return out
    for path in sorted(directory.glob("*/*.json")):
        item = json.loads(path.read_text(encoding="utf-8"))
        iid = item.get("intake_id")
        if isinstance(iid, str) and iid:
            item["_path"] = path.relative_to(root).as_posix()
            out.setdefault(iid, []).append(item)
    return out


def syntheses(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    directory = root / "research_parallel_syntheses"
    if not directory.exists():
        return out
    for path in sorted(directory.glob("*/*.json")):
        item = json.loads(path.read_text(encoding="utf-8"))
        sid = item.get("synthesis_id")
        if isinstance(sid, str) and sid:
            if sid in out:
                raise ParallelEvidenceError(f"duplicate synthesis_id: {sid}")
            item["_path"] = path.relative_to(root).as_posix()
            out[sid] = item
    return out


def evidence_hash(publication_ids: list[str], result_ids: list[str]) -> str:
    payload = {
        "publication_ids": sorted(publication_ids),
        "result_ids": sorted(result_ids),
    }
    raw = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _string_list(value: Any, label: str) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(x, str) or not x for x in value):
        raise ParallelEvidenceError(f"{label} must be a string list")
    if len(value) != len(set(value)):
        raise ParallelEvidenceError(f"{label} contains duplicates")
    return value


def _valid_id(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value or not ID_RE.fullmatch(value):
        raise ParallelEvidenceError(f"{label} is invalid")
    return value


def _validated_pass_map(
    intake: dict[str, Any], rows: list[dict[str, Any]]
) -> dict[str, dict[str, Any]]:
    by_id: dict[str, dict[str, Any]] = {}
    numbers: set[int] = set()
    for row in rows:
        if row.get("schema") != PASS_SCHEMA:
            raise ParallelEvidenceError("wrong reference pass schema")
        pass_id = _valid_id(row.get("pass_id"), "pass_id")
        if pass_id in by_id:
            raise ParallelEvidenceError(f"duplicate pass_id {pass_id}")
        if row.get("intake_id") != intake.get("intake_id"):
            raise ParallelEvidenceError("reference pass intake_id mismatch")
        if row.get("task_id") != intake.get("task_id"):
            raise ParallelEvidenceError("reference pass task_id mismatch")
        number = row.get("pass_number")
        if type(number) is not int or number < 1:
            raise ParallelEvidenceError("pass_number must be a positive integer label")
        if number in numbers:
            raise ParallelEvidenceError(f"duplicate pass_number {number}")
        _valid_id(row.get("pass_kind"), "pass_kind")
        if row.get("evidence_set_sha256") != intake.get("evidence_set_sha256"):
            raise ParallelEvidenceError("reference pass evidence set differs from intake")
        if sorted(_string_list(row.get("publication_ids"), "publication_ids")) != sorted(intake["publication_ids"]):
            raise ParallelEvidenceError("reference pass publication set differs from intake")
        if sorted(_string_list(row.get("result_ids"), "result_ids")) != sorted(intake["result_ids"]):
            raise ParallelEvidenceError("reference pass result set differs from intake")
        reviewer = row.get("reviewer_id")
        if not isinstance(reviewer, str) or not EM_ID_RE.fullmatch(reviewer.strip().upper()):
            raise ParallelEvidenceError("reviewer_id must be a valid EM execution identity")
        if row.get("independence_status") not in INDEPENDENCE:
            raise ParallelEvidenceError("invalid independence_status")
        if not isinstance(row.get("findings_summary"), str) or not row["findings_summary"].strip():
            raise ParallelEvidenceError("findings_summary missing")
        if not isinstance(row.get("recommendation"), str) or not row["recommendation"].strip():
            raise ParallelEvidenceError("recommendation missing")
        if row.get("working_truth_granted") is not False or row.get("canonical_promotion_granted") is not False:
            raise ParallelEvidenceError("reference pass cannot grant truth/promotion")
        numbers.add(number)
        by_id[pass_id] = row
    return by_id


def _validate_synthesis(
    synth: dict[str, Any], intake: dict[str, Any], passes: dict[str, dict[str, Any]],
    *, require_current_references: bool = False,
) -> None:
    if synth.get("schema") != SYNTH_SCHEMA:
        raise ParallelEvidenceError("wrong synthesis schema")
    _valid_id(synth.get("synthesis_id"), "synthesis_id")
    if synth.get("intake_id") != intake.get("intake_id"):
        raise ParallelEvidenceError("synthesis intake_id mismatch")
    if synth.get("task_id") != intake.get("task_id"):
        raise ParallelEvidenceError("synthesis task_id mismatch")
    if synth.get("evidence_set_sha256") != intake.get("evidence_set_sha256"):
        raise ParallelEvidenceError("synthesis evidence set differs from intake")
    pids = _string_list(synth.get("publication_ids"), "publication_ids")
    rids = _string_list(synth.get("result_ids"), "result_ids")
    if sorted(pids) != sorted(intake["publication_ids"]) or sorted(rids) != sorted(intake["result_ids"]):
        raise ParallelEvidenceError("synthesis must cover the exact intake evidence set")
    pass_ids = _string_list(synth.get("reference_pass_ids"), "reference_pass_ids")
    if not set(pass_ids) <= set(passes):
        raise ParallelEvidenceError("synthesis references an unknown reference pass")
    if require_current_references and set(pass_ids) != set(passes):
        raise ParallelEvidenceError("synthesis reference_pass_ids must match the complete recorded reference set")
    expected_status = "RECORDED" if pass_ids else "NOT_PERFORMED"
    # Existing two-pass records omit this field. Empty new reference sets must
    # explicitly disclose that no reference review took place.
    if not pass_ids or "reference_review_status" in synth:
        if synth.get("reference_review_status") != expected_status:
            raise ParallelEvidenceError(f"synthesis reference_review_status must be {expected_status}")
    if synth.get("disposition") not in SYNTHESIS_DISPOSITIONS:
        raise ParallelEvidenceError("invalid synthesis disposition")
    operational = synth.get("operational_publication_id")
    if operational is not None and operational not in pids:
        raise ParallelEvidenceError("operational_publication_id is outside synthesis publication set")
    if synth.get("working_truth_granted") is not False or synth.get("canonical_promotion_granted") is not False:
        raise ParallelEvidenceError("synthesis cannot grant truth/promotion")


def intake_state(intake: dict[str, Any], root: Path = ROOT) -> dict[str, Any]:
    """Read one exact intake without imposing a reference count or method order.

    This is evidence state only. Result-review authority and terminal control
    dispositions are still checked by the existing Result/cohort consumers.
    """
    if intake.get("schema") != INTAKE_SCHEMA:
        raise ParallelEvidenceError("wrong intake schema")
    _valid_id(intake.get("intake_id"), "intake_id")
    _valid_id(intake.get("task_id"), "task_id")
    pids = _string_list(intake.get("publication_ids"), "publication_ids")
    rids = _string_list(intake.get("result_ids"), "result_ids")
    if evidence_hash(pids, rids) != intake.get("evidence_set_sha256"):
        raise ParallelEvidenceError("evidence_set_sha256 mismatch")
    rows = reference_passes(root).get(intake["intake_id"], [])
    passes = _validated_pass_map(intake, rows)
    current: list[dict[str, Any]] = []
    stale_ids: list[str] = []
    for candidate in syntheses(root).values():
        if (candidate.get("intake_id") != intake["intake_id"]
                or candidate.get("evidence_set_sha256") != intake["evidence_set_sha256"]):
            continue
        # A historical snapshot remains valid when a later reference arrives.
        # Only a snapshot covering the complete current set can control now.
        _validate_synthesis(candidate, intake, passes)
        if set(candidate["reference_pass_ids"]) == set(passes):
            current.append(candidate)
        else:
            stale_ids.append(candidate["synthesis_id"])
    if len(current) > 1:
        raise ParallelEvidenceError("multiple syntheses claim the same current reference snapshot")
    synth = current[0] if current else None
    phase = "AWAITING_SYNTHESIS" if synth is None else (
        "PARALLEL_SYNTHESIS_TERMINAL" if synth.get("task_terminal") is True
        else "PARALLEL_SYNTHESIS_NONTERMINAL"
    )
    return {
        "parallel_state": phase,
        "synthesis": synth,
        "reference_pass_ids": sorted(passes),
        "reference_pass_count": len(passes),
        "reference_review_status": "RECORDED" if passes else "NOT_PERFORMED",
        "stale_synthesis_ids": sorted(stale_ids),
    }


def write_synthesis(record: dict[str, Any], root: Path = ROOT) -> Path:
    """Append an exact-current synthesis through the existing immutable writer.

    Historical audit cannot reconstruct which references existed at a past
    write. This public writer checks the complete actual set before and after
    exclusive creation, and rolls back only its own unchanged bytes on failure.
    """
    from control_plane import immutable_write_transaction as transaction

    sid = _valid_id(record.get("synthesis_id"), "synthesis_id")
    task_id = _valid_id(record.get("task_id"), "task_id")
    iid = _valid_id(record.get("intake_id"), "intake_id")

    def validate_current() -> list[str]:
        try:
            intake = intakes(root).get(iid)
            if intake is None:
                raise ParallelEvidenceError("synthesis references unknown intake")
            if evidence_hash(intake["publication_ids"], intake["result_ids"]) != intake.get("evidence_set_sha256"):
                raise ParallelEvidenceError("evidence_set_sha256 mismatch")
            pass_map = _validated_pass_map(intake, reference_passes(root).get(iid, []))
            _validate_synthesis(record, intake, pass_map, require_current_references=True)
            pubs, source_results = publications(root), results(root)
            for pid in record["publication_ids"]:
                if pid not in pubs or pubs[pid].get("task_id") != task_id:
                    raise ParallelEvidenceError(f"unknown or cross-task publication {pid}")
            for rid in record["result_ids"]:
                source = source_results.get(rid)
                if (source is None or source.get("task_id") != task_id
                        or source.get("publication_id") not in record["publication_ids"]):
                    raise ParallelEvidenceError(f"unknown or out-of-scope result {rid}")
            intake_state(intake, root)
            if record.get("task_terminal") is True:
                reviews = result_reviews(root)
                for rid in record["result_ids"]:
                    if not reviews.get(rid):
                        raise ParallelEvidenceError(f"terminal synthesis requires at least one review for result {rid}")
            return []
        except Exception as exc:
            return [str(exc)]

    errors = validate_current()
    if errors:
        raise ParallelEvidenceError("; ".join(errors))
    path = root / "research_parallel_syntheses" / task_id / f"{sid}.json"
    try:
        transaction.commit([transaction.PlannedFile(path, transaction.json_bytes(record))],
                           postcheck=validate_current)
    except transaction.ImmutableWriteTransactionError as exc:
        raise ParallelEvidenceError(str(exc)) from exc
    return path


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        pubs = publications(root)
        res = results(root)
        reviews = result_reviews(root)
        intake_map = intakes(root)
        passes = reference_passes(root)
        synth_map = syntheses(root)
    except Exception as exc:
        return [str(exc)]

    for iid, intake in intake_map.items():
        prefix = intake.get("_path", iid)
        try:
            if intake.get("schema") != INTAKE_SCHEMA:
                raise ParallelEvidenceError("wrong intake schema")
            _valid_id(iid, "intake_id")
            task_id = _valid_id(intake.get("task_id"), "task_id")
            mode = intake.get("mode")
            if mode not in INTAKE_MODES:
                raise ParallelEvidenceError("invalid intake mode")
            pids = _string_list(intake.get("publication_ids"), "publication_ids")
            rids = _string_list(intake.get("result_ids"), "result_ids")
            if mode == "PARALLEL_PUBLICATIONS" and len(pids) < 2:
                raise ParallelEvidenceError("PARALLEL_PUBLICATIONS requires at least two publication_ids")
            if mode == "PARALLEL_RESULTS" and len(rids) < 2:
                raise ParallelEvidenceError("PARALLEL_RESULTS requires at least two result_ids")
            if mode == "MIXED_PARALLEL_EVIDENCE" and (not pids or not rids or len(pids) + len(rids) < 2):
                raise ParallelEvidenceError("MIXED_PARALLEL_EVIDENCE requires publication and result evidence")
            if evidence_hash(pids, rids) != intake.get("evidence_set_sha256"):
                raise ParallelEvidenceError("evidence_set_sha256 mismatch")
            for pid in pids:
                item = pubs.get(pid)
                if item is None:
                    raise ParallelEvidenceError(f"unknown publication_id {pid}")
                if item.get("task_id") != task_id:
                    raise ParallelEvidenceError(f"publication {pid} belongs to another task")
            for rid in rids:
                item = res.get(rid)
                if item is None:
                    raise ParallelEvidenceError(f"unknown result_id {rid}")
                if item.get("task_id") != task_id:
                    raise ParallelEvidenceError(f"result {rid} belongs to another task")
                if pids and item.get("publication_id") not in pids:
                    raise ParallelEvidenceError(f"result {rid} references publication outside intake")
            if intake.get("dispatch_authority_unchanged") is not True:
                raise ParallelEvidenceError("intake must state dispatch_authority_unchanged=true")
            if not isinstance(intake.get("opened_by"), str) or not intake["opened_by"]:
                raise ParallelEvidenceError("opened_by missing")
            if intake.get("working_truth_granted") is not False:
                raise ParallelEvidenceError("intake cannot grant Working Truth")
            if intake.get("canonical_promotion_granted") is not False:
                raise ParallelEvidenceError("intake cannot grant canonical promotion")
        except Exception as exc:
            errors.append(f"{prefix}: {exc}")

    for iid, rows in passes.items():
        intake = intake_map.get(iid)
        if intake is None:
            errors.append(f"parallel reference passes for unknown intake {iid}")
            continue
        try:
            _validated_pass_map(intake, rows)
        except Exception as exc:
            errors.append(f"parallel reference passes for {iid}: {exc}")

    for sid, synth in synth_map.items():
        prefix = synth.get("_path", sid)
        try:
            iid = _valid_id(synth.get("intake_id"), "intake_id")
            intake = intake_map.get(iid)
            if intake is None:
                raise ParallelEvidenceError("synthesis references unknown intake")
            pass_map = _validated_pass_map(intake, passes.get(iid, []))
            _validate_synthesis(synth, intake, pass_map)
            if synth.get("task_terminal") is True and len(synth["result_ids"]) >= 2:
                for rid in synth["result_ids"]:
                    if not reviews.get(rid):
                        raise ParallelEvidenceError(f"terminal synthesis requires at least one review for result {rid}")

        except Exception as exc:
            errors.append(f"{prefix}: {exc}")

    resolution_path = root / "research_task_publication_resolutions.json"
    if resolution_path.exists():
        try:
            resolution = json.loads(resolution_path.read_text(encoding="utf-8"))
            for row in resolution.get("resolutions", []):
                iid = row.get("parallel_intake_id")
                if not iid:
                    continue
                intake = intake_map.get(iid)
                if intake is None:
                    errors.append(f"research_task_publication_resolutions.json: {row.get('task_id')}: missing parallel intake {iid}")
                    continue
                retained = row.get("retained_parallel_publication_ids", [])
                if sorted(retained) != sorted(intake.get("publication_ids", [])):
                    errors.append(f"research_task_publication_resolutions.json: {row.get('task_id')}: retained publication set differs from parallel intake")
                process = row.get("reference_process", {})
                if not isinstance(process, dict):
                    raise ParallelEvidenceError("reference_process must be an object")
                by_number = {item.get("pass_number"): item.get("pass_id") for item in passes.get(iid, [])}
                # Legacy slots are aliases only. New projections use the whole
                # list so a third or nonconsecutive reference is never lost.
                for number in (1, 2):
                    key = f"pass_{number}_id"
                    if key in process and process[key] != by_number.get(number):
                        errors.append(f"research_task_publication_resolutions.json: {row.get('task_id')}: inline reference pass IDs are not backed by immutable pass records")
                actual_ids = set(by_number.values())
                sid = row.get("parallel_synthesis_id")
                snapshot_ids = (set(synth_map[sid].get("reference_pass_ids", []))
                                if sid in synth_map else actual_ids)
                if "reference_pass_ids" in process:
                    if set(_string_list(process["reference_pass_ids"], "reference_pass_ids")) != snapshot_ids:
                        errors.append(f"research_task_publication_resolutions.json: {row.get('task_id')}: inline reference set is incomplete or unbacked")
                if "reference_review_status" in process:
                    expected = "RECORDED" if snapshot_ids else "NOT_PERFORMED"
                    if process["reference_review_status"] != expected:
                        errors.append(f"research_task_publication_resolutions.json: {row.get('task_id')}: inline reference status must be {expected}")
                if sid and sid not in synth_map:
                    errors.append(f"research_task_publication_resolutions.json: {row.get('task_id')}: missing parallel synthesis {sid}")
        except Exception as exc:
            errors.append(f"research_task_publication_resolutions.json: {exc}")
    return errors


def state(task_id: str, publication_id: str | None = None, root: Path = ROOT) -> dict[str, Any]:
    res = results(root)
    matching = [
        item for item in res.values()
        if item.get("task_id") == task_id
        and (publication_id is None or item.get("publication_id") == publication_id)
    ]
    if len(matching) <= 1:
        return {
            "task_id": task_id,
            "publication_id": publication_id,
            "parallel_state": "SINGLE_RESULT_FLOW",
            "result_ids": sorted(str(item.get("result_id")) for item in matching),
        }
    rids = sorted(str(item["result_id"]) for item in matching)
    pids = sorted({str(item.get("publication_id")) for item in matching if item.get("publication_id")})
    target_hash = evidence_hash(pids, rids)
    intake = next(
        (item for item in intakes(root).values() if item.get("task_id") == task_id and item.get("evidence_set_sha256") == target_hash),
        None,
    )
    if intake is None:
        return {"task_id": task_id, "publication_id": publication_id, "parallel_state": "AWAITING_PARALLEL_INTAKE", "result_ids": rids}
    evidence_state = intake_state(intake, root)
    return {
        "task_id": task_id,
        "publication_id": publication_id,
        "parallel_state": evidence_state["parallel_state"],
        "reference_pass_ids": evidence_state["reference_pass_ids"],
        "reference_pass_count": evidence_state["reference_pass_count"],
        "reference_review_status": evidence_state["reference_review_status"],
        "stale_synthesis_ids": evidence_state["stale_synthesis_ids"],
        "result_ids": rids,
        "intake_id": intake["intake_id"],
        "evidence_set_sha256": target_hash,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise Math parallel evidence exact-set synthesis")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("audit")
    status = sub.add_parser("state")
    status.add_argument("--task-id", required=True)
    status.add_argument("--publication-id")
    write = sub.add_parser("write-synthesis", help="append an exact-current immutable synthesis JSON record")
    write.add_argument("--record-file", required=True)
    args = parser.parse_args()
    if args.command == "write-synthesis":
        path = write_synthesis(_load(Path(args.record_file)))
        print(json.dumps({"saved": True, "path": path.relative_to(ROOT).as_posix()}, sort_keys=True))
        return 0
    if args.command == "audit":
        errors = audit()
        if errors:
            for error in errors:
                print("ERROR:", error)
            return 1
        print(
            f"PASS: parallel evidence valid ({len(intakes())} intake(s), "
            f"{sum(len(v) for v in reference_passes().values())} reference pass(es), "
            f"{len(syntheses())} synthesis record(s))."
        )
        return 0
    print(json.dumps(state(args.task_id, args.publication_id), ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ParallelEvidenceError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
