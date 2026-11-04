#!/usr/bin/env python3
"""Exact modular verification of original D25 a/b fifth-digit reflection.
No floating point. Independent high sums from original recurrences.
Author-side portable evidence, not a native Source/CM H0/B0 experiment.
"""
import argparse
import math


def primes_up_to(N):
    sieve = bytearray(b'\x01') * (N + 1)
    sieve[:2] = b'\x00\x00'
    for k in range(2, math.isqrt(N) + 1):
        if sieve[k]:
            sieve[k*k::k] = b'\x00' * ((N - k*k)//k + 1)
    return [k for k in range(5, N+1) if sieve[k]]


def a_b_mod(p, modulus):
    a = [1]
    b = [1]
    for j in range(p-1):
        den_a = 36 * (j+1)**3
        den_b = 576 * (j+1)**3
        a.append(a[-1]*(2*j+1)*(3*j+1)*(3*j+2)*pow(den_a,-1,modulus)%modulus)
        b.append(b[-1]*(4*j+1)*(4*j+2)*(4*j+3)*pow(den_b,-1,modulus)%modulus)
    return a,b


def one_prime(p):
    M=p**5
    a,b=a_b_mod(p,M)
    eps=1 if pow(-3%p,(p-1)//2,p)==1 else -1
    J=(sum((6*j+1)*x for j,x in enumerate(a))-2*sum((8*j+1)*x for j,x in enumerate(b))+eps*p)%M
    ma=(p-1)//3
    mb=(p-1)//4
    q216=(pow(216,p-1,p*p)-1)//p
    q2304=(pow(2304,p-1,p*p)-1)//p
    ca=(13*pow(2,-1,p)-q216)%p
    cb=(22*pow(3,-1,p)-q2304)%p
    ha=hb=0
    high_a=high_b=0
    source_a=source_b=0
    count=0
    for k in range(1,max(ma,mb)+1):
        if k<=ma:
            high=a[p-k]
            assert high%p**3==0,(p,k,'a valuation')
            direct=pow(k,3,p*p)*(a[k]%(p*p))*(high//p**3)%(p*p)
            predicted=(-pow(18,-1,p*p)*(1+p*((ca+ha)%p)))%(p*p)
            assert direct==predicted,(p,k,'a fifth digit',direct,predicted)
            term=(1-6*k+6*p)*(high//p**3)
            high_a=(high_a+term)%(p*p)
            source_a=(source_a+(1-6*k+6*p)*predicted*pow(k**3*a[k],-1,p*p))%(p*p)
            count+=1
        if k<=mb:
            high=b[p-k]
            assert high%p**3==0,(p,k,'b valuation')
            direct=pow(k,3,p*p)*(b[k]%(p*p))*(high//p**3)%(p*p)
            predicted=(-pow(96,-1,p*p)*(1+p*((cb+hb)%p)))%(p*p)
            assert direct==predicted,(p,k,'b fifth digit',direct,predicted)
            term=(1-8*k+8*p)*(high//p**3)
            high_b=(high_b+term)%(p*p)
            source_b=(source_b+(1-8*k+8*p)*predicted*pow(k**3*b[k],-1,p*p))%(p*p)
            count+=1
        if k<ma:
            ha=(ha - 3*pow(k,-1,p)+2*pow(2*k+1,-1,p)
                   +3*pow(3*k+1,-1,p)+3*pow(3*k+2,-1,p))%p
        if k<mb:
            hb=(hb - 3*pow(k,-1,p)+4*pow(4*k+1,-1,p)
                   +4*pow(4*k+2,-1,p)+4*pow(4*k+3,-1,p))%p
    assert high_a==source_a and high_b==source_b,(p,'weighted high source')
    # Independent integer-binomial coefficient check at selected small primes.
    if p in (5,7,11,13,19,23,29,97):
        dena=denb=1
        for k in range(p):
            if k:
                dena=dena*216%M
                denb=denb*2304%M
            aa=math.comb(2*k,k)**2 * math.comb(3*k,k)*pow(dena,-1,M)%M
            bb=math.comb(2*k,k)**2 * math.comb(4*k,2*k)*pow(denb,-1,M)%M
            assert a[k]==aa and b[k]==bb,(p,k,'independent binomial')
    return count,(high_a-2*high_b)%(p*p),high_a,high_b,J


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--limit',type=int,default=2000)
    args=parser.parse_args()
    total=0
    out={}
    p5zero=0
    ps=primes_up_to(args.limit)
    for p in ps:
        count,signed,A,B,J=one_prime(p)
        p5zero += (J==0)
        total+=count
        if p in (5,7,11,13,19,23,29,97,373):
            out[p]=(signed,A,B,J)
    print(f'PASS primes={len(ps)} reflected_pairs={total} original_p5_weighted_ports=2 per prime; signed_J_mod_p5_zero={p5zero}')
    for p,item in out.items():
        print(f'p={p} signed_Ha_minus_2Hb_mod_p2={item[0]} Ha_mod_p2={item[1]} Hb_mod_p2={item[2]} signed_J_mod_p5={item[3]}')

if __name__=='__main__':
    main()
