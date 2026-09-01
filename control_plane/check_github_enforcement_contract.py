#!/usr/bin/env python3
"""Validate stable required checks and the repository-side protection contract."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "control_plane" / "github_enforcement_contract.json"


class GithubEnforcementContractError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GithubEnforcementContractError(message)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def event_block(workflow: str, event: str) -> str:
    marker = f"  {event}:"
    start = workflow.find(marker)
    require(start >= 0, f"workflow missing {event} trigger")
    tail = workflow[start + len(marker) :]
    match = re.search(r"(?m)^  [A-Za-z_][A-Za-z0-9_-]*:\s*$", tail)
    return tail[: match.start()] if match else tail


def job_block(workflow: str, job_id: str) -> str:
    marker = f"  {job_id}:"
    start = workflow.find(marker)
    require(start >= 0, f"workflow missing stable job id {job_id}")
    tail = workflow[start + len(marker) :]
    match = re.search(r"(?m)^  [A-Za-z_][A-Za-z0-9_-]*:\s*$", tail)
    return tail[: match.start()] if match else tail


def protection_payload(contract: dict[str, Any]) -> dict[str, Any]:
    policy = contract["branch_protection"]
    return {
        "required_status_checks": {
            "strict": policy["strict_status_checks"],
            "contexts": [],
            "checks": [
                {
                    "context": context,
                    "app_id": contract["status_check_app"]["app_id"],
                }
                for context in contract["required_status_checks"]
            ],
        },
        "enforce_admins": policy["enforce_admins"],
        "required_pull_request_reviews": {
            "dismiss_stale_reviews": False,
            "require_code_owner_reviews": False,
            "required_approving_review_count": policy[
                "required_approving_review_count"
            ],
            "require_last_push_approval": False,
        }
        if policy["require_pull_request"]
        else None,
        "restrictions": None,
        "required_linear_history": policy["required_linear_history"],
        "allow_force_pushes": policy["allow_force_pushes"],
        "allow_deletions": policy["allow_deletions"],
        "block_creations": False,
        "required_conversation_resolution": policy[
            "required_conversation_resolution"
        ],
        "lock_branch": False,
        "allow_fork_syncing": False,
    }


def check() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    require(
        contract.get("schema")
        == "ENTERPRISE_MATH_GITHUB_ENFORCEMENT_CONTRACT_V1",
        "unexpected GitHub enforcement contract schema",
    )
    require(contract.get("status") == "ACTIVE_CANONICAL", "contract is not active")
    require(
        contract.get("repository") == "awdawmip/enterprise-math",
        "enforcement repository drifted",
    )
    require(contract.get("branch") == "main", "enforcement branch must be main")

    app = contract.get("status_check_app", {})
    require(
        app.get("slug") == "github-actions" and app.get("app_id") == 15368,
        "required checks must remain pinned to the GitHub Actions app",
    )

    checks = contract.get("required_status_checks")
    require(
        isinstance(checks, list)
        and checks
        and all(isinstance(item, str) and item for item in checks),
        "required_status_checks must be a nonempty string list",
    )
    require(len(checks) == len(set(checks)), "required check names must be unique")

    workflow_by_check = {
        "quality-gate": ".github/workflows/quality.yml",
        "reference-integrity-gate": ".github/workflows/reference-integrity.yml",
        "bilingual-sync-gate": ".github/workflows/bilingual-sync.yml",
        "lean-gate": ".github/workflows/lean.yml",
    }
    require(
        set(checks) == set(workflow_by_check),
        "required check set drifted from the stable workflow map",
    )

    for check_name, path in workflow_by_check.items():
        workflow = read(path)
        require(
            f"name: {check_name}" in job_block(workflow, check_name),
            f"{path}: stable gate must have explicit name {check_name}",
        )
        pr = event_block(workflow, "pull_request")
        require(
            "paths:" not in pr and "paths-ignore:" not in pr,
            f"{path}: required gate must be emitted on every pull request",
        )
        require(
            "types: [opened, synchronize, reopened]" in pr,
            f"{path}: required gate must validate opened/synchronized/reopened heads",
        )
        require(
            "cancel-in-progress: true" in workflow,
            f"{path}: superseded validation heads must be cancelled",
        )

    lean = read(".github/workflows/lean.yml")
    require(
        "Determine whether Lean validation is required" in lean
        and "Record no-op Lean gate" in lean,
        "lean-gate must remain always emitted while compiling only Lean changes",
    )

    quality = read(".github/workflows/quality.yml")
    require(
        "if: always()" in job_block(quality, "quality-gate"),
        "quality-gate must aggregate skipped/applicable jobs deterministically",
    )

    provision = read(".github/workflows/github-enforcement-provision.yml")
    for marker in (
        "control_plane/apply_github_enforcement.py",
        "actions/create-github-app-token@v2",
        "GITHUB_ADMIN_TOKEN",
        "GITHUB_ENFORCEMENT_TOKEN",
        "github-enforcement-report",
    ):
        require(marker in provision, f"provisioning workflow missing marker: {marker}")

    tool = read("control_plane/apply_github_enforcement.py")
    serialized = json.dumps(protection_payload(contract), sort_keys=True)
    require(
        "IDEMPOTENT_APPLY_THEN_VERIFY" in tool,
        "enforcement tool must declare apply-then-verify semantics",
    )
    require(
        "required_status_checks" in tool and "required_pull_request_reviews" in tool,
        "enforcement tool must apply status and pull-request protection",
    )
    require(
        serialized == json.dumps(protection_payload(contract), sort_keys=True),
        "protection payload construction is nondeterministic",
    )

    cutover = contract.get("cutover", {})
    require(
        cutover.get("missing_new_gate_on_old_head_is_not_conversation_blocker")
        is True,
        "pre-cutover PR heads must not become conversation blockers",
    )
    require(
        cutover.get("do_not_bulk_touch_research_heads_only_to_create_checks")
        is True,
        "do not mutate research heads merely to manufacture new check contexts",
    )

    liveness = contract.get("liveness", {})
    require(
        liveness.get("required_checks_are_integration_gates_not_conversation_leases")
        is True,
        "required checks must not become conversation leases",
    )
    require(
        liveness.get("pending_ci_keeps_turn_released") is True,
        "pending CI must preserve released turn state",
    )


def main() -> int:
    check()
    print("github enforcement contract: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
