#!/usr/bin/env python3
"""R36 author check: p-adic integral lift of the R27/R28 finite Green/adjoint.

Exact modular integer arithmetic on Z/(p^N), with all denominator inversions
restricted to declared p-units. This is author evidence, not native CM/Frobenius.
"""
from fractions import Fraction
from math import factorial, isqrt, gcd


def primes_below(n):
    for x in range(7, n):
        if x % 6 != 1:
            continue
        if all(x % d for d in range(2, isqrt(x) + 1)):
            yield x


def rational_mod(a, mod):
    if not isinstance(a, Fraction):
        a = Fraction(a)
    assert gcd(a.denominator, mod) == 1
    return (a.numerator % mod) * pow(a.denominator % mod, -1, mod) % mod


def poch(x, n):
    result = Fraction(1)
    for k in range(n):
        result *= (x + k)
    return result


def direct_a(r):
    return poch(Fraction(2, 3), r)**3 / (poch(Fraction(7, 6), r) * poch(Fraction(4, 3), r) * factorial(r))


def direct_h(r):
    return poch(Fraction(4, 3), r) * factorial(r) / (poch(Fraction(11, 12), r) * poch(Fraction(17, 12), r))


def plus_minus_mod(p, power=2):
    m = (p - 1) // 6
    mod = p**power
    inv = lambda d: pow(d % mod, -1, mod)
    a, h = [1], [1]
    for r in range(1, m):
        aa = (2 * (3*r - 1)**3 * inv(3*r*(6*r+1)*(3*r+1))) % mod
        hh = (48*r*(3*r+1)*inv((12*r-1)*(12*r+5))) % mod
        a.append(a[-1]*aa%mod)
        h.append(h[-1]*hh%mod)
    C = 3*pow(216, 2*m, mod)*pow(factorial(2*m), 5, mod)*inv(factorial(4*m+1))%mod
    D = 2*pow(2304, 2*m, mod)*pow(factorial(2*m), 4, mod)*inv(factorial(2*m+2))%mod
    # Original W/S source-labelled weighted observer, no changed input.
    v = [(C*(2*r+1)*pow(2,r,mod)
          - D*(24*r+13)*inv(3)*pow(9,r,mod)*h[r])%mod for r in range(m)]
    U = sum(C*(2*r+1)*pow(2,r,mod)*a[r] for r in range(m))%mod
    M = sum(D*(24*r+13)*inv(3)*pow(9,r,mod)*h[r]*a[r] for r in range(m))%mod
    Q = (U - M) % mod
    A = lambda r: r*(6*r+1)*(3*r+1)*inv(18)%mod
    B = lambda r: pow(3*r-1,3,mod)*inv(27)%mod
    c = (-B(m)*a[-1])%mod
    c_lift = a[-1]*inv(8)*pow((1 - p*inv(3))%mod,3,mod)%mod
    assert c==c_lift
    return p,m,mod,a,h,C,D,v,U,M,Q,A,B,c


def check_prime(p):
    p,m,mod,a,h,C,D,v,U,M,Q,A,B,c=plus_minus_mod(p,3)
    inv=lambda x:pow(x%mod,-1,mod)
    def LW(f):
        return [0]+[(A(r)*(f[r] if r<m else 0)-B(r)*f[r-1])%mod for r in range(1,m+1)]
    def LS(f):
        return [0]+[(r*(12*r-1)*(6*r+1)*(12*r+5)*inv(864)*(f[r] if r<m else 0)-r*B(r)*f[r-1])%mod for r in range(1,m+1)]
    fs=[a,[(r*r+7*r+2)%mod for r in range(m)], [(-1)**r*(3*r+2)%mod for r in range(m)]]
    for f in fs:
        g=LW(f)
        hf=[h[r]*f[r]%mod for r in range(m)]
        assert LS(hf)==[0]+[r*h[r-1]*g[r]%mod for r in range(1,m+1)], (p,'intertwiner')
        z=[0]*m
        z[-1]=g[m]*inv(c)%mod
        for r in range(m-1,0,-1):
            z[r-1]=(z[r]-g[r]*inv(A(r)*a[r]))%mod
        rec=[a[r]*z[r]%mod for r in range(m)]
        assert rec == [x%mod for x in f], (p,'Green inverse')
        prefixes=[]
        qsum=0
        for r in range(m):
            qsum=(qsum+v[r]*a[r])%mod
            prefixes.append(qsum)
        assert qsum==Q
        obs=sum(v[r]*f[r] for r in range(m))%mod
        adj=(Q*inv(c)*g[m]-sum(prefixes[t-1]*inv(A(t)*a[t])*g[t] for t in range(1,m)))%mod
        assert obs==adj, (p,'adjoint')
    assert LW(a)[1:m]==[0]*(m-1), (p,'true homogeneous carrier')
    assert LW(a)[m]==c
    if p in (7,13,19,37,43,67,181):
        for r in range(m):
            assert a[r]==rational_mod(direct_a(r),mod)
            assert h[r]==rational_mod(direct_h(r),mod)
        C0=Fraction(3*216**(2*m)*factorial(2*m)**5,factorial(4*m+1))
        D0=Fraction(2*2304**(2*m)*factorial(2*m)**4,factorial(2*m+2))
        U0=C0*sum((2*r+1)*2**r*direct_a(r) for r in range(m))
        M0=D0*sum((Fraction(13,3)+8*r)*9**r*direct_a(r)*direct_h(r) for r in range(m))
        assert U==rational_mod(U0,mod)
        assert M==rational_mod(M0,mod)
    return (p,m,Q%p**2,c%p**2,(Q*inv(c))%p**2,U%p**2,M%p**2)


def run():
    out=[check_prime(p) for p in primes_below(1000)]
    print('PASS: p-adic Z_(p)/p^3 full W/S intertwiner + Green inverse + adjoint')
    print('primes p<1000, p=1 mod6:', len(out))
    print('three deterministic input vectors each prime, both endpoints retained')
    print('direct Fraction cross-check primes 7,13,19,37,43,67,181')
    print('rows (p,m,Q mod p^2,c mod p^2,Q/c mod p^2,U mod p^2,M mod p^2):')
    for row in out:
        if row[0] in (7,13,19,37,43,67,181): print(row)
    row=next(row for row in out if row[0]==37)
    assert row==(37,6,37,678,1258,1056,1019)
    print('p=37 first-digit-safe / second-digit-not-safe certificate: PASS')


if __name__ == '__main__':
    run()
