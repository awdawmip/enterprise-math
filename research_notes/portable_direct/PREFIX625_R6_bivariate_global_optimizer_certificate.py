#!/usr/bin/env python3
"""PREFIX625: exact corner-exclusion witnesses for the bivariate global optimizer theorem.
Frozen science pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Python standard library; uses the established PREFIX621 exact first-passage recurrence.
"""
import contextlib, io, json
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from math import comb
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    import PREFIX621_R6_stochastic_tail_certificate as cert
rows=cert.rows
assert cert.first==25 and cert.surv[189]==0
assert rows[25]=={k:comb(25,k) for k in range(1,25)}
shape_checks=0
for n in range(1,190):
    row=rows[n]
    for k in range((n+1)//2):
        assert row.get(k,0)*comb(n,k+1) <= row.get(k+1,0)*comb(n,k)
        shape_checks+=1

def survive(p):
    a,b=p.numerator,p.denominator
    return [Q(sum(v*a**k*(b-a)**(n-k) for k,v in row.items()),b**n)
            for n,row in enumerate(rows[:189])]

def moment_pair(p1,p2):
    s,t=survive(p1),survive(p2)
    mu=sum(s,Q(0))+sum(t,Q(0))
    halfE2=sum(((n+1)*(s[n]+t[n]) for n in range(189)),Q(0))
    for n,sn in enumerate(s):
        if not sn:continue
        for m,tm in enumerate(t):
            if not tm:continue
            z=sn*tm*Q(comb(n+m,n),2**(n+m+1))
            mu-=z
            halfE2-=Q(n+m+1,2)*z
    W=2*halfE2-mu*mu
    assert W>0 and mu>0
    return mu,W

points={'witness_edge':(Q(0),Q(1,8)),
        'corner_zero_zero':(Q(0),Q(0)),
        'corner_zero_half':(Q(0),Q(1,2)),
        'corner_half_half':(Q(1,2),Q(1,2))}
computed={k:moment_pair(*p) for k,p in points.items()}
def V(k,q):
    mu,W=computed[k]
    return q*q*W-q*mu
for k in list(points)[1:]: assert V('witness_edge',12)>V(k,12),k
for k in points: assert V(k,24)==4*V(k,12)+24*computed[k][0]
with localcontext() as ctx:
    ctx.prec=28
    dec=lambda x:str(Decimal(x.numerator)/Decimal(x.denominator))
    cases=[{'point':k,'p1':str(p[0]),'p2':str(p[1]),
            'poissonized_mean':dec(computed[k][0]),
            'poissonized_variance':dec(computed[k][1]),
            'native_Var_q12':dec(V(k,12)),
            'native_Var_q24':dec(V(k,24))}
           for k,p in points.items()]
result={'schema':'PREFIX625_R6_BIVARIATE_GLOBAL_VARIANCE_OPTIMIZER_COST_ORDER_V1',
 'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'model':'d=2; q=12,24; beta=1/40; width=1/4; closure [0,1/2]^2',
 'theorem':'All global optimizer pairs for q2>q1>=2 have mu(y)>=mu(x) and W(y)>=W(x); both strict for q1=12,q2=24.',
 'proof_basis':'Poissonization plus central unimodality and s25 strictness; exact corner-exclusion witness.',
 'checks':{'reused_prefix621_integer_threshold_tests':cert.checks,
           'central_coefficient_checks':shape_checks,
           'strict_witness_inequalities':3,'variance_transfer':4},
 'values':cases,'verification':'ALL_CHECKS_PASS',
 'status':'AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED'}
Path(__file__).with_name('PREFIX625_R6_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('ALL_CHECKS_PASS',shape_checks,cert.checks)
for c in cases:print(c['point'],c['native_Var_q12'])
