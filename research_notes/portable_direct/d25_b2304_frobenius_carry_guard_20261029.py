#!/usr/bin/env python3
"""Exact finite-ring verification of the B2304 Clausen truncation / Frobenius carry.

Author-side diagnostic, not a native H0/B0 benchmark or a formal theorem admission.
Uses Python standard-library integers only and retains coefficient provenance.
"""
from math import comb, isqrt


def primes_below(n):
    for p in range(5, n):
        if all(p % d for d in range(2, isqrt(p) + 1)):
            yield p


def pochhammer_coeffs(p, modulus, terms, numerators, common_denominator):
    """Coefficients of (numerator parameters)_n/n!^len(params) mod p^s,
    where the caller supplies the fixed denominator powers at each step.
    Only n<p, so every recurrence denominator is a p-adic unit.
    """
    values = [1]
    for n in range(terms - 1):
        numerator = 1
        for a, b in numerators:
            numerator *= a + b * n
        denominator = common_denominator * (n + 1) ** len(numerators)
        values.append(values[-1] * numerator * pow(denominator, -1, modulus) % modulus)
    return values


def convolute(a, modulus):
    result = [0] * (2 * len(a) - 1)
    for i, ai in enumerate(a):
        for j, aj in enumerate(a):
            result[i + j] = (result[i + j] + ai * aj) % modulus
    return result


def evaluate(values, z, p):
    s = d = 0
    power = 1
    for n, v in enumerate(values):
        s = (s + v * power) % p
        d = (d + n * v * power) % p
        power = power * z % p
    return s, d


def check_prime(p):
    assert p % 8 in (3, 5)
    mod = p * p
    bound = (3 * p - 1) // 8 if p % 8 == 3 else (7 * p - 3) // 8
    beta = pochhammer_coeffs(p, mod, bound + 1, [(1, 8), (3, 8)], 64)
    gamma = pochhammer_coeffs(p, mod, p, [(1, 4), (2, 4), (3, 4)], 64)
    # gamma recurrence numerator /64 = (1/4)(1/2)(3/4) numerator /32.
    # We used (2+4n), not (1+2n), so /64 is identical to /32.
    square = convolute(beta, mod)
    assert all((square[n] if n < len(square) else 0) == gamma[n] for n in range(p)), ('clausen-truncation', p)

    z = pow(9, -1, p)
    B, theta_B = evaluate([v % p for v in beta], z, p)
    C, theta_C = evaluate([v % p for v in gamma], z, p)
    weighted_C = (C + 8 * theta_C) % p
    weighted_square = (B * B + 16 * B * theta_B) % p
    if p % 8 == 3:
        assert 2 * bound < p
        assert len(square) < p
        assert weighted_C == weighted_square
        return ('3',p,bound,0,B,weighted_C,weighted_square,0)

    a = (5 * p - 1) // 8
    t = (p - 1) // 4
    assert bound - a == t and 2*a == p + t
    Q = [comb(a, n) * comb(bound, n) % p for n in range(a + 1)]
    assert [v % p for v in beta] == Q + [0] * (bound - a)
    Q_squared = convolute(Q, p)
    # Leading and complete over-cutoff polynomial: - z^p * C_t(z)
    assert Q_squared[p] == p - 1
    assert [v % p for v in Q_squared[p:]] == [(-v) % p for v in gamma[:t+1]]
    assert all(v % p == 0 for v in square[p+t+1:])
    assert [v % p for v in square[p:p+t+1]] == [(-v) % p for v in gamma[:t+1]]
    short_C, short_theta = evaluate([v % p for v in gamma[:t+1]], z, p)
    carry = z * (short_C + 8 * short_theta) % p
    assert weighted_C == (weighted_square + carry) % p
    # Quotient z^p = z is valid for pointwise values, not before theta.
    # At z=2, differentiation *before* this quotient preserves the source degree.
    if p in (13, 373):
        c2, th2 = evaluate([v % p for v in gamma[:t+1]], 2, p)
        true_carry = 2 * (c2 + 8 * th2) % p
        false_carry = 2 * (9 * c2 + 8 * th2) % p
        assert true_carry != false_carry
        print('OBSERVER_FROBENIUS_LOSS',p,c2,th2,true_carry,false_carry)
    return ('5',p,bound,t,B,weighted_C,weighted_square,carry)


def main():
    tests = [p for p in primes_below(400) if p % 8 in (3, 5)]
    reports = [check_prime(p) for p in tests]
    odd3 = sum(x[0]=='3' for x in reports)
    odd5 = sum(x[0]=='5' for x in reports)
    assert odd3 and odd5 and any(x[1]==373 for x in reports)
    print('PASS_D25_B2304_FROBENIUS_CARRY',len(reports),'primes <400; mod p² coefficientwise; mod p exact high-tail')
    print('GROUP_COUNTS',{'p_mod_8_3':odd3,'p_mod_8_5':odd5})
    for p in (13,19,37,43,373):
        print('P_EXACT',check_prime(p))

if __name__=='__main__':
    main()
