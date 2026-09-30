#!/usr/bin/env python3
"""Recheck this transaction using the repository's actual current native tools.
No mutation. This full-checkout entry was not run by the publishing conversation;
its executed equivalent-preflight evidence is in PREFLIGHT.json.
"""
from pathlib import Path
import json
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools import research_taskbook
from control_plane import research_task_records_impl as records
TASK='RS-R11-ONE-TICK-DELAY-ATLAS-LOCAL-REPAIR-20260930'
EXPECTED='TP2-D90E968EA0178B9BD0DE'
path=ROOT/'research_tasks'/f'{TASK}.md'
meta,body=records._prepared(path,root=ROOT)
record=records.current_records(ROOT)[TASK]
assert record['publication_id']==EXPECTED, 'A different active generation must be reviewed, not silently selected'
assert record['taskbook_blob_sha1']==records.taskbook_blob(path)
assert record['parent_objective_id']==meta['parent_objective_id']
assert record['working_truth_granted'] is False
assert record['canonical_promotion_granted'] is False
for field in ('identity_lane','source_refs','dependencies','evidence_status','successor_gate'):
    assert record[field]==meta[field],field
assert not records.validate_body(body)
errors=[r for r in research_taskbook.audit_taskbook(path,root=ROOT,dispatch=True) if r['severity']=='ERROR']
assert not errors,errors
print(json.dumps({'result':'PASS','task_id':TASK,'publication_id':EXPECTED,'policy_digest':research_taskbook.policy_digest(ROOT),'scope':'native taskbook and selected immutable record; not a science test'},ensure_ascii=False,indent=2))
