#!/usr/bin/env python3
"""D25 exact integer proof-check; arithmetic power gauge, NOT native Frobenius."""
import json
from math import isqrt

def primes(bound):
    mark=bytearray(b'\x01')*(bound+1)
    mark[:2]=b'\x00\x00'
    for k in range(2,isqrt(bound)+1):
        if mark[k]:
            mark[k*k::k]=b'\x00'*((bound-k*k)//k+1)
    return [i for i in range(2,bound+1) if mark[i]]

def check(p):
    assert p>3 and p%24 in (13,19)
    m=p**3
    a=pow(18,(p*p-1)//4,m)
    c=pow(-18,(p-1)//2,p)
    assert c in (1,p-1)
    eps=1 if c==1 else -1
    assert a%p==eps%p
    q=(pow(18,p-1,m)-1)//p
    i4=pow(4,-1,m); i32=pow(32,-1,m)
    direct=eps*(1+p*q*i4+p*p*(q*i4-3*q*q*i32))%m
    inverse=eps*(1-p*q*i4+p*p*(-q*i4+5*q*q*i32))%m
    assert a==direct
    assert pow(a,-1,m)==inverse
    assert a*inverse%m==1
    assert a**4%m==pow(18,p*p-1,m)
    assert ((eps*a-1)%(p*p))//p==q*pow(4,-1,p)%p
    return dict(p=p,epsilon=eps,q18_mod_p=q%p,q18_mod_p2=q,
                power_gauge_mod_p2=a%(p*p),power_gauge_mod_p3=a,
                inverse_power_gauge_mod_p3=inverse,
                naive_sign_p2=(a%(p*p))==(eps%(p*p)))

if __name__=="__main__":
    rows=[check(p) for p in primes(2000) if p%24 in (13,19)]
    print(json.dumps(dict(schema="D25_CM_TWIST_ARITHMETIC_POWER_GAUGE_P3_CHECK_V1",
                          count=len(rows),passed=len(rows),
                          sign_only_failures=sum(not r["naive_sign_p2"] for r in rows),
                          examples=[r for r in rows if r["p"] in (13,19,37,43,109,181,373,1171)],
                          status="PASS_EXACT_INTEGER_NOT_NATIVE"),indent=2))
