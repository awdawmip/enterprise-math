#!/usr/bin/env python3
"""PREFIX-619: exact BRC stopping costs at rational signed-label parameters.
Requires PREFIX618_R6_exact_balanced_stop_certificate.py in the same directory.
"""
from fractions import Fraction as Q
from collections import defaultdict
from math import comb
from decimal import Decimal, localcontext
import contextlib, io, json
with contextlib.redirect_stdout(io.StringIO()):
    import PREFIX618_R6_exact_balanced_stop_certificate as c618

survival_counts=[{0:1}]
for m in range(1,190):
    cand=defaultdict(int)
    for k,v in survival_counts[-1].items():
        cand[k]+=v; cand[k+1]+=v
    survival_counts.append({k:v for k,v in cand.items() if c618.wide(m,k)})
assert len(survival_counts)==len(c618.A)
assert all(sum(row.values())==c618.A[i] for i,row in enumerate(survival_counts))

def survival(p):
    return [sum((v*p**k*(1-p)**(m-k) for k,v in row.items()),Q(0))
            for m,row in enumerate(survival_counts)]

def exact_cost(p1,p2):
    a,b=survival(p1),survival(p2)
    e1=sum(a,Q(0)); e2=sum(b,Q(0))
    overlap=sum((s*t*Q(comb(m+n,m),2**(m+n+1))
                for m,s in enumerate(a) if s for n,t in enumerate(b) if t),Q(0))
    return e1,e2,12*(e1+e2-overlap)

assert exact_cost(Q(1,2),Q(1,2))[2]==12*c618.mu
rows=[]
with localcontext() as ctx:
    ctx.prec=35
    for p1,p2 in ((Q(1,2),Q(1,2)),(Q(1,4),Q(1,2)),(Q(1,4),Q(1,4)),(Q(1,8),Q(1,2)),(Q(1,8),Q(1,8))):
        e1,e2,v=exact_cost(p1,p2)
        rows.append({'p1':str(p1),'p2':str(p2),
          'E_J1':str(e1),'E_J2':str(e2),'E_T12_exact':str(v),
          'E_T12_decimal':str(Decimal(v.numerator)/Decimal(v.denominator)),
          'E_T24_exact':str(2*v)})
result={'schema':'PREFIX619_R6_RATIONAL_ASYMMETRIC_BRC_STOPPING_V1',
'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
'parameters':{'d':2,'beta':'1/40','target_diameter':'1/4','q0':12,'q1_q2':24},
'pathwise_informative_cap':189,'cases':rows,
'identity':'E_T24(p1,p2)=2*E_T12(p1,p2) for all 0<=p1,p2<=1 in this experiment',
'verification':'ALL_CHECKS_PASS'}
print(json.dumps(result,indent=2))
