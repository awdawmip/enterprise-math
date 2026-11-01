#!/usr/bin/env python3
"""Check the exact 2304 Clausen first-boundary coefficient modulo p²."""
from math import isqrt
def primes(n):
    a=bytearray(b'\1')*(n+1);a[:2]=b'\0\0'
    for d in range(2,isqrt(n)+1):
        if a[d]:a[d*d:n+1:d]=b'\0'*((n-d*d)//d+1)
    return [p for p in range(5,n+1) if a[p]]
def coeff(p,exp=2):
    m=p**exp
    f=[1]
    for k in range(p-1):
        f.append(f[-1]*(8*k+1)*(8*k+3)*pow(64*(k+1)**2,-1,m)%m)
    return f
by8={}
ps=primes(3000)
for p in ps:
    f=coeff(p,2)
    val=sum(f[i]*f[p-i] for i in range(1,p))%p**2
    expected=0 if p%8 in (1,3) else p-1
    assert val%p==expected,(p,val,expected)
    by8[p%8]=by8.get(p%8,0)+1
    if p%8==3 and p<=200:
        for n in range(p,2*p-1):
            actual=sum(f[i]*f[n-i] for i in range(n-(p-1),p))%p**2
            assert actual==0,(p,n,actual)
for p in (5,7,11,13,19,37,43,61,109,373):
    f=coeff(p,3)
    val=sum(f[i]*f[p-i] for i in range(1,p))%p**3
    print('sample',p,'class',p%8,'first_cutoff_mod_p3',val,'modp',val%p)
print('PASS',len(ps),'primes through 3000',dict(sorted(by8.items())))
