#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASK = "RS-R037-R033-R034-INDEPENDENT-ALGORITHM-DATA-REPLICATION-AUDIT"
PUB = "TP2-FEE5990D460CCB106345"
SOURCE_COMMIT = "ce629e24e5af59128e25af87075c6622413684e0"
PUB_PATH = ROOT / f"research_task_records/{TASK}/{PUB}.json"
TASKBOOK_PATH = ROOT / "research_tasks/LEGACY_CONTROL_MIGRATION_RS_R037_R033_R034_INDEPENDENT_ALGORITHM_DATA_REPLICATION_AUDIT_20260902.md"
HIST_PATH = "research_tasks/R037_R033_R034_INDEPENDENT_ALGORITHM_DATA_REPLICATION_AUDIT_20260812.md"
MANIFEST_PATH = ROOT / "control_plane/legacy_control_migration_manifest.json"
CERT_PATH = ROOT / "research_artifacts/R037_R033_R034_V2_PRESERVATION_AUDIT/preservation_certificate_20260902.json"

def load(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))

def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def embedded_task(text: str):
    m = re.search(r"<!--\s*ENTERPRISE_MATH_TASK_V1\s*(\{.*?\})\s*-->", text, re.S)
    if not m:
        raise AssertionError("missing ENTERPRISE_MATH_TASK_V1 block")
    return json.loads(m.group(1))

def find_task(obj):
    out = []
    def walk(x):
        if isinstance(x, dict):
            if x.get("task_id") == TASK:
                out.append(x)
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(obj)
    defs = [x for x in out if "frontier" in x and "owner" in x and "priority" in x]
    if not defs:
        raise AssertionError("legacy scheduler task definition not found")
    return defs[0]

def find_manifest_row(obj):
    out = []
    def walk(x):
        if isinstance(x, dict):
            if x.get("task_id") == TASK and x.get("publication_id") == PUB:
                out.append(x)
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(obj)
    if not out:
        raise AssertionError("migration manifest row not found")
    return out[0]

pub = load(PUB_PATH)
manifest = load(MANIFEST_PATH)
cert = load(CERT_PATH)
taskbook_bytes = TASKBOOK_PATH.read_bytes()
v2 = embedded_task(taskbook_bytes.decode("utf-8"))

legacy_scheduler = json.loads(subprocess.check_output(
    ["git", "show", f"{SOURCE_COMMIT}:research_scheduler.json"],
    cwd=ROOT, text=True
))
legacy = find_task(legacy_scheduler)
hist_text = subprocess.check_output(
    ["git", "show", f"{SOURCE_COMMIT}:{HIST_PATH}"],
    cwd=ROOT, text=True
)
hist = embedded_task(hist_text)
row = find_manifest_row(manifest)

assert pub["record_schema"] == "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2"
assert pub["record_state"] == "ACTIVE"
assert pub["task_id"] == TASK and pub["publication_id"] == PUB
assert pub["claimable"] is True
assert pub["owner"] == legacy["owner"] == v2["owner"] == cert["current_v2"]["owner"]
assert pub["effective_priority"] == legacy["priority"] == v2["priority"] == "P0"
assert pub["effective_leverage"] == legacy["leverage"] == v2["leverage"] == "HIGH"
assert pub["frontier"] == legacy["frontier"] == v2["frontier"] == cert["current_v2"]["frontier"]
assert pub["next_action"] == v2["next_action"] == cert["authenticated_runtime_overlay"]["next_action"]
assert v2["base_state"] == row["legacy_runtime_state"] == pub["migration_source"]["legacy_runtime_state"] == "HANDOFF_READY"
assert pub["migration_source"]["source_commit"] == SOURCE_COMMIT
assert pub["migration_source"]["source_definition"] == "research_scheduler.json"
assert pub["migration_source"]["legacy_last_progress_ref"] == v2["last_progress_ref"] == cert["authenticated_runtime_overlay"]["progress_ref"]
assert pub["migration_source"]["legacy_last_progress_at"] == v2["last_progress_at"] == "2026-08-28T15:52:42+00:00"
assert pub["migration_source"]["no_execution_claim_created"] is True

actual_taskbook_blob = "sha1:" + git_blob_sha1(taskbook_bytes)
assert actual_taskbook_blob == pub["taskbook_blob_sha1"] == cert["current_v2"]["taskbook_blob_sha1"]

assert row["disposition"] == "ACTIVE_FRONTIER"
assert row["record_state"] == "ACTIVE" and row["claimable"] is True
assert row["record_path"] == cert["migration_manifest"]["row"]["record_path"]
assert row["taskbook_path"] == pub["taskbook_path"] == cert["migration_manifest"]["row"]["taskbook_path"]

assert [d["target"] for d in hist["dependencies"]] == [d["target"] for d in v2["dependencies"]]
assert [d["satisfied"] for d in hist["dependencies"]] == [d["satisfied"] for d in v2["dependencies"]] == [True, True]
assert [d["action"] for d in hist["dependencies"]] == [
    "TEST_FROZEN_INTRINSIC_GRAPH_SPHERE_RESULTS",
    "TEST_FROZEN_PROPAGATION_SPHERE_RESULTS",
]
assert [d["action"] for d in v2["dependencies"]] == ["TEST", "TEST"]
assert hist["claim_lease_minutes"] == 1440 and v2["claim_lease_minutes"] == 120

assert all(a["status"] in {"PASS", "PASS_WITH_CAVEAT"} for a in cert["assertions"])
assert cert["verdict"] == "V2_PRESERVATION_CONFIRMED_AT_CUTOVER_SEMANTICS_WITH_NONBLOCKING_HISTORICAL_NORMALIZATION_CAVEAT"

print("PASS R037 V2 preservation: cutover identity/owner/P0-HIGH/frontier exact; "
      "authenticated HANDOFF overlay preserved; synthetic cutover claim=false; "
      "historical normalization caveat pinned.")
