#!/usr/bin/env python3
"""Audit active semantic migration debt and exact V2 cutover retirements.

Active entries may contain only their frozen legacy value or declared canonical
target. Protected selector fields remain exact. Runtime-pointer migrations that
were completed by the pre-V2 physical cutover are no longer active patch debt:
they live in ``retired_entries`` and must prove both that the legacy JSON paths
are absent and that the current V2 fields retain their required values.

This checker is control-plane only and grants no mathematical, Working Truth,
Foundation, Driver, publication, execution, or successor authority.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "control_plane" / "control_semantic_migration_registry.json"
AUTHORITY_PATH = ROOT / "control_plane" / "current_control_authority.json"
SCHEMA = "ENTERPRISE_MATH_CONTROL_SEMANTIC_MIGRATION_REGISTRY_V1"
RETIRED_STATE = "RETIRED_BY_V2_PHYSICAL_CUTOVER"
REQUIRED_RETIRED_RUNTIME_IDS = {
    "CSM-RUNTIME-CANONICAL-DISPATCH-004",
    "CSM-RUNTIME-OWNER-SCOPE-LIVENESS-006",
}
_FULL_SHA = re.compile(r"^[0-9a-f]{40}$")


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


def _pointer_exists(value: Any, pointer: str) -> bool:
    try:
        _pointer(value, pointer)
    except MigrationRegistryError:
        return False
    return True


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
    return [
        (str(pointer), old, target)
        for pointer, old, target in zip(pointers, legacy, targets, strict=True)
    ]


def _check_protected_selectors(registry: dict[str, Any], root: Path) -> list[str]:
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
        if not isinstance(semantic_role, str) or not semantic_role:
            raise MigrationRegistryError(f"{protection_id}: semantic_role missing")
        if not isinstance(reason, str) or not reason:
            raise MigrationRegistryError(f"{protection_id}: reason missing")

        path = root / path_value
        if not path.exists():
            raise MigrationRegistryError(
                f"{protection_id}: protected target file missing: {path_value}"
            )
        actual = _pointer(_load(path), pointer)
        if actual != required:
            raise MigrationRegistryError(
                f"{protection_id}: protected selector {path_value}{pointer} drifted to "
                f"{actual!r}; required={required!r} ({semantic_role})"
            )
        reports.append(
            f"{protection_id}: PROTECTED_SELECTOR / {semantic_role} / "
            f"{path_value}{pointer}={required!r}"
        )
    return reports


def _check_active_entries(
    registry: dict[str, Any], root: Path
) -> tuple[list[str], set[str]]:
    entries = registry.get("entries")
    if not isinstance(entries, list) or not entries:
        raise MigrationRegistryError("semantic migration registry has no active entries")

    seen: set[str] = set()
    reports: list[str] = []
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
            if actual == target:
                field_states.append(f"{pointer}=TARGET_OR_RESOLVED")
            elif actual == old:
                field_states.append(f"{pointer}=LEGACY_PENDING")
            else:
                raise MigrationRegistryError(
                    f"{migration_id}: {pointer} has unexpected third value {actual!r}; "
                    f"allowed legacy={old!r} or target={target!r}"
                )
        reports.append(
            f"{migration_id}: {state} / {risk} / {blob_note} / " + ", ".join(field_states)
        )
    return reports, seen


def _check_retired_entries(
    registry: dict[str, Any], root: Path, active_ids: set[str]
) -> list[str]:
    rows = registry.get("retired_entries")
    if not isinstance(rows, list):
        raise MigrationRegistryError("retired_entries must be a list")

    seen: set[str] = set()
    reports: list[str] = []
    for row in rows:
        if not isinstance(row, dict):
            raise MigrationRegistryError("retired migration entry must be an object")
        migration_id = row.get("migration_id")
        if not isinstance(migration_id, str) or not migration_id or migration_id in seen:
            raise MigrationRegistryError(f"invalid/duplicate retired migration_id: {migration_id!r}")
        if migration_id in active_ids:
            raise MigrationRegistryError(f"{migration_id}: migration cannot be active and retired")
        seen.add(migration_id)

        if row.get("state") != RETIRED_STATE:
            raise MigrationRegistryError(f"{migration_id}: wrong retired state")
        if row.get("execution_authority_while_open") is not False:
            raise MigrationRegistryError(f"{migration_id}: retired entry cannot grant authority")
        for field in ("archive_branch", "legacy_target_path", "current_target_path"):
            if not isinstance(row.get(field), str) or not row[field]:
                raise MigrationRegistryError(f"{migration_id}: missing {field}")
        if not str(row["archive_branch"]).startswith("archive/"):
            raise MigrationRegistryError(f"{migration_id}: archive_branch must be an archive ref")
        for field in ("archive_source_commit", "cutover_commit"):
            value = row.get(field)
            if not isinstance(value, str) or not _FULL_SHA.fullmatch(value):
                raise MigrationRegistryError(f"{migration_id}: {field} must be a full commit SHA")

        legacy_pointers = row.get("legacy_json_pointers")
        required_fields = row.get("current_required_fields")
        if not isinstance(legacy_pointers, list) or not legacy_pointers or not all(
            isinstance(item, str) and item.startswith("/") for item in legacy_pointers
        ):
            raise MigrationRegistryError(f"{migration_id}: legacy_json_pointers invalid")
        if not isinstance(required_fields, dict) or not required_fields:
            raise MigrationRegistryError(f"{migration_id}: current_required_fields invalid")

        current_path = root / str(row["current_target_path"])
        if not current_path.exists():
            raise MigrationRegistryError(
                f"{migration_id}: current target missing: {row['current_target_path']}"
            )
        document = _load(current_path)
        for pointer in legacy_pointers:
            if _pointer_exists(document, pointer):
                raise MigrationRegistryError(
                    f"{migration_id}: retired legacy pointer reappeared: {pointer}"
                )
        for pointer, required in required_fields.items():
            if not isinstance(pointer, str) or not pointer.startswith("/"):
                raise MigrationRegistryError(f"{migration_id}: invalid current pointer {pointer!r}")
            actual = _pointer(document, pointer)
            if actual != required:
                raise MigrationRegistryError(
                    f"{migration_id}: current V2 field {pointer} drifted to {actual!r}; "
                    f"required={required!r}"
                )
        reports.append(
            f"{migration_id}: {RETIRED_STATE} / legacy paths absent / "
            f"{len(required_fields)} V2 field(s) exact"
        )

    missing = REQUIRED_RETIRED_RUNTIME_IDS - seen
    if missing:
        raise MigrationRegistryError(
            f"required retired runtime migrations missing: {sorted(missing)}"
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
    active_reports, active_ids = _check_active_entries(registry, root)
    reports.extend(active_reports)
    reports.extend(_check_retired_entries(registry, root, active_ids))
    return reports


def main() -> int:
    try:
        reports = check()
    except (MigrationRegistryError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    print(
        "PASS: active semantic migration debt remains fail-closed; completed runtime "
        "migrations are retired against exact V2 fields and absent legacy paths."
    )
    for row in reports:
        print(" -", row)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
