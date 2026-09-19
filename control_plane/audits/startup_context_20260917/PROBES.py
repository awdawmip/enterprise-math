"""Read-only probes of the exact pinned upstream packet builder; no remote writes.
Findings are observations, not newly granted routing/execution authority.
"""
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, json, sys, tempfile
from pathlib import Path

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--repo-root',type=Path,default=Path(__file__).resolve().parent/'snapshot')
parser.add_argument('--out',type=Path,default=Path.cwd()/'probe_results.json')
args=parser.parse_args()
BASE=Path(__file__).resolve().parent
ROOT=args.repo_root.resolve()
for rel,expected in {
    'control_plane/researcher_startup_packet.py':'f987bd676b07abc2d57ffeda1bd22aae31515108',
    'tests/test_researcher_startup_packet.py':'329bbd7c5f7e207004616705e14bd278a4d37894',
}.items():
    data=(ROOT/rel).read_bytes()
    actual=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if actual!=expected:raise RuntimeError('Source drift: '+rel)
sys.path.insert(0,str(ROOT))
from control_plane import researcher_startup_packet as m
spec=importlib.util.spec_from_file_location('upstream_tests',ROOT/'tests/test_researcher_startup_packet.py')
tests=importlib.util.module_from_spec(spec);spec.loader.exec_module(tests)
rows=[]

def run(name,kind,fn):
    case=tests.ResearcherStartupPacketTests()
    try:
        root,receipt=case.make_root()
        result=fn(root,receipt)
        rows.append({'name':name,'kind':kind,'status':'OBSERVED','result':result})
    finally:
        case.doCleanups()

def rewrite_meta(root,changes,body_extra=''):
    book=root/'research_tasks/T1.md'; text=book.read_text()
    meta=m._task_metadata(text); meta.update(changes)
    text=m.TASK_FRONTMATTER.sub(lambda _: '<!-- ENTERPRISE_MATH_TASK_V1\n'+json.dumps(meta)+'\n-->',text)+body_extra
    book.write_text(text)
    pp=root/'research_task_records/T1/P1.json';p=json.loads(pp.read_text());p['taskbook_blob_sha1']=m._git_blob_sha1(book.read_bytes());pp.write_text(json.dumps(p));return p

def ordinary(root,r):
    p=m.build_packet(r,root); n=len(m._serialized_packet(p));assert n==p['packet_bytes'] and n<=8192
    return {'packet_bytes':n,'projection_mode':p['task']['projection_mode']}
run('ordinary_packet','POSITIVE',ordinary)

def large(root,r):
    rewrite_meta(root,{},'\n## Frozen inputs and scope\n'+('exact frozen input; '*10000))
    p=m.build_packet(r,root); b=(root/p['task']['taskbook_path']).stat().st_size
    assert p['task']['projection'] is None and p['packet_bytes']<=8192 and b>81920
    return {'packet_bytes':p['packet_bytes'],'fallback_taskbook_bytes':b,'combined_minimum_bytes':b+p['packet_bytes'],'whole_startup_80KiB_enforced_by_builder':False}
run('oversize_taskbook_is_outside_packet_budget','COVERAGE_GAP',large)

def absent(root,r):
    rewrite_meta(root,{'last_progress_ref':None,'dependencies':[],'source_refs':[]})
    oldglob=Path.glob;oldrglob=Path.rglob
    def forbidden(*a,**kw):raise AssertionError('unexpected directory scan')
    Path.glob=forbidden;Path.rglob=forbidden
    try:p=m.build_packet(r,root)
    finally:Path.glob=oldglob;Path.rglob=oldrglob
    assert p['read_plan']['first_dependency_ref'] is None
    return {'first_dependency_ref':None,'directory_enumeration':False}
run('unknown_dependency_does_not_enumerate','POSITIVE',absent)

def string_dep(root,r):
    rewrite_meta(root,{'last_progress_ref':None,'dependencies':['research_returns/R1.md'],'source_refs':[]})
    p=m.build_packet(r,root);assert p['read_plan']['first_dependency_ref'] is None
    return {'existing_dependency':'research_returns/R1.md','returned':None}
run('existing_string_dependency_is_omitted','CONFIRMED_PROJECTION_GAP',string_dep)

def string_pin(root,r):
    rewrite_meta(root,{'last_progress_ref':None,'dependencies':['research_returns/R1.md@main'],'source_refs':[]})
    p=m.build_packet(r,root);assert p['read_plan']['first_dependency_ref'] is None
    return {'declared_dependency':'research_returns/R1.md@main','returned':None}
run('existing_ref_suffixed_string_dependency_is_omitted','CONFIRMED_PROJECTION_GAP',string_pin)

def dict_dep(root,r):
    rewrite_meta(root,{'last_progress_ref':None,'dependencies':[{'path':'research_returns/R1.md','satisfied':False}],'source_refs':[]})
    p=m.build_packet(r,root);assert p['read_plan']['first_dependency_ref']=='research_returns/R1.md'
    return {'returned':p['read_plan']['first_dependency_ref']}
run('dictionary_dependency_positive_control','POSITIVE',dict_dep)

def live_frontier(root,r):
    (root/'research_returns/R2.md').write_text('new progress\n')
    r['route'].update(action='ADOPT_OWNER_CLAIM',required_guard='tools/research_runtime_guard.py adopt')
    r['route']['target'].update(last_progress_ref='research_returns/R2.md',claim_id='C1',researcher_id='EM-T1-ABCD')
    p=m.build_packet(r,root);assert p['read_plan']['first_dependency_ref']=='research_returns/R1.md'
    assert 'last_progress_ref' not in p['task'] and 'required_guard' not in p
    return {'current_target_frontier':'research_returns/R2.md','packet_first_dependency':p['read_plan']['first_dependency_ref'],'guard_preserved':False,'current_frontier_ref_preserved':False}
run('live_frontier_and_adoption_guard_are_omitted','CONFIRMED_PROJECTION_GAP',live_frontier)

def liveness(root,r):
    r['route']={'action':'VERIFY_SESSION_LIVENESS','owner_claim_preserved':True,'new_claim_required':False,'targets':[{'target_key':'T1','surface':'ORDINARY_TASK','task_id':'T1','execution_cohort_id':None,'execution_lane_id':None,'claim_id':'C1','owner_lease_until':'2026-09-17T18:00:00Z'}],'reason':'exact-owner liveness unknown'}
    p=m.build_packet(r,root);assert p['task'] is None and 'targets' not in p
    return {'input_target_count':1,'output_task':p['task'],'output_targets_present':False,'packet_bytes':p['packet_bytes']}
run('canonical_liveness_targets_are_lost','CONFIRMED_PROJECTION_GAP',liveness)

def lane(root,r):
    r['route'].update(surface='COHORT_LANE',target_key='T1::CO1::L1')
    r['route']['target'].update(execution_cohort_id='CO1',execution_lane_id='L1',output_prefix='research_notes/lane1/')
    p=m.build_packet(r,root)
    lost=[k for k in ('execution_cohort_id','execution_lane_id','output_prefix') if k not in p['task']]
    assert len(lost)==3 and 'surface' not in p and 'target_key' not in p
    return {'lost_target_fields':lost,'lost_route_fields':['surface','target_key']}
run('canonical_cohort_lane_scope_is_lost','CONFIRMED_PROJECTION_GAP',lane)

def bulk_exclusion(root,r):
    for k in ('quarantined_tasks','ignored_events','research_activity_overview'):r['route'][k]=['bulky private diagnostic'*1000]
    p=m.build_packet(r,root);assert all(k not in p for k in ('quarantined_tasks','ignored_events','research_activity_overview'))
    return {'packet_bytes':p['packet_bytes'],'bulk_top_level_fields_excluded':True}
run('bulk_diagnostic_fields_are_excluded','POSITIVE',bulk_exclusion)

def fixed_overflow(root,r):
    r['route']['target']['frontier']='x'*10000
    try:m.build_packet(r,root)
    except m.StartupPacketError as e:return {'rejected':True,'error':str(e)}
    raise AssertionError('oversized fixed field accepted')
run('oversize_nonprojection_fields_fail_closed','POSITIVE',fixed_overflow)

def utf8(root,r):
    r['route']['reason']='这是中文测试'*20;p=m.build_packet(r,root)
    assert p['packet_bytes']==len(m._serialized_packet(p))
    return {'utf8_bytes_match':True,'packet_bytes':p['packet_bytes']}
run('actual_serialized_utf8_size_is_checked','POSITIVE',utf8)

output={'source_repository':'awdawmip/enterprise-math','source_commit':'0db088a3b5793269ddcdd15a3d9a7996d3f9fff3','source_blob':'f987bd676b07abc2d57ffeda1bd22aae31515108','scope':'Exact upstream packet builder executed on isolated fixtures. Not a live dispatch/claim or whole-repository authorization audit.','probe_count':len(rows),'probes':rows}
args.out.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(output,ensure_ascii=False,indent=2))
