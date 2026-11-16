#!/usr/bin/env python3
"""Exact audit of modular named-source observation fibers, repair and time monotonicity."""
from math import gcd, lcm
from collections import defaultdict
import itertools
import json
from pathlib import Path

def c(t, a, b):
    return a**(t//2) * b**((t-1)//2)

def primes(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0: n//=d
        d+=1
    if n>1: out.append(n)
    return out

def prime_free(m,C):
    for d in primes(C):
        while m%d==0: m//=d
    return m

def min_coprime(N,C):
    m=N
    while gcd(m,C)!=1: m+=1
    return m

def repair(y,m,scale,S,N,high):
    g=gcd(scale,m)
    M=m//g
    assert y%g==0
    low=0 if M==1 else (((y//g)*pow(scale//g,-1,M)-S)%M)
    u=high*M+low
    assert 0<=u<N
    return u

def bits(k):
    return (k-1).bit_length()

stats={'families':0,'time_modulus_cases':0,'assignments_checked':0,
       'fibers_checked':0,'repair_checked':0,'monotone_step_checks':0,
       'temporal_future_pairs_checked':0,'unbounded_modulus_cases':0}
examples=[]
for p in range(1,5):
    for W in range(2,5):
        N=W**p
        S=sum(W**i for i in range(p))
        for a,b in itertools.product(range(1,5),repeat=2):
            stats['families']+=1
            for m in range(1,17):
                prev=None
                for t in range(1,9):
                    scale=c(t,a,b)
                    g=gcd(m,scale)
                    M=m//g
                    observed=defaultdict(list)
                    for u in range(N):
                        y=scale*(S+u)%m
                        observed[y].append(u)
                        assert repair(y,m,scale,S,N,u//M)==u
                        stats['repair_checked']+=1
                        stats['assignments_checked']+=1
                    assert len(observed)==min(N,M)
                    for yy, vals in observed.items():
                        base=vals[0]%M
                        assert all(v%M==base for v in vals)
                        assert vals==list(range(base,N,M))
                        assert len(vals) in (N//M, (N+M-1)//M)
                        stats['fibers_checked']+=1
                    max_fiber=(N+M-1)//M
                    assert max(map(len,observed.values()))==max_fiber
                    assert max(u//M for u in range(N))+1==max_fiber
                    if prev is not None:
                        assert prev%M==0
                        stats['monotone_step_checks']+=1
                        for uu in range(N):
                            for vv in range(uu+1,N):
                                if c(t-1,a,b)*(uu-vv)%m==0:
                                    assert scale*(uu-vv)%m==0
                                stats['temporal_future_pairs_checked']+=1
                    prev=M
                    stats['time_modulus_cases']+=1

for L in (4,8,10,20,30,40,50):
    C=lcm(*range(1,L+1))
    N=4
    optimal=min_coprime(N,C)
    assert optimal>L
    assert all(prime_free(m,C)<N for m in range(1,optimal))
    examples.append({'L':L,'ab':str(C),'N':N,'uniform_least_modulus':optimal,
                     'raw_bits':bits(optimal),'payload_bits':bits(N)})
    stats['unbounded_modulus_cases']+=1

cases=[]
for p,W,a,b,m,T in [(2,2,2,1,4,5),(2,2,2,1,5,5),
                    (2,3,2,3,10,6),(2,3,2,3,11,6),(2,3,2,3,12,6)]:
    N=W**p
    rows=[]
    for t in range(1,T+1):
        M=m//gcd(m,c(t,a,b))
        rows.append({'t':t,'c_t':c(t,a,b),
                     'observable_classes':min(N,M),'M':M,
                     'largest_fiber':(N+M-1)//M,
                     'min_repair_bits':bits((N+M-1)//M)})
    cases.append({'p':p,'W':W,'a':a,'b':b,'modulus':m,'N':N,'by_time':rows})

result={
 'schema':'PREFIX843_MODULAR_BRC_FIBER_REPAIR_V1',
 'input_commit':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'theorem':'At time t, U in [0,N) has observer fibers by U mod M_t, M_t=m/gcd(m,c_t); largest fiber ceil(N/M_t); minimal worst-case supplementary bits ceil(log2 ceil(N/M_t)). The fibers coarsen with t and converge to M_inf=m_perp(ab).',
 'verification':'ALL_EXACT_ASSERTIONS_PASSED',
 'stats':stats,'worked_cases':cases,
 'arbitrarily_large_overhead_witnesses':examples,
 'scope':'Fixed raw observer Z=c_t(S+U) mod m and positive integers p,W>=2,a,b,m; one Q-only tagged-deletion channel. Supplementary digit h=floor(U/M_t) and known time t.'
}
out=Path(__file__).with_name('PREFIX843_R6_MODULAR_FIBER_REPAIR_RESULTS.json')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'verification':result['verification'],'stats':stats},ensure_ascii=False,indent=2))
