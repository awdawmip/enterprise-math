#!/usr/bin/env python3
"""Exact modular check of a single boundary injection in the D25 Gauss carry.
Author-side finite regression; does not infer a universal theorem from tests.
"""
from math import comb

def primes_upto(n):
    sieve = bytearray(b'\x01') * (n+1)
    sieve[0:2] = b'\x00\x00'
    for k in range(2, int(n**0.5)+1):
        if sieve[k]:
            sieve[k*k:n+1:k] = b'\x00' * ((n-k*k)//k+1)
    return [k for k in range(5,n+1) if sieve[k] and k % 8 in (5,7)]

def check(p):
    q=(p-5)//8 if p%8==5 else (p-7)//8
    if p%8==5:
        a,b,c,d,h,sign=(5*q+3,7*q+4,q,3*q+1,4*q+3,1)
    else:
        a,b,c,d,h,sign=(7*q+6,5*q+4,3*q+2,q,4*q+4,-1)
    L,R=min(a,b),max(a,b)
    assert L==h+q and R<p
    mod=p*p
    # Original Pochhammer polynomial, independent of the carry recurrence.
    f=[1]
    for k in range(p-1):
        ratio=(8*k+1)*(8*k+3)*pow(64*(k+1)**2,-1,mod)
        f.append(f[-1]*ratio %mod)
    # Build Euler polynomial B=(1-z)^h J via integer binomials.
    J=[comb(c,k)*comb(d,k)%mod for k in range(q+1)]
    B=[0]*(p)
    for i in range(h+1):
        x=(-1 if i%2 else 1)*comb(h,i)
        for j in range(q+1):
            B[i+j]=(B[i+j]+x*J[j])%mod
    assert len(B)==p and all((f[k]-B[k])%p==0 for k in range(p))
    C=[((f[k]-B[k])%mod)//p for k in range(p)]
    assert C[0]==0
    lead=((-1 if h%2 else 1)*comb(max(c,d),q))%p
    assert lead==B[L]%p
    seed=(sign*5*pow(32,-1,p)*lead*pow((L+1)**2,-1,p))%p
    assert C[L+1]==seed,(p,C[L+1],seed)
    terms=[seed]
    for s in range(1,R-L):
        terms.append((terms[-1]*s*(s-(R-L))*pow((L+s+1)**2,-1,p))%p)
    assert terms==C[L+1:R+1], (p,'middle mismatch')
    assert all(x==0 for x in C[R+1:]),(p,'late carry mismatch')
    if p>=11:
        assert all(x!=0 for x in terms), (p, 'unexpected middle p-adic valuation')
        assert all(f[k]%p==0 and f[k]%mod !=0 for k in range(L+1,R+1))
        assert all(f[k]%mod==0 for k in range(R+1,p))
    z=pow(9,-1,p)
    sum_mid=sum(terms[s]*pow(z,L+1+s,p) for s in range(R-L))%p
    dmid=sum((1+16*(L+1+s))*terms[s]*pow(z,L+1+s,p) for s in range(R-L))%p
    # Independent per-term evaluation validates weighted observer split.
    assert sum_mid==sum(C[k]*pow(z,k,p) for k in range(L+1,p))%p
    assert dmid==sum((1+16*k)*C[k]*pow(z,k,p) for k in range(L+1,p))%p
    return dict(p=p,L=L,R=R,seed=seed,mid_val=sum_mid,mid_weighted=dmid,primes_q=q)

def main():
    pp=primes_upto(2000)
    samples=[]
    total_middle=0
    for p in pp:
        row=check(p)
        total_middle+=row['R']-row['L']
        if p in (5,7,13,19,23,29,37,373):
            samples.append(row)
    print(f'PASS primes={len(pp)} through 2000; exact_middle_positions={total_middle}; high_boundary=all; beyond_R=all; both_mid_ports=all')
    for x in samples: print(x)

if __name__=='__main__':
    main()
