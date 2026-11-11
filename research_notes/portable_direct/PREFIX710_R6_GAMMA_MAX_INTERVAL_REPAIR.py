#!/usr/bin/env python3
"""PREFIX-710: correct gamma-clock max interval certificate (exact integers).

Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
The PREFIX-709 count-max kernel is used only to exhibit a precise invalid bound.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from math import comb
import json
from pathlib import Path

N, WD, G = 189, 1 << 18, 192
B = F(559812917, 1000000)

@lru_cache(None)
def inside(m,k,a):
    return 40*(m+1)*comb(m,k)*a**k*(WD-a)**(m-k) > WD**m

@lru_cache(None)
def wide(m,k):
    if k > m//2: return wide(m,m-k)
    mid=k*WD//m
    assert inside(m,k,mid)
    if k==0: left_lo=left_hi=0
    else:
        lo,hi=0,mid
        while hi-lo>1:
            x=(lo+hi)//2
            if inside(m,k,x): hi=x
            else: lo=x
        left_lo,left_hi=lo,hi
    lo,hi=mid,WD
    while hi-lo>1:
        x=(lo+hi)//2
        if inside(m,k,x): lo=x
        else: hi=x
    right_lo,right_hi=lo,hi
    if 4*(right_lo-left_hi)>WD:return True
    if 4*(right_hi-left_lo)<WD:return False
    raise AssertionError(('width undecided',m,k))

rows=[{0:1}]
for m in range(1,N+1):
    new=defaultdict(int)
    for k,v in rows[-1].items():
        new[k]+=v;new[k+1]+=v
    rows.append({k:v for k,v in new.items() if wide(m,k)})
assert rows[-1]=={} and sum(map(len,rows[:N]))==9529
assert rows[25]=={k:comb(25,k) for k in range(1,25)}

# Exact gamma-max witness from the original Erlang kernel; N_0=25.
coeff=[[comb(n+m,n)*2**(2*N-2-n-m) for m in range(N)] for n in range(N)]
Z=2**(2*N-1)

def zero_clock_pair(znum,zden):
    zscale=zden**(N-1)
    pa=[1];pb=[1]
    for _ in range(N):pa.append(pa[-1]*znum);pb.append(pb[-1]*(zden-znum))
    tz=[sum(v*pa[k]*pb[n-k] for k,v in row.items())*zden**(N-1-n)
        for n,row in enumerate(rows[:N])]
    cross0=sum(tz[m]*sum(coeff[n][m] for n in range(25)) for m in range(N))
    cross1=sum(tz[m]*sum((n+m+1)*coeff[n][m] for n in range(25)) for m in range(N))
    denom=zscale*Z
    mu_num=(25*zscale+sum(tz))*Z-cross0
    m2_num=2*(325*zscale+sum((m+1)*v for m,v in enumerate(tz)))*Z-cross1
    mu=F(mu_num,denom)
    return mu,F(m2_num,denom)-mu*mu

mu_e,W_e=zero_clock_pair(3,20)
assert B < W_e-mu_e/2 < F(559812918,1000000)
mu_00,W_00=zero_clock_pair(0,1)
assert mu_00==F(3913470354001175,140737488355328)>25
assert W_00>19

# Exact integer kernel; common moment denominator R.
D=2*G
L=D**(N-1)
Z=2**(2*N-1)
R=L*L*Z
T=[]
for i in range(G+1):
    a,b=i,D-i
    ap=[1];bp=[1]
    for _ in range(N):ap.append(ap[-1]*a);bp.append(bp[-1]*b)
    T.append([sum(v*ap[k]*bp[n-k] for k,v in row.items())*D**(N-1-n)
              for n,row in enumerate(rows[:N])])
A=[sum(t) for t in T]
B1=[sum((n+1)*v for n,v in enumerate(t)) for t in T]
K0=[];K1=[]
for tj in T:
    active=[(m,v) for m,v in enumerate(tj) if v]
    K0.append([sum(coeff[n][m]*v for m,v in active) for n in range(N)])
    K1.append([sum((n+m+1)*coeff[n][m]*v for m,v in active) for n in range(N)])

def gamma_pair(i,j):
    mu=(A[i]+A[j])*L*Z-sum(x*y for x,y in zip(T[i],K0[j]))
    m2=2*(B1[i]+B1[j])*L*Z-sum(x*y for x,y in zip(T[i],K1[j]))
    return mu,m2

mu,m2=gamma_pair(0,0)
assert F(mu,R)==mu_00
assert F(m2*R-mu**2,R**2)==W_00

selected=0
smallest_gap=None
for i in range(G):
    for j in range(i,G):
        mu_lo,_=gamma_pair(i,j)
        _,second_hi=gamma_pair(i+1,j+1)
        upper_num=second_hi*R-mu_lo**2
        gap=B.numerator*R**2-B.denominator*upper_num
        if gap>0:
            selected+=1 if i==j else 2
            if smallest_gap is None or gap<smallest_gap:smallest_gap=gap

assert selected==26445
assert smallest_gap is not None
floor_micro=(1000000*smallest_gap)//(B.denominator*R**2)
assert floor_micro==15701
assert smallest_gap*1000000>15701*B.denominator*R**2

# Exact counterexample to PREFIX-709's count-max upper bound.
i=G-1
def count_pair(i,j):
    js=[(a+b)*L-a*b for a,b in zip(T[i],T[j])]
    return sum(js),sum((2*n+1)*v for n,v in enumerate(js))

mu_lo,sec_lo=count_pair(i,i)
mu_hi,sec_hi=count_pair(i+1,i+1)
L2=L*L
old_upper=min(sec_hi*L2-mu_lo**2,
              (N*N*L2-2*N*mu_lo+sec_lo)*L2-(N*L2-mu_hi)**2)
old_denom=L2*L2
true_mu,true_second=gamma_pair(i,i)
true_var=true_second*R-true_mu**2
assert 0<old_upper<old_denom
assert true_var>137*R**2
assert true_var*old_denom>old_upper*R**2

fraction=F(selected,G*G)
assert fraction==F(8815,12288)
ratio_708=fraction/F(345931,1048576)
assert ratio_708==F(2256640,1037793)
result={
  'schema':'PREFIX710_R6_CORRECT_GAMMA_MAX_INTERVAL_V1',
  'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
  'model':'independent Gamma(N_p,1) clocks; Y=max(T_p,T_z)',
  'survivor_rows':189,'surviving_count_cells':9529,
  'grid_per_axis':G,'certified_ordered_cells':selected,
  'unresolved_ordered_cells':G*G-selected,
  'certified_fraction_of_full_square':str(fraction),
  'certified_area':str(fraction/4),
  'ratio_to_PREFIX708':str(ratio_708),
  'strict_all_real_q_ge_2_margin':'15701/1000000 times q^2',
  'PREFIX709_counterexample':{
    'point':'(191/384,191/384)',
    'count_max_bound_upper':'< 1',
    'true_gamma_max_variance_lower':'> 137',
    'issue':'PREFIX709 mistakes count-max survivor moments for gamma-max moments'
  },
  'zero_point_exact_gamma_mean':str(mu_00),
  'witness_floor_millionths':int((W_e-mu_e/2)*1000000),
  'verification':'ALL_CHECKS_PASS PREFIX710-R6',
  'grade':'AUTHOR_RECOMPUTED / EXACT_INTEGER_GAMMA_KERNEL / UNREVIEWED / NOT_ADMITTED'
}
Path(__file__).with_name('PREFIX710_R6_RESULTS.json').write_text(
    json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(result['verification'])
print('certified:',selected,'/',G*G,'fraction:',fraction)
print('gamma witness',result['witness_floor_millionths'],'; minimum margin floor',floor_micro)
print('PREFIX709 load-bearing upper bound falsified at (191/384,191/384)')
