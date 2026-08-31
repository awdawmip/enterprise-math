#!/usr/bin/env python3
"""Run the frozen V1 compatibility registry audit on the fault-isolated task view.

The V1 registry remains read-only compatibility state. This wrapper only makes
its audit consume the same canonical task-local fault boundary as live dispatch,
so one known immutable task fault cannot deny service to the whole audit.

For orphan detection only, an exact audit-only nonoperational immutable V2
record is also valid provenance even when that malformed historical record
itself omitted/drifted its taskbook blob pin. The dedicated audit-quarantine
validator must first prove the exact record blob, actual taskbook blob, strict
error set, and independent nonoperational basis. This grants no V1 write,
current publication, dispatch, Working Truth, Foundation, or promotion authority.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import research_control_bootstrap  # noqa: E402
from control_plane import research_task_record_audit_fault_isolation as record_audit_isolation  # noqa: E402
from tools import research_task_registry  # noqa: E402

ORPHAN_SUFFIX = (
    "orphaned published taskbook has neither a V1 compatibility mirror "
    "nor exact immutable V2/retained-parallel publication provenance"
)


def audit() -> list[str]:
    try:
        research_control_bootstrap.install(ROOT)
        audit_only_rows = record_audit_isolation.validated_rows(ROOT)
    except Exception as exc:
        return [f"cannot install canonical task-view fault isolation: {exc}"]

    errors = research_task_registry.audit_registry(strict=True)
    exact_audit_only_provenance = {
        f"{row['taskbook_path']}: {ORPHAN_SUFFIX}"
        for row in audit_only_rows
        if isinstance(row.get("taskbook_path"), str) and row.get("taskbook_path")
    }
    return [error for error in errors if error not in exact_audit_only_provenance]


def main() -> int:
    errors = audit()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    count = len(
        research_task_registry.load_json(research_task_registry.REGISTRY_PATH).get("tasks", [])
    )
    print(
        "PASS: V1 compatibility registry valid on the canonical fault-isolated "
        f"task view; {count} mirrored task(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
