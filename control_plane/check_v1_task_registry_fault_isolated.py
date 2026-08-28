#!/usr/bin/env python3
"""Run the frozen V1 compatibility registry audit on the fault-isolated task view.

The V1 registry remains read-only compatibility state.  This wrapper only makes
its audit consume the same task-local publication/definition fault boundary as
the canonical dispatch control plane, so one unresolved immutable task fault
cannot deny service to the whole repository audit.
"""
from __future__ import annotations

from control_plane import research_publication_fault_isolation as isolation
from tools import research_task_registry


def audit() -> list[str]:
    try:
        isolation.install()
    except Exception as exc:
        return [f"cannot install canonical task-view fault isolation: {exc}"]
    return research_task_registry.audit_registry(strict=True)


def main() -> int:
    errors = audit()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    count = len(research_task_registry.load_json(research_task_registry.REGISTRY_PATH).get("tasks", []))
    print(
        "PASS: V1 compatibility registry valid on the canonical fault-isolated "
        f"task view; {count} mirrored task(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
