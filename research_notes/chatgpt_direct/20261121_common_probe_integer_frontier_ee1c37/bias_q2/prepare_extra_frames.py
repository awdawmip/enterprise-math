"""Generate the three q2-only canonical mother-family catalogues."""
from concurrent.futures import ThreadPoolExecutor,as_completed
from pathlib import Path
import argparse,hashlib,json,subprocess,time
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--baseline',type=Path,required=True);p.add_argument('--work',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--jobs',type=int,default=2);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
base=a.baseline.resolve();w=a.work.resolve();out=a.output.resolve();sources={'union':base/'previous/previous/mothers/union.cpp','frame':base/'previous/eleven/frame.cpp'}
for name,src in sources.items():subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',str(src),'-o',str(out/name)],check=True)
parent=(w/'parent').read_text()
def generate(key):
 k,s=key;t=time.time();raw=out/f'raw{k}_{s}';f=out/f'f{k}_{s}';target=out/f'f{k}_{s}.json'
 if target.exists():
  data=json.loads(target.read_text());assert data['frame_sha256']==hashlib.sha256(f.read_bytes()).hexdigest();return data
 with raw.open('w')as stream:subprocess.run([str(out/'union'),str(k),str(s),'-1','all'],input=parent,text=True,stdout=stream,check=True)
 with raw.open()as stream,f.open('w')as dest:r=subprocess.run([str(out/'frame'),str(w/'parent'),str(w/'maps'),str(k)],stdin=stream,stdout=dest,stderr=subprocess.PIPE,text=True,check=True)
 n,canonical=map(int,r.stderr.split());assert canonical==sum(1 for line in f.open()) and n>=canonical>0
 data={'k':k,'minimum_union':s,'raw_count':n,'canonical_count':canonical,'frame_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'parent_sha256':hashlib.sha256((w/'parent').read_bytes()).hexdigest(),'maps_sha256':hashlib.sha256((w/'maps').read_bytes()).hexdigest(),'source_sha256':{name:hashlib.sha256(src.read_bytes()).hexdigest()for name,src in sources.items()},'elapsed_seconds':time.time()-t}
 target.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n');raw.unlink();return data
with ThreadPoolExecutor(a.jobs)as pool:
 for task in as_completed([pool.submit(generate,key)for key in [(3,38),(4,48),(7,80)]]):print(json.dumps(task.result()),flush=True)
