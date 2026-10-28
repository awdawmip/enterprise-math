#!/usr/bin/env python3
"""Exact original-216 vs Guo-Zudilin 2304 kernel: mod-p3 checks and p4 falsifier.

Mod-p3 congruence for the 216 kernel is a conjecture, not a theorem.
No native H0/B0 data are generated.
"""
from math import isqrt, comb
from fractions import Fraction


def primes_below(bound):
    for p in range(5, bound):
        if all(p % d for d in range(2, isqrt(p)+1)):
            yield p


def weighted(p, base, precision):
    modulus=p**precision
    term=1
    answer=0
    for n in range(p):
        answer=(answer+((6*n+1) if base==216 else (8*n+1))*term)%modulus
        if n==p-1:
            continue
        if base==216:
            numerator=(2*n+1)*(3*n+1)*(3*n+2)
            denominator=36*(n+1)**3
        else:
            numerator=(2*n+1)*(4*n+1)*(4*n+3)
            denominator=288*(n+1)**3
        term=term*numerator*pow(denominator,-1,modulus)%modulus
    return answer


def independent_2304(p):
    modulus=p**3
    inverse=pow(2304,-1,modulus)
    power=1
    result=0
    for n in range(p):
        result=(result+(8*n+1)*comb(2*n,n)**2*comb(4*n,2*n)*power)%modulus
        power=power*inverse%modulus
    return result


def main():
    count=0
    frozen=0
    for p in primes_below(6000):
        a=weighted(p,216,3)
        b=weighted(p,2304,3)
        assert a==b,('p3-transport-counterexample',p,a,b)
        assert b==((1 if p%3==1 else -1)*p)%(p**3)
        frozen+=(p%24 in (13,19))
        count+=1
    for p in (5,7,13,19,37,43,211,373):
        assert weighted(p,2304,3)==independent_2304(p)
    p4=[]
    for p in (5,7,13,19,31,37,43,61,67,73,211,373):
        a=weighted(p,216,4)
        b=weighted(p,2304,4)
        assert (a-b)%(p**3)==0
        p4.append((p,((a-b)%(p**4))//p**3))
    assert p4[1]==(7,4) and p4[-1]==(373,114)
    # Exact first-coefficient difference: A1=7/18, B1=3/32.
    assert Fraction(7,18)-Fraction(3,32)==Fraction(85,288)
    # For all j>=0: (j+1/3)(j+2/3) > (j+1/4)(j+3/4)
    # because 2/9 > 3/16. The n-th weighted A/B ratio
    # is > (9/2)^n * (6n+1)/(8n+1) > 1 for every n>=1.
    assert Fraction(2,9)>Fraction(3,16)
    print('PASS_MOD_P3_INTER_KERNEL_OBSERVATION',count,'primes <6000; frozen target count',frozen)
    print('EXACT_ANALYTIC_NAIVE_IDENTITY_FALSIFIED','A_infinity-B_infinity > 85/288')
    print('P4_COUNTEREXAMPLE_CERTIFICATES',p4)
    print('P373',(weighted(373,216,3),weighted(373,2304,3)), 'delta_p4_digit',p4[-1][1])


if __name__=='__main__':main()
