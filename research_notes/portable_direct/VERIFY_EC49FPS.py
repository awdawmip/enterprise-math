#!/usr/bin/env python3
"""EC49FPR: exhaustive exact Bellman proof for class16995, root-price = terminal-price/2.
Data: frozen_original_master.txt, EC49FPG_PROFILE.csv, EC49FPL_CERTIFICATE.json,
      EC49FPN_CERTIFICATE.json from the SHA-verified EC49FPQ/EC49FPL-FPN evidence bundles.
No external network, floating-point optimization, or historical session needed.
"""
#!/usr/bin/env python3
"""EC49FPQ: complete finite mixed sensing class16995 proof.
Input: frozen_original_master.txt, EC49FPG_PROFILE.csv, EC49FPL_CERTIFICATE.json, EC49FPN_CERTIFICATE.json.
All 324 complete-allocation terminal and 96 reachable named-root/subset scalar observations.
Both observational types have unit cost; 112 rooted profiles (or 242 source weights).
"""
import collections,csv,functools,hashlib,itertools,json,sys
from pathlib import Path
base=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).parent
out=Path(sys.argv[2]) if len(sys.argv)>2 else Path('EC49FPR_HALF_ROOT_MACHINE_CERT.json')
master=base/'frozen_original_master.txt'; table=base/'EC49FPG_PROFILE.csv'
MASTER_HASH='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
COST_HASH='a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f'
assert hashlib.sha256(master.read_bytes()).hexdigest()==MASTER_HASH
assert hashlib.sha256(table.read_bytes()).hexdigest()==COST_HASH
roots=(3,5,6,7)
with master.open() as f:
    nk,nw,nc=map(int,f.readline().split());assert (nk,nw,nc)==(94,178850,38169)
    family=[];count=0
    for _ in range(nk):
        fam=[0]*4;n=int(f.readline());count+=n
        for __ in range(n):
            l,word=f.readline().split();r=bytes.fromhex(word)[0]
            fam[roots.index(r)]|=1<<int(l)
        family.append(fam)
    assert count==nw
    configs=[tuple(map(int,f.readline().split())) for _ in range(nc)]

def domain(keys):
    sig=[0]*24
    for k in keys:
        for j,mask in enumerate(family[k]):
            while mask:
                low=mask&-mask;sig[low.bit_length()-1]|=1<<j;mask^=low
    assert all(sig)
    return tuple(sig)

rep=16995;target=domain(configs[rep]);ids=[i for i,ks in enumerate(configs) if domain(ks)==target]
assert len(ids)==242 and ids[0]==16995
idset=set(ids)
opt=[l for l in range(24) if target[l].bit_count()>1]
actions=list(itertools.product(*[tuple(r for j,r in enumerate(roots) if (target[l]>>j)&1) for l in opt]))
assert len(actions)==324
coordinate_subsets={r:sorted(sum(1<<l for l,b in zip(ropts,bs) if b) for bs in itertools.product((0,1),repeat=len(ropts))) for r in roots for ropts in [[l for l in opt if target[l]>>(roots.index(r))&1]]}
assert sum(len(x) for x in coordinate_subsets.values())==96
entries=collections.defaultdict(dict)
with table.open() as f:
    for row in csv.DictReader(f):
        config=int(row['config'])
        if config in idset:
            key=int(row['root']),int(row['subset'])
            assert key not in entries[config]
            entries[config][key]=(int(row['cost']),int(row['must']),int(row['opt']))
assert set(entries)==idset
Pclasses={};Tclasses={};terminal={}
for i in ids:
    e=entries[i];p=[]
    for j,r in enumerate(roots):
        must=sum(1<<l for l,v in enumerate(target) if v==(1<<j))
        optmask=sum(1<<l for l in opt if target[l]>>j&1)
        for sub in coordinate_subsets[r]:
            val,m,o=e[r,sub];assert (m,o)==(must,optmask)
            p.append(val)
    p=tuple(p)
    res=[]
    for assignment in actions:
        subsets={r:0 for r in roots}
        for label,r in zip(opt,assignment):subsets[r]|=1<<label
        res.append(sum(e[r,subsets[r]][0] for r in roots))
    t=tuple(res);terminal[i]=t
    Pclasses.setdefault(p,i)
    Tclasses.setdefault(t,i)
assert len(Pclasses)==len(Tclasses)==112
assert len({terminal[i] for i in Pclasses.values()})==112
profile_source_ids=list(Pclasses.values());N=len(profile_source_ids);Q=len(actions)
rows=[terminal[i] for i in profile_source_ids]
values=[[r[q] for r in rows] for q in range(Q)]
FULL=(1<<N)-1;INF=10**9


def bits(mask):
    while mask:
        low=mask&-mask
        yield low.bit_length()-1
        mask^=low

# Extend terminal responses by every root/subset scalar readout, retaining source keys.
all_actions=[['T',q] for q in range(Q)]
all_values=[tuple(v) for v in values]
for r in roots:
    for sub in coordinate_subsets[r]:
        all_actions.append(['R',r,sub])
        all_values.append(tuple(entries[i][r,sub][0] for i in profile_source_ids))
assert len(all_actions)==420
all_groups=[];indices=[];seen_full=set()
for q,vec in enumerate(all_values):
    d={}
    for i,v in enumerate(vec):d[v]=d.get(v,0)|(1<<i)
    g=tuple(sorted(d.values()))
    if g not in seen_full:
        seen_full.add(g);all_groups.append(g);indices.append(q)
assert len(indices)==395
import time
weights_unif=tuple([1]*N)
weights_src=tuple(collections.Counter(terminal.values())[terminal[i]] for i in profile_source_ids)
FPL=json.loads((base/'EC49FPL_CERTIFICATE.json').read_text());FPN=json.loads((base/'EC49FPN_CERTIFICATE.json').read_text())
# one concrete exact-price case, scaling by 2
qcosts=tuple(2 if all_actions[ix][0]=='T' else 1 for ix in indices)
# Validate distinct partitions do not silently discard same partition different price
partition_options={}
for i,a in enumerate(all_actions):
    vs=all_values[i]; d={}
    for k,v in enumerate(vs):d[v]=d.get(v,0)|(1<<k)
    part=tuple(sorted(d.values()))
    if part not in partition_options or (1 if a[0]=='R' else 2)<partition_options[part][0]:
       partition_options[part]=((1 if a[0]=='R' else 2),i)
assert len(partition_options)==395
indices=list(index[1] for index in partition_options.values());
qcosts=tuple(1 if all_actions[ix][0]=='R' else 2 for ix in indices)
all_groups=[]
for ix in indices:
    d={}
    for k,v in enumerate(all_values[ix]):d[v]=d.get(v,0)|(1<<k)
    all_groups.append(tuple(sorted(d.values())))
@functools.lru_cache(None)
def partitions(mask,qi):
    return tuple(x for g in all_groups[qi] if (x:=g&mask))


from fractions import Fraction
from collections import Counter
rootcert=json.loads((base/'EC49FPR_HALF_ROOT_MACHINE_CERT.json').read_text())
weight_src=tuple(FPN['weights_per_rooted_profile'])
assert weight_src==weights_src and sum(weights_src)==242
base_tree=rootcert['uniform_rooted_profile']['tree']
# A complete, reusable proven witness, not an upper-bound guess.
def base_cost(mask, node, mass_func):
    if mask.bit_count()<=1:return 0
    q=node['action_index'];bucket={}
    for k in bits(mask):
        v=all_values[q][k]
        bucket[v]=bucket.get(v,0)|(1<<k)
    if len(bucket)==1:
        k,b=next(iter(bucket.items()))
        return base_cost(b,node['children'][str(k)],mass_func)
    cost=1 if all_actions[q][0]=='R' else 2
    return cost*mass_func(mask)+sum(base_cost(b,node['children'][str(v)],mass_func) for v,b in bucket.items() if b.bit_count()>1)
@functools.lru_cache(None)
def mass(mask):
    s=0
    while mask:
        lb=mask&-mask;s+=weight_src[lb.bit_length()-1];mask^=lb
    return s
assert base_cost(FULL,base_tree,mass)==850
# cache of best score for every candidate mask, exact positive-cost tree recurrence
allq=range(len(indices))
@functools.lru_cache(None)
def C(mask):
    if mask.bit_count()<=1:return 0
    m=mass(mask)
    best=base_cost(mask,base_tree,mass)
    # admissible bound lets us prioritize high-yield actions, but never discard a potentially improving action
    candidates=[]
    for qi in allq:
        fs=partitions(mask,qi)
        if len(fs)<2:continue
        child=[f for f in fs if f.bit_count()>1]
        lb=qcosts[qi]*m+sum(mass(f) for f in child)
        if lb < best:
            candidates.append((lb,qi,child))
    candidates.sort(key=lambda x:x[0])
    for lb,qi,child in candidates:
        if lb>=best:break
        cost=qcosts[qi]*m
        # large first improves early branch-and-bound
        for f in sorted(child,key=mass,reverse=True):
            cost+=C(f)
            if cost>=best:break
        if cost<best:best=cost
        if best==m:break
    return best
start=time.time()
result=C(FULL)
print('WEIGHTED_SCALED',result,'DEN',2*sum(weights_src),'fraction',str(Fraction(result,2*sum(weights_src))),'MEMO',C.cache_info(),'SEC',round(time.time()-start,3),flush=True)
all_first=[]
for qi in allq:
    fs=partitions(FULL,qi)
    if len(fs)<2:
        all_first.append(None)
    else:
        all_first.append(qcosts[qi]*mass(FULL)+sum(C(f) for f in fs if f.bit_count()>1))
assert min(x for x in all_first if x is not None)==result
best_first_original=[indices[qi] for qi,v in enumerate(all_first) if v==result]
# exact witness builder; tie-break by least original sensor index
@functools.lru_cache(None)
def build(mask):
    if mask.bit_count()==1:return {'leaf':next(bits(mask))}
    cur=C(mask)
    for qi in sorted(allq,key=lambda j:indices[j]):
        fs=partitions(mask,qi)
        if len(fs)<2:continue
        cost=qcosts[qi]*mass(mask)+sum(C(f) for f in fs if f.bit_count()>1)
        if cost==cur:
            r={}
            for i in bits(mask):
                v=all_values[indices[qi]][i]
                r[v]=r.get(v,0)|(1<<i)
            return {'action_index':indices[qi],'action':all_actions[indices[qi]],'children':{str(v):build(f) for v,f in sorted(r.items())}}
    raise AssertionError('cannot build witness')
tree=build(FULL)
hist=Counter();total=0;paths=set();unweighted=Counter();depth_hist=Counter()
for i in range(N):
    curr=tree;price=0;depth=0;path=[]
    while 'leaf' not in curr:
        q=curr['action_index'];v=all_values[q][i]
        price+=1 if all_actions[q][0]=='R' else 2
        depth+=1;path.append((q,v));curr=curr['children'][str(v)]
    assert curr['leaf']==i
    assert tuple(path) not in paths
    paths.add(tuple(path));hist[price]+=weights_src[i];total+=price*weights_src[i];unweighted[price]+=1;depth_hist[depth]+=weights_src[i]
assert len(paths)==112 and total==result
payload={'schema':'EC49FPS_ORIGINAL_CONFIGURATION_WEIGHTED_MIXED_HALFPRICE_EXACT_V1',
'science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
'original_master_sha256':MASTER_HASH,'root_cost_table_sha256':COST_HASH,
'base_proof':'EC49FPR', 'prior':'Uniform on 242 original source configurations; 112 rooted profiles carry multiplicities',
'profile_weights':weight_src,'source_configurations':242,'rooted_profiles':N,'sensor_indices':len(all_actions),
'distinct_response_partitions':len(indices),'scaled_costs':{'T':2,'R':1},
'optimal_scaled_sum':result,'total_mass':242,'expected_price_fraction':str(Fraction(result,484)),
'optimal_first_original_indices':best_first_original,
'optimal_first_original_actions':[[i,all_actions[i]] for i in best_first_original],
'weighted_price_histogram':sorted(hist.items()),'profile_price_histogram':sorted(unweighted.items()),
'weighted_depth_histogram':sorted(depth_hist.items()), 'bellman_masks':C.cache_info().currsize,
'all_first_action_costs':all_first,'canonical_action_indices':indices,'profile_source_ids':profile_source_ids,'tree':tree,
'exact_method':'Integer Bellman recurrence, base feasible root/terminal policy, admissible scaled child-mass lower bounds, complete root enumeration and leaf walk; all exact integer responses',
'scientific_status':'AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED'}
out=Path(sys.argv[2]) if len(sys.argv)>2 else Path('EC49FPS_CONFIG_WEIGHTED_HALF_PRICE_CERT.json')
out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print('FIRST',best_first_original,'HIST',sorted(hist.items()),'CERT',out,hashlib.sha256(out.read_bytes()).hexdigest(),flush=True)
