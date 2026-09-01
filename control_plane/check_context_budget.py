#!/usr/bin/env python3
"""Enforce bounded repository-static hot-start context without false runtime claims."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "research_context_budget.json"


class ContextBudgetError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ContextBudgetError(message)


def check() -> dict[str, object]:
    policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
    require(
        policy.get("schema") == "ENTERPRISE_MATH_CONTEXT_READ_BUDGET_V1",
        "unexpected context-budget schema",
    )
    require(policy.get("status") == "ACTIVE_CANONICAL", "context budget must be ACTIVE_CANONICAL")

    invariants = policy.get("invariants", {})
    for key in (
        "UNBOUNDED_COLLECTION_READ_FOR_DISCOVERY",
        "RECURSIVE_REPOSITORY_TREE_IN_CONVERSATIONAL_CONTEXT",
        "HIGH_FANOUT_DIRECTORY_ENUMERATION_FOR_DISCOVERY",
        "ISSUE_240_ALL_COMMENTS_IN_CONVERSATIONAL_CONTEXT",
    ):
        require(invariants.get(key) == "FORBIDDEN", f"context invariant drifted: {key}")
    require(
        invariants.get("TRUNCATION_OR_COMPACTION_IS_A_STOP_BOUNDARY") is False,
        "context compaction must not become a stop boundary",
    )

    defaults = policy.get("bounded_defaults", {})
    expected_maxima = {
        "startup_source_reads_soft_max": 3,
        "search_results_max": 20,
        "file_line_range_soft_max": 200,
        "issue_comment_page_size_max": 20,
        "matching_test_files_soft_max": 3,
    }
    for key, maximum in expected_maxima.items():
        value = defaults.get(key)
        require(isinstance(value, int) and 0 < value <= maximum, f"context default exceeds bound: {key}={value!r}")

    guard = policy.get("static_hot_start_guard", {})
    require(
        guard.get("scope_limit") == "REPOSITORY_STATIC_HOT_ROUTER_ONLY",
        "static guard must not claim to measure dynamic/product context",
    )
    require(
        guard.get("checker") == "control_plane/check_context_budget.py",
        "context guard checker path drifted",
    )
    files = guard.get("files")
    require(isinstance(files, list) and files, "static hot-start file list must be nonempty")
    require(len(files) == len(set(files)), "static hot-start file list contains duplicates")

    max_file = guard.get("max_file_bytes")
    max_total = guard.get("max_total_bytes")
    require(isinstance(max_file, int) and 0 < max_file <= 65_536, "max_file_bytes must be a bounded positive integer")
    require(isinstance(max_total, int) and max_file < max_total <= 196_608, "max_total_bytes must be bounded and exceed max_file_bytes")

    measurements: dict[str, int] = {}
    total = 0
    for raw in files:
        require(isinstance(raw, str) and raw and not raw.startswith("/"), f"invalid hot-start path: {raw!r}")
        path = ROOT / raw
        require(path.is_file(), f"missing static hot-start file: {raw}")
        size = len(path.read_bytes())
        require(size <= max_file, f"static hot-start file exceeds {max_file} bytes: {raw}={size}")
        measurements[raw] = size
        total += size

    require(total <= max_total, f"static hot-start aggregate exceeds {max_total} bytes: {total}")

    limitations = guard.get("does_not_measure")
    required_limitations = {
        "DYNAMIC_TASK_LOCAL_DEPENDENCIES",
        "CONNECTED_TOOL_OUTPUTS",
        "GLOBAL_KNOWLEDGE_EXTERNAL_REPOSITORY_INPUTS",
        "PRODUCT_RUNTIME_TOKENIZATION",
    }
    require(isinstance(limitations, list), "static guard must disclose measurement limitations")
    require(set(limitations) == required_limitations, "static guard limitation disclosure drifted")

    return {
        "files": measurements,
        "total_bytes": total,
        "max_file_bytes": max_file,
        "max_total_bytes": max_total,
        "scope": guard.get("scope_limit"),
    }


def main() -> int:
    result = check()
    print(json.dumps({"context_budget": "PASS", **result}, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
