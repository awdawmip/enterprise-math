#!/usr/bin/env python3
"""Fail closed if the control-plane end-to-end canary stops proving turn release.

The canary is deliberately ordered around the key liveness claim:

PRE_TOOL checkpoint -> tool call -> generation recheck -> progress ->
immutable handoff verification -> turn completion/release -> one bounded
GitHub CI snapshot -> reconciliation that preserves the completed turn.

GitHub CI and branch enforcement remain integration evidence. They never become
the owner-scope conversation lease that authorizes or keeps a turn RUNNING.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ControlPlaneCanaryError(RuntimeError):
    pass


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ControlPlaneCanaryError(message)


def ordered(text: str, *markers: str) -> None:
    cursor = -1
    for marker in markers:
        position = text.find(marker, cursor + 1)
        require(position >= 0, f"canary missing marker: {marker}")
        require(position > cursor, f"canary marker is out of order: {marker}")
        cursor = position


def check() -> None:
    smoke = read("infrastructure/cloudflare-supervisor/scripts/smoke-live.mjs")
    ordered(
        smoke,
        'current_action: "PRE_TOOL_CHECKPOINT"',
        'name: "supervisor_snapshot"',
        'name: "handoff_verify"',
        'const postToolSnapshot',
        'current_action: "POST_TOOL_PROGRESS"',
        'name: "turn_complete"',
        'const releasedBeforeCi',
        'const ciSnapshot = await githubCheckSnapshot',
        'const reconciledAfterCi',
        'name: "github_enforcement_status"',
    )
    for marker in (
        "pre_tool_checkpoint_verified: true",
        "generation_recheck_verified: true",
        "turn_released_before_ci_observation: true",
        "reconciliation_preserved_completed_turn: true",
        "blocks_turn: false",
        'schema: "ENTERPRISE_MATH_CONTROL_PLANE_E2E_CANARY_V1"',
        "github_enforcement_match: enforcementMatch",
    ):
        require(marker in smoke, f"live canary lost required evidence marker: {marker}")

    require(
        smoke.count("githubCheckSnapshot(") == 2,
        "canary must define and execute exactly one bounded GitHub check snapshot",
    )
    for forbidden in (
        "WAITING_FOR_CI",
        "WAITING_FOR_GITHUB_ENFORCEMENT",
        "while (ci",
        "for (let attempt = 1; attempt <= 12",
    ):
        require(
            forbidden not in smoke,
            f"live canary must not poll asynchronous integration state: {forbidden}",
        )

    owner_test = read(
        "infrastructure/cloudflare-supervisor/test/owner-scope.test.ts"
    )
    for marker in (
        'it("releases the turn before asynchronous CI reconciliation"',
        'status: "COMPLETED"',
        "CI_PENDING_NONBLOCKING",
        "completed scope cannot be reopened",
    ):
        require(
            marker in owner_test,
            f"local owner-scope canary lost marker: {marker}",
        )

    workflow = read(".github/workflows/cloudflare-supervisor-live-canary.yml")
    for marker in (
        "name: control-plane-e2e-canary",
        "control_plane/apply_github_enforcement.py",
        "scripts/access-ci-identity.mjs create",
        "scripts/smoke-live.mjs",
        "scripts/access-ci-identity.mjs revoke",
        "if: always()",
        "control-plane-e2e-canary-report",
        "turn_released_before_ci_observation",
        "github_enforcement_match",
    ):
        require(marker in workflow, f"live canary workflow missing marker: {marker}")

    require(
        workflow.index("control_plane/apply_github_enforcement.py")
        < workflow.index("scripts/smoke-live.mjs"),
        "live canary must apply/verify GitHub enforcement before observing it",
    )
    require(
        workflow.index("scripts/smoke-live.mjs")
        < workflow.index("scripts/access-ci-identity.mjs revoke"),
        "ephemeral Access identity must be revoked after the live canary",
    )

    provision = read(".github/workflows/github-enforcement-provision.yml")
    require(
        "IDEMPOTENT_APPLY_THEN_VERIFY" in read(
            "control_plane/apply_github_enforcement.py"
        ),
        "GitHub enforcement tool lost idempotent apply-and-verify semantics",
    )
    require(
        "github-enforcement-report" in provision,
        "scheduled enforcement workflow must retain an auditable report",
    )


def main() -> int:
    check()
    print("control-plane end-to-end canary contract: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
