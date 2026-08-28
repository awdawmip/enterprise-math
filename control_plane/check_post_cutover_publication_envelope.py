#!/usr/bin/env python3
"""Fail fast on post-cutover task-publication writer bypass.

Every unquarantined object in the live ``research_task_records`` authority path
must use the V2 publication record and canonical ``ENTERPRISE_MATH_TASK_V1``
taskbook envelope, with an exact Git-blob pin.

Known historical defects are not silently grandfathered: the only exception is
an exact current record already validated by
``research_task_integrity_quarantines.json``.  Blob drift, a changed error set,
a new malformed writer, or a repaired-but-stale quarantine fails elsewhere in
the same canonical integrity chain.
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

from control_plane import research_task_integrity_fault_isolation as integrity_isolation  # noqa: E402

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


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        quarantine_rows = integrity_isolation.validated_quarantines(root)
    except Exception as exc:
        return [f"task-integrity quarantine invalid: {exc}"]
    quarantined_paths = {
        row["record_path"]
        for row in quarantine_rows.values()
        if isinstance(row.get("record_path"), str)
    }

    record_dir = root / "research_task_records"
    for record_path in sorted(record_dir.glob("*/*.json")):
        rel = record_path.relative_to(root).as_posix()
        if rel in quarantined_paths:
            # Exact bytes/error-set validation already ran above.  This is not a
            # compatibility waiver for any other record.
            continue
        try:
            record = json.loads(record_path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{rel}: invalid JSON: {exc}")
            continue
        if not isinstance(record, dict):
            errors.append(f"{rel}: record must be an object")
            continue
        if record.get("record_schema") != RECORD_SCHEMA:
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
            errors.append(f"{rel}: missing/invalid taskbook_blob_sha1")
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
            errors.append(
                f"{rel}: {path_value} does not use canonical ENTERPRISE_MATH_TASK_V1 envelope"
            )
            continue
        actual_blob = git_blob_sha1(data)
        if actual_blob != declared_blob:
            errors.append(
                f"{rel}: taskbook Git blob drift: declared {declared_blob}, actual {actual_blob}"
            )
    return errors


def main() -> int:
    errors = audit(ROOT)
    if errors:
        for error in errors:
            print("ERROR:", error)
        print(f"post-cutover publication envelope audit: FAIL ({len(errors)} error(s))")
        return 1
    quarantined = len(integrity_isolation.validated_quarantines(ROOT))
    print(
        "post-cutover publication envelope audit: OK "
        f"(exact quarantined legacy faults={quarantined}; all other live records canonical)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
