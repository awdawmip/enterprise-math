#!/usr/bin/env python3
"""Prove the proposed runtime control migration is structurally field-local.

No repository file is modified by this checker. It loads the current runtime JSON,
applies only the target values declared by the two approved runtime migration
entries, and proves that the resulting object is deeply identical to the source
after the declared migration pointers are removed from both copies.

Protected selector fields are also checked before and after the in-memory
transformation. This is a control-structure proof only; it does not adjudicate
mathematical truth, Working Truth, Foundation semantics, result/review status, or
any task-local mathematical content.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "control_plane" / "control_semantic_migration_registry.json"
RUNTIME = ROOT / "research_runtime_state_machine.json"
RUNTIME_MIGRATION_IDS = (
    "CSM-RUNTIME-CANONICAL-DISPATCH-004",
    "CSM-RUNTIME-OWNER-SCOPE-LIVENESS-006",
)
RUNTIME_PROTECTION_IDS = ("CSP-RUNTIME-FRESH-SELECTOR-004",)


class RuntimeMigrationEquivalenceError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeMigrationEquivalenceError(f"{path}: JSON object required")
    return value


def _tokens(pointer: str) -> list[str]:
    if not pointer.startswith("/"):
        raise RuntimeMigrationEquivalenceError(f"invalid JSON pointer: {pointer!r}")
    return [part.replace("~1", "/").replace("~0", "~") for part in pointer.split("/")[1:]]


def _get(value: dict[str, Any], pointer: str) -> Any:
    current: Any = value
    for token in _tokens(pointer):
        if not isinstance(current, dict) or token not in current:
            raise RuntimeMigrationEquivalenceError(f"pointer not found: {pointer}")
        current = current[token]
    return current


def _set(value: dict[str, Any], pointer: str, replacement: Any) -> None:
    tokens = _tokens(pointer)
    if not tokens:
        raise RuntimeMigrationEquivalenceError("root replacement is forbidden")
    current: Any = value
    for token in tokens[:-1]:
        if not isinstance(current, dict) or token not in current:
            raise RuntimeMigrationEquivalenceError(f"pointer not found: {pointer}")
        current = current[token]
    if not isinstance(current, dict) or tokens[-1] not in current:
        raise RuntimeMigrationEquivalenceError(f"pointer not found: {pointer}")
    current[tokens[-1]] = copy.deepcopy(replacement)


def _delete(value: dict[str, Any], pointer: str) -> None:
    tokens = _tokens(pointer)
    if not tokens:
        raise RuntimeMigrationEquivalenceError("root deletion is forbidden")
    current: Any = value
    for token in tokens[:-1]:
        if not isinstance(current, dict) or token not in current:
            raise RuntimeMigrationEquivalenceError(f"pointer not found: {pointer}")
        current = current[token]
    if not isinstance(current, dict) or tokens[-1] not in current:
        raise RuntimeMigrationEquivalenceError(f"pointer not found: {pointer}")
    del current[tokens[-1]]


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
    olds = entry.get("observed_legacy_values")
    targets = entry.get("canonical_target_values")
    if not isinstance(pointers, list) or not isinstance(olds, list) or not isinstance(targets, list):
        raise RuntimeMigrationEquivalenceError(f"{entry.get('migration_id')}: malformed pointer bundle")
    if not (len(pointers) == len(olds) == len(targets)):
        raise RuntimeMigrationEquivalenceError(f"{entry.get('migration_id')}: pointer bundle length mismatch")
    return [(str(pointer), old, target) for pointer, old, target in zip(pointers, olds, targets, strict=True)]


def _digest(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def prove(root: Path = ROOT) -> dict[str, Any]:
    registry = _load(root / "control_plane" / "control_semantic_migration_registry.json")
    source = _load(root / "research_runtime_state_machine.json")
    entries = {
        row.get("migration_id"): row
        for row in registry.get("entries", [])
        if isinstance(row, dict)
    }
    protections = {
        row.get("protection_id"): row
        for row in registry.get("protected_selector_fields", [])
        if isinstance(row, dict)
    }

    proposed = copy.deepcopy(source)
    changed_pointers: list[str] = []
    before_values: dict[str, Any] = {}
    after_values: dict[str, Any] = {}

    for migration_id in RUNTIME_MIGRATION_IDS:
        entry = entries.get(migration_id)
        if not isinstance(entry, dict):
            raise RuntimeMigrationEquivalenceError(f"missing runtime migration entry: {migration_id}")
        if entry.get("path") != "research_runtime_state_machine.json":
            raise RuntimeMigrationEquivalenceError(f"{migration_id}: wrong target path")
        state = str(entry.get("state") or "")
        if "READY_FOR_MECHANICAL_PATCH" not in state and state != "TARGET_MIGRATED":
            raise RuntimeMigrationEquivalenceError(
                f"{migration_id}: migration is not approved for mechanical patch: {state}"
            )
        for pointer, old, target in _field_rows(entry):
            actual = _get(source, pointer)
            if actual not in (old, target):
                raise RuntimeMigrationEquivalenceError(
                    f"{migration_id}: source has third-state value at {pointer}: {actual!r}"
                )
            before_values[pointer] = copy.deepcopy(actual)
            _set(proposed, pointer, target)
            after_values[pointer] = copy.deepcopy(_get(proposed, pointer))
            changed_pointers.append(pointer)

    protected_before: dict[str, Any] = {}
    protected_after: dict[str, Any] = {}
    for protection_id in RUNTIME_PROTECTION_IDS:
        row = protections.get(protection_id)
        if not isinstance(row, dict):
            raise RuntimeMigrationEquivalenceError(f"missing runtime protection entry: {protection_id}")
        if row.get("path") != "research_runtime_state_machine.json":
            raise RuntimeMigrationEquivalenceError(f"{protection_id}: wrong protected path")
        pointer = str(row.get("json_pointer") or "")
        required = row.get("required_value")
        before = _get(source, pointer)
        after = _get(proposed, pointer)
        if before != required or after != required:
            raise RuntimeMigrationEquivalenceError(
                f"{protection_id}: protected selector changed or already drifted: before={before!r} after={after!r} required={required!r}"
            )
        protected_before[pointer] = copy.deepcopy(before)
        protected_after[pointer] = copy.deepcopy(after)

    source_without_targets = copy.deepcopy(source)
    proposed_without_targets = copy.deepcopy(proposed)
    for pointer in sorted(set(changed_pointers), key=lambda item: item.count("/"), reverse=True):
        _delete(source_without_targets, pointer)
        _delete(proposed_without_targets, pointer)

    if source_without_targets != proposed_without_targets:
        raise RuntimeMigrationEquivalenceError(
            "proposed runtime migration changes structure outside registered migration pointers"
        )

    return {
        "target_file": "research_runtime_state_machine.json",
        "migration_ids": list(RUNTIME_MIGRATION_IDS),
        "changed_pointers": sorted(set(changed_pointers)),
        "before_values": before_values,
        "after_values": after_values,
        "protected_before": protected_before,
        "protected_after": protected_after,
        "non_target_structure_sha256": _digest(source_without_targets),
        "proposed_non_target_structure_sha256": _digest(proposed_without_targets),
        "non_target_structure_equal": True,
    }


def main() -> int:
    try:
        proof = prove()
    except (RuntimeMigrationEquivalenceError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    print(json.dumps(proof, ensure_ascii=False, indent=2, sort_keys=True))
    print("PASS: proposed runtime control migration is identical outside registered pointers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
