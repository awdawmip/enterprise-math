"""Finite exact modular certificate for integer Pfaff first-digit ports (not native CM)."""
from math import isqrt, comb

def primes(n):
    s=bytearray(b'\1')*(n+1)
    s[:2]=b'\0\0'
    for k in range(2,isqrt(n)+1):
        if s[k]:s[k*k:n+1:k]=b'\0'*((n-k*k)//k+1)
    return [p for p in range(7,n+1) if s[p] and p%6==1]

def ports(p):
    m=(p-1)//6
    v=S=1;T=0
    for k in range(1,m+1):
        v=v*(m-k+1)*(2*m+k)*pow(k*k,-1,p)%p
        S=(S+v)%p
        T=(T+k*v)%p
    return S,T

P=primes(10000)
for p in P:
    m=(p-1)//6
    S,T=ports(p)
    assert (S==0) == (p%8 in(3,5)), p
    assert ((S+8*T)%p==0) == (p%8 in(1,7)),p
    if p<500:
        # An independent exact integer sum, not the modular recurrence.
        sint=sum(comb(m,k)*comb(2*m+k,k) for k in range(m+1))
        tint=sum(k*comb(m,k)*comb(2*m+k,k) for k in range(m+1))
        assert (sint%p,tint%p)==(S,T)
print('primes',len(P),'target',sum(p%24 in(13,19) for p in P),'PASS')
print('examples',[(p,*ports(p)) for p in (7,13,19,31,37,43,67,73,373,5113)])
m=14
S=sum(comb(m,k)*comb(2*m+k,k) for k in range(m+1))
print('composite 6m+1=85 m=14 S mod85',S%85)
