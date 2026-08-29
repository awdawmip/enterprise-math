#!/usr/bin/env python3
"""Verify the semantic-safe control-migration authority contract.

This checker is deliberately control-only.  It validates that
``current_control_authority.json`` routes mixed/large JSON cleanup through the
registered migration, non-executable verification-request, and exact-span safety
surfaces.  It does not interpret theorem, Working Truth, Foundation, discovery,
or task-local mathematical semantics.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
AUTHORITY = "control_plane/current_control_authority.json"


class SemanticMigrationAuthorityError(ValueError):
    pass


def _load(path: str) -> dict[str, Any]:
    value = json.loads((ROOT / path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise SemanticMigrationAuthorityError(f"{path}: JSON object required")
    return value


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise SemanticMigrationAuthorityError(message)


def check() -> None:
    authority = _load(AUTHORITY)
    _require(
        authority.get("status") == "ACTIVE_CANONICAL_CONTROL_PRECEDENCE",
        "current control authority must be active",
    )
    migration = authority.get("semantic_migration")
    _require(isinstance(migration, dict), "semantic_migration authority block missing")

    exact_paths = {
        "registry": "control_plane/control_semantic_migration_registry.json",
        "checker": "control_plane/check_control_semantic_migration_registry.py",
        "verification_requests": "control_plane/control_semantic_verification_requests.json",
        "verification_request_checker": "control_plane/check_control_semantic_verification_requests.py",
        "safe_exact_span_applier": "control_plane/apply_registered_json_migration.py",
        "structural_equivalence_checker": "control_plane/check_runtime_control_migration_equivalence.py",
        "production_consumer_checker": "control_plane/check_control_pointer_python_consumers.py",
    }
    for field, expected in exact_paths.items():
        _require(migration.get(field) == expected, f"semantic_migration.{field} drifted")
        _require((ROOT / expected).is_file(), f"semantic migration surface missing: {expected}")

    _require(
        migration.get("mode") == "GRADUAL_TYPED_FIELD_MIGRATION",
        "semantic migration must remain gradual typed field migration",
    )
    _require(
        migration.get("baseline_blob_drift_is_automatic_failure") is False,
        "unrelated source evolution must not automatically fail migration debt",
    )
    _require(
        migration.get("registered_field_third_state_is_failure") is True,
        "registered control fields must fail closed on third-state drift",
    )
    _require(
        migration.get("mixed_semantics_requires_verification_before_edit") is True,
        "mixed semantic files must require verification before edit",
    )
    _require(
        migration.get("migration_registry_overrides_mathematical_semantics") is False,
        "migration registry may not override mathematical semantics",
    )

    for field in (
        "verification_request_is_task",
        "verification_request_is_claimable",
        "verification_request_grants_authority",
    ):
        _require(migration.get(field) is False, f"semantic_migration.{field} must be false")
    _require(
        migration.get("future_real_verification_task_requires_immutable_v2_publication_by_authorized_role")
        is True,
        "future real verification tasks must require authorized immutable V2 publication",
    )

    _require(
        migration.get("large_or_mixed_json_whole_file_reserialization_for_pointer_cleanup")
        == "FORBIDDEN_BY_DEFAULT",
        "large/mixed JSON pointer cleanup must forbid whole-file reserialization by default",
    )
    for field in (
        "exact_expected_git_blob_required_before_pending_patch",
        "dry_run_required_before_write",
        "non_target_json_structure_must_remain_equal",
        "non_target_text_segments_must_remain_byte_identical",
        "protected_selector_must_remain_exact",
        "write_mode_may_change_only_registered_approved_pointers",
    ):
        _require(migration.get(field) is True, f"semantic_migration.{field} must be true")

    precedence = authority.get("precedence")
    _require(isinstance(precedence, dict), "precedence block missing")
    _require(
        precedence.get("mixed_semantic_file_edit_rule")
        == "CONSULT_CONTROL_SEMANTIC_MIGRATION_REGISTRY_AND_VERIFY_BEFORE_EDIT",
        "mixed semantic edit precedence drifted",
    )
    _require(
        precedence.get("uncertain_semantics_rule")
        == "CAPTURE_NONEXECUTABLE_VERIFICATION_REQUEST_OR_ROUTE_TO_AUTHORIZED_GOVERNANCE_ROLE; DO_NOT_SELF_PUBLISH_FROM_CONTROL_MODE",
        "uncertain semantic routing drifted",
    )
    _require(
        precedence.get("large_json_pointer_cleanup_rule")
        == "USE_EXACT_SPAN_REGISTERED_MIGRATION; DO_NOT_WHOLE_FILE_RESERIALIZE_BY_DEFAULT",
        "large JSON pointer cleanup precedence drifted",
    )


def main() -> int:
    try:
        check()
    except (SemanticMigrationAuthorityError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    print("PASS: semantic migration authority is non-mathematical, non-executive, and exact-span fail-closed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
