"""Invoke the current canonical reducer on this task's actual server events."""
import datetime, hashlib, json, sys, time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT))
from control_plane import research_control_bootstrap
research_control_bootstrap.install(ROOT)
from tools import research_dispatch, research_runtime_reducer
from control_plane import research_runtime_guard_core
raw_path=Path(sys.argv[1])
output_path=Path(sys.argv[2])
started=datetime.datetime.now(datetime.timezone.utc)
tick=time.monotonic()
task=research_runtime_guard_core._registered_definition("RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT",ROOT)
events=research_dispatch.load_events(raw_path)
authenticated,authentication_ignored=research_dispatch._event_authentication_filter(task,events)
filtered,registration_ignored=research_dispatch._filter_registered_events(task,authenticated,ROOT)
state=research_runtime_reducer.reduce_task(task,filtered,default_lease_minutes=int(task["claim_lease_minutes"]),now=datetime.datetime.now(datetime.timezone.utc))
receipt={"schema":"JT2_UR_ACTUAL_HANDOFF_REDUCER_RECEIPT_V1","actual_source_root":"52775e4f53b4a34210341f7ac07f7c6c2d3834df","entrypoint":"unchanged canonical bootstrap -> registered_definition -> load_events -> authenticated filter -> registered filter -> reduce_task","started_at":started.isoformat(),"elapsed_seconds":time.monotonic()-tick,"raw_count":len(json.loads(raw_path.read_bytes())),"raw_sha256":hashlib.sha256(raw_path.read_bytes()).hexdigest(),"authentication_ignored":authentication_ignored,"registration_ignored":registration_ignored,"state":state}
output_path.write_bytes((json.dumps(receipt,ensure_ascii=False,indent=2)+"\n").encode())
print(json.dumps({"state":state.get("state"),"dispatch_state":state.get("dispatch_state"),"claim_id":state.get("claim_id"),"lease_until":state.get("lease_until"),"result_id":state.get("result_id"),"ignored_events":state.get("ignored_events"),"raw_count":receipt["raw_count"]},ensure_ascii=True))

