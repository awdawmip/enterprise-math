#!/usr/bin/env python3
"""Exact independent checks for a corrected-Clausen six-Hasse local-rank obstruction.

Author-only algebraic/finite-ring evidence; not native CM/Frobenius or Source admission.
No third-party runtime dependencies.
"""
from fractions import Fraction as F
from math import factorial, gcd, isqrt

PAIRS = ((0, 2), (1, 2), (0, 3), (2, 2), (1, 3), (0, 4))


def mul(x, y):
    return [sum(x[i] * y[k-i] for i in range(k+1)) for k in range(3)]


def times(x, c, d):
    return mul(x, [c, d, F(0)])


def over(x, c, d):
    assert c
    return mul(x, [1/c, -d/c**2, d**2/c**3])


def rational_low(j):
    a = [F(1), F(0), F(0)]
    for k in range(j):
        a = times(a, F(k)+F(1,6), F(-1))
        a = times(a, F(k)+F(1,3), F(-2))
        a = over(a, F(k+1), F(-3))
    return [v/factorial(j) for v in a]


def rational_high(ell):
    a = [F(2*factorial(ell-1)), F(0), F(0)]
    for i in range(1,ell):
        a = times(a, F(i), F(3))
    for i in range(1,ell+1):
        a = over(a, F(1,6)-i, F(-1))
        a = over(a, F(1,3)-i, F(-2))
    return a


def det3(a):
    x, y, z = a
    return (x[0]*(y[1]*z[2]-y[2]*z[1])
            -x[1]*(y[0]*z[2]-y[2]*z[0])
            +x[2]*(y[0]*z[1]-y[1]*z[0]))


def modfrac(x, p):
    assert gcd(x.denominator, p) == 1
    return x.numerator * pow(x.denominator, -1, p) % p


def jets_mod_p(p):
    assert p >= 7 and p % 6 == 1
    m=(p-1)//6
    u=[[0]*p for _ in range(5)]
    u[0][0]=1
    for r in range(1,p):
        d=pow(r*r,-1,p)
        for a in range(5):
            v=(r-1-m)*(r-1-2*m)*u[a][r-1]
            if a:
                v+=3*r*u[a-1][r]-(3*(r-1)-4*m)*u[a-1][r-1]
            if a>=2:
                v+=2*u[a-2][r-1]
            u[a][r]=v*d%p
    return u


def rank_mod(a,p):
    a=[[v%p for v in row] for row in a]
    row=0
    for c in range(len(a[0])):
        pivot=next((r for r in range(row,len(a)) if a[r][c]),None)
        if pivot is None:
            continue
        a[row],a[pivot]=a[pivot],a[row]
        inverse=pow(a[row][c],-1,p)
        a[row]=[v*inverse%p for v in a[row]]
        for r in range(len(a)):
            if r != row and a[r][c]:
                factor=a[r][c]
                a[r]=[(v-factor*w)%p for v,w in zip(a[r],a[row])]
        row+=1
        if row == len(a):
            break
    return row


def primes(limit):
    return [p for p in range(13,limit+1) if p%6 == 1 and
            all(p%d for d in range(2,isqrt(p)+1))]


def main():
    L=[rational_low(j) for j in range(1,5)]
    H=[rational_high(ell) for ell in range(1,5)]
    DL1,DL2=det3(L[:3]),det3([L[0],L[1],L[3]])
    DH1,DH2=det3(H[:3]),det3([H[0],H[1],H[3]])
    assert (DL1,DL2)==(F(-223,51018336),F(-590771,117546246144))
    assert (DH1,DH2)==(F(235924728894,102175046875),
                       F(176774596383358548,71941348329640625))
    assert gcd(223,590771)==1 and gcd(8221,114071533)==1
    checked=primes(997)+[8221]
    for p in checked:
        u=jets_mod_p(p)
        for j in range(1,5):
            assert [u[a][j] for a in range(3)] == [modfrac(v,p) for v in L[j-1]], (p,j,'L')
        for ell in range(1,5):
            assert [u[b][p-ell] for b in range(2,5)] == [modfrac(v,p) for v in H[ell-1]], (p,ell,'H')
        assert (modfrac(DL1,p)!=0 or modfrac(DL2,p)!=0),p
        assert (modfrac(DH1,p)!=0 or modfrac(DH2,p)!=0),p
        cells=[[u[a][j]*u[b][p-ell]%p for a,b in PAIRS]
               for j in range(1,5) for ell in range(1,5)]
        assert rank_mod(cells,p)==6, (p,'six-channel-rank')
    u=jets_mod_p(7)
    p7=[[u[a][j]*u[b][7-ell]%7 for a,b in PAIRS]
        for j in (1,2) for ell in (1,2)]
    assert rank_mod(p7,7)==4
    assert modfrac(DL1,223)==0 and modfrac(DL2,223)!=0
    assert modfrac(DH1,8221)==0 and modfrac(DH2,8221)!=0
    print('PASS rational minors and gcds; p>=13 theorem, all primes 6m+1')
    print('PASS exact finite-field jets and tensor rank 6:', len(checked),
          'primes (13..997 and 8221), including 223, 733, 8221')
    print('p=7 exceptional small window: rank',rank_mod(p7,7),'<6')
    print('minor pair L:',DL1,DL2,'; H:',DH1,DH2)


if __name__=='__main__':
    main()
