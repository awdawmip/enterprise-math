#!/usr/bin/env python3
"""PREFIX-730: deduplicate PREFIX-729's 64 exact Gamma cells against PREFIX-712..718.
Run in research_notes/portable_direct with prior source files at their published pins.
No floating-point decision; author-level result pending independent review.
"""
from PREFIX729_R6_MONOTONE_SUBBOX import N,rows,coeff,Z,result as new_result
from functools import lru_cache
from fractions import Fraction as F
from pathlib import Path
import json

base=Path(__file__).parent
pin='f42f2906d77f24085c123f3ccfe9667d41caa96d'
assert new_result['frozen_science_pin'].endswith(pin)
assert new_result['whole_grid_cells_independently_certified']==64

def tail(a,d):
    pa=[1];pb=[1]
    for _ in range(N):pa.append(pa[-1]*a);pb.append(pb[-1]*(d-a))
    return [sum(v*pa[k]*pb[n-k] for k,v in row.items())*d**(N-1-n)
            for n,row in enumerate(rows[:N])]

def exact_raw_pairs(indices,d):
    T={i:tail(i,d) for i in indices}
    A={i:sum(T[i]) for i in indices}
    B={i:sum((n+1)*v for n,v in enumerate(T[i])) for i in indices}
    K0={};K1={}
    for j in indices:
        K0[j]=[sum(coeff[n][m]*T[j][m] for m in range(N) if T[j][m]) for n in range(N)]
        K1[j]=[sum((n+m+1)*coeff[n][m]*T[j][m] for m in range(N) if T[j][m]) for n in range(N)]
    dscale=d**(N-1);R=dscale*dscale*Z
    @lru_cache(None)
    def pair(i,j):
        if j<i:i,j=j,i
        mu=(A[i]+A[j])*dscale*Z-sum(x*y for x,y in zip(T[i],K0[j]))
        m2=2*(B[i]+B[j])*dscale*Z-sum(x*y for x,y in zip(T[i],K1[j]))
        return mu,m2
    return R,pair

R,pair=exact_raw_pairs(tuple(range(40,49)),384)
RE,epair=exact_raw_pairs((0,3),20)
em,em2=epair(0,3)
we_num=em2*RE-em*em
assert we_num>0
@lru_cache(None)
def old_all_q(a,b,c,d):
    lm,_=pair(a,b)
    _,hm2=pair(c,d)
    u=hm2*R-lm*lm
    return we_num*R*R>u*RE*RE and (2*we_num-em*RE)*R*R>(2*u-lm*R)*RE*RE

square={(i,j) for i in range(40,48) for j in range(40,48)}
old=set();coarse=0
for a in range(40,48,2):
    for b in range(40,48,2):
        if old_all_q(a,b,a+2,b+2):
            coarse+=1
            old.update((a+i,b+j) for i in (0,1) for j in (0,1))
        else:
            for i in (0,1):
                for j in (0,1):
                    if old_all_q(a+i,b+j,a+i+1,b+j+1):old.add((a+i,b+j))
assert coarse==0
assert old=={(40,40),(40,41),(41,40),(41,41),(40,42),(42,40)}

def load(name):return json.loads((base/name).read_text(encoding='utf-8'))
d713=load('PREFIX713_R6_RESULTS.json')
d713multi=load('PREFIX713_R6_MULTICOMPETITOR_RESULTS.json')
d716=load('PREFIX716_R6_RESULTS.json')
d718=load('PREFIX718_R6_RESULTS.json')
assert d713['scientific_pin']==d713multi['scientific_pin']==d716['scientific_pin']==d718['scientific_pin']==pin

def reflected(items):
    s=set(items)
    return s | {(j,i) for i,j in s}

coupled={(2*i+di,2*j+dj) for i,j in d713['full_child_parents'] for di in (0,1) for dj in (0,1)}
par=d713['extra_child'];coupled.add((2*par['parent'][0]+par['subcell'][0],2*par['parent'][1]+par['subcell'][1]))
coupled=reflected(coupled)
assert len(coupled)==90
multi=reflected((i,j) for i,j,_ in d713multi['additional_exact_cells']['all_q_ge_2'])
assert len(multi)==20
stage716=reflected(tuple(x) for x in d716['representatives'])
assert len(stage716)==1590
stage718=reflected(tuple(x) for x in d718['new_half_square_representatives'])
assert len(stage718)==150
later=coupled|multi|stage716|stage718
assert not square.intersection(later)
assert len(old)==6
increment=square-old
assert len(increment)==58
assert 137168+90+20+1590+150==139018
new_total=139018+len(increment)
assert new_total==139076
assert F(new_total,147456)==F(34769,36864)

result={
 'schema':'PREFIX730_R6_DEDUPLICATED_GAMMA_GRID_GAIN_V1',
 'frozen_science_pin':pin,
 'parent':'PREFIX-675','underlying_witness_certificate':'PREFIX729-R6',
 'old_base_prefix712_overlap_indices':[list(x) for x in sorted(old)],
 'old_base_overlap_count':len(old),
 'later_certificates_overlap_count':len(square&later),
 'certified_square_indices_half_open':[[40,48],[40,48]],
 'independently_certified_square_cells':len(square),
 'new_deduplicated_cells':len(increment),
 'new_deduplicated_indices':[list(x) for x in sorted(increment)],
 'prior_all_q_cells':139018,'new_all_q_cells':new_total,
 'new_fraction':str(F(new_total,147456)),
 'new_percent_approx_for_display_only':round(100*new_total/147456,9),
 'strict_uniform_witness_gap':'V_q(0,73/500)-V_q(p,z)>100*q^2 on [5/48,1/8]^2 for all real q>=2',
 'verification':'ALL_CHECKS_PASS PREFIX730-R6',
 'grade':'AUTHOR_EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED'
}
if __name__=='__main__':
    (base/'PREFIX730_R6_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('ALL_CHECKS_PASS PREFIX730-R6; +58 cells; total',new_total, 'fraction',result['new_fraction'])
