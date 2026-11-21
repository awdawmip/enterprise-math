"""Persist each orbit representative of the final 9861 mixed-core profile."""
import argparse,hashlib,json,subprocess,time
from pathlib import Path
here=Path(__file__).resolve().parent;work=here/'work'
p=argparse.ArgumentParser();p.add_argument('--frames',default='0,1,3,5');p.add_argument('--receipts',type=Path,default=here/'mixed_frame_receipts');a=p.parse_args()
request=(here/'frame_pending_request.txt').read_text();directory=a.receipts.resolve();directory.mkdir(parents=True,exist_ok=True)
manifest=json.loads((here/'mixed_frame_orbits.json').read_text())
source_sha=hashlib.sha256((here/'front_orbit_frames.cpp').read_bytes()).hexdigest();bank_sha=hashlib.sha256((work/'bank').read_bytes()).hexdigest()
for fi in map(int,a.frames.split(',')):
 dest=directory/f'frame_{fi}.json'
 if dest.exists():continue
 (here/'mixed_frame_running.json').write_text(json.dumps({'frame':fi,'started':time.time()})+'\n')
 started=time.monotonic()
 r=subprocess.run([work/'front_orbit_frames',work/'bank',work,work,str(fi)],input=request,text=True,capture_output=True,check=True)
 fields=list(map(int,r.stdout.split()));assert len(fields)==5 and fields[0]==9861
 assert any(line.startswith(f'FRAME_BEGIN 9861 {fi} 9 ') for line in r.stderr.splitlines())
 assert any(line.startswith(f'FRAME_END 9861 {fi} ') for line in r.stderr.splitlines())
 row={'frame':fi,'free_mask':manifest['free_masks'][fi],'cost':fields[0],'geometric_nodes':fields[1],'leaf_nodes':fields[2],'search_nodes':fields[3],'found':fields[4],'seconds':time.monotonic()-started,'source_sha256':source_sha,'bank_sha256':bank_sha,'stderr':r.stderr}
 dest.write_text(json.dumps(row,indent=2)+'\n');print(json.dumps(row),flush=True)
 if row['found']:break
(here/'mixed_frame_running.json').unlink(missing_ok=True)
