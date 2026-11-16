#!/usr/bin/env python3
"""EC49FQM: independent exhaustive finite Bellman and q-first tree replay.
Run inside the standalone evidence archive from package root:
  PYTHONPATH=code python code/EC49FQM_INDEPENDENT_VERIFY.py
Requires the bundled source/, certificates/ and EC49FQI_NATIVE_DATA.py.
Python >=3.10, exact integer/Fraction arithmetic, no external dependencies.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import hashlib,json
from EC49FQI_NATIVE_DATA import V,weights,reps,cost_pair,PIN,MASTER,CSV
B=Path(__file__).resolve().parent.parent
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert hashlib.sha256((B/'source/frozen_original_master.txt').read_bytes()).hexdigest()==MASTER
assert hashlib.sha256((B/'source/EC49FPG_PROFILE.csv').read_bytes()).hexdigest()==CSV
assert len(reps)==141 and len(V)==228 and sum(weights)==310
N=len(reps);FULL=(1<<N)-1
parts={};physical=[]
for q,row in enumerate(V):
    groups={}
    for i,z in enumerate(row):groups[z]=groups.get(z,0)|(1<<i)
    physical.append(tuple(groups.values()))
    parts.setdefault(tuple(sorted(groups.values())),q)
assert len(parts)==209
terminal={}
for i in range(N):
    key=tuple(V[q][i] for q in range(144))
    terminal.setdefault(key,[]).append(i)
doublets=[v for v in terminal.values() if len(v)>1]
assert len(terminal)==139 and sorted(map(len,doublets))==[2,2]
assert all(weights[i]==1 for v in doublets for i in v)
print('FIBER_LOWER_BOUND_PASS',len(terminal),'fibers',flush=True)
def bits(s):
    while s:
        b=s&-s;yield b.bit_length()-1;s^=b
def bellman(R,T,a,b):
    w=[310*(b-a)+141*a*m for m in weights]
    assert sum(w)==141*310*b
    price=[T]*144+[R]*84;lower=min(R,T)
    @lru_cache(None)
    def mass(s):return sum(w[i] for i in bits(s))
    @lru_cache(None)
    def dp(s):
        if s.bit_count()<=1:return 0
        W=mass(s);best=10**40
        for groups,q in parts.items():
            sub=[u for g in groups if (u:=g&s)]
            if len(sub)<=1:continue
            live=[u for u in sub if u.bit_count()>1]
            if price[q]*W+lower*sum(mass(u) for u in live)>=best:continue
            cost=price[q]*W
            for u in live:
                cost+=dp(u)
                if cost>=best:break
            if cost<best:best=cost
        assert best<10**40
        return best
    optimum=dp(FULL);total=mass(FULL)
    first=[q for q,blocks in enumerate(physical)
        if len(blocks)>1 and price[q]*total+
        sum(dp(u) for u in blocks if u.bit_count()>1)==optimum]
    return optimum,first,dp.cache_info().currsize
BETA=F(620,3299)
def A(l,x):return (1-l)*F(6*x+290,141)+l*F(6*x+751,310)
def Bmid(l,x):return (1-l)*F(5*x+293,141)+l*F(5*x+704,310)
def C(l,x):return (1-l)*F(5*x+295,141)+l*F(5*x+685,310)
def Hmid(l,x):return (1-l)*F(4*x+296,141)+l*F(4*x+707,310)
def Hc(l,x):return (1-l)*F(4*x+298,141)+l*F(4*x+688,310)
def check(R,T,a,b,expected_first):
    rec=json.loads((B/'certificates'/f'r{R}_t{T}_lambda_{a}_{b}.json').read_text())
    l=F(a,b);x=F(R,T)
    expected=(min(Hmid(l,x),Hc(l,x)) if x==3 else
              min(A(l,x),Bmid(l,x),C(l,x)))*T
    assert rec['frozen_scientific_commit']==PIN
    assert rec['source_master_sha256']==MASTER and rec['native_root_costs_sha256']==CSV
    assert rec['reps']==reps and rec['raw_multiplicities']==weights
    assert rec['prices']=={'root':R,'terminal':T}
    assert rec['interpolation']=={'numerator':a,'denominator':b,
                                  'formula':'(1-lambda)/141 + lambda*m_i/310'}
    val,first,states=bellman(R,T,a,b)
    assert val==rec['optimal_total_interpolated']==int(expected*141*310*b)
    assert first==expected_first
    assert sorted(map(int,rec['all_optimal_first_trees']))==first
    for k,tree in rec['all_optimal_first_trees'].items():
        assert tree['q']==int(k)
        c=cost_pair(tree)
        uR,uT,mR,mT=(c[z] for z in ['U_R','U_T','M_R','M_T'])
        raw=310*(b-a)*(uR*R+uT*T)+141*a*(mR*R+mT*T)
        assert raw==val
    print('INDEPENDENT_BELLMAN_AND_ALL_FIRST_TREE_PASS',
          R,T,a,b,'first',first,'states',states,flush=True)
cases=[
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
]
for c in cases:check(*c)
for f,indices,quad in [
('r3_t2_lambda_310_4869.json',[32,34],(6,290,6,751)),
('r3_t2_lambda_310_4869.json',[140,142],(5,293,5,704)),
('r3_t2_lambda_620_3299.json',[16,23],(5,295,5,685)),
('r3_t1_lambda_0_1.json',[140,142],(4,296,4,707)),
('r3_t1_lambda_620_3299.json',[16,23],(4,298,4,688)),
]:
    rec=json.loads((B/'certificates'/f).read_text())
    for q in indices:
        c=cost_pair(rec['all_optimal_first_trees'][str(q)])
        assert tuple(c[z] for z in ['U_R','U_T','M_R','M_T'])==quad
for x,g in [(F(3,2),F(310,4869)),(F(2),F(310,7219)),(F(5,2),F(310,14269))]:
    assert F(310)*(3-x)/(7557-169*x)==g
    assert A(g,x)==Bmid(g,x)
    assert Bmid(BETA,x)==C(BETA,x)
    assert g<BETA
assert Hmid(BETA,F(3))==Hc(BETA,F(3))
assert Bmid(BETA,F(1))==C(BETA,F(1))
print('EC49FQM_13_INDEPENDENT_ANCHORS_TWO_SLICES_FULL_HIGH_RAY_AND_RIGHT_STRIP_PASS')
