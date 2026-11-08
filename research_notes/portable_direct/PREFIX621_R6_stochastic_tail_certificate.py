#!/usr/bin/env python3
"""PREFIX-621. Exact finite BRC signed-label first-passage and stochastic order certificate.
Frozen science pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Python standard library; no network; no native graph re-execution.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb
from decimal import Decimal, localcontext
import json, pathlib

D=1<<18
checks=0

def inside(m,k,a):
    global checks
    checks+=1
    return 40*(m+1)*comb(m,k)*a**k*(D-a)**(m-k)>D**m

def wide(m,k):
    if k>m//2:return wide(m,m-k)
    mid=k*D//m
    assert inside(m,k,mid)
    if k==0:left_lo=left_hi=0
    else:
        lo,hi=0,mid
        assert not inside(m,k,lo)
        while hi-lo>1:
            x=(lo+hi)//2
            if inside(m,k,x):hi=x
            else:lo=x
        left_lo,left_hi=lo,hi
    lo,hi=mid,D
    assert not inside(m,k,hi)
    while hi-lo>1:
        x=(lo+hi)//2
        if inside(m,k,x):lo=x
        else:hi=x
    right_lo,right_hi=lo,hi
    if 4*(right_lo-left_hi)>D:return True
    if 4*(right_hi-left_lo)<D:return False
    raise AssertionError(('ambiguous dyadic width',m,k))

A={0:1}; surv=[1]; rows=[{0:1}]; first=0
for m in range(1,190):
    nxt=defaultdict(int)
    for k,v in A.items():nxt[k]+=v;nxt[k+1]+=v
    A={k:v for k,v in nxt.items() if wide(m,k)}

    if not first and sum(nxt.values())>sum(A.values()):first=m
    surv.append(sum(A.values()))
    rows.append(A.copy())
assert first==25 and surv[189]==0 and all(v==0 for v in A.values())
assert wide(188,94) and all(not wide(189,k) for k in range(190))
assert surv[24]==2**24
assert surv[25]==2**25-2
# At first stop m=25, exactly two paths: 25 plus or 25 minus.
assert surv[25] == 2**25-2
unimodal_checks=symmetry_checks=0
for m in range(1,190):
    row=rows[m]
    for k in range(m+1):
        assert row.get(k,0)==row.get(m-k,0)
        symmetry_checks+=1
    for k in range((m+1)//2):
        assert row.get(k,0)*comb(m,k+1)<=row.get(k+1,0)*comb(m,k)
        unimodal_checks+=1
assert (symmetry_checks,unimodal_checks)==(18144,9025)
assert not wide(25,25) and wide(26,25) and rows[26].get(25,0)>0
# Pathwise survivor coefficient central unimodality of PREFIX-620 is reused rather than re-proved here.
# For independent validation of the 50-trial event, directly compare two exact formulas.

def cdf50(q,p1,p2):
    return Fraction(comb(50,25),q**50)*(p1**25+(1-p1)**25)*(p2**25+(1-p2)**25)

for q in (12,24):
    fair=cdf50(q,Fraction(1,2),Fraction(1,2))
    quarter=cdf50(q,Fraction(1,4),Fraction(1,2))
    edge=cdf50(q,Fraction(0),Fraction(1))
    assert fair==Fraction(comb(50,25), (2**48)*q**50)
    assert fair<quarter<edge
    assert cdf50(q,Fraction(0),Fraction(1,2))>fair
    assert fair>0

# Integer-valued CDF using independent fair sign-prefix survival counts.
def fair_cdf(n,q):
    # probability both directions have stopped after n native actions.
    # For n<=100 this positive-sum formula is fast and independently checks boundary.
    assert 0<=n<=110
    total=0
    for a in range(25,n+1):
        won_a=(1<<a)-(surv[a] if a<len(surv) else 0)
        for b in range(25,n-a+1):
            won_b=(1<<b)-(surv[b] if b<len(surv) else 0)
            total+=comb(n,a)*comb(n-a,b)*won_a*won_b*(2*(q-2))**(n-a-b)
    return Fraction(total,(2*q)**n)

assert fair_cdf(49,12)==0
assert fair_cdf(49,24)==0
for q in (12,24):
    assert fair_cdf(50,q)==cdf50(q,Fraction(1,2),Fraction(1,2))
    assert fair_cdf(51,q)>=fair_cdf(50,q)
    assert fair_cdf(60,q)>fair_cdf(51,q)
# Direct all-parameter probability order follows PREFIX620's proved Bernstein survivor coefficients.
result={
 'schema':'PREFIX621_R6_SHARP_STOCHASTIC_TAIL_V1',
 'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'dependency':'PREFIX620_R6_global_worst_parameter_certificate.py (Bernstein-unimodality integer certificate)',
 'parameters':'d=2, q in {12,24}, beta=1/40, delta=1/4, (p1,p2) in [0,1]^2',
 'first_possible_stop_informative':first,'forced_stop_informative':189,
 'fair_survivor_count_m25':str(surv[25]),
 'q12_cdf_at_50_balanced':str(cdf50(12,Fraction(1,2),Fraction(1,2))),
 'q12_cdf_at_50_quarter_fair':str(cdf50(12,Fraction(1,4),Fraction(1,2))),
 'q12_cdf_at_60_balanced':str(fair_cdf(60,12)),
 'q24_cdf_at_50_balanced':str(cdf50(24,Fraction(1,2),Fraction(1,2))),
 'q24_cdf_at_60_balanced':str(fair_cdf(60,24)),
 'claim':'P(T_q(p1,p2)>n)<=P(T_q(1/2,1/2)>n) for every integer n>=0, strict for n>=50 if parameters differ',
 'integer_root_checks':checks,
 'symmetry_checks':symmetry_checks,'unimodality_checks':unimodal_checks,
 'verification':'ALL_CHECKS_PASS',
 'scope':'Exact dyadic first-passage carrier + finite CDF checks; infinite n/all-parameter inequality follows analytic conditional-order argument and prior PREFIX620 finite shape lemma.',
}
out=pathlib.Path(__file__).with_name('PREFIX621_R6_RESULTS.json')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('ALL_CHECKS_PASS',checks)
print('CDF50 q12 fair vs quarter-fair',float(Fraction(result['q12_cdf_at_50_balanced'])),float(Fraction(result['q12_cdf_at_50_quarter_fair'])))
print('written',out)

# Uniform all-parameter quantile certificate: by the theorem the balanced pair is worst.
# For any fixed n, this is exact integer enumeration; no approximate tail math enters the checks.
def fair_tail_integer(n,q):
    assert n>=0 and q in (12,24)
    cap=min(188,n)
    A=2*(q-1); B=2*(q-2)
    cp=[comb(n,a) for a in range(cap+1)]
    marg=sum(cp[a]*surv[a]*A**(n-a) for a in range(cap+1))
    bp=[B**(n-j) for j in range(2*cap+1) if n-j>=0]
    # n is much greater than 2*cap for quantiles; this avoids enormous repeated powers.
    joint=0
    for a in range(cap+1):
        w=cp[a]*surv[a]
        for b in range(min(cap,n-a)+1):
            joint+=w*comb(n-a,b)*surv[b]*bp[a+b]
    den=(2*q)**n
    tail=2*marg-joint
    assert 0<=tail<=den
    return tail,den

quantiles=[]
for q,target,n in ((12,95,2578),(12,99,2687),(24,95,5171),(24,99,5393)):
    before,d0=fair_tail_integer(n-1,q)
    after,d1=fair_tail_integer(n,q)
    # P(T<=n)>=target/100 is equivalent to P(T>n)<=1-target/100.
    assert before*100>(100-target)*d0
    assert after*100<=(100-target)*d1
    assert before*d1>after*d0
    quantiles.append({'q':q,'confidence_percent':target,'minimum_n':n,
                      'cdf_at_n_minus_1':str(round(1-float(Fraction(before,d0)),12)),
                      'cdf_at_n':str(round(1-float(Fraction(after,d1)),12)),
                      'exact_check':'PASS'})
result['parameter_uniform_minimum_sample_quantiles']=quantiles
result['finite_tail_formula']='tail=(2*marginal_survival - joint_survival)/(2*q)^n; marginal=sum C(n,m)*A_m*(2*(q-1))^(n-m); joint=sum multinomial(n;a,b,n-a-b)*A_a*A_b*(2*(q-2))^(n-a-b); A_m=0 if m>=189.'
result['verification']='ALL_CHECKS_PASS'
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('ALL_QUANTILES_EXACT_PASS',[(r['q'],r['confidence_percent'],r['minimum_n']) for r in quantiles])
