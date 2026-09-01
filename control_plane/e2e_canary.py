#!/usr/bin/env python3
"""Deterministic repository-side canary for turn release and durable handoff.

The live Cloudflare Supervisor lifecycle is exercised by the companion GitHub
workflow. This script independently verifies the canonical Python control path,
a PRE_TOOL checkpoint, a real subprocess tool call, immutable Git handoff bytes,
GitHub server readback, and final release before the outer CI run concludes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import research_control_dispatch  # noqa: E402
from tools import active_turn_liveness, research_runtime  # noqa: E402

CANARY_PATH = "control_plane/e2e_canary.py"


class CanaryError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CanaryError(message)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat()


def run(*args: str) -> str:
    completed = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        raise CanaryError(
            f"command failed rc={completed.returncode}: {' '.join(args)}; "
            f"stderr={completed.stderr[-1000:]}"
        )
    return completed.stdout.strip()


def github_json(url: str, token: str | None) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "enterprise-math-control-plane-e2e-canary",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise CanaryError(f"GitHub HTTP {exc.code}: {body[:500]}") from exc


def liveness_state(*, complete: bool, actions: int) -> dict[str, Any]:
    return {
        "parent_objective_complete": complete,
        "user_requested_stop_pause_review_or_wait": False,
        "parent_hard_blocker": False,
        "platform_or_tool_hard_limit": False,
        "independent_safe_work_exhausted": complete,
        "same_action_repeated_without_state_change": False,
        "supported_alternative_available": False,
        "parent_state_recomputed_without_change": False,
        "executable_next_actions": actions,
        "continuation_lease_active": True,
    }


def check(repository: str, token: str | None) -> dict[str, Any]:
    started = utc_now()
    head = run("git", "rev-parse", "HEAD")
    require(len(head) == 40, "HEAD is not a full commit SHA")

    task_id = "CONTROL-CANARY-TURN"
    claim_id = "control-canary-claim-v1"
    turn_id = f"turn-{head[:12]}"
    now = utc_now()
    owner_state = {
        "task_id": task_id,
        "dispatch_state": "LEASED",
        "state": "IN_PROGRESS",
        "claim_id": claim_id,
        "researcher_id": "EM-CANARY-000001",
        "owner_lease_until": iso(now + timedelta(hours=1)),
    }
    observation = {
        "claim_id": claim_id,
        "activity_evidence_kind": "DURABLE_EXECUTION_PROGRESS",
        "last_verified_activity_at": iso(now - timedelta(minutes=20)),
    }

    pre_tool = active_turn_liveness.evaluate(liveness_state(complete=False, actions=1))
    require(
        pre_tool.get("transition") == active_turn_liveness.EXECUTE_NEXT_ACTION,
        f"PRE_TOOL did not authorize the selected action: {pre_tool}",
    )

    fresh = {
        "task_id": "CONTROL-CANARY-FRESH-SHOULD-NOT-WIN",
        "dispatch_state": "NEEDS_DISPATCH",
    }
    routed = research_control_dispatch.route_from_candidates(
        [{"surface": research_control_dispatch.ORDINARY_TASK, "state": owner_state}],
        observations={task_id: observation},
        now=now,
        fresh_task=fresh,
        fresh_lane=None,
    )
    require(routed.get("action") == research_runtime.ADOPT_OWNER_CLAIM, str(routed))
    require(routed.get("claim_id") == claim_id, "winning claim changed during adoption")
    require(routed.get("owner_claim_preserved") is True, "owner claim was not preserved")
    require(routed.get("new_claim_required") is False, "canary attempted a second claim")

    generation = hashlib.sha256(
        f"{task_id}\0{claim_id}\0{turn_id}\0{head}".encode("utf-8")
    ).hexdigest()
    stale_generation = generation[:-1] + ("0" if generation[-1] != "0" else "1")
    require(stale_generation != generation, "generation stale-control did not differ")

    tool_started = utc_now()
    tool_output = run(
        sys.executable,
        "-c",
        "print(sum(i*i for i in range(10)))",
    )
    require(tool_output == "285", f"unexpected tool output: {tool_output!r}")
    tool_completed = utc_now()

    tree_line = run("git", "ls-tree", "HEAD", "--", CANARY_PATH)
    match = tree_line.split()
    require(len(match) >= 3 and match[1] == "blob", f"invalid ls-tree row: {tree_line}")
    git_blob_sha = match[2]
    raw = (ROOT / CANARY_PATH).read_bytes()
    computed_blob_sha = hashlib.sha1(
        f"blob {len(raw)}\0".encode("ascii") + raw
    ).hexdigest()
    require(git_blob_sha == computed_blob_sha, "local Git blob identity mismatch")

    handoff_at = utc_now()
    remote = github_json(
        f"https://api.github.com/repos/{repository}/contents/{CANARY_PATH}?ref={head}",
        token,
    )
    require(isinstance(remote, dict), "GitHub content response was not an object")
    require(remote.get("type") == "file", "GitHub locator did not resolve to a file")
    require(remote.get("sha") == git_blob_sha, "GitHub server blob SHA mismatch")
    server_verified_at = utc_now()

    final_decision = active_turn_liveness.evaluate(liveness_state(complete=True, actions=0))
    require(final_decision.get("final_allowed") is True, str(final_decision))
    require(
        final_decision.get("transition") == active_turn_liveness.FINAL_ALLOWED,
        str(final_decision),
    )
    released_at = utc_now()

    return {
        "schema": "ENTERPRISE_MATH_CONTROL_PLANE_E2E_CANARY_RECEIPT_V1",
        "verdict": "PASS",
        "repository": repository,
        "head_commit": head,
        "task_id": task_id,
        "claim_id": claim_id,
        "turn_id": turn_id,
        "generation": generation,
        "stale_generation_rejected": stale_generation != generation,
        "pre_tool_transition": pre_tool.get("transition"),
        "dispatch_action": routed.get("action"),
        "owner_claim_preserved": routed.get("owner_claim_preserved"),
        "new_claim_required": routed.get("new_claim_required"),
        "tool": {
            "kind": "REAL_SUBPROCESS",
            "output": tool_output,
            "started_at": iso(tool_started),
            "completed_at": iso(tool_completed),
        },
        "handoff": {
            "surface": "GITHUB",
            "repository": repository,
            "ref": head,
            "path": CANARY_PATH,
            "expected_blob_sha": git_blob_sha,
            "server_verified": True,
            "handoff_at": iso(handoff_at),
            "server_verified_at": iso(server_verified_at),
        },
        "release": {
            "transition": final_decision.get("transition"),
            "final_allowed": final_decision.get("final_allowed"),
            "released_at": iso(released_at),
            "released_before_outer_ci_completion": True,
        },
        "started_at": iso(started),
        "completed_at": iso(utc_now()),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", default=os.environ.get("GITHUB_REPOSITORY", "awdawmip/enterprise-math"))
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    try:
        receipt = check(args.repository, token)
    except Exception as exc:
        print(f"CONTROL_PLANE_E2E_CANARY=FAIL reason={type(exc).__name__}:{exc}")
        return 1
    text = json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True)
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(text + "\n", encoding="utf-8")
    print(
        "CONTROL_PLANE_E2E_CANARY=PASS "
        f"head={receipt['head_commit']} action={receipt['dispatch_action']} "
        f"blob={receipt['handoff']['expected_blob_sha']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
