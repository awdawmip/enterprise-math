#!/usr/bin/env python3
"""Exact audit-only isolation for nonlive immutable execution-intent defects.

The strict execution-record audit remains unchanged in ``tools/research_execution_records``.
This wrapper may suppress only exact error strings for exact record blobs whose execution
is independently proven non-live by either:

* a frozen result bound to the same task/publication/execution_record_id; or
* the immutable execution record's own TERMINAL_EXECUTION state.

An explicitly registered legacy post-execution payload may instead use its
literal record_id only inside this audit layer: both its exact bytes and one
frozen result's exact bytes must be pinned, and that result must bind the full
execution identity and include the exact payload path/blob in its output manifest.
The missing canonical execution_record_id remains a strict error, not an alias.

The registry is never consulted by intent lookup, ownership, dispatch, result authority,
or review authority.
"""
from __future__ import annotations

import json
import hashlib
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import research_task_records_impl as record_core  # noqa: E402
from tools import research_execution_records  # noqa: E402

REGISTRY = "research_execution_record_audit_quarantines.json"
SCHEMA = "ENTERPRISE_MATH_EXECUTION_RECORD_AUDIT_QUARANTINE_V1"
STATE = "NONLIVE_IMMUTABLE_EXECUTION_AUDIT_FAULT"
BASIS_RESULT = "BOUND_FROZEN_RESULT_EXISTS"
BASIS_TERMINAL = "TERMINAL_EXECUTION_STATE"
BASIS_LEGACY_RESULT = "BOUND_FROZEN_RESULT_EXACT_LEGACY_RECORD"
BASES = {BASIS_RESULT, BASIS_TERMINAL, BASIS_LEGACY_RESULT}
SHA1 = re.compile(r"^sha1:[0-9a-f]{40}$")


class ExecutionAuditIsolationError(ValueError):
    pass


def _payload(root: Path) -> dict[str, Any]:
    path = root / REGISTRY
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ExecutionAuditIsolationError(f"{REGISTRY}: JSON root must be object")
    if value.get("schema") != SCHEMA or value.get("status") != "ACTIVE":
        raise ExecutionAuditIsolationError(f"{REGISTRY}: wrong schema/status")
    return value


def _result_records(root: Path) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    directory = root / "research_result_records"
    if not directory.exists():
        return out
    for path in sorted(directory.glob("*/*.json")):
        value = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(value, dict):
            value["_record_path"] = path.relative_to(root).as_posix()
            out.append(value)
    return out


def _pinned_object(root: Path, relative: Any, pin: Any, directory: str, qid: str) -> dict[str, Any]:
    if not isinstance(relative, str) or not relative or "\\" in relative:
        raise ExecutionAuditIsolationError(f"{qid}: exact source path invalid")
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or len(path.parts) != 3 or path.parts[0] != directory:
        raise ExecutionAuditIsolationError(f"{qid}: exact source path escapes {directory}")
    target = root / path
    if not target.resolve().is_relative_to(root.resolve()):
        raise ExecutionAuditIsolationError(f"{qid}: exact source resolves outside repository")
    if not isinstance(pin, str) or not SHA1.fullmatch(pin):
        raise ExecutionAuditIsolationError(f"{qid}: exact source blob pin invalid")
    raw = target.read_bytes()
    if record_core.git_blob_sha1_bytes(raw) != pin:
        raise ExecutionAuditIsolationError(f"{qid}: exact source blob drift: {relative}")
    value = json.loads(raw)
    if not isinstance(value, dict):
        raise ExecutionAuditIsolationError(f"{qid}: exact source must be a JSON object")
    value["_record_path"] = relative
    return value


def _legacy_record(row: dict[str, Any], root: Path) -> dict[str, Any]:
    qid = row["quarantine_id"]
    record = _pinned_object(
        root, row["record_path"], row["record_blob_sha1"], "research_execution_records", qid,
    )
    if "execution_record_id" in record:
        raise ExecutionAuditIsolationError(f"{qid}: legacy basis requires canonical execution_record_id to be absent")
    if record.get("record_schema") != research_execution_records.SCHEMA:
        raise ExecutionAuditIsolationError(f"{qid}: legacy execution record schema mismatch")
    if record.get("record_id") != row["execution_record_id"]:
        raise ExecutionAuditIsolationError(f"{qid}: literal legacy record_id mismatch")
    return record


def _validate_legacy_result(row: dict[str, Any], record: dict[str, Any], root: Path) -> None:
    qid = row["quarantine_id"]
    result = _pinned_object(
        root, row.get("result_record_path"), row.get("result_record_blob_sha1"),
        "research_result_records", qid,
    )
    result_id = row.get("result_id")
    if not isinstance(result_id, str) or not result_id or result.get("result_id") != result_id:
        raise ExecutionAuditIsolationError(f"{qid}: frozen result identity mismatch")
    if result.get("record_schema") != "ENTERPRISE_MATH_RESEARCH_RESULT_RECORD_V1":
        raise ExecutionAuditIsolationError(f"{qid}: frozen result schema mismatch")
    if result.get("execution_record_id") != row["execution_record_id"]:
        raise ExecutionAuditIsolationError(f"{qid}: frozen result execution binding mismatch")
    for field in (
        "task_id", "publication_id", "claim_id", "researcher_id",
        "execution_branch", "execution_branch_base",
    ):
        value = record.get(field)
        if not isinstance(value, str) or not value.strip() or result.get(field) != value:
            raise ExecutionAuditIsolationError(f"{qid}: frozen result {field} binding mismatch")
    for field in ("frozen_at", "terminal_verdict"):
        if not isinstance(result.get(field), str) or not result[field].strip():
            raise ExecutionAuditIsolationError(f"{qid}: frozen result lacks {field}")
    if result["terminal_verdict"] != record.get("terminal_verdict"):
        raise ExecutionAuditIsolationError(f"{qid}: frozen result terminal verdict differs from legacy payload")
    manifest = result.get("output_manifest")
    if not isinstance(manifest, list) or any(not isinstance(item, dict) for item in manifest):
        raise ExecutionAuditIsolationError(f"{qid}: frozen result output_manifest invalid")
    paths = [item.get("path") for item in manifest]
    if any(not isinstance(path, str) or not path for path in paths) or len(set(paths)) != len(paths):
        raise ExecutionAuditIsolationError(f"{qid}: frozen result output_manifest paths invalid/duplicated")
    matches = [item for item in manifest if item["path"] == row["record_path"]]
    if len(matches) != 1 or matches[0].get("git_blob_sha1") != row["record_blob_sha1"]:
        raise ExecutionAuditIsolationError(f"{qid}: frozen result manifest lacks exact legacy record path/blob")
    declared_sha256 = matches[0].get("sha256")
    if declared_sha256 is not None:
        actual_sha256 = "sha256:" + hashlib.sha256((root / row["record_path"]).read_bytes()).hexdigest()
        if declared_sha256 != actual_sha256:
            raise ExecutionAuditIsolationError(f"{qid}: frozen result manifest legacy record SHA256 mismatch")


def validated_rows(root: Path = ROOT) -> list[dict[str, Any]]:
    payload = _payload(root)
    rows = payload.get("quarantines")
    if not isinstance(rows, list):
        raise ExecutionAuditIsolationError(f"{REGISTRY}: quarantines must be list")

    executions = {
        str(item.get("execution_record_id")): item
        for item in research_execution_records.iter_records(root)
        if isinstance(item.get("execution_record_id"), str)
    }
    results = _result_records(root)
    seen_qids: set[str] = set()
    seen_execs: set[str] = set()
    out: list[dict[str, Any]] = []

    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ExecutionAuditIsolationError(f"{REGISTRY}: row {index} must be object")
        qid = row.get("quarantine_id")
        erid = row.get("execution_record_id")
        task_id = row.get("task_id")
        publication_id = row.get("publication_id")
        if not isinstance(qid, str) or not qid or qid in seen_qids:
            raise ExecutionAuditIsolationError(f"{REGISTRY}: invalid/duplicate quarantine_id {qid!r}")
        if not isinstance(erid, str) or not erid or erid in seen_execs:
            raise ExecutionAuditIsolationError(f"{qid}: invalid/duplicate execution_record_id")
        if not isinstance(task_id, str) or not task_id:
            raise ExecutionAuditIsolationError(f"{qid}: missing task_id")
        if not isinstance(publication_id, str) or not publication_id:
            raise ExecutionAuditIsolationError(f"{qid}: missing publication_id")
        if row.get("state") != STATE or row.get("nonlive_basis") not in BASES:
            raise ExecutionAuditIsolationError(f"{qid}: wrong state/nonlive_basis")
        record_path = row.get("record_path")
        declared_blob = row.get("record_blob_sha1")
        if not isinstance(record_path, str) or not record_path:
            raise ExecutionAuditIsolationError(f"{qid}: missing record_path")
        if not isinstance(declared_blob, str) or not SHA1.fullmatch(declared_blob):
            raise ExecutionAuditIsolationError(f"{qid}: invalid record_blob_sha1")
        allowed = row.get("allowed_execution_record_audit_errors")
        if (
            not isinstance(allowed, list)
            or not allowed
            or any(not isinstance(item, str) or not item for item in allowed)
            or len(set(allowed)) != len(allowed)
        ):
            raise ExecutionAuditIsolationError(f"{qid}: invalid allowed_execution_record_audit_errors")
        for flag in (
            "runtime_authority_granted",
            "working_truth_granted",
            "foundation_authority_granted",
            "canonical_promotion_granted",
        ):
            if row.get(flag) is not False:
                raise ExecutionAuditIsolationError(f"{qid}: cannot grant {flag}")

        basis = row["nonlive_basis"]
        record = _legacy_record(row, root) if basis == BASIS_LEGACY_RESULT else executions.get(erid)
        if record is None:
            raise ExecutionAuditIsolationError(f"{qid}: unknown execution_record_id {erid}")
        if record.get("task_id") != task_id or record.get("publication_id") != publication_id:
            raise ExecutionAuditIsolationError(f"{qid}: task/publication binding drift")
        if record.get("_record_path") != record_path:
            raise ExecutionAuditIsolationError(f"{qid}: record_path drift")
        path = root / record_path
        if not path.is_file():
            raise ExecutionAuditIsolationError(f"{qid}: execution record path missing")
        actual_blob = record_core.git_blob_sha1_bytes(path.read_bytes())
        if actual_blob != declared_blob:
            raise ExecutionAuditIsolationError(
                f"{qid}: execution record blob drift; declared={declared_blob} actual={actual_blob}"
            )

        if basis == BASIS_TERMINAL:
            if record.get("record_state") != "TERMINAL_EXECUTION":
                raise ExecutionAuditIsolationError(f"{qid}: execution record is not TERMINAL_EXECUTION")
            if not isinstance(record.get("terminal_at"), str) or not record["terminal_at"].strip():
                raise ExecutionAuditIsolationError(f"{qid}: terminal execution lacks terminal_at")
        elif basis == BASIS_RESULT:
            matches = [
                result
                for result in results
                if result.get("task_id") == task_id
                and result.get("publication_id") == publication_id
                and result.get("execution_record_id") == erid
                and isinstance(result.get("frozen_at"), str)
                and result.get("frozen_at", "").strip()
                and isinstance(result.get("terminal_verdict"), str)
                and result.get("terminal_verdict", "").strip()
            ]
            if not matches:
                raise ExecutionAuditIsolationError(
                    f"{qid}: no frozen terminal result binds exact task/publication/execution record"
                )
        elif basis == BASIS_LEGACY_RESULT:
            _validate_legacy_result(row, record, root)

        seen_qids.add(qid)
        seen_execs.add(erid)
        out.append(row)
    return out


def suppression_strings(root: Path = ROOT) -> set[str]:
    return {
        f"{row['record_path']}: {suffix}"
        for row in validated_rows(root)
        for suffix in row["allowed_execution_record_audit_errors"]
    }


def audit(root: Path = ROOT) -> list[str]:
    raw = research_execution_records.audit(root)
    try:
        suppressions = suppression_strings(root)
    except Exception as exc:
        return [str(exc)]
    raw_set = set(raw)
    errors = [
        f"{REGISTRY}: stale or unused suppression: {item}"
        for item in sorted(suppressions - raw_set)
    ]
    errors.extend(item for item in raw if item not in suppressions)
    return errors


def main() -> int:
    errors = audit(ROOT)
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    rows = validated_rows(ROOT)
    print(
        "PASS: immutable execution intents strict-audited with exact nonlive audit isolation; "
        f"{len(rows)} historical/terminal record(s) pinned; no runtime authority granted."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
