#!/usr/bin/env python3
"""Author's exact finite-field certificate for D25/LIFT R53/R54.

Source: original W/S factorial terms and R47 exact first-order transitions.
All observations are over F_p; symbolic proof establishes the infinite family.
"""
from fractions import Fraction

P = lambda x: 2688*x**4 + 6160*x**3 + 4456*x**2 + 1166*x + 85

def prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5) + 1))

def inv(a, p):
    assert a % p
    return pow(a, -1, p)

def qmod(x, p):
    if isinstance(x, Fraction):
        return (x.numerator % p) * inv(x.denominator, p) % p
    return x % p

def a(k):
    return Fraction((6*k+7)*(2*k+1)*(3*k+1)*(3*k+2),36*(6*k+1)*(k+1)**3)

def b(k):
    return Fraction((8*k+9)*(2*k+1)*(4*k+1)*(4*k+3),288*(8*k+1)*(k+1)**3)

def fact_unit_mod_p(n, p):
    z = 1
    v = 0
    for j in range(1, n+1):
        while j % p == 0:
            j //= p
            v += 1
        z = z * j % p
    return z, v

def normalized_w_s(k, p):
    # Original rational w_k/p^3, s_k/p^3 modulo p, without big factorials.
    f1, v1 = fact_unit_mod_p(k, p)
    f2, v2 = fact_unit_mod_p(2*k, p)
    f3, v3 = fact_unit_mod_p(3*k, p)
    f4, v4 = fact_unit_mod_p(4*k, p)
    assert v2 + v3 - 5*v1 == 3
    assert v4 - 4*v1 == 3
    w = (6*k+1)*f2*f3*inv(pow(f1,5,p)*pow(216,k,p),p)%p
    s = (8*k+1)*f4*inv(pow(f1,4,p)*pow(2304,k,p),p)%p
    assert w and s
    return w,s

def check(p):
    assert p>=13 and p%6==1 and prime(p)
    N=(3*p-1)//4+1
    assert N+2 < p
    da=qmod(a(N)-b(N),p)
    dn=qmod(a(N+1)-b(N+1),p)
    exceptional=p in (139,199,277)
    assert (da==0)==exceptional, (p,N,da)
    assert dn != 0, (p,N,dn)
    Ws=[normalized_w_s(k,p) for k in (N,N+1,N+2)]
    xs=[(w-s)%p for w,s in Ws]
    aa,bb=qmod(a(N),p),qmod(b(N),p)
    aa1,bb1=qmod(a(N+1),p),qmod(b(N+1),p)
    assert Ws[1][0]==aa*Ws[0][0]%p and Ws[1][1]==bb*Ws[0][1]%p
    assert Ws[2][0]==aa1*Ws[1][0]%p and Ws[2][1]==bb1*Ws[1][1]%p
    w1=qmod(Fraction(7,18),p)
    s1=qmod(Fraction(3,32),p)
    A=Ws[1][0]*inv(w1,p)%p
    B=Ws[1][1]*inv(s1,p)%p
    # R53: shift a single rank; the next two raw high-high endpoints recover sources.
    C1=(aa1*inv(B,p)-bb1*inv(A,p))*inv(dn,p)%p
    C2=(inv(A,p)-inv(B,p))*inv(dn,p)%p
    assert (C1*xs[1]+C2*xs[2])%p==(w1-s1)%p
    assert C1 or C2
    U=(xs[2]-bb1*xs[1])*inv(dn*A,p)%p
    V=(xs[2]-aa1*xs[1])*inv(dn*B,p)%p
    assert (U,V)==(w1,s1),(p,N,U,V,w1,s1)
    if exceptional:
        W0,S0=Ws[0]
        A0=W0*inv(w1,p)%p
        B0=S0*inv(s1,p)%p
        # R54: kernel of first observer at the singular rank.
        h=(B0,A0)
        assert (A0*h[0]-B0*h[1])%p==0
        assert (aa*A0*h[0]-bb*B0*h[1])%p==0
        assert (h[0]-h[1])%p != 0
        assert (aa1*A*h[0]-bb1*B*h[1])%p != 0
    return (p,N,da,dn,*xs,C1,C2)

if __name__ == '__main__':
    assert P(Fraction(1,4)) == Fraction(11*277,4)
    assert P(Fraction(3,4)) == Fraction(139*199,4)
    assert P(Fraction(5,4)) == Fraction(5*7*19*163,4)
    assert P(Fraction(7,4)) == Fraction(5*59197,4)
    assert all(prime(q) for q in (5,7,19,163,59197))
    primes=[p for p in range(13,1000) if p%6==1 and prime(p)]
    rows=[check(p) for p in primes]
    print('Target primes checked:',len(rows))
    print('Degenerate first window:',[(p,N) for p,N,da,*_ in rows if da==0])
    print('Shifted first-order differences units:',len(rows))
    print('Exceptional exact certificates (p,N,D_N mod p,D_{N+1} mod p,x_N,x_{N+1},x_{N+2},p^3 Q_{N+1} mod p,p^3 Q_{N+2} mod p):')
    for row in rows:
        if row[0] in (139,199,277):
            print(row)
    assert len(rows)==79
    assert len([r for r in rows if r[2]==0])==3
    print('PASS')
