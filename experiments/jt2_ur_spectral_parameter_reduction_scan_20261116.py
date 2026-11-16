#!/usr/bin/env python3
"""Exact p-adic spectral-parameter reduction of the JT2 UR norm-jet residue.

Uses the source-published O(m) symmetric-square scanner for original u,d,J
and independently builds the finite hypergeometric truncation at C0=-1/9.
Checks two algebraic reduction identities for every admissible prime.
"""
import argparse
import math
from jt2_ur_symmetric_square_linear_scan_20261116 import evaluate, primes_upto

def check_prime(p):
    m=(p-1)//6
    mod=p*p
    half=pow(2,-1,mod)
    half_p=half%p
    C0=(-pow(9,-1,mod))%mod
    a=1
    da=0
    ypow=1
    ypow_p=1
    H=0
    DH=0
    H_Y=0
    S0=0
    a_m=None
    a_prev=None
    for j in range(m+1):
        H=(H+a*ypow)%mod
        DH=(DH+da*ypow)%mod
        if j:
            H_Y=(H_Y+j*a*a_prev)%mod
        S0=(S0+(a%p)*ypow_p*pow(2*m+2*j+1,-1,p))%p
        if j==m:
            a_m=a%p
        a_prev=ypow
        ypow=ypow*half%mod
        ypow_p=ypow_p*half_p%p
        if j<m:
            den=pow((j+1)*(2*j+1),-1,mod)
            ratio=(j*(2*j+1)-C0)*den%mod
            da=(da*ratio-a*den)%mod
            a=a*ratio%mod

    c0=(((-1)**m)*math.comb(2*m,m)*pow(4,-m,mod))%mod
    pwr=pow(half_p,m,p)
    S=(c0*S0*pwr)%p
    cm=(c0*a_m)%p
    out=evaluate(p)
    CM0,J,u,d,epsilon=out[2:]
    assert CM0==0 and H%p==0
    assert d==c0*H_Y%p
    z=c0*DH%p
    J_spec=((d*z*pow(2,-1,p))+cm*S)%p
    shift_check=(18*u-z-18*c0*(H//p))%p
    epsilon_reduced=(18*c0*d*(H//p)-2*cm*S-3)%p
    assert J_spec==J and shift_check==0 and epsilon_reduced==epsilon
    return (p,J_spec,epsilon_reduced)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--limit",type=int,default=20000)
    args=parser.parse_args()
    n=0
    for p in primes_upto(args.limit):
        check_prime(p)
        n+=1
    print(f"SUMMARY hi={args.limit} exact_spectral_checks={n} failures=0")

if __name__=="__main__":
    main()
