#!/usr/bin/env python3
"""All-prime two-seam Green certificate, exact finite modular arithmetic.
Author-side only; no native Enterprise Math experiment/admission.
"""
from math import isqrt, comb

def primes(limit):
    q=bytearray(b'\x01')*(limit+1); q[:2]=b'\x00\x00'
    for d in range(2,isqrt(limit)+1):
        if q[d]:q[d*d:limit+1:d]=b'\x00'*((limit-d*d)//d+1)
    return [p for p in range(5,limit+1) if q[p]]

def vp(n,p):
    if not n:return 10**9
    s=0
    while n%p==0:n//=p;s+=1
    return s

def check(p,detail=False):
    modulus=p**3; a=[1]*p;b=[1]*p;rho=[0]*(p-1);gamma=[0]*(p-1)
    ai=pow(36,-1,modulus);bi=pow(576,-1,modulus);gi=pow(288,-1,modulus)
    for j in range(p-1):
        inv=pow(j+1,-3,modulus)
        rho[j]=(4*j+1)*(4*j+2)*(4*j+3)*bi*inv%modulus
        gamma[j]=(2*j+1)*(56*j*(j+1)+13)*gi*inv%modulus
        a[j+1]=a[j]*(rho[j]+gamma[j])%modulus
        b[j+1]=b[j]*rho[j]%modulus
    if p in (5,7,11,13,19,23,97,373):
        for j in range(p):
            assert a[j]==comb(2*j,j)**2*comb(3*j,j)*pow(216,-j,modulus)%modulus
            assert b[j]==comb(2*j,j)**2*comb(4*j,2*j)*pow(2304,-j,modulus)%modulus
    L=p//4+1;M=(p+1)//2;R=3*p//4+1;cuts={L,M,R}
    assert 1<L<M<R<=p-1
    K=[[0]*(p-1) for _ in range(3)]
    full=[0]*(p-1)
    for j in range(p-2,-1,-1):
        w=6*(j+1)+1
        if j==p-2:
            full[j]=K[0][j]=w%modulus
        else:
            full[j]=(w+rho[j+1]*full[j+1])%modulus
            z=int(j+2 in cuts)
            K[0][j]=(w+(rho[j+1]*K[0][j+1] if not z else 0))%modulus
            for m in (1,2):
                K[m][j]=rho[j+1]*K[m-z][j+1]%modulus if m>=z else 0
    channels={(e,m):0 for e in range(3) for m in range(3-e)}
    for j in range(p-1):
        e=2*j//p+3*j//p+vp((2*j+1)*(56*j*(j+1)+13),p)
        if e<=2:
            for m in range(3-e):
                channels[e,m]=(channels[e,m]+a[j]*gamma[j]*K[m][j])%modulus
    g0=sum(channels[e,0] for e in (0,1,2))%modulus
    green=sum(a[j]*gamma[j]*full[j] for j in range(p-1))%modulus
    assert sum(channels.values())%modulus==green
    def tail(start,stop):
        prod=1;out=0
        for n in range(start,stop):
            out=(out+(6*n+1)*prod)%modulus
            if n<stop-1:prod=prod*rho[n]%modulus
        return out
    T0=tail(L,M);T1=tail(M,R);T2=tail(R,p)
    E0=rho[L-1]*(a[L-1]-b[L-1])%modulus
    E1=rho[M-1]*(a[M-1]-b[M-1])%modulus
    E2=rho[R-1]*(a[R-1]-b[R-1])%modulus
    assert E0%p==E1%p**2==E2==0
    assert (green-g0-E0*T0-E1*T1-E2*T2)%modulus==0
    assert (channels[0,1]+channels[1,1]+channels[0,2]-E0*T0-E1*T1)%modulus==0
    h=(p-1)//2
    chi=1 if pow(6,h,p)==1 else -1
    assert a[h]%p==b[h]%p==rho[h]%p==0
    assert a[h]//p%p==(-2*chi)%p
    assert b[h]//p%p==(-1)%p
    assert rho[h]//p%p==(-pow(36,-1,p))%p
    assert E1//p**2%p==(2*chi-1)*pow(36,-1,p)%p
    wa=sum((6*n+1)*a[n] for n in range(p))%modulus
    vb=sum((8*n+1)*b[n] for n in range(p))%modulus
    moment=sum(2*n*b[n] for n in range(p))%modulus
    assert (wa-vb-green+moment)%modulus==0
    assert (wa-vb-g0-E0*T0-p**2*((2*chi-1)*pow(36,-1,p)%p)*T1+moment)%modulus==0
    expected=(p if p%3==1 else -p)%modulus
    if detail:
        print(f"p={p} class={p%24} chi6={chi} E0/p={E0//p%p} E1/p²={E1//p**2%p} W={wa} V={vb}")
    assert wa==vb==expected,(p,wa,vb,expected)
    return p%6

if __name__=="__main__":
    cases=primes(5000)
    counts={1:0,5:0}
    for p in cases:
        counts[check(p,p in (5,7,11,13,19,23,97,373))]+=1
    print(f"PASS all={len(cases)} p_mod6_5={counts[5]} p_mod6_1={counts[1]} six_channel=True two_seam=True all_class_finite=True")
