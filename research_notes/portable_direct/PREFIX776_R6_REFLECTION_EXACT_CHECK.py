"""PREFIX-776: exact reflection symmetry forces both grid mixed signs for every q>0.
Frozen model: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Author exact arithmetic; no native-X6 claim or original comparator exclusion.
"""
from collections import defaultdict
from functools import lru_cache
from math import comb
from decimal import Decimal, localcontext
from pathlib import Path
import json

N = 189
WIDTH_DEN = 1 << 18
GRID_DEN = 768
K_DEN = 1 << 377

@lru_cache(None)
def inside(n, k, x):
    return 40*(n+1)*comb(n,k)*x**k*(WIDTH_DEN-x)**(n-k) > WIDTH_DEN**n
@lru_cache(None)
def wide(n,k):
    if k > n//2:
        return wide(n,n-k)
    m=k*WIDTH_DEN//n
    assert inside(n,k,m)
    if k==0:
        lo=hi=0
    else:
        a,b=0,m
        while b-a>1:
            t=(a+b)//2
            if inside(n,k,t): b=t
            else: a=t
        lo,hi=a,b
    a,b=m,WIDTH_DEN
    while b-a>1:
        t=(a+b)//2
        if inside(n,k,t):a=t
        else:b=t
    if 4*(a-hi)>WIDTH_DEN: return True
    if 4*(b-lo)<WIDTH_DEN: return False
    raise AssertionError((n,k))

rows=[{0:1}]
for n in range(1,N+1):
    next_row=defaultdict(int)
    for k,c in rows[-1].items():
        next_row[k]+=c
        next_row[k+1]+=c
    rows.append({k:c for k,c in next_row.items() if wide(n,k)})
assert rows[-1]=={}
assert sum(len(x) for x in rows[:N])==9529

E=GRID_DEN**188
H=E*E*K_DEN
@lru_cache(None)
def survivor(a):
    powers_a=[1];powers_b=[1];powers_den=[1]
    for _ in range(N):
        powers_a.append(powers_a[-1]*a)
        powers_b.append(powers_b[-1]*(GRID_DEN-a))
        powers_den.append(powers_den[-1]*GRID_DEN)
    return [sum(c*powers_a[k]*powers_b[n-k] for k,c in row.items())*powers_den[188-n]
            for n,row in enumerate(rows[:N])]

K=[[comb(i+j,i)<<(376-i-j) for j in range(N)] for i in range(N)]

def bilinear(s,t,l_kernel=False):
    total=0
    for i,si in enumerate(s):
        if si==0:continue
        row=K[i]
        if l_kernel:
            total+=si*sum(kij*(i+j+1)*tj for j,(kij,tj) in enumerate(zip(row,t)) if tj)
        else:
            total+=si*sum(kij*tj for kij,tj in zip(row,t) if tj)
    return total

@lru_cache(None)
def moments(a,b):
    s,t=survivor(a),survivor(b)
    mu=(sum(s)+sum(t))*E*K_DEN-bilinear(s,t)
    m2=(2*sum((i+1)*v for i,v in enumerate(s))+2*sum((i+1)*v for i,v in enumerate(t)))*E*K_DEN-bilinear(s,t,True)
    v=m2*H-mu*mu
    assert mu>0 and v>0
    return mu,v

def difference(p,z):
    a,b=p,p+1
    c,d=z,z+1
    u00,v00=moments(a,c)
    u10,v10=moments(b,c)
    u01,v01=moments(a,d)
    u11,v11=moments(b,d)
    return u11-u10-u01+u00, v11-v10-v01+v00

# Binomial survivor rows are invariant under the index involution k -> n-k.
for n,row in enumerate(rows[:N]):
    assert all(row.get(k,0)==row.get(n-k,0) for k in range(n+1))
for a in [38,39,40,728,729,730]:
    assert survivor(a)==survivor(GRID_DEN-a)

def mirror_cell(k):
    return difference(k,GRID_DEN-k-1)

R38=difference(38,38)
R39=difference(39,39)
M38=mirror_cell(38)
M39=mirror_cell(39)
assert M38==tuple(-v for v in R38), (M38,R38)
assert M39==tuple(-v for v in R39), (M39,R39)
assert R38[0]<0 and R38[1]<0
assert R39[0]<0 and R39[1]<0

# r_k = H * Delta(mu numerator) / Delta(variance numerator).
dm38,dw38=R38
dm39,dw39=R39
assert dm39*dw38 > dm38*dw39
assert 2852034258349*dw38 > 10**14*H*dm38
assert 2852034258350*dw38 < 10**14*H*dm38
assert 28523464*dw39 > 10**9*H*dm39
assert 28523465*dw39 < 10**9*H*dm39

q38_num,q38_den=H*dm38,dw38
q39_num,q39_den=H*dm39,dw39
assert q38_num<0 and q38_den<0
assert q39_num<0 and q39_den<0
assert dm39*dw38 != dm38*dw39

def mixed_v_sign(cell, qnum, qden):
    # qnum/qden>0, qden>0; the prefactor q is positive.
    a,b=cell
    val=qnum*b-qden*H*a
    return (val>0)-(val<0)

assert mixed_v_sign(R38,-q38_num,-q38_den)==0
assert mixed_v_sign(R39,-q38_num,-q38_den)!=0
assert mixed_v_sign(R39,-q39_num,-q39_den)==0
assert mixed_v_sign(R38,-q39_num,-q39_den)!=0
for qnum,qden in [(1,1000),(2,1),(2852034258350,10**14)]:
    s38=mixed_v_sign(R38,qnum,qden)
    s39=mixed_v_sign(R39,qnum,qden)
    assert s38 or s39
    assert mixed_v_sign(M38,qnum,qden)==-s38
    assert mixed_v_sign(M39,qnum,qden)==-s39

with localcontext() as ctx:
    ctx.prec=50
    dec=lambda n,d: str(Decimal(n)/Decimal(d))
    result={
        'schema':'PREFIX776_R6_REFLECTION_NO_MODULARITY_FOR_ALL_Q_V1',
        'date':'2026-11-14',
        'frozen_scientific_pin':'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
        'model':'external 189-layer killed-Pascal, two independent unit Gamma clocks, maximum Y',
        'survivor_nonzero_positions':9529,
        'terminal_survivor_empty':True,
        'survivor_binomial_symmetry_exact':True,
        'survivor_reflection_checked_indices':[38,39,40,728,729,730],
        'grid_denominator':GRID_DEN,
        'cells':[{
            'base_cell':[k,k],
            'mirror_cell':[k,GRID_DEN-k-1],
            'delta_mu_sign':'negative',
            'delta_variance_sign':'negative',
            'mirror_delta_sign':'positive',
            'mirror_increment_equals_exact_negative':True,
            'switch_ratio_decimal':dec(H*dmu,dv),
            'delta_mu_decimal':dec(dmu,H),
            'delta_variance_decimal':dec(dv,H*H),
        } for k,(dmu,dv) in [(38,R38),(39,R39)]],
        'switch_ratio_r38_certified_strict_interval':['2852034258349/10^14','2852034258350/10^14'],
        'switch_ratio_r39_certified_strict_interval':['28523464/10^9','28523465/10^9'],
        'switch_ratios_distinct_by_integer_cross_product':True,
        'theorem':'for all real q > 0, both signs of the rectangular mixed difference of V_q occur on the 1/768 auxiliary parameter lattice',
        'validation':'ALL_CHECKS_PASS PREFIX776 REFLECTION_ALL_Q',
        'scientific_status':'AUTHOR_EXACT_INTEGER_THEOREM / UNREVIEWED / NOT_ADMITTED',
        'original_comparator_exclusion_count_increment':0
    }
Path(__file__).with_name('PREFIX776_R6_REFLECTION_EXACT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
