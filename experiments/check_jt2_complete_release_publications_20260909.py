#!/usr/bin/env python3
"""Recheck the exact JT2 publication packet using canonical repository auditors.
Run from a complete checkout: python experiments/check_jt2_complete_release_publications_20260909.py
This validates publication, not mathematics or live ownership.
"""
from pathlib import Path
import json, sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import research_taskbook as tb
from tools import research_task_records as tr

def main() -> int:
    report = json.loads((ROOT / "research_notes/EMW59A_JT2_COMPLETE_RELEASE_PREFLIGHT_20260909.json").read_text())
    errors = []
    current = tr.current_records(ROOT)
    for item in report["tasks"]:
        path = ROOT / item["taskbook_path"]
        record = json.loads((ROOT / item["record_path"]).read_text())
        meta, body = tb.split_taskbook(path.read_text())
        findings = tb.audit_taskbook(path, root=ROOT, dispatch=True)
        errors.extend(f"{item['task_id']}: {x['code']}: {x['message']}" for x in findings if x["severity"] == "ERROR")
        errors.extend(f"{item['task_id']}: {x}" for x in tr.validate_body(body))
        for field in ("task_id", "parent_objective_id", "task_lineage", "parent_task_id", "source_refs", "dependencies", "successor_gate"):
            if record.get(field) != meta.get(field):
                errors.append(f"{item['task_id']}: record/taskbook mismatch: {field}")
        if tr.taskbook_blob(path) != record["taskbook_blob_sha1"]:
            errors.append(f"{item['task_id']}: taskbook blob mismatch")
        if current.get(item["task_id"], {}).get("publication_id") != item["publication_id"]:
            errors.append(f"{item['task_id']}: publication has since changed; recover current generation")
        if record.get("working_truth_granted") is not False or record.get("canonical_promotion_granted") is not False:
            errors.append(f"{item['task_id']}: forbidden authority grant")
        if meta.get("base_state") == "BLOCKED":
            if not all(meta.get("hard_block", {}).get(k) for k in ("missing_object", "owner", "necessity", "unblock_condition")):
                errors.append(f"{item['task_id']}: incomplete BLOCKED gate")
    if errors:
        print("\n".join(errors)); return 1
    print("PASS: five current JT2 taskbooks, publication bindings and dependency gates")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
