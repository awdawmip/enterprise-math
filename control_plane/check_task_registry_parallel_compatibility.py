#!/usr/bin/env python3
"""Extend the frozen V1 orphan audit for exact retained-parallel immutable taskbooks.

The V1 registry remains read-only. This control-plane bridge exempts only a
published taskbook that is still backed by an exact immutable V2-schema
publication record explicitly listed in the task's active parallel-intake
resolution. The record may have entered through the normal V2 writer or an
accepted legacy-to-immutable migration transaction. No retained publication
receives runtime/claim authority from this bridge.
"""
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools import research_task_records, research_task_registry, research_taskbook

ORPHAN_SUFFIX = (
    ": orphaned published taskbook has neither a V1 compatibility mirror "
    "nor exact current V2 immutable publication authority"
)


def exact_retained_parallel_authority(path: Path) -> bool:
    try:
        meta, _ = research_taskbook.split_taskbook(path.read_text(encoding="utf-8"))
    except Exception:
        return False
    task_id = meta.get("task_id")
    if not isinstance(task_id, str) or not task_id:
        return False
    try:
        resolution = research_task_records.publication_resolutions(ROOT).get(task_id)
    except Exception:
        return False
    if not isinstance(resolution, dict):
        return False
    retained = resolution.get("retained_parallel_publication_ids")
    if not isinstance(retained, list) or not all(isinstance(x, str) for x in retained):
        return False
    rel = path.relative_to(ROOT).as_posix()
    blob = research_task_registry.blob_sha1(path)
    for record in research_task_records.iter_records(ROOT):
        if record.get("publication_id") not in retained:
            continue
        if (
            record.get("record_schema") == research_task_records.RECORD_SCHEMA
            and record.get("record_state", "ACTIVE") == "ACTIVE"
            and record.get("task_id") == task_id
            and record.get("taskbook_path") == rel
            and record.get("taskbook_blob_sha1") == blob
        ):
            return True
    return False


def audit() -> list[str]:
    errors = research_task_registry.audit_registry(root=ROOT, strict=True)
    remaining: list[str] = []
    for error in errors:
        if not error.endswith(ORPHAN_SUFFIX):
            remaining.append(error)
            continue
        rel = error[: -len(ORPHAN_SUFFIX)]
        path = ROOT / rel
        if not path.exists() or not exact_retained_parallel_authority(path):
            remaining.append(error)
            continue
        print(
            "PASS retained-parallel immutable compatibility: "
            f"{rel} remains research evidence but is not current runtime authority."
        )
    return remaining


if __name__ == "__main__":
    failures = audit()
    if failures:
        for failure in failures:
            print("ERROR:", failure)
        raise SystemExit(1)
    print("PASS: V1 compatibility plus exact retained-parallel immutable taskbooks are non-orphaned.")
