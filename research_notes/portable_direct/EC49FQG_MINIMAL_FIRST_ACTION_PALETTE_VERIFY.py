#!/usr/bin/env python3
"""EC49FQG: exact native BRC first-action palette/isolated-tie/re-entry audit.

python EC49FQG_PALETTE_VERIFY.py EC49FQF_EVIDENCE [out.json]

Reconstructs physical observations from frozen native source, audits 25 prior
unrestricted Bellman breakpoint certificates and 2 tail certificates, and
independently replays both optimal decision trees in each: 54 full trees.
The Bellman recursions themselves are inherited, not rerun here.
"""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import csv, hashlib, itertools, json, sys

BASE=Path(sys.argv[1])
OUT=Path(sys.argv[2]) if len(sys.argv)>2 else None
info=json.loads((BASE/'notes/EC49FQF_FIRST_QUERY_DATA.json').read_text())
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
MASTER='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
CSV='a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
master=BASE/'source/frozen_original_master.txt'
costfile=BASE/'source/EC49FPG_PROFILE.csv'
assert info['scientific_pin']==PIN and sha(master)==MASTER and sha(costfile)==CSV

roots=(3,5,6,7)
with master.open() as f:
    nk,nw,nconfigs=map(int,f.readline().split())
    assert (nk,nw,nconfigs)==(94,178850,38169)
    families=[]
    for _ in range(nk):
        masks=[0]*4
        for _ in range(int(f.readline())):
            l,w=f.readline().split()
            masks[roots.index(bytes.fromhex(w)[0])] |= 1<<int(l)
        families.append(masks)
    configurations=[tuple(map(int,f.readline().split())) for _ in range(nconfigs)]
def domain(config):
    out=[0]*24
    for fid in config:
        for j,mask0 in enumerate(families[fid]):
            mask=mask0
            while mask:
                lowest=mask&-mask
                out[lowest.bit_length()-1] |= 1<<j
                mask^=lowest
    return tuple(out)
target=domain(configurations[16943])
ids=[i for i,c in enumerate(configurations) if domain(c)==target]
assert len(ids)==310
opts=[l for l in range(24) if target[l].bit_count()>1]
alloc=list(itertools.product(*(tuple(r for j,r in enumerate(roots)
                                     if target[l]>>j&1) for l in opts)))
assert len(alloc)==144
keys=[]
for j,r in enumerate(roots):
    ls=[l for l in opts if target[l]>>j&1]
    keys.extend((r,s) for s in sorted(sum(1<<l for l,b in zip(ls,bits) if b)
                                       for bits in itertools.product((0,1),repeat=len(ls))))
assert len(keys)==84
byconfig=defaultdict(dict)
idset=set(ids)
with costfile.open() as f:
    for row in csv.DictReader(f):
        i=int(row['config'])
        if i in idset:
            k=(int(row['root']),int(row['subset']))
            assert k not in byconfig[i]
            byconfig[i][k]=int(row['cost'])
assert len(byconfig)==310
assert all(len(byconfig[i])==84 for i in ids)
profiles={};reps=[];weights=[]
for i in ids:
    profile=tuple(byconfig[i][k] for k in keys)
    if profile not in profiles:
        profiles[profile]=len(profiles)
        reps.append(i);weights.append(0)
    weights[profiles[profile]]+=1
assert len(reps)==141 and sum(weights)==310

terminal=[]
for assignment in alloc:
    masks={r:0 for r in roots}
    for l,r in zip(opts,assignment):masks[r] |= 1<<l
    terminal.append(tuple(sum(byconfig[i][(r,masks[r])] for r in roots) for i in reps))
named=[tuple(byconfig[i][k] for i in reps) for k in keys]
vectors=terminal+named
assert len(vectors)==228
partition_groups=defaultdict(list)
for q,values in enumerate(vectors):
    fibers=defaultdict(list)
    for i,value in enumerate(values):fibers[value].append(i)
    signature=tuple(sorted(tuple(v) for v in fibers.values()))
    partition_groups[signature].append(q)
assert len(partition_groups)==209
assert all(all(q<144 for q in g) or all(q>=144 for q in g)
           for g in partition_groups.values())
aliases={q:tuple(g) for g in partition_groups.values() for q in g}

def replay(tree,kind,r,t):
    R=T=0
    for i in range(141):
        node=tree
        seen=set()
        ri=ti=0
        while 'leaf' not in node:
            q=node['q']
            assert isinstance(q,int) and 0<=q<228 and q not in seen
            seen.add(q)
            if q>=144:ri+=1
            else:ti+=1
            node=node['children'][str(vectors[q][i])]
        assert node['leaf']==i
        w=weights[i] if kind=='config_weighted' else 1
        R+=w*ri;T+=w*ti
    return R,T,R*r+T*t

all_endpoints={}
all_phases={}
audited=0;replayed=0
for name,key,valueskey in [
  ('uniform','uniform_endpoints','first_query_costs_uniform'),
  ('config_weighted','multiplicity_endpoints','first_query_costs_weighted')]:
    E=[]
    for row in info[key]:
        p=BASE/'certificates'/row['full_certificate_file']
        assert sha(p)==row['full_certificate_sha256']
        d=json.loads(p.read_text());audited+=1
        assert d['frozen_scientific_commit']==PIN
        assert d['source_master_sha256']==MASTER
        assert d['native_root_costs_sha256']==CSV
        assert d['reps']==reps and d['weights']==weights
        assert (d['profile_count'],d['config_count'])==(141,310)
        r,t=row['r'],row['t']
        assert d['prices']=={'root':r,'terminal':t}
        vals=d[valueskey]
        goal=min(vals)
        target_key='optimal_total_uniform' if name=='uniform' else 'optimal_total_config_weighted'
        assert goal==d[target_key]==row['global_total']
        can=[q for q,z in enumerate(vals) if z==goal]
        assert can==row['argmin_indices']
        assert row['terminal_first_lower_bound']==min(vals[:144])
        assert row['root_first_lower_bound']==min(vals[144:])
        physical=sorted({q for c in can for q in aliases[c]})
        assert physical==can and all(len(aliases[q])==1 for q in physical)
        for kind in ('uniform','config_weighted'):
            R,T,c=replay(d['trees'][kind],kind,r,t)
            targetcost=d['optimal_total_uniform' if kind=='uniform' else 'optimal_total_config_weighted']
            assert c==targetcost
            assert R==d['replay'][kind]['weighted_root_observations']
            assert T==d['replay'][kind]['weighted_terminal_observations']
            replayed+=1
        x=Fraction(r,t)
        E.append({'ratio':f'{x.numerator}/{x.denominator}','first':physical,
                  'certificate':p.name,'certificate_sha256':sha(p),'cost':goal})
    assert [Fraction(z['ratio']) for z in E]==sorted({Fraction(z['ratio']) for z in E})
    all_endpoints[name]=E
    ph=[]
    for a,b in zip(E,E[1:]):
        possible=sorted(set(a['first']) & set(b['first']))
        assert 1<=len(possible)<=2
        ph.append({'interval':f'({a["ratio"]},{b["ratio"]})','necessary_first':possible})
    all_phases[name]=ph

for tail in info['tail_checks']:
    r,t=tail['r'],tail['t']
    fname='EC49FQE_TAIL_LOW_1_4.json' if (r,t)==(1,4) else 'EC49FQE_TAIL_HIGH_4_1.json'
    p=BASE/'certificates'/fname
    assert sha(p)==tail['certificate_sha256']
    d=json.loads(p.read_text())
    assert d['prices']=={'root':r,'terminal':t}
    for name,key,prior in [
        ('uniform','uniform_first','first_query_costs_uniform'),
        ('config_weighted','multiplicity_first','first_query_costs_weighted')]:
        vals=d[prior]
        assert [i for i,z in enumerate(vals) if z==min(vals)]==tail[key]
        R,T,c=replay(d['trees'][name],name,r,t)
        assert c==min(vals)
        replayed+=1

U=sorted({q for row in all_endpoints['uniform'] for q in row['first']})
M=sorted({q for row in all_endpoints['config_weighted'] for q in row['first']})
assert U==[32,34,140,142,153,161]
assert M==[16,23,46,59,88,93,124,131,153,161]
Mrows=all_endpoints['config_weighted']
def at(ratio):
    return next(row['first'] for row in Mrows if row['ratio']==ratio)
assert at('1/1')==[16,23,124,131]
assert all(124 not in z['first'] and 131 not in z['first']
           for z in Mrows if z['ratio']!='1/1')
assert all(124 not in z['necessary_first'] and 131 not in z['necessary_first']
           for z in all_phases['config_weighted'])
for q in (59,88):
    assert q in at('17/24') and q not in at('1/1') and q in at('3/1')
assert audited==25 and replayed==54
summary={
 'schema':'EC49FQG_NATIVE_BRC_MINIMAL_ALL_PRICE_FIRST_QUERY_PALETTE_V1',
 'scientific_pin':PIN,'class_id':16943,
 'master_sha256':MASTER,'root_costs_sha256':CSV,
 'profiles':141,'raw_configurations':310,'query_count':228,
 'distinct_response_partitions':209,'duplicate_physical_indices':19,
 'optimal_initial_indices_with_duplicate_partitions':0,
 'uniform_all_price_first_union':U,
 'multiplicity_all_price_first_union':M,
 'joint_union':sorted(set(U)|set(M)),
 'excluded_first_indices_uniform':222,'excluded_first_indices_multiplicity':218,
 'isolated_optimal_indices_at_equal_prices_M':[124,131],
 'reentrant_indices_M':[59,88],
 'reentry_witness_ratios':['17/24','1/1','3/1'],
 'endpoints':all_endpoints,'necessary_interior_sets':all_phases,
 'low_price_tail_first_U_M':[153,161],
 'high_price_tail_first_U':[32,34,140,142],
 'high_price_tail_first_M':[16,23,59,88],
 'verified_prior_endpoint_certificates':audited,
 'independently_replayed_saved_trees':replayed,
 'status':'AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED',
 'bellman_proof_provenance':'inherited EC49FQD-FQF unrestricted exact endpoint Bellman certificates; no new recursion performed'
}
if OUT:OUT.write_text(json.dumps(summary,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
print('EC49FQG_PALETTE_AND_REENTRY_CHECK_PASS')
print('U',U,'M',M,'joint',summary['joint_union'])
print('full_endpoint_certificates',audited,'independent_tree_replays',replayed)
