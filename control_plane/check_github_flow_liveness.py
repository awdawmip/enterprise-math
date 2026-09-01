#!/usr/bin/env python3
"""Fail closed if GitHub validation regresses into a conversation-liveness barrier."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class GitHubFlowLivenessError(RuntimeError):
    pass


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GitHubFlowLivenessError(message)


def check() -> None:
    draft_validated = (
        ".github/workflows/quality.yml",
        ".github/workflows/reference-integrity.yml",
        ".github/workflows/lean.yml",
        ".github/workflows/bilingual-sync.yml",
    )
    for path in draft_validated:
        text = read(path)
        require(
            "github.event.pull_request.draft == false" not in text,
            f"{path}: Draft PRs must remain validation-capable; Draft is review readiness, not a CI-off switch",
        )
        require(
            "cancel-in-progress: true" in text,
            f"{path}: obsolete validation runs must be cancelled on a newer head",
        )

    quality = read(".github/workflows/quality.yml")
    for marker in (
        "unit_mode:",
        "heavy_required:",
        "shard: [0, 1, 2, 3, 4, 5, 6, 7]",
        "rm -f tests/test_p017_mirror_cross.py",
        "heavy-regression:",
        "if: always()",
    ):
        require(marker in quality, f"quality.yml missing low-burden validation marker: {marker}")
    require(
        "needs.classify.outputs.unit_mode == 'full'" in quality,
        "quality.yml must reserve the sharded Python suite for classified Python-surface changes",
    )
    require(
        "needs.classify.outputs.heavy_required == 'true'" in quality,
        "quality.yml must isolate the slow P017 bounded regression",
    )

    supervisor = read(".github/workflows/cloudflare-supervisor.yml")
    require(
        "group: cloudflare-supervisor-${{ github.event_name }}-${{ github.event.pull_request.number || github.ref }}"
        in supervisor,
        "cloudflare-supervisor validation and manual deployment must use separate event-scoped concurrency groups",
    )
    require(
        "cancel-in-progress: ${{ github.event_name != 'workflow_dispatch' }}" in supervisor,
        "cloudflare-supervisor must cancel obsolete validation but never cancel an active manual deployment",
    )

    budget = read("docs/GITHUB_INTERACTION_BUDGET.md")
    require(
        "CI_PENDING_NONBLOCKING -> CONTINUE_PARENT_TASK" in budget,
        "GitHub interaction budget lost the nonblocking-CI invariant",
    )
    require(
        "do not toggle ready merely to trigger CI" in budget.lower(),
        "GitHub interaction budget must forbid Ready-state toggles used only to obtain validation",
    )

    liveness = read("active_turn_liveness.json")
    require(
        "MERGEABLE_OR_CI_OR_REVIEW_PENDING_NONBLOCKING" in liveness,
        "active-turn contract lost the nonblocking remote-boundary invariant",
    )
    require(
        "REPEATED_CI_OR_STATUS_POLL_WITHOUT_STATE_CHANGE" in liveness,
        "active-turn contract must reject unchanged CI/status polling as material progress",
    )


def main() -> int:
    check()
    print("github-flow liveness: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
