#!/usr/bin/env python3
"""Reference-integrity checker for task-local publication-fork isolation."""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import research_publication_fault_isolation as isolation  # noqa: E402


def audit() -> list[str]:
    errors = list(isolation.audit())
    if errors:
        return errors

    try:
        isolation.install()
        import research_operational_publications as operational
        from tools import research_dispatch

        quarantines = isolation.validated_quarantines()
        heads = operational.publication_heads()
        resolutions = operational.resolution_map()

        # Preserve the existing operational-publication contract everywhere
        # except the exact unresolved forks that have explicitly selected no head.
        for task_id in sorted(heads):
            if task_id in quarantines:
                if task_id in resolutions:
                    errors.append(
                        f"{task_id}: unresolved fork quarantine cannot coexist with operational resolution"
                    )
                continue
            try:
                operational.selection(task_id)
            except Exception as exc:
                errors.append(str(exc))

        definitions = research_dispatch.merged_definitions()
        states = research_dispatch.effective_states(
            [], now=datetime(2026, 8, 28, 8, 0, tzinfo=timezone.utc)
        )
        by_id = {item["task_id"]: item for item in definitions}
        state_by_id = {item["task_id"]: item for item in states}
        for task_id in quarantines:
            if by_id.get(task_id, {}).get("base_state") != "BLOCKED":
                errors.append(f"{task_id}: dispatch definition is not locally BLOCKED")
            if state_by_id.get(task_id, {}).get("dispatch_state") != "BLOCKED":
                errors.append(f"{task_id}: effective dispatch state is not BLOCKED")
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
        "PASS: strict publication integrity preserved with explicit task-local "
        "unresolved-fork isolation."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
