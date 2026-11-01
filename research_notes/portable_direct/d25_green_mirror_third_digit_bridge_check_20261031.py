#!/usr/bin/env python3
"""Exact finite check of second-order Green/mirror ratio with a cyclotomic carry port."""
from math import comb
from d25_green_mirror_fermat_bridge_check_20261031 import primes_upto, inv


def qmod(a,p):
    return (pow(a,p-1,p**3)-1)//p


def hmod(l,p,m):
    return sum(inv(k,m) for k in range(1,l+1))%m


def mirror_mod(p,m):
    product=1
    for n,t in ((p-2,1),(p-1,1),(p-3,2)):
        for j in range(1,n+1):
            product=product*(1+t*p*inv(j,m))%m
    return (-2*product*inv((p-1)**2*(p-2)*pow(216,p-1,m),m))%m


def main(limit=3000):
    anchors=[]
    for p in primes_upto(limit):
        l=(p-1)//6
        m2,m3=p*p,p*p*p
        q,Q=qmod(2,p),qmod(216,p)
        A=(hmod(l,p,m2)+hmod(2*l,p,m2))%m2
        B=sum(inv(k*k,p) for k in range(1,l+1))+sum(inv(k*k,p) for k in range(1,2*l+1))
        B%=p
        # p-adic rational 13/2 is evaluated at the declared precision.
        D=(q-13*inv(2,m2))%m2
        cp_numerator=(A-q+Q)%m2
        assert cp_numerator%p==0
        C=cp_numerator//p
        gamma18=((-1)**l*inv(comb(p-1,l)*comb(p-1,2*l),m3))%m3
        M=mirror_mod(p,m3)
        ratio=gamma18*inv(M,m3)%m3
        predicted=(1+p*D+p*p*(C+(q*q-13*q+27+B-Q*Q)*inv(2,p)))%m3
        assert ratio==predicted,(p,ratio,predicted)
        if p in (7,13,19,37,67,283,373):
            b=comb(2*p-2,p-1)**2*comb(3*p-3,p-1)
            assert b%(p**3)==0
            M_orig=(-b//p**3)*inv(pow(216,p-1,m3),m3)%m3
            assert M_orig==M
            anchors.append(dict(p=p,C=C,B=B,D=D%p,gamma18=gamma18,M=M,ratio=ratio,third=((ratio-1-p*D)//(p*p))%p))
    print('PASS_D25_THIRD_DIGIT_GREEN_MIRROR_RATIO',len(primes_upto(limit)),'primes')
    for a in anchors:print('ANCHOR',a)


if __name__=='__main__':
    main()
