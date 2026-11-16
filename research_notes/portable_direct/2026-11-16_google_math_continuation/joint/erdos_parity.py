"""Exact CRT densities and independent checks of reflection and parity for #1063."""
from collections import Counter
from fractions import Fraction
from itertools import count
from math import comb, factorial, isqrt, lcm
import json


def period(k):
    return lcm(*range(1,k+1))*lcm(*range(1,k//2+1))


def primes(k):
    return [p for p in range(2,k+1) if all(p%d for d in range(2,isqrt(p)+1))]


def valuation(n,p):
    assert n>0
    e=0
    while n%p==0:
        n//=p
        e+=1
    return e


def count_positions(k):
    full=period(k)
    columns=[1]*k
    empty=1
    for p in primes(k):
        q=p**valuation(full,p)
        base=((2*k+q-1)//q)*q
        values=[valuation(n,p) for n in range(base-k+1,base+q)]
        a=valuation(factorial(k),p)
        h=Counter()
        for j in range(q):
            window=values[j:j+k]
            extra=sum(window)-a
            failed=[i for i,x in enumerate(reversed(window)) if x>extra]
            if len(failed)<=1:
                h[failed[0] if failed else None]+=1
        columns=[x*(h[None]+h[i]) for i,x in enumerate(columns)]
        empty*=h[None]
    return [value-empty for value in columns]


def exceptional(n,k):
    b=comb(n,k)
    return [i for i in range(k) if b%(n-i)]


def power_of_two(x):
    return x>0 and x&(x-1)==0


def run():
    demo={}
    for k in range(2,129):
        p=period(k)
        cols=count_positions(k)
        assert cols==cols[::-1]
        assert sum(cols)%2 == (k>=7 and power_of_two(k+1))
        if k%2:
            m=k//2
            centers=[m,m+p//2]
            for j,a in enumerate(centers):
                n=a+p*((max(0,2*k-a)+p-1)//p)
                expected=[m]
                if j and k>=7 and power_of_two(k+1):
                    step=(k+1)//4
                    expected=[m-step,m,m+step]
                assert exceptional(n,k)==expected
        if k<=10:
            direct=[0]*k
            for n in range(2*k,2*k+p):
                f=exceptional(n,k)
                if len(f)==1:direct[f[0]]+=1
            assert cols==direct
        if k in [3,5,7,8,9,15,31,63]:
            demo[str(k)]=dict(period=p,count=sum(cols),density=str(Fraction(sum(cols),p)))
    print(json.dumps(demo,indent=2))


if __name__=='__main__':
    run()
