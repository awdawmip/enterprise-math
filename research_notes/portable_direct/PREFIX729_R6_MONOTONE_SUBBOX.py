#!/usr/bin/env python3
"""PREFIX-729. Run beside PREFIX726_R6_GAMMA_WITNESS_LIPSCHITZ.py.
Pinned BRC science f42f2906d77f24085c123f3ccfe9667d41caa96d.
Exact integer/directed-floor certificate; no floating point acceptance.
"""
from PREFIX726_R6_GAMMA_WITNESS_LIPSCHITZ import N, rows, coeff, Z
from math import comb
from pathlib import Path
import json

S=10**6
A,B,D=80,96,768
for n,row in enumerate(rows[:N]):
    for k in range(n+1):
        assert row.get(k,0)==row.get(n-k,0)
        assert 0<=row.get(k,0)<=comb(n,k)
    for k in range(n//2):
        assert row.get(k+1,0)*comb(n,k)>=row.get(k,0)*comb(n,k+1)
# Therefore s_n(x) is nondecreasing for x<=1/2; the Gamma survival
# mixtures and mu=E[max(Tp,Tz)], M2=E[max(Tp,Tz)^2] are coordinatewise monotone.
def tail(a,d):
    aa=[1];bb=[1]
    for _ in range(N):aa.append(aa[-1]*a);bb.append(bb[-1]*(d-a))
    return [sum(v*aa[k]*bb[n-k] for k,v in row.items())*d**(N-1-n)
            for n,row in enumerate(rows[:N])]
def lookup(indices,den):
    t={i:tail(i,den) for i in indices}
    sum0={i:sum(t[i]) for i in indices}
    sum1={i:sum((n+1)*v for n,v in enumerate(t[i])) for i in indices}
    k0={};k1={}
    for j in indices:
        k0[j]=[sum(coeff[n][m]*t[j][m] for m in range(N) if t[j][m]) for n in range(N)]
        k1[j]=[sum((n+m+1)*coeff[n][m]*t[j][m] for m in range(N) if t[j][m]) for n in range(N)]
    d=den**(N-1);R=d*d*Z
    def moment_floor(i,j):
        mu=(sum0[i]+sum0[j])*d*Z-sum(x*y for x,y in zip(t[i],k0[j]))
        m2=2*(sum1[i]+sum1[j])*d*Z-sum(x*y for x,y in zip(t[i],k1[j]))
        assert mu>0 and m2>0
        return mu*S//R,m2*S//R
    return moment_floor

grid=lookup(tuple(range(A,B+1)),D)
mu_e,m2_e=lookup((0,73),500)(0,73)
assert 88*S<mu_e<89*S
# Exact directed bounds: floor(x*S)/S <= x < (floor(x*S)+1)/S.
W_e_lower_num=m2_e*S-(mu_e+1)**2
assert W_e_lower_num>600*S*S
cache={}
def get(i,j):
    key=(min(i,j),max(i,j))
    if key not in cache:cache[key]=grid(*key)
    return cache[key]
min_num=None;argmin=None
for i in range(A,B):
    for j in range(A,B):
        mu_l,_=get(i,j)
        _,m2_h=get(i+1,j+1)
        # f_t(e)-f_t(x) >= W_e-M2(h)+mu(l)^2-t*(mu_e-mu(l)).
        # Take t endpoints 0,1/2. All numerators share 2*S^2.
        gap0=W_e_lower_num-(m2_h+1)*S+mu_l*mu_l
        gap=min(2*gap0, 2*gap0-S*(mu_e+1-mu_l))
        if min_num is None or gap<min_num:min_num,argmin=gap,(i,j)
        assert gap>200*S*S,(i,j,gap)
assert len(cache)==152
result={
 'schema':'PREFIX729_R6_MONOTONE_GAMMA_SUBBOX_V1',
 'frozen_science_pin':'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'predecessor':'PREFIX726_R6_GAMMA_WITNESS_LIPSCHITZ.py',
 'domain':'all (p,z) in [5/48,1/8]^2; every real q>=2',
 'witness':['0','73/500'],
 'subbox_index_range_half_open':[[80,96],[80,96]],
 'subbox_denominator':768,'subboxes':256,
 'whole_grid_cell_indices_half_open':[[40,48],[40,48]],
 'whole_grid_cells_independently_certified':64,
 'floor_scale':S,'minimum_gap_numerator_over_2scale_squared':str(min_num),
 'limiting_subbox':list(argmin),'distinct_moment_pairs':len(cache),
 'witness_mu_floor':mu_e,'witness_m2_floor':m2_e,
 'strict_comparison':'V_q(witness)-V_q(p,z)>100*q^2',
 'prior_union':139018,'dedup_with_prior_union':'PENDING; no additive count',
 'grade':'AUTHOR_EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED',
 'verification':'ALL_CHECKS_PASS PREFIX729-R6'
}
if __name__=='__main__':
    Path(__file__).with_name('PREFIX729_R6_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['verification'], 'minimum numerator:',min_num, 'argmin:',argmin)
