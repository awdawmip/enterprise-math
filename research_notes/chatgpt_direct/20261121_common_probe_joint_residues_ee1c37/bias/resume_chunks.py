"""Resume a prepared weighted-bias census using complete, durable frame chunks.

The prepared directory is produced by replay.py. This uses the same unchanged
native source and all complete per-profile receipts; it changes only scheduling.
A chunk [first,end) is passed to the original engine's inclusive-id convention.
"""
from concurrent.futures import ThreadPoolExecutor,as_completed
from pathlib import Path
from collections import defaultdict
import argparse,hashlib,json,os,subprocess,sys,time
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--baseline',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
p.add_argument('--work',type=Path,required=True);p.add_argument('--jobs',type=int,default=4)
p.add_argument('--profiles',type=Path,required=True);p.add_argument('--chunk-size',type=int,default=0)
a=p.parse_args();baseline=a.baseline.resolve();out=a.output.resolve();work=a.work.resolve()
sys.path.insert(0,str(baseline/'bias'))
from plan_extended import catalog
plan=json.loads(a.profiles.read_text());q=plan['q'];rows=plan['rows'];case_dir=out/f'completed_q{q}';chunks=out/f'chunks_q{q}';chunks.mkdir(exist_ok=True)
case_dir.mkdir(exist_ok=True)
combined_path=out/f'completed_q{q}.json';combined=json.loads(combined_path.read_text()) if combined_path.exists() else {}
source=baseline/'bias/weighted_native.cpp';binary=work/'native_chunks'
subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',str(source),'-o',str(binary)],check=True)
label=lambda s:','.join(map(str,s))
identity={str(f.relative_to(work)):hashlib.sha256(f.read_bytes()).hexdigest()for f in work.iterdir()if f.name in ['obs','parent','B11','B12']or f.name.startswith('f')and f.name[1:2].isdigit()}
identity['native_source_sha256']=hashlib.sha256(source.read_bytes()).hexdigest()
metadata=chunks/'input_identity.json'
if metadata.exists():assert json.loads(metadata.read_text())==identity
else:metadata.write_text(json.dumps(identity,indent=2,sort_keys=True)+'\n')
weights=','.join(str(min((q*c-d for c,d in catalog.get((s,0),{}).items()),default=100000))for s in range(14))
profiles={};todo_by_profile=[]
for P,E,floor,ceiling in rows:
 key=label(P)+'__'+label(E);frame=work/f'f{len(E)}_{sum(E)}';total=sum(1 for _ in frame.open());receipt=case_dir/(key+'.json')
 if receipt.exists() or key in combined:
  v=json.loads(receipt.read_text()) if receipt.exists() else combined[key];assert v['algorithm']=='weighted_hall' and v['result'][:3]==[ceiling,floor,total] and v['result'][-1]==0
  continue
 weightedE=sum(min(q*c-d for c,d in catalog[s,1].items())for s in E)+q*(floor-sum(min(catalog[s,1])for s in E))
 profiles[key]={'P':P,'E':E,'floor':floor,'ceiling':ceiling,'total':total,'ranges':[],'receipt':receipt}
 group=[]
 existing=[]
 for t in chunks.glob(key+'__*.json'):
  r=json.loads(t.read_text());assert r['profile']==key and r['counts'][-1]==0
  assert 0<=r['first']<r['end']<=total and r['counts'][0]==r['end']-r['first']
  existing.append((r['first'],r['end']))
 existing.sort();cursor=0;ranges=[];chunk_size=a.chunk_size or max(1,(total+15)//16)
 for start,end in existing+[(total,total)]:
  assert start>=cursor
  while cursor<start:
   stop=min(start,cursor+chunk_size);ranges.append((cursor,stop));cursor=stop
  if start<end:ranges.append((start,end));cursor=end
 assert cursor==total
 for first,end in ranges:
  target=chunks/(key+f'__{first}_{end}.json');profiles[key]['ranges'].append(target)
  if target.exists():
   r=json.loads(target.read_text());assert r['first']==first and r['end']==end and r['counts'][0]==end-first and r['counts'][-1]==0
   continue
  cmd=[str(binary),str(work/'obs'),str(work/'parent'),str(work/'B'),str(frame),label(P),label(E),str(floor),str(ceiling),str(first),str(end),str(q),str(weightedE),weights]
  group.append((key,first,end,target,cmd))
 todo_by_profile.append(group)
# Interleave profiles so a very large frame does not block all later profiles.
todo=[]
while any(todo_by_profile):
 for group in todo_by_profile:
  if group:todo.append(group.pop(0))
print(json.dumps({'pending_profiles':len(profiles),'pending_chunks':len(todo),'jobs':a.jobs}),flush=True)
def settle(key):
 d=profiles[key]
 if not all(t.exists()for t in d['ranges']):return
 counts=[0]*5
 for t in d['ranges']:
  x=json.loads(t.read_text());assert x['counts'][0]==x['end']-x['first'] and x['counts'][-1]==0
  counts=[u+v for u,v in zip(counts,x['counts'])]
 assert counts[0]==d['total'];value={'key':key,'algorithm':'weighted_hall','result':[d['ceiling'],d['floor'],*counts]}
 if d['receipt'].exists():assert json.loads(d['receipt'].read_text())==value
 else:
  d['receipt'].write_text(json.dumps(value,sort_keys=True)+'\n');print(json.dumps({'completed_profile':key,'counts':counts}),flush=True)
for key in profiles:settle(key)
def run(item):
 key,first,end,target,cmd=item;start=time.time()
 r=subprocess.run(cmd,capture_output=True,text=True,check=True);counts=list(map(int,r.stderr.split()));assert len(counts)==5
 if counts[-1]:
  (out/(key+f'__{first}_{end}.witness.txt')).write_text(r.stdout)
  raise RuntimeError('Competing witness: '+key+' '+str(first))
 assert not r.stdout and counts[0]==end-first
 value={'profile':key,'first':first,'end':end,'counts':counts,'elapsed_seconds':time.time()-start}
 target.write_text(json.dumps(value,sort_keys=True)+'\n');return key,value
with ThreadPoolExecutor(a.jobs)as pool:
 futures=[pool.submit(run,item)for item in todo]
 for future in as_completed(futures):
  key,value=future.result();print(json.dumps(value),flush=True);settle(key)
print(json.dumps({'completed_profiles_total':len(list(case_dir.glob('*.json'))),'planned_profiles':len(rows)}),flush=True)
