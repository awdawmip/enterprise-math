#!/usr/bin/env python3
"""EC49FQI self-contained independent exact Bellman and prior-phase audit.
Usage: python EC49FQI_VERIFY.py <unpacked-EC49FQI_EVIDENCE_20261116-root>
Requires only Python standard library; original frozen master and root-cost CSV.
Reuses only the independently implemented BRC native response reconstruction
from EC49FQG; the scalar DP below is independent of the primary FQA optimizer.
"""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import csv, hashlib, itertools, json, sys

BASE=Path(sys.argv[1])
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
MASTER='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
CSV='a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
master=BASE/'source/frozen_original_master.txt'
costfile=BASE/'source/EC49FPG_PROFILE.csv'
assert sha(master)==MASTER and sha(costfile)==CSV

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


from functools import lru_cache

FULL=(1<<141)-1
part=[]
for p,qs in partition_groups.items():
    blocks=tuple(sum(1<<i for i in group) for group in p)
    part.append((blocks,qs[0]))
assert len(part)==209

def bitids(m):
    while m:
        z=m&-m
        yield z.bit_length()-1
        m^=z

def replay_all_profiles(tree):
    Ur=Ut=Mr=Mt=0
    for i in range(141):
        node=tree
        seen=set()
        while 'leaf' not in node:
            q=node['q']
            assert isinstance(q,int) and 0<=q<228 and q not in seen
            seen.add(q)
            if q<144:Ut+=1;Mt+=weights[i]
            else:Ur+=1;Mr+=weights[i]
            node=node['children'][str(vectors[q][i])]
        assert node['leaf']==i
    return (Ur,Ut,Mr,Mt)

def check(a,b):
    path=BASE/'certificates'/f'lambda_{a}_{b}.json'
    d=json.loads(path.read_text())
    assert d['source_master_sha256']==MASTER
    assert d['native_root_costs_sha256']==CSV
    assert d['frozen_scientific_commit']==PIN
    assert d['reps']==reps and d['raw_multiplicities']==weights
    assert d['interpolation']['numerator']==a and d['interpolation']['denominator']==b
    w=[310*(b-a)+141*a*m for m in weights]
    total=sum(w)
    assert total==141*310*b
    @lru_cache(None)
    def mass(mask):
        return sum(w[i] for i in bitids(mask))
    @lru_cache(None)
    def opt(mask):
        if mask.bit_count()==1:return 0
        m=mass(mask);best=10**30
        for blocks,_q in part:
            branches=[p for block in blocks if (p:=block&mask)]
            if len(branches)<2:continue
            unresolved=[p for p in branches if p.bit_count()>1]
            if m+sum(mass(p) for p in unresolved)>=best:continue
            cost=m
            for p in unresolved:
                cost+=opt(p)
                if cost>=best:break
            if cost<best:best=cost
            if best==m:break
        assert best<10**30
        return best
    optimum=opt(FULL)
    costs=[]
    for q,vs in enumerate(vectors):
        fibers={}
        for i,v in enumerate(vs):fibers[v]=fibers.get(v,0)|(1<<i)
        if len(fibers)<=1: costs.append(None);continue
        costs.append(total+sum(opt(p) for p in fibers.values() if p.bit_count()>1))
    first={q for q,cost in enumerate(costs) if cost==optimum}
    assert optimum==d['optimal_total_interpolated']
    assert first==set(d['optimal_first_interpolated'])
    for q,cost in enumerate(costs):
        saved=d['first_query_costs_interpolated'][q]
        if cost!=None and saved!=cost:
            assert saved==10**12, (a,b,q,cost,saved) # partition duplicate ignored in primary solver
    pair=replay_all_profiles(d['trees']['interpolated'])
    assert 310*(b-a)*(pair[0]+pair[1])+141*a*(pair[2]+pair[3])==optimum
    print('INDEPENDENT_PASS',a,b,'total',optimum,'first',sorted(first),'masks',opt.cache_info().currsize)
    return {'lambda':Fraction(a,b),'total':Fraction(optimum,total),'pair':pair,'first':first}

anchors=[(0,1),(1,16),(155,1847),(1,8),(620,3299),(1,4),(1,1)]
C={}
for a,b in anchors:
    d=check(a,b)
    C[d['lambda']]=d
alpha=Fraction(155,1847)
beta=Fraction(620,3299)
assert Fraction(0)<Fraction(1,16)<alpha<Fraction(1,8)<beta<Fraction(1,4)<1
A=(6,290,6,751);B=(5,293,5,704);D=(5,295,5,685)
assert C[Fraction(0)]['pair']==A
assert C[Fraction(1,8)]['pair']==B
assert C[Fraction(1,4)]['pair']==D
def cost(pair,x):
    return Fraction(pair[0]+pair[1],141)*(1-x)+Fraction(pair[2]+pair[3],310)*x
assert cost(A,alpha)==cost(B,alpha)
assert cost(B,beta)==cost(D,beta)
assert cost(A,alpha)<cost(D,alpha)
assert cost(D,beta)<cost(A,beta)
for x,rec in C.items():
    assert rec['total']==min(cost(A,x),cost(B,x),cost(D,x))
for a,b,mid,pair in [(Fraction(0),alpha,Fraction(1,16),A),
                      (alpha,beta,Fraction(1,8),B),
                      (beta,Fraction(1),Fraction(1,4),D)]:
    # Endpoint exact Bellman + one feasible policy connecting both endpoints.
    assert C[a]['total']==cost(pair,a)
    assert C[b]['total']==cost(pair,b)
    # Endpoint intersection + one strict interior exact argmin proves all actions.
    assert C[mid]['first']==C[a]['first']&C[b]['first']
assert C[Fraction(0)]['first']=={32,34}
assert C[alpha]['first']=={32,34,140,142}
assert C[beta]['first']=={16,23,140,142}
assert C[Fraction(1)]['first']=={16,23,124,131}
print('EC49FQI_INDEPENDENT_EXHAUSTIVE_BELLMAN_PASS 7')
print('EC49FQI_FULL_PRIOR_CONTINUUM_AND_PHYSICAL_FIRST_ACTIONS_PASS')
print('Two exact transitions:',str(alpha),str(beta))
