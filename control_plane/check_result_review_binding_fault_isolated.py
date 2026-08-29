#!/usr/bin/env python3
"""Audit exact stale result-review binding isolation."""
from __future__ import annotations

from pathlib import Path

from control_plane import research_result_review_binding_fault_isolation as isolation

ROOT = Path(__file__).resolve().parents[1]


def audit() -> list[str]:
    return isolation.audit(ROOT)


def main() -> int:
    errors = audit()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(
        "PASS: exact stale result-review binding history is nonoperational "
        f"({len(isolation.quarantine_rows(ROOT))} isolated review(s))."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
