"""Check the full 9-frame domain and reconcile exact search receipts by affine orbit."""
import argparse,hashlib,json
from pathlib import Path
here=Path(__file__).resolve().parent;work=here/'work';work=work if (work/'linear').exists() else here/'inputs';FULL=(1<<125)-1
parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--receipts',type=Path,default=here/'mixed_frame_receipts');args=parser.parse_args()
frames=set()
for line in (work/'cores2.txt').read_text().splitlines():
 lo,hi,*centres=map(int,line.split());assert len(centres)==2;free=lo+(hi<<64)
 for c in centres:
  if free>>c&1:frames.add(free^(1<<c))
frames=sorted(frames);assert len(frames)==9
manifest=json.loads((here/'mixed_frame_orbits.json').read_text());assert manifest['free_masks']==list(map(str,frames))
linear=[list(map(int,l.split())) for l in (work/'linear').read_text().splitlines()]
assert len(linear)==96 and len(set(map(tuple,linear)))==96
for row in linear:assert sorted(row)==list(range(125))
source=hashlib.sha256((here/'front_orbit_frames.cpp').read_bytes()).hexdigest();bank=(hashlib.sha256((work/'bank').read_bytes()).hexdigest() if (work/'bank').exists() else '5037ac43179fe73784d32e0f8011d105aeea1d0df964ef7bbfa13c7641a5f564')
receipts={}
for p in args.receipts.glob('frame_*.json'):
 row=json.loads(p.read_text());fi=row['frame'];assert row['free_mask']==str(frames[fi]);assert row['found']==0 and row['cost']==9861
 assert row['source_sha256']==source and row['bank_sha256']==bank
 assert f'FRAME_BEGIN 9861 {fi} 9 ' in row['stderr']
 assert f"FRAME_END 9861 {fi} {row['search_nodes']} 0" in row['stderr']
 receipts[fi]=row
covered=set();used=[]
for orbit in manifest['orbits']:
 rep=orbit['representative'];members=set(map(int,orbit['members']))
 assert not covered&members;covered|=members
 for member,action in orbit['members'].items():
  a=linear[action['linear_row']];d=action['translation'];p=[i for i in range(125) if frames[rep]>>i&1]
  image=sum(1<<(25*((a[i]//25+d//25)%5)+5*((a[i]//5%5+d//5%5)%5)+(a[i]%5+d%5)%5) for i in p)
  assert image==frames[int(member)]
 candidates=members&receipts.keys();assert candidates
 chosen=min(candidates,key=lambda fi:receipts[fi]['search_nodes']);used.append(chosen)
assert covered==set(range(9))
tag='9-557-3_10-744-2_10-747-2_11-936-3_12-1104-1_13-1296-1'
result={'cost':9861,'tag':tag,'engine':'orbit-min-fixed-frame-affine-cover','geometric_nodes':sum(receipts[i]['geometric_nodes'] for i in used),'leaf_nodes':sum(receipts[i]['leaf_nodes'] for i in used),'search_nodes':sum(receipts[i]['search_nodes'] for i in used),'found':0,'frames_in_complete_domain':9,'affine_frame_orbits':5,'frame_representatives_used':used,'source_sha256':source,'bank_sha256':bank,'complete':True,'scope':'Full final 9861 profile, via exact integer covers for five representative free sets and explicitly verified affine transports to all nine fixed-core free sets.'}
(here/'mixed_frame_result.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
(here/'mixed_completed.jsonl').write_text(json.dumps(result,sort_keys=True)+'\n');print(json.dumps(result,sort_keys=True,indent=2))
