"""Pinned polynomial-in-parameter/Sylvester pure functions, with source provenance.
Source: awdawmip/enterprise-math@dc86d1d26a1374fc15cfb85c8db10f8bfbef849b
experiments/brc_newton_resultant_event_generator_check.py
Blob ff01133934706a309e7499d702fc0a3777e88e17.
The original reference determinant backend is subset-DP, NOT a fast
polynomial-bit-complexity resultant engine. Only these pure functions run here.
"""
from fractions import Fraction
Q = Fraction
TPoly = tuple[Fraction, ...]
XPoly = tuple[TPoly, ...]
ZERO: TPoly = (Q(0),)
ONE: TPoly = (Q(1),)

def t_trim(poly: TPoly) -> TPoly:
    values = list(poly) if poly else [Q(0)]
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)

def t_const(value) -> TPoly:
    return (Q(value),)

def t_add(a: TPoly, b: TPoly) -> TPoly:
    n = max(len(a), len(b))
    return t_trim(tuple((a[i] if i < len(a) else Q(0)) + (b[i] if i < len(b) else Q(0)) for i in range(n)))

def t_scale(poly: TPoly, scalar) -> TPoly:
    return t_trim(tuple(Q(scalar) * value for value in poly))

def t_mul(a: TPoly, b: TPoly) -> TPoly:
    out = [Q(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return t_trim(tuple(out))

def t_eval(poly: TPoly, value: Fraction) -> Fraction:
    out = Q(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out

def t_divmod(a: TPoly, b: TPoly):
    a, b = t_trim(a), t_trim(b)
    if b == ZERO:
        raise ZeroDivisionError
    if len(a) < len(b):
        return ZERO, a
    quotient = [Q(0) for _ in range(len(a) - len(b) + 1)]
    remainder = list(a)
    while len(remainder) >= len(b) and any(remainder):
        degree = len(remainder) - len(b)
        factor = remainder[-1] / b[-1]
        quotient[degree] += factor
        for j, coefficient in enumerate(b):
            remainder[degree + j] -= factor * coefficient
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
    return t_trim(tuple(quotient)), t_trim(tuple(remainder))

def t_div_exact(a: TPoly, b: TPoly) -> TPoly:
    q, r = t_divmod(a, b)
    assert r == ZERO
    return q

def x_trim(poly: XPoly) -> XPoly:
    values = list(poly)
    while len(values) > 1 and t_trim(values[-1]) == ZERO:
        values.pop()
    return tuple(t_trim(value) for value in values)

def x_derivative(poly: XPoly) -> XPoly:
    poly = x_trim(poly)
    if len(poly) <= 1:
        return (ZERO,)
    return x_trim(tuple(t_scale(poly[i], i) for i in range(1, len(poly))))

def x_eval(poly: XPoly, value: Fraction) -> TPoly:
    out = ZERO
    power = Q(1)
    for coefficient in poly:
        out = t_add(out, t_scale(coefficient, power))
        power *= value
    return out

def x_mul(a: XPoly, b: XPoly) -> XPoly:
    out = [ZERO for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = t_add(out[i + j], t_mul(x, y))
    return x_trim(tuple(out))

def determinant_poly_matrix(matrix: tuple[tuple[TPoly, ...], ...]) -> TPoly:
    n = len(matrix)
    assert n > 0 and all(len(row) == n for row in matrix)
    dp: dict[int, TPoly] = {0: ONE}
    for row in range(n):
        nxt: dict[int, TPoly] = {}
        for mask, partial in dp.items():
            assert mask.bit_count() == row
            for column in range(n):
                if mask & (1 << column):
                    continue
                entry = matrix[row][column]
                if entry == ZERO:
                    continue
                inversions_with_prior = (mask >> (column + 1)).bit_count()
                term = t_mul(partial, entry)
                if inversions_with_prior % 2:
                    term = t_scale(term, -1)
                target = mask | (1 << column)
                nxt[target] = t_add(nxt.get(target, ZERO), term)
        dp = nxt
    return t_trim(dp.get((1 << n) - 1, ZERO))

def sylvester_resultant(p: XPoly, q: XPoly) -> TPoly:
    p, q = x_trim(p), x_trim(q)
    if p == (ZERO,) or q == (ZERO,):
        return ZERO
    m, n = len(p) - 1, len(q) - 1
    size = m + n
    if size == 0:
        return ONE
    p_desc = tuple(reversed(p))
    q_desc = tuple(reversed(q))
    rows: list[tuple[TPoly, ...]] = []
    for shift in range(n):
        row = [ZERO for _ in range(size)]
        for j, coefficient in enumerate(p_desc):
            row[shift + j] = coefficient
        rows.append(tuple(row))
    for shift in range(m):
        row = [ZERO for _ in range(size)]
        for j, coefficient in enumerate(q_desc):
            row[shift + j] = coefficient
        rows.append(tuple(row))
    return determinant_poly_matrix(tuple(rows))

def resultant_event_factor(poly: XPoly) -> TPoly:
    return sylvester_resultant(poly, x_derivative(poly))
