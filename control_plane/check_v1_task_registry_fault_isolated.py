#!/usr/bin/env python3
"""Run the frozen V1 compatibility registry audit on the fault-isolated task view.

The V1 registry remains read-only compatibility state. This wrapper only makes
its audit consume the same canonical task-local fault boundary as live dispatch,
so one known immutable task fault cannot deny service to the whole audit.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import research_control_bootstrap  # noqa: E402
from tools import research_task_registry  # noqa: E402


def audit() -> list[str]:
    try:
        research_control_bootstrap.install(ROOT)
    except Exception as exc:
        return [f"cannot install canonical task-view fault isolation: {exc}"]
    return research_task_registry.audit_registry(strict=True)


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
