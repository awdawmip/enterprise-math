#!/usr/bin/env python3
"""Author exact check: original-parameter full-rank genuine finite-face Ward flux.

Carrier: p=6m+1 prime, ordered low-high (j, ell) pairs, theta=-p/6.
No approximation/floating point; p-adic unit/power representation modulo p^3.
All compared E_n values have the genuine two cutoff origins.
"""
from __future__ import annotations
from math import isqrt
from fractions import Fraction


def target_primes(limit=997):
    for p in range(7, limit + 1):
        if p % 6 != 1 or any(p % q == 0 for q in range(2, isqrt(p)+1)):
            continue
        yield p


def run(p: int, verify_ranks: bool = True):
    m = (p - 1) // 6
    L, N = 1 - 2 * m, 2 * m - 1
    mod = p**3
    inv = lambda t: pow(t % mod, -1, mod)
    theta = -p * inv(6) % mod
    # Original f_r(theta) ratio: (6r+1)(3r+1)/(18(r+1)^2).
    # Strip p factors so f/p and f/p^2 are computed truthfully.
    v, unit = 0, 1
    f = [0] * p
    beta = [None] * p
    v2m_unit = None
    for r in range(p):
        f[r] = unit * pow(p, v, mod) % mod
        if r > 2 * m:
            assert v == 2, (p, r, v)
            beta[r] = unit
        if r == 2*m:
            assert v == 1, (p,r,v)
            v2m_unit = unit
        if r == p-1:
            break
        x, y = 6*r + 1, 3*r + 1
        while x % p == 0:
            x //= p; v += 1
        while y % p == 0:
            y //= p; v += 1
        unit = unit*x*y*inv(18*(r+1)**2) % mod
    assert v2m_unit is not None
    E, Z = {}, {}
    if verify_ranks:
        for n in range(L, N+1):
            s0 = s1 = 0
            for j in range(1, 2*m+1):
                ell = j + n
                if 1 <= ell <= 2*m:
                    t = f[j] * beta[p-ell] % mod
                    s0 += t
                    s1 += j*t
            Z[n] = (2*s1 - (p-n)*s0) % mod
    zleft = -4*m*f[2*m]*beta[p-1] % mod
    if verify_ranks:
        assert Z[L] == zleft, (p, Z[L],zleft)
    # Two rank-sign families preserve four genuine finite-cutoff origins.
    for n in range(L, N+1):
        if n >= 0:
            E[n] = (2*(m+theta)**2 * beta[p-n-1]
                    -(6*m*m - 8*m*theta + 2*theta*theta) * f[2*m-n]*beta[4*m]) % mod
        else:
            E[n] = ((20*m*m-14*m*theta+2*theta*theta)*f[-n]*beta[p-1]
                   +(2*m*theta-2*theta*theta)*f[2*m]*beta[p-(2*m+n+1)]) % mod
        if verify_ranks:
            zn1 = Z[n+1] if n<N else 0
            assert ((p-n)*Z[n] - ((2*(p-n)-1)*inv(2))*zn1 - E[n]) % mod == 0, ('rank',p,n)
    q=2*p
    suffix=1
    flux=0
    flux_plus=flux_minus=0
    for n in range(N,L-1,-1):
        B=q-2*n-1
        A=q-2*n
        D = suffix * inv(B) % mod
        term=36*D*E[n]%mod
        flux = (flux + term) % mod
        if n>=0:
            flux_plus=(flux_plus+term)%mod
        else:
            flux_minus=(flux_minus+term)%mod
        suffix = suffix*A*inv(B) % mod
    P = suffix
    assert flux == P*(18*zleft) % mod, ('source_flux',p,flux,P*18*zleft%mod)
    pplus=1
    for r in range(0,N+1):
        pplus=pplus*(q-2*r)*inv(q-2*r-1)%mod
    assert flux_plus==pplus*18*Z[0]%mod, ('positive_split',p)
    assert flux_minus==(P*18*zleft-pplus*18*Z[0])%mod, ('negative_split',p)
    assert (flux_plus+flux_minus)%mod==flux, ('split_sum',p)
    assert flux_plus%p==0 and flux_minus%p==0, ('split_valuation',p)
    assert (flux_plus//p+flux_minus//p)%p==0, ('split_residual_cancel',p)
    if Z[0]%p:
        assert flux_plus%(p*p)!=0 and flux_minus%(p*p)!=0, ('split_first_digit',p)
    assert flux % (p*p) == 0, ('valuation_at_least_two',p)
    u = 1
    for r in range(L,N+1):
        if r == 0:
            u = u*inv(q-1)%mod
        else:
            u = u*(q-2*r)*inv(q-2*r-1)%mod
    assert P==(2*p*u)%mod
    zunit=(-4*m*v2m_unit*beta[p-1])%p
    a=(-108*zunit)%p
    # Yhat(theta)=18Z, and a is the Hasse first jet of the left cell.
    assert (18*zunit)%p == (-a*pow(6,-1,p))%p, ('bridge',p)
    leading = (-u*a*pow(3,-1,p))%p
    assert flux//(p*p)==leading, ('leading',p,flux//(p*p),leading)
    assert leading != 0, ('nonzero',p)
    hjet=(-6*u*a)%p
    assert leading == hjet*pow(18,-1,p)%p
    return {'p':p,'m':m,'U_mod_p':u%p,'a_mod_p':a,
            'flux_over_p2_mod_p':leading,'hesse_second_jet':hjet,
            'left_Z_over_p_mod_p':zunit,
            'Z0_mod_p':Z[0]%p,'plus_over_p_mod_p':flux_plus//p%p,
            'minus_over_p_mod_p':flux_minus//p%p}


def exact_rational_audit(p: int):
    # Independent Q-valued Pochhammer recurrence; not shared modular arithmetic.
    m=(p-1)//6; L=1-2*m; N=2*m-1
    theta=Fraction(-p,6)
    f=[Fraction(1)]
    for r in range(p-1):
        f.append(f[-1]*Fraction((6*r+1)*(3*r+1),18*(r+1)**2))
    beta={r:f[r]/p**2 for r in range(2*m+1,p)}
    Z={}
    E={}
    for n in range(L,N+1):
        v0=v1=Fraction(0)
        for j in range(1,2*m+1):
            ell=j+n
            if 1<=ell<=2*m:
                v=f[j]*beta[p-ell]; v0+=v; v1+=j*v
        Z[n]=2*v1-(p-n)*v0
        if n>=0:
            E[n]=2*(m+theta)**2*beta[p-n-1]-(6*m*m-8*m*theta+2*theta**2)*f[2*m-n]*beta[4*m]
        else:
            E[n]=(20*m*m-14*m*theta+2*theta**2)*f[-n]*beta[p-1]+(2*m*theta-2*theta**2)*f[2*m]*beta[p-(2*m+n+1)]
    Z[N+1]=Fraction(0)
    for n in range(L,N+1):
        assert (p-n)*Z[n]-Fraction(2*(p-n)-1,2)*Z[n+1]==E[n], ('rational_rank',p,n)
    q=2*p; suffix=Fraction(1); flux=Fraction(0); fplus=fminus=Fraction(0)
    for n in range(N,L-1,-1):
        term=36*suffix*E[n]/(q-2*n-1)
        flux+=term
        if n>=0: fplus+=term
        else: fminus+=term
        suffix*=Fraction(q-2*n,q-2*n-1)
    assert flux==suffix*(18*Z[L]), ('rational_flux',p)
    pplus=Fraction(1)
    for r in range(0,N+1):pplus*=Fraction(q-2*r,q-2*r-1)
    assert fplus==pplus*18*Z[0], ('rational_split_plus',p)
    assert fminus==suffix*18*Z[L]-pplus*18*Z[0], ('rational_split_minus',p)
    assert flux.denominator%p!=0 and flux.numerator%(p*p)==0 and flux.numerator%(p**3)!=0
    return flux


if __name__ == '__main__':
    results=[run(p) for p in target_primes(997)]
    assert len(results)==80, len(results)
    for p in [7,13,19]:
        exact_rational_audit(p)
    for p in [7,13,733,997]:
        print(next(x for x in results if x['p']==p))
    print('PASS: 80 target primes, all genuine source rank recurrences, finite-face flux, '
          'and original-parameter exact valuation certificates modulo p^3; '
          'independent exact rational audits p=7,13,19')
