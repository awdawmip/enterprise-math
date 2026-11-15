#!/usr/bin/env python3
"""Independent unrestricted Bellman check for EC49FQJ four corners.
Usage: python EC49FQJ_RECTANGLE_VERIFY.py MASTER.txt PROFILE.csv CERTIFICATE_DIRECTORY
"""
from pathlib import Path
from functools import lru_cache
import json,sys,hashlib
from EC49FQJ_NATIVE_DATA import load_native,read_tree,MASTER,CSV,PIN

V,m,reps=load_native(sys.argv[1],sys.argv[2])
folder=Path(sys.argv[3])
N=len(reps);FULL=(1<<N)-1
partitions={};responses=[]
for q,vs in enumerate(V):
    buckets={}
    for i,v in enumerate(vs):buckets[v]=buckets.get(v,0)|(1<<i)
    groups=tuple(buckets.values());responses.append(groups)
    partitions.setdefault(tuple(sorted(groups)),[]).append(q)
assert len(partitions)==209
assert all(all(q<144 for q in qs) or all(q>=144 for q in qs) for qs in partitions.values())
classes=[(groups,qs[0]) for groups,qs in partitions.items()]
def bits(mask):
    while mask:
        bit=mask&-mask
        yield bit.bit_length()-1
        mask^=bit
def corner(a,b,x):
    W=[310*(b-a)+141*a*mi for mi in m]
    total=sum(W);assert total==141*310*b
    @lru_cache(None)
    def mass(mask):return sum(W[i] for i in bits(mask))
    @lru_cache(None)
    def dp(mask):
        if mask.bit_count()<=1:return 0
        w=mass(mask);best=10**30
        for groups,q in classes:
            parts=[child for g in groups if (child:=g&mask)]
            if len(parts)<=1:continue
            live=[child for child in parts if child.bit_count()>1]
            price=x if q>=144 else 1
            if price*w+sum(mass(child) for child in live)>=best:continue
            score=price*w
            for child in live:
                score+=dp(child)
                if score>=best:break
            if score<best:best=score
        assert best<10**30
        return best
    v=dp(FULL)
    first=[]
    for q,groups in enumerate(responses):
        if len(groups)<=1:continue
        forced=(x if q>=144 else 1)*total+sum(dp(g) for g in groups if g.bit_count()>1)
        if forced==v:first.append(q)
    return v,first,dp.cache_info().currsize

EXPECTED={(1,10,1):931389,(1,6,1):561869,(1,10,3):960699,(1,6,3):578779}
for (a,b,x),expected in EXPECTED.items():
    p=folder/f"probe_x_{x}_1_lam_{a}_{b}.json"
    raw=p.read_bytes();c=json.loads(raw)
    assert c["frozen_scientific_commit"]==PIN
    assert c["source_master_sha256"]==MASTER and c["native_root_costs_sha256"]==CSV
    assert c["reps"]==reps and c["raw_multiplicities"]==m
    assert c["prices"]=={"root":x,"terminal":1}
    assert c["interpolation"]["numerator"]==a and c["interpolation"]["denominator"]==b
    assert c["optimal_total_interpolated"]==expected
    computed,first,nodes=corner(a,b,x)
    assert computed==expected,(computed,expected)
    assert first==c["optimal_first_interpolated"]==[140,142],first
    print("CORNER_PASS",a,b,x,expected,first,nodes,hashlib.sha256(raw).hexdigest(),flush=True)

w=json.loads((folder/"witness_both_queries_x_5_2_lam_1_10.json").read_text())
for q,tree in [(140,w["trees"]["interpolated"]),(142,w["extra_q142_tree"])]:
    assert tree["q"]==q
    actual=read_tree(tree,V,m)
    assert actual==(5,293,5,704),actual
    print("TREE_PASS",q,actual,flush=True)
print("EC49FQJ_RECTANGLE_EXACT_PASS")
