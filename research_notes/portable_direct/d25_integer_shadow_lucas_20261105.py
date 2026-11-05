#!/usr/bin/env python3
"""Lucas digit-shadow theorem: exact finite base-prime and composite checks."""
from math import comb, isqrt

def primes(bound):
    bits=bytearray([1])*(bound+1)
    bits[0]=bits[1]=0
    for d in range(2,isqrt(bound)+1):
        if bits[d]:
            bits[d*d::d]=bytes((bound-d*d)//d+1)
    return [p for p in range(5,bound+1) if bits[p]]

def weighted_digit(q):
    n0=-pow(6,-1,q)%q
    a,b,c=tuple(t*n0%q for t in (2,3,4))
    s=sum((6*k+1)*(-1)**k*pow(2,-k,q)*comb(a,k)*comb(b,k)*comb(c,k)
          for k in range(min(a,b,c)+1))%q
    return n0,(a,b,c),s

def lucas_factors(n,q):
    a,b,c=2*n,3*n,4*n
    prod=1; level=0
    while a or b or c:
        da,db,dc=a%q,b%q,c%q
        f=0
        for k in range(min(da,db,dc)+1):
            z=(-1)**k*pow(2,-k,q)*comb(da,k)*comb(db,k)*comb(dc,k)
            f=(f+(6*k+1 if level==0 else 1)*z)%q
        prod=prod*f%q
        a//=q; b//=q; c//=q; level+=1
    return prod

def C_mod(n,q):
    return sum((6*k+1)*(-1)**k*pow(2,2*n-k,q)
               *comb(2*n,k)*comb(3*n,k)*comb(4*n,k)
               for k in range(2*n+1))%q

def main():
    pp=primes(1500)
    assert len(pp)==237
    for q in pp:
        assert weighted_digit(q)[2]==0,('lowest-digit',q)
    count=0
    for n in range(1,125):
        for q in pp:
            if (6*n+1)%q==0:
                assert C_mod(n,q)==pow(2,2*n,q)*lucas_factors(n,q)%q==0,(n,q)
                count+=1
    print('PASS',len(pp),'primes q<=1500; Lucas all-n q-adic first digit;',
          count,'direct (n,q) incidence checks')
    for q in (5,7,11,13,17,19,373):
        print(q,weighted_digit(q))

if __name__=='__main__':
    main()
