#!/usr/bin/env python3
"""PREFIX-713: exact Gamma-clock witness improvement. Scientific pin:
awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
All claimed inequalities use Python integers/Fraction, never floating point."""
from collections import defaultdict
from functools import lru_cache
from math import comb
from fractions import Fraction as Q
import json
from pathlib import Path

N=189; WD=1<<18
@lru_cache(None)
def inside(m,k,a):
    return 40*(m+1)*comb(m,k)*a**k*(WD-a)**(m-k)>WD**m
@lru_cache(None)
def wide(m,k):
    if k>m//2: return wide(m,m-k)
    mid=k*WD//m
    assert inside(m,k,mid)
    if k==0: llo=lhi=0
    else:
        lo,hi=0,mid
        while hi-lo>1:
            h=(lo+hi)//2
            if inside(m,k,h): hi=h
            else: lo=h
        llo,lhi=lo,hi
    lo,hi=mid,WD
    while hi-lo>1:
        h=(lo+hi)//2
        if inside(m,k,h): lo=h
        else: hi=h
    rlo,rhi=lo,hi
    if 4*(rlo-lhi)>WD: return True
    if 4*(rhi-llo)<WD: return False
    raise AssertionError((m,k))

rows=[{0:1}]
for m in range(1,N+1):
    d=defaultdict(int)
    for k,v in rows[-1].items(): d[k]+=v;d[k+1]+=v
    rows.append({k:v for k,v in d.items() if wide(m,k)})
assert rows[-1]=={} and sum(map(len,rows[:N]))==9529
assert rows[25]=={k:comb(25,k) for k in range(1,25)}
Z=2**(2*N-1)
c0=[sum(comb(n+m,n)*2**(2*N-2-n-m) for n in range(25)) for m in range(N)]
c1=[sum((n+m+1)*comb(n+m,n)*2**(2*N-2-n-m) for n in range(25)) for m in range(N)]

def moments(z):
    z=Q(z);a=z.numerator;den=z.denominator;b=den-a
    scale=den**(N-1);pa=[1];pb=[1]
    for _ in range(N): pa.append(pa[-1]*a);pb.append(pb[-1]*b)
    tail=[sum(v*pa[k]*pb[n-k] for k,v in row.items())*den**(N-1-n)
          for n,row in enumerate(rows[:N])]
    mu=Q((25*scale+sum(tail))*Z-sum(v*c for v,c in zip(tail,c0)),scale*Z)
    m2=Q(2*(325*scale+sum((m+1)*v for m,v in enumerate(tail)))*Z
         -sum(v*c for v,c in zip(tail,c1)),scale*Z)
    return mu,m2-mu*mu

oldz=Q(3,20);hi_z=Q(149,1000);lo_z=Q(146,1000)
m0,w0=moments(oldz);mhi,whi=moments(hi_z);mlo,wlo=moments(lo_z)
dw=whi-w0;dm=m0-mhi
assert dw>Q(5224,100000) and dm>Q(5474,10000)
assert mlo<mhi and wlo<whi
tcross=(whi-wlo)/(mhi-mlo)
assert Q(23,100)<tcross<Q(24,100)
for t in (Q(0),Q(1,2),Q(1,12),Q(1,24),tcross):
    assert max(whi-t*mhi,wlo-t*mlo)>w0-t*m0
assert whi>w0 and mhi<m0
out={
  'schema':'PREFIX713_R6_EXACT_GAMMA_WITNESS_ENVELOPE_V1',
  'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
  'model':'independent Gamma(N_p,1) completion clocks, max of two clocks',
  'count_rows':189,'nonzero_count_cells':9529,
  'old_witness':'(0,3/20)',
  'new_witnesses':['(0,149/1000)','(0,146/1000)'],
  'old_witness_strictly_dominated':True,
  'certified_W_increase_lower':'5224/100000',
  'certified_mean_decrease_lower':'5474/10000',
  'two_witness_cross_t_interval':'(23/100,24/100)',
  'cross_t_approx':str(round(float(tcross),12)),
  'cross_q_approx':str(round(float(1/tcross),12)),
  'author_verification':'ALL_CHECKS_PASS PREFIX713-R6',
  'grade':'AUTHOR_RECOMPUTED / EXACT_INTEGER_GAMMA_KERNEL / UNREVIEWED / NOT_ADMITTED'
}
Path(__file__).with_name('PREFIX713_R6_RESULTS.json').write_text(
    json.dumps(out,indent=2)+'\n')
print('ALL_CHECKS_PASS PREFIX713-R6')
