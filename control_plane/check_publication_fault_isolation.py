#!/usr/bin/env python3
"""Reference-integrity checker for task-local publication fault isolation."""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import research_control_bootstrap  # noqa: E402
from control_plane import research_publication_fault_isolation as fork_isolation  # noqa: E402
from control_plane import research_task_integrity_fault_isolation as integrity_isolation  # noqa: E402


def audit() -> list[str]:
    errors: list[str] = []

    # The strict immutable-record audit remains authoritative. Only exact errors
    # pinned to exact current blobs in the integrity-quarantine registry may be
    # subtracted; every stale/unused suppression is itself an error.
    task_record_errors = integrity_isolation.audit_task_records(ROOT)
    if task_record_errors:
        return task_record_errors

    try:
        research_control_bootstrap.install(ROOT)
        import research_operational_publications as operational
        from tools import research_dispatch

        fork_quarantines = fork_isolation.validated_quarantines(ROOT)
        integrity_quarantines = integrity_isolation.validated_quarantines(ROOT)
        isolated_tasks = set(fork_quarantines) | set(integrity_quarantines)
        heads = operational.publication_heads(ROOT)
        resolutions = operational.resolution_map(ROOT)

        # Preserve the existing operational-publication contract everywhere
        # except exact locally isolated tasks that explicitly select no head.
        for task_id in sorted(heads):
            if task_id in isolated_tasks:
                if task_id in resolutions:
                    errors.append(
                        f"{task_id}: locally isolated task cannot coexist with operational resolution"
                    )
                continue
            try:
                operational.selection(task_id, ROOT)
            except Exception as exc:
                errors.append(str(exc))

        definitions = research_dispatch.merged_definitions(ROOT)
        states = research_dispatch.effective_states(
            [], now=datetime(2026, 8, 28, 8, 0, tzinfo=timezone.utc), root=ROOT
        )
        by_id = {item["task_id"]: item for item in definitions}
        state_by_id = {item["task_id"]: item for item in states}
        for task_id in isolated_tasks:
            if by_id.get(task_id, {}).get("base_state") != "BLOCKED":
                errors.append(f"{task_id}: dispatch definition is not locally BLOCKED")
            if state_by_id.get(task_id, {}).get("dispatch_state") != "BLOCKED":
                errors.append(f"{task_id}: effective dispatch state is not BLOCKED")
            if by_id.get(task_id, {}).get("publication_id") is not None:
                errors.append(f"{task_id}: locally isolated task selected publication_id")

        errors.extend(integrity_isolation.audit_runtime_projection(ROOT))
    except Exception as exc:
        errors.append(str(exc))
    return errors


def main() -> int:
    errors = audit()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(
        "PASS: strict publication integrity preserved with exact task-local "
        "fork/integrity isolation and no operational selection for isolated tasks."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
