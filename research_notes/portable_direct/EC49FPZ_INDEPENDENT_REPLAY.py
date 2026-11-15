#!/usr/bin/env python3
"""Independent configuration-level replay for EC49FPY. Inputs: master, root CSV, machine certificate.
No imports from REPRODUCE_EC49FPY, no scipy/numpy; validates all 310 original configs.
"""
import sys,csv,json,itertools,collections,hashlib
from pathlib import Path
A=Path(sys.argv[1]);B=Path(sys.argv[2]);C=Path(sys.argv[3]);cert=json.loads(C.read_text())
assert hashlib.sha256(A.read_bytes()).hexdigest()==cert['source_master_sha256']
assert hashlib.sha256(B.read_bytes()).hexdigest()==cert['native_root_costs_sha256']
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
assert [list(k) for k in coords]==cert['root_coordinates'] and len(coords)==84
ids_set=set(ids);entry=collections.defaultdict(dict)
with B.open() as f:
 for row in csv.DictReader(f):
  k=int(row['config'])
  if k in ids_set:
   key=(int(row['root']),int(row['subset']));entry[k][key]=int(row['cost'])
assert len(entry)==310
origin_reps=cert['reps']
lookup={tuple(entry[k][coord] for coord in coords):j for j,k in enumerate(origin_reps)}
assert len(lookup)==141
# Independent replay all original 310 configurations for two optimal trees.
for kind in ('uniform','config_weighted'):
 sig_set=set();depth_hist=collections.Counter();root_reads=0;terminal_reads=0;depth_by_profile={}
 for config in ids:
  p=tuple(entry[config][coord] for coord in coords);profile=lookup[p]
  def response(q):
   if q>=144:return entry[config][coords[q-144]]
   chosen=alloc[q];subsets={r:0 for r in roots}
   for label,r in zip(multi,chosen):subsets[r]|=1<<label
   return sum(entry[config][r,subsets[r]] for r in roots)
  node=cert['trees'][kind];depth=0
  while 'leaf' not in node:
   q=node['q'];depth+=1
   if q>=144:root_reads+=1
   else:terminal_reads+=1
   node=node['children'][str(response(q))]
  assert node['leaf']==profile and depth<=3
  depth_hist[depth]+=1;sig_set.add(profile)
  if profile in depth_by_profile:assert depth_by_profile[profile]==depth
  depth_by_profile[profile]=depth
 assert len(sig_set)==141
 if kind=='config_weighted':assert sum(k*v for k,v in depth_hist.items())==cert['minimum_total_config_weighted']
 else:assert sum(depth_by_profile.values())==cert['minimum_total_uniform']
 assert cert['replay'][kind]['hist_configs']=={str(k):v for k,v in depth_hist.items()}
 assert cert['replay'][kind]['weighted_query_modalities']=={'named_root':root_reads,'terminal':terminal_reads}
 print('INDEPENDENT_CONFIG_REPLAY_PASS',kind,'configs',len(ids),'profiles',len(sig_set),'hist',dict(depth_hist),'reads',root_reads,terminal_reads)
print('EC49FPZ_INDEPENDENT_REPLAY_ALL_PASS')
