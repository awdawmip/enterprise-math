#!/usr/bin/env python3
"""Author-side D25/LIFT exact finite falsifier (NOT a native H0/B0 experiment).

Checks both original frozen observables Delta, R and independently formed W,
not a replacement of the frozen task or proof for all primes.
All operations use exact integer arithmetic in Z/(p^3) or F_p.
"""
import argparse
import json
import math
from collections import Counter


def primes(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    for q in range(2, math.isqrt(limit) + 1):
        if sieve[q]:
            sieve[q*q:limit+1:q] = b'\x00' * ((limit-q*q)//q+1)
    return [p for p in range(5,limit+1) if sieve[p] and p % 24 in (13,19)]


def check(p):
    assert p > 3 and p % 24 in (13,19)
    m=(p-1)//6
    mod=p**3
    q=p*p
    inv=[0]*p
    inv[1]=1
    for k in range(2,p):
        inv[k]=(-(mod//k)*inv[mod%k]) % mod
    c36=pow(36,-1,mod)
    # Frozen B_k = (1/6)_k (1/3)_k/(2^k(k!)^2)
    B=1
    g=1
    h=1
    # Frozen signed-cutoff R_p with C_a initial and exact recurrence
    R=0
    V=0
    J=0
    C=pow(10,-1,p)
    for k in range(p):
        if k>=1 and k<=m:
            if k>1:
                a=k-1
                C=C*36*a*a*pow((6*a+5)*(3*a+2),-1,p)%p
            V=(V+C)%p
            J=(J+k*C)%p
            R=(R+2*(B%p)*((6*k+1)*V-6*J))%p
        if k == p-1:
            break
        t=k+1
        B=(B*(6*k+1)*(3*k+1)*c36*inv[t]*inv[t])%mod
        g=(g+B)%mod
        h=(h+(12*t+1)*B)%mod
    assert g%p==0, ('CM0',p,g%p)
    G=(g//p)%q
    assert ((G*h-1)%p)==0, ('UR',p,(G*h-1)%p)
    Delta=((G*h-1)%q)//p

    # Independent original weighted 3F2 recurrence through full n=p-1,
    # A_n=binom(2n,n)^2 * binom(3n,n) / 216^n.
    A=1
    W=1
    for k in range(p-1):
        t=k+1
        A=(A*(2*k+1)*(3*k+1)*(3*k+2)*c36*inv[t]**3)%mod
        W=(W+(6*t+1)*A)%mod
    residual=(W-p)%mod
    assert residual%q==0, ('first_digit',p,residual%q)
    port=((W-p)%mod)//q
    assert (Delta-R)%p==port, ('source_port_mismatch',p,Delta,R,port)
    return dict(p=p, class24=p%24, Delta=Delta, R=R, W=W, residual=port)


def main(limit):
    ps=primes(limit)
    counts=Counter()
    samples=[]
    failures=[]
    for i,p in enumerate(ps):
        x=check(p)
        counts[x['class24']]+=1
        if p in (13,19,37,43,211,373,2011,7333,9973,19997) or (p>2000 and len([y for y in samples if y['p']>2000])<4):
            samples.append(x)
        if x['residual']!=0:
            failures.append(x)
    result=dict(limit=limit,total=len(ps),by_class=dict(counts),failures=failures[:20],num_failures=len(failures),samples=samples,
        method='frozen Delta and R plus separately built signed W; exact integer mod p^3; not H0/B0',
        status='FINITE_REGRESSION_ONLY_NOT_A_UNIVERSAL_PROOF_NOT_NATIVE')
    print(json.dumps(result,ensure_ascii=False,indent=2))
    assert not failures, 'Counterexample(s) require independent recomputation'


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--limit',type=int,default=20000)
    main(parser.parse_args().limit)
