"""PREFIX-775: exact opposite-sign 1/768 cells in the two-Gamma auxiliary model.
Frozen model: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Author checks only; no native-X6 claim or original comparator exclusion.
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

negative=difference(38,38)
positive=difference(12,760)
dmu_neg,dv_neg=negative
dmu_pos,dv_pos=positive
assert dmu_neg<0 and dv_neg<0
assert dmu_pos>0 and dv_pos>0

# q_R = H * Delta(mu_num) / Delta(var_num), compared with exact integer products.
Q_NUM=33662
Q_DEN=1000000
assert Q_NUM*dv_pos > Q_DEN*H*dmu_pos
assert Q_NUM*dv_neg < Q_DEN*H*dmu_neg

def sign_at(pair,qn,qd):
    dmu,dv=pair
    numerator=qn*dv-qd*H*dmu
    return (numerator>0)-(numerator<0)

assert sign_at(positive,Q_NUM,Q_DEN)>0
assert sign_at(negative,Q_NUM,Q_DEN)<0
assert sign_at(positive,2,1)>0
assert sign_at(negative,2,1)<0

pos_lower,pos_upper=33661560,33661562
neg_lower,neg_upper=28520342,28520343
assert pos_lower*dv_pos < 10**9*H*dmu_pos < pos_upper*dv_pos
assert neg_lower*dv_neg > 10**9*H*dmu_neg > neg_upper*dv_neg

with localcontext() as ctx:
    ctx.prec=42
    def dec(value,denominator):
        return str(Decimal(value)/Decimal(denominator))
    def record(pair,kind,grid):
        dmu,dv=pair
        return {'cell':grid, 'delta_mu_sign':kind, 'delta_var_sign':kind,
                'delta_mu_decimal':dec(dmu,H),'delta_var_decimal':dec(dv,H*H),
                'switch_ratio_decimal':dec(H*dmu,dv),
                'mixed_V2_decimal':dec(4*dv-2*H*dmu,H*H),
                'mixed_V_at_0_033662_sign':'positive' if kind=='positive' else 'negative'}
    result={
        'schema':'PREFIX775_R6_EXACT_TWO_CELL_NONMODULARITY_V1',
        'date':'2026-11-14',
        'scientific_pin':'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
        'model':'external independent two Gamma clocks; Y=max(C_p,C_z), V_q=q^2 Var(Y)-q E(Y)',
        'grid_denominator':768,
        'survivor_count':9529,
        'terminal_row_empty':True,
        'positive_cell':record(positive,'positive',{'p':['12/768','13/768'],'z':['760/768','761/768']}),
        'negative_cell':record(negative,'negative',{'p':['38/768','39/768'],'z':['38/768','39/768']}),
        'certified_switch_ratio_pos': ['33661560/10^9','33661562/10^9'],
        'certified_switch_ratio_neg': ['28520342/10^9','28520343/10^9'],
        'lattice_two_signs_for_all_real_q_at_least':'33662/1000000',
        'checks':['positive/negative mixed signs','switch ratios exact rational brackets','mixed signs at q=0.033662','mixed signs at q=2'],
        'validation':'ALL_CHECKS_PASS PREFIX775 TWO_GRID_CELL_SIGN',
        'original_comparator_exclusion_count_increment':0,
        'research_status':'AUTHOR_EXACT_INTEGER_FINITE_CERTIFICATE / UNREVIEWED / NOT_ADMITTED'
    }
out=Path(__file__).with_name('PREFIX775_R6_TWO_GRID_CELLS_RESULTS.json')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
