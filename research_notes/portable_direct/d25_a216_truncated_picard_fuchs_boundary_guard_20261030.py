"""Exact original-A216 truncated 3F2 differential boundary; author-side only."""
from math import comb


def check(p):
    assert p>=7 and p%6==1
    m=(p-1)//6; N=3*m; M=p**3
    inv2=pow(2,-1,M); inv3=pow(3,-1,M)
    a=1; lhs=0
    for n in range(N+1):
        top=(n+inv2)*(n+inv3)*(n+2*inv3)%M
        lhs=(lhs+(n**3-inv2*top)*a)%M
        if n<N:
            a=a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,M)%M
    endpoint=comb(2*N,N)**2*comb(3*N,N)*pow(216,-N,M)%M
    assert a==endpoint
    assert a%p==0
    rhs=(-p*(9*p*p-1)*a*pow(144,-1,M))%M
    assert lhs==rhs and rhs%(p*p)==0
    chi=1 if pow(6,(p-1)//2,p)==1 else -1
    expected=(-chi*pow(72,-1,p))%p
    assert rhs//(p*p)==expected
    return p,chi,a//p%p,expected


def main():
    primes=[n for n in range(7,1500) if n%6==1 and all(n%d for d in range(2,int(n**0.5)+1))]
    rows=[check(p) for p in primes]
    assert len(rows)==115
    print('PASS exact differential truncation + nonzero p^2 defect for 115 primes p<1500, p=1 mod 6')
    for x in rows:
        if x[0] in (7,13,19,31,37,373): print('p chi aN/p normalized_defect:',*x)

if __name__=='__main__':main()
