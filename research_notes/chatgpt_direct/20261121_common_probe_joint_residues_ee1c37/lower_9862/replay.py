"""Verify the complete cost-9862 certificate, or rerun its native integer search."""
import argparse,hashlib,json,subprocess,sys,tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--previous',type=Path,required=True,help='The 2026-11-20 complete predecessor package')
p.add_argument('--lower',type=Path,default=HERE.parent/'lower',help='The unchanged checkpoint-B lower/ proof directory')
p.add_argument('--mode',choices=['audit','full'],default='audit')
p.add_argument('--jobs',type=int,default=2)
p.add_argument('--output',type=Path,default=HERE/'verification')
a=p.parse_args();a.lower=a.lower.resolve();a.previous=a.previous.resolve();a.output.mkdir(parents=True,exist_ok=True)
bindings=json.loads((HERE/'bindings.json').read_text());expected=json.loads((HERE/'result.json').read_text())['layer']
for row in bindings['source_bindings']:
 assert hashlib.sha256((a.lower/row['path']).read_bytes()).hexdigest()==row['sha256'],row['path']
receipts=[json.loads(l) for l in (HERE/'cost_9862_completed.jsonl').read_text().splitlines()]
assert len(receipts)==len({r['tag'] for r in receipts})==114
assert all(r['cost']==9862 and r['found']==0 and r['engine']=='orbit-min' for r in receipts)

def audit(receipts,seeds=None):
 command=[sys.executable,a.lower/'audit_completed.py','--previous',a.previous,'--receipts',receipts,'--first','9862','--last','9862','--output',a.output]
 command+=['--seeds',seeds] if seeds else ['--spectrum',a.lower/'class_cost_spectrum.json']
 subprocess.run(command,check=True)
 actual=json.loads((a.output/'coverage.json').read_text())['layers'][0]
 assert actual['complete'] and actual['expected_low_core_profiles']==actual['completed_low_core_profiles']==114
 assert actual['profile_sha256']==expected['profile_sha256']
 return actual
if a.mode=='audit':
 actual=audit(HERE/'cost_9862_completed.jsonl');assert actual==expected
else:
 with tempfile.TemporaryDirectory(prefix='twelve_9862_') as temp:
  work=Path(temp)
  subprocess.run([sys.executable,a.lower/'replay.py','--previous',a.previous,'--work',work,'--first','9861','--last','9870','--cost','9862','--cores','0,1,2','--engine','orbit-min','--jobs',str(a.jobs)],check=True)
  for row in bindings['input_bindings']:
   assert hashlib.sha256((work/row['path']).read_bytes()).hexdigest()==row['sha256'],row['path']
  actual=audit(work/'completed.jsonl',work/'seeds')
result={'complete':True,'cost':9862,'profiles':114,'search_rerun':a.mode=='full','layer':actual,'new_global_lower_bound':9863,'upper_bound':9996}
(a.output/'result.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,sort_keys=True))
