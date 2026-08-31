#!/usr/bin/env python3
"""Standard-library checker for R049 candidate-blind frozen engineering holdout."""
from pathlib import Path
import hashlib, json, sys, re

ROOT = Path(__file__).resolve().parent.parent
REQ_ID = "EM-R049-6D82B4"
REQ_TASK = "RS-R049-CANDIDATE-BLIND-INDEPENDENT-ENGINEERING-HOLDOUT-CONSTRUCTION"
REQ_SOURCE = "cff6152a1f0e57141990b5ca2614326c3da7fbde"
REQ_FAMILIES = {
    "GEOMETRIC_MEASURE_COHERENCE",
    "CYCLE_CLOSURE_AND_RELATIVE_PHASE",
    "DIFFUSIVE_RELAXATION",
    "BOUNDED_MODE_SPECTRUM",
}
REQ_ATTACKS = {
    "SAME_PROTOCOL_NEW_SOURCE",
    "SAME_DEFINITION_DOUBLE_COUNT",
    "UNIT_CONVERSION_AS_NEW_EVIDENCE",
    "CALCULATED_OUTPUT_AS_MEASURED_OUTPUT",
    "TARGET_CHOSEN_FOR_UNKNOWN_CANDIDATE",
    "CLASSICAL_PI_NUMERIC_SELECTION",
    "BLOCK_B_RENAMED_OLD_PRESSURE",
    "TRAINING_SOURCE_REUSED_AS_HOLDOUT",
    "TOLERANCE_INVENTED_WITHOUT_SOURCE",
}
ROW_FIELDS = {
    "protocol",
    "controlled_input_or_intervention",
    "measured_output",
    "scale_regime",
    "uncertainty_tolerance_error_envelope",
    "classical_representation",
    "definition_unit_normalization_dependencies",
    "definition_stripped_operational_constraint",
    "source_provenance",
}
TARGET_FILES = [
    "R049_SOURCE_REGISTRY.json",
    "R049_RAW_ENGINEERING_ATLAS.json",
    "R049_DEPENDENCY_GRAPH.json",
    "R049_DEFINITION_STRIPPED_CONSTRAINTS.json",
    "R049_DEPENDENCY_QUOTIENT.json",
    "R049_BLOCK_A_HOLDOUT_TARGET.json",
    "R049_BLOCK_B_NOVEL_PRESSURE_LEDGER.json",
    "R049_HOLDOUT_INDEPENDENCE_CERTIFICATES.json",
    "R049_CONTAMINATION_AUDIT.json",
    "R049_ADVERSARIAL_TEST_RESULTS.json",
]

def die(msg):
    print("FAIL:", msg)
    raise SystemExit(1)

def load(name):
    try:
        return json.loads((ROOT / name).read_text(encoding="utf-8"))
    except Exception as exc:
        die(f"cannot load {name}: {exc}")

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

manifest = load("R049_HOLDOUT_MANIFEST.json")
if manifest.get("researcher_id") != REQ_ID: die("researcher id")
if manifest.get("task_id") != REQ_TASK: die("task id")
if manifest.get("taskbook_source_commit") != REQ_SOURCE: die("taskbook source")
for key, want in [("frozen", True), ("candidate_blind", True), ("block_a_complete", True),
                  ("block_b_quotiented", True), ("calibration_run", False), ("canonical", False)]:
    if manifest.get(key) is not want: die(f"manifest flag {key}")

if sorted(manifest.get("authoritative_target_files", [])) != sorted(TARGET_FILES):
    die("authoritative target file list")

expected_hashes = {name: "sha256:" + sha(ROOT / name) for name in sorted(TARGET_FILES)}
if manifest.get("artifact_hashes") != expected_hashes:
    die("artifact hash mapping mismatch")
payload = json.dumps(expected_hashes, sort_keys=True, separators=(",",":"), ensure_ascii=False).encode("utf-8")
expected_target_hash = "sha256:" + hashlib.sha256(payload).hexdigest()
if manifest.get("target_hash") != expected_target_hash:
    die("target hash mismatch")

registry = load("R049_SOURCE_REGISTRY.json")
source_ids = {s["source_id"] for s in registry.get("sources", [])}
if len(source_ids) != len(registry.get("sources", [])): die("duplicate source id")

atlas = load("R049_RAW_ENGINEERING_ATLAS.json")
rows = atlas.get("rows", [])
if len(rows) != 8: die("raw row count must be 8")
if len({r.get("protocol_fingerprint") for r in rows}) != len(rows):
    die("protocol fingerprints must be unique")
for r in rows:
    missing = ROW_FIELDS - set(r)
    if missing: die(f"{r.get('row_id')} missing fields {sorted(missing)}")
    if not r["source_provenance"]: die(f"{r.get('row_id')} has no provenance")
    if any(s not in source_ids for s in r["source_provenance"]):
        die(f"{r.get('row_id')} references unknown source")
    env = r["uncertainty_tolerance_error_envelope"]
    refs = env.get("source_ref_ids", [])
    if not refs or any(s not in source_ids for s in refs):
        die(f"{r.get('row_id')} tolerance/envelope lacks valid source reference")
    measured = json.dumps(r["measured_output"], ensure_ascii=False).lower()
    for calc in r.get("calculated_outputs_not_counted", []):
        if str(calc).strip().lower() == measured.strip():
            die(f"{r.get('row_id')} calculated output equals measured output")

a = load("R049_BLOCK_A_HOLDOUT_TARGET.json")
families = {x["family"] for x in a.get("families", [])}
if families != REQ_FAMILIES or len(a.get("families", [])) != 4:
    die("Block A family set")

q = load("R049_DEPENDENCY_QUOTIENT.json")
cands = q.get("block_b_candidates", [])
if not 2 <= len(cands) <= 4: die("Block B candidate count")
for c in cands:
    if c.get("verdict") not in {"RETAIN_NEW_INDEPENDENT_PRESSURE","KILL_DEPENDENCY_QUOTIENT"}:
        die("invalid Block B verdict")
    tests = c.get("tests", {})
    if set(tests) != {"renamed_inherited_pressure","convention_or_normalization_only","calculated_output_only","independent_operational_residual"}:
        die("Block B quotient test coverage")

cert = load("R049_HOLDOUT_INDEPENDENCE_CERTIFICATES.json")
for c in cert.get("certificates", []):
    if "row_id" in c and c["row_id"].startswith("A"):
        if len(c.get("independence_dimensions", [])) < 2:
            die(f"insufficient independence dimensions {c['row_id']}")
    if "candidate" in c and c.get("substantive_independence_count", 0) < 2:
        die(f"insufficient Block B row independence {c['candidate']}")

adv = load("R049_ADVERSARIAL_TEST_RESULTS.json")
attacks = {x["attack"] for x in adv.get("tests", [])}
if attacks != REQ_ATTACKS: die("adversarial attack coverage")
for x in adv["tests"]:
    if x["attack"] == "TRAINING_SOURCE_REUSED_AS_HOLDOUT":
        if x["verdict"] not in {"PASS","PASS_WITH_TOOLING_LIMITATION"}:
            die("training-source reuse verdict")
    elif x["verdict"] != "PASS":
        die(f"attack did not pass: {x['attack']}")

cont = load("R049_CONTAMINATION_AUDIT.json")
if cont.get("candidate_calibration_run") is not False: die("calibration contamination")
if cont.get("classical_pi_numeric_target_signal_used") is not False: die("numeric target leakage flag")
if cont.get("prior_exact_protocol_or_tolerance_rows_read_before_freeze") is not False:
    die("prior protocol leakage flag")

# Scan only target-bearing objects. Do not scan audit prose, where attack names must appear.
scan_names = [
    "R049_RAW_ENGINEERING_ATLAS.json",
    "R049_DEPENDENCY_GRAPH.json",
    "R049_DEFINITION_STRIPPED_CONSTRAINTS.json",
    "R049_DEPENDENCY_QUOTIENT.json",
    "R049_BLOCK_A_HOLDOUT_TARGET.json",
    "R049_BLOCK_B_NOVEL_PRESSURE_LEDGER.json",
    "R049_HOLDOUT_INDEPENDENCE_CERTIFICATES.json",
]
blob = "\n".join((ROOT / n).read_text(encoding="utf-8") for n in scan_names)
for pattern in [r"3\.14159", r"\bmath\.pi\b", r"candidate_hash", r"secondary_family"]:
    if re.search(pattern, blob, flags=re.IGNORECASE):
        die(f"forbidden target-bearing token matched: {pattern}")

counts = manifest.get("frozen_counts", {})
if counts.get("block_a_families") != 4 or counts.get("block_a_rows") != 4:
    die("Block A manifest counts")
if counts.get("block_b_candidates_searched") != len(cands):
    die("Block B manifest count")
if counts.get("raw_engineering_rows_total") != len(rows):
    die("atlas manifest count")
if counts.get("source_registry_entries") != len(source_ids):
    die("source manifest count")

print("PASS")
print("Researcher-ID:", REQ_ID)
print("Target-Hash:", expected_target_hash)
print("Status:", manifest["status"])
