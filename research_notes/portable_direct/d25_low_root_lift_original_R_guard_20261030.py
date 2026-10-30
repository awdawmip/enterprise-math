#!/usr/bin/env python3
"""Original D25 second-digit LIFT exactly reduced to a degree-2m Gauss root.

Independent original weighted A216 and original frozen reflected R ports.
Author-side portable exact check only, not the native H0/B0 experiment.
"""
from d25_onhour_gauss_tail_hensel_transport_20261030 import (
    primes_below, evaluate, root, factorial_tail,
)


def frozen_original_R(p, m, gauss_half_coefficients):
    """Original signed double sum, linear-time equivalent with preserved a-index."""
    C = 1 * pow(10, -1, p) % p
    pref = first = result = 0
    for i in range(1, m + 1):
        pref = (pref + C) % p
        first = (first + i * C) % p
        bracket = ((6*i+1)*pref - 6*first) % p
        result = (result + 2*gauss_half_coefficients[i]*bracket) % p
        if i < m:
            C = C * 36*i*i*pow((6*i+5)*(3*i+2), -1, p) % p
    return result


def original_weighted_A(p):
    mod = p**3
    a = 1
    weighted = 1
    for n in range(p - 1):
        num = (2*n+1)*(2*n+2)*(3*n+1)*(3*n+2)*(3*n+3)
        den = 216 * (n+1)**5
        a = a*num*pow(den, -1, mod) % mod
        weighted = (weighted + (6*(n+1)+1)*a) % mod
    return weighted


def check(p):
    m = (p - 1)//6
    mod = p**3
    q = p**2
    inv2 = pow(2, -1, mod)
    h = [1]
    for n in range(p-1):
        h.append(h[-1]*(6*n+1)*(3*n+1)*pow(36*(n+1)**2, -1, mod) % mod)
    tail = sum(h[2*m+1:]) % mod
    assert tail % q == 0
    F = tail//q
    assert F == factorial_tail(p, m)
    R = frozen_original_R(p, m, [a % p for a in h])
    _, g = evaluate(h, p-1, inv2, mod)
    _, gl = evaluate(h, 2*m, inv2, mod)
    assert g % q == gl % q
    assert g % p
    zlo = root(h, 2*m, p)
    zfull = root(h, p-1, p)
    dl = ((inv2-zlo)%mod)//p
    df = ((inv2-zfull)%mod)//p
    g2 = g % q
    t = pow(g2, -2, q)
    # Original full-root criterion from accepted CM0 and source-aligned Clausen.
    dstar = (t*pow(6,-1,q) + p*(R*t*pow(6,-1,q) - t*t*pow(54,-1,q)))%q
    # New source-corrected degree-2m root criterion.
    dlow_star = (dstar - p*F*pow(g2,-1,p))%q
    assert dl % p == dlow_star % p
    A = original_weighted_A(p)
    assert (A-p)%q==0
    residual = ((A-p)%mod)//q
    root_error = 6*(g2 % p)**2*(((dl-dstar)%q)//p) % p
    corrected = (root_error+6*(g2%p)*F) % p
    assert corrected == residual, (p, R, F, residual, corrected)
    assert ((df-dstar)%q)//p*6*(g2%p)**2%p == residual
    assert (A-p)%mod==0, (p, residual)
    assert dl==dlow_star, (p, dl, dlow_star, R, F)
    return p,R,F,dl,dlow_star,df,dstar,root_error,corrected


def main():
    out=[check(p) for p in primes_below(5000)]
    for x in out:
        if x[0] in (13,19,37,43,157,211,373):
            print('original_R_corrected_low_root p,R,F,d_low,predicted_low,d_full,predicted_full,uncorrected_residual,corrected_residual',*x)
    shortcut=[x[0] for x in out if x[3]==x[6]]
    print('target_primes_checked',len(out))
    print('uncorrected_low_root_shortcut_accidentally_succeeds',shortcut)
    print('PASS_D25_ORIGINAL_R_SOURCE_CORRECTED_LOW_ROOT_LIFT')


if __name__ == '__main__':
    main()
