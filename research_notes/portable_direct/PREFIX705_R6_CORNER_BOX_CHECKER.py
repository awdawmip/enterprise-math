#!/usr/bin/env python3
"""PREFIX705: exact BRC survivor stochastic order + all-q corner-box certificate."""
import runpy, json
from fractions import Fraction as F
from math import comb
from pathlib import Path

root=Path(__file__).resolve().parent
b=runpy.run_path(str(root/'PREFIX700_R6_STRICT_OPTIMIZER_ORDER.py'))
rows,survive,moments=b['rows'],b['survive'],b['moments']
assert b['N']==189 and sum(len(r) for r in rows[:189])==9529
zpos=ppos=0
for n in range(1,189):
    r=[F(rows[n].get(k,0),comb(n,k)) for k in range(n+1)]
    a=[n*(r[k+1]-r[k]) for k in range(n)]
    left=[a[0]]
    while len(a)>1:
        a=[(a[k]+a[k+1])/2 for k in range(len(a)-1)]
        left.append(a[0])
    assert min(left)>=0,(n,min(left))
    zpos+=sum(x==0 for x in left)
    ppos+=sum(x>0 for x in left)
assert (zpos,ppos)==(4513,13253)
eps=F(1,64)
lo=survive(eps);hi=survive(F(1,2)-eps)
low_bound=sum(((2*n+1)*s for n,s in enumerate(lo)),F(0))-600
high_bound=189+sum(((2*(189-n)-1)*(1-s) for n,s in enumerate(hi)),F(0))
mu,w=moments(F(0),F(3,20))
witness_bound=w-mu/2
margin=witness_bound-2*max(low_bound,high_bound)
assert low_bound<F(1101,4) and high_bound<F(773,4)
assert witness_bound>F(2799,5) and margin>F(93,10)
area_multiplier=F(43251**2,2048)
assert area_multiplier>900000

def ticks(x):
    i=(x*1000000).__floor__()
    return [i,i+1]
result={
 'schema':'PREFIX705_R6_BERNSTEIN_STOCHASTIC_ORDER_CORNER_BOX_V1',
 'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'surviving_cells':9529,
 'tail_derivative_bernstein_coefficients':{'total':17766,'nonnegative':17766,'zero':zpos,'positive':ppos,'negative':0},
 'clock_upper_bounds_millionth_ticks':{'low_p_le_1_64':ticks(low_bound),'high_p_ge_31_64':ticks(high_bound)},
 'witness_W_minus_mu_over_2_millionth_ticks':ticks(witness_bound),
 'strict_margin_millionth_ticks':ticks(margin),
 'q_domain':'real q>=2',
 'excluded_boxes':'four closed square corners, side length 1/64',
 'exclusion_margin':'V_q(0,3/20)-V_q(p,z)>93*q^2/10',
 'excluded_total_area':'1/1024',
 'area_multiplier_vs_PREFIX704_triangles':str(area_multiplier),
 'reuses':['PREFIX700_R6_STRICT_OPTIMIZER_ORDER.py','PREFIX701','PREFIX704'],
 'validation':'ALL_CHECKS_PASS PREFIX705-R6',
 'admission':'AUTHOR_RECOMPUTED/EXACT_FRACTION_BERNSTEIN_CHECKED/UNREVIEWED/NOT_ADMITTED'
}
(root/'PREFIX705_R6_RESULTS.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS PREFIX705-R6')
print('Bernstein coefficient counts:',zpos,ppos)
print('clock variance U ticks:',ticks(low_bound),ticks(high_bound))
print('witness threshold ticks:',ticks(witness_bound),'strict gap ticks:',ticks(margin))
print('area multiplier:',area_multiplier)
