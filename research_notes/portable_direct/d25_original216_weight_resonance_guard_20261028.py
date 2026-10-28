#!/usr/bin/env python3
"""D25 on-hour author-side exact p-adic resonance check.

Original 216 signed finite cutoff and separate terminating Clausen coefficient;
no native H0/B0 operator or source admission is executed here.
"""
from math import comb

PRIMES = (7, 13, 19, 31, 37, 43, 61, 67, 73, 211, 373)
TARGETS = (13, 19, 37, 43, 61, 67, 211, 373)


def inv(x, modulus):
    return pow(x % modulus, -1, modulus)


def rising_integer(x, n):
    result = 1
    for k in range(n):
        result *= x + k
    return result


def original_unweighted(n, mod):
    return comb(2*n, n)**2 * comb(3*n, n) * inv(pow(216, n, mod), mod) % mod


def original_weighted_sum(p):
    mod = p**3
    return sum((6*n+1)*original_unweighted(n, mod) for n in range(p)) % mod


def clausen_unweighted(m, n, mod):
    den = pow(2, n, mod) * pow(__import__('math').factorial(n), 3, mod) % mod
    return (rising_integer(-3*m, n) * rising_integer(-2*m, n) *
            rising_integer(-4*m, n) * inv(den, mod)) % mod


def denominator_lift(n, p, mod):
    # E_n = product_{j=1}^n (1-p/(2j))^-1 (1-p/j)^-1
    u = 1
    for j in range(1, n+1):
        u = u*(2*j*inv(2*j-p, mod)) % mod
        u = u*(j*inv(j-p, mod)) % mod
    return u


def first_log_shift(m, n, p):
    # Three original Pochhammer parameter shifts at s=p.
    values = [(-3*m, 1, 2), (-2*m, 1, 3), (-4*m, 2, 3)]
    return sum(num * inv(den * (a+j), p)
               for a, num, den in values for j in range(n)) % p


def harmonic(n, p):
    return sum(inv(j, p) for j in range(1, n+1)) % p


def check(p):
    assert p % 6 == 1 and p > 3
    m = (p-1)//6
    q, r = p*p, p**3
    singular_indices = [n for n in range(p) if (6*n+1)%p == 0]
    assert singular_indices == [m]
    assert all((6*n+1)%p for n in range(p) if n!=m)
    assert 6*m+1 == p

    a = original_unweighted(m, q)
    t = clausen_unweighted(m, m, q)
    e = denominator_lift(m, p, q)
    L = first_log_shift(m, m, p)
    H = harmonic(m, p)
    correction = (L - 3 * inv(2, p) * H) % p
    H2, H3, H4 = (harmonic(j*m, p) for j in (2, 3, 4))
    # Exact rational rewriting and prime-reflection at p-1=6m.
    assert L == (H2 + H3 + 2*H - 4*H4) * inv(6, p) % p
    assert H4 == H2
    assert correction == (H3 - 3*H2 - 7*H) * inv(6, p) % p
    # Classical Eisenstein/Lehmer harmonic congruences, used only at mod p.
    q2 = (pow(2, p-1, q)-1)//p
    q3 = (pow(3, p-1, q)-1)//p
    q3888 = (pow(3888, p-1, q)-1)//p
    assert H3 == -2*q2 % p
    assert H2 == -3*inv(2,p)*q3 % p
    assert H == (-2*q2 - 3*inv(2,p)*q3) % p
    assert correction == (2*q2 + 5*inv(2,p)*q3) % p
    assert correction == q3888*inv(2,p) % p
    left_unweighted = (a - t*e) % q
    assert left_unweighted % p == 0
    assert left_unweighted // p == (t % p)*correction % p
    original_weighted = p*a % r
    clausen_weighted = p*t*e % r
    source_defect = (original_weighted - clausen_weighted) % r
    assert source_defect == p*p*((t%p)*correction%p)
    assert a%p and t%p

    W = original_weighted_sum(p)
    if p in TARGETS:
        assert W == p % r, (p,W)
        assert (W - original_weighted)%p == 0
    out = dict(p=p,m=m,resonant_unit=a%p,T_unit=t%p,
               weight_source_correction=source_defect//q,
               Fermat_q3888=q3888, W_mod_p3=W)
    if p == 373:
        assert (a,t,e,L,H,correction) == (32200,117244,110409,151,73,228)
        assert (H2,H3,H4,q2,q3,q3888) == (108,338,108,204,301,83)
        assert (source_defect//q,source_defect) == (214,29773606)
        assert (original_weighted,clausen_weighted) == (12010600,34132111)
        assert (W-original_weighted)//p % q == 106930
        out.update(resonance_unweighted_mod_p2=a, term_weighted_mod_p3=original_weighted,
                   clausen_weighted_mod_p3=clausen_weighted,
                   rest_over_p_mod_p2=((W-original_weighted)//p)%q,
                   E_mod_p2=e,L_mod_p=L,H_mod_p=H)
    return out


def main():
    for p in PRIMES:
        print(check(p))
    print('PASS_D25_ORIGINAL216_UNIQUE_RESONANCE_SOURCE_DEFECT',len(PRIMES),'exact-prime-cases')


if __name__ == '__main__':
    main()
