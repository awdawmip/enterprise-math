#!/usr/bin/env python3
"""Control-only result replacement chains.

A corrected re-freeze of the *same execution* is not a second independent research
result. This module validates explicit replacement edges and identifies the
historical source results that must stay referenceable but leave the operational
result/review view. Distinct executions remain parallel evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from control_plane import research_result_records_impl as result_impl
import research_driver_authority

ROOT = Path(__file__).resolve().parent
CONTRACT = "research_result_control_replacement_contract.json"
RECORD_ROOT = "research_result_control_replacements"
CONTRACT_SCHEMA = "ENTERPRISE_MATH_RESULT_CONTROL_REPLACEMENT_CONTRACT_V1"
RECORD_SCHEMA = "ENTERPRISE_MATH_RESULT_CONTROL_REPLACEMENT_RECORD_V1"
DRIVER_RE = re.compile(r"^EM-DVR-[A-Z0-9]{4,8}$")
_CORE_EQUAL_FIELDS = (
    "task_id",
    "publication_id",
    "execution_record_id",
    "claim_id",
    "researcher_id",
    "taskbook_path",
    "taskbook_blob_sha1",
    "execution_branch",
    "execution_branch_base",
    "return_path",
    "terminal_verdict",
    "unresolved_residue",
    "method_harvest",
    "independence_status",
    "source_exposure_status",
    "driver_review_required",
)


class ResultControlReplacementError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ResultControlReplacementError(f"{path}: JSON object required")
    return value


def _parse_time(value: Any, label: str) -> datetime:
    if not isinstance(value, str) or not value.strip():
        raise ResultControlReplacementError(f"{label} is required")
    try:
        dt = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except Exception as exc:
        raise ResultControlReplacementError(f"invalid {label}: {value!r}") from exc
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def replacement_id(historical_result_id: str, corrected_result_id: str) -> str:
    raw = f"{historical_result_id}\0{corrected_result_id}".encode("utf-8")
    return "RCR-" + hashlib.sha256(raw).hexdigest()[:20].upper()


def contract(root: Path = ROOT) -> dict[str, Any] | None:
    path = root / CONTRACT
    if not path.exists():
        return None
    value = _load(path)
    if value.get("schema") != CONTRACT_SCHEMA:
        raise ResultControlReplacementError("wrong control-result replacement contract schema")
    if value.get("status") not in {"ACTIVE_CANONICAL_CANDIDATE", "ACTIVE_CANONICAL"}:
        raise ResultControlReplacementError("control-result replacement contract is not active")
    if value.get("record_schema") != RECORD_SCHEMA:
        raise ResultControlReplacementError("replacement record schema boundary drifted")
    return value


def iter_records(root: Path = ROOT) -> list[dict[str, Any]]:
    directory = root / RECORD_ROOT
    if not directory.exists():
        return []
    out: list[dict[str, Any]] = []
    for path in sorted(directory.glob("*/*.json")):
        value = _load(path)
        value["_path"] = path.relative_to(root).as_posix()
        out.append(value)
    return out


def _raw_results(root: Path) -> list[dict[str, Any]]:
    raw = result_impl.__dict__.get("_history_original_iter_results", result_impl.iter_results)
    return raw(root)


def _manifest_map(result: dict[str, Any], label: str) -> dict[str, dict[str, Any]]:
    rows = result.get("output_manifest")
    if not isinstance(rows, list) or not rows:
        raise ResultControlReplacementError(f"{label}: output_manifest missing")
    out: dict[str, dict[str, Any]] = {}
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("path"), str) or not row["path"]:
            raise ResultControlReplacementError(f"{label}: invalid output manifest row")
        path = row["path"]
        if path in out:
            raise ResultControlReplacementError(f"{label}: duplicate output path {path}")
        out[path] = row
    return out


def _record_blob_matches(item: dict[str, Any], expected_path: Any, expected_blob: Any, root: Path) -> bool:
    actual_path = item.get("_record_path")
    if not isinstance(expected_path, str) or actual_path != expected_path:
        return False
    path = root / expected_path
    if not path.exists() or not isinstance(expected_blob, str):
        return False
    return result_impl._same_git_blob_identity(result_impl._blob(path), expected_blob)


def _authority_errors(row: dict[str, Any], prefix: str, root: Path) -> list[str]:
    driver_id = row.get("driver_id")
    created_at = row.get("created_at")
    if not isinstance(driver_id, str) or not DRIVER_RE.fullmatch(driver_id.strip().upper()):
        return [f"{prefix}: driver_id must use EM-DVR-* syntax"]
    if not isinstance(created_at, str) or not created_at:
        return [f"{prefix}: created_at is required"]
    try:
        active = research_driver_authority.require_active_driver(driver_id, created_at, root)
    except research_driver_authority.DriverAuthorityError as exc:
        return [f"{prefix}: {exc}"]
    if active is None:
        return [f"{prefix}: source-backed Driver authority unexpectedly disabled"]
    if row.get("driver_authority_record_id") != active.get("authority_record_id"):
        return [f"{prefix}: driver_authority_record_id does not pin active authority"]
    if row.get("driver_authority_source_comment_id") != active.get("source_comment_id"):
        return [f"{prefix}: driver_authority_source_comment_id does not pin active authority"]
    return []


def _edge_errors(row: dict[str, Any], raw_results: dict[str, dict[str, Any]], root: Path) -> list[str]:
    errors: list[str] = []
    prefix = str(row.get("_path") or row.get("replacement_id") or "<result-replacement>")
    if row.get("record_schema") != RECORD_SCHEMA:
        errors.append(f"{prefix}: wrong record_schema")
    old_id = row.get("historical_result_id")
    new_id = row.get("corrected_result_id")
    if not isinstance(old_id, str) or not old_id or not isinstance(new_id, str) or not new_id or old_id == new_id:
        errors.append(f"{prefix}: historical/corrected result ids are invalid")
        return errors
    if row.get("replacement_id") != replacement_id(old_id, new_id):
        errors.append(f"{prefix}: replacement_id mismatch")
    old = raw_results.get(old_id)
    new = raw_results.get(new_id)
    if old is None or new is None:
        errors.append(f"{prefix}: historical/corrected result is unavailable")
        return errors
    if row.get("resolution") != "CONTROL_ONLY_REFREEZE_SUPERSEDES":
        errors.append(f"{prefix}: unsupported replacement resolution")
    if row.get("operational_result_id") != new_id:
        errors.append(f"{prefix}: operational_result_id must equal corrected_result_id")
    if row.get("history_preserved") is not True or row.get("parallel_evidence") is not False:
        errors.append(f"{prefix}: replacement must preserve history and deny parallel-evidence semantics")
    if not _record_blob_matches(old, row.get("historical_record_path"), row.get("historical_record_blob_sha1"), root):
        errors.append(f"{prefix}: historical immutable record path/blob drift")
    if not _record_blob_matches(new, row.get("corrected_record_path"), row.get("corrected_record_blob_sha1"), root):
        errors.append(f"{prefix}: corrected immutable record path/blob drift")
    for field in _CORE_EQUAL_FIELDS:
        if old.get(field) != new.get(field):
            errors.append(f"{prefix}: control replacement changed core field {field}")
    if not result_impl._same_git_blob_identity(old.get("return_blob_sha1"), new.get("return_blob_sha1")):
        errors.append(f"{prefix}: control replacement changed return Git blob")
    if old.get("return_sha256") != new.get("return_sha256"):
        errors.append(f"{prefix}: control replacement changed return SHA-256")
    old_hard = old.get("hard_target_disposition")
    new_hard = new.get("hard_target_disposition")
    if not isinstance(old_hard, str) or not isinstance(new_hard, str) or not new_hard.startswith(old_hard):
        errors.append(f"{prefix}: corrected hard_target_disposition must preserve/extend historical disposition")
    if old.get("owner_head") == new.get("owner_head"):
        errors.append(f"{prefix}: control re-freeze requires a distinct owner checkpoint")
    try:
        if _parse_time(new.get("frozen_at"), "corrected frozen_at") <= _parse_time(old.get("frozen_at"), "historical frozen_at"):
            errors.append(f"{prefix}: corrected result must freeze strictly after historical result")
    except ResultControlReplacementError as exc:
        errors.append(f"{prefix}: {exc}")
    try:
        old_manifest = _manifest_map(old, old_id)
        new_manifest = _manifest_map(new, new_id)
        if not set(old_manifest) < set(new_manifest):
            errors.append(f"{prefix}: corrected output manifest must be a strict path superset")
        for path in set(old_manifest) & set(new_manifest):
            before = old_manifest[path]
            after = new_manifest[path]
            if not result_impl._same_git_blob_identity(before.get("git_blob_sha1"), after.get("git_blob_sha1")):
                errors.append(f"{prefix}: common manifest Git blob changed: {path}")
            if before.get("sha256") != after.get("sha256"):
                errors.append(f"{prefix}: common manifest SHA-256 changed: {path}")
    except ResultControlReplacementError as exc:
        errors.append(f"{prefix}: {exc}")
    reason = row.get("reason")
    if not isinstance(reason, list) or not reason or any(not isinstance(x, str) or not x.strip() for x in reason):
        errors.append(f"{prefix}: reason must be a nonempty string list")
    errors.extend(_authority_errors(row, prefix, root))
    for field in (
        "working_truth_granted",
        "foundation_authority_granted",
        "canonical_promotion_granted",
        "successor_triggered",
    ):
        if row.get(field) is not False:
            errors.append(f"{prefix}: {field} must be false")
    return errors


def replacement_edges(raw_results: dict[str, dict[str, Any]], root: Path = ROOT) -> dict[str, dict[str, Any]]:
    if contract(root) is None:
        return {}
    rows = iter_records(root)
    errors: list[str] = []
    by_old: dict[str, dict[str, Any]] = {}
    incoming: dict[str, str] = {}
    for row in rows:
        errors.extend(_edge_errors(row, raw_results, root))
        old_id = row.get("historical_result_id")
        new_id = row.get("corrected_result_id")
        if isinstance(old_id, str):
            if old_id in by_old:
                errors.append(f"multiple control replacements leave {old_id}")
            by_old[old_id] = row
        if isinstance(new_id, str):
            if new_id in incoming:
                errors.append(f"multiple control replacements enter {new_id}")
            incoming[new_id] = str(old_id)
    for old_id, row in by_old.items():
        new_id = row.get("corrected_result_id")
        if old_id == new_id:
            errors.append(f"self-cycle in control replacement: {old_id}")
    for start in by_old:
        seen: set[str] = set()
        cursor = start
        while cursor in by_old:
            if cursor in seen:
                errors.append(f"cycle in control replacement chain at {cursor}")
                break
            seen.add(cursor)
            cursor = str(by_old[cursor].get("corrected_result_id"))
    if errors:
        raise ResultControlReplacementError("; ".join(errors))
    return by_old


def operationally_replaced_result_ids(raw_results: dict[str, dict[str, Any]], root: Path = ROOT) -> set[str]:
    return set(replacement_edges(raw_results, root))


def audit(root: Path = ROOT) -> list[str]:
    try:
        contract(root)
        raw = {
            str(item.get("result_id")): item
            for item in _raw_results(root)
            if isinstance(item.get("result_id"), str) and item.get("result_id")
        }
        replacement_edges(raw, root)
        return []
    except Exception as exc:
        return [str(exc)]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Enterprise Math control-only result replacement chains")
    parser.add_argument("command", choices=["audit"])
    args = parser.parse_args(argv)
    errors = audit(ROOT)
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(f"PASS: control-result replacement chains valid ({len(iter_records(ROOT))} edge(s)).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
