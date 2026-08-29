#!/usr/bin/env python3
"""Build control-only structural evidence for Architecture V2 publication cutover.

This checker does *not* approve the migration.  It applies the six publication
pointer replacements from CSM-ARCHITECTURE-TASK-PUBLICATION-003 in memory and
proves that every other JSON value is unchanged.  It also pins digests of the
research-semantic sentinel blocks called out by the non-executable verification
request.  Foundation Steward or Research Driver authority is still required to
classify the mixed-semantics migration as approved.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "control_plane" / "control_semantic_migration_registry.json"
ARCHITECTURE = ROOT / "research_architecture.json"
MIGRATION_ID = "CSM-ARCHITECTURE-TASK-PUBLICATION-003"
SENTINEL_POINTERS = (
    "/core_invariants",
    "/research_modes",
    "/context_visibility",
    "/axiom_candidate_lifecycle",
    "/working_truth_boundary",
    "/successor_stage_gate",
    "/portfolio_balance",
    "/scheduler_boundary",
    "/foundation_backflow_boundary",
    "/independence_and_replication",
    "/promotion_channels",
    "/persistence_and_promotion",
)


class ArchitectureCutoverEvidenceError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ArchitectureCutoverEvidenceError(f"{path}: JSON object required")
    return value


def _tokens(pointer: str) -> list[str]:
    if not pointer.startswith("/"):
        raise ArchitectureCutoverEvidenceError(f"invalid JSON pointer: {pointer!r}")
    return [part.replace("~1", "/").replace("~0", "~") for part in pointer.split("/")[1:]]


def _get(value: dict[str, Any], pointer: str) -> Any:
    current: Any = value
    for token in _tokens(pointer):
        if not isinstance(current, dict) or token not in current:
            raise ArchitectureCutoverEvidenceError(f"pointer not found: {pointer}")
        current = current[token]
    return current


def _set(value: dict[str, Any], pointer: str, replacement: Any) -> None:
    tokens = _tokens(pointer)
    current: Any = value
    for token in tokens[:-1]:
        if not isinstance(current, dict) or token not in current:
            raise ArchitectureCutoverEvidenceError(f"pointer not found: {pointer}")
        current = current[token]
    if not isinstance(current, dict) or tokens[-1] not in current:
        raise ArchitectureCutoverEvidenceError(f"pointer not found: {pointer}")
    current[tokens[-1]] = copy.deepcopy(replacement)


def _delete(value: dict[str, Any], pointer: str) -> None:
    tokens = _tokens(pointer)
    current: Any = value
    for token in tokens[:-1]:
        if not isinstance(current, dict) or token not in current:
            raise ArchitectureCutoverEvidenceError(f"pointer not found: {pointer}")
        current = current[token]
    if not isinstance(current, dict) or tokens[-1] not in current:
        raise ArchitectureCutoverEvidenceError(f"pointer not found: {pointer}")
    del current[tokens[-1]]


def _digest(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def prove(root: Path = ROOT) -> dict[str, Any]:
    registry = _load(root / "control_plane" / "control_semantic_migration_registry.json")
    source = _load(root / "research_architecture.json")
    entries = {
        row.get("migration_id"): row
        for row in registry.get("entries", [])
        if isinstance(row, dict)
    }
    entry = entries.get(MIGRATION_ID)
    if not isinstance(entry, dict):
        raise ArchitectureCutoverEvidenceError(f"missing migration entry: {MIGRATION_ID}")
    if entry.get("path") != "research_architecture.json":
        raise ArchitectureCutoverEvidenceError("architecture migration points to wrong file")
    if entry.get("state") != "REQUIRES_GOVERNANCE_VERIFICATION":
        raise ArchitectureCutoverEvidenceError(
            "control structural evidence is only valid while governance verification remains open"
        )

    pointers = entry.get("json_pointers")
    old_values = entry.get("observed_legacy_values")
    target_values = entry.get("canonical_target_values")
    if not isinstance(pointers, list) or not isinstance(old_values, list) or not isinstance(target_values, list):
        raise ArchitectureCutoverEvidenceError("architecture migration pointer bundle malformed")
    if len(pointers) != 6 or not (len(pointers) == len(old_values) == len(target_values)):
        raise ArchitectureCutoverEvidenceError("architecture migration must remain an exact six-pointer bundle")

    proposed = copy.deepcopy(source)
    before_values: dict[str, Any] = {}
    after_values: dict[str, Any] = {}
    for pointer, old, target in zip(pointers, old_values, target_values, strict=True):
        pointer = str(pointer)
        actual = _get(source, pointer)
        if actual not in (old, target):
            raise ArchitectureCutoverEvidenceError(
                f"{pointer}: unexpected third-state value {actual!r}"
            )
        before_values[pointer] = copy.deepcopy(actual)
        _set(proposed, pointer, target)
        after_values[pointer] = copy.deepcopy(_get(proposed, pointer))

    source_without_targets = copy.deepcopy(source)
    proposed_without_targets = copy.deepcopy(proposed)
    for pointer in sorted((str(item) for item in pointers), key=lambda item: item.count("/"), reverse=True):
        _delete(source_without_targets, pointer)
        _delete(proposed_without_targets, pointer)
    if source_without_targets != proposed_without_targets:
        raise ArchitectureCutoverEvidenceError(
            "proposed publication cutover changes architecture outside the six registered pointers"
        )

    sentinels: dict[str, dict[str, str]] = {}
    for pointer in SENTINEL_POINTERS:
        before = _get(source, pointer)
        after = _get(proposed, pointer)
        if before != after:
            raise ArchitectureCutoverEvidenceError(
                f"research semantic sentinel changed under proposed cutover: {pointer}"
            )
        digest = _digest(before)
        sentinels[pointer] = {"before": digest, "after": _digest(after)}

    return {
        "status": "CONTROL_STRUCTURAL_EVIDENCE_ONLY_NOT_GOVERNANCE_APPROVAL",
        "migration_id": MIGRATION_ID,
        "source_architecture_blob_sha1": entry.get("baseline_blob_sha1"),
        "changed_pointer_count": len(pointers),
        "changed_pointers": list(pointers),
        "before_values": before_values,
        "after_values": after_values,
        "non_target_structure_equal": True,
        "non_target_structure_sha256": _digest(source_without_targets),
        "proposed_non_target_structure_sha256": _digest(proposed_without_targets),
        "semantic_sentinel_digests": sentinels,
        "governance_approval_granted": False,
        "migration_authority_granted": False,
    }


def main() -> int:
    try:
        evidence = prove()
    except (ArchitectureCutoverEvidenceError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    print(json.dumps(evidence, ensure_ascii=False, indent=2, sort_keys=True))
    print("PASS: architecture V2 publication cutover is field-local; governance semantic approval remains open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
