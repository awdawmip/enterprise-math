"""Current rule locators, separate from immutable scientific input references.

This pure projection performs no fetch, policy evaluation, or authorization.
Consumers resolve or reuse the current rule snapshot through the linked entry.
"""
from __future__ import annotations


def current_normative_context() -> dict[str, object]:
    return {
        "schema": "ENTERPRISE_MATH_CURRENT_NORMATIVE_CONTEXT_V1",
        "protocol": "docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context",
        "resolution": "RESOLVE_OR_REUSE_CURRENT_RULE_SNAPSHOT_SEPARATELY_FROM_SCIENTIFIC_INPUTS",
        "project": {
            "repository": "awdawmip/enterprise-math",
            "ref": "main",
            "path": "research_priorities/research_method.json",
            "apply_when": "TASK_DRIVER_OR_FROZEN_FREE_PHASE_B",
        },
        "authorized_account_only": {
            "repository": "awdawmip/chatgpt-global-knowledge",
            "ref": "main",
            "entrypoints": ["00_BOOTSTRAP.md", "OPERATING_MANUAL.md"],
            "rules": [
                "knowledge/preferences/OUTPUT_TEMPORAL_SEMANTICS_POLICY.json#conclusion_contract",
                "knowledge/preferences/MATH_RESEARCH_POLICY.json",
            ],
        },
        "public_contributors": "USE_PUBLIC_PROJECT_RULES_WITHOUT_PRIVATE_REPOSITORY_ACCESS",
        "free_phase_a": "GENERIC_RULES_AND_EXISTING_SUBSTRATE_ONLY; PROJECT_METHOD_ROUTE_DEFERRED",
        "scientific_input_pins": "PRESERVE_EXISTING_TASK_PINS_AND_SOURCE_FIREWALLS",
        "authority_granted": False,
    }
