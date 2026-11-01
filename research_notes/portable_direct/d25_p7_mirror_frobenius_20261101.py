#!/usr/bin/env python3
"""Author-only exact p≡7 (mod 8) mirrored beta/Jacobi p² and signed ports.

NOT an H0/B0 native benchmark or a proof of universal supersingular p² zero.
All denominators are p-units; counts and finite controls are explicit.
"""
from math import comb, isqrt


def primes(limit):
    a = bytearray(b'\1') * (limit + 1)
    a[:2] = b'\0\0'
    for j in range(2, isqrt(limit) + 1):
        if a[j]:
            a[j*j::j] = b'\0' * ((limit-j*j)//j+1)
    return [p for p in range(7, limit+1) if a[p] and p % 8 == 7]


def beta_original(p):
    mod = p*p
    term = value = 1
    for k in range(p-1):
        term = term * (8*k+1) * (8*k+3) * pow(576*(k+1)**2, -1, mod) % mod
        value = (value + term) % mod
    return value


def shifted_binomial(n, x, lam, mod):
    """sum binom(n,k)binom(x,k)lam^k modulo p²; 0<=n<p, x<2p."""
    term = 1
    value = 1
    for k in range(n):
        term = term * (n-k) * (x-k) % mod
        term = term * pow((k+1)**2, -1, mod) * lam % mod
        value = (value + term) % mod
    return value


def extraction(a, b, lam, mod, r):
    """Independent binomial-convolution [t^r](1+t)^a(t+lam)^b."""
    return sum(comb(a, j)*comb(b, r-j)*pow(lam, b-r+j, mod)
               for j in range(max(0,r-b), min(a,r)+1)) % mod


def readout(p, independent=False):
    assert p>3 and p%8==7
    a,b=(7*p-1)//8,(5*p-3)//8
    assert 0<b<a<p
    mod=p*p
    lam=pow(9,-1,mod)
    j=shifted_binomial(b,a,lam,mod)
    k1=shifted_binomial(b,a+p,lam,mod)
    kl=shifted_binomial(a,b+p,lam,mod)
    g=beta_original(p)
    # Mirrored Jacobi p² identity for p ≡ 7 (mod 8).
    assert (20*j-7*k1-5*kl-8*g)%mod==0, p
    assert (k1-j)%p==0 and (kl-j)%p==0
    c1=((k1-j)%mod)//p
    cl=((kl-j)%mod)//p
    assert (8*g-8*j+p*(7*c1+5*cl))%mod==0
    if independent:
        # Compute coefficient ports from integer binomial expansions rather
        # than from shifted Jacobi sums. This preserves two distinct cuts.
        assert j==extraction(a,b,lam,mod,b)
        e1=sum((comb(p,k)//p)*extraction(a,b,lam,mod,b-k)
               for k in range(1,b+1))%p
        el=sum((comb(p,k)//p)*pow(lam,p-k,mod)*
               extraction(a,b,lam,mod,b+p-k)
               for k in range(1,p))%p
        assert (c1,cl)==(e1,el),(p,c1,cl,e1,el)
    return dict(p=p, cls=p%24, a=a,b=b,J=j,C1=c1,Clambda=cl,G=g,
                J_over_p=j//p if j%p==0 else None,
                carry_residual=(8*(j//p)-7*c1-5*cl)%p if j%p==0 else None)


def main():
    cases=primes(3000)
    rows=[readout(p) for p in cases]
    fixed=[7,23,31,47,71,167,191,239]
    checked=[readout(p,True) for p in fixed]
    target=[r for r in rows if r['cls']==23]
    control=[r for r in rows if r['cls']==7]
    assert all(r['G']==0 and r['J']%r['p']==0 and r['carry_residual']==0
               for r in target)
    assert all(r['G']%r['p'] and r['J']%r['p'] for r in control)
    print('MIRRORED_JACOBI_ALL_P7MOD8_UP_TO_3000',len(rows),'PASS')
    print('INDEPENDENT_DIVIDED_FROBENIUS_PORTS',len(checked),'PASS')
    print('P23MOD24_P2_ZERO_FINITE_OBSERVATIONS',len(target),'PASS_UNPROVED_GLOBAL')
    print('P7MOD24_UNIT_CONTROLS',len(control),'PASS_UNPROVED_GLOBAL')
    for row in checked:
        print(row)
    print('UNIVERSAL_P13_P23_P2_ZERO_NOT_PROVED; ORIGINAL_NATIVE_H0B0_NOT_RUN')


if __name__=='__main__':
    main()
