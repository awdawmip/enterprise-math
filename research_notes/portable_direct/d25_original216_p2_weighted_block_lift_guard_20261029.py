#!/usr/bin/env python3
"""Exact original-216 p^2 block lift; NOT the D25 native H0/B0 experiment."""
from math import comb, isqrt


def primes_below(limit):
    return [p for p in range(5, limit) if all(p % d for d in range(2, isqrt(p)+1))]


def orig_a(n, p):
    M=p*p
    return comb(2*n,n)**2 * comb(3*n,n) * pow(216,-n,M) % M


def d_digit(p,r):
    D=0
    for j in range(r):
        D=(D+2*pow(2*j+1,-1,p)+3*pow(3*j+1,-1,p)
             +3*pow(3*j+2,-1,p)-3*pow(j+1,-1,p)) % p
    return D


def q216(p):
    residue=pow(216,p-1,p*p)
    assert residue%p==1
    return (residue-1)//p


def check(p,u,r):
    assert 0<=r<=(p-1)//3
    M=p*p
    ar=orig_a(r,p); au=orig_a(u,p)
    d=d_digit(p,r); q=q216(p)
    pred=au*ar*(1+p*u*(d-q))%M
    direct=orig_a(p*u+r,p)
    assert pred==direct,(p,u,r,pred,direct,d,q)
    w_pred=(au*ar*((6*r+1)+p*u*(6+(6*r+1)*(d-q))))%M
    w_direct=((6*(p*u+r)+1)*direct)%M
    assert w_pred==w_direct,(p,u,r,w_pred,w_direct)
    return pred


def main():
    primes=primes_below(220)
    tests=0
    for p in primes:
        for u in range(5):
            for r in range((p-1)//3+1):
                check(p,u,r)
                tests+=1
        # Pure binomial polynomial proof precursor, verified independently.
        for a in range(1,8):
            for b in range(a+1):
                assert comb(a*p,b*p)% (p*p)==comb(a,b)%(p*p),(p,a,b)
    p=373
    proof={}
    for u,r in ((1,0),(1,1),(1,62),(2,62),(3,62),(4,124)):
        if r<=(p-1)//3:
            val=check(p,u,r)
            proof[f'{u},{r}']={'a':val,'w':(6*(p*u+r)+1)*val%(p*p),'D_r':d_digit(p,r)}
            tests+=1
    print('PASS_A216_FIRST_ORDER_P2_WEIGHTED_DWORK_BLOCK_LIFT',tests,'instances',len(primes),'primes p<220 and p373')
    print('PASS_BINOM_AP_BP_MOD_P2',sum((a+1) for a in range(1,8))*len(primes),'combinations')
    print('P373_FERMAT_QUOTIENT_216',q216(373))
    print('P373_WEIGHTED_WITNESSES',proof)


if __name__ == '__main__':
    main()
