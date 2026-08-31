#!/usr/bin/env python3
"""Audit multiple Driver-review exact-set authority on the operational review view.

Earlier canonical integrity/authority layers may prove immutable review records
nonoperational.  This wrapper composes those exact, byte-pinned decisions before
running the strict review-evidence reducer.  The reducer itself remains unchanged:
all surviving operational reviews must still satisfy its schema and every
intake/pass/synthesis must cover the exact current review set.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import research_control_bootstrap  # noqa: E402
from control_plane import research_result_review_binding_fault_isolation as binding_isolation  # noqa: E402
from control_plane import research_result_review_audit_fault_isolation as structural_isolation  # noqa: E402
from control_plane import research_driver_review_authority_fault_isolation as authority_isolation  # noqa: E402
import research_driver_authority as driver_authority  # noqa: E402


def audit() -> list[str]:
    errors: list[str] = []
    try:
        research_control_bootstrap.install(ROOT)

        binding_isolation.validated_quarantines(ROOT)
        binding_isolation.install(ROOT)

        structural_isolation.validated_rows(ROOT)
        structural_isolation.install(ROOT)

        driver_authority.contract(ROOT)
        driver_authority.valid_records(ROOT)
        authority_errors = authority_isolation.quarantine_authority_errors(
            driver_authority.review_authority_errors,
            legacy_review_ids=driver_authority.legacy_review_ids(ROOT),
            root=ROOT,
        )
        if authority_errors:
            return authority_errors
        authority_isolation.install(ROOT)

        import research_review_evidence

        errors.extend(research_review_evidence.audit(ROOT))
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
        "PASS: multiple Driver-review exact-set authority is valid on the canonical "
        "operational review view after prior exact nonoperational review isolation."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
