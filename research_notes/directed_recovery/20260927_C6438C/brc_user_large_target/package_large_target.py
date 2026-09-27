"""Administrative packaging only; no scientific imports or replay."""
from pathlib import Path
import base64, hashlib, json, os
R=Path(__file__).resolve().parent
A=R/'publication_admin'
P='research_notes/directed_recovery/20260927_C6438C/brc_user_large_target/'
def sh(b): return hashlib.sha256(b).hexdigest()
def dump(x): return (json.dumps(x,ensure_ascii=False,indent=2)+'\n').encode()
def meta(n,b): return dict(path=n,remote_path=P+n,bytes=len(b),sha256=sh(b),git_blob_sha1=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())
names=json.loads((A/'PLANNED_PUBLICATION_FILES.json').read_bytes())['observed_text_inputs']+"""
read_streamed_records.py
read_interrupted_reported_cost.py
FULL_INTERRUPTION_SCOPE.md
ACTUAL_OUTPUT_INTEGRITY.json
RESULTS_AND_CONTINUE.md
RESULTS_PARENT_REVIEW_AND_ACCOUNTING.md
review/POSTMORTEM_STATIC_REVIEW.md
runs/full/ACTUAL_INTERRUPT_REQUEST.json
runs/full/INTERRUPTED_REPORTED_COST.json
runs/full/ACTUAL_REPORTED_COST_EXTRACTION_TOOL_RESULT.json
runs/block/STARTED.json
runs/block/SUMMARY.json
runs/block/RECORD_REVIEW.json
runs/block/ACTUAL_EXECUTION_INITIAL.json
runs/block/ACTUAL_EXECUTION_TOOL_LOG.json
runs/block/ACTUAL_RECORD_REVIEW_TOOL_RESULT.json
postmortem/postmortem_native.py
postmortem/PLAN.md
postmortem/read_postmortem_records.py
postmortem/POSTMORTEM_RECORD_REVIEW.json
postmortem/ACTUAL_RECORD_REVIEW_TOOL_RESULT.json
postmortem/run/STARTED.json
postmortem/run/SUMMARY.json
postmortem/run/ACTUAL_EXECUTION_INITIAL.json
postmortem/run/ACTUAL_EXECUTION_TOOL_LOG.json
postmortem/run/MEMBER_INDEX.jsonl
package_large_target.py
""".strip().splitlines()
assert len(names)==len(set(names))
raw={n:(R/n).read_bytes() for n in names}
for b in raw.values(): b.decode()
assert sh(raw['RESULTS_AND_CONTINUE.md'])=='d73700811a0f6ed4d368f79ed6881b3bf6454390a6743db92c48e123caedbb63'
assert sh(raw['streaming_public_clock.py'])=='e4cde846c1d5c0238b881e05f3128c184fb599366f7da1f3e55161c8fbf5b86b'
assert sh(raw['PLAN.md'])=='d861ea6b08801f457816e7a18752409d053f6e13174b2070320e0206511f87af'
summaries={}
for base in ['runs/block','postmortem/run']:
 s=json.loads(raw[base+'/SUMMARY.json']); summaries[base]=s
 assert s['execution_status']=='COMPLETE'
 for key,n in [('evidence','EVIDENCE.jsonl.gz'),('member_index','MEMBER_INDEX.jsonl')]:
  b=(R/base/n).read_bytes(); assert len(b)==s[key]['bytes'] and sh(b)==s[key]['sha256']
 for n,pin in s['binding']['dependencies'].items(): assert sh((R.parent/n).read_bytes())==pin,n
c=json.loads((A/'block_artifacts_v1/PREUPLOAD_ARTIFACT_CATALOG.json').read_bytes())
for i,e in enumerate(c['evidence']['chunks_in_order']+[c['index']]):
 n=e['path']; b=(A/'block_artifacts_v1'/n).read_bytes()
 assert meta(n,b)['git_blob_sha1']==e['git_blob_sha1'] and sh(b)==e['sha256']
 receipt=json.loads((A/f'block_blob_readbacks/part{i:03}.json').read_bytes())
 assert receipt['creation_result']['structuredContent']['sha']==e['git_blob_sha1']
 assert receipt['observation']['result']['structuredContent']['content'].encode()==b
 raw[n]=b
assert b''.join(base64.b64decode(raw[e['path']]) for e in c['evidence']['chunks_in_order'])==(R/'runs/block/EVIDENCE.jsonl.gz').read_bytes()
binary=[]
for n in ['input_integrity/FAILED.json.gz','input_integrity_v2/INPUT_RESULTS.json.gz','postmortem/run/EVIDENCE.jsonl.gz']:
 b=(R/n).read_bytes(); t=n+'.b64'; raw[t]=base64.b64encode(b)+b'\n'
 binary.append({'original':meta(n,b),'transport':meta(t,raw[t]),'reconstruction':'Decode this ASCII base64 file to exact original compressed bytes.'})
i=json.loads(raw['input_integrity_v2/INPUT_SUMMARY.json'])
for n,k in [('INPUT_RESULTS.json.gz','gzip_sha256'),('check_inputs_native.py','source_sha256'),('PLAN.md','plan_sha256')]:
 assert sh((R/'input_integrity_v2'/n).read_bytes())==i[k]
for n,b in raw.items():
 if (R/n).exists(): assert (R/n).read_bytes()==b
manifest={'schema':'BRC_USER_LARGE_TARGET_EVIDENCE_MANIFEST_V1','status':'FROZEN_EXACT_SAVED_BYTES_NOT_ADMISSION',
'entrypoint':'RESULTS_AND_CONTINUE.md','accounting_entrypoint':'RESULTS_PARENT_REVIEW_AND_ACCOUNTING.md',
'confirmed_target':'input_block.json only. Repeated-string full target cancelled; do not continue it.',
'formal_outcome':'k=3, E=N-Jacobi(k*k-4,N), both main signed gcds 1. Not general factoring or Shor closure.',
'character_predecessor_commit':'b0a9c5de14e058d5e478d3571d79df32fdb97e71',
'adjacent_predecessor_commit':'2034df3def543e151ef122e8e260d417331de0aa',
'block_evidence':c['evidence'],'block_member_index':c['index'],'other_compressed_evidence':binary,
'cancelled_full':{'remote_raw_stream_and_index':False,'preservation_receipt':'runs/full/INTERRUPTED_EVIDENCE_PRESERVATION.json','reported_cost_only':'runs/full/INTERRUPTED_REPORTED_COST.json','scope':'Raw stream/index preserved locally; remote metadata is not scientific completion or executable resume state.'},
'continuation':'Any authorized conversation may continue from saved outcomes and conditional diagnosis; no specific host/tool is required for symbolic progress. Advance factor-blind odd-part or geometric selection; new numeric work retains native typing and separate accounting.',
'dependencies':{k:s['binding']['dependencies'] for k,s in summaries.items()},
'files':[meta(n,b) for n,b in sorted(raw.items())],'manifest_excludes_own_hash':True,
'global_knowledge_sync':'main@a668c14 / GLOBAL_KNOWLEDGE_V1'}
raw['LARGE_TARGET_EVIDENCE_MANIFEST.json']=dump(manifest)
out=R/'publication'; stage=R/'publication.new'
assert not out.exists() and not stage.exists()
stage.mkdir()
for n,b in raw.items():
 p=stage/n;p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('xb') as f:f.write(b)
for n,b in raw.items(): assert (stage/n).read_bytes()==b
os.rename(stage,out)
catalog={'schema':'BRC_PUBLICATION_TRANSPORT_CATALOG_V1','prefix':P,'files':[meta(n,b) for n,b in sorted(raw.items())]}
with (A/'FINAL_TRANSPORT_CATALOG.json').open('xb') as f:f.write(dump(catalog))
print(json.dumps({'status':'ADMIN_FROZEN_NOT_PUBLISHED','files':len(raw),'manifest':meta('LARGE_TARGET_EVIDENCE_MANIFEST.json',raw['LARGE_TARGET_EVIDENCE_MANIFEST.json'])}))
