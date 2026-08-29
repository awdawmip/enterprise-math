#!/usr/bin/env python3
"""Audit non-executable semantic verification requests.

A CONTROL_PLANE_MAINTENANCE conversation may preserve an unresolved semantic
question, but it may not turn that request into a scheduler task or grant itself
Researcher/Driver/Steward authority.  This checker binds each request to an open
migration-registry item and requires any future real task to use the immutable
V2 publication path under an authorized publisher role.
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


class VerificationRequestError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise VerificationRequestError(f"{path.relative_to(ROOT)}: JSON object required")
    return value


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
        if not isinstance(related, list) or not related or any(not isinstance(item, str) or not item for item in related):
            raise VerificationRequestError(f"{request_id}: related_migration_ids must be nonempty strings")
        migration_states: dict[str, str] = {}
        for migration_id in related:
            migration = migration_map.get(migration_id)
            if not isinstance(migration, dict):
                raise VerificationRequestError(f"{request_id}: unknown migration_id {migration_id}")
            state = str(migration.get("state") or "")
            migration_states[migration_id] = state
            if state not in OPEN_VERIFICATION_STATES:
                raise VerificationRequestError(
                    f"{request_id}: migration {migration_id} is no longer in an open semantic-verification state ({state}); retire or update the request"
                )

        required = row.get("required_verification")
        if not isinstance(required, list) or not required or any(not isinstance(item, str) or not item.strip() for item in required):
            raise VerificationRequestError(f"{request_id}: required_verification must be nonempty strings")
        question = row.get("question")
        if not isinstance(question, str) or not question.strip():
            raise VerificationRequestError(f"{request_id}: verification question is required")

        publication = row.get("future_authorized_publication")
        if not isinstance(publication, dict):
            raise VerificationRequestError(f"{request_id}: future_authorized_publication is required")
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
            raise VerificationRequestError(f"{request_id}: future task must use V2 publication contract")
        if publication.get("publication_tool") != "tools/research_task_records.py":
            raise VerificationRequestError(f"{request_id}: future task must use immutable V2 publication tool")

        reports.append(
            f"{request_id}: NONEXECUTABLE / migrations={migration_states} / future_publishers={sorted(publisher_set)}"
        )
    return reports


def main() -> int:
    try:
        reports = check()
    except (VerificationRequestError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    print("PASS: semantic verification requests are non-executable and bound to open governance-verification debt.")
    for row in reports:
        print(" -", row)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
