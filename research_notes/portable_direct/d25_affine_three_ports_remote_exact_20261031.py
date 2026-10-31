#!/usr/bin/env python3
"""Independent finite regression for D25 exact I3/I4 p^4 port formulas.
The universal proofs are in the companion note. Native H0/B0 NOT executed.
"""
from math import comb, isqrt


def primes(n=1200):
    f = [True]*(n+1)
    f[0] = f[1] = False
    for j in range(2, isqrt(n)+1):
        if f[j]:
            f[j*j::j] = [False]*((n-j*j)//j+1)
    return [p for p in range(5,n+1) if f[p]]


def test(p):
    m2, m4 = p*p, p**4
    fac = [1]*p
    H = [0]*p
    for k in range(1,p):
        fac[k] = fac[k-1]*k % m2
        H[k] = (H[k-1]+pow(k,-1,p))%p
    W = ((fac[-1]+1)//p)%p
    inv216 = pow(216,-1,m2)
    inv2304 = pow(2304,-1,m2)
    a = b = 1
    acc = [[0,0] for _ in range(2)]
    raw = [[0,0] for _ in range(2)]
    n3=n4=0
    for k in range(p):
        region = 3 if (2*k>=p and 3*k<2*p) else 4 if (3*k>=2*p and 4*k<3*p) else None
        if region is not None:
            x = region-3
            if region == 3:
                s2,s3,s4=2*k-p,3*k-p,4*k-2*p
                A = fac[s2]*fac[s3]*pow(fac[k],-5,m2)*pow(inv216,k,m2)%m2
                A = A*(1+p*(H[s2]+H[s3]-2*W))%m2
                B = 2*fac[s4]*pow(fac[k],-4,m2)*pow(inv2304,k,m2)%m2
                B = B*(1+2*p*(H[s4]-W))%m2
                assert a == p*p*A % m4 and b == p*p*B % m4
                acc[x][0] = (acc[x][0]+(6*k+1)*p*p*A)%m4
                acc[x][1] = (acc[x][1]+(8*k+1)*p*p*B)%m4
                n3 += 1
            else:
                r2,r3,r4=2*k-p,3*k-2*p,4*k-2*p
                Y = -2*fac[r2]*fac[r3]*pow(fac[k],-5,p)*pow(216,-k,p)%p
                X = 2*fac[r4]*pow(fac[k],-4,m2)*pow(inv2304,k,m2)%m2
                X = X*(1+2*p*(H[r4]-W))%m2
                assert a == p**3*Y % m4 and b == p*p*X % m4
                acc[x][0] = (acc[x][0]+(6*k+1)*p**3*Y)%m4
                acc[x][1] = (acc[x][1]+(8*k+1)*p*p*X)%m4
                n4 += 1
            raw[x][0] = (raw[x][0]+(6*k+1)*a)%m4
            raw[x][1] = (raw[x][1]+(8*k+1)*b)%m4
        if k+1<p:
            h = pow(k+1,-3,m4)
            a = a*(2*k+1)*(3*k+1)*(3*k+2)*pow(36,-1,m4)*h%m4
            b = b*(4*k+1)*(2*k+1)*(4*k+3)*pow(288,-1,m4)*h%m4
    assert acc == raw
    if p in (5,7,11,13,19,37,67,373):
        for x in (0,1):
            A=B=0
            for k in range(p):
                region = 3 if 2*k>=p and 3*k<2*p else 4 if 3*k>=2*p and 4*k<3*p else None
                if region != x+3:
                    continue
                A += (6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,m4)
                B += (8*k+1)*comb(4*k,2*k)*comb(2*k,k)**2*pow(2304,-k,m4)
            assert (A%m4,B%m4)==tuple(raw[x])
    return n3,n4,[(z[0]-2*z[1])%m4 for z in raw]


def main():
    ps=primes()
    n3=n4=0
    marks={}
    for p in ps:
        x,y,d=test(p)
        n3+=x
        n4+=y
        if p in (13,19,67,373):
            marks[p]=d
    print('PASS_D25_HARMONIC_THREE_UPPER_PORTS',len(ps),n3,n4,marks)
    print('FINITE REGRESSION ONLY; AFFINE UNIVERSAL PROOF OPEN; NATIVE NOT RUN')


if __name__=='__main__':
    main()
