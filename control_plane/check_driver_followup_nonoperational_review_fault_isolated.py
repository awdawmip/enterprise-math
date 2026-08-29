#!/usr/bin/env python3
"""Audit follow-up isolation across all exact nonoperational review causes."""
from __future__ import annotations

from pathlib import Path

from control_plane import research_nonoperational_review_source_adapter as adapter

ROOT = Path(__file__).resolve().parents[1]


def audit() -> list[str]:
    return adapter.audit(ROOT)


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
