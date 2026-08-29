#!/usr/bin/env python3
"""Audit follow-up isolation across all exact nonoperational review causes.

This checker must run on the same canonical fault-isolated repository view as
live control routing.  Unrelated publication/task-local faults may block their
own task, but must not abort the follow-up authority audit globally.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import research_control_bootstrap
from control_plane import research_nonoperational_review_source_adapter as adapter


def audit() -> list[str]:
    try:
        research_control_bootstrap.install(ROOT)
        return adapter.audit(ROOT)
    except Exception as exc:
        return [str(exc)]


def main() -> int:
    errors = audit()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(
        "PASS: follow-up packets and solely-derived task publications from all exact "
        f"nonoperational review causes are isolated ({len(adapter.review_rows(ROOT))} review(s))."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
