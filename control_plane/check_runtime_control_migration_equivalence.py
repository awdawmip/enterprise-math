#!/usr/bin/env python3
"""Verify the terminal V2 runtime cutover and retired migration binding.

The old gradual runtime-pointer migrations are complete. This checker no longer
constructs a hypothetical edit against removed V1 paths. Instead it proves that
``research_runtime_state_machine.json`` is the active V2 surface, that the exact
live/fresh/liveness fields retain their required values, that the retired legacy
paths remain absent, and that the migration registry binds those facts to the
pre-V2 archive and cutover commit.

This is a control-structure check only. It grants no mathematical, task,
publication, Working Truth, Foundation, Driver, review, or successor authority.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "control_plane" / "control_semantic_migration_registry.json"
RUNTIME = ROOT / "research_runtime_state_machine.json"
RETIRED_IDS = (
    "CSM-RUNTIME-CANONICAL-DISPATCH-004",
    "CSM-RUNTIME-OWNER-SCOPE-LIVENESS-006",
)
PROTECTION_ID = "CSP-RUNTIME-FRESH-SELECTOR-004"
RETIRED_STATE = "RETIRED_BY_V2_PHYSICAL_CUTOVER"
_FULL_SHA = re.compile(r"^[0-9a-f]{40}$")


class RuntimeMigrationEquivalenceError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeMigrationEquivalenceError(f"{path}: JSON object required")
    return value


def _pointer(value: Any, pointer: str) -> Any:
    if not pointer.startswith("/"):
        raise RuntimeMigrationEquivalenceError(f"invalid JSON pointer: {pointer!r}")
    current = value
    for raw in pointer.split("/")[1:]:
        token = raw.replace("~1", "/").replace("~0", "~")
        if not isinstance(current, dict) or token not in current:
            raise RuntimeMigrationEquivalenceError(f"pointer not found: {pointer}")
        current = current[token]
    return current


def _exists(value: Any, pointer: str) -> bool:
    try:
        _pointer(value, pointer)
    except RuntimeMigrationEquivalenceError:
        return False
    return True


def _digest(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def prove(root: Path = ROOT) -> dict[str, Any]:
    registry = _load(root / "control_plane" / "control_semantic_migration_registry.json")
    runtime = _load(root / "research_runtime_state_machine.json")

    required_runtime = {
        "/schema": "ENTERPRISE_MATH_RESEARCH_RUNTIME_STATE_MACHINE_V2",
        "/status": "ACTIVE_CANONICAL",
        "/classification": "CONTROL_FLOW_ONLY_NO_MATHEMATICAL_AUTHORITY",
        "/task_definition_authority": "research_task_records/<task-id>/<publication-id>.json",
        "/runtime_policy": "research_runtime_policy_v2.json",
        "/event_reducer": "tools/research_runtime_reducer.py",
        "/canonical_live_dispatch": "research_control_dispatch.py",
        "/fresh_task_selector": "tools/research_dispatch.py",
        "/fresh_lane_selector": "tools/research_lane_dispatch.py",
        "/executable_runtime": "tools/research_runtime_guard.py",
        "/owner_lease_is_session_liveness": False,
        "/stale_valid_owner_action": "ADOPT_EXISTING_CLAIM",
        "/legacy_runtime_on_main": False,
        "/legacy_archive/branch": "archive/legacy-control-plane-pre-v2-20260902",
        "/legacy_archive/source_commit": "ce629e24e5af59128e25af87075c6622413684e0",
    }
    for pointer, required in required_runtime.items():
        actual = _pointer(runtime, pointer)
        if actual != required:
            raise RuntimeMigrationEquivalenceError(
                f"runtime V2 field drift at {pointer}: actual={actual!r} required={required!r}"
            )

    forbidden_legacy_paths = {
        "/dispatch",
        "/composes",
        "/lease_model",
    }
    reappeared = sorted(pointer for pointer in forbidden_legacy_paths if _exists(runtime, pointer))
    if reappeared:
        raise RuntimeMigrationEquivalenceError(
            f"legacy runtime blocks reappeared after physical cutover: {reappeared}"
        )

    protections = {
        row.get("protection_id"): row
        for row in registry.get("protected_selector_fields", [])
        if isinstance(row, dict)
    }
    protection = protections.get(PROTECTION_ID)
    if not isinstance(protection, dict):
        raise RuntimeMigrationEquivalenceError(
            f"missing runtime selector protection: {PROTECTION_ID}"
        )
    if (
        protection.get("path") != "research_runtime_state_machine.json"
        or protection.get("json_pointer") != "/fresh_task_selector"
        or protection.get("required_value") != "tools/research_dispatch.py"
        or _pointer(runtime, "/fresh_task_selector") != protection.get("required_value")
    ):
        raise RuntimeMigrationEquivalenceError(
            "runtime fresh-selector protection is not bound to the exact V2 field"
        )

    retired = {
        row.get("migration_id"): row
        for row in registry.get("retired_entries", [])
        if isinstance(row, dict)
    }
    retired_proofs: dict[str, Any] = {}
    for migration_id in RETIRED_IDS:
        row = retired.get(migration_id)
        if not isinstance(row, dict):
            raise RuntimeMigrationEquivalenceError(
                f"missing retired runtime migration: {migration_id}"
            )
        if (
            row.get("state") != RETIRED_STATE
            or row.get("execution_authority_while_open") is not False
            or row.get("current_target_path") != "research_runtime_state_machine.json"
            or row.get("archive_branch") != "archive/legacy-control-plane-pre-v2-20260902"
            or not isinstance(row.get("archive_source_commit"), str)
            or not _FULL_SHA.fullmatch(row["archive_source_commit"])
            or not isinstance(row.get("cutover_commit"), str)
            or not _FULL_SHA.fullmatch(row["cutover_commit"])
        ):
            raise RuntimeMigrationEquivalenceError(
                f"{migration_id}: retired provenance envelope invalid"
            )
        legacy = row.get("legacy_json_pointers")
        required = row.get("current_required_fields")
        if not isinstance(legacy, list) or not legacy:
            raise RuntimeMigrationEquivalenceError(
                f"{migration_id}: legacy pointer list missing"
            )
        if not isinstance(required, dict) or not required:
            raise RuntimeMigrationEquivalenceError(
                f"{migration_id}: current V2 field map missing"
            )
        for pointer in legacy:
            if not isinstance(pointer, str) or _exists(runtime, pointer):
                raise RuntimeMigrationEquivalenceError(
                    f"{migration_id}: legacy pointer is invalid or reappeared: {pointer!r}"
                )
        for pointer, expected in required.items():
            actual = _pointer(runtime, str(pointer))
            if actual != expected:
                raise RuntimeMigrationEquivalenceError(
                    f"{migration_id}: retired binding drift at {pointer}: "
                    f"actual={actual!r} expected={expected!r}"
                )
        retired_proofs[migration_id] = {
            "legacy_paths_absent": list(legacy),
            "current_fields_exact": dict(required),
            "archive_branch": row["archive_branch"],
            "archive_source_commit": row["archive_source_commit"],
            "cutover_commit": row["cutover_commit"],
        }

    return {
        "status": "V2_RUNTIME_CUTOVER_VERIFIED",
        "target_file": "research_runtime_state_machine.json",
        "runtime_sha256": _digest(runtime),
        "required_runtime_fields": required_runtime,
        "forbidden_legacy_paths_absent": sorted(forbidden_legacy_paths),
        "fresh_selector_protection_id": PROTECTION_ID,
        "retired_migrations": retired_proofs,
        "mathematical_authority_granted": False,
        "execution_authority_granted": False,
    }


def main() -> int:
    try:
        proof = prove()
    except (RuntimeMigrationEquivalenceError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    print(json.dumps(proof, ensure_ascii=False, indent=2, sort_keys=True))
    print(
        "PASS: V2 runtime cutover is exact; legacy runtime paths remain absent and "
        "retired migrations bind the current fields to archive provenance."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
