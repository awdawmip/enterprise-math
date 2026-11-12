#!/usr/bin/env python3
"""Exact rational finite-sample checks for R749SE and high-precision Chernoff readout.

Assumes R749SA 1:1:14 fiber law; no native Cell/Link/Port event permission.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from math import comb
import json

def q(p):
    return (1 + 15*p)/16

def a(p):
    return (1 + 7*p)/8

def bayes_error(c0, c1, m):
    assert 0 <= c0 < c1 <= 1 and m >= 1
    total_abs = sum(
        abs(Fraction(comb(m,k)) *
            (c1**k * (1-c1)**(m-k) - c0**k * (1-c0)**(m-k)))
        for k in range(m+1)
    )
    return Fraction(1,2)-total_abs/4

def guaranteed_gap(q0,q1,m):
    return min(q1**m-q0**m,
               ((1-q0)**m-(1-q1)**m)/15**m)/2

def fisher_s(p):
    return Fraction(15,1) / ((1+15*p)*(1-p))

def fisher_u(p):
    return Fraction(7,1) / ((1+7*p)*(1-p))

def decimal_cher(q0,q1,precision=65):
    assert 0 < q0 < q1 < 1
    with localcontext() as ctx:
        ctx.prec=precision
        x=Decimal(q0.numerator)/Decimal(q0.denominator)
        y=Decimal(q1.numerator)/Decimal(q1.denominator)
        t=((1-x)/(1-y)).ln()/(y*(1-x)/(x*(1-y))).ln()
        d=t*(t/x).ln()+(1-t)*((1-t)/(1-x)).ln()
        d1=t*(t/y).ln()+(1-t)*((1-t)/(1-y)).ln()
        assert abs(d-d1)<Decimal('1e-58')
        assert x<t<y
        return t, d

def main():
    p0,p1=Fraction(0),Fraction(1,2)
    qs0,qs1=q(p0),q(p1)
    au0,au1=a(p0),a(p1)
    rows=[]
    for m in [1,2,4,8,16,32,64]:
        es=bayes_error(qs0,qs1,m)
        eu=bayes_error(au0,au1,m)
        lb=guaranteed_gap(qs0,qs1,m)
        assert es < eu and eu-es >= lb > 0
        rows.append({'m':m,'signed_error_exact':str(es),
                     'unsigned_error_exact':str(eu),
                     'observer_penalty_exact':str(eu-es),
                     'lower_bound_exact':str(lb)})
    assert rows[0]['observer_penalty_exact']=='1/64'
    assert bayes_error(qs0,qs1,2)==Fraction(349,2048)
    assert bayes_error(au0,au1,2)==Fraction(109,512)
    assert bayes_error(qs0,qs1,2)-bayes_error(au0,au1,2)==-Fraction(87,2048)
    for p in [Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4)]:
        qs,au=q(p),a(p)
        assert fisher_s(p)==(Fraction(15,16)**2)/(qs*(1-qs))
        assert fisher_u(p)==(Fraction(7,8)**2)/(au*(1-au))
        assert fisher_s(p)-fisher_u(p)==Fraction(8,1)/((1+15*p)*(1+7*p)*(1-p))
        assert fisher_s(p)/fisher_u(p)==Fraction(15,7)*(1+7*p)/(1+15*p)
    for p0,p1 in [(Fraction(0),Fraction(1,4)),(Fraction(0),Fraction(1,2)),
                  (Fraction(1,4),Fraction(3,4)),(Fraction(1,2),Fraction(1))]:
        for m in range(1,13):
            assert bayes_error(q(p0),q(p1),m) < bayes_error(a(p0),a(p1),m)
        if p1==1:
            for m in range(1,13):
                assert bayes_error(q(p0),q(p1),m)==q(p0)**m/2
                assert bayes_error(a(p0),a(p1),m)==a(p0)**m/2
    ts,cs=decimal_cher(q(Fraction(0)),q(Fraction(1,2)))
    tu,cu=decimal_cher(a(Fraction(0)),a(Fraction(1,2)))
    assert cs>cu>0
    result={'status':'PASS','model':'R749SA 1:1:14 exact transition classes',
            'finite_sample_method':'fractions.Fraction exact integer rational summation',
            'sample_rows':rows,
            'strict_gap_cases_tested':4*12,
            'fisher_checks':4,
            'chernoff_readout_method':'decimal.Decimal natural logarithm, precision 65; noncertified numerical readout',
            'case':'p0=0,p1=1/2',
            'signed_threshold':format(ts,'.18f'),
            'unsigned_threshold':format(tu,'.18f'),
            'signed_chernoff_exponent':format(cs,'.18f'),
            'unsigned_chernoff_exponent':format(cu,'.18f'),
            'asymptotic_sample_inflation':format(cs/cu,'.18f'),
            'native_event_permission':False}
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
