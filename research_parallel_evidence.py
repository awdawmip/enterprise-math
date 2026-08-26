#!/usr/bin/env python3
"""Parallel publication/result evidence registry and two-pass synthesis reducer.

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
        by_number: dict[int, dict[str, Any]] = {}
        for row in rows:
            prefix = row.get("_path", "<reference-pass>")
            try:
                if row.get("schema") != PASS_SCHEMA:
                    raise ParallelEvidenceError("wrong reference pass schema")
                number = row.get("pass_number")
                if type(number) is not int or number not in PASS_KINDS:
                    raise ParallelEvidenceError("pass_number must be 1 or 2")
                if number in by_number:
                    raise ParallelEvidenceError(f"duplicate pass_number {number}")
                if row.get("pass_kind") != PASS_KINDS[number]:
                    raise ParallelEvidenceError(f"pass {number} has wrong pass_kind")
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
                by_number[number] = row
            except Exception as exc:
                errors.append(f"{prefix}: {exc}")

    for sid, synth in synth_map.items():
        prefix = synth.get("_path", sid)
        try:
            if synth.get("schema") != SYNTH_SCHEMA:
                raise ParallelEvidenceError("wrong synthesis schema")
            _valid_id(sid, "synthesis_id")
            iid = _valid_id(synth.get("intake_id"), "intake_id")
            intake = intake_map.get(iid)
            if intake is None:
                raise ParallelEvidenceError("synthesis references unknown intake")
            if synth.get("task_id") != intake.get("task_id"):
                raise ParallelEvidenceError("synthesis task_id mismatch")
            if synth.get("evidence_set_sha256") != intake.get("evidence_set_sha256"):
                raise ParallelEvidenceError("synthesis evidence set differs from intake")
            pids = _string_list(synth.get("publication_ids"), "publication_ids")
            rids = _string_list(synth.get("result_ids"), "result_ids")
            if sorted(pids) != sorted(intake["publication_ids"]) or sorted(rids) != sorted(intake["result_ids"]):
                raise ParallelEvidenceError("synthesis must cover the exact intake evidence set")
            rows = passes.get(iid, [])
            by_number = {row.get("pass_number"): row for row in rows}
            if 1 not in by_number or 2 not in by_number:
                raise ParallelEvidenceError("synthesis requires both reference passes")
            pass_ids = _string_list(synth.get("reference_pass_ids"), "reference_pass_ids")
            actual_ids = [by_number[1].get("pass_id"), by_number[2].get("pass_id")]
            if sorted(pass_ids) != sorted(actual_ids):
                raise ParallelEvidenceError("synthesis reference_pass_ids do not match pass 1/2")
            if synth.get("disposition") not in SYNTHESIS_DISPOSITIONS:
                raise ParallelEvidenceError("invalid synthesis disposition")
            operational = synth.get("operational_publication_id")
            if operational is not None and operational not in pids:
                raise ParallelEvidenceError("operational_publication_id is outside synthesis publication set")
            if synth.get("task_terminal") is True and len(rids) >= 2:
                for rid in rids:
                    if not reviews.get(rid):
                        raise ParallelEvidenceError(f"terminal synthesis requires at least one review for result {rid}")
            if synth.get("working_truth_granted") is not False or synth.get("canonical_promotion_granted") is not False:
                raise ParallelEvidenceError("synthesis cannot grant truth/promotion")
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
                pass_ids = {item.get("pass_number"): item.get("pass_id") for item in passes.get(iid, [])}
                if process.get("pass_1_id") != pass_ids.get(1) or process.get("pass_2_id") != pass_ids.get(2):
                    errors.append(f"research_task_publication_resolutions.json: {row.get('task_id')}: inline reference pass IDs are not backed by immutable pass records")
                sid = row.get("parallel_synthesis_id")
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
    rows = reference_passes(root).get(intake["intake_id"], [])
    numbers = {row.get("pass_number") for row in rows}
    if 1 not in numbers:
        phase = "AWAITING_REFERENCE_PASS_1"
    elif 2 not in numbers:
        phase = "AWAITING_REFERENCE_PASS_2"
    else:
        synth = next(
            (item for item in syntheses(root).values() if item.get("intake_id") == intake["intake_id"] and item.get("evidence_set_sha256") == target_hash),
            None,
        )
        phase = "AWAITING_SYNTHESIS" if synth is None else ("PARALLEL_SYNTHESIS_TERMINAL" if synth.get("task_terminal") is True else "PARALLEL_SYNTHESIS_NONTERMINAL")
    return {
        "task_id": task_id,
        "publication_id": publication_id,
        "parallel_state": phase,
        "result_ids": rids,
        "intake_id": intake["intake_id"],
        "evidence_set_sha256": target_hash,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise Math parallel evidence two-pass synthesis")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("audit")
    status = sub.add_parser("state")
    status.add_argument("--task-id", required=True)
    status.add_argument("--publication-id")
    args = parser.parse_args()
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
