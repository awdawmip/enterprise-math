#!/usr/bin/env python3
"""PREFIX-707-R6 exact 256-cell corner certificate, frozen science.
Dependencies: PREFIX705 survivor monotonicity and PREFIX706 witness B lower bound.
All deciding comparisons use Fraction, never floating point.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

N=189
DEN=2**18
SCIENCE_PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'

@lru_cache(None)
def inside(m,k,a):
    return 40*(m+1)*comb(m,k)*a**k*(DEN-a)**(m-k)>DEN**m

@lru_cache(None)
def wide(m,k):
    if k>m//2: return wide(m,m-k)
    mid=k*DEN//m
    assert inside(m,k,mid)
    if k==0: left_lo=left_hi=0
    else:
        lo,hi=0,mid
        assert not inside(m,k,lo)
        while hi-lo>1:
            x=(hi+lo)//2
            if inside(m,k,x):hi=x
            else:lo=x
        left_lo,left_hi=lo,hi
    lo,hi=mid,DEN
    assert not inside(m,k,hi)
    while hi-lo>1:
        x=(hi+lo)//2
        if inside(m,k,x):lo=x
        else:hi=x
    right_lo,right_hi=lo,hi
    if 4*(right_lo-left_hi)>DEN:return True
    if 4*(right_hi-left_lo)<DEN:return False
    raise AssertionError(('uncertified width',m,k))

rows=[{0:1}]
for m in range(1,N+1):
    nxt=defaultdict(int)
    for k,v in rows[-1].items():
        nxt[k]+=v
        nxt[k+1]+=v
    rows.append({k:v for k,v in nxt.items() if wide(m,k)})
assert len(rows)==190 and not rows[189]
assert sum(map(len,rows[:N]))==9529
assert rows[25]=={k:comb(25,k) for k in range(1,25)}

@lru_cache(None)
def survival(p):
    a,b=p.numerator,p.denominator
    return tuple(F(sum(v*a**k*(b-a)**(n-k) for k,v in row.items()),b**n)
                 for n,row in enumerate(rows[:N]))

@lru_cache(None)
def moments_n(p):
    s=survival(p)
    en=sum(s,F(0))
    en2=sum(((2*n+1)*v for n,v in enumerate(s)),F(0))
    ed=189-en
    ed2=189*189-378*en+en2
    vt=en2+en-en*en
    assert vt==189+ed2-ed-ed*ed
    return en,en2,ed,ed2,vt

def cell_cap(l,r):
    assert 0<=l<=r<=F(1,2)
    en_l,en2_l,ed_l,ed2_l,_=moments_n(l)
    en_r,en2_r,ed_r,ed2_r,_=moments_n(r)
    low_form=en2_r+en_l-en_l*en_l
    high_form=189+ed2_l-ed_r-ed_r*ed_r
    assert low_form>=0 and high_form>=0
    return min(low_form,high_form)

def interval_cap(l,r,num=256):
    grid=[l+(r-l)*F(j,num) for j in range(num+1)]
    caps=[cell_cap(x,y) for x,y in zip(grid,grid[1:])]
    peak=max(caps)
    return peak,caps.index(peak)

def ticks(x):
    i=x.numerator*10**6//x.denominator
    return [i,i+1]

s64=survival(F(1,64))
L64=sum(((2*n+1)*v for n,v in enumerate(s64)),F(0))-600
sH=survival(F(1,2)-F(3,32))
U332=189+sum(((2*(189-n)-1)*(1-v) for n,v in enumerate(sH)),F(0))
assert ticks(L64)==[275220940,275220941]
assert ticks(U332)==[279763526,279763527]

a,b=F(1,18),F(1,6)
assert a+b<F(1,2)
low_bound,low_peak=interval_cap(F(0),a)
high_bound,high_peak=interval_cap(F(1,2)-b,F(1,2))
B_lower=F(559812917,1000000)
C=max(low_bound,high_bound)
gap_lower=B_lower-2*C
assert gap_lower>F(119,10)
assert ticks(low_bound)==[263733972,263733973]
assert ticks(high_bound)==[273906511,273906512]
assert ticks(gap_lower)==[11999893,11999894]
area=(a+b)**2
assert area==F(4,81)
assert area/F(49,4096)==F(16384,3969)
assert area/F(1,4)==F(16,81)

result={
  'schema':'PREFIX707_R6_PARTITIONED_CORNER_CERTIFICATE_V1',
  'date':'2026-11-11 Asia/Shanghai',
  'scientific_pin':SCIENCE_PIN,
  'source_preconditions':[
    'PREFIX700 frozen 189-level survivor recurrence',
    'PREFIX705 exact stochastic monotonicity of s_n on [0,1/2]',
    'PREFIX706 exact witness B>559812917/1000000',
    'Efron-Stein bound for max of independent clocks'],
  'survivor_cells':9529,'partition_cells_per_interval':256,
  'low_interval':['0','1/18'],'high_interval':['1/3','1/2'],
  'max_single_clock_variance_cap_low_ticks':ticks(low_bound),
  'max_single_clock_variance_cap_high_ticks':ticks(high_bound),
  'low_max_cell_index_zero_based':low_peak,
  'high_max_cell_index_zero_based':high_peak,
  'B_strict_lower_bound':str(B_lower),
  'uniform_competitor_gap_strict_lower_ticks':ticks(gap_lower),
  'uniform_gap_claim':'V_q(e)-V_q(x)>119*q^2/10 for all real q>=2 and x in C',
  'excluded_area':str(area),'fraction_of_full_auxiliary_square':str(area/F(1,4)),
  'area_multiple_vs_PREFIX706':str(area/F(49,4096)),
  'recomputed_regression_L_1_64_ticks':ticks(L64),
  'recomputed_regression_U_3_32_ticks':ticks(U332),
  'verification':'ALL_CHECKS_PASS PREFIX707-R6',
  'admission':'AUTHOR_RECOMPUTED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED'
}
Path(__file__).with_name('PREFIX707_R6_RESULTS.json').write_text(
    json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS PREFIX707-R6')
print('Low/high variance caps:',ticks(low_bound),ticks(high_bound))
print('Gap:',ticks(gap_lower),'area:',area,'ratio:',area/F(49,4096))
