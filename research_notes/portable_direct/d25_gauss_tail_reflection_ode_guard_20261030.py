#!/usr/bin/env python3
"""D25 exact p-local check for the original Gauss high tail / frozen C recurrence.

It verifies the termwise identity c_(p-a) * 2**(-(p-a)) / p**2 == C_a (mod p)
for 1<=a<=4m, p=6m+1 prime, with c_n=(1/6)_n(1/3)_n/(n!)**2.
It also verifies the nonhomogeneous p^2 hypergeometric endpoint defect.
No surrogate H0/B0 or native Frobenius is computed. No floating-point arithmetic.
"""
from math import isqrt


def primes_under(bound):
    for p in range(7, bound):
        if p % 6 != 1:
            continue
        if all(p % d for d in range(2, isqrt(p) + 1)):
            yield p


def check_prime(p):
    assert p > 5 and p % 6 == 1
    m, modulus = (p - 1) // 6, p**3
    inv2 = pow(2, -1, modulus)
    c, zpow = 1, 1
    weighted = []
    M = d = d2 = 0
    for n in range(p):
        w = c * zpow % modulus
        weighted.append(w)
        M = (M + w) % modulus
        d = (d + 2*n*w) % modulus
        d2 = (d2 + 4*n*(n-1)*w) % modulus
        if n == p-1:
            last_c, last_zpow = c, zpow
        else:
            c = c * (6*n + 1) * (3*n + 1) * pow(18*(n+1)**2, -1, modulus) % modulus
            zpow = zpow * inv2 % modulus

    # This is exactly the frozen reflected sequence, extended only within its
    # p-unit recurrence domain a <= 4m. The original R observer is unchanged.
    C = pow(10, -1, p)
    Csum = 0
    Cprefix = 0
    for a in range(1, 4*m+1):
        original = weighted[p-a]
        assert original % (p*p) == 0, (p, a, 'tail valuation')
        actual = original // (p*p) % p
        assert actual == C, (p, a, 'source-indexed reflection', actual, C)
        Csum = (Csum + C) % p
        if a == m:
            Cprefix = Csum
        if a < 4*m:
            C = C * 36*a*a*pow((6*a+5)*(3*a+2), -1, p) % p

    F_original = sum(weighted[2*m+1:]) % modulus
    assert F_original % (p*p) == 0
    F = F_original // (p*p) % p
    assert F == Csum, (p, 'original high tail', F, Csum)
    assert last_c % (p*p) == 0
    assert last_c // (p*p) % p == pow(10, -1, p)

    # Exact truncated hypergeometric differential equation L(G) at z=1/2.
    slope = (p-5*pow(6,-1,modulus))*(p-2*pow(3,-1,modulus)) % modulus
    lhs4 = (d2+d-2*pow(9,-1,modulus)*M) % modulus
    rhs4 = (-4*slope*last_c*last_zpow) % modulus
    assert lhs4 == rhs4, (p, 'original coefficient differential recurrence')
    assert lhs4 == (-2*pow(9,-1,modulus)*p*p) % modulus

    return {'p':p,'m':m,'F_original':F,'C_extended_sum':Csum,
            'C_original_prefix_sum':Cprefix,'c_p_minus_1_over_p2':last_c//(p*p)%p,
            'ODE_defect_over_p2':lhs4//(p*p)%p,
            'M_mod_p3':M,'Gprime_mod_p2':d%(p*p)}


if __name__ == '__main__':
    checked = inert = 0
    for p in primes_under(5000):
        row = check_prime(p)
        checked += 1
        inert += p%24 in (13,19)
        if p in (7,13,19,157,373):
            print('sample',row)
    print('PASS_D25_SOURCE_INDEXED_TAIL_REFLECTION_AND_ODE_BOUNDARY')
    print('p_1mod6_checked',checked,'target_class_checked',inert)
