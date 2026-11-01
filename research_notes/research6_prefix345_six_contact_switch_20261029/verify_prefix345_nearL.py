#!/usr/bin/env python3
"""Certified 4-point BRC retained-phase risk dual at h=416599/250000.
Uses exact previously certified PREFIX342 roots, no 6-orbit exhaustiveness.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import runpy, json
v=runpy.run_path(str(Path(__file__).with_name('verify_prefix342.py')))
IV,ci=v['IV'],v['ci']
zscalar,zmul,zconj=v['zscalar'],v['zmul'],v['zconj']
znorm2,zadd=v['znorm2'],v['zadd']
q3,L=v['q3'],v['L']
sources,ports=v['sources'],v['ports']
h=F(416599,250000) # h=1.666396, strictly below the six-orbit risk crossing
assert h>1
y=h-1;rad=q3-y*y
assert rad>0
scale=10**35
k=isqrt(rad.numerator*scale*scale//rad.denominator)
slo,shi=F(k,scale),F(k+1,scale)
assert slo*slo<rad<shi*shi
s=IV(slo,shi)
contact=[(0,'-'),(1,'+'),(3,'-'),(4,'+')]
weights=[F(n,10**6) for n in [140253,100513,363029,396205]]
assert sum(weights)==1 and all(x>0 for x in weights)
points=[]
for j,sgn in contact:
    z=ci(s if sgn=='+' else -s,y)
    phase=zscalar(F(1)/q3,zmul(z,zconj(ports[j])))
    p=[zmul(phase,zj) for zj in sources[j]]
    points.append(p)
mu=[ci(0,0) for _ in range(3)]
second=IV(0)
for weight,point in zip(weights,points):
    for k in range(3):mu[k]=zadd(mu[k],zscalar(weight,point[k]))
    second+=weight*sum((znorm2(z) for z in point),IV(0))
variance=second-sum((znorm2(z) for z in mu),IV(0))
# For any center b, max_k ||p_k-b||^2 >=sum w_k||p_k-b||^2
# = variance +||b-mu||^2 >= variance; no optimality assumption.
assert variance.lo > L+F(1,10**6), (float(variance.lo),float(L))
assert variance.hi < L+F(3,10**6)
result={
'schema':'PREFIX345_NEAR_L_FOUR_POINT_DUAL_V1',
'h':str(h),'labels':[[j,s] for j,s in contact],
'weights':[str(x) for x in weights],
'variance_open_interval':[str(variance.lo),str(variance.hi)],
'reported_strict_lower':'1062562/458329 + 1/1000000',
'conclusion':'For ALL 1<h<=416599/250000, MEB²(S(h))>L+10^-6. This uses four explicit certified BRC source states and nested source fibres, not six-orbit exhaustion.',
'scope':'static auxiliary retained-phase C3, no native X6/Detector/time',
'status':'PASS_AUTHOR_SIDE_EXACT_RATIONAL'}
Path(__file__).with_name('RESULTS_PREFIX345_NEAR_L.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('PASS_AUTHOR_SIDE_EXACT_RATIONAL near-L 4-point dual')
print('For all 1<h<=',h,' MEB²(S(h))>L+1/1000000')
print('Var-L in',float(variance.lo-L),float(variance.hi-L))
