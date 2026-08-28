#!/usr/bin/env python3
"""Source-backed Driver authority guard for Objective control records.

This layer is intentionally separate from objective semantics. It proves that a
post-cutover Objective generation, operational head selection, or historical task
binding was performed by a Driver whose Issue #240 authority was active at the
control-action time. Legacy exemptions are exact frozen IDs, never timestamps.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import research_driver_authority as driver_authority

ROOT = Path(__file__).resolve().parent


def _contract(root: Path) -> dict[str, Any] | None:
    return driver_authority.contract(root)


def authority_fields(driver_id: str, at: str, root: Path = ROOT) -> dict[str, Any]:
    authority = driver_authority.require_active_driver(driver_id, at, root)
    if authority is None:
        return {}
    return {
        "driver_authority_record_id": authority["authority_record_id"],
        "driver_authority_source_comment_id": authority["source_comment_id"],
    }


def _errors_for_action(
    *,
    actor: Any,
    at: Any,
    authority_record_id: Any,
    authority_source_comment_id: Any,
    prefix: str,
    root: Path,
) -> list[str]:
    if not driver_authority.contract_enabled(root):
        return []
    if not isinstance(actor, str) or not isinstance(at, str):
        return [f"{prefix}: Driver actor/time provenance fields are required"]
    try:
        active = driver_authority.require_active_driver(actor, at, root)
    except driver_authority.DriverAuthorityError as exc:
        return [f"{prefix}: {exc}"]
    if active is None:
        return [f"{prefix}: Driver authority enforcement unexpectedly disabled"]
    if authority_record_id != active.get("authority_record_id"):
        return [f"{prefix}: driver_authority_record_id does not pin active authority"]
    if authority_source_comment_id != active.get("source_comment_id"):
        return [f"{prefix}: driver_authority_source_comment_id does not pin active authority"]
    return []


def audit(root: Path = ROOT) -> list[str]:
    if not driver_authority.contract_enabled(root):
        return []
    try:
        contract = _contract(root)
        if contract is None:
            return []
        import research_objective_records as objectives
        records = objectives.iter_objective_records(root)
        heads = objectives.iter_heads(root)
        bindings = objectives.iter_bindings(root)
    except Exception as exc:
        return [str(exc)]

    errors: list[str] = []
    legacy_generations = set(contract.get("legacy_objective_generation_ids") or [])
    legacy_heads = contract.get("legacy_objective_heads") or {}
    legacy_bindings = set(contract.get("legacy_task_objective_bindings") or [])
    if not isinstance(legacy_heads, dict):
        return ["legacy_objective_heads must be an object"]

    for item in records:
        gid = item.get("objective_generation_id")
        if gid in legacy_generations:
            continue
        prefix = str(item.get("_record_path") or gid or "<objective-generation>")
        errors.extend(
            _errors_for_action(
                actor=item.get("publisher_id"),
                at=item.get("created_at"),
                authority_record_id=item.get("driver_authority_record_id"),
                authority_source_comment_id=item.get("driver_authority_source_comment_id"),
                prefix=prefix,
                root=root,
            )
        )

    for item in heads:
        oid = item.get("objective_id")
        gid = item.get("objective_generation_id")
        if isinstance(oid, str) and legacy_heads.get(oid) == gid:
            continue
        prefix = str(item.get("_head_path") or oid or "<objective-head>")
        errors.extend(
            _errors_for_action(
                actor=item.get("updated_by"),
                at=item.get("updated_at"),
                authority_record_id=item.get("driver_authority_record_id"),
                authority_source_comment_id=item.get("driver_authority_source_comment_id"),
                prefix=prefix,
                root=root,
            )
        )

    for item in bindings:
        key = f"{item.get('task_id')}|{item.get('publication_id')}"
        if key in legacy_bindings:
            continue
        prefix = str(item.get("_binding_path") or key)
        errors.extend(
            _errors_for_action(
                actor=item.get("bound_by"),
                at=item.get("bound_at"),
                authority_record_id=item.get("driver_authority_record_id"),
                authority_source_comment_id=item.get("driver_authority_source_comment_id"),
                prefix=prefix,
                root=root,
            )
        )
    return errors


def main() -> int:
    errors = audit(ROOT)
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print("PASS: Objective Driver authority provenance valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
