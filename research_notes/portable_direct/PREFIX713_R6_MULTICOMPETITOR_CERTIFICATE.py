#!/usr/bin/env python3
"""PREFIX-713: exact, sparse additional Gamma-clock grid exclusion witnesses.
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
No binary floats participate in any certification test.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

N=189
WD=1<<18
@lru_cache(None)
def inside(m,k,a):
    return 40*(m+1)*comb(m,k)*a**k*(WD-a)**(m-k)>WD**m
@lru_cache(None)
def wide(m,k):
    if k>m//2:return wide(m,m-k)
    mid=k*WD//m
    assert inside(m,k,mid)
    if k==0: left_lo=left_hi=0
    else:
        lo,hi=0,mid
        while hi-lo>1:
            x=(lo+hi)//2
            if inside(m,k,x):hi=x
            else:lo=x
        left_lo,left_hi=lo,hi
    lo,hi=mid,WD
    while hi-lo>1:
        x=(lo+hi)//2
        if inside(m,k,x):lo=x
        else:hi=x
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
assert rows[-1]=={}
assert sum(map(len,rows[:N]))==9529
assert rows[25]=={k:comb(25,k) for k in range(1,25)}
print('Exact frozen rows: 189; nonzero cells: 9529',flush=True)
# Common rational Gamma maximum kernel (PREFIX-710 corrected kernel).
Z=1<<(2*N-1)
coeff=[[comb(n+m,n) << (2*N-2-n-m) for m in range(N)] for n in range(N)]
coeff1=[[(n+m+1)*coeff[n][m] for m in range(N)] for n in range(N)]

@lru_cache(None)
def axis(a,d):
    # All survival polynomials scaled by d^(N-1).
    ap=[1];bp=[1]
    for _ in range(N):
        ap.append(ap[-1]*a);bp.append(bp[-1]*(d-a))
    T=[sum(v*ap[k]*bp[n-k] for k,v in row.items())*d**(N-1-n)
       for n,row in enumerate(rows[:N])]
    return T

@lru_cache(None)
def pair(i,j):
    # Fine cell lattice: x=(i/768,j/768), integer counts with common denominator.
    if j<i:i,j=j,i
    d=768;L=d**(N-1);R=L*L*Z
    A=axis(i,d);B=axis(j,d)
    s1=(sum(A)+sum(B))*L*Z
    s2=2*(sum((n+1)*x for n,x in enumerate(A))+sum((m+1)*x for m,x in enumerate(B)))*L*Z
    nzA=[(n,x) for n,x in enumerate(A) if x]
    nzB=[(m,x) for m,x in enumerate(B) if x]
    cross0=sum(x*y*coeff[n][m] for n,x in nzA for m,y in nzB)
    cross1=sum(x*y*coeff1[n][m] for n,x in nzA for m,y in nzB)
    return F(s1-cross0,R),F(s2-cross1,R)

@lru_cache(None)
def edge(z):
    # p=0: its exact survivor tail is 1 for n<25, zero after.
    T=axis(z.numerator,z.denominator)
    L=z.denominator**(N-1);R=L*Z
    C0=[sum(coeff[n][m] for n in range(25)) for m in range(N)]
    C1=[sum(coeff1[n][m] for n in range(25)) for m in range(N)]
    mu=F((25*L+sum(T))*Z-sum(v*c for v,c in zip(T,C0)),R)
    m2=F(2*(325*L+sum((m+1)*v for m,v in enumerate(T)))*Z-sum(v*c for v,c in zip(T,C1)),R)
    return mu,m2-mu*mu

comparators={
 'old_3_20':F(3,20),
 'new_147_1000':F(147,1000),
 'new_59_400':F(59,400),
 'new_297_2000':F(297,2000)
}
C={k:edge(z) for k,z in comparators.items()}
mu0,W0=C['old_3_20']
assert F(559812917,1000000) < W0-mu0/2 < F(559812918,1000000)
# Ordered cells of the 384x384 grid. Each is [i/768,(i+1)/768] x [j/768,(j+1)/768].
extra_all=[
 (1,79,'new_59_400'),(9,81,'new_147_1000'),(21,85,'new_59_400'),
 (28,88,'new_59_400'),(30,89,'new_59_400'),(32,90,'new_59_400'),
 (34,91,'new_59_400'),(49,101,'new_59_400'),
 (57,163,'new_297_2000'),(74,138,'new_297_2000'),
 (79,1,'new_59_400'),(81,9,'new_147_1000'),(85,21,'new_59_400'),
 (88,28,'new_59_400'),(89,30,'new_59_400'),(90,32,'new_59_400'),
 (91,34,'new_59_400'),(101,49,'new_59_400'),
 (138,74,'new_297_2000'),(163,57,'new_297_2000')]
extra_range=[
 (17,169,'new_297_2000'),(74,141,'new_297_2000'),
 (74,142,'new_297_2000'),(141,74,'new_297_2000'),
 (142,74,'new_297_2000'),(169,17,'new_297_2000')]
assert len(extra_all)==20 and len(extra_range)==6
assert len(set((i,j) for i,j,_ in extra_all))==20
assert len(set((i,j) for i,j,_ in extra_range))==6

@lru_cache(None)
def gap_for_cell(i,j,label,t):
    lo_mu=pair(i,j)[0]
    hi_m2=pair(i+1,j+1)[1]
    U=hi_m2-lo_mu**2
    e_mu,e_w=C[label]
    return e_w-U-t*(e_mu-lo_mu)

# Every selected cell failed the exact prior fixed-comparator endpoint certificate;
# each passes BOTH endpoints under the new stated single comparator.
minimums={}
for kind,cells,ends in [
 ('all_q_ge_2',extra_all,(F(0),F(1,2))),
 ('q_12_to_24',extra_range,(F(1,24),F(1,12)))]:
    vals=[]
    for i,j,label in cells:
        old=[gap_for_cell(i,j,'old_3_20',t) for t in ends]
        new=[gap_for_cell(i,j,label,t) for t in ends]
        assert min(old)<=0,(kind,i,j,'already in old certified cells')
        assert min(new)>0,(kind,i,j,label,'failed new exact certificate')
        vals+=new
    m=min(vals)
    minimums[kind]={'lower_floor_millionths':(m.numerator*1000000)//m.denominator,
                    'comparison_count':2*len(cells)}
    print(kind,'new cells',len(cells),'minimum gap >',
          str(F(minimums[kind]['lower_floor_millionths'],1000000)),flush=True)

# Previous immutable PREFIX-712 exact exhaustive verifier establishes
# 137168 and 137398 old certified fine-cell interiors. Proven disjointness above
# gives lower bounds, without needing to re-test those inherited 147456 cells.
new_total_all=137168+20
new_total_range=137398+6
assert new_total_all==137188 and new_total_range==137404
assert len(extra_all)==len(set((i,j) for i,j,_ in extra_all))
assert len(extra_range)==len(set((i,j) for i,j,_ in extra_range))
results={
 'schema':'PREFIX713_R6_SPARSE_MULTICOMPETITOR_V1',
 'date':'2026-11-12',
 'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'parent':'PREFIX-675',
 'base':'PREFIX-712 exact 384x384 continuous Gamma max certificate',
 'grid_denominator':768,
 'base_area_certificate_count':{'all_q_ge_2':137168,'q_12_to_24':137398},
 'additional_exact_cells':{'all_q_ge_2':[[i,j,k] for i,j,k in extra_all],
                           'q_12_to_24':[[i,j,k] for i,j,k in extra_range]},
 'comparators':{k:str(z) for k,z in comparators.items()},
 'minimum_extra_cell_gaps':minimums,
 'lower_bound_certified_counts':{'all_q_ge_2':new_total_all,'q_12_to_24':new_total_range},
 'fractions':{'all_q_ge_2':str(F(new_total_all,384*384)),
              'q_12_to_24':str(F(new_total_range,384*384))},
 'proof_semantics':'Exact endpoint strict inequalities on every new closed cell; inherited PREFIX-712 certificate on all old cells.  No floating-point acceptance.',
 'author_check':'ALL_CHECKS_PASS PREFIX713-R6',
 'evidence_status':'AUTHOR_RECOMPUTED / EXACT_INTEGER_GAMMA_KERNEL / UNREVIEWED / NOT_ADMITTED'
}
path=Path(__file__).with_name('PREFIX713_R6_RESULTS.json')
path.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS PREFIX713-R6',flush=True)
