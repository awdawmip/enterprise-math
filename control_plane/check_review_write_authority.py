#!/usr/bin/env python3
"""Audit review-record write authority without reviewing mathematics.

This checker verifies only the transaction that binds an immutable review record
to exact current result bytes. Driver disposition/theorem/Foundation semantics are
outside scope.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


class ReviewWriteAuthorityError(ValueError):
    pass


def _load(path: str) -> dict[str, Any]:
    value = json.loads((ROOT / path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ReviewWriteAuthorityError(f"{path}: JSON object required")
    return value


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ReviewWriteAuthorityError(message)


def check() -> None:
    authority = _load("control_plane/current_control_authority.json")
    contract = _load("research_review_write_authority.json")
    binding_quarantine = _load("research_result_review_binding_quarantines.json")

    _require(
        contract.get("schema") == "ENTERPRISE_MATH_REVIEW_WRITE_AUTHORITY_V1",
        "review write authority: wrong schema",
    )
    _require(contract.get("status") == "ACTIVE_CANONICAL_CONTROL", "review write contract not active")
    _require(contract.get("classification") == "NO_NEW_MATHEMATICS_CONTROL_PLANE_ONLY", "review write contract must be control-only")

    review_auth = authority.get("review_write_authority")
    _require(isinstance(review_auth, dict), "current control authority missing review_write_authority")
    exact_paths = {
        "contract": "research_review_write_authority.json",
        "result_store": "research_result_records/<task-id>/<result-id>.json",
        "review_store": "research_result_reviews/<result-id>/<review-id>.json",
        "binding_quarantine_registry": "research_result_review_binding_quarantines.json",
        "binding_isolation": "control_plane/research_result_review_binding_fault_isolation.py",
        "binding_checker": "control_plane/check_result_review_binding_fault_isolated.py",
        "nonoperational_review_source_adapter": "control_plane/research_nonoperational_review_source_adapter.py",
        "followup_isolation": "control_plane/research_driver_followup_fault_isolation.py",
    }
    for field, expected in exact_paths.items():
        _require(review_auth.get(field) == expected, f"review_write_authority.{field} drifted")
        if field not in {"result_store", "review_store"}:
            _require((ROOT / expected).is_file(), f"review write surface missing: {expected}")

    for field in (
        "refresh_result_binding_immediately_before_remote_mutation",
        "review_record_result_digest_must_match_mutation_parent_bytes",
        "remote_head_move_requires_abort_or_recompute",
        "binding_mismatch_removes_review_operational_authority",
    ):
        _require(review_auth.get(field) is True, f"review_write_authority.{field} must be true")
    for field in (
        "caller_cached_result_is_write_authority",
        "earlier_read_snapshot_is_write_authority",
        "result_record_may_change_in_same_review_record_transaction",
        "remote_write_force_allowed",
        "binding_mismatch_is_auto_repaired",
        "nonoperational_review_retains_followup_authority",
        "control_plane_may_rewrite_review_disposition",
    ):
        _require(review_auth.get(field) is False, f"review_write_authority.{field} must be false")

    invariants = set(contract.get("core_invariants", []))
    for invariant in (
        "READ_SNAPSHOT_IS_NOT_REVIEW_WRITE_AUTHORITY",
        "REVIEW_RECORD_RESULT_BINDING_MUST_BE_RECOMPUTED_FROM_MUTATION_PARENT_RESULT_BYTES",
        "REVIEW_RECORD_MUTATION_PARENT_MUST_MATCH_THE_REFRESHED_REMOTE_AUTHORITY_HEAD",
        "RESULT_RECORD_SHA256_MUST_NOT_BE_REUSED_FROM_STALE_MEMORY_OR_PREVIOUS_TOOL_OUTPUT",
        "REMOTE_REVIEW_RECORD_WRITE_USES_COMPARE_AND_SWAP_OR_NONFORCE_FAST_FORWARD",
        "CONTROL_PLANE_MAINTENANCE_CANNOT_REWRITE_DISPOSITION_OR_CREATE_REPLACEMENT_DRIVER_REVIEW",
        "NONOPERATIONAL_REVIEW_CANNOT_RETAIN_AUTOMATIC_FOLLOWUP_AUTHORITY",
    ):
        _require(invariant in invariants, f"review write contract missing invariant: {invariant}")

    pre = contract.get("pre_mutation_refresh", {})
    _require(pre.get("required") is True, "review pre-mutation refresh must be mandatory")
    _require(pre.get("refresh_remote_head") is True, "review write must refresh remote head")
    _require(pre.get("refresh_exact_result_record_path") is True, "review write must refresh exact result")
    _require(pre.get("recompute_result_record_sha256_from_refreshed_bytes") is True, "review write must recompute result SHA256")
    _require(pre.get("caller_cached_result_object_is_authority") is False, "cached result may not be authority")
    _require(pre.get("earlier_conversation_read_is_authority") is False, "earlier read may not be authority")

    candidate = contract.get("candidate_commit_gate", {})
    for field in (
        "required_when_constructing_remote_commit",
        "candidate_parent_equals_refreshed_head",
        "candidate_parent_contains_exact_refreshed_result_blob",
        "review_record_result_record_path_matches_parent_tree",
        "review_record_result_record_sha256_matches_parent_tree_bytes",
    ):
        _require(candidate.get(field) is True, f"candidate review gate missing: {field}")
    _require(candidate.get("candidate_may_modify_result_record_in_same_transaction") is False, "review transaction may not modify result record")
    _require(candidate.get("candidate_diff_may_reinterpret_review_disposition") is False, "control transaction may not reinterpret disposition")

    remote = contract.get("remote_write", {})
    _require(remote.get("force_update_allowed") is False, "review record remote force update must be forbidden")
    _require(remote.get("nonforce_fast_forward_allowed") is True, "nonforce review write must be allowed")
    _require(remote.get("contents_api_expected_blob_compare_and_swap_allowed") is True, "CAS review write must be allowed")
    _require(remote.get("if_remote_head_moves_after_refresh") == "ABORT_OR_REBASE_AND_RECOMPUTE_RESULT_BINDING", "head move must recompute binding")
    _require(remote.get("if_result_blob_changes_after_refresh") == "ABORT_AND_RECOMPUTE_REVIEW_BINDING", "result move must recompute binding")

    post = contract.get("post_write_integrity", {})
    _require(post.get("canonical_audit") == "control_plane/check_result_review_binding_fault_isolated.py", "binding audit path drifted")
    _require(post.get("raw_binding_error") == "result record digest drift", "binding error signature drifted")
    _require(post.get("mismatch_effect", "").startswith("PRESERVE_EXACT_REVIEW_BYTES_AS_HISTORY"), "binding mismatch must preserve history but remove authority")
    _require(post.get("derived_followup_effect", "").startswith("REMOVE_EXACT_PACKET"), "binding mismatch must remove derived followup authority")
    _require(post.get("replacement_path", "").startswith("AUTHORIZED_DRIVER_CREATES"), "replacement review must remain Driver-owned")

    boundaries = contract.get("authority_boundaries", {})
    for field in (
        "grants_driver_authority",
        "grants_working_truth",
        "grants_foundation_authority",
        "grants_canonical_promotion",
        "changes_review_disposition",
        "changes_result_content",
    ):
        _require(boundaries.get(field) is False, f"review write contract may not grant/change {field}")

    _require(
        binding_quarantine.get("schema") == "ENTERPRISE_MATH_RESULT_REVIEW_BINDING_QUARANTINE_V1",
        "binding quarantine schema drifted",
    )
    _require(binding_quarantine.get("status") == "ACTIVE", "binding quarantine must be active")

    driver_expect = set(authority.get("role_expectations", {}).get("RESEARCH_DRIVER", []))
    _require(
        "REVIEW_RECORD_WRITE_REFRESHES_REMOTE_HEAD_AND_EXACT_RESULT_BYTES_BEFORE_RECOMPUTING_BINDING" in driver_expect,
        "Driver role expectation missing write-boundary binding refresh",
    )
    control_expect = set(authority.get("role_expectations", {}).get("CONTROL_PLANE_MAINTENANCE", []))
    _require(
        "NO_REVIEW_DISPOSITION_REWRITE_OR_REPLACEMENT_REVIEW_CREATION" in control_expect,
        "Control mode must not create replacement Driver reviews",
    )


def main() -> int:
    try:
        check()
    except (ReviewWriteAuthorityError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    print("PASS: review-record write authority refreshes exact result bytes and fails closed without changing review semantics.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
