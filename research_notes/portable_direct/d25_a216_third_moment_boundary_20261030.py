#!/usr/bin/env python3
"""Author-side exact finite moment-boundary test (not native H0/B0)."""
from fractions import Fraction
from math import comb


def primes_lt(limit):
    sieve = bytearray(b"\x01") * limit
    sieve[:2] = b"\x00\x00"
    for k in range(2, int(limit**0.5)+1):
        if sieve[k]:
            sieve[k*k:limit:k] = b"\x00" * len(sieve[k*k:limit:k])
    return (i for i in range(5,limit) if sieve[i])


def exact_prefix(nmax):
    a = Fraction(1)
    mom = [Fraction(1),Fraction(0),Fraction(0),Fraction(0)]
    for n in range(nmax+1):
        if n:
            a *= Fraction((2*n-1)*(3*n-1)*(3*n-2), 36*n**3)
            for j in range(4): mom[j] += n**j * a
        s0,s1,s2,s3=mom
        defect=18*s3-27*s2-13*s1-2*s0
        expected=-(2*n+1)*(3*n+1)*(3*n+2)*a
        assert defect==expected, (n,defect,expected)
    return True


def prime_check(p):
    m=p**4
    a=1
    s=[1,0,0,0]
    for n in range(1,p):
        a=a*((2*n-1)*(3*n-1)*(3*n-2)) * pow(36*n**3,-1,m)%m
        z=1
        for j in range(4):
            s[j]=(s[j]+z*a)%m
            z=z*n%m
    defect=(18*s[3]-27*s[2]-13*s[1]-2*s[0])%m
    rhs=-(2*p-1)*(3*p-2)*(3*p-1)*a %m
    assert defect==rhs
    assert a%p**3==0
    assert (a//p**3)%p==p-1, (p, a//p**3)
    assert defect==(-2*p**3)%m, (p,defect)
    A=(s[0]+6*s[1])%m
    assert (108*s[3]-162*s[2]+s[0]-13*A)%m==(-12*p**3)%m
    return {"p":p,"defect_over_p3_mod_p":(defect//p**3)%p,"a_last_over_p3_mod_p":(a//p**3)%p,"S0":s[0],"S1":s[1],"S2":s[2],"S3":s[3]}


def original_binomial_check(p):
    mod=p**4
    moments=[0,0,0,0]
    for n in range(p):
        a=comb(2*n,n)**2 * comb(3*n,n)*pow(216,-n,mod)%mod
        z=1
        for j in range(4):
            moments[j]=(moments[j]+z*a)%mod
            z=z*n%mod
    recursive=prime_check(p)
    assert [recursive[f"S{i}"] for i in range(4)] == moments
    return p, recursive["defect_over_p3_mod_p"]


def main():
    assert exact_prefix(12)
    checked = [prime_check(p) for p in primes_lt(5000)]
    target = sum(x["p"]%24 in (13,19) for x in checked)
    independent=[original_binomial_check(p) for p in (5,7,11,13,19,37,373)]
    print("EXACT_N_0_TO_12 13")
    print("PRIMES_5_TO_4999",len(checked))
    print("FROZEN_RESIDUE_CLASSES",target)
    print("INDEPENDENT_ORIGINAL_BINOMIAL",independent)
    print("UNIVERSAL_BOUNDARY_DEFECT mod_p4 = -2*p^3")
    print("P373",next(x for x in checked if x["p"]==373))
    print("PASS_D25_A216_THIRD_MOMENT_BOUNDARY")


if __name__ == "__main__":main()
