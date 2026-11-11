#!/usr/bin/env python3
"""Exact extension of PREFIX705 stochastic-order corner exclusion.

Requires existing PREFIX700_R6_STRICT_OPTIMIZER_ORDER.py alongside this file.
Exact 189-level frozen survival computation; does not perform native X6 evolution.
"""
import runpy, json
from fractions import Fraction as F
from pathlib import Path

root=Path(__file__).resolve().parent
b=runpy.run_path(str(root/'PREFIX700_R6_STRICT_OPTIMIZER_ORDER.py'))
assert b['N']==189 and sum(map(len,b['rows'][:189]))==9529
s=b['survive']; moments=b['moments']; nmax=189

def upper_low(h):
    return sum(((2*n+1)*v for n,v in enumerate(s(h))),F(0))-600

def upper_high(h):
    return 189+sum(((2*(189-n)-1)*(1-v) for n,v in enumerate(s(F(1,2)-h))),F(0))

def ticks(x):
    j=(x*10**6).__floor__()
    return [j,j+1]

low=F(1,64)
L=upper_low(low)
U11=upper_high(F(1,11))
U332=upper_high(F(3,32))
mu,w=moments(F(0),F(3,20))
B=w-mu/2
assert mu>0
assert ticks(L)==[275220940,275220941]
assert ticks(U11)==[271896051,271896052]
assert ticks(U332)==[279763526,279763527]
assert ticks(B)==[559812917,559812918]

out={}
for key,high,U,min_margin in (
    ('strong_margin',F(1,11),U11,F(93,10)),
    ('larger_area',F(3,32),U332,F(7,25))):
    component_bounds={'low_low':2*L,'mixed':L+U,'high_high':2*U}
    peak=max(component_bounds.values())
    cert_margin=B-peak
    assert cert_margin>min_margin
    area=(low+high)**2
    gain=area/F(1,1024)
    out[key]={
        'low_side':str(low), 'high_side':str(high),
        'high_bound_ticks':ticks(U),
        'upper_W_by_corner_type_ticks':{k:ticks(v) for k,v in component_bounds.items()},
        'strict_certified_gap_ticks':ticks(cert_margin),
        'uniform_gap_claim':str(min_margin),
        'excluded_area':str(area),
        'area_multiple_vs_PREFIX705':str(gain)
    }
assert out['strong_margin']['area_multiple_vs_PREFIX705']=='5625/484'
assert out['larger_area']['area_multiple_vs_PREFIX705']=='49/4'
result={
    'schema':'PREFIX706_R6_ASYMMETRIC_CORNER_RECTANGLES_V1',
    'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'input_surviving_cells':9529,
    'low_bound_ticks':ticks(L),
    'witness_W_minus_mu_over_2_ticks':ticks(B),
    'q_domain':'every real q>=2',
    'stochastic_order_dependency':'PREFIX705 exact 17766 Bernstein derivative coefficients nonnegative',
    'cases':out,
    'verification':'ALL_CHECKS_PASS PREFIX706-R6',
    'scope':'Exact Fraction recomputation of frozen survivor and witness values, using original PREFIX700 recurrence; inherits PREFIX705 stochastic tail monotonicity, and Efron-Stein variance tensorization.',
    'admission':'AUTHOR_RECOMPUTED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED'
}
(root/'PREFIX706_R6_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS PREFIX706-R6')
print('L:',ticks(L),'U11:',ticks(U11),'U332:',ticks(U332),'B:',ticks(B))
for name,row in out.items():print(name,row['strict_certified_gap_ticks'],row['excluded_area'],row['area_multiple_vs_PREFIX705'])
