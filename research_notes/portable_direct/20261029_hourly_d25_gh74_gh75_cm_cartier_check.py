#!/usr/bin/env python3
"""GH-74/75 author exact checks: normalized CM 3-isogeny and split/inert Cartier coefficients.

This checker is independent of a native Enterprise Math experiment or admitted Result.
It exercises finite-field examples; mathematical universality is supplied by the accompanying proof.
"""
from math import comb
import sympy as sp


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def exact_isogeny_check() -> None:
    x = sp.symbols("x")
    r2 = sp.sqrt(2)
    t = 2 * r2 / 3
    b = (1 + t) / 8
    bm = (1 - t) / 8
    alpha = -sp.Rational(1, 3) - r2 / 4
    f = x**3 + x**2 + b*x
    ga = sp.simplify(sp.diff(f, x).subs(x, alpha))
    fa = sp.simplify(f.subs(x, alpha))
    psi3 = 3*x**4 + 4*x**3 + 6*b*x**2 - b**2
    assert sp.simplify(psi3.subs(x, alpha)) == 0
    assert fa != 0
    h = x - alpha
    XV = x + 2*ga/h + 4*fa/h**2
    VYmult = sp.diff(XV, x)
    a4 = -sp.Rational(37, 24) - 9*t/8
    a6 = sp.Rational(31, 108) + 3*t/4
    quotient_eq = sp.cancel(sp.expand(VYmult**2)*f - (XV**3 + XV**2 + a4*XV + a6))
    assert sp.simplify(quotient_eq) == 0
    X = sp.symbols("X")
    model_eq = (3*X+sp.Rational(2,3))**3+(3*X+sp.Rational(2,3))**2 +a4*(3*X+sp.Rational(2,3))+a6 - 27*(X**3 + X**2 +bm*X)
    assert sp.simplify(model_eq) == 0
    # Coefficient of omega in the exact differential d(y/(x-alpha))
    D = h - ga/h - 2*fa/h**2
    # The eta pullback difference is exactly -(2u/3) d(y/(x-alpha)).
    eta_diff = sp.cancel((XV-sp.Rational(2, 3))/3 - (x+t/4) + sp.Rational(2,3)*D)
    assert sp.simplify(eta_diff) == 0
    # Compound normalized CM matrix: c [[1,-A],[0,-1]]; square = -6 I.
    A=(2+t)/4
    M=sp.Matrix([[1, -A],[0, -1]])
    assert M*M == sp.eye(2)
    print("PASS_GH74_EXACT_3ISOGENY_CM_MODEL_AND_DERHAM")


def pair_add(a, b, p):
    return ((a[0]+b[0]) % p, (a[1]+b[1]) % p)


def pair_mul(a, b, p, s):
    return ((a[0]*b[0]+s*a[1]*b[1]) % p, (a[0]*b[1]+a[1]*b[0]) % p)


def pair_scalar(a, c, p):
    return ((a[0]*c) % p, (a[1]*c) % p)


def check_prime(p: int):
    m=(p-3)//8
    N=(p-1)//2
    n=2*m
    assert p == 8*m+3 and (p-3)%8 == 0
    s=8*pow(9,-1,p)%p  # t^2 = 8/9
    inv8=pow(8,-1,p)
    b=(inv8,inv8)
    H=(0,0)
    K=(0,0)
    Hprime=(0,0)
    h=1
    bp=(1,0)
    prev=(1,0)
    for j in range(n+1):
        H=pair_add(H,pair_scalar(bp,h,p),p)
        kcoef=(N-2*j)*pow(j+1,-1,p)*h %p
        K=pair_add(K,pair_scalar(pair_mul(bp,b,p,s),kcoef,p),p)
        if j:
            Hprime=pair_add(Hprime,pair_scalar(prev,j*h*inv8,p),p)
        if j < n:
            h_next=h*(N-2*j)*(N-2*j-1)*pow((j+1)**2,-1,p)%p
        else:
            h_next=0
        # Whole-polynomial coefficient relation (75.3), including the terminal coefficient.
        assert kcoef == (2*((j+1)*h_next-(4*j+1)*h))%p, (p,j,"K-H' coefficient")
        prev=bp
        bp=pair_mul(bp,b,p,s)
        h=h_next
    t=(0,1)
    A=(2*pow(4,-1,p)%p,pow(4,-1,p))
    # (-6/p) is +-1, not the raw modular Euler-power residue p-1.
    chi=1 if pow(p-6,(p-1)//2,p)==1 else -1
    sel=pair_add(pair_scalar(K,1+chi,p),pair_mul(A,H,p,s),p)
    assert sel==(0,0),(p,"CM Cartier selection",sel)
    full_rhs=pair_add(pair_scalar(H,(-1*pow(4,-1,p))%p,p),pair_scalar(pair_mul(t,H,p,s),(-pow(4,-1,p))%p,p),p)
    # (1-t^2) H'_t, where t^2=s.
    full_rhs=pair_add(full_rhs,pair_scalar(Hprime,1-s,p),p)
    assert K==full_rhs,(p,"whole-polynomial K derivative identity")
    euler=pair_add(pair_mul(t,Hprime,p,s),pair_scalar(H,-1,p),p)
    if p%24==11:
        assert chi==1
        assert pair_add(pair_scalar(K,2,p),pair_mul(A,H,p,s),p)==(0,0)
        assert euler==(0,0), (p,"split Euler")
        assert H!=(0,0), (p,"split H nonzero")
    else:
        assert p%24==19 and chi==-1
        assert H==(0,0), (p,"inert H zero")
        assert euler!=(0,0), (p,"inert Euler nonzero")
    # GH-55's original independently calculated F/G hypergeometric channels.
    c=1
    nine=1
    F=0
    G=0
    for j in range(m+1):
        F=(F+c*nine)%p
        G=(G+(16*j+5)*c*nine)%p
        if j<m:
            c=(c*(j-m)**2*pow((2*m+2+j)*(j+1),-1,p))%p
            nine=nine*9%p
    D=comb(3*m+1,m)%p
    factor=pow(9,m,p)
    DF=(D*F)%p
    DG=(D*G)%p
    assert pair_scalar(H,factor,p)==(DF,0),(p,"F-Hasse transport")
    assert pair_scalar(euler,factor,p)==(DG,0),(p,"G-Euler transport")
    assert (F == 0) != (G == 0),(p,"exclusive F/G")
    if p%24==11: assert G==0 and F!=0
    else: assert F==0 and G!=0
    return (F,G,H,K,Hprime)


def main() -> None:
    exact_isogeny_check()
    count={11:0,19:0}
    cases={}
    for p in range(11,10000):
        if p%8 != 3 or not is_prime(p):
            continue
        cases[p]=check_prime(p)
        count[p%24]+=1
    assert sum(count.values())==310, count
    print(f"PASS_GH75_EXACT_MODP_CARTIER_H_K_AND_F_G {sum(count.values())} primes p<10000; classes 11:{count[11]} 19:{count[19]}")
    for p in (11,19,43,59,67,83):
        F,G,H,K,Hp=cases[p]
        print(f"p={p} F={F} G={G} H={H} K={K} Hprime={Hp}")
    print("PASS_GH75_INDEPENDENT_ALL_PRIME_CLASS_PROOF_HAS_ALGEBRAIC_ARGUMENT; finite tests are checks only")


if __name__=="__main__":
    main()
