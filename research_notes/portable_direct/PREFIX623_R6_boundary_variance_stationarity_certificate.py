#!/usr/bin/env python3
"""PREFIX-623 exact rational derivative-sign certificate, frozen BRC pin f42f2906d77f24085c123f3ccfe9667d41caa96d."""
from collections import defaultdict
from fractions import Fraction as Q
from math import comb
from decimal import Decimal, localcontext
import json
from pathlib import Path
D=1<<18
N=189
checks=0

def inside(m,k,a):
    global checks
    checks+=1
    return 40*(m+1)*comb(m,k)*a**k*(D-a)**(m-k)>D**m

def wide(m,k):
    if k>m//2: return wide(m,m-k)
    mid=k*D//m
    assert inside(m,k,mid)
    if k==0:left_lo=left_hi=0
    else:
        lo,hi=0,mid
        assert not inside(m,k,lo)
        while hi-lo>1:
            z=(lo+hi)//2
            if inside(m,k,z):hi=z
            else:lo=z
        left_lo,left_hi=lo,hi
    lo,hi=mid,D
    assert not inside(m,k,hi)
    while hi-lo>1:
        z=(lo+hi)//2
        if inside(m,k,z):lo=z
        else:hi=z
    right_lo,right_hi=lo,hi
    if 4*(right_lo-left_hi)>D:return True
    if 4*(right_hi-left_lo)<D:return False
    raise AssertionError(('unresolved dyadic interval',m,k))

A={0:1}; rows=[A.copy()]
for m in range(1,N+1):
    B=defaultdict(int)
    for k,v in A.items(): B[k]+=v; B[k+1]+=v
    A={k:v for k,v in B.items() if wide(m,k)}
    rows.append(A)
assert rows[N]=={} and rows[24]=={k:comb(24,k) for k in range(25)}
assert rows[25].get(0,0)==rows[25].get(25,0)==0
assert all(rows[m].get(0,0)==(1 if m<25 else 0) for m in range(N+1))
alpha=[];beta=[]
for n in range(N):
    b=sum((Q(comb(m+n,m),2**(m+n+1)) for m in range(25)),Q(0))
    c=sum((Q((m+n+1)*comb(m+n,m),2**(m+n+2)) for m in range(25)),Q(0))
    alpha.append(1-b);beta.append(n+1-c)

def survivor_and_derivative(n,p):
    z=Q(0);dz=Q(0)
    for k,A in rows[n].items():
        z+=A*p**k*(1-p)**(n-k)
        if k:dz+=A*k*p**(k-1)*(1-p)**(n-k)
        if n-k:dz-=A*(n-k)*p**k*(1-p)**(n-k-1)
    return z,dz

def moment_and_slope(p,q):
    S=Q(25);H=Q(325);Sd=Q(0);Hd=Q(0)
    for n in range(N):
        s,ds=survivor_and_derivative(n,p)
        S+=alpha[n]*s
        H+=beta[n]*s
        Sd+=alpha[n]*ds
        Hd+=beta[n]*ds
    mean=q*S
    variance=q*q*(2*H-S*S)-q*S
    slope=q*q*(2*Hd-2*S*Sd)-q*Sd
    assert mean>0 and variance>0
    return mean,variance,slope

samples={}
with localcontext() as ctx:
    ctx.prec=24
    for q in (12,24):
        rec=[]
        for p in (Q(0),Q(1,8),Q(37,256),Q(39,256),Q(1,2)):
            mu,v,dv=moment_and_slope(p,q)
            rec.append({'p':str(p),'mean':str(Decimal(mu.numerator)/Decimal(mu.denominator)),
                        'variance':str(Decimal(v.numerator)/Decimal(v.denominator)),
                        'variance_slope_sign':1 if dv>0 else -1 if dv<0 else 0,
                        'slope_numerator_digits':len(str(abs(dv.numerator)))})
        samples[str(q)]=rec
        assert rec[2]['variance_slope_sign']==1 and rec[3]['variance_slope_sign']==-1
        assert moment_and_slope(Q(1,8),q)[1]>moment_and_slope(Q(0),q)[1]
        assert moment_and_slope(Q(1,8),q)[1]>moment_and_slope(Q(1,2),q)[1]
        print(f'EXACT_SIGNS_PASS q={q}, Vprime(37/256)>0, Vprime(39/256)<0')
for p in (Q(0),Q(1,8),Q(37,256),Q(39,256),Q(1,2)):
    m,v,d=moment_and_slope(p,12)
    m2,v2,d2=moment_and_slope(p,24)
    assert m2==2*m and v2==4*v+m2
out={'schema':'PREFIX623_R6_EDGE_VARIANCE_STATIONARITY_V1',
     'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
     'models':'2 signed directions; p1=0 in compact closure; q=12 or 24; beta=1/40; diameter delta=1/4',
     'theorem':'For q=12,24 there is at least one variance maximizer p2* strictly inside (37/256,39/256) on edge p1=0, and Vprime_q(37/256)>0>Vprime_q(39/256).',
     'p1_zero_first_passage_count':25,
     'finite_polynomial_degree_bound':376,
     'alpha_beta_formula':'alpha_n=1-sum_{m=0}^{24}binom(m+n,m)/2^(m+n+1); beta_n=(n+1)-sum_{m=0}^{24}(m+n+1)*binom(m+n,m)/2^(m+n+2)',
     'verification':'ALL_CHECKS_PASS',
     'scope':'Author exact rational derivative signs; independent review and native original-graph re-execution pending',
     'samples':samples,
     'integer_root_comparison_checks':checks}
Path(__file__).with_name('PREFIX623_R6_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('ALL_CHECKS_PASS; integer comparisons:',checks)
