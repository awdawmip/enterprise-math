#!/usr/bin/env python3
"""PREFIX-622: exact BRC first-passage second moments and variance counterexample.
Frozen pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Input: PREFIX621_R6_stochastic_tail_certificate.py in same directory.
Only integer/Fraction arithmetic; independently checks the single-direction endpoint.
"""
import contextlib
import io
import json
from fractions import Fraction as Q
from math import comb
from decimal import Decimal,localcontext
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    import PREFIX621_R6_stochastic_tail_certificate as c621

assert c621.first == 25 and c621.surv[189] == 0
ROWS=c621.rows

def survival(p):
    assert 0<=p<=1
    a,b=p.numerator,p.denominator
    return [Q(sum(v*a**k*(b-a)**(m-k) for k,v in row.items()),b**m)
            for m,row in enumerate(ROWS)]

def moments(p1,p2,q=12):
    assert q in (12,24)
    s,t=survival(p1),survival(p2)
    # X = max of independent unit-rate informative-direction Poisson stopping times.
    I1=sum(s,Q(0))+sum(t,Q(0))
    I2=sum(((m+1)*(s[m]+t[m]) for m in range(189)),Q(0))
    J1=Q(0);J2=Q(0)
    for m,sm in enumerate(s):
        if not sm: continue
        for n,tn in enumerate(t):
            if not tn: continue
            c=sm*tn*Q(comb(m+n,m),2**(m+n+1))
            J1+=c
            J2+=Q(m+n+1,2)*c
    mu=I1-J1
    ex2=2*(I2-J2)
    # Poisson horizon tau has Var(tau)=Var(T)+E[T].
    mean=q*mu
    variance=q*q*(ex2-mu*mu)-mean
    assert mean>0 and variance>0
    return mean,variance

# An independent identity for a single direction: p=1 gives J=25 exactly.
endpoint_survival=survival(Q(1))
assert endpoint_survival==[Q(1)]*25+[Q(0)]*165
single_mu=sum(endpoint_survival,Q(0))
single_e2=2*sum(((m+1)*v for m,v in enumerate(endpoint_survival)),Q(0))
assert single_mu==25 and single_e2-single_mu**2==25
for q in (12,24):
    assert q*q*(single_e2-single_mu**2)-q*single_mu==25*q*(q-1)

cases=[(Q(1,2),Q(1,2)),(Q(1,4),Q(1,4)),(Q(1,8),Q(1,8)),
       (Q(1,2),Q(1,4)),(Q(1,2),Q(2,5))]
rows=[]
with localcontext() as ctx:
    ctx.prec=35
    for p1,p2 in cases:
        mean,variance=moments(p1,p2,12)
        mean24,var24=moments(p1,p2,24)
        assert mean24==2*mean
        assert var24==4*variance+mean24
        decimal=lambda x:str(Decimal(x.numerator)/Decimal(x.denominator))
        rows.append({'p1':str(p1),'p2':str(p2),
                     'E_T12_exact':str(mean),'Var_T12_exact':str(variance),
                     'E_T12_decimal':decimal(mean), 'Var_T12_decimal':decimal(variance),
                     'Var_T24_exact':str(var24),'Var_T24_decimal':decimal(var24)})

# The previous uniquely maximal MEAN at balance does not maximize VARIANCE.
fair=Q(rows[0]['Var_T12_exact']);quarter=Q(rows[1]['Var_T12_exact']);eighth=Q(rows[2]['Var_T12_exact'])
assert fair<quarter<eighth
assert Q(rows[0]['E_T12_exact'])>Q(rows[1]['E_T12_exact'])>Q(rows[2]['E_T12_exact'])
result={'schema':'PREFIX622_R6_EXACT_VARIANCE_COUNTEREXAMPLE_V1',
        'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
        'model':'d=2,q=12 or 24,beta=1/40,delta=1/4, first passage',
        'theorem':'Var_Tq(1/4,1/4)>Var_Tq(1/2,1/2), both q; fair uniquely maximizes E_Tq, not Var_Tq',
        'formula':'E_Tq=q*mu, Var_Tq=q^2*(2*H-mu^2)-q*mu; mu=S1+S2-J1, H=H1+H2-J2',
        'q_identity':'E_T24=2E_T12; Var_T24=4Var_T12+E_T24',
        'single_endpoint_validation':'p=1 first 25 informative signs deterministic; negative-binomial Var=25*q*(q-1)',
        'cases':rows,'verification':'ALL_CHECKS_PASS',
        'scope':'Exact BRC signed-label statistical model; inherits PREFIX620 first-passage finite carrier; original 96-port graph not rerun'}
out=Path(__file__).with_name('PREFIX622_R6_RESULTS.json')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('ALL_CHECKS_PASS PREFIX622 q12 Var balanced,quarter,eighth =',*[x['Var_T12_decimal'] for x in rows[:3]])
print('Output',out)
