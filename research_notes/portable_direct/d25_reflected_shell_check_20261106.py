#!/usr/bin/env python3
"""D25 exact integer modular original-216 third-shell reflection; author-only."""
from math import isqrt

def primes_to(limit):
    s=bytearray(b'\x01')*(limit+1);s[:2]=b'\x00\x00'
    for i in range(2,isqrt(limit)+1):
        if s[i]:s[i*i::i]=b'\x00'*(((limit-i*i)//i)+1)
    return [p for p in range(7,limit+1) if s[p] and p%6==1]

def compute(p):
    m=(p-1)//6; modulus=p**3
    # Original coefficients via exact p-adic unit denominator recurrence.
    a=1; shell=0; first=None; naive=[]
    for k in range(4*m+1):
        if k==4*m: first=a//(p*p) % p
        if 3*m<k<=4*m:
            assert a%(p*p)==0 and a%modulus!=0,(p,k,'valuation')
            shell=(shell+(6*k+1)*a//(p*p))%p
            naive.append((k,a//(p*p)%p))
        if k<4*m:
            n=k+1
            a=a*(2*n-1)*(3*n-2)*(3*n-1)*pow(36*n**3,-1,modulus)%modulus
    # Wilson-calibrated original last coefficient.
    fac=[1]*p
    for k in range(1,p):fac[k]=fac[k-1]*k%p
    # Separate factorial p-extraction, independent of the p^3 recurrence.
    for k,norm in naive:
        direct=fac[2*k-p]*fac[3*k-p]*pow(pow(216,k,p)*pow(fac[k],5,p)%p,-1,p)%p
        assert direct==norm,(p,k,direct,norm)
    c1=fac[2*m-1]*pow(pow(216,4*m,p)*pow(fac[4*m],5,p)%p,-1,p)%p
    assert c1==first,(p,c1,first)
    c=c1; reflected=(3-6)*c %p; all_norm=[c]
    for j in range(1,m):
        num=4*pow(3*j-1,3,p)
        den=3*j*(6*j+1)*(3*j+1)
        c=c*num*pow(den,-1,p)%p
        reflected=(reflected+(3-6*(j+1))*c)%p
        all_norm.append(c)
    assert reflected==shell,(p,reflected,shell)
    assert [naive[m-1-i][1] for i in range(m)]==all_norm,(p,'term mismatch')
    return (p,m,c1,reflected)

if __name__ == '__main__':
    data=[compute(p) for p in primes_to(1999)]
    assert len(data)==148,len(data)
    data.extend([compute(5113)])
    print('ALL_PASS',len(data), 'reflected_coefficient_checks', sum(m for _,m,_,_ in data))
    for x in data:
        if x[0] in (7,13,19,67,373,5113):print(x)
