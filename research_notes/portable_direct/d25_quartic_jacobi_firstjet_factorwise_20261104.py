#!/usr/bin/env python3
"""Exact author-side certificate for the quartic Gauss Jacobi first jet.
Input: all primes p=8q+5 within an explicit finite bound.
Outputs: integer congruences and separate unit, harmonic, Frobenius sources.
Mathematical status: coefficient jet and exclusive-zero theorem proved;
class-selected second-digit vanishing supported by finite checks only.
"""
from math import isqrt


def primes(limit):
    f = bytearray(b'\x01') * (limit+1)
    f[:2] = b'\x00\x00'
    for i in range(2, isqrt(limit)+1):
        if f[i]:
            f[i*i:limit+1:i] = b'\x00' * ((limit-i*i)//i+1)
    return [p for p in range(5, limit+1) if f[p] and p%8==5]


def check(p):
    q=(p-5)//8
    L=5*q+3
    M=7*q+4
    mod=p*p
    h=[0]*(M+1)
    for n in range(1,M+1):
        h[n]=(h[n-1]+pow(n,-1,p))%p
    c5=5*pow(8,-1,p)%p
    c7=7*pow(8,-1,p)%p
    inv576=pow(576,-1,mod)
    inv9=pow(9,-1,mod)
    j=v=1
    J0=JD=K0=KD=0
    for k in range(L+1):
        dk=(c5*(h[L]-h[L-k])+c7*(h[M]-h[M-k]))%p
        assert v == j*(1-p*dk)%mod, ('unit first jet', p, k)
        J0=(J0+j)%mod
        JD=(JD+k*j)%mod
        K0=(K0+j*dk)%p
        KD=(KD+k*j*dk)%p
        if k<L:
            invk2=pow((k+1)**2,-1,mod)
            j=j*(L-k)*(M-k)*inv9*invk2%mod
            v=v*(8*k+1)*(8*k+3)*inv576*invk2%mod
    sigma=10*(v%p)*pow(441,-1,p)%p
    r=sigma
    R0=RD=0
    for k in range(L+1,M+1):
        R0=(R0+r)%p
        RD=(RD+k*r)%p
        if k<M:
            r=r*(8*k+1)*(8*k+3)*pow(576*(k+1)**2,-1,p)%p
    source_S=(J0+p*(R0-K0))%mod
    source_D=(JD+p*(RD-KD))%mod
    vx=1
    sum_S=1
    sum_D=0
    for k in range(1,p):
        vx=vx*(8*k-7)*(8*k-5)*inv576*pow(k*k,-1,mod)%mod
        sum_S=(sum_S+vx)%mod
        sum_D=(sum_D+k*vx)%mod
    assert source_S==sum_S and source_D==sum_D, ('full first jet', p)
    Y=(sum_S+16*sum_D)%mod
    assert (sum_S*Y)%p==0, ('first digit',p)
    assert (sum_S%p==0) != (Y%p==0), ('ODE exclusivity',p)
    selected=sum_S if p%24==13 else Y
    assert selected==0, ('finite class-selected mod p² vanishing',p,selected)
    return dict(p=p, class24=p%24, L=L, M=M, J0=J0, JD=JD,
                K0=K0,KD=KD,R0=R0,RD=RD,
                S=sum_S,D=sum_D,Y=Y, sigma=sigma)


def main():
    all_checks=[check(p) for p in primes(5000)]
    print('PASS primes=%d class13=%d class5=%d unit_band_coefficients=%d' % (
        len(all_checks),sum(x['class24']==13 for x in all_checks),
        sum(x['class24']==5 for x in all_checks),sum(x['L']+1 for x in all_checks)))
    for p in (5,13,29,37,53,61,373):
        row=next(x for x in all_checks if x['p']==p)
        print('p={p} J0={J0} K0={K0} R0={R0} S={S} JD={JD} KD={KD} RD={RD} Y={Y}'.format(**row))


if __name__=='__main__':
    main()
