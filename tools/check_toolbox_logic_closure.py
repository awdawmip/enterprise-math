#!/usr/bin/env python3
"""Audit the complete Enterprise Math Toolbox invocation loop.

The checker verifies that a Driver-accepted tool is not merely documented. It
must be routable through registry/inventory, visible under the current role
policy, and executable when declared production-callable.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import tools.enterprise_toolbox as toolbox  # noqa: E402

REGISTRY = ROOT / "enterprise_toolbox_registry.json"
POLICY = ROOT / "tool_invocation_policy.json"
CONTRACT = ROOT / "research_taskbook_contract.json"
PROTOCOL = ROOT / "docs" / "ENTERPRISE_TOOL_INVOCATION_PROTOCOL.md"
TOOLBOX_DOC = ROOT / "docs" / "ENTERPRISE_TOOLBOX_REGISTRY.md"
TASKBOOK_TOOL = ROOT / "tools" / "research_taskbook.py"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def existing_path(path: str) -> bool:
    return (ROOT / path).exists()


def check() -> None:
    registry = load(REGISTRY)
    policy = load(POLICY)
    contract = load(CONTRACT)
    protocol_text = PROTOCOL.read_text(encoding="utf-8")
    toolbox_text = TOOLBOX_DOC.read_text(encoding="utf-8")
    taskbook_tool_text = TASKBOOK_TOOL.read_text(encoding="utf-8")

    require(
        registry.get("schema") == "ENTERPRISE_MATH_TOOLBOX_REGISTRY_V2",
        "unexpected toolbox registry schema",
    )
    require(
        policy.get("schema") == "ENTERPRISE_MATH_TOOL_INVOCATION_POLICY_V2",
        "tool invocation policy must be V2",
    )
    require(
        contract.get("schema") == "ENTERPRISE_MATH_RESEARCH_TASKBOOK_CONTRACT_V7",
        "taskbook contract must be V7",
    )

    require(policy.get("registry") == REGISTRY.name, "policy registry pointer drift")
    require(
        policy.get("method_inventory_base") == "research_method_inventory.json",
        "policy base method-inventory pointer drift",
    )
    require(
        policy.get("method_inventory_addenda")
        == "research_method_inventory_addenda/*.json",
        "policy addendum pointer drift",
    )
    require(
        policy.get("executable_router") == "tools/enterprise_toolbox.py",
        "policy router pointer drift",
    )
    require(
        registry.get("method_inventory") == policy.get("method_inventory_base"),
        "registry/policy base inventory mismatch",
    )
    require(
        registry.get("method_inventory_addenda")
        == [policy.get("method_inventory_addenda")],
        "registry/policy addendum mismatch",
    )

    tools = registry.get("tools", [])
    ids = [tool.get("id") for tool in tools]
    require(len(ids) == len(set(ids)), "duplicate toolbox family id")
    for index in range(13):
        matches = [
            tool_id
            for tool_id in ids
            if str(tool_id).startswith(f"T{index}_")
        ]
        require(
            len(matches) == 1,
            f"expected exactly one T{index} family, got {matches}",
        )

    callability = registry.get("callability_gate", {})
    production_ids = callability.get("production_callable_tool_ids", [])
    interface_only_ids = callability.get("interface_only_tool_ids", [])
    require(
        not set(production_ids) & set(interface_only_ids),
        "tool cannot be both production-callable and interface-only",
    )
    require(
        {
            "T10_LOCAL_REDISTRIBUTION_TOPPLING",
            "T11_DISCRETE_MORSE_CHAIN_REDUCTION",
            "T12_IDEMPOTENT_PATH_CLOSURE_BELLMAN",
        }
        <= set(production_ids),
        "T10-T12 must all be production-callable after closure integration",
    )

    by_id = {tool["id"]: tool for tool in tools}
    for tool_id in production_ids:
        tool = by_id.get(tool_id)
        require(tool is not None, f"unknown production-callable tool {tool_id}")
        source_modules = [
            path
            for path in tool.get("source_methods", [])
            if isinstance(path, str)
            and path.startswith("src/enterprise_math/")
            and path.endswith(".py")
        ]
        require(source_modules, f"{tool_id} has no production source module")
        for path in source_modules:
            require(existing_path(path), f"{tool_id} source module missing: {path}")

    path_prefixes = (
        "src/",
        "driver_reviews/",
        "research_notes/",
        "research_tasks/",
        "scripts/",
        "tools/",
        "docs/",
        "definitions/",
    )
    for tool in tools:
        for key in ("source_methods", "known_specializations"):
            for path in tool.get(key, []):
                if isinstance(path, str) and path.startswith(path_prefixes):
                    require(existing_path(path), f"registered path missing: {path}")
        for key in ("driver_review", "result"):
            path = tool.get(key)
            if path:
                require(existing_path(path), f"registered path missing: {path}")

    for facade in registry.get("domain_facades", []):
        for path in facade.get("sources", []):
            require(existing_path(path), f"domain facade source missing: {path}")

    inventory = toolbox.load_method_inventory()
    require(
        "research_method_inventory_addenda/20260823_tool_discovery_six_return.json"
        in inventory.get("loaded_addenda", []),
        "six-return method addendum is not loaded",
    )
    method_ids = [method.get("method_id") for method in inventory.get("methods", [])]
    require(
        len(method_ids) == len(set(method_ids)),
        "duplicate method_id across base/addenda",
    )
    t12_method = next(
        method
        for method in inventory["methods"]
        if method.get("method_id") == "tool.idempotent_path_closure_bellman"
    )
    require(
        "src/enterprise_math/idempotent_path_closure.py"
        in t12_method.get("source_refs", []),
        "T12 method record does not expose production module",
    )

    required_meta = contract.get("new_dispatchable_taskbook_required_metadata", {})
    require(
        required_meta.get("tool_invocation_policy") == "INHERIT_GLOBAL",
        "taskbook-only dispatch lacks tool invocation inheritance",
    )
    require(
        '"tool_invocation_policy": "INHERIT_GLOBAL"' in taskbook_tool_text,
        "taskbook generator/reviewer does not expose tool invocation inheritance",
    )

    for marker in (
        "research_method_inventory_addenda/*.json",
        "TASKBOOK-ONLY LAST MILE",
        "ACCEPTED TOOL -> ROUTABLE -> CALLABLE",
    ):
        require(marker in protocol_text, f"invocation protocol missing marker: {marker}")

    for marker in (
        "T10",
        "T11",
        "T12",
        "src/enterprise_math/idempotent_path_closure.py",
        "tools/check_toolbox_logic_closure.py",
    ):
        require(marker in toolbox_text, f"toolbox human registry missing marker: {marker}")

    module_hits = toolbox.module_suggestions(
        "min-plus max-plus Kleene Bellman path closure"
    )
    require(
        any(
            item.get("source_ref")
            == "src/enterprise_math/idempotent_path_closure.py"
            for item in module_hits
        ),
        "executable router cannot rediscover the T12 production module",
    )

    print(
        "toolbox logic closure: OK "
        f"({len(tools)} families, {len(inventory['methods'])} methods, "
        f"{len(production_ids)} production-callable newly gated families)"
    )


def main() -> int:
    try:
        check()
    except (AssertionError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"toolbox logic closure: FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
