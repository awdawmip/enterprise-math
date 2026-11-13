#!/usr/bin/env python3
"""PREFIX-760/R6: exact finite Gamma moments, variance and row-25 gap checks.
Frozen BRC width recurrence faithfully reproduced from PREFIX754.
Stdlib only; all signs checked by Fraction, never from floating output.
"""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from math import comb, factorial
from pathlib import Path
import json

N=189
W=1<<18

@lru_cache(None)
def inside(n,k,x):
    return 40*(n+1)*comb(n,k)*x**k*(W-x)**(n-k)>W**n

@lru_cache(None)
def wide(n,k):
    if k>n//2:return wide(n,n-k)
    mid=k*W//n
    assert inside(n,k,mid)
    if k==0:lo=hi=0
    else:
        a,b=0,mid
        while b-a>1:
            x=(a+b)//2
            if inside(n,k,x):b=x
            else:a=x
        lo,hi=a,b
    a,b=mid,W
    while b-a>1:
        x=(a+b)//2
        if inside(n,k,x):a=x
        else:b=x
    if 4*(a-hi)>W:return True
    if 4*(b-lo)<W:return False
    raise ValueError(('undecidable-width',n,k))

rows=[{0:1}]
for n in range(1,N+1):
    conv=defaultdict(int)
    for k,v in rows[-1].items():conv[k]+=v;conv[k+1]+=v
    rows.append({k:v for k,v in conv.items() if wide(n,k)})
assert not rows[N] and sum(map(len,rows[:N]))==9529

@lru_cache(None)
def survivors(z):
    z=Q(z);a,b=z.numerator,z.denominator-z.numerator
    aa=[1];bb=[1]
    for _ in range(N):aa.append(aa[-1]*a);bb.append(bb[-1]*b)
    out=tuple(Q(sum(v*aa[k]*bb[n-k] for k,v in r.items()),z.denominator**n) for n,r in enumerate(rows[:N]))
    assert out[:25]==(Q(1),)*25
    assert out[25]==1-z**25-(1-z)**25
    assert all(0<=y<=x<=1 for x,y in zip(out,out[1:]))
    return out

@lru_cache(None)
def kernel(i,j):
    a=Q(comb(i+j,i),2**(i+j+1))
    return a,(i+j+1)*a

def exact_moments(p,z):
    s,t=survivors(Q(p)),survivors(Q(z))
    cross1=cross2=Q(0)
    for i,si in enumerate(s):
        if not si:continue
        for j,tj in enumerate(t):
            if not tj:continue
            k1,k2=kernel(i,j)
            v=si*tj
            cross1+=v*k1;cross2+=v*k2
    mu=sum(s)+sum(t)-cross1
    second=2*sum((i+1)*(s[i]+t[i]) for i in range(N))-cross2
    return mu,second,second-mu**2

def beta_bound(m,z):
    s=survivors(z)
    first=Q(m*factorial(m+24),factorial(25))
    for j,sj in enumerate(s):
        if sj:
            first-=sj*Q(m*factorial(m+24+j),factorial(25)*factorial(j)*2**(m+25+j))
    return first

def older_bound(m,z):
    g=z**25+(1-z)**25
    x=sum(comb(m+49,k) for k in range(25,m+50))
    return g*Q(m*factorial(m+24)*x,factorial(25)*2**(m+49))

def sign(x):return 1 if x>0 else (-1 if x<0 else 0)
def decimal(x):return format(float(x),'.16g')

result={'schema':'PREFIX760_R6_EXACT_GAMMA_VARIANCE_V1',
'scientific_input_commit':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
'scope':'external two-independent-Gamma clock auxiliary, not native X6',
'survivor_layers':N,'positive_count_positions':sum(map(len,rows[:N])),
'checker':'Python3 stdlib Fraction/int, exact signs and identities',
'second_clock_moment_improvement':{},'variance_comparisons':{}}

for z in [Q(0),Q(1,4),Q(1,2)]:
    items={}
    for m in (1,2):
        now,old=beta_bound(m,z),older_bound(m,z)
        assert now>=old>0
        assert (now==old)==(z==0)
        items[str(m)]={'exact_bound':f'{now.numerator}/{now.denominator}',
            'decimal':decimal(now),'prefix759_bound':decimal(old),
            'multiplicative_improvement':decimal(now/old)}
    result['second_clock_moment_improvement'][str(z)]=items
    print('MOMENT',str(z),items['1']['decimal'],items['2']['decimal'],items['1']['multiplicative_improvement'])

p0,p1=Q(0),Q(1,4)
for z in [Q(0),Q(1,16),Q(5,64),Q(3,32),Q(1,4),Q(1,2)]:
    a,b,c=exact_moments(p0,z)
    A,B,C=exact_moments(p1,z)
    dmu=A-a;dm2=B-b;dv=C-c
    dvq2=4*dv-2*dmu
    assert dmu>0 and dm2>0
    if z==0:
        assert Q(367)<dv<Q(369) and Q(111)<dmu<Q(112)
        assert dvq2>Q(1249)
    if z==Q(1,16):assert dvq2>Q(259)
    if z==Q(5,64):assert dv>Q(14) and dvq2<Q(-113)
    if z==Q(3,32):assert dv<Q(-78)
    if z==Q(1,4):assert dv<Q(-159) and dvq2<Q(-659) and dmu>Q(10)
    if z==Q(1,2):assert dv<Q(-3) and dvq2<Q(-14)
    result['variance_comparisons'][str(z)]={'p0':'0','p1':'1/4',
        'delta_mean':decimal(dmu),'delta_second_raw':decimal(dm2),
        'delta_variance':decimal(dv),'delta_Vq_at_q2':decimal(dvq2),
        'delta_variance_sign':sign(dv),'delta_Vq_at_q2_sign':sign(dvq2),
        'exact_delta_variance_numerator':str(dv.numerator),
        'exact_delta_variance_denominator':str(dv.denominator),
        'exact_delta_Vq2_numerator':str(dvq2.numerator),
        'exact_delta_Vq2_denominator':str(dvq2.denominator)}
    print('VAR',z,'delta_mu',decimal(dmu),'delta_var',decimal(dv),'delta_V_2',decimal(dvq2))

def min_moment(r,a,b):
    return r*sum(Q(factorial(r+i+j-1),factorial(i)*factorial(j)*2**(r+i+j)) for i in range(a) for j in range(b))
assert min_moment(1,1,1)==Q(1,2)
assert min_moment(2,1,1)==Q(1,2)
assert min_moment(1,1,2)==Q(3,4)
assert min_moment(2,1,2)==Q(1,1)
assert beta_bound(1,Q(0))==older_bound(1,Q(0))
result['conclusions']={
 'variance_not_coordinate_monotone':'ΔVar(z=0)>367, ΔVar(z=1/4)<-159',
 'Vq_not_coordinate_monotone_for_every_q_at_least_2':'ΔV_q(z=0)>0, ΔV_q(z=1/4)<0',
 'q2_zero_in_open_interval':'z in (1/16,5/64), by continuity and exact signs',
 'variance_zero_in_open_interval':'z in (5/64,3/32), by continuity and exact signs',
 'maximality_or_unique_root_claimed':False,
 'uncertainty':'no native X6 transfer, no independent peer review'}
path=Path(__file__).with_name('PREFIX760_R6_EXACT_GAMMA_VARIANCE_RESULTS.json')
path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS PREFIX760 exact finite moment, variance, q2 root-bracketing and full-second-clock bounds')
