"""Task-local exact regression for the finite Gauss/Hesse p^2 comparison.

Executed only after this researcher's own actual execution-open:
RUN-725aa319e999e96ac1a99acb / MCP-634560f210aa28118cb281a0 / epoch6109143010.
Finite regressions are not the all-prime proof or a UR/LIFT proof.
No network, provider request, task mutation, or general toolbox registration.
"""
from __future__ import annotations

import ast
from fractions import Fraction as F
from hashlib import sha256
from math import comb
import json
from pathlib import Path

PRIMES = [7, 13, 19, 31, 37, 43, 61, 67, 73, 97]
ROOT = Path(__file__).resolve().parent


def coeffs(a, b, p):
    out = [F(1)]
    for n in range(p - 1):
        out.append(out[-1] * (a + n) * (b + n) / (n + 1)**2)
    return out


def vp_int(n, p):
    if n == 0:
        return None
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def vp(c, p):
    return vp_int(c.numerator, p) - vp_int(c.denominator, p)


def mod_fraction(c, modulus):
    return c.numerator % modulus * pow(c.denominator, -1, modulus) % modulus


def compose_quadratic(a):
    # Exact Q polynomial coefficients: a_n (4X(1-X))^n.
    out = [F(0)] * (2 * len(a) - 1)
    for n, c in enumerate(a):
        for r in range(n + 1):
            out[n + r] += c * 4**n * (-1)**r * comb(n, r)
    return out


def reflect_coeffs(b):
    out = [F(0)] * len(b)
    for n, c in enumerate(b):
        for k in range(n + 1):
            out[k] += c * (-1)**k * comb(n, k)
    return out


def mul(a, b, modulus):
    # R=(Z/modulus)[S]/(S^2-2), retaining both coefficients.
    return ((a[0]*b[0] + 2*a[1]*b[1]) % modulus,
            (a[0]*b[1] + a[1]*b[0]) % modulus)


def add(a, b, modulus):
    return ((a[0]+b[0]) % modulus, (a[1]+b[1]) % modulus)


def scalar(c, modulus):
    return (mod_fraction(F(c), modulus), 0)


def power(a, n, modulus):
    out = (1, 0)
    while n:
        if n & 1:
            out = mul(out, a, modulus)
        a = mul(a, a, modulus)
        n >>= 1
    return out


def evaluate(b, x, modulus):
    out = (0, 0)
    for c in reversed(b):
        out = add(mul(out, x, modulus), scalar(c, modulus), modulus)
    return out


def derivative(b):
    return [n*c for n, c in enumerate(b)][1:]


def difference(a, b, modulus):
    return ((a[0]-b[0]) % modulus, (a[1]-b[1]) % modulus)


def sigma(a, modulus):
    return (a[0], -a[1] % modulus)


def divide_p(a, p):
    assert all(v % p == 0 for v in a)
    return tuple(v // p % p for v in a)


def reused_precision_functions():
    # Execute these exact, unchanged functions from the fully pinned Source
    # precision.py, without importing unrelated core/root helpers.
    src = (ROOT / 'REUSED_PRECISION_SOURCE.py').read_text()
    assert sha256(src.encode()).hexdigest() == 'd8a19c7e4a319b5e9b17b66a1b5ef4ac563bd984815c7355bd73784e0bc521d8'
    names = {'_require_natural', '_require_positive', 'precision_ratio',
             'project_precision', 'precision_detail', 'recompose_precision'}
    tree = ast.parse(src)
    nodes = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
    assert {n.name for n in nodes} == names
    ns = {}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), 'Source precision.py exact functions', 'exec'), ns)
    return ns, sha256(src.encode()).hexdigest()


def check_prime(p, precision):
    m = (p - 1) // 6
    assert p == 6*m + 1
    a = coeffs(F(1, 6), F(1, 3), p)
    b = coeffs(F(1, 3), F(2, 3), p)
    assert all(c.denominator % p for c in a + b)
    expected_a = [int(n > m) + int(n > 2*m) for n in range(p)]
    expected_b = [int(n > 2*m) + int(n > 4*m) for n in range(p)]
    assert [vp(c, p) for c in a] == expected_a
    assert [vp(c, p) for c in b] == expected_b
    composed = compose_quadratic(a)
    padded_b = b + [F(0)] * (p - 1)
    # Below p, the full characteristic-zero identity needs no missing n>=p.
    assert composed[:p] == b
    delta = [c-d for c, d in zip(composed, padded_b)]
    nonzero_delta_vp = [vp(c, p) for c in delta if c]
    assert all(v >= 2 for v in nonzero_delta_vp)
    assert vp(delta[-1], p) == 2
    mod2, mod3 = p*p, p*p*p
    assert all(mod_fraction(c, mod2) == 0 for c in delta)
    assert mod_fraction(delta[-1], mod3) != 0
    assert all(mod_fraction(c-d, mod2) == 0 for c, d in zip(reflect_coeffs(b), b))
    g = sum(c * F(1, 2)**n for n, c in enumerate(a))
    fp = sum(n*c*F(1, 2)**(n-1) for n, c in enumerate(a) if n)
    h = sum((12*n+1)*c*F(1, 2)**n for n, c in enumerate(a))
    assert h == g + 6*fp
    xplus = (pow(2, -1, mod2), pow(4, -1, mod2))
    xminus = sigma(xplus, mod2)
    one_minus_plus = difference((1, 0), xplus, mod2)
    assert one_minus_plus == xminus
    q = mul(scalar(4, mod2), mul(xplus, xminus, mod2), mod2)
    assert q == scalar(F(1, 2), mod2)
    vals, slopes, qslopes = [], [], []
    for x in [xplus, xminus]:
        lx = evaluate(b, x, mod2)
        qprime = mul(scalar(4, mod2), difference((1, 0), mul(scalar(2, mod2), x, mod2), mod2), mod2)
        lp = evaluate(derivative(b), x, mod2)
        assert lx == scalar(g, mod2)
        assert lp == mul(qprime, scalar(fp, mod2), mod2)
        vals.append(lx); slopes.append(lp); qslopes.append(qprime)
    assert sigma(slopes[0], mod2) == slopes[1]
    assert add(slopes[0], slopes[1], mod2) == (0, 0)
    assert qslopes[0] == (0, -2 % mod2)
    assert qslopes[1] == (0, 2)
    target = p % 24 in [13, 19]
    digit = None
    shift = None
    if target:
        assert g.numerator % p == 0
        digit = mod_fraction(g / p, p)
        assert divide_p(vals[0], p) == divide_p(vals[1], p) == (digit, 0)
        # Reuse exact integer precision projection/detail/recomposition.
        representative = mod_fraction(g, mod2)
        d = precision['project_precision'](representative, p, mod2)
        detail = precision['precision_detail'](representative, p, mod2)
        assert d == digit and detail == 0
        assert precision['recompose_precision'](d, detail, p, mod2) == representative
        assert mod_fraction(fp, p) != 0  # inherited SIMPLE, finite check only
        shifted_g = sum(c * (F(1, 2) + p)**n for n, c in enumerate(a))
        shifted_digit = mod_fraction(shifted_g / p, p)
        assert shifted_digit == (digit + mod_fraction(fp, p)) % p
        assert shifted_digit != digit
        shifted_x = add(xplus, scalar(p, mod2), mod2)
        lshift = evaluate(b, shifted_x, mod2)
        assert divide_p(lshift, p) == add((digit, 0), (slopes[0][0] % p, slopes[0][1] % p), p)
        shift = {'rational_delta': 1, 'digit_at_rational_half': digit,
                 'digit_at_rational_half_plus_p': shifted_digit,
                 'fprime_half_mod_p': mod_fraction(fp, p),
                 'Hesse_x_shift_epsilon': [1, 0], 'shifted_Hesse_digit': divide_p(lshift, p)}
    frob_difference = difference(power(xplus, p, mod2), xminus, mod2)
    literal_frob_digit = None
    if pow(2, (p-1)//2, p) == p-1:
        assert all(c % p == 0 for c in frob_difference)
        if target:
            epsilon = divide_p(frob_difference, p)
            literal_frob_digit = divide_p(evaluate(b, power(xplus, p, mod2), mod2), p)
            predicted = add((digit, 0), mul(epsilon, tuple(v % p for v in slopes[1]), p), p)
            assert literal_frob_digit == predicted
    # At p^3 this truncation bridge is deliberately tested as a negative
    # precision extension, not silently used to obtain G_p modulo p^2.
    xplus3 = (pow(2, -1, mod3), pow(4, -1, mod3))
    value_difference3 = difference(evaluate(b, xplus3, mod3), scalar(g, mod3), mod3)
    return {'p': p, 'm': m, 'p_mod_24': p % 24, 'target': target,
            'denominators_units': True, 'valuation_boundaries': {'Gauss': [m, 2*m], 'Hesse': [2*m, 4*m]},
            'coefficient_identity_below_p_exact': True, 'coefficient_mod_p2_all': True,
            'reflection_mod_p2': True, 'minimum_nonzero_polynomial_difference_valuation': min(nonzero_delta_vp),
            'highest_coefficient_mod_p3_nonzero': mod_fraction(delta[-1], mod3),
            'g_mod_p2': mod_fraction(g, mod2), 'first_divided_digit_mod_p': digit,
            'branch_values_mod_p2': vals, 'branch_derivatives_mod_p2': slopes,
            'branch_map_derivatives_mod_p2': qslopes, 'rational_shift': shift,
            'literal_p_power_minus_sigma_mod_p2': frob_difference,
            'digit_at_literal_p_power_lift': literal_frob_digit,
            'Hesse_minus_Gauss_exact_half_mod_p3': value_difference3}


def excluded_small_prime_counterexample():
    p = 5
    a = coeffs(F(1, 6), F(1, 3), p)
    b = coeffs(F(1, 3), F(2, 3), p)
    delta = [c-d for c,d in zip(compose_quadratic(a), b+[F(0)]*(p-1))]
    nonzero = [(k, mod_fraction(c, p*p)) for k,c in enumerate(delta) if mod_fraction(c, p*p)]
    assert nonzero
    return {'p': 5, 'excluded_reason': 'p is not 1 mod 6; no integer m=(p-1)/6',
            'coefficient_mod_25_failure': nonzero}


def main():
    precision, precision_source_sha = reused_precision_functions()
    results = [check_prime(p, precision) for p in PRIMES]
    out = {'scope': 'TEN_SELECTED_PRIMES_EXACT_REGRESSION_NOT_ALL_PRIME_PROOF_OR_UR_LIFT',
           'status': 'PASS', 'selected_primes': PRIMES, 'cases': results,
           'excluded_p5_negative': excluded_small_prime_counterexample(),
           'reused_precision_source_sha256': precision_source_sha,
           'positive_mod_p2_cases': len(results), 'target_divided_digit_cases': sum(r['target'] for r in results),
           'polynomial_mod_p3_negative_cases': len(results),
           'literal_p_power_is_sigma_mod_p2': False,
           'period_normal_identified': False, 'UR_proved': False, 'LIFT_proved': False}
    (ROOT/'QUADRATIC_EXACT_REGRESSION_RESULTS.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k != 'cases'}, indent=2))


if __name__ == '__main__':
    main()
