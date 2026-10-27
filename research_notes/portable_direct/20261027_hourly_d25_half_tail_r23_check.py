#!/usr/bin/env python3
"""Author-side finite-ring exact check, D25/LIFT R23.

Checks reflected W high-jet and GZ companion half-S cancellation.
Portable author evidence, not Source-native CM, Result or Driver review.
"""
from math import comb, isqrt

def eligible_primes(bound=997):
    return [p for p in range(7,bound+1) if p%6==1 and all(p%d for d in range(2,isqrt(p)+1))]

def factorials_mod(p):
    f=[1]*p
    for i in range(1,p): f[i]=f[i-1]*i%p
    return f

def reflected_jets(p):
    m=(p-1)//6
    f=factorials_mod(p)
    def ifac(n):
        assert 0<=n<p
        return pow(f[n],-1,p)
    A={j:(6*j+5)*pow(216,j,p)*pow(f[j],5,p)*ifac(2*j+1)*ifac(3*j-6*m+1)%p
       for j in range(2*m,3*m)}
    B={j:2*(8*j+7)*pow(2304,j,p)*pow(f[j],4,p)*ifac(4*j-6*m+2)%p
       for j in range(3*m//2,3*m)}
    return A,B

def recurrence_terms(p):
    mod=p**3
    wbase=sbase=1
    W,S=[],[]
    iw=pow(36,-1,mod); iss=pow(288,-1,mod)
    for k in range(p):
        W.append((6*k+1)*wbase%mod)
        S.append((8*k+1)*sbase%mod)
        if k+1<p:
            d=pow(k+1,-3,mod)
            wbase=wbase*(2*k+1)*(3*k+1)*(3*k+2)*iw*d%mod
            sbase=sbase*(4*k+1)*(2*k+1)*(4*k+3)*iss*d%mod
    return W,S

def direct_binomial_late(p,k):
    mod=p**3
    w=(6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,mod)%mod
    s=(8*k+1)*comb(4*k,2*k)*comb(2*k,k)**2*pow(2304,-k,mod)%mod
    return w,s

def run():
    ps=eligible_primes()
    assert len(ps)==80
    all_obs=[]; units=0
    for p in ps:
        m=(p-1)//6
        H=(3*p-1)//4
        A,B=reflected_jets(p)
        W,S=recurrence_terms(p)
        mod=p**3
        for k in range(3*m+1,4*m+1):
            assert W[k]%p**2==0
            j=p-1-k
            assert W[k]//p**2==A[j],(p,k,'W-j')
            units+=1
        for k in range(3*m+1,H+1):
            assert S[k]%p**2==0
            j=p-1-k
            assert S[k]//p**2==B[j],(p,k,'S-j')
            units+=1
        assert all(x==0 for x in W[4*m+1:]),(p,'W cutoff')
        assert all(x==0 for x in S[H+1:]),(p,'S cutoff')
        for j in range(2*m,3*m-1):
            assert ((6*j+5)*(2*j+3)*(3*j+4)*(3*j+5)*A[j+1]
                -36*(6*j+11)*(j+1)**3*A[j])%p==0
        for j in range(3*m//2,3*m-1):
            assert ((8*j+7)*(4*j+5)*(4*j+6)*(4*j+7)*B[j+1]
                -576*(8*j+15)*(j+1)**3*B[j])%p==0
        U=sum(A.values())%p
        V=sum(B.values())%p
        s_mid=sum(B[j] for j in range(2*m,3*m))%p
        t=sum(B[j] for j in range(3*m//2,2*m))%p
        assert V==(s_mid+t)%p
        # Published two-truncation theorem predicts this all-prime equality;
        # finite checking here does not prove that scope.
        assert V==0,(p,'GZ truncation sanity')
        lateW=sum(W[3*m+1:])%mod
        lateS=sum(S[3*m+1:])%mod
        assert lateW==p*p*U%mod and lateS==p*p*V%mod
        low=sum(W[k]-S[k] for k in range(3*m+1))%mod
        assert (sum(W)-sum(S)-low-p*p*U)%mod==0
        all_obs.append((p,U,s_mid,t,low))
    for p in [7,13,19,181,373,733]:
        m=(p-1)//6;H=(3*p-1)//4
        A,B=reflected_jets(p)
        for k in range(3*m+1,H+1):
            w,s=direct_binomial_late(p,k)
            assert w%p**2==0 and s%p**2==0
            j=p-1-k
            assert s//p**2==B[j],(p,k,'direct-S')
            if k<=4*m: assert w//p**2==A[j],(p,k,'direct-W')
            else: assert w==0,(p,k,'direct-W-high')
    p=181;m=(p-1)//6
    A,B=reflected_jets(p)
    assert sum(B[j] for j in range(3*m//2,2*m))%p==0
    assert sum(B[j] for j in range(2*m,3*m))%p==0
    assert sum(A.values())%p==152
    assert next(x[4] for x in all_obs if x[0]==p)==950069
    for p in [13,19,181,373,733]:
        q=next(x for x in all_obs if x[0]==p)
        print(f'p={p}: U={q[1]}, S_mid={q[2]}, S_tail={q[3]}, low={q[4]}')
    print(f'PASS: {len(ps)} primes, {units} termwise reflected checks, six direct-binomial cases')
    print('All-prime cancellation uses Guo-Zudilin theorem; W/S bridge remains OPEN')

if __name__=='__main__':
    run()
