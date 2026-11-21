"""Portable audit or complete native rerun of the 9861 layer."""
import argparse,json,subprocess,sys,tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--previous',type=Path,required=True)
p.add_argument('--mode',choices=['audit','full'],default='audit')
p.add_argument('--jobs',type=int,default=2)
p.add_argument('--output',type=Path,default=HERE/'verification')
a=p.parse_args();previous=a.previous.resolve();a.output.mkdir(parents=True,exist_ok=True)
if a.mode=='audit':
 subprocess.run([sys.executable,HERE/'audit_mixed_frames.py'],check=True)
 subprocess.run([sys.executable,HERE/'audit_completed.py','--previous',previous,'--spectrum',HERE/'class_cost_spectrum.json','--receipts',HERE/'certificates/cost_9861_completed.jsonl','--first','9861','--last','9861','--output',a.output],check=True)
 actual=json.loads((a.output/'coverage.json').read_text())['layers'][0]
 expected=json.loads((HERE/'certificates/coverage.json').read_text())['layers'][0]
 assert actual==expected,(actual,expected)
 print(json.dumps({'complete':True,'profiles':114,'search_rerun':False,'cost':9861,'new_global_lower_bound':9862}))
else:
 with tempfile.TemporaryDirectory(prefix='twelve_9861_') as scratch:
  subprocess.run([sys.executable,HERE/'replay.py','--previous',previous,'--work',scratch,'--first','9861','--last','9870','--cost','9861','--cores','0,1,2','--engine','orbit-min','--jobs',str(a.jobs)],check=True)
  subprocess.run([sys.executable,HERE/'audit_completed.py','--previous',previous,'--seeds',Path(scratch)/'seeds','--receipts',Path(scratch)/'completed.jsonl','--first','9861','--last','9861','--output',a.output],check=True)
  actual=json.loads((a.output/'coverage.json').read_text())['layers'][0]
  assert actual['complete'] and actual['expected_low_core_profiles']==114
 print(json.dumps({'complete':True,'profiles':114,'search_rerun':True,'cost':9861,'new_global_lower_bound':9862}))
