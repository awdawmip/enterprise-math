#!/usr/bin/env python3
"""Independent configuration-level replay for EC49FPY. Inputs: master, root CSV, machine certificate.
No imports from REPRODUCE_EC49FPY, no scipy/numpy; validates all 310 original configs.
"""
import sys,csv,json,itertools,collections,hashlib
from pathlib import Path
A=Path(sys.argv[1]);B=Path(sys.argv[2]);C=Path(sys.argv[3]);cert=json.loads(C.read_text())
assert hashlib.sha256(A.read_bytes()).hexdigest()==cert['master_sha256']
assert hashlib.sha256(B.read_bytes()).hexdigest()==cert['root_cost_table_sha256']
with A.open() as f:
 fam_count,word_count,config_count=map(int,f.readline().split())
 assert (fam_count,word_count,config_count)==(94,178850,38169)
 family=[];roots=(3,5,6,7)
 for k in range(fam_count):
  d={r:set() for r in roots}
  for _ in range(int(f.readline())):
   label,rawhex=f.readline().split(); d[bytes.fromhex(rawhex)[0]].add(int(label))
  family.append(d)
 configs=[list(map(int,f.readline().split())) for _ in range(config_count)]
def allowed(k):
 a={j:set() for j in range(24)}
 for fam in configs[k]:
  for r,labels in family[fam].items():
   for label in labels:a[label].add(r)
 return tuple(tuple(sorted(a[j])) for j in range(24))
target=allowed(16943);ids=[k for k in range(config_count) if allowed(k)==target];assert len(ids)==310
multi=[j for j,rs in enumerate(target) if len(rs)>1]
alloc=list(itertools.product(*(target[j] for j in multi)));assert len(alloc)==144
root_coords={r:[] for r in roots}
for r in roots:
 optlabels=[j for j in multi if r in target[j]]
 root_coords[r]=sorted(sum(1<<j for idx,j in enumerate(optlabels) if subset>>idx&1) for subset in range(1<<len(optlabels)))
# Explicitly check canonical names/subsets from certificate.
coords=[(r,s) for r in roots for s in root_coords[r]]
assert [list(k) for k in coords]==cert['root_query_coordinates'] and len(coords)==84
ids_set=set(ids);entry=collections.defaultdict(dict)
with B.open() as f:
 for row in csv.DictReader(f):
  k=int(row['config'])
  if k in ids_set:
   key=(int(row['root']),int(row['subset']));entry[k][key]=int(row['cost'])
assert len(entry)==310
origin_reps=cert['source_profile_representatives']
lookup={tuple(entry[k][coord] for coord in coords):j for j,k in enumerate(origin_reps)}
assert len(lookup)==141
rootindex=cert['fixed_queries_zero_based']['named_root']['root_index']
fixed_terminal=cert['fixed_queries_zero_based']['terminal']
assert rootindex==coords.index((5,0))
sig_set={};profile_to_depth={};weighted_depth=collections.Counter();readcounts=collections.Counter();leafids=set()
for config in ids:
 p=tuple(entry[config][coord] for coord in coords)
 profile=lookup[p]
 def terminal_response(q):
  chosen=alloc[q]
  subsets={r:0 for r in roots}
  for label,r in zip(multi,chosen):subsets[r]|=1<<label
  return sum(entry[config][r,subsets[r]] for r in roots)
 fixed=(entry[config][coords[rootindex]],)+(tuple(terminal_response(q) for q in fixed_terminal))
 if fixed in sig_set:assert sig_set[fixed]==profile
 else:sig_set[fixed]=profile
 node=cert['adaptive_tree'];depth=0
 while 'leaf' not in node:
  q=node['action_index']; depth+=1
  if q<144:
   v=terminal_response(q);readcounts['terminal']+=1
  else:
   v=entry[config][coords[q-144]];readcounts['root']+=1
  assert str(v) in node['children']
  node=node['children'][str(v)]
 assert node['leaf']==profile
 assert 1<=depth<=3
 leafids.add(node['leaf']);weighted_depth[depth]+=1
 if profile in profile_to_depth:assert profile_to_depth[profile]==depth
 profile_to_depth[profile]=depth
assert len(sig_set)==141 and len(leafids)==141
assert dict(weighted_depth)=={int(k):v for k,v in cert['adaptive_depth_histogram_source_configs'].items()}
assert dict(readcounts)==cert['adaptive_weighted_root_terminal_reads']
# Check the gauge twins as raw source configurations.
for first,second in ((17928,38165),(24541,38166)):
 assert tuple(entry[first][k] for k in coords)!=tuple(entry[second][k] for k in coords)
 for q in range(144):
  subset={r:0 for r in roots}
  for label,r in zip(multi,alloc[q]):subset[r]|=1<<label
  assert sum(entry[first][r,subset[r]] for r in roots)==sum(entry[second][r,subset[r]] for r in roots)
print('EC49FPY_INDEPENDENT_REPLAY_PASS','configs',len(ids),'profiles',len(leafids),'fixed_signatures',len(sig_set),'adaptive_weighted_depth',dict(weighted_depth),'root_terminal_reads',dict(readcounts),'gauge_pairs',2)