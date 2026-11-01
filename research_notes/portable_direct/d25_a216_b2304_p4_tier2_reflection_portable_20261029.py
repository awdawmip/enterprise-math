#!/usr/bin/env python3
"""Exact independent finite guard for the proved A216/B2304 p^4 valuation-two jets."""
from math import comb


def primes(bound):
    z = bytearray(b'\x01') * bound
    z[:2] = b'\x00\x00'
    for d in range(2, int(bound**.5)+1):
        if z[d]:
            z[d*d:bound:d] = b'\x00'*((bound-1-d*d)//d+1)
    return (p for p in range(5,bound) if z[p])


def test_prime(p):
    M, m = p**4, p**2
    f = [1]*p
    H = [0]*p
    for n in range(1,p):
        f[n] = f[n-1]*n % m
        H[n] = (H[n-1]+pow(n,-1,p))%p
    fi = [0]*p
    fi[-1] = pow(f[-1],-1,m)
    for n in range(p-1,0,-1):
        fi[n-1] = fi[n]*n % m
    assert (f[-1]+1)%p==0
    W = ((f[-1]+1)//p)%p
    qa = ((pow(216,p-1,m)-1)//p)%p
    qb = ((pow(2304,p-1,m)-1)//p)%p
    a = b = 1
    A2 = B2 = count = 0
    for n in range(p):
        r = p-1-n
        if (2*n)//p+(3*n)//p==2:
            t2,t3 = 2*r+1,3*r+2-p
            s2,s3 = 2*n-p,3*n-p
            C = pow(216,r,m)*pow(f[r],5,m)*fi[t2]*fi[t3]%m
            J = (H[t2]+H[t3]+H[s2]+H[s3]-5*H[r]+W-qa)%p
            pred = C*((6*r+5)+p*((6*r+5)*J-6))%m
            orig = ((6*n+1)*a%M)//p**2
            assert pred==orig, ('A',p,n,pred,orig)
            A2 = (A2+pred)%m
            count+=1
        if (4*n)//p==2:
            t,s = 4*r+3-p,4*n-2*p
            C = 2*pow(2304,r,m)*pow(f[r],4,m)*fi[t]%m
            J = (H[t]+2*H[s]-4*H[r]+W-qb)%p
            pred = C*((8*r+7)+p*((8*r+7)*J-8))%m
            orig = ((8*n+1)*b%M)//p**2
            assert pred==orig, ('B',p,n,pred,orig)
            B2 = (B2+pred)%m
            count+=1
        if p in (5,7,11,13,19,31,373):
            ar = comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,M)%M
            br = comb(2*n,n)**2*comb(4*n,2*n)*pow(2304,-n,M)%M
            assert (a,b)==(ar,br), ('RAW',p,n)
        if n+1<p:
            k = n+1
            inv3=pow(pow(k,-1,M),3,M)
            a=a*(2*k-1)*(3*k-2)*(3*k-1)*inv3*pow(36,-1,M)%M
            b=b*(2*k-1)*(4*k-3)*(4*k-1)*inv3*pow(288,-1,M)%M
    return count,A2,B2


if __name__=='__main__':
    ps=list(primes(1500))
    total=0
    for p in ps:
        count,A2,B2=test_prime(p)
        total+=count
        if p in (13,19,373):
            print('SOURCE',p,'A2/p2',A2,'B2/p2',B2,'Q', (A2-2*B2)%(p*p))
    assert len(ps)==237 and total==68767
    print('PASS',len(ps),'primes; exact weighted terms',total)
