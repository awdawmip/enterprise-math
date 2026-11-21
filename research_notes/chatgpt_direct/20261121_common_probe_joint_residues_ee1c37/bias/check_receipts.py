"""Verify complete receipt accounting, frame partitions, and summary consistency.
This is an integrity check; replay.py performs the actual exhaustive searches.
"""
from pathlib import Path
from collections import defaultdict
import argparse,hashlib,json
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--baseline',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();h=Path(__file__).resolve().parent
plan=json.loads((h/'profiles_q3.json').read_text());records=json.loads((h/'completed_q3.json').read_text());result=json.loads((h/'result_q3_weighted.json').read_text());chunks=json.loads((h/'frame_chunks_q3.json').read_text());identity=json.loads((h/'frame_chunk_inputs.json').read_text());label=lambda s:','.join(map(str,s))
assert hashlib.sha256((a.baseline/'bias/weighted_native.cpp').read_bytes()).hexdigest()==identity['native_source_sha256']
keys=set()
for P,E,floor,ceiling in plan['rows']:
 key=label(P)+'__'+label(E);keys.add(key);r=records[key];v=r['result'];family=result['normalized_mother_locations'][f'{len(E)},{sum(E)}'][1]
 assert r['key']==key and r['algorithm']=='weighted_hall' and v[:3]==[ceiling,floor,family] and v[-1]==0
 assert result['cases'][key]==v
assert keys==set(records)==set(result['cases']) and len(keys)==530
counts=[sum(r['result'][j]for r in records.values())for j in range(2,7)]
assert counts[0]==result['family_profile_placements']==3086925
assert counts[1]==result['search_nodes']==584517341
assert counts[3]==result['settlement_calls']==0 and counts[4]==0
assert result['complete_exclusion'] and result['competing_witness_profiles']==0
chunk_count=0;chunk_frames=0
for key,parts in chunks.items():
 cursor=0;total=[0]*5
 for r in sorted(parts,key=lambda x:x['first']):
  assert r['profile']==key and r['first']==cursor and r['end']>cursor
  assert r['counts'][0]==r['end']-r['first'] and r['counts'][-1]==0
  cursor=r['end'];total=[u+v for u,v in zip(total,r['counts'])];chunk_count+=1
 assert total==records[key]['result'][2:];chunk_frames+=cursor
out={'profiles':len(keys),'complete_exclusion':True,'family_profile_placements':counts[0],'search_nodes':counts[1],'enumerated_class_emissions':counts[2],'settlement_calls':counts[3],'competing_profiles':counts[4],'chunked_profiles':len(chunks),'complete_frame_chunks':chunk_count,'frame_chunk_coverage':chunk_frames,'native_source_sha256':identity['native_source_sha256'],'scope':'Receipt integrity and exact frame coverage; mathematical exhaustiveness is replayed by replay.py.'}
a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out),flush=True)
