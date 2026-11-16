#!/usr/bin/env python3
"""Independent exact Bellman and physical first-action certificate verification.
Native class16943; frozen science fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Python >=3.10, standard library. Run in EC49FQO evidence root (PYTHONPATH=code).
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import hashlib, json, sys
from EC49FQI_NATIVE_DATA import V, weights, reps, cost_pair, PIN, MASTER, CSV

B=Path(__file__).resolve().parent.parent
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert hashlib.sha256((B/'source/frozen_original_master.txt').read_bytes()).hexdigest()==MASTER
assert hashlib.sha256((B/'source/EC49FPG_PROFILE.csv').read_bytes()).hexdigest()==CSV
assert len(V)==228 and len(reps)==141 and sum(weights)==310
N=len(reps); FULL=(1<<N)-1
parts={}; physical=[]
for q,row in enumerate(V):
    groups={}
    for i,z in enumerate(row): groups[z]=groups.get(z,0)|(1<<i)
    physical.append(tuple(groups.values()))
    parts.setdefault(tuple(sorted(groups.values())),q)
assert len(parts)==209
terminal={}
for i in range(N):
    key=tuple(V[q][i] for q in range(144))
    terminal.setdefault(key,[]).append(i)
nontrivial=[group for group in terminal.values() if len(group)>1]
assert len(terminal)==139 and sorted(map(len,nontrivial))==[2,2]
assert all(weights[i]==1 for group in nontrivial for i in group)
print('FIBER_LOWER_BOUND_PASS 139 terminal fibers, two disjoint multiplicity-one doublets',flush=True)

def bits(mask):
    while mask:
        b=mask&-mask
        yield b.bit_length()-1
        mask^=b

def bellman(R,T,a,b):
    wt=[310*(b-a)+141*a*m for m in weights]
    assert sum(wt)==141*310*b
    price=[T]*144+[R]*84
    MIN=min(R,T)
    distinct=list(parts.items())
    @lru_cache(None)
    def mass(s):return sum(wt[i] for i in bits(s))
    @lru_cache(None)
    def one(s):
        if s.bit_count()<=1:return 0
        best=10**60
        for groups,q in distinct:
            if all((g&s).bit_count()<=1 for g in groups):
                best=min(best,price[q])
                if best==MIN:break
        return best
    @lru_cache(None)
    def two(s):
        if s.bit_count()<=1:return 0
        W=mass(s);best=10**60
        for groups,q in distinct:
            subs=[g&s for g in groups if g&s]
            if len(subs)<=1:continue
            c=price[q]*W
            for u in subs:
                if u.bit_count()>1:c+=one(u)*mass(u)
            best=min(best,c)
        return best
    @lru_cache(None)
    def dp(s):
        if s.bit_count()<=1:return 0
        W=mass(s);best=two(s)
        for groups,q in distinct:
            sub=[u for g in groups if (u:=g&s)]
            if len(sub)<=1:continue
            live=[u for u in sub if u.bit_count()>1]
            if price[q]*W+MIN*sum(mass(u) for u in live)>=best:continue
            cost=price[q]*W
            for u in live:
                cost+=dp(u)
                if cost>=best:break
            if cost<best:best=cost
        assert best<10**60
        return best
    val=dp(FULL);total=mass(FULL)
    first=[q for q,blocks in enumerate(physical)
        if len(blocks)>1 and (price[q]*total+
           sum(dp(u) for u in blocks if u.bit_count()>1))==val]
    return val,first,dp.cache_info().currsize

BETA=F(620,3299)
def A(l,x):return (1-l)*F(6*x+290,141)+l*F(6*x+751,310)
def MID(l,x):return (1-l)*F(5*x+293,141)+l*F(5*x+704,310)
def C(l,x):return (1-l)*F(5*x+295,141)+l*F(5*x+685,310)
def HIGH_MID(l,x):return (1-l)*F(4*x+296,141)+l*F(4*x+707,310)
def HIGH_C(l,x):return (1-l)*F(4*x+298,141)+l*F(4*x+688,310)

def case(r,t,a,b,allowed):
    file=B/'certificates'/f'r{r}_t{t}_lambda_{a}_{b}.json'
    data=json.loads(file.read_text());lam=F(a,b);x=F(r,t)
    expected=t*(min(HIGH_MID(lam,x),HIGH_C(lam,x)) if x==3
                 else min(A(lam,x),MID(lam,x),C(lam,x)))
    assert data['frozen_scientific_commit']==PIN
    assert data['source_master_sha256']==MASTER
    assert data['native_root_costs_sha256']==CSV
    assert data['reps']==reps and data['raw_multiplicities']==weights
    assert data['prices']=={'root':r,'terminal':t}
    assert data['interpolation']['numerator']==a
    assert data['interpolation']['denominator']==b
    actual,first,states=bellman(r,t,a,b)
    assert actual==data['optimal_total_interpolated']==int(expected*141*310*b),(r,t,a,b,actual,expected)
    assert first==allowed,(r,t,a,b,first,allowed)
    trees=data.get('all_optimal_first_trees')
    if trees is None:
        trees={str(data['trees']['interpolated']['q']):data['trees']['interpolated']}
    else:assert sorted(map(int,trees.keys()))==first
    for key,tree in trees.items():
        assert tree['q']==int(key) and tree['q'] in first
        c=cost_pair(tree)
        z=310*(b-a)*(c['U_R']*r+c['U_T']*t)+141*a*(c['M_R']*r+c['M_T']*t)
        assert z==actual
    print('INDEPENDENT_BELLMAN',r,t,a,b,'first',first,'subsets',states,flush=True)

cases=[
# 13 inherited EC49FQM:
(3,2,0,1,[32,34]),
(3,2,310,4869,[32,34,140,142]),
(3,2,620,3299,[16,23,140,142]),
(3,2,1,1,[16,23]),
(5,2,0,1,[32,34]),
(5,2,310,14269,[32,34,140,142]),
(5,2,620,3299,[16,23,140,142]),
(5,2,1,1,[16,23]),
(1,1,620,3299,[16,23,140,142]),
(1,1,1,1,[16,23,124,131]),
(3,1,0,1,[32,34,140,142]),
(3,1,620,3299,[16,23,140,142]),
(3,1,1,1,[16,23,59,88]),
# Four inherited EC49FQL price x=2:
(2,1,0,1,[32,34]),
(2,1,310,7219,[32,34,140,142]),
(2,1,620,3299,[16,23,140,142]),
(2,1,1,1,[16,23]),

# Sixteen new EC49FQO exact anchors, covering 4 new full-prior price sections:
(7,6,0,1,[32,34]),
(7,6,3410,44159,[32,34,140,142]),
(7,6,620,3299,[16,23,140,142]),
(7,6,1,1,[16,23]),
(7,4,0,1,[32,34]),
(7,4,310,5809,[32,34,140,142]),
(7,4,620,3299,[16,23,140,142]),
(7,4,1,1,[16,23]),
(9,4,0,1,[32,34]),
(9,4,310,9569,[32,34,140,142]),
(9,4,620,3299,[16,23,140,142]),
(9,4,1,1,[16,23]),
(17,6,0,1,[32,34]),
(17,6,310,42469,[32,34,140,142]),
(17,6,620,3299,[16,23,140,142]),
(17,6,1,1,[16,23]),
# Eight inherited EC49FQN exact anchors:
(4,3,0,1,[32,34]),
(4,3,310,4399,[32,34,140,142]),
(4,3,620,3299,[16,23,140,142]),
(4,3,1,1,[16,23]),
(8,3,0,1,[32,34]),
(8,3,310,21319,[32,34,140,142]),
(8,3,620,3299,[16,23,140,142]),
(8,3,1,1,[16,23]),
]
mode=int(sys.argv[1]) if len(sys.argv)>1 else -1
indices=(range(int(sys.argv[1]),int(sys.argv[2])) if len(sys.argv)>=3 else
         (range(len(cases)) if mode==-1 else range(mode*11,min((mode+1)*11,len(cases)))))
for i in indices:case(*cases[i])
xs=[F(1),F(7,6),F(4,3),F(3,2),F(7,4),F(2),F(9,4),F(5,2),F(8,3),F(17,6),F(3)]
def gamma(x):return F(310)*(3-x)/(7557-169*x)
def d(l):return (1-l)/141+l/310
errors=[]
for a,b in zip(xs[:-1],xs[1:]):
    assert b-a<=F(1,4)
    g=gamma(b)
    assert 0<=g<=BETA
    errors.append(d(g)*(b-a)/4)
assert max(errors)==F(25,57076)
assert gamma(F(7,6))==F(3410,44159)
assert gamma(F(7,4))==F(310,5809)
assert gamma(F(9,4))==F(310,9569)
assert gamma(F(17,6))==F(310,42469)
assert gamma(F(4,3))==F(310,4399)
assert gamma(F(8,3))==F(310,21319)
assert gamma(F(1))==F(155,1847)
assert gamma(F(3))==0
print('EC49FQO_CERTIFIED_11_PRICE_GRID_ENCLOSURE_PASS max_gap_bound',
      str(max(errors)),'tested',len(indices),'of 41',flush=True)
