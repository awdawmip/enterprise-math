#!/usr/bin/env python3
"""EC49FPZ: complete 14-knot native BRC finite Bellman audit; no floating point.
Usage: python VERIFY_EC49FPZ.py frozen_original_master.txt EC49FPG_PROFILE.csv EC49FPS_CONFIG_WEIGHTED_HALF_PRICE_CERT.json
Exhausts all 420 native queries, 395 partition types, and all needed information states at 14 exact price knots.
"""
import csv, hashlib, itertools, json, sys
from collections import Counter
from functools import lru_cache
from pathlib import Path

master,table,prior=map(Path,sys.argv[1:4])
assert hashlib.sha256(master.read_bytes()).hexdigest()=='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
assert hashlib.sha256(table.read_bytes()).hexdigest()=='a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f'
roots=(3,5,6,7)
with master.open() as f:
    nk,nw,nc=map(int,f.readline().split());assert (nk,nw,nc)==(94,178850,38169)
    family=[]
    for _ in range(nk):
        d=[0]*4
        for _ in range(int(f.readline())):
            label,word=f.readline().split();d[roots.index(bytes.fromhex(word)[0])]|=1<<int(label)
        family.append(d)
    configs=[tuple(map(int,f.readline().split())) for _ in range(nc)]
def domain(keys):
    d=[0]*24
    for k in keys:
        for j,mask in enumerate(family[k]):
            while mask:
                b=mask&-mask;d[b.bit_length()-1]|=1<<j;mask^=b
    return tuple(d)
target=domain(configs[16995]);ids=[i for i,keys in enumerate(configs) if domain(keys)==target]
assert len(ids)==242 and ids[0]==16995
opts=[l for l in range(24) if target[l].bit_count()>1]
assignments=list(itertools.product(*(tuple(r for j,r in enumerate(roots) if target[l]>>j&1) for l in opts)))
assert len(assignments)==324
subsets={r:sorted(sum(1<<l for l,b in zip([q for q in opts if target[q]>>(roots.index(r))&1],bs) if b) for bs in itertools.product((0,1),repeat=sum(bool(target[q]>>(roots.index(r))&1) for q in opts))) for r in roots}
assert sum(map(len,subsets.values()))==96
rows={i:{} for i in ids}
with table.open() as f:
    for d in csv.DictReader(f):
        i=int(d['config'])
        if i in rows:
            k=int(d['root']),int(d['subset']);assert k not in rows[i];rows[i][k]=int(d['cost'])
profile_to_id={}
for i in ids:
    p=tuple(rows[i][r,s] for r in roots for s in subsets[r]);profile_to_id.setdefault(p,i)
assert len(profile_to_id)==112
reps=list(profile_to_id.values());N=len(reps);FULL=(1<<N)-1
weight=Counter(tuple(rows[i][r,s] for r in roots for s in subsets[r]) for i in ids)
w=tuple(weight[p] for p in profile_to_id)
base=json.loads(prior.read_text());assert base['profile_source_ids']==reps and tuple(base['profile_weights'])==w
# Full terminal readouts and every named-root/optional-demand scalar readout
queries=[];observations=[]
for assign in assignments:
    v=[]
    for i in reps:
        picks={r:0 for r in roots}
        for l,r in zip(opts,assign):picks[r]|=1<<l
        v.append(sum(rows[i][r,picks[r]] for r in roots))
    queries.append(('T',));observations.append(tuple(v))
for r in roots:
    for s in subsets[r]:
        queries.append(('R',r,s));observations.append(tuple(rows[i][r,s] for i in reps))
assert len(queries)==len(observations)==420
# Canonical partitions; identical partitions retain the cheaper R-action at r<=t.
unique={}
for qi,vec in enumerate(observations):
    groups={}
    for i,x in enumerate(vec):groups[x]=groups.get(x,0)|(1<<i)
    key=tuple(sorted(groups.values()))
    if key not in unique or (queries[qi][0]=='R' and queries[unique[key][0]][0]=='T'):
        unique[key]=(qi,key)
acts=[x[0] for x in unique.values()];groups=[x[1] for x in unique.values()]
assert len(acts)==395
@lru_cache(None)
def mass(mask):
    z=0
    while mask:
        b=mask&-mask;z+=w[b.bit_length()-1];mask^=b
    return z
def node_mask(node):
    if 'leaf' in node:return 1<<node['leaf']
    return sum(node_mask(ch) for ch in node['children'].values())
root_tree=base['tree'];assert node_mask(root_tree)==FULL
NODES=[]
def compact(node):
    ix=len(NODES);NODES.append(None)
    if 'leaf' in node: NODES[ix]=(1<<node['leaf'],None,())
    else:
        kids=tuple(compact(child) for child in node['children'].values())
        NODES[ix]=(sum(NODES[c][0] for c in kids),node['action_index'],kids)
    return ix
ROOT=compact(root_tree);assert NODES[ROOT][0]==FULL
def solve(r,t):
    assert 0<r<=t
    prices=[r if queries[qi][0]=='R' else t for qi in acts]
    low=min(prices)
    @lru_cache(None)
    def feasible(mask,nid):
        if mask.bit_count()==1:return 0
        nmask,action,kids=NODES[nid]
        fibers=[(mask & NODES[c][0],c) for c in kids if mask & NODES[c][0]]
        if len(fibers)==1:return feasible(*fibers[0])
        assert action is not None
        cost=r if queries[action][0]=='R' else t
        return cost*mass(mask)+sum(feasible(f,c) for f,c in fibers if f.bit_count()>1)
    @lru_cache(None)
    def bellman(mask):
        if mask.bit_count()==1:return 0
        m=mass(mask);best=feasible(mask,ROOT)
        choices=[]
        for qi,part in enumerate(groups):
            fibers=[g&mask for g in part if g&mask]
            if len(fibers)<=1:continue
            kids=[f for f in fibers if f.bit_count()>1]
            lb=prices[qi]*m+low*sum(mass(f) for f in kids)
            if lb<best:choices.append((lb,qi,kids))
        choices.sort()
        for lb,qi,kids in choices:
            if lb>=best:break
            v=prices[qi]*m
            for f in sorted(kids,key=mass,reverse=True):
                v+=bellman(f)
                if v>=best:break
            if v<best:best=v
            if best==low*m:break
        return best
    value=bellman(FULL)
    first=[]
    for qi,part in enumerate(groups):
        fibers=[g&FULL for g in part if g&FULL]
        if len(fibers)>1 and prices[qi]*242+sum(bellman(f) for f in fibers if f.bit_count()>1)==value:first.append(acts[qi])
    return value,first,bellman.cache_info().currsize
knots = [[44,79,37004],[39,70,32798],[3,5,2491],[11,18,9105],[2,3,1629],[11,16,8907],[31,45,25091],[9,13,7265],[7,10,5616],[3,4,2316],[7,8,4948],[37,41,25642],[40,41,26152],[1,1,641]]
for r,t,want in knots:
    cost,first,masks=solve(r,t)
    assert cost==want,(r,t,cost,want)
    print('EXACT_BELLMAN_PASS',r,t,'weighted_cost',cost,'optimal_first_indices',first,'masks',masks)
# Exact lower-envelope crossing test at all 14 globally verified knots
lines=[[841,0],[762,44],[692,83],[687,86],[669,97],[657,105],[641,116],[371,302],[358,311],[348,318],[316,342],[252,398],[170,472],[129,512],[0,641]]
for r,t,want in knots:
    vals=[R*r+T*t for R,T in lines]
    assert min(vals)==want,(r,t,min(vals),want)
for i in range(len(lines)-1):
    R1,T1=lines[i]; R2,T2=lines[i+1]
    assert R1>R2 and T1<T2
    ratio=(T2-T1,R1-R2)
    from fractions import Fraction
    got=Fraction(*ratio)
    expected=Fraction(knots[i][0],knots[i][1])
    assert got==expected,(i,got,expected)
print('EC49FPZ_COMPLETE_NATIVE_BRC_PRICE_ENVELOPE_14_KNOTS_PASS')
