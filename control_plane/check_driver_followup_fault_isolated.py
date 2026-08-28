#!/usr/bin/env python3
"""Canonical automatic-follow-up gate with exact nonoperational-source isolation."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import research_control_bootstrap  # noqa: E402
from control_plane import research_driver_followup_fault_isolation as isolation  # noqa: E402
import research_driver_followup_guard as guard  # noqa: E402


def audit() -> list[str]:
    errors: list[str] = []
    try:
        research_control_bootstrap.install(ROOT)
        errors.extend(isolation.audit(ROOT))
        errors.extend(guard.audit(ROOT))
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
        "PASS: automatic Driver follow-up authority is valid after exact isolation of "
        f"{len(isolation.quarantine_rows(ROOT))} nonoperational-source packet(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
