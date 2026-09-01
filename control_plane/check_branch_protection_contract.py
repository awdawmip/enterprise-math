#!/usr/bin/env python3
"""Reconcile the declared main-branch protection mode with live GitHub state.

This checker is deliberately control-plane only. It never changes repository
settings and never interprets mathematical truth. The current contract keeps the
emergency direct-main repair lane open until an administration-authorized,
read-back-verified ruleset with an exact bypass actor can be installed.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "control_plane" / "branch_protection_contract.json"


class BranchProtectionContractError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise BranchProtectionContractError(message)


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"{path}: expected JSON object")
    return value


def github_json(url: str, token: str | None) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "enterprise-math-branch-protection-reconciler",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise BranchProtectionContractError(
            f"GitHub read failed HTTP {exc.code} for {url}: {body[:500]}"
        ) from exc


def workflow_jobs(text: str) -> dict[str, str]:
    jobs: dict[str, str] = {}
    in_jobs = False
    current: str | None = None
    for line in text.splitlines():
        if re.fullmatch(r"jobs:\s*", line):
            in_jobs = True
            current = None
            continue
        if in_jobs and line and not line.startswith(" "):
            in_jobs = False
            current = None
        if not in_jobs:
            continue
        match = re.fullmatch(r"  ([A-Za-z0-9_-]+):\s*", line)
        if match:
            current = match.group(1)
            jobs[current] = current
            continue
        match = re.fullmatch(r"    name:\s*(.+?)\s*", line)
        if current and match:
            jobs[current] = match.group(1).strip().strip("\"'")
    return jobs


def inspect_workflows(contract: dict[str, Any]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    names: dict[str, list[str]] = {}
    for rel in contract.get("core_workflows", []):
        require(isinstance(rel, str) and rel, "core_workflows entries must be paths")
        path = ROOT / rel
        require(path.is_file(), f"missing core workflow: {rel}")
        text = path.read_text(encoding="utf-8")
        jobs = workflow_jobs(text)
        require(jobs, f"{rel}: no jobs found")
        for job_id, display_name in jobs.items():
            names.setdefault(display_name, []).append(f"{rel}#{job_id}")
        rows.append(
            {
                "path": rel,
                "jobs": jobs,
                "pull_request": bool(re.search(r"^\s{2}pull_request:\s*$", text, re.MULTILINE)),
                "push": bool(re.search(r"^\s{2}push:\s*$", text, re.MULTILINE)),
                "workflow_dispatch": bool(
                    re.search(r"^\s{2}workflow_dispatch:\s*$", text, re.MULTILINE)
                ),
                "cancel_in_progress": "cancel-in-progress: true" in text,
                "ready_for_review_trigger": "ready_for_review" in text,
            }
        )
    duplicates = {
        name: locations for name, locations in names.items() if len(locations) > 1
    }
    forbidden = set(contract.get("forbidden_required_contexts", []))
    observed_forbidden = sorted(forbidden.intersection(names))
    return {
        "workflows": rows,
        "duplicate_check_names": duplicates,
        "observed_forbidden_context_names": observed_forbidden,
    }


def check(token: str | None = None) -> dict[str, Any]:
    contract = load_json(CONTRACT)
    require(
        contract.get("schema") == "ENTERPRISE_MATH_BRANCH_PROTECTION_RECONCILIATION_V1",
        "unexpected branch-protection contract schema",
    )
    require(contract.get("status") == "ACTIVE_CANONICAL_CONTROL_ONLY", "contract not active")
    repository = contract.get("repository")
    branch = contract.get("branch")
    require(isinstance(repository, str) and "/" in repository, "invalid repository")
    require(isinstance(branch, str) and branch, "invalid branch")

    expected = contract.get("expected_remote_state")
    require(isinstance(expected, dict), "expected_remote_state must be an object")
    expected_protected = expected.get("protected")
    require(type(expected_protected) is bool, "expected protected must be boolean")
    required_contexts = expected.get("required_status_check_contexts")
    require(isinstance(required_contexts, list), "required contexts must be a list")
    require(len(required_contexts) == len(set(required_contexts)), "duplicate required contexts")

    branch_data = github_json(
        f"https://api.github.com/repos/{repository}/branches/{branch}", token
    )
    require(isinstance(branch_data, dict), "GitHub branch response must be an object")
    actual_protected = branch_data.get("protected")
    require(type(actual_protected) is bool, "GitHub branch response missing protected boolean")
    require(
        actual_protected is expected_protected,
        f"live {repository}@{branch} protected={actual_protected}, expected={expected_protected}",
    )

    workflow_view = inspect_workflows(contract)
    if not expected_protected:
        require(
            required_contexts == [],
            "unprotected direct-main recovery mode must not pretend required contexts exist",
        )
    else:
        forbidden = set(contract.get("forbidden_required_contexts", []))
        overlap = sorted(forbidden.intersection(required_contexts))
        require(not overlap, f"forbidden ambiguous required contexts: {overlap}")
        require(required_contexts, "protected mode requires exact nonempty contexts")

    return {
        "schema": "ENTERPRISE_MATH_BRANCH_PROTECTION_RECONCILIATION_RECEIPT_V1",
        "repository": repository,
        "branch": branch,
        "main_sha": branch_data.get("commit", {}).get("sha"),
        "expected_protected": expected_protected,
        "actual_protected": actual_protected,
        "required_status_check_contexts": required_contexts,
        **workflow_view,
        "verdict": "PASS",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    receipt = check(token)
    text = json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True)
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(text + "\n", encoding="utf-8")
    print(
        "BRANCH_PROTECTION_RECONCILIATION=PASS "
        f"repository={receipt['repository']} branch={receipt['branch']} "
        f"protected={str(receipt['actual_protected']).lower()} "
        f"main_sha={receipt['main_sha']}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BranchProtectionContractError as exc:
        print(f"BRANCH_PROTECTION_RECONCILIATION=FAIL reason={exc}")
        raise SystemExit(1)
