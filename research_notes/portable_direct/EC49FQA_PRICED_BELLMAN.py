#!/usr/bin/env python3
"""EC49FQA: exact unrestricted priced native BRC class 16943.
Usage: python EC49FQA_PRICED_BELLMAN.py MASTER ROOT_CSV OUTPUT_JSON R_PRICE T_PRICE [--root-only]
All integer-positive prices, finite exact Bellman; same frozen source as EC49FPZ.
"""
import sys,csv,json,hashlib,itertools,collections,functools,time
from pathlib import Path
start=time.monotonic()
MASTER='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
CSV='a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f'
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
rootnames=(3,5,6,7)
master=Path(sys.argv[1]);csvfile=Path(sys.argv[2]);out=Path(sys.argv[3]);R_PRICE,T_PRICE=map(int,sys.argv[4:6]);assert R_PRICE>0 and T_PRICE>0
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
price=(T_PRICE,)*144+(R_PRICE,)*84
MIN_PRICE=min(R_PRICE,T_PRICE)
queries_by_partition={}
for q,p in enumerate(partitions):
 old=queries_by_partition.get(p)
 if old is None or (price[q],q)<(price[old],old):queries_by_partition[p]=q
eligible_q=sorted(queries_by_partition.values())
ONLY_ROOT=len(sys.argv)>6 and sys.argv[6]=="--root-only"
if ONLY_ROOT:eligible_q=[q for q in eligible_q if q>=144]
print("loaded",N,Q,"partitions",len(eligible_q),"root-price",R_PRICE,"terminal-price",T_PRICE,flush=True)
def bits(m):
 while m:
  x=m&-m;yield x.bit_length()-1;m^=x
@functools.lru_cache(None)
def weight(mask):
 return sum(weights[i] for i in bits(mask))
INF=10**12
@functools.lru_cache(None)
def one(mask):
 if mask.bit_count()<=1:return (0,-1)
 best=(INF,-1)
 for q in eligible_q:
  if all((m&mask).bit_count()<=1 for m in response_groups[q].values()):
   if price[q]<best[0]:best=(price[q],q)
   if price[q]==MIN_PRICE:break
 return best
@functools.lru_cache(None)
def two(mask):
 if mask.bit_count()<=1:return (0,0,-1,-1)
 n=mask.bit_count();w=weight(mask)
 bestu=bestw=INF;qu=qw=-1
 for q in eligible_q:
  branch=[x for m in response_groups[q].values() if (x:=m&mask)]
  if len(branch)<=1:continue
  children=[(x,one(x)) for x in branch if x.bit_count()>1]
  if any(c[1][1]<0 for c in children):continue
  cu=price[q]*n+sum(x.bit_count()*c[0] for x,c in children)
  cw=price[q]*w+sum(weight(x)*c[0] for x,c in children)
  if cu<bestu:bestu,qu=cu,q
  if cw<bestw:bestw,qw=cw,q
  if bestu==MIN_PRICE*n and bestw==MIN_PRICE*w:break
 return bestu,bestw,qu,qw
@functools.lru_cache(None)
def optimum(mask):
 if mask.bit_count()<=1:return (0,0,-1,-1)
 n=mask.bit_count();w=weight(mask)
 bestu,bestw,qu,qw=two(mask)
 for q in eligible_q:
  branch=[x for m in response_groups[q].values() if (x:=m&mask)]
  if len(branch)<=1:continue
  nontrivial=[x for x in branch if x.bit_count()>1]
  lowu=price[q]*n+MIN_PRICE*sum(x.bit_count() for x in nontrivial)
  loww=price[q]*w+MIN_PRICE*sum(weight(x) for x in nontrivial)
  if lowu>=bestu and loww>=bestw:continue
  su=price[q]*n;sw=price[q]*w
  for x in nontrivial:
   cu,cw,_,_=optimum(x);su+=cu;sw+=cw
  if su<bestu:bestu,qu=su,q
  if sw<bestw:bestw,qw=sw,q
  if bestu==MIN_PRICE*n and bestw==MIN_PRICE*w:break
 return bestu,bestw,qu,qw
result=optimum(FULL)
first_u=[];first_w=[]
for q,gm in enumerate(response_groups):
 sub=list(gm.values())
 if q not in eligible_q or len(sub)<=1:
  first_u.append(INF);first_w.append(INF);continue
 child=[optimum(x) for x in sub if x.bit_count()>1]
 first_u.append(price[q]*N+sum(c[0] for c in child))
 first_w.append(price[q]*sum(weights)+sum(c[1] for c in child))
assert min(first_u)==result[0] and min(first_w)==result[1]
def build(mask,weighted,q=None):
 if mask.bit_count()==1:return {"leaf":mask.bit_length()-1}
 if q is None:q=optimum(mask)[3 if weighted else 2]
 assert q>=0
 child={str(v):build(m&mask,weighted) for v,m in sorted(response_groups[q].items()) if (m&mask)}
 assert len(child)>1
 return {"q":q,"children":child}
opt_first_u=[i for i,x in enumerate(first_u) if x==result[0]]
opt_first_w=[i for i,x in enumerate(first_w) if x==result[1]]
trees={"uniform":build(FULL,False,opt_first_u[0]),"config_weighted":build(FULL,True,opt_first_w[0])}
checks={}
for prior,tree in trees.items():
 hist=collections.Counter();w_hist=collections.Counter();rootcount=terminalcount=total=0
 for i in range(N):
  node=tree;depth=cost=0
  while "leaf" not in node:
   q=node["q"];depth+=1;cost+=price[q]
   if q>=144:rootcount+=weights[i] if prior=="config_weighted" else 1
   else:terminalcount+=weights[i] if prior=="config_weighted" else 1
   node=node["children"][str(vals[q][i])]
  assert node["leaf"]==i
  hist[depth]+=1;w_hist[depth]+=weights[i]
  total+=cost*(weights[i] if prior=="config_weighted" else 1)
 assert total==result[1 if prior=="config_weighted" else 0]
 checks[prior]={"total_integer_cost":total,"hist_profiles":dict(hist),"hist_configs":dict(w_hist),"weighted_root_observations":rootcount,"weighted_terminal_observations":terminalcount,"max_depth":max(hist)}
cert={"schema":"EC49FQA_CLASS16943_MIXED_COST_UNRESTRICTED_V1","frozen_scientific_commit":PIN,"source_master_sha256":MASTER,"native_root_costs_sha256":CSV,"domain_rep":16943,"config_count":310,"profile_count":141,"terminal_actions":144,"named_root_actions":84,"prices":{"root":R_PRICE,"terminal":T_PRICE},"observation_scope":"root_only" if ONLY_ROOT else "all_228","optimal_total_uniform":result[0],"optimal_total_config_weighted":result[1],"optimal_first_uniform":opt_first_u,"optimal_first_config_weighted":opt_first_w,"first_query_costs_uniform":first_u,"first_query_costs_weighted":first_w,"trees":trees,"replay":checks,"memo_sizes":{"one":one.cache_info().currsize,"two":two.cache_info().currsize,"unrestricted":optimum.cache_info().currsize},"duration_seconds":round(time.monotonic()-start,3),"reps":reps,"weights":weights,"root_coordinates":[list(k) for k in keys],"status":"AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED"}
out.write_text(json.dumps(cert,sort_keys=True,ensure_ascii=False,indent=2)+"\n")
print("EC49FQA_EXACT_FINITE_PASS",R_PRICE,T_PRICE,"root_only",ONLY_ROOT,"totals",result[:2],"first",opt_first_u,opt_first_w,"Bellman",optimum.cache_info().currsize,"seconds",round(time.monotonic()-start,2),flush=True)
