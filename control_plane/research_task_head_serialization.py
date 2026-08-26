#!/usr/bin/env python3
"""Per-task Git CAS pointers for immutable task publication authority."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools import research_task_records

HEAD_DIR = "research_task_heads"
HEAD_SCHEMA = "ENTERPRISE_MATH_TASK_PUBLICATION_HEAD_V1"
SERIALIZATION_ROLE = "PER_TASK_GIT_CAS"


class HeadSerializationError(ValueError):
    pass


def _safe_task_id(task_id: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9._-]+", task_id):
        raise HeadSerializationError("task_id contains unsupported characters")
    return task_id


def head_path(root: Path, task_id: str) -> Path:
    return root / HEAD_DIR / f"{_safe_task_id(task_id)}.json"


def expected_head(record: dict[str, Any], root: Path = ROOT) -> dict[str, Any]:
    task_id = str(record["task_id"])
    record_rel = str(record["_record_path"])
    record_file = root / record_rel
    return {
        "head_schema": HEAD_SCHEMA,
        "task_id": task_id,
        "current_publication_id": record["publication_id"],
        "publication_generation": int(record.get("publication_generation", 1)),
        "publication_record_path": record_rel,
        "publication_record_blob_sha1": research_task_records.git_blob_sha1_bytes(
            record_file.read_bytes()
        ),
        "serialization_role": SERIALIZATION_ROLE,
        "working_truth_granted": False,
        "canonical_promotion_granted": False,
        "successor_triggered": False,
    }


def load_heads(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    directory = root / HEAD_DIR
    if not directory.exists():
        return {}
    out: dict[str, dict[str, Any]] = {}
    for path in sorted(directory.glob("*.json")):
        value = json.loads(path.read_text(encoding="utf-8"))
        task_id = value.get("task_id")
        if not isinstance(task_id, str) or not task_id:
            raise HeadSerializationError(f"{path}: missing task_id")
        if task_id in out:
            raise HeadSerializationError(f"duplicate head pointer for {task_id}")
        if path.name != f"{_safe_task_id(task_id)}.json":
            raise HeadSerializationError(f"{path}: filename/task_id mismatch")
        out[task_id] = value
    return out


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        current = research_task_records.current_records(root)
        heads = load_heads(root)
    except Exception as exc:
        return [str(exc)]

    missing = sorted(set(current) - set(heads))
    orphan = sorted(set(heads) - set(current))
    errors.extend(f"missing head pointer: {task_id}" for task_id in missing)
    errors.extend(f"orphan head pointer: {task_id}" for task_id in orphan)

    for task_id in sorted(set(current) & set(heads)):
        expected = expected_head(current[task_id], root)
        actual = heads[task_id]
        if actual != expected:
            errors.append(
                f"head pointer drift for {task_id}: expected "
                f"{expected['current_publication_id']} generation "
                f"{expected['publication_generation']}"
            )
    return errors


def _atomic_write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def sync(task_id: str, root: Path = ROOT) -> dict[str, Any]:
    current = research_task_records.current_records(root)
    if task_id not in current:
        raise HeadSerializationError(f"no current publication for {task_id}")
    value = expected_head(current[task_id], root)
    _atomic_write(head_path(root, task_id), value)
    return value


def sync_all(root: Path = ROOT) -> int:
    current = research_task_records.current_records(root)
    for task_id in sorted(current):
        sync(task_id, root)
    return len(current)


def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise Math per-task publication head serialization")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("audit")
    sync_parser = sub.add_parser("sync")
    sync_parser.add_argument("--task-id", required=True)
    sub.add_parser("sync-all")
    args = parser.parse_args()

    if args.command == "audit":
        errors = audit()
        if errors:
            for error in errors:
                print("ERROR:", error)
            return 1
        print(f"PASS: {len(load_heads())} per-task publication head pointers are serialized.")
        return 0
    if args.command == "sync":
        print(json.dumps(sync(args.task_id), ensure_ascii=False, indent=2))
        return 0
    count = sync_all()
    print(f"PASS: synchronized {count} per-task publication head pointers.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except HeadSerializationError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
