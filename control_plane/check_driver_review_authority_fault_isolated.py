#!/usr/bin/env python3
"""Canonical source-backed Driver review-provenance gate with exact local isolation."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import research_result_review_binding_fault_isolation as binding_isolation  # noqa: E402
from control_plane import research_result_review_audit_fault_isolation as review_audit_isolation  # noqa: E402
from control_plane import research_driver_review_authority_fault_isolation as isolation  # noqa: E402
import research_driver_authority as driver_authority  # noqa: E402


def audit() -> list[str]:
    errors: list[str] = []
    try:
        driver_authority.contract(ROOT)
        records = driver_authority.valid_records(ROOT)
        if not records:
            errors.append("Driver authority contract is active but no authority records exist")

        # Authority provenance is checked only on the operational review view.
        # Reviews already proven nonoperational by exact stale-binding or strict
        # structural-integrity isolation must not be judged a second time here.
        binding_isolation.validated_quarantines(ROOT)
        binding_isolation.install(ROOT)
        review_audit_isolation.validated_rows(ROOT)
        review_audit_isolation.install(ROOT)

        errors.extend(isolation.audit(ROOT))
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
        "PASS: source-backed Driver authority is valid on the operational review view; "
        "prior exact nonoperational review faults are consumed before authority audit and "
        f"{len(isolation.quarantine_rows(ROOT))} additional authority-invalid review(s) are isolated."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
