"""Offline integrity replay for this 35-task snapshot, not a full native runtime audit."""
from pathlib import Path
import hashlib, json, re

P = Path(__file__).resolve().parent
ROOT = P.parents[2]
manifest = json.loads((P / "TASKSET.json").read_text())

def blob(data):
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

count = 0
for family in manifest["group_order"]:
    rows = manifest["groups"][family]["tasks"]
    assert [r[0] for r in rows] == list("ABCDE")
    for slot, publication, task_blob, record_blob in rows:
        task = manifest["task_id_format"].format(family=family, slot=slot)
        task_path = manifest["taskbook_path_format"].format(task_id=task)
        record_path = manifest["record_path_format"].format(task_id=task, publication_id=publication)
        tb = (ROOT / task_path).read_bytes()
        rb = (ROOT / record_path).read_bytes()
        assert blob(tb) == task_blob, task_path
        assert blob(rb) == record_blob, record_path
        meta = json.loads(re.search(r"<!-- ENTERPRISE_MATH_TASK_V1\s*(.*?)\s*-->", tb.decode(), re.S)[1])
        rec = json.loads(rb)
        assert meta["task_id"] == rec["task_id"] == task
        assert rec["publication_id"] == publication
        assert rec["taskbook_blob_sha1"] == "sha1:" + task_blob
        assert rec["record_state"] == "ACTIVE" and rec["claimable"] is True
        assert rec["publisher_id"] == manifest["publisher"]
        assert rec["parent_objective_id"] == manifest["parent_objective_id"]
        parts = [task, "sha1:" + task_blob, rec["publisher_id"], rec["parent_objective_id"]]
        expected = "TP2-" + hashlib.sha256("\0".join(parts).encode()).hexdigest()[:20].upper()
        assert expected == publication
        assert not rec["working_truth_granted"] and not rec["canonical_promotion_granted"]
        count += 1
assert count == manifest["task_count"] == 35
assert len(manifest["groups"]) == manifest["group_count"] == 7
print(json.dumps({"status":"PASS", "taskbooks":count, "records":count, "groups":7,
                  "scope":"Exact snapshot bytes, task-record binding and publication IDs; no live ownership or theorem validation"}))
