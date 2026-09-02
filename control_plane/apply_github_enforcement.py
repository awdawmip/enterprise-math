#!/usr/bin/env python3
"""Idempotently apply and verify the canonical GitHub main protection contract.

Semantic mode: IDEMPOTENT_APPLY_THEN_VERIFY.
This tool changes repository integration policy only. It does not grant
mathematical, task, Driver, Working Truth, Foundation, or publication authority.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "control_plane" / "github_enforcement_contract.json"
API = "https://api.github.com"


class GithubEnforcementError(RuntimeError):
    pass


def load_contract() -> dict[str, Any]:
    value = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    if value.get("schema") != "ENTERPRISE_MATH_GITHUB_ENFORCEMENT_CONTRACT_V1":
        raise GithubEnforcementError("unexpected enforcement contract schema")
    if value.get("status") != "ACTIVE_CANONICAL":
        raise GithubEnforcementError("enforcement contract is not active")
    return value


def protection_payload(contract: dict[str, Any]) -> dict[str, Any]:
    policy = contract["branch_protection"]
    return {
        "required_status_checks": {
            "strict": bool(policy["strict_status_checks"]),
            "contexts": [],
            "checks": [
                {
                    "context": context,
                    "app_id": int(contract["status_check_app"]["app_id"]),
                }
                for context in contract["required_status_checks"]
            ],
        },
        "enforce_admins": bool(policy["enforce_admins"]),
        "required_pull_request_reviews": {
            "dismiss_stale_reviews": False,
            "require_code_owner_reviews": False,
            "required_approving_review_count": int(
                policy["required_approving_review_count"]
            ),
            "require_last_push_approval": False,
        }
        if policy["require_pull_request"]
        else None,
        "restrictions": None,
        "required_linear_history": bool(policy["required_linear_history"]),
        "allow_force_pushes": bool(policy["allow_force_pushes"]),
        "allow_deletions": bool(policy["allow_deletions"]),
        "block_creations": False,
        "required_conversation_resolution": bool(
            policy["required_conversation_resolution"]
        ),
        "lock_branch": False,
        "allow_fork_syncing": False,
    }


class GithubApi:
    def __init__(self, token: str):
        if not token:
            raise GithubEnforcementError("GitHub administration token is required")
        self.headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "enterprise-math-github-enforcement",
        }

    def request(
        self,
        method: str,
        path: str,
        payload: dict[str, Any] | None = None,
    ) -> Any:
        body = None
        headers = dict(self.headers)
        if payload is not None:
            body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
            headers["Content-Type"] = "application/json"
        request = urllib.request.Request(
            f"{API}{path}",
            data=body,
            headers=headers,
            method=method,
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                raw = response.read()
                return json.loads(raw.decode("utf-8")) if raw else None
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise GithubEnforcementError(
                f"GitHub API {method} {path} failed status={exc.code}: {detail}"
            ) from exc
        except urllib.error.URLError as exc:
            raise GithubEnforcementError(
                f"GitHub API {method} {path} transport failed: {exc}"
            ) from exc


def enabled(value: Any) -> bool:
    if isinstance(value, dict):
        return value.get("enabled") is True
    return value is True


def observed_status_checks(
    protection: dict[str, Any],
) -> tuple[list[str], list[tuple[str, int | None]]]:
    status = protection.get("required_status_checks") or {}
    contexts: set[str] = set()
    pinned: set[tuple[str, int | None]] = set()
    for item in status.get("contexts") or []:
        if isinstance(item, str) and item:
            contexts.add(item)
    for item in status.get("checks") or []:
        if not isinstance(item, dict):
            continue
        context = item.get("context")
        app_id = item.get("app_id")
        if isinstance(context, str) and context:
            contexts.add(context)
            pinned.add(
                (
                    context,
                    int(app_id) if isinstance(app_id, int) else None,
                )
            )
    return sorted(contexts), sorted(
        pinned,
        key=lambda item: (item[0], -1 if item[1] is None else item[1]),
    )


def verify_state(
    contract: dict[str, Any],
    branch: dict[str, Any],
    protection: dict[str, Any],
    rulesets: Any,
) -> dict[str, Any]:
    policy = contract["branch_protection"]
    expected_checks = sorted(contract["required_status_checks"])
    observed_checks, observed_pinned = observed_status_checks(protection)
    expected_app_id = int(contract["status_check_app"]["app_id"])
    expected_pinned = sorted(
        (context, expected_app_id)
        for context in contract["required_status_checks"]
    )
    pull_request = protection.get("required_pull_request_reviews")
    status = protection.get("required_status_checks") or {}

    assertions = {
        "main_protected": branch.get("protected") is True,
        "required_checks_exact": observed_checks == expected_checks,
        "required_checks_app_pinned": observed_pinned == expected_pinned,
        "strict_status_checks": status.get("strict") is bool(
            policy["strict_status_checks"]
        ),
        "pull_request_required": (pull_request is not None)
        is bool(policy["require_pull_request"]),
        "approval_count_exact": (
            int((pull_request or {}).get("required_approving_review_count", -1))
            == int(policy["required_approving_review_count"])
        )
        if policy["require_pull_request"]
        else True,
        "enforce_admins_exact": enabled(protection.get("enforce_admins"))
        is bool(policy["enforce_admins"]),
        "force_pushes_exact": enabled(protection.get("allow_force_pushes"))
        is bool(policy["allow_force_pushes"]),
        "deletions_exact": enabled(protection.get("allow_deletions"))
        is bool(policy["allow_deletions"]),
        "conversation_resolution_exact": enabled(
            protection.get("required_conversation_resolution")
        )
        is bool(policy["required_conversation_resolution"]),
        "linear_history_exact": enabled(protection.get("required_linear_history"))
        is bool(policy["required_linear_history"]),
    }
    return {
        "schema": "ENTERPRISE_MATH_GITHUB_ENFORCEMENT_REPORT_V1",
        "repository": contract["repository"],
        "branch": contract["branch"],
        "verified": all(assertions.values()),
        "assertions": assertions,
        "expected_checks": expected_checks,
        "observed_checks": observed_checks,
        "expected_app_id": expected_app_id,
        "observed_pinned_checks": [
            {"context": context, "app_id": app_id}
            for context, app_id in observed_pinned
        ],
        "ruleset_count": len(rulesets) if isinstance(rulesets, list) else None,
        "required_checks_are_conversation_lease": False,
        "admin_emergency_bypass": policy["enforce_admins"] is False,
    }


def read_state(api: GithubApi, contract: dict[str, Any]) -> tuple[Any, Any, Any]:
    repository = contract["repository"]
    branch_name = contract["branch"]
    branch = api.request("GET", f"/repos/{repository}/branches/{branch_name}")
    protection = api.request(
        "GET", f"/repos/{repository}/branches/{branch_name}/protection"
    )
    rulesets = api.request("GET", f"/repos/{repository}/rulesets")
    return branch, protection, rulesets


def write_report(path: Path | None, report: dict[str, Any]) -> None:
    text = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if path is not None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    print(text, end="")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Apply and verify the Enterprise Math GitHub protection contract"
    )
    parser.add_argument("--verify-only", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    contract = load_contract()
    payload = protection_payload(contract)
    if args.dry_run:
        write_report(
            args.report,
            {
                "schema": "ENTERPRISE_MATH_GITHUB_ENFORCEMENT_DRY_RUN_V1",
                "repository": contract["repository"],
                "branch": contract["branch"],
                "payload": payload,
            },
        )
        return 0

    token = os.environ.get("GITHUB_ENFORCEMENT_TOKEN", "").strip()
    api = GithubApi(token)
    repository = contract["repository"]
    branch_name = contract["branch"]

    if not args.verify_only:
        api.request(
            "PUT",
            f"/repos/{repository}/branches/{branch_name}/protection",
            payload,
        )

    branch, protection, rulesets = read_state(api, contract)
    report = verify_state(contract, branch, protection, rulesets)
    report["mode"] = "VERIFY_ONLY" if args.verify_only else "IDEMPOTENT_APPLY_THEN_VERIFY"
    write_report(args.report, report)
    return 0 if report["verified"] else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except GithubEnforcementError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
