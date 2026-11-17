#!/usr/bin/env python3
"""EC49FRP independent native BRC source reconstruction and all-228 Bellman DP.
Python stdlib only. Execute inside extracted self-contained evidence folder,
which must contain source/frozen_original_master.txt and source/EC49FPG_PROFILE.csv.
This file does not import the other Bellman implementation or native constructor.
"""
from pathlib import Path
from functools import cache
from collections import defaultdict
import csv,hashlib,itertools

ROOT=Path(__file__).resolve().parent.parent
master=ROOT/'source/frozen_original_master.txt'
csvpath=ROOT/'source/EC49FPG_PROFILE.csv'
assert hashlib.sha256(master.read_bytes()).hexdigest()=='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
assert hashlib.sha256(csvpath.read_bytes()).hexdigest()=='a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f'
roots=(3,5,6,7)
with master.open() as f:
    nf,nw,nc=map(int,f.readline().split())
    assert (nf,nw,nc)==(94,178850,38169)
    family=[]
    for _ in range(nf):
        masks=[0]*4
        for __ in range(int(f.readline())):
            loc,word=f.readline().split()
            masks[roots.index(bytes.fromhex(word)[0])]|=1<<int(loc)
        family.append(masks)
    configurations=[tuple(map(int,f.readline().split())) for _ in range(nc)]

def domain(config):
    arr=[0]*24
    for f in config:
        for j,bits in enumerate(family[f]):
            while bits:
                lo=bits&-bits;bits-=lo;arr[lo.bit_length()-1]|=1<<j
    return tuple(arr)

target=domain(configurations[16943])
selected=[i for i,c in enumerate(configurations) if domain(c)==target]
assert len(selected)==310
active=[l for l in range(24) if target[l].bit_count()>1]
choices=list(itertools.product(*(tuple(r for j,r in enumerate(roots) if target[l]&(1<<j)) for l in active)))
assert len(choices)==144
keys=[]
for j,r in enumerate(roots):
    locs=[l for l in active if target[l]&(1<<j)]
    keys.extend((r,sum((1<<l) for l,bit in zip(locs,bits) if bit)) for bits in itertools.product((0,1),repeat=len(locs)))
assert len(keys)==84
rows=defaultdict(dict);selected_set=set(selected)
for record in csv.DictReader(csvpath.open()):
    cid=int(record['config'])
    if cid in selected_set:
        key=(int(record['root']),int(record['subset']))
        rows[cid][key]=int(record['cost'])
assert len(rows)==310 and all(len(v)==84 for v in rows.values())
profiles={};representatives=[];weights=[]
for cid in selected:
    signature=tuple(rows[cid][key] for key in keys)
    if signature not in profiles:
        profiles[signature]=len(representatives);representatives.append(cid);weights.append(0)
    weights[profiles[signature]]+=1
assert len(representatives)==141 and sum(weights)==310

T=[]
for option in choices:
    bins={r:0 for r in roots}
    for l,r in zip(active,option):bins[r]|=1<<l
    T.append(tuple(sum(rows[c][(r,bins[r])] for r in roots) for c in representatives))
R=[tuple(rows[c][k] for c in representatives) for k in keys]
V=T+R
assert len(V)==228
parts=[]
for output in V:
    groups=defaultdict(int)
    for i,v in enumerate(output):groups[v]|=1<<i
    parts.append(tuple(groups.values()))
ALL=(1<<141)-1; INF=10**100

def solve(state_weights,parity):
    @cache
    def mass(mask):
        total=0
        while mask:
            lo=mask&-mask;mask-=lo;total+=state_weights[lo.bit_length()-1]
        return total
    @cache
    def recur(mask):
        if mask.bit_count()<2:return (0,INF) if parity else (0,)
        best=[INF,INF] if parity else [INF]
        for q,group in enumerate(parts): # all original 228 named physical observations
            children=[mask&z for z in group if mask&z]
            if len(children)<2:continue
            c=1 if q<144 else 3
            acc={0:0}
            for child in children:
                if child.bit_count()<2:continue
                nxt={}
                for old,score in acc.items():
                    for k,v in enumerate(recur(child)):
                        if v>=INF:continue
                        dest=(old^k) if parity else 0
                        nxt[dest]=min(nxt.get(dest,INF),score+v)
                acc=nxt
            shift=(c*mask.bit_count())&1 if parity else 0
            for k,v in acc.items():
                out=k^shift;best[out]=min(best[out],c*mass(mask)+v)
        return tuple(best)
    val=recur(ALL)
    print('ALL_228',val,'memoized_subsets',recur.cache_info().currsize)
    return val

assert solve([19+2*w for w in weights],True)==(7290,7311)
assert solve([1]*141,False)==(308,)
assert solve(weights,False)==(700,)
print('PASS independently reconstructed original 310 configs, 141 profiles, 228 physical actions and parity Bellman')
