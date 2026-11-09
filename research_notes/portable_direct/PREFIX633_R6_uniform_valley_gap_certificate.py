#!/usr/bin/env python3
"""PREFIX633: exact rational signed-BRC valley separation certificate."""
from fractions import Fraction as F
from math import comb
import json
from pathlib import Path
L=5244748236
m=F(comb(50,25),2**51)*F(217,256)**25*25*(F(5,6)**24-F(1,6)**24)
gap=m/(24*L)
assert m>0 and gap>F(9,4*10**15)
out={'schema':'PREFIX633_R6_UNIFORM_VALLEY_GAP_V1',
     'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
     'dependency':'PREFIX627 global Hessian bound; PREFIX632 strict interior minimizer ordering; PREFIX625 Poisson survivor monotonicity',
     'q1':12,'q2':24,'p2_range':['37/256','39/256'],
     'p1_interval':['3/20','1/6'],
     'mu_prime_lower_bound_fraction':str(m),
     'gap_lower_bound_fraction':str(gap),
     'strict_simple_gap':'a-b > 9/(4*10^15)',
     'gap_lower_bound_display':format(float(gap),'.18g'),
     'verification':'ALL_CHECKS_PASS',
     'status':'AUTHOR_PROVED / EXACT_ARITHMETIC_CHECKED / UNREVIEWED / NOT_ADMITTED'}
Path(__file__).with_name('PREFIX633_R6_RESULTS.json').write_text(
    json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS',out['strict_simple_gap'])
