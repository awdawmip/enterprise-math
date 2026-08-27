#!/usr/bin/env python3
"""Integrity audit for immutable research results/reviews with narrow V1 aliases.

Writers keep the current destination-class enum. Historical immutable V1 reviews
are not rewritten solely to rename the old ``RETURN_ONLY`` spelling: when and
only when that value has no destination reference, audit treats it as the old
spelling of current ``NONE``. Every digest, linkage, disposition and terminal
check remains owned by the base result audit.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from tools import research_result_records as records

ROOT = Path(__file__).resolve().parent
LEGACY_DESTINATION_ALIAS = "RETURN_ONLY"


def compatible_review_paths(root: Path = ROOT) -> set[str]:
    out: set[str] = set()
    for review in records.iter_reviews(root):
        if (
            review.get("record_schema") == records.REVIEW_SCHEMA
            and review.get("destination_class") == LEGACY_DESTINATION_ALIAS
            and review.get("destination_ref_or_none") in (None, "")
        ):
            path = review.get("_review_path")
            if isinstance(path, str) and path:
                out.add(path)
    return out


def audit(root: Path = ROOT) -> list[str]:
    errors = records.audit(root)
    compatible = compatible_review_paths(root)
    return [
        error
        for error in errors
        if not any(
            error == f"{path}: invalid destination_class" for path in compatible
        )
    ]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Enterprise Math immutable result/review integrity with narrow V1 aliases"
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
        "PASS: research result/review records valid; legacy RETURN_ONLY is accepted "
        "only as a no-destination immutable V1 audit alias."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
