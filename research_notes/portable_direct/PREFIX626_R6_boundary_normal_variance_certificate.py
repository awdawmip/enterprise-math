#!/usr/bin/env python3
"""PREFIX-626 exact inward-gradient certificate; frozen scientific pin
f42f2906d77f24085c123f3ccfe9667d41caa96d.
Run beside the published PREFIX621_R6_stochastic_tail_certificate.py.
"""
import contextlib
import io
import json
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from math import comb
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    import PREFIX621_R6_stochastic_tail_certificate as baseline
rows = baseline.rows
N = 189
assert len(rows) >= N and baseline.first == 25 and not rows[189]

# The p1=0 first derivative has exactly nine nonzero survivor layers.
for n in range(N):
    deriv = rows[n].get(1,0)-n*rows[n].get(0,0)
    assert deriv == (25 if 25<=n<=33 else 0), (n,deriv)

shape_checks = 0
for n in range(1,N):
    for k in range((n+1)//2):
        assert rows[n].get(k,0)*comb(n,k+1) <= rows[n].get(k+1,0)*comb(n,k)
        shape_checks += 1
assert shape_checks == 8930

def survivors(p):
    a,b=p.numerator,p.denominator
    return [Q(sum(v*a**k*(b-a)**(n-k) for k,v in rows[n].items()),b**n)
            for n in range(N)]

def weight(n,m):
    return Q(comb(n+m,n),2**(n+m+1))

a,b=Q(37,256),Q(39,256)
sa,sb=survivors(a),survivors(b)
mu_a=Q(25)
for n in range(N):
    alpha=Q(1)-sum((weight(m,n) for m in range(25)),Q(0))
    assert alpha>0
    mu_a+=alpha*sa[n]

dmu_b,dH_a=Q(0),Q(0)
for n in range(25,34):
    cross_b=sum((weight(n,m)*sb[m] for m in range(N)),Q(0))
    cross_Ha=sum((Q(n+m+1,2)*weight(n,m)*sa[m] for m in range(N)),Q(0))
    assert cross_b<1
    dmu_b+=25*(1-cross_b)
    dH_a+=25*(n+1-cross_Ha)

assert mu_a>87
assert dmu_b>4
assert dH_a<182
assert 2*(dH_a-mu_a*dmu_b)<-332

with localcontext() as ctx:
    ctx.prec=16
    dec=lambda x:str(Decimal(x.numerator)/Decimal(x.denominator))
    samples={'mu_at_a':dec(mu_a),'dmu_dp1_at_b':dec(dmu_b),
             'dH_dp1_at_a':dec(dH_a),
             'upper_bound_dW_dp1':dec(2*(dH_a-mu_a*dmu_b))}
result={'schema':'PREFIX626_R6_BOUNDARY_NORMAL_GRADIENT_V1',
        'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
        'model':'d=2; q=12,24; beta=1/40; width=1/4; [0,1/2]^2',
        'interval_p2':['37/256','39/256'],
        'proved':'partial_p1 Var(T_q)(0,p2) < -332*q^2 for every p2 in the interval and q>=2; PREFIX623 gives full-square strict boundary local maxima for q=12,24.',
        'exact_checks':['mu(0,a)>87','partial_1 mu(0,b)>4',
                        'partial_1 H(0,a)<182',
                        '2*(partial_1 H(0,a)-mu(0,a)*partial_1 mu(0,b))<-332'],
        'first_passage_derivative_support':'n=25..33; coefficient 25',
        'central_coefficient_checks':shape_checks,
        'reused_prefix621_integer_threshold_tests':baseline.checks,
        'display_approximations':samples,
        'verification':'ALL_CHECKS_PASS',
        'status':'AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED'}
Path(__file__).with_name('PREFIX626_R6_RESULTS.json').write_text(
    json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('ALL_CHECKS_PASS',shape_checks,baseline.checks)
print(samples)
