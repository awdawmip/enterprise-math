#!/usr/bin/env python3
"""Audit gradual control-pointer migration without adjudicating mathematics.

This checker is intentionally conservative. A registered migration field may
contain only its frozen legacy value or the declared already-canonical target
value. Anything else is a control-state inconsistency and fails closed.
Baseline blob drift is reported but is not itself an error because the
containing file may legitimately change mathematical or research semantics
outside the registered JSON pointer.

Some dispatch-looking fields are intentionally subordinate task-definition or
fresh selectors rather than top-level live routes. Those fields are registered
under ``protected_selector_fields`` and must remain at their exact required
value. This prevents a blind string-replacement migration from changing their
meaning.

The checker does not decide whether a MIXED_* entry is safe to migrate; it only
keeps the unresolved debt explicit and prevents silent semantic drift.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "control_plane" / "control_semantic_migration_registry.json"
AUTHORITY_PATH = ROOT / "control_plane" / "current_control_authority.json"
SCHEMA = "ENTERPRISE_MATH_CONTROL_SEMANTIC_MIGRATION_REGISTRY_V1"


class MigrationRegistryError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise MigrationRegistryError(f"{path.relative_to(ROOT)}: JSON object required")
    return value


def _blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def _pointer(value: Any, pointer: str) -> Any:
    if pointer == "":
        return value
    if not pointer.startswith("/"):
        raise MigrationRegistryError(f"invalid JSON pointer: {pointer!r}")
    current = value
    for raw in pointer.split("/")[1:]:
        token = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(current, dict) and token in current:
            current = current[token]
        else:
            raise MigrationRegistryError(f"JSON pointer not found: {pointer}")
    return current


def _field_rows(entry: dict[str, Any]) -> list[tuple[str, Any, Any]]:
    if "json_pointer" in entry:
        return [
            (
                str(entry["json_pointer"]),
                entry.get("observed_legacy_value"),
                entry.get("canonical_target_value"),
            )
        ]
    pointers = entry.get("json_pointers")
    legacy = entry.get("observed_legacy_values")
    targets = entry.get("canonical_target_values")
    if not isinstance(pointers, list) or not isinstance(legacy, list) or not isinstance(targets, list):
        raise MigrationRegistryError(f"{entry.get('migration_id')}: malformed multi-field entry")
    if not (len(pointers) == len(legacy) == len(targets)) or not pointers:
        raise MigrationRegistryError(f"{entry.get('migration_id')}: pointer/value list lengths differ")
    return [(str(pointer), old, target) for pointer, old, target in zip(pointers, legacy, targets, strict=True)]


def _check_protected_selectors(
    registry: dict[str, Any], root: Path
) -> list[str]:
    rows = registry.get("protected_selector_fields")
    if not isinstance(rows, list) or not rows:
        raise MigrationRegistryError("semantic migration registry has no protected selector fields")

    seen: set[str] = set()
    reports: list[str] = []
    for row in rows:
        if not isinstance(row, dict):
            raise MigrationRegistryError("protected selector entry must be an object")
        protection_id = row.get("protection_id")
        if not isinstance(protection_id, str) or not protection_id or protection_id in seen:
            raise MigrationRegistryError(f"invalid/duplicate protection_id: {protection_id!r}")
        seen.add(protection_id)

        path_value = row.get("path")
        pointer = row.get("json_pointer")
        required = row.get("required_value")
        semantic_role = row.get("semantic_role")
        reason = row.get("reason")
        if not isinstance(path_value, str) or not path_value:
            raise MigrationRegistryError(f"{protection_id}: path missing")
        if not isinstance(pointer, str) or not pointer:
            raise MigrationRegistryError(f"{protection_id}: json_pointer missing")
        if not isinstance(required, str) or not required:
            raise MigrationRegistryError(f"{protection_id}: required_value missing")
        if not isinstance(semantic_role, str) or not semantic_role:
            raise MigrationRegistryError(f"{protection_id}: semantic_role missing")
        if not isinstance(reason, str) or not reason:
            raise MigrationRegistryError(f"{protection_id}: reason missing")

        path = root / path_value
        if not path.exists():
            raise MigrationRegistryError(
                f"{protection_id}: protected target file missing: {path_value}"
            )
        document = _load(path)
        actual = _pointer(document, pointer)
        if actual != required:
            raise MigrationRegistryError(
                f"{protection_id}: protected selector {path_value}{pointer} drifted to "
                f"{actual!r}; required={required!r} ({semantic_role})"
            )
        reports.append(
            f"{protection_id}: PROTECTED_SELECTOR / {semantic_role} / "
            f"{path_value}{pointer}={required}"
        )
    return reports


def check(root: Path = ROOT) -> list[str]:
    registry = _load(root / "control_plane" / "control_semantic_migration_registry.json")
    authority = _load(root / "control_plane" / "current_control_authority.json")
    if registry.get("schema") != SCHEMA or registry.get("status") != "ACTIVE":
        raise MigrationRegistryError("semantic migration registry schema/status invalid")
    if registry.get("authority") != "control_plane/current_control_authority.json":
        raise MigrationRegistryError("semantic migration registry authority pointer drifted")
    if authority.get("status") != "ACTIVE_CANONICAL_CONTROL_PRECEDENCE":
        raise MigrationRegistryError("current control authority is not active")

    reports = _check_protected_selectors(registry, root)

    entries = registry.get("entries")
    if not isinstance(entries, list) or not entries:
        raise MigrationRegistryError("semantic migration registry has no entries")
    seen: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise MigrationRegistryError("migration entry must be an object")
        migration_id = entry.get("migration_id")
        if not isinstance(migration_id, str) or not migration_id or migration_id in seen:
            raise MigrationRegistryError(f"invalid/duplicate migration_id: {migration_id!r}")
        seen.add(migration_id)
        if entry.get("execution_authority_while_open") is not False:
            raise MigrationRegistryError(f"{migration_id}: open debt may not grant execution authority")
        path_value = entry.get("path")
        if not isinstance(path_value, str) or not path_value:
            raise MigrationRegistryError(f"{migration_id}: path missing")
        path = root / path_value
        if not path.exists():
            raise MigrationRegistryError(f"{migration_id}: target file missing: {path_value}")
        document = _load(path)
        baseline = entry.get("baseline_blob_sha1")
        actual_blob = _blob_sha1(path)
        blob_note = "baseline-match" if baseline == actual_blob else f"baseline-drift:{actual_blob}"
        state = str(entry.get("state") or "")
        risk = str(entry.get("risk_class") or "")
        if not state or not risk:
            raise MigrationRegistryError(f"{migration_id}: state/risk_class required")

        field_states: list[str] = []
        for pointer, old, target in _field_rows(entry):
            actual = _pointer(document, pointer)
            if actual == old:
                field_states.append(f"{pointer}=LEGACY_PENDING")
            elif actual == target:
                field_states.append(f"{pointer}=TARGET_MIGRATED")
            else:
                raise MigrationRegistryError(
                    f"{migration_id}: {pointer} has unexpected third value {actual!r}; "
                    f"allowed legacy={old!r} or target={target!r}"
                )
        reports.append(
            f"{migration_id}: {state} / {risk} / {blob_note} / " + ", ".join(field_states)
        )
    return reports


def main() -> int:
    try:
        reports = check()
    except (MigrationRegistryError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    print(
        "PASS: semantic migration debt is explicit; protected selectors retain their "
        "meaning and no registered control field has third-state drift."
    )
    for row in reports:
        print(" -", row)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
