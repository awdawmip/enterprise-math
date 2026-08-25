#!/usr/bin/env python3
"""Immutable research-result and Driver-review records."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from tools import research_identity
    from tools import research_task_records
except ModuleNotFoundError:
    import research_identity  # type: ignore
    import research_task_records  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
RESULT_ROOT = ROOT / "research_result_records"
REVIEW_ROOT = ROOT / "research_result_reviews"
RESULT_SCHEMA = "ENTERPRISE_MATH_RESEARCH_RESULT_RECORD_V1"
REVIEW_SCHEMA = "ENTERPRISE_MATH_RESEARCH_RESULT_REVIEW_V1"
TERMINAL_DISPOSITIONS = {"ACCEPTED", "REJECTED", "PARKED", "CLOSED", "SUPERSEDED"}
NONTERMINAL_DISPOSITIONS = {"RETURN_TO_OWNER", "REQUEST_REPLICATION", "REQUEST_REVISION"}
ALL_DISPOSITIONS = TERMINAL_DISPOSITIONS | NONTERMINAL_DISPOSITIONS
TERMINAL_VERDICTS = {
    "SUCCESS", "PASS", "KILL", "REFUTED", "NO_GO", "BLOCKED",
    "NEGATIVE_BOUNDARY", "FORMALIZED", "INTEGRATED", "AUDIT_COMPLETE",
}
METHOD_HARVEST = {
    "GLOBAL_TOOL_FAMILY", "GLOBAL_SUBTOOL", "DOMAIN_FACADE", "DOMAIN_OPERATOR",
    "RESULT_ONLY", "CANDIDATE_NOT_TOOL", "DUPLICATE_ALIAS", "NO_TOOL_PAYLOAD",
}


class ResultRecordError(ValueError):
    pass


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _save_exclusive(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    try:
        with path.open("x", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError as exc:
        raise ResultRecordError(f"immutable record already exists: {path}") from exc


def _parse_time(value: str) -> datetime:
    dt = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _now(value: str | None) -> str:
    return (_parse_time(value) if value else datetime.now(timezone.utc)).isoformat()


def _blob(path: Path) -> str:
    return research_task_records.git_blob_sha1_bytes(path.read_bytes())


def _safe_id(value: str, label: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9._-]+", value):
        raise ResultRecordError(f"{label} contains unsupported characters")
    return value


def _legacy_task_ids(root: Path = ROOT) -> set[str]:
    scheduler = _load_json(root / "research_scheduler.json")
    return {
        item["task_id"] for item in scheduler.get("tasks", [])
        if isinstance(item, dict) and isinstance(item.get("task_id"), str)
    }


def task_exists(task_id: str, root: Path = ROOT) -> bool:
    return task_id in research_task_records.current_records(root) or task_id in _legacy_task_ids(root)


def result_id(task_id: str, return_blob: str, owner_head: str) -> str:
    raw = "\0".join((task_id, return_blob, owner_head)).encode("utf-8")
    return "RR-" + hashlib.sha256(raw).hexdigest()[:20].upper()


def review_id(result_id_value: str, driver_id: str, review_blob: str, disposition: str) -> str:
    raw = "\0".join((result_id_value, driver_id, review_blob, disposition)).encode("utf-8")
    return "DR-" + hashlib.sha256(raw).hexdigest()[:20].upper()


def iter_results(root: Path = ROOT) -> list[dict[str, Any]]:
    directory = root / "research_result_records"
    if not directory.exists():
        return []
    out = []
    for path in sorted(directory.glob("*/*.json")):
        item = _load_json(path)
        item["_record_path"] = path.relative_to(root).as_posix()
        out.append(item)
    return out


def iter_reviews(root: Path = ROOT) -> list[dict[str, Any]]:
    directory = root / "research_result_reviews"
    if not directory.exists():
        return []
    out = []
    for path in sorted(directory.glob("*/*.json")):
        item = _load_json(path)
        item["_review_path"] = path.relative_to(root).as_posix()
        out.append(item)
    return out


def result_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for item in iter_results(root):
        rid = item.get("result_id")
        if not isinstance(rid, str) or not rid:
            raise ResultRecordError("result record missing result_id")
        if rid in out:
            raise ResultRecordError(f"duplicate result_id: {rid}")
        out[rid] = item
    return out


def latest_review(result_id_value: str, root: Path = ROOT) -> dict[str, Any] | None:
    values = [item for item in iter_reviews(root) if item.get("result_id") == result_id_value]
    if not values:
        return None
    values.sort(key=lambda item: (item.get("reviewed_at", ""), item.get("review_id", "")))
    return values[-1]


def task_result_state(task_id: str, root: Path = ROOT) -> dict[str, Any] | None:
    values = [item for item in iter_results(root) if item.get("task_id") == task_id]
    if not values:
        return None
    values.sort(key=lambda item: (item.get("frozen_at", ""), item.get("result_id", "")))
    result = values[-1]
    review = latest_review(result["result_id"], root)
    if review is None:
        return {"state": "AWAITING_DRIVER_REVIEW", "result": result, "review": None, "terminal": False}
    disposition = review.get("disposition")
    return {
        "state": "TERMINAL" if disposition in TERMINAL_DISPOSITIONS else "RETURN_TO_EXECUTION",
        "result": result,
        "review": review,
        "terminal": disposition in TERMINAL_DISPOSITIONS,
    }


def freeze_result(
    *,
    task_id: str,
    return_path: Path,
    owner_head: str,
    researcher_id: str,
    terminal_verdict: str,
    method_harvest: str,
    output_manifest: list[str],
    frozen_at: str,
    root: Path = ROOT,
) -> dict[str, Any]:
    if not task_exists(task_id, root):
        raise ResultRecordError("cannot freeze result for an unknown task")
    if not return_path.exists():
        raise ResultRecordError(f"return artifact does not exist: {return_path}")
    if not owner_head.strip():
        raise ResultRecordError("owner_head is required")
    if not research_identity.valid_execution_id(researcher_id):
        raise ResultRecordError("invalid researcher_id")
    if terminal_verdict not in TERMINAL_VERDICTS:
        raise ResultRecordError("invalid terminal_verdict")
    if method_harvest not in METHOD_HARVEST:
        raise ResultRecordError("invalid method_harvest")
    if not output_manifest or any(not isinstance(item, str) or not item.strip() for item in output_manifest):
        raise ResultRecordError("output_manifest must be a nonempty string list")
    return_blob = _blob(return_path)
    rid = result_id(task_id, return_blob, owner_head)
    return {
        "record_schema": RESULT_SCHEMA,
        "result_id": rid,
        "task_id": task_id,
        "state": "FROZEN_RETURN",
        "return_path": return_path.relative_to(root).as_posix(),
        "return_blob_sha1": return_blob,
        "owner_head": owner_head,
        "researcher_id": researcher_id.strip().upper(),
        "frozen_at": frozen_at,
        "terminal_verdict": terminal_verdict,
        "output_manifest": output_manifest,
        "method_harvest": method_harvest,
        "driver_review_required": True,
    }


def review_result(
    *,
    result: dict[str, Any],
    driver_id: str,
    disposition: str,
    review_path: Path,
    reviewed_at: str,
    root: Path = ROOT,
) -> dict[str, Any]:
    if not research_identity.valid_execution_id(driver_id):
        raise ResultRecordError("invalid driver_id")
    if disposition not in ALL_DISPOSITIONS:
        raise ResultRecordError("invalid disposition")
    if not review_path.exists():
        raise ResultRecordError(f"Driver review artifact missing: {review_path}")
    review_blob = _blob(review_path)
    rid = review_id(result["result_id"], driver_id, review_blob, disposition)
    return {
        "record_schema": REVIEW_SCHEMA,
        "review_id": rid,
        "result_id": result["result_id"],
        "task_id": result["task_id"],
        "driver_id": driver_id.strip().upper(),
        "review_path": review_path.relative_to(root).as_posix(),
        "review_blob_sha1": review_blob,
        "reviewed_at": reviewed_at,
        "disposition": disposition,
        "terminal": disposition in TERMINAL_DISPOSITIONS,
    }


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        results = result_map(root)
    except Exception as exc:
        return [str(exc)]
    seen_reviews: set[str] = set()
    for rid, item in results.items():
        prefix = item.get("_record_path", rid)
        if item.get("record_schema") != RESULT_SCHEMA:
            errors.append(f"{prefix}: wrong result schema")
        if not task_exists(str(item.get("task_id", "")), root):
            errors.append(f"{prefix}: unknown task")
        path_value = item.get("return_path")
        if not isinstance(path_value, str) or not (root / path_value).exists():
            errors.append(f"{prefix}: return artifact missing")
        elif _blob(root / path_value) != item.get("return_blob_sha1"):
            errors.append(f"{prefix}: return artifact blob drift")
        if item.get("terminal_verdict") not in TERMINAL_VERDICTS:
            errors.append(f"{prefix}: invalid terminal_verdict")
        if item.get("method_harvest") not in METHOD_HARVEST:
            errors.append(f"{prefix}: invalid method_harvest")
    for item in iter_reviews(root):
        prefix = item.get("_review_path", "<review>")
        rev_id = item.get("review_id")
        if not isinstance(rev_id, str) or not rev_id:
            errors.append(f"{prefix}: missing review_id")
        elif rev_id in seen_reviews:
            errors.append(f"{prefix}: duplicate review_id")
        seen_reviews.add(rev_id)
        if item.get("record_schema") != REVIEW_SCHEMA:
            errors.append(f"{prefix}: wrong review schema")
        rid = item.get("result_id")
        if rid not in results:
            errors.append(f"{prefix}: unknown result")
        elif item.get("task_id") != results[rid].get("task_id"):
            errors.append(f"{prefix}: task mismatch")
        path_value = item.get("review_path")
        if not isinstance(path_value, str) or not (root / path_value).exists():
            errors.append(f"{prefix}: review artifact missing")
        elif _blob(root / path_value) != item.get("review_blob_sha1"):
            errors.append(f"{prefix}: review artifact blob drift")
        if item.get("disposition") not in ALL_DISPOSITIONS:
            errors.append(f"{prefix}: invalid disposition")
        if item.get("terminal") is not (item.get("disposition") in TERMINAL_DISPOSITIONS):
            errors.append(f"{prefix}: terminal flag mismatch")
    return errors


def command_freeze(args: argparse.Namespace) -> int:
    path = Path(args.return_path)
    if not path.is_absolute():
        path = ROOT / path
    record = freeze_result(
        task_id=args.task_id,
        return_path=path,
        owner_head=args.owner_head,
        researcher_id=args.researcher_id,
        terminal_verdict=args.terminal_verdict,
        method_harvest=args.method_harvest,
        output_manifest=json.loads(args.output_manifest_json),
        frozen_at=_now(args.frozen_at),
    )
    out = RESULT_ROOT / _safe_id(args.task_id, "task_id") / f"{record['result_id']}.json"
    _save_exclusive(out, record)
    errors = audit()
    if errors:
        raise ResultRecordError("result record created but audit failed: " + "; ".join(errors))
    print(json.dumps({**record, "record_path": out.relative_to(ROOT).as_posix()}, ensure_ascii=False, indent=2))
    return 0


def command_review(args: argparse.Namespace) -> int:
    result = result_map().get(args.result_id)
    if result is None:
        raise ResultRecordError(f"unknown result_id: {args.result_id}")
    path = Path(args.review_path)
    if not path.is_absolute():
        path = ROOT / path
    record = review_result(
        result=result,
        driver_id=args.driver_id,
        disposition=args.disposition,
        review_path=path,
        reviewed_at=_now(args.reviewed_at),
    )
    out = REVIEW_ROOT / _safe_id(args.result_id, "result_id") / f"{record['review_id']}.json"
    _save_exclusive(out, record)
    errors = audit()
    if errors:
        raise ResultRecordError("review record created but audit failed: " + "; ".join(errors))
    print(json.dumps({**record, "record_path": out.relative_to(ROOT).as_posix()}, ensure_ascii=False, indent=2))
    return 0


def command_audit(args: argparse.Namespace) -> int:
    errors = audit()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(f"PASS: result/review records valid ({len(iter_results())} result(s), {len(iter_reviews())} review(s)).")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise Math immutable result/review registry")
    sub = parser.add_subparsers(dest="command", required=True)
    freeze = sub.add_parser("freeze")
    freeze.add_argument("--task-id", required=True)
    freeze.add_argument("--return-path", required=True)
    freeze.add_argument("--owner-head", required=True)
    freeze.add_argument("--researcher-id", required=True)
    freeze.add_argument("--terminal-verdict", choices=sorted(TERMINAL_VERDICTS), required=True)
    freeze.add_argument("--method-harvest", choices=sorted(METHOD_HARVEST), required=True)
    freeze.add_argument("--output-manifest-json", required=True)
    freeze.add_argument("--frozen-at")
    freeze.set_defaults(func=command_freeze)
    review = sub.add_parser("review")
    review.add_argument("--result-id", required=True)
    review.add_argument("--driver-id", required=True)
    review.add_argument("--disposition", choices=sorted(ALL_DISPOSITIONS), required=True)
    review.add_argument("--review-path", required=True)
    review.add_argument("--reviewed-at")
    review.set_defaults(func=command_review)
    audit_parser = sub.add_parser("audit")
    audit_parser.set_defaults(func=command_audit)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ResultRecordError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
