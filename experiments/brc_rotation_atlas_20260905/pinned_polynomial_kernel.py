"""Pinned pure-function reuse for the BRC factor-incidence reference experiment.

Source repository: awdawmip/enterprise-math
Commit: dc86d1d26a1374fc15cfb85c8db10f8bfbef849b
Core: src/enterprise_math/brc_critical_degeneracy.py
Blob: 8abc2ed4608bd222d16b6453e4f48f7b80566653
The polynomial and Sturm function bodies below are transcribed from the
connector-returned pure-function source. This is NOT a full-package import,
a CI run, a native arithmetic replacement, or a new arithmetic tool.
"""
from fractions import Fraction
from typing import Sequence

Poly = tuple[Fraction, ...]

def _trim(poly: Poly) -> Poly:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)

def _p_add(left: Poly, right: Poly) -> Poly:
    n = max(len(left), len(right))
    return _trim(tuple(
        (left[i] if i < len(left) else Fraction(0, 1))
        + (right[i] if i < len(right) else Fraction(0, 1))
        for i in range(n)
    ))

def _p_mul(left: Poly, right: Poly) -> Poly:
    out = [Fraction(0, 1) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return _trim(tuple(out))

def _p_scale(poly: Poly, scalar: Fraction) -> Poly:
    return _trim(tuple(scalar * value for value in poly))

def _p_eval(poly: Poly, x: Fraction) -> Fraction:
    result = Fraction(0, 1)
    for coefficient in reversed(poly):
        result = result * x + coefficient
    return result

def _p_derivative(poly: Poly) -> Poly:
    if len(poly) <= 1:
        return (Fraction(0, 1),)
    return _trim(tuple(Fraction(i, 1) * poly[i] for i in range(1, len(poly))))

def _p_divmod(numerator: Poly, denominator: Poly) -> tuple[Poly, Poly]:
    numerator = _trim(numerator)
    denominator = _trim(denominator)
    if denominator == (Fraction(0, 1),):
        raise ZeroDivisionError("zero polynomial divisor")
    if len(numerator) < len(denominator):
        return (Fraction(0, 1),), numerator
    quotient = [Fraction(0, 1) for _ in range(len(numerator) - len(denominator) + 1)]
    remainder = list(numerator)
    while len(remainder) >= len(denominator) and any(remainder):
        degree = len(remainder) - len(denominator)
        factor = remainder[-1] / denominator[-1]
        quotient[degree] += factor
        for j, value in enumerate(denominator):
            remainder[degree + j] -= factor * value
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
    return _trim(tuple(quotient)), _trim(tuple(remainder))

def _p_monic(poly: Poly) -> Poly:
    poly = _trim(poly)
    if poly == (Fraction(0, 1),):
        return poly
    return _p_scale(poly, Fraction(1, 1) / poly[-1])

def _p_gcd(left: Poly, right: Poly) -> Poly:
    left, right = _trim(left), _trim(right)
    while right != (Fraction(0, 1),):
        _, remainder = _p_divmod(left, right)
        left, right = right, remainder
    return _p_monic(left)

def _p_div_exact(poly: Poly, factor: Poly) -> Poly:
    quotient, remainder = _p_divmod(poly, factor)
    if remainder != (Fraction(0, 1),):
        raise AssertionError("polynomial division was not exact")
    return quotient

def _sturm_sequence(poly: Poly) -> tuple[Poly, ...]:
    poly = _trim(poly)
    derivative = _p_derivative(poly)
    gcd = _p_gcd(poly, derivative)
    squarefree = _p_div_exact(poly, gcd) if len(gcd) > 1 else poly
    squarefree = _trim(squarefree)
    if len(squarefree) <= 1:
        return (squarefree,)
    sequence = [squarefree, _p_derivative(squarefree)]
    while sequence[-1] != (Fraction(0, 1),):
        _, remainder = _p_divmod(sequence[-2], sequence[-1])
        if remainder == (Fraction(0, 1),):
            break
        next_poly = _p_scale(remainder, Fraction(-1, 1))
        scale = abs(next_poly[-1])
        if scale:
            next_poly = _p_scale(next_poly, Fraction(1, 1) / scale)
        sequence.append(next_poly)
    return tuple(sequence)

def _variations(sequence: Sequence[Poly], x: Fraction) -> int:
    signs: list[int] = []
    for poly in sequence:
        value = _p_eval(poly, x)
        if value > 0:
            signs.append(1)
        elif value < 0:
            signs.append(-1)
    return sum(signs[i] != signs[i - 1] for i in range(1, len(signs)))

def _root_count(sequence: Sequence[Poly], left: Fraction, right: Fraction) -> int:
    if not left < right:
        raise ValueError("root interval must have left < right")
    return _variations(sequence, left) - _variations(sequence, right)
