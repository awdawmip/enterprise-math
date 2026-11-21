"""Run or resume the finite q2 plan; only complete frame chunks are evidence."""
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor,as_completed
from threading import Lock,Event
import argparse,hashlib,json,subprocess,time
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--work',type=Path,required=True);p.add_argument('--frames',type=Path,required=True);p.add_argument('--inheritance',type=Path,required=True);p.add_argument('--catalog',type=Path,required=True);p.add_argument('--source',type=Path,required=True);p.add_argument('--engine',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--jobs',type=int,default=2)
a=p.parse_args();w=a.work.resolve();out=a.output.resolve();out.mkdir(parents=True,exist_ok=True);chunks=out/'chunks';completed=out/'completed';chunks.mkdir(exist_ok=True);completed.mkdir(exist_ok=True)
hashfile=lambda x:hashlib.sha256(Path(x).read_bytes()).hexdigest()
def save(path,data):
 tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n');tmp.replace(path)
meta={'source_sha256':hashfile(a.source),'typed_catalog_sha256':hashfile(a.catalog),'inheritance_sha256':hashfile(a.inheritance),'prepared':{name:hashfile(w/name)for name in ['obs','parent','B11','B12','maps']},'q':2,'algorithm':a.engine.stem+'_signed_ordered_budget_spectrum_full13_union_root_orbit'}
meta_path=out/'input_identity.json'
if meta_path.exists():assert json.loads(meta_path.read_text())==meta
else:save(meta_path,meta)
cat=defaultdict(dict)
for line in a.catalog.read_text().splitlines()[1:]:
 s,e,c,d=map(int,line.split());cat[s,e][c]=d
weights=','.join(str(min((2*c-d for c,d in cat[s,0].items()),default=999999))for s in range(14))
joblist=json.loads(a.inheritance.read_text())['jobs'];assert len(joblist)==775
joblist.sort(key=lambda j:(j.get('q3_search_nodes',0),-j['q2_ceiling'],j['key']))
profiles={};tasks=[];lock=Lock();stop=Event();active={};witnesses=[];chunkCache={};completedCache={}
for job in joblist:
 key=job['key'];E=job['E'];P=job['P'];frame_name=f'f{len(E)}_{sum(E)}';frame=(a.frames/frame_name if (a.frames/frame_name).exists()else w/frame_name).resolve();assert frame.exists()
 total=sum(1 for line in frame.open());parts=4 if(total>1000 or job.get('q3_search_nodes',0)>1000000 and total>8)else 1;step=max(1,(total+parts-1)//parts)
 ranges=[(first,min(first+step,total))for first in range(0,total,step)]
 weighted_e=sum(min(2*c-d for c,d in cat[s,1].items())for s in E)+2*(job['embedded_floor']-sum(min(cat[s,1])for s in E))
 data={'job':job,'frame':str(frame),'frame_sha256':hashfile(frame),'total_frames':total,'ranges':ranges,'weighted_embedded_floor':weighted_e};profiles[key]=data
 for first,end in ranges:
  target=chunks/(key+f'__{first}_{end}.json')
  args=[str(w/'obs'),str(w/'parent'),str(w/'B'),str(frame),','.join(map(str,P)),','.join(map(str,E)),str(job['embedded_floor']),str(job['q2_ceiling']),str(first),str(end),'2',str(weighted_e),weights,str(w/'maps'),str(a.catalog.resolve()),str(job['minimum_cost'])]
  spec={'key':key,'first':first,'end':end,'minimum_cost':job['minimum_cost'],'maximum_cost':job['q2_ceiling'],'embedded_floor':job['embedded_floor'],'frame_sha256':data['frame_sha256'],'source_sha256':meta['source_sha256']}
  if target.exists():
   old=json.loads(target.read_text());assert old['spec']==spec and old['returncode']==0 and old['counts'][0]==end-first and old['counts'][-1]==0 and not old['stdout'];chunkCache[(key,first,end)]=old
  else:tasks.append((key,target,args,spec))

def summary():
 values=list(completedCache.values())
 return {'planned_profiles':len(profiles),'completed_profiles':len(values),'complete_exclusion':len(values)==len(profiles)and not witnesses,'witnesses':witnesses,'completed_frame_chunks':len(chunkCache),'completed_profile_frames':sum(v['counts'][0]for v in values),'completed_profile_search_nodes':sum(v['counts'][1]for v in values),'total_planned_profile_frames':sum(v['total_frames']for v in profiles.values()),'algorithm':meta['algorithm'],'source_sha256':meta['source_sha256'],'all_unfinished_profiles_remain_pending':True}

def settle(key):
 d=profiles[key];receipts=[]
 for first,end in d['ranges']:
  if (key,first,end)not in chunkCache:return
  r=chunkCache[key,first,end];assert r['counts'][0]==end-first and r['counts'][-1]==0;receipts.append(r)
 counts=[sum(r['counts'][j]for r in receipts)for j in range(5)];assert counts[0]==d['total_frames']
 result={'key':key,'job':d['job'],'counts':counts,'ranges':d['ranges'],'frame_sha256':d['frame_sha256'],'source_sha256':meta['source_sha256'],'algorithm':meta['algorithm'],'complete_profile_exclusion':True}
 target=completed/(key+'.json')
 if key in completedCache:assert completedCache[key]==result
 elif target.exists():assert json.loads(target.read_text())==json.loads(json.dumps(result))
 else:save(target,result);print(json.dumps({'completed_profile':key,'counts':counts}),flush=True)
 completedCache[key]=result
for key in profiles:settle(key)
save(out/'profiles.json',profiles);save(out/'summary.json',summary());print(json.dumps({'pending_chunks':len(tasks),**summary()}),flush=True)

def run(task):
 key,target,args,spec=task
 if (out/'STOP').exists():stop.set()
 if stop.is_set():return
 started=time.time();process=subprocess.Popen([str(a.engine.resolve()),*args],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
 active_key=key+'__'+str(spec['first'])
 with lock:active[active_key]=spec;save(out/'active.json',active)
 while process.poll() is None:
  if (out/'STOP').exists():stop.set()
  if stop.wait(0.25):
   process.terminate();process.communicate()
   with lock:active.pop(active_key,None);save(out/'active.json',active)
   return
 stdout,stderr=process.communicate();counts=list(map(int,stderr.split()))if process.returncode==0 else []
 receipt={'spec':spec,'returncode':process.returncode,'stdout':stdout,'stderr':stderr,'counts':counts,'elapsed_seconds':time.time()-started}
 if process.returncode!=0 or len(counts)!=5:
  save(out/(key+'.error.json'),receipt);stop.set();raise RuntimeError(key+' search error')
 if counts[-1]:
  save(out/(key+'.witness.json'),receipt)
  with lock:witnesses.append(key);stop.set();save(out/'summary.json',summary());print(json.dumps({'competing_witness':key,'counts':counts}),flush=True)
  return
 assert not stdout and counts[0]==spec['end']-spec['first']
 with lock:
  save(target,receipt);chunkCache[key,spec['first'],spec['end']]=receipt;active.pop(active_key,None);save(out/'active.json',active);settle(key);save(out/'summary.json',summary());print(json.dumps({'completed_chunk':key,'first':spec['first'],'end':spec['end'],'counts':counts,'elapsed_seconds':receipt['elapsed_seconds']}),flush=True)
with ThreadPoolExecutor(a.jobs)as pool:
 futures=[pool.submit(run,task)for task in tasks]
 for future in as_completed(futures):future.result()
with lock:save(out/'summary.json',summary())
print(json.dumps(summary()),flush=True)
