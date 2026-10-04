from pathlib import Path
import json, hashlib, re, datetime, copy, shutil
import sys
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[2]
BASE='937aea6bbb6a774d7165a9d8e782940f47248fc4'
OBJ='OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS'
GEN='OG-7AE66316D7566C519AE0'
PREFIX='research_inputs/fermat_residual_20261004'
PUBLISHER='EM-DIRECT-BE4AEF'
MANIFEST=[
('research_taskbook_policy.json','c326d6eed8f89f0c7be3e0a767ccbfbcdf972358'),
('AGENTS.md','3263b74a0ef8550b045cd8a32b2947f42327bb46'),
('FOUNDATIONAL_LOGIC.md','f089400136341efbf10a5e24e8f0729800b942cd'),
('foundational_logic.json','6875d84746ee369ea222fd32bdcd92206c2db9b2'),
('docs/GITHUB_INTERACTION_BUDGET.md','4e63cf335107e6a2c43e07e8144b40f66c3fc9bb'),
('docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md','538ab28305bfe7d1d1fb4650ff634474f6649826'),
('docs/RESEARCH_ARCHITECTURE.md','81abba617ee575ab770b7736de4caa9c40bea9e5'),
('docs/RESEARCH_RUNTIME_STATE_MACHINE.md','a2d626a7159291c4e1d60b3ed459aeb3457a3a43'),
('docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md','819b4d54038bd943c998f3de0861c9f729bd1457'),
('research_architecture.json','bc016f1ef9c7b1dec202f530e6a13d4419e64fe0'),
('research_runtime_state_machine.json','56927bf8ec00a0bcfd111517712039b8db94e9d4'),
('research_task_publication_contract_v2.json','2e1d24d80dca16f54542241cae57e237d667aa41'),
('templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json','1593a79ede875d5498c8fe4e08d908bd30c6c138'),
('research_axiom_candidate_state_machine.json','56f0a6a009ca01c8b09cb5b7682b5d17946fb9ef'),
('research_role_policy.json','b868febb218c6a7ed4373cc3edd25d59636d2850'),
('research_identity_state_machine.json','775fcdfb2f764de7b1583081f6332b2c5bea9af6'),
('active_turn_liveness.json','ae481f92648792313465b77bccf59074b2c28145'),
('final_response_identity_policy.json','6dd37111cc5085de5dc59beb5a93313f5f1ceabd'),
('research_taskbook_contract.json','8bf4183eb46c18ba4e2aef913b7b0f57e6bb490d'),
('tool_invocation_policy.json','7c11ccc90f2dcfed61444cfe97fe89d5d117aa26'),
('native_semantics_admissibility.json','689b039410d1a5f2ee404edc9a9b5819cb682349')]
h=hashlib.sha256()
for rel, sha in MANIFEST:
    h.update(rel.encode()); h.update(b'\0'); h.update(bytes.fromhex(sha)); h.update(b'\0')
DIGEST='sha256:'+h.hexdigest()
SECTIONS=['Mother question','Frozen inputs and scope','Hard target and required outputs','Research value to preserve','Success, kill, and return criteria']
PATTERNS={
'TB-REMOTE-RUNTIME':[r'github actions',r'\bworkflow(?:s)?\b',r'\bremote validation\b',r'\bpull request\b',r'\bdraft pr\b',r'\bpush\b',r'\bpoll(?:ing)?\b',r'\bwait(?:ing)? for ci\b',r'\bcheck(?:ing)? ci\b',r'\bready for review\b',r'\bmoving main\b',r'\breconcil(?:e|ing).*main\b'],
'TB-SCHEDULER-RUNTIME':[r'\bissue #240\b',r'\bscheduler\b',r'\bheartbeat\b',r'\bclaim event\b'],
'TB-PROMOTION-RUNTIME':[r'\bcanonical promotion\b',r'\bl4 promotion\b',r'\bmerge(?: the| this)? pr\b'],
'TB-RESTATE-REMOTE':[r'ci_not_required_for_research',r'\bremote_silent\b',r'research is the hot path',r'github is a sparse persistence'],
'TB-RESTATE-IDENTITY':[r'no fixed researcher-id',r'do not wait for the driver to assign an id'],
'TB-RESTATE-SUCCESSOR-GATE':[r'pass is not a successor trigger',r'stage pass does not imply successor',r'successor-stage gate']}
REQUIRED={'created_by_role':None,'task_authority':'PUBLISHED_REGISTERED','publication_contract':'RESEARCH_TASK_PUBLICATION_V1','publication_template':'RESEARCH_TASK_PUBLICATION_TEMPLATE_V1','registry_key':None,'parent_objective_id':None,'identity_policy':'AUTO_RESOLVE_OR_ALLOCATE','final_response_identity_policy':'INHERIT_GLOBAL','origin_kind':None,'policy_review':None}
GATE=['new_information_gap','why_parent_result_does_not_close_it','discriminating_outcomes','kill_condition','alternative_route_or_free_exploration_considered','why_new_stage_or_task_is_better_than_same_task_or_closure']

def blob(data): return 'sha1:'+hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def write(path, content):
    p=R/path;p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(content,encoding='utf-8');return p

def render(m,b):return '<!-- ENTERPRISE_MATH_TASK_V1\n'+json.dumps(m,indent=2,ensure_ascii=False)+'\n-->\n\n'+b.rstrip()+'\n'
def parse(t):
    prefix='<!-- ENTERPRISE_MATH_TASK_V1\n';assert t.startswith(prefix)
    i=t.index('\n-->',len(prefix)); return json.loads(t[len(prefix):i]),t[i+len('\n-->'):].lstrip('\n')
def audit(t, dispatch):
    # Equivalent preflight for current fixed no-override direct-user publication scope.
    # Every current regex is evaluated; origin, lineage and prepared-record checks included.
    errors=[]
    try:m,b=parse(t)
    except Exception:return ['TB-PARSE']
    for k,v in REQUIRED.items():
        if k not in m or (v is not None and m[k]!=v):errors.append('TB-META:'+k)
    if m.get('created_by_role') not in ['RESEARCHER','RESEARCH_DRIVER','FOUNDATION_STEWARD']:errors.append('PUBLISHER_ROLE')
    for k in ['researcher_id','driver_id','execution_id']:
        if k in m:errors.append('TB-RUNTIME-META:'+k)
    origins=['DIRECT_USER_DIRECTION','DRIVER_ROADMAP','FREE_AXIOM_CANDIDATE','FOUNDATION_QUESTION','REPLAY_OR_INTEGRATION','MAINTENANCE']
    if m.get('origin_kind') not in origins:errors.append('TB-ORIGIN-VALUE')
    if m.get('origin_kind')=='FREE_AXIOM_CANDIDATE':
        if not m.get('origin_candidate_id'):errors.append('TB-ORIGIN-CANDIDATE')
        if m.get('origin_candidate_state') not in ['AUDITED_AXIOM_CANDIDATE','AUDITED_REPLACEMENT_CANDIDATE','EXACT_NEGATIVE_OBSTRUCTION']:errors.append('TB-ORIGIN-CANDIDATE-STATE')
    if m.get('origin_kind')=='FOUNDATION_QUESTION' and not m.get('origin_foundation_question_id'):errors.append('TB-ORIGIN-FOUNDATION')
    lin=m.get('task_lineage')
    if lin not in ['NEW_DIRECTION','CONTINUATION','REPLAY','INTEGRATION','MAINTENANCE']:errors.append('TB-LINEAGE-VALUE')
    stages=[int(x) for x in re.findall(r'\bSTAGE[- _]?(\d+)\b',m.get('task_id','')+' '+m.get('title',''),flags=re.I)]
    if stages and max(stages)>=2 and lin!='CONTINUATION':errors.append('TB-STAGE-LINEAGE')
    if lin=='CONTINUATION':
        if not m.get('parent_task_id'):errors.append('TB-SUCCESSOR-PARENT')
        for k in GATE:
            if not (m.get('successor_gate') or {}).get(k):errors.append('TB-SUCCESSOR-GATE:'+k)
    if lin!='CONTINUATION' and (m.get('parent_task_id') or m.get('successor_gate')):errors.append('SCOPED_PREFLIGHT_UNSUPPORTED_LINEAGE_EXTRA')
    review=m.get('policy_review') or {}
    if review.get('policy_set')!='research_taskbook_policy.json':errors.append('TB-POLICY-SET')
    if review.get('policy_digest')!=DIGEST:errors.append('TB-POLICY-STALE')
    if dispatch and review.get('review_state')!='PASS':errors.append('TB-POLICY-REVIEW')
    if review.get('temporary_overrides')!=[]:errors.append('SCOPED_PREFLIGHT_OVERRIDE_UNSUPPORTED')
    for code,patterns in PATTERNS.items():
        if any(re.search(p,b,flags=re.I|re.M) for p in patterns):errors.append(code)
    for k in ['task_id','title','frontier','next_action','parent_objective_id']:
        if not isinstance(m.get(k),str) or not m[k].strip():errors.append('PREPARED_NONEMPTY:'+k)
    if m.get('registry_key')!=m.get('task_id'):errors.append('REGISTRY_KEY')
    if m.get('parent_objective_id')!=OBJ or m.get('parent_objective_generation_id')!=GEN:errors.append('OBJECTIVE_BINDING')
    if m.get('owner')!='taskbook/unassigned' or m.get('base_state')!='READY':errors.append('FRESH_OWNER_STATE')
    parts={}
    found=[(x.start(),x.end(),x.group(1)) for x in re.finditer(r'^## (.+)$',b,re.M)]
    for i,(s,e,name) in enumerate(found):parts[name]=b[e:found[i+1][0] if i+1<len(found) else len(b)].strip()
    for name in SECTIONS:
        if not parts.get(name) or re.search(r'<(?:write|task|describe|insert)|\b(?:TODO|TBD)\b',parts.get(name,''),re.I):errors.append('BODY:'+name)
    return errors


if __name__ == '__main__':
    report=json.loads((R/PREFIX/'preflight.json').read_text())
    assert report['policy_digest']==DIGEST
    archive=R/PREFIX/'source_archive.zip'
    assert hashlib.sha256(archive.read_bytes()).hexdigest()=='7d2002193d3cb5ef79d699354a86ab0d0082a853623290c89abbdb818b3fb7dd'
    count=0
    for expected in report['reports']:
        tid=expected['task_id']; p=R/'research_tasks'/f'{tid}.md'; text=p.read_text()
        assert not audit(text,True), audit(text,True)
        m,b=parse(text)
        assert blob(p.read_bytes())==expected['taskbook_blob_sha1']
        rp=R/'research_task_records'/tid/(expected['publication_id']+'.json')
        rec=json.loads(rp.read_text())
        assert blob(rp.read_bytes())==expected['record_blob_sha1']
        assert rec['taskbook_blob_sha1']==blob(p.read_bytes())
        assert rec['publication_id']=='TP2-'+hashlib.sha256('\0'.join([tid,rec['taskbook_blob_sha1'],PUBLISHER,OBJ]).encode()).hexdigest()[:20].upper()
        assert rec['publication_generation']==1 and rec['supersedes_publication_id'] is None
        for k in ['task_id','registry_key','parent_objective_id','task_lineage','origin_kind','parent_task_id','frontier','next_action','owner','source_refs','dependencies','successor_gate','parent_objective_generation_id']:
            assert rec[k]==m[k]
        for mut in [lambda q:q['policy_review'].update(policy_digest='sha256:0'),lambda q:q['policy_review'].update(review_state='PENDING_POLICY_REVIEW'),lambda q:q.update(researcher_id='forbidden'),lambda q:q.update(parent_objective_id=''),lambda q:q.update(task_lineage='CONTINUATION'),lambda q:q.update(origin_kind='FREE_AXIOM_CANDIDATE'),lambda q:q.update(parent_objective_generation_id='OG-WRONG')]:
            bad=copy.deepcopy(m);mut(bad);assert audit(render(bad,b),True);count+=1
        assert audit(render(m,b.replace('## Mother question','## Removed section')),True);count+=1
        for phrase in ['GitHub Actions','scheduler','canonical promotion','REMOTE_SILENT','no fixed researcher-id','pass is not a successor trigger']:
            assert audit(render(m,b+'\n'+phrase),True);count+=1
        print(tid+': POLICY, BODY, RECORD PASS')
    assert count==42
    print('42 negative mutations rejected; exact archive and three transactions verified.')
