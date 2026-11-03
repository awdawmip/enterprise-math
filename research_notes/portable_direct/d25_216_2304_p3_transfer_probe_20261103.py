#!/usr/bin/env python3
"""D25 author-side finite 216/2304 signed bridge probe, not a universal proof."""
import math,json
def primes(N=2000):
    a=[True]*(N+1); a[0]=a[1]=False
    for q in range(2,math.isqrt(N)+1):
        if a[q]:
            for m in range(q*q,N+1,q):a[m]=False
    return [p for p in range(5,N+1) if a[p]]
def recur(p):
    mod=p**4; b=t=w=s=1
    for k in range(1,p):
        b=b*(2*k-1)*(3*k-2)*(3*k-1)*pow(36*k**3,-1,mod)%mod
        t=t*(4*k-3)*(4*k-2)*(4*k-1)*pow(576*k**3,-1,mod)%mod
        w=(w+(6*k+1)*b)%mod
        s=(s+(8*k+1)*t)%mod
    return w,s,b,t
def independent(p):
    mod=p**4; w=s=0
    for k in range(p):
        b=math.comb(2*k,k)**2*math.comb(3*k,k)*pow(216,-k,mod)%mod
        t=math.factorial(4*k)//math.factorial(k)**4*pow(2304,-k,mod)%mod
        w=(w+(6*k+1)*b)%mod; s=(s+(8*k+1)*t)%mod
    return w,s
sample={5,7,11,13,19,37,43,109,181,373}
res=[]; nonzero=0; target=0
for p in primes():
    w,s,b,t=recur(p); mod=p**4; d=(w-s)%mod; chi=1 if p%3==1 else -1
    assert d%p**3==0 and w%p**3==(chi*p)%p**3 and s%p**3==(chi*p)%p**3
    assert b%p**3==0 and t%p**3==0
    assert b//p**3==p-1 and t//p**3==p-1
    assert ((6*p-5)*b-(8*p-7)*t+2*p**3)%mod==0
    nonzero+=int(d!=0); target+=int(p%24 in (13,19))
    if p in sample:
        assert independent(p)==(w,s)
        res.append({'p':p,'W216_mod_p4':w,'S2304_mod_p4':s,
                    'difference_mod_p4':d,'difference_over_p3_mod_p':d//p**3})
print(json.dumps({'status':'FINITE_EXACT_CHECKED_NOT_UNIVERSAL_PROOF',
 'total_primes':len(primes()),'target_primes':target,'p3_bridge_failures':0,
 'p4_bridge_nonzero_count':nonzero,'samples':res,'native_h0b0':'NOT_EXECUTED'},indent=2))
