#!/usr/bin/env python3
"""Current-policy audit wrapper for immutable task publication history.

The canonical task publication writer/reducer remains ``tools.research_task_records``.
Its legacy V2 audit predates lossless parallel-publication retention and applies
current executable body-shape requirements to every historical V2 record.

This wrapper preserves every base integrity check, but treats one narrow class as
historical compatibility rather than corruption: a publication explicitly listed
as non-operational by a valid publication resolution may retain its original body
section naming. Blob pins, schemas, task IDs, parent-objective pins, resolution
set completeness and every other base error remain fatal.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from tools import research_task_records as records

ROOT = Path(__file__).resolve().parent
_BODY_SHAPE_MARKERS = (
    "mandatory body section is missing or empty:",
    "mandatory body section contains placeholder text:",
)


def retained_nonoperational_record_paths(root: Path = ROOT) -> set[str]:
    out: set[str] = set()
    for task_id, resolution in records.publication_resolutions(root).items():
        for publication_id in resolution.get("quarantined_publication_ids", []):
            out.add(
                f"research_task_records/{task_id}/{publication_id}.json"
            )
    return out


def _is_retained_body_shape_error(error: str, retained: set[str]) -> bool:
    for path in retained:
        prefix = path + ": "
        if error.startswith(prefix) and any(
            marker in error[len(prefix) :] for marker in _BODY_SHAPE_MARKERS
        ):
            return True
    return False


def audit(root: Path = ROOT) -> list[str]:
    # Base audit still owns all immutable-chain integrity. A malformed resolution
    # fails inside current_records/publication_resolutions before any compatibility
    # filtering can occur.
    base_errors = records.audit(root)
    try:
        retained = retained_nonoperational_record_paths(root)
    except Exception as exc:
        return [*base_errors, f"publication-resolution compatibility audit failed: {exc}"]
    return [
        error
        for error in base_errors
        if not _is_retained_body_shape_error(error, retained)
    ]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Enterprise Math task publication integrity with retained-history compatibility"
    )
    parser.add_argument("command", choices=["audit"])
    args = parser.parse_args()
    if args.command != "audit":
        raise AssertionError(args.command)
    errors = audit()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(
        "PASS: immutable task publication records valid; retained non-operational "
        "history is exempt only from current executable body-shape naming."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
