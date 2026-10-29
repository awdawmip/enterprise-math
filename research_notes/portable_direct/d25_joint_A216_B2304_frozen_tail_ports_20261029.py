#!/usr/bin/env python3
"""Author-only exact source-preserving finite-ring check for D25 original A216/B2304.

No H0/B0, Source-native activity/claim or Result is computed. All arithmetic is
integer mod p^3; index cutoffs and weighted degree observers are never replaced.
"""
from math import comb, isqrt


def primes_under(n):
    for p in range(13, n):
        if p % 24 not in (13, 19):
            continue
        if all(p % i for i in range(2, isqrt(p) + 1)):
            yield p


def companion(p, which):
    mod = p ** 3
    b = [1]
    for n in range(p - 1):
        if which == 'A':
            multiplier = (6*n+1)*(3*n+1)
            denominator = 36*(n+1)**2
        else:
            multiplier = (8*n+1)*(8*n+3)
            denominator = 576*(n+1)**2
        b.append((b[-1] * multiplier * pow(denominator, -1, mod)) % mod)
    return b


def weighted_source(p, terms, cutoff, factor):
    """Source-labeled weighted K^2 and 2KT, split BEFORE evaluation by degree."""
    mod = p ** 3
    U = H = L = E = 0
    for i in range(cutoff+1):
        bi = terms[i]
        for j in range(cutoff+1):
            v = (1+factor*(i+j))*bi*terms[j]
            U += v
            if i+j >= p:
                H += v
        for j in range(cutoff+1,p):
            v = 2*(1+factor*(i+j))*bi*terms[j]
            if i+j < p:
                L += v
            else:
                E += v
    return tuple(x % mod for x in (U,H,L,E))


def complete_direct(p, which):
    mod = p ** 3
    out = 0
    for n in range(p):
        if which == 'A':
            integer = comb(2*n,n)**2 * comb(3*n,n)
            denominator = 216
            weight = 6*n+1
        else:
            integer = comb(2*n,n)**2 * comb(4*n,2*n)
            denominator = 2304
            weight = 8*n+1
        out = (out + weight * integer * pow(denominator,-n,mod)) % mod
    return out


def frozen_R(p, A):
    m=(p-1)//6
    c=pow(10,-1,p)
    R=0
    for i in range(1,m+1):
        c_prefix = c
        inner=0
        # Independent frozen source formula: C_1=1/10 and ratio recurrence.
        for r in range(1,i+1):
            if r>1:
                a=r-1
                c_prefix=c_prefix*36*a*a*pow((6*a+5)*(3*a+2),-1,p)%p
            inner += (6*(i-r)+1)*c_prefix
        R = (R+2*(A[i]%p)*(inner%p))%p
    return R


def inspect(p):
    mod=p**3
    m=(p-1)//6
    a=companion(p,'A')
    # A cutoff m_2=2m; no old K-high carry is possible (4m<p).
    Ua,Ha,La,Ea = weighted_source(p,a,2*m,6)
    assert Ha==0
    wa=complete_direct(p,'A')
    assert wa==(Ua+La)%mod
    assert La%p**2==0 and Ea%p**2==0
    ra=frozen_R(p,a)
    assert Ea//p**2==ra
    # Exact source compression at the original complete weighted observer:
    # delta(U)=2*T*(K+6thetaK)+12*K*thetaT modulo p^3.
    # The accepted CM0 input K=0 mod p on target primes kills the thetaT port,
    # but it cannot kill the separate high-degree (frozen R) observer.
    tail_unit=(sum(a[2*m+1:])%mod)//(p*p)
    theta_tail_unit=(sum(j*a[j] for j in range(2*m+1,p))%mod)//(p*p)
    K0=sum(a[:2*m+1])%p
    thetaK0=sum(i*a[i] for i in range(2*m+1))%p
    H0=sum((12*i+1)*a[i] for i in range(m+1))%p
    general=((2*(K0+6*thetaK0)*tail_unit + 12*K0*theta_tail_unit)%p)
    assert ((La+Ea)%mod)//(p*p)==general
    assert K0==0 # accepted CM0 at all two target classes
    assert general==(H0*tail_unit)%p
    assert (La//p**2+ra)%p==(H0*tail_unit)%p
    g=sum(a)%mod
    h=sum((12*n+1)*v for n,v in enumerate(a))%mod
    assert g%p==0 and (g*h-p)%p**2==0
    delta=((g*h-p)%mod)//p**2
    assert delta==(((Ua+La+Ea-p)%mod)//p**2)
    # Complete square under original observer equals gh, with tail^2=0 mod p^3.
    assert (Ua+La+Ea)%mod == (g*h)%mod

    b=companion(p,'B')
    hits=[next(j for j in range(p) if (8*j+q)%p==0) for q in (1,3)]
    cut=max(hits)
    Ub,Hb,Lb,Eb=weighted_source(p,b,cut,8)
    wb=complete_direct(p,'B')
    assert wb == (Ub-Hb+Lb)%mod
    assert (Lb%p**2)==(Eb%p**2)==0
    # Direct full-square original signed projection, independently of the split.
    full_low=full_high=0
    for i in range(p):
        for j in range(p):
            val=(1+8*(i+j))*b[i]*b[j]
            if i+j<p:
                full_low+=val
            else:
                full_high+=val
    assert full_low%mod==wb
    assert full_high%mod==(Hb+Eb)%mod
    assert (Ub+Lb+Eb)%mod==(full_low+full_high)%mod

    # Exact four-source A-B identity, source reductions retain division order.
    cross=(Ua-Ub+Hb+La-Lb)%mod
    assert cross==(wa-wb)%mod
    if (p%24 in (13,19)):
        assert (wa-p)%p**2==0 and (wb-p)%p**2==0
        # Historical published B congruence (also empirically checked here).
        assert wb==p
        assert cross%p**2==0
        assert (cross//p**2)%p == (delta-ra)%p
    return dict(p=p, U_A=Ua,L_A=La,E_A=Ea,R_frozen=ra,Delta=delta,H0=H0,V_tail=tail_unit,tail_product=general,
                R_A_low=(La//p**2)*pow(2,-1,p)%p,
                U_B=Ub,H_B=Hb,L_B=Lb,E_B=Eb,
                R_B_low=(Lb//p**2)*pow(2,-1,p)%p,
                A=wa,B=wb,CROSS=(wa-wb)%mod,
                K_A_cut=2*m,K_B_cut=cut)


def main():
    checks=[inspect(p) for p in primes_under(400)]
    assert len(checks)==21, len(checks)
    for d in checks:
        if d['p'] in (13,19,37,43,157,211,373):
            print('SOURCE_LEDGER',d)
    p=373
    x=next(d for d in checks if d['p']==p)
    assert (x['R_frozen'],x['Delta'],x['R_A_low'],x['R_B_low']) == (196,196,187,246)
    assert (x['L_A'],x['E_A'],x['L_B'],x['E_B']) == (p*p,196*p*p,119*p*p,111*p*p)
    assert (x['U_A'],x['U_B'],x['H_B']) == (51756361,49669053,14329914)
    print('PASS_D25_ORIGINAL_A216_B2304_FROZEN_LOW_HIGH',len(checks),'target primes <400; independent factorial-binomial original sums; original frozen R double sum')


if __name__ == '__main__':
    main()
