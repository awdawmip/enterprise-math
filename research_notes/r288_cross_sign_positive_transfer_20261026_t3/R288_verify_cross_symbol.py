#!/usr/bin/env python3
"""R288 exact certificate: positive cross-sign Green-kernel transfer.
Independent raw ordered-source dynamic programming and integer series recurrence.
No floating-point arithmetic, no external dependencies.
"""
from __future__ import annotations
from collections import Counter
import json

MAX_N=170
MAX_M=30
COEFFICIENT_DEGREE=95

# h=y^4+(y+2y^2+y^3+y^4)h + y(1+y)^2 h^2.
h=[0]*(COEFFICIENT_DEGREE+1)
for n in range(COEFFICIENT_DEGREE+1):
    v=int(n==4)
    for shift,weight in ((1,1),(2,2),(3,1),(4,1)):
        if n>=shift:v+=weight*h[n-shift]
    for shift,weight in ((1,1),(2,2),(3,1)):
        if n>=shift:
            v+=weight*sum(h[j]*h[n-shift-j] for j in range(n-shift+1))
    h[n]=v
assert h[:4]==[0,0,0,0] and all(x>0 for x in h[4:])

# A=1-Q, Q=2y+y(1+y)h. R=1/A; C=1+y(1-y)R.
q=[0]*(COEFFICIENT_DEGREE+1)
for n in range(1,COEFFICIENT_DEGREE+1):
    q[n]=(2 if n==1 else 0)
    if n>=1:q[n]+=h[n-1]
    if n>=2:q[n]+=h[n-2]
r=[0]*(COEFFICIENT_DEGREE+1);r[0]=1
for n in range(1,len(r)):
    r[n]=sum(q[j]*r[n-j] for j in range(1,n+1))
c=[1]+[r[j-1]-(r[j-2] if j>=2 else 0) for j in range(1,len(r))]
assert c[:8]==[1,1,1,2,4,8,17,37]
assert all(cj>=1 for cj in c)
assert all(r[j]>=2*r[j-1] for j in range(1,len(r)))

# State (control q, epsilon, k, last_zero), start q0, effect (+1,0).
transitions={
    0:{0:(2,-1,-1),1:(2,1,-1)},
    1:{0:(0,-1,-1),1:(0,1,-1)},
    2:{0:(1,1,1),1:(2,1,-1)},
}
state=Counter({(0,1,0,0):1})
fibers=[]
for n in range(MAX_N+1):
    clean=Counter()
    for (q0,eps,k,last_zero),multiplicity in state.items():
        if q0==0:clean[(eps,k)]+=multiplicity
    fibers.append(clean)
    nxt=Counter()
    for (q0,eps,k,last_zero),multiplicity in state.items():
        for bit in (0,1):
            if bit==0 and last_zero:continue
            q1,eta,delta=transitions[q0][bit]
            nxt[(q1,eta*eps,eta*k+delta,int(bit==0))]+=multiplicity
    state=nxt

# Cross-sign universal positive-convolution identity at exact integer coefficients.
checks=0;strict_checks=0;min_coefficient_checks=0
for m in range(1,MAX_M+1):
    assert fibers[m+2][(1,-m)]==1, (m,'leading clean fiber')
    for n in range(MAX_N+1):
        left=fibers[n][(-1,-m-2)]
        right=sum(c[j]*fibers[n-2-2*j][(1,-m)] for j in range((n-2)//2+1)) if n>=2 else 0
        assert left==right,(m,n,left,right)
        checks+=1
        lead=fibers[n-2][(1,-m)] if n>=2 else 0
        assert left>=lead
        if n>=m+6 and (n-m)%2==0:
            assert left>lead,(m,n,'strict')
            strict_checks+=1
        if n>=m+4 and (n-m)%2==0:
            t=(n-m-4)//2
            assert left>=c[t]
            min_coefficient_checks+=1

# A separate raw word enumeration checks recurrence semantics at small lengths.
raw_cases=0
for n in range(0,15):
    counted=Counter()
    for bits in range(1<<n):
        word=tuple((bits >> (n-1-i))&1 for i in range(n))
        if any(word[i]==word[i+1]==0 for i in range(n-1)):continue
        q0=0;eps=1;k=0
        for bit in word:
            q0,eta,delta=transitions[q0][bit]
            eps=eta*eps;k=eta*k+delta
        if q0==0:counted[(eps,k)]+=1
        raw_cases+=1
    assert counted==fibers[n], n

out={
    'schema':'EM_R288_EXACT_EVIDENCE_V1',
    'status':'PASS',
    'model':'ordered positive weight-1 clean source words; six edges; full (epsilon,k) effect; terminal q=0',
    'arithmetic':'Python arbitrary-precision integers only',
    'source_DP_lengths':[0,MAX_N],
    'cross_symbol_m_range':[1,MAX_M],
    'kernel_c_degree':[0,COEFFICIENT_DEGREE],
    'cross_symbol_coefficients_checked':checks,
    'strict_comparison_cases_checked':strict_checks,
    'base_lower_bound_cases_checked':min_coefficient_checks,
    'raw_source_words_accepted':raw_cases,
    'C_first_12':[str(x) for x in c[:12]],
    'h_first_12':[str(x) for x in h[:12]],
    'scope':'Finite checks confirm coefficients; universal theorem follows algebraic identity + formal nonnegative kernel induction.',
    'unproved':'R287 four all-length base Δ positivity; global peak and six-channel equality; Driver admission.'
}
with open('/mnt/data/R288_EXACT_EVIDENCE.json','w',encoding='utf8') as f:json.dump(out,f,ensure_ascii=False,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
