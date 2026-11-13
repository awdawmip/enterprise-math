#!/usr/bin/env python3
"""Independent exact transcription check of Frid–Jamet 2014 Theorem 1."""
from fractions import Fraction as Q
from math import gcd
from check_r128 import all_patterns


def phi(n):
    return sum(gcd(k,n)==1 for k in range(1,n+1))


def published_count(m):
    """Frid–Jamet Theorem 1, f(n+1) with n=m-1>=3."""
    n=m-1
    def tot(t):
        return sum(phi(p) for p in range(1,t+1))
    if n%2:
        k=(n-1)//2
        f1=2*sum(tot(i+1) for i in range(k,2*k+1))
    else:
        k=n//2
        f1=2*sum(tot(i+1) for i in range(k,2*k))+tot(k)
    def f2(l):
        g=n-l+1+n%(l+1)
        h=min(l+1,n-l)
        return (Q((n//(l+1))*g,2)-h)*(phi(l+1)-1)+h*(Q(phi(l+1),2)-1)
    result=(n*n+3*n+4
        + Q(sum(phi(p)*(n*n-p*p+n+p) for p in range(3,n+1)),2)
        - f1 - 2*sum(f2(l) for l in range(2,n)))
    assert result.denominator==1
    return int(result)


def main():
    for m in range(4,14):
        assert published_count(m)==len(all_patterns(m)),m
    paper={6:64,7:112,10:504,15:2804,20:9442,30:51306,
           50:423814,75:2222984,100:7155096}
    for m,expected in paper.items():
        assert published_count(m)==expected,(m,published_count(m),expected)
    print("R128_FRID_JAMET_FORMULA_CROSSCHECK_PASS",10,len(paper))


if __name__=="__main__":
    main()
