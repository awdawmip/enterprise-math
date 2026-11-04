#!/usr/bin/env python3
"""Independent [X^(p+1)] Sun truncation defect, 216/2304, exact p^3."""
from math import comb

def prime(p): return p>=5 and all(p%d for d in range(2,int(p**.5)+1))

def check(p,d):
    m=p**3;den={3:27,4:64}[d]
    c=[comb(2*k,k)*comb(d*k,(d-2)*k)*pow(den,-k,m)%m for k in range(p)]
    j=p+1
    f2=sum(c[i]*c[j-i] for i in range(2,p))%m
    hh=sum(((-1)**(j-k))*comb(k,j-k)*comb(2*k,k)*c[k]
        for k in range((j+1)//2,p))%m
    defect=(f2-hh)%m
    assert defect%p**2==0
    observed=defect//p**2
    predicted=(4*pow(27,-1,p) if d==3 else 21*pow(128,-1,p))%p
    assert observed==predicted,(p,d,observed,predicted)
    return observed
if __name__=='__main__':
    result=[(p,check(p,3),check(p,4)) for p in range(5,1001) if prime(p)]
    print('primes=',len(result),'checks=',2*len(result),'failures=0')
    for row in result:
        if row[0] in (5,7,11,13,19,97,373,997): print(row)
