#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

TASK_ID = "RS-NATIVE-FILAMENT-COUPLED-SELECTION-EXTERNAL-NOVELTY-INDEPENDENT-REEXECUTION"
PUBLICATION_ID = "TP2-9568CDEA1071463F9532"

ORIGINAL_TASKBOOK = Path("research_tasks/NATIVE_FILAMENT_COUPLED_SELECTION_EXTERNAL_NOVELTY_INDEPENDENT_REEXECUTION_20260825.md")
V2_TASKBOOK = Path("research_tasks/LEGACY_CONTROL_MIGRATION_RS_NATIVE_FILAMENT_COUPLED_SELECTION_EXTERNAL_NOVELTY_INDEPENDENT_REEXECUTION_20260902.md")
PUBLICATION = Path(f"research_task_records/{TASK_ID}/{PUBLICATION_ID}.json")
MANIFEST = Path("control_plane/legacy_control_migration_manifest.json")

PINNED_BLIND_REVIEW = (
    "driver_reviews/NATIVE_FILAMENT_COUPLED_SELECTION_INDEPENDENT_AUDIT_DRIVER_REVIEW_20260825.md"
    "@d4e3f8eca68bff1d8803b8eb74402fc6d69e7b5f"
)


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def task_meta(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    marker = "<!-- ENTERPRISE_MATH_TASK_V1"
    if marker not in text:
        fail(f"missing metadata marker: {path}")
    start = text.index(marker) + len(marker)
    end = text.index("-->", start)
    return json.loads(text[start:end].strip())


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    raw = b"blob " + str(len(data)).encode("ascii") + b"\0" + data
    return "sha1:" + hashlib.sha1(raw).hexdigest()


legacy = task_meta(ORIGINAL_TASKBOOK)
v2 = task_meta(V2_TASKBOOK)
publication = json.loads(PUBLICATION.read_text(encoding="utf-8"))
manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

# Immutable binding and unique manifest row.
if publication["task_id"] != TASK_ID or publication["publication_id"] != PUBLICATION_ID:
    fail("publication identity mismatch")
if publication["taskbook_path"] != str(V2_TASKBOOK):
    fail("publication taskbook path mismatch")
if publication["taskbook_blob_sha1"] != git_blob_sha1(V2_TASKBOOK):
    fail("publication taskbook blob pin mismatch")

rows = [row for row in manifest["tasks"] if row.get("task_id") == TASK_ID]
if len(rows) != 1:
    fail(f"expected one manifest row, got {len(rows)}")
row = rows[0]
expected_manifest = {
    "disposition": "ACTIVE_FRONTIER",
    "publication_id": PUBLICATION_ID,
    "record_state": "ACTIVE",
    "claimable": True,
    "legacy_runtime_state": "HANDOFF_READY",
}
for key, expected in expected_manifest.items():
    if row.get(key) != expected:
        fail(f"manifest {key}: expected {expected!r}, got {row.get(key)!r}")

# Core mathematical/task-owner invariants are preserved.
for key in ("task_id", "kind", "owner", "priority", "leverage", "frontier"):
    if legacy.get(key) != v2.get(key):
        fail(f"core preservation mismatch at {key}: {legacy.get(key)!r} != {v2.get(key)!r}")

if publication["frontier"] != legacy["frontier"]:
    fail("publication frontier drift")
if publication["owner"] != legacy["owner"]:
    fail("publication owner drift")
if publication["effective_priority"] != legacy["priority"]:
    fail("priority drift")
if publication["effective_leverage"] != legacy["leverage"]:
    fail("leverage drift")
if publication["migration_source"]["legacy_runtime_state"] != "HANDOFF_READY":
    fail("durable runtime state not preserved as HANDOFF_READY")

# The result being checked is a NEGATIVE BOUNDARY: exact lineage/provenance
# preservation must be demonstrably false on the frozen bytes.
expected_drifts = {
    "identity_lane": ("NFNOV2", "NATIVE"),
    "origin_kind": ("DIRECT_USER_DIRECTION", "MAINTENANCE"),
    "task_lineage": ("CONTINUATION", "MAINTENANCE"),
    "parent_task_id": (
        "RS-NATIVE-FILAMENT-COUPLED-SELECTION-EXTERNAL-NOVELTY-AUDIT",
        None,
    ),
}
for key, (old, new) in expected_drifts.items():
    if legacy.get(key) != old:
        fail(f"legacy witness changed at {key}: {legacy.get(key)!r}")
    if v2.get(key) != new:
        fail(f"V2 witness changed at {key}: {v2.get(key)!r}")

if "successor_gate" not in legacy:
    fail("legacy continuation successor_gate unexpectedly absent")
required_gate = {
    "new_information_gap",
    "why_parent_result_does_not_close_it",
    "discriminating_outcomes",
    "kill_condition",
    "alternative_route_or_free_exploration_considered",
    "why_new_stage_or_task_is_better_than_same_task_or_closure",
}
if set(legacy["successor_gate"]) != required_gate:
    fail("legacy successor_gate is not the expected complete six-part gate")
if v2.get("successor_gate") is not None:
    fail("expected V2 successor_gate to be absent for the frozen counterexample")

if PINNED_BLIND_REVIEW not in legacy.get("source_refs", []):
    fail("legacy pinned blind-review ref missing")
if PINNED_BLIND_REVIEW in v2.get("source_refs", []):
    fail("expected exact source-ref drift witness is no longer present")

print(
    "PASS: core frontier/owner/P0-HIGH and durable HANDOFF state are preserved; "
    "exact identity-lineage-provenance preservation is refuted by frozen field witnesses."
)
