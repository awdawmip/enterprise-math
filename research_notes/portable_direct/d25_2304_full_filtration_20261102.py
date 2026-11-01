#!/usr/bin/env python3
"""Independent all-index p-adic filtration check for weighted 2304 summands."""
from math import isqrt

def primes_upto(n):
    a=bytearray(b'\x01')*(n+1)
    a[:2]=b'\x00\x00'
    for x in range(2,isqrt(n)+1):
        if a[x]:
            a[x*x:n+1:x]=b'\x00'*(((n-x*x)//x)+1)
    return [p for p in range(5,n+1) if a[p]]

def check_one(p):
    modulus=p**7
    a=1
    exceptional=[]
    total_terms=0
    truncated=0
    for k in range(p):
        weight=8*k+1
        w=weight
        weight_v=0
        while w%p==0:
            weight_v+=1
            w//=p
        predicted=(4*k)//p+weight_v
        t=(weight*a)%modulus
        assert t % (p**predicted)==0
        assert t % (p**(predicted+1))!=0, (p,k,predicted)
        if weight_v:
            exceptional.append((k,weight_v,predicted))
        if 4*k>=3*p:
            assert t%(p**3)==0
            truncated+=1
        total_terms+=1
        if k+1<p:
            a=(a* ((4*k+1)*(4*k+2)*(4*k+3)*(4*k+4)))%modulus
            a=(a*pow(2304*(k+1)**4,-1,modulus))%modulus
    assert len(exceptional)==1
    return exceptional[0],total_terms,truncated

if __name__=='__main__':
    ps=primes_upto(997)
    records=[(p,*check_one(p)) for p in ps]
    print('PRIMES=',len(records),'ALL_TERMS_CHECKED=',sum(x[2] for x in records))
    print('HIGH_TERMS_VANISH_P3=',sum(x[3] for x in records))
    print('EXAMPLES=',[(p,x) for p,x,_,_ in records if p in (5,7,13,19,37,43,373)])
    print('PASS_ALL_INDEX_EXACT_FILTRATION=True')
