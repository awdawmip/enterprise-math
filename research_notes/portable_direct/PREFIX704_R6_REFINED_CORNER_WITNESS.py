#!/usr/bin/env python3
"""PREFIX-704 exact 3/20 witness; reuse frozen PREFIX-700 integer recurrence."""
import json
import runpy
from pathlib import Path
from fractions import Fraction as F

folder=Path(__file__).resolve().parent
prior=runpy.run_path(str(folder/'PREFIX700_R6_STRICT_OPTIMIZER_ORDER.py'))
moments=prior['moments']
assert prior['N']==189 and sum(map(len,prior['rows'][:189]))==9529
e=(F(0),F(3,20))
me,we=moments(*e)
corners={'c00':(F(0),F(0)),'c01':(F(0),F(1,2)),'c11':(F(1,2),F(1,2))}
expected={
'c00':((62503978,62503979),(585040038,585040039)),
'c01':((-97817334,-97817333),(414603256,414603257)),
'c11':((-105596401,-105596400),(467493873,467493874))
}
checks=[]
for name,c in corners.items():
    mc,wc=moments(*c)
    dm,dw=me-mc,we-wc
    bins=tuple(((v*10**6).__floor__(),(v*10**6).__floor__()+1) for v in (dm,dw))
    assert bins==expected[name],(name,bins)
    assert dw>0 and 2*dw-dm>0
    checks.append({'corner':name,'delta_mu_1e6_ticks':list(bins[0]),
                   'delta_W_1e6_ticks':list(bins[1])})
a,b=F(414603256,10**6),F(97817333,10**6)
assert F(585040038,10**6)>a
assert F(585040038,10**6)-F(62503979,10**6)/2>a+b/2
assert F(467493873,10**6)>a
assert F(105596400,10**6)>b
c,d=F(17931816),F(17766)
assert b*c-a*d>0
rho0=a/c
rho24=(a+b/24)/(c+d/24)
assert F(1,43251)<rho0
assert F(1,42840)<rho24
assert F(1,38707)<(a+b/2)/(c+d/2)
margin_all=a-c/F(43251)
margin_12_24=a+b/24-(c+d/24)/F(42840)
assert margin_all==F(7892719,1802125000)>F(4,1000)
assert margin_12_24==F(2045477,24000000)>F(8,100)
ratio_all=F(46357,43251)**2
ratio_12_24=F(45809,42840)**2
assert ratio_all==F(2148971449,1870649001)>F(1148,1000)
assert ratio_12_24>F(114,100)
record={
'schema':'PREFIX704_R6_REFINED_RATIONAL_CORNER_WITNESS_V1',
'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
'witness':'(0,3/20)','surviving_cells':9529,'exact_tick_bins':checks,
'gap_lower':'(414603256+97817333*t)/1000000, 0<=t<=1/2',
'derivative_envelope':'17931816+17766*t',
'adaptive_radius':'(414603256+97817333*t)/(1000000*(17931816+17766*t))',
'radius_q_ge_2':'1/43251','radius_q_12_to_24':'1/42840','radius_q_2':'1/38707',
'normalized_margin_q_ge_2_gt':'4/1000','normalized_margin_q12_24_gt':'8/100',
'area_multiplier_all':str(ratio_all),'area_multiplier_q12_24':str(ratio_12_24),
'dependencies':['PREFIX700','PREFIX701','PREFIX702'],
'verification':'ALL_CHECKS_PASS PREFIX704-R6',
'status':'AUTHOR_RECOMPUTED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED'
}
(folder/'PREFIX704_R6_RESULTS.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS PREFIX704-R6')
