#!/usr/bin/env python3
"""Independent author exact check: finite Clausen defect E^[3] modulo p^3.
All arithmetic uses prime-power integers, exact coefficient recurrences and two
separate routes (original finite 3F2/2F1 evaluation vs reflected source ports).
"""
import json
from pathlib import Path


def primes(n):
    sv = bytearray(b'\x01') * (n + 1)
    sv[:2] = b'\x00\x00'
    for q in range(2, int(n ** 0.5) + 1):
        if sv[q]:
            sv[q*q::q] = b'\x00' * ((n-q*q)//q+1)
    return [p for p in range(7, n+1) if sv[p] and p % 6 == 1]


def verify(p):
    r=(p-1)//6
    mod=p**5; m=p**3
    inv2=pow(2,-1,mod)
    c=[1]*p; a=[1]*p
    for k in range(p-1):
        c[k+1]=(c[k] * (6*k+1)*(3*k+1) * pow(18*(k+1)**2,-1,mod))%mod
        a[k+1]=(a[k] * (2*k+1)*(3*k+1)*(3*k+2) * pow(18*(k+1)**3,-1,mod))%mod
    G=thetaG=W=0; z=1
    for k in range(p):
        G=(G+c[k]*z)%mod
        thetaG=(thetaG+k*c[k]*z)%mod
        W=(W+(6*k+1)*a[k]*z)%mod
        z=z*inv2%mod
    numerator=(W-G*G-12*G*thetaG)%mod
    assert numerator % (p*p)==0,(p,'nondivisible')
    direct=numerator//(p*p)
    assert c[-1]%(p*p)==0,(p,'bad-high-edge')
    U=(c[-1]//(p*p))%m
    scale=(-2*U*pow(2,-(p-1),m))%m

    Lam=Gam=LH=GH=LQ=GQ=0
    A=1; H=J=0; power=1
    port_low=port_mid=0
    # At step i include s=i-1, then accumulate c_i * (...) for that prefix.
    for i in range(1,2*r+1):
        s=i-1
        Q=(H*H+J)*pow(2,-1,m)%m
        X=power*A%m
        Lam=(Lam+X)%m; Gam=(Gam+s*X)%m
        LH=(LH+X*H)%m; GH=(GH+s*X*H)%m
        LQ=(LQ+X*Q)%m; GQ=(GQ+s*X*Q)%m
        B=((6*i-5)*Lam-6*Gam)%m
        K=((6*i-5)*LH-6*GH+6*Lam)%m
        L=((6*i-5)*LQ-6*GQ+6*LH)%m
        ci=c[i]%m
        ti=(scale*ci*pow(2,-i,m) * (B+p*K+p*p*L))%m
        if i<=r: port_low=(port_low+ti)%m
        else: port_mid=(port_mid+ti)%m
        den1=6*s+11;den2=3*s+5
        assert den1%p and den2%p and (s+1)%p
        H=(H+6*pow(den1,-1,m)+3*pow(den2,-1,m)-2*pow(s+1,-1,m))%m
        J=(J+36*pow(den1,-2,m)+9*pow(den2,-2,m)-2*pow(s+1,-2,m))%m
        A=(A*18*(s+1)**2*pow(den1*den2,-1,m))%m
        power=power*2%m

    # Independent high/high triangular source component modulo p (then scale p^2).
    A0=1; ppow=1; Xs=[]
    for s in range(4*r):
        Xs.append(A0*ppow%p)
        if s+1<4*r:
            A0=A0*18*(s+1)**2*pow((6*s+11)*(3*s+5),-1,p)%p
        ppow=ppow*2%p
    Lpref=[0]; Gpref=[0]
    for s,x in enumerate(Xs):
        Lpref.append((Lpref[-1]+x)%p)
        Gpref.append((Gpref[-1]+s*x)%p)
    coef=0
    for s,x in enumerate(Xs):
        length=min(4*r,p-1-s)
        coef=(coef+x*((11+6*s)*Lpref[length]+6*Gpref[length]))%p
    high_high=p*p*(coef*pow(100,-1,p)%p)
    reconstructed=(port_low+port_mid+high_high)%m
    assert direct==reconstructed,(p,direct,reconstructed,port_low,port_mid,high_high)
    return dict(p=p,r=r,E_p3=direct,E_p2=direct%(p*p),E_p=direct%p,
                port_low_high=port_low,port_middle_high=port_mid,
                port_high_high=high_high,coefficient_high_high=coef*pow(100,-1,p)%p,
                edge_unit_mod_p3=U)


def main():
    checked=[]
    for p in primes(2000):
        checked.append(verify(p))
    out=dict(schema='D25_CLAUSEN_SIXMOMENT_HIGHHIGH_P5_EXACT_CHECK_V1',
            date='2026-11-03',domain='all primes 7<=p<=2000, p=1 mod6',
            number_primes=len(checked),result='PASS',
            verification='independent original finite Gauss and 3F2 mod p^5 scalar versus six reflected prefix moments + high/high triangular carrier',
            samples=[x for x in checked if x['p'] in (7,13,19,31,37,43,73,181,373,1171,1999)],
            proof_status='algebraic theorem requires independent review',
            native_original_H0_B0=False)
    dest=Path('/mnt/data/d25_clausen_p5_sixmoment_full_results_20261103.json')
    dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
