#!/usr/bin/env python3
"""Exact 3-stratum parameter shift for truncated weighted 216 3F2, modulo p^3.
Independent of native H0/B0; author-side only. Python stdlib.
"""
import json, argparse


def primes_upto(bound):
    sieve=bytearray(b'\x01')*(bound+1)
    sieve[0:2]=b'\x00\x00'
    for d in range(2,int(bound**0.5)+1):
        if sieve[d]: sieve[d*d::d]=b'\x00'*((bound-d*d)//d+1)
    return [p for p in range(7,bound+1) if sieve[p] and p%6==1]


def case(p):
    assert p%6==1 and p>=7
    n=(p-1)//6
    mod=p**3
    shifts=((3*n,2),(2*n,3),(4*n,3))
    # (m, denominator of beta); beta=(1/2,1/3,2/3) handled explicitly below
    betas=(pow(2,-1,mod),pow(3,-1,mod),2*pow(3,-1,mod)%mod)
    unit=1
    valuation=0
    sigma1=0
    sigma2_raw=0
    denom=1   # 2^k (k!)^3
    W_calc=0
    sums=[0,0,0,0]
    for k in range(p):
        if valuation<3:
            tail=(1+p*sigma1+p*p*((sigma1*sigma1-sigma2_raw)*pow(2,-1,mod)))%mod
            coef=(pow(p,valuation,mod)*unit*pow(denom,-1,mod)*tail)%mod
            sums[valuation]=(sums[valuation]+(6*k+1)*coef)%mod
            W_calc=(W_calc+(6*k+1)*coef)%mod
        if k==p-1:
            break
        # append (alpha_a+k), alpha_a = -m_a + p*beta_a
        for (m,_),beta in zip(shifts,betas):
            a=k-m
            if a==0:
                valuation+=1
                unit=unit*beta%mod
            else:
                unit=unit*a%mod
                inv=pow(a,-1,mod)
                sigma1=(sigma1+beta*inv)%mod
                sigma2_raw=(sigma2_raw+beta*beta*inv*inv)%mod
        denom=denom*(2*(k+1)**3)%mod
    # Reference independent direct hypergeometric recurrence with no valuation expansion
    w=1;term=1
    inv36=pow(36,-1,mod)
    for k in range(1,p):
        term=(term*(2*k-1)*(3*k-2)*(3*k-1)*inv36*pow(k**3,-1,mod))%mod
        w=(w+(6*k+1)*term)%mod
    assert w==W_calc,(p,w,W_calc)
    assert sums[3]==0
    return {'p':p,'n':n,'W':w,'W_minus_p_div_p2':((w-p)//(p*p))%p if (w-p)%(p*p)==0 else None,'valuation_channels':sums[:3]}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--limit',type=int,default=10000)
    args=parser.parse_args()
    ps=primes_upto(args.limit)
    out=[case(p) for p in ps]
    print(json.dumps({'primes_checked':len(out),'pass':len(out),'anchors':[r for r in out if r['p'] in (7,13,19,37,139,373,997)],'all_W_eq_p_mod_p3':sum(r['W']==r['p'] for r in out)},indent=2))
