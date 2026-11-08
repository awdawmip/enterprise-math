#!/usr/bin/env python3
"""Exact original weighted-216 W_p (mod p^3), with source-preserving p-adic valuation bands.
No numpy, floating point, p-divisible inverses or surrogate H0/B0.
Original frozen target p % 24 in (13,19); enlarged falsifier p > 3 all residues.
"""
from math import comb, isqrt
from sys import argv
import json


def primes(limit):
    s=bytearray(b'\x01')*(limit+1); s[:2]=b'\x00\x00'
    for x in range(2,isqrt(limit)+1):
        if s[x]:s[x*x::x]=b'\x00'*(((limit-x*x)//x)+1)
    return [i for i in range(5,limit+1) if s[i]]


def original_W(p):
    assert p>3
    m=(p-1)//6
    q=p**3; cut=(2*p-1)//3
    # Exact p-free factorial up to 3*cut <= 2p-1.
    maxfac=3*cut
    fac=[1]*(maxfac+1)
    for k in range(1,maxfac+1):
        fac[k]=fac[k-1]*(1 if k==p else k) % q
    invf=[0]*(cut+1)
    invf[cut]=pow(fac[cut],-1,q)
    for k in range(cut,0,-1):
        invf[k-1]=invf[k]*k % q
    root=pow(216,-1,q)
    inv216n=1
    branches=[0,0,0]
    for n in range(cut+1):
        e=(2*n)//p+(3*n)//p
        assert 0<=e<=2
        core=fac[2*n]*fac[3*n] % q
        core=core*pow(invf[n],5,q)%q
        term=(6*n+1)*core*pow(p,e,q)*inv216n % q
        band=e
        branches[band]=(branches[band]+term)%q
        inv216n=inv216n*root%q
    W=sum(branches)%q
    return W,branches


def original_W_naive(p):
    q=p**3
    return sum((6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,q) for n in range(p))%q


def scan(limit=10000, verbose=False):
    checked=0; targets=0; errors=[]; all_failures=[]; controls=[]; checksum=0
    examples={}; nonzero_tail=0; nonzero_bulk=0
    for p in primes(limit):
        W,b=original_W(p)
        if p<=73 or p==373:
            assert W==original_W_naive(p), (p,W,original_W_naive(p))
        expected=p if p%3==1 else -p
        if (W-expected)%(p**3)!=0:all_failures.append((p,W,(W-expected)%(p**3)))
        if p%24 in (13,19):
            targets+=1
            x=(W-p)%(p**3)
            if x!=0:errors.append((p, W, x))
            assert b[1]%p==0 and b[2]%(p*p)==0, (p,b)
            tail=b[2]//(p*p)%p
            bulk=(b[0]+b[1])%(p**3)
            bulk_digit=((bulk-p)//(p*p))%p if (bulk-p)%(p*p)==0 else None
            if tail:nonzero_tail+=1
            if bulk_digit:nonzero_bulk+=1
            if p in (13,19,37,43,211,373,1009):
                examples[str(p)]={"W_mod_p3":W,"bands_mod_p3":b,"tail_digit":tail,"bulk_defect_digit":bulk_digit}
            checksum=(checksum*1315423911+W+tail*1000003+p)%(2**64)
        else:
            if p<100 or p==1009:controls.append([p, W, W%p, (W//p)%p if W%p==0 else None])
        checked+=1
    return {"limit":limit,"primes_gt3_checked":checked,"all_prime_character_failures":all_failures[:30],"all_prime_character_failure_count":len(all_failures),"target_prime_count":targets,"target_failures":errors[:30],"total_target_failures":len(errors),"nonzero_tail_target_count":nonzero_tail,"nonzero_bulk_defect_target_count":nonzero_bulk,"examples":examples,"negative_class_controls":controls,"rolling_checksum_u64":checksum}

if __name__=='__main__':
    L=int(argv[1]) if len(argv)>1 else 10000
    print(json.dumps(scan(L),ensure_ascii=False,sort_keys=True,indent=2))
