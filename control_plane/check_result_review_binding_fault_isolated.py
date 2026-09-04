#!/usr/bin/env python3
"""Audit exact result/review historical fault isolation without semantic repair."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import research_result_review_binding_fault_isolation as binding_isolation
from control_plane import research_result_review_audit_fault_isolation as review_audit_isolation
from control_plane import research_result_record_audit_fault_isolation as result_audit_isolation


def audit() -> list[str]:
    errors: list[str] = []
    try:
        binding_rows = binding_isolation.validated_quarantines(ROOT)
        binding_isolation.install(ROOT)

        review_rows = review_audit_isolation.validated_rows(ROOT)
        review_audit_isolation.install(ROOT)

        result_audit_isolation.validated_rows(ROOT)

        from tools import research_result_records

        operational_review_ids = {
            str(item.get("review_id"))
            for item in research_result_records.iter_reviews(ROOT)
            if isinstance(item.get("review_id"), str)
        }
        leaked_binding = sorted(set(binding_rows) & operational_review_ids)
        leaked_invalid = sorted(set(review_rows) & operational_review_ids)
        if leaked_binding:
            errors.append(
                f"{binding_isolation.QUARANTINE_FILE}: stale-binding reviews remain operational: {leaked_binding}"
            )
        if leaked_invalid:
            errors.append(
                f"{review_audit_isolation.QUARANTINE_FILE}: invalid reviews remain operational: {leaked_invalid}"
            )

        strict_errors = research_result_records.audit(ROOT)
        errors.extend(result_audit_isolation.audit_against(strict_errors, ROOT))
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
        "PASS: result/review integrity preserved with exact stale-binding review isolation, "
        "exact invalid-review isolation, and audit-only superseded-result containment; "
        f"binding_reviews={len(binding_isolation.quarantine_rows(ROOT))}; "
        f"invalid_reviews={len(review_audit_isolation.quarantine_rows(ROOT))}; "
        f"superseded_result_audit_rows={len(result_audit_isolation.quarantine_rows(ROOT))}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
