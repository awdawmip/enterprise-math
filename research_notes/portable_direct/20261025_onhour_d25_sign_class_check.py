#!/usr/bin/env python3
"""D25 original weighted sum, two exact p^3 arithmetic observers.

AUTHOR-PORTABLE / NOT SOURCE-NATIVE BENCHMARK / NOT INDEPENDENT PEER REVIEW.
"""
from collections import Counter
from math import isqrt


def primes_upto(bound: int):
    ok = bytearray(b'\x01')*(bound+1)
    ok[0:2] = b'\x00\x00'
    for q in range(2, isqrt(bound)+1):
        if ok[q]:
            ok[q*q:bound+1:q] = b'\x00'*(((bound-q*q)//q)+1)
    return [i for i,good in enumerate(ok) if good]


def pochhammer_recurrence(p: int) -> int:
    mod = p**3
    a = 1
    total = 1
    for n in range(1,p):
        a = a*(2*n-1)*(3*n-2)*(3*n-1)*pow(36*n**3,-1,mod)%mod
        total = (total+(6*n+1)*a)%mod
    return total


def independent_factorial(p: int) -> int:
    mod = p**3
    fact1=fact2=fact3=1
    q=pow(216,-1,mod)
    qpow=1
    total=0
    for n in range(p):
        if n:
            fact1=fact1*n%mod
            fact2=fact2*(2*n-1)*(2*n)%mod
            fact3=fact3*(3*n-2)*(3*n-1)*(3*n)%mod
            qpow=qpow*q%mod
        b=fact2*fact3*pow(fact1,-5,mod)*qpow%mod
        total=(total+(6*n+1)*b)%mod
    return total


def expected_sign(p:int):
    return p if p%3==1 else (-p)%(p**3)


def main():
    pp=[p for p in primes_upto(5000) if p>3]
    classes=Counter()
    exceptions=[]
    for p in pp:
        residue=pochhammer_recurrence(p)
        good=(residue==expected_sign(p))
        classes[(p%24,good)]+=1
        if not good:
            exceptions.append((p,residue,expected_sign(p)))
    print("PRIME_BOUND=5000")
    print("TOTAL_PRIMES",len(pp))
    print("SIGNED_CONGRUENCE_EXCEPTIONS",exceptions[:12])
    print("CLASSES",dict(sorted(classes.items())))
    cross=[p for p in pp if p<=500 or p%24 in (13,19)]
    cross += [1013,1103,1301,1741,1997,2111,2309,3041,4001,4999,19963]
    cross=[p for p in sorted(set(cross)) if p in pp or p==19963]
    larger=next(p for p in range(19991,20100)
                if p%6==5 and all(p%d for d in range(2,isqrt(p)+1)))
    cross.append(larger)
    print("CROSSCOUNT",len(cross),"EXTRA_LARGE_INERT",larger)
    for p in cross:
        x=pochhammer_recurrence(p)
        y=independent_factorial(p)
        assert x==y,(p,x,y)
        assert x==expected_sign(p),(p,x)
    for p in (5,7,11,13,17,19,23,211,19963,larger):
        print("SAMPLE",p,"p_mod24",p%24,
              "W_mod_p3",pochhammer_recurrence(p),
              "expected",expected_sign(p))
    print("PASS: all prime checks and independent factorial crosschecks.")


if __name__=="__main__":
    main()
