#!/usr/bin/env python3
"""Audit non-executable semantic verification requests.

A CONTROL_PLANE_MAINTENANCE conversation may preserve an unresolved semantic
question, but it may not turn that request into a scheduler task or grant itself
Researcher/Driver/Steward authority. This checker binds each request to an open
migration-registry item and requires any future real task to use the immutable
V2 publication path under an authorized publisher role.

Optional control-only structural evidence is also validated here. Such evidence
may prove field locality and pin unchanged semantic blocks, but it must never
masquerade as governance approval or migration authority.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REQUESTS_PATH = ROOT / "control_plane" / "control_semantic_verification_requests.json"
MIGRATION_PATH = ROOT / "control_plane" / "control_semantic_migration_registry.json"
SCHEMA = "ENTERPRISE_MATH_CONTROL_SEMANTIC_VERIFICATION_REQUESTS_V1"
OPEN_VERIFICATION_STATES = {
    "REQUIRES_GOVERNANCE_VERIFICATION",
}
ALLOWED_FUTURE_PUBLISHERS = {"RESEARCH_DRIVER", "FOUNDATION_STEWARD"}
ARCHITECTURE_EVIDENCE_CHECKER = "control_plane/check_architecture_publication_cutover_evidence.py"
ARCHITECTURE_EVIDENCE_STATUS = "CONTROL_STRUCTURAL_EVIDENCE_ONLY_NOT_GOVERNANCE_APPROVAL"


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


def _check_structural_evidence(
    request_id: str,
    row: dict[str, Any],
    related_migrations: list[dict[str, Any]],
    root: Path,
) -> str | None:
    evidence = row.get("control_structural_evidence")
    if evidence is None:
        return None
    if not isinstance(evidence, dict):
        raise VerificationRequestError(f"{request_id}: control_structural_evidence must be an object")
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
    if evidence.get("status") != ARCHITECTURE_EVIDENCE_STATUS:
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
        raise VerificationRequestError(f"{request_id}: structural evidence must preserve non-target JSON")
    if evidence.get("semantic_sentinel_digests_pinned") is not True:
        raise VerificationRequestError(f"{request_id}: semantic sentinel digests must be pinned")
    sentinels = evidence.get("sentinel_families")
    if not isinstance(sentinels, list) or len(sentinels) < 8 or any(
        not isinstance(item, str) or not item.strip() for item in sentinels
    ):
        raise VerificationRequestError(f"{request_id}: structural evidence sentinel families incomplete")
    if evidence.get("governance_approval_granted") is not False:
        raise VerificationRequestError(
            f"{request_id}: control structural evidence may not grant governance approval"
        )
    if evidence.get("migration_authority_granted") is not False:
        raise VerificationRequestError(
            f"{request_id}: control structural evidence may not grant migration authority"
        )
    return ARCHITECTURE_EVIDENCE_STATUS


def check(root: Path = ROOT) -> list[str]:
    requests = _load(root / "control_plane" / "control_semantic_verification_requests.json")
    migrations = _load(root / "control_plane" / "control_semantic_migration_registry.json")
    if requests.get("schema") != SCHEMA or requests.get("status") != "ACTIVE_NONEXECUTABLE":
        raise VerificationRequestError("verification request schema/status invalid")
    if requests.get("migration_registry") != "control_plane/control_semantic_migration_registry.json":
        raise VerificationRequestError("verification request migration registry pointer drifted")

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
    for row in rows:
        if not isinstance(row, dict):
            raise VerificationRequestError("verification request must be an object")
        request_id = row.get("request_id")
        if not isinstance(request_id, str) or not request_id or request_id in seen:
            raise VerificationRequestError(f"invalid/duplicate request_id: {request_id!r}")
        seen.add(request_id)
        if row.get("is_research_task") is not False:
            raise VerificationRequestError(f"{request_id}: request may not be a research task")
        if row.get("claimable") is not False:
            raise VerificationRequestError(f"{request_id}: request may not be claimable")
        if row.get("runtime_dispatchable") is not False:
            raise VerificationRequestError(f"{request_id}: request may not be runtime-dispatchable")
        if row.get("authority_granted") is not False:
            raise VerificationRequestError(f"{request_id}: request may not grant authority")

        related = row.get("related_migration_ids")
        if not isinstance(related, list) or not related or any(
            not isinstance(item, str) or not item for item in related
        ):
            raise VerificationRequestError(
                f"{request_id}: related_migration_ids must be nonempty strings"
            )
        migration_states: dict[str, str] = {}
        related_rows: list[dict[str, Any]] = []
        for migration_id in related:
            migration = migration_map.get(migration_id)
            if not isinstance(migration, dict):
                raise VerificationRequestError(f"{request_id}: unknown migration_id {migration_id}")
            related_rows.append(migration)
            state = str(migration.get("state") or "")
            migration_states[migration_id] = state
            if state not in OPEN_VERIFICATION_STATES:
                raise VerificationRequestError(
                    f"{request_id}: migration {migration_id} is no longer in an open semantic-verification state ({state}); retire or update the request"
                )

        required = row.get("required_verification")
        if not isinstance(required, list) or not required or any(
            not isinstance(item, str) or not item.strip() for item in required
        ):
            raise VerificationRequestError(
                f"{request_id}: required_verification must be nonempty strings"
            )
        question = row.get("question")
        if not isinstance(question, str) or not question.strip():
            raise VerificationRequestError(f"{request_id}: verification question is required")

        evidence_status = _check_structural_evidence(request_id, row, related_rows, root)

        publication = row.get("future_authorized_publication")
        if not isinstance(publication, dict):
            raise VerificationRequestError(
                f"{request_id}: future_authorized_publication is required"
            )
        if publication.get("kind") != "GOVERNANCE":
            raise VerificationRequestError(f"{request_id}: any future task must be GOVERNANCE")
        publishers = publication.get("publisher_role_must_be_one_of")
        if not isinstance(publishers, list) or not publishers:
            raise VerificationRequestError(f"{request_id}: future publisher roles are required")
        publisher_set = set(publishers)
        if not publisher_set <= ALLOWED_FUTURE_PUBLISHERS:
            raise VerificationRequestError(
                f"{request_id}: unsupported future publisher role(s): {sorted(publisher_set - ALLOWED_FUTURE_PUBLISHERS)}"
            )
        if publication.get("publication_contract") != "research_task_publication_contract_v2.json":
            raise VerificationRequestError(
                f"{request_id}: future task must use V2 publication contract"
            )
        if publication.get("publication_tool") != "tools/research_task_records.py":
            raise VerificationRequestError(
                f"{request_id}: future task must use immutable V2 publication tool"
            )

        evidence_note = f" / evidence={evidence_status}" if evidence_status else ""
        reports.append(
            f"{request_id}: NONEXECUTABLE / migrations={migration_states} / "
            f"future_publishers={sorted(publisher_set)}{evidence_note}"
        )
    return reports


def main() -> int:
    try:
        reports = check()
    except (VerificationRequestError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    print(
        "PASS: semantic verification requests are non-executable, evidence-bounded, "
        "and bound to open governance-verification debt."
    )
    for row in reports:
        print(" -", row)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
