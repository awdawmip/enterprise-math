#!/usr/bin/env python3
"""Exact counterexamples to the composite-index 216/2304 transport extension.

Author-side portable integer certificate, not a native H0/B0 computation,
not a proof of the still-open prime p^3 comparison.
"""
from math import comb, factorial, gcd


def transport_via_binomials(length: int, power: int = 3):
    modulus = length**power
    assert length >= 5 and gcd(length, 6) == 1
    a_inverse = pow(216, -1, modulus)
    b_inverse = pow(2304, -1, modulus)
    a_pow = b_pow = 1
    a_total = b_total = 0
    for n in range(length):
        central_squared = comb(2*n, n)**2
        a_total += (6*n+1)*central_squared*comb(3*n, n)*a_pow
        b_total += (8*n+1)*central_squared*comb(4*n, 2*n)*b_pow
        a_total %= modulus
        b_total %= modulus
        a_pow = a_pow*a_inverse % modulus
        b_pow = b_pow*b_inverse % modulus
    return a_total, b_total


def transport_via_factorials(length: int, power: int = 3):
    """Second route: integral factorial quotients before modular inversion."""
    modulus = length**power
    a_inv = pow(216, -1, modulus)
    b_inv = pow(2304, -1, modulus)
    a_total = b_total = 0
    for n in range(length):
        numerator_a = factorial(2*n)*factorial(3*n)
        denominator_a = factorial(n)**5
        numerator_b = factorial(4*n)
        denominator_b = factorial(n)**4
        assert numerator_a % denominator_a == 0
        assert numerator_b % denominator_b == 0
        t_a = numerator_a // denominator_a
        t_b = numerator_b // denominator_b
        a_total = (a_total + (6*n+1)*t_a*pow(a_inv, n, modulus)) % modulus
        b_total = (b_total + (8*n+1)*t_b*pow(b_inv, n, modulus)) % modulus
    return a_total, b_total


def main():
    expected = {
        25: (3150, 9400, 9375),
        49: (86485, 43267, 43218),
        55: (96800, 48400, 48400),
        85: (416500, 144500, 272000),
        115: (51750, 471500, 1101125),
    }
    for length, (a_expected, b_expected, diff_expected) in expected.items():
        modulus = length**3
        a, b = transport_via_binomials(length)
        x, y = transport_via_factorials(length)
        assert (a, b) == (x, y) == (a_expected, b_expected)
        assert (a-b) % modulus == diff_expected
        assert diff_expected != 0
        print(f'COMPOSITE_WITNESS length={length} modulus={modulus} A={a} B={b} '
              f'delta={diff_expected} delta_mod_length2={diff_expected%(length**2)}')

    assert 9375 == 15*25**2
    assert 43218 == 18*49**2
    assert 272000 % (85**2) == 4675
    for prime in [7, 13, 19, 37, 43, 373]:
        a, b = transport_via_binomials(prime)
        assert a == b, (prime, a, b)
    print('PASS_D25_COMPOSITE_CUTOFF_FALSIFIER 5 exact composite witnesses; '
          '2 independent integer evaluators; 6 prime regressions')


if __name__ == '__main__':
    main()
