#!/usr/bin/env python3
"""Audit open and closed non-executable semantic verification requests.

A CONTROL_PLANE_MAINTENANCE conversation may preserve an unresolved semantic
question, but it may not turn that request into a scheduler task or grant itself
Researcher/Driver/Steward authority. Open requests must bind to an open migration
item and any future real task must use immutable V2 publication under an
authorized role.

When the registered current values already equal the canonical values and no
field mutation remains, the request is retained as closed provenance. Closing a
no-change request grants neither governance approval nor migration authority and
must not manufacture a synthetic task.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REQUESTS_PATH = ROOT / "control_plane" / "control_semantic_verification_requests.json"
MIGRATION_PATH = ROOT / "control_plane" / "control_semantic_migration_registry.json"
SCHEMA = "ENTERPRISE_MATH_CONTROL_SEMANTIC_VERIFICATION_REQUESTS_V1"
OPEN_REQUEST_STATUS = "ACTIVE_NONEXECUTABLE"
CLOSED_REQUEST_STATUS = "CLOSED_NONEXECUTABLE_HISTORY"
OPEN_REQUEST_STATE = "AWAITING_AUTHORIZED_GOVERNANCE_TASK_PUBLICATION_OR_DIRECT_STEWARD_VERIFICATION"
CLOSED_REQUEST_STATE = "RESOLVED_NO_TASK_REQUIRED_CURRENT_VALUES_ALREADY_CANONICAL"
OPEN_VERIFICATION_STATES = {"REQUIRES_GOVERNANCE_VERIFICATION"}
NO_CHANGE_TERMINAL_STATES = {"VERIFIED_NO_POINTER_CHANGE_REQUIRED"}
ALLOWED_FUTURE_PUBLISHERS = {"RESEARCH_DRIVER", "FOUNDATION_STEWARD"}
ARCHITECTURE_EVIDENCE_CHECKER = "control_plane/check_architecture_publication_cutover_evidence.py"
ARCHITECTURE_OPEN_EVIDENCE_STATUS = "CONTROL_STRUCTURAL_EVIDENCE_ONLY_NOT_GOVERNANCE_APPROVAL"
ARCHITECTURE_CLOSED_EVIDENCE_STATUS = "CURRENT_ARCHITECTURE_V2_POINTERS_VERIFIED_NO_CHANGE_REQUIRED"


class VerificationRequestError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise VerificationRequestError(f"{path.relative_to(ROOT)}: JSON object required")
    return value


def _migration_pointer_count(migration: dict[str, Any]) -> int:
    if "json_pointer" in migration:
        return 1
    pointers = migration.get("json_pointers")
    if not isinstance(pointers, list) or not pointers:
        raise VerificationRequestError(
            f"{migration.get('migration_id')}: migration has no registered pointer set"
        )
    return len(pointers)


def _require_string_list(value: Any, label: str) -> list[str]:
    if not isinstance(value, list) or not value or any(
        not isinstance(item, str) or not item.strip() for item in value
    ):
        raise VerificationRequestError(f"{label} must be nonempty strings")
    return value


def _check_historical_structural_evidence(
    request_id: str,
    evidence: Any,
    migration: dict[str, Any],
    root: Path,
) -> None:
    if not isinstance(evidence, dict):
        raise VerificationRequestError(
            f"{request_id}: historical_control_structural_evidence must be an object"
        )
    if evidence.get("checker") != ARCHITECTURE_EVIDENCE_CHECKER:
        raise VerificationRequestError(f"{request_id}: structural evidence checker drifted")
    if not (root / ARCHITECTURE_EVIDENCE_CHECKER).is_file():
        raise VerificationRequestError(f"{request_id}: structural evidence checker missing")
    if evidence.get("prior_status") != ARCHITECTURE_OPEN_EVIDENCE_STATUS:
        raise VerificationRequestError(f"{request_id}: historical evidence status drifted")
    if evidence.get("source_architecture_blob_sha1") != migration.get("baseline_blob_sha1"):
        raise VerificationRequestError(
            f"{request_id}: historical evidence source blob does not match migration baseline"
        )
    if evidence.get("exact_registered_pointer_count") != _migration_pointer_count(migration):
        raise VerificationRequestError(
            f"{request_id}: historical evidence pointer count does not match migration registry"
        )
    if evidence.get("non_target_json_structure_equal") is not True:
        raise VerificationRequestError(
            f"{request_id}: historical evidence must preserve non-target JSON"
        )
    if evidence.get("semantic_sentinel_digests_pinned") is not True:
        raise VerificationRequestError(
            f"{request_id}: historical semantic sentinel digests must be pinned"
        )
    sentinels = evidence.get("sentinel_families")
    if not isinstance(sentinels, list) or len(sentinels) < 8 or any(
        not isinstance(item, str) or not item.strip() for item in sentinels
    ):
        raise VerificationRequestError(
            f"{request_id}: historical evidence sentinel families incomplete"
        )
    if evidence.get("governance_approval_granted") is not False:
        raise VerificationRequestError(
            f"{request_id}: historical control evidence may not grant governance approval"
        )
    if evidence.get("migration_authority_granted") is not False:
        raise VerificationRequestError(
            f"{request_id}: historical control evidence may not grant migration authority"
        )


def _check_open_structural_evidence(
    request_id: str,
    row: dict[str, Any],
    related_migrations: list[dict[str, Any]],
    root: Path,
) -> str | None:
    evidence = row.get("control_structural_evidence")
    if evidence is None:
        return None
    if not isinstance(evidence, dict):
        raise VerificationRequestError(
            f"{request_id}: control_structural_evidence must be an object"
        )
    if len(related_migrations) != 1:
        raise VerificationRequestError(
            f"{request_id}: attached structural evidence currently requires exactly one migration"
        )
    migration = related_migrations[0]
    checker = evidence.get("checker")
    if checker != ARCHITECTURE_EVIDENCE_CHECKER:
        raise VerificationRequestError(f"{request_id}: structural evidence checker drifted")
    if not (root / ARCHITECTURE_EVIDENCE_CHECKER).is_file():
        raise VerificationRequestError(f"{request_id}: structural evidence checker missing")
    if evidence.get("status") != ARCHITECTURE_OPEN_EVIDENCE_STATUS:
        raise VerificationRequestError(f"{request_id}: structural evidence status drifted")
    if evidence.get("source_architecture_blob_sha1") != migration.get("baseline_blob_sha1"):
        raise VerificationRequestError(
            f"{request_id}: structural evidence source blob does not match migration baseline"
        )
    if evidence.get("exact_registered_pointer_count") != _migration_pointer_count(migration):
        raise VerificationRequestError(
            f"{request_id}: structural evidence pointer count does not match migration registry"
        )
    if evidence.get("non_target_json_structure_equal") is not True:
        raise VerificationRequestError(
            f"{request_id}: structural evidence must preserve non-target JSON"
        )
    if evidence.get("semantic_sentinel_digests_pinned") is not True:
        raise VerificationRequestError(
            f"{request_id}: semantic sentinel digests must be pinned"
        )
    sentinels = evidence.get("sentinel_families")
    if not isinstance(sentinels, list) or len(sentinels) < 8 or any(
        not isinstance(item, str) or not item.strip() for item in sentinels
    ):
        raise VerificationRequestError(
            f"{request_id}: structural evidence sentinel families incomplete"
        )
    if evidence.get("governance_approval_granted") is not False:
        raise VerificationRequestError(
            f"{request_id}: control structural evidence may not grant governance approval"
        )
    if evidence.get("migration_authority_granted") is not False:
        raise VerificationRequestError(
            f"{request_id}: control structural evidence may not grant migration authority"
        )
    return ARCHITECTURE_OPEN_EVIDENCE_STATUS


def _check_future_publication(request_id: str, publication: Any) -> set[str]:
    if not isinstance(publication, dict):
        raise VerificationRequestError(
            f"{request_id}: future_authorized_publication is required for open request"
        )
    if publication.get("kind") != "GOVERNANCE":
        raise VerificationRequestError(f"{request_id}: any future task must be GOVERNANCE")
    publishers = publication.get("publisher_role_must_be_one_of")
    if not isinstance(publishers, list) or not publishers:
        raise VerificationRequestError(f"{request_id}: future publisher roles are required")
    publisher_set = set(publishers)
    if not publisher_set <= ALLOWED_FUTURE_PUBLISHERS:
        raise VerificationRequestError(
            f"{request_id}: unsupported future publisher role(s): "
            f"{sorted(publisher_set - ALLOWED_FUTURE_PUBLISHERS)}"
        )
    if publication.get("publication_contract") != "research_task_publication_contract_v2.json":
        raise VerificationRequestError(
            f"{request_id}: future task must use V2 publication contract"
        )
    if publication.get("publication_tool") != "tools/research_task_records.py":
        raise VerificationRequestError(
            f"{request_id}: future task must use immutable V2 publication tool"
        )
    return publisher_set


def _check_closed_request(
    request_id: str,
    row: dict[str, Any],
    related_rows: list[dict[str, Any]],
    migration_states: dict[str, str],
    root: Path,
) -> str:
    if any(state not in NO_CHANGE_TERMINAL_STATES for state in migration_states.values()):
        raise VerificationRequestError(
            f"{request_id}: closed no-change request references nonterminal migration(s) "
            f"{migration_states}"
        )
    if row.get("future_authorized_publication") is not None:
        raise VerificationRequestError(
            f"{request_id}: closed no-change request cannot retain a future task publication"
        )
    if len(related_rows) != 1:
        raise VerificationRequestError(
            f"{request_id}: closed Architecture no-change request requires exactly one migration"
        )
    migration = related_rows[0]
    resolution = row.get("resolution")
    if not isinstance(resolution, dict):
        raise VerificationRequestError(f"{request_id}: resolution object is required")
    if resolution.get("migration_state") != migration.get("state"):
        raise VerificationRequestError(f"{request_id}: resolution migration state drifted")
    if resolution.get("checker") != ARCHITECTURE_EVIDENCE_CHECKER:
        raise VerificationRequestError(f"{request_id}: resolution checker drifted")
    if resolution.get("evidence_status") != ARCHITECTURE_CLOSED_EVIDENCE_STATUS:
        raise VerificationRequestError(f"{request_id}: resolution evidence status drifted")
    pointer_count = _migration_pointer_count(migration)
    if resolution.get("registered_pointer_count") != pointer_count:
        raise VerificationRequestError(f"{request_id}: resolved pointer count drifted")
    if resolution.get("changed_pointer_count") != 0:
        raise VerificationRequestError(
            f"{request_id}: closed no-change request must have zero changed pointers"
        )
    for field in (
        "all_current_values_equal_canonical_targets",
        "non_target_json_structure_equal",
        "semantic_sentinel_digests_unchanged",
    ):
        if resolution.get(field) is not True:
            raise VerificationRequestError(f"{request_id}: resolution must prove {field}")
    if resolution.get("task_publication_required") is not False:
        raise VerificationRequestError(
            f"{request_id}: no-change resolution cannot require a task publication"
        )
    if resolution.get("governance_approval_granted") is not False:
        raise VerificationRequestError(
            f"{request_id}: no-change resolution may not grant governance approval"
        )
    if resolution.get("migration_authority_granted") is not False:
        raise VerificationRequestError(
            f"{request_id}: no-change resolution may not grant migration authority"
        )
    reason = resolution.get("reason")
    if not isinstance(reason, str) or not reason.strip():
        raise VerificationRequestError(f"{request_id}: resolution reason is required")
    _check_historical_structural_evidence(
        request_id,
        row.get("historical_control_structural_evidence"),
        migration,
        root,
    )
    _require_string_list(
        row.get("required_verification_completed"),
        f"{request_id}: required_verification_completed",
    )
    return (
        f"{request_id}: CLOSED_NONEXECUTABLE_NO_TASK_REQUIRED / "
        f"migrations={migration_states} / changed_pointers=0"
    )


def check(root: Path = ROOT) -> list[str]:
    requests = _load(root / "control_plane" / "control_semantic_verification_requests.json")
    migrations = _load(root / "control_plane" / "control_semantic_migration_registry.json")
    status = requests.get("status")
    if requests.get("schema") != SCHEMA or status not in {
        OPEN_REQUEST_STATUS,
        CLOSED_REQUEST_STATUS,
    }:
        raise VerificationRequestError("verification request schema/status invalid")
    if requests.get("migration_registry") != "control_plane/control_semantic_migration_registry.json":
        raise VerificationRequestError(
            "verification request migration registry pointer drifted"
        )

    migration_map = {
        row.get("migration_id"): row
        for row in migrations.get("entries", [])
        if isinstance(row, dict) and isinstance(row.get("migration_id"), str)
    }
    rows = requests.get("requests")
    if not isinstance(rows, list) or not rows:
        raise VerificationRequestError("verification request list is empty")

    seen: set[str] = set()
    reports: list[str] = []
    has_open = False
    for row in rows:
        if not isinstance(row, dict):
            raise VerificationRequestError("verification request must be an object")
        request_id = row.get("request_id")
        if not isinstance(request_id, str) or not request_id or request_id in seen:
            raise VerificationRequestError(f"invalid/duplicate request_id: {request_id!r}")
        seen.add(request_id)
        for field in ("is_research_task", "claimable", "runtime_dispatchable", "authority_granted"):
            if row.get(field) is not False:
                raise VerificationRequestError(
                    f"{request_id}: non-executable request must keep {field}=false"
                )

        related = _require_string_list(
            row.get("related_migration_ids"),
            f"{request_id}: related_migration_ids",
        )
        migration_states: dict[str, str] = {}
        related_rows: list[dict[str, Any]] = []
        for migration_id in related:
            migration = migration_map.get(migration_id)
            if not isinstance(migration, dict):
                raise VerificationRequestError(
                    f"{request_id}: unknown migration_id {migration_id}"
                )
            related_rows.append(migration)
            migration_states[migration_id] = str(migration.get("state") or "")

        question = row.get("question")
        if not isinstance(question, str) or not question.strip():
            raise VerificationRequestError(
                f"{request_id}: verification question is required"
            )
        state = row.get("state")
        if state == OPEN_REQUEST_STATE:
            has_open = True
            if any(
                migration_state not in OPEN_VERIFICATION_STATES
                for migration_state in migration_states.values()
            ):
                raise VerificationRequestError(
                    f"{request_id}: open request references non-open migration(s) "
                    f"{migration_states}"
                )
            _require_string_list(
                row.get("required_verification"),
                f"{request_id}: required_verification",
            )
            evidence_status = _check_open_structural_evidence(
                request_id, row, related_rows, root
            )
            publisher_set = _check_future_publication(
                request_id, row.get("future_authorized_publication")
            )
            evidence_note = (
                f" / evidence={evidence_status}" if evidence_status else ""
            )
            reports.append(
                f"{request_id}: OPEN_NONEXECUTABLE / migrations={migration_states} / "
                f"future_publishers={sorted(publisher_set)}{evidence_note}"
            )
        elif state == CLOSED_REQUEST_STATE:
            reports.append(
                _check_closed_request(
                    request_id, row, related_rows, migration_states, root
                )
            )
        else:
            raise VerificationRequestError(
                f"{request_id}: unsupported request state {state!r}"
            )

    expected_status = OPEN_REQUEST_STATUS if has_open else CLOSED_REQUEST_STATUS
    if status != expected_status:
        raise VerificationRequestError(
            f"verification request container status must be {expected_status}"
        )
    return reports


def main() -> int:
    try:
        reports = check()
    except (VerificationRequestError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    print(
        "PASS: semantic verification requests are non-executable; open requests bind "
        "to real open debt, and closed no-change requests remain provenance only."
    )
    for row in reports:
        print(" -", row)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
