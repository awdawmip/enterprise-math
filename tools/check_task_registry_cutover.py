#!/usr/bin/env python3
"""Verify the task-registry cutover has no legacy scheduler publication bypass."""
from __future__ import annotations

import json
from pathlib import Path

try:
    from tools import research_taskbook
except ModuleNotFoundError:
    import research_taskbook  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "research_task_registry.json"


def git_blob_sha1(path: Path) -> str:
    return research_taskbook.git_blob_identity(path.read_bytes()).hex()


def check(root: Path = ROOT) -> list[str]:
    registry = json.loads((root / "research_task_registry.json").read_text(encoding="utf-8"))
    errors: list[str] = []
    legacy = registry.get("legacy_baseline")
    if not isinstance(legacy, dict):
        return ["task registry missing legacy_baseline"]
    if legacy.get("mode") != "FROZEN_SCHEDULER_DEFINITION_FILE":
        errors.append("legacy baseline must freeze the scheduler definition file")
    path_value = legacy.get("scheduler_path")
    expected = legacy.get("scheduler_git_blob_sha1")
    if not isinstance(path_value, str) or not path_value:
        errors.append("legacy baseline missing scheduler_path")
        return errors
    if not isinstance(expected, str) or len(expected) != 40:
        errors.append("legacy baseline missing 40-hex scheduler_git_blob_sha1")
        return errors
    scheduler = root / path_value
    if not scheduler.exists():
        errors.append(f"frozen legacy scheduler missing: {path_value}")
        return errors
    actual = git_blob_sha1(scheduler)
    if actual != expected:
        errors.append(
            "legacy scheduler definition drifted after registry cutover: "
            f"expected {expected}, got {actual}; new/modified tasks must be published "
            "through research_task_registry.json rather than editing research_scheduler.json"
        )
    if legacy.get("scheduler_file_may_publish_new_tasks") is not False:
        errors.append("legacy scheduler must not be an allowed new-task publication path")
    if legacy.get("fresh_redispatch_requires_explicit_record") is not True:
        errors.append("legacy fresh redispatch must require explicit registry migration")
    return errors


def main() -> int:
    errors = check()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print("PASS: legacy scheduler task definitions are frozen; new tasks are registry-only.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
