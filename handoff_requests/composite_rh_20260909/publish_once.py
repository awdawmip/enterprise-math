#!/usr/bin/env python3
"""One-shot branch-scoped publication with unchanged canonical EM tools.
No main write, no claim, no policy override, no mathematical acceptance.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
HERE = Path(__file__).resolve().parent
OUT = ROOT / 'research_handoffs/COMPOSITE_ROAD_RH_20260909'
ACTIVITY = 'RA-C4A91D-RH-HANDOFF-20260909'
BRANCH = 'handoff/composite-rh-20260909-c4a91d'
from tools import research_taskbook, research_task_records

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def run(args: list[str], log_name: str) -> str:
    cp = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    (OUT / log_name).write_text(cp.stdout + cp.stderr, encoding='utf-8')
    if cp.returncode:
        raise RuntimeError(f'{args!r}: exit {cp.returncode}\n{cp.stdout}\n{cp.stderr}')
    return cp.stdout

def save(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def main() -> None:
    if os.environ.get('GITHUB_REF_NAME') != BRANCH:
        raise RuntimeError('Publisher restricted to its dedicated branch')
    request = json.loads((HERE / 'request.json').read_text())
    if request.get('schema') != 'COMPOSITE_RH_PUBLICATION_REQUEST_V1':
        raise RuntimeError('Invalid request schema')
    raw = (HERE / 'task_specs.json').read_bytes()
    specs = json.loads(raw)
    spec_sha = sha(raw)
    spec_blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if request.get('task_spec_git_blob_sha1') != spec_blob:
        raise RuntimeError('Request does not bind these task specifications')
    receipt_path = OUT / 'publication_receipt.json'
    if receipt_path.exists():
        old = json.loads(receipt_path.read_text())
        if old['task_spec_sha256'] != spec_sha:
            raise RuntimeError('Published specifications differ; immutable revision required')
        run([sys.executable,'tools/research_task_records.py','audit'],'record_audit.log')
        print('Verified existing publication; no task restarted')
        return
    run([sys.executable,'tools/research_task_records.py','audit'],'baseline_record_audit.log')
    current = research_task_records.current_records(ROOT)
    ids = [s['task_id'] for s in specs['tasks']]
    if any(t in current for t in ids):
        raise RuntimeError('Exact task exists; reconcile rather than republish')
    matches = []
    for tid, record in current.items():
        text = json.dumps(record, ensure_ascii=False).lower()
        if any(term in text for term in ('composite_road_rh_', 'em-free-c4a91d', 'nyman')):
            matches.append(tid)
    save(OUT/'dedup_check.json', {'current_record_count':len(current),'matching_task_ids':matches,'terms':['COMPOSITE_ROAD_RH_','EM-FREE-C4A91D','nyman'],'scope':'Current immutable publications; not a literature novelty search'})
    if matches:
        raise RuntimeError('Reconcile potentially existing route publications: '+repr(matches))
    verifier = OUT/'stage2_verify.py'
    if sha(verifier.read_bytes()) != 'df49a8cd07f84375466ff9e003ac7c96044936e5b9e5b5a73cb62165bb1ae436':
        raise RuntimeError('Frozen verifier bytes drifted')
    result=json.loads(run([sys.executable,str(verifier)],'stage2_execution.log'))
    if result.get('status') != 'EXACT_CHECK_PASS':
        raise RuntimeError('Finite certificate verification failed')
    save(OUT/'stage2_remote_recheck.json',result)
    snap=specs['source_snapshot']
    names=subprocess.check_output(['git','ls-tree','-r','--name-only',snap,'research_notes'],cwd=ROOT,text=True).splitlines()
    names=sorted(p for p in names if Path(p).name.startswith('COMPOSITE_ROAD_RH_') and p.endswith('_20260906.md'))
    if len(names)<6:
        raise RuntimeError('Missing prior road research sources')
    sources=[]
    for name in names:
        data=subprocess.check_output(['git','show',snap+':'+name],cwd=ROOT)
        blob=subprocess.check_output(['git','rev-parse',snap+':'+name],cwd=ROOT,text=True).strip()
        sources.append({'repository':'awdawmip/enterprise-math','commit':snap,'path':name,'git_blob_sha1':blob,'sha256':sha(data)})
    save(OUT/'source_manifest.json',{'schema':'COMPOSITE_RH_SOURCE_HANDOFF_V1','source_snapshot':snap,'prior_road_sources':sources,'stage2_program':{'path':verifier.relative_to(ROOT).as_posix(),'sha256':sha(verifier.read_bytes())},'stage2_full_proof':{'repository':'awdawmip/chatgpt-global-knowledge','commit':'bb649a26fd04db9bee3cf237b7c0d0311f99e7d2','path':'journal/enterprise-math/2026-09-05/20260905T073134Z-composite-residue-rh-stage2-c4a91d.md'},'acceptance':'RESEARCH_SOURCE_ONLY_NOT_INDEPENDENT_MATHEMATICAL_ACCEPTANCE'})
    save(HERE/'checkpoint_source.json',request['checkpoint_source'])
    save(HERE/'activity_registration_source.json',request['activity_registration_source'])
    run([sys.executable,'tools/research_activity.py','guard','--activity-id',ACTIVITY,'--session-id','local-chat-c4a91d-rh-handoff-20260909','--boundary','startup','--registration-json',str(HERE/'activity_registration_source.json')],'activity_startup_guard.json')
    pubs=[]
    for s in specs['tasks']:
        path=ROOT/'research_tasks'/(s['task_id']+'.md')
        if path.exists():
            raise RuntimeError('Refusing to overwrite '+str(path))
        meta={'task_id':s['task_id'],'title':s['title'],'kind':'RESEARCH','owner':'taskbook/unassigned','base_state':'DRAFT','priority':'P2','leverage':'MEDIUM','frontier':s['frontier'],'next_action':s['next_action'],'dependencies':s['dependencies'],'source_refs':['research_handoffs/COMPOSITE_ROAD_RH_20260909/START_HERE.md','research_handoffs/COMPOSITE_ROAD_RH_20260909/source_manifest.json','research_handoffs/COMPOSITE_ROAD_RH_20260909/stage2_verify.py']+names,'evidence_status':'RESEARCH_DERIVATIONS_PENDING_INDEPENDENT_AUDIT_WITH_REPRODUCED_FINITE_CERTIFICATES','last_progress_ref':None,'last_progress_at':None,'hard_block':None,'tags':['RH','composite-road','full-integer-population','signed-phase','source-handoff'],'claim_lease_minutes':120,'created_by_role':'RESEARCHER','task_authority':'PENDING_PUBLICATION','publication_contract':'RESEARCH_TASK_PUBLICATION_V1','publication_template':'RESEARCH_TASK_PUBLICATION_TEMPLATE_V1','registry_key':s['task_id'],'parent_objective_id':specs['parent_objective_id'],'identity_policy':'AUTO_RESOLVE_OR_ALLOCATE','final_response_identity_policy':'INHERIT_GLOBAL','identity_lane':'RH-ROAD','origin_kind':'DIRECT_USER_DIRECTION','task_lineage':s['task_lineage'],'parent_task_id':s['parent_task_id'],'successor_gate':s['successor_gate'],'origin_research_provenance':'EM-FREE-C4A91D; user-selected classical arithmetic research; ANCHOR_EXPOSED; no raw axiom candidate promoted','policy_review':{'policy_set':'research_taskbook_policy.json','review_state':'PENDING_POLICY_REVIEW','temporary_overrides':[]}}
        path.parent.mkdir(exist_ok=True)
        path.write_text(research_taskbook.render_taskbook(meta,s['body']),encoding='utf-8')
        rel=path.relative_to(ROOT).as_posix()
        run([sys.executable,'tools/research_task_records.py','prepare','--taskbook',rel,'--publisher-role','RESEARCHER','--parent-objective-id',specs['parent_objective_id']],s['task_id']+'_prepare.json')
        run([sys.executable,'tools/research_taskbook.py','audit',rel],s['task_id']+'_audit.log')
        pub=json.loads(run([sys.executable,'tools/research_task_records.py','publish','--taskbook',rel,'--publisher-role','RESEARCHER','--publisher-id',specs['publisher_id'],'--research-value',s['research_value']],s['task_id']+'_publication.json'))
        pubs.append(pub)
    run([sys.executable,'tools/research_task_records.py','audit'],'record_audit.log')
    after=research_task_records.current_records(ROOT)
    for pub in pubs:
        rec=after[pub['task_id']]
        if rec['publication_id'] != pub['publication_id']:
            raise RuntimeError('Publication is not unique current generation')
        if rec['taskbook_blob_sha1'] != research_task_records.taskbook_blob(ROOT/rec['taskbook_path']):
            raise RuntimeError('Taskbook binding mismatch')
        for field in ('working_truth_granted','canonical_promotion_granted'):
            if rec[field] is not False:
                raise RuntimeError('Unexpected theorem authority')
    ap=ROOT/'research_activity_records'/f'{ACTIVITY}.json'
    run([sys.executable,'tools/research_activity.py','checkpoint','--activity-id',ACTIVITY,'--event-id','RH-ROAD-HANDOFF-SOURCE-20260909','--expected-sha256',sha(ap.read_bytes()),'--source-json',str(HERE/'checkpoint_source.json')],'activity_checkpoint.json')
    save(receipt_path,{'schema':'COMPOSITE_RH_CANONICAL_PUBLICATION_RECEIPT_V1','observed_at':datetime.now(timezone.utc).isoformat(),'request_id':request['request_id'],'execution_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'task_spec_sha256':spec_sha,'canonical_policy_digest':research_taskbook.policy_digest(ROOT),'canonical_tools_used':['tools/research_task_records.py prepare','tools/research_taskbook.py audit','tools/research_task_records.py publish','tools/research_task_records.py audit','tools/research_activity.py guard','tools/research_activity.py checkpoint'],'record_audit':'PASS','source_file_count':len(sources),'finite_certificate_recheck':'EXACT_CHECK_PASS','activity_id':ACTIVITY,'publications':pubs,'scope':'Validated on the dedicated branch; main visibility requires non-forced integration and immutable readback. No CLAIM issued; dependencies remain operative.','working_truth_granted':False,'canonical_promotion_granted':False})
    print(json.dumps({'status':'PUBLICATION_SET_VALIDATED','task_ids':ids,'receipt':receipt_path.relative_to(ROOT).as_posix()},ensure_ascii=False))

if __name__=='__main__':
    main()
