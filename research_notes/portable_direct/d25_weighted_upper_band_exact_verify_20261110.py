#!/usr/bin/env python3
"""D25 weighted-W upper band, exact independent integer checks; author-side only.
Frozen scientific input: c47e13e4aba0e006366f989d6334d443f6333ae3.
"""
from math import isqrt


def primes(bound):
    for p in range(13, bound+1):
        if p % 24 in (13, 19) and all(p % d for d in range(2, isqrt(p)+1)):
            yield p


def high_factorial(p):
    m = (p-1)//6
    fact = [1]*p
    for i in range(1,p): fact[i] = fact[i-1]*i % p
    h = 0
    for k in range(3*m+1,4*m+1):
        h += (6*k+1)*fact[2*k-p]*fact[3*k-p] * pow(216,-k,p)*pow(fact[k],-5,p)
    return h % p


def high_recurrence(p,full=False):
    m = (p-1)//6
    q = p**3
    a = 1
    blocks = [0,0,0]
    stop = p-1 if full else 4*m+1
    for k in range(stop):
        band = 0 if k<=2*m else (1 if k<=3*m else (2 if k<=4*m else 3))
        if band<=2: blocks[band] = (blocks[band]+(6*k+1)*a) % q
        else: assert a==0,(p,k)
        if k+1<stop:
            a = a*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,q)%q
    assert blocks[2]%(p*p)==0
    return blocks,blocks[2]//(p*p)


def factorial_mod_p3(p):
    m = (p-1)//6
    q = p**3
    f = [1]*(3*p)
    for i in range(1,3*p): f[i] = f[i-1]*i%q
    upper = 0
    for k in range(3*m+1,4*m+1):
        a = f[2*k]*f[3*k]*pow(216,-k,q)*pow(f[k],-5,q)%q
        assert a%(p*p)==0
        upper = (upper+(6*k+1)*a)%q
    return upper//(p*p)


def main():
    ps=list(primes(10000))
    assert len(ps)==312
    zeros=[]
    for p in ps:
        h=high_factorial(p)
        blocks,r=high_recurrence(p)
        assert h==r,(p,h,r)
        if not h: zeros.append(p)
        if p in (13,19,157,373):
            bb,rr=high_recurrence(p,True)
            assert bb==blocks and rr==r
            assert factorial_mod_p3(p)==h
            assert sum(bb)%(p**3)==p
            print(p,{"L":bb[0],"M":bb[1],"H":h,
                     "W":sum(bb)%(p**3),
                     "W_without_H":(bb[0]+bb[1])%(p**3)})
    print("checked",len(ps),"eligible primes<=10000; H-zero primes:",zeros)


if __name__=="__main__": main()
