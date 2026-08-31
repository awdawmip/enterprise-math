#!/usr/bin/env python3
"""Fail fast on post-cutover task-publication writer bypass.

Every unquarantined object in the live ``research_task_records`` authority path
must use the V2 publication record, canonical ``ENTERPRISE_MATH_TASK_V1``
taskbook envelope, exact Git-blob pin, and the five canonical mandatory body
sections required by the publication transaction.

Exact current-task integrity quarantine and exact audit-only nonoperational-record
quarantine remain explicit exceptions because their bytes/error sets are already
pinned and independently nonoperational. Full record-audit errors and earliest
envelope errors remain separate vocabularies so no stale suppression leaks across
checkers. Exact historical heading-alias waivers remain valid only through their
existing nonoperational compatibility validator. No generic grandfathering is
allowed: a new malformed remote/manual publication must fail this earliest
writer-envelope gate.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import research_control_bootstrap  # noqa: E402
from control_plane import research_task_integrity_fault_isolation as integrity_isolation  # noqa: E402
from control_plane import research_task_record_audit_fault_isolation as record_audit_isolation  # noqa: E402
from control_plane import research_task_records_impl as record_core  # noqa: E402
from tools import research_taskbook  # noqa: E402
from tools import research_task_records as task_records_facade  # noqa: E402

RECORD_DIR = ROOT / "research_task_records"
RECORD_SCHEMA = "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2"
TASKBOOK_PREFIX = b"<!-- ENTERPRISE_MATH_TASK_V1\n"
SHA1 = re.compile(r"^sha1:[0-9a-f]{40}$")


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return "sha1:" + hashlib.sha1(header + data).hexdigest()


def safe_path(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("taskbook_path must be repository-relative and traversal-free")
    resolved = (ROOT / path).resolve()
    resolved.relative_to(ROOT.resolve())
    return resolved


def _validated_exception_paths(
    root: Path,
) -> tuple[set[str], set[str], set[str], list[str]]:
    """Return exact known-defect paths, envelope suppressions, and legacy-heading paths."""
    errors: list[str] = []
    try:
        # Compatibility-waiver validation resolves operational/current state, so
        # install the same canonical task-local fault-isolated view first.
        research_control_bootstrap.install(root)
        current_rows = integrity_isolation.validated_quarantines(root)
        audit_only_rows = record_audit_isolation.validated_rows(root)
        exact_suppressions = (
            integrity_isolation.suppression_strings(root)
            | record_audit_isolation.envelope_suppression_strings(root)
        )
        compatibility_suppressions, compatibility_errors = (
            task_records_facade._compatibility_suppressions(root)
        )
    except Exception as exc:
        return set(), set(), set(), [f"publication exception validation failed: {exc}"]

    errors.extend(
        f"task-record compatibility waiver invalid: {item}"
        for item in compatibility_errors
    )
    known_defect_paths = {
        row["record_path"]
        for row in current_rows.values()
        if isinstance(row.get("record_path"), str)
    } | {
        row["record_path"]
        for row in audit_only_rows
        if isinstance(row.get("record_path"), str)
    }
    legacy_heading_paths = {
        item.split(": ", 1)[0]
        for item in compatibility_suppressions
        if ": " in item
    }
    return known_defect_paths, legacy_heading_paths, exact_suppressions, errors


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    (
        known_defect_paths,
        legacy_heading_paths,
        exact_suppressions,
        exception_errors,
    ) = _validated_exception_paths(root)
    if exception_errors:
        return exception_errors

    record_dir = root / "research_task_records"
    for record_path in sorted(record_dir.glob("*/*.json")):
        rel = record_path.relative_to(root).as_posix()
        try:
            record = json.loads(record_path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{rel}: invalid JSON: {exc}")
            continue
        if not isinstance(record, dict):
            errors.append(f"{rel}: record must be an object")
            continue
        if record.get("record_schema") != RECORD_SCHEMA:
            if rel in known_defect_paths:
                # Exact bytes/error-set validation already ran above. This is not
                # a compatibility waiver for any other record.
                continue
            errors.append(
                f"{rel}: live task record must use record_schema={RECORD_SCHEMA}; "
                "new malformed formats are not quarantine-compatible"
            )
            continue
        path_value = record.get("taskbook_path")
        if not isinstance(path_value, str) or not path_value:
            errors.append(f"{rel}: missing taskbook_path")
            continue
        declared_blob = record.get("taskbook_blob_sha1")
        if not isinstance(declared_blob, str) or not SHA1.fullmatch(declared_blob):
            exact_error = f"{rel}: missing/invalid taskbook_blob_sha1"
            if exact_error in exact_suppressions:
                # The quarantine validator has already pinned this immutable
                # record, independently pinned the actual taskbook Git blob, and
                # proved the record nonoperational. Only this exact envelope
                # suffix is suppressed; a different defect remains fail-closed.
                continue
            errors.append(exact_error)
            continue
        try:
            taskbook = safe_path(path_value)
        except Exception as exc:
            errors.append(f"{rel}: unsafe taskbook_path: {exc}")
            continue
        if not taskbook.is_file():
            errors.append(f"{rel}: taskbook does not exist: {path_value}")
            continue
        data = taskbook.read_bytes()
        if not data.startswith(TASKBOOK_PREFIX):
            if rel in known_defect_paths:
                continue
            errors.append(
                f"{rel}: {path_value} does not use canonical ENTERPRISE_MATH_TASK_V1 envelope"
            )
            continue
        actual_blob = git_blob_sha1(data)
        if actual_blob != declared_blob:
            exact_error = f"{rel}: taskbook Git blob drift: declared {declared_blob}, actual {actual_blob}"
            if exact_error in exact_suppressions:
                continue
            if rel in known_defect_paths:
                # Any audit-only path reaching this branch must already have an
                # independently exact taskbook pin. Current-task quarantines are
                # separately exact-pinned and task-local BLOCKED.
                continue
            errors.append(exact_error)
            continue

        # Known exact malformed records are intentionally nonoperational and were
        # fully validated by their quarantine registries above. Do not reinterpret
        # their mathematics or retrofit body sections here.
        if rel in known_defect_paths:
            continue

        try:
            meta, body = research_taskbook.split_taskbook(data.decode("utf-8"))
        except Exception as exc:
            errors.append(f"{rel}: canonical taskbook parse failed: {exc}")
            continue
        if meta.get("task_id") != record.get("task_id"):
            errors.append(
                f"{rel}: taskbook task_id {meta.get('task_id')!r} does not match "
                f"record task_id {record.get('task_id')!r}"
            )
            continue

        # Existing exact legacy-heading waivers have their alias payloads and
        # nonoperational status validated by the dedicated compatibility layer.
        if rel in legacy_heading_paths:
            continue

        for message in record_core.validate_body(body):
            errors.append(f"{rel}: {message}")
    return errors


def main() -> int:
    errors = audit(ROOT)
    if errors:
        for error in errors:
            print("ERROR:", error)
        print(f"post-cutover publication envelope audit: FAIL ({len(errors)} error(s))")
        return 1
    current_quarantined = len(integrity_isolation.validated_quarantines(ROOT))
    audit_only_quarantined = len(record_audit_isolation.validated_rows(ROOT))
    print(
        "post-cutover publication envelope audit: OK "
        f"(current invalid publications blocked={current_quarantined}; "
        f"nonoperational immutable audit defects pinned={audit_only_quarantined}; "
        "all other records require canonical envelope/blob/body preflight)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
