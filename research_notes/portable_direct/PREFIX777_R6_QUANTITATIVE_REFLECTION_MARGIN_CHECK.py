"""PREFIX-777: sharp all-q quantitative mixed-sign margin on four frozen Gamma grid cells.
Frozen input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d
External killed-Pascal + independent unit Gamma clocks only; author-level exact integer evidence.
No non-native X6 computation or task-claim is asserted.
"""
from collections import defaultdict
from functools import lru_cache
from math import comb
from decimal import Decimal, localcontext
import json
from pathlib import Path

N, DEN, W = 189, 768, 1 << 18
@lru_cache(None)
def inside(n,k,x):
    return 40*(n+1)*comb(n,k)*x**k*(W-x)**(n-k)>W**n
@lru_cache(None)
def wide(n,k):
    if 2*k>n:return wide(n,n-k)
    m=k*W//n
    assert inside(n,k,m)
    if k==0:lo=hi=0
    else:
        a,b=0,m
        while b-a>1:
            t=(a+b)//2
            if inside(n,k,t):b=t
            else:a=t
        lo,hi=a,b
    a,b=m,W
    while b-a>1:
        t=(a+b)//2
        if inside(n,k,t):a=t
        else:b=t
    if 4*(a-hi)>W:return True
    if 4*(b-lo)<W:return False
    raise ValueError((n,k))

rows=[{0:1}]
for n in range(1,N+1):
    nxt=defaultdict(int)
    for k,c in rows[-1].items():
        nxt[k]+=c;nxt[k+1]+=c
    rows.append({k:c for k,c in nxt.items() if wide(n,k)})
assert not rows[N] and sum(map(len,rows[:N]))==9529
for n,row in enumerate(rows[:N]):
    assert all(row.get(k,0)==row.get(n-k,0) for k in row)
E=DEN**188; H=E*E*(1<<377)
K=[[comb(i+j,i)<<(376-i-j) for j in range(N)] for i in range(N)]
@lru_cache(None)
def surv(a):
    pa=[1];pb=[1];pd=[1]
    for i in range(N):
        pa.append(pa[-1]*a);pb.append(pb[-1]*(DEN-a));pd.append(pd[-1]*DEN)
    return [sum(c*pa[k]*pb[n-k] for k,c in row.items())*pd[188-n] for n,row in enumerate(rows[:N])]

def B(s,t,order=0):
    return sum(si*sum(kij*(i+j+1 if order else 1)*tj for j,(kij,tj) in enumerate(zip(K[i],t)) if tj)
               for i,si in enumerate(s) if si)

@lru_cache(None)
def moment(a,b):
    s,t=surv(a),surv(b)
    mu=(sum(s)+sum(t))*E*(1<<377)-B(s,t)
    m2=2*(sum((i+1)*v for i,v in enumerate(s))+sum((j+1)*v for j,v in enumerate(t)))*E*(1<<377)-B(s,t,1)
    return mu,m2*H-mu*mu

def diff(k,l):
    p00=moment(k,l);p10=moment(k+1,l);p01=moment(k,l+1);p11=moment(k+1,l+1)
    return tuple(p11[i]-p10[i]-p01[i]+p00[i] for i in (0,1))

d38,d39=diff(38,38),diff(39,39)
for d in (d38,d39):assert d[0]<0 and d[1]<0
assert diff(38,729)==tuple(-x for x in d38)
assert diff(39,728)==tuple(-x for x in d39)
# dmu/H and dw/H^2 are the physical mixed differences.
a38,a39=-d38[0],-d39[0]
b38,b39=-d38[1],-d39[1]
# r39>r38 iff H*(a39*b38-a38*b39)>0; common H cancels.
J=a39*b38-a38*b39
assert J>0
# Certify both |Delta variance| > 1/6.
assert 6*b38>H*H and 6*b39>H*H
# C=(b38*b39/(b38+b39))*(H*a39/b39-H*a38/b38)
#   = H*(a39*b38-a38*b39)/(b38+b39) / H^2 = J/(H*(b38+b39))
# (since a are numerators of mu, b of variance).
Cnum=J
Cden=H*(b38+b39)
assert Cnum>0 and Cden>0
# A simple strong bound with exact integer cross multiplication:
assert Cnum*10**8>27*Cden  # C > 2.7e-7.
assert Cnum*10**9<271*Cden # C < 2.71e-7.
# q0=(A38+A39)/(B38+B39)=H*(a38+a39)/(b38+b39)
q0_num=H*(a38+a39);q0_den=b38+b39
assert q0_num*b38>H*a38*q0_den  # r38<q0
assert q0_num*b39<H*a39*q0_den  # q0<r39
# Universal proof: for all real q, max(B38|q-r38|,B39|q-r39|) >= C.
# Equality exactly at q=q0, with opposite signed differences on R38/R39.
# Mirror cells give equal-magnitude opposite signs even at endpoints.
with localcontext() as ctx:
    ctx.prec=55
    dec=lambda a,b: str(Decimal(a)/Decimal(b))
    result={
      'schema':'PREFIX777_R6_SHARP_UNIFORM_NONMODULARITY_MARGIN_V1',
      'frozen_scientific_pin':'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
      'date':'2026-11-14',
      'scope':'189-layer external killed-Pascal first-stop / independent unit-scale Gamma maximum Y; grid 1/768',
      'survivor_nonzero_positions':9529,'terminal_survivor_empty':True,
      'cells':[[38,38],[39,39],[38,729],[39,728]],
      'both_negative_variance_increments_gt_one_sixth_in_magnitude':True,
      'r38_decimal':dec(H*a38,b38),'r39_decimal':dec(H*a39,b39),
      'q_opt_decimal':dec(q0_num,q0_den),
      'C_exact_rational_numerator_decimal':str(Cnum),
      'C_exact_rational_denominator_decimal':str(Cden),
      'C_sharp_decimal':dec(Cnum,Cden),
      'C_certified_strict_bounds':['27/100000000','271/1000000000'],
      'universal_theorem':'For every real q>0, four fixed cells include a mixed difference >= q*C and one <= -q*C; C is optimal for this four-cell witness family.',
      'perturbation_corollary':'For pointwise errors <=epsilon at every corner of the four cells, signs persist if 4epsilon < q*C. In particular epsilon <= q*27/400000000 is sufficient (strict C bound).',
      'verification':'ALL_CHECKS_PASS PREFIX777 SHARP_MARGIN',
      'original_comparator_exclusion_count_increment':0,
      'scientific_status':'AUTHOR_EXACT_INTEGER_AND_ALGEBRAIC_THEOREM / UNREVIEWED / NOT_ADMITTED',
      'open':'Determine whether a native BRC comparator has a typed reflection-equivariant observer and preserves this quantitative margin after source/branch/port readout.'
    }
Path(__file__).with_name('PREFIX777_R6_QUANTITATIVE_REFLECTION_MARGIN_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('r38_decimal','r39_decimal','q_opt_decimal','C_sharp_decimal','C_certified_strict_bounds','verification')},indent=2))
