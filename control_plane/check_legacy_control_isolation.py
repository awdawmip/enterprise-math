#!/usr/bin/env python3
"""Fail closed if the pre-V2 control surface or migration drift re-enters main."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import research_task_semantic_integrity_fault_isolation  # noqa: E402

ARCHIVE_BRANCH = "archive/legacy-control-plane-pre-v2-20260902"
ARCHIVE_SHA = "ce629e24e5af59128e25af87075c6622413684e0"
LEGACY_PATHS = [
    "research_scheduler.json",
    "tools/research_scheduler.py",
    "research_task_registry.json",
    "tools/research_task_registry.py",
    "research_task_publication_contract.json",
    "tools/check_task_registry_cutover.py",
    "docs/RESEARCH_SCHEDULER.md",
    "docs/RESEARCH_TASK_PUBLICATION_PROTOCOL_V1.md",
    "docs/RESEARCH_SCHEDULER_NONBLOCKING_STARTUP.md",
]
FORBIDDEN_NAMES = (
    "research_scheduler.json",
    "tools/research_scheduler.py",
    "research_task_registry.json",
    "tools/research_task_registry.py",
    "research_task_publication_contract.json",
    "tools/check_task_registry_cutover.py",
)
ACTIVE_PROMPTS = (
    "AGENTS.md",
    "docs/RESEARCH_RUNTIME_STATE_MACHINE.md",
    "docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md",
    "docs/RESEARCH_SCHEDULING_PROTOCOL.en.md",
    "docs/RESEARCH_SCHEDULING_PROTOCOL.zh-CN.md",
    "docs/RESEARCH_ARCHITECTURE.md",
    "docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md",
    "research_roles/EM_FREE_RESEARCHER_ROLE.md",
)
SUCCESSOR_GATE = {
    "new_information_gap": "writer canary gap",
    "why_parent_result_does_not_close_it": "writer canary parent boundary",
    "discriminating_outcomes": ["writer canary outcome"],
    "kill_condition": "writer canary kill",
    "alternative_route_or_free_exploration_considered": "writer canary alternative",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "writer canary continuation reason",
}


def _check_semantic_writer() -> list[str]:
    """Exercise the public writer without creating a repository publication."""
    from tools import research_task_records

    errors: list[str] = []
    with TemporaryDirectory() as directory:
        root = Path(directory)
        path = root / "research_tasks" / "WRITER_CANARY.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("semantic-preservation writer canary\n", encoding="utf-8")
        migration_source = {
            "archive_branch": ARCHIVE_BRANCH,
            "source_commit": ARCHIVE_SHA,
            "source_kind": "WRITER_CANARY",
        }
        meta = {
            "task_id": "RS-CONTROL-SEMANTIC-WRITER-CANARY",
            "parent_objective_id": "OBJ-CONTROL-SEMANTIC-WRITER-CANARY",
            "parent_objective_generation_id": "OG-CONTROL-SEMANTIC-WRITER-CANARY",
            "priority": "P1",
            "leverage": "HIGH",
            "owner": "control-plane/semantic-writer-canary",
            "frontier": "writer canary",
            "next_action": "writer canary",
            "kind": "GOVERNANCE",
            "origin_kind": "DIRECT_USER_DIRECTION",
            "task_lineage": "CONTINUATION",
            "parent_task_id": "RS-CONTROL-SEMANTIC-WRITER-PARENT",
            "identity_lane": "CONTROLSEM",
            "source_refs": ["source/ref@canary"],
            "dependencies": ["dependency-canary"],
            "evidence_status": "WRITER_CANARY",
            "successor_gate": SUCCESSOR_GATE,
            "migration_source": migration_source,
        }
        record = research_task_records.build_record(
            meta,
            path=path,
            publisher_role="RESEARCH_DRIVER",
            publisher_id="EM-DVR-WRITER-CANARY",
            research_value="writer semantic-preservation canary",
            published_at="2026-09-02T00:00:00+00:00",
            supersedes_publication_id=None,
            root=root,
        )
        expected = {
            "identity_lane": "CONTROLSEM",
            "origin_kind": "DIRECT_USER_DIRECTION",
            "task_lineage": "CONTINUATION",
            "parent_task_id": "RS-CONTROL-SEMANTIC-WRITER-PARENT",
            "source_refs": ["source/ref@canary"],
            "dependencies": ["dependency-canary"],
            "evidence_status": "WRITER_CANARY",
            "successor_gate": SUCCESSOR_GATE,
            "migration_source": migration_source,
            "parent_objective_generation_id": "OG-CONTROL-SEMANTIC-WRITER-CANARY",
        }
        for field, value in expected.items():
            if record.get(field) != value:
                errors.append(
                    f"canonical publication writer does not preserve {field}: "
                    f"expected={value!r} actual={record.get(field)!r}"
                )
        if record.get("migration_source") == record.get("successor_gate"):
            errors.append(
                "canonical publication writer conflates migration provenance and task semantics"
            )
    return errors


def check() -> list[str]:
    errors: list[str] = []
    for rel in LEGACY_PATHS:
        if (ROOT / rel).exists():
            errors.append(f"legacy control path remains on main: {rel}")
    manifest_path = ROOT / "control_plane/legacy_control_migration_manifest.json"
    if not manifest_path.is_file():
        errors.append("migration manifest missing")
        return errors
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("status") != "COMPLETE":
        errors.append("migration manifest is not COMPLETE")
    source = manifest.get("source") or {}
    if (
        source.get("archive_branch") != ARCHIVE_BRANCH
        or source.get("commit") != ARCHIVE_SHA
    ):
        errors.append("migration manifest archive pin mismatch")
    rows = manifest.get("tasks")
    if not isinstance(rows, list) or len(rows) != 27:
        errors.append("migration manifest must preserve exactly 27 legacy task identities")
    elif len({row.get("task_id") for row in rows if isinstance(row, dict)}) != 27:
        errors.append("migration manifest task identities are duplicated or incomplete")
    authority = manifest.get("authority") or {}
    for flag in (
        "mathematical_truth_granted",
        "working_truth_granted",
        "foundation_authority_granted",
        "canonical_promotion_granted",
        "execution_claim_created",
    ):
        if authority.get(flag) is not False:
            errors.append(f"migration manifest illegally grants {flag}")
    policy = json.loads((ROOT / "research_runtime_policy_v2.json").read_text(encoding="utf-8"))
    if (
        policy.get("legacy_task_definition_source") is not None
        or policy.get("legacy_runtime_on_main") is not False
    ):
        errors.append("V2 runtime policy still exposes a legacy definition fallback")
    dispatch = (ROOT / "tools/research_dispatch.py").read_text(encoding="utf-8")
    if "FROZEN_LEGACY_BASELINE" in dispatch or "LEGACY_BARE_EVENT_REPLAY" in dispatch:
        errors.append("live dispatch still contains legacy fallback semantics")
    if "raw authenticated Issue #240 comment objects" not in dispatch:
        errors.append("live dispatch does not fail closed on bare runtime events")
    guard = (ROOT / "control_plane/research_runtime_guard_core.py").read_text(
        encoding="utf-8"
    )
    if "legacy_task_ids" in guard or "LEGACY_BASELINE_REGISTERED" in guard:
        errors.append("runtime guard still authorizes legacy registration")
    for rel in ACTIVE_PROMPTS:
        text = (ROOT / rel).read_text(encoding="utf-8")
        for name in FORBIDDEN_NAMES:
            if name in text:
                errors.append(f"active prompt {rel} still names isolated file {name}")
        if re.search(r"(?i)do not read|must not read|不要读|不得读取|禁止读取", text):
            errors.append(f"active prompt {rel} still relies on file-avoidance instructions")
    errors.extend(_check_semantic_writer())
    errors.extend(
        "semantic preservation quarantine: " + error
        for error in research_task_semantic_integrity_fault_isolation.audit(ROOT)
    )
    return errors


def main() -> int:
    errors = check()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    semantic_rows = research_task_semantic_integrity_fault_isolation.validated_quarantines(
        ROOT
    )
    semantic_open = sum(
        row["repair_state"]
        == research_task_semantic_integrity_fault_isolation.OPEN_REPAIR_STATE
        for row in semantic_rows.values()
    )
    print(
        "PASS: 27 task identities migrated; pre-V2 control files are physically isolated; "
        "live prompts are current-only; canonical writer preserves task semantics; "
        f"{semantic_open} exact semantic-preservation fault(s) are locally blocked."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
