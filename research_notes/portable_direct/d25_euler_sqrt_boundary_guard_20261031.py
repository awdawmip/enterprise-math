#!/usr/bin/env python3
"""Exact author-side check of Euler-Clausen p-adic boundary for original A216.

Formal power-series coefficient comparison, modular arithmetic (Z/p^3), no floating
point, no native H0/B0 Frobenius experiment, no formal Source admission.
"""


def primes_below(limit):
    for p in range(5, limit):
        if all(p % d for d in range(2, int(p**0.5) + 1)):
            yield p


def e_coeffs(p):
    q = p**3
    e = [1] * p
    for j in range(1, p):
        # (-1)^j binom(1/2,j), in p-local rationals.
        e[j] = e[j-1] * (2*j - 3) * pow(2*j, -1, q) % q
    return e


def check_euler_digit_strata(p):
    q = p**3
    e = e_coeffs(p)
    j0 = (p + 1)//2
    s = -1 if j0 % 2 else 1
    H = sum(pow(k, -1, q) for k in range(1, j0+1)) % q
    H2 = sum(pow(k*k, -1, q) for k in range(1, j0+1)) % q
    predicted_j0 = s * (
        1 - p * H * pow(2, -1, q)
        + p*p * (H*H-H2)*pow(8, -1, q)
    ) % q
    assert e[j0] == predicted_j0, (p, 'boundary', e[j0], predicted_j0)
    assert all(e[j] % p for j in range(j0+1))
    assert all(e[j] % p == 0 and e[j] % (p*p) != 0
               for j in range(j0+1, p))

    # First-order p-local expansion of each high-index normalized e_j/p,
    # verified independently against the recurrence.
    prod = 1
    delta = (-H * pow(2, -1, p) - pow(3, -1, p)) % p
    for r in range((p-5)//2 + 1):
        if r:
            prod = prod * (2*r) * pow(2*r+3, -1, q) % q
            delta = (delta + pow(2*r, -1, p) - pow(2*r+3, -1, p)) % p
        j = j0 + 1 + r
        expected = p*s * pow(3, -1, q) * prod * (1+p*delta) % q
        assert e[j] == expected, (p,'high', j,e[j],expected)
    return e


def convolution(a, b, limit, mod):
    out = [0]*limit
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j in range(min(len(b),limit-i)):
            out[i+j] = (out[i+j] + ai*b[j]) % mod
    return out


def exceptional_modp_from_original_indices(p):
    """Original (j,k,l) labels, weighted finite Cauchy boundary over F_p."""
    m=(p-1)//6
    j0=(p+1)//2
    tmax=p-1-j0
    from math import comb
    g0=[comb(m,k)*comb(2*m,k)%p for k in range(m+1)]
    h0=[comb(4*m,k)*comb(5*m,k)%p for k in range(tmax+1)]
    conv0=convolution(g0,h0,tmax+1,p)
    s=-1 if j0%2 else 1
    return (s*pow(2,-j0,p)*sum(
        (6*t+4)*conv0[t]*pow(2,-t,p)
        for t in range(tmax+1)))%p


def full_original_vs_euler(p):
    q = p**3
    e = check_euler_digit_strata(p)
    g = [1]*p
    h = [1]*p
    a = [1]*p
    for n in range(1,p):
        k=n-1
        # [ (1/6)_n (1/3)_n ] / n!^2
        g[n] = g[n-1]*(6*k+1)*(3*k+1)*pow(18*n*n,-1,q)%q
        # [ (5/6)_n (2/3)_n ] / n!^2
        h[n] = h[n-1]*(6*k+5)*(3*k+2)*pow(18*n*n,-1,q)%q
        # binom(2n,n)^2 binom(3n,n)/216^n
        a[n] = a[n-1]*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*n**3,-1,q)%q
    conv = convolution(g,h,p,q)
    j0 = (p+1)//2
    def weighted_e(e_arr):
        f=convolution(e_arr,conv,p,q)
        return sum((6*n+1)*f[n]*pow(2,-n,q) for n in range(p))%q
    original=sum((6*n+1)*a[n] for n in range(p))%q
    full=weighted_e(e)
    naive=weighted_e(e[:j0])
    exceptional=weighted_e([0]*j0+[e[j0]])
    high=weighted_e([0]*(j0+1)+e[j0+1:])
    assert original==full==(naive+exceptional+high)%q
    assert high%p==0
    assert original%p == 0
    # A second finite-field computation using integer binomial sources.
    exceptional_other=exceptional_modp_from_original_indices(p)
    assert exceptional_other == exceptional%p
    return {'p':p,'original_A_mod_p3':original,
            'exceptional_j':j0,'e_j_mod_p':e[j0]%p,
            'exceptional_port_mod_p':exceptional%p,
            'false_low_cut_mod_p':naive%p,
            'high_port_div_p_mod_p':high//p%p,
            'three_port_sum_mod_p3':full}


def main():
    eligible=[p for p in primes_below(1500) if p%24 in (13,19)]
    assert len(eligible)==60
    ports=[]
    for p in eligible:
        check_euler_digit_strata(p)
        ports.append((p,exceptional_modp_from_original_indices(p)))
    assert all(v!=0 for _,v in ports)
    witnesses=[]
    for p in (13,19,37,43,61,67,373):
        witnesses.append(full_original_vs_euler(p))
    for data in witnesses:
        print(data)
    print('PASS: ALL_EULER_DIGIT_STRATA_60_PRIMES + NONZERO_EXCEPTIONAL_PORT_60_PRIMES + ORIGINAL_216_CAUCHY_P3_7_PRIMES')


if __name__ == '__main__':
    main()
