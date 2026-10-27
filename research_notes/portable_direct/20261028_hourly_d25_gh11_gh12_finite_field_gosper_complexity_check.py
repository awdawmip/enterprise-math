#!/usr/bin/env python3
"""Exact finite-field rank-window witnesses for D25/GH-11 and GH-12.

Author-level validation only; universal conclusions use the supplied proofs.
No network, non-standard packages, or random sampling.
"""
from math import comb
from fractions import Fraction


def primes_below(limit: int) -> list[int]:
    sieve = bytearray(b'\x01') * limit
    sieve[:2] = b'\x00\x00'
    for q in range(2, int(limit ** .5) + 1):
        if sieve[q]:
            sieve[q*q:limit:q] = b'\x00' * len(sieve[q*q:limit:q])
    return [p for p in range(5, limit) if sieve[p]]


def source_coefficients(p: int, d: int) -> list[int]:
    c = [1]
    for r in range(d):
        a = (9 * (4*r+1)**3) % p
        b = ((4*r+2)*(4*r+3)*(4*r+4)) % p
        assert b != 0 and a != 0, (p,r,a,b)
        c.append(c[-1] * a * pow(b, -1, p) % p)
    assert len(c) == d+1 and all(c)
    return c


def finite_difference(values: list[int], p: int) -> int:
    d = len(values)-1
    return sum(((-1)**(d-k))*comb(d,k)*value
               for k,value in enumerate(values)) % p


def interpolate_degree(values: list[int], p: int) -> int:
    f = values[:]
    degree = -1
    for j in range(len(f)):
        if f[0]:
            degree = j
        f = [(f[k+1]-f[k])%p for k in range(len(f)-1)]
    return degree


def one_prime(p: int) -> dict[str,int]:
    d = (p-1)//4
    c = source_coefficients(p,d)
    S = [0]
    for k in range(d):
        S.append((S[-1]+(8*k+1)*c[k])%p)
    T = (S[-1]+(8*d+1)*c[-1])%p
    c_inv = [pow(x,-1,p) for x in c]
    U = finite_difference([S[k]*c_inv[k]%p for k in range(d+1)],p)
    V = finite_difference(c_inv,p)
    lam = (-U*pow(V,-1,p)) % p if V else 0
    r = [(lam+S[k])*c_inv[k]%p for k in range(d+1)]
    assert (S[-1]+(8*d+1)*c[-1])%p == ((r[-1]+8*d+1)*c[-1]-lam)%p
    for k in range(d):
        assert ((r[k+1]*c[k+1]-r[k]*c[k])-(8*k+1)*c[k])%p==0
    degree=interpolate_degree(r,p)
    if V:
        assert degree<=d-1
    elif U:
        assert degree==d
    else:
        assert degree<=d-1
    return dict(p=p,d=d,U=U,V=V,lambda_=lam,degree=degree,Cd=c[-1],T=T)


def check_exact_rational_source() -> None:
    for r in range(40):
        C0 = Fraction(1)
        for j in range(r):
            C0 *= Fraction(9*(4*j+1)**3,(4*j+2)*(4*j+3)*(4*j+4))
        C1 = Fraction(1)
        for j in range(r+1):
            C1 *= Fraction(9*(4*j+1)**3,(4*j+2)*(4*j+3)*(4*j+4))
        assert C1/C0 == Fraction(9*(4*r+1)**3,(4*r+2)*(4*r+3)*(4*r+4))


def check_polynomial_global_obstruction() -> None:
    # For R(x)=x+11/16, the polynomial defect is
    #  -9(608x²+356x+45)/16, not identically zero over F_p for any p>=5.
    for p in primes_below(5000):
        assert (608%p,356%p,45%p) != (0,0,0)
        for x in (0,1,2,3):
            A = 9*(4*x+1)**3
            B = (4*x+2)*(4*x+3)*(4*x+4)
            R = lambda t: Fraction(t)+Fraction(11,16)
            defect = A*R(x+1)-B*R(x)-B*(8*x+1)
            assert defect == Fraction(-9*(608*x*x+356*x+45),16)


def check_pole_orbits() -> None:
    for p in primes_below(5000):
        d=(p-1)//4
        z=3*pow(4,-1,p)%p
        targets={(-pow(2,-1,p))%p,(-3*pow(4,-1,p))%p,p-1}
        gaps={((end-z)%p) for end in targets}
        assert min(gaps)==d-1, (p,d,z,gaps)


def main() -> None:
    check_exact_rational_source()
    check_polynomial_global_obstruction()
    check_pole_orbits()
    results=[one_prime(p) for p in primes_below(2000)]
    by_p={x['p']:x for x in results}
    for p,values in {
        5:(1,1,0,0,1),
        7:(1,5,4,4,0),
        19:(4,0,0,0,3),
        23:(5,2,11,4,4),
        43:(10,9,2,17,9),
        191:(47,164,0,0,47),
    }.items():
        x=by_p[p]
        assert (x['d'],x['U'],x['V'],x['lambda_'],x['degree'])==values, x
    # A distinct lambda can sharply reduce degree when U=V=0.
    p=19; d=by_p[p]['d']; c=source_coefficients(p,d); S=[0]
    for k in range(d):
        S.append((S[-1]+(8*k+1)*c[k])%p)
    assert [(6+S[k])*pow(c[k],-1,p)%p for k in range(d+1)] == [6]*(d+1)
    for x in results:
        if x['d']>4:
            assert x['degree']>=x['d']-3, x
    print('PASS exact rational source recurrence; polynomial defect; finite-field pole-gap ranks')
    print(f'PASS {len(results)} primes 5<=p<2000: recurrence, finite-window telescope,')
    print('     unique polynomial degree, U/V endpoint coefficients and witness cases')
    print('witnesses:')
    for p in (5,7,19,23,43,191):
        print(by_p[p])
    print(f'T=0 observations: {sum(x["T"]==0 for x in results)} / {len(results)}; finite only')


if __name__=='__main__':
    main()
