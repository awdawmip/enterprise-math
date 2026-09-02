#!/usr/bin/env python3
"""Fail closed if the pre-V2 control surface re-enters main."""
from __future__ import annotations

import json
import re
from pathlib import Path

from control_plane import research_task_semantic_integrity_fault_isolation

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE_BRANCH = 'archive/legacy-control-plane-pre-v2-20260902'
ARCHIVE_SHA = 'ce629e24e5af59128e25af87075c6622413684e0'
LEGACY_PATHS = ['research_scheduler.json', 'tools/research_scheduler.py', 'research_task_registry.json', 'tools/research_task_registry.py', 'research_task_publication_contract.json', 'tools/check_task_registry_cutover.py', 'docs/RESEARCH_SCHEDULER.md', 'docs/RESEARCH_TASK_PUBLICATION_PROTOCOL_V1.md', 'docs/RESEARCH_SCHEDULER_NONBLOCKING_STARTUP.md']
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
    if source.get("archive_branch") != ARCHIVE_BRANCH or source.get("commit") != ARCHIVE_SHA:
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
    if policy.get("legacy_task_definition_source") is not None or policy.get("legacy_runtime_on_main") is not False:
        errors.append("V2 runtime policy still exposes a legacy definition fallback")
    dispatch = (ROOT / "tools/research_dispatch.py").read_text(encoding="utf-8")
    if "FROZEN_LEGACY_BASELINE" in dispatch or "LEGACY_BARE_EVENT_REPLAY" in dispatch:
        errors.append("live dispatch still contains legacy fallback semantics")
    if "raw authenticated Issue #240 comment objects" not in dispatch:
        errors.append("live dispatch does not fail closed on bare runtime events")
    guard = (ROOT / "control_plane/research_runtime_guard_core.py").read_text(encoding="utf-8")
    if "legacy_task_ids" in guard or "LEGACY_BASELINE_REGISTERED" in guard:
        errors.append("runtime guard still authorizes legacy registration")
    for rel in ACTIVE_PROMPTS:
        text = (ROOT / rel).read_text(encoding="utf-8")
        for name in FORBIDDEN_NAMES:
            if name in text:
                errors.append(f"active prompt {rel} still names isolated file {name}")
        if re.search(r"(?i)do not read|must not read|不要读|不得读取|禁止读取", text):
            errors.append(f"active prompt {rel} still relies on file-avoidance instructions")
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
    semantic_rows = research_task_semantic_integrity_fault_isolation.validated_quarantines(ROOT)
    semantic_open = sum(
        row["repair_state"]
        == research_task_semantic_integrity_fault_isolation.OPEN_REPAIR_STATE
        for row in semantic_rows.values()
    )
    print(
        "PASS: 27 task identities migrated; pre-V2 control files are physically isolated; "
        "live prompts are current-only; "
        f"{semantic_open} exact semantic-preservation fault(s) are locally blocked."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
