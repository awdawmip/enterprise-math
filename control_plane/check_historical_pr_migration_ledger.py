#!/usr/bin/env python3
"""Validate the compact exhaustive historical-PR authority migration ledger."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "historical_pr_migration_ledger.json"
SCHEMA = "ENTERPRISE_MATH_HISTORICAL_PR_MIGRATION_LEDGER_V1"


def audit() -> list[str]:
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    errors: list[str] = []
    if data.get("schema") != SCHEMA:
        errors.append("wrong historical PR migration ledger schema")
    if data.get("status") != "ACTIVE":
        errors.append("historical PR migration ledger must be ACTIVE")
    if data.get("scope") != "CONTROL_PLANE_PR_AUTHORITY":
        errors.append("historical PR ledger scope must remain control-plane authority")

    inv = data.get("inventory_snapshot")
    if not isinstance(inv, dict):
        return errors + ["missing inventory_snapshot"]
    start = inv.get("number_space_start")
    end = inv.get("number_space_end")
    cutoff = inv.get("cutoff_pr_number")
    issues = inv.get("non_pr_issue_numbers")
    if not isinstance(start, int) or not isinstance(end, int) or not isinstance(cutoff, int):
        return errors + ["inventory number-space bounds must be integers"]
    if start != 1 or end != cutoff or cutoff != 659:
        errors.append("historical inventory cutoff must remain the pinned pre-#660 range 1..659")
    if not isinstance(issues, list) or any(not isinstance(n, int) for n in issues):
        return errors + ["non_pr_issue_numbers must be an integer list"]
    if issues != sorted(set(issues)):
        errors.append("non_pr_issue_numbers must be sorted and unique")
    if any(n < start or n > end for n in issues):
        errors.append("non-PR issue number lies outside the historical number space")
    if inv.get("non_pr_issue_count") != len(issues):
        errors.append("non_pr_issue_count mismatch")
    expected_pr_count = end - start + 1 - len(issues)
    if inv.get("historical_pr_count") != expected_pr_count:
        errors.append("historical_pr_count does not equal range minus non-PR issues")
    if expected_pr_count != 614:
        errors.append(f"expected exactly 614 historical PRs, got {expected_pr_count}")
    if inv.get("inventory_complete") is not True:
        errors.append("historical PR inventory must be marked complete")

    evidence = inv.get("derivation_evidence", {})
    if evidence.get("github_search_pr_count_through_current_pr_660") != 615:
        errors.append("pinned GitHub PR count evidence mismatch")
    if evidence.get("github_search_issue_count_through_number_660") != 45:
        errors.append("pinned GitHub issue count evidence mismatch")
    if evidence.get("max_observed_number_for_derivation") != 660:
        errors.append("pinned max-number evidence mismatch")
    if evidence.get("current_migration_pr_number_excluded_from_history") != 660:
        errors.append("PR #660 must remain excluded from the historical snapshot")

    migration = data.get("migration")
    if not isinstance(migration, dict):
        return errors + ["missing migration policy"]
    if migration.get("control_plane_authority_migration_complete") is not True:
        errors.append("control-plane historical authority migration must be complete")
    if migration.get("historical_pr_metadata_runtime_effect") != "NONE":
        errors.append("historical PR metadata must have no runtime effect")
    if migration.get("github_pr_state_is_not_runtime_state") is not True:
        errors.append("GitHub PR state must not be treated as canonical runtime state")

    guards = data.get("authority_guards", {})
    for field in (
        "working_truth_granted",
        "task_authority_granted_by_history_only",
        "foundation_authority_granted_by_history_only",
        "canonical_promotion_granted_by_history_only",
        "successor_triggered_by_history_only",
    ):
        if guards.get(field) is not False:
            errors.append(f"historical authority guard must be false: {field}")
    return errors


if __name__ == "__main__":
    failures = audit()
    if failures:
        for failure in failures:
            print("ERROR:", failure)
        raise SystemExit(1)
    print("PASS: 614 historical PRs are exhaustively inventoried and PR metadata has no runtime authority.")
