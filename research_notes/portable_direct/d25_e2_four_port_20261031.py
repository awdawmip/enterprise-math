#!/usr/bin/env python3
"""Exact author-side original-216 / E.2 first-digit four-port certificate.

Finite-field/p-adic arithmetic only; no native H0/B0 execution.
"""


def primes(limit):
    sieve=bytearray(b'\1')*(limit+1)
    sieve[:2]=b'\0\0'
    for i in range(2,int(limit**.5)+1):
        if sieve[i]:
            sieve[i*i::i]=b'\0'*((limit-i*i)//i+1)
    return [p for p in range(7,limit+1) if sieve[p] and p%24 in (13,19)]


def run_one(p):
    ell=(p-1)//6
    m=2*ell; h=3*ell; q=4*ell
    md=p*p
    fac=[1]*(q+1)
    for n in range(1,q+1):fac[n]=fac[n-1]*n%md
    invfac=[1]*(q+1)
    invfac[q]=pow(fac[q],-1,md)
    for n in range(q,0,-1):invfac[n-1]=invfac[n]*n%md
    def cmb(n,k):return fac[n]*invfac[k]*invfac[n-k]%md
    inv2=pow(2,-1,md)
    pow2inv=[1]*(h+1)
    for n in range(1,h+1):pow2inv[n]=pow2inv[n-1]*inv2%md
    harm=[0]*(q+1)
    for n in range(1,q+1):harm[n]=(harm[n-1]+pow(n,-1,p))%p
    def dh(v,n):return (harm[v]-harm[v-n])%p
    i2=pow(2,-1,p);i3=pow(3,-1,p)
    carry_n=gauss_jet=e2_jet=onecross=0
    for n in range(m+1):
        w=6*n+1
        t=((-1)**n*cmb(h,n)*cmb(m,n)*cmb(q,n)*pow2inv[n])%md
        v=cmb(m,n)**3%md
        carry_n=(carry_n+w*(t-v))%md
        K=(i2*dh(h,n)+i3*dh(m,n)+2*i3*dh(q,n))%p
        gauss_jet=(gauss_jet-w*t*K)%p
        e2_jet=(e2_jet+w*v*dh(m,n))%p
    assert carry_n%p==0,(p,carry_n)
    carry=carry_n//p%p
    for n in range(m+1,h+1):
        w=6*n+1
        u=fac[m]*fac[n-m-1]*pow(3*fac[n],-1,p)%p
        u=u*cmb(h,n)*cmb(q,n)*pow2inv[n]%p
        onecross=(onecross+w*u)%p
    # Independent exact original recurrence, not computed from the port formulas.
    a=b=1
    A0=A1=B0=0
    for n in range(h+1):
        w=6*n+1
        if n<=m:
            A0=(A0+w*a)%md
            B0=(B0+w*b)%md
        else:
            A1=(A1+w*a)%md
        if n<h:
            a=a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,md)%md
            b=b*-(3*n+1)**3*pow(27*(n+1)**3,-1,md)%md
    true_diff=(A0+A1-B0)%md
    four=(carry+gauss_jet+e2_jet+onecross)%p
    assert true_diff%p==0,(p,'first-digit prerequisite')
    assert four==true_diff//p%p,(p,four,true_diff//p)
    return {'p':p,'carry':carry,'low216_harm':gauss_jet,'e2_harm':e2_jet,
            'once_cross':onecross,'total':four,'direct_digit':true_diff//p%p}


def run(limit=5000):
    rows=[run_one(p) for p in primes(limit)]
    print('FROZEN_PRIMES',len(rows),'ZERO_FIRST_BRIDGE_SAMPLES',sum(r['total']==0 for r in rows))
    for r in rows:
        if r['p'] in (13,19,37,157,373):print('ANCHOR',r)
    assert len(rows)==166
    print('PASS_D25_E2_FOUR_PORT_DIGIT_FORMULA_EXACT')


if __name__=='__main__':run()
