#!/usr/bin/env python3
"""Independent modular p^3 certificate: terminating integer-shadow jets.
No native CM/H0/B0 experiment. Integer modular inverses only.
"""
from math import comb, isqrt

def primes(bound):
    flags=bytearray([1])*(bound+1)
    flags[0]=flags[1]=0
    for d in range(2,isqrt(bound)+1):
        if flags[d]:
            flags[d*d::d]=b'\\0'*((bound-d*d)//d+1)
    return [p for p in range(7,bound+1) if flags[p] and p%6==1]

def row(p):
    n=(p-1)//6; M=p**3
    inv2=pow(2,-1,M); inv3=pow(3,-1,M)
    ms=(3*n,2*n,4*n); betas=(inv2,inv3,2*inv3%M)
    u=1; valuation=0; h1=h2=0
    S=A=B=0
    for k in range(p):
        weight=6*k+1
        if valuation==0:
            S=(S+weight*u)%M
            A=(A+weight*u*h1)%M
            B=(B+weight*u*(h1*h1-h2)*inv2)%M
        elif valuation==1:
            A=(A+weight*u)%M
            B=(B+weight*u*h1)%M
        elif valuation==2:
            B=(B+weight*u)%M
        if k==p-1:
            break
        multiplier=pow(2*(k+1)**3,-1,M)
        for m,beta in zip(ms,betas):
            r=k-m
            if r==0:
                valuation+=1
                multiplier=multiplier*beta%M
            else:
                multiplier=multiplier*r%M
                z=beta*pow(r,-1,M)%M
                h1=(h1+z)%M
                h2=(h2+z*z)%M
        u=u*multiplier%M
    C=sum((6*k+1)*(-1)**k*2**(2*n-k)*comb(2*n,k)
          *comb(3*n,k)*comb(4*n,k) for k in range(2*n+1))
    assert S == C*pow(2,-2*n,M)%M, (p,'shadow')
    a=total=1
    for k in range(1,p):
        j=k-1
        a=a*(2*j+1)*(3*j+1)*(3*j+2)*pow(36*k**3,-1,M)%M
        total=(total+(6*k+1)*a)%M
    assert total==(S+p*A+p*p*B)%M, (p,'two-jet')
    assert total%p**2==p and C%p==0, (p,'first-digit')
    carry=(S+p*A-p)%M
    assert carry%p**2==0, (p,'carry-divisibility')
    carry=carry//p**2
    assert (carry+B)%p==((total-p)//p**2)%p, (p,'residual')
    return S,A%p**2,B%p,carry%p,total

def main():
    pp=primes(1200)
    assert len(pp)==94, len(pp)
    for p in pp:
        result=row(p)
        assert result[-1]==p, (p,'finite-W')
    print('PASS',len(pp),'primes 7<=p<=1200, p=1 mod6; exact shadow/two-jet/residual checks')
    for p in (13,19,373):
        print('p=',p,'(S,A mod p^2,B mod p,carry,W)=',row(p))

if __name__=='__main__':
    main()
