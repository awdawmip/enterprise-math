#!/usr/bin/env python3
"""PREFIX-630-R6: exact signed-observer BRC off-strip gradient witness and patch.
Reconstruct SOURCE-published PREFIX-621 first-passage rule, and use PREFIX-622
moment formulas and PREFIX-627 Hessian bound. No native 96-port graph rerun.
Only Python standard library, integers and Fraction exact arithmetic.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json

SCIENCE_PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'
DEN=1 << 18
N=189
assertions=0

def check(x):
    global assertions
    assert x
    assertions+=1

@lru_cache(maxsize=None)
def inside(m,k,a):
    return 40*(m+1)*comb(m,k)*a**k*(DEN-a)**(m-k)>DEN**m

@lru_cache(maxsize=None)
def wide(m,k):
    if k>m//2:
        return wide(m,m-k)
    mid=k*DEN//m
    check(inside(m,k,mid))
    if k==0:
        left_lo=left_hi=0
    else:
        lo,hi=0,mid
        check(not inside(m,k,lo))
        while hi-lo>1:
            point=(lo+hi)//2
            if inside(m,k,point):hi=point
            else:lo=point
        left_lo,left_hi=lo,hi
    lo,hi=mid,DEN
    check(not inside(m,k,hi))
    while hi-lo>1:
        point=(lo+hi)//2
        if inside(m,k,point):lo=point
        else:hi=point
    right_lo,right_hi=lo,hi
    if 4*(right_lo-left_hi)>DEN:return True
    if 4*(right_hi-left_lo)<DEN:return False
    raise AssertionError(('ambiguous dyadic diameter',m,k))

rows=[{0:1}]
state={0:1}
first=None
for m in range(1,N+1):
    nxt=defaultdict(int)
    for k,v in state.items():
        nxt[k]+=v
        nxt[k+1]+=v
    state={k:v for k,v in nxt.items() if wide(m,k)}
    if first is None and sum(nxt.values())>sum(state.values()): first=m
    rows.append(state.copy())
check(first==25)
check(not rows[N])
check(sum(rows[24].values())==2**24)
check(sum(rows[25].values())==2**25-2)

p=Q(1,8)
a=Q(37,256)
s1=[];ds1=[];s2=[]
for n,row in enumerate(rows[:N]):
    x=sum((v*7**(n-k) for k,v in row.items()),0)
    dx=sum((v*7**(n-k)*(8*k-n) for k,v in row.items()),0)
    y=sum((v*37**k*219**(n-k) for k,v in row.items()),0)
    s1.append(Q(x,8**n))
    ds1.append(Q(8*dx,7*8**n))
    s2.append(Q(y,256**n))
check(s1[25]==1-p**25-(1-p)**25)
check(ds1[25]==25*((1-p)**24-p**24))
check(all(0<=x<=1 for x in s1+s2))

alpha=[];beta=[]
for n in range(N):
    alpha.append(Q(1)-sum((Q(comb(n+m,n),2**(n+m+1))*s2[m]
                         for m in range(N) if s2[m]),Q(0)))
    beta.append(Q(n+1)-sum((Q((n+m+1)*comb(n+m,n),2**(n+m+2))*s2[m]
                         for m in range(N) if s2[m]),Q(0)))
check(all(0<=x<=1 for x in alpha))
check(all(0<=x<=n+1 for n,x in enumerate(beta)))
mu=sum(s2,Q(0))+sum((v*x for v,x in zip(alpha,s1)),Q(0))
U=sum((v*x for v,x in zip(alpha,ds1)),Q(0))
J=sum((v*x for v,x in zip(beta,ds1)),Q(0))
Wp=2*(J-mu*U)
check(0<mu<2*N)
check(U>0)
check(Wp < Q(-1500))

A=sum(range(N))
B=sum(2*n*(n-1) for n in range(N))
D=sum(2*n*(n-1)*(n+1) for n in range(N))
L11=2*D+2*A*A+4*N*B+Q(B,2)
check((A,B,D,L11)==(17766,4429656,631225980,5244748236))

S2=sum(n*(n+1) for n in range(N))
Cmu=(N-1)*A
CH=(N-1)*S2
CW=2*CH+2*(A*A+2*N*Cmu)
L12=CW+Q(Cmu,2)
check((S2,Cmu,CH,CW,L12)==(2250360,3340008,423067680,4002442920,4004112924))

h=Q(1,2**24)
margin=Q(1500)-(L11+L12)*h
check(margin>948)
check(p-h>Q(1,14))
check(a+h<Q(39,256))

result={
    'schema':'PREFIX630_R6_DISCONNECTED_VARIANCE_PATCH_V1',
    'science_pin':SCIENCE_PIN,
    'base_point':{'p1':str(p),'p2':str(a)},
    'rectangle':{'p1_min':str(p-h),'p1_max':str(p+h),
                 'p2_min':str(a),'p2_max':str(a+h)},
    'model':'PREFIX-621 signed two-direction first passage, beta=1/40, confidence diameter <=1/4, q>=2',
    'witness':{'mean_mu_exact':str(mu),'mean_gradient_U_exact':str(U),
               'poisson_variance_gradient_Wp_exact':str(Wp),
               'verified_Wp_strict_upper_bound':'-1500',
               'U_strict_positive':True},
    'uniform_bounds':{'L11':str(L11),'L12':str(L12),
                      'max_total_gradient_drift_per_q_squared':str((L11+L12)*h),
                      'guaranteed_positive_margin':str(margin)},
    'conclusion':'For every q>=2 and (p1,p2) in stated rectangle, partial_1 Var(T_q)< -948*q^2; hence points with p1>p1_min are not global variance maximizers.',
    'checks':{'assertions_executed':assertions,'first_informative_stop':first,
              'forced_informative_stop':N,'result':'ALL_CHECKS_PASS'},
    'provenance':'Reconstructed SOURCE-published PREFIX621 dyadic first-passage recurrence; PREFIX622 moment law; PREFIX627 second-gradient bound; no frozen 96-port native-graph reexecution.',
    'review':'AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED',
    'next_question':'Use subdivided 2D signed Bernstein envelopes to bridge the gap 1/14<p1<1/8 and extend rectangle across full p2 bracket.'
}
out=Path(__file__).with_name('PREFIX630_R6_RESULTS.json')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS',assertions)
print('W_prime_display',float(Wp),'U_display',float(U))
print('new_gradient_margin',str(margin))
