#!/usr/bin/env python3
"""Independent configuration-level replay for EC49FPY. Inputs: master, root CSV, machine certificate.
No imports from the price optimizer; uses the original master and root-cost CSV to replay 310 configurations.
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
assert "prices" in cert and "trees" in cert and "replay" in cert
pR=cert["prices"]["root"];pT=cert["prices"]["terminal"]
assert pR>0 and pT>0 and len(ids)==310 and len(origin_reps)==141
def response(config,q):
 if q>=144:return entry[config][coords[q-144]]
 chosen=alloc[q];subsets={r:0 for r in roots}
 for label,r in zip(multi,chosen):subsets[r]|=1<<label
 return sum(entry[config][r,subsets[r]] for r in roots)
# All legal terminal query outputs coincide for this original configuration pair,
# but full rooted scalar query 148 (root 5, mask 0) differs.
i,j=17928,38165
assert i in ids and j in ids
assert all(response(i,q)==response(j,q) for q in range(144))
assert (response(i,148),response(j,148))==(66,62)
assert lookup[tuple(entry[i][co] for co in coords)]!=lookup[tuple(entry[j][co] for co in coords)]
print("TERMINAL_ONLY_INVISIBLE_WITNESS",i,j,"root_q148",66,62)
for kind in ("uniform","config_weighted"):
 total_weighted=0;per_profile={};hist=collections.Counter()
 weighted_root=weighted_terminal=0
 for config in ids:
  p=tuple(entry[config][co] for co in coords);profile=lookup[p]
  node=cert["trees"][kind];cost=depth=0
  while "leaf" not in node:
   q=node["q"];assert 0<=q<228
   if cert.get("observation_scope","all_228")=="root_only":assert q>=144
   if q>=144:cost+=pR;weighted_root+=1
   else:cost+=pT;weighted_terminal+=1
   depth+=1;node=node["children"][str(response(config,q))]
  assert node["leaf"]==profile
  if profile in per_profile:assert per_profile[profile][0]==cost and per_profile[profile][1]==depth
  else:per_profile[profile]=(cost,depth)
  total_weighted+=cost;hist[depth]+=1
 assert len(per_profile)==141
 total=total_weighted if kind=="config_weighted" else sum(c for c,d in per_profile.values())
 want=cert["optimal_total_config_weighted"] if kind=="config_weighted" else cert["optimal_total_uniform"]
 assert total==want,(kind,total,want)
 assert cert["replay"][kind]["hist_configs"]=={str(k):v for k,v in hist.items()}
 if kind=="uniform":
  rc=tc=0
  for config in origin_reps:
   node=cert["trees"][kind]
   while "leaf" not in node:
    q=node["q"];rc+=q>=144;tc+=q<144;node=node["children"][str(response(config,q))]
 else:rc,tc=weighted_root,weighted_terminal
 assert rc==cert["replay"][kind]["weighted_root_observations"]
 assert tc==cert["replay"][kind]["weighted_terminal_observations"]
 assert pR*rc+pT*tc==total
 print("INDEPENDENT_310_CONFIG_REPLAY_PASS",kind,"cost",total,"root",rc,"terminal",tc,"maxdepth",max(hist))
print("EC49FQA_REPLAY_PASS")
