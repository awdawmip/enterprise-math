import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

OUT = Path(__file__).resolve().parent
ORIGINAL = OUT.parent
ROOT = Path('D:/em/control-assigned-gov-driver-entry-20260909')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def write(path, value): path.write_bytes((json.dumps(value,ensure_ascii=False,indent=2)+'\n').encode())
prior = json.loads(ORIGINAL.joinpath('postclaim-raw-comments.json').read_bytes())
new = json.loads(OUT.joinpath('progress-new-window-raw-comments.json').read_bytes())
merged = {int(e['id']):e for e in prior}
for event in new: merged[int(event['id'])]=event
events=sorted(merged.values(), key=lambda e:(e['created_at'],int(e['id'])))
event_path=OUT.joinpath('merged-current-raw-comments.json')
write(event_path,events)
progress=next(e for e in events if e['id']==5597593924)
assert progress['created_at']=='2026-09-09T07:00:53Z'
body=json.loads(progress['body'])
assert body['event']=='PROGRESS' and body['claim_id']=='chatgpt-jt2-driver-20260909-b35e4ba5561b4a2bb7f096b81cff6140'
host=json.loads(OUT.joinpath('host-session-observation.json').read_bytes())
assert host['session_id']==os.environ.get('CODEX_THREAD_ID')=='01a07c03-521b-7000-b312-17428b1edddf'
observations={'schema':'ENTERPRISE_MATH_SESSION_LIVENESS_OBSERVATIONS_V2','observations':[{
 'task_id':body['task_id'],'claim_id':body['claim_id'],
 'session_id':host['session_id'],'activity_evidence_kind':'DURABLE_EXECUTION_PROGRESS',
 'last_verified_activity_at':progress['created_at']}]}
obs_path=OUT.joinpath('actual-exact-task-observations.json')
write(obs_path,observations)
write(OUT.joinpath('observation-provenance.json'),{
 'scope':'Actual claimed-GOV durable frontier report; not generic Driver/chat activity or source commit time substituted for a lease.',
 'actual_host_observation':host,'actual_server_progress_id':progress['id'],'actual_server_progress_time':progress['created_at'],
 'actual_progress_ref':body['progress_ref'],'durable_source_readback_receipt_sha256':sha(OUT.joinpath('actual-publication-readbacks.json')),
 'events_window':{'old_since_inclusive':'2026-09-09T04:11:39Z','incremental_since':'2026-09-09T05:08:31Z','incremental_count':len(new),'incremental_page_less_than_100':len(new)<100,'merged_count':len(events),'last_id':events[-1]['id']},
 'no_claim_recreated':True,'no_server_timestamp_fabricated':True,
 'forward_source':'096c2fb3dd71dea4ef40940928d8d0b71c0c3304','source_overlay_not_main':True})

input_path=ORIGINAL.joinpath('authorization-input.json')
calls=[('authorize',[sys.executable,'-B','-X','utf8',str(OUT.joinpath('current_authorize_entry.py')),'authorize','--state-file',str(input_path),'--events',str(event_path)]),
       ('forward-route',[sys.executable,'-B','-X','utf8','research_control_dispatch.py','--events',str(event_path),'--kind','GOVERNANCE','--assigned-driver-task','D:/em/TEMP/assigned-gov-driver-entry-20260909/hume-forward-request.json','--session-observations',str(obs_path)])]
for name,argv in calls:
    started=datetime.datetime.now(datetime.timezone.utc).isoformat(); start=time.monotonic()
    try:
        run=subprocess.run(argv,cwd=ROOT,capture_output=True,timeout=150)
        stdout,stderr,code=run.stdout,run.stderr,run.returncode
    except subprocess.TimeoutExpired as ex:
        stdout,stderr,code=ex.stdout or b'',ex.stderr or b'',None
    elapsed=time.monotonic()-start
    out=OUT.joinpath(name+'.stdout');err=OUT.joinpath(name+'.stderr')
    out.write_bytes(stdout);err.write_bytes(stderr)
    try:result=json.loads(stdout)
    except (json.JSONDecodeError,UnicodeDecodeError):result=None
    receipt={'name':name,'argv':argv,'cwd':str(ROOT),'started_at':started,'elapsed_seconds':elapsed,'exit_code':code,'timeout_seconds':150,
             'stdout_sha256':sha(out),'stderr_sha256':sha(err),'events_sha256':sha(event_path),'state_sha256':sha(input_path),'observations_sha256':sha(obs_path),
             'control_source':'096c2fb3dd71dea4ef40940928d8d0b71c0c3304 (published source, not main)','result':result}
    write(OUT.joinpath(name+'-actual-receipt.json'),receipt)
    print(json.dumps(receipt,ensure_ascii=False),flush=True)
    if code!=0: raise SystemExit(1)
