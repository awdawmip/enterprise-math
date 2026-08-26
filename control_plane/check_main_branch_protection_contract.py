#!/usr/bin/env python3
"""Validate that the unresolved main-protection blocker is explicit and non-overclaimed."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "main_branch_protection_contract.json"
SCHEMA = "ENTERPRISE_MATH_MAIN_BRANCH_PROTECTION_CONTRACT_V1"


def audit() -> list[str]:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    errors: list[str] = []
    if data.get("schema") != SCHEMA:
        errors.append("wrong main branch protection contract schema")
    if data.get("status") != "REQUIRED_NOT_YET_ENFORCED":
        errors.append("contract must not claim protection is enforced before GitHub proves it")
    if data.get("branch") != "main":
        errors.append("protection contract must target main")
    if data.get("observed_protected") is not False:
        errors.append("pinned observation must remain false until refreshed after settings change")
    if data.get("blocking_issue") != 662:
        errors.append("branch-protection blocker must remain linked to Issue #662")
    required = data.get("required_controls", {})
    for field in (
        "pull_request_required",
        "strict_up_to_date_before_merge",
        "force_push_blocked",
        "branch_deletion_blocked",
    ):
        if required.get(field) is not True:
            errors.append(f"required branch control missing: {field}")
    if required.get("ordinary_driver_bypass_allowed") is not False:
        errors.append("ordinary Driver bypass must be forbidden")
    if required.get("ordinary_researcher_bypass_allowed") is not False:
        errors.append("ordinary researcher bypass must be forbidden")
    if set(required.get("required_workflows", [])) != {"quality", "bilingual-sync", "reference-integrity"}:
        errors.append("required workflow set mismatch")
    if data.get("hard_enforcement_state") != "PARTIAL_UNTIL_GITHUB_SETTING_ENFORCED":
        errors.append("hard enforcement state must remain partial")
    for field in ("working_truth_granted", "canonical_promotion_granted", "successor_triggered"):
        if data.get(field) is not False:
            errors.append(f"control-plane protection contract may not grant {field}")
    return errors


if __name__ == "__main__":
    failures = audit()
    if failures:
        for failure in failures:
            print("ERROR:", failure)
        raise SystemExit(1)
    print("PASS: main protection blocker is explicit and not overclaimed as enforced.")
