#!/usr/bin/env python3
"""EC49FPQ: exact mixed terminal/root observation optima on frozen original BRC class16995.
Usage: python VERIFY_EC49FPL.py EVIDENCE_DIR [CERTIFICATE_JSON]
Inputs: frozen_original_master.txt, EC49FPG_PROFILE.csv (original native cost table).
"""
import collections,csv,functools,hashlib,itertools,json,sys
from pathlib import Path
base=Path(sys.argv[1])
out=Path(sys.argv[2]) if len(sys.argv)>2 else Path("EC49FPQ_FULL_CERTIFICATE.json")
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

@functools.lru_cache(None)
def groups(mask,q):
    return tuple(x for g in all_groups[q] if (x:=g&mask))
@functools.lru_cache(None)
def one_query_suffices(mask):
    if mask.bit_count()<=1:return True
    return any(len(groups(mask,q))==mask.bit_count() for q in range(len(indices)))
@functools.lru_cache(None)
def two_queries_suffice(mask):
    if mask.bit_count()<=1:return True
    for q in range(len(indices)):
        pp=groups(mask,q)
        if len(pp)==1:continue
        if all(one_query_suffices(x) for x in pp if x.bit_count()>1):return True
    return False

first_bad_fiber=[]
for q in range(len(indices)):
    pp=groups(FULL,q)
    bad=next((g for g in pp if g.bit_count()>1 and not two_queries_suffice(g)),None)
    if bad is None:raise AssertionError('mixed-depth-three witness found')
    first_bad_fiber.append({'q':indices[q],'bad_fiber_hex':hex(bad),'size':bad.bit_count()})
print('MIXED_MIN_WORST_DEPTH_FOUR',len(first_bad_fiber),'one',one_query_suffices.cache_info().currsize,'two',two_queries_suffice.cache_info().currsize,flush=True)

fpl=json.loads((base/'EC49FPL_CERTIFICATE.json').read_text())
fpn=json.loads((base/'EC49FPN_CERTIFICATE.json').read_text())
assert fpl['minimal_sum_of_observation_counts']==238
assert fpn['expected_cost_numerator']==641
profile_weights=tuple(collections.Counter(terminal.values())[terminal[i]] for i in profile_source_ids)
assert tuple(fpn['weights_per_rooted_profile'])==profile_weights and sum(profile_weights)==242

def verify_legacy_tree(node,weights):
    total=0;codes=set();hist=collections.Counter()
    for i in range(N):
        n=node;path=[]
        while n is not None:
            q=n['q'];assert 0<=q<Q
            val=all_values[q][i];path.append((q,val));n=n['children'].get(str(val))
        assert tuple(path) not in codes;codes.add(tuple(path))
        total+=weights[i]*len(path);hist[len(path)]+=weights[i]
    assert len(codes)==N
    return total,dict(sorted(hist.items()))
assert verify_legacy_tree(fpl['tree'],(1,)*N)[0]==238
assert verify_legacy_tree(fpn['verified_tree'],profile_weights)[0]==641

def exact_expectation(weights,old_tree):
    @functools.lru_cache(None)
    def weight(mask):
        s=0
        while mask:
            b=mask&-mask;s+=weights[b.bit_length()-1];mask^=b
        return s
    def legacy_bound(mask,node):
        if mask.bit_count()<=1:return 0
        q=node['q'];d={}
        for i in bits(mask):
            v=all_values[q][i];d[v]=d.get(v,0)|(1<<i)
        if len(d)==1:
            v,g=next(iter(d.items()))
            return legacy_bound(g,node['children'].get(str(v)))
        return weight(mask)+sum(legacy_bound(g,node['children'][str(v)]) for v,g in d.items() if g.bit_count()>1)
    @functools.lru_cache(None)
    def C(mask):
        if mask.bit_count()<=1:return 0
        mass=weight(mask);best=legacy_bound(mask,old_tree)
        scanned=set()
        for q in range(len(indices)):
            gs=groups(mask,q)
            if len(gs)<=1 or gs in scanned:continue
            scanned.add(gs)
            lower=mass+sum(weight(g) for g in gs if g.bit_count()>1)
            if lower>=best:continue
            cost=mass
            for g in sorted(gs,key=weight,reverse=True):
                if g.bit_count()>1:
                    cost+=C(g)
                    if cost>=best:break
            if cost<best:best=cost
            if best==mass:break
        return best
    optimum=C(FULL)
    all_first=[weight(FULL)+sum(C(g) for g in groups(FULL,q) if g.bit_count()>1) for q in range(len(indices))]
    good=[indices[q] for q,c in enumerate(all_first) if c==optimum]
    assert optimum==min(all_first)
    return optimum,good,C.cache_info().currsize,all_first

unit,first_u,n_unit,all_u=exact_expectation((1,)*N,fpl['tree'])
source,first_s,n_source,all_s=exact_expectation(profile_weights,fpn['verified_tree'])
assert (unit,first_u)==(238,[118,119,124,201,203,204]),(unit,first_u)
assert (source,first_s)==(641,[150,209,290,312]),(source,first_s)
print('EC49FPQ_MIXED_EXACT_PASS',unit,source,first_u,first_s,n_unit,n_source,flush=True)

certificate={
 'schema':'EC49FPQ_MIXED_NATIVE_BRC_SENSOR_GLOBAL_OPT_V1',
 'frozen_scientific_commit':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
 'original_master_sha256':MASTER_HASH,'root_cost_sha256':COST_HASH,
 'model':'Original full class16995, exact rooted Trie costs; unit cost per scalar observation',
 'source_configurations':242,'rooted_profiles':N,'terminal_queries':Q,
 'named_root_queries':96,'unique_observation_partitions':len(indices),
 'root_query_keys':all_actions[Q:],
 'distinct_query_representatives':indices,
 'worst_adaptive_depth_exact':4,
 'depth_three_exclusion_all_first_query_fibers':first_bad_fiber,
 'rooted_profile_uniform':{'minimum_total_query_cost':unit,'expected_numerator':unit,
    'expected_denominator':N,'optimal_first_indices':first_u,
    'all_unique_query_first_costs':all_u,'memo_subsets':n_unit},
 'source_config_uniform':{'minimum_total_query_cost':source,'expected_numerator':source,
    'expected_denominator':242,'optimal_first_indices':first_s,
    'all_unique_query_first_costs':all_s,'memo_subsets':n_source,
    'rooted_profile_weights':profile_weights},
 'existing_terminal_witness_tree_verified':{
    'uniform':verify_legacy_tree(fpl['tree'],(1,)*N),
    'source':verify_legacy_tree(fpn['verified_tree'],profile_weights)},
 'proof_status':'AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED'
}
out.write_text(json.dumps(certificate,ensure_ascii=False,indent=2)+'\n')
