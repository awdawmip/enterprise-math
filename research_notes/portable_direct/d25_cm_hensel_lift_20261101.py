#!/usr/bin/env python3
"""Author-side D25 p-adic CM Hensel-root displacement certificate.

For p % 24 in (13,19), p > 3, compute F_p(1/9) and its derivative
from exact 1/8,3/8 rising-factorial coefficients, with no floating point.
The p=19 class explicit displacement is a theorem conditional only on
predecessor-proved CM selection, p^2 signed-tail divisibility, and the
published Guo-Zudilin B_p supercongruence. The p=13 zero displacement
is a finite observation / restatement of its OPEN supercongruence.
This is not the original H0/B0 native Frobenius benchmark.
"""
from math import isqrt


def primes(n):
    flag=bytearray(b'\x01')*(n+1)
    flag[:2]=b'\x00\x00'
    for d in range(2,isqrt(n)+1):
        if flag[d]:
            flag[d*d:n+1:d]=b'\x00'*((n-d*d)//d+1)
    return [p for p in range(5,n+1) if flag[p] and p%24 in (13,19)]


def gauss_and_derivative(p,order=2):
    mod=p**order
    t=1; G=0; Z=0
    for k in range(p):
        G=(G+t)%mod
        Z=(Z+k*t)%mod  # Z=z0*F'_p(z0)
        if k+1<p:
            t=t*(8*k+1)*(8*k+3)*pow(576*(k+1)**2,-1,mod)%mod
    return G,Z


def polynomial_value(p,z,order=2):
    mod=p**order
    t=s=1
    for k in range(p-1):
        t=t*(8*k+1)*(8*k+3)*z*pow(64*(k+1)**2,-1,mod)%mod
        s=(s+t)%mod
    return s


def legendre_prime_square_at_t0(p):
    """P_n'(sqrt(8/9))^2 in F_p for p=19 (mod24).
    Use scalar polynomial coeff in s=t^2 by Legendre three-term recurrence
    over F_p[sqrt(s)]; represent (c0+c1*t), t^2=s.
    """
    n=(p-3)//4
    s=8*pow(9,-1,p)%p
    # P0=1, P1=t; recurrence P_(k+1)=((2k+1)t Pk-k P_(k-1))/(k+1).
    pprev=(1,0); pcur=(0,1)
    dprev=(0,0); dcur=(1,0)
    for k in range(1,n):
        inv=pow(k+1,-1,p)
        mult=lambda c:(s*c[1]%p,c[0])
        tt=mult(pcur); dt=mult(dcur)
        pnext=tuple(((2*k+1)*tt[j]-k*pprev[j])*inv%p for j in range(2))
        # derivative of t Pk is Pk + t Pk'
        dnext=tuple(((2*k+1)*(pcur[j]+dt[j])-k*dprev[j])*inv%p for j in range(2))
        pprev,pcur= pcur,pnext
        dprev,dcur= dcur,dnext
    assert pcur[1]==0 and dcur[0]==0, (p,pcur,dcur)
    return (dcur[1]**2*s)%p


def verify(limit=3000):
    rows=[]
    for p in primes(limit):
        m=p*p
        G,Z=gauss_and_derivative(p)
        H=(G+16*Z)%m
        assert G%p==0 and H%p!=0, (p,G,H)
        D=(9*Z)%p
        assert D!=0 and D==(9*H*pow(16,-1,p))%p
        q=G//p
        d=(-q*pow(D,-1,p))%p
        z0=pow(9,-1,m)
        zr=(z0+p*d)%m
        assert polynomial_value(p,z0)==G
        assert polynomial_value(p,zr)==0, (p,d,zr)
        # Check local uniqueness: F(zr+p) = p*D (mod p^2), nonzero.
        assert polynomial_value(p,(zr+p)%m)==p*D%m
        if p%24==19:
            expected= -16*pow(9*pow(H%p,2,p),-1,p)%p
            assert d==expected and d!=0, (p,d,expected)
            legendre_deriv_sq=legendre_prime_square_at_t0(p)
            assert legendre_deriv_sq and d==(-2*pow(legendre_deriv_sq,-1,p))%p
        else:
            assert d==0  # p=13 class: *finite regression*, NOT a universal assertion.
        if p in (13,19,37,43,67,373):
            rec=dict(p=p,G_modp2=G,H_modp=H%p,D_modp=D,d_first=d,
                     z0_modp2=z0,root_modp2=zr)
            if p%24==13:
                G3,_=gauss_and_derivative(p,3)
                assert G3%(p*p)==0
                digit2=(G3//(p*p))%p
                d2=(-digit2*pow(D,-1,p))%p
                z3=pow(9,-1,p**3)
                assert polynomial_value(p,(z3+p*p*d2)%(p**3),3)==0
                rec.update(G_div_p2_modp=digit2,second_root_digit=d2)
            rows.append(rec)
    counts=[sum(p%24==r for p in primes(limit)) for r in (13,19)]
    print('PASS exact finite CM Hensel-root checks',len(primes(limit)),'primes p<=',limit,
          '(p=13mod24,p=19mod24)',counts)
    print('p=19 branch: explicit nonzero first displacement matches two independent formulas')
    print('p=13 branch: first displacement zero is FINITE evidence only')
    for r in rows: print(r)

if __name__=='__main__': verify()
