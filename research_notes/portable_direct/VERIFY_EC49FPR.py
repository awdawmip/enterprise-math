#!/usr/bin/env python3
"""EC49FPR: exact expected-price optimum for half-price rooted readouts, original class16995.
Usage: python VERIFY_EC49FPR.py EVIDENCE_DIR [CERTIFICATE_JSON]
Inputs: frozen_original_master.txt, EC49FPG_PROFILE.csv (original native cost table).
"""
import collections,csv,functools,hashlib,itertools,json,sys
from pathlib import Path
base=Path(sys.argv[1])
out=Path(sys.argv[2]) if len(sys.argv)>2 else Path("EC49FPR_HALF_ROOT_MACHINE_CERT.json")
master=base/"frozen_original_master.txt"
table=base/"EC49FPG_PROFILE.csv"
MASTER_HASH="cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
COST_HASH="a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f"
assert hashlib.sha256(master.read_bytes()).hexdigest()==MASTER_HASH
assert hashlib.sha256(table.read_bytes()).hexdigest()==COST_HASH
roots=(3,5,6,7)
with master.open() as f:
    nk,nw,nc=map(int,f.readline().split())
    assert (nk,nw,nc)==(94,178850,38169)
    family=[];count=0
    for _ in range(nk):
        masks=[0]*4;n=int(f.readline());count+=n
        for _ in range(n):
            label,word=f.readline().split()
            masks[roots.index(bytes.fromhex(word)[0])]|=1<<int(label)
        family.append(masks)
    assert count==nw
    configs=[tuple(map(int,f.readline().split())) for _ in range(nc)]
def domain(keys):
    sig=[0]*24
    for key in keys:
        for j,mask in enumerate(family[key]):
            while mask:
                low=mask&-mask
                sig[low.bit_length()-1]|=1<<j
                mask^=low
    assert all(sig)
    return tuple(sig)
rep=16995;target=domain(configs[rep])
ids=[i for i,keys in enumerate(configs) if domain(keys)==target]
assert len(ids)==242 and ids[0]==rep
idset=set(ids)
opt=[l for l in range(24) if target[l].bit_count()>1]
actions=list(itertools.product(*[
    tuple(root for j,root in enumerate(roots) if target[label]>>j&1)
    for label in opt]))
assert len(actions)==324
root_subs={}
for j,root in enumerate(roots):
    choices=[l for l in opt if target[l]>>j&1]
    root_subs[root]=sorted(
        sum(1<<l for l,use in zip(choices,flags) if use)
        for flags in itertools.product((0,1),repeat=len(choices)))
assert sum(map(len,root_subs.values()))==96
entries=collections.defaultdict(dict)
with table.open() as f:
    for row in csv.DictReader(f):
        cid=int(row["config"])
        if cid in idset:
            key=int(row["root"]),int(row["subset"])
            assert key not in entries[cid]
            entries[cid][key]=(int(row["cost"]),int(row["must"]),int(row["opt"]))
assert set(entries)==idset
pclasses={};tclasses={};term={}
for cid in ids:
    e=entries[cid];profile=[]
    for j,root in enumerate(roots):
        must=sum(1<<l for l,v in enumerate(target) if v==(1<<j))
        omask=sum(1<<l for l in opt if target[l]>>j&1)
        for s in root_subs[root]:
            val,m,o=e[root,s]
            assert (m,o)==(must,omask)
            profile.append(val)
    profile=tuple(profile)
    results=[]
    for assignment in actions:
        subs={root:0 for root in roots}
        for label,root in zip(opt,assignment):subs[root]|=1<<label
        results.append(sum(e[root,subs[root]][0] for root in roots))
    result=tuple(results)
    pclasses.setdefault(profile,cid)
    tclasses.setdefault(result,cid)
    term[cid]=result
assert len(pclasses)==len(tclasses)==112
assert len({term[c] for c in pclasses.values()})==112
profile_ids=list(pclasses.values())
rows=[term[c] for c in profile_ids]
N=112;Q=324;U=(1<<N)-1;INF=10**9
values=[[row[q] for row in rows] for q in range(Q)]

# Names are adapted from the frozen EC49FPL loader above; the reconstructed
# cost profiles are unmodified and all input checks have already executed.
coordinate_subsets=root_subs;profile_source_ids=profile_ids;terminal=term;FULL=U
def bits(mask):
    while mask:
        low=mask&-mask
        yield low.bit_length()-1
        mask^=low

all_actions=[['T',q] for q in range(Q)]
all_values=[tuple(v) for v in values]
for root in roots:
    for sub in coordinate_subsets[root]:
        all_actions.append(['R',root,sub])
        all_values.append(tuple(entries[i][root,sub][0] for i in profile_source_ids))
assert len(all_actions)==420
all_groups=[];indices=[];seen_full=set()
for q,vec in enumerate(all_values):
    d={}
    for i,v in enumerate(vec):d[v]=d.get(v,0)|(1<<i)
    g=tuple(sorted(d.values()))
    if g not in seen_full:
        seen_full.add(g);all_groups.append(g);indices.append(q)
assert len(indices)==395


# All 420 original scalar readouts are retained. Identical response partitions
# permit a price-safe quotient: keep the cheapest original-action representative.
import time
weights_unif=(1,)*N
weights_src=tuple(collections.Counter(terminal.values())[terminal[i]] for i in profile_source_ids)
fpl=json.loads((base/'EC49FPL_CERTIFICATE.json').read_text())
fpn=json.loads((base/'EC49FPN_CERTIFICATE.json').read_text())
assert fpl['minimal_sum_of_observation_counts']==238
assert fpn['expected_cost_numerator']==641
assert tuple(fpn['weights_per_rooted_profile'])==weights_src
parts={}
for ix,a in enumerate(all_actions):
    bucket={}
    for k,value in enumerate(all_values[ix]):
        bucket[value]=bucket.get(value,0)|(1<<k)
    partition=tuple(sorted(bucket.values()))
    price=1 if a[0]=='R' else 2
    if partition not in parts or price<parts[partition][0]:
        parts[partition]=(price,ix)
assert len(parts)==395
chosen=[x[1] for x in parts.values()]
prices=[1 if all_actions[ix][0]=='R' else 2 for ix in chosen]
full_groups=[]
for ix in chosen:
    bucket={}
    for k,value in enumerate(all_values[ix]):
        bucket[value]=bucket.get(value,0)|(1<<k)
    full_groups.append(tuple(sorted(bucket.values())))
@functools.lru_cache(None)
def restricted(mask,qi):
    return tuple(m for g in full_groups[qi] if (m:=g&mask))
start=time.time()
@functools.lru_cache(None)
def population(mask):
    return mask.bit_count()
def prior_terminal_bound(mask,node):
    if mask.bit_count()<=1:return 0
    q=node['q'];bucket={}
    for k in bits(mask):
        val=all_values[q][k];bucket[val]=bucket.get(val,0)|(1<<k)
    if len(bucket)==1:
        val,b=next(iter(bucket.items()))
        return prior_terminal_bound(b,node['children'][str(val)])
    return 2*population(mask)+sum(prior_terminal_bound(b,node['children'][str(val)]) for val,b in bucket.items() if b.bit_count()>1)
@functools.lru_cache(None)
def C(mask):
    if mask.bit_count()<=1:return 0
    mass=population(mask)
    best=prior_terminal_bound(mask,fpl['tree'])
    for qi in sorted(range(len(chosen)),key=lambda i:prices[i]):
        fs=restricted(mask,qi)
        if len(fs)<=1:continue
        # Every nonsingleton child needs >=1 more positive-cost query.
        lower=prices[qi]*mass+sum(population(f) for f in fs if f.bit_count()>1)
        if lower>=best:continue
        cost=prices[qi]*mass
        for f in sorted((f for f in fs if f.bit_count()>1),key=population,reverse=True):
            cost+=C(f)
            if cost>=best:break
        if cost<best:best=cost
        if best==mass:break
    return best
optimum=C(FULL)
all_first=[]
first=[]
for qi in range(len(chosen)):
    fs=restricted(FULL,qi)
    cost=None if len(fs)<=1 else prices[qi]*N+sum(C(f) for f in fs if f.bit_count()>1)
    all_first.append(cost)
    if cost==optimum:first.append(chosen[qi])
assert optimum==296 and first==[346,354],(optimum,first)
def construct(mask):
    if mask.bit_count()==1:return {'leaf':next(bits(mask))}
    for qi in range(len(chosen)):
        fs=restricted(mask,qi)
        if len(fs)<=1:continue
        cost=prices[qi]*population(mask)+sum(C(f) for f in fs if f.bit_count()>1)
        if cost!=C(mask):continue
        ix=chosen[qi];d={}
        for k in bits(mask):
            v=all_values[ix][k];d[v]=d.get(v,0)|(1<<k)
        return {'action_index':ix,'action':all_actions[ix],
                'children':{str(v):construct(b) for v,b in sorted(d.items())}}
    raise AssertionError('missing exact optimum')
tree=construct(FULL)
leaf_scaled={}
paths=set()
for i in range(N):
    node=tree;path=[];price=0
    while 'leaf' not in node:
        ix=node['action_index'];response=all_values[ix][i]
        path.append((ix,response))
        price+=1 if all_actions[ix][0]=='R' else 2
        node=node['children'][str(response)]
    assert node['leaf']==i
    assert tuple(path) not in paths
    paths.add(tuple(path));leaf_scaled[i]=price
hist=collections.Counter(leaf_scaled.values())
assert sorted(hist.items())==[(1,3),(2,50),(3,47),(4,8),(5,4)]
assert sum(leaf_scaled.values())==296
source_total=sum(weights_src[i]*leaf_scaled[i] for i in range(N))
assert source_total==850
assert len(paths)==N
certificate={
    'schema':'EC49FPR_HALF_ROOT_PRICE_EXACT_V1',
    'frozen_scientific_commit':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
    'master_sha256':MASTER_HASH,'root_cost_sha256':COST_HASH,
    'original_source_configurations':242,'distinct_rooted_profiles':N,
    'terminal_actions':Q,'named_root_actions':96,'partition_representatives':len(chosen),
    'scaled_prices':{'terminal':2,'named_root':1},
    'profile_uniform':{'exact_optimal_total_scaled':optimum,'expected_terminal_price_units':'37/28',
        'optimal_first_original_actions':[[ix,all_actions[ix]] for ix in first],
        'leaf_scaled_cost_histogram':sorted(hist.items()),
        'bellman_subset_count':C.cache_info().currsize,'complete_tree':tree,
        'all_first_partition_costs':all_first},
    'source_config_uniform':{'status':'FEASIBLE_ONLY','scaled_total_of_profile_uniform_tree':source_total,
        'expected_terminal_price_units_upper_bound':'425/242','exact_optimum':'OPEN'},
    'status':'AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED'
}
assert C.cache_info().currsize==16347
out.write_text(json.dumps(certificate,ensure_ascii=False,indent=2)+'\n')
print('EC49FPR_HALF_ROOT_EXACT_PASS',optimum,first,
      sorted(hist.items()),'source_weighted_upper',source_total,
      'bellman_masks',C.cache_info().currsize,'elapsed_sec',round(time.time()-start,3),flush=True)
