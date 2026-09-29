"""New-transaction equivalent of the pinned taskbook/record preflight.
No network. Not a whole-repository audit or a native runtime receipt.
Policy digest is computed from connector-observed raw Git blob identities.
In a full checkout --root may point to it; --verify-existing never restamps files.
"""
from pathlib import Path
import argparse, copy, hashlib, json, re
from datetime import datetime, timezone
D='research_notes/cfd_pilots/20260929_task_publication_8F8257D1'
SECTIONS=('Mother question','Frozen inputs and scope','Hard target and required outputs','Research value to preserve','Success, kill, and return criteria')
GATES=('new_information_gap','why_parent_result_does_not_close_it','discriminating_outcomes','kill_condition','alternative_route_or_free_exploration_considered','why_new_stage_or_task_is_better_than_same_task_or_closure')
PATTERNS=[r'github actions',r'\bworkflow(?:s)?\b',r'\bremote validation\b',r'\bpull request\b',r'\bdraft pr\b',r'\bpush\b',r'\bpoll(?:ing)?\b',r'\bwait(?:ing)? for ci\b',r'\bcheck(?:ing)? ci\b',r'\bready for review\b',r'\bmoving main\b',r'\breconcil(?:e|ing).*main\b',r'\bissue #240\b',r'\bscheduler\b',r'\bheartbeat\b',r'\bclaim event\b',r'\bcanonical promotion\b',r'\bl4 promotion\b',r'\bmerge(?: the| this)? pr\b',r'ci_not_required_for_research',r'\bremote_silent\b',r'research is the hot path',r'github is a sparse persistence',r'no fixed researcher-id',r'do not wait for the driver to assign an id',r'pass is not a successor trigger',r'stage pass does not imply successor',r'successor-stage gate']
ORIGINS={'DIRECT_USER_DIRECTION','DRIVER_ROADMAP','FREE_AXIOM_CANDIDATE','FOUNDATION_QUESTION','REPLAY_OR_INTEGRATION','MAINTENANCE'}
LINEAGES={'NEW_DIRECTION','CONTINUATION','REPLAY','INTEGRATION','MAINTENANCE'}
REQUIRED=('task_id','title','kind','owner','base_state','priority','leverage','frontier','next_action','created_by_role','task_authority','publication_contract','publication_template','registry_key','parent_objective_id','identity_policy','final_response_identity_policy','origin_kind','task_lineage','parent_task_id','successor_gate','policy_review')
def enc(x): return json.dumps(x,ensure_ascii=False,indent=2)+'\n'
def gitblob(b): return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def split(t):
 prefix='<!-- ENTERPRISE_MATH_TASK_V1\n'
 if not t.startswith(prefix): raise ValueError('bad prefix')
 end=t.index('\n-->',len(prefix))
 return json.loads(t[len(prefix):end]), t[end+4:].lstrip('\n')
def render(m,b): return '<!-- ENTERPRISE_MATH_TASK_V1\n'+json.dumps(m,ensure_ascii=False,indent=2)+'\n-->\n\n'+b.rstrip()+'\n'
def pdigest(rows):
 h=hashlib.sha256()
 for r in rows: h.update(r['path'].encode()+b'\0'+bytes.fromhex(r['git_blob_sha1'])+b'\0')
 return 'sha256:'+h.hexdigest()
def audit(m,b,digest,approved=True):
 e=[]
 for k in REQUIRED:
  if k not in m:e.append('missing:'+k)
 for k in ('task_id','title','frontier','next_action','parent_objective_id'):
  if not isinstance(m.get(k),str) or not m[k].strip(): e.append('empty:'+k)
 if not re.fullmatch('[A-Za-z0-9._-]+',m.get('task_id','')):e.append('bad task id')
 for k,v in dict(task_authority='PUBLISHED_REGISTERED',publication_contract='RESEARCH_TASK_PUBLICATION_V1',publication_template='RESEARCH_TASK_PUBLICATION_TEMPLATE_V1',identity_policy='AUTO_RESOLVE_OR_ALLOCATE',final_response_identity_policy='INHERIT_GLOBAL',registry_key=m.get('task_id'),base_state='READY').items():
  if m.get(k)!=v:e.append('wrong:'+k)
 if m.get('created_by_role') not in {'RESEARCHER','RESEARCH_DRIVER','FOUNDATION_STEWARD'}:e.append('publisher role')
 if m.get('kind') not in {'RESEARCH','GOVERNANCE'}:e.append('kind')
 if m.get('origin_kind') not in ORIGINS:e.append('origin')
 if m.get('origin_kind')=='FREE_AXIOM_CANDIDATE' and (not m.get('origin_candidate_id') or m.get('origin_candidate_state') not in {'AUDITED_AXIOM_CANDIDATE','AUDITED_REPLACEMENT_CANDIDATE','EXACT_NEGATIVE_OBSTRUCTION'}):e.append('candidate origin')
 if m.get('origin_kind')=='FOUNDATION_QUESTION' and not m.get('origin_foundation_question_id'):e.append('foundation origin')
 if m.get('task_lineage') not in LINEAGES:e.append('lineage')
 stages=re.findall(r'stage[\s_-]*(\d+)',m.get('task_id','')+' '+m.get('title',''),re.I)
 if any(int(s)>=2 for s in stages) and m.get('task_lineage')!='CONTINUATION':e.append('stage lineage')
 if m.get('task_lineage')=='CONTINUATION':
  if not m.get('parent_task_id'):e.append('parent')
  g=m.get('successor_gate')
  if not isinstance(g,dict) or any(not g.get(k) for k in GATES):e.append('successor gap')
  elif not isinstance(g['discriminating_outcomes'],list):e.append('outcome list')
 for k in ('researcher_id','driver_id','execution_id'):
  if k in m:e.append('fixed runtime:'+k)
 review=m.get('policy_review') or {}
 if review.get('policy_set')!='research_taskbook_policy.json':e.append('policy set')
 if review.get('policy_digest')!=digest:e.append('stale policy')
 if approved and review.get('review_state')!='PASS':e.append('not approved')
 if review.get('temporary_overrides')!=[]:e.append('this preflight accepts no overrides')
 headers=[]
 for i,line in enumerate(b.splitlines()):
  if line.lstrip().startswith('##'):
   for s in SECTIONS:
    if s.lower() in line.lower():headers.append((i,s));break
 lines=b.splitlines(); payloads={}
 for j,(i,s) in enumerate(headers):payloads[s]='\n'.join(lines[i+1:headers[j+1][0] if j+1<len(headers) else len(lines)]).strip()
 for s in SECTIONS:
  if not payloads.get(s) or re.search(r'^\s*<[^>\n]+>\s*$',payloads.get(s,''),re.M):e.append('section:'+s)
 for pattern in PATTERNS:
  if re.search(pattern,b,re.I|re.M):e.append('policy-sensitive body:'+pattern)
 return e

def record(m,bpath,pub):
 bb='sha1:'+gitblob(bpath.read_bytes()); tid=m['task_id']; parent=m['parent_objective_id']; pid=pub['publisher_id']
 pubid='TP2-'+hashlib.sha256('\0'.join((tid,bb,pid,parent)).encode()).hexdigest()[:20].upper()
 r=dict(record_schema='ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2',record_state='ACTIVE',task_id=tid,registry_key=tid,publication_id=pubid,publication_generation=1,supersedes_publication_id=None,publication_contract='RESEARCH_TASK_PUBLICATION_V1',template_version='RESEARCH_TASK_PUBLICATION_TEMPLATE_V1',publication_transaction='RESEARCH_TASK_IMMUTABLE_PUBLICATION_V2',taskbook_path=pub['taskbook_path'],taskbook_blob_sha1=bb,publisher_role=pub['publisher_role'],publisher_id=pid,published_at=pub['published_at'],parent_objective_id=parent,origin_kind=m['origin_kind'],origin_candidate_id=m.get('origin_candidate_id'),origin_candidate_state=m.get('origin_candidate_state'),kind=m['kind'],task_lineage=m['task_lineage'],parent_task_id=m.get('parent_task_id'),claimable=True,effective_priority='P2',effective_leverage='MEDIUM',priority_source='RESEARCHER_DEFAULT',publisher_priority_request=m['priority'],publisher_leverage_request=m['leverage'],owner=m['owner'],frontier=m['frontier'],next_action=m['next_action'],research_value=pub['research_value'],terminal_scope='TASK',working_truth_granted=False,canonical_promotion_granted=False)
 assert pub['publisher_role']=='RESEARCHER' and pid and pub['research_value']
 for k in ('identity_lane','source_refs','dependencies','evidence_status','successor_gate','migration_source','parent_objective_generation_id'):
  if k in m:r[k]=m[k]
 return r

def main():
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);p.add_argument('--verify-existing',action='store_true');a=p.parse_args();root=a.root
 manifest=json.loads((root/D/'INPUTS.json').read_text()); d=pdigest(manifest['ordered_policy_blobs']); assert d==manifest['policy_digest']
 # A full checkout can additionally verify actual bytes against the pinned manifest.
 actual=[]
 for row in manifest['ordered_policy_blobs']:
  f=root/row['path']
  if f.exists():
   assert gitblob(f.read_bytes())==row['git_blob_sha1'],row['path']; actual.append(row['path'])
 result=[]; negative=0
 for spec in manifest['tasks']:
  f=root/spec['taskbook_path'];m,b=split(f.read_text()); assert not audit(m,b,d,approved=False),audit(m,b,d,approved=False)
  if not a.verify_existing:
   m['policy_review']['review_state']='PASS';f.write_text(render(m,b),encoding='utf-8')
  assert not audit(m,b,d),audit(m,b,d)
  # Mutation tests: reject broken critical metadata, ancestry, policy and body.
  for key in REQUIRED:
   n=copy.deepcopy(m);n.pop(key);assert audit(n,b,d),key;negative+=1
  for key,val in [('task_authority','DRAFT'),('policy_review',dict(policy_set='research_taskbook_policy.json',policy_digest='sha256:'+'0'*64,review_state='PASS',temporary_overrides=[])),('researcher_id','ILLEGAL_FIXED_EXECUTOR'),('origin_kind','FREE_AXIOM_CANDIDATE'),('task_lineage','CONTINUATION')]:
   n=copy.deepcopy(m);n[key]=val
   if key=='task_lineage':n['successor_gate']=None
   assert audit(n,b,d),key;negative+=1
  for sec in SECTIONS:
   assert audit(m,b.replace('## '+sec,'## Missing section'),d),sec;negative+=1
  assert audit(m,b+'\nUse GitHub Actions\n',d);negative+=1
  r=record(m,f,spec);rp=root/'research_task_records'/m['task_id']/(r['publication_id']+'.json')
  if a.verify_existing:assert json.loads(rp.read_text())==r
  else:rp.parent.mkdir(parents=True,exist_ok=True);rp.write_text(enc(r))
  # Record drift rejects a changed taskbook, grants, identities and copied fields.
  for key in ('taskbook_blob_sha1','working_truth_granted','canonical_promotion_granted','parent_objective_id','source_refs','successor_gate'):
   bad=copy.deepcopy(r);bad[key]='CORRUPT';assert bad!=record(m,f,spec);negative+=1
  result.append(dict(task_id=m['task_id'],taskbook_path=spec['taskbook_path'],taskbook_blob_sha1=r['taskbook_blob_sha1'],publication_id=r['publication_id'],record_path=rp.relative_to(root).as_posix(),record_blob_sha1='sha1:'+gitblob(rp.read_bytes()),findings=[]))
 assert len({r['task_id'] for r in result})==len(result)
 report=dict(schema='CFD_TASK_PUBLICATION_PREFLIGHT_RESULT_V1',state='PASS',checked_at=datetime.now(timezone.utc).isoformat(),scope='2 new task transactions only; source-derived equivalent validation, NOT full-registry audit or native runtime approval',policy_digest=d,negative_mutations_rejected=negative,tasks=result,actual_policy_files_in_local_root=actual,policy_blob_identity_source=manifest['source_commit'],native_runtime_state='SOURCE_TREE_SIZE_LIMIT;NO_DRIVER_SESSION',scientific_review='NOT_PERFORMED;PILOT_NOT_ADMITTED')
 if not a.verify_existing:(root/D/'PREFLIGHT.json').write_text(enc(report))
 print(enc(report))
if __name__=='__main__':main()
