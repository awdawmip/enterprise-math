#!/usr/bin/env python3
"""Fail fast on post-cutover task-publication writer bypass.

This checker is intentionally simpler and earlier than the full publication
validator. Every object left in the live ``research_task_records`` authority
path must have the one V2 record schema and point to bytes using the one
``ENTERPRISE_MATH_TASK_V1`` taskbook envelope. Historical malformed bytes may
be preserved only outside the live authority path.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
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


def main() -> int:
    errors: list[str] = []
    checked = 0
    for record_path in sorted(RECORD_DIR.glob("*/*.json")):
        rel = record_path.relative_to(ROOT).as_posix()
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
                "new malformed formats are not historical compatibility"
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
            continue
        checked += 1

    if errors:
        for error in errors:
            print("ERROR:", error)
        print(f"post-cutover publication envelope audit: FAIL ({len(errors)} error(s), {checked} valid record(s))")
        return 1
    print(f"post-cutover publication envelope audit: OK ({checked} live V2 record(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
