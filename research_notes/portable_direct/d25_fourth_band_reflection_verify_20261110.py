#!/usr/bin/env python3
"""Exact, finite pointwise checks of D25 fourth-band reflection; not the theorem's proof."""
import json

def eligible_primes(N=10000):
    s=bytearray([1])*(N+1)
    s[:2]=b"\x00\x00"
    for t in range(2,int(N**.5)+1):
        if s[t]:
            s[t*t::t]=b"\x00"*(((N-t*t)//t)+1)
    return (p for p in range(13,N+1) if s[p] and p%24 in (13,19))

def verify_prime(p):
    m=(p-1)//6
    mod=p**4
    a=[1]
    for i in range(p-1):
        a.append(a[-1]*(2*i+1)*(3*i+1)*(3*i+2)
                 *pow(36*(i+1)**3,-1,mod)%mod)
    high=low=0
    for k in range(1,2*m+1):
        h=a[p-k]
        assert h%p**3==0
        assert a[k]%p!=0
        inv=pow(18*k**3*a[k]%p,-1,p)
        assert (h//p**3+inv)%p==0, (p,k)
        high+=(6*(p-k)+1)*(h//p**3)
        low+=(6*k-1)*inv
    high%=p; low%=p
    assert high==low
    fac=[1]*p
    for i in range(1,p):
        fac[i]=fac[i-1]*i%p
    invfac=[pow(fac[i],-1,p) for i in range(p)]
    independent=0
    for j in range(4*m+1,p):
        independent+=(-2*(6*j+1)*fac[2*j-p]*fac[3*j-2*p]
                      *pow(216,-j,p)*pow(invfac[j],5,p))
    assert independent%p==high, (p,independent%p,high)
    return {'p':p,'m':m,'pointwise_pairs':2*m,'F':high}

if __name__=="__main__":
    rows=[verify_prime(p) for p in eligible_primes()]
    assert len(rows)==312
    print(json.dumps({'prime_count':len(rows),
                      'pointwise_pairs':sum(x['pointwise_pairs'] for x in rows),
                      'selected':{str(x['p']):x['F'] for x in rows
                                  if x['p'] in {13,19,37,43,61,157,373}}},indent=2))
