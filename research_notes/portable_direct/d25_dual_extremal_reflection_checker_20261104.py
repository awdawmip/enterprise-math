#!/usr/bin/env python3
"""Author-side exact source-preserving dual extremal p^4 reflection checks."""
import json
from math import isqrt, comb
def primes_up_to(n):
    sieve=bytearray([1])*(n+1); sieve[:2]=b'\0\0'
    for d in range(2,isqrt(n)+1):
        if sieve[d]: sieve[d*d:n+1:d]=b'\0'*((n-d*d)//d+1)
    return [i for i in range(5,n+1) if sieve[i]]
def check(p):
    m=p**4; p3=p**3; a=[1]*p; b=[1]*p
    for k in range(p-1):
        j=k+1
        a[j]=a[k]*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*j*j*j,-1,m)%m
        b[j]=b[k]*(4*k+1)*(4*k+2)*(4*k+3)*pow(576*j*j*j,-1,m)%m
    if p in {5,7,11,13,19,97,373}:
        for k in range(p):
            ca=comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,m)%m
            cb=comb(2*k,k)**2*comb(4*k,2*k)*pow(2304,-k,m)%m
            assert (ca,cb)==(a[k],b[k]),('factorial',p,k)
    ma=(p-1)//3; mb=(p-1)//4
    assert a[p-1]%p3==0 and a[p-1]//p3%p==p-1
    assert b[p-1]%p3==0 and b[p-1]//p3%p==p-1
    inv18=pow(18,-1,p); inv96=pow(96,-1,p)
    for k in range(1,ma+1):
        assert a[k]%p and a[p-k]%p3==0
        assert k**3*a[k]*(a[p-k]//p3)%p==(-inv18)%p,('a-pair',p,k)
    for k in range(1,mb+1):
        assert b[k]%p and b[p-k]%p3==0
        assert k**3*b[k]*(b[p-k]//p3)%p==(-inv96)%p,('b-pair',p,k)
    A3=sum((6*k+1)*a[k] for k in range(p-ma,p))%m
    B3=sum((8*k+1)*b[k] for k in range(p-mb,p))%m
    assert A3%p3==B3%p3==0
    HA=-inv18*sum((1-6*k)*pow(k**3*a[k],-1,p) for k in range(1,ma+1))%p
    HB=-inv96*sum((1-8*k)*pow(k**3*b[k],-1,p) for k in range(1,mb+1))%p
    assert A3//p3%p==HA and B3//p3%p==HB,('high-layer',p)
    W=sum((6*k+1)*a[k] for k in range(p))%m
    V=sum((8*k+1)*b[k] for k in range(p))%m
    eps=1 if p%3==1 else -1
    J=(W-2*V+eps*p)%m
    bulk=(W-A3-2*(V-B3)+eps*p)%m
    assert J==(bulk+p3*(HA-2*HB))%m,('signed-source',p)
    return dict(p=p,Ha=HA,Hb=HB,signed_high=(HA-2*HB)%p,
                bulk_digit=bulk//p3%p if bulk%p3==0 else None,
                J_zero=J==0,pairs_a=ma,pairs_b=mb)
def main():
    ps=primes_up_to(5000); samples={5,7,11,13,19,23,37,97,373}
    rows=[check(p) for p in ps]
    outcome=dict(domain='all primes 5<=p<=5000',primes=len(rows),
       pair_checks_a=sum(x['pairs_a'] for x in rows),
       pair_checks_b=sum(x['pairs_b'] for x in rows),
       fourth_digit_J_zero=sum(x['J_zero'] for x in rows),
       signed_high_nonzero=sum(bool(x['signed_high']) for x in rows),
       samples=[x for x in rows if x['p'] in samples],
       native_benchmark='NOT_EXECUTED',formal_admission='NOT_ADMITTED')
    print(json.dumps(outcome,indent=2))
if __name__=='__main__':main()
