#!/usr/bin/env python3
"""EC49FPL: exhaustive depth-four uniform expected-query optimum in original BRC class16995.
Usage: python VERIFY_EC49FPL.py EVIDENCE_DIR [CERTIFICATE_JSON]
Inputs: frozen_original_master.txt, EC49FPG_PROFILE.csv (original native cost table).
"""
import collections,csv,functools,hashlib,itertools,json,sys
from pathlib import Path
base=Path(sys.argv[1])
out=Path(sys.argv[2]) if len(sys.argv)>2 else Path("EC49FPL_CERTIFICATE.json")
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
def bits(mask):
    while mask:
        bit=mask&-mask
        yield bit.bit_length()-1
        mask^=bit
@functools.lru_cache(maxsize=None)
def part(mask,q):
    groups={}
    for i in bits(mask):
        v=values[q][i]
        groups[v]=groups.get(v,0)|(1<<i)
    return tuple(sorted(groups.values()))
# Bellman exact integer cost, uniformly weighted profiles, maximal remaining depth d.
@functools.lru_cache(maxsize=None)
def C(mask,d):
    n=mask.bit_count()
    if n<=1:return 0,-1
    if d==0:return INF,-1
    best=INF;which=-1;seen=set()
    for q in range(Q):
        fibers=part(mask,q)
        if len(fibers)==1 or fibers in seen:continue
        seen.add(fibers)
        if d==1:
            if len(fibers)==n:return n,q
            continue
        lower=n+sum(g.bit_count() for g in fibers if g.bit_count()>1)
        if lower>=best:continue
        c=n
        for g in fibers:
            if g.bit_count()>1:
                c+=C(g,d-1)[0]
                if c>=best:break
        if c<best:best,which=c,q
        if best==n:break
    return best,which
first_cost=[]
for q in range(Q):
    cost=N+sum(C(g,3)[0] for g in part(U,q) if g.bit_count()>1)
    first_cost.append(cost)
minimum=min(first_cost)
optimal=[q for q,v in enumerate(first_cost) if v==minimum]
assert minimum==238 and optimal==[118,124,201,203]
def response_groups(mask,q):
    out={}
    for i in bits(mask):
        v=values[q][i]
        out[v]=out.get(v,0)|(1<<i)
    return out
def build(mask,d,q=None):
    if mask.bit_count()==1:return None
    if q is None:q=C(mask,d)[1]
    assert q>=0
    groups=response_groups(mask,q)
    assert len(groups)>1
    return {"q":q,"children":{
        str(v):build(g,d-1) for v,g in sorted(groups.items())
        if g.bit_count()>1}}
tree=build(U,4,optimal[0])
paths=set();depths=[]
for i in range(N):
    node=tree;path=[]
    while node is not None:
        q=node["q"];v=values[q][i]
        path.append((q,v))
        node=node["children"].get(str(v))
    assert 1<=len(path)<=4
    path=tuple(path)
    assert path not in paths
    paths.add(path);depths.append(len(path))
assert len(paths)==112 and sum(depths)==minimum
hist=dict(sorted(collections.Counter(depths).items()))
assert hist=={1:9,2:84,3:15,4:4}
cert={
    "schema":"EC49FPL_EXACT_UNIFORM_EXPECTED_DEPTH4_V1",
    "scientific_pin":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
    "master_sha256":MASTER_HASH,"root_table_sha256":COST_HASH,
    "original_class_representative":16995,"original_config_count":242,
    "distinct_root_profiles":N,"terminal_query_count":Q,
    "prior":"uniform on distinct rooted profiles",
    "worst_depth_cap":4,"minimum_path_length_sum":minimum,
    "expectation":{"numerator":minimum,"denominator":N},
    "optimal_first_queries":optimal,
    "first_query_path_length_sums":first_cost,
    "feasible_first_query_count":sum(c<INF for c in first_cost),
    "leaf_depth_histogram":hist,
    "full_optimal_decision_tree":tree,
    "dp_subproblems":C.cache_info().currsize,
    "verification":"AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED"}
out.write_text(json.dumps(cert,indent=2)+"\n")
print("EC49FPL_EXACT_EXPECTATION_DP4_PASS",minimum,N,optimal,hist)
