#!/usr/bin/env python3
"""EC49FQL independent exact Bellman & physical first-action verification.
Place under code/ of the EC49FQL evidence package; source/ contains frozen
native data, certificates/ contains the four endpoint records, and
EC49FQI_NATIVE_DATA.py is the pinned EC49FQK data reconstructor.
Python 3.10+, standard library only.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import hashlib, json
from EC49FQI_NATIVE_DATA import V, weights, reps, cost_pair, MASTER, CSV, PIN
B=Path(__file__).resolve().parent.parent
assert len(V)==228 and len(reps)==141 and sum(weights)==310
assert hashlib.sha256((B/'source/frozen_original_master.txt').read_bytes()).hexdigest()==MASTER
assert hashlib.sha256((B/'source/EC49FPG_PROFILE.csv').read_bytes()).hexdigest()==CSV
n=len(weights); FULL=(1<<n)-1
parts={}; response=[]
for q,row in enumerate(V):
    groups={}
    for i,z in enumerate(row): groups[z]=groups.get(z,0)|(1<<i)
    fibers=tuple(groups.values())
    response.append(fibers)
    parts.setdefault(tuple(sorted(fibers)),q)
assert len(parts)==209

def bits(s):
    while s:
        p=s&-s; yield p.bit_length()-1;s^=p

def calc(a,b):
    w=[310*(b-a)+141*a*m for m in weights]
    assert sum(w)==141*310*b
    @lru_cache(None)
    def mass(s): return sum(w[i] for i in bits(s))
    @lru_cache(None)
    def bell(s):
        if s.bit_count()<=1: return 0
        W=mass(s);out=10**40
        for blocks,q in parts.items():
            sub=[k for block in blocks if (k:=block&s)]
            if len(sub)<=1: continue
            alive=[k for k in sub if k.bit_count()>1]
            rate=2 if q>=144 else 1
            if rate*W+sum(mass(k) for k in alive)>=out:continue
            cost=rate*W
            for k in alive:
                cost+=bell(k)
                if cost>=out:break
            out=min(out,cost)
        assert out<10**40
        return out
    v=bell(FULL); total=mass(FULL)
    forced=[None if len(fib)<=1 else
         (2 if q>=144 else 1)*total+sum(bell(k) for k in fib if k.bit_count()>1)
         for q,fib in enumerate(response)]
    first=[q for q,c in enumerate(forced) if c==v]
    return F(v,total),first,bell.cache_info().currsize

G=F(310,7219); H=F(620,3299)
checks=[(0,1,F(302,141),[32,34]),
        (310,7219,None,[32,34,140,142]),
        (620,3299,None,[16,23,140,142]),
        (1,1,F(695,310),[16,23])]
def A(l): return (1-l)*F(302,141)+l*F(763,310)
def Bmid(l): return (1-l)*F(303,141)+l*F(714,310)
def C(l): return (1-l)*F(305,141)+l*F(695,310)
assert A(G)==Bmid(G) and Bmid(H)==C(H)
assert 0<G<H<1
for a,b,v,first in checks:
    l=F(a,b); observed,first_obs,states=calc(a,b)
    expected=min(A(l),Bmid(l),C(l))
    assert observed==expected and (v is None or observed==v)
    assert first_obs==first
    print('INDEPENDENT_EXACT_BELLMAN_PASS',f'{a}/{b}',str(observed),first_obs,states,flush=True)

for filename, expected in [('gamma_allfirst_x2.json',
                             {'32':(6,290,6,751),'34':(6,290,6,751),
                              '140':(5,293,5,704),'142':(5,293,5,704)}),
                           ('beta_allfirst_x2.json',
                             {'16':(5,295,5,685),'23':(5,295,5,685),
                              '140':(5,293,5,704),'142':(5,293,5,704)})]:
    rec=json.loads((B/'certificates'/filename).read_text())
    assert rec['frozen_scientific_commit']==PIN
    assert rec['source_master_sha256']==MASTER and rec['native_root_costs_sha256']==CSV
    assert rec['raw_multiplicities']==weights and rec['reps']==reps
    assert set(rec['all_optimal_first_trees'])==set(expected)
    for q,tuple4 in expected.items():
        t=rec['all_optimal_first_trees'][q]
        assert t['q']==int(q)
        counts=cost_pair(t)
        assert tuple(counts[k] for k in ('U_R','U_T','M_R','M_T'))==tuple4
    print('ALL_PHYSICAL_TIE_WITNESS_REPLAYS_PASS',filename,sorted(expected),flush=True)

assert A(F(0)) < Bmid(F(0)) < C(F(0))
assert C(F(1)) < Bmid(F(1)) < A(F(1))
for l,query_pair in [(F(0),('A',)),(G,('A','B')),(F(1,10),('B',)),
                      (H,('B','C')),(F(1),('C',))]:
    scores={'A':A(l),'B':Bmid(l),'C':C(l)}
    assert tuple(k for k,z in scores.items() if z==min(scores.values()))==query_pair
print('EC49FQL_ALL_PRIOR_AT_PRICE_2_FULL_PHASES_PASS')
