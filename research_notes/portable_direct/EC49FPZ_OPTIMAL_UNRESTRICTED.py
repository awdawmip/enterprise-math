#!/usr/bin/env python3
"""Class 16943 exact optimal expected observation cost, worst depth <=3.
Standard library, integer arithmetic, 228 native legal scalar observations.
Invocation: python EC49FPZ_OPTIMAL_EXPECTATION3.py ORIGINAL_MASTER ROOT_COST_CSV CERT_OUT
"""
import sys,csv,json,hashlib,itertools,collections,functools,time
from pathlib import Path
start=time.monotonic()
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
vals=T+R;Q=len(vals);assert Q==228
FULL=(1<<N)-1
response_groups=[]
for v in vals:
 groups={}
 for i,x in enumerate(v):groups[x]=groups.get(x,0)|(1<<i)
 response_groups.append(groups)
partitions=[tuple(sorted(g.values())) for g in response_groups]
print('loaded',N,Q, 'seconds',round(time.monotonic()-start,2),flush=True)
INF=10**9
@functools.lru_cache(None)
def weight(mask):
 return sum(weights[i] for i in bits(mask))
def bits(m):
 while m:
  x=m&-m;yield x.bit_length()-1;m^=x
@functools.lru_cache(None)
def can_one(mask):
 if mask.bit_count()<=1:return -1
 for q,gm in enumerate(response_groups):
  if all((m & mask).bit_count()<=1 for m in gm.values()):return q
 return None
@functools.lru_cache(None)
def two(mask):
 n=mask.bit_count()
 if n<=1:return (0,0,-1,-1)
 best_u,best_w=INF,INF;qu,qw=-1,-1
 tested=set()
 for q,gm in enumerate(response_groups):
  branch=tuple(sorted(x for m in gm.values() if (x:=m&mask)))
  if len(branch)==1 or branch in tested:continue
  tested.add(branch)
  if all(can_one(x) is not None for x in branch):
   u=n+sum(x.bit_count() for x in branch if x.bit_count()>1)
   w=weight(mask)+sum(weight(x) for x in branch if x.bit_count()>1)
   if u<best_u:best_u,qu=u,q
   if w<best_w:best_w,qw=w,q
   if best_u==n and best_w==weight(mask):break
 return best_u,best_w,qu,qw
first_u=[];first_w=[]
for q,gm in enumerate(response_groups):
 branch=tuple(sorted(gm.values()))
 if len(branch)<=1: first_u.append(INF);first_w.append(INF);continue
 children=[two(x) for x in branch if x.bit_count()>1]
 first_u.append(N+sum(c[0] for c in children))
 first_w.append(sum(weights)+sum(c[1] for c in children))
 if q%20==0:print('first',q,'best',min(first_u),min(first_w),'two_cache',two.cache_info().currsize,'t',round(time.monotonic()-start,2),flush=True)
# Exact unlimited-depth Bellman recursion. A query incurs each profile/config weight
# once; residual non-singleton fibers require at least one additional query.
@functools.lru_cache(None)
def infinite(mask):
 n=mask.bit_count()
 if n<=1:return (0,0,-1,-1)
 au,aw,qu,qw=two(mask)
 best_u,best_w=au,aw
 if mask==FULL:
  best_u,best_w=min(first_u),min(first_w)
  qu,qw=first_u.index(best_u),first_w.index(best_w)
 seen=set()
 for q,gm in enumerate(response_groups):
  sub=tuple(sorted(x for m in gm.values() if (x:=m&mask)))
  if len(sub)<=1 or sub in seen:continue
  seen.add(sub)
  nontrivial=[x for x in sub if x.bit_count()>1]
  lowu=n+sum(x.bit_count() for x in nontrivial)
  loww=weight(mask)+sum(weight(x) for x in nontrivial)
  if lowu>=best_u and loww>=best_w:continue
  su=n;sw=weight(mask)
  for x in nontrivial:
   cu,cw,_,_=infinite(x)
   su+=cu;sw+=cw
  if su<best_u:best_u,qu=su,q
  if sw<best_w:best_w,qw=sw,q
  if best_u==n and best_w==weight(mask):break
 return (best_u,best_w,qu,qw)
print('start full Bellman',flush=True)
ibest=infinite(FULL)
print('UNRESTRICTED',ibest,'memo',infinite.cache_info().currsize,'t',round(time.monotonic()-start,2),flush=True)
# Determine all optimal initial observations, using globally exact solutions on fibers.
inf_first_u=[];inf_first_w=[]
for q,gm in enumerate(response_groups):
 children=[infinite(x) for x in gm.values() if x.bit_count()>1]
 inf_first_u.append(N+sum(z[0] for z in children))
 inf_first_w.append(sum(weights)+sum(z[1] for z in children))
assert min(inf_first_u)==ibest[0] and min(inf_first_w)==ibest[1]
print('UNRESTRICTED FIRST', [i for i,x in enumerate(inf_first_u) if x==ibest[0]],[i for i,x in enumerate(inf_first_w) if x==ibest[1]],flush=True)
u=min(first_u);w=min(first_w);assert u<INF and w<INF
opt_u=[q for q,x in enumerate(first_u) if x==u]
opt_w=[q for q,x in enumerate(first_w) if x==w]
print('RESULT',u,'/',N,w,'/',sum(weights),'opt first',opt_u,opt_w,'t',round(time.monotonic()-start,2),flush=True)
# Full zero-based response-index trees; recursive witness for each prior, each subtree chooses best q.
def build(mask,d,weighted,q=None):
 if mask.bit_count()==1:return {'leaf':mask.bit_length()-1}
 if q is None:
  if d==1:q=can_one(mask)
  elif d==2:q=two(mask)[3 if weighted else 2]
  else:raise ValueError('unexpected depth')
 assert q is not None and q>=0
 children={str(v):build(m&mask,d-1,weighted) for v,m in sorted(response_groups[q].items()) if (m&mask)}
 assert len(children)>1
 return {'q':q,'children':children}
trees={'uniform':build(FULL,3,False,opt_u[0]),'config_weighted':build(FULL,3,True,opt_w[0])}
checks={}
for prior,tree in trees.items():
 hist=collections.Counter();weighted_hist=collections.Counter();qtypes=collections.Counter();total=0;seen=set()
 for i in range(N):
  node=tree;depth=0
  while 'leaf' not in node:
   q=node['q'];depth+=1;qtypes['named_root' if q>=144 else 'terminal']+=weights[i]
   node=node['children'][str(vals[q][i])]
  assert node['leaf']==i and depth<=3
  hist[depth]+=1;weighted_hist[depth]+=weights[i]
  total+=depth*(weights[i] if prior=='config_weighted' else 1)
 assert sum(hist.values())==N and sum(weighted_hist.values())==310
 assert total==(w if prior=='config_weighted' else u)
 checks[prior]={'total':total,'hist_profiles':dict(hist),'hist_configs':dict(weighted_hist),'weighted_query_modalities':dict(qtypes)}
cert={'schema':'EC49FPZ_CLASS16943_DEPTH3_EXACT_EXPECTATION_V1','frozen_scientific_commit':PIN,'source_master_sha256':MASTER,'native_root_costs_sha256':CSV,'domain_rep':16943,'config_count':310,'profile_count':N,'terminal_actions':144,'named_root_actions':84,'first_query_costs_uniform':first_u,'first_query_costs_weighted':first_w,'optimal_first_queries_uniform':opt_u,'optimal_first_queries_config_weighted':opt_w,'minimum_total_uniform':u,'minimum_total_config_weighted':w,'max_depth':3,'weights':weights,'reps':reps,'root_coordinates':[list(k) for k in keys], 'trees':trees,'replay':checks,'memo_sizes':{'one':can_one.cache_info().currsize,'two':two.cache_info().currsize},'duration_seconds':round(time.monotonic()-start,3),'unrestricted_global_min_uniform':ibest[0],'unrestricted_global_min_config_weighted':ibest[1],'unrestricted_opt_first_uniform':[i for i,x in enumerate(inf_first_u) if x==ibest[0]],'unrestricted_opt_first_weighted':[i for i,x in enumerate(inf_first_w) if x==ibest[1]],'unrestricted_first_costs_uniform':inf_first_u,'unrestricted_first_costs_weighted':inf_first_w,'unrestricted_Bellman_states':infinite.cache_info().currsize,'status':'AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED'}
out.write_text(json.dumps(cert,sort_keys=True,ensure_ascii=False,indent=2)+'\n')
print('SAVED',out,'sha256',hashlib.sha256(out.read_bytes()).hexdigest(),'cache',cert['memo_sizes'],flush=True)
