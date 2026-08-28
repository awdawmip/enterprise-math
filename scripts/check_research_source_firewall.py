#!/usr/bin/env python3
"""Audit opt-in BLIND_INDEPENDENT source-firewall declarations.

This repository-level audit checks only the declarative control contract. Exact
Git-object availability is revalidated at the PRE_MATH / SOURCE_EXPOSED runtime
boundaries, because CI uses a shallow checkout and must not fetch hidden source
commits merely to validate a taskbook declaration.
"""
from __future__ import annotations

from pathlib import Path

from control_plane import research_source_firewall as firewall
from tools import research_task_records, research_taskbook

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    try:
        current = research_task_records.current_records(ROOT)
    except Exception as exc:
        print(f"source firewall audit: FAIL: cannot resolve current publications: {exc}")
        return 1

    declared: list[str] = []
    errors: list[str] = []
    seen_paths: set[str] = set()
    for task_id, record in sorted(current.items()):
        path_value = record.get("taskbook_path")
        if not isinstance(path_value, str) or not path_value:
            errors.append(f"{task_id}: current publication has no taskbook_path")
            continue
        if path_value in seen_paths:
            continue
        seen_paths.add(path_value)
        path = ROOT / path_value
        try:
            meta, _ = research_taskbook.split_taskbook(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{task_id}: cannot parse current taskbook {path_value}: {exc}")
            continue
        if "source_firewall" not in meta:
            continue
        try:
            config = firewall.validate_config(meta.get("source_firewall"))
        except firewall.SourceFirewallError as exc:
            errors.append(f"{task_id}: invalid source_firewall: {exc}")
            continue
        if config is not None:
            declared.append(task_id)

    if errors:
        for error in errors:
            print("ERROR:", error)
        print(
            f"source firewall audit: FAIL ({len(errors)} error(s), "
            f"{len(declared)} valid BLIND_INDEPENDENT task(s))"
        )
        return 1

    print(
        "source firewall audit: OK "
        f"({len(current)} current task(s), {len(declared)} BLIND_INDEPENDENT declaration(s))"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
