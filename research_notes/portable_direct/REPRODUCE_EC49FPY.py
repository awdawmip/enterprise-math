#!/usr/bin/env python3
"""EC49FPY complete finite native-BRC observation theorem.
Reproduction: python3 REPRODUCE_EC49FPY.py frozen_original_master.txt EC49FPG_PROFILE.csv output.json
Standard-library only. Integer equality, exhaustive legal domains and observer pairs.
"""
import sys,csv,json,hashlib,itertools,collections,functools
from pathlib import Path
MASTER='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
CSV='a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f'
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
rootnames=(3,5,6,7)
master=Path(sys.argv[1]);csvfile=Path(sys.argv[2]);out=Path(sys.argv[3])
assert hashlib.sha256(master.read_bytes()).hexdigest()==MASTER
assert hashlib.sha256(csvfile.read_bytes()).hexdigest()==CSV
with master.open() as f:
 nk,nw,nconfigs=map(int,f.readline().split());assert (nk,nw,nconfigs)==(94,178850,38169)
 families=[]
 for k in range(nk):
  m=[0]*4
  for _ in range(int(f.readline())):
   l,w=f.readline().split();m[rootnames.index(bytes.fromhex(w)[0])]|=1<<int(l)
  families.append(m)
 configurations=[tuple(map(int,f.readline().split())) for _ in range(nconfigs)]
def domain(configuration):
 res=[0]*24
 for fid in configuration:
  for j,m in enumerate(families[fid]):
   while m:
    x=m&-m;res[x.bit_length()-1]|=1<<j;m^=x
 return tuple(res)
target=domain(configurations[16943]);ids=[i for i,c in enumerate(configurations) if domain(c)==target]
assert len(ids)==310
opts=[l for l in range(24) if target[l].bit_count()>1]
alloc=list(itertools.product(*(tuple(r for j,r in enumerate(rootnames) if target[l]>>j&1) for l in opts)))
assert len(alloc)==144
root_subsets={r:sorted(sum(1<<l for l,b in zip(ol,bs) if b) for bs in itertools.product((0,1),repeat=len(ol))) for r in rootnames for ol in [[l for l in opts if target[l]>>rootnames.index(r)&1]]}
keys=[(r,s) for r in rootnames for s in root_subsets[r]];assert len(keys)==84
idset=set(ids);costs=collections.defaultdict(dict)
with csvfile.open() as f:
 for row in csv.DictReader(f):
  i=int(row['config'])
  if i in idset:
   rs=(int(row['root']),int(row['subset']));assert rs not in costs[i]
   costs[i][rs]=int(row['cost'])
assert len(costs)==310 and all(len(costs[i])==84 for i in ids)
Pclasses={};weights=[];pindex={}
for cid in ids:
 profile=tuple(costs[cid][k] for k in keys)
 if profile not in Pclasses:Pclasses[profile]=len(Pclasses);weights.append(0)
 pindex[cid]=Pclasses[profile];weights[Pclasses[profile]]+=1
profiles=list(Pclasses);reps=[next(i for i in ids if pindex[i]==j) for j in range(len(profiles))]
N=len(profiles);assert N==141 and sum(weights)==310
T=[]
for assignment in alloc:
 masks={r:0 for r in rootnames}
 for l,r in zip(opts,assignment):masks[r]|=1<<l
 T.append(tuple(sum(costs[cid][r,masks[r]] for r in rootnames) for cid in reps))
R=[tuple(costs[cid][k] for cid in reps) for k in keys]
vals=T+R;assert len(vals)==228
# Index all 9870 unordered pairs, then record all pairs unseparated by each scalar observer.
npairs=N*(N-1)//2
same=[];response_groups=[]
for col in vals:
 groups={}
 for j,v in enumerate(col):groups[v]=groups.get(v,0)|(1<<j)
 response_groups.append(groups)
 s=0
 for m in groups.values():
  members=[]
  while m:
   x=m&-m;members.append(x.bit_length()-1);m^=x
  for i,j in itertools.combinations(members,2):
   index=i*(2*N-i-1)//2+j-i-1
   s|=1<<index
 same.append(s)
# The explicit old terminal-gauge pairs have distinct P profiles but the same terminal output.
for a,b in [(17928,38165),(24541,38166)]:
 assert pindex[a]!=pindex[b]
 i=pindex[a];j=pindex[b]
 assert all(col[i]==col[j] for col in T)
assert any(s!=0 for s in same[:144])
# All three-query modality compositions: 0R3T is obstructed by the gauge pairs.
root_T2_count=0
for r in range(84):
 rm=same[144+r]
 for i in range(144):
  im=rm&same[i]
  for j in range(i+1,144):
   if not (im&same[j]):root_T2_count+=1
assert root_T2_count==0
root2_T_count=0
for i in range(84):
 for j in range(i+1,84):
  m=same[144+i]&same[144+j]
  for t in range(144):
   if not (m&same[t]):root2_T_count+=1
assert root2_T_count==0
root3_count=0
for i in range(84):
 for j in range(i+1,84):
  m=same[144+i]&same[144+j]
  for k in range(j+1,84):
   if not (m&same[144+k]):root3_count+=1
assert root3_count==0
# Explicit fixed upper bound: root05 empty, 3 terminal queries (indices 66,72,106).
baseline=keys.index((5,0));terminal_indices=(66,72,106)
selected=(144+baseline,)+terminal_indices
assert not (same[selected[0]]&same[selected[1]]&same[selected[2]]&same[selected[3]])
assert len({tuple(vals[q][i] for q in selected) for i in range(N)})==N
# Worst-case adaptive depth <=3: exact exhaustive depth-one and depth-two decisions.
@functools.lru_cache(None)
def state_pairs(mask):
 members=[]
 while mask:
  x=mask&-mask;members.append(x.bit_length()-1);mask^=x
 outmask=0
 for i,j in itertools.combinations(members,2):outmask|=1<<(i*(2*N-i-1)//2+j-i-1)
 return outmask
@functools.lru_cache(None)
def one(mask):
 if mask.bit_count()<=1:return -1
 pair=state_pairs(mask)
 for q,collisions in enumerate(same):
  if pair&collisions==0:return q
 return None
@functools.lru_cache(None)
def two(mask):
 if mask.bit_count()<=1:return (-1,{})
 ans=one(mask)
 if ans is not None:return (ans,{})
 for q,groups in enumerate(response_groups):
  fibers={v:g&mask for v,g in groups.items() if g&mask}
  if len(fibers)<=1:continue
  if all(one(m) is not None for m in fibers.values()):
   return (q,{str(v):one(m) for v,m in fibers.items()})
 return None
FULL=(1<<N)-1
assert two(FULL) is None
first=None
for q,groups in enumerate(response_groups):
 fibers={v:g for v,g in groups.items() if g}
 if len(fibers)<=1:continue
 if all(two(m) is not None for m in fibers.values()):first=q;break
assert first==0
# Recursively build the full explicit decision certificate.
def tree(mask,level):
 if mask.bit_count()==1:return {'leaf':mask.bit_length()-1}
 if level==1:q=one(mask)
 elif level==2:
  v=two(mask);q=v[0] if v is not None else None
 else:q=first
 assert q is not None and q>=0
 children={str(v):tree(m,level-1) for v,g in response_groups[q].items() if (m:=g&mask)}
 assert len(children)>1
 return {'action_index':q,'children':children}
certtree=tree(FULL,3)
per_state_depth=[];weighted_depth=collections.Counter();used_queries=collections.Counter()
for i in range(N):
 node=certtree;depth=0
 while 'leaf' not in node:
  q=node['action_index'];depth+=1;used_queries['root' if q>=144 else 'terminal']+=weights[i]
  node=node['children'][str(vals[q][i])]
 assert node['leaf']==i and depth<=3
 per_state_depth.append(depth);weighted_depth[depth]+=weights[i]
assert max(per_state_depth)==3
assert weighted_depth[2]+weighted_depth[3]==310
payload={'schema':'EC49FPY_CLASS16943_FIXED4_ADAPTIVE3_V1','scientific_commit':PIN,'master_sha256':MASTER,'root_cost_table_sha256':CSV,'root_domain_representative':16943,'source_configurations':310,'distinct_named_root_profiles':N,'terminal_queries':144,'named_root_queries':84,'source_profile_representatives':reps,'profile_weights':weights,'root_query_coordinates':[list(k) for k in keys], 'fixed_min_total_scalar_queries':4,'fixed_min_terminal_given_exactly_one_root':3,'fixed_queries_zero_based':{'terminal':list(terminal_indices),'named_root':{'root':5,'optional_subset_mask':0,'root_index':baseline}},'fixed_signature_count':N,'infeasible_3_query_compositions':{'all_terminal':'two explicit terminal-invisible named-root pairs','one_root_two_terminal':{'combination_count':84*144*143//2,'successful':root_T2_count},'two_root_one_terminal':{'combination_count':84*83//2*144,'successful':root2_T_count},'all_root':{'combination_count':84*83*82//6,'successful':root3_count}},'adaptive_minimum_worst_depth':3,'adaptive_depth2_all_first_queries_checked':228,'adaptive_first_query_zero_based':first,'adaptive_depth_histogram_profiles':dict(collections.Counter(per_state_depth)),'adaptive_depth_histogram_source_configs':dict(weighted_depth),'adaptive_weighted_root_terminal_reads':dict(used_queries),'adaptive_tree':certtree,'exact_method':'All state-pair collision bitsets; complete finite observation action enumeration; depth-2 exhaustive response-fiber test; verified 141-leaf depth-3 tree','status':'AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED'}
out.write_text(json.dumps(payload,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
print('EC49FPY_FULL_EXACT_PASS','rooted',N,'configs',len(ids),'three_query_impossible', '1R2T',root_T2_count,'2R1T',root2_T_count,'3R',root3_count,'depth2_impossible',two(FULL) is None,'adaptive_first',first,'adaptive_weighted_depth',dict(weighted_depth),'root_terminal_reads',dict(used_queries),'sha256',hashlib.sha256(out.read_bytes()).hexdigest())