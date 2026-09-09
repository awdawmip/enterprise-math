#!/usr/bin/env python3
"""W59A exact rational completion certificates. No pi/trig input.

Research-specific verifier, not a Foundation promotion or a new tool family.
All certificate arithmetic uses integers, Fraction and isqrt. The underlying
all-level theorem is proved in the companion research note.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
from math import isqrt, prod
import json
from pathlib import Path


def weights(m: int) -> list[Q]:
    if m < 0:
        raise ValueError('m must be nonnegative')
    c = [Q(1)]
    for r in range(1, m + 1):
        t = 4**r
        d = [Q(0)] * (len(c) + 1)
        for j, w in enumerate(c):
            d[j] -= w / (t - 1)
            d[j + 1] += t * w / (t - 1)
        c = d
    return c


def bvalue(m: int, q: int) -> int:
    if m < 0 or q < 2:
        raise ValueError('require m >= 0, q >= 2')
    return 4**m * q*q * (2*m + 4)*(2*m + 5) - (4**(m + 2)-1)//3


def upper_weights(m: int, q: int) -> list[Q]:
    a, c, b = weights(m) + [Q(0)], weights(m + 1), bvalue(m, q)
    return [(1 + Q(1, b))*v - u/b for u, v in zip(a, c)]


def sqrt_bounds(x: Q, bits: int) -> tuple[Q, Q]:
    if x < 0 or bits < 1:
        raise ValueError('nonnegative radicand and positive precision required')
    scale = 1 << bits
    n = isqrt((x.numerator * scale * scale) // x.denominator)
    lo = Q(n, scale)
    hi = lo if n*n*x.denominator == x.numerator*scale*scale else Q(n+1, scale)
    assert lo*lo <= x <= hi*hi
    return lo, hi


def outward(lo: Q, hi: Q, bits: int) -> tuple[Q, Q]:
    if lo > hi:
        raise ValueError('reversed interval')
    scale = 1 << bits
    return Q((lo.numerator*scale)//lo.denominator, scale), Q(-((-hi.numerator*scale)//hi.denominator), scale)


def mode_intervals(max_power: int, bits: int) -> list[tuple[Q, Q]]:
    """T_(2^k) enclosures for k=1,...,max_power.

    Carries s_q=T_q^2 rather than the vanishing eigenvalue a_q.
    s_(2q)=4*s_q/(2+sqrt(4-s_q/q^2)), s_2=8.
    """
    if max_power < 1:
        raise ValueError('max_power must be positive')
    s_lo = s_hi = Q(8)
    out = []
    for k in range(1, max_power + 1):
        lo = sqrt_bounds(s_lo, bits)[0]
        hi = sqrt_bounds(s_hi, bits)[1]
        out.append((lo, hi))
        if k == max_power:
            break
        q = 2**k
        xlo, xhi = 4 - s_hi/(q*q), 4 - s_lo/(q*q)
        if xlo <= 0:
            raise ArithmeticError('insufficient precision: radicand interval')
        dlo = 2 + sqrt_bounds(xlo, bits)[0]
        dhi = 2 + sqrt_bounds(xhi, bits)[1]
        s_lo, s_hi = outward(4*s_lo/dhi, 4*s_hi/dlo, bits)
    return out


def linear_interval(c: list[Q], nodes: list[tuple[Q, Q]]) -> tuple[Q, Q]:
    if len(c) != len(nodes):
        raise ValueError('coefficient/node length mismatch')
    lo = hi = Q(0)
    for w, (a, b) in zip(c, nodes):
        lo += w * (a if w >= 0 else b)
        hi += w * (b if w >= 0 else a)
    return lo, hi


def certificate(m: int, base_power: int, bits: int) -> dict:
    """m indexes the pair (E_m,E_(m+1)), not the lower endpoint level."""
    if base_power < 1:
        raise ValueError('base must be a power of two >= 2')
    q = 2**base_power
    nodes = mode_intervals(base_power + m + 1, bits)[base_power-1:]
    c, u = weights(m+1), upper_weights(m, q)
    e_lo, e_hi = linear_interval(c, nodes)
    u_lo, u_hi = linear_interval(u, nodes)
    if not e_lo < u_hi:
        raise ArithmeticError('empty output interval')
    return dict(m=m, q=q, bits=bits, b=bvalue(m,q), lower=e_lo,
                upper=u_hi, lower_rounding_width=e_hi-e_lo,
                upper_rounding_width=u_hi-u_lo,
                lower_norm=sum(map(abs,c)), upper_norm=sum(map(abs,u)),
                sqrt_bound_calls=4*(base_power+m+1)-2,
                nodes=len(nodes))


def decimal_outer(lo: Q, hi: Q, digits: int) -> tuple[int, int, int]:
    scale = 10**digits
    a = lo.numerator * scale // lo.denominator
    b = -((-hi.numerator * scale)//hi.denominator)
    return a, b, scale


def decimal_text(numerator: int, digits: int) -> str:
    s = str(numerator).zfill(digits+1)
    return s[:-digits] + '.' + s[-digits:] if digits else s


def sine_bounds(x: Q, last_even: int) -> tuple[Q, Q]:
    """Exact alternating partial-sum bracket, valid for 0 < x < 4.
    Returns P_(N-1) < S(x) < P_N for positive even N.
    """
    if not 0 < x < 4 or last_even < 2 or last_even % 2:
        raise ValueError('0<x<4 and even N>=2 required')
    term = x
    total = term
    lower = Q(0)
    for n in range(1, last_even + 1):
        term *= -x*x / ((2*n)*(2*n+1))
        total += term
        if n == last_even - 1:
            lower = total
    assert lower < total
    return lower, total


def exact_checks() -> dict:
    # Coefficient identities are finite checks, not a substitute for induction.
    for m in range(25):
        c = weights(m)
        assert sum(c) == 1
        norm = sum(map(abs, c))
        assert norm == prod((Q(4**r+1, 4**r-1) for r in range(1,m+1)), start=Q(1))
        assert norm <= Q(357,181) < 2
        for n in range(1, m+1):
            assert sum(w*Q(1,4**(j*n)) for j,w in enumerate(c)) == 0
        assert sum(w*Q(1,4**(j*(m+1))) for j,w in enumerate(c)) == (-1)**m*Q(1,4**(m*(m+1)//2))
        for q in (2,3,4,8,17,64):
            b = bvalue(m,q)
            h, C = Q(1,4**(m+1)), (2*m+4)*(2*m+5)
            kappa = Q(4,3)*(1-h)
            ratio = 4*h/(q*q*C-4*kappa)
            assert ratio == Q(1,b+1)
            u = upper_weights(m,q)
            assert sum(u) == 1
            assert sum(map(abs,u)) < 2
    # Erasing filter signs destroys the first moment annihilation.
    assert sum(abs(w)*Q(1,4**j) for j,w in enumerate(weights(1))) == Q(2,3)
    for bits in (16,32,64):
        for x in (Q(0),Q(1),Q(2),Q(8),Q(10),Q(1,17)):
            a,b = sqrt_bounds(x,bits)
            assert a*a <= x <= b*b
    return {'coefficient_levels':25, 'q_values':[2,3,4,8,17,64],
            'moment_annihilation':'PASS', 'uniform_norm':'PASS',
            'posterior_ratio_identity':'PASS', 'outward_sqrt':'PASS',
            'signed_erasure_negative_control':'PASS'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--digits', type=int, default=100)
    parser.add_argument('--output', type=Path, default=Path('w59a_certificate.json'))
    args = parser.parse_args()
    if not 1 <= args.digits <= 2000:
        parser.error('digits must be between 1 and 2000')
    checks = exact_checks()
    # 4 bits/decimal digit is conservative; extra bits absorb root rounding.
    bits = 4*args.digits + 64
    c = None
    for m in range(0, 160):
        candidate = certificate(m,1,bits)
        a,b,scale = decimal_outer(candidate['lower'],candidate['upper'],args.digits)
        if b-a == 1:
            c = candidate
            break
    if c is None:
        raise ArithmeticError('requested decimal cell not reached; increase budget')
    n = 2
    sign_result = None
    # Independent finite exact sign check, not a stored decimal constant.
    for n in range(2, 2*args.digits+40, 2):
        slo = sine_bounds(Q(a,scale),n)[0]
        shi = sine_bounds(Q(b,scale),n)[1]
        if slo > 0 and shi < 0:
            sign_result = {'last_even_index':n,'lower_partial_sum_positive':True,
                           'upper_partial_sum_negative':True}
            break
    if sign_result is None:
        raise ArithmeticError('independent rational sign certificate not reached')
    # Compact records retain exact interval data and reproducible sign settings;
    # giant polynomial numerators are checked but omitted from display payload.
    out = {**{k:(str(v) if isinstance(v,Q) else v) for k,v in c.items()},
           'digits':args.digits,'decimal_lower':decimal_text(a,args.digits),
           'decimal_upper':decimal_text(b,args.digits),
           'decimal_width':str(Q(b-a,scale)),
           'independent_sine_sign_check':sign_result, 'exact_checks':checks,
           'pi_or_trigonometric_input':False,
           'status':'FINITE_EXACT_CERTIFICATE_NOT_FOUNDATION'}
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('lower','upper')},indent=2))

if __name__ == '__main__':
    main()
