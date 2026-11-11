#!/usr/bin/env python3
"""PREFIX-709-R6: exact two-stream joint-survivor interval certificate.

Frozen BRC statistical input: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Dependencies: PREFIX-705 survivor-tail monotonicity; PREFIX-706 exact witness
  W(0,3/20)-mu(0,3/20)/2 > 559812917/1000000.
No floating-point operation participates in a comparison.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json

N, WIDTH_DEN, G = 189, 1 << 18, 192
B = Q(559812917, 1000000)
PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'

@lru_cache(None)
def inside(m, k, a):
    return 40*(m+1)*comb(m,k)*a**k*(WIDTH_DEN-a)**(m-k) > WIDTH_DEN**m

@lru_cache(None)
def wide(m, k):
    if k > m//2:
        return wide(m, m-k)
    mid = k*WIDTH_DEN//m
    assert inside(m, k, mid)
    if k == 0:
        left_lo = left_hi = 0
    else:
        lo, hi = 0, mid
        assert not inside(m,k,lo)
        while hi-lo > 1:
            z = (lo+hi)//2
            if inside(m,k,z): hi=z
            else: lo=z
        left_lo,left_hi=lo,hi
    lo,hi=mid,WIDTH_DEN
    assert not inside(m,k,hi)
    while hi-lo > 1:
        z=(lo+hi)//2
        if inside(m,k,z): lo=z
        else: hi=z
    right_lo,right_hi=lo,hi
    if 4*(right_lo-left_hi)>WIDTH_DEN: return True
    if 4*(right_hi-left_lo)<WIDTH_DEN: return False
    raise AssertionError(('uncertified width',m,k))

rows=[{0:1}]
for m in range(1,N+1):
    nxt=defaultdict(int)
    for k,v in rows[-1].items():
        nxt[k]+=v; nxt[k+1]+=v
    rows.append({k:v for k,v in nxt.items() if wide(m,k)})
assert rows[-1]=={} and sum(map(len,rows[:N]))==9529
assert rows[25]=={k:comb(25,k) for k in range(1,25)}

D=2*G
powers=[D**k for k in range(2*N)]
scale=powers[N-1]
scale2=scale*scale

def survival_numerators(i):
    ps=[1]; qs=[1]
    for _ in range(N):
        ps.append(ps[-1]*i);qs.append(qs[-1]*(D-i))
    return [sum(v*ps[k]*qs[n-k] for k,v in row.items())
            for n,row in enumerate(rows[:N])]

surv=[survival_numerators(i) for i in range(G+1)]
A=[sum(num*powers[N-1-n] for n,num in enumerate(s)) for s in surv]
C=[sum((2*n+1)*num*powers[N-1-n] for n,num in enumerate(s)) for s in surv]
weights=[powers[2*(N-1-n)] for n in range(N)]

@lru_cache(None)
def joint_moments(i,j):
    # Returns mean, second raw moment as integers over scale2.
    if i>j: return joint_moments(j,i)
    prod=[x*y*w for x,y,w in zip(surv[i],surv[j],weights)]
    return ((A[i]+A[j])*scale-sum(prod),
            (C[i]+C[j])*scale-sum((2*n+1)*z for n,z in enumerate(prod)))

chosen=0
smallest_gap_numerator=None
bound_denom=B.denominator*scale2**2
threshold=B.numerator*scale2**2
undecided=0
for i in range(G):
    for j in range(i,G):
        mu_lo,m2_lo=joint_moments(i,j)
        mu_hi,m2_hi=joint_moments(i+1,j+1)
        upper_raw = m2_hi*scale2-mu_lo**2
        upper_comp = (N*N*scale2-2*N*mu_lo+m2_lo)*scale2 - (N*scale2-mu_hi)**2
        upper=min(upper_raw,upper_comp)
        delta=threshold-B.denominator*upper
        if delta>0:
            chosen+=1 if i==j else 2
            if smallest_gap_numerator is None or delta<smallest_gap_numerator:
                smallest_gap_numerator=delta
        else:
            undecided+=1 if i==j else 2

assert chosen==33766
assert undecided==3098
assert chosen+undecided==G*G
assert smallest_gap_numerator is not None
floor_millionths=(1000000*smallest_gap_numerator)//bound_denom
assert floor_millionths==169821
assert smallest_gap_numerator*1000000>169821*bound_denom
excluded=Q(chosen,G*G)
assert excluded==Q(16883,18432)
ratio_old=excluded/Q(345931,1048576)
result={
    'schema':'PREFIX709_R6_EXACT_JOINT_SURVIVOR_CERTIFICATE_V1',
    'date':'2026-11-12 Asia/Shanghai',
    'scientific_pin':PIN,
    'dependencies':['PREFIX-705 stochastic monotonicity','PREFIX-706 witness lower bound'],
    'count_rows':N,'nonzero_survivor_cells':9529,
    'cells_per_axis':G,'certified_closed_cells':chosen,'undecided_cells':undecided,
    'certified_fraction_of_square':str(excluded),
    'certified_area':str(excluded/4),
    'certified_ratio_to_PREFIX708_area':str(ratio_old),
    'strict_uniform_gap_lower_bound':'169821/1000000',
    'verification':'ALL_CHECKS_PASS PREFIX709-R6',
    'grade':'AUTHOR_RECOMPUTED / EXACT_INTEGER_RATIONAL / UNREVIEWED / NOT_ADMITTED'
}
Path(__file__).with_name('PREFIX709_R6_RESULTS.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print(result['verification'])
print('certified',chosen,'/',G*G, 'fraction=',excluded, 'ratio_to_708=',ratio_old)
print('minimum gap floor millionths=',floor_millionths)
