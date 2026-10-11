"""Bounded nonauthor check; no author code is imported or executed.

Coefficients use fresh exact integer products.  Quadratic composition uses
direct binomial coefficient extraction.  The full carrier is I+B*H, not a
recurrence with the author's nonzero seed.  All ring operations are local.
This is a task-local falsification check, not a general toolbox or a proof.
"""
from fractions import Fraction as Q
from math import prod, factorial, comb, gcd
from pathlib import Path
import json
import hashlib
import ast

PRIMES = (7, 13, 19, 31, 37, 43)
PRECISION_SOURCE = Path('/workspace/em-owner-resume-20261011/cm24-next-p3-20261011/frozen-inputs/REUSED_PRECISION_SOURCE.py')
_reuse_names = {'_require_natural', '_require_positive', 'precision_ratio',
                'project_precision', 'precision_detail', 'recompose_precision'}
_source_tree = ast.parse(PRECISION_SOURCE.read_text())
_reuse_tree = ast.Module(body=[node for node in _source_tree.body
                             if isinstance(node, ast.FunctionDef) and node.name in _reuse_names],
                        type_ignores=[])
assert len(_reuse_tree.body) == len(_reuse_names)
_precision_scope = {}
exec(compile(_reuse_tree, str(PRECISION_SOURCE), 'exec'), _precision_scope)


def unit_residue(a, modulus):
    a = Q(a)
    assert gcd(a.denominator, modulus) == 1, (a, modulus)
    return (a.numerator % modulus) * pow(a.denominator, -1, modulus) % modulus


def coefficient(n, which):
    if which == 'gauss':
        numerator = prod((6*j+1)*(3*j+1) for j in range(n))
        denominator = 18**n * factorial(n)**2
    else:
        numerator = prod((3*j+1)*(3*j+2) for j in range(n))
        denominator = 9**n * factorial(n)**2
    return Q(numerator, denominator)


def q_composition(a):
    size = 2*len(a)-1
    return [sum((a[n]*4**n*(-1)**(d-n)*comb(n, d-n)
                 for n in range((d+1)//2, min(d, len(a)-1)+1)), Q(0))
            for d in range(size)]


def hesse_residual(coeffs):
    coeffs = list(map(Q, coeffs)) + [Q(0)]
    return [((j+1)**2 * coeffs[j+1]
             - Q((3*j+1)*(3*j+2), 9)*coeffs[j])
            for j in range(len(coeffs)-1)]


def gauss_residual(coeffs):
    coeffs = list(map(Q, coeffs)) + [Q(0)]
    return [((j+1)**2*coeffs[j+1]
             - Q((6*j+1)*(3*j+1), 18)*coeffs[j])
            for j in range(len(coeffs)-1)]


def valuation(q, p):
    q = Q(q)
    assert q
    ans = 0
    for value, sign in ((abs(q.numerator), 1), (q.denominator, -1)):
        while value % p == 0:
            ans += sign
            value //= p
    return ans


def boundary_harmonic(p):
    m = (p-1)//6
    q2 = (2**(p-1)-1)//p
    s2 = sum((Q(1, 6*k+2) for k in range(m)), Q(0))
    t = {r: sum((Q(1, (6*k+r)**2) for k in range(m)), Q(0))
         for r in (2, 3, 6)}
    first = -3*s2-q2
    assert first.numerator % p == 0
    assert first.denominator % p != 0
    b = Q(2, 9)*(first/p + Q(q2*q2, 2)-3*t[6]+12*t[3]+Q(33, 2)*t[2])
    return unit_residue(b, p)


def boundary_factorial(p):
    m = (p-1)//6
    return sum(unit_residue(Q((-1)**(3*m)*factorial(m)*factorial(2*m)
                             *factorial(n-1-m)*factorial(n-1-2*m)
                             *4**n*(-1)**(p-n)*comb(n, p-n),
                             18*factorial(n)**2), p)
               for n in range(3*m+1, p)) % p


def zero_seed(p):
    out = [0]
    for j in range(p-2):
        out.append(((3*j+1)*(3*j+2)*out[-1]-2)
                   *pow(9*(j+1)**2, -1, p) % p)
    return out


def ring_add(a, b, modulus):
    return ((a[0]+b[0]) % modulus, (a[1]+b[1]) % modulus)


def ring_scale(c, a, modulus):
    return (c*a[0] % modulus, c*a[1] % modulus)


def ring_mul(a, b, modulus):
    return ((a[0]*b[0]+2*a[1]*b[1]) % modulus,
            (a[0]*b[1]+a[1]*b[0]) % modulus)


def ring_power(a, k, modulus):
    result = (1, 0)
    # This deliberately uses repeated multiplication, not the author code.
    for _ in range(k):
        result = ring_mul(result, a, modulus)
    return result


def ring_eval(coeffs, x, modulus):
    result = (0, 0)
    for a in reversed(coeffs):
        result = ring_add(ring_mul(result, x, modulus),
                          (unit_residue(a, modulus), 0), modulus)
    return result


def subtract(a, b, modulus):
    return ((a[0]-b[0]) % modulus, (a[1]-b[1]) % modulus)


def divide_ring(a, p, modulus):
    result = []
    for value in a:
        assert _precision_scope['precision_detail'](value, modulus, p*modulus) == 0
        quotient = _precision_scope['project_precision'](value, modulus, p*modulus)
        assert _precision_scope['recompose_precision'](quotient, 0, modulus, p*modulus) == value
        result.append(quotient % modulus)
    return tuple(result)


def derivative(coeffs):
    return [n*coeffs[n] for n in range(1, len(coeffs))]


def one_prime(p):
    m = (p-1)//6
    a = [coefficient(n, 'gauss') for n in range(p)]
    b = [coefficient(n, 'hesse') for n in range(p)]
    composed = q_composition(a)
    delta = [c-(b[d] if d < p else 0) for d, c in enumerate(composed)]
    assert all(d == 0 for d in delta[:p])
    residue = [unit_residue(d, p**3) for d in delta]
    boundary = boundary_harmonic(p)
    assert boundary == boundary_factorial(p)
    # Boundary extraction is a check of B, never input to its definition.
    boundary_direct = coefficient(p, 'hesse')-4**p*coefficient(p, 'gauss')
    assert valuation(boundary_direct, p) >= 2 if boundary_direct else True
    assert unit_residue(boundary_direct/p**2, p) == boundary
    i = zero_seed(p)
    h = [unit_residue(c, p) for c in b]
    assert all(c == 0 for c in h[2*m+1:])
    jcarrier = [(i[n]+boundary*h[n]) % p for n in range(p-1)]
    assert all(residue[d] == (0 if d < p else p*p*jcarrier[d-p])
               for d in range(2*p-1))
    assert all(unit_residue(d, p) == unit_residue(Q(-2, 9), p)
               for d in hesse_residual(jcarrier))
    assert all(unit_residue(d, p) == unit_residue(Q(-2, 9), p)
               for d in hesse_residual(i))
    assert all(unit_residue(d, p) == 0 for d in hesse_residual(h))
    assert valuation(a[-1], p) == valuation(b[-1], p) == 2
    assert unit_residue(a[-1]/p**2, p) == pow(10, -1, p)
    assert unit_residue(b[-1]/p**2, p) == 1
    assert jcarrier[-1] == pow(10, -1, p)
    dg = gauss_residual(a)
    dh = hesse_residual(b)
    assert all(d == 0 for d in dg[:-1]+dh[:-1])
    assert dg[-1] == -(Q(p)-Q(5, 6))*(Q(p)-Q(2, 3))*a[-1]
    assert dh[-1] == -(Q(p)-Q(2, 3))*(Q(p)-Q(1, 3))*b[-1]
    de = hesse_residual(delta)
    forcing = [Q(0)]*len(delta)
    for r in range(p):
        forcing[p-1+r] = Q(2, 9)*((1 if r == 0 else 0)
                                   - (-1)**r*comb(p-1, r))
    assert all(unit_residue(e/p**2, p) == unit_residue(v, p)
               for e, v in zip(de, forcing))
    entry_checks = []
    for k in (2*m, 4*m):
        assert jcarrier[k+1] == (-2*pow(9*(k+1)**2, -1, p)) % p
        entry_checks.append({'index': k, 'following_coefficient': jcarrier[k+1]})
    zero_seed_poly_error = [d for d, r in enumerate(residue)
                            if r != (0 if d < p else p*p*i[d-p])]
    assert bool(zero_seed_poly_error) == bool(boundary)
    result = {'prime': p, 'coefficients_checked': len(delta), 'boundary': boundary,
              'full_polynomial': 'PASS', 'harmonic_factorial_boundary': 'PASS',
              'residual_terminal_wilson': 'PASS', 'factor_entries': entry_checks,
              'zero_seed_polynomial_negative_indices': zero_seed_poly_error}
    if p in (13, 19):
        modulus = p**3
        g = unit_residue(sum((a[n]*Q(1, 2)**n for n in range(p)), Q(0)), modulus)
        gp = unit_residue(sum((n*a[n]*Q(1, 2)**(n-1) for n in range(1, p)), Q(0)), modulus)
        assert g % p == 0
        result['g_div_p_mod_p2'] = g//p
        branch_results = []
        for sign in (1, -1):
            x = (2*pow(4, -1, modulus) % modulus, sign*pow(4, -1, modulus) % modulus)
            xp = ring_power(x, p, modulus)
            sigma = (x[0] % p, (-x[1]) % p)
            assert (xp[0] % p, xp[1] % p) == sigma
            assert ring_scale(4, ring_mul(x, subtract((1, 0), x, modulus), modulus), modulus) == (pow(2, -1, modulus), 0)
            lv = ring_eval(b, x, modulus)
            assert ring_eval(h, x, p) == (0, 0)
            assert ring_eval(jcarrier, x, p) == ring_eval(i, x, p)
            correction = ring_scale(p*p, ring_mul(xp, ring_eval(jcarrier, x, modulus), modulus), modulus)
            assert ring_add(lv, correction, modulus) == (g, 0)
            second = ring_add(divide_ring(lv, p, p*p),
                              ring_scale(p, ring_mul(sigma, ring_eval(i, x, p), p*p), p*p), p*p)
            assert second == (g//p, 0)
            jacobian = ring_add((4, 0), ring_scale(-8, x, modulus), modulus)
            assert jacobian == (0, -sign*2 % modulus)
            lhs = ring_scale(gp, jacobian, modulus)
            ld = ring_eval(derivative(b), x, modulus)
            full_d = ring_scale(p*p, ring_mul(xp, ring_eval(derivative(jcarrier), x, modulus), modulus), modulus)
            assert ring_add(ld, full_d, modulus) == lhs
            omit_d = ring_scale(p*p, ring_mul(xp, ring_eval(derivative(i), x, modulus), modulus), modulus)
            derivative_error = subtract(lhs, ring_add(ld, omit_d, modulus), modulus)
            expected_error = ring_scale(p*p*boundary, ring_mul(xp, ring_eval(derivative(h), x, modulus), modulus), modulus)
            assert derivative_error == expected_error
            assert ring_eval(derivative(h), x, p) != (0, 0)
            assert (derivative_error != (0, 0)) == bool(boundary)
            uncorrected_error = subtract(lv, (g, 0), modulus)
            if p == 13:
                assert uncorrected_error == (p*p*3, p*p*(sign*10 % p))
            branch_results.append({'branch': '+' if sign == 1 else '-',
                                   'L_div_p_mod_p2': divide_ring(lv, p, p*p),
                                   'zero_seed_value': ring_eval(i, x, p),
                                   'second_digit_transport': 'PASS',
                                   'full_derivative_transport': 'PASS',
                                   'uncorrected_value_error_mod_p3': uncorrected_error,
                                   'zero_seed_derivative_error_mod_p3': derivative_error})
        result['branches'] = branch_results
    return result


if __name__ == '__main__':
    out = {'scope': 'NONAUTHOR_SHARED_NONBLIND_LOCAL_FINITE_REVIEW',
           'researcher_id': 'EM-ENTERPRISE-3F2857',
           'activity_id': 'RA-C05628958AD19A1F120F685E',
           'author_checker_model_read_imported_or_executed': False,
           'author_binding_borrowed': False,
           'precision_tool_reuse': 'COMPOSE_APPLIED_UNCHANGED_SOURCE_FUNCTIONS',
           'precision_source_sha256': hashlib.sha256(PRECISION_SOURCE.read_bytes()).hexdigest(),
           'primes': [one_prime(p) for p in PRIMES],
           'status': 'PASS_BOUNDED_REGRESSION_ONLY',
           'parent_UR_LIFT_period_normalization': 'OPEN_UNCHANGED'}
    out['implementation_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    target = Path(__file__).with_name('INDEPENDENT_FINITE_RESULTS.json')
    target.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2))
