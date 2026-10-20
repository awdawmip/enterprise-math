#!/usr/bin/env python3
"""Focused checker for the R037 immutable-V2 preservation / redispatch audit."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASK_ID = "RS-R037-R033-R034-INDEPENDENT-ALGORITHM-DATA-REPLICATION-AUDIT"
PUBLICATION_ID = "TP2-FEE5990D460CCB106345"

record_path = (
    ROOT
    / "research_task_records"
    / TASK_ID
    / f"{PUBLICATION_ID}.json"
)
taskbook_path = (
    ROOT
    / "research_tasks"
    / "LEGACY_CONTROL_MIGRATION_RS_R037_R033_R034_INDEPENDENT_ALGORITHM_DATA_REPLICATION_AUDIT_20260902.md"
)
policy_path = ROOT / "research_runtime_policy_v2.json"
reducer_path = ROOT / "tools" / "research_runtime_reducer.py"
audit_path = (
    ROOT
    / "research_artifacts"
    / "R037_R033_R034_V2_PRESERVATION_AUDIT"
    / "AUDIT_MATRIX.json"
)

record = json.loads(record_path.read_text(encoding="utf-8"))
taskbook = taskbook_path.read_text(encoding="utf-8")
policy = json.loads(policy_path.read_text(encoding="utf-8"))
reducer = reducer_path.read_text(encoding="utf-8")
audit = json.loads(audit_path.read_text(encoding="utf-8"))

match = re.search(
    r"<!--\s*ENTERPRISE_MATH_TASK_V1\s*(\{.*?\})\s*-->",
    taskbook,
    flags=re.DOTALL,
)
assert match, "taskbook metadata envelope missing"
meta = json.loads(match.group(1))

assert record["task_id"] == TASK_ID
assert record["publication_id"] == PUBLICATION_ID
assert record["kind"] == "RESEARCH"
assert record["owner"] == "program/p022-geometry-v2"
assert record["claimable"] is True
assert record["effective_priority"] == "P0"
assert record["effective_leverage"] == "HIGH"
assert record["working_truth_granted"] is False
assert record["canonical_promotion_granted"] is False

assert meta["task_id"] == TASK_ID
assert meta["base_state"] == "HANDOFF_READY"
assert meta["priority"] == "P0"
assert meta["leverage"] == "HIGH"
assert meta["claim_lease_minutes"] == 120
assert "Driver review PR #812" in meta["next_action"]
assert "without replaying completed work" in taskbook
assert "Mathematical execution and review remain separate actions." in taskbook

selection = policy["selection_policy"]
assert selection["state_order"][0] == "HANDOFF_READY"
assert '"READY", "HANDOFF_READY"' in reducer
assert 'state["dispatch_state"] = "NEEDS_DISPATCH"' in reducer
assert 'value.get("dispatch_state") == "NEEDS_DISPATCH"' in reducer

rows = {row["check"]: row for row in audit["matrix"]}
assert rows["TASK_IDENTITY_AND_OWNER"]["result"] == "PASS"
assert rows["PROVENANCE_CAVEAT_PRESERVATION"]["result"] == "PASS"
assert rows["TRUTH_AUTHORITY_BACKFLOW"]["result"] == "PASS"
assert rows["RUNTIME_RESULT_OVERLAY_AT_CLAIM_BASE"]["result"] == "FAIL_CONTROL_GAP"
assert rows["DISPATCH_SEMANTICS"]["result"] == "FAIL_CONTROL_GAP"
assert rows["OBSERVED_REDISPATCH"]["result"] == "REPRODUCED_EXACT"

verdict = audit["verdict"]
assert verdict["mathematical_meaning_preserved"] is True
assert verdict["durable_handoff_boundary_preserved"] is True
assert verdict["truth_status_not_upgraded"] is True
assert verdict["runtime_dispatch_semantics_safe"] is False
assert verdict["terminal_label"] == "PRESERVATION_PASS_WITH_RUNTIME_DISPATCH_GAP"

print("PASS: R037 V2 preservation is mathematically faithful but runtime redispatch safety fails.")
